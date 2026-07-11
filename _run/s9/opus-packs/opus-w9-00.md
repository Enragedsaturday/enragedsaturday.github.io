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

## GROUP: _overhaul2/lake/cases/Oregon v. Bradshaw.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Oregon v. Bradshaw"
type: case
citation: "462 U.S. 1039 (1983)"
parallel_cite: "103 S. Ct. 2830; 77 L. Ed. 2d 405; 51 U.S.L.W. 4940"
neutral_cite: 1983 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-06-23
docket: 81-1857
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1983-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Bradshaw
  varies_by_point: false
  scope_note: "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110987/oregon-v-bradshaw/"
  cluster_id: 110987
  opinion_id: 9429286
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "edwards", "initiation"]
holding: "After invoking counsel, a suspect 'initiates' further communication under Edwards only by a statement evincing a desire to open a generalized discussion about the investigation (not a routine request); even then, any resulting statement is admissible only if the suspect also validly waived counsel under the totality of the circumstances."
lake:
  record_id: Oregon v. Bradshaw
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Bradshaw

*462 U.S. 1039 (1983)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After being arrested and given [[Miranda and Custodial Interrogation|Miranda warnings]], Bradshaw invoked his right to counsel and questioning stopped. Sometime later, while being transferred, he asked an officer, "Well, what is going to happen to me now?" The officer reminded him he need not talk, and a conversation followed; Bradshaw later took a polygraph and made incriminating statements. The issue was whether *Bradshaw* — not the police — had reopened communication under *[[Edwards v. Arizona]]*.

## Issue
After a suspect invokes the right to counsel, what does it mean for the suspect to "initiate" further communication so that interrogation may resume — and what else must the State show before the resulting statements are admissible?

## Rule
*[[Edwards v. Arizona|Edwards]]* bars further interrogation after an invocation of counsel unless the accused himself "initiates" further communication. A routine inquiry does not count: "There are some inquiries, such as a request for a drink of water or a request to use a telephone, that are so routine that they cannot be fairly said to represent a desire on the part of an accused to open up a more generalized discussion relating directly or indirectly to the investigation." — 462 U.S. at 1045 (plurality opinion). ^pin-1045

Initiation requires a statement that "evinced a willingness and a desire for a generalized discussion about the investigation." — *Id.* at 1045–46. ^pin-1046

Initiation is only the **first** step: the second is whether, under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], the accused then knowingly and intelligently waived the right to counsel he had previously invoked.

## Application
Bradshaw's question — "Well, what is going to happen to me now?" — was not a routine request about the mechanics of custody; it evinced a desire to discuss the investigation, so it "initiated" further communication. With that step satisfied, the plurality concluded that on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] Bradshaw thereafter validly waived his right to counsel, so the later statements were admissible.

## Conclusion
Bradshaw initiated the renewed dialogue and validly waived counsel; the statements were admissible. The Oregon Court of Appeals' suppression was reversed. *Bradshaw* fixes the two-step *[[Edwards v. Arizona|Edwards]]* analysis: (1) did the accused initiate? (2) was there a valid waiver under the totality?

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Although a plurality, the two-step initiation-then-waiver framework stated here is the settled application of [[Edwards v. Arizona]] and remains good law.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Oregon v. Bradshaw*, 462 U.S. 1039 (1983) — https://www.courtlistener.com/opinion/110987/oregon-v-bradshaw/ — pinpoints: 1045, 1046 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bb80e3bc8168b07a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Oregon v. Bradshaw"}, "payload": {"all": [{"cite": "462 U.S. 1039", "page": "1039", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "462"}, {"cite": "103 S. Ct. 2830", "page": "2830", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "77 L. Ed. 2d 405", "page": "405", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "77"}, {"cite": "1983 U.S. LEXIS 82", "page": "82", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4940", "page": "4940", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "462 U.S. 1039", "official": {"cite": "462 U.S. 1039", "page": "1039", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "462"}, "official_selection_present": true, "record_id": "Oregon v. Bradshaw"}}
{"assertion_id": "608dd68225a8565a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1045", "record_id": "Oregon v. Bradshaw"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1045", "pinpoint_status": "slip-only", "quote": "further communication so that interrogation may resume — and what else must the State show before the resulting statements are admissible? ## Rule *Edwards* bars further interrogation after an invocation of counsel unless the accused himself", "quote_fidelity": "mismatch", "record_id": "Oregon v. Bradshaw", "star_marker": null}}
{"assertion_id": "61a5e46dff023478", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1046", "record_id": "Oregon v. Bradshaw"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1046", "pinpoint_status": "slip-only", "quote": "evinced a willingness and a desire for a generalized discussion about the investigation.", "quote_fidelity": "mismatch", "record_id": "Oregon v. Bradshaw", "star_marker": null}}
{"assertion_id": "87b95ccf8ebde1bd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Oregon v. Bradshaw"}, "payload": {"as_of_content": "1983-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Oregon v. Bradshaw", "scope_note": "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law.", "varies_by_point": false}}
```

### lake record — Oregon v. Bradshaw

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Bradshaw",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Bradshaw",
    "case_name_short": "Bradshaw",
    "case_name_full": "Oregon v. Bradshaw",
    "input_case_name": "Oregon v. Bradshaw",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-06-23",
    "year": 1983,
    "docket": "81-1857",
    "cluster_id": 110987,
    "lead_opinion_id": 9429286,
    "sibling_ids": [
      110987,
      9429286,
      9429287,
      9429288
    ],
    "absolute_url": "/opinion/110987/oregon-v-bradshaw/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "462 U.S. 1039",
      "volume": "462",
      "reporter": "U.S.",
      "page": "1039",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 2830",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 405",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4940",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4940",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 82",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "462 U.S. 1039",
        "volume": "462",
        "reporter": "U.S.",
        "page": "1039",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 2830",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "2830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 2d 405",
        "volume": "77",
        "reporter": "L. Ed. 2d",
        "page": "405",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 82",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4940",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4940",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "462 U.S. 1039",
    "official_selection": {
      "court_class": "scotus",
      "selected": "462 U.S. 1039",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1045",
      "page": null,
      "quote": "further communication so that interrogation may resume \u2014 and what else must the State show before the resulting statements are admissible? ## Rule *Edwards* bars further interrogation after an invocation of counsel unless the accused himself",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1046",
      "page": null,
      "quote": "evinced a willingness and a desire for a generalized discussion about the investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1983-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Bradshaw",
    "varies_by_point": false,
    "scope_note": "Plurality; the two-step Edwards initiation/waiver framework it states is settled and good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4892536,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 4671866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rowland v. State",
          "cluster_id": 10367127,
          "cite": [
            "306 Ga. 59"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Boyd",
          "cluster_id": 4259208,
          "cite": [
            "360 Or. 302",
            "380 P.3d 941",
            "2016 Ore. LEXIS 612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Hill, E.",
          "cluster_id": 2754405,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Letkowski",
          "cluster_id": 6589954,
          "cite": [
            "83 Mass. App. Ct. 847",
            "991 N.E.2d 1106",
            "2013 WL 3242668",
            "2013 Mass. App. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
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
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1450662,
          "cite": [
            "275 S.W.3d 29",
            "2008 WL 2840151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane1_negative"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1869722,
          "cite": [
            "451 So. 2d 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solem v. Stumes",
          "cluster_id": 111112,
          "cite": [
            "79 L. Ed. 2d 579",
            "104 S. Ct. 1338",
            "465 U.S. 638",
            "1984 U.S. LEXIS 36",
            "52 U.S.L.W. 4307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Memro",
          "cluster_id": 1375029,
          "cite": [
            "905 P.2d 1305",
            "11 Cal. 4th 786",
            "47 Cal. Rptr. 2d 219",
            "95 Daily Journal DAR 15919",
            "95 Cal. Daily Op. Serv. 9091",
            "1995 Cal. LEXIS 6793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mickey",
          "cluster_id": 1226896,
          "cite": [
            "818 P.2d 84",
            "54 Cal. 3d 612",
            "286 Cal. Rptr. 801",
            "91 Daily Journal DAR 13544",
            "91 Cal. Daily Op. Serv. 8732",
            "1991 Cal. LEXIS 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. State",
          "cluster_id": 2382336,
          "cite": [
            "504 A.2d 1096",
            "1986 Del. LEXIS 1040"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Powell",
          "cluster_id": 2690788,
          "cite": [
            "2012 Ohio 2577",
            "132 Ohio St. 3d 233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Marshall",
          "cluster_id": 1425683,
          "cite": [
            "790 P.2d 676",
            "50 Cal. 3d 907",
            "269 Cal. Rptr. 269",
            "1990 Cal. LEXIS 1959"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 1801680,
          "cite": [
            "46 Cal. 4th 539",
            "208 P.3d 78",
            "94 Cal. Rptr. 3d 322",
            "2009 Cal. LEXIS 4707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 2689817,
          "cite": [
            "2000 Ohio 187",
            "90 Ohio St. 3d 403",
            "739 N.E.2d 300"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Etheridge v. State",
          "cluster_id": 2372478,
          "cite": [
            "903 S.W.2d 1",
            "1994 Tex. Crim. App. LEXIS 83",
            "1994 WL 273325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
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
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cruz",
          "cluster_id": 2584939,
          "cite": [
            "44 Cal. 4th 636",
            "187 P.3d 970",
            "80 Cal. Rptr. 3d 126",
            "2008 Cal. LEXIS 9079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Bradshaw:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjE2NzcxMjAwMDAwJnM9Mjg3OTQ0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTEmcz0xNTIwMzA5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
        "reviewed": 28,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 28,
        "triage_read": 0,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110987 OR 9429286 OR 9429287 OR 9429288)",
    "indexed_citing_opinions": 824,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110987,
        "count": 732,
        "count_source": "search"
      },
      {
        "opinion_id": 9429286,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9429287,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429288,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1351,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-bradshaw.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzE5ODQmcz05NDUwOTMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110987+OR+9429286+OR+9429287+OR+9429288%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110987,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 392817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 403900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 406019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 409288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1115589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1159238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1356056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1363682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1385367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1767568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1771028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 1962224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2075223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2144643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2280262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2362374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110987,
        "cited_id": 2385822,
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
    "date_created": "2026-07-05T16:16:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:16:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Bradshaw

```
<opinion type="majority">
<author id="b1086-11">Justice Rehnquist</author>
<p id="AotR">announced the judgment of the Court and delivered an opinion, in which The Chief Justice, Justice White, and Justice O’Connor joined.</p>
<p id="b1086-12">After a bench trial in an Oregon trial court, respondent James Edward Bradshaw was convicted of the offenses of <page-number citation-index="1" label="1041">*1041</page-number>first-degree manslaughter, driving while under the influence of intoxicants, and driving while his license was revoked. The Oregon Court of Appeals reversed his conviction, holding that an inquiry he made of a police officer at the time he was in custody did not “initiate” a conversation with the officer, and that therefore statements by the respondent growing out of that conversation should have been excluded from evidence under <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). We granted certiorari to review this determination. <span class="citation multiple-matches"><a href="/c/U.%20S./459/966/">459 U. S. 966</a></span> (1982).</p>
<p id="b1087-5">In September 1980, Oregon police were investigating the death of one Lowell Reynolds in Tillamook County. Reynolds’ body had been found in his wrecked pickup truck, in which he appeared to have been a passenger at the time the vehicle left the roadway, struck a tree and an embankment, and finally came to rest on its side in a shallow creek. Reynolds had died from traumatic injury, coupled with asphyxia by drowning. During the investigation of Reynolds’ death, respondent was asked to accompany a police officer to the Rockaway Police Station for questioning.</p>
<p id="b1087-6">Once at the station, respondent was advised of his rights as required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Respondent then repeated to the police his earlier account of the events of the evening of Reynolds’ death, admitting that he had provided Reynolds and others with liquor for a party at Reynolds’ house, but denying involvement in the traffic accident that apparently killed Reynolds. Respondent suggested that Reynolds might have met with foul play at the hands of the assailant whom respondent alleged had struck him at the party.</p>
<p id="b1087-7">At this point, respondent was placed under arrest for furnishing liquor to Reynolds, a minor, and again advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. A police officer then told respondent the officer’s theory of how the traffic accident that killed Reynolds occurred; a theory which placed respondent behind the wheel of the vehicle. Respondent again denied his involvement, and said “I do want an attorney before it goes very <page-number citation-index="1" label="1042">*1042</page-number>much further.” App. 72. The officer immediately terminated the conversation.</p>
<p id="b1088-5">Sometime later respondent was transferred from the Rock-away Police Station to the Tillamook County Jail, a distance of some 10 or 15 miles. Either just before, or during, his trip from Rockaway to Tillamook, respondent inquired of a police officer, “Well, what is going to happen to me now?” The officer answered by saying: “You do not have to talk to me. You have requested an attorney and I don’t want you talking to me unless you so desire because anything you say — because—since you have requested an attorney, you know, it has to be at your own free will.” <em>Id., </em>at 16. See <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#951" aria-description="Citation for case: State v. Bradshaw">54 Ore. App. 949, 951</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1011" aria-description="Citation for case: State v. Bradshaw">636 P. 2d 1011, 1011-1012</a></span> (1981). Respondent said he understood. There followed a discussion between respondent and the officer concerning where respondent was being taken and the offense with which he would be charged. The officer suggested that respondent might help himself by taking a polygraph examination. Respondent agreed to take such an examination, saying that he was willing to do whatever he could to clear up the matter.</p>
<p id="b1088-6">The next day, following another reading to respondent of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and respondent’s signing a written waiver of those rights, the polygraph was administered. At its conclusion, the examiner told respondent that he did not believe respondent was telling the truth. Respondent then recanted his earlier story, admitting that he had been at the wheel of the vehicle in which Reynolds was killed, that he had consumed a considerable amount of alcohol, and that he had passed out at the wheel before the vehicle left the roadway and came to rest in the creek.</p>
<p id="b1088-7">Respondent was charged with first-degree manslaughter, driving while under the influence of intoxicants, and driving while his license was revoked. His motion to suppress the statements described above was denied, and he was found guilty after a bench trial. The Oregon Court of Appeals, relying on our decision in <em>Edwards </em>v. <em>Arizona, supra, </em>re<page-number citation-index="1" label="1043">*1043</page-number>versed, concluding that the statements had been obtained in violation of respondent’s Fifth Amendment rights. <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/" aria-description="Citation for case: State v. Bradshaw">54 Ore. App. 949</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/" aria-description="Citation for case: State v. Bradshaw">636 P. 2d 1011</a></span> (1981). We now conclude that the Oregon Court of Appeals misapplied our decision in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em></p>
<p id="b1089-5">In <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>the defendant had voluntarily submitted to questioning but later stated that he wished an attorney before the discussions continued. The following day detectives accosted the defendant in the county jail, and when he refused to speak with them he was told that “he had” to talk. We held that subsequent incriminating statements made without his attorney present violated the rights secured to the defendant by the Fifth and Fourteenth Amendments to the United States Constitution. In our opinion, we stated:</p>
<blockquote id="b1089-6">“[Although we have held that after initially being advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, the accused may himself validly waive his rights and respond to interrogation, see <em>North Carolina </em>v. <em>Butler, </em>[<span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 372-376</a></span> (1979)], the Court has strongly indicated that additional safeguards are necessary when the accused asks for counsel; and we now hold that when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights. We further hold that <em>an accused, such as [the defendant], having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the </em>police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span> (footnote omitted) (emphasis added).</blockquote>
<p id="b1089-7">Respondent’s question in the present case, “Well, what is going to happen to me now?”, admittedly was asked prior to <page-number citation-index="1" label="1044">*1044</page-number>respondent’s being “subjected] to further interrogation by the authorities.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Id., </em>at 484</a></span>. The Oregon Court of Appeals stated that it did not “construe defendant’s question about what was going to happen to him to have been a waiver of his right to counsel, invoked only minutes before. . ..” <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#953" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 953</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1013" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1013</a></span>. The Court of Appeals, after quoting relevant language from <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>concluded that “under the reasoning enunciated in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>defendant did not make a valid waiver of his Fifth Amendment rights, and his statements were inadmissible.” <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></em></p>
<p id="b1090-5">We think the Oregon Court of Appeals misapprehended the test laid down in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>We did not there hold that the “initiation” of a conversation by a defendant such as respondent would amount to a waiver of a previously invoked right to counsel; we held that after the right to counsel had been asserted by an accused, further interrogation of the accused should not take place “unless the accused himself initiates further communication, exchanges, or conversations with the police.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. This was in effect a prophylactic rule, designed to protect an accused in police custody from being badgered by police officers in the manner in which the defendant in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>was. We recently restated the requirement in <em>Wyrick </em>v. <em>Fields, </em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/#46" aria-description="Citation for case: Wyrick v. Fields">459 U. S. 42, 46</a></span> (1982) <em>(per curiam), </em>to be that before a suspect in custody can be subjected to further interrogation after he requests an attorney there must be a showing that the “suspect himself initiates dialogue with the authorities.”</p>
<p id="b1090-6">But even if a conversation taking place after the accused has “expressed his desire to deal with the police only through counsel,” is initiated by the accused, where reinterrogation follows, the burden remains upon the prosecution to show that subsequent events indicated a waiver of the Fifth Amendment right to have counsel present during the interrogation. This is made clear in the following footnote to our <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>opinion:</p>
<blockquote id="b1090-7">“If, as frequently would occur in the course of a meeting initiated by the accused, the conversation is not <page-number citation-index="1" label="1045">*1045</page-number>wholly one-sided, it is likely that the officers will say or do something that clearly would be ‘interrogation.’ In that event, the question would be whether a valid waiver of the right to counsel and the right to silence had occurred, that is, <em>whether the purported waiver was knowing and intelligent and found to be so under the totality of the circumstances, </em>including the necessary fact that the accused, not the police, reopened the dialogue with the authorities.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#486" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 486, n. 9</a></span> (emphasis added).</blockquote>
<p id="b1091-5">This rule was reaffirmed earlier this Term in <em>Wyrick </em>v. <em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/" aria-description="Citation for case: Wyrick v. Fields">Fields, supra.</a></span></em></p>
<p id="b1091-6">Thus, the Oregon Court of Appeals was wrong in thinking that an “initiation” of a conversation or discussion by an accused not only satisfied the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, but <em>ex proprio vigore </em>sufficed to show a waiver of the previously asserted right to counsel. The inquiries are separate, and clarity of application is not gained by melding them together.</p>
<p id="b1091-7">There can be no doubt in this case that in asking, “Well, what is going to happen to me now?”, respondent “initiated” further conversation in the ordinary dictionary sense of that word. While we doubt that it would be desirable to build a superstructure of legal refinements around the word “initiate” in this context, there are undoubtedly situations where a bare inquiry by either a defendant or by a police officer should not be held to “initiate” any conversation or dialogue. There are some inquiries, such as a request for a drink of water or a request to use a telephone, that are so routine that they cannot be fairly said to represent a desire on the part of an accused to open up a more generalized discussion relating directly or indirectly to the investigation. Such inquiries or statements, by either an accused or a police officer, relating to routine incidents of the custodial relationship, will not generally “initiate” a conversation in the sense in which that word was used in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em></p>
<p id="b1091-8">Although ambiguous, the respondent’s question in this case as to what was going to happen to him evinced a willingness <page-number citation-index="1" label="1046">*1046</page-number>and a desire for a generalized discussion about the investigation; it was not merely a necessary inquiry arising out of the incidents of the custodial relationship. It could reasonably have been interpreted by the officer as relating generally to the investigation. That the police officer so understood it is apparent from the fact that he immediately reminded the accused that “[y]ou do not have to talk to me,” and only after the accused told him that he “understood” did they have a generalized conversation. <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#951" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 951</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1011" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1011-1012</a></span>. On these facts we believe that there was not a violation of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule.</p>
<p id="b1092-5">Since there was no violation of the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule in this case, the next inquiry was “whether a valid waiver of the right to counsel and the right to silence had occurred, that is, whether the purported waiver was knowing and intelligent and found to be so under the totality of the circumstances, including the necessary fact that the accused, not the police, reopened the dialogue with the authorities.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#486" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 486, n. 9</a></span>. As we have said many times before, this determination depends upon “‘the particular facts and circumstances surrounding [the] case, including the background, experience, and conduct of the accused.’” <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 374-375</a></span> (1979) (quoting <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938)). See also <em>Edwards </em>v. <em>Arizona, supra, </em>at 482-483.</p>
<p id="b1092-6">The state trial court made this inquiry and, in the words of the Oregon Court of Appeals, “found that the police made no threats, promises or inducements to talk, that defendant was properly advised of his rights and understood them and that within a short time after requesting an attorney he changed his mind without any impropriety on the part of the police. The court held that the statements made to the polygraph examiner were voluntary and the result of a knowing waiver of his right to remain silent.” <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#952" aria-description="Citation for case: State v. Bradshaw">54 Ore. App., at 952</a></span>, <span class="citation" data-id="1385367"><a href="/opinion/1385367/state-v-bradshaw/#1012" aria-description="Citation for case: State v. Bradshaw">636 P. 2d, at 1012</a></span>.</p>
<p id="b1092-7">We have no reason to dispute these conclusions, based as they are upon the trial court’s firsthand observation of the <page-number citation-index="1" label="1047">*1047</page-number>witnesses to the events involved. The judgment of the Oregon Court of Appeals is therefore reversed, and the cause is remanded for further proceedings.</p>
<p id="b1093-5">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Oregon v. Elstad.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Oregon v. Elstad"
type: case
citation: "470 U.S. 298 (1985)"
parallel_cite: "105 S. Ct. 1285; 84 L. Ed. 2d 222; 53 U.S.L.W. 4244"
neutral_cite: 1985 U.S. LEXIS 60
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-04
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1985-03-04
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Elstad
  varies_by_point: true
  scope_note: "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
  point_overrides:
    - point: legacy-limited-oregon-v-elstad
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Missouri v. Seibert
          cluster_id: 137002
          cite: 542 U.S. 600
          field_ii: limited
      scope_note: "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111364/oregon-v-elstad/"
  cluster_id: 111364
  opinion_id: 9429930
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Missouri v. Seibert]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "unwarned-statement", "waiver"]
holding: "An initial, un-warned but voluntary statement does not automatically taint a later confession; if the suspect is then properly…"
lake:
  record_id: Oregon v. Elstad
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Elstad

