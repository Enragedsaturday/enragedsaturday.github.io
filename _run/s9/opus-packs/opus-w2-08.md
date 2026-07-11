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

## GROUP: _overhaul2/lake/cases/Carpenter v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Carpenter v. United States"
type: case
citation: "585 U.S. 296 (2018)"
parallel_cite: "138 S. Ct. 2206; 201 L. Ed. 2d 507"
neutral_cite: 2018 U.S. LEXIS 3844
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-06-22
docket: 16-402
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Carpenter v. United States
  varies_by_point: false
  scope_note: "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/"
  cluster_id: 4510032
  opinion_id: 4287285
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — CSLI dividing line (co-home, A6)"
related: ["[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[Riley v. California]]", "[[Chatrie v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "cell-site", "third-party-doctrine"]
holding: "Acquiring extended historical cell-site location information is a search — a reasonable expectation of privacy in 'the whole of [one's] physical movements'; narrows the third-party doctrine for digital-age data."
lake:
  record_id: Carpenter v. United States
  status: verified
  projected_at: 2026-07-06
---

# Carpenter v. United States

*585 U.S. 296 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a series of armed robberies, the FBI obtained 127 days of Carpenter's historical cell-site location information (CSLI) from his wireless carriers under the Stored Communications Act, which required only "specific and articulable facts" — a showing short of probable cause — rather than a warrant. The records (nearly 12,900 location points) placed his phone near the robbery sites. He moved to suppress the CSLI as the product of a warrantless search.

## Issue
Whether the Government's acquisition of historical cell-site records that chronicle a person's past movements is a search under the Fourth Amendment.

## Rule
Yes. "Whether the Government employs its own surveillance technology as in *Jones* or leverages the technology of a wireless carrier, we hold that an individual maintains a legitimate expectation of privacy in the record of his physical movements as captured through CSLI." — *Carpenter v. United States*, 585 U.S. 296 (2018) (slip op., at 11). ^pin-op11

Because that acquisition is a search, the Government must generally obtain a warrant supported by probable cause before acquiring such records. The Court declined to extend the third-party doctrine of *[[Smith v. Maryland]]* and *[[United States v. Miller]]* to the "qualitatively different category of cell-site records."

## Application
The Government accessed 127 days of Carpenter's CSLI without a warrant, relying instead on a court order issued on less than probable cause. Because that data provided an all-encompassing, retrospective record of his whereabouts — "an intimate window into a person's life" — its acquisition invaded a legitimate expectation of privacy and was a search; on these facts the warrantless acquisition could not be justified by the third-party doctrine.

## Conclusion
Acquiring Carpenter's historical CSLI was a Fourth Amendment search; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. The Court's holding was expressly narrow, declining to disturb conventional surveillance techniques or other business records.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carpenter* itself **narrows** the third-party doctrine ([[Smith v. Maryland]]) for digital-age location data and builds on the mosaic concern voiced in the [[United States v. Jones]] [[Common Legal Terms#concurring-opinion|concurrences]].
- **Extended (2026):** *[[Chatrie v. United States]]*, 609 U.S. ___ (2026), **applies and extends *Carpenter*** to bulk **geofence / Google Location History** data — holding its acquisition is a Fourth Amendment search even for a short (~2-hour) window and even though held by a third party (rejecting the opt-in/third-party rationale) — and leaves geofence-warrant probable cause/[[Particularity|particularity]] for remand. *Carpenter* remains good law and anchors that ruling.

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key — Progeny / Refinement*
- [[Third-Party Doctrine & CSLI]] — *Key — CSLI dividing line (co-home)*

## Sources
- *Carpenter v. United States*, 585 U.S. 296 (2018) — https://www.courtlistener.com/opinion/4510032/carpenter-v-united-states/ — pinpoint: slip op., at 11 (CL carries the slip opinion; cluster 4510032 → opinion 4287285).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7e3bf97717823440", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Carpenter v. United States"}, "payload": {"all": [{"cite": "585 U.S. 296", "page": "296", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "585"}, {"cite": "138 S. Ct. 2206", "page": "2206", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "138"}, {"cite": "201 L. Ed. 2d 507", "page": "507", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "201"}, {"cite": "2018 U.S. LEXIS 3844", "page": "3844", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2018"}], "display": "585 U.S. 296", "official": {"cite": "585 U.S. 296", "page": "296", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "585"}, "official_selection_present": true, "record_id": "Carpenter v. United States"}}
{"assertion_id": "7b89405c7a6b03e2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op11", "record_id": "Carpenter v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op11", "pinpoint_status": "slip-only", "quote": "— a showing short of probable cause — rather than a warrant. The records (nearly 12,900 location points) placed his phone near the robbery sites. He moved to suppress the CSLI as the product of a warrantless search. ## Issue Whether the Government's acquisition of historical cell-site records that chronicle a person's past movements is a search under the Fourth Amendment. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Carpenter v. United States", "star_marker": null}}
{"assertion_id": "a494181936d54fc5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Carpenter v. United States"}, "payload": {"as_of_content": "2018-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Carpenter v. United States", "scope_note": "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law.", "varies_by_point": false}}
```

### lake record — Carpenter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carpenter v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Carpenter v. United States",
    "case_name_short": "Carpenter",
    "case_name_full": "",
    "input_case_name": "Carpenter v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-06-22",
    "year": 2018,
    "docket": "16-402",
    "cluster_id": 4510032,
    "lead_opinion_id": 4287285,
    "sibling_ids": [
      4287285
    ],
    "absolute_url": "/opinion/4510032/carpenter-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4512666,
        "score": 20,
        "case_name": "Carpenter v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "585 U.S. 296",
      "volume": "585",
      "reporter": "U.S.",
      "page": "296",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 2206",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "2206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 507",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3844",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "585 U.S. 296",
        "volume": "585",
        "reporter": "U.S.",
        "page": "296",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 2206",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "2206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 507",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "507",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3844",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3844",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "585 U.S. 296",
    "official_selection": {
      "court_class": "scotus",
      "selected": "585 U.S. 296",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op11",
      "page": null,
      "quote": "\u2014 a showing short of probable cause \u2014 rather than a warrant. The records (nearly 12,900 location points) placed his phone near the robbery sites. He moved to suppress the CSLI as the product of a warrantless search. ## Issue Whether the Government's acquisition of historical cell-site records that chronicle a person's past movements is a search under the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Carpenter v. United States",
    "varies_by_point": false,
    "scope_note": "Carpenter itself narrows the third-party doctrine for digital-age location data; it is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Devin J. Johnson",
          "cluster_id": 10132115,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas v. State",
          "cluster_id": 10680321,
          "cite": [
            "902 S.E.2d 566",
            "319 Ga. 123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Singleton",
          "cluster_id": 9506618,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Janvier",
          "cluster_id": 9494606,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamin Kidron Stocker v. the State of Texas",
          "cluster_id": 9329108,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane1_negative"
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
        "journal_ref": "Carpenter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Perrin Davis v. Facebook, Inc.",
          "cluster_id": 4743751,
          "cite": [
            "956 F.3d 589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caro",
          "cluster_id": 4629272,
          "cite": [
            "248 Cal. Rptr. 3d 96",
            "7 Cal. 5th 463",
            "442 P.3d 316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matthew Jones",
          "cluster_id": 4757714,
          "cite": [
            "960 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North American Butterfly Association v. Chad F. Wolf",
          "cluster_id": 4795622,
          "cite": [
            "977 F.3d 1244"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eaglin",
          "cluster_id": 8443840,
          "cite": [
            "913 F.3d 88"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Kurtz, J.",
          "cluster_id": 10317095,
          "cite": [
            "294 A.3d 509",
            "2023 Pa. Super. 72"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
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
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leaders of Beautiful Struggle v. Baltimore Police Department",
          "cluster_id": 4894627,
          "cite": [
            "2 F.4th 330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Troester v. Starbucks Corporation",
          "cluster_id": 4520879,
          "cite": [
            "235 Cal. Rptr. 3d 820",
            "5 Cal. 5th 829",
            "421 P.3d 1114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In the Matter of the Application of Jason Leopold to Unseal Certain Electronic Surveillance Applications and Orders",
          "cluster_id": 4766181,
          "cite": [
            "964 F.3d 1121"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
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
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kaufhold",
          "cluster_id": 4770908,
          "cite": [
            "2020 Ohio 3835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trump v. Mazars USA, LLP",
          "cluster_id": 4766665,
          "cite": [
            "140 S. Ct. 2019",
            "207 L. Ed. 2d 951"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charlie L. Green",
          "cluster_id": 4833880,
          "cite": [
            "981 F.3d 945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 10367330,
          "cite": [
            "850 S.E.2d 110",
            "310 Ga. 180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelsey Rose Juliana v. United States",
          "cluster_id": 4707560,
          "cite": [
            "947 F.3d 1159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Dunkins, A.",
          "cluster_id": 10315445,
          "cite": [
            "229 A.3d 622",
            "2020 Pa. Super. 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kunz",
          "cluster_id": 9400913,
          "cite": [
            "68 F.4th 748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcus Walker",
          "cluster_id": 4861532,
          "cite": [
            "990 F.3d 316"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rex Hammond",
          "cluster_id": 4877368,
          "cite": [
            "996 F.3d 374"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Young, Jr. v. State of Hawaii",
          "cluster_id": 4867182,
          "cite": [
            "992 F.3d 765"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric K. Brooks v. D Miller",
          "cluster_id": 9421763,
          "cite": [
            "78 F.4th 1267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carpenter v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4287285) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQzNjczNjAwMDAwJnM9NjI0NzMxNCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284287285%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4287285)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMiZzPTEwMzgyNzc1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%284287285%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4287285)",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 6,
        "triage_snippet_classified": 172
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4287285)",
    "indexed_citing_opinions": 525,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4287285,
        "count": 525,
        "count_source": "search"
      }
    ],
    "citation_count": 1207,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/carpenter-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNDgxMDUmcz0xMDU4MTk5OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284287285%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4287285,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 99422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 103990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 104758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 137006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 145633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 148797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 149703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 158478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 181032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 612140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 746807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 779290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1215380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 1440458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2443377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2513954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2680439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2789928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 2812209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 3235330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 4181058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4287285,
        "cited_id": 4274911,
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
    "date_created": "2026-07-04T23:36:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:40:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:36:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Carpenter v. United States (truncated)

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                 CARPENTER v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE SIXTH CIRCUIT

   No. 16–402.      Argued November 29, 2017—Decided June 22, 2018
Cell phones perform their wide and growing variety of functions by con-
  tinuously connecting to a set of radio antennas called “cell sites.”
  Each time a phone connects to a cell site, it generates a time-stamped
  record known as cell-site location information (CSLI). Wireless carri-
  ers collect and store this information for their own business purposes.
  Here, after the FBI identified the cell phone numbers of several rob-
  bery suspects, prosecutors were granted court orders to obtain the
  suspects’ cell phone records under the Stored Communications Act.
  Wireless carriers produced CSLI for petitioner Timothy Carpenter’s
  phone, and the Government was able to obtain 12,898 location points
  cataloging Carpenter’s movements over 127 days—an average of 101
  data points per day. Carpenter moved to suppress the data, arguing
  that the Government’s seizure of the records without obtaining a
  warrant supported by probable cause violated the Fourth Amend-
  ment. The District Court denied the motion, and prosecutors used
  the records at trial to show that Carpenter’s phone was near four of
  the robbery locations at the time those robberies occurred. Carpen-
  ter was convicted. The Sixth Circuit affirmed, holding that Carpen-
  ter lacked a reasonable expectation of privacy in the location infor-
  mation collected by the FBI because he had shared that information
  with his wireless carriers.
Held:
    1. The Government’s acquisition of Carpenter’s cell-site records
 was a Fourth Amendment search. Pp. 4–18.
       (a) The Fourth Amendment protects not only property interests
 but certain expectations of privacy as well. Katz v. United States, 389
 U. S. 347, 351. Thus, when an individual “seeks to preserve some-
 thing as private,” and his expectation of privacy is “one that society is
2                   CARPENTER v. UNITED STATES

                                  Syllabus

    prepared to recognize as reasonable,” official intrusion into that
    sphere generally qualifies as a search and requires a warrant sup-
    ported by probable cause. Smith v. Maryland, 442 U. S. 735, 740 (in-
    ternal quotation marks and alterations omitted). The analysis re-
    garding which expectations of privacy are entitled to protection is
    informed by historical understandings “of what was deemed an un-
    reasonable search and seizure when [the Fourth Amendment] was
    adopted.” Carroll v. United States, 267 U. S. 132, 149. These Found-
    ing-era understandings continue to inform this Court when applying
    the Fourth Amendment to innovations in surveillance tools. See, e.g.,
    Kyllo v. United States, 533 U. S. 27. Pp. 4–7.
         (b) The digital data at issue—personal location information
    maintained by a third party—does not fit neatly under existing prec-
    edents but lies at the intersection of two lines of cases. One set ad-
    dresses a person’s expectation of privacy in his physical location and
    movements. See, e.g., United States v. Jones, 565 U. S. 400 (five Jus-
    tices concluding that privacy concerns would be raised by GPS track-
    ing). The other addresses a person’s expectation of privacy in infor-
    mation voluntarily turned over to third parties. See United States v.
    Miller, 425 U. S. 435 (no expectation of privacy in financial records
    held by a bank), and Smith, 442 U. S. 735 (no expectation of privacy
    in records of dialed telephone numbers conveyed to telephone compa-
    ny). Pp. 7–10.
         (c) Tracking a person’s past movements through CSLI partakes
    of many of the qualities of GPS monitoring considered in Jones—it is
    detailed, encyclopedic, and effortlessly compiled. At the same time,
    however, the fact that the individual continuously reveals his loca-
    tion to his wireless carrier implicates the third-party principle of
    Smith and Miller. Given the unique nature of cell-site records, this
    Court declines to extend Smith and Miller to cover them. Pp. 10–18.
            (1) A majority of the Court has already recognized that indi-
    viduals have a reasonable expectation of privacy in the whole of their
    physical movements. Allowing government access to cell-site rec-
    ords—which “hold for many Americans the ‘privacies of life,’ ” Riley v.
    California, 573 U. S. ___, ___—contravenes that expectation. In fact,
    historical cell-site records present even greater privacy concerns than
    the GPS monitoring considered in Jones: They give the Government
    near perfect surveillance and allow it to travel back in time to retrace
    a person’s whereabouts, subject only to the five-year retention poli-
    cies of most wireless carriers. The Government contends that CSLI
    data is less precise than GPS information, but it thought the data ac-
    curate enough here to highlight it during closing argument in Car-
    penter’s trial. At any rate, the rule the Court adopts “must take ac-
    count of more sophisticated systems that are already in use or in
                   Cite as: 585 U. S. ____ (2018)                    3

                              Syllabus

development,” Kyllo, 533 U. S., at 36, and the accuracy of CSLI is
rapidly approaching GPS-level precision. Pp. 12–15.
       (2) The Government contends that the third-party doctrine
governs this case, because cell-site records, like the records in Smith
and Miller, are “business records,” created and maintained by wire-
less carriers. But there is a world of difference between the limited
types of personal information addressed in Smith and Miller and the
exhaustive chronicle of location information casually collected by
wireless carriers.
   The third-party doctrine partly stems from the notion that an indi-
vidual has a reduced expectation of privacy in information knowingly
shared with another. Smith and Miller, however, did not rely solely
on the act of sharing. They also considered “the nature of the partic-
ular documents sought” and limitations on any “legitimate ‘expecta-
tion of privacy’ concerning their contents.” Miller, 425 U. S., at 442.
In mechanically applying the third-party doctrine to this case the
Government fails to appreciate the lack of comparable limitations on
the revealing nature of CSLI.
   Nor does the second rationale for the third-party doctrine—
voluntary exposure—hold up when it comes to CSLI. Cell phone lo-
cation information is not truly “shared” as the term is normally un-
derstood. First, cell phones and the services they provide are “such a
pervasive and insistent part of daily life” that carrying one is indis-
pensable to participation in modern society. Riley, 573 U. S., at ___.
Second, a cell phone logs a cell-site record by dint of its operation,
without any affirmative act on the user’s part beyond powering up.
Pp. 15–17.
     (d) This decision is narrow. It does not express a view on matters
not before the Court; does not disturb the application of Smith and
Miller or call into question conventional surveillance techniques and
tools, such as security cameras; does not address other business rec-
ords that might incidentally reveal location information; and does not
consider other collection techniques involving foreign affairs or na-
tional security. Pp. 17–18.
   2. The Government did not obtain a warrant supported by proba-
ble cause before acquiring Carpenter’s cell-site records. It acquired
those records pursuant to a court order under the Stored Communi-
cations Act, which required the Government to show “reasonable
grounds” for believing that the records were “relevant and material to
an ongoing investigation.” 18 U. S. C. §2703(d). That showing falls
well short of the probable cause required for a warrant. Consequent-
ly, an order issued under §2703(d) is not a permissible mechanism for
accessing historical cell-site records. Not all orders compelling the
production of documents will require a showing of probable cause. A
4                  CARPENTER v. UNITED STATES

                                 Syllabus

    warrant is required only in the rare case where the suspect has a le-
    gitimate privacy interest in records held by a third party. And even
    though the Government will generally need a warrant to access
    CSLI, case-specific exceptions—e.g., exigent circumstances—may
    support a warrantless search. Pp. 18–22.
819 F. 3d 880, reversed and remanded.

   ROBERTS, C. J., delivered the opinion of the Court, in which GINS-
BURG,  BREYER, SOTOMAYOR, and KAGAN, JJ., joined. KENNEDY, J., filed a
dissenting opinion, in which THOMAS and ALITO, JJ., joined. THOMAS, J.,
filed a dissenting opinion. ALITO, J., filed a dissenting opinion, in which
THOMAS, J., joined. GORSUCH, J., filed a dissenting opinion.
                        Cite as: 585 U. S. ____ (2018)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 16–402
                                   _________________


    TIMOTHY IVORY CARPENTER, PETITIONER v.

               UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                                 [June 22, 2018] 


  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  This case presents the question whether the Govern-
ment conducts a search under the Fourth Amendment
when it accesses historical cell phone records that provide
a comprehensive chronicle of the user’s past movements.
                               I

                               A

   There are 396 million cell phone service accounts in the
United States—for a Nation of 326 million people. Cell
phones perform their wide and growing variety of func-
tions by connecting to a set of radio antennas called “cell
sites.” Although cell sites are usually mounted on a tower,
they can also be found on light posts, flagpoles, church
steeples, or the sides of buildings. Cell sites typically have
several directional antennas that divide the covered area
into sectors.
   Cell phones continuously scan their environment look-
ing for the best signal, which generally comes from the
closest cell site.       Most modern devices, such as
smartphones, tap into the wireless network several times
2              CARPENTER v. UNITED STATES

                      Opinion of the Court

a minute whenever their signal is on, even if the owner is
not using one of the phone’s features. Each time the
phone connects to a cell site, it generates a time-stamped
record known as cell-site location information (CSLI). The
precision of this information depends on the size of the
geographic area covered by the cell site. The greater the
concentration of cell sites, the smaller the coverage area.
As data usage from cell phones has increased, wireless
carriers have installed more cell sites to handle the traffic.
That has led to increasingly compact coverage areas,
especially in urban areas.
  Wireless carriers collect and store CSLI for their own
business purposes, including finding weak spots in their
network and applying “roaming” charges when another
carrier routes data through their cell sites. In addition,
wireless carriers often sell aggregated location records to
data brokers, without individual identifying information of
the sort at issue here. While carriers have long retained
CSLI for the start and end of incoming calls, in recent
years phone companies have also collected location infor-
mation from the transmission of text messages and rou-
tine data connections. Accordingly, modern cell phones
generate increasingly vast amounts of increasingly precise
CSLI.
                              B
   In 2011, police officers arrested four men suspected of
robbing a series of Radio Shack and (ironically enough) T-
Mobile stores in Detroit. One of the men confessed that,
over the previous four months, the group (along with a
rotating cast of getaway drivers and lookouts) had robbed
nine different stores in Michigan and Ohio. The suspect
identified 15 accomplices who had participated in the
heists and gave the FBI some of their cell phone numbers;
the FBI then reviewed his call records to identify addi-
tional numbers that he had called around the time of the
                 Cite as: 585 U. S. ____ (2018)            3

                     Opinion of the Court

robberies.
   Based on that information, the prosecutors applied for
court orders under the Stored Communications Act to
obtain cell phone records for petitioner Timothy Carpenter
and several other suspects. That statute, as amended in
1994, permits the Government to compel the disclosure of
certain telecommunications records when it “offers specific
and articulable facts showing that there are reasonable
grounds to believe” that the records sought “are relevant
and material to an ongoing criminal investigation.” 18
U. S. C. §2703(d). Federal Magistrate Judges issued two
orders directing Carpenter’s wireless carriers—MetroPCS
and Sprint—to disclose “cell/site sector [information] for
[Carpenter’s] telephone[ ] at call origination and at call
termination for incoming and outgoing calls” during the
four-month period when the string of robberies occurred.
App. to Pet. for Cert. 60a, 72a. The first order sought 152
days of cell-site records from MetroPCS, which produced
records spanning 127 days. The second order requested
seven days of CSLI from Sprint, which produced two days
of records covering the period when Carpenter’s phone was
“roaming” in northeastern Ohio. Altogether the Govern-
ment obtained 12,898 location points cataloging Carpen-
ter’s movements—an average of 101 data points per day.
   Carpenter was charged with six counts of robbery and
an additional six counts of carrying a firearm during a
federal crime of violence. See 18 U. S. C. §§924(c), 1951(a).
Prior to trial, Carpenter moved to suppress the cell-site
data provided by the wireless carriers. He argued that the
Government’s seizure of the records violated the Fourth
Amendment because they had been obtained without a
warrant supported by probable cause. The District Court
denied the motion. App. to Pet. for Cert. 38a–39a.
   At trial, seven of Carpenter’s confederates pegged him
as the leader of the operation. In addition, FBI agent
Christopher Hess offered expert testimony about the cell-
4              CARPENTER v. UNITED STATES

                      Opinion of the Court

site data. Hess explained that each time a cell phone taps
into the wireless network, the carrier logs a time-stamped
record of the cell site and particular sector that were used.
With this information, Hess produced maps that placed
Carpenter’s phone near four of the charged robberies. In
the Government’s view, the location records clinched the
case: They confirmed that Carpenter was “right where the
. . . robbery was at the exact time of the robbery.” App.
131 (closing argument). Carpenter was convicted on all
but one of the firearm counts and sentenced to more than
100 years in prison.
    The Court of Appeals for the Sixth Circuit affirmed. 819
F. 3d 880 (2016). The court held that Carpenter lacked a
reasonable expectation of privacy in the location infor-
mation collected by the FBI because he had shared that
information with his wireless carriers. Given that cell
phone users voluntarily convey cell-site data to their
carriers as “a means of establishing communication,” the
court concluded that the resulting business records are not
entitled to Fourth Amendment protection. Id., at 888
(quoting Smith v. Maryland, 442 U. S. 735, 741 (1979)).
    We granted certiorari. 582 U. S. ___ (2017).
                             II

                             A

  The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” The
“basic purpose of this Amendment,” our cases have recog-
nized, “is to safeguard the privacy and security of individ-
uals against arbitrary invasions by governmental offi-
cials.” Camara v. Municipal Court of City and County of
San Francisco, 387 U. S. 523, 528 (1967). The Founding
generation crafted the Fourth Amendment as a “response
to the reviled ‘general warrants’ and ‘writs of assistance’ of
the colonial era, which allowed British officers to rum-
                    Cite as: 585 U. S. ____ (2018)                  5

                        Opinion of the Court

mage through homes in an unrestrained search for evi-
dence of criminal activity.” Riley v. California, 573 U. S.
___, ___ (2014) (slip op., at 27). In fact, as John Adams
recalled, the patriot James Otis’s 1761 speech condemning
writs of assistance was “the first act of opposition to the
arbitrary claims of Great Britain” and helped spark the
Revolution itself. Id., at ___–___ (slip op., at 27–28) (quot-
ing 10 Works of John Adams 248 (C. Adams ed. 1856)).
   For much of our history, Fourth Amendment search
doctrine was “tied to common-law trespass” and focused on
whether the Government “obtains information by physi-
cally intruding on a constitutionally protected area.”
United States v. Jones, 565 U. S. 400, 405, 406, n. 3 (2012).
More recently, the Court has recognized that “property
rights are not the sole measure of Fourth Amendment
violations.” Soldal v. Cook County, 506 U. S. 56, 64
(1992). In Katz v. United States, 389 U. S. 347, 351 (1967),
we established that “the Fourth Amendment protects
people, not places,” and expanded our conception of the
Amendment to protect certain expectations of privacy as
well. When an individual “seeks to preserve something as
private,” and his expectation of privacy is “one that society
is prepared to recognize as reasonable,” we have held that
official intrusion into that private sphere generally quali-
fies as a search and requires a warrant supported by
probable cause. Smith, 442 U. S., at 740 (internal quota-
tion marks and alterations omitted).
   Although no single rubric definitively resolves which
expectations of privacy are entitled to protection,1 the
——————
  1 JUSTICE KENNEDY believes that there is such a rubric—the “proper-

ty-based concepts” that Katz purported to move beyond. Post, at 3
(dissenting opinion). But while property rights are often informative,
our cases by no means suggest that such an interest is “fundamental”
or “dispositive” in determining which expectations of privacy are
legitimate. Post, at 8–9. JUSTICE THOMAS (and to a large extent
JUSTICE GORSUCH) would have us abandon Katz and return to an
6                 CARPENTER v. UNITED STATES

                          Opinion of the Court

analysis is informed by historical understandings “of what
was deemed an unreasonable search and seizure when
[the Fourth Amendment] was adopted.” Carroll v. United
States, 267 U. S. 132, 149 (1925). On this score, our cases
have recognized some basic guideposts. First, that the
Amendment seeks to secure “the privacies of life” against
“arbitrary power.” Boyd v. United States, 116 U. S. 616,
630 (1886). Second, and relatedly, that a central aim of
the Framers was “to place obstacles in the way of a too
permeating police surveillance.” United States v. Di Re,
332 U. S. 581, 595 (1948).
  We have kept this attention to Founding-era under-
standings in mind when applying the Fourth Amendment
to innovations in surveillance tools. As technology has
enhanced the Government’s capacity to encroach upon
areas normally guarded from inquisitive eyes, this Court
has sought to “assure[ ] preservation of that degree of
privacy against government that existed when the Fourth
Amendment was adopted.” Kyllo v. United States, 533
U. S. 27, 34 (2001). For that reason, we rejected in Kyllo a
“mechanical interpretation” of the Fourth Amendment and
held that use of a thermal imager to detect heat radiating
from the side of the defendant’s home was a search. Id., at
35. Because any other conclusion would leave homeown-
ers “at the mercy of advancing technology,” we determined
that the Government—absent a warrant—could not capi-
talize on such new sense-enhancing technology to explore
——————
exclusively property-based approach. Post, at 1–2, 17–21 (THOMAS J.,
dissenting); post, at 6–9 (GORSUCH, J., dissenting). Katz of course
“discredited” the “premise that property interests control,” 389 U. S., at
353, and we have repeatedly emphasized that privacy interests do not
rise or fall with property rights, see, e.g., United States v. Jones, 565
U. S. 400, 411 (2012) (refusing to “make trespass the exclusive test”);
Kyllo v. United States, 533 U. S. 27, 32 (2001) (“We have since decou-
pled violation of a person’s Fourth Amendment rights from trespassory
violation of his property.”). Neither party has asked the Court to
reconsider Katz in this case.
                  Cite as: 585 U. S. ____ (2018)              7

                      Opinion of the Court

what was happening within the home. Ibid.
  Likewise in Riley, the Court recognized the “immense
storage capacity” of modern cell phones in holding that
police officers must generally obtain a warrant before
searching the contents of a phone. 573 U. S., at ___ (slip
op., at 17). We explained that while the general rule
allowing warrantless searches incident to arrest “strikes
the appropriate balance in the context of physical objects,
neither of its rationales has much force with respect to”
the vast store of sensitive information on a cell phone. Id.,
at ___ (slip op., at 9).
                                B
   The case before us involves the Government’s acquisi-
tion of wireless carrier cell-site records revealing the
location of Carpenter’s cell phone whenever it made or
received calls. This sort of digital data—personal location
information maintained by a third party—does not fit
neatly under existing precedents. Instead, requests for
cell-site records lie at the intersection of two lines of cases,
both of which inform our understanding of the privacy
interests at stake.
   The first set of cases addresses a person’s expectation of
privacy in his physical location and movements. In United
States v. Knotts, 460 U. S. 276 (1983), we considered the
Government’s use of a “beeper” to aid in tracking a vehicle
through traffic. Police officers in that case planted a
beeper in a container of chloroform before it was pur-
chased by one of Knotts’s co-conspirators. The officers
(with intermittent aerial assistance) then followed the
automobile carrying the container from Minneapolis to
Knotts’s cabin in Wisconsin, relying on the beeper’s signal
to help keep the vehicle in view. The Court concluded that
the “augment[ed]” visual surveillance did not constitute a
search because “[a] person traveling in an automobile on
public thoroughfares has no reasonable expectation of
8              CARPENTER v. UNITED STATES

                     Opinion of the Court

privacy in his movements from one place to another.” Id.,
at 281, 282. Since the movements of the vehicle and its
final destination had been “voluntarily conveyed to anyone
who wanted to look,” Knotts could not assert a privacy
interest in the information obtained. Id., at 281.
   This Court in Knotts, however, was careful to distin-
guish between the rudimentary tracking facilitated by the
beeper and more sweeping modes of surveillance. The
Court emphasized the “limited use which the government
made of the signals from this particular beeper” during a
discrete “automotive journey.” Id., at 284, 285. Signifi-
cantly, the Court reserved the question whether “different
constitutional principles may be applicable” if “twenty-four
hour surveillance of any citizen of this country [were]
possible.” Id., at 283–284.
   Three decades later, the Court considered more sophis-
ticated surveillance of the sort envisioned in Knotts and
found that different principles did indeed apply. In United
States v. Jones, FBI agents installed a GPS tracking de-
vice on Jones’s vehicle and remotely monitored the vehi-
cle’s movements for 28 days. The Court decided the case
based on the Government’s physical trespass of the vehi-
cle. 565 U. S., at 404–405. At the same time, five Justices
agreed that related privacy concerns would be raised by,
for example, “surreptitiously activating a stolen vehicle
detection system” in Jones’s car to track Jones himself, or
conducting GPS tracking of his cell phone. Id., at 426, 428
(ALITO, J., concurring in judgment); id., at 415
(SOTOMAYOR, J., concurring). Since GPS monitoring of a
vehicle tracks “every movement” a person makes in that
vehicle, the concurring Justices concluded that “longer
term GPS monitoring in investigations of most offenses
impinges on expectations of privacy”—regardless whether
those movements were disclosed to the public at large.
Id., at 430 (opinion of ALITO, J.); id., at 415 (opinion of
                      Cite as: 585 U. S. ____ (2018)                      9

                           Opinion of the Court

SOTOMAYOR, J.).2
  In a second set of decisions, the Court has drawn a line
between what a person keeps to himself and what he
shares with others. We have previously held that “a per-
son has no legitimate expectation of privacy in information
he voluntarily turns over to third parties.” Smith, 442
U. S., at 743–744. That remains true “even if the infor-
mation is revealed on the assumption that it will be used
only for a limited purpose.” United States v. Miller, 425
U. S. 435, 443 (1976). As a result, the Government is
typically free to obtain such information from the recipient
without triggering Fourth Amendment protections.
  This third-party doctrine largely traces its roots to
Miller. While investigating Miller for tax evasion, the
Government subpoenaed his banks, seeking several
months of canceled checks, deposit slips, and monthly
statements. The Court rejected a Fourth Amendment
challenge to the records collection. For one, Miller could
“assert neither ownership nor possession” of the docu-
ments; they were “business records of the banks.” Id., at
440. For another, the nature of those records confirmed
Miller’s limited expectation of privacy, because the checks
were “not confidential communications but negotiable
instruments to be used in commercial transactions,” and
the bank statements contained information “exposed to
——————
  2 JUSTICE KENNEDY argues that this case is in a different category

from Jones and the dragnet-type practices posited in Knotts because the
disclosure of the cell-site records was subject to “judicial authorization.”
Post, at 14–16. That line of argument conflates the threshold question
whether a “search” has occurred with the separate matter of whether
the search was reasonable. The subpoena process set forth in the
Stored Communications Act does not determine a target’s expectation
of privacy. And in any event, neither Jones nor Knotts purported to
resolve the question of what authorization may be required to conduct
such electronic surveillance techniques. But see Jones, 565 U. S., at
430 (ALITO, J., concurring in judgment) (indicating that longer term
GPS tracking may require a warrant).
10             CARPENTER v. UNITED STATES

                     Opinion of the Court

[bank] employees in the ordinary course of business.” Id.,
at 442. The Court thus concluded that Miller had “take[n]
the risk, in revealing his affairs to another, that the in-
formation [would] be conveyed by that person to the Gov-
ernment.” Id., at 443.
  Three years later, Smith applied the same principles in
the context of information conveyed to a telephone com-
pany. The Court ruled that the Government’s use of a pen
register—a device that recorded the outgoing phone num-
bers dialed on a landline telephone—was not a search.
Noting the pen register’s “limited capabilities,” the Court
“doubt[ed] that people in general entertain any actual
expectation of privacy in the numbers they dial.” 442
U. S., at 742. Telephone subscribers know, after all, that
the numbers are used by the telephone company “for a
variety of legitimate business purposes,” including routing
calls. Id., at 743. And at any rate, the Court explained,
such an expectation “is not one that society is prepared to
recognize as reasonable.” Ibid. (internal quotation marks
omitted). When Smith placed a call, he “voluntarily con-
veyed” the dialed numbers to the phone company by “ex-
pos[ing] that information to its equipment in the ordinary
course of business.” Id., at 744 (internal quotation marks
omitted). Once again, we held that the defendant “as-
sumed the risk” that the company’s records “would be
divulged to police.” Id., at 745.
                            III
  The question we confront today is how to apply the
Fourth Amendment to a new phenomenon: the ability to
chronicle a person’s past movements through the record of
his cell phone signals. Such tracking partakes of many of
the qualities of the GPS monitoring we considered in
Jones. Much like GPS tracking of a vehicle, cell phone
location information is detailed, encyclopedic, and effort-
lessly compiled.
                     Cite as: 585 U. S. ____ (2018)                    11

                          Opinion of the Court

   At the same time, the fact that the individual continu-
ously reveals his location to his wireless carrier implicates
the third-party principle of Smith and Miller. But while
the third-party doctrine applies to telephone numbers and
bank records, it is not clear whether its logic extends to
the qualitatively different category of cell-site records.
After all, when Smith was decided in 1979, few could have
imagined a society in which a phone goes wherever its
owner goes, conveying to the wireless carrier not just
dialed digits, but a detailed and comprehensive record of
the person’s movements.
   We decline to extend Smith and Miller to cover these
novel circumstances. Given the unique nature of cell
phone location records, the fact that the information is
held by a third party does not by itself overcome the user’s
claim to Fourth Amendment protection. Whether the
Government employs its own surveillance technology as in
Jones or leverages the technology of a wireless carrier, we
hold that an individual maintains a legitimate expectation
of privacy in the record of his physical movements as
captured through CSLI. The location information ob-
tained from Carpenter’s wireless carriers was the product
of a search.3

——————
  3 The parties suggest as an alternative to their primary submissions

that the acquisition of CSLI becomes a search only if it extends beyond
a limited period. See Reply Brief 12 (proposing a 24-hour cutoff); Brief
for United States 55–56 (suggesting a seven-day cutoff). As part of its
argument, the Government treats the seven days of CSLI requested
from Sprint as the pertinent period, even though Sprint produced only
two days of records. Brief for United States 56. Contrary to JUSTICE
KENNEDY’s assertion, post, at 19, we need not decide whether there is a
limited period for which the Government may obtain an individual’s
historical CSLI free from Fourth Amendment scrutiny, and if so, how
long that period might be. It is sufficient for our purposes today to hold
that accessing seven days of CSLI constitutes a Fourth Amendment
search.
12             CARPENTER v. UNITED STATES

                     Opinion of the Court

                              A
   A person does not surrender all Fourth Amendment
protection by venturing into the public sphere. To the
contrary, “what [one] seeks to preserve as private, even in
an area accessible to the public, may be constitutionally
protected.” Katz, 389 U. S., at 351–352. A majority of this
Court has already recognized that individuals have a
reasonable expectation of privacy in the whole of their
physical movements. Jones, 565 U. S., at 430 (ALITO, J.,
concurring in judgment); id., at 415 (SOTOMAYOR, J.,
concurring). Prior to the digital age, law enforcement
might have pursued a suspect for a brief stretch, but doing
so “for any extended period of time was difficult and costly
and therefore rarely undertaken.” Id., at 429 (opinion of
ALITO, J.). For that reason, “society’s expectation has
been that law enforcement agents and others would not—
and indeed, in the main, simply could not—secretly moni-
tor and catalogue every single movement of an individual’s
car for a very long period.” Id., at 430.
   Allowing government access to cell-site records contra-
venes that expectation. Although such records are gener-
ated for commercial purposes, that distinction does not
negate Carpenter’s anticipation of privacy in his physical
location. Mapping a cell phone’s location over the course
of 127 days provides an all-encompassing record of the
holder’s whereabouts. As with GPS information, the time-
stamped data provides an intimate window into a person’s
life, revealing not only his particular movements, but
through them his “familial, political, professional, reli-
gious, and sexual associations.” Id., at 415 (opinion of
SOTOMAYOR, J.). These location records “hold for many
Americans the ‘privacies of life.’ ” Riley, 573 U. S., at ___
(slip op., at 28) (quoting Boyd, 116 U. S., at 630). And like
GPS monitoring, cell phone tracking is remarkably easy,
cheap, and efficient compared to traditional investigative
tools. With just the click of a button, the Government can
                  Cite as: 585 U. S. ____ (2018)            13

                      Opinion of the Court

access each carrier’s deep repository of historical location
information at practically no expense.
   In fact, historical cell-site records present even greater
privacy concerns than the GPS monitoring of a vehicle we
considered in Jones. Unlike the bugged container in
Knotts or the car in Jones, a cell phone—almost a “feature
of human anatomy,” Riley, 573 U. S., at ___ (slip op., at
9)—tracks nearly exactly the movements of its owner.
While individuals regularly leave their vehicles, they
compulsively carry cell phones with them all the time. A
cell phone faithfully follows its owner beyond public thor-
oughfares and into private residences, doctor’s offices,
political headquarters, and other potentially revealing
locales. See id., at ___ (slip op., at 19) (noting that “nearly
three-quarters of smart phone users report being within
five feet of their phones most of the time, with 12% admit-
ting that they even use their phones in the shower”);
contrast Cardwell v. Lewis, 417 U. S. 583, 590 (1974)
(plurality opinion) (“A car has little capacity for escaping
public scrutiny.”). Accordingly, when the Government
tracks the location of a cell phone it achieves near perfect
surveillance, as if it had attached an ankle monitor to the
phone’s user.
   Moreover, the retrospective quality of the data here
gives police access to a category of information otherwise
unknowable. In the past, attempts to reconstruct a per-
son’s movements were limited by a dearth of records and
the frailties of recollection. With access to CSLI, the
Government can now travel back in time to retrace a
person’s whereabouts, subject only to the retention polices
of the wireless carriers, which currently maintain records
for up to five years. Critically, because location infor-
mation is continually logged for all of the 400 million
devices in the United States—not just those belonging to
persons who might happen to come under investigation—
this newfound tracking capacity runs against everyone.
14             CARPENTER v. UNITED STATES

                     Opinion of the Court

Unlike with the GPS device in Jones, police need not even
know in advance whether they want to follow a particular
individual, or when.
   Whoever the suspect turns out to be, he has effectively
been tailed every moment of every day for five years, and
the police may—in the Government’s view—call upon the
results of that surveillance without regard to the con-
straints of the Fourth Amendment. Only the few with-
out cell phones could escape this tireless and absolute
surveillance.
   The Government and JUSTICE KENNEDY contend, how-
ever, that the collection of CSLI should be permitted
because the data is less precise than GPS information.
Not to worry, they maintain, because the location records
did “not on their own suffice to place [Carpenter] at the
crime scene”; they placed him within a wedge-shaped
sector ranging from one-eighth to four square miles. Brief
for United States 24; see post, at 18–19. Yet the Court has
already rejected the proposition that “inference insulates a
search.” Kyllo, 533 U. S., at 36. From the 127 days of
location data it received, the Government could, in combi-
nation with other information, deduce a detailed log of
Carpenter’s movements, including when he was at the site
of the robberies. And the Government thought the CSLI
accurate enough to highlight it during the closing argu-
ment of his trial. App. 131.
   At any rate, the rule the Court adopts “must take ac-
count of more sophisticated systems that are already in
use or in development.” Kyllo, 533 U. S., at 36. While the
records in this case reflect the state of technology at the
start of the decade, the accuracy of CSLI is rapidly ap-
proaching GPS-level precision. As the number of cell sites
has proliferated, the geographic area covered by each cell
sector has shrunk, particularly in urban areas. In addi-
tion, with new technology measuring the time and angle of
signals hitting their towers, wireless carriers already have
                 Cite as: 585 U. S. ____ (2018)           15

                     Opinion of the Court

the capability to pinpoint a phone’s location within 50
meters. Brief for Electronic Frontier Foundation et al. as
Amici Curiae 12 (describing triangulation methods that
estimate a device’s location inside a given cell sector).
  Accordingly, when the Government accessed CSLI from
the wireless carriers, it invaded Carpenter’s reason-
able expectation of privacy in the whole of his physical
movements.
                              B
  The Government’s primary contention to the contrary is
that the third-party doctrine governs this case. In its
view, cell-site records are fair game because they are
“business records” created and maintained by the wireless
carriers. The Government (along with JUSTICE KENNEDY)
recognizes that this case features new technology, but
asserts that the legal question nonetheless turns on a
garden-variety request for information from a third-party
witness. Brief for United States 32–34; post, at 12–14.
  The Government’s position fails to contend with the
seismic shifts in digital technology that made possible the
tracking of not only Carpenter’s location but also everyone
else’s, not for a short period but for years and years.
Sprint Corporation and its competitors are not your typi-
cal witnesses. Unlike the nosy neighbor who keeps an eye
on comings and goings, they are ever alert, and their
memory is nearly infallible. There is a world of difference
between the limited types of personal information ad-
dressed in Smith and Miller and the exhaustive chronicle
of location information casually collected by wireless
carriers today. The Government thus is not asking for a
straightforward application of the third-party doctrine,
but instead a significant extension of it to a distinct cate-
gory of information.
  The third-party doctrine partly stems from the notion
that an individual has a reduced expectation of privacy in
16             CARPENTER v. UNITED STATES

                      Opinion of the Court

information knowingly shared with another. But the fact
of “diminished privacy interests does not mean that the
Fourth Amendment falls out of the picture entirely.”
Riley, 573 U. S., at ___ (slip op., at 16). Smith and Miller,
after all, did not rely solely on the act of sharing. Instead,
they considered “the nature of the particular documents
sought” to determine whether “there is a legitimate ‘expec-
tation of privacy’ concerning their contents.” Miller, 425
U. S., at 442. Smith pointed out the limited capabilities of
a pen register; as explained in Riley, telephone call logs
reveal little in the way of “identifying information.”
Smith, 442 U. S., at 742; Riley, 573 U. S., at ___ (slip op.,
at 24). Miller likewise noted that checks were “not confi-
dential communications but negotiable instruments to be
used in commercial transactions.” 425 U. S., at 442. In
mechanically applying the third-party doctrine to this
case, the Government fails to appreciate that there are no
comparable limitations on the revealing nature of CSLI.
  The Court has in fact already shown special solicitude
for location information in the third-party context. In
Knotts, the Court relied on Smith to hold that an individ-
ual has no reasonable expectation of privacy in public
movements that he “voluntarily conveyed to anyone who
wanted to look.” Knotts, 460 U. S., at 281; see id., at 283
(discussing Smith). But when confronted with more per-
vasive tracking, five Justices agreed that longer term GPS
monitoring of even a vehicle traveling on public streets
constitutes a search. Jones, 565 U. S., at 430 (ALITO, J.,
concurring in judgment); id., at 415 (SOTOMAYOR, J.,
concurring). JUSTICE GORSUCH wonders why “someone’s
location when using a phone” is sensitive, post, at 3, and
JUSTICE KENNEDY assumes that a person’s discrete
movements “are not particularly private,” post, at 17. Yet
this case is not about “using a phone” or a person’s move-
ment at a particular time. It is about a detailed chronicle
of a person’s physical presence compiled every day, every
                 Cite as: 585 U. S. ____ (2018)           17

                     Opinion of the Court

moment, over several years. Such a chronicle implicates
privacy concerns far beyond those considered in Smith and
Miller.
  Neither does the second rationale underlying the third-
party doctrine—voluntary exposure—hold up when it
comes to CSLI. Cell phone location information is not
truly “shared” as one normally understands the term. In
the first place, cell phones and the services they provide
are “such a pervasive and insistent part of daily life” that
carrying one is indispensable to participation in modern
society. Riley, 573 U. S., at ___ (slip op., at 9). Second, a
cell phone logs a cell-site record by dint of its operation,
without any affirmative act on the part of the user beyond
powering up. Virtually any activity on the phone gener-
ates CSLI, including incoming calls, texts, or e-mails and
countless other data connections that a phone automati-
cally makes when checking for news, weather, or social
media updates. Apart from disconnecting the phone from
the network, there is no way to avoid leaving behind a
trail of location data. As a result, in no meaningful sense
does the user voluntarily “assume[ ] the risk” of turning
over a comprehensive dossier of his physical movements.
Smith, 442 U. S., at 745.
  We therefore decline to extend Smith and Miller to the
collection of CSLI. Given the unique nature of cell phone
location information, the fact that the Government ob-
tained the information from a third party does not over-
come Carpenter’s claim to Fourth Amendment protection.
The Government’s acquisition of the cell-site records was a
search within the meaning of the Fourth Amendment.
                       *     *    *
  Our decision today is a narrow one. We do not express a
view on matters not before us: real-time CSLI or “tower
dumps” (a download of information on all the devices that
connected to a particular cell site during a particular
18                CARPENTER v. UNITED STATES

                         Opinion of the Court

interval). We do not disturb the application of Smith and
Miller or call into question conventional surveillance
techniques and tools, such as security cameras. Nor do we
address other business records that might incidentally
reveal location information. Further, our opinion does not
consider other collection techniques involving foreign
affairs or national security. As Justice Frankfurter noted
when considering new innovations in airplanes and radios,
the Court must tread carefully in such cases, to ensure
that we do not “embarrass the future.” Northwest Air-
lines, Inc. v. Minnesota, 322 U. S. 292, 300 (1944).4
                               IV
   Having found that the acquisition of Carpenter’s CSLI
was a search, we also conclude that the Government must
generally obtain a warrant supported by probable cause
before acquiring such records. Although the “ultimate
measure of the constitutionality of a governmental search
is ‘reasonableness,’ ” our cases establish that warrantless
searches are typically unreasonable where “a search is
undertaken by law enforcement officials to discover evi-
dence of criminal wrongdoing.” Vernonia School Dist. 47J
v. Acton, 515 U. S. 646, 652–653 (1995). Thus, “[i]n the
absence of a warrant, a search is reasonable only if it falls
within a specific exception to the warrant requirement.”
Riley, 573 U. S., at ___ (slip op., at 5).
   The Government acquired the cell-site records pursuant
to a court order issued under the Stored Communications
Act, which required the Government to show “reasonable
grounds” for believing that the records were “relevant and
——————
  4 JUSTICE GORSUCH faults us for not promulgating a complete code

addressing the manifold situations that may be presented by this new
technology—under a constitutional provision turning on what is “rea-
sonable,” no less. Post, at 10–12. Like JUSTICE GORSUCH, we “do not
begin to claim all the answers today,” post, at 13, and therefore decide
no more than the case before us.
                 Cite as: 585 U. S. ____ (2018)          19

                     Opinion of the Court

material to an ongoing investigation.”          18 U. S. C.
§2703(d). That showing falls well short of the probable
cause required for a warrant. The Court usually requires
“some quantum of individualized suspicion” before
a search or seizure may take place. United States v.
Martinez-Fuerte, 428 U. S. 543, 560–561 (1976). Under the
standard in the Stored Communications Act, however, law
enforcement need only show that the cell-site evidence
might be pertinent to an ongoing investigation—a “gigan-
tic” departure from the probable cause rule, as the Gov-
ernment explained below. App. 34. Consequently, an
order issued under Section 2703(d) of the Act is not a
permissible mechanism for accessing historical cell-site
records. Before compelling a wireless carrier to turn over
a subscriber’s CSLI, the Government’s obligation is a
familiar one—get a warrant.
   JUSTICE ALITO contends that the warrant requirement
simply does not apply when the Government acquires
records using compulsory process. Unlike an actual
search, he says, subpoenas for documents do not involve
the direct taking of evidence; they are at most a “construc-
tive search” conducted by the target of the subpoena. Post,
at 12. Given this lesser intrusion on personal privacy,
JUSTICE ALITO argues that the compulsory production of
records is not held to the same probable cause standard.
In his view, this Court’s precedents set forth a categorical
rule—separate and distinct from the third-party doc-
trine—subjecting subpoenas to lenient scrutiny without
regard to the suspect’s expectation of privacy in the rec-
ords. Post, at 8–19.
   But this Court has never held that the Government may
subpoena third parties for records in which the suspect
has a reasonable expectation of privacy. Almost all of the
examples JUSTICE ALITO cites, see post, at 14–15, contem-
plated requests for evidence implicating diminished pri-
20                CARPENTER v. UNITED STATES

                          Opinion of the Court

vacy interests or for a corporation’s own books.5 The lone
exception, of course, is Miller, where the Court’s analysis
of the third-party subpoena merged with the application of
the third-party doctrine. 425 U. S., at 444 (concluding
that Miller lacked the necessary privacy interest to contest
the issuance of a subpoena to his bank).
   JUSTICE ALITO overlooks the critical issue. At some
point, the dissent should recognize that CSLI is an entirely
different species of business record—something that
implicates basic Fourth Amendment concerns about arbi-
trary government power much more directly than corpo-
rate tax or payroll ledgers. When confronting new con-
cerns wrought by digital technology, this Court has been
careful not to uncritically extend existing precedents. See
Riley, 573 U. S., at ___ (slip op., at 10) (“A search of
the information on a cell phone bears little resemblance
to the type of brief physical search considered [in prior
precedents].”).
   If the choice to proceed by subpoena provided a categori-
cal limitation on Fourth Amendment protection, no type of
record would ever be protected by the warrant require-
ment. Under JUSTICE ALITO’s view, private letters, digital
contents of a cell phone—any personal information re-
duced to document form, in fact—may be collected by
——————
  5 See United States v. Dionisio, 410 U. S. 1, 14 (1973) (“No person can

have a reasonable expectation that others will not know the sound of
his voice”); Donovan v. Lone Steer, Inc., 464 U. S. 408, 411, 415 (1984)
(payroll and sales records); California Bankers Assn. v. Shultz, 416
U. S. 21, 67 (1974) (Bank Secrecy Act reporting requirements); See v.
Seattle, 387 U. S. 541, 544 (1967) (financial books and records); United
States v. Powell, 379 U. S. 48, 49, 57 (1964) (corporate tax records);
McPhaul v. United States, 364 U. S. 372, 374, 382 (1960) (books and
records of an organization); United States v. Morton Salt Co., 338 U. S.
632, 634, 651–653 (1950) (Federal Trade Commission reporting re-
quirement); Oklahoma Press Publishing Co. v. Walling, 327 U. S. 186,
189, 204–208 (1946) (payroll records); Hale v. Henkel, 201 U. S. 43, 45,
75 (1906) (corporate books and papers).
                  Cite as: 585 U. S. ____ (2018)            21

                      Opinion of the Court

subpoena for no reason other than “official curiosity.”
United States v. Morton Salt Co., 338 U. S. 632, 652
(1950). JUSTICE KENNEDY declines to adopt the radical
implications of this theory, leaving open the question
whether the warrant requirement applies “when the Gov-
ernment obtains the modern-day equivalents of an indi-
vidual’s own ‘papers’ or ‘effects,’ even when those papers
or effects are held by a third party. ” Post, at 13 (citing
United States v. Warshak, 631 F. 3d 266, 283–288 (CA6
2010)). That would be a sensible exception, because it
would prevent the subpoena doctrine from overcoming any
reasonable expectation of privacy. If the third-party doc-
trine does not apply to the “modern-day equivalents of an
individual’s own ‘papers’ or ‘effects,’ ” then the clear impli-
cation is that the documents should receive full Fourth
Amendment protection. We simply think that such pro-
tection should extend as well to a detailed log of a person’s
movements over several years.
   This is certainly not to say that all orders compelling the
production of documents will require a showing of proba-
ble cause. The Government will be able to use subpoenas
to acquire records in the overwhelming majority of inves-
tigations. We hold only that a warrant is required in the
rare case where the suspect has a legitimate privacy in-
terest in records held by a third party.
   Further, even though the Government will generally
need a warrant to access CSLI, case-specific exceptions
may support a warrantless search of an individual’s cell-
site records under certain circumstances. “One well-
recognized exception applies when ‘ “the exigencies of the
situation” make the needs of law enforcement so compel-
ling that [a] warrantless search is objectively reasonable
under the Fourth Amendment.’ ” Kentucky v. King, 563
U. S. 452, 460 (2011) (quoting Mincey v. Arizona, 437 U. S.
385, 394 (1978)). Such exigencies include the need to
pursue a fleeing suspect, protect individuals who are
22             CARPENTER v. UNITED STATES

                     Opinion of the Court

threatened with imminent harm, or prevent the imminent
destruction of evidence. 563 U. S., at 460, and n. 3.
  As a result, if law enforcement is confronted with an
urgent situation, such fact-specific threats will likely
justify the warrantless collection of CSLI. Lower courts,
for instance, have approved warrantless searches related
to bomb threats, active shootings, and child abductions.
Our decision today does not call into doubt warrantless
access to CSLI in such circumstances. While police must
get a warrant when collecting CSLI to assist in the mine-
run criminal investigation, the rule we set forth does not
limit their ability to respond to an ongoing emergency.
                        *      *   *
   As Justice Brandeis explained in his famous dissent, the
Court is obligated—as “[s]ubtler and more far-reaching
means of invading privacy have become available to the
Government”—to ensure that the “progress of science”
does not erode Fourth Amendment protections. Olmstead
v. United States, 277 U. S. 438, 473–474 (1928). Here the
progress of science has afforded law enforcement a power-
ful new tool to carry out its important responsibilities. At
the same time, this tool risks Government encroachment
of the sort the Framers, “after consulting the lessons of
history,” drafted the Fourth Amendment to prevent. Di
Re, 332 U. S., at 595.
   We decline to grant the state unrestricted access to a
wireless carrier’s database of physical location infor-
mation. In light of the deeply revealing nature of CSLI,
its depth, breadth, and comprehensive reach, and the
inescapable and automatic nature of its collection, the fact
that such information is gathered by a third party does not
make it any less deserving of Fourth Amendment protec-
tion. The Government’s acquisition of the cell-site records
here was a search under that Amendment.
   The judgment of the Court of Appeals is reversed, and
                Cite as: 585 U. S. ____ (2018)         23

                    Opinion of the Court

the case is remanded for further proceedings consistent
with this opinion.
                                        It is so ordered.
                 Cite as: 585 U. S. ____ (2018)          1

                   KENNEDY, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 16–402
                         _________________


   TIMOTHY IVORY CARPENTER, PETITIONER v.

              UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [June 22, 2018] 


  JUSTICE KENNEDY, with whom JUSTICE THOMAS and
JUSTICE ALITO join, dissenting.
  This case involves new technology, but the Court’s stark
departure from relevant Fourth Amendment precedents
and principles is, in my submission, unnecessary and
incorrect, requiring this respectful dissent.
  The new rule the Court seems to formulate puts needed,
reasonable, accepted, lawful, and congressionally author-
ized criminal investigations at serious risk in serious
cases, often when law enforcement seeks to prevent the
threat of violent crimes. And it places undue restrictions
on the lawful and necessary enforcement powers exercised
not only by the Federal Government, but also by law
enforcement in every State and locality throughout the
Nation. Adherence to this Court’s longstanding prece-
dents and analytic framework would have been the proper
and prudent way to resolve this case.
  The Court has twice held that individuals have no
Fourth Amendment interests in business records which
are possessed, owned, and controlled by a third party.
United States v. Miller, 425 U. S. 435 (1976); Smith v.
Maryland, 442 U. S. 735 (1979). This is true even when
the records contain personal and sensitive information. So
when the Government uses a subpoena to obtain, for
example, bank records, telephone records, and credit card
2              CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

statements from the businesses that create and keep these
records, the Government does not engage in a search of
the business’s customers within the meaning of the Fourth
Amendment.
   In this case petitioner challenges the Government’s
right to use compulsory process to obtain a now-common
kind of business record: cell-site records held by cell phone
service providers. The Government acquired the records
through an investigative process enacted by Congress.
Upon approval by a neutral magistrate, and based on the
Government’s duty to show reasonable necessity, it au-
thorizes the disclosure of records and information that are
under the control and ownership of the cell phone service
provider, not its customer. Petitioner acknowledges that
the Government may obtain a wide variety of business
records using compulsory process, and he does not ask the
Court to revisit its precedents. Yet he argues that, under
those same precedents, the Government searched his
records when it used court-approved compulsory process to
obtain the cell-site information at issue here.
   Cell-site records, however, are no different from the
many other kinds of business records the Government has
a lawful right to obtain by compulsory process. Customers
like petitioner do not own, possess, control, or use the
records, and for that reason have no reasonable expecta-
tion that they cannot be disclosed pursuant to lawful
compulsory process.
   The Court today disagrees. It holds for the first time
that by using compulsory process to obtain records of a
business entity, the Government has not just engaged in
an impermissible action, but has conducted a search of the
business’s customer. The Court further concludes that the
search in this case was unreasonable and the Government
needed to get a warrant to obtain more than six days of
cell-site records.
   In concluding that the Government engaged in a search,
                 Cite as: 585 U. S. ____ (2018)            3

                    KENNEDY, J., dissenting

the Court unhinges Fourth Amendment doctrine from the
property-based concepts that have long grounded the
analytic framework that pertains in these cases. In doing
so it draws an unprincipled and unworkable line between
cell-site records on the one hand and financial and tele-
phonic records on the other. According to today’s majority
opinion, the Government can acquire a record of every
credit card purchase and phone call a person makes over
months or years without upsetting a legitimate expecta-
tion of privacy. But, in the Court’s view, the Government
crosses a constitutional line when it obtains a court’s
approval to issue a subpoena for more than six days of
cell-site records in order to determine whether a person
was within several hundred city blocks of a crime scene.
That distinction is illogical and will frustrate principled
application of the Fourth Amendment in many routine yet
vital law enforcement operations.
   It is true that the Cyber Age has vast potential both to
expand and restrict individual freedoms in dimensions not
contemplated in earlier times. See Packingham v. North
Carolina, 582 U. S. ___, ___–___ (2017) (slip op., at 46).
For the reasons that follow, however, there is simply no
basis here for concluding that the Government interfered
with information that the cell phone customer, either from
a legal or commonsense standpoint, should have thought
the law would deem owned or controlled by him.
                              I
  Before evaluating the question presented it is helpful to
understand the nature of cell-site records, how they are
commonly used by cell phone service providers, and their
proper use by law enforcement.
  When a cell phone user makes a call, sends a text mes-
sage or e-mail, or gains access to the Internet, the cell
phone establishes a radio connection to an antenna at a
nearby cell site. The typical cell site covers a more-or-less
4               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

circular geographic area around the site. It has three (or
sometimes six) separate antennas pointing in different
directions. Each provides cell service for a different 120-
degree (or 60-degree) sector of the cell site’s circular cover-
age area. So a cell phone activated on the north side of a
cell site will connect to a different antenna than a cell
phone on the south side.
   Cell phone service providers create records each time a
cell phone connects to an antenna at a cell site. For a
phone call, for example, the provider records the date,
time, and duration of the call; the phone numbers making
and receiving the call; and, most relevant here, the cell
site used to make the call, as well as the specific antenna
that made the connection. The cell-site and antenna data
points, together with the date and time of connection, are
known as cell-site location information, or cell-site records.
By linking an individual’s cell phone to a particular 120-
or 60-degree sector of a cell site’s coverage area at a par-
ticular time, cell-site records reveal the general location of
the cell phone user.
   The location information revealed by cell-site records is
imprecise, because an individual cell-site sector usually
covers a large geographic area. The FBI agent who offered
expert testimony about the cell-site records at issue here
testified that a cell site in a city reaches between a half
mile and two miles in all directions. That means a 60-
degree sector covers between approximately one-eighth
and two square miles (and a 120-degree sector twice that
area). To put that in perspective, in urban areas cell-site
records often would reveal the location of a cell phone user
within an area covering between around a dozen and
several hundred city blocks. In rural areas cell-site rec-
ords can be up to 40 times more imprecise. By contrast, a
Global Positioning System (GPS) can reveal an individ-
ual’s location within around 15 feet.
   Major cell phone service providers keep cell-site records
                 Cite as: 585 U. S. ____ (2018)            5

                    KENNEDY, J., dissenting

for long periods of time. There is no law requiring them to
do so. Instead, providers contract with their customers to
collect and keep these records because they are valuable to
the providers. Among other things, providers aggregate
the records and sell them to third parties along with other
information gleaned from cell phone usage. This data can
be used, for example, to help a department store deter-
mine which of various prospective store locations is likely
to get more foot traffic from middle-aged women who live
in affluent zip codes. The market for cell phone data is
now estimated to be in the billions of dollars. See Brief for
Technology Experts as Amici Curiae 23.
   Cell-site records also can serve an important investiga-
tive function, as the facts of this case demonstrate. Peti-
tioner, Timothy Carpenter, along with a rotating group of
accomplices, robbed at least six RadioShack and T-Mobile
stores at gunpoint over a 2-year period. Five of those
robberies occurred in the Detroit area, each crime at least
four miles from the last. The sixth took place in Warren,
Ohio, over 200 miles from Detroit.
   The Government, of course, did not know all of these
details in 2011 when it began investigating Carpenter. In
April of that year police arrested four of Carpenter’s co-
conspirators. One of them confessed to committing nine
robberies in Michigan and Ohio between December 2010
and March 2011. He identified 15 accomplices who had
participated in at least one of those robberies; named
Carpenter as one of the accomplices; and provided Carpen-
ter’s cell phone number to the authorities. The suspect
also warned that the other members of the conspiracy
planned to commit more armed robberies in the immediate
future.
   The Government at this point faced a daunting task.
Even if it could identify and apprehend the suspects, still
it had to link each suspect in this changing criminal gang
to specific robberies in order to bring charges and convict.
6               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

And, of course, it was urgent that the Government take all
necessary steps to stop the ongoing and dangerous crime
spree.
   Cell-site records were uniquely suited to this task. The
geographic dispersion of the robberies meant that, if Car-
penter’s cell phone were within even a dozen to several
hundred city blocks of one or more of the stores when the
different robberies occurred, there would be powerful
circumstantial evidence of his participation; and this
would be especially so if his cell phone usually was not
located in the sectors near the stores except during the
robbery times.
   To obtain these records, the Government applied to
federal magistrate judges for disclosure orders pursuant to
§2703(d) of the Stored Communications Act. That Act
authorizes a magistrate judge to issue an order requiring
disclosure of cell-site records if the Government demon-
strates “specific and articulable facts showing that there
are reasonable grounds to believe” the records “are rele-
vant and material to an ongoing criminal investigation.”
18 U. S. C. §§2703(d), 2711(3). The full statutory provi-
sion is set out in the Appendix, infra.
   From Carpenter’s primary service provider, MetroPCS,
the Government obtained records from between December
2010 and April 2011, based on its understanding that nine
robberies had occurred in that timeframe. The Govern-
ment also requested seven days of cell-site records from
Sprint, spanning the time around the robbery in Warren,
Ohio. It obtained two days of records.
   These records confirmed that Carpenter’s cell phone was
in the general vicinity of four of the nine robberies, includ-
ing the one in Ohio, at the times those robberies occurred.
                               II
  The first Clause of the Fourth Amendment provides that
“the right of the people to be secure in their persons, houses,
                 Cite as: 585 U. S. ____ (2018)           7

                   KENNEDY, J., dissenting

papers, and effects, against unreasonable searches and
seizures, shall not be violated.” The customary beginning
point in any Fourth Amendment search case is whether
the Government’s actions constitute a “search” of the
defendant’s person, house, papers, or effects, within the
meaning of the constitutional provision. If so, the next
question is whether that search was reasonable.
   Here the only question necessary to decide is whether
the Government searched anything of Carpenter’s when it
used compulsory process to obtain cell-site records from
Carpenter’s cell phone service providers. This Court’s
decisions in Miller and Smith dictate that the answer is
no, as every Court of Appeals to have considered the ques-
tion has recognized. See United States v. Thompson, 866
F. 3d 1149 (CA10 2017); United States v. Graham, 824
F. 3d 421 (CA4 2016) (en banc); Carpenter v. United
States, 819 F. 3d 880 (CA6 2016); United States v. Davis,
785 F. 3d 498 (CA11 2015) (en banc); In re Application
of U. S. for Historical Cell Site Data, 724 F. 3d 600
(CA5 2013).
                             A
  Miller and Smith hold that individuals lack any protected
Fourth Amendment interests in records that are pos-
sessed, owned, and controlled only by a third party. In
Miller federal law enforcement officers obtained four
months of the defendant’s banking records. 425 U. S., at
437438. And in Smith state police obtained records of
the phone numbers dialed from the defendant’s home
phone. 442 U. S., at 737. The Court held in both cases
that the officers did not search anything belonging to the
defendants within the meaning of the Fourth Amendment.
The defendants could “assert neither ownership nor pos-
session” of the records because the records were created,
owned, and controlled by the companies. Miller, supra, at
440; see Smith, supra, at 741. And the defendants had no
8               CARPENTER v. UNITED STATES

                     KENNEDY, J., dissenting

reasonable expectation of privacy in information they
“voluntarily conveyed to the [companies] and exposed to
their employees in the ordinary course of business.” Mil-
ler, supra, at 442; see Smith, 442 U. S., at 744. Rather,
the defendants “assumed the risk that the information
would be divulged to police.” Id., at 745.
   Miller and Smith have been criticized as being based on
too narrow a view of reasonable expectations of privacy.
See, e.g., Ashdown, The Fourth Amendment and the “Le-
gitimate Expectation of Privacy,” 34 Vand. L. Rev. 1289,
13131316 (1981). Those criticisms, however, are unwar-
ranted. The principle established in Miller and Smith is
correct for two reasons, the first relating to a defendant’s
attenuated interest in property owned by another, and the
second relating to the safeguards inherent in the use of
compulsory process.
   First, Miller and Smith placed necessary limits on the
ability of individuals to assert Fourth Amendment inter-
ests in property to which they lack a “requisite connec-
tion.” Minnesota v. Carter, 525 U. S. 83, 99 (1998)
(KENNEDY, J., concurring). Fourth Amendment rights,
after all, are personal. The Amendment protects “[t]he
right of the people to be secure in their . . . persons, houses,
papers, and effects”—not the persons, houses, papers, and
effects of others. (Emphasis added.)
   The concept of reasonable expectations of privacy, first
announced in Katz v. United States, 389 U. S. 347 (1967),
sought to look beyond the “arcane distinctions developed
in property and tort law” in evaluating whether a person
has a sufficient connection to the thing or place searched
to assert Fourth Amendment interests in it. Rakas v.
Illinois, 439 U. S. 128, 143 (1978). Yet “property concepts”
are, nonetheless, fundamental “in determining the pres-
ence or absence of the privacy interests protected by that
Amendment.” Id., at 143144, n. 12. This is so for at least
two reasons. First, as a matter of settled expectations
                 Cite as: 585 U. S. ____ (2018)           9

                    KENNEDY, J., dissenting

from the law of property, individuals often have greater
expectations of privacy in things and places that belong to
them, not to others. And second, the Fourth Amendment’s
protections must remain tethered to the text of that
Amendment, which, again, protects only a person’s own
“persons, houses, papers, and effects.”
   Katz did not abandon reliance on property-based con-
cepts. The Court in Katz analogized the phone booth used
in that case to a friend’s apartment, a taxicab, and a hotel
room. 389 U. S., at 352, 359. So when the defendant
“shu[t] the door behind him” and “pa[id] the toll,” id., at
352, he had a temporary interest in the space and a legit-
imate expectation that others would not intrude, much
like the interest a hotel guest has in a hotel room, Stoner
v. California, 376 U. S. 483 (1964), or an overnight guest
has in a host’s home, Minnesota v. Olson, 495 U. S. 91
(1990). The Government intruded on that space when it
attached a listening device to the phone booth. Katz, 389
U. S., at 348. (And even so, the Court made it clear that
the Government’s search could have been reasonable had
there been judicial approval on a case-specific basis,
which, of course, did occur here. Id., at 357359.)
   Miller and Smith set forth an important and necessary
limitation on the Katz framework. They rest upon the
commonsense principle that the absence of property law
analogues can be dispositive of privacy expectations. The
defendants in those cases could expect that the third-party
businesses could use the records the companies collected,
stored, and classified as their own for any number of
business and commercial purposes. The businesses were
not bailees or custodians of the records, with a duty to
hold the records for the defendants’ use. The defendants
could make no argument that the records were their own
papers or effects. See Miller, supra, at 440 (“the docu-
ments subpoenaed here are not respondent’s ‘private
papers’ ”); Smith, supra, at 741 (“petitioner obviously
10             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

cannot claim that his ‘property’ was invaded”). The rec-
ords were the business entities’ records, plain and simple.
The defendants had no reason to believe the records were
owned or controlled by them and so could not assert a
reasonable expectation of privacy in the records.
    The second principle supporting Miller and Smith is the
longstanding rule that the Government may use compul-
sory process to compel persons to disclose documents and
other evidence within their possession and control. See
United States v. Nixon, 418 U. S. 683, 709 (1974) (it is an
“ancient proposition of law” that “the public has a right to
every man’s evidence” (internal quotation marks and
alterations omitted)). A subpoena is different from a
warrant in its force and intrusive power. While a warrant
allows the Government to enter and seize and make the
examination itself, a subpoena simply requires the person
to whom it is directed to make the disclosure. A subpoena,
moreover, provides the recipient the “opportunity to pre-
sent objections” before complying, which further mitigates
the intrusion. Oklahoma Press Publishing Co. v. Walling,
327 U. S. 186, 195 (1946).
    For those reasons this Court has held that a subpoena
for records, although a “constructive” search subject to
Fourth Amendment constraints, need not comply with the
procedures applicable to warrants—even when challenged
by the person to whom the records belong. Id., at 202,
208.      Rather, a subpoena complies with the Fourth
Amendment’s reasonableness requirement so long as it is
“ ‘sufficiently limited in scope, relevant in purpose, and
specific in directive so that compliance will not be unrea-
sonably burdensome.’ ” Donovan v. Lone Steer, Inc., 464
U. S. 408, 415 (1984). Persons with no meaningful inter-
ests in the records sought by a subpoena, like the defend-
ants in Miller and Smith, have no rights to object to the
records’ disclosure—much less to assert that the Govern-
ment must obtain a warrant to compel disclosure of the
                 Cite as: 585 U. S. ____ (2018)          11

                   KENNEDY, J., dissenting

records. See Miller, 425 U. S., at 444446; SEC v. Jerry T.
O’Brien, Inc., 467 U. S. 735, 742743 (1984).
  Based on Miller and Smith and the principles underly-
ing those cases, it is well established that subpoenas may
be used to obtain a wide variety of records held by busi-
nesses, even when the records contain private information.
See 2 W. LaFave, Search and Seizure §4.13 (5th ed. 2012).
Credit cards are a prime example. State and federal law
enforcement, for instance, often subpoena credit card
statements to develop probable cause to prosecute crimes
ranging from drug trafficking and distribution to
healthcare fraud to tax evasion. See United States v.
Phibbs, 999 F. 2d 1053 (CA6 1993) (drug distribution);
McCune v. DOJ, 592 Fed. Appx. 287 (CA5 2014)
(healthcare fraud); United States v. Green, 305 F. 3d 422
(CA6 2002) (drug trafficking and tax evasion); see also 12
U. S. C. §§3402(4), 3407 (allowing the Government to
subpoena financial records if “there is reason to believe
that the records sought are relevant to a legitimate law
enforcement inquiry”). Subpoenas also may be used to
obtain vehicle registration records, hotel records, employ-
ment records, and records of utility usage, to name just a
few other examples. See 1 LaFave, supra, §2.7(c).
  And law enforcement officers are not alone in their
reliance on subpoenas to obtain business records for legit-
imate investigations. Subpoenas also are used for investi-
gatory purposes by state and federal grand juries, see
United States v. Dionisio, 410 U. S. 1 (1973), state and
federal administrative agencies, see Oklahoma Press,
supra, and state and federal legislative bodies, see
McPhaul v. United States, 364 U. S. 372 (1960).
                             B
   Carpenter does not question these traditional investiga-
tive practices. And he does not ask the Court to reconsider
Miller and Smith. Carpenter argues only that, under
12             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

Miller and Smith, the Government may not use compulsory
process to acquire cell-site records from cell phone service
providers.
   There is no merit in this argument. Cell-site records,
like all the examples just discussed, are created, kept,
classified, owned, and controlled by cell phone service
providers, which aggregate and sell this information to
third parties. As in Miller, Carpenter can “assert neither
ownership nor possession” of the records and has no con-
trol over them. 425 U. S., at 440.
   Carpenter argues that he has Fourth Amendment inter-
ests in the cell-site records because they are in essence his
personal papers by operation of 47 U. S. C. §222. That
statute imposes certain restrictions on how providers may
use “customer proprietary network information”—a term
that encompasses cell-site records. §§222(c), (h)(1)(A).
The statute in general prohibits providers from disclosing
personally identifiable cell-site records to private third
parties. §222(c)(1). And it allows customers to request
cell-site records from the provider. §222(c)(2).
   Carpenter’s argument is unpersuasive, however, for
§222 does not grant cell phone customers any meaningful
interest in cell-site records. The statute’s confidentiality
protections may be overridden by the interests of the
providers or the Government. The providers may disclose
the records “to protect the[ir] rights or property” or to
“initiate, render, bill, and collect for telecommunications
services.” §§222(d)(1), (2). They also may disclose the
records “as required by law”—which, of course, is how they
were disclosed in this case. §222(c)(1). Nor does the stat-
ute provide customers any practical control over the rec-
ords. Customers do not create the records; they have no
say in whether or for how long the records are stored; and
they cannot require the records to be modified or de-
stroyed. Even their right to request access to the records
is limited, for the statute “does not preclude a carrier from
                  Cite as: 585 U. S. ____ (2018)           13

                    KENNEDY, J., dissenting

being reimbursed by the customers . . . for the costs asso-
ciated with making such disclosures.” H. R. Rep. No. 104–
204, pt. 1, p. 90 (1995). So in every legal and practical
sense the “network information” regulated by §222 is,
under that statute, “proprietary” to the service providers,
not Carpenter. The Court does not argue otherwise.
  Because Carpenter lacks a requisite connection to the
cell-site records, he also may not claim a reasonable expec-
tation of privacy in them. He could expect that a third
party—the cell phone service provider—could use the
information it collected, stored, and classified as its own
for a variety of business and commercial purposes.
  All this is not to say that Miller and Smith are without
limits. Miller and Smith may not apply when the Gov-
ernment obtains the modern-day equivalents of an indi-
vidual’s own “papers” or “effects,” even when those papers
or effects are held by a third party. See Ex parte Jackson,
96 U. S. 727, 733 (1878) (letters held by mail carrier);
United States v. Warshak, 631 F. 3d 266, 283288 (CA6
2010) (e-mails held by Internet service provider). As
already discussed, however, this case does not involve
property or a bailment of that sort. Here the Govern-
ment’s acquisition of cell-site records falls within the
heartland of Miller and Smith.
  In fact, Carpenter’s Fourth Amendment objection is
even weaker than those of the defendants in Miller and
Smith. Here the Government did not use a mere sub-
poena to obtain the cell-site records. It acquired the records
only after it proved to a Magistrate Judge reasonable
grounds to believe that the records were relevant and
material to an ongoing criminal investigation. See 18
U. S. C. §2703(d). So even if §222 gave Carpenter some
attenuated interest in the records, the Government’s
conduct here would be reasonable under the standards
governing subpoenas. See Donovan, 464 U. S., at 415.
  Under Miller and Smith, then, a search of the sort that
14             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

requires a warrant simply did not occur when the Gov-
ernment used court-approved compulsory process, based
on a finding of reasonable necessity, to compel a cell phone
service provider, as owner, to disclose cell-site records.
                             III
  The Court rejects a straightforward application of Miller
and Smith. It concludes instead that applying those cases
to cell-site records would work a “significant extension” of
the principles underlying them, ante, at 15, and holds that
the acquisition of more than six days of cell-site records
constitutes a search, ante, at 11, n. 3.
  In my respectful view the majority opinion misreads this
Court’s precedents, old and recent, and transforms Miller
and Smith into an unprincipled and unworkable doctrine.
The Court’s newly conceived constitutional standard will
cause confusion; will undermine traditional and important
law enforcement practices; and will allow the cell phone to
become a protected medium that dangerous persons will
use to commit serious crimes.
                             A
  The Court errs at the outset by attempting to sidestep
Miller and Smith. The Court frames this case as following
instead from United States v. Knotts, 460 U. S. 276 (1983),
and United States v. Jones, 565 U. S. 400 (2012). Those
cases, the Court suggests, establish that “individuals have
a reasonable expectation of privacy in the whole of their
physical movements.” Ante, at 79, 12.
  Knotts held just the opposite: “A person traveling in an
automobile on public thoroughfares has no reasonable
expectation of privacy in his movements from one place to
another.” 460 U. S., at 281. True, the Court in Knotts also
suggested that “different constitutional principles may be
applicable” to “dragnet-type law enforcement practices.”
Id., at 284. But by dragnet practices the Court was refer-
                  Cite as: 585 U. S. ____ (2018)           15

                    KENNEDY, J., dissenting

ring to “ ‘twenty-four hour surveillance of any citizen of
this country . . . without judicial knowledge or supervi-
sion.’ ” Id., at 283.
   Those “different constitutional principles” mentioned in
Knotts, whatever they may be, do not apply in this case.
Here the Stored Communications Act requires a neutral
judicial officer to confirm in each case that the Govern-
ment has “reasonable grounds to believe” the cell-site
records “are relevant and material to an ongoing criminal
investigation.” 18 U. S. C. §2703(d). This judicial check
mitigates the Court’s concerns about “ ‘a too permeating
police surveillance.’ ” Ante, at 6 (quoting United States v.
Di Re, 332 U. S. 581, 595 (1948)). Here, even more so
than in Knotts, “reality hardly suggests abuse.” 460 U. S.,
at 284.
   The Court’s reliance on Jones fares no better. In Jones
the Government installed a GPS tracking device on the
defendant’s automobile. The Court held the Government
searched the automobile because it “physically occupied
private property [of the defendant] for the purpose of
obtaining information.” 565 U. S., at 404. So in Jones it
was “not necessary to inquire about the target’s expecta-
tion of privacy in his vehicle’s movements.” Grady v.
North Carolina, 575 U. S. ___, ___ (2015) (per curiam) (slip
op., at 3).
   Despite that clear delineation of the Court’s holding in
Jones, the Court today declares that Jones applied the
“ ‘different constitutional principles’ ” alluded to in Knotts
to establish that an individual has an expectation of pri-
vacy in the sum of his whereabouts. Ante, at 8, 12. For that
proposition the majority relies on the two concurring
opinions in Jones, one of which stated that “longer term
GPS monitoring in investigations of most offenses impinges
on expectations of privacy.” 565 U. S., at 430 (ALITO, J.,
concurring). But Jones involved direct governmental
surveillance of a defendant’s automobile without judicial
16             CARPENTER v. UNITED STATES

                   KENNEDY, J., dissenting

authorization—specifically, GPS surveillance accurate
within 50 to 100 feet. Id., at 402403. Even assuming
that the different constitutional principles mentioned in
Knotts would apply in a case like Jones—a proposition the
Court was careful not to announce in Jones, supra, at
412413—those principles are inapplicable here. Cases
like this one, where the Government uses court-approved
compulsory process to obtain records owned and controlled
by a third party, are governed by the two majority opin-
ions in Miller and Smith.
                              B
   The Court continues its analysis by misinterpreting
Miller and Smith, and then it reaches the wrong outcome
on these facts even under its flawed standard.
   The Court appears, in my respectful view, to read Miller
and Smith to establish a balancing test. For each “quali-
tatively different category” of information, the Court
suggests, the privacy interests at stake must be weighed
against the fact that the information has been disclosed to
a third party. See ante, at 11, 1517. When the privacy
interests are weighty enough to “overcome” the third-party
disclosure, the Fourth Amendment’s protections apply.
See ante, at 17.
   That is an untenable reading of Miller and Smith. As
already discussed, the fact that information was relin-
quished to a third party was the entire basis for conclud-
ing that the defendants in those cases lacked a reasonable
expectation of privacy. Miller and Smith do not establish
the kind of category-by-category balancing the Court today
prescribes.
   But suppose the Court were correct to say that Miller
and Smith rest on so imprecise a foundation. Still the
Court errs, in my submission, when it concludes that cell-
site records implicate greater privacy interests—and thus
deserve greater Fourth Amendment protection—than
                  Cite as: 585 U. S. ____ (2018)             17

                     KENNEDY, J., dissenting

financial records and telephone records.
    Indeed, the opposite is true. A person’s movements are
not particularly private. As the Court recognized in
Knotts, when the defendant there “traveled over the public
streets he voluntarily conveyed to anyone who wanted to
look the fact that he was traveling over particular roads in
a particular direction, the fact of whatever stops he made,
and the fact of his final destination.” 460 U. S., at
281282. Today expectations of privacy in one’s location
are, if anything, even less reasonable than when the Court
decided Knotts over 30 years ago. Millions of Americans
choose to share their location on a daily basis, whether by
using a variety of location-based services on their phones,
or by sharing their location with friends and the public at
large via social media.
    And cell-site records, as already discussed, disclose a
person’s location only in a general area. The records at
issue here, for example, revealed Carpenter’s location
within an area covering between around a dozen and
several hundred city blocks. “Areas of this scale might
encompass bridal stores and Bass Pro Shops, gay bars and
straight ones, a Methodist church and the local mosque.”
819 F. 3d 880, 889 (CA6 2016). These records could not
reveal where Carpenter lives and works, much less his
“ ‘familial, political, professional, religious, and sexual
associations.’ ” Ante, at 12 (quoting Jones, supra, at 415
(SOTOMAYOR, J., concurring)).
    By contrast, financial records and telephone records do
“ ‘revea[l] . . . personal affairs, opinions, habits and associ-
ations.’ ” Miller, 425 U. S., at 451 (Brennan, J., dissent-
ing); see Smith, 442 U. S., at 751 (Marshall, J., dissent-
ing). What persons purchase and to whom they talk might
disclose how much money they make; the political and
religious organizations to which they donate; whether they
have visited a psychiatrist, plastic surgeon, abortion clinic,
or AIDS treatment center; whether they go to gay bars or
18             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

straight ones; and who are their closest friends and family
members. The troves of intimate information the Gov-
ernment can and does obtain using financial records and
telephone records dwarfs what can be gathered from cell-
site records.
   Still, the Court maintains, cell-site records are “unique”
because they are “comprehensive” in their reach; allow for
retrospective collection; are “easy, cheap, and efficient
compared to traditional investigative tools”; and are not
exposed to cell phone service providers in a meaningfully
voluntary manner. Ante, at 1113, 17, 22. But many
other kinds of business records can be so described. Fi-
nancial records are of vast scope. Banks and credit card
companies keep a comprehensive account of almost every
transaction an individual makes on a daily basis. “With
just the click of a button, the Government can access each
[company’s] deep repository of historical [financial] infor-
mation at practically no expense.” Ante, at 1213. And
the decision whether to transact with banks and credit
card companies is no more or less voluntary than the
decision whether to use a cell phone. Today, just as when
Miller was decided, “ ‘it is impossible to participate in the
economic life of contemporary society without maintaining
a bank account.’ ” 425 U. S., at 451 (Brennan, J., dissent-
ing). But this Court, nevertheless, has held that individ-
uals do not have a reasonable expectation of privacy in
financial records.
   Perhaps recognizing the difficulty of drawing the consti-
tutional line between cell-site records and financial and
telephonic records, the Court posits that the accuracy of
cell-site records “is rapidly approaching GPS-level preci-
sion.” Ante, at 14. That is certainly plausible in the era of
cyber technology, yet the privacy interests associated with
location information, which is often disclosed to the public
at large, still would not outweigh the privacy interests
implicated by financial and telephonic records.
                 Cite as: 585 U. S. ____ (2018)          19

                    KENNEDY, J., dissenting

   Perhaps more important, those future developments are
no basis upon which to resolve this case. In general, the
Court “risks error by elaborating too fully on the Fourth
Amendment implications of emerging technology before its
role in society has become clear.” Ontario v. Quon, 560
U. S. 746, 759 (2010). That judicial caution, prudent in
most cases, is imperative in this one.
   Technological changes involving cell phones have com-
plex effects on crime and law enforcement. Cell phones
make crimes easier to coordinate and conceal, while also
providing the Government with new investigative tools
that may have the potential to upset traditional privacy
expectations.     See Kerr, An Equilibrium-Adjustment
Theory of the Fourth Amendment, 125 Harv. L. Rev 476,
512517 (2011). How those competing effects balance
against each other, and how property norms and expecta-
tions of privacy form around new technology, often will be
difficult to determine during periods of rapid technological
change. In those instances, and where the governing legal
standard is one of reasonableness, it is wise to defer to
legislative judgments like the one embodied in §2703(d) of
the Stored Communications Act. See Jones, 565 U. S., at
430 (ALITO, J., concurring). In §2703(d) Congress weighed
the privacy interests at stake and imposed a judicial check
to prevent executive overreach. The Court should be wary
of upsetting that legislative balance and erecting constitu-
tional barriers that foreclose further legislative instruc-
tions. See Quon, supra, at 759. The last thing the Court
should do is incorporate an arbitrary and outside limit—in
this case six days’ worth of cell-site records—and use it as
the foundation for a new constitutional framework. The
Court’s decision runs roughshod over the mechanism
Congress put in place to govern the acquisition of cell-site
records and closes off further legislative debate on these
issues.
20             CARPENTER v. UNITED STATES

                    KENNEDY, J., dissenting

                               C
   The Court says its decision is a “narrow one.” Ante, at
17. But its reinterpretation of Miller and Smith will have
dramatic consequences for law enforcement, courts, and
society as a whole.
   Most immediately, the Court’s holding that the Gov-
ernment must get a warrant to obtain more than six days
of cell-site records limits the effectiveness of an important
investigative tool for solving serious crimes. As this case
demonstrates, cell-site records are uniquely suited to help
the Government develop probable cause to apprehend
some of the Nation’s most dangerous criminals: serial
killers, rapists, arsonists, robbers, and so forth. See also,
e.g., Davis, 785 F. 3d, at 500501 (armed robbers); Brief
for Alabama et al. as Amici Curiae 2122 (serial killer).
These records often are indispensable at the initial stages
of investigations when the Government lacks the evidence
necessary to obtain a warrant. See United States v. Pem-
brook, 876 F. 3d 812, 816819 (CA6 2017). And the long-
term nature of many serious crimes, including serial
crimes and terrorism offenses, can necessitate the use of
significantly more than six days of cell-site records. The
Court’s arbitrary 6-day cutoff has the perverse effect
of nullifying Congress’ reasonable framework for obtain-
ing cell-site records in some of the most serious criminal
investigations.
   The Court’s decision also will have ramifications that
extend beyond cell-site records to other kinds of infor-
mation held by third parties, yet the Court fails “to pro-
vide clear guidance to law enforcement” and courts on key
issues raised by its reinterpretation of Miller and Smith.
Riley v. California, 573 U. S. ___, ___ (2014) (slip op.,
at 22).
   First, the Court’s holding is premised on cell-site records
being a “distinct category of information” from other busi-
                 Cite as: 585 U. S. ____ (2018)          21

                    KENNEDY, J., dissenting

ness records. Ante, at 15. But the Court does not explain
what makes something a distinct category of information.
Whether credit card records are distinct from bank rec-
ords; whether payment records from digital wallet applica-
tions are distinct from either; whether the electronic bank
records available today are distinct from the paper and
microfilm records at issue in Miller; or whether cell-phone
call records are distinct from the home-phone call records
at issue in Smith, are just a few of the difficult questions
that require answers under the Court’s novel conception of
Miller and Smith.
   Second, the majority opinion gives courts and law en-
forcement officers no indication how to determine whether
any particular category of information falls on the finan-
cial-records side or the cell-site-records side of its newly
conceived constitutional line. The Court’s multifactor
analysis—considering intimacy, comprehensiveness, ex-
pense, retrospectivity, and voluntariness—puts the law on
a new and unstable foundation.
   Third, even if a distinct category of information is
deemed to be more like cell-site records than financial
records, courts and law enforcement officers will have to
guess how much of that information can be requested
before a warrant is required. The Court suggests that less
than seven days of location information may not require a
warrant. See ante, at 11, n. 3; see also ante, at 1718
(expressing no opinion on “real-time CSLI,” tower dumps,
and security-camera footage). But the Court does not
explain why that is so, and nothing in its opinion even
alludes to the considerations that should determine
whether greater or lesser thresholds should apply to in-
formation like IP addresses or website browsing history.
   Fourth, by invalidating the Government’s use of court-
approved compulsory process in this case, the Court calls
into question the subpoena practices of federal and state
grand juries, legislatures, and other investigative bodies,
22             CARPENTER v. UNITED STATES

                   KENNEDY, J., dissenting

as JUSTICE ALITO’s opinion explains. See post, at 219
(dissenting opinion). Yet the Court fails even to mention
the serious consequences this will have for the proper
administration of justice.
  In short, the Court’s new and uncharted course will
inhibit law enforcement and “keep defendants and judges
guessing for years to come.” Riley, 573 U. S., at ___ (slip
op., at 25) (internal quotation marks omitted).
                        *     *     *
   This case should be resolved by interpreting accepted
property principles as the baseline for reasonable expecta-
tions of privacy. Here the Government did not search
anything over which Carpenter could assert ownership or
control. Instead, it issued a court-authorized subpoena to
a third party to disclose information it alone owned and
controlled. That should suffice to resolve this case.
   Having concluded, however, that the Government
searched Carpenter when it obtained cell-site records from
his cell phone service providers, the proper resolution of
this case should have been to remand for the Court of
Appeals to determine in the first instance whether the
search was reasonable. Most courts of appeals, believing
themselves bound by Miller and Smith, have not grappled
with this question. And the Court’s reflexive imposition of
the warrant requirement obscures important and difficult
issues, such as the scope of Congress’ power to authorize
the Government to collect new forms of information using
processes that deviate from traditional warrant proce-
dures, and how the Fourth Amendment’s reasonableness
requirement should apply when the Government uses
compulsory process instead of engaging in an actual,
physical search.
   These reasons all lead to this respectful dissent.
                 Cite as: 585 U. S. ____ (2018)          23

                   KENNEDY
               Appendix      , J., dissenting
                        to opinion  of KENNEDY, J.

                         APPENDIX

“§2703. Required disclosure of customer communi-
cations or records

   “(d) REQUIREMENTS FOR COURT ORDER.—A court order
for disclosure under subsection (b) or (c) may be issued by
any court that is a court of competent jurisdiction and
shall issue only if the governmental entity offers specific
and articulable facts showing that there are reasonable
grounds to believe that the contents of a wire or electronic
communication, or the records or other information
sought, are relevant and material to an ongoing criminal
investigation. In the case of a State governmental author-
ity, such a court order shall not issue if prohibited by the
law of such State. A court issuing an order pursuant to
this section, on a motion made promptly by the service
provider, may quash or modify such order, if the infor-
mation or records requested are unusually voluminous in
nature or compliance with such order otherwise would
cause an undue burden on such provider.”
                 Cite as: 585 U. S. ____ (2018)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 16–402
                         _________________


    TIMOTHY IVORY CARPENTER, PETITIONER v.

               UNITED STATES

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

            APPEALS FOR THE SIXTH CIRCUIT

                        [June 22, 2018] 


  JUSTICE THOMAS, dissenting.
  This case should not turn on “whether” a search oc­
curred. Ante, at 1. It should turn, instead, on whose
property was searched. The Fourth Amendment guaran­
tees individuals the right to be secure from unreasonable
searches of “their persons, houses, papers, and effects.”
(Emphasis added.) In other words, “each person has the
right to be secure against unreasonable searches . . . in his
own person, house, papers, and effects.” Minnesota v.
Carter, 525 U. S. 83, 92 (1998) (Scalia, J., concurring). By
obtaining the cell-site records of MetroPCS and Sprint, the
Government did not search Carpenter’s property. He did
not create the records, he does not maintain them, he
cannot control them, and he cannot destroy them. Neither
the terms of his contracts nor any provision of law makes
the records his. The records belong to MetroPCS and
Sprint.
  The Court concludes that, although the records are not
Carpenter’s, the Government must get a warrant because
Carpenter had a reasonable “expectation of privacy” in the
location information that they reveal. Ante, at 11. I agree
with JUSTICE KENNEDY, JUSTICE ALITO, JUSTICE
GORSUCH, and every Court of Appeals to consider the
question that this is not the best reading of our
precedents.
2                 CARPENTER v. UNITED STATES

                         THOMAS, J., dissenting

  The more fundamental problem with the Court’s opin­
ion, however, is its use of the “reasonable expectation of
privacy” test, which was first articulated by Justice Har­
lan in Katz v. United States, 389 U. S. 347, 360–361 (1967)
(concurring opinion). The Katz test has no basis in the
text or history of the Fourth Amendment. And, it invites
courts to make judgments about policy, not law. Until we
confront the problems with this test, Katz will continue to
distort Fourth Amendment jurisprudence. I respectfully
dissent.
                             I
  Katz was the culmination of a series of decisions apply­
ing the Fourth Amendment to electronic eavesdropping.
The first such decision was Olmstead v. United States, 277
U. S. 438 (1928), where federal officers had intercepted the
defendants’ conversations by tapping telephone lines near
their homes. Id., at 456–457. In an opinion by Chief
Justice Taft, the Court concluded that this wiretap did not
violate the Fourth Amendment. No “search” occurred,
according to the Court, because the officers did not physi­
cally enter the defendants’ homes. Id., at 464–466. And
neither the telephone lines nor the defendants’ intangible
conversations qualified as “persons, houses, papers, [or]
effects” within the meaning of the Fourth Amendment.
Ibid.1 In the ensuing decades, this Court adhered to

——————
   1 Justice Brandeis authored the principal dissent in Olmstead. He

consulted the “underlying purpose,” rather than “the words of the
[Fourth] Amendment,” to conclude that the wiretap was a search. 277
U. S., at 476. In Justice Brandeis’ view, the Framers “recognized the
significance of man’s spiritual nature, of his feelings and of his intel­
lect” and “sought to protect Americans in their beliefs, their thoughts,
their emotions and their sensations.” Id., at 478. Thus, “every unjusti­
fiable intrusion by the Government upon the privacy of the individual,
whatever the means employed,” should constitute an unreasonable
search under the Fourth Amendment. Ibid.
                 Cite as: 585 U. S. ____ (2018)           3

                    THOMAS, J., dissenting

Olmstead and rejected Fourth Amendment challenges to
various methods of electronic surveillance. See On Lee v.
United States, 343 U. S. 747, 749–753 (1952) (use of mi­
crophone to overhear conversations with confidential
informant); Goldman v. United States, 316 U. S. 129, 131–
132, 135–136 (1942) (use of detectaphone to hear conver­
sations in office next door).
  In the 1960’s, however, the Court began to retreat from
Olmstead. In Silverman v. United States, 365 U. S. 505
(1961), for example, federal officers had eavesdropped on
the defendants by driving a “spike mike” several inches
into the house they were occupying. Id., at 506–507. This
was a “search,” the Court held, because the “unauthorized
physical penetration into the premises” was an “actual
intrusion into a constitutionally protected area.” Id., at
509, 512. The Court did not mention Olmstead’s other
holding that intangible conversations are not “persons,
houses, papers, [or] effects.” That omission was signifi­
cant. The Court confirmed two years later that “[i]t fol­
lows from [Silverman] that the Fourth Amendment may
protect against the overhearing of verbal statements as
well as against the more traditional seizure of ‘papers and
effects.’ ” Wong Sun v. United States, 371 U. S. 471, 485
(1963); accord, Berger v. New York, 388 U. S. 41, 51 (1967).
  In Katz, the Court rejected Olmstead’s remaining hold-
ing—that eavesdropping is not a search absent a physical
intrusion into a constitutionally protected area. The
federal officers in Katz had intercepted the defendant’s
conversations by attaching an electronic device to the
outside of a public telephone booth. 389 U. S., at 348. The
Court concluded that this was a “search” because the
officers “violated the privacy upon which [the defendant]
justifiably relied while using the telephone booth.” Id., at
353. Although the device did not physically penetrate the
booth, the Court overruled Olmstead and held that “the
reach of [the Fourth] Amendment cannot turn upon the
4              CARPENTER v. UNITED STATES

                    THOMAS, J., dissenting

presence or absence of a physical intrusion.” 389 U. S., at
353. The Court did not explain what should replace
Olmstead’s physical-intrusion requirement.         It simply
asserted that “the Fourth Amendment protects people, not
places” and “what [a person] seeks to preserve as private
. . . may be constitutionally protected.” 389 U. S., at 351.
    Justice Harlan’s concurrence in Katz attempted to artic­
ulate the standard that was missing from the majority
opinion. While Justice Harlan agreed that “ ‘the Fourth
Amendment protects people, not places,’ ” he stressed that
“[t]he question . . . is what protection it affords to those
people,” and “the answer . . . requires reference to a
‘place.’ ” Id., at 361. Justice Harlan identified a “twofold
requirement” to determine when the protections of the
Fourth Amendment apply: “first that a person have exhib­
ited an actual (subjective) expectation of privacy and,
second, that the expectation be one that society is pre­
pared to recognize as ‘reasonable.’ ” Ibid.
    Justice Harlan did not cite anything for this “expecta­
tion of privacy” test, and the parties did not discuss it in
their briefs. The test appears to have been presented for
the first time at oral argument by one of the defendant’s
lawyers. See Winn, Katz and the Origins of the “Reason-
able Expectation of Privacy” Test, 40 McGeorge L. Rev. 1,
9–10 (2009). The lawyer, a recent law-school graduate,
apparently had an “[e]piphany” while preparing for oral
argument. Schneider, Katz v. United States: The Untold
Story, 40 McGeorge L. Rev. 13, 18 (2009). He conjectured
that, like the “reasonable person” test from his Torts class,
the Fourth Amendment should turn on “whether a rea­
sonable person . . . could have expected his communication
to be private.” Id., at 19. The lawyer presented his new
theory to the Court at oral argument. See, e.g., Tr. of Oral
Arg. in Katz v. United States, O. T. 1967, No. 35, p. 5
(proposing a test of “whether or not, objectively speaking,
the communication was intended to be private”); id., at 11
                 Cite as: 585 U. S. ____ (2018)            5

                    THOMAS, J., dissenting

(“We propose a test using a way that’s not too dissimilar
from the tort ‘reasonable man’ test”). After some question­
ing from the Justices, the lawyer conceded that his test
should also require individuals to subjectively expect
privacy. See id., at 12. With that modification, Justice
Harlan seemed to accept the lawyer’s test almost verbatim
in his concurrence.
  Although the majority opinion in Katz had little practi­
cal significance after Congress enacted the Omnibus
Crime Control and Safe Streets Act of 1968, Justice Har­
lan’s concurrence profoundly changed our Fourth Amend­
ment jurisprudence. It took only one year for the full
Court to adopt his two-pronged test. See Terry v. Ohio,
392 U. S. 1, 10 (1968). And by 1979, the Court was de­
scribing Justice Harlan’s test as the “lodestar” for deter­
mining whether a “search” had occurred. Smith v. Mary-
land, 442 U. S. 735, 739 (1979). Over time, the Court
minimized the subjective prong of Justice Harlan’s test.
See Kerr, Katz Has Only One Step: The Irrelevance of
Subjective Expectations, 82 U. Chi. L. Rev. 113 (2015).
That left the objective prong—the “reasonable expectation
of privacy” test that the Court still applies today. See
ante, at 5; United States v. Jones, 565 U. S. 400, 406
(2012).
                               II
   Under the Katz test, a “search” occurs whenever “gov­
ernment officers violate a person’s ‘reasonable expectation
of privacy.’ ” Jones, supra, at 406. The most glaring prob­
lem with this test is that it has “no plausible foundation in
the text of the Fourth Amendment.” Carter, 525 U. S., at
97 (opinion of Scalia, J.). The Fourth Amendment, as
relevant here, protects “[t]he right of the people to be
secure in their persons, houses, papers, and effects,
against unreasonable searches.” By defining “search” to
mean “any violation of a reasonable expectation of pri-
6              CARPENTER v. UNITED STATES

                     THOMAS, J., dissenting

vacy,” the Katz test misconstrues virtually every one of
these words.
                               A
   The Katz test distorts the original meaning of
“searc[h]”—the word in the Fourth Amendment that it
purports to define, see ante, at 5; Smith, supra. Under the
Katz test, the government conducts a search anytime it
violates someone’s “reasonable expectation of privacy.”
That is not a normal definition of the word “search.”
   At the founding, “search” did not mean a violation of
someone’s reasonable expectation of privacy. The word
was probably not a term of art, as it does not appear in
legal dictionaries from the era. And its ordinary meaning
was the same as it is today: “ ‘[t]o look over or through for
the purpose of finding something; to explore; to examine
by inspection; as, to search the house for a book; to search
the wood for a thief.’ ” Kyllo v. United States, 533 U. S. 27,
32, n. 1 (2001) (quoting N. Webster, An American Diction­
ary of the English Language 66 (1828) (reprint 6th ed.
1989)); accord, 2 S. Johnson, A Dictionary of the English
Language (5th ed. 1773) (“Inquiry by looking into every
suspected place”); N. Bailey, An Universal Etymological
English Dictionary (22d ed. 1770) (“a seeking after, a
looking for, &c.”); 2 J. Ash, The New and Complete Dic­
tionary of the English Language (2d ed. 1795) (“An en­
quiry, an examination, the act of seeking, an enquiry by
looking into every suspected place; a quest; a pursuit”); T.
Sheridan, A Complete Dictionary of the English Language
(6th ed. 1796) (similar). The word “search” was not asso­
ciated with “reasonable expectation of privacy” until Jus­
tice Harlan coined that phrase in 1967. The phrase “ex­
pectation(s) of privacy” does not appear in the pre-Katz
federal or state case reporters, the papers of prominent
                    Cite as: 585 U. S. ____ (2018)                   7

                        THOMAS, J., dissenting

Founders,2 early congressional documents and debates,3
collections of early American English texts,4 or early
American newspapers.5
                               B
   The Katz test strays even further from the text by focus­
ing on the concept of “privacy.” The word “privacy” does
not appear in the Fourth Amendment (or anywhere else in
the Constitution for that matter). Instead, the Fourth
Amendment references “[t]he right of the people to be
secure.” It then qualifies that right by limiting it to “per­
sons” and three specific types of property: “houses, papers,
and effects.” By connecting the right to be secure to these
four specific objects, “[t]he text of the Fourth Amendment
reflects its close connection to property.” Jones, supra, at
405. “[P]rivacy,” by contrast, “was not part of the political
vocabulary of the [founding]. Instead, liberty and privacy
rights were understood largely in terms of property
rights.” Cloud, Property Is Privacy: Locke and Brandeis in
the Twenty-First Century, 55 Am. Crim. L. Rev. 37, 42
(2018).
   Those who ratified the Fourth Amendment were quite
familiar with the notion of security in property. Security
in property was a prominent concept in English law. See,
e.g., 3 W. Blackstone, Commentaries on the Laws of Eng-

——————
  2 National Archives, Library of Congress, Founders Online, https://
founders.archives.gov (all Internet materials as last visited June
18, 2018).
  3 A Century of Lawmaking For A New Nation, U. S. Congressional

Documents and Debates, 1774–1875 (May 1, 2003), https://memory.loc
.gov/ammem/amlaw/lawhome.html.
  4 Corpus of Historical American English, https://corpus.byu.edu/coha;

Google Books (American), https://googlebooks.byu.edu/x.asp; Corpus of
Founding Era American English, https://lawncl.byu.edu/cofea.
  5 Readex,   America’s Historical Newspapers (2018), https://
www.readex.com/content/americas-historical-newspapers.
8                CARPENTER v. UNITED STATES

                       THOMAS, J., dissenting

land 288 (1768) (“[E]very man’s house is looked upon by
the law to be his castle”); 3 E. Coke, Institutes of Laws of
England 162 (6th ed. 1680) (“[F]or a man[’]s house is his
Castle, & domus sua cuique est tutissimum refugium
[each man’s home is his safest refuge]”). The political
philosophy of John Locke, moreover, “permeated the 18th­
century political scene in America.” Obergefell v. Hodges,
576 U. S. ___, ___ (2015) (THOMAS, J., dissenting) (slip op.,
at 8). For Locke, every individual had a property right “in
his own person” and in anything he “removed from the
common state [of] Nature” and “mixed his labour with.”
Second Treatise of Civil Government §27 (1690). Because
property is “very unsecure” in the state of nature, §123,
individuals form governments to obtain “a secure enjoy­
ment of their properties.” §95. Once a government is
formed, however, it cannot be given “a power to destroy
that which every one designs to secure”; it cannot legiti­
mately “endeavour to take away, and destroy the property
of the people,” or exercise “an absolute power over [their]
lives, liberties, and estates.” §222.
   The concept of security in property recognized by Locke
and the English legal tradition appeared throughout the
materials that inspired the Fourth Amendment. In Entick
v. Carrington, 19 How. St. Tr. 1029 (C. P. 1765)—a her­
alded decision that the founding generation considered
“the true and ultimate expression of constitutional law,”
Boyd v. United States, 116 U. S. 616, 626 (1886)—Lord
Camden explained that “[t]he great end, for which men
entered into society, was to secure their property.” 19
How. St. Tr., at 1066. The American colonists echoed this
reasoning in their “widespread hostility” to the Crown’s
writs of assistance6—a practice that inspired the Revolu­

——————
   6 Writs of assistance were “general warrants” that gave “customs

officials blanket authority to search where they pleased for goods
                     Cite as: 585 U. S. ____ (2018)                      9

                         THOMAS, J., dissenting

tion and became “[t]he driving force behind the adoption of
the [Fourth] Amendment.” United States v. Verdugo-
Urquidez, 494 U. S. 259, 266 (1990). Prominent colonists
decried the writs as destroying “ ‘domestic security’ ” by
permitting broad searches of homes. M. Smith, The Writs
of Assistance Case 475 (1978) (quoting a 1772 Boston town
meeting); see also id., at 562 (complaining that “ ‘every
householder in this province, will necessarily become less
secure than he was before this writ’ ” (quoting a 1762
article in the Boston Gazette)); id., at 493 (complaining
that the writs were “ ‘expressly contrary to the common
law, which ever regarded a man’s house as his castle, or a
place of perfect security’ ” (quoting a 1768 letter from John
Dickinson)). John Otis, who argued the famous Writs of
Assistance case, contended that the writs violated “ ‘the
fundamental Principl[e] of Law’ ” that “ ‘[a] Man who is
quiet, is as secure in his House, as a Prince in his Castle.’ ”
Id., at 339 (quoting John Adam’s notes). John Adams
attended Otis’ argument and later drafted Article XIV of
the Massachusetts Constitution,7 which served as a model
for the Fourth Amendment. See Clancy, The Framers’
Intent: John Adams, His Era, and the Fourth Amendment,
86 Ind. L. J. 979, 982 (2011); Donahue, The Original
Fourth Amendment, 83 U. Chi. L. Rev. 1181, 1269 (2016)

—————— 

imported in violation of the British tax laws.” Stanford v. Texas, 379

U. S. 476, 481 (1965).
   7 “Every subject has a right to be secure from all unreasonable

searches and seizures of his person, his house, his papers, and all his
possessions. All warrants, therefore, are contrary to right, if the cause
or foundation of them be not previously supported by oath or affirma­
tion, and if the order in the warrant to a civil officer, to make search in
suspected places, or to arrest one or more suspected persons, or to seize
their property, be not accompanied with a special designation of the
person or objects of search, arrest, or seizure; and no warrant ought to
be issued but in cases, and with the formalities prescribed by the laws.”
Mass. Const., pt. I, Art. XIV (1780).
10              CARPENTER v. UNITED STATES

                      THOMAS, J., dissenting

(Donahue). Adams agreed that “[p]roperty must be se­
cure

[...TRUNCATED 124974 of 244974 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Carroll v. Carman.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Carroll v. Carman
type: case
citation: "574 U.S. 13 (2014)"
parallel_cite: ""
neutral_cite: ""
court: U.S.
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-11-10
docket: 14-212
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
  opinion_url: "https://www.courtlistener.com/opinion/2750102/carroll-v-carman/"
  cluster_id: 2750102
  opinion_id: null
  identity_checked: false
lake:
  record_id: Carroll v. Carman
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
related:
  - "[[Knock and Talk]]"
  - "[[Florida v. Jardines]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - curtilage
  - qualified-immunity
  - per-curiam
holding: "It is not clearly established that the 'knock and talk' exception requires officers to approach only the front door; an officer who went to a side sliding-glass door that visitors could use was therefore entitled to qualified immunity, and the Supreme Court left open whether such an approach is constitutional."
aliases:
  - Carman v. Carroll
---

# Carroll v. Carman

*574 U.S. 13 (2014)* (No. 14-212) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): per curiam; identity cluster 2750102 → 574 U.S. 13, 135 S. Ct. 348, decided 2014-11-10; Rule quote string-matched to the CL opinion text 2026-07-07. The CL text carries S. Ct. star pagination, so the pin is to 135 S. Ct. 352. S9 promotes. -->

## Background
Officer Jeremy Carroll went to the Carmans' home to investigate a report about a stolen car and a possibly armed suspect. Rather than the front door, he walked into the backyard and onto a deck, entering through a sliding glass door area, where an encounter ensued. The Carmans sued under § 1983; a jury found for Carroll, but the Third Circuit reversed, holding as a matter of law that the "knock and talk" exception requires officers to begin at the front door and denying Carroll [[Qualified Immunity|qualified immunity]].

## Issue
Whether it was clearly established that the "knock and talk" exception to the warrant requirement forbids officers from approaching a home by any route other than the front door.

## Rule
The Supreme Court, [[Common Legal Terms#per-curiam|per curiam]], reversed. It held that no such rule was clearly established: the Third Circuit's sole authority did not require officers to knock at the front door before going to other visitor-accessible parts of the property, and other courts had upheld approaches to side and back entrances. The Court expressly reserved the merits: "We do not decide today whether those cases were correctly decided or whether a police officer may conduct a 'knock and talk' at any entrance that is open to visitors rather than only the front door." — 135 S. Ct. at 352. Because the contrary rule was not "beyond debate," "[t]he Third Circuit therefore erred when it held that Carroll was not entitled to qualified immunity."

## Application
[[Qualified Immunity|Qualified immunity]] protects officers unless they violate a right so settled that every reasonable officer would know it — a standard the front-door rule did not meet in 2009. Whatever the correct Fourth Amendment answer, an officer could reasonably have believed he was permitted to approach a door open to ordinary visitors, so Carroll could not be held personally liable.

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted; the judgment of the Third Circuit was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] — Officer Carroll was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Carroll v. Carman* is a qualified-immunity decision that deliberately left the front-door question open: it neither adopted nor rejected the view that a lawful "knock and talk" (cf. *[[Florida v. Jardines]]*'s implied-license analysis) is confined to the front door, holding only that the contrary rule was not clearly established.

## Appears on
- [[Knock and Talk]] — *Key*

## Sources
- [*Carroll v. Carman*, 574 U.S. 13 (2014) (per curiam)](https://www.courtlistener.com/opinion/2750102/carroll-v-carman/) — pinpoint: 135 S. Ct. 348, 352 (the parallel reporter the CL text star-paginates; = 574 U.S. at 18–19); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "64f4a2640be4ba0f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Carroll v. Carman"}, "payload": {"all": [{"cite": "574 U.S. 13", "page": "13", "reporter": "U.S.", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "574"}], "display": "574 U.S. 13", "official": {"cite": "574 U.S. 13", "page": "13", "reporter": "U.S.", "selected_official": true, "source": "web-dual-leg", "type": 1, "volume": "574"}, "official_selection_present": true, "record_id": "Carroll v. Carman"}}
{"assertion_id": "418622352ab1ebc1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Carroll v. Carman"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Carroll v. Carman", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Carroll v. Carman

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carroll v. Carman",
  "status": "under_review",
  "identity": {
    "case_name": "Carroll v. Carman",
    "case_name_short": "Carroll",
    "case_name_full": "Jeremy CARROLL v. Andrew CARMAN, Et Ux.",
    "input_case_name": "Carroll v. Carman",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-11-10",
    "year": 2014,
    "docket": "14-212",
    "cluster_id": 2750102,
    "lead_opinion_id": 2750102,
    "sibling_ids": [],
    "absolute_url": "/opinion/2750102/carroll-v-carman/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "574 U.S. 13",
      "volume": "574",
      "reporter": "U.S.",
      "page": "13",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "574 U.S. 13",
        "volume": "574",
        "reporter": "U.S.",
        "page": "13",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "574 U.S. 13",
    "official_selection": {
      "court_class": "scotus",
      "selected": "574 U.S. 13",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "Google Scholar",
        "url": "https://scholar.google.com/scholar_case?case=3474605511210172307",
        "cite": "574 U.S. 13",
        "checked_date": "2026-07-07"
      },
      {
        "source": "Oyez",
        "url": "https://www.oyez.org/cases/2014/14-212",
        "cite": "574 U.S. 13",
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
    "date_created": "2026-07-07T01:36:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "carroll-v-carman--2750102",
      "to_record_id": "Carroll v. Carman",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Carroll v. Carman

```
                 Cite as: 574 U. S. ____ (2014)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
   JEREMY CARROLL v. ANDREW CARMAN, ET UX.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE THIRD CIRCUIT

            No. 14–212.   Decided November 10, 2014


   PER CURIAM.
   On July 3, 2009, the Pennsylvania State Police Depart-
ment received a report that a man named Michael Zita
had stolen a car and two loaded handguns. The report
also said that Zita might have fled to the home of Andrew
and Karen Carman. The department sent Officers Jeremy
Carroll and Brian Roberts to the Carmans’ home to inves-
tigate. Neither officer had been to the home before. 749
F. 3d 192, 195 (CA3 2014).
   The officers arrived in separate patrol cars around 2:30
p.m. The Carmans’ house sat on a corner lot—the front of
the house faced a main street while the left (as viewed
from the front) faced a side street. The officers initially
drove to the front of the house, but after discovering that
parking was not available there, turned right onto the side
street. As they did so, they saw several cars parked side-
by-side in a gravel parking area on the left side of the
Carmans’ property. The officers parked in the “first avail-
able spot,” at “the far rear of the property.” Ibid. (quoting
Tr. 70 (Apr. 8, 2013)).
   The officers exited their patrol cars. As they looked
toward the house, the officers saw a small structure (ei-
ther a carport or a shed) with its door open and a light on.
Id., at 71. Thinking someone might be inside, Officer
Carroll walked over, “poked [his] head” in, and said
“Pennsylvania State Police.” 749 F. 3d, at 195 (quoting Tr.
71 (Apr. 8, 2013); alteration in original). No one was
there, however, so the officers continued walking toward
the house. As they approached, they saw a sliding glass
2                   CARROLL v. CARMAN

                         Per Curiam

door that opened onto a ground-level deck. Carroll
thought the sliding glass door “looked like a customary
entryway,” so he and Officer Roberts decided to knock on
it. 749 F. 3d, at 195 (quoting Tr. 83 (Apr. 8, 2013)).
   As the officers stepped onto the deck, a man came out
of the house and “belligerent[ly] and aggressively ap-
proached” them. 749 F. 3d, at 195. The officers identified
themselves, explained they were looking for Michael Zita,
and asked the man for his name. The man refused to
answer. Instead, he turned away from the officers and
appeared to reach for his waist. Id., at 195–196. Carroll
grabbed the man’s right arm to make sure he was not
reaching for a weapon. The man twisted away from Car-
roll, lost his balance, and fell into the yard. Id., at 196.
   At that point, a woman came out of the house and asked
what was happening. The officers again explained that
they were looking for Zita. The woman then identified
herself as Karen Carman, identified the man as her hus-
band, Andrew Carman, and told the officers that Zita was
not there. In response, the officers asked for permission to
search the house for Zita. Karen Carman consented, and
everyone went inside. Ibid.
   The officers searched the house, but did not find Zita.
They then left. The Carmans were not charged with any
crimes. Ibid.
   The Carmans later sued Officer Carroll in Federal
District Court under 42 U. S. C. §1983. Among other
things, they alleged that Carroll unlawfully entered their
property in violation of the Fourth Amendment when he
went into their backyard and onto their deck without a
warrant. 749 F. 3d, at 196.
   At trial, Carroll argued that his entry was lawful under
the “knock and talk” exception to the warrant require-
ment. That exception, he contended, allows officers to
knock on someone’s door, so long as they stay “on those
portions of [the] property that the general public is al-
                  Cite as: 574 U. S. ____ (2014)            3

                           Per Curiam

lowed to go on.” Tr. 7 (Apr. 8, 2013). The Carmans re-
sponded that a normal visitor would have gone to their
front door, rather than into their backyard or onto their
deck. Thus, they argued, the “knock and talk” exception
did not apply.
  At the close of Carroll’s case in chief, the parties each
moved for judgment as a matter of law. The District Court
denied both motions, and sent the case to a jury. As rele-
vant here, the District Court instructed the jury that the
“knock and talk” exception “allows officers without a
warrant to knock on a resident’s door or otherwise ap-
proach the residence seeking to speak to the inhabitants,
just as any private citizen might.” Id., at 24 (Apr. 10,
2013). The District Court further explained that “officers
should restrict their movements to walkways, driveways,
porches and places where visitors could be expected to go.”
Ibid. The jury then returned a verdict for Carroll.
  The Carmans appealed, and the Court of Appeals for the
Third Circuit reversed in relevant part. The court held
that Officer Carroll violated the Fourth Amendment as a
matter of law because the “knock and talk” exception
“requires that police officers begin their encounter at the
front door, where they have an implied invitation to go.”
749 F. 3d, at 199. The court also held that Carroll was not
entitled to qualified immunity because his actions violated
clearly established law. Ibid. The court therefore re-
versed the District Court and held that the Carmans were
entitled to judgment as a matter of law.
  Carroll petitioned for certiorari. We grant the petition
and reverse the Third Circuit’s determination that Carroll
was not entitled to qualified immunity.
  A government official sued under §1983 is entitled to
qualified immunity unless the official violated a statutory
or constitutional right that was clearly established at the
time of the challenged conduct. See Ashcroft v. al-Kidd,
563 U. S. ___, ___ (2011) (slip op., at 3). A right is clearly
4                    CARROLL v. CARMAN

                          Per Curiam

established only if its contours are sufficiently clear that
“a reasonable official would understand that what he is
doing violates that right.” Anderson v. Creighton, 483
U. S. 635, 640 (1987). In other words, “existing precedent
must have placed the statutory or constitutional question
beyond debate.” al-Kidd, 563 U. S., at ___ (slip op., at 9).
This doctrine “gives government officials breathing room
to make reasonable but mistaken judgments,” and “pro-
tects ‘all but the plainly incompetent or those who know-
ingly violate the law.’ ” Id., at ___ (slip op., at 12) (quoting
Malley v. Briggs, 475 U. S. 335, 341 (1986)).
   Here the Third Circuit cited only a single case to sup-
port its decision that Carroll was not entitled to qualified
immunity—Estate of Smith v. Marasco, 318 F. 3d 497
(CA3 2003). Assuming for the sake of argument that a
controlling circuit precedent could constitute clearly estab-
lished federal law in these circumstances, see Reichle v.
Howards, 566 U. S. ___, ___ (2012) (slip op., at 7), Marasco
does not clearly establish that Carroll violated the Car-
mans’ Fourth Amendment rights.
   In Marasco, two police officers went to Robert Smith’s
house and knocked on the front door. When Smith did not
respond, the officers went into the backyard, and at least
one entered the garage. 318 F. 3d, at 519. The court
acknowledged that the officers’ “entry into the curtilage
after not receiving an answer at the front door might be
reasonable.” Id., at 520. It held, however, that the Dis-
trict Court had not made the factual findings needed to
decide that issue. Id., at 521. For example, the Third
Circuit noted that the record “did not discuss the layout of
the property or the position of the officers on that prop-
erty,” and that “there [was] no indication of whether the
officers followed a path or other apparently open route
that would be suggestive of reasonableness.” Ibid. The
court therefore remanded the case for further proceedings.
   In concluding that Officer Carroll violated clearly estab-
                 Cite as: 574 U. S. ____ (2014)            5

                          Per Curiam

lished law in this case, the Third Circuit relied exclusively
on Marasco’s statement that “entry into the curtilage after
not receiving an answer at the front door might be reason-
able.” Id., at 520; see 749 F. 3d, at 199 (quoting Marasco,
supra, at 520). In the court’s view, that statement clearly
established that a “knock and talk” must begin at the
front door. But that conclusion does not follow. Marasco
held that an unsuccessful “knock and talk” at the front
door does not automatically allow officers to go onto other
parts of the property. It did not hold, however, that
knocking on the front door is required before officers go
onto other parts of the property that are open to visitors.
Thus, Marasco simply did not answer the question whether
a “knock and talk” must begin at the front door when
visitors may also go to the back door. Indeed, the house at
issue seems not to have even had a back door, let alone
one that visitors could use. 318 F. 3d, at 521.
   Moreover, Marasco expressly stated that “there [was] no
indication of whether the officers followed a path or other
apparently open route that would be suggestive of reason-
ableness.” Ibid. That makes Marasco wholly different
from this case, where the jury necessarily decided that
Carroll “restrict[ed] [his] movements to walkways, drive-
ways, porches and places where visitors could be expected
to go.” Tr. 24 (Apr. 10, 2013).
   To the extent that Marasco says anything about this
case, it arguably supports Carroll’s view. In Marasco, the
Third Circuit noted that “[o]fficers are allowed to knock on
a residence’s door or otherwise approach the residence
seeking to speak to the inhabitants just as any private
citizen may.” 318 F. 3d, at 519. The court also said that,
“ ‘when the police come on to private property . . . and
restrict their movements to places visitors could be ex-
pected to go (e.g., walkways, driveways, porches), observa-
tions made from such vantage points are not covered by
the Fourth Amendment.’ ” Ibid. (quoting 1 W. LaFave,
6                       CARROLL v. CARMAN

                              Per Curiam

Search and Seizure §2.3(f ) (3d ed. 1996 and Supp. 2003)
(footnotes omitted)). Had Carroll read those statements
before going to the Carmans’ house, he may have concluded—
quite reasonably—that he was allowed to knock on any
door that was open to visitors.*
   The Third Circuit’s decision is even more perplexing in
comparison to the decisions of other federal and state
courts, which have rejected the rule the Third Circuit
adopted here. For example, in United States v. Titemore,
437 F. 3d 251 (CA2 2006), a police officer approached a
house that had two doors. The first was a traditional door
that opened onto a driveway; the second was a sliding
glass door that opened onto a small porch. The officer
chose to knock on the latter. Id., at 253–254. On appeal,
the defendant argued that the officer had unlawfully
entered his property without a warrant in violation of the
Fourth Amendment. Id., at 255–256. But the Second
Circuit rejected that argument. As the court explained,
the sliding glass door was “a primary entrance visible to
and used by the public.” Id., at 259. Thus, “[b]ecause [the
officer] approached a principal entrance to the home using
a route that other visitors could be expected to take,” the
court held that he did not violate the Fourth Amendment.
Id., at 252.
   The Seventh Circuit’s decision in United States v.
James, 40 F. 3d 850 (1994), vacated on other grounds, 516
U. S. 1022 (1995), provides another example. There, police
——————
  * In a footnote, the Court of Appeals “recognize[d] that there may be
some instances in which the front door is not the entrance used by
visitors,” but noted that “this is not one such instance.” 749 F. 3d 192,
198, n. 6 (2014) (emphasis added). This footnote still reflects the Third
Circuit’s view that the “knock and talk” exception is available for only
one entrance to a dwelling, “which in most circumstances is the front
door.” Id., at 198. Cf. United States v. Perea-Rey, 680 F. 3d 1179, 1188
(CA9 2012) (“Officers conducting a knock and talk . . . need not ap-
proach only a specific door if there are multiple doors accessible to the
public.”).
                 Cite as: 574 U. S. ____ (2014)           7

                          Per Curiam

officers approached a duplex with multiple entrances.
Bypassing the front door, the officers “used a paved walk-
way along the side of the duplex leading to the rear side
door.” 40 F. 3d, at 862. On appeal, the defendant argued
that the officers violated his Fourth Amendment rights
when they went to the rear side door. The Seventh Circuit
rejected that argument, explaining that the rear side door
was “accessible to the general public” and “was commonly
used for entering the duplex from the nearby alley.” Ibid.
In situations “where the back door of a residence is readily
accessible to the general public,” the court held, “the
Fourth Amendment is not implicated when police officers
approach that door in the reasonable belief that it is a
principal means of access to the dwelling.” Ibid. See also,
e.g., United States v. Garcia, 997 F. 2d 1273, 1279–1280
(CA9 1993) (“If the front and back of a residence are read-
ily accessible from a public place, like the driveway and
parking area here, the Fourth Amendment is not implicated
when officers go to the back door reasonably believing it
is used as a principal entrance to the dwelling”); State v.
Domicz, 188 N. J. 285, 302, 907 A. 2d 395, 405 (2006)
(“when a law enforcement officer walks to a front or back
door for the purpose of making contact with a resident and
reasonably believes that the door is used by visitors, he is
not unconstitutionally trespassing on to the property”).
   We do not decide today whether those cases were cor-
rectly decided or whether a police officer may conduct a
“knock and talk” at any entrance that is open to visitors
rather than only the front door. “But whether or not the
constitutional rule applied by the court below was correct,
it was not ‘beyond debate.’ ” Stanton v. Sims, 571 U. S.
___, ___ (2013) (per curiam) (slip op., at 8) (quoting al-
Kidd, 563 U. S., at ___ (slip op., at 9)). The Third Circuit
therefore erred when it held that Carroll was not entitled
to qualified immunity.
   The petition for certiorari is granted. The judgment of
8                   CARROLL v. CARMAN

                         Per Curiam

the United States Court of Appeals for the Third Circuit is
reversed, and the case is remanded for further proceedings
consistent with this opinion.
                                           It is so ordered.

```

---

## GROUP: _overhaul2/lake/cases/Carroll v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Carroll v. United States"
type: case
citation: "267 U.S. 132 (1925)"
parallel_cite: "45 S. Ct. 280; 69 L. Ed. 543"
neutral_cite: 1925 U.S. LEXIS 361
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1925
date_decided: 1925-11-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1925-03-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Carroll v. United States
  varies_by_point: false
  scope_note: "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100567/carroll-v-united-states/"
  cluster_id: 100567
  opinion_id: 100567
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Anchor"
related: ["[[Chambers v. Maroney]]", "[[California v. Carney]]", "[[California v. Acevedo]]", "[[Collins v. Virginia]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "warrantless-search", "vehicle", "probable-cause"]
holding: "Origin of the automobile exception: a vehicle may be searched without a warrant on probable cause because, unlike a fixed structure, it…"
lake:
  record_id: Carroll v. United States
  status: verified
  projected_at: 2026-07-06
---

# Carroll v. United States

*267 U.S. 132 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During Prohibition, federal agents who had probable cause to believe Carroll and a companion were transporting bootleg liquor stopped their automobile on a highway between Detroit and Grand Rapids and searched it without a warrant, finding 68 bottles of liquor concealed behind the upholstery. Carroll was convicted of transporting intoxicating liquor and challenged the warrantless search.

## Issue
Whether officers with probable cause may search a moving vehicle for contraband without first obtaining a warrant.

## Rule
Yes. The Court distinguished fixed premises from vehicles: there is "a necessary difference between a search of a store, dwelling house, or other structure in respect of which a proper official warrant readily may be obtained and a search of a ship, motor boat, wagon, or automobile for contraband goods, where it is not practicable to secure a warrant, because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." — 267 U.S. 132, ¶ 37. ^pin-p37

The exception rests on probable cause plus the vehicle's ready mobility; a warrantless search of a vehicle on probable cause to believe it carries contraband is reasonable.

## Application
The officers had probable cause — built on prior dealings and recognition of the car and its occupants — to believe Carroll's automobile was carrying contraband liquor. Because the car was readily movable and a warrant could not practicably be obtained before it left the area, the warrantless search of the vehicle on these facts was reasonable under the Fourth Amendment.

## Conclusion
The warrantless search of the moving automobile on probable cause was lawful; the conviction was affirmed. *Carroll* is the origin of the automobile exception.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Carroll*'s rule has been repeatedly reaffirmed and elaborated — extended to delayed station-house searches in [[Chambers v. Maroney]], grounded in ready mobility and pervasive regulation in [[California v. Carney]], and unified for containers in [[California v. Acevedo]]; its reach was bounded at the home's [[Curtilage|curtilage]] in [[Collins v. Virginia]].

## Appears on
- [[Automobile Exception]] — *Key — Anchor*

## Sources
- *Carroll v. United States*, 267 U.S. 132 (1925) — https://www.courtlistener.com/opinion/100567/carroll-v-united-states/ — pinpoint given as CourtListener paragraph number (¶ 37); CL's text of this 1925 opinion is paragraph-numbered without U.S. Reports star pagination at the quoted passage.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b66f974dd047317c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Carroll v. United States"}, "payload": {"all": [{"cite": "267 U.S. 132", "page": "132", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "267"}, {"cite": "45 S. Ct. 280", "page": "280", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "45"}, {"cite": "69 L. Ed. 543", "page": "543", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "69"}, {"cite": "1925 U.S. LEXIS 361", "page": "361", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1925"}], "display": "267 U.S. 132", "official": {"cite": "267 U.S. 132", "page": "132", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "267"}, "official_selection_present": true, "record_id": "Carroll v. United States"}}
{"assertion_id": "75c911a1883ff6d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-p37", "record_id": "Carroll v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-p37", "pinpoint_status": "slip-only", "quote": "--- # Carroll v. United States *267 U.S. 132 (1925)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During Prohibition, federal agents who had probable cause to believe Carroll and a companion were transporting bootleg liquor stopped their automobile on a highway between Detroit and Grand Rapids and searched it without a warrant, finding 68 bottles of liquor concealed behind the upholstery. Carroll was convicted of transporting intoxicating liquor and challenged the warrantless search. ## Issue Whether officers with probable cause may search a moving vehicle for contraband without first obtaining a warrant. ## Rule Yes. The Court distinguished fixed premises from vehicles: there is", "quote_fidelity": "mismatch", "record_id": "Carroll v. United States", "star_marker": null}}
{"assertion_id": "8c8befd131e4418c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Carroll v. United States"}, "payload": {"as_of_content": "1925-03-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Carroll v. United States", "scope_note": "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law.", "varies_by_point": false}}
```

### lake record — Carroll v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carroll v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Carroll v. United States",
    "case_name_short": "Carroll",
    "case_name_full": "Carroll Et Al. v. United States",
    "input_case_name": "Carroll v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1925-11-26",
    "year": 1925,
    "docket": null,
    "cluster_id": 100567,
    "lead_opinion_id": 100567,
    "sibling_ids": [
      100567,
      9418540,
      9418541
    ],
    "absolute_url": "/opinion/100567/carroll-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "267 U.S. 132",
      "volume": "267",
      "reporter": "U.S.",
      "page": "132",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "45 S. Ct. 280",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 543",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1925 U.S. LEXIS 361",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "361",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "267 U.S. 132",
        "volume": "267",
        "reporter": "U.S.",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 S. Ct. 280",
        "volume": "45",
        "reporter": "S. Ct.",
        "page": "280",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 L. Ed. 543",
        "volume": "69",
        "reporter": "L. Ed.",
        "page": "543",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1925 U.S. LEXIS 361",
        "volume": "1925",
        "reporter": "U.S. LEXIS",
        "page": "361",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "267 U.S. 132",
    "official_selection": {
      "court_class": "scotus",
      "selected": "267 U.S. 132",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-p37",
      "page": null,
      "quote": "--- # Carroll v. United States *267 U.S. 132 (1925)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During Prohibition, federal agents who had probable cause to believe Carroll and a companion were transporting bootleg liquor stopped their automobile on a highway between Detroit and Grand Rapids and searched it without a warrant, finding 68 bottles of liquor concealed behind the upholstery. Carroll was convicted of transporting intoxicating liquor and challenged the warrantless search. ## Issue Whether officers with probable cause may search a moving vehicle for contraband without first obtaining a warrant. ## Rule Yes. The Court distinguished fixed premises from vehicles: there is",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1925-03-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Carroll v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the automobile exception; repeatedly reaffirmed and refined (Chambers, Ross, Carney, Acevedo). Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane1_negative"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brinegar v. United States",
          "cluster_id": 104716,
          "cite": [
            "93 L. Ed. 2d 1879",
            "69 S. Ct. 1302",
            "338 U.S. 160",
            "1949 U.S. LEXIS 2084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Carroll v. United States:lane2_top_cited"
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
        "journal_ref": "Carroll v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100567 OR 9418540 OR 9418541) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMyMDQ0ODAwMDAwJnM9NDUxODk5MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100567+OR+9418540+OR+9418541%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(100567 OR 9418540 OR 9418541)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDgwJnM9MTA0NzY5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28100567+OR+9418540+OR+9418541%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(100567 OR 9418540 OR 9418541)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 1,
        "triage_snippet_classified": 76
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(100567 OR 9418540 OR 9418541)",
    "indexed_citing_opinions": 4916,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100567,
        "count": 4498,
        "count_source": "search"
      },
      {
        "opinion_id": 9418540,
        "count": 536,
        "count_source": "search"
      },
      {
        "opinion_id": 9418541,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7455,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/carroll-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMjIxMTYmcz0xMDM4ODk1NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28100567+OR+9418540+OR+9418541%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100567,
        "cited_id": 85007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 85121,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 86221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 87693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 90759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 95241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 100265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 5560847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100567,
        "cited_id": 6236987,
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
    "date_created": "2026-07-04T23:40:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:43:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:41:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Carroll v. United States

```
<p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U.S. 132</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">45 S.Ct. 280</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">69 L.Ed. 543</a></span></p>
    <p class="parties">CARROLL et al.<br>v.<br>UNITED STATES.</p>
    <p class="docket">No. 15.</p>
    <p class="date">Reargued and Submitted March 14, 1924.</p>
    <p class="date">Decided March 2, 1925.</p>
    <div class="prelims">
      <p class="indent">[Syllabus and Statement of the Case from pages 132-136 intentionally omitted]</p>
      <p class="indent">Messrs. Thomas E. Atkinson and Clare J. Hall, both of Grand Rapids, Mich., for plaintiffs in error.</p>
      <p class="indent">[Argument of Counsel from pages 136-143 intentionally omitted]</p>
      <p class="indent">The Attorney General and Mr. James M. Beck, Sol. Gen., of Washington, D. C., for the United States.</p>
      <p class="indent">Mr. Chief Justice TAFT, after stating the case as above, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The constitutional and statutory provisions involved in this case include the Fourth Amendment and the National Prohibition Act.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">The Fourth Amendment is in part as follows:</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">'The right of the people to be secure in their persons,      houses, papers and effects against unreasonable searches and      seizures shall not be violated, and no warrants shall issue      but upon probable cause, supported by oath or affirmation,      and particularly describing the place to be searched, and the      persons or things to be seized.'</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">Section 25, title 2, of the National Prohibition Act, c. 85, <span class="citation no-link">41 Stat. 305</span>, 315, passed to enforce the Eighteenth Amendment, makes it unlawful to have or possess any liquor intended for use in violating the act, or which has been so used, and provides that no property rights shall exist in such inquor. A search warrant may issue and such liquor, with the containers thereof, may be seized under the warrant and be ultimately destroyed. The section further provides:</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">'No search warrant shall issue to search any private dwelling      occupied as such unless it is being used for the unlawful      sale of intoxicating liquor, or unless it is in part used for      some business purpose such as a store, shop, saloon,      restaurant, hotel, or boaring house. The term 'private      dwelling' shall be construed to include the room or rooms      used and occupied not transiently but solely as a residence in an apartment house, hotel, or boarding house.'</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Section 26, title 2, under which the seizure herein was made, provides in part as follows:</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">'When the commissioner, his assistants, inspectors, or any      officer of the law shall discover any person in the act of      transporting in violation of the law, intoxicating liquors in      any wagon, buggy, automobile, water or air craft, or other      vehicle, it shall be his duty to seize any and all      intoxicating liquors found therein being transported contrary      to law. Whenever intoxicating liquors transported or      possessed illegally shall be seized by an officer he shall      take possession of the vehicle and team or automobile, boat,      air or water craft, or any other conveyance, and shall arrest      any person in charge thereof.'</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">The section then provides that the court upon conviction of the person so arrested shall order the liquor destroyed, and except for good cause shown shall order a sale by public auction of the other property seized, and that the proceeds shall be paid into the Treasury of the United States.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">By section 6 of an act supplemental to the National Prohibition Act (<span class="citation no-link">42 Stat. 222</span>, 223, c. 134 [Comp. St. Ann. Supp. 1923, &#167; 10184a]) it is provided that if any officer or agent or employee of the United States engaged in the enforcement of the Prohibition Act or this Amendment, 'shall search any private dwelling,' as defined in that act, 'without a warrant directing such search,' or 'shall without a search warrant maliciously and without reasonable cause search any other building or property,' he shall be guilty of a misdemeanor and subject to fine or imprisonment or both.</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">In the passage of the supplemental act through the Senate, amendment No. 32, known as the Stanley Amendment, was adopted, the relevant part of which was as follows:</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">'Sec. 6. That any officer, agent or employee of the United      States engaged in the enforcement of this act or the National Prohibition Act, or any other law of the United      States, who shall search or attempt to search the property or      premises of any person without previously securing a search      warrant, as provided by law, shall be guilty of a misdemeanor      and upon conviction thereof shall be fined not to exceed      $1,000, or imprisoned not to exceed one year, or both so      fined and imprisoned in the discretion of the court.'</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">This amendment was objected to in the House, and the judiciary committee, to whom it was referred, reported to the House of Representatives the following as a substitute:</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">'Sec. 6. That no officer, agent or employee of the United      States, while engaged in the enforcement of this act, the      National Prohibition Act, or any law in reference to the      manufacture or taxation of, or traffic in, intoxicating      liquor, shall search any private dwelling without a warrant      directing such search, and no such warrant shall issue unless      there is reason to believe such dwelling is used as a place      in which liquor is manufactured for sale or sold. The term      'private dwelling' shall be construed to include the room or      rooms occupied not transiently, but solely as a residence in      an apartment house, hotel, or boarding house. Any violation      of any provision of this paragraph shall be punished by a      fine of not to exceed $1,000 or imprisonment not to exceed      one year, or both such fine and imprisonment, in the      discretion of the court.'</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">In its report the committee spoke in part as follows:</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">'It appeared to the committee that the effect of the Senate      amendment No. 32, if agreed to by the House, would greatly      cripple the enforcement of the National Prohibition Act and      would otherwise seriously interfere with the government in      the enforcement of many other laws, as its scope is not      limited to the prohibition law, but applies equally to all laws where prompt action is      necessary. There are on the statute books of the United      States a number of laws authorizing search without a search      warrant. Under the common law and agreeable to the      Constitution search may in many cases be legally made without      a warrant. The Constitution does not forbid search, as some      parties contend, but it does forbid unreasonable search. This      provision in regard to search is as a rule contained in the      various state Constitutions, but notwithstanding that fact      search without a warrant is permitted in many cases, and      especially is that true in the enforcement of liquor      legislation.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">'The Senate amendment prohibits all search or attempt to      search any property or premises without a search warrant. The      effect of that would necessarily be to prohibit all search,      as no search can take place if it is not on some property or      premises.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">'Not only does this amendment prohibit search of any lands      but it prohibits the search of all property. It will prevent      the search of the common bootlegger and his stock in trade,      though caught and arrested in the act of violating the law.      But what is perhaps more serious, it will make it impossible      to stop the rum-running automobiles engaged in like illegal      traffic. It would take from the officers the power that they      absolutely must have to be of any service, for if they cannot      search for liquor without a warrant they might as well be      discharged. It is impossible to get a warrant to stop an      automobile. Before a warrant could be secured the automobile      would be beyond the reach of the officer with its load of      illegal liquor disposed of.'</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">The conference report resulted, so far as the difference between the two houses was concerned, in providing for the punishment of any officer, agent, or employee of the government who searches a 'private dwelling' without a warrant, and for the punishment of any such officer, etc., who searches any 'other building or property' where, and only where, he makes the search without a warrant 'maliciously and without probable cause.' In other words, it left the way open for searching an automobile or vehicle of transportation without a warrant, if the search was not malicious or without probable cause.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">The intent of Congress to make a distinction between the necessity for a search warrant in the searching of private dwellings and in that of automobiles and other road vehicles in the enforcement of the Prohibition Act is thus clearly established by the legislative history of the Stanley Amendment. Is such a distinction consistent with the Fourth Amendment? We think that it is, The Fourth Amendment does not denounce all searches or seizures, but only such as are unreasonable.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">The leading case on the subject of search and seizure is Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S. Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L. Ed. 746</a></span>. An Act of Congress of June 22, 1874 (<span class="citation no-link">18 Stat. 187</span>), authorized a court of the United States in revenue cases, on motion of the government attorney, to require the defendant to produce in court his private books, invoices, and papers on pain in case of refusal of having the allegations of the attorney in his motion taken as confessed. This was held to be unconstitutional and void as applied to suits for penalties or to establish a forfeiture of goods, on the ground that under the Fourth Amendment the compulsory production of invoices to furnish evidence for forfeiture of goods constituted an unreasonable search even where made upon a search warrant, and was also a violation of the Fifth Amendment, in that it compelled the defendant in a criminal case to produce evidence against himself or be in the attitude of confessing his guilt.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">In Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177, it was held that a court in a criminal prosecution could not retain letters of the accused seized in his house, in his absence and without his authority, by a United States marshal holding no warrant for his arrest and none for the search of his premises, to be used as evidence against him, the accused having made timely application to the court for an order for the return of the letters.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">In Silverthorne Lumber Co. v. United States, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">40 S. Ct. 182</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">64 L. Ed. 319</a></span>, a writ of error was brought to reverse a judgment of contempt of the District Court, fining the company and imprisoning one Silverthorne, its president, until he should purge himself of contempt in not producing books and documents of the company before the grand jury to prove violation of the statutes of the United States by the company and Silverthorne. Silverthorne had been arrested, and while under arrest the marshal had gone to the office of the company without a warrant and made a clean sweep of all books, papers, and documents found there and had taken copies and photographs of the papers. The District Court ordered the return of the originals, but impounded the photographs and copies. This was held to be an unreasonable search of the property and possessions of the corporation and a violation of the Fourth Amendment and the judgment for contempt was reversed.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">In Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S. Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L. Ed. 647</a></span>, the obtaining through stealth by a representative of the government from the office of one suspected of defrauding the government of a paper which had no pecuniary value in itself, but was only to be used as evidence against its owner, was held to be a violation of the Fourth Amendment. It was further held that when the paper was offered in evidence and duly objected to it must be ruled inadmissible because obtained through an unreasonable search and seizure and also in violation of the Fifth Amendment because working compulsory incrimination.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">In Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S. Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L. Ed. 654</a></span>, it was held that where concealed liquor was found by government officers without a search warrant in the home of the defendant, in his absence, and after a demand made upon his wife, it was inadmissible as evidence against the defendant, because acquired by an unreasonable seizure.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">In none of the cases cited is there any ruling as to the validity under the Fourth Amendment of a seizure without a warrant of contraband goods in the course of transportation and subject to forfeiture or destruction.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">On reason and authority the true rule is that if the search and seizure without a warrant are made upon probable cause, that is, upon a belief, reasonably arising out of circumstaces known to the seizing officer, that an automobile or other vehicle contains that which by law is subject to seizure and destruction, the search and seizure are valid. The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens.</p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">In Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S. Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L. Ed. 746</a></span>, as already said, the decision did not turn on whether a reasonable search might be made without a warrant; but for the purpose of showing the principle on which the Fourth Amendment proceeds, and to avoid any misapprehension of what was decided, the court, speaking through Mr. Justice Bradley, used language which is of particular significance and applicability here. It was there said (page 623 [<span class="citation no-link">6 S. Ct. 528</span>]):</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">'The search for and seizure of stolen or forfeited goods, or      goods liable to duties and concealed to avoid the payment      thereof, are totally different things from a search for and      seizure of a man's private books and papers for the purpose      of obtaining information therein contained, or of using them      as evidence against him. The two things differ toto coelo. In      the one case, the government is entitled to the possession of      the property; in the other it is not. The seizure of stolen      goods is authorized by the common law; and the seizure of goods forfeited for a breach      of the revenue laws, or concealed to avoid the duties payable      on them, has been authorized by English statutes for at least      two centuries past; and the like seizures have been      authorized by our own revenue acts from the commencement of      the government. The first statute passed by Congress to      regulate the collection of duites, the Act of July 31, 1789,      <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this      act was passed by the same Congress which proposed for      adoption the original amendments to the Constitution, it is      clear that the members of that body did not regard searches      and seizures of this kind as 'unreasonable,' and they are not      embraced within the prohibition of the amendment. So, also,      the supervision authorized to be exercised by officers of the      revenue over the manufacture or custody of excisable      articles, and the entries thereof in books required by law to      be kept for their inspection, are necessarily excepted out of      the category of unreasonable searches and seizures. So, also,      the laws which provide for the search and seizure of articles      and things which it is unlawful for a person to have in his      possession for the purpose of issue or disposition, such as      counterfeit coin, lottery tickets, implements of gambling,      etc., are not within this category. Common-welath v. Dana, 2      Metc. (Mass.) 329. Many other things of this character might      be enumerated.'</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">It is noteworthy that the twenty-fourth section of the act of 1789 to which the court there refers provides:</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">'That every collector, naval officer and surveyor, or other      person specially appointed by either of them for that      purpose, shall have full power and authority, to enter any      ship or vessel, in which they shall have reason to suspect      any goods, wares or merchandise subject to duty shall be      concealed; and therein to search for, seize, and secure any      such goods, wares or merchandise; and if they shall have      cause to suspect a concealment thereof, in any particular dwelling house, store, building, or other place,      they or either of them shall, upon application on oath or      affirmation to any justice of the peace, be entitled to a      warrant to enter such house, store, or other place (in the      daytime only) and there to search for such goods, and if any      shall be found, to seize and secure the same for trial; and      all such goods, wares and merchandise, on which the duties      shall not have been paid or secured, shall be forfeited.' <span class="citation no-link">1      Stat. 43</span>.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">Like provisions were contained in the Act of August 4, 1790, c. 35, &#167;&#167; 48-51, <span class="citation no-link">1 Stat. 145</span>, 170; in section 27 of the Act of February 18, 1793, c. 8, <span class="citation no-link">1 Stat. 305</span>, 315; and in sections 68-71 of the Act of March 2, 1799, c. 22, <span class="citation no-link">1 Stat. 627</span>, 677, 678.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">Thus contemporaneously with the adoption of the Fourth Amendment we find in the First Congress, and in the following Second and Fourth Congresses, a difference made as to the necessity for a search warrant between goods subject to forfeiture, when concealed in a dwelling house or similar place, and like goods in course of transportation and concealed in a movable vessel where they readily could be put out of reach of a search warrant. Compare Hester v. United States, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">44 S. Ct. 445</a></span>, <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">68 L. Ed. 898</a></span>.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">Again, by the second section of the Act of March 3, 1815, <span class="citation no-link">3 Stat. 231</span>, 232, it was made lawful for customs officers, not only to board and search vessels within their own and adjoining districts, but also to stop, search, and examine any vehicle, beast, or person on which or whom they should suspect there was merchandise which was subject to duty or had been introduced into the United States in any manner contrary to law, whether by the person in charge of the vehicle or beast or otherwise, and if they should find any goods, wares or merchandise thereon, which they had probable cause to believe had been so unlawfully brought into the country, to seize and secure the same, and the vehicle or beast as well, for trial and forfeiture. This act was renewed April 27, 1816 (<span class="citation no-link">3 Stat. 315</span>), for a year and expired. The Act of February 28, 1865, revived section 2 of the Act of 1815, above described, <span class="citation no-link">13 Stat. 441</span>, c. 67. The substance of this section was re-enacted in the third section of the Act of July 18, 1866, c. 201, <span class="citation no-link">14 Stat. 178</span>, and was thereafter embodied in the Revised Statutes as section 3061 (Comp. St. &#167; 5763). Neither section 3061 nor any of its earlier counterparts has ever been attacked as unconstitutional. Indeed, that section was referred to and treated as operative by this court in Cotzhausen v. Nazro, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/#219" aria-description="Citation for case: Cotzhausen v. Nazro">107 U. S. 215, 219</a></span>, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">2 S. Ct. 503</a></span>, <span class="citation" data-id="90759"><a href="/opinion/90759/cotzhausen-v-nazro/" aria-description="Citation for case: Cotzhausen v. Nazro">27 L. Ed. 540</a></span>. See, also, United States v. One Black Horse (D C.) <span class="citation" data-id="8754123"><a href="/opinion/8770588/united-states-v-one-black-horse/" aria-description="Citation for case: United States v. One Black Horse">129 F. 167</a></span>.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">Again by section 2140 of the Revised Statutes (Comp. St. &#167; 4141) any Indian agent, subagent or commander of a military post in the Indian country, having reason to suspect or being informed that any white person or Indian is about to introduce, or has introduced, any spirituous liquor or wine into the Indian country, in violation of law, may cause the boats, stores, packages, wagons, sleds and places of deposit of such person to be searched and if any liquor is found therein, then it, together with the vehicles, shall be seized and and proceeded against by libel in the proper court and forfeited. Section 2140 was the outgrowth of the Act of May 6, 1822, c. 58, <span class="citation no-link">3 Stat. 682</span>, authorizing Indian agents to cause the goods of traders in the Indian country to be searched upon suspicion or information that ardent spirits were being introduced into the Indian country to be seized and forfeited if found, and of the Act of June 30, 1834, &#167; 20, c. 161, <span class="citation no-link">4 Stat. 729</span>, 732, enabling an Indian agent having reason to suspect any person of having introduced or being about to introduce liquors into the Indian country to cause the boat, stores or places of deposit of such person to be searched and the liquor found forfeited. This court recognized the statute of 1822 as justifying such a search and seizure in American Fur Co. v. United States, <span class="citation" data-id="85637"><a href="/opinion/85637/sundry-goods-wares-merchandises-v-united-states/" aria-description="Citation for case: Sundry Goods, Wares &amp; Merchandises v. United States">2 Pet. 358</a></span>, <span class="citation" data-id="85637"><a href="/opinion/85637/sundry-goods-wares-merchandises-v-united-states/" aria-description="Citation for case: Sundry Goods, Wares &amp; Merchandises v. United States">7 L. Ed. 450</a></span>. By the Indian Appropriation Act of March 2, 1917, c. 146, <span class="citation no-link">39 Stat. 969</span>, 970, automobiles used in introducing or attempting to introduce intoxicants into the Indian territory may be seized, libeled, and forfeited as provided in the Revised Statutes, &#167; 2140.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">And again in Alaska, by section 174 of the Act of March 3, 1899, c. 429, <span class="citation no-link">30 Stat. 1253</span>, 1280, it is provided that collectors and deputy collectors or any person authorized by them in writing shall be given power to arrest persons and seize vessels and merchandise in Alaska liable to fine, penalties, or forfeiture under the act and to keep and deliver the same, and the Attorney General, in construing the act, advised the government:</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">'If your agents reasonably suspect that a violation of law      has occurred, in my opinion they have power to search any      vessel within the three-mile limit according to the practice      of customs officers when acting under section 3059 of the      Revised Statutes [Comp. St. &#167; 5761], and to seize such      vessels.' 26 Op. Attys. Gen. 243.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">We have made a somewhat extended reference to these statutes to show that the guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the government, as recognizing a necessary difference between a search of a store, dwelling house, or other structure in respect of which a proper official warrant readily may be obtained and a search of a ship, motor boat, wagon, or automobile for contraband goods, where it is not practicable to secure a warrant, because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">Having thus established that contraband goods concealed and illegally transported in an automobile or other vehicle may be searched for without a warrant, we come now to consider under what circumstances such search may be made. It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor, and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travelers may be so stopped in crossing an international boundary because of national self-protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is known to a competent official, authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise. Section 26, title 2, of the National Prohibition Act, like the second section of the act of 1789, for the searching of vessels, like the provisions of the act of 1815, and section 3601, Revised Statutes, for searching vehicles for smuggled goods, and like the act of 1822, and that of 1834 and section 2140, R. S., and the act of 1917 for the search of vehicles and automobiles for liquor smuggled into the Indian country, was enacted primarily to accomplish the seizure and destruction of contraband goods; secondly, the automobile was to be forfeited; and, thirdly, the driver was to be arrested. Under section 29, title 2, of the act the latter might be punished by not more than $500 fine for the first offense, not more than $1,000 fine and 90 days' imprisonment for the second offense, and by a fine of $500 or more and by not more than 2 years' imprisonment for the third offense. Thus he is to be arrested for a misdemeanor for his first and second offenses, and for a felony if he offends the third time.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">The main purpose of the act obviously was to deal with the liquor and its transportation, and to destroy it. The mere manufacture of liquor can do little to defeat the policy of the Eighteenth Amendment and the Prohibition Act, unless the for bidden product can be distributed for illegal sale and use. Section 26 was intended to reach and destroy the forbidden liquor in transportation and the provisions for forfeiture of the vehicle and the arrest of the transporter were incidental. The rule for determining what may be required before a seizure may be made by a competent seizing official is not to be determined by the character of the penalty to which the transporter may be subjected. Under section 28, title 2, of the Prohibition Act, the Commissioner of Internal Revenue, his assistants, agents and inspectors are to have the power and protection in the enforcement of the act conferred by the existing laws relating to the manufacture or sale of intoxicating liquors. Officers who seize under section 26 of the Prohibition Act are therefore protected by section 970 of the Revised Statutes (Comp. St. &#167; 1611), providing that:</p>
    </div>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">'When, in any prosecution commenced on account of the seizure      of any vessel, goods, wares, or merchandise, made by any      collector or other officer, under any act of Congress      authorizing such seizure, judgment is rendered for the      claimant, but it appears to the court that there was      reasonable cause of seizure, the court shall cause a proper      certificate thereof to be entered, and the claimant shall      not, in such case, be entitled to costs, nor shall the person      who made the seizure, nor the prosecutor, be liable to suit      or judgment on account of such suit or prosecution: Provided,      that the vessel, goods, wares, or merchandise be, after      judgment, forthwith returned to such claimant or his agent.'</p>
    </div>
    <div class="num" id="p41">
      <span class="num">41</span>
      <p class="indent">It follows from this that, if an officer seizes an autombile or the liquor in it without a warrant, and the facts as subsequently developed do not justify a judgment of condemnation and forfeiture, the officer may escape costs or a suit for damages by a showing that he had reasonable or probable cause for the seizure. Stacey v. Emery, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642</a></span>, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">24 L. Ed. 1035</a></span>. The measure of legality of such a seizure is, therefore, that the seizing officer shall have reasonable or probable cause for believing that the antomobile which he stops and seizes has contraband liquor therein which is being illegally transported.</p>
    </div>
    <div class="num" id="p42">
      <span class="num">42</span>
      <p class="indent">We here find the line of distrinction between legal and illegal seizures of liquor in transport in vehicles. It is certainly a reasonable distinction. It gives the owner of an automobile or other vehicle seized under section 26, in absence of probable cause, a right to have restored to him the automobile, it protects him under the Weeks and Amos Cases from use of the liquor as evidence against him, and it subjects the officer making the seizures to damages. On the other hand, in a case showing probalbe cause, the government and its officials are given the opportunity which they should have, to make the investigation necessary to trace reasonably suspected contraband goods and to seize them.</p>
    </div>
    <div class="num" id="p43">
      <span class="num">43</span>
      <p class="indent">Such a rule fulfills the guaranty of the Fourth Amendment. In cases where the securing of a warrant is reasonably practicable, it must be used and when properly supported by affidavit and issued after judicial approval protects the seizing officer against a suit for damages. In cases where seizure is impossible except without warrant, the seizing officer acts unlawfully and at his peril unless he can show the court probable cause. United States v. Kaplan (D. C.) <span class="citation" data-id="8829037"><a href="/opinion/8843816/united-states-v-kaplan/#972" aria-description="Citation for case: United States v. Kaplan">286 F. 963, 972</a></span>.</p>
    </div>
    <div class="num" id="p44">
      <span class="num">44</span>
      <p class="indent">But we are pressed with the argument that if the search of the automobile discloses the presence of liquor and leads under the staute to the arrest of the person in charge of the automobile, the right of seizure should be limited by the common-law rule as to the circumstances justifying an arrest without a warrant for a misdemeanor. The usual rule is that a police officer may arrest without warrant one believed by the officer upon reasonable cause to have been guilty of a felony, and that he may only arrest without a warrant one guilty of a misdemeanor if committed in his presence. Kurtz v. Moffitt, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">6 S. Ct. 148</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">29 L. Ed. 458</a></span>; John Bad Elk v. United States, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">20 S. Ct. 729</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">44 L. Ed. 874</a></span>. The rule is sometimes expressed as follows:</p>
    </div>
    <div class="num" id="p45">
      <span class="num">45</span>
      <p class="indent">'In cases of misdemeanor, a peace officer like a private      person has at common law no power of arresting without a      warrant except when a breach of the peace has been committed      in his presence or there is reasonable ground for supposing      that a breach of peace is about to be committed or renewed in      his presence.' Halsbury's Laws of England, vol. 9, part. III,      612.</p>
    </div>
    <div class="num" id="p46">
      <span class="num">46</span>
      <p class="indent">The reason for arrest for misdemeanors without warrant at common law was promptly to suppress breaches of the peace (1 Stephen, History of Criminal Law, 193), while the reason for arrest without warrant on a reliable report of a felony was because the public safety and the due apprehension of criminals charged with heinous offenses required that such arrests should be made at once without warrant (Rohan v. Sawin, 5 Cush. [Mass.] 281). The argument for defendants is that, as the misdemeanor to justify arrest without warrant must be committed in the presence of the police officer, the offense is not committed in his presence unless he can by his senses detect that the liquor is being transported, no matter how reliable his previous information by which he can identify the automobile as loaded with it. Elrod v. Moss (C. C. A.) <span class="citation" data-id="8823999"><a href="/opinion/8838892/elrod-v-moss/" aria-description="Citation for case: Elrod v. Moss">278 F. 123</a></span>; Hughes v. State, <span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span>, 20 A. L. R. 639.</p>
    </div>
    <div class="num" id="p47">
      <span class="num">47</span>
      <p class="indent">So it is that under the rule contended for by defendants the liquor if carried by one who has been already twice convicted of the same offense may be seized on information other than the senses, while if he has been only once convicted it may not be seized unless the presence of the liquor is detected by the senses as the automobile concealing it rushes by. This is certainly a very unsatisfactory line of difference when the main object of the section is to forfeit and suppress the liquor, the arrest of the individual being only incidental as shown by the lightness of the penalty. See Commonwealth v. Street, 3 Pa. Dist. and Co. Ct. Rep.783. In England at the common law the difference in punishment between felonies and misdemeanors was very great. Under our present federal statutes, it is much less important and Congress may exercise a relatively wide discretion in classing particular offenses as felonies or misdemeanors. As the main purpose of section 26 was seizure and forfeiture, it is not so much the owner as the property that offends. Agnew v. Haymes, <span class="citation" data-id="8758980"><a href="/opinion/8775358/agnew-v-haymes/#641" aria-description="Citation for case: Agnew v. Haymes">141 F. 631, 641</a></span>, <span class="citation" data-id="8758980"><a href="/opinion/8775358/agnew-v-haymes/" aria-description="Citation for case: Agnew v. Haymes">72 C. C. A. 325</a></span>. The language of the section provides for seizure when the officer of the law 'discovers' any one in the act of transporting the liquor by automobile or other vehicle. Certainly it is a very narrow and technical construction of this word which would limit it to what the officer sees, hears or smells as the automobile rolls by and excludes therefrom when he identifies the car the convincing information that he may previously have received as to the use being made of it.</p>
    </div>
    <div class="num" id="p48">
      <span class="num">48</span>
      <p class="indent">We do not think such a nice distinction is applicable in the present case. When a man is legally arrested for an offense, whatever is found upon his person or in his control which it is unlawful for him to have and which may be used to prove the offense may be seized and held as evidence in the prosecution. Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177; Dillon v. O'Brien and Davis, 16 Cox, C. C. 245; Getchell v. Page, <span class="citation" data-id="4937159"><a href="/opinion/5118454/getchell-v-page/" aria-description="Citation for case: Getchell v. Page">103 Me. 387</a></span>, <span class="citation" data-id="4937159"><a href="/opinion/5118454/getchell-v-page/" aria-description="Citation for case: Getchell v. Page">69 A. 624</a></span>, 18 L. R. A. (N. S.) 253, <span class="citation no-link">125 Am. St. Rep. 307</span>; Kneeland v. Connally, <span class="citation" data-id="5560847"><a href="/opinion/5710842/kneeland-v-connally/" aria-description="Citation for case: Kneeland v. Connally">70 Ga. 424</a></span>; 1 Bishop, Criminal Procedure, &#167; 211; 1 Wharton, Criminal Procedure (10th Ed.) &#167; 97. The argument of defendants is based on the theory that the seizure in this case can only be thus justified. If their theory were sound, their conclusion would be. The validity of the seizure then would turn wholly on the validity of the arrest without a seizure. But the theory is unsound. The right to search and the validity of the seizure are not dependent on the right to arrest. They are dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law. The seizure in such a proceeding comes before the arrest as section 26 indicates. It is true that section 26, title 2, provides for immediate proceedings against the person arrested and that upon conviction the liquor is to be destroyed and the automobile or other vehicle is to be sold, with the saving of the interest of a lienor who does not know of its unlawful use; but it is evident that if the person arrested is ignorant of the contents of the vehicle, or if he escapes, proceedings can be had against the liquor for destruction or other disposition under section 25 of the same title. The character of the offense for which, after the contraband liquor is found and seized, the driver can be prosecuted does not affect the validity of the seizure.</p>
    </div>
    <div class="num" id="p49">
      <span class="num">49</span>
      <p class="indent">This conclusion is in keeping with the requirements of the Fourth Amendment and the principles of search and seizure of contraband forfeitable property; and it is a wise one because it leaves the rule one which is easily applied and understood and is uniform. Houck v. State, <span class="citation no-link">106 Ohio St. 195</span>, <span class="citation no-link">140 N. E. 112</span>, accords with this conclusion. Ash v. United States (C. C. A.) <span class="citation" data-id="9335932"><a href="/opinion/9340588/ash-v-states/" aria-description="Citation for case: Ash v. States">299 F. 277</a></span>, and Milam v. United States (C. C. A.) <span class="citation" data-id="8835196"><a href="/opinion/8849836/milam-v-united-states/" aria-description="Citation for case: Milam v. United States">296 F. 629</a></span>, decisions by the Circuit Court of Appeals for the Fourth Circuit take the same view. The Ash Case is very similar in its facts to the case at bar, and both were by the same court which decided Snyder v. United States (C. C. A.) <span class="citation" data-id="8828212"><a href="/opinion/8843002/snyder-v-united-states/" aria-description="Citation for case: Snyder v. United States">285 F. 1</a></span>, cited for the defendants. See, also, Park v. United States (1st C. C. A.) <span class="citation" data-id="8833538"><a href="/opinion/8848214/park-v-united-states/#783" aria-description="Citation for case: Park v. United States">294 F. 776, 783</a></span>, and Lambert v. United States (9th C. C. A.) <span class="citation" data-id="8826550"><a href="/opinion/8841368/lambert-v-united-states/" aria-description="Citation for case: Lambert v. United States">282 F. 413</a></span>.</p>
    </div>
    <div class="num" id="p50">
      <span class="num">50</span>
      <p class="indent">Finally, was there probable cause? In The Apollon, <span class="citation" data-id="85416"><a href="/opinion/85416/the-apollon/" aria-description="Citation for case: The Apollon.">9 Wheat. 362</a></span>, <span class="citation" data-id="85416"><a href="/opinion/85416/the-apollon/" aria-description="Citation for case: The Apollon.">6 L. Ed. 111</a></span>, the question was whether the seizure of a French vessel at a particular place was upon probable cause that she was there for the purpose of smuggling. In this discussion Mr. Justice Story, who delivered the judgment of the court, said (page 374):</p>
    </div>
    <div class="num" id="p51">
      <span class="num">51</span>
      <p class="indent">'It has been very justly observed at the bar that the court      is bound to take notice of public facts and geographical positions, and that this remote part of the country has been      infested, at different periods, by smugglers, is matter of      general notoriety, and may be gathered from the public      documents of the government.'</p>
    </div>
    <div class="num" id="p52">
      <span class="num">52</span>
      <p class="indent">We know in this way that Grand Rapids is about 152 miles from Detroit, and that Detroit and its neighborhood along the Detroit river, which is the international boundary, is one of the most active centers for introducing illegally into this country spirituous liquors for distribution into the interior. It is obvious from the evidence that the prohibition agents were engaged in a regular patrol along the important highways from Detroit to Grand Rapids to stop and seize liquor carried in automobiles. They knew or had convincing evidence to make them believe that the Carroll boys, as they called them, were so-called 'bootleggers' in Grand Rapids; i. e., that they were engaged in plying the unlawful trade of selling such liquor in that city. The officers had soon after noted their going from Grand Rapids half way to Detroit, and attempted to follow them to that city to see where they went, but they escaped observation. Two months later these officers suddenly met the same men on their way westward presumably from Detroit. The partners in the original combination to sell liquor in Grand Rapids were together in the same automobile they had been in the night when they tried to furnish the whisky to the officers, which was thus identified as part of the firm equipment. They were coming from the direction of the great source of supply for their stock to Grand Rapids, where they plied their trade. That the officers, when they saw the defendants, believed that they were carrying liquor, we can have no doubt, and we think it is equally clear that they had reasonable cause for thinking so. Emphasis is put by defendants' counsel on the statement made by one of the officers that they were not looking for defendants at the particular time when they appeared. We do not perceive that it has any weight. As soon as they did appear, the officers were entitled to use their reasoning faculties upon all the facts of which they had previous knowledge in respect to the defendants.</p>
    </div>
    <div class="num" id="p53">
      <span class="num">53</span>
      <p class="indent">The necessity for probable cause in justifying seizures on land or sea, in making arrests without warrant for past felonies, and in malicious prosecution and false imprisonment cases has led to frequent definition of the phrase. In Stacey v. Emery, <span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (<span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/" aria-description="Citation for case: Stacey v. Emery">24 L. Ed. 1035</a></span>), a suit for damages for seizure by a collector, this court defined probable cause as follows:</p>
    </div>
    <div class="num" id="p54">
      <span class="num">54</span>
      <p class="indent">'If the facts and circumstances before the officer are such      as to warrant a man of prudence and caution in believing that      the offense has been committed, it is sufficient.'</p>
    </div>
    <div class="num" id="p55">
      <span class="num">55</span>
      <p class="indent">See Locke v. United States, <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">7 Cranch, 339</a></span>, <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/" aria-description="Citation for case: Locke v. United States">3 L. Ed. 364</a></span>; The George, <span class="citation" data-id="8631556"><a href="/opinion/8651731/the-george/" aria-description="Citation for case: The George">1 Mason, 24</a></span>, Fed. Cas. No. 5328; The Thompson, <span class="citation" data-id="87693"><a href="/opinion/87693/the-thompson/" aria-description="Citation for case: The Thompson">3 Wall. 155</a></span>, <span class="citation" data-id="87693"><a href="/opinion/87693/the-thompson/" aria-description="Citation for case: The Thompson">18 L. Ed. 55</a></span>.</p>
    </div>
    <div class="num" id="p56">
      <span class="num">56</span>
      <p class="indent">It was laid down by Chief Justice Shaw, in Commonwealth v. Carey, <span class="citation no-link">12 Cush. 246</span>, 251, that:</p>
    </div>
    <div class="num" id="p57">
      <span class="num">57</span>
      <p class="indent">'If a constable or other peace officer arrest a person      without a warrant, he is not bound to show in his      justification a felony actually committed, to render the      arrest lawful; but if he suspects one on his own knowledge of      facts, or on facts communicated to him by others, and      thereupon he has reasonable ground to believe that the      accused has been guilty of felony, the arrest is not      unlawful.' Commonwealth v. Phelps, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">209 Mass. 396</a></span>, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">95 N. E.      868</a></span>, Ann. Cas. 1912B, 566; Rohan v. Sawin, <span class="citation no-link">5 Cush. 281</span>, 285.</p>
    </div>
    <div class="num" id="p58">
      <span class="num">58</span>
      <p class="indent">In McCarthy v. De Armit, <span class="citation" data-id="6236987"><a href="/opinion/6368121/mccarthy-v-de-armit/" aria-description="Citation for case: McCarthy v. De Armit">99 Pa. 63</a></span>, the Supreme Court of Pennsylvania sums up the definition of probable cause in this way (page 69):</p>
    </div>
    <div class="num" id="p59">
      <span class="num">59</span>
      <p class="indent">'The substance of all the definitions is a reasonable ground      for belief of guilt.'</p>
    </div>
    <div class="num" id="p60">
      <span class="num">60</span>
      <p class="indent">In the case of the Director General v. Kastenbaum, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">263 U. S. 25</a></span>, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">44 S. Ct. 52</a></span>, <span class="citation" data-id="100265"><a href="/opinion/100265/director-general-of-railroads-v-kastenbaum/" aria-description="Citation for case: Director General of Railroads v. Kastenbaum">68 L. Ed. 146</a></span>, which was a suit for false imprisonment, it was said by this court (page 28 [<span class="citation no-link">44 S. Ct. 53</span>]):</p>
    </div>
    <div class="num" id="p61">
      <span class="num">61</span>
      <p class="indent">'But, as we have seen, good faith is not enough to constitute      probable cause. That faith must be grounded on facts within      knowledge of the Director General's agent, which in the judgment of the court would make his faith      reasonable.'</p>
    </div>
    <div class="num" id="p62">
      <span class="num">62</span>
      <p class="indent">See, also, Munn v. De Nemours, <span class="citation no-link">3 Wash. C. C. 37</span>, Fed. Cas. No. 9926.</p>
    </div>
    <div class="num" id="p63">
      <span class="num">63</span>
      <p class="indent">In the light of these authorities, and what is shown by this record, it is clear the officers here had justification for the search and seizure. This is to say that the facts and circumstances within their knowledge and of which they had reasonably trustworthy information were sufficient in themselves to warrant a man of reasonable caution in the belief that intoxicating liquor was being transported in the automobile which they stopped and searched.</p>
    </div>
    <div class="num" id="p64">
      <span class="num">64</span>
      <p class="indent">Counsel finally argue that the defendants should be permitted to escape the effect of the conviction because the court refused on motion to deliver them the liquor when, as they say, the evidence adduced on the motion was much less than that shown on the trial, and did not show probable cause. The record does not make it clear what evidence was produced in support of or against the motion. But, apart from this, we think the point is without substance here. If the evidence given on the trial was sufficient, as we think it was, to sustain the introduction of the liquor as evidence, it is immaterial that there was an inadequacy of evidence when application was made for its return. A conviction on adequate and admissible evidence should not be set aside on such a ground. The whole matter was gone into at the trial, so no right of the defendants was infringed.</p>
    </div>
    <div class="num" id="p65">
      <span class="num">65</span>
      <p class="indent">Counsel for the government contend that Kiro, the defendant who did not own the automobile, could not complain of the violation of the Fourth Amendment in the use of the liquor as evidence against him, whatever the view taken as to Carroll's rights. Our conclusion as to the whole case makes it unnecessary for us to discuss this aspect of it.</p>
    </div>
    <div class="num" id="p66">
      <span class="num">66</span>
      <p class="indent">The judgment is affirmed.</p>
    </div>
    <div class="num" id="p67">
      <span class="num">67</span>
      <p class="indent">Mr. Justice McKENNA, before his retirement, concurred in this opinion.</p>
    </div>
    <div class="num" id="p68">
      <span class="num">68</span>
      <p class="indent">The separate opinion of Mr. Justice McREYNOLDS.</p>
    </div>
    <div class="num" id="p69">
      <span class="num">69</span>
      <p class="indent">1. The damnable character of the 'bootlegger's' business should not close our eyes to the mischief which will surely follow any attempt to destroy it by unwarranted methods. 'To press forward to a great principle by breaking through every other great principle that stands in the way of its establishment; * * * in short, to procure an eminent good by means that are unlawful, is as little consonant to private morality as to public justice.' Sir William Scott, The Le Louis, 2 Dodson, 210, 257.</p>
    </div>
    <div class="num" id="p70">
      <span class="num">70</span>
      <p class="indent">While quietly driving an ordinary automobile along a much frequented public road, plaintiffs in error were arrested by federal officers without a warrant and upon mere suspicion ill-founded, as I think. The officers then searched the machine and discovered carefully secreted whisky, which was seized and thereafter used as evidence against plaintiffs in error when on trial for transporting intoxicating liquor contrary to the Volstead Act. <span class="citation no-link">41 Stat. 305</span>, c. 85. They maintain that both arrest and seizure were unlawful and that use of the liquor as evidence violated their constitutional rights.</p>
    </div>
    <div class="num" id="p71">
      <span class="num">71</span>
      <p class="indent">This is not a proceeding to forfeit seized goods; nor is it an action against the seizing officer for a tort. Cases like the following are not controlling: Crowell v. McFadon. <span class="citation" data-id="85059"><a href="/opinion/85059/crowell-and-others-v-mfadon/#98" aria-description="Citation for case: Crowell and Others v. M&#x27;fadon">8 Cranch, 94, 98</a></span>, <span class="citation" data-id="85059"><a href="/opinion/85059/crowell-and-others-v-mfadon/" aria-description="Citation for case: Crowell and Others v. M&#x27;fadon">3 L. Ed. 499</a></span>; United States v. 1960 Bags of Coffee, <span class="citation" data-id="9416272"><a href="/opinion/85079/united-states-v-1960-bags-of-coffee/#403" aria-description="Citation for case: United States v. 1960 Bags of Coffee">8 Cranch, 398, 403, 405</a></span>, <span class="citation" data-id="9416272"><a href="/opinion/85079/united-states-v-1960-bags-of-coffee/" aria-description="Citation for case: United States v. 1960 Bags of Coffee">3 L. Ed. 602</a></span>; Otis v. Watkins, <span class="citation" data-id="85121"><a href="/opinion/85121/otis-v-watkins/" aria-description="Citation for case: Otis v. Watkins">9 Cranch, 339</a></span>, <span class="citation" data-id="85121"><a href="/opinion/85121/otis-v-watkins/" aria-description="Citation for case: Otis v. Watkins">3 L. Ed. 752</a></span>; Gelston v. Hoyt, <span class="citation" data-id="8373743"><a href="/opinion/8403401/gelston-v-hoyt/#310" aria-description="Citation for case: Gelston v. Hoyt">3 Wheat. 246, 310, 318</a></span>, <span class="citation" data-id="8373743"><a href="/opinion/8403401/gelston-v-hoyt/" aria-description="Citation for case: Gelston v. Hoyt">4 L. Ed. 381</a></span>; Wood v. United States, <span class="citation" data-id="86221"><a href="/opinion/86221/wood-v-united-states/" aria-description="Citation for case: Wood v. United States">16 Pet. 342</a></span>, <span class="citation" data-id="86221"><a href="/opinion/86221/wood-v-united-states/" aria-description="Citation for case: Wood v. United States">10 L. Ed. 987</a></span>; Taylor v. United States, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/#205" aria-description="Citation for case: Taylor v. United States">3 How. 197, 205</a></span>, <span class="citation" data-id="86316"><a href="/opinion/86316/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">11 L. Ed. 559</a></span>. They turned upon express provisions of applicable acts of Congress; they did not involve the point now presented and afford little, if any, assistance toward its proper solution. The Volstead Act does not, in terms, authorize arrest or seizure upon mere suspicion.</p>
    </div>
    <div class="num" id="p72">
      <span class="num">72</span>
      <p class="indent">Whether the officers are shielded from prosecution or action by Rev. Stat. &#167; 970, is not important. That section does not undertake to deprive the citizen of any constitutional right or to permit the use of evidence unlawfully obtained. It does, however, indicate the clear understanding of Congress that probable cause is not always enough to justify a seizure.</p>
    </div>
    <div class="num" id="p73">
      <span class="num">73</span>
      <p class="indent">Nor are we now concerned with the question whether by apt words Congress might have authorized the arrest without a warrant. It has not attempted to do this. On the contrary, the whole history of the legislation indicates a fixed purpose not so to do. First and second violations are declared to be misdemeanors nothing more&#8212;and Congress, of course, understood the rule concerning arrests for such offenses. Whether different penalties should have been prescribed or other provisions added is not for us to inquire; nor do difficulties attending enforcement give us power to supplement the legislation.</p>
    </div>
    <div class="num" id="p74">
      <span class="num">74</span>
      <p class="indent">2. As the Volstead Act contains no definite grant of authority to arrest upon suspicion and without warrant for a first offense, we come to inquire whether such authority can be inferred from its provisions.</p>
    </div>
    <div class="num" id="p75">
      <span class="num">75</span>
      <p class="indent">Unless the statute which creates a misdemeanor contains some clear provision to the contrary, suspicion that it is being violated will not justify an arrest. Criminal statutes must be strictly construed and applied, in harmony with rules of the common law. United States v. Harris, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/#310" aria-description="Citation for case: United States v. Harris">177 U. S. 305, 310</a></span>, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">20 S. Ct. 609</a></span>, <span class="citation" data-id="95241"><a href="/opinion/95241/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">44 L. Ed. 780</a></span>. And the well-settled doctrine is that an arrest for a misdemeanor may not be made without a warrant unless the offense is committed in the officer's presence.</p>
    </div>
    <div class="num" id="p76">
      <span class="num">76</span>
      <p class="indent">Kurtz v. Moffitt, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498</a></span>, <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#152" aria-description="Citation for case: Kurtz v. Moffitt">6 S. Ct. 148, 152</a></span> (<span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/" aria-description="Citation for case: Kurtz v. Moffitt">29 L. Ed. 458</a></span>):</p>
    </div>
    <div class="num" id="p77">
      <span class="num">77</span>
      <p class="indent">'By the common law of England, neither a civil officer nor a      private citizen had the right without a warrant to make an      arrest for a crime not committed in his presence, except in      the case of felony, and then only for the purpose of bringing the      offender before a civil magistrate.'</p>
    </div>
    <div class="num" id="p78">
      <span class="num">78</span>
      <p class="indent">John Bad Elk v. United States, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534</a></span>, <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#731" aria-description="Citation for case: Bad Elk v. United States">20 S. Ct. 729, 731</a></span> (<span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/" aria-description="Citation for case: Bad Elk v. United States">44 L. Ed. 874</a></span>):</p>
    </div>
    <div class="num" id="p79">
      <span class="num">79</span>
      <p class="indent">'An officer, at common law, was not authorized to make an      arrest without a warrant, for a mere misdemeanor not      committed in his presence.'</p>
    </div>
    <div class="num" id="p80">
      <span class="num">80</span>
      <p class="indent">Commonwealth v. Wright, <span class="citation" data-id="6424446"><a href="/opinion/6550711/commonwealth-v-wright/#158" aria-description="Citation for case: Commonwealth v. Wright">158 Mass. 149, 158</a></span>, <span class="citation" data-id="6424446"><a href="/opinion/6550711/commonwealth-v-wright/#85" aria-description="Citation for case: Commonwealth v. Wright">33 N. E. 82, 85</a></span> (19 L. R. A. 206, <span class="citation no-link">35 Am. St. Rep. 475</span>):</p>
    </div>
    <div class="num" id="p81">
      <span class="num">81</span>
      <p class="indent">'It is suggested that the statutory misdemeanor of having in      one's possession short lobsters with intent to sell them is a      continuing offence, which is being committed while such      possession continues, and that therefore an officer who sees      any person in possession of such lobsters with intent to sell      them can arrest such person without a warrant, as for a      misdemeanor committed in his presence. We are of opinion,      however, that for statutory misdemeanors of this kind, not      amounting to a breach of the peace, there is no authority in      an officer to arrest without a warrant, unless it is given by      statute. * * * The Legislature has often empowered officers      to arrest without a warrant for similar offenses, which      perhaps tends to show that, in its opinion, no such right      exists at common law.'</p>
    </div>
    <div class="num" id="p82">
      <span class="num">82</span>
      <p class="indent">Pinkerton v. Verberg, <span class="citation" data-id="7934479"><a href="/opinion/7981669/pinkerton-v-verberg/#584" aria-description="Citation for case: Pinkerton v. Verberg">78 Mich. 573, 584</a></span>, <span class="citation" data-id="7934479"><a href="/opinion/7981669/pinkerton-v-verberg/#582" aria-description="Citation for case: Pinkerton v. Verberg">44 N. W. 579, 582</a></span> (7 L. R. A. 507, <span class="citation no-link">18 Am. St. Rep. 473</span>):</p>
    </div>
    <div class="num" id="p83">
      <span class="num">83</span>
      <p class="indent">'Any law which would place the keeping and safe-conduct of      another in the hands of even a conservator of the peace,      unless for some breach of the peace committed in his      presence, or upon suspicion of felony, would be most      oppressive and unjust, and destroy all the rights which our      Constitution guarantees. These are rights which existed long      before our Constitution, and we have taken just pride in      their maintenance, making them a part of the fundamental law      of the land.' 'If persons can be restrained of their liberty,      and assaulted and imprisoned, under such circumstances,      without complaint or warrant, then there is no limit to the      power of a police officer.'</p>
    </div>
    <div class="num" id="p84">
      <span class="num">84</span>
      <p class="indent">3. The Volstead Act contains no provision which annuls the accepted common-law rule or discloses definite intent to authorize arrests without warrant for misdemeanors not committed in the officer's presence.</p>
    </div>
    <div class="num" id="p85">
      <span class="num">85</span>
      <p class="indent">To support the contrary view section 26 is relied upon.</p>
    </div>
    <div class="num" id="p86">
      <span class="num">86</span>
      <p class="indent">'When * * * any officer of the law shall discover any person      in the act of transporting in violation of the law,      intoxicating liquors in any wagon, buggy, automobile, water      or air craft, or other vehicle, it shall be his duty to seize      any and all intoxicating liquors found therein being      transported contrary to law. Whenever intoxicating liquors      transported or possessed illegally shall be seized by an      officer he shall take possession of the vehicle and team or      automobile, boat, air or water craft, or any other      conveyance, and shall arrest any person in charge thereof.'</p>
    </div>
    <div class="num" id="p87">
      <span class="num">87</span>
      <p class="indent">Let it be observed that this section has no special application to automobiles; it includes <i>any</i> vehicle&#8212;buggy, wagon, boat, or air craft. Certainly, in a criminal statute, always to be strictly construed, the words 'shall discover * * * in the act of transporting in violation of the law' cannot mean shall have reasonable cause to suspect or believe that such transportation is being carried on. To discover and to suspect are wholly different things. Since the beginning apt words have been used when Congress intended that arrests for misdemeanors or seizures might be made upon suspicion. It has studiously refrained from making a felony of the offense here charged; and it did not undertake by any apt words to enlarge the power to arrest. It was not ignorant of the established rule on the subject, and well understood how this could be abrogated, as plainly appears from statutes like the following:</p>
    </div>
    <div class="num" id="p88">
      <span class="num">88</span>
      <p class="indent">'An act to regulate the collection of duties on imports and      tonnage,' approved March 2, 1789, <span class="citation no-link">1 Stat. 627</span>, 677, 678, c.      22; 'An act to provide more effectually for the collection of      the duties imposed by law on goods, wares and merchandise      imported into the United States, and on the tonnage of ships or      vessels,' approved August 4, 1790, <span class="citation no-link">1 Stat. 145</span>, 170, c. 35;      'An act further to provide for the collection of duties on      imports and tonnage,' approved March 3, 1815, <span class="citation no-link">3 Stat. 231</span>,      232, c. 94.</p>
    </div>
    <div class="num" id="p89">
      <span class="num">89</span>
      <p class="indent">These and similar acts definitely empowered officers to seize upon suspicion and therein radically differ from the Volstead Act, which authorized no such thing.</p>
    </div>
    <div class="num" id="p90">
      <span class="num">90</span>
      <p class="indent">'An act supplemental to the National Prohibition Act,' approved November 23, 1921, <span class="citation no-link">42 Stat. 222</span>, 223, c. 134, provides:</p>
    </div>
    <div class="num" id="p91">
      <span class="num">91</span>
      <p class="indent">'That any officer, agent, or employee of the United States      engaged in the enforcement of this act, or the National      Prohibition Act, or any other law of the United States, who      shall search any private dwelling as defined in the National      Prohibition Act, and occupied as such dwelling, without a      warrant directing such search, or who while so engaged shall      without a search warrant maliciously and without reasonable      cause search any other building or property, shall be guilty      of a misdemeanor and upon conviction thereof shall be fined      for a first offense not more than $1,000, and for a      subsequent offense not more than $1,000 or imprisoned not      more than one year, or both such fine and imprisonment.'</p>
    </div>
    <div class="num" id="p92">
      <span class="num">92</span>
      <p class="indent">And it is argued that the words and history of this section indicate the intent of Congress to distinguish between the necessity for warrants in order to search private dwelling and the right to search automobiles without one. Evidently Congress regarded the searching of private dwellings as matter of much graver consequence than some other searches and distinguished between them by declaring the former criminal. But the connection between this distinction and the legality of plaintiffs in error's arrest is not apparent. Nor can I find reason for inquiring concerning the validity of the distinction under the Fourth Amendment. Of course, the distinction is valid, and so are some seizures. But what of it? The act made nothing legal which theretofore was unlawful, and to conclude that by declaring the unauthorized search of a private dwelling criminal Congress intended to remove ancient restrictions from other searches and from arrests as well, would seem impossible.</p>
    </div>
    <div class="num" id="p93">
      <span class="num">93</span>
      <p class="indent">While the Fourth Amendment denounces only unreasonable seizures unreasonableness often depends upon the means adopted. Here the seizure followed an unlawful arrest, and therefore became itself unlawful&#8212;as plainly unlawful as the seizure within the home so vigorously denounced in Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391, 392, 393</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S. Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L. Ed. 652</a></span>, L. R. A. 1915B, 834, Ann. Cas. 1915C, 1177.</p>
    </div>
    <div class="num" id="p94">
      <span class="num">94</span>
      <p class="indent">In Snyder v. United States, <span class="citation" data-id="8828212"><a href="/opinion/8843002/snyder-v-united-states/#2" aria-description="Citation for case: Snyder v. United States">285 F. 1, 2</a></span>, the Court of Appeals, Fourth Circuit, rejected evidence obtained by an unwarranted arrest, and clearly announced some very wholesome doctrine:</p>
    </div>
    <div class="num" id="p95">
      <span class="num">95</span>
      <p class="indent">'That an officer may not make an arrest for a misdemeanor not      committed in his presence, without a warrant, has been so      frequently decided as not to require citation of authority.      It is equally fundamental that a citizen may not be arrested      on suspicion of having committed a misdemeanor and have his      person searched by force, without a warrant of arrest. If,      therefore, the arresting officer in this case had no other      justification for the arrest than the mere suspicion that a      bottle, only the neck of which he could see protruding from      the pocket of defendant's coat, contained intoxicating      liquor, then it would seem to follow without much question      that the arrest and search, without first having secured a      warrant, were illegal. And that his only justification was      his suspicion is admitted by the evidence of the arresting      officer himself. If the bottle had been empty or if it had      contained any one of a dozen innoxious liquids, the act of      the officer would, admittedly, have been an unlawful invasion      of the personal liberty of the defendant. That it happened in      this instance to contain whisky, we think, neither justifies the assault nor condemns the principle      which makes such an act unlawful.'</p>
    </div>
    <div class="num" id="p96">
      <span class="num">96</span>
      <p class="indent">The validity of the seizure under consideration depends on the legality of the arrest. This did not follow the seizure, but the reverse is true. Plaintiffs in error were first brought within the officers' power, and, while therein, the seizure took place. If an officer, upon mere suspicion of a misdemeanor, may stop one on the public highway, take articles away from him and thereafter use them as evidence to convict him of crime, what becomes of the Fourth and Fifth Amendments?</p>
    </div>
    <div class="num" id="p97">
      <span class="num">97</span>
      <p class="indent">In Weeks v. United States, supra, through Mr. Justice Day, this court said:</p>
    </div>
    <div class="num" id="p98">
      <span class="num">98</span>
      <p class="indent">'The effect of the Fourth Amendment is to put the courts of      the United States and federal officials, in the exercise of      their power and authority, under limitations and restraints      as to the exercise of such power and authority, and to      forever secure the people, their persons, houses, papers and      effects against all unreasonable searches and seizures under      the guise of law. This protection reaches all alike, whether      accused of crime or not, and the duty of giving to it force      and effect is obligatory upon all entrusted under our federal      system with the enforcement of the laws. The tendency of      those who execute the criminal laws of the country to obtain      conviction by means of unlawful seizures and enforced      confessions, the latter often obtained after subjecting      accused persons to unwarranted practices destructive of      rights secured by the federal Constitution, should find no      sanction in the judgments of the courts which are charged at      all times with the support of the Constitution and to which      people of all conditions have a right to appeal for the      maintenance of such fundamental rights. * * * The efforts of      the courts and their officials to bring the guilty to      punishment, praiseworthy as they are, are not to be aided by      the sacrifice of those great principles established by years      of endeavor and suffering which have resulted in their embodiment in the fundamental law of the      land.'</p>
    </div>
    <div class="num" id="p99">
      <span class="num">99</span>
      <p class="indent">Silverthorne Lumber Co. v. United States, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 391</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">40 S. Ct. 182</a></span>, <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">64 L. Ed. 319</a></span>:</p>
    </div>
    <div class="num" id="p100">
      <span class="num">100</span>
      <p class="indent">'The proposition could not be presented more nakedly. It is      that although of course its seizure was an outrage which the      government now regrets, it may study the papers before it      returns them, copy them, and then may use the knowledge that      it has gained to call upon the owners in a more regular form      to produce them; that the protection of the Constitution      covers the physical possession but not any advantages that      the government can gain over the object of its pursuit by      doing the forbidden act. Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S.      383</a></span>, to be sure, had established that laying the papers      directly before the grand jury was unwarranted, but it is      taken to mean only that two steps are required instead of      one. In our opinion such is not the law. It reduces the      Fourth Amendment to a form of words. <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 393</a></span>. The      essence of a provision forbidling the acquisition of evidence      in a certain way is that not merely evidence so acquired      shall not be used before the court but that it shall not be      used at all. Of course this does not mean that the facts thus      obtained become sacred and inaccessible. If knowledge of them      is gained from an independent source they may be proved like      any others, but the knowledge gained by the government's own      wrong cannot be used by it in the way proposed.'</p>
    </div>
    <div class="num" id="p101">
      <span class="num">101</span>
      <p class="indent">Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S. Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L. Ed. 647</a></span>, and Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S. Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L. Ed. 654</a></span>, distinctly point out that property procured by unlawful action of federal officers cannot be introduced as evidence.</p>
    </div>
    <div class="num" id="p102">
      <span class="num">102</span>
      <p class="indent">The arrest of plaintiffs in error was unauthorized, illegal, and violated the guaranty of due process given by the Fifth Amendment. The liquor offered in evidence was obtained by the search which followed this arrest and was therefore obtained in violation of their constitutional rights. Articles found upon or in the control of one lawfully arrested may be used as evidence for certain purposes, but not at all when secured by the unlawful action of a federal officer.</p>
    </div>
    <div class="num" id="p103">
      <span class="num">103</span>
      <p class="indent">4. The facts known by the officers who arrested plaintiffs in error were wholly insufficient to create a reasonable belief that they were transporting liquor contrary to law. These facts were detailed by Fred Cronenwett, chief prohibition officer. His entire testimony as given at the trial follows:</p>
    </div>
    <div class="num" id="p104">
      <span class="num">104</span>
      <p class="indent">'I am in charge of the federal prohibition department in this      district. I am acquainted with these two respondents, and      first saw them on September 29, 1921, in Mr. Scully's      apartment on Oakes street, Grand Rapids. There were three of      them that came to Mr. Scully's apartment, one by the name of      Kruska, George Krio, and John Carroll. I was introduced to      them under the name of Stafford, and told them I was working      for the Michigan Chair Company, and wanted to buy three cases      of whisky, and the price was agreed upon. After they thought      I was all right, they said they would be back in half or      three-quarters of an hour; that they had to go out to the      east end of Grand Rapids to get this liquor. They went away      and came back in a short time, and Mr. Kruska came upstairs      and said they couldn't get it that night; that a fellow by      the name of Irving, where they were going to get it, wasn't      in, but they were going to deliver it the next day, about      ten. They didn't deliver it the next day. I am not positive      about the price. It seems to me it was around $130 a case. It      might be $135. Both respondents took part in this      conversation. When they came to Mr. Scully's apartment they      had this same car. While it was dark and I wasn't able to get      a good look at this car, later, on the 6th day of October,      when I was out on the road with Mr. Scully, I was waiting on      the highway while he went to Reed's Lake to get a light lunch, and they drove by, and I had their license number and      the appearance of their car, and knowing the two boys, seeing      them on the 29th day of September, I was satisfied when I      seen the car on December 15th it was the same car I had seen      on the 6th day of October. On the 6th day of October it was      probably twenty minutes before Scully got back to where I      was. I told him the Carroll boys had just gone toward Detroit      and we were trying to catch up with them and see where they      were going. We did catch up with them somewhere along by Ada,      just before we got to Ada, and followed them to East Lansing.      We gave up the chase at East Lansing.</p>
    </div>
    <div class="num" id="p105">
      <span class="num">105</span>
      <p class="indent">'On the 15th of December, when Peterson and Scully and I      overhauled this car on the road, it was in the country, on      Pike 16, the road leading between Grand Rapids and Detroit.      When we passed the car we were going toward Ionia, or      Detroit, and the Kiro and Carroll boys were coming towards      Grand Rapids when Mr. Scully and I recognized them and said,      'There goes the Carroll brothers,' and we went on still      further in the same direction we were going and turned around      and went back to them&#8212;drove up to the side of them. Mr.      Scully was driving the car; I was sitting in the front seat,      and I stepped out on the running board and held out my hand      and said, 'Carroll, stop that car,' and they did stop it.      John Kiro was driving the car. After we got them stopped, we      asked them to get out of the car, which they did. Carroll      referred to me, and called me by the name of 'Fred,' just as      soon as I got up to him. Raised up the back part of the      roadster; didn't find any liquor there; then raised up the      cushion; then I struck at the lazyback of the seat and it was      hard. I then started to open it up, and I did tear the      cushion some, and Carroll said, 'Don't tear the cushion; we      have only got six cases in there;' and I took out two bottles      and found out it was liquor; satisfied it was liquor. Mr.      Peterson and a fellow by the name of Gerald Donker came in with the two Carroll boys and      the liquor and the car to Grand Rapids. They brought the two      defendants and the car and the liquor to Grand Rapids. I and      the other men besides Peterson stayed out on the road,      looking for other cars that we had information were coming      in. There was conversation between me and Carroll before      Peterson started for town with the defendants. Mr. Carroll      said, 'Take the liquor, and give us one more chance, and I      will make it right with you.' At the same time he reached in      one of his trousers pockets and pulled out money; the amount      of it I don't know. I wouldn't say it was a whole lot. I saw      a $10 bill and there was some other bills; I don't know how      much there was; it wasn't a large amount.</p>
    </div>
    <div class="num" id="p106">
      <span class="num">106</span>
      <p class="indent">'As I understand, Mr. Hanley helped carry the liquor from the      car. On the next day afterwards, we put this liquor in boxes,      steel boxes, and left it in the marshal's vault, and it is      still there now. Mr. Hanley and Chief Deputy Johnson, some of      the agents and myself were there. Mr. Peterson was there the      next day that the labels were signed by the different      officers; those two bottles, Exhibits A and B.</p>
    </div>
    <div class="num" id="p107">
      <span class="num">107</span>
      <p class="indent">'Q. Now, those two bottles, Exhibits A and B, were those the      two bottles you took out of the car out there, or were those      two bottles taken out of the liquor after it got up here? A.      We didn't label them out on the road; simply found it was      liquor and sent it in; and this liquor was in Mr. Hanley's      custody that evening and during the middle of the next day      when we checked it over to see the amount of liquor that was      there. Mr. Johnson and I sealed the bottles, and Mr.      Johnson's name is on the label that goes over the bottle with      mine, and this liquor was taken out of the case to-day. It      was taken out for the purpose of analyzation. The others were      not broken until to-day.</p>
    </div>
    <div class="num" id="p108">
      <span class="num">108</span>
      <p class="indent">'Q. And are you able to tell us, from the label and from           the bottles, whether it is part of the same liquor taken           out of that car? A. It has the appearance of it; yes,           sir. Those are the bottles that were in there that Mr.           Hanley said was gotten out of the Carroll car.'</p>
    </div>
    <p class="indent">Cross-examination:</p>
    <div class="num" id="p109">
      <span class="num">109</span>
      <p class="indent">'I think I was the first one to get back to the Carroll car      after it was stopped. I had a gun in my pocket; I didn't      present it. I was the first one to the car and raised up the      back of the car, but the others were there shortly afterward.      We assembled right around the car immediately.</p>
    </div>
    <div class="num" id="p110">
      <span class="num">110</span>
      <p class="indent">'Q. And whatever examination and what investigation you made      you went right ahead and did it in your own way? A. Yes, sir.</p>
    </div>
    <div class="num" id="p111">
      <span class="num">111</span>
      <p class="indent">'Q. And took possession of it, arrested them, and brought      them in? A. Yes, sir.</p>
    </div>
    <div class="num" id="p112">
      <span class="num">112</span>
      <p class="indent">'Q. And at that time, of course, you had no search warrant?      A. No, sir. We had no knowledge that this car was coming      through at that particular time.'</p>
    </div>
    <p class="indent">Redirect examination:</p>
    <div class="num" id="p113">
      <span class="num">113</span>
      <p class="indent">'The lazyback was awfully hard when I struck it with my fist.      It was harder than upholstery ordinarily is in those backs; a      great deal harder. It was practically solid. Sixty-nine      quarts of whisky in one lazyback.'</p>
    </div>
    <div class="num" id="p114">
      <span class="num">114</span>
      <p class="indent">The negotiation concerning three cases of whisky on September 29th was the only circumstance which could have subjected plaintiffs in error to any reasonable suspicion. No whisky was delivered, and it is not certain that they ever intended to deliver any. The arrest came 2 1/2 months after the negotiation. Every act in the meantime is consistent with complete innocence. Has it come about that merely because a man once agreed to deliver whisky, but did not, he may be arrested whenever thereafter he ventures to drive an automobile on the road to Detroit!</p>
    </div>
    <div class="num" id="p115">
      <span class="num">115</span>
      <p class="indent">5. When Congress has intended that seizures or arrests might be made upon suspicion it has been careful to say so. The history and terms of the Volstead Act are not consistent with the suggestion that it was the purpose of Congress to grant the power here claimed for enforcement officers. The facts known when the arrest occurred were wholly insufficient to engender reasonable belief that plaintiffs in error were committing a misdemeanor, and the legality of the arrest cannot be supported by facts ascertained through the search which followed.</p>
    </div>
    <div class="num" id="p116">
      <span class="num">116</span>
      <p class="indent">To me it seems clear enough that the judgment should be reversed.</p>
    </div>
    <div class="num" id="p117">
      <span class="num">117</span>
      <p class="indent">I am authorized to say that Mr. Justice SUTHERLAND concurs in this opinion.</p>
    </div>
    
```

---

## GROUP: _overhaul2/lake/cases/Carter v. United States.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: Carter v. United States
type: case
citation: "No. 23-CF-0388, slip op. (dc 2025)"
parallel_cite: ""
neutral_cite: ""
court: D.C. 2025
court_level: state
circuit: ""
year: 2025
date_decided: 2025-08-28
docket: 23-CF-0388
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/10662535/carter-v-united-states/"
  cluster_id: 10662535
  opinion_id: null
  identity_checked: false
lake:
  record_id: Carter v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Seizure of the Person]]"
    role: Key
related:
  - "[[Seizure of the Person]]"
  - "[[Terry v. Ohio]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - show-of-authority
  - free-to-leave
  - reasonable-suspicion
holding: "A man was seized under the Fourth Amendment when an officer, backed by a show of authority and after disbelieving his response, directed him to hike up his pants; on the objective free-to-terminate inquiry — which properly accounts for the reasonable apprehension of a Black man in a heavily policed encounter — that request occurred before reasonable suspicion arose, making the seizure and its fruits unlawful."
---

# Carter v. United States

No. 23-CF-0388, slip op. (D.C. Ct. App. Aug. 28, 2025) · District of Columbia Court of Appeals · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): slip-only record (no A.3d cite yet); identity cluster 10662535 → opinion 11129122, decided 2025-08-28; Rule quote string-matched to the CL opinion text 2026-07-07. Slip-cite render per S2 A3; S9 promotes. -->

