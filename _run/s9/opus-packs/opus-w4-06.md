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

## GROUP: _overhaul2/lake/cases/Florida v. Riley.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Riley"
type: case
citation: "488 U.S. 445 (1989)"
parallel_cite: "109 S. Ct. 693; 102 L. Ed. 2d 835"
neutral_cite: 1989 U.S. LEXIS 580
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-04-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: null
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Riley
  varies_by_point: false
  scope_note: "Controlling plurality (White, J.), with O'Connor, J., concurring in the judgment on a public-use rationale. Good law; the naked-eye-from-lawful-public-airspace holding governs aerial observation."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112175/florida-v-riley/"
  cluster_id: 112175
  opinion_id: 112175
  identity_checked: true
homes:
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Key — Anchor"
related: ["[[California v. Ciraolo]]", "[[Dow Chemical Co. v. United States]]", "[[Kyllo v. United States]]", "[[United States v. Dunn]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "aerial-surveillance", "curtilage", "helicopter"]
holding: "Naked-eye observation of a backyard greenhouse from a helicopter lawfully in public airspace at 400 feet is not a search."
lake:
  record_id: Florida v. Riley
  status: verified
  projected_at: 2026-07-09
---

# Florida v. Riley

*488 U.S. 445 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Acting on a tip, an officer circled Riley's property in a helicopter at 400 feet and, through openings in the roof and sides of a greenhouse in the [[Curtilage|curtilage]] behind Riley's mobile home, saw with the naked eye what he believed to be marijuana. That observation supported a warrant. Riley moved to suppress, arguing the aerial observation of his [[Curtilage|curtilage]] was a search.

## Issue
Whether naked-eye observation of the [[Curtilage|curtilage]] of a home, made from a helicopter lawfully operating in public navigable airspace at an altitude of 400 feet, constitutes a Fourth Amendment search.

## Rule
No (plurality). Because helicopters may lawfully fly that low, the vantage point was one available to the public: "Any member of the public could legally have been flying over Riley's property in a helicopter at the altitude of 400 feet and could have observed Riley's greenhouse." — 488 U.S. at 451 (plurality opinion). ^pin-451

The plurality concluded: "As far as this record reveals, no intimate details connected with the use of the home or curtilage were observed, and there was no undue noise, and no wind, dust, or threat of injury. In these circumstances, there was no violation of the Fourth Amendment." — [*Id.* at 452](https://www.courtlistener.com/opinion/112175/florida-v-riley/#:~:text=As%20far%20as%20this%20record%20reveals%2C%20no%20intimate%20details%20connected%20with%20the%20use%20of%20the%20home%20or%20curtilage%20were%20observed%2C%20and%20there%20was%20no%20undue%20noise%2C%20and%20no%20wind%2C%20dust%2C%20or%20threat%20of%20injury.%20In%20these%20circumstances%2C%20there%20was%20no%20violation%20of%20the%20Fourth%20Amendment.,-The). ^pin-452

## Application
The officer used only his naked eye, from a height (400 feet) at which helicopter flight was lawful and at which any member of the public could have been present. The contents of the greenhouse were visible through gaps Riley had left in its roof and sides. No intimate details of the home were observed, and the overflight caused no wind, dust, undue noise, or threat of injury. On those facts the plurality found no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] invaded; Justice O'Connor concurred in the judgment, reasoning that what mattered was whether public travel at that altitude was sufficiently routine rather than mere compliance with FAA floor regulations.

## Conclusion
The aerial observation was not a search; the Florida Supreme Court's suppression was reversed. Extending [[California v. Ciraolo]] to rotary-wing aircraft, the case holds that naked-eye observation of [[Curtilage|curtilage]] from lawful public airspace is not a Fourth Amendment search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (controlling plurality).
- Follows [[California v. Ciraolo]] and the open-areas reasoning of [[Dow Chemical Co. v. United States]]. The home-interior, technology-enhanced line is governed instead by [[Kyllo v. United States]] (2001), which the plurality's "intimate details" caveat foreshadows.

## Appears on
- [[Aerial and Enhanced Surveillance]] — *Key — Anchor*

## Sources
- *Florida v. Riley*, 488 U.S. 445 (1989) — https://www.courtlistener.com/opinion/112175/florida-v-riley/ — pinpoints: 451, 452.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6493a0f000596759", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Riley"}, "payload": {"all": [{"cite": "488 U.S. 445", "page": "445", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "488"}, {"cite": "109 S. Ct. 693", "page": "693", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "102 L. Ed. 2d 835", "page": "835", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "1989 U.S. LEXIS 580", "page": "580", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}], "display": "488 U.S. 445", "official": {"cite": "488 U.S. 445", "page": "445", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "488"}, "official_selection_present": true, "record_id": "Florida v. Riley"}}
{"assertion_id": "3b986ff999357939", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-452", "record_id": "Florida v. Riley"}, "payload": {"fragment": "#:~:text=As%20far%20as%20this%20record%20reveals%2C%20no%20intimate%20details%20connected%20with%20the%20use%20of%20the%20home%20or%20curtilage%20were%20observed%2C%20and%20there%20was%20no%20undue%20noise%2C%20and%20no%20wind%2C%20dust%2C%20or%20threat%20of%20injury.%20In%20these%20circumstances%2C%20there%20was%20no%20violation%20of%20the%20Fourth%20Amendment.,-The", "page": null, "pin_id": "pin-452", "pinpoint_status": "star-verified", "quote": "As far as this record reveals, no intimate details connected with the use of the home or curtilage were observed, and there was no undue noise, and no wind, dust, or threat of injury. In these circumstances, there was no violation of the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "Florida v. Riley", "star_marker": "452"}}
{"assertion_id": "c1124d7d57b6c69b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-451", "record_id": "Florida v. Riley"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-451", "pinpoint_status": "slip-only", "quote": "--- # Florida v. Riley *488 U.S. 445 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, an officer circled Riley's property in a helicopter at 400 feet and, through openings in the roof and sides of a greenhouse in the curtilage behind Riley's mobile home, saw with the naked eye what he believed to be marijuana. That observation supported a warrant. Riley moved to suppress, arguing the aerial observation of his curtilage was a search. ## Issue Whether naked-eye observation of the curtilage of a home, made from a helicopter lawfully operating in public navigable airspace at an altitude of 400 feet, constitutes a Fourth Amendment search. ## Rule No (plurality). Because helicopters may lawfully fly that low, the vantage point was one available to the public:", "quote_fidelity": "mismatch", "record_id": "Florida v. Riley", "star_marker": null}}
{"assertion_id": "46f8181040551a54", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Riley"}, "payload": {"as_of_content": null, "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Riley", "scope_note": "Controlling plurality (White, J.), with O'Connor, J., concurring in the judgment on a public-use rationale. Good law; the naked-eye-from-lawful-public-airspace holding governs aerial observation.", "varies_by_point": false}}
```

### lake record — Florida v. Riley

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Riley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Riley",
    "case_name_short": "Riley",
    "case_name_full": "Florida v. Riley",
    "input_case_name": "Florida v. Riley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-04-03",
    "year": 1989,
    "docket": null,
    "cluster_id": 112175,
    "lead_opinion_id": 112175,
    "sibling_ids": [
      112175,
      9431518,
      9431519,
      9431520,
      9431521
    ],
    "absolute_url": "/opinion/112175/florida-v-riley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9086444,
        "score": 20,
        "case_name": "Florida v. Riley"
      },
      {
        "cluster_id": 9086443,
        "score": 20,
        "case_name": "Florida v. Riley"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "488 U.S. 445",
      "volume": "488",
      "reporter": "U.S.",
      "page": "445",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 693",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "693",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 835",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "835",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 580",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "580",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "488 U.S. 445",
        "volume": "488",
        "reporter": "U.S.",
        "page": "445",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 693",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "693",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 835",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "835",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 580",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "580",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "488 U.S. 445",
    "official_selection": {
      "court_class": "scotus",
      "selected": "488 U.S. 445",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-451",
      "page": null,
      "quote": "--- # Florida v. Riley *488 U.S. 445 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Acting on a tip, an officer circled Riley's property in a helicopter at 400 feet and, through openings in the roof and sides of a greenhouse in the curtilage behind Riley's mobile home, saw with the naked eye what he believed to be marijuana. That observation supported a warrant. Riley moved to suppress, arguing the aerial observation of his curtilage was a search. ## Issue Whether naked-eye observation of the curtilage of a home, made from a helicopter lawfully operating in public navigable airspace at an altitude of 400 feet, constitutes a Fourth Amendment search. ## Rule No (plurality). Because helicopters may lawfully fly that low, the vantage point was one available to the public:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-452",
      "page": null,
      "quote": "As far as this record reveals, no intimate details connected with the use of the home or curtilage were observed, and there was no undue noise, and no wind, dust, or threat of injury. In these circumstances, there was no violation of the Fourth Amendment.",
      "star_marker": "452",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10550,
      "fragment": "#:~:text=As%20far%20as%20this%20record%20reveals%2C%20no%20intimate%20details%20connected%20with%20the%20use%20of%20the%20home%20or%20curtilage%20were%20observed%2C%20and%20there%20was%20no%20undue%20noise%2C%20and%20no%20wind%2C%20dust%2C%20or%20threat%20of%20injury.%20In%20these%20circumstances%2C%20there%20was%20no%20violation%20of%20the%20Fourth%20Amendment.,-The",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": null,
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Riley",
    "varies_by_point": false,
    "scope_note": "Controlling plurality (White, J.), with O'Connor, J., concurring in the judgment on a public-use rationale. Good law; the naked-eye-from-lawful-public-airspace holding governs aerial observation.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bauder",
          "cluster_id": 8345070,
          "cite": [
            "181 Vt. 392",
            "2007 Vt. 16",
            "2007 VT 16",
            "924 A.2d 38",
            "2007 Vt. LEXIS 45"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cavely",
          "cluster_id": 163041,
          "cite": [
            "318 F.3d 987",
            "60 Fed. R. Serv. 1052",
            "2003 U.S. App. LEXIS 1912",
            "2003 WL 245628"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane1_negative"
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
        "journal_ref": "Florida v. Riley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kirchoff",
          "cluster_id": 2202269,
          "cite": [
            "587 A.2d 988",
            "156 Vt. 1",
            "1991 Vt. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 6069456,
          "cite": [
            "169 A.D.2d 1023"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lockhart v. Fretwell",
          "cluster_id": 112807,
          "cite": [
            "122 L. Ed. 2d 180",
            "113 S. Ct. 838",
            "506 U.S. 364",
            "1993 U.S. LEXIS 1016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
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
        "journal_ref": "Florida v. Riley:lane2_top_cited"
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
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Webster v. Reproductive Health Services",
          "cluster_id": 112330,
          "cite": [
            "106 L. Ed. 2d 410",
            "109 S. Ct. 3040",
            "492 U.S. 490",
            "1989 U.S. LEXIS 3290",
            "57 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bond v. United States",
          "cluster_id": 118354,
          "cite": [
            "146 L. Ed. 2d 365",
            "120 S. Ct. 1462",
            "529 U.S. 334",
            "2000 U.S. LEXIS 2520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
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
        "journal_ref": "Florida v. Riley:lane2_top_cited"
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
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Fields Christopher Crawley",
          "cluster_id": 740479,
          "cite": [
            "113 F.3d 313",
            "1997 U.S. App. LEXIS 10728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Broderick",
          "cluster_id": 2967256,
          "cite": [
            "225 F.3d 440",
            "2000 U.S. App. LEXIS 22165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hector Hernan Hoyos",
          "cluster_id": 534551,
          "cite": [
            "892 F.2d 1387"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re the United States",
          "cluster_id": 8441402,
          "cite": [
            "724 F.3d 600",
            "58 Communications Reg. (P&F) 1292",
            "2013 WL 3914484",
            "2013 U.S. App. LEXIS 15510"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neil Morgan v. Fairfield Cty., Ohio",
          "cluster_id": 4532978,
          "cite": [
            "903 F.3d 553"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Betts, Tony",
          "cluster_id": 2948317,
          "cite": [
            "397 S.W.3d 198",
            "2013 WL 1628963",
            "2013 Tex. Crim. App. LEXIS 705"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. LeFlore",
          "cluster_id": 2812402,
          "cite": [
            "2015 IL 116799"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. DeFusco",
          "cluster_id": 7895140,
          "cite": [
            "224 Conn. 627",
            "620 A.2d 746",
            "1993 Conn. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wacker",
          "cluster_id": 1364515,
          "cite": [
            "856 P.2d 1029",
            "317 Or. 419",
            "1993 Ore. LEXIS 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Noel C. Jenkins (96-5338) Linda L. Jenkins (96-5346)",
          "cluster_id": 746252,
          "cite": [
            "124 F.3d 768"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Julio Gori, Sorin Pichardo and Victor Rosario",
          "cluster_id": 770836,
          "cite": [
            "230 F.3d 44",
            "2000 U.S. App. LEXIS 25974"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Riley:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112175 OR 9431518 OR 9431519 OR 9431520 OR 9431521) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 149,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 149,
        "triage_read": 7,
        "triage_snippet_classified": 142
      },
      "lane2_top_cited": {
        "query": "cites:(112175 OR 9431518 OR 9431519 OR 9431520 OR 9431521)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTU5MzMxNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112175+OR+9431518+OR+9431519+OR+9431520+OR+9431521%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112175 OR 9431518 OR 9431519 OR 9431520 OR 9431521)",
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
    "complete_query": "cites:(112175 OR 9431518 OR 9431519 OR 9431520 OR 9431521)",
    "indexed_citing_opinions": 203,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112175,
        "count": 171,
        "count_source": "search"
      },
      {
        "opinion_id": 9431518,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9431519,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431520,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431521,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 345,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-riley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY1NTE5MzMmcz00NjgyNTI5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112175+OR+9431518+OR+9431519+OR+9431520+OR+9431521%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112175,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 1113918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112175,
        "cited_id": 1743339,
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
    "date_created": "2026-07-05T04:22:26Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:22:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:22:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:25:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:22:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Riley

```
<div>
<center><b><span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">488 U.S. 445</a></span> (1989)</b></center>
<center><h1>FLORIDA<br>
v.<br>
RILEY</h1></center>
<center>No. 87-764.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 3, 1988</center>
<center>Decided January 23, 1989</center>
CERTIORARI TO THE SUPREME COURT OF FLORIDA
<p><span class="star-pagination">*446</span> <i>Parker D. Thomson,</i> Special Assistant Attorney General of Florida, argued the cause for petitioner. With him on the briefs were <i>Robert A. Butterworth,</i> Attorney General, <span class="star-pagination">*447</span> <i>Candace M. Sunderland</i> and <i>Peggy A. Quince,</i> Assistant Attorneys General, and <i>Cloyce L. Mangas, Jr.,</i> Special Assistant Attorney General.</p>
<p><i>Marc H. Salton</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><i>Ronald M. Sinoway</i> filed a brief for the California Attorneys for Criminal Justice et al. as <i>amici curiae.</i></p>
<p>JUSTICE WHITE announced the judgment of the Court and delivered an opinion, in which THE CHIEF JUSTICE, JUSTICE SCALIA, and JUSTICE KENNEDY join.</p>
<p>On certification to it by a lower state court, the Florida Supreme Court addressed the following question: "Whether surveillance of the interior of a partially covered greenhouse <span class="star-pagination">*448</span> in a residential backyard from the vantage point of a helicopter located 400 feet above the greenhouse constitutes a `search' for which a warrant is required under the Fourth Amendment and Article I, § 12 of the Florida Constitution." <span class="citation multiple-matches"><a href="/c/So.%202d/511/282/">511 So. 2d 282</a></span> (1987). The court answered the question in the affirmative, and we granted the State's petition for certiorari challenging that conclusion. <span class="citation multiple-matches"><a href="/c/U.%20S./484/1058/">484 U. S. 1058</a></span> (1988).<sup>[1]</sup></p>
<p>Respondent Riley lived in a mobile home located on five acres of rural property. A greenhouse was located 10 to 20 feet behind the mobile home. Two sides of the greenhouse were enclosed. The other two sides were not enclosed but the contents of the greenhouse were obscured from view from surrounding property by trees, shrubs, and the mobile home. The greenhouse was covered by corrugated roofing panels, some translucent and some opaque. At the time relevant to this case, two of the panels, amounting to approximately 10% of the roof area, were missing. A wire fence surrounded the mobile home and the greenhouse, and the property was posted with a "DO NOT ENTER" sign.</p>
<p>This case originated with an anonymous tip to the Pasco County Sheriff's office that marijuana was being grown on respondent's property. When an investigating officer discovered that he could not see the contents of the greenhouse from the road, he circled twice over respondent's property in a helicopter at the height of 400 feet. With his naked eye, he was able to see through the openings in the roof and one or more of the open sides of the greenhouse and to identify what he thought was marijuana growing in the structure. A warrant <span class="star-pagination">*449</span> was obtained based on these observations, and the ensuing search revealed marijuana growing in the greenhouse. Respondent was charged with possession of marijuana under Florida law. The trial court granted his motion to suppress; the Florida Court of Appeals reversed but certified the case to the Florida Supreme Court, which quashed the decision of the Court of Appeals and reinstated the trial court's suppression order.</p>
<p>We agree with the State's submission that our decision in <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986), controls this case. There, acting on a tip, the police inspected the backyard of a particular house while flying in a fixed-wing aircraft at 1,000 feet. With the naked eye the officers saw what they concluded was marijuana growing in the yard. A search warrant was obtained on the strength of this airborne inspection, and marijuana plants were found. The trial court refused to suppress this evidence, but a state appellate court held that the inspection violated the Fourth and Fourteenth Amendments to the United States Constitution, and that the warrant was therefore invalid. We in turn reversed, holding that the inspection was not a search subject to the Fourth Amendment. We recognized that the yard was within the curtilage of the house, that a fence shielded the yard from observation from the street, and that the occupant had a subjective expectation of privacy. We held, however, that such an expectation was not reasonable and not one "that society is prepared to honor." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#214" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 214</a></span>. Our reasoning was that the home and its curtilage are not necessarily protected from inspection that involves no physical invasion. " `What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection.' " <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 213</a></span>, quoting <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967). As a general proposition, the police may see what may be seen "from a public vantage point where [they have] a right to be," <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo">476 U. S., at 213</a></span>. Thus the police, like the public, would have been free to inspect the backyard garden from <span class="star-pagination">*450</span> the street if their view had been unobstructed. They were likewise free to inspect the yard from the vantage point of an aircraft flying in the navigable airspace as this plane was. "In an age where private and commercial flight in the public airways is routine, it is unreasonable for respondent to expect that his marijuana plants were constitutionally protected from being observed with the naked eye from an altitude of 1,000 feet. The Fourth Amendment simply does not require the police traveling in the public airways at this altitude to obtain a warrant in order to observe what is visible to the naked eye." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 215</a></span>.</p>
<p>We arrive at the same conclusion in the present case. In this case, as in <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>,</i> the property surveyed was within the curtilage of respondent's home. Riley no doubt intended and expected that his greenhouse would not be open to public inspection, and the precautions he took protected against ground-level observation. Because the sides and roof of his greenhouse were left partially open, however, what was growing in the greenhouse was subject to viewing from the air. Under the holding in <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>,</i> Riley could not reasonably have expected the contents of his greenhouse to be immune from examination by an officer seated in a fixed-wing aircraft flying in navigable airspace at an altitude of 1,000 feet or, as the Florida Supreme Court seemed to recognize, at an altitude of 500 feet, the lower limit of the navigable airspace for such an aircraft. 511 So. 2d, at 288. Here, the inspection was made from a helicopter, but as is the case with fixed-wing planes, "private and commercial flight [by helicopter] in the public airways is routine" in this country, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Ciraolo, supra,</i> at 215</a></span>, and there is no indication that such flights are unheard of in Pasco County, Florida.<sup>[2]</sup> Riley could not reasonably <span class="star-pagination">*451</span> have expected that his greenhouse was protected from public or official observation from a helicopter had it been flying within the navigable airspace for fixed-wing aircraft.</p>
<p>Nor on the facts before us, does it make a difference for Fourth Amendment purposes that the helicopter was flying at 400 feet when the officer saw what was growing in the greenhouse through the partially open roof and sides of the structure. We would have a different case if flying at that altitude had been contrary to law or regulation. But helicopters are not bound by the lower limits of the navigable airspace allowed to other aircraft.<sup>[3]</sup> Any member of the public could legally have been flying over Riley's property in a helicopter at the altitude of 400 feet and could have observed Riley's greenhouse. The police officer did no more. This is not to say that an inspection of the curtilage of a house from an aircraft will always pass muster under the Fourth Amendment simply because the plane is within the navigable airspace specified by law. But it is of obvious importance that the helicopter in this case was <i>not</i> violating the law, and there is nothing in the record or before us to suggest that helicopters flying at 400 feet are sufficiently rare in this country to lend substance to respondent's claim that he reasonably anticipated that his greenhouse would not be subject to <span class="star-pagination">*452</span> observation from that altitude. Neither is there any intimation here that the helicopter interfered with respondent's normal use of the greenhouse or of other parts of the curtilage. As far as this record reveals, no intimate details connected with the use of the home or curtilage were observed, and there was no undue noise, and no wind, dust, or threat of injury. In these circumstances, there was no violation of the Fourth Amendment.</p>
<p>The judgment of the Florida Supreme Court is accordingly reversed.</p>
<p><i>So ordered.</i></p>
<p>JUSTICE O'CONNOR, concurring in the judgment.</p>
<p>I concur in the judgment reversing the Supreme Court of Florida because I agree that police observation of the greenhouse in Riley's curtilage from a helicopter passing at an altitude of 400 feet did not violate an expectation of privacy "that society is prepared to recognize as `reasonable.' " <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). I write separately, however, to clarify the standard I believe follows from <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986). In my view, the plurality's approach rests the scope of Fourth Amendment protection too heavily on compliance with FAA regulations whose purpose is to promote air safety, not to protect "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." U. S. Const., Amdt. 4.</p>
<p><i>Ciraolo</i> involved observation of curtilage by officers flying in an airplane at an altitude of 1,000 feet. In evaluating whether this observation constituted a search for which a warrant was required, we acknowledged the importance of curtilage in Fourth Amendment doctrine: "The protection afforded the curtilage is essentially a protection of families and personal privacy in an area intimately linked to the home, both physically and psychologically, where privacy expectations are most heightened." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#212" aria-description="Citation for case: California v. Ciraolo">476 U. S., at 212-213</a></span>. Although the curtilage is an area to which the private activities <span class="star-pagination">*453</span> of the home extend, all police observation of the curtilage is not necessarily barred by the Fourth Amendment. As we observed: "The Fourth Amendment protection of the home has never been extended to require law enforcement officers to shield their eyes when passing by a home on public thoroughfares." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 213</a></span>. In <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>,</i> we likened observation from a plane traveling in "public navigable airspace" at 1,000 feet to observation by police "passing by a home on public thoroughfares." We held that "[i]n an age where private and commercial flight in the public airways is routine," it is unreasonable to expect the curtilage to be constitutionally protected from aerial observation with the naked eye from an altitude of 1,000 feet. <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 215</a></span>.</p>
<p>Ciraolo's expectation of privacy was unreasonable not because the airplane was operating where it had a "right to be," but because public air travel at 1,000 feet is a sufficiently routine part of modern life that it is unreasonable for persons on the ground to expect that their curtilage will not be observed from the air at that altitude. Although "helicopters are not bound by the lower limits of the navigable airspace allowed to other aircraft," <i>ante,</i> at 451, there is no reason to assume that compliance with FAA regulations alone determines " `whether the government's intrusion infringes upon the personal and societal values protected by the Fourth Amendment.' " <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra,</a></span></i> at 212 (quoting <i>Oliver</i> v. <i>United States,</i> <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 182-183</a></span> (1984)). Because the FAA has decided that helicopters can lawfully operate at virtually any altitude so long as they pose no safety hazard, it does not follow that the expectations of privacy "society is prepared to recognize as `reasonable' " simply mirror the FAA's safety concerns.</p>
<p>Observations of curtilage from helicopters at very low altitudes are not perfectly analogous to ground-level observations from public roads or sidewalks. While in both cases the police may have a legal right to occupy the physical space from which their observations are made, the two situations <span class="star-pagination">*454</span> are not necessarily comparable in terms of whether expectations of privacy from such vantage points should be considered reasonable. Public roads, even those less traveled by, are clearly demarked public thoroughfares. Individuals who seek privacy can take precautions, tailored to the location of the road, to avoid disclosing private activities to those who pass by. They can build a tall fence, for example, and thus ensure private enjoyment of the curtilage without risking public observation from the road or sidewalk. If they do not take such precautions, they cannot reasonably expect privacy from public observation. In contrast, even individuals who have taken effective precautions to ensure against ground-level observations cannot block off all conceivable aerial views of their outdoor patios and yards without entirely giving up their enjoyment of those areas. To require individuals to completely cover and enclose their curtilage is to demand more than the "precautions customarily taken by those seeking privacy." <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#152" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 152</a></span> (1978) (Powell, J., concurring). The fact that a helicopter could conceivably observe the curtilage at virtually any altitude or angle, without violating FAA regulations, does not in itself mean that an individual has no reasonable expectation of privacy from such observation.</p>
<p>In determining whether Riley had a reasonable expectation of privacy from aerial observation, the relevant inquiry after <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span></i> is not whether the helicopter was where it had a right to be under FAA regulations. Rather, consistent with <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> we must ask whether the helicopter was in the public airways at an altitude at which members of the public travel with sufficient regularity that Riley's expectation of privacy from aerial observation was not "one that society is prepared to recognize as `reasonable.' " <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>Katz, supra,</i> at 361</a></span>. Thus, in determining " `whether the government's intrusion infringes upon the personal and societal values protected by the Fourth Amendment,' " <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra,</a></span></i> at 212 (quoting <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#182" aria-description="Citation for case: Oliver v. United States"><i>Oliver, supra,</i> at 182-183</a></span>), it is not conclusive to observe, <span class="star-pagination">*455</span> as the plurality does, that "[a]ny member of the public could legally have been flying over Riley's property in a helicopter at the altitude of 400 feet and could have observed Riley's greenhouse." <i>Ante,</i> at 451. Nor is it conclusive that police helicopters may often fly at 400 feet. If the public rarely, if ever, travels overhead at such altitudes, the observation cannot be said to be from a vantage point generally used by the public and Riley cannot be said to have "knowingly expose[d]" his greenhouse to public view. However, if the public can generally be expected to travel over residential backyards at an altitude of 400 feet, Riley cannot reasonably expect his curtilage to be free from such aerial observation.</p>
<p>In my view, the defendant must bear the burden of proving that his expectation of privacy was a reasonable one, and thus that a "search" within the meaning of the Fourth Amendment even took place. Cf. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960) ("Ordinarily, then, it is entirely proper to require of one who seeks to challenge the legality of a search as the basis for suppressing relevant evidence that he allege, and if the allegation be disputed that he establish, that he himself was the victim of an invasion of privacy"); <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).</p>
<p>Because there is reason to believe that there is considerable public use of airspace at altitudes of 400 feet and above, and because Riley introduced no evidence to the contrary before the Florida courts, I conclude that Riley's expectation that his curtilage was protected from naked-eye aerial observation from that altitude was not a reasonable one. However, public use of altitudes lower than that  particularly public observations from helicopters circling over the curtilage of a home  may be sufficiently rare that police surveillance from such altitudes would violate reasonable expectations of privacy, despite compliance with FAA air safety regulations.</p>
<p><span class="star-pagination">*456</span> JUSTICE BRENNAN, with whom JUSTICE MARSHALL and JUSTICE STEVENS join, dissenting.</p>
<p>The Court holds today that police officers need not obtain a warrant based on probable cause before circling in a helicopter 400 feet above a home in order to investigate what is taking place behind the walls of the curtilage. I cannot agree that the Fourth Amendment to the Constitution, which safeguards "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures," tolerates such an intrusion on privacy and personal security.</p>
<p></p>
<h2>I</h2>
<p>The opinion for a plurality of the Court reads almost as if <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), had never been decided. Notwithstanding the disclaimers of its final paragraph, the opinion relies almost exclusively on the fact that the police officer conducted his surveillance from a vantage point where, under applicable Federal Aviation Administration regulations, he had a legal right to be. <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> teaches, however, that the relevant inquiry is whether the police surveillance "violated the privacy upon which [the defendant] justifiably relied," <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">id.,</a></span></i> at 353  or, as Justice Harlan put it, whether the police violated an "expectation of privacy . . . that society is prepared to recognize as `reasonable.' " <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 361</a></span> (concurring opinion). The result of that inquiry in any given case depends ultimately on the judgment "whether, if the particular form of surveillance practiced by the police is permitted to go unregulated by constitutional restraints, the amount of privacy and freedom remaining to citizens would be diminished to a compass inconsistent with the aims of a free and open society." Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 403 (1974); see also 1 W. LaFave, Search and Seizure § 2.1(d), pp. 310-314 (2d ed. 1987).</p>
<p>The plurality undertakes no inquiry into whether low-level helicopter surveillance by the police of activities in an enclosed <span class="star-pagination">*457</span> backyard is consistent with the "aims of a free and open society." Instead, it summarily concludes that Riley's expectation of privacy was unreasonable because "[a]ny member of the public could legally have been flying over Riley's property in a helicopter at the altitude of 400 feet and could have observed Riley's greenhouse." <i>Ante,</i> at 451. This observation is, in turn, based solely on the fact that the police helicopter was within the airspace within which such craft are allowed by federal safety regulations to fly.</p>
<p>I agree, of course, that "[w]hat a person knowingly exposes to the public . . . is not a subject of Fourth Amendment protection." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Katz, supra,</i> at 351</a></span>. But I cannot agree that one "knowingly exposes [an area] to the public" solely because a helicopter may legally fly above it. Under the plurality's exceedingly grudging Fourth Amendment theory, the expectation of privacy is defeated if a single member of the public could conceivably position herself to see into the area in question without doing anything illegal. It is defeated whatever the difficulty a person would have in so positioning herself, and however infrequently anyone would in fact do so. In taking this view the plurality ignores the very essence of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> The reason why there is no reasonable expectation of privacy in an area that is exposed to the public is that little diminution in "the amount of privacy and freedom remaining to citizens" will result from police surveillance of something that any passerby readily sees. To pretend, as the plurality opinion does, that the same is true when the police use a helicopter to peer over high fences is, at best, disingenuous. Notwithstanding the plurality's statistics about the number of helicopters registered in this country, can it seriously be questioned that Riley enjoyed virtually complete privacy in his backyard greenhouse, and that that privacy was invaded solely by police helicopter surveillance? Is the theoretical possibility that any member of the public (with sufficient means) could also have hired a helicopter and looked over Riley's fence of any relevance at all in determining <span class="star-pagination">*458</span> whether Riley suffered a serious loss of privacy and personal security through the police action?</p>
<p>In <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986), we held that whatever might be observed from the window of an airplane flying at 1,000 feet could be deemed unprotected by any reasonable expectation of privacy. That decision was based on the belief that airplane traffic at that altitude was sufficiently common that no expectation of privacy could inure in anything on the ground observable with the naked eye from so high. Indeed, we compared those airways to "public thoroughfares," and made the obvious point that police officers passing by a home on such thoroughfares were not required by the Fourth Amendment to "shield their eyes." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 213</a></span>. Seizing on a reference in <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span></i> to the fact that the police officer was in a position "where he ha[d] a right to be," <i>ibid.,</i> today's plurality professes to find this case indistinguishable because FAA regulations do not impose a minimum altitude requirement on helicopter traffic; thus, the officer in this case too made his observations from a vantage point where he had a right to be.<sup>[1]</sup></p>
<p>It is a curious notion that the reach of the Fourth Amendment can be so largely defined by administrative regulations issued for purposes of flight safety.<sup>[2]</sup> It is more curious still <span class="star-pagination">*459</span> that the plurality relies to such an extent on the legality of the officer's act, when we have consistently refused to equate police violation of the law with infringement of the Fourth Amendment.<sup>[3]</sup> But the plurality's willingness to end its inquiry when it finds that the officer was in a position he had a right to be in is misguided for an even more fundamental reason. Finding determinative the fact that the officer was where he had a right to be is, at bottom, an attempt to analogize surveillance from a helicopter to surveillance by a police officer standing on a public road and viewing evidence of crime through an open window or a gap in a fence. In such a situation, the occupant of the home may be said to lack any <span class="star-pagination">*460</span> reasonable expectation of privacy in what can be seen from that road  even if, in fact, people rarely pass that way.</p>
<p>The police officer positioned 400 feet above Riley's backyard was not, however, standing on a public road. The vantage point he enjoyed was not one any citizen could readily share. His ability to see over Riley's fence depended on his use of a very expensive and sophisticated piece of machinery to which few ordinary citizens have access. In such circumstances it makes no more sense to rely on the legality of the officer's position in the skies than it would to judge the constitutionality of the wiretap in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> by the legality of the officer's position outside the telephone booth. The simple inquiry whether the police officer had the legal right to be in the position from which he made his observations cannot suffice, for we cannot assume that Riley's curtilage was so open to the observations of passersby in the skies that he retained little privacy or personal security to be lost to police surveillance. The question before us must be not whether the police were where they had a right to be, but whether public observation of Riley's curtilage was so commonplace that Riley's expectation of privacy in his backyard could not be considered reasonable. To say that an invasion of Riley's privacy from the skies was not impossible is most emphatically not the same as saying that his expectation of privacy within his enclosed curtilage was not "one that society is prepared to recognize as `reasonable.' " <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring).<sup>[4]</sup> While, as we held in <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo</a></span>,</i> air traffic at elevations of 1,000 feet or more may be so common that whatever could be seen with the naked eye from that elevation is unprotected by the Fourth Amendment, it is a large step from there to say that the Amendment offers no protection against low-level helicopter surveillance of enclosed curtilage <span class="star-pagination">*461</span> areas. To take this step is error enough. That the plurality does so with little analysis beyond its determination that the police complied with FAA regulations is particularly unfortunate.</p>
<p></p>
<h2>II</h2>
<p>Equally disconcerting is the lack of any meaningful limit to the plurality's holding. It is worth reiterating that the FAA regulations the plurality relies on as establishing that the officer was where he had a right to be set no minimum flight altitude for helicopters. It is difficult, therefore, to see what, if any, helicopter surveillance would run afoul of the plurality's rule that there exists no reasonable expectation of privacy as long as the helicopter is where it has a right to be.</p>
<p>Only in its final paragraph does the plurality opinion suggest that there might be some limits to police helicopter surveillance beyond those imposed by FAA regulations:</p>
<blockquote>"Neither is there any intimation here that the helicopter interfered with respondent's normal use of the greenhouse or of other parts of the curtilage. As far as this record reveals, no intimate details connected with the use of the home or curtilage were observed, and there was no undue noise, and no wind, dust, or threat of injury. In these circumstances, there was no violation of the Fourth Amendment." <i>Ante,</i> at 452.<sup>[5]</sup></blockquote>
<p>I will deal with the "intimate details" below. For the rest, one wonders what the plurality believes the purpose of the Fourth Amendment to be. If through noise, wind, dust, and threat of injury from helicopters the State "interfered with respondent's normal use of the greenhouse or of other parts <span class="star-pagination">*462</span> of the curtilage," Riley might have a cause of action in inverse condemnation, but that is not what the Fourth Amendment is all about. Nowhere is this better stated than in JUSTICE WHITE'S opinion for the Court in <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967): "The basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." See also <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312</a></span> (1978) (same); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 767</a></span> (1966) ("The overriding function of the Fourth Amendment is to protect personal privacy and dignity against unwarranted intrusion by the State"); <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949) ("The security of one's privacy against arbitrary intrusion by the police . . . is at the core of the Fourth Amendment. . . "), overruled on other grounds, <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886) ("It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security. . .").</p>
<p>If indeed the purpose of the restraints imposed by the Fourth Amendment is to "safeguard the privacy and security of individuals," then it is puzzling why it should be the helicopter's noise, wind, and dust that provides the measure of whether this constitutional safeguard has been infringed. Imagine a helicopter capable of hovering just above an enclosed courtyard or patio without generating any noise, wind, or dust at all  and, for good measure, without posing any threat of injury. Suppose the police employed this miraculous tool to discover not only what crops people were growing in their greenhouses, but also what books they were reading and who their dinner guests were. Suppose, finally, that the FAA regulations remained unchanged, so that the police were undeniably "where they had a right to be." Would today's <span class="star-pagination">*463</span> plurality continue to assert that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures" was not infringed by such surveillance? Yet that is the logical consequence of the plurality's rule that, so long as the police are where they have a right to be under air traffic regulations, the Fourth Amendment is offended only if the aerial surveillance interferes with the use of the backyard as a garden spot. Nor is there anything in the plurality's opinion to suggest that any different rule would apply were the police looking from their helicopter, not into the open curtilage, but through an open window into a room viewable only from the air.</p>
<p></p>
<h2>III</h2>
<p>Perhaps the most remarkable passage in the plurality opinion is its suggestion that the case might be a different one had any "intimate details connected with the use of the home or curtilage [been] observed." <i>Ante,</i> at 452. What, one wonders, is meant by "intimate details"? If the police had observed Riley embracing his wife in the backyard greenhouse, would we then say that his reasonable expectation of privacy had been infringed? Where in the Fourth Amendment or in our cases is there any warrant for imposing a requirement that the activity observed must be "intimate" in order to be protected by the Constitution?</p>
<p>It is difficult to avoid the conclusion that the plurality has allowed its analysis of Riley's expectation of privacy to be colored by its distaste for the activity in which he was engaged. It is indeed easy to forget, especially in view of current concern over drug trafficking, that the scope of the Fourth Amendment's protection does not turn on whether the activity disclosed by a search is illegal or innocuous. But we dismiss this as a "drug case" only at the peril of our own liberties. Justice Frankfurter once noted that "[i]t is a fair summary of history to say that the safeguards of liberty have frequently been forged in controversies involving not very <span class="star-pagination">*464</span> nice people," <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 69</a></span> (1950) (dissenting opinion), and nowhere is this observation more apt than in the area of the Fourth Amendment, whose words have necessarily been given meaning largely through decisions suppressing evidence of criminal activity. The principle enunciated in this case determines what limits the Fourth Amendment imposes on aerial surveillance of any person, for any reason. If the Constitution does not protect Riley's marijuana garden against such surveillance, it is hard to see how it will prohibit the government from aerial spying on the activities of a law-abiding citizen on her fully enclosed outdoor patio. As Professor Amsterdam has eloquently written: "The question is not whether you or I must draw the blinds before we commit a crime. It is whether you and I must discipline ourselves to draw the blinds every time we enter a room, under pain of surveillance if we do not." 58 Minn. L. Rev., at 403.<sup>[6]</sup></p>
<p></p>
<h2>IV</h2>
<p>I find little to disagree with in JUSTICE O'CONNOR'S concurrence, apart from its closing paragraphs. A majority of the Court thus agrees that the fundamental inquiry is not whether the police were where they had a right to be under FAA regulations, but rather whether Riley's expectation of privacy was rendered illusory by the extent of <span class="star-pagination">*465</span> public observation of his backyard from aerial traffic at 400 feet.</p>
<p>What separates me from JUSTICE O'CONNOR is essentially an empirical matter concerning the extent of public use of the airspace at that altitude, together with the question of how to resolve that issue. I do not think the constitutional claim should fail simply because "there is reason to believe" that there is "considerable" public flying this close to earth or because Riley "introduced no evidence to the contrary before the Florida courts." <i>Ante,</i> at 455 (O'CONNOR, J., concurring in judgment). I should think that this might be an apt occasion for the application of Professor Davis' distinction between "adjudicative" and "legislative" facts. See Davis, An Approach to Problems of Evidence in the Administrative Process, <span class="citation no-link">55 Harv. L. Rev. 364</span>, 402-410 (1942); see also Advisory Committee's Notes on Fed. Rule Evid. 201, 28 U. S. C. App., pp. 683-684. If so, I think we could take judicial notice that, while there may be an occasional privately owned helicopter that flies over populated areas at an altitude of 400 feet, such flights are a rarity and are almost entirely limited to approaching or leaving airports or to reporting traffic congestion near major roadways. And, as the concurrence agrees, <i>ante,</i> at 455, the extent of police surveillance traffic cannot serve as a bootstrap to demonstrate public use of the airspace.</p>
<p>If, however, we are to resolve the issue by considering whether the appropriate party carried its burden of proof, I again think that Riley must prevail. Because the State has greater access to information concerning customary flight patterns and because the coercive power of the State ought not be brought to bear in cases in which it is unclear whether the prosecution is a product of an unconstitutional, warrantless search, cf. <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548</a></span> (1968) (prosecutor has burden of proving consent to search), the burden of proof properly rests with the State and <span class="star-pagination">*466</span> not with the individual defendant. The State quite clearly has not carried this burden.<sup>[7]</sup></p>
<p></p>
<h2>V</h2>
<p>The issue in this case is, ultimately, "how tightly the fourth amendment permits people to be driven back into the recesses of their lives by the risk of surveillance." Amsterdam, <i>supra,</i> at 402. The Court today approves warrantless helicopter surveillance from an altitude of 400 feet. While JUSTICE O'CONNOR'S opinion gives reason to hope that this altitude may constitute a lower limit, I find considerable cause for concern in the fact that a plurality of four Justices would remove virtually all constitutional barriers to police surveillance from the vantage point of helicopters. The Fourth Amendment demands that we temper our efforts to apprehend criminals with a concern for the impact on our fundamental liberties of the methods we use. I hope it will be a matter of concern to my colleagues that the police surveillance methods they would sanction were among those described 40 years ago in George Orwell's dread vision of life in the 1980's:</p>
<blockquote>"The black-mustachio'd face gazed down from every commanding corner. There was one on the house front immediately opposite. BIG BROTHER IS WATCHING YOU, the caption said . . . . In the far distance a helicopter skimmed down between the roofs, hovered for an instant like a bluebottle, and darted away again with a curving flight. It was the Police Patrol, snooping into people's windows." Nineteen Eighty-Four 4 (1949).</blockquote>
<p><span class="star-pagination">*467</span> Who can read this passage without a shudder, and without the instinctive reaction that it depicts life in some country other than ours? I respectfully dissent.</p>
<p>JUSTICE BLACKMUN, dissenting.</p>
<p>The question before the Court is whether the helicopter surveillance over Riley's property constituted a "search" within the meaning of the Fourth Amendment. Like JUSTICE BRENNAN, JUSTICE MARSHALL, JUSTICE STEVENS, and JUSTICE O'CONNOR, I believe that answering this question depends upon whether Riley has a "reasonable expectation of privacy" that no such surveillance would occur, and does not depend upon the fact that the helicopter was flying at a lawful altitude under FAA regulations. A majority of this Court thus agrees to at least this much.</p>
<p>The inquiry then becomes how to determine whether Riley's expectation was a reasonable one. JUSTICE BRENNAN, the two Justices who have joined him, and JUSTICE O'CONNOR all believe that the reasonableness of Riley's expectation depends, in large measure, on the frequency of nonpolice helicopter flights at an altitude of 400 feet. Again, I agree.</p>
<p>How is this factual issue to be decided? JUSTICE BRENNAN suggests that we may resolve it ourselves without any evidence in the record on this point. I am wary of this approach. While I, too, suspect that for most American communities it is a rare event when nonpolice helicopters fly over one's curtilage at an altitude of 400 feet, I am not convinced that we should establish a <i>per se</i> rule for the entire Nation based on judicial suspicion alone. See Coffin, Judicial Balancing, 63 N. Y. U. L. Rev. 16, 37 (1988).</p>
<p>But we need not abandon our judicial intuition entirely. The opinions of both JUSTICE BRENNAN and JUSTICE O'CONNOR, by their use of "cf." citations, implicitly recognize that none of our prior decisions tells us who has the burden of proving whether Riley's expectation of privacy was reasonable. In the absence of precedent on the point, it is appropriate for us to take into account our estimation of the <span class="star-pagination">*468</span> frequency of nonpolice helicopter flights. See 4 W. LaFave, Search and Seizure § 11.2(b), p. 228 (2d ed. 1987) (burdens of proof relevant to Fourth Amendment issues may be based on a judicial estimate of the probabilities involved). Thus, because I believe that private helicopters rarely fly over curtilages at an altitude of 400 feet, I would impose upon the prosecution the burden of proving contrary facts necessary to show that Riley lacked a reasonable expectation of privacy. Indeed, I would establish this burden of proof for any helicopter surveillance case in which the flight occurred below 1,000 feet  in other words, for any aerial surveillance case not governed by the Court's decision in <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986).</p>
<p>In this case, the prosecution did not meet this burden of proof, as JUSTICE BRENNAN notes. This failure should compel a finding that a Fourth Amendment search occurred. But because our prior cases gave the parties little guidance on the burden of proof issue, I would remand this case to allow the prosecution an opportunity to meet this burden.</p>
<p>The order of this Court, however, is not to remand the case in this manner. Rather, because JUSTICE O'CONNOR would impose the burden of proof on Riley and because she would not allow Riley an opportunity to meet this burden, she joins the plurality's view that no Fourth Amendment search occurred. The judgment of the Court, therefore, is to reverse outright on the Fourth Amendment issue. Accordingly, for the reasons set forth above, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of Indiana et al. by <i>Linley E. Pearson,</i> Attorney General of Indiana, and <i>Lisa M. Paunicka,</i> Deputy Attorney General, <i>Don Siegelman,</i> Attorney General of Alabama, <i>Robert K. Corbin,</i> Attorney General of Arizona, <i>John Steven Clark,</i> Attorney General of Arkansas, <i>John J. Kelly,</i> Chief State's Attorney of Connecticut, <i>Charles M. Oberly,</i> Attorney General of Delaware, <i>Warren Price III,</i> Attorney General of Hawaii, <i>Jim Jones,</i> Attorney General of Idaho, <i>Neil F. Hartigan,</i> Attorney General of Illinois, <i>Robert T. Stephan,</i> Attorney General of Kansas, <i>Frederic J. Cowan,</i> Attorney General of Kentucky, <i>Frank J. Kelley,</i> Attorney General of Michigan, <i>Hubert H. Humphrey III,</i> Attorney General of Minnesota, <i>William L. Webster,</i> Attorney General of Missouri, <i>Robert M. Spire,</i> Attorney General of Nebraska, <i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Anthony J. Celebrezze, Jr.,</i> Attorney General of Ohio, <i>Dave Frohnmayer,</i> Attorney General of Oregon, <i>Travis Medlock,</i> Attorney General of South Carolina, <i>Roger A. Tellinghuisen,</i> Attorney General of South Dakota, <i>David L. Wilkinson,</i> Attorney General of Utah, <i>Jeffrey Amestoy,</i> Attorney General of Vermont, <i>Don Hanaway,</i> Attorney General of Wisconsin, and <i>Joseph B. Meyer,</i> Attorney General of Wyoming; and for the Airborne Law Enforcement Association, Inc., by <i>Ellen M. Condon</i> and <i>Paul J. Marino.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Kent L. Richland, Pamela Victorine, John A. Powell, Steve R. Shapiro, Paul Hoffman, Joan W. Howarth,</i> and <i>James K. Green;</i> for Community Outreach to Vietnam Era Returnees, Inc., by <i>Deborah C. Wyatt;</i> and for the National Association of Criminal Defense Lawyers by <i>Milton Hirsch.</i></p>
<p>[1]  The Florida Supreme Court mentioned the State Constitution in posing the question, once in the course of its opinion, and again in finally concluding that the search violated the Fourth Amendment and the State Constitution. The bulk of the discussion, however, focused exclusively on federal cases dealing with the Fourth Amendment, and there being no indication that the decision "clearly and expressly . . . is alternatively based on bona fide separate, adequate, and independent grounds," we have jurisdiction. <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1041" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1041</a></span> (1983).</p>
<p>[2]  The first use of the helicopter by police was in New York in 1947, and today every State in the country uses helicopters in police work. As of 1980, there were 1,500 such aircraft used in police work. E. Brown, The Helicopter in Civil Operations 79 (1981). More than 10,000 helicopters, both public and private, are registered in the United States. Federal Aviation Administration, Census of U. S. Civil Aircraft, Calendar Year 1987, p. 12. See also 1988 Helicopter Annual 9. And there are an estimated 31,697 helicopter pilots. Federal Aviation Administration, Statistical Handbook of Aviation, Calendar Year 1986, p. 147.</p>
<p>[3]  While Federal Aviation Administration regulations permit fixed-wing aircraft to be operated at an altitude of 1,000 feet while flying over congested areas and at an altitude of 500 feet above the surface in other than congested areas, helicopters may be operated at less than the minimums for fixed-wing aircraft "if the operation is conducted without hazard to persons or property on the surface. In addition, each person operating a helicopter shall comply with routes or altitudes specifically prescribed for helicopters by the [FAA] Administrator." <span class="citation no-link">14 CFR § 91.79</span> (1988).</p>
<p>[1]  What the plurality now states as a firm rule of Fourth Amendment jurisprudence appeared in <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo">476 U. S., at 213</a></span>, as a passing comment: "Nor does the mere fact that an individual has taken measures to restrict some views of his activities preclude an officer's observations from a public vantage point where he has a right to be and which renders the activities clearly visible. <i>E. g., </i><i>United States</i> v. <i>Knotts,</i> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#282" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 282</a></span> (1983)." This rule for determining the constitutionality of aerial surveillance thus derives ultimately from <i><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">Knotts</a></span>,</i> a case in which the police officers' feet were firmly planted on the ground. What is remarkable is not that one case builds on another, of course, but rather that a principle based on terrestrial observation was applied to airborne surveillance without any consideration whether that made a difference.</p>
<p>[2]  The plurality's use of the FAA regulations as a means for determining whether Riley enjoyed a reasonable expectation of privacy produces an incredible result. Fixed-wing aircraft may not be operated below 500 feet (1,000 feet over congested areas), while helicopters may be operated below those levels. See <i>ante,</i> at 451, n. 3. Therefore, whether Riley's expectation of privacy is reasonable turns on whether the police officer at 400 feet above his curtilage is seated in an airplane or a helicopter. This cannot be the law.</p>
<p>[3]  In <i>Oliver</i> v. <i>United States,</i> <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">466 U. S. 170</a></span> (1984), for example, we held that police officers who trespassed upon posted and fenced private land did not violate the Fourth Amendment, despite the fact that their action was subject to criminal sanctions. We noted that the interests vindicated by the Fourth Amendment were not identical with those served by the common law of trespass. See <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#183" aria-description="Citation for case: Oliver v. United States"><i>id.,</i> at 183-184</a></span>, and n. 15; see also <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924) (trespass in "open fields" does not violate the Fourth Amendment). In <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#466" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 466-469</a></span> (1928), the illegality under state law of a wiretap that yielded the disputed evidence was deemed irrelevant to its admissibility. And of course <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), which overruled <i><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span>,</i> made plain that the question whether or not the disputed evidence had been procured by means of a trespass was irrelevant. Recently, in <i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/#239" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227, 239, n. 6</a></span> (1986), we declined to consider trade-secret laws indicative of a reasonable expectation of privacy. Our precedent thus points not toward the position adopted by the plurality opinion, but rather toward the view on this matter expressed some years ago by the Oregon Court of Appeals: "We . . . find little attraction in the idea of using FAA regulations because they were not formulated for the purpose of defining the reasonableness of citizens' expectations of privacy. They were designed to promote air safety." <i>State</i> v. <i>Davis,</i> <span class="citation" data-id="1113918"><a href="/opinion/1113918/state-v-davis/#831" aria-description="Citation for case: State v. Davis">51 Ore. App. 827, 831</a></span>, <span class="citation" data-id="1113918"><a href="/opinion/1113918/state-v-davis/#494" aria-description="Citation for case: State v. Davis">627 P. 2d 492, 494</a></span> (1981).</p>
<p>[4]  Cf. <i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#54" aria-description="Citation for case: California v. Greenwood">486 U. S. 35, 54</a></span> (1988) (BRENNAN, J., dissenting) ("The mere <i>possibility</i> that unwelcome meddlers <i>might</i> open and rummage through the containers does not negate the expectation of privacy in their contents . . .").</p>
<p>[5]  Without actually stating that it makes any difference, the plurality also notes that "there is nothing in the record or before us to suggest" that helicopter traffic at the 400-foot level is so rare as to justify Riley's expectation of privacy. <i>Ante,</i> at 451. The absence of anything "in the record or before us" to suggest the opposite, however, seems not to give the plurality pause. It appears, therefore, that it is the FAA regulations rather than any empirical inquiry that is determinative.</p>
<p>[6]  See also <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#789" aria-description="Citation for case: United States v. White">401 U. S. 745, 789-790</a></span> (1971) (Harlan, J., dissenting):
</p>
<p>"By casting its `risk analysis' solely in terms of the expectations and risks that `wrongdoers' or `one contemplating illegal activities' ought to bear, the plurality opinion, I think, misses the mark entirely. . . . The interest [protected by the Fourth Amendment] is the expectation of the ordinary citizen, who has never engaged in illegal conduct in his life, that he may carry on his private discourse freely, openly, and spontaneously . . . . Interposition of a warrant requirement is designed not to shield `wrongdoers,' but to secure a measure of privacy and a sense of personal security throughout our society."</p>
<p>[7]  The issue in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960), cited by JUSTICE O'CONNOR, was whether the defendant had standing to raise a Fourth Amendment challenge. While I would agree that the burden of alleging and proving facts necessary to show standing could ordinarily be placed on the defendant, I fail to see how that determination has any relevance to the question where the burden should lie on the merits of the Fourth Amendment claim.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Florida v. Royer.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Royer"
type: case
citation: "460 U.S. 491 (1983)"
parallel_cite: "103 S. Ct. 1319; 75 L. Ed. 2d 229; 51 U.S.L.W. 4293"
neutral_cite: 1983 U.S. LEXIS 151
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-03-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-03-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Royer
  varies_by_point: false
  scope_note: "Controlling plurality (White, J.); Brennan, J., concurred in the result and Powell, J., concurred. Good law; the least-intrusive-means and de-facto-arrest principles for investigative detentions remain well established."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110890/florida-v-royer/"
  cluster_id: 110890
  opinion_id: 9429117
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Progeny"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[United States v. Mendenhall]]", "[[Florida v. Bostick]]", "[[United States v. Sharpe]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "investigative-detention", "de-facto-arrest", "consent", "airport"]
holding: "A consensual airport encounter escalated into a de facto arrest requiring probable cause when officers held the suspect's ticket and ID and confined him; Terry detentions must use the least intrusive means."
lake:
  record_id: Florida v. Royer
  status: verified
  projected_at: 2026-07-06
