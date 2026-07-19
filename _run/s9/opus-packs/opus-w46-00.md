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

## GROUP: content/cases/Mancusi v. DeForte.md  (`case`, 5 assertions)

### content_page

```
---
title: "Mancusi v. DeForte"
type: case
citation: "392 U.S. 364 (1968)"
parallel_cite: "88 S. Ct. 2120; 20 L. Ed. 2d 1154; 68 L.R.R.M. (BNA) 2449"
neutral_cite: 1968 U.S. LEXIS 3075
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-17
docket: 844
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mancusi v. DeForte
  varies_by_point: false
  scope_note: "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/"
  cluster_id: 107745
  opinion_id: 107745
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Jones v. United States]]", "[[Katz v. United States]]", "[[Rakas v. Illinois]]", "[[O'Connor v. Ortega]]", "[[Minnesota v. Carter]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "workplace", "shared-office"]
holding: "A union official has Fourth Amendment standing to challenge a warrantless search of the office he shares with other officials, because capacity to claim the Amendment turns on a reasonable expectation of freedom from governmental intrusion in the area, not on a property right."
lake:
  record_id: Mancusi v. DeForte
  status: verified
  projected_at: 2026-07-09
---

# Mancusi v. DeForte

*392 U.S. 364 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DeForte, a vice president of a Teamsters local, was charged with conspiracy, coercion, and extortion. State officials, armed only with a district attorney's subpoena and no warrant, entered the single large office DeForte shared with other union officials and, over his objection, seized union records that were in his custody. The records were used to convict him. On [[Common Legal Terms#habeas-corpus|habeas]], he claimed the warrantless search violated his Fourth Amendment rights.

## Issue
Whether DeForte had [[Standing to Challenge a Search|Fourth Amendment standing]] to challenge the warrantless search and seizure of union records taken from the office he shared with other union officials.

## Rule
Standing turns on a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the area, not on ownership. "[C]apacity to claim the protection of the Amendment depends not upon a property right in the invaded place but upon whether the area was one in which there was a reasonable expectation of freedom from governmental intrusion." — 392 U.S. at 368 (citing *Katz v. United States*, 389 U.S. 347, 352). ^pin-368

"We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial." — [*Id.* at 369](https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/#:~:text=We%20hold%20that%20in%20these). ^pin-369

## Application
DeForte shared one large room with other union officials, spent considerable time there, and had custody of the records when they were seized. Even without a private office, "DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups." — [*Id.* at 369](https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/#:~:text=DeForte%20still%20could%20reasonably%20have). ^pin-369b

That expectation "was inevitably defeated by the entrance of state officials, their conduct of a general search, and their removal of records which were in DeForte's custody." Because he had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the shared office, he had standing; and the warrantless search on a bare DA subpoena was unreasonable.

## Conclusion
DeForte had [[Standing to Challenge a Search|Fourth Amendment standing]] and the search was unreasonable; the grant of [[Common Legal Terms#habeas-corpus|habeas corpus]] relief was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the result. *Mancusi* applies [[Katz v. United States]] to the standing question and relies on [[Jones v. United States]]'s loosening of the ownership requirement. [[Rakas v. Illinois]] (1978) abandoned the broad "legitimately on premises" formula and recast standing as a substantive expectation-of-privacy inquiry, but *Mancusi*'s holding that an employee can have a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a shared workplace endures and underlies [[O'Connor v. Ortega]]; cf. [[Minnesota v. Carter]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *Mancusi v. DeForte*, 392 U.S. 364 (1968) — https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/ — pinpoints: 368, 369.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f575dfe1e045c806", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "392 U.S. 364 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 3075", "official_citation_present": true, "parallel_cite": "88 S. Ct. 2120; 20 L. Ed. 2d 1154; 68 L.R.R.M. (BNA) 2449", "title": "Mancusi v. DeForte", "year": "1968"}}
{"assertion_id": "0cdf055a63486381", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A union official has Fourth Amendment standing to challenge a warrantless search of the office he shares with other officials, because capacity to claim the Amendment turns on a reasonable expectation of freedom from governmental intrusion in the area, not on a property right.", "title": "Mancusi v. DeForte"}}
{"assertion_id": "488ebbe51f1706c4", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny", "title": "Mancusi v. DeForte"}}
{"assertion_id": "9cd1d6e177ce638d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mancusi v. DeForte"}}
{"assertion_id": "dcb35a6fb1c6ba3c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mancusi v. DeForte", "field_i_validity": "good_law", "scope_note": "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result.", "title": "Mancusi v. DeForte", "varies_by_point": "false"}}
```