## Background
A five-officer tactical unit approached a group of about ten men, including Mr. Carter, in public during the daytime. An officer asked how he was doing; Carter lifted his shirt to show his waistband. When the officer expressed disbelief and asked whether he had "nothing" on him, Carter lifted his shirt again. The officer then asked him to "hike" up his pants; officers observed a bulge, seized him, and recovered a firearm. The trial court held Carter was not seized until after he raised his pants — by which point officers had reasonable suspicion — and denied suppression.

## Issue
Whether Mr. Carter was seized within the meaning of the Fourth Amendment when the officer directed him to raise his pants, before the officers had reasonable suspicion.

## Rule
The D.C. Court of Appeals reversed, holding that the seizure occurred earlier — at the request to raise his pants — and that the objective free-to-terminate inquiry must account for the defendant's race under *Dozier v. United States*: "we hold that Mr. Carter was seized within the meaning of the Fourth Amendment when Officer DelBorrell requested that he raise his pants." — slip op. at 30. Because that seizure preceded any reasonable suspicion or probable cause, it was unreasonable, and the firearm and Carter's ensuing statement should have been suppressed.

## Application
The court weighed the officers' coercive show of authority — the number of officers, the accusatory and repetitive questioning, and the disbelief of Carter's initial cooperation — and, applying *Dozier*, considered how an objectively reasonable Black man in Carter's position would experience that pressure. On that record, a reasonable person would not have felt free to walk away when told to hike up his pants, so the seizure crystallized before the bulge that supplied suspicion.

