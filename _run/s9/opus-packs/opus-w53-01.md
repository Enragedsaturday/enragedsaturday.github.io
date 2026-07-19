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

## GROUP: content/cases/United States v. Havens.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Havens"
type: case
citation: "446 U.S. 620 (1980)"
parallel_cite: "100 S. Ct. 1912; 64 L. Ed. 2d 559"
neutral_cite: 1980 U.S. LEXIS 103
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-08-11
docket: 79-305
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Havens
  varies_by_point: false
  scope_note: "Extends Walder's impeachment exception to cross-examination reasonably suggested by direct; remains good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110267/united-states-v-havens/"
  cluster_id: 110267
  opinion_id: 9427937
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny (impeachment exception)"
related: ["[[Walder v. United States]]", "[[Agnello v. United States]]", "[[James v. Illinois]]", "[[Weeks v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "impeachment-exception", "cross-examination"]
holding: "Illegally seized evidence may be used to impeach a defendant's false statements first elicited on cross-examination, so long as that cross-examination was reasonably suggested by the defendant's direct testimony; such evidence remains inadmissible as substantive proof of guilt."
lake:
  record_id: United States v. Havens
  status: verified
  projected_at: 2026-07-06
---

# United States v. Havens

*446 U.S. 620 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Havens and McLeroth flew from Peru to Miami; cocaine was found taped to McLeroth's body in cotton swatches sewn to a T-shirt, and McLeroth implicated Havens. A warrantless customs search of Havens's luggage turned up a T-shirt with pieces cut out matching the swatches; that T-shirt was suppressed as the fruit of an unlawful search. At trial, McLeroth testified Havens helped prepare the T-shirt. On direct, Havens denied "ever engag[ing] in that kind of activity"; on cross, the Government asked whether he helped sew the swatches, he denied it, and the Government then introduced the suppressed T-shirt to impeach him.

## Issue
Whether illegally seized evidence may be used to impeach a defendant's false statements first elicited on cross-examination, where that cross-examination was reasonably suggested by his direct testimony.

## Rule
Yes. For impeachment, "we see no difference of constitutional magnitude between the defendant's statements on direct examination and his answers to questions put to him on cross-examination that are plainly within the scope of the defendant's direct examination." — 446 U.S. at 627. ^pin-627

"We reaffirm this assessment of the competing interests, and hold that a defendant's statements made in response to proper cross-examination reasonably suggested by the defendant's direct examination are subject to otherwise proper impeachment by the government, albeit by evidence that has been illegally obtained and that is inadmissible on the government's direct case, or otherwise, as substantive evidence of guilt." — *Id.* at 627–628. ^pin-627b

## Application
Havens's direct testimony — denying that he had "ever engage[d] in that kind of activity with Mr. McLeroth" — could reasonably be understood as denying any connection with the T-shirt and contradicting McLeroth. The Government's cross-examination about sewing the cotton swatches "grow[ing] out of Havens' direct testimony" was therefore proper, and the suppressed T-shirt could be used to impeach his false denial — though not as substantive evidence of guilt. The Fifth Circuit's narrower rule (impeachment only of statements made on direct) was rejected.

## Conclusion
Because the impeachment followed proper cross-examination reasonably suggested by the direct, it did not violate Havens's constitutional rights; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Havens* extends the impeachment exception of [[Walder v. United States]] (distinguishing [[Agnello v. United States]]) from direct examination to cross-examination reasonably suggested by direct. The Court later declined to extend the exception to other defense witnesses in [[James v. Illinois]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny (impeachment exception)*

## Sources
- *United States v. Havens*, 446 U.S. 620 (1980) — https://www.courtlistener.com/opinion/110267/united-states-v-havens/ — pinpoints: 627–628.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8ec74a7c9db58fdc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "446 U.S. 620 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 103", "official_citation_present": true, "parallel_cite": "100 S. Ct. 1912; 64 L. Ed. 2d 559", "title": "United States v. Havens", "year": "1980"}}
{"assertion_id": "de76e9b361a0204f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Illegally seized evidence may be used to impeach a defendant's false statements first elicited on cross-examination, so long as that cross-examination was reasonably suggested by the defendant's direct testimony; such evidence remains inadmissible as substantive proof of guilt.", "title": "United States v. Havens"}}
{"assertion_id": "fe49adbd52e2109b", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Progeny (impeachment exception)", "title": "United States v. Havens"}}
{"assertion_id": "42c69fffa38a0f7c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Havens"}}
{"assertion_id": "c99302b9486040a9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-05-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Havens", "field_i_validity": "good_law", "scope_note": "Extends Walder's impeachment exception to cross-examination reasonably suggested by direct; remains good law.", "title": "United States v. Havens", "varies_by_point": "false"}}
```

### lake record — United States v. Havens

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Havens",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Havens",
    "case_name_short": "Havens",
    "case_name_full": "United States v. Havens",
    "input_case_name": "United States v. Havens",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-08-11",
    "year": 1980,
    "docket": "79-305",
    "cluster_id": 110267,
    "lead_opinion_id": 9427937,
    "sibling_ids": [
      110267,
      9427937,
      9427938
    ],
    "absolute_url": "/opinion/110267/united-states-v-havens/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "446 U.S. 620",
      "volume": "446",
      "reporter": "U.S.",
      "page": "620",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1912",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1912",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 559",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 103",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "446 U.S. 620",
        "volume": "446",
        "reporter": "U.S.",
        "page": "620",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1912",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1912",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 559",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 103",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "446 U.S. 620",
    "official_selection": {
      "court_class": "scotus",
      "selected": "446 U.S. 620",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-627",
      "page": null,
      "quote": "; on cross, the Government asked whether he helped sew the swatches, he denied it, and the Government then introduced the suppressed T-shirt to impeach him. ## Issue Whether illegally seized evidence may be used to impeach a defendant's false statements first elicited on cross-examination, where that cross-examination was reasonably suggested by his direct testimony. ## Rule Yes. For impeachment,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-627b",
      "page": null,
      "quote": "We reaffirm this assessment of the competing interests, and hold that a defendant's statements made in response to proper cross-examination reasonably suggested by the defendant's direct examination are subject to otherwise proper impeachment by the government, albeit by evidence that has been illegally obtained and that is inadmissible on the government's direct case, or otherwise, as substantive evidence of guilt.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Havens",
    "varies_by_point": false,
    "scope_note": "Extends Walder's impeachment exception to cross-examination reasonably suggested by direct; remains good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Mendes",
          "cluster_id": 6589481,
          "cite": [
            "78 Mass. App. Ct. 474",
            "940 N.E.2d 467",
            "2010 Mass. App. LEXIS 1666"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Castillo-Basa",
          "cluster_id": 3047445,
          "cite": [
            "478 F.3d 1025",
            "2007 U.S. App. LEXIS 4144",
            "2007 WL 570326"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James David Nichols, United States of America v. James David Nichols",
          "cluster_id": 793364,
          "cite": [
            "438 F.3d 437",
            "2006 WL 464130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agim Baftiri",
          "cluster_id": 774763,
          "cite": [
            "263 F.3d 856",
            "2001 U.S. App. LEXIS 19334",
            "2001 WL 987524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barry Mark Hall",
          "cluster_id": 603523,
          "cite": [
            "989 F.2d 711",
            "38 Fed. R. Serv. 239",
            "1993 U.S. App. LEXIS 4177",
            "1993 WL 57543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane1_negative"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunnigan",
          "cluster_id": 112821,
          "cite": [
            "122 L. Ed. 2d 445",
            "113 S. Ct. 1111",
            "507 U.S. 87",
            "1993 U.S. LEXIS 1779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Whiteside",
          "cluster_id": 111603,
          "cite": [
            "89 L. Ed. 2d 123",
            "106 S. Ct. 988",
            "475 U.S. 157",
            "1986 U.S. LEXIS 8",
            "54 U.S.L.W. 4194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
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
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Johnson",
          "cluster_id": 4889243,
          "cite": [
            "2021 CO 35"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banek v. Thomas",
          "cluster_id": 1244295,
          "cite": [
            "733 P.2d 1171",
            "1986 Colo. LEXIS 678"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Electroplating, Inc.",
          "cluster_id": 1082668,
          "cite": [
            "990 S.W.2d 211",
            "1998 Tenn. Crim. App. LEXIS 618",
            "1998 WL 301728"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huizar",
          "cluster_id": 1764122,
          "cite": [
            "414 So. 2d 741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Huddleston",
          "cluster_id": 2435833,
          "cite": [
            "924 S.W.2d 666",
            "1996 Tenn. LEXIS 387",
            "1996 WL 328642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin M. Clark v. State of Indiana",
          "cluster_id": 1041668,
          "cite": [
            "994 N.E.2d 252",
            "2013 WL 5228498",
            "2013 Ind. LEXIS 700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gilley",
          "cluster_id": 4282804,
          "cite": [
            "56 M.J. 113",
            "2001 CAAF LEXIS 1378",
            "2001 WL 1441832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Stevens",
          "cluster_id": 563201,
          "cite": [
            "935 F.2d 1380",
            "33 Fed. R. Serv. 831",
            "1991 U.S. App. LEXIS 11861"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "LaChance v. Erickson",
          "cluster_id": 118163,
          "cite": [
            "139 L. Ed. 2d 695",
            "118 S. Ct. 753",
            "522 U.S. 262",
            "1998 U.S. LEXIS 636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tomblin",
          "cluster_id": 6970,
          "cite": [
            "46 F.3d 1369"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cipriano",
          "cluster_id": 1844552,
          "cite": [
            "429 N.W.2d 781",
            "431 Mich. 315"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Ruhe",
          "cluster_id": 766122,
          "cite": [
            "191 F.3d 376",
            "1999 U.S. App. LEXIS 20861",
            "1999 WL 674758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Winsett",
          "cluster_id": 2036163,
          "cite": [
            "606 N.E.2d 1186",
            "153 Ill. 2d 335",
            "180 Ill. Dec. 109",
            "1992 Ill. LEXIS 179"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Havens:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110267 OR 9427937 OR 9427938) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTY4MTYwMDAwMDAmcz0xNzc2MjAwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110267+OR+9427937+OR+9427938%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110267 OR 9427937 OR 9427938)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQmcz0yMDkzMzE4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110267+OR+9427937+OR+9427938%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110267 OR 9427937 OR 9427938)",
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
    "complete_query": "cites:(110267 OR 9427937 OR 9427938)",
    "indexed_citing_opinions": 436,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110267,
        "count": 398,
        "count_source": "search"
      },
      {
        "opinion_id": 9427937,
        "count": 48,
        "count_source": "search"
      },
      {
        "opinion_id": 9427938,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 665,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-havens.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU4MTY1NzYmcz00NDg4MzgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110267+OR+9427937+OR+9427938%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110267,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 105661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 108001,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 108002,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 109658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 110216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110267,
        "cited_id": 363621,
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
    "date_created": "2026-07-06T00:27:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:27:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:27:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:33:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:27:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Havens

```
<opinion type="majority">
<author id="b679-9">Mr. Justice White</author>
<p id="Al5">delivered the opinion of the Court.</p>
<p id="AL8">The petition for certiorari filed by the United States in this criminal case presented a single question: whether evidence suppressed as the fruit of an unlawful search .and seizure may nevertheless be used to impeach a defendant's false trial testimony, given in response to proper cross-examination, where the evidence does not squarely contradict the defendant's testimony on direct examination. We issued the writ, <span class="citation multiple-matches"><a href="/c/U.%20S./444/962/">444 U. S. 962</a></span> (1979).</p>
<p id="b679-10">I</p>
<p id="b679-11">Respondent was convicted of importing, conspiring to import, and intentionally possessing a controlled substance, cocaine. According to the evidence at his trial, Havens and John McLeroth, both attorneys from Ft. Wayne, Ind., boarded a flight from Lima, Peru, to Miami, Fla. In Miami, a customs officer searched McLeroth and found cocaine sewed into makeshift pockets in a T-shirt he was wearing under his outer <page-number citation-index="1" label="622">*622</page-number>clothing. McLeroth implicated respondent, who had previously cleared customs and who was then arrested. His luggage was seized and searched without a warrant. The officers found no drugs but seized a T-shirt from which pieces had been cut that matched the pieces that had been sewn to McLeroth’s T-shirt. The T-shirt and other evidence seized in the course of the search were suppressed on motion prior to trial.</p>
<p id="b680-5">Both men were charged in a three-count indictment, but McLeroth pleaded guilty to one count and testified against Havens. Among other things, he asserted that Havens had supplied him with the altered T-shirt and had sewed the makeshift pockets shut. Havens took the stand in his own defense and denied involvement in smuggling cocaine. His direct testimony included the following:</p>
<blockquote id="b680-6">“Q. And you heard Mr. McLeroth testify earlier as to something to the effect that this material was taped or draped around his body and so on, you heard that testimony?</blockquote>
<blockquote id="b680-7">“A. Yes, I did.</blockquote>
<blockquote id="b680-8">“Q. Did you ever engage in that kind of activity with Mr. McLeroth and Augusto or Mr. McLeroth and anyone else on that fourth visit to Lima, Peru?</blockquote>
<blockquote id="b680-9"><em>“A. </em>I did not.” App. 34.</blockquote>
<p id="b680-10">On cross-examination, Havens testified as follows:</p>
<blockquote id="b680-11">“Q. Now, on direct examination, sir, you testified that on the fourth trip you had absolutely nothing to do with the wrapping of any bandages or tee shirts or anything involving Mr. McLeroth; is that correct?</blockquote>
<blockquote id="b680-12">“A. I don’t — I said I had nothing to do with any wrapping or bandages or anything, yes. I had nothing to do with anything with McLeroth in connection with this cocaine matter.</blockquote>
<blockquote id="pAI1">
<img class="blockquote" height="26" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA/0AAAAaAQAAAADN7QFqAAAAsUlEQVR4nO2VMQrDMBAEV3KTMk8I5AH5gp6mp+Up16WM7MoyBKWISbl32BwOQduoGKQdjgOFhkNT47H9QBfQBBZKJ0pN66UJPCh9ZkYnSlsyCQh9ROjdcmd0EZOAElrBM5dVoGavCmVAWAVmXpF2CFxMAkV2NKTtd78CSkWmmNJzYvT0OUIbb6JIbM1roPQqcP4LaD8GAQBE26r4JTQ+KO/UqAzKPT//G3aBLtAF/l/gDSI/JmCmgfXUAAAAAElFTkSuQmCC" width="1022"/>
</blockquote>
<blockquote id="b680-13">“Q. And your testimony is that you had nothing to <page-number citation-index="1" label="623">*623</page-number>do with the sewing of the cotton swatches to make pockets on that tee shirt?</blockquote>
<blockquote id="b681-4">“A. Absolutely not.</blockquote>
<blockquote id="b681-5">“Q. Sir, when you came through Customs, the Miami International Airport, on October 2, 1977, did you have in your suitcase Size 38-40 medium tee shirts?” <em>Id., </em>at 35.</blockquote>
<p id="b681-6">An objection to the latter question was overruled and questioning continued:</p>
<blockquote id="b681-7">“Q. On that day, sir, did you have in your luggage a Size 38-40 medium man’s tee shirt with swatches of clothing missing from the tail of that tee shirt?</blockquote>
<blockquote id="b681-8">“A. Not to my knowledge.</blockquote>
<blockquote id="pAUsh">
<img class="blockquote" height="30" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA9sAAAAeAQAAAAAUPzDrAAAAiklEQVR4nO2WoQ2AMBBFrzUYBOMgEIyFrCCBmVBIJCPQsAASEsKxAPkVF1Lzn329vhNNwKlkI/p8bRHGGWeccca/WQyzVzq+QttAi1c7g/jEkRraB9oJ2mMWj7fXG15gxGf8nhsfnGW6alPjDuveEC+DiBaKGKDF7Am/OR07w/omouMPJOOMM/4nL2CEjr/ehDkqAAAAAElFTkSuQmCC" width="988"/>
</blockquote>
<blockquote id="b681-9">“Q. Mr. Havens, I’m going to hand you what is Government’s Exhibit 9 for. identification and ask you if this tee shirt was in your luggage on October 2nd, 1975 [sic] ?</blockquote>
<blockquote id="b681-10">“A. Not to my knowledge. No.” <em>Id., </em>at 46.</blockquote>
<p id="b681-11">Respondent Havens also denied having told a Government agent that the T-shirts found in his luggage belonged to McLeroth.</p>
<p id="b681-12">On rebuttal, a Government agent testified that Exhibit 9 had been found in respondent’s suitcase and that Havens claimed the T-shirts found in his bag, including Exhibit 9, belonged to McLeroth. Over objection, the T-shirt was then admitted into evidence, the jury being instructed that the rebuttal evidence should be considered only for impeaching Havens’ credibility.</p>
<p id="b681-13">The Court of Appeals reversed, relying on <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span> (1925), and <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). The court held that illegally seized evidence may be used for impeachment only if the evidence contradicts a particular statement made by a defendant in the course of his direct examination. <span class="citation" data-id="363621"><a href="/opinion/363621/united-states-v-j-lee-havens/" aria-description="Citation for case: United States v. J. Lee Havens">592 F. 2d 848</a></span> (CA5 1979). We reverse.</p>
<p id="b682-4"><page-number citation-index="1" label="624">*624</page-number>II</p>
<p id="b682-5">In <em>Agnello </em>v. <em>United States, supra, </em>a defendant charged with conspiracy to sell a package, of cocaine testified on direct examination that he had possessed the packages involved but did not know what was in them. On cross-examination, he denied ever having seen narcotics and ever having seen a can of cocaine which was exhibited to him and which had been illegally seized from his apartment. The can of cocaine was permitted into evidence on rebuttal. Agnello was convicted and his conviction was affirmed by the Court of Appeals. This Court reversed, holding that the Fourth Amendment required exclusion of the evidence. The Court pointed out that “[i]n his direct examination, Agnello was not asked and did not testify concerning the can of cocaine” and “did nothing to waive his constitutional protection or to justify cross-examination in respect of the evidence claimed to have been obtained by the search.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#35" aria-description="Citation for case: Agnello v. United States">269 U. S., at 35</a></span>. The Court also said, quoting from <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920), that the exclusionary rule not only commands that illegally seized evidence “shall not be used before the Court but that it shall not be used at all.” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#35" aria-description="Citation for case: Agnello v. United States">269 U. S., at 35</a></span>.</p>
<p id="b682-6">The latter statement has been rejected in our later cases, however, and <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>otherwise limited. In <em>Walder </em>v. <em>United States, supra, </em>the use of evidence obtained in an illegal search and inadmissible in the Government’s case in chief was admitted to impeach the direct testimony of the defendant. This Court approved, saying that it would pervert the rule of <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), to hold otherwise. Similarly, in <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), and <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714</a></span> (1975), statements taken in violation of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and unusable by the prosecution as part of its own case, were held admissible to impeach statements made by the defendant in the course of his direct testimony. <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em><page-number citation-index="1" label="625">*625</page-number>also made clear that the permitted impeachment by otherwise inadmissible evidence is not limited to collateral matters. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York">401 U. S., at 225</a></span>.</p>
<p id="b683-5">These cases were understood by the Court of Appeals to hold that tainted evidence, inadmissible when offered as part of the Government’s main case, may not be used as rebuttal evidence to impeach a defendant’s credibility unless the evidence is offered to contradict a particular statement made by a defendant during his direct examination; a statement made for the first time on cross-examination may not be so impeached. This approach required the exclusion of the T-shirt taken from Havens’ luggage because, as the Court of Appeals read the record, Havens was asked nothing on his direct testimony about the incriminating T-shirt or about the contents of his luggage; the testimony about the T-shirt, which the Government desired to impeach first appeared on cross-examination, not on direct.</p>
<p id="b683-6">It is true that <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>involved the impeachment of testimony first brought out on cross-examination and that in <em>Walder, Harris, </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span>, </em>the testimony impeached was given by the defendant while testifying on direct examination. In our view, however, a flat rule permitting only statements on direct examination to be impeached misapprehends the underlying rationale of <em>Walder, Harris, </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span>. </em>These cases repudiated the statement in <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>that no use at all may be made of illegally obtained evidence. - Furthermore, in <em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span>, </em>the Court said that in <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span>, </em>the Government had “smuggled in” the impeaching opportunity in the course of cross-examination. The Court also relied on the statement in <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#35" aria-description="Citation for case: Agnello v. United States"><em>Agnello, supra, </em>at 35</a></span>, that Agnello had done nothing “to justify cross-examination in respect of the evidence claimed to have been obtained by the search.” The implication of <em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span> </em>is that <em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span> </em>was a case of cross-examination having too tenuous a connection with any subject opened upon direct examination to permit impeachment by tainted evidence.</p>
<p id="b684-3"><page-number citation-index="1" label="626">*626</page-number>In reversing the District Court in the case before us, the Court of Appeals did not stop to consider how closely the cross-examination about the T-shirt and the luggage was connected with matters gone into in direct examination. If these questions would have been suggested to a reasonably competent cross-examiner by Havens’ direct testimony, they were not “smuggled in”; and forbidding the Government to impeach the answers to these questions by using contrary and reliable evidence in its possession fails to take account of our cases, particularly <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span>. </em>In both cases, the Court stressed the importance of arriving at the truth in criminal trials, as well as the defendant’s obligation to speak the truth in response to proper questions. We rejected the notion that the defendant’s constitutional shield against having illegally seized evidence used against him could be “perverted into a license to use perjury by way of a defense, free from the risk of confrontation with prior inconsistent utterances.” <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#226" aria-description="Citation for case: Harris v. New York">401 U. S., at 226</a></span>. See also <em>Oregon </em>v. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at 722, 723</a></span>. Both cases also held that the deterrent function of the rules excluding unconstitutionally obtained evidence is sufficiently served by denying its use to the government on its direct case. It was only a “speculative possibility” that also making it unavailable to the government for otherwise proper impeachment would contribute substantially in this respect. <em>Harris </em>v. <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><em>New York, supra, </em>at 225</a></span>. <em>Oregon </em>v. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#723" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at 723</a></span>.</p>
<p id="b684-4">Neither <em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">Harris</a></span> </em>nor <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>involved the impeachment of assertedly false testimony first given on cross-examination, but the reasoning of those cases controls this one. There is no gainsaying that arriving at the truth is a fundamental goal of our legal system. <em>Oregon </em>v. <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#722" aria-description="Citation for case: Oregon v. Hass"><em>Hass, supra, </em>at 722</a></span>. We have repeatedly insisted that when defendants testify, they must testify truthfully or suffer the consequences. This is true even though a defendant is compelled to testify against his will. <em>Bryson </em>v. <em>United States, </em><span class="citation" data-id="9424114"><a href="/opinion/108001/bryson-v-united-states/#72" aria-description="Citation for case: Bryson v. United States">396 U. S. 64, 72</a></span> (1969); <em>United States </em>v. <em>Knox, </em><span class="citation" data-id="9841978"><a href="/opinion/108002/united-states-v-knox/" aria-description="Citation for case: United States v. Knox">396 U. S. 77</a></span> (1969). It is essential, <page-number citation-index="1" label="627">*627</page-number>therefore, to the proper functioning of the adversary system that when a defendant takes the stand, the government be permitted proper and effective cross-examination in an attempt to elicit the truth. The defendant’s obligation to testify truthfully is fully binding on him when he is cross-examined. His privilege against self-incrimination does not shield him from proper questioning. <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="9421572"><a href="/opinion/105661/brown-v-united-states/#154" aria-description="Citation for case: Brown v. United States">356 U. S. 148, 154-155</a></span> (1958). He would unquestionably be subject to a perjury prosecution if he knowingly lies on cross-examination. Cf. <em>United States </em>v. <em>Apfelbaum, </em><span class="citation" data-id="9427814"><a href="/opinion/110216/united-states-v-apfelbaum/" aria-description="Citation for case: United States v. Apfelbaum">445 U. S. 115</a></span> (1980); <em>Bryson </em>v. <em>United States, supra; United States </em>v. <em><span class="citation" data-id="9841978"><a href="/opinion/108002/united-states-v-knox/" aria-description="Citation for case: United States v. Knox">Knox, supra;</a></span> United States </em>v. <em>Wong, </em><span class="citation" data-id="109658"><a href="/opinion/109658/united-states-v-wong/" aria-description="Citation for case: United States v. Wong">431 U. S. 174</a></span> (1977). In terms of impeaching a defendant’s seemingly false statements with his prior inconsistent utterances or with other reliable evidence available to the government, we see no difference of constitutional magnitude between the defendant’s statements on direct examination and his answers to questions put to him on cross-examination that are plainly within the scope of the defendant’s direct examination. Without this opportunity, the normal function of cross-examination would be severely impeded.</p>
<p id="b685-5">We also think that the policies of the exclusionary rule no more bar impeachment here than they did in <em>Walder, Harris, </em>and <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span>. </em>In those cases, the ends of the exclusionary rules were thought adequately implemented by denying the government the use of the challenged evidence to make out its ease in chief. The incremental furthering of those ends by forbidding impeachment of the defendant who testifies was deemed insufficient to permit or require that false testimony go unchallenged, with the resulting impairment of the integrity of the factfinding goals of the criminal trial. We reaffirm this assessment of the competing interests, and hold that a defendant’s statements made in response to proper cross-examination reasonably suggested by the defendant’s direct examination are subject to otherwise proper impeach<page-number citation-index="1" label="628">*628</page-number>ment by the government, albeit by evidence that has been illegally obtained and that is inadmissible on the government’s direct case, or otherwise, as substantive evidence of guilt.</p>
<p id="b686-5">In arriving at its judgment, the Court of Appeals noted that in response to defense counsel’s objection to the impeaching evidence on the ground that the matter had not been “covered on direct,” the trial court had remarked that “[i]t does not have to be covered on direct.” The Court of Appeals thought this was error since in its view illegally seized evidence could be used only to impeach a statement made on direct examination. As we have indicated, we hold a contrary view; and we do not understand the District Court to have indicated that the Government’s question, the answer to which is sought to be impeached, need not be proper cross-examination in the first instance. The Court of Appeals did not suggest that either the cross-examination or the impeachment of Havens would have been improper absent the use of illegally seized evidence, and we cannot accept respondent’s suggestions that because of the illegal search and seizure, the Government’s questions about the T-shirt were improper cross-examination. McLeroth testified that Havens had assisted him in preparing the T-shirt for smuggling. Havens, in his direct testimony, acknowledged McLeroth’s prior testimony that the cocaine “was taped or draped around his body and so on” but denied that he had “ever engage [d] in that kind of activity with Mr. McLeroth. . . .” This testimony could easily be understood as a denial of any connection with McLeroth’s T-shirt and as a contradiction of McLeroth’s testimony. Quite reasonably, it seems to us, the Government on cross-examination called attention to his answers on direct and then asked whether he had anything to do with sewing the cotton swatches on McLeroth’s T-shirt. This was cross-examination growing out of Havens’ direct testimony; and, as we hold above, the ensuing impeachment did not violate Havens’ constitutional rights.</p>
<p id="b687-4"><page-number citation-index="1" label="629">*629</page-number>We reverse the judgment of the Court of Appeals and remand the case to that court for further proceedings consistent with this opinion.</p>
<p id="b687-5">
<em>So ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/United States v. Henry.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Henry"
type: case
citation: "447 U.S. 264 (1980)"
parallel_cite: "100 S. Ct. 2183; 65 L. Ed. 2d 115"
neutral_cite: 1980 U.S. LEXIS 111
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-16
docket: 79-121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Henry
  varies_by_point: false
  scope_note: "Cabined by Kuhlmann v. Wilson (a passive 'listening post' informant who does not deliberately elicit does not violate the Sixth Amendment); Henry itself remains good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110300/united-states-v-henry/"
  cluster_id: 110300
  opinion_id: 9427972
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Brewer v. Williams]]", "[[Kuhlmann v. Wilson]]", "[[Maine v. Moulton]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "jailhouse-informant", "deliberately-elicited", "massiah"]
holding: "By intentionally creating a situation likely to induce the indicted defendant to make incriminating statements, the government (through…"
lake:
  record_id: United States v. Henry
  status: verified
  projected_at: 2026-07-06
