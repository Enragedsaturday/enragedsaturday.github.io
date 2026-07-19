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

## GROUP: content/cases/Simmons v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Simmons v. United States"
type: case
citation: "390 U.S. 377 (1968)"
parallel_cite: "88 S. Ct. 967; 19 L. Ed. 2d 1247"
neutral_cite: 1968 U.S. LEXIS 2167
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-03-18
docket: 55
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-03-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Simmons v. United States
  varies_by_point: false
  scope_note: "Both holdings — the photographic-identification due-process standard and the immunity for suppression-hearing testimony — remain good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107636/simmons-v-united-states/"
  cluster_id: 107636
  opinion_id: 107636
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny"
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Stovall v. Denno]]", "[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[Jones v. United States]]", "[[Alderman v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "fifth-amendment", "standing", "eyewitness-identification", "photographic-identification", "due-process"]
holding: "A pretrial photographic identification violates due process only if it was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification; and a defendant's testimony given to establish Fourth Amendment standing at a suppression hearing may not be used against him at trial on guilt."
lake:
  record_id: Simmons v. United States
  status: verified
  projected_at: 2026-07-06
---

# Simmons v. United States

*390 U.S. 377 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Simmons, Andrews, and Garrett were tried for the armed robbery of a federally insured Chicago savings and loan. Two issues bear on this wiki. First, the FBI showed bank-employee eyewitnesses group photographs the day after the robbery, and Simmons argued the photographic procedure was so suggestive that it tainted the in-court identifications. Second, Garrett, to establish standing to suppress a suitcase of incriminating evidence, testified at a pretrial [[Common Legal Terms#suppression-hearing|suppression hearing]] that the suitcase was his; the Government used that admission against him at trial.

## Issue
(1) When does a pretrial photographic identification procedure deny due process; and (2) whether testimony a defendant gives at a [[Common Legal Terms#suppression-hearing|suppression hearing]] to establish [[Standing to Challenge a Search|Fourth Amendment standing]] may be admitted against him at trial on the issue of guilt.

## Rule
Two holdings. On identification: "convictions based on eyewitness identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." — 390 U.S. at 384. ^pin-384

On suppression-hearing testimony: a defendant should not have to trade one right for another. "[W]e find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection." — *Id.* at 394. ^pin-394

## Application
Applying the identification standard, Simmons's claim failed: the robbery occurred in a well-lit bank where five employees saw the robber for up to five minutes; the witnesses were shown at least six photographs each, separately, the next day while memories were fresh, with no suggestion of whom the FBI suspected; and all five identified Simmons. There was "little chance" of misidentification, so the procedure did not deny due process. As to Garrett, his suppression-hearing testimony admitting ownership of the suitcase was "a strong piece of evidence against [him]"; forcing him to choose between asserting his Fourth Amendment claim and his Fifth Amendment privilege was intolerable, so that testimony could not be used against him at trial.

## Conclusion
The judgment was affirmed as to Simmons (the photographic procedure was not impermissibly suggestive) and reversed as to Garrett (his suppression-hearing testimony was immunized from use on the issue of guilt).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Simmons* "very substantial likelihood of irreparable misidentification" standard, drawn from [[Stovall v. Denno]], carries into [[Neil v. Biggers]] and [[Manson v. Brathwaite]]; the suppression-hearing testimonial-immunity rule is the standing companion cited in [[Alderman v. United States]] and rests on the standing predicate of [[Jones v. United States]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny*
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *Simmons v. United States*, 390 U.S. 377 (1968) — https://www.courtlistener.com/opinion/107636/simmons-v-united-states/ — pinpoints: 384, 394.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1d64d2993c84d21a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "390 U.S. 377 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 2167", "official_citation_present": true, "parallel_cite": "88 S. Ct. 967; 19 L. Ed. 2d 1247", "title": "Simmons v. United States", "year": "1968"}}
{"assertion_id": "9c6253b263fb8d34", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A pretrial photographic identification violates due process only if it was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification; and a defendant's testimony given to establish Fourth Amendment standing at a suppression hearing may not be used against him at trial on guilt.", "title": "Simmons v. United States"}}
{"assertion_id": "ca51d9d28f5b7c52", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny", "title": "Simmons v. United States"}}
{"assertion_id": "fe825b2327eaffcd", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny", "title": "Simmons v. United States"}}
{"assertion_id": "8f6e9a6afc50a8eb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-03-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Simmons v. United States", "field_i_validity": "good_law", "scope_note": "Both holdings — the photographic-identification due-process standard and the immunity for suppression-hearing testimony — remain good law.", "title": "Simmons v. United States", "varies_by_point": "false"}}
{"assertion_id": "a5a25511b6ee1be1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Simmons v. United States"}}
```

### lake record — Simmons v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Simmons v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Simmons v. United States",
    "case_name_short": "Simmons",
    "case_name_full": "SIMMONS Et Al v. UNITED STATES",
    "input_case_name": "Simmons v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-03-18",
    "year": 1968,
    "docket": "55",
    "cluster_id": 107636,
    "lead_opinion_id": 107636,
    "sibling_ids": [
      107636,
      9423638,
      9423639,
      9423640
    ],
    "absolute_url": "/opinion/107636/simmons-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "390 U.S. 377",
      "volume": "390",
      "reporter": "U.S.",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 967",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1247",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 2167",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "390 U.S. 377",
        "volume": "390",
        "reporter": "U.S.",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 967",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1247",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 2167",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "390 U.S. 377",
    "official_selection": {
      "court_class": "scotus",
      "selected": "390 U.S. 377",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-384",
      "page": null,
      "quote": "--- # Simmons v. United States *390 U.S. 377 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Simmons, Andrews, and Garrett were tried for the armed robbery of a federally insured Chicago savings and loan. Two issues bear on this wiki. First, the FBI showed bank-employee eyewitnesses group photographs the day after the robbery, and Simmons argued the photographic procedure was so suggestive that it tainted the in-court identifications. Second, Garrett, to establish standing to suppress a suitcase of incriminating evidence, testified at a pretrial suppression hearing that the suitcase was his; the Government used that admission against him at trial. ## Issue (1) When does a pretrial photographic identification procedure deny due process; and (2) whether testimony a defendant gives at a suppression hearing to establish Fourth Amendment standing may be admitted against him at trial on the issue of guilt. ## Rule Two holdings. On identification:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-394",
      "page": null,
      "quote": "[W]e find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-03-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Simmons v. United States",
    "varies_by_point": false,
    "scope_note": "Both holdings \u2014 the photographic-identification due-process standard and the immunity for suppression-hearing testimony \u2014 remain good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Farook",
          "cluster_id": 9352623,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Farook",
          "cluster_id": 6466318,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fontanez",
          "cluster_id": 4610750,
          "cite": [
            "120 N.E.3d 707",
            "482 Mass. 22"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockett v. Ohio",
          "cluster_id": 109935,
          "cite": [
            "57 L. Ed. 2d 973",
            "98 S. Ct. 2954",
            "438 U.S. 586",
            "1978 U.S. LEXIS 133",
            "9 Ohio Op. 3d 26"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darden v. Wainwright",
          "cluster_id": 111717,
          "cite": [
            "91 L. Ed. 2d 144",
            "106 S. Ct. 2464",
            "477 U.S. 168",
            "1986 U.S. LEXIS 113"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tibbs v. Florida",
          "cluster_id": 110731,
          "cite": [
            "72 L. Ed. 2d 652",
            "102 S. Ct. 2211",
            "457 U.S. 31",
            "1982 U.S. LEXIS 116",
            "50 U.S.L.W. 4607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Green",
          "cluster_id": 108189,
          "cite": [
            "26 L. Ed. 2d 489",
            "90 S. Ct. 1930",
            "399 U.S. 149",
            "1970 U.S. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110382,
          "cite": [
            "66 L. Ed. 2d 722",
            "101 S. Ct. 764",
            "449 U.S. 539",
            "1981 U.S. LEXIS 62",
            "49 U.S.L.W. 4133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Stincer",
          "cluster_id": 111928,
          "cite": [
            "96 L. Ed. 2d 631",
            "107 S. Ct. 2658",
            "482 U.S. 730",
            "1987 U.S. LEXIS 2727",
            "55 U.S.L.W. 4901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. United States",
          "cluster_id": 108760,
          "cite": [
            "36 L. Ed. 2d 208",
            "93 S. Ct. 1565",
            "411 U.S. 223",
            "1973 U.S. LEXIS 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGautha v. California",
          "cluster_id": 108329,
          "cite": [
            "28 L. Ed. 2d 711",
            "91 S. Ct. 1454",
            "402 U.S. 183",
            "1971 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Foster v. California",
          "cluster_id": 107890,
          "cite": [
            "22 L. Ed. 2d 402",
            "89 S. Ct. 1127",
            "394 U.S. 440",
            "1969 U.S. LEXIS 2050"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conner v. State",
          "cluster_id": 2335623,
          "cite": [
            "67 S.W.3d 192",
            "2001 Tex. Crim. App. LEXIS 61",
            "2001 WL 1043248"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chaffin v. Stynchcombe",
          "cluster_id": 108793,
          "cite": [
            "36 L. Ed. 2d 714",
            "93 S. Ct. 1977",
            "412 U.S. 17",
            "1973 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ash",
          "cluster_id": 108846,
          "cite": [
            "37 L. Ed. 2d 619",
            "93 S. Ct. 2568",
            "413 U.S. 300",
            "1973 U.S. LEXIS 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDg3NzIxNjAwMDAwJnM9NDM3MDE0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01ODImcz0xOTYwODExJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 0,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
    "indexed_citing_opinions": 4614,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107636,
        "count": 4208,
        "count_source": "search"
      },
      {
        "opinion_id": 9423638,
        "count": 509,
        "count_source": "search"
      },
      {
        "opinion_id": 9423639,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423640,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6701,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/simmons-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTIyNzkmcz0xMDEyMjc0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107636,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 105517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 240852,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 261271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 262814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 271407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 274369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 276553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 278761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1178843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1472609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1509817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1542459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1569514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1609276,
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
    "date_created": "2026-07-05T19:46:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:49:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Simmons v. United States

```
<div>
<center><b><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U.S. 377</a></span> (1968)</b></center>
<center><h1>SIMMONS ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 55.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 15, 1968.</center>
<center>Decided March 18, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*379</span> <i>Raymond J. Smith</i> argued the cause for petitioners. With him on the brief were <i>John Powers Crowley</i> and <i>George F. Callaghan.</i></p>
<p><i>Solicitor General Griswold</i> argued the cause for the United States. With him on the brief were <i>Assistant Attorney General Vinson, Beatrice Rosenberg</i> and <i>Mervyn Hamburg.</i></p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>This case presents issues arising out of the petitioners trial and conviction in the United States District Court for the Northern District of Illinois for the armed robbery of a federally insured savings and loan association.</p>
<p>The evidence at trial showed that at about 1:45 p. m. <span class="star-pagination">*380</span> on February 27, 1964, two men entered a Chicago savings and loan association. One of them pointed a gun at a teller and ordered her to put money into a sack which the gunman supplied. The men remained in the bank about five minutes. After they left, a bank employee rushed to the street and saw one of the men sitting on the passenger side of a departing white 1960 Thunderbird automobile with a large scrape on the right door. Within an hour police located in the vicinity a car matching this description. They discovered that it belonged to a Mrs. Rey, sister-in-law of petitioner Simmons. She told the police that she had loaned the car for the afternoon to her brother, William Andrews.</p>
<p>At about 5:15 p. m. the same day, two FBI agents came to the house of Mrs. Mahon, Andrews' mother, about half a block from the place where the car was then parked.<sup>[1]</sup> The agents had no warrant, and at trial it was disputed whether Mrs. Mahon gave them permission to search the house. They did search, and in the basement they found two suitcases, of which Mrs. Mahon disclaimed any knowledge. One suitcase contained, among other items, a gun holster, a sack similar to the one used in the robbery, and several coin cards and bill wrappers from the bank which had been robbed.</p>
<p>The following morning the FBI obtained from another of Andrews' sisters some snapshots of Andrews and of petitioner Simmons, who was said by the sister to have been with Andrews the previous afternoon. These snapshots were shown to the five bank employees who had witnessed the robbery. Each witness identified pictures of Simmons as representing one of the robbers. A week or two later, three of these employees identified photographs <span class="star-pagination">*381</span> of petitioner Garrett as depicting the other robber, the other two witnesses stating that they did not have a clear view of the second robber.</p>
<p>The petitioners, together with William Andrews, subsequently were indicted and tried for the robbery, as indicated. Just prior to the trial, Garrett moved to suppress the Government's exhibit consisting of the suitcase containing the incriminating items. In order to establish his standing so to move, Garrett testified that, although he could not identify the suitcase with certainty, it was similar to one he had owned, and that he was the owner of clothing found inside the suitcase. The District Court denied the motion to suppress. Garrett's testimony at the "suppression" hearing was admitted against him at trial.</p>
<p>During the trial, all five bank employee witnesses identified Simmons as one of the robbers. Three of them identified Garrett as the second robber, the other two testifying that they did not get a good look at the second robber. The District Court denied the petitioners' request under <span class="citation no-link">18 U. S. C. § 3500</span> (the so-called Jencks Act) for production of the photographs which had been shown to the witnesses before trial.</p>
<p>The jury found Simmons and Garrett, as well as Andrews, guilty as charged. On appeal, the Court of Appeals for the Seventh Circuit affirmed as to Simmons and Garrett, but reversed the conviction of Andrews on the ground that there was insufficient evidence to connect him with the robbery. <span class="citation" data-id="274369"><a href="/opinion/274369/united-states-v-robert-james-garrett-thomas-earl-simmons-and-william-earl/" aria-description="Citation for case: United States v. Robert James Garrett, Thomas Earl...">371 F. 2d 296</a></span>.</p>
<p>We granted certiorari as to Simmons and Garrett, <span class="citation" data-id="8959716"><a href="/opinion/8968302/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">388 U. S. 906</a></span>, to consider the following claims. First, Simmons asserts that his pretrial identification by means of photographs was in the circumstances so unnecessarily suggestive and conducive to misidentification as to deny him due process of law, or at least to require reversal of his conviction in the exercise of our supervisory power <span class="star-pagination">*382</span> over the lower federal courts. Second, both petitioners contend that the District Court erred in refusing defense requests for production under <span class="citation no-link">18 U. S. C. § 3500</span> of the pictures of the petitioners which were shown to eyewitnesses prior to trial. Third, Garrett urges that his constitutional rights were violated when testimony given by him in support of his "suppression" motion was admitted against him at trial. For reasons which follow, we affirm the judgment of the Court of Appeals as to Simmons, but reverse as to Garrett.</p>
<p></p>
<h2>I.</h2>
<p>The facts as to the identification claim are these. As has been noted previously, FBI agents on the day following the robbery obtained from Andrews' sister a number of snapshots of Andrews and Simmons. There seem to have been at least six of these pictures, consisting mostly of group photographs of Andrews, Simmons, and others. Later the same day, these were shown to the five bank employees who had witnessed the robbery at their place of work, the photographs being exhibited to each employee separately. Each of the five employees identified Simmons from the photographs. At later dates, some of these witnesses were again interviewed by the FBI and shown indeterminate numbers of pictures. Again, all identified Simmons. At trial, the Government did not introduce any of the photographs, but relied upon in-court identification by the five eyewitnesses, each of whom swore that Simmons was one of the robbers.</p>
<p>In support of his argument, Simmons looks to last Term's "lineup" decisions<i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <i>Gilbert</i> v. <i>California,</i> 388 U. S. 263in which this Court first departed from the rule that the manner of an extra-judicial identification affects only the weight, not the admissibility, of identification testimony at trial. The rationale of those cases was that an <span class="star-pagination">*383</span> accused is entitled to counsel at any "critical stage of the prosecution," and that a post-indictment lineup is such a "critical stage." See 388 U. S., at 236-237. Simmons, however, does not contend that he was entitled to counsel at the time the pictures were shown to the witnesses. Rather, he asserts simply that in the circumstances the identification procedure was so unduly prejudicial as fatally to taint his conviction. This is a claim which must be evaluated in light of the totality of surrounding circumstances. See <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, at 302</a></span>; <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span>. Viewed in that context, we find the claim untenable.</p>
<p>It must be recognized that improper employment of photographs by police may sometimes cause witnesses to err in identifying criminals. A witness may have obtained only a brief glimpse of a criminal, or may have seen him under poor conditions. Even if the police subsequently follow the most correct photographic identification procedures and show him the pictures of a number of individuals without indicating whom they suspect, there is some danger that the witness may make an incorrect identification. This danger will be increased if the police display to the witness only the picture of a single individual who generally resembles the person he saw, or if they show him the pictures of several persons among which the photograph of a single such individual recurs or is in some way emphasized.<sup>[2]</sup> The chance of misidentification is also heightened if the police indicate to the witness that they have other evidence that one of the persons pictured committed the crime.<sup>[3]</sup> Regardless of how the initial misidentification comes about, the witness thereafter is apt to retain in his memory the image of the photograph rather than of the person actually <span class="star-pagination">*384</span> seen, reducing the trustworthiness of subsequent lineup or courtroom identification.<sup>[4]</sup></p>
<p>Despite the hazards of initial identification by photograph, this procedure has been used widely and effectively in criminal law enforcement, from the standpoint both of apprehending offenders and of sparing innocent suspects the ignominy of arrest by allowing eyewitnesses to exonerate them through scrutiny of photographs. The danger that use of the technique may result in convictions based on misidentification may be substantially lessened by a course of cross-examination at trial which exposes to the jury the method's potential for error. We are unwilling to prohibit its employment, either in the exercise of our supervisory power or, still less, as a matter of constitutional requirement. Instead, we hold that each case must be considered on its own facts, and that convictions based on eyewitness identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification. This standard accords with our resolution of a similar issue in <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 301-302</a></span>, and with decisions of other courts on the question of identification by photograph.<sup>[5]</sup></p>
<p>Applying the standard to this case, we conclude that petitioner Simmons' claim on this score must fail. In the first place, it is not suggested that it was unnecessary for the FBI to resort to photographic identification in this instance. A serious felony had been committed. The perpetrators were still at large. The inconclusive clues which law enforcement officials possessed led to <span class="star-pagination">*385</span> Andrews and Simmons. It was essential for the FBI agents swiftly to determine whether they were on the right track, so that they could properly deploy their forces in Chicago and, if necessary, alert officials in other cities. The justification for this method of procedure was hardly less compelling than that which we found to justify the "one-man lineup" in <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i></p>
<p>In the second place, there was in the circumstances of this case little chance that the procedure utilized led to misidentification of Simmons. The robbery took place in the afternoon in a well-lighted bank. The robbers wore no masks. Five bank employees had been able to see the robber later identified as Simmons for periods ranging up to five minutes. Those witnesses were shown the photographs only a day later, while their memories were still fresh. At least six photographs were displayed to each witness. Apparently, these consisted primarily of group photographs, with Simmons and Andrews each appearing several times in the series. Each witness was alone when he or she saw the photographs. There is no evidence to indicate that the witnesses were told anything about the progress of the investigation, or that the FBI agents in any other way suggested which persons in the pictures were under suspicion.</p>
<p>Under these conditions, all five eyewitnesses identified Simmons as one of the robbers. None identified Andrews, who apparently was as prominent in the photographs as Simmons. These initial identifications were confirmed by all five witnesses in subsequent viewings of photographs and at trial, where each witness identified Simmons in person. Notwithstanding cross-examination, none of the witnesses displayed any doubt about their respective identifications of Simmons. Taken together, these circumstances leave little room for doubt that the identification of Simmons was correct, even though the identification procedure employed may have in some <span class="star-pagination">*386</span> respects fallen short of the ideal.<sup>[6]</sup> We hold that in the factual surroundings of this case the identification procedure used was not such as to deny Simmons due process of law or to call for reversal under our supervisory authority.</p>
<p></p>
<h2>II.</h2>
<p>It is next contended, by both petitioners, that in any event the District Court erred in refusing a defense request that the photographs shown to the witnesses prior to trial be turned over to the defense for purposes of cross-examination. This claim to production is based on <span class="citation no-link">18 U. S. C. § 3500</span>, the so-called Jencks Act. That Act, passed in response to this Court's decision in <i>Jencks</i> v. <i>United States,</i> <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>, provides that after a witness has testified for the Government in a federal criminal prosecution the Government must, on request of the defense, produce any "statement . . . of the witness in the possession of the United States which relates to the subject matter as to which the witness has testified." For the Act's purposes, as they relate to this case, a "statement" is defined as "a written statement made by said witness and signed or otherwise adopted or approved by him . . . ."</p>
<p><span class="star-pagination">*387</span> Written statements of this kind were taken from all five eyewitnesses by the FBI on the day of the robbery. Apparently none were taken thereafter. When these statements were produced by the Government at trial pursuant to § 3500, the defense also claimed the right to look at the photographs "under 3500." The District Judge denied these requests.</p>
<p>The petitioners' theory seems to be that the photographs were incorporated in the written statements of the witnesses, and that they therefore had to be produced under § 3500. The legislative history of the Jencks Act does confirm that photographs must be produced if they constitute a part of a written statement.<sup>[7]</sup> However, the record in this case does not bear out the petitioners' claim that the pictures involved here were part of the statements which were approved by the witnesses and, therefore, producible under § 3500. It appears that all such statements were made on the day of the robbery. At that time, the FBI and police had no pictures of the petitioners. The first pictures were not acquired and shown to the witnesses until the morning of the following day. Hence, they could not possibly have been a part of the statements made and approved by the witnesses the day of the robbery.</p>
<p>The petitioners seem also to suggest that, quite apart from § 3500, the District Court's refusal of their request for the photographs amounted to an abuse of discretion. The photographs were not referred to by the Government in its case-in-chief. They were first asked for by the defense after the direct examination of the first eyewitness, <span class="star-pagination">*388</span> on the second day of the trial. When the defense requested the pictures, counsel for the Government noted that there were a "multitude" of pictures and stated that it might be difficult to identify those which were shown to particular witnesses. However, he indicated that the Government was willing to furnish all of the pictures, if they could be found. The District Court, referring to the fact that production of the photographs was not required under § 3500, stated that it would not stop the trial in order to have the pictures made available.</p>
<p>Although the pictures might have been of some assistance to the defense, and although it doubtless would have been preferable for the Government to have labeled the pictures shown to each witness and kept them available for trial,<sup>[8]</sup> we hold that in the circumstances the refusal of the District Court to order their production did not amount to an abuse of discretion, at least as to petitioner Simmons.<sup>[9]</sup> The defense surely knew that photographs had played a role in the identification process. Yet there was no attempt to have the pictures produced prior to trial pursuant to Fed. Rule Crim. Proc. 16. When production of the pictures was sought at trial, the defense did not explain why they were <span class="star-pagination">*389</span> needed, but simply argued that production was required under § 3500. Moreover, the strength of the eyewitness identifications of Simmons renders it highly unlikely that nonproduction of the photographs caused him any prejudice.</p>
<p></p>
<h2>III.</h2>
<p>Finally, it is contended that it was reversible error to allow the Government to use against Garrett on the issue of guilt the testimony given by him upon his unsuccessful motion to suppress as evidence the suitcase seized from Mrs. Mahon's basement and its contents. That testimony established that Garrett was the owner of the suitcase.<sup>[10]</sup></p>
<p>In order to effectuate the Fourth Amendment's guarantee of freedom from unreasonable searches and seizures, this Court long ago conferred upon defendants in federal prosecutions the right, upon motion and proof, to have excluded from trial evidence which had been secured by means of an unlawful search and seizure. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. More recently, this Court has held that "the exclusionary rule is an essential part of both the Fourth and Fourteenth Amendments. . . ." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#657" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 657</a></span>.</p>
<p>However, we have also held that rights assured by the Fourth Amendment are personal rights, and that they may be enforced by exclusion of evidence only at the instance of one whose own protection was infringed by the search and seizure. See, <i>e. g., </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#260" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 260-261</a></span>. At one time, a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor of <span class="star-pagination">*390</span> the seized property or that he had a possessory interest in the searched premises.<sup>[11]</sup> In part to avoid having to resolve the issue presented by this case, we relaxed those standing requirements in two alternative ways in <i>Jones</i> v. <i>United States, supra</i><i>.</i> First, we held that when, as in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> possession of the seized evidence is itself an essential element of the offense with which the defendant is charged, the Government is precluded from denying that the defendant has the requisite possessory interest to challenge the admission of the evidence. Second, we held alternatively that the defendant need have no possessory interest in the searched premises in order to have standing; it is sufficient that he be legitimately on those premises when the search occurs. Throughout this case, petitioner Garrett has justifiably, and without challenge from the Government, proceeded on the assumption that the standing requirements must be satisfied.<sup>[12]</sup> On that premise, he contends that testimony given by a defendant to meet such requirements should not be admissible against him at trial on the question of guilt or innocence. We agree.</p>
<p>Under the standing rules set out in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> there will be occasions, even in prosecutions for nonpossessory offenses, when a defendant's testimony will be needed to establish standing. This case serves as an example. <span class="star-pagination">*391</span> Garrett evidently was not in Mrs. Mahon's house at the time his suitcase was seized from her basement. The only, or at least the most natural, way in which he could found standing to object to the admission of the suitcase was to testify that he was its owner.<sup>[13]</sup> Thus, his testimony is to be regarded as an integral part of his Fourth Amendment exclusion claim. Under the rule laid down by the courts below, he could give that testimony only by assuming the risk that the testimony would later be admitted against him at trial. Testimony of this kind, which links a defendant to evidence which the Government considers important enough to seize and to seek to have admitted at trial, must often be highly prejudicial to a defendant. This case again serves as an example, for Garrett's admitted ownership of a suitcase which only a few hours after the robbery was found to contain money wrappers taken from the victimized bank was undoubtedly a strong piece of evidence against him. Without his testimony, the Government might have found it hard to prove that he was the owner of the suitcase.<sup>[14]</sup></p>
<p>The dilemma faced by defendants like Garrett is most extreme in prosecutions for possessory crimes, for then the testimony required for standing itself proves an element of the offense. We eliminated that Hobson's choice in <i>Jones</i> v. <i>United States, supra</i><i>,</i> by relaxing the standing requirements. This Court has never considered squarely the question whether defendants charged with nonpossessory crimes, like Garrett, are entitled to be relieved <span class="star-pagination">*392</span> of their dilemma entirely.<sup>[15]</sup> The lower courts which have considered the matter, both before and after <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> have with two exceptions agreed with the holdings of the courts below that the defendant's testimony may be admitted when, as here, the motion to suppress has failed.<sup>[16]</sup> The reasoning of some of these courts would seem to suggest that the testimony would be admissible even if the motion to suppress had succeeded,<sup>[17]</sup> but the only court which has actually decided that question held that when the motion to suppress succeeds the testimony given in support of it is excludable as a "fruit" of the unlawful search.<sup>[18]</sup> The rationale for admitting the testimony when the motion fails has been that the testimony is voluntarily given and relevant, and that it is therefore entitled to admission on the same basis as any other prior testimony or admission of a party.<sup>[19]</sup></p>
<p>It seems obvious that a defendant who knows that his testimony may be admissible against him at trial will sometimes be deterred from presenting the testimonial proof of standing necessary to assert a Fourth Amendment <span class="star-pagination">*393</span> claim. The likelihood of inhibition is greatest when the testimony is known to be admissible regardless of the outcome of the motion to suppress. But even in jurisdictions where the admissibility of the testimony depends upon the outcome of the motion, there will be a deterrent effect in those marginal cases in which it cannot be estimated with confidence whether the motion will succeed. Since search-and-seizure claims depend heavily upon their individual facts,<sup>[20]</sup> and since the law of search and seizure is in a state of flux,<sup>[21]</sup> the incidence of such marginal cases cannot be said to be negligible. In such circumstances, a defendant with a substantial claim for the exclusion of evidence may conclude that the admission of the evidence, together with the Government's proof linking it to him, is preferable to risking the admission of his own testimony connecting himself with the seized evidence.</p>
<p>The rule adopted by the courts below does not merely impose upon a defendant a condition which may deter him from asserting a Fourth Amendment objectionit imposes a condition of a kind to which this Court has always been peculiarly sensitive. For a defendant who wishes to establish standing must do so at the risk that the words which he utters may later be used to incriminate him. Those courts which have allowed the admission of testimony given to establish standing have reasoned that there is no violation of the Fifth Amendment's Self-Incrimination Clause because the testimony was voluntary.<sup>[22]</sup> As an abstract matter, this may well be true. A defendant is "compelled" to testify in support of a motion to suppress only in the sense that if he <span class="star-pagination">*394</span> refrains from testifying he will have to forgo a benefit, and testimony is not always involuntary as a matter of law simply because it is given to obtain a benefit.<sup>[23]</sup> However, the assumption which underlies this reasoning is that the defendant has a choice: he may refuse to testify and give up the benefit.<sup>[24]</sup> When this assumption is applied to a situation in which the "benefit" to be gained is that afforded by another provision of the Bill of Rights, an undeniable tension is created. Thus, in this case Garrett was obliged either to give up what he believed, with advice of counsel, to be a valid Fourth Amendment claim or, in legal effect, to waive his Fifth Amendment privilege against self-incrimination. In these circumstances, we find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.</p>
<p>For the foregoing reasons, we affirm the judgment of the Court of Appeals so far as it relates to petitioner Simmons. We reverse the judgment with respect to petitioner Garrett, and as to him remand the case to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p><span class="star-pagination">*395</span> MR. JUSTICE BLACK, concurring in part and dissenting in part.</p>
<p>I concur in affirmance of the conviction of Simmons but dissent from reversal of Garrett's conviction. I shall first discuss Simmons' case.</p>
<p>1. Simmons' chief claim is that his "pretrial identification [was] so unnecessarily suggestive and conducive to irreparable mistaken identification, that he was denied due process of law." The Court rejects this contention. I agree with the Court but for quite different reasons. The Court's opinion rests on a lengthy discussion of inferences that the jury could have drawn from the evidence of identifying witnesses. A mere summary reading of the evidence as outlined by this Court shows that its discussion is concerned with the weight of the testimony given by the identifying witnesses. The weight of the evidence, however, is not a question for the Court but for the jury, and does not raise a due process issue. The due process question raised by Simmons is, and should be held to be, frivolous. The identifying witnesses were all present in the bank when it was robbed and all saw the robbers. The due process contention revolves around the circumstances under which these witnesses identified pictures of the robbers shown to them, and these circumstances are relevant only to the weight the identification was entitled to be given. The Court, however, considers Simmons' contention on the premise that a denial of due process could be found in the "totality of circumstances" of the picture identification. I do not believe the Due Process Clause or any other constitutional provision vests this Court with any such wide-ranging, uncontrollable power. A trial according to due process of law is a trial according to the "law of the land"the law as enacted by the Constitution or the Legislative Branch of Government, and not "laws" formulated by the courts according to <span class="star-pagination">*396</span> the "totality of the circumstances." Simmons' due process claim here should be denied because it is frivolous.<sup>[*]</sup> For these reasons I vote to affirm Simmons' conviction.</p>
<p>2. I agree with the Court, in part for reasons it assigns, that the District Court did not commit error in declining to permit the photographs used to be turned over to the defense for purposes of cross-examination.</p>
<p>3. The Court makes new law in reversing Garrett's conviction on the ground that it was error to allow the Government to use against him testimony he had given upon his unsuccessful motion to suppress evidence allegedly seized in violation of the Fourth Amendment. The testimony used was Garrett's statement in the suppression hearing that he was the owner of a suitcase which contained money wrappers taken from the bank that was robbed. The Court is certainly guilty of no overstatement in saying that this "was undoubtedly a strong piece of evidence against [Garrett]." <i>Ante,</i> at 391. In fact, one might go further and say that this testimony, along with the statements of the eyewitnesses against him, showed beyond all question that Garrett was one of the bank robbers. The question then is whether the Government is barred from offering a truthful statement made by a defendant at a suppression hearing in order to prevent the defendant from winning an acquittal on the false premise that he is not the owner of the property he has already sworn that he owns. My answer to this question is "No." The Court's answer is "Yes" on the premise that "a defendant who knows that his testimony may be admissible against him at trial will sometimes <span class="star-pagination">*397</span> be deterred from presenting the testimonial proof of standing necessary to assert a Fourth Amendment claim." <i>Ante,</i> at 392-393.</p>
<p>For the Court, though not for me, the question seems to be whether the disadvantages associated with deterring a defendant from testifying on a motion to suppress are significant enough to offset the advantages of permitting the Government to use such testimony when relevant and probative to help convict the defendant of a crime. The Court itself concedes, however, that the deterrent effect on which it relies comes into play, at most, only in "marginal cases" in which the defendant cannot estimate whether the motion to suppress will succeed. <i>Ante,</i> at 393. The value of permitting the Government to use such testimony is, of course, so obvious that it is usually left unstated, but it should not for that reason be ignored. The standard of proof necessary to convict in a criminal case is high, and quite properly so, but for this reason highly probative evidence such as that involved here should not lightly be held inadmissible. For me the importance of bringing guilty criminals to book is a far more crucial consideration than the desirability of giving defendants every possible assistance in their attempts to invoke an evidentiary rule which itself can result in the exclusion of highly relevant evidence.</p>
<p>This leaves for me only the possible contention that Garrett's testimony was inadmissible under the Fifth Amendment because it was compelled. Of course, I could never accept the Court's statement that "testimony is not always involuntary as a matter of law simply because it is given to obtain a benefit." <i>Ante,</i> at 394. No matter what Professor Wigmore may have thought about the subject, it has always been clear to me that any threat of harm or promise of benefit is sufficient to render a defendant's statement involuntary. See <i>Shotwell</i> <span class="star-pagination">*398</span> <i>Mfg. Co.</i> v. <i>United States,</i> <span class="citation" data-id="106512"><a href="/opinion/106512/shotwell-manufacturing-co-v-united-states/#367" aria-description="Citation for case: Shotwell Manufacturing Co. v. United States">371 U. S. 341, 367</a></span> (1963) (dissenting opinion). The reason why the Fifth Amendment poses no bar to acceptance of Garrett's testimony is not, therefore, that a promise of benefit is not generally fatal. Rather, the answer is that the privilege against self-incrimination has always been considered a privilege that can be waived, and the validity of the waiver is, of course, not undermined by the inevitable fact that by testifying, a defendant can obtain the "benefit" of a chance to help his own case by the testimony he gives. When Garrett took the stand at the suppression hearing, he validly surrendered his privilege with respect to the statements he actually made at that time, and since these statements were therefore not "compelled," they could be used against him for any subsequent purpose.</p>
<p>The consequence of the Court's holding, it seems to me, is that defendants are encouraged to come into court, either in person or through other witnesses, and swear falsely that they do not own property, knowing at the very moment they do so that they have already sworn precisely the opposite in a prior court proceeding. This is but to permit lawless people to play ducks and drakes with the basic principles of the administration of criminal law.</p>
<p>There is certainly no language in the Fourth Amendment which gives support to any such device to hobble law enforcement in this country. While our Constitution does provide procedural safeguards to protect defendants from arbitrary convictions, that governmental charter holds out no promises to stultify justice by erecting barriers to the admissibility to relevant evidence voluntarily given in a court of justice. Under the first principles of ethics and morality a defendant who secures a court order by telling the truth should not be allowed to seek a court advantage later based on a premise <span class="star-pagination">*399</span> directly opposite to his prior solemn judicial oath. This Court should not lend the prestige of its high name to such a justice-defeating stratagem. I would affirm Garrett's conviction.</p>
<p>MR. JUSTICE WHITE, concurring in part and dissenting in part.</p>
<p>I concur in Parts I and II of the Court's opinion but dissent from the reversal of Garrett's conviction substantially for the reasons given by MR. JUSTICE BLACK in his separate opinion.</p>
<h2>NOTES</h2>
<p>[1]  Mrs. Mahon also testified that at about 3:30 p. m. the same day six men with guns forced their way into and ransacked her house. However, these men were never identified, and they apparently took nothing.</p>
<p>[2]  See P. Wall, Eye-Witness Identification in Criminal Cases 74-77 (1965).</p>
<p>[3]  See <i>id.,</i> at 82-83.</p>
<p>[4]  See <i>id.,</i> at 68-70.</p>
<p>[5]  See, <i>e. g., </i><i>People</i> v. <i>Evans,</i> <span class="citation" data-id="1178843"><a href="/opinion/1178843/people-v-evans/" aria-description="Citation for case: People v. Evans">39 Cal. 2d 242</a></span>, <span class="citation" data-id="1178843"><a href="/opinion/1178843/people-v-evans/" aria-description="Citation for case: People v. Evans">246 P. 2d 636</a></span>.</p>
<p>[6]  The reliability of the identification procedure could have been increased by allowing only one or two of the five eyewitnesses to view the pictures of Simmons. If thus identified, Simmons could later have been displayed to the other eyewitnesses in a lineup, thus permitting the photographic identification to be supplemented by a corporeal identification, which is normally more accurate. See P. Wall, Eye-Witness Identification in Criminal Cases 83 (1965); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 531. Also, it probably would have been preferable for the witnesses to have been shown more than six snapshots, for those snapshots to have pictured a greater number of individuals, and for there to have been proportionally fewer pictures of Simmons. See Wall, <i>supra,</i> at 74-82; Williams, <i>supra,</i> at 530.</p>
<p>[7]  In the discussion of the bill on the floor of the Senate, Senator O'Mahoney, sponsor of the bill in the Senate, stated that photographs <i>per se</i> were not required to be produced under the bill, but that "[i]f the pictures have anything to do with the statement of the witness . . . of course that would be part of it . . . ." 103 Cong. Rec. 16489.</p>
<p>[8]  See P. Wall, Eye-Witness Identification in Criminal Cases 84 (1965); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 530.</p>
<p>[9]  Garrett was also initially identified from photographs, but at a later date than Simmons. He was identified by fewer witnesses than was Simmons, and even those witnesses had less opportunity to see him during the robbery than they did Simmons. The record is opaque as to the number and type of photographs of Garrett which were shown to these witnesses, and as to the circumstances of the showings. However, it is unnecessary to decide whether Garrett was prejudiced by the District Court's failure to order production of the pictures at trial, since we are reversing Garrett's conviction on other grounds.</p>
<p>[10]  Although petitioner Simmons objected at trial to the admission of Garrett's testimony, the claim was not pressed on his behalf here. Garrett did not mention Simmons in his testimony, and the District Court instructed the jury to consider the testimony only with reference to Garrett.</p>
<p>[11]  See, <i>e. g., </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States">362 U. S. 257, at 262</a></span>; Edwards, Standing to Suppress Unreasonably Seized Evidence, <span class="citation no-link">47 Nw. U. L. Rev. 471</span> (1952).</p>
<p>[12]  It has been suggested that the adoption of a "police-deterrent" rationale for the exclusionary rule, see <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>, logically dictates that a defendant should be able to object to the admission against him of <i>any</i> unconstitutionally seized evidence. See Comment, Standing to Object to an Unreasonable Search and Seizure, <span class="citation no-link">34 U. Chi. L. Rev. 342</span> (1967); Note, Standing to Object to an Unlawful Search and Seizure, 1965 Wash. U. L. Q. 488. However, that argument is not advanced in this case, and we do not consider it.</p>
<p>[13]  The record shows that Mrs. Mahon, the owner of the premises from which the suitcase was taken, disclaimed all knowledge of its presence there and of its ownership.</p>
<p>[14]  The Government concedes that there were no identifying marks on the outside of the suitcase. See Brief for the United States 33.</p>
<p>[15]  In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the only reference to the subject was a statement that "[The defendant] has been faced . . . with the chance that the allegations made on the motion to suppress may be used against him at the trial, although that they may is by no means an inevitable holding . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States">362 U. S., at 262</a></span>.</p>
<p>[16]  See <i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>; <i>Kaiser</i> v. <i>United States,</i> <span class="citation" data-id="1542459"><a href="/opinion/1542459/kaiser-v-united-states/" aria-description="Citation for case: Kaiser v. United States">60 F. 2d 410</a></span>; <i>Fowler</i> v. <i>United States,</i> <span class="citation" data-id="240852"><a href="/opinion/240852/harvey-gene-fowler-v-united-states-of-america-two-cases-haskell-d/" aria-description="Citation for case: Harvey Gene Fowler v. United States of America, (Two...">239 F. 2d 93</a></span>; <i>Monroe</i> v. <i>United States,</i> <span class="citation" data-id="261271"><a href="/opinion/261271/henry-monroe-v-united-states/" aria-description="Citation for case: Henry Monroe v. United States">320 F. 2d 277</a></span>; <i>United States</i> v. <i>Taylor,</i> <span class="citation" data-id="262814"><a href="/opinion/262814/united-states-v-gerald-j-taylor-clifton-a-hammond-and-john-w-butler/" aria-description="Citation for case: United States v. Gerald J. Taylor, Clifton A. Hammond,...">326 F. 2d 277</a></span>; <i>United States</i> v. <i>Airdo,</i> <span class="citation" data-id="276553"><a href="/opinion/276553/united-states-v-dominic-daniel-alrdo/" aria-description="Citation for case: United States v. Dominic Daniel Alrdo">380 F. 2d 103</a></span>; <i>United States</i> v. <i>Lindsly,</i> <span class="citation" data-id="1509817"><a href="/opinion/1509817/united-states-v-lindsly/" aria-description="Citation for case: United States v. Lindsly">7 F. 2d 247</a></span>, rev'd on other grounds, <span class="citation" data-id="6832764"><a href="/opinion/6936013/lindsly-v-united-states/" aria-description="Citation for case: Lindsly v. United States">12 F. 2d 771</a></span>. Contra, see <i>Bailey</i> v. <i>United States,</i> 128 U. S. App. D. C. 354, <span class="citation" data-id="8878268"><a href="/opinion/8891974/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">389 F. 2d 305</a></span>; <i>United States</i> v. <i>Lewis,</i> <span class="citation" data-id="1609276"><a href="/opinion/1609276/united-states-v-lewis/#810" aria-description="Citation for case: United States v. Lewis">270 F. Supp. 807, 810, n. 1</a></span> (dictum).</p>
<p>[17]  See, <i>e. g., </i><i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>; <i>Monroe</i> v. <i>United States,</i> <span class="citation" data-id="261271"><a href="/opinion/261271/henry-monroe-v-united-states/" aria-description="Citation for case: Henry Monroe v. United States">320 F. 2d 277</a></span>.</p>
<p>[18]  See <i>Safarik</i> v. <i>United States,</i> <span class="citation" data-id="1472609"><a href="/opinion/1472609/safarik-v-united-states/" aria-description="Citation for case: Safarik v. United States">62 F. 2d 892</a></span>, rehearing denied, <span class="citation" data-id="6854259"><a href="/opinion/6957046/safarik-v-united-states/" aria-description="Citation for case: Safarik v. United States">63 F. 2d 369</a></span>. Accord, <i>Fowler</i> v. <i>United States,</i> <span class="citation" data-id="240852"><a href="/opinion/240852/harvey-gene-fowler-v-united-states-of-america-two-cases-haskell-d/" aria-description="Citation for case: Harvey Gene Fowler v. United States of America, (Two...">239 F. 2d 93</a></span> (dictum); cf. <i>Fabri</i> v. <i>United States,</i> <span class="citation" data-id="6836858"><a href="/opinion/6940021/fabri-v-united-states/" aria-description="Citation for case: Fabri v. United States">24 F. 2d 185</a></span>.</p>
<p>[19]  See cases cited in n. 16, <i>supra.</i></p>
<p>[20]  See, <i>e. g., </i><i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63</a></span>.</p>
<p>[21]  <i>E. g.,</i> compare <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, with <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; compare <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, with <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>.</p>
<p>[22]  See, <i>e. g., </i><i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>.</p>
<p>[23]  For example, testimony given for his own benefit by a plaintiff in a civil suit is admissible against him in a subsequent criminal prosecution. See 4 Wigmore, Evidence § 1066 (3d ed. 1940); 8 <i>id.,</i> § 2276 (McNaughton rev. 1961).</p>
<p>[24]  <i>Ibid.</i></p>
<p>[*]  Although Simmons' "questions presented" raise no such contention, the Court declines to use its "supervisory power" to hold Simmons' rights were violated by the identification methods. One must look to the Constitution in vain, I think, to find a "supervisory power" in this Court to reverse cases like this on such a ground.</p>

</div>
```

---

## GROUP: content/cases/Smith v. Cain.md  (`case`, 5 assertions)

### content_page

```
---
title: "Smith v. Cain"
type: case
citation: "565 U.S. 73 (2012)"
parallel_cite: "132 S. Ct. 627; 181 L. Ed. 2d 571"
neutral_cite: 2012 U.S. LEXIS 576
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-10
docket: 10-8145
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Cain
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/620666/smith-v-cain/"
  cluster_id: 620666
  opinion_id: 620666
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Strickler v. Greene]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]"]
aliases: []
tags: ["case", "brady", "impeachment", "materiality", "due-process"]
holding: "Modern *Brady* reversal: undisclosed impeachment of the sole eyewitness is material — conviction reversed."
lake:
  record_id: Smith v. Cain
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Cain

*565 U.S. 73 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Juan Smith was convicted of five murders based solely on the testimony of a single eyewitness, Larry Boatner, who told the jury he had "[n]o doubt" Smith was the gunman. The prosecution had not disclosed police notes recording that, on the night of the crime and days later, Boatner said he could not identify anyone. Smith sought relief under *[[Brady v. Maryland|Brady]]*.

## Issue
Whether the State's failure to disclose the eyewitness's contradictory statements was a material *[[Brady v. Maryland|Brady]]* violation.

## Rule
Suppressed impeachment evidence is material when it could reasonably undermine confidence in the verdict. "[E]vidence impeaching an eyewitness may not be material if the State's other evidence is strong enough to sustain confidence in the verdict." — 565 U.S. 73 (2012) (slip op., at 2). ^pin-2

But here "Boatner's undisclosed statements were plainly material." — *Id.* (slip op., at 3). ^pin-3

## Application
Boatner's testimony was the only evidence linking Smith to the crime, and his undisclosed statements—that he "could not ID anyone because [he] couldn't see faces"—directly contradicted his confident trial identification. Because that impeachment was material and the State failed to disclose it, the nondisclosure violated *[[Brady v. Maryland|Brady]]*, and the conviction was reversed.

## Conclusion
The undisclosed impeachment of the sole eyewitness was material; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- A modern application of the materiality standard of [[Brady v. Maryland]] and [[Strickler v. Greene]] to impeachment evidence ([[Giglio v. United States]]); see the cumulative-materiality analysis of [[Kyles v. Whitley]] and [[United States v. Bagley]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Smith v. Cain*, 565 U.S. 73 (2012) — https://www.courtlistener.com/opinion/620666/smith-v-cain/ — pinpoints: slip op. 2, 3.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bb1a953002969790", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 73 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 576", "official_citation_present": true, "parallel_cite": "132 S. Ct. 627; 181 L. Ed. 2d 571", "title": "Smith v. Cain", "year": "2012"}}
{"assertion_id": "b084072b140bf9ff", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Smith v. Cain"}}
{"assertion_id": "eb120cae9fc8e2fc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Modern *Brady* reversal: undisclosed impeachment of the sole eyewitness is material — conviction reversed.", "title": "Smith v. Cain"}}
{"assertion_id": "497d797bd51724d6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Smith v. Cain"}}
{"assertion_id": "4c47868d55248469", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-01-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Smith v. Cain", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Smith v. Cain", "varies_by_point": "false"}}
```

### lake record — Smith v. Cain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Cain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Cain",
    "case_name_short": "Cain",
    "case_name_full": "Smith v. Cain, Warden",
    "input_case_name": "Smith v. Cain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-10",
    "year": 2012,
    "docket": "10-8145",
    "cluster_id": 620666,
    "lead_opinion_id": 620666,
    "sibling_ids": [
      620666,
      9485187,
      9485188
    ],
    "absolute_url": "/opinion/620666/smith-v-cain/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 73",
      "volume": "565",
      "reporter": "U.S.",
      "page": "73",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 627",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 571",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "571",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 576",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 627",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 571",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "571",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 73",
        "volume": "565",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 576",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 73",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 73",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2",
      "page": null,
      "quote": "Smith was the gunman. The prosecution had not disclosed police notes recording that, on the night of the crime and days later, Boatner said he could not identify anyone. Smith sought relief under *Brady*. ## Issue Whether the State's failure to disclose the eyewitness's contradictory statements was a material *Brady* violation. ## Rule Suppressed impeachment evidence is material when it could reasonably undermine confidence in the verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-3",
      "page": null,
      "quote": "Boatner's undisclosed statements were plainly material.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Cain",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lesley Esther Diamond v. State",
          "cluster_id": 4546474,
          "cite": [
            "561 S.W.3d 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lesley Esther Diamond v. State",
          "cluster_id": 4534153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santos",
          "cluster_id": 4450366,
          "cite": [
            "176 A.3d 877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Bartko",
          "cluster_id": 1038291,
          "cite": [
            "728 F.3d 327",
            "2013 WL 4560333",
            "2013 U.S. App. LEXIS 17914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Candelario-Del-Moral v. UBS Financial Services Incorpo",
          "cluster_id": 811754,
          "cite": [
            "699 F.3d 93",
            "2012 WL 5458435",
            "2012 U.S. App. LEXIS 23188"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Crow",
          "cluster_id": 4899382,
          "cite": [
            "4 F.4th 982"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wearry v. Cain",
          "cluster_id": 3183098,
          "cite": [
            "577 U.S. 385",
            "136 S. Ct. 1002",
            "194 L. Ed. 2d 78",
            "2016 U.S. LEXIS 1654",
            "84 U.S.L.W. 4125",
            "26 Fla. L. Weekly Fed. S 17",
            "2016 WL 854158"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. United States",
          "cluster_id": 4403802,
          "cite": [
            "582 U.S. 313",
            "2017 U.S. LEXIS 4041",
            "137 S. Ct. 1885",
            "198 L. Ed. 2d 443",
            "26 Fla. L. Weekly Fed. S 700",
            "85 U.S.L.W. 4488",
            "2017 WL 2674152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Barton v. Warden, Southern Ohio Correctional Facility",
          "cluster_id": 2801073,
          "cite": [
            "786 F.3d 450",
            "2015 U.S. App. LEXIS 8020",
            "2015 WL 2262762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bethel (Slip Opinion)",
          "cluster_id": 6453344,
          "cite": [
            "192 N.E.3d 470",
            "167 Ohio St. 3d 362",
            "2022 Ohio 783"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Grissom",
          "cluster_id": 824278,
          "cite": [
            "492 Mich. 296",
            "821 N.W.2d 50",
            "2012 Mich. LEXIS 1231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dolloff",
          "cluster_id": 5146055,
          "cite": [
            "58 A.3d 1032",
            "2012 ME 130",
            "2012 WL 5928662",
            "2012 Me. LEXIS 130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas Lennear v. Eric Wilson",
          "cluster_id": 4655566,
          "cite": [
            "937 F.3d 257"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Pelzer, K.",
          "cluster_id": 2747170,
          "cite": [
            "104 A.3d 267",
            "628 Pa. 193"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miles, Ex Parte Richard Ray Jr.",
          "cluster_id": 2947078,
          "cite": [
            "359 S.W.3d 647",
            "2012 WL 468520",
            "2012 Tex. Crim. App. LEXIS 355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stellato",
          "cluster_id": 2828959,
          "cite": [
            "74 M.J. 473",
            "2015 CAAF LEXIS 725",
            "2015 WL 4991663"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Bies v. Ed Sheldon",
          "cluster_id": 2763624,
          "cite": [
            "775 F.3d 386",
            "2014 FED App. 0302P",
            "2014 WL 7247396",
            "2014 U.S. App. LEXIS 24242"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis Hill v. Betty Mitchell",
          "cluster_id": 4326477,
          "cite": [
            "842 F.3d 910",
            "2016 FED App. 0281P",
            "96 Fed. R. Serv. 3d 131",
            "2016 U.S. App. LEXIS 21458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyjuan Anderson v. City of Rockford, Illinois",
          "cluster_id": 4642953,
          "cite": [
            "932 F.3d 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Angelo McMullan v. Raymond Booker",
          "cluster_id": 2708508,
          "cite": [
            "761 F.3d 662",
            "2014 WL 3823980",
            "2014 U.S. App. LEXIS 14999"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Behenna",
          "cluster_id": 803734,
          "cite": [
            "71 M.J. 228",
            "2012 CAAF LEXIS 736",
            "2012 WL 2684980"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Floyd v. Darrel Vannoy, Warden",
          "cluster_id": 4510860,
          "cite": [
            "894 F.3d 143"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coleman",
          "cluster_id": 867087,
          "cite": [
            "72 M.J. 184",
            "2013 WL 1920736",
            "2013 CAAF LEXIS 500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 799463,
          "cite": [
            "679 F.3d 1183",
            "2012 WL 1592967",
            "2012 U.S. App. LEXIS 9337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie McNeill, Jr. v. Margaret Bagley",
          "cluster_id": 4987267,
          "cite": [
            "10 F.4th 588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darryl Gumm v. Betty Mitchell",
          "cluster_id": 2763627,
          "cite": [
            "775 F.3d 345",
            "2014 FED App. 0301P",
            "2014 WL 7247393",
            "2014 U.S. App. LEXIS 24245"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(620666 OR 9485187 OR 9485188) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 130,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 130,
        "triage_read": 6,
        "triage_snippet_classified": 124
      },
      "lane2_top_cited": {
        "query": "cites:(620666 OR 9485187 OR 9485188)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOCZzPTk0MTQ0NzAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28620666+OR+9485187+OR+9485188%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(620666 OR 9485187 OR 9485188)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 1,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(620666 OR 9485187 OR 9485188)",
    "indexed_citing_opinions": 156,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 620666,
        "count": 105,
        "count_source": "search"
      },
      {
        "opinion_id": 9485187,
        "count": 54,
        "count_source": "search"
      },
      {
        "opinion_id": 9485188,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 418,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-cain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1ODgwNjcmcz05NDU0OTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28620666+OR+9485187+OR+9485188%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 620666,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 145883,
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
    "date_created": "2026-07-05T19:52:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:56:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Cain

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

                       SMITH v. CAIN, WARDEN

        CERTIORARI TO THE CRIMINAL DISTRICT COURT OF 

                LOUISIANA, ORLEANS PARISH


 No. 10–8145. Argued November 8, 2011—Decided January 10, 2012
Petitioner Juan Smith was convicted of first-degree murder based on
  the testimony of a single eyewitness. During state postconviction re-
  lief proceedings, Smith obtained police files containing statements by
  the eyewitness contradicting his testimony. Smith argued that the
  prosecution’s failure to disclose those statements violated Brady v.
  Maryland, 373 U. S. 83. Brady held that due process bars a State
  from withholding evidence that is favorable to the defense and mate-
  rial to the defendant’s guilt or punishment. See id., at 87. The state
  trial court rejected Smith’s Brady claim, and the Louisiana Court of
  Appeal and Louisiana Supreme Court denied review.
Held: Brady requires that Smith’s conviction be reversed. The State
 does not dispute that the eyewitness’s statements were favorable to
 Smith and that those statements were not disclosed to Smith. Under
 Brady, evidence is material if there is a “reasonable probability that,
 had the evidence been disclosed, the result of the proceeding would
 have been different.” Cone v. Bell, 556 U. S. 449, 469–470. A “rea-
 sonable probability” means that the likelihood of a different result is
 great enough to “undermine[ ] confidence in the outcome of the trial.”
 Kyles v. Whitley, 514 U. S. 419, 434. Evidence impeaching an eye-
 witness’s testimony may not be material if the State’s other evidence
 is strong enough to sustain confidence in the verdict. United States v.
 Agurs, 427 U. S. 97, 112–113, and n. 21. Here, however, the eyewit-
 ness’s testimony was the only evidence linking Smith to the crime,
 and the eyewitness’s undisclosed statements contradicted his testi-
 mony. The eyewitness’s statements were plainly material, and the
 State’s failure to disclose those statements to the defense thus violat-
 ed Brady. Pp. 2–4.
2                          SMITH v. CAIN

                               Syllabus

Reversed and remanded.

   ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, GINSBURG, BREYER, ALITO, SOTOMAYOR, and KAGAN, JJ.,
joined. THOMAS, J., filed a dissenting opinion.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–8145
                                   _________________


JUAN SMITH, PETITIONER v. BURL CAIN, WARDEN
ON WRIT OF CERTIORARI TO THE ORLEANS PARISH CRIMINAL
             DISTRICT COURT OF LOUISIANA
                               [January 10, 2012]

   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   The State of Louisiana charged petitioner Juan Smith
with killing five people during an armed robbery. At
Smith’s trial a single witness, Larry Boatner, linked Smith
to the crime. Boatner testified that he was socializing at a
friend’s house when Smith and two other gunmen entered
the home, demanded money and drugs, and shortly there-
after began shooting, resulting in the death of five of
Boatner’s friends. In court Boatner identified Smith as
the first gunman to come through the door. He claimed
that he had been face to face with Smith during the initial
moments of the robbery. No other witnesses and no physi-
cal evidence implicated Smith in the crime.
   The jury convicted Smith of five counts of first-degree
murder. The Louisiana Court of Appeal affirmed Smith’s
conviction. State v. Smith, 797 So. 2d 193 (2001). The
Louisiana Supreme Court denied review, as did this
Court. 2001–2416 (La. 9/13/02), 824 So. 2d 1189; 537 U. S.
1201 (2003).
   Smith then sought postconviction relief in the state
courts. As part of his effort, Smith obtained files from the
2                      SMITH v. CAIN

                     Opinion of the Court

police investigation of his case, including those of the lead
investigator, Detective John Ronquillo. Ronquillo’s notes
contain statements by Boatner that conflict with his tes-
timony identifying Smith as a perpetrator. The notes from
the night of the murder state that Boatner “could not . . .
supply a description of the perpetrators other then [sic]
they were black males.” App. 252–253. Ronquillo also
made a handwritten account of a conversation he had with
Boatner five days after the crime, in which Boatner said
he “could not ID anyone because [he] couldn’t see faces”
and “would not know them if [he] saw them.” Id., at 308.
And Ronquillo’s typewritten report of that conversation
states that Boatner told Ronquillo he “could not identify
any of the perpetrators of the murder.” Id., at 259–260.
  Smith requested that his conviction be vacated, arguing,
inter alia, that the prosecution’s failure to disclose Ron-
quillo’s notes violated this Court’s decision in Brady v.
Maryland, 373 U. S. 83 (1963). The state trial court re-
jected Smith’s Brady claim, and the Louisiana Court of
Appeal and Louisiana Supreme Court denied review. We
granted certiorari, 564 U. S. ___ (2011), and now reverse.
  Under Brady, the State violates a defendant’s right to
due process if it withholds evidence that is favorable to the
defense and material to the defendant’s guilt or punish-
ment. See 373 U. S., at 87. The State does not dispute
that Boatner’s statements in Ronquillo’s notes were fa-
vorable to Smith and that those statements were not dis-
closed to him. The sole question before us is thus whether
Boatner’s statements were material to the determination
of Smith’s guilt. We have explained that “evidence is
‘material’ within the meaning of Brady when there is a
reasonable probability that, had the evidence been dis-
closed, the result of the proceeding would have been dif-
ferent.” Cone v. Bell, 556 U. S. 449, 469–470 (2009). A
reasonable probability does not mean that the defendant
“would more likely than not have received a different
                 Cite as: 565 U. S. ____ (2012)            3

                     Opinion of the Court

verdict with the evidence,” only that the likelihood of a
different result is great enough to “undermine[] confidence
in the outcome of the trial.” Kyles v. Whitley, 514 U. S.
419, 434 (1995) (internal quotation marks omitted).
   We have observed that evidence impeaching an eyewit-
ness may not be material if the State’s other evidence is
strong enough to sustain confidence in the verdict. See
United States v. Agurs, 427 U. S. 97, 112–113, and n. 21
(1976). That is not the case here. Boatner’s testimony
was the only evidence linking Smith to the crime. And
Boatner’s undisclosed statements directly contradict his
testimony: Boatner told the jury that he had “[n]o doubt”
that Smith was the gunman he stood “face to face” with on
the night of the crime, but Ronquillo’s notes show Boatner
saying that he “could not ID anyone because [he] couldn’t
see faces” and “would not know them if [he] saw them.”
App. 196, 200, 308. Boatner’s undisclosed statements
were plainly material.
   The State and the dissent advance various reasons why
the jury might have discounted Boatner’s undisclosed
statements. They stress, for example, that Boatner made
other remarks on the night of the murder indicating that
he could identify the first gunman to enter the house, but
not the others. That merely leaves us to speculate about
which of Boatner’s contradictory declarations the jury
would have believed. The State also contends that Boat-
ner’s statements made five days after the crime can be
explained by fear of retaliation. Smith responds that the
record contains no evidence of any such fear. Again, the
State’s argument offers a reason that the jury could have
disbelieved Boatner’s undisclosed statements, but gives us
no confidence that it would have done so.
   The police files that Smith obtained in state postconvic-
tion proceedings contain other evidence that Smith con-
tends is both favorable to him and material to the verdict.
Because we hold that Boatner’s undisclosed statements
4                      SMITH v. CAIN

                     Opinion of the Court

alone suffice to undermine confidence in Smith’s convic-
tion, we have no need to consider his arguments that the
other undisclosed evidence also requires reversal under
Brady.
   The judgment of the Orleans Parish Criminal District
Court of Louisiana is reversed, and the case is remanded
for further proceedings not inconsistent with this opinion.

                                            It is so ordered.
                 Cite as: 565 U. S. ____ (2012)           1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 10–8145
                         _________________


JUAN SMITH, PETITIONER v. BURL CAIN, WARDEN
ON WRIT OF CERTIORARI TO THE ORLEANS PARISH CRIMINAL
             DISTRICT COURT OF LOUISIANA
                      [January 10, 2012]

   JUSTICE THOMAS, dissenting.
   The Court holds that Juan Smith is entitled to a new
murder trial because the State, in violation of Brady v.
Maryland, 373 U. S. 83 (1963), did not disclose that the
eyewitness who identified Smith at trial stated shortly
after the murders that he could not identify any of the
perpetrators. I respectfully dissent. In my view, Smith
has not shown a “reasonable probability” that the jury
would have been persuaded by the undisclosed evidence.
United States v. Bagley, 473 U. S. 667, 682 (1985) (opinion
of Blackmun, J.). That materiality determination must be
made “in the context of the entire record,” United States v.
Agurs, 427 U. S. 97, 112 (1976), and “turns on the cumu-
lative effect of all such evidence suppressed by the gov-
ernment,” Kyles v. Whitley, 514 U. S. 419, 421 (1995).
Applying these principles, I would affirm the judgment
of the Louisiana trial court.
                             I
   The evidence presented at trial showed the following
facts. On March 1, 1995, Larry Boatner and several
friends gathered at Rebe Espadron’s home in New Or-
leans. Boatner and others were drinking and talking in
the kitchen when Boatner heard the loud sound of a car
without a muffler outside. As Boatner opened the kitchen’s
outside door to investigate the noise, armed men pushed
2                         SMITH v. CAIN

                       THOMAS, J., dissenting

their way through the door, demanding drugs and money.
Tr. 153–154 (Dec. 5, 1995). The first man though the door
put a gun in Boatner’s face and pushed him backwards.
Id., at 154–155. The men initially ordered Boatner and
his friends to the floor, but then ordered Boatner to stand
up. At that time, the man who had been the first one
through the door placed his gun under Boatner’s chin. Id.,
at 156–157. When Boatner asked what the men wanted
him to do, the first man struck Boatner on the back of the
head with his gun, knocking Boatner back to the ground.
Id., at 157–158.
   After hearing the commotion, Espadron emerged from a
back bedroom, where she had been when the men entered
the house. As Espadron opened an inside door leading to
the kitchen, a man with a “covering” over his mouth point-
ed his gun at her face and ordered her to the floor. Id., at
70–71. Disregarding his command, Espadron ran back
toward the bedroom, at which point the intruders opened
fire. Id., at 71–72, 159.
   When the shooting was over, four people lay dead. A
fifth person, 17-year-old Shelita Russell, was mortally
wounded and died later at the hospital. Of those original-
ly gathered in the house, the only survivors were Boatner,
who suffered a severe laceration to his head from the first
man’s blow but was otherwise uninjured; Espadron, who
escaped unharmed; and Reginald Harbor, who had re-
mained in a back bedroom during the shooting. The police
also found a man named Phillip Young at the scene.
Young was alive but had suffered a gunshot wound to the
head. Because Boatner, Espadron, and Harbor had never
seen Young before, the police surmised that Young had
been one of the perpetrators.1
——————
  1 Young was indicted along with Smith for the murders, but he was

deemed incompetent to stand trial due to the brain damage he suffered
                    Cite as: 565 U. S. ____ (2012)                  3

                        THOMAS, J., dissenting

   New Orleans police officer Joseph Narcisse was a first
responder to the scene of the shooting. He testified at trial
that he encountered Boatner in the bathroom of Espa-
dron’s home, where Boatner was attempting to care for the
laceration to his head. According to Narcisse, “Mr. Boat-
ner . . . had let inside the perpetrators and did see them.”
Id., at 21 (Dec. 4, 1995). Narcisse further explained that
Boatner “had a description” of the person that he saw, the
details of which Narcisse could not recall. Id., at 32.
   Detective John Ronquillo, the lead investigator of the
shootings, testified that Boatner had described the first
man through the kitchen door as having a “short-type
haircut,” “a lot of golds in his teeth,” and “brown-ski[n].”2
Id., at 115 (Dec. 5, 1995). Ronquillo further testified that
Boatner could describe no other perpetrator, but that
Boatner had viewed the first man twice: once when the
man initially came through the door and again when
Boatner was ordered to stand up and the man held a gun
to his chin. Id., at 117–118.
   Ronquillo also testified that, during the four months
following the shootings, Boatner viewed 14 six-person
photograph arrays of potential suspects—only one of
which contained a picture of Smith. Id., at 89–100. Three
weeks after the crime, Ronquillo presented Boatner with
one of the arrays that did not include a picture of Smith.
Ronquillo recalled that Boatner noted that one man in the
array had a “similar haircut” and “a similar expression on
his face” as the “gentleman that came into the house
initially with the gun that [Boatner] confronted,” but that

——————
as a result of being shot. 1 Record 49.
  2 “Golds” are permanent or removable mouth jewelry, also referred to

as “grills.” See Mouth Jewelry Wearers Love Gleam of the Grill, South
Florida Sun-Sentinel, Feb. 4, 2007, p. 5, 2007 WLNR 2187080. See also
A. Westbrook, Hip Hoptionary 59 (2002) (defining a “grill” as a “teeth
cover, usually made of gold and diamonds”).
4                       SMITH v. CAIN

                     THOMAS, J., dissenting

Boatner “was positive this wasn’t the individual.” Id., at
97; see also 5 Record 828. A few months later, Ronquillo
presented Boatner with the array that included a photo-
graph of Smith. Tr. 99–101 (Dec. 5, 1995). Ronquillo
testified that Boatner identified Smith “immediately,”
stating, “ ‘This is it. I’ll never forget that face.’ ” Id., at
100. Of the 84 photographs that Boatner viewed, Smith’s
photograph was the only one that Boatner identified.
   Boatner identified Smith again when he was called to
the stand during Smith’s trial. Boatner testified that
Smith’s face was the “[s]ame face,” id., at 174, and that
Smith’s mouth was the “[s]ame mouth” “full of gold,” ibid.,
as that of the first man who came through the kitchen
door on the night of the attack. Boatner also testified that
Smith’s hair at trial was “shaved on the sides” as it was
during the crime, but that “the top was a little bit lower”
at the time of the murders. Id., at 165. Boatner explain-
ed that, during the attack, he had focused on the first
man through the door—who was unmasked—but that he
“didn’t notice” the faces of any of the other assailants or
whether they were masked. Id., at 154. On cross-
examination, Boatner testified that he had described the
first man’s build, haircut, and gold teeth jewelry to the
police. Id., at 178.
   Based on this evidence, the jury convicted Smith of first-
degree murder. Following the conclusion of direct review,
Smith petitioned the trial court for postconviction relief.
Smith argued that the State had failed to disclose various
police notes revealing favorable evidence material to
Smith’s guilt. As relevant here, those items include pre-
trial statements by Boatner; statements by victim Shelita
Russell and Espadron’s neighbor, Dale Mims; a pretrial
statement by firearms examiner Kenneth Leary; state-
ments by cosuspect Robert Trackling and Trackling’s
fellow inmate, Eric Rogers; and a statement by cosuspect
Phillip Young. After holding a 4-day evidentiary hearing,
                 Cite as: 565 U. S. ____ (2012)           5

                    THOMAS, J., dissenting

the postconviction judge—who had also presided over
Smith’s 2-day trial—denied Smith’s Brady claims.
  Like the postconviction court below, I conclude that
Smith is not entitled to a new trial under Brady. In my
view, Smith has not established a reasonable probability
that the cumulative effect of this evidence would have
caused the jury to change its verdict.
                             II

                             A

  Smith first identifies two undisclosed statements by
Boatner, which the Court concludes are “plainly material.”
Ante, at 3. First, a note by Ronquillo, documenting a
conversation he had with Boatner at the scene, states that
Boatner “could not . . . supply a description of the perpe-
trators other th[a]n they were black males.” 5 Record 809.
Second, a handwritten note by Ronquillo, documenting a
phone conversation he had with Boatner on March 6, five
days after the murders, states that “Boatner . . . could not
ID anyone because couldn’t see faces . . . glanced at 1st
one—saw man—through door—can’t tell if had—faces
covered didn’t see anyone . . . Could not ID—would not
know them if—I saw them.” 13 id., at 2515. Ronquillo’s
typed summary of this note states that Boatner advised
him that he “could not identify any perpetrators of the
murder.” 5 id., at 817.
  Smith is correct that these undisclosed statements could
have been used to impeach Boatner and Ronquillo during
cross-examination. But the statements are not material
for purposes of Brady because they cannot “reasonably be
taken to put the whole case in such a different light as to
undermine confidence in the verdict.” Kyles, 514 U. S., at
435. When weighed against the substantial evidence that
Boatner had opportunities to view the first perpetrator,
offered consistent descriptions of him on multiple occa-
sions, and even identified him as Smith, the undisclosed
6                            SMITH v. CAIN

                         THOMAS, J., dissenting

statements do not warrant a new trial.
  The evidence showed that, notwithstanding Ronquillo’s
on-scene note, Boatner offered a description of the perpe-
trator at the scene. Officer Narcisse testified that Boatner
provided him with a description of the perpetrator that
Boatner saw. Narcisse’s testimony thus corroborated
Boatner’s trial testimony that he saw the first man and
described him to police.3 Narcisse’s testimony also miti-
gated the impeachment value of Ronquillo’s on-scene note
by indicating that, although Boatner may have provided
no detailed description to Ronquillo at the scene, Boatner
had described the first man to another officer.4
  In any event, Ronquillo’s notes reflect that Boatner
provided a description of the first perpetrator at the police
station only a few hours after the shootings occurred. Tr.
403 (Jan. 22, 2009). Boatner was asked if he could “de-
scribe the subjects wh[o] shot the people in the house.” 5
Record 866. He responded: “I can tell you about one, the
one who put the pistol in my face, he was a black male
with a low cut, gold[s] in his mouth . . . about my complex-
ion, brown skinned.” Ibid. When asked, “[Y]ou say you


——————
    3 Ina pretrial hearing, Boatner testified that he “gave a description
to the officer that came to the scene.” Tr. 24 (Oct. 27, 1995). Boatner
responded negatively when asked whether this officer was Detective
Ronquillo. Ibid. Boatner further testified that he told the officer that
the first man through the door was “heavy built with his hair with a
fade, with a little small top with a lot of gold teeth in his mouth.” Ibid.
That testimony was consistent with the testimony that Boatner and
Officer Narcisse gave at trial.
  4 Moreover, Boatner’s reticence toward Ronquillo at the scene of the

crime was entirely understandable. As Ronquillo noted at the postcon-
viction hearing, “there were dead bodies everywhere,” and Boatner was
“a little shook up.” Id., at 402–403 (Jan. 22, 2009). Similarly, Narcisse
testified at trial that Boatner, while “not as frantic” as Espadron, was a
“bit emotional” when Narcisse encountered him at the scene. Id., at 34
(Dec. 4, 1995).
                 Cite as: 565 U. S. ____ (2012)            7

                    THOMAS, J., dissenting

can’t describe any of the other shooters besides the one
who put the gun in your face after you opened the door,”
Boatner replied, “No, I can’t.” Ibid. In his brief, Smith
cites this station house statement as an example of favor-
able, undisclosed evidence. But this statement actually
corroborates Boatner’s trial testimony that he saw and
described the first perpetrator to police and that he did not
get a good look at the other assailants. Moreover, the
description Boatner provided was consistent with Smith’s
appearance. The Court completely ignores Boatner’s
station house statement, but our cases instruct us to
evaluate “the net effect of the evidence withheld by the
State” in assessing materiality. See Kyles, supra, at 421–
422.
   The evidence not only shows that Boatner described the
first perpetrator twice in the immediate aftermath of the
crime, but also that Boatner described him again three
weeks later when he viewed a photograph array and elim-
inated a similar-looking individual. The evidence before
the jury further indicated that, several months after the
crime, Boatner confidently identified Smith in an array,
after evincing a discriminating, careful eye over a 4-month
investigative period. What is more, the reliability of
Boatner’s out-of-court identification was extensively tested
during cross-examination at Smith’s trial. In particular,
Boatner was asked whether the fact that he saw Smith’s
picture in a newspaper article naming Smith as a suspect
had tainted his identification. Boatner did not waiver,
responding, “I picked out the person I seen come in that
house that held a gun to my head and under my chin and
the person that was there when all my friends died.” Tr.
190 (Dec. 5, 1995). That Boatner credibly rejected defense
counsel’s “suggestion” theory is supported by the fact that
Boatner did not identify cosuspect Robert Trackling—
whose photograph was included in a separate array shown
to Boatner on the same day that Boatner identified
8                      SMITH v. CAIN

                    THOMAS, J., dissenting

Smith—even though Trackling’s picture was next to
Smith’s in the same newspaper article. 5 Record 833, 835.
   When weighed against Boatner’s repeated and con-
sistent descriptions and confident out-of-court and in-court
identifications, Boatner’s March 6 statement is also imma-
terial. As an initial matter, Ronquillo’s note of his March
6 conversation with Boatner contains an internal contra-
diction that undercuts its impeachment value. Although
the note states that Boatner “didn’t see anyone,” it also
states that Boatner “glanced at 1st one—saw man—
through door.” 13 id., at 2515. The latter part is con-
sistent with Boatner’s repeated statements that he only
saw the first man through the door. Moreover, the jury
would have evaluated any equivocation in Boatner’s
statement in light of the fact that he made it a mere five
days after a traumatic shooting, when the perpetrators
were still at large. The jury would have considered Boat-
ner’s trial testimony that, following the murders of his
friends, he began having nightmares, had difficulty sleep-
ing, quit his job, and began drinking heavily—so much so
that he checked into a hospital for substance abuse treat-
ment and grief counseling. Tr. 162–163, 170–171, 182
(Dec. 5, 1995). Any impeachment value in the March 6
note would have been further mitigated by the fact that,
as Ronquillo explained, “on the night of the incident
[Boatner] said that he could [identify someone] and he
gave a description that was very close to Mr. Smith’s
description.” Id., at 401 (Jan. 22, 2009). And, following
his March 6 conversation with Ronquillo, Boatner viewed
numerous photograph arrays, described the first perpetra-
tor, and ultimately identified him as Smith.
   Of course, had the jury been presented with Ronquillo’s
notes of Boatner’s on-scene and March 6 statements, it
might have believed that Boatner could not identify any of
the perpetrators, but a possibility of a different verdict is
insufficient to establish a Brady violation. See Strickler v.
                  Cite as: 565 U. S. ____ (2012)            9

                     THOMAS, J., dissenting

Greene, 527 U. S. 263, 291 (1999); see also Agurs, 427
U. S., at 109–110 (“The mere possibility that an item of
undisclosed information might have helped the defense, or
might have affected the outcome of the trial, does not es-
tablish ‘materiality’ in the constitutional sense.” Rather,
a “petitioner’s burden is to establish a reasonable prob-
ability of a different result.” Strickler, supra, at 291.
  Instead of requiring Smith to show a reasonable proba-
bility that Boatner’s undisclosed statements would have
caused the jury to acquit, the Court improperly requires
the State to show that the jury would have given Boatner’s
undisclosed statements no weight. See ante, at 3 (“[T]he
State’s argument offers a reason that the jury could have
disbelieved Boatner’s undisclosed statements, but gives us
no confidence that it would have done so”). But Smith
is not entitled to a new trial simply because the jury
could have accorded some weight to Boatner’s undisclosed
statements. Smith’s burden is to show a reasonable prob-
ability that the jury would have accorded those statements
sufficient weight to alter its verdict. In light of the record
as a whole—which the Court declines to consider—Smith
has not carried that burden.
                             B
   Smith also argues that statements by Shelita Russell
and Dale Mims documented in Ronquillo’s handwritten
notes could have been used to impeach Boatner’s identifi-
cation of Smith because the statements indicate that
the perpetrators were masked. One undated note, which
contains several entries about various aspects of the inves-
tigation, states, “female—face down against cabinets—
conscious.” On the next line, the note continues, “said—in
kitchen saw people barge in—one—black cloth across
face—first one through door—[no further statement].” 13
Record 2556. When cross-examined during the postconvic-
tion hearing about whether this note documented the
10                          SMITH v. CAIN

                         THOMAS, J., dissenting

statement of Russell, Ronquillo confirmed that the note
was in his handwriting, but he testified that he never
talked to Russell, that he did not know when the note was
made, and that someone else could have relayed the in-
formation to him. Tr. 415–418 (Jan. 22, 2009).5 I will
assume arguendo that, had this note been disclosed, it
would have been admissible at Smith’s trial as a dying
declaration of Russell.6 But the note would have had
minimal impeachment value because, contrary to Smith’s
assertions, it is ambiguous in light of the context in which
the statement was made. Officer Narcisse testified that
Russell was conscious and able to talk, but that she was in
“bad condition.” Id., at 20 (Dec. 4, 1995). Similarly, Reg-
inald Harbor testified that, as Russell lay wounded, she
was “whining” and he “didn’t catch nothing [t]hat she
said.” Id., at 205 (Dec. 5, 1995). And, although Smith
contends that the note says “exactly” that the “first person
through the door had a black cloth across his face,” that
is not how the note reads. Reply Brief for Petitioner 11
(emphasis deleted; internal quotation marks omitted)
(hereinafter Reply Brief). The note first states that the
declarant “saw people barge in,” then states “one—black


——————
   5 Russell did not make this statement to Officer Narcisse. He testi-

fied that Russell “was not able to give us any information or any details
of what had happened.” Id., at 20.
   6 Louisiana law provides that “[a] statement made by a declarant

while believing that his death was imminent, concerning the cause or
circumstances of what he believed to be his impending death[,]” is “not
excluded by the hearsay rule if the declarant is unavailable as a wit-
ness.” La. Code Evid. Ann., Art. 804(B)(2) (West Supp. 2012). Assum-
ing this statement was actually Russell’s, it likely qualifies as a dying
declaration. At trial, Boatner testified that, in the aftermath of the
shooting, Russell told him, “Feel like I’m about to die.” Tr. 161 (Dec. 5,
1995) (internal quotation marks omitted). Espadron also testified that
Russell told her, “I’m gonna die,” and, “Don’t let me die.” Id., at 73–74
(internal quotation marks omitted).
                     Cite as: 565 U. S. ____ (2012)                  11

                        THOMAS, J., dissenting

cloth across face—first one through door—[no further
statement].” 13 Record 2556 (emphasis added). It is at
least as logical to read this statement as indicating only
that “one” of the “people” had a “black cloth across [his]
face.” Russell, suffering from fatal wounds, said nothing
further after “first one through door,” and it is impossible
to know whether the “first one” was also the “one” with a
“black cloth across [his] face.”
  The second statement Smith identifies is that of Dale
Mims, who lived down the street from Espadron’s home
and who heard the shooting. A note by Ronquillo states
that Mims saw four males fleeing Espadron’s home, “all
wearing mask[s].” Id., at 2518. Like Russell’s purported
statement, this statement has minimal impeachment
value in light of the record. Mims’ undisclosed statement
does not address whether some or all of the perpetrators
were masked inside Espadron’s home.7 Moreover, had
Mims been called as a witness at trial, he presumably
would have testified, as he did at the postconviction hear-
ing, that he was “positive” that he only saw three perpe-
trators fleeing, and that, of those three, only two were
masked. Tr. 269, 271–273, 275 (Jan. 13, 2009).
  Both Russell’s purported statement and Mims’ testimo-
ny are consistent with Boatner’s testimony that he did not
know whether any of the other perpetrators were masked,
id., at 154 (Dec. 5, 1995), and with Officer Narcisse’s and
Espadron’s testimony that the single perpetrator whom
Espadron observed was wearing some sort of face cover-

——————
  7 Smith ridicules the “exceedingly peculiar” notion that the perpetra-

tors would have remained unmasked inside Espadron’s home, only to
mask themselves before leaving the scene. Reply Brief 12–13. But that
notion is eminently reasonable if the perpetrators intended to massacre
the witnesses who were inside the home—as they did—and were
concerned only with disguising themselves from neighbors outside who
might see or hear the burglary.
12                     SMITH v. CAIN

                    THOMAS, J., dissenting

ing, id., at 30–31 (Dec. 4, 1995); id., at 71 (Dec. 5, 1995).
Thus, the totality of the evidence indicates that some, but
not all, of the perpetrators were masked, a conclusion that
in no way undermines Boatner’s consistent assertions that
the only perpetrator he saw was unmasked.
                             C
   Smith also contends that Ronquillo’s undisclosed note
documenting a pretrial statement by firearms examiner
Kenneth Leary is material for purposes of Brady. The
note states that “Leary advised Ronquillo that the 9MM
ammunition confiscated from [the scene of the murders]
was typed to have been fired from a[n] [Intratec], ‘Mac[-]
11’ model type, semi automatic weapon.” 5 Record 831.
According to Smith, this statement conflicts with Leary’s
trial testimony that the 9-millimeter ammunition found
at the scene “was fired by one particular weapon, one 9-
millimeter handgun,” Tr. 132 (Dec. 5, 1995), because an
Intratec or Mac-11 pistol is not a “handgun.” Smith fur-
ther argues that Leary’s pretrial statement could have
been used to exculpate Smith, whose guilt the prosecution
attempted to show by calling a pathologist to testify that
Shelita Russell’s wounds could have been inflicted by a
9-millimeter “handgun,” id., at 39 (Dec. 4, 1995), and by
calling Boatner to testify that the gun Smith held under
his chin was a 9-millimeter silver “hand gun,” id., at 157
(Dec. 5, 1995).
   Contrary to Smith’s contentions, Leary’s pretrial state-
ment does not undermine the evidence presented at trial.
Leary’s pretrial statement is consistent with his and
Boatner’s trial testimony because an Intratec or Mac-11
pistol is a 9-millimeter handgun. Smith concedes that
such a weapon uses 9-millimeter cartridges. Brief for
Petitioner 48. Moreover, a “handgun” is simply “[a] fire-
arm that can be used with one hand,” American Heritage
Dictionary 819 (3d ed. 1992), and no one disputes that an
                     Cite as: 565 U. S. ____ (2012)                   13

                         THOMAS, J., dissenting

Intratec or Mac-11 pistol can be used with one hand.
Smith nonetheless insists that, “as a colloquial matter,
machine pistols of the Intratec or MAC-11 type would be
considered automatic or semiautomatic weapons, rather
than handguns.” Reply Brief 18. But even assuming that
Smith is correct, he fails to explain why Leary, a firearms
expert, would have been expected to use colloquial rather
than technical terminology.8
  The record also makes clear that, when Boatner used
the term “handgun,” he did not understand it to exclude
automatic or semiautomatic machine pistols. In the im-
mediate aftermath of the murders, as well as at trial,
Boatner stated that a second perpetrator carried a “Ma[c]
10” or “Tech Nine” “Uzi” type weapon, Tr. 159, 179 (Dec. 5,
1995); 5 Record 809, 813, 866, and Boatner described that
weapon as a “handgun,” id., at 809. Moreover, Boatner’s
pretrial description of the silver or chrome “handgun” that
the first man held was consistent with Leary’s undisclosed
statement that the gun that fired the 9-millimeter ammu-
nition found at the scene was a semiautomatic weapon. In
his station house statement, Boatner described the first
man’s weapon as a “big,” “automatic pistol.” Id., at 813,
866. Because Leary’s pretrial statement is neither im-
peaching nor exculpatory, Leary’s undisclosed statement
cannot form the basis of a Brady violation. See Strickler,

——————
  8 Smith argues that Leary himself considered an “[Intratec] or ‘Mac[-]
11’ ” model type to be different from a 9-millimeter handgun. Smith
relies on the fact that Leary’s pretrial statement indicated that the
ammunition recovered from the scene did not come from the handgun
recovered from Donielle Bannister, another suspect in the murders.
Id., at 18. Leary’s pretrial statement did not describe the handgun
recovered from Bannister as a 9-millimeter, contrary to Smith’s repre-
sentation. More importantly, Leary’s statement suggests only that
Bannister’s handgun did not fire the 9-millimeter ammunition found at
the scene, not that Leary did not consider an “[Intratec] or ‘Mac[-]11’ ”
model type to be a handgun.
14                     SMITH v. CAIN

                    THOMAS, J., dissenting

527 U. S., at 281–282 (To make out a Brady viola-
tion, “[t]he evidence at issue must be favorable to the
accused, either because it is exculpatory, or because it is
impeaching”).
                              D
   Smith next points to purportedly exculpatory and ma-
terial undisclosed pretrial statements made by Robert
Trackling, a member of the “Cut Throat Posse” street gang
with which Smith was allegedly associated, and by Eric
Rogers, an inmate who was incarcerated with Trackling.
5 Record 845. Police notes reflect that Eric Rogers gave an
interview to investigators on May 19, 1995, during which
he described a conversation that he had with Trackling
while in prison. During that conversation, Trackling
described the murders at Espadron’s home and stated that
he had committed the crime along with “Fat, Buckle, and
a guy they call uh, Short Dog.” Id., at 841. According to
Rogers, Fat’s real name was “Darnell [Donielle] Banister,”
Buckle’s real name was “Contez [Kintad] Phillips,” and
Short Dog’s real name was “Juan.” Id., at 843–844.
   Smith contends that Rogers’ interview was exculpatory
in two respects. First, he points to the following comment
by Rogers later during the interview: “They call Contez
Philip Buckle, they call Darnell Banister Fat, Short Dog
that’s what they call him, they call Robert Home.” Id., at
845. Smith suggests that Rogers’ prior identification of
“Short Dog” as “Juan [Smith]” was equivocal in light of his
later statement that “Short Dog” was a man named “Rob-
ert Home.” Reply Brief 21. Second, Smith asserts that
disclosure of Rogers’ interview would have led the defense
and the jury to learn of Rogers’ allegation—made for the
first time 10 years after Smith’s trial—that the police had
asked him to implicate Juan Smith as “Short Dog,” Tr.
284–285 (Jan. 13, 2009).
   Neither argument is persuasive. If the jury had learned
                    Cite as: 565 U. S. ____ (2012)                  15

                        THOMAS, J., dissenting

of Rogers’ statement, it would have heard information
directly inculpating Smith as “Short Dog,” a perpetrator of
the shootings. Rogers’ physical description of “Short
Dog”—“he[’s] short[,] he[’s] got golds going across his
mouth[,] and . . . he’s like built,” 5 Record 844–also corrob-
orated Boatner’s description of the first man through the
door as having a “mouth full of gold” and a “heavy” build.
Furthermore, Smith ignores other inculpatory information
documented in Ronquillo’s notes of Rogers’ statement.
Those notes reflect Trackling’s own interview with police
on June 1, 1995, in which Trackling identified Phillips,
Bannister, and “Juan Smith” as the perpetrators of the
murders at Espadron’s home. Id., at 832; see also id., at
854–855. Trackling’s statement only strengthens the
inculpatory nature of Rogers’ interview.
  Further, the jury assuredly would not have believed
Smith’s suggestion that Rogers identified “Short Dog” as a
man named “Robert Home.” When this statement is taken
in context, it appears that Rogers was describing the
nickname—“Home”9—of Robert Trackling, the “Robert”
whom Rogers had repeatedly referenced throughout his
interview. See id., at 839–850. Indeed, Rogers’ phrase-
ology, “they call Robert Home,” was consistent with his pre-
vious comments that “[t]hey call Contez Philip Buckle,”
and “they call Darnell Banister Fat.” Id., at 845 (emphasis
added). Unsurprisingly, in the thousands of pages of


——————
   9 See 2 Dictionary of American Regional English 1064–1065, 1069 (F.

Cassidy & J. Hall eds. 1991) (defining “Home” as “a term of address
used by two black people either from the same Southern state or simply
from the South,” similar to “homey” or “home boy”); 2 Green’s Diction-
ary of Slang 828 (2010) (defining “home,” an abbreviation of homeboy,
as “a friend, often used in direct address”); Concise New Partridge
Dictionary of Slang and Unconventional English (T. Dalzell & T. Victor
eds. 2008) (defining “home” as “a very close male friend,” an abbrevia-
tion of “Homeboy”).
16                          SMITH v. CAIN

                         THOMAS, J., dissenting

record material, I have not found, nor have the parties
cited, a single reference to anyone named “Robert Home.”
   If the jury had heard Rogers’ postconviction testimony
that police asked him to implicate Smith and that Track-
ling’s description of the murders did not include Smith, Tr.
284–285 (Jan. 13, 2009), it would have weighed Rogers’
allegation against Trackling’s own statement to the police
that Smith had participated in the murders at Espadron’s
home, 5 Record 832. The prosecution also would have
called Smith’s sister, Trinieze Smith, to testify that she
believed her brother was known as “Short Dog,” as she did
at the postconviction hearing. Tr. 371 (Jan. 14, 2009). On
this record, the undisclosed statements by Rogers and
Trackling actually strengthen rather than weaken confi-
dence in the jury’s guilty verdict.10
                            E
  Finally, Smith argues that an undisclosed handwritten
note by Ronquillo documenting a statement by Phillip
Young—the man found injured at the scene and suspected
of having participated in the crime—is also material evi-
dence warranting a new trial. At trial, Ronquillo testified
that he met with Young while Young was hospitalized as a
result of permanent brain damage suffered in the shoot-


——————
  10 Detective Byron Adams, who took Rogers’ statement, did not testify

at the postconviction hearing because he had died in the meantime. He
thus had no opportunity to address Rogers’ recantation or his newly
minted allegation that Detective Adams asked Rogers to implicate
Smith. Smith argues that “there is no reason to believe that . . . Adams
would have contradicted Rogers—much less that the jury would have
believed [him] if [he] did.” Reply Brief 21. But Smith offers no support
for his dubious assertion that Detective Adams would have admitted to
framing Smith, or that, had the detective denied the allegation, the jury
would have believed Rogers—a convicted murderer who never ex-
plained any motive Adams would have had to frame Smith—over the
detective.
                 Cite as: 565 U. S. ____ (2012)          17

                    THOMAS, J., dissenting

ings. Id., at 102 (Dec. 5, 1995). According to Ronquillo,
Young “was strapped to a chair. He really couldn’t talk,
[h]e mumbled. He could use his left hand, that was all.
He couldn’t walk or anything. He was fed through a tube
by the people there. He was in really bad shape.” Id., at
102–103. When asked whether Young was able to com-
municate with him “at all,” Ronquillo responded, “No. I
couldn’t understand anything that he was saying.” Id., at
103.
  The undisclosed note from Ronquillo’s meeting with
Young reads as follows: “Short Dog/Bucko/Fats—No—
Didn’t shoot me—No—Not with me when went to house—
Yes—one of people in house shot me—No—Not responsi-
ble—‘Posse’—Didn’t drive to house—‘Posse’—Yes—Knows
names of perps—Yes—Drove in car—Yes—girlfriend’s
car.” 13 Record 2568. Smith contends that this note is
exculpatory in that it suggests that he was “not involved”
in the shootings. Brief for Petitioner 43.
  Young’s statement is only exculpatory if Smith concedes
(as the statement asserts) that he is, in fact, “Short Dog”
and a member of the “Cut Throat Posse.” Such a conces-
sion would only have strengthened the inculpatory value
of the statements by Rogers and Trackling indicating that
Smith was the “Short Dog” who committed the murders at
Espadron’s home. In any event, the exculpatory value of
the note is minimal for several other reasons. First, it is
unclear whether Ronquillo’s note reflects a statement by
Young that the “Posse” was not responsible for shooting
the victims or a statement that the “Posse” was not re-
sponsible for shooting Young. Further, the statement that
“Short Dog” and others were not with Young when he went
to the house is certainly not a clear statement that “Short
Dog” did not commit the murders, especially in light of
evidence in the record that the assailants used two cars on
18                         SMITH v. CAIN

                        THOMAS, J., dissenting

the night of the murders.11 Second, had the jury learned
of Ronquillo’s note, it would have presumably heard Ron-
quillo testify, as he did at the postconviction hearing, that
he was not even sure whether his note actually reflected
statements by Young, given that Young “couldn’t talk,”
was “jumbled,” could only “kind of move his head,” and
sometimes would just sit and stare when Ronquillo asked
a question.12 Tr. 423–424 (Jan. 22, 2009). Accordingly,
Ronquillo explained, “I never had hide nor hair actually of
what [Young] said.” Id., at 423.
   The jury thus would have evaluated Ronquillo’s note, of
unclear exculpatory value on its face, against a backdrop
of doubt as to what, if anything, Young actually communi-
cated. The jury also would have weighed this evidence
against the strongly inculpatory nature of Boatner’s de-
scriptions and identifications and Rogers’ and Trackling’s
statements, which corroborated Boatner’s identification.
When all of the evidence is considered cumulatively, as it
must be, Smith has not shown a reasonable probability
that the jury would have reached a different verdict.



——————
  11 In his station house statement, Boatner explained that the loud car
that arrived at Espadron’s home was white. 5 Record 866. In Rogers’
interview with the police, Rogers said that Trackling escaped from
Espadron’s home in a burgundy car. Id., at 842.
   12 Smith also contends that the defense could have used the undis-

closed note to impeach Ronquillo’s trial testimony that Young was not
able to communicate with him “at all.” That argument lacks merit.
Ronquillo’s trial testimony, when read in context, does not suggest that
no communication occurred. Rather, Ronquillo made clear that he
simply “couldn’t understand anything that [Young] was saying.” See Tr.
103 (Dec. 5, 1995) (emphasis added). That testimony is consistent with
the garbled nature of the note, and the note thus would have had little,
if any, impeachment value.
                 Cite as: 565 U. S. ____ (2012)          19

                    THOMAS, J., dissenting

                        *      *    *
   The question presented here is not whether a prudent
prosecutor should have disclosed the information that
Smith identifies. Rather, the question is whether the cu-
mulative effect of the disclosed and undisclosed evidence
in Smith’s case “put[s] the whole case in such a different
light as to undermine confidence in the verdict.” Kyles,
514 U. S., at 435. When, as in this case, the Court departs
from its usual practice of declining to review alleged mis-
applications of settled law to particular facts, id., at 456
(SCALIA, J., joined by Rehnquist, C. J., and KENNEDY and
THOMAS, JJ., dissenting), the Court should at least consid-
er all of the facts. And, the Court certainly should not
decline to review all of the facts on the assumption that
the remainder of the record would only further support
Smith’s claims, as the Court appears to have done here.
Ante, at 3–4.
   Such an assumption is incorrect. Here, much of the
record evidence confirms that, from the night of the mur-
ders through trial, Boatner consistently described—with
one understandable exception—the first perpetrator
through the door, that Boatner’s description matched
Smith, and that Boatner made strong out-of-court and in-
court identifications implicating Smith. Some of the un-
disclosed evidence cited by Smith is not favorable to him
at all, either because it is of no impeachment or exculpa-
tory value or because it actually inculpates him. Because
what remains is evidence of such minimal impeachment
and exculpatory value as to be immaterial in light of the
whole record, I must dissent from the Court’s holding that
the State violated Brady.

```

---

## GROUP: content/cases/Smith v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: "Smith v. Illinois"
type: case
citation: "469 U.S. 91 (1984)"
parallel_cite: "105 S. Ct. 490; 83 L. Ed. 2d 488; 53 U.S.L.W. 3430"
neutral_cite: 1984 U.S. LEXIS 167
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-12-10
docket: 84-5332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Illinois
  varies_by_point: false
  scope_note: "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111288/smith-v-illinois/"
  cluster_id: 111288
  opinion_id: 9429796
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Davis v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel"]
holding: "Once an accused unambiguously requests counsel, his postrequest responses to continued interrogation may not be used to cast retrospective doubt on the clarity of that invocation; such later statements bear only on the distinct question of waiver."
lake:
  record_id: Smith v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Illinois

*469 U.S. 91 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During custodial interrogation Smith was advised of his [[Miranda and Custodial Interrogation|Miranda rights]]. When told he had the right to a lawyer, Smith responded, "Uh, yeah. I'd like to do that." Rather than stopping, the officers finished the warnings and continued questioning; Smith then made some equivocal remarks and ultimately confessed. The Illinois courts used Smith's later equivocal statements to conclude that his initial request for counsel had not been a clear invocation.

## Issue
Whether an accused's responses to *continued* interrogation, given after he has requested counsel, may be used to determine that the initial request for counsel was ambiguous.

## Rule
No. Under *[[Edwards v. Arizona]]*, once an accused invokes the right to counsel all interrogation must cease until counsel is provided or the accused himself reinitiates and validly waives. The clarity of an invocation is judged on the request and the circumstances leading up to it — not on what the suspect says afterward in response to officers who improperly kept questioning.

"We hold only that, under the clear logical force of settled precedent, an accused's *postrequest* responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself. Such subsequent statements are relevant only to the distinct question of waiver." — 469 U.S. at 100. ^pin-100

## Application
Smith's statement — "Uh, yeah. I'd like to do that" — was, in context, a request for counsel, and questioning should have stopped. The state courts erred by mining his *later* equivocal answers (made only because interrogation wrongly continued) to recharacterize the initial request as ambiguous. Those later answers could bear only on whether Smith waived a right he had already invoked, not on whether he invoked it.

## Conclusion
Postrequest responses cannot be used to make an otherwise clear invocation ambiguous. The judgment of the Illinois Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. (The Court expressly left open how to treat a request that is ambiguous from the outset — later answered in *Davis v. United States*.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Smith*'s narrow holding stands. The threshold question it reserved — what counts as an unambiguous invocation, and whether officers must clarify an ambiguous one — was decided by [[Davis v. United States]] (no duty to clarify; the request must itself be unambiguous).

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Smith v. Illinois*, 469 U.S. 91 (1984) (per curiam) — https://www.courtlistener.com/opinion/111288/smith-v-illinois/ — pinpoint: 100.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "551a14f846e1fec1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "469 U.S. 91 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 167", "official_citation_present": true, "parallel_cite": "105 S. Ct. 490; 83 L. Ed. 2d 488; 53 U.S.L.W. 3430", "title": "Smith v. Illinois", "year": "1984"}}
{"assertion_id": "39af754f19ebfebb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Once an accused unambiguously requests counsel, his postrequest responses to continued interrogation may not be used to cast retrospective doubt on the clarity of that invocation; such later statements bear only on the distinct question of waiver.", "title": "Smith v. Illinois"}}
{"assertion_id": "56aa895afb7a310b", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Smith v. Illinois"}}
{"assertion_id": "3e9647ad40ebd2d1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-12-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Smith v. Illinois", "field_i_validity": "good_law", "scope_note": "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994).", "title": "Smith v. Illinois", "varies_by_point": "false"}}
{"assertion_id": "c023cf61a629f241", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Smith v. Illinois"}}
```

### lake record — Smith v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Illinois",
    "case_name_short": "",
    "case_name_full": "Smith v. Illinois",
    "input_case_name": "Smith v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-12-10",
    "year": 1984,
    "docket": "84-5332",
    "cluster_id": 111288,
    "lead_opinion_id": 9429796,
    "sibling_ids": [
      111288,
      9429796,
      9429797
    ],
    "absolute_url": "/opinion/111288/smith-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 91",
      "volume": "469",
      "reporter": "U.S.",
      "page": "91",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 490",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 488",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 3430",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "3430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 167",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 91",
        "volume": "469",
        "reporter": "U.S.",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 490",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 488",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 167",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 3430",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "3430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 91",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 91",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-100",
      "page": null,
      "quote": "Rather than stopping, the officers finished the warnings and continued questioning; Smith then made some equivocal remarks and ultimately confessed. The Illinois courts used Smith's later equivocal statements to conclude that his initial request for counsel had not been a clear invocation. ## Issue Whether an accused's responses to *continued* interrogation, given after he has requested counsel, may be used to determine that the initial request for counsel was ambiguous. ## Rule No. Under *Edwards v. Arizona*, once an accused invokes the right to counsel all interrogation must cease until counsel is provided or the accused himself reinitiates and validly waives. The clarity of an invocation is judged on the request and the circumstances leading up to it \u2014 not on what the suspect says afterward in response to officers who improperly kept questioning.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Illinois",
    "varies_by_point": false,
    "scope_note": "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tellez-Suarez",
          "cluster_id": 10134379,
          "cite": [
            "312 Or. App. 531",
            "493 P.3d 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kevin Jones, Jr. v. K. Harrington",
          "cluster_id": 4240929,
          "cite": [
            "829 F.3d 1128",
            "2015 U.S. App. LEXIS 23120",
            "2016 WL 3947820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Francisco Garcia v. David Long",
          "cluster_id": 3164323,
          "cite": [
            "808 F.3d 771",
            "2015 U.S. App. LEXIS 22205",
            "2015 WL 9267557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2830722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2828358,
          "cite": [
            "413 S.C. 458",
            "776 S.E.2d 367",
            "2015 S.C. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ryan E. Bean v. State of Indiana",
          "cluster_id": 2729695,
          "cite": [
            "973 N.E.2d 35",
            "2012 WL 3598405",
            "2012 Ind. App. LEXIS 403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
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
        "journal_ref": "Smith v. Illinois:lane1_negative"
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
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez",
          "cluster_id": 3145133,
          "cite": [
            "402 Ill. App. 3d 638",
            "343 Ill. Dec. 405",
            "934 N.E.2d 1008",
            "2010 Ill. App. LEXIS 587"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muniz v. State",
          "cluster_id": 1471480,
          "cite": [
            "851 S.W.2d 238",
            "1993 Tex. Crim. App. LEXIS 5",
            "1993 WL 871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 1890892,
          "cite": [
            "313 S.W.3d 317",
            "2010 Tex. Crim. App. LEXIS 723",
            "2010 WL 2382567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2459967,
          "cite": [
            "919 S.W.2d 370",
            "1996 Tex. Crim. App. LEXIS 35",
            "1994 WL 706957"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Duff",
          "cluster_id": 2651723,
          "cite": [
            "58 Cal. 4th 527",
            "317 P.3d 1148",
            "167 Cal. Rptr. 3d 615",
            "2014 WL 321872",
            "2014 Cal. LEXIS 637"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Russell Clark v. Tim Murphy",
          "cluster_id": 782256,
          "cite": [
            "331 F.3d 1062",
            "2003 Cal. Daily Op. Serv. 4923",
            "2003 Daily Journal DAR 6263",
            "2003 U.S. App. LEXIS 11496",
            "2003 WL 21338911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martinez",
          "cluster_id": 2637824,
          "cite": [
            "47 Cal. 4th 911",
            "10 Cal. Daily Op. Serv. 583",
            "224 P.3d 877",
            "105 Cal. Rptr. 3d 131",
            "2010 Cal. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balfour v. State",
          "cluster_id": 1858937,
          "cite": [
            "598 So. 2d 731",
            "1992 WL 64497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montoya v. State",
          "cluster_id": 1529929,
          "cite": [
            "744 S.W.2d 15",
            "1987 Tex. Crim. App. LEXIS 681",
            "1987 WL 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. San Nicolas",
          "cluster_id": 2507905,
          "cite": [
            "101 P.3d 509",
            "21 Cal. Rptr. 3d 612",
            "34 Cal. 4th 614",
            "2004 Daily Journal DAR 14410",
            "2004 Cal. Daily Op. Serv. 10643",
            "2004 Cal. LEXIS 11655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duplantis v. State",
          "cluster_id": 1659824,
          "cite": [
            "644 So. 2d 1235",
            "1994 WL 590825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111288 OR 9429796 OR 9429797) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjc1MzUwNDAwMDAwJnM9MTQ3NTI5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111288+OR+9429796+OR+9429797%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111288 OR 9429796 OR 9429797)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODAmcz0xMjAyNTMzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111288+OR+9429796+OR+9429797%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111288 OR 9429796 OR 9429797)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 0,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111288 OR 9429796 OR 9429797)",
    "indexed_citing_opinions": 751,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111288,
        "count": 658,
        "count_source": "search"
      },
      {
        "opinion_id": 9429796,
        "count": 112,
        "count_source": "search"
      },
      {
        "opinion_id": 9429797,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1228,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NDIzODMmcz05NDkxMzY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111288+OR+9429796+OR+9429797%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111288,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 368063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1161267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1259486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1773695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2087192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2090485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2190311,
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
    "date_created": "2026-07-05T19:56:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:59:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Illinois

```
<opinion type="majority">
<author id="b233-10">Per Curiam.</author>
<p id="b233-11">The petitioner Steven Smith was convicted of armed robbery and sentenced to a 9-year prison term. He contends that the police improperly elicited a confession from him after he clearly had requested the assistance of counsel, and that <page-number citation-index="1" label="92">*92</page-number>the trial court’s refusal to suppress the confession therefore violated <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). The Illinois Supreme Court held that Smith’s responses to continued police questioning rendered his initial request for counsel “ambiguous,” and that the officers therefore were not required to terminate their questioning. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d 365, 373-374</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d 236, 240</a></span> (1984). Under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>however, an accused’s postrequest responses to further interrogation may not be used to cast doubt on the clarity of his initial request for counsel. Finding no ambiguity in Smith’s initial request, we accordingly grant the petition and reverse.</p>
<p id="b234-5">I</p>
<p id="b234-6">Shortly after his arrest, 18-year-old Steven Smith was taken to an interrogation room at the Logan County Safety Complex for questioning by two police detectives. The session began as follows:</p>
<blockquote id="b234-7">“Q. Steve, I want to talk with you in reference to the armed robbery that took place at McDonald’s restaurant on the morning of the 19th. Are you familiar with this?</blockquote>
<blockquote id="A6q">“A. Yeah. My cousin Greg was.</blockquote>
<blockquote id="b234-8">“Q. Okay. But before I do that I must advise you of your rights. Okay? You have a right to remain silent. You do not have to talk to me unless you want to do so. Do you understand that?</blockquote>
<blockquote id="b234-9">“A. Uh. She told me to get my lawyer. She said you guys would railroad me.[<footnotemark>1</footnotemark>]</blockquote>
<blockquote id="b234-10">“Q. Do you understand that as I gave it to you, Steve?</blockquote>
<blockquote id="Ayg">“A. Yeah.</blockquote>
<blockquote id="b235-4"><page-number citation-index="1" label="93">*93</page-number>“Q. If you do want to talk to me I must advise you that whatever you say can and will be used against you in court. Do you understand that?</blockquote>
<blockquote id="b235-5">“A. Yeah.</blockquote>
<blockquote id="b235-6">“Q. You have a right to consult with a lawyer and to have a lawyer present with you when you’re being questioned. Do you understand that?</blockquote>
<blockquote id="b235-7">“A. <em>Uh, yeah. I’d like to do that.</em></blockquote>
<blockquote id="b235-8">“Q. Okay.” 102 111. 2d, at 368-369, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span> (emphasis in opinion).</blockquote>
<p id="b235-9">Instead of terminating the questioning at this point, the interrogating officers proceeded to finish reading Smith his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and then pressed him again to answer their questions:</p>
<blockquote id="b235-10">“Q. ... If you want a lawyer and you’re unable to pay for one a lawyer will be appointed to represent you free of cost, do you understand that?</blockquote>
<blockquote id="b235-11">“A. Okay.</blockquote>
<blockquote id="b235-12">“Q. Do you wish to talk to me at this time without a lawyer being present?</blockquote>
<blockquote id="b235-13">“A. <em>Yeah and no, uh, I don’t know what’s what, really.</em></blockquote>
<blockquote id="Af">“Q. <em>Well. You either have [to agree] to talk to me this time without a lawyer being present </em>and if you do agree to talk with me without a lawyer being present you can stop at any time you want to.</blockquote>
<blockquote id="b235-14">“Q. All right. I’ll talk to you then.” <em>Id., </em>at 369, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span> (emphasis in opinion) (bracketed words appear in Tr. 230).</blockquote>
<p id="b235-15">Smith then told the detectives that he knewin advance about the planned robbery, but contended that he had not been a participant. After considerable probing by the detectives, Smith confessed that “I committed it,” but he then returned to his earlier story that he had only known about the planned crime. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#369" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 369-370</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span>. Upon further <page-number citation-index="1" label="94">*94</page-number>questioning, Smith again insisted that “I wanta get a lawyer.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#370" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 370</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span>. This time the detectives honored the request and terminated the interrogation.</p>
<p id="b236-5">Smith moved at trial to suppress his incriminating statements, 1 Record 45, but the trial judge denied the motion, 4 Record 231. A transcript of the interrogation was introduced as part of the State’s case in chief, and Smith was convicted.</p>
<p id="b236-6">In affirming Smith’s conviction, the Appellate Court of Illinois for the Fourth District acknowledged that Smith’s first request for counsel “appears clear and unequivocal.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d 305, 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d 556, 559</a></span> (1983). The court concluded, however, that “when [the request] is considered with other statements — as it should be — it is clear that Smith was undecided about exercising his right to counsel” and “never made an effective request for counsel.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#309" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 309-310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#558" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 558-559</a></span>. Rather, Smith had made “merely an indecisive inquiry into the right to counsel.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.</p>
<p id="b236-7">The Illinois Supreme Court affirmed in a 4-3 vote. The majority agreed with the lower court that “Smith’s statements, considered in total, were ambiguous, and did not effectively invoke his right to counsel.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>. Specifically, the majority noted that although Smith stated “I’d like to do that” upon learning he had a right to his counsel’s presence at the interrogation, Smith <em>subsequently </em>replied “Yeah and no, uh, I don’t know what’s what really,” and “All right. I’ll talk to you then.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#372" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 372</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>. In light of these subsequent remarks, the majority reasoned, “Steven Smith did not <em>dearly assert </em>his right to counsel.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span> (emphasis in original).</p>
<p id="b236-8">II</p>
<p id="b236-9">An accused in custody, “having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made <page-number citation-index="1" label="95">*95</page-number>available to him,” unless he validly waives his earlier request for the assistance of counsel. <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>.<footnotemark>2</footnotemark> This “rigid” prophylactic rule, <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979), embodies two distinct inquiries. First, courts must determine whether the accused actually invoked his right to counsel. See, <em>e. g., Edwards </em>v. <em>Arizona, supra, </em>at 484-485 (whether accused “expressed his desire” for, or “clearly asserted” his right to, the assistance of counsel); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (whether accused “indicate[d] in any manner and at any stage of the process that he wish[ed] to consult with an attorney before speaking”). Second, if the accused invoked his right to counsel, courts may admit his responses to further questioning only on finding that he (a) initiated further discussions with the police, and (b) knowingly and intelligently waived the right he had invoked. <em>Edwards </em>v. <em>Arizona, supra, </em>at 485, 486, n. 9.</p>
<p id="b237-5">This case concerns the threshold inquiry: whether Smith invoked his right to counsel in the first instance. On occasion, an accused’s asserted request for counsel may be ambiguous or equivocal. As the majority and dissenting opinions below noted, courts have developed conflicting standards for determining the consequences of such ambiguities. See <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#372" aria-description="Citation for case: People v. Smith">102 <page-number citation-index="1" label="96">*96</page-number>Ill. 2d, at 372-373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>; <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#375" aria-description="Citation for case: People v. Smith"><em>id., </em>at 375-377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241-242</a></span> (Simon, J., dissenting).<footnotemark>3</footnotemark> We need not resolve this conflict in the instant case, however, because the judgment of the Illinois Supreme Court must be reversed irrespective of which standard is applied.</p>
<p id="b238-5">The conflict among courts is addressed to the relevance of alleged ambiguities or equivocations that either (1) <em>precede </em>an accused’s purported request for counsel, or (2) are part of the request <em>itself. </em>Neither circumstance pertains here, however. Neither the State nor the courts below, for example, have pointed to anything Smith previously had said that might have cast doubt on the meaning of his statement “I’d like to do that” upon learning that he had the right to his counsel’s presence.<footnotemark>4</footnotemark> Nor have they pointed to anything <page-number citation-index="1" label="97">*97</page-number>inherent in the nature of Smith’s actual request for counsel that reasonably would have suggested equivocation. As Justice Simon noted in his dissent below, “with the possible exception of the word ‘uh’ the defendant’s statement in this case was neither indecisive nor ambiguous: ‘Uh, yeah, I’d like to do that.’” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>. And the Illinois Appellate Court for the Fourth District itself acknowledged that the statement “appears clear and unequivocal.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.<footnotemark>5</footnotemark></p>
<p id="b239-5">The courts below were able to construe Smith’s request for counsel as “ambiguous” <em>only </em>by looking to Smith’s <em>subsequent </em>responses to continued police questioning and by concluding that, “considered in total,” Smith’s <em>“statements” </em>were equivocal. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span> (emphasis added); see also <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.<footnotemark>6</footnotemark> This line of analysis is unprecedented and untenable. As Justice Simon emphasized below, “[a] statement either is <page-number citation-index="1" label="98">*98</page-number>such an assertion [of the right to counsel] or it is not.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#375" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 375</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241</a></span>. Where nothing about the request for counsel or the circumstances leading up to the request would render it ambiguous, all questioning must cease. In these circumstances, an accused’s subsequent statements are relevant only to the question whether the accused waived the right he had invoked. Invocation and waiver are entirely distinct inquiries, and the two must not be blurred by merging them together.<footnotemark>7</footnotemark></p>
<p id="b240-5">The importance of keeping the two inquiries distinct is manifest. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>set forth a “bright-line rule” that <em>all </em>questioning must cease after an accused requests counsel. <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646</a></span> (1984). In the absence of such a bright-line prohibition, the authorities through “badger[ing]” or “overreaching” — explicit or subtle, deliberate or unintentional — might otherwise wear down the accused and persuade him to incriminate himself notwithstanding his earlier request for counsel’s assistance. <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>. With respect to the waiver inquiry, we accordingly have emphasized that a valid waiver “cannot be established by showing only that [the accused] responded to further police-initiated custodial interrogation.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. Using an accused’s subse<page-number citation-index="1" label="99">*99</page-number>quent responses to cast doubt on the adequacy of the initial request <em>itself </em>is even more intolerable. “No authority, and no logic, permits the interrogator to proceed ... on his own terms and as if the defendant had requested nothing, in the hope that the defendant might be induced to say something casting retrospective doubt on his initial statement that he wished to speak through an attorney or not at all.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#376" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 376</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241</a></span> (Simon, J., dissenting).<footnotemark>8</footnotemark></p>
<p id="b241-5">Ill</p>
<p id="b241-6">Our decision is a narrow one. We do not decide the circumstances in which an accused’s request for counsel may be <page-number citation-index="1" label="100">*100</page-number>characterized as ambiguous or equivocal as a result of events preceding the request or of nuances inherent in the request itself, nor do we decide the consequences of such ambiguity or equivocation. We hold only that, under the clear logical force of settled precedent, an accused’s <em>postrequest </em>responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself. Such subsequent statements are relevant only to the distinct question of waiver.</p>
<p id="b242-5">Accordingly, Smith’s motion for leave to proceed <em>informa pauperis </em>is granted, the petition for a writ of certiorari is granted, the judgment of the Illinois Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b242-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b234-11"> According to the Illinois Supreme Court, the “she” that Smith referred to was an unidentified woman named Chico. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#368" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 368-369</a></span>, 466 N. E. 2d. at 238.</p>
</footnote>
<footnote label="2">
<p id="b237-6"> We have repeatedly emphasized this restraint on police interrogation. In addition to <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>see also <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646-647</a></span> (1984); <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) <em>(Edwards </em>set forth a “prophylactic rule, designed to protect an accused in police custody from being badgered by police officers . . .”); <em>Wyrick </em>v. <em>Fields, </em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/#45" aria-description="Citation for case: Wyrick v. Fields">459 U. S. 42, 45-46</a></span> (1982) <em>(per curiam); Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 298</a></span> (1980); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979) (discussing the “rigid rule” that “an accused’s request for an attorney is <em>per se </em>an invocation of his Fifth Amendment rights, requiring that all interrogation cease”); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966) (“If the individual states that he wants an attorney, the interrogation must cease until-an attorney is present”). Cf. <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#105" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 105-106</a></span> (1975) (rule requiring termination of questioning upon accused’s invocation of his right to silence prevents police from “persisting in repeated efforts to wear down [the accused’s] resistance and make him change his mind”).</p>
</footnote>
<footnote label="3">
<p id="b238-6"> Some courts have held that all questioning must cease upon any request for or reference to counsel, however equivocal or ambiguous. See, <em>e. g., People </em>v. <em>Superior Court, </em><span class="citation" data-id="1161267"><a href="/opinion/1161267/people-v-superior-court-zolnay/#735" aria-description="Citation for case: People v. Superior Court (Zolnay)">15 Cal. 3d 729, 735-736</a></span>, <span class="citation" data-id="1161267"><a href="/opinion/1161267/people-v-superior-court-zolnay/#1394" aria-description="Citation for case: People v. Superior Court (Zolnay)">542 P. 2d 1390, 1394-1395</a></span> (1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/816/">429 U. S. 816</a></span> (1976); <em>Ochoa </em>v. <em>State, </em><span class="citation" data-id="9680788"><a href="/opinion/1773695/ochoa-v-state/#800" aria-description="Citation for case: Ochoa v. State">573 S. W. 2d 796, 800-801</a></span> (Tex. Crim. App. 1978). Others have attempted to define a threshold standard of clarity for such requests, and have held that requests falling below this threshold do not trigger the right to counsel. See, <em>e. g., People </em>v. <em>Krueger, </em><span class="citation" data-id="2090485"><a href="/opinion/2090485/people-v-krueger/#311" aria-description="Citation for case: People v. Krueger">82 Ill. 2d 305, 311</a></span>, <span class="citation" data-id="2090485"><a href="/opinion/2090485/people-v-krueger/#540" aria-description="Citation for case: People v. Krueger">412 N. E. 2d 537, 540</a></span> (1980) (“[A]n assertion of the right to counsel need not be explicit, unequivocal, or made with unmistakable clarity,” but not “every reference to an attorney, no matter how vague, indecisive or ambiguous, should constitute an invocation of the right to counsel”), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./451/1019/">451 U. S. 1019</a></span> (1981). Still others have adopted a third approach, holding that when an accused makes an equivocal statement that “arguably” can be construed as a request for counsel, all interrogation must immediately cease except for narrow questions designed to “clarify” the earlier statement and the accused’s desires respecting counsel. See, <em>e. g., Thompson </em>v. <em>Wainwright, </em><span class="citation" data-id="9465905"><a href="/opinion/368063/larry-thompson-v-louie-l-wainwright-secretary-department-of-offender/#771" aria-description="Citation for case: Larry Thompson v. Louie L. Wainwright, Secretary,...">601 F. 2d 768, 771-772</a></span> (CA5 1979); <em>State </em>v. <em>Moulds, </em><span class="citation" data-id="1259486"><a href="/opinion/1259486/state-v-moulds/#888" aria-description="Citation for case: State v. Moulds">105 Idaho 880, 888</a></span>, <span class="citation" data-id="1259486"><a href="/opinion/1259486/state-v-moulds/#1082" aria-description="Citation for case: State v. Moulds">673 P. 2d 1074, 1082</a></span> (App. 1983).</p>
</footnote>
<footnote label="4">
<p id="b238-7"> Indeed, as Justice Simon noted in his dissent below, Smith’s “only previous statement to the officer which is of any significance in this regard is an assertion that ‘she’ warned him that the police would ‘railroad’ him and advised him to get a lawyer before submitting to interrogation.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>; see <em>supra, </em>at 92. Far from creating “ambiguity” concerning Smith’s subsequent request, this statement could only have reinforced the clarity of Smith’s invocation of his right to counsel.</p>
</footnote>
<footnote label="5">
<p id="b239-6"> Justice Rehnquist in his dissent asserts that the trial judge “implicitly concluded that petitioner’s initial statement was not a clear request,” post, at 101, and criticizes the Court for “relitigat[ingj” this “essentially factual inquiry,” <em>post, </em>at 100. As this argument suggests, the trial judge did not discuss the clarity of Smith’s request, but instead simply denied without comment Smith’s motion to suppress. 4 Record 231. In fact, the only “finding” made by the state courts with respect to Smith’s initial request was that it did indeed appear to be “clear and unequivocal.” See <em>supra </em>this pagé.</p>
</footnote>
<footnote label="6">
<p id="b239-11"> The Illinois Appellate Court for the Fourth District also suggested that it was significant that Smith’s request came <em>during </em>the administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings: “[H]e merely expressed an <em>interest </em>in obtaining counsel during the administration of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and prior to the beginning of any interrogation. . . . Smith’s statements were not a request for counsel during interrogation. Indeed, interrogation had not begun.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#309" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 309-310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#558" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 558-559</a></span> (emphasis in original). Justice Rehnquist in his dissent similarly contends that the authorities need not stop their questioning if an accused requests counsel prior to or during the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. See <em>post, </em>at 100-101, 104. Such reasoning is plainly wrong. A request for counsel coming “at <em>any </em>stage of the process” requires that questioning cease until counsel has been provided. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (emphasis added).</p>
</footnote>
<footnote label="7">
<p id="b240-6"> The dissent contends that the questioning here was “entirely consistent” with the proscriptions of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039</a></span> (1983). <em>Post, </em>at 102. In those cases, the dissent argues, the authorities immediately terminated their questioning once the suspects had invoked their right to counsel, but then sought “to resume interrogation at a later time.” <em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">Ibid.</a></span> </em>In this case, on the other hand, the detectives did not even <em>initially </em>terminate their questioning. In such circumstances, the dissent proclaims, it is proper to consider “the entire flavor of the colloquy.” <em>Post, </em>at 101. To the extent the dissent suggests that an accused’s Fifth Amendment right <em>to </em>counsel should turn on whether the authorities initially honor his request, we reject this approach as palpably untenable under <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>Whether in the same interrogating session or in subsequent sessions, the so-called “flavor” of an accused’s request for counsel cannot be dissipated by continued police questioning.</p>
</footnote>
<footnote label="8">
<p id="b241-7"> Most of the dissent is devoted to an effort at demonstrating that the detectives did not <em>actually </em>extract Smith’s confession through trickery or coercion. See <em>post, </em>at 103. This effort is of course beside the point, because the rule we announced in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and which we follow today is a prophylactic safeguard whose application does not turn on whether coercion in fact was employed. Nevertheless, the actual course of the subsequent interrogation in this case reinforces our concern that, absent a bright-line rule requiring an immediate cessation of questioning, an accused may be “badgered” to speak as a result of police “overreaching.” See <em>supra, </em>at 98. As Justice Simon noted in his dissent below:</p>
<blockquote id="b241-8">“I fail to understand how the officer could have mistaken the defendant’s meaning, and no justification is given or is apparent for his proceeding through to the end of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and in the course of doing so misrepresenting to Smith the meaning of those warnings by the following admonition: ‘You either have to talk to me this time without a lawyer being present and if you do agree to talk with me without a lawyer being present you can stop at any time you want to.’ This communication, even if inadvertent, clearly imparted to the defendant the warning that he had to talk to the interrogator and was seriously misleading.</blockquote>
<blockquote id="b241-9">“. . . In this regard, I find it particularly significant that Smith, who was apparently in police custody for the first time in his life and admitted that he did not ‘know what’s what,’ agreed to talk to the police only after he was told, ostensibly by way of explaining the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, that he had no other choice.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 377-378</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>.</blockquote>
<p id="b241-10">The interrogation here bore a substantial similarity to the one condemned in <em>Edwards </em>v. <em>Arizona, </em>where the accused after requesting counsel was told that “he had” to talk to his interrogators. <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 479</a></span>. It was precisely such “badger[ing]” that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>safeguard was designed to prevent. See <em>Oregon </em>v. <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw"><em>Bradshaw, supra, </em>at 1044</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Spano v. New York.md  (`case`, 5 assertions)

### content_page

```
---
title: "Spano v. New York"
type: case
citation: "360 U.S. 315 (1959)"
parallel_cite: "79 S. Ct. 1202; 3 L. Ed. 2d 1265"
neutral_cite: 1959 U.S. LEXIS 751
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-06-22
docket: 326
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Spano v. New York
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105917/spano-v-new-york/"
  cluster_id: 105917
  opinion_id: 105917
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "confession", "voluntariness", "due-process"]
holding: "A confession produced by psychological pressure — here a friend's feigned distress plus persistent overnight questioning of a suspect…"
lake:
  record_id: Spano v. New York
  status: verified
  projected_at: 2026-07-06
---

# Spano v. New York

*360 U.S. 315 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spano, a foreign-born man of limited education, was indicted for murder and surrendered with his retained lawyer, who instructed him to remain silent. Over an eight-hour overnight interrogation, police refused his repeated requests to consult his lawyer and enlisted a rookie-officer acquaintance, Bruno, to falsely tell Spano that Spano's call had jeopardized Bruno's job and family—until Spano confessed.

## Issue
Whether a confession obtained by prolonged overnight questioning and a false-friend appeal, after the suspect was indicted, had counsel, and asked to remain silent, was voluntary.

## Rule
Voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and a confession produced by official pressure is involuntary. "We conclude that petitioner's will was overborne by official pressure, fatigue and sympathy falsely aroused, after considering all the facts in their post-indictment setting." — 360 U.S. at 323. ^pin-323

## Application
The combination of persistent overnight questioning, the repeated denial of Spano's requests to consult his lawyer, and the calculated use of Bruno's feigned distress overbore Spano's will. On those facts the confession was involuntary, and its admission violated due process, so the conviction was reversed.

## Conclusion
The confession was involuntary under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Part of the due-process voluntariness line ([[Brown v. Mississippi]], [[Chambers v. Florida]], [[Ashcraft v. Tennessee]]); [[Colorado v. Connelly]] later held that coercive police activity is a necessary predicate to an involuntariness finding.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Spano v. New York*, 360 U.S. 315 (1959) — https://www.courtlistener.com/opinion/105917/spano-v-new-york/ — pinpoint: 323.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b0ec43d0a23f027d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "360 U.S. 315 (1959)", "court": "U.S. Supreme Court", "neutral_cite": "1959 U.S. LEXIS 751", "official_citation_present": true, "parallel_cite": "79 S. Ct. 1202; 3 L. Ed. 2d 1265", "title": "Spano v. New York", "year": "1959"}}
{"assertion_id": "6eacc9d941abcce2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession produced by psychological pressure — here a friend's feigned distress plus persistent overnight questioning of a suspect…", "title": "Spano v. New York"}}
{"assertion_id": "77bc3d873c677529", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Spano v. New York"}}
{"assertion_id": "3dee4f2ecda10cdc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1959-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Spano v. New York", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Spano v. New York", "varies_by_point": "false"}}
{"assertion_id": "45384156ce3171d3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Spano v. New York"}}
```

### lake record — Spano v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Spano v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Spano v. New York",
    "case_name_short": "Spano",
    "case_name_full": "Spano v. New York",
    "input_case_name": "Spano v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-06-22",
    "year": 1959,
    "docket": "326",
    "cluster_id": 105917,
    "lead_opinion_id": 105917,
    "sibling_ids": [
      105917,
      9421842,
      9421843,
      9421844
    ],
    "absolute_url": "/opinion/105917/spano-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "360 U.S. 315",
      "volume": "360",
      "reporter": "U.S.",
      "page": "315",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 1202",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1265",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1265",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 751",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "751",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "360 U.S. 315",
        "volume": "360",
        "reporter": "U.S.",
        "page": "315",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 1202",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1265",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1265",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 751",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "751",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "360 U.S. 315",
    "official_selection": {
      "court_class": "scotus",
      "selected": "360 U.S. 315",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-323",
      "page": null,
      "quote": "--- # Spano v. New York *360 U.S. 315 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spano, a foreign-born man of limited education, was indicted for murder and surrendered with his retained lawyer, who instructed him to remain silent. Over an eight-hour overnight interrogation, police refused his repeated requests to consult his lawyer and enlisted a rookie-officer acquaintance, Bruno, to falsely tell Spano that Spano's call had jeopardized Bruno's job and family\u2014until Spano confessed. ## Issue Whether a confession obtained by prolonged overnight questioning and a false-friend appeal, after the suspect was indicted, had counsel, and asked to remain silent, was voluntary. ## Rule Voluntariness is judged on the totality of the circumstances, and a confession produced by official pressure is involuntary.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Spano v. New York",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sawyer",
          "cluster_id": 2521466,
          "cite": [
            "2004 OK CR 22",
            "92 P.3d 707",
            "2004 WL 1244992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gomes v. State",
          "cluster_id": 2342281,
          "cite": [
            "9 S.W.3d 373",
            "1999 WL 1080989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Dorton",
          "cluster_id": 2966500,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zuliani v. State",
          "cluster_id": 2372052,
          "cite": [
            "903 S.W.2d 812",
            "1995 WL 410841"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knotts",
          "cluster_id": 3990639,
          "cite": [
            "677 N.E.2d 358",
            "111 Ohio App. 3d 753"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell Ledbetter v. Ron Edwards, Warden",
          "cluster_id": 678531,
          "cite": [
            "35 F.3d 1062",
            "1994 U.S. App. LEXIS 26229",
            "1994 WL 511213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte McCary",
          "cluster_id": 1793877,
          "cite": [
            "528 So. 2d 1133",
            "1988 WL 10157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massiah v. United States",
          "cluster_id": 106822,
          "cite": [
            "12 L. Ed. 2d 246",
            "84 S. Ct. 1199",
            "377 U.S. 201",
            "1964 U.S. LEXIS 1277"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kastigar v. United States",
          "cluster_id": 108541,
          "cite": [
            "32 L. Ed. 2d 212",
            "92 S. Ct. 1653",
            "406 U.S. 441",
            "1972 U.S. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Waterfront Commission of New York Harbor",
          "cluster_id": 106864,
          "cite": [
            "12 L. Ed. 2d 678",
            "84 S. Ct. 1594",
            "378 U.S. 52",
            "1964 U.S. LEXIS 2229",
            "56 L.R.R.M. (BNA) 2544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rogers v. Richmond",
          "cluster_id": 106192,
          "cite": [
            "5 L. Ed. 2d 760",
            "81 S. Ct. 735",
            "365 U.S. 534",
            "1961 U.S. LEXIS 1494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haynes v. Washington",
          "cluster_id": 106625,
          "cite": [
            "10 L. Ed. 2d 513",
            "83 S. Ct. 1336",
            "373 U.S. 503",
            "1963 U.S. LEXIS 1439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NjkyMDMyMDAwMDAmcz0xNzkzODc3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDEmcz0xMTIzODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
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
    "complete_query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
    "indexed_citing_opinions": 763,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105917,
        "count": 720,
        "count_source": "search"
      },
      {
        "opinion_id": 9421842,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9421843,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9421844,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1164,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/spano-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzODczMjQmcz00NjUwNTM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105917,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 1236300,
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
    "date_created": "2026-07-05T20:13:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Spano v. New York

```
<div>
<center><b><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U.S. 315</a></span> (1959)</b></center>
<center><h1>SPANO<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 582.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 27, 1959.</center>
<center>Decided June 22, 1959.</center>
CERTIORARI TO THE COURT OF APPEALS OF NEW YORK.
<p><i>Herbert S. Siegal</i> argued the cause for petitioner. With him on the brief was <i>Rita D. Schechter.</i></p>
<p><i>Irving Anolik</i> argued the cause for respondent. With him on the brief were <i>Daniel V. Sullivan</i> and <i>Walter E. Dillon.</i></p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>This is another in the long line of cases presenting the question whether a confession was properly admitted into evidence under the Fourteenth Amendment. As in all such cases, we are forced to resolve a conflict between two fundamental interests of society; its interest in prompt and efficient law enforcement, and its interest in preventing the rights of its individual members from being abridged by unconstitutional methods of law enforcement. <span class="star-pagination">*316</span> Because of the delicate nature of the constitutional determination which we must make, we cannot escape the responsibility of making our own examination of the record. <i>Norris</i> v. <i>Alabama,</i> <span class="citation" data-id="102407"><a href="/opinion/102407/norris-v-alabama/" aria-description="Citation for case: Norris v. Alabama">294 U. S. 587</a></span>.</p>
<p>The State's evidence reveals the following: Petitioner Vincent Joseph Spano is a derivative citizen of this country, having been born in Messina, Italy. He was 25 years old at the time of the shooting in question and had graduated from junior high school. He had a record of regular employment. The shooting took place on January 22, 1957.</p>
<p>On that day, petitioner was drinking in a bar. The decedent, a former professional boxer weighing almost 200 pounds who had fought in Madison Square Garden, took some of petitioner's money from the bar. Petitioner followed him out of the bar to recover it. A fight ensued, with the decedent knocking petitioner down and then kicking him in the head three or four times. Shock from the force of these blows caused petitioner to vomit. After the bartender applied some ice to his head, petitioner left the bar, walked to his apartment, secured a gun, and walked eight or nine blocks to a candy store where the decedent was frequently to be found. He entered the store in which decedent, three friends of decedent, at least two of whom were ex-convicts, and a boy who was supervising the store were present. He fired five shots, two of which entered the decedent's body, causing his death. The boy was the only eyewitness; the three friends of decedent did not see the person who fired the shot. Petitioner then disappeared for the next week or so.</p>
<p>On February 1, 1957, the Bronx County Grand Jury returned an indictment for first-degree murder against petitioner. Accordingly, a bench warrant was issued for his arrest, commanding that he be forthwith brought before the court to answer the indictment, or, if the court had adjourned for the term, that he be delivered into the <span class="star-pagination">*317</span> custody of the Sheriff of Bronx County. See N. Y. Code Crim. Proc. § 301.</p>
<p>On February 3, 1957, petitioner called one Gaspar Bruno, a close friend of 8 or 10 years' standing who had attended school with him. Bruno was a fledgling police officer, having at that time not yet finished attending police academy. According to Bruno's testimony, petitioner told him "that he took a terrific beating, that the deceased hurt him real bad and he dropped him a couple of times and he was dazed; he didn't know what he was doing and that he went and shot at him." Petitioner told Bruno that he intended to get a lawyer and give himself up. Bruno relayed this information to his superiors.</p>
<p>The following day, February 4, at 7:10 p. m., petitioner, accompanied by counsel, surrendered himself to the authorities in front of the Bronx County Building, where both the office of the Assistant District Attorney who ultimately prosecuted his case and the courtroom in which he was ultimately tried were located. His attorney had cautioned him to answer no questions, and left him in the custody of the officers. He was promptly taken to the office of the Assistant District Attorney and at 7:15 p. m. the questioning began, being conducted by Assistant District Attorney Goldsmith, Lt. Gannon, Detectives Farrell, Lehrer and Motta, and Sgt. Clarke. The record reveals that the questioning was both persistent and continuous. Petitioner, in accordance with his attorney's instructions, steadfastly refused to answer. Detective Motta testified: "He refused to talk to me." "He just looked up to the ceiling and refused to talk to me." Detective Farrell testified:</p>
<blockquote>"Q. And you started to interrogate him?</blockquote>
<blockquote>"A. That is right.</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. What did he say?</blockquote>
<blockquote>
<span class="star-pagination">*318</span> "A. He said `you would have to see my attorney. I tell you nothing but my name."</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Did you continue to examine him?</blockquote>
<blockquote>"A. Verbally, yes, sir."</blockquote>
<p>He asked one officer, Detective Ciccone, if he could speak to his attorney, but that request was denied. Detective Ciccone testified that he could not find the attorney's name in the telephone book.<sup>[1]</sup> He was given two sandwiches, coffee and cake at 11 p. m.</p>
<p>At 12:15 a. m. on the morning of February 5, after five hours of questioning in which it became evident that petitioner was following his attorney's instructions, on the Assistant District Attorney's orders petitioner was transferred to the 46th Squad, Ryer Avenue Police Station. The Assistant District Attorney also went to the police station and to some extent continued to participate in the interrogation. Petitioner arrived at 12:30 and questioning was resumed at 12:40. The character of the questioning is revealed by the testimony of Detective Farrell:</p>
<blockquote>"Q. Who did you leave him in the room with?</blockquote>
<blockquote>"A. With Detective Lehrer and Sergeant Clarke came in and Mr. Goldsmith came in or Inspector Halk came in. It was back and forth. People just came in, spoke a few words to the defendant or they listened a few minutes and they left."</blockquote>
<p>But petitioner persisted in his refusal to answer, and again requested permission to see his attorney, this time from Detective Lehrer. His request was again denied.</p>
<p>It was then that those in charge of the investigation decided that petitioner's close friend, Bruno, could be of <span class="star-pagination">*319</span> use. He had been called out on the case around 10 or 11 p. m., although he was not connected with the 46th Squad or Precinct in any way. Although, in fact, his job was in no way threatened, Bruno was told to tell petitioner that petitioner's telephone call had gotten him "in a lot of trouble," and that he should seek to extract sympathy from petitioner for Bruno's pregnant wife and three children. Bruno developed this theme with petitioner without success, and petitioner, also without success, again sought to see his attorney, a request which Bruno relayed unavailingly to his superiors. After this first session with petitioner, Bruno was again directed by Lt. Gannon to play on petitioner's sympathies, but again no confession was forthcoming. But the Lieutenant a third time ordered Bruno falsely to importune his friend to confess, but again petitioner clung to his attorney's advice. Inevitably, in the fourth such session directed by the Lieutenant, lasting a full hour, petitioner succumbed to his friend's prevarications and agreed to make a statement. Accordingly, at 3:25 a. m. the Assistant District Attorney, a stenographer, and several other law enforcement officials entered the room where petitioner was being questioned, and took his statement in question and answer form with the Assistant District Attorney asking the questions. The statement was completed at 4:05 a. m.</p>
<p>But this was not the end. At 4:30 a. m. three detectives took petitioner to Police Headquarters in Manhattan. On the way they attempted to find the bridge from which petitioner said he had thrown the murder weapon. They crossed the Triborough Bridge into Manhattan, arriving at Police Headquarters at 5 a. m., and left Manhattan for the Bronx at 5:40 a. m. via the Willis Avenue Bridge. When petitioner recognized neither bridge as the one from which he had thrown the weapon, they reentered Manhattan via the Third Avenue Bridge, which petitioner stated was the right one, and then returned to <span class="star-pagination">*320</span> the Bronx well after 6 a. m. During that trip the officers also elicited a statement from petitioner that the deceased was always "on [his] back," "always pushing" him and that he was "not sorry" he had shot the deceased. All three detectives testified to that statement at the trial.</p>
<p>Court opened at 10 a. m. that morning, and petitioner was arraigned at 10:15.</p>
<p>At the trial, the confession was introduced in evidence over appropriate objections. The jury was instructed that it could rely on it only if it was found to be voluntary. The jury returned a guilty verdict and petitioner was sentenced to death. The New York Court of Appeals affirmed the conviction over three dissents, 4 N. Y. 2d 256, 173 N. Y. S. 2d 793, <span class="citation" data-id="5516991"><a href="/opinion/5669883/people-v-spano/" aria-description="Citation for case: People v. Spano">150 N. E. 2d 226</a></span>, and we granted certiorari to resolve the serious problem presented under the Fourteenth Amendment. <span class="citation multiple-matches"><a href="/c/U.%20S./358/919/">358 U. S. 919</a></span>.</p>
<p>Petitioner's first contention is that his absolute right to counsel in a capital case, <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, became operative on the return of an indictment against him, for at that time he was in every sense a defendant in a criminal case, the grand jury having found sufficient cause to believe that he had committed the crime. He argues accordingly that following indictment no confession obtained in the absence of counsel can be used without violating the Fourteenth Amendment. He seeks to distinguish <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, on the ground that in those cases no indictment had been returned. We find it unnecessary to reach that contention, for we find use of the confession obtained here inconsistent with the Fourteenth Amendment under traditional principles.</p>
<p>The abhorrence of society to the use of involuntary confessions does not turn alone on their inherent untrust-worthiness. It also turns on the deep-rooted feeling that the police must obey the law while enforcing the law; that in the end life and liberty can be as much endangered <span class="star-pagination">*321</span> from illegal methods used to convict those thought to be criminals as from the actual criminals themselves. Accordingly, the actions of police in obtaining confessions have come under scrutiny in a long series of cases.<sup>[2]</sup> Those cases suggest that in recent years law enforcement officials have become increasingly aware of the burden which they share, along with our courts, in protecting fundamental rights of our citizenry, including that portion of our citizenry suspected of crime. The facts of no case recently in this Court have quite approached the brutal beatings in <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), or the 36 consecutive hours of questioning present in <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944). But as law enforcement officers become more responsible, and the methods used to extract confessions more sophisticated, our duty to enforce federal constitutional protections does not cease. It only becomes more difficult because of the more delicate judgments to be made. Our judgment here is that, on all the facts, this conviction cannot stand.</p>
<p>Petitioner was a foreign-born young man of 25 with no past history of law violation or of subjection to official interrogation, at least insofar as the record shows. He <span class="star-pagination">*322</span> had progressed only one-half year into high school and the record indicates that he had a history of emotional instability.<sup>[3]</sup> He did not make a narrative statement, but was subject to the leading questions of a skillful prosecutor in a question and answer confession. He was subjected to questioning not by a few men, but by many. They included Assistant District Attorney Goldsmith, one Hyland of the District Attorney's Office, Deputy Inspector Halks,<sup>[4]</sup> Lieutenant Gannon, Detective Ciccone, Detective Motta, Detective Lehrer, Detective Marshal, Detective Farrell, Detective Leira,<sup>[5]</sup> Detective Murphy, Detective Murtha, Sergeant Clarke, Patrolman Bruno and Stenographer Baldwin. All played some part, and the effect of such massive official interrogation must have been felt. Petitioner was questioned for virtually eight straight hours before he confessed, with his only respite being a transfer to an arena presumably considered more appropriate by the police for the task at hand. Nor was the questioning conducted during normal business hours, but began in early evening, continued into the night, and did not bear fruition until the not-too-early morning. The drama was not played out, with the final admissions obtained, until almost sunrise. In such circumstances slowly mounting fatigue does, and is calculated to, play its part. The questioners persisted in the face of his repeated refusals to answer on the advice of his <span class="star-pagination">*323</span> attorney, and they ignored his reasonable requests to contact the local attorney whom he had already retained and who had personally delivered him into the custody of these officers in obedience to the bench warrant.</p>
<p>The use of Bruno, characterized in this Court by counsel for the State as a "childhood friend" of petitioner's, is another factor which deserves mention in the totality of the situation. Bruno's was the one face visible to petitioner in which he could put some trust. There was a bond of friendship between them going back a decade into adolescence. It was with this material that the officers felt that they could overcome petitioner's will. They instructed Bruno falsely to state that petitioner's telephone call had gotten him into trouble, that his job was in jeopardy, and that loss of his job would be disastrous to his three children, his wife and his unborn child. And Bruno played this part of a worried father, harried by his superiors, in not one, but four different acts, the final one lasting an hour. Cf. <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>. Petitioner was apparently unaware of John Gay's famous couplet:</p>
         "An open foe may prove a curse,
          But a pretended friend is worse,"
<p>and he yielded to his false friend's entreaties.</p>
<p>We conclude that petitioner's will was overborne by official pressure, fatigue and sympathy falsely aroused, after considering all the facts in their post-indictment setting.<sup>[6]</sup> Here a grand jury had already found sufficient cause to require petitioner to face trial on a charge of first-degree murder, and the police had an eyewitness to the shooting. The police were not therefore merely trying to solve a crime, or even to absolve a suspect. Compare <span class="star-pagination">*324</span> <i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>,</i> and <i>Cicenia</i> v. <i><span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">Lagay, supra</a></span></i><i>.</i> They were rather concerned primarily with securing a statement from defendant on which they could convict him. The undeviating intent of the officers to extract a confession from petitioner is therefore patent. When such an intent is shown, this Court has held that the confession obtained must be examined with the most careful scrutiny, and has reversed a conviction on facts less compelling than these. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>. Accordingly, we hold that petitioner's conviction cannot stand under the Fourteenth Amendment.</p>
<p>The State suggests, however, that we are not free to reverse this conviction, since there is sufficient other evidence in the record from which the jury might have found guilt, relying on <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span>. But <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 568</a></span>, authoritatively establishes that <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> did not hold that a conviction may be sustained on the basis of other evidence if a confession found to be involuntary by this Court was used, even though limiting instructions were given. <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> held only that when a confession is not found by this Court to be involuntary, this Court will not reverse on the ground that the jury might have found it involuntary and might have relied on it. The judgment must be</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BLACK and MR. JUSTICE BRENNAN join, concurring.</p>
<p>While I join the opinion of the Court, I add what for me is an even more important ground of decision.</p>
<p>We have often divided on whether state authorities may question a suspect for hours on end when he has no lawyer present and when he has demanded that he have the benefit of legal advice. See <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and cases cited. But here we deal not with a suspect but with a man who has been formally charged <span class="star-pagination">*325</span> with a crime. The question is whether after the indictment and before the trial the Government can interrogate the accused <i>in secret</i> when he asked for his lawyer and when his request was denied. This is a capital case; and under the rule of <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, the defendant was entitled to be represented by counsel. This representation by counsel is not restricted to the trial. As stated in <i>Powell</i> v. <i>Alabama, supra,</i> p. 57:</p>
<blockquote>"during perhaps the most critical period of the proceedings against these defendants, that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation were vitally important, the defendants did not have the aid of counsel in any real sense, although they were as much entitled to such aid during that period as at the trial itself."</blockquote>
<p>Depriving a person, formally charged with a crime, of counsel during the period prior to trial may be more damaging than denial of counsel during the trial itself.</p>
<p>We do not have here mere suspects who are being secretly interrogated by the police as in <i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>,</i> nor witnesses who are being questioned in secret administrative or judicial proceedings as in <i>In re Groban,</i> <span class="citation" data-id="9421372"><a href="/opinion/105449/in-re-groban/" aria-description="Citation for case: In Re Groban">352 U. S. 330</a></span>, and <i>Anonymous Nos. 6 &amp; 7</i> v. <i>Baker, ante,</i> p. 287. This is a case of an accused, who is scheduled to be tried by a judge and jury, being tried in a preliminary way by the police. This is a kangaroo court procedure whereby the police produce the vital evidence in the form of a confession which is useful or necessary to obtain a conviction. They in effect deny him effective representation by counsel. This seems to me to be a flagrant violation of the principle announced in <i>Powell</i> v. <i>Alabama, supra</i><i>,</i> that the right of counsel extends to the preparation for trial, as well as to the trial itself. As Professor Chafee once said, "A person accused of crime <span class="star-pagination">*326</span> needs a lawyer right after his arrest probably more than at any other time." Chafee, Documents on Fundamental Human Rights, Pamphlet 2 (1951-1952), p. 541. When he is deprived of that right after indictment and before trial, he may indeed be denied effective representation by counsel at the only stage when legal aid and advice would help him. This <i>secret inquisition</i> by the police when defendant asked for and was denied counsel was as serious an invasion of his constitutional rights as the denial of a continuance in order to employ counsel was held to be in <i>Chandler</i> v. <i>Fretag,</i> <span class="citation" data-id="105241"><a href="/opinion/105241/chandler-v-warden-fretag/#10" aria-description="Citation for case: Chandler v. Warden Fretag">348 U. S. 3, 10</a></span>. What we said in <i>Avery</i> v. <i>Alabama,</i> <span class="citation" data-id="103272"><a href="/opinion/103272/avery-v-alabama/#446" aria-description="Citation for case: Avery v. Alabama">308 U. S. 444, 446</a></span>, has relevance here:</p>
<blockquote>". . . the denial of opportunity for appointed counsel to confer, to consult with the accused and to prepare his defense, could convert the appointment of counsel into a sham and nothing more than a formal compliance with the Constitution's requirement that an accused be given the assistance of counsel."</blockquote>
<p>I join with Judges Desmond, Fuld, and Van Voorhis of the New York Court of Appeals (4 N. Y. 2d 256, 266, 173 N. Y. S. 2d 793, 801, <span class="citation" data-id="5516991"><a href="/opinion/5669883/people-v-spano/#231" aria-description="Citation for case: People v. Spano">150 N. E. 2d 226, 231-232</a></span>), in asking, what use is a defendant's right to effective counsel at every stage of a criminal case if, while he is held awaiting trial, he can be questioned in the absence of counsel until he confesses? In that event the secret trial in the police precincts effectively supplants the public trial guaranteed by the Bill of Rights.</p>
<p>MR. JUSTICE STEWART, whom MR. JUSTICE DOUGLAS and MR. JUSTICE BRENNAN join, concurring.</p>
<p>While I concur in the opinion of the Court, it is my view that the absence of counsel when this confession was elicited was alone enough to render it inadmissible under the Fourteenth Amendment.</p>
<p><span class="star-pagination">*327</span> Let it be emphasized at the outset that this is not a case where the police were questioning a suspect in the course of investigating an unsolved crime. See <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>; <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>. When the petitioner surrendered to the New York authorities he was under indictment for first degree murder.</p>
<p>Under our system of justice an indictment is supposed to be followed by an arraignment and a trial. At every stage in those proceedings the accused has an absolute right to a lawyer's help if the case is one in which a death sentence may be imposed. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>. Indeed the right to the assistance of counsel whom the accused has himself retained is absolute, whatever the offense for which he is on trial. <i>Chandler</i> v. <i>Fretag,</i> <span class="citation" data-id="105241"><a href="/opinion/105241/chandler-v-warden-fretag/" aria-description="Citation for case: Chandler v. Warden Fretag">348 U. S. 3</a></span>.</p>
<p>What followed the petitioner's surrender in this case was not arraignment in a court of law, but an all-night inquisition in a prosecutor's office, a police station, and an automobile. Throughout the night the petitioner repeatedly asked to be allowed to send for his lawyer, and his requests were repeatedly denied. He finally was induced to make a confession. That confession was used to secure a verdict sending him to the electric chair.</p>
<p>Our Constitution guarantees the assistance of counsel to a man on trial for his life in an orderly courtroom, presided over by a judge, open to the public, and protected by all the procedural safeguards of the law. Surely a Constitution which promises that much can vouchsafe no less to the same man under midnight inquisition in the squad room of a police station.</p>
<h2>NOTES</h2>
<p>[1]  How this could be so when the attorney's name, Tobias Russo, was concededly in the telephone book does not appear. The trial judge sustained objections by the Assistant District Attorney to questions designed to delve into this mystery.</p>
<p>[2]  <i>E. g., </i><i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>; <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>; <i>Ashdown</i> v. <i>Utah,</i> <span class="citation" data-id="9421686"><a href="/opinion/105744/ashdown-v-utah/" aria-description="Citation for case: Ashdown v. Utah">357 U. S. 426</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>; <i>Thomas</i> v. <i>Arizona,</i> <span class="citation" data-id="105683"><a href="/opinion/105683/thomas-v-arizona/" aria-description="Citation for case: Thomas v. Arizona">356 U. S. 390</a></span>; <i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191</a></span>; <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>; <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span>; <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>; <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55</a></span>; <i>Johnson</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="8920216"><a href="/opinion/8930122/johnson-v-pennsylvania/" aria-description="Citation for case: Johnson v. Pennsylvania">340 U. S. 881</a></span>; <i>Harris</i> v. <i>South Carolina,</i> <span class="citation" data-id="9420383"><a href="/opinion/104712/harris-v-south-carolina/" aria-description="Citation for case: Harris v. South Carolina">338 U. S. 68</a></span>; <i>Turner</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9420381"><a href="/opinion/104711/turner-v-pennsylvania/" aria-description="Citation for case: Turner v. Pennsylvania">338 U. S. 62</a></span>; <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49</a></span>; <i>Lee</i> v. <i>Mississippi,</i> <span class="citation" data-id="104497"><a href="/opinion/104497/lee-v-mississippi/" aria-description="Citation for case: Lee v. Mississippi">332 U. S. 742</a></span>; <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span>; <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Lyons</i> v. <i>Oklahoma,</i> <span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596</a></span>; <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>; <i>Vernon</i> v. <i>Alabama,</i> <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U. S. 547</a></span>; <i>Lomax</i> v. <i>Texas,</i> <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U. S. 544</a></span>; <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span>; <i>Canty</i> v. <i>Alabama,</i> <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U. S. 629</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>.</p>
<p>[3]  Medical reports from New York City's Fordham Hospital introduced by defendant showed that he had suffered a cerebral concussion in 1955. He was described by a private physician in 1951 as "an extremely nervous tense individual who is emotionally unstable and maladjusted," and was found unacceptable for military service in 1951, primarily because of "Psychiatric disorder." He failed the Army's AFQT-1 intelligence test. His mother had been in mental hospitals on three separate occasions.</p>
<p>[4]  His name is sometimes spelled "Hawks."</p>
<p>[5]  Although each is referred to separately in the record, it may be that Detectives Lehrer and Leira are the same person.</p>
<p>[6]  <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, is not to the contrary. There, while petitioner had already been arraigned on an incest charge, his later questioning and confession concerned a murder.</p>

</div>
```

---
