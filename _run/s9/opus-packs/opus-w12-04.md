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

## GROUP: _overhaul2/lake/cases/Stoner v. California.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Stoner v. California"
type: case
citation: "376 U.S. 483 (1964)"
parallel_cite: "84 S. Ct. 889; 11 L. Ed. 2d 856"
neutral_cite: 1964 U.S. LEXIS 1579
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-05-18
docket: 209
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-03-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stoner v. California
  varies_by_point: false
  scope_note: "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106777/stoner-v-california/"
  cluster_id: 106777
  opinion_id: 106777
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Progeny (third-party consent / apparent authority)"
related: ["[[Chapman v. United States (1961)]]", "[[Illinois v. Rodriguez]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "third-party-consent", "apparent-authority", "hotel"]
holding: "A hotel desk clerk cannot give valid third-party consent to a police search of a current guest's room; a guest retains Fourth Amendment protection that only the guest may waive, and unrealistic notions of 'apparent authority' do not validate the search."
lake:
  record_id: Stoner v. California
  status: verified
  projected_at: 2026-07-06
---

# Stoner v. California

*376 U.S. 483 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating an armed robbery, police traced the petitioner to the Mayfair Hotel. Without a warrant, they asked the night clerk for Stoner's room and, on the clerk's statement that Stoner was out and his offer of "permission," had the clerk unlock Room 404 and let them in ("Be my guest"). Officers searched the room and seized eyeglasses, a jacket, and a pistol used at trial to convict Stoner of robbery.

## Issue
Whether a hotel desk clerk's consent can authorize a warrantless police search of a guest's rented room consistent with the Fourth Amendment.

## Rule
No. A hotel guest enjoys full Fourth Amendment protection in the room. "No less than a tenant of a house, or the occupant of a room in a boarding house, … a guest in a hotel room is entitled to constitutional protection against unreasonable searches and seizures. That protection would disappear if it were left to depend upon the unfettered discretion of an employee of the hotel." — 376 U.S. at 490. ^pin-490

That protection is the guest's alone to waive, and cannot be conjured from agency law: "the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of 'apparent authority.'" — *Id.* at 488. ^pin-488

The right "only the petitioner could waive by word or deed, either directly or through an agent," and there was "nothing in the record to indicate that the police had any basis whatsoever to believe that the night clerk had been authorized by the petitioner" to permit a search. — *Id.* at 489. ^pin-489

## Application
The clerk "clearly and unambiguously consented," but the consent was legally irrelevant: the constitutional right was Stoner's, not the clerk's or the hotel's. A guest impliedly permits maids or repairmen to enter for their duties, but not police to conduct a criminal search; and the police had no basis to think the clerk was the guest's authorized agent. The warrantless search therefore violated the Fourth Amendment.

## Conclusion
The hotel clerk could not consent to the search of Stoner's room; the search was unlawful and the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The later apparent-authority rule of [[Illinois v. Rodriguez]] (1990) validates a search where officers reasonably (if mistakenly) believe the consenter has authority — but a hotel clerk has neither actual nor reasonably-[[Consent Searches|apparent authority]] over a current guest's room, so *Stoner* remains good law and is taught alongside [[Chapman v. United States (1961)]] (landlord) as the core third-party-consent limit.

## Appears on
- [[Consent Searches]] — *Progeny ([[Consent Searches|third-party consent]] / [[Consent Searches|apparent authority]])*

## Sources
- *Stoner v. California*, 376 U.S. 483 (1964) — https://www.courtlistener.com/opinion/106777/stoner-v-california/ — pinpoints: 488, 489, 490.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0fd854acd6bd9c0d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Stoner v. California"}, "payload": {"all": [{"cite": "376 U.S. 483", "page": "483", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "376"}, {"cite": "84 S. Ct. 889", "page": "889", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "11 L. Ed. 2d 856", "page": "856", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "11"}, {"cite": "1964 U.S. LEXIS 1579", "page": "1579", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "376 U.S. 483", "official": {"cite": "376 U.S. 483", "page": "483", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "376"}, "official_selection_present": true, "record_id": "Stoner v. California"}}
{"assertion_id": "7653d1cedde46ad1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-489", "record_id": "Stoner v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-489", "pinpoint_status": "slip-only", "quote": "only the petitioner could waive by word or deed, either directly or through an agent,", "quote_fidelity": "mismatch", "record_id": "Stoner v. California", "star_marker": null}}
{"assertion_id": "8be466d66eff8ca4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-490", "record_id": "Stoner v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-490", "pinpoint_status": "slip-only", "quote": "). Officers searched the room and seized eyeglasses, a jacket, and a pistol used at trial to convict Stoner of robbery. ## Issue Whether a hotel desk clerk's consent can authorize a warrantless police search of a guest's rented room consistent with the Fourth Amendment. ## Rule No. A hotel guest enjoys full Fourth Amendment protection in the room.", "quote_fidelity": "mismatch", "record_id": "Stoner v. California", "star_marker": null}}
{"assertion_id": "df89b1bc64fe04d7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-488", "record_id": "Stoner v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-488", "pinpoint_status": "slip-only", "quote": "the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of 'apparent authority.'", "quote_fidelity": "mismatch", "record_id": "Stoner v. California", "star_marker": null}}
{"assertion_id": "56fd72bd97861b58", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Stoner v. California"}, "payload": {"as_of_content": "1964-03-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Stoner v. California", "scope_note": "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law.", "varies_by_point": false}}
```

### lake record — Stoner v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stoner v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stoner v. California",
    "case_name_short": "Stoner",
    "case_name_full": "Stoner v. California",
    "input_case_name": "Stoner v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-05-18",
    "year": 1964,
    "docket": "209",
    "cluster_id": 106777,
    "lead_opinion_id": 106777,
    "sibling_ids": [
      106777,
      9422755,
      9422756
    ],
    "absolute_url": "/opinion/106777/stoner-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "376 U.S. 483",
      "volume": "376",
      "reporter": "U.S.",
      "page": "483",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 889",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 856",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1579",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "376 U.S. 483",
        "volume": "376",
        "reporter": "U.S.",
        "page": "483",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 889",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 856",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "856",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1579",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "376 U.S. 483",
    "official_selection": {
      "court_class": "scotus",
      "selected": "376 U.S. 483",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-490",
      "page": null,
      "quote": "). Officers searched the room and seized eyeglasses, a jacket, and a pistol used at trial to convict Stoner of robbery. ## Issue Whether a hotel desk clerk's consent can authorize a warrantless police search of a guest's rented room consistent with the Fourth Amendment. ## Rule No. A hotel guest enjoys full Fourth Amendment protection in the room.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-488",
      "page": null,
      "quote": "the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of 'apparent authority.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-489",
      "page": null,
      "quote": "only the petitioner could waive by word or deed, either directly or through an agent,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-03-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Stoner v. California",
    "varies_by_point": false,
    "scope_note": "Good law. Later apparent-authority doctrine (Illinois v. Rodriguez) permits searches on an officer's reasonable belief in a consenter's authority, but a hotel clerk still lacks authority to consent to a current guest's room; Stoner remains good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gatto",
          "cluster_id": 10133498,
          "cite": [
            "304 Or. App. 210",
            "466 P.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Owens",
          "cluster_id": 4425178,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2820149,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
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
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareem Jamal Currence",
          "cluster_id": 794165,
          "cite": [
            "446 F.3d 554",
            "2006 U.S. App. LEXIS 11090",
            "2006 WL 1172337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 3975410,
          "cite": [
            "164 Ohio App. 3d 558",
            "2005 Ohio 6380",
            "843 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Opinion Piedad Barajas-Avaslos",
          "cluster_id": 785295,
          "cite": [
            "359 F.3d 1204",
            "2004 U.S. App. LEXIS 4569",
            "2004 D.A.R. 3084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane1_negative"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mancusi v. DeForte",
          "cluster_id": 107745,
          "cite": [
            "20 L. Ed. 2d 1154",
            "88 S. Ct. 2120",
            "392 U.S. 364",
            "1968 U.S. LEXIS 3075",
            "68 L.R.R.M. (BNA) 2449"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxwell v. State",
          "cluster_id": 2105782,
          "cite": [
            "73 S.W.3d 278",
            "2002 Tex. Crim. App. LEXIS 84",
            "2002 WL 562264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Peltier",
          "cluster_id": 109302,
          "cite": [
            "45 L. Ed. 2d 374",
            "95 S. Ct. 2313",
            "422 U.S. 531",
            "1975 U.S. LEXIS 155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stoner v. California:lane2_top_cited"
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
        "journal_ref": "Stoner v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106777 OR 9422755 OR 9422756) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDQ3NjAwMDAwMDAwJnM9MTI5ODU1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106777+OR+9422755+OR+9422756%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(106777 OR 9422755 OR 9422756)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDAmcz0xMTc0OTc0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106777+OR+9422755+OR+9422756%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106777 OR 9422755 OR 9422756)",
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
    "complete_query": "cites:(106777 OR 9422755 OR 9422756)",
    "indexed_citing_opinions": 1038,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106777,
        "count": 963,
        "count_source": "search"
      },
      {
        "opinion_id": 9422755,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9422756,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1576,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stoner-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3MzAzODUmcz02NDY0MzQ2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106777+OR+9422755+OR+9422756%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106777,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106777,
        "cited_id": 106699,
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
    "date_created": "2026-07-05T21:03:18Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:06:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:03:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stoner v. California

```
<div>
<center><b><span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U.S. 483</a></span> (1964)</b></center>
<center><h1>STONER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 209.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1964.</center>
<center>Decided March 23, 1964.</center>
CERTIORARI TO THE DISTRICT COURT OF APPEAL OF CALIFORNIA, SECOND APPELLATE DISTRICT.
<p><i>William H. Dempsey, Jr.,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./375/805/">375 U. S. 805</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Arlo E. Smith,</i> Chief Assistant Attorney General of California, argued the cause for respondent. With him on the brief were <i>Stanley Mosk,</i> Attorney General of California, and <i>Albert W. Harris, Jr.</i> and <i>Michael J. Phelan,</i> Deputy Attorneys General.</p>
<p><i>A. L. Wirin, Fred Okrand</i> and <i>Paul Cooksey</i> filed a brief for the American Civil Liberties Union of Southern California, as <i>amicus curiae,</i> urging reversal.</p>
<p><span class="star-pagination">*484</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner was convicted of armed robbery after a jury trial in the Superior Court of Los Angeles County, California. At the trial several articles which had been found by police officers in a search of the petitioner's hotel room during his absence were admitted into evidence over his objection. A District Court of Appeal of California affirmed the conviction,<sup>[1]</sup> and the Supreme Court of California denied further review.<sup>[2]</sup> We granted certiorari, limiting review "to the question of whether evidence was admitted which had been obtained by an unlawful search and seizure." <span class="citation multiple-matches"><a href="/c/U.%20S./374/826/">374 U. S. 826</a></span>. For the reasons which follow, we conclude that the petitioner's conviction must be set aside.</p>
<p>The essential facts are not in dispute. On the night of October 25, 1960, the Budget Town Food Market in Monrovia, California, was robbed by two men, one of whom was described by eyewitnesses as carrying a gun and wearing horn-rimmed glasses and a grey jacket. Soon after the robbery a checkbook belonging to the petitioner was found in an adjacent parking lot and turned over to the police. Two of the stubs in the checkbook indicated that checks had been drawn to the order of the Mayfair Hotel in Pomona, California. Pursuing this lead, the officers learned from the Police Department of Pomona that the petitioner had a previous criminal record, and they obtained from the Pomona police a photograph of the petitioner. They showed the photograph to the two eyewitnesses to the robbery, who both stated that the picture looked like the man who had carried the gun. On the basis of this information the officers went to the Mayfair Hotel in Pomona at about 10 <span class="star-pagination">*485</span> o'clock on the night of October 27. They had neither search nor arrest warrants. There then transpired the following events, as later recounted by one of the officers:</p>
<blockquote>"We approached the desk, the night clerk, and asked him if there was a party by the name of Joey L. Stoner living at the hotel. He checked his records and stated `Yes, there is.' And we asked him what room he was in. He stated he was in Room 404 but he was out at this time.</blockquote>
<blockquote>"We asked him how he knew that he was out. He stated that the hotel regulations required that the key to the room would be placed in the mail box each time they left the hotel. The key was in the mail box, that he therefore knew he was out of the room.</blockquote>
<blockquote>"We asked him if he would give us permission to enter the room, explaining our reasons for this.</blockquote>
<blockquote>"Q. What reasons did you explain to the clerk?</blockquote>
<blockquote>"A. We explained that we were there to make an arrest of a man who had possibly committed a robbery in the City of Monrovia, and that we were concerned about the fact that he had a weapon. He stated `In this case, I will be more than happy to give you permission and I will take you directly to the room.'</blockquote>
<blockquote>"Q. Is that what the clerk told you?</blockquote>
<blockquote>"A. Yes, sir.</blockquote>
<blockquote>"Q. What else happened?</blockquote>
<blockquote>"A. We left one detective in the lobby, and Detective Oliver, Officer Collins, and myself, along with the night clerk, got on the elevator and proceeded to the fourth floor, and went to Room 404. The night clerk placed a key in the lock, unlocked the door, and says, `Be my guest.' "</blockquote>
<p>The officers entered and made a thorough search of the room and its contents. They found a pair of hornrimmed <span class="star-pagination">*486</span> glasses and a grey jacket in the room, and a .45-caliber automatic pistol with a clip and several cartridges in the bottom of a bureau drawer. The petitioner was arrested two days later in Las Vegas, Nevada. He waived extradition and was returned to California for trial on the charge of armed robbery. The gun, the cartridges and clip, the horn-rimmed glasses, and the grey jacket were all used as evidence against him at his trial.</p>
<p>The search of the petitioner's room by the police officers was conducted without a warrant of any kind, and it therefore "can survive constitutional inhibition only upon a showing that the surrounding facts brought it within one of the exceptions to the rule that a search must rest upon a search warrant. <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>." <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261</a></span>. The District Court of Appeal thought the search was justified as an incident to a lawful arrest.<sup>[3]</sup> But a search can be incident to an arrest only if it is substantially contemporaneous with the arrest and is confined to the immediate vicinity of the arrest. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.<sup>[4]</sup><span class="star-pagination">*487</span> Whatever room for leeway there may be in these concepts,<sup>[5]</sup> it is clear that the search of the petitioner's hotel room in Pomona, California, on October 27 was not incident to his arrest in Las Vegas, Nevada, on October 29. The search was completely unrelated to the arrest, both as to time and as to place. See <i>Preston</i> v. <i>United States,</i> decided this day, <i>ante,</i> p. 364.</p>
<p>In this Court the respondent has recognized that the reasoning of the California District Court of Appeal cannot be reconciled with our decision in <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span>,</i> nor, indeed, with the most recent California decisions.<sup>[6]</sup> Accordingly, the respondent has made no argument that the search can be justified as an incident to the petitioner's arrest. Instead, the argument is made that the search of the hotel room, although conducted without the petitioner's consent, was lawful because it was conducted <span class="star-pagination">*488</span> with the consent of the hotel clerk. We find this argument unpersuasive.</p>
<p>Even if it be assumed that a state law which gave a hotel proprietor blanket authority to authorize the police to search the rooms of the hotel's guests could survive constitutional challenge, there is no intimation in the California cases cited by the respondent that California has any such law.<sup>[7]</sup> Nor is there any substance to the claim that the search was reasonable because the police, relying upon the night clerk's expressions of consent, had a reasonable basis for the belief that the clerk had authority to consent to the search. Our decisions make clear that the rights protected by the Fourth Amendment are not to be eroded by strained applications of the law of agency or by unrealistic doctrines of "apparent authority." As this Court has said,</p>
<blockquote>"it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical.. . . [W]e ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span>.</blockquote>
<p><span class="star-pagination">*489</span> It is important to bear in mind that it was the petitioner's constitutional right which was at stake here, and not the night clerk's nor the hotel's. It was a right, therefore, which only the petitioner could waive by word or deed, either directly or through an agent. It is true that the night clerk clearly and unambiguously consented to the search. But there is nothing in the record to indicate that the police had any basis whatsoever to believe that the night clerk had been authorized by the petitioner to permit the police to search the petitioner's room.</p>
<p>At least twice this Court has explicitly refused to permit an otherwise unlawful police search of a hotel room to rest upon consent of the hotel proprietor. <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. In <i><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">Lustig</a></span></i> the manager of a hotel allowed police to enter and search a room without a warrant in the occupant's absence, and the search was held unconstitutional. In <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span></i> the assistant manager allowed a similar search, and that search was likewise held unconstitutional.</p>
<p>It is true, as was said in <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span>,</i> that when a person engages a hotel room he undoubtedly gives "implied or express permission" to "such persons as maids, janitors or repairmen" to enter his room "in the performance of their duties." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S., at 51</a></span>. But the conduct of the night clerk and the police in the present case was of an entirely different order. In a closely analogous situation the Court has held that a search by police officers of a house occupied by a tenant invaded the tenant's constitutional right, even though the search was authorized by the owner of the house, who presumably had not only apparent but actual authority to enter the house for some purposes, such as to "view waste." <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>. The Court pointed out that the officers' purpose in entering was not to view waste but to search for distilling equipment, and concluded that to uphold such a search without a warrant would leave <span class="star-pagination">*490</span> tenants' homes secure only in the discretion of their landlords.</p>
<p>No less than a tenant of a house, or the occupant of a room in a boarding house, <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>, a guest in a hotel room is entitled to constitutional protection against unreasonable searches and seizures. <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>. That protection would disappear if it were left to depend upon the unfettered discretion of an employee of the hotel. It follows that this search without a warrant was unlawful. Since evidence obtained through the search was admitted at the trial, the judgment must be reversed. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>.<sup>[8]</sup></p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE HARLAN, concurring in part and dissenting in part.</p>
<p>I entirely agree with the Court's opinion, except as to its disposition of the case. I would remand the case to the California District Court of Appeal so that it may consider whether or not admission of the illegally seized evidence was harmless error. <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span>, does not require or justify the course which the Court takes. In <i><span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">Fahy</a></span>,</i> Connecticut at least had had the opportunity to decide the question of harmless error with respect to the illegally seized evidence there involved; <span class="star-pagination">*491</span> here California has had no such opportunity.<sup>[*]</sup> For this Court to decide that question as an original matter is, in my opinion, incompatible with proper federal-state relations.</p>
<p>Accordingly, I would vacate the judgment below and remand the case to the California courts for further appropriate proceedings.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d 108</a></span>, <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/" aria-description="Citation for case: People v. Stoner">22 Cal. Rptr. 718</a></span>.</p>
<p>[2]  <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#116" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d, at 116</a></span>.</p>
<p>[3]  The court reasoned that the officers had probable cause to arrest the petitioner prior to their entry into the hotel room; that they were not obliged to accept as true the night clerk's statement that the petitioner was not in his room; that "it may be reasonably inferred that they entered his room for the purpose of making an arrest," that their observation of the glasses in plain sight reasonably led them to a further search; and that in the circumstances the arrest and the search and seizure were "part of the same transaction." <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#113" aria-description="Citation for case: People v. Stoner">205 Cal. App. 2d 108, 113</a></span>, <span class="citation" data-id="2213895"><a href="/opinion/2213895/people-v-stoner/#722" aria-description="Citation for case: People v. Stoner">22 Cal. Rptr. 718, 722</a></span>.</p>
<p>[4]  "The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things connected with the crime as its fruits or as the means by which it was committed, as well as weapons and other things to effect an escape from custody, is not to be doubted. See <i>Carroll</i> v. <i>United States.</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 158</a></span>; <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>. . . . But the right does not extend to other places." <i>Id.,</i> at 30. See also <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42, n. 13</a></span>; <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#79" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 79-80</a></span>.</p>
<p>[5]  Although some members of this Court have expressed the view that the statement in <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span></i> defining the permissible bounds of a search incident to arrest went too far, see, <i>e. g., </i><i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155, 183, 195</a></span> (dissenting opinions); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 68</a></span> (dissenting opinion), the <i><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">Agnello</a></span></i> holding as to what may <i>not</i> be searcheda house substantially removed geographically from the place of arrest at a time not substantially contemporaneous with the arresthas never been questioned in this Court.</p>
<p>[6]  "[T]he search cannot be justified as incident to the arrest `for it was at a distance from the place thereof and was not contemporaneous therewith.' (Castaneda v. Superior Court, 59 A. C. 456, 459, <span class="citation" data-id="9559447"><a href="/opinion/1198462/castaneda-v-superior-court/#3" aria-description="Citation for case: Castaneda v. Superior Court">30 Cal. Rptr. 1, 3</a></span>, <span class="citation" data-id="9559447"><a href="/opinion/1198462/castaneda-v-superior-court/#643" aria-description="Citation for case: Castaneda v. Superior Court">380 P. 2d 641, 643</a></span>; Tompkins v. Superior Court, 59 A. C. 75, 77, <span class="citation" data-id="9533071"><a href="/opinion/1126066/tompkins-v-superior-court/" aria-description="Citation for case: Tompkins v. Superior Court">27 Cal. Rptr. 889</a></span>, <span class="citation" data-id="9533071"><a href="/opinion/1126066/tompkins-v-superior-court/" aria-description="Citation for case: Tompkins v. Superior Court">378 P. 2d 113</a></span>; People v. Gorg, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/#781" aria-description="Citation for case: People v. Gorg">45 Cal. 2d 776, 781</a></span>, <span class="citation" data-id="1359720"><a href="/opinion/1359720/people-v-gorg/" aria-description="Citation for case: People v. Gorg">291 P. 2d 469</a></span>.)" <i>People</i> v. <i>King,</i> <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#311" aria-description="Citation for case: People v. King">60 Cal. 2d 308, 311</a></span>, <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#826" aria-description="Citation for case: People v. King">32 Cal. Rptr. 825, 826</a></span>, <span class="citation" data-id="9791441"><a href="/opinion/2609262/people-v-king/#155" aria-description="Citation for case: People v. King">384 P. 2d 153, 155</a></span>.</p>
<p>[7]  See <i>Roberts</i> v. <i>Casey,</i> <span class="citation" data-id="1111698"><a href="/opinion/1111698/roberts-v-casey/" aria-description="Citation for case: Roberts v. Casey">36 Cal. App. 2d Supp. 767</a></span>, <span class="citation" data-id="1111698"><a href="/opinion/1111698/roberts-v-casey/" aria-description="Citation for case: Roberts v. Casey">93 P. 2d 654</a></span>; <i>Fox</i> v. <i>Windemere Hotel Apt. Co.,</i> <span class="citation" data-id="3293015"><a href="/opinion/3294337/fox-v-windemere-hotel-apartment-co/" aria-description="Citation for case: Fox v. Windemere Hotel Apartment Co.">30 Cal. App. 162</a></span>, <span class="citation" data-id="3293015"><a href="/opinion/3294337/fox-v-windemere-hotel-apartment-co/" aria-description="Citation for case: Fox v. Windemere Hotel Apartment Co.">157 P. 820</a></span>; <i>People</i> v. <i>Vaughan,</i> <span class="citation" data-id="1209992"><a href="/opinion/1209992/people-v-vaughan/" aria-description="Citation for case: People v. Vaughan">65 Cal. App. 2d Supp. 844</a></span>; <span class="citation" data-id="1209992"><a href="/opinion/1209992/people-v-vaughan/" aria-description="Citation for case: People v. Vaughan">150 P. 2d 964</a></span>. "The mere fact that a person is a hotel manager does not import an authority to permit the police to enter and search the rooms of her guests." <i>People</i> v. <i>Burke,</i> <span class="citation" data-id="2207511"><a href="/opinion/2207511/people-v-burke/#160" aria-description="Citation for case: People v. Burke">208 Cal. App. 2d 149, 160</a></span>, <span class="citation" data-id="2207511"><a href="/opinion/2207511/people-v-burke/#919" aria-description="Citation for case: People v. Burke">24 Cal. Rptr. 912, 919</a></span>.</p>
<p>[8]  The respondent has argued that the case should be remanded to let the California District Court of Appeal decide whether the admission of this evidence was harmless error. But the conviction depended in large part upon the jury's resolution of the question of the credibility of witnesses, and that determination must almost certainly have been influenced by the incriminating nature of the physical evidence illegally seized and erroneously admitted. There is thus at least "a reasonable possibility that the evidence complained of might have contributed to the conviction." <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#86" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85, 86</a></span>.</p>
<p>[*]  The evidence against the accused included a confession of the crime charged. This Court refused to review the claim, contained in the petition for certiorari, that this confession had been involuntarily made. <span class="citation multiple-matches"><a href="/c/U.%20S./374/826/">374 U. S. 826</a></span>, <i>ante,</i> p. 484.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Stovall v. Denno.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Stovall v. Denno"
type: case
citation: "388 U.S. 293 (1967)"
parallel_cite: "87 S. Ct. 1967; 18 L. Ed. 2d 1199"
neutral_cite: 1967 U.S. LEXIS 1087
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: 254
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stovall v. Denno
  varies_by_point: false
  scope_note: "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107488/stovall-v-denno/"
  cluster_id: 107488
  opinion_id: 107488
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Gilbert v. California]]", "[[United States v. Wade]]", "[[Neil v. Biggers]]", "[[Manson v. Brathwaite]]"]
aliases: []
tags: ["case", "eyewitness-identification", "due-process", "suggestive-identification"]
holding: "A confrontation that is unnecessarily suggestive and conducive to irreparable mistaken identification can violate due process;…"
lake:
  record_id: Stovall v. Denno
  status: verified
  projected_at: 2026-07-06