---

# Florida v. Royer

*460 U.S. 491 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Detectives at Miami International Airport, suspecting Royer of carrying narcotics based on a "drug courier profile," approached him, asked for and kept his airline ticket and driver's license, told him he was suspected of transporting drugs, and asked him to accompany them to a small room. Without his consent they retrieved his checked luggage. Royer then produced a key and the agents found marijuana. He moved to suppress, arguing his consent was the product of an illegal detention.

## Issue
Whether a consensual airport encounter and permissible *[[Terry v. Ohio|Terry]]* stop escalated into a detention tantamount to arrest — requiring probable cause — such that Royer's later consent to search his luggage was tainted.

## Rule
Investigative detentions must be limited and minimally intrusive: "an investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop. Similarly, the investigative methods employed should be the least intrusive means reasonably available to verify or dispel the officer's suspicion in a short period of time." — 460 U.S. at 500 (plurality opinion). ^pin-500

On these facts the encounter became an arrest: "What had begun as a consensual inquiry in a public place had escalated into an investigatory procedure in a police interrogation room . . . . As a practical matter, Royer was under arrest." — *Id.* at 503. ^pin-503

## Application
Although the officers had reasonable suspicion to detain Royer briefly, by the time he produced his key the detention had exceeded what suspicion alone allows: the agents had identified themselves as narcotics officers, retained his ticket and identification, retrieved his luggage without consent, confined him in a small room, and never told him he was free to leave. That combination amounted, as a practical matter, to an arrest unsupported by probable cause. The officers could have used less intrusive means — returning his documents and telling him he was free to go — but did not. Because the detention was illegal, Royer's ensuing consent to the luggage search was tainted, and the marijuana was suppressed.

