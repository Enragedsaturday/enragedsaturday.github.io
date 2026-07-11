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

## GROUP: _overhaul2/lake/cases/United States v. Jacobsen.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Jacobsen"
type: case
citation: "466 U.S. 109 (1984)"
parallel_cite: "104 S. Ct. 1652; 80 L. Ed. 2d 85; 52 U.S.L.W. 4414"
neutral_cite: 1984 U.S. LEXIS 53
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-04-02
docket: 82-1167
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Jacobsen
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/"
  cluster_id: 111143
  opinion_id: 111143
  identity_checked: true
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[Carpenter v. United States]]", "[[United States v. Jones]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-definition", "seizure-definition", "private-search-doctrine", "field-test", "government-action"]
holding: "Defines a property seizure; the Amendment reaches only government action — once a private party exposes contents, a government inspection within that scope invades no remaining privacy (private-search doctrine)."
lake:
  record_id: United States v. Jacobsen
  status: verified
  projected_at: 2026-07-09
---

# United States v. Jacobsen

*466 U.S. 109 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Express employees, following company policy after a forklift damaged a package, opened it and found a tube containing plastic bags of white powder. They notified the DEA and put the items back in the box. A DEA agent arrived, removed the bags from the tube, saw the powder, and conducted a field chemical test that identified it as cocaine. The agent had not obtained a warrant. The Eighth Circuit held the testing was an unlawful search.

## Issue
Whether a government agent's reexamination of a package — and a field chemical test of its contents — after a private party had already opened it and exposed the contents, constitutes a "search" or "seizure" within the meaning of the Fourth Amendment.

## Rule
The Fourth Amendment "protects two types of expectations, one involving 'searches,' the other 'seizures.'" — 466 U.S. at 113. "A 'search' occurs when an expectation of privacy that society is prepared to consider reasonable is infringed. A 'seizure' of property occurs when there is some meaningful interference with an individual's possessory interests in that property." — *Id.* ^pin-113

The Amendment reaches only government action; it is "wholly inapplicable 'to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government.'" — *Id.* ^pin-113a

Where a private search has already occurred, the government's later conduct is measured against it: "The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search." — [*Id.* at 115](https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/#:~:text=The%20additional%20invasions%20of%20respondents%27). ^pin-115

A test that reveals only the presence or absence of contraband is not a search: "A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy." — [*Id.* at 123](https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/#:~:text=A%20chemical%20test%20that%20merely). ^pin-123

## Application
On these facts there was no Fourth Amendment violation. The FedEx employees' opening of the package was private action, so it implicated no constitutional limit "because of their private character." The DEA agent's reexamination did not exceed the scope of that private search — he viewed and handled what the employees had already exposed — so it infringed no remaining expectation of privacy and was not a "search." The field test exceeded the private search but revealed only whether the powder was cocaine, compromising no legitimate privacy interest, and so was not a "search" either. The agent's destruction of a trace of the powder to run the test was a "seizure," but a reasonable one, because it is constitutionally reasonable to seize effects on probable cause to believe they contain contraband. Each step was therefore permissible.

## Conclusion
Neither the reinspection of the package nor the field test was an unreasonable search or seizure; the Eighth Circuit's judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Jacobsen* supplies the canonical Fourth Amendment definitions of "search" and "seizure," the government-action requirement, and the private-search doctrine; it remains good law and is read alongside the trespass/privacy framework of [[Katz v. United States]], [[United States v. Jones]], and [[Carpenter v. United States]].

## Appears on
- [[Private and Foreign Searches]] — *Key — Anchor*

## Sources
- *United States v. Jacobsen*, 466 U.S. 109 (1984) — https://www.courtlistener.com/opinion/111143/united-states-v-jacobsen/ — pinpoints: 113, 115, 123.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ba5df66592e6a62e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Jacobsen"}, "payload": {"all": [{"cite": "466 U.S. 109", "page": "109", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "466"}, {"cite": "104 S. Ct. 1652", "page": "1652", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "80 L. Ed. 2d 85", "page": "85", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "1984 U.S. LEXIS 53", "page": "53", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4414", "page": "4414", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "466 U.S. 109", "official": {"cite": "466 U.S. 109", "page": "109", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "466"}, "official_selection_present": true, "record_id": "United States v. Jacobsen"}}
{"assertion_id": "03e5ea89a04e2100", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-113a", "record_id": "United States v. Jacobsen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-113a", "pinpoint_status": "slip-only", "quote": "wholly inapplicable 'to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government.'", "quote_fidelity": "mismatch", "record_id": "United States v. Jacobsen", "star_marker": null}}
{"assertion_id": "25ccc4b07327536a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-113", "record_id": "United States v. Jacobsen"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-113", "pinpoint_status": "slip-only", "quote": "within the meaning of the Fourth Amendment. ## Rule The Fourth Amendment", "quote_fidelity": "mismatch", "record_id": "United States v. Jacobsen", "star_marker": null}}
{"assertion_id": "3e8e488db840386d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-115", "record_id": "United States v. Jacobsen"}, "payload": {"fragment": "#:~:text=The%20additional%20invasions%20of%20respondents%27", "page": null, "pin_id": "pin-115", "pinpoint_status": "star-verified", "quote": "The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search.", "quote_fidelity": "matched", "record_id": "United States v. Jacobsen", "star_marker": "115"}}
{"assertion_id": "ea139f0f17c4015e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-123", "record_id": "United States v. Jacobsen"}, "payload": {"fragment": "#:~:text=A%20chemical%20test%20that%20merely", "page": null, "pin_id": "pin-123", "pinpoint_status": "star-verified", "quote": "A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy.", "quote_fidelity": "matched", "record_id": "United States v. Jacobsen", "star_marker": "123"}}
{"assertion_id": "7c79f87fb6d948ee", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Jacobsen"}, "payload": {"as_of_content": "1984-04-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Jacobsen", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Jacobsen

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Jacobsen",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Jacobsen",
    "case_name_short": "Jacobsen",
    "case_name_full": "UNITED STATES v. JACOBSEN Et Al.",
    "input_case_name": "United States v. Jacobsen",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-04-02",
    "year": 1984,
    "docket": "82-1167",
    "cluster_id": 111143,
    "lead_opinion_id": 111143,
    "sibling_ids": [
      111143,
      9429558,
      9429559,
      9429560
    ],
    "absolute_url": "/opinion/111143/united-states-v-jacobsen/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 109",
      "volume": "466",
      "reporter": "U.S.",
      "page": "109",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 1652",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 85",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4414",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4414",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 53",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "53",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 109",
        "volume": "466",
        "reporter": "U.S.",
        "page": "109",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 1652",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 85",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "85",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 53",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "53",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4414",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4414",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 109",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 109",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule The Fourth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-113a",
      "page": null,
      "quote": "wholly inapplicable 'to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-115",
      "page": null,
      "quote": "The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search.",
      "star_marker": "115",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8004,
      "fragment": "#:~:text=The%20additional%20invasions%20of%20respondents%27",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-123",
      "page": null,
      "quote": "A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy.",
      "star_marker": "123",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19669,
      "fragment": "#:~:text=A%20chemical%20test%20that%20merely",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Jacobsen",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane1_negative"
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
        "journal_ref": "United States v. Jacobsen:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hudson v. Palmer",
          "cluster_id": 111252,
          "cite": [
            "82 L. Ed. 2d 393",
            "104 S. Ct. 3194",
            "468 U.S. 517",
            "1984 U.S. LEXIS 143",
            "52 U.S.L.W. 5052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
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
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oles v. State",
          "cluster_id": 1762668,
          "cite": [
            "993 S.W.2d 103",
            "1999 Tex. Crim. App. LEXIS 53",
            "1999 WL 330266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amores v. State",
          "cluster_id": 1670855,
          "cite": [
            "816 S.W.2d 407",
            "1991 Tex. Crim. App. LEXIS 183",
            "1991 WL 183121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Jacobsen:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI5MDIwODAwMDAwJnM9NDUwNzU5MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTkmcz0xMDYwNTkzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
        "reviewed": 80,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 80,
        "triage_read": 2,
        "triage_snippet_classified": 78
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111143 OR 9429558 OR 9429559 OR 9429560)",
    "indexed_citing_opinions": 1716,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111143,
        "count": 1456,
        "count_source": "search"
      },
      {
        "opinion_id": 9429558,
        "count": 288,
        "count_source": "search"
      },
      {
        "opinion_id": 9429559,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429560,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3226,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-jacobsen.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzODAyNjMmcz0xMDU5NzM3MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111143+OR+9429558+OR+9429559+OR+9429560%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111143,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 376747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 401057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 406270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
        "cited_id": 2114544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111143,
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
    "date_created": "2026-07-06T00:44:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:47:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:44:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Jacobsen

```
<div>
<center><b><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">466 U.S. 109</a></span> (1984)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
JACOBSEN ET AL.</h1></center>
<center>No. 82-1167.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 7, 1983</center>
<center>Decided April 2, 1984</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT
<p><span class="star-pagination">*110</span> <i>David A. Strauss</i> argued the cause for the United States. With him on the briefs were <i>Solicitor General Lee, Assistant Attorney General Jensen, Deputy Solicitor General Frey,</i> and <i>Joel M. Gershowitz.</i></p>
<p><i>Mark W. Peterson</i> argued the cause and filed a brief for respondents.<sup>[*]</sup></p>
<p><i>John Kenneth Zwerling</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p><span class="star-pagination">*111</span> JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>During their examination of a damaged package, the employees of a private freight carrier observed a white powdery substance, originally concealed within eight layers of wrappings. They summoned a federal agent, who removed a trace of the powder, subjected it to a chemical test and determined that it was cocaine. The question presented is whether the Fourth Amendment required the agent to obtain a warrant before he did so.</p>
<p>The relevant facts are not in dispute. Early in the morning of May 1, 1981, a supervisor at the Minneapolis-St. Paul Airport Federal Express office asked the office manager to look at a package that had been damaged and torn by a fork-lift. They then opened the package in order to examine its contents pursuant to a written company policy regarding insurance claims.</p>
<p>The container was an ordinary cardboard box wrapped in brown paper. Inside the box five or six pieces of crumpled newspaper covered a tube about 10 inches long; the tube was made of the silver tape used on basement ducts. The supervisor and office manager cut open the tube, and found a series of four zip-lock plastic bags, the outermost enclosing the other three and the innermost containing about six and a half ounces of white powder. When they observed the white powder in the innermost bag, they notified the Drug Enforcement Administration. Before the first DEA agent arrived, they replaced the plastic bags in the tube and put the tube and the newspapers back into the box.</p>
<p>When the first federal agent arrived, the box, still wrapped in brown paper, but with a hole punched in its side and the top open, was placed on a desk. The agent saw that one end of the tube had been slit open; he removed the four plastic bags from the tube and saw the white powder. He then opened each of the four bags and removed a trace of the <span class="star-pagination">*112</span> white substance with a knife blade. A field test made on the spot identified the substance as cocaine.<sup>[1]</sup></p>
<p>In due course, other agents arrived, made a second field test, rewrapped the package, obtained a warrant to search the place to which it was addressed, executed the warrant, and arrested respondents. After they were indicted for the crime of possessing an illegal substance with intent to distribute, their motion to suppress the evidence on the ground that the warrant was the product of an illegal search and seizure was denied; they were tried and convicted, and appealed. The Court of Appeals reversed. <span class="citation" data-id="9469462"><a href="/opinion/406270/united-states-v-bradley-thomas-jacobsen-and-donna-marie-jacobsen/" aria-description="Citation for case: United States v. Bradley Thomas Jacobsen and Donna Marie...">683 F. 2d 296</a></span> (CA8 1982). It held that the validity of the search warrant depended on the validity of the agents' warrantless test of the white powder,<sup>[2]</sup> that the testing constituted a significant expansion of the earlier private search, and that a warrant was required.</p>
<p>As the Court of Appeals recognized, its decision conflicted with a decision of another Court of Appeals on comparable facts, <i>United States</i> v. <i>Barry,</i> <span class="citation" data-id="9469019"><a href="/opinion/401057/united-states-v-richard-john-barry/" aria-description="Citation for case: United States v. Richard John Barry">673 F. 2d 912</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./459/927/">459 U. S. 927</a></span> (1982).<sup>[3]</sup> For that reason, and because <span class="star-pagination">*113</span> field tests play an important role in the enforcement of the narcotics laws, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./460/1021/">460 U. S. 1021</a></span>.</p>
<p></p>
<h2>I</h2>
<p>The first Clause of the Fourth Amendment provides that the "right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." This text protects two types of expectations, one involving "searches," the other "seizures." A "search" occurs when an expectation of privacy that society is prepared to consider reasonable is infringed.<sup>[4]</sup> A "seizure" of property occurs when there is some meaningful interference with an individual's possessory interests in that property.<sup>[5]</sup> This Court has also consistently construed this protection as proscribing only governmental action; it is wholly inapplicable "to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government or with the participation or knowledge of any governmental official." <i>Walter</i> v. <span class="star-pagination">*114</span> <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 662</a></span> (1980) (BLACKMUN, J., dissenting).<sup>[6]</sup></p>
<p>When the wrapped parcel involved in this case was delivered to the private freight carrier, it was unquestionably an "effect" within the meaning of the Fourth Amendment. Letters and other sealed packages are in the general class of effects in which the public at large has a legitimate expectation of privacy; warrantless searches of such effects are presumptively unreasonable.<sup>[7]</sup> Even when government agents may lawfully seize such a package to prevent loss or destruction of suspected contraband, the Fourth Amendment requires that they obtain a warrant before examining the contents of such a package.<sup>[8]</sup> Such a warrantless search could not be characterized as reasonable simply because, after the official invasion of privacy occurred, contraband is discovered.<sup>[9]</sup> Conversely, in this case the fact that agents of the private carrier independently opened the package and made an examination that might have been impermissible for a government agent <span class="star-pagination">*115</span> cannot render otherwise reasonable official conduct unreasonable. The reasonableness of an official invasion of the citizen's privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred.</p>
<p>The initial invasions of respondents' package were occasioned by private action. Those invasions revealed that the package contained only one significant item, a suspicious looking tape tube. Cutting the end of the tube and extracting its contents revealed a suspicious looking plastic bag of white powder. Whether those invasions were accidental or deliberate,<sup>[10]</sup> and whether they were reasonable or unreasonable, they did not violate the Fourth Amendment because of their private character.</p>
<p>The additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search. That standard was adopted by a majority of the Court in <i>Walter</i> v. <i>United States, supra</i><i>.</i> In <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> a private party had opened a misdirected carton, found rolls of motion picture films that appeared to be contraband, and turned the carton over to the Federal Bureau of Investigation. Later, without obtaining a warrant, FBI agents obtained a projector and viewed the films. While there was no single opinion of the Court, a majority did agree on the appropriate analysis of a governmental search which follows on the heels of a private one. Two Justices took the position:</p>
<blockquote>"If a properly authorized official search is limited by the particular terms of its authorization, at least the same kind of strict limitation must be applied to any official <span class="star-pagination">*116</span> use of a private party's invasion of another person's privacy. Even though some circumstances  for example, if the results of the private search are in plain view when materials are turned over to the Government  may justify the Government's reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search. In these cases, the private party had not actually viewed the films. Prior to the Government screening, one could only draw inferences about what was on the films. The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search." <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 657</a></span> (opinion of STEVENS, J., joined by Stewart, J.) (footnote omitted).<sup>[11]</sup></blockquote>
<p>Four additional Justices, while disagreeing with this characterization of the scope of the private search, were also of the view that the legality of the governmental search must be tested by the scope of the antecedent private search.</p>
<blockquote>"`Under these circumstances, since the L'Eggs employees so fully ascertained the nature of the films before contacting the authorities, we find that the FBI's subsequent viewing of the movies on a projector did not "change the nature of the search" and was not an additional search subject to the warrant requirement.' " <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#663" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 663-664</a></span> (BLACKMUN, J., dissenting, joined by BURGER, C. J., and POWELL and REHNQUIST, JJ.) (footnote omitted) (quoting <i>United States</i> v. <i>Sanders,</i> 592 <span class="star-pagination">*117</span> F. 2d 788, 793-794 (CA5 1979) (case below in <i>Walter</i>).<sup>[12]</sup></blockquote>
<p>This standard follows from the analysis applicable when private parties reveal other kinds of private information to the authorities. It is well settled that when an individual reveals private information to another, he assumes the risk that his confidant will reveal that information to the authorities, and if that occurs the Fourth Amendment does not prohibit governmental use of that information. Once frustration of the original expectation of privacy occurs, the Fourth Amendment does not prohibit governmental use of the now nonprivate information: "This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in a third party will not be betrayed." <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 443</a></span> (1976).<sup>[13]</sup> The Fourth Amendment is implicated only if the authorities use information with respect to which the expectation of privacy has not already been frustrated. In such a case the authorities have not relied on what is in effect a private <span class="star-pagination">*118</span> search, and therefore presumptively violate the Fourth Amendment if they act without a warrant.<sup>[14]</sup></p>
<p>In this case, the federal agents' invasions of respondents' privacy involved two steps: first, they removed the tube from the box, the plastic bags from the tube, and a trace of powder from the innermost bag; second, they made a chemical test of the powder. Although we ultimately conclude that both actions were reasonable for essentially the same reason, it is useful to discuss them separately.</p>
<p></p>
<h2>II</h2>
<p>When the first federal agent on the scene initially saw the package, he knew it contained nothing of significance except a tube containing plastic bags and, ultimately, white powder. It is not entirely clear that the powder was visible to him before he removed the tube from the box.<sup>[15]</sup> Even if the white <span class="star-pagination">*119</span> powder was not itself in "plain view" because it was still enclosed in so many containers and covered with papers, there was a virtual certainty that nothing else of significance was in the package and that a manual inspection of the tube and its contents would not tell him anything more than he already had been told. Respondents do not dispute that the Government could utilize the Federal Express employees' testimony concerning the contents of the package. If that is the case, it hardly infringed respondents' privacy for the agents to re-examine the contents of the open package by brushing aside a crumpled newspaper and picking up the tube. The advantage the Government gained thereby was merely avoiding the risk of a flaw in the employees' recollection, rather than in further infringing respondents' privacy. Protecting the risk of misdescription hardly enhances any legitimate privacy interest, and is not protected by the Fourth Amendment.<sup>[16]</sup> Respondents could have no privacy interest in the contents of the package, since it remained unsealed and since the Federal Express employees had just examined the package and had, of their own accord, invited the federal agent to their offices for the express purpose of viewing its contents. The agent's viewing of what a private party had freely made available for his inspection did not violate the Fourth Amendment. <span class="star-pagination">*120</span> See <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971); <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475-476</a></span> (1921).</p>
<p>Similarly, the removal of the plastic bags from the tube and the agent's visual inspection of their contents enabled the agent to learn nothing that had not previously been learned during the private search.<sup>[17]</sup> It infringed no legitimate expectation of privacy and hence was not a "search" within the meaning of the Fourth Amendment.</p>
<p>While the agents' assertion of dominion and control over the package and its contents did constitute a "seizure,"<sup>[18]</sup> that <span class="star-pagination">*121</span> seizure was not unreasonable. The fact that, prior to the field test, respondents' privacy interest in the contents of the package had been largely compromised is highly relevant to the reasonableness of the agents' conduct in this respect. The agents had already learned a great deal about the contents of the package from the Federal Express employees, all of which was consistent with what they could see. The package itself, which had previously been opened, remained unsealed, and the Federal Express employees had invited the agents to examine its contents. Under these circumstances, the package could no longer support any expectation of privacy; it was just like a balloon "the distinctive character [of which] spoke volumes as to its contents  particularly to the trained eye of the officer," <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#743" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 743</a></span> (1983) (plurality opinion); see also <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><i>id.,</i> at 746</a></span> (POWELL, J., concurring in judgment); or the hypothetical gun case in <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span> (1979). Such containers may be seized, at least temporarily, without a warrant.<sup>[19]</sup> Accordingly, since it was apparent that the tube and plastic bags contained contraband and little else, this warrantless seizure was reasonable,<sup>[20]</sup> for it is well settled that it is constitutionally reasonable for law enforcement officials to seize "effects" that cannot support a justifiable expectation <span class="star-pagination">*122</span> of privacy without a warrant, based on probable cause to believe they contain contraband.<sup>[21]</sup></p>
<p></p>
<h2>III</h2>
<p>The question remains whether the additional intrusion occasioned by the field test, which had not been conducted by the Federal Express employees and therefore exceeded the scope of the private search, was an unlawful "search" or "seizure" within the meaning of the Fourth Amendment.</p>
<p>The field test at issue could disclose only one fact previously unknown to the agent  whether or not a suspicious white powder was cocaine. It could tell him nothing more, not even whether the substance was sugar or talcum powder. We must first determine whether this can be considered a "search" subject to the Fourth Amendment  did it infringe an expectation of privacy that society is prepared to consider reasonable?</p>
<p>The concept of an interest in privacy that society is prepared to recognize as reasonable is, by its very nature, critically different from the mere expectation, however well justified, that certain facts will not come to the attention of the authorities.<sup>[22]</sup> Indeed, this distinction underlies the rule that <span class="star-pagination">*123</span> government may utilize information voluntarily disclosed to a governmental informant, despite the criminal's reasonable expectation that his associates would not disclose confidential information to the authorities. See <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#751" aria-description="Citation for case: United States v. White">401 U. S. 745, 751-752</a></span> (1971) (plurality opinion).</p>
<p>A chemical test that merely discloses whether or not a particular substance is cocaine does not compromise any legitimate interest in privacy. This conclusion is not dependent on the result of any particular test. It is probably safe to assume that virtually all of the tests conducted under circumstances comparable to those disclosed by this record would result in a positive finding; in such cases, no legitimate interest has been compromised. But even if the results are negative  merely disclosing that the substance is something other than cocaine  such a result reveals nothing of special interest. Congress has decided  and there is no question about its power to do so  to treat the interest in "privately" possessing cocaine as illegitimate; thus governmental conduct that can reveal whether a substance is cocaine, and no other arguably "private" fact, compromises no legitimate privacy interest.<sup>[23]</sup></p>
<p>This conclusion is dictated by <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), in which the Court held that subjecting luggage to a "sniff test" by a trained narcotics detection dog was not a "search" within the meaning of the Fourth Amendment:</p>
<blockquote>
<span class="star-pagination">*124</span> "A `canine sniff' by a well-trained narcotics detection dog, however, does not require opening the luggage. It does not expose noncontraband items that otherwise would remain hidden from public view, as does, for example, an officer's rummaging through the contents of the luggage. Thus, the manner in which information is obtained through this investigative technique is much less intrusive than a typical search. Moreover, the sniff discloses only the presence or absence of narcotics, a contraband item. Thus, despite the fact that the sniff tells the authorities something about the contents of the luggage, the information obtained is limited." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>.<sup>[24]</sup></blockquote>
<p>Here, as in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the likelihood that official conduct of the kind disclosed by the record will actually compromise any legitimate interest in privacy seems much too remote to characterize the testing as a search subject to the Fourth Amendment.</p>
<p>We have concluded, in Part II, <i>supra,</i> that the initial "seizure" of the package and its contents was reasonable. Nevertheless, as <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> also holds, a seizure lawful at its inception can nevertheless violate the Fourth Amendment because its manner of execution unreasonably infringes possessory interests protected by the Fourth Amendment's prohibition on "unreasonable seizures."<sup>[25]</sup> Here, the field test did affect respondents' possessory interests protected by the Amendment, since by destroying a quantity of the powder it converted <span class="star-pagination">*125</span> what had been only a temporary deprivation of possessory interests into a permanent one. To assess the reasonableness of this conduct, "[w]e must balance the nature and quality of the intrusion on the individual's Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S., at 703</a></span>.<sup>[26]</sup></p>
<p>Applying this test, we conclude that the destruction of the powder during the course of the field test was reasonable. The law enforcement interests justifying the procedure were substantial; the suspicious nature of the material made it virtually certain that the substance tested was in fact contraband. Conversely, because only a trace amount of material was involved, the loss of which appears to have gone unnoticed by respondents, and since the property had already been lawfully detained, the "seizure" could, at most, have only a <i>de minimis</i> impact on any protected property interest. Cf. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 591-592</a></span> (1974) (plurality opinion) (examination of automobile's tires and taking of paint scrapings was a <i>de minimis</i> invasion of constitutional interests).<sup>[27]</sup> Under these circumstances, the safeguards of a warrant would only minimally advance Fourth Amendment interests. This warrantless "seizure" was reasonable.<sup>[28]</sup></p>
<p><span class="star-pagination">*126</span> In sum, the federal agents did not infringe any constitutionally protected privacy interest that had not already been frustrated as the result of private conduct. To the extent that a protected possessory interest was infringed, the infringement was <i>de minimis</i> and constitutionally reasonable. The judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>JUSTICE WHITE, concurring in part and concurring in the judgment.</p>
<p>It is relatively easy for me to concur in the judgment in this case, since in my view the case should be judged on the basis of the Magistrate's finding that, when the first DEA agent arrived, the "tube was in plain view in the box and the bags with the white powder were visible from the end of the tube." App. to Pet. for Cert. 18a. Although this finding was challenged before the District Court, that court found it unnecessary to pass on the issue. <i><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Id.,</a></span></i> at 12a-13a. As I understand its opinion, however, the Court of Appeals accepted the Magistrate's finding: the Federal Express manager "placed the bags back in the tube, leaving them visible from the tube's end, and placed the tube back in the box"; he later gave the box to the DEA agent, who "removed the tube from the open box, took the bags out of the tube, and extracted a sample of the powder." <span class="citation" data-id="9469462"><a href="/opinion/406270/united-states-v-bradley-thomas-jacobsen-and-donna-marie-jacobsen/#297" aria-description="Citation for case: United States v. Bradley Thomas Jacobsen and Donna Marie...">683 F. 2d 296, 297</a></span> (CA8 1982). At the very least, the Court of Appeals assumed that <span class="star-pagination">*127</span> the contraband was in plain view. The Court of Appeals then proceeded to consider whether the federal agent's field test was an illegal extension of the private search, and it invalidated the field test solely for that reason.</p>
<p>Particularly since respondents argue here that whether or not the contraband was in plain view when the federal agent arrived is irrelevant and that the only issue is the validity of the field test, see, <i>e. g.,</i> Brief for Respondents 25, n. 11; Tr. of Oral Arg. 28, I would proceed on the basis that the clear plastic bags were in plain view when the agent arrived and that the agent thus properly observed the suspected contraband. On that basis, I agree with the Court's conclusion in Part III that the Court of Appeals erred in holding that the type of chemical test conducted here violated the Fourth Amendment.</p>
<p>The Court, however, would not read the Court of Appeals' opinion as having accepted the Magistrate's finding. It refuses to assume that the suspected contraband was visible when the first DEA agent arrived on the scene, conducts its own examination of the record, and devotes a major portion of its opinion to a discussion that would be unnecessary if the facts were as found by the Magistrate. The Court holds that even if the bags were not visible when the agent arrived, his removal of the tube from the box and the plastic bags from the tube and his subsequent visual examination of the bags' contents "infringed no legitimate expectation of privacy and hence was not a `search' within the meaning of the Fourth Amendment" because these actions "enabled the agent to learn nothing that had not previously been learned during the private search." <i>Ante,</i> at 120 (footnote omitted). I disagree with the Court's approach for several reasons.</p>
<p>First, as I have already said, respondents have abandoned any attack on the Magistrate's findings; they assert that it is irrelevant whether the suspected contraband was in plain view when the first DEA agent arrived and argue only that the plastic bags could not be opened and their contents tested <span class="star-pagination">*128</span> without a warrant. In short, they challenge only the expansion of the private search, place no reliance on the fact that the plastic bags containing the suspected contraband might not have been left in plain view by the private searchers, and do not contend that their Fourth Amendment rights were violated by the duplication of the private search they alleged in the District Court was necessitated by the condition to which the private searchers returned the package. In these circumstances, it would be the better course for the Court to decide the case on the basis of the facts found by the Magistrate and not rejected by the Court of Appeals, to consider only whether the alleged expansion of the private search by the field test violated the Fourth Amendment, and to leave for another day the question whether federal agents could have duplicated the prior private search had that search not left the contraband in plain view.</p>
<p>Second, if the Court feels that the Magistrate may have erred in concluding that the white powder was in plain view when the first agent arrived and believes that respondents have not abandoned their challenge to the agent's duplication of the prior private search, it nevertheless errs in responding to that challenge. The task of reviewing the Magistrate's findings belongs to the District Court and the Court of Appeals in the first instance. We should request that they perform that function, particularly since if the Magistrate's finding that the contraband was in plain view when the federal agent arrived were to be sustained, there would be no need to address the difficult constitutional question decided today. The better course, therefore, would be to remand the case after rejecting the Court of Appeals' decision invalidating the field test as an illegal expansion of the private search.</p>
<p>Third, if this case must be judged on the basis that the plastic bags and their contents were concealed when the first agent arrived, I disagree with the Court's conclusion that the agent could, without a warrant, uncover or unwrap the tube <span class="star-pagination">*129</span> and remove its contents simply because a private party had previously done so. The remainder of this opinion will address this issue.</p>
<p>The governing principles with respect to the constitutional protection afforded closed containers and packages may be readily discerned from our cases. The Court has consistently rejected proposed distinctions between worthy and unworthy containers and packages, <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#815" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 815, 822-823</a></span> (1982); <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#425" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 425-426</a></span> (1981) (plurality opinion), and has made clear that "the Fourth Amendment provides protection to the owner of every container that conceals its contents from plain view" and does not otherwise unmistakably reveal its contents. <i>United States</i> v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross"><i>Ross, supra,</i> at 822-823</a></span>; see <i>Robbins</i> v. <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#427" aria-description="Citation for case: Robbins v. California"><i>California, supra,</i> at 427-428</a></span> (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764, n. 13</a></span> (1979). Although law enforcement officers may sometimes seize such containers and packages pending issuance of warrants to examine their contents, <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701</a></span> (1983); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#749" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 749-750</a></span> (1983) (STEVENS, J., concurring in judgment), the mere existence of probable cause to believe that a container or package contains contraband plainly cannot justify a warrantless examination of its contents. <i>Ante,</i> at 114; <i>United States</i> v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross"><i>Ross, supra,</i> at 809-812</a></span>; <i>Arkansas</i> v. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders"><i>Sanders, supra,</i> at 762</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13</a></span>, and n. 8 (1977).</p>
<p>This well-established prohibition of warrantless searches has applied notwithstanding the manner in which the police obtained probable cause. The Court now for the first time sanctions warrantless searches of closed or covered containers or packages whenever probable cause exists as a result of a prior private search. It declares, in fact, that governmental inspections following on the heels of private searches are not searches at all as long as the police do no more than the private parties have already done. In reaching this conclusion, the Court excessively expands our prior decisions recognizing <span class="star-pagination">*130</span> that the Fourth Amendment proscribes only governmental action. <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971).</p>
<p>As the Court observes, the Fourth Amendment "is wholly inapplicable `to a search or seizure, even an unreasonable one, effected by a private individual not acting as an agent of the Government or with the participation or knowledge of any governmental official.' " <i>Ante,</i> at 113 (quoting <i>Walter</i> v. <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S. 649, 662</a></span> (1980) (BLACKMUN, J., dissenting)). Where a private party has revealed to the police information he has obtained during a private search or exposed the results of his search to plain view, no Fourth Amendment interest is implicated because the police have done no more than fail to avert their eyes. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#489" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 489</a></span>.</p>
<p>The private-search doctrine thus has much in common with the plain-view doctrine, which is "grounded on the proposition that once police are lawfully in a position <i>to observe an item firsthand,</i> its owner's privacy interest in that item is lost . . . ." <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983) (emphasis added). It also shares many of the doctrinal underpinnings of cases establishing that "the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities," <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 443</a></span> (1976), although the analogy is imperfect since the risks assumed by a person whose belongings are subjected to a private search are not comparable to those assumed by one who voluntarily chooses to reveal his secrets to a companion.</p>
<p>Undoubtedly, the fact that a private party has conducted a search "that might have been impermissible for a government agent cannot render otherwise reasonable official conduct unreasonable." <i>Ante,</i> at 114-115. But the fact that a repository of personal property previously was searched by a private party has never been used to legitimize <i>governmental conduct</i> that otherwise would be subject to challenge under <span class="star-pagination">*131</span> the Fourth Amendment. If government agents are unwilling or unable to rely on information or testimony provided by a private party concerning the results of a private search and that search has not left incriminating evidence in plain view, the agents may wish to duplicate the private search to observe firsthand what the private party has related to them or to examine and seize the suspected contraband the existence of which has been reported. The information provided by the private party clearly would give the agents probable cause to secure a warrant authorizing such actions. Nothing in our previous cases suggests, however, that the agents may proceed to conduct their own search of the same or lesser scope as the private search without first obtaining a warrant. <i>Walter</i> v. <i>United States, supra,</i> at 660-662 (WHITE, J., concurring in part and concurring in judgment).</p>
<p><i>Walter</i> v. <i>United States</i><i>,</i> on which the majority heavily relies in opining that "[t]he additional invasions of respondents' privacy by the Government agent must be tested by the degree to which they exceeded the scope of the private search," <i>ante,</i> at 115, does not require that conclusion. JUSTICE STEVENS' opinion in <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> does contain language suggesting that the government is free to do all of what was done earlier by the private searchers. But this language was unnecessary to the decision, as JUSTICE STEVENS himself recognized in leaving open the question whether "the Government would have been required to obtain a warrant had the private party been the first to view [the films]," <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States">447 U. S., at 657, n. 9</a></span>, and in emphasizing that "[e]ven though some circumstances  for example, <i>if the results of the private search are in plain view when materials are turned over to the Government</i>  may justify the Government's reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search." <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#657" aria-description="Citation for case: Walter v. United States"><i>Id.,</i> at 657</a></span> (emphasis added). Nor does JUSTICE BLACKMUN's dissent in <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span></i> necessarily support today's holding, for it emphasized that the opened containers <span class="star-pagination">*132</span> turned over to the Government agents "clearly revealed the nature of their contents," <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#663" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 663</a></span>; see <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#665" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 665</a></span>, and the facts of this case, at least as viewed by the Court, do not support such a conclusion.</p>
<p>Today's decision also is not supported by the majority's reference to cases involving the transmission of previously private information to the police by a third party who has been made privy to that information. <i>Ante,</i> at 117-118. The police may, to be sure, use confidences revealed to them by a third party to establish probable cause or for other purposes, and the third party may testify about those confidences at trial without violating the Fourth Amendment. But we have never intimated until now that an individual who reveals that he stores contraband in a particular container or location to an acquaintance who later betrays his confidence has no expectation of privacy in that container or location and that the police may thus search it without a warrant.</p>
<p>That, I believe, is the effect of the Court's opinion. If a private party breaks into a locked suitcase, a locked car, or even a locked house, observes incriminating information, returns the object of his search to its prior locked condition, and then reports his findings to the police, the majority apparently would allow the police to duplicate the prior search on the ground that the private search vitiated the owner's expectation of privacy. As JUSTICE STEVENS has previously observed, this conclusion cannot rest on the proposition that the owner no longer has a subjective expectation of privacy since a person's expectation of privacy cannot be altered by subsequent events of which he was unaware. <i>Walter</i> v. <i>United States, supra,</i> at 659, n. 12.</p>
<p>The majority now ignores an individual's subjective expectations and suggests that "[t]he reasonableness of an official invasion of a citizen's privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred." <i>Ante,</i> at 115. On that view, however, the reasonableness of a particular individual's remaining expectation of privacy should turn entirely on whether the private <span class="star-pagination">*133</span> search left incriminating evidence or contraband in plain view. Cf. <i>Walter</i> v. <i>United States, supra,</i> at 663, 665 (BLACKMUN, J., dissenting). If the evidence or contraband is not in plain view and not in a container that clearly announces its contents at the end of a private search, the government's subsequent examination of the previously searched object necessarily constitutes an independent, governmental search that infringes Fourth Amendment privacy interests. <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#662" aria-description="Citation for case: Walter v. United States">447 U. S., at 662</a></span> (WHITE, J., concurring in part and concurring in judgment).</p>
<p>The majority opinion is particularly troubling when one considers its logical implications. I would be hard-pressed to distinguish this case, which involves a private search, from (1) one in which the private party's knowledge, later communicated to the government, that a particular container concealed contraband and nothing else arose from his presence at the time the container was sealed; (2) one in which the private party learned that a container concealed contraband and nothing else when it was previously opened in his presence; or (3) one in which the private party knew to a certainty that a container concealed contraband and nothing else as a result of conversations with its owner. In each of these cases, the approach adopted by the Court today would seem to suggest that the owner of the container has no legitimate expectation of privacy in its contents and that government agents opening that container without a warrant on the strength of information provided by the private party would not violate the Fourth Amendment.</p>
<p>Because I cannot accept the majority's novel extension of the private-search doctrine and its implications for the entire concept of legitimate expectations of privacy, I concur only in Part III of its opinion and in the judgment.</p>
<p>JUSTICE BRENNAN, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>This case presents two questions: first whether law enforcement officers may conduct a warrantless search of the <span class="star-pagination">*134</span> contents of a container merely because a private party has previously examined the container's contents and informed the officers of its suspicious nature; and second, whether law enforcement officers may conduct a chemical field test of a substance once the officers have legitimately located the substance. Because I disagree with the Court's treatment of each of these issues, I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>I agree entirely with JUSTICE WHITE that the Court has expanded the reach of the private-search doctrine far beyond its logical bounds. <i>Ante,</i> at 127-133 (WHITE, J., concurring in judgment). It is difficult to understand how respondents can be said to have no expectation of privacy in a closed container simply because a private party has previously opened the container and viewed its contents. I also agree with JUSTICE WHITE, however, that if the private party presents the contents of a container to a law enforcement officer in such a manner that the contents are plainly visible, the officer's visual inspection of the contents does not constitute a "search" within the meaning of the Fourth Amendment. Because the record in this case is unclear on the question whether the contents of respondents' package were plainly visible when the Federal Express employee showed the package to the DEA officer, I would remand the case for further factfinding on this central issue.</p>
<p></p>
<h2>II</h2>
<p>As noted, I am not persuaded that the DEA officer actually came upon respondents' cocaine without violating the Fourth Amendment and, accordingly, I need not address the legality of the chemical field test. Since the Court has done so, however, I too will address the question, assuming, <i>arguendo,</i> that the officer committed neither an unconstitutional search nor an unconstitutional seizure prior to the point at which he took the sample of cocaine out of the plastic bags to conduct the test.</p>
<p></p>
<h2>
<span class="star-pagination">*135</span> A</h2>
<p>I agree that, under the hypothesized circumstances, the field test in this case was not a search within the meaning of the Fourth Amendment for the following reasons: <i>First,</i> the officer came upon the white powder innocently; <i>second,</i> under the hypothesized circumstances, respondents could not have had a reasonable expectation of privacy in the chemical identity of the powder because the DEA agents were already able to identify it as contraband with virtual certainty, <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#750" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 750-751</a></span> (1983) (STEVENS, J., concurring in judgment); and <i>third,</i> the test required the destruction of only a minute quantity of the powder. The Court, however, has reached this conclusion on a much broader ground, relying on two factors alone to support the proposition that the field test was not a search: <i>First,</i> the fact that the test revealed only whether or not the substance was cocaine, without providing any further information; and <i>second,</i> the assumption that an individual does not have a reasonable expectation of privacy in such a fact.</p>
<p>The Court asserts that its "conclusion is dictated by <i>United States</i> v. <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i>" <i>ante,</i> at 123, in which the Court stated that a "canine sniff" of a piece of luggage did not constitute a search because it "is much less intrusive than a typical search," and because it "discloses only the presence or absence of narcotics, a contraband item." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983). Presumably, the premise of <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was that an individual could not have a reasonable expectation of privacy in the presence or absence of narcotics in his luggage. The validity of the canine sniff in that case, however, was neither briefed by the parties nor addressed by the courts below. Indeed, since the Court ultimately held that the defendant's luggage had been impermissibly seized, its discussion of the question was wholly unnecessary to its judgment. In short, as JUSTICE BLACKMUN pointed out at the time, "[t]he Court [was] certainly in no position to consider all the ramifications of this important issue." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#723" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 723-724</a></span>.</p>
<p><span class="star-pagination">*136</span> Nonetheless, the Court concluded:</p>
<blockquote>"[T]he canine sniff is <i>sui generis.</i> We are aware of no other investigative procedure that is so limited both in the manner in which the information is obtained and in the content of the information revealed by the procedure. Therefore, we conclude that the particular course of investigation that the agents intended to pursue here  exposure of respondent's luggage, which was located in a public place, to a trained canine  did not constitute a `search' within the meaning of the Fourth Amendment." <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>Id.,</i> at 707</a></span>.</blockquote>
<p>As it turns out, neither the Court's knowledge nor its imagination regarding criminal investigative techniques proved very sophisticated, for within one year we have learned of another investigative procedure that shares with the dog sniff the same defining characteristics that led the Court to suggest that the dog sniff was not a search.</p>
<p>Before continuing along the course that the Court so hastily charted in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> it is only prudent to take this opportunity  in my view, the first real opportunity  to consider the implications of the Court's new Fourth Amendment jurisprudence. Indeed, in light of what these two cases have taught us about contemporary law enforcement methods, it is particularly important that we analyze the basis upon which the Court has redefined the term "search" to exclude a broad class of surveillance techniques. In my view, such an analysis demonstrates that, although the Court's conclusion is correct in this case, its dictum in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> was dangerously incorrect. More important, however, the Court's reasoning in both cases is fundamentally misguided and could potentially lead to the development of a doctrine wholly at odds with the principles embodied in the Fourth Amendment.</p>
<p>Because the requirements of the Fourth Amendment apply only to "searches" and "seizures," an investigative technique <span class="star-pagination">*137</span> that falls within neither category need not be reasonable and may be employed without a warrant and without probable cause, regardless of the circumstances surrounding its use. The prohibitions of the Fourth Amendment are not, however, limited to any preconceived conceptions of what constitutes a search or a seizure; instead we must apply the constitutional language to modern developments according to the fundamental principles that the Fourth Amendment embodies. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 356 (1974). Before excluding a class of surveillance techniques from the reach of the Fourth Amendment, therefore, we must be certain that none of the techniques so excluded threatens the areas of personal security and privacy that the Amendment is intended to protect.</p>
<p>What is most startling about the Court's interpretation of the term "search," both in this case and in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> is its exclusive focus on the nature of the information or item sought and revealed through the use of a surveillance technique, rather than on the context in which the information or item is concealed. Combining this approach with the blanket assumption, implicit in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and explicit in this case, that individuals in our society have no reasonable expectation of privacy in the fact that they have contraband in their possession, the Court adopts a general rule that a surveillance technique does not constitute a search if it reveals only whether or not an individual possesses contraband.</p>
<p>It is certainly true that a surveillance technique that identifies only the presence or absence of contraband is less intrusive than a technique that reveals the precise nature of an item regardless of whether it is contraband. But by seizing upon this distinction alone to conclude that the first type of technique, as a general matter, is not a search, the Court has foreclosed any consideration of the circumstances under which the technique is used, and may very well have paved <span class="star-pagination">*138</span> the way for technology to override the limits of law in the area of criminal investigation.</p>
<p>For example, under the Court's analysis in these cases, law enforcement officers could release a trained cocaine-sensitive dog  to paraphrase the California Court of Appeal, a "canine cocaine connoisseur"  to roam the streets at random, alerting the officers to people carrying cocaine. Cf. <i>People</i> v. <i>Evans,</i> <span class="citation" data-id="2114544"><a href="/opinion/2114544/people-v-evans/#932" aria-description="Citation for case: People v. Evans">65 Cal. App. 3d 924, 932</a></span>, <span class="citation" data-id="2114544"><a href="/opinion/2114544/people-v-evans/#440" aria-description="Citation for case: People v. Evans">134 Cal. Rptr. 436, 440</a></span> (1977). Or, if a device were developed that, when aimed at a person, would detect instantaneously whether the person is carrying cocaine, there would be no Fourth Amendment bar, under the Court's approach, to the police setting up such a device on a street corner and scanning all passersby. In fact, the Court's analysis is so unbounded that if a device were developed that could detect, from the outside of a building, the presence of cocaine inside, there would be no constitutional obstacle to the police cruising through a residential neighborhood and using the device to identify all homes in which the drug is present. In short, under the interpretation of the Fourth Amendment first suggested in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> and first applied in this case, these surveillance techniques would not constitute searches and therefore could be freely pursued whenever and wherever law enforcement officers desire. Hence, at some point in the future, if the Court stands by the theory it has adopted today, search warrants, probable cause, and even "reasonable suspicion" may very well become notions of the past. Fortunately, we know from precedents such as <i>Katz</i> v. <i>United States, supra</i><i>,</i> overruling the "trespass" doctrine of <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span> (1942), and <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), that this Court ultimately stands ready to prevent this Orwellian world from coming to pass.</p>
<p>Although the Court accepts, as it must, the fundamental proposition that an investigative technique is a search within the meaning of the Fourth Amendment if it intrudes upon a privacy expectation that society considers to be reasonable, <span class="star-pagination">*139</span> <i>ante,</i> at 113, the Court has entirely omitted from its discussion the considerations that have always guided our decisions in this area. In determining whether a reasonable expectation of privacy has been violated, we have always looked to the context in which an item is concealed, not to the identity of the concealed item. Thus in cases involving searches for physical items, the Court has framed its analysis first in terms of the expectation of privacy that normally attends the location of the item and ultimately in terms of the legitimacy of that expectation. In <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), for example, we held that "[n]o less than one who locks the doors of his home against intruders, one who safeguards his possessions [by locking them in a footlocker] is due the protection of the Fourth Amendment . . . ." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 11</a></span>. Our holding was based largely on the observation that, "[b]y placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination." <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></i> The Court made the same point in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 822-823</a></span> (1982), where it held that the "Fourth Amendment provides protection to the owner of every container that conceals its contents from plain view." The fact that a container contains contraband, which indeed it usually does in such cases, has never altered our analysis.</p>
<p>Similarly, in <i>Katz</i> v. <i>United States</i><i>,</i> we held that electronic eavesdropping constituted a search under the Fourth Amendment because it violated a reasonable expectation of privacy. In reaching that conclusion, we focused upon the private context in which the conversation in question took place, stating: "What a person knowingly exposes to the public . . . is not a subject of Fourth Amendment protection. . . . But what he seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351-352</a></span>. Again, the fact that the conversations involved in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> were incriminating did not alter our consideration of the <span class="star-pagination">*140</span> privacy issue. Nor did such a consideration affect our analysis in <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), in which we reaffirmed the principle that the home is private even though it may be used to harbor a fugitive.</p>
<p>In sum, until today this Court has always looked to the manner in which an individual has attempted to preserve the private nature of a particular fact before determining whether there is a reasonable expectation of privacy upon which the government may not intrude without substantial justification. And it has always upheld the general conclusion that searches constitute at least "those more extensive intrusions that significantly jeopardize the sense of security which is the paramount concern of Fourth Amendment liberties." <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S. 745, 786</a></span> (1971) (Harlan, J., dissenting).</p>
<p>Nonetheless, adopting the suggestion in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the Court has veered away from this sound and well-settled approach and has focused instead solely on the product of the would-be search. In so doing, the Court has ignored the fundamental principle that "[a] search prosecuted in violation of the Constitution is not made lawful by what it brings to light." <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927). The unfortunate product of this departure from precedent is an undifferentiated rule allowing law enforcement officers free rein in utilizing a potentially broad range of surveillance techniques that reveal only whether or not contraband is present in a particular location. The Court's new rule has rendered irrelevant the circumstances surrounding the use of the technique, the accuracy of the technique, and the privacy interest upon which it intrudes. Furthermore, the Court's rule leaves no room to consider whether the surveillance technique is employed randomly or selectively, a consideration that surely implicates Fourth Amendment concerns. See 2 W. LaFave, Search and Seizure § 2.2(f) (1978). Although a technique that reveals only the presence or absence of illegal <span class="star-pagination">*141</span> activity intrudes less into the private life of an individual under investigation than more conventional techniques, the fact remains that such a technique does intrude. In my view, when the investigation intrudes upon a domain over which the individual has a reasonable expectation of privacy, such as his home or a private container, it is plainly a search within the meaning of the Fourth Amendment. Surely it cannot be that the individual's reasonable expectation of privacy dissipates simply because a sophisticated surveillance technique is employed.</p>
<p>This is not to say that the limited nature of the intrusion has no bearing on the general Fourth Amendment inquiry. Although there are very few exceptions to the general rule that warrantless searches are presumptively unreasonable, the isolated exceptions that do exist are based on a "balancing [of] the need to search against the invasion which the search entails." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967). Hence it may be, for example, that the limited intrusion effected by a given surveillance technique renders the employment of the technique, under particular circumstances, a "reasonable" search under the Fourth Amendment. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#723" aria-description="Citation for case: United States v. Place">462 U. S., at 723</a></span> (BLACKMUN, J., concurring in judgment) ("a dog sniff may be a search, but a minimally intrusive one that could be justified in this situation under <i>Terry</i>"). At least under this wellsettled approach, the Fourth Amendment inquiry would be broad enough to allow consideration of the method by which a surveillance technique is employed as well as the circumstances attending its use. More important, however, it is only under this approach that law enforcement procedures, like those involved in this case and in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> may continue to be governed by the safeguards of the Fourth Amendment.</p>
<p></p>
<h2>B</h2>
<p>In sum, the question whether the employment of a particular surveillance technique constitutes a search depends on <span class="star-pagination">*142</span> whether the technique intrudes upon a reasonable expectation of privacy. This inquiry, in turn, depends primarily on the private nature of the area or item subjected to the intrusion. In cases involving techniques used to locate or identify a physical item, the manner in which a person has attempted to shield the item's existence or identity from public scrutiny will usually be the key to determining whether a reasonable expectation of privacy has been violated. Accordingly, the use of techniques like the dog sniff at issue in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> constitutes a search whenever the police employ such techniques to secure any information about an item that is concealed in a container that we are prepared to view as supporting a reasonable expectation of privacy. The same would be true if a more technologically sophisticated method were developed to take the place of the dog.</p>
<p>In this case, the chemical field test was used to determine whether certain white powder was cocaine. Upon visual inspection of the powder in isolation, one could not identify it as cocaine. In the abstract, therefore, it is possible that an individual could keep the powder in such a way as to preserve a reasonable expectation of privacy in its identity. For instance, it might be kept in a transparent pharmaceutical vial and disguised as legitimate medicine. Under those circumstances, the use of a chemical field test would constitute a search. However, in this case, as hypothesized above, see <i>supra,</i> at 134, the context in which the powder was found could not support a reasonable expectation of privacy. In particular, the substance was found in four plastic bags, which had been inside a tube wrapped with tape and sent to respondents via Federal Express. It was essentially inconceivable that a legal substance would be packaged in this manner for transport by a common carrier. Thus, viewing the powder as they did at the offices of Federal Express, the DEA agent could identify it with "virtual certainty"; it was essentially as though the chemical identity of the powder was <span class="star-pagination">*143</span> plainly visible. See <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#751" aria-description="Citation for case: Texas v. Brown">460 U. S., at 751</a></span> (STEVENS, J., concurring in judgment). Under these circumstances, therefore, respondents had no reasonable expectation of privacy in the identity of the powder, and the use of the chemical field test did not constitute a "search" violative of the Fourth Amendment.</p>
<h2>NOTES</h2>
<p>[*]  <i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak, Howard G. Berringer, David Crump, Daniel B. Hales, William B. Randall,</i> and <i>Evelle J. Younger</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  As the test is described in the evidence, it involved the use of three test tubes. When a substance containing cocaine is placed in one test tube after another, it will cause liquids to take on a certain sequence of colors. Such a test discloses whether or not the substance is cocaine, but there is no evidence that it would identify any other substances.</p>
<p>[2]  The Court of Appeals did not hold that the facts would not have justified the issuance of a warrant without reference to the test results; the court merely held that the facts recited in the warrant application, which relied almost entirely on the results of the field tests, would not support the issuance of the warrant if the field test was itself unlawful. " `It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention.' " <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#413" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 413, n. 3</a></span> (1969) (emphasis in original) (quoting <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 109, n. 1</a></span> (1964)). See <i>Illinois</i> v. <i>Gates,</i> <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213, 238-239</a></span> (1983).</p>
<p>[3]  See also <i>People</i> v. <i>Adler,</i> 50 N. Y. 2d 730, <span class="citation" data-id="5533133"><a href="/opinion/5684320/people-v-adler/" aria-description="Citation for case: People v. Adler">409 N. E. 2d 888</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/1014/">449 U. S. 1014</a></span> (1980); cf. <i>United States</i> v. <i>Andrews,</i> <span class="citation" data-id="9466632"><a href="/opinion/376747/united-states-v-john-allen-andrews/" aria-description="Citation for case: United States v. John Allen Andrews">618 F. 2d 646</a></span> (CA10) (upholding warrantless field test without discussion), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/824/">449 U. S. 824</a></span> (1980).</p>
<p>[4]  See <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983); <i>United States</i> v. <i>Knotts,</i> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/#280" aria-description="Citation for case: United States v. Knotts">460 U. S. 276, 280-281</a></span> (1983); <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-741</a></span> (1979); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968).</p>
<p>[5]  See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983); <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#716" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 716</a></span> (BRENNAN, J., concurring in result); <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (STEVENS, J., concurring in judgment); see also <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13-14, n. 8</a></span> (1977); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#76" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 76</a></span> (1906). While the concept of a "seizure" of property is not much discussed in our cases, this definition follows from our oft-repeated definition of the "seizure" of a person within the meaning of the Fourth Amendment  meaningful interference, however brief, with an individual's freedom of movement. See <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#696" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 696</a></span> (1981); <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span>, n. (1980) <i>(per curiam); </i><i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#551" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 551-554</a></span> (1980) (opinion of Stewart, J.); <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50</a></span> (1979); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 16, 19, n. 16</a></span>.</p>
<p>[6]  See <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#656" aria-description="Citation for case: Walter v. United States">447 U. S., at 656</a></span> (opinion of STEVENS, J.); <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#660" aria-description="Citation for case: Walter v. United States"><i>id.,</i> at 660-661</a></span> (WHITE, J., concurring in part and concurring in judgment); <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#455" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 455-456, n. 31</a></span> (1976); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span> (1971); <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span> (1921).</p>
<p>[7]  <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 10</a></span> (1977); <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#251" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249, 251</a></span> (1970); <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878); see also <i>Walter,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#654" aria-description="Citation for case: Walter v. United States">447 U. S., at 654-655</a></span> (opinion of STEVENS, J.).</p>
<p>[8]  See, <i>e. g., </i><i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S., at 701</a></span>; <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 809-812</a></span> (1982); <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 426</a></span> (1981) (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#762" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 762</a></span> (1979); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>, and n. 8; <i>United States</i> v. <i>Van <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">Leeuwen, supra</a></span></i><i>.</i> There is, of course, a well-recognized exception for customs searches; but that exception is not involved in this case.</p>
<p>[9]  See <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#567" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 567, n. 11</a></span> (1971); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 484</a></span> (1963); <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960); <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span> (1959); <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#312" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 312</a></span> (1958); <i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span> (1948); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#29" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 29</a></span> (1927).</p>
<p>[10]  A post-trial affidavit indicates that an agent of Federal Express may have opened the package because he was suspicious about its contents, and not because of damage from a forklift. However, the lower courts found no governmental involvement in the private search, a finding not challenged by respondents. The affidavit thus is of no relevance to the issue we decide.</p>
<p>[11]  See also <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/#658" aria-description="Citation for case: Walter v. United States">447 U. S., at 658-659</a></span> (footnotes omitted) ("The fact that the cartons were unexpectedly opened by a third party before the shipment was delivered to its intended consignee does not alter the consignor's legitimate expectation of privacy. The private search merely frustrated that expectation in part. It did not simply strip the remaining unfrustrated portion of that expectation of all Fourth Amendment protection").</p>
<p>[12]  In <i><span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">Walter</a></span>,</i> a majority of the Court found a violation of the Fourth Amendment. For present purposes, the disagreement between the majority and the dissenters in that case with respect to the comparison between the private search and the official search is less significant than the agreement on the standard to be applied in evaluating the relationship between the two searches.</p>
<p>[13]  See <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#743" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 743-744</a></span> (1979); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#749" aria-description="Citation for case: United States v. White">401 U. S. 745, 749-753</a></span> (1971) (plurality opinion); <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/#326" aria-description="Citation for case: Osborn v. United States">385 U. S. 323, 326-331</a></span> (1966); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#300" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 300-303</a></span> (1966); <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> (1966); <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#437" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 437-439</a></span> (1963); <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#753" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 753-754</a></span> (1952). See also <i>United States</i> v. <i>Henry,</i> <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#272" aria-description="Citation for case: United States v. Henry">447 U. S. 264, 272</a></span> (1980); <i>United States</i> v. <i>Caceres,</i> <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#744" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 744, 750-751</a></span> (1979).</p>
<p>[14]  See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967); <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961).</p>
<p>[15]  Daniel Stegemoller, the Federal Express office manager, testified at the suppression hearing that the white substance was not visible without reentering the package at the time the first agent arrived. App. 42-43, 58. As JUSTICE WHITE points out, the Magistrate found that the "tube was in plain view in the box and the bags with the white powder were visible from the end of the tube." App. to Pet. for Cert. 18a. The bags were, however, only visible if one picked up the tube and peered inside through a small aperture; even then, what was visible was only the translucent bag that contained the white powder. The powder itself was barely visible, and surely was not so plainly in view that the agents did "no more than fail to avert their eyes," <i>post,</i> at 130. In any event, respondents filed objections to the Magistrate's report with the District Court. The District Court declined to resolve respondents' objections, ruling that fact immaterial and assuming for purposes of its decision "that the newspaper in the box covered the gray tube and that neither the gray tube nor the contraband could be seen when the box was turned over to the . . . DEA agents." App. to Pet. for Cert. 12a-13a. At trial, the federal agent first on the scene testified that the powder was not visible until after he pulled the plastic bags out of the tube. App. 71-72. Respondents continue to argue this case on the assumption that the Magistrate's report is incorrect. Brief for Respondents 2-3. As our discussion will make clear, we agree with the District Court that it does not matter whether the loose pieces of newspaper covered the tube at the time the agent first saw the box.</p>
<p>[16]  See <i>United States</i> v. <i>Caceres,</i> <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#750" aria-description="Citation for case: United States v. Caceres">440 U. S., at 750-751</a></span>; <i>United States</i> v. <i>White,</i> 401 U. S., at 749-753 (plurality opinion); <i>Osborn</i> v. <i>United States,</i> 385 U. S., at 326-331; <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#753" aria-description="Citation for case: On Lee v. United States">343 U. S., at 753-754</a></span>. For example, in <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963), the Court wrote: "Stripped to its essentials, petitioner's argument amounts to saying that he has a constitutional right to rely on possible flaws in the agent's memory, or to challenge the agent's credibility without being beset by corroborating evidence . . . . For no other argument can justify excluding an accurate version of a conversation that the agent could testify to from memory. We think the risk that petitioner took in offering a bribe to Davis fairly included the risk that the offer would be accurately reproduced in court . . . ." <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States"><i>Id.,</i> at 439</a></span> (footnote omitted).</p>
<p>[17]  We reject JUSTICE WHITE's suggestion that this case is indistinguishable from one in which the police simply learn from a private party that a container contains contraband, seize it from its owner, and conduct a warrantless search which, as JUSTICE WHITE properly observes, would be unconstitutional. Here, the Federal Express employees who were lawfully in possession of the package invited the agent to examine its contents; the governmental conduct was made possible only because private parties had compromised the integrity of this container. JUSTICE WHITE would have this case turn on the fortuity of whether the Federal Express employees placed the tube back into the box. But in the context of their previous examination of the package, their communication of what they had learned to the agent, and their offer to have the agent inspect it, that act surely could not create any privacy interest with respect to the package that would not otherwise exist. See <i>Illinois</i> v. <i>Andreas,</i> <span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S., at 771-772</a></span>. Thus the precise character of the white powder's visibility to the naked eye is far less significant than the facts that the container could no longer support any expectation of privacy, and that it was virtually certain that it contained nothing but contraband. Contrary to JUSTICE WHITE's suggestion, we do not "sanctio[n] warrantless searches of closed or covered containers or packages whenever probable cause exists as a result of a prior private search." <i>Post,</i> at 129. A container which can support a reasonable expectation of privacy may not be searched, even on probable cause, without a warrant. See <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S., at 809-812</a></span>; <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#426" aria-description="Citation for case: Robbins v. California">453 U. S., at 426-427</a></span> (plurality opinion); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 764-765</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977).</p>
<p>[18]  Both the Magistrate and the District Court found that the agents took custody of the package from Federal Express after they arrived. Although respondents had entrusted possession of the items to Federal Express, the decision by governmental authorities to exert dominion and control over the package for their own purposes clearly constituted a "seizure," though not necessarily an unreasonable one. See <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970). Indeed, this is one thing on which the entire Court appeared to agree in <i>Walter</i> v. <i>United States,</i> <span class="citation" data-id="9428007"><a href="/opinion/110314/walter-v-united-states/" aria-description="Citation for case: Walter v. United States">447 U. S. 649</a></span> (1980).</p>
<p>[19]  See also <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S., at 822-823</a></span>; <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#428" aria-description="Citation for case: Robbins v. California">453 U. S., at 428</a></span> (plurality opinion).</p>
<p>[20]  Respondents concede that the agents had probable cause to believe the package contained contraband. Therefore we need not decide whether the agents could have seized the package based on something less than probable cause. Some seizures can be justified by an articulable suspicion of criminal activity. See <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983).</p>
<p>[21]  See <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S., at 701-702</a></span>; <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#741" aria-description="Citation for case: Texas v. Brown">460 U. S., at 741-742</a></span> (plurality opinion); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#748" aria-description="Citation for case: Texas v. Brown"><i>id.,</i> at 748</a></span> (STEVENS, J., concurring in judgment); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980); <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#354" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 354</a></span> (1977); <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968) <i>(per curiam)</i><i>.</i></p>
<p>[22]  "Obviously, however, a `legitimate' expectation of privacy by definition means more than a subjective expectation of not being discovered. A burglar plying his trade in a summer cabin during the off season may have a thoroughly justified subjective expectation of privacy, but it is not one which the law recognizes as `legitimate.' His presence, in the words of <i>Jones</i> [v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960)], is `wrongful'; his expectation [of privacy] is not `one that society is prepared to recognize as "reasonable." ' <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring). And it would, of course, be merely tautological to fall back on the notion that those expectations of privacy which are legitimate depend primarily on cases deciding exclusionary-rule issues in criminal cases. Legitimation of expectations of privacy by law must have a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society." <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143-144, n. 12</a></span> (1978). See also <i>United States</i> v. <i>Knotts,</i> <span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983) (use of a beeper to track car's movements infringed no reasonable expectation of privacy); <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979) (use of a pen register to record phone numbers dialed infringed no reasonable expectation of privacy).</p>
<p>[23]  See Loewy, The Fourth Amendment as a Device for Protecting the Innocent, <span class="citation no-link">81 Mich. L. Rev. 1229</span> (1983). Our discussion, of course, is confined to possession of contraband. It is not necessarily the case that the purely "private" possession of an article that cannot be distributed in commerce is itself illegitimate. See <i>Stanley</i> v. <i>Georgia,</i> <span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557</a></span> (1969).</p>
<p>[24]  Respondents attempt to distinguish <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> arguing that it involved no physical invasion of Place's effects, unlike the conduct at issue here. However, as the quotation makes clear, the <i>reason</i> this did not intrude upon any legitimate privacy interest was that the governmental conduct could reveal nothing about noncontraband items. That rationale is fully applicable here.</p>
<p>[25]  In <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,</i> the Court held that while the initial seizure of luggage for the purpose of subjecting it to a "dog sniff" test was reasonable, the seizure became unreasonable because its length unduly intruded upon constitutionally protected interests. See <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place"><i>id.,</i> at 707-710</a></span>.</p>
<p>[26]  See, <i>e. g., </i><i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1046" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1046-1047</a></span> (1983); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <i>United States</i> v. <i>BrignoniPonce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878</a></span>; <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20-21</a></span>; <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967).</p>
<p>[27]  In fact, respondents do not contend that the amount of material tested was large enough to make it possible for them to have detected its loss. The only description in the record of the amount of cocaine seized is that "[i]t was a trace amount." App. 75.</p>
<p>[28]  See <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#296" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 296</a></span> (1973) (warrantless search and seizure limited to scraping suspect's fingernails justified even when full search may not be). Cf. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S., at 703-706</a></span> (approving brief warrantless seizure of luggage for purposes of "sniff test" based on its minimal intrusiveness and reasonable belief that the luggage contained contraband); <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#252" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S., at 252-253</a></span> (detention of package on reasonable suspicion was justified since detention infringed no "significant Fourth Amendment interest"). Of course, where more substantial invasions of constitutionally protected interests are involved, a warrantless search or seizure is unreasonable in the absence of exigent circumstances. See, <i>e. g., </i><i>Steagald</i> v. <i>United States,</i> <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">451 U. S. 204</a></span> (1981); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). We do not suggest, however, that any seizure of a small amount of material is necessarily reasonable. An agent's arbitrary decision to take the "white powder" he finds in a neighbor's sugar bowl, or his medicine cabinet, and subject it to a field test for cocaine, might well work an unreasonable seizure.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. James Daniel Good Real Property.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. James Daniel Good Real Property
type: case
citation: "510 U.S. 43 (1993)"
parallel_cite: "114 S. Ct. 492; 126 L. Ed. 2d 490; 7 Fla. L. Weekly Fed. S 665; 93 Daily Journal DAR 15706; 62 U.S.L.W. 4013"
neutral_cite: "1993 U.S. LEXIS 7941; 93 Cal. Daily Op. Serv. 9143; 1993 WL 505539"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-12-13
docket: No. 92-1180
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
  opinion_url: "https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/"
  cluster_id: 112914
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. James Daniel Good Real Property
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. $8,850 in Currency]]"
tags:
  - case
  - civil-forfeiture
  - due-process
  - real-property
  - notice-and-hearing
  - exigent-circumstances