---

# United States v. Henry

*447 U.S. 264 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Henry was indicted for armed robbery and held in jail awaiting trial. Government agents had a paid informant, Nichols — a fellow inmate in Henry's cellblock — report on Henry, instructing him not to question Henry but to be alert to statements. Nichols engaged Henry in conversation, and Henry made incriminating remarks about the robbery that were used at trial. Nichols was paid on a contingent-fee basis for producing useful information.

## Issue
Whether the government "deliberately elicited" incriminating statements from an indicted, incarcerated defendant, in violation of his Sixth Amendment right to counsel under *[[Massiah v. United States|Massiah]]*, when it used a paid jailhouse informant posing as a fellow inmate.

## Rule
Yes. The Sixth Amendment, as construed in [[Massiah v. United States]], bars the government from "deliberately elicit[ing]" incriminating statements from an indicted defendant in the absence of counsel. Whether elicitation was deliberate turns on the circumstances: "Three factors are important. First, Nichols was acting under instructions as a paid informant for the Government; second, Nichols was ostensibly no more than a fellow inmate of Henry; and third, Henry was in custody and under indictment at the time he was engaged in conversation by Nichols." — 447 U.S. at 270. ^pin-270

Applying those factors, the Court held: "By intentionally creating a situation likely to induce Henry to make incriminating statements without the assistance of counsel, the Government violated Henry's Sixth Amendment right to counsel." — *Id.* at 274. ^pin-274

## Application
On these facts the government deliberately elicited the statements even without express interrogation. Nichols was a paid government agent acting under instructions, not a mere private citizen; his pose as an ordinary cellmate exploited Henry's confidence; and Henry was already indicted and in custody, when the right to counsel had attached. Although Nichols was told only to listen, the agent "must have known that such propinquity likely would lead to" incriminating disclosures, and the contingent-fee arrangement gave Nichols every incentive to draw Henry out. The government thus "intentionally creat[ed] a situation likely to induce" the statements — an impermissible circumvention of counsel — so the statements should have been excluded. The Court emphasized this was not a case where "the constable . . . blundered," but one where the government "planned an impermissible interference with the right to the assistance of counsel."