### lake record — Mancusi v. DeForte

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mancusi v. DeForte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mancusi v. DeForte",
    "case_name_short": "Mancusi",
    "case_name_full": "MANCUSI, WARDEN v. DeFORTE",
    "input_case_name": "Mancusi v. DeForte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-17",
    "year": 1968,
    "docket": "844",
    "cluster_id": 107745,
    "lead_opinion_id": 107745,
    "sibling_ids": [
      107745,
      9423796,
      9423797,
      9423798
    ],
    "absolute_url": "/opinion/107745/mancusi-v-deforte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8970275,
        "score": 20,
        "case_name": "Mancusi v. DeForte"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 364",
      "volume": "392",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 2120",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2120",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1154",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L.R.R.M. (BNA) 2449",
        "volume": "68",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2449",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 3075",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 364",
        "volume": "392",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 2120",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2120",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1154",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 3075",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L.R.R.M. (BNA) 2449",
        "volume": "68",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2449",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-368",
      "page": null,
      "quote": "--- # Mancusi v. DeForte *392 U.S. 364 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DeForte, a vice president of a Teamsters local, was charged with conspiracy, coercion, and extortion. State officials, armed only with a district attorney's subpoena and no warrant, entered the single large office DeForte shared with other union officials and, over his objection, seized union records that were in his custody. The records were used to convict him. On habeas, he claimed the warrantless search violated his Fourth Amendment rights. ## Issue Whether DeForte had Fourth Amendment standing to challenge the warrantless search and seizure of union records taken from the office he shared with other union officials. ## Rule Standing turns on a reasonable expectation of privacy in the area, not on ownership.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-369",
      "page": null,
      "quote": "We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial.",
      "star_marker": "369",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10264,
      "fragment": "#:~:text=We%20hold%20that%20in%20these",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-369b",
      "page": null,
      "quote": "DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups.",
      "star_marker": "369",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13112,
      "fragment": "#:~:text=DeForte%20still%20could%20reasonably%20have",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mancusi v. DeForte",
    "varies_by_point": false,
    "scope_note": "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Brian Ziegler",
          "cluster_id": 796647,
          "cite": [
            "474 F.3d 1184",
            "2007 U.S. App. LEXIS 1953",
            "2007 WL 222167"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grays v. State",
          "cluster_id": 5261713,
          "cite": [
            "905 S.W.2d 54",
            "1995 Tex. App. LEXIS 1833",
            "1995 WL 478381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Delgado, Dagoberto Silva, Henry Escobar",
          "cluster_id": 542046,
          "cite": [
            "903 F.2d 1495",
            "30 Fed. R. Serv. 1038",
            "1990 U.S. App. LEXIS 10078",
            "1990 WL 75081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schowengerdt v. General Dynamics Corp.",
          "cluster_id": 8961234,
          "cite": [
            "823 F.2d 1328",
            "2 I.E.R. Cas. (BNA) 545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Dale Dunn",
          "cluster_id": 454693,
          "cite": [
            "766 F.2d 880"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. McKeithen",
          "cluster_id": 107964,
          "cite": [
            "23 L. Ed. 2d 404",
            "89 S. Ct. 1843",
            "395 U.S. 411",
            "1969 U.S. LEXIS 3175",
            "71 L.R.R.M. (BNA) 2385"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cupp v. Murphy",
          "cluster_id": 108801,
          "cite": [
            "36 L. Ed. 2d 900",
            "93 S. Ct. 2000",
            "412 U.S. 291",
            "1973 U.S. LEXIS 63"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaufman v. United States",
          "cluster_id": 107874,
          "cite": [
            "22 L. Ed. 2d 227",
            "89 S. Ct. 1068",
            "394 U.S. 217",
            "1969 U.S. LEXIS 2158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul v. Oates",
          "cluster_id": 348314,
          "cite": [
            "560 F.2d 45",
            "1 Fed. R. Serv. 718",
            "1977 U.S. App. LEXIS 13091"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bliss v. Franco",
          "cluster_id": 167399,
          "cite": [
            "446 F.3d 1036",
            "64 Fed. R. Serv. 3d 781",
            "2006 U.S. App. LEXIS 10342",
            "2006 WL 1075595"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burton",
          "cluster_id": 2223932,
          "cite": [
            "848 N.E.2d 454",
            "6 N.Y.3d 584",
            "815 N.Y.S.2d 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lorenzana v. Superior Court",
          "cluster_id": 1183387,
          "cite": [
            "511 P.2d 33",
            "9 Cal. 3d 626",
            "108 Cal. Rptr. 585",
            "1973 Cal. LEXIS 214"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. United States",
          "cluster_id": 4497658,
          "cite": [
            "584 U.S. 395",
            "138 S. Ct. 1518",
            "200 L. Ed. 2d 805",
            "2018 U.S. LEXIS 2803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert G. Baker v. United States",
          "cluster_id": 281912,
          "cite": [
            "401 F.2d 958",
            "131 U.S. App. D.C. 7",
            "22 A.F.T.R.2d (RIA) 5342",
            "1968 U.S. App. LEXIS 5836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Alston",
          "cluster_id": 2283490,
          "cite": [
            "440 A.2d 1311",
            "88 N.J. 211",
            "1981 N.J. LEXIS 1677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMjU3MjgwMDAwMDAmcz0zNzcxNDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0zNjIyNzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
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
    "complete_query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
    "indexed_citing_opinions": 507,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107745,
        "count": 468,
        "count_source": "search"
      },
      {
        "opinion_id": 9423796,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9423797,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423798,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 745,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mancusi-v-deforte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQxODcwODgmcz03MzA2NzcwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107745,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 97431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 97758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 100203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 263829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 276492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 2443377,
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
    "date_created": "2026-07-05T11:31:25Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:35:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mancusi v. DeForte

```
<div>
<center><b><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U.S. 364</a></span> (1968)</b></center>
<center><h1>MANCUSI, WARDEN<br>
v.<br>
DeFORTE.</h1></center>
<center>No. 844.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 25, 1968.</center>
<center>Decided June 17, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Michael H. Rauch,</i> Assistant Attorney General of New York, argued the cause for petitioner. With him on the brief were <i>Louis J. Lefkowitz,</i> Attorney General, and <i>Samuel A. Hirshowitz,</i> First Assistant Attorney General.</p>
<p><span class="star-pagination">*365</span> <i>James L. Lekin</i> argued the cause and filed a brief for respondent.</p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>In 1959 the respondent, Frank DeForte, a vice president of Teamsters Union Local 266, was indicted in Nassau County, New York, on charges of conspiracy, coercion, and extortion, it being alleged that he had misused his union office to "organize" owners of juke boxes and compel them to pay tribute. Prior to the return of the indictment, the Nassau County District Attorney's office issued a subpoena <i>duces tecum</i> to Local 266, calling upon it to produce certain books and records. The subpoena was served upon the Union at its offices. When the Union refused to comply, the state officials who had served the subpoena conducted a search and seized union records from an office shared by DeForte and several other union officials. The search and seizure were without a warrant and took place despite the protests of DeForte, who was present in the office at the time. Over DeForte's objection, the seized material was admitted against him at trial. He was convicted.</p>
<p>On direct appeal to the New York courts,<sup>[1]</sup> DeForte unsuccessfully argued, <i>inter alia,</i> that the seized material was constitutionally inadmissible in state proceedings under the rule laid down in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, because the search and seizure occurred without a warrant.<sup>[2]</sup> DeForte subsequently brought a federal habeas <span class="star-pagination">*366</span> corpus proceeding, in which he made the same contention. The United States District Court for the Western District of New York denied the writ, <span class="citation" data-id="8756522"><a href="/opinion/8772945/united-states-ex-rel-deforte-v-mancusi/" aria-description="Citation for case: United States ex rel. DeForte v. Mancusi">261 F. Supp. 579</a></span>, but on appeal the Court of Appeals for the Second Circuit reversed and directed that the writ issue. <span class="citation" data-id="276492"><a href="/opinion/276492/united-states-of-america-ex-rel-frank-deforte-v-vincent-r-mancusi/" aria-description="Citation for case: United States of America Ex Rel. Frank Deforte v. Vincent...">379 F. 2d 897</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./390/903/">390 U. S. 903</a></span>, to consider the State's<sup>[3]</sup> contention that the Court of Appeals erred in upsetting this state conviction. Concluding that the Court of Appeals was right, we affirm.</p>
<p></p>
<h2>I.</h2>
<p>It is desirable at the outset to make clear what is and what is not involved in this case. The decision below was based solely upon a finding that DeForte's Fourth and Fourteenth Amendment rights, see <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30-34</a></span>, were violated by the search and seizure, and that the seized material was therefore inadmissible under <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i> It is on this ground alone that DeForte argues for affirmance. Consequently, there is no occasion to consider whether DeForte might successfully have asserted his Fifth Amendment right against self-incrimination with respect to the use against him of the seized records. Cf. <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/" aria-description="Citation for case: United States v. White">322 U. S. 694</a></span>; <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>. Nor is there any need to inquire whether DeForte could have asserted a Fourth or Fifth Amendment claim on behalf of the Union, for he did not do so. Moreover, this is not a case in which it is necessary to decide whether the traditional doctrine that Fourth Amendment rights "are personal rights, and . . . may be enforced by exclusion of evidence only at the instance of one whose own protection was infringed by the search and seizure," <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, at 389</a></span>, should be modified. Cf. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#390" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 390, n. 12</a></span>. For DeForte claims <span class="star-pagination">*367</span> that under the traditional rule he does have standing to challenge the admission against him at trial of union records seized from the office where he worked. The questions for decision, then, are whether DeForte has Fourth Amendment standing to object to the seizure of the records and, if so, whether the search was one prohibited by the Fourth Amendment.</p>
<p></p>
<h2>II.</h2>
<p>We deal, first, with the question of "standing." The Fourth Amendment guarantees that "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." The papers which were seized in this case belonged not to DeForte but to the Union. Hence, DeForte can have personal standing only if, as to him, the search violated the "right of the people to be secure in their . . . houses . . . ."<sup>[4]</sup> This Court has held that the word "houses," as it appears in the Amendment, is not to be taken literally, and that the protection of the Amendment may extend to commercial premises. See, <i>e. g., </i><i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>; <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>.</p>
<p>Furthermore, the Amendment does not shield only those who have title to the searched premises. It was <span class="star-pagination">*368</span> settled even before our decision in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, that one with a possessory interest in the premises might have standing. See, <i>e. g., </i><i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> even that requirement was loosened, and we held that "anyone legitimately on premises where a search occurs may challenge its legality . . . when its fruits are proposed to be used against him." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>.<sup>[5]</sup> The Court's recent decision in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, also makes it clear that capacity to claim the protection of the Amendment depends not upon a property right in the invaded place but upon whether the area was one in which there was a reasonable expectation of freedom from governmental intrusion. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S., at 352</a></span>. The crucial issue, therefore, is whether, in light of all the circumstances, DeForte's office was such a place.</p>
<p>The record reveals that the office where DeForte worked consisted of one large room, which he shared with several other union officials. The record does not show from what part of the office the records were taken, and DeForte does not claim that it was a part reserved for his exclusive personal use. The parties have stipulated that DeForte spent "a considerable amount of time" in <span class="star-pagination">*369</span> the office, and that he had custody of the papers at the moment of their seizure.<sup>[6]</sup></p>
<p>We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial. It has long been settled that one has standing to object to a search of his office, as well as of his home. See, <i>e. g., </i><i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>; <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; cf. <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>. Since the Court in <i>Jones</i> v. <i>United States, supra</i><i>,</i> explicitly did away with the requirement that to establish standing one must show legal possession or ownership of the searched premises, see <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#265" aria-description="Citation for case: Jones v. United States">362 U. S., at 265-267</a></span>, it seems clear that if DeForte had occupied a "private" office in the union headquarters, and union records had been seized from a desk or a filing cabinet in that office, he would have had standing. Cf. <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>. In such a "private" office, DeForte would have been entitled to expect that he would not be disturbed except by personal or business invitees, and that records would not be taken except with his permission or that of his union superiors. It seems to us that the situation was not fundamentally changed because DeForte shared an office with other union officers. DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups. This expectation was inevitably defeated by the entrance of state officials, their conduct of a general search, and their removal of records which were in DeForte's custody. It is, of course, irrelevant that the <span class="star-pagination">*370</span> Union or some of its officials might validly have consented to a search of the area where the records were kept, regardless of DeForte's wishes, for it is not claimed that any such consent was given, either expressly or by implication.</p>
<p>Our conclusion that DeForte had standing finds strong support in <i>Jones</i> v. <i>United States, supra</i><i>.</i> Jones was the occasional occupant of an apartment to which the owner had given him a key. The police searched the apartment while Jones was present, and seized narcotics which they found in a bird's nest in an awning outside a window. Thus, like DeForte, Jones was not the owner of the searched premises. Like DeForte, Jones had little expectation of absolute privacy, since the owner and those authorized by him were free to enter. There was no indication that the area of the apartment near the bird's nest had been set off for Jones' personal use, so that he might have expected more privacy there than in the rest of the apartment; in this, it was like the part of DeForte's office where the union records were kept. Hence, we think that our decision that Jones had standing clearly points to the result which we reach here.</p>
<p></p>
<h2>III.</h2>
<p>The remaining question is whether the search of DeForte's office was "unreasonable" within the meaning of the Fourth Amendment. The State does not deny that the search and seizure were without a warrant, and it is settled for purposes of the Amendment that "except in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' unless it has been authorized by a valid search warrant." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span>.<sup>[7]</sup> We <span class="star-pagination">*371</span> think it plain that the state officials' possession of a district attorney's subpoena of the kind involved here<sup>[8]</sup> does not bring this case within one of those "carefully defined classes." The State has not attempted to justify the search and seizure on that ground, and the New York courts have themselves said as a matter of state law that "[a district attorney's] subpoena duces tecum confers no right to seize the property referred to in the subpoena. . . ." <i>Amalgamated Union, Local 224</i> v. <i>Levine,</i> <span class="citation" data-id="6178892"><a href="/opinion/6310518/amalgamated-union-v-levine/#417" aria-description="Citation for case: Amalgamated Union v. Levine">31 Misc. 2d 416, 417</a></span>, 219 N. Y. S. 2d 851, 853.<sup>[9]</sup></p>
<p>Moreover, the subpoena involved here could not in any event qualify as a valid search warrant under the Fourth Amendment, for it was issued by the District Attorney himself,<sup>[10]</sup> and thus omitted the indispensable condition that "the inferences from the facts which lead to the complaint `. . . be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.' <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>." <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>. In <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, a corporate office was searched for papers which the corporation had refused to deliver in response to a New York District Attorney's subpoena, apparently similar to the one in this case. Speaking for the Court, Mr. Justice Holmes not only held that the seizure of the papers was unjustified but characterized it as "an outrage." <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States"><i>Id.,</i> at 391</a></span>. <span class="star-pagination">*372</span> The objections of both the corporation and the officer were sustained. Thus, there can be no doubt that under this Court's past decisions<sup>[11]</sup> the search of DeForte's office was "unreasonable" within the meaning of the Fourth Amendment.<sup>[12]</sup></p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACK, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p>Until this case was decided just now it has been the law in this country, since the federal Fourth Amendment exclusionary rule was adopted in 1914, that a defendant on trial for a crime has no standing or substantive right to object to the use of papers and documents against him on the ground that those papers, belonging to someone else, had been taken from the owner in violation of the Fourth Amendment. Heretofore successful objection to use of such papers as evidence has been left to the owner whose constitutional rights had been invaded. In <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>, decided in 1911, this Court in an exhaustive opinion by Mr. Justice Hughes, later Chief Justice, applied that principle by denying the benefit of the Fourth and Fifth Amendments to a corporate <span class="star-pagination">*373</span> officer, even one who had helped to prepare the corporate papers summoned to be produced.<sup>[1]</sup> In <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/" aria-description="Citation for case: United States v. White">322 U. S. 694</a></span>, decided in 1944, this Court applied the same principle in rejecting a claim of a union officer that the use of union papers and documents against him under a subpoena <i>duces tecum</i> would incriminate him. And indeed the Court in today creating its new rule is unable to cite a single previous opinion of this Court <i>holding</i> to the contrary.</p>
<p>In creating this new rule against the use of papers and documents which speak truthfully for themselves, the Court is putting up new hurdles and barriers bound to save many criminals from conviction. I should not object to this new rule, however, if I thought it was or could be justified by the Fourth or any other constitutional amendment. But I do not think it can. The exclusionary rule itself, even as it applies to the exclusion of the defendant's own property when illegally seized, has had only a precarious tenure in this Court. See <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); and my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span> (1961). I wish to repeat here what I have indicated before, that this seems to me a rather inopportune time to create a single rule more than the Constitution plainly requires to block conviction of guilty persons by keeping out probably the most reliable kind of evidence that can be offered.</p>
<p>A corporate or union official suffers no personal injury when the business office he occupies as an agent of the <span class="star-pagination">*374</span> corporation or union is invaded and when records he has prepared and safeguarded as an agent are seized. The invasion by the Government may disrupt the functioning of the office, prevent employees from performing their duties, and result in disclosure of business matters the company or union wished to keep secret. But all these are injuries only to the corporation or union as such. The organization has every right to challenge such intrusions whenever they occurif the seizure is illegal, the records obtained can be suppressed in a prosecution against the organization, and if no prosecution is initiated, the organization can obtain return of all the documents by bringing a civil action. See, <i>e. g., </i><i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931). Such intrusions, however, involve absolutely no invasion of the "personal privacy" or security of the agent or employee as an individual, and he accordingly has no right to seek suppression of records that the corporation or union itself has made no effort to regain.</p>
<p>The cases decided by this Court have, until today, uniformly supported this view and rejected the sweeping new exclusionary rule now advanced by the Court. Nor in my judgment does any one of the cases relied on by the Court provide support for its holding. The Court's basic premise is that if the union papers had been taken directly from a desk used by DeForte in a union office used only by him, his standing would have been clear, without regard to any other circumstances. I have found no past decision by this Court to that effect. Neither <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920), nor <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931), mentions the question of standing at all, and it is hard to see how the Court's inference can be drawn from these cases since in both the party seeking suppression of the documents was in fact the owner of <span class="star-pagination">*375</span> them. Although in <i>Silverthorne</i> the objections had been raised by both the corporation and one of its officers, standing was never even mentioned from the beginning to the end of the opinion, and the Court treated both parties as the "owners" of the documents. <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S., at 391</a></span>. Consequently, the Court's use of Mr. Justice Holmes' reference to "outrage" in no way supports the Court's holding today, directly or indirectly.</p>
<p><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), also fails to sustain the Court's position. In that case the petitioner had been arrested in a friend's apartment and was charged with possession of narcotics found there. This Court was troubled about the "dilemma" that would be created by requiring the petitioner, in order to secure suppression of the narcotics, to swear that they were taken from his possession, thus confessing his guilt of the very offense charged against him. To avoid this situation the Court held that petitioner could make his motion to suppress without swearing to possession, either because of the dilemma itself or because as a guest in the apartment he had the "legally requisite interest in the premises." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States">362 U. S., at 263</a></span>. The Court today puts great stress on the statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that "anyone legitimately on premises where a search occurs may challenge its legality . . . when its fruits are proposed to be used against him." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>. With deference I must point out that this sweeping dictum is taken somewhat out of context and cannot possibly have the literal meaning attributed to it. It would be quite a hyperbole, I think, to say that the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> opinion suggested that just any person who happened to be in a house against which an unreasonable search was perpetrated could ask to have all evidence obtained by that search excluded from evidence against him. As was asked by the court below, would that dictum enable a <span class="star-pagination">*376</span> janitor to escape the use of evidence illegally seized from his boss? The Court apparently recognizes this problem even now, for DeForte clearly was "legitimately on [the] premises" and thus his standing should be obvious, under its reading of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> without the Court's extended discussion of "reasonable expectation" and the related limiting tests. This reasoning in terms of "expectations," however, requires conferring standing without regard to whether the agent happens to be present at the time of the search or not, a rather remarkable consequence of the statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i> In fact the Court's opinion indicates to me that the Court is preparing the way to use <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> to eliminate entirely the requirement for standing to raise a search and seizure question and to permit a search to be challenged at any time, at any place, and under all circumstances, regardless of the defendant's relationship to the person or place searched or to the things seized. Any such step would elevate the Fourth Amendment to a position of importance far above that of any other constitutional provision, compare <i>Flast</i> v. <i>Cohen, ante,</i> p. 83, and would make it more difficult for the government to convict guilty persons who can make no claim to redress in any form since they suffered no invasion of any kind by the search itself. I would prefer to return to <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> itself, where we made quite clear throughout the opinion that while common-law concepts of property ownership were not controlling, standing was not automatically conferred on "anyone legitimately on [the] premises." We stressed:</p>
<blockquote>"In order to qualify as a `person aggrieved by an unlawful search and seizure' one must have been a victim of a search or seizure, one against whom the search was directed, as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>.</blockquote>
<p><span class="star-pagination">*377</span> In the present case I think it is entirely clear that the search was not "directed" against DeForte personally, but was addressed to and aimed at the Union and designed to secure from the Union papers belonging to the Union. The search occurred in a large room, which DeForte shared with a number of others, and the records were not taken from files and drawers used exclusively by him for his own private purposes. The police had been investigating a large conspiracy perpetrated through the Union and at the time were primarily interested in getting more information about the operation of the Union. The records taken were those that had been listed in a subpoena addressed to the Union itself, and since the Union had raised no objection to the subpoena, it was under a duty to turn over the records. Compare <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span> (1906).</p>
<p>Undoubtedly, I suppose, even if the Union's papers here should be returned either to the Union or to the defendant, the State could, on a new trial, summon the papers and get them and use them.<sup>[2]</sup> A rule which encourages such circumvention as that is hardly the kind of principle to which this great Court should give birth. I disclaim any responsibility whatever for the new rule.</p>
<p>MR. JUSTICE WHITE, dissenting.</p>
<p>Although the Fourth Amendment perhaps protects the individual's private desk in a union office shared with other officers or employees, I dissent from the Court's extension of the protected area to the office door.</p>
<h2>NOTES</h2>
<p>[1]  Those appeals culminated in a petition for certiorari to this Court, which was denied <i>sub nom. De Grandis</i> v. <i>New York,</i> <span class="citation" data-id="8947816"><a href="/opinion/8956781/de-grandis-v-new-york/" aria-description="Citation for case: De Grandis v. New York">375 U. S. 868</a></span>.</p>
<p>[2]  DeForte's petition for certiorari following direct appeal was denied in 1963, more than two years after the Court's decision in <i>Mapp</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span></i><i>.</i> Under the rule laid down in <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>, DeForte is entitled to invoke the exclusionary principle established in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i> See <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 622</a></span> and n. 5.</p>
<p>[3]  The petitioner, Mancusi, is the warden of the New York State prison in which DeForte is confined.</p>
<p>[4]  The fact that the seized papers belonged to the Union does not imply of itself that an individual could never have personal standing to object to their admission against him. For example, state officers conceivably might have seized the papers during a search of DeForte's home, and in that event we think it clear that he would have had standing. <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>, is by no means to the contrary, for in that case there was no physical search at all. The only Fourth Amendment standing question in <i><span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">Wilson</a></span></i> was whether a corporate officer had personal standing to object to a subpoena <i>duces tecum</i> addressed to the corporation, on the ground that it was overbroad. See <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/#375" aria-description="Citation for case: Wilson v. United States">221 U. S., at 375-376</a></span>.</p>
<p>[5]  The petitioner contends that this holding was not intended to have general application, but that it was devised solely to solve the particular dilemma presented in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>:</i> that of a defendant who was charged with a possessory offense and consequently might have to concede his guilt in order to establish standing in the usual way. However, this limited reading of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> overlooks the fact that in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> standing was held to exist on two distinct grounds: "(1) [The circumstance that] possession both convicts and confers standing, eliminates any necessity for a preliminary showing of an interest in the premises searched or the property seized . . . . (2) <i>Even were this not a prosecution turning on illicit possession,</i> the legally requisite interest in the premises was here satisfied . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States">362 U. S., at 263</a></span>. (Emphasis added.) Thus, the second branch of the holding, with which we are here concerned, was explicitly stated to be of general effect.</p>
<p>[6]  See Joint Appendix 51-52.</p>
<p>[7]  See also <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.</p>
<p>[8]  A copy of the subpoena appears in the Joint Appendix, at 22. The subpoena was signed by the District Attorney and directed to the Union as a witness in a criminal action. It ordered the Union to appear before the District Attorney forthwith, and to bring with it specified union records. The subpoena appears to have been issued under the authority of N. Y. Code Crim. Proc. §§ 609-613.</p>
<p>[9]  See also <i>In re Atlas Lathing Corp.,</i> <span class="citation" data-id="5426289"><a href="/opinion/5584153/atlas-lathing-corp-v-bennett/" aria-description="Citation for case: Atlas Lathing Corp. v. Bennett">176 Misc. 959</a></span>, 29 N. Y. S. 2d 458; Hagan, Impounding and the Subpoena Duces Tecum, 26 Brooklyn L. Rev. 199, 210-211 (1960).</p>
<p>[10]  See n. 8, <i>supra.</i></p>
<p>[11]  The Court's opinion in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>, does contain dicta to the effect that there is a lesser right to privacy when government officials have a "right" to inspect the seized items. See, <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States"><i>e. g., id.,</i> at 593</a></span>. However, the only holding in <i><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">Davis</a></span></i> was that there had been a valid consent to the search; the case "did not involve a search warrant issue." <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#545" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 545, n. 7</a></span>.</p>
<p>[12]  It is, of course, immaterial that the State might have been able to obtain the same papers by means which did not violate the Fourth Amendment. As Mr. Justice Holmes stated in <i>Silverthorne Lumber Co.</i> v. <i>United States, supra,</i> at 392: "[T]he rights . . . against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way."</p>
<p>[1]  See also <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span> (1906); <i>Grant</i> v. <i>United States,</i> <span class="citation" data-id="97758"><a href="/opinion/97758/grant-v-united-states/" aria-description="Citation for case: Grant v. United States">227 U. S. 74</a></span> (1913); <i>Essgee Co.</i> v. <i>United States,</i> <span class="citation" data-id="100203"><a href="/opinion/100203/essgee-co-of-china-v-united-states/" aria-description="Citation for case: Essgee Co. of China v. United States">262 U. S. 151</a></span> (1923); <i>Goldstein</i> v. <i>United States,</i> <span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span> (1942); <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span> (1946); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <i>Wild</i> v. <i>Brewer,</i> <span class="citation" data-id="9449961"><a href="/opinion/263829/albert-j-wild-v-bennett-y-brewer-revenue-agent-of-the-internal-revenue/" aria-description="Citation for case: Albert J. Wild v. Bennett Y. Brewer, Revenue Agent of the...">329 F. 2d 924</a></span> (C. A. 9th Cir. 1964).</p>
<p>[2]  Since the State had obtained a subpoena for these documents even before the search, the new subpoena would not be an invalid "fruit" of the illegal seizure. Compare <i><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">Silverthorne, supra</a></span></i><i>.</i></p>

</div>
```

---

## GROUP: content/cases/Marshall v. Barlow's Inc.md  (`case`, 5 assertions)

### content_page

```
---
title: "Marshall v. Barlow's, Inc."
type: case
citation: "436 U.S. 307 (1978)"
parallel_cite: "98 S. Ct. 1816; 56 L. Ed. 2d 305; 8 Envtl. L. Rep. (Envtl. Law Inst.) 20434; 6 OSHC (BNA) 1571"
neutral_cite: 1978 U.S. LEXIS 26
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-05-23
docket: 76-1143
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-05-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Marshall v. Barlow's, Inc."
  varies_by_point: false
  scope_note: "Good law. OSHA § 8(a)'s warrantless-inspection authorization held unconstitutional; the administrative-warrant requirement for ordinary workplaces stands."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109866/marshall-v-barlows-inc/"
  cluster_id: 109866
  opinion_id: 109866
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Progeny (workplace inspections)"
related: ["[[See v. City of Seattle]]", "[[Camara v. Municipal Court]]", "[[Donovan v. Dewey]]", "[[United States v. Biswell]]"]
aliases: ["Marshall v. Barlow's"]
tags: ["case", "fourth-amendment", "administrative-search", "inspections", "OSHA", "workplace", "warrant"]
holding: "OSHA's authorization of warrantless workplace inspections is unconstitutional; a nonconsensual inspection of an ordinary business generally requires an administrative warrant, unless the pervasively-regulated-industry exception applies."
lake:
  record_id: "Marshall v. Barlow's Inc"
  status: verified
  projected_at: 2026-07-09
---

# Marshall v. Barlow's, Inc.

*436 U.S. 307 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An OSHA inspector arrived at Barlow's, Inc., an electrical and plumbing business in Idaho, to inspect the nonpublic work area for safety violations. There was no complaint; the firm had simply come up in OSHA's selection process. The owner asked whether the inspector had a warrant; he had none, so the owner refused entry, invoking the Fourth Amendment. Section 8(a) of the Occupational Safety and Health Act purported to authorize such inspections without any warrant.

## Issue
Whether OSHA may constitutionally authorize warrantless inspections of the nonpublic areas of an employer's premises over the employer's objection.

## Rule
No. "The Warrant Clause of the Fourth Amendment protects commercial buildings as well as private homes." — 436 U.S. at 311. ^pin-311

Following *[[Camara v. Municipal Court|Camara]]* and [[See v. City of Seattle]], "unless some recognized exception to the warrant requirement applies, *See v. Seattle* would require a warrant to conduct the inspection sought in this case." — *Id.* at 313. ^pin-313

The Secretary's enforcement concerns "do not suffice to justify warrantless inspections under OSHA or vitiate the general constitutional requirement that for a search to be reasonable a warrant must be obtained." — [*Id.* at 324](https://www.courtlistener.com/opinion/109866/marshall-v-barlows-inc/#:~:text=do%20not%20suffice%20to%20justify). ^pin-324

"We hold that Barlow's was entitled to a declaratory judgment that the Act is unconstitutional insofar as it purports to authorize inspections without warrant or its equivalent." — *Id.* at 325. ^pin-325

## Application
Barlow's was an ordinary electrical and plumbing business, not a member of a pervasively regulated industry of the *Colonnade*/[[United States v. Biswell]] kind, so no warrant exception applied. The Court rejected the Secretary's claim that warrantless inspections were essential to OSHA enforcement, noting an inspection warrant need not rest on traditional criminal probable cause — a showing of specific evidence of a violation **or** reasonable administrative/legislative standards for selecting the premises would support it. Because § 8(a) dispensed with even that, the warrantless-inspection scheme was unconstitutional and the injunction was proper.

## Conclusion
OSHA's warrantless-inspection provision was unconstitutional; the declaratory judgment and injunction for Barlow's were affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Barlow's* confirms that ordinary workplaces enjoy the *[[Camara v. Municipal Court|Camara]]*/*See* administrative-warrant rule, while expressly preserving the **pervasively-regulated-industry exception** later applied in [[Donovan v. Dewey]] (mines), [[United States v. Biswell]] (firearms), and *[[New York v. Burger]]* (auto dismantlers).

## Appears on
- [[Special Needs and Administrative Searches]] — *Progeny (workplace inspections)*

## Sources
- *Marshall v. Barlow's, Inc.*, 436 U.S. 307 (1978) — https://www.courtlistener.com/opinion/109866/marshall-v-barlows-inc/ — pinpoints: 311, 313, 324, 325.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "116fb4eb7ba5f11c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "436 U.S. 307 (1978)", "court": "U.S. Supreme Court", "neutral_cite": "1978 U.S. LEXIS 26", "official_citation_present": true, "parallel_cite": "98 S. Ct. 1816; 56 L. Ed. 2d 305; 8 Envtl. L. Rep. (Envtl. Law Inst.) 20434; 6 OSHC (BNA) 1571", "title": "Marshall v. Barlow's, Inc.", "year": "1978"}}
{"assertion_id": "8ea1e12cd1430f4d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "OSHA's authorization of warrantless workplace inspections is unconstitutional; a nonconsensual inspection of an ordinary business generally requires an administrative warrant, unless the pervasively-regulated-industry exception applies.", "title": "Marshall v. Barlow's, Inc."}}
{"assertion_id": "e2d6fc3ab3723b88", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Progeny (workplace inspections)", "title": "Marshall v. Barlow's, Inc."}}
{"assertion_id": "795fecb23f7fc1e3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1978-05-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Marshall v. Barlow's, Inc.", "field_i_validity": "good_law", "scope_note": "Good law. OSHA § 8(a)'s warrantless-inspection authorization held unconstitutional; the administrative-warrant requirement for ordinary workplaces stands.", "title": "Marshall v. Barlow's, Inc.", "varies_by_point": "false"}}
{"assertion_id": "98dde4194cb14c5a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Marshall v. Barlow's, Inc."}}
```

### lake record — Marshall v. Barlow's Inc

```json
{
  "schema_version": "s2.v1",
  "record_id": "Marshall v. Barlow's Inc",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Marshall v. Barlow's, Inc.",
    "case_name_short": "Marshall",
    "case_name_full": "MARSHALL, SECRETARY OF LABOR, Et Al. v. BARLOW\u2019S, INC.",
    "input_case_name": "Marshall v. Barlow's, Inc.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-05-23",
    "year": 1978,
    "docket": "76-1143",
    "cluster_id": 109866,
    "lead_opinion_id": 109866,
    "sibling_ids": [
      109866,
      9427200,
      9427201
    ],
    "absolute_url": "/opinion/109866/marshall-v-barlows-inc/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 307",
      "volume": "436",
      "reporter": "U.S.",
      "page": "307",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 1816",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1816",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 305",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
        "volume": "8",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20434",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 OSHC (BNA) 1571",
        "volume": "6",
        "reporter": "OSHC (BNA)",
        "page": "1571",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 26",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "26",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 307",
        "volume": "436",
        "reporter": "U.S.",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 1816",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1816",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 305",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 26",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "26",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
        "volume": "8",
        "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)",
        "page": "20434",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 OSHC (BNA) 1571",
        "volume": "6",
        "reporter": "OSHC (BNA)",
        "page": "1571",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 307",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 307",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-311",
      "page": null,
      "quote": "--- # Marshall v. Barlow's, Inc. *436 U.S. 307 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An OSHA inspector arrived at Barlow's, Inc., an electrical and plumbing business in Idaho, to inspect the nonpublic work area for safety violations. There was no complaint; the firm had simply come up in OSHA's selection process. The owner asked whether the inspector had a warrant; he had none, so the owner refused entry, invoking the Fourth Amendment. Section 8(a) of the Occupational Safety and Health Act purported to authorize such inspections without any warrant. ## Issue Whether OSHA may constitutionally authorize warrantless inspections of the nonpublic areas of an employer's premises over the employer's objection. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-313",
      "page": null,
      "quote": "unless some recognized exception to the warrant requirement applies, *See v. Seattle* would require a warrant to conduct the inspection sought in this case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-324",
      "page": null,
      "quote": "do not suffice to justify warrantless inspections under OSHA or vitiate the general constitutional requirement that for a search to be reasonable a warrant must be obtained.",
      "star_marker": "324",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 25894,
      "fragment": "#:~:text=do%20not%20suffice%20to%20justify",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-325",
      "page": null,
      "quote": "We hold that Barlow's was entitled to a declaratory judgment that the Act is unconstitutional insofar as it purports to authorize inspections without warrant or its equivalent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-05-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Marshall v. Barlow's, Inc.",
    "varies_by_point": false,
    "scope_note": "Good law. OSHA \u00a7 8(a)'s warrantless-inspection authorization held unconstitutional; the administrative-warrant requirement for ordinary workplaces stands.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cardenas-Alatorre",
          "cluster_id": 169200,
          "cite": [
            "485 F.3d 1111",
            "2007 U.S. App. LEXIS 10876",
            "2007 WL 1334511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Schofner",
          "cluster_id": 1473736,
          "cite": [
            "800 A.2d 1072",
            "174 Vt. 430",
            "2002 Vt. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3262306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane1_negative"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Steagald v. United States",
          "cluster_id": 110464,
          "cite": [
            "68 L. Ed. 2d 38",
            "101 S. Ct. 1642",
            "451 U.S. 204",
            "1981 U.S. LEXIS 89",
            "49 U.S.L.W. 4418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browning-Ferris Industries of Vermont, Inc. v. Kelco Disposal, Inc.",
          "cluster_id": 112324,
          "cite": [
            "106 L. Ed. 2d 219",
            "109 S. Ct. 2909",
            "492 U.S. 257",
            "1989 U.S. LEXIS 3285",
            "57 U.S.L.W. 4985"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dolan v. City of Tigard",
          "cluster_id": 117861,
          "cite": [
            "129 L. Ed. 2d 304",
            "114 S. Ct. 2309",
            "512 U.S. 374",
            "1994 U.S. LEXIS 4826"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
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
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lo-Ji Sales, Inc. v. New York",
          "cluster_id": 110100,
          "cite": [
            "60 L. Ed. 2d 920",
            "99 S. Ct. 2319",
            "442 U.S. 319",
            "1979 U.S. LEXIS 107",
            "5 Media L. Rep. (BNA) 1177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dalia v. United States",
          "cluster_id": 110061,
          "cite": [
            "60 L. Ed. 2d 177",
            "99 S. Ct. 1682",
            "441 U.S. 238",
            "1979 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlos Botero-Ospina",
          "cluster_id": 709242,
          "cite": [
            "71 F.3d 783",
            "1995 U.S. App. LEXIS 34347",
            "1995 WL 723102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villamonte-Marquez",
          "cluster_id": 110973,
          "cite": [
            "77 L. Ed. 2d 22",
            "103 S. Ct. 2573",
            "462 U.S. 579",
            "1983 U.S. LEXIS 68",
            "51 U.S.L.W. 4812"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marshall v. Barlow's Inc:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109866 OR 9427200 OR 9427201) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04ODgyNzg0MDAwMDAmcz0xMDY3MDYyJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109866+OR+9427200+OR+9427201%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109866 OR 9427200 OR 9427201)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDAmcz03NjYxMjImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109866+OR+9427200+OR+9427201%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109866 OR 9427200 OR 9427201)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 0,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109866 OR 9427200 OR 9427201)",
    "indexed_citing_opinions": 946,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109866,
        "count": 854,
        "count_source": "search"
      },
      {
        "opinion_id": 9427200,
        "count": 122,
        "count_source": "search"
      },
      {
        "opinion_id": 9427201,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1429,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/marshall-v-barlow-s-inc.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0MDIzMDQmcz01MDkxMTIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109866+OR+9427200+OR+9427201%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109866,
        "cited_id": 104130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 105389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109866,
        "cited_id": 340592,
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
    "date_created": "2026-07-05T11:46:11Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:46:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:46:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:48:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:46:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Marshall v. Barlow's Inc

```
<div>
<center><b><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U.S. 307</a></span> (1978)</b></center>
<center><h1>MARSHALL, SECRETARY OF LABOR, ET AL.<br>
v.<br>
BARLOW'S, INC.</h1></center>
<center>No. 76-1143.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 9, 1978.</center>
<center>Decided May 23, 1978.</center>
APPEAL FROM THE UNITED STATES DISTRICT COURT FOR THE DISTRICT OF IDAHO
<p><span class="star-pagination">*308</span> <i>Solicitor General McCree</i> argued the cause for appellants. With him on the briefs were <i>Deputy Solicitor General Wallace, Stuart A. Smith,</i> and <i>Michael H. Levin.</i></p>
<p><i>John L. Runft</i> argued the cause for appellee. With him on the brief was <i>Iver J. Longeteig.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*309</span> MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>Section 8 (a) of the Occupational Safety and Health Act of 1970 (OSHA or Act)<sup>[1]</sup> empowers agents of the Secretary of Labor (Secretary) to search the work area of any employment facility within the Act's jurisdiction. The purpose of the search is to inspect for safety hazards and violations of OSHA regulations. No search warrant or other process is expressly required under the Act.</p>
<p>On the morning of September 11, 1975, an OSHA inspector entered the customer service area of Barlow's, Inc., an electrical and plumbing installation business located in Pocatello, Idaho. The president and general manager, Ferrol G. "Bill" Barlow, was on hand; and the OSHA inspector, after showing his credentials,<sup>[2]</sup> informed Mr. Barlow that he wished to conduct <span class="star-pagination">*310</span> a search of the working areas of the business. Mr. Barlow inquired whether any complaint had been received about his company. The inspector answered no, but that Barlow's, Inc., had simply turned up in the agency's selection process. The inspector again asked to enter the nonpublic area of the business; Mr. Barlow's response was to inquire whether the inspector had a search warrant. The inspector had none. Thereupon, Mr. Barlow refused the inspector admission to the employee area of his business. He said he was relying on his rights as guaranteed by the Fourth Amendment of the United States Constitution.</p>
<p>Three months later, the Secretary petitioned the United States District Court for the District of Idaho to issue an order compelling Mr. Barlow to admit the inspector.<sup>[3]</sup> The requested order was issued on December 30, 1975, and was presented to Mr. Barlow on January 5, 1976. Mr. Barlow again refused admission, and he sought his own injunctive relief against the warrantless searches assertedly permitted by OSHA. A three-judge court was convened. On December 30, 1976, it ruled in Mr. Barlow's favor. <span class="citation" data-id="1444752"><a href="/opinion/1444752/barlows-inc-v-usery/" aria-description="Citation for case: Barlow&#x27;s, Inc. v. Usery">424 F. Supp. 437</a></span>. Concluding that <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967), and <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 543</a></span> (1967), controlled this case, the court held that the Fourth Amendment required a warrant for the type of search involved here<sup>[4]</sup> and that the statutory authorization for warrantless inspections was unconstitutional. An injunction against searches or inspections pursuant to § 8 (a) was entered. The Secretary appealed, challenging the judgment, and we noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./430/964/">430 U. S. 964</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*311</span> I</h2>
<p>The Secretary urges that warrantless inspections to enforce OSHA are reasonable within the meaning of the Fourth Amendment. Among other things, he relies on § 8 (a) of the Act, <span class="citation no-link">29 U. S. C. § 657</span> (a), which authorizes inspection of business premises without a warrant and which the Secretary urges represents a congressional construction of the Fourth Amendment that the courts should not reject. Regrettably, we are unable to agree.</p>
<p>The Warrant Clause of the Fourth Amendment protects commercial buildings as well as private homes. To hold otherwise would belie the origin of that Amendment, and the American colonial experience. An important forerumier of the first 10 Amendments to the United States Constitution, the Virginia Bill of Rights, specifically opposed "general warrants, whereby an officer or messenger may be commanded to search suspected places without evidence of a fact committed."<sup>[5]</sup> The general warrant was a recurring point of contention in the Colonies immediately preceding the Revolution.<sup>[6]</sup> The particular offensiveness it engendered was acutely felt by the merchants and businessmen whose premises and products were inspected for compliance with the several parliamentary revenue measures that most irritated the colonists.<sup>[7]</sup> "[T]he Fourth Amendment's commands grew in large measure out of the colonists' experience with the writs of assistance. . . [that] granted sweeping power to customs officials and other agents of the King to search at large for smuggled goods." <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977). <span class="star-pagination">*312</span> See also <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#355" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 355</a></span> (1977). Against this background, it is untenable that the ban on warrantless searches was not intended to shield places of business as well as of residence.</p>
<p>This Court has already held that warrantless searches are generally unreasonable, and that this rule applies to commercial premises as well as homes. In <i>Camara</i> v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Municipal Court, supra,</i> at 528-529</a></span>, we held:</p>
<blockquote>"[E]xcept in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' unless it has been authorized by a valid search warrant."</blockquote>
<p>On the same day, we also ruled:</p>
<blockquote>"As we explained in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i> a search of private houses is presumptively unreasonable if conducted without a warrant. The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property. The businessman, too, has that right placed in jeopardy if the decision to enter and inspect for violation of regulatory laws can be made and enforced by the inspector in the field without official authority evidenced by a warrant." <i>See</i> v. <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle"><i>Seattle, supra,</i> at 543</a></span>.</blockquote>
<p>These same cases also held that the Fourth Amendment prohibition against unreasonable searches protects against warrantless intrusions during civil as well as criminal investigations. <i><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Ibid.</a></span></i> The reason is found in the "basic purpose of this Amendment . . . [which] is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 528</a></span>. If the government intrudes on a person's property, the privacy interest suffers whether the government's motivation is to investigate violations of criminal laws or breaches of other statutory or <span class="star-pagination">*313</span> regulatory standards. It therefore appears that unless some recognized exception to the warrant requirement applies, <i>See</i> v. <i><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Seattle</a></span></i> would require a warrant to conduct the inspection sought in this case.</p>
<p>The Secretary urges that an exception from the search warrant requirement has been recognized for "pervasively regulated business[es]," <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316</a></span> (1972), and for "closely regulated" industries "long subject to close supervision and inspection." <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#74" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72, 74, 77</a></span> (1970). These cases are indeed exceptions, but they represent responses to relatively unique circumstances. Certain industries have such a history of government oversight that no reasonable expectation of privacy, see <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351-352</a></span> (1967), could exist for a proprietor over the stock of such an enterprise. Liquor (<i>Colonnade</i>) and firearms (<span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell"><i>Biswell</i></a></span>) are industries of this type; when an entrepreneur embarks upon such a business, he has voluntarily chosen to subject himself to a full arsenal of governmental regulation.</p>
<p>Industries such as these fall within the "certain carefully defined classes of cases," referenced in <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. The element that distinguishes these enterprises from ordinary businesses is a long tradition of close government supervision, of which any person who chooses to enter such a business must already be aware. "A central difference between those cases <i>[Colonnade</i> and <i>Biswell]</i> and this one is that businessmen engaged in such federally licensed and regulated enterprises accept the burdens as well as the benefits of their trade, whereas the petitioner here was not engaged in any regulated or licensed business. The businessman in a regulated industry in effect consents to the restrictions placed upon him." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#271" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 271</a></span> (1973).</p>
<p>The clear import of our cases is that the closely regulated industry of the type involved in <i>Colonnade</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> is the exception. The Secretary would make it the rule. Invoking <span class="star-pagination">*314</span> the Walsh-Healey Act of 1936, <span class="citation no-link">41 U. S. C. § 35</span> <i>et seq.,</i> the Secretary attempts to support a conclusion that all businesses involved in interstate commerce have long been subjected to close supervision of employee safety and health conditions. But the degree of federal involvement in employee working circumstances has never been of the order of specificity and pervasiveness that OSHA mandates. It is quite unconvincing to argue that the imposition of minimum wages and maximum hours on employers who contracted with the Government under the Walsh-Healey Act prepared the entirety of American interstate commerce for regulation of working conditions to the minutest detail. Nor can any but the most fictional sense of voluntary consent to later searches be found in the single fact that one conducts a business affecting interstate commerce; under current practice and law, few businesses can be conducted without having some effect on interstate commerce.</p>
<p>The Secretary also attempts to derive support for a <i>Colonnade-Biswell-type</i> exception by drawing analogies from the field of labor law. In <i>Republic Aviation Corp.</i> v. <i>NLRB,</i> <span class="citation" data-id="104130"><a href="/opinion/104130/republic-aviation-corp-v-national-labor-relations-board/" aria-description="Citation for case: Republic Aviation Corp. v. National Labor Relations Board">324 U. S. 793</a></span> (1945), this Court upheld the rights of employees to solicit for a union during nonworking time where efficiency was not compromised. By opening up his property to employees, the employer had yielded so much of his private property rights as to allow those employees to exercise § 7 rights under the National Labor Relations Act. But this Court also held that the private property rights of an owner prevailed over the intrusion of nonemployee organizers, even in nonworking areas of the plant and during nonworking hours. <i>NLRB</i> v. <i>Babcock &amp; Wilcox Co.,</i> <span class="citation" data-id="105389"><a href="/opinion/105389/national-labor-relations-board-v-babcock-wilcox-co/" aria-description="Citation for case: National Labor Relations Board v. Babcock &amp; Wilcox Co.">351 U. S. 105</a></span> (1956).</p>
<p>The critical fact in this case is that entry over Mr. Barlow's objection is being sought by a Government agent.<sup>[8]</sup> Employees <span class="star-pagination">*315</span> are not being prohibited from reporting OSHA violations. What they observe in their daily functions is undoubtedly beyond the employer's reasonable expectation of privacy. The Government inspector, however, is not an employee. Without a warrant he stands in no better position than a member of the public. What is observable by the public is observable, without a warrant, by the Government inspector as well.<sup>[9]</sup> The owner of a business has not, by the necessary utilization of employees in his operation, thrown open the areas where employees alone are permitted to the warrantless scrutiny of Government agents. That an employee is free to report, and the Government is free to use, any evidence of noncompliance with OSHA that the employee observes furnishes no justification for federal agents to enter a place of business from which the public is restricted and to conduct their own warrantless search.<sup>[10]</sup></p>
<p></p>
<h2>II</h2>
<p>The Secretary nevertheless stoutly argues that the enforcement scheme of the Act requires warrantless searches, and that the restrictions on search discretion contained in the Act and its regulations already protect as much privacy as a warrant would. The Secretary thereby asserts the actual reasonableness of OSHA searches, whatever the general rule against warrantless searches might be. Because "reasonableness is still the ultimate standard," <i>Camara</i> v. <i>Municipal</i> <span class="star-pagination">*316</span> <i>Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 539</a></span>, the Secretary suggests that the Court decide whether a warrant is needed by arriving at a sensible balance between the administrative necessities of OSHA inspections and the incremental protection of privacy of business owners a warrant would afford. He suggests that only a decision exempting OSHA inspections from the Warrant Clause would give "full recognition to the competing public and private interests here at stake." <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Ibid.</a></span></i></p>
<p>The Secretary submits that warrantless inspections are essential to the proper enforcement of OSHA because they afford the opportunity to inspect without prior notice and hence to preserve the advantages of surprise. While the dangerous conditions outlawed by the Act include structural defects that cannot be quickly hidden or remedied, the Act also regulates a myriad of safety details that may be amenable to speedy alteration or disguise. The risk is that during the interval between an inspector's initial request to search a plant and his procuring a warrant following the owner's refusal of permission, violations of this latter type could be corrected and thus escape the inspector's notice. To the suggestion that warrants may be issued <i>ex parte</i> and executed without delay and without prior notice, thereby preserving the element of surprise, the Secretary expresses concern for the administrative strain that would be experienced by the inspection system, and by the courts, should <i>ex parte</i> warrants issued in advance become standard practice.</p>
<p>We are unconvinced, however, that requiring warrants to inspect will impose serious burdens on the inspection system or the courts, will prevent inspections necessary to enforce the statute, or will make them less effective. In the first place, the great majority of businessmen can be expected in normal course to consent to inspection without warrant; the Secretary has not brought to this Court's attention any widespread pattern of refusal.<sup>[11]</sup> In those cases where an owner does insist <span class="star-pagination">*317</span> on a warrant, the Secretary argues that inspection efficiency will be impeded by the advance notice and delay. The Act's penalty provisions for giving advance notice of a search, <span class="citation no-link">29 U. S. C. § 666</span> (f), and the Secretary's own regulations, <span class="citation no-link">29 CFR § 1903.6</span> (1977), indicate that surprise searches are indeed contemplated. However, the Secretary has also promulgated a regulation providing that upon refusal to permit an inspector to enter the property or to complete his inspection, the inspector shall attempt to ascertain the reasons for the refusal and report to his superior, who shall "promptly take appropriate action, including compulsory process, if necessary." <span class="citation no-link">29 CFR § 1903.4</span> (1977).<sup>[12]</sup> The regulation represents a choice to proceed <span class="star-pagination">*318</span> by process where entry is refused; and on the basis of evidence available from present practice, the Act's effectiveness has not been crippled by providing those owners who wish to refuse an initial requested entry with a time lapse while the inspector obtains the necessary process.<sup>[13]</sup> Indeed, the kind of process sought in this case and apparently anticipated by the regulation provides notice to the business operator.<sup>[14]</sup><span class="star-pagination">*319</span> If this safeguard endangers the efficient administration of OSHA, the Secretary should never have adopted it, particularly when the Act does not require it. Nor is it immediately <span class="star-pagination">*320</span> apparent why the advantages of surprise would be lost if, after being refused entry, procedures were available for the Secretary to seek an <i>ex parte</i> warrant and to reappear at the premises without further notice to the establishment being inspected.<sup>[15]</sup></p>
<p>Whether the Secretary proceeds to secure a warrant or other process, with or without prior notice, his entitlement to inspect will not depend on his demonstrating probable cause to believe that conditions in violation of OSHA exist on the premises. Probable cause in the criminal law sense is not required. For purposes of an administrative search such as this, probable cause justifying the issuance of a warrant may be based not only on specific evidence of an existing violation<sup>[16]</sup> but also on a showing that "reasonable legislative or administrative standards for conducting an . . . inspection are satisfied with respect to a particular [establishment] ." <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> <span class="star-pagination">*321</span> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>. A warrant showing that a specific business has been chosen for an OSHA search on the basis of a general administrative plan for the enforcement of the Act derived from neutral sources such as, for example, dispersion of employees in various types of industries across a given area, and the desired frequency of searches in any of the lesser divisions of the area, would protect an employer's Fourth Amendment rights.<sup>[17]</sup> We doubt that the consumption of enforcement energies in the obtaining of such warrants will exceed manageable proportions.</p>
<p>Finally, the Secretary urges that requiring a warrant for OSHA inspectors will mean that, as a practical matter, warrantless-search provisions in other regulatory statutes are also constitutionally infirm. The reasonableness of a warrantless search, however, will depend upon the specific enforcement needs and privacy guarantees of each statute. Some of the statutes cited apply only to a single industry, where regulations might already be so pervasive that a <i>Colonnade-Biswell</i> exception to the warrant requirement could apply. Some statutes already envision resort to federal-court enforcement when entry is refused, employing specific language in some cases<sup>[18]</sup> and general language in others.<sup>[19]</sup> In short, we base <span class="star-pagination">*322</span> today's opinion on the facts and law concerned with OSHA and do not retreat from a holding appropriate to that statute because of its real or imagined effect on other, different administrative schemes.</p>
<p>Nor do we agree that the incremental protections afforded the employer's privacy by a warrant are so marginal that they fail to justify the administrative burdens that may be entailed. <span class="star-pagination">*323</span> The authority to make warrantless searches devolves almost unbridled discretion upon executive and administrative officers, particularly those in the field, as to when to search and whom to search. A warrant, by contrast, would provide assurances from a neutral officer that the inspection is reasonable under the Constitution, is authorized by statute, and is pursuant to an administrative plan containing specific neutral criteria.<sup>[20]</sup> Also, a warrant would then and there advise the owner of the scope and objects of the search, beyond which limits the inspector is not expected to proceed.<sup>[21]</sup> These are important functions for a warrant to perform, functions which underlie the Court's prior decisions that the Warrant Clause applies to <span class="star-pagination">*324</span> inspections for compliance with regulatory statutes.<sup>[22]</sup><i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967); <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). We conclude that the concerns expressed by the Secretary do not suffice to justify warrantless inspections under OSHA or vitiate the general constitutional requirement that for a search to be reasonable a warrant must be obtained.</p>
<p></p>
<h2>
<span class="star-pagination">*325</span> III</h2>
<p>We hold that Barlow's was entitled to a declaratory judgment that the Act is unconstitutional insofar as it purports to authorize inspections without warrant or its equivalent and to an injunction enjoining the Act's enforcement to that extent.<sup>[23]</sup> The judgment of the District Court is therefore affirmed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BRENNAN took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE STEVENS, with whom MR. JUSTICE BLACKMUN and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>Congress enacted the Occupational Safety and Health Act to safeguard employees against hazards in the work areas of businesses subject to the Act. To ensure compliance, Congress authorized the Secretary of Labor to conduct routine, nonconsensual inspections. Today the Court holds that the Fourth Amendment prohibits such inspections without a warrant. The Court also holds that the constitutionally required warrant may be issued without any showing of probable cause. I disagree with both of these holdings.</p>
<p>The Fourth Amendment contains two separate Clauses, each <span class="star-pagination">*326</span> flatly prohibiting a category of governmental conduct. The first Clause states that the right to be free from unreasonable searches "shall not be violated";<sup>[1]</sup> the second unequivocally prohibits the issuance of warrants except "upon probable cause."<sup>[2]</sup> In this case the ultimate question is whether the category of warrantless searches authorized by the statute is "unreasonable" within the meaning of the first Clause.</p>
<p>In cases involving the investigation of criminal activity, the Court has held that the reasonableness of a search generally depends upon whether it was conducted pursuant to a valid warrant. See, <i>e. g., </i><i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>. There is, however, also a category of searches which are reasonable within the meaning of the first Clause even though the probable-cause requirement of the Warrant Clause cannot be satisfied. See <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>; <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>; <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>. The regulatory inspection program challenged in this case, in my judgment, falls within this category.</p>
<p></p>
<h2>I</h2>
<p>The warrant requirement is linked "textually . . . to the probable-cause concept" in the Warrant Clause. <i>South Dakota</i> v. <i><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman, supra,</a></span></i> at 370 n. 5. The routine OSHA inspections are, by definition, not based on cause to believe there is a violation on the premises to be inspected. Hence, if the inspections were measured against the requirements of the Warrant Clause, they would be automatically and unequivocally unreasonable.</p>
<p><span class="star-pagination">*327</span> Because of the acknowledged importance and reasonableness of routine inspections in the enforcement of federal regulatory statutes such as OSHA, the Court recognizes that requiring full compliance with the Warrant Clause would invalidate all such inspection programs. Yet, rather than simply analyzing such programs under the "Reasonableness" Clause of the Fourth Amendment, the Court holds the OSHA program invalid under the Warrant Clause and then avoids a blanket prohibition on all routine, regulatory inspections by relying on the notion that the "probable cause" requirement in the Warrant Clause may be relaxed whenever the Court believes that the governmental need to conduct a category of "searches" outweighs the intrusion on interests protected by the Fourth Amendment.</p>
<p>The Court's approach disregards the plain language of the Warrant Clause and is unfaithful to the balance struck by the Framers of the Fourth Amendment"the one procedural safeguard in the Constitution that grew directly out of the events which immediately preceded the revolutionary struggle with England."<sup>[3]</sup> This preconstitutional history includes the controversy in England over the issuance of general warrants to aid enforcement of the seditious libel laws and the colonial experience with writs of assistance issued to facilitate collection of the various import duties imposed by Parliament. The Framers' familiarity with the abuses attending the issuance of such general warrants provided the principal stimulus for the restraints on arbitrary governmental intrusions embodied in the Fourth Amendment.</p>
<blockquote>"[O]ur constitutional fathers were not concerned about warrantless searches, but about overreaching warrants. It is perhaps too much to say that they feared the warrant more than the search, but it is plain enough that the warrant was the prime object of their concern. Far from <span class="star-pagination">*328</span> looking at the warrant as a protection against unreasonable searches, they saw it as an authority for unreasonable and oppressive searches . . . ."<sup>[4]</sup></blockquote>
<p>Since the general warrant, not the warrantless search, was the immediate evil at which the Fourth Amendment was directed, it is not surprising that the Framers placed precise limits on its issuance. The requirement that a warrant only issue on a showing of particularized probable cause was the means adopted to circumscribe the warrant power. While the subsequent course of Fourth Amendment jurisprudence in this Court emphasizes the dangers posed by warrantless searches conducted without probable cause, it is the general reasonableness standard in the first Clause, not the Warrant Clause, that the Framers adopted to limit this category of searches. It is, of course, true that the existence of a valid warrant normally satisfies the reasonableness requirement under the Fourth Amendment. But we should not dilute the requirements of the Warrant Clause in an effort to force every kind of governmental intrusion which satisfies the Fourth Amendment definition of a "search" into a judicially developed, warrant-preference scheme.</p>
<p>Fidelity to the original understanding of the Fourth Amendment, therefore, leads to the conclusion that the Warrant Clause has no application to routine, regulatory inspections of commercial premises. If such inspections are valid, it is because they comport with the ultimate reasonableness standard of the Fourth Amendment. If the Court were correct in its view that such inspections, if undertaken without a warrant, are unreasonable in the constitutional sense, the issuance of a "new-fangled warrant"to use Mr. Justice Clark's characteristically expressive termwithout any true showing of particularized probable cause would not be sufficient to validate them.<sup>[5]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*329</span> II</h2>
<p>Even if a warrant issued without probable cause were faithful to the Warrant Clause, I could not accept the Court's holding that the Government's inspection program is constitutionally unreasonable because it fails to require such a warrant procedure. In determining whether a warrant is a necessary safeguard in a given class of cases, "the Court has weighed the public interest against the Fourth Amendment interest of the individual . . . ." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 555</a></span>. Several considerations persuade me that this balance should be struck in favor of the routine inspections authorized by Congress.</p>
<p>Congress has determined that regulation and supervision of safety in the workplace furthers an important public interest and that the power to conduct warrantless searches is necessary to accomplish the safety goals of the legislation. In assessing the public interest side of the Fourth Amendment balance, however, the Court today substitutes its judgment for that of Congress on the question of what inspection authority is needed to effectuate the purposes of the Act. The Court states that if surprise is truly an important ingredient of an effective, representative inspection program, it can be retained by obtaining <i>ex parte</i> warrants in advance. The Court assures the Secretary that this will not unduly burden enforcement resources because most employers will consent to inspection.</p>
<p>The Court's analysis does not persuade me that Congress' determination that the warrantless-inspection power as a necessary adjunct of the exercise of the regulatory power is unreasonable. It was surely not unreasonable to conclude that the rate at which employers deny entry to inspectors would increase if covered businesses, which may have safety violations on their premises, have a right to deny warrantless entry to a compliance inspector. The Court is correct that this problem could be avoided by requiring inspectors to obtain a warrant prior to every inspection visit. But the adoption of <span class="star-pagination">*330</span> such a practice undercuts the Court's explanation of why a warrant requirement would not create undue enforcement problems. For, even if it were true that many employers would not exercise their right to demand a warrant, it would provide little solace to those charged with administration of OSHA; faced with an increase in the rate of refusals and the added costs generated by futile trips to inspection sites where entry is denied, officials may be compelled to adopt a general practice of obtaining warrants in advance. While the Court's prediction of the effect a warrant requirement would have on the behavior of covered employers may turn out to be accurate, its judgment is essentially empirical. On such an issue, I would defer to Congress' judgment regarding the importance of a warrantless-search power to the OSHA enforcement scheme.</p>
<p>The Court also appears uncomfortable with the notion of second-guessing Congress and the Secretary on the question of how the substantive goals of OSHA can best be achieved. Thus, the Court offers an alternative explanation for its refusal to accept the legislative judgment. We are told that, in any event, the Secretary, who is charged with enforcement of the Act, has indicated that inspections without delay are not essential to the enforcement scheme. The Court bases this conclusion on a regulation prescribing the administrative response when a compliance inspector is denied entry. It provides: "The Area Director shall immediately consult with the Assistant Regional Director and the Regional Solicitor, who shall promptly take appropriate action, including compulsory process, if necessary." <span class="citation no-link">29 CFR § 1903.4</span> (1977). The Court views this regulation as an admission by the Secretary that no enforcement problem is generated by permitting employers to deny entry and delaying the inspection until a warrant has been obtained. I disagree. The regulation was promulgated against the background of a statutory right to immediate entry, of which covered employers are presumably <span class="star-pagination">*331</span> aware and which Congress and the Secretary obviously thought would keep denials of entry to a minimum. In these circumstances, it was surely not unreasonable for the Secretary to adopt an orderly procedure for dealing with what he believed would be the occasional denial of entry. The regulation does not imply a judgment by the Secretary that delay caused by numerous denials of entry would be administratively acceptable.</p>
<p>Even if a warrant requirement does not "frustrate" the legislative purpose, the Court has no authority to impose an additional burden on the Secretary unless that burden is required to protect the employer's Fourth Amendment interests.<sup>[6]</sup> The essential function of the traditional warrant requirement is the interposition of a neutral magistrate between the citizen and the presumably zealous law enforcement officer so that there might be an objective determination of probable cause. But this purpose is not served by the newfangled inspection warrant. As the Court acknowledges, the inspector's "entitlement to inspect will not depend on his demonstrating probable cause to believe that conditions in violation of OSHA exist on the premises. . . . For purposes of an administrative search such as this, probable cause justifying the issuance of a warrant may be based . . . on a showing that `reasonable legislative or administrative standards for conducting an . . . inspection are satisfied with respect to a particular [establishment].'" <i>Ante,</i> at 320. To obtain a warrant, the inspector need only show that "a specific business has been chosen for an OSHA search on the basis of a general administrative plan for the enforcement of the Act derived <span class="star-pagination">*332</span> from neutral sources . . . ." <i>Ante,</i> at 321. Thus, the only question for the magistrate's consideration is whether the contemplated inspection deviates from an inspection schedule drawn up by higher level agency officials.</p>
<p>Unlike the traditional warrant, the inspection warrant provides no protection against the search itself for employers who the Government has no reason to suspect are violating OSHA regulations. The Court plainly accepts the proposition that random health and safety inspections are reasonable. It does not question Congress' determination that the public interest in workplaces free from health and safety hazards outweighs the employer's desire to conduct his business only in the presence of permittees, except in those rare instances when the Government has probable cause to suspect that the premises harbor a violation of the law.</p>
<p>What purposes, then, are served by the administrative warrant procedure? The inspection warrant purports to serve three functions: to inform the employer that the inspection is authorized by the statute, to advise him of the lawful limits of the inspection, and to assure him that the person demanding entry is an authorized inspector. <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span>. An examination of these functions in the OSHA context reveals that the inspection warrant adds little to the protections already afforded by the statute and pertinent regulations, and the slight additional benefit it might provide is insufficient to identify a constitutional violation or to justify overriding Congress' judgment that the power to conduct warrantless inspections is essential.</p>
<p>The inspection warrant is supposed to assure the employer that the inspection is in fact routine, and that the inspector has not improperly departed from the program of representative inspections established by responsible officials. But to the extent that harassment inspections would be reduced by the necessity of obtaining a warrant, the Secretary's present enforcement scheme would have precisely the same effect. <span class="star-pagination">*333</span> The representative inspections are conducted "`in accordance with criteria based upon accident experience and the number of employees exposed in particular industries.'" <i>Ante,</i> at 321 n. 17. If, under the present scheme, entry to covered premises is denied, the inspector can gain entry only by informing his administrative superiors of the refusal and seeking a court order requiring the employer to submit to the inspection. The inspector who would like to conduct a nonroutine search is just as likely to be deterred by the prospect of informing his superiors of his intention and of making false representations to the court when he seeks compulsory process as by the prospect of having to make bad-faith representations in an <i>ex parte</i> warrant proceeding.</p>
<p>The other two asserted purposes of the administrative warrant are also adequately achieved under the existing scheme. If the employer has doubts about the official status of the inspector, he is given adequate opportunity to reassure himself in this regard before permitting entry. The OSHA inspector's statutory right to enter the premises is conditioned upon the presentation of appropriate credentials. <span class="citation no-link">29 U. S. C. § 657</span> (a) (1). These credentials state the inspector's name, identify him as an OSHA compliance officer, and contain his photograph and signature. If the employer still has doubts, he may make a toll-free call to verify the inspector's authority, <i>Usery</i> v. <i>Godfrey Brake &amp; Supply Service, Inc.,</i> <span class="citation" data-id="340592"><a href="/opinion/340592/w-j-usery-jr-secretary-of-labor-v-godfrey-brake-and-supply-service/#54" aria-description="Citation for case: W. J. Usery, Jr., Secretary of Labor v. Godfrey Brake and...">545 F. 2d 52, 54</a></span> (CA8 1976), or simply deny entry and await the presentation of a court order.</p>
<p>The warrant is not needed to inform the employer of the lawful limits of an OSHA inspection. The statute expressly provides that the inspector may enter all areas in a covered business "where work is performed by an employee of an employer," <span class="citation no-link">29 U. S. C. § 657</span> (a) (1), "to inspect and investigate during regular working hours and at other reasonable times, and within reasonable limits and in a reasonable manner. . . all pertinent conditions, structures, machines, apparatus, <span class="star-pagination">*334</span> devices, equipment, and materials therein . . . ." <span class="citation no-link">29 U. S. C. § 657</span> (a)(2). See also <span class="citation no-link">29 CFR § 1903</span> (1977). While it is true that the inspection power granted by Congress is broad, the warrant procedure required by the Court does not purport to restrict this power but simply to ensure that the employer is apprised of its scope. Since both the statute and the pertinent regulations perform this informational function, a warrant is superfluous.</p>
<p>Requiring the inspection warrant, therefore, adds little in the way of protection to that already provided under the existing enforcement scheme. In these circumstances, the warrant is essentially a formality. In view of the obviously enormous cost of enforcing a health and safety scheme of the dimensions of OSHA, this Court should not, in the guise of construing the Fourth Amendment, require formalities which merely place an additional strain on already overtaxed federal resources.</p>
<p>Congress, like this Court, has an obligation to obey the mandate of the Fourth Amendment. In the past the Court "has been particularly sensitive to the Amendment's broad standard of `reasonableness' where . . . authorizing statutes permitted the challenged searches." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#290" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 290</a></span> (WHITE, J., dissenting). In <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span>, for example, respondents challenged the routine stopping of vehicles to check for aliens at permanent checkpoints located away from the border. The checkpoints were established pursuant to statutory authority and their location and operation were governed by administrative criteria. The Court rejected respondents' argument that the constitutional reasonableness of the location and operation of the fixed checkpoints should be reviewed in a <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> warrant proceeding. The Court observed that the reassuring purposes of the inspection warrant were adequately served by the visible manifestations of authority exhibited at the fixed checkpoints.</p>
<p><span class="star-pagination">*335</span> Moreover, although the location and method of operation of the fixed checkpoints were deemed critical to the constitutional reasonableness of the challenged stops, the Court did not require Border Patrol officials to obtain a warrant based on a showing that the checkpoints were located and operated in accordance with administrative standards. Indeed, the Court observed that "[t]he choice of checkpoint locations must be left largely to the discretion of Border Patrol officials, to be exercised in accordance with statutes and regulations that may be applicable . . . [and] [m]any incidents of checkpoint operation also must be committed to the discretion of such officials." 428 U. S., at 559-560, n. 13. The Court had no difficulty assuming that those officials responsible for allocating limited enforcement resources would be "unlikely to locate a checkpoint where it bears arbitrarily or oppressively on motorists as a class." <i>Id.,</i> at 559.</p>
<p>The Court's recognition of Congress' role in balancing the public interest advanced by various regulatory statutes and the private interest in being free from arbitrary governmental intrusion has not been limited to situations in which, for example, Congress is exercising its special power to exclude aliens. Until today, we have not rejected a congressional judgment concerning the reasonableness of a category of regulatory inspections of commercial premises.<sup>[7]</sup> While businesses are unquestionably entitled to Fourth Amendment protection, we have "recognized that a business, by its special nature and voluntary existence, may open itself to intrusions that would not be permissible in a purely private context." <span class="star-pagination">*336</span> <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#353" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 353</a></span>. Thus, in <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span>, the Court recognized the reasonableness of a statutory authorization to inspect the premises of a caterer dealing in alcoholic beverages, noting that "Congress has broad power to design such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand." <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><i>Id.,</i> at 76</a></span>. And in <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>, the Court sustained the authority to conduct warrantless searches of firearm dealers under the Gun Control Act of 1968 primarily on the basis of the reasonableness of the congressional evaluation of the interests at stake.<sup>[8]</sup></p>
<p>The Court, however, concludes that the deference accorded Congress in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> and <i>Colonnade</i> should be limited to situations where the evils addressed by the regulatory statute are peculiar to a specific industry and that industry is one which has long been subject to Government regulation. The Court reasons that only in those situations can it be said that a person who engages in business will be aware of and consent to routine, regulatory inspections. I cannot agree that the respect due the congressional judgment should be so narrowly confined.</p>
<p>In the first place, the longevity of a regulatory program does not, in my judgment, have any bearing on the reasonableness of routine inspections necessary to achieve adequate enforcement of that program. Congress' conception of what constitute <span class="star-pagination">*337</span> urgent federal interests need not remain static. The recent vintage of public and congressional awareness of the dangers posed by health and safety hazards in the workplace is not a basis for according less respect to the considered judgment of Congress. Indeed, in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> the Court upheld an inspection program authorized by a regulatory statute enacted in 1968. The Court there noted that "[f]ederal regulation of the interstate traffic in firearms is not as deeply rooted in history as is governmental control of the liquor industry, but close scrutiny of this traffic is undeniably" an urgent federal interest. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315</a></span>. Thus, the critical fact is the congressional determination that federal regulation would further significant public interests, not the date that determination was made.</p>
<p>In the second place, I see no basis for the Court's conclusion that a congressional determination that a category of regulatory inspections is reasonable need only be respected when Congress is legislating on an industry-by-industry basis. The pertinent inquiry is not whether the inspection program is authorized by a regulatory statute directed at a single industry, but whether Congress has limited the exercise of the inspection power to those commercial premises where the evils at which the statute is directed are to be found. Thus, in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> if Congress had authorized inspections of all commercial premises as a means of restricting the illegal traffic in firearms, the Court would have found the inspection program unreasonable; the power to inspect was upheld because it was tailored to the subject matter of Congress' proper exercise of regulatory power. Similarly, OSHA is directed at health and safety hazards in the workplace, and the inspection power granted the Secretary extends only to those areas where such hazards are likely to be found.</p>
<p>Finally, the Court would distinguish the respect accorded Congress' judgment in <i>Colonnade</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> on the ground that businesses engaged in the liquor and firearms industry "`accept the burdens as well as the benefits of their trade...." <span class="star-pagination">*338</span> <i>Ante,</i> at 313. In the Court's view, such businesses consent to the restrictions placed upon them, while it would be fiction to conclude that a businessman subject to OSHA consented to routine safety inspections. In fact, however, consent is fictional in both contexts. Here, as well as in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> businesses are required to be aware of and comply with regulations governing their business activities. In both situations, the validity of the regulations depends not upon the consent of those regulated, but on the existence of a federal statute embodying a congressional determination that the public interest in the health of the Nation's work force or the limitation of illegal firearms traffic outweighs the businessman's interest in preventing a Government inspector from viewing those areas of his premises which relate to the subject matter of the regulation.</p>
<p>The case before us involves an attempt to conduct a warrantless search of the working area of an electrical and plumbing contractor. The statute authorizes such an inspection during reasonable hours. The inspection is limited to those areas over which Congress has exercised its proper legislative authority.<sup>[9]</sup> The area is also one to which employees <span class="star-pagination">*339</span> have regular access without any suggestion that the work performed or the equipment used has any special claim to confidentiality.<sup>[10]</sup> Congress has determined that industrial safety is an urgent federal interest requiring regulation and supervision, and further, that warrantless inspections are necessary to accomplish the safety goals of the legislation. While one may question the wisdom of pervasive governmental oversight of industrial life, I decline to question Congress' judgment that the inspection power is a necessary enforcement device in achieving the goals of a valid exercise of regulatory power.<sup>[11]</sup></p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Warren Spannaus,</i> Attorney General of Minnesota, <i>Richard B. Allyn,</i> Solicitor General, and <i>Steven M. Gunn</i> and <i>Richard A. Lockridge,</i> Special Assistant Attorneys General, filed a brief for 11 States as <i>amici curiae</i> urging reversal, joined by the Attorneys General for their respective States as follows: <i>Frank J. Kelley</i> of Michigan, <i>William F. Hyland</i> of New Jerssey, <i>Toney Anaya</i> of New Mexico, <i>Rufus Edmisten</i> of North Carolina, <i>Robert P. Kane</i> of Pennsylvania, <i>Daniel R. McLeod</i> of South Carolina, <i>M. Jerome Diamond</i> of Vermont, <i>Anthony F. Troy</i> of Virginia, and <i>V. Frank Mendicino</i> of Wyoming. Briefs of <i>amici curiae</i> urging reversal were filed by <i>J. Albert Woll</i> and <i>Laurence Gold</i> for the American Federation of Labor and Congress of Industrial Organizations; and by <i>Michael R. Sherwood</i> for the Sierra Club et al.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed by <i>Wayne L. Kidwell,</i> Attorney General of Idaho, and <i>Guy G. Hurlbutt,</i> Chief Deputy Attorney General, <i>Robert B. Hansen,</i> Attorney General of Utah, and <i>Michael L. Deamer,</i> Deputy Attorney General, for the States of Idaho and Utah; by <i>Allen A. Lauterbach</i> for the American Farm Bureau Federation; by <i>Robert T. Thompson, Lawrence Kraus,</i> and <i>Stanley T. Kaleczyc</i> for the Chamber of Commerce of the United States; by <i>Anthony J. Obadal, Steven R.</i> <i>Semler, Stephen C. Yohay, Leonard J. Theberge, Edward H. Dowd,</i> and <i>James Watt</i> for the Mountain States Legal Foundation; by <i>James D. McKevitt</i> for the National Federation of Independent Business; and by <i>Ronald A. Zumbrun, John H. Findley, Albert Ferri, Jr.,</i> and <i>W. Hugh O'Riordan</i> for the Pacific Legal Foundation.</p>
<p>Briefs of <i>amici curiae</i> were filed by <i>Robert E. Rader, Jr.,</i> for the American Conservative Union; and by <i>David Goldberger, Barbara O'Toole, McNeill Stokes, Ira J. Smotherman, Jr.,</i> and <i>David Rudenstine</i> for the Roger Baldwin Foundation, Inc., of the American Civil Liberties Union, Illinois Division.</p>
<p>[1]  "In order to carry out the purposes of this chapter, the Secretary, upon presenting appropriate credentials to the owner, operator, or agent in charge, is authorized
</p>
<p>"(1) to enter without delay and at reasonable times any factory, plant, establishment, construction site, or other area, workplace or environment where work is performed by an employee of an employer; and</p>
<p>"(2) to inspect and investigate during regular working hours and at other reasonable times, and within reasonable limits and in a reasonable manner, any such place of employment and all pertinent conditions, structures, machines, apparatus, devices, equipment, and materials therein, and to question privately any such employer, owner, operator, agent, or employee." <span class="citation no-link">84 Stat. 1598</span>, <span class="citation no-link">29 U. S. C. § 657</span> (a).</p>
<p>[2]  This is required by the Act. See n. 1, <i>supra.</i></p>
<p>[3]  A regulation of the Secretary, <span class="citation no-link">29 CFR § 1903.4</span> (1977), requires an inspector to seek compulsory process if an employer refuses a requested search. See <i>infra,</i> at 317, and n. 12.</p>
<p>[4]  No <i>res judicata</i> bar arose against Mr. Barlow from the December 30, 1975, order authorizing a search, because the earlier decision reserved the constitutional issue. See <span class="citation" data-id="1444752"><a href="/opinion/1444752/barlows-inc-v-usery/" aria-description="Citation for case: Barlow&#x27;s, Inc. v. Usery">424 F. Supp. 437</a></span>.</p>
<p>[5]  H. Commager, Documents of American History 104 (8th ed. 1968).</p>
<p>[6]  See, <i>e. g.,</i> Dickerson, Writs of Assistance as a Cause of the Revolution in The Era of the American Revolution 40 (R. Morris ed. 1939).</p>
<p>[7]  The Stamp Act of 1765, the Townshend Revenue Act of 1767, and the tea tax of 1773 are notable examples. See Commager, <i>supra,</i> n. 5, at 53, 63. For commentary, see 1 S. Morison, H. Commager, &amp; W. Leuchtenburg, The Growth of the American Republic 143, 149, 159 (1969).</p>
<p>[8]  The Government has asked that Mr. Barlow be ordered to show cause why he should not be held in contempt for refusing to honor the inspection order, and its position is that the OSHA inspector is now entitled to enter at once, over Mr. Barlow's objection.</p>
<p>[9]  Cf. <i>Air Pollution Variance Bd.</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861</a></span> (1974).</p>
<p>[10]  The automobile-search cases cited by the Secretary are even less helpful to his position than the labor cases. The fact that automobiles occupy a special category in Fourth Amendment case law is by now beyond doubt due, among other factors, to the quick mobility of a car, the registration requirements of both the car and the driver, and the more available opportunity for plain-view observations of a car's contents. <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); see also <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#48" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 48-51</a></span> (1970). Even so, probable cause has not been abandoned as a requirement for stopping and searching an automobile.</p>
<p>[11]  We recognize that today's holding itself might have an impact on whether owners choose to resist requested searches; we can only await the development of evidence not present on this record to determine how serious an impediment to effective enforcement this might be.</p>
<p>[12]  It is true, as the Secretary asserts, that § 8 (a) of the Act, <span class="citation no-link">29 U. S. C. § 657</span> (a), purports to authorize inspections without warrant; but it is also true that it does not forbid the Secretary from proceeding to inspect only by warrant or other process. The Secretary has broad authority to prescribe such rules and regulations as he may deem necessary to carry out his responsibilities under this chapter, "including rules and regulations dealing with the inspection of an employer's establishment." § 8 (g) (2), <span class="citation no-link">29 U. S. C. § 657</span> (g) (2). The regulations with respect to inspections are contained in 29 CFR Part 1903 (1977). Section 1903.4, referred to in the text, provides as follows:
</p>
<p>"Upon a refusal to permit a Compliance Safety and Health Officer, in the exercise of his official duties, to enter without delay and at reasonable times any place of employment or any place therein, to inspect, to review records, or to question any employer, owner, operator, agent, or employee, in accordance with § 1903.3, or to permit a representative of employees to accompany the Compliance Safety and Health Officer during the physical inspection of any workplace in accordance with § 1903.8, the Compliance Safety and Health Officer shall terminate the inspection or confine the inspection to other areas, conditions, structures, machines, apparatus, devices, equipment, materials, records, or interviews concerning which no objection is raised. The Compliance Safety and Health Officer shall endeavor to ascertain the reason for such refusal, and he shall immediately report the refusal and the reason therefor to the Area Director. The Area Director shall immediately consult with the Assistant Regional Director and the Regional Solicitor, who shall promptly take appropriate action, including compulsory process, if necessary."</p>
<p>When his representative was refused admission by Mr. Barlow, the Secretary proceeded in federal court to enforce his right to enter and inspect, as conferred by <span class="citation no-link">29 U. S. C. § 657</span>.</p>
<p>[13]  A change in the language of the Compliance Operations Manual for OSHA inspectors supports the inference that, whatever the Act's administrators might have thought at the start, it was eventually concluded that enforcement efficiency would not be jeopardized by permitting employers to refuse entry, at least until the inspector obtained compulsory process. The 1972 Manual included a section specifically directed to obtaining "warrants," and one provision of that section dealt with <i>ex parte</i> warrants:
</p>
<p>"In cases where a refusal of entry is to be expected from the past performance of the employer, or where the employer has given some indication prior to the commencement of the investigation of his intention to bar entry or limit or interfere with the investigation, a warrant should be obtained before the inspection is attempted. Cases of this nature should also be referred through the Area Director to the appropriate Regional Solicitor and the Regional Administrator alerted." Dept. of Labor, OSHA Compliance Operations Manual V-7 (Jan. 1972).</p>
<p>The latest available manual, incorporating changes as of November 1977, deletes this provision, leaving only the details for obtaining "compulsory process" <i>after</i> an employer has refused entry. Dept. of Labor, OSHA Field Operations Manual, Vol. V, pp. V-4-V-5. In its present form, the Secretary's regulation appears to permit establishment owners to insist on "process"; and hence their refusal to permit entry would fall short of criminal conduct within the meaning of <span class="citation no-link">18 U. S. C. §§ 111</span> and 1114 (1976 ed.), which make it a crime forcibly to impede, intimidate, or interfere with federal officials, including OSHA inspectors, while engaged in or on account of the performance of their official duties.</p>
<p>[14]  The proceeding was instituted by filing an "Application for Affirmative Order to Grant Entry and for an Order to show cause why such affirmative order should not issue." The District Court issued the order to show cause, the matter was argued, and an order then issued authorizing the inspection and enjoining interference by Barlow's. The following is the order issued by the District Court:
</p>
<p>"IT IS HEREBY ORDERED, ADJUDGED AND DECREED that the United States of America, United States Department of Labor, Occupational Safety and Health Administration, through its duly designated representative or representatives, are entitled to entry upon the premises known as Barlow's Inc., 225 West Pine, Pocatello, Idaho, and may go upon said business premises to conduct an inspection and investigation as provided for in Section 8 of the Occupational Safety and Health Act of 1970 (29 U. S. C. 651, <i>et seq.</i>), as part of an inspection program designed to assure compliance with that Act; that the inspection and investigation shall be conducted during regular working hours or at other reasonable times, within reasonable limits and in a reasonable manner, all as set forth in the regulations pertaining to such inspections promulgated by the Secretary of Labor, at 29 C. F. R., Part 1903; that appropriate credentials as representatives of the Occupational Safety and Health Administration, United States Department of Labor, shall be presented to the Barlow's Inc. representative upon said premises and the inspection and investigation shall be commenced as soon as practicable after the issuance of this Order and shall be completed within reasonable promptness; that the inspection and investigation shall extend to the establishment or other area, workplace, or environment where work is performed by employees of the employer, Barlow's Inc., and to all pertinent conditions, structures, machines, apparatus, devices, equipment, materials, and all other things therein (including but not limited to records, files, papers, processes, controls, and facilities) bearing upon whether Barlow's Inc. is furnishing to its employees employment and a place of employment that are free from recognized hazards that are causing or are likely to cause death or serious physical harm to its employees, and whether Barlow's Inc. is complying with the Occupational Safety and Health Standards promulgated under the Occupational Safety and Health Act and the rules, regulations, and orders issued pursuant to that Act; that representatives of the Occupational Safety and Health Administration may, at the option of Barlow's Inc., be accompanied by one or more employees of Barlow's Inc., pursuant to Section 8 (e) of that Act; that Barlow's Inc., its agents, representatives, officers, and employees are hereby enjoined and restrained from in anyway whatsoever interfering with the inspection and investigation authorized by this Order and, further, Barlow's Inc. is hereby ordered and directed to, within five working days from the date of this Order, furnish a copy of this Order to its officers and managers, and, in addition, to post a copy of this Order at its employee's bulletin board located upon the business premises; and Barlow's Inc. is hereby ordered and directed to comply in all respects with this order and allow the inspection and investigation to take place without delay and forthwith."</p>
<p>[15]  Insofar as the Secretary's statutory authority is concerned, a regulation expressly providing that the Secretary could proceed <i>ex parte</i> to seek a warrant or its equivalent would appear to be as much within the Secretary's power as the regulation currently in force and calling for "compulsory process."</p>
<p>[16]  Section 8 (f) (1), <span class="citation no-link">29 U. S. C. § 657</span> (f) (1), provides that employees or their representatives may give written notice to the Secretary of what they believe to be violations of safety or health standards and may request an inspection. If the Secretary then determines that "there are reasonable grounds to believe that such violation or danger exists, he shall make a special inspection in accordance with the provisions of this section as soon as practicable." The statute thus purports to authorize a warrantless inspection in these circumstances.</p>
<p>[17]  The Secretary, Brief for Petitioner 9 n. 7, states that the Barlow inspection was not based on an employee complaint but was a "general schedule" investigation. "Such general inspections," he explains, "now called Regional Programmed Inspections, are carried out in accordance with criteria based upon accident experience and the number of employees exposed in particular industries. U. S. Department of Labor, Occupational Safety and Health Administration, Field Operations Manual, <i>supra,</i> 1 CCH Employment Safety and Health Guide ¶ 4327.2 (1976)."</p>
<p>[18]  The Federal Metal and Nonmetallic Mine Safety Act provides: "Whenever an operator . . . refuses to permit the inspection or investigation of any mine which is subject to this chapter . . . a civil action for preventive relief, including an application for a permanent or temporary injunction, restraining order, or other order, may be instituted by the Secretary in the district court of the United States for the district . . . ." <span class="citation no-link">30 U. S. C. § 733</span> (a). "The Secretary may institute a civil action for relief, including a permanent or temporary injunction, restraining order, or any other appropriate order in the district court . . . whenever such operator or his agent . . . refuses to permit the inspection of the mine . . . . Each court shall have jurisdiction to provide such relief as may be appropriate." <span class="citation no-link">30 U. S. C. § 818</span>. Another example is the Clean Air Act, which grants federal district courts jurisdiction "to require compliance" with the Administrator of the Environmental Protection Agency's attempt to inspect under <span class="citation no-link">42 U. S. C. § 7414</span> (1976 ed., Supp. I), when the Administrator has commenced "a civil action" for injunctive relief or to recover a penalty. <span class="citation no-link">42 U. S. C. § 7413</span> (b) (4) (1976 ed., Supp. I).</p>
<p>[19]  Exemplary language is contained in the Animal Welfare Act of 1970 which provides for inspections by the Secretary of Agriculture; federal district courts are vested with jurisdiction "specifically to enforce, and to prevent and restrain violations of this chapter, and shall have jurisdiction in all other kinds of cases arising under this chapter." <span class="citation no-link">7 U. S. C. § 2146</span> (c) (1976 ed.). Similar provisions are included in other agricultural inspection Acts; see, <i>e. g.,</i> <span class="citation no-link">21 U. S. C. § 674</span> (meat product inspection); <span class="citation no-link">21 U. S. C. § 1050</span> (egg product inspection). The Internal Revenue Code, whose excise tax provisions requiring inspections of businesses are cited by the Secretary, provides: "The district courts . . . shall have such jurisdiction to make and issue in civil actions, writs and orders of injunction. . . and such other orders and processes, and to render such . . . decrees as may be necessary or appropriate for the enforcement of the internal revenue laws." <span class="citation no-link">26 U. S. C. § 7402</span> (a). For gasoline inspections, federal district courts are granted jurisdiction to restrain violations and enforce standards (one of which, <span class="citation no-link">49 U. S. C. § 1677</span>, requires gas transporters to permit entry or inspection). The owner is to be afforded the opportunity for notice and response in most cases, but "failure to give such notice and afford such opportunity shall not preclude the granting of appropriate relief [by the district court]." <span class="citation no-link">49 U. S. C. § 1679</span> (a).</p>
<p>[20]  The application for the inspection order filed by the Secretary in this case represented that "the desired inspection and investigation are contemplated as a part of an inspection program designed to assure compliance with the Act and are authorized by Section 8 (a) of the Act." The program was not described, however, or any facts presented that would indicate why an inspection of Barlow's establishment was within the program. The order that issued concluded generally that the inspection authorized was "part of an inspection program designed to assure compliance with the Act."</p>
<p>[21]  Section 8 (a) of the Act, as set forth in <span class="citation no-link">29 U. S. C. § 657</span> (a), provides that "[i]n order to carry out the purposes of this chapter" the Secretary may enter any establishment, area, work place or environment "where work is performed by an employee of an employer" and "inspect and investigate" any such place of employment and all "pertinent conditions, structures, machines, apparatus, devices, equipment, and materials therein, and . . . question privately any such employer, owner, operator, agent, or employee." Inspections are to be carried out "during regular working hours and at other reasonable times, and within reasonable limits and in a reasonable manner." The Secretary's regulations echo the statutory language in these respects. <span class="citation no-link">29 CFR § 1903.3</span> (1977). They also provide that inspectors are to explain the nature and purpose of the inspection and to "indicate generally the scope of the inspection." <span class="citation no-link">29 CFR § 1903.7</span> (a) (1977). Environmental samples and photographs are authorized, <span class="citation no-link">29 CFR § 1903.7</span> (b) (1977), and inspections are to be performed so as "to preclude unreasonable disruption of the operations of the employer's establishment." <span class="citation no-link">29 CFR § 1903.7</span> (d) (1977). The order that issued in this case reflected much of the foregoing statutory and regulatory langnage.</p>
<p>[22]  Delineating the scope of a search with some care is particularly important where documents are involved. Section 8 (c) of the Act, <span class="citation no-link">29 U. S. C. § 657</span> (c), provides that an employer must "make, keep and preserve, and make available to the Secretary [of Labor] or to the Secretary of Health, Education and Welfare" such records regarding his activities relating to OSHA as the Secretary of Labor may prescribe by regulation as necessary or appropriate for enforcement of the statute or for developing information regarding the causes and prevention of occupational accidents and illnesses. Regulations requiring employers to maintain records of and to make periodic reports on "work-related deaths, injuries and illnesses" are also contemplated, as are rules requiring accurate records of employee exposures to potential toxic materials and harmful physical agents.
</p>
<p>In describing the scope of the warrantless inspection authorized by the statute, § 8 (a) does not expressly include any <i>records</i> among those items or things that may be examined, and § 8 (c) merely provides that the employer is to "make available" his pertinent records and to make periodic reports.</p>
<p>The Secretary's regulation, <span class="citation no-link">29 CFR § 1903.3</span> (1977), however, expressly includes among the inspector's powers the authority "to review records required by the Act and regulations published in this chapter, and other records which are directly related to the purpose of the inspection." Further, § 1903.7 requires inspectors to indicate generally "the records specified in § 1903.3 which they wish to review" but "such designations of records shall not preclude access to additional records specified in § 1903.3." It is the Secretary's position, which we reject, that an inspection of documents of this scope may be effected without a warrant.</p>
<p>The order that issued in this case included among the objects and things to be inspected "all other things therein (including but not limited to records, files, papers, processes, controls and facilities) bearing upon whether Barlow's, Inc. is furnishing to its employees employment and a place of employment that are free from recognized hazards that are causing or are likely to cause death or serious physical harm to its employees, and whether Barlow's, Inc. is complying with . . ." the OSHA regulations.</p>
<p>[23]  The injunction entered by the District Court, however, should not be understood to forbid the Secretary from exercising the inspection authority conferred by § 8 pursuant to regulations and judicial process that satisfy the Fourth Amendment. The District Court did not address the issue whether the order for inspection that was issued in this case was the functional equivalent of a warrant, and the Secretary has limited his submission in this case to the constitutionality of a warrantless search of the Barlow establishment authorized by § 8 (a). He has expressly declined to rely on <span class="citation no-link">29 CFR § 1903.4</span> (1977) and upon the order obtained in this case. Tr. of Oral Arg. 19. Of course, if the process obtained here, or obtained in other cases under revised regulations, would satisfy the Fourth Amendment, there would be no occasion for enjoining the inspections authorized by § 8 (a).</p>
<p>[1]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ."</p>
<p>[2]  "[A]nd no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[3]  J. Landynski, Search and Seizure and the Supreme Court 19 (1966).</p>
<p>[4]  T. Taylor, Two Studies in Constitutional Interpretation 41 (1969).</p>
<p>[5]  <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#547" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 547</a></span> (Clark, J., dissenting).</p>
<p>[6]  When it passed OSHA, Congress was cognizant of the fact that in light of the enormity of the enforcement task "the number of inspections which it would be desirable to have made will undoubtedly for an unforeseeable period, exceed the capacity of the inspection force . . . ." Senate Committee on Labor and Public Welfare, Legislative History of the Occupational Safety and Health Act of 1970, 92d Cong., 1st Sess., 152 (Comm. Print 1971).</p>
<p>[7]  The Court's rejection of a legislative judgment regarding the reasonableness of the OSHA inspection program is especially puzzling in light of recent decisions finding law enforcement practices constitutionally reasonable, even though those practices involved significantly more individual discretion than the OSHA program. See, <i>e. g., </i><i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>; <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span>; <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span>; <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span>.</p>
<p>[8]  The Court held:
</p>
<p>"In the context of a regulatory inspection system of business premises that is carefully limited in time, place, and scope, the legality of the search depends . . . on the authority of a valid statute.</p>
<p>. . . . .</p>
<p>"We have little difficulty in concluding that where, as here, regulatory inspections further urgent federal interest, and the possibilities of abuse and the threat to privacy are not of impressive dimensions, the inspection may proceed without a warrant where specifically authorized by statute." <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315, 317</a></span>.</p>
<p>[9]  What the Court actually decided in <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, and <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>, does not require the result it reaches today. <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> involved a residence, rather than a business establishment; although the Fourth Amendment extends its protection to commercial buildings, the central importance of protecting residential privacy is manifest. The building involved in <i>See</i> was, of course, a commercial establishment, but a holding that a locked warehouse may not be entered pursuant to a general authorization to "enter all buildings and premises, except the interior of dwellings, as often as may be necessary," 387 U. S., at 541, need not be extended to cover more carefully delineated grants of authority. My view that the <i>See</i> holding should be narrowly confined is influenced by my favorable opinion of the dissent written by Mr. Justice Clark and joined by Justices Harlan and STEWART. As <i>Colonnade</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> demonstrate, however, the doctrine of <i>stare decisis</i> does not compel the Court to extend those cases to govern today's holding.</p>
<p>[10]  The Act and pertinent regulation provide protection for any trade secrets of the employer. <span class="citation no-link">29 U. S. C. §§ 664-665</span>; <span class="citation no-link">29 CFR § 1903.9</span> (1977).</p>
<p>[11]  The decision today renders presumptively invalid numerous inspection provisions in federal regulatory statutes. <i>E. g.,</i> <span class="citation no-link">30 U. S. C. § 813</span> (Federal Coal Mine Health and Safety Act of 1969); <span class="citation no-link">30 U. S. C. §§ 723</span>, 724 (Federal Metal and Nonmetallic Mine Safety Act); <span class="citation no-link">21 U. S. C. § 603</span> (inspection of meat and food products). That some of these provisions apply only to a single industry, as noted above, does not alter this fact. And the fact that some "envision resort to federal-court enforcement when entry is refused" is also irrelevant since the OSHA inspection program invalidated here requires compulsory process when a compliance inspector has been denied entry. <i>Ante,</i> at 321.</p>

</div>
```

---

## GROUP: content/cases/Maryland v. Dyson.md  (`case`, 5 assertions)

### content_page

```
---
title: "Maryland v. Dyson"
type: case
citation: "527 U.S. 465 (1999)"
parallel_cite: "119 S. Ct. 2013; 144 L. Ed. 2d 442"
neutral_cite: 1999 U.S. LEXIS 4200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-06-21
docket: 98-1062
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Dyson
  varies_by_point: false
  scope_note: "Per curiam. Settled statement of the automobile exception; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2621047/maryland-v-dyson/"
  cluster_id: 2621047
  opinion_id: 9795106
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Pennsylvania v. Labron]]", "[[United States v. Ross]]", "[[California v. Carney]]", "[[Carroll v. United States]]", "[[Michigan v. Thomas]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "no-exigency", "probable-cause", "readily-mobile"]
holding: "The automobile exception has no separate exigency requirement; if a car is readily mobile and probable cause exists to believe it contains contraband, police may search it without a warrant even when there was ample time to obtain one."
lake:
  record_id: Maryland v. Dyson
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Dyson

*527 U.S. 465 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A sheriff's deputy received a tip from a reliable confidential informant that the respondent, a known drug dealer, had gone to New York to buy cocaine and would return that day in a specifically identified rented red Toyota. The deputy corroborated the rental and the license plate. When the respondent returned in the car, deputies stopped and searched it without a warrant and found 23 grams of crack cocaine in a duffel bag in the trunk. The Maryland Court of Special Appeals reversed the conviction, holding that the automobile exception requires, in addition to probable cause, a separate finding of [[Exigent Circumstances and Hot Pursuit|exigency]] — and that here, with "abundant probable cause" but ample time to get a warrant, the warrantless search was invalid.

## Issue
Whether the automobile exception requires a separate finding of [[Exigent Circumstances and Hot Pursuit|exigency]] in addition to probable cause to believe the vehicle contains contraband.

## Rule
No. "[U]nder our established precedent, the 'automobile exception' has no separate exigency requirement." — 527 U.S. at 466. ^pin-466

Quoting *[[Pennsylvania v. Labron]]*: "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment . . . permits police to search the vehicle without more." — *Id.* at 467 (quoting 518 U.S. at 940). ^pin-467

## Application
The state court itself found "abundant probable cause" that the car contained contraband. That finding alone satisfied the automobile exception, exactly as the trial court had concluded. Requiring a separate showing of [[Exigent Circumstances and Hot Pursuit|exigency]] — and faulting the police for not getting a warrant when there was time — was "squarely contrary" to *[[United States v. Ross|Ross]]* and *[[Pennsylvania v. Labron|Labron]]*. The warrantless search of the readily mobile car was therefore valid.

## Conclusion
Reversed (per curiam). Probable cause that a readily mobile vehicle contains contraband is enough; the automobile exception carries no independent [[Exigent Circumstances and Hot Pursuit|exigency]] requirement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Dyson* states flatly the principle developed across [[Carroll v. United States]], [[United States v. Ross]], [[Michigan v. Thomas]], and [[Pennsylvania v. Labron]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Dyson*, 527 U.S. 465 (1999) — https://www.courtlistener.com/opinion/2621047/maryland-v-dyson/ — pinpoints: 466, 467.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e672049554f752c0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "527 U.S. 465 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 4200", "official_citation_present": true, "parallel_cite": "119 S. Ct. 2013; 144 L. Ed. 2d 442", "title": "Maryland v. Dyson", "year": "1999"}}
{"assertion_id": "39c2791d5e873bf2", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Maryland v. Dyson"}}
{"assertion_id": "5a726fe13e412133", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The automobile exception has no separate exigency requirement; if a car is readily mobile and probable cause exists to believe it contains contraband, police may search it without a warrant even when there was ample time to obtain one.", "title": "Maryland v. Dyson"}}
{"assertion_id": "7cbfa1e0fd11d2ca", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Maryland v. Dyson"}}
{"assertion_id": "80e75b5af77f6b32", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Maryland v. Dyson", "field_i_validity": "good_law", "scope_note": "Per curiam. Settled statement of the automobile exception; no negative treatment.", "title": "Maryland v. Dyson", "varies_by_point": "false"}}
```

### lake record — Maryland v. Dyson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Dyson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Dyson",
    "case_name_short": "Dyson",
    "case_name_full": "Maryland v. Dyson",
    "input_case_name": "Maryland v. Dyson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-06-21",
    "year": 1999,
    "docket": "98-1062",
    "cluster_id": 2621047,
    "lead_opinion_id": 9795106,
    "sibling_ids": [
      2621047,
      9795106,
      9795107
    ],
    "absolute_url": "/opinion/2621047/maryland-v-dyson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "527 U.S. 465",
      "volume": "527",
      "reporter": "U.S.",
      "page": "465",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 2013",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "2013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 442",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 4200",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "527 U.S. 465",
        "volume": "527",
        "reporter": "U.S.",
        "page": "465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 2013",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "2013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 442",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 4200",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "527 U.S. 465",
    "official_selection": {
      "court_class": "scotus",
      "selected": "527 U.S. 465",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-466",
      "page": null,
      "quote": "but ample time to get a warrant, the warrantless search was invalid. ## Issue Whether the automobile exception requires a separate finding of exigency in addition to probable cause to believe the vehicle contains contraband. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-467",
      "page": null,
      "quote": "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment . . . permits police to search the vehicle without more.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Dyson",
    "varies_by_point": false,
    "scope_note": "Per curiam. Settled statement of the automobile exception; no negative treatment.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Limon v. State",
          "cluster_id": 1466284,
          "cite": [
            "314 S.W.3d 694",
            "2010 Tex. App. LEXIS 4565",
            "2010 WL 2430428"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
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
        "journal_ref": "Maryland v. Dyson:lane1_negative"
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
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 2187417,
          "cite": [
            "305 S.W.3d 530",
            "2009 Tex. Crim. App. LEXIS 1440",
            "2009 WL 3365661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tyronski Johnson",
          "cluster_id": 790485,
          "cite": [
            "410 F.3d 137",
            "2005 U.S. App. LEXIS 10600",
            "2005 WL 1345622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kazmierczak",
          "cluster_id": 1965440,
          "cite": [
            "605 N.W.2d 667",
            "461 Mich. 411",
            "2000 WL 146099"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keehn v. State",
          "cluster_id": 2341745,
          "cite": [
            "279 S.W.3d 330",
            "2009 Tex. Crim. App. LEXIS 425",
            "2009 WL 774854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randy Graham",
          "cluster_id": 775981,
          "cite": [
            "275 F.3d 490",
            "2001 U.S. App. LEXIS 26685",
            "2001 WL 1636805"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 2196499,
          "cite": [
            "751 A.2d 92",
            "163 N.J. 657",
            "2000 N.J. LEXIS 529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. State",
          "cluster_id": 1400372,
          "cite": [
            "206 S.W.3d 613",
            "2006 Tex. Crim. App. LEXIS 1006",
            "2006 WL 1408451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randall Cope and Terry Wayne Cope",
          "cluster_id": 780062,
          "cite": [
            "312 F.3d 757"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gauster",
          "cluster_id": 1873770,
          "cite": [
            "752 N.W.2d 496",
            "2008 Minn. LEXIS 322",
            "2008 WL 2678037"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 852726,
          "cite": [
            "839 N.E.2d 1146",
            "2005 Ind. LEXIS 1135",
            "2005 WL 3484607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Mosley",
          "cluster_id": 794964,
          "cite": [
            "454 F.3d 249",
            "2006 U.S. App. LEXIS 18322",
            "2006 WL 2035249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elison",
          "cluster_id": 885285,
          "cite": [
            "2000 MT 288",
            "14 P.3d 456",
            "302 Mont. 228",
            "2000 Mont. LEXIS 291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
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
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Katrina Lyons",
          "cluster_id": 805149,
          "cite": [
            "687 F.3d 754",
            "2012 WL 3023528",
            "2012 U.S. App. LEXIS 15300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2621047 OR 9795106 OR 9795107) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMxOTc3NjAwMDAwJnM9MjkyNzUxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282621047+OR+9795106+OR+9795107%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(2621047 OR 9795106 OR 9795107)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MSZzPTIxNjI2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282621047+OR+9795106+OR+9795107%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2621047 OR 9795106 OR 9795107)",
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
    "complete_query": "cites:(2621047 OR 9795106 OR 9795107)",
    "indexed_citing_opinions": 416,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2621047,
        "count": 352,
        "count_source": "search"
      },
      {
        "opinion_id": 9795106,
        "count": 72,
        "count_source": "search"
      },
      {
        "opinion_id": 9795107,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 696,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-dyson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwODM4ODImcz05MzU3MDM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282621047+OR+9795106+OR+9795107%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2621047,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 1929659,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T11:53:09Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:56:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Dyson

```
<opinion type="majority">
<author id="b499-10">Per Curiam.</author>
<p id="b499-11">In this case, the Maryland Court of Special Appeals held that the Fourth Amendment requires police to obtain a search warrant before searching a vehicle which they have probable cause to believe contains illegal drugs. Because this holding rests upon an incorrect interpretation of the automobile exception to the Fourth Amendment’s warrant requirement, we grant the petition for certiorari and reverse.</p>
<p id="b499-12">At 11 a.m. on the morning of July 2, 1996, a St. Mary’s County (Maryland) Sheriff’s Deputy received a tip from a reliable confidential informant that respondent had gone to New York to buy drugs, and would be returning to Maryland in a rented red Toyota, license number DDY 787, later that day with a large quantity of cocaine. The deputy investí-<page-number citation-index="1" label="466">*466</page-number>gated the tip and found that the license number given to him by the informant belonged to a red Toyota Corolla that had been rented to respondent, who was a known drug dealer in St. Mary’s County. When respondent returned to St. Mary’s County in the rented car at 1 a.m. on July 3, the deputies stopped and searched the vehicle, finding 23 grams of crack cocaine in a duffel bag in the trunk. Respondent was arrested, tried, and convicted of conspiracy to possess cocaine with intent to distribute. He appealed, arguing that the trial court had erroneously denied his motion to suppress the cocaine on the alternative grounds that the police lacked probable cause, or that even if there was probable cause, the warrantless search violated the Fourth Amendment because there was sufficient time after the informant’s tip to obtain a warrant.</p>
<p id="b500-5">The Maryland Court of Special Appeals reversed, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/" aria-description="Citation for case: Dyson v. State">122 Md. App. 413</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/" aria-description="Citation for case: Dyson v. State">712 A. 2d 573</a></span> (1998), holding that in order for the automobile exception to the warrant requirement to apply, there must not only be probable cause to believe that evidence of a crime is contained in the automobile, but also a separate finding of exigency precluding the police from obtaining a warrant. <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#424" aria-description="Citation for case: Dyson v. State"><em>Id., </em>at 424</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#578" aria-description="Citation for case: Dyson v. State">712 A. 2d, at 578</a></span>. Applying this rule to the facts of the case, the Court of Special Appeals concluded that although there was “abundant probable cause,” the search violated the Fourth Amendment because there was no exigency that prevented or even made it significantly difficult for the police to obtain a search warrant. <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#426" aria-description="Citation for case: Dyson v. State"><em>Id., </em>at 426</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#579" aria-description="Citation for case: Dyson v. State">712 A. 2d, at 579</a></span>. The Maryland Court of Appeals denied certiorari. <span class="citation no-link">351 Md. 287</span>, <span class="citation no-link">718 A. 2d 235</span> (1998). We grant certiorari and now reverse.</p>
<p id="b500-6">The Fourth Amendment generally requires police to secure a warrant before conducting a search. <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390-391</a></span> (1985). As we recognized nearly 75 years ago in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925), there is an exception to this requirement for searches of vehicles. And under our established precedent, the “automobile exception” has no separate exigency re<page-number citation-index="1" label="467">*467</page-number>quirement. We made this clear in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 809</a></span> (1982), when we said that in cases where there was probable cause to search a vehicle “a search is not unreasonable if based on facts that would justify the issuance of a warrant, <em>even though a warrant has not been actually obtained.” </em>(Emphasis added.) In a case with virtually identical facts to this one (even down to the bag of cocaine in the trunk of the car), <em>Pennsylvania </em>v. <em>Labron, </em><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">518 U. S. 938</a></span> (1996) <em>(per curiam), </em>we repeated that the automobile exception does not have a separate exigency requirement: “If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment... permits police to search the vehicle without more.” <span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/#940" aria-description="Citation for case: Pennsylvania v. Labron"><em>Id., </em>at 940</a></span>.</p>
<p id="b501-5">In this case, the Court of Special Appeals found that there was “abundant probable cause” that the car contained contraband. This finding alone satisfies the automobile exception to the Fourth Amendment’s warrant requirement, a conclusion correctly reached by the trial court when it denied respondent’s motion to suppress. The holding of the Court of Special Appeals that the “automobile exception” requires a separate finding of exigency in addition to a finding of probable cause is squarely contrary to our holdings in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>and <em><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">Labron</a></span>. </em>We therefore grant the petition for writ of certiorari and reverse the judgment of the Court of Special Appeals.<footnotemark>*</footnotemark></p>
<p id="b501-6">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b501-7">Justice Breyer in dissent suggests that we should not summarily reverse a judgment in a criminal case, even though he agrees with this opinion as a matter of law. But to adopt that position would simply leave it in the hands of a respondent — who had obtained a lower court judgment manifestly wrong as a matter of federal constitutional law — to avoid summary reversal by the simple expedient of refusing to file a response. While we have on occasion appointed an attorney to file a brief as <em>amicus curiae </em>in a case where we have <em>granted </em>certiorari, in order to be sure that the argued case is fully briefed, we have never done so in cases which we have summarily reversed. The reason for this is that a summary reversal does not decide any new or unanswered question of law, but simply corrects a lower court’s demonstrably erroneous application of federal law.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Maryland v. Garrison.md  (`case`, 5 assertions)

### content_page

```
---
title: "Maryland v. Garrison"
type: case
citation: "480 U.S. 79 (1987)"
parallel_cite: "107 S. Ct. 1013; 94 L. Ed. 2d 72; 55 U.S.L.W. 4190"
neutral_cite: 1987 U.S. LEXIS 559
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Garrison
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111823/maryland-v-garrison/"
  cluster_id: 111823
  opinion_id: 9430836
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Hill v. California]]", "[[Groh v. Ramirez]]", "[[Andresen v. Maryland]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "particularity", "reasonable-mistake", "overbroad-warrant"]
holding: "A warrant's validity is judged on the information reasonably available to officers when they sought it; a reasonable, good-faith mistake…"
lake:
  record_id: Maryland v. Garrison
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Garrison

*480 U.S. 79 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers obtained a warrant to search "the third floor apartment" of a building they reasonably believed contained a single unit on that floor. In fact the third floor held two apartments. Before they realized their mistake, the officers entered Garrison's apartment (not the target's) and found contraband. They stopped once they recognized the third floor was divided.

## Issue
Whether a warrant valid on its face is invalidated by a latent factual mistake about the premises, and whether the officers' good-faith execution of the warrant before discovering the error violated the Fourth Amendment.

## Rule
Warrant validity is judged on the information reasonably available when it issued: "The validity of the warrant must be assessed on the basis of the information that the officers disclosed, or had a duty to discover and to disclose, to the issuing Magistrate." — 480 U.S. at 85. ^pin-85

And execution is judged for objective reasonableness in light of the facts then known: "the validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable." — *Id.* at 88. ^pin-88

## Application
When the officers applied for the warrant, the information available to them — and reasonably discoverable — indicated a single third-floor apartment, so the warrant was valid when issued despite the later-revealed ambiguity. As the officers executed it, the objective facts (a single doorbell, mailbox, and the like) gave them no reason to know the floor was divided; their failure to appreciate the overbreadth was objectively understandable and reasonable, and they limited the search once they recognized the error. The entry into Garrison's apartment was therefore constitutional.

## Conclusion
Affirmed: a warrant valid when issued is not retroactively invalidated by a latent factual mistake, and a search executed on an objectively reasonable, honest mistake about the premises does not violate the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Garrison* applies the reasonable-mistake logic of [[Hill v. California]] to warrant execution and remains good law on warrant [[Particularity|particularity]] and objectively reasonable execution; compare the facial-[[Particularity|particularity]] failure in [[Groh v. Ramirez]].

## Appears on
- [[Particularity]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Garrison*, 480 U.S. 79 (1987) — https://www.courtlistener.com/opinion/111823/maryland-v-garrison/ — pinpoints: 85, 88.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "77555bec023c118f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "480 U.S. 79 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 559", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1013; 94 L. Ed. 2d 72; 55 U.S.L.W. 4190", "title": "Maryland v. Garrison", "year": "1987"}}
{"assertion_id": "c0be0009c6df6cef", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Key — Progeny / Refinement", "title": "Maryland v. Garrison"}}
{"assertion_id": "fed950ce998f9e90", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant's validity is judged on the information reasonably available to officers when they sought it; a reasonable, good-faith mistake…", "title": "Maryland v. Garrison"}}
{"assertion_id": "1b683bbbb5843efb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Maryland v. Garrison", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Maryland v. Garrison", "varies_by_point": "false"}}
{"assertion_id": "98eb07ef54262b06", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Maryland v. Garrison"}}
```

### lake record — Maryland v. Garrison

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Garrison",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Garrison",
    "case_name_short": "Garrison",
    "case_name_full": "Maryland v. Garrison",
    "input_case_name": "Maryland v. Garrison",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-02-24",
    "year": 1987,
    "docket": null,
    "cluster_id": 111823,
    "lead_opinion_id": 9430836,
    "sibling_ids": [
      111823,
      9430836,
      9430837
    ],
    "absolute_url": "/opinion/111823/maryland-v-garrison/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 79",
      "volume": "480",
      "reporter": "U.S.",
      "page": "79",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1013",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 72",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4190",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 559",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "559",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 79",
        "volume": "480",
        "reporter": "U.S.",
        "page": "79",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1013",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 72",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 559",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "559",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4190",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 79",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 79",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-85",
      "page": null,
      "quote": "of a building they reasonably believed contained a single unit on that floor. In fact the third floor held two apartments. Before they realized their mistake, the officers entered Garrison's apartment (not the target's) and found contraband. They stopped once they recognized the third floor was divided. ## Issue Whether a warrant valid on its face is invalidated by a latent factual mistake about the premises, and whether the officers' good-faith execution of the warrant before discovering the error violated the Fourth Amendment. ## Rule Warrant validity is judged on the information reasonably available when it issued:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-88",
      "page": null,
      "quote": "the validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Garrison",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hector Feliciano(074395)",
          "cluster_id": 3183943,
          "cite": [
            "224 N.J. 351",
            "132 A.3d 1245",
            "2016 N.J. LEXIS 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
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
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948505,
          "cite": [
            "403 S.W.3d 867",
            "2013 Tex. Crim. App. LEXIS 531",
            "2013 WL 1136522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hamilton",
          "cluster_id": 893142,
          "cite": [
            "2012 NMCA 115",
            "3 N.M. 61"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bryan Santini v. Joseph Fuentes",
          "cluster_id": 2823503,
          "cite": [
            "795 F.3d 410",
            "2015 U.S. App. LEXIS 13552",
            "2015 WL 4620235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockett v. State",
          "cluster_id": 1148135,
          "cite": [
            "517 So. 2d 1317",
            "1987 WL 778"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curley v. Klem",
          "cluster_id": 1362944,
          "cite": [
            "499 F.3d 199",
            "2007 U.S. App. LEXIS 20213",
            "2007 WL 2404803"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. City of Madera",
          "cluster_id": 223714,
          "cite": [
            "648 F.3d 1119",
            "2011 U.S. App. LEXIS 17459",
            "2011 WL 3659355"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bradley",
          "cluster_id": 220050,
          "cite": [
            "644 F.3d 1213"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaime Soto, Also Known as Leonel Guerra",
          "cluster_id": 602824,
          "cite": [
            "988 F.2d 1548",
            "1993 U.S. App. LEXIS 5415",
            "1993 WL 77475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Archer v. John Chisholm",
          "cluster_id": 4422481,
          "cite": [
            "870 F.3d 603",
            "2017 WL 3709149",
            "2017 U.S. App. LEXIS 16493"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martin",
          "cluster_id": 1651199,
          "cite": [
            "721 N.W.2d 815",
            "271 Mich. App. 280"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard J. Leary, and F.L. Kleinberg & Co.",
          "cluster_id": 505922,
          "cite": [
            "846 F.2d 592",
            "1988 U.S. App. LEXIS 5755",
            "1988 WL 39811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Enrique Espinosa",
          "cluster_id": 493363,
          "cite": [
            "827 F.2d 604",
            "23 Fed. R. Serv. 963",
            "1987 U.S. App. LEXIS 12164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Riccardi",
          "cluster_id": 165743,
          "cite": [
            "405 F.3d 852",
            "2005 U.S. App. LEXIS 6631",
            "2005 WL 896430"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111823 OR 9430836 OR 9430837) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MTM0NDAwMDAwJnM9MjAxMDQ2MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111823+OR+9430836+OR+9430837%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111823 OR 9430836 OR 9430837)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDImcz01MTgwODgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111823+OR+9430836+OR+9430837%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111823 OR 9430836 OR 9430837)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 1,
        "triage_snippet_classified": 41
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111823 OR 9430836 OR 9430837)",
    "indexed_citing_opinions": 655,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111823,
        "count": 551,
        "count_source": "search"
      },
      {
        "opinion_id": 9430836,
        "count": 120,
        "count_source": "search"
      },
      {
        "opinion_id": 9430837,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1108,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-garrison.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MDQwOTUmcz0xMDAxMTYzNSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111823+OR+9430836+OR+9430837%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111823,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 290856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 328845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 340572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 1513305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 2379484,
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
    "date_created": "2026-07-05T11:56:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:59:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Garrison

```
<opinion type="majority">
<author id="b126-7">Justice Stevens</author>
<p id="Ahc">delivered the opinion of the Court.</p>
<p id="b126-8">Baltimore police officers obtained and executed a warrant to search the person of Lawrence McWebb and “the premises known as 2036 Park Avenue third floor apartment.”<footnotemark>1</footnotemark> When the police applied for the warrant and when they conducted the search pursuant to the warrant, they reasonably believed that there was only one apartment on the premises described in the warrant. In fact, the third floor was divided into two apartments, one occupied by McWebb and one by respondent Garrison. Before the officers executing the warrant became aware that they were in a separate apartment occupied by respondent, they had discovered the contraband that provided the basis for respondent’s conviction for violating Maryland’s Controlled Substances Act. The question presented is whether the seizure of that contraband was prohibited by the Fourth Amendment.</p>
<p id="b126-9">The trial court denied respondent’s motion to suppress the evidence seized from his apartment, App. 46, and the Mary<page-number citation-index="1" label="81">*81</page-number>land Court of Special Appeals affirmed. <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/" aria-description="Citation for case: Garrison v. State">58 Md. App. 417</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/" aria-description="Citation for case: Garrison v. State">473 A. 2d 514</a></span> (1984). The Court of Appeals of Maryland reversed and remanded with instructions to remand the case for a new trial. <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/" aria-description="Citation for case: Garrison v. State">303 Md. 385</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/" aria-description="Citation for case: Garrison v. State">494 A. 2d 193</a></span> (1985).</p>
<p id="b127-5">There is no question that the warrant was valid and was supported by probable cause. <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#392" aria-description="Citation for case: Garrison v. State"><em>Id., </em>at 392</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 196</a></span>. The trial court found, and the two appellate courts did not dispute, that after making a reasonable investigation, including a verification of information obtained from a reliable informant, an exterior examination of the three-story building at 2036 Park Avenue, and an inquiry of the utility company, the officer who obtained the warrant reasonably concluded that there was only one apartment on the third floor and that it was occupied by McWebb. App. 41; <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#433" aria-description="Citation for case: Garrison v. State">58 Md. App., at 433</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#522" aria-description="Citation for case: Garrison v. State">473 A. 2d, at 522</a></span>; <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#387" aria-description="Citation for case: Garrison v. State">303 Md., at 387-390</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#194" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 194-195</a></span>. When six Baltimore police officers executed the warrant, they fortuitously encountered McWebb in front of the building and used his key to gain admittance to the first-floor hallway and to the locked door at the top of the stairs to the third floor. As they entered the vestibule on the third floor, they encountered respondent, who was standing in the hallway area. The police could see into the interior of both Mc-Webb’s apartment to the left and respondent’s to the right, for the doors to both were open. Only after respondent’s apartment had been entered and heroin, cash, and drug paraphernalia had been found did any of the officers realize that the third floor contained two apartments. App. 41-46. As soon as they became aware of that fact, the search was discontinued. <em>Id., </em>at 32, 39. All of the officers reasonably believed that they were searching McWebb’s apartment.<footnotemark>2</footnotemark> No further search of respondent’s apartment was made.</p>
<p id="b128-4"><page-number citation-index="1" label="82">*82</page-number>The matter on which there is a difference of opinion concerns the proper interpretation of the warrant. A literal reading of its plain language, as well as the language used in the application for the warrant, indicates that it was intended to authorize a search of the entire third floor.<footnotemark>3</footnotemark> This is the construction adopted by the intermediate appellate court, see <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#419" aria-description="Citation for case: Garrison v. State">58 Md. App., at 419</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#515" aria-description="Citation for case: Garrison v. State">473 A. 2d, at 515</a></span>, and it also appears to be the construction adopted by the trial judge. See App. 41. One sentence in the trial judge’s oral opinion, however, lends support to the construction adopted by the Court of Appeals, namely, that the warrant authorized a search of McWebb’s apartment only.<footnotemark>4</footnotemark> Under that interpretation, the Court of <page-number citation-index="1" label="83">*83</page-number>Appeals concluded that the warrant did not authorize the search of respondent’s apartment and the police had no justification for making a warrantless entry into his premises.<footnotemark>5</footnotemark></p>
<p id="b129-4">The opinion of the Maryland Court of Appeals relies on Article 26 of the Maryland Declaration of Rights<footnotemark>6</footnotemark> and Maryland cases as well as the Fourth Amendment to the Federal Constitution and federal cases. Rather than containing any “plain statement” that the decision rests upon adequate and independent state grounds, see <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1042" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1042</a></span> (1983), the opinion indicates that the Maryland constitutional provision is construed <em>in pari materia </em>with the</p>
<p id="b130-7"><page-number citation-index="1" label="84">*84</page-number>Fourth Amendment.<footnotemark>7</footnotemark> We therefore have jurisdiction. Because the result that the Court of Appeals reached did not appear to be required by the Fourth Amendment, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./475/1009/">475 U. S. 1009</a></span> (1986). We reverse.</p>
<p id="b130-8">In our view, the case presents two separate constitutional issues, one concerning the validity of the warrant and the other concerning the reasonableness of the manner in which it was executed. See <em>Dalia </em>v. <em>United States, </em><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/#258" aria-description="Citation for case: Dalia v. United States">441 U. S. 238, 258</a></span> (1979). We shall discuss the questions separately.</p>
<p id="b130-9">I-H</p>
<p id="b130-3">The Warrant Clause of the Fourth Amendment categorically prohibits the issuance of any warrant except one “particularly describing the place to be searched and the persons or things to be seized.” The manifest purpose of this particularity requirement was to prevent general searches. By limiting the authorization to search to the specific areas and things for which there is probable cause to search, the requirement ensures that the search will be carefully tailored to its justifications, and will not take on the character of the wide-ranging exploratory searches the Framers intended to prohibit.<footnotemark>8</footnotemark> Thus, the scope of a lawful search is “defined by the object of the search and the places in which there is probable cause to believe that it may be found. Just as probable cause to believe that a stolen lawnmower may be found in a garage will not support a warrant to search an upstairs bedroom, probable cause to believe that undocumented aliens are being transported in a van will not justify a warrantless <page-number citation-index="1" label="85">*85</page-number>search of a suitcase.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824</a></span> (1982).</p>
<p id="b131-5">In this case there is no claim that the “persons or things to be seized” were inadequately described or that there was no probable cause to believe that those things might be found in “the place to be searched” as it was described in the warrant. With the benefit of hindsight, however, we now know that the description of that place was broader than appropriate because it was based on the mistaken belief that there was only one apartment on the third floor of the building at 2036 Park Avenue. The question is whether that factual mistake invalidated a warrant that undoubtedly would have been valid if it had reflected a completely accurate understanding of the building’s floor plan.</p>
<p id="b131-6">Plainly, if the officers had known, or even if they should have known, that there were two separate dwelling units on the third floor of 2036 Park Avenue, they would have been obligated to exclude respondent’s apartment from the scope of the requested warrant. But we must judge the constitutionality of their conduct in light of the information available to them at the time they acted. Those items of evidence that emerge after the warrant is issued have no bearing on whether or not a warrant was validly issued.<footnotemark>9</footnotemark> Just as the discovery of contraband cannot validate a warrant invalid when issued, so is it equally clear that the discovery of facts demonstrating that a valid warrant was unnecessarily broad does not retroactively invalidate the warrant. The validity of the warrant must be assessed on the basis of the information that the officers disclosed, or had a duty to discover and to disclose, to the issuing Magistrate.<footnotemark>10</footnotemark> On the basis of that <page-number citation-index="1" label="86">*86</page-number>information, we agree with the conclusion of all three Maryland courts that the warrant, insofar as it authorized a search that turned out to be ambiguous in scope, was valid when it issued.</p>
<p id="b132-5">II</p>
<p id="b132-6">The question whether the execution of the warrant violated respondent’s constitutional right to be secure in his home is somewhat less clear. We have no difficulty concluding that the officers’ entry into the third-floor common area was legal; they carried a warrant for those premises, and they were accompanied by McWebb, who provided the key that they used to open the door giving access to the third-floor common area. If the officers had known, or should have known, that the third floor contained two apartments before they entered the living quarters on the third floor, and thus had been aware of the error in the warrant, they would have been obligated to limit their search to McWebb’s apart<page-number citation-index="1" label="87">*87</page-number>ment. Moreover, as the officers recognized, they were required to discontinue the search of respondent’s apartment as soon as they discovered that there were two separate units on the third floor and therefore were put on notice of the risk that they might be in a unit erroneously included within the terms of the warrant. The officers’ conduct and the limits of the search were based on the information available as the search proceeded. While the purposes justifying a police search strictly limit the permissible extent of the search, the Court has also recognized the need to allow some latitude for honest mistakes that are made by officers in the dangerous and difficult process of making arrests and executing search warrants.<footnotemark>11</footnotemark></p>
<p id="b133-5">In <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), we considered the validity of the arrest of a man named Miller based on the mistaken belief that he was Hill. The police had probable cause to arrest Hill and they in good faith believed that Miller was Hill when they found him in Hill’s apartment. As we explained:</p>
<blockquote id="b133-6">“The upshot was that the officers in good faith believed Miller was Hill and arrested him. They Were quite wrong as it turned out, and subjective good-faith belief would not in itself justify either the arrest or the subsequent search. But sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers’ mistake was understandable and the arrest a reasonable response to the situation facing them at the time.” <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#803" aria-description="Citation for case: Hill v. California"><em>Id., </em>at 803-804</a></span>.</blockquote>
<p id="b133-7">While <em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">Hill</a></span> </em>involved an arrest without a warrant, its underlying rationale that an officer’s reasonable misidentification <page-number citation-index="1" label="88">*88</page-number>of a person does not invalidate a valid arrest is equally applicable to an officer’s reasonable failure to appreciate that a valid warrant describes too broadly the premises to be searched. Under the reasoning in <em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">Hill</a></span>, </em>the validity of the search of respondent’s apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers’ failure to realize the overbreadth of the warrant was objectively understandable and reasonable. Here it unquestionably was. The objective facts available to the officers at the time suggested no distinction between McWebb’s apartment and the third-floor premises.<footnotemark>12</footnotemark></p>
<p id="b134-5">For that reason, the officers properly responded to the command contained in a valid warrant even if the warrant is interpreted as authorizing a search limited to McWebb’s apartment rather than the entire third floor. Prior to the officers’ discovery of the factual mistake, they perceived McWebb’s apartment and the third-floor premises as one and the same; therefore their execution of the warrant reasonably included the entire third floor.<footnotemark>13</footnotemark> Under either interpretation of the warrant, the officers’ conduct was consistent with a reasonable effort to ascertain and identify the place intended to be searched within the meaning of the Fourth Amend<page-number citation-index="1" label="89">*89</page-number>ment.<footnotemark>14</footnotemark> Cf. <em>Steele </em>v. <em>United States, </em><span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#503" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 503</a></span> (1925).</p>
<p id="b135-4">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b135-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b126-11"><em> </em>App. 9, 41. The warrant was issued and executed on May 21, 1982. It authorized the Baltimore police to search the person of McWebb and “the premises known as 2036 Park Avenue third floor apartment” for “Marihuana, related paraphernalia, minies, books, papers, and photographs pertaining to the illegal distribution of Marihuana . . . .” <em>Id., </em>at 9.</p>
</footnote>
<footnote label="2">
<p id="b127-6"> While the search was in progress, an officer in respondent’s apartment answered the telephone. The caller asked for “Red Cross”; that was the name by which McWebb was known to the confidential informant. <em>Id., </em>at 6. Neither respondent nor McWebb indicated to the police during the search that there were two apartments. <em>Id., </em>at 38, 39-40.</p>
</footnote>
<footnote label="3">
<p id="b128-5"> The warrant states:</p>
<blockquote id="b128-6">“Affidavit having been made before me by Detective Albert Marcus, Baltimore Police Department, Narcotic Unit, that he has reason to believe that on the person of Lawrence Meril McWebb . . . [and] that on the premises known as 2036 Park Avenue third floor apartment, described as a three story brick dwelling with the numerals 2-0-3-6 affixed to the front of same in the City of Baltimore, there is now being concealed certain property ....</blockquote>
<blockquote id="b128-7">“You are therefor commanded, with the necessary and proper assistants, to search forthwith the person/premises hereinabove described for the property specified, executing this warrant and making the search . . . .” <em>Id., </em>at 9.</blockquote>
</footnote>
<footnote label="4">
<p id="b128-8"> Immediately before ruling on the suppression motions made by McWebb and Garrison, the court observed that a search of two or more apartments in the same building must be supported by probable cause for searching each apartment. The court added, “[t]here is an exception to this general rule where the multiple unit character of the premises is not externally apparent and is not known to the officer applying for or executing the warrant.” <em>Id., </em>at 45. The trial court then ruled, “It is clear that the warrant specified the premises to be searched as the third floor apartment of the Defendant McWebb . . . .” <em>Id., at </em>46. This statement only makes sense as a rejection of Garrison’s claim that “the warrant was a general warrant as it did not specify which apartment was to be searched on the third floor,” <em>id., </em>at 40, and as a recognition that the search was not invalid for lack of specificity in the warrant as to the premises to be searched. We interpret the trial court’s statement as a ruling that the search of a subunit of the building — which he referred to as “the third floor <page-number citation-index="1" label="83">*83</page-number>apartment of the Defendant McWebb” — was authorized by the warrant. The court then found on the precise facts of this ease that the search of Garrison’s apartment was valid because “the officers did not know that there was more than one apartment on the third floor and nothing alerted them of such a fact until after the search had been made and the items were [seized].” <em>Id., </em>at 46. The contrary construction adopted by the Court of Appeals fails to take into account the plain language of the warrant, which authorized a search of the person of McWebb and of the premises of 2036 Park Avenue, third floor. <em>Id., </em>at 9.</p>
</footnote>
<footnote label="5">
<p id="b129-9"> As the Court of Appeals explained:</p>
<blockquote id="b129-10">“It is undisputed that the police were authorized to search only one apartment, MeWebb’s; the warrant did not authorize the search of Garrison’s apartment. There is no question as to the validity of the search warrant itself. No argument was made in this Court that any of the exceptions to the warrant requirement applied here. It is clear, therefore, that the police had no authority to cross the threshold of Garrison’s apartment and seize evidence.</blockquote>
<blockquote id="b129-11">“Police had a warrant to search MeWebb’s apartment. They had no warrant to search Garrison’s. They had no justification for entering his premises, regardless of appearances.” <span class="citation no-link">303 Md. 386</span>, 392r394, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, 193, 196-197</a></span> (1985).</blockquote>
</footnote>
<footnote label="6">
<p id="b129-12"> Article 26 of the Maryland Declaration of Rights provides:</p>
<blockquote id="b129-13">“That all warrants, without oath or affirmation, to search suspected places, or to seize any person or property, are grevious [grievous] and oppressive; and all general warrants to search suspected places, or to apprehend suspected persons, without naming or describing the place, or the person in special, are illegal, and ought not to be granted.”</blockquote>
</footnote>
<footnote label="7">
<p id="b130-4"> <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#391" aria-description="Citation for case: Garrison v. State">303 Md., at 391</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 196</a></span>. This statement indicates that the “state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law . . . .” <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b130-5"> See <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 480</a></span> (1976); <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#569" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 569-572</a></span> (1969) (Stewart, J., concurring in result); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482, 485</a></span> (1965); <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931); <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#195" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 195-196</a></span> (1927).</p>
</footnote>
<footnote label="9">
<p id="b131-7"> Cf. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#115" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 115</a></span> (1984) (warrantless test of white powder; “[t]he reasonableness of an official invasion of the citizen’s privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred”).</p>
</footnote>
<footnote label="10">
<p id="b131-8">Arguments can certainly be made that the police in this case should have been able to ascertain that there was more than one apartment on the <page-number citation-index="1" label="86">*86</page-number>third floor of this building. It contained seven separate dwelling units and it was surely possible that two of them might be on the third floor. But the record also establishes that Officer Marcus made specific inquiries to determine the identity of the occupants of the third-floor premises. The officer went to 2036 Park Avenue and found that it matched the description given by the informant: a three-story brick dwelling with the numerals 2-0-3-6 affixed to the front of the premises. App. 7. The officer “made a cheek with the Baltimore Gas and Electric Company and discovered that the premises of 2036 Park Ave. third floor was in the name of Lawrence McWebb.” <em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span> </em>Officer Marcus testified at the suppression hearing that he inquired of the Baltimore Gas and Electric Company in whose name the third floor apartment was listed: “I asked if there is a front or rear or middle room. They told me, one third floor was only listed to Lawrence McWebb.” <em>Id., </em>at 36-38. The officer also discovered from a check with the Baltimore Police Department that the police records of Lawrence McWebb matched the address and physical description given by the informant. <em>Id., </em>at 7. The Maryland courts that are presumptively familiar with local conditions were unanimous in concluding that the officer reasonably believed McWebb was the only tenant on that floor. Because the evidence supports their conclusion, we accept that conclusion for the purpose of our decision.</p>
</footnote>
<footnote label="11">
<p id="b133-8"> “Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949).</p>
</footnote>
<footnote label="12">
<p id="b134-6"> Nothing McWebb did or said after he was detained outside 2036 Park Avenue would have suggested to the police that there were two apartments on the third floor. McWebb provided the key that opened the doors on the first floor and on the third floor. The police could reasonably have believed that McWebb was admitting them to an undivided apartment on the third floor. When the officers entered the foyer on the third floor, neither McWebb nor Garrison informed them that they lived in separate apartments. App. 39-40, 42.</p>
</footnote>
<footnote label="13">
<p id="b134-7"> We expressly distinguish the facts of this case from a situation in which the police know there are two apartments on a certain floor of a building, and have probable cause to believe that drugs are being sold out of that floor, but do not know in which of the two apartments the illegal transactions are taking place. A search pursuant to a warrant authorizing a search of the entire floor under those circumstances would present quite different issues from the ones before us in this case.</p>
</footnote>
<footnote label="14">
<p id="b135-8"> Respondent argued that the execution of the warrant violated the Fourth Amendment at the moment when the officers “walked in through that threshold of that house . . . .” Tr. ofOralArg. 35. At another point respondent argued that the search was illegal at the point when the police went through Garrison’s apartment without probable cause for his apartment. <em>Id., </em>at 43. For the purpose of addressing respondent’s argument, the exact point at which he asserts the search became illegal is not essential. Whether the illegal threshold is viewed as the beginning of the entire premises or as the beginning of those premises that, upon closer examination, turn out to be excluded from the intended scope of the warrant, we cannot accept respondent’s argument. It would brand as illegal the execution of any warrant in which, due to a mistake in fact, the premises intended to be searched vary from their description in the warrant. Yet in this case, in which the mistake in fact does not invalidate the warrant precisely because the police do not know of the mistake in fact when they apply for, receive, and prepare to execute the warrant, the police cannot reasonably know prior to their search that the warrant rests on a mistake in fact. It is only after the police begin to execute the warrant and set foot upon the described premises that they will discover the factual mistake and must reasonably limit their search accordingly.</p>
<p id="b135-9">Respondent proposes that the police conduct a preliminary survey of the premises whenever they search a building in which there are multiple dwelling units, in order to determine the extent of the premises to be searched. Id., at 42. We find no persuasive reason to impose such a burden over and above the bedrock requirement that, with the exceptions we have traced in our cases, the police may conduct searches only pursuant to a reasonably detailed warrant.</p>
</footnote>
</opinion>
```

---
