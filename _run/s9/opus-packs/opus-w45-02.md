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

## GROUP: content/cases/Kolender v. Lawson.md  (`case`, 6 assertions)

### content_page

```
---
title: "Kolender v. Lawson"
type: case
citation: "461 U.S. 352 (1983)"
parallel_cite: "103 S. Ct. 1855; 75 L. Ed. 2d 903; 51 U.S.L.W. 4532"
neutral_cite: 1983 U.S. LEXIS 159
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-05-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-05-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kolender v. Lawson
  varies_by_point: false
  scope_note: "Good law. A stop-and-identify statute requiring a suspect to provide 'credible and reliable' identification is void for vagueness (Fourteenth Amendment Due Process) because it gives police standardless discretion. Hiibel v. Sixth Judicial Dist. Court (2004) distinguished Kolender, upholding a narrower statute that required only that the suspect state his name."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110926/kolender-v-lawson/"
  cluster_id: 110926
  opinion_id: 9429183
  identity_checked: true
homes:
  - page: "[[Stop-and-Identify]]"
    role: "Key — statutory-vagueness limit"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Hiibel v. Sixth Judicial Dist. Court]]", "[[Brown v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "fourteenth-amendment", "stop-and-identify", "void-for-vagueness", "terry-stop"]
holding: "A stop-and-identify statute that requires a detained suspect to provide 'credible and reliable' identification is unconstitutionally vague, because it vests police with standardless discretion to decide what satisfies it."
lake:
  record_id: Kolender v. Lawson
  status: under_review
  projected_at: 2026-07-09
---

# Kolender v. Lawson

*461 U.S. 352 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Edward Lawson was detained or arrested about fifteen times under California Penal Code § 647(e), which made it a crime for a person who loiters or wanders the streets to refuse to provide "credible and reliable" identification and to account for his presence when asked by an officer who had reasonable suspicion sufficient to justify a *[[Terry v. Ohio|Terry]]* stop. As construed by the state courts, "credible and reliable" identification meant identification carrying reasonable assurance of authenticity and providing a means of later contacting the person. Lawson sued for a declaration that the statute was unconstitutional; the Ninth Circuit held it invalid, and the State appealed.

## Issue
Whether a stop-and-identify statute that requires a lawfully detained suspect to provide "credible and reliable" identification is unconstitutionally vague under the Due Process Clause.

## Rule
Yes. "We conclude that the statute as it has been construed is unconstitutionally vague within the meaning of the Due Process Clause of the Fourteenth Amendment by failing to clarify what is contemplated by the requirement that a suspect provide a 'credible and reliable' identification." — 461 U.S. at 353–354. ^pin-353

The governing standard targets standardless enforcement: "the void-for-vagueness doctrine requires that a penal statute define the criminal offense with sufficient definiteness that ordinary people can understand what conduct is prohibited and in a manner that does not encourage arbitrary and discriminatory enforcement." — [*Id.* at 357](https://www.courtlistener.com/opinion/110926/kolender-v-lawson/#:~:text=the%20void%2Dfor%2Dvagueness%20doctrine%20requires%20that). ^pin-357

Section 647(e) failed that test: it "contains no standard for determining what a suspect has to do in order to satisfy the requirement to provide a 'credible and reliable' identification. As such, the statute vests virtually complete discretion in the hands of the police to determine whether the suspect has satisfied the statute and must be permitted to go on his way in the absence of probable cause to arrest." — *Id.* at 358. ^pin-358

## Application
Neither the statute nor the state court's narrowing construction told a suspect what would actually satisfy the identification requirement — appellants conceded at argument that whether a jogger without ID complied could depend on the particular officer (reciting name and address might suffice, or the officer might demand answers about the suspect's route). Because compliance turned on whether the individual officer was "satisfied that the identification is reliable," the law left the decision to the officer's moment-to-moment judgment, inviting arbitrary and discriminatory enforcement. That standardless discretion is what rendered § 647(e) void for vagueness.

## Conclusion
Section 647(e) was unconstitutionally vague on its face, and the judgment invalidating it was affirmed. A stop-and-identify law cannot condition a citizen's freedom to walk away on an officer's unguided assessment of whether the identification offered is "credible and reliable."

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Kolender* pairs with [[Brown v. Texas]] (no detention to demand ID without reasonable suspicion). [[Hiibel v. Sixth Judicial Dist. Court]] (2004) distinguished *Kolender* and upheld a stop-and-identify statute that required only that a lawfully stopped suspect state his name — a definite, non-discretionary command that avoids the vagueness defect condemned here.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Kolender v. Lawson*, 461 U.S. 352 (1983) — https://www.courtlistener.com/opinion/110926/kolender-v-lawson/ — pinpoints: 353–354, 357, 358.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ff09cb4c36e3c33d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "461 U.S. 352 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 159", "official_citation_present": true, "parallel_cite": "103 S. Ct. 1855; 75 L. Ed. 2d 903; 51 U.S.L.W. 4532", "title": "Kolender v. Lawson", "year": "1983"}}
{"assertion_id": "5edefaee91c13522", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A stop-and-identify statute that requires a detained suspect to provide 'credible and reliable' identification is unconstitutionally vague, because it vests police with standardless discretion to decide what satisfies it.", "title": "Kolender v. Lawson"}}
{"assertion_id": "a8f4e9fd4dee87d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Kolender v. Lawson"}}
{"assertion_id": "fff3c91d2d636a25", "dimension": "support", "kind": "home_role", "locator": {"home": "Stop-and-Identify"}, "payload": {"home": "Stop-and-Identify", "role": "Key — statutory-vagueness limit", "title": "Kolender v. Lawson"}}
{"assertion_id": "1d0045042243a137", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1983-05-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kolender v. Lawson", "field_i_validity": "good_law", "scope_note": "Good law. A stop-and-identify statute requiring a suspect to provide 'credible and reliable' identification is void for vagueness (Fourteenth Amendment Due Process) because it gives police standardless discretion. Hiibel v. Sixth Judicial Dist. Court (2004) distinguished Kolender, upholding a narrower statute that required only that the suspect state his name.", "title": "Kolender v. Lawson", "varies_by_point": "false"}}
{"assertion_id": "3224fbdebe976c79", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kolender v. Lawson"}}
```