*470 U.S. 298 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers came to Elstad's home with a warrant for his arrest in a burglary. Before any *[[Miranda v. Arizona|Miranda]]* warnings, an officer said he believed Elstad was involved, and Elstad admitted, "Yes, I was there." About an hour later at the station, he was given full *[[Miranda v. Arizona|Miranda]]* warnings, waived his rights, and gave a complete written confession.

## Issue
Whether an initial, voluntary but un-Mirandized admission taints a later, properly warned confession.

## Rule
No, absent coercion. "[A]bsent deliberately coercive or improper tactics in obtaining the initial statement, the mere fact that a suspect has made an unwarned admission does not warrant a presumption of compulsion. A subsequent administration of *Miranda* warnings to a suspect who has given a voluntary but unwarned statement ordinarily should suffice to remove the conditions that precluded admission of the earlier statement." — 470 U.S. at 314. ^pin-314

"We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite *Miranda* warnings." — *Id.* at 318. ^pin-318

**As applied to deliberate "question-first" two-step interrogations, this rule was later limited by [[Missouri v. Seibert]]** (see Treatment).

## Application
Elstad's initial "Yes, I was there" was voluntary and not the product of coercive tactics, so it did not create a presumption that his later station-house confession was compelled. Once he received and waived his *[[Miranda v. Arizona|Miranda]]* rights, his subsequent written confession was admissible. The Court reversed the suppression of the second statement.