## Conclusion
The use of the paid jailhouse informant violated Henry's Sixth Amendment right to counsel; the Fourth Circuit's judgment that the statements should have been excluded was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Cabined by** [[Kuhlmann v. Wilson]] — a jailhouse informant who acts as a mere passive "listening post," taking no action beyond listening to deliberately elicit statements, does not violate the Sixth Amendment. *[[Kuhlmann v. Wilson|Kuhlmann]]* clarifies the line *Henry* draws (deliberate elicitation vs. passive receipt); it does not disturb *Henry*'s holding.
- Part of the [[Massiah v. United States]] / [[Brewer v. Williams]] / [[Maine v. Moulton]] line on the post-attachment Sixth Amendment right to counsel.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Henry*, 447 U.S. 264 (1980) — https://www.courtlistener.com/opinion/110300/united-states-v-henry/ — pinpoints: 270, 274.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f30c7bcb57408bbe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "447 U.S. 264 (1980)", "court": "U.S. Supreme Court", "neutral_cite": "1980 U.S. LEXIS 111", "official_citation_present": true, "parallel_cite": "100 S. Ct. 2183; 65 L. Ed. 2d 115", "title": "United States v. Henry", "year": "1980"}}
{"assertion_id": "3f92860ea49651d7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "By intentionally creating a situation likely to induce the indicted defendant to make incriminating statements, the government (through…", "title": "United States v. Henry"}}
{"assertion_id": "eafae8f97f7310eb", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "United States v. Henry"}}
{"assertion_id": "05c44cd47b33506d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1980-06-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Henry", "field_i_validity": "good_law", "scope_note": "Cabined by Kuhlmann v. Wilson (a passive 'listening post' informant who does not deliberately elicit does not violate the Sixth Amendment); Henry itself remains good law.", "title": "United States v. Henry", "varies_by_point": "false"}}
{"assertion_id": "999c6a1ab1627333", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Henry"}}
```

### lake record — United States v. Henry

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Henry",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Henry",
    "case_name_short": "Henry",
    "case_name_full": "United States v. Henry",
    "input_case_name": "United States v. Henry",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-16",
    "year": 1980,
    "docket": "79-121",
    "cluster_id": 110300,
    "lead_opinion_id": 9427972,
    "sibling_ids": [
      110300,
      9427972,
      9427973,
      9427974,
      9427975
    ],
    "absolute_url": "/opinion/110300/united-states-v-henry/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "447 U.S. 264",
      "volume": "447",
      "reporter": "U.S.",
      "page": "264",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2183",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 115",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "115",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 111",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "447 U.S. 264",
        "volume": "447",
        "reporter": "U.S.",
        "page": "264",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2183",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2183",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 115",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "115",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 111",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "111",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "447 U.S. 264",
    "official_selection": {
      "court_class": "scotus",
      "selected": "447 U.S. 264",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-270",
      "page": null,
      "quote": "incriminating statements from an indicted, incarcerated defendant, in violation of his Sixth Amendment right to counsel under *Massiah*, when it used a paid jailhouse informant posing as a fellow inmate. ## Rule Yes. The Sixth Amendment, as construed in [[Massiah v. United States]], bars the government from",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-274",
      "page": null,
      "quote": "By intentionally creating a situation likely to induce Henry to make incriminating statements without the assistance of counsel, the Government violated Henry's Sixth Amendment right to counsel.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Henry",
    "varies_by_point": false,
    "scope_note": "Cabined by Kuhlmann v. Wilson (a passive 'listening post' informant who does not deliberately elicit does not violate the Sixth Amendment); Henry itself remains good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Bateman",
          "cluster_id": 9413757,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane1_negative"
      },
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
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Taylor",
          "cluster_id": 7306221,
          "cite": [
            "17 F. Supp. 3d 162",
            "2014 WL 1653194",
            "2014 U.S. Dist. LEXIS 57397"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Darnell Hayes",
          "cluster_id": 771010,
          "cite": [
            "231 F.3d 663",
            "2000 Cal. Daily Op. Serv. 8991",
            "2000 Daily Journal DAR 11947",
            "2000 U.S. App. LEXIS 27872",
            "2000 WL 1672631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane1_negative"
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
        "journal_ref": "United States v. Henry:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 7898512,
          "cite": [
            "253 Conn. 1",
            "751 A.2d 298",
            "2000 Conn. LEXIS 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuhlmann v. Wilson",
          "cluster_id": 111726,
          "cite": [
            "91 L. Ed. 2d 364",
            "106 S. Ct. 2616",
            "477 U.S. 436",
            "1986 U.S. LEXIS 65",
            "54 U.S.L.W. 4809"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rushen v. Spain",
          "cluster_id": 111051,
          "cite": [
            "78 L. Ed. 2d 267",
            "104 S. Ct. 453",
            "464 U.S. 114",
            "1983 U.S. LEXIS 11",
            "52 U.S.L.W. 3452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Gonzalez",
          "cluster_id": 2612406,
          "cite": [
            "800 P.2d 1159",
            "51 Cal. 3d 1179",
            "275 Cal. Rptr. 729",
            "90 Daily Journal DAR 13736",
            "90 Cal. Daily Op. Serv. 8746",
            "1990 Cal. LEXIS 5233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Miranda",
          "cluster_id": 1394991,
          "cite": [
            "744 P.2d 1127",
            "44 Cal. 3d 57",
            "241 Cal. Rptr. 594",
            "1987 Cal. LEXIS 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Thomas Franklin v. Jim Fox Martin Murray Robert Morse Bryan Cassandro John Cuneo, Sergeant Eileen Franklin-Lipsker",
          "cluster_id": 780047,
          "cite": [
            "312 F.3d 423",
            "2002 Daily Journal DAR 13381",
            "2002 Cal. Daily Op. Serv. 11479",
            "2002 U.S. App. LEXIS 24254",
            "2002 WL 31663614"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
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
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Teel",
          "cluster_id": 2376013,
          "cite": [
            "793 S.W.2d 236",
            "1990 Tenn. LEXIS 216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyrick v. Fields",
          "cluster_id": 110809,
          "cite": [
            "74 L. Ed. 2d 214",
            "103 S. Ct. 394",
            "459 U.S. 42",
            "1982 U.S. LEXIS 165",
            "51 U.S.L.W. 3411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Beardslee",
          "cluster_id": 1379313,
          "cite": [
            "806 P.2d 1311",
            "53 Cal. 3d 68",
            "279 Cal. Rptr. 276",
            "91 Cal. Daily Op. Serv. 2101",
            "91 Daily Journal DAR 3490",
            "1991 Cal. LEXIS 1157"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conway",
          "cluster_id": 6894227,
          "cite": [
            "108 Ohio St. 3d 214"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Henry:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110300 OR 9427972 OR 9427973 OR 9427974 OR 9427975) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NTcyMjU2MDAwMDAmcz03ODk4NTEyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110300+OR+9427972+OR+9427973+OR+9427974+OR+9427975%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110300 OR 9427972 OR 9427973 OR 9427974 OR 9427975)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDAmcz03NTExMDgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110300+OR+9427972+OR+9427973+OR+9427974+OR+9427975%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110300 OR 9427972 OR 9427973 OR 9427974 OR 9427975)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 1,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110300 OR 9427972 OR 9427973 OR 9427974 OR 9427975)",
    "indexed_citing_opinions": 705,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110300,
        "count": 642,
        "count_source": "search"
      },
      {
        "opinion_id": 9427972,
        "count": 78,
        "count_source": "search"
      },
      {
        "opinion_id": 9427973,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427974,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427975,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1014,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-henry.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMTQyNjcmcz00ODk2MjExJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110300+OR+9427972+OR+9427973+OR+9427974+OR+9427975%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110300,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 107542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 258052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 303848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 349660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 360154,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 362794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110300,
        "cited_id": 3580565,
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
    "date_created": "2026-07-06T00:33:23Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:38:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:33:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Henry

```
<opinion type="majority">
<author id="b307-7">Me. Chief Justice Burgee</author>
<p id="A8i">delivered the opinion of the Court.</p>
<p id="b307-8">We granted certiorari to consider whether respondent’s Sixth Amendment right to the assistance of counsel was violated by the admission at trial of incriminating statements made by respondent to his cellmate, an undisclosed Government informant, after indictment and while in custody. <span class="citation multiple-matches"><a href="/c/U.%20S./444/824/">444 U. S. 824</a></span> (1979).</p>
<p id="b307-9">I</p>
<p id="b307-10">The Janaf Branch of the United Virginia Bank/Seaboard National in Norfolk, Va., was robbed in August 1972. Witnesses saw two men wearing masks and carrying guns enter the bank while a third man waited in the car. No witnesses were able to identify respondent Henry as one of the participants. About an hour after the robbery, the getaway car was discovered. Inside was found a rent receipt signed by one “Allen It. Norris” and a lease, also sighed by Norris, for a house in Norfolk. Two men, who were subsequently convicted of participating in the robbery, were arrested at the rented house. Discovered with them were the proceeds of the robbery and the guns and masks used by the gunmen.</p>
<p id="b307-11">Government agents traced the rent receipt to Henry; on the basis of this information, Henry was arrested in Atlanta, Ga., in November 1972. Two weeks later he was indicted for <page-number citation-index="1" label="266">*266</page-number>armed robbery under <span class="citation no-link">18 U. S. C. §§2113</span> (a) and (d). He was held pending trial in the Norfolk city jail. Counsel was appointed on November 27.</p>
<p id="b308-5">On November 21, 1972, shortly after Henry was incarcerated, Government agents working on the Janaf robbery contacted one Nichols, an inmate at the Norfolk city jail, who for some time prior to this meeting had been engaged to provide confidential information to the Federal Bureau of Investigation as a paid informant. Nichols was then serving a sentence on local forgery charges. The record does not disclose whether the agent contacted Nichols specifically to acquire information about Henry or the Janaf robbery.<footnotemark>1</footnotemark></p>
<p id="b308-6">Nichols informed the agent that he was housed in the same cellbloclc with several federal prisoners awaiting trial, including Henry. The agent told him to be alert to any statements made by the federal prisoners, but not to initiate any conversation with or question Henry regarding the bank robbery. In early December, after Nichols had been released from jail, the agent again contacted Nichols, who reported that he and Henry had engaged in conversation and that Henry had told him about the robbery of the Janaf bank.<footnotemark>2</footnotemark> Nichols was paid for furnishing the information.</p>
<p id="b308-7">When Henry was tried in March 1973, an agent of the <page-number citation-index="1" label="267">*267</page-number>Federal Bureau of Investigation testified concerning the events surrounding the discovery of the rental slip and the evidence uncovered at the rented house. Other witnesses also connected Henry to the rented house, including the rental agent who positively identified Henry as the “Allen R. Norris” who had rented the house and had taken the rental receipt described earlier. A neighbor testified that prior to the robbery she saw Henry at the rented house with John Luck, one of the two men who had by the time of Henry’s trial been convicted for the robbery. In addition, palm prints found on the lease agreement matched those of Henry.</p>
<p id="b309-5">Nichols testified at trial that he had “an opportunity to have some conversations with Mr. Henry while he was in the jail,” and that Henry told him that on several occasions he had gone to the Janaf Branch to see which employees opened the vault. Nichols also testified that Henry described to him the details of the robbery and stated that the only evidence connecting him to the robbery was the rental receipt. The jury was not informed that Nichols was a paid Government informant.</p>
<p id="b309-6">On the basis of this testimony,<footnotemark>3</footnotemark> Henry was convicted of bank robbery and sentenced to a term of imprisonment of 25 years. On appeal, he raised no Sixth Amendment claims. His conviction was affirmed, judgt. order reported at <span class="citation multiple-matches"><a href="/c/F.%202d/483/1401/">483 F. 2d 1401</a></span> (CA4 1973), and his petition to this Court for a writ of cer-tiorari was denied. <span class="citation multiple-matches"><a href="/c/U.%20S./421/915/">421 U. S. 915</a></span> (1975).</p>
<p id="b309-7">On August 28, 1975, Henry moved to vacate his sentence pursuant to <span class="citation no-link">28 U. S. C. § 2255</span><footnotemark>4</footnotemark> At this stage, he stated that <page-number citation-index="1" label="268">*268</page-number>he had just learned that Nichols was a paid Government informant and alleged that he had been intentionally placed in the same cell with Nichols so that Nichols could secure information about the robbery. Thus, Henry contended that the introduction of Nichols’ testimony violated his Sixth Amendment right to the assistance of counsel. The District Court denied the motion without a hearing. The Court of Appeals, however, reversed and remanded for an evidentiary inquiry into “whether the witness [Nichols] was acting as a government agent during his interviews with Henry.”</p>
<p id="b310-5">On remand, the District Court requested affidavits from the Government agents. An affidavit was submitted describing the agent’s relationship with Nichols and relating the following conversation:</p>
<blockquote id="b310-6">“I recall telling Nichols at this time to be alert to any statements made by these individuals [the federal prisoners] regarding the charges against them. I specifically recall telling Nichols that he was not to question Henry or these individuals about the charges against them, however, if they engaged him in conversation or talked in front of him, he was requested to pay attention to their statements. I recall telling Nichols not to initiate any conversations with Henry regarding the bank robbery charges against Henry, but that if Henry initiated the conversations with Nichols, I requested Nichols to pay attention to the information furnished by Henry.”</blockquote>
<p id="b310-7">The agent’s affidavit also stated that he never requested anyone affiliated with the Norfolk city jail to place Nichols in the same cell with Henry.</p>
<p id="b310-8">The District Court again denied Henry’s § 2255 motion, concluding that Nichols’ testimony at trial did not violate Henry’s <page-number citation-index="1" label="269">*269</page-number>Sixth Amendment right to counsel. The Court of Appeals reversed and remanded, holding that the actions of the Government impaired the Sixth Amendment rights of the defendant under <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). The court noted that Nichols had engaged in conversation with Henry and concluded that if by association, by general conversation, or both, Nichols had developed a relationship of trust and confidence with Henry such that Henry revealed incriminating information, this constituted interference with the right to the assistance of counsel under the Sixth Amendment.<footnotemark>5</footnotemark> <span class="citation" data-id="9465406"><a href="/opinion/362794/billy-gale-henry-v-united-states/" aria-description="Citation for case: Billy Gale Henry v. United States">590 F. 2d 544</a></span> (1978).</p>
<p id="b311-5">II</p>
<p id="b311-6">This Court has scrutinized postindictment confrontations between Government agents and the accused to determine whether they are “critical stages” of the prosecution at which the Sixth Amendment right to the assistance of counsel attaches. See, <em>e. g., United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">413 U. S. 300</a></span> (1973); <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967). The present case involves incriminating statements made by the accused to an undisclosed and undercover Government informant while in custody and after indictment. The Government characterizes Henry’s incriminating statements as voluntary and not the result of any affirmative conduct on the part of Government agents to elicit evidence. From this, the Government argues that Henry’s rights were not violated, even assuming the Sixth Amendment applies to such surreptitious confrontations; in short, it is contended that the Government has not interfered with Henry’s right to counsel.<footnotemark>6</footnotemark></p>
<p id="b312-4"><page-number citation-index="1" label="270">*270</page-number>This Court first applied the Sixth Amendment to postindictment communications between the accused and agents of the Government in <em>Massiah </em>v. <em>United States, supra. </em>There, after the accused had been charged, he made incriminating statements to his codefendant, who was acting as an agent of the Government. In reversing the conviction, the Court held that the accused was denied “the basic protections of [the Sixth Amendment] when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicted from him.” <em>Id., </em>at 206. The <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>holding rests squarely on interference with his right to counsel.</p>
<p id="b312-5">The question here is whether under the facts of this case a Government agent “deliberately elicited” incriminating statements from Henry within the meaning of <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>. </em>Three factors are important. First, Nichols was acting under instructions as a paid informant for the Government; second, Nichols was ostensibly no more than a fellow inmate of Henry; and third, Henry was in custody and under indictment at the time he was engaged in conversation by Nichols.</p>
<p id="b312-6">The Court of Appeals viewed the record as showing that Nichols deliberately used his position to secure incriminating information from Henry when counsel was not present and held that conduct attributable to the Government. Nichols had been a paid Government informant for more than a year; moreover, the FBI agent was aware that Nichols had access to Henry and would be able to engage him in conversations without arousing Henry’s suspicion. The arrangement between Nichols and the agent was on a contingent-fee basis; Nichols was to be paid only if he produced useful information.<footnotemark>7</footnotemark> <page-number citation-index="1" label="271">*271</page-number>This combination of circumstances is sufficient to support the Court of Appeals’ determination. Even if the agent’s statement that he did not intend that Nichols would take affirmative steps to secure incriminating information is accepted, he must have known that such propinquity likely would lead' to that result.</p>
<p id="b313-5">The Government argues that the federal agents instructed Nichols not to question Henry about the robbery.<footnotemark>8</footnotemark> Yet according to his own testimony, Nichols was not a passive listener; rather, he had “some conversations with Mr. Henry” while he was in jail and Henry’s incriminatory statements were “the product of this conversation.” While affirmative interrogation, absent waiver, would certainly satisfy <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>we are not persuaded, as the Government contends, that <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977), modified Massiah’s “deliberately elicited” test., See <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980).<footnotemark>9</footnotemark> In <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>no inquiry was <page-number citation-index="1" label="272">*272</page-number>made as to whether Massiah or his codefendant first raised the subject of the crime under investigation.<footnotemark>10</footnotemark></p>
<p id="b314-4">It is quite a different matter when the Government uses undercover agents to obtain incriminating statements from persons not in custody but suspected of criminal activity prior to the time charges are filed. In <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 302</a></span> (1966), for example, this Court held that “no interest legitimately protected by the Fourth Amendment is involved” because “the Fourth Amendment [does not protect] a wrongdoer’s misplaced belief that a person to whom he voluntarily confides his wrongdoing will not reveal it.” See also <em>United States </em>v. <em>White, </em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971). Similarly, the Fifth Amendment has been held not to be implicated by the use of undercover Government agents before charges are filed because of the absence of the potential for compulsion. See <em>Hoffa </em>v. <em>United States, swpra, </em>at 303-304. But the Fourth and Fifth Amendment claims made in those cases are not relevant to the inquiry under the Sixth Amendment here — whether the Government has interfered with the right to counsel of the accused by “deliberately eliciting” incriminating statements. Our holding today does not modify <em><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">White</a></span> </em>or <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span>.</em></p>
<p id="b314-5">It is undisputed that Henry was unaware of Nichols’ role as a Government informant. The Government argues that this Court should apply a less rigorous standard under the <page-number citation-index="1" label="273">*273</page-number>Sixth Amendment where the accused is prompted by an undisclosed undercover informant than where the accused is speaking in the hearing of persons he knows to be Government officers. That line of argument, however, seeks to infuse Fifth Amendment concerns against compelled self-incrimination into the Sixth Amendment protection of the right to the assistance of counsel. An accused speaking to a known Government agent is typically aware that his statements may be used against him. The adversary positions at that stage are well established; the parties are then “arm’s-length” adversaries.</p>
<p id="b315-5">When the accused is in the company of a fellow inmate who is acting by prearrangement as a Government agent, the same cannot be said. Conversation stimulated in such circumstances may elicit information that an accused would not intentionally reveal to persons known to be Government agents. Indeed, the <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>Court noted that if the Sixth Amendment “is to have any efficacy it must apply to indirect and surreptitious interrogations as well as those conducted in the jailhouse.” The Court pointedly observed that Massiah was more seriously imposed upon because he did not know that his codefendant was a Government agent. <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S., at 206</a></span>.</p>
<p id="b315-6">Moreover, the concept of a knowing and voluntary waiver of Sixth Amendment rights does not apply in the context of communications with an undisclosed undercover informant acting for the Government. See <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938). In that setting, Henry, being unaware that Nichols was a Government agent expressly commissioned to secure evidence, cannot be held to have waived his right to. the assistance of counsel.</p>
<p id="b315-7">Finally, Henry’s incarceration at the time he was engaged in conversation by Nichols is also a relevant factor.<footnotemark>11</footnotemark> As a ground <page-number citation-index="1" label="274">*274</page-number>for imposing the prophylactic requirements in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467</a></span> (1966), this Court noted the powerful psychological inducements to reach for aid when a person is in confinement. See also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#448" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 448-454</a></span>. While the concern in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was limited to custodial police interrogation, the mere fact of custody imposes pressures on the accused; confinement may bring into play subtle influences that will make him particularly susceptible to the ploys of undercover Government agents. The Court of Appeals determined that on this record the incriminating conversations between Henry and Nichols were facilitated by Nichols’ conduct and apparent status as a person sharing a common plight. That Nichols had managed to gain the confidence of Henry, as the Court of Appeals determined, is confirmed by Henry’s request that Nichols assist him in his escape plans when Nichols was released from confinement.<footnotemark>12</footnotemark></p>
<p id="b316-5">Under the strictures of the Court’s holdings on the exclusion of evidence, we conclude that the Court of Appeals did not err in holding that Henry’s statements to Nichols should not have been admitted at trial. By intentionally creating a situation likely to induce Henry to make incriminating statements without the assistance of counsel, the Government violated Henry’s Sixth Amendment right to counsel.<footnotemark>13</footnotemark> This is <page-number citation-index="1" label="275">*275</page-number>not a case where, in Justice Cardozo’s words, “the constable . . . blundered,” <em>People </em>v. <em>DeFore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span> (1926); rather, it is one where the “constable” planned an impermissible interference with the right to the assistance of counsel.<footnotemark>14</footnotemark></p>
<p id="b317-5">The judgment of the Court of Appeals for the Fourth Circuit is</p>
<p id="b317-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="pAQr"> The record does disclose that on November 21, 1972, the same day the agent contacted Nichols, the agent’s supervisor interrogated Henry at the jail. After denying participation in the robbery, Henry exercised his right to terminate the interview.</p>
</footnote>
<footnote label="2">
<p id="b308-9"> Henry also asked Nichols if he would help him once Nichols was released. Henry requested Nichols to go to Virginia Beach and contact a woman there. He prepared instructions on how to find the woman and wanted Nichols to tell her to visit Henry in the Norfolk jail. He explained that he wanted to ask the woman to carry a message to his partner, who was incarcerated in the Portsmouth city jail. Henry also gave Nichols a telephone number and asked him to contact an individual named “Junior” or “Nail.” In addition Henry asked Nichols to provide him with a floor plan of the United States Marshals’ office and a handcuff key because Henry intended to attempt an escape.</p>
</footnote>
<footnote label="3">
<p id="b309-8"> Joseph Sadler, another of Henry’s cellmates, also testified at trial. He stated that Henry had told him that Henry had robbed a bank with a man named “Lucky” or “Luck.” Sadler testified that on advice of counsel he informed Government agents of the conversation with Henry. Sadler was not a paid informant and had no arrangement to monitor or report on conversations with Henry.</p>
</footnote>
<footnote label="4">
<p id="b309-9"> In his § 2255 petition, Henry also alleged that Sadler’s testimony was perjurious; that the Government failed to disclose <em>Brady </em>material, see <page-number citation-index="1" label="268">*268</page-number><em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963); that the United. States Attorney’s argument to the jury was impermissibly prejudicial; and that his trial counsel was incompetent. The District Court rejected each of these grounds, and none of these issues is before this Court.</p>
</footnote>
<footnote label="5">
<p id="b311-7"> The Court of Appeals acknowledged that the testimony of Sadler, another cellmate of Henry, supported the conviction but was not willing to conclude beyond a reasonable doubt that Nichols’ testimony did not influence the jury. <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span> (1967).</p>
</footnote>
<footnote label="6">
<p id="b311-8"><em> </em>Although both the Government, and Mr. Justice Rehnquist in dissent, question the continuing vitality of the <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>branch of the Sixth Amendment, we reject their invitation to reconsider it.</p>
</footnote>
<footnote label="7">
<p id="b312-7"> The affidavit of the agent discloses that “Nichols had been paid by the FBI for expenses and services in connection with information he had provided” as an informant for at least a year. The only reasonable inference from this statement is that Nichols was paid when he produced information, not that Nichols was continuously on the payroll of the FBI. Here, the service requested of Nichols was that he obtain incriminating <page-number citation-index="1" label="271">*271</page-number>information from Henry; there is no indication that Nichols would have been paid if he had not performed the requested service.</p>
</footnote>
<footnote label="8">
<p id="b313-8"> Two aspects of the agent’s affidavit are particularly significant. First, it is clear that the agent in his discussions with Nichols singled out Henry as the inmate in whom the agent had a special interest. Thus, the affidavit relates that “I specifically recall telling Nichols that he was not to question <em>Henry </em>or these individuals” and “I recall telling Nichols not to initiate any conversations <em>with Henry </em>regarding the bank robbery charges,” but to “pay attention to the information furnished <em>by Henry.” </em>(Emphasis added.) Second, the agent only instructed Nichols not to question Henry or to initiate conversations regarding the bank robbery charges. Under these instructions, Nichols remained free to discharge his task of eliciting the statements in myriad less direct ways.</p>
</footnote>
<footnote label="9">
<p id="b313-9"> The situation where the “listening post” is an inanimate electronic device differs; such a device has no capability of leading the conversation into any particular subject or prompting any particular replies. See, <em>e. g., United States </em>v. <em>Hearst, </em><span class="citation" data-id="349660"><a href="/opinion/349660/united-states-v-patricia-campbell-hearst/#1347" aria-description="Citation for case: United States v. Patricia Campbell Hearst">563 F. 2d 1331, 1347-1348</a></span> (CA9 1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/1000/">435 U. S. 1000</a></span> (1978). However, that situation is not presented in this case, and there is no occasion to treat it; nor are we called upon to pass on the situation where an informant is placed in close proximity but makes no effort to stimulate conversations about the crime charged.</p>
</footnote>
<footnote label="10">
<p id="b314-6"> No doubt the role of the agent at the time of the conversations between Massiah and his codefendant was more active than that of the federal agents here. Yet the additional fact in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>that the agent was monitoring the conversations is hardly determinative. In both <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>and this case, the informant was charged with the task of obtaining information from an accused. Whether Massiah's codefendant questioned Massiah about the crime or merely engaged in general conversation about it was a matter of no concern to the <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>Court. Moreover, we deem it irrelevant that in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>the agent had to arrange the meeting between Massiah and his codefendant while here the agents were fortunate enough to have an undercover informant already in close proximity to the accused.</p>
</footnote>
<footnote label="11">
<p id="b315-8"> This is not to read a “custody” requirement, which is a prerequisite to the attachment of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, into this branch of the Sixth Amend<page-number citation-index="1" label="274">*274</page-number>ment. Massiah was in no sense in custody at the time of his conversation with his eodefendant. Rather, we believe the fact of custody bears on whether the Government “deliberately elicited” the incriminating statements from Henry.</p>
</footnote>
<footnote label="12">
<p id="b316-7"> This is admittedly not a case such as <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>where the informant and the accused had a prior longstanding relationship. Nevertheless, there is ample evidence in the record which discloses that Nichols had managed to become more than a casual jailhouse acquaintance. That Henry could be induced to discuss his past crime is hardly surprising in view of the fact that Nichols had so ingratiated himself that Henry actively solicited his aid in executing his next crime — his planned attempt to escape from the jail.</p>
</footnote>
<footnote label="13">
<p id="b316-8"> The holding of the Court of Appeals that this was not harmless error is on less firm grounds in view of the strong evidence against Henry, in-<page-number citation-index="1" label="275">*275</page-number>eluding the testimony of a neutral fellow inmate, Henry's rental of the hideaway house, and his presence there with the other participants in the robbery before the crime. The Government, however, has not argued that the error was harmless, and on balance, we are not inclined to disturb the determination of the Court of Appeals.</p>
</footnote>
<footnote label="14">
<p id="b317-12"> Although it does not bear on the constitutional question in this case, we note that Disciplinary Rule 7-104 (A) (1) of the Code of Professional Responsibility provides:</p>
<blockquote id="b317-13">“ (A) During the course of his representation of a client a lawyer shall not:</blockquote>
<blockquote id="A_Y">“(1) Communicate or cause another to communicate on the subject of the representation with a party he knows to be represented by a lawyer in that matter unless he has the prior consent of the lawyer representing such other party or is authorized by law to do so.”</blockquote>
<p id="b317-14">See also Ethical Consideration 7-18.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/United States v. Jackson.md  (`case`, 5 assertions)

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
{"assertion_id": "2f5538159a9d1c7a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "784 F.3d 1227 (2015)", "court": "U.S. Court of Appeals, Eighth Circuit", "neutral_cite": "2015 U.S. App. LEXIS 7397; 2015 WL 2048440", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Jackson", "year": "2015"}}
{"assertion_id": "99cf9fe7917cdcce", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "United States v. Jackson"}}
{"assertion_id": "c0c02c30383bdbe5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Although the warrant application failed to supply probable cause, the deputy acted in objectively reasonable good faith (affidavit…", "title": "United States v. Jackson"}}
{"assertion_id": "5576edbb46fbc228", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-05-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Jackson", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Jackson", "varies_by_point": "false"}}
{"assertion_id": "6738b20e43e3bc2f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Jackson"}}
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