### lake record — Kolender v. Lawson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kolender v. Lawson",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Kolender v. Lawson",
    "case_name_short": "Kolender",
    "case_name_full": "KOLENDER, CHIEF OF POLICE OF SAN DIEGO, Et Al. v. LAWSON",
    "input_case_name": "Kolender v. Lawson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-05-02",
    "year": 1983,
    "docket": null,
    "cluster_id": 110926,
    "lead_opinion_id": 9429183,
    "sibling_ids": [
      110926,
      9429183,
      9429184,
      9429185
    ],
    "absolute_url": "/opinion/110926/kolender-v-lawson/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "461 U.S. 352",
      "volume": "461",
      "reporter": "U.S.",
      "page": "352",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 1855",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1855",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 903",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "903",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4532",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4532",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 159",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "461 U.S. 352",
        "volume": "461",
        "reporter": "U.S.",
        "page": "352",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 1855",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "1855",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 L. Ed. 2d 903",
        "volume": "75",
        "reporter": "L. Ed. 2d",
        "page": "903",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 159",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "159",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4532",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4532",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "461 U.S. 352",
    "official_selection": {
      "court_class": "scotus",
      "selected": "461 U.S. 352",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-353",
      "page": null,
      "quote": "identification is unconstitutionally vague under the Due Process Clause. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-357",
      "page": null,
      "quote": "the void-for-vagueness doctrine requires that a penal statute define the criminal offense with sufficient definiteness that ordinary people can understand what conduct is prohibited and in a manner that does not encourage arbitrary and discriminatory enforcement.",
      "star_marker": "357",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6679,
      "fragment": "#:~:text=the%20void%2Dfor%2Dvagueness%20doctrine%20requires%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-358",
      "page": null,
      "quote": "contains no standard for determining what a suspect has to do in order to satisfy the requirement to provide a 'credible and reliable' identification. As such, the statute vests virtually complete discretion in the hands of the police to determine whether the suspect has satisfied the statute and must be permitted to go on his way in the absence of probable cause to arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-05-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kolender v. Lawson",
    "varies_by_point": false,
    "scope_note": "Good law. A stop-and-identify statute requiring a suspect to provide 'credible and reliable' identification is void for vagueness (Fourteenth Amendment Due Process) because it gives police standardless discretion. Hiibel v. Sixth Judicial Dist. Court (2004) distinguished Kolender, upholding a narrower statute that required only that the suspect state his name.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Manning v. Caldwell for City of Roanoke",
          "cluster_id": 4639944,
          "cite": [
            "930 F.3d 264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Demott",
          "cluster_id": 8443719,
          "cite": [
            "906 F.3d 231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dianna Helmers v. City of Des Moines",
          "cluster_id": 4483928,
          "cite": [
            "918 N.W.2d 501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane1_negative"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 2812210,
          "cite": [
            "576 U.S. 591",
            "135 S. Ct. 2551",
            "192 L. Ed. 2d 569",
            "2015 U.S. LEXIS 4251",
            "83 U.S.L.W. 4576",
            "25 Fla. L. Weekly Fed. S 459"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pruitt v. Mote",
          "cluster_id": 1218369,
          "cite": [
            "503 F.3d 647",
            "2007 U.S. App. LEXIS 23109",
            "2007 WL 2850448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 4632235,
          "cite": [
            "588 U.S. 445",
            "139 S. Ct. 2319",
            "2019 U.S. LEXIS 4210",
            "204 L. Ed. 2d 757"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "R. A. v. v. City of St. Paul",
          "cluster_id": 112774,
          "cite": [
            "120 L. Ed. 2d 305",
            "112 S. Ct. 2538",
            "505 U.S. 377",
            "1992 U.S. LEXIS 3863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. United States Jaycees",
          "cluster_id": 111255,
          "cite": [
            "82 L. Ed. 2d 462",
            "104 S. Ct. 3244",
            "468 U.S. 609",
            "1984 U.S. LEXIS 146",
            "52 U.S.L.W. 5076"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Isassi v. State",
          "cluster_id": 2280007,
          "cite": [
            "330 S.W.3d 633",
            "2010 Tex. Crim. App. LEXIS 1641",
            "2010 WL 3894792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Houston v. Hill",
          "cluster_id": 111919,
          "cite": [
            "96 L. Ed. 2d 398",
            "107 S. Ct. 2502",
            "482 U.S. 451",
            "1987 U.S. LEXIS 2617",
            "55 U.S.L.W. 4823"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pacific Mutual Life Insurance v. Haslip",
          "cluster_id": 112557,
          "cite": [
            "113 L. Ed. 2d 1",
            "111 S. Ct. 1032",
            "499 U.S. 1",
            "1991 U.S. LEXIS 1306",
            "59 U.S.L.W. 4157",
            "18 Media L. Rep. (BNA) 1753",
            "91 Daily Journal DAR 2599",
            "91 Cal. Daily Op. Serv. 1626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. Colorado",
          "cluster_id": 118385,
          "cite": [
            "147 L. Ed. 2d 597",
            "120 S. Ct. 2480",
            "530 U.S. 703",
            "2000 U.S. LEXIS 4486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Chicago v. Morales",
          "cluster_id": 118299,
          "cite": [
            "144 L. Ed. 2d 67",
            "119 S. Ct. 1849",
            "527 U.S. 41",
            "1999 U.S. LEXIS 4005"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James v. United States",
          "cluster_id": 145743,
          "cite": [
            "167 L. Ed. 2d 532",
            "127 S. Ct. 1586",
            "550 U.S. 192",
            "2007 U.S. LEXIS 4337"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boos v. Barry",
          "cluster_id": 112027,
          "cite": [
            "99 L. Ed. 2d 333",
            "108 S. Ct. 1157",
            "485 U.S. 312",
            "1988 U.S. LEXIS 1445"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Secretary of State of Md. v. Joseph H. Munson Co.",
          "cluster_id": 111226,
          "cite": [
            "81 L. Ed. 2d 786",
            "104 S. Ct. 2839",
            "467 U.S. 947",
            "1984 U.S. LEXIS 123",
            "52 U.S.L.W. 4875"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skilling v. United States",
          "cluster_id": 149286,
          "cite": [
            "561 U.S. 358",
            "130 S. Ct. 2896",
            "177 L. Ed. 2d 619",
            "2010 U.S. LEXIS 5259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sessions v. Dimaya",
          "cluster_id": 4487345,
          "cite": [
            "584 U.S. 148",
            "138 S. Ct. 1204",
            "200 L. Ed. 2d 549",
            "2018 U.S. LEXIS 2497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Osborne v. Ohio",
          "cluster_id": 112417,
          "cite": [
            "109 L. Ed. 2d 98",
            "110 S. Ct. 1691",
            "495 U.S. 103",
            "1990 U.S. LEXIS 2036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
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
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clark v. Martinez",
          "cluster_id": 137741,
          "cite": [
            "160 L. Ed. 2d 734",
            "125 S. Ct. 716",
            "543 U.S. 371",
            "2005 U.S. LEXIS 627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kolender v. Lawson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTIxMDcyMDAwMDAwJnM9NDQ3NzkwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Nzgmcz0xNzIxOTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
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
    "complete_query": "cites:(110926 OR 9429183 OR 9429184 OR 9429185)",
    "indexed_citing_opinions": 2222,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110926,
        "count": 1927,
        "count_source": "search"
      },
      {
        "opinion_id": 9429183,
        "count": 345,
        "count_source": "search"
      },
      {
        "opinion_id": 9429184,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429185,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3308,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kolender-v-lawson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzOTA5OTYmcz0xMDYwMTgzOSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110926+OR+9429183+OR+9429184+OR+9429185%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110926,
        "cited_id": 89266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 91256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 96198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 100759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 103347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 104453,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 104532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 105716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 106884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 108988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 109966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 280147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 393990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 2138359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110926,
        "cited_id": 2169575,
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
    "date_created": "2026-07-05T10:24:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:29:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:26:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kolender v. Lawson

```
<opinion type="majority">
<author id="b411-6">Justice O’Connor</author>
<p id="ABn">delivered the opinion of the Court.</p>
<p id="b411-7">This appeal presents a facial challenge to a criminal statute that requires persons who loiter or wander on the streets to provide a “credible and reliable” identification and to account for their presence when requested by a peace officer under circumstances that would justify a stop under the standards of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968).<footnotemark>1</footnotemark> We conclude that the statute as it has been construed is unconstitutionally vague within the meaning of the Due Process Clause of the Fourteenth Amendment by failing to clarify what is contemplated <page-number citation-index="1" label="354">*354</page-number><em>by the requirement that a suspect provide a "credible and reliable" identification. Accordingly, we affirm the judgment of the court below.</em></p>
<p id="b412-5">
<em>I</em>
</p>
<p id="b412-6">
<em>Appellee Edward Lawson was detained or arrested on approximately 15 occasions between March 1975 and January 1977 pursuant to Cal. Penal Code Ann. § 647(e) (West 1970).</em>
<footnotemark>
<em>2</em>
</footnotemark>
<em> Lawson was prosecuted only twice, and was convicted once. The second charge was dismissed.</em>
</p>
<p id="b412-7">
<em>Lawson then brought a civil action in the District Court for the Southern District of California seeking a declaratory judgment that § 647(e) is unconstitutional, a mandatory injunction to restrain enforcement of the statute, and compensatory and punitive damages against the various officers who detained him. The District Court found that § 647(e) was overbroad because "a person who is stopped on less than probable cause cannot be punished for failing to identify himself." App. to Juris. Statement A-78. The District Court enjoined enforcement of the statute, but held that Lawson could not recover damages because the officers involved acted in the good-faith belief that each detention or arrest was lawful.</em>
</p>
<p id="b412-8"><em>Appellant H. A. Porazzo, Deputy Chief Commander of the California Highway Patrol, appealed the District Court decision to the Court of Appeals for the Ninth Circuit. Lawson </em><page-number citation-index="1" label="355">*355</page-number>cross-appealed, arguing that he was entitled to a jury trial on the issue of damages against the officers. The Court of Appeals affirmed the District Court determination as to the unconstitutionality of § 647(e). <span class="citation multiple-matches"><a href="/c/F.%202d/658/1362/">658 F. 2d 1362</a></span> (1981). The appellate court determined that the statute was unconstitutional in that it violates the Fourth Amendment’s proscription against unreasonable searches and seizures, it contains a vague enforcement standard that is susceptible to arbitrary enforcement, and it fails to give fair and adequate notice of the type of conduct prohibited. Finally, the Court of Appeals reversed the District Court as to its holding that Lawson was not entitled to a jury trial to determine the good faith of the officers in his damages action against them, and remanded the case to the District Court for trial.</p>
<p id="b413-5">The officers appealed to this Court from that portion of the judgment of the Court of Appeals which declared § 647(e) unconstitutional and which enjoined its enforcement. We noted probable jurisdiction pursuant to <span class="citation no-link">28 U. S. C. § 1254</span>(2). <span class="citation multiple-matches"><a href="/c/U.%20S./455/999/">455 U. S. 999</a></span> (1982).</p>
<p id="b413-6">II</p>
<p id="b413-7">In the courts below, Lawson mounted an attack on the facial validity of § 647(e).<footnotemark>3</footnotemark> “In evaluating a facial challenge to a state law, a federal court must, of course, consider any limiting construction that a state court or enforcement agency has proffered.” <em>Hoffman Estates </em>v. <em>Flipside, Hoffman Estates, Inc., </em><span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/#494" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">455 U. S. 489, 494, n. 5</a></span> (1982). As construed by the California Court of Appeal,<footnotemark>4</footnotemark> § 647(e) requires that an in<page-number citation-index="1" label="356">*356</page-number>dividual provide “credible and reliable” identification when requested by a police officer who has reasonable suspicion of criminal activity sufficient to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>detention.<footnotemark>5</footnotemark> <em>People </em>v. <em>Solomon, </em><span class="citation no-link">83 Cal. App. 3d 429</span>, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr. 867</a></span> <page-number citation-index="1" label="357">*357</page-number>(1973). “Credible and reliable” identification is defined by the State Court of Appeal as identification “carrying reasonable assurance that the identification is authentic and providing means for later getting in touch with the person who has identified himself.” <em>Id., </em>at 438, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#873" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr., at 873</a></span>. In addition, a suspect may be required to <em>“account for his presence </em>... to the extent that it assists in producing credible and reliable identification . . . .” <em>Id., at </em>438, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#872" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr., at 872</a></span>. Under the terms of the statute, failure of the individual to provide “credible and reliable” identification permits the arrest.<footnotemark>6</footnotemark></p>
<p id="b415-5">III</p>
<p id="b415-6">Our Constitution is designed to maximize individual freedoms within a framework of ordered liberty. Statutory limitations on those freedoms are examined for substantive authority and content as well as for definiteness or certainty of expression. See generally M. Bassiouni, Substantive Criminal Law 53 (1978).</p>
<p id="b415-7">As generally stated, the void-for-vagueness doctrine requires that a penal statute define the criminal offense with sufficient definiteness that ordinary people can understand what conduct is prohibited and in a manner that does not encourage arbitrary and discriminatory enforcement. <em>Hoffman Estates </em>v. <em>Flipside, Hoffman Estates, <span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">Inc., supra;</a></span> Smith </em>v. <em>Goguen, </em><span class="citation" data-id="9425639"><a href="/opinion/108988/smith-v-goguen/" aria-description="Citation for case: Smith v. Goguen">415 U. S. 566</a></span> (1974); <em>Grayned </em>v. <em>City of Rockford, </em><span class="citation" data-id="8980926"><a href="/opinion/8988822/grayned-v-city-of-rockford/" aria-description="Citation for case: Grayned v. City of Rockford">408 U. S. 104</a></span> (1972); <em>Papachristou </em>v. <em>City of Jacksonville, </em><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S. 156</a></span> (1972); <em>Connally </em>v. <em>General Construction Co., </em><span class="citation" data-id="100759"><a href="/opinion/100759/connally-v-general-construction-co/" aria-description="Citation for case: Connally v. General Construction Co.">269 U. S. 385</a></span> (1926). Although the doctrine focuses <page-number citation-index="1" label="358">*358</page-number>both on actual notice to citizens and arbitrary enforcement, we have recognized recently that the more important aspect of the vagueness doctrine “is not actual notice, but the other principal element of the doctrine — the requirement that a legislature establish minimal guidelines to govern law enforcement.” <em>Smith, </em><span class="citation" data-id="9425639"><a href="/opinion/108988/smith-v-goguen/#574" aria-description="Citation for case: Smith v. Goguen">415 U. S., at 574</a></span>. Where the legislature fails to provide such minimal guidelines, a criminal statute may permit “a standardless sweep [that] allows policemen, prosecutors, and juries to pursue their personal predilections.” 7d., at 575.<footnotemark>7</footnotemark></p>
<p id="b416-5">Section 647(e), as presently drafted and as construed by the state courts, contains no standard for determining what a suspect has to do in order to satisfy the requirement to provide a “credible and reliable” identification. As such, the statute vests virtually complete discretion in the hands of the police to determine whether the suspect has satisfied the statute and must be permitted to go on his way in the absence of probable cause to arrest. An individual, whom police may think is suspicious but do not have probable cause to believe has committed a crime, is entitled to continue to walk the public streets “only at the whim of any police officer” who happens to stop that individual under § 647(e). <em>Shuttlesworth </em>v. <em>City of Birmingham, </em><span class="citation" data-id="9423099"><a href="/opinion/107111/shuttlesworth-v-city-of-birmingham/#90" aria-description="Citation for case: Shuttlesworth v. City of Birmingham">382 U. S. 87, 90</a></span> (1965). Our concern here is based upon the “potential for arbitrarily suppressing First Amendment liberties . . . .” <span class="citation" data-id="9423099"><a href="/opinion/107111/shuttlesworth-v-city-of-birmingham/#91" aria-description="Citation for case: Shuttlesworth v. City of Birmingham"><em>Id., </em>at 91</a></span>. In addition, § 647(e) implicates consideration of the constitutional right to freedom of movement. See <em>Kent </em>v. <em>Dulles, </em><span class="citation" data-id="9421652"><a href="/opinion/105716/kent-v-dulles/#126" aria-description="Citation for case: Kent v. Dulles">357 U. S. 116, 126</a></span> (1958); <em>Aptheker </em>v. <em>Secretary of State, </em><span class="citation" data-id="9422871"><a href="/opinion/106884/aptheker-v-secretary-of-state/#505" aria-description="Citation for case: Aptheker v. Secretary of State">378 U. S. 500, 505-506</a></span> (1964).<footnotemark>8</footnotemark></p>
<p id="b417-4"><page-number citation-index="1" label="359">*359</page-number>Section 647(e) is not simply a “stop-and-identify” statute. Rather, the statute requires that the individual provide a “credible and reliable” identification that carries a “reasonable assurance” of its authenticity, and that provides “means for later getting in touch with the person who has identified himself.” <em>Solomon, </em><span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#438" aria-description="Citation for case: People v. Solomon">33 Cal. App. 3d, at 438</a></span>, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#872" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr., at 872-873</a></span>. In addition, the suspect may also have to account for his presence “to the extent it assists in producing <page-number citation-index="1" label="360">*360</page-number>credible and reliable identification.” <em>Id., </em>at 438, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#872" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr., at 872</a></span>.</p>
<p id="b418-5">At oral argument, the appellants confirmed that a suspect violates § 647(e) unless “the officer [is] satisfied that the identification is reliable.” Tr. of Oral Arg. 6. In giving examples of how suspects would satisfy the requirement, appellants explained that a jogger, who was not carrying identification, could, depending on the particular officer, be required to answer a series of questions concerning the route that he followed to arrive at the place where the officers detained him,<footnotemark>9</footnotemark> or .could satisfy the identification requirement simply by reciting his name and address. See <em>id., </em>at 6-10.</p>
<p id="b418-6">It is clear that the full discretion accorded to the police to determine whether the suspect has provided a “credible and reliable” identification necessarily “entrusts] lawmaking ‘to the moment-to-moment judgment of the policeman on his beat.’” <em><span class="citation" data-id="9425639"><a href="/opinion/108988/smith-v-goguen/" aria-description="Citation for case: Smith v. Goguen">Smith, supra,</a></span> </em>at 575 (quoting <em>Gregory </em>v. <em>Chicago, </em><span class="citation" data-id="9423936"><a href="/opinion/107869/gregory-v-city-of-chicago/#120" aria-description="Citation for case: Gregory v. City of Chicago">394 U. S. 111, 120</a></span> (1969) (Black, J., concurring)). Section 647(e) “furnishes a convenient tool for ‘harsh and discriminatory enforcement by local prosecuting officials, against particular groups deemed to merit their displeasure/” <em>Papachristou, </em><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S., at 170</a></span> (quoting <em>Thornhill </em>v. <em>Alabama, </em><span class="citation" data-id="103347"><a href="/opinion/103347/thornhill-v-alabama/#97" aria-description="Citation for case: Thornhill v. Alabama">310 U. S. 88, 97-98</a></span> (1940)), and “confers on police a virtually unrestrained power to arrest and charge persons with a violation.” <em>Lewis </em>v. <em>City of New Orleans, </em><span class="citation" data-id="9425601"><a href="/opinion/108965/lewis-v-city-of-new-orleans/#135" aria-description="Citation for case: Lewis v. City of New Orleans">415 U. S. 130, 135</a></span> (1974) (Powell, J., concurring in result). In providing that a detention under § 647(e) may occur only where there is the level of suspicion sufficient to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop, the State ensures the existence of “neutral limitations on the conduct of individual officers.” <em>Brown </em>v. <em>Texas, </em>443 <page-number citation-index="1" label="361">*361</page-number>U. S., at 51. Although the initial detention is justified, the State fails to establish standards by which the officers may determine whether the suspect has complied with the subsequent identification requirement.</p>
<p id="b419-5">Appellants stress the need for strengthened law enforcement tools to combat the epidemic of crime that plagues our Nation. The concern of our citizens with curbing criminal activity is certainly a matter requiring the attention of all branches of government. As weighty as this concern is, however, it cannot justify legislation that would otherwise fail to meet constitutional standards for definiteness and clarity. See <em>Lanzetta </em>v. <em>New Jersey, </em><span class="citation" data-id="103170"><a href="/opinion/103170/lanzetta-v-new-jersey/" aria-description="Citation for case: Lanzetta v. New Jersey">306 U. S. 451</a></span> (1939). Section 647(e), as presently construed, requires that “suspicious” persons satisfy some undefined identification requirement, or face criminal punishment. Although due process does not require “impossible standards” of clarity, see <em>United States </em>v. <em>Petrillo, </em><span class="citation" data-id="9420030"><a href="/opinion/104453/united-states-v-petrillo/#7" aria-description="Citation for case: United States v. Petrillo">332 U. S. 1, 7-8</a></span> (1947), this is not a case where further precision in the statutory language is either impossible or impractical.</p>
<p id="b419-6">IV</p>
<p id="b419-7">We conclude § 647(e) is unconstitutionally vague on its face because it encourages arbitrary enforcement by failing to describe with sufficient particularity what a suspect must do in order to satisfy the statute.<footnotemark>10</footnotemark> Accordingly, the judgment of <page-number citation-index="1" label="362">*362</page-number><em>the </em>Court of Appeals is affirmed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b420-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b411-11"> California Penal Code Ann. § 647(e) (West 1970) provides:</p>
<blockquote id="b411-12">“Every person who commits any of the following acts is guilty of disorderly conduct, a misdemeanor: . . . (e) Who loiters or wanders upon the streets or from place to place without apparent reason or business and who refuses to identify himself and to account for his presence when requested by any peace officer so to do, if the surrounding circumstances are such as to indicate to a reasonable man that the public safety demands such identification.”</blockquote>
</footnote>
<footnote label="2">
<p id="b412-9"><em> District Court failed to find facts concerning the particular occasions on which Lawson was detained or arrested under § 647(e). However, the trial transcript contains numerous descriptions of the stops given both by Lawson and by the police officers who detained him. For example, one police officer testified that he stopped Lawson while walking on an otherwise vacant street because it was late at night, the area was isolated, and the area was located close to a high crime area. Tr. 266-267. Another officer testified that he detained Lawson, who was walking at a late hour in a business area where some businesses were still open, and asked for identification because burglaries had been committed by unknown persons in the general area. Id., at 207. The appellee states that he has never been stopped by police for any reason apart from his detentions under § </em>647(e).</p>
</footnote>
<footnote label="3">
<p id="b413-8"> The appellants have apparently never challenged the propriety of declaratory and injunctive relief in this ease. See <em>Steffel </em>v. <em>Thompson, </em><span class="citation" data-id="9425630"><a href="/opinion/108985/steffel-v-thompson/" aria-description="Citation for case: Steffel v. Thompson">415 U. S. 452</a></span> (1974). Nor have appellants ever challenged Lawson’s standing to seek such relief. We note that Lawson has been stopped on approximately 15 occasions pursuant to § 647(e), and that these 15 stops occurred in a period of less than two years. Thus, there is a “credible threat” that Lawson might be detained again under § 647(e). See <em>Ellis </em>v. <em>Dyson, </em><span class="citation" data-id="9426080"><a href="/opinion/109253/ellis-v-dyson/#434" aria-description="Citation for case: Ellis v. Dyson">421 U. S. 426, 434</a></span> (1975).</p>
</footnote>
<footnote label="4">
<p id="b413-9"> In <em>Wainwright </em>v. <em>Stone, </em><span class="citation" data-id="108876"><a href="/opinion/108876/wainwright-v-stone/#22" aria-description="Citation for case: Wainwright v. Stone">414 U. S. 21, 22-23</a></span> (1973), we held that “[f]or the purpose of determining whether a state statute is too vague and indefi<page-number citation-index="1" label="356">*356</page-number>nite to constitute valid legislation ‘we must take the statute as though it read precisely as the highest court of the State has interpreted it.’ <em>Minnesota ex rel. Pearson </em>v. <em>Probate Court, </em><span class="citation" data-id="103305"><a href="/opinion/103305/minnesota-ex-rel-pearson-v-probate-court-of-ramsey-county/#273" aria-description="Citation for case: Minnesota Ex Rel. Pearson v. Probate Court of Ramsey County">309 U. S. 270, 273</a></span> (1940).” The Court of Appeals for the Ninth Circuit noted in its decision that the state intermediate appellate court has construed the statute in <em>People </em>v. <em>Solomon, </em><span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/" aria-description="Citation for case: People v. Solomon">33 Cal. App. 3d 429</a></span>, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr. 867</a></span> (1973), that the State Supreme Court has refused review, and that <em>Solomon </em>has been the law of California for nine years. In these circumstances, we agree with the Ninth Circuit that the <em>Solomon </em>opinion is authoritative for purposes of defining the meaning of § 647(e). See <span class="citation multiple-matches"><a href="/c/F.%202d/658/1362/">658 F. 2d 1362</a></span>, 1364-1365, n. 3 (1981).</p>
</footnote>
<footnote label="5">
<p id="b414-6"> The <em>Solomon </em>court apparently read <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to hold that the test for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>detention was whether the officer had information that would lead a reasonable man to believe that the intrusion was appropriate. The Ninth Circuit noted that according to <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the applicable test under the Fourth Amendment requires that the police officer making a detention “be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span>. The Ninth Circuit then held that although what <em>Solomon </em>articulated as the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>standard differed from what <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>actually held, “[w]e believe that the <em>Solomon </em>court meant to incorporate in principle the standards enunciated in <em>Terry.” </em>658 F. 2d, at 1366, n. 8. We agree with that interpretation of <em>Solomon. </em>Of course, if the <em>Solomon </em>court misread <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>and interpreted § 647(e) to permit investigative detentions in situations where the officers lack a reasonable suspicion of criminal activity based on objective facts, Fourth Amendment concerns would be implicated. See <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979).</p>
<p id="b414-7">In addition, the <em>Solomon </em>court appeared to believe that both the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>detention <em>and </em>frisk were proper under the standard for <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>detentions, and since the frisk was more intrusive than the request for identification, the request for identification <em>must </em>be proper under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>See <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#435" aria-description="Citation for case: People v. Solomon">33 Cal. App. 3d, at 435</a></span>, <span class="citation" data-id="2138359"><a href="/opinion/2138359/people-v-solomon/#870" aria-description="Citation for case: People v. Solomon">108 Cal. Rptr., at 870-871</a></span>. The Ninth Circuit observed that the <em>Solomon </em>analysis was “slightly askew.” 658 F. 2d, at 1366, n. 9. The court reasoned that under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>the frisk, as opposed to the detention, is proper only if the detaining officer reasonably believes that the suspect may be armed and dangerous, in addition to having an articulable suspicion that criminal activity is afoot.</p>
</footnote>
<footnote label="6">
<p id="b415-8"> In <em>People </em>v. <em>Caylor, </em><span class="citation" data-id="2169575"><a href="/opinion/2169575/people-v-caylor/#56" aria-description="Citation for case: People v. Caylor">6 Cal. App. 3d 51, 56</a></span>, <span class="citation" data-id="2169575"><a href="/opinion/2169575/people-v-caylor/#501" aria-description="Citation for case: People v. Caylor">85 Cal. Rptr. 497, 501</a></span> (1970), the court suggested that the State must prove that a suspect detained under § 647(e) was loitering or wandering for “evil purposes.” However, in <em>Solomon, </em>which the court below and the parties concede is “authoritative” in the absence of a California Supreme Court decision on the issue, there is no discussion of any requirement that the State prove “evil purposes.”</p>
</footnote>
<footnote label="7">
<p id="b416-6"> Our concern for minimal guidelines finds its roots as far back as our decision in <em>United States </em>v. <em>Reese, </em><span class="citation" data-id="9417037"><a href="/opinion/89266/united-states-v-reese/#221" aria-description="Citation for case: United States v. REESE">92 U. S. 214, 221</a></span> (1876):</p>
<blockquote id="b416-7">“It would certainly be dangerous if the legislature could set a net large enough to catch all possible offenders, and leave it to the courts to step inside and say who could be rightfully detained, and who should be set at large. This would, to some extent, substitute the judicial for the legislative department of government.”</blockquote>
</footnote>
<footnote label="8">
<p id="b416-8"> In his dissent, Justice White claims that “[t]he upshot of our cases ... is that whether or not a statute purports to regulate constitutionally <page-number citation-index="1" label="359">*359</page-number>protected conduct, it should not be held unconstitutionally vague on its face unless it is vague in all of its possible applications.” <em>Post, </em>at 370. The description of our holdings is inaccurate in several respects. First, it neglects the fact that we permit a facial challenge if a law reaches “a substantial amount of constitutionally protected conduct.” <em>Hoffman Estates </em>v. <em>Flipside, Hoffman Estates, Inc., </em><span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/#494" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">455 U. S. 489, 494</a></span> (1982). Second, where a statute imposes criminal penalties, the standard of certainty is higher. See <em>Winters </em>v. <em>New York, </em><span class="citation" data-id="9420132"><a href="/opinion/104532/winters-v-new-york/#515" aria-description="Citation for case: Winters v. New York">333 U. S. 507, 515</a></span> (1948). This concern has, at times, led us to invalidate a criminal statute on its face even when it could conceivably have had some valid application. See, <em>e. g., Colautti </em>v. <em>Franklin, </em><span class="citation" data-id="9427408"><a href="/opinion/109966/colautti-v-franklin/#394" aria-description="Citation for case: Colautti v. Franklin">439 U. S. 379, 394-401</a></span> (1979); <em>Lanzetta </em>v. <em>New Jersey, </em><span class="citation" data-id="103170"><a href="/opinion/103170/lanzetta-v-new-jersey/" aria-description="Citation for case: Lanzetta v. New Jersey">306 U. S. 451</a></span> (1939). The dissent concedes that “the overbreadth doctrine permits facial challenge of a law that reaches a substantial amount of conduct protected by the First Amendment. . ..” <em>Post, </em>at 371. However, in the dissent’s view, one may not “confuse vagueness and over-breadth by attacking the enactment as being vague as applied to conduct other than his own.” <em>Post, </em>at 370. But we have traditionally viewed vagueness and overbreadth as logically related and similar doctrines. See, <em>e. g., Keyishian </em>v. <em>Board of Regents, </em><span class="citation" data-id="9423328"><a href="/opinion/107343/keyishian-v-board-of-regents-of-univ-of-state-of-ny/#609" aria-description="Citation for case: Keyishian v. Board of Regents of Univ. of State of NY">385 U. S. 589, 609</a></span> (1967); <em>NAACP </em>v. <em>Button, </em><span class="citation" data-id="9422512"><a href="/opinion/106514/national-assn-for-the-advancement-of-colored-people-v-button/#433" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">371 U. S. 415, 433</a></span> (1963). See also Note, The Void-for-Vagueness Doctrine in the Supreme Court, <span class="citation no-link">109 U. Pa. L. Rev. 67</span>, 110-113 (1960).</p>
<p id="b417-6">No authority cited by the dissent supports its argument about facial challenges in the arbitrary enforcement context. The dissent relies heavily on <em>Parker </em>v. <em>Levy, </em><span class="citation" data-id="9425778"><a href="/opinion/109077/parker-v-levy/" aria-description="Citation for case: Parker v. Levy">417 U. S. 733</a></span> (1974), but in that ease we deliberately applied a less stringent vagueness analysis “[bjecause of the factors differentiating military society from civilian society.” <span class="citation" data-id="9425778"><a href="/opinion/109077/parker-v-levy/#756" aria-description="Citation for case: Parker v. Levy"><em>Id., </em>at 756</a></span>. <em>Hoffman <span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">Estates, supra,</a></span> </em>also relied upon by the dissent, does not support its position. In addition to reaffirming the validity of facial challenges in situations where free speech or free association are affected, see <span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/#494" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">455 U. S., at 494, 495, 498-499</a></span>, the Court emphasized that the ordinance in <em><span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc.">Hoffman Estates</a></span> </em>“simply regulates business behavior” and that “economic regulation is subject to a less strict vagueness test because its subject matter is often more narrow.” <span class="citation" data-id="9428688"><a href="/opinion/110661/hoffman-estates-v-flipside-hoffman-estates-inc/#499" aria-description="Citation for case: Hoffman Estates v. Flipside, Hoffman Estates, Inc."><em>Id., </em>at 499, 498</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b418-7"> To the extent that § 647(e) criminalizes a suspect’s failure to answer such questions put to him by police officers, Fifth Amendment concerns are implicated. It is a “settled principle that while the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes they have no right to compel them to answer.” <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 727, n. 6</a></span> (1969).</p>
</footnote>
<footnote label="10">
<p id="b419-8"> Because we affirm the judgment of the court below on this ground, we find it unnecessary to decide the other questions raised by the parties because our resolution of these other issues would decide constitutional questions in advance of the necessity of doing so. See <em>Burton </em>v. <em>United States, </em><span class="citation" data-id="9417974"><a href="/opinion/96198/burton-v-united-states/#295" aria-description="Citation for case: Burton v. United States">196 U. S. 283, 295</a></span> (1905); <em>Liverpool, N. Y. &amp; P. S.S. Co. </em>v. <em>Commissioners of Emigration, </em><span class="citation" data-id="91256"><a href="/opinion/91256/liverpool-new-york-philadelphia-steamship-co-v-commissioners-of/#39" aria-description="Citation for case: Liverpool, New York &amp; Philadelphia Steamship Co. v....">113 U. S. 33, 39</a></span> (1885). See also <em>Ashwander </em>v. <em>TV A, </em><span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#346" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 346-347</a></span> (1936) (Brandeis, J., concurring). The remaining issues raised by the parties include whether § 647(e) implicates Fourth Amendment concerns, whether the individual has a legitimate expectation of privacy in his identity when he is detained lawfully under <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>, </em>whether the requirement that an individual identify himself during a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop violates the Fifth Amendment protection against compelled testimony, and whether inclusion of the <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>standard as part of a criminal <page-number citation-index="1" label="362">*362</page-number>statute creates other vagueness problems. The appellee also argues that § 647(e) permits arrests on less than probable cause. See <em>Michigan </em>v. <em>DeFillippo, </em><span class="citation" data-id="9427654"><a href="/opinion/110127/michigan-v-defillippo/#36" aria-description="Citation for case: Michigan v. DeFillippo">443 U. S. 31, 36</a></span> (1979).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Kuhlmann v. Wilson.md  (`case`, 5 assertions)

### content_page

```
---
title: "Kuhlmann v. Wilson"
type: case
citation: "477 U.S. 436 (1986)"
parallel_cite: "106 S. Ct. 2616; 91 L. Ed. 2d 364; 54 U.S.L.W. 4809"
neutral_cite: 1986 U.S. LEXIS 65
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-06-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kuhlmann v. Wilson
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111726/kuhlmann-v-wilson/"
  cluster_id: 111726
  opinion_id: 9430620
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Maine v. Moulton]]", "[[United States v. Henry]]", "[[Brewer v. Williams]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "deliberate-elicitation", "jailhouse-informant"]
holding: "A defendant does not make out a Sixth Amendment violation merely by showing an informant reported his statements; he must show the…"
lake:
  record_id: Kuhlmann v. Wilson
  status: under_review
  projected_at: 2026-07-09
---

# Kuhlmann v. Wilson

*477 U.S. 436 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Wilson was arraigned and jailed, police placed him in a cell with an informant, Lee, and instructed Lee only to listen — to learn the identities of Wilson's accomplices, not to question him. The state courts found that Lee asked no questions and "only listened" to Wilson's spontaneous statements, offering no more than a remark that Wilson's first account "didn't sound too good." Wilson later made incriminating statements that were used against him.

## Issue
Whether a defendant's Sixth Amendment right to counsel is violated merely because a jailhouse informant, placed in his cell, reports his incriminating statements to the police — or whether more is required.

## Rule
Passive listening is not enough; the State must have taken affirmative steps to draw out statements. "the Sixth Amendment is not violated whenever — by luck or happenstance — the State obtains incriminating statements from the accused after the right to counsel has attached." — 477 U.S. at 459. ^pin-459

Accordingly, "the defendant must demonstrate that the police and their informant took some action, beyond merely listening, that was designed deliberately to elicit incriminating remarks." — [*Id.*](https://www.courtlistener.com/opinion/111726/kuhlmann-v-wilson/#:~:text=the%20defendant%20must%20demonstrate%20that) ^pin-459a

## Application
Here the state courts found that Lee was instructed only to listen, asked Wilson no questions about the pending charges, and merely heard Wilson's spontaneous and unsolicited statements. Because Lee took no action beyond listening that was designed to elicit incriminating remarks, the informant functioned as a passive "listening post," and Wilson failed to make out a Sixth Amendment violation under the *[[Massiah v. United States|Massiah]]* deliberate-elicitation standard.

## Conclusion
The Court of Appeals erred in finding a Sixth Amendment violation; absent deliberate elicitation beyond mere listening, no right-to-counsel violation occurred. (Judgment reversed.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Kuhlmann* refines the [[Massiah v. United States]] / [[United States v. Henry]] line by drawing the line between a passive "listening post" (permissible) and active "deliberate elicitation" (a violation), consistent with [[Maine v. Moulton]].

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Kuhlmann v. Wilson*, 477 U.S. 436 (1986) — https://www.courtlistener.com/opinion/111726/kuhlmann-v-wilson/ — pinpoint: 459.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7e7220b984d8ee6b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "477 U.S. 436 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 65", "official_citation_present": true, "parallel_cite": "106 S. Ct. 2616; 91 L. Ed. 2d 364; 54 U.S.L.W. 4809", "title": "Kuhlmann v. Wilson", "year": "1986"}}
{"assertion_id": "509038b18003cd90", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A defendant does not make out a Sixth Amendment violation merely by showing an informant reported his statements; he must show the…", "title": "Kuhlmann v. Wilson"}}
{"assertion_id": "c6091cc1f2820a3f", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "Kuhlmann v. Wilson"}}
{"assertion_id": "7e88437405ef39ba", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kuhlmann v. Wilson"}}
{"assertion_id": "adba6ae159e51bf7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kuhlmann v. Wilson", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Kuhlmann v. Wilson", "varies_by_point": "false"}}
```

### lake record — Kuhlmann v. Wilson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kuhlmann v. Wilson",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Kuhlmann v. Wilson",
    "case_name_short": "Kuhlmann",
    "case_name_full": "Kuhlmann, Superintendent, Sullivan Correctional Facility v. Wilson",
    "input_case_name": "Kuhlmann v. Wilson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-06-26",
    "year": 1986,
    "docket": null,
    "cluster_id": 111726,
    "lead_opinion_id": 9430620,
    "sibling_ids": [
      111726,
      9430620,
      9430621,
      9430622,
      9430623
    ],
    "absolute_url": "/opinion/111726/kuhlmann-v-wilson/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "477 U.S. 436",
      "volume": "477",
      "reporter": "U.S.",
      "page": "436",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 2616",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "2616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 L. Ed. 2d 364",
        "volume": "91",
        "reporter": "L. Ed. 2d",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4809",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4809",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 65",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "477 U.S. 436",
        "volume": "477",
        "reporter": "U.S.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 2616",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "2616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 L. Ed. 2d 364",
        "volume": "91",
        "reporter": "L. Ed. 2d",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 65",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4809",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4809",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "477 U.S. 436",
    "official_selection": {
      "court_class": "scotus",
      "selected": "477 U.S. 436",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-459",
      "page": null,
      "quote": "Wilson later made incriminating statements that were used against him. ## Issue Whether a defendant's Sixth Amendment right to counsel is violated merely because a jailhouse informant, placed in his cell, reports his incriminating statements to the police \u2014 or whether more is required. ## Rule Passive listening is not enough; the State must have taken affirmative steps to draw out statements.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-459a",
      "page": null,
      "quote": "the defendant must demonstrate that the police and their informant took some action, beyond merely listening, that was designed deliberately to elicit incriminating remarks.",
      "star_marker": "459",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 51920,
      "fragment": "#:~:text=the%20defendant%20must%20demonstrate%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kuhlmann v. Wilson",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Justin Barrett Blakeney v. State of Mississippi",
          "cluster_id": 4442047,
          "cite": [
            "236 So. 3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zackary Stewart v. Karl Wagner",
          "cluster_id": 4255669,
          "cite": [
            "836 F.3d 978",
            "2016 U.S. App. LEXIS 16642",
            "2016 WL 4728039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended September 20, 2016 State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 4472001,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 3218790,
          "cite": [
            "882 N.W.2d 68",
            "2016 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 2806802,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lee v. Lampert",
          "cluster_id": 222324,
          "cite": [
            "653 F.3d 929",
            "2011 U.S. App. LEXIS 15830",
            "2011 WL 3275947"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McKithen v. Brown",
          "cluster_id": 1458192,
          "cite": [
            "565 F. Supp. 2d 440",
            "2008 U.S. Dist. LEXIS 55094",
            "2008 WL 2791852"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Abshear v. Moore",
          "cluster_id": 1870722,
          "cite": [
            "546 F. Supp. 2d 530",
            "2008 U.S. Dist. LEXIS 16269",
            "2008 WL 640363"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. Giurbino",
          "cluster_id": 8642780,
          "cite": [
            "237 F. App'x 299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re: Will C. Dean, Jr.",
          "cluster_id": 76288,
          "cite": [
            "341 F.3d 1247",
            "2003 U.S. App. LEXIS 16630",
            "2003 WL 21920231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steven L. Manning v. Michael Bowersox, Superintendent Jeremiah (Jay) Nixon, Attorney General, State of Missouri.",
          "cluster_id": 779815,
          "cite": [
            "310 F.3d 571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United State ex rel. Bryant v. Warden",
          "cluster_id": 7295228,
          "cite": [
            "50 F. App'x 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane1_negative"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bousley v. United States",
          "cluster_id": 118205,
          "cite": [
            "140 L. Ed. 2d 828",
            "118 S. Ct. 1604",
            "523 U.S. 614",
            "1998 U.S. LEXIS 3334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McQuiggin v. Perkins",
          "cluster_id": 872995,
          "cite": [
            "185 L. Ed. 2d 1019",
            "133 S. Ct. 1924",
            "2013 U.S. LEXIS 4068",
            "569 U.S. 383",
            "82 A.L.R. Fed. 2d 663",
            "81 U.S.L.W. 4327",
            "24 Fla. L. Weekly Fed. S 213",
            "2013 WL 2300806"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montgomery v. Louisiana",
          "cluster_id": 3171724,
          "cite": [
            "577 U.S. 190",
            "136 S. Ct. 718",
            "193 L. Ed. 2d 599",
            "25 Fla. L. Weekly Fed. S 611",
            "84 U.S.L.W. 4063",
            "2016 U.S. LEXIS 862"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sawyer v. Whitley",
          "cluster_id": 112773,
          "cite": [
            "120 L. Ed. 2d 269",
            "112 S. Ct. 2514",
            "505 U.S. 333",
            "1992 U.S. LEXIS 3864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'NEAL v. McAninch",
          "cluster_id": 117897,
          "cite": [
            "130 L. Ed. 2d 947",
            "115 S. Ct. 992",
            "513 U.S. 432",
            "1995 U.S. LEXIS 908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Panetti v. Quarterman",
          "cluster_id": 145700,
          "cite": [
            "168 L. Ed. 2d 662",
            "127 S. Ct. 2842",
            "551 U.S. 930",
            "2007 U.S. LEXIS 8667"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Preciose",
          "cluster_id": 2309234,
          "cite": [
            "609 A.2d 1280",
            "129 N.J. 451",
            "1992 N.J. LEXIS 422"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Udzinski",
          "cluster_id": 6046950,
          "cite": [
            "146 A.D.2d 245",
            "541 N.Y.S.2d 9",
            "1989 N.Y. App. Div. LEXIS 5019"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1172635,
          "cite": [
            "16 Cal. 4th 153",
            "940 P.2d 710",
            "66 Cal. Rptr. 2d 123",
            "97 Cal. Daily Op. Serv. 6192",
            "97 Daily Journal DAR 10025",
            "1997 Cal. LEXIS 4410"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banister v. Davis",
          "cluster_id": 4757658,
          "cite": [
            "590 U.S. 504",
            "140 S. Ct. 1698",
            "207 L. Ed. 2d 58"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
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
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Clark",
          "cluster_id": 1113311,
          "cite": [
            "855 P.2d 729",
            "5 Cal. 4th 750",
            "21 Cal. Rptr. 2d 509",
            "93 Cal. Daily Op. Serv. 5736",
            "93 Daily Journal DAR 9761",
            "1993 Cal. LEXIS 3652"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kuhlmann v. Wilson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111726 OR 9430620 OR 9430621 OR 9430622 OR 9430623) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDAwMDgwMDAwMDAwJnM9Nzc1MzM3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111726+OR+9430620+OR+9430621+OR+9430622+OR+9430623%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111726 OR 9430620 OR 9430621 OR 9430622 OR 9430623)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNDMmcz01MzQ4NzImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111726+OR+9430620+OR+9430621+OR+9430622+OR+9430623%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111726 OR 9430620 OR 9430621 OR 9430622 OR 9430623)",
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
    "complete_query": "cites:(111726 OR 9430620 OR 9430621 OR 9430622 OR 9430623)",
    "indexed_citing_opinions": 674,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111726,
        "count": 618,
        "count_source": "search"
      },
      {
        "opinion_id": 9430620,
        "count": 70,
        "count_source": "search"
      },
      {
        "opinion_id": 9430621,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430622,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430623,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1210,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kuhlmann-v-wilson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyMDEyNDEmcz0xMDEwOTk0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111726+OR+9430620+OR+9430621+OR+9430622+OR+9430623%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111726,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 103660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 103842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 105075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 106591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 107679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 108263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 108302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 108578,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 109405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 109717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 110138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 110143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 110382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 110692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 111228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 111235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 111674,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 258052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 360154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111726,
        "cited_id": 440444,
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
    "date_created": "2026-07-05T10:29:37Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:29:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:29:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:35:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:29:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kuhlmann v. Wilson

```
<opinion type="majority">
<author id="b462-9">Justice Powell</author>
<p id="Anh">announced the judgment of the Court and delivered the opinion of the Court with respect to Parts I, IV, and V, and an opinion with respect to Parts II and III in which The Chief Justice, Justice Rehnquist, and Justice O’Connor join.</p>
<p id="b462-10">This case requires us to define the circumstances under which federal courts should entertain a state prisoner’s petition for writ of habeas corpus that raises claims rejected on a prior petition for the same relief.</p>
<p id="b462-11">
<em>h-4</em>
</p>
<p id="b462-3">In the early morning of July 4, 1970, respondent and two confederates robbed the Star Taxicab Garage in the Bronx, New York, and fatally shot the night dispatcher. Shortly <page-number citation-index="1" label="439">*439</page-number>before, employees of the garage had observed respondent, a former employee there, on the premises conversing with two other men. They also witnessed respondent fleeing after the robbery, carrying loose money in his arms. After eluding the police for four days, respondent turned himself in. Respondent admitted that he had been present when the crimes took place, claimed that he had witnessed the robbery, gave the police a description of the robbers, but denied knowing them. Respondent also denied any involvement in the robbery or murder, claiming that he had fled because he was afraid of being blamed for the crimes.</p>
<p id="b463-5">After his arraignment, respondent was confined in the Bronx House of Detention, where he was placed in a cell with a prisoner named Benny Lee. Unknown to respondent, Lee had agreed to act as a police informant. Respondent made incriminating statements that Lee reported to the police. Prior to trial, respondent moved to suppress the statements on the ground that they were obtained in violation of his right to counsel. The trial court held an evidentiary hearing on the suppression motion, which revealed that the statements were made under the following circumstances.</p>
<p id="b463-6">Before respondent arrived in the jail, Lee had entered into an arrangement with Detective Cullen, according to which Lee agreed to listen to respondent’s conversations and report his remarks to Cullen. Since the police had positive evidence of respondent’s participation, the purpose of placing Lee in the cell was to determine the identities of respondent’s confederates. Cullen instructed Lee not to ask respondent any questions, but simply to “keep his ears open” for the names of the other perpetrators. Respondent first spoke to Lee about the crimes after he looked out the cellblock window at the Star Taxicab Garage, where the crimes' had occurred. Respondent said, “someone’s messing with me,” and began talking to Lee about the robbery, narrating the same story that he had given the police at the time of his arrest. Lee advised respondent that this explanation “didn’t <page-number citation-index="1" label="440">*440</page-number>sound too good,”<footnotemark>1</footnotemark> but respondent did not alter his story. Over the next few days, however, respondent changed details of his original account. Respondent then received a visit from his brother, who mentioned that members of his family were upset because they believed that respondent had murdered the dispatcher. After the visit, respondent again described the crimes to Lee. Respondent now admitted that he and two other men, whom he never identified, had planned and carried out the robbery, and had murdered the dispatcher. Lee informed Cullen of respondent’s statements and furnished Cullen with notes that he had written surreptitiously while sharing the cell with respondent.</p>
<p id="b464-5">After hearing the testimony of Cullen and Lee,<footnotemark>2</footnotemark> the trial court found that Cullen had instructed Lee “to ask no questions of [respondent] about the crime but merely to listen as to what [respondent] might say in his presence.” The court determined that Lee obeyed these instructions, that he “at no time asked any questions with respect to the crime,” and that he “only listened to [respondent] and made notes regarding what [respondent] had to say.” The trial court also found that respondent’s statements to Lee were “spontaneous” and “unsolicited.” Under state precedent, a defendant’s volunteered statements to a police agent were admissible in evidence because the police were not required to prevent talkative defendants from making incriminating statements. See <em>People </em>v. <em>Kaye, </em>25 N. Y. 2d 139, 145, <span class="citation" data-id="5525126"><a href="/opinion/5677288/people-v-kaye/#332" aria-description="Citation for case: People v. Kaye">250 N. E. 2d 329, 332</a></span> (1969). The trial court accordingly denied the suppression motion.</p>
<p id="b465-4"><page-number citation-index="1" label="441">*441</page-number>The jury convicted respondent of common-law murder and felonious possession of a weapon. On May 18, 1972, the trial court sentenced him to a term of 20 years to life on the murder count and to a concurrent term of up to 7 years on the weapons count. The Appellate Division affirmed without opinion, <em>People </em>v. <em>Wilson, </em>41 App. Div. 2d 903, 343 N. Y. S. 2d 563 (1973), and the New York Court of Appeals denied respondent leave to appeal.</p>
<p id="b465-5">On December 7, 1973, respondent filed a petition for federal habeas corpus relief. Respondent argued, among other things, that his statements to Lee were obtained pursuant to police investigative methods that violated his constitutional rights. After considering <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the District Court for the Southern District of New York denied the writ on January 7,1977. The record demonstrated “no interrogation whatsoever” by Lee and “only spontaneous statements” from respondent. In the District Court’s view, these “fact[s] preclude[d] any Sixth Amendment violation.”</p>
<p id="b465-6">A divided panel of the Court of Appeals for the Second Circuit affirmed. <em>Wilson </em>v. <em>Henderson, </em><span class="citation" data-id="9465174"><a href="/opinion/360154/joseph-allen-wilson-v-hon-robert-j-henderson-superintendent-auburn/" aria-description="Citation for case: Joseph Allen Wilson v. Hon. Robert J. Henderson,...">584 F. 2d 1185</a></span> (1978). The court noted that a defendant is denied his Sixth Amendment rights when the trial court admits in evidence incriminating statements that state agents “‘had deliberately elicited from him after he had been indicted and in the absence of counsel.’” <span class="citation" data-id="9465174"><a href="/opinion/360154/joseph-allen-wilson-v-hon-robert-j-henderson-superintendent-auburn/#1189" aria-description="Citation for case: Joseph Allen Wilson v. Hon. Robert J. Henderson,..."><em>Id., </em>at 1189</a></span>, quoting <em>Massiah </em>v. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States"><em>United States, supra, </em>at 206</a></span>. Relying in part on <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977), the court reasoned that the “deliberately elicited” test of <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>requires something more than incriminating statements uttered in the absence of counsel. On the facts found by the state trial court, which were entitled to a presumption of correctness under <span class="citation no-link">28 U. S. C. § 2254</span>(d), the court held that respondent had not established a violation of his Sixth Amendment rights.<footnotemark>3</footnotemark> We denied a <page-number citation-index="1" label="442">*442</page-number>petition for a writ of certiorari. <em>Wilson </em>v. <em>Henderson, </em><span class="citation" data-id="9016088"><a href="/opinion/9022858/wilson-v-henderson/" aria-description="Citation for case: Wilson v. Henderson">442 U. S. 945</a></span> (1979).</p>
<p id="b466-5">Following this Court’s decision in <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980), which applied the <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>test to suppress statements made to a paid jailhouse informant, respondent decided to relitigate his Sixth Amendment claim. On September 11, 1981, he filed in state trial court a motion to vacate his conviction. The judge denied the motion, on the grounds that <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>was factually distinguishable from this case,<footnotemark>4</footnotemark> and that under state precedent <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>was not to be given retroactive effect, see <em>People </em>v. <em>Pepper, </em>53 N. Y. 2d 213, <span class="citation" data-id="5533816"><a href="/opinion/5684915/people-v-pepper/" aria-description="Citation for case: People v. Pepper">423 N. E. 2d 366</a></span> (1981). The Appellate Division denied respondent leave to appeal.</p>
<p id="b466-6">On July 6, 1982, respondent returned to the District Court for the Southern District of New York on a habeas petition, again arguing that admission in evidence of his incriminating statements to Lee violated his Sixth Amendment rights. Respondent contended that the decision in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>constituted a new rule of law that should be applied retroactively to this case. The District Court found it unnecessary to consider retroactivity because it decided that <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>did not undermine the Court of Appeals’ prior disposition of respondent’s Sixth Amendment claim. Noting that <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>reserved the question whether the Constitution forbade admission in evidence of an accused’s statements to an informant who made “no effort to stimulate conversations about the crime charged,” see <em>United States </em>v. <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry"><em>Henry, supra, </em>at 271, n. 9</a></span>, <page-number citation-index="1" label="443">*443</page-number>the District Court believed that this case presented that open question and that the question must be answered negatively. The District Court noted that the trial court’s findings were presumptively correct, see <span class="citation no-link">28 U. S. C. § 2254</span>(d), and were fully supported by the record. The court concluded that these findings were “fatal” to respondent’s claim under <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>since they showed that Lee made no “affirmative effort” of any kind “to elicit information” from respondent.</p>
<p id="b467-5">A different, and again divided, panel of the Court of Appeals reversed. <em>Wilson </em>v. <em>Henderson, </em><span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d 741</a></span> (1984). As an initial matter, the court stated that, under <em>Sanders </em>v. <em>United States, </em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">373 U. S. 1</a></span> (1963), the “ends of justice” required consideration of this petition, notwithstanding the fact that the prior panel had determined the merits adversely to respondent. <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#743" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 743</a></span>. The court then reasoned that the circumstances under which respondent made his incriminating statements to Lee were indistinguishable from the facts of <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>. </em>Finally, the court decided that <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>was fully applicable here because it did not announce a new constitutional rule, but merely applied settled principles to new facts. <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#746" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 746-747</a></span>. Therefore, the court concluded that all of the judges who had considered and rejected respondent’s claim had erred, and remanded the case to the District Court with instructions to order respondent’s release from prison unless the State elected to retry him.<footnotemark>5</footnotemark></p>
<p id="b468-8"><page-number citation-index="1" label="444">*444</page-number>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./472/1026/">472 U. S. 1026</a></span> (1985), to consider the Court of Appeals’ decision that the “ends of justice” required consideration of this successive habeas corpus petition and that court’s application of our decision in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>to the facts of this case. We now reverse.</p>
<p id="b468-9">K</p>
<p id="b468-3">A</p>
<p id="AWP">In concluding that it was appropriate to entertain respondent’s successive habeas corpus petition, the Court of Appeals relied upon <em>Sanders </em>v. <em>United States, </em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">373 U. S. 1</a></span> (1963), which announced guidelines for the federal courts to follow when presented with habeas petitions or their equivalent claimed to be “successive” or an “abuse of the writ.”<footnotemark>6</footnotemark> The narrow question in <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>was whether a federal prisoner’s motion under <span class="citation no-link">28 U. S. C. § 2255</span> was properly denied without a hearing on the ground that the motion constituted a successive application. <span class="citation no-link">Id., at 4-6</span>. The Court undertook not only to answer that question, but also to explore the standard that should <em>govern </em>district courts’ consideration of successive petitions. <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>framed the inquiry in terms of the requirements of the “ends of justice,” advising district courts to dismiss habeas petitions or their equivalent raising claims determined adversely to the prisoner on a prior petition if <page-number citation-index="1" label="445">*445</page-number>“the ends of justice would not be served by reaching the merits of the subsequent application.” <span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#15" aria-description="Citation for case: Sanders v. United States"><em>Id., </em>at 15, 16-17</a></span>. While making clear that the burden of proof on this issue rests on the prisoner, <span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#17" aria-description="Citation for case: Sanders v. United States"><em>id., </em>at 17</a></span>, the Court in <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>provided little specific guidance as to the kind of proof that a prisoner must offer to establish that the “ends of justice” would be served by relitigation of the claims previously decided against him.</p>
<p id="b469-5">The Court of Appeals’ decision in this case demonstrates the need for this Court to provide that guidance. The opinion of the Court of Appeals sheds no light on this important threshold question, merely declaring that the “ends of justice” required successive federal habeas corpus review. Failure to provide clear guidance leaves district judges “at large in disposing of applications for a writ of habeas corpus,” creating the danger that they will engage in “the exercise not of law but of arbitrariness.” <em>Brown </em>v. <em>Allen, </em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#497" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 497</a></span> (1953) (opinion of Frankfurter, J.). This Court therefore must now define the considerations that should govern federal courts’ disposition of successive petitions for habeas corpus.</p>
<p id="b469-6">B</p>
<p id="b469-7">Since 1867, when Congress first authorized the federal courts to issue the writ on behalf of persons in state custody,<footnotemark>7</footnotemark> this Court often has been called upon to interpret the language of the statutes defining the scope of that jurisdiction. It may be helpful to review our cases construing these frequently used statutes before we answer the specific question before us today.</p>
<p id="b469-8">Until the early years of this century, the substantive scope of the federal habeas corpus statutes was defined by refer<page-number citation-index="1" label="446">*446</page-number>ence to the scope of the writ at common law, where the courts’ inquiry on habeas was limited exclusively “to the jurisdiction of the sentencing tribunal.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#475" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 475</a></span> (1976). See <em>Wainwright </em>v. <em>Sykes, </em><span class="citation multiple-matches"><a href="/c/U.%20S./438/72/">438 U. S. 72</a></span>, 78, 79 (1977); see also Oaks, Legal History in the High Court — Habeas Corpus, <span class="citation no-link">64 Mich. L. Rev. 451</span>, 458-468 (1966). Thus, the finality of the judgment of a committing court of competent jurisdiction was accorded absolute respect on habeas review. See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#254" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 254-256</a></span> (1973) (POWELL, J., concurring). During this century, the Court gradually expanded the grounds on which habeas corpus relief was available, authorizing use of the writ to challenge convictions where the prisoner claimed a violation of certain constitutional rights. See <em>Wainwright </em>v. <em>Sykes, supra, </em>at 79-80; <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#475" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 475-478</a></span>. The Court initially accomplished this expansion while purporting to adhere to the inquiry into the sentencing court’s jurisdiction. <em>Wainwright </em>v. <em>Sykes, </em>433 U. S., at 79. Ultimately, the Court abandoned the concept of jurisdiction and acknowledged that habeas “review is available for claims of ‘disregard of the constitutional rights of the accused, and where the writ is the only effective means of preserving his rights.’” <em>Ibid., </em>quoting <em>Waley </em>v. <em>Johnston, </em><span class="citation" data-id="103660"><a href="/opinion/103660/waley-v-johnston/#104" aria-description="Citation for case: Waley v. Johnston">316 U. S. 101, 104-105</a></span> (1942).</p>
<p id="b470-5">Our decisions have not been limited to expanding the scope of the writ. Significantly, in <em>Stone </em>v. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Powell</a></span>, </em>we removed from the reach of the federal habeas statutes a state prisoner’s claim that “evidence obtained in an unconstitutional search or seizure was introduced at his trial” unless the prisoner could show that the State had failed to provide him “an opportunity for full and fair litigation” of his Fourth Amendment claim. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#494" aria-description="Citation for case: Stone v. Powell">428 U. S., at 494</a></span> (footnotes omitted). Although the Court previously had accepted jurisdiction of search and seizure claims, <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#480" aria-description="Citation for case: Stone v. Powell"><em>id., </em>at 480</a></span>, we were persuaded that any “advance of the legitimate goal of furthering Fourth Amendment rights” through application of the judicially ere-<page-number citation-index="1" label="447">*447</page-number>ated exclusionary rule on federal habeas was “outweighed by the acknowledged costs to other values vital to a rational system of criminal justice.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#494" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 494</a></span>. Among those costs were diversion of the attention of the participants at a criminal trial “from the ultimate question of guilt or innocence,” and exclusion of reliable evidence that was “often the most probative information bearing on the guilt or innocence of the defendant.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 490</a></span>. Our decision to except this category of claims from habeas corpus review created no danger that we were denying a “safeguard against compelling an innocent man to suffer an unconstitutional loss of liberty.” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#491" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 491-492, n. 31</a></span>. Rather, a convicted defendant who pressed a search and seizure claim on collateral attack was “usually asking society to redetermine an issue that ha[d] no bearing on the basic justice of his incarceration. ” <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#492" aria-description="Citation for case: Stone v. Powell"><em>Id., </em>at 492, n. 31</a></span>.</p>
<p id="b471-5">In decisions of the past two or three decades construing the reach of the habeas statutes, whether reading those statutes broadly or narrowly, the Court has reaffirmed that “habeas corpus has traditionally been regarded as governed by equitable principles.” <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#438" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 438</a></span> (1963), citing <em>United States ex rel. Smith </em>v. <em>Baldi, </em><span class="citation" data-id="9420866"><a href="/opinion/105075/united-states-ex-rel-smith-v-baldi/#573" aria-description="Citation for case: United States Ex Rel. Smith v. Baldi">344 U. S. 561, 573</a></span> (1953) (dissenting opinion). See <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#478" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 478, n. 11</a></span>. The Court uniformly has been guided by the proposition that the writ should be available to afford relief to those “persons whom society has grievously wronged” in light of modern concepts of justice. <em>Fay </em>v. <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#440" aria-description="Citation for case: Fay v. Noia"><em>Noia, supra, </em>at 440-441</a></span>. See <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#492" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 492, n. 31</a></span>. Just as notions of justice prevailing at the inception of habeas corpus were offended when a conviction was issued by a court that lacked jurisdiction, so the modern conscience found intolerable convictions obtained in violation of certain constitutional commands. But the Court never has defined the scope of the writ simply by reference to a perceived need to assure that an individual accused of crime is afforded a trial free of constitutional error. Rather, the Court has performed its <page-number citation-index="1" label="448">*448</page-number>statutory task through a sensitive weighing of the interests implicated by federal habeas corpus adjudication of constitutional claims determined adversely to the prisoner by the state courts. <em>E. g., Engle </em>v. <em>Isaac, </em><span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#126" aria-description="Citation for case: Engle v. Isaac">456 U. S. 107, 126-129</a></span> (1982); <em>Stone </em>v. <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell"><em>Powell, supra, </em>at 489-495</a></span>; <em>Fay </em>v. <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#426" aria-description="Citation for case: Fay v. Noia"><em>Noia, supra, </em>at 426-434</a></span>.<footnotemark>8</footnotemark></p>
<p id="b472-5">III</p>
<p id="b472-6">A</p>
<p id="b472-7">The Court in <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>drew the phrase “ends of justice” directly from the version of <span class="citation no-link">28 U. S. C. § 2244</span> in effect in 1963. The provision, which then governed petitions filed by both federal and state prisoners, stated in relevant part that no federal judge “shall be required to entertain an application for a writ of habeas corpus to inquire into the detention of a person ... , if it appears that the legality of such detention has been determined” by a federal court “on a prior application for a writ of habeas corpus and the petition presents no new ground not theretofore presented and determined, and the judge ... is satisfied that the <em>ends of justice will not be served by such </em>inquiry.” <span class="citation no-link">28 U. S. C. §2244</span> (1964 ed.) (emphasis added). Accordingly, in describing guidelines for suc<page-number citation-index="1" label="449">*449</page-number>cessive petitions, <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>did little more than quote the language of the then-pertinent statute, leaving for another day the task of giving that language substantive content.</p>
<p id="b473-5">In 1966, Congress carefully reviewed the habeas corpus statutes and amended their provisions, including §2244. Section 2244(b), which we construe today, governs successive petitions filed by state prisoners. The section makes no reference to the “ends of justice,”<footnotemark>9</footnotemark> and provides that the federal courts “need not” entertain “subsequent applications” from state prisoners “unless the application alleges and is predicated on a factual or other ground not adjudicated on” the prior application “and unless the court ... is satisfied that the applicant has not on the earlier application deliberately withheld the newly asserted ground or otherwise abused the writ.”<footnotemark>10</footnotemark> In construing this language, we are cognizant that Congress adopted the section in light of the need — often recognized by this Court — to weigh the interests of the individual prisoner against the sometimes contrary interests of the State in administering a fair and rational system of criminal laws.<footnotemark>11</footnotemark></p>
<p id="b474-4"><page-number citation-index="1" label="450">*450</page-number>The legislative history demonstrates that Congress intended the 1966 amendments, including those to § 2244(b), to introduce “a greater degree of finality of judgments in habeas corpus proceedings.” S. Rep. No. 1797, 89th Cong., 2d Sess., 2 (1966) (Senate Report). Congress was concerned with the “steadily increasing” burden imposed on the federal courts by “applications by State prisoners for writs of habeas corpus.”<footnotemark>12</footnotemark> <em>Id., </em>at 1; see H. R. Rep. No. 1892, 89th Cong., 2d Sess., 5-6 (1966) (House Report). In many instances, the “heavy burden” created by these applications was “unnecessary” because state prisoners “have been filing applications either containing allegations identical to those asserted in a previous application that has been denied, or predicated upon grounds obviously well known to them when they filed the preceding application.” Senate Report, at 2; see House Report, at 5. The Senate Report explicitly states that the “purpose” of the amendments was to “alleviate the unnecessary burden” by adding “to section 2244 . . . provisions for a qualified application of the doctrine of res judicata.” Senate Report, at 2; see House Report, at 8. The House also <page-number citation-index="1" label="451">*451</page-number>expressed concern that the increasing number of habeas applications from state prisoners “greatly interfered with the procedures and processes of the State courts by delaying, in many eases, the proper enforcement of their judgments.” <em>Id., </em>at 5.</p>
<p id="b475-5">Based on the 1966 amendments and their legislative history, petitioner argues that federal courts no longer must consider the “ends of justice” before dismissing a successive petition. We reject this argument. It is clear that Congress intended for district courts, as the general rule, to give preclusive effect to a judgment denying on the merits a ha-beas petition alleging grounds identical in substance to those raised in the subsequent petition. But the permissive language of § 2244(b) gives federal courts discretion to entertain successive petitions under some circumstances. Moreover, Rule 9(b) of the Rules Governing Section 2254 Cases in the United States District Courts, which was amended in 1976, contains similar permissive language, providing that the district court “may” dismiss a “second or successive petition” that does not “allege new or different grounds for relief.” Consistent with Congress’ intent in enacting § 2244(b), however, the Advisory Committee Note to Rule 9(b), 28 U. S. C., p. 358, states that federal courts should entertain successive petitions only in “rare instances.”<footnotemark>13</footnotemark> Unless those “rare instances” are to be identified by whim or caprice, district judges must be given guidance for determining when to exercise the limited discretion granted them by § 2244(b). Accordingly, as a means of identifying the rare case in which federal courts should exercise their discretion to hear a successive petition, we continue to rely on the reference in <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>to the “ends of justice.” Our task is to provide a definition of the “ends of justice” that will accommodate Congress’ intent to give finality to federal habeas judgments with <page-number citation-index="1" label="452">*452</page-number>the historic function of habeas corpus to provide relief from unjust incarceration.</p>
<p id="b476-5">B</p>
<p id="b476-6">We now consider the limited circumstances under which the interests of the prisoner in relitigating constitutional claims held meritless on a prior petition may outweigh the countervailing interests served by according finality to the prior judgment. We turn first to the interests of the prisoner.</p>
<p id="b476-7">The prisoner may have a vital interest in having a second chance to test the fundamental justice of his incarceration. Even where, as here, the many judges who have reviewed the prisoner’s claims in several proceedings provided by the State and on his first petition for federal habeas corpus have determined that his trial was free from constitutional error, a prisoner retains a powerful and legitimate interest in obtaining his release from custody if he is innocent of the charge for which he was incarcerated. That interest does not extend, however, to prisoners whose guilt is conceded or plain. As Justice Harlan observed, the guilty prisoner himself has “an interest in insuring that there will at some point be the certainty that comes with an end to litigation, and that attention will ultimately be focused not on whether a conviction was free from error but rather on whether the prisoner can be restored to a useful place in the community.” <em>Sanders </em>v. <em>United States, </em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#24" aria-description="Citation for case: Sanders v. United States">373 U. S., at 24-25</a></span> (dissenting).</p>
<p id="b476-8">Balanced against the prisoner’s interest in access to a forum to test the basic justice of his confinement are the interests of the State in administration of its criminal statutes. Finality serves many of those important interests. Availability of unlimited federal collateral review to guilty defendants frustrates the State’s legitimate interest in deterring crime, since the deterrent force of penal laws is diminished to the extent that persons contemplating criminal activity believe there is a possibility that they will 'escape punishment <page-number citation-index="1" label="453">*453</page-number>through repetitive collateral attacks.<footnotemark>14</footnotemark> See <em>Engle </em>v. <em>Isaac, </em><span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#127" aria-description="Citation for case: Engle v. Isaac">456 U. S., at 127-128, n. 32</a></span>. Similarly, finality serves the State’s goal of rehabilitating those who commit crimes because “[rjehabilitation demands that the convicted defendant realize that ‘he is justly subject to sanction, that he stands in need of rehabilitation.’” <span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#128" aria-description="Citation for case: Engle v. Isaac"><em>Id., </em>at 128</a></span>, n. 32 (quoting Bator, Finality in Criminal Law and Federal Habeas Corpus for State Prisoners, <span class="citation no-link">76 Harv. L. Rev. 441</span>, 452 (1963)). See <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#262" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 262</a></span> (Powell, J., concurring). Finality also serves the State’s legitimate punitive interests. When a prisoner is freed on a successive petition, often many years after his crime, the State may be unable successfully to retry him.<footnotemark>15</footnotemark> <em>Peyton </em>v. <em>Rowe, </em><span class="citation" data-id="107679"><a href="/opinion/107679/peyton-v-rowe/#62" aria-description="Citation for case: Peyton v. Rowe">391 U. S. 54, 62</a></span> (1968). This result is unacceptable if the State must forgo conviction of a guilty defendant through the “erosion of memory” and “dispersion of witnesses” that occur with the passage of time that invariably attends collateral attack.<footnotemark>16</footnotemark> <page-number citation-index="1" label="454">*454</page-number><em>Engle </em>v. <span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#127" aria-description="Citation for case: Engle v. Isaac"><em>Isaac, supra, </em>at 127-128</a></span>; Friendly, Is Innocence Irrelevant? Collateral Attack on Criminal Judgments, <span class="citation no-link">38 U. Chi. L. Rev. 142</span>, 146-148 (1970).</p>
<p id="b478-5">In the light of the historic purpose of habeas corpus and the interests implicated by successive petitions for federal ha-beas relief from a state conviction, we conclude that the “ends of justice” require federal courts to entertain such petitions only where the prisoner supplements his constitutional claim with a colorable showing of factual innocence. This standard was proposed by Judge Friendly more than a decade ago as a prerequisite for federal habeas review generally. Friendly, <em>supra. </em>As Judge Friendly persuasively argued then, a requirement that the prisoner come forward with a colorable showing of innocence identifies those habeas petitioners who are justified in again seeking relief from their incarceration. We adopt this standard now to effectuate the clear intent of Congress that successive federal habeas review should be granted only in rare cases, but that it should be available when the ends of justice so require. The prisoner may make the requisite showing by establishing that under the probative evidence he has a colorable claim of factual innocence. The prisoner must make his evidentiary showing even though — as argued in this case — the evidence of guilt may have been unlawfully admitted.<footnotemark>17</footnotemark></p>
<p id="b479-4"><page-number citation-index="1" label="455">*455</page-number>C</p>
<p id="b479-5">Applying the foregoing standard in this case, we hold that the Court of Appeals erred in concluding that the “ends of justice” would be served by consideration of respondent’s successive petition. The court conceded that the evidence of respondent’s guilt “was nearly overwhelming.” <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#742" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 742</a></span>. The constitutional claim argued by respondent does not itself raise any question as to his guilt or innocence. The District Court and the Court of Appeals should have dismissed this successive petition under § 2244(b) on the ground that the prior judgment denying relief on this identical claim was final.<footnotemark>18</footnotemark></p>
<p id="b480-9">
<page-number citation-index="1" label="456">*456</page-number>
<em>&gt;</em>
</p>
<p id="b480-3">Even if the Court of Appeals had correctly decided to entertain this successive habeas petition, we conclude that it erred in holding that respondent was entitled to relief under <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">447 U. S. 264</a></span> (1980). As the District Court observed, <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>left open the question whether the Sixth Amendment forbids admission in evidence of an accused’s statements to a jailhoúse informant who was “placed in close proximity but [made] no effort to stimulate conversations about the crime charged.” <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry"><em>Id., </em>at 271, n. 9</a></span>.<footnotemark>19</footnotemark> Our review of the line of cases beginning with <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), shows that this question must, as the District Court properly decided, be answered negatively.</p>
<p id="b480-4">A</p>
<p id="b480-5">The decision in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>had its roots in two concurring opinions written in <em>Spano </em>v. <em>New York, </em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span> (1959). See <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#172" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 172</a></span> (1985). Following his indictment for first-degree murder, the defendant in <em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span> </em>retained a lawyer and surrendered to the authorities. Before leaving the defendant in police custody, counsel cautioned him not to respond to interrogation. The prosecutor and police questioned the defendant, persisting in the face of his repeated refusal to answer and his repeated request to speak with his lawyer. The lengthy interrogation involved improper police tactics, and the defendant ultimately con<page-number citation-index="1" label="457">*457</page-number>fessed. Following a trial at which his confession was admitted in evidence, the defendant was convicted and sentenced to death. <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#316" aria-description="Citation for case: Spano v. New York">360 U. S., at 316-320</a></span>. Agreeing with the Court that the confession was involuntary and thus improperly admitted in evidence under the Fourteenth Amendment, the concurring Justices also took the position that the defendant’s right to counsel was violated by the secret interrogation. <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#325" aria-description="Citation for case: Spano v. New York">Id., at 325</a></span> (Douglas, J., concurring). As Justice Stewart observed, an indicted person has the right to assistance of counsel throughout the proceedings against him. <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#327" aria-description="Citation for case: Spano v. New York"><em>Id., </em>at 327</a></span>. The defendant was denied that right when he was subjected to an “all-night inquisition,” during which police ignored his repeated requests for his lawyer. <em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Ibid.</a></span></em></p>
<p id="b481-5">The Court in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>adopted the reasoning of the concurring opinions in <em><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span> </em>and held that, once a defendant’s Sixth Amendment right to counsel has attached, he is denied that right when federal agents “deliberately elicit” incriminating statements from him in the absence of his lawyer. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S., at 206</a></span>. The Court adopted this test, rather than one that turned simply on whether the statements were obtained in an “interrogation,” to protect accused persons from “‘indirect and surreptitious interrogations as well as those conducted in the jailhouse. In this case, Massiah was more seriously imposed upon . . . because he did not even know that he was under interrogation by a government agent.’” <em>Ibid., </em>quoting <em>United States </em>v. <em>Massiah, </em><span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/#72" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62, 72-73</a></span> (1962) (Hays, J., dissenting in part). Thus, the Court made clear that it was concerned with interrogation or investigative techniques that were equivalent to interrogation, and that it so viewed the technique in issue in Massiah.<footnotemark>20</footnotemark></p>
<p id="b482-4"><page-number citation-index="1" label="458">*458</page-number>In <em>United States </em>v. <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>the Court applied the <em>Massiah </em>test to incriminating statements made to a jailhouse informant. The Court of Appeals in that case found a violation of <em>Massiah </em>because the informant had engaged the defendant in conversations and “had developed a relationship of trust and confidence with [the defendant] such that [the defendant] revealed incriminating information.” <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#269" aria-description="Citation for case: United States v. Henry">447 U. S., at 269</a></span>. This Court affirmed, holding that the Court of Appeals reasonably concluded that the Government informant “deliberately used his position to secure incriminating information from [the defendant] when counsel was not present.” <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#270" aria-description="Citation for case: United States v. Henry"><em>Id., </em>at 270</a></span>. Although the informant had not questioned the defendant, the informant had “stimulated” conversations with the defendant in order to “elicit” incriminating information. <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#273" aria-description="Citation for case: United States v. Henry"><em>Id., </em>at 273</a></span>; see <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#271" aria-description="Citation for case: United States v. Henry"><em>id., </em>at 271, n. 9</a></span>. The Court emphasized that those facts, like the facts of <em>Massiah, </em>amounted to “ ‘indirect and surreptitious interrogation]’ ” of the defendant. <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#273" aria-description="Citation for case: United States v. Henry">447 U. S., at 273</a></span>.</p>
<p id="b482-5">Earlier this Term, we applied the <em>Massiah </em>standard in a case involving incriminating statements made under circumstances substantially similar to the facts of <em>Massiah </em>itself. In <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159</a></span> (1985), the defendant made incriminating statements in a meeting with his accomplice, who had agreed to cooperate with the police. During that meeting, the accomplice, who wore a wire transmitter to record the conversation, discussed with the defendant the charges pending against him, repeatedly asked the defendant to remind him of the details of the crime, and encouraged the defendant to describe his plan for killing witnesses. <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#165" aria-description="Citation for case: Maine v. Moulton"><em>Id., </em>at 165-166</a></span>, and n. 4. The Court concluded that these investigatory techniques denied the defendant his right to counsel on the pending charges.<footnotemark>21</footnotemark> Significantly, the Court emphasized that, because of the relationship between the defendant <page-number citation-index="1" label="459">*459</page-number>and the informant, the informant’s engaging the defendant “in active conversation about their upcoming trial was certain to elicit” incriminating statements from the defendant. <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#177" aria-description="Citation for case: Maine v. Moulton"><em>Id., </em>at 177, n. 13</a></span>. Thus, the informant’s participation “in this conversation was ‘the functional equivalent of interrogation.’” <em>Ibid, </em>(quoting <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#277" aria-description="Citation for case: United States v. Henry">447 U. S., at 277</a></span> (Powell, J., concurring)).</p>
<p id="b483-5">As our recent examination of this Sixth Amendment issue in <em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span> </em>makes clear, the primary concern of the <em>Massiah </em>line of decisions is secret interrogation by investigatory techniques that are the equivalent of direct police interrogation. Since “the Sixth Amendment is not violated whenever — by luck or happenstance — the State obtains incriminating statements from the accused after the right to counsel has attached,” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 176</a></span>, citing <em>United States </em>v. <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#276" aria-description="Citation for case: United States v. Henry"><em>Henry, supra, </em>at 276</a></span> (Powell, J., concurring), a defendant does not make out a violation of that right simply by showing that an informant, either through prior arrangement or voluntarily, reported his incriminating statements to the police. Rather, the defendant must demonstrate that the police and their informant took some action, beyond merely listening, that was designed deliberately to elicit incriminating remarks.</p>
<p id="b483-6">B</p>
<p id="b483-7">It is thus apparent that the Court of Appeals erred in concluding that respondent’s right to counsel was violated under the circumstances of this case. Its error did not stem from any disagreement with the District Court over appropriate resolution of the question reserved in <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span>, </em>but rather from its implicit conclusion that this case did not present that open question. That conclusion was based on a fundamental mistake, namely, the Court of Appeals’ failure to accord to the state trial court’s factual findings the presumption of correctness expressly required by <span class="citation no-link">28 U. S. C. § 2254</span>(d). <em>Patton </em>v. <em>Yount, </em><span class="citation" data-id="9429681"><a href="/opinion/111228/patton-v-yount/" aria-description="Citation for case: Patton v. Yount">467 U. S. 1025</a></span> (1984); <em>Sumner </em>v. <em>Mata, </em><span class="citation" data-id="9428144"><a href="/opinion/110382/sumner-v-mata/" aria-description="Citation for case: Sumner v. Mata">449 U. S. 539</a></span> (1981).</p>
<p id="b484-4"><page-number citation-index="1" label="460">*460</page-number>The state court found that Officer Cullen had instructed Lee only to listen to respondent for the purpose of determining the identities of the other participants in the robbery and murder. The police already had solid evidence of respondent’s participation.<footnotemark>22</footnotemark> The court further found that Lee followed those instructions, that he “at no time asked any questions” of respondent concerning the pending charges, and that he “only listened” to respondent’s “spontaneous” and “unsolicited” statements. The only remark made by Lee that has any support in this record was his comment that respondent’s initial version of his participation in the crimes “didn’t sound too good.” Without holding that any of the state court’s findings were not entitled to the presumption of correctness under § 2254(d),<footnotemark>23</footnotemark> the Court of Appeals focused on that one remark and gave a description of Lee’s interaction with respondent that is completely at odds with the facts found by the trial court. In the Court of Appeals’ view, “[s]ubtly and slowly, but surely, Lee’s ongoing verbal intercourse with [respondent] served to exacerbate [respondent’s] already troubled state of mind.”<footnotemark>24</footnotemark> <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#745" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 745</a></span>. After thus revising some of the trial court’s findings, and ignoring other more relevant findings, the Court of Appeals concluded that the police “deliberately elicited” respondent’s incriminating statements. <em><span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/" aria-description="Citation for case: Wilson v. Henderson">Ibid.</a></span> </em>This conclusion conflicts with the <page-number citation-index="1" label="461">*461</page-number>decision of every other state and federal judge who reviewed this record, and is clear error in light of the provisions and intent of § 2254(d).</p>
<p id="b485-6">V</p>
<p id="b485-7">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b485-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b464-6"> At the suppression hearing, Lee testified that, after hearing respondent’s initial version of his participation in the crimes, “I think I remember telling him that the story wasn’t — it didn’t sound too good. Things didn’t look too good for him.” At trial, Lee testified to a somewhat different version of his remark: “Well, I said, look, you better come up with a better story than that because that one doesn’t sound too cool to me, that’s what I said.”</p>
</footnote>
<footnote label="2">
<p id="b464-7"> Respondent did not testify at the suppression hearing.</p>
</footnote>
<footnote label="3">
<p id="b465-7"> The Court of Appeals observed that suppression of respondent’s statements would serve “no useful purpose” because Cullen had not engaged in <page-number citation-index="1" label="442">*442</page-number>“reprehensible police behavior,” but rather had made a “conscious effort” to protect respondent’s “constitutional rights [under <em>Massiah] </em>while pursuing a crucial homicide investigation.” <em>Wilson </em>v. <em>Henderson, </em><span class="citation" data-id="9465174"><a href="/opinion/360154/joseph-allen-wilson-v-hon-robert-j-henderson-superintendent-auburn/#1191" aria-description="Citation for case: Joseph Allen Wilson v. Hon. Robert J. Henderson,...">584 F. 2d, at 1191</a></span>.</p>
<p id="A4qQ">Judge Oakes dissented, arguing that the “deliberately elicited” test of <em>Massiah </em>proscribed admission in evidence of an accused’s statements obtained pursuant to the investigatory tactics used here. <em>Id., </em>at 1194-1195.</p>
</footnote>
<footnote label="4">
<p id="b466-10"> The trial judge found that <em>United States </em>v. <em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/" aria-description="Citation for case: United States v. Henry">Henry</a></span> </em>was distinguishable because the jailhouse informant in that case was paid for reporting the defendant’s statements to the police.</p>
</footnote>
<footnote label="5">
<p id="b467-6">Judge Van Graafeiland, dissenting, observed that the majority conceded that there had been no change in the law that had “transformed conduct that we formerly held to be constitutional into conduct that is now unconstitutional.” <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#749" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 749</a></span>. Thus, the majority’s rejection of the conclusion reached by the judges who previously had considered respondent’s claim was based on its refusal to accept the trial court’s factual determinations. <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#748" aria-description="Citation for case: Wilson v. Henderson"><em>Id., </em>at 748</a></span>. The dissent criticized the majority for disregarding “the presumption that the State court’s factual findings are correct, <span class="citation no-link">28 U. S. C. § 2254</span>(d), without an adequate explanation as to why the findings are not fairly supported by the record.” <span class="citation no-link"><em>Id., </em>at 749</span>. In Judge Van Graafeiland’s view, “[a] boilerplate statement that the ‘ends of justice’ <page-number citation-index="1" label="444">*444</page-number>justify reconsideration on the merits does not warrant rejection of all that has gone on before.” <em>Ibid, </em>(citations omitted).</p>
</footnote>
<footnote label="6">
<p id="b468-6"> The terms “successive petition” and “abuse of the writ” have distinct meanings. A “successive petition” raises grounds identical to those raised and rejected on the merits on a prior petition. See <em>Sanders </em>v. <em>United States, </em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#15" aria-description="Citation for case: Sanders v. United States">373 U. S., at 15-17</a></span>. Our decision today concerns the circumstances under which district courts properly should entertain the merits of such a petition. The concept of “abuse of the writ” is founded on the equitable nature of habeas corpus. Thus, where a prisoner files a petition raising grounds that were available but not relied upon in a prior petition, or engages in other conduct that “disentitle[s] him to the relief he seeks,” the federal court may dismiss the subsequent petition on the ground that the prisoner has abused the writ. <span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#17" aria-description="Citation for case: Sanders v. United States">Id., at 17-19</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b469-9"> The Judiciary Act of 1789, ch. 20, § 14, <span class="citation no-link">1 Stat. 81</span>, the first grant of jurisdiction to the federal courts, included authority to issue the writ of habeas corpus <em>ad subjiciendum </em>on behalf of federal prisoners. In 1867, Congress authorized the federal courts to grant habeas relief to persons in the custody of the States. Act of Feb. 5, 1867, ch. 28, § 1, <span class="citation no-link">14 Stat. 385</span>. See <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#474" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 474-475</a></span> (1976).</p>
</footnote>
<footnote label="8">
<p id="b472-8"> Contrary to the suggestion of Justice Brennan’s dissent, our cases deciding that federal habeas review ordinarily does not extend to procedurally defaulted claims plainly concern the “general scope of the writ.” <em>Post, </em>at 464. The point of those decisions is that, on balancing the competing interests implicated by affording federal collateral relief to persons in state custody, federal courts should not exercise habeas corpus jurisdiction over a certain category of constitutional claims, whether or not those claims are meritorious. Whether one characterizes those decisions as carving out an “exception” to federal habeas jurisdiction, as the dissent apparently prefers to do, <em>post, </em>at 465, n. 3, or as concerning the scope of that jurisdiction, the result is the same, and was reached under a framework of analysis that weighed the pertinent interests. Similarly, in <em>Fay </em>v. <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span>, </em>Justice Brennan’s opinion for the Court expressly made a “practical appraisal of the state interest” in a system of procedural forfeitures, weighing that interest against the other interests implicated by federal collateral review of procedurally defaulted claims. <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#433" aria-description="Citation for case: Fay v. Noia">372 U. S., at 433</a></span>. Of course, that the Court in <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span> </em>adopted an expansive reading <em>of </em>the scope of the writ does not undercut the fact that it did so by balancing competing interests.</p>
</footnote>
<footnote label="9">
<p id="b473-6"> In § 2244(a), which now governs successive petitions filed by federal prisoners, Congress preserved virtually intact the language of former § 2244, including the reference to the “ends of justice.”</p>
</footnote>
<footnote label="10">
<p id="b473-7"> Title <span class="citation no-link">28 U. S. C. § 2244</span>(b) provides:</p>
<p id="b473-8">“When after an evidentiary hearing on the merits of a material factual issue, or after a hearing on the merits of an issue of law, a person in custody pursuant to the judgment of a State court has been denied by a court of the United States or a justice or judge of the United States release from custody or other remedy on an application for a writ of habeas corpus, a subsequent application for a writ of habeas corpus in behalf of such person need not be entertained by a court of the United States or a justice or judge of the United States unless the application alleges and is predicated on a factual or other ground not adjudicated on the hearing of the earlier application for the writ, and unless the court, justice, or judge is satisfied that the applicant has not on the earlier application deliberately withheld the newly asserted ground or otherwise abused the writ.”</p>
</footnote>
<footnote label="11">
<p id="b473-9"> Sensitivity to the interests implicated by federal habeas corpus review is implicit in the statutory command that the federal courts “shall. . . dis<page-number citation-index="1" label="450">*450</page-number>pose of the matter as law <em>and justice </em>require.” <span class="citation no-link">28 U. S. C. § 2243</span> (emphasis added).</p>
</footnote>
<footnote label="12">
<p id="b474-6"> The Senate Report incorporates a letter from Senior Circuit Judge Orie L. Phillips to Senator Joseph D. Tydings that states:</p>
<p id="b474-7">“The need for this legislation... is demonstrated by the fact that the number of applications for writs of habeas corpus in Federal courts by State court prisoners increased from 134 in 1941 to 814 in 1957. In fiscal 1963, 1,692 applications for the writ were filed by State court prisoners; in fiscal 1964, 3,248 such applications were filed; in fiscal 1965, 4,845 such applications were filed; and in the first 9 months of fiscal 1966, 3,773 such applications were filed, yet less than 5 percent of such applications were decided by the Federal district courts in favor of the applicant for the writ. More than 95 percent were held to be without merit.” Senate Report, at 4, 5-6.</p>
<p id="b474-8">Since 1966, the burden imposed by applications for federal habeas corpus filed by state prisoners has continued to increase. In 1966, a total of 5,339 such applications was filed. In 1985, 8,534 applications were filed. Annual Report of the Director of the Administrative Office of the U. S. Courts (1985).</p>
</footnote>
<footnote label="13">
<p id="b475-6"> The Advisory Committee Note relies on the “ends of justice” inquiry described in <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>to identify the unusual case where a successive petition should be heard.</p>
</footnote>
<footnote label="14">
<p id="b477-4"> “Deterrence depends upon the expectation that ‘one violating the law will swiftly and certainly become subject to punishment, just punishment.”’ <em>Engle </em>v. <em>Isaac, </em><span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#127" aria-description="Citation for case: Engle v. Isaac">456 U. S. 107, 127-128, n. 32</a></span> (1982), quoting Bator, Finality in Criminal Law and Federal Habeas Corpus for State Prisoners, <span class="citation no-link">76 Harv. L. Rev. 441</span>, 452 (1963).</p>
</footnote>
<footnote label="15">
<p id="b477-5"> Where the prisoner secures his release on a successive petition, the delay between the crime and retrial following issuance of the writ often will be substantial. The delay in this case is illustrative. Respondent committed the robbery and murder in 1970, and was convicted in 1972. Direct appeal was completed in 1973. The intervening years have been largely consumed by federal habeas corpus review, with the past four years devoted to relitigation of respondent’s claim that admission in evidence of his statements to Lee violated the Sixth Amendment.</p>
</footnote>
<footnote label="16">
<p id="b477-6"> Finality serves other goals important to our system of criminal justice and to federalism. Unlimited availability of federal collateral attack burdens our criminal justice system as successive petitions divert the “time of judges, prosecutors, and lawyers” from the important task of trying criminal cases. Friendly, Is Innocence Irrelevant? Collateral Attack on Criminal Judgments, <span class="citation no-link">38 U. Chi. L. Rev. 142</span>, 148-149 (1970). See <em>Engle </em>v. <span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#127" aria-description="Citation for case: Engle v. Isaac"><em>Isaac, supra, </em>at 127</a></span>. Federal habeas review creates friction between our state and federal courts, as state judges — however able and thorough-know that their judgments may be set aside by a single federal judge, <page-number citation-index="1" label="454">*454</page-number>years after it was entered and affirmed on direct appeal. See <span class="citation" data-id="9428734"><a href="/opinion/110692/engle-v-isaac/#128" aria-description="Citation for case: Engle v. Isaac">456 U. S., at 128</a></span>. Moreover, under our federal system the States “possess primary authority for defining and enforcing the criminal law,” and “hold the initial responsibility for vindicating constitutional rights. Federal intrusions into state criminal trials frustrate both the States’ sovereign power to punish offenders and their good-faith attempts to honor constitutional rights.” <em>Ibid., </em>citing <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#263" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 263-265</a></span> (1983) (Powell, J., concurring). Despite those costs, Congress has continued to afford federal habeas relief in appropriate cases, “recognizing the need in a free society for an additional safeguard against compelling an innocent [person] to suffer an unconstitutional loss of liberty.” <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#491" aria-description="Citation for case: Stone v. Powell">428 U. S., at 491-492, n. 31</a></span>.</p>
</footnote>
<footnote label="17">
<p id="b478-7"> As Judge Friendly explained, a prisoner does not make a colorable showing of innocence “by showing that he might not, or even would not, have been convicted in the absence of evidence claimed to have been uncon<page-number citation-index="1" label="455">*455</page-number>stitutionally obtained.” Friendly, <em>supra, </em>at 160. Rather, the prisoner must “show a fair probability that, in light of all the evidence, including that alleged to have been illegally admitted (but with due regard to any unreliability of it) and evidence tenably claimed to have been wrongly excluded or to have become available only after the trial, the trier of the facts would have entertained a reasonable doubt of his guilt.” <em>Ibid, </em>(footnote omitted). Thus, the question whether the prisoner can make the requisite showing must be determined by reference to <em>all </em>probative evidence of guilt or innocence.</p>
</footnote>
<footnote label="18">
<p id="b479-7"> Justice Brennan’s dissenting opinion mischaracterizes our opinion in several respects. The dissent states that the plurality <em>“implies </em>that federal habeas review is not available as a matter of right to a prisoner who alleges in his <em>first </em>federal petition a properly preserved [constitutional claim].” <em>Post, </em>at 462 (emphasis added). This case involves, and our opinion describes, <em>only </em>the standard applicable to <em>successive </em>petitions for federal habeas corpus relief. Thus, the first six pages of the dissent have little, if any, relevance to this ease. There, Justice Brennan merely reiterates at length his views as to the general scope of federal habeas corpus jurisdiction, with no explanation of how those views apply when a district judge is required to consider a habeas corpus petition presenting an issue decided on the merits in a previous federal habeas proceeding.</p>
<p id="b479-8">The dissent further mistakenly asserts that we reject <em>Sanders’ </em>holding that the question whether successive review is proper should be decided under a ‘“sound discretion’ standard.” <em>Post, </em>at 462. As we have stated, the permissive language of § 2244(b) of course gives the federal courts discretion to decide whether to entertain a successive petition, and since <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>those courts have relied on the phrase “ends of justice” as a general standard for identifying cases in which successive review may be appropriate. What <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>left open — and the dissent today ignores —is the <page-number citation-index="1" label="456">*456</page-number>critieal question of what considerations should inform a court’s decision that successive review of an issue previously decided will serve the “ends of justice. ” While the dissent today purports to provide some substance to the <em><span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/" aria-description="Citation for case: Sanders v. United States">Sanders</a></span> </em>standard by requiring a “good justification” for relitigation of a claim previously decided, its standard provides no real guidance to federal courts confronted with successive claims for habeas corpus relief. As to the need for a standard, see <em>supra, </em>at 445.</p>
</footnote>
<footnote label="19">
<p id="b480-7"> In <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159</a></span> (1985), we again reserved this question, declining to reach the situation where the informant acts simply as a “ ‘listening post’ ” without “participating] in active conversation and prompting] particular replies.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#177" aria-description="Citation for case: Maine v. Moulton"><em>Id., </em>at 177, n. 13</a></span>.</p>
</footnote>
<footnote label="20">
<p id="b481-6"> The defendant in <em>Massiah </em>made the incriminating statements in a conversation with one of his confederates, who had secretly agreed to permit Government agents to listen to the conversation over a radio transmitter. The agents instructed the confederate to “engage Massiah in conversation relating to the alleged crimes.” <em>United States </em>v. <em>Massiah, </em><span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/#72" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d, at 72</a></span> (Hays, J., dissenting in part).</p>
</footnote>
<footnote label="21">
<p id="b482-6"> The Court observed, however, that where the defendant makes “[i]n-criminating statements pertaining to other crimes, as to which the Sixth Amendment right has not yet attached,” those statements “are, of course, admissible at a trial of those offenses.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#180" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 180, n. 16</a></span>.</p>
</footnote>
<footnote label="22">
<p id="b484-5"> Eyewitnesses had identified respondent as the man they saw fleeing from the garage with an armful of money.</p>
</footnote>
<footnote label="23">
<p id="b484-6"> The majority did not respond to Judge Van Graafeiland’s criticism that the court could not “dispense with the presumption that the State court’s factual findings are correct without an adequate explanation as to why the findings are not fairly supported by the record.” <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#749" aria-description="Citation for case: Wilson v. Henderson">742 F. 2d, at 749</a></span> (citations omitted).</p>
</footnote>
<footnote label="24">
<p id="b484-7"> Curiously, the Court of Appeals expressed concern that respondent was placed in a cell that overlooked the scene of his crimes. <span class="citation" data-id="8924313"><a href="/opinion/8934093/wilson-v-henderson/#745" aria-description="Citation for case: Wilson v. Henderson"><em>Id., </em>at 745</a></span>. For all the record shows, however, that fact was sheer coincidence. Nor do we perceive any reason to require police to isolate one charged with crime so that he cannot view the scene, whatever it may be, from his cell window.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Kyles v. Whitley.md  (`case`, 5 assertions)

### content_page

```
---
title: "Kyles v. Whitley"
type: case
citation: "514 U.S. 419 (1995)"
parallel_cite: "115 S. Ct. 1555; 131 L. Ed. 2d 490"
neutral_cite: 1995 U.S. LEXIS 2845
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-04-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-04-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kyles v. Whitley
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117923/kyles-v-whitley/"
  cluster_id: 117923
  opinion_id: 117923
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[United States v. Bagley]]", "[[Smith v. Cain]]"]
aliases: []
tags: ["case", "brady", "exculpatory-evidence", "materiality", "disclosure"]
holding: "Two load-bearing points: (1) materiality is assessed CUMULATIVELY — all suppressed evidence considered collectively, not item by item;…"
lake:
  record_id: Kyles v. Whitley
  status: verified
  projected_at: 2026-07-09
---

# Kyles v. Whitley

*514 U.S. 419 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Kyles was convicted of murder and sentenced to death after a trial at which the State withheld several pieces of favorable evidence — inconsistent eyewitness statements, the changing accounts of a key informant, and other impeachment and [[Brady and Giglio|exculpatory]] material, some of which was known only to the police. On [[Common Legal Terms#habeas-corpus|habeas]] review he argued the cumulative effect of the suppressed evidence undermined confidence in the verdict.

## Issue
Whether *[[Brady v. Maryland|Brady]]* materiality is assessed item-by-item or by the cumulative effect of all suppressed favorable evidence, and whether the prosecutor's disclosure duty extends to favorable evidence known only to the police.

## Rule
Materiality is cumulative, and the prosecutor's duty reaches the police: the State's "obligation under *Brady* v. *Maryland* . . . to disclose evidence favorable to the defense, turns on the cumulative effect of all such evidence suppressed by the government, and we hold that the prosecutor remains responsible for gauging that effect regardless of any failure by the police to bring favorable evidence to the prosecutor's attention." — 514 U.S. at 421. ^pin-421

The materiality standard is confidence-based, not a sufficiency or more-likely-than-not test: "The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in its absence he received a fair trial, understood as a trial resulting in a verdict worthy of confidence." — [*Id.* at 434](https://www.courtlistener.com/opinion/117923/kyles-v-whitley/#:~:text=The%20question%20is%20not%20whether). ^pin-434

## Application
The favorable evidence the State withheld in Kyles's case — the inconsistent and evolving statements of the eyewitnesses and the informant, and impeachment material some of which was known only to the investigating police — had to be considered collectively, with the prosecutor charged with knowledge of what the police knew. Viewed cumulatively, the suppressed evidence put the whole case in such a different light as to undermine confidence in the verdict, so its nondisclosure was material and Kyles was entitled to a new trial.

## Conclusion
The suppression of the cumulative favorable evidence violated *[[Brady v. Maryland|Brady]]*; the conviction and death sentence were reversed and the case [[Reading and Citing Cases#on-remand|remanded]] for a new trial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Kyles* refines [[Brady v. Maryland]] and [[United States v. Bagley]]: materiality is judged by the **cumulative** effect of all suppressed favorable evidence, and the individual prosecutor bears responsibility for favorable evidence known to others "acting on the government's behalf," including the police.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Kyles v. Whitley*, 514 U.S. 419 (1995) — https://www.courtlistener.com/opinion/117923/kyles-v-whitley/ — pinpoints: 421, 434.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c05f4b36762ca8b2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "514 U.S. 419 (1995)", "court": "U.S. Supreme Court", "neutral_cite": "1995 U.S. LEXIS 2845", "official_citation_present": true, "parallel_cite": "115 S. Ct. 1555; 131 L. Ed. 2d 490", "title": "Kyles v. Whitley", "year": "1995"}}
{"assertion_id": "a6b32cefa4838168", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Kyles v. Whitley"}}
{"assertion_id": "e27c343178afa1f2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Two load-bearing points: (1) materiality is assessed CUMULATIVELY — all suppressed evidence considered collectively, not item by item;…", "title": "Kyles v. Whitley"}}
{"assertion_id": "af8202d7c5b03b31", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kyles v. Whitley"}}
{"assertion_id": "e940f9e1f4d2f7ff", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1995-04-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kyles v. Whitley", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Kyles v. Whitley", "varies_by_point": "false"}}
```

### lake record — Kyles v. Whitley

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kyles v. Whitley",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kyles v. Whitley",
    "case_name_short": "Kyles",
    "case_name_full": "Kyles v. Whitley, Warden",
    "input_case_name": "Kyles v. Whitley",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-04-19",
    "year": 1995,
    "docket": null,
    "cluster_id": 117923,
    "lead_opinion_id": 117923,
    "sibling_ids": [
      117923,
      9433120,
      9433121,
      9433122
    ],
    "absolute_url": "/opinion/117923/kyles-v-whitley/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "514 U.S. 419",
      "volume": "514",
      "reporter": "U.S.",
      "page": "419",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 1555",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 490",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 2845",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "2845",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "514 U.S. 419",
        "volume": "514",
        "reporter": "U.S.",
        "page": "419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 1555",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "1555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 L. Ed. 2d 490",
        "volume": "131",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 2845",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "2845",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "514 U.S. 419",
    "official_selection": {
      "court_class": "scotus",
      "selected": "514 U.S. 419",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-421",
      "page": null,
      "quote": "--- # Kyles v. Whitley *514 U.S. 419 (1995)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Kyles was convicted of murder and sentenced to death after a trial at which the State withheld several pieces of favorable evidence \u2014 inconsistent eyewitness statements, the changing accounts of a key informant, and other impeachment and exculpatory material, some of which was known only to the police. On habeas review he argued the cumulative effect of the suppressed evidence undermined confidence in the verdict. ## Issue Whether *Brady* materiality is assessed item-by-item or by the cumulative effect of all suppressed favorable evidence, and whether the prosecutor's disclosure duty extends to favorable evidence known only to the police. ## Rule Materiality is cumulative, and the prosecutor's duty reaches the police: the State's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-434",
      "page": null,
      "quote": "The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in its absence he received a fair trial, understood as a trial resulting in a verdict worthy of confidence.",
      "star_marker": "434",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 31702,
      "fragment": "#:~:text=The%20question%20is%20not%20whether",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-04-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kyles v. Whitley",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Kyles v. Whitley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. Darrell J. Robinson v. Darrel Vannoy, Warden, Louisiana State Penitentiary, Angola, Louisiana",
          "cluster_id": 10292764,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. J. D. B.",
          "cluster_id": 10143633,
          "cite": [
            "326 Or. App. 237",
            "532 P.3d 99"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane1_negative"
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
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
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
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
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
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. California",
          "cluster_id": 127897,
          "cite": [
            "155 L. Ed. 2d 108",
            "123 S. Ct. 1179",
            "538 U.S. 11",
            "2003 U.S. LEXIS 1952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Kahled Burgos, United States of America v. Alexio Burnard Gobern",
          "cluster_id": 725510,
          "cite": [
            "94 F.3d 849",
            "1996 U.S. App. LEXIS 21911",
            "1996 WL 478498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Calderon v. Thompson",
          "cluster_id": 118202,
          "cite": [
            "140 L. Ed. 2d 728",
            "118 S. Ct. 1489",
            "523 U.S. 538",
            "1998 U.S. LEXIS 2964"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
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
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cavazos v. Smith",
          "cluster_id": 616357,
          "cite": [
            "181 L. Ed. 2d 311",
            "132 S. Ct. 2",
            "565 U.S. 1",
            "2011 U.S. LEXIS 7603",
            "2011 WL 5118826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guthrie",
          "cluster_id": 1375314,
          "cite": [
            "461 S.E.2d 163",
            "194 W. Va. 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fry v. Pliler",
          "cluster_id": 145720,
          "cite": [
            "168 L. Ed. 2d 16",
            "127 S. Ct. 2321",
            "551 U.S. 112",
            "2007 U.S. LEXIS 7715"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilbert Isgar",
          "cluster_id": 2649047,
          "cite": [
            "739 F.3d 829",
            "2014 WL 113433"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Osband",
          "cluster_id": 5607850,
          "cite": [
            "13 Cal. 4th 622",
            "919 P.2d 640",
            "96 Daily Journal DAR 9137",
            "96 Cal. Daily Op. Serv. 5583",
            "55 Cal. Rptr. 2d 26",
            "1996 Cal. LEXIS 3814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thomas",
          "cluster_id": 2629208,
          "cite": [
            "83 P.3d 970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lagrone v. State",
          "cluster_id": 1622023,
          "cite": [
            "942 S.W.2d 602",
            "1997 Tex. Crim. App. LEXIS 10",
            "1997 WL 43516"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Baltimore City State's Attorneys Office",
          "cluster_id": 2736472,
          "cite": [
            "767 F.3d 379",
            "2014 U.S. App. LEXIS 18294",
            "2014 WL 4723803"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glossip v. Gross",
          "cluster_id": 2812588,
          "cite": [
            "576 U.S. 863",
            "135 S. Ct. 2726",
            "192 L. Ed. 2d 761",
            "2015 U.S. LEXIS 4255",
            "83 U.S.L.W. 4656",
            "25 Fla. L. Weekly Fed. S 494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 6890210,
          "cite": [
            "95 Ohio St. 3d 181",
            "767 N.E.2d 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
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
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 844247,
          "cite": [
            "52 Cal. 4th 856",
            "261 P.3d 243",
            "131 Cal. Rptr. 3d 225",
            "2011 Cal. LEXIS 8769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 1969802,
          "cite": [
            "690 A.2d 1",
            "148 N.J. 89",
            "1997 N.J. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Spotz",
          "cluster_id": 2555770,
          "cite": [
            "18 A.3d 244",
            "610 Pa. 17",
            "2011 Pa. LEXIS 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blake v. State",
          "cluster_id": 9423249,
          "cite": [
            "485 Md. 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyles v. Whitley:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117923 OR 9433120 OR 9433121 OR 9433122) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjcyMTg1NjAwMDAwJnM9OTM1NTM2MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117923+OR+9433120+OR+9433121+OR+9433122%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(117923 OR 9433120 OR 9433121 OR 9433122)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NTgmcz0xNDExMzk0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117923+OR+9433120+OR+9433121+OR+9433122%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117923 OR 9433120 OR 9433121 OR 9433122)",
        "reviewed": 191,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 191,
        "triage_read": 5,
        "triage_snippet_classified": 186
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117923 OR 9433120 OR 9433121 OR 9433122)",
    "indexed_citing_opinions": 3464,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117923,
        "count": 2946,
        "count_source": "search"
      },
      {
        "opinion_id": 9433120,
        "count": 573,
        "count_source": "search"
      },
      {
        "opinion_id": 9433121,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433122,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6013,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kyles-v-whitley.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1MTEwMzYmcz0xMDY2NDI3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28117923+OR+9433120+OR+9433121+OR+9433122%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117923,
        "cited_id": 100655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 104321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 107083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 109693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 110382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 110496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 111957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 117899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 456348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 475335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 653644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 673496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 1152224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 1610706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117923,
        "cited_id": 1708963,
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
    "date_created": "2026-07-05T10:35:43Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:39:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:35:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kyles v. Whitley (truncated)

```
<div>
<center><b><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U.S. 419</a></span> (1995)</b></center>
<center><h1>KYLES<br>
v.<br>
WHITLEY, WARDEN</h1></center>
<center>No. 93-7927.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued November 7, 1994.</center>
<center>Decided April 19, 1995.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
<p><span class="star-pagination">*421</span> <span class="star-pagination">*421</span> Souter, J.,delivered the opinion of the Court,in which Stevens, O'Connor, Ginsburg, and Breyer, JJ.,joined. Stevens, J.,filed a concurring opinion, in which Ginsburg and Breyer, JJ.,joined,<i>post,</i>  p. 454.Scalia, J., filed a dissenting opinion, in which Rehnquist, C. J., and Kennedy and Thomas, JJ., joined, <i>post,</i> p. 456.</p>
<p><i>James S. Liebman</i> argued the cause for petitioner. On the briefs were <i>George W. Healy III, Nicholas J. Trenticosta, Denise Leboeuf,</i> and <i>Gerard A. Rault, Jr.</i> </p>
<p><i>Jack Peebles</i> argued the cause for respondent. With him on the brief was <i>Harry F. Connick.</i> </p>
<p>Justice Souter, delivered the opinion of the Court.</p>
<p>After his first trial in 1984 ended in a hung jury, petitioner Curtis Lee Kyles was tried again, convicted of first-degree murder, and sentenced to death. On habeas review, we follow the established rule that the state's obligation under <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), to disclose evidence favorable to the defense, turns on the cumulative effect of all such evidence suppressed by the government, and we hold that the prosecutor remains responsible for gauging that effect regardless of any failure by the police to bring favorable evidence to the prosecutor's attention. Because the net effect of the evidence withheld by the State in this case raises <span class="star-pagination">*422</span> a reasonable probability that its disclosure would have produced a different result, Kyles is entitled to a new trial.</p>
<p></p>
<h2>I</h2>
<p>Following the mistrial when the jury was unable to reach a verdict, Kyles's subsequent conviction and sentence of death were affirmed on direct appeal. <i>State</i> v. <i>Kyles,</i> <span class="citation" data-id="1708963"><a href="/opinion/1708963/state-v-kyles/" aria-description="Citation for case: State v. Kyles">513 So. 2d 265</a></span> (La. 1987), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./486/1027/">486 U. S. 1027</a></span> (1988). On state collateral review, the trial court denied relief, but the Supreme Court of Louisiana remanded for an evidentiary hearing on Kyles's claims of newly discovered evidence. During this state-court proceeding, the defense was first able to present certain evidence, favorable to Kyles, that the State had failed to disclose before or during trial. The state trial court nevertheless denied relief, and the State Supreme Court denied Kyles's application for discretionary review. <i>State ex rel. Kyles</i> v. <i>Butler,</i> <span class="citation" data-id="1152224"><a href="/opinion/1152224/state-ex-rel-kyles-v-butler/" aria-description="Citation for case: State Ex Rel. Kyles v. Butler">566 So. 2d 386</a></span> (La. 1990).</p>
<p>Kyles then filed a petition for habeas corpus in the United States District Court for the Eastern District of Louisiana, which denied the petition. The Court of Appeals for the Fifth Circuit affirmed by a divided vote. <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d 806</a></span> (1993). As we explain, <i>infra,</i> at 440-441, there is reason to question whether the Court of Appeals evaluated the significance of undisclosed evidence under the correct standard. Because "[o]ur duty to search for constitutional error with painstaking care is never more exacting than it is in a capital case," <i>Burger</i> v. <i>Kemp,</i> <span class="citation" data-id="9431130"><a href="/opinion/111957/burger-v-kemp/#785" aria-description="Citation for case: Burger v. Kemp">483 U. S. 776, 785</a></span> (1987),<sup>[1]</sup> we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./511/1051/">511 U. S. 1051</a></span> (1994), and now reverse.</p>
<p></p>
<h2>
<span class="star-pagination">*423</span> II</h2>
<p></p>
<h2>A</h2>
<p>The record indicates that, at about 2:20 p.m. on Thursday, September 20, 1984, 60-year-old Dolores Dye left the Schwegmann Brothers' store (Schwegmann's) on Old Gentilly Road in New Orleans after doing some food shopping. As she put her grocery bags into the trunk of her red Ford LTD, a man accosted her and after a short struggle drew a revolver, fired into her left temple, and killed her. The gunman took Dye's keys and drove away in the LTD.</p>
<p>New Orleans police took statements from six eyewitnesses,<sup>[2]</sup> who offered various descriptions of the gunman. They agreed that he was a black man, and four of them said that he had braided hair. The witnesses differed significantly, however, in their descriptions of height, age, weight, build, and hair length. Two reported seeing a man of 17 or 18, while another described the gunman as looking as old as 28. One witness described him as 5'4" or 5'5", medium build, 140-150 pounds; another described the man as slim and close to six feet. One witness said he had a mustache; none of the others spoke of any facial hair at all. One witness said the murderer had shoulder-length hair; another described the hair as "short."</p>
<p>Since the police believed the killer might have driven his own car to Schwegmann's and left it there when he drove off in Dye's LTD, they recorded the license numbers of the cars remaining in the parking lots around the store at 9:15 p.m. on the evening of the murder. Matching these numbers with registration records produced the names and addresses of the owners of the cars, with a notation of any owner's police <span class="star-pagination">*424</span> record. Despite this list and the eyewitness descriptions, the police had no lead to the gunman until the Saturday evening after the shooting.</p>
<p>At 5:30 p.m., on September 22, a man identifying himself as James Joseph called the police and reported that on the day of the murder he had bought a red Thunderbird from a friend named Curtis, whom he later identified as petitioner, Curtis Kyles. He said that he had subsequently read about Dye's murder in the newspapers and feared that the car he purchased was the victim's. He agreed to meet with the police.</p>
<p>A few hours later, the informant met New Orleans Detective John Miller, who was wired with a hidden body microphone, through which the ensuing conversation was recorded. See App. 221-257 (transcript). The informant now said his name was Joseph Banks and that he was called Beanie. His actual name was Joseph Wallace.<sup>[3]</sup></p>
<p>His story, as well as his name, had changed since his earlier call. In place of his original account of buying a Thunderbird from Kyles on Thursday, Beanie told Miller that he had not seen Kyles at all on Thursday, <i>id.,</i> at 249 250, and had bought a red LTD the previous day, Friday, <i>id.,</i>  at 221-222, 225. Beanie led Miller to the parking lot of a nearby bar, where he had left the red LTD, later identified as Dye's.</p>
<p>Beanie told Miller that he lived with Kyles's brother-in-law (later identified as Johnny Burns),<sup>[4]</sup> whom Beanie repeatedly called his "partner." <i>Id.,</i> at 221. Beanie described Kyles as slim, about 6-feet tall, 24 or 25 years old, with a "bush" hairstyle. <i>Id.,</i> at 226, 252. When asked if Kyles ever wore <span class="star-pagination">*425</span> his hair in plaits, Beanie said that he did but that he "had a bush" when Beanie bought the car. <i>Id.,</i> at 249.</p>
<p>During the conversation, Beanie repeatedly expressed concern that he might himself be a suspect in the murder. He explained that he had been seen driving Dye's car on Friday evening in the French Quarter, admitted that he had changed its license plates, and worried that he "could have been charged" with the murder on the basis of his possession of the LTD. <i>Id.,</i> at 231, 246, 250. He asked if he would be put in jail. <i>Id.,</i> at 235, 246. Miller acknowledged that Beanie's possession of the car would have looked suspicious, <i>id.,</i> at 247, but reassured him that he "didn't do anything wrong," <i>id.,</i> at 235.</p>
<p>Beanie seemed eager to cast suspicion on Kyles, who allegedly made his living by "robbing people," and had tried to kill Beanie at some prior time. <i>Id.,</i> at 228, 245, 251. Beanie said that Kyles regularly carried two pistols, a .38 and a .32, and that if the police could "set him up good," they could "get that same gun" used to kill Dye. <i>Id.,</i> at 228-229. Beanie rode with Miller and Miller's supervisor, Sgt. James Eaton, in an unmarked squad car to Desire Street, where he pointed out the building containing Kyles's apartment. <i>Id.,</i>  at 244-246.</p>
<p>Beanie told the officers that after he bought the car, he and his "partner" (Burns) drove Kyles to Schwegmann's about 9 p.m. on Friday evening to pick up Kyles's car, described as an orange four-door Ford.<sup>[5]</sup><i>Id.,</i> at 221, 223, 231-232, 242. When asked where Kyles's car had been parked, Beanie replied that it had been "[o]n the same side [of the lot] where the woman was killed at." <i>Id.,</i> at 231. The officers later drove Beanie to Schwegmann's, where he indicated the space where he claimed Kyles's car had been parked. Beanie went on to say that when he and Burns had brought Kyles to pick <span class="star-pagination">*426</span> up the car, Kyles had gone to some nearby bushes to retrieve a brown purse, <i>id.,</i> at 253-255, which Kyles subsequently hid in a wardrobe at his apartment. Beanie said that Kyles had "a lot of groceries" in Schwegmann's bags and a new baby's potty "in the car." <i>Id.,</i> at 254-255. Beanie told Eaton that Kyles's garbage would go out the next day and that if Kyles was "smart" he would "put [the purse] in [the] garbage." <i>Id.,</i> at 257. Beanie made it clear that he expected some reward for his help, saying at one point that he was not "doing all of this for nothing." <i>Id.,</i> at 246. The police repeatedly assured Beanie that he would not lose the $400 he paid for the car. <i>Id.,</i> at 243, 246.</p>
<p>After the visit to Schwegmann's, Eaton and Miller took Beanie to a police station where Miller interviewed him again on the record, which was transcribed and signed by Beanie, using his alias "Joseph Banks." See <i>id.,</i> at 214-220. This statement, Beanie's third (the telephone call being the first, then the recorded conversation), repeats some of the essentials of the second one: that Beanie had purchased a red Ford LTD from Kyles for $400 on Friday evening; that Kyles had his hair "combed out" at the time of the sale; and that Kyles carried a .32 and a .38 with him "all the time."</p>
<p>Portions of the third statement, however, embellished or contradicted Beanie's preceding story and were even internally inconsistent. Beanie reported that after the sale, he and Kyles unloaded Schwegmann's grocery bags from the trunk and back seat of the LTD and placed them in Kyles's own car. Beanie said that Kyles took a brown purse from the front seat of the LTD and that they then drove in separate cars to Kyles's apartment, where they unloaded the groceries. <i>Id.,</i> at 216-217. Beanie also claimed that, a few hours later, he and his "partner" Burns went with Kyles to Schwegmann's, where they recovered Kyles's car and a "big brown pocket book" from "next to a building." <i>Id.,</i> at 218. Beanie did not explain how Kyles could have picked up his car and recovered the purse at Schwegmann's, after Beanie <span class="star-pagination">*427</span> had seen Kyles with both just a few hours earlier. The police neither noted the inconsistencies nor questioned Beanie about them.</p>
<p>Although the police did not thereafter put Kyles under surveillance, Tr. 94 (Dec. 6, 1984), they learned about events at his apartment from Beanie, who went there twice on Sunday. According to a fourth statement by Beanie, this one given to the chief prosecutor in November (between the first and second trials), he first went to the apartment about 2 p.m., after a telephone conversation with a police officer who asked whether Kyles had the gun that was used to kill Dye. Beanie stayed in Kyles's apartment until about 5 p.m., when he left to call Detective John Miller. Then he returned about 7 p.m. and stayed until about 9:30 p.m., when he left to meet Miller, who also asked about the gun. According to this fourth statement, Beanie "rode around" with Miller until 3 a.m. on Monday, September 24. Sometime during those same early morning hours, detectives were sent at Sgt. Eaton's behest to pick up the rubbish outside Kyles's building. As Sgt. Eaton wrote in an inter office memorandum, he had "reason to believe the victims <i>[sic]</i> personal papers and the Schwegmann's bags will be in the trash." Record, Defendant's Exh. 17.</p>
<p>At 10:40 a.m., Kyles was arrested as he left the apartment, which was then searched under a warrant. Behind the kitchen stove, the police found a .32-caliber revolver containing five live rounds and one spent cartridge. Ballistics tests later showed that this pistol was used to murder Dye. In a wardrobe in a hallway leading to the kitchen, the officers found a homemade shoulder holster that fit the murder weapon. In a bedroom dresser drawer, they discovered two boxes of ammunition, one containing several .32-caliber rounds of the same brand as those found in the pistol. Back in the kitchen, various cans of cat and dog food, some of them of the brands Dye typically purchased, were found in Schwegmann's sacks. No other groceries were identified as <span class="star-pagination">*428</span> possibly being Dye's, and no potty was found. Later that afternoon at the police station, police opened the rubbish bags and found the victim's purse, identification, and other personal belongings wrapped in a Schwegmann's sack.</p>
<p>The gun, the LTD, the purse, and the cans of pet food were dusted for fingerprints. The gun had been wiped clean. Several prints were found on the purse and on the LTD, but none was identified as Kyles's. Dye's prints were not found on any of the cans of pet food. Kyles's prints were found, however, on a small piece of paper taken from the front passenger-side floorboard of the LTD. The crime laboratory recorded the paper as a Schwegmann's sales slip, but without noting what had been printed on it, which was obliterated in the chemical process of lifting the fingerprints. A second Schwegmann's receipt was found in the trunk of the LTD, but Kyles's prints were not found on it. Beanie's fingerprints were not compared to any of the fingerprints found. Tr. 97 (Dec. 6, 1984).</p>
<p>The lead detective on the case, John Dillman, put together a photo lineup that included a photograph of Kyles (but not of Beanie) and showed the array to five of the six eyewitnesses who had given statements. Three of them picked the photograph of Kyles; the other two could not confidently identify Kyles as Dye's assailant.</p>
<p></p>
<h2>B</h2>
<p>Kyles was indicted for first-degree murder. Before trial, his counsel filed a lengthy motion for disclosure by the State of any exculpatory or impeachment evidence. The prosecution responded that there was "no exculpatory evidence of any nature," despite the government's knowledge of the following evidentiary items: (1) the six contemporaneous eyewitness statements taken by police following the murder; (2) records of Beanie's initial call to the police; (3) the tape recording of the Saturday conversation between Beanie and officers Eaton and Miller; (4) the typed and signed statement <span class="star-pagination">*429</span> given by Beanie on Sunday morning; (5) the computer printout of license numbers of cars parked at Schwegmann's on the night of the murder, which did not list the number of Kyles's car; (6) the internal police memorandum calling for the seizure of the rubbish after Beanie had suggested that the purse might be found there; and (7) evidence linking Beanie to other crimes at Schwegmann's and to the unrelated murder of one Patricia Leidenheimer, committed in January before the Dye murder.</p>
<p>At the first trial, in November, the heart of the State's case was eyewitness testimony from four people who were at the scene of the crime (three of whom had previously picked Kyles from the photo lineup). Kyles maintained his innocence, offered supporting witnesses, and supplied an alibi that he had been picking up his children from school at the time of the murder. The theory of the defense was that Kyles had been framed by Beanie, who had planted evidence in Kyles's apartment and his rubbish for the purposes of shifting suspicion away from himself, removing an impediment to romance with Pinky Burns, and obtaining reward money. Beanie did not testify as a witness for either the defense or the prosecution.</p>
<p>Because the State withheld evidence, its case was much stronger, and the defense case much weaker, than the full facts would have suggested. Even so, after four hours of deliberation, the jury became deadlocked on the issue of guilt, and a mistrial was declared.</p>
<p>After the mistrial, the chief trial prosecutor, Cliff Strider, interviewed Beanie. See App. 258-262 (notes of interview). Strider's notes show that Beanie again changed important elements of his story. He said that he went with Kyles to retrieve Kyles's car from the Schwegmann's lot on Thursday, the day of the murder, at some time between 5 and 7:30 p.m., not on Friday, at 9 p.m., as he had said in his second and third statements. (Indeed, in his second statement, Beanie said that he had not seen Kyles at all on Thursday. <i>Id.,</i> at <span class="star-pagination">*430</span> 249-250.) He also said, for the first time, that when they had picked up the car they were accompanied not only by Johnny Burns but also by Kevin Black, who had testified for the defense at the first trial. Beanie now claimed that after getting Kyles's car they went to Black's house, retrieved a number of bags of groceries, a child's potty, and a brown purse, all of which they took to Kyles's apartment. Beanie also stated that on the Sunday after the murder he had been at Kyles's apartment two separate times. Notwithstanding the many inconsistencies and variations among Beanie's statements, neither Strider's notes nor any of the other notes and transcripts were given to the defense.</p>
<p>In December 1984, Kyles was tried a second time. Again, the heart of the State's case was the testimony of four eyewitnesses who positively identified Kyles in front of the jury. The prosecution also offered a blown-up photograph taken at the crime scene soon after the murder, on the basis of which the prosecutors argued that a seemingly two-toned car in the background of the photograph was Kyles's. They repeatedly suggested during cross-examination of defense witnesses that Kyles had left his own car at Schwegmann's on the day of the murder and had retrieved it later, a theory for which they offered no evidence beyond the blown-up photograph. Once again, Beanie did not testify.</p>
<p>As in the first trial, the defense contended that the eyewitnesses were mistaken. Kyles's counsel called several individuals, including Kevin Black, who testified to seeing Beanie, with his hair in plaits, driving a red car similar to the victim's about an hour after the killing. Tr. 209 (Dec. 7, 1984). Another witness testified that Beanie, with his hair in braids, had tried to sell him the car on Thursday evening, shortly after the murder. <i>Id.,</i> at 234-235. Another witness testified that Beanie, with his hair in a "Jheri curl," had attempted to sell him the car on Friday. <i>Id.,</i> at 249-251. One witness, Beanie's "partner," Burns, testified that he had seen Beanie on Sunday at Kyles's apartment, stooping down near <span class="star-pagination">*431</span> the stove where the gun was eventually found, and the defense presented testimony that Beanie was romantically interested in Pinky Burns. To explain the pet food found in Kyles's apartment, there was testimony that Kyles's family kept a dog and cat and often fed stray animals in the neighborhood.</p>
<p>Finally, Kyles again took the stand. Denying any involvement in the shooting, he explained his fingerprints on the cash register receipt found in Dye's car by saying that Beanie had picked him up in a red car on Friday, September 21, and had taken him to Schwegmann's, where he purchased transmission fluid and a pack of cigarettes. He suggested that the receipt may have fallen from the bag when he removed the cigarettes.</p>
<p>On rebuttal, the prosecutor had Beanie brought into the courtroom. All of the testifying eyewitnesses, after viewing Beanie standing next to Kyles, reaffirmed their previous identifications of Kyles as the murderer. Kyles was convicted of first-degree murder and sentenced to death. Beanie received a total of $1,600 in reward money. See Tr. of Hearing on Post-Conviction Relief 19-20 (Feb. 24, 1989); <i>id.,</i> at 114 (Feb. 20, 1989).</p>
<p>Following direct appeal, it was revealed in the course of state collateral review that the State had failed to disclose evidence favorable to the defense. After exhausting state remedies, Kyles sought relief on federal habeas, claiming, among other things, that the evidence withheld was material to his defense and that his conviction was thus obtained in violation of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i> Although the United States District Court denied relief and the Fifth Circuit affirmed,<sup>[6]</sup> Judge <span class="star-pagination">*432</span> King dissented, writing that "[f]or the first time in my fourteen years on this court . . . I have serious reservations about whether the State has sentenced to death the right man." <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#820" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 820</a></span>.</p>
<p></p>
<h2>III</h2>
<p>The prosecution's affirmative duty to disclose evidence favorable to a defendant can trace its origins to early 20thcentury strictures against misrepresentation and is of course most prominently associated with this Court's decision in <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963). See <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#86" aria-description="Citation for case: Brady v. Maryland"><i>id.,</i> at 86</a></span> (relying on <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935), and <i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/#215" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213, 215-216</a></span> (1942)). <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> held "that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>; see <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786</a></span>, 794-795 <span class="star-pagination">*433</span> (1972). In <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), however, it became clear that a defendant's failure to request favorable evidence did not leave the Government free of all obligation. There, the Court distinguished three situations in which a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim might arise: first, where previously undisclosed evidence revealed that the prosecution introduced trial testimony that it knew or should have known was perjured, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U. S., at 103-104</a></span>;<sup>[7]</sup> second, where the Government failed to accede to a defense request for disclosure of some specific kind of exculpatory evidence, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs"><i>id.,</i> at 104-107</a></span>; and third, where the Government failed to volunteer exculpatory evidence never requested, or requested only in a general way. The Court found a duty on the part of the Government even in this last situation, though only when suppression of the evidence would be "of sufficient significance to result in the denial of the defendant's right to a fair trial." <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs"><i>Id.,</i> at 108</a></span>.</p>
<p>In the third prominent case on the way to current <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  law, <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">473 U. S. 667</a></span> (1985), the Court disavowed any difference between exculpatory and impeachment evidence for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes, and it abandoned the distinction between the second and third <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span></i> circumstances, <i>i. e.,</i> the "specific-request" and "general- or no-request" situations. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> held that regardless of request, favorable evidence is material, and constitutional error results from its suppression by the government, "if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different." <span class="star-pagination">*434</span> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U. S., at 682</a></span> (opinion of Blackmun, J.); <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#685" aria-description="Citation for case: United States v. Bagley"><i>id.,</i> at 685</a></span> (White, J., concurring in part and concurring in judgment).</p>
<p>Four aspects of materiality under <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> bear emphasis. Although the constitutional duty is triggered by the potential impact of favorable but undisclosed evidence, a showing of materiality does not require demonstration by a preponderance that disclosure of the suppressed evidence would have resulted ultimately in the defendant's acquittal (whether based on the presence of reasonable doubt or acceptance of an explanation for the crime that does not inculpate the defendant). <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley"><i>Id.,</i> at 682</a></span> (opinion of Blackmun, J.) (adopting formulation announced in <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668, 694</a></span> (1984)); <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#685" aria-description="Citation for case: United States v. Bagley"><i>Bagley, supra,</i> at 685</a></span> (White, J., concurring in part and concurring in judgment) (same); see <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#680" aria-description="Citation for case: United States v. Bagley">473 U. S., at 680</a></span> (opinion of Blackmun, J.) (<span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs"><i>Agurs</i></a></span> "rejected a standard that would require the defendant to demonstrate that the evidence if disclosed probably would have resulted in acquittal"); cf. <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#693" aria-description="Citation for case: Strickland v. Washington"><i>Strickland, supra,</i> at 693</a></span> ("[W]e believe that a defendant need not show that counsel's deficient conduct more likely than not altered the outcome in the case"); <i>Nix</i> v. <i>Whiteside,</i> <span class="citation" data-id="9430360"><a href="/opinion/111603/nix-v-whiteside/#175" aria-description="Citation for case: Nix v. Whiteside">475 U. S. 157, 175</a></span> (1986) ("[A] defendant need not establish that the attorney's deficient performance more likely than not altered the outcome in order to establish prejudice under <i>Strickland</i> "). <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> `s touchstone of materiality is a "reasonable probability" of a different result, and the adjective is important. The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in its absence he received a fair trial, understood as a trial resulting in a verdict worthy of confidence. A "reasonable probability" of a different result is accordingly shown when the government's evidentiary suppression "undermines confidence in the outcome of the trial." <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U. S., at 678</a></span>.</p>
<p>The second aspect of <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> materiality bearing emphasis here is that it is not a sufficiency of evidence test. A defendant need not demonstrate that after discounting the inculpatory <span class="star-pagination">*435</span> evidence in light of the undisclosed evidence, there would not have been enough left to convict. The possibility of an acquittal on a criminal charge does not imply an insufficient evidentiary basis to convict. One does not show a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation by demonstrating that some of the inculpatory evidence should have been excluded, but by showing that the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict.<sup>[8]</sup></p>
<p>Third, we note that, contrary to the assumption made by the Court of Appeals, <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#818" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 818</a></span>, once a reviewing court applying <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> has found constitutional error there is no need for further harmless-error review. Assuming, <i>arguendo,</i> that a harmless-error enquiry were to apply, a <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i>  error could not be treated as harmless, since "a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different," <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U. S., at 682</a></span> (opinion of Blackmun, J.); <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#685" aria-description="Citation for case: United States v. Bagley"><i>id.,</i> at 685</a></span> (White, J., concurring in part and concurring in judgment), necessarily entails the conclusion that the suppression must have had "`substantial and injurious effect or influence in determining the jury's verdict,' " <i>Brecht</i> v. <i>Abrahamson,</i> <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#623" aria-description="Citation for case: Brecht v. Abrahamson">507 U. S. 619, 623</a></span> (1993), quoting <i>Kotteakos</i> v. <i>United States,</i> <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#776" aria-description="Citation for case: Kotteakos v. United States">328 U. S. 750, 776</a></span> (1946). This is amply confirmed by the development of the respective governing standards. Although <span class="star-pagination">*436</span> <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span> (1967), held that a conviction tainted by constitutional error must be set aside unless the error complained of "was harmless beyond a reasonable doubt," we held in <i><span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">Brecht</a></span></i> that the standard of harmlessness generally to be applied in habeas cases is the <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span></i> formulation (previously applicable only in reviewing nonconstitutional errors on direct appeal), <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#622" aria-description="Citation for case: Brecht v. Abrahamson"><i>Brecht, supra,</i> at 622-623</a></span>. Under <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span></i> a conviction may be set aside only if the error "had substantial and injurious effect or influence in determining the jury's verdict." <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#776" aria-description="Citation for case: Kotteakos v. United States"><i>Kotteakos, supra,</i> at 776</a></span>. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>,</i> however, had previously rejected <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span></i> as the standard governing constitutional disclosure claims, reasoning that "the constitutional standard of materiality must impose a higher burden on the defendant." <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span>. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span></i> thus opted for its formulation of materiality, later adopted as the test for prejudice in <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span>,</i> only after expressly noting that this standard would recognize reversible constitutional error only when the harm to the defendant was greater than the harm sufficient for reversal under <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span>.</i> In sum, once there has been <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> error as claimed in this case, it cannot subsequently be found harmless under <i><span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">Brecht</a></span>.</i><sup>[9]</sup></p>
<p>The fourth and final aspect of <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> materiality to be stressed here is its definition in terms of suppressed evidence considered collectively, not item by item.<sup>[10]</sup> As Justice Blackmun emphasized in the portion of his opinion written for the Court, the Constitution is not violated every time the <span class="star-pagination">*437</span> government fails or chooses not to disclose evidence that might prove helpful to the defense. <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#675" aria-description="Citation for case: United States v. Bagley">473 U. S., at 675</a></span>, and n. 7. We have never held that the Constitution demands an open file policy (however such a policy might work out in practice), and the rule in <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> (and, hence, in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> ) requires less of the prosecution than the ABA Standards for Criminal Justice, which call generally for prosecutorial disclosures of any evidence tending to exculpate or mitigate. See ABA Standards for Criminal Justice, Prosecution Function and Defense Function 3-3.11(a) (3d ed. 1993) ("A prosecutor should not intentionally fail to make timely disclosure to the defense, at the earliest feasible opportunity, of the existence of all evidence or information which tends to negate the guilt of the accused or mitigate the offense charged or which would tend to reduce the punishment of the accused"); ABA Model Rule of Professional Conduct 3.8(d) (1984) ("The prosecutor in a criminal case shall . . . make timely disclosure to the defense of all evidence or information known to the prosecutor that tends to negate the guilt of the accused or mitigates the offense").</p>
<p>While the definition of <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> materiality in terms of the cumulative effect of suppression must accordingly be seen as leaving the government with a degree of discretion, it must also be understood as imposing a corresponding burden. On the one side, showing that the prosecution knew of an item of favorable evidence unknown to the defense does not amount to a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation, without more. But the prosecution, which alone can know what is undisclosed, must be assigned the consequent responsibility to gauge the likely net effect of all such evidence and make disclosure when the point of "reasonable probability" is reached. This in turn means that the individual prosecutor has a duty to learn of any favorable evidence known to the others acting on the government's behalf in the case, including the police. But whether the prosecutor succeeds or fails in meeting this obligation (whether, that is, a failure to disclose is in good faith <span class="star-pagination">*438</span> or bad faith, see <i>Brady,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>), the prosecution's responsibility for failing to disclose known, favorable evidence rising to a material level of importance is inescapable.</p>
<p>The State of Louisiana would prefer an even more lenient rule. It pleads that some of the favorable evidence in issue here was not disclosed even to the prosecutor until after trial, Brief for Respondent 25, 27, 30, 31, and it suggested below that it should not be held accountable under <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i>  and <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> for evidence known only to police investigators and not to the prosecutor.<sup>[11]</sup> To accommodate the State in this manner would, however, amount to a serious change of course from the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> line of cases. In the State's favor it may be said that no one doubts that police investigators sometimes fail to inform a prosecutor of all they know. But neither is there any serious doubt that "procedures and regulations can be established to carry [the prosecutor's] burden and to insure communication of all relevant information on each case to every lawyer who deals with it." <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972). Since, then, the prosecutor has the means to discharge the government's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> responsibility if he will, any argument for excusing a prosecutor from disclosing what he does not happen to know about boils down to a plea to substitute the police for the prosecutor, and even for the courts themselves, as the final arbiters of the government's obligation to ensure fair trials.</p>
<p>Short of doing that, we were asked at oral argument to raise the threshold of materiality because the <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> standard "makes it difficult . . . to know" from the "perspective [of the prosecutor at] trial . . . exactly what might become important later on." Tr. of Oral Arg. 33. The State asks for "a certain amount of leeway in making a judgment call" as to the disclosure of any given piece of evidence. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Ibid.</a></span></i> </p>
<p><span class="star-pagination">*439</span> Uncertainty about the degree of further "leeway" that might satisfy the State's request for a "certain amount" of it is the least of the reasons to deny the request. At bottom, what the State fails to recognize is that, with or without more leeway, the prosecution cannot be subject to any disclosure obligation without at some point having the responsibility to determine when it must act. Indeed, even if due process were thought to be violated by every failure to disclose an item of exculpatory or impeachment evidence (leaving harmless error as the government's only fallback), the prosecutor would still be forced to make judgment calls about what would count as favorable evidence, owing to the very fact that the character of a piece of evidence as favorable will often turn on the context of the existing or potential evidentiary record. Since the prosecutor would have to exercise some judgment even if the State were subject to this most stringent disclosure obligation, it is hard to find merit in the State's complaint over the responsibility for judgment under the existing system, which does not tax the prosecutor with error for any failure to disclose, absent a further showing of materiality. Unless, indeed, the adversary system of prosecution is to descend to a gladiatorial level unmitigated by any prosecutorial obligation for the sake of truth, the government simply cannot avoid responsibility for knowing when the suppression of evidence has come to portend such an effect on a trial's outcome as to destroy confidence in its result.</p>
<p>This means, naturally, that a prosecutor anxious about tacking too close to the wind will disclose a favorable piece of evidence. See <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs">427 U. S., at 108</a></span> ("[T]he prudent prosecutor will resolve doubtful questions in favor of disclosure"). This is as it should be. Such disclosure will serve to justify trust in the prosecutor as "the representative . . . of a sovereignty . . . whose interest . . . in a criminal prosecution is not that it shall win a case, but that justice shall be done." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935). <span class="star-pagination">*440</span> And it will tend to preserve the criminal trial, as distinct from the prosecutor's private deliberations, as the chosen forum for ascertaining the truth about criminal accusations. See <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark">478 U. S. 570, 577-578</a></span> (1986); <i>Estes</i> v. <i>Texas,</i> <span class="citation" data-id="9423071"><a href="/opinion/107083/estes-v-texas/#540" aria-description="Citation for case: Estes v. Texas">381 U. S. 532, 540</a></span> (1965); <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#900" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 900-901</a></span> (1984) (recognizing general goal of establishing "procedures under which criminal defendants are `acquitted or convicted on the basis of all the evidence which exposes the truth' " (quoting <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175</a></span> (1969)). The prudence of the careful prosecutor should not therefore be discouraged.</p>
<p>There is room to debate whether the two judges in the majority in the Court of Appeals made an assessment of the cumulative effect of the evidence. Although the majority's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> discussion concludes with the statement that the court was not persuaded of the reasonable probability that Kyles would have obtained a favorable verdict if the jury had been "exposed to any or all of the undisclosed materials," <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#817" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 817</a></span>, the opinion also contains repeated references dismissing particular items of evidence as immaterial and so suggesting that cumulative materiality was not the touchstone. See, <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#812" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana..."><i>e. g., id.,</i> at 812</a></span> ("We do not agree that this statement made the transcript material and so mandated disclosure . . . . Beanie's statement . . . is itself not decisive"), 814 ("The nondisclosure of this much of the transcript was insignificant"), 815 ("Kyles has not shown on this basis that the three statements were material"), 815 ("In light of the entire record . . . we cannot conclude that [police reports relating to discovery of the purse in the trash] would, in reasonable probability, have moved the jury to embrace the theory it otherwise discounted"), 816 ("We are not persuaded that these notes [relating to discovery of the gun] were material"), 816 ("[W]e are not persuaded that [the printout of the license plate numbers] would, in reasonable probability, have induced reasonable doubt where the jury did not find it. . . . the rebuttal of the photograph would have made no difference"). <span class="star-pagination">*441</span> The result reached by the Fifth Circuit majority is compatible with a series of independent materiality evaluations, rather than the cumulative evaluation required by <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span>,</i> as the ensuing discussion will show.</p>
<p></p>
<h2>IV</h2>
<p>In this case, disclosure of the suppressed evidence to competent counsel would have made a different result reasonably probable.</p>
<p></p>
<h2>A</h2>
<p>As the District Court put it, "the essence of the State's case" was the testimony of eyewitnesses, who identified Kyles as Dye's killer. <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#853" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 853</a></span> (Appendix A). Disclosure of their statements would have resulted in a markedly weaker case for the prosecution and a markedly stronger one for the defense. To begin with, the value of two of those witnesses would have been substantially reduced or destroyed.</p>
<p>The State rated Henry Williams as its best witness, who testified that he had seen the struggle and the actual shooting by Kyles. The jury would have found it helpful to probe this conclusion in the light of Williams's contemporaneous statement, in which he told the police that the assailant was "a black male, about 19 or 20 years old, about 5'4" or 5'5", 140 to 150 pounds, medium build" and that "his hair looked like it was platted." App. 197. If cross-examined on this description, Williams would have had trouble explaining how he could have described Kyles, 6-feet tall and thin, as a man more than half a foot shorter with a medium build.<sup>[12]</sup> Indeed, since Beanie was 22 years old, 5'5" tall, and 159 pounds, <span class="star-pagination">*442</span> the defense would have had a compelling argument that Williams's description pointed to Beanie but not to Kyles.<sup>[13]</sup></p>
<p>The trial testimony of a second eyewitness, Isaac Smallwood, was equally damning to Kyles. He testified that Kyles was the assailant, and that he saw him struggle with Dye. He said he saw Kyles take a ".32, a small black gun" out of his right pocket, shoot Dye in the head, and drive off in her LTD. When the prosecutor asked him whether he actually saw Kyles shoot Dye, Smallwood answered "Yeah." Tr. 41-48 (Dec. 6, 1984).</p>
<p>Smallwood's statement taken at the parking lot, however, was vastly different. Immediately after the crime, Smallwood <span class="star-pagination">*443</span> claimed that he had not seen the actual murder and had not seen the assailant outside the vehicle. "I heard a lound [sic]pop," he said. "When I looked around I saw a lady laying on the ground, and there was a red car coming toward me." App. 189. Smallwood said that he got a look at the culprit, a black teenage male with a mustache and shoulder-length braided hair, as the victim's red Thunderbird passed where he was standing. When a police investigator specifically asked him whether he had seen the assailant outside the car, Smallwood answered that he had not; the gunman "was already in the car and coming toward me." <i>Id.,</i> at 188-190.</p>
<p>A jury would reasonably have been troubled by the adjustments to Smallwood's original story by the time of the second trial. The struggle and shooting, which earlier he had not seen, he was able to describe with such detailed clarity as to identify the murder weapon as a small black .32-caliber pistol, which, of course, was the type of weapon used. His description of the victim's car had gone from a "Thunderbird" to an "LTD"; and he saw fit to say nothing about the assailant's shoulder-length hair and moustache, details noted by no other eyewitness. These developments would have fueled a withering cross-examination, destroying confidence in Smallwood's story and raising a substantial implication that the prosecutor had coached him to give it.<sup>[14]</sup></p>
<p><span class="star-pagination">*444</span> Since the evolution over time of a given eyewitness's description can be fatal to its reliability, cf. <i>Manson</i> v. <i>Brathwaite,</i> <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98, 114</a></span> (1977) (reliability depends in part on the accuracy of prior description); <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188, 199</a></span> (1972) (reliability of identification following impermissibly suggestive lineup depends in part on accuracy of witness's prior description), the Smallwood and Williams identifications would have been severely undermined by use of their suppressed statements. The likely damage is best understood by taking the word of the prosecutor, who contended during closing arguments that Smallwood and Williams were the State's two best witnesses. See Tr. of Closing Arg. 49 (Dec. 7, 1984) (After discussing Territo's and Kersh's testimony: "Isaac Smallwood, have you ever seen a better witness[?] . . . What's better than that is Henry Williams. . . . Henry Williams was the closest of them all <span class="star-pagination">*445</span> right here"). Nor, of course, would the harm to the State's case on identity have been confined to their testimony alone. The fact that neither Williams nor Smallwood could have provided a consistent eyewitness description pointing to Kyles would have undercut the prosecution all the more because the remaining eyewitnesses called to testify (Territo and Kersh) had their best views of the gunman only as he fled the scene with his body partly concealed in Dye's car. And even aside from such important details, the effective impeachment of one eyewitness can call for a new trial even though the attack does not extend directly to others, as we have said before. See <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112-113, n. 21</a></span>.</p>
<p></p>
<h2>B</h2>
<p>Damage to the prosecution's case would not have been confined to evidence of the eyewitnesses, for Beanie's various statements would have raised opportunities to attack not only the probative value of crucial physical evidence and the circumstances in which it was found, but the thoroughness and even the good faith of the investigation, as well. By the State's own admission, Beanie was essential to its investigation and, indeed, "made the case" against Kyles. Tr. of Closing Arg. 13 (Dec. 7, 1984). Contrary to what one might hope for from such a source, however, Beanie's statements to the police were replete with inconsistencies and would have allowed the jury to infer that Beanie was anxious to see Kyles arrested for Dye's murder. Their disclosure would have revealed a remarkably uncritical attitude on the part of the police.</p>
<p>If the defense had called Beanie as an adverse witness, he could not have said anything of any significance without being trapped by his inconsistencies. A short recapitulation of some of them will make the point. In Beanie's initial meeting with the police, and in his signed statement, he said he bought Dye's LTD and helped Kyles retrieve his car from the Schwegmann's lot on Friday. In his first call to the police, <span class="star-pagination">*446</span> he said he bought the LTD on Thursday, and in his conversation with the prosecutor between trials it was again on Thursday that he said he helped Kyles retrieve Kyles's car. Although none of the first three versions of this story mentioned Kevin Black as taking part in the retrieval of the car and transfer of groceries, after Black implicated Beanie by his testimony for the defense at the first trial, Beanie changed his story to include Black as a participant. In Beanie's several accounts, Dye's purse first shows up variously next to a building, in some bushes, in Kyles's car, and at Black's house.</p>
<p>Even if Kyles's lawyer had followed the more conservative course of leaving Beanie off the stand, though, the defense could have examined the police to good effect on their knowledge of Beanie's statements and so have attacked the reliability of the investigation in failing even to consider Beanie's possible guilt and in tolerating (if not countenancing) serious possibilities that incriminating evidence had been planted. See, <i>e. g., </i><i>Bowen</i> v. <i>Maynard,</i> <span class="citation" data-id="475335"><a href="/opinion/475335/clifford-henry-bowen-v-gary-d-maynard-warden-oklahoma-state/#613" aria-description="Citation for case: Clifford Henry Bowen v. Gary D. Maynard, Warden, Oklahoma...">799 F. 2d 593, 613</a></span> (CA10 1986) ("A common trial tactic of defense lawyers is to discredit the caliber of the investigation or the decision to charge the defendant, and we may consider such use in assessing a possible <i>Brady</i> violation"); <i>Lindsey</i> v. <i>King,</i> <span class="citation" data-id="456348"><a href="/opinion/456348/tyronne-lindsey-v-john-t-king-etc/#1042" aria-description="Citation for case: Tyronne Lindsey v. John T. King, Etc.">769 F. 2d 1034, 1042</a></span> (CA5 1985) (awarding new trial of prisoner convicted in Louisiana state court because withheld <i>Brady</i> evidence "carried within it the potential . . . for the . . . discrediting . . . of the police methods employed in assembling the case").<sup>[15]</sup></p>
<p><span class="star-pagination">*447</span> By demonstrating the detectives' knowledge of Beanie's affirmatively self-incriminating statements, the defense could have laid the foundation for a vigorous argument that the police had been guilty of negligence. In his initial meeting with police, Beanie admitted twice that he changed the license plates on the LTD. This admission enhanced the suspiciousness of his possession of the car; the defense could have argued persuasively that he was no bona fide purchaser. And when combined with his police record, evidence of prior criminal activity near Schwegmann's, and his status as a suspect in another murder, his devious behavior gave reason to believe that he had done more than buy a stolen car. There was further self-incrimination in Beanie's statement that Kyles's car was parked in the same part of the Schwegmann's lot where Dye was killed. Beanie's apparent awareness of the specific location of the murder could have been based, as the State contends, on television or newspaper reports, but perhaps it was not. Cf. App. 215 (Beanie saying that he knew about the murder because his brother-in-law had seen it "on T. V. and in the paper" and had told Beanie). Since the police admittedly never treated Beanie as a suspect, the defense could thus have used his statements to throw the reliability of the investigation into doubt and to sully the credibility of Detective Dillman, who testified that Beanie was never a suspect, Tr. 103-105, 107 (Dec. 6, 1984), and that he had "no knowledge" that Beanie had changed the license plate, <i>id.,</i> at 95.</p>
<p>The admitted failure of the police to pursue these pointers toward Beanie's possible guilt could only have magnified the effect on the jury of explaining how the purse and the gun happened to be recovered. In Beanie's original recorded statement, he told the police that "[Kyles's] garbage goes out tomorrow," and that "if he's smart he'll put [the purse] in [the] garbage." App. 257. These statements, along with the internal memorandum stating that the police had "reason to believe" Dye's personal effects and Schwegmann's bags <span class="star-pagination">*448</span> would be in the garbage, would have supported the defense's theory that Beanie was no mere observer, but was determining the investigation's direction and success. The potential for damage from using Beanie's statement to undermine the ostensible integrity of the investigation is only confirmed by the prosecutor's admission at one of Kyles's post conviction hearings, that he did not recall a single instance before this case when police had searched and seized garbage on the street in front of a residence, Tr. of Hearing on PostConviction Relief 113 (Feb. 20, 1989), and by Detective John Miller's admission at the same hearing that he thought at the time that it "was a possibility" that Beanie had planted the incriminating evidence in the garbage, Tr. of Hearing on Post-Conviction Relief 51 (Feb. 24, 1989). If a police officer thought so, a juror would have, too.<sup>[16]</sup></p>
<p>To the same effect would have been an enquiry based on Beanie's apparently revealing remark to police that "if you can set [Kyles] up good, you can get that same gun."<sup>[17]</sup> App. 228-229. While the jury might have understood that Beanie meant simply that if the police investigated Kyles, they would probably find the murder weapon, the jury could also have taken Beanie to have been making the more sinister <span class="star-pagination">*449</span> suggestion that the police "set up" Kyles, and the defense could have argued that the police accepted the invitation. The prosecutor's notes of his interview with Beanie would have shown that police officers were asking Beanie the whereabouts of the gun all day Sunday, the very day when he was twice at Kyles's apartment and was allegedly seen by Johnny Burns lurking near the stove, where the gun was later found.<sup>[18]</sup> Beanie's same statement, indeed, could have been used to cap an attack on the integrity of the investigation and on the reliability of Detective Dillman, who testified on cross-examination that he did not know if Beanie had been at Kyles's apartment on Sunday. Tr. 93, 101 (Dec. 6, 1984).<sup>[19]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*450</span> C</h2>
<p>Next to be considered is the prosecution's list of the cars in the Schwegmann's parking lot at mid-evening after the murder. While its suppression does not rank with the failure to disclose the other evidence discussed here, it would have had some value as exculpation and impeachment, and it counts accordingly in determining whether <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> `s standard of materiality is satisfied. On the police's assumption, argued to the jury, that the killer drove to the lot and left his car there during the heat of the investigation, the list without Kyles's registration would obviously have helped Kyles and would have had some value in countering an argument by the prosecution that a grainy enlargement of a photograph of the crime scene showed Kyles's car in the background. The list would also have shown that the police either knew that it was inconsistent with their informant's second and third statements (in which Beanie described retrieving Kyles's car after the time the list was compiled) or never even bothered to check the informant's story against known fact. Either way, the defense would have had further support for arguing that the police were irresponsible in relying on Beanie to tip them off to the location of evidence damaging to Kyles.</p>
<p>The State argues that the list was neither impeachment nor exculpatory evidence because Kyles could have moved his car before the list was created and because the list does <span class="star-pagination">*451</span> not purport to be a comprehensive listing of all the cars in the Schwegmann's lot. Such argument, however, confuses the weight of the evidence with its favorable tendency, and even if accepted would work against the State, not for it. If the police had testified that the list was incomplete, they would simply have underscored the unreliability of the investigation and complemented the defense's attack on the failure to treat Beanie as a suspect and his statements with a presumption of fallibility. But however the evidence would have been used, it would have had some weight and its tendency would have been favorable to Kyles.</p>
<p></p>
<h2>D</h2>
<p>In assessing the significance of the evidence withheld, one must of course bear in mind that not every item of the State's case would have been directly undercut if the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> evidence had been disclosed. It is significant, however, that the physical evidence remaining unscathed would, by the State's own admission, hardly have amounted to overwhelming proof that Kyles was the murderer. See Tr. of Oral Arg. 56 ("The heart of the State's case was eye-witness identification"); see also Tr. of Hearing on Post-Conviction Relief 117 (Feb. 20, 1989) (testimony of chief prosecutor Strider) ("The crux of the case was the four eye-witnesses"). Ammunition and a holster were found in Kyles's apartment, but if the jury had suspected the gun had been planted the significance of these items might have been left in doubt. The fact that pet food was found in Kyles's apartment was consistent with the testimony of several defense witnesses that Kyles owned a dog and that his children fed stray cats. The brands of pet food found were only two of the brands that Dye typically bought, and these two were common, whereas the one specialty brand that was found in Dye's apartment after her murder, Tr. 180 (Dec. 7, 1984), was not found in Kyles's apartment, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#188" aria-description="Citation for case: Brady v. Maryland"><i>id.,</i> at 188</a></span>. Although Kyles was wrong in describing the cat food as being on sale the day he said he bought it, he <span class="star-pagination">*452</span> was right in describing the way it was priced at Schwegmann's market, where he commonly shopped.<sup>[20]</sup></p>
<p>Similarly undispositive is the small Schwegmann's receipt on the front passenger floorboard of the LTD, the only physical evidence that bore a fingerprint identified as Kyles's. Kyles explained that Beanie had driven him to Schwegmann's on Friday to buy cigarettes and transmission fluid, and he theorized that the slip must have fallen out of the bag when he removed the cigarettes. This explanation is consistent with the location of the slip when found and with its small size. The State cannot very well argue that the fingerprint ties Kyles to the killing without also explaining how the 2-inch-long register slip could have been the receipt for a week's worth of groceries, which Dye had gone to Schwegmann's to purchase. <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#181" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 181-182</a></span>.<sup>[21]</sup></p>
<p><span class="star-pagination">*453</span> The inconclusiveness of the physical evidence does not, to be sure, prove Kyles's innocence, and the jury might have found the eyewitness testimony of Territo and Kersh sufficient to convict, even though less damning to Kyles than that of Smallwood and Williams.<sup>[22]</sup> But the question is not whether the State would have had a case to go to the jury if it had disclosed the favorable evidence, but whether we can be confident that the jury's verdict would have been the same. Confidence that it would have been cannot survive a recap of the suppressed evidence and its significance for the prosecution. The jury would have been entitled to find</p>
<blockquote>(a) that the investigation was limited by the police's uncritical readiness to accept the story and suggestions of an informant whose accounts were inconsistent to the point, for example, of including four different versions of the discovery of the victim's purse, and whose own behavior was enough to raise suspicions of guilt;</blockquote>
<blockquote>(b) that the lead police detective who testified was either less than wholly candid or less than fully informed;</blockquote>
<blockquote>(c) that the informant's behavior raised suspicions that he had planted both the murder weapon and the victim's purse in the places they were found;</blockquote>
<blockquote>(d) that one of the four eyewitnesses crucial to the State's case had given a description that did not match the defendant and better described the informant;</blockquote>
<blockquote>(e) that another eyewitness had been coached, since he had first stated that he had not seen the killer outside the getaway car, or the killing itself, whereas at trial he <span class="star-pagination">*454</span> claimed to have seen the shooting, described the murder weapon exactly, and omitted portions of his initial description that would have been troublesome for the case;</blockquote>
<blockquote>(f) that there was no consistency to eyewitness descriptions of the killer's height, build, age, facial hair, or hair length.</blockquote>
<p>Since all of these possible findings were precluded by the prosecution's failure to disclose the evidence that would have supported them, "fairness" cannot be stretched to the point of calling this a fair trial. Perhaps, confidence that the verdict would have been the same could survive the evidence impeaching even two eyewitnesses if the discoveries of gun and purse were above suspicion. Perhaps those suspicious circumstances would not defeat confidence in the verdict if the eyewitnesses had generally agreed on a description and were free of impeachment. But confidence that the verdict would have been unaffected cannot survive when suppressed evidence would have entitled a jury to find that the eyewitnesses were not consistent in describing the killer, that two out of the four eyewitnesses testifying were unreliable, that the most damning physical evidence was subject to suspicion, that the investigation that produced it was insufficiently probing, and that the principal police witness was insufficiently informed or candid. This is not the "massive" case envisioned by the dissent, <i>post,</i> at 475; it is a significantly weaker case than the one heard by the first jury, which could not even reach a verdict.</p>
<p>The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Stevens, with whom Justice Ginsburg and Justice Breyer join, concurring.</p>
<p>As the Court has explained, this case presents an important legal issue. See <i>ante,</i> at 440-441. Because Justice <span class="star-pagination">*455</span> Scalia so emphatically disagrees, I add this brief response to his criticism of the Court's decision to grant certiorari.</p>
<p>Proper management of our certiorari docket, as Justice Scalia notes, see <i>post,</i> at 456-460, precludes us from hearing argument on the merits of even a "substantial percentage" of the capital cases that confront us. Compare <i>Coleman</i> v. <i>Balkcom,</i> <span class="citation" data-id="9428365"><a href="/opinion/110496/coleman-v-balkcom-warden/" aria-description="Citation for case: Coleman v. Balkcom, Warden">451 U. S. 949</a></span> (1981) (Stevens, J., concurring in denial of certiorari), with <span class="citation" data-id="9428365"><a href="/opinion/110496/coleman-v-balkcom-warden/#956" aria-description="Citation for case: Coleman v. Balkcom, Warden"><i>id.,</i> at 956</a></span> (Rehnquist, J., dissenting). Even aside from its legal importance, however, this case merits "favored treatment," cf. <i>post,</i> at 457, for at least three reasons. First, the fact that the jury was unable to reach a verdict at the conclusion of the first trial provides strong reason to believe the significant errors that occurred at the second trial were prejudicial. Second, cases in which the record reveals so many instances of the state's failure to disclose exculpatory evidence are extremely rare. Even if I shared Justice Scalia's appraisal of the evidence in this casewhich I do notI would still believe we should independently review the record to ensure that the prosecution's blatant and repeated violations of a wellsettled constitutional obligation did not deprive petitioner of a fair trial. Third, despite my high regard for the diligence and craftsmanship of the author of the majority opinion in the Court of Appeals, my independent review of the case left me with the same degree of doubt about petitioner's guilt expressed by the dissenting judge in that court.</p>
<p>Our duty to administer justice occasionally requires busy judges to engage in a detailed review of the particular facts of a case, even though our labors may not provide posterity with a newly minted rule of law. The current popularity of capital punishment makes this "generalizable principle," <i>post,</i> at 460, especially important. Cf. <i>Harris</i> v. <i>Alabama,</i>  <span class="citation" data-id="9433087"><a href="/opinion/117899/harris-v-alabama/#519" aria-description="Citation for case: Harris v. Alabama">513 U. S. 504, 519-520</a></span>, and n. 5 (1995) (Stevens, J., dissenting). I wish such review were unnecessary, but I cannot agree that our position in the judicial hierarchy makes it inappropriate. Sometimes the performance of an unpleasant <span class="star-pagination">*456</span> duty conveys a message more significant than even the most penetrating legal analysis.</p>
<p>Justice Scalia, with whom The Chief Justice, Justice Kennedy, and Justice Thomas join, dissenting.</p>
<p>In a sensible system of criminal justice, wrongful conviction is avoided by establishing, at the trial level, lines of procedural legality that leave ample margins of safety (for example, the requirement that guilt be proved beyond a reasonable doubt)not by providing recurrent and repetitive appellate review of whether the facts in the record show those lines to have been narrowly crossed. The defect of the latter system was described, with characteristic candor, by Justice Jackson:</p>
<blockquote>"Whenever decisions of one court are reviewed by another, a percentage of them are reversed. That reflects a difference in outlook normally found between personnel comprising different courts. However, reversal by a higher court is not proof that justice is thereby better done." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#540" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 540</a></span> (1953) (opinion concurring in result).</blockquote>
<p>Since this Court has long shared Justice Jackson's view, today's opinionwhich considers a fact-bound claim of error rejected by every court, state and federal, that previously heard itis, so far as I can tell, wholly unprecedented. The Court has adhered to the policy that, when the petitioner claims only that a concededly correct view of the law was incorrectly applied to the facts, certiorari should generally (<i>i. e.,</i> except in cases of the plainest error) be denied. <i>United States</i> v. <i>Johnston,</i> <span class="citation" data-id="100655"><a href="/opinion/100655/united-states-v-johnston/#227" aria-description="Citation for case: United States v. Johnston">268 U. S. 220, 227</a></span> (1925). That policy has been observed even when the fact-bound assessment of the federal court of appeals has differed from that of the district court, <i>Sumner</i> v. <i>Mata,</i> <span class="citation" data-id="9428144"><a href="/opinion/110382/sumner-v-mata/#543" aria-description="Citation for case: Sumner v. Mata">449 U. S. 539, 543</a></span> (1981); and under what we have called the "two-court rule," the policy has been applied with particular rigor when district <span class="star-pagination">*457</span> court and court of appeals are in agreement as to what conclusion the record requires. See, <i>e. g., </i><i>Graver Tank &amp; Mfg. Co.</i> v. <i>Linde Air Products Co.,</i> <span class="citation" data-id="104637"><a href="/opinion/104637/graver-tank-mfg-co-v-linde-air-products-co/#275" aria-description="Citation for case: Graver Tank &amp; Mfg. Co. v. Linde Air Products Co.">336 U. S. 271, 275</a></span> (1949). How much the more should the policy be honored in this case, a federal habeas proceeding where not only both lower federal courts but also the state courts on post conviction review have all reviewed and rejected precisely the factspecific claim before us. Cf. <span class="citation no-link">28 U. S. C. § 2254</span>(d) (requiring federal habeas courts to accord a presumption of correctness to state-court findings of fact); <span class="citation" data-id="9428144"><a href="/opinion/110382/sumner-v-mata/#550" aria-description="Citation for case: Sumner v. Mata"><i>Sumner, supra,</i> at 550, n. 3</a></span>. Instead, however, the Court not only grants certiorari to consider whether the Court of Appeals (and all the previous courts that agreed with it) was correct as to what the facts showed in a case where the answer is far from clear, but in the process of such consideration renders new findings of fact and judgments of credibility appropriate to a trial court of original jurisdiction. See, <i>e. g., ante,</i> at 425 ("Beanie seemed eager to cast suspicion on Kyles"); <i>ante,</i> at 441, n. 12 ("Record photographs of Beanie . . . depict a man possessing a medium build"); <i>ante,</i> at 449, n. 18 ("the record photograph of the homemade holster indicates . . .").</p>
<p>The Court says that we granted certiorari "[b]ecause `[o]ur duty to search for constitutional error with painstaking care is never more exacting than it is in a capital case,' <i>Burger</i> v. <i>Kemp,</i> <span class="citation" data-id="9431130"><a href="/opinion/111957/burger-v-kemp/#785" aria-description="Citation for case: Burger v. Kemp">483 U. S. 776, 785</a></span> (1987)." <i>Ante,</i> at 422. The citation is perverse, for the reader who looks up the quoted opinion will discover that the very next sentence confirms the traditional practice from which the Court today glaringly departs: "Nevertheless, when the lower courts have found that [no constitutional error occurred], . . . deference to the shared conclusion of two reviewing courts prevent[s] us from substituting speculation for their considered opinions." <i>Burger</i> v. <i>Kemp,</i> <span class="citation" data-id="9431130"><a href="/opinion/111957/burger-v-kemp/#785" aria-description="Citation for case: Burger v. Kemp">483 U. S. 776, 785</a></span> (1987).</p>
<p>The greatest puzzle of today's decision is what could have caused <i>this</i> capital case to be singled out for favored treatment. Perhaps it has been randomly selected as a symbol, <span class="star-pagination">*458</span> to reassure America that the United States Supreme Court is reviewing capital convictions to make sure no factual error has been made. If so, it is a false symbol, for we assuredly do not do that. At, and during the week preceding, our February 24 Conference, for example, we considered and disposed of 10 petitions in capital cases, from seven States. We carefully considered whether the convictions and sentences in those cases had been obtained in reliance upon correct principles of federal law; but if we had tried to consider, in addition, whether those correct principles had been applied, not merely plausibly, but <i>accurately,</i> to the particular facts of each case, we would have done nothing else for the week. The reality is that responsibility for factual accuracy, in capital cases as in other cases, rests elsewherewith trial judges and juries, state appellate courts, and the lower federal courts; we do nothing but encourage foolish reliance to pretend otherwise.</p>
<p>Straining to suggest a legal error in the decision below that might warrant review, the Court asserts that "[t]here is room to debate whether the two judges in the majority in the Court of Appeals made an assessment of the cumulative effect of the evidence," <i>ante,</i> at 440. In support of this it quotes isolated sentences of the opinion below that supposedly "dismiss[ed] particular items of evidence as immaterial," <i><span class="citation" data-id="9431130"><a href="/opinion/111957/burger-v-kemp/" aria-description="Citation for case: Burger v. Kemp">ibid.</a></span></i> This claim of legal error does not withstand minimal scrutiny. The Court of Appeals employed <i>precisely</i> the same legal standard that the Court does. Compare <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#811" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d 806, 811</a></span> (CA5 1993) ("We apply the [<i>United States</i> v.] <i>Bagley</i> [, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">473 U. S. 667</a></span> (1985),] standard here by examining whether it is reasonably probable that, had the undisclosed information been available to Kyles, the result would have been different"), with <i>ante,</i> at 441 ("In this case, disclosure of the suppressed evidence to competent counsel would have made a different result reasonably probable"). Nor did the Court of Appeals announce a rule of law, that might have precedential force in later cases, to the effect that <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i>  <span class="star-pagination">*459</span> requires a series of independent materiality evaluations; in fact, the court said just the contrary. See <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#817" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 817</a></span> ("[W]e are not persuaded that it is reasonably probable that the jury would have found in Kyles' favor if exposed to any <i>or all</i> of the undisclosed materials") (emphasis added). If the decision is read, shall we say, cumulatively, it is clear beyond cavil that the court assessed the cumulative effect of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> evidence in the context of the whole record. See <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#807" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 807</a></span> (basing its rejection of petitioner's claim on "a complete reading of the record"); <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#811" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana..."><i>id.,</i> at 811</a></span> ("Rather than reviewing the alleged <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> materials in the abstract, we will examine the evidence presented at trial and how the extra materials would have fit"); <i>id.,</i> at 813 ("We must bear [the eyewitness testimony] in mind while assessing the probable effect of other undisclosed information"). It is, in other words, the Court itself which errs in the manner that it accuses the Court of Appeals of erring: failing to consider the material under review as a whole. The isolated snippets it quotes from the decision merely do what the Court's own opinion acknowledges must be done: to "evaluate the tendency and force of the undisclosed evidence item by item; there is no other way." <i>Ante,</i> at 436, n. 10. Finally, the Court falls back on this: "The result reached by the Fifth Circuit majority is compatible with a series of independent materiality evaluations, rather than the cumulative evaluation required by <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span>,</i> " <i>ante,</i> at 441. In other words, even though the Fifth Circuit plainly enunciated the <i>correct</i> legal rule, since the outcome it reached would not properly follow from that rule, the Fifth Circuit must in fact (and unbeknownst to itself) have been applying an <i>incorrect</i> legal rule. This effectively eliminates all distinction between mistake in law and mistake in application.</p>
<p>What the Court granted certiorari to review, then, is not a decision on an issue of federal law that conflicts with a decision of another federal or state court; nor even a decision announcing a rule of federal law that because of its novelty <span class="star-pagination">*460</span> or importance might warrant review despite the lack of a conflict; nor yet even a decision that <i>patently</i> errs in its application of an old rule. What we have here is an intensely fact-specific case in which the court below unquestionably applied the correct rule of law and did not unquestionably errprecisely the type of case in which we are <i>most</i> inclined to deny certiorari. But despite all of that, I would not have dissented on the ground that the writ of certiorari should be dismissed as improvidently granted. Since the majority is as aware of the limits of our capacity as I am, there is little fear that the grant of certiorari in a case of this sort will often be repeatedwhich is to say little fear that today's grant has any generalizable principle behind it. I am still forced to dissent, however, because, having improvidently decided to review the facts of this case, the Court goes on to get the facts wrong. Its findings are in my view clearly erroneous, cf. Fed. Rule Civ. Proc. 52(a), and the Court's verdict would be reversed if there were somewhere further to appeal.</p>
<p></p>
<h2>I</h2>
<p>Before proceeding to detailed consideration of the evidence, a few general observations about the Court's methodology are appropriate. It is fundamental to the discovery rule of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), that the materiality of a failure to disclose favorable evidence "must be evaluated in the context of the entire record." <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 112</a></span> (1976). It is simply not enough to show that the undisclosed evidence would have allowed the defense to weaken, or even to "destro[y]," <i>ante,</i>  at 441, the <i>particular</i> prosecution witnesses or items of prosecution evidence to which the undisclosed evidence relates. It is petitioner's burden to show that in light of all the evidence, including that untainted by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation, it is reasonably probable that a jury would have entertained a reasonable doubt regarding petitioner's guilt. See <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 682</a></span> (1985); <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>,</i>  <span class="star-pagination">*461</span> <i>supra,</i> at 112-113. The Court's opinion fails almost entirely to take this principle into account. Having spent many pages assessing the effect of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material on two prosecution witnesses and a few items of prosecution evidence, <i>ante,</i> at 441-451, it dismisses the remainder of the evidence against Kyles in a quick page-and-a-half, <i>ante,</i> at 451-453. This partiality is confirmed in the Court's attempt to "recap . . . <i>the suppressed evidence</i> and its significance for the prosecution," <i>ante,</i> at 453 (emphasis added), which omits the required comparison between that evidence and the evidence that was disclosed. My discussion of the record will present the half of the analysis that the Court omits, emphasizing the evidence concededly unaffected by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation which demonstrates the immateriality of the violation.</p>
<p>In any analysis of this case, the desperate implausibility of the theory that petitioner put before the jury must be kept firmly in mind. The first half of that theorydesigned to neutralize the physical evidence (Mrs. Dye's purse in his garbage, the murder weapon behind his stove)was that petitioner was the victim of a "frame-up" by the police informer and evil genius, Beanie. Now it is not unusual for a guilty person who knows that he is suspected of a crime to try to shift blame to someone else; and it is less common, but not unheard of, for a guilty person who is neither suspected nor subject to suspicion (because he has established a perfect alibi), to call attention to himself by coming forward to point the finger at an innocent person. But petitioner's theory is that the guilty Beanie, who <i>could</i> plausibly be accused of the crime (as petitioner's brief amply demonstrates), but who was <i>not</i> a suspect any more than Kyles was (the police as yet had no leads, see <i>ante,</i> at 424), injected both Kyles and himself into the investigation in order to get the innocent Kyles convicted.<sup>[1]</sup> If this were not stupid enough, the <span class="star-pagination">*462</span> wicked Beanie is supposed to have suggested that the police search his victim's premises <i>a full day before he got around to planting the incriminating evidence on the premises.</i> </p>
<p>The second half of petitioner's theory was that he was the victim of a quadruple coincidence, in which four eyewitnesses to the crime mistakenly identified him as the murdererthree picking him out of a photo array without hesitation, and all four affirming their identification in open court after comparing him with Beanie. The extraordinary mistake petitioner had to persuade the jury these four witnesses made was not simply to mistake the real killer, Beanie, for the very same innocent third party (hard enough to believe), but in addition to mistake him <i>for the very man Beanie had chosen to frame</i> the last and most incredible level of coincidence. However small the chance that the jury would believe any one of those improbable scenarios, the likelihood that it would believe them all together is far smaller. The Court concludes that it is "reasonably probable" the undisclosed witness interviews would have persuaded the jury of petitioner's implausible theory of mistaken eyewitness testimony, and then argues that it is "reasonably probable" the undisclosed information regarding Beanie would have persuaded the jury of petitioner's implausible theory regarding the incriminating physical evidence. I think neither of those conclusions is remotely true, but even if they were the Court would still be guilty of a fallacy in declaring victory on each implausibility in turn, and thus victory on the whole, <span class="star-pagination">*463</span> without considering the infinitesimal probability of the jury's swallowing the entire concoction of implausibility squared.</p>
<p>This basic error of approaching the evidence piecemeal is also what accounts for the Court's obsessive focus on the credibility or culpability of Beanie, who did not even testify at trial and whose credibility or innocence the State has never once avowed. The Court's opinion reads as if either petitioner or Beanie must be telling the truth, and any evidence tending to inculpate or undermine the credibility of the one would exculpate or enhance the credibility of the other. But the jury verdict in this case said only that petitioner was guilty of the murder. That is perfectly consistent with the possibilities that Beanie repeatedly lied, <i>ante,</i>  at 445, that he was an accessory after the fact, cf. <i>ante,</i> at 445-446, or even that he planted evidence against petitioner, <i>ante,</i> at 448. Even if the undisclosed evidence would have allowed the defense to thoroughly impeach Beanie and to suggest the above possibilities, the jury could well have believed <i>all</i> of those things and yet have condemned petitioner because it could not believe that <i>all four</i> of the eyewitnesses were similarly mistaken.<sup>[2]</sup></p>
<p>Of course even that much rests on the premise that competent counsel would run the terrible risk of calling Beanie, a witness whose "testimony almost certainly would have inculpated [petitioner]" and whom "any reasonable attorney would perceive . . . as a `loose cannon.' " <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#818" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 818</a></span>. Perhaps because that premise seems so implausible, the Court retreats to the possibility that petitioner's counsel, <span class="star-pagination">*464</span> even if not calling Beanie to the stand, could have used the evidence relating to Beanie to attack "the reliability of the investigation." <i>Ante,</i> at 446. But that is distinctly less effective than substantive evidence bearing on the guilt or innocence of the accused. In evaluating <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims, we assume jury conduct that is both rational and obedient to the law. We do not assume that even though the whole mass of the evidence, both disclosed and undisclosed, shows petitioner guilty beyond a reasonable doubt, the jury will punish sloppy investigative techniques by setting the defendant free. Neither Beanie nor the police were on trial in this case. Petitioner was, and no amount of collateral evidence could have enabled his counsel to move the mountain of direct evidence against him.</p>
<p></p>
<h2>II</h2>
<p>The undisclosed evidence does not create a"`reasonable probability' of a different result." <i>Ante,</i> at 434 (quoting <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U. S., at 682</a></span>). To begin with the eyewitness testimony: Petitioner's basic theory at trial was that the State's four eyewitnesses happened to mistake Beanie, the real killer, for petitioner, the man whom Beanie was simultaneously trying to frame. Police officers testified to the jury, and petitioner has never disputed, that three of the four eyewitnesses (Territo, Smallwood, and Williams) were shown a photo lineup of six young men four days after the shooting and, without aid or duress, identified petitioner as the murderer; and that all of them, plus the fourth eyewitness, Kersh, reaffirmed their identifications at trial after petitioner and Beanie were made to stand side by side.</p>
<p>Territo, the first eyewitness called by the State, was waiting at a red light in a truck 30 or 40 yards from the Schwegmann's parking lot. He saw petitioner shoot Mrs. Dye, start her car, drive out onto the road, and pull up just behind Territo's truck. When the light turned green petitioner pulled <span class="star-pagination">*465</span> beside Territo and stopped while waiting to make a turn. Petitioner looked Territo full in the face. Territo testified, "I got a good look at him. If I had been in the passenger seat of the little truck, I could have reached out and not even stretched my arm out, I could have grabbed hold of him." Tr. 13-14 (Dec. 6, 1984). Territo also testified that a detective had shown him a picture of Beanie and asked him if the picture "could have been the guy that did it. I told him no." <i>Id.,</i> at 24. The second eyewitness, Kersh, also saw petitioner shoot Mrs. Dye. When asked whether she got "a good look" at him as he drove away, she answered "yes." <i>Id.,</i> at 32. She also answered "yes" to the question whether she "got to see the side of his face," <i>id.,</i> at 31, and said that while petitioner was stopped she had driven to within reaching distance of the driver's-side door of Mrs. Dye's car and stopped there. <i>Id.,</i> at 34. The third eyewitness, Smallwood, testified that he saw petitioner shoot Mrs. Dye, walk to the car, and drive away. <i>Id.,</i> at 42. Petitioner drove slowly by, within a distance of 15 or 25 feet, <i>id.,</i> at 43-45, and Smallwood saw his face from the side. <i>Id.,</i> at 43. The fourth eyewitness, Williams, who had been working outside the parking lot, testified that "the gentleman came up the side of the car," struggled with Mrs. Dye, shot her, walked around to the driver's side of the car, and drove away. <i>Id.,</i>  at 52. Williams not only "saw him before he shot her," <i>id.,</i>  at 54, but watched petitioner drive slowly by "within less than ten feet." <i>Ibid.</i> When asked "[d]id you get an opportunity to look at him good?", Williams said, "I did." <i>Id.,</i> at 55.</p>
<p>The Court attempts to dispose of this direct, unqualified, and consistent eyewitness testimony in two ways. First, by relying on a theory so implausible that it was apparently not suggested by petitioner's counsel until the oral-argument<i>cum</i> -evidentiary-hearing held before us, perhaps because it is a theory that only the most removed appellate court could <span class="star-pagination">*466</span> love. This theory is that there is a reasonable probability that the jury would have changed its mind about the eyewitness identification because the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material would have permitted the defense to argue that the eyewitnesses only got a good look at the killer when he was sitting in Mrs. Dye's car, and thus could identify him, not by his height and build, but <i>only by his face.</i> Never mind, for the moment, that this is factually false, since the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material showed that only <i>one</i> of the four eyewitnesses, Smallwood, did not see the killer outside the car.<sup>[3]</sup> And never mind, also, the dubious premise that the build of a man 6-feet tall (like petitioner) is indistinguishable, when seated behind the wheel, from that of a man less than 5<sup>[1]</sup>20442-feet tall (like Beanie). To assert that unhesitant and categorical identification by four witnesses who viewed the killer, close-up and with the sun high in the sky, would not eliminate reasonable doubt if it were based <i>only</i> on <i>facial</i> characteristics, and not on height and build, is quite simply absurd. Facial features are <i>the primary means</i> by which human beings recognize one another. That is why police departments distribute "mug" shots of wanted felons, rather than Ivy-League-type posture pictures; it is why bank robbers wear stockings over their faces instead of floor-length capes over their shoulders; it is why the Lone Ranger wears a mask instead of a poncho; and it is why a criminal defense lawyer who seeks to destroy an <span class="star-pagination">*467</span> identifying witness by asking "You admit that you saw only the killer's face?" will be laughed out of the courtroom.</p>
<p>It would be different, of course, if there were evidence that Kyles's and Beanie's faces looked like twins, or at least bore an unusual degree of resemblance. That facial resemblance <i>would</i> explain why, if Beanie committed the crime, all four witnesses picked out Kyles at first (though not why they continued to pick him out when he and Beanie stood side-by-side in court), and would render their failure to observe the height and build of the killer relevant. But without evidence of facial similarity, the question "You admit that you saw only the killer's face?" draws no blood; it does not explain <i>any</i> witness's identification of petitioner as the killer. While the assumption of facial resemblance between Kyles and Beanie underlies all of the Court's repeated references to the partial concealment of the killer's body from view, see, <i>e. g., ante,</i> at 442-443, 443-444, n. 14, 445, the Court never actually says that such resemblance exists. That is because there is not the slightest basis for such a statement in the record. <i>No</i> court has found that Kyles and Beanie bear any facial resemblance. In fact, quite the opposite: <i>every</i> federal and state court that has reviewed the record photographs, or seen the two men, has found that they do not resemble each other in any respect. See <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#813" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 813</a></span> ("Comparing photographs of Kyles and Beanie, it is evident that the former is taller, thinner, and has a narrower face"); App. 181 (District Court opinion) ("The court examined all of the pictures used in the photographic line-up and compared Kyles' and Beanie's pictures; it finds that they did not resemble one another"); <i>id.,</i> at 36 (state trial court findings on post conviction review) ("[Beanie] clearly and distinctly did <i>not resemble</i> the defendant in this case") (emphasis in original). The District Court's finding controls because it is not clearly erroneous, Fed. Rule Civ. Proc. 52(a), and the state court's finding, because fairly supported by the record, must be presumed correct on habeas review. See <span class="citation no-link">28 U. S. C. § 2254</span>(d).</p>
<p><span class="star-pagination">*468</span> The Court's second means of seeking to neutralize the impressive and unanimous eyewitness testimony uses the same "build-is-everything" theory to exaggerate the effect of the State's failure to disclose the contemporaneous statement of Henry Williams. That statement would assuredly have permitted a sharp cross-examination, since it contained estimations of height and weight that fit Beanie better than petitioner. <i>Ante,</i> at 441-442. But I think it is hyperbole to say that the statement would have "substantially reduced or destroyed" the value of Williams' testimony. <i>Ante,</i> at 441. Williams saw the murderer drive slowly by less than 10 feet away, Tr. 54 (Dec. 6, 1984), and unhesitatingly picked him out of the photo lineup. The jury might well choose to give greater credence to the simple fact of identification than to the difficult estimation of height and weight.</p>
<p>The Court spends considerable time, see <i>ante,</i> at 443, showing how Smallwood's testimony could have been discredited to such a degree as to "rais[e] a substantial implication that the prosecutor had coached him to give it." <i><span class="citation no-link">Ibid.</span></i>  Perhaps so, but that is all irrelevant to this appeal, since <i>all</i>  of that impeaching material (except the "facial identification" point I have discussed above) was available to the defense independently of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. See <i>ante,</i> at 443-444, n. 14. In sum, the undisclosed statements, credited with everything they could possibly have provided to the defense, leave two prosecution witnesses (Territo and Kersh) totally untouched; one prosecution witness (Smallwood) barely affected (he saw "only" the killer's face); and one prosecution witness (Williams) somewhat impaired (his description of the killer's height and weight did not match Kyles). We must keep all this in due perspective, remembering that the relevant question in the materiality inquiry is not how many points the defense could have scored off the prosecution witnesses, but whether it is reasonably probable that the new evidence would have caused the jury to accept the basic thesis that all four witnesses were mistaken. I think it plainly <span class="star-pagination">*469</span> is not. <i>No</i> witness involved in the case ever identified <i>anyone</i> but petitioner as the murderer. Their views of the crime and the escaping criminal were obtained in bright daylight from close at hand; and their identifications were reaffirmed before the jury. After the side-by-side comparison between Beanie and Kyles, the jury heard Territo say that there was "[n]o doubt in my mind" that petitioner was the murderer, Tr. 378 (Dec. 7, 1984); heard Kersh say "I know it was him. . . . I seen his face and I know the color of his skin. I know it. I know it's him," <i>id.,</i> at 383; heard Smallwood say "I'm positive . . . [b]ecause that's the man who I seen kill that woman," <i>id.,</i> at 387; and heard Williams say "[n]o doubt in my mind," <i>id.,</i> at 391. With or without the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> evidence, there could be no doubt in the mind of the jury either.</p>
<p>There remains the argument that is the major contribution of today's opinion to <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> litigation; with our endorsement, it will surely be trolled past appellate courts in all future failure-to-disclose cases. The Court argues that "the effective impeachment of one eyewitness can call for a new trial even though the attack does not extend directly to others, as we have said before." <i>Ante,</i> at 445 (citing <i>Agurs</i> v. <i>United States,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112-113, n. 21</a></span>). It would be startling if we <i>had</i> "said [this] before," since it assumes irrational jury conduct. The weakening of one witness's testimony does not weaken the unconnected testimony of another witness; and to entertain the possibility that the jury will give it such an effect is incompatible with the whole idea of a materiality standard, which presumes that the incriminating evidence that would have been destroyed by proper disclosure can be logically separated from the incriminating evidence that would have remained unaffected. In fact we have said nothing like what the Court suggests. The opinion's only authority for its theory, the cited footnote from <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>,</i> was appended to the proposition that "[a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> ] omission must be evaluated in the context of the entire record," 427 U. S., <span class="star-pagination">*470</span> at 112. In accordance with that proposition, the footnote recited a hypothetical that shows how a witness's testimony could have been destroyed by withheld evidence <i>that contradicts the witness.</i><sup>[4]</sup> That is worlds apart from having it destroyed by the corrosive effect of withheld evidence that impeaches (or, as here, merely weakens) <i>some other corroborating witness.</i> </p>
<p>The physical evidence confirms the immateriality of the nondisclosures. In a garbage bag outside petitioner's home the police found Mrs. Dye's purse and other belongings. Inside his home they found, behind the kitchen stove, the .32caliber revolver used to kill Mrs. Dye; hanging in a wardrobe, a homemade shoulder holster that was "a perfect fit" for the revolver, Tr. 74 (Dec. 6, 1984) (Detective Dillman); in a dresser drawer in the bedroom, two boxes of gun cartridges, one containing only .32-caliber rounds of the same brand found in the murder weapon, another containing .22,.32, and .38-caliber rounds; in a kitchen cabinet, eight empty Schwegmann's bags; and in a cupboard underneath that cabinet, one Schwegmann's bag containing 15 cans of pet food. Petitioner's account at trial was that Beanie planted the purse, gun, and holster, that petitioner received the ammunition from Beanie as collateral for a loan, and that petitioner had bought the pet food the day of the murder. That account strains credulity to the breaking point.</p>
<p><span class="star-pagination">*471</span> The Court is correct that the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material would have supported the claim that Beanie planted Mrs. Dye's belongings in petitioner's garbage and (to a lesser degree) that Beanie planted the gun behind petitioner's stove. <i>Ante,</i> at 448. But we must see the whole story that petitioner presented to the jury. Petitioner would have it that Beanie did not plant the incriminating evidence until the day <i>after</i> he incited the police to search petitioner's home. Moreover, he succeeded in surreptitiously placing the gun behind the stove, and the matching shoulder holster in the wardrobe, while <i>at least 10 and as many as 19 people</i> were present in petitioner's small apartment.<sup>[5]</sup> Beanie, who was wearing blue jeans and either a "tank-top" shirt, Tr. 302 (Dec. 7, 1984) (Cathora Brown), or a short-sleeved shirt, <i>id.,</i> at 351 (petitioner), would have had to be concealing about his person not only the shoulder holster and the murder weapon, but also a different gun with tape wrapped around the barrel that he showed to petitioner. <i>Id.,</i> at 352. Only appellate judges could swallow such a tale. Petitioner's only supporting evidence was Johnny Burns's testimony that he saw Beanie stooping behind the stove, presumably to plant the gun. <i>Id.,</i> at 262-263. Burns's credibility on the stand can perhaps best be gauged by observing that the state judge who presided over petitioner's trial stated, in a post conviction proceeding, that "[I] ha[ve] chosen to totally disregard everything that [Burns] has said," App. 35. See also <i>id.,</i> at 165 (District Court opinion) ("Having reviewed the entire record, this court without hesitation concurs with the trial court's determination concerning the credibility of [Burns]"). Burns, by the way, who repeatedly stated at trial that Beanie was his "best friend," Tr. 279 (Dec. 7, 1984), has since been <span class="star-pagination">*472</span> tried and convicted for killing Beanie. See <i>State</i> v. <i>Burnes,</i>  <span class="citation" data-id="1610706"><a href="/opinion/1610706/state-v-burnes/" aria-description="Citation for case: State v. Burnes">533 So. 2d 1029</a></span> (La. App. 1988).<sup>[6]</sup></p>
<p>Petitioner did not claim that the ammunition had been planted. The police found a .22-caliber rifle under petitioner's mattress and two boxes of ammunition, one containing .22, .32, and .38-caliber rounds, another containing only.32-caliber rounds of the same brand as those found loaded in the murder weapon. Petitioner's story was that Beanie gave him the rifle and the .32-caliber shells as security for a loan, but that he had taken the .22-caliber shells out of the box. Tr. 353, 355 (Dec. 7, 1984). Put aside that the latter detail was contradicted by the facts; but consider the inherent implausibility of Beanie's giving petitioner collateral in the form of a box containing <i>only</i> .32 shells, if it were true that petitioner did not own a .32-caliber gun. As the Fifth Circuit wrote, "[t]he more likely inference, apparently chosen by the jury, is that [petitioner] possessed .32-caliber ammunition because he possessed a .32-caliber firearm." <span class="citation" data-id="9485897"><a href="/opinion/653644/curtis-lee-kyles-v-john-p-whitley-warden-louisiana-state-penitentiary/#817" aria-description="Citation for case: Curtis Lee Kyles v. John P. Whitley, Warden, Louisiana...">5 F. 3d, at 817</a></span>.</p>
<p>We come to the evidence of the pet food, so mundane and yet so very damning. Petitioner's confused and changing explanations for the presence of 15 cans of pet food in a Schwegmann's bag under the sink must have fatally undermined his credibility before the jury. See App. 36 (trial judge finds that petitioner's "obvious lie" concerning the pet food "may have been a crucial bit of evidence in the minds of the jurors which caused them to discount the entire defense <span class="star-pagination">*473</span> in this case"). The Court disposes of the pet food evidence as follows:</p>
<blockquote>"The fact that pet food was found in Kyles's apartment was consistent with the testimony of several defense witnesses that Kyles owned a dog and that his children fed stray cats. The brands of pet food found were only two of the brands that Dye typically bought, and these two were common, whereas the one specialty brand that was found in Dye's apartment after her murder, Tr. 180 (Dec. 7,1984), was not found in Kyles's apartment, <i>id.,</i>  7, Although at 188. Kyles was wrong in describing the cat food as being on sale the day he said he bought it, he was right in describing the way it was priced at Schwegmann's market, where he commonly shopped." <i>Ante,</i> at 451-452; see also <i>ante,</i> at 452, n. 20.</blockquote>
<p>The full story is this. Mr. and Mrs. Dye owned two cats and a dog, Tr. 178 (Dec. 7, 1984), for which she regularly bought varying brands of pet food, several different brands at a time. <i>Id.,</i> at 179, 180. Found in Mrs. Dye's home after her murder were the brands Nine Lives, Kalkan, and P

[...TRUNCATED 29542 of 149542 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/LaChance v. Erickson.md  (`case`, 5 assertions)

### content_page

```
---
title: "LaChance v. Erickson"
type: case
citation: "522 U.S. 262 (1998)"
parallel_cite: "118 S. Ct. 753; 139 L. Ed. 2d 695"
neutral_cite: 1998 U.S. LEXIS 636
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-01-21
docket: 96-1395
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: LaChance v. Erickson
  varies_by_point: false
  scope_note: "Good law; marks the boundary of the Garrity line — the privilege lets a public employee stay silent, but not lie."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118163/lachance-v-erickson/"
  cluster_id: 118163
  opinion_id: 118163
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Related (cross-doctrine)"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]"]
aliases: []
tags: ["case", "fifth-amendment", "due-process", "public-employee", "garrity", "false-statements", "federal-employee"]
holding: "Neither due process nor the civil-service statutes bar a federal agency from disciplining an employee for making false statements to investigators in response to an underlying misconduct charge; the right to be heard does not include a right to lie (an employee facing criminal exposure may stay silent, but may not lie)."
lake:
  record_id: LaChance v. Erickson
  status: under_review
  projected_at: 2026-07-06
---

# LaChance v. Erickson

*522 U.S. 262 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Several federal employees were the subject of agency adverse actions for misconduct, and each made false statements to agency investigators denying the charged conduct. The agencies added a false-statement charge and relied on it in part. The Merit Systems Protection Board upheld the penalties based on the underlying misconduct but overturned the false-statement charges, and the Court of Appeals for the Federal Circuit agreed, reasoning that due process barred charging an employee for denying the underlying charge. The Director of the Office of Personnel Management sought review.

## Issue
Whether the Due Process Clause or the Civil Service Reform Act precludes a federal agency from sanctioning an employee for making false statements to the agency in response to an underlying charge of employment-related misconduct.

## Rule
No. There is no right to lie, even within a right to be heard. Quoting *Bryson*: "A citizen may decline to answer the question, or answer it honestly, but he cannot with impunity knowingly and willfully answer with a falsehood." — 522 U.S. at 265. ^pin-265

The privilege protects silence, not falsehood: "If answering an agency's investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent." — *Id.* at 267. ^pin-267

The Court therefore held: "[W]e hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct." — *Id.* at 268. ^pin-268

## Application
The respondent employees did not stay silent or answer truthfully; they lied to investigators about the conduct with which they were charged. A "meaningful opportunity to be heard" does not include a right to make false statements, and the absence of an oath was immaterial because the charge was making false statements, not perjury. Because each employee could have declined to answer — invoking the Fifth Amendment if answering risked criminal exposure — rather than lying, the agencies were free to sanction the false statements made in response to the underlying charges.

## Conclusion
A government agency may take adverse action against an employee for making false statements in response to an underlying misconduct charge; the Federal Circuit's judgments were reversed. Within the public-employee privilege line, *LaChance* marks the limit: the privilege secures the right to remain silent, not a right to lie.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *LaChance* is good law and complements [[Garrity v. New Jersey]], [[Gardner v. Broderick]], and [[Lefkowitz v. Turley]]: those cases protect an employee from being penalized for asserting the privilege, while *LaChance* makes clear the privilege does not shelter affirmative falsehoods.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Related (cross-doctrine)*

## Sources
- *LaChance v. Erickson*, 522 U.S. 262 (1998) — https://www.courtlistener.com/opinion/118163/lachance-v-erickson/ — pinpoints: 265, 267, 268.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5b777ec26cf50b81", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "522 U.S. 262 (1998)", "court": "U.S. Supreme Court", "neutral_cite": "1998 U.S. LEXIS 636", "official_citation_present": true, "parallel_cite": "118 S. Ct. 753; 139 L. Ed. 2d 695", "title": "LaChance v. Erickson", "year": "1998"}}
{"assertion_id": "5bb9cf2c461b9b09", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Neither due process nor the civil-service statutes bar a federal agency from disciplining an employee for making false statements to investigators in response to an underlying misconduct charge; the right to be heard does not include a right to lie (an employee facing criminal exposure may stay silent, but may not lie).", "title": "LaChance v. Erickson"}}
{"assertion_id": "c6a7e442364b6c8f", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Related (cross-doctrine)", "title": "LaChance v. Erickson"}}
{"assertion_id": "6b0009963860ebff", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1998-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "LaChance v. Erickson", "field_i_validity": "good_law", "scope_note": "Good law; marks the boundary of the Garrity line — the privilege lets a public employee stay silent, but not lie.", "title": "LaChance v. Erickson", "varies_by_point": "false"}}
{"assertion_id": "8741a85e54719d57", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "LaChance v. Erickson"}}
```

### lake record — LaChance v. Erickson

```json
{
  "schema_version": "s2.v1",
  "record_id": "LaChance v. Erickson",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "LaChance v. Erickson",
    "case_name_short": "LaChance",
    "case_name_full": "LACHANCE, DIRECTOR, OFFICE OF PERSONNEL MANAGEMENT v. ERICKSON Et Al.",
    "input_case_name": "LaChance v. Erickson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-01-21",
    "year": 1998,
    "docket": "96-1395",
    "cluster_id": 118163,
    "lead_opinion_id": 118163,
    "sibling_ids": [
      118163
    ],
    "absolute_url": "/opinion/118163/lachance-v-erickson/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "522 U.S. 262",
      "volume": "522",
      "reporter": "U.S.",
      "page": "262",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "118 S. Ct. 753",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 695",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 636",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "522 U.S. 262",
        "volume": "522",
        "reporter": "U.S.",
        "page": "262",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 S. Ct. 753",
        "volume": "118",
        "reporter": "S. Ct.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 L. Ed. 2d 695",
        "volume": "139",
        "reporter": "L. Ed. 2d",
        "page": "695",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 636",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "522 U.S. 262",
    "official_selection": {
      "court_class": "scotus",
      "selected": "522 U.S. 262",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-265",
      "page": null,
      "quote": "--- # LaChance v. Erickson *522 U.S. 262 (1998)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Several federal employees were the subject of agency adverse actions for misconduct, and each made false statements to agency investigators denying the charged conduct. The agencies added a false-statement charge and relied on it in part. The Merit Systems Protection Board upheld the penalties based on the underlying misconduct but overturned the false-statement charges, and the Court of Appeals for the Federal Circuit agreed, reasoning that due process barred charging an employee for denying the underlying charge. The Director of the Office of Personnel Management sought review. ## Issue Whether the Due Process Clause or the Civil Service Reform Act precludes a federal agency from sanctioning an employee for making false statements to the agency in response to an underlying charge of employment-related misconduct. ## Rule No. There is no right to lie, even within a right to be heard. Quoting *Bryson*:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-267",
      "page": null,
      "quote": "If answering an agency's investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-268",
      "page": null,
      "quote": "[W]e hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "LaChance v. Erickson",
    "varies_by_point": false,
    "scope_note": "Good law; marks the boundary of the Garrity line \u2014 the privilege lets a public employee stay silent, but not lie.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Douglas M. Wright v. United States Postal Service",
          "cluster_id": 765216,
          "cite": [
            "183 F.3d 1328",
            "1999 U.S. App. LEXIS 13194",
            "1999 WL 391364"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Stevenson v. Carroll",
          "cluster_id": 1395962,
          "cite": [
            "495 F.3d 62",
            "2007 WL 2164165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73222,
          "cite": [
            "153 F.3d 1233",
            "1998 U.S. App. LEXIS 38861",
            "1998 WL 564374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veal",
          "cluster_id": 73223,
          "cite": [
            "153 F.3d 1233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Geiken",
          "cluster_id": 1755481,
          "cite": [
            "28 S.W.3d 553",
            "2000 Tex. Crim. App. LEXIS 90",
            "2000 WL 1468654"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joshua v. City of Gainesville",
          "cluster_id": 1140033,
          "cite": [
            "768 So. 2d 432",
            "25 Fla. L. Weekly Supp. 641",
            "2000 Fla. LEXIS 1751",
            "2000 WL 1227755"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Azad Haji Abdullah",
          "cluster_id": 3133306,
          "cite": [
            "158 Idaho 386",
            "348 P.3d 1",
            "2015 Ida. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aubrey v. Koppes",
          "cluster_id": 4786583,
          "cite": [
            "975 F.3d 995"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hale v. Fox",
          "cluster_id": 4239796,
          "cite": [
            "829 F.3d 1162",
            "2016 U.S. App. LEXIS 13155",
            "2016 WL 3902561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph A. Kirschenbaum, A/K/A Ari Kirschenbaum, Appeal Of: Julie Kirschenbaum",
          "cluster_id": 758074,
          "cite": [
            "156 F.3d 784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Xy, LLC v. Trans Ova Genetics, L.C.",
          "cluster_id": 4500454,
          "cite": [
            "890 F.3d 1282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elliott v. Martinez",
          "cluster_id": 626933,
          "cite": [
            "675 F.3d 1241",
            "2012 U.S. App. LEXIS 7096",
            "2012 WL 1153488"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Psc Vsmpo-Avismo Corp. v. United States",
          "cluster_id": 805388,
          "cite": [
            "688 F.3d 751",
            "2012 WL 3055876",
            "34 I.T.R.D. (BNA) 1737",
            "2012 U.S. App. LEXIS 15638"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sears v. State",
          "cluster_id": 1636585,
          "cite": [
            "91 S.W.3d 451",
            "2002 Tex. App. LEXIS 8309",
            "2002 WL 31627990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frey Corporation v. City of Peoria, Illinois",
          "cluster_id": 2709391,
          "cite": [
            "735 F.3d 505",
            "2013 WL 4257891",
            "2013 U.S. App. LEXIS 17123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. William Little",
          "cluster_id": 3216832,
          "cite": [
            "499 Mich. 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carlin",
          "cluster_id": 2254756,
          "cite": [
            "58 Cal. Rptr. 3d 495",
            "150 Cal. App. 4th 322",
            "2007 Daily Journal DAR 5883",
            "2007 Cal. Daily Op. Serv. 4622",
            "2007 Cal. App. LEXIS 658"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. Total Health Care, Inc.",
          "cluster_id": 2070848,
          "cite": [
            "709 A.2d 142",
            "349 Md. 499",
            "1998 Md. LEXIS 313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alisal Water Corporation Toro Water Service, Inc. North Monterey County Water Service, Inc. Moss Landing Water Service, Inc. Natholyn P. Adcock Robert T. Adcock, United States of America v. Alisal Water Corporation Toro Water Service, Inc. Robert T. Adcock North Monterey County Water Service, Inc. Moss Landing Water Service, Inc. Natholyn P. Adcock, and Patricia Adcock Bruce Pierson David M. Simcho, John W. Richardson, Receiver",
          "cluster_id": 792691,
          "cite": [
            "431 F.3d 643",
            "62 ERC (BNA) 1009",
            "2005 U.S. App. LEXIS 27271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neifert v. Department of the Environment",
          "cluster_id": 2320041,
          "cite": [
            "910 A.2d 1100",
            "395 Md. 486",
            "64 ERC (BNA) 1685",
            "2006 Md. LEXIS 754"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sullivan v. Barnett",
          "cluster_id": 752420,
          "cite": [
            "139 F.3d 158"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hardy v. State",
          "cluster_id": 2174351,
          "cite": [
            "50 S.W.3d 689",
            "2001 Tex. App. LEXIS 4458",
            "2001 WL 739242"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Department of Public Safety v. Story",
          "cluster_id": 1880958,
          "cite": [
            "115 S.W.3d 588",
            "2003 Tex. App. LEXIS 6040",
            "2003 WL 21665542"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "LaChance v. Erickson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118163) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(118163)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMiZzPTI0NzUxNTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118163%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 22,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118163)",
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
    "complete_query": "cites:(118163)",
    "indexed_citing_opinions": 125,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118163,
        "count": 125,
        "count_source": "search"
      }
    ],
    "citation_count": 220,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/lachance-v-erickson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcxNjc3NjQmcz01MzEzMzU5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118163%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118163,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 106221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 107265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 108001,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 109922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 110267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 110331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 111372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 111603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 112821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118163,
        "cited_id": 722408,
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
    "date_created": "2026-07-05T10:42:02Z",
    "date_modified": "2026-07-06T08:11:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:46:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:42:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — LaChance v. Erickson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b440-4">
<span citation-index="1" class="star-pagination" label="264"> 
   *264
   </span>
  CHIEF Justice Rehnquist
 </author>
<p id="AEn">
  delivered the opinion of the Court.
 </p>
<p id="b440-5">
  The question presented by this action is whether either the Due Process Clause or the Civil Service Reform Act of 1978 (CSRA), <span class="citation no-link">5 U. S. C. § 1101</span>
  <em>
   et seq.,
  </em>
  precludes a federal agency from sanctioning an employee for making false statements to the agency regarding alleged employment-related misconduct on the part of the employee. We hold that they do not.
 </p>
<p id="b440-6">
  Respondents Walsh, Erickson, Kye, Barrett, Roberts, and McManus are Government employees who were the subject of adverse actions by the various agencies for which they worked. Each employee made false statements to agency investigators with respect to the misconduct with which they were charged. In each ease, the agency additionally charged the false statement as a ground for adverse action, and the action taken in each was based in part on the added charge. The employees separately appealed the actions taken against them to the Merit Systems Protection Board (Board). The Board upheld that portion of the penalty based on the underlying charge in each case, but overturned the false statement charge. The Board further held that an employee’s false statements could not be used for purposes of impeaching the employee’s credibility, nor could they be considered in setting the appropriate punishment for the employee’s underlying misconduct. Finally, the Board held that an agency may not charge an employee with failure to report an act of fraud when reporting such fraud would tend to implicate the employee in employment-related misconduct.
 </p>
<p id="b440-7">
  The Director of the Office of Personnel Management appealed each of these decisions by the Board to the Court of Appeals for the Federal Circuit. In a consolidated appeal involving the cases of Walsh, Erickson, Kye, Barrett, and Roberts, that court agreed with the Board that no penalty could be based on a false denial of the underlying claim.
  <span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
<em>
   King
  </em>
  v.
  <em>
   Erickson,
  </em>
  <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/" aria-description="Citation for case: King v. Erickson">89 F. 3d 1575</a></span> (1996). Citing the Fifth Amendment’s Due Process Clause, the court held that “an agency may not charge an employee with falsification or a similar charge on the ground of the employee’s denial of another charge or of underlying facts relating to that other charge,” nor may “[d]enials of charges and related facts ... he considered in determining a penalty.”
  <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/#1585" aria-description="Citation for case: King v. Erickson"><em>
   Id.,
  </em>
  at 1585</a></span>. In a separate unpublished decision, judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%203d/92/1208/">92 F. 3d 1208</a></span> (1996), the Court of Appeals affirmed the Board’s reversal of the false statement charge against McManus as well as the Board’s conclusion that an employee’s “false statements . . : may not be considered” even for purposes of impeachment.
  <em>
   McManus
  </em>
  v.
  <em>
   Department of Justice,
  </em>
  66 MSPR 564, 568 (1995).
 </p>
<p id="b441-5">
  We granted certiorari in both cases, <span class="citation multiple-matches"><a href="/c/U.%20S./521/1117/">521 U. S. 1117</a></span> (1997), and now reverse. In
  <em>
   Bryson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/" aria-description="Citation for case: Bryson v. United States">396 U. S. 64</a></span> (1969), we said: “Our legal system provides methods for challenging the Government’s right to ask questions — lying is not one of them. A citizen may decline to answer the question, or answer it honestly, but he cannot with impunity knowingly and willfully answer with a falsehood.”
  <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/#72" aria-description="Citation for case: Bryson v. United States"><em>
   Id.,
  </em>
  at 72</a></span> (footnote omitted). We find it impossible to square the result reached by the Court of Appeals in the present case with our holding in
  <em>
   <span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/" aria-description="Citation for case: Bryson v. United States">Bryson</a></span>
  </em>
  and in other cases of similar import.
 </p>
<p id="b441-6">
  Title <span class="citation no-link">5 U. S. C. § 7513</span>(a) provides that an agency may impose the sort of penalties involved here “for such eause as will promote the efficiency of the service.” It then sets forth four procedural rights accorded to the employee against whom adverse action is proposed. The agency must:
 </p>
<blockquote id="b441-7">
  (1) give the employee “at least 30 days’ advance written notice”; (2) allow the employee “a reasonable time, but not less than 7 days, to answer orally and in writing and to furnish . . . evidence in support of the answer”; (3) permit the employee to “be represented by an attorney or other representative”; and (4) provide the employee ,
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  with “a written decision and the specific reasons therefor.” <span class="citation no-link">5 U. S. C. § 7513</span>(b).
 </blockquote>
<p id="b442-5">
  In these carefully delineated rights there is no hint of any right to “put the government to its proof” by falsely denying the charged conduct. Such a right, then, if it exists at all, must come from the Fifth Amendment of the United States Constitution.
 </p>
<p id="b442-6">
  The Fifth Amendment be deprived of life, liberty, or property, without due process of law . . . .” The Court of Appeals stated that “it is undisputed that the government employees here had a protected property interest in their employment,” <span class="citation" data-id="722408"><a href="/opinion/722408/king-v-erickson/#1581" aria-description="Citation for case: King v. Erickson">89 F. 3d, at 1581</a></span>, and we assume that to be the ease for purposes of our decision.
 </p>
<p id="b442-7">
  The core of due process is ingful opportunity to be heard.
  <em>
   Cleveland Bd. of Ed.
  </em>
  v.
  <em>
   Loudermill,
  </em>
  <span class="citation" data-id="9429945"><a href="/opinion/111372/cleveland-board-of-education-v-loudermill/#542" aria-description="Citation for case: Cleveland Board of Education v. Loudermill">470 U. S. 532, 542</a></span> (1985). But we reject, on the basis of both precedent and principle, the view expressed by the Court of Appeals in this action that a “meaningful opportunity to be heard” includes a right to make false statements with respect to the charged conduct.
 </p>
<p id="b442-8">
  It is well established that a testify does not include the light to commit perjury.
  <em>
   Nix
  </em>
  v.
  <em>
   Whiteside,
  </em>
  <span class="citation" data-id="9430360"><a href="/opinion/111603/nix-v-whiteside/#173" aria-description="Citation for case: Nix v. Whiteside">475 U. S. 157, 173</a></span> (1986);
  <em>
   United States
  </em>
  v.
  <em>
   Havens,
  </em>
  <span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/#626" aria-description="Citation for case: United States v. Havens">446 U. S. 620, 626</a></span> (1980);
  <em>
   United States
  </em>
  v.
  <em>
   Grayson,
  </em>
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/#54" aria-description="Citation for case: United States v. Grayson">438 U. S. 41, 54</a></span> (1978). Indeed, in
  <em>
   United States
  </em>
  v.
  <em>
   Dunnigan,
  </em>
  <span class="citation" data-id="112821"><a href="/opinion/112821/united-states-v-dunnigan/#97" aria-description="Citation for case: United States v. Dunnigan">507 U. S. 87, 97</a></span> (1993), we held that a court could, consistent with the Constitution, enhance a criminal defendant’s sentence based on a finding that he perjured himself at trial.
 </p>
<p id="b442-9">
  Witnesses appearing before a grand jury under oath are likewise required to testify truthfully, on pain of being prosecuted for perjury.
  <em>
   United States
  </em>
  v.
  <em>
   Wong,
  </em>
  <span class="citation" data-id="109658"><a href="/opinion/109658/united-states-v-wong/" aria-description="Citation for case: United States v. Wong">431 U. S. 174</a></span> (1977). There we said that “the predicament of being forced to choose between incriminatory truth and falsehood... does not justify perjury.”
  <span class="citation" data-id="109658"><a href="/opinion/109658/united-states-v-wong/#178" aria-description="Citation for case: United States v. Wong"><em>
   Id.,
  </em>
  at 178</a></span>. Similarly, one who files a
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  false affidavit required by statute may be fined and imprisoned.
  <em>
   Dennis
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">384 U. S. 855</a></span> (1966).
 </p>
<p id="b443-5">
  The Court of Appeals sought to distinguish these eases on the ground that the defendants in them had been under oath, while here the respondents were not. The fact that respondents were not under oath, of course, negates a charge of perjury, but that is not the charge brought against them. They were charged with making false statements during the course of an agency investigation, a charge that does not require that the statements be made under oath. While the Court of Appeals would apparently permit the imposition of punishment for the former but not the latter, we fail to see how the presence or absence of an oath is material to the due process inquiry.
 </p>
<p id="b443-6">
  The Court of Appeals also relied on its fear that if employees were not allowed to make false statements, they might “be coerced into admitting the misconduct, whether they believe that they are guilty or not, in order to avoid the more severe penalty of removal possibly resulting from a falsification charge.” App. to Pet. for Cert. 16a-17a. But we rejected a similar claim in
  <em>
   United States
  </em>
  v.
  <em>
   Grayson,
  </em>
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/" aria-description="Citation for case: United States v. Grayson">438 U. S. 41</a></span> (1978). There a sentencing judge took into consideration his belief that the defendant had testified falsely at his trial. The defendant argued before us that such a practice would inhibit the exercise of the right to testify truthfully in the proceeding. We described that contention as “entirely frivolous.”
  <span class="citation" data-id="9427313"><a href="/opinion/109922/united-states-v-grayson/#55" aria-description="Citation for case: United States v. Grayson"><em>
   Id.,
  </em>
  at 55</a></span>.
 </p>
<p id="b443-7">
  If answering an agency’s investigatory question could expose an employee to a criminal prosecution, he may exercise his Fifth Amendment right to remain silent. See
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#67" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 67</a></span> (1906);
  <em>
   United States
  </em>
  v.
  <em>
   Ward,
  </em>
  <span class="citation" data-id="9428052"><a href="/opinion/110331/united-states-v-ward/#248" aria-description="Citation for case: United States v. Ward">448 U. S. 242, 248</a></span> (1980). It may well be that an agency, in ascertaining the truth or falsity of the charge, would take into consideration the failure of the employee to respond. See
  <em>
   Baxter
  </em>
  v.
  <em>
   Palmigiano,
  </em>
  <span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#318" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 318</a></span> (1976) (discussing the “prevailing rule that the Fifth Amendment does not for
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  bid adverse inferences against parties to civil actions when they refuse to testify”). But there is nothing inherently irrational about such an investigative posture. See
  <em>
   Konigsberg
  </em>
  v.
  <em>
   State Bar of Cal.,
  </em>
  <span class="citation" data-id="9422190"><a href="/opinion/106221/konigsberg-v-state-bar-of-cal/" aria-description="Citation for case: Konigsberg v. State Bar of Cal.">366 U. S. 36</a></span> (1961).
 </p>
<p id="b444-5">
  For these reasons, we hold that a Government agency may take adverse action against an employee because the employee made false statements in response to an underlying charge of misconduct. The judgments of the Court of Appeals are therefore
 </p>
<p id="b444-6">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---