## Conclusion
The detention ripened into an arrest without probable cause, and the tainted consent could not justify the search; suppression was affirmed. *Royer* supplies the least-intrusive-means principle and the markers (holding ID/ticket, confinement, no notice of freedom to leave) that turn a *[[Terry v. Ohio|Terry]]* stop into a [[Common Legal Terms#de-facto|de facto]] arrest.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (controlling plurality).
- Applies the seizure test of [[United States v. Mendenhall]]; its duration/diligence reasoning is refined in [[United States v. Sharpe]] (no rigid time limit), and its free-to-leave analysis informs [[Florida v. Bostick]].

## Appears on
- [[Seizure of the Person]] — *Progeny*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Florida v. Royer*, 460 U.S. 491 (1983) — https://www.courtlistener.com/opinion/110890/florida-v-royer/ — pinpoints: 500, 503.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bbbcb3639ffa7f7a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Royer"}, "payload": {"all": [{"cite": "460 U.S. 491", "page": "491", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "460"}, {"cite": "103 S. Ct. 1319", "page": "1319", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "75 L. Ed. 2d 229", "page": "229", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "75"}, {"cite": "1983 U.S. LEXIS 151", "page": "151", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4293", "page": "4293", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "460 U.S. 491", "official": {"cite": "460 U.S. 491", "page": "491", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "460"}, "official_selection_present": true, "record_id": "Florida v. Royer"}}
{"assertion_id": "78328327098ca42d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-500", "record_id": "Florida v. Royer"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-500", "pinpoint_status": "slip-only", "quote": "approached him, asked for and kept his airline ticket and driver's license, told him he was suspected of transporting drugs, and asked him to accompany them to a small room. Without his consent they retrieved his checked luggage. Royer then produced a key and the agents found marijuana. He moved to suppress, arguing his consent was the product of an illegal detention. ## Issue Whether a consensual airport encounter and permissible *Terry* stop escalated into a detention tantamount to arrest — requiring probable cause — such that Royer's later consent to search his luggage was tainted. ## Rule Investigative detentions must be limited and minimally intrusive:", "quote_fidelity": "mismatch", "record_id": "Florida v. Royer", "star_marker": null}}
{"assertion_id": "e976908985380747", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-503", "record_id": "Florida v. Royer"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-503", "pinpoint_status": "slip-only", "quote": "What had begun as a consensual inquiry in a public place had escalated into an investigatory procedure in a police interrogation room . . . . As a practical matter, Royer was under arrest.", "quote_fidelity": "mismatch", "record_id": "Florida v. Royer", "star_marker": null}}
{"assertion_id": "00b18a7407ea2665", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Royer"}, "payload": {"as_of_content": "1983-03-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Royer", "scope_note": "Controlling plurality (White, J.); Brennan, J., concurred in the result and Powell, J., concurred. Good law; the least-intrusive-means and de-facto-arrest principles for investigative detentions remain well established.", "varies_by_point": false}}
```

### lake record — Florida v. Royer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Royer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Royer",
    "case_name_short": "Royer",
    "case_name_full": "Florida v. Royer",
    "input_case_name": "Florida v. Royer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-03-23",
    "year": 1983,
    "docket": null,
    "cluster_id": 110890,
    "lead_opinion_id": 9429117,
    "sibling_ids": [
      110890,
      9429117,
      9429118,
      9429119,
      9429120,
      9429121
    ],
    "absolute_url": "/opinion/110890/florida-v-royer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "460 U.S. 491",
      "volume": "460",
      "reporter": "U.S.",
      "page": "491",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1319",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 229",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4293",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4293",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 151",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "151",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "460 U.S. 491",
        "volume": "460",
        "reporter": "U.S.",
        "page": "491",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1319",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 229",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 151",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "151",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4293",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4293",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "460 U.S. 491",
    "official_selection": {
      "court_class": "scotus",
      "selected": "460 U.S. 491",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-500",
      "page": null,
      "quote": "approached him, asked for and kept his airline ticket and driver's license, told him he was suspected of transporting drugs, and asked him to accompany them to a small room. Without his consent they retrieved his checked luggage. Royer then produced a key and the agents found marijuana. He moved to suppress, arguing his consent was the product of an illegal detention. ## Issue Whether a consensual airport encounter and permissible *Terry* stop escalated into a detention tantamount to arrest \u2014 requiring probable cause \u2014 such that Royer's later consent to search his luggage was tainted. ## Rule Investigative detentions must be limited and minimally intrusive:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-503",
      "page": null,
      "quote": "What had begun as a consensual inquiry in a public place had escalated into an investigatory procedure in a police interrogation room . . . . As a practical matter, Royer was under arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-03-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Royer",
    "varies_by_point": false,
    "scope_note": "Controlling plurality (White, J.); Brennan, J., concurred in the result and Powell, J., concurred. Good law; the least-intrusive-means and de-facto-arrest principles for investigative detentions remain well established.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane1_negative"
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
        "journal_ref": "Florida v. Royer:lane1_negative"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
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
        "journal_ref": "Florida v. Royer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110890 OR 9429117 OR 9429118 OR 9429119 OR 9429120 OR 9429121) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjExMDE0NDAwMDAwJnM9NDg0ODk0MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110890+OR+9429117+OR+9429118+OR+9429119+OR+9429120+OR+9429121%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(110890 OR 9429117 OR 9429118 OR 9429119 OR 9429120 OR 9429121)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MDQmcz0xMTEzODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110890+OR+9429117+OR+9429118+OR+9429119+OR+9429120+OR+9429121%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110890 OR 9429117 OR 9429118 OR 9429119 OR 9429120 OR 9429121)",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 2,
        "triage_snippet_classified": 109
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110890 OR 9429117 OR 9429118 OR 9429119 OR 9429120 OR 9429121)",
    "indexed_citing_opinions": 4172,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110890,
        "count": 3750,
        "count_source": "search"
      },
      {
        "opinion_id": 9429117,
        "count": 484,
        "count_source": "search"
      },
      {
        "opinion_id": 9429118,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429120,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9429121,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6730,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-royer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODg1NDEmcz0xMDM3NDUxNCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110890+OR+9429117+OR+9429118+OR+9429119+OR+9429120+OR+9429121%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110890,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 101098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 321920,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 345757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 354343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 355301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 364902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 366054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 366535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 373660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 379013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 379320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 380029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 380433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 380469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 381325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 384403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 384586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 387382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 388379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 396175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 1693550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 2302762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110890,
        "cited_id": 2364698,
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
    "date_created": "2026-07-05T04:25:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:29:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Royer

```
<opinion type="majority">
<author id="b555-8"><page-number citation-index="1" label="493">*493</page-number>Justice White</author>
<p id="AO5">announced the judgment of the Court and delivered an opinion, in which Justice Marshall, Justice Powell, and Justice Stevens joined.</p>
<p id="b555-9">We are required in this case to determine whether the Court of Appeal of Florida, Third District, properly applied the precepts of the Fourth Amendment in holding that respondent Royer was being illegally detained at the time of his purported consent to a search of his luggage.</p>
<p id="b555-3">On January 3, 1978, Royer was observed at Miami International Airport by two plainclothes detectives of the Dade County, Fla., Public Safety Department assigned to the county’s Organized Crime Bureau, Narcotics Investigation Section.<footnotemark>1</footnotemark> Detectives Johnson and Magdalena believed that Royer’s appearance, mannerisms, luggage, and actions fit the so-called “drug courier profile.”<footnotemark>2</footnotemark> Royer, apparently unaware of the attention he had attracted, purchased a one-way ticket to New York City and checked his two suitcases, placing on each suitcase an identification tag bearing the name “Holt” and the destination “La Guardia.” As Royer made <page-number citation-index="1" label="494">*494</page-number>his way to the concourse which led to the airline boarding area, the two detectives approached him, identified themselves as policemen working out of the sheriff’s office, and asked if Royer had a “moment” to speak with them; Royer said “Yes.”</p>
<p id="b556-5">Upon request, but without oral consent, Royer produced for the detectives his airline ticket and his driver’s license. The airline ticket, like the baggage identification tags, bore the name “Holt,” while the driver’s license carried respondent’s correct name, “Royer.” When the detectives asked about the discrepancy, Royer explained that a friend had made the reservation in the name of “Holt.” Royer became noticeably more nervous during this conversation, whereupon the detectives informed Royer that they were in fact narcotics investigators and that they had reason to suspect him of transporting narcotics.</p>
<p id="b556-6">The detectives did not return his airline ticket and identification but asked Royer to accompany them to a room, approximately 40 feet away, adjacent to the concourse. Royer said nothing in response but went with the officers as he had been asked to do. The room was later described by Detective Johnson as a “large storage closet,” located in the stewardesses’ lounge and containing a small desk and two chairs. Without Royer’s consent or agreement, Detective Johnson, using Royer’s baggage check stubs, retrieved the “Holt” luggage from the airline and brought it to the room where respondent and Detective Magdalena were waiting. Royer was asked if he would consent to a search of the suitcases. Without orally responding to this request, Royer produced a key and unlocked one of the suitcases, which one detective then opened without seeking further assent from Royer. Marihuana was found in that suitcase. According to Detective Johnson, Royer stated that he did not know the combination to the lock on the second suitcase. When asked if he objected to the detective opening the second suitcase, Royer said “[n]o, go ahead,” and did not object when the de<page-number citation-index="1" label="495">*495</page-number>tective explained that the suitcase might have to be broken open. The suitcase was pried open by the officers and more marihuana was found. Royer was then told that he was under arrest. Approximately 15 minutes had elapsed from the time the detectives initially approached respondent until his arrest upon the discovery of the contraband.</p>
<p id="b557-5">Prior to his trial for felony possession of marihuana,<footnotemark>3</footnotemark> Royer made a motion to suppress the evidence obtained in the search of the suitcases. The trial court found that Royer’s consent to the search was “freely and voluntarily given,” and that, regardless of the consent, the warrantless search was reasonable because “the officer doesn’t have the time to run out and get a search warrant because the plane is going to take off.”<footnotemark>4</footnotemark> Following the denial of the motion to suppress, Royer changed his plea from “not guilty” to <em>“nolo conten-</em>dere,” specifically reserving the right to appeal the denial of the motion to suppress.<footnotemark>5</footnotemark> Royer was convicted.</p>
<p id="b557-6">The District Court of Appeal, sitting en banc, reversed Royer’s conviction.<footnotemark>6</footnotemark> The court held that Royer had been involuntarily confined within the small room without probable cause; that the involuntary detention had exceeded the limited restraint permitted by <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), at the time his consent to the search was obtained; and that the consent to search was therefore invalid because tainted by the unlawful confinement.<footnotemark>7</footnotemark></p>
<p id="b558-4"><page-number citation-index="1" label="496">*496</page-number>Several factors led the court to conclude that respondent’s confinement was tantamount to arrest. Royer had “found himself in a small enclosed area being confronted by two police officers — a situation which presents an almost classic definition of imprisonment.” <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1018" aria-description="Citation for case: Royer v. State">389 So. 2d 1007, 1018</a></span> (1980). The detectives’ statement to Royer that he was suspected of transporting narcotics also bolstered the finding that Royer was “in custody” at the time the consent to search was given. <em><span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">Ibid.</a></span> </em>In addition, the detectives’ possession of Royer’s airline ticket and their retrieval and possession of his luggage made it clear, in the District Court of Appeal’s view, that Royer was not free to leave. <em><span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">Ibid.</a></span></em></p>
<p id="b558-5">At the suppression hearing Royer testified that he was under the impression that he was not free to leave the officers’ presence. The Florida District Court of Appeal found that this apprehension “was much more than a well-justified subjective belief,” for the State had conceded at oral argument before that court that “the officers would not have permitted Royer to leave the room even if he had erroneously thought he could.” <em><span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">Ibid.</a></span> </em>The nomenclature used to describe Royer’s confinement, the court found, was unimportant because under <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), “a police confinement which . . . goes beyond the limited restraint of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>investigatory stop may be constitutionally justified only by probable cause.” <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1019" aria-description="Citation for case: Royer v. State">389 So. 2d, at 1019</a></span> (footnote omitted). Detective Johnson, who conducted the search, had specifically stated at the suppression hearing that he did not have probable cause to arrest Royer until the suitcases were opened and their contents revealed. <page-number citation-index="1" label="497">*497</page-number><em><span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">Ibid.</a></span> </em>In the absence of probable cause, the court concluded, Royer’s consent to search, given only after he had been unlawfully confined, was ineffective to justify the search. <em><span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">Ibid.</a></span> </em>Because there was no proof at all that a “break in the chain of illegality” had occurred, the court found that Royer’s consent was invalid as a matter of law. <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1020" aria-description="Citation for case: Royer v. State"><em>Id., </em>at 1020</a></span>. We granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./454/1079/">454 U. S. 1079</a></span> (1981), and now affirm.</p>
<p id="b559-5">II</p>
<p id="b559-6">Some preliminary observations are in order. First, it is unquestioned that without a warrant to search Royer’s luggage and in the absence of probable cause and exigent circumstances, the validity of the search depended on Royer’s purported consent. Neither is it disputed that where the validity of a search rests on consent, the State has the burden of proving that the necessary consent was obtained and that it was freely and voluntarily given, a burden that is not satisfied by showing a mere submission to a claim of lawful authority. <em>Lo-Ji Sales, Inc. </em>v. <em>New York, </em><span class="citation" data-id="110100"><a href="/opinion/110100/lo-ji-sales-inc-v-new-york/#329" aria-description="Citation for case: Lo-Ji Sales, Inc. v. New York">442 U. S. 319, 329</a></span> (1979); <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#233" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 233-234</a></span> (1973); <em>Bumper </em>v. <em>North Carolina, </em><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548-549</a></span> (1968); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13</a></span> (1948); <em>Amos </em>v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921).</p>
<p id="b559-7">Second, law enforcement officers do not violate the Fourth Amendment by merely approaching an individual on the street or in another public place, by asking him if he is willing to answer some questions, by putting questions to him if the person is willing to listen, or by offering in evidence in a criminal prosecution his voluntary answers to such questions. See <em>Dunaway </em>v. <em>New York, supra, </em>at 210, n. 12; <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#31" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 31, 32-33</a></span> (Harlan, J., concurring); <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span> (White, J., concurring). Nor would the fact that the officer identifies himself as a police officer, without more, convert the encounter into a seizure requiring some level of objective justification. <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#555" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 555</a></span> (1980) (opinion of Stewart, J.). The person <page-number citation-index="1" label="498">*498</page-number>approached, however, need not answer any question put to him; indeed, he may decline to listen to the questions at all and may go on his way. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#32" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 32-33</a></span> (Harlan, J., concurring); <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><em>id., </em>at 34</a></span> (White, J., concurring). He may not be detained even momentarily without reasonable, objective grounds for doing so; and his refusal to listen or answer does not, without more, furnish those grounds. <em>United States </em>v. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#556" aria-description="Citation for case: United States v. Mendenhall"><em>Mendenhall, supra, </em>at 556</a></span> (opinion of Stewart, J.). If there is no detention — no seizure within the meaning of the Fourth Amendment — then no constitutional rights have been infringed.</p>
<p id="b560-5">Third, it is also clear that not all seizures of the person must be justified by probable cause to arrest for a crime. Prior to <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>any restraint on the person amounting to a seizure for the purposes of the Fourth Amendment was invalid unless justified by probable cause. <em>Dunaway </em>v. <em>New York, supra, </em>at 207-209. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>created a limited exception to this general rule: certain seizures are justifiable under the Fourth Amendment if there is articula-ble suspicion that a person has committed or is about to commit a crime. In that case, a stop and a frisk for weapons were found unexceptionable. <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), applied the same approach in the context of an informant’s report that an unnamed individual in a nearby vehicle was carrying narcotics and a gun. Although not expressly authorized in <em>Terry, United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881-882</a></span> (1975), was unequivocal in saying that reasonable suspicion of criminal activity warrants a temporary seizure for the purpose of questioning limited to the purpose of the stop. In <em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>, </em>that purpose was to verify or dispel the suspicion that the immigration laws were being violated, a governmental interest that was sufficient to warrant temporary detention for limited questioning. Royer does not suggest, nor do we, that a similar rationale would not warrant temporary detention for questioning on less than probable cause where the public interest <page-number citation-index="1" label="499">*499</page-number>involved is the suppression of illegal transactions in drugs or of any other serious crime.</p>
<p id="b561-5"><em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981), involved another circumstance in which a temporary detention on less than probable cause satisfied the ultimate test of reasonableness under the Fourth Amendment. There the occupant of a house was detained while a search warrant for the house was being executed. We held that the warrant made the occupant sufficiently suspect to justify his temporary seizure. The “limited intrusio[n] on the personal security” of the person detained was justified “by such substantial law enforcement interests” that the seizure could be made on articulable suspicion not amounting to probable cause. <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#699" aria-description="Citation for case: Michigan v. Summers"><em>Id., </em>at 699</a></span>.</p>
<p id="b561-6">Fourth, <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and its progeny nevertheless created only limited exceptions to the general rule that seizures of the person require probable cause to arrest. Detentions may be “investigative” yet violative of the Fourth Amendment absent probable cause. In the name of investigating a person who is no more than suspected of criminal activity, the police may not carry out a full search of the person or of his automobile or other effects. Nor may the police seek to verify their suspicions by means that approach the conditions of arrest. <em>Dunaway </em>v. <em>New York, swpra, </em>made this clear. There, the suspect was taken to the police station from his home and, without being formally arrested, interrogated for an hour. The resulting incriminating statements were held inadmissible: reasonable suspicion of crime is insufficient to justify custodial interrogation even though the interrogation is investigative. <em>Id., </em>at 211-212. <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), and <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), are to the same effect.</p>
<p id="b561-7">The Fourth Amendment’s prohibition against unreasonable searches and seizures has always been interpreted to prevent a search that is not limited to the particularly described “place to be searched, and the persons or things to be seized,” U. S. Const., Arndt. 4, even if the search is made pursuant to <page-number citation-index="1" label="500">*500</page-number>a warrant and based upon probable cause. The Amendment’s protection is not diluted in those situations where it has been determined that legitimate law enforcement interests justify a warrantless search: the search must be limited in scope to that which is justifed by the particular purposes served by the exception. For example, a warrantless search is permissible incident to a lawful arrest because of legitimate concerns for the safety of the officer and to prevent the destruction of evidence by the arrestee. <em>E. g., Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763</a></span> (1969). Nevertheless, such a search is limited to the person of the arrestee and the area immediately within his control. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">Id., at 762</a></span>. <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra,</a></span> </em>also embodies this principle: “The scope of the search must be ‘strictly tied to and justified by’ the circumstances which rendered its initiation permissible.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19</a></span>, quoting <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (For-tas, J., concurring). The reasonableness requirement of the Fourth Amendment requires no less when the police action is a seizure permitted on less than probable cause because of legitimate law enforcement interests. The scope of the detention must be carefully tailored to its underlying justification.</p>
<p id="b562-5">The predicate permitting seizures on suspicion short of probable cause is that law enforcement interests warrant a limited intrusion on the personal security of the suspect. The scope of the intrusion permitted will vary to some extent with the particular facts and circumstances of each case. This much, however, is clear: an investigative detention must be temporary and last no longer than is necessary to effectuate the purpose of the stop. Similarly, the investigative methods employed should be the least intrusive means reasonably available to verify or dispel the officer’s suspicion in a short period of time. See, <em>e. g., United States </em>v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>Brignoni-Ponce, supra, </em>at 881-882</a></span>; <em>Adams </em>v. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams"><em>Williams, supra, </em>at 146</a></span>. It is the State’s burden to demonstrate that the seizure it seeks to justify on the basis of a reasonable suspicion was sufficiently limited in scope and duration to satisfy the conditions of an investigative seizure.</p>
<p id="b563-5"><page-number citation-index="1" label="501">*501</page-number>Fifth, <em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span> </em>and <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span> </em>hold that statements given during a period of illegal detention are inadmissible even though voluntarily given if they are the product of the illegal detention and not the result of an independent act of free will. <em>Dunaway </em>v. <em>New York, </em>442 U. S., at 218-219; <em>Brown </em>v. <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois"><em>Illinois, supra, </em>at 601-602</a></span>. In this respect those cases reiterated one of the principal holdings of <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<p id="b563-6">Sixth, if the events in this case amounted to no more than a permissible police encounter in a public place or a justifiable Terry-type detention, Royer’s consent, if voluntary, would have been effective to legalize the search of his two suitcases. Cf. <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#424" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 424-425</a></span> (1976). The Florida District Court of Appeal in the case before us, however, concluded not only that Royer had been seized when he gave his consent to search his luggage but also that the bounds of an investigative stop had been exceeded. In its view the “confinement” in this case went beyond the limited restraint of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>investigative stop, and Royer’s consent was thus tainted by the illegality, a conclusion that required reversal in the absence of probable cause to arrest. The question before us is whether the record warrants that conclusion. We think that it does.</p>
<p id="b563-7">HH HH I — I</p>
<p id="b563-3">The State proffers three reasons for holding that when Royer consented to the search of his luggage, he was not being illegally detained. First, it is submitted that the entire encounter was consensual and hence Royer was not being held against his will at all. We find this submission untenable. Asking for and examining Royer’s ticket and his driver’s license were no doubt permissible in themselves, but when the officers identified themselves as narcotics agents, told Royer that he was suspected of transporting narcotics, and asked him to accompany them to the police room, while retaining his ticket and driver’s license and without indicating in any way that he was free to depart, Royer was effectively seized for the purposes of the Fourth Amendment. <page-number citation-index="1" label="502">*502</page-number>These circumstances surely amount to a show of official authority such that “a reasonable person would have believed that he was not free to leave.” <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554</a></span> (opinion of Stewart, J.) (footnote omitted).</p>
<p id="b564-5">Second, the State submits that if Royer was seized, there existed reasonable, articulable suspicion to justify a temporary detention and that the limits of a Terry-type stop were never exceeded. We agree with the State that when the officers discovered that Royer was traveling under an assumed name, this fact, and the facts already known to the officers— paying cash for a one-way ticket, the mode of checking the two bags, and Royer’s appearance and conduct in general— were adequate grounds for suspecting Royer of carrying drugs and for temporarily detaining him and his luggage while they attempted to verify or dispel their suspicions in a manner that did not exceed the limits of an investigative detention. We also agree that had Royer voluntarily consented to the search of his luggage while he was justifiably being detained on reasonable suspicion, the products of the search would be admissible against him. We have concluded, however, that at the time Royer produced the key to his suitcase, the detention to which he was then subjected was a more serious intrusion on his personal liberty than is allowable on mere suspicion of criminal activity.</p>
<p id="b564-6">By the time Royer was informed that the officers wished to examine his luggage, he had identified himself when approached by the officers and had attempted to explain the discrepancy between the name shown on his identification and the name under which he had purchased his ticket and identified his luggage. The officers were not satisfied, for they informed him they were narcotics agents and had reason to believe that he was carrying illegal drugs. They requested him to accompany them to the police room. Royer went with them. He found himself in a small room — a large closet — equipped with a desk and two chairs. He was alone with two police officers who again told him that they thought <page-number citation-index="1" label="503">*503</page-number>he was carrying narcotics. He also found that the officers, without his consent, had retrieved his checked luggage from the airline. What had begun as a consensual inquiry in a public place had escalated into an investigatory procedure in a police interrogation room, where the police, unsatisfied with previous explanations, sought to confirm their suspicions. The officers had Royer’s ticket, they had his identification, and they had seized his luggage. Royer was never informed that he was free to board his plane if he so chose, and he reasonably believed that he was being detained. At least as of that moment, any consensual aspects of the encounter had evaporated, and we cannot fault the Florida District Court of Appeal for concluding that <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span> </em>and the cases following it did not justify the restraint to which Royer was then subjected. As a practical matter, Royer was under arrest. Consistent with this conclusion, the State conceded in the Florida courts that Royer would not have been free to leave the interrogation room had he asked to do so.<footnotemark>8</footnotemark> Furthermore, the State’s brief in this Court interprets the testimony of the officers at the suppression hearing as indicating that had Royer refused to consent to a search of his luggage, the officers would have held the luggage and sought a warrant to authorize the search. Brief for Petitioner 6.<footnotemark>9</footnotemark></p>
<p id="b566-4"><page-number citation-index="1" label="504">*504</page-number>We also think that the officers’ conduct was more intrusive than necessary to effectuate an investigative detention otherwise authorized by the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>line of cases. First, by returning his ticket and driver’s license, and informing him that he was free to go if he so desired, the officers might have obviated any claim that the encounter was anything but a consensual matter from start to finish. Second, there are undoubtedly reasons of safety and security that would justify moving a suspect from one location to another during an investigatory detention, such as from an airport concourse to a more <page-number citation-index="1" label="505">*505</page-number>private area. Cf. <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109-111</a></span> (1977) <em>(per curiam). </em>There is no indication in this case that such reasons prompted the officers to transfer the site of the encounter from the concourse to the interrogation room. It appears, rather, that the primary interest of the officers was not in having an extended conversation with Royer but in the contents of his luggage, a matter which the officers did not pursue orally with Royer until after the encounter was relocated to the police room. The record does not reflect any facts which would support a finding that the legitimate law enforcement purposes which justified the detention in the first instance were furthered by removing Royer to the police room prior to the officers’ attempt to gain his consent to a search of his luggage. As we have noted, had Royer consented to a search on the spot, the search could have been conducted with Royer present in the area where the bags were retrieved by Detective Johnson and any evidence recovered would have been admissible against him. If the search proved negative, Royer would have been free to go much earlier and with less likelihood of missing his flight, which in itself can be a very serious matter in a variety of circumstances.</p>
<p id="b567-5">Third, the State has not touched on the question whether it would have been feasible to investigate the contents of Royer’s bags in a more expeditious way. The courts are not strangers to the use of trained dogs to detect the presence of controlled substances in luggage.<footnotemark>10</footnotemark> There is no indication <page-number citation-index="1" label="506">*506</page-number>here that this means was not feasible and available. If it had been used, Royer and his luggage could have been momentarily detained while this investigative procedure was carried out. Indeed, it may be that no detention at all would have been necessary. A negative result would have freed Royer in short order; a positive result would have resulted in his justifiable arrest on probable cause.</p>
<p id="b568-5">We do not suggest that there is a litmus-paper test for distinguishing a consensual encounter from a seizure or for determining when a seizure exceeds the bounds of an investigative stop. Even in the discrete category of airport encounters, there will be endless variations in the facts and circumstances, so much variation that it is unlikely that the courts can reduce to a sentence or a paragraph a rule that will <page-number citation-index="1" label="507">*507</page-number>provide unarguable answers to the question whether there has been an unreasonable search or seizure in violation of the Fourth Amendment. Nevertheless, we must render judgment, and we think that the Florida District Court of Appeal cannot be faulted in concluding that the limits of a <em>Terry-stop </em>had been exceeded.</p>
<p id="b569-5">IV</p>
<p id="b569-6">The State’s third and final argument is that Royer was not being illegally held when he gave his consent because there was probable cause to arrest him at that time. Detective Johnson testified at the suppression hearing and the Florida District Court of Appeal held that there was no probable cause to arrest until Royer’s bags were opened, but the fact that the officers did not believe there was probable cause and proceeded on a consensual or Terry-stop rationale would not foreclose the State from justifying Royer’s custody by proving probable cause and hence removing any barrier to relying on Royer’s consent to search. <em>Peters </em>v. <em>New York, </em>decided with <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#66" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 66-67</a></span> (1968). We agree with the Florida District Court of Appeal, however, that probable cause to arrest Royer did not exist at the time he consented to the search of his luggage. The facts are that a nervous young man with two American Tourister bags paid cash for an airline ticket to a “target city.” These facts led to inquiry, which in turn revealed that the ticket had been bought under an assumed name. The proffered explanation did not satisfy the officers. We cannot agree with the State, if this is its position, that every nervous young man paying cash for a ticket to New York City under an assumed name and carrying two heavy American Tourister bags may be arrested and held to answer for a serious felony charge.</p>
<p id="b569-7">V</p>
<p id="b569-8">Because we affirm the Florida District Court of Appeal’s conclusion that Royer was being illegally detained when he consented to the search of his luggage, we agree that the con<page-number citation-index="1" label="508">*508</page-number>sent was tainted by the illegality and was ineffective to justify the search. The judgment of the Florida District Court of Appeal is accordingly</p>
<p id="b570-4">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b555-5"> The facts set forth in this opinion are taken from the en banc decision of the Florida District Court of Appeal, Third District, <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1015" aria-description="Citation for case: Royer v. State">389 So. 2d 1007, 1015-1018</a></span> (1980), and from the transcript of the hearing on the motion to suppress contained in the joint appendix. App. 11A-116A.</p>
</footnote>
<footnote label="2">
<p id="b555-6"> The “drug courier profile” is an abstract of characteristics found to be typical of persons transporting illegal drugs. In Royer’s ease, the detectives attention was attracted by the following facts which were considered to be within the profile: (a) Royer was carrying American Tourister luggage, which appeared to be heavy, (b) he was young, apparently between 25-35, (c) he was casually dressed, (d) he appeared pale and nervous, looking around at other people, (e) he paid for his ticket in cash with a large number of bills, and (f) rather than completing the airline identification tag to be attached to checked baggage, which had space for a name, address, and telephone number, he wrote only a name and the destination. <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1016" aria-description="Citation for case: Royer v. State">389 So. 2d, at 1016</a></span>; App. 27A-40A.</p>
</footnote>
<footnote label="3">
<p id="b557-7"> <span class="citation no-link">Fla. Stat. §893.13</span>(l)(a)(2) (1975).</p>
</footnote>
<footnote label="4">
<p id="b557-8"> App. 114A-116A.</p>
</footnote>
<footnote label="5">
<p id="b557-9"> Under Florida law, a plea of <em>nolo contendere </em>is equivalent to a plea of guilty.</p>
</footnote>
<footnote label="6">
<p id="b557-10"> On appeal, a panel of the District Court of Appeal of Florida found that viewing the totality of the circumstances, the finding of consent by the trial court was supported by clear and convincing evidence. <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/" aria-description="Citation for case: Royer v. State">389 So. 2d 1007</a></span> (1979). The panel decision was vacated and rehearing en banc granted. <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1015" aria-description="Citation for case: Royer v. State"><em>Id., </em>at 1015</a></span> (1980). It is the decision of the en banc court that is reviewed here.</p>
</footnote>
<footnote label="7">
<p id="b557-11"> The Florida court was also of the opinion that “a mere similarity with the contents of the drug courier profile is insufficient even to constitute the <page-number citation-index="1" label="496">*496</page-number>articulable suspicion required to justify” the stop authorized by <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>. </em>It went on to hold that even if it followed a contrary rule, or even if articulable suspicion occurred at some point prior to Royer’s consent to search, the facts did not amount to probable cause that would justify the restraint imposed on Royer. <span class="citation" data-id="1693550"><a href="/opinion/1693550/royer-v-state/#1019" aria-description="Citation for case: Royer v. State">389 So. 2d, at 1019</a></span>. As will become clear, we disagree on the reasonable-suspicion issue but do concur that probable cause to arrest was lacking.</p>
</footnote>
<footnote label="8">
<p id="b565-5"> In its brief and at oral argument before this Court, the State contests whether this concession was ever made. We have no basis to question the statement of the Florida court.</p>
</footnote>
<footnote label="9">
<p id="b565-6"> Our decision here is consistent with the Court’s judgment in <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980). In <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>, </em>the respondent was walking along an airport concourse when she was approached by two federal Drug Enforcement Agency (DEA) officers. As in the present case, the officers asked for Mendenhall’s airline ticket and some identification; the names on the ticket and identification did not match. When one of the agents specifically identified himself as attached to the DEA, Men-denhall became visibly shaken and nervous. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#548" aria-description="Citation for case: United States v. Mendenhall"><em>Id., </em>at 548</a></span>.</p>
<p id="b565-7">After returning the ticket and identification, one officer asked Menden-hall if she would accompany him to the DEA airport office, 50 feet away, for further questions. Once in the office, Mendenhall was asked to consent <page-number citation-index="1" label="504">*504</page-number>to a search of her person and her handbag; she was advised of her right to decline. <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span> </em>In a private room following further assurance from Men-denhall that she consented to the search, a policewoman began the search of Mendenhall’s person by requesting that Mendenhall disrobe. As she began to undress, Mendenhall removed two concealed packages that appeared to contain heroin and handed them to the policewoman. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#549" aria-description="Citation for case: United States v. Mendenhall"><em>Id., </em>at 549</a></span>. The Court of Appeals determined that the initial “stop” of Menden-hall was unlawful because not based upon a reasonable suspicion of criminal activity. In the alternative, the court found that even if the initial stop was permissible, the officer’s request that Mendenhall accompany him to the DEA office constituted an arrest without probable cause.</p>
<p id="b566-6">This Court reversed. Two Justices were of the view that the entire encounter was consensual and that no seizure had taken place. Three other Justices assumed that there had been a seizure but would have held that there was reasonable suspicion to warrant it; hence a voluntary consent to search was a valid basis for the search. Thus, the five Justices voting to reverse appeared to agree that Mendenhall was not being illegally detained when she consented to be searched. The four dissenting Justices also assumed that there had been a detention but were of the view that reasonable grounds for suspecting Mendenhall did not exist and concluded that Mendenhall was thus being illegally detained at the time of her consent.</p>
<p id="b566-7">The case before us differs in important respects. Here, Royer’s ticket and identification remained in the possession of the officers throughout the encounter; the officers also seized and had possession of his luggage. As a practical matter, Royer could not leave the airport without them. In <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>, </em>no luggage was involved, the ticket and identification were immediately returned, and the officers were careful to advise that the suspect could decline to be searched. Here, the officers had seized Royer’s luggage and made no effort to advise him that he need not consent to the search.</p>
</footnote>
<footnote label="10">
<p id="b567-6"> Courts of Appeals are in disagreement as to whether using a dog to detect drugs in luggage is a search, but no Court of Appeals has held that more than an articulable suspicion is necessary to justify this kind of a war-rantless search if indeed it is a search. See, <em>e. g., United States </em>v. <em>Sullivan, </em><span class="citation" data-id="380029"><a href="/opinion/380029/united-states-v-diann-pansey-sullivan-aka-brenda-rowe-kathy-ruth/#13" aria-description="Citation for case: United States v. Diann Pansey Sullivan, A/K/A Brenda...">625 F. 2d 9, 13</a></span> (CA4 1980) (no search), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./450/923/">450 U. S. 923</a></span> (1981); <em>United States </em>v. <em>Burns, </em><span class="citation" data-id="379320"><a href="/opinion/379320/united-states-v-michael-henry-burns-vincent-m-andrade-britt-lance/#101" aria-description="Citation for case: United States v. Michael Henry Burns, Vincent M. Andrade,...">624 F. 2d 95, 101</a></span> (CA10 1980) (same); <em>United States </em>v. <em>Beale, </em><span class="citation" data-id="402247"><a href="/opinion/402247/united-states-v-john-christopher-beale/#1335" aria-description="Citation for case: United States v. John Christopher Beale">674 F. 2d 1327, 1335</a></span> (CA9 1982) (sniff is an intrusion requiring reasonable suspicion), cert, pending, No. 82-674. Furthermore, the law of the Circuit from which this case comes was and is that “use of [drug-detecting canines] constitute^] neither a search nor a seizure <page-number citation-index="1" label="506">*506</page-number>under the Fourth Amendment.” <em>United States </em>v. <em>Goldstein, </em><span class="citation" data-id="384586"><a href="/opinion/384586/united-states-v-bennett-goldstein-and-james-edward-kern/#361" aria-description="Citation for case: United States v. Bennett Goldstein and James Edward Kern">635 F. 2d 356, 361</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./452/962/">452 U. S. 962</a></span> (1981). See <em>United States </em>v. <em>Viera, </em><span class="citation" data-id="388379"><a href="/opinion/388379/united-states-v-jose-viera-and-jose-alonso/#510" aria-description="Citation for case: United States v. Jose Viera and Jose Alonso">644 F. 2d 509, 510</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/867/">454 U. S. 867</a></span> (1981). Decisions of the United States Court of Appeals for the Fifth Circuit rendered prior to September 30, 1981, are binding precedent on the United States Court of Appeals for the Eleventh Circuit. <em>Bonner </em>v. <em>City of Prichard, </em><span class="citation" data-id="396175"><a href="/opinion/396175/larry-bonner-v-city-of-prichard-alabama/#1207" aria-description="Citation for case: Larry Bonner v. City of Prichard, Alabama">661 F. 2d 1206, 1207</a></span> (CA11 1981).</p>
<p id="b568-7">In any event, we hold here that the officers had reasonable suspicion to believe that Royer’s luggage contained drugs, and we assume that the use of dogs in the investigation would not have entailed any prolonged detention of either Royer or his luggage which may involve other Fourth Amendment concerns. In <em>United States </em>v. <em><span class="citation" data-id="402247"><a href="/opinion/402247/united-states-v-john-christopher-beale/" aria-description="Citation for case: United States v. John Christopher Beale">Beale, supra,</a></span> </em>for example, after briefly questioning two suspects who had checked baggage for a flight from the Fort Lauderdale, Fla., airport, the officers proceeded to the baggage area where a trained dog alerted to one of the checked bags. Meanwhile, the suspects had boarded their plane for California, where their bags were again sniffed by a trained dog and they were arrested. The Court of Appeals for the Ninth Circuit vacated a judgment convicting the suspects on the ground that articulable suspicion was necessary to justify the use of a trained dog to sniff luggage and that the existence or not of that requirement should have been determined in the District Court. <span class="citation" data-id="402247"><a href="/opinion/402247/united-states-v-john-christopher-beale/#1335" aria-description="Citation for case: United States v. John Christopher Beale">674 F. 2d, at 1335</a></span>. In the case before us, the officers, with founded suspicion, could have detained Royer for the brief period during which Florida authorities at busy airports seem able to carry out the dog-sniffing procedure.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Florida v. Wells.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Wells"
type: case
citation: "495 U.S. 1 (1990)"
parallel_cite: "110 S. Ct. 1632; 109 L. Ed. 2d 1; 58 U.S.L.W. 4454"
neutral_cite: 1990 U.S. LEXIS 2035
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-04-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-04-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Wells
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112412/florida-v-wells/"
  cluster_id: 112412
  opinion_id: 9431971
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Limiting"
related: ["[[Colorado v. Bertine]]", "[[Illinois v. Lafayette]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory-search", "standardized-criteria", "impoundment"]
holding: "An inventory search must not be a ruse for general rummaging to discover incriminating evidence; standardized criteria or established…"
lake:
  record_id: Florida v. Wells
  status: verified
  projected_at: 2026-07-09