## Conclusion
The properly warned confession was admissible despite the earlier unwarned admission; the Oregon Court of Appeals' suppression order was reversed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited as applied by [[Missouri v. Seibert]] (2004)**: where officers deliberately use a "question-first, warn-later" two-step technique to undermine *[[Miranda v. Arizona|Miranda]]*, the midstream warnings may be ineffective and the second statement inadmissible. *Elstad* continues to govern the ordinary case of an inadvertent or good-faith failure to warn followed by a properly warned statement. *Elstad* also relies on [[Miranda v. Arizona]] as a prophylactic, not constitutional, rule — a characterization later qualified by [[Dickerson v. United States]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Oregon v. Elstad*, 470 U.S. 298 (1985) — https://www.courtlistener.com/opinion/111364/oregon-v-elstad/ — pinpoints: 314, 318.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "675def41a6215ef5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Oregon v. Elstad"}, "payload": {"all": [{"cite": "470 U.S. 298", "page": "298", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "470"}, {"cite": "105 S. Ct. 1285", "page": "1285", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "84 L. Ed. 2d 222", "page": "222", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1985 U.S. LEXIS 60", "page": "60", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4244", "page": "4244", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "470 U.S. 298", "official": {"cite": "470 U.S. 298", "page": "298", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "470"}, "official_selection_present": true, "record_id": "Oregon v. Elstad"}}
{"assertion_id": "0434bb6141c32af6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-318", "record_id": "Oregon v. Elstad"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-318", "pinpoint_status": "slip-only", "quote": "We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite *Miranda* warnings.", "quote_fidelity": "mismatch", "record_id": "Oregon v. Elstad", "star_marker": null}}
{"assertion_id": "76ef3c5bba6437db", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-314", "record_id": "Oregon v. Elstad"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-314", "pinpoint_status": "slip-only", "quote": "About an hour later at the station, he was given full *Miranda* warnings, waived his rights, and gave a complete written confession. ## Issue Whether an initial, voluntary but un-Mirandized admission taints a later, properly warned confession. ## Rule No, absent coercion.", "quote_fidelity": "mismatch", "record_id": "Oregon v. Elstad", "star_marker": null}}
{"assertion_id": "53496184a22c5743", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Oregon v. Elstad"}, "payload": {"as_of_content": "1985-03-04", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Oregon v. Elstad", "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn.", "varies_by_point": true}}
```

### lake record — Oregon v. Elstad

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Elstad",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Elstad",
    "case_name_short": "Elstad",
    "case_name_full": "Oregon v. Elstad",
    "input_case_name": "Oregon v. Elstad",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-04",
    "year": 1985,
    "docket": null,
    "cluster_id": 111364,
    "lead_opinion_id": 9429930,
    "sibling_ids": [
      111364,
      9429930,
      9429931,
      9429932
    ],
    "absolute_url": "/opinion/111364/oregon-v-elstad/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "470 U.S. 298",
      "volume": "470",
      "reporter": "U.S.",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1285",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 222",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4244",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4244",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 60",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "470 U.S. 298",
        "volume": "470",
        "reporter": "U.S.",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1285",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 2d 222",
        "volume": "84",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 60",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "60",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4244",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4244",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "470 U.S. 298",
    "official_selection": {
      "court_class": "scotus",
      "selected": "470 U.S. 298",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-314",
      "page": null,
      "quote": "About an hour later at the station, he was given full *Miranda* warnings, waived his rights, and gave a complete written confession. ## Issue Whether an initial, voluntary but un-Mirandized admission taints a later, properly warned confession. ## Rule No, absent coercion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-318",
      "page": null,
      "quote": "We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite *Miranda* warnings.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1985-03-04",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Elstad",
    "varies_by_point": true,
    "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn.",
    "point_overrides": [
      {
        "point": "legacy-limited-oregon-v-elstad",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Missouri v. Seibert",
            "cluster_id": 137002,
            "cite": "542 U.S. 600",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Limited as applied to deliberate 'question-first' two-step interrogations by Missouri v. Seibert (2004); Elstad otherwise governs inadvertent/good-faith failures to warn."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": "542 U.S. 600",
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
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
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
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portillo",
          "cluster_id": 3210008,
          "cite": [
            "787 S.E.2d 822",
            "247 N.C. App. 834",
            "2016 N.C. App. LEXIS 619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane1_negative"
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
        "journal_ref": "Oregon v. Elstad:lane1_negative"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leday v. State",
          "cluster_id": 1678149,
          "cite": [
            "983 S.W.2d 713",
            "1998 Tex. Crim. App. LEXIS 172",
            "1998 WL 870371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillips v. People",
          "cluster_id": 4636609,
          "cite": [
            "2019 CO 72",
            "443 P.3d 1016"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Russell",
          "cluster_id": 1296847,
          "cite": [
            "882 P.2d 747",
            "125 Wash. 2d 24",
            "63 U.S.L.W. 2291",
            "1994 Wash. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1653372,
          "cite": [
            "836 S.W.2d 530",
            "1992 Tenn. LEXIS 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
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
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samayoa",
          "cluster_id": 5607879,
          "cite": [
            "15 Cal. 4th 795",
            "938 P.2d 2",
            "97 Daily Journal DAR 7699",
            "64 Cal. Rptr. 2d 400",
            "97 Cal. Daily Op. Serv. 4760",
            "1997 Cal. LEXIS 2966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connecticut v. Barrett",
          "cluster_id": 111796,
          "cite": [
            "93 L. Ed. 2d 920",
            "107 S. Ct. 828",
            "479 U.S. 523",
            "1987 U.S. LEXIS 419",
            "55 U.S.L.W. 4151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Elstad:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQzNTcxMjAwMDAwJnM9NDI5MjY1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTkmcz03NTEzNDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 0,
        "triage_snippet_classified": 45
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111364 OR 9429930 OR 9429931 OR 9429932)",
    "indexed_citing_opinions": 1760,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111364,
        "count": 1568,
        "count_source": "search"
      },
      {
        "opinion_id": 9429930,
        "count": 232,
        "count_source": "search"
      },
      {
        "opinion_id": 9429931,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429932,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2824,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-elstad.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMzg3OTYmcz0xMDI4MTUxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111364+OR+9429930+OR+9429931+OR+9429932%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111364,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 260072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 262430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 263485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 275353,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 280455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 280782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 315338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 317110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 336178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 339054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 348792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 349630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 397374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 414117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 877624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1112895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1144156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1145231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1161498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1170008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1180469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1231742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1234251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1248061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1306478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1320417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1360101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1419581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1472767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1496973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1502926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1519558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1566744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1631959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1634761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1635158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1758320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1837744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1851084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1962849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 1992428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2012195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2023548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2064265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2084604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2093616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2096024,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2112079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2122160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2141638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2195849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2211745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2225068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2280368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2285307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2609123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111364,
        "cited_id": 2615164,
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
    "date_created": "2026-07-05T16:20:09Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:20:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Elstad

```
<opinion type="majority">
<author id="b356-5">Justice O’Connor</author>
<p id="AQH">delivered the opinion of the Court.</p>
<p id="b356-6">This case requires us to decide whether an initial failure of law enforcement officers to administer the warnings required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), without more, “taints” subsequent admissions made after a suspect has been fully advised of and has waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Respondent, Michael James Elstad, was convicted of burglary by an Oregon trial court. The Oregon Court of Appeals reversed, holding that respondent’s signed confession, although voluntary, was rendered inadmissible by a prior remark made in response to questioning without benefit of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./465/1078/">465 U. S. 1078</a></span> (1984), and we now reverse.</p>
<p id="b356-7">I</p>
<p id="b356-8">In December 1981, the home of Mr. and Mrs. Gilbert Gross, in the town of Salem, Polk County, Ore., was burglarized. Missing were art objects and furnishings valued at $150,000. A witness to the burglary contacted the Polk County Sheriff’s Office, implicating respondent Michael El-stad, an 18-year-old neighbor and friend of the Grosses’ teenage son. Thereupon, Officers Burke and McAllister went to the home of respondent Elstad, with a warrant for his arrest. Elstad’s mother answered the door. She led the officers to her son’s room where he lay on his bed, clad in shorts and listening to his stereo. The officers asked him to get dressed and to accompany them into the living room. Officer McAllister asked respondent’s mother to step into the kitchen, where he explained that they had a warrant for her <page-number citation-index="1" label="301">*301</page-number>son’s arrest for the burglary of a neighbor’s residence. Officer Burke remained with Elstad in the living room. He later testified:</p>
<blockquote id="b357-4">“I sat down with Mr. Elstad and I asked him if he was aware of why Detective McAllister and myself were there to talk with him. He stated no, he had no idea why we were there. I then asked him if he knew a person by the name of Gross, and he said yes, he did, and also added that he heard that there was a robbery at the Gross house. And at that point I told Mr. Elstad that I felt he was involved in that, and he looked at me and stated, ‘Yes, I was there.’” App. 19-20.</blockquote>
<p id="b357-5">The officers then escorted Elstad to the back of the patrol car. As they were about to leave for the Polk County Sheriff’s office, Elstad’s father arrived home and came to the rear of the patrol car. The officers advised him that his son was a suspect in the burglary. Officer Burke testified that Mr. Elstad became quite agitated, opened the rear door of the car and admonished his son: “I told you that you were going to get into trouble. You wouldn’t listen to me. You never learn.” <em>Id., </em>at 21.</p>
<p id="b357-6">Elstad was transported to the Sheriff’s headquarters and approximately one hour later, Officers Burke and McAllister joined him in McAllister’s office. McAllister then advised respondent for the first time of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, reading from a standard card. Respondent indicated he understood his rights, and, having these rights in mind, wished to speak with the officers. Elstad gave a full statement, explaining that he had known that the Gross family was out of town and had been paid to lead several acquaintances to the Gross residence and show them how to gain entry through a defective sliding glass door. The statement was typed, reviewed by respondent, read back to him for correction, initialed and signed by Elstad and both officers. As an afterthought, Elstad added and initialed the sentence, “After leaving the house Robby &amp; I went back to [the] van &amp; Robby handed <page-number citation-index="1" label="302">*302</page-number>me a small bag of grass.” App. 42. Respondent concedes that the officers made no threats or promises either at his residence or at the Sheriff’s office.</p>
<p id="b358-5">Respondent was charged with first-degree burglary. He was represented at trial by retained counsel. Elstad waived his right to a jury, and his case was tried by a Circuit Court Judge. Respondent moved at once to suppress his oral statement and signed confession. He contended that the statement he made in response to questioning at his house “let the cat out of the bag,” citing <em>United States </em>v. <em>Bayer, </em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">331 U. S. 532</a></span> (1947), and tainted the subsequent confession as “fruit of the poisonous tree,” citing <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The judge ruled that the statement, “I was there,” had to be excluded because the defendant had not been advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The written confession taken after Elstad’s arrival at the Sheriff’s office, however, was admitted in evidence. The court found:</p>
<blockquote id="b358-6">“[H]is written statement was given freely, voluntarily and knowingly by the defendant after he had waived his right to remain silent and have counsel present which waiver was evidenced by the card which the defendant had signed. [It] was not tainted in any way by the previous brief statement between the defendant and the Sheriff’s Deputies that had arrested him.” App. 45.</blockquote>
<p id="b358-7">Elstad was found guilty of burglary in the first degree. He received a 5-year sentence and was ordered to pay $18,000 in restitution.</p>
<p id="b358-8">Following his conviction, respondent appealed to the Oregon Court of Appeals, relying on <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>and <em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">Bayer</a></span>. </em>The State conceded that Elstad had been in custody when he made his statement, “I was there,” and accordingly agreed that this statement was inadmissible as having been given without the prescribed <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. But the State maintained that any conceivable “taint” had been dissipated prior to the respondent’s written confession by McAllister’s careful administration of the requisite warnings. The Court <page-number citation-index="1" label="303">*303</page-number>of Appeals reversed respondent’s conviction, identifying the crucial constitutional inquiry as “whether there was a sufficient break in the stream of events between [the] inadmissible statement and the written confession to insulate the latter statement from the effect of what went before.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#676" aria-description="Citation for case: State v. Elstad">61 Ore. App. 673, 676</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P. 2d 552, 554</a></span> (1983). The Oregon court concluded:</p>
<blockquote id="b359-5">“Regardless of the absence of actual compulsion, the coercive impact of the unconstitutionally obtained statement remains, because in a defendant’s mind it has sealed his fate. It is this impact that must be dissipated in order to make a subsequent confession admissible. In determining whether it has been dissipated, lapse of time, and change of place from the original surroundings are the most important considerations.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#677" aria-description="Citation for case: State v. Elstad"><em>Id., </em>at 677</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 554</a></span>.</blockquote>
<p id="b359-6">Because of the brief period separating the two incidents, the “cat was sufficiently out of the bag to exert a coercive impact on [respondent’s] later admissions.” <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#678" aria-description="Citation for case: State v. Elstad"><em>Id., </em>at 678</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#555" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 555</a></span>.</p>
<p id="b359-7">The State of Oregon petitioned the Oregon Supreme Court for review, and review was declined. This Court granted certiorari to consider the question whether the Self-Incrimination Clause of the Fifth Amendment requires the suppression of a confession, made after proper <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and a valid waiver of rights, solely because the police had obtained an earlier voluntary but unwarned admission from the defendant.</p>
<p id="b359-8">II</p>
<p id="b359-9">The arguments advanced in favor of; suppression of respondent’s written confession rely heavily on metaphor. One metaphor, familiar from the Fourth Amendment context, would require that respondent’s confession, regardless of its integrity, voluntariness, and probative value, be suppressed as the “tainted fruit of the poisonous tree” of the Miranda, violation. A second metaphor questions whether a <page-number citation-index="1" label="304">*304</page-number>confession can be truly voluntary once the “cat is out of the bag.” Taken out of context, each of these metaphors can be misleading. They should not be used to obscure fundamental differences between the role of the Fourth Amendment exclusionary rule and the function of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>in guarding against the prosecutorial use of compelled statements as prohibited by the Fifth Amendment. The Oregon court assumed and respondent here contends that a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings necessarily breeds the same consequences as police infringement of a constitutional right, so that evidence uncovered following an unwarned statement must be suppressed as “fruit of the poisonous tree.” We believe this view misconstrues the nature of the protections afforded by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and therefore misreads the consequences of police failure to supply them.</p>
<p id="b360-5">A</p>
<p id="b360-6">Prior to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the admissibility of an accused’s in-custody statements was judged solely by whether they were “voluntary” within the meaning of the Due Process Clause. See, <em>e. g., Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span> (1963); <em>Chambers </em>v. <em>Florida, </em><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940). If a suspect’s statements had been obtained by “techniques and methods offensive to due process,” <em>Haynes </em>v. <em>Washington, </em><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S., at 515</a></span>, or under circumstances in which the suspect clearly had no opportunity to exercise “a free and unconstrained will,” <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#514" aria-description="Citation for case: Haynes v. Washington"><em>id., </em>at 514</a></span>, the statements would not be admitted. The Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>required suppression of many statements that would have been admissible under traditional due process analysis by presuming that statements made while in custody and without adequate warnings were protected by the Fifth Amendment. The Fifth Amendment, of course, is not concerned with nontestimonial evidence. See <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 764</a></span> (1966) (defendant may be compelled to supply blood samples). Nor is it concerned <page-number citation-index="1" label="305">*305</page-number>with moral and psychological pressures to confess emanating from sources other than official coercion. See, <em>e. g., California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span>, and n. 3 (1983) <em>(per curiam); Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#303" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 303</a></span>, and n. 10 (1980); <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495-496</a></span> (1977). Voluntary statements “remain a proper element in law enforcement.” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>. “Indeed, far from being prohibited by the Constitution, admissions of guilt by wrongdoers, if not coerced, are inherently desirable. . . . Absent some officially coerced self-accusation, the Fifth Amendment privilege is not violated by even the most damning admissions.” <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977). As the Court noted last Term in <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984) (footnote omitted):</p>
<blockquote id="b361-5">“The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court, however, presumed that interrogation in certain custodial circumstances is inherently coercive and . . . that statements made under those circumstances are inadmissible unless the suspect is specifically informed of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and freely decides to forgo those rights. The prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings therefore are ‘not themselves rights protected by the Constitution but [are] instead measures to insure that the right against compulsory self-incrimination [is] protected.’ <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974); see <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#492" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 492</a></span> (1981) (Powell, J., concurring). Requiring <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before custodial interrogation provides ‘practical reinforcement’ for the Fifth Amendment right.”</blockquote>
<p id="b361-6">Respondent’s contention that his confession was tainted by the earlier failure of the police to provide <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and must be excluded as “fruit of the poisonous tree” assumes the existence of a constitutional violation. This figure of speech is drawn from <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), in which the Court held that evidence and wit<page-number citation-index="1" label="306">*306</page-number>nesses discovered as a result of a search in violation of the Fourth Amendment must be excluded from evidence. The <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>doctrine applies as well when the fruit of the Fourth Amendment violation is a confession. It is settled law that “a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is ‘sufficiently an act of free will to purge the primary taint.’” <em>Taylor </em>v. <em>Alabama, </em><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687, 690</a></span> (1982) (quoting <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 602</a></span> (1975)).</p>
<p id="b362-5">But as we explained in <em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles</a></span> </em>and <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>, </em>a procedural <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation differs in significant respects from violations of the Fourth Amendment, which have traditionally mandated a broad application of the “fruits” doctrine. The purpose of the Fourth Amendment exclusionary rule is to deter unreasonable searches, no matter how probative their fruits. <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#216" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 216-217</a></span> (1979); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#600" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 600-602</a></span>. “The exclusionary rule, . . . when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth.” <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois"><em>Id., </em>at 601</a></span>. Where a Fourth Amendment violation “taints” the confession, a finding of voluntariness for the purposes of the Fifth Amendment is merely a threshold requirement in determining whether the confession may be admitted in evidence. <em>Taylor </em>v. <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama"><em>Alabama, supra, </em>at 690</a></span>. Beyond this, the prosecution must show a sufficient break in events to undermine the inference that the confession was caused by the Fourth Amendment violation.</p>
<p id="b362-6">The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>exclusionary rule, however, serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself. It may be triggered even in the absence of a Fif th Amendment violation.<footnotemark>1</footnotemark> The Fif th Amendment prohib<page-number citation-index="1" label="307">*307</page-number>its use by the prosecution in its case in chief only of <em>compelled </em>testimony. Failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings creates a presumption of compulsion. Consequently, unwarned statements that are otherwise voluntary within the meaning of the Fifth Amendment must nevertheless be excluded from evidence under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Thus, in the individual case, <em>Miranda’s </em>preventive medicine provides a remedy even to the defendant who has suffered no identifiable constitutional harm. See <em>New York </em>v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles"><em>Quarles, supra, </em>at 654</a></span>; <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974).</p>
<p id="b363-4">But the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>presumption, though irrebuttable for purposes of the prosecution’s case in chief, does not require that the statements and their fruits be discarded as inherently tainted. Despite the fact that patently <em>voluntary </em>statements taken in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>must be excluded from the prosecution’s case, the presumption of coercion does not bar their use for impeachment purposes on cross-examination. <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971). The Court in <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>rejected as an “extravagant extension of the Constitution,” the theory that a defendant who had confessed under circumstances that made the confession inadmissible, could thereby enjoy the freedom to “deny every fact disclosed or discovered as a ‘fruit’ of his confession, free from confrontation with his prior statements” and that the voluntariness of his confession would be totally irrelevant. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><em>Id., </em>at 225</a></span>, and n. 2. Where an unwarned statement is preserved for use in situations that fall outside the sweep of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>presumption, “the primary criterion of admissibility <page-number citation-index="1" label="308">*308</page-number>[remains] the ‘old’ due process voluntariness test.” Schul-hofer, Confessions and the Court, <span class="citation no-link">79 Mich. L. Rev. 865</span>, 877 (1981).</p>
<p id="b364-5">In <em>Michigan </em>v. <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span> </em>the Court was asked to extend the <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>fruits doctrine to suppress the testimony of a witness for the prosecution whose identity was discovered as the result of a statement taken from the accused without benefit of full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. As in respondent’s case, the breach of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures in <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span> </em>involved no actual compulsion. The Court concluded that the unwarned questioning “did not abridge respondent’s constitutional privilege . . . but departed only from the prophylactic standards later laid down by this Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to safeguard that privilege.” <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 446</a></span>. Since there was no actual infringement of the suspect’s constitutional rights, the case was not controlled by the doctrine expressed in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>that fruits of a constitutional violation must be suppressed. In deciding “how sweeping the judicially imposed consequences” of a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings should be, <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 445</a></span>, the <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span> </em>Court noted that neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression of the witness’ testimony. The unwarned confession must, of course, be suppressed, but the Court ruled that introduction of the third-party witness’ testimony did not violate Tucker’s Fifth Amendment rights.</p>
<p id="b364-6">We believe that this reasoning applies with equal force when the alleged “fruit” of a noncoercive <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation is neither a witness nor an article of evidence but the accused’s own voluntary testimony. As in <em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>, </em>the absence of any coercion or improper tactics undercuts the twin rationales— trustworthiness and deterrence — for a broader rule. Once warned, the suspect is free to exercise his own volition in deciding whether or not to make a statement to the authorities. The Court has often noted: “‘[A] living witness is not to be <page-number citation-index="1" label="309">*309</page-number>mechanically equated with the proffer of inanimate eviden-tiary objects illegally seized. . . . [T]he living "witness is an individual human personality whose attributes of will, perception, memory and <em>volition </em>interact to determine what testimony he wall give.”’ <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#277" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 277</a></span> (1978) (emphasis added) (quoting from <em>Smith </em>v. <em>United States, </em>117 U. S. App. D. C. 1, 3-4, <span class="citation" data-id="9449714"><a href="/opinion/262430/wilson-m-smith-jr-v-united-states-of-america-raymond-bowden-v-united/#881" aria-description="Citation for case: Wilson M. Smith, Jr. v. United States of America, Raymond...">324 F. 2d 879, 881-882</a></span> (1963) (Burger, J.) (footnotes omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./377/954/">377 U. S. 954</a></span> (1964)).</p>
<p id="b365-5">Because <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings may inhibit persons from giving information, this Court has determined that they need be administered only after the person is taken into “custody” or his freedom has otherwise been significantly restrained. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>. Unfortunately, the task of defining “custody” is a slippery one, and “policemen investigating serious crimes [cannot realistically be expected to] make no errors whatsoever.” <em>Michigan </em>v. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker"><em>Tucker, supra, </em>at 446</a></span>. If errors are made by law enforcement officers in administering the prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures, they should not breed the same irremediable consequences as police infringement of the Fifth Amendment itself. It is an unwarranted extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to hold that a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect’s ability to exercise his free will, so taints the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period. Though <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made.</p>
<p id="b365-6">B</p>
<p id="b365-7">The Oregon court, however, believed that the unwarned remark compromised the voluntariness of respondent’s later confession. It was the court’s view that the prior <em>answer </em><page-number citation-index="1" label="310">*310</page-number>and not the unwarned questioning impaired respondent’s ability to give a valid waiver and that only lapse of time and change of place could dissipate what it termed the “coercive impact” of the inadmissible statement. When a prior statement is actually coerced, the time that passes between confessions, the change in place of interrogations, and the change in identity of the interrogators all bear on whether that coercion has carried over into the second confession. See <em>Westover </em>v. <em>United States, </em>decided together with <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 494</a></span>; <em>Clewis </em>v. <em>Texas, </em><span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967). The failure of police to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings does not mean that the statements received have actually been coerced, but only that courts will presume the privilege against compulsory self-incrimination has not been intelligently exercised. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S., at 654</a></span>, and n. 5; <em>Miranda </em>v. <em>Arizona, supra, </em>at 457. Of the courts that have considered whether a properly warned confession must be suppressed because it was preceded by an unwarned but clearly voluntary admission, the majority have explicitly or implicitly recognized that <em>Westover's </em>requirement of a break in the stream of events is inapposite.<footnotemark>2</footnotemark> In these circumstances, a careful and thorough <page-number citation-index="1" label="311">*311</page-number>administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings serves to cure the condition that rendered the unwarned statement inadmissible. The warning conveys the relevant information and thereafter the suspect’s choice whether to exercise his privilege to remain silent should ordinarily be viewed as an “act of free will.” <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>.</p>
<p id="b367-4">The Oregon court nevertheless identified a subtle form of lingering compulsion, the psychological impact of the suspect’s conviction that he has let the cat out of the bag and, in so doing, has sealed his own fate. But endowing the psychological effects of <em>voluntary </em>unwarned admissions with constitutional implications would, practically speaking, disable the police from obtaining the suspect’s informed cooperation even when the official coercion proscribed by the Fifth Amendment played no part in either his warned or unwarned confessions. As the Court remarked in <em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/" aria-description="Citation for case: United States v. Bayer">Bayer</a></span>:</em></p>
<blockquote id="b367-5">“[AJfter an accused has once let the cat out of the bag by confessing, no matter what the inducement, he is never thereafter free of the psychological and practical disadvantages of having confessed. He can never get the cat back in the bag. The secret is out for good. In such a sense, a later confession may always be looked upon as fruit of the first. But this Court has never gone so far as to hold that making a confession under circumstances which preclude its use, perpetually disables the confessor from making a usable one after those conditions have been removed.” <span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/#540" aria-description="Citation for case: United States v. Bayer">331 U. S., at 540-541</a></span>.</blockquote>
<p id="b367-6">Even in such extreme cases as <em>Lyons </em>v. <em>Oklahoma, </em><span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596</a></span> (1944), in which police forced a full confession from the accused through unconscionable methods of interrogation, the Court has assumed that the coercive effect of the confes<page-number citation-index="1" label="312">*312</page-number>sion could, with time, be dissipated. See also <em>Westover </em>v. <em>United States, supra, </em>at 496.</p>
<p id="b368-5">This Court has never held that the psychological impact of voluntary disclosure of a guilty secret qualifies as state compulsion or compromises the voluntariness of a subsequent informed waiver. The Oregon court, by adopting this expansive view of Fifth Amendment compulsion, effectively immunizes a suspect who responds to <em>pre-Miranda </em>warning questions from the consequences of his subsequent informed waiver of the privilege of remaining silent. See <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#679" aria-description="Citation for case: State v. Elstad">61 Ore. App., at 679</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#555" aria-description="Citation for case: State v. Elstad">658 P. 2d, at 555</a></span> (Gillette, P. J., concurring). This immunity comes at a high cost to legitimate law enforcement activity, while adding little desirable protection to. the individual’s interest in not being <em>compelled </em>to testify against himself. Cf. <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#107" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 107-111</a></span> (1975) (White, J., concurring in result). When neither the initial nor the subsequent admission is coerced, little, justification exists for permitting the highly probative evidence of a voluntary confession to be irretrievably lost to the factfinder.</p>
<p id="b368-6">There is a vast difference between the direct consequences flowing from coercion of a confession by physical violence or other deliberate means calculated to break the suspect’s will and the uncertain consequences of disclosure of a “guilty secret” freely given in response to an unwarned but non-coercive question, as in this case. Justice Brennan’s contention that it is impossible to perceive any causal distinction between this case and one involving a confession that is coerced by torture is wholly unpersuasive.<footnotemark>3</footnotemark> Certainly, in <page-number citation-index="1" label="313">*313</page-number>respondent’s case, the causal connection between any psychological disadvantage created by his admission and his ultimate decision to cooperate is speculative and attenuated at</p>
<p id="b370-3"><page-number citation-index="1" label="314">*314</page-number>Though belated, the reading of respondent’s rights was undeniably complete. McAllister testified that he read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings aloud from a printed card and recorded best. It is difficult to tell with certainty what motivates a suspect to speak. A suspect’s confession may be traced to factors as disparate as “a prearrest event such as a visit with a minister,” <em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#220" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 220</a></span> (Stevens, J., concurring), or an intervening event such as the exchange of words respondent had with his father. We must conclude that, absent deliberately coercive or improper tactics in obtaining the initial statement, the mere fact that a suspect has made an unwarned admission does not warrant a presumption of compulsion. A subsequent administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to a suspect who has given a voluntary but unwarned statement ordinarily should suffice to remove the conditions that precluded admission of the earlier statement. In such circumstances, the finder of fact may reasonably conclude that the suspect made a rational and intelligent choice whether to waive or invoke his rights.</p>
<p id="b370-7">I — I <page-number citation-index="1" label="315">*315</page-number>Elstad’s responses.<footnotemark>4</footnotemark> There is no question that respondent knowingly and voluntarily waived his right to remain silent before he described his participation in the burglary. It is also beyond dispute that respondent’s earlier remark was voluntary, within the meaning of the Fifth Amendment. Neither the environment nor the manner of either “interrogation” was coercive. The initial conversation took place at midday, in the living room area of respondent’s own home, with his mother in the kitchen area, a few steps away. Although in retrospect the officers testified that respondent was then in custody, at the time he made his statement he had not been informed that he was under arrest. The arresting officers’ testimony indicates that the brief stop in the living room before proceeding to the station house was not to interrogate the suspect but to notify his mother of the reason for his arrest. App. 9-10.</p>
<p id="b371-5">The State has conceded the issue of custody and thus we must assume that Burke breached <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures in failing to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings before initiating the discussion in the living room. This breach may have been the result of confusion as to whether the brief exchange qualified as “custodial interrogation” or it may simply have reflected Burke’s reluctance to initiate an alarming police <page-number citation-index="1" label="316">*316</page-number>procedure before McAllister had spoken with respondent’s mother. Whatever the reason for Burke’s oversight, the incident had none of the earmarks of coercion. See <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#109" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 109-110</a></span> (1980). Nor did the officers exploit the unwarned admission to pressure respondent into waiving his right to remain silent.</p>
<p id="b372-5">Respondent, however, has argued that he was unable to give a fully <em>informed </em>waiver of his rights because he was unaware that his prior statement could not be used against him. Respondent suggests that Officer McAllister, to cure this deficiency, should have added an additional warning to those given him at the Sheriff’s office. Such a requirement is neither practicable nor constitutionally necessary. In many cases, a breach of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>procedures may not be identified as such until long after full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are administered and a valid confession obtained. See, <em>e. g., United States </em>v. <em>Bowler, </em><span class="citation" data-id="348792"><a href="/opinion/348792/united-states-v-patrick-earl-bowler/#1324" aria-description="Citation for case: United States v. Patrick Earl Bowler">561 F. 2d 1323, 1324-1325</a></span> (CA9 1977) (certain statements ruled inadmissible by trial court); <em>United States </em>v. <em>Toral, </em><span class="citation" data-id="336178"><a href="/opinion/336178/united-states-v-marco-antonio-toral/#896" aria-description="Citation for case: United States v. Marco Antonio Toral">536 F. 2d 893, 896</a></span> (CA9 1976); <em>United States </em>v. <em>Knight, </em><span class="citation" data-id="9453695"><a href="/opinion/280455/united-states-v-richard-s-knight/#974" aria-description="Citation for case: United States v. Richard S. Knight">395 F. 2d 971, 974-975</a></span> (CA2 1968) (custody unclear). The standard <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings explicitly inform the suspect of his right to consult a lawyer before speaking. Police officers are ill-equipped to pinch-hit for counsel, construing the murky and difficult questions of when “custody” begins or whether a given unwarned statement will ultimately be held admissible. See <em>Tanner </em>v. <em>Vincent, </em><span class="citation" data-id="339054"><a href="/opinion/339054/carlson-tanner-jr-v-leon-vincent-warden-of-green-haven-prison/#936" aria-description="Citation for case: Carlson Tanner, Jr. v. Leon Vincent, Warden of Green...">541 F. 2d 932, 936</a></span> (CA2 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/1065/">429 U. S. 1065</a></span> (1977).</p>
<p id="b372-6">This Court has never embraced the theory that a defendant’s ignorance of the full consequences of his decisions vitiates their voluntariness. See <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S., at 1125-1126, n. 3</a></span>; <em>McMann </em>v. <em>Richardson, </em><span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 769</a></span> (1970). If the prosecution has actually violated the defendant’s Fifth Amendment rights by introducing an inadmissible confession at trial, compelling the defendant to testify in rebuttal, the rule announced in <em>Harrison </em>v. <em>United States, </em><span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/" aria-description="Citation for case: Harrison v. United States">392 U. S. 219</a></span> (1968), precludes use of that testimony <page-number citation-index="1" label="317">*317</page-number>on retrial. “Having ‘released the spring’ by using the petitioner’s unlawfully obtained confessions against him, the Government must show that its illegal action did not induce his testimony.” <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/#224" aria-description="Citation for case: Harrison v. United States">Id., at 224-225</a></span>. But the Court has refused to find that a defendant who confesses, after being falsely told that his codefendant has turned State’s evidence, does so involuntarily. <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969). The Court has also rejected the argument that a defendant’s ignorance that a prior coerced confession could not be admitted in evidence compromised the voluntariness of his guilty plea. <em>McMann </em>v. <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson"><em>Richardson, supra, </em>at 769</a></span>. Likewise, in <em>California </em>v. <em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">Beheler, supra,</a></span> </em>the Court declined to accept defendant’s contention that, because he was unaware of the potential adverse consequences of statements he made to the police, his participation in the interview was involuntary. Thus we have not held that the <em>sine qua non </em>for a knowing and voluntary waiver of the right to remain silent is a full and complete appreciation of all of the consequences flowing from the nature and the quality of the evidence in the case.</p>
<p id="At24">J — I &lt;1</p>
<p id="Aiu">When police ask questions of a suspect in custody without administering the required warnings, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>dictates that the answers received be presumed compelled and that they be excluded from evidence at trial in the State’s case in chief. The Court has carefully adhered to this principle, permitting a narrow exception only where pressing public safety concerns demanded. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#655" aria-description="Citation for case: New York v. Quarles">467 U. S., at 655-656</a></span>. The Court today in no way retreats from the bright-line rule of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>We do not imply that good faith excuses, a failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings; nor do we condone inherently coercive police tactics or methods offensive to due process that render the initial admission involuntary and undermine the suspect’s will to invoke his rights once they are read to him. A handful of courts have, however, applied our precedents relating to confessions ob<page-number citation-index="1" label="318">*318</page-number>tained under coercive circumstances to situations involving wholly voluntary admissions, requiring a passage of time or break in events before a second, fully warned statement can be deemed voluntary. Far from establishing a rigid rule, we direct courts to avoid one; there is no warrant for presuming coercive effect where the suspect’s initial inculpatory statement, though technically in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>was voluntary.<footnotemark>5</footnotemark> The relevant inquiry is whether, in fact, the second statement was also voluntarily made. As in any such inquiry, the finder of fact must examine the surrounding circumstances and the entire course of police conduct with respect to the suspect in evaluating the voluntariness of his statements. The fact that a suspect chooses to speak after being informed of his rights is, of course, highly probative. We find that the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and the goals of the Fifth Amendment proscription against use of compelled testimony are fully satisfied in the circumstances of this case by barring use of the unwarned statement in the case in chief. No further purpose is served by imputing “taint” to subsequent statements obtained pursuant to a voluntary and knowing waiver. We hold today that a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
<p id="b374-5">The judgment of the Court of Appeals of Oregon is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b374-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b362-7"> Justice Stevens expresses puzzlement at our statement that a simple failure to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is not in itself a violation of the Fifth Amendment. Yet the Court so held in <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 <page-number citation-index="1" label="307">*307</page-number>U. S. 649, 654</a></span> (1983), and <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974). The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court itself recognized this point when it disclaimed any intent to create a “constitutional straitjacket” and invited Congress and the States to suggest “potential alternatives for protecting the privilege.” 384 U. S., at 467. A <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>violation does not <em>constitute </em>coercion but rather affords a bright-line, legal presumption of coercion, requiring suppression of all unwarned statements. It has never been remotely suggested that any statement taken from Mr. Elstad without benefit of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would be admissible.</p>
</footnote>
<footnote label="2">
<p id="b366-5"> See, <em>e. g., United States </em>v. <em>Bowler, </em><span class="citation" data-id="348792"><a href="/opinion/348792/united-states-v-patrick-earl-bowler/#1326" aria-description="Citation for case: United States v. Patrick Earl Bowler">561 F. 2d 1323, 1326</a></span> (CA9 1977); <em>Tanner </em>v. <em>Vincent, </em><span class="citation" data-id="339054"><a href="/opinion/339054/carlson-tanner-jr-v-leon-vincent-warden-of-green-haven-prison/" aria-description="Citation for case: Carlson Tanner, Jr. v. Leon Vincent, Warden of Green...">541 F. 2d 932</a></span> (CA2 1976); <em>United States </em>v. <em>Toral, </em><span class="citation" data-id="336178"><a href="/opinion/336178/united-states-v-marco-antonio-toral/#896" aria-description="Citation for case: United States v. Marco Antonio Toral">536 F. 2d 893, 896-897</a></span> (CA9 1976); <em>United States </em>v. <em>Knight, </em><span class="citation" data-id="9453695"><a href="/opinion/280455/united-states-v-richard-s-knight/#975" aria-description="Citation for case: United States v. Richard S. Knight">395 F. 2d 971, 975</a></span> (CA21968); <em>State </em>v. <em>Montes, </em><span class="citation" data-id="1145231"><a href="/opinion/1145231/state-v-montes/#496" aria-description="Citation for case: State v. Montes">136 Ariz. 491,496-497</a></span>, <span class="citation" data-id="1145231"><a href="/opinion/1145231/state-v-montes/#196" aria-description="Citation for case: State v. Montes">667 P. 2d 191,196-197</a></span> (1983); <em>State </em>v. <em>Derrico, </em><span class="citation" data-id="1502926"><a href="/opinion/1502926/state-v-derrico/#166" aria-description="Citation for case: State v. Derrico">181 Conn. 151, 166-167</a></span>, <span class="citation" data-id="1502926"><a href="/opinion/1502926/state-v-derrico/#365" aria-description="Citation for case: State v. Derrico">434 A. 2d 356, 365-366</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1064/">449 U. S. 1064</a></span> (1980); <em>State </em>v. <em>Holt, </em><span class="citation" data-id="1690277"><a href="/opinion/1690277/state-v-holt/#890" aria-description="Citation for case: State v. Holt">354 So. 2d 888, 890</a></span> (Fla. App.), cert. denied, <span class="citation no-link">361 So. 2d 832</span> (Fla. 1978); <em>Fried </em>v. <em>State, </em><span class="citation" data-id="1496973"><a href="/opinion/1496973/fried-v-state/#644" aria-description="Citation for case: Fried v. State">42 Md. App. 643, 644-648</a></span>, <span class="citation" data-id="1496973"><a href="/opinion/1496973/fried-v-state/#102" aria-description="Citation for case: Fried v. State">402 A. 2d 101, 102-104</a></span> (1979); <em>Commonwealth </em>v. <em>White, </em><span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">353 Mass. 409</a></span>, <span class="citation" data-id="2225068"><a href="/opinion/2225068/commonwealth-v-white/" aria-description="Citation for case: Commonwealth v. White">232 N. E. 2d 335</a></span> (1967); <em>State </em>v. <em>Sickels, </em><span class="citation" data-id="1725960"><a href="/opinion/1725960/state-v-sickels/#813" aria-description="Citation for case: State v. Sickels">275 N. W. 2d 809, 813-814</a></span> (Minn. 1979); <em>State </em>v. <em>Dakota, </em><span class="citation" data-id="1837744"><a href="/opinion/1837744/state-v-dakota/" aria-description="Citation for case: State v. Dakota">300 Minn. 12</a></span>, <span class="citation" data-id="1837744"><a href="/opinion/1837744/state-v-dakota/" aria-description="Citation for case: State v. Dakota">217 N. W. 2d 748</a></span> (1974); <em>State </em>v. <em>Raymond, </em><span class="citation" data-id="2012195"><a href="/opinion/2012195/state-v-raymond/#170" aria-description="Citation for case: State v. Raymond">305 Minn. 160,170</a></span>, <span class="citation" data-id="2012195"><a href="/opinion/2012195/state-v-raymond/#886" aria-description="Citation for case: State v. Raymond">232 N. W. 2d 879, 886</a></span> (1975) (noting common thread in line of cases holding prejudicial coercion not present “just because [defendant] had made an earlier confession which ‘let the cat out of the bag’ ”); <em>Commonwealth </em>v. <em>Chacko, </em><span class="citation" data-id="1472767"><a href="/opinion/1472767/commonwealth-v-chacko/#580" aria-description="Citation for case: Commonwealth v. Chacko">500 Pa. 571, 580-582</a></span>, <span class="citation" data-id="1472767"><a href="/opinion/1472767/commonwealth-v-chacko/#316" aria-description="Citation for case: Commonwealth v. Chacko">459 A. 2d 311, 316</a></span> (1983) (“After being given his <em>Miranda </em>warnings it is clear [defendant] maintained his intention to provide his questioners with <page-number citation-index="1" label="311">*311</page-number>his version of the incident”). But see <em>In re Pablo A. C., </em><span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">129 Cal. App. 3d 984</a></span>,<span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">181 Cal. Rptr. 468</a></span> (1982); <em>State </em>v. <em>Hibdon, </em><span class="citation" data-id="1231742"><a href="/opinion/1231742/state-v-hibdon/" aria-description="Citation for case: State v. Hibdon">57 Ore. App. 509</a></span>, <span class="citation" data-id="1231742"><a href="/opinion/1231742/state-v-hibdon/" aria-description="Citation for case: State v. Hibdon">645 P. 2d 580</a></span> (1982); <em>State </em>v. <em>Lavaris, </em><span class="citation" data-id="1234251"><a href="/opinion/1234251/state-v-lavaris/#857" aria-description="Citation for case: State v. Lavaris">99 Wash. 2d 851, 857-860</a></span>, <span class="citation" data-id="1234251"><a href="/opinion/1234251/state-v-lavaris/#1237" aria-description="Citation for case: State v. Lavaris">664 P. 2d 1234, 1237-1239</a></span> (1983).</p>
</footnote>
<footnote label="3">
<p id="b368-7"> Most of the 50 cases cited by Justice Brennan in his discussion of consecutive confessions concern an initial unwarned statement obtained through overtly or inherently coercive methods which raise serious Fifth Amendment and due process concerns. Without describing each case cited, the following are representative of the situations Justice Brennan views as analogous to this case: <em>e. g., Darwin </em>v. <em>Connecticut, </em><span class="citation" data-id="9423713"><a href="/opinion/107694/darwin-v-connecticut/" aria-description="Citation for case: Darwin v. Connecticut">391 U. S. 346</a></span> (1968) (suspect interrogated for 48 hours incommunicado while officers denied access to counsel); <em>Beecher </em>v. <em>Alabama, </em><span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#36" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 36</a></span> (1967) (officer fired rifle next to suspect’s ear and said “If you don’t tell the truth I am <page-number citation-index="1" label="313">*313</page-number>going to kill you”); <em>Clewis </em>v. <em>Texas, </em><span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967) (suspect was arrested without probable cause, interrogated for nine days with little food or sleep, and gave three unwarned “confessions” each of which he immediately retracted); <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#439" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 439-440, n. 3</a></span> (1961) (mentally retarded youth interrogated incommunicado for a week “during which time he was frequently ill, fainted several times, vomited blood on the floor of the police station and was twice taken to the hospital on a stretcher”). Typical of the state cases cited in the dissent’s discussion are: <em>e. g., Cagle </em>v. <em>State, </em><span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#4" aria-description="Citation for case: Cagle v. State">45 Ala. App. 3, 4</a></span>, <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#120" aria-description="Citation for case: Cagle v. State">221 So. 2d 119, 120</a></span> (1969) (police interrogated wounded suspect at police station for one hour before obtaining statement, took him to hospital to have his severe wounds treated, only then giving the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings; suspect prefaced second statement with “I have already give the Chief a statement and I might as well give one to you, too”), cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./284/727/">284 Ala. 727</a></span>, <span class="citation multiple-matches"><a href="/c/So.%202d/221/121/">221 So. 2d 121</a></span> (1969); <em>People </em>v. <em>Saiz, </em><span class="citation" data-id="9558965"><a href="/opinion/1196896/people-v-saiz/" aria-description="Citation for case: People v. Saiz">620 P. 2d 15</a></span> (Colo. 1980) (two hours’ unwarned custodial interrogation of 16-year-old in violation of state law requiring parent’s presence, culminating in visit to scene of crime); <em>People </em>v. <em>Bodner, </em>75 App. Div. 2d 440, 430 N. Y. S. 2d 433 (1980) (confrontation at police station and at scene of crime between police and retarded youth with mental age of eight or nine); <em>State </em>v. <em>Badger, </em><span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#441" aria-description="Citation for case: State v. Badger">141 Vt. 430, 441</a></span>, <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/" aria-description="Citation for case: State v. Badger">450 A. 2d 336</a></span>, 343 .(1982) (unwarned “close and intense” station house questioning of 15-year-old, including threats and promises, resulted in confession at 1:20 a. m.; court held “[w]arnings . . . were insufficient to cure such blatant abuse or compensate for the coercion in this case”).</p>
<p id="b369-6">Justice Brennan cannot seriously mean to equate such situations with the case at bar. Likewise inapposite are the cases the dissent cites concerning suspects whose invocation of their rights to remain silent and to have counsel present were flatly ignored while police subjected them to continued interrogation. See, <em>e. g., United States ex rel. Sanders </em>v. <em>Rowe, </em><span class="citation" data-id="2093616"><a href="/opinion/2093616/united-states-ex-rel-sanders-v-rowe/" aria-description="Citation for case: United States Ex Rel. Sanders v. Rowe">460 F. Supp. 1128</a></span> (ND Ill. 1978); <em>People </em>v. <em>Braeseke, </em><span class="citation" data-id="9578828"><a href="/opinion/1320417/people-v-braeseke/" aria-description="Citation for case: People v. Braeseke">25 Cal. 3d 691</a></span>, <span class="citation" data-id="9578828"><a href="/opinion/1320417/people-v-braeseke/" aria-description="Citation for case: People v. Braeseke">602 P. 2d 384</a></span> (1979), vacated on other grounds, <span class="citation multiple-matches"><a href="/c/U.%20S./446/932/">446 U. S. 932</a></span> (1980); <em>Smith </em>v. <em>State, </em><span class="citation" data-id="1306478"><a href="/opinion/1306478/smith-v-state/" aria-description="Citation for case: Smith v. State">132 Ga. App. 491</a></span>, <span class="citation" data-id="1306478"><a href="/opinion/1306478/smith-v-state/" aria-description="Citation for case: Smith v. State">208 S. E. 2d 351</a></span> (1974). Finally, many of the decisions Justice Brennan claims require that the “taint” be “dissipated” simply recite the stock “cat” and “tree” metaphors but go on to find the second confession voluntary without identifying any break in the stream of events beyond the simple administration of a careful and thorough warning. See cases cited in n. 2, <em>supra.</em></p>
<p id="b369-7">Out of the multitude of decisions Justice Brennan cites, no more than half a dozen fairly can be said to suppress confessions on facts remotely <page-number citation-index="1" label="314">*314</page-number>comparable to those in the instant case, and some of these decisions involved other elements not present here. See <em>United States </em>v. <em>Pierce, </em><span class="citation" data-id="9453756"><a href="/opinion/280782/united-states-v-thomas-michael-pierce/" aria-description="Citation for case: United States v. Thomas Michael Pierce">397 F. 2d 128</a></span> (CA4 1968) (thorough custodial interrogation at station house); <em>United States </em>v. <em>Pellegrini, </em><span class="citation" data-id="2096024"><a href="/opinion/2096024/united-states-v-pellegrini/#257" aria-description="Citation for case: United States v. Pellegrini">309 F. Supp. 250, 257</a></span> (SDNY 1970) (officers induced unwarned suspect to produce “the clinching evidence of his crime”); <em>In re Pablo A. C., </em><span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">129 Cal. App. 3d 984</a></span>, <span class="citation" data-id="9721638"><a href="/opinion/2122160/people-v-pablo-c/" aria-description="Citation for case: People v. Pablo C.">181 Cal. Rptr. 468</a></span> (1982) (25-minute interrogation of juvenile; court finds causal connection but notes that all prior cited eases relying on “cat-out-of-bag” theory have involved coercion); <em>State </em>v. <em>Lekas, </em><span class="citation" data-id="9542762"><a href="/opinion/1161498/state-v-lekas/" aria-description="Citation for case: State v. Lekas">201 Kan. 579</a></span>, <span class="citation" data-id="9542762"><a href="/opinion/1161498/state-v-lekas/" aria-description="Citation for case: State v. Lekas">442 P. 2d 11</a></span> (1968) (parolee taken into custody and questioned at courthouse). At least one State Supreme Court cited by Justice Brennan that read <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>as mandating suppression of a subsequent voluntary and fully warned confession did so with express reluctance, convinced that admissibility of a subsequent confession should turn on voluntariness alone. See <em>Brunson </em>v. <em>State, </em><span class="citation" data-id="1724789"><a href="/opinion/1724789/brunson-v-state/#819" aria-description="Citation for case: Brunson v. State">264 So. 2d 817, 819-820</a></span> (Miss. 1972).</p>
</footnote>
<footnote label="4">
<p id="b371-6"> The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>advice on the card was clear and comprehensive, incorporating the warning that any statements could be used in a court of law; the rights to remain silent, consult an attorney at state expense, and interrupt the conversation at any time; and the reminder that any statements must be voluntary. The reverse side of the card carried three questions in boldface and recorded Elstad’s responses:</p>
<blockquote id="b371-7">“DO YOU UNDERSTAND THESE RIGHTS? ‘Yeh’</blockquote>
<blockquote id="b371-8">“DO YOU HAVE ANY QUESTIONS ABOUT YOUR RIGHTS? ‘No’ “HAVING THESE RIGHTS IN MIND, DO YOU WISH TO TALK TO US NOW? ‘Yeh I do!”’</blockquote>
<p id="b371-9">The card is dated and signed by respondent and by Officer McAllister. A recent high school graduate, Elstad was fully capable of understanding this careful administering of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings.</p>
</footnote>
<footnote label="5">
<p id="b374-9"> Justice Brennan, with an apocalyptic tone, heralds this opinion as dealing a “crippling blow to <em>Miranda.’’ Post, </em>at 319. Justice Brennan not only distorts the reasoning and holding of our decision, but, worse, invites trial courts and prosecutors to do the same.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Oregon v. Mathiason.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Oregon v. Mathiason"
type: case
citation: "429 U.S. 492 (1977)"
parallel_cite: "97 S. Ct. 711; 50 L. Ed. 2d 714"
neutral_cite: 1977 U.S. LEXIS 38
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-01-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-01-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Oregon v. Mathiason
  varies_by_point: false
  scope_note: "Per curiam; voluntary station-house interview is not custody; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109587/oregon-v-mathiason/"
  cluster_id: 109587
  opinion_id: 109587
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[Stansbury v. California]]", "[[Howes v. Fields]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "station-house"]
holding: "A suspect who comes voluntarily to the station, is told he is not under arrest, and is free to leave is NOT in custody for Miranda —…"
lake:
  record_id: Oregon v. Mathiason
  status: verified
  projected_at: 2026-07-06
---

# Oregon v. Mathiason

*429 U.S. 492 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A parolee, Mathiason, came voluntarily to a state police office after an officer left a note asking him to call. The officer told him he was not under arrest, falsely said that his fingerprints had been found at a burglary scene, and questioned him behind a closed door. Mathiason confessed and then left the office freely. ([[Common Legal Terms#per-curiam|Per curiam]].)

## Issue
Whether a suspect questioned at a police station — who came voluntarily, was told he was not under arrest, and was free to leave — is "in custody" for *[[Miranda v. Arizona|Miranda]]* purposes.

## Rule
*[[Miranda v. Arizona|Miranda]]* applies only to custodial interrogation; a station-house setting or a "coercive environment" does not by itself trigger it. "[P]olice officers are not required to administer *Miranda* warnings to everyone whom they question. Nor is the requirement of warnings to be imposed simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect." — 429 U.S. at 495. ^pin-495

"*Miranda* warnings are required only where there has been such a restriction on a person's freedom as to render him 'in custody.'" — *Id.* ^pin-495b

## Application
Mathiason came to the station voluntarily, was told he was not under arrest, was questioned briefly, and left without hindrance; he was therefore not in custody. The officer's false statement that fingerprints had been found did not convert the noncustodial interview into custodial interrogation. Because Mathiason was not in custody, no *[[Miranda v. Arizona|Miranda]]* warnings were required and his confession was admissible.

## Conclusion
Mathiason was not in custody; *[[Miranda v. Arizona|Miranda]]* did not apply and the confession was admissible. The Oregon Supreme Court's judgment was reversed. *([[Common Legal Terms#per-curiam|Per curiam]].)*

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mathiason* applies [[Miranda v. Arizona]]'s custody threshold and was reaffirmed in [[California v. Beheler]]; the custody inquiry is objective ([[Stansbury v. California]]) and turns on a formal-arrest-or-equivalent restraint on freedom of movement ([[Howes v. Fields]]).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Oregon v. Mathiason*, 429 U.S. 492 (1977) (per curiam) — https://www.courtlistener.com/opinion/109587/oregon-v-mathiason/ — pinpoint: 495.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "128abd4be8d04903", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Oregon v. Mathiason"}, "payload": {"all": [{"cite": "429 U.S. 492", "page": "492", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "429"}, {"cite": "97 S. Ct. 711", "page": "711", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "50 L. Ed. 2d 714", "page": "714", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "50"}, {"cite": "1977 U.S. LEXIS 38", "page": "38", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "429 U.S. 492", "official": {"cite": "429 U.S. 492", "page": "492", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "429"}, "official_selection_present": true, "record_id": "Oregon v. Mathiason"}}
{"assertion_id": "32cf087d77740b31", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-495b", "record_id": "Oregon v. Mathiason"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-495b", "pinpoint_status": "slip-only", "quote": "*Miranda* warnings are required only where there has been such a restriction on a person's freedom as to render him 'in custody.'", "quote_fidelity": "mismatch", "record_id": "Oregon v. Mathiason", "star_marker": null}}
{"assertion_id": "551af3ec40f1fe99", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-495", "record_id": "Oregon v. Mathiason"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-495", "pinpoint_status": "slip-only", "quote": "for *Miranda* purposes. ## Rule *Miranda* applies only to custodial interrogation; a station-house setting or a", "quote_fidelity": "mismatch", "record_id": "Oregon v. Mathiason", "star_marker": null}}
{"assertion_id": "8cb5a19bea015014", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Oregon v. Mathiason"}, "payload": {"as_of_content": "1977-01-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Oregon v. Mathiason", "scope_note": "Per curiam; voluntary station-house interview is not custody; good law.", "varies_by_point": false}}
```

### lake record — Oregon v. Mathiason

```json
{
  "schema_version": "s2.v1",
  "record_id": "Oregon v. Mathiason",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Oregon v. Mathiason",
    "case_name_short": "Mathiason",
    "case_name_full": "Oregon v. Mathiason",
    "input_case_name": "Oregon v. Mathiason",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-01-25",
    "year": 1977,
    "docket": null,
    "cluster_id": 109587,
    "lead_opinion_id": 109587,
    "sibling_ids": [
      109587,
      9426651,
      9426652,
      9426653
    ],
    "absolute_url": "/opinion/109587/oregon-v-mathiason/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 492",
      "volume": "429",
      "reporter": "U.S.",
      "page": "492",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 711",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "711",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 714",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 38",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 492",
        "volume": "429",
        "reporter": "U.S.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 711",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "711",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "50 L. Ed. 2d 714",
        "volume": "50",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 38",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "38",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 492",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 492",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-495",
      "page": null,
      "quote": "for *Miranda* purposes. ## Rule *Miranda* applies only to custodial interrogation; a station-house setting or a",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-495b",
      "page": null,
      "quote": "*Miranda* warnings are required only where there has been such a restriction on a person's freedom as to render him 'in custody.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-01-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Oregon v. Mathiason",
    "varies_by_point": false,
    "scope_note": "Per curiam; voluntary station-house interview is not custody; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8244686,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8242363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 7861363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Welch",
          "cluster_id": 4883662,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mattox",
          "cluster_id": 4478290,
          "cite": [
            "2018 Ohio 992",
            "108 N.E.3d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacDonald",
          "cluster_id": 5309859,
          "cite": [
            "2017 UT App 124",
            "402 P.3d 91",
            "844 Utah Adv. Rep. 90",
            "2017 WL 3224516",
            "2017 Utah App. LEXIS 124"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Soto",
          "cluster_id": 4401346,
          "cite": [
            "2017 Ohio 4348",
            "93 N.E.3d 204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Parlier",
          "cluster_id": 4373268,
          "cite": [
            "797 S.E.2d 340",
            "2017 WL 899978",
            "2017 N.C. App. LEXIS 136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portillo",
          "cluster_id": 3210008,
          "cite": [
            "787 S.E.2d 822",
            "247 N.C. App. 834",
            "2016 N.C. App. LEXIS 619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane1_negative"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Beheler",
          "cluster_id": 111023,
          "cite": [
            "77 L. Ed. 2d 1275",
            "103 S. Ct. 3517",
            "463 U.S. 1121",
            "1983 U.S. LEXIS 114",
            "51 U.S.L.W. 3934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1407600,
          "cite": [
            "616 P.2d 628",
            "94 Wash. 2d 216",
            "1980 Wash. LEXIS 1360"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Minjarez",
          "cluster_id": 2623400,
          "cite": [
            "81 P.3d 348",
            "2003 WL 22938909"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffers v. United States",
          "cluster_id": 109694,
          "cite": [
            "53 L. Ed. 2d 168",
            "97 S. Ct. 2207",
            "432 U.S. 137",
            "1977 U.S. LEXIS 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hankerson v. North Carolina",
          "cluster_id": 109699,
          "cite": [
            "53 L. Ed. 2d 306",
            "97 S. Ct. 2339",
            "432 U.S. 233",
            "1977 U.S. LEXIS 121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1890229,
          "cite": [
            "313 S.W.3d 274",
            "2010 Tex. Crim. App. LEXIS 722",
            "2010 WL 2382555"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie Sevier v. Kenneth Turner",
          "cluster_id": 440363,
          "cite": [
            "742 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
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
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1728885,
          "cite": [
            "868 S.W.2d 561",
            "1993 Tenn. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. State",
          "cluster_id": 2378796,
          "cite": [
            "866 S.W.2d 9",
            "1993 Tex. Crim. App. LEXIS 166",
            "1993 WL 431505"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Oregon v. Mathiason:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDYzMDk3NjAwMDAwJnM9MzIwNDg0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjkmcz0xNzQ1NjQxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
        "reviewed": 38,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 38,
        "triage_read": 0,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109587 OR 9426651 OR 9426652 OR 9426653)",
    "indexed_citing_opinions": 1709,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109587,
        "count": 1538,
        "count_source": "search"
      },
      {
        "opinion_id": 9426651,
        "count": 200,
        "count_source": "search"
      },
      {
        "opinion_id": 9426652,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426653,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2680,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/oregon-v-mathiason.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzM5MzYmcz0xMDAzODI1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109587+OR+9426651+OR+9426652+OR+9426653%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109587,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 283849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 1289115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109587,
        "cited_id": 1390996,
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
    "date_created": "2026-07-05T16:22:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:25:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:22:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Oregon v. Mathiason

```
<div>
<center><b><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U.S. 492</a></span> (1977)</b></center>
<center><h1>OREGON<br>
v.<br>
MATHIASON.</h1></center>
<center>No. 76-201.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided January 25, 1977.</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE SUPREME COURT OF OREGON.
<p>PER CURIAM.</p>
<p>Respondent Carl Mathiason was convicted of first-degree burglary after a bench trial in which his confession was critical to the State's case. At trial he moved to suppress the confession as the fruit of questioning by the police not preceded by the warnings required in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The trial court refused to exclude the confession because it found that Mathiason was not in custody at the time of the confession.</p>
<p>The Oregon Court of Appeals affirmed respondent's conviction, but on his petition for review in the Supreme Court of Oregon that court by a divided vote reversed the conviction. It found that although Mathiason had not been arrested or otherwise formally detained, "the interrogation took place in a `coercive environment' " of the sort to which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was intended to apply. The court conceded that its holding was contrary to decisions in other jurisdictions, and referred in particular to <i>People</i> v. <i>Yukl,</i> 25 N. Y. 2d 585, <span class="citation" data-id="5525196"><a href="/opinion/5677336/people-v-yukl/" aria-description="Citation for case: People v. Yukl">256 N. E. 2d 172</a></span> (1969). The State of Oregon has <span class="star-pagination">*493</span> petitioned for certiorari to review the judgment of the Supreme Court of Oregon. We think that court has read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> too broadly, and we therefore reverse its judgment.</p>
<p>The Supreme Court of Oregon described the factual situation surrounding the confession as follows:</p>
<blockquote>"An officer of the State Police investigated a theft at a residence near Pendleton. He asked the lady of the house which had been burglarized if she suspected anyone. She replied that the defendant was the only one she could think of. The defendant was a parolee and a `close associate' of her son. The officer tried to contact defendant on three or four occasions with no success. Finally, about 25 days after the burglary, the officer left his card at defendant's apartment with a note asking him to call because `I'd like to discuss something with you.' The next afternoon the defendant did call. The officer asked where it would be convenient to meet. The defendant had no preference; so the officer asked if the defendant could meet him at the state patrol office in about an hour and a half, about 5:00 p. m. The patrol office was about two blocks from defendant's apartment. The building housed several state agencies.</blockquote>
<blockquote>"The officer met defendant in the hallway, shook hands and took him into an office. The defendant was told he was not under arrest. The door was closed. The two sat across a desk. The police radio in another room could be heard. The officer told defendant he wanted to talk to him about a burglary and that his truthfulness would possibly be considered by the district attorney or judge. The officer further advised that the police believed defendant was involved in the burglary and [falsely stated that] defendant's fingerprints were found at the scene. The defendant sat for a few minutes and then said he had taken the property. This occurred within five minutes after defendant had come to the office. The <span class="star-pagination">*494</span> officer then advised defendant of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights and took a taped confession.</blockquote>
<blockquote>"At the end of the taped conversation the officer told defendant he was not arresting him at this time; he was released to go about his job and return to his family. The officer said he was referring the case to the district attorney for him to determine whether criminal charges would be brought. It was 5:30 p. m. when the defendant left the office.</blockquote>
<blockquote>"The officer gave all the testimony relevant to this issue. The defendant did not take the stand either at the hearing on the motion to suppress or at the trial." <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#3" aria-description="Citation for case: State v. Mathiason">275 Ore. 1, 3-4</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#674" aria-description="Citation for case: State v. Mathiason">549 P. 2d 673, 674</a></span> (1976).</blockquote>
<p>The Supreme Court of Oregon reasoned from these facts that:</p>
<blockquote>"We hold the interrogation took place in a `coercive environment.' The parties were in the offices of the State Police; they were alone behind closed doors; the officer informed the defendant he was a suspect in a theft and the authorities had evidence incriminating him in the crime; and the defendant was a parolee under supervision. We are of the opinion that this evidence is not overcome by the evidence that the defendant came to the office in response to a request and was told he was not under arrest." <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#5" aria-description="Citation for case: State v. Mathiason"><i>Id.,</i> at 5</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#675" aria-description="Citation for case: State v. Mathiason">549 P. 2d, at 675</a></span>.</blockquote>
<p>Our decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> set forth rules of police procedure applicable to "custodial interrogation." "By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. Subsequently we have found the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> principle applicable to questioning which takes place in a prison setting during a suspect's term of imprisonment on a separate offense, <i>Mathis</i> v. <i>United States,</i> <span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968), and to questioning taking place in a <span class="star-pagination">*495</span> suspect's home, after he has been arrested and is no longer free to go where he pleases, <i>Orozco</i> v. <i>Texas,</i> <span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969).</p>
<p>In the present case, however, there is no indication that the questioning took place in a context where respondent's freedom to depart was restricted in any way. He came voluntarily to the police station, where he was immediately informed that he was not under arrest. At the close of a 1/2-hour interview respondent did in fact leave the police station without hindrance. It is clear from these facts that Mathiason was not in custody "or otherwise deprived of his freedom of action in any significant way."</p>
<p>Such a noncustodial situation is not converted to one in which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> applies simply because a reviewing court concludes that, even in the absence of any formal arrest or restraint on freedom of movement, the questioning took place in a "coercive environment." Any interview of one suspected of a crime by a police officer will have coercive aspects to it, simply by virtue of the fact that the police officer is part of a law enforcement system which may ultimately cause the suspect to be charged with a crime. But police officers are not required to administer <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to everyone whom they question. Nor is the requirement of warnings to be imposed simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are required only where there has been such a restriction on a person's freedom as to render him "in custody." It was <i>that</i> sort of coercive environment to which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> by its terms was made applicable, and to which it is limited.</p>
<p>The officer's false statement about having discovered Mathiason's fingerprints at the scene was found by the Supreme Court of Oregon to be another circumstance contributing to the coercive environment which makes the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rationale applicable. Whatever relevance this fact <span class="star-pagination">*496</span> may have to other issues in the case, it has nothing to do with whether respondent was in custody for purposes of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule.</p>
<p>The petition for certiorari is granted, the judgment of the Oregon Supreme Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BRENNAN would grant the writ but dissents from the summary disposition and would set the case for oral argument.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>The respondent in this case was interrogated behind closed doors at police headquarters in connection with a burglary investigation. He had been named by the victim of the burglary as a suspect, and was told by the police that they believed he was involved. He was falsely informed that his fingerprints had been found at the scene, and in effect was advised that by cooperating with the police he could help himself. Not until after he had confessed was he given the warnings set forth in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>The Court today holds that for constitutional purposes all this is irrelevant because respondent had not " `been taken into custody or otherwise deprived of his freedom of action in any significant way.' " <i>Ante,</i> at 494, quoting <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 444</a></span>. I do not believe that such a determination is possible on the record before us. It is true that respondent was not formally placed under arrest, but surely formalities alone cannot control. At the very least, if respondent entertained an objectively reasonable belief that he was not free to leave during the questioning, then he was "deprived of his freedom of action in a significant way."<sup>[1]</sup><span class="star-pagination">*497</span> Plainly the respondent could have so believed, after being told by the police that they thought he was involved in a burglary and that his fingerprints had been found at the scene. Yet the majority is content to note that "there is no indication that . . . respondent's freedom to depart was restricted in any way," <i>ante,</i> at 495, as if a silent record (and no state-court findings) means that the State has sustained its burden, see <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 489</a></span> (1972), of demonstrating that respondent received his constitutional due.<sup>[2]</sup></p>
<p>More fundamentally, however, I cannot agree with the Court's conclusion that if respondent were not in custody no warnings were required. I recognize that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is limited to custodial interrogations, but that is because, as we noted last Term, the facts in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases raised only this "narrow issue." <i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). The rationale of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, is not so easily cabined.</p>
<p><i>Miranda</i> requires warnings to "combat" a situation in which there are "inherently compelling pressures which work to undermine the individual's will to resist and to compel <span class="star-pagination">*498</span> him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. It is of course true, as the Court notes, that "[a]ny interview of one suspected of a crime by a police officer will have coercive aspects to it." <i>Ante,</i> at 495. But it does not follow that because police "are not required to administer <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to everyone whom they question," <i>ibid.,</i> that they need not administer warnings to <i>anyone,</i> unless the factual setting of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases is replicated. Rather, faithfulness to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires us to distinguish situations that resemble the "coercive aspects" of custodial interrogation from those that more nearly resemble "[g]eneral on-the-scene questioning . . . or other general questioning of citizens in the fact-finding process" which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> states usually can take place without warnings. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477</a></span>.</p>
<p>In my view, even if respondent were not in custody, the coercive elements in the instant case were so pervasive as to require <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>-type warnings.<sup>[3]</sup> Respondent was interrogated in "privacy" and in "unfamiliar surroundings," factors on which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> places great stress. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#449" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 449-450</a></span>; see also <i>Beckwith</i> v. <i>United States, supra,</i> at 346 n. 7. The investigation had focused on respondent. And respondent was subjected to some of the "deceptive stratagems," <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 455</a></span>, which called forth the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. I therefore agree with the Oregon Supreme Court that to excuse the absence of warnings given these facts is "contrary to the rationale expressed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>" <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#5" aria-description="Citation for case: State v. Mathiason">275 Ore. 1, 5</a></span>, <span class="citation" data-id="9616436"><a href="/opinion/1390996/state-v-mathiason/#675" aria-description="Citation for case: State v. Mathiason">549 P. 2d 673, 675</a></span> (1976).<sup>[4]</sup></p>
<p><span class="star-pagination">*499</span> The privilege against self-incrimination "has always been `as broad as the mischief against which it seeks to guard.' " <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#459" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 459-460</a></span>, quoting <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). Today's decision means, however, that the Fifth Amendment privilege does not provide full protection against mischiefs equivalent to, but different from, custodial interrogation.<sup>[5]</sup> See also <i>Beckwith</i> v. <i>United States, supra</i><i>.</i> It is therefore important to note that the state courts remain free, in interpreting state constitutions, to guard against the evil clearly identified by this case.<sup>[6]</sup></p>
<p>I respectfully dissent.</p>
<p>MR. JUSTICE STEVENS, dissenting.</p>
<p>In my opinion the issues presented by this case are too important to be decided summarily. Of particular importance <span class="star-pagination">*500</span> is the fact that the respondent was on parole at the time of his interrogation in the police station. This fact lends support to inconsistent conclusions.</p>
<p>On the one hand, the State surely has greater power to question a parolee about his activities than to question someone else. Moreover, as a practical matter, it seems unlikely that a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning would have much effect on a parolee's choice between silence and responding to police interrogation. Arguably, therefore, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are entirely inappropriate in the parole context.</p>
<p>On the other hand, a parolee is technically in legal custody continuously until his sentence has been served. Therefore, if a formalistic analysis of the custody question is to determine when the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning is necessary, a parolee should always be warned. Moreover, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> teaches that even if a suspect is not in custody, warnings are necessary if he is "otherwise deprived of his freedom of action in any significant way." If a parolee being questioned in a police station is not described by that language, today's decision qualifies that part of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to some extent. I believe we would have a better understanding of the extent of that qualification, and therefore of the situations in which warnings must be given to a suspect who is not technically in custody, if we had the benefit of full argument and plenary consideration.</p>
<p>I therefore respectfully dissent from the Court's summary disposition.</p>
<h2>NOTES</h2>
<p>[1]  See, <i>e. g., </i><i>United States</i> v. <i>Hall,</i> <span class="citation" data-id="288311"><a href="/opinion/288311/united-states-v-glenn-w-hall/#544" aria-description="Citation for case: United States v. Glenn W. Hall">421 F. 2d 540, 544-545</a></span> (CA2 1969) (Friendly, J.); <i>Lowe</i> v. <i>United States,</i> <span class="citation" data-id="283849"><a href="/opinion/283849/arnold-lowe-v-united-states/" aria-description="Citation for case: Arnold Lowe v. United States">407 F. 2d 1391</a></span> (CA9 1969); <i>People</i> v. <i>Arnold,</i> <span class="citation" data-id="9853164"><a href="/opinion/1289115/people-v-arnold/" aria-description="Citation for case: People v. Arnold">66 Cal. 2d 438</a></span>, <span class="citation" data-id="9853164"><a href="/opinion/1289115/people-v-arnold/" aria-description="Citation for case: People v. Arnold">426 P. 2d 515</a></span> (1967); <i>People</i> v. <i>Rodney P.,</i> 21 N. Y. 2d 1, <span class="citation" data-id="9787785"><a href="/opinion/2590535/people-v-rodney-panonymous/" aria-description="Citation for case: People v. Rodney P.(Anonymous)">233 N. E. 2d 255</a></span> (1967). See also cases collected in Annot., 31 A. L. R. 3d 565, 581-583 (1970 and Supp. 1976).
</p>
<p>It has been noted that as a logical matter, a person who honestly but unreasonably believes he is in custody is subject to the same coercive pressures as one whose belief is reasonable; this suggests that such persons also are entitled to warnings. See, <i>e. g.,</i> LaFave, "Street Encounters" and the Constitution: Terry, Sibron, Peters, and Beyond, <span class="citation no-link">67 Mich. L. Rev. 39</span>, 105 (1968); Smith, The Threshold Question in Applying Miranda: What Constitutes Custodial Interrogation?, 25 S. C. L. Rev. 699, 711-714 (1974).</p>
<p>[2]  The Court's action is particularly inappropriate because the record of this case has not been transmitted to us, and thus our knowledge of the facts is limited to the information contained in the petition and in the opinions of the state courts.</p>
<p>[3]  I do not rule out the possibility that lesser warnings would suffice when a suspect is not in custody but is subjected to a highly coercive atmosphere. See, <i>e. g., </i><i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#348" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 348-349</a></span> (1976) (MARSHALL, J., concurring in judgment); ALI, Model Code of Pre-Arraignment Procedure § 110.1 (2) (Approved Draft 1975) (suspects interrogated at police station must be advised of their right to leave and right to consult with counsel, relatives, or friends).</p>
<p>[4]  See also Graham, What is "Custodial Interrogation?": California's Anticipatory Application of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span>,</i> <span class="citation no-link">14 UCLA L. Rev. 59</span>, 81-82 (1966); Smith, <i>supra,</i> n. 1, at 732, 735.</p>
<p>[5]  I trust today's decision does not suggest that police officers can circumvent <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> by deliberately postponing the official "arrest" and the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings until the necessary incriminating statements have been obtained.</p>
<p>[6]  See, <i>e. g., </i><i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#384" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 384</a></span> (1976) (MARSHALL, J., dissenting); <i>Baxter</i> v. <i>Palmigiano,</i> <span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#324" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 324, 338-339</a></span> (1976) (BRENNAN, J., dissenting); <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#120" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 120-121</a></span> (1975) (BRENNAN, J., dissenting); Wilkes, The New Federalism in Criminal Procedure: State Court Evasion of the Burger Court, 62 Ky. L. J. 421 (1974); Wilkes, More on the New Federalism in Criminal Procedure, 63 Ky. L. J. 873 (1975).
</p>
<p>In <i><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>,</i> this Court reversed a decision of the South Dakota Supreme Court holding that routine inventory searches of impounded automobiles, made without probable cause or consent, violated the Fourth Amendment. The case was remanded, like this one, "for further proceedings not inconsistent with [the] opinion." <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#376" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 376</a></span>. On remand, the South Dakota Supreme Court held that such searches violated a nearly identical provision of the State Constitution, and that therefore the seized evidence should have been suppressed. <i>State</i> v. <i>Opperman,</i> 89 S. D., <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152</a></span> (1976).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Ornelas v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Ornelas v. United States"
type: case
citation: "517 U.S. 690 (1996)"
parallel_cite: "116 S. Ct. 1657; 134 L. Ed. 2d 911"
neutral_cite: 1996 U.S. LEXIS 3391
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-06-10
docket: 95-5257
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ornelas v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/"
  cluster_id: 118030
  opinion_id: 118030
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Brinegar v. United States]]", "[[Terry v. Ohio]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "reasonable-suspicion", "standard-of-review", "de-novo"]
holding: "Appellate review of determinations of reasonable suspicion and probable cause to make a warrantless search/stop is de novo (historical…"
lake:
  record_id: Ornelas v. United States
  status: verified
  projected_at: 2026-07-09
---

# Ornelas v. United States

*517 U.S. 690 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A 20-year veteran detective conducting drug-interdiction surveillance in Milwaukee noticed a car with California plates and, after a records check, stopped and questioned Ornelas and a companion. The detective searched the car and found two kilograms of cocaine behind a loose interior panel. The District Court found reasonable suspicion for the stop and probable cause for the search and denied suppression; the Seventh Circuit reviewed those determinations "deferentially," for "clear error."

## Issue
What standard of review applies on appeal to a trial court's determinations of reasonable suspicion to make a stop and probable cause to conduct a warrantless search.

## Rule
The ultimate determinations are reviewed [[Common Legal Terms#de-novo|de novo]]. "We hold that the ultimate questions of reasonable suspicion and probable cause to make a warrantless search should be reviewed *de novo*." — 517 U.S. at 691. ^pin-691

"We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed *de novo* on appeal." — 517 U.S. at 699. ^pin-699

At the same time, "a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers." — [*Id.* at 699–700](https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/#:~:text=a%20reviewing%20court%20should%20take). ^pin-699a

## Application
The Seventh Circuit had reviewed the reasonable-suspicion and probable-cause rulings only for [[Common Legal Terms#clear-error|clear error]]. Because the ultimate mixed questions of reasonable suspicion and probable cause must instead be reviewed [[Common Legal Terms#de-novo|de novo]] — while the historical facts (here, the officer's observations and the loose panel) are reviewed for [[Common Legal Terms#clear-error|clear error]] with due weight to his experience-based inferences — the Court [[Reading and Citing Cases#vacated|vacated]] the judgment and [[Reading and Citing Cases#on-remand|remanded]] for the Court of Appeals to review those determinations [[Common Legal Terms#de-novo|de novo]].

## Conclusion
Reasonable-suspicion and probable-cause determinations get independent, [[Common Legal Terms#de-novo|de novo]] appellate review (with clear-error review of the underlying historical facts); the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. The [[Common Legal Terms#de-novo|de novo]] standard for reviewing reasonable suspicion and probable cause remains controlling.

## Appears on
- [[Probable Cause]] — *Key — Progeny / Refinement*

## Sources
- *Ornelas v. United States*, 517 U.S. 690 (1996) — https://www.courtlistener.com/opinion/118030/ornelas-v-united-states/ — pinpoints: 691, 699–700.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "256b0fc9b80152a9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ornelas v. United States"}, "payload": {"all": [{"cite": "517 U.S. 690", "page": "690", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "517"}, {"cite": "116 S. Ct. 1657", "page": "1657", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "134 L. Ed. 2d 911", "page": "911", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}, {"cite": "1996 U.S. LEXIS 3391", "page": "3391", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1996"}], "display": "517 U.S. 690", "official": {"cite": "517 U.S. 690", "page": "690", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "517"}, "official_selection_present": true, "record_id": "Ornelas v. United States"}}
{"assertion_id": "16d59ad234cb8aa6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-699a", "record_id": "Ornelas v. United States"}, "payload": {"fragment": "#:~:text=a%20reviewing%20court%20should%20take", "page": null, "pin_id": "pin-699a", "pinpoint_status": "star-verified", "quote": "a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers.", "quote_fidelity": "matched", "record_id": "Ornelas v. United States", "star_marker": "699"}}
{"assertion_id": "2e563bfc8d18a3ad", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-699", "record_id": "Ornelas v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-699", "pinpoint_status": "slip-only", "quote": "We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed *de novo* on appeal.", "quote_fidelity": "mismatch", "record_id": "Ornelas v. United States", "star_marker": null}}
{"assertion_id": "e6e02f67d196cfb3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-691", "record_id": "Ornelas v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-691", "pinpoint_status": "slip-only", "quote": "## Issue What standard of review applies on appeal to a trial court's determinations of reasonable suspicion to make a stop and probable cause to conduct a warrantless search. ## Rule The ultimate determinations are reviewed de novo.", "quote_fidelity": "mismatch", "record_id": "Ornelas v. United States", "star_marker": null}}
{"assertion_id": "311521b7461527d6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ornelas v. United States"}, "payload": {"as_of_content": "1996-06-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Ornelas v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Ornelas v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ornelas v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ornelas v. United States",
    "case_name_short": "Ornelas",
    "case_name_full": "ORNELAS Et Al. v. UNITED STATES",
    "input_case_name": "Ornelas v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-06-10",
    "year": 1996,
    "docket": "95-5257",
    "cluster_id": 118030,
    "lead_opinion_id": 118030,
    "sibling_ids": [
      118030,
      9433305,
      9433306
    ],
    "absolute_url": "/opinion/118030/ornelas-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9283005,
        "score": 20,
        "case_name": "Ornelas-Martinez v. United States"
      },
      {
        "cluster_id": 9273679,
        "score": 20,
        "case_name": "Ornelas v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 U.S. 690",
      "volume": "517",
      "reporter": "U.S.",
      "page": "690",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 1657",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1657",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 911",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 3391",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3391",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 U.S. 690",
        "volume": "517",
        "reporter": "U.S.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 1657",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1657",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 911",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 3391",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3391",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 U.S. 690",
    "official_selection": {
      "court_class": "scotus",
      "selected": "517 U.S. 690",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-691",
      "page": null,
      "quote": "## Issue What standard of review applies on appeal to a trial court's determinations of reasonable suspicion to make a stop and probable cause to conduct a warrantless search. ## Rule The ultimate determinations are reviewed de novo.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-699",
      "page": null,
      "quote": "We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed *de novo* on appeal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-699a",
      "page": null,
      "quote": "a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers.",
      "star_marker": "699",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24571,
      "fragment": "#:~:text=a%20reviewing%20court%20should%20take",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ornelas v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Ornelas v. United States:lane1_negative"
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
        "journal_ref": "Ornelas v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane1_negative"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edward H. Phillips v. Awh Corporation, Hopeman Brothers, Inc., and Lofton Corporation, Defendants-Cross",
          "cluster_id": 791122,
          "cite": [
            "415 F.3d 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gasperini v. Center for Humanities, Inc.",
          "cluster_id": 2528498,
          "cite": [
            "135 L. Ed. 2d 659",
            "116 S. Ct. 2211",
            "518 U.S. 415",
            "1996 U.S. LEXIS 4051",
            "64 U.S.L.W. 4607",
            "96 Cal. Daily Op. Serv. 4548",
            "10 Fla. L. Weekly Fed. S 26",
            "96 Daily Journal DAR 7338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bajakajian",
          "cluster_id": 118234,
          "cite": [
            "141 L. Ed. 2d 314",
            "118 S. Ct. 2028",
            "524 U.S. 321",
            "1998 U.S. LEXIS 4172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lilly v. Virginia",
          "cluster_id": 118300,
          "cite": [
            "144 L. Ed. 2d 117",
            "119 S. Ct. 1887",
            "527 U.S. 116",
            "1999 U.S. LEXIS 4006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kothe v. State",
          "cluster_id": 1504839,
          "cite": [
            "152 S.W.3d 54",
            "2004 Tex. Crim. App. LEXIS 1749",
            "2004 WL 2347781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cooper Industries, Inc. v. Leatherman Tool Group, Inc.",
          "cluster_id": 118424,
          "cite": [
            "149 L. Ed. 2d 674",
            "121 S. Ct. 1678",
            "532 U.S. 424",
            "2001 U.S. LEXIS 3520",
            "2001 Cal. Daily Op. Serv. 3820",
            "69 U.S.L.W. 4299",
            "58 U.S.P.Q. 2d (BNA) 1641",
            "2001 Daily Journal DAR 4673",
            "2001 Colo. J. C.A.R. 2407",
            "14 Fla. L. Weekly Fed. S 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
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
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 1382816,
          "cite": [
            "43 S.W.3d 527",
            "2001 Tex. Crim. App. LEXIS 30",
            "2001 WL 387433"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael B. Smith v. Douglas Lamz and the Village of Algonquin, a Municipal Corporation",
          "cluster_id": 781088,
          "cite": [
            "321 F.3d 680",
            "2003 U.S. App. LEXIS 3888",
            "2003 WL 730093"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ornelas v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118030 OR 9433305 OR 9433306) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgxODYyNDAwMDAwJnM9OTM5MjY5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118030 OR 9433305 OR 9433306)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDAmcz03OTA0ODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118030 OR 9433305 OR 9433306)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjk2MjA0ODAwMDAwJnM9OTQzMDcwNiZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118030 OR 9433305 OR 9433306)",
    "indexed_citing_opinions": 4083,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118030,
        "count": 3455,
        "count_source": "search"
      },
      {
        "opinion_id": 9433305,
        "count": 699,
        "count_source": "search"
      },
      {
        "opinion_id": 9433306,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7200,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ornelas-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Nzg2MzYmcz0xMDY0ODY0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118030+OR+9433305+OR+9433306%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118030,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 106071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 117937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 117982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 537758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 538805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 561395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 583951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 597487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118030,
        "cited_id": 663109,
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
    "date_created": "2026-07-05T16:25:07Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:28:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:25:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ornelas v. United States

```
<div>
<center><b><span class="citation" data-id="9433305"><a href="/opinion/118030/ornelas-v-united-states/" aria-description="Citation for case: Ornelas v. United States">517 U.S. 690</a></span> (1996)</b></center>
<center><h1>ORNELAS et al.<br>
v.<br>
UNITED STATES</h1></center>
<center>No. 95-5257.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 26, 1996.</center>
<center>Decided May 28, 1996.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p>Rehnquist, C. J., delivered the opinion of the Court, in which Stevens, O'Connor, Kennedy, Souter, Thomas, Ginsburg, and Breyer, JJ., joined. Scalia, J., filed a dissenting opinion, <i>post,</i> p. 700.</p>
<p><span class="star-pagination">*692</span> <i>Robert G. LeBell</i> argued the cause for petitioners. With him on the briefs was <i>Brian W. Gleason.</i> </p>
<p><i>Cornelia T. L. Pillard</i> argued the cause for the United States. With her on the brief were <i>Solicitor General Days, Acting Assistant Attorney General Keeney, Deputy Solicitor General Dreeben,</i> and <i>Joel M. Gershowitz.</i> </p>
<p><i>Peter D. Isakoff,</i> by invitation of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./516/1008/">516 U. S. 1008</a></span>, argued the cause and filed a brief as <i>amicus curiae</i> in support of the judgment below.<sup>[*]</sup></p>
<p>Chief Justice Rehnquist delivered the opinion of the Court.</p>
<p>Petitioners each pleaded guilty to possession of cocaine with intent to distribute. They reserved their right to appeal the District Court's denial of their motion to suppress the cocaine found in their car. The District Court had found reasonable suspicion to stop and question petitioners as they entered their car, and probable cause to remove one of the interior panels where a package containing two kilograms of cocaine was found. The Court of Appeals opined that the findings of reasonable suspicion to stop, and probable cause to search, should be reviewed "deferentially," and "for clear error." We hold that the ultimate questions of reasonable suspicion and probable cause to make a warrantless search should be reviewed <i>de novo.</i> </p>
<p>The facts are not disputed. In the early morning of a December day in 1992, Detective Michael Pautz, a 20-year veteran of the Milwaukee County Sheriff's Department with 2 years specializing in drug enforcement, was conducting drug-interdiction surveillance in downtown Milwaukee. <span class="star-pagination">*692</span> Pautz noticed a 1981 two-door Oldsmobile with California license plates in a motel parking lot. The car attracted Pautz's attention for two reasons: because older model, twodoor General Motors cars are a favorite with drug couriers because it is easy to hide things in them; and because California is a "source State" for drugs. Detective Pautz radioed his dispatcher to inquire about the car's registration. The dispatcher informed Pautz that the owner was either Miguel Ledesma Ornelas or Miguel Ornelas Ledesma from San Jose, California; Pautz was unsure which name the dispatcher gave. Detective Pautz checked the motel registry and learned that an Ismael Ornelas accompanied by a second man had registered at 4 a.m., without reservations.</p>
<p>Pautz called for his partner, Donald Hurrle, a detective with approximately 25 years of law enforcement experience, assigned for the past 6 years to the drug enforcement unit. When Hurrle arrived at the scene, the officers contacted the local office of the Drug Enforcement Administration (DEA) and asked DEA personnel to run the names Miguel Ledesma Ornelas and Ismael Ornelas through the Narcotics and Dangerous Drugs Information System (NADDIS), a federal database of known and suspected drug traffickers. Both names appeared in NADDIS. The NADDIS report identified Miguel Ledesma Ornelas as a heroin dealer from El Centro, California, and Ismael Ornelas, Jr., as a cocaine dealer from Tucson, Arizona. The officers then summoned Deputy Luedke and the department's drug-sniffing dog, Merlin. Upon their arrival, Detective Pautz left for another assignment. Detective Hurrle informed Luedke of what they knew and together they waited.</p>
<p>Sometime later, petitioners emerged from the motel and got into the Oldsmobile. Detective Hurrle approached the car, identified himself as a police officer, and inquired whether they had any illegal drugs or contraband. Petitioners answered "No." Hurrle then asked for identification and was given two California driver's licenses bearing the names <span class="star-pagination">*693</span> Saul Ornelas and Ismael Ornelas. Hurrle asked them if he could search the car and petitioners consented. The men appeared calm, but Ismael was shaking somewhat. Deputy Luedke, who over the past nine years had searched approximately 2,000 cars for narcotics, searched the Oldsmobile's interior. He noticed that a panel above the right rear passenger armrest felt somewhat loose and suspected that the panel might have been removed and contraband hidden inside. Luedke would testify later that a screw in the doorjam adjacent to the loose panel was rusty, which to him meant that the screw had been removed at some time. Luedke dismantled the panel and discovered two kilograms of cocaine. Petitioners were arrested.</p>
<p>Petitioners filed pretrial motions to suppress, alleging that the police officers violated their Fourth Amendment rights when the officers detained them in the parking lot and when Deputy Luedke searched inside the panel without a warrant.<sup>[1]</sup> The Government conceded in the court below that when the officers approached petitioners in the parking lot, a reasonable person would not have felt free to leave, so the encounter was an investigatory stop. See <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#716" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">16 F. 3d 714, 716</a></span> (CA7 1994). An investigatory stop is permissible under the Fourth Amendment if supported by reasonable suspicion, <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and a warrantless search of a car is valid if based on probable cause, <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/#569" aria-description="Citation for case: California v. Acevedo">500 U. S. 565, 569-570</a></span> (1991).</p>
<p><span class="star-pagination">*694</span> After conducting an evidentiary hearing, the Magistrate Judge concluded that the circumstances gave the officers reasonable suspicion, but not probable cause. The Magistrate found, as a finding of fact, that there was no rust on the screw and hence concluded that Deputy Luedke had an insufficient basis to conclude that drugs would be found within the panel. The Magistrate nonetheless recommended that the District Court deny the suppression motions because he thought, given the presence of the drug-sniffing dog, that the officers would have found the cocaine by lawful means eventually and therefore the drugs were admissible under the inevitable discovery doctrine. See <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984).</p>
<p>The District Court adopted the Magistrate's recommendation with respect to reasonable suspicion, but not its reasoning as to probable cause. The District Court thought that the model, age, and source-State origin of the car, and the fact that two men traveling together checked into a motel at 4 o'clock in the morning without reservations, formed a drug-courier profile and that this profile together with the NADDIS reports gave rise to reasonable suspicion of drugtrafficking activity; in the court's view, reasonable suspicion became probable cause when Deputy Luedke found the loose panel. Accordingly, the court ruled that the cocaine need not be excluded.<sup>[2]</sup></p>
<p>The Court of Appeals reviewed deferentially the District Court's determinations of reasonable suspicion and probable cause; it would reverse only upon a finding of "clear error."<sup>[3]</sup><span class="star-pagination">*695</span> <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#719" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">16 F. 3d, at 719</a></span>. The court found no clear error in the reasonable-suspicion analysis and affirmed that determination. <i><span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas">Ibid.</a></span></i> With respect to the probable-cause finding, however, the court remanded the case for a determination on whether Luedke was credible when testifying about the loose panel. <span class="citation" data-id="663109"><a href="/opinion/663109/united-states-v-ismael-ornelas-ledesma-and-saul-ornelas/#721" aria-description="Citation for case: United States v. Ismael Ornelas-Ledesma and Saul Ornelas"><i>Id.,</i> at 721-722</a></span>.</p>
<p>On remand, the Magistrate Judge expressly found the testimony credible. The District Court accepted the finding, and once again ruled that probable cause supported the search. The Seventh Circuit held that determination not clearly erroneous. Judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%203d/52/328/">52 F. 3d 328</a></span> (1995).</p>
<p>We granted certiorari to resolve the conflict among the Circuits over the applicable standard of appellate review. <span class="citation multiple-matches"><a href="/c/U.%20S./516/963/">516 U. S. 963</a></span> (1996).<sup>[4]</sup></p>
<p>Articulating precisely what "reasonable suspicion" and "probable cause" mean is not possible. They are commonsense, nontechnical conceptions that deal with "`the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act.' " <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#231" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 231</a></span> (1983) (quoting <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949)); see <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7-8</a></span> (1989). As such, the standards are "not readily, or even usefully, reduced to a neat set of legal <span class="star-pagination">*696</span> rules." <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>. We have described reasonable suspicion simply as "a particularized and objective basis" for suspecting the person stopped of criminal activity, <i>United States</i> v. <i>Cortez,</i> <span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417-418</a></span> (1981), and probable cause to search as existing where the known facts and circumstances are sufficient to warrant a man of reasonable prudence in the belief that contraband or evidence of a crime will be found, see <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 175-176</a></span>; <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 238</a></span>. We have cautioned that these two legal principles are not "finely-tuned standards," comparable to the standards of proof beyond a reasonable doubt or of proof by a preponderance of the evidence. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#235" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 235</a></span>. They are instead fluid concepts that take their substantive content from the particular contexts in which the standards are being assessed. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232</a></span>; <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i>  at 175</a></span> ("The standard of proof [for probable cause] is . . . correlative to what must be proved"); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963) ("This Cour[t] [has a] long-established recognition that standards of reasonableness under the Fourth Amendment are not susceptible of Procrustean application"; "[e]ach case is to be decided on its own facts and circumstances" (internal quotation marks omitted)); <i>Terry</i> v. <i>Ohio,</i>  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span> (the limitations imposed by the Fourth Amendment "will have to be developed in the concrete factual circumstances of individual cases").</p>
<p>The principal components of a determination of reasonable suspicion or probable cause will be the events which occurred leading up to the stop or search, and then the decision whether these historical facts, viewed from the standpoint of an objectively reasonable police officer, amount to reasonable suspicion or to probable cause. The first part of the analysis involves only a determination of historical facts, but the second is a mixed question of law and fact: "[T]he historical facts are admitted or established, the rule of law is undisputed, and the issue is whether the facts satisfy the [relevant] statutory [or constitutional] standard, or to put it another <span class="star-pagination">*697</span> way, whether the rule of law as applied to the established facts is or is not violated." <i>Pullman-Standard</i> v. <i>Swint,</i> <span class="citation" data-id="9428745"><a href="/opinion/110698/pullman-standard-v-swint/#289" aria-description="Citation for case: Pullman-Standard v. Swint">456 U. S. 273, 289, n. 19</a></span> (1982).</p>
<p>We think independent appellate review of these ultimate determinations of reasonable suspicion and probable cause is consistent with the position we have taken in past cases. We have never, when reviewing a probable-cause or reasonable-suspicion determination ourselves, expressly deferred to the trial court's determination. See, <i>e. g., </i><i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar, supra</a></span></i> (rejecting District Court's conclusion that the police lacked probable cause); <i>Alabama</i> v. <i>White,</i> <span class="citation" data-id="9432055"><a href="/opinion/112454/alabama-v-white/" aria-description="Citation for case: Alabama v. White">496 U. S. 325</a></span> (1990) (conducting independent review and finding reasonable suspicion). A policy of sweeping deference would permit, "[i]n the absence of any significant difference in the facts," "the Fourth Amendment's incidence [to] tur[n] on whether different trial judges draw general conclusions that the facts are sufficient or insufficient to constitute probable cause." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#171" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 171</a></span>. Such varied results would be inconsistent with the idea of a unitary system of law. This, if a matter-of-course, would be unacceptable.</p>
<p>In addition, the legal rules for probable cause and reasonable suspicion acquire content only through application. Independent review is therefore necessary if appellate courts are to maintain control of, and to clarify, the legal principles. See <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 114</a></span> (1985) (where the "relevant legal principle can be given meaning only through its application to the particular circumstances of a case, the Court has been reluctant to give the trier of fact's conclusions presumptive force and, in so doing, strip a federal appellate court of its primary function as an expositor of law").</p>
<p>Finally, <i>de novo</i> review tends to unify precedent and will come closer to providing law enforcement officers with a defined "`set of rules which, in most instances, makes it possible to reach a correct determination beforehand as to whether an invasion of privacy is justified in the interest of <span class="star-pagination">*698</span> law enforcement.' " <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981); see also <i>Thompson</i> v. <i>Keohane,</i> <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#115" aria-description="Citation for case: Thompson v. Keohane">516 U. S. 99, 115</a></span> (1995) ("[T]he law declaration aspect of independent review potentially may guide police, unify precedent, and stabilize the law," and those effects "serve legitimate law enforcement interests").</p>
<p>It is true that because the mosaic which is analyzed for a reasonable-suspicion or probable-cause inquiry is multifaceted, "one determination will seldom be a useful `precedent' for another," <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 238, n. 11</a></span>. But there are exceptions. For instance, the circumstances in <i>Brinegar</i> , <i>supra,</i> and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), were so alike that we concluded that reversing the Court of Appeals' decision in <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> was necessary to be faithful to <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#178" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 178</a></span> ("Nor . . . can we find in the present facts any substantial basis for distinguishing this case from the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> case"). We likewise recognized the similarity of facts in <i>United States</i> v. <i><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">Sokolow, supra</a></span></i><i>,</i> and <i>Florida</i> v. <i>Royer,</i> <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983) (in both cases, the defendant traveled under an assumed name; paid for an airline ticket in cash with a number of small bills; traveled from Miami, a source city for illicit drugs; and appeared nervous in the airport). The same was true both in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), and <i>California</i> v. <i>Acevedo,</i> <span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U. S. 565</a></span> (1991), see <i><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">id.</a></span></i> , at 572 ("The facts in this case closely resemble the facts in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> "); and in <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), and <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438</a></span> (1980), see <i><span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/" aria-description="Citation for case: Reid v. Georgia">id.</a></span></i> , at 443 (Powell, J., concurring) ("facts [in <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span></i> ] [are] remarkably similar to those in the present case"). And even where one case may not squarely control another one, the two decisions when viewed together may usefully add to the body of law on the subject.</p>
<p>The Court of Appeals, in adopting its deferential standard of review here, reasoned that <i>de novo</i> review for warrantless searches would be inconsistent with the "`great deference' " paid when reviewing a decision to issue a warrant, see <i>Illi-</i>  <span class="star-pagination">*699</span> <i>nois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983). See <i>United States</i> v. <i>Spears,</i> <span class="citation" data-id="9482988"><a href="/opinion/583951/united-states-v-charles-j-spears-also-known-as-blackie-and-donald/#269" aria-description="Citation for case: United States v. Charles J. Spears, Also Known as...">965 F. 2d 262, 269-271</a></span> (CA7 1992). We cannot agree. The Fourth Amendment demonstrates a "strong preference for searches conducted pursuant to a warrant," <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#236" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i>  at 236</a></span>, and the police are more likely to use the warrant process if the scrutiny applied to a magistrate's probablecause determination to issue a warrant is less than that for warrantless searches. Were we to eliminate this distinction, we would eliminate the incentive.</p>
<p>We therefore hold that as a general matter determinations of reasonable suspicion and probable cause should be reviewed <i>de novo</i> on appeal. Having said this, we hasten to point out that a reviewing court should take care both to review findings of historical fact only for clear error and to give due weight to inferences drawn from those facts by resident judges and local law enforcement officers.</p>
<p>A trial judge views the facts of a particular case in light of the distinctive features and events of the community; likewise, a police officer views the facts through the lens of his police experience and expertise. The background facts provide a context for the historical facts, and when seen together yield inferences that deserve deference. For example, what may not amount to reasonable suspicion at a motel located alongside a transcontinental highway at the height of the summer tourist season may rise to that level in December in Milwaukee. That city is unlikely to have been an overnight stop selected at the last minute by a traveler coming from California to points east. The 85-mile width of Lake Michigan blocks any further eastward progress. And while the city's salubrious summer climate and seasonal attractions bring many tourists at that time of year, the same is not true in December. Milwaukee's average daily high temperature in that month is 31 degrees and its average daily low is 17 degrees; the percentage of possible sunshine is only 38 percent. It is a reasonable inference that a Californian stopping in Milwaukee in December is either there <span class="star-pagination">*700</span> to transact business or to visit family or friends. The background facts, though rarely the subject of explicit findings, inform the judge's assessment of the historical facts.</p>
<p>In a similar vein, our cases have recognized that a police officer may draw inferences based on his own experience in deciding whether probable cause exists. See, <i>e. g., </i><i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#897" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 897</a></span> (1975). To a layman the sort of loose panel below the back seat armrest in the automobile involved in this case may suggest only wear and tear, but to Officer Luedke, who had searched roughly 2,000 cars for narcotics, it suggested that drugs may be secreted inside the panel. An appeals court should give due weight to a trial court's finding that the officer was credible and the inference was reasonable.</p>
<p>We vacate the judgments and remand the case to the Court of Appeals to review <i>de novo</i> the District Court's determinations that the officer had reasonable suspicion and probable cause in this case.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Scalia, dissenting.</p>
<p>The Court today decides that a district court's determinations whether there was probable cause to justify a warrantless search and reasonable suspicion to make an investigatory stop should be reviewed <i>de novo.</i> We have in the past reviewed some mixed questions of law and fact on a <i>de novo</i>  basis, and others on a deferential basis, depending upon essentially practical considerations. Because, with respect to the questions at issue here, the purpose of the determination and its extremely fact-bound nature will cause <i>de novo</i> review to have relatively little benefit, it is in my view unwise to require courts of appeals to undertake the searching inquiry that standard requires. I would affirm the judgment of the Court of Appeals.</p>
<p>As the Court recognizes, determinations of probable cause and reasonable suspicion involve a two-step process. First, <span class="star-pagination">*701</span> a court must identify all of the relevant historical facts known to the officer at the time of the stop or search; and second, it must decide whether, under a standard of objective reasonableness, those facts would give rise to a reasonable suspicion justifying a stop or probable cause to search. See <i>ante,</i> at 696-697. Because this second step requires application of an objective legal standard to the facts, it is properly characterized as a mixed question of law and fact. See <i>ibid.; </i><i>Pullman-Standard</i> v. <i>Swint,</i> <span class="citation" data-id="9428745"><a href="/opinion/110698/pullman-standard-v-swint/#289" aria-description="Citation for case: Pullman-Standard v. Swint">456 U. S. 273, 289, n. 19</a></span> (1982).</p>
<p>Merely labeling the issues "mixed questions," however, does not establish that they receive <i>de novo</i> review. While it is well settled that appellate courts "accep[t] findings of fact that are not `clearly erroneous' but decid[e] questions of law <i>de novo,</i> " <i>First Options of Chicago, Inc.</i> v. <i>Kaplan,</i> <span class="citation" data-id="117937"><a href="/opinion/117937/first-options-of-chicago-inc-v-kaplan/#948" aria-description="Citation for case: First Options of Chicago, Inc. v. Kaplan">514 U. S. 938, 948</a></span> (1995), there is no rigid rule with respect to mixed questions. We have said that "deferential review of mixed questions of law and fact is warranted when it appears that the district court is `better positioned' than the appellate court to decide the issue in question or that probing appellate scrutiny will not contribute to the clarity of legal doctrine." <i>Salve Regina College</i> v. <i>Russell,</i> <span class="citation" data-id="9432235"><a href="/opinion/112564/salve-regina-college-v-russell/#233" aria-description="Citation for case: Salve Regina College v. Russell">499 U. S. 225, 233</a></span> (1991) (citing <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 114</a></span> (1985)).</p>
<p>These primary factors that counsel in favor of deferential review of some mixed questions of law and factexpertise of the district court and lack of law-clarifying value in the appellate decisionare ordinarily present with respect to determinations of reasonable suspicion and probable cause. The factual details bearing upon those determinations are often numerous and (even when supported by uncontroverted police testimony) subject to credibility determinations. An appellate court never has the benefit of the district court's intimate familiarity with the details of the casenor the full benefit of its hearing of the live testimony, unless the district court makes specific findings on the "totality of the circumstances" bearing upon the stop or search. <span class="star-pagination">*702</span> As we recognized in <i>Cooter &amp; Gell</i> v. <i>Hartmarx Corp.,</i> <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">496 U. S. 384</a></span> (1990), a case holding that deferential (abuseof-discretion) review should be applied to a district court's Federal Rule of Civil Procedure 11 determination that an attorney did not conduct a reasonable inquiry or entertain a "substantiated belief" regarding the nonfrivolousness of the complaint, see <i><span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">id.,</a></span></i> at 393: A district court, "[f]amiliar with the issues and litigants . . . is better situated than the court of appeals to marshal the pertinent facts and apply the factdependent legal standard . . . ." <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#402" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp."><i>Id.,</i> at 402</a></span>.</p>
<p>Moreover, as the Court acknowledges, "reasonable suspicion" and "probable cause" are "commonsense, nontechnical conceptions that deal with ` "the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act."` " <i>Ante,</i> at 695 (quoting <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#231" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 231</a></span> (1983) (quoting <i>Brinegar</i>  v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949))). Where a trial court makes such commonsense determinations based on the totality of circumstances, it is ordinarily accorded deference. What we said in a case concerning the question whether certain payments were a "gift" excludable from income under the Internal Revenue Code is equally pertinent here.</p>
<blockquote>"Decision of the issue presented in these cases must be based ultimately on the application of the fact-finding tribunal's experience with the mainsprings of human conduct to the totality of the facts of each case. The nontechnical nature of the . . . standard, the close relationship of it to the data of practical human experience, and the multiplicity of relevant factual elements, with their various combinations, creating the necessity of ascribing the proper force to each, confirm us in our conclusion that primary weight in this area must be given to the conclusions of the trier of fact." <i>Commissioner</i>  v. <i>Duberstein,</i> <span class="citation" data-id="9422005"><a href="/opinion/106071/commissioner-v-duberstein/#289" aria-description="Citation for case: Commissioner v. Duberstein">363 U. S. 278, 289</a></span> (1960).</blockquote>
<p><span class="star-pagination">*703</span> With respect to the second factor counseling in favor of deferential review, level of law-clarifying value in the appellate decision: Law clarification requires generalization, and some issues lend themselves to generalization much more than others. Thus, in <i>Pierce</i> v. <i>Underwood,</i> <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#562" aria-description="Citation for case: Pierce v. Underwood">487 U. S. 552, 562</a></span> (1988), a principal basis for our applying an abuse-ofdiscretion standard to a district court's determination that the United States' litigating position was "substantially justified" within the meaning of the Equal Access to Justice Act, <span class="citation no-link">28 U. S. C. § 2412</span>(d), was that the question was "a multifarious and novel question, little susceptible, for the time being at least, of useful generalization." <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#562" aria-description="Citation for case: Pierce v. Underwood">487 U. S., at 562</a></span>. Probable-cause and reasonable-suspicion determinations are similarly resistant to generalization. As the Court recognizes, these are "fluid concepts," "`not readily, or even usefully, reduced to a neat set of legal rules' "; and "because the mosaic which is analyzed for a reasonable-suspicion or probable-cause inquiry is multifaceted, `one determination will seldom be a useful "precedent" for another.' " <i>Ante,</i> at 695-696, 698 (quoting <i>Illinois</i> v. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#232" aria-description="Citation for case: Illinois v. Gates"><i>Gates, supra,</i> at 232, 238, n. 11</a></span>). The Court maintains that there will be exceptions to thisthat fact patterns will occasionally repeat themselves, so that a prior <i>de novo</i> appellate decision will provide useful guidance in a similar case. <i>Ante,</i> at 698. I do not dispute that, but I do not understand why we should allow the exception to frame the rule. Here, as in <i>Anderson</i> v. <i>Bessemer City,</i> <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#574" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U. S. 564, 574-575</a></span> (1985), "[d]uplication of the trial judge's efforts in the court of appeals would very likely contribute only negligibly to the accuracy of fact determination at a huge cost in diversion of judicial resources."</p>
<p>The facts of this very case illustrate the futility of attempting to craft useful precedent from the fact-intensive review demanded by determinations of probable cause and reasonable suspicion. On remand, in conducting <i>de novo</i> review, the Seventh Circuit might consider, <i>inter alia,</i> the following <span class="star-pagination">*704</span> factors relevant to its determination whether there was probable cause to conduct a warrantless search and reasonable suspicion justifying the investigatory stop: (i) the two NADDIS tips; (ii) that the car was a 1981 two-door General Motors product; (iii) that the car was from California, a source State; (iv) that the car was in Milwaukee; (v) that it was December; (vi) that one suspect checked into the hotel at 4 a.m.; (vii) that he did not have reservations; (viii) that he had one traveling companion; (ix) that one suspect appeared calm but shaking; and (x) that there was a loose panel in the car door. If the Seventh Circuit were to find that this unique confluence of factors supported probable cause and reasonable suspicion, the absence of any one of these factors in the next case would render the precedent inapplicable.</p>
<p>Of course, even when all of the factors <i>are</i> replicated, use of a <i>de novo</i> standard as opposed to a deferential standard will provide greater clarity only where the latter would not suffice to set the trial court's conclusion aside. For where the appellate court holds, on the basis of deferential review, that it <i>was</i> reversible error for a district court to find probable cause or reasonable suspicion in light of certain facts, it advances the clarity of the law just as much as if it had reversed the district court after conducting plenary review.</p>
<p>In the present case, an additional factor counseling against <i>de novo</i> review must be mentioned: The prime benefit of <i>de novo</i> appellate review in criminal cases is, of course, to prevent a miscarriage of justice that might result from permitting the verdict of guilty to rest upon the legal determinations of a single judge. But the issue in these probablecause and reasonable-suspicion cases is not innocence but deterrence of unlawful police conduct. That deterrence will not be <i>at all</i> lessened if the trial judge's determination, right or wrong, is subjected to only deferential review.</p>
<p>The Court is wrong in its assertion, <i>ante,</i> at 698-699, that unless there is a dual standard of reviewdeferential review of a magistrate's decision to issue a warrant, and <i>de novo</i>  <span class="star-pagination">*705</span> review of a district court's <i>ex post facto</i> approval of a warrantless searchthe incentive to obtain a warrant would be eliminated. In <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#913" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 913</a></span> (1984), we held that "reliable physical evidence seized by officers reasonably relying on a warrant issued by a detached and neutral magistrate . . . should be admissible in the prosecutor's case in chief." Only a warrant can provide this assurance that the fruits of even a technically improper search will be admissible. Law enforcement officers would still have ample incentive to proceed by warrant.</p>
<p>Finally, I must observe that the Court does not appear to have the courage of its conclusions. In an apparent effort to reduce the unproductive burden today's decision imposes upon appellate courts, or perhaps to salvage some of the trial court's superior familiarity with the facts that it has cast aside, the Court suggests that an appellate court should give "due weight" to a trial court's finding that an officer's inference of wrongdoing (<i>i. e.,</i> his assessment of probable cause to search) was reasonable. <i>Ante,</i> at 700. The Court cannot have it both ways. This finding of "reasonableness" is precisely what it has told us the appellate court must review <i>de novo;</i> and in <i>de novo</i> review, the "weight due" to a trial court's finding is zero. In the last analysis, therefore, the Court's opinion seems to me not only wrong but contradictory.</p>
<p></p>
<h2>* * *</h2>
<p>I would affirm the judgment of the Seventh Circuit on the ground that it correctly applied a deferential standard of review to the District Court's findings of probable cause and reasonable suspicion.</p>
<h2>NOTES</h2>
<p>[*]   <i>Tracey Maclin, Steven R. Shapiro,</i> and <i>Barbara E. Bergman</i> filed a brief for the American Civil Liberties Union et al.as <i>amici curiae</i>  urging reversal.
</p>
<p><i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak,</i> and <i>Bernard J. Farber</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging affirmance.</p>
<p>[1]  Petitioners also alleged that they had not given their consent to search the interior of the car. The Magistrate Judge rejected this claim, finding that the record "clearly establishe[d] consent to search the Oldsmobile" and that "neither [petitioner] placed any restrictions on the areas the officers could search." App. 21. The Magistrate ruled that this consent did not give the officers authority to search inside the panel, however, because under Seventh Circuit precedent the police may not dismantle the car body during an otherwise valid search unless the police have probable cause to believe the car's panels contain narcotics. See <i>United States</i> v. <i>Garcia,</i>  <span class="citation" data-id="537758"><a href="/opinion/537758/united-states-v-carlos-garcia-and-jose-luis-garcia/#1419" aria-description="Citation for case: United States v. Carlos Garcia and Jose Luis Garcia">897 F. 2d 1413, 1419-1420</a></span> (1990). We assume correct the Circuit's limitation on the scope of consent only for purposes of this decision.</p>
<p>[2]  The District Court emphasized twice that it did not reject the Magistrate's recommendation with respect to the inevitable discovery doctrine. App. 30-31, and n. 2; <i>id.,</i> at 43-44. But on appeal the Government did not defend the seizure on this alternative ground and the Seventh Circuit considered the argument waived. <i>Id.,</i> at 71-72.</p>
<p>[3]  While the Seventh Circuit uses the term "clear error" to denote the deferential standard applied when reviewing determinations of reasonable suspicion or probable cause, we think the preferable term is "abuse of discretion." See <i>Pierce</i> v. <i>Underwood,</i> <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#558" aria-description="Citation for case: Pierce v. Underwood">487 U. S. 552, 558</a></span> (1988). "Clear error" is aterm of art derived from Rule 52(a) of the Federal Rules of Civil Procedure, and applies when reviewing questions of fact.</p>
<p>[4]  Compare, <i>e. g., </i><i>United States</i> v. <i>Puerta,</i> <span class="citation" data-id="597487"><a href="/opinion/597487/united-states-v-antonio-medina-puerta/#1300" aria-description="Citation for case: United States v. Antonio Medina Puerta">982 F. 2d 1297, 1300</a></span> (CA9 1992) (<i>de novo</i> review); <i>United States</i> v. <i>Ramos,</i> <span class="citation" data-id="561395"><a href="/opinion/561395/united-states-v-armando-balbino-ramos-evaristo-ramos/#972" aria-description="Citation for case: United States v. Armando Balbino Ramos, Evaristo Ramos">933 F. 2d 968, 972</a></span> (CA11 1991) (same), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./503/908/">503 U. S. 908</a></span> (1992); <i>United States</i> v. <i>Patrick,</i>  <span class="citation" data-id="9480132"><a href="/opinion/538805/united-states-v-christopher-patrick-linda-taylor-and-christopher-patrick/#171" aria-description="Citation for case: United States v. Christopher Patrick, Linda Taylor and...">899 F. 2d 169, 171</a></span> (CA2 1990) (same), with <i>United States</i> v. <i>Spears,</i> <span class="citation" data-id="9482988"><a href="/opinion/583951/united-states-v-charles-j-spears-also-known-as-blackie-and-donald/#268" aria-description="Citation for case: United States v. Charles J. Spears, Also Known as...">965 F. 2d 262, 268-271</a></span> (CA7 1992) (clear error).
</p>
<p>The United States, in accord with petitioners, contends that a <i>de novo</i>  standard of review should apply to determinations of probable cause and reasonable suspicion. We therefore invited Peter D. Isakoff to brief and argue this case as <i>amicus curiae</i> in support of the judgment below. <span class="citation multiple-matches"><a href="/c/U.%20S./516/1008/">516 U. S. 1008</a></span> (1996). Mr. Isakoff accepted the appointment and has well fulfilled his assigned responsibility.</p>

</div>
```

---