---

# Stovall v. Denno

*388 U.S. 293 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Stovall was brought, handcuffed, to the hospital room of a stabbing victim (Mrs. Behrendt)—who was the only person who could identify her attacker and might not survive—where she identified him in a one-on-one showup. He challenged the identification as unnecessarily suggestive and as a denial of due process, independent of any right-to-counsel claim.

## Issue
Whether an unnecessarily suggestive identification procedure can violate due process, and how that claim is judged.

## Rule
Suggestive identification procedures are tested for due-process fairness under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The claim asks whether "the confrontation conducted in this case was so unnecessarily suggestive and conducive to irreparable mistaken identification that he was denied due process of law. This is a recognized ground of attack upon a conviction independent of any right to counsel claim." — 388 U.S. at 302. ^pin-302

And "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it." — *Id.* ^pin-302a

## Application
Although showing a suspect singly has been widely condemned, the totality here justified it: Mrs. Behrendt was the only person who could identify or exonerate Stovall, no one knew how long she would live, and she could not come to a station-house lineup. On those facts the immediate hospital showup was imperative and did not deny Stovall due process.

## Conclusion
On these facts the suggestive hospital showup did not violate due process; the judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The origin of the due-process attack on suggestive identifications; the reliability-focused "linchpin" test was later developed in [[Neil v. Biggers]] and [[Manson v. Brathwaite]]. *Stovall*'s separate holding that the [[United States v. Wade]] / [[Gilbert v. California]] counsel rules were non-retroactive has been superseded by later retroactivity doctrine, but its due-process identification holding remains good law.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Stovall v. Denno*, 388 U.S. 293 (1967) — https://www.courtlistener.com/opinion/107488/stovall-v-denno/ — pinpoint: 302.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5f219475b8dfa030", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Stovall v. Denno"}, "payload": {"all": [{"cite": "388 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "388"}, {"cite": "87 S. Ct. 1967", "page": "1967", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 1199", "page": "1199", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1087", "page": "1087", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "388 U.S. 293", "official": {"cite": "388 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "388"}, "official_selection_present": true, "record_id": "Stovall v. Denno"}}
{"assertion_id": "2250b524addfdeb3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-302", "record_id": "Stovall v. Denno"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-302", "pinpoint_status": "slip-only", "quote": "--- # Stovall v. Denno *388 U.S. 293 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Stovall was brought, handcuffed, to the hospital room of a stabbing victim (Mrs. Behrendt)—who was the only person who could identify her attacker and might not survive—where she identified him in a one-on-one showup. He challenged the identification as unnecessarily suggestive and as a denial of due process, independent of any right-to-counsel claim. ## Issue Whether an unnecessarily suggestive identification procedure can violate due process, and how that claim is judged. ## Rule Suggestive identification procedures are tested for due-process fairness under the totality of the circumstances. The claim asks whether", "quote_fidelity": "mismatch", "record_id": "Stovall v. Denno", "star_marker": null}}
{"assertion_id": "bf5a6f26a87aa6bf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-302a", "record_id": "Stovall v. Denno"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-302a", "pinpoint_status": "slip-only", "quote": "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it.", "quote_fidelity": "mismatch", "record_id": "Stovall v. Denno", "star_marker": null}}
{"assertion_id": "9bbaf957a35860b3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Stovall v. Denno"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Stovall v. Denno", "scope_note": "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite.", "varies_by_point": false}}
```

### lake record — Stovall v. Denno

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stovall v. Denno",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stovall v. Denno",
    "case_name_short": "Stovall",
    "case_name_full": "Stovall v. Denno, Warden",
    "input_case_name": "Stovall v. Denno",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": "254",
    "cluster_id": 107488,
    "lead_opinion_id": 107488,
    "sibling_ids": [
      107488,
      9423482,
      9423483
    ],
    "absolute_url": "/opinion/107488/stovall-v-denno/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 293",
      "volume": "388",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1967",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1199",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1087",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1087",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 293",
        "volume": "388",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1967",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1199",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1087",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1087",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-302",
      "page": null,
      "quote": "--- # Stovall v. Denno *388 U.S. 293 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Stovall was brought, handcuffed, to the hospital room of a stabbing victim (Mrs. Behrendt)\u2014who was the only person who could identify her attacker and might not survive\u2014where she identified him in a one-on-one showup. He challenged the identification as unnecessarily suggestive and as a denial of due process, independent of any right-to-counsel claim. ## Issue Whether an unnecessarily suggestive identification procedure can violate due process, and how that claim is judged. ## Rule Suggestive identification procedures are tested for due-process fairness under the totality of the circumstances. The claim asks whether",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-302a",
      "page": null,
      "quote": "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Stovall v. Denno",
    "varies_by_point": false,
    "scope_note": "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Hopkins",
          "cluster_id": 4607692,
          "cite": [
            "920 F.3d 690"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neil C. Albee v. State of Indiana",
          "cluster_id": 4371568,
          "cite": [
            "71 N.E.3d 856",
            "2017 WL 765903",
            "2017 Ind. App. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
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
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. David Ruiz-Hiracheta",
          "cluster_id": 2766491,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. David Ruiz-Hiracheta",
          "cluster_id": 2766490,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Andres Deleon-Gloria",
          "cluster_id": 2766489,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Andres Deleon-Gloria",
          "cluster_id": 2766488,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Escalante-Reyes",
          "cluster_id": 805234,
          "cite": [
            "689 F.3d 415",
            "2012 WL 3024195",
            "2012 U.S. App. LEXIS 15385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Batson v. Kentucky",
          "cluster_id": 111662,
          "cite": [
            "90 L. Ed. 2d 69",
            "106 S. Ct. 1712",
            "476 U.S. 79",
            "1986 U.S. LEXIS 150",
            "54 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Witherspoon v. Illinois",
          "cluster_id": 107715,
          "cite": [
            "20 L. Ed. 2d 776",
            "88 S. Ct. 1770",
            "391 U.S. 510",
            "1968 U.S. LEXIS 1469",
            "46 Ohio Op. 2d 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. Kentucky",
          "cluster_id": 111785,
          "cite": [
            "93 L. Ed. 2d 649",
            "107 S. Ct. 708",
            "479 U.S. 314",
            "1987 U.S. LEXIS 283",
            "55 U.S.L.W. 4089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Geesa v. State",
          "cluster_id": 1522092,
          "cite": [
            "820 S.W.2d 154",
            "1991 Tex. Crim. App. LEXIS 240",
            "1991 WL 226418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107488 OR 9423482 OR 9423483) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzExMTIwMDAwMDAwJnM9MzEwNjk3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107488+OR+9423482+OR+9423483%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(107488 OR 9423482 OR 9423483)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTQmcz0xMjMxMjk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107488+OR+9423482+OR+9423483%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107488 OR 9423482 OR 9423483)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107488 OR 9423482 OR 9423483)",
    "indexed_citing_opinions": 4105,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107488,
        "count": 3847,
        "count_source": "search"
      },
      {
        "opinion_id": 9423482,
        "count": 359,
        "count_source": "search"
      },
      {
        "opinion_id": 9423483,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6067,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stovall-v-denno.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNzg3NDUmcz05NDE2OTMzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107488+OR+9423482+OR+9423483%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107488,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 270486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 271227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 271407,
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
    "date_created": "2026-07-05T21:06:15Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:09:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stovall v. Denno

```
<div>
<center><b><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U.S. 293</a></span> (1967)</b></center>
<center><h1>STOVALL<br>
v.<br>
DENNO, WARDEN.</h1></center>
<center>No. 254.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 16, 1967.</center>
<center>Decided June 12, 1967.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*294</span> <i>Leon B. Polsky</i> argued the cause and filed briefs for petitioner.</p>
<p><i>William Cahn</i> argued the cause and filed a brief for respondent.</p>
<p><i>H. Richard Uviller</i> argued the cause and filed a brief for the New York State District Attorneys' Association, as <i>amicus curiae,</i> urging affirmance.</p>
<p><i>Louis J. Lefkowitz,</i> Attorney General, <i>pro se, Samuel A. Hirshowitz,</i> First Assistant Attorney General, and <i>Barry Mahoney,</i> Assistant Attorney General, filed a brief for the Attorney General of New York, as <i>amicus curiae,</i> urging affirmance.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>This federal habeas corpus proceeding attacks collaterally a state criminal conviction for the same alleged constitutional errors in the admission of allegedly tainted identification evidence that were before us on direct review of the convictions involved in <i>United States</i> v. <i>Wade, ante,</i> p. 218, and <i>Gilbert</i> v. <i>California, ante,</i> p. 263. This case therefore provides a vehicle for deciding the extent to which the rules announced in <i>Wade</i> and <i>Gilbert</i> requiring the exclusion of identification evidence which is tainted by exhibiting the accused to identifying witnesses before trial in the absence of his counselare to be applied retroactively. See <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>; <i>Tehan</i> v. <i>Shott,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./382/406/">382 U. S. 406</a></span>; <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span>.<sup>[1]</sup> A further question is whether in any event, on the facts of the particular confrontation <span class="star-pagination">*295</span> involved in this case, petitioner was denied due process of law in violation of the Fourteenth Amendment. Cf. <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>.</p>
<p>Dr. Paul Behrendt was stabbed to death in the kitchen of his home in Garden City, Long Island, about midnight August 23, 1961. Dr. Behrendt's wife, also a physician, had followed her husband to the kitchen and jumped at the assailant. He knocked her to the floor and stabbed her 11 times. The police found a shirt on the kitchen floor and keys in a pocket which they traced to petitioner. They arrested him on the afternoon of August 24. An arraignment was promptly held but was postponed until petitioner could retain counsel.</p>
<p>Mrs. Behrendt was hospitalized for major surgery to save her life. The police, without affording petitioner time to retain counsel, arranged with her surgeon to permit them to bring petitioner to her hospital room about noon of August 25, the day after the surgery. Petitioner was handcuffed to one of five police officers who, with two members of the staff of the District Attorney, brought him to the hospital room. Petitioner was the only Negro in the room. Mrs. Behrendt identified him from her hospital bed after being asked by an officer whether he "was the man" and after petitioner repeated at the direction of an officer a "few words for voice identification." None of the witnesses could recall the words that were used. Mrs. Behrendt and the officers testified at the trial to her identification of the petitioner in the hospital room, and she also made an in-court identification of petitioner in the courtroom.</p>
<p>Petitioner was convicted and sentenced to death. The New York Court of Appeals affirmed without opinion. 13 N. Y. 2d 1094, <span class="citation" data-id="5521096"><a href="/opinion/5673625/people-v-stovall/" aria-description="Citation for case: People v. Stovall">196 N. E. 2d 65</a></span>. Petitioner <i>pro se</i> sought federal habeas corpus in the District Court for the Southern District of New York. He claimed that among other constitutional rights allegedly denied him <span class="star-pagination">*296</span> at his trial, the admission of Mrs. Behrendt's identification testimony violated his rights under the Fifth, Sixth, and Fourteenth Amendments because he had been compelled to submit to the hospital room confrontation without the help of counsel and under circumstances which unfairly focused the witness' attention on him as the man believed by the police to be the guilty person. The District Court dismissed the petition after hearing argument on an unrelated claim of an alleged invalid search and seizure. On appeal to the Court of Appeals for the Second Circuit a panel of that court initially reversed the dismissal after reaching the issue of the admissibility of Mrs. Behrendt's identification evidence and holding it inadmissible on the ground that the hospital room identification violated petitioner's constitutional right to the assistance of counsel. The Court of Appeals thereafter heard the case <i>en banc,</i> vacated the panel decision, and affirmed the District Court. <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1000/">384 U. S. 1000</a></span>, and set the case for argument with <i>Wade</i> and <i>Gilbert.</i> We hold that <i>Wade</i> and <i>Gilbert</i> affect only those cases and all future cases which involve confrontations for identification purposes conducted in the absence of counsel after this date. The rulings of <i>Wade</i> and <i>Gilbert</i> are therefore inapplicable in the present case. We think also that on the facts of this case petitioner was not deprived of due process of law in violation of the Fourteenth Amendment. The judgment of the Court of Appeals is, therefore, affirmed.</p>
<p></p>
<h2>I.</h2>
<p>Our recent discussions of the retroactivity of other constitutional rules of criminal procedure make unnecessary any detailed treatment of that question here. <i>Linkletter</i> v. <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Walker, supra</a></span></i><i>; </i><i>Tehan</i> v. <i>Shott, supra</i><i>; </i><i>Johnson</i> v. <i>New <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Jersey, supra</a></span></i><i>.</i> "These cases establish the principle that in criminal litigation concerning constitutional <span class="star-pagination">*297</span> claims, `the Court may in the interest of justice make the rule prospective . . . where the exigencies of the situation require such an application' . . . ." <i><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson, supra,</a></span></i> 384 U. S., at 726-727. The criteria guiding resolution of the question implicate (a) the purpose to be served by the new standards, (b) the extent of the reliance by law enforcement authorities on the old standards, and (c) the effect on the administration of justice of a retroactive application of the new standards. "[T]he retroactivity or nonretroactivity of a rule is not automatically determined by the provision of the Constitution on which the dictate is based. Each constitutional rule of criminal procedure has its own distinct functions, its own background of precedent, and its own impact on the administration of justice, and the way in which these factors combine must inevitably vary with the dictate involved." <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#728" aria-description="Citation for case: Johnson v. New Jersey"><i>Johnson, supra,</i> at 728</a></span>.</p>
<p><i>Wade</i> and <i>Gilbert</i> fashion exclusionary rules to deter law enforcement authorities from exhibiting an accused to witnesses before trial for identification purposes without notice to and in the absence of counsel. A conviction which rests on a mistaken identification is a gross miscarriage of justice. The <i>Wade</i> and <i>Gilbert</i> rules are aimed at minimizing that possibility by preventing the unfairness at the pretrial confrontation that experience has proved can occur and assuring meaningful examination of the identification witness' testimony at trial. Does it follow that the rules should be applied retroactively? We do not think so.</p>
<p>It is true that the right to the assistance of counsel has been applied retroactively at stages of the prosecution where denial of the right must almost invariably deny a fair trial, for example, at the trial itself. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, or at some forms of arraignment. <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>, or on appeal, <i>Douglas</i> v. <i>California,</i> <span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span>. "The basic purpose <span class="star-pagination">*298</span> of a trial is the determination of truth, and it is self-evident that to deny a lawyer's help through the technical intricacies of a criminal trial or to deny a full opportunity to appeal a conviction because the accused is poor is to impede that purpose and to infect a criminal proceeding with the clear danger of convicting the innocent." <i>Tehan</i> v. <i>Shott, supra,</i> at 416. We have also retroactively applied rules of criminal procedure fashioned to correct serious flaws in the fact-finding process at trial. See for example <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span>. Although the <i>Wade</i> and <i>Gilbert</i> rules also are aimed at avoiding unfairness at the trial by enhancing the reliability of the fact-finding process in the area of identification evidence, "the question whether a constitutional rule of criminal procedure does or does not enhance the reliability of the fact-finding process at trial is necessarily a matter of degree." <i>Johnson</i> v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#728" aria-description="Citation for case: Johnson v. New Jersey"><i>New Jersey, supra,</i> at 728-729</a></span>. The extent to which a condemned practice infects the integrity of the truth-determining process at trial is a "question of probabilities." 384 U. S., at 729. Such probabilities must in turn be weighed against the prior justified reliance upon the old standard and the impact of retroactivity upon the administration of justice.</p>
<p>We have outlined in <i>Wade</i> the dangers and unfairness inherent in confrontations for identification. The possibility of unfairness at that point is great, both because of the manner in which confrontations are frequently conducted, and because of the likelihood that the accused will often be precluded from reconstructing what occurred and thereby from obtaining a full hearing on the identification issue at trial. The presence of counsel will significantly promote fairness at the confrontation and a full hearing at trial on the issue of identification. We have, therefore, concluded that the confrontation is a "critical stage," and that counsel is required at all confrontations. It must be recognized, however, that, unlike <span class="star-pagination">*299</span> cases in which counsel is absent at trial or on appeal, it may confidently be assumed that confrontations for identification can be and often have been conducted in the absence of counsel with scrupulous fairness and without prejudice to the accused at trial. Therefore, while we feel that the exclusionary rules set forth in <i>Wade</i> and <i>Gilbert</i> are justified by the need to assure the integrity and reliability of our system of justice, they undoubtedly will affect cases in which no unfairness will be present. Of course, we should also assume there have been injustices in the past which could have been averted by having counsel present at the confrontation for identification, just as there are injustices when counsel is absent at trial. But the certainty and frequency with which we can say in the confrontation cases that no injustice occurred differs greatly enough from the cases involving absence of counsel at trial or on appeal to justify treating the situations as different in kind for the purpose of retroactive application, especially in light of the strong countervailing interests outlined below, and because it remains open to all persons to allege and prove, as Stovall attempts to do in this case, that the confrontation resulted in such unfairness that it infringed his right to due process of law. See <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span> (C. A. 4th Cir. 1966).</p>
<p>The unusual force of the countervailing considerations strengthens our conclusion in favor of prospective application. The law enforcement officials of the Federal Government and of all 50 States have heretofore proceeded on the premise that the Constitution did not require the presence of counsel at pretrial confrontations for identification. Today's rulings were not foreshadowed in our cases; no court announced such a requirement until <i>Wade</i> was decided by the Court of Appeals for the Fifth Circuit, <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d 557</a></span>. The overwhelming majority of American courts have always treated the evidence question <span class="star-pagination">*300</span> not as one of admissibility but as one of credibility for the jury. Wall, Eye-Witness Identification in Criminal Cases 38. Law enforcement authorities fairly relied on this virtually unanimous weight of authority, now no longer valid, in conducting pretrial confrontations in the absence of counsel. It is, therefore, very clear that retroactive application of <i>Wade</i> and <i>Gilbert</i> "would seriously disrupt the administration of our criminal laws." <i>Johnson</i> v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#731" aria-description="Citation for case: Johnson v. New Jersey"><i>New Jersey, supra,</i> at 731</a></span>. In <i>Tehan</i> v. <i>Shott, supra</i><i>,</i> we thought it persuasive against retroactive application of the no-comment rule of <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>, that such application would have a serious impact on the six States that allowed comment on an accused's failure to take the stand. We said, "To require all of those States now to void the conviction of every person who did not testify at his trial would have an impact upon the administration of their criminal law so devastating as to need no elaboration." 382 U. S., at 419. That impact is insignificant compared to the impact to be expected from retroactivity of the <i>Wade</i> and <i>Gilbert</i> rules. At the very least, the processing of current criminal calendars would be disrupted while hearings were conducted to determine taint, if any, in identification evidence, and whether in any event the admission of the evidence was harmless error. Doubtless, too, inquiry would be handicapped by the unavailability of witnesses and dim memories. We conclude, therefore, that the <i>Wade</i> and <i>Gilbert</i> rules should not be made retroactive.</p>
<p>We also conclude that, for these purposes, no distinction is justified between convictions now final, as in the instant case, and convictions at various stages of trial and direct review. We regard the factors of reliance and burden on the administration of justice as entitled to such overriding significance as to make that distinction <span class="star-pagination">*301</span> unsupportable.<sup>[2]</sup> We recognize that Wade and Gilbert are, therefore, the only victims of pretrial confrontations in the absence of their counsel to have the benefit of the rules established in their cases. That they must be given that benefit is, however, an unavoidable consequence of the necessity that constitutional adjudications not stand as mere dictum. Sound policies of decision-making, rooted in the command of Article III of the Constitution that we resolve issues solely in concrete cases or controversies,<sup>[3]</sup> and in the possible effect upon the incentive of counsel to advance contentions requiring a change in the law,<sup>[4]</sup> militate against denying Wade and Gilbert the benefit of today's decisions. Inequity arguably results from according the benefit of a new rule to the parties in the case in which it is announced but not to other litigants similarly situated in the trial or appellate process who have raised the same issue.<sup>[5]</sup> But we regard the fact that the parties involved are chance beneficiaries as an insignificant cost for adherence to sound principles of decision-making.</p>
<p></p>
<h2>II.</h2>
<p>We turn now to the question whether petitioner, although not entitled to the application of <i>Wade</i> and <i>Gilbert</i> to his case, is entitled to relief on his claim that in any event the confrontation conducted in this <span class="star-pagination">*302</span> case was so unnecessarily suggestive and conductive to irreparable mistaken identification that he was denied due process of law. This is a recognized ground of attack upon a conviction independent of any right to counsel claim. <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span> (C. A. 4th Cir. 1966). The practice of showing suspects singly to persons for the purpose of identification, and not as part of a lineup, has been widely condemned.<sup>[6]</sup> However, a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it, and the record in the present case reveals that the showing of Stovall to Mrs. Behrendt in an immediate hospital confrontation was imperative. The Court of Appeals, <i>en banc,</i> stated <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#735" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d, at 735</a></span>,</p>
<blockquote>"Here was the only person in the world who could possibly exonerate Stovall. Her words, and only her words, `He is not the man' could have resulted in freedom for Stovall. The hospital was not far distant from the courthouse and jail. No one knew how long Mrs. Behrendt might live. Faced with the responsibility of identifying the attacker, with the need for immediate action and with the knowledge that Mrs. Behrendt could not visit the jail, the police followed the only feasible procedure and took Stovall to the hospital room. Under these circumstances, the usual police station line-up, which Stovall now argues he should have had, was out of the question."</blockquote>
<p>The judgment of the Court of Appeals is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE DOUGLAS is of the view that the deprivation of the right to counsel in the setting of this case <span class="star-pagination">*303</span> should be given retroactive effect as it was in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, and in <i>Douglas</i> v. <i>California,</i> <span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span>. And see <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#640" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 640</a></span> (dissenting opinion); <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#736" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 736</a></span> (dissenting opinion).</p>
<p>MR. JUSTICE FORTAS would reverse and remand for a new trial on the ground that the State's reference at trial to the improper hospital identification violated petitioner's Fourteenth Amendment rights and was prejudicial. He would not reach the question of retroactivity of <i>Wade</i> and <i>Gilbert.</i></p>
<p>MR. JUSTICE WHITE, whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART join.</p>
<p>For the reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, ante,</i> p. 250, I perceive no constitutional error in the identification procedure to which the petitioner was subjected. I concur in the result and in that portion of the Court's opinion which limits application of the new Sixth Amendment rule.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>In <i>United States</i> v. <i>Wade, ante,</i> p. 218, and <i>Gilbert</i> v. <i>California, ante,</i> p. 263, the Court holds that lineup identification testimony should be excluded if it was obtained by exhibiting an accused to identifying witnesses before trial in the absence of his counsel. I concurred in part in those holdings as to out-of-court lineup identification on the ground that the right to counsel is guaranteed in federal courts by the Sixth Amendment and in state courts by the Sixth and Fourteenth Amendments. The first question in this case is whether other defendants, already in prison on <span class="star-pagination">*304</span> such unconstitutional evidence, shall be accorded the benefit of the rule. In this case the Court holds that the petitioner here, convicted on such unconstitutional evidence, must remain in prison, and that besides Wade and Gilbert, who are "chance beneficiaries," no one can invoke the rule except defendants exhibited in lineups in the future. I dissent from that holding. It keeps people serving sentences who were convicted through the use of unconstitutional evidence. This is sought to be justified on the ground that retroactive application of the holding in <i>Gilbert</i> and <i>Wade</i> would somehow work a "burden on the administration of justice" and would not serve the Court's purpose "to deter law enforcement authorities." It seems to me that to deny this petitioner and others like him the benefit of the new rule deprives them of a constitutional trial and perpetrates a rank discrimination against them. Once the Court determines what the Constitution says, I do not believe it has the power, by weighing "countervailing interests," to legislate a timetable by which the Constitution's provisions shall become effective. For reasons stated in my dissent in <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#640" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 640</a></span>, I would hold that the petitioner here and every other person in jail under convictions based on unconstitutional evidence should be given the advantage of today's newly announced constitutional rules.</p>
<p>The Court goes on, however, to hold that even though its new constitutional rule about the Sixth Amendment's right to counsel cannot help this petitioner, he is nevertheless entitled to a consideration of his claim, "independent of any right to counsel claim," that his identification by one of the victims of the robbery was made under circumstances so "unfair" that he was denied "due process of law" guaranteed by the Fourteenth Amendment. Although the Court finds petitioner's claim without merit, I dissent from its holding that a general <span class="star-pagination">*305</span> claim of "unfairness" at the lineup is "open to all persons to allege and prove." The term "due process of law" is a direct descendant of Magna Charta's promise of a trial according to the "law of the land" as it has been established by the lawmaking agency, constitutional or legislative. No one has ever been able to point to a word in our constitutional history that shows the Framers ever intended that the Due Process Clause of the Fifth or Fourteenth Amendment was designed to mean any more than that defendants charged with crimes should be entitled to a trial governed by the laws, constitutional and statutory, that are in existence at the time of the commission of the crime and the time of the trial. The concept of due process under which the Court purports to decide this question, however, is that this Court looks at "the totality of the circumstances" of a particular case to determine in its own judgment whether they comport with the Court's notions of decency, fairness, and fundamental justice, and, if so, declares they comport with the Constitution, and, if not, declares they are forbidden by the Constitution. See, <i>e. g., </i><i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>. Such a constitutional formula substitutes this Court's judgment of what is right for what the Constitution declares shall be the supreme law of the land. This due process notion proceeds as though our written Constitution, designed to grant limited powers to government, had neutralized its limitations by using the Due Process Clause to authorize this Court to override its written limiting language by substituting the Court's view of what powers the Framers should have granted government. Once again I dissent from any such view of the Constitution. Where accepted, its result is to make this Court not a Constitution-interpreter, but a day-to-day Constitution-maker.</p>
<p>But even if the Due Process Clause could possibly be construed as giving such latitudinarian powers to the <span class="star-pagination">*306</span> Court, I would still think the Court goes too far in holding that the courts can look at the particular circumstances of each identification lineup to determine at large whether they are too "suggestive and conducive to irreparable mistaken identification" to be constitutional. That result is to freeze as constitutional or as unconstitutional the circumstances of each case, giving the States and the Federal Government no permanent constitutional standards. It also transfers to this Court power to determine what the Constitution should say, instead of performance of its undoubted constitutional power to determine what the Constitution does say. And the result in this particular case is to put into a constitutional mould a rule of evidence which I think is plainly within the constitutional powers of the States in creating and enforcing their own criminal laws. I must say with all deference that for this Court to hold that the Due Process Clause gives it power to bar state introduction of lineup testimony on its notion of fairness, not because it violates some specific constitutional prohibition, is an arbitrary, wholly capricious action.</p>
<p>I would not affirm this case but would reverse and remand for consideration of whether the out-of-court lineup identification of petitioner was, under <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, harmless error. If it was not, petitioner is entitled to a new trial because of a denial of the right to counsel guaranteed by the Sixth Amendment which the Fourteenth Amendment makes obligatory on the States.</p>
<h2>NOTES</h2>
<p>[1]  Although respondent did not raise the bar of retroactivity, the Attorney General of the State of New York, as <i>amicus curiae,</i> extensively briefed the issue of retroactivity and petitioner, in his reply brief, addressed himself to this question. Compare <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#646" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 646, n. 3</a></span>.</p>
<p>[2]  Schaefer, The Control of "Sunbursts": Techniques of Prospective Overruling, 22 Record of N. Y. C. B. A. 394, 408-411 (1967).</p>
<p>[3]  Note, Prospective Overruling and Retroactive Application in the Federal Courts, 71 Yale L. J. 907, 930-933 (1962).</p>
<p>[4]  See Mishkin, Foreword, The Supreme Court 1964 Term, <span class="citation no-link">79 Harv. L. Rev. 56</span>, 60-61 (1965).</p>
<p>[5]  See Mishkin, n. 4, <i>supra,</i> at 61, n. 23; Bender, The Retroactive Effect of an Overruling Constitutional Decision: <i>Mapp</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span>,</i> <span class="citation no-link">110 U. Pa. L. Rev. 650</span>, 675-678 (1962); Schwartz, Retroactivity, Reliability, and Due Process: A Reply to Professor Mishkin, <span class="citation no-link">33 U. Chi. L. Rev. 719</span>, 764 (1966).</p>
<p>[6]  See Wall, Eye-Witness Identification in Criminal Cases 26-40; Paul, Identification of Accused Persons, 12 Austl. L. J. 42, 44 (1938); Williams &amp; Hammelmann, Identification Parades, Part I, [1963] Crim. L. Rev. 479, 480-481; Frankfurter, The Case of Sacco and Vanzetti 31-32.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Strickler v. Greene.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Strickler v. Greene"
type: case
citation: "527 U.S. 263 (1999)"
parallel_cite: "119 S. Ct. 1936; 144 L. Ed. 2d 286"
neutral_cite: 1999 U.S. LEXIS 4191
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-06-17
docket: 98-5864
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Strickler v. Greene
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118307/strickler-v-greene/"
  cluster_id: 118307
  opinion_id: 118307
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Smith v. Cain]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]"]
aliases: []
tags: ["case", "brady", "materiality", "suppression", "prejudice"]
holding: "Canonical statement of the THREE Brady components: (1) the evidence must be favorable (exculpatory OR impeaching); (2) it must have been…"
lake:
  record_id: Strickler v. Greene
  status: verified
  projected_at: 2026-07-06
---

# Strickler v. Greene

*527 U.S. 263 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Strickler was convicted of capital murder. The prosecution had not disclosed police notes and letters showing that a key eyewitness, Anne Stoltzfus, had initially been unable to recall the events she later described with confidence at trial. Strickler raised a *[[Brady v. Maryland|Brady]]* claim in federal [[Common Legal Terms#habeas-corpus|habeas]].

## Issue
What a defendant must establish to prove a *[[Brady v. Maryland|Brady]]* violation.

## Rule
The Court set out the elements of a *[[Brady v. Maryland|Brady]]* violation. "There are three components of a true *Brady* violation: The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." — 527 U.S. at 281–282. ^pin-281

As to that prejudice (materiality) element, "strictly speaking, there is never a real '*Brady* violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict." — *Id.* at 281. ^pin-281a

## Application
The undisclosed documents were favorable because they impeached Stoltzfus, and they had been suppressed by the State—so two components were established. But the Court found no reasonable probability of a different verdict given the other evidence of guilt, so the prejudice component was not met and Strickler's claim failed.

## Conclusion
The three-component *[[Brady v. Maryland|Brady]]* standard governs, but because Strickler did not show prejudice, relief was denied.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The canonical statement of the [[Brady v. Maryland]] elements, incorporating impeachment evidence ([[Giglio v. United States]]) and the reasonable-probability materiality standard of [[United States v. Bagley]] / [[Kyles v. Whitley]]; applied in [[Smith v. Cain]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Strickler v. Greene*, 527 U.S. 263 (1999) — https://www.courtlistener.com/opinion/118307/strickler-v-greene/ — pinpoints: 281, 282.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4203f09e3acfdaf2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Strickler v. Greene"}, "payload": {"all": [{"cite": "527 U.S. 263", "page": "263", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "527"}, {"cite": "119 S. Ct. 1936", "page": "1936", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "144 L. Ed. 2d 286", "page": "286", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "144"}, {"cite": "1999 U.S. LEXIS 4191", "page": "4191", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "527 U.S. 263", "official": {"cite": "527 U.S. 263", "page": "263", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "527"}, "official_selection_present": true, "record_id": "Strickler v. Greene"}}
{"assertion_id": "147a3c5b45c85383", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-281", "record_id": "Strickler v. Greene"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-281", "pinpoint_status": "slip-only", "quote": "--- # Strickler v. Greene *527 U.S. 263 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Strickler was convicted of capital murder. The prosecution had not disclosed police notes and letters showing that a key eyewitness, Anne Stoltzfus, had initially been unable to recall the events she later described with confidence at trial. Strickler raised a *Brady* claim in federal habeas. ## Issue What a defendant must establish to prove a *Brady* violation. ## Rule The Court set out the elements of a *Brady* violation.", "quote_fidelity": "mismatch", "record_id": "Strickler v. Greene", "star_marker": null}}
{"assertion_id": "3600816a74599fb6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-281a", "record_id": "Strickler v. Greene"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-281a", "pinpoint_status": "slip-only", "quote": "strictly speaking, there is never a real '*Brady* violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict.", "quote_fidelity": "mismatch", "record_id": "Strickler v. Greene", "star_marker": null}}
{"assertion_id": "4dd0281d0128c6cd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Strickler v. Greene"}, "payload": {"as_of_content": "1999-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Strickler v. Greene", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Strickler v. Greene

```json
{
  "schema_version": "s2.v1",
  "record_id": "Strickler v. Greene",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Strickler v. Greene",
    "case_name_short": "Strickler",
    "case_name_full": "Strickler v. Greene, Warden",
    "input_case_name": "Strickler v. Greene",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-06-17",
    "year": 1999,
    "docket": "98-5864",
    "cluster_id": 118307,
    "lead_opinion_id": 118307,
    "sibling_ids": [
      118307,
      9433839,
      9433840
    ],
    "absolute_url": "/opinion/118307/strickler-v-greene/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "527 U.S. 263",
      "volume": "527",
      "reporter": "U.S.",
      "page": "263",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1936",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 286",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 4191",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4191",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "527 U.S. 263",
        "volume": "527",
        "reporter": "U.S.",
        "page": "263",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1936",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 286",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "286",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 4191",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4191",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "527 U.S. 263",
    "official_selection": {
      "court_class": "scotus",
      "selected": "527 U.S. 263",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-281",
      "page": null,
      "quote": "--- # Strickler v. Greene *527 U.S. 263 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Strickler was convicted of capital murder. The prosecution had not disclosed police notes and letters showing that a key eyewitness, Anne Stoltzfus, had initially been unable to recall the events she later described with confidence at trial. Strickler raised a *Brady* claim in federal habeas. ## Issue What a defendant must establish to prove a *Brady* violation. ## Rule The Court set out the elements of a *Brady* violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-281a",
      "page": null,
      "quote": "strictly speaking, there is never a real '*Brady* violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Strickler v. Greene",
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
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 10309030,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane1_negative"
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
        "journal_ref": "Strickler v. Greene:lane1_negative"
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
        "journal_ref": "Strickler v. Greene:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ardolino v. People",
          "cluster_id": 2595020,
          "cite": [
            "69 P.3d 73",
            "2003 WL 21057416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
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
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Pitsonbarger",
          "cluster_id": 2024743,
          "cite": [
            "793 N.E.2d 609",
            "205 Ill. 2d 444",
            "275 Ill. Dec. 838"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sykes v. Anderson",
          "cluster_id": 178987,
          "cite": [
            "625 F.3d 294",
            "2010 U.S. App. LEXIS 23204",
            "2010 WL 4453313"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sean Howell",
          "cluster_id": 771006,
          "cite": [
            "231 F.3d 615",
            "55 Fed. R. Serv. 1314",
            "2000 Daily Journal DAR 11612",
            "2000 Cal. Daily Op. Serv. 8736",
            "2000 U.S. App. LEXIS 27067",
            "2000 WL 1617019"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sullivan",
          "cluster_id": 2973136,
          "cite": [
            "431 F.3d 976",
            "2005 U.S. App. LEXIS 28073",
            "2005 WL 3466534"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyron Brown v. Lee Lucas",
          "cluster_id": 2675935,
          "cite": [
            "753 F.3d 606",
            "2014 WL 2198419",
            "2014 U.S. App. LEXIS 9771"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joe D'Ambrosio v. Carmen Marino",
          "cluster_id": 2658128,
          "cite": [
            "747 F.3d 378",
            "2014 WL 1243792",
            "2014 U.S. App. LEXIS 5588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kwame Ajamu v. City of Cleveland",
          "cluster_id": 4621394,
          "cite": [
            "925 F.3d 793"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo, United States of America v. Leonard A. Pelullo",
          "cluster_id": 789362,
          "cite": [
            "399 F.3d 197",
            "2005 WL 433589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. LaMar",
          "cluster_id": 10686381,
          "cite": [
            "2002 Ohio 2128",
            "95 Ohio St. 3d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aldrich v. Bock",
          "cluster_id": 2453961,
          "cite": [
            "327 F. Supp. 2d 743",
            "2004 U.S. Dist. LEXIS 14683",
            "2004 WL 1682907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortiz v. Barkley",
          "cluster_id": 1810562,
          "cite": [
            "558 F. Supp. 2d 444",
            "2008 U.S. Dist. LEXIS 43653",
            "2008 WL 2266313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Cain",
          "cluster_id": 620666,
          "cite": [
            "181 L. Ed. 2d 571",
            "132 S. Ct. 627",
            "565 U.S. 73",
            "2012 U.S. LEXIS 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunlap v. State",
          "cluster_id": 2508569,
          "cite": [
            "106 P.3d 376",
            "141 Idaho 50",
            "2004 Ida. LEXIS 194"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Spotz",
          "cluster_id": 2074443,
          "cite": [
            "896 A.2d 1191",
            "587 Pa. 1",
            "2006 Pa. LEXIS 659"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lesko",
          "cluster_id": 2422962,
          "cite": [
            "15 A.3d 345",
            "609 Pa. 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Albarran",
          "cluster_id": 2276132,
          "cite": [
            "57 Cal. Rptr. 3d 92",
            "149 Cal. App. 4th 214",
            "2007 Cal. Daily Op. Serv. 3495",
            "2007 Daily Journal DAR 4378",
            "2007 Cal. App. LEXIS 486"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Chavez",
          "cluster_id": 2333628,
          "cite": [
            "213 S.W.3d 320",
            "2006 Tex. Crim. App. LEXIS 2294",
            "2006 WL 3391014"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Strickler v. Greene:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118307 OR 9433839 OR 9433840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQ1MDU2MDAwMDAwJnM9NjM1ODAyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118307+OR+9433839+OR+9433840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118307 OR 9433839 OR 9433840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yODYmcz03OTE5NDgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118307+OR+9433839+OR+9433840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118307 OR 9433839 OR 9433840)",
        "reviewed": 146,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 146,
        "triage_read": 4,
        "triage_snippet_classified": 142
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118307 OR 9433839 OR 9433840)",
    "indexed_citing_opinions": 2221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118307,
        "count": 1865,
        "count_source": "search"
      },
      {
        "opinion_id": 9433839,
        "count": 379,
        "count_source": "search"
      },
      {
        "opinion_id": 9433840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4395,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/strickler-v-greene.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzM5OTImcz0xMDYyNDU0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118307+OR+9433839+OR+9433840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118307,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 104321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 104547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 106440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 109380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 110797,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 111984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 112893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 117987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 118205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 683528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1219071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1348258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118307,
        "cited_id": 1385494,
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
    "date_created": "2026-07-05T21:09:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:12:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:09:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Strickler v. Greene (truncated)

```
<div>
<center><b><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U.S. 263</a></span> (1999)</b></center>
<center><h1>STRICKLER<br>
v.<br>
GREENE, WARDEN</h1></center>
<center>No. 98-5864.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 3, 1999.</center>
<center>Decided June 17, 1999.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*264</span> <span class="star-pagination">*265</span> Stevens, J., delivered the opinion of the Court, in which Rehnquist, C. J., and O'Connor, Scalia, Ginsburg, and Breyer, JJ., joined in full, in which Kennedy and Souter, JJ., joined as to Part III, and in which Thomas, J., joined as to Parts I and IV. Souter, J., filed an opinion concurring in part and dissenting in part, in which Kennedy, J., joined as to Part II, <i>post,</i> p. 296.</p>
<p><i>Miguel A. Estrada</i> argued the cause for petitioner. With him on the briefs were <i>Barbara L. Hartung, Mark E. Olive,</i>  and <i>John H. Blume.</i> </p>
<p><i>Pamela A. Rumpz,</i> Assistant Attorney General of Virginia, argued the cause for respondent. With her on the brief was <i>Mark L. Earley,</i> Attorney General.<sup>[*]</sup></p>
<p>Justice Stevens delivered the opinion of the Court.<sup>[]</sup></p>
<p>The District Court for the Eastern District of Virginia granted petitioner's application for a writ of habeas corpus and vacated his capital murder conviction and death sentence on the grounds that the Commonwealth had failed to disclose important exculpatory evidence and that petitioner had not, in consequence, received a fair trial. The Court of Appeals for the Fourth Circuit reversed because petitioner had not raised his constitutional claim at his trial or in state collateral proceedings. In addition, the Fourth Circuit concluded that petitioner's claim was, "in any event, without merit." App. 418, n. 8.<sup>[1]</sup> Finding the legal question presented by this <span class="star-pagination">*266</span> case considerably more difficult than the Fourth Circuit, we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./525/809/">525 U. S. 809</a></span> (1998), to consider (1) whether the Commonwealth violated <i>Brady</i> v. <i>Maryland,</i>  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), and its progeny; (2) whether there was an acceptable "cause" for petitioner's failure to raise this claim in state court; and (3), if so, whether he suffered prejudice sufficient to excuse his procedural default.</p>
<p></p>
<h2>I</h2>
<p>In the early evening of January 5, 1990, Leanne Whitlock, an African-American sophomore at James Madison University, was abducted from a local shopping center and robbed and murdered. In separate trials, both petitioner and Ronald Henderson were convicted of all three offenses. Henderson was convicted of first-degree murder, a noncapital offense, whereas petitioner was convicted of capital murder and sentenced to death.<sup>[2]</sup></p>
<p>At both trials, a woman named Anne Stoltzfus testified in vivid detail about Whitlock's abduction. The exculpatory material that petitioner claims should have been disclosed before trial includes documents prepared by Stoltzfus, and notes of interviews with her, that impeach significant portions of her testimony. We begin, however, by noting that, even without the Stoltzfus testimony, the evidence in the record was sufficient to establish petitioner's guilt on the murder charge. Whether petitioner would have been convicted of capital murder and received the death sentence if she had not testified, or if she had been sufficiently impeached, is less clear. To put the question in context, we review the trial testimony at some length.</p>
<p><i>The Testimony at Trial</i> </p>
<p>At about 4:30 p.m. on January 5, 1990, Whitlock borrowed a 1986 blue Mercury Lynx from her boyfriend, John Dean, <span class="star-pagination">*267</span> who worked in the Valley Shopping Mall in Harrisonburg, Virginia. At about 6:30 or 6:45 p.m., she left her apartment, intending to return the car to Dean at the mall. She did not return the car and was not again seen alive by any of her friends or family.</p>
<p>Petitioner's mother testified that she had driven petitioner and Henderson to Harrisonburg on January 5. She also testified that petitioner always carried a hunting knife that had belonged to his father. Two witnesses, a friend of Henderson's and a security guard, saw petitioner and Henderson at the mall that afternoon. The security guard was informed around 3:30 p.m. that two men, one of whom she identified at trial as petitioner, were attempting to steal a car in the parking lot. She had them under observation during the remainder of the afternoon but lost sight of them at about 6:45.</p>
<p>At approximately 7:30 p.m., a witness named Kurt Massie saw the blue Lynx at a location in Augusta County about 25 miles from Harrisonburg and a short distance from the cornfield where Whitlock's body was later found. Massie identified petitioner as the driver of the vehicle; he also saw a white woman in the front seat and another man in the back. Massie noticed that the car was muddy, and that it turned off Route 340 onto a dirt road.</p>
<p>At about 8 p.m., another witness saw the Lynx at Buddy's Market, with two men sitting in the front seat. The witness did not see anyone else in the car. At approximately 9 p.m., petitioner and Henderson arrived at Dice's Inn, a bar in Staunton, Virginia, where they stayed for about four or five hours. They danced with several women, including four prosecution witnesses: Donna Kay Tudor, Nancy Simmons, Debra Sievers, and Carolyn Brown. While there, Henderson gave Nancy Simmons a watch that had belonged to Whitlock. Petitioner spent most of his time with Tudor, who was later arrested for grand larceny based on her possession of the blue Lynx.</p>
<p><span class="star-pagination">*268</span> These four women all testified that Tudor had arrived at Dice's at about 8 p.m. Three of them noticed nothing unusual about petitioner's appearance, but Tudor saw some blood on his jeans and a cut on his knuckle. Tudor also testified that she, Henderson, and petitioner left Dice's together after it closed to search for marijuana. Henderson was driving the blue Lynx, and petitioner and Tudor rode in back. Tudor related that petitioner was leaning toward Henderson and talking with him; she overheard a crude conversation that could reasonably be interpreted as describing the assault and murder of a black person with a "rock crusher." Tudor stated that petitioner made a statement that implied that he had killed someone, so the person "wouldn't give him no more trouble." App. 99. Tudor testified that while she, petitioner, and Henderson were driving around, petitioner took out his knife and threatened to stab Henderson because he was driving recklessly. Petitioner then began driving.</p>
<p>At about 4:30 or 5 a.m. on January 6, petitioner drove Henderson to Kenneth Workman's apartment in Timberville.<sup>[3]</sup> Henderson went inside to get something, and petitioner and Tudor drove off without waiting for him. Workman testified that Henderson had blood on his pants and stated he had killed a black person.</p>
<p>Petitioner and Tudor then drove to a motel in Blue Ridge. A day or two later they went to Virginia Beach, where they spent the rest of the week. Petitioner gave Tudor pearl earrings that Whitlock had been wearing when she was last seen. Tudor saw Whitlock's driver's license and bank card in the glove compartment of the car. Tudor testified that petitioner unsuccessfully attempted to use Whitlock's bank card when they were in Virginia Beach.</p>
<p>When petitioner and Tudor returned to Augusta County, they abandoned the blue Lynx. On January 11, the police identified the car as Dean's, and found petitioner's and Tudor's <span class="star-pagination">*269</span> fingerprints on both the inside and the outside of the car. They also found shoe impressions that matched the soles of shoes belonging to petitioner. Inside the car, they retrieved a jacket that contained identification papers belonging to Henderson.</p>
<p>The police also recovered a bag at petitioner's mother's house that Tudor testified she and petitioner had left when they returned from Virginia Beach. The bag contained, among other items, three identification cards belonging to Whitlock and a black "tank top" shirt that was later found to have human blood and semen stains on it. Tr. 707.</p>
<p>On January 13, a farmer called the police to advise them that he had found Henderson's wallet; a search of the area led to the discovery of Whitlock's frozen, nude, and battered body. A 69-pound rock, spotted with blood, lay nearby. Forensic evidence indicated that Whitlock's death was caused by "multiple blunt force injuries to the head." App. 109. The location of the rock and the human blood on the rock suggested that it had been used to inflict these injuries. Based on the contents of Whitlock's stomach, the medical examiner determined that she died fewer than six hours after she had last eaten.<sup>[4]</sup></p>
<p>A number of Caucasian hair samples were found at the scene, three of which were probably petitioner's. Given the weight of the rock, the prosecution argued that one of the killers must have held the victim down while the other struck her with the murder weapon.</p>
<p>Donna Tudor's estranged husband, Jay Tudor, was called by the defense and testified that in March she had told him that she was present at the murder scene and that petitioner did not participate in the murder. Jay Tudor's testimony was inconsistent in several respects with that of other witnesses. For example, he testified that several days elapsed <span class="star-pagination">*270</span> between the time that petitioner, Henderson, and Donna Tudor picked up Whitlock and the time of Whitlock's murder. <i>Anne Stoltzfus' Testimony</i> </p>
<p>Anne Stoltzfus testified that on two occasions on January 5 she saw petitioner, Henderson, and a blonde girl inside the Harrisonburg mall, and that she later witnessed their abduction of Whitlock in the parking lot. She did not call the police, but a week and a half after the incident she discussed it with classmates at James Madison University, where both she and Whitlock were students. One of them called the police. The next night a detective visited her, and the following morning she went to the police station and told her story to Detective Claytor, a member of the Harrisonburg City Police Department. Detective Claytor showed her photographs of possible suspects, and she identified petitioner and Henderson "with absolute certainty" but stated that she had a slight reservation about her identification of the blonde woman. <i>Id.,</i> at 56.</p>
<p>At trial, Stoltzfus testified that, at about 6 p.m. on January 5, she and her 14-year-old daughter were in the Music Land store in the mall looking for a compact disc. While she was waiting for assistance from a clerk, petitioner, whom she described as "Mountain Man," and the blonde girl entered.<sup>[5]</sup><span class="star-pagination">*271</span> Because petitioner was "revved up" and "very impatient," she was frightened and backed up, bumping into Henderson (whom she called "Shy Guy"), and thought she felt something hard in the pocket of his coat. <i>Id.,</i> at 36-37.</p>
<p>Stoltzfus left the store, intending to return later. At about 6:45, while heading back toward Music Land, she again encountered the threesome: "Shy Guy" walking by himself, followed by the girl, and then "Mountain Man" yelling "Donna, Donna, Donna." The girl bumped into Stoltzfus and then asked for directions to the bus stop.<sup>[6]</sup> The three then left.</p>
<p>At first Stoltzfus tried to follow them because of her concern about petitioner's behavior, but she "lost him" and then headed back to Music Land. The clerk had not returned, so she and her daughter went to their car. While driving to another store, they saw a shiny dark blue car. The driver was "beautiful," "well dressed and she was happy, she was singing . . . ." <i>Id.,</i> at 41. When the blue car was stopped behind a minivan at a stop sign, Stoltzfus saw petitioner for the third time.</p>
<p>She testified:</p>
<blockquote>"`Mountain Man' came tearing out of the Mall entrance door and went up to the driver of the van and . . . was just really mad and ran back and banged on back of the backside of the van and then went back to the Mall entrance wall where `Shy Guy' and `Blonde Girl' was standing . . . . [T]hen we left [and before the van and a white pickup truck could turn] `Mountain Man' came out again . . . ." <i>Id.,</i> at 42-43.</blockquote>
<p>After first going to the passenger side of the pickup truck, petitioner came back to the black girl's car, "pounded on" the passenger window, shook the car, yanked the door open and jumped in. When he motioned for "Blonde Girl" and "Shy <span class="star-pagination">*272</span> Guy" to get in, the driver stepped on the gas and "just laid on the horn" but she could not go because there were people walking in front of the car. The horn "blew a long time" and petitioner</p>
<blockquote>"started hitting her . . . on the left shoulder, her right shoulder and then it looked like to me that he started hitting her on the head and I was, I just became concerned and upset. So I beeped, honked my horn and then she stopped honking the horn and he stopped hitting her and opened the door again and the `Blonde Girl' got in the back and `Shy Guy' followed and got behind him." <i>Id.,</i> at 44-45.</blockquote>
<p>Stoltzfus pulled her car up parallel to the blue car, got out for a moment, got back in, and leaned over to ask repeatedly if the other driver was "O.K." The driver looked "frozen" and mouthed an inaudible response. Stoltzfus started to drive away and then realized "the only word that it could possibly be, was help." <i>Id.,</i> at 47. The blue car then drove slowly around her, went over the curb with its horn honking, and headed out of the mall. Stoltzfus briefly followed, told her daughter to write the license number on a "3x4 [inch] index card,"<sup>[7]</sup> and then left for home because she had an empty gas tank and "three kids at home waiting for supper." <i>Id.,</i> at 48-49.</p>
<p>At trial Stoltzfus identified Whitlock from a picture as the driver of the car and pointed to petitioner as "Mountain Man." When asked if pretrial publicity about the murder had influenced her identification, Stoltzfus replied "absolutely not." She explained:</p>
<blockquote>"[F]irst of all, I have an exceptionally good memory. I had very close contact with [petitioner] and he made an <span class="star-pagination">*273</span> emotional impression with me because of his behavior and I, he caught my attention and I paid attention. So I have absolutely no doubt of my identification." <i>Id.,</i>  at 58.</blockquote>
<p>The Commonwealth did not produce any other witnesses to the abduction. Stoltzfus' daughter did not testify.</p>
<p><i>The Stoltzfus Documents</i> </p>
<p>The materials that provide the basis of petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim consist of notes taken by Detective Claytor during his interviews with Stoltzfus, and letters written by Stoltzfus to Claytor. They cast serious doubt on Stoltzfus' confident assertion of her "exceptionally good memory." Because the content of the documents is critical to petitioner's procedural and substantive claims, we summarize their content.</p>
<p>Exhibit 1<sup>[8]</sup> is a handwritten note prepared by Detective Claytor after his first interview with Stoltzfus on January 19, 1990, just two weeks after the crime. The note indicates that she could not identify the black female victim. The only person Stoltzfus apparently could identify at this time was the white female. <i>Id.,</i> at 306.</p>
<p>Exhibit 2 is a document prepared by Detective Claytor some time after February 1. It contains a summary of his interviews with Stoltzfus conducted on January 19 and January 20, 1990.<sup>[9]</sup> At that time "she was not sure whether she could identify the white males but felt sure she could identify the white female."</p>
<p><span class="star-pagination">*274</span> Exhibit 3 is entitled "Observations" and includes a summary of the abduction.</p>
<p>Exhibit 4 is a letter written by Stoltzfus to Claytor three days after their first interview "to clarify some of my confusion for you." The letter states that she had not remembered being at the mall, but that her daughter had helped jog her memory. Her description of the abduction includes the comment: "I have a very vague memory that I'm not sure of. It seems as if the wild guy that I saw had come running through the door and up to a bus as the bus was pulling off. . . . Then the guy I saw came running up to the black girl's window. Were those 2 memories the same person?" <i>Id.,</i> at 316. In a postscript she noted that her daughter "doesn't remember seeing the 3 people get into the black girl's car . . . ." <i>Ibid.</i> </p>
<p>Exhibit 5 is a note to Claytor captioned "My Impressions of `The Car,' " which contains three paragraphs describing the size of the car and comparing it with Stoltzfus' Volkswagen Rabbit, but not mentioning the license plate number that she vividly recalled at the trial. <i>Id.,</i> at 317-318.</p>
<p>Exhibit 6 is a brief note from Stoltzfus to Claytor dated January 25, 1990, stating that after spending several hours with John Dean, Whitlock's boyfriend, "looking at current photos," she had identified Whitlock "beyond a shadow of a doubt."<sup>[10]</sup><i>Id.,</i> at 318. The District Court noted that by the time of trial her identification had been expanded to include a description of her clothing and her appearance as a college kid who was "singing" and "happy." <i>Id.,</i> at 387-388.</p>
<p>Exhibit 7 is a letter from Stoltzfus to Detective Claytor, dated January 16, 1990, in which she thanks him for his "patience with my sometimes muddled memories." She states that if the student at school had not called the police, "I never would have made any of the associations that you helped me make." <i>Id.,</i> at 321.</p>
<p><span class="star-pagination">*275</span> In Exhibit 8, which is undated and summarizes the events described in her trial testimony, Stoltzfus commented:</p>
<blockquote>"So where is the 3x4 card? . . . It would have been very nice if I could have remembered all this at the time and had simply gone to the police with the information. But I totally wrote this off as a trivial episode of college kids carrying on and proceeded with my own full-time college load at JMU. . . . Monday, January 15th. I was cleaning out my car and found the 3x4 card. I tore it into little pieces and put it in the bottom of a trash bag." <i>Id.,</i> at 326.</blockquote>
<p>There is a dispute between the parties over whether petitioner's counsel saw Exhibits 2, 7, and 8 before trial. The prosecuting attorney conceded that he himself never saw Exhibits 1, 3, 4, 5, and 6 until long after petitioner's trial, and they were not in the file he made available to petitioner.<sup>[11]</sup> For purposes of this case, therefore, we assume that petitioner proceeded to trial without having seen Exhibits 1, 3, 4, 5, and 6.<sup>[12]</sup></p>
<p><span class="star-pagination">*276</span> <i>State Proceedings</i> </p>
<p>Petitioner was tried in Augusta County, where Whitlock's body was found, on charges of capital murder, robbery, and abduction. Because the prosecutor maintained an open file policy, which gave petitioner's counsel access to all of the evidence in the Augusta County prosecutor's files,<sup>[13]</sup> petitioner's counsel did not file a pretrial motion for discovery of possible exculpatory evidence.<sup>[14]</sup> In closing argument, petitioner's lawyer effectively conceded that the evidence was sufficient to support the robbery and abduction charges, as well as the lesser offense of first-degree murder, but argued that the evidence was insufficient to prove that petitioner was guilty of capital murder. <i>Id.,</i> at 192-193.</p>
<p>The judge instructed the jury that petitioner could be found guilty of the capital charge if the evidence established beyond a reasonable doubt that he "jointly participated in the fatal beating" and "was an active and immediate participant <span class="star-pagination">*277</span> in the act or acts that caused the victim's death." <i>Id.,</i>  at 160-161. The jury found petitioner guilty of abduction, robbery, and capital murder. <i>Id.,</i> at 200-201. After listening to testimony and arguments presented during the sentencing phase, the jury made findings of "vileness" and "future dangerousness," and unanimously recommended the death sentence that the judge later imposed.</p>
<p>The Virginia Supreme Court affirmed the conviction and sentence. <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">241 Va. 482</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d 227</a></span> (1991). It held that the trial court had properly instructed the jury on the "joint perpetrator" theory of capital murder and that the evidence, viewed most favorably in support of the verdict, amply supported the prosecution's theory that both petitioner and Henderson were active participants in the actual killing.<sup>[15]</sup></p>
<p>In December 1991, the Augusta County Circuit Court appointed new counsel to represent petitioner in state habeas corpus proceedings. State habeas counsel advanced an <span class="star-pagination">*278</span> ineffective-assistance-of-counsel claim based, in part, on trial counsel's failure to file a motion under <i>Brady</i> v. <i>Maryland,</i>  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), "to have the Commonwealth disclose to the defense all exculpatory evidence known to itor in its possession." App. 205-206. In answer to that claim, the Commonwealth asserted that such a motion was unnecessary because the prosecutor had maintained an open file policy.<sup>[16]</sup> The Circuit Court dismissed the petition, and the State Supreme Court affirmed. <i>Strickler</i> v. <i>Murray,</i> <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">249 Va. 120</a></span>, <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">452 S. E. 2d 648</a></span> (1995).</p>
<p><i>Federal Habeas Corpus Proceedings</i> </p>
<p>In March 1996, petitioner filed a federal habeas corpus petition in the Eastern District of Virginia. The District Court entered a sealed, <i>ex parte</i> order granting petitioner's counsel the right to examine and to copy all of the police and prosecution files in the case. Record, Doc. No. 20. That order led to petitioner's counsel's first examination of the Stoltzfus materials, described <i>supra,</i> at 273-275.</p>
<p>Based on the discovery of those exhibits, petitioner for the first time raised a direct claim that his conviction was invalid because the prosecution had failed to comply with the rule of <i>Brady</i> v. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span></i><i>.</i> The District Court granted the Commonwealth's motion to dismiss all claims except for petitioner's contention that the Commonwealth violated <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i>  that he received ineffective assistance of counsel,<sup>[17]</sup> and that he was denied due process of law under the Fifth and Fourteenth Amendments. In its order denying the Commonwealth's motion to dismiss, the District Court found that petitioner had "demonstrated cause for his failure to raise this claim earlier [because] [d]efense counsel had no independent access to this material and the Commonwealth repeatedly withheld it throughout Petitioner's state habeas proceeding." App. 287.</p>
<p><span class="star-pagination">*279</span> After reviewing the Stoltzfus materials, and making the assumption that the three disputed exhibits had been available to the defense, the District Court concluded that the failure to disclose the other five was sufficiently prejudicial to undermine confidence in the jury's verdict. <i>Id.,</i> at 396. It granted summary judgment to petitioner and granted the writ.</p>
<p>The Court of Appeals vacated in part and remanded. It held that petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was procedurally defaulted because the factual basis for the claim was available to him at the time he filed his state habeas petition. Given that he knew that Stoltzfus had been interviewed by Harrisonburg police officers, the court opined that "reasonably competent counsel would have sought discovery in state court" of the police files, and that in response to this "simple request, it is likely the state court would have ordered the production of the files." App. 421. Therefore, the Court of Appeals reasoned, it could not address the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim unless petitioner could demonstrate both cause and actual prejudice.</p>
<p>Under Fourth Circuit precedent a party "cannot establish cause to excuse his default if he should have known of such claims through the exercise of reasonable diligence." App. 423 (citing <i>Stockton</i> v. <i>Murray,</i> <span class="citation" data-id="683528"><a href="/opinion/683528/dennis-waldon-stockton-v-edward-murray/#925" aria-description="Citation for case: Dennis Waldon Stockton v. Edward Murray">41 F. 3d 920, 925</a></span> (1994)). Having already decided that the claim was available to reasonably competent counsel, the Fourth Circuit stated that the basis for finding procedural default also foreclosed a finding of cause. Moreover, the Court of Appeals reasoned, petitioner could not fault his trial lawyers' failure to make a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim because they reasonably relied on the prosecutor's open file policy. App. 423-424.<sup>[18]</sup></p>
<p>As an alternative basis for decision, the Court of Appeals also held that petitioner could not establish prejudice because <span class="star-pagination">*280</span> "the Stoltzfus materials would have provided little or no help .. . in either the guilt or sentencing phases of the trial." <i>Id.,</i> at 425. With respect to guilt, the court noted that Stoltzfus' testimony was not relevant to petitioner's argument that he was only guilty of first-degree murder rather than capital murder because Henderson, rather than he, actually killed Whitlock. With respect to sentencing, the court concluded that her testimony "was of no import" because the findings of future dangerousness and vileness rested on other evidence. Finally, the court noted that even if it could get beyond the procedural default, the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim would fail on the merits because of the absence of prejudice. App. 425, n. 11. The Court of Appeals, therefore, reversed the District Court's judgment and remanded the case with instructions to dismiss the petition.</p>
<p></p>
<h2>II</h2>
<p>The first question that our order granting certiorari directed the parties to address is whether the Commonwealth violated the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule. We begin our analysis by identifying the essential components of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation.</p>
<p>In <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> this Court held "that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. We have since held that the duty to disclose such evidence is applicable even though there has been no request by the accused, <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#107" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 107</a></span> (1976), and that the duty encompasses impeachment evidence as well as exculpatory evidence, <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 676</a></span> (1985). Such evidence is material "if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different." <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley"><i>Id.,</i> at 682</a></span>; see also <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#433" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 433-434</a></span> (1995). Moreover, the rule encompasses evidence "known only to police <span class="star-pagination">*281</span> investigators and not to the prosecutor." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#438" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 438</a></span>. In order to comply with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> therefore, "the individual prosecutor has a duty to learn of any favorable evidence known to the others acting on the government's behalf in this case, including the police." <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 437</a></span>.</p>
<p>These cases, together with earlier cases condemning the knowing use of perjured testimony,<sup>[19]</sup> illustrate the special role played by the American prosecutor in the search for truth in criminal trials. Within the federal system, for example, we have said that the United States Attorney is "the representative not of an ordinary party to a controversy, but of a sovereignty whose obligation to govern impartially is as compelling as its obligation to govern at all; and whose interest, therefore, in a criminal prosecution is not that it shall win a case, but that justice shall be done." <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935).</p>
<p>This special status explains both the basis for the prosecution's broad duty of disclosure and our conclusion that not every violation of that duty necessarily establishes that the outcome was unjust. Thus the term "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation" is sometimes used to refer to any breach of the broad obligation to disclose exculpatory evidence<sup>[20]</sup>that is, to any suppression of so-called "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> material"although, strictly speaking, there is never a real "<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation" unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict. There are three components of a true <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  violation: The evidence at issue must be favorable to the accused, <span class="star-pagination">*282</span> either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued.</p>
<p>Two of those components are unquestionably established by the record in this case. The contrast between (a) the terrifying incident that Stoltzfus confidently described in her testimony and (b) her initial perception of that event "as a trivial episode of college kids carrying on" that her daughter did not even notice, suffices to establish the impeaching character of the undisclosed documents.<sup>[21]</sup> Moreover, with respect to at least five of those documents, there is no dispute about the fact that they were known to the Commonwealth but not disclosed to trial counsel. It is the third componentwhether petitioner has established the prejudice necessary to satisfy the "materiality" inquirythat is the most difficult element of the claimed <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation in this case.</p>
<p>Because petitioner acknowledges that his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim is procedurally defaulted, we must first decide whether that default is excused by an adequate showing of cause and prejudice. In this case, cause and prejudice parallel two of the three components of the alleged <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation itself. The suppression of the Stoltzfus documents constitutes one of the causes for the failure to assert a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in the state courts, and unless those documents were "material" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes, their suppression did not give rise to sufficient prejudice to overcome the procedural default.</p>
<p></p>
<h2>III</h2>
<p>Respondent expressly disavows any reliance on the fact that petitioner's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was not raised at trial. Brief <span class="star-pagination">*283</span> for Respondent 17-18, n. 6. He states that the Commonwealth has consistently argued "that the claim is defaulted because it could have been raised on state habeas corpus through the exercise of due diligence, but was not." <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Ibid.</a></span></i>  Despite this concession, it is appropriate to begin the analysis of the "cause" issue by explaining why petitioner's reasons for failing to raise his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim at trial are acceptable under this Court's cases.</p>
<p>Three factors explain why trial counsel did not advance this claim: The documents were suppressed by the Commonwealth; the prosecutor maintained an open file policy;<sup>[22]</sup> and trial counsel were not aware of the factual basis for the claim. The first and second factors<i>i. e.,</i> the nondisclosure and the open file policyare both fairly characterized as conduct attributable to the Commonwealth that impeded trial counsel's access to the factual basis for making a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim.<sup>[23]</sup> As we explained in <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S. 478, 488</a></span> (1986), it is just such factors that ordinarily establish the existence of cause for a procedural default.<sup>[24]</sup></p>
<p><span class="star-pagination">*284</span> If it was reasonable for trial counsel to rely on, not just the presumption that the prosecutor would fully perform his duty to disclose all exculpatory materials, but also the implicit representation that such materials would be included in the open files tendered to defense counsel for their examination, we think such reliance by counsel appointed to represent petitioner in state habeas proceedings was equally reasonable. Indeed, in <i>Murray</i> we expressly noted that "the standard for cause should not vary depending on the timing of a procedural default." <i>Id.,</i> at 491.</p>
<p>Respondent contends, however, that the prosecution's maintenance of an open file policy that did not include all it was purported to contain is irrelevant because the factual basis for the assertion of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim was available to state habeas counsel. He presses two factors to support this assertion. First, he argues that an examination of Stoltzfus' trial testimony,<sup>[25]</sup> as well as a letter published in a local newspaper,<sup>[26]</sup> made it clear that she had had several interviews with Detective Claytor. Second, the fact that the Federal District Court entered an order allowing discovery of the Harrisonburg police files indicates that diligent counsel could <span class="star-pagination">*285</span> have obtained a similar order from the state court. We find neither factor persuasive.</p>
<p>Although it is true that petitioner's lawyersboth at trial and in post-trial proceedingsmust have known that Stoltzfus had had multiple interviews with the police, it by no means follows that they would have known that records pertaining to those interviews, or that the notes that Stoltzfus sent to the detective, existed and had been suppressed.<sup>[27]</sup> Indeed, if respondent is correct that Exhibits 2, 7, and 8 were in the prosecutor's "open file," it is especially unlikely that counsel would have suspected that additional impeaching evidence was being withheld. The prosecutor must have known about the newspaper articles and Stoltzfus' meetings with Claytor, yet he did not believe that his prosecution file was incomplete.</p>
<p>Furthermore, the fact that the District Court entered a broad discovery order even before federal habeas counsel had advanced a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim does not demonstrate that a state court also would have done so.<sup>[28]</sup> Indeed, as we understand Virginia law and respondent's position, petitioner would not have been entitled to such discovery in state habeas <span class="star-pagination">*286</span> proceedings without a showing of good cause.<sup>[29]</sup> Even pursuant to the broader discovery provisions afforded at trial, petitioner would not have had access to these materials under Virginia law, except as modified by <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[30]</sup> Mere speculation that some exculpatory material may have been withheld is unlikely to establish good cause for a discovery request on collateral review. Nor, in our opinion, should such suspicion suffice to impose a duty on counsel to advance a claim for which they have no evidentiary support. Proper respect for state procedures counsels against a requirement that all possible claims be raised in state collateral proceedings, even when no known facts support them. The presumption, well established by "`tradition and experience,' " that prosecutors have fully "`discharged their official duties,' " <i>United States</i> v. <i>Mezzanatto,</i> <span class="citation" data-id="117889"><a href="/opinion/117889/united-states-v-mezzanatto/#210" aria-description="Citation for case: United States v. Mezzanatto">513 U. S. 196, 210</a></span> (1995), is inconsistent with the novel suggestion that conscientious defense counsel have a procedural obligation to assert constitutional <span class="star-pagination">*287</span> error on the basis of mere suspicion that some prosecutorial misstep may have occurred.</p>
<p>Respondent's position on the "cause" issue is particularly weak in this case because the state habeas proceedings confirmed petitioner's justification for his failure to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. As already noted, when he alleged that trial counsel had been incompetent because they had not advanced such a claim, the warden responded by pointing out that there was no need for counsel to do so because they "were voluntarily given full disclosure of everything known to the government."<sup>[31]</sup> Given that representation, petitioner had no basis for believing the Commonwealth had failed to comply with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> at trial.<sup>[32]</sup></p>
<p>Respondent also argues that our decisions in <i>Gray</i> v. <i>Netherland,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/" aria-description="Citation for case: Gray v. Netherland">518 U. S. 152</a></span> (1996), and <i>McCleskey</i> v. <i>Zant,</i> <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">499 U. S. 467</a></span> (1991), preclude the conclusion that the cause for petitioner's default was adequate. In both of those cases, however, the petitioner was previously aware of the factual basis for his claim but failed to raise it earlier. See <i>Gray,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#161" aria-description="Citation for case: Gray v. Netherland">518 U. S., at 161</a></span>; <i>McCleskey,</i> <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/#498" aria-description="Citation for case: McCleskey v. Zant">499 U. S., at 498-499</a></span>. In the context of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, a defendant cannot conduct the "reasonable <span class="star-pagination">*288</span> and diligent investigation" mandated by <i><span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">McCleskey</a></span></i>  to preclude a finding of procedural default when the evidence is in the hands of the State.<sup>[33]</sup></p>
<p>The controlling precedents on "cause" are <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S., at 488</a></span>, and <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214</a></span> (1988). As we explained in the latter case:</p>
<blockquote>"If the District Attorney's memorandum was not reasonably discoverable because it was concealed by Putnam County officials, and if that concealment, rather than tactical considerations, was the reason for the failure of petitioner's lawyers to raise the jury challenge in the trial court, then petitioner established ample cause to excuse his procedural default under this Court's precedents." <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#222" aria-description="Citation for case: Amadeo v. Zant"><i>Id.,</i> at 222</a></span>.<sup>[34]</sup></blockquote>
<p>There is no suggestion that tactical considerations played any role in petitioner's failure to raise his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state court. Moreover, under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> an inadvertent nondisclosure has the same impact on the fairness of the proceedings as deliberate concealment. "If the suppression of evidence results in constitutional error, it is because of the character of the evidence, not the character of the prosecutor." <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#110" aria-description="Citation for case: United States v. Agurs">427 U. S., at 110</a></span>.</p>
<p><span class="star-pagination">*289</span> In summary, petitioner has established cause for failing to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim prior to federal habeas because (a) the prosecution withheld exculpatory evidence; (b) petitioner reasonably relied on the prosecution's open file policy as fulfilling the prosecution's duty to disclose such evidence; and (c) the Commonwealth confirmed petitioner's reliance on the open file policy by asserting during state habeas proceedings that petitioner had already received "everything known to the government."<sup>[35]</sup> We need not decide in this case whether any one or two of these factors would be sufficient to constitute cause, since the combination of all three surely suffices.</p>
<p></p>
<h2>IV</h2>
<p>The differing judgments of the District Court and the Court of Appeals attest to the difficulty of resolving the issue of prejudice. Unlike the Fourth Circuit, we do not believe that "the Stolzfus <i>[sic]</i> materials would have provided little or no help to Strickler in either the guilt or sentencing phases of the trial." App. 425. Without a doubt, Stoltzfus' testimony was prejudicial in the sense that it made petitioner's conviction more likely than if she had not testified, and discrediting her testimony might have changed the outcome of the trial.</p>
<p>That, however, is not the standard that petitioner must satisfy in order to obtain relief. He must convince us that "there is a reasonable probability" that the result of the trial would have been different if the suppressed documents had been disclosed to the defense. As we stressed in <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span>:</i>  "[T]he adjective is important. The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in its absence <span class="star-pagination">*290</span> he received a fair trial, understood as a trial resulting in a verdict worthy of confidence." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span>.</p>
<p>The Court of Appeals' negative answer to that question rested on its conclusion that, without considering Stoltzfus' testimony, the record contained ample, independent evidence of guilt, as well as evidence sufficient to support the findings of vileness and future dangerousness that warranted the imposition of the death penalty. The standard used by that court was incorrect. As we made clear in <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span>,</i> the materiality inquiry is not just a matter of determining whether, after discounting the inculpatory evidence in light of the undisclosed evidence, the remaining evidence is sufficient to support the jury's conclusions. <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 434-435</a></span>. Rather, the question is whether "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Id.,</i> at 435</a></span>.</p>
<p>The District Judge decided not to hold an evidentiary hearing to determine whether Exhibits 2, 7, and 8 had been disclosed to the defense, because he was satisfied that the "potentially devastating impeachment material" contained in the other five warranted the entry of summary judgment in petitioner's favor. App. 392. The District Court's conclusion that the admittedly undisclosed documents were sufficiently important to establish a violation of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> rule was supported by the prosecutor's closing argument. That argument relied on Stoltzfus' testimony to demonstrate petitioner's violent propensities and to establish that he was the instigator and leader in Whitlock's abduction and, by inference, her murder. The prosecutor emphasized the importance of Stoltzfus' testimony in proving the abduction:</p>
<blockquote>"[W]e are lucky enough to have an eyewitness who saw [what] happened out there in that parking lot. [In a] lot of cases you don't. A lot of cases you can just theorize what happened in the actual abduction. But Mrs. Stoltzfus was there, she saw [what] happened." App. 169.</blockquote>
<p><span class="star-pagination">*291</span> Given the record evidence involving Henderson,<sup>[36]</sup> the District Court concluded that, without Stoltzfus' testimony, the jury might have been persuaded that Henderson, rather than petitioner, was the ringleader. He reasoned that a "reasonable probability of conviction" of first-degree, rather than capital, murder sufficed to establish the materiality of the undisclosed Stoltzfus materials and, thus, a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation. App. 396.</p>
<p>The District Court was surely correct that there is a reasonable <i>possibility</i> that either a total, or just a substantial, discount of Stoltzfus' testimony might have produced a different result, either at the guilt or sentencing phases. Petitioner did, for example, introduce substantial mitigating evidence about abuse he had suffered as a child at the hands of his stepfather.<sup>[37]</sup> As the District Court recognized, however, petitioner's burden is to establish a reasonable <i>probability</i>  of a different result. <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span>.</p>
<p><span class="star-pagination">*292</span> Even if Stoltzfus and her testimony had been entirely discredited, the jury might still have concluded that petitioner was the leader of the criminal enterprise because he was the one seen driving the car by Kurt Massie near the location of the murder and the one who kept the car for the following week.<sup>[38]</sup> In addition, Tudor testified that petitioner threatened Henderson with a knife later in the evening.</p>
<p>More importantly, however, petitioner's guilt of capital murder did not depend on proof that he was the dominant partner: Proof that he was an equal participant with Henderson was sufficient under the judge's instructions.<sup>[39]</sup> Accordingly, the strong evidence that Henderson was a killer is entirely consistent with the conclusion that petitioner was also an actual participant in the killing.<sup>[40]</sup></p>
<p><span class="star-pagination">*293</span> Furthermore, there was considerable forensic and other physical evidence linking petitioner to the crime.<sup>[41]</sup> The weight and size of the rock,<sup>[42]</sup> and the character of the fatal injuries to the victim,<sup>[43]</sup> are powerful evidence supporting the conclusion that two people acted jointly to commit a brutal murder.</p>
<p>We recognize the importance of eyewitness testimony; Stoltzfus provided the only disinterested, narrative account of what transpired on January 5, 1990. However, Stoltzfus' vivid description of the events at the mall was not the only evidence that the jury had before it. Two other eyewitnesses, <span class="star-pagination">*294</span> the security guard and Henderson's friend, placed petitioner and Henderson at the Harrisonburg Valley Shopping Mall on the afternoon of Whitlock's murder. One eyewitness later saw petitioner driving Dean's car near the scene of the murder.</p>
<p>The record provides strong support for the conclusion that petitioner would have been convicted of capital murder and sentenced to death, even if Stoltzfus had been severely impeached. The jury was instructed on two predicates for capital murder: robbery with a deadly weapon and abduction with intent to defile.<sup>[44]</sup> On state habeas, the Virginia Supreme Court rejected as procedurally barred petitioner's challenge to this jury instruction on the ground that "abduction with intent to defile" was not a predicate for capital murder for a victim over the age of 12.<sup>[45]</sup> That issue is not before us. Even assuming, however, that this predicate was erroneous, armed robbery still would have supported the capital murder conviction.</p>
<p>Petitioner argues that the prosecution's evidence on armed robbery "flowed almost entirely from inferences from Stoltzfus' testimony," and especially from her statement that Henderson had a "hard object" under his coat at the mall. Brief for Petitioner 35. That argument, however, ignores the fact that petitioner's mother and Tudor provided direct evidence that petitioner had a knife with him on the day of the crime. <span class="star-pagination">*295</span> In addition, the prosecution contended in its closing argument that the rocknot the knifewas the murder weapon.<sup>[46]</sup> The prosecution did advance the theory that petitioner had a knife when he got in the car with Whitlock, but it did not specifically argue that petitioner used the knife during the robbery.<sup>[47]</sup></p>
<p>Petitioner also maintains that he suffered prejudice from the failure to disclose the Stoltzfus documents because her testimony impacted on the jury's decision to impose the death penalty. Her testimony, however, did not relate to his eligibility for the death sentence and was not relied upon by the prosecution at all during its closing argument at the penalty phase.<sup>[48]</sup> With respect to the jury's discretionary decision to impose the death penalty, it is true that Stoltzfus described petitioner as a violent, aggressive person, but that portrayal surely was not as damaging as either the evidence that he spent the evening of the murder dancing and drinking at Dice's or the powerful message conveyed by the 69pound <span class="star-pagination">*296</span> rock that was part of the record before the jury. Notwithstanding the obvious significance of Stoltzfus' testimony, petitioner has not convinced us that there is a reasonable probability that the jury would have returned a different verdict if her testimony had been either severely impeached or excluded entirely.</p>
<p>Petitioner has satisfied two of the three components of a constitutional violation under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>:</i> exculpatory evidence and nondisclosure of this evidence by the prosecution. Petitioner has also demonstrated cause for failing to raise this claim during trial or on state postconviction review. However, petitioner has not shown that there is a reasonable probability that his conviction or sentence would have been different had these materials been disclosed. He therefore cannot show materiality under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> or prejudice from his failure to raise the claim earlier. Accordingly, the judgment of the Court of Appeals is <i>Affirmed.</i>  Justice Souter, with whom Justice Kennedy joins as to Part II, concurring in part and dissenting in part.</p>
<p>I look at this case much as the Court does, starting with its view in Part III (which I join) that Strickler has shown cause to excuse the procedural default of his <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. Like the Court, I think it clear that the materials withheld were exculpatory as devastating ammunition for impeaching Stoltzfus.<sup>[1]</sup> See <i>ante,</i> at 282. Even on the question of prejudice <span class="star-pagination">*297</span> or materiality,<sup>[2]</sup> over which I ultimately part company with the majority, I am persuaded that Strickler has failed to establish a reasonable probability that, had the materials withheld been disclosed, he would not have been found guilty of capital murder. See <i>ante,</i> at 292-296. As the Court says, however, the prejudice enquiry does not stop at the conviction but goes to each step of the sentencing process: the jury's consideration of aggravating, death-qualifying facts, the jury's discretionary recommendation of a death sentence if it finds the requisite aggravating factors, and the judge's discretionary decision to follow the jury's recommendation. See <i>ante,</i> at 294-296. It is with respect to the penultimate step in determining the sentence that I think Strickler has carried his burden. I believe there is a reasonable probability (which I take to mean a significant possibility) that disclosure of the Stoltzfus materials would have led the jury to recommend life, not death, and I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>Before I get to the analysis of prejudice I should say something about the standard for identifying it, and about the unfortunate phrasing of the shorthand version in which the standard is customarily couched. The Court speaks in terms of the familiar, and perhaps familiarly deceptive, formulation: whether there is a "reasonable probability" of a different outcome if the evidence withheld had been disclosed. The Court rightly cautions that the standard intended <span class="star-pagination">*298</span> by these words does not require defendants to show that a different outcome would have been more likely than not with the suppressed evidence, let alone that without the materials withheld the evidence would have been insufficient to support the result reached. See <i>ante,</i> at 289-290; <i>Kyles</i>  v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 434-435</a></span> (1995). Instead, the Court restates the question (as I have done elsewhere) as whether "`the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence' " in the outcome. <i>Ante,</i> at 290 (quoting <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 435</a></span>).</p>
<p>Despite our repeated explanation of the shorthand formulation in these words, the continued use of the term "probability" raises an unjustifiable risk of misleading courts into treating it as akin to the more demanding standard, "more likely than not." While any short phrases for what the cases are getting at will be "inevitably imprecise," <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#108" aria-description="Citation for case: United States v. Agurs">427 U. S. 97, 108</a></span> (1976), I think "significant possibility" would do better at capturing the degree to which the undisclosed evidence would place the actual result in question, sufficient to warrant overturning a conviction or sentence.</p>
<p>To see that this is so, we need to recall <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> `s evolution since the appearance of the rule as originally stated, that "suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963). <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> itself did not explain what it meant by "material" (perhaps assuming the term would be given its usual meaning in the law of evidence, see <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#703" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 703, n. 5</a></span> (1985) (Marshall, J., dissenting)). We first essayed a partial definition in <i>United States</i> v. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs, supra</a></span></i><i>,</i> where we identified three situations arguably within the ambit of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and said that in the first, involving knowing use of perjured testimony, <span class="star-pagination">*299</span> reversal was required if there was "any reasonable likelihood" that the false testimony had affected the verdict. <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs, supra,</a></span></i> at 103 (citing <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 154</a></span> (1972), in turn quoting <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 271</a></span> (1959)). We have treated "reasonable likelihood" as synonymous with "reasonable possibility" and thus have equated materiality in the perjured-testimony cases with a showing that suppression of the evidence was not harmless beyond a reasonable doubt. <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley"><i>Bagley, supra,</i> at 678-680</a></span>, and n. 9 (opinion of Blackmun, J.). See also <i>Brecht</i> v. <i>Abrahamson,</i> <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#637" aria-description="Citation for case: Brecht v. Abrahamson">507 U. S. 619, 637</a></span> (1993) (defining harmless-beyond-areasonable-doubt standard as no "`reasonable possibility' that trial error contributed to the verdict"); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 24</a></span> (1967) (same). In <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>,</i> we thought a less demanding standard appropriate when the prosecution fails to turn over materials in the absence of a specific request. Although we refrained from attaching a label to that standard, we explained it as falling between the more-likely-than-not level and yet another criterion, whether the reviewing court's "`conviction [was] sure that the error did not influence the jury, or had but very slight effect.' " <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span> (quoting <i>Kotteakos</i> v. <i>United States,</i> <span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/#764" aria-description="Citation for case: Kotteakos v. United States">328 U. S. 750, 764</a></span> (1946)). Finally, in <i>United States</i> v. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley, supra</a></span></i><i>,</i> we embraced "reasonable probability" as the appropriate standard to judge the materiality of information withheld by the prosecution whether or not the defense had asked first. <i><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">Bagley</a></span></i> took that phrase from <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668, 694</a></span> (1984), where it had been used for the level of prejudice needed to make out a claim of constitutionally ineffective assistance of counsel. <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span></i> in turn cited two cases for its formulation, <i><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span></i> (which did not contain the expression "reasonable probability") and <i>United States</i> v. <i>Valenzuela-Bernal,</i> <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#873" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 873-874</a></span> (1982) (which held that sanctions against the Government for deportation of a potential defense witness were appropriate only <span class="star-pagination">*300</span> if there was a "reasonable likelihood" that the lost testimony "could have affected the judgment of the trier of fact").</p>
<p>The circuitous path by which the Court came to adopt "reasonable probability" of a different result as the rule of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> materiality suggests several things. First, while "reasonable possibility" or "reasonable likelihood," the <i><span class="citation" data-id="104321"><a href="/opinion/104321/kotteakos-v-united-states/" aria-description="Citation for case: Kotteakos v. United States">Kotteakos</a></span></i> standard, and "reasonable probability" express distinct levels of confidence concerning the hypothetical effects of errors on decisionmakers' reasoning, the differences among the standards are slight. Second, the gap between all three of those formulations and "more likely than not" is greater than any differences among them. Third, because of that larger gap, it is misleading in <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> cases to use the term "probability," which is naturally read as the cognate of "probably" and thus confused with "more likely than not," see <i>Morris</i> v. <i>Mathews,</i> <span class="citation" data-id="9430368"><a href="/opinion/111606/morris-v-mathews/#247" aria-description="Citation for case: Morris v. Mathews">475 U. S. 237, 247</a></span> (1986) (apparently treating "reasonable probability" as synonymous with "probably"); <span class="citation" data-id="9430368"><a href="/opinion/111606/morris-v-mathews/#254" aria-description="Citation for case: Morris v. Mathews"><i>id.,</i> at 254, n. 3</a></span> (Blackmun, J., concurring in judgment) (cautioning against confusing "reasonable probability" with more likely than not). We would be better off speaking of a "significant possibility" of a different result to characterize the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> materiality standard. Even then, given the soft edges of all these phrases,<sup>[3]</sup> the touchstone of the enquiry <span class="star-pagination">*301</span> must remain whether the evidentiary suppression "undermines our confidence" that the factfinder would have reached the same result.</p>
<p></p>
<h2>II</h2>
<p>Even keeping in mind these caveats about the appropriate level of materiality, applying the standard to the facts of this case does not give the Court easy answers, as the Court candidly acknowledges. See <i>ante,</i> at 289. Indeed, the Court concedes that discrediting Stoltzfus's testimony "might have changed the outcome of the trial," <i>ibid.,</i> and that the District Court was "surely correct" to find a "reasonable <i>possibility</i>  that either a total, or just a substantial, discount of Stoltzfus' testimony might have produced a different result, either at the guilt or sentencing phases," <i>ante,</i> at 291.</p>
<p>In the end, however, the Court finds the undisclosed evidence inadequate to undermine confidence in the jury's sentencing <span class="star-pagination">*302</span> recommendation, whereas I find it sufficient to do that. Since we apply the same standard to the same record, our differing conclusions largely reflect different assessments of the significance the jurors probably ascribed to the Stoltzfus testimony. My assessment turns on two points. First, I believe that in making the ultimate judgment about what should be done to one of several participants in a crime this appalling the jurors would very likely have given weight to the degree of initiative and leadership exercised by that particular defendant. Second, I believe that no other testimony comes close to the prominence and force of Stoltzfus's account in showing Strickler as the unquestionably dominant member of the trio involved in Whitlock's abduction and the aggressive and moving figure behind her murder.</p>
<p>Although Stoltzfus was not the prosecution's first witness, she was the first to describe Strickler in any detail, thus providing the frame for the remainder of the story the prosecution presented to the jury. From the start of Stoltzfus's testimony, Strickler was "Mountain Man" and his male companion "Shy Guy," labels whose repetition more than a dozen times (by the prosecutor as well as by Stoltzfus) must have left the jurors with a clear sense of the relative roles that Strickler and Henderson played in the crimes that followed Stoltzfus's observation. According to her, when she first saw Strickler she "just sort of instinctively backed up because I was frightened." App. 36. Unlike retiring "Shy Guy," Strickler was "revved up." <i>Id.,</i> at 39, 60. Even in describing her first encounter with Strickler inside the mall, Stoltzfus spoke of him as domineering, a "very impatient" character yelling at his female companion, "Blonde Girl," to join him. <i>Id.,</i> at 36, 38-39.</p>
<p>After describing in detail how "Mountain Man" and "Blonde Girl" were dressed, Stoltzfus said that "`Mountain Man' came tearing out of the Mall entrance door and went up to the driver of [a] van and . . . was just really mad and ran back and banged on back of the backside of the van" <span class="star-pagination">*303</span> while "Shy Guy" and "Blonde Girl" hung back. <i>Id.,</i> at 43. "Mountain Man" approached a pickup truck, then "pounded on" the front passenger side window of Whitlock's car, "shook and shook the car door," "banging and banging on the window" while Whitlock checked to see if the door was locked. <i>Ibid.</i> Finally, "he just really shook it hard and you could tell he was mad. Shook it really hard and the door opened and he jumped in . . . and faced her." <i>Id.,</i> at 43-44. While Whitlock tried to push him away, "Mountain Man" "motioned for `Blonde Girl' and `Shy Guy' to come" and the girl did as she was bidden. She "started to jump into the car," but "jumped back" when Whitlock stepped on the gas. <i>Id.,</i> at 44. Then "Mountain Man" started "hitting [Whitlock] on the left shoulder, her right shoulder and then . . . the head," finally "open[ing] the door again" so "the `Blonde Girl' got in the back and `Shy Guy' followed and got behind him." <i>Id.,</i> at 45. "Shy Guy" passed "Mountain Man" his tan coat, which "Mountain Man" "fiddled with" for "what seemed like a long time," then "sat back up and . . . faced" Whitlock while "the other two in the back seat sat back and relaxed." <i>Ibid.</i>  Stoltzfus then claimed that she got out of her car and went over to Whitlock's, whereupon unassertive "Shy Guy" "instinctively jumped, you know, laid over on the seat to hide from me." <i>Id.,</i> at 46. Stoltzfus pulled up next to Whitlock's car and repeatedly asked, "[A]re you O.K.[?]," but Whitlock responded only with eye contact; "she didn't smile, there was no expression," and "[j]ust very serious, looked down to her right," suggesting Strickler was holding a weapon on her. <i>Id.,</i> at 46, 47. Finally, Whitlock mouthed something, which Stoltzfus demonstrated for the jury and then explained she realized must have been the word, "help." <i>Id.,</i> at 47.</p>
<p>Without rejecting the very notion that jurors with discretion in sentencing would be influenced by the relative dominance of one accomplice among others in a shocking crime, I could not regard Stoltzfus's colorful testimony as anything but significant on the matter of sentence. It was Stoltzfus <span class="star-pagination">*304</span> alone who described Strickler as the initiator of the abduction, as the one who broke into Whitlock's car, who beckoned his companions to follow him, and who violently subdued the victim while "Shy Guy" sat in the back seat. The bare content of this testimony, important enough, was enhanced by one of the inherent hallmarks of reliability, as Stoltzfus confidently recalled detail after detail. The withheld documents would have shown, however, that many of the details Stoltzfus confidently mentioned on the stand (such as Strickler's appearance, Whitlock's appearance, the hour of day when the episode occurred, and her daughter's alleged notation of the license plate number of Whitlock's car) had apparently escaped her memory in her initial interviews with the police. Her persuasive account did not come, indeed, until after her recollection had been aided by further conversations with the police and with the victim's boyfriend. I therefore have to assess the likely havoc that an informed cross-examiner could have wreaked upon Stoltzfus as adequate to raise a significant possibility of a different recommendation, as sufficient to undermine confidence that the death recommendation would have been the choice. All it would have taken, after all, was one juror to hold out against death to preclude the recommendation actually given.</p>
<p>The Court does not, of course, deny that evidence of dominant role would probably have been considered by the jury; the Court, instead, doubts that this consideration, and the evidence bearing on it, would have figured so prominently in a juror's mind as to be a fulcrum of confidence. I am not convinced by the Court's reasons.</p>
<p>The Court emphasizes the brutal manner of the killing and Strickler's want of remorse as jury considerations diminishing the relative importance of Strickler's position as ringleader. See <i>ante,</i> at 295-296. Without doubt the jurors considered these to be important factors, and without doubt they may have been treated as sufficient to warrant death. But as the Court says, sufficiency of other evidence and the <span class="star-pagination">*305</span> facts it supports is not the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> standard, and the significance of both brutality and sangfroid must surely have been complemented by a certainty that without Strickler there would have been no abduction and no ensuing murder.</p>
<p>The Court concludes that Stoltzfus's testimony is unlikely to have had significant influence on the jury's sentencing recommendation because the prosecutor made no mention of her testimony in his closing statement at the sentencing proceeding. See <i>ante,</i> at 295. But although the Court is entirely right that the prosecution gave no prominence to the Stoltzfus testimony at the sentencing stage, the Commonwealth's closing actually did include two brief references to Strickler's behavior in "just grabbing a complete stranger and abducting her," 19 Record 919; see also <i>id.,</i> at 904, as relevant to the jury's determination of future dangerousness. And since Strickler's criminal record had no convictions involving actual violence, a point defense counsel stressed in his closing argument, see <i>id.,</i> at 913, the jurors may well have given weight to Stoltzfus's lively portrait of Strickler as the aggressive leader of the group when they came to assess his future dangerousness.</p>
<p>What is more important, common experience, supported by at least one empirical study, see Bowers, Sandys, &amp; Steiner, Foreclosed Impartiality in Capital Sentencing: Jurors' Predispositions, Guilt-Trial Experience, and Premature Decision Making, <span class="citation no-link">83 Cornell L. Rev. 1476</span>, 1486-1496 (1998), tells us that the evidence and arguments presented during the guilt phase of a capital trial will often have a significant effect on the jurors' choice of sentence. True, Stoltzfus's testimony directly discussed only the circumstances of Whitlock's abduction, but its impact on the jury was almost certainly broader, as the prosecutor recognized. After the jury rendered its verdict on guilt, for example, the defense moved for a judgment of acquittal on the capital murder charge based on insufficiency of the evidence. In the prosecutor's argument to the court he replied that</p>
<blockquote>
<span class="star-pagination">*306</span> "the evidence clearly shows that this man was the aggressor. He was the one that ran out. He was the one that grabbed Leanne Whitlock. When she struggled trying to get away from him . . . , he was the one that started beating her there in the car. And finally subdued her enough to make her drive away from the mall, so you start with the principle that he is the aggressor." 20 Record 15.</blockquote>
<p>Stoltzfus's testimony helped establish the "principle," as the prosecutor put it, that Strickler was "the aggressor," the dominant figure, in the whole sequence of criminal events, including the murder, not just in the abduction. If the defense could have called Stoltzfus's credibility into question, the jurors' belief that Strickler was the chief aggressor might have been undermined to the point that at least one of them would have hesitated to recommend death.</p>
<p>The Court suggests that the jury might have concluded that Strickler was the leader based on three other pieces of evidence: Kurt Massie's identification of Strickler as the driver of Whitlock's car on its way toward the field where she was killed; Donna Tudor's testimony that Strickler kept the car the following week; and Tudor's testimony that Strickler threatened Henderson with a knife later on the evening of the murder. But if we are going to look at other testimony we cannot stop here. The accuracy of both Massie's and Tudor's testimony was open to question,<sup>[4]</sup> and all of it was subject to some evidence that Henderson had taken a major role in the murder. The Court has quoted the District <span class="star-pagination">*307</span> Court's summation of evidence against him, <i>ante,</i> at 291, n. 36: Henderson's wallet was found near the body, his clothes were bloody, he presented a woman friend with the victim's watch at a postmortem celebration (which he left driving the victim's car), and he confessed to a friend that he had just killed an unidentified black person. Had this been the totality of the evidence, the jurors could well have had little certainty about who had been in charge. But they could have had no doubt about the leader if they believed Stoltzfus.</p>
<p>Ultimately, I cannot accept the Court's discount of Stoltzfus in the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> sentencing calculus for the reason I have repeatedly emphasized, the undeniable narrative force of what she said. Against this, it does not matter so much that other witnesses could have placed Strickler at the shopping mall on the afternoon of the murder, <i>ante,</i> at 293-294, or that the Stoltzfus testimony did not directly address the aggravating factors found, <i>ante,</i> at 295. What is important is that her evidence presented a gripping story, see E. Loftus &amp; J. Doyle, Eyewitness Testimony: Civil and Criminal 5 (3d ed. 1997) ("[R]esearch redoundingly proves that the story format is a powerful key to juror decision making"). Its message was that Strickler was the madly energetic leader of two morally apathetic accomplices, who were passive but for his direction. One cannot be reasonably confident that not a single juror would have had a different perspective after an impeachment that would have destroyed the credibility of that story. I would accordingly vacate the sentence and remand for reconsideration, and to that extent I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Gerald T. Zerkin</i> filed a brief for the National Association of Criminal Defense Lawyers et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>Kent S. Scheidegger</i> filed a brief for the Criminal Justice Legal Foundation as <i>amicus curiae</i> urging affirmance.</p>
<p>[]   Justice Thomas joins Parts I and IV of this opinion. Justice Kennedy joins Part III.</p>
<p>[1]  The opinion of the Court of Appeals is unreported. The judgment order is reported, <i>Strickler</i> v<i>. Pruett,</i> <span class="citation no-link">149 F. 3d 1170</span> (CA4 1998). The opinion of the District Court is also unreported.</p>
<p>[2]  Petitioner was tried in May 1990. Henderson fled the Commonwealth and was later apprehended in Oregon. He was tried in March 1991.</p>
<p>[3]  Workman was calledas a defense witness.</p>
<p>[4]  Whitlock's roommate testified that Whitlock had dinner at 6 p.m. on January 5, 1990, just before she left for the mall to return Dean's car.</p>
<p>[5]  She testified to their appearances in great detail. She stated that petitioner had "a kind of multi layer look." He wore a grey T-shirt with a Harley Davidson insignia on it. The prosecutor showed Stoltzfus the shirt, stained with blood and semen, that the police had discovered at petitioner's mother's house. He asked if it were the same shirt she saw petitioner wearing at the mall. She replied,"That could have been it." App. 37, 39. Henderson "had either a white or light colored shirt, probably a short sleeve knit shirt and his pants were neat. They weren't just old blue jeans. They may have been new blue jeans or it may have just been more dressy slacks of some sort." <i>Id.,</i> at 37. The woman "had blonde hair, it was kind of in a shaggy cut down the back. She had blue eyes, she had a real sweet smile, kind of a small mouth. Just a touch of freckles on her face."<i>Id.,</i> at 60.</p>
<p>[6]  Stoltzfus stated that the girl caught a button in Stoltzfus' "open weave sweater, which is why I remember her attire." <i>Id.,</i> at 39.</p>
<p>[7]  "I said to my fourteen[-year-]old daughter, write down the license number, you know, it was West Virginia, NKA 243 and I said help me to remember, `No Kids Alone 243,' and I said remember, 243 is my age." <i>Id.,</i>  at 48.</p>
<p>[8]  These materials were originally attached to an affidavit submitted with petitioner's motion for summary judgment on his federal petition for habeas corpus. Because both the District Court and the Court of Appeals referred to the documents by their exhibit numbers, we have done the same.</p>
<p>[9]  As the District Court pointed out, however, it omits reference to the fact that Stoltzfus originally said that she could not identify the victim a fact recorded in his handwritten notes. <i>Id.,</i> at 387.</p>
<p>[10]  Stoltzfus' trial testimony made no mention of her meeting with Dean.</p>
<p>[11]  The prosecutor recalled that Exhibits 2, 7, and 8 had been in his open file, <i>id.,</i> at 365-368, but the lawyer who represented Henderson at his trial swore that they were not in the file, <i>id.,</i> at 330; the recollection of petitioner's trial counsel was somewhat equivocal. Lead defense counsel was sure he had not seen the documents, <i>id.,</i> at 300, while petitioner's other lawyer signed an affidavit to the effect that he does "remember the information contained in [the documents]" but "cannot recall if I have seen these specific documents," <i>id.,</i> at 371.</p>
<p>[12]  Although the parties have not advanced an explanation for the nondisclosure of the documents, perhaps it was an inadvertent consequence of the fact that Harrisonburg is in Rockingham County and the trial was conducted by the Augusta County prosecutor. We note, however, that the prosecutor is responsible for "any favorable evidence known to the others acting on the government's behalf in the case, including the police." <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 437</a></span> (1995). Thus, the Commonwealth, through its prosecutor, is charged with knowledge of the Stoltzfus materials for purposes of <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).</p>
<p>[13]  In the federal habeas proceedings, the prosecutor gave the following sworn answer to an interrogatory requesting him to state what materials were disclosed by him to defense counsel pursuant to <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>:</i> "I disclosed my entire prosecution file to Strickler's defense counsel prior to Strickler's trial by allowing him to inspect my entire prosecution file including, but not limited to, all police reports in the file and all witness statements in the file." App. 368. Petitioner's trial counsel had shared the prosecutor's understanding of the "open file" policy. In an affidavit filed in the state habeas proceeding, they stated that they "thoroughly investigated" petitioner's case. "In this we were aided by the prosecutor's office, which gave us full access to their files and the evidence they intended to present. We made numerous visits to their office to examine these files . . . . As a result of this cooperation, they introduced nothing at trial of which we were previously unaware." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#223" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 223</a></span>.</p>
<p>[14]  In its pleadings on state habeas, the Commonwealth explained: "From the inception of this case, the prosecutor's files were open to the petitioner's counsel. Each of the petitioner's attorneys made numerous visits to the prosecutor's offices and reviewed <i>all</i> the evidence the Commonwealth intended to present. . . . Given that counsel were voluntarily given full disclosure of everything known to the government, there was no need for a formal <i>[Brady]</i> motion." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#212" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 212-213</a></span>.</p>
<p>[15]  "The Commonwealth's theory of the case was that Strickler and Henderson had acted jointly to accomplish the actual killing. It contended at trial, and argues on appeal, that the physical evidence points to a violent struggle between the assailants and the victim, in which Strickler's hair had actually been torn out by the roots. Although Leanne had been beaten and kicked, none of her injuries would have been sufficient to immobilize her until her skull was crushed with the 69-pound rock. Because, the Commonwealth's argument goes, the rock had been dropped on her head at least twice, while she was on the ground, leaving two bloodstained depressions in the frozen earth, it would have been necessary that she be held down by one assailant while the other lifted the rock and dropped it on her head.
</p>
<p>"The weight and dimensions of the 69-pound bloodstained rock, which was introduced in evidence as an exhibit, made it apparent that a single person could not have lifted it and dropped or thrown it while simultaneously holding the victim down. The bloodstains on Henderson's jacket as well as on Strickler's clothing further tended to corroborate the Commonwealth's theory that the two men had been in the immediate presence of the victim's body when the fatal blows were struck and, hence, had jointly participated in the killing." <i>Strickler,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#494" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>.</p>
<p>[16]  See n. 14, <i>supra.</i> </p>
<p>[17]  Petitioner later voluntarily dismissed this claim. App. 384.</p>
<p>[18]  For reasons we do not entirely understand, the Court of Appeals thus concluded that, while it was reasonable for trial counsel to rely on the open file policy, it was unreasonable for postconviction counsel to do so.</p>
<p>[19]  See, <i>e. g., </i><i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935) <i>(per curiam)</i><i>; </i><i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/#216" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213, 216</a></span> (1942); <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269-270</a></span> (1959).</p>
<p>[20]  Consider, for example, this comment in the dissenting opinion in <i>Kyles</i>  v. <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Whitley</a></span></i><i>:</i> "It is petitioner's burden to show that in light of all the evidence, including that untainted by the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation, it is reasonably probable that a jury would have entertained a reasonable doubt regarding petitioner's guilt." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#460" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 460</a></span> (opinion of Scalia, J.).</p>
<p>[21]  We reject respondent's contention that these documents do not fall under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> because they were "inculpatory." Brief for Respondent 41. Our cases make clear that <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> `s disclosure requirements extend to materials that, whatever their other characteristics, may be used to impeach a witness. <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 676</a></span> (1985).</p>
<p>[22]  While the precise dimensions of an "open file policy" may vary from jurisdiction to jurisdiction, in this case it is clear that the prosecutor's use of the term meant that his entire prosecution file was made available to the defense. App. 368; see also n. 13, <i>supra.</i> </p>
<p>[23]  We certainly do not criticize the prosecution's use of the open file policy. We recognize that this practice may increase the efficiency and the fairness of the criminal process. We merely note that, if a prosecutor asserts that he complies with <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> through an open file policy, defense counsel may reasonably rely on that file to contain all materials the State is constitutionally obligated to disclose under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i> </p>
<p>[24]  "[W]e think that the existence of cause for a procedural default must ordinarily turn on whether the prisoner can show that some objective factor external to the defense impeded counsel's efforts to comply with the State's procedural rule. Without attempting an exhaustive catalog of such objective impediments to compliance with a procedural rule, we note that a showing that the factual or legal basis for a claim was not reasonably available to counsel, see <i>Reed</i> v<i>. Ross,</i> 468 U. S., at 16, or that `some interference by officials,' <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#486" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 486</a></span> (1953), made compliance impracticable, would constitute cause under this standard." <i>Murray,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S., at 488</a></span>; see also <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#221" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214, 221-222</a></span> (1988).</p>
<p>[25]  Stoltzfus testified to meeting with Claytor at least three times. App. 55-56.</p>
<p>[26]  In her letter, which appeared on July 18, 1990 (after petitioner's trial) in the Harrisonburg Daily News-Record, Stoltzfus stated: "It never occurred to me that I was witnessing an abduction. In fact, if it hadn't been for the intelligent, persistent, professional work of Detective Daniel Claytor, I still wouldn't realize it. What sounded like a coherent story at the trial was the result of an incredible effort by the police to fit a zillion little puzzle pieces into one big picture." <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#250" aria-description="Citation for case: Amadeo v. Zant"><i>Id.,</i> at 250</a></span>. Stoltzfus also gave a pretrial interview to a reporter with the Roanoke Times that conflicted in some respects with her trial testimony, principally because she identified the blonde woman at the mall as Tudor. <i>Id.,</i> at 373.</p>
<p>[27]  The defense could not discover copies of these notes from Stoltzfus herself, because she refused to speak with defense counsel before trial. <i>Id.,</i> at 370.</p>
<p>[28]  The parties have been unable to provide, and the record does not illuminate, the factual basis on which the District Court entered the discovery order. It was granted <i>ex parte</i> and under seal and furnished broad access to any records relating to petitioner. District Court Record, Doc. No. 20. The Fourth Circuit has since found that federal district courts do not possess the authority to issue <i>ex parte</i> discovery orders in habeas proceedings. <i>In re Pruett,</i> <span class="citation" data-id="6961602"><a href="/opinion/7057802/in-re-pruett/#280" aria-description="Citation for case: In re Pruett">133 F. 3d 275, 280</a></span> (1997). We express no opinion on the Fourth Circuit's decision on this question. However, we note that it is unlikely that petitioner would have been granted in state court the sweeping discovery that led to the Stoltzfus materials, since Virginia law limits discovery available during state habeas. Indeed, it is not even clear that he had a right to such discovery in federal court. See n. 29<i>, infra.</i> </p>
<p>[29]  Virginia law provides that "no discovery shall be allowed in any proceeding for a writ of habeas corpus or in the nature of coram nobis without prior leave of the court, which may deny or limit discovery in any such proceeding." Va. Sup. Ct. Rule 4:1(b)(5)(3)(b) (1998); see also <i>Yeatts</i> v. <i>Murray,</i> <span class="citation" data-id="1219071"><a href="/opinion/1219071/yeatts-v-murray/#289" aria-description="Citation for case: Yeatts v. Murray">249 Va. 285, 289</a></span>, <span class="citation" data-id="1219071"><a href="/opinion/1219071/yeatts-v-murray/#21" aria-description="Citation for case: Yeatts v. Murray">455 S. E. 2d 18, 21</a></span> (1995). Respondent acknowledges that petitioner was not entitled to discovery under Virginia law. Brief for Respondent 25.</p>
<p>[30]  See Va. Sup. Ct. Rule 3A:11 (1998). This rule expressly excludes from defendants "the discovery or inspection of statements made by Commonwealth witnesses or prospective Commonwealth witnesses to agents of the Commonwealth or of reports, memoranda or other internal Commonwealth documents made by agents in connection with the investigation or prosecution of the case, except [for scientific reports of the accused or alleged victim]." The Virginia Supreme Court found that petitioner had been afforded all the discovery he was entitled to on direct review. "Limited discovery is permitted in criminal cases by the Rules of Court. . . . Strickler had the benefit of all the discovery to which he was entitled under the Rules. Those rights do not extend to general production of evidence, except in the limited areas prescribed by Rule 3A:11." <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#491" aria-description="Citation for case: Strickler v. Commonwealth">241 Va. 482, 491</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#233" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d 227, 233</a></span> (1991).</p>
<p>[31]  This statement is quoted in full at n. 14, <i>supra.</i> Respondent argues that this representation is not dispositive because it was made in his motion to dismiss and therefore cannot excuse the failure to include a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim in the petitioner's original state habeas pleading. We find the timing of the statement irrelevant, since the warden's response merely summarizes the Commonwealth's "open file" policy, instituted by the prosecution at the inception of the case.</p>
<p>[32]  Furthermore, in its opposition to petitioner's motion during state habeas review for funds for an investigator, the Commonwealth argued: "Strickler's Petition contains 139 separate habeas claims. By requesting appointment of an investigator `to procure the necessary factual basis to support certain of Petitioner's claims' (Motion, p. 1), Petitioner is implicitly conceding that he is not aware of factual support for the claims he has already made<i>.</i> Respondent agrees." App. 242.
</p>
<p>In light of these assertions, we fail to see how the Commonwealth believes petitioner could have shown "good cause" sufficient to get discovery on a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state habeas.</p>
<p>[33]  We do not reach, because it is not raised in this case, the impact of a showing by the State that the defendant was aware of the existence of the documents in question and knew, or could reasonably discover, how to obtain them. Although <i><span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/" aria-description="Citation for case: Gray v. Netherland">Gray</a></span></i> involved a procedurally defaulted <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>  claim, in that case, the Court found that the petitioner had made "no attempt to demonstrate cause or prejudice for his default." <i>Gray,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#162" aria-description="Citation for case: Gray v. Netherland">518 U. S., at 162</a></span>.</p>
<p>[34]  It is noteworthy that both of the reasons on which we relied in <i><span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/" aria-description="Citation for case: McCleskey v. Zant">McCleskey</a></span></i> to distinguish <i><span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">Amadeo</a></span></i> also apply to this case: "This case differs from <i><span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/" aria-description="Citation for case: Amadeo v. Zant">Amadeo</a></span></i> in two crucial respects. First, there is no finding that the State concealed evidence. And second, even if the State intentionally concealed the 21-page document, the concealment would not establish cause here because, in light of McCleskey's knowledge of the information in the document, any initial concealment would not have prevented him from raising the claim in the first federal petition." <span class="citation" data-id="9432249"><a href="/opinion/112573/mccleskey-v-zant/#501" aria-description="Citation for case: McCleskey v. Zant">499 U. S., at 501-502</a></span>.</p>
<p>[35]  Because our opinion does not modify <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> we reject respondent's contention that we announce a "new rule" today. See <i>Bousley</i> v. <i>United States,</i> <span class="citation" data-id="9433629"><a href="/opinion/118205/bousley-v-united-states/" aria-description="Citation for case: Bousley v. United States">523 U. S. 614</a></span> (1998).</p>
<p>[36]  The District Court summarized the evidence against Henderson. "Henderson's clothes had blood on them that night. Henderson had property belonging to Whitlock and gave her watch to a woman, Simmons, while at a restaurant known as Dice's Inn. Tr. 541. Henderson left Dice's Inn driving Whitlock's car. Henderson's wallet was found in the vicinity of Whitlock's body and was possibly lost during his struggle with her. Significantly, Henderson confessed to a friend on the night of the murder that he had just killed an unidentified black person and that friend observed blood on Henderson's jeans." App. 395.</p>
<p>[37]  At sentencing, the trial court discussed the mitigation evidence: "On the charge of capital murder . . . it is difficult . . . to sit here and listen to the testimony of [petitioner's mother] and Mr. Strickler's two sisters and not feel a great, great deal of sympathy for, for any person who has a childhood and a life like Mr. Strickler has had. He was in no way responsible for the circumstances of his birth. He was brutalized from the minute he's, almost from the minute he was born and certainly with his . . . limitations and his ability with which he was born, it would have been extremely difficult for him to, to help himself. And difficult, when you look at a case like that to feel but anything but sympathy for him." Sentencing Hearing, 20 Record 57-58.</p>
<p>[38]  As the trial court stated at petitioner's sentencing hearing: "The facts in this case which support this jury verdict are one that Mr. Strickler was . . . in control of this situation. He was in control at the shopping center in Harrisonburg. He was in control when the car went into the field up here on the 340 north of Waynesboro. He was in control thereafter, he ended up with the car. There is no question who . . . was in control of this entire situation." <i>Id.,</i> at 22.</p>
<p>[39]  The judge gave the following instruction at petitioner's trial: "You may find the defendant guilty of capital murder if the evidence establishes that the defendant jointly participated in the fatal beating, if it is established beyond a reasonable doubt that the defendant was an active and immediate participant in the act or acts that caused the victim's death." <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#493" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 493-494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#234" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 234-235</a></span>. The Virginia Supreme Court affirmed the propriety of this instruction on petitioner's direct appeal. <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#495" aria-description="Citation for case: Strickler v. Commonwealth"><i>Id.,</i> at 495</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>.</p>
<p>[40]  It is also consistent with the fact that Henderson was convicted of first-degree murder but acquitted of capital murder after his jury, unlike petitioner's, was instructed that they could convict him of capital murder only if they found that he had "`inflict[ed] the fatal blows.' " Henderson's jury was instructed, "`One who is present aiding and abetting the actual killing, but who does not inflict the fatal blows that cause death is a principle [sic] in the second degree, and may not be found guilty of capital murder. Before you can find the defendant guilty of capital murder, the evidence must establish beyond a reasonable doubt that the defendant was an active and immediate participant in the acts that caused the death.' " 2 App. in No. 97-29 (CA4), p. 777.
</p>
<p>Henderson's trial took place before the Virginia Supreme Court affirmed the trial instruction, and the "joint perpetrator" theory it embodied, given at petitioner's trial. <i>Strickler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#494" aria-description="Citation for case: Strickler v. Commonwealth">241 Va., at 494</a></span>, <span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/#235" aria-description="Citation for case: Strickler v. Commonwealth">404 S. E. 2d, at 235</a></span>. Petitioner's trial judge rejected one of petitioner's proffered instructions, which would have required the Commonwealth to prove that "the defendant was the person who actually delivered the blow that killed Leanne Whitlock." <i><span class="citation" data-id="1348258"><a href="/opinion/1348258/strickler-v-commonwealth/" aria-description="Citation for case: Strickler v. Commonwealth">Ibid.</a></span></i> Petitioner's trial judge recused himself from presiding over Henderson's trial, indicating that he had already formed his own opinion about what had happened the night of Whitlock's murder. 21 Record 2.</p>
<p>[41]  For example, the police recovered hairs on a bra and shirt found with Whitlock's body that "were microscopically alike in all identifiable characteristics" to petitioner's hair. App. 135. The shirt recovered from the car at Strickler's mother's house had human blood on it. Petitioner's fingerprints were found on the outside and inside of the car taken from Whitlock. <i>Id.,</i> at 128-129. Tudor testified that petitioner's pants had blood on them, and he had a cut on his knuckle. <i>Id.,</i> at 95.</p>
<p>[42]  The trial judge thought the shape of the rock so significant to the jury's conclusion that he instructed the lawyers to have "detailed, high quality photographs taken of [the rock] . . . and I want it put in the record of the case." Sentencing Hearing, 20 Record 53.</p>
<p>[43]  The Deputy Chief Medical Examiner, who performed the autopsy, testified that the object that produced the fractures in Whitlock's skull caused "severe lacerations to the brain," and any two of the four fractures would have been fatal. App. 112.</p>
<p>[44]  The trial court instructed the jury that, to convict petitioner of capital murder, it must find beyond a reasonable doubt that (1) "the defendant killed Leanne Whitlock"; (2) "the killing was willful, deliberate and premeditated"; and (3) "the killing occurred during the commission of robbery while the defendant was armed with a deadly weapon, or occurred during the commission of abduction with intent to extort money or a pecuniary benefit or with the intent to defile or was of a person during the commission of, or subsequent to, rape." <i>Strickler</i> v. <i>Murray,</i> <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/" aria-description="Citation for case: Strickler v. Murray">249 Va. 120</a></span>, 124 125, <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#650" aria-description="Citation for case: Strickler v. Murray">452 S. E. 2d 648, 650</a></span> (1995).</p>
<p>[45]  In its motion to dismiss petitioner's state habeas petition, the Commonwealth conceded that the instruction on intent to defile was erroneously given in this case as a predicate for capital murder. App. 218.</p>
<p>[46]  In his closing argument, the prosecutor stated that there was "really no doubt about where it happened and what the murder weapon was. It was not a gun, it wasn't a knife. It was this thing here, it is to[o] big to be called a rock and to[o] small to be called a boulder." <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#167" aria-description="Citation for case: Strickler v. Murray"><i>Id.,</i> at 167</a></span>.</p>
<p>[47]  The instructions given to the jury defined a deadly weapon as "any object or instrument that is likely to cause death or great bodily injury because of the manner and under the circumstance in which it is used." <span class="citation" data-id="1385494"><a href="/opinion/1385494/strickler-v-murray/#160" aria-description="Citation for case: Strickler v. Murray"><i>Id.,</i> at 160</a></span>.</p>
<p>[48]  The jury recommended death after finding the predicates of "future dangerousness" and "vileness." Neither of these predicates depended on Stoltzfus' testimony. The trial court instructed the jury, "Before the penalty can be fixed at death, the Commonwealth must prove beyond a reasonable doubt at least one of the following two alternatives. One, that after consideration of his history and background, there is a probability that he would commit criminal acts of violence that would constitute a continuing, continuing serious threat to society or two, that his conduct in committing the offense was outrageously or wantonly vile, horrible or inhuman and that it involved torture, depravity of mind or aggravated battery to the victim beyond the minimum necessary to accomplish the act of murder." Tr. 899-900.</p>
<p>[1]  The Court notes that the District Court did not resolve whether all eight of the Stoltzfus documents had been withheld, as Strickler claimed, or only five. For purposes of its decision granting summary judgment for Strickler, the District Court assumed that only five had not been disclosed. See <i>ante,</i> at 290, 279. The Court of Appeals also left the dispute unresolved, see App. 418, n. 8, though granting summary judgment for respondent based on a lack of prejudice would presumably have required that court to assume that all eight documents had been withheld. Because this Court affirms the grant of summary judgment for respondent based on lack of prejudice and because it relies on at least one of the disputed documents in its analysis, see <i>ante,</i> at 282, I understand it to have assumed that none of the eight documents was disclosed. I proceed based on that assumption as well. If one thought the difference between five and eight documents withheld would affect the determination of prejudice, a remand to resolve that factual question would be necessary.</p>
<p>[2]  In keeping with suggestions in a number of our opinions, see <i>Schlup</i> v. <i>Delo,</i> <span class="citation" data-id="9433081"><a href="/opinion/117893/schlup-v-delo/#327" aria-description="Citation for case: Schlup v. Delo">513 U. S. 298, 327, n. 45</a></span> (1995); <i>Sawyer</i> v. <i>Whitley,</i> <span class="citation" data-id="9432638"><a href="/opinion/112773/sawyer-v-whitley/#345" aria-description="Citation for case: Sawyer v. Whitley">505 U. S. 333, 345</a></span> (1992), the Court treats the prejudice enquiry as synonymous with the materiality determination under <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963). See <i>ante,</i> at 282, 288-289, 296. I follow the Court's lead.</p>
<p>[3]  Each of these phrases or standards has been used in a number of contexts. This Court has used "reasonable possibility," for example, in defining the level of threat of injury to competition needed to make out a claim under the Robinson-Patman Act, see, <i>e. g., </i><i>Brooke Group Ltd.</i> v. <i>Brown &amp; Williamson Tobacco Corp.,</i> <span class="citation" data-id="9432860"><a href="/opinion/112893/brooke-group-ltd-v-brown-williamson-tobacco-corp/#222" aria-description="Citation for case: Brooke Group Ltd. v. Brown &amp; Williamson Tobacco Corp.">509 U. S. 209, 222</a></span> (1993); the standard for judging whether a grand jury subpoena should be quashed under Federal Rule of Criminal Procedure 17(c), see <i>United States</i> v. <i>R. Enterprises, Inc.,</i> <span class="citation" data-id="9432185"><a href="/opinion/112523/unite

[...TRUNCATED 5006 of 125006 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Tanzin v. Tanvir.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Tanzin v. Tanvir
type: case
citation: "592 U.S. 43 (2020)"
parallel_cite: "141 S. Ct. 486; 208 L. Ed. 2d 295"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2020
date_decided: ""
docket: 19-71
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
  opinion_url: "https://www.courtlistener.com/opinion/4837663/tanzin-v-tanvir/"
  cluster_id: 4837663
  opinion_id: null
  identity_checked: true
lake:
  record_id: Tanzin v. Tanvir
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - rfra
  - federal-officer-liability
  - money-damages
  - first-amendment
holding: "The Religious Freedom Restoration Act's authorization of 'appropriate relief against a government' permits a plaintiff to recover money damages against federal officials sued in their individual capacities for burdening religious exercise."
---

# Tanzin v. Tanvir

*592 U.S. 43 (2020)* (No. 19-71) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4837663 → opinion 4641442; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "592 U. S. ____ (2020)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Muhammad Tanvir and other practicing Muslims alleged that FBI agents placed them on the No Fly List in retaliation for their refusal to act as informants against their religious communities. They sued under the Religious Freedom Restoration Act (RFRA), seeking injunctive relief against the agents in their official capacities and money damages against the agents in their individual capacities. The District Court held that RFRA does not authorize monetary relief and dismissed the individual-capacity claims; the Second Circuit reversed, holding that RFRA's remedies provision reaches money damages against government officials.

## Issue
Whether RFRA's authorization of "appropriate relief against a government" includes claims for money damages against federal officials sued in their individual capacities.

## Rule
RFRA lets a person whose religious exercise is unlawfully burdened "obtain appropriate relief against a government," and expressly defines "government" to include an "official (or other person acting under color of law) of the United States." The phrase "under color of law" carries the meaning long given it in the 42 U.S.C. § 1983 context, where it permits suits against officials in their individual capacities; and "appropriate relief" is open-ended and context-dependent, with damages historically available against government officials. The Court framed and answered the question directly: the issue "is whether 'appropriate relief' includes claims for money damages against Government officials in their individual capacities. We hold that it does." — 592 U.S. 43 (slip op., at 1). ^pin-op

## Application
When RFRA was enacted its definition of "government" included state and local officials, and to restore the pre-*Smith* protections and the right to vindicate them by a claim, its remedies had to encompass at least the relief available under § 1983 — which has always allowed damages for clearly established First Amendment violations. The *Sossamon* presumption against damages did not apply, because a suit against officials in their individual capacities does not implicate sovereign immunity.

## Conclusion
The judgment of the Second Circuit was **affirmed**. Thomas, J., delivered the opinion of the Court, in which all other Members joined, except Barrett, J., who took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Tanzin* establishes a money-damages remedy against federal officers personally under RFRA, paralleling the individual-capacity exposure long recognized under § 1983 and sharpening the stakes of official conduct that substantially burdens religious exercise.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Tanzin v. Tanvir*, 592 U.S. 43 (2020)](https://www.courtlistener.com/opinion/4837663/tanzin-v-tanvir/) — pinpoint: slip op., at 1 (Opinion of the Court, holding; Thomas, J.). CL carries the slip opinion ("592 U. S. ____ (2020)"; cluster 4837663 → opinion 4641442); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "75cc5ab65f300b4f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Tanzin v. Tanvir"}, "payload": {"all": [{"cite": "592 U.S. 43", "page": "43", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "592"}, {"cite": "141 S. Ct. 486", "page": "486", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "208 L. Ed. 2d 295", "page": "295", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "208"}], "display": "592 U.S. 43", "official": {"cite": "592 U.S. 43", "page": "43", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "592"}, "official_selection_present": true, "record_id": "Tanzin v. Tanvir"}}
{"assertion_id": "f64d9d8b7eb49946", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Tanzin v. Tanvir"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Tanzin v. Tanvir", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Tanzin v. Tanvir

```json
{
  "schema_version": "s2.v1",
  "record_id": "Tanzin v. Tanvir",
  "status": "under_review",
  "identity": {
    "case_name": "Tanzin v. Tanvir",
    "case_name_short": "Tanzin",
    "case_name_full": "",
    "input_case_name": "Tanzin v. Tanvir",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2020,
    "docket": "19-71",
    "cluster_id": 4837663,
    "lead_opinion_id": 4641442,
    "sibling_ids": [],
    "absolute_url": "/opinion/4837663/tanzin-v-tanvir/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 43",
      "volume": "592",
      "reporter": "U.S.",
      "page": "43",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 486",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 295",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 43",
        "volume": "592",
        "reporter": "U.S.",
        "page": "43",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 486",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 295",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 43",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 43",
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
    "date_created": "2026-07-06T12:09:45Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "tanzin-v-tanvir--4837663",
      "to_record_id": "Tanzin v. Tanvir",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Tanzin v. Tanvir

```
(Slip Opinion)              OCTOBER TERM, 2020                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                  TANZIN ET AL. v. TANVIR ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE SECOND CIRCUIT

   No. 19–71.      Argued October 6, 2020—Decided December 10, 2020
The Religious Freedom Restoration Act of 1993 (RFRA) was enacted in
  the wake of Employment Div., Dept. of Human Resources of Ore. v.
  Smith, 494 U. S. 872, to provide a remedy to redress Federal Govern-
  ment violations of the right to free exercise under the First Amend-
  ment. Respondents are practicing Muslims who sued under RFRA,
  claiming that federal agents placed them on the No Fly List for refus-
  ing to act as informants against their religious communities. They
  sought injunctive relief against the agents in their official capacities
  and monetary damages against the agents in their individual capaci-
  ties. As relevant here, the District Court found that RFRA does not
  permit monetary relief and dismissed their individual-capacity claims.
  The Second Circuit reversed, holding that RFRA’s remedies provision
  encompasses money damages against Government officials.
Held: RFRA’s express remedies provision permits litigants, when appro-
 priate, to obtain money damages against federal officials in their indi-
 vidual capacities. Pp. 3–9.
    (a) RFRA’s text provides that persons may sue and “obtain appro-
 priate relief against a government,” 42 U. S. C. §2000bb–1(c), includ-
 ing an “official (or other person acting under color of law) of the United
 States,” §2000bb–2(1). RFRA supplants the ordinary meaning of “gov-
 ernment” with a different, express definition that includes “official[s].”
 It then underscores that “official[s]” are “person[s].” Under RFRA’s
 definition, relief that can be executed against an “official . . . of the
 Unites States” is “relief against a government.” This reading is con-
 firmed by RFRA’s use of the phrase “persons acting under color of law,”
 which has long been interpreted by this Court in the 42 U. S. C. §1983
 context to permit suits against officials in their individual capacities.
 See, e.g., Memphis Community School Dist. v. Stachura, 477 U. S. 299,
2                           TANZIN v. TANVIR

                                  Syllabus

    305–306. Pp. 3–5.
       (b) RFRA’s term “appropriate relief” is “open-ended” on its face;
    thus, what relief is “ ‘appropriate’ ” is “inherently context dependent.”
    Sossamon v. Texas, 563 U. S. 277, 286. In the context of suits against
    Government officials, damages have long been awarded as appropriate
    relief, and though more limited today, they remain an appropriate
    form of relief. The availability of damages under §1983 is particularly
    salient here. When Congress first enacted RFRA, the definition of
    “government” included state and local officials. In order to reinstate
    the pre-Smith substantive protections of the First Amendment and the
    right to vindicate those protections by a claim, §2000bb(b), the reme-
    dies provision must have encompassed at least the same forms of relief
    authorized by §1983. Because damages claims have always been avail-
    able under §1983 for clearly established violations of the First Amend-
    ment, that means RFRA provides, as one avenue for relief, a right to
    seek damages against Government employees. The presumption in
    Sossamon, 563 U. S. 277, is inapplicable because this case does not in-
    volve sovereign immunity. Pp. 5–9.
894 F. 3d 449, affirmed.

  THOMAS, J., delivered the opinion of the Court, in which all other Mem-
bers joined, except BARRETT, J., who took no part in the consideration or
decision of the case.
                        Cite as: 592 U. S. ____ (2020)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–71
                                    _________________


 FNU TANZIN, ET AL., PETITIONERS v. MUHAMMAD
                 TANVIR, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                               [December 10, 2020]

   JUSTICE THOMAS delivered the opinion of the Court.
   The Religious Freedom Restoration Act of 1993 (RFRA)
prohibits the Federal Government from imposing substan-
tial burdens on religious exercise, absent a compelling in-
terest pursued through the least restrictive means. 107
Stat. 1488, 42 U. S. C. §2000bb et seq. It also gives a person
whose religious exercise has been unlawfully burdened the
right to seek “appropriate relief.” The question here is
whether “appropriate relief ” includes claims for money
damages against Government officials in their individual
capacities. We hold that it does.
                               I
                              A
  RFRA secures Congress’ view of the right to free exercise
under the First Amendment, and it provides a remedy to
redress violations of that right. Congress passed the Act in
the wake of this Court’s decision in Employment Div., Dept.
of Human Resources of Ore. v. Smith, 494 U. S. 872, 885–
890 (1990), which held that the First Amendment tolerates
neutral, generally applicable laws that burden or prohibit
2                     TANZIN v. TANVIR

                      Opinion of the Court

religious acts even when the laws are unsupported by a nar-
rowly tailored, compelling governmental interest. See
§2000bb(a). RFRA sought to counter the effect of that hold-
ing and restore the pre-Smith “compelling interest test” by
“provid[ing] a claim . . . to persons whose religious exercise
is substantially burdened by government.” §§2000bb(b)(1)–
(2). That right of action enables a person to “obtain appro-
priate relief against a government.” §2000bb–1(c). A “ ‘gov-
ernment’ ” is defined to include “a branch, department,
agency, instrumentality, and official (or other person acting
under color of law) of the United States.” §2000bb–2(1).
                               B
   Respondents Muhammad Tanvir, Jameel Algibhah, and
Naveed Shinwari are practicing Muslims who claim that
Federal Bureau of Investigation agents placed them on the
No Fly List in retaliation for their refusal to act as inform-
ants against their religious communities. Respondents
sued various agents in their official capacities, seeking re-
moval from the No Fly List. They also sued the agents in
their individual capacities for money damages. According
to respondents, the retaliation cost them substantial sums
of money: airline tickets wasted and income from job oppor-
tunities lost.
   More than a year after respondents sued, the Department
of Homeland Security informed them that they could now
fly, thus mooting the claims for injunctive relief. The Dis-
trict Court then dismissed the individual-capacity claims
for money damages, ruling that RFRA does not permit mon-
etary relief.
   The Second Circuit reversed. 894 F. 3d 449 (2018). It
determined that RFRA’s express remedies provision, com-
bined with the statutory definition of “Government,” au-
thorizes claims against federal officials in their individual
capacities. Relying on our precedent and RFRA’s broad pro-
tections for religious liberty, the court concluded that the
                  Cite as: 592 U. S. ____ (2020)              3

                      Opinion of the Court

open-ended phrase “appropriate relief ” encompasses
money damages against officials. We granted certiorari,
589 U. S. ___ (2019), and now affirm.
                              II
  As usual, we start with the statutory text. E.g., Mission
Product Holdings, Inc. v. Tempnology, LLC, 587 U. S. ___,
___ (2019) (slip op., at 8). A person whose exercise of reli-
gion has been unlawfully burdened may “obtain appropri-
ate relief against a government.” 42 U. S. C. §2000bb–1(c).
                                 A
   We first have to determine if injured parties can sue Gov-
ernment officials in their personal capacities. RFRA’s text
provides a clear answer: They can. Persons may sue and
obtain relief “against a government,” §2000bb–1(c), which
is defined to include “a branch, department, agency, instru-
mentality, and official (or other person acting under color of
law) of the United States.” §2000bb–2(1) (emphasis added).
   The Government urges us to limit lawsuits against offi-
cials to suits against them in their official, not personal, ca-
pacities. A lawsuit seeking damages from employees in
their individual capacities, the Government argues, is not
really “against a government” because relief “can be exe-
cuted only against the official’s personal assets.” Kentucky
v. Graham, 473 U. S. 159, 166 (1985).
   The problem with this otherwise plausible argument is
that Congress supplanted the ordinary meaning of “govern-
ment” with a different, express definition. “ ‘When a statute
includes an explicit definition, we must follow that defini-
tion,’ even if it varies from a term’s ordinary meaning.” Dig-
ital Realty Trust, Inc. v. Somers, 583 U. S. ___, ___ (slip op.,
at 9) (quoting Burgess v. United States, 553 U. S. 124, 130
(2008)). For example, if a statute defines a “State” to in-
clude territories and districts, that addition to the plain
meaning controls. See, e.g., 15 U. S. C. §267. So too here.
4                     TANZIN v. TANVIR

                      Opinion of the Court

A “government,” under RFRA, extends beyond the term’s
plain meaning to include officials. And the term “official”
does not refer solely to an office, but rather to the actual
person “who is invested with an office.” 10 Oxford English
Dictionary 733 (2d ed. 1989). Under RFRA’s definition, re-
lief that can be executed against an “official . . . of the
United States” is “relief against a government.” 42 U. S. C.
§§2000bb–1(c), 2000bb–2(1).
   Not only does the term “government” encompass officials,
it also authorizes suits against “other person[s] acting un-
der color of law.” §2000bb–2(1). The right to obtain relief
against “a person” cannot be squared with the Govern-
ment’s reading that relief must always run against the
United States. Moreover, the use of the phrase “official (or
other person . . . )” underscores that “official[s]” are treated
like “person[s].” Ibid. (emphasis added). In other words,
the parenthetical clarifies that “a government” includes
both individuals who are officials acting under color of law
and other, additional individuals who are nonofficials act-
ing under color of law. Here, respondents sued the former.
   The legal “backdrop against which Congress enacted”
RFRA confirms the propriety of individual-capacity suits.
Stewart v. Dutra Constr. Co., 543 U. S. 481, 487 (2005). The
phrase “persons acting under color of law” draws on one of
the most well-known civil rights statutes: 42 U. S. C. §1983.
That statute applies to “person[s] . . . under color of any
statute,” and this Court has long interpreted it to permit
suits against officials in their individual capacities. See,
e.g., Memphis Community School Dist. v. Stachura, 477
U. S. 299, 305–306, and n. 8 (1986). Because RFRA uses
the same terminology as §1983 in the very same field of civil
rights law, “it is reasonable to believe that the terminology
bears a consistent meaning.” A. Scalia & B. Garner, Read-
ing Law: The Interpretation of Legal Texts 323 (2012). A
suit against an official in his personal capacity is a suit
against a person acting under color of law. And a suit
                  Cite as: 592 U. S. ____ (2020)             5

                      Opinion of the Court

against a person acting under color of law is a suit against
“a government,” as defined under RFRA. §2000bb–1(c).
                               B
   The question then becomes what “appropriate relief ” en-
tails. Without a statutory definition, we turn to the
phrase’s plain meaning at the time of enactment. See FCC
v. AT&T Inc., 562 U. S. 397, 403 (2011). “Appropriate”
means “[s]pecially fitted or suitable, proper.” 1 Oxford Eng-
lish Dictionary, at 586; see also Merriam-Webster’s Colle-
giate Dictionary 57 (10th ed. 1996) (“especially suitable or
compatible”). Because this language is “open-ended” on its
face, what relief is “ ‘appropriate’ ” is “inherently context
dependent.” Sossamon v. Texas, 563 U. S. 277, 286 (2011)
(interpreting identical language).
   In the context of suits against Government officials, dam-
ages have long been awarded as appropriate relief. In the
early Republic, “an array of writs . . . allowed individuals to
test the legality of government conduct by filing suit
against government officials” for money damages “payable
by the officer.” Pfander & Hunt, Public Wrongs and Private
Bills: Indemnification and Govt Accountability in the Early
Republic, 85 N. Y. U. L. Rev. 1862, 1871–1875 (2010); see
id., at 1875, n. 52 (collecting cases). These common-law
causes of action remained available through the 19th cen-
tury and into the 20th. See, e.g., Little v. Barreme, 2 Cranch
170 (1804); Elliott v. Swartwout, 10 Pet. 137 (1836); Mitch-
ell v. Harmony, 13 How. 115 (1852); Buck v. Colbath, 3
Wall. 334 (1866); Belknap v. Schild, 161 U. S. 10 (1896);
Philadelphia Co. v. Stimson, 223 U. S. 605, 619–620 (1912)
(“The exemption of the United States from suit does not pro-
tect its officers from personal liability to persons whose
rights of property they have wrongfully invaded”).
   Though more limited, damages against federal officials
remain an appropriate form of relief today. In 1988 the
Westfall Act foreclosed common-law claims for damages
6                     TANZIN v. TANVIR

                      Opinion of the Court

against federal officials, 28 U. S. C. §2679, but it left open
claims for constitutional violations and certain statutory vi-
olations. §§2679(b)(2)(A)–(B). Indeed, the Act expressly
contemplates that a statute could authorize an action for
damages against Government employees. §2679(b)(2)(B)
(explaining that the displacement of remedies “does not ex-
tend or apply to a civil action against an employee of the
Government . . . which is brought for a violation of a statute
of the United States under which such action against an in-
dividual is otherwise authorized”).
   Damages are also commonly available against state and
local government officials. In 1871, for example, Congress
passed the precursor to §1983, imposing liability on any
person who, under color of state law, deprived another of a
constitutional right. 17 Stat. 13; see also Myers v. Ander-
son, 238 U. S. 368, 379, 383 (1915) (affirming award of dam-
ages against state election officials). By the time Congress
enacted RFRA, this Court had interpreted the modern ver-
sion of §1983 to permit monetary recovery against officials
who violated “clearly established” federal law. E.g., Procu-
nier v. Navarette, 434 U. S. 555, 561–562 (1978); Siegert v.
Gilley, 500 U. S. 226, 231 (1991).
   This availability of damages under §1983 is particularly
salient in light of RFRA’s origins. When first enacted,
RFRA defined “ ‘government’ ” to include an “official (or
other person acting under color of law) of the United States,
a State, or a subdivision of a State.” 107 Stat. 1489 (empha-
sis added). It made no distinction between state and federal
officials. After this Court held that RFRA could not be en-
forced against the States, see City of Boerne v. Flores, 521
U. S. 507, 511 (1997), Congress narrowly amended the def-
inition “by striking ‘a State, or a subdivision of a State.’ ”
114 Stat. 806. That context is important because RFRA
made clear that it was reinstating both the pre-Smith sub-
stantive protections of the First Amendment and the right
to vindicate those protections by a claim. §2000bb(b).
                  Cite as: 592 U. S. ____ (2020)            7

                      Opinion of the Court

There is no doubt that damages claims have always been
available under §1983 for clearly established violations of
the First Amendment. See, e.g., Sause v. Bauer, 585 U. S.
___ (2018) (per curiam) (reversing grant of qualified im-
munity in a case seeking damages under §1983 based on
alleged violations of free exercise rights and Fourth Amend-
ment rights); Murphy v. Missouri Dept. of Corrections, 814
F. 2d 1252, 1259 (CA8 1987) (remanding to enter judgment
for plaintiffs on a §1983 free speech and free exercise claims
and to determine and order “appropriate relief, which . . .
may, if appropriate, include an award” of damages). Given
that RFRA reinstated pre-Smith protections and rights,
parties suing under RFRA must have at least the same av-
enues for relief against officials that they would have had
before Smith. That means RFRA provides, as one avenue
for relief, a right to seek damages against Government em-
ployees.
   A damages remedy is not just “appropriate” relief as
viewed through the lens of suits against Government em-
ployees. It is also the only form of relief that can remedy
some RFRA violations. For certain injuries, such as re-
spondents’ wasted plane tickets, effective relief consists of
damages, not an injunction. See, e.g., DeMarco v. Davis,
914 F. 3d 383, 390 (CA5 2019) (destruction of religious prop-
erty); Yang v. Sturner, 728 F. Supp. 845 (RI 1990), opinion
withdrawn 750 F. Supp. 558 (RI 1990) (autopsy of son that
violated Hmong beliefs). Given the textual cues just noted,
it would be odd to construe RFRA in a manner that prevents
courts from awarding such relief. Had Congress wished to
limit the remedy to that degree, it knew how to do so. See,
e.g., 29 U. S. C. §1132(a)(3) (providing for “appropriate eq-
uitable relief ”); 42 U. S. C. §2000e–5(g)(1) (providing for
“equitable relief as the court deems appropriate”); 15
U. S. C. §78u(d)(5) (providing for “any equitable relief that
8                          TANZIN v. TANVIR

                           Opinion of the Court

may be appropriate or necessary”).*
   Our opinion in Sossamon does not change this analysis.
Sossamon held that a State’s acceptance of federal funding
did not waive sovereign immunity to suits for damages un-
der a related statute—the Religious Land Use and Institu-
tionalized Persons Act of 2000—which also permits “ ‘appro-
priate relief.’ ” 563 U. S., at 280, 282. The obvious
difference is that this case features a suit against individu-
als, who do not enjoy sovereign immunity.
   The Government also posits that we should be wary of
damages against government officials because these
awards could raise separation-of-powers concerns. But this
exact remedy has coexisted with our constitutional system
since the dawn of the Republic. To be sure, there may be
policy reasons why Congress may wish to shield Govern-
ment employees from personal liability, and Congress is
free to do so. But there are no constitutional reasons why
we must do so in its stead.
   To the extent the Government asks us to create a new
policy-based presumption against damages against individ-
ual officials, we are not at liberty to do so. Congress is best
suited to create such a policy. Our task is simply to inter-
pret the law as an ordinary person would. Although back-
ground presumptions can inform the understanding of a
word or phrase, those presumptions must exist at the time
of enactment. We cannot manufacture a new presumption
now and retroactively impose it on a Congress that acted 27
years ago.

——————
  * Both the Government and respondents agree that government offi-
cials are entitled to assert a qualified immunity defense when sued in
their individual capacities for money damages under RFRA. Indeed, re-
spondents emphasize that the “qualified immunity defense was created
for precisely these circumstances,” Brief for Respondents 22, and is a
“powerful shield” that “protects all but the plainly incompetent or those
who flout clearly established law,” Tr. of Oral Arg. 42; see District of Co-
lumbia v. Wesby, 583 U. S. ___, ___–___ (2018) (slip op., at 13–15).
                  Cite as: 592 U. S. ____ (2020)             9

                      Opinion of the Court

                         *     *     *
  We conclude that RFRA’s express remedies provision per-
mits litigants, when appropriate, to obtain money damages
against federal officials in their individual capacities. The
judgment of the United States Court of Appeals for the Sec-
ond Circuit is affirmed.
                                              It is so ordered.

  JUSTICE BARRETT took no part in the consideration or
decision of this case.

```

---