holding: "Absent exigent circumstances, the Due Process Clause of the Fifth Amendment requires the Government to give the owner notice and a meaningful opportunity to be heard before seizing real property in a civil forfeiture; separately, filing the forfeiture action within the five-year statute of limitations makes it timely, and non-compliance with the customs laws' internal reporting deadlines does not require dismissal."
aliases:
  - United States v. James Daniel Good Real Property
  - United States v. James Daniel Good
  - "United States v. James Daniel Good Real Property (1993)"
---

# United States v. James Daniel Good Real Property

*510 U.S. 43 (1993)* (No. 92-1180) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112914 → combined opinion 112914 (Kennedy, J.; 510 U.S. 43, argued Oct. 6, 1993, decided Dec. 13, 1993). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*62` and `*63`, i.e., on page 62). S9 promotes. -->

## Background
In January 1985, Hawaii police searched James Daniel Good's home and found about 89 pounds of marijuana and related contraband; Good later pleaded guilty to a state drug offense and was sentenced. Roughly four and a half years later, in August 1989, the United States filed an *in rem* action to forfeit Good's house and its four-acre parcel under 21 U.S.C. § 881(a)(7). A magistrate found probable cause in an *[[Common Legal Terms#ex-parte|ex parte]]* proceeding, and the Government seized the property without any prior notice to Good or an adversary hearing, redirecting the tenants' rent to the U.S. Marshal. Good challenged the seizure as a denial of due process and argued the action was untimely. The District Court granted summary judgment for the Government; the Ninth Circuit held the no-notice seizure unconstitutional but also held the action untimely for failing certain internal reporting deadlines.

## Issue
Whether, absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], the Due Process Clause permits the Government to seize real property for civil forfeiture without prior notice and a hearing; and whether a forfeiture filed within the [[Common Legal Terms#statute-of-limitations|statute of limitations]] must be dismissed for failing to meet the customs laws' internal timing directives.

## Rule
On the constitutional question, the Court applied the general due-process rule that the Government must afford notice and an opportunity to be heard before depriving a person of property, and found no extraordinary justification for dispensing with it when the property is real estate — which cannot abscond and can be secured by less drastic means (a *lis pendens*, restraining order, or bond). It held: "Unless exigent circumstances are present, the Due Process Clause requires the Government to afford notice and a meaningful opportunity to be heard before seizing real property subject to civil forfeiture." — 510 U.S. at 62. ^pin-62

## Application
Because the Government sought only to preserve the property pending forfeiture — not to seize contraband or protect the public — nothing about a house and land presented the kind of [[Exigent Circumstances and Hot Pursuit|exigency]] that could justify skipping pre-seizure process; less restrictive measures would protect the Government's interests. That Good had already been convicted did not matter, since fair procedures are not confined to the innocent and the issue was the legality of the seizure, not the strength of the Government's case. On the separate timeliness question, the Court held that filing within the five-year limitations period made the action timely: where a statute sets internal reporting deadlines but no consequence for missing them, courts will not invent dismissal as a sanction.

## Conclusion
The Court **affirmed** the Ninth Circuit's due-process ruling and **reversed** its ruling that the action was untimely. Kennedy, J., delivered the opinion of the Court. Rehnquist, C.J. (joined by Scalia, J., and in part by O'Connor, J.), and O'Connor and Thomas, JJ., each filed opinions concurring in part and dissenting in part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *James Daniel Good* is the pre-deprivation-process anchor for civil forfeiture: the Government must ordinarily give notice and a hearing *before* seizing real property, unless it proves genuine [[Exigent Circumstances and Hot Pursuit|exigency]]. Teach it against *[[United States v. $8,850 in Currency]]* (1983), which governs the different question of how long the Government may wait to *file* a forfeiture action after a seizure (the *Barker v. Wingo* factors).

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. James Daniel Good Real Property*, 510 U.S. 43 (1993)](https://www.courtlistener.com/opinion/112914/united-states-v-james-daniel-good-real-property/) — pinpoint: 62 (Kennedy, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*62` and `*63`, i.e., on page 62). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6be38587b02d288b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. James Daniel Good Real Property"}, "payload": {"all": [{"cite": "510 U.S. 43", "page": "43", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "510"}, {"cite": "114 S. Ct. 492", "page": "492", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "114"}, {"cite": "126 L. Ed. 2d 490", "page": "490", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "1993 U.S. LEXIS 7941", "page": "7941", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1993"}, {"cite": "7 Fla. L. Weekly Fed. S 665", "page": "665", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "7"}, {"cite": "93 Daily Journal DAR 15706", "page": "15706", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "93"}, {"cite": "93 Cal. Daily Op. Serv. 9143", "page": "9143", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "93"}, {"cite": "62 U.S.L.W. 4013", "page": "4013", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "62"}, {"cite": "1993 WL 505539", "page": "505539", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1993"}], "display": "510 U.S. 43", "official": {"cite": "510 U.S. 43", "page": "43", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "510"}, "official_selection_present": true, "record_id": "United States v. James Daniel Good Real Property"}}
{"assertion_id": "74e8d17989d67afd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. James Daniel Good Real Property"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. James Daniel Good Real Property", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. James Daniel Good Real Property

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. James Daniel Good Real Property",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. James Daniel Good Real Property",
    "case_name_short": "James Daniel Good ",
    "case_name_full": "UNITED STATES v. JAMES DANIEL GOOD REAL PROPERTY Et Al.",
    "input_case_name": "United States v. James Daniel Good Real Property",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-12-13",
    "year": 1993,
    "docket": "No. 92-1180",
    "cluster_id": 112914,
    "lead_opinion_id": 9432907,
    "sibling_ids": [],
    "absolute_url": "/opinion/112914/united-states-v-james-daniel-good-real-property/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "510 U.S. 43",
      "volume": "510",
      "reporter": "U.S.",
      "page": "43",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "510 U.S. 43",
        "volume": "510",
        "reporter": "U.S.",
        "page": "43",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 492",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 L. Ed. 2d 490",
        "volume": "126",
        "reporter": "L. Ed. 2d",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 7941",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "7941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "7 Fla. L. Weekly Fed. S 665",
        "volume": "7",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "665",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 15706",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "15706",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 9143",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9143",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "62 U.S.L.W. 4013",
        "volume": "62",
        "reporter": "U.S.L.W.",
        "page": "4013",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 505539",
        "volume": "1993",
        "reporter": "WL",
        "page": "505539",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "510 U.S. 43",
    "official_selection": {
      "court_class": "scotus",
      "selected": "510 U.S. 43",
      "reason": "selected_rank_1"
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
    "date_created": "2026-07-06T13:16:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:16:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-james-daniel-good-real-property--112914",
      "to_record_id": "United States v. James Daniel Good Real Property",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. James Daniel Good Real Property

```
<opinion type="majority">
<author id="Afh"><page-number citation-index="1" label="46">*46</page-number>Justice Kennedy</author>
<p id="AYL">delivered the opinion of the Court.</p>
<p id="ASH">The principal question presented is whether, in the absence of exigent circumstances, the Due Process Clause of the Fifth Amendment prohibits the Government in a civil forfeiture case from seizing real property without first affording the owner notice and an opportunity to be heard. We hold that it does.</p>
<p id="AZ2">A second issue in the case concerns the timeliness of the forfeiture action. We hold that filing suit for forfeiture within the statute of limitations suffices to make the action timely, and that the cause should not be dismissed for failure to comply with certain other statutory directives for expeditious prosecution in forfeiture cases.</p>
<p id="A9v">I.</p>
<p id="Ax">On January 31, 1985, Hawaii police officers executed a search warrant at the home of claimant James Daniel Good. The search uncovered about 89 pounds of marijuana, marijuana seeds, vials containing hashish oil, and drug paraphernalia. About six months later, Good pleaded guilty to promoting a harmful drug in the second degree, in violation of Hawaii law. <span class="citation no-link">Haw. Rev. Stat. § 712-1245</span>(l)(b) (1985). He was sentenced to one year in jail and five years’ probation, and fined $1,000. Good was also required to forfeit to the State $3,187 in cash found on the premises.</p>
<p id="Aq7">On August 8, 1989, 4V2 years after the drugs were found, the United States filed an <em>in rem </em>action in the United States District Court for the District of Hawaii, seeking to forfeit Good’s house and the 4-acre parcel on which it was situated. The United States sought forfeiture under <span class="citation no-link">21 U. S. C. § 881</span>(a)(7), on the ground that the property had been used to commit or facilitate the commission of a federal drug offense.<footnotemark>1</footnotemark></p>
<p id="b251-4"><page-number citation-index="1" label="47">*47</page-number>On August 18, 1989, in an <em>ex parte </em>proceeding, a United States Magistrate Judge found that the Government had established probable cause to believe Good’s property was subject to forfeiture under § 881(a)(7). A warrant of arrest <em>in rem </em>was issued, authorizing seizure of the property. The warrant was based on an affidavit recounting the fact of Good’s conviction and the evidence discovered during the January 1985 search of his home by Hawaii police.</p>
<p id="b251-5">The Government seized the property on August 21, 1989, without prior notice to Good or an adversary hearing. At the time of the seizure, Good was renting his home to tenants for $900 per month. The Government permitted the tenants to remain on the premises subject to an occupancy agreement, but directed the payment of future rents to the United States Marshal.</p>
<p id="b251-6">Good filed a claim for the property and an answer to the Government’s complaint. He asserted that the seizure deprived him of his property without due process of law and that the forfeiture action was invalid because it had not been timely commenced under the statute. The District Court granted the Government’s motion for summary judgment and entered an order forfeiting the property.</p>
<p id="b251-7">The Court of Appeals for the Ninth Circuit affirmed in part, reversed in part, and remanded for further proceedings. <span class="citation multiple-matches"><a href="/c/F.%202d/971/1376/">971 F. 2d 1376</a></span> (1992). The court was unanimous in holding that the seizure of Good’s property, without prior notice and a hearing, violated the Due Process Clause.</p>
<p id="b252-3"><page-number citation-index="1" label="48">*48</page-number>In a divided decision, the Court of Appeals further held that the District Court erred in finding the action timely. The Court of Appeals ruled that the 5-year statute of limitations in <span class="citation no-link">19 U. S. C. § 1621</span> is only an “outer limit” for filing a forfeiture action, and that further limits are imposed by <span class="citation no-link">19 U. S. C. §§ 1602-1604</span>. 971 F. 2d, at 1378-1382. Those provisions, the court reasoned, impose a “series of internal notification and reporting requirements,” under which “customs agents must report to customs officers, customs officers must report to the United States attorney, and the Attorney General must ‘immediately’ and ‘forthwith’ bring a forfeiture action if he believes that one is warranted.” <em>Id., </em>at 1379 (citations omitted). The Court of Appeals ruled that failure to comply with these internal reporting rules could require dismissal of the forfeiture action as untimely. The court remanded the case for a determination whether the Government had satisfied its obligation to make prompt reports. <em>Id., </em>at 1382.</p>
<p id="b252-4">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./507/983/">507 U. S. 983</a></span> (1993), to resolve a conflict among the Courts of Appeals on the constitutional question presented. Compare <em>United States </em>v. <em>Premises and Real Property at 4492 South Livonia Road, </em><span class="citation" data-id="8975191"><a href="/opinion/8983256/united-states-v-4492-south-livonia-road/" aria-description="Citation for case: United States v. 4492 South Livonia Road">889 F. 2d 1258</a></span> (CA2 1989), with <em>United States </em>v. <em>A Single Family Residence and Real Property, </em><span class="citation" data-id="478062"><a href="/opinion/478062/united-states-v-a-single-family-residence-and-real-property-located-at-900/" aria-description="Citation for case: United States v. A Single Family Residence and Real...">803 F. 2d 625</a></span> (CA11 1986). We now affirm the due process ruling and reverse the ruling on the timeliness question.</p>
<p id="b252-5">II</p>
<p id="b252-6">The Due Process Clause of the Fifth Amendment guarantees that “[n]o person shall ... be deprived of life, liberty, or property, without due process of law.” Our precedents establish the general rule that individuals must receive notice and an opportunity to be heard before the Government deprives them of property. See <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S. 555, 562, n. 12</a></span> (1983); <em>Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#82" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 82</a></span> (1972); <em>Sniadach </em>v. <em>Family Finance Corp. of Bay View, </em><page-number citation-index="1" label="49">*49</page-number><span class="citation" data-id="9424067"><a href="/opinion/107960/sniadach-v-family-finance-corp-of-bay-view/#342" aria-description="Citation for case: Sniadach v. Family Finance Corp. of Bay View">395 U. S. 337, 342</a></span> (1969) (Harlan, J., concurring); <em>Mullane </em>v. <em>Central Hanover Bank &amp; Trust Co., </em><span class="citation" data-id="9420472"><a href="/opinion/104786/mullane-v-central-hanover-bank-trust-co/#313" aria-description="Citation for case: Mullane v. Central Hanover Bank &amp; Trust Co.">339 U. S. 306, 313</a></span> (1950).</p>
<p id="b253-5">The Government does not, and could not, dispute that the seizure of Good’s home and 4-acre parcel deprived him of property interests protected by the Due Process Clause. By the Government’s own submission, the seizure gave it the right to charge rent, to condition occupancy, and even to evict the occupants. Instead, the Government argues that it afforded Good all the process the Constitution requires. The Government makes two separate points in this regard. First, it contends that compliance with the Fourth Amendment suffices when the Government seizes property for purposes of forfeiture. In the alternative, it argues that the seizure of real property under the drug forfeiture laws justifies an exception to the usual due process requirement of preseizure notice and hearing. We turn to these issues.</p>
<p id="b253-6">A</p>
<p id="b253-7">The Government argues that because civil forfeiture serves a “law enforcement purpos[e],” Brief for United States 13, the Government need comply only with the Fourth Amendment when seizing forfeitable property. We disagree. The Fourth Amendment does place restrictions on seizures conducted for purposes of civil forfeiture, <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#696" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 696</a></span> (1965) (holding that the exclusionary rule applies to civil forfeiture), but it does not follow that the Fourth Amendment is the sole constitutional provision in question when the Government seizes property subject to forfeiture.</p>
<p id="b253-8">We have rejected the view that the applicability of one constitutional amendment pre-empts the guarantees of another. As explained in <em>Soldal </em>v. <em>Cook County, </em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#70" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 70</a></span> (1992):</p>
<blockquote id="b253-9">“Certain wrongs affect more than a single right and, accordingly, can implicate more than one of the Constitution’s commands. Where such multiple violations <page-number citation-index="1" label="50">*50</page-number>are alleged, we are not in the habit of identifying as a preliminary matter the claim’s ‘dominant’ character. Rather, we examine each constitutional provision in turn.”</blockquote>
<p id="b254-4">Here, as in <em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Soldal</a></span>, </em>the seizure of property implicates two “ ‘explicit textual source[s] of constitutional protection,’ ” the Fourth Amendment and the Fifth. <em><span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Ibid.</a></span> </em>The proper question is not which Amendment controls but whether either Amendment is violated.</p>
<p id="b254-5">Nevertheless, the Government asserts that when property is seized for forfeiture, the Fourth Amendment provides the full measure of process due under the Fifth. The Government relies on <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975), and <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), in support of this proposition. That reliance is misplaced. <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>and <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span> </em>concerned not the seizure of property but the arrest or detention of criminal suspects, subjects we have considered to be governed by the provisions of the Fourth Amendment without reference to other constitutional guarantees. In addition, also unlike the seizure presented by this case, the arrest or detention of a suspect occurs as part of the regular criminal process, where other safeguards ordinarily ensure compliance with due process.</p>
<p id="b254-6"><em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>held that the Fourth Amendment, rather than the Due Process Clause, determines the requisite postarrest proceedings when individuals are detained on criminal charges. Exclusive reliance on the Fourth Amendment is appropriate in the arrest context, we explained, because the Amendment was “tailored explicitly for the criminal justice system,” and its “balance between individual and public interests always has been thought to define the ‘process that is due’ for seizures of person or property in criminal cases.” <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 125, n. 27</a></span>. Furthermore, we noted that the protections afforded during an arrest and initial detention are “only the <em>first </em>stage of an elaborate system, unique in jurisprudence, <page-number citation-index="1" label="51">*51</page-number>designed to safeguard the rights of those accused of criminal conduct.” <em>Ibid, </em>(emphasis in original).</p>
<p id="b255-5">So too, in <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span> </em>we held that claims of excessive force in the course of an arrest or investigatory stop should be evaluated under the Fourth Amendment reasonableness standard, not under the “more generalized notion of ‘substantive due process.’” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor">490 U.S., at 395</a></span>. Because the degree of force used to effect a seizure is one determinant of its reasonableness, and because the Fourth Amendment guarantees citizens the right “to be secure in their persons . . . against unreasonable . . . seizures,” we held that a claim of excessive force in the course of such a seizure is “most properly characterized as one invoking the protections of the Fourth Amendment.” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor"><em>Id., </em>at 394</a></span>.</p>
<p id="b255-6">Neither <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span> </em>nor <em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>, </em>however, provides support for the proposition that the Fourth Amendment is the beginning and end of the constitutional inquiry whenever a seizure occurs. That proposition is inconsistent with the approach we took in <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), which examined the constitutionality of <em>ex parte </em>seizures of forfeitable property under general principles of due process, rather than the Fourth Amendment. And it is at odds with our reliance on the Due Process Clause to analyze prejudgment seizure and sequestration of personal property. See, <em>e. g., Fuentes </em>v. <em>Shevin, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <em>Mitchell </em>v. <em>W. T. Grant Co., </em><span class="citation" data-id="9425706"><a href="/opinion/109023/mitchell-v-w-t-grant-co/" aria-description="Citation for case: Mitchell v. W. T. Grant Co.">416 U. S. 600</a></span> (1974).</p>
<p id="b255-7">It is true, of course, that the Fourth Amendment applies to searches and seizures in the civil context and may serve to resolve the legality of these governmental actions without reference to other constitutional provisions. See <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (holding that a warrant based on probable cause is required for administrative search of residences for safety inspections); <em>Skinner </em>v. <em>Railway Labor Executives' Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989) (holding that federal regulations authorizing railroads to conduct blood and urine tests of cer<page-number citation-index="1" label="52">*52</page-number>tain employees, without a warrant and without reasonable suspicion, do not violate the Fourth Amendment prohibition against unreasonable searches and seizures). But the purpose and effect of the Government’s action in the present case go beyond the traditional meaning of search or seizure. Here the Government seized property not to preserve evidence of wrongdoing, but to assert ownership and control over the property itself. Our cases establish that government action of this consequence must comply with the Due Process Clauses of the Fifth and Fourteenth Amendments.</p>
<p id="b256-4">Though the Fourth Amendment places limits on the Government’s power to seize property for purposes of forfeiture, it does not provide the sole measure of constitutional protection that must be afforded property owners in forfeiture proceedings. So even assuming that the Fourth Amendment were satisfied in this case, it remains for us to determine whether the seizure complied with our well-settled jurisprudence under the Due Process Clause.</p>
<p id="b256-5">B</p>
<p id="b256-6">Whether <em>ex parte </em>seizures of forfeitable property satisfy the Due Process Clause is a question we last confronted in <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., supra, </em>which held that the Government could seize a yacht subject to civil forfeiture without affording prior notice or hearing. Central to our analysis in <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>was the fact that a yacht was the “sort [of property] that could be removed to another jurisdiction, destroyed, or concealed, if advance warning of confiscation were given.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#679" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Id., </em>at 679</a></span>. The ease with which an owner could frustrate the Government’s interests in the forfeitable property created a “ ‘special need for very prompt action’ ” that justified the postponement of notice and hearing until after the seizure. <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Id.,</a></span> </em>at 678 (quoting <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin"><em>Fuentes, supra, </em>at 91</a></span>).</p>
<p id="b256-7">We had no occasion in <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>to decide whether the same considerations apply to the forfeiture of real property, <page-number citation-index="1" label="53">*53</page-number>which, by its very nature, can be neither moved nor concealed. In fact, when <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>was decided, both the Puerto Rican statute, P. R. Laws Ann., Tit. 24, §2512 (Supp. 1973), and the federal forfeiture statute upon which it was modeled, <span class="citation no-link">21 U. S. C. § 881</span> (1970 ed.), authorized the forfeiture of personal property only. It was not until 1984, 10 years later, that Congress amended § 881 to authorize the forfeiture of real property. See <span class="citation no-link">21 U. S. C. § 881</span>(a)(7); <span class="citation no-link">Pub. L. 98-473, §306</span>, <span class="citation no-link">98 Stat. 2050</span>.</p>
<p id="b257-5">The right to prior notice and a hearing is central to the Constitution’s command of due process. “The purpose of this requirement is not only to ensure abstract fair play to the individual. Its purpose, more particularly, is to protect his use and possession of property from arbitrary encroachment — to minimize substantively unfair or mistaken deprivations of property . . . .” <em>Fuentes, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#80" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 80-81</a></span>.</p>
<p id="b257-6">We tolerate some exceptions to the general rule requiring predeprivation notice and hearing, but only in “‘extraordinary situations where some valid governmental interest is at stake that justifies postponing the hearing until after the event.’” <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Id.,</a></span> </em>at 82 (quoting <em>Boddie </em>v. <em>Connecticut, </em><span class="citation" data-id="9424471"><a href="/opinion/108281/boddie-v-connecticut/#379" aria-description="Citation for case: Boddie v. Connecticut">401 U. S. 371, 379</a></span> (1971)); <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 562, n. 12</a></span>. Whether the seizure of real property for purposes of civil forfeiture justifies such an exception requires an examination of the competing interests at stake, along with the promptness and adequacy of later proceedings. The three-part inquiry set forth in <em>Mathews </em>v. <em>Eldridge, </em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">424 U. S. 319</a></span> (1976), provides guidance in this regard. The <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span> </em>analysis requires us to consider the private interest affected by the official action; the risk of an erroneous deprivation of that interest through the procedures used, as well as the probable value of additional safeguards; and the Government’s interest, including the administrative burden that additional procedural requirements would impose. <span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/#335" aria-description="Citation for case: Mathews v. Eldridge"><em>Id., </em>at 335</a></span>.</p>
<p id="b257-7">Good’s right to maintain control over his home, and to be free from governmental interference, is a private interest of <page-number citation-index="1" label="54">*54</page-number>historic and continuing importance. Cf. <em>United States </em>v. <em>Karo, </em><span class="citation no-link">468 U. S. 706</span>, 714-716 (1984); <em>Payton </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./446/673/">446 U. S. 673</a></span>, 690 (1980). The seizure deprived Good of valuable rights of ownership, including the right of sale, the right of occupancy, the right to unrestricted use and enjoyment, and the right to receive rents. All that the seizure left him, by the Government’s own submission, was the right to bring a claim for the return of title at some unscheduled future hearing.</p>
<p id="b258-4">In <em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">Fuentes</a></span>, </em>we held that the loss of kitchen appliances and household furniture was significant enough to warrant a predeprivation hearing. <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#70" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 70-71</a></span>. And in <em>Connecticut </em>v. <em>Doehr, </em><span class="citation" data-id="9432319"><a href="/opinion/112615/connecticut-v-doehr/" aria-description="Citation for case: Connecticut v. Doehr">501 U. S. 1</a></span> (1991), we held that a state statute authorizing prejudgment attachment of real estate without prior notice or hearing was unconstitutional, in the absence of extraordinary circumstances, even though the attachment did not interfere with the owner’s use or possession and did not affect, as a general matter, rentals from existing leaseholds.</p>
<p id="b258-5">The seizure of a home produces a far greater deprivation than the loss of furniture, or even attachment. It gives the Government not only the right to prohibit sale, but also the right to evict occupants, to modify the property, to condition occupancy, to receive rents, and to supersede the owner in all rights pertaining to the use, possession, and enjoyment of the property.</p>
<p id="b258-6">The Government makes much of the fact that Good was renting his home to tenants, and contends that the tangible effect of the seizure was limited to taking the $900 a month he was due in rent. But even if this were the only deprivation at issue, it'would not render the loss insignificant or unworthy of due process protection. The rent represents a significant portion of the exploitable economic value of Good’s home. It cannot be classified as <em>de minimis </em>for purposes of procedural due process. In sum, the private <page-number citation-index="1" label="55">*55</page-number>interests at stake in the seizure of real property weigh heavily in the <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span> </em>balance.</p>
<p id="b259-5">The practice of <em>ex parte </em>seizure, moreover, creates an unacceptable risk of error. Although Congress designed the drug forfeiture statute to be a powerful instrument in enforcement of the drug laws, it did not intend to deprive innocent owners of their property. The affirmative defense of innocent ownership is allowed by statute. See <span class="citation no-link">21 U. S. C. § 881</span>(a)(7) (“[N]o property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner”).</p>
<p id="b259-6">The <em>ex parte </em>preseizure proceeding affords little or no protection to the innocent owner. In issuing a warrant of seizure, the magistrate judge need determine only that there is probable cause to believe that the real property was “used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of,” a felony narcotics offense. <em><span class="citation no-link">Ibid.</span> </em>The Government is not required to offer any evidence on the question of innocent ownership or other potential defenses a claimant might have. See, <em>e. g., Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U. S. 602</a></span> (1993) (holding that forfeitures under <span class="citation no-link">21 U. S. C. §§ 881</span>(a)(4) and (a)(7) are subject to the limitations of the Excessive Fines Clause). Nor would that inquiry, in the <em>ex parte </em>stage, suffice to protect the innocent owner’s interests. “[Fjairness cán rarely be obtained by secret, one-sided determination of facts decisive of rights. ... No better instrument has been devised for arriving at truth than to give a person in jeopardy of serious loss notice of the case against him and opportunity to meet it.” <em>Joint Anti-Fascist Refugee Comm. </em>v. <em>McGrath, </em><span class="citation" data-id="9420571"><a href="/opinion/104894/joint-anti-fascist-refugee-committee-v-mcgrath/#170" aria-description="Citation for case: Joint Anti-Fascist Refugee Committee v. McGrath">341 U. S. 123, 170-172</a></span> (1951) (Frankfurter, J., concurring) (footnotes omitted).</p>
<p id="b259-7">The purpose of an adversary hearing is to ensure the requisite neutrality that must inform all governmental decision-making. That protection is of particular importance here, <page-number citation-index="1" label="56">*56</page-number>where the Government has a direct pecuniary interest in the outcome of the proceeding.<footnotemark>2</footnotemark> See <em>Harmelin </em>v. <em>Michigan, </em><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/#979" aria-description="Citation for case: Harmelin v. Michigan">501 U. S. 957, 979, n. 9</a></span> (1991) (opinion of Scalia, J.) (“[I]t makes sense to scrutinize governmental action more closely when the State stands to benefit”). Moreover, the availability of a postseizure hearing may be no recompense for losses caused by erroneous seizure. Given the congested civil dockets in federal courts, a claimant may not receive an adversary hearing until many months after the seizure. And even if the ultimate judicial decision is that the claimant was an innocent owner, or that the Government lacked' probable cause, this determination, coming months after the seizure, “would not cure the temporary deprivation that an earlier hearing might have prevented.” <em>Doehr, </em><span class="citation" data-id="9432319"><a href="/opinion/112615/connecticut-v-doehr/#15" aria-description="Citation for case: Connecticut v. Doehr">501 U. S., at 15</a></span>.</p>
<p id="b260-4">This brings us to the third consideration under <em><span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/" aria-description="Citation for case: Mathews v. Eldridge">Mathews</a></span>, </em>“the Government’s interest, including the function involved and the fiscal and administrative burdens that the additional or substitute procedural requirement would entail.” <span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/#335" aria-description="Citation for case: Mathews v. Eldridge">424 U. S., at 335</a></span>. The governmental interest we consider here is not some general interest in forfeiting property but the specific interest in seizing real property before the forfeiture hearing. The question in the civil forfeiture context is whether <em>ex parte </em>seizure is justified by a pressing need for prompt action. See <em>Fuentes, </em><span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#91" aria-description="Citation for case: Fuentes v. Shevin">407 U. S., at 91</a></span>. We find no pressing need here.</p>
<p id="b261-4"><page-number citation-index="1" label="57">*57</page-number>This is apparent by comparison to <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span>, </em>where the Government’s interest in immediate, seizure of a yacht subject to civil forfeiture justified dispensing with the usual requirement of prior notice and hearing. Two essential considerations informed our ruling in that case: First, immediate seizure was necessary to establish the court’s jurisdiction over the property, 416 U. S., at 679, and second, the yacht might have disappeared had the Government given advance warning of the forfeiture action, <em>ibid. </em>See also <em>United States </em>v. <em>Von Neumann, </em><span class="citation" data-id="9430249"><a href="/opinion/111551/united-states-v-von-neumann/#251" aria-description="Citation for case: United States v. Von Neumann">474 U. S. 242, 251</a></span> (1986) (no preseizure hearing is required when customs officials seize an automobile at the border). Neither of these factors is present when the target of forfeiture is real property.</p>
<p id="b261-5">Because real property cannot abscond, the court’s jurisdiction can be preserved without prior seizure. It is true that seizure of the res has long been considered a prerequisite to the initiation of <em>in rem </em>forfeiture proceedings. See <em>Republic Nat. Bank of Miami </em>v. <em>United States, </em><span class="citation" data-id="9432701"><a href="/opinion/112797/republic-national-bank-of-miami-v-united-states/#84" aria-description="Citation for case: Republic National Bank of Miami v. United States">506 U. S. 80, 84</a></span> (1992); <em>United States </em>v. <em>One Assortment of 89 Firearms, </em><span class="citation" data-id="111103"><a href="/opinion/111103/united-states-v-one-assortment-of-89-firearms/#363" aria-description="Citation for case: United States v. One Assortment of 89 Firearms">465 U. S. 354, 363</a></span> (1984). This rule had its origins in the Court’s early admiralty cases, which involved the forfeiture of vessels and other movable personal property. See <em>Taylor </em>v. <em>Carryl, </em><span class="citation" data-id="9416646"><a href="/opinion/87188/james-l-v-carryl/#599" aria-description="Citation for case: James L. v. Carryl">20 How. 583, 599</a></span> (1858); <em>The Brig Ann, </em><span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/" aria-description="Citation for case: The Brig Ann, McLain, Master">9 Cranch 289</a></span> (1815); <em>Keene </em>v. <em>United States, </em><span class="citation" data-id="84912"><a href="/opinion/84912/keene-v-the-united-states/#310" aria-description="Citation for case: Keene v. The United States">5 Cranch 304, 310</a></span> (1809). Justice Story, writing for the Court in <em>The Brig Ann, </em>explained the justification for the rule as one of fixing and preserving jurisdiction: “[Bjefore judicial cognizance can attach upon a forfeiture <em>in rem, . . . </em>there must be a seizure; for until seizure it is impossible to ascertain what is the competent forum.” <span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/#291" aria-description="Citation for case: The Brig Ann, McLain, Master">9 Cranch, at 291</a></span>. But when the res is real property, rather than personal goods, the appropriate judicial forum may be determined without actual seizure.</p>
<p id="b261-6">As <em>The Brig Ann </em>held, all that is necessary “[i]n order to institute and perfect proceedings <em>in rem, </em>[is] that the thing should be actually or constructively within the reach of the Court.” <em><span class="citation" data-id="85119"><a href="/opinion/85119/the-brig-ann-mclain-master/" aria-description="Citation for case: The Brig Ann, McLain, Master">Ibid.</a></span> </em>And as we noted last Term, “[f]airly read, <page-number citation-index="1" label="58">*58</page-number><em>The Brig Ann </em>simply restates the rule that the court must have actual or constructive control of the res when an <em>in rem </em>forfeiture suit is initiated.” <em>Republic Nat </em>Bank, <em>supra, </em>at 87. In the case of real property, the res may be brought within the reach of the court simply by posting notice on the property and leaving a copy of the process with the occupant. In fact, the rules which govern forfeiture proceedings under § 881 already permit process to be executed on real property without physical seizure:</p>
<blockquote id="b262-4">“If the character or situation of the property is such that the taking of actual possession is impracticable, the marshal or other person executing the process shall affix a copy thereof to the property in a conspicuous place and leave a copy of the complaint and process with the person having possession or the person’s agent.” Rule E(4)(b), Supplemental Rules for Certain Admiralty and Maritime Claims.</blockquote>
<p id="APc">See also <em>United States </em>v. <em>TWP 17 R 4, Certain Real Property in Maine, </em><span class="citation" data-id="587573"><a href="/opinion/587573/united-states-v-twp-17-r-4-certain-real-property-in-maine-united-states/#986" aria-description="Citation for case: United States v. Twp 17 R 4, Certain Real Property in...">970 F. 2d 984, 986</a></span>, and n. 4 (CA1 1992).</p>
<p id="b262-6">Nor is the <em>ex parte </em>seizure of real property necessary to accomplish the statutory purpose of § 881(a)(7). The Government’s legitimate interests at the inception of forfeiture proceedings are to ensure that the property not be sold, destroyed, or used for further illegal activity prior to the forfeiture judgment. These legitimate interests can be secured without seizing the subject property.</p>
<p id="b262-7">Sale of the property can be prevented by filing a notice of <em>lis pendens </em>as authorized by state law when the forfeiture proceedings commence. <span class="citation no-link">28 U. S. C. § 1964</span>; and see <span class="citation no-link">Haw. Rev. Stat. § 684-51</span> (1985) <em>(lis pendens </em>provision). If there is evidence, in a particular case, that an owner is likely to destroy his property when advised of the pending action, the Government may obtain an <em>ex parte </em>restraining order, or other appropriate relief, upon a proper showing in district court. See Fed. Rule Civ. Proc. 65; <em>United States </em>v. <em>Prem</em><page-number citation-index="1" label="59">*59</page-number><em>ises and Real Property at 4492 South Livonia Road, </em><span class="citation" data-id="8975191"><a href="/opinion/8983256/united-states-v-4492-south-livonia-road/#1265" aria-description="Citation for case: United States v. 4492 South Livonia Road">889 F. 2d 1258, 1265</a></span> (CA2 1989). The Government’s policy of leaving occupants in possession of real property under an occupancy agreement pending the final forfeiture ruling demonstrates that there is no serious concern about destruction in the ordinary case. See Brief for United States 13, n. 6 (citing Directive No. 90-10 (Oct. 9, 1990), Executive Office for Asset Forfeiture, Office of Deputy Attorney General). Finally, the Government can forestall further illegal activity with search and arrest warrants obtained in the ordinary course.</p>
<p id="b263-5">In the usual case, the Government thus has various means, short of seizure, to protect its legitimate interests in forfeit-able real property. There is no reason to take the additional step of asserting control over the property without first affording notice and an adversary hearing.</p>
<p id="b263-6">Requiring the Government to postpone seizure until after an adversary hearing creates no significant administrative burden. A claimant is already entitled to an adversary hearing before a final judgment of forfeiture. No extra hearing would be required in the typical case, since the Government can wait until after the forfeiture judgment to seize the property. From an administrative standpoint it makes little difference whether that hearing is held before or after the seizure. And any harm that results from delay is minimal in comparison to the injury occasioned by erroneous seizure.</p>
<p id="b263-7">C</p>
<p id="b263-8">It is true that, in cases decided over a century ago, we permitted the <em>ex parte </em>seizure of real property when the Government was collecting debts or revenue. See, <em>e. g., Springer </em>v. <em>United States, </em><span class="citation" data-id="90272"><a href="/opinion/90272/springer-v-united-states/#593" aria-description="Citation for case: Springer v. United States">102 U. S. 586, 593-594</a></span> (1881); <em>Murray’s Lessee </em>v. <em>Hoboken Land &amp; Improvement Co., </em><span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856). Without revisiting these cases, it suffices to say that their apparent rationale — like that for allowing summary seizures during wartime, see <em>Stoehr </em>v. <em>Wallace, </em><span class="citation" data-id="99736"><a href="/opinion/99736/stoehr-v-wallace/" aria-description="Citation for case: Stoehr v. Wallace">255 <page-number citation-index="1" label="60">*60</page-number>U. S. 239</a></span> (1921); <em>Bowles </em>v. <em>Willingham, </em><span class="citation" data-id="9419466"><a href="/opinion/103952/bowles-v-willingham/" aria-description="Citation for case: Bowles v. Willingham">321 U. S. 503</a></span> (1944), and seizures of contaminated food, see <em>North American Cold Storage Co. </em>v. <em>Chicago, </em><span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (1908) — was one of executive urgency. “The prompt payment of taxes,” we noted, “may be vital to the existence of a government.” <span class="citation" data-id="90272"><a href="/opinion/90272/springer-v-united-states/#594" aria-description="Citation for case: Springer v. United States"><em>Springer, supra, </em>at 594</a></span>. See also <em>G. M. Leasing Corp. </em>v. <em>United States, </em><span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352, n. 18</a></span> (1977) (“The rationale underlying [the revenue] decisions, of course, is that the very existence of government depends upon the prompt collection of the revenues”).</p>
<p id="b264-4">A like rationale justified the <em>ex parte </em>seizure of tax-delinquent distilleries in the late 19th century, see, <em>e. g., United States </em>v. <em>Stowell, </em><span class="citation" data-id="92645"><a href="/opinion/92645/united-states-v-stowell/" aria-description="Citation for case: United States v. Stowell">133 U. S. 1</a></span> (1890); <em>Dobbins's Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395</a></span> (1878), since before passage of the Sixteenth Amendment, the Federal Government relied heavily on liquor, customs, and tobacco taxes to generate operating revenues. In 1902, for example, nearly 75 percent of total federal revenues — $479 million out of a total of $653 million — was raised from taxes on liquor, customs, and tobacco. See U. S. Bureau of Census, Historical Statistics of the United States, Colonial Times to the Present 1122 (1976).</p>
<p id="b264-5">The federal income tax code adopted in the first quarter of this century, however, afforded the taxpayer notice and an opportunity to be heard by the Board of Tax Appeals before the Government could seize property for nonpayment of taxes. See Revenue Act of 1921, <span class="citation no-link">42 Stat. 265</span>-266; Revenue Act of 1924, <span class="citation no-link">43 Stat. 297</span>. In <em>Phillips </em>v. <em>Commissioner, </em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589</a></span> (1931), the Court relied upon the availability, and adequacy, of these preseizure administrative procedures in holding that no judicial hearing was required prior to the seizure of property. <em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">Id.,</a></span> </em>at 597-599 (citing Act of Feb. 26, 1926, ch. 27, § 274(a), <span class="citation no-link">44 Stat. 9</span>, 55; Act of May 29, 1928, ch. 852, §§ 272(a), 601, <span class="citation no-link">45 Stat. 791</span>, 852, 872). These constraints on the Commissioner could be overridden, but only when the Commissioner made a determination that a jeopardy assessment was necessary. <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#598" aria-description="Citation for case: Phillips v. Commissioner">283 U. S., at 598</a></span>. Writing for a unani<page-number citation-index="1" label="61">*61</page-number>mous Court, Justice Brandéis explained that under the tax laws “[f]ormal notice of the tax liability is thus given; the Commissioner is required to answer; and there is a complete hearing <em>de novo </em>.... These provisions amply protect the [taxpayer] against improper administrative action.” <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#598" aria-description="Citation for case: Phillips v. Commissioner"><em>Id., </em>at 598-599</a></span>; see also <em>Commissioner </em>v. <em>Shapiro, </em><span class="citation" data-id="9426305"><a href="/opinion/109396/commissioner-v-shapiro/#631" aria-description="Citation for case: Commissioner v. Shapiro">424 U. S. 614, 631</a></span> (1976) (“[In] the <em>Phillips </em>case . .. the taxpayer’s assets could not have been taken or frozen . . . until he had either had, or waived his right to, a full and final adjudication of his tax liability before the Tax Court (then the Board of Tax Appeals)”).</p>
<p id="b265-5">Similar provisions remain in force today. The current Internal Revenue Code prohibits the Government from levying upon a deficient taxpayer’s property without first affording the taxpayer notice and an opportunity for a hearing, unless exigent circumstances indicate that delay will jeopardize the collection of taxes due. See <span class="citation no-link">26 U. S. C. §§6212</span>, 6213, 6851, 6861.</p>
<p id="b265-6">Just as the urgencies that justified summary seizure of property in the 19th century had dissipated by the time of <em><span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/" aria-description="Citation for case: Phillips v. Commissioner">Phillips</a></span>, </em>neither is there a plausible claim of urgency today to justify the summary seizure of real property under § 881(a)(7). Although the Government relies to some extent on forfeitures as a means of defraying law enforcement expenses, it does not, and we think could not, justify the prehearing seizure of forfeitable real property as necessary for the protection of its revenues.</p>
<p id="b265-7">D</p>
<p id="b265-8">The constitutional limitations we enforce in this case apply to real property in general, not simply to residences. That said, the case before us well illustrates an essential principle: Individual freedom finds tangible expression in property rights. At stake in this and many other forfeiture cases are the security and privacy of the home and those who take shelter within it.</p>
<p id="b266-3"><page-number citation-index="1" label="62">*62</page-number>Finally, the suggestion that this one claimant must lose because his conviction was known at the time of seizure, and because he raises an as applied challenge to the statute, founders on a bedrock proposition: Fair procedures are not confined to the innocent. The question before us is the legality of the seizure, not the strength of the Government’s case.</p>
<p id="b266-4">In sum, based upon the importance of the private interests at risk and the absence of countervailing Government needs, we hold that the seizure of real property under § 881(a)(7) is not one of those extraordinary instances that justify the postponement of notice and hearing. Unless exigent circumstances are present, the Due Process Clause requires the Government to afford notice and a meaningful opportunity to be heard before seizing real property subject to civil forfeiture.<footnotemark>3</footnotemark></p>
<p id="b266-5">To establish exigent circumstances, the Government must show that less restrictive <em>measures </em>— i. <em>e., </em>a <em>lis pendens, </em>restraining order, or bond — would not suffice to protect the Government’s interests in preventing the sale, destruction, or continued unlawful use of the real property. We agree with the Court of Appeals that no showing of exigent circumstances has been made in this case, and we affirm its ruling that the <em>ex parte </em>seizure of Good’s real property violated due process.</p>
<p id="b266-6">Ill</p>
<p id="b266-7">We turn now to the question whether a court must dismiss a forfeiture action that the Government filed within the stat<page-number citation-index="1" label="63">*63</page-number>ute of limitations, but without complying with certain other statutory timing directives.</p>
<p id="b267-5">Title <span class="citation no-link">21 U. S. C. § 881</span>(d) incorporates the “provisions of law relating to the seizure, summary and judicial forfeiture, and condemnation of property for violation of the customs laws.” The customs laws in turn set forth various timing requirements. Title <span class="citation no-link">19 U. S. C. § 1621</span> contains the statute of limitations: “No suit or action to recover any pecuniary penalty or forfeiture of property accruing under the customs laws shall be instituted unless such suit or action is commenced within five years after the time when the alleged offense was discovered.” All agree that the Government filed its action within the statutory period.</p>
<p id="b267-6">The customs laws also contain a series of internal requirements relating to the timing of forfeitures. Title <span class="citation no-link">19 U. S. C. § 1602</span> requires that a customs agent “report immediately” to a customs officer every seizure for violation of the customs laws, and every violation of the customs laws. Section 1603 requires that the customs officer “report promptly” such seizures or violations to the United States attorney. And § 1604 requires the Attorney General “forthwith to cause the proper proceedings to be commenced” if it appears probable that any fine, penalty, or forfeiture has been incurred. The Court of Appeals held, over a dissent, that failure to comply with these internal timing requirements mandates dismissal of the forfeiture action. We disagree.</p>
<p id="b267-7">We have long recognized that “many statutory requisitions intended for the guide of officers in the conduct of business devolved upon them ... do not limit their power or render its exercise in disregard of the requisitions ineffectual.” <em>French </em>v. <em>Edwards, </em><span class="citation" data-id="9416845"><a href="/opinion/88488/french-v-edwards/#511" aria-description="Citation for case: French v. Edwards">13 Wall. 506, 511</a></span> (1872). We have held that if a statute does not specify a consequence for noncompliance with statutory timing provisions, the federal courts will not in the ordinary course impose their own coercive sanction. See <em>United States </em>v. <em>Montalvo-Murillo, </em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#717" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S. 711, 717-721</a></span> (1990); <em>Brock </em>v. <em>Pierce County, </em><span class="citation" data-id="111668"><a href="/opinion/111668/brock-v-pierce-county/#259" aria-description="Citation for case: Brock v. Pierce County">476 U. S. 253, <page-number citation-index="1" label="64">*64</page-number>259-262</a></span> (1986); see also <em>St. Regis Mohawk Tribe </em>v. <em>Brock, </em><span class="citation" data-id="456178"><a href="/opinion/456178/st-regis-mohawk-tribe-new-york-v-william-e-brock-secretary-of-labor/#41" aria-description="Citation for case: St. Regis Mohawk Tribe, New York v. William E. Brock,...">769 F. 2d 37, 41</a></span> (CA2 1985) (Friendly, J.).</p>
<p id="b268-4">In <em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/" aria-description="Citation for case: United States v. Montalvo-Murillo">Montalvo-Murillo</a></span>, </em>for example, we considered the Bail Reform Act of 1984, which requires an “immediate]” hearing upon a pretrial detainee’s “first appearance before the judicial officer.” <span class="citation no-link">18 U. S. C. § 3142</span>(f). Because “[n]either the timing requirements nor any other part of the Act [could] be read to require, or even suggest, that a timing error must result in release of a person who should otherwise be detained,” we held that the federal courts could not release a person pending trial solely because the hearing had not been held “immediately.” <span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#716" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S., at 716-717</a></span>. We stated that “[t]here is no presumption or general rule that for every duty imposed upon the court or the Government and its prosecutors there must exist some corollary punitive sanction for departures or omissions, even if negligent.” <em><span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/" aria-description="Citation for case: United States v. Montalvo-Murillo">Id.,</a></span> </em>at 717 (citing <span class="citation" data-id="9416845"><a href="/opinion/88488/french-v-edwards/#511" aria-description="Citation for case: French v. Edwards"><em>French, supra, </em>at 511</a></span>). To the contrary, we stated that “[w]e dp not agree that we should, or can, invent a remedy to satisfy some perceived need to coerce the courts and the Government into complying with the statutory time limits.” <span class="citation" data-id="9432031"><a href="/opinion/112440/united-states-v-montalvo-murillo/#721" aria-description="Citation for case: United States v. Montalvo-Murillo">495 U. S., at 721</a></span>.</p>
<p id="b268-5">Similarly, in <em>Brock, supra, </em>we considered a statute requiring that the Secretary of Labor begin an investigation within 120 days of receiving information about the misuse of federal funds. The respondent there argued that failure to act within the specified time period divested the Secretary of authority to investigate a claim after the time limit had passed. We rejected that contention, relying on the fact that the statute did not specify a consequence for a failure to comply with the timing provision. <em>Id., </em>at 258-262.</p>
<p id="b268-6">Under our precedents, the failure of Congress to specify a consequence for noncompliance with the timing requirements of <span class="citation no-link">19 U. S. C. §§ 1602-1604</span> implies that Congress intended the responsible officials administering the Act to have discretion to determine what disciplinary measures are appropriate when their subordinates fail to discharge their statu<page-number citation-index="1" label="65">*65</page-number>tory duties. Examination of the structure and history of the internal timing provisions at issue in this case supports the conclusion that the courts should not dismiss a forfeiture action for noncompliance. Because § 1621 contains a statute of limitations — the usual legal protection against stale claims— we doubt Congress intended to require dismissal of a forfeiture action for noncompliance with the internal timing requirements of §§ 1602-1604. Cf. <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#563" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 563, n. 13</a></span>.</p>
<p id="b269-5">Statutes requiring customs officials to proceed with dispatch have existed at least since 1799. See Act of Mar. 2, 1799, § 89, <span class="citation no-link">1 Stat. 695</span>-696. These directives help to ensure that the Government is prompt in obtaining revenue from forfeited property. It would make little sense to interpret directives designed to ensure the expeditious collection of revenues in a way that renders the Government unable, in certain circumstances, to obtain its revenues at all.</p>
<p id="b269-6">We hold that courts may not dismiss a forfeiture action filed within the 5-year statute of limitations for noncompliance with the internal timing requirements of §§ 1602-1604. The Government filed the action in this case within the 5-year statute of limitations, and that sufficed to make it timely. We reverse the contrary holding of the Court of Appeals.</p>
<p id="b269-7">IV</p>
<p id="b269-8">The case is remanded for further proceedings consistent with this opinion.</p>
<p id="b269-9">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="AMq"> Title <span class="citation no-link">21 U. S. C. § 881</span>(a)(7) provides:</p>
<blockquote id="AOj">“(a) . . .</blockquote>
<blockquote id="AgD">“The following shall be subject to forfeiture to the United States and no property right shall exist in them:</blockquote>
<blockquote id="ATo"><page-number citation-index="1" label="47">*47</page-number>“(7) All real property, including any right, title, and interest (including any leasehold interest) in the whole of any lot or tract of land and any appurtenances or improvements, which is used, or intended to be used, in any manner or part, to commit, or to facilitate the commission of, a violation of this subchapter punishable by more than one year’s imprisonment, except that no property shall be forfeited under this paragraph, to the extent of an interest of an owner, by reason of any act or omission established by that owner to have been committed or omitted without the knowledge or consent of that owner.”</blockquote>
</footnote>
<footnote label="2">
<p id="b260-5"> The extent of the Government’s financial stake in drug forfeiture is apparent from a 1990 memo, in which the Attorney General urged United States Attorneys to increase the volume of forfeitures in order to meet the Department of Justice’s annual budget target:</p>
<p id="b260-6">“We must significantly increase production to reach our budget target.</p>
<p id="b260-7">“. . . Failure to achieve the $470 million projection would expose the Department’s forfeiture program to criticism and undermine confidence in our budget projections. Every effort must be made to increase forfeiture income during the remaining three months of [fiscal year] 1990.” Executive Office for United States Attorneys, U. S. Dept, of Justice, 38 United States Attorney’s Bulletin 180 (1990).</p>
</footnote>
<footnote label="3">
<p id="b266-8"> We do not address what sort of procedures are required for preforfeiture seizures of real property in the context of criminal forfeiture. See, <em>e. g., </em><span class="citation no-link">21 U. S. C. § 863</span>; <span class="citation no-link">18 U. S. C. § 1963</span> (1988 ed. and Supp. IV). We note, however, that the federal drug laws now permit seizure before entry of a criminal forfeiture judgment only where the Government persuades a district court that there is probable cause to believe that a protective order “may not be sufficient to assure the availability of the property for forfeiture.” <span class="citation no-link">21 U.S.C. § 863</span>(f).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Janis.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "7703e675fe5d5b25", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Janis"}, "payload": {"all": [{"cite": "428 U.S. 433", "page": "433", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "428"}, {"cite": "96 S. Ct. 3021", "page": "3021", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 1046", "page": "1046", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 162", "page": "162", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "428 U.S. 433", "official": {"cite": "428 U.S. 433", "page": "433", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "428"}, "official_selection_present": true, "record_id": "United States v. Janis"}}
{"assertion_id": "0ca479293ca34f28", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-454", "record_id": "United States v. Janis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-454", "pinpoint_status": "slip-only", "quote": "--- # United States v. Janis *428 U.S. 433 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Los Angeles police, executing a search warrant that later proved defective, seized wagering records and cash from Janis; the state gambling case was dismissed after suppression. The IRS then used the seized records to assess a federal wagering excise tax against Janis and levied on the cash. Janis sued for a refund and the Government counterclaimed for the unpaid tax. He argued that the evidence, having been unconstitutionally seized by the state officers, was inadmissible in the federal civil tax proceeding. ## Issue Whether evidence unconstitutionally seized by state law-enforcement officers (in good-faith reliance on a defective warrant) is inadmissible, under the exclusionary rule, in a federal civil tax proceeding. ## Rule No; the exclusionary rule extends only where its deterrence benefits outweigh its substantial social costs.", "quote_fidelity": "mismatch", "record_id": "United States v. Janis", "star_marker": null}}
{"assertion_id": "b000885633b228c9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-454b", "record_id": "United States v. Janis"}, "payload": {"fragment": "#:~:text=In%20short%2C%20we%20conclude%20that", "page": null, "pin_id": "pin-454b", "pinpoint_status": "star-verified", "quote": "In short, we conclude that exclusion from federal civil proceedings of evidence unlawfully seized by a state criminal enforcement officer has not been shown to have a sufficient likelihood of deterring the conduct of the state police so that it outweighs the societal costs imposed by the exclusion. This Court, therefore, is not justified in so extending the exclusionary rule.", "quote_fidelity": "matched", "record_id": "United States v. Janis", "star_marker": "454"}}
{"assertion_id": "0be1e29849880bfe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Janis"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Janis", "scope_note": "The exclusionary rule does not extend to a federal civil tax proceeding to bar evidence unlawfully seized by state officers; good law.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Johns.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Johns"
type: case
citation: "469 U.S. 478 (1985)"
parallel_cite: "105 S. Ct. 881; 83 L. Ed. 2d 890; 53 U.S.L.W. 4126"
neutral_cite: 1985 U.S. LEXIS 45
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-21
docket: 83-1625
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Johns
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111305/united-states-v-johns/"
  cluster_id: 111305
  opinion_id: 9429826
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Acevedo]]", "[[Chambers v. Maroney]]", "[[United States v. Gastiaburo]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "container-search", "delayed-search", "probable-cause"]
holding: "A warrantless search of packages lawfully removed from a vehicle on PC is not rendered unreasonable merely because officers delayed the…"
lake:
  record_id: United States v. Johns
  status: verified
  projected_at: 2026-07-09
---

# United States v. Johns

*469 U.S. 478 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs officers investigating a smuggling operation watched two pickup trucks rendezvous with small planes at a remote Arizona airstrip; agents detected the odor of marihuana coming from packages wrapped in plastic and paper in the trucks. They arrested the people at the scene, drove the trucks to DEA headquarters, and moved the packages into a DEA warehouse. Without a warrant, agents opened the packages about three days later and found marihuana. The Ninth Circuit suppressed it, holding the automobile exception did not authorize a search three days after the packages were removed.

## Issue
Whether the automobile exception permits a warrantless search of packages that officers had probable cause to search and lawfully removed from vehicles, when the search occurs three days after the packages were removed.

## Rule
Yes. Where officers had probable cause and the authority to search the vehicles and their containers under the [[Carroll v. United States]] / *[[United States v. Ross|Ross]]* automobile-exception line, a later search of the removed packages is not made unreasonable by delay. The Court framed the question as "whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks." — 469 U.S. at 482. ^pin-482

It answered no: "Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the warrantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our precedent involving searches of impounded vehicles." — *Id.* at 487. ^pin-487

A defendant who would invalidate such a delayed search must show prejudice to a protected interest: here "respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/111305/united-states-v-johns/#:~:text=respondents%20have%20not%20even%20alleged%2C) ^pin-487a

## Application
On these facts the three-day delay did not defeat the search. The Customs officers conducted a vehicle search "at least to the extent of entering the trucks and removing the packages," and there was probable cause — the plain odor of marihuana — to believe the packages held contraband. Because the Government could have opened the packages immediately without a warrant, it did not lose that authority by waiting: the respondents did not challenge the seizure of the trucks or packages, never sought their return, and never alleged that the delay harmed any Fourth Amendment interest. The delayed warehouse search was therefore reasonable, by analogy to the Court's impounded-vehicle cases.

## Conclusion
The warrantless search of the packages three days after their removal from the trucks was reasonable under the automobile exception; the Ninth Circuit's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Johns* extends the [[Carroll v. United States]] / *[[United States v. Ross|Ross]]* automobile-exception rule (later unified for containers in [[California v. Acevedo]]) to delayed container searches, and is relied on by lower courts rejecting any "temporal limit" on the exception (e.g., [[United States v. Gastiaburo]]).

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Johns*, 469 U.S. 478 (1985) — https://www.courtlistener.com/opinion/111305/united-states-v-johns/ — pinpoints: 482, 487.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0c1938dc84e98c24", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Johns"}, "payload": {"all": [{"cite": "469 U.S. 478", "page": "478", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "469"}, {"cite": "105 S. Ct. 881", "page": "881", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "83 L. Ed. 2d 890", "page": "890", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "1985 U.S. LEXIS 45", "page": "45", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4126", "page": "4126", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "469 U.S. 478", "official": {"cite": "469 U.S. 478", "page": "478", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "469"}, "official_selection_present": true, "record_id": "United States v. Johns"}}
{"assertion_id": "76393ddf294107f0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-487a", "record_id": "United States v. Johns"}, "payload": {"fragment": "#:~:text=respondents%20have%20not%20even%20alleged%2C", "page": null, "pin_id": "pin-487a", "pinpoint_status": "star-verified", "quote": "respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "United States v. Johns", "star_marker": "487"}}
{"assertion_id": "a796c1ad338609c2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-482", "record_id": "United States v. Johns"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-482", "pinpoint_status": "slip-only", "quote": "--- # United States v. Johns *469 U.S. 478 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs officers investigating a smuggling operation watched two pickup trucks rendezvous with small planes at a remote Arizona airstrip; agents detected the odor of marihuana coming from packages wrapped in plastic and paper in the trucks. They arrested the people at the scene, drove the trucks to DEA headquarters, and moved the packages into a DEA warehouse. Without a warrant, agents opened the packages about three days later and found marihuana. The Ninth Circuit suppressed it, holding the automobile exception did not authorize a search three days after the packages were removed. ## Issue Whether the automobile exception permits a warrantless search of packages that officers had probable cause to search and lawfully removed from vehicles, when the search occurs three days after the packages were removed. ## Rule Yes. Where officers had probable cause and the authority to search the vehicles and their containers under the [[Carroll v. United States]] / *Ross* automobile-exception line, a later search of the removed packages is not made unreasonable by delay. The Court framed the question as", "quote_fidelity": "mismatch", "record_id": "United States v. Johns", "star_marker": null}}
{"assertion_id": "ba3fdad4af5d7dda", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-487", "record_id": "United States v. Johns"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-487", "pinpoint_status": "slip-only", "quote": "Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the warrantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our precedent involving searches of impounded vehicles.", "quote_fidelity": "mismatch", "record_id": "United States v. Johns", "star_marker": null}}
{"assertion_id": "1e20de2cfc71d5c6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Johns"}, "payload": {"as_of_content": "1985-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Johns", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Johns

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Johns",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Johns",
    "case_name_short": "Johns",
    "case_name_full": "UNITED STATES v. JOHNS Et Al.",
    "input_case_name": "United States v. Johns",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-21",
    "year": 1985,
    "docket": "83-1625",
    "cluster_id": 111305,
    "lead_opinion_id": 9429826,
    "sibling_ids": [
      111305,
      9429826,
      9429827
    ],
    "absolute_url": "/opinion/111305/united-states-v-johns/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 478",
      "volume": "469",
      "reporter": "U.S.",
      "page": "478",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 881",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 890",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4126",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4126",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 45",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 478",
        "volume": "469",
        "reporter": "U.S.",
        "page": "478",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 881",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 890",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "890",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 45",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "45",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4126",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4126",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 478",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 478",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-482",
      "page": null,
      "quote": "--- # United States v. Johns *469 U.S. 478 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs officers investigating a smuggling operation watched two pickup trucks rendezvous with small planes at a remote Arizona airstrip; agents detected the odor of marihuana coming from packages wrapped in plastic and paper in the trucks. They arrested the people at the scene, drove the trucks to DEA headquarters, and moved the packages into a DEA warehouse. Without a warrant, agents opened the packages about three days later and found marihuana. The Ninth Circuit suppressed it, holding the automobile exception did not authorize a search three days after the packages were removed. ## Issue Whether the automobile exception permits a warrantless search of packages that officers had probable cause to search and lawfully removed from vehicles, when the search occurs three days after the packages were removed. ## Rule Yes. Where officers had probable cause and the authority to search the vehicles and their containers under the [[Carroll v. United States]] / *Ross* automobile-exception line, a later search of the removed packages is not made unreasonable by delay. The Court framed the question as",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-487",
      "page": null,
      "quote": "Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the warrantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our precedent involving searches of impounded vehicles.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-487a",
      "page": null,
      "quote": "respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment.",
      "star_marker": "487",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 28246,
      "fragment": "#:~:text=respondents%20have%20not%20even%20alleged%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Johns",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 1619349,
          "cite": [
            "303 S.W.3d 863",
            "2009 WL 3821453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Earnest Lynn Ross",
          "cluster_id": 3131028,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monterio Desha Hill v. State",
          "cluster_id": 2855208,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrew Wamsley v. State",
          "cluster_id": 2854445,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Blevins v. State",
          "cluster_id": 1384203,
          "cite": [
            "74 S.W.3d 125",
            "2002 WL 535490"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
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
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Doe",
          "cluster_id": 196225,
          "cite": [
            "61 F.3d 107",
            "1995 U.S. App. LEXIS 20643",
            "1995 WL 452641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
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
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Acevedo",
          "cluster_id": 2175164,
          "cite": [
            "216 Cal. App. 3d 586",
            "265 Cal. Rptr. 23",
            "1989 Cal. App. LEXIS 1266"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lyle Gerald Johns",
          "cluster_id": 533056,
          "cite": [
            "891 F.2d 243",
            "1989 U.S. App. LEXIS 18434",
            "1989 WL 146951"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Anthony Prati",
          "cluster_id": 514000,
          "cite": [
            "861 F.2d 82",
            "27 Fed. R. Serv. 66",
            "1988 U.S. App. LEXIS 16205",
            "1988 WL 121235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane1_negative"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
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
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Guzman",
          "cluster_id": 1785574,
          "cite": [
            "959 S.W.2d 631",
            "1998 Tex. Crim. App. LEXIS 12",
            "1998 WL 28103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Pace, Anthony Besase, Christ Savides, Donald Smith, John Cialoni, and Robert Wilson",
          "cluster_id": 538544,
          "cite": [
            "898 F.2d 1218",
            "1990 U.S. App. LEXIS 3831"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amador Rodriguez Chaidez, A/K/A Rodriguez Amador Chaidez and Amador Rodriguez",
          "cluster_id": 543654,
          "cite": [
            "906 F.2d 377",
            "1990 U.S. App. LEXIS 11006",
            "1990 WL 88172"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stabile",
          "cluster_id": 183984,
          "cite": [
            "633 F.3d 219",
            "2011 U.S. App. LEXIS 1945",
            "2011 WL 294036"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Josey v. State",
          "cluster_id": 1760044,
          "cite": [
            "981 S.W.2d 831",
            "1998 Tex. App. LEXIS 6635",
            "1998 WL 734011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Taketa and Thomas O'Brien",
          "cluster_id": 554097,
          "cite": [
            "923 F.2d 665",
            "91 Daily Journal DAR 307",
            "91 Cal. Daily Op. Serv. 314",
            "1991 U.S. App. LEXIS 86",
            "1991 WL 594"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Serafin Alfonso, Humberto Rayo, Fabian Mora, Primo Antonio Serrano-Tellez",
          "cluster_id": 450644,
          "cite": [
            "759 F.2d 728",
            "18 Fed. R. Serv. 1398",
            "1985 U.S. App. LEXIS 30539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McSween",
          "cluster_id": 7205,
          "cite": [
            "53 F.3d 684",
            "1995 WL 309564"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Ricciardelli",
          "cluster_id": 610895,
          "cite": [
            "998 F.2d 8",
            "1993 U.S. App. LEXIS 14891",
            "1993 WL 210540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony H. Lindsey",
          "cluster_id": 77608,
          "cite": [
            "482 F.3d 1285",
            "2007 WL 894366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burgess",
          "cluster_id": 172511,
          "cite": [
            "576 F.3d 1078",
            "80 Fed. R. Serv. 344",
            "2009 U.S. App. LEXIS 17823",
            "2009 WL 2436674"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cast",
          "cluster_id": 2099235,
          "cite": [
            "556 N.E.2d 69",
            "407 Mass. 891",
            "1990 Mass. LEXIS 315"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Solomon Philip Panitz, United States of America v. Andrew Stewart Baumwald",
          "cluster_id": 544607,
          "cite": [
            "907 F.2d 1267",
            "1990 U.S. App. LEXIS 11808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darren Eugene Henderson",
          "cluster_id": 772238,
          "cite": [
            "241 F.3d 638"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Staula",
          "cluster_id": 196665,
          "cite": [
            "80 F.3d 596",
            "1996 U.S. App. LEXIS 5821",
            "1996 WL 134813"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernesto J. Benevento, Ernest A. Benevento, Earl A. Keller, and Carmine Loiacono",
          "cluster_id": 499444,
          "cite": [
            "836 F.2d 60",
            "1987 U.S. App. LEXIS 16699"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randolph Williams",
          "cluster_id": 490903,
          "cite": [
            "822 F.2d 1174",
            "262 U.S. App. D.C. 112",
            "1987 U.S. App. LEXIS 8870"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Moses",
          "cluster_id": 2039425,
          "cite": [
            "557 N.E.2d 14",
            "408 Mass. 136",
            "1990 Mass. LEXIS 329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Johns:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111305 OR 9429826 OR 9429827) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01ODc3NzkyMDAwMDAmcz0yMTMzNTg1JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111305+OR+9429826+OR+9429827%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(111305 OR 9429826 OR 9429827)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OCZzPTUyNzYwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111305+OR+9429826+OR+9429827%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111305 OR 9429826 OR 9429827)",
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
    "complete_query": "cites:(111305 OR 9429826 OR 9429827)",
    "indexed_citing_opinions": 334,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111305,
        "count": 292,
        "count_source": "search"
      },
      {
        "opinion_id": 9429826,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9429827,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 515,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-johns.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNjg0MTgmcz00ODg2NzEyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111305+OR+9429826+OR+9429827%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111305,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 371884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 398924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111305,
        "cited_id": 418796,
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
    "date_created": "2026-07-06T00:50:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:55:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:51:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Johns

```
<opinion type="majority">
<author id="b621-9">Justice O’Connor</author>
<p id="AU5">delivered the opinion of the Court.</p>
<p id="b621-10">In <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), the Court held that if police officers have probable cause to search a lawfully stopped vehicle, they may conduct a warrantless search of any containers found inside that may conceal the <page-number citation-index="1" label="480">*480</page-number>object of the search. The issue in the present case is whether <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>authorizes a warrantless search of packages several days after they were removed from vehicles that police officers had probable cause to believe contained contraband. Although the Court of Appeals for the Ninth Circuit acknowledged that under <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>the police officers could have searched the packages when they were first discovered in the vehicles, the court concluded that the delay after the initial seizure made the subsequent warrantless search unreasonable within the meaning of the Fourth Amendment. <span class="citation multiple-matches"><a href="/c/F.%202d/707/1093/">707 F. 2d 1093</a></span> (1983). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1250/">467 U. S. 1250</a></span> (1984), and we now reverse.</p>
<p id="b622-5">I</p>
<p id="b622-6">Pursuant to an investigation of a suspected drug smuggling operation, a United States Customs officer went to respondent Duarte’s residence in Tucson, Ariz., where he saw two pickup trucks. The Customs officer observed the trucks drive away, and he contacted other officers who conducted ground and air surveillance of the trucks as they traveled 100 miles to a remote private airstrip near Bowie, Ariz., approximately 50 miles from the Mexican border. Soon after the trucks arrived, a small aircraft landed. Although the Customs officers on the ground were unable to see what transpired, their counterparts in the air informed them that one of the trucks had approached the airplane. After a short time, the aircraft departed. A second small aircraft landed and then departed.</p>
<p id="b622-7">Two Customs officers on the ground came closer and parked their vehicles about 30 yards from the two trucks. One officer approached to investigate and saw an individual at the rear of one of the trucks covering the contents with a blanket. The officer ordered respondents to come out from behind the trucks and to lie on the ground. As he and the other officer walked towards the trucks, they smelled the odor of marihuana. They saw in the back of the trucks <page-number citation-index="1" label="481">*481</page-number>packages wrapped in dark green plastic and sealed with tape. Based on their prior experience, the officers knew that smuggled marihuana is commonly packaged in this manner. Respondents Duarte, Leon, Gomez, Redmond, and Soto were arrested at the scene. The Customs Office surveillance aircraft followed the two small airplanes back to Tucson. Respondents Johns and Hearron, the pilots, were arrested upon landing.</p>
<p id="b623-5">The Customs officers did not search the pickup trucks at the desert airstrip. Instead, after arresting the respondents who were at the scene, the Customs officers took the trucks back to Drug Enforcement Administration (DEA) headquarters in Tucson. The packages were removed from the trucks and placed in a DEA warehouse. Without obtaining a search warrant, DEA agents opened some of the packages and took samples that later proved to be marihuana. Although the record leaves unclear precisely when the agents opened the packages, the parties do not dispute the conclusion of the Court of Appeals, 707 F. 2d, at 1095, that the search occurred three days after the packages were seized from the pickup trucks.</p>
<p id="b623-6">A federal grand jury in the District of Arizona indicted respondents for conspiracy to possess and possession of marihuana with intent to distribute, in violation of <span class="citation no-link">21 U. S. C. §§ 841</span>(a)(1) and 846. Before trial, the District Court granted respondents’ motion to suppress the marihuana, and the Government appealed pursuant to <span class="citation no-link">18 U. S. C. § 3731</span>. The Court of Appeals rejected the Government’s contentions that the plain odor of marihuana emanating from the packages made a warrant unnecessary and that respondents Johns and Hearron lacked standing to challenge the search of the packages. 707 F. 2d, at 1095-1096, 1099-1100. Neither of these issues is before this Court. Finally, the Court of Appeals held that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not authorize the warrantless search of the packages three days after they were removed from the pickup trucks. 707 F. 2d, at 1097-1099. Because we disagree with this conclusion, we reverse.</p>
<p id="b624-4"><page-number citation-index="1" label="482">*482</page-number>II</p>
<p id="b624-5">Respondents argue that we should affirm the suppression of the marihuana on the ground that the Customs officers never had probable cause to conduct a vehicle search, and therefore <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>is inapplicable to this case. Instead, respondents contend that <em>United States </em>v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), establishes that the warrantless search was unlawful. These arguments are not persuasive. The events surrounding the rendezvous of the aircraft and the pickup trucks at the isolated desert airstrip indicated that the vehicles were involved in smuggling activity. The Customs officers on the ground were unable to observe the airplanes after they landed, and consequently did not see the packages loaded into the pickup trucks. After the officers came closer and detected the distinct odor of marihuana, they had probable cause to believe that the vehicles contained contraband. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149, 162</a></span> (1925). Given their experience with drug smuggling cases, the officers no doubt suspected that the scent was emanating from the packages that they observed in the back of the pickup trucks. The officers, however, were unaware of the packages until they approached the trucks, and contraband might well have been hidden elsewhere in the vehicles. We agree with the Court of Appeals, see 707 F. 2d, at 1097, that the Customs officers had probable cause to believe that not only the packages but also the vehicles themselves contained contraband.</p>
<p id="b624-6">Under the circumstances of this case, respondents’ reliance on <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>is misplaced. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>police officers had probable cause to believe that a footlocker contained contraband. As soon as the footlocker was placed in the trunk of an automobile, the officers seized the footlocker and later searched it without obtaining a warrant. The Court in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>refused to hold that probable cause generally supports the warrantless search of luggage. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-13</a></span>. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>however, did not involve the exception <page-number citation-index="1" label="483">*483</page-number>to the warrant requirement recognized in <em>Carroll </em>v. <em>United States, supra, </em>because the police had no probable cause to believe that the automobile, as contrasted to the footlocker, contained contraband. See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-12</a></span>. This point is underscored by our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>which held that notwithstanding <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>police officers may conduct a warrantless search of containers discovered in the course of a lawful vehicle search. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#810" aria-description="Citation for case: United States v. Ross">456 U. S., at 810-814</a></span>. Given our conclusion that the Customs officers had probable cause to believe that the pickup trucks contained contraband, <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>is simply inapposite. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>.</p>
<p id="b625-5">Respondents further contend that the record fails to show that a vehicle search ever in fact occurred. This argument is meritless. It is true that the trucks were not searched at the scene, and the record leaves unclear whether the Customs officers thoroughly searched the trucks after they were taken to DEA headquarters. The record does show, however, that the packages were unloaded from the trucks. Thus, the Customs officers conducted a vehicle search at least to the extent of entering the trucks and removing the packages. The possibility that the officers did not search the vehicles more extensively does not affect our conclusion that the packages were removed pursuant to a vehicle search. The issue presented by this case is whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks.</p>
<p id="b625-6">Ill</p>
<p id="b625-7">Our analysis of the central issue in this case begins with our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>. </em>There the Court observed that the exception to the warrant requirement recognized by <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>allows a search of the same scope as could be authorized by a magistrate. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823, 825</a></span>. “A warrant to search a vehicle would support a search of every part of the vehicle that might contain the object of the search.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><em>Id., </em>at 821</a></span>. Although probable cause may not generally justify a war-<page-number citation-index="1" label="484">*484</page-number>rantless search of a container, the Court noted that the protection afforded by the Fourth Amendment varies in different settings. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">Id., at 823</a></span>. “[A]n individual’s expectation of privacy in a vehicle and its contents may not survive if probable cause is given to believe that the vehicle is transporting contraband.” <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span> </em>Cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367-368</a></span> (1976) (discussing lesser expectation of privacy in motor vehicles); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality opinion). Consequently, “[i]f probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of every part of the vehicle and its contents that may conceal the object of the search.” <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#825" aria-description="Citation for case: United States v. Ross">456 U. S., at 825</a></span>.</p>
<p id="b626-5"><em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>as the Court of Appeals acknowledged, 707 F. 2d, at 1098, establishes that the Customs officers could have lawfully searched the packages when they were first discovered inside the trucks at the desert airstrip. Moreover, our previous decisions indicate that the officers acted permissibly by waiting until they returned to DEA headquarters before they searched the vehicles and removed their contents. See <em>id., </em>at 1099. There is no requirement that the warrantless search of a vehicle occur contemporaneously with its lawful seizure. <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S. 67, 68</a></span> (1975) <em>(per curiam); Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970). “[T]he justification to conduct such a warrantless search does not vanish once the car has been immobilized.” <em>Michigan </em>v. <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U. S. 259, 261</a></span> (1982) <em>(per curiam). </em>A vehicle lawfully in police custody may be searched on the basis of probable cause to believe that it contains contraband, and there is no requirement of exigent circumstances to justify such a warrantless search. <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas"><em>Id., </em>at 261-262</a></span>; see also <em>Florida </em>v. <em>Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984) <em>(per curiam).</em></p>
<p id="b626-6">The Court of Appeals concluded that <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>allows warrant-less searches of containers only if the search occurs “immediately” as part of the vehicle inspection or “soon thereafter.” See 707 F. 2d, at 1099. Neither <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>nor our other vehicle search cases suggest any such limitation. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>involved the <page-number citation-index="1" label="485">*485</page-number>warrantless search of two different containers. After making a roadside arrest of the driver of an automobile, police officers opened the trunk and discovered a paper bag that contained what appeared to be narcotics. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#801" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 801</a></span>. The officers took the car to police headquarters and after a more thorough search discovered a leather pouch containing currency. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#801" aria-description="Citation for case: United States v. Ross">456 U. S., at 801</a></span>. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not distinguish between the search of the paper bag that occurred at the scene of arrest and the later search of the leather pouch. Because the police had probable cause to search the entire vehicle, the Court concluded that the police were entitled to open the containers discovered inside without first obtaining a warrant. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross"><em>id., </em>at 817</a></span>. <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>did not suggest that this conclusion was affected by the fact that the leather pouch was not searched until after the police had impounded the vehicle or by the existence of exigent circumstances that might have made it impractical to secure a warrant for the search of the container. Instead, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>indicated that the legality of the search was determined by reference to the exception to the warrant requirement recognized by <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</em></p>
<p id="b627-5"><em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>as the Court of Appeals noted, did observe in a footnote that if police may immediately search a vehicle on the street without a warrant, “a search soon thereafter at the police station is permitted if the vehicle is impounded.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#807" aria-description="Citation for case: United States v. Ross">456 U. S., at 807, n. 9</a></span>. When read in context, these remarks plainly do not suggest that searches of containers discovered in the course of a vehicle search are subject to temporal restrictions not applicable to the vehicle search itself. Moreover, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>expressly refused to limit the application of the <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>exception by requiring police officers to secure a warrant before they searched containers found inside a lawfully stopped vehicle. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross">456 U. S., at 821, n. 28</a></span>. “The scope of a warrantless search of an automobile ... is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object of the search and the places in which there is probable cause to believe that it may <page-number citation-index="1" label="486">*486</page-number>be found.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross"><em>Id., </em>at 824</a></span>. Consequently, the fact that a container is involved does not in itself either expand or contract the well-established exception to the warrant requirement recognized in <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>. </em>See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>.</p>
<p id="b628-5">The approach of the Court of Appeals not only lacks support in our decision in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>, </em>but it also fails to further the privacy interests protected by the Fourth Amendment. Whether respondents ever had a privacy interest in the packages reeking of marihuana is debatable. We have previously observed that certain containers may not support a reasonable expectation of privacy because their contents can be inferred from their outward appearance, <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span> (1979), and based on this rationale the Fourth Circuit has held that “plain odor” may justify a warrantless search of a container. See <em>United States </em>v. <em>Haley, </em><span class="citation" data-id="9468815"><a href="/opinion/398924/united-states-v-michael-ray-haley-william-harry-riehl/#203" aria-description="Citation for case: United States v. Michael Ray Haley William Harry Riehl">669 F. 2d 201, 203-204</a></span>, and n. 3, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./457/1117/">457 U. S. 1117</a></span> (1982). The Ninth Circuit, however, rejected this approach, 707 F. 2d, at 1096, and the Government has not pursued this issue on appeal. We need not determine whether respondents possessed a legitimate expectation of privacy in the packages. Because the Customs officers had probable cause to believe that the pickup trucks contained contraband, any expectation of privacy in the vehicles or their contents was subject to the authority of the officers to conduct a warrantless search. See <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823</a></span>.</p>
<p id="b628-6">The warrantless search of the packages was not unreasonable merely because the Customs officers returned to Tucson and placed the packages in a DEA warehouse rather than immediately opening them. Cf. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#119" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 119-120</a></span> (1984) (no privacy interest in package that was in possession of and had been examined by private party); <em>Michigan </em>v. <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas"><em>Thomas, supra, </em>at 261</a></span>. The practical effect of the opposite conclusion would only be to direct police officers to search immediately all containers that they discover in the course of a vehicle search. Cf. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#807" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em><page-number citation-index="1" label="487">*487</page-number>at 807, n. 9</a></span> (noting similar consequence if police could not conduct warrantless search after vehicle is impounded). This result would be of little benefit to the person whose property is searched, and where police officers are entitled to seize the container and continue to have probable cause to believe that it contains contraband, we do not think that delay in the execution of the warrantless search is necessarily unreasonable. Cf. <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#592" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 592-593</a></span> (impoundment and 1-day delay did not make examination of exterior of vehicle unreasonable where it could have been done on the spot); <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#805" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 805-806</a></span> (1974) (warrantless search of suspect’s clothing permissible notwithstanding delay after initial arrest).</p>
<p id="b629-5">We do not suggest that police officers may indefinitely retain possession of a vehicle and its contents before they complete a vehicle search. Cf. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#523" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 523</a></span> (1971) (White, J., dissenting). Nor do we foreclose the possibility that the owner of a vehicle or its contents might attempt to prove that delay in the completion of a vehicle search was unreasonable because it adversely affected a privacy or possessory interest. Cf. <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983). We note that in this case there was probable cause to believe that the trucks contained contraband and there is no plausible argument that the object of the search could not have been concealed in the packages. Respondents do not challenge the legitimacy of the seizure of the trucks or the packages, and they never sought return of the property. Thus, respondents have not even alleged, much less proved, that the delay in the search of packages adversely affected legitimate interests protected by the Fourth Amendment. Inasmuch as the Government was entitled to seize the packages and could have searched them immediately without a warrant, we conclude that the war-rantless search three days after the packages were placed in the DEA warehouse was reasonable and consistent with our <page-number citation-index="1" label="488">*488</page-number>precedent involving searches of impounded vehicles. See <em>Florida </em>v. <em>Meyers, </em><span class="citation" data-id="9429577"><a href="/opinion/111157/florida-v-meyers/" aria-description="Citation for case: Florida v. Meyers">466 U. S. 380</a></span> (1984); <em>Michigan </em>v. <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">458 U. S. 259</a></span> (1982); <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967) (upholding warrantless search that took place seven days after seizure of automobile pending forfeiture proceedings).</p>
<p id="b630-5">Accordingly, the decision of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b630-6">
<em>It is so ordered.</em>
</p>
</opinion>
```

---