## GROUP: content/cases/United States v. Janis.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Janis"
type: case
citation: "428 U.S. 433 (1976)"
parallel_cite: "96 S. Ct. 3021; 49 L. Ed. 2d 1046"
neutral_cite: 1976 U.S. LEXIS 162
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-10-04
docket: 74-958
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Janis
  varies_by_point: false
  scope_note: "The exclusionary rule does not extend to a federal civil tax proceeding to bar evidence unlawfully seized by state officers; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109539/united-states-v-janis/"
  cluster_id: 109539
  opinion_id: 109539
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Limiting"
related: ["[[United States v. Calandra]]", "[[United States v. Leon]]", "[[Elkins v. United States]]", "[[Pennsylvania Board of Probation and Parole v. Scott]]", "[[Mapp v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "civil-proceeding", "deterrence", "cost-benefit"]
holding: "The exclusionary rule does not bar evidence unlawfully seized by state law-enforcement officers from being used in a federal civil (tax) proceeding, because the marginal deterrence of an intersovereign civil exclusion does not outweigh its substantial social costs."
lake:
  record_id: United States v. Janis
  status: verified
  projected_at: 2026-07-09
---

# United States v. Janis

*428 U.S. 433 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Los Angeles police, executing a search warrant that later proved defective, seized wagering records and cash from Janis; the state gambling case was dismissed after suppression. The IRS then used the seized records to assess a federal wagering excise tax against Janis and levied on the cash. Janis sued for a refund and the Government counterclaimed for the unpaid tax. He argued that the evidence, having been unconstitutionally seized by the state officers, was inadmissible in the federal civil tax proceeding.

## Issue
Whether evidence unconstitutionally seized by state law-enforcement officers (in good-faith reliance on a defective warrant) is inadmissible, under the exclusionary rule, in a federal civil tax proceeding.

## Rule
No; the exclusionary rule extends only where its deterrence benefits outweigh its substantial social costs. "[T]he additional marginal deterrence provided by forbidding a different sovereign from using the evidence in a civil proceeding surely does not outweigh the cost to society of extending the rule to that situation. If, on the other hand, the exclusionary rule does not result in appreciable deterrence, then, clearly, its use in the instant situation is unwarranted." — 428 U.S. at 454. ^pin-454

"In short, we conclude that exclusion from federal civil proceedings of evidence unlawfully seized by a state criminal enforcement officer has not been shown to have a sufficient likelihood of deterring the conduct of the state police so that it outweighs the societal costs imposed by the exclusion. This Court, therefore, is not justified in so extending the exclusionary rule." — [*Id.*](https://www.courtlistener.com/opinion/109539/united-states-v-janis/#:~:text=In%20short%2C%20we%20conclude%20that) ^pin-454b

## Application
The party to be deterred was the state officer, who is already "punished" by exclusion of the evidence in both the state criminal trial and any federal criminal trial — so the entire criminal enforcement process that is his concern is already frustrated. Adding exclusion in a federal civil tax proceeding brought by a different sovereign ("intersovereign") supplied only minimal additional deterrence, which did not outweigh the cost of withholding concededly reliable evidence. The Court therefore declined to extend the rule to this context.

## Conclusion
The unlawfully seized evidence was admissible in the federal civil tax proceeding; the contrary judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Janis* is a foundational cost-benefit limit on the exclusionary rule, applied alongside [[United States v. Calandra]] (grand jury) and later relied on by [[United States v. Leon]] (good faith) and [[Pennsylvania Board of Probation and Parole v. Scott]] (parole hearings). It draws on the deterrence rationale of [[Elkins v. United States]] and [[Mapp v. Ohio]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Limiting*

## Sources
- *United States v. Janis*, 428 U.S. 433 (1976) — https://www.courtlistener.com/opinion/109539/united-states-v-janis/ — pinpoint: 454.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "95c9e475a1449950", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "428 U.S. 433 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 162", "official_citation_present": true, "parallel_cite": "96 S. Ct. 3021; 49 L. Ed. 2d 1046", "title": "United States v. Janis", "year": "1976"}}
{"assertion_id": "7f1db31276ea2236", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Limiting", "title": "United States v. Janis"}}
{"assertion_id": "d69d0d7ae9430dbe", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The exclusionary rule does not bar evidence unlawfully seized by state law-enforcement officers from being used in a federal civil (tax) proceeding, because the marginal deterrence of an intersovereign civil exclusion does not outweigh its substantial social costs.", "title": "United States v. Janis"}}
{"assertion_id": "2f216c202823fa30", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Janis", "field_i_validity": "good_law", "scope_note": "The exclusionary rule does not extend to a federal civil tax proceeding to bar evidence unlawfully seized by state officers; good law.", "title": "United States v. Janis", "varies_by_point": "false"}}
{"assertion_id": "5bb7934e9d192b6f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Janis"}}
```

### lake record — United States v. Janis

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Janis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Janis",
    "case_name_short": "Janis",
    "case_name_full": "UNITED STATES Et Al. v. JANIS",
    "input_case_name": "United States v. Janis",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-10-04",
    "year": 1976,
    "docket": "74-958",
    "cluster_id": 109539,
    "lead_opinion_id": 109539,
    "sibling_ids": [
      109539,
      9426584,
      9426585,
      9426586
    ],
    "absolute_url": "/opinion/109539/united-states-v-janis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 433",
      "volume": "428",
      "reporter": "U.S.",
      "page": "433",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3021",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3021",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1046",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1046",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 162",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "162",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 433",
        "volume": "428",
        "reporter": "U.S.",
        "page": "433",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3021",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3021",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1046",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1046",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 162",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "162",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 433",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 433",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-454",
      "page": null,
      "quote": "--- # United States v. Janis *428 U.S. 433 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Los Angeles police, executing a search warrant that later proved defective, seized wagering records and cash from Janis; the state gambling case was dismissed after suppression. The IRS then used the seized records to assess a federal wagering excise tax against Janis and levied on the cash. Janis sued for a refund and the Government counterclaimed for the unpaid tax. He argued that the evidence, having been unconstitutionally seized by the state officers, was inadmissible in the federal civil tax proceeding. ## Issue Whether evidence unconstitutionally seized by state law-enforcement officers (in good-faith reliance on a defective warrant) is inadmissible, under the exclusionary rule, in a federal civil tax proceeding. ## Rule No; the exclusionary rule extends only where its deterrence benefits outweigh its substantial social costs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-454b",
      "page": null,
      "quote": "In short, we conclude that exclusion from federal civil proceedings of evidence unlawfully seized by a state criminal enforcement officer has not been shown to have a sufficient likelihood of deterring the conduct of the state police so that it outweighs the societal costs imposed by the exclusion. This Court, therefore, is not justified in so extending the exclusionary rule.",
      "star_marker": "454",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 29995,
      "fragment": "#:~:text=In%20short%2C%20we%20conclude%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Janis",
    "varies_by_point": false,
    "scope_note": "The exclusionary rule does not extend to a federal civil tax proceeding to bar evidence unlawfully seized by state officers; good law.",
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
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Alexandria v. Kendall Dixon",
          "cluster_id": 3200119,
          "cite": [
            "196 So. 3d 592",
            "41 I.E.R. Cas. (BNA) 619",
            "2016 WL 2337943",
            "2016 La. LEXIS 1057"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Principal Life Insurance Company and Subsidiaries v. United States",
          "cluster_id": 2776459,
          "cite": [
            "120 Fed. Cl. 41",
            "115 A.F.T.R.2d (RIA) 726",
            "2015 U.S. Claims LEXIS 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re Noronha",
          "cluster_id": 1808476,
          "cite": [
            "382 B.R. 363",
            "2007 Bankr. LEXIS 4425",
            "101 A.F.T.R.2d (RIA) 515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Osama Awadallah",
          "cluster_id": 784129,
          "cite": [
            "349 F.3d 42",
            "2 A.L.R. Fed. 2d 705",
            "2003 U.S. App. LEXIS 22879",
            "2003 WL 22519622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane1_negative"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jacobsen",
          "cluster_id": 111143,
          "cite": [
            "80 L. Ed. 2d 85",
            "104 S. Ct. 1652",
            "466 U.S. 109",
            "1984 U.S. LEXIS 53",
            "52 U.S.L.W. 4414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. Michigan",
          "cluster_id": 145646,
          "cite": [
            "165 L. Ed. 2d 56",
            "126 S. Ct. 2159",
            "547 U.S. 586",
            "2006 U.S. LEXIS 4677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Lopez-Mendoza",
          "cluster_id": 111265,
          "cite": [
            "82 L. Ed. 2d 778",
            "104 S. Ct. 3479",
            "468 U.S. 1032",
            "1984 U.S. LEXIS 156",
            "52 U.S.L.W. 5190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
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
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Petzoldt v. Commissioner",
          "cluster_id": 4706920,
          "cite": [
            "92 T.C. 661",
            "1989 U.S. Tax Ct. LEXIS 42",
            "92 T.C. No. 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ceccolini",
          "cluster_id": 109816,
          "cite": [
            "55 L. Ed. 2d 268",
            "98 S. Ct. 1054",
            "435 U.S. 268",
            "1978 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McGhee",
          "cluster_id": 1872247,
          "cite": [
            "709 N.W.2d 595",
            "268 Mich. App. 600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny Weimerskirch v. Commissioner of Internal Revenue",
          "cluster_id": 365515,
          "cite": [
            "596 F.2d 358",
            "44 A.F.T.R.2d (RIA) 5072",
            "1979 U.S. App. LEXIS 15008"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Janis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109539 OR 9426584 OR 9426585 OR 9426586) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDI2MzQ1NjAwMDAwJnM9MTY1ODc5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109539+OR+9426584+OR+9426585+OR+9426586%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(109539 OR 9426584 OR 9426585 OR 9426586)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTQmcz0xMzA1ODQ5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109539+OR+9426584+OR+9426585+OR+9426586%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109539 OR 9426584 OR 9426585 OR 9426586)",
        "reviewed": 20,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 20,
        "triage_read": 0,
        "triage_snippet_classified": 20
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109539 OR 9426584 OR 9426585 OR 9426586)",
    "indexed_citing_opinions": 841,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109539,
        "count": 767,
        "count_source": "search"
      },
      {
        "opinion_id": 9426584,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9426585,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426586,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1453,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-janis.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxODkxODgmcz05Mzg1NjA4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109539+OR+9426584+OR+9426585+OR+9426586%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109539,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 101556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 101820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 102139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 102360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 102455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 106413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109340,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 109396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 264948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 273172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 275789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 276982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 279381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 280893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 283983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 284130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 290318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 290347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 293542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 296208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 296729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 312624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1380502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1550076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1574898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1575214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 1675172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 2262725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109539,
        "cited_id": 4482082,
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
    "date_created": "2026-07-06T00:47:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:47:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:47:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:50:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:47:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Janis

```
<div>
<center><b><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U.S. 433</a></span> (1976)</b></center>
<center><h1>UNITED STATES ET AL.<br>
v.<br>
JANIS.</h1></center>
<center>No. 74-958.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 8, 1975.</center>
<center>Decided July 6, 1976.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*434</span> <i>Solicitor General Bork</i> argued the cause for petitioners. With him on the brief were <i>Assistant Attorney General Crampton, Stuart A. Smith, Robert E. Lindsay,</i> and <i>Carleton D. Powell.</i></p>
<p><i>Herbert D. Sturman</i> argued the cause for respondent. With him on the brief was <i>Richard G. Sherman.</i></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents an issue of the appropriateness of an extension of the judicially created exclusionary rule: Is evidence seized by a state criminal law enforcement officer in good faith, but nonetheless unconstitutionally, inadmissible in a civil proceeding by or against the United States?</p>
<p></p>
<h2>I</h2>
<p>In November 1968 the Los Angeles police obtained a warrant directing a search for bookmaking paraphernalia at two specified apartment locations in the city and, as well, on the respective persons of Morris Aaron Levine and respondent Max Janis. The warrant was issued by <span class="star-pagination">*435</span> a judge of the Municipal Court of the Los Angeles Judicial District. It was based upon the affidavit of Officer Leonard Weissman.<sup>[1]</sup> After the search, made pursuant <span class="star-pagination">*436</span> to the warrant, both the respondent and Levine were arrested and the police seized from respondent property consisting of $4,940 in cash and certain wagering records.<sup>[2]</sup></p>
<p>Soon thereafter, Officer Weissman telephoned an agent of the United States Internal Revenue Service and informed the agent that Janis had been arrested for bookmaking activity.<sup>[3]</sup> With the assistance of Weissman, who was familiar with bookmakers' codes, the revenue agent analyzed the wagering records that had been seized and determined from them the gross volume of respondent's gambling activity for the five days immediately preceding the seizure. Weissman informed the agent that he had conducted a surveillance of respondent's activities that indicated that respondent had been engaged in bookmaking <span class="star-pagination">*437</span> during the 77-day period from September 14 through November 30, 1968, the day of the arrest.</p>
<p>Respondent had not filed any federal wagering tax return pertaining to bookmaking activities for that 77-day period. Based exclusively upon its examination of the evidence so obtained by the Los Angeles police, the Internal Revenue Service made an assessment jointly against respondent and Levine for wagering taxes, under § 4401 of the Internal Revenue Code of 1954, <span class="citation no-link">26 U. S. C. § 4401</span>, in the amount of $89,026.09, plus interest. The amount of the assessment was computed by first determining respondent's average daily gross proceeds for the five-day period covered by the seized material and analyzed by the agent, and then multiplying the resulting figure by 77, the period of the police surveillance of respondent's activities.<sup>[4]</sup> The assessment having been made, the Internal Revenue Service exercised its statutory authority, under <span class="citation no-link">26 U. S. C. § 6331</span>, to levy upon the $4,940 in cash in partial satisfaction of the assessment against respondent.</p>
<p>Charges were filed in due course against respondent and Levine in Los Angeles Municipal Court for violation of the local gambling laws. They moved to quash the search warrant. A suppression hearing was held by the same judge who had issued the warrant. The defendants pressed upon the court the case of <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), which had been decided just three weeks earlier and <i>after</i> the search warrant had been issued. They urged that the Weissman affidavit did not set forth, in sufficient detail, the underlying circumstances to enable the issuing magistrate to determine independently <span class="star-pagination">*438</span> the reliability of the information supplied by the informants. The judge granted the motion to quash the warrant. He then ordered that all items seized pursuant to it be returned except the cash that had been levied upon by the Internal Revenue Service. App. 78-80.</p>
<p>In June 1969 respondent filed a claim for refund of the $4,940. The claim was not honored, and 18 months later, in December 1970, respondent filed suit for that amount in the United States District Court for the Central District of California. The Government answered and counterclaimed for the substantial unpaid balance of the assessment.<sup>[5]</sup> In pretrial proceedings, it was agreed that the "sole basis of the computation of the civil tax assessment . . . was . . . the items obtained pursuant to the search warrant . . . and the information furnished to [the revenue agent] by Officer Weissman with respect to the duration of [respondent's] alleged wagering activities."<sup>[6]</sup><i>Id.,</i> at 18. Respondent then moved to suppress the evidence seized, and all copies thereof in the possession of the Service, and to quash the assessment. <i>Id.,</i> at 23-24.</p>
<p>At the outset of the hearing on the motion, the District Court observed that it was "reluctantly holding that <span class="star-pagination">*439</span> the affidavit supporting the search warrant is insufficient under the <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> and <i>Aguilar</i> [v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964)] doctrines." <i>Id.,</i> at 47. It then concluded that "[a]ll of the evidence utilized as the basis" of the assessment "was obtained directly or indirectly as a result of the search pursuant to the defective search warrant," and that, consequently, the assessment "was based in substantial part, if not completely, on illegally procured evidence. . . in violation of [respondent's] Fourth Amendment rights to be free from unreasonable searches and seizures." <span class="citation no-link">73-1 USTC ¶ 16,083</span>, p. 81,392 (1973). The court concluded that Janis was entitled to a refund of the $4,940, together with interest thereon, "for the reason that substantially all, if not all, of the evidence utilized by the defendants herein in making their assessment . . . was illegally obtained, and, as such, the assessment was invalid." <i><span class="citation no-link">Ibid.</span></i> Further, where, as here, "illegally obtained evidence constitutes the basis of a federal tax assessment," the respondent was "not required to prove the extent of the refund to which he claims he is entitled." <span class="citation no-link"><i>Id.,</i> at 81,393</span>. Instead, it was sufficient if he prove "that substantially all, if not all, of the evidence upon which the assessment was based was the result of illegally obtained evidence." Accordingly, the court ordered that the civil tax assessment made by the Internal Revenue Service "against all the property and assets of . . . Janis be quashed," and entered judgment for the respondent. <i><span class="citation no-link">Ibid.</span></i> The Government's counterclaim was dismissed with prejudice. The United States Court of Appeals for the Ninth Circuit, by unpublished memorandum without opinion, affirmed on the basis of the District Court's findings of fact and conclusions of law. Pet. for Cert. 12A.</p>
<p>Because of the obvious importance of the question, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./421/1010/">421 U. S. 1010</a></span> (1975).</p>
<p></p>
<h2>
<span class="star-pagination">*440</span> II</h2>
<p>Some initial observations about the procedural posture of the case in the District Court are indicated. If there is to be no limit to the burden of proof the respondent, as "taxpayer," must carry, then, even though he were to obtain a favorable decision on the inadmissibility-of-evidence issue, the respondent on this record could not possibly defeat the Government's counterclaim. The Government notes, properly we think, that the litigation is composed of two separate elements: the refund suit instituted by the respondent, and the collection suit instituted by the United States through its counterclaim. In a refund suit the taxpayer bears the burden of proving the amount he is entitled to recover. <i>Lewis</i> v. <i>Reynolds,</i> <span class="citation" data-id="101820"><a href="/opinion/101820/lewis-v-reynolds/" aria-description="Citation for case: Lewis v. Reynolds">284 U. S. 281</a></span> (1932). It is not enough for him to demonstrate that the assessment of the tax for which refund is sought was erroneous in some respects.</p>
<p>This Court has not spoken with respect to the burden of proof in a tax collection suit. The Government argues here that the presumption of correctness that attaches to the assessment in a refund suit must also apply in a civil collection suit instituted by the United States under the authority granted by §§ 7401 and 7403 of the Code, <span class="citation no-link">26 U. S. C. §§ 7401</span> and 7403. Thus, it is said, the defendant in a collection suit has the same burden of proving that he paid the correct amount of his tax liability.</p>
<p>The policy behind the presumption of correctness and the burden of proof, see <i>Bull</i> v. <i>United States,</i> <span class="citation" data-id="102455"><a href="/opinion/102455/bull-v-united-states/#259" aria-description="Citation for case: Bull v. United States">295 U. S. 247, 259-260</a></span> (1935), would appear to be applicable in each situation. It accords, furthermore, with the burden-of-proof rule which prevails in the usual preassessment proceeding in the United States Tax Court. <i>Lucas</i> v. <i>Structural Steel Co.,</i> <span class="citation" data-id="101556"><a href="/opinion/101556/lucas-v-kansas-city-structural-steel-co/#271" aria-description="Citation for case: Lucas v. Kansas City Structural Steel Co.">281 U. S. 264, 271</a></span> (1930); <i>Welch</i> v. <i>Helvering,</i> <span class="citation" data-id="102139"><a href="/opinion/102139/welch-v-helvering/#115" aria-description="Citation for case: Welch v. Helvering">290 U. S. 111, 115</a></span> (1933); Rule 142 (a) <span class="star-pagination">*441</span> of the Rules of Practice and Procedure of the United States Tax Court (1973). In any event, for purposes of this case, we assume that this is so and that the burden of proof may be said technically to rest with respondent Janis.</p>
<p>Respondent, however, submitted no evidence tending either to demonstrate that the assessment was incorrect or to show the correct amount of wagering tax liability, if any, on his part. In the usual situation one might well argue, as the Government does, that the District Court then could not properly grant judgment for the respondent on either aspect of the suit. But the present case may well not be the usual situation. What we have is a "naked" assessment without <i>any</i> foundation whatsoever if what was seized by the Los Angeles police cannot be used in the formulation of the assessment.<sup>[7]</sup> The determination of tax due then may be one "without rational foundation and excessive," and not properly subject to the usual rule with respect to the burden of proof in tax cases. <i>Helvering</i> v. <i>Taylor,</i> <span class="citation" data-id="9418831"><a href="/opinion/102360/helvering-v-taylor/#514" aria-description="Citation for case: Helvering v. Taylor">293 U. S. 507, 514-515</a></span> (1935).<sup>[8]</sup> See 9 J. Mertens, Law of Federal Income Taxation § 50.65 (1971).</p>
<p>There appears, indeed, to be some debate among the <span class="star-pagination">*442</span> Federal Courts of Appeals, in different factual contexts, as to the effect upon the burden of proof in a tax case when there is positive evidence that an assessment is incorrect. Some courts indicate that the burden of showing the amount of the deficiency then shifts to the Commissioner.<sup>[9]</sup> Others hold that the burden of showing the correct amount of the tax remains with the taxpayer.<sup>[10]</sup> However that may be, the debate does not extend to the situation where the assessment is shown to be naked and without <i>any</i> foundation. The courts then appear to apply the rule of the <i><span class="citation" data-id="9418831"><a href="/opinion/102360/helvering-v-taylor/" aria-description="Citation for case: Helvering v. Taylor">Taylor</a></span></i> case. See <i>United States</i> v. <i>Rexach,</i> <span class="citation" data-id="312624"><a href="/opinion/312624/united-states-v-felix-benitez-rexach/#16" aria-description="Citation for case: United States v. Felix Benitez Rexach">482 F. 2d 10, 16-17, n. 3</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1039/">414 U. S. 1039</a></span> (1973); <i>Pizzarello</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/408/579/">408 F. 2d 579</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/986/">396 U. S. 986</a></span> (1969); <i>Suarez</i> v. <i>Commisioner,</i> <span class="citation" data-id="4482081"><a href="/opinion/4703384/suarez-v-commissioner/#814" aria-description="Citation for case: Suarez v. Commissioner">58 T. C. 792, 814-815</a></span> (1972). But cf. <i>Compton</i> v. <i>United States,</i> <span class="citation" data-id="264948"><a href="/opinion/264948/nannie-v-compton-v-united-states-of-america/#216" aria-description="Citation for case: Nannie v. Compton v. United States of America">334 F. 2d 212, 216</a></span> (CA4 1964).</p>
<p>Certainly, proof that an assessment is utterly without foundation is proof that it is arbitrary and erroneous. For purposes of this case, we need not go so far as to accept the Government's argument that the exclusion of the evidence in issue here is insufficient to require judgment for the respondent or even to shift the burden to the Government. We are willing to assume that if the District Court was correct in ruling that the evidence seized by the Los Angeles police may not be used in formulating the assessment (on which both the levy and the counterclaim were based), then the District Court was also correct in granting judgment for Janis in both <span class="star-pagination">*443</span> aspects of the present suit. This assumption takes us, then, to the primary issue.<sup>[11]</sup></p>
<p></p>
<h2>III</h2>
<p>This Court early pronounced a rule that the Fifth Amendment's command that no person "shall be compelled in any criminal case to be a witness against himself" renders evidence falling within the Amendment's prohibition inadmissible. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886). It was not until 1914, however, that the Court held that the Fourth Amendment alone may be the basis for excluding from a federal criminal trial evidence seized by a federal officer in violation solely of that Amendment. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. This comparatively late judicial creation of a Fourth Amendment exclusionary rule is not particularly surprising. In contrast to the Fifth Amendment's direct command against the admission of compelled testimony, the issue of admissibility of evidence obtained in violation of the Fourth Amendment is determined after, and apart from, the violation.<sup>[12]</sup> In <span class="star-pagination">*444</span> <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> it was held, however, that the Fourth Amendment did not apply to state officers, and, therefore, that material seized unconstitutionally by a state officer could be admitted in a federal criminal proceeding. This was the "silver platter" doctrine.<sup>[13]</sup></p>
<p>In <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), the Court determined that the Due Process Clause of the Fourteenth Amendment reflected the Fourth Amendment to the extent of providing those protections against intrusions that are " `implicit in the concept of ordered liberty.' " <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado"><i>Id.,</i> at 27</a></span>. Nonetheless, the Court, in not applying the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> doctrine in a state trial to the product of a state search, held:</p>
<blockquote>"Granting that in practice the exclusion of evidence may be an effective way of deterring unreasonable searches, it is not for this Court to condemn as falling below the minimal standards assured by the Due Process Clause a State's reliance upon other methods which, if consistently enforced, would be equally effective." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#31" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 31</a></span>.</blockquote>
<p>Not long thereafter, the Court ruled that means used by a State to procure evidence could be sufficiently offensive to the concept of ordered liberty as to make admission of the evidence so procured a violation of the Due Process Clause, <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), but that such a violation would exist only in the most extreme case, <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span> (1954).</p>
<p><span class="star-pagination">*445</span> Thus, as matters then stood, the Fourth Amendment was applicable to the States, but a State could allow an official to engage in a violation thereof with no judicial sanction except in the most extreme case. In addition, federal authorities, if they happened upon a State so inclined, could profit from the State's action by receiving on a silver platter evidence unconstitutionally obtained. The federal authorities, profiting thereby, had no judicially created reason to discourage unconstitutional searches by a State, and the States, having no judicially mandated controls, were free to engage in such searches.<sup>[14]</sup></p>
<p><i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, was decided in 1960. Invoking its "supervisory power over the administration of criminal justice in the federal courts," <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#216" aria-description="Citation for case: Elkins v. United States"><i>id.,</i> at 216</a></span>, the Court held that</p>
<blockquote>"evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#223" aria-description="Citation for case: Elkins v. United States"><i>Id.,</i> at 223</a></span>.</blockquote>
<p>The rule thus announced apparently served two purposes. First, it assured that a State, which could admit the evidence in its own proceedings if it so chose, <span class="star-pagination">*446</span> nevertheless would suffer some deterrence in that its federal counterparts would be unable to use the evidence in federal criminal proceedings. Second, the rule discouraged federal authorities from using a state official to circumvent the restrictions of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>.</i></p>
<p>Only one year later, however, the exclusionary rule was made applicable to state criminal trials. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). The Court ruled:</p>
<blockquote>"Since the Fourth Amendment's right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth, it is enforceable against them by the same sanction of exclusion as is used against the Federal Government." <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio"><i>Id.,</i> at 655</a></span>.</blockquote>
<p>The debate within the Court on the exclusionary rule has always been a warm one.<sup>[15]</sup> It has been unaided, unhappily, by any convincing empirical evidence on the effects of the rule. The Court, however, has established that the "prime purpose" of the rule, if not the sole one, "is to deter future unlawful police conduct." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974). See <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975). Thus,</p>
<blockquote>"[i]n sum, the rule is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect, rather than a personal constitutional right of the party aggrieved." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>.</blockquote>
<p><span class="star-pagination">*447</span> And</p>
<blockquote>"[a]s with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served." <i><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Ibid.</a></span></i><sup>[16]</sup></blockquote>
<p>In the complex and turbulent history of the rule, the Court never has applied it to exclude evidence from a civil proceeding, federal or state.<sup>[17]</sup></p>
<p></p>
<h2>IV</h2>
<p>In the present case we are asked to create judicially a deterrent sanction by holding that evidence obtained by a state criminal law enforcement officer in good-faith reliance on a warrant that later proved to be defective shall be inadmissible in a federal civil tax proceeding. Clearly, the enforcement of admittedly valid laws would be hampered by so extending the exclusionary rule, and, as is nearly always the case with the rule, concededly relevant and reliable evidence would be rendered unavailable.<sup>[18]</sup></p>
<p><span class="star-pagination">*448</span> In evaluating the need for a deterrent sanction, one must first identify those who are to be deterred. In this case it is the state officer who is the primary object of the sanction. It is his conduct that is to be controlled. Two factors suggest that a sanction in addition to those that presently exist is unnecessary. First, the local law enforcement official is already "punished" by the exclusion of the evidence in the state criminal trial.<sup>[19]</sup> That, necessarily, is of substantial concern to him. Second, the evidence is also excludable in the federal criminal trial, <i>Elkins</i> v. <i>United States, supra</i><i>,</i> so that the entire criminal enforcement process, which is the concern and duty of these officers, is frustrated.<sup>[20]</sup></p>
<p>Jurists and scholars uniformly have recognized that the exclusionary rule imposes a substantial cost on the societal interest in law enforcement by its proscription <span class="star-pagination">*449</span> of what concededly is relevant evidence. See, <i>e. g., </i><i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (BURGER, C. J., dissenting); Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 429 (1974). And alternatives that would be less costly to societal interests have been the subject of extensive discussion and exploration.<sup>[21]</sup></p>
<p>Equally important, although scholars have attempted to determine whether the exclusionary rule in fact does have any deterrent effect, each empirical study on the <span class="star-pagination">*450</span> subject, in its own way, appears to be flawed.<sup>[22]</sup> It would not be appropriate to fault those who have attempted empirical studies for their lack of convincing data. The <span class="star-pagination">*451</span> number of variables is substantial,<sup>[23]</sup> and many cannot be measured or subjected to effective controls. Record-keeping before <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> was spotty at best, a fact which <span class="star-pagination">*452</span> thus severely hampers before-and-after studies. Since <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>,</i> of course, all possibility of broad-scale controlled or even semi-controlled comparison studies has been eliminated.<sup>[24]</sup> "Response" studies are hampered by the <span class="star-pagination">*453</span> presence of the respondents' interests.<sup>[25]</sup> And extrapolation studies are rendered highly inconclusive by the changes in legal doctrines and police-citizen relationships that have taken place in the 15 years since <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> was decided.<sup>[26]</sup></p>
<p>We find ourselves, therefore, in no better position than the Court was in 1960 when it said:</p>
<blockquote>"Empirical statistics are not available to show that the inhabitants of states which follow the exclusionary rule suffer less from lawless searches and seizures than do those of states which admit evidence unlawfully obtained. Since as a practical matter it is never easy to prove a negative, it is hardly likely that conclusive factual data could ever be assembled. For much the same reason, it cannot positively be demonstrated that enforcement of the criminal law is either more or less effective under either rule." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S., at 218</a></span>.</blockquote>
<p>If the exclusionary rule is the "strong medicine" that its proponents claim it to be, then its use in the situations in which it is now applied (resulting, for example, in this case in frustration of the Los Angeles police officers' good-faith duties as enforcers of the criminal laws) must be assumed to be a substantial and efficient deterrent. Assuming this efficacy, the additional marginal deterrence provided by forbidding a different sovereign from using the evidence in a civil proceeding surely does not outweigh <span class="star-pagination">*454</span> the cost to society of extending the rule to that situation.<sup>[27]</sup> If, on the other hand, the exclusionary rule does not result in appreciable deterrence, then, clearly, its use in the instant situation is unwarranted. Under either assumption, therefore, the extension of the rule is unjustified.<sup>[28]</sup></p>
<p>In short, we conclude that exclusion from federal civil proceedings of evidence unlawfully seized by a state criminal enforcement officer has not been shown to have a sufficient likelihood of deterring the conduct of the state police so that it outweighs the societal costs imposed by the exclusion. This Court, therefore, is not justified in so extending the exclusionary rule.<sup>[29]</sup></p>
<p><span class="star-pagination">*455</span> Respondent argues, however, that the application of the exclusionary rule to civil proceedings long has been recognized in the federal courts. He cites a number of cases.<sup>[30]</sup> But respondent does not critically distinguish between those cases in which the officer committing the unconstitutional search or seizure was an agent of the sovereign that sought to use the evidence, on the one hand, and those cases, such as the present one, on the other hand, where the officer has no responsibility or duty to, or agreement with, the sovereign seeking to use the evidence.<sup>[31]</sup></p>
<p><span class="star-pagination">*456</span> The seminal cases that apply the exclusionary rule to a civil proceeding involve "intrasovereign" violations,<sup>[32]</sup> a situation we need not consider here. In some cases the courts have refused to create an exclusionary rule for either intersovereign or intrasovereign violations in proceedings other than strictly criminal prosecutions. See <i>United States ex rel. Sperling</i> v. <i>Fitzpatrick,</i> <span class="citation" data-id="9455670"><a href="/opinion/290347/united-states-of-america-ex-rel-herbert-sperling-relator-appellant-v/" aria-description="Citation for case: United States of America Ex Rel. Herbert Sperling,...">426 F. 2d 1161</a></span> (CA2 1970) (intrasovereign/parole revocation); <i>United States</i> v. <i>Schipani,</i> <span class="citation" data-id="293542"><a href="/opinion/293542/united-states-v-joseph-f-schipani/" aria-description="Citation for case: United States v. Joseph F. Schipani">435 F. 2d 26</a></span> (CA2 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/983/">401 U. S. 983</a></span> (1971) (intersovereign/sentencing).<sup>[33]</sup> And in <i>Compton</i> v. <i>United States,</i> <span class="citation" data-id="264948"><a href="/opinion/264948/nannie-v-compton-v-united-states-of-america/#215" aria-description="Citation for case: Nannie v. Compton v. United States of America">334 F. 2d 212, 215-216</a></span> (1964), a case remarkably like this one, the Fourth Circuit held that the presumption of correctness given a tax assessment was not affected by the fact that the assessment was based upon evidence unconstitutionally seized by state criminal law enforcement officers. Only one case cited by the respondent squarely holds that there must be an exclusionary rule barring use in a civil proceeding by one sovereign of material seized in violation of the Fourth Amendment by an officer of another sovereign.<sup>[34]</sup> In <i>Suarez</i> v. <i>Commissioner,</i> 58 T. C. 792 <span class="star-pagination">*457</span> (1972) (reviewed by the court, with two judges dissenting), the Tax Court determined that the exclusionary rule should be applied in a situation similar to the one that confronts us here. The court concluded that</p>
<blockquote>"any competing consideration based upon the need for effective enforcement of civil tax liabilities (compare <i>Elkins</i> v. <i>United States</i> . . .) must give way to the higher goal of protection of the individual and the necessity for preserving confidence in, rather than encouraging contempt for, the processes of Government." <span class="citation" data-id="4482081"><a href="/opinion/4703384/suarez-v-commissioner/#805" aria-description="Citation for case: Suarez v. Commissioner"><i>Id.,</i> at 805</a></span>.</blockquote>
<p>No appeal was taken.</p>
<p>We disagree with the broad implications of this statement of the Tax Court for two reasons. To the extent that the court did not focus on the deterrent purpose of the exclusionary rule, the law has since been clarified. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974); <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">422 U. S. 531</a></span> (1975). Moreover, the court did not distinguish between intersovereign and intrasovereign uses of unconstitutionally seized material. Working, as we must, with the absence of convincing empirical data, common sense dictates that <span class="star-pagination">*458</span> the deterrent effect of the exclusion of relevant evidence is highly attenuated when the "punishment" imposed upon the offending criminal enforcement officer is the removal of that evidence from a civil suit by or against a different sovereign. In <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span></i> the Court indicated that the assumed interest of criminal law enforcement officers in the criminal proceedings of another sovereign counterbalanced this attenuation sufficiently to justify an exclusionary rule. Here, however, the attenuation is further augmented by the fact that the proceeding is one to enforce only the civil law of the other sovereign.</p>
<p>This attenuation, coupled with the existing deterrence effected by the denial of use of the evidence by either sovereign in the criminal trials with which the searching officer is concerned, creates a situation in which the imposition of the exclusionary rule sought in this case is unlikely to provide significant, much less substantial, additional deterrence. It falls outside the offending officer's zone of primary interest. The extension of the exclusionary rule, in our view, would be an unjustifiably drastic action by the courts in the pursuit of what is an undesired and undesirable supervisory role over police officers.<sup>[35]</sup> See <i>Rizzo</i> v. <i>Goode,</i> <span class="citation" data-id="9426245"><a href="/opinion/109349/rizzo-v-goode/" aria-description="Citation for case: Rizzo v. Goode">423 U. S. 362</a></span> (1976).</p>
<p><span class="star-pagination">*459</span> In the past this Court has opted for exclusion in the anticipation that law enforcement officers would be deterred from violating Fourth Amendment rights. Then, as now, the Court acted in the absence of convincing empirical evidence and relied, instead, on its own assumptions of human nature and the interrelationship of the various components of the law enforcement system. In the situation before us, we do not find sufficient justification for the drastic measure of an exclusionary rule. There comes a point at which courts, consistent with their duty to administer the law, cannot continue to create barriers to law enforcement in the pursuit of a supervisory role that is properly the duty of the Executive and Legislative Branches. We find ourselves at that point in this case. We therefore hold that the judicially <span class="star-pagination">*460</span> created exclusionary rule should not be extended to forbid the use in the civil proceeding of one sovereign of evidence seized by a criminal law enforcement agent of another sovereign.</p>
<p>The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE STEVENS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE MARSHALL concurs, dissenting.</p>
<p>I adhere to my view that the exclusionary rule is a necessary and inherent constitutional ingredient of the protections of the Fourth Amendment. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#355" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 355-367</a></span> (1974) (BRENNAN, J., dissenting), and <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#550" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 550-562</a></span> (1975) (BRENNAN, J., dissenting). Repetition or elaboration of the reasons supporting that view in this case would serve no useful purpose. My view of the exclusionary rule would, of course, require an affirmance of the Court of Appeals. Today's decisions in this case and in <i>Stone</i> v. <i>Powell, post,</i> p. 465, continue the Court's "business of slow strangulation of the rule," <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#561" aria-description="Citation for case: United States v. Peltier">422 U. S., at 561</a></span>. But even accepting the proposition that deterrence of police misconduct is the only purpose served by the exclusionary rule, as my Brother STEWART apparently does, his dissent persuasively demonstrates the error of today's result. I dissent.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>The Court today holds that evidence unconstitutionally seized from the respondent by state officials may be introduced against him in a proceeding to adjudicate his <span class="star-pagination">*461</span> liability under the wagering excise tax provisions of the Internal Revenue Code of 1954. This result, in my view, cannot be squared with <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>. In that case the Court discarded the "silver platter doctrine" and held that evidence illegally seized by state officers cannot lawfully be introduced against a defendant in a federal criminal trial.</p>
<p>Unless the <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span></i> doctrine is to be abandoned, evidence illegally seized by state officers must be excluded as well from federal proceedings to determine liability under the federal wagering excise tax provisions. These provisions, constituting an "interrelated statutory system for taxing wagers," <i>Marchetti</i> v. <i>United States,</i> <span class="citation" data-id="107606"><a href="/opinion/107606/marchetti-v-united-states/#42" aria-description="Citation for case: Marchetti v. United States">390 U. S. 39, 42</a></span>, operate in an area "permeated with criminal statutes" and impose liability on a group "inherently suspect of criminal activities." <i>Albertson</i> v. <i>SACB,</i> <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#79" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 79</a></span>, quoted in <i>Marchetti</i> v. <i>United States, supra,</i> at 47. While the enforcement of these provisions results in the collection of revenue, "we cannot ignore either the characteristics of the activities" which give rise to wagering tax liability "or the composition of the group" from which payment is sought. <i>Grosso</i> v. <i>United States,</i> <span class="citation" data-id="9423605"><a href="/opinion/107607/grosso-v-united-states/#68" aria-description="Citation for case: Grosso v. United States">390 U. S. 62, 68</a></span>. The wagering provisions are intended not merely to raise revenue but also to "assist the efforts of state and federal authorities to enforce [criminal] penalties" for unlawful wagering activities. <i>Marchetti</i> v. <i>United States, supra,</i> at 47.</p>
<p>Federal officials responsible for the enforcement of the wagering tax provisions regularly cooperate with federal and local officials responsible for enforcing criminal laws restricting or forbidding wagering. See 390 U. S., at 47-48. Similarly, federal and local law enforcement personnel regularly provide federal tax officials with information, obtained in criminal investigations, indicating <span class="star-pagination">*462</span> liability under the wagering tax.<sup>[*]</sup> The pattern is one of mutual cooperation and coordination, with the federal wagering tax provisions buttressing state and federal criminal sanctions.</p>
<p><span class="star-pagination">*463</span> Given this pattern, our observation in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span></i> is directly opposite:</p>
<blockquote>"Free and open cooperation between state and federal law enforcement officers is to be commended and encouraged. Yet that kind of cooperation is hardly promoted by a rule that . . . at least tacitly [invites federal officers] to encourage state officers in the disregard of constitutionally protected freedom." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#221" aria-description="Citation for case: Elkins v. United States">364 U. S., at 221-222</a></span>.</blockquote>
<p>To be sure, the <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span></i> case was a federal criminal proceeding and the present case is civil in nature. But our prior decisions make it clear that this difference is irrelevant for Fourth Amendment exclusionary rule purposes where, as here, the civil proceeding serves as an adjunct to the enforcement of the criminal law. See <i>Plymouth Sedan</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693</a></span>.</p>
<p>The Court's failure to heed these precedents not only rips a hole in the fabric of the law but leads to a result that cannot even serve the valid arguments of those who would eliminate the exclusionary rule entirely. For under the Court's ruling, society must not only continue to pay the high cost of the exclusionary rule (by forgoing criminal convictions which can be obtained only on the basis of illegally seized evidence) but it must also forfeit the benefit for which it has paid so dearly.</p>
<p>If state police officials can effectively crack down on gambling law violators by the simple expedient of violating their constitutional rights and turning the illegally seized evidence over to Internal Revenue Service agents on the proverbial "silver platter," then the deterrent <span class="star-pagination">*464</span> purpose of the exclusionary rule is wholly frustrated. "If, on the other hand, it is understood that the fruit of an unlawful search by state agents will be inadmissible in a federal trial, there can be no inducement to subterfuge and evasion with respect to federal-state cooperation in criminal investigation." <i>Elkins</i> v. <i>United States, supra,</i> at 222.</p>
<h2>NOTES</h2>
<p>[1]  Officer Weissman's affidavit, App. 69-74, stated: He and Sergeant Briggs of the Los Angeles Police Department each had received information from an informant concerning respondent Janis and Levine and concerning telephone numbers the two men used for bookmaking. Police investigation disclosed that Janis had two telephones with unpublished numbers, including the number given by Weissman's informant, and that there was a third published number at the same address in the name of Nancy L. Janis. The unpublished numbers given by Weissman's informant as being used by Levine were found to be maintained by Levine at a different address, and that address was the one given by Briggs' informant as being Levine's base of operations. Both informants stated that Levine and Janis were working in concert. Each officer regarded his informant as reliable; the informant had given information in the past that led to arrests for bookmaking and, in the case of Briggs' informant, to convictions as well. Preliminary hearings and trials were pending for persons arrested with the aid of Weissman's informant. Each officer and his informant believed that it was necessary for the informant's safety, and his future usefulness to law enforcement officers, that his identity be kept secret.
</p>
<p>Weissman further stated:</p>
<p>"From the nature and context of the information supplied by the informant to this affiant, and from the nature and context of the information which was supplied to Sgt. Briggs, as told to this affiant, it is believed that the informants . . . at all times mentioned in this affidavit, unless otherwise specified, were speaking with personal knowledge." <i>Id.,</i> at 73.</p>
<p>The affidavit, taken in its entirety, bears some similarity to the affidavit the Court later considered in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#420" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 420-422</a></span> (1969). <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> was a 5-3 decision handed down two months <i>after</i> the Los Angeles warrant in the present case had been issued. MR. JUSTICE WHITE joined the opinion in <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#423" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, id.,</i> at 423-429</a></span>, but, in doing so, referred, <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#427" aria-description="Citation for case: Spinelli v. United States"><i>id.,</i> at 427</a></span>, to the "tension between <i>Draper</i> [v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959)]," on the one hand, and <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933), and <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), on the other, and, "[p]ending full-scale reconsideration" of <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> "or of the <i>Nathanson-Aguilar</i> cases," joined "the opinion of the Court and the judgment of reversal, especially since a vote to affirm would produce an equally divided Court." <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#429" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 429</a></span>.</p>
<p>[2]  The Internal Revenue Service's Certificate of Assessments and Payments, App. 81, shows a credit of $5,097, the amount actually seized by the police and subjected to the Service's subsequent levy. The Government acknowledges, however, that $157 of this amount was money belonging to Levine. It was applied upon the joint assessment made against both Janis and Levine. Levine has not sought a refund of the $157. Brief for United States 5 n. 1. The present case, therefore, concerns only the $4,940 taken from respondent Janis.</p>
<p>[3]  Officer Weissman testified that there was no departmental policy to call the Internal Revenue Service in a situation of this kind. He did it "as a matter of police procedure." He would not do it, he said, on what he "would consider a small-size book, but I considered this one a major-size book. So, I, therefore, did it." App. 42. He further stated that some of his fellow officers had acted similarly, but that he did not think "that they all have done it." <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Ibid.</a></span></i> The District Court did not rest its conclusion on any federal involvement in, or encouragement of, the search. We therefore must assume, for purposes of this opinion, that there was no federal involvement. See n. 31, <i>infra.</i></p>
<p>[4]  The wagering excise tax at the time was 10% of the amount of the wagers. § 4401 (a) of the Internal Revenue Code of 1954, <span class="citation no-link">26 U. S. C. § 4401</span> (a). The rate was reduced to 2%, effective December 1, 1974, by <span class="citation no-link">Pub. L. 93-499, § 3</span> (a), <span class="citation no-link">88 Stat. 1550</span>.</p>
<p>[5]  The Government advises us that, in order to avoid multiple litigation, its policy is to counterclaim in a refund suit, just as it did here, where there is an outstanding unpaid assessment and the refund suit and the counterclaim involve the same facts. Brief for United States 17 n. 4.</p>
<p>[6]  The Certificate of Assessments and Payments was stipulated "to be admissible without objection." App. 20. The Government did not seek to introduce the wagering records obtained by the Los Angeles police.
</p>
<p>The Government has not asserted that, absent the seized materials, it would have had grounds for an assessment against respondent and Levine.</p>
<p>[7]  The situation may be described as having some resemblance to that for which the Court has developed an exception to the Anti-Injunction Act, § 7421 (a) of the Code, <span class="citation no-link">26 U. S. C. § 7421</span> (a). See <i>Enochs</i> v. <i>Williams Packing Co.,</i> <span class="citation" data-id="106413"><a href="/opinion/106413/enochs-v-williams-packing-navigation-co/" aria-description="Citation for case: Enochs v. Williams Packing &amp; Navigation Co.">370 U. S. 1</a></span> (1962); <i>Bob Jones University</i> v. <i>Simon,</i> <span class="citation" data-id="9425714"><a href="/opinion/109028/bob-jones-university-v-simon/" aria-description="Citation for case: Bob Jones University v. Simon">416 U. S. 725</a></span> (1974); <i>Commissioner</i> v. "<i>Americans United</i>" <i>Inc.,</i> <span class="citation" data-id="9425716"><a href="/opinion/109029/alexander-v-americans-united-inc/" aria-description="Citation for case: Alexander v. &quot;Americans United&quot; Inc.">416 U. S. 752</a></span> (1974); <i>Laing</i> v. <i>United States,</i> <span class="citation" data-id="9426233"><a href="/opinion/109340/laing-v-united-states/" aria-description="Citation for case: Laing v. United States">423 U. S. 161</a></span> (1976); <i>Commissioner</i> v. <i>Shapiro,</i> <span class="citation" data-id="9426305"><a href="/opinion/109396/commissioner-v-shapiro/" aria-description="Citation for case: Commissioner v. Shapiro">424 U. S. 614</a></span> (1976).</p>
<p>[8]  <i><span class="citation" data-id="9418831"><a href="/opinion/102360/helvering-v-taylor/" aria-description="Citation for case: Helvering v. Taylor">Taylor</a></span>,</i> although decided more than 40 years ago, has never been cited by this Court on the burden-of-proof issue. The Courts of Appeals, the Court of Claims, the Tax Court, and the Federal District Courts, however, frequently have referred to that aspect of the case.</p>
<p>[9]  <i>E. g., </i><i>Foster</i> v. <i>Commissioner,</i> <span class="citation" data-id="279381"><a href="/opinion/279381/grant-foster-and-barbara-dunn-foster-v-commissioner-of-internal-revenue/#735" aria-description="Citation for case: Grant Foster and Barbara Dunn Foster v. Commissioner of...">391 F. 2d 727, 735</a></span> (CA4 1968); <i>Herbert</i> v. <i>Commissioner,</i> <span class="citation" data-id="9452722"><a href="/opinion/275789/bow-herbert-and-nancy-herbert-v-commissioner-of-internal-revenue/#69" aria-description="Citation for case: Bow Herbert and Nancy Herbert v. Commissioner of Internal...">377 F. 2d 65, 69</a></span> (CA9 1967). See <i>Bar L Ranch, Inc.</i> v. <i>Phinney,</i> <span class="citation" data-id="290318"><a href="/opinion/290318/bar-l-ranch-inc-and-in-intervention-appellant-v-robert-l-phinney/#999" aria-description="Citation for case: Bar L Ranch, Inc., and in Intervention-Appellant v....">426 F. 2d 995, 999</a></span> (CA5 1970).</p>
<p>[10]  <i>E. g., </i><i>United States</i> v. <i>Rexach,</i> <span class="citation" data-id="312624"><a href="/opinion/312624/united-states-v-felix-benitez-rexach/#15" aria-description="Citation for case: United States v. Felix Benitez Rexach">482 F. 2d 10, 15-17</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1039/">414 U. S. 1039</a></span> (1973); <i>Psaty</i> v. <i>United States,</i> <span class="citation" data-id="296729"><a href="/opinion/296729/milton-r-psaty-and-martin-m-psaty-v-united-states/#1158" aria-description="Citation for case: Milton R. Psaty, and Martin M. Psaty v. United States">442 F. 2d 1154, 1158-1161</a></span> (CA3 1971); <i>Ehlers</i> v. <i>Vinal,</i> <span class="citation" data-id="8877642"><a href="/opinion/8891388/ehlers-v-vinal/#65" aria-description="Citation for case: Ehlers v. Vinal">382 F. 2d 58, 65-66</a></span> (CA8 1967). See <i>Bar L Ranch, Inc.</i> v. <i>Phinney,</i> <span class="citation" data-id="290318"><a href="/opinion/290318/bar-l-ranch-inc-and-in-intervention-appellant-v-robert-l-phinney/#998" aria-description="Citation for case: Bar L Ranch, Inc., and in Intervention-Appellant v....">426 F. 2d, at 998</a></span>.</p>
<p>[11]  Although the present case presents only the issue whether such evidence may be used in the formulation of the assessment, there appears to be no difference between that question and the issue whether the evidence is to be excluded in the refund or collection suit itself. We perceive no principled distinction to be made between the use of the evidence as the basis of an assessment and its use in the case in chief.</p>
<p>[12]  "[T]he ruptured privacy of the victims' homes and effects cannot be restored. Reparation comes too late." <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#637" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 637</a></span> (1965). "The rule is calculated to prevent, not to repair. Its purpose is to deterto compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960). See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347-348</a></span> (1974); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span> (1961); <i>Tehan</i> v. <i>United States ex rel. Shott,</i> <span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#413" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 413</a></span> (1966); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968).</p>
<p>[13]  In <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S., at 207</a></span> n. 1, the Court noted that the appellation stems from Mr. Justice Frankfurter's plurality opinion in <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span> (1949):
</p>
<p>"The crux of that doctrine is that a search is a search by a federal official if he had a hand in it; it is not a search by a federal official if evidence secured by state authorities is turned over to the federal authorities on a silver platter." <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#78" aria-description="Citation for case: Lustig v. United States"><i>Id.,</i> at 78-79</a></span>.</p>
<p>[14]  The absence of this Court's imposition of controls did not mean, of course, that the States were running unchecked in their pursuit of evidence. Not only were there tort remedies and internal disciplinary sanctions available, but, as the Court noted in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>:</i>
</p>
<p>"Not more than half the states continue totally to adhere to the rule that evidence is freely admissible no matter how it was obtained. Most of the others have adopted the exclusionary rule in its entirety; the rest have adopted it in part." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#219" aria-description="Citation for case: Elkins v. United States">364 U. S., at 219</a></span> (footnote omitted).</p>
<p>See also <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#224" aria-description="Citation for case: Elkins v. United States"><i>id.,</i> at 224-225</a></span> (Appendix to opinion).</p>
<p>[15]  Except for the unanimous decision written by Mr. Justice Day in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), the evolution of the exclusionary rule has been marked by sharp divisions in the Court. Indeed, <i>Wolf, Lustig, Rochin, Irvine, Elkins, Mapp,</i> and <i><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span></i> produced a combined total of 27 separate signed opinions or statements.</p>
<p>[16]  Thus, the Court has held that the exclusionary rule may be invoked only by those whose rights are infringed by the search itself, and not by those who are merely aggrieved by the introduction of evidence so obtained. <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174-175</a></span> (1969).</p>
<p>[17]  The Court has applied the exclusionary rule in a proceeding for forfeiture of an article used in violation of the criminal law. <i>Plymouth Sedan</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693</a></span> (1965). There it expressly relied on the fact that "forfeiture is clearly a penalty for the criminal offense" and "[i]t would be anomalous indeed, under these circumstances, to hold that in the criminal proceeding the illegally seized evidence is excludable, while in the forfeiture proceeding, requiring the determination that the criminal law has been violated, the same evidence would be admissible." <span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#701" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania"><i>Id.,</i> at 701</a></span>. See also <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 634</a></span> (1886), where a forfeiture proceeding was characterized as "quasi-criminal."</p>
<p>[18]  There are studies and commentary to the effect that the exclusionary rule tends to lessen the accuracy of the evidence presented in court because it encourages the police to lie in order to avoid suppression of evidence. See, <i>e. g.,</i> Garbus, Police Perjury: An Interview, <span class="citation no-link">8 Crim. L. Bull. 363</span> (1972); Kuh, The Mapp Case One Year After; An Appraisal of Its Impact in New York, 148 N. Y. L. J. Nos. 55 and 56 (1962); Comment, Police Perjury in Narcotics "Dropsy" Cases: A New Credibility Gap, 60 Geo. L. J. 507 (1971); Effect of <i>Mapp</i> v. <i>Ohio</i> on Police Search-and-Seizure Practices in Narcotics Cases, 4 Colum. J. L. &amp; Soc. Probs. 87 (1968). See also <i>People</i> v. <i>McMurty,</i> <span class="citation" data-id="6222348"><a href="/opinion/6353632/people-v-mcmurty/" aria-description="Citation for case: People v. McMurty">64 Misc. 2d 63</a></span>, 314 N. Y. S. 2d 194 (N. Y. C. Crim. Ct. 1970).</p>
<p>[19]  It is of interest to note that the exclusion of this evidence from the California state trial was required by a decision of the State's Supreme Court issued some years prior to <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i> See <i>People</i> v. <i>Cahan,</i> <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span> (1955).</p>
<p>[20]  We are aware of the suggestion, made by some commentators and incorporated in some studies, that police often view trial and conviction as a lesser aspect of law enforcement. See, <i>e. g.,</i> J. Skolnick, Justice Without Trial 219-235 (2d ed., 1975); Milner, Supreme Court Effectiveness and the Police Organization, <span class="citation no-link">36 Law &amp; Contemp. Probs. 467</span>, 475, 479 (1971); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 720-736 (1970).</p>
<p>[21]  See, <i>e. g., </i><i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (BURGER, C. J., dissenting); ALI Model Code of Pre-Arraignment Procedure § SS 290.2 (Proposed Official Draft 1975); Davidow, Criminal Procedure Ombudsman as a Substitute for the Exclusionary Rule: A Proposal, 4 Tex. Tech. L. Rev. 317 (1973); Davis, An Approach to Legal Control of the Police, 52 Texas L. Rev. 703 (1974); Foote, Tort Remedies for Police Violations of Individual Rights, <span class="citation no-link">39 Minn. L. Rev. 493</span> (1955); Geller, Enforcing the Fourth Amendment: The Exclusionary Rule and Its Alternatives, 1975 Wash. U. L. Q. 621; Kaplan, The Limits of the Exclusionary Rule, <span class="citation no-link">26 Stan. L. Rev. 1027</span> (1974); LaFave, Improving Police Performance Through the Exclusionary RulePart II: Defining the Norms and Training the Police, <span class="citation no-link">30 Mo. L. Rev. 566</span> (1965); McGowan, Rule-Making and the Police, <span class="citation no-link">70 Mich. L. Rev. 659</span> (1972); Quinn, The Effect of Police Rulemaking on the Scope of Fourth Amendment Rights, <span class="citation no-link">52 J. Urb. L. 25</span> (1974); Roche, A Viable Substitute for the Exclusionary Rule: A Civil Rights Appeals Board, <span class="citation no-link">30 Wash. &amp; Lee L. Rev. 223</span> (1973); Spiotto, The Search and Seizure ProblemTwo Approaches: The Canadian Tort Remedy and the U. S. Exclusionary Rule, 1 J. Police Sci. &amp; Ad. 36 (1973); Spiotto, Search and Seizure: An Empirical Study of the Exclusionary Rule and Its Alternatives, 2 J. Leg. Stud. 243 (1973); Comment, Federal Injunctive Relief from Illegal Search, 1967 Wash. U. L. Q. 104; Comment. The Federal Injunction as a Remedy for Unconstitutional Police Conduct, 78 Yale L. J. 143 (1968); Comment, Use of § 1983 to Remedy Unconstitutional Police Conduct: Guarding the Guards, 5 Harv. Civ. Rights-Civ. Lib. L. Rev. 104 (1970).</p>
<p>[22]  The salient and most comprehensive study is that of Oaks, cited above in n. 20. Professor (now President) Oaks reviews at length the data in previous studies and the problems involved in drawing conclusions from those data. The previous studies include, <i>inter alia,</i> D. Oaks &amp; W. Lehman, A Criminal Justice System and the Indigent: A Study of Chicago and Cook County (1968); J. Skolnick, Justice Without Trial (1st ed. 1966); Goldstein, Police Discretion not to Invoke the Criminal Process: Low-Visibility Decisions in the Administration of Justice, 69 Yale L. J. 543 (1960); Kamisar, On the Tactics of Police-Prosecution Oriented Critics of the Courts, 49 Cornell L. Q. 436 (1964); Kamisar, Public Safety v. Individual Liberties: Some "Facts" and "Theories," 53 J. Crim. L. C. &amp; P. S. 171 (1962); Kamisar, <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">Lustig</a></span></i> Ten Years Later: Illegal State Evidence in State and Federal Courts, <span class="citation no-link">43 Minn. L. Rev. 1083</span> (1959); Katz, The Supreme Court and the States: An Inquiry into Mapp v. Ohio in North Carolina. The Model, the Study and the Implications, 45 N. C. L. Rev. 119 (1966); Kuh, <i>supra,</i> n. 18; Nagel, Testing the Effects of Excluding Illegally Seized Evidence, <span class="citation no-link">1965 Wis. L. Rev. 283</span>; Paulsen, The Exclusionary Rule and Misconduct by the Police, 52 J. Crim. L. C. &amp; P. S. 255 (1961); Comment, Search and Seizure in Illinois: Enforcement of the Constitutional Right of Privacy, <span class="citation no-link">47 Nw. U. L. Rev. 493</span> (1952); Weinstein, Local Responsibility for Improvement of Search and Seizure Practices, 34 Rocky Mt. L. Rev. 150 (1962); Younger, Constitutional Protection on Search and Seizure Dead?, 3 Trial 41 (Aug-Sept. 1967); Comment, Effect of <i>Mapp</i> v. <i>Ohio</i> on Police Search-and-Seizure Practices in Narcotics Cases, 4 Colum. J. L. &amp; Soc. Probs. 87 (1968).
</p>
<p>Oaks discusses the types of research that may be possible, and the difficulties inherent in each. His final conclusion is straightforward:</p>
<p>"Writing just after the decision in <i>Mapp</i> v. <i>Ohio</i><i>,</i> Francis A. Allen declared that up to that time, `no effective quantitative measure of the rule's deterrent efficacy has been devised or applied.' [Allen, Federalism and the Fourth Amendment: A Requiem for <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> <span class="citation no-link">1961 Sup. Ct. Rev. 1</span>, 34.] That conclusion is not yet outdated. The foregoing findings represent the largest fund of information yet assembled on the effect of the exclusionary rule, but they obviously fall short of an empirical substantiation or refutation of the deterrent effect of the exclusionary rule." Oaks, <i>supra,</i> n. 20, at 709.</p>
<p>More recently, Canon, Is the Exclusionary Rule in Failing Health? Some New Data and a Plea against a Precipitous Conclusion, 62 Ky. L. J. 681 (1974), discusses the data collected and reviewed by Oaks, and explores the difficulties in drawing conclusions from those data. The paper also reviews studies that appeared subsequent to the Oaks article: Spiotto, <i>supra,</i> n. 21, at 243; and two papers by Michael Ban, The Impact of <i>Mapp</i> v. <i>Ohio</i> on Police Behavior (delivered at the annual meeting of the Midwest Political Science Assn., Chicago, May 1973) and Local Courts v. The Supreme Court: The Impact of <i>Mapp</i> v. <i>Ohio</i> (delivered at the annual meeting of the American Political Science Assn., New Orleans, Sept. 1973). Canon describes his own research, but his data and conclusions appear to suffer from many of the same difficulties and faults present in the prior studies, many of which are explicitly recognized. Consequently, although Canon argues in favor of retaining the exclusionary rule while Oaks argues against it, Canon's conclusions are no firmer than are Oaks': "Consequently, our argument is negative rather than positive; we are maintaining that the evidence from the 14 cities certainly does not support a conclusion that the exclusionary rule had no impact upon arrests in search-and-seizure type crimes in the years following its imposition." Canon, <i>supra,</i> at 707. "Consequently, we cannot confidently attribute the increased use of search warrants entirely or even primarily to police reaction to the exclusionary rule." <i>Id.,</i> at 713. See also <i>id.,</i> at 724-725 and at 725-726. Canon concedes that "the inconclusiveness of our findings is real enough," <i>id.,</i> at 726, but argues that the exclusionary rule should be given time to take effect. "Only after a substantial amount of time has passed do trends of changing behavior (if any) become apparent." <i>Id.,</i> at 727. One might wonder why, if the substantial amount of time necessary for the rule to take effect is extremely relevant, the study fails to take into account the fact that over half the States have had an exclusionary rule for a significantly greater length of time than <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> has been on the books.</p>
<p>Most recently, Critique. On the Limitations of Empirical Evaluations of the Exclusionary Rule: A Critique of the Spiotto Research and United States v. Calandra, <span class="citation no-link">69 Nw. U. L. Rev. 740</span> (1974), reviews the Oaks, Canon, and Spiotto papers and the studies mentioned therein. The comment discusses the design difficulties present and involved in studying the deterrent effect of the exclusionary rule in general. Although a proponent of the rule, the author concludes:</p>
<p>"A review of Spiotto's research and that conducted by others does not demonstrate the ineffectiveness of the exclusionary rule. Rather, it tends to illustrate the obstacles that stand in the way of any sound, empirical evaluation of the rule. When all factors are considered, there is virtually no likelihood that the Court is going to receive any `relevant statistics' which objectively measure the `practical efficacy' of the exclusionary rule." <span class="citation no-link"><i>Id.,</i> at 763-764</span>.</p>
<p>The final conclusion is clear. No empirical researcher, proponent or opponent of the rule, has yet been able to establish with any assurance whether the rule has a deterrent effect even in the situations in which it is now applied. It is, of course, virtually impossible to study the marginal deterrence added to <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> by the <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span></i> silver platter rule because of the difficulty of controlling the effect of intersovereign exclusion.</p>
<p>We are aware of no study on the possible deterrent effect of excluding evidence in a civil proceeding.</p>
<p>[23]  For discussion of the variables involved, see Canon, <i>supra,</i> n. 22; Geller, <i>supra,</i> n. 21; Kaplan, <i>supra,</i> n. 21; Milner, <i>supra,</i> n. 20: Oaks, <i>supra,</i> n. 20; Wright, Must the Criminal Go Free if the Constable Blunders?, 50 Texas L. Rev. 736 (1972); Critique, <i>supra.</i></p>
<p>[24]  Studies have attempted to compare the experience in countries without the exclusionary rule with the experience in this country. See, <i>e. g.,</i> Oaks, <i>supra,</i> n. 20, at 701-706; Spiotto, The Search and Seizure ProblemTwo Approaches: The Canadian Tort Remedy and the U. S. Exclusionary Rule, 1 J. Police Sci. &amp; Ad. 36 (1973). See generally The Exclusionary Rule Regarding Illegally Seized Evidence: An International Symposium, 52 J. Crim. L. C. &amp; P. S. 245 (1961). The difficulties in drawing conclusions from cross-cultural comparisons are self-evident. See also Canon, <i>supra,</i> n. 22, at 692 n. 53.</p>
<p>[25]  See generally <i>id.,</i> at 713-717, 723-725; Katz, <i>supra,</i> n. 22; Murphy, Judicial Review of Police Methods in Law Enforcement, 44 Texas L. Rev. 939, 941-943 (1966).</p>
<p>[26]  We do not mean to imply that more accurate studies could never be developed, or that what statisticians refer to as "triangulation" might not eventually provide us with firmer conclusions. We just do not find that the studies now available provide us with reliable conclusions.</p>
<p>[27]  If the exclusionary rule is not "strong medicine," but does provide some marginal deterrence in the criminal situations in which it is now applied, that marginal deterrence is diluted by the attenuation existing when a different sovereign uses the material in a civil proceeding, and we must again find that the marginal utility of the creation of such a rule is outweighed by the costs it imposes on society.</p>
<p>[28]  "[W]e simply decline to extend the court-made exclusionary rule to cases in which its deterrent purpose would not be served." <i>Desist</i> v. <i>United States,</i> <span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/" aria-description="Citation for case: Desist v. United States">394 U. S. 244</a></span>, 254 n. 24 (1969).
</p>
<p>"As with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>.</p>
<p>"Where the official action was pursued in complete good faith, however, the deterrence rationale loses much of its force." <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#447" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 447</a></span> (1974). See <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#537" aria-description="Citation for case: United States v. Peltier">422 U. S., at 537-538</a></span>.</p>
<p>[29]  "[I]t will not do to forget that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule is a rule arrived at only on the nicest balance of competing considerations and in view of the necessity of finding some effective judicial sanction to preserve the Constitution's search and seizure guarantees. The rule is unsupportable as reparation or compensatory dispensation to the injured criminal; its sole rational justification is the experience of its indispensability in `exert[ing] general legal pressures to secure obedience to the Fourth Amendment on the part of federal law-enforcing officers.' As it serves this function, the rule is a needed, but grud[g]ingly taken, medicament; no more should be swallowed than is needed to combat the disease. Granted that so many criminals must go free as will deter the constables from blundering, pursuance of this policy of liberation beyond the confines of necessity inflicts gratuitous harm on the public interest as declared by Congress." Amsterdam, Search, Seizure, and Section 2255: A Comment, <span class="citation no-link">112 U. Pa. L. Rev. 378</span>, 388-389 (1964) (footnotes omitted).</p>
<p>[30]  <i>Suarez</i> v. <i>Commissioner,</i> <span class="citation" data-id="4482081"><a href="/opinion/4703384/suarez-v-commissioner/" aria-description="Citation for case: Suarez v. Commissioner">58 T. C. 792</a></span> (1972); <i>Pizzarello</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/408/579/">408 F. 2d 579</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/986/">396 U. S. 986</a></span> (1969); <i>Knoll Associates, Inc.</i> v. <i>FTC,</i> <span class="citation" data-id="9453781"><a href="/opinion/280893/knoll-associates-inc-a-new-york-corporation-v-federal-trade-commission/" aria-description="Citation for case: Knoll Associates, Inc., a New York Corporation v. Federal...">397 F. 2d 530</a></span> (CA7 1968); <i>Powell</i> v. <i>Zuckert,</i> 125 U. S. App. D. C. 55, <span class="citation" data-id="273172"><a href="/opinion/273172/robert-i-powell-v-eugene-m-zuckert/" aria-description="Citation for case: Robert I. Powell v. Eugene M. Zuckert">366 F. 2d 634</a></span> (1966); <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="1550076"><a href="/opinion/1550076/rogers-v-united-states/" aria-description="Citation for case: Rogers v. United States">97 F. 2d 691</a></span> (CA1 1938); <i>Anderson</i> v. <i>Richardson,</i> <span class="citation" data-id="1380502"><a href="/opinion/1380502/anderson-v-richardson/" aria-description="Citation for case: Anderson v. Richardson">354 F. Supp. 363</a></span> (SD Fla. 1973); <i>Iowa</i> v. <i>Union Asphalt &amp; Roadoils, Inc.,</i> <span class="citation" data-id="1575214"><a href="/opinion/1575214/state-of-iowa-v-union-asphalt-roadoils-inc/" aria-description="Citation for case: State of Iowa v. Union Asphalt &amp; Roadoils, Inc.">281 F. Supp. 391</a></span> (SD Iowa 1968), aff'd <i>sub nom. </i><i>Standard Oil Co.</i> v. <i>Iowa,</i> <span class="citation" data-id="284130"><a href="/opinion/284130/standard-oil-company-v-state-of-iowa/" aria-description="Citation for case: Standard Oil Company v. State of Iowa">408 F. 2d 1171</a></span> (CA8 1969); <i>United States</i> v. <i>Stonehill,</i> <span class="citation" data-id="1574898"><a href="/opinion/1574898/united-states-v-stonehill/" aria-description="Citation for case: United States v. Stonehill">274 F. Supp. 420</a></span> (SD Cal. 1967), aff'd, <span class="citation" data-id="9454171"><a href="/opinion/283019/harry-s-stonehill-and-robert-p-brooks-v-united-states/" aria-description="Citation for case: Harry S. Stonehill and Robert P. Brooks v. United States">405 F. 2d 738</a></span> (CA9 1968), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./395/960/">395 U. S. 960</a></span> (1969); <i>United States</i> v. <i>Blank,</i> <span class="citation" data-id="1675172"><a href="/opinion/1675172/united-states-v-blank/" aria-description="Citation for case: United States v. Blank">261 F. Supp. 180</a></span> (ND Ohio 1966); <i>Lassoff</i> v. <i>Gray,</i> <span class="citation" data-id="2262725"><a href="/opinion/2262725/lassoff-v-gray/" aria-description="Citation for case: Lassoff v. Gray">207 F. Supp. 843</a></span> (WD Ky. 1962).</p>
<p>[31]  The decision by the District Court to suppress the evidence did not rest upon any finding of such an agreement or participation, and from the record it does not appear that any "federal participation" existed. See <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span> (1949); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927). As stated above in n. 3, we decide the present case on the assumption that no such agreement or arrangement existed. Respondent remains free on remand to attempt to prove that there was federal participation in fact. If he succeeds in that proof, he raises the question, not presented by this case, whether the exclusionary rule is to be applied in a civil proceeding involving an intrasovereign violation.
</p>
<p>It is well established, of course, that the exclusionary rule, as a deterrent sanction, is not applicable where a private party or a foreign government commits the offending act. See <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921); <i>United States</i> v. <i>Stonehill, supra</i><i>.</i></p>
<p>[32]  See <i>Pizzarello</i> v. <i>United States, supra</i><i>; </i><i>Knoll Associates, Inc.</i> v. <i>FTC, supra</i><i>; </i><i>Powell</i> v. <i><span class="citation" data-id="273172"><a href="/opinion/273172/robert-i-powell-v-eugene-m-zuckert/" aria-description="Citation for case: Robert I. Powell v. Eugene M. Zuckert">Zuckert, supra</a></span></i><i>; </i><i>Iowa</i> v. <i>Union Asphalt &amp; Roadoils, Inc., supra</i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="1675172"><a href="/opinion/1675172/united-states-v-blank/" aria-description="Citation for case: United States v. Blank">Blank, supra</a></span></i><i>.</i> See also <i>Hand</i> v. <i>United States,</i> <span class="citation" data-id="8885229"><a href="/opinion/8898533/hand-v-united-states/" aria-description="Citation for case: Hand v. United States">441 F. 2d 529</a></span> (CA5 1971).</p>
<p>[33]  We express no view on the issue whether sentencing and parole revocation proceedings constitute "civil proceedings" for the purposes of the principles announced in this opinion.</p>
<p>[34]  In <i>Anderson</i> v. <i>Richardson,</i> <span class="citation" data-id="1380502"><a href="/opinion/1380502/anderson-v-richardson/" aria-description="Citation for case: Anderson v. Richardson">354 F. Supp. 363</a></span> (SD Fla. 1973), which otherwise might be in this category, the trial court relied on <i>Pizzarello, supra,</i> in enjoining a tax assessment based upon illegally seized evidence. The Government had conceded, however, that the jeopardy assessment upon which it relied could not ultimately succeed. <span class="citation" data-id="1380502"><a href="/opinion/1380502/anderson-v-richardson/#366" aria-description="Citation for case: Anderson v. Richardson">354 F. Supp., at 366</a></span>. To the extent that dicta in that case might be relevant, the court failed to note that <i>Pizzarello</i> concerned an intrasovereign situation.
</p>
<p>In <i>United States</i> v. <i>Chase,</i> <span class="citation no-link">67-1 USTC ¶ 15733</span> (DC 1966), the District Court relied entirely upon principles of judicial integrity in excluding from a tax proceeding evidence unconstitutionally seized by state agents. <span class="citation no-link"><i>Id.,</i> at 84,477</span>. As noted previously, the Court has since clarified the fact that the primary, if not the sole, function of the exclusionary rule is deterrence. See <i>United States</i> v. <i><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra</a></span></i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier, supra</a></span></i><i>.</i> See also n. 35, <i>infra.</i></p>
<p>[35]  To the extent that recent cases state that deterrence is the prime purpose of the exclusionary rule, and that "judicial integrity" is a relevant, albeit subordinate factor, we hold that in this case considerations of judicial integrity do not require exclusion of the evidence.
</p>
<p>Judicial integrity clearly does not mean that the courts must never admit evidence obtained in violation of the Fourth Amendment. The requirement that a defendant must have standing to make a motion to suppress demonstrates as much. See <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969).</p>
<p>The primary meaning of "judicial integrity" in the context of evidentiary rules is that the courts must not commit or encourage violations of the Constitution. In the Fourth Amendment area, however, the evidence is unquestionably accurate, and the violation is complete by the time the evidence is presented to the court. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S., at 347, 354</a></span>. The focus therefore must be on the question whether the admission of the evidence encourages violations of Fourth Amendment rights. As the Court has noted in recent cases, this inquiry is essentially the same as the inquiry into whether exclusion would serve a deterrent purpose. See <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier">422 U. S., at 538</a></span>; <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 450</a></span> n. 25. The analysis showing that exclusion in this case has no demonstrated deterrent effect and is unlikely to have any significant such effect shows, by the same reasoning, that the admission of the evidence is unlikely to encourage violations of the Fourth Amendment. The admission of evidence in a federal civil proceeding is simply not important enough to state criminal law enforcement officers to encourage them to violate Fourth Amendment rights (and thus to obtain evidence that they are unable to use in either state or federal criminal proceedings). In addition, the officers here were clearly acting in good faith, see n. <span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">1, <i>supra,</i></a></span> a factor that the Court has recognized reduces significantly the potential deterrent effect of exclusion. See <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#447" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 447</a></span>; <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#539" aria-description="Citation for case: United States v. Peltier">422 U. S., at 539</a></span>.</p>
<p>[*]  The parties here stipulated as follows:
</p>
<p>"On December 3, 1968, Leonard Weissman, a Los Angeles Police Department officer, informed Morris Nimovitz, a revenue officer of the Internal Revenue Service, that the plaintiff herein had been arrested for alleged bookmaking activities. Officer Weissman was the same person who had prepared the affidavit in support of the search warrant which had been quashed by Judge Lang on the basis of an insufficient affidavit in support thereof. Mr. Nimovitz proceeded to the Los Angeles Police Department and with the help of Officer Weissman, analyzed certain betting markers and information which had been seized pursuant to the aforementioned search warrant. On the basis of their analysis, the gross volume of book-making activities alleged to have been conducted by the plaintiff herein and Morris Aaron Levine was determined for the five days immediately preceding the arrest of the plaintiff herein and Morris Aaron Levine. Officer Weissman further informed Mr. Nimovitz that he had commenced his investigation of the plaintiff herein on September 14, 1968, which continued on an intermittent basis through November 30, 1968, the date of the arrest. On the basis of the information given by Officer Weissman to Mr. Nimovitz, the civil tax assessment was made by taking five days of activities as determined from the items seized pursuant to the aforementioned search warrant and multiplying the daily gross volume times 77 days, to wit, the period of Officer Weissman's intermittent surveillance (September 14, 1968 through November 30, 1968)."</p>
<p>Officer Weissman stated as follows in a deposition:</p>
<p>"Q Now, Sergeant Weissman, is it police department policy to call the Internal Revenue Service when you have taken a substantial sum of cash related to a bookmaking arrest?</p>
<p>"A I don't think that there's policy either way. I justI did it as a matter ofI wouldn't say it was policy. I did it as a matter of police procedure.</p>
<p>"In other words, here's a person that was involved in a crime that had this kind of money, and I thought of Internal Revenue.</p>
<p>"Q Do you do that on a regular basis?</p>
<p>"A I don't do it on what I would consider a small-size book, but I considered this one a major-size book. So, I, therefore, did it.</p>
<p>"Q Would you do that with every major-size book that you run across with a substantial amount of cash?</p>
<p>"A I probably would."</p>

</div>
```

---