## Conclusion
Carter's convictions were **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. McLeese, Associate Judge, concurred in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Carter* illustrates the objective "free to terminate the encounter" test for when a *[[Seizure of the Person|seizure of the person]]* occurs and applies the D.C. rule (*Dozier v. United States*) that a suspect's race is relevant to that objective inquiry — a development the Supreme Court has not addressed. It is a published decision of the District of Columbia Court of Appeals, cited here for its reasoning.

## Appears on
- [[Seizure of the Person]] — *Key*

## Sources
- [*Carter v. United States*, No. 23-CF-0388 (D.C. Aug. 28, 2025)](https://www.courtlistener.com/opinion/10662535/carter-v-united-states/) — pinpoint: slip op. at 30 (opinion of the court; III. Conclusion); Rule quote string-matched to the CL opinion text 2026-07-07. No A.3d reporter cite has issued; the slip form is per S2 A3.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fe3d14adef664984", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Carter v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Carter v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Carter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Carter v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Carter v. United States",
    "case_name_short": "Carter",
    "case_name_full": "",
    "input_case_name": "Carter v. United States",
    "court": "D.C. 2025",
    "court_id": "dc",
    "court_level": "state",
    "circuit": null,
    "state": "dc",
    "date_decided": "2025-08-28",
    "year": 2025,
    "docket": "23-CF-0388",
    "cluster_id": 10662535,
    "lead_opinion_id": 11129122,
    "sibling_ids": [],
    "absolute_url": "/opinion/10662535/carter-v-united-states/",
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
      "note": "D.C. Court of Appeals slip No. 23-CF-0388, filed 2025-08-28; no A.3d volume/page. (A search-floated '341 A.3d 1067' could not be independently confirmed; treated as unverified.)",
      "legs": [
        {
          "source": "Justia",
          "url": "https://law.justia.com/cases/district-of-columbia/court-of-appeals/2025/23-cf-0388.html",
          "cite": "No. 23-CF-0388 (D.C. 2025-08-28)"
        },
        {
          "source": "Court PDF",
          "url": "https://www.dccourts.gov/sites/default/files/2025-08/Carter%20v.%20U.S.%20%2023-CF-0388.pdf",
          "cite": "slip No. 23-CF-0388"
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
    "date_created": "2026-07-06T05:44:26Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:44:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "carter-v-united-states--10662535",
      "to_record_id": "Carter v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Carter v. United States

```
Notice: This opinion is subject to formal revision before publication in the Atlantic
and Maryland Reporters. Users are requested to notify the Clerk of the Court of
any formal errors so that corrections may be made before the bound volumes go
to press.

             DISTRICT OF COLUMBIA COURT OF APPEALS

                                  No. 23-CF-0388

                          DONTE J. CARTER, APPELLANT,

                                         V.

                            UNITED STATES, APPELLEE.

                          Appeal from the Superior Court
                           of the District of Columbia
                               (2020-CF2-007280)

                        (Hon. Lynn Leibovitz, Trial Judge)

(Submitted April 18, 2024                                Decided August 28, 2025)

      Brian D. Shefferman was on the brief for appellant.

      Chrisellen R. Kolb, Assistant United States Attorney, with whom Matthew M.
Graves, United States Attorney at the time the brief was filed, and John P.
Mannarino, Benjamin Helfand, Jacqueline Yarbro, and Michael C. Lee, Assistant
United States Attorneys, were on the brief, for appellee.

      Before BECKWITH and MCLEESE, Associate Judges, and WASHINGTON, *
Senior Judge.

      Opinion for the court by Senior Judge WASHINGTON.



      *
        Senior Judge Fisher was originally assigned to this case. Following his
retirement on August 22, 2024, Judge Fisher was replaced by Senior Judge
Washington.
                                          2

      Concurring opinion by Associate Judge MCLEESE at page 31.


      WASHINGTON, Senior Judge: Appellant Donte Carter was conversing amongst

a group of ten Black men on a sunlit sidewalk in Ward Four of the District. Despite

not having raised any suspicion of engaging in criminal activity, the group was

approached by four members of the Metropolitan Police Department’s Gun

Recovery Unit (GRU). One of the officers approached Mr. Carter from behind and

asked whether he was carrying a firearm. Mr. Carter replied that he was not and

twice lifted his shirt to demonstrate that nothing was hidden underneath. The officer

then asked Mr. Carter to “hike” his pants up. In this appeal, we are asked to

determine whether Mr. Carter was seized at this moment within the meaning of the

Fourth Amendment. We hold that he was.


                                  I.     Background


      Our articulation of the facts is based on both the trial court’s extensive factual

findings and footage from body-cameras worn by the officers.             Neither party

disputes these facts.


      At some time between 3:00 and 4:00 pm on a sunny day in September 2020,

five officers of the GRU 1 drove two unmarked vehicles into Ward Four of the


      1
          The unit has since been renamed to the Violent Crime Impact Team (VCIT).
                                         3

District, an area that consists predominantly of Black Americans, 2 to conduct a

firearm interdiction. They went there because of “an uptick in shootings and sounds

of gunfire” in the area. The officers observed ten Black men conversing on a

sidewalk and parked along the road opposite them. The group was split between

three men “sitting and standing near some planters,” and another seven men about

fifteen feet away. Among the group of seven men was appellant Mr. Carter, leaned

up against a parked car and facing everyone else.


      Four officers, Officers Sanders, Guzman, DelBorrell, and Keleman, emerged

from the vehicles and approached the group. They wore tactical vests with “police”

written on the back as well as visible handcuffs, firearms, and other police

equipment. Officers Sanders and Guzman focused on the group of three and

announced that they were “checking for firearms.”       Almost immediately, and

without being prompted to, one of the men lifted his shirt to reveal his waistband

seemingly to demonstrate that nothing was hidden underneath. Upon checking the




      2
         Ward Four consists of approximately 44 percent Black Americans and 29
percent White Americans. 2020 Consensus Information & Data: Table 3, D.C.
Office of Plan., https://planning.dc.gov/publication/2020-census-information-and-
data; https://perma.cc/B6QF-C8YQ.
                                            4

man’s waistband and a small bag he was carrying, Officers Sanders and Guzman

continued toward the larger group.


      Meanwhile, Officers DelBorrell and Keleman focused on Mr. Carter’s group.

Officer Keleman approached two individuals standing a few feet to Mr. Carter’s left

while Officer DelBorrell looped around the vehicle Mr. Carter was leaning on to

approach him from behind. As Officer DelBorrell rounded the vehicle, another man

approximately a foot ahead of Mr. Carter and several feet ahead of the officer also

lifted his shirt to reveal his waistband. Within three to four feet of Mr. Carter, Officer

DelBorrell asked how he was “doing,” to which Mr. Carter briefly replied, “how are

you doing” or “what’s up” before turning away. Officer DelBorrell then moved

closer to Mr. Carter but before he could say anything else, Mr. Carter also lifted his

shirt to show his waistband and then lowered it. As Mr. Carter raised his shirt,

DelBorrell asked, “[h]ey [c]hamp, you not got nothing on you?” Mr. Carter

responded, “no” and lifted his shirt again. Unsatisfied, Officer DelBorrell requested,

“[d]o you mind hiking your pants for me real quick?” Mr. Carter complied. “[I]n a

single quick motion, [Mr. Carter] hiked his pants [up] by holding them at the

waistband with two hands.” He “then lifted his shirt [again] and put it back down.”


      While this was happening, Officer Guzman had begun to approach Mr. Carter

from the other group. When he was about six to ten feet away, he noticed a bulge in
                                          5

Mr. Carter’s groin area. When Mr. Carter raised his pants in response to Officer

DelBorrell’s question, Officer Guzman, from approximately three to five feet away,

saw that the bulge was an L-shape, which he believed to be a firearm. Officer

Guzman then instructed Mr. Carter to “[s]tand up . . . one more time.” Mr. Carter

stood. Guzman then remarked, “[r]ight there, brother, right there,” pointing to Mr.

Carter’s right groin area. Mr. Carter replied, “[t]his is my phone,” pulling a phone

from his right pocket. Officer Guzman subsequently frisked Mr. Carter and after a

brief struggle in which the other officers on the scene joined, the officers recovered

a firearm hidden in Mr. Carter’s pants.


      Based on this encounter, Mr. Carter was charged with eight offenses

connected to the firearm. He moved to suppress the firearm as well as a statement

he made following the incident on grounds that they were the result of an

unreasonable seizure in violation of the Fourth Amendment. The trial court denied

his motion. It rejected his argument that he was seized when Officer DelBorrell

asked him to raise his pants and held that Mr. Carter was seized only after he pulled

his pants up. The court held that by then, the officers had reasonable suspicion to

seize him based on Officer Guzman’s observation of an L-shaped bulge in his groin

area that he made only after Mr. Carter raised his pants. Accordingly, the court held

that the firearm and statement were not the product of an unreasonable seizure.
                                           6

      Mr. Carter was subsequently convicted on all eight counts following a trial on

stipulated facts. He timely appealed.


                                     II.   Analysis


      The Fourth Amendment to the United States Constitution protects against

unreasonable searches and seizures. U.S. Const. amend. IV. Under the Fourth

Amendment’s prohibition against unreasonable seizures, law enforcement officers

may not seize an individual unless they have reasonable suspicion or probable cause

to believe that the person is engaged in criminal activity. See Terry v. Ohio, 392

U.S. 1, 27 (1968); Robinson v. United States, 76 A.3d 329, 335 (D.C. 2013).


      Mr. Carter’s sole claim on appeal is that the trial court erroneously denied his

motion to suppress. Contrary to the court’s holding, he argues that the officers seized

him within the meaning of the Fourth Amendment when Officer DelBorrell

requested that he raise his pants. Because, according to Mr. Carter, the officers

lacked reasonable suspicion or probable cause, such conduct violated his Fourth

Amendment rights. Mr. Carter claims that the trial court therefore should have

suppressed the fruits of that seizure—the firearm and his subsequent statement. See

Smith v. United States, 283 A.3d 88, 98 (D.C. 2022) (explaining that a court must

generally suppress any evidence “obtained as a direct result of” or “found to be a
                                          7

derivative of” an illegal search or seizure (quoting Utah v. Strieff, 579 U.S. 232, 237

(2016))).


      For its part, the government admits that it lacked reasonable suspicion or

probable cause to seize Mr. Carter when Officer DelBorrell asked him to raise his

pants. It also concedes that if it did seize Mr. Carter at that moment, the firearm and

statement were products of an unreasonable seizure and should have been

suppressed. The government’s sole argument on appeal is that it did not seize Mr.

Carter until after Officer DelBorrell’s request that Mr. Carter “hike” his pants up,

when it did have reasonable suspicion to seize him. Mr. Carter does not deny that

the officers had reasonable suspicion after Officer DelBorrell’s question and simply

argues that the seizure began before then.


      Accordingly, the central question before us is whether Mr. Carter was seized

when Officer DelBorrell requested that he raise his pants. We review this question

de novo. Sharp v. United States, 132 A.3d 161, 166 (D.C. 2016) (holding that

whether a defendant was seized within the meaning of the Fourth Amendment is a

question of law, which we review de novo).


      To determine whether a defendant was seized within the meaning of the

Fourth Amendment, we ask whether in view of all the circumstances surrounding

the defendant’s encounter with law enforcement, an objective and reasonable person
                                          8

in the defendant’s shoes would have “felt free to terminate” the interaction and “go

about [their] business.” Jones v. United States, 154 A.3d 591, 592 (D.C. 2017); see

Graham v. Connor, 490 U.S. 386, 397 (1989) (explaining that the test for

reasonableness    under   the   Fourth   Amendment       is   an   “objective   one”).

“Circumstances that might signify a seizure include the ‘presence of several officers,

the display of a weapon by an officer, some physical touching of the [defendant], or

the use of language or tone of voice indicating that compliance with the officer[s’]

request[s] might [have been] compelled.’” T.W. v. United States, 292 A.3d 790, 795

(D.C. 2023) (quoting United States v. Mendenhall, 446 U.S. 544, 554 (1980)). To

that list, we have added factors such as whether (1) the officers asked the defendant

questions of such an accusatory nature that an objective and reasonable person in the

defendant’s position would have felt “apprehensive” in failing to reply, see Jones,

154 A.3d at 596; (2) the officers continued to press the defendant with such

questions “in the face of an initial denial,” signaling that they “‘refused to accept’

the answer given,” T.W., 292 A.3d at 795 (quoting Golden v. United States, 248 A.3d

925, 938 (D.C. 2021)); (3) the encounter took place at night or the defendant was

alone or secluded, see Dozier v. United States, 220 A.3d 933, 944 (D.C. 2019); and

(4) “the officers . . . blocked the [defendant’s] potential exit paths or ‘means of

egress’” so as to signal that the defendant was not free to leave, T.W., 292 A.3d at

795 (quoting Golden, 248 A.3d at 939). In addition, we also consider the defendant’s
                                          9

race and the role that it may have played in affecting their willingness to leave. See

Dozier, 220 A.3d at 944.


                                         A.


      At the outset, we acknowledge that this is a close case. Whereas several

aspects of Mr. Carter’s interaction with the officers strongly suggest that he was

seized, there are other features that sway us in the opposite direction.


      Beginning with the case that favors Mr. Carter, we recognize that this case is

not too dissimilar from Golden, in which we held that the defendant was seized. See

generally Golden, 248 A.3d 925. In that case, the defendant, Brandon Golden, was

walking alone along a sidewalk at night when four GRU officers in a pair of

unmarked SUVs approached him from behind. Id. at 931. One of the SUVs stopped

at a curb in front of Mr. Golden and the other parked several feet to the left. Id.

With his window rolled down and his police badge, tactical vest, and firearm clearly

visible, an officer in the first car, Officer Vaillancourt, asked Mr. Golden, “in a

conversational tone . . . whether he had any weapons on him.” Id. at 932. Mr.

Golden replied that he did not. Id. Officer Vaillancourt then asked, “[c]an you just

show me your waistband[?]” Id. (second alteration in original).            Mr. Golden

complied by pulling up the middle and left sides of his shirt but not the right. Id.

Suspecting that Mr. Golden was attempting to conceal something underneath the
                                          10

right part of his shirt, Officer Vaillancourt continued to probe Mr. Golden about what

he was hiding. Id. Eventually, Officer Vaillancourt exited the vehicle, frisked Mr.

Golden, and discovered a firearm. Id. Mr. Golden was subsequently charged with

various firearm-related offenses and sought to suppress the firearm on grounds that

the officers seized him without reasonable suspicion or probable cause and that the

firearm was a product of this unreasonable seizure. Id. at 931, 933. The trial court

denied his motion and Mr. Golden was convicted. Id. at 933.


      On appeal, we vacated Mr. Golden’s conviction and remanded. Id. at 949.

We held that the officers in the SUVs seized Mr. Golden the moment Officer

Vaillancourt requested to see his waistband. Id. at 936. Because the officers lacked

reasonable suspicion or probable cause at that point, the seizure was unreasonable.

Id. at 940. Accordingly, the trial court erred in failing to suppress the firearm. Id.


      We arrived at the conclusion that Mr. Golden was seized by first recognizing

that Mr. Golden’s encounter with the officers was not merely one between “equals,”

which an objective and reasonable person would feel free to terminate, but rather

“commenced with an impressive show of police authority.” Id. at 936 (quoting

Jones, 154 A.3d at 595). We observed that “[n]ot one but four police officers in two

unmarked vehicles simultaneously converged on and partially surrounded [Mr.
                                          11

Golden], with one of the vehicles blocking his path by stopping directly in front of

him[—]a visible signal that the police intended for him to stop.” Id.


      Second, we held that Officer Vaillancourt’s immediate questioning of Mr.

Golden as to whether he was carrying any weapons was of such an accusatory nature

that it could not be viewed as merely “a simple request for information.” Id. at 937;

cf. Florida v. Bostick, 501 U.S. 429, 434 (1991) (holding that an officer does not

seize someone merely by approaching them and “ask[ing] a few questions”). Rather,

it indicated to Mr. Golden that he had been “singled . . . out” because the police

“suspected him of being armed and committing a crime,” thereby contributing to a

“sense of powerlessness in an investigative confrontation by the police,” one which

he could relieve himself of only by demonstrating his innocence. Golden, 248 A.3d

at 937 (second alteration in original).


      Finally, we explained that Officer Vaillancourt’s request that Mr. Golden

reveal his waistband after Mr. Golden denied carrying a weapon took the interaction

“beyond mere questioning,” because it “implied” to Mr. Golden that the officers

would continue to view him with “heightened suspicion if he attempted to end the

encounter without first exposing his waist[band].” Id. We held that an objective

and reasonable person in Mr. Golden’s shoes “would not [have felt] free to frustrate
                                         12

the police inquiry” without first complying with Officer Vaillancourt’s request in

order to “allay [his] suspicions” and “get the confrontation over with.” Id.


      Here, Mr. Carter’s interaction with the officers bore many of the same features

that contributed to our finding that Mr. Golden was seized. First, like in Golden,

two police vehicles simultaneously approached Mr. Carter and others in his group.

Four officers then exited the vehicles and converged on the group, suggesting that

the men were not simply free to continue conversing amongst themselves as they

were previously. Officer DelBorrell also approached Mr. Carter from behind,

which—in our view—would make any objective and reasonable person feel uneasy

and intimidated, especially when faced with an openly visible firearm within close

proximity.


      Second, like Officer Vaillancourt, Officer DelBorrell immediately asked Mr.

Carter whether he possessed a firearm. As we did in Golden, we view this question

as one that suggested to Mr. Carter that he, alongside other members of the group,

had been singled out as being suspected of criminal activity. An objective and

reasonable person in his shoes would have felt apprehensive in refusing to respond

to the officer’s question. See, e.g., Mayo v. United States, 315 A.3d 606, 628-29

(D.C. 2024) (en banc) (explaining that such a question is intimidating in part due to

the “illegal[ity] [of] carry[ing] a gun in the District without proper licensure and
                                         13

registration”); T.W., 292 A.3d at 796-97 (explaining the coercive nature of a request

for a weapon). They may have felt fearful that refusing to answer such a question

would have suggested to “the suspicious officer[]” that they had “something to

hide.” Guadalupe v. United States, 585 A.2d 1348, 1360 (D.C. 1991).


      Finally, despite Mr. Carter both denying carrying a firearm and raising his

shirt not once but twice to reveal his waistband, Officer DelBorrell continued to

probe him by asking him to “hik[e] [his] pants up.” We see no appreciable difference

between this request and that in Golden as both required the defendants to continue

assuaging the officers’ suspicions despite initially denying any wrongdoing. Indeed,

both requests implied to the defendants that they would continue to be suspected of

criminal activity until the officers stopped asking questions, thereby leaving them

with little choice but to respond. See T.W., 292 A.3d at 798 (seeing no meaningful

difference between the officer’s offer to pat down the defendant and Officer

Vaillancourt’s request to view Mr. Golden’s waistband because both questions were

asked after the defendants denied carrying a weapon).


      While we recognize the similarities between this case and Golden, we also

acknowledge two key differences that prevent us from holding that Golden controls

the outcome here. Most notably, in Golden, we placed significant weight on the fact

that Mr. Golden was approached at night by four officers in a secluded setting where
                                          14

there were no bystanders to witness the interaction. See Golden, 248 A.3d at 936-37.

This not only resulted in a more intimidating atmosphere, but it also heightened Mr.

Golden’s concern that he was being singled out for criminal activity and would need

to comply to dispel that suspicion. Id. at 937. Here, in contrast, Mr. Carter was not

singled out on his own but rather as a member of a larger group. This likely

mitigated Mr. Carter’s concern that he alone was being targeted by the police.

Further, Mr. Carter was not outnumbered by four officers in a secluded setting at

night. Less intimidating, the interaction took place in broad daylight with nine

potential witnesses, all occupying the attention of just four officers.


      Second, whereas the officers in Golden exerted significant control over Mr.

Golden’s movement by partially surrounding him, thereby signaling that he was not

free to leave, the officers here did not restrict Mr. Carter’s movement. Rather, as the

trial court found in its suppression ruling, Mr. Carter “was not surrounded or

hemmed in by the police” and was “more surrounded by those he had been hanging

out with.” Indeed, unlike in Golden, any restriction on Mr. Carter’s movement was,

at least in part, self-imposed, namely by his decision to lean against a car in the

company of others. 3 See I.N.S. v. Delgado, 466 U.S. 210, 218 (1984) (holding that


      3
       We are unpersuaded by the government’s additional attempts to distinguish
Golden. Namely, the government argues that Officer DelBorrell’s conduct toward
Mr. Carter was less “intimidating” than Officer Vaillancourt’s actions toward Mr.
Golden. It points to Officer DelBorrell’s casual tone, the fact that Mr. Carter did not
                                          15




seem to be bothered, and that Officer Vaillancourt requested that Mr. Golden
“acquiesce in a public unveiling of part of his body” whereas Officer DelBorrell
merely asked Mr. Carter to raise his pants.

       We disagree with the government that Officer DelBorrell was less
intimidating than Officer Vaillancourt. To begin, as we recognized in Golden,
Officer Vaillancourt’s tone was also “conversational.” Id. at 932. Despite that, we
held that his questions were still intimidating due to their accusatory nature. Id. at
937. Indeed, we have previously discouraged courts from “attach[ing] undue weight
to a police officer’s ‘conversational’ tone in speaking to a suspect.” T.W., 292 A.3d
at 803 (quoting Golden, 248 A.3d at 935 n.26). “While a harsh and commanding
tone could certainly convey to a person that their compliance is non-optional, a polite
and conversational tone does little to dispel coercion that arises from the content of
officers’ inquiries, or in how they have approached the suspect.” Id. at 803; see also
Guadalupe, 585 A.2d at 1361 (explaining that police questioning does “not have to
assume an intensity marking a shift from polite conversation to harsh words to create
an intimidating atmosphere”). This is especially true when the officer’s inquiries
are accusatory in nature, as they were here.

       Second, we disagree with the government’s characterization of Mr. Carter as
being “[un]bothered.” Almost immediately after Officer DelBorrell began
questioning him, Mr. Carter raised his shirt up twice. If he were unbothered, we
think it far more likely that he would ignore the officer’s questions or at minimum
verbally deny possessing a firearm, let alone take the more drastic step of revealing
his waistband. In any case, we place little weight on Mr. Carter’s subjective response
to Officer DelBorrell’s conduct as the Fourth Amendment seizure inquiry is an
objective one—that is, whether an objective and reasonable person in Mr. Carter’s
shoes would feel free to terminate the encounter. See Jackson v. United States, 805
A.2d 979, 987 (D.C. 2002).

       Finally, that Officer DelBorrell requested that Mr. Carter raise his pants
whereas Officer Vaillancourt asked Mr. Golden to reveal his waistband is not legally
significant for present purposes. Setting aside the fact that Mr. Carter had already
raised his shirt twice before Officer DelBorrell called on him to raise his pants, our
main point here in Golden was not that Mr. Golden was subject to a highly intrusive
inquiry (though he was), it was that the officer indicated to him that he would not be
free to leave until he fully satisfied the officer that he did not possess any weapons.
See Golden, 248 A.3d at 937. Similarly here, by failing to take “‘no’ for an answer,”
                                          16

workers in a factory were not seized despite officers being stationed at the factory

doors because the workers had already voluntarily limited their movement to the

factory floor before the officers arrived).


                                          B.


      In addition to the differences between Golden and this case, we previously

concluded in two cases—Brown and Kelly—that defendants in circumstances also

not too dissimilar to those here were not seized within the meaning of the Fourth

Amendment. See generally Brown v. United States, 983 A.2d 1023 (D.C. 2009);

Kelly v. United States, 580 A.2d 1282 (D.C. 1990).           In Brown, two officers

approached a group of “five or six [people] standing on [a] sidewalk.” 983 A.2d at

1024-25. One of the officers approached the defendant, Valerie Brown, and asked

if she had “any guns, drugs, or narcotics on [her].” Id. at 1025. Ms. Brown replied

that she was “not doing anything” and that she was just “counting [her] money.” Id.

The officer repeated her question and Ms. Brown “reached into her purse and handed

the officer a brown pill bottle,” which later tested positive for cocaine. Id.


      We held that Ms. Brown was not seized despite the fact that the officer asked

the same accusatory question twice. Id. at 1026. We relied on the fact that the



Officer DelBorrell gave Mr. Carter the impression that he would have to respond to
all his questions before being let go. Id. (alterations in original).
                                         17

officers were outnumbered by the group Ms. Brown was a part of, the fact that she

was approached by only one officer while the other was further away speaking to

two other individuals, that the officers did not engage in behavior, “such as

threatening gestures, orders, or intimidation, which might have caused the encounter

to lose its consensual nature,” and that other members of the group walked away

unimpeded, suggesting that an objective and reasonable person in Ms. Brown’s

shoes would have felt free to leave. Id. at 1025-26. That the officer asked an

accusatory question and that she repeated her question were insufficient to overcome

the non-coercive nature of the other aspects of the interaction. See id.


      In Kelly, two officers approached the defendant, James Kelly, at Union

Station. Kelly, 580 A.2d at 1284. Both officers were in plain clothes and neither

was visibly carrying a firearm or displaying their badge. Id. One of the officers

asked Mr. Kelly if he “could speak with him” and Mr. Kelly replied, “yes.” Id.

Meanwhile, the other officer stood “about four feet in front of Kelly.” Id. The

questioning officer inquired about where Mr. Kelly was arriving from, where he

lived, and how long he had lived there. Id. The officer then introduced himself as a

member of the Narcotics Branch of the police department and asked if Mr. Kelly

was “carrying any drugs.” Id. Mr. Kelly replied, “no.” Id. The officer then asked

to search Mr. Kelly’s bag, which Mr. Kelly permitted. Id.
                                          18

      Like in Brown, we held that Mr. Kelly was not seized despite being repeatedly

asked an accusatory question. Id. at 1288. We explained that the officer “made no

demands” of Mr. Kelly, never produced a weapon, and never touched Mr. Kelly. Id.

at 1286. Further, we rejected Mr. Kelly’s argument that the non-questioning officer

was impeding his movement as the officer was four feet away, did not brandish a

weapon, or make any threatening gestures. Id. Finally, we emphasized that the

questioning officer asked Mr. Kelly if he could speak with him, thereby implying to

Mr. Kelly that he did not have to comply. Id.


      Brown and Kelly suggest that we should similarly overlook the fact that Mr.

Carter was repeatedly asked accusatory questions as the other aspects of the

encounter were just as non-coercive as in those two cases. Like in Brown, Mr.

Carter’s group far outnumbered the officers who approached them. In fact, the

number of non-officers to officers was approximately the same in both cases (five

to two). Further, like in Brown, Mr. Carter was initially approached by one officer,

Officer DelBorrell, while the others focused elsewhere. Indeed, at the time Officer

DelBorrell requested that Mr. Carter raise his pants, Officer DelBorrell was the only

officer in Mr. Carter’s immediate vicinity. Officer Guzman, the next closest officer,

was still several feet away. Finally, like in Brown and Kelly, the officers here did not

make any threatening gestures or orders, nor did they touch Mr. Carter, so as to

suggest that compliance was mandatory.
                                         19

      The government goes so far as to argue that considering the similarities,

Brown and Kelly control the outcome in this case. While we certainly place

analytical weight on both cases, we reject the government’s claim that they are

controlling. Brown is distinguishable for two reasons. First, unlike in Brown, no

member of Mr. Carter’s group left once the police arrived. To the contrary, not only

did members of the group comply with the officers’ requests, but some went further

by raising their shirts before they were even asked. Accordingly, unlike in Brown,

the behavior of others surrounding Mr. Carter suggest that an objective and

reasonable person in his shoes would not have felt free to leave. Second, what made

the repetitive questioning less coercive in Brown was that Ms. Brown’s first answer

was non-responsive to the officer’s question. The officer asked whether she was

carrying any contraband, and rather than replying “yes” or “no,” Ms. Brown

answered that she was simply counting her money. Brown, 983 A.2d at 1025. Thus,

it was “entirely reasonable for the officer to ask her question again.” Gordon v.

United States, 120 A.3d 73, 82 (D.C. 2015) (differentiating Brown on grounds that

the repetitive questioning in Brown was simply to seek clarification to a non-

responsive initial answer); T.W., 292 A.3d at 801 (same). Here, in contrast, Mr.

Carter explicitly denied carrying a weapon and raised his shirt twice when Officer

DelBorrell questioned him. In the face of this denial, unlike in Brown, Officer

DelBorrell implied that he was unsatisfied by asking Mr. Carter to raise his pants.
                                         20

      Kelly is also distinguishable. Namely, the officer there requested Mr. Kelly’s

permission to speak with him before questioning him, thereby indicating that

cooperation was only optional. Kelly, 580 A.2d at 1284. An acknowledgement that

an individual need not comply significantly reduces the coercive nature of a police

encounter as it dispels doubt in an individual’s mind that they must cooperate to

terminate the interaction. Whereas the officer in Kelly effectively informed Mr.

Kelly of his right to walk away by asking him if he could speak, the officers did not

do so here. Officer DelBorrell simply approached Mr. Carter from behind and began

asking if he was carrying any weapons.


                                   *     *      *


      In light of the similarities between this case and those in which we both found

that the defendant was seized (Golden), and not seized (Brown and Kelly), we must

look beyond the mere conduct of the officers to objectively determine whether Mr.

Carter was seized. To do so, we examine the impact of the defendant’s race. Dozier,

220 A.3d at 944.     Indeed, in its suppression ruling, the trial court implicitly

recognized the relevance of race to its Fourth Amendment seizure inquiry. It

acknowledged that “in certain neighborhoods among certain demographics that are

highly policed[,] the behavior of police can convey to a reasonable . . . person that

they are compelled to allay [the] officers’ suspicion by acceding to their wishes.”
                                         21

The court went no further, however, and instead focused its analysis solely on the

coercive nature of the officers’ conduct. It did not delve further into how the

officers’ conduct might have uniquely impacted an objective and reasonable person

sharing Mr. Carter’s racial status as a Black man. Accordingly, in this next part, we

conduct a more thorough inquiry.


                                        C.


      Dozier requires that in addition to considering the coercive nature of the

officers’ conduct in a Fourth Amendment seizure analysis, we must also take into

account the defendant’s race. Id. More specifically, we are to consider whether an

objective and reasonable person sharing the defendant’s generalized lived

experiences arising out of their racial status would have felt free to terminate the

police encounter. See id. at 944-45. Our consideration of the defendant’s race

recognizes that a Fourth Amendment seizure inquiry would be incomplete, and

indeed, incongruent with the objective reality that people of color face during

interactions with law enforcement. Id. For people of color, and as relevant here,

Black men, feel “especially apprehensive” around the police such that conduct that
                                              22

may not rise to the level of a seizure without consideration of race, may do so once

the defendant’s race and lived experiences are accounted for. Id. at 944. 4


         To inform our analysis as to the role that Mr. Carter’s status as a Black man

may have played here, it is first important to understand why Black men, generally

speaking, are especially cautious around and more likely to comply with the

demands of law enforcement. There are two central reasons. First, “[i]t is no secret”

that Black Americans are disproportionately likely to be victims of violence at the

hands of police officers, particularly during suspicionless investigatory inquiries like

the one here. Bloom, supra at note 4, at 7 (quoting Strieff, 579 U.S. at 254 (2016)

(Sotomayor, J., dissenting)).       In recent years, nationally, police officers have

threatened or used non-fatal force in roughly three percent of encounters they

initiated or which resulted from a traffic accident. Nazgol Ghandnoosh & Celeste

Barry,       One   in   Five:   Disparities   in   Crime   and   Policing   9   (2023),




        For a more thorough discussion as to why considering the defendant’s race
         4

is consistent with the objective nature of the Fourth Amendment seizure inquiry, see,
e.g., Daniel S. Harawa, Coloring in the Fourth Amendment, 137 Harv. L. Rev. 1533
(2024); Aliza H. Bloom, Objective Enough: Race is Relevant to the Reasonable
Person in Criminal Procedure, 19 Stan. J. C.R. & C.L. 1 (2023); Lindsey Webb,
Legal Consciousness as Race Consciousness: Expansion of the Fourth Amendment
Seizure Analysis Through Objective Knowledge of Police Impunity, 48 Seton Hall
L. Rev. 403 (2018); Devon W. Carbado, (E)Racing the Fourth Amendment, 100
Mich. L. Rev. 946 (2002); Tracey Maclin, “Black and Blue Encounters”—Some
Preliminary Thoughts About Fourth Amendment Seizures: Should Race Matter, 26
Val. U. L. Rev. 243 (1991).
                                         23

https://www.sentencingproject.org/app/uploads/2023/11/One-in-Five-Disparities-

in-Crime-and-Policing.pdf;     https://perma.cc/J367-HYVL.           During     these

interactions, Black individuals were over twice as likely to be subject to force or

threatened force as White individuals. Id. And with regard to fatal force, Black

Americans were over twice as likely to be shot and killed by police officers as White

Americans. Id. Twenty-one percent of Black adults have reported being victims of

police violence on account of their race (compared to three percent of white adults)

and nearly half have stated that they were at some point fearful for their life around

law enforcement (compared to sixteen percent of white adults). Craig Palosky, Poll:

7 in 10 Black Americans Say They Have Experienced Incidents of Discrimination or

Police Mistreatment in their Lifetime, Including Nearly Half Who Felt Their Lives

Were in Danger, KFF (June 18, 2020), https://www.kff.org/racial-equity-and-

health-policy/press-release/poll-7-in-10-black-americans-say-they-have-

experienced-incidents-of-discrimination-or-police-mistreatment-in-lifetime-

including-nearly-half-who-felt-lives-were-in-danger/;        https://perma.cc/RR22-

LDNJ.


      Naturally, this statistical reality has led to the perception among Black

Americans, and Black men in particular, that they are unsafe around law

enforcement and that they must engage in “particular kinds of performances” around

the police to “preempt” and mitigate the risks of “law enforcement discipline.”
                                         24

Carbado, supra at note 4, at 966. Indeed, the inundation of countless stories of young

and unarmed Black men being killed by police for their failure to comply and

generations-worth of experience in dealing with the police within the Black

community have led Black parents to give their children “‘the talk’—instructing

them to never run down the street; always keep [their] hands where they can be seen;

[and to never] even think of talking back to . . . stranger[s]—all out of fear of how

an officer with a gun will react to them.” Strieff, 579 U.S. at 254 (Sotomayor, J.,

dissenting); see Rod K. Brunson, “Police Don’t Like Black People”: African-

American Young Men’s Accumulated Police Experiences, 6 Crim. & Pub. Pol’y 71,

88 (2007) (finding that “violence at the hands of the police . . . happened enough to

convince [Black youth] that it was a real possibility during any encounter with police

officers”); Rayan Succar et al., Understanding the Role of Media in the Formation

of Public Sentiment Towards the Police, Commc’ns Psych (2024) (describing the

influential role of individual media stories of police brutality on perceptions about

the police). Having been raised in this environment, and “being more vulnerable to

police violence” than other demographic groups, Black men are more likely to

comply with police demands rather than exercise their constitutional right to

terminate a suspicionless police encounter. Dozier, 220 A.3d at 945.


      Second, even setting aside the risk of provoking violence, Black Americans

are especially distrustful of law enforcement and are thus less likely to terminate a
                                          25

police encounter due to skepticism that any attempt to exercise their constitutional

rights will be respected. From slave patrols during the antebellum era to Black

Codes post-Reconstruction to disparate charging and sentencing practices today, the

criminal legal system has historically been used as a tool to undermine rather than

uphold the freedom and dignity of Black Americans. See Daniel S. Harawa,

Whitewashing the Fourth Amendment, 111 Geo. L.J. 923, 940 (2023); see generally

Michelle Alexander, The New Jim Crow (2010). Modern-day policing reflects this

history with Black communities disproportionately subject to adverse police

interactions. See Radley Balko, There’s Overwhelming Evidence that the Criminal

Justice System is Racist: Here’s the Proof, Wash. Post (June 10, 2020),

https://perma.cc/ND2K-SUGV (cataloging studies of racial bias in the criminal

justice system, including 46 peer-reviewed studies demonstrating racial bias in

policing and profiling over the prior five years). Black Americans are more likely

to be subject to suspicionless stops and are more likely to be searched and detained

during these stops. Bloom, supra at note 4, at 7, 13 (citing U.S. Dep’t Justice,

Investigation    of    the     Ferguson        Police    Department     4    (2015),

https://www.justice.gov/sites/default/files/opa/press-

releases/attachments/2015/03/04/ferguson_police_department_report.pdf;

https://perma.cc/ZBT9-7BJP (concluding that Black drivers were “more than twice

as likely as white drivers to be searched during vehicle stops even after controlling
                                         26

for non-race variables”)). Black men in particular also tend to be questioned more

accusatorily and aggressively—a product of both historical tension between law

enforcement and the Black community and, as social science research suggests,

stereotyping of Black men as being dangerous and criminally predisposed. Carbado,

supra at note 4, at 982; Graham Cronogue, Race and the Fourth Amendment: Why

the Reasonable Person Analysis Should Include Race as a Factor, 20 Tex. J. C.L &

C.R. 61 (2015). That is, whereas a police officer’s objective in questioning a White

individual will be to simply “check things out,” they will often “need more time with

and more information from the” Black individual given their perception that the

Black individual is more likely to engage in criminal activity. Carbado, supra at

note 4, at 982.


      It should therefore come as “no surprise” that Black Americans “often

perceive their interactions with law enforcement differently than other

demographics.” State v. Spears, 839 S.E.2d 450, 463 (S.C. 2020) (Beatty, C.J.,

dissenting). Eighty-four percent of Black adults have said that in dealing with the

police, Black Americans are generally treated less fairly than other demographic

groups. Drew DeSilver et al., 10 Things we Know About Race and Policing in the

U.S., Pew Rsch. Ctr. (June 3, 2020), https://www.pewresearch.org/short-

reads/2020/06/03/10-things-we-know-about-race-and-policing-in-the-u-s/;

https://perma.cc/RH4E-D3UA. Eighty-seven percent have said that the criminal
                                          27

legal system as a whole treats Black Americans less fairly. Id. Such distrust, sown

both historically through the use of the criminal legal system to subjugate Black

Americans and via biased modern police practices, has produced an objective reality

in which Black Americans lack confidence that the police will respect the exercise

of their rights. Maclin, supra at note 4, at 254. Rather, to avoid suffering physical

abuse and criminal consequences during suspicionless police interactions, Black

Americans, and Black men in particular, are often left with no other choice but to

remain “calm” and “congenial” and comply with the requests of law enforcement.

Id. at 278.


      Applying this understanding as to why Black men are especially apprehensive

around police, it is clear that many of the historical features of blue-on-black

interaction that have led to this perception were present in Mr. Carter’s encounter.

First, Mr. Carter was confronted in a predominantly Black area in a group consisting

entirely of Black men by GRU officers who were wearing tactical gear and who

were visibly displaying their firearms. This alone was likely sufficient to trigger the

elevated fear that Black men experience around law enforcement not only because

the officers were carrying openly visible firearms but also because their selective

targeting reflected a pervasive understanding that the police target Black men and

treat them unfairly. Moreover, the GRU (now the VCIT) has a “reputation for

[aggression].” Mayo, 315 A.3d at 631; Robinson, 76 A.3d at 331-32, 339 (noting
                                           28

GRU’s acknowledged “technique” of confronting people on the street, “ask[ing]

people if they have a gun,” and then “looking for a reaction,” including people’s

“movements” in response to the question (internal quotation marks omitted)); United

States v. Gibson, 366 F. Supp. 3d 14, 21 (D.D.C. 2018) (describing how the GRU

“trawl[s]” certain “neighborhoods asking occupants who fit a certain statistical

profile—mostly males in their late teens to early forties—if they possess contraband[

] [d]espite lacking any semblance of particularized suspicion when the initial contact

is made” (quoting United States v. Gross, 784 F.3d 784, 789 (D.C. Cir. 2015)

(Brown, J., concurring))). It is also known to selectively target Black individuals.

See Michael G. Tobin, Metropolitan Police Department Narcotics and Specialized

Investigations          Division           5,          20,          26,          (2020),

https://policecomplaints.dc.gov/sites/default/files/dc/sites/office%20of%20police%

20complaints/publication/attachments/National%20Police%20Foundation%20MP

D%20NSID%20Report%20September%202020%20Final.pdf;

https://perma.cc/S29N-PMF7 (reporting that between August 1, 2019 and January

31, 2020, Black individuals were the subject of over 87% of GRU stops, 91% of

arrests, and 100% of use-of-force incidents). Given this background, it should not

come as a shock that several of the men in Mr. Carter’s group immediately

capitulated to the police presence, including Mr. Carter, by raising their shirts despite

not being asked to. Indeed, whereas any reasonable person would be fearful of
                                           29

failing to cooperate under these circumstances, a Black man would be especially

cautious here so as to avoid potential physical retaliation. 5


      Second, compounding the already racially charged and coercive environment

in which Mr. Carter’s interaction with the police took place, Officer DelBorrell

accusatorily and repetitively questioned him regarding whether he possessed a

firearm. As explained above, Black men already widely believe that police officers

disrespect their rights. We view it as likely that Officer DelBorrell’s failure to accept

Mr. Carter’s initial denial triggered a fear that Officer DelBorrell would not permit

Mr. Carter to terminate the encounter without first dispelling his suspicions. To

avoid prolonging the suspicion, Mr. Carter felt compelled to comply rather than

attempt to exercise his constitutional rights.




      5
         The VCIT and similar police tactical units that engage in large-scale
suspicionless investigations are generally distinguishable from those police units
that are engaged in what many refer to as community policing activities. Generally
speaking, community policing promotes the systematic use of partnerships and
problem-solving techniques to proactively address the conditions that give rise to
public safety issues. U.S. Dep’t Justice, Community Policing Defined 1 (2014),
https://portal.cops.usdoj.gov/resourcecenter/content.ashx/cops-p157-pub.pdf;
https://perma.cc/9GU6-CNH7. Typically, police officers are assigned to particular
communities where they get to know and work with community leaders and others
to address the immediate conditions that give rise to public safety issues.
                                          30

                                   III.   Conclusion


      Accordingly, taking into account the coercive nature of the officers’ conduct

and factoring in the elevated effect that this would have had on an objective and

reasonable Black man in Mr. Carter’s shoes, we hold that Mr. Carter was seized

within the meaning of the Fourth Amendment when Officer DelBorrell requested

that he raise his pants. The combination of the impressive show of authority

reflected in the officers’ initial approach and the accusatory and repetitive nature of

Officer DelBorrell’s questioning already resembled a scenario in which we held a

seizure took place. Compounding the compulsive effect of the police tactics here

was that they were used against a man for whom, by virtue of his race and lived

experiences, it would have been objectively reasonable to be apprehensive around

police officers. Given the facts of this case, we believe that such apprehension would

have led an objective and reasonable Black man in Mr. Carter’s shoes to feel as

though he had to comply with the officers’ demands rather than terminating the

encounter. For this reason, we are satisfied that Mr. Carter was seized when Officer

Delborrell disbelieved his initial response, and further requested that he raise his

pants. Because this seizure was not based on reasonable suspicion or probable cause,

it was unreasonable and violated the Fourth Amendment. The trial court thus erred

in failing to suppress the fruits of the seizure—the firearm and Mr. Carter’s later

statement.
                                          31

      For the foregoing reasons, we vacate Mr. Carter’s convictions and remand for

further proceedings.


                                                            So ordered.


      MCLEESE, Associate Judge, concurring in the judgment: The opinion for the

court holds that Mr. Carter was unlawfully seized. Ante at 30. I respectfully concur

in the judgment.


      As the opinion for the court notes, the key facts are undisputed: (1) in public

and during the daytime, a group of five officers approached a group of ten men that

included Mr. Carter; (2) one of the officers asked Mr. Carter how he was doing;

(3) Mr. Carter lifted his shirt to show his waistband; (4) the officer asked if Mr.

Carter had “nothing” on him; (5) Mr. Carter responded no and lifted his shirt again;

and (6) the officer asked if Mr. Carter “mind[ed] hiking [his] pants for me real

quick?” Ante at 2-4.


      Describing the case as “close,” ante at 9, the opinion for the court appears to

give dispositive weight to an additional consideration: that Mr. Carter as a Black

man would reasonably be “especially apprehensive around police” and “especially

distrustful of law enforcement,” ante at 24, 27, and therefore would reasonably have

felt obliged to comply with the officer’s request to hike up his pants, ante at 30.
                                         32

      In support of the conclusion that Mr. Carter’s race is properly considered in

determining whether Mr. Carter was seized, the opinion for the court relies on this

court’s decision in Dozier v. United States, 220 A.3d 933 (D.C. 2019). I concurred

in the judgment in Dozier. Id. at 948-51 (McLeese, J., concurring in the judgment).

Among other things, I expressed uncertainty as to whether the race of a suspect can

permissibly be considered in assessing whether police conduct constitutes a seizure.

Id. at 950-51 (citing conflicting authority on issue). The opinion for the court in

Dozier held, however, that Mr. Dozier’s race should be so considered. Id. at 943-45.

That holding is binding on me. E.g., M.A.P. v. Ryan, 285 A.2d 310, 312 (D.C. 1971).


      Taking as a given that Mr. Carter’s race may properly be considered, I agree

with the conclusion of the opinion for the court that, although this is a close case,

Mr. Carter was seized. Ante at 9, 30. I therefore respectfully concur in the judgment.

```

---