---

# Florida v. Wells

*495 U.S. 1 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Florida trooper stopped Wells for speeding, arrested him for DUI, and had his car impounded. An inventory search at the impound facility turned up a locked suitcase in the trunk; at the trooper's direction, facility employees forced it open and found a large quantity of marijuana. The record showed no Florida Highway Patrol policy governing whether closed containers should be opened during an inventory search.

## Issue
Whether marijuana found inside a locked suitcase during an inventory search is admissible when the police had no standardized policy governing the opening of closed containers.

## Rule
No. An inventory search is valid only when conducted under standardized criteria or an established routine, so that it does not become a pretext for an investigatory search: "[A]n inventory search must not be a ruse for a general rummaging in order to discover incriminating evidence." — 495 U.S. at 4. ^pin-4

"The policy or practice governing inventory searches should be designed to produce an inventory." — [*Id.*](https://www.courtlistener.com/opinion/112412/florida-v-wells/#:~:text=The%20policy%20or%20practice%20governing) ^pin-4a

Officers need not proceed in a "totally mechanical 'all or nothing' fashion," but they may not be left with uncanalized discretion over whether to open containers.

## Application
The Florida Highway Patrol had no policy at all governing the opening of closed containers in an inventory search, so the trooper's decision to force open Wells's locked suitcase rested on uncanalized discretion rather than a standardized inventory routine. With nothing channeling that discretion, opening the suitcase was not a valid inventory search, and the marijuana was properly suppressed.

## Conclusion
The suppression of the marijuana was affirmed; absent a standardized policy on opening closed containers, the inventory search of the locked suitcase did not satisfy the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wells* refines the inventory-search rule of [[Colorado v. Bertine]] and [[Illinois v. Lafayette]]: standardized criteria must channel an officer's discretion, though the policy need not be rigidly all-or-nothing.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. Wells*, 495 U.S. 1 (1990) — https://www.courtlistener.com/opinion/112412/florida-v-wells/ — pinpoint: 4.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "61e5d4bcf8f9af2e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Wells"}, "payload": {"all": [{"cite": "495 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "495"}, {"cite": "110 S. Ct. 1632", "page": "1632", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "109 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "1990 U.S. LEXIS 2035", "page": "2035", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "58 U.S.L.W. 4454", "page": "4454", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "58"}], "display": "495 U.S. 1", "official": {"cite": "495 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "495"}, "official_selection_present": true, "record_id": "Florida v. Wells"}}
{"assertion_id": "9d9941a74f4a5b87", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-4a", "record_id": "Florida v. Wells"}, "payload": {"fragment": "#:~:text=The%20policy%20or%20practice%20governing", "page": null, "pin_id": "pin-4a", "pinpoint_status": "star-verified", "quote": "The policy or practice governing inventory searches should be designed to produce an inventory.", "quote_fidelity": "matched", "record_id": "Florida v. Wells", "star_marker": "4"}}
{"assertion_id": "c5cc5b8c60e86289", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-4", "record_id": "Florida v. Wells"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-4", "pinpoint_status": "slip-only", "quote": "--- # Florida v. Wells *495 U.S. 1 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Florida trooper stopped Wells for speeding, arrested him for DUI, and had his car impounded. An inventory search at the impound facility turned up a locked suitcase in the trunk; at the trooper's direction, facility employees forced it open and found a large quantity of marijuana. The record showed no Florida Highway Patrol policy governing whether closed containers should be opened during an inventory search. ## Issue Whether marijuana found inside a locked suitcase during an inventory search is admissible when the police had no standardized policy governing the opening of closed containers. ## Rule No. An inventory search is valid only when conducted under standardized criteria or an established routine, so that it does not become a pretext for an investigatory search:", "quote_fidelity": "mismatch", "record_id": "Florida v. Wells", "star_marker": null}}
{"assertion_id": "97ab852faa620452", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Wells"}, "payload": {"as_of_content": "1990-04-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Wells", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Florida v. Wells

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Wells",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Wells",
    "case_name_short": "Wells",
    "case_name_full": "Florida v. Wells",
    "input_case_name": "Florida v. Wells",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-04-18",
    "year": 1990,
    "docket": null,
    "cluster_id": 112412,
    "lead_opinion_id": 9431971,
    "sibling_ids": [
      112412,
      9431971,
      9431972,
      9431973,
      9431974
    ],
    "absolute_url": "/opinion/112412/florida-v-wells/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "495 U.S. 1",
      "volume": "495",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1632",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1632",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 1",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4454",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4454",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 2035",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2035",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "495 U.S. 1",
        "volume": "495",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1632",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1632",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 L. Ed. 2d 1",
        "volume": "109",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 2035",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "2035",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 U.S.L.W. 4454",
        "volume": "58",
        "reporter": "U.S.L.W.",
        "page": "4454",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "495 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "495 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-4",
      "page": null,
      "quote": "--- # Florida v. Wells *495 U.S. 1 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Florida trooper stopped Wells for speeding, arrested him for DUI, and had his car impounded. An inventory search at the impound facility turned up a locked suitcase in the trunk; at the trooper's direction, facility employees forced it open and found a large quantity of marijuana. The record showed no Florida Highway Patrol policy governing whether closed containers should be opened during an inventory search. ## Issue Whether marijuana found inside a locked suitcase during an inventory search is admissible when the police had no standardized policy governing the opening of closed containers. ## Rule No. An inventory search is valid only when conducted under standardized criteria or an established routine, so that it does not become a pretext for an investigatory search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-4a",
      "page": null,
      "quote": "The policy or practice governing inventory searches should be designed to produce an inventory.",
      "star_marker": "4",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6278,
      "fragment": "#:~:text=The%20policy%20or%20practice%20governing",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-04-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Wells",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Weathers v. State of Indiana",
          "cluster_id": 4248521,
          "cite": [
            "61 N.E.3d 279",
            "2016 Ind. App. LEXIS 297",
            "2016 WL 4379346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 3210125,
          "cite": [
            "10 N.M. 348",
            "2016 NMCA 073"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eddie Tyler v. State of Florida",
          "cluster_id": 3176188,
          "cite": [
            "185 So. 3d 659",
            "2016 Fla. App. LEXIS 1811",
            "2016 WL 514244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeffrey Ray Cox v. State",
          "cluster_id": 4288224,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Corbin",
          "cluster_id": 2740840,
          "cite": [
            "121 A.D.3d 803",
            "993 N.Y.S.2d 746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jesus Cervantes",
          "cluster_id": 799940,
          "cite": [
            "678 F.3d 798",
            "2012 WL 1700840",
            "2012 U.S. App. LEXIS 9843"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Five Thousand Five Hundred Dollars in United States Currency",
          "cluster_id": 2903783,
          "cite": [
            "296 S.W.3d 696",
            "2009 Tex. App. LEXIS 2678",
            "2009 WL 1026607"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
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
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
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
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
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
        "journal_ref": "Florida v. Wells:lane2_top_cited"
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
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ladson",
          "cluster_id": 1191947,
          "cite": [
            "979 P.2d 833"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Redd",
          "cluster_id": 2387024,
          "cite": [
            "48 Cal. 4th 691",
            "229 P.3d 101",
            "108 Cal. Rptr. 3d 192",
            "2010 Cal. LEXIS 3749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1302221,
          "cite": [
            "973 P.2d 52",
            "83 Cal. Rptr. 2d 275",
            "20 Cal. 4th 119"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George M. Khoury, Howard Kluver, David W. West, Louis H. Chippas",
          "cluster_id": 540141,
          "cite": [
            "901 F.2d 948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amos Salmon, No. 90-3355, Raymond E. Washington, No. 90-3363, Richard Fitzpatrick, No. 90-3366, John Surratt, No. 90-3438",
          "cluster_id": 568506,
          "cite": [
            "944 F.2d 1106",
            "1991 U.S. App. LEXIS 21727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zavala",
          "cluster_id": 63259,
          "cite": [
            "541 F.3d 562",
            "2008 U.S. App. LEXIS 18132",
            "2008 WL 3877232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crittenden v. State",
          "cluster_id": 1506576,
          "cite": [
            "899 S.W.2d 668",
            "1995 Tex. Crim. App. LEXIS 57",
            "1995 WL 296354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher Duguay",
          "cluster_id": 724910,
          "cite": [
            "93 F.3d 346",
            "1996 WL 467316"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rodney Lee Morgan",
          "cluster_id": 563786,
          "cite": [
            "936 F.2d 1561",
            "1991 U.S. App. LEXIS 13305",
            "33 Fed. R. Serv. 583"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Alvaro Gallo",
          "cluster_id": 557219,
          "cite": [
            "927 F.2d 815",
            "1991 U.S. App. LEXIS 4366",
            "1991 WL 34983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Newman",
          "cluster_id": 1953250,
          "cite": [
            "548 N.W.2d 739",
            "250 Neb. 226",
            "1996 Neb. LEXIS 122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Vineyard",
          "cluster_id": 1060923,
          "cite": [
            "958 S.W.2d 730",
            "1997 Tenn. LEXIS 634",
            "1997 WL 790359"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cyrus Jonathan George",
          "cluster_id": 588130,
          "cite": [
            "971 F.2d 1113"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Wells:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112412 OR 9431971 OR 9431972 OR 9431973 OR 9431974) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE3NDYyNDAwMDAwJnM9MTYyOTc1OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112412+OR+9431971+OR+9431972+OR+9431973+OR+9431974%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112412 OR 9431971 OR 9431972 OR 9431973 OR 9431974)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTEmcz0xNzgyODI3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112412+OR+9431971+OR+9431972+OR+9431973+OR+9431974%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112412 OR 9431971 OR 9431972 OR 9431973 OR 9431974)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 0,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112412 OR 9431971 OR 9431972 OR 9431973 OR 9431974)",
    "indexed_citing_opinions": 591,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112412,
        "count": 498,
        "count_source": "search"
      },
      {
        "opinion_id": 9431971,
        "count": 108,
        "count_source": "search"
      },
      {
        "opinion_id": 9431972,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431973,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431974,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1010,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-wells.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3Mzc5NTQmcz05NDg5NjIwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112412+OR+9431971+OR+9431972+OR+9431973+OR+9431974%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112412,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112412,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112412,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112412,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112412,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112412,
        "cited_id": 1095147,
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
    "date_created": "2026-07-05T04:29:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:29:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:29:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:33:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:29:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Wells

```
<opinion type="majority">
<author id="b58-9">Chief Justice Rehnquist</author>
<p id="AY">delivered the opinion of the Court.</p>
<p id="b58-10">A Florida Highway Patrol trooper stopped respondent Wells for speeding. After smelling alcohol on Wells’ breath, the trooper arrested Wells for driving under the influence. Wells then agreed to accompany the trooper to the station to take a breathalyzer test. The trooper informed Wells that the car would be impounded and obtained Wells’ permission to open the trunk. At the impoundment facility, an inventory search of the car turned up two marijuana cigarette butts in an ashtray and a locked suitcase in the trunk. Under the trooper’s direction, employees of the facility forced open the suitcase and discovered a garbage bag containing a considerable amount of marijuana.</p>
<p id="b58-11">Wells was charged with possession of a controlled substance. His motion to suppress the marijuana on the ground that it was seized in violation of the Fourth Amendment to the United States Constitution was denied by the trial court. <page-number citation-index="1" label="3">*3</page-number>He thereupon pleaded <em>nolo contendere </em>to the charge but reserved his right to appeal the denial of the motion to suppress. On appeal, the Florida District Court of Appeal for the Fifth District held, <em>inter alia, </em>that the trial court erred in denying suppression of the marijuana found in the suitcase. Over a dissent, the Supreme Court of Florida affirmed. <span class="citation" data-id="1095147"><a href="/opinion/1095147/state-v-wells/#469" aria-description="Citation for case: State v. Wells">539 So. 2d 464, 469</a></span> (1989). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./491/903/">491 U. S. 903</a></span> (1989), and now affirm (although we disagree with part of the reasoning of the Supreme Court of Florida).</p>
<p id="b59-5">The Supreme Court of Florida relied on the opinions in <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987); <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#376" aria-description="Citation for case: Colorado v. Bertine"><em>id., </em>at 376</a></span> (Blackmun, J., concurring). Referring to language in the <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Bertine</a></span> </em>concurrence and a footnote in the majority opinion, the court held that</p>
<blockquote id="b59-6">“[i]n the absence of a policy specifically requiring the opening of closed containers found during a legitimate inventory search, <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Bertine</a></span> </em>prohibits us from countenancing the procedure followed in this instance.” <span class="citation" data-id="1095147"><a href="/opinion/1095147/state-v-wells/#469" aria-description="Citation for case: State v. Wells">539 So. 2d, at 469</a></span>.</blockquote>
<p id="b59-7">According to the court, the record contained no evidence of any Highway Patrol policy on the opening of closed containers found during inventory searches. <em><span class="citation" data-id="1095147"><a href="/opinion/1095147/state-v-wells/" aria-description="Citation for case: State v. Wells">Ibid.</a></span> </em>The court added, however:</p>
<blockquote id="b59-8">“The police under <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Bertine</a></span> </em>must mandate either that all containers will be opened during an inventory search, or that no containers will be opened. There can be no room for discretion.” <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Ibid.</a></span></em></blockquote>
<p id="b59-9">While this latter statement of the Supreme Court of Florida derived support from a sentence in the <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Bertine</a></span> </em>concurrence taken in isolation, we think it is at odds with the thrust of both the concurrence and the opinion of the Court in that case. We said in <em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">Bertine</a></span>:</em></p>
<blockquote id="b59-10">“Nothing in <em>[South Dakota </em>v.] <em>Opperman[, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976),] or <em>[Illinois </em>v.] <em>Lafayette[, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983),] prohibits the exercise of police discretion so long as that <page-number citation-index="1" label="4">*4</page-number>discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity.” <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#375" aria-description="Citation for case: Colorado v. Bertine">479 U. S., at 375</a></span>.</blockquote>
<p id="b60-5">Our view that standardized criteria, ibid., or established routine, <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640, 648</a></span> (1983), must regulate the opening of containers found during inventory searches is based on the principle that an inventory search must not be a ruse for a general rummaging in order to discover incriminating evidence. The policy or practice governing inventory searches should be designed to produce an inventory. The individual police officer must not be allowed so much latitude that inventory searches are turned into “a purposeful and general means of discovering evidence of crime,” <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#376" aria-description="Citation for case: Colorado v. Bertine">479 U. S., at 376</a></span> (Blackmun, J., concurring).</p>
<p id="b60-6">But in forbidding uncanalized discretion to police officers conducting inventory searches, there is no reason to insist that they be conducted in a totally mechanical “all or nothing” fashion, “[inventory procedures serve to protect an owner’s property while it is in the custody of the police, to insure against claims of lost, stolen, or vandalized property, and to guard the police from danger.” <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#372" aria-description="Citation for case: Colorado v. Bertine"><em>Id., </em>at 372</a></span>; see also <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#369" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 369</a></span> (1976). A police officer may be allowed sufficient latitude to determine whether a particular container should or should not be opened in light of the nature of the search and characteristics of the container itself. Thus, while policies of opening all containers or of opening no containers are unquestionably permissible, it would be equally permissible, for example, to allow the opening of closed containers whose contents officers determine they are unable to ascertain from examining the containers’ exteriors. The allowance of the exercise of judgment based on concerns related to the purposes of an inventory search does not violate the Fourth Amendment.</p>
<p id="b60-7">In the present case, the Supreme Court of Florida found that the Florida Highway Patrol had no policy whatever with respect to the opening of closed containers encountered dur<page-number citation-index="1" label="5">*5</page-number>ing an inventory search. We hold that absent such a policy, the instant search was not sufficiently regulated to satisfy the Fourth Amendment and that the marijuana which was found in the suitcase, therefore, was properly suppressed by the Supreme Court of Florida. Its judgment is therefore</p>
<p id="b61-5">
<em>Affirmed.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Florida v. White.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. White"
type: case
citation: "526 U.S. 559 (1999)"
parallel_cite: "119 S. Ct. 1555; 143 L. Ed. 2d 748"
neutral_cite: 1999 U.S. LEXIS 3172
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-05-17
docket: 98-223
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-05-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. White
  varies_by_point: false
  scope_note: "Good law. Souter, J. (joined by Breyer, J.), concurred to caution against reading the holding as a general endorsement of warrantless seizures of anything a State labels 'contraband.'"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118287/florida-v-white/"
  cluster_id: 118287
  opinion_id: 9433798
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Carroll v. United States]]", "[[Cooper v. California]]", "[[United States v. Watson]]", "[[California v. Carney]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "forfeiture", "warrantless-seizure", "public-place", "contraband"]
holding: "When police have probable cause to believe a vehicle is itself forfeitable contraband, the Fourth Amendment does not require a warrant to seize the car from a public place."
lake:
  record_id: Florida v. White
  status: verified
  projected_at: 2026-07-06
---

# Florida v. White

*526 U.S. 559 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Identity note:** distinct stem from *[[Alabama v. White]]*, 496 U.S. 325 (1990), and from the page-less, UNVERIFIABLE "United States v. White" stolen-vehicle caption (S4 collisions ledger, Tier C). No year-suffix needed; `[[Florida v. White]]` resolves here.

## Background
Police developed probable cause that Tyvessel White was using his car to deliver cocaine, making the car subject to forfeiture under the Florida Contraband Forfeiture Act. Months later, after arresting White at work on an unrelated charge and obtaining his keys, officers seized the car from his employer's parking lot without a warrant. An inventory search of the seized car turned up cocaine. The Florida Supreme Court held the warrantless seizure invalid.

## Issue
Whether the Fourth Amendment requires police to obtain a warrant before seizing an automobile from a public place when they have probable cause to believe the car is itself contraband subject to forfeiture.

## Rule
No. Probable cause that the vehicle itself is forfeitable contraband supports a warrantless seizure from a public place. The police "certainly had probable cause to believe that the vehicle *itself* was contraband under Florida law," and the founding-era need "to seize readily movable contraband before it is spirited away . . . is equally weighty when the *automobile*, as opposed to its contents, is the contraband that the police seek to secure." — 526 U.S. at 565. ^pin-565

Because the car was seized from a public area, no privacy was invaded: "Based on the relevant history and our prior precedent, we therefore conclude that the Fourth Amendment did not require a warrant to seize respondent's automobile in these circumstances." — *Id.* at 566. ^pin-566

## Application
Although police lacked probable cause to believe the car *contained* contraband at the time of seizure, they had probable cause to believe the car *itself* was contraband under the forfeiture statute, drawn from White's earlier use of it to deliver narcotics. The seizure took place in a public place — the employer's parking lot — so, like the warrantless arrest in *[[United States v. Watson|Watson]]* and the seizure in *G. M. Leasing Corp.*, it involved no invasion of privacy and required no warrant.

## Conclusion
Reversed. The warrantless seizure of a car from a public place, on probable cause that the car is forfeitable contraband, did not violate the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *[[Alabama v. White|White]]* extends the *[[Carroll v. United States|Carroll]]* line — drawn on in [[Carroll v. United States]], [[California v. Carney]], and the forfeiture/custody holding of [[Cooper v. California]] — from searching for contraband to seizing the contraband vehicle itself. The [[Common Legal Terms#concurring-opinion|concurrence]] cautions the holding is not a blanket license to seize anything a legislature labels "contraband."

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Florida v. White*, 526 U.S. 559 (1999) — https://www.courtlistener.com/opinion/118287/florida-v-white/ — pinpoints: 565, 566.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "908890c91bb990b8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. White"}, "payload": {"all": [{"cite": "526 U.S. 559", "page": "559", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "526"}, {"cite": "119 S. Ct. 1555", "page": "1555", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "143 L. Ed. 2d 748", "page": "748", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "143"}, {"cite": "1999 U.S. LEXIS 3172", "page": "3172", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "526 U.S. 559", "official": {"cite": "526 U.S. 559", "page": "559", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "526"}, "official_selection_present": true, "record_id": "Florida v. White"}}
{"assertion_id": "84e128d999f91b08", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-566", "record_id": "Florida v. White"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-566", "pinpoint_status": "slip-only", "quote": "Based on the relevant history and our prior precedent, we therefore conclude that the Fourth Amendment did not require a warrant to seize respondent's automobile in these circumstances.", "quote_fidelity": "mismatch", "record_id": "Florida v. White", "star_marker": null}}
{"assertion_id": "a5e0745fba7f2e2f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-565", "record_id": "Florida v. White"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-565", "pinpoint_status": "slip-only", "quote": "stolen-vehicle caption (S4 collisions ledger, Tier C). No year-suffix needed; `[[Florida v. White]]` resolves here. ## Background Police developed probable cause that Tyvessel White was using his car to deliver cocaine, making the car subject to forfeiture under the Florida Contraband Forfeiture Act. Months later, after arresting White at work on an unrelated charge and obtaining his keys, officers seized the car from his employer's parking lot without a warrant. An inventory search of the seized car turned up cocaine. The Florida Supreme Court held the warrantless seizure invalid. ## Issue Whether the Fourth Amendment requires police to obtain a warrant before seizing an automobile from a public place when they have probable cause to believe the car is itself contraband subject to forfeiture. ## Rule No. Probable cause that the vehicle itself is forfeitable contraband supports a warrantless seizure from a public place. The police", "quote_fidelity": "mismatch", "record_id": "Florida v. White", "star_marker": null}}
{"assertion_id": "60ae00bd31f5e9ac", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. White"}, "payload": {"as_of_content": "1999-05-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. White", "scope_note": "Good law. Souter, J. (joined by Breyer, J.), concurred to caution against reading the holding as a general endorsement of warrantless seizures of anything a State labels 'contraband.'", "varies_by_point": false}}
```

### lake record — Florida v. White

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. White",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. White",
    "case_name_short": "White",
    "case_name_full": "Florida v. White",
    "input_case_name": "Florida v. White",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-05-17",
    "year": 1999,
    "docket": "98-223",
    "cluster_id": 118287,
    "lead_opinion_id": 9433798,
    "sibling_ids": [
      118287,
      9433798,
      9433799,
      9433800
    ],
    "absolute_url": "/opinion/118287/florida-v-white/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9183871,
        "score": 20,
        "case_name": "Florida v. White"
      },
      {
        "cluster_id": 9183870,
        "score": 20,
        "case_name": "Florida v. White"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 559",
      "volume": "526",
      "reporter": "U.S.",
      "page": "559",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1555",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 748",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 3172",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 559",
        "volume": "526",
        "reporter": "U.S.",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1555",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 748",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 3172",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3172",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 559",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 559",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-565",
      "page": null,
      "quote": "stolen-vehicle caption (S4 collisions ledger, Tier C). No year-suffix needed; `[[Florida v. White]]` resolves here. ## Background Police developed probable cause that Tyvessel White was using his car to deliver cocaine, making the car subject to forfeiture under the Florida Contraband Forfeiture Act. Months later, after arresting White at work on an unrelated charge and obtaining his keys, officers seized the car from his employer's parking lot without a warrant. An inventory search of the seized car turned up cocaine. The Florida Supreme Court held the warrantless seizure invalid. ## Issue Whether the Fourth Amendment requires police to obtain a warrant before seizing an automobile from a public place when they have probable cause to believe the car is itself contraband subject to forfeiture. ## Rule No. Probable cause that the vehicle itself is forfeitable contraband supports a warrantless seizure from a public place. The police",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-566",
      "page": null,
      "quote": "Based on the relevant history and our prior precedent, we therefore conclude that the Fourth Amendment did not require a warrant to seize respondent's automobile in these circumstances.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-05-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. White",
    "varies_by_point": false,
    "scope_note": "Good law. Souter, J. (joined by Breyer, J.), concurred to caution against reading the holding as a general endorsement of warrantless seizures of anything a State labels 'contraband.'",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Lee",
          "cluster_id": 2548,
          "cite": [
            "549 F.3d 84",
            "2008 U.S. App. LEXIS 24462",
            "2008 WL 5076677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Lee Brookins",
          "cluster_id": 783712,
          "cite": [
            "345 F.3d 231",
            "2003 U.S. App. LEXIS 19731",
            "2003 WL 22211620"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2188251,
          "cite": [
            "32 S.W.3d 294",
            "2000 WL 1389720"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wayne Gaskin, AKA \"Atiba,\" and Al Castle",
          "cluster_id": 785776,
          "cite": [
            "364 F.3d 438",
            "2004 U.S. App. LEXIS 7440",
            "2004 WL 818734"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baldwin v. Reagan",
          "cluster_id": 853850,
          "cite": [
            "715 N.E.2d 332",
            "1999 Ind. LEXIS 413",
            "1999 WL 452155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rafael Sandoval v. County of Sonoma",
          "cluster_id": 4576214,
          "cite": [
            "912 F.3d 509"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Akins v. State",
          "cluster_id": 1672782,
          "cite": [
            "202 S.W.3d 879",
            "2006 Tex. App. LEXIS 7792",
            "2006 WL 2507346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Krimstock v. Kelly",
          "cluster_id": 779364,
          "cite": [
            "306 F.3d 40",
            "2002 U.S. App. LEXIS 19182"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Krimstock v. Kelly",
          "cluster_id": 7108370,
          "cite": [
            "306 F.3d 40",
            "2002 WL 31061111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Smith",
          "cluster_id": 1390409,
          "cite": [
            "510 F.3d 641",
            "2007 U.S. App. LEXIS 29732",
            "2007 WL 4482202"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. One 1998 GMC",
          "cluster_id": 3135641,
          "cite": [
            "2011 IL 110236",
            "355 Ill. Dec. 900",
            "960 N.E.2d 1071",
            "2011 Ill. LEXIS 2238"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Theodore Richards",
          "cluster_id": 2709635,
          "cite": [
            "719 F.3d 746",
            "2013 WL 2991897",
            "2013 U.S. App. LEXIS 12026"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tate v. District of Columbia",
          "cluster_id": 181303,
          "cite": [
            "627 F.3d 904",
            "393 U.S. App. D.C. 270",
            "2010 U.S. App. LEXIS 25799",
            "2010 WL 5128849"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwight Anthony Goddard",
          "cluster_id": 76021,
          "cite": [
            "312 F.3d 1360",
            "2002 WL 31670388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark Alfisi",
          "cluster_id": 779552,
          "cite": [
            "308 F.3d 144",
            "2002 U.S. App. LEXIS 21082",
            "2002 WL 31245977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Weaver",
          "cluster_id": 1324259,
          "cite": [
            "649 S.E.2d 479",
            "374 S.C. 313",
            "2007 S.C. LEXIS 293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael L. Enas",
          "cluster_id": 773865,
          "cite": [
            "255 F.3d 662",
            "2001 Cal. Daily Op. Serv. 5504",
            "2001 Daily Journal DAR 6767",
            "2001 U.S. App. LEXIS 14397",
            "2001 WL 726669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joshua Conlan",
          "cluster_id": 2800862,
          "cite": [
            "786 F.3d 380",
            "2015 U.S. App. LEXIS 7956",
            "2015 WL 2330296"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dion",
          "cluster_id": 4398696,
          "cite": [
            "859 F.3d 114",
            "2017 U.S. App. LEXIS 10239",
            "2017 WL 2470405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byndloss v. State",
          "cluster_id": 2263194,
          "cite": [
            "893 A.2d 1119",
            "391 Md. 462",
            "2006 Md. LEXIS 115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Newdow v. Rio Linda Union School District",
          "cluster_id": 88,
          "cite": [
            "597 F.3d 1007",
            "2010 U.S. App. LEXIS 5201"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Antonio Mercado",
          "cluster_id": 779541,
          "cite": [
            "307 F.3d 1226",
            "2002 U.S. App. LEXIS 20927",
            "2002 WL 31230836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Silva",
          "cluster_id": 2652343,
          "cite": [
            "742 F.3d 1",
            "2014 WL 448449",
            "2014 U.S. App. LEXIS 2201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ewing",
          "cluster_id": 214224,
          "cite": [
            "638 F.3d 1226",
            "2011 U.S. App. LEXIS 7065",
            "2011 WL 1312942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Capelton",
          "cluster_id": 200745,
          "cite": [
            "350 F.3d 231",
            "62 Fed. R. Serv. 1583",
            "7 A.L.R. Fed. 2d 781",
            "2003 U.S. App. LEXIS 24042",
            "2003 WL 22801166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. White:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118287 OR 9433798 OR 9433799 OR 9433800) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 3,
        "triage_snippet_classified": 69
      },
      "lane2_top_cited": {
        "query": "cites:(118287 OR 9433798 OR 9433799 OR 9433800)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNiZzPTUwOTM5NDYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118287+OR+9433798+OR+9433799+OR+9433800%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118287 OR 9433798 OR 9433799 OR 9433800)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118287 OR 9433798 OR 9433799 OR 9433800)",
    "indexed_citing_opinions": 98,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118287,
        "count": 81,
        "count_source": "search"
      },
      {
        "opinion_id": 9433798,
        "count": 20,
        "count_source": "search"
      },
      {
        "opinion_id": 9433799,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433800,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 188,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-white.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2ODA2NjYmcz0xMDcxMzUwMiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118287+OR+9433798+OR+9433799+OR+9433800%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118287,
        "cited_id": 87010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 107043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 109572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 112904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 112914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 118005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 389949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 409430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 421669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 524700,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 526530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 538544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 594396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 627489,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 665819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 1634396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 1720618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 1767741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118287,
        "cited_id": 1839728,
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
    "date_created": "2026-07-05T04:33:40Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:34:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:34:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:37:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:34:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. White

```
<opinion type="majority">
<author id="b673-4"><page-number citation-index="1" label="561">*561</page-number>Justice Thomas</author>
<p id="AzqO">delivered the opinion of the Court.</p>
<p id="b673-5">The Florida Contraband Forfeiture Act provides that certain forms of contraband, including motor vehicles used in violation of the Act’s provisions, may be seized and potentially forfeited. In this ease, we must decide whether the Fourth Amendment requires the police to obtain a warrant before seizing an automobile from a public place when they have probable cause to believe that it is forfeitable contraband. We hold that it does not.</p>
<p id="b673-6">I</p>
<p id="b673-7">On three occasions in July and August 1993, police officers observed respondent Tyvessel Tyvorus White using his car to deliver cocaine, and thereby developed probable cause to believe that his ear was subject to forfeiture under the Florida Contraband Forfeiture Act (Act), <span class="citation no-link">Fla. Stat. §932.701</span> <em>et seq. </em>(1997).<footnotemark>1</footnotemark> Several months later, the police arrested respondent at his place of employment on charges unrelated to the drug transactions observed in July and August 1993. At the same time, the arresting officers, without securing a warrant, seized respondent’s automobile in accordance with the provisions of the Act. See § 932.703(2)(a).<footnotemark>2</footnotemark> They seized the <page-number citation-index="1" label="562">*562</page-number>vehicle solely because they believed that it was forfeitable under the Act. During a subsequent inventory search, the police found two pieces of crack cocaine in the ashtray. Based on the discovery of the cocaine, respondent was charged with possession of a controlled substance in violation of Florida law.</p>
<p id="b674-5">At his trial on the possession charge, motion to suppress the evidence discovered during the inventory search. He argued that the warrantless seizure of his car violated the Fourth Amendment, thereby making the cocaine the “fruit of the poisonous tree.” The trial court initially reserved ruling on respondent’s motion, but later denied it after the jury returned a guilty verdict. On appeal, the Florida First District Court of Appeal affirmed. <span class="citation" data-id="1634396"><a href="/opinion/1634396/white-v-state/" aria-description="Citation for case: White v. State">680 So. 2d 550</a></span> (1996). Adopting the position of a majority of state and federal courts to have considered the question, the court rejected respondent’s argument that the Fourth Amendment required the police to secure a warrant prior to seizing his vehicle. <span class="citation" data-id="1634396"><a href="/opinion/1634396/white-v-state/#554" aria-description="Citation for case: White v. State"><em>Id., </em>at 554</a></span>. Because the Florida Supreme Court and this Court had not directly addressed the issue, the court certified to the Florida Supreme Court the question whether, absent exigent circumstances, the war-rantless seizure of an automobile under the Act violated the Fourth Amendment. <span class="citation" data-id="1634396"><a href="/opinion/1634396/white-v-state/#555" aria-description="Citation for case: White v. State"><em>Id., </em>at 555</a></span>.</p>
<p id="b674-6">In a divided opinion, the Florida Supreme Court answered the certified question in the affirmative, quashed the First District Court of Appeal’s opinion, and remanded. <span class="citation" data-id="1839728"><a href="/opinion/1839728/white-v-state/#955" aria-description="Citation for case: White v. State">710 So. 2d 949, 955</a></span> (1998). The majority of the court concluded that, absent exigent circumstances, the Fourth Amendment requires the police to obtain a warrant prior to seizing prop<page-number citation-index="1" label="563">*563</page-number>erty that has been used in violation of the Act. <em><span class="citation" data-id="1839728"><a href="/opinion/1839728/white-v-state/" aria-description="Citation for case: White v. State">Ibid.</a></span> </em>According to the court, the fact that the police develop probable cause to believe that such a violation occurred does not, standing alone, justify a warrantless seizure. The court expressly rejected the holding of the Eleventh Circuit, see <em>United States </em>v. <em>Valdes, </em><span class="citation" data-id="524700"><a href="/opinion/524700/united-states-v-jose-valdes-lino-lopez/" aria-description="Citation for case: United States v. Jose Valdes, Lino Lopez">876 F. 2d 1554</a></span> (1989), and the majority of other Federal Circuits to have addressed the same issue in the context of the federal civil forfeiture law, <span class="citation no-link">21 U. S. C. §881</span>, which is similar to Florida’s. See <em>United States </em>v. <em>Decker, </em><span class="citation" data-id="665819"><a href="/opinion/665819/united-states-v-david-john-decker/" aria-description="Citation for case: United States v. David John Decker">19 F. 3d 287</a></span> (CA6 1994) <em>(per curiam); United States </em>v. <em>Pace, </em><span class="citation" data-id="538544"><a href="/opinion/538544/united-states-v-joseph-pace-anthony-besase-christ-savides-donald-smith/#1241" aria-description="Citation for case: United States v. Joseph Pace, Anthony Besase, Christ...">898 F. 2d 1218, 1241</a></span> (CA7 1990); <em>United States </em>v. <em>One 1978 Mercedes Benz, </em><span class="citation multiple-matches"><a href="/c/F.%202d/711/1297/">711 F. 2d 1297</a></span> (CA5 1983); <em>United States </em>v. <em>Kemp, </em><span class="citation" data-id="9469787"><a href="/opinion/409430/united-states-v-robert-allen-kemp/" aria-description="Citation for case: United States v. Robert Allen Kemp">690 F. 2d 397</a></span> (CA4 1982); <em>United States </em>v. <em>Bush, </em><span class="citation" data-id="8913192"><a href="/opinion/8923945/united-states-v-bush/" aria-description="Citation for case: United States v. Bush">647 F. 2d 357</a></span> (CA3 1981). But see <em>United States </em>v. <em>Dixon, </em><span class="citation" data-id="627489"><a href="/opinion/627489/united-states-v-lewis-nathaniel-dixon/" aria-description="Citation for case: United States v. Lewis Nathaniel Dixon">1 F. 3d 1080</a></span> (CA10 1993); <em>United States </em>v. <em>Lasanta, </em><span class="citation" data-id="594396"><a href="/opinion/594396/united-states-v-doris-lasanta-luis-rivera-juan-cardona-and-eladio/" aria-description="Citation for case: United States v. Doris Lasanta, Luis Rivera, Juan...">978 F. 2d 1300</a></span> (CA2 1992); <em>United States </em>v. <em>Linn, </em><span class="citation" data-id="526530"><a href="/opinion/526530/united-states-v-kenneth-herbert-linn-aka-dennis-kenneth-long/" aria-description="Citation for case: United States v. Kenneth Herbert Linn, A/K/A Dennis...">880 F. 2d 209</a></span> (CA9 1989). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./525/1000/">525 U. S. 1000</a></span> (1998), and now reverse.</p>
<p id="b675-7">► — 1</p>
<p id="b675-3">The Fourth Amendment guarantees “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures,” and further provides that "no Warrants shall issue, but upon probable cause.” U. S. Const., Arndt. 4. In deciding whether a challenged governmental action violates the Amendment, we have taken care to inquire whether the action was regarded as an unlawful search and seizure when the Amendment was framed. See <em>Wyoming </em>v. <em>Houghton, ante, </em>at 299; <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/#149" aria-description="Citation for case: Work v. United States Ex Rel. Rives">267 U. S. 182, 149</a></span> (1925) (“The Fourth Amendment is to be construed in light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens”).</p>
<p id="b675-4">In <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Carroll</a></span>, </em>we held that when federal officers have probable cause to believe that an automobile contains contraband, <page-number citation-index="1" label="564">*564</page-number>the Fourth Amendment does not require them to obtain a warrant prior to searching the car for and seizing the contraband. Our holding was rooted in federal law enforcement practice at the time of the adoption of the Fourth Amendment. Specifically, we looked to laws of the First, Second, and Fourth Congresses that authorized federal officers to conduct warrantless searches of ships and to seize concealed goods subject to duties. <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Id.,</a></span> </em>at 150-151 (citing Act of July 81,1789, §§24,29,1 Stat. 43; Act of Aug. 4,1790, §50,1 Stat. 170; Act of Feb. 18, 1793, §27, <span class="citation no-link">1 Stat. 315</span>; Act of Mar. 2, 1799, §§68-70, <span class="citation no-link">1 Stat. 677</span>, 678). These enactments led us to conclude that “contemporaneously with the adoption of the Fourth Amendment,” Congress distinguished “the necessity for a search warrant between goods subject to forfeiture, when concealed in a dwelling house or similar place, and like goods in course of transportation and concealed in a movable vessel where they readily could be put out of reach of a search warrant.” <span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/#151" aria-description="Citation for case: Work v. United States Ex Rel. Rives">267 U. S., at 151</a></span>.</p>
<p id="b676-5">The Florida Supreme Court recognized that under Carroll, the police could search respondent’s car, without obtaining a warrant, if they had probable cause to believe that it contained contraband. The court, however, rejected the argument that the warrantless seizure of respondent’s vehicle itself also was appropriate under <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Carroll</a></span> </em>and its progeny. It reasoned that “[tjhere is a vast difference between permitting the immediate search of a movable automobile based on actual knowledge that it then contains contraband [and] the discretionary seizure of a citizen’s automobile based upon a belief that it may have been used at some time in the past to assist in illegal activity.” <span class="citation" data-id="1839728"><a href="/opinion/1839728/white-v-state/#953" aria-description="Citation for case: White v. State">710 So. 2d, at 953</a></span>. We disagree.</p>
<p id="b676-6">The principles underlying the rule in <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Carroll</a></span> </em>and the founding-era statutes upon which they are based fully support the conclusion that the warrantless seizure of respondent’s ear did not violate the Fourth Amendment. Although, as the Florida Supreme Court observed, the police lacked <page-number citation-index="1" label="565">*565</page-number>probable cause to believe that respondent’s car contained contraband, see <span class="citation" data-id="1839728"><a href="/opinion/1839728/white-v-state/#953" aria-description="Citation for case: White v. State">710 So. 2d, at 953</a></span>, they certainly had probable cause to believe that the vehicle <em>itself </em>was contraband under Florida law.<footnotemark>3</footnotemark> Recognition of the need to seize readily movable contraband before it is spirited away undoubtedly underlies the early federal laws relied upon in <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Carroll</a></span>. </em>See <span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/#150" aria-description="Citation for case: Work v. United States Ex Rel. Rives">267 U. S., at 150-152</a></span>; see also <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390</a></span> (1985); <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span> (1976). This need is equally weighty when the <em>automobile, </em>as opposed to its contents, is the contraband that the police seek to secure.<footnotemark>4</footnotemark> Furthermore, the early federal statutes that we looked to in <em><span class="citation" data-id="100568"><a href="/opinion/100568/work-v-united-states-ex-rel-rives/" aria-description="Citation for case: Work v. United States Ex Rel. Rives">Carroll</a></span>, </em>like the Florida Contraband Forfeiture Act, authorized the warrantless seizure of <em>both </em>goods subject to duties <em>and </em>the ships upon which those goods were concealed. See, <em>e. g., </em><span class="citation no-link">1 Stat. 43</span>, 46; <span class="citation no-link">1 Stat. 170</span>, 174; <span class="citation no-link">1 Stat. 677</span>, 678, 692.</p>
<p id="b677-5">In addition to the special considerations recognized in the context of movable items, our Fourth Amendment jurisprudence has consistently accorded law enforcement officials greater latitude in exercising their duties in public places. For example, although a warrant presumptively is required for a felony arrest in a suspect’s home, the Fourth Amendment permits warrantless arrests in public places where an officer has probable cause to believe that a felony has occurred. See <em>United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#416" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 416-424</a></span> (1976). In explaining this rule, we have drawn upon the es<page-number citation-index="1" label="566">*566</page-number>tablished “distinction between a warrantless seizure in an open area and such a seizure on private premises.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980); see also <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>id., </em>at 586-587</a></span> (“It is also well settled that objects such as weapons or contraband found in a public place may be seized by the police without a warrant”). The principle that underlies <em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span> </em>extends to the seizure at issue in this case. Indeed, the facts of this case are nearly indistinguishable from those in <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338</a></span> (1977). There, we considered whether federal agents violated the Fourth Amendment by failing to secure a warrant prior to seizing automobiles in partial satisfaction of income tax assessments. <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#351" aria-description="Citation for case: G. M. Leasing Corp. v. United States"><em>Id., </em>at 351</a></span>. We concluded that they did not, reasoning that “[t]he seizures of the automobiles in this case took place on public streets, parking lots, or other open places, and did not involve any invasion of privacy.” <em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">Ibid.</a></span> </em>Here, because the police seized respondent’s vehicle from a public area — respondent’s employer’s parking lot — the warrantless seizure also did not involve any invasion of respondent’s privacy. Based on the relevant history and our prior precedent, we therefore conclude that the Fourth Amendment did not require a warrant to seize respondent’s automobile in these circumstances.</p>
<p id="b678-5">The judgment of the Florida Supreme Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p id="b678-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b673-10"> That Act provides, in relevant part: “Any contraband article, vessel, motor vehicle, aircraft, other personal property, or real property used in violation of any provision of the Florida Contraband Forfeiture Act, or in, upon, or by means of which any violation of the Florida Contraband Forfeiture Act has taken or is taking place, may be seized and shall be forfeited.” <span class="citation no-link">Fla. Stat. § 932.703</span>(l)(a) (1997).</p>
</footnote>
<footnote label="2">
<p id="b673-11"> Nothing in the Act requires the police to obtain a warrant prior to seizing a vehicle. See <em>State </em>v. <em>Pomerance, </em><span class="citation" data-id="1720618"><a href="/opinion/1720618/state-v-pomerance/#330" aria-description="Citation for case: State v. Pomerance">434 So. 2d 329, 330</a></span> (Fla. App. 1983). Rather, the Act simply provides that “[plersonal property <page-number citation-index="1" label="562">*562</page-number>may be seized at the time of the violation or subsequent to the violation, if the person entitled to notice is notified at the time of the seizure . . . that there is a right to an adversarial preliminary hearing after the seizure to determine whether probable cause exists to believe that such property has been or is being used in violation of the Florida Contraband Forfeiture Act." §932.703(2)(a).</p>
</footnote>
<footnote label="3">
<p id="b677-6"> The Aet defines "contraband” to include any "vehicle of any kind,... which was used... as an instrumentality in the commission of, or in aiding or abetting in the commission of, any felony.” § 932.701(2)(a)(5).</p>
</footnote>
<footnote label="4">
<p id="b677-7"><em> </em>At oral argument, respondent contended that the delay between the time that the police developed probable cause to seize the vehicle and when the seizure actually occurred undercuts the argument that the war-rantless seizure was necessary to prevent respondent from removing the car out of the jurisdiction. We express no opinion about whether excessive delay prior to a seizure could render probable cause stale, and the seizure therefore unreasonable under the Fourth Amendment.</p>
</footnote>
</opinion>
```

---
