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

## GROUP: content/cases/Florence v. County of Burlington.md  (`case`, 6 assertions)

### content_page

```
---
title: "Florence v. County of Burlington"
type: case
citation: "566 U.S. 318 (2012)"
parallel_cite: "132 S. Ct. 1510; 182 L. Ed. 2d 566"
neutral_cite: 2012 U.S. LEXIS 2712
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-04-02
docket: 10-945
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florence v. County of Burlington
  varies_by_point: false
  scope_note: "Controlling: jail-intake visual strip searches of all arrestees entering the general population are reasonable without individualized suspicion. Roberts and Alito concurred to note the holding may not reach detainees not admitted to the general population."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/"
  cluster_id: 626454
  opinion_id: 626454
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Inventory Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Lafayette]]", "[[Maryland v. King]]", "[[Atwater v. City of Lago Vista]]"]
aliases: ["Florence v. Board of Chosen Freeholders of County of Burlington", "Florence v. Board of Chosen Freeholders"]
tags: ["case", "fourth-amendment", "jail-search", "strip-search", "booking", "special-needs"]
holding: "Jail officials may conduct a close visual strip search of every arrestee admitted to the general population without reasonable suspicion, regardless of the minor nature of the offense; the Fourth and Fourteenth Amendments do not require an exception for minor offenders."
lake:
  record_id: Florence v. County of Burlington
  status: verified
  projected_at: 2026-07-09
---

# Florence v. County of Burlington

*566 U.S. 318 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Florence was a passenger in a car stopped by a state trooper; he was arrested on a bench warrant for an unpaid fine that he had in fact already paid. He was held for about six days across two county jails and, at intake to each, was subjected to a close visual strip search — directed to disrobe and submit to a visual inspection while undressed — without any suspicion that he was carrying contraband. He sued under § 1983, claiming that suspicionless strip searches of a person arrested for a minor offense violated the Fourth Amendment.

## Issue
May jail officials, consistent with the Fourth Amendment, conduct a close visual strip search of every arrestee being admitted to the general population without reasonable suspicion, regardless of the minor nature of the offense of arrest?

## Rule
Yes. Maintaining institutional safety requires deference to correctional officials, and "a regulation impinging on an inmate's constitutional rights must be upheld 'if it is reasonably related to legitimate penological interests.'" — 566 U.S. at 326 (quoting *Turner v. Safley*). ^pin-326

There is a "substantial interest in preventing any new inmate, either of his own will or as a result of coercion, from putting all who live or work at these institutions at even greater risk when he is admitted to the general population." — [*Id.*](https://www.courtlistener.com/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/#:~:text=substantial%20interest%20in%20preventing%20any) (Part IV). ^pin-iv

Weighing those interests, the intake "search procedures . . . struck a reasonable balance between inmate privacy and the needs of the institutions[;] [t]he Fourth and Fourteenth Amendments do not require adoption of the framework of rules petitioner proposes." — *Id.* at 339. ^pin-339

## Application
The two jails' intake procedures — requiring detainees to disrobe, shower, and submit to a visual inspection without physical contact — addressed the genuine and substantial dangers of admitting new inmates to the general population: smuggled weapons, drugs, and contraband; communicable disease and lice; and gang affiliation that can spark violence. Because there is no reliable way to identify in advance which arrestees, including those held for minor offenses, pose these risks, the Court deferred to the officials' judgment rather than impose a reasonable-suspicion requirement for minor offenders. The searches were reasonable.

## Conclusion
The suspicionless visual strip searches at intake were constitutional; the judgment of the Third Circuit upholding the procedures was affirmed. (Chief Justice Roberts and Justice Alito concurred to emphasize that the holding governs detainees admitted to the general population and may not reach arrestees who are not.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Florence* remains the controlling authority that jail-intake visual strip searches of arrestees entering the general population need no individualized suspicion. It extends the *[[Bell v. Wolfish]]* institutional-deference line and sits beside [[Illinois v. Lafayette]] (booking inventory) and [[Maryland v. King]] (DNA at booking). The Roberts/Alito [[Common Legal Terms#concurring-opinion|concurrences]] cabin its reach to detainees actually committed to the general population. No negative treatment.

## Appears on
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Florence v. Board of Chosen Freeholders of County of Burlington*, 566 U.S. 318 (2012) — https://www.courtlistener.com/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/ — pinpoints to published U.S. Reports (the CL copy is the slip opinion, 566 U.S. ___, without embedded reporter pagination): 326, 339, plus Part IV.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "787722f72e88e19f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "566 U.S. 318 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 2712", "official_citation_present": true, "parallel_cite": "132 S. Ct. 1510; 182 L. Ed. 2d 566", "title": "Florence v. County of Burlington", "year": "2012"}}
{"assertion_id": "99fb16727c1980aa", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Jail officials may conduct a close visual strip search of every arrestee admitted to the general population without reasonable suspicion, regardless of the minor nature of the offense; the Fourth and Fourteenth Amendments do not require an exception for minor offenders.", "title": "Florence v. County of Burlington"}}
{"assertion_id": "9cc052306aaef2ad", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Related (cross-doctrine)", "title": "Florence v. County of Burlington"}}
{"assertion_id": "f7d18ac6c71a61bb", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Progeny / Refinement", "title": "Florence v. County of Burlington"}}
{"assertion_id": "5287f7ab051f12a0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Florence v. County of Burlington"}}
{"assertion_id": "6b99046609ca7b6f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-04-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Florence v. County of Burlington", "field_i_validity": "good_law", "scope_note": "Controlling: jail-intake visual strip searches of all arrestees entering the general population are reasonable without individualized suspicion. Roberts and Alito concurred to note the holding may not reach detainees not admitted to the general population.", "title": "Florence v. County of Burlington", "varies_by_point": "false"}}
```

### lake record — Florence v. County of Burlington

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florence v. County of Burlington",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florence v. Board of Chosen Freeholders of County of Burlington",
    "case_name_short": "Florence",
    "case_name_full": "FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF COUNTY OF BURLINGTON Et Al.",
    "input_case_name": "Florence v. County of Burlington",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-04-02",
    "year": 2012,
    "docket": "10-945",
    "cluster_id": 626454,
    "lead_opinion_id": 626454,
    "sibling_ids": [
      626454,
      9485643,
      9485644,
      9485645,
      9485646
    ],
    "absolute_url": "/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "566 U.S. 318",
      "volume": "566",
      "reporter": "U.S.",
      "page": "318",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1510",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 566",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "566",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 2712",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2712",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1510",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 566",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "566",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 2712",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2712",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "566 U.S. 318",
        "volume": "566",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "566 U.S. 318",
    "official_selection": {
      "court_class": "scotus",
      "selected": "566 U.S. 318",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "--- # Florence v. County of Burlington *566 U.S. 318 (2012)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Florence was a passenger in a car stopped by a state trooper; he was arrested on a bench warrant for an unpaid fine that he had in fact already paid. He was held for about six days across two county jails and, at intake to each, was subjected to a close visual strip search \u2014 directed to disrobe and submit to a visual inspection while undressed \u2014 without any suspicion that he was carrying contraband. He sued under \u00a7 1983, claiming that suspicionless strip searches of a person arrested for a minor offense violated the Fourth Amendment. ## Issue May jail officials, consistent with the Fourth Amendment, conduct a close visual strip search of every arrestee being admitted to the general population without reasonable suspicion, regardless of the minor nature of the offense of arrest? ## Rule Yes. Maintaining institutional safety requires deference to correctional officials, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-iv",
      "page": null,
      "quote": "substantial interest in preventing any new inmate, either of his own will or as a result of coercion, from putting all who live or work at these institutions at even greater risk when he is admitted to the general population.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 33621,
      "fragment": "#:~:text=substantial%20interest%20in%20preventing%20any",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-339",
      "page": null,
      "quote": "search procedures . . . struck a reasonable balance between inmate privacy and the needs of the institutions[;] [t]he Fourth and Fourteenth Amendments do not require adoption of the framework of rules petitioner proposes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florence v. County of Burlington",
    "varies_by_point": false,
    "scope_note": "Controlling: jail-intake visual strip searches of all arrestees entering the general population are reasonable without individualized suspicion. Roberts and Alito concurred to note the holding may not reach detainees not admitted to the general population.",
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
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cole v. Commonwealth",
          "cluster_id": 4443619,
          "cite": [
            "806 S.E.2d 387",
            "294 Va. 342"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfonzo Williams",
          "cluster_id": 4327223,
          "cite": [
            "842 F.3d 1143",
            "2016 U.S. App. LEXIS 21621",
            "2016 WL 7046754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tynisa Williams v. City of Cleveland",
          "cluster_id": 2750185,
          "cite": [
            "771 F.3d 945",
            "2014 FED App. 0276P",
            "2014 U.S. App. LEXIS 21367",
            "2014 WL 5802282"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Saeed Hatim v. Barack Obama",
          "cluster_id": 2689122,
          "cite": [
            "411 U.S. App. D.C. 354",
            "760 F.3d 54",
            "2014 WL 3765701",
            "2014 U.S. App. LEXIS 14759"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Alexandra Chavarriaga v. State of NJ Department of Corr",
          "cluster_id": 3154962,
          "cite": [
            "806 F.3d 210",
            "2015 U.S. App. LEXIS 19854",
            "2015 WL 7171306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall King v. Robert McCarty",
          "cluster_id": 2789826,
          "cite": [
            "781 F.3d 889",
            "2015 U.S. App. LEXIS 5008",
            "2015 WL 1396611"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Parkell v. Carl Danberg",
          "cluster_id": 4248660,
          "cite": [
            "833 F.3d 313",
            "2016 U.S. App. LEXIS 15092",
            "2016 WL 4375620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Mays v. Thomas Dart",
          "cluster_id": 4783259,
          "cite": [
            "974 F.3d 810"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
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
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wallace Beaulieu v. Cal Ludeman",
          "cluster_id": 807638,
          "cite": [
            "690 F.3d 1017",
            "2012 WL 3711342",
            "2012 U.S. App. LEXIS 18306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Miller",
          "cluster_id": 8442644,
          "cite": [
            "818 F.3d 49",
            "2016 U.S. App. LEXIS 4701",
            "2016 WL 963904"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. John Yost",
          "cluster_id": 4772727,
          "cite": [
            "968 F.3d 311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
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
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anson McFaul v. Daniel Valenzuela",
          "cluster_id": 802444,
          "cite": [
            "684 F.3d 564",
            "2012 WL 2210300",
            "2012 U.S. App. LEXIS 12283"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Prieto v. Harold Clarke",
          "cluster_id": 2787619,
          "cite": [
            "780 F.3d 245",
            "2015 WL 1020718"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miriam Mendiola-Martinez v. Joseph Arpaio",
          "cluster_id": 4255699,
          "cite": [
            "836 F.3d 1239",
            "2016 U.S. App. LEXIS 16666",
            "2016 WL 4729476"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinique Stoudemire v. Mich. Dep't of Corrections",
          "cluster_id": 817115,
          "cite": [
            "705 F.3d 560",
            "2013 WL 362828",
            "2013 U.S. App. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raheem Jacobs v. Cumberland County",
          "cluster_id": 4906491,
          "cite": [
            "8 F.4th 187"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Porter v. Harold Clarke",
          "cluster_id": 4616681,
          "cite": [
            "923 F.3d 348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrick Harrington v. A. Scribner",
          "cluster_id": 2799368,
          "cite": [
            "785 F.3d 1299",
            "2015 U.S. App. LEXIS 7545",
            "2015 WL 2106387"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Elizalde",
          "cluster_id": 2811965,
          "cite": [
            "61 Cal. 4th 523",
            "351 P.3d 1010",
            "189 Cal. Rptr. 3d 518",
            "2015 Cal. LEXIS 4518"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barnes v. Felix",
          "cluster_id": 10584846,
          "cite": [
            "605 U.S. 73",
            "145 S. Ct. 1353"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bretton Westmoreland v. Butler Cnty.",
          "cluster_id": 6454550,
          "cite": [
            "29 F.4th 721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sloley v. VanBramer",
          "cluster_id": 4686314,
          "cite": [
            "945 F.3d 30"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turkmen v. Hasty",
          "cluster_id": 8442249,
          "cite": [
            "789 F.3d 218",
            "2015 U.S. App. LEXIS 10160",
            "2015 WL 3756331"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hinkle v. Beckham County Board of County",
          "cluster_id": 4762695,
          "cite": [
            "962 F.3d 1204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Cotterman",
          "cluster_id": 854692,
          "cite": [
            "709 F.3d 952",
            "2013 WL 856292",
            "2013 U.S. App. LEXIS 4731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. City of New York",
          "cluster_id": 7321242,
          "cite": [
            "197 F. Supp. 3d 529",
            "2016 U.S. Dist. LEXIS 84586",
            "2016 WL 3636249"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florence v. County of Burlington:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(626454 OR 9485643 OR 9485644 OR 9485645 OR 9485646) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 7,
        "triage_snippet_classified": 104
      },
      "lane2_top_cited": {
        "query": "cites:(626454 OR 9485643 OR 9485644 OR 9485645 OR 9485646)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNSZzPTk1NjczMDYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28626454+OR+9485643+OR+9485644+OR+9485645+OR+9485646%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(626454 OR 9485643 OR 9485644 OR 9485645 OR 9485646)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(626454 OR 9485643 OR 9485644 OR 9485645 OR 9485646)",
    "indexed_citing_opinions": 141,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 626454,
        "count": 83,
        "count_source": "search"
      },
      {
        "opinion_id": 9485643,
        "count": 58,
        "count_source": "search"
      },
      {
        "opinion_id": 9485644,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485645,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485646,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 709,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florence-v-county-of-burlington.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxMDA5MTMmcz05MzY4ODE4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28626454+OR+9485643+OR+9485644+OR+9485645+OR+9485646%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 626454,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 103990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 110635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 111254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 112224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 130150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 137748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 170650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 175607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 199267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 395191,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 420906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 429227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 436169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 443066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 454822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 457122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 457687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 478949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 521919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 602915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 775758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 776906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 1302147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 1313115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 2480296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 626454,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T03:41:38Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:41:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:41:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:45:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:41:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florence v. County of Burlington

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

  FLORENCE v. BOARD OF CHOSEN FREEHOLDERS 

       OF COUNTY OF BURLINGTON ET AL. 


CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE THIRD CIRCUIT

      No. 10–945.     Argued October 12, 2011—Decided April 2, 2012
Petitioner was arrested during a traffic stop by a New Jersey state
  trooper who checked a statewide computer database and found a
  bench warrant issued for petitioner’s arrest after he failed to appear
  at a hearing to enforce a fine. He was initially detained in the Bur-
  lington County Detention Center and later in the Essex County Cor-
  rectional Facility, but was released once it was determined that the
  fine had been paid. At the first jail, petitioner, like every incoming
  detainee, had to shower with a delousing agent and was checked for
  scars, marks, gang tattoos, and contraband as he disrobed. Petition-
  er claims that he also had to open his mouth, lift his tongue, hold out
  his arms, turn around, and lift his genitals. At the second jail, peti-
  tioner, like other arriving detainees, had to remove his clothing while
  an officer looked for body markings, wounds, and contraband; had an
  officer look at his ears, nose, mouth, hair, scalp, fingers, hands, arm-
  pits, and other body openings; had a mandatory shower; and had his
  clothes examined. Petitioner claims that he was also required to lift
  his genitals, turn around, and cough while squatting. He filed a 42
  U. S. C. §1983 action in the Federal District Court against the gov-
  ernment entities that ran the jails and other defendants, alleging
  Fourth and Fourteenth Amendment violations, and arguing that per-
  sons arrested for minor offenses cannot be subjected to invasive
  searches unless prison officials have reason to suspect concealment of
  weapons, drugs, or other contraband. The court granted him sum-
  mary judgment, ruling that “strip-searching” nonindictable offenders
  without reasonable suspicion violates the Fourth Amendment. The
  Third Circuit reversed.
Held: The judgment is affirmed.
2     FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                 COUNTY OF BURLINGTON

                         Syllabus


621 F. 3d 296, affirmed.
     JUSTICE KENNEDY delivered the opinion of the Court, except as to
  Part IV, concluding that the search procedures at the county jails
  struck a reasonable balance between inmate privacy and the needs of
  the institutions, and thus the Fourth and Fourteenth Amendments
  do not require adoption of the framework and rules petitioner pro-
  poses. Pp. 5−18, 19.
     (a) Maintaining safety and order at detention centers requires the
  expertise of correctional officials, who must have substantial discre-
  tion to devise reasonable solutions to problems. A regulation imping-
  ing on an inmate’s constitutional rights must be upheld “if it is rea-
  sonably related to legitimate penological interests.” Turner v. Safley,
  482 U. S. 78, 89. This Court, in Bell v. Wolfish, 441 U. S. 520, 558,
  upheld a rule requiring pretrial detainees in federal correctional fa-
  cilities “to expose their body cavities for visual inspection as a part of
  a strip search conducted after every contact visit with a person from
  outside the institution[s],” deferring to the judgment of correctional
  officials that the inspections served not only to discover but also to
  deter the smuggling of weapons, drugs, and other prohibited items.
  In Block v. Rutherford, 468 U. S. 576, 586−587, the Court upheld a
  general ban on contact visits in a county jail, noting the smuggling
  threat posed by such visits and the difficulty of carving out exceptions
  for certain detainees. The Court, in Hudson v. Palmer, 468 U. S. 517,
  522−523, also recognized that deterring the possession of contraband
  depends in part on the ability to conduct searches without predictable
  exceptions when it upheld the constitutionality of random searches of
  inmate lockers and cells even without suspicion that an inmate is
  concealing a prohibited item. These cases establish that correctional
  officials must be permitted to devise reasonable search policies to de-
  tect and deter the possession of contraband in their facilities, and
  that “in the absence of substantial evidence in the record to indicate
  that the officials have exaggerated their response to these considera-
  tions courts should ordinarily defer to their expert judgment in such
  matters,” Block, supra, at 584–585.
     Persons arrested for minor offenses may be among the detainees to
  be processed at jails. See Atwater v. Lago Vista, 532 U. S. 318, 354.
  Pp. 5−9.
     (b) The question here is whether undoubted security imperatives
  involved in jail supervision override the assertion that some detain-
  ees must be exempt from the invasive search procedures at issue ab-
  sent reasonable suspicion of a concealed weapon or other contraband.
  Correctional officials have a significant interest in conducting a thor-
  ough search as a standard part of the intake process. The admission
  of new inmates creates risks for staff, the existing detainee popula-
                   Cite as: 566 U. S. ____ (2012)                      3

                              Syllabus

tion, and the new detainees themselves. Officials therefore must
screen for contagious infections and for wounds or injuries requiring
immediate medical attention. It may be difficult to identify and treat
medical problems until detainees remove their clothes for a visual in-
spection. Jails and prisons also face potential gang violence, giving
them reasonable justification for a visual inspection of detainees for
signs of gang affiliation as part of the intake process. Additionally,
correctional officials have to detect weapons, drugs, alcohol, and
other prohibited items new detainees may possess. Drugs can make
inmates aggressive toward officers or each other, and drug trading
can lead to violent confrontations. Contraband has value in a jail’s
culture and underground economy, and competition for scarce goods
can lead to violence, extortion, and disorder. Pp. 9−13.
   (c) Petitioner’s proposal―that new detainees not arrested for seri-
ous crimes or for offenses involving weapons or drugs be exempt from
invasive searches unless they give officers a particular reason to sus-
pect them of hiding contraband―is unworkable. The seriousness of
an offense is a poor predictor of who has contraband, and it would be
difficult to determine whether individual detainees fall within the
proposed exemption. Even persons arrested for a minor offense may
be coerced by others into concealing contraband. Exempting people
arrested for minor offenses from a standard search protocol thus may
put them at greater risk and result in more contraband being
brought into the detention facility.
   It also may be difficult to classify inmates by their current and pri-
or offenses before the intake search. Jail officials know little at the
outset about an arrestee, who may be carrying a false ID or lie about
his identity. The officers conducting an initial search often do not
have access to criminal history records. And those records can be in-
accurate or incomplete. Even with accurate information, officers
would encounter serious implementation difficulties. They would be
required to determine quickly whether any underlying offenses were
serious enough to authorize the more invasive search protocol. Other
possible classifications based on characteristics of individual detain-
ees also might prove to be unworkable or even give rise to charges of
discriminatory application. To avoid liability, officers might be in-
clined not to conduct a thorough search in any close case, thus creat-
ing unnecessary risk for the entire jail population. While the re-
strictions petitioner suggests would limit the intrusion on the privacy
of some detainees, it would be at the risk of increased danger to eve-
ryone in the facility, including the less serious offenders. The Fourth
and Fourteenth Amendments do not require adoption of the proposed
framework. Pp. 13−18, 19.
4     FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF 

                 COUNTY OF BURLINGTON

                         Syllabus


   KENNEDY, J., delivered the opinion of the Court, except as to Part IV.
ROBERTS, C. J., and SCALIA and ALITO, JJ., joined that opinion in full,
and THOMAS, J., joined as to all but Part IV. ROBERTS, C. J., and ALITO,
J., filed concurring opinions. BREYER, J., filed a dissenting opinion, in
which GINSBURG, SOTOMAYOR, and KAGAN, JJ., joined.
                        Cite as: 566 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–945
                                   _________________


 ALBERT W. FLORENCE, PETITIONER v. BOARD OF

   CHOSEN FREEHOLDERS OF THE COUNTY OF

             BURLINGTON ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                                 [April 2, 2012]


  JUSTICE KENNEDY delivered the opinion of the Court,
except as to Part IV.*
  Correctional officials have a legitimate interest, indeed
a responsibility, to ensure that jails are not made less
secure by reason of what new detainees may carry in on
their bodies. Facility personnel, other inmates, and the
new detainee himself or herself may be in danger if these
threats are introduced into the jail population. This case
presents the question of what rules, or limitations, the
Constitution imposes on searches of arrested persons who
are to be held in jail while their cases are being processed.
The term “jail” is used here in a broad sense to include
prisons and other detention facilities.         The specific
measures being challenged will be described in more
detail; but, in broad terms, the controversy concerns
whether every detainee who will be admitted to the gen-
eral population may be required to undergo a close visual
inspection while undressed.
  The case turns in part on the extent to which this Court
——————
 * JUSTICE THOMAS joins all but Part IV of this opinion.
2    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


has sufficient expertise and information in the record to
mandate, under the Constitution, the specific restrictions
and limitations sought by those who challenge the visual
search procedures at issue. In addressing this type of
constitutional claim courts must defer to the judgment of
correctional officials unless the record contains substantial
evidence showing their policies are an unnecessary or un-
justified response to problems of jail security. That
necessary showing has not been made in this case.
                              I
   In 1998, seven years before the incidents at issue, peti-
tioner Albert Florence was arrested after fleeing from
police officers in Essex County, New Jersey. He was
charged with obstruction of justice and use of a deadly
weapon. Petitioner entered a plea of guilty to two lesser
offenses and was sentenced to pay a fine in monthly in-
stallments. In 2003, after he fell behind on his payments
and failed to appear at an enforcement hearing, a bench
warrant was issued for his arrest. He paid the outstand-
ing balance less than a week later; but, for some unex-
plained reason, the warrant remained in a statewide
computer database.
   Two years later, in Burlington County, New Jersey,
petitioner and his wife were stopped in their automobile
by a state trooper. Based on the outstanding warrant in
the computer system, the officer arrested petitioner and
took him to the Burlington County Detention Center. He
was held there for six days and then was transferred to
the Essex County Correctional Facility. It is not the ar-
rest or confinement but the search process at each jail that
gives rise to the claims before the Court.
   Burlington County jail procedures required every ar-
restee to shower with a delousing agent. Officers would
check arrestees for scars, marks, gang tattoos, and contra-
band as they disrobed. App. to Pet. for Cert. 53a–56a.
                  Cite as: 566 U. S. ____ (2012)            3

                      Opinion of the Court

Petitioner claims he was also instructed to open his
mouth, lift his tongue, hold out his arms, turn around, and
lift his genitals. (It is not clear whether this last step was
part of the normal practice. See ibid.) Petitioner shared a
cell with at least one other person and interacted with
other inmates following his admission to the jail. Tr. of
Oral Arg. 17.
   The Essex County Correctional Facility, where peti-
tioner was taken after six days, is the largest county jail
in New Jersey. App. 70a. It admits more than 25,000 in-
mates each year and houses about 1,000 gang members at
any given time. When petitioner was transferred there,
all arriving detainees passed through a metal detector and
waited in a group holding cell for a more thorough search.
When they left the holding cell, they were instructed to
remove their clothing while an officer looked for body
markings, wounds, and contraband. Apparently without
touching the detainees, an officer looked at their ears,
nose, mouth, hair, scalp, fingers, hands, arms, armpits,
and other body openings. Id., at 57a–59a; App. to Pet.
for Cert. 137a–144a. This policy applied regardless of the
circumstances of the arrest, the suspected offense, or the
detainee’s behavior, demeanor, or criminal history. Peti-
tioner alleges he was required to lift his genitals, turn
around, and cough in a squatting position as part of the
process. After a mandatory shower, during which his
clothes were inspected, petitioner was admitted to the
facility. App. 3a–4a, 52a, 258a. He was released the next
day, when the charges against him were dismissed.
   Petitioner sued the governmental entities that operated
the jails, one of the wardens, and certain other defendants.
The suit was commenced in the United States District
Court for the District of New Jersey. Seeking relief under
42 U. S. C. §1983 for violations of his Fourth and Four-
teenth Amendment rights, petitioner maintained that per-
sons arrested for a minor offense could not be required
4    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


to remove their clothing and expose the most private areas
of their bodies to close visual inspection as a routine part
of the intake process. Rather, he contended, officials could
conduct this kind of search only if they had reason to
suspect a particular inmate of concealing a weapon, drugs,
or other contraband. The District Court certified a class of
individuals who were charged with a nonindictable offense
under New Jersey law, processed at either the Burlington
County or Essex County jail, and directed to strip naked
even though an officer had not articulated any reasonable
suspicion they were concealing contraband.
   After discovery, the court granted petitioner’s motion
for summary judgment on the unlawful search claim. It
concluded that any policy of “strip searching” nonindict-
able offenders without reasonable suspicion violated the
Fourth Amendment. A divided panel of the United States
Court of Appeals for the Third Circuit reversed, holding
that the procedures described by the District Court struck
a reasonable balance between inmate privacy and the
security needs of the two jails. 621 F. 3d 296 (2010). The
case proceeds on the understanding that the officers
searched detainees prior to their admission to the general
population, as the Court of Appeals seems to have as-
sumed. See id., at 298, 311. Petitioner has not argued
this factual premise is incorrect.
   The opinions in earlier proceedings, the briefs on file,
and some cases of this Court refer to a “strip search.” The
term is imprecise. It may refer simply to the instruction
to remove clothing while an officer observes from a dis-
tance of, say, five feet or more; it may mean a visual in-
spection from a closer, more uncomfortable distance; it
may include directing detainees to shake their heads or to
run their hands through their hair to dislodge what might
be hidden there; or it may involve instructions to raise
arms, to display foot insteps, to expose the back of the
ears, to move or spread the buttocks or genital areas, or to
                 Cite as: 566 U. S. ____ (2012)           5

                     Opinion of the Court

cough in a squatting position. In the instant case, the
term does not include any touching of unclothed areas
by the inspecting officer. There are no allegations that
the detainees here were touched in any way as part of the
searches.
  The Federal Courts of Appeals have come to differing
conclusions as to whether the Fourth Amendment requires
correctional officials to exempt some detainees who will be
admitted to a jail’s general population from the searches
here at issue. This Court granted certiorari to address the
question. 563 U. S. ___ (2011).
                              II
  The difficulties of operating a detention center must not
be underestimated by the courts. Turner v. Safley, 482
U. S. 78, 84–85 (1987). Jails (in the stricter sense of
the term, excluding prison facilities) admit more than 13
million inmates a year. See, e.g., Dept. of Justice, Bureau
of Justice Statistics, T. Minton, Jail Inmates at Midyear
2010—Statistical Tables 2 (2011). The largest facilities
process hundreds of people every day; smaller jails may be
crowded on weekend nights, after a large police operation,
or because of detainees arriving from other jurisdictions.
Maintaining safety and order at these institutions re-
quires the expertise of correctional officials, who must
have substantial discretion to devise reasonable solutions
to the problems they face. The Court has confirmed the
importance of deference to correctional officials and ex-
plained that a regulation impinging on an inmate’s consti-
tutional rights must be upheld “if it is reasonably related
to legitimate penological interests.” Turner, supra, at 89;
see Overton v. Bazzetta, 539 U. S. 126, 131–132 (2003).
But see Johnson v. California, 543 U. S. 499, 510–511
(2005) (applying strict scrutiny to racial classifications).
  The Court’s opinion in Bell v. Wolfish, 441 U. S. 520
(1979), is the starting point for understanding how this
6    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


framework applies to Fourth Amendment challenges.
That case addressed a rule requiring pretrial detainees
in any correctional facility run by the Federal Bureau of
Prisons “to expose their body cavities for visual inspection
as a part of a strip search conducted after every contact
visit with a person from outside the institution.” Id., at
558. Inmates at the federal Metropolitan Correctional
Center in New York City argued there was no security
justification for these searches. Officers searched guests
before they entered the visiting room, and the inmates
were under constant surveillance during the visit. Id., at
577–578 (Marshall, J., dissenting). There had been but
one instance in which an inmate attempted to sneak con-
traband back into the facility. See id., at 559 (majority
opinion). The Court nonetheless upheld the search policy.
It deferred to the judgment of correctional officials that
the inspections served not only to discover but also to
deter the smuggling of weapons, drugs, and other prohib-
ited items inside. Id., at 558. The Court explained that
there is no mechanical way to determine whether intru-
sions on an inmate’s privacy are reasonable. Id., at 559.
The need for a particular search must be balanced against
the resulting invasion of personal rights. Ibid.
   Policies designed to keep contraband out of jails and
prisons have been upheld in cases decided since Bell. In
Block v. Rutherford, 468 U. S. 576 (1984), for example, the
Court concluded that the Los Angeles County Jail could
ban all contact visits because of the threat they posed:
    “They open the institution to the introduction of
    drugs, weapons, and other contraband. Visitors can
    easily conceal guns, knives, drugs, or other contra-
    band in countless ways and pass them to an inmate
    unnoticed by even the most vigilant observers. And
    these items can readily be slipped from the clothing of
    an innocent child, or transferred by other visitors
                 Cite as: 566 U. S. ____ (2012)            7

                     Opinion of the Court

    permitted close contact with inmates.” Id., at 586.
There were “many justifications” for imposing a general
ban rather than trying to carve out exceptions for certain
detainees. Id., at 587. Among other problems, it would be
“a difficult if not impossible task” to identify “inmates who
have propensities for violence, escape, or drug smuggling.”
Ibid. This was made “even more difficult by the brevity of
detention and the constantly changing nature of the in-
mate population.” Ibid.
   The Court has also recognized that deterring the posses-
sion of contraband depends in part on the ability to con-
duct searches without predictable exceptions. In Hudson
v. Palmer, 468 U. S. 517 (1984), it addressed the question
of whether prison officials could perform random searches
of inmate lockers and cells even without reason to suspect
a particular individual of concealing a prohibited item.
Id., at 522–523. The Court upheld the constitutionality of
the practice, recognizing that “ ‘[f]or one to advocate that
prison searches must be conducted only pursuant to an
enunciated general policy or when suspicion is directed at
a particular inmate is to ignore the realities of prison
operation.’ ” Id., at 529 (quoting Marrero v. Common-
wealth, 222 Va. 754, 757, 284 S. E. 2d 809, 811 (1981)).
Inmates would adapt to any pattern or loopholes they
discovered in the search protocol and then undermine the
security of the institution. 468 U. S., at 529.
   These cases establish that correctional officials must be
permitted to devise reasonable search policies to detect
and deter the possession of contraband in their facilities.
See Bell, 441 U. S., at 546 (“[M]aintaining institutional
security and preserving internal order and discipline are
essential goals that may require limitation or retraction of
retained constitutional rights of both convicted prisoners
and pretrial detainees”). The task of determining whether
a policy is reasonably related to legitimate security inter-
8    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


ests is “peculiarly within the province and professional
expertise of corrections officials.” Id., at 548. This Court
has repeated the admonition that, “ ‘in the absence of
substantial evidence in the record to indicate that the
officials have exaggerated their response to these consid-
erations courts should ordinarily defer to their expert
judgment in such matters.’ ” Block, supra, at 584–585;
Bell, supra, at 548.
   In many jails officials seek to improve security by re-
quiring some kind of strip search of everyone who is to be
detained. These procedures have been used in different
places throughout the country, from Cranston, Rhode
Island, to Sapulpa, Oklahoma, to Idaho Falls, Idaho. See
Roberts v. Rhode Island, 239 F. 3d 107, 108–109 (CA1
2001); Chapman v. Nichols, 989 F. 2d 393, 394 (CA10
1993); Giles v. Ackerman, 746 F. 2d 614, 615 (CA9 1984)
(per curiam); see also, e.g., Bull v. City and Cty. of San
Francisco, 595 F. 3d 964 (CA9 2010) (en banc) (San Fran-
cisco, California); Powell v. Barrett, 541 F. 3d 1298 (CA11
2008) (en banc) (Fulton Cty., Ga.); Masters v. Crouch, 872
F. 2d 1248, 1251 (CA6 1989) (Jefferson Cty., Ky.); Weber v.
Dell, 804 F. 2d 796, 797–798 (CA2 1986) (Monroe Cty.,
N. Y.); Stewart v. Lubbock Cty., 767 F. 2d 153, 154 (CA5
1985) (Lubbock Cty., Tex.).
   Persons arrested for minor offenses may be among the
detainees processed at these facilities. This is, in part, a
consequence of the exercise of state authority that was the
subject of Atwater v. Lago Vista, 532 U. S. 318 (2001).
Atwater addressed the perhaps more fundamental ques-
tion of who may be deprived of liberty and taken to jail in
the first place. The case involved a woman who was ar-
rested after a police officer noticed neither she nor her
children were wearing their seatbelts. The arrestee ar-
gued the Fourth Amendment prohibited her custodial
arrest without a warrant when an offense could not result
in jail time and there was no compelling need for immedi-
                 Cite as: 566 U. S. ____ (2012)           9

                     Opinion of the Court

ate detention. Id., at 346. The Court held that a Fourth
Amendment restriction on this power would put officers in
an “almost impossible spot.” Id., at 350. Their ability to
arrest a suspect would depend in some cases on the pre-
cise weight of drugs in his pocket, whether he was a repeat
offender, and the scope of what counted as a compelling
need to detain someone. Id., at 348–349. The Court re-
jected the proposition that the Fourth Amendment barred
custodial arrests in a set of these cases as a matter of
constitutional law. It ruled, based on established princi-
ples, that officers may make an arrest based upon proba-
ble cause to believe the person has committed a criminal
offense in their presence. See id., at 354. The Court
stated that “a responsible Fourth Amendment balance is
not well served by standards requiring sensitive, case-by-
case determinations of government need, lest every discre-
tionary judgment in the field be converted into an occasion
for constitutional review.” Id., at 347.
   Atwater did not address whether the Constitution im-
poses special restrictions on the searches of offenders
suspected of committing minor offenses once they are
taken to jail. Some Federal Courts of Appeals have held
that corrections officials may not conduct a strip search of
these detainees, even if no touching is involved, absent
reasonable suspicion of concealed contraband. 621 F. 3d,
at 303–304, and n. 4. The Courts of Appeals to address
this issue in the last decade, however, have come to the
opposite conclusion. See 621 F. 3d 296 (case below); Bame
v. Dillard, 637 F. 3d 380 (CADC 2011); Powell, supra;
Bull, supra. The current case is set against this precedent
and governed by the principles announced in Turner and
Bell.
                            III
  The question here is whether undoubted security im-
peratives involved in jail supervision override the asser-
10   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


tion that some detainees must be exempt from the more
invasive search procedures at issue absent reasonable
suspicion of a concealed weapon or other contraband. The
Court has held that deference must be given to the offi-
cials in charge of the jail unless there is “substantial
evidence” demonstrating their response to the situation is
exaggerated. Block, 468 U. S., at 584–585 (internal quota-
tion marks omitted). Petitioner has not met this standard,
and the record provides full justifications for the proce-
dures used.
                                A
  Correctional officials have a significant interest in con-
ducting a thorough search as a standard part of the intake
process. The admission of inmates creates numerous risks
for facility staff, for the existing detainee population, and
for a new detainee himself or herself. The danger of intro-
ducing lice or contagious infections, for example, is well
documented. See, e.g., Deger & Quick, The Enduring
Menace of MRSA: Incidence, Treatment, and Prevention
in a County Jail, 15 J. Correctional Health Care 174, 174–
175, 177–178 (2009); Bick, Infection Control in Jails and
Prisons, 45 Healthcare Epidemiology 1047, 1049 (2007).
The Federal Bureau of Prisons recommends that staff
screen new detainees for these conditions. See Clinical
Practice Guidelines, Management of Methicillin-Resistant
Staphylococcus aureus (MRSA) Infections 2 (2011); Clini-
cal Practice Guidelines, Lice and Scabies Protocol 1 (2011).
Persons just arrested may have wounds or other injuries
requiring immediate medical attention. It may be difficult
to identify and treat these problems until detainees re-
move their clothes for a visual inspection. See Prison and
Jail Administration: Practice and Theory 142 (P. Carlson
& G. Garrett eds., 2d ed. 2008) (hereinafter Carlson &
Garrett).
  Jails and prisons also face grave threats posed by the
                 Cite as: 566 U. S. ____ (2012)          11

                     Opinion of the Court

increasing number of gang members who go through the
intake process. See Brief for Policemen’s Benevolent As-
sociation, Local 249, et al. as Amici Curiae 14 (hereinaf-
ter PBA Brief); New Jersey Comm’n of Investigation,
Gangland Behind Bars: How and Why Organized Criminal
Street Gangs Thrive in New Jersey’s Prisons . . . And
What Can Be Done About It 10–11 (2009). “Gang rivalries
spawn a climate of tension, violence, and coercion.” Carl-
son & Garrett 462. The groups recruit new members by
force, engage in assaults against staff, and give other
inmates a reason to arm themselves. Ibid. Fights among
feuding gangs can be deadly, and the officers who must
maintain order are put in harm’s way. PBA Brief 17.
These considerations provide a reasonable basis to justify
a visual inspection for certain tattoos and other signs of
gang affiliation as part of the intake process. The identi-
fication and isolation of gang members before they are
admitted protects everyone in the facility. Cf. Fraise v.
Terhune, 283 F. 3d 506, 509–510 (CA3 2002) (Alito, J.)
(describing a statewide policy authorizing the identifica-
tion and isolation of gang members in prison).
   Detecting contraband concealed by new detainees, fur-
thermore, is a most serious responsibility. Weapons,
drugs, and alcohol all disrupt the safe operation of a jail.
Cf. Hudson, 468 U. S., at 528 (recognizing “the constant
fight against the proliferation of knives and guns, illicit
drugs, and other contraband”). Correctional officers have
had to confront arrestees concealing knives, scissors, razor
blades, glass shards, and other prohibited items on their
person, including in their body cavities. See Bull, 595
F. 3d, at 967, 969; Brief for New Jersey County Jail War-
dens Association as Amicus Curiae 17–18 (hereinafter
New Jersey Wardens Brief). They have also found crack,
heroin, and marijuana. Brief for City and County of San
Francisco et al. as Amici Curiae 9–11 (hereinafter San
Francisco Brief). The use of drugs can embolden inmates
12   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


in aggression toward officers or each other; and, even
apart from their use, the trade in these substances can
lead to violent confrontations. See PBA Brief 11.
   There are many other kinds of contraband. The text-
book definition of the term covers any unauthorized item.
See Prisons: Today and Tomorrow 237 (J. Pollock ed.
1997) (“Contraband is any item that is possessed in viola-
tion of prison rules. Contraband obviously includes drugs
or weapons, but it can also be money, cigarettes, or even
some types of clothing”). Everyday items can undermine
security if introduced into a detention facility:
     “Lighters and matches are fire and arson risks or po-
     tential weapons. Cell phones are used to orchestrate
     violence and criminality both within and without jail-
     house walls. Pills and medications enhance suicide
     risks. Chewing gum can block locking devices; hair-
     pins can open handcuffs; wigs can conceal drugs and
     weapons.” New Jersey Wardens Brief 8–9.
Something as simple as an overlooked pen can pose a
significant danger. Inmates commit more than 10,000
assaults on correctional staff every year and many more
among themselves. See Dept. of Justice, Bureau of Justice
Statistics, J. Stephan & J. Karberg, Census of State and
Federal Correctional Facilities, 2000, p. v (2003).
   Contraband creates additional problems because scarce
items, including currency, have value in a jail’s culture
and underground economy. Correctional officials inform
us “[t]he competition . . . for such goods begets violence,
extortion, and disorder.” New Jersey Wardens Brief 2.
Gangs exacerbate the problem. They “orchestrate thefts,
commit assaults, and approach inmates in packs to take
the contraband from the weak.” Id., at 9–10. This puts
the entire facility, including detainees being held for a
brief term for a minor offense, at risk. Gangs do coerce
inmates who have access to the outside world, such as
                 Cite as: 566 U. S. ____ (2012)           13

                     Opinion of the Court

people serving their time on the weekends, to sneak things
into the jail. Id., at 10; see, e.g., Pugmire, Vegas Suspect
Has Term to Serve, Los Angeles Times, Sept. 23, 2005,
p. B1 (“Weekend-only jail sentences are a common punish-
ment for people convicted of nonviolent drug crimes . . .”).
These inmates, who might be thought to pose the least
risk, have been caught smuggling prohibited items into
jail. See New Jersey Wardens Brief 10. Concealing con-
traband often takes little time and effort. It might be done
as an officer approaches a suspect’s car or during a brief
commotion in a group holding cell. Something small
might be tucked or taped under an armpit, behind an ear,
between the buttocks, in the instep of a foot, or inside the
mouth or some other body cavity.
   It is not surprising that correctional officials have
sought to perform thorough searches at intake for disease,
gang affiliation, and contraband. Jails are often crowded,
unsanitary, and dangerous places. There is a substantial
interest in preventing any new inmate, either of his own
will or as a result of coercion, from putting all who live or
work at these institutions at even greater risk when he is
admitted to the general population.
                             B
  Petitioner acknowledges that correctional officials must
be allowed to conduct an effective search during the intake
process and that this will require at least some detainees
to lift their genitals or cough in a squatting position.
These procedures, similar to the ones upheld in Bell, are
designed to uncover contraband that can go undetected by
a patdown, metal detector, and other less invasive
searches. See Brief for United States as Amicus Curiae 23
(hereinafter United States Brief); New Jersey Wardens
Brief 19, n. 6. Petitioner maintains there is little benefit
to conducting these more invasive steps on a new detainee
who has not been arrested for a serious crime or for any
14   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


offense involving a weapon or drugs. In his view these de-
tainees should be exempt from this process unless they
give officers a particular reason to suspect them of hiding
contraband. It is reasonable, however, for correctional
officials to conclude this standard would be unworkable.
The record provides evidence that the seriousness of an
offense is a poor predictor of who has contraband and
that it would be difficult in practice to determine whether
individual detainees fall within the proposed exemption.
                             1
  People detained for minor offenses can turn out to be
the most devious and dangerous criminals. Cf. Clements v.
Logan, 454 U. S. 1304, 1305 (1981) (Rehnquist, J., in
chambers) (deputy at a detention center shot by misde-
meanant who had not been strip searched). Hours after
the Oklahoma City bombing, Timothy McVeigh was
stopped by a state trooper who noticed he was driving
without a license plate. Johnston, Suspect Won’t Answer
Any Questions, N. Y. Times, Apr. 25, 1995, p. A1. Police
stopped serial killer Joel Rifkin for the same reason.
McQuiston, Confession Used to Portray Rifkin as Method-
ical Killer, N. Y. Times, Apr. 26, 1994, p. B6. One of
the terrorists involved in the September 11 attacks was
stopped and ticketed for speeding just two days before
hijacking Flight 93. The Terrorists: Hijacker Got a Speed-
ing Ticket, N. Y. Times, Jan. 8, 2002, p. A12. Reasonable
correctional officials could conclude these uncertainties
mean they must conduct the same thorough search of
everyone who will be admitted to their facilities.
  Experience shows that people arrested for minor of-
fenses have tried to smuggle prohibited items into jail,
sometimes by using their rectal cavities or genitals for the
concealment. They may have some of the same incentives
as a serious criminal to hide contraband. A detainee
might risk carrying cash, cigarettes, or a penknife to
                  Cite as: 566 U. S. ____ (2012)           15

                      Opinion of the Court

survive in jail. Others may make a quick decision to hide
unlawful substances to avoid getting in more trouble at
the time of their arrest. This record has concrete exam-
ples. Officers at the Atlantic County Correctional Facility,
for example, discovered that a man arrested for driving
under the influence had “2 dime bags of weed, 1 pack of
rolling papers, 20 matches, and 5 sleeping pills” taped
under his scrotum. Brief for Atlantic County et al. as
Amici Curiae 36 (internal quotation marks omitted). A
person booked on a misdemeanor charge of disorderly
conduct in Washington State managed to hide a lighter,
tobacco, tattoo needles, and other prohibited items in his
rectal cavity. See United States Brief 25, n. 15. San
Francisco officials have discovered contraband hidden in
body cavities of people arrested for trespassing, public
nuisance, and shoplifting. San Francisco Brief 3. There
have been similar incidents at jails throughout the coun-
try. See United States Brief 25, n. 15.
  Even if people arrested for a minor offense do not them-
selves wish to introduce contraband into a jail, they may
be coerced into doing so by others. See New Jersey War-
dens Brief 16; cf. Block, 468 U. S., at 587 (“It is not unrea-
sonable to assume, for instance, that low security risk
detainees would be enlisted to help obtain contraband or
weapons by their fellow inmates who are denied contact
visits”). This could happen any time detainees are held in
the same area, including in a van on the way to the station
or in the holding cell of the jail. If, for example, a person
arrested and detained for unpaid traffic citations is not
subject to the same search as others, this will be well
known to other detainees with jail experience. A hardened
criminal or gang member can, in just a few minutes, ap-
proach the person and coerce him into hiding the fruits of
a crime, a weapon, or some other contraband. As an ex-
pert in this case explained, “the interaction and mingling
between misdemeanants and felons will only increase the
16   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of the Court 


amount of contraband in the facility if the jail can only
conduct admission searches on felons.” App. 381a. Ex-
empting people arrested for minor offenses from a stand-
ard search protocol thus may put them at greater risk and
result in more contraband being brought into the deten-
tion facility. This is a substantial reason not to mandate
the exception petitioner seeks as a matter of constitutional
law.
                              2
  It also may be difficult, as a practical matter, to classify
inmates by their current and prior offenses before the
intake search. Jails can be even more dangerous than
prisons because officials there know so little about the
people they admit at the outset. See New Jersey Wardens
Brief 11–14. An arrestee may be carrying a false ID or lie
about his identity. The officers who conduct an initial
search often do not have access to criminal history records.
See, e.g., App. 235a; New Jersey Wardens Brief 13. And
those records can be inaccurate or incomplete. See De-
partment of Justice v. Reporters Comm. for Freedom of
Press, 489 U. S. 749, 752 (1989). Petitioner’s rap sheet is
an example. It did not reflect his previous arrest for pos-
session of a deadly weapon. Tr. of Oral Arg. 18–19. In
the absence of reliable information it would be illogical to
require officers to assume the arrestees in front of them do
not pose a risk of smuggling something into the facility.
  The laborious administration of prisons would become
less effective, and likely less fair and evenhanded, were
the practical problems inevitable from the rules suggested
by petitioner to be imposed as a constitutional mandate.
Even if they had accurate information about a detainee’s
current and prior arrests, officers, under petitioner’s pro-
posed regime, would encounter serious implementation
difficulties. They would be required, in a few minutes, to
determine whether any of the underlying offenses were
                 Cite as: 566 U. S. ____ (2012)           17

                     Opinion of the Court

serious enough to authorize the more invasive search
protocol. Other possible classifications based on charac-
teristics of individual detainees also might prove to be
unworkable or even give rise to charges of discriminatory
application. Most officers would not be well equipped to
make any of these legal determinations during the pres-
sures of the intake process. Bull, 595 F. 3d, at 985–987
(Kozinski, C. J., concurring); see also Welsh v. Wisconsin,
466 U. S. 740, 761–762 (1984) (White, J., dissenting)
(“[T]he Court’s approach will necessitate a case-by-case
evaluation of the seriousness of particular crimes, a dif-
ficult task for which officers and courts are poorly
equipped”). To avoid liability, officers might be inclined
not to conduct a thorough search in any close case, thus
creating unnecessary risk for the entire jail population.
Cf. Atwater, 532 U. S., at 351, and n. 22.
   The Court addressed an analogous problem in Atwater.
The petitioner in that case argued the Fourth Amendment
prohibited a warrantless arrest when being convicted of
the suspected crime “could not ultimately carry any jail
time” and there was “no compelling need for immediate
detention.” Id., at 346. That rule “promise[d] very little in
the way of administrability.” Id., at 350. Officers could
not be expected to draw the proposed lines on a moment’s
notice, and the risk of violating the Constitution would
have discouraged them from arresting criminals in any
questionable circumstances. Id., at 350–351 (“An officer
not quite sure the drugs weighed enough to warrant jail
time or not quite certain about a suspect’s risk of flight
would not arrest, even though it could perfectly well turn
out that, in fact, the offense called for incarceration and
the defendant was long gone on the day of trial”). The
Fourth Amendment did not compel this result in Atwater.
The Court held that officers who have probable cause to
believe even a minor criminal offense has been committed
in their presence may arrest the offender. See id., at 354.
18   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON

                   Opinion of Kthe Court 

                    Opinion of ENNEDY, J.

Individual jurisdictions can of course choose “to impose
more restrictive safeguards through statutes limiting
warrantless arrests for minor offenders.” Id., at 352.
   One of the central principles in Atwater applies with
equal force here. Officers who interact with those sus-
pected of violating the law have an “essential interest in
readily administrable rules.” Id., at 347; accord, New York
v. Belton, 453 U. S. 454, 458 (1981). The officials in charge
of the jails in this case urge the Court to reject any compli-
cated constitutional scheme requiring them to conduct less
thorough inspections of some detainees based on their
behavior, suspected offense, criminal history, and other
factors. They offer significant reasons why the Constitu-
tion must not prevent them from conducting the same
search on any suspected offender who will be admitted to
the general population in their facilities. The restrictions
suggested by petitioner would limit the intrusion on the
privacy of some detainees but at the risk of increased
danger to everyone in the facility, including the less seri-
ous offenders themselves.
                             IV
  This case does not require the Court to rule on the types
of searches that would be reasonable in instances where,
for example, a detainee will be held without assignment to
the general jail population and without substantial contact
with other detainees. This describes the circumstances in
Atwater. See 532 U. S., at 324 (“Officers took Atwater’s
‘mug shot’ and placed her, alone, in a jail cell for about one
hour, after which she was taken before a magistrate and
released on $310 bond”). The accommodations provided in
these situations may diminish the need to conduct some
aspects of the searches at issue. Cf. United States Brief 30
(discussing the segregation, and less invasive searches, of
individuals held by the Federal Bureau of Prisons for
misdemeanors or civil contempt). The circumstances
                 Cite as: 566 U. S. ____ (2012)           19

                     Opinion of the Court

before the Court, however, do not present the opportunity
to consider a narrow exception of the sort JUSTICE ALITO
describes, post, at 2–3 (concurring opinion), which might
restrict whether an arrestee whose detention has not yet
been reviewed by a magistrate or other judicial officer,
and who can be held in available facilities removed from
the general population, may be subjected to the types of
searches at issue here.
   Petitioner’s amici raise concerns about instances of
officers engaging in intentional humiliation and other
abusive practices. See Brief for Sister Bernie Galvin et al.
as Amici Curiae; see also Hudson, 468 U. S., at 528
(“[I]ntentional harassment of even the most hardened
criminals cannot be tolerated by a civilized society”); Bell,
441 U. S., at 560. There also may be legitimate concerns
about the invasiveness of searches that involve the touch-
ing of detainees. These issues are not implicated on the
facts of this case, however, and it is unnecessary to con-
sider them here.
                           V
  Even assuming all the facts in favor of petitioner, the
search procedures at the Burlington County Detention
Center and the Essex County Correctional Facility struck
a reasonable balance between inmate privacy and the
needs of the institutions. The Fourth and Fourteenth
Amendments do not require adoption of the framework of
rules petitioner proposes.
  The judgment of the Court of Appeals for the Third
Circuit is affirmed.
                                         It is so ordered.
                 Cite as: 566 U. S. ____ (2012)            1

                   ROBERTS, C. J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–945
                         _________________


 ALBERT W. FLORENCE, PETITIONER v. BOARD OF

   CHOSEN FREEHOLDERS OF THE COUNTY OF

             BURLINGTON ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                        [April 2, 2012]


  CHIEF JUSTICE ROBERTS, concurring.
  I join the opinion of the Court. As with JUSTICE ALITO,
however, it is important for me that the Court does not
foreclose the possibility of an exception to the rule it an-
nounces. JUSTICE KENNEDY explains that the circum-
stances before it do not afford an opportunity to consider
that possibility. Ante, at 18–19. Those circumstances
include the facts that Florence was detained not for a
minor traffic offense but instead pursuant to a warrant for
his arrest, and that there was apparently no alternative, if
Florence were to be detained, to holding him in the gen-
eral jail population.
  Factual nuances have not played a significant role as
this case has been presented to the Court. Both courts
below regarded acknowledged factual disputes as “imma-
terial” to their conflicting dispositions, 621 F. 3d 296, 300
(CA3 2010), and before this Court Florence challenged
suspicionless strip searches “no matter what the circum-
stances.” Pet. for Cert. i.
  The Court makes a persuasive case for the general
applicability of the rule it announces. The Court is none-
theless wise to leave open the possibility of exceptions, to
ensure that we “not embarrass the future.” Northwest
Airlines, Inc. v. Minnesota, 322 U. S. 292, 300 (1944)
(Frankfurter, J.).
                 Cite as: 566 U. S. ____ (2012)           1

                     ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–945
                         _________________


 ALBERT W. FLORENCE, PETITIONER v. BOARD OF

   CHOSEN FREEHOLDERS OF THE COUNTY OF

             BURLINGTON ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE THIRD CIRCUIT

                        [April 2, 2012]


   JUSTICE ALITO, concurring.
   I join the opinion of the Court but emphasize the limits
of today’s holding. The Court holds that jail adminis-
trators may require all arrestees who are committed to
the general population of a jail to undergo visual strip
searches not involving physical contact by corrections
officers. To perform the searches, officers may direct the
arrestees to disrobe, shower, and submit to a visual in-
spection. As part of the inspection, the arrestees may be
required to manipulate their bodies.
   Undergoing such an inspection is undoubtedly humiliat-
ing and deeply offensive to many, but there are reason-
able grounds for strip searching arrestees before they are
admitted to the general population of a jail. As the Court
explains, there is a serious danger that some detainees
will attempt to smuggle weapons, drugs, or other contra-
band into the jail. Some detainees may have lice, which
can easily spread to others in the facility, and some de-
tainees may have diseases or injuries for which the jail
is required to provide medical treatment. In addition, if a
detainee with gang-related tattoos is inadvertently housed
with detainees from a rival gang, violence may ensue.
   Petitioner and the dissent would permit corrections
officers to conduct the visual strip search at issue here
2     FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                 COUNTY OF BURLINGTON

                    ALITO, J., concurring


only if the officers have a reasonable basis for thinking
that a particular arrestee may present a danger to other
detainees or members of the jail staff. But as the Court
explains, corrections officers are often in a very poor posi-
tion to make such a determination, and the threat to the
health and safety of detainees and staff, should the offic-
ers miscalculate, is simply too great.
   It is important to note, however, that the Court does not
hold that it is always reasonable to conduct a full strip
search of an arrestee whose detention has not been re-
viewed by a judicial officer and who could be held in avail-
able facilities apart from the general population. Most of
those arrested for minor offenses are not dangerous, and
most are released from custody prior to or at the time of
their initial appearance before a magistrate. In some
cases, the charges are dropped. In others, arrestees are
released either on their own recognizance or on minimal
bail. In the end, few are sentenced to incarceration. For
these persons, admission to the general jail population,
with the concomitant humiliation of a strip search, may
not be reasonable, particularly if an alternative procedure
is feasible. For example, the Federal Bureau of Prisons
(BOP) and possibly even some local jails appear to segre-
gate temporary detainees who are minor offenders from
the general population. See, e.g., Brief for United States
as Amicus Curiae 30; Bull v. City & Cty. of San Francisco,
595 F. 3d 964, 968 (CA9 2010) (en banc).*
——————
  * In its amicus brief, the United States informs us that, according to
BOP policy, prison and jail officials cannot subject persons arrested for
misdemeanor or civil contempt offenses to visual body-cavity searches
without their consent or without reasonable suspicion that they are
concealing contraband. Brief for United States 30. Those who are not
searched must be housed separately from the inmates in the general
population. Ibid. Similarly, as described by the Court of Appeals in
Bull, 595 F. 3d 964, the San Francisco County jail system distinguishes
between arrestees who are eligible for release because, for instance,
they can post bail within 12 hours and those who must be housed for an
                     Cite as: 566 U. S. ____ (2012)                    3

                          ALITO, J., concurring

   The Court does not address whether it is always reason-
able, without regard to the offense or the reason for deten-
tion, to strip search an arrestee before the arrestee’s de-
tention has been reviewed by a judicial officer. The lead
opinion explicitly reserves judgment on that question. See
ante, at 18–19. In light of that limitation, I join the opin-
ion of the Court in full.




——————
extended period of time. Id., at 968. The former are kept in holding
cells at a temporary intake and release facility where they are pat
searched and scanned with a metal detector but apparently are not
strip searched. Ibid. The latter are transported to a jail with custodial
housing facilities where they are then strip searched prior to their
admission into the general population. Ibid.
                 Cite as: 566 U. S. ____ (2012)           1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–945
                         _________________


 ALBERT W. FLORENCE, PETITIONER v. BOARD OF 

   CHOSEN FREEHOLDERS OF THE COUNTY OF 

             BURLINGTON ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE THIRD CIRCUIT

                        [April 2, 2012]


  JUSTICE BREYER, with whom JUSTICE GINSBURG,
JUSTICE SOTOMAYOR, and JUSTICE KAGAN join, dissenting.
  The petition for certiorari asks us to decide
“[w]hether the Fourth Amendment permits a . . . suspi-
cionless strip search of every individual arrested for
any minor offense . . . .” Pet. for Cert. i. This question
is phrased more broadly than what is at issue. The
case is limited to strip searches of those arrestees
entering a jail’s general population, see 621 F. 3d 296,
298 (CA3 2010). And the kind of strip search in ques-
tion involves more than undressing and taking a
shower (even if guards monitor the shower area for
threatened disorder). Rather, the searches here in-
volve close observation of the private areas of a per-
son’s body and for that reason constitute a far more
serious invasion of that person’s privacy.
  The visually invasive kind of strip search at issue
here is not unique. A similar practice is well described
in Dodge v. County of Orange, 282 F. Supp. 2d 41
(SDNY 2003). In that New York case, the “strip
search” (as described in a relevant prison manual)
involved:
    “ ‘a visual inspection of the inmate’s naked body. This
    should include the inmate opening his mouth and
2    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF 

                COUNTY OF BURLINGTON

                   BREYER, J., dissenting 


    moving his tongue up and down and from side to side,
    removing any dentures, running his hands through
    his hair, allowing his ears to be visually examined,
    lifting his arms to expose his arm pits, lifting his feet
    to examine the sole, spreading and/or lifting his testi-
    cles to expose the area behind them and bending over
    and/or spreading the cheeks of his buttocks to expose
    his anus. For females, the procedures are similar ex-
    cept females must in addition, squat to expose the
    vagina.’ ” Id., at 46.
Because the Dodge court obtained considerable empirical
information about the need for such a search in respect
to minor offenders, and because the searches alleged in
this case do not differ significantly, I shall use the succinct
Dodge description as a template for the kind of strip
search to which the Question Presented refers. See, e.g.,
App. to Pet. for Cert. 3a–4a (alleging that officers in-
spected his genitals from an arm’s length away, required
him to lift his genitals, and examined his anal cavity).
  In my view, such a search of an individual arrested for a
minor offense that does not involve drugs or violence—say
a traffic offense, a regulatory offense, an essentially civil
matter, or any other such misdemeanor—is an “unreason-
able searc[h]” forbidden by the Fourth Amendment, unless
prison authorities have reasonable suspicion to believe
that the individual possesses drugs or other contraband.
And I dissent from the Court’s contrary determination.
                             I
   Those confined in prison retain basic constitutional
rights. Bell v. Wolfish, 441 U. S. 520, 545 (1979); Turner
v. Safley, 482 U. S. 78, 84 (1987) (“Prison walls do not
form a barrier separating prison inmates from the protec-
tions of the Constitution”). The constitutional right at
issue here is the Fourth Amendment right to be free of
“unreasonable searches and seizures.” And, as the Court
                 Cite as: 566 U. S. ____ (2012)            3

                     BREYER, J., dissenting

notes, the applicable standard is the Fourth Amendment
balancing inquiry announced regarding prison inmates in
Bell v. Wolfish, supra. The Court said:
    “The test of reasonableness under the Fourth
    Amendment is not capable of precise definition or me-
    chanical application. In each case it requires a bal-
    ancing of the need for the particular search against
    the invasion of personal rights that the search entails.
    Courts must consider the scope of the particular in-
    trusion, the manner in which it is conducted, the justi-
    fication for initiating it, and the place in which it is
    conducted.” Id., at 559.
I have described in general terms, see supra, at 1–2, the
place, scope and manner of “the particular intrusion.”
Bell, 441 U. S., at 559. I now explain why I believe that
the “invasion of personal rights” here is very serious and
lacks need or justification, ibid.—at least as to the cate-
gory of minor offenders at issue.
                             II
   A strip search that involves a stranger peering without
consent at a naked individual, and in particular at the
most private portions of that person’s body, is a serious in-
vasion of privacy. We have recently said, in respect to a
schoolchild (and a less intrusive search), that the “mean-
ing of such a search, and the degradation its subject may
reasonably feel, place a search that intrusive in a category
of its own demanding its own specific suspicions.” Safford
Unified School Dist. #1 v. Redding, 557 U. S. ___, ___
(2009) (slip op., at 11). The Courts of Appeals have more
directly described the privacy interests at stake, writing,
for example, that practices similar to those at issue here
are “demeaning, dehumanizing, undignified, humiliating,
terrifying, unpleasant, embarrassing, [and] repulsive,
signifying degradation and submission.” Mary Beth G. v.
4    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF 

                COUNTY OF BURLINGTON

                   BREYER, J., dissenting 


Chicago, 723 F. 2d 1263, 1272 (CA7 1984) (internal quota-
tion marks omitted); see also, e.g., Blackburn v. Snow, 771
F. 2d 556, 564 (CA1 1985) (“ ‘[A]ll courts’ ” have recognized
the “ ‘ severe if not gross interference with a person’s pri-
vacy’ ” that accompany visual body cavity searches (quoting
Arruda v. Fair, 710 F. 2d 886, 887 (CA1 1983))). These
kinds of searches also gave this Court the “most pause” in
Bell, supra, at 558 (guards strip searched prisoners after
they received outside visits). Even when carried out in a
respectful manner, and even absent any physical touching,
see ante at 4–5, 19, such searches are inherently harmful,
humiliating, and degrading. And the harm to privacy
interests would seem particularly acute where the person
searched may well have no expectation of being subject
to such a search, say, because she had simply received a
traffic ticket for failing to buckle a seatbelt, because he
had not previously paid a civil fine, or because she had
been arrested for a minor trespass.
   In Atwater v. Lago Vista, 532 U. S. 318, 323–324 (2001),
for example, police arrested a mother driving with her two
children because their seat belts were not buckled. This
Court held that the Constitution did not forbid an arrest
for a minor seatbelt offense. Id., at 323. But, in doing so,
it pointed out that the woman was held for only an hour
(before being taken to a magistrate and released on bond)
and that the search—she had to remove her shoes, jew-
elry, and the contents of her pockets, id., at 355—was not
“ ‘unusually harmful to [her] privacy or . . . physical inter-
ests.’ ” Id., at 354 (quoting Whren v. United States, 517
U. S. 806, 818 (1996)). Would this Court have upheld the
arrest had the magistrate not been immediately available,
had the police housed her overnight in the jail, and had
they subjected her to a search of the kind at issue here?
Cf. County of Riverside v. McLaughlin, 500 U. S. 44, 56
(1991) (presentment must be within 48 hours after arrest).
   The petitioner, Albert W. Florence, states that his pre-
                 Cite as: 566 U. S. ____ (2012)            5

                     BREYER, J., dissenting

sent arrest grew out of an (erroneous) report that he had
failed to pay a minor civil fine previously assessed because
he had hindered a prosecution (by fleeing police officers
in his automobile). App. 25a–26a. He alleges that he was
held for six days in jail before being taken to a magistrate
and that he was subjected to two strip searches of the kind
in question. App. to Pet. for Cert. 3a.
   Amicus briefs present other instances in which individ-
uals arrested for minor offenses have been subjected to
the humiliations of a visual strip search. They include a
nun, a Sister of Divine Providence for 50 years, who was ar-
rested for trespassing during an antiwar demonstration.
Brief for Sister Bernie Galvin et al. as Amici Curiae 6.
They include women who were strip-searched during
periods of lactation or menstruation. Id., at 11–12 (de-
scribing humiliating experience of female student who was
strip searched while menstruating); Archuleta v. Wagner,
523 F. 3d 1278, 1282 (CA10 2008) (same for woman lac-
tating). They include victims of sexual violence. Brief
for Domestic Violence Legal Empowerment and Appeals
Project et al. as Amici Curiae. They include individuals
detained for such infractions as driving with a noisy muf-
fler, driving with an inoperable headlight, failing to use a
turn signal, or riding a bicycle without an audible bell.
Brief for Petitioner 11, 25; see also Mary Beth G., supra, at
1267, n. 2 (considering strip search of a person arrested for
having outstanding parking tickets and a person arrested
for making an improper left turn); Jones v. Edwards, 770
F. 2d 739, 741 (CA8 1985) (same for violation of dog leash
law). They include persons who perhaps should never
have been placed in the general jail population in the first
place. See ante, at 2 (ALITO, J. concurring) (“admission to
general jail population, with the concomitant humiliation
of a strip search, may not be reasonable” for those “whose
detention has not been reviewed by a judicial officer and
who could not be held in available facilities apart from the
6    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF 

                COUNTY OF BURLINGTON

                   BREYER, J., dissenting 


general population”).
  I need not go on. I doubt that we seriously disagree
about the nature of the strip search or about the serious
affront to human dignity and to individual privacy that it
presents. The basic question before us is whether such
a search is nonetheless justified when an individual ar-
rested for a minor offense is involuntarily placed in the
general jail or prison population.
                              III
    The majority, like the respondents, argues that strip
searches are needed (1) to detect injuries or diseases, such
as lice, that might spread in confinement, (2) to identify
gang tattoos, which might reflect a need for special hous-
ing to avoid violence, and (3) to detect contraband, includ-
ing drugs, guns, knives, and even pens or chewing gum,
which might prove harmful or dangerous in prison. In
evaluating this argument, I, like the majority, recognize:
that managing a jail or prison is an “inordinately difficult
undertaking,” Turner, 482 U. S., at 85; that prison regula-
tions that interfere with important constitutional interests
are generally valid as long as they are “reasonably related
to legitimate penological interests,” id., at 89; that finding
injuries and preventing the spread of disease, minimizing
the threat of gang violence, and detecting contraband are
“legitimate penological interests,” ibid.; and that we nor-
mally defer to the expertise of jail and prison administra-
tors in such matters, id., at 85.
    Nonetheless, the “particular” invasion of interests, Bell,
441 U. S., at 559, must be “ ‘reasonably related’ ” to the jus-
tifying “penological interest” and the need must not be
“ ‘exaggerated.’ ” Turner, supra, at 87. It is at this point
that I must part company with the majority. I have found
no convincing reason indicating that, in the absence of
reasonable suspicion, involuntary strip searches of those
arrested for minor offenses are necessary in order to fur-
                 Cite as: 566 U. S. ____ (2012)            7

                     BREYER, J., dissenting

ther the penal interests mentioned. And there are strong
reasons to believe they are not justified.
  The lack of justification is fairly obvious with respect to
the first two penological interests advanced. The searches
already employed at Essex and Burlington include: (a)
pat-frisking all inmates; (b) making inmates go through
metal detectors (including the Body Orifice Screening
System (BOSS) chair used at Essex County Correctional
Facility that identifies metal hidden within the body); (c)
making inmates shower and use particular delousing
agents or bathing supplies; and (d) searching inmates’
clothing. In addition, petitioner concedes that detainees
could be lawfully subject to being viewed in their under-
garments by jail officers or during showering (for security
purposes). Brief for Petitioner 9; Tr. of Oral Arg. 7–8
(“Showering in the presence of officers is not something
that requires reasonable suspicion”). No one here has
offered any reason, example, or empirical evidence sug-
gesting the inadequacy of such practices for detecting
injuries, diseases, or tattoos. In particular, there is no
connection between the genital lift and the “squat and
cough” that Florence was allegedly subjected to and health
or gang concerns. See Brief for Academics on Gang Be-
havior as Amici Curiae; Brief for Medical Society of New
Jersey et al. as Amici Curiae.
  The lack of justification for such a strip search is less
obvious but no less real in respect to the third interest,
namely that of detecting contraband. The information
demonstrating the lack of justification is of three kinds.
First, there are empirically based conclusions reached in
specific cases. The New York Federal District Court, to
which I have referred, conducted a study of 23,000 persons
admitted to the Orange County correctional facility be-
tween 1999 and 2003. Dodge, 282 F. Supp. 2d, at 69.
These 23,000 persons underwent a strip search of the kind
described, supra, at 1. Of these 23,000 persons, the court
8    FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF 

                COUNTY OF BURLINGTON

                   BREYER, J., dissenting 


wrote, “the County encountered three incidents of drugs
recovered from an inmate’s anal cavity and two incidents
of drugs falling from an inmate’s underwear during the
course of a strip search.” 282 F. Supp. 2d, at 69. The
court added that in four of these five instances there may
have been “reasonable suspicion” to search, leaving only
one instance in 23,000 in which the strip search policy
“arguably” detected additional contraband. Id., at 70. The
study is imperfect, for search standards changed during
the time it was conducted. Id., at 50–51. But the large
number of inmates, the small number of “incidents,” and
the District Court’s own conclusions make the study pro-
bative though not conclusive.
   Similarly, in Shain v. Ellison, 273 F. 3d 56, 60 (CA2
2001), the court received data produced by the county
jail showing that authorities conducted body-cavity strip
searches, similar to those at issue here, of 75,000 new
inmates over a period of five years. Brief for Plaintiff-
Appellee-Cross-Appellant in No. 00–7061 etc. (CA2), p. 16
(citing to its App. 343a–493a). In 16 instances the
searches led to the discovery of contraband. The record
further showed that 13 of these 16 pieces of contraband
would have been detected in a patdown or a search of shoes
and outer-clothing. In the three instances in which contra-
band was found on the detainee’s body or in a body cavity,
there was a drug or felony history that would have justi-
fied a strip search on individualized reasonable suspicion.
Ibid.; Brief for National Police Accountability Project as
Amicus Curiae 10.
   Second, there is the plethora of recommendations of
professional bodies, such as correctional associations, that
have studied and thoughtfully considered the matter. The
American Correctional Association (ACA)—an association
that informs our view of “what is obtainable and what is
acceptable in corrections philosophy,” Brown v. Plata, 563
U. S. ___, ___ (2011) (slip op., at 43)—has promulgated a
                  Cite as: 566 U. S. ____ (2012)             9

                     BREYER, J., dissenting

standard that forbids suspicionless strip searches. And
it has done so after consultation with the American Jail
Association, National Sheriff’s Association, National In-
stitute of Corrections of the Department of Justice, and
Federal Bureau of Prisons. ACA, Performance-Based
Standards for Adult Local Detention Facilities, Standard
4–ALDF–2C–03, p. 36 (4th ed. 2004); Dept. of Justice,
Federal Performance-Based Detention Standards Hand-
book, §C. 6, p. 99 (Feb. 23, 2011, rev.-2), http://www.
justice.gov/ofdt/fpbds02232011.pdf (all Internet materials
as visited Mar. 30, 2012, and available in Clerk of Court’s
case file); ACA, Core Jail Standards §1–CORE–2C–02,
pp. vii, 23 (2010). A standard desk reference for general
information about sound correctional practices advises
against suspicionless strip searches. Dept. of Justice,
National Institute of Corrections, M. Martin & T. Rosazza,
Resource Guide for Jail Administrators 4, 113 (2004); see
also Dept. of Justice, National Institute of Corrections, M.
Martin & P. Katsampes, Sheriff’s Guide to Effective Jail
Operations 50 (2007).
   Moreover, many correctional facilities apply a reason-
able suspicion standard before strip searching inmates
entering the general jail population, including the U. S.
Marshals Service, the Immigration and Customs Service,
and the Bureau of Indian Affairs. See U. S. Marshals
Serv., Policy Directive, Prisoner Custody-Body Searches
§9.1(E)(3) (2010), http://www.usmarshals.gov/foia / Directives-
Policy / prisoner_ops / body_searches.pdf; Immigration and
Customs Enforcement (ICE) Detention Standard: Searches
of Detainees 1 (2008), http://www.ice.gov/doclib/
dro/ detention-standards / pdf/searches_of_detainees.pdf;
ICE/DRO, Detention Standard: Admission and Release 4–5
(2008), http://www.ice.gov/doclib/dro/detention-standards/
pdf/environmental_health_and_safety.pdf; Bureau of Indian
Affairs, Office of Justice Servs., BIA Adult Detention
Facility Guidelines 22 (Draft 2010). The Federal Bureau
10   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON
                   BREYER, J., dissenting

of Prisons (BOP) itself forbids suspicionless strip searches
for minor offenders, though it houses separately (and does
not admit to the general jail population) a person who does
not consent to such a search. See Dept. of Justice, BOP
Program Statement 5140.38, p. 5. (2004), http://www.
bop.gov/policy/progstat/5140_038.pdf.
   Third, there is general experience in areas where the
law has forbidden here-relevant suspicionless searches.
Laws in at least 10 States prohibit suspicionless strip
searches. See, e.g., Mo. Stat. Ann. §544.193.2 (2002) (“No
person arrested or detained for a traffic offense or an
offense which does not constitute a felony may be subject
to a strip search or a body cavity search . . . unless there is
probable cause to believe that such person is concealing a
weapon . . . or contraband”); Kan. Stat. Ann. §22–2521(a)
(2007) (similar); Iowa Code §804.30 (2009) (similar); 725
Ill. Comp. Stat., ch. 725, §5/103–1(c) (2011) (similar but
requiring “reasonable belief ”); 501 Ky. Admin. Regs.
3:120, §3(1)(b) (2011) (similar); Tenn. Code Ann. §40–7–
119 (2006) (similar); Colo. Rev. Stat. Ann. §16–3–405(1)
(2011) (no strip search absent individualized suspicion
unless person has been arraigned and court orders that
suspect be detained); Fla. Stat. §901.211(2) (2010) (simi-
lar); Mich. Comp. Laws Ann. §764.25a(2) (2000) (similar);
Wash. Rev. Code §10.79.130(1) (2010) (similar).
   At the same time at least seven Courts of Appeals have
considered the question and have required reasonable
suspicion that an arrestee is concealing weapons or con-
traband before a strip search of one arrested for a minor
offense can take place. See, e.g., Roberts v. Rhode Island,
239 F. 3d 107, 112–113 (CA1 2001); Weber v. Dell, 804
F. 2d 796, 802 (CA2 1986); Logan v. Shealy, 660 F. 2d
1007, 1013 (CA4 1981); Stewart v. Lubbock Cty. Tex., 767
F. 2d 153, 156–157 (CA5 1985); Masters v. Crouch, 872
F. 2d 1248, 1255 (CA6 1989); Mary Beth G., 723 F. 2d, at
1266, 1273; Edwards, 770 F. 2d, at 742; Hill v. Bogans,
                 Cite as: 566 U. S. ____ (2012)           11

                     BREYER, J., dissenting

735 F. 2d 391, 394 (CA10 1984). But see 621 F. 3d, at 311
(case below); Bull v. City and County of San Francisco,
595 F. 3d 964, 975 (CA9 2010) (en banc); Powell v. Barrett,
541 F. 3d 1298, 1307 (CA11 2008) (en banc). Respondents
have not presented convincing grounds to believe that
administration of these legal standards has increased the
smuggling of contraband into prison.
   Indeed, neither the majority’s opinion nor the briefs set
forth any clear example of an instance in which contra-
band was smuggled into the general jail population during
intake that could not have been discovered if the jail was
employing a reasonable suspicion standard. The majority
does cite general examples from Atlantic County and
Washington State where contraband has been recovered
in correctional facilities from inmates arrested for driving
under the influence and disorderly conduct. Ante, at 15.
Similarly, the majority refers to information, provided by
San Francisco jail authorities, stating that they have
found handcuff keys, syringes, crack pipes, drugs, and
knives during body-cavity searches, including during
searches of minor offenders, including a man arrested for
illegally lodging (drugs), and a woman arrested for prosti-
tution and public nuisance (“bindles of crack cocaine”).
Brief for City and County of San Francisco et al. as Amici
Curiae 7–13; Bull, supra, at 969; ante, at 15. And associ-
ated statistics indicate that the policy of conducting visual
cavity searches of all those admitted to the general popu-
lation in San Francisco may account for the discovery of
contraband in approximately 15 instances per year. Bull,
supra, at 969.
   But neither San Francisco nor the respondents tell us
whether reasonable suspicion was present or absent in any
of the 15 instances. Nor is there any showing by the
majority that the few unclear examples of contraband
recovered in Atlantic County, Washington State, or any-
where else could not have been discovered through a policy
12   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON
                   BREYER, J., dissenting

that required reasonable suspicion for strip searches. And
without some such indication, I am left without an exam-
ple of any instance in which contraband was found on an
individual through an inspection of their private parts or
body cavities which could not have been found under a
policy requiring reasonable suspicion. Hence, at a mini-
mum these examples, including San Francisco’s statistics,
do not provide a significant counterweight to those pre-
sented in Dodge and Shain.
   Nor do I find the majority’s lack of examples surprising.
After all, those arrested for minor offenses are often
stopped and arrested unexpectedly. And they conse-
quently will have had little opportunity to hide things in
their body cavities. Thus, the widespread advocacy by
prison experts and the widespread application in many
States and federal circuits of “reasonable suspicion” re-
quirements indicates an ability to apply such standards in
practice without unduly interfering with the legitimate penal
interest in preventing the smuggling of contraband.
   The majority is left with the word of prison officials in
support of its contrary proposition. And though that word
is important, it cannot be sufficient. Cf. Dept. of Justice,
National Institute of Corrections, W. Collins, Jails and the
Constitution: An Overview 28–29 (2d ed. 2007) (Though
prison officials often “passionately believed” similar re-
quirements would lead to contraband-related security
problems, once those requirements were imposed those
“problems did not develop”).
   The majority also relies upon Bell, 441 U. S. 520, itself.
Ante, at 5–6. In that case, the Court considered a prison
policy requiring a strip search of all detainees after “con-
tact visits” with unimprisoned visitors. 441 U. S., at 558.
The Court found that policy justified. Id., at 560. Con-
trary to the majority’s suggestion, that case does not pro-
vide precedent for the proposition that the word of prison
officials (accompanied by a “single instance” of empirical
                 Cite as: 566 U. S. ____ (2012)           13

                     BREYER, J., dissenting

example) is sufficient to support a strip search policy.
Ante, at 6. The majority correctly points out that there
was but “one instance” in which the policy had led to the
discovery of an effort to smuggle contraband. Bell, 441
U. S., at 558. But the Court understood that the prison
had been open only four months. Id., at 526. And the
Court was also presented with other examples where
inmates attempted to smuggle contraband during contact
visits. Id., at 559.
   It is true that in Bell the Court found the prison jus-
tified in conducting postcontact searches even as to pre-
trial detainees who had been brought before a magistrate,
denied bail, and “committed to the detention facility only
because no other less drastic means [could] reasonably
assure [their] presence at trial.” 441 U. S., at 546, n. 28.
The Court recognized that those ordered detained by a
magistrate were often those “charged with serious crimes,
or who have prior records.” Ibid. For that reason, those
detainees posed at least the same security risk as con-
victed inmates, if not “a greater risk to jail security and
order,” and a “greater risk of escape.” Ibid. And, of
course, in Bell, both the inmates at issue and their visitors
had the time to plan to smuggle contraband in that case,
unlike those persons at issue here (imprisoned soon after
an unexpected arrest).
   The Bell Court had no occasion to focus upon those
arrested for minor crimes, prior to a judicial officer’s de-
termination that they should be committed to prison. I
share JUSTICE ALITO’s intuition that the calculus may be
different in such cases, given that “[m]ost of those arrested
for minor offenses are not dangerous, and most are re-
leased from custody prior to or at the time of their initial
appearance before a magistrate.” Ante, at 2 (concurring
opinion). As he notes, this case does not address, and
“reserves judgment on,” whether it is always reasonable
“to strip search an arrestee before the arrestee’s detention
14   FLORENCE v. BOARD OF CHOSEN FREEHOLDERS OF
                COUNTY OF BURLINGTON
                   BREYER, J., dissenting

has been reviewed by a judicial officer.” Ante, at 3. In my
view, it is highly questionable that officials would be
justified, for instance, in admitting to the dangerous world
of the general jail population and subjecting to a strip
search someone with no criminal background arrested for
jaywalking or another similarly minor crime, supra, at 5.
Indeed, that consideration likely underlies why the Fed-
eral Government and many States segregate such individ-
uals even when admitted to jail, and several jurisdictions
provide that such individuals be released without deten-
tion in the ordinary case. See, e.g., Cal. Penal Code Ann.
§853.6 (West Supp. 2012).
   In an appropriate case, therefore, it remains open for
the Court to consider whether it would be reasonable to
admit an arrestee for a minor offense to the general jail
population, and to subject her to the “humiliation of a strip
search,” prior to any review by a judicial officer. Ante, at 2
(ALITO, J., concurring).
                         *    *     *
  For the reasons set forth, I cannot find justification for
the strip search policy at issue here—a policy that would
subject those arrested for minor offenses to serious inva-
sions of their personal privacy. I consequently dissent.

```

---

## GROUP: content/cases/Florida v. Bostick.md  (`case`, 5 assertions)

### content_page

```
---
title: "Florida v. Bostick"
type: case
citation: "501 U.S. 429 (1991)"
parallel_cite: "111 S. Ct. 2382; 115 L. Ed. 2d 389; 59 U.S.L.W. 4708; 91 Daily Journal DAR 7328"
neutral_cite: "1991 U.S. LEXIS 3625; 91 Cal. Daily Op. Serv. 4671; 1991 WL 105224"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Bostick
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112631/florida-v-bostick/"
  cluster_id: 112631
  opinion_id: 112631
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Hodari D.]]", "[[United States v. Mendenhall]]", "[[Florida v. Royer]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "consensual-encounter", "bus-sweep"]
holding: "On a bus (where the passenger isn't free to leave regardless), the seizure question is whether a reasonable person would feel free to…"
lake:
  record_id: Florida v. Bostick
  status: verified
  projected_at: 2026-07-09
---

# Florida v. Bostick

*501 U.S. 429 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a drug-interdiction sweep, two officers boarded a bus during a stopover and, without articulable suspicion, approached Terrance Bostick, asked for his ticket and identification, explained they were narcotics officers, and asked to search his luggage. Bostick consented and the officers found cocaine. The Florida Supreme Court adopted a [[Common Legal Terms#per-se|per se]] rule that the police practice of "working the buses" was an unconstitutional seizure.

## Issue
How to determine whether a police-citizen encounter is a Fourth Amendment seizure when the person's freedom of movement is already restricted by a factor independent of police conduct (being a passenger on a bus about to depart), so that the usual "free to leave" test does not fit.

## Rule
When a person's movement is constrained by something other than the police, the seizure question is not whether he was free to leave but whether he was free to end the encounter: "the appropriate inquiry is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter." — 501 U.S. at 436. ^pin-436

That objective standard governs all such encounters: "in order to determine whether a particular encounter constitutes a seizure, a court must consider all the circumstances surrounding the encounter to determine whether the police conduct would have communicated to a reasonable person that the person was not free to decline the officers' requests or otherwise terminate the encounter." — [*Id.* at 439](https://www.courtlistener.com/opinion/112631/florida-v-bostick/#:~:text=in%20order%20to%20determine%20whether). ^pin-439

## Application
Because Bostick's freedom to leave was limited by his being a passenger on a bus about to depart — not by any show of police authority — the Florida court erred in treating the encounter as a [[Common Legal Terms#per-se|per se]] seizure. Whether he was seized turned on whether a reasonable person in his position would have felt free to decline the officers' requests; the Court [[Reading and Citing Cases#on-remand|remanded]] for that totality-of-the-circumstances assessment rather than resolving the seizure question categorically.

## Conclusion
The Florida Supreme Court's [[Common Legal Terms#per-se|per se]] rule was reversed; whether a bus-sweep encounter is a seizure is judged by the free-to-decline-or-terminate standard on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and the case was [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Bostick*'s free-to-decline-or-terminate formulation remains the governing test for distinguishing a consensual encounter from a seizure.

## Appears on
- [[Knock and Talk]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. Bostick*, 501 U.S. 429 (1991) — https://www.courtlistener.com/opinion/112631/florida-v-bostick/ — pinpoints: 436, 439.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ce565f4fe87d027c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "501 U.S. 429 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 3625; 91 Cal. Daily Op. Serv. 4671; 1991 WL 105224", "official_citation_present": true, "parallel_cite": "111 S. Ct. 2382; 115 L. Ed. 2d 389; 59 U.S.L.W. 4708; 91 Daily Journal DAR 7328", "title": "Florida v. Bostick", "year": "1991"}}
{"assertion_id": "cd4384e5d819b7c4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "On a bus (where the passenger isn't free to leave regardless), the seizure question is whether a reasonable person would feel free to…", "title": "Florida v. Bostick"}}
{"assertion_id": "ed71c4cc88ea846f", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key — Progeny / Refinement", "title": "Florida v. Bostick"}}
{"assertion_id": "fb0247acb3ad7e67", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Florida v. Bostick", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Florida v. Bostick", "varies_by_point": "false"}}
{"assertion_id": "fc2616ed38ebdd50", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Florida v. Bostick"}}
```

### lake record — Florida v. Bostick

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Bostick",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Bostick",
    "case_name_short": "Bostick",
    "case_name_full": "Florida v. Bostick",
    "input_case_name": "Florida v. Bostick",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-06-20",
    "year": 1991,
    "docket": null,
    "cluster_id": 112631,
    "lead_opinion_id": 112631,
    "sibling_ids": [
      112631,
      9842116,
      9842117
    ],
    "absolute_url": "/opinion/112631/florida-v-bostick/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9104125,
        "score": 20,
        "case_name": "Florida v. Bostick"
      },
      {
        "cluster_id": 9104124,
        "score": 20,
        "case_name": "Florida v. Bostick"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "501 U.S. 429",
      "volume": "501",
      "reporter": "U.S.",
      "page": "429",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 2382",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 389",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4708",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4708",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 7328",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "7328",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 3625",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3625",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 4671",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "4671",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 105224",
        "volume": "1991",
        "reporter": "WL",
        "page": "105224",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "501 U.S. 429",
        "volume": "501",
        "reporter": "U.S.",
        "page": "429",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 2382",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2382",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 389",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 3625",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3625",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 U.S.L.W. 4708",
        "volume": "59",
        "reporter": "U.S.L.W.",
        "page": "4708",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Daily Journal DAR 7328",
        "volume": "91",
        "reporter": "Daily Journal DAR",
        "page": "7328",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 Cal. Daily Op. Serv. 4671",
        "volume": "91",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "4671",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 WL 105224",
        "volume": "1991",
        "reporter": "WL",
        "page": "105224",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "501 U.S. 429",
    "official_selection": {
      "court_class": "scotus",
      "selected": "501 U.S. 429",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-436",
      "page": null,
      "quote": "test does not fit. ## Rule When a person's movement is constrained by something other than the police, the seizure question is not whether he was free to leave but whether he was free to end the encounter:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-439",
      "page": null,
      "quote": "in order to determine whether a particular encounter constitutes a seizure, a court must consider all the circumstances surrounding the encounter to determine whether the police conduct would have communicated to a reasonable person that the person was not free to decline the officers' requests or otherwise terminate the encounter.",
      "star_marker": "439",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24942,
      "fragment": "#:~:text=in%20order%20to%20determine%20whether",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Bostick",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Florida v. Bostick:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane1_negative"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muehler v. Mena",
          "cluster_id": 142878,
          "cite": [
            "161 L. Ed. 2d 299",
            "125 S. Ct. 1465",
            "544 U.S. 93",
            "2005 U.S. LEXIS 2755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
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
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "St. George v. State",
          "cluster_id": 1450469,
          "cite": [
            "237 S.W.3d 720",
            "2007 Tex. Crim. App. LEXIS 1476",
            "2007 WL 3171746"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mateen Yusuf Shabazz, A/K/A Edward L. Eberhart, A/K/A Edward Wallace, and Keith Lamar Parker",
          "cluster_id": 606689,
          "cite": [
            "993 F.2d 431",
            "1993 U.S. App. LEXIS 13132",
            "1993 WL 187994"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nenno v. State",
          "cluster_id": 1491957,
          "cite": [
            "970 S.W.2d 549",
            "1998 Tex. Crim. App. LEXIS 81",
            "1998 WL 331283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Bostick:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112631 OR 9842116 OR 9842117) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTc5NTY0ODAwMDAwJnM9NDcxMzkxNSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112631+OR+9842116+OR+9842117%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112631 OR 9842116 OR 9842117)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTAmcz02MDI4MjQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112631+OR+9842116+OR+9842117%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112631 OR 9842116 OR 9842117)",
        "reviewed": 90,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 90,
        "triage_read": 2,
        "triage_snippet_classified": 88
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112631 OR 9842116 OR 9842117)",
    "indexed_citing_opinions": 2663,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112631,
        "count": 2402,
        "count_source": "search"
      },
      {
        "opinion_id": 9842116,
        "count": 299,
        "count_source": "search"
      },
      {
        "opinion_id": 9842117,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4438,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-bostick.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjM0MSZzPTEwNTg5MjIzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112631+OR+9842116+OR+9842117%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112631,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 535568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 545303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 547221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 553310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 563232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1111734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1427842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1492587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1689153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1689253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1721587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1721782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1721924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1797492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1797787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1816927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1817273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1817337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1874170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1905980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 1915148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 2253144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 2596785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112631,
        "cited_id": 2618916,
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
    "date_created": "2026-07-05T03:45:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:46:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:46:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:48:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:46:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Bostick

```
<div>
<center><b><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429</a></span> (1991)</b></center>
<center><h1>FLORIDA<br>
v.<br>
BOSTICK.</h1></center>
<center>No. 89-1717.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued February 26, 1991.</center>
<center>Decided June 20, 1991.</center>
CERTIORARI TO THE SUPREME COURT OF FLORIDA.
<p><span class="star-pagination">*430</span> <i>Joan Fowler,</i> Assistant Attorney General of Florida, argued the cause for petitioner. With her on the brief was <i>Robert A. Butterworth,</i> Attorney General.</p>
<p><i>Solicitor General Starr</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Assistant Attorney General Mueller, Deputy Solicitor General Bryson, Christopher J. Wright,</i> and <i>Kathleen A. Felton.</i></p>
<p><i>Donald B. Ayer</i> argued the cause for respondent. With him on the brief was <i>Robert H. Klonoff.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*431</span> JUSTICE O'CONNOR delivered the opinion of the Court.</p>
<p>We have held that the Fourth Amendment permits police officers to approach individuals at random in airport lobbies and other public places to ask them questions and to request consent to search their luggage, so long as a reasonable person would understand that he or she could refuse to cooperate. This case requires us to determine whether the same rule applies to police encounters that take place on a bus.</p>
<p></p>
<h2>I</h2>
<p>Drug interdiction efforts have led to the use of police surveillance at airports, train stations, and bus depots. Law enforcement officers stationed at such locations routinely approach individuals, either randomly or because they suspect in some vague way that the individuals may be engaged in criminal activity, and ask them potentially incriminating questions. Broward County has adopted such a program. County Sheriff's Department officers routinely board buses at scheduled stops and ask passengers for permission to search their luggage.</p>
<p>In this case, two officers discovered cocaine when they searched a suitcase belonging to Terrance Bostick. The underlying facts of the search are in dispute, but the Florida Supreme Court, whose decision we review here, stated explicitly the factual premise for its decision:</p>
<blockquote>"`Two officers, complete with badges, insignia and one of them holding a recognizable zipper pouch, containing a pistol, boarded a bus bound from Miami to Atlanta during a stopover in Fort Lauderdale. Eyeing the passengers, the officers, admittedly without articulable suspicion, picked out the defendant passenger and asked to inspect his ticket and identification. The ticket, from Miami to Atlanta, matched the defendant's identification and both were immediately returned to him as unremarkable. However, the two police officers persisted and explained their presence as narcotics agents on the <span class="star-pagination">*432</span> lookout for illegal drugs. In pursuit of that aim, they then requested the defendant's consent to search his luggage. Needless to say, there is a conflict in the evidence about whether the defendant consented to the search of the second bag in which the contraband was found and as to whether he was informed of his right to refuse consent. However, any conflict must be resolved in favor of the state, it being a question of fact decided by the trial judge.'" <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d 1153, 1154-1155</a></span> (1989), quoting <span class="citation" data-id="1915148"><a href="/opinion/1915148/bostick-v-state/#322" aria-description="Citation for case: Bostick v. State">510 So. 2d 321, 322</a></span> (Fla. App. 1987) (Letts, J., dissenting in part).</blockquote>
<p>Two facts are particularly worth noting. First, the police specifically advised Bostick that he had the right to refuse consent. Bostick appears to have disputed the point, but, as the Florida Supreme Court noted explicitly, the trial court resolved this evidentiary conflict in the State's favor. Second, at no time did the officers threaten Bostick with a gun. The Florida Supreme Court indicated that one officer carried a zipper pouch containing a pistol  the equivalent of carrying a gun in a holster  but the court did not suggest that the gun was ever removed from its pouch, pointed at Bostick, or otherwise used in a threatening manner. The dissent's characterization of the officers as "gun-wielding inquisitor[s]," <i>post,</i> at 448, is colorful, but lacks any basis in fact.</p>
<p>Bostick was arrested and charged with trafficking in cocaine. He moved to suppress the cocaine on the grounds that it had been seized in violation of his Fourth Amendment rights. The trial court denied the motion but made no factual findings. Bostick subsequently entered a plea of guilty, but reserved the right to appeal the denial of the motion to suppress.</p>
<p>The Florida District Court of Appeal affirmed, but considered the issue sufficiently important that it certified a question to the Florida Supreme Court. <span class="citation" data-id="1915148"><a href="/opinion/1915148/bostick-v-state/#322" aria-description="Citation for case: Bostick v. State">510 So. 2d, at 322</a></span>. The <span class="star-pagination">*433</span> Supreme Court reasoned that Bostick had been seized because a reasonable passenger in his situation would not have felt free to leave the bus to avoid questioning by the police. <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1154</a></span>. It rephrased and answered the certified question so as to make the bus setting dispositive in every case. It ruled categorically that "`an impermissible seizure result[s] when police mount a drug search on buses during scheduled stops and question boarded passengers without articulable reasons for doing so, thereby obtaining consent to search the passengers' luggage.'" <i><span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/" aria-description="Citation for case: Bostick v. State">Ibid.</a></span></i> The Florida Supreme Court thus adopted a <i>per se</i> rule that the Broward County Sheriff's practice of "working the buses" is unconstitutional.<sup>[*]</sup> The result of this decision is that police in Florida, as elsewhere, may approach persons at random in most public places, ask them questions and seek consent to a search, see <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1156" aria-description="Citation for case: Bostick v. State"><i>id.,</i> at 1156</a></span>; but they may not engage in the same behavior on a bus. <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1157" aria-description="Citation for case: Bostick v. State"><i>Id.,</i> at 1157</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./498/894/">498 U. S. 894</a></span> (1990), to determine whether the Florida Supreme Court's <i>per se</i> rule is consistent with our Fourth Amendment jurisprudence.</p>
<p></p>
<h2>II</h2>
<p>The sole issue presented for our review is whether a police encounter on a bus of the type described above necessarily constitutes a "seizure" within the meaning of the Fourth Amendment. The State concedes, and we accept for purposes of this decision, that the officers lacked the reasonable <span class="star-pagination">*434</span> suspicion required to justify a seizure and that, if a seizure took place, the drugs found in Bostick's suitcase must be suppressed as tainted fruit.</p>
<p>Our cases make it clear that a seizure does not occur simply because a police officer approaches an individual and asks a few questions. So long as a reasonable person would feel free "to disregard the police and go about his business," <i>California</i> v. <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#628" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 628</a></span> (1991), the encounter is consensual and no reasonable suspicion is required. The encounter will not trigger Fourth Amendment scrutiny unless it loses its consensual nature. The Court made precisely this point in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19, n. 16</a></span> (1968): "Obviously, not all personal intercourse between policemen and citizens involves `seizures' of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a `seizure' has occurred."</p>
<p>Since <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> we have held repeatedly that mere police questioning does not constitute a seizure. In <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983) (plurality opinion), for example, we explained that "law enforcement officers do not violate the Fourth Amendment by merely approaching an individual on the street or in another public place, by asking him if he is willing to answer some questions, by putting questions to him if the person is willing to listen, or by offering in evidence in a criminal prosecution his voluntary answers to such questions." <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer"><i>Id.,</i> at 497</a></span>; see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#523" aria-description="Citation for case: Florida v. Royer"><i>id.,</i> at 523, n. 3</a></span> (REHNQUIST, J., dissenting).</p>
<p>There is no doubt that if this same encounter had taken place before Bostick boarded the bus or in the lobby of the bus terminal, it would not rise to the level of a seizure. The Court has dealt with similar encounters in airports and has found them to be "the sort of consensual encounter[s] that implicat[e] no Fourth Amendment interest." <i>Florida</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 5-6</a></span> (1984). We have stated that even <span class="star-pagination">*435</span> when officers have no basis for suspecting a particular individual, they may generally ask questions of that individual, see <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 216</a></span> (1984); <span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#5" aria-description="Citation for case: Florida v. Rodriguez"><i>Rodriguez, supra,</i> at 5-6</a></span>; ask to examine the individual's identification, see <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216</a></span>; <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer"><i>Royer, supra,</i> at 501</a></span> (plurality opinion); <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#557" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 557-558</a></span> (1980); and request consent to search his or her luggage, see <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer"><i>Royer, supra,</i> at 501</a></span> (plurality opinion)  as long as the police do not convey a message that compliance with their requests is required.</p>
<p>Bostick insists that this case is different because it took place in the cramped confines of a bus. A police encounter is much more intimidating in this setting, he argues, because police tower over a seated passenger and there is little room to move around. Bostick claims to find support in language from <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#573" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 573</a></span> (1988), and other cases, indicating that a seizure occurs when a reasonable person would believe that he or she is not "free to leave." Bostick maintains that a reasonable bus passenger would not have felt free to leave under the circumstances of this case because there is nowhere to go on a bus. Also, the bus was about to depart. Had Bostick disembarked, he would have risked being stranded and losing whatever baggage he had locked away in the luggage compartment.</p>
<p>The Florida Supreme Court found this argument persuasive, so much so that it adopted a <i>per se</i> rule prohibiting the police from randomly boarding buses as a means of drug interdiction. The state court erred, however, in focusing on whether Bostick was "free to leave" rather than on the principle that those words were intended to capture. When police attempt to question a person who is walking down the street or through an airport lobby, it makes sense to inquire whether a reasonable person would feel free to continue walking. But when the person is seated on a bus and has no desire to leave, the degree to which a reasonable person <span class="star-pagination">*436</span> would feel that he or she could leave is not an accurate measure of the coercive effect of the encounter.</p>
<p>Here, for example, the mere fact that Bostick did not feel free to leave the bus does not mean that the police seized him. Bostick was a passenger on a bus that was scheduled to depart. He would not have felt free to leave the bus even if the police had not been present. Bostick's movements were "confined" in a sense, but this was the natural result of his decision to take the bus; it says nothing about whether or not the police conduct at issue was coercive.</p>
<p>In this respect, the Court's decision in <i>INS</i> v. <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado, supra</a></span></i><i>,</i> is dispositive. At issue there was the INS' practice of visiting factories at random and questioning employees to determine whether any were illegal aliens. Several INS agents would stand near the building's exits, while other agents walked through the factory questioning workers. The Court acknowledged that the workers may not have been free to leave their worksite, but explained that this was not the result of police activity: "Ordinarily, when people are at work their freedom to move about has been meaningfully restricted, not by the actions of law enforcement officials, but by the workers' voluntary obligations to their employers." <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Id.,</i> at 218</a></span>. We concluded that there was no seizure because, even though the workers were not free to leave the building without being questioned, the agents' conduct should have given employees "no reason to believe that they would be detained if they gave truthful answers to the questions put to them or if they simply refused to answer." <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Ibid.</a></span></i></p>
<p>The present case is analytically indistinguishable from <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>.</i> Like the workers in that case, Bostick's freedom of movement was restricted by a factor independent of police conduct  <i>i. e.,</i> by his being a passenger on a bus. Accordingly, the "free to leave" analysis on which Bostick relies is inapplicable. In such a situation, the appropriate inquiry is whether a reasonable person would feel free to decline the officers' requests or otherwise terminate the encounter. This <span class="star-pagination">*437</span> formulation follows logically from prior cases and breaks no new ground. We have said before that the crucial test is whether, taking into account all of the circumstances surrounding the encounter, the police conduct would "have communicated to a reasonable person that he was not at liberty to ignore the police presence and go about his business." <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#569" aria-description="Citation for case: Michigan v. Chesternut"><i>Chesternut, supra,</i> at 569</a></span>. See also <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#628" aria-description="Citation for case: California v. Hodari D.">499 U. S., at 628</a></span>. Where the encounter takes place is one factor, but it is not the only one. And, as the Solicitor General correctly observes, an individual may decline an officer's request without fearing prosecution. See Brief for United States as <i>Amicus Curiae</i> 25. We have consistently held that a refusal to cooperate, without more, does not furnish the minimal level of objective justification needed for a detention or seizure. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216-217</a></span>; <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S., at 498</a></span> (plurality opinion); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52-53</a></span> (1979).</p>
<p>The facts of this case, as described by the Florida Supreme Court, leave some doubt whether a seizure occurred. Two officers walked up to Bostick on the bus, asked him a few questions, and asked if they could search his bags. As we have explained, no seizure occurs when police ask questions of an individual, ask to examine the individual's identification, and request consent to search his or her luggage  so long as the officers do not convey a message that compliance with their requests is required. Here, the facts recited by the Florida Supreme Court indicate that the officers did not point gnns at Bostick or otherwise threaten him and that they specifically advised Bostick that he could refuse consent.</p>
<p>Nevertheless, we refrain from deciding whether or not a seizure occurred in this case. The trial court made no express findings of fact, and the Florida Supreme Court rested its decision on a single fact  that the encounter took place on a bus  rather than on the totality of the circumstances. We remand so that the Florida courts may evaluate the seizure question under the correct legal standard. We do reject, however, Bostick's argument that he must have been seized <span class="star-pagination">*438</span> because no reasonable person would freely consent to a search of luggage that he or she knows contains drugs. This argument cannot prevail because the "reasonable person" test presupposes an <i>innocent</i> person. See <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#519" aria-description="Citation for case: Florida v. Royer"><i>Royer, supra,</i> at 519, n. 4</a></span> (BLACKMUN, J., dissenting) ("The fact that [respondent] knew the search was likely to turn up contraband is of course irrelevant; the potential intrusiveness of the officers' conduct must be judged from the viewpoint of an innocent person in [his] position"). Accord, <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 574</a></span> ("This `reasonable person' standard ... ensures that the scope of Fourth Amendment protection does not vary with the state of mind of the particular individual being approached").</p>
<p>The dissent characterizes our decision as holding that police may board buses and by an "<i>intimidating</i> show of authority," <i>post,</i> at 447 (emphasis added), demand of passengers their "voluntary" cooperation. That characterization is incorrect. Clearly, a bus passenger's decision to cooperate with law enforcement officers authorizes the police to conduct a search without first obtaining a warrant <i>only</i> if the cooperation is voluntary. "Consent" that is the product of official intimidation or harassment is not consent at all. Citizens do not forfeit their constitutional rights when they are coerced to comply with a request that they would prefer to refuse. The question to be decided by the Florida courts on remand is whether Bostick chose to permit the search of his luggage.</p>
<p>The dissent also attempts to characterize our decision as applying a lesser degree of constitutional protection to those individuals who travel by bus, rather than by other forms of transportation. This, too, is an erroneous characterization. Our Fourth Amendment inquiry in this case  whether a reasonable person would have felt free to decline the officers' requests or otherwise terminate the encounter  applies equally to police encounters that take place on trains, planes, and city streets. It is the dissent that would single out this particular <span class="star-pagination">*439</span> mode of travel for differential treatment by adopting a <i>per se</i> rule that random bus searches are unconstitutional.</p>
<p>The dissent reserves its strongest criticism for the proposition that police officers can approach individuals as to whom they have no reasonable suspicion and ask them potentially incriminating questions. But this proposition is by no means novel; it has been endorsed by the Court any number of times. <i>Terry, Royer, Rodriguez,</i> and <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> are just a few examples. As we have explained, today's decision follows logically from those decisions and breaks no new ground. Unless the dissent advocates overruling a long, unbroken line of decisions dating back more than 20 years, its criticism is not well taken.</p>
<p>This Court, as the dissent correctly observes, is not empowered to suspend constitutional guarantees so that the Government may more effectively wage a "war on drugs." See <i>post,</i> at 440, 450-451. If that war is to be fought, those who fight it must respect the rights of individuals, whether or not those individuals are suspected of having committed a crime. By the same token, this Court is not empowered to forbid law enforcement practices simply because it considers them distasteful. The Fourth Amendment proscribes unreasonable searches and seizures; it does not proscribe voluntary cooperation. The cramped confines of a bus are one relevant factor that should be considered in evaluating whether a passenger's consent is voluntary. We cannot agree, however, with the Florida Supreme Court that this single factor will be dispositive in every case.</p>
<p>We adhere to the rule that, in order to determine whether a particular encounter constitutes a seizure, a court must consider all the circumstances surrounding the encounter to determine whether the police conduct would have communicated to a reasonable person that the person was not free to decline the officers' requests or otherwise terminate the encounter. That rule applies to encounters that take place on a city street or in an airport lobby, and it applies equally to <span class="star-pagination">*440</span> encounters on a bus. The Florida Supreme Court erred in adopting a <i>per se</i> rule.</p>
<p>The judgment of the Florida Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE MARSHALL, with whom JUSTICE BLACKMUN and JUSTICE STEVENS join, dissenting.</p>
<p>Our Nation, we are told, is engaged in a "war on drugs." No one disputes that it is the job of law-enforcement officials to devise effective weapons for fighting this war. But the effectiveness of a law-enforcement technique is not proof of its constitutionality. The general warrant, for example, was certainly an effective means of law enforcement. Yet it was one of the primary aims of the Fourth Amendment to protect citizens from the tyranny of being singled out for search and seizure without particularized suspicion <i>notwithstanding</i> the effectiveness of this method. See <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625-630</a></span> (1886); see also <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#171" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 171</a></span> (1947) (Frankfurter, J., dissenting). In my view, the law-enforcement technique with which we are confronted in this case  the suspicionless police sweep of buses in intrastate or interstate travel  bears all of the indicia of coercion and unjustified intrusion associated with the general warrant. Because I believe that the bus sweep at issue in this case violates the core values of the Fourth Amendment, I dissent.</p>
<p></p>
<h2>I</h2>
<p>At issue in this case is a "new and increasingly common tactic in the war on drugs": the suspicionless police sweep of buses in interstate or intrastate travel. <i>United States</i> v. <i>Lewis,</i> 287 U. S. App. D. C. 306, 307, <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/#1295" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of...">921 F. 2d 1294, 1295</a></span> (1990); see <i>United States</i> v. <i>Flowers,</i> <span class="citation" data-id="547221"><a href="/opinion/547221/united-states-v-ervin-herman-flowers/#710" aria-description="Citation for case: United States v. Ervin Herman Flowers">912 F. 2d 707, 710</a></span> (CA4 1990) (describing technique in Charlotte, North Carolina); <i>United States</i> v. <i>Madison,</i> <span class="citation" data-id="563232"><a href="/opinion/563232/united-states-v-marc-a-madison-aka-stanley-johnson/#91" aria-description="Citation for case: United States v. Marc A. Madison, A/K/A &quot;Stanley Johnson&quot;">936 F. 2d 90, 91</a></span> (CA2 1991) (describing <span class="star-pagination">*441</span> technique in Port Authority terminal in New York City); <i>United States</i> v. <i>Chandler,</i> <span class="citation" data-id="1797787"><a href="/opinion/1797787/united-states-v-chandler/#335" aria-description="Citation for case: United States v. Chandler">744 F. Supp. 333, 335</a></span> (DC 1990) ("[I]t has become routine to subject interstate travelers to warrantless searches and intimidating interviews while sitting aboard a bus stopped for a short layover in the Capital"); <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1156" aria-description="Citation for case: Bostick v. State">554 So. 2d 1153, 1156-1157</a></span> (Fla. 1989) (describing Florida police policy of "`working the buses'"); see also <i>ante,</i> at 431. Typically under this technique, a group of state or federal officers will board a bus while it is stopped at an intermediate point on its route. Often displaying badges, weapons or other indicia of authority, the officers identify themselves and announce their purpose to intercept drug traffickers. They proceed to approach individual passengers, requesting them to show identification, produce their tickets, and explain the purpose of their travels. Never do the officers advise the passengers that they are free not to speak with the officers. An "interview" of this type ordinarily culminates in a request for consent to search the passenger's luggage. See generally <i>United States</i> v. <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/#308" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of..."><i>Lewis, supra,</i> at 308</a></span>, <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/#1296" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of...">921 F. 2d, at 1296</a></span>; <i>United States</i> v. <span class="citation" data-id="547221"><a href="/opinion/547221/united-states-v-ervin-herman-flowers/#708" aria-description="Citation for case: United States v. Ervin Herman Flowers"><i>Flowers, supra,</i> at 708-709</a></span>; <i>United States</i> v. <span class="citation" data-id="563232"><a href="/opinion/563232/united-states-v-marc-a-madison-aka-stanley-johnson/#91" aria-description="Citation for case: United States v. Marc A. Madison, A/K/A &quot;Stanley Johnson&quot;"><i>Madison, supra,</i> at 91</a></span>; <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1154</a></span>.</p>
<p>These sweeps are conducted in "dragnet" style. The police admittedly act without an "articulable suspicion" in deciding which buses to board and which passengers to approach for interviewing.<sup>[1]</sup> By proceeding systematically in this <span class="star-pagination">*442</span> fashion, the police are able to engage in a tremendously high volume of searches. See, <i>e. g., </i><i>Florida</i> v. <i>Kerwick,</i> <span class="citation" data-id="1111734"><a href="/opinion/1111734/state-v-kerwick/#348" aria-description="Citation for case: State v. Kerwick">512 So. 2d 347, 348-349</a></span> (Fla. App. 1987) (single officer employing sweep technique able to search over 3,000 bags in nine-month period). The percentage of successful drug interdictions is low. See <i>United States</i> v. <span class="citation" data-id="547221"><a href="/opinion/547221/united-states-v-ervin-herman-flowers/#710" aria-description="Citation for case: United States v. Ervin Herman Flowers"><i>Flowers, supra,</i> at 710</a></span> (sweep of 100 buses resulted in seven arrests).</p>
<p>To put it mildly, these sweeps "are inconvenient, intrusive, and intimidating." <i>United States</i> v. <i>Chandler,</i> <span class="citation" data-id="1797787"><a href="/opinion/1797787/united-states-v-chandler/#335" aria-description="Citation for case: United States v. Chandler">744 F. Supp., at 335</a></span>. They occur within cramped confines, with officers typically placing themselves in between the passenger selected for an interview and the exit of the bus. See, <span class="citation" data-id="1797787"><a href="/opinion/1797787/united-states-v-chandler/#336" aria-description="Citation for case: United States v. Chandler"><i>e. g., id.,</i> at 336</a></span>. Because the bus is only temporarily stationed at a point short of its destination, the passengers are in no position to leave as a means of evading the officers' questioning. Undoubtedly, such a sweep holds up the progress of the bus. See <i>United States</i> v. <i>Fields,</i> <span class="citation" data-id="545303"><a href="/opinion/545303/united-states-v-alaine-decarlo-fields/" aria-description="Citation for case: United States v. Alaine Decarlo Fields">909 F. 2d 470</a></span>, 474 n. 2 (CA11 1990); cf. <i>United States</i> v. <i>Rembert,</i> <span class="citation" data-id="1874170"><a href="/opinion/1874170/united-states-v-rembert/#175" aria-description="Citation for case: United States v. Rembert">694 F. Supp. 163, 175</a></span> (WDNC 1988) (reporting testimony of officer that he makes "`every effort in the world not to delay the bus'" but that the driver does not leave terminal until sweep is complete). Thus, this "new and increasingly common tactic," <i>United States</i> v. <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/#307" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of..."><i>Lewis, supra,</i> at 307</a></span>, <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/#1295" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of...">921 F. 2d, at 1295</a></span>, burdens the experience of traveling by bus with a degree of governmental interference to which, until now, our society has been proudly unaccustomed. See, <i>e. g., </i><i>State ex rel. Ekstrom</i> v. <i>Justice Court,</i> <span class="citation" data-id="9794637"><a href="/opinion/2618916/state-ex-rel-ekstrom-v-justice-ct-of-state/#6" aria-description="Citation for case: State Ex Rel. Ekstrom v. Justice Ct. of State">136 Ariz. 1, 6</a></span>, <span class="citation" data-id="9794637"><a href="/opinion/2618916/state-ex-rel-ekstrom-v-justice-ct-of-state/#997" aria-description="Citation for case: State Ex Rel. Ekstrom v. Justice Ct. of State">663 P. 2d 992, 997</a></span> (1983) (Feldman, J., concurring) ("The thought that an American can be compelled to `show his papers' before exercising his right to walk the streets, drive the highways or board the trains is repugnant to American institutions and ideals").</p>
<p><span class="star-pagination">*443</span> This aspect of the suspicionless sweep has not been lost on many of the lower courts called upon to review the constitutionality of this practice. Remarkably, the courts located at the heart of the "drug war" have been the most adamant in condemning this technique. As one Florida court put it:</p>
<blockquote>"`[T]he evidence in this cause has evoked images of other days, under other flags, when no man traveled his nation's roads or railways without fear of unwarranted interruption, by individuals who held temporary power in the Government. The spectre of American citizens being asked, by badge-wielding police, for identification, travel papers  in short a <i>raison d'etre</i>  is foreign to <i>any</i> fair reading of the Constitution, and its guarantee of human liberties. This is not Hitler's Berlin, nor Stalin's Moscow, nor is it white supremacist South Africa. Yet in Broward County, Florida, these police officers approach every person on board buses and trains ("that time permits") and check identification [and] tickets, [and] ask to search luggage  all in the name of "voluntary cooperation" with law enforcement ....'" <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1158" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1158</a></span>, quoting <i>State</i> v. <i><span class="citation" data-id="1111734"><a href="/opinion/1111734/state-v-kerwick/" aria-description="Citation for case: State v. Kerwick">Kerwick, supra,</a></span></i> at 348-349 (quoting trial court order).</blockquote>
<p>The District Court for the District of Columbia spoke in equally pointed words:</p>
<blockquote>"It seems rather incongruous at this point in the world's history that we find totalitarian states becoming more like our free society while we in this nation are taking on their former trappings of suppressed liberties and freedoms."</blockquote>
<blockquote>. . . . .</blockquote>
<blockquote>"The random indiscriminate stopping and questioning of individuals on interstate busses seems to have gone too far. If this Court approves such `bus stops' and allows prosecutions to be based on evidence seized as a result of such `stops,' then we will have stripped our <span class="star-pagination">*444</span> citizens of basic Constitutional protections. Such action would be inconsistent with what this nation has stood for during its 200 years of existence. If passengers on a bus passing through the Capital of this great nation cannot be free from police interference where there is absolutely no basis for the police officers to stop and question them, then the police will be free to accost people on our streets without any reason or cause. In this `anything goes' war on drugs, random knocks on the doors of our citizens' homes seeking `consent' to search for drugs cannot be far away. This is not America." <i>United States</i> v. <i>Lewis,</i> <span class="citation" data-id="2596785"><a href="/opinion/2596785/united-states-v-lewis/#788" aria-description="Citation for case: United States v. Lewis">728 F. Supp. 784, 788-789</a></span>, rev'd, 287 U. S. App. D. C. 306, <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of...">921 F. 2d 1294</a></span> (1990).</blockquote>
<p>See also <i>United States</i> v. <i>Alexander,</i> <span class="citation" data-id="1427842"><a href="/opinion/1427842/united-states-v-alexander/#453" aria-description="Citation for case: United States v. Alexander">755 F. Supp. 448, 453</a></span> (DC 1991); <i>United States</i> v. <i>Madison,</i> <span class="citation" data-id="1797492"><a href="/opinion/1797492/united-states-v-madison/#495" aria-description="Citation for case: United States v. Madison">744 F. Supp. 490, 495-497</a></span> (SDNY 1990), rev'd, <span class="citation" data-id="563232"><a href="/opinion/563232/united-states-v-marc-a-madison-aka-stanley-johnson/" aria-description="Citation for case: United States v. Marc A. Madison, A/K/A &quot;Stanley Johnson&quot;">936 F. 2d 90</a></span> (CA2 1991); <i>United States</i> v. <i><span class="citation" data-id="1797787"><a href="/opinion/1797787/united-states-v-chandler/" aria-description="Citation for case: United States v. Chandler">Chandler, supra,</a></span></i> at, 335-336; <i>United States</i> v. <i>Mark,</i> <span class="citation" data-id="1689253"><a href="/opinion/1689253/united-states-v-mark/#18" aria-description="Citation for case: United States v. Mark">742 F. Supp. 17, 18-19</a></span> (DC 1990); <i>United States</i> v. <i>Alston,</i> <span class="citation" data-id="1689153"><a href="/opinion/1689153/united-states-v-alston/#15" aria-description="Citation for case: United States v. Alston">742 F. Supp. 13, 15</a></span> (DC 1990); <i>United States</i> v. <i>Cothran,</i> <span class="citation" data-id="1492587"><a href="/opinion/1492587/united-states-v-cothran/#156" aria-description="Citation for case: United States v. Cothran">729 F. Supp. 153, 156-158</a></span> (DC 1990), rev'd, 287 U. S. App. D. C. 306, <span class="citation" data-id="553310"><a href="/opinion/553310/united-states-v-dennis-s-lewis-united-states-of-america-v-leigha-t/" aria-description="Citation for case: United States v. Dennis S. Lewis. United States of...">921 F. 2d 1294</a></span> (1990); <i>United States</i> v. <i>Felder,</i> <span class="citation" data-id="2253144"><a href="/opinion/2253144/united-states-v-felder/#209" aria-description="Citation for case: United States v. Felder">732 F. Supp. 204, 209</a></span> (DC 1990).</p>
<p>The question for this Court, then, is whether the suspicionless, dragnet-style sweep of buses in intrastate and interstate travel is consistent with the Fourth Amendment. The majority suggests that this latest tactic in the drug war is perfectly compatible with the Constitution. I disagree.</p>
<p></p>
<h2>II</h2>
<p>I have no objection to the manner in which the majority frames the test for determining whether a suspicionless bus sweep amounts to a Fourth Amendment "seizure." I agree that the appropriate question is whether a passenger who is approached during such a sweep "would feel free to decline the officers' requests or otherwise terminate the encounter." <span class="star-pagination">*445</span> <i>Ante,</i> at 436. What I cannot understand is how the majority can possibly suggest an affirmative answer to this question.</p>
<p>The majority reverses what it characterizes as the Florida Supreme Court's "<i>per se</i> rule" against suspicionless encounters between the police and bus passengers, see <i>ante,</i> at 433, 435-440, suggesting only in dictum its "doubt" that a seizure occurred on the facts of this case, see <i>ante,</i> at 437. However, the notion that the Florida Supreme Court decided this case on the basis of any "<i>per se</i> rule" <i>independent</i> of the facts of this case is wholly a product of the majority's imagination. As the majority acknowledges, the Florida Supreme Court "stated explicitly the factual premise for its decision." <i>Ante,</i> at 431. This factual premise contained <i>all</i> of the details of the encounter between respondent and the police. See <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1154</a></span>; <i>ante,</i> at 431-432. The lower court's analysis of whether respondent was seized drew heavily on these facts, and the court repeatedly emphasized that its conclusion was based on "<i>all the circumstances</i>" of this case. <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1157" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1157</a></span> (emphasis added); see <i><span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/" aria-description="Citation for case: Bostick v. State">ibid.</a></span></i> ("<i>Here, the circumstances indicate</i> that the officers effectively `seized' [respondent]" (emphasis added)).</p>
<p>The majority's conclusion that the Florida Supreme Court, contrary to all appearances, <i>ignored</i> these facts is based solely on the failure of the lower court to expressly incorporate all of the facts into its reformulation of the certified question on which respondent took his appeal. See <i>ante,</i> at 433.<sup>[2]</sup> The majority never explains the basis of its implausible assumption that the Florida Supreme Court intended its phrasing of the certified question to trump its opinion's careful treatment of the facts in this case. Certainly, when <i>this</i> Court issues an opinion, it does not intend lower courts and <span class="star-pagination">*446</span> parties to treat as irrelevant the analysis of facts that the parties neglected to cram into the question presented in the petition for certiorari. But in any case, because the issue whether a seizure has occurred in any given factual setting is a question of law, see <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554-555</a></span> (1980) (opinion of Stewart, J.); <i>United States</i> v. <i>Maragh,</i> 282 U. S. App. D. C. 256, 258-259, <span class="citation" data-id="9479910"><a href="/opinion/535568/united-states-v-mark-a-maragh/#417" aria-description="Citation for case: United States v. Mark A. Maragh">894 F. 2d 415, 417-418</a></span> (CADC), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./498/880/">498 U. S. 880</a></span> (1990), nothing prevents this Court from deciding on its own whether a seizure occurred based on <i>all</i> of the facts of this case as they appear in the opinion of the Florida Supreme Court.</p>
<p>These facts exhibit all of the elements of coercion associated with a typical bus sweep. Two officers boarded the Greyhound bus on which respondent was a passenger while the bus, en route from Miami to Atlanta, was on a brief stop to pick up passengers in Fort Lauderdale. The officers made a visible display of their badges and wore bright green "raid" jackets bearing the insignia of the Broward County Sheriff's Department; one held a gun in a recognizable weapons pouch. See <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1154, 1157</a></span>. These facts alone constitute an intimidating "show of authority." See <i>Michigan</i> v. <i>Chesternut,</i> <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#575" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 575</a></span> (1988) (display of weapon contributes to coercive environment); <i>United States</i> v. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 554</a></span> (opinion of Stewart, J.) ("threatening presence of several officers" and "display of a weapon"); <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#555" aria-description="Citation for case: United States v. Mendenhall"><i>id.,</i> at 555</a></span> (uniformed attire). Once on board, the officers approached respondent, who was sitting in the back of the bus, identified themselves as narcotics officers and began to question him. See <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1154" aria-description="Citation for case: Bostick v. State">554 So. 2d, at 1154</a></span>. One officer stood in front of respondent's seat, partially blocking the narrow aisle through which respondent would have been required to pass to reach the exit of the bus. See <span class="citation" data-id="1721782"><a href="/opinion/1721782/bostick-v-state/#1157" aria-description="Citation for case: Bostick v. State"><i>id.,</i> at 1157</a></span>.</p>
<p>As far as is revealed by facts on which the Florida Supreme Court premised its decision, the officers did not advise respondent that he was free to break off this "interview." Inexplicably, the majority repeatedly stresses the trial court's <span class="star-pagination">*447</span> implicit finding that the police officers advised respondent that he was free to refuse permission to search his travel bag. See <i>ante,</i> at 432, 437-438. This aspect of the exchange between respondent and the police is completely irrelevant to the issue before us. For as the State concedes, and as the majority purports to "accept," <i>id.,</i> at 433-434, <i>if</i> respondent was unlawfully seized when the officers approached him and initiated questioning, the resulting search was likewise unlawful no matter how well advised respondent was of his right to refuse it. See <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 501, 507-508</a></span> (1983) (plurality opinion); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). Consequently, the issue is not whether a passenger in respondent's position would have felt free to deny consent to the search of his bag, but whether such a passenger  without being apprised of his rights  would have felt free to terminate the antecedent encounter with the police.</p>
<p>Unlike the majority, I have no doubt that the answer to this question is no. Apart from trying to accommodate the officers, respondent had only two options. First, he could have remained seated while obstinately refusing to respond to the officers' questioning. But in light of the intimidating show of authority that the officers made upon boarding the bus, respondent reasonably could have believed that such behavior would only arouse the officers' suspicions and intensify their interrogation. Indeed, officers who carry out bus sweeps like the one at issue here frequently admit that this is the effect of a passenger's refusal to cooperate. See, <i>e. g., </i><i>United States</i> v. <i>Cothran,</i> <span class="citation" data-id="1492587"><a href="/opinion/1492587/united-states-v-cothran/#156" aria-description="Citation for case: United States v. Cothran">729 F. Supp., at 156</a></span>; <i>United States</i> v. <i>Felder,</i> <span class="citation" data-id="2253144"><a href="/opinion/2253144/united-states-v-felder/#205" aria-description="Citation for case: United States v. Felder">732 F. Supp., at 205</a></span>. The majority's observation that a mere refusal to answer questions, "without more," does not give rise to a reasonable basis for seizing a passenger, <i>ante,</i> at 437, is utterly beside the point, because a passenger unadvised of his rights and otherwise unversed in constitutional law <i>has no reason to know</i> that the police cannot hold his refusal to cooperate against him.</p>
<p><span class="star-pagination">*448</span> Second, respondent could have tried to escape the officers' presence by leaving the bus altogether. But because doing so would have required respondent to squeeze past the gun-wielding inquisitor who was blocking the aisle of the bus, this hardly seems like a course that respondent reasonably would have viewed as available to him.<sup>[3]</sup> The majority lamely protests that nothing in the stipulated facts shows that the questioning officer "<i>point[ed]</i> [his] gu[n] at [respondent] or otherwise <i>threaten[ed]</i> him" with the weapon. <i>Ante,</i> at 437 (emphasis added). Our decisions recognize the obvious point, however, that the choice of the police to "display" their weapons during an encounter exerts significant coercive pressure on the confronted citizen. <i>E. g., </i><i>Michigan</i> v. <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#575" aria-description="Citation for case: Michigan v. Chesternut"><i>Chesternut, supra,</i> at 575</a></span>; <i>United States</i> v. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><i>Mendenhall, supra,</i> at 554</a></span>. We have never suggested that the police must go so far as to put a citizen in immediate apprehension of <i>being shot</i> before a court can take account of the intimidating effect of being questioned by an officer with weapon in hand.</p>
<p>Even if respondent had perceived that the officers would <i>let</i> him leave the bus, moreover, he could not reasonably have been expected to resort to this means of evading their intrusive questioning. For so far as respondent knew, the bus' departure from the terminal was imminent. Unlike a person approached by the police on the street, see <i>Michigan</i> v. <i><span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/" aria-description="Citation for case: Michigan v. Chesternut">Chesternut, supra</a></span></i><i>,</i> or at a bus or airport terminal after reaching his destination, see <i>United States</i> v. <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall, supra</a></span></i><i>,</i> a passenger approached by the police at an intermediate point in a long bus journey cannot simply leave the scene and repair to a safe haven to avoid unwanted probing by law-enforcement officials. The vulnerability that an intrastate or interstate traveler experiences when confronted by the police outside of his "own familiar territory" surely aggravates <span class="star-pagination">*449</span> the coercive quality of such an encounter. See <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 247</a></span> (1973).</p>
<p>The case on which the majority primarily relies, <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984), is distinguishable in every relevant respect. In <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span>,</i> this Court held that workers approached by law-enforcement officials inside of a factory were not "seized" for purposes of the Fourth Amendment. The Court was careful to point out, however, that the presence of the agents did not furnish the workers with a reasonable basis for believing that they were not free to leave the factory, as at least some of them did. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 218-219</a></span>, and n. 7. Unlike passengers confronted by law-enforcement officials on a bus stopped temporarily at an intermediate point in its journey, workers approached by law-enforcement officials at their workplace need not abandon personal belongings and venture into unfamiliar environs in order to avoid unwanted questioning. Moreover, the workers who did not leave the building in <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> remained free to move about the entire factory, see <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 218</a></span>, a considerably less confining environment than a bus. Finally, contrary to the officer who confronted respondent, the law-enforcement officials in <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado</a></span></i> did not conduct their interviews with guns in hand. See <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#212" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>id.,</i> at 212</a></span>.</p>
<p>Rather than requiring the police to justify the coercive tactics employed here, the majority blames respondent for his own sensation of constraint. The majority concedes that respondent "did not feel free to leave the bus" as a means of breaking off the interrogation by the Broward County officers. <i>Ante,</i> at 436. But this experience of confinement, the majority explains, "was the natural result of <i>his</i> decision to take the bus." <i><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Ibid.</a></span></i> (emphasis added). Thus, in the majority's view, because respondent's "freedom of movement was restricted by a factor independent of police conduct  <i>i. e.,</i> by his being a passenger on a bus," <i>ante,</i> at 436  respondent was not seized for purposes of the Fourth Amendment.</p>
<p><span class="star-pagination">*450</span> This reasoning borders on sophism and trivializes the values that underlie the Fourth Amendment. Obviously, a person's "voluntary decision" to place himself in a room with only one exit does not authorize the police to force an encounter upon him by placing themselves in front of the exit. It is no more acceptable for the police to force an encounter on a person by exploiting his "voluntary decision" to expose himself to perfectly legitimate personal or social constraints. By consciously deciding to single out persons who have undertaken interstate or intrastate travel, officers who conduct suspicionless, dragnet-style sweeps put passengers to the choice of cooperating or of exiting their buses and possibly being stranded in unfamiliar locations. It is exactly because this "choice" is no "choice" at all that police engage this technique.</p>
<p>In my view, the Fourth Amendment clearly condemns the suspicionless, dragnet-style sweep of intrastate or interstate buses. Withdrawing this particular weapon from the government's drug-war arsenal would hardly leave the police without any means of combatting the use of buses as instrumentalities of the drug trade. The police would remain free, for example, to approach passengers whom they have a reasonable, articulable basis to suspect of criminal wrongdoing.<sup>[4]</sup> Alternatively, they could continue to confront passengers without suspicion so long as they took simple steps, like advising the passengers confronted of their right to decline to be questioned, to dispel the aura of coercion and intimidation that pervades such encounters. There is no reason to expect that such requirements would render the Nation's buses law-enforcement-free zones.</p>
<p></p>
<h2>III</h2>
<p>The majority attempts to gloss over the violence that today's decision does to the Fourth Amendment with empty admonitions. "If th[e] [war on drugs] is to be fought," the majority <span class="star-pagination">*451</span> intones, "those who fight it must respect the rights of individuals, whether or not those individuals are suspected of having committed a crime." <i>Ante,</i> at 439. The majority's actions, however, speak louder than its words.</p>
<p>I dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Mary Irene Coombs, Steven R. Shapiro, John A. Powell, James K. Green, Jeffrey S. Weiner,</i> and <i>Robert G. Amsel</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.
</p>
<p><i>Fred E. Inbau, Wayne W. Schmidt, Bernard J. Farber,</i> and <i>James P. Manak</i> filed a brief for Americans for Effective Law Enforcement as <i>amicus curiae.</i></p>
<p>[*]  The dissent acknowledges that the Florida Supreme Court's answer to the certified question reads like a <i>per se</i> rule, but dismisses as "implausible" the notion that the court would actually apply this rule to "trump" a careful analysis of all the relevant facts. <i>Post,</i> at 445. Implausible as it may seem, that is precisely what the Florida Supreme Court does. It routinely grants review in bus search cases and quashes denials of motions to suppress <i>expressly on the basis of its answer to the certified question in this case.</i> See, <i>e. g., </i><i>McBride</i> v. <i>State,</i> <span class="citation" data-id="1721587"><a href="/opinion/1721587/mcbride-v-state/" aria-description="Citation for case: McBride v. State">554 So. 2d 1160</a></span> (1989); <i>Mendez</i> v. <i>State,</i> <span class="citation" data-id="1721924"><a href="/opinion/1721924/mendez-v-state/" aria-description="Citation for case: Mendez v. State">554 So. 2d 1161</a></span> (1989); <i>Shaw</i> v. <i>State,</i> <span class="citation" data-id="1817337"><a href="/opinion/1817337/shaw-v-state/" aria-description="Citation for case: Shaw v. State">555 So. 2d 351</a></span> (1989); <i>Avery</i> v. <i>State,</i> <span class="citation" data-id="1817273"><a href="/opinion/1817273/avery-v-state/" aria-description="Citation for case: Avery v. State">555 So. 2d 351</a></span> (1989); <i>Serpa</i> v. <i>State,</i> <span class="citation" data-id="1816927"><a href="/opinion/1816927/serpa-v-state/" aria-description="Citation for case: Serpa v. State">555 So. 2d 1210</a></span> (1989); <i>Jones</i> v. <i>State,</i> <span class="citation" data-id="1905980"><a href="/opinion/1905980/jones-v-state/" aria-description="Citation for case: Jones v. State">559 So. 2d 1096</a></span> (1990).</p>
<p>[1]  That is to say, the police who conduct these sweeps decline to offer a reasonable, articulable suspicion of criminal wrongdoing sufficient to justify a warrantless "stop" or "seizure" of the confronted passenger. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-22, 30-31</a></span> (1968); <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 498-499</a></span> (1983) (plurality opinion). It does not follow, however, that the approach of passengers during a sweep is completely random. Indeed, at least one officer who routinely confronts interstate travelers candidly admitted that <i>race</i> is a factor influencing his decision whom to approach. See <i>United States</i> v. <i>Williams,</i> No. 1:89CR0135 (ND Ohio, June 13, 1989), p. 3 ("Detective Zaller testified that the factors initiating the focus upon the three young black males in this case included: (1) that they were young and black...."), aff'd, No. 89-4083 (CA6, Oct. 19, 1990), p. 7 (the officers "knew that the couriers, more often than not, were young black males"), vacated and remanded, <span class="citation multiple-matches"><a href="/c/U.%20S./500/901/">500 U. S. 901</a></span> (1991). Thus, the basis of the decision to single out particular passengers during a suspicionless sweep is less likely to be <i>inarticulable</i> than <i>unspeakable.</i></p>
<p>[2]  As reformulated, this question read:
</p>
<p>"Does an impermissible seizure result when police mount a drug search on buses during scheduled stops and question boarded passengers without articulable reasons for doing so, thereby obtaining consent to search the passengers' luggage?" 554 So. 2d, at 1154.</p>
<p>[3]  As the majority's discussion makes plain, see <i>ante,</i> at 432, 437, the officer questioning respondent clearly carried a weapons pouch during the interview. See also 554 So. 2d, at 1157.</p>
<p>[4]  Insisting that police officers explain their decision to single out a particular passenger for questioning would help prevent their reliance on impermissible criteria such as race. See n. 1, <i>supra.</i></p>

</div>
```

---

## GROUP: content/cases/Florida v. Harris.md  (`case`, 5 assertions)

### content_page

```
---
title: "Florida v. Harris"
type: case
citation: "568 U.S. 237 (2013)"
parallel_cite: "133 S. Ct. 1050; 185 L. Ed. 2d 61"
neutral_cite: 2013 U.S. LEXIS 1121
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-02-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-02-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Harris
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/820744/florida-v-harris/"
  cluster_id: 820744
  opinion_id: 820744
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Florida v. Jardines]]", "[[District of Columbia v. Wesby]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "drug-dog", "dog-sniff"]
holding: "Whether a dog's alert furnishes probable cause is a totality-of-the-circumstances question; evidence of a dog's satisfactory performance…"
lake:
  record_id: Florida v. Harris
  status: verified
  projected_at: 2026-07-06
---

# Florida v. Harris

*568 U.S. 237 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Florida deputy stopped Clayton Harris's truck for an expired tag and deployed his drug-detection dog, Aldo, who alerted at the driver's door. The ensuing search turned up materials for making methamphetamine. Harris moved to suppress, attacking Aldo's reliability; the Florida Supreme Court held that to establish probable cause the State must produce an exhaustive set of records, including the dog's field-performance history.

## Issue
Whether a trained drug-detection dog's alert establishes probable cause to search, and what a court must consider in evaluating the dog's reliability.

## Rule
Whether a dog's alert supplies probable cause is a totality-of-the-circumstances question, not a rigid checklist: "The question—similar to every inquiry into probable cause—is whether all the facts surrounding a dog's alert, viewed through the lens of common sense, would make a reasonably prudent person think that a search would reveal contraband or evidence of a crime. A sniff is up to snuff when it meets that test." — 568 U.S. at 248. ^pin-248

Training and certification, rather than field-performance records, are the better measure of reliability: "evidence of a dog's satisfactory performance in a certification or training program can itself provide sufficient reason to trust his alert." — *Id.* at 247. ^pin-247

A defendant must, however, have the opportunity to contest that evidence.

## Application
Aldo had completed two recent narcotics-detection courses and maintained his proficiency through weekly training, and Harris did not contest that training in the trial court. On the totality of those circumstances, Aldo's alert gave the deputy probable cause to search the truck; the Florida Supreme Court's inflexible evidentiary checklist was the wrong standard.

## Conclusion
A trained dog's alert can furnish probable cause under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; the Florida Supreme Court's rigid evidentiary rule was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Harris* governs the reliability side of a dog sniff; the separate question whether bringing a drug dog onto a home's [[Curtilage|curtilage]] is itself a search is answered in [[Florida v. Jardines]].

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. Harris*, 568 U.S. 237 (2013) — https://www.courtlistener.com/opinion/820744/florida-v-harris/ — pinpoints: 247, 248.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8862f11e1e65bc54", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "568 U.S. 237 (2013)", "court": "U.S. Supreme Court", "neutral_cite": "2013 U.S. LEXIS 1121", "official_citation_present": true, "parallel_cite": "133 S. Ct. 1050; 185 L. Ed. 2d 61", "title": "Florida v. Harris", "year": "2013"}}
{"assertion_id": "7fdce2877633a353", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Key — Progeny / Refinement", "title": "Florida v. Harris"}}
{"assertion_id": "f40bda4da517794f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Whether a dog's alert furnishes probable cause is a totality-of-the-circumstances question; evidence of a dog's satisfactory performance…", "title": "Florida v. Harris"}}
{"assertion_id": "771d0c00da9b575a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Florida v. Harris"}}
{"assertion_id": "eeb76051ce0fc1e8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2013-02-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Florida v. Harris", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Florida v. Harris", "varies_by_point": "false"}}
```

### lake record — Florida v. Harris

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Harris",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Harris",
    "case_name_short": "Harris",
    "case_name_full": "Florida v. Harris",
    "input_case_name": "Florida v. Harris",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-02-19",
    "year": 2013,
    "docket": null,
    "cluster_id": 820744,
    "lead_opinion_id": 820744,
    "sibling_ids": [
      820744
    ],
    "absolute_url": "/opinion/820744/florida-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "568 U.S. 237",
      "volume": "568",
      "reporter": "U.S.",
      "page": "237",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "133 S. Ct. 1050",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1050",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 61",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "61",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 1121",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1050",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1050",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 61",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "61",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 1121",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "1121",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "568 U.S. 237",
        "volume": "568",
        "reporter": "U.S.",
        "page": "237",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "568 U.S. 237",
    "official_selection": {
      "court_class": "scotus",
      "selected": "568 U.S. 237",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-248",
      "page": null,
      "quote": "--- # Florida v. Harris *568 U.S. 237 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Florida deputy stopped Clayton Harris's truck for an expired tag and deployed his drug-detection dog, Aldo, who alerted at the driver's door. The ensuing search turned up materials for making methamphetamine. Harris moved to suppress, attacking Aldo's reliability; the Florida Supreme Court held that to establish probable cause the State must produce an exhaustive set of records, including the dog's field-performance history. ## Issue Whether a trained drug-detection dog's alert establishes probable cause to search, and what a court must consider in evaluating the dog's reliability. ## Rule Whether a dog's alert supplies probable cause is a totality-of-the-circumstances question, not a rigid checklist:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-247",
      "page": null,
      "quote": "evidence of a dog's satisfactory performance in a certification or training program can itself provide sufficient reason to trust his alert.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-02-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Harris",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Mickel",
          "cluster_id": 10680424,
          "cite": [
            "321 Ga. 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grimm v. State",
          "cluster_id": 4488743,
          "cite": [
            "183 A.3d 167",
            "458 Md. 602"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hadley",
          "cluster_id": 4454377,
          "cite": [
            "410 P.3d 140",
            "55 Kan. App. 2d 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felders v. Malcom",
          "cluster_id": 2679716,
          "cite": [
            "755 F.3d 870",
            "2014 WL 2782368",
            "2014 U.S. App. LEXIS 11627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Westerfield",
          "cluster_id": 4587116,
          "cite": [
            "243 Cal. Rptr. 3d 18",
            "433 P.3d 914",
            "6 Cal. 5th 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Omar Paez v. Claudia Mulvey",
          "cluster_id": 4588729,
          "cite": [
            "915 F.3d 1276"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Albert White",
          "cluster_id": 4438318,
          "cite": [
            "874 F.3d 490",
            "2017 FED App. 0242P",
            "2017 WL 4848911",
            "2017 U.S. App. LEXIS 21332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zalaski v. City of Hartford",
          "cluster_id": 1034747,
          "cite": [
            "723 F.3d 382",
            "2013 WL 3796448",
            "2013 U.S. App. LEXIS 14898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "April Smith v. Jason Munday",
          "cluster_id": 4345933,
          "cite": [
            "848 F.3d 248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Gadson",
          "cluster_id": 2719320,
          "cite": [
            "763 F.3d 1189",
            "2014 WL 4067203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthews, Cornelious L.",
          "cluster_id": 2949477,
          "cite": [
            "431 S.W.3d 596",
            "2014 WL 3029070",
            "2014 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Boyce",
          "cluster_id": 4765497,
          "cite": [
            "2020 Ohio 3573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ricky Brown",
          "cluster_id": 3219351,
          "cite": [
            "828 F.3d 375",
            "2016 FED App. 0148P",
            "2016 U.S. App. LEXIS 11739",
            "2016 WL 3584723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Booker Powell",
          "cluster_id": 1043365,
          "cite": [
            "732 F.3d 361",
            "2013 WL 5493969"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hinkle v. Beckham County Board of County",
          "cluster_id": 4762695,
          "cite": [
            "962 F.3d 1204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ganek v. Leibowitz",
          "cluster_id": 4434937,
          "cite": [
            "874 F.3d 73",
            "2017 WL 4639594",
            "2017 U.S. App. LEXIS 20226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zuniga",
          "cluster_id": 4247572,
          "cite": [
            "2016 CO 52",
            "372 P.3d 1052",
            "2016 WL 3574390"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miguel Gutierrez v. Michael Kermon",
          "cluster_id": 2709559,
          "cite": [
            "722 F.3d 1003",
            "2013 WL 3481359",
            "2013 U.S. App. LEXIS 14101"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David Jones v. Clark Cty., Ky.",
          "cluster_id": 4754762,
          "cite": [
            "959 F.3d 748"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson, Williams & Spriggs v. State",
          "cluster_id": 4340111,
          "cite": [
            "152 A.3d 661",
            "451 Md. 94"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rasanen v. Brown",
          "cluster_id": 1034417,
          "cite": [
            "723 F.3d 325",
            "86 Fed. R. Serv. 3d 351",
            "2013 WL 3766538",
            "2013 U.S. App. LEXIS 14628"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eleuterio Murillo-Salgado",
          "cluster_id": 4382837,
          "cite": [
            "854 F.3d 407",
            "2017 WL 1359478",
            "2017 U.S. App. LEXIS 6324"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Miller",
          "cluster_id": 4835528,
          "cite": [
            "982 F.3d 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christie",
          "cluster_id": 899673,
          "cite": [
            "717 F.3d 1156",
            "2013 U.S. App. LEXIS 11704",
            "2013 WL 2477252"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Manzo",
          "cluster_id": 4658488,
          "cite": [
            "2018 IL 122761"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyree Bell v. Officer Peter Neukirch",
          "cluster_id": 4801444,
          "cite": [
            "979 F.3d 594"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Harris:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(820744) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDY0OTEyMDAwMDAwJnM9MzIwOTE1OSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28820744%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(820744)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNyZzPTQ2Mjc0MTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28820744%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(820744)",
        "reviewed": 98,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 98,
        "triage_read": 1,
        "triage_snippet_classified": 97
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(820744)",
    "indexed_citing_opinions": 351,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 820744,
        "count": 351,
        "count_source": "search"
      }
    ],
    "citation_count": 784,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-harris.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNzU2NjUmcz0xMDU5NTU4NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28820744%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 820744,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 131150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 145852,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 1640193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 820744,
        "cited_id": 2490998,
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
    "date_created": "2026-07-05T03:48:49Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:49:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:49:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:54:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:49:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Harris

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                           FLORIDA v. HARRIS

        CERTIORARI TO THE SUPREME COURT OF FLORIDA

  No. 11–817.      Argued October 31, 2012—Decided February 19, 2013
Officer Wheetley pulled over respondent Harris for a routine traffic
  stop. Observing Harris’s nervousness and an open beer can, Wheet-
  ley sought consent to search Harris’s truck. When Harris refused,
  Wheetley executed a sniff test with his trained narcotics dog, Aldo.
  The dog alerted at the driver’s-side door handle, leading Wheetley to
  conclude that he had probable cause for a search. That search turned
  up nothing Aldo was trained to detect, but did reveal pseudoephed-
  rine and other ingredients for manufacturing methamphetamine.
  Harris was arrested and charged with illegal possession of those in-
  gredients. In a subsequent stop while Harris was out on bail, Aldo
  again alerted on Harris’s truck but nothing of interest was found. At
  a suppression hearing, Wheetley testified about his and Aldo’s exten-
  sive training in drug detection. Harris’s attorney did not contest the
  quality of that training, focusing instead on Aldo’s certification and
  performance in the field, particularly in the two stops of Harris’s
  truck. The trial court denied the motion to suppress, but the Florida
  Supreme Court reversed. It held that a wide array of evidence was
  always necessary to establish probable cause, including field-
  performance records showing how many times the dog has falsely
  alerted. If an officer like Wheetley failed to keep such records, he
  could never have probable cause to think the dog a reliable indicator
  of drugs.
Held: Because training and testing records supported Aldo’s reliability
 in detecting drugs and Harris failed to undermine that evidence,
 Wheetley had probable cause to search Harris’s truck. Pp. 5–11.
    (a) In testing whether an officer has probable cause to conduct a
 search, all that is required is the kind of “fair probability” on which
 “reasonable and prudent [people] act.” Illinois v. Gates, 462 U. S.
 213, 235. To evaluate whether the State has met this practical and
2                          FLORIDA v. HARRIS

                                  Syllabus

    common-sensical standard, this Court has consistently looked to the
    totality of the circumstances and rejected rigid rules, bright-line
    tests, and mechanistic inquiries. Ibid.
       The Florida Supreme Court flouted this established approach by
    creating a strict evidentiary checklist to assess a drug-detection dog’s
    reliability. Requiring the State to introduce comprehensive docu-
    mentation of the dog’s prior hits and misses in the field, and holding
    that absent field records will preclude a finding of probable cause no
    matter how much other proof the State offers, is the antithesis of a
    totality-of-the-circumstances approach. This is made worse by the
    State Supreme Court’s treatment of field-performance records as the
    evidentiary gold standard when, in fact, such data may not capture a
    dog’s false negatives or may markedly overstate a dog’s false posi-
    tives. Such inaccuracies do not taint records of a dog’s performance
    in standard training and certification settings, making that perfor-
    mance a better measure of a dog’s reliability. Field records may
    sometimes be relevant, but the court should evaluate all the evi-
    dence, and should not prescribe an inflexible set of requirements.
       Under the correct approach, a probable-cause hearing focusing on a
    dog’s alert should proceed much like any other, with the court allow-
    ing the parties to make their best case and evaluating the totality of
    the circumstances. If the State has produced proof from controlled
    settings that a dog performs reliably in detecting drugs, and the de-
    fendant has not contested that showing, the court should find proba-
    ble cause. But a defendant must have an opportunity to challenge
    such evidence of a dog’s reliability, whether by cross-examining the
    testifying officer or by introducing his own fact or expert witnesses.
    The defendant may contest training or testing standards as flawed or
    too lax, or raise an issue regarding the particular alert. The court
    should then consider all the evidence and apply the usual test for
    probable cause—whether all the facts surrounding the alert, viewed
    through the lens of common sense, would make a reasonably prudent
    person think that a search would reveal contraband or evidence of a
    crime. Pp. 5–9.
       (b) The record in this case amply supported the trial court’s deter-
    mination that Aldo’s alert gave Wheetley probable cause to search
    the truck. The State introduced substantial evidence of Aldo’s train-
    ing and his proficiency in finding drugs. Harris declined to challenge
    any aspect of that training or testing in the trial court, and the Court
    does not consider such arguments when they are presented for this
    first time in this Court. Harris principally relied below on Wheetley’s
    failure to find any substance that Aldo was trained to detect. That
    infers too much from the failure of a particular alert to lead to drugs,
    and did not rebut the State’s evidence from recent training and test-
                     Cite as: 568 U. S. ____ (2013)         3

                               Syllabus

  ing. Pp. 9–11.
71 So. 3d 756, reversed.

  KAGAN, J., delivered the opinion for a unanimous Court.
                        Cite as: 568 U. S. ____ (2013)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 11–817
                                   _________________


     FLORIDA, PETITIONER v. CLAYTON HARRIS
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                              [February 19, 2013]


   JUSTICE KAGAN delivered the opinion of the Court.
   In this case, we consider how a court should determine
if the “alert” of a drug-detection dog during a traffic stop
provides probable cause to search a vehicle. The Florida
Supreme Court held that the State must in every case
present an exhaustive set of records, including a log of the
dog’s performance in the field, to establish the dog’s relia-
bility. See 71 So. 3d 756, 775 (2011). We think that de-
mand inconsistent with the “flexible, common-sense
standard” of probable cause. Illinois v. Gates, 462 U. S.
213, 239 (1983).
                             I
   William Wheetley is a K–9 Officer in the Liberty County,
Florida Sheriff ’s Office. On June 24, 2006, he was on a
routine patrol with Aldo, a German shepherd trained to
detect certain narcotics (methamphetamine, marijuana,
cocaine, heroin, and ecstasy). Wheetley pulled over re-
spondent Clayton Harris’s truck because it had an expired
license plate. On approaching the driver’s-side door,
Wheetley saw that Harris was “visibly nervous,” unable to
sit still, shaking, and breathing rapidly. Wheetley also
noticed an open can of beer in the truck’s cup holder. App.
2                    FLORIDA v. HARRIS

                      Opinion of the Court

62. Wheetley asked Harris for consent to search the truck,
but Harris refused. At that point, Wheetley retrieved Aldo
from the patrol car and walked him around Harris’s truck
for a “free air sniff.” Id., at 63. Aldo alerted at the
driver’s-side door handle—signaling, through a distinctive
set of behaviors, that he smelled drugs there.
  Wheetley concluded, based principally on Aldo’s alert,
that he had probable cause to search the truck. His search
did not turn up any of the drugs Aldo was trained to de-
tect. But it did reveal 200 loose pseudoephedrine pills,
8,000 matches, a bottle of hydrochloric acid, two contain-
ers of antifreeze, and a coffee filter full of iodine crystals—
all ingredients for making methamphetamine. Wheetley
accordingly arrested Harris, who admitted after proper
Miranda warnings that he routinely “cooked” metham-
phetamine at his house and could not go “more than a few
days without using” it. Id., at 68. The State charged
Harris with possessing pseudoephedrine for use in manu-
facturing methamphetamine.
  While out on bail, Harris had another run-in with
Wheetley and Aldo. This time, Wheetley pulled Harris
over for a broken brake light. Aldo again sniffed the
truck’s exterior, and again alerted at the driver’s-side door
handle. Wheetley once more searched the truck, but on
this occasion discovered nothing of interest.
  Harris moved to suppress the evidence found in his
truck on the ground that Aldo’s alert had not given Wheet-
ley probable cause for a search. At the hearing on that
motion, Wheetley testified about both his and Aldo’s train-
ing in drug detection. See id., at 52–82. In 2004, Wheet-
ley (and a different dog) completed a 160-hour course in
narcotics detection offered by the Dothan, Alabama Police
Department, while Aldo (and a different handler) completed
a similar, 120-hour course given by the Apopka, Florida
Police Department. That same year, Aldo received a one-
year certification from Drug Beat, a private company that
                 Cite as: 568 U. S. ____ (2013)           3

                     Opinion of the Court

specializes in testing and certifying K–9 dogs. Wheetley
and Aldo teamed up in 2005 and went through another,
40-hour refresher course in Dothan together. They also
did four hours of training exercises each week to maintain
their skills. Wheetley would hide drugs in certain ve-
hicles or buildings while leaving others “blank” to deter-
mine whether Aldo alerted at the right places. Id., at 57.
According to Wheetley, Aldo’s performance in those exer-
cises was “really good.” Id., at 60. The State introduced
“Monthly Canine Detection Training Logs” consistent with
that testimony: They showed that Aldo always found
hidden drugs and that he performed “satisfactorily” (the
higher of two possible assessments) on each day of train-
ing. Id., at 109–116.
   On cross-examination, Harris’s attorney chose not to
contest the quality of Aldo’s or Wheetley’s training. She
focused instead on Aldo’s certification and his performance
in the field, particularly the two stops of Harris’s truck.
Wheetley conceded that the certification (which, he noted,
Florida law did not require) had expired the year before
he pulled Harris over. See id., at 70–71. Wheetley also
acknowledged that he did not keep complete records of
Aldo’s performance in traffic stops or other field work;
instead, he maintained records only of alerts resulting in
arrests. See id., at 71–72, 74. But Wheetley defended
Aldo’s two alerts to Harris’s seemingly narcotics-free
truck: According to Wheetley, Harris probably transferred
the odor of methamphetamine to the door handle, and
Aldo responded to that “residual odor.” Id., at 80.
   The trial court concluded that Wheetley had probable
cause to search Harris’s truck and so denied the motion to
suppress. Harris then entered a no-contest plea while
reserving the right to appeal the trial court’s ruling. An
intermediate state court summarily affirmed. See 989
So. 2d 1214, 1215 (2008) (per curiam).
   The Florida Supreme Court reversed, holding that
4                   FLORIDA v. HARRIS

                     Opinion of the Court

Wheetley lacked probable cause to search Harris’s vehicle
under the Fourth Amendment. “[W]hen a dog alerts,” the
court wrote, “the fact that the dog has been trained and
certified is simply not enough to establish probable cause.”
71 So. 3d, at 767. To demonstrate a dog’s reliability, the
State needed to produce a wider array of evidence:
    “[T]he State must present . . . the dog’s training and
    certification records, an explanation of the meaning of
    the particular training and certification, field perfor-
    mance records (including any unverified alerts), and
    evidence concerning the experience and training of the
    officer handling the dog, as well as any other objective
    evidence known to the officer about the dog’s reliabil-
    ity.” Id., at 775.
The court particularly stressed the need for “evidence of
the dog’s performance history,” including records showing
“how often the dog has alerted in the field without illegal
contraband having been found.” Id., at 769. That data,
the court stated, could help to expose such problems as a
handler’s tendency (conscious or not) to “cue [a] dog to
alert” and “a dog’s inability to distinguish between resid-
ual odors and actual drugs.” Id., at 769, 774. Accordingly,
an officer like Wheetley who did not keep full records of
his dog’s field performance could never have the requisite
cause to think “that the dog is a reliable indicator of
drugs.” Id., at 773.
   Judge Canady dissented, maintaining that the major-
ity’s “elaborate and inflexible evidentiary requirements”
went beyond the demands of probable cause. Id., at 775.
He would have affirmed the trial court’s ruling on the
strength of Aldo’s training history and Harris’s “fail[ure]
to present any evidence challenging” it. Id., at 776.
   We granted certiorari, 566 U. S. ___ (2012), and now
reverse.
                 Cite as: 568 U. S. ____ (2013)            5

                     Opinion of the Court

                               II
   A police officer has probable cause to conduct a search
when “the facts available to [him] would ‘warrant a [per-
son] of reasonable caution in the belief ’” that contraband
or evidence of a crime is present. Texas v. Brown, 460
U. S. 730, 742 (1983) (plurality opinion) (quoting Carroll v.
United States, 267 U. S. 132, 162 (1925)); see Safford
Unified School Dist. #1 v. Redding, 557 U. S. 364, 370–
371 (2009). The test for probable cause is not reducible to
“precise definition or quantification.” Maryland v. Pringle,
540 U. S. 366, 371 (2003). “Finely tuned standards such
as proof beyond a reasonable doubt or by a preponderance
of the evidence . . . have no place in the [probable-cause]
decision.” Gates, 462 U. S., at 235. All we have required
is the kind of “fair probability” on which “reasonable and
prudent [people,] not legal technicians, act.” Id., at 238,
231 (internal quotation marks omitted).
   In evaluating whether the State has met this practical
and common-sensical standard, we have consistently
looked to the totality of the circumstances. See, e.g., Prin-
gle, 540 U. S., at 371; Gates, 462 U. S., at 232; Brinegar v.
United States, 338 U. S. 160, 176 (1949). We have rejected
rigid rules, bright-line tests, and mechanistic inquiries in
favor of a more flexible, all-things-considered approach. In
Gates, for example, we abandoned our old test for as-
sessing the reliability of informants’ tips because it had
devolved into a “complex superstructure of evidentiary
and analytical rules,” any one of which, if not complied
with, would derail a finding of probable cause. 462 U. S.,
at 235. We lamented the development of a list of “inflexi-
ble, independent requirements applicable in every case.”
Id., at 230, n. 6. Probable cause, we emphasized, is “a
fluid concept—turning on the assessment of probabilities
in particular factual contexts—not readily, or even use-
fully, reduced to a neat set of legal rules.” Id., at 232.
   The Florida Supreme Court flouted this established
6                         FLORIDA v. HARRIS

                          Opinion of the Court

approach to determining probable cause. To assess the
reliability of a drug-detection dog, the court created a
strict evidentiary checklist, whose every item the State
must tick off.1 Most prominently, an alert cannot estab-
lish probable cause under the Florida court’s decision
unless the State introduces comprehensive documentation
of the dog’s prior “hits” and “misses” in the field. (One
wonders how the court would apply its test to a rookie
dog.) No matter how much other proof the State offers of
the dog’s reliability, the absent field performance records
will preclude a finding of probable cause. That is the
antithesis of a totality-of-the-circumstances analysis. It
is, indeed, the very thing we criticized in Gates when we
overhauled our method for assessing the trustworthiness
of an informant’s tip. A gap as to any one matter, we
explained, should not sink the State’s case; rather, that
“deficiency . . . may be compensated for, in determining
the overall reliability of a tip, by a strong showing as to . . .
other indicia of reliability.” Id., at 233. So too here, a
finding of a drug-detection dog’s reliability cannot depend
on the State’s satisfaction of multiple, independent eviden-
tiary requirements. No more for dogs than for human
informants is such an inflexible checklist the way to prove
reliability, and thus establish probable cause.
   Making matters worse, the decision below treats records
of a dog’s field performance as the gold standard in evi-
——————
    1 Bythe time of oral argument in this case, even Harris declined to
defend the idea that the Fourth Amendment compels the State to
produce each item of evidence the Florida Supreme Court enumerated.
See Tr. of Oral Arg. 29–30 (“I don’t believe the Constitution requires
[that list]”). Harris instead argued that the court’s decision, although
“look[ing] rather didactic,” in fact did not impose any such requirement.
Id., at 29; see id., at 31 (“[I]t’s not a specific recipe that can’t be de-
viated from”). But in reading the decision below as establishing a man-
datory checklist, we do no more than take the court at its (oft-repeated)
word. See, e.g., 71 So. 3d 756, 758, 759, 771, 775 (Fla. 2011) (holding
that the State “must” present the itemized evidence).
                      Cite as: 568 U. S. ____ (2013)                      7

                           Opinion of the Court

dence, when in most cases they have relatively limited
import. Errors may abound in such records. If a dog
on patrol fails to alert to a car containing drugs, the mis-
take usually will go undetected because the officer will not
initiate a search. Field data thus may not capture a dog’s
false negatives. Conversely (and more relevant here), if
the dog alerts to a car in which the officer finds no narcot-
ics, the dog may not have made a mistake at all. The dog
may have detected substances that were too well hidden or
present in quantities too small for the officer to locate. Or
the dog may have smelled the residual odor of drugs pre-
viously in the vehicle or on the driver’s person.2 Field data
thus may markedly overstate a dog’s real false positives.
By contrast, those inaccuracies—in either direction—do
not taint records of a dog’s performance in standard train-
ing and certification settings. There, the designers of an
assessment know where drugs are hidden and where they
are not—and so where a dog should alert and where he
——————
  2 See  U. S. Dept. of Army, Military Working Dog Program 30 (Pam-
phlet 190–12, 1993) (“The odor of a substance may be present in enough
concentration to cause the dog to respond even after the substance has
been removed. Therefore, when a detector dog responds and no drug
or explosive is found, do not assume the dog has made an error”);
S. Bryson, Police Dog Tactics 257 (2d ed. 2000) (“Four skiers toke up in
the parking lot before going up the mountain. Five minutes later a
narcotic detector dog alerts to the car. There is no dope inside. How-
ever, the dog has performed correctly”). The Florida Supreme Court
treated a dog’s response to residual odor as an error, referring to the
“inability to distinguish between [such] odors and actual drugs” as a
“facto[r] that call[s] into question Aldo’s reliability.” 71 So. 3d, at 773–
774; see supra, at 4. But that statement reflects a misunderstanding.
A detection dog recognizes an odor, not a drug, and should alert when-
ever the scent is present, even if the substance is gone (just as a police
officer’s much inferior nose detects the odor of marijuana for some time
after a joint has been smoked). In the usual case, the mere chance that
the substance might no longer be at the location does not matter; a
well-trained dog’s alert establishes a fair probability—all that is re-
quired for probable cause—that either drugs or evidence of a drug
crime (like the precursor chemicals in Harris’s truck) will be found.
8                        FLORIDA v. HARRIS

                          Opinion of the Court

should not. The better measure of a dog’s reliability
thus comes away from the field, in controlled testing
environments.3
  For that reason, evidence of a dog’s satisfactory perfor-
mance in a certification or training program can itself
provide sufficient reason to trust his alert. If a bona fide
organization has certified a dog after testing his reliability
in a controlled setting, a court can presume (subject to any
conflicting evidence offered) that the dog’s alert provides
probable cause to search. The same is true, even in the
absence of formal certification, if the dog has recently and
successfully completed a training program that evaluated
his proficiency in locating drugs. After all, law enforce-
ment units have their own strong incentive to use effective
training and certification programs, because only accurate
drug-detection dogs enable officers to locate contraband
without incurring unnecessary risks or wasting limited
time and resources.
  A defendant, however, must have an opportunity to
challenge such evidence of a dog’s reliability, whether by
cross-examining the testifying officer or by introducing his
own fact or expert witnesses. The defendant, for example,
may contest the adequacy of a certification or training
program, perhaps asserting that its standards are too lax
or its methods faulty. So too, the defendant may examine
how the dog (or handler) performed in the assessments
made in those settings. Indeed, evidence of the dog’s (or
handler’s) history in the field, although susceptible to the
kind of misinterpretation we have discussed, may some-
times be relevant, as the Solicitor General acknowledged
——————
   3 See K. Furton, J. Greb, & H. Holness, Florida Int’l Univ., The Scien-

tific Working Group on Dog and Orthogonal Detector Guidelines 1, 61–
62, 66 (2010) (recommending as a “best practice” that a dog’s reliability
should be assessed based on “the results of certification and proficiency
assessments,” because in those “procedure[s] you should know whether
you have a false positive,” unlike in “most operational situations”).
                 Cite as: 568 U. S. ____ (2013)           9

                     Opinion of the Court

at oral argument. See Tr. of Oral Arg. 23–24 (“[T]he
defendant can ask the handler, if the handler is on the
stand, about field performance, and then the court can
give that answer whatever weight is appropriate”). And
even assuming a dog is generally reliable, circumstances
surrounding a particular alert may undermine the case
for probable cause—if, say, the officer cued the dog (con-
sciously or not), or if the team was working under un-
familiar conditions.
   In short, a probable-cause hearing focusing on a dog’s
alert should proceed much like any other. The court
should allow the parties to make their best case, con-
sistent with the usual rules of criminal procedure. And
the court should then evaluate the proffered evidence to
decide what all the circumstances demonstrate. If the
State has produced proof from controlled settings that a
dog performs reliably in detecting drugs, and the defend-
ant has not contested that showing, then the court should
find probable cause. If, in contrast, the defendant has
challenged the State’s case (by disputing the reliability of
the dog overall or of a particular alert), then the court
should weigh the competing evidence. In all events, the
court should not prescribe, as the Florida Supreme Court
did, an inflexible set of evidentiary requirements. The
question—similar to every inquiry into probable cause—is
whether all the facts surrounding a dog’s alert, viewed
through the lens of common sense, would make a reason-
ably prudent person think that a search would reveal con-
traband or evidence of a crime. A sniff is up to snuff when
it meets that test.
                             III
  And here, Aldo’s did. The record in this case amply
supported the trial court’s determination that Aldo’s alert
gave Wheetley probable cause to search Harris’s truck.
  The State, as earlier described, introduced substantial
10                  FLORIDA v. HARRIS

                     Opinion of the Court

evidence of Aldo’s training and his proficiency in finding
drugs. See supra, at 2–3. The State showed that two
years before alerting to Harris’s truck, Aldo had success-
fully completed a 120-hour program in narcotics detection,
and separately obtained a certification from an independ-
ent company. And although the certification expired after
a year, the Sheriff ’s Office required continuing training
for Aldo and Wheetley. The two satisfied the require-
ments of another, 40-hour training program one year prior
to the search at issue. And Wheetley worked with Aldo
for four hours each week on exercises designed to keep
their skills sharp. Wheetley testified, and written records
confirmed, that in those settings Aldo always performed at
the highest level.
   Harris, as also noted above, declined to challenge in the
trial court any aspect of Aldo’s training. See supra, at 3.
To be sure, Harris’s briefs in this Court raise questions
about that training’s adequacy—for example, whether the
programs simulated sufficiently diverse environments and
whether they used enough blind testing (in which the
handler does not know the location of drugs and so cannot
cue the dog). See Brief for Respondent 57–58. Similarly,
Harris here queries just how well Aldo performed in con-
trolled testing. See id., at 58. But Harris never voiced
those doubts in the trial court, and cannot do so for the
first time here. See, e.g., Rugendorf v. United States, 376
U. S. 528, 534 (1964). As the case came to the trial court,
Aldo had successfully completed two recent drug-detection
courses and maintained his proficiency through weekly
training exercises. Viewed alone, that training record—
with or without the prior certification—sufficed to estab-
lish Aldo’s reliability. See supra, at 8–9.
   And Harris’s cross-examination of Wheetley, which
focused on Aldo’s field performance, failed to rebut the
State’s case. Harris principally contended in the trial
court that because Wheetley did not find any of the sub-
                 Cite as: 568 U. S. ____ (2013)                 11

                     Opinion of the Court

stances Aldo was trained to detect, Aldo’s two alerts must
have been false. See Brief for Respondent 1; App. 77–80.
But we have already described the hazards of inferring too
much from the failure of a dog’s alert to lead to drugs, see
supra, at 7; and here we doubt that Harris’s logic does
justice to Aldo’s skills. Harris cooked and used metham-
phetamine on a regular basis; so as Wheetley later sur-
mised, Aldo likely responded to odors that Harris had
transferred to the driver’s-side door handle of his truck.
See supra, at 3. A well-trained drug-detection dog should
alert to such odors; his response to them might appear
a mistake, but in fact is not. See n. 2, supra. And still
more fundamentally, we do not evaluate probable cause in
hindsight, based on what a search does or does not turn
up. See United States v. Di Re, 332 U. S. 581, 595 (1948).
For the reasons already stated, Wheetley had good cause
to view Aldo as a reliable detector of drugs. And no special
circumstance here gave Wheetley reason to discount Aldo’s
usual dependability or distrust his response to Harris’s
truck.
   Because training records established Aldo’s reliability in
detecting drugs and Harris failed to undermine that show-
ing, we agree with the trial court that Wheetley had prob-
able cause to search Harris’s truck. We accordingly
reverse the judgment of the Florida Supreme Court.

                                                  It is so ordered.

```

---

## GROUP: content/cases/Florida v. J.L..md  (`case`, 5 assertions)

### content_page

```
---
title: "Florida v. J.L."
type: case
citation: "529 U.S. 266 (2000)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-03-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-03-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. J.L.
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9189388/florida-v-j-l/"
  cluster_id: 9189388
  opinion_id: 9184148
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Alabama v. White]]", "[[Terry v. Ohio]]", "[[Illinois v. Gates]]"]
aliases: ["Florida v. JL"]
tags: ["case", "fourth-amendment", "reasonable-suspicion", "anonymous-tip", "stop-and-frisk"]
holding: "A bare anonymous tip that a person is carrying a gun, without more, is NOT reasonable suspicion for a stop and frisk; an accurate…"
lake:
  record_id: Florida v. J.L.
  status: verified
  projected_at: 2026-07-09
---

# Florida v. J.L.

*529 U.S. 266 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An anonymous caller told Miami-Dade police that a young Black male standing at a particular bus stop and wearing a plaid shirt was carrying a gun. Officers went to the bus stop, saw J.L. (a juvenile) matching the description, frisked him on no other basis, and found a firearm. The tip supplied no predictive information, so the officers had no way to test the caller's knowledge or credibility before the frisk.

## Issue
Whether an anonymous tip that a person is carrying a gun, without more, furnishes the reasonable suspicion needed to justify a [[Terry Stops and Reasonable Suspicion|Terry stop]] and frisk.

## Rule
No. A bare anonymous tip that merely identifies a person is not enough; the tip must be reliable about the alleged wrongdoing, not just about who the suspect is. "The reasonable suspicion here at issue requires that a tip be reliable in its assertion of illegality, not just in its tendency to identify a determinate person." — 529 U.S. at 272. ^pin-272

The Court refused to recognize a "firearm exception" that would permit a stop and frisk on a gun tip that failed standard reliability testing: "We decline to adopt this position." — [*Id.*](https://www.courtlistener.com/opinion/9189388/florida-v-j-l/#:~:text=justifies%20a%20%E2%80%9C-,firearm%20exception) ^pin-272a

## Application
All the police had was an unknown caller's bare assertion that J.L. had a gun; the tip offered no predictive detail and nothing showing the caller knew of concealed criminal activity. That the description of J.L.'s appearance proved accurate showed only that the caller could identify him — not that he was breaking the law — so the officers lacked reasonable suspicion and the frisk was unlawful.

## Conclusion
The anonymous gun tip did not supply reasonable suspicion; the firearm seized in the frisk should have been suppressed, and the Florida Supreme Court's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *J.L.* refines the anonymous-tip analysis of [[Alabama v. White]]: an accurate description of a suspect's appearance, without indicia that the tipster knows of criminal activity, does not establish reasonable suspicion.

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. J.L.*, 529 U.S. 266 (2000) — https://www.courtlistener.com/opinion/118352/florida-v-jl/ — pinpoint: 272.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bc26957a71b6325e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "529 U.S. 266 (2000)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Florida v. J.L.", "year": "2000"}}
{"assertion_id": "2c153c5943da5f09", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A bare anonymous tip that a person is carrying a gun, without more, is NOT reasonable suspicion for a stop and frisk; an accurate…", "title": "Florida v. J.L."}}
{"assertion_id": "343929a7a1088b9c", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "Florida v. J.L."}}
{"assertion_id": "10b12cee473d87a2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Florida v. J.L."}}
{"assertion_id": "198a79c2d6e4acdd", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-03-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Florida v. J.L.", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Florida v. J.L.", "varies_by_point": "false"}}
```

### lake record — Florida v. J.L.

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. J.L.",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. J. L.",
    "case_name_short": "",
    "case_name_full": "FLORIDA v. J. L.",
    "input_case_name": "Florida v. J.L.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-03-28",
    "year": 2000,
    "docket": null,
    "cluster_id": 9189388,
    "lead_opinion_id": 9184148,
    "sibling_ids": [
      9184148,
      9184150
    ],
    "absolute_url": "/opinion/9189388/florida-v-j-l/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9189387,
        "score": 120,
        "case_name": "Florida v. J. L."
      },
      {
        "cluster_id": 9264504,
        "score": 20,
        "case_name": "Florida v. J. L."
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "529 U.S. 266",
      "volume": "529",
      "reporter": "U.S.",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "529 U.S. 266",
        "volume": "529",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "529 U.S. 266",
    "official_selection": {
      "court_class": "scotus",
      "selected": "529 U.S. 266",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-272",
      "page": null,
      "quote": "--- # Florida v. J.L. *529 U.S. 266 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An anonymous caller told Miami-Dade police that a young Black male standing at a particular bus stop and wearing a plaid shirt was carrying a gun. Officers went to the bus stop, saw J.L. (a juvenile) matching the description, frisked him on no other basis, and found a firearm. The tip supplied no predictive information, so the officers had no way to test the caller's knowledge or credibility before the frisk. ## Issue Whether an anonymous tip that a person is carrying a gun, without more, furnishes the reasonable suspicion needed to justify a Terry stop and frisk. ## Rule No. A bare anonymous tip that merely identifies a person is not enough; the tip must be reliable about the alleged wrongdoing, not just about who the suspect is.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-272a",
      "page": null,
      "quote": "firearm exception",
      "star_marker": "269",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 3038,
      "fragment": "#:~:text=justifies%20a%20%E2%80%9C-,firearm%20exception",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-03-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. J.L.",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Jahloni G.",
          "cluster_id": 5957964,
          "cite": [
            "83 A.D.3d 485",
            "921 N.Y.S.2d 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 1057358,
          "cite": [
            "2008 VT 43",
            "954 A.2d 1290",
            "183 Vt. 401",
            "2008 Vt. LEXIS 44"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Aitoro",
          "cluster_id": 202211,
          "cite": [
            "446 F.3d 246",
            "2006 U.S. App. LEXIS 11767",
            "2006 WL 1303940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Swazine Swindle",
          "cluster_id": 790194,
          "cite": [
            "407 F.3d 562",
            "2005 U.S. App. LEXIS 8245",
            "2005 WL 1110925"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rigoberto Fernandez-Castillo",
          "cluster_id": 781494,
          "cite": [
            "324 F.3d 1114",
            "2003 Daily Journal DAR 3855",
            "2003 Cal. Daily Op. Serv. 3019",
            "2003 U.S. App. LEXIS 6598",
            "2003 WL 1811633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Montanez",
          "cluster_id": 6587119,
          "cite": [
            "55 Mass. App. Ct. 132",
            "769 N.E.2d 784",
            "2002 Mass. App. LEXIS 815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hawes v. State",
          "cluster_id": 1385029,
          "cite": [
            "125 S.W.3d 535",
            "2002 WL 287129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walter Harrell and Lawrence Dunham",
          "cluster_id": 775206,
          "cite": [
            "268 F.3d 141",
            "2001 U.S. App. LEXIS 21774"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fudge",
          "cluster_id": 1591103,
          "cite": [
            "42 S.W.3d 226",
            "2001 WL 193835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Colon",
          "cluster_id": 773257,
          "cite": [
            "250 F.3d 130",
            "2001 U.S. App. LEXIS 9205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reed",
          "cluster_id": 7113127,
          "cite": [
            "1 F. App'x 706"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Torrez v. State",
          "cluster_id": 1450090,
          "cite": [
            "34 S.W.3d 10",
            "2000 WL 1723658"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane1_negative"
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
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Moore",
          "cluster_id": 2037938,
          "cite": [
            "847 N.E.2d 1141",
            "6 N.Y.3d 496",
            "814 N.Y.S.2d 567"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sylvia Panetta v. Thomas M. Crowley, Marc Jurnove, Patricia A. Kelvasa, John Doe I, Docket No. 02-7275-Cv",
          "cluster_id": 795420,
          "cite": [
            "460 F.3d 388",
            "2006 U.S. App. LEXIS 21293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 2541531,
          "cite": [
            "348 S.W.3d 919",
            "2011 Tex. Crim. App. LEXIS 912",
            "2011 WL 2555712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldarola v. Calabrese",
          "cluster_id": 7106428,
          "cite": [
            "298 F.3d 156",
            "2002 WL 1759778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldarola v. Calabrese",
          "cluster_id": 778515,
          "cite": [
            "298 F.3d 156",
            "2002 U.S. App. LEXIS 15339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony v. City of New York",
          "cluster_id": 8437661,
          "cite": [
            "339 F.3d 129",
            "2003 U.S. App. LEXIS 16279",
            "2003 WL 21864087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Urioste",
          "cluster_id": 2636842,
          "cite": [
            "52 P.3d 964",
            "132 N.M. 592",
            "2002 NMSC 023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kerman v. City of New York",
          "cluster_id": 7097772,
          "cite": [
            "261 F.3d 229",
            "2001 WL 845442"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
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
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Herman Patayan Soriano",
          "cluster_id": 785454,
          "cite": [
            "361 F.3d 494",
            "2003 U.S. App. LEXIS 27154",
            "2004 WL 439854"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wells",
          "cluster_id": 2575791,
          "cite": [
            "136 P.3d 810",
            "45 Cal. Rptr. 3d 8",
            "38 Cal. 4th 1078",
            "2006 Cal. Daily Op. Serv. 5529",
            "2006 Daily Journal DAR 8181",
            "2006 Cal. LEXIS 7815"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furr v. State",
          "cluster_id": 5447280,
          "cite": [
            "499 S.W.3d 872",
            "2016 Tex. Crim. App. LEXIS 1094",
            "2016 WL 5118607"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 01-7978(l)",
          "cluster_id": 783048,
          "cite": [
            "339 F.3d 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barros",
          "cluster_id": 6578377,
          "cite": [
            "435 Mass. 171",
            "755 N.E.2d 740",
            "2001 Mass. LEXIS 495"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellant-Cross-Appellee v. Vamond Elmore, Defendant-Appellee-Cross-Appellant",
          "cluster_id": 797353,
          "cite": [
            "482 F.3d 172",
            "2007 U.S. App. LEXIS 7354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Kerman v. The City of New York, Daniel Dilucia, William Crossan, John Hume, Thomas Loomis, Steve Kaminski, Mark Demarco, Andrew Oberfeldt, James Moran, Edward Joergens, \"John Doe\", \"Richard Roe\", \"Jane Doe\", (The Last Three Names Being Fictitious, Said Individuals Being Employees of the City of New York Who Participated in Taking Robert Kerman, Into Custody or in Dispatching Police Officers to Robert Kerman's Home or Operating the City's Emergency Medical Service 911 System as Set Forth in the Complaint)",
          "cluster_id": 774506,
          "cite": [
            "261 F.3d 229",
            "2001 U.S. App. LEXIS 16808"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mara v. Rilling",
          "cluster_id": 4608048,
          "cite": [
            "921 F.3d 48"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Boyea",
          "cluster_id": 1959712,
          "cite": [
            "765 A.2d 862",
            "171 Vt. 401",
            "2000 Vt. LEXIS 322"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. J.L.:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9184148 OR 9184150) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 173,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 13,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 173,
        "triage_read": 20,
        "triage_snippet_classified": 153
      },
      "lane2_top_cited": {
        "query": "cites:(9184148 OR 9184150)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MCZzPTIwMjIxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%289184148+OR+9184150%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(9184148 OR 9184150)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 0,
        "triage_snippet_classified": 27
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9184148 OR 9184150)",
    "indexed_citing_opinions": 272,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9184148,
        "count": 272,
        "count_source": "search"
      },
      {
        "opinion_id": 9184150,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1787,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-j-l.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMDM0NzEmcz05Mzg4MzMzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%289184148+OR+9184150%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T03:54:46Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:55:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:55:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:55:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. J.L.

```
<opinion type="majority">
<author id="b344-7">Justice Ginsburg</author>
<p id="Aqz">delivered the opinion of the Court.</p>
<p id="b344-8">The question presented in this case is whether an anonymous tip that a person is carrying a gun is, without more, sufficient to justify a police officer’s stop and frisk of that person. We hold that it is not.</p>
<p id="b344-3">I</p>
<p id="AoX">On October 13, 1995, an anonymous caller reported to the Miami-Dade Police that a young black male standing at a particular bus stop and wearing a plaid shirt was carrying a gun. App. to Pet. for Cert. A-40 to A-41. So far as the record reveals, there is no audio recording of the tip, and nothing is known about the informant. Sometime after the police received the tip — the record does not say how long— two officers were instructed to respond. They arrived at the bus stop about six minutes later and saw three black males “just hanging out [there].” <em>Id., </em>at A-42. One of the three, respondent J. L., was wearing a plaid shirt. <em>Id., </em>at A-41. Apart from the tip, the officers had.no reason tp suspect any of the three of illegal conduct. The officers did not see a firearm, and J. L. made no threatening or otherwise unusual movements. <em>Id., </em>at A-42 to A-44. One of the officers approached J. L., told him to put his hands up on the bus stop, frisked him, and seized a gun from J. L.’s pocket. The second officer frisked the other two individuals, against whom no allegations had been made, and found nothing.</p>
<p id="b345-6"><page-number citation-index="1" label="269">*269</page-number>J. L., who was at the time of the frisk “10 days shy of his 16th birth[dayj,” Tr. of Oral Arg. 6, was charged under state law with carrying a concealed firearm without a license and possessing a firearm while under the age of 18. He moved to suppress the gun as the fruit of an unlawful search, and the trial court granted his motion. The intermediate appellate court reversed, but the Supreme Court of Florida quashed that decision and held the search invalid under the Fourth Amendment. <span class="citation multiple-matches"><a href="/c/So.%202d/727/204/">727 So. 2d 204</a></span> (1998).</p>
<p id="b345-7">Anonymous tips, the Florida Supreme Court stated, are generally less reliable than tips from known informants and can form the basis for reasonable suspicion only'if accompanied by specific indicia of reliability, for example, the correct forecast of a subject’s “‘not easily predicted’” movements. <em>Id., </em>at 207 (quoting <em>Alabama </em>v. <em>White, </em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/#332" aria-description="Citation for case: Alabama v. White">496 U. S. 325, 332</a></span> (1990)), The tip leading to the frisk of J. L., the court observed, provided no such predictions, nor did it contain any other qualifying indicia of reliability. 727 So. 2d, at 207-208. Two justices dissented. The safety of the police and the public, they maintained, justifies a “firearm exception” to the general rule barring investigatory stops and frisks on the basis of bare-boned anonymous tips. <em>Id., </em>at 214-215.</p>
<p id="b345-8">Seeking review in this Court, the State of Florida noted that the decision of the State’s Supreme Court conflicts with decisions of other courts declaring similar searches compatible with the Fourth Amendment. See, <em>e. g., United States </em>v. <em>DeBerry, </em><span class="citation" data-id="9488902"><a href="/opinion/712960/united-states-v-anthony-deberry/#886" aria-description="Citation for case: United States v. Anthony Deberry">76 F. 3d 884, 886-887</a></span> (CA7 1996); <em>United States </em>v. <em>Clipper, </em><span class="citation" data-id="589955"><a href="/opinion/589955/united-states-v-ronald-t-clipper/#951" aria-description="Citation for case: United States v. Ronald T. Clipper">973 F. 2d 944, 951</a></span> (CADC 1992). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/963/">528 U. S. 963</a></span> (1999), and now affirm the judgment of the Florida Supreme Court.</p>
<p id="b345-9">HH</p>
<p id="b345-3">Our stop and frisk” decisions begin with <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). This Court held in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>:</em></p>
<blockquote id="b345-4">“[Wjhere a police officer observes unusual conduct which leads him reasonably to conclude in light of his <page-number citation-index="1" label="270">*270</page-number>experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others’ safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">Id., at 30</a></span>.</blockquote>
<p id="b346-5">In the instant case, the officers’ suspicion that J. L. was carrying a weapon arose not from any observations of their own but solely from a call made from an unknown location by an unknown caller. Unlike a tip from a known informant whose reputation can be assessed and who can be held responsible if her allegations turn out to be fabricated, see <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146-147</a></span> (1972), “an anonymous tip alone seldom demonstrates the informant’s basis of knowledge or veracity,” <em>Alabama </em>v. <em>White, </em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/#329" aria-description="Citation for case: Alabama v. White">496 U. S., at 329</a></span>. As we have recognized, however, there are situations in which an anonymous tip, suitably corroborated, exhibits “sufficient indicia of reliability to provide reasonable suspicion to make the investigatory stop.” <span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/#327" aria-description="Citation for case: Alabama v. White"><em>Id., </em>at 327</a></span>. The question we here confront is whether the tip pointing to J. L. had those indicia of reliability.</p>
<p id="b346-6">In <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span>, </em>the police received an anonymous tip asserting that a woman was carrying cocaine and predicting that she would leave an apartment building at a specified time, get into a car matching a particular description, and drive to a named motel. <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">Ibid.</a></span> </em>Standing alone, the tip would not have justified a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. <span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/#329" aria-description="Citation for case: Alabama v. White">496 U. S., at 329</a></span>. Only after police observation showed that the informant had accurately predicted the woman’s movements, we explained, did it become reasonable to think the tipster had inside knowledge about the suspect and therefore to credit his assertion about the cocaine. <page-number citation-index="1" label="271">*271</page-number>Id, at 332. Although the Court held that the suspicion in <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span> </em>became reasonable after police surveillance, we regarded the ease as borderline. Knowledge about a person’s future movements indicates some familiarity with that person’s affairs, but having such knowledge does not necessarily imply that the informant knows, in particular, whether that person is carrying hidden contraband. We accordingly classified <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span> </em>as a “close case.” <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">Ibid.</a></span></em></p>
<p id="b347-5">The tip in the instant case lacked the moderate indicia of reliability present in <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span> </em>and essential to the Court’s decision in that case. The anonymous call concerning J. L. provided no predictive information and therefore left the police without means to test the informant’s knowledge or credibility. That the allegation about the gun turned out to be correct does not suggest that the officers, prior to the frisks, had a reasonable basis for suspecting J. L. of engaging in unlawful conduct: The reasonableness of official suspicion must be measured by what the officers knew before they conducted their search. All the police had to go on in this case was the bare report of an unknown, unaccountable informant who neither explained how he knew about the gun nor supplied any basis for believing he had inside information about J. L. If <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span> </em>was a close case on the reliability of anonymous tips, this one surely falls on the other side of the line.</p>
<p id="b347-6">Florida contends that the tip was reliable because its description of the suspect’s visible attributes proved accurate: There really was a young black male wearing a plaid shirt at the bus stop. Brief for Petitioner 20-21. The United States as <em>amicus curiae </em>makes a similar argument, proposing that a stop and frisk should be permitted “when (1) an anonymous tip provides a description of a particular person at a particular location illegally carrying a concealed firearm, (2) police promptly verify the pertinent details of the tip except the existence of the firearm, and (3) there are no factors that cast doubt on the reliability of the tip ... Brief <page-number citation-index="1" label="272">*272</page-number>for United States 16. These contentions misapprehend the reliability needed for a tip to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop.</p>
<p id="b348-5">An accurate description of a subject’s readily observable location and appearance is of course reliable in this limited sense: It will help the police correctly identify the person whom the tipster means to accuse. Such a tip, however, does not show that the tipster has knowledge of concealed criminal activity. The reasonable suspicion here at issue requires that a tip be reliable in its assertion of illegality, not just in its tendency to identify a determinate person. Cf. 4 W. LaFave, Search and Seizure § 9.4(h), p. 213 (3d ed. 1996) (distinguishing reliability as to identification, which is often important in other criminal law contexts, from reliability as to the likelihood of criminal activity, which is central in anonymous-tip cases).</p>
<p id="b348-6">A second major argument advanced by Florida and the United States as <em>amicus </em>is, in essence, that the standard <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>analysis should be modified to license a “firearm exception.” Under such an exception, a tip alleging an illegal gun would justify a stop and frisk even if the accusation would fail standard pre-search reliability testing. We decline to adopt this position.</p>
<p id="b348-7">Firearms are dangerous, and extraordinary dangers sometimes justify unusual precautions. Our decisions recognize the serious threat that armed criminals pose to public safety; Terry’s rule, which permits protective police searches on the basis of reasonable suspicion rather than demanding that officers meet the higher standard of probable cause, responds to this very concern. See <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 30</a></span>. But an automatic firearm exception to our established reliability analysis would rove too far. Such an exception would enable any person seeking to harass another to set in motion an intrusive, embarrassing police search of the targeted person simply by placing an anonymous call falsely reporting the target’s unlawful carriage of a gun. Nor could one securely confine such an exception to allegations involving firearms.</p>
<p id="b349-4"><page-number citation-index="1" label="273">*273</page-number>Several Courts of Appeals have held it <em>per se </em>foreseeable for people carrying significant amounts of illegal drugs to be carrying guns as well. See, <em>e. g., United States </em>v. <em>Sakyi, </em><span class="citation" data-id="759135"><a href="/opinion/759135/united-states-v-collins-kusi-sakyi/#169" aria-description="Citation for case: United States v. Collins Kusi Sakyi">160 F. 3d 164, 169</a></span> (CA4 1998); <em>United States </em>v. <em>Dean, </em><span class="citation" data-id="699537"><a href="/opinion/699537/united-states-v-george-dean-james-earl-cofer-kenneth-dewayne-smith-and/#1490" aria-description="Citation for case: United States v. George Dean, James Earl Cofer, Kenneth...">59 F. 3d 1479, 1490, n. 20</a></span> (CA5 1995); <em>United States </em>v. <em>Odom, </em><span class="citation" data-id="9486298"><a href="/opinion/660214/united-states-v-gary-odom-92-582258235827-leonard-johnson-92-5824/#959" aria-description="Citation for case: United States v. Gary Odom (92-5822/5823/5827) Leonard...">13 F. 3d 949, 959</a></span> (CA6 1994); <em>United States </em>v. <em>Martinez, </em><span class="citation" data-id="578721"><a href="/opinion/578721/united-states-v-juan-ramon-martinez/#219" aria-description="Citation for case: United States v. Juan Ramon Martinez">958 F. 2d 217, 219</a></span> (CA8 1992). If police officers may properly conduct <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>frisks on the basis of bare-boned tips about guns, it would be reasonable to maintain under the above-cited decisions that the police should similarly have discretion to frisk based on bare-boned tips about narcotics. As we clarified when we made indicia of reliability critical in <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span> </em>and <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span>, </em>the Fourth Amendment is not so easily satisfied. Cf. <em>Richards </em>v. <em>Wisconsin, </em><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/#393" aria-description="Citation for case: Richards v. Wisconsin">520 U. S. 385, 393-394</a></span> (1997) (rejecting a <em>per se </em>exception to the “knock and announce” rule for narcotics cases partly because “the reasons for creating an exception in one category [of Fourth Amendment eases] can, relatively easily, be applied to others,” thus allowing the exception to swallow the rule).<footnotemark>*</footnotemark></p>
<p id="b349-5">The facts of this case do not require us to speculate about the circumstances under which the danger alleged in an anonymous tip might be so great as to justify a search even without a showing of reliability. We do not say, for example, that a report of a person carrying a bomb need bear the <page-number citation-index="1" label="274">*274</page-number>indicia of reliability we demand for a report of a person carrying a firearm before the police can constitutionally conduct a frisk. Nor do we hold that public safety officials in quarters where the reasonable expectation of Fourth Amendment privacy is diminished, such as airports, see <em>Florida </em>v. <em>Rodriguez, </em><span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1</a></span> (1984) <em>(per curiam), </em>and schools, see <em>New Jersey </em>v. <em>T L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985), cannot conduct protective searches on the basis of information insufficient to justify searches elsewhere.</p>
<p id="b350-5">Finally, the requirement that an anonymous tip bear standard indicia of reliability in order to justify a stop in no way diminishes a police officer’s prerogative, in accord with <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>to conduct a protective search of a person who has already been legitimately stopped. We speak in today’s decision only of cases in which the officer’s authority to make the initial stop is at issue. In that context, we hold that an anonymous tip lacking indicia of reliability of the kind contemplated in <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span> </em>and <em><span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">White</a></span> </em>does not justify a stop and frisk whenever and however it alleges the illegal possession of a firearm.</p>
<p id="b350-6">The judgment of the Florida Supreme Court is affirmed.</p>
<p id="b350-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b349-6">At oral argument, petitioner also advanced the position that J. L.’s youth made the stop and frisk valid, because it is a crime in Florida for persons under the age of 21 to carry concealed firearms. See <span class="citation no-link">Fla. Stat. § 790.01</span> (1997) (carrying a concealed weapon without a license is a misdemeanor), § 79Q.06(2)(b) (only persons aged 21 or older may be licensed to carry concealed weapons). This contention misses the mark. Even assuming that the arresting officers could be sure that J. L. was under 21, they would have had reasonable suspicion that J. L. was engaged in criminal activity only if they could be confident that he was carrying a gun in the first place. The mere fact that a tip, if true, would describe illegal activity does not mean that the police may make a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop without meeting the reliability requirement, and the fact that J. L. was under 21 in no way made the gun tip more reliable than if he had been an adult.</p>
</footnote>
</opinion>
```

---
