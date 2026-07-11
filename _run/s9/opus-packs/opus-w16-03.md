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

## GROUP: _overhaul2/lake/cases/United States v. Harris (1971).json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Harris (1971)"
type: case
citation: "403 U.S. 573 (1971)"
parallel_cite: "91 S. Ct. 2075; 29 L. Ed. 2d 723"
neutral_cite: 1971 U.S. LEXIS 18
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-06-28
docket: 30
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "United States v. Harris (1971)"
  varies_by_point: false
  scope_note: "The penal-interest reliability principle survives — a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108379/united-states-v-harris/"
  cluster_id: 108379
  opinion_id: 108379
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Progeny"
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Related (cross-doctrine)"
related: ["[[Aguilar v. Texas]]", "[[Spinelli v. United States]]", "[[Illinois v. Gates]]"]
aliases: ["United States v. Harris"]
tags: ["case", "fourth-amendment", "probable-cause", "informant", "warrant-requirement"]
holding: "An informant's statement against his penal interest is itself an indicium of reliability that can support probable cause for a warrant; admissions of crime 'carry their own indicia of credibility,' and a magistrate may also rely on an officer's knowledge of the suspect's reputation."
lake:
  record_id: "United States v. Harris (1971)"
  status: verified
  projected_at: 2026-07-09
---

# United States v. Harris (1971)

*403 U.S. 573 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A federal tax investigator obtained a warrant to search Harris's premises for nontaxpaid liquor. The affidavit recited the affiant's knowledge of Harris's longstanding reputation as a trafficker in illicit whiskey and a tip from a confidential informant — who feared for his safety — stating that he had repeatedly, and recently, purchased illicit whiskey at the premises over the past two years. The Court of Appeals held the affidavit insufficient under *[[Aguilar v. Texas]]* and *[[Spinelli v. United States]]*.

## Issue
May an informant's tip support probable cause for a warrant where it is corroborated by the affiant's knowledge of the suspect's reputation and by the informant's own admission — against his penal interest — of buying illicit whiskey at the premises?

## Rule
Yes. The informant's statements "were against the informant's penal interest, for he thereby admitted major elements of an offense." Because "[p]eople do not lightly admit a crime and place critical evidence in the hands of the police in the form of their own admissions," such "[a]dmissions of crime, like admissions against proprietary interests, carry their own indicia of credibility — sufficient at least to support a finding of probable cause to search." — 403 U.S. at 583. ^pin-583

"That the informant may be paid or promised a 'break' does not eliminate the residual risk and opprobrium of having admitted criminal conduct." — *Id.* at 584. ^pin-584

The admission of long-running illicit purchases "itself and without more, implicated that property and furnished probable cause to search." — [*Id.*](https://www.courtlistener.com/opinion/108379/united-states-v-harris/#:~:text=itself%20and%20without%20more%2C%20implicated) ^pin-584b

A magistrate may likewise rely on an officer's knowledge of a suspect's reputation as a "practical consideration of everyday life." — *Id.* at 583. ^pin-583b

## Application
The informant admitted repeatedly buying unstamped whiskey from Harris — major elements of a federal offense — so his tip carried its own credibility, undiminished by any payment or promised leniency, and standing alone furnished probable cause to search the premises. The affiant's knowledge of Harris's reputation as a bootlegger added further support. Read commonsensically rather than under a rigid two-pronged formula, the affidavit established probable cause.

## Conclusion
The affidavit established probable cause and the warrant was valid; the judgment below was reversed. (The Chief Justice's opinion was fractured, but a majority agreed with Part III's penal-interest rationale.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The penal-interest reliability principle remains valid and is a recognized factor in assessing an informant's credibility. The *[[Aguilar v. Texas|Aguilar]]*–*[[Spinelli v. United States|Spinelli]]* two-pronged test that this plurality was already eroding was later abandoned for a totality-of-the-circumstances inquiry in [[Illinois v. Gates]] (1983), within which *Harris*'s penal-interest insight survives. No negative treatment of *Harris* itself.

## Appears on
- [[Probable Cause]] — *Progeny*
- [[Probable Cause in the Affidavit]] — *Related (cross-doctrine)*

## Sources
- *United States v. Harris*, 403 U.S. 573 (1971) — https://www.courtlistener.com/opinion/108379/united-states-v-harris/ — pinpoints: 583, 584.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c9a2c479526ca83b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Harris (1971)"}, "payload": {"all": [{"cite": "403 U.S. 573", "page": "573", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "403"}, {"cite": "91 S. Ct. 2075", "page": "2075", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "29 L. Ed. 2d 723", "page": "723", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "29"}, {"cite": "1971 U.S. LEXIS 18", "page": "18", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}], "display": "403 U.S. 573", "official": {"cite": "403 U.S. 573", "page": "573", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "403"}, "official_selection_present": true, "record_id": "United States v. Harris (1971)"}}
{"assertion_id": "6e24a38839854716", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-583b", "record_id": "United States v. Harris (1971)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-583b", "pinpoint_status": "slip-only", "quote": "practical consideration of everyday life.", "quote_fidelity": "mismatch", "record_id": "United States v. Harris (1971)", "star_marker": null}}
{"assertion_id": "8dc4e536331a7103", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-583", "record_id": "United States v. Harris (1971)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-583", "pinpoint_status": "slip-only", "quote": "--- # United States v. Harris (1971) *403 U.S. 573 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A federal tax investigator obtained a warrant to search Harris's premises for nontaxpaid liquor. The affidavit recited the affiant's knowledge of Harris's longstanding reputation as a trafficker in illicit whiskey and a tip from a confidential informant — who feared for his safety — stating that he had repeatedly, and recently, purchased illicit whiskey at the premises over the past two years. The Court of Appeals held the affidavit insufficient under *Aguilar v. Texas* and *Spinelli v. United States*. ## Issue May an informant's tip support probable cause for a warrant where it is corroborated by the affiant's knowledge of the suspect's reputation and by the informant's own admission — against his penal interest — of buying illicit whiskey at the premises? ## Rule Yes. The informant's statements", "quote_fidelity": "mismatch", "record_id": "United States v. Harris (1971)", "star_marker": null}}
{"assertion_id": "9ffd56142be0f1e7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-584", "record_id": "United States v. Harris (1971)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-584", "pinpoint_status": "slip-only", "quote": "That the informant may be paid or promised a 'break' does not eliminate the residual risk and opprobrium of having admitted criminal conduct.", "quote_fidelity": "mismatch", "record_id": "United States v. Harris (1971)", "star_marker": null}}
{"assertion_id": "e7985ddb49af353d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-584b", "record_id": "United States v. Harris (1971)"}, "payload": {"fragment": "#:~:text=itself%20and%20without%20more%2C%20implicated", "page": null, "pin_id": "pin-584b", "pinpoint_status": "star-verified", "quote": "itself and without more, implicated that property and furnished probable cause to search.", "quote_fidelity": "matched", "record_id": "United States v. Harris (1971)", "star_marker": "584"}}
{"assertion_id": "d83e4ca7d33163c2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Harris (1971)"}, "payload": {"as_of_content": "1971-06-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Harris (1971)", "scope_note": "The penal-interest reliability principle survives — a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983).", "varies_by_point": false}}
```

### lake record — United States v. Harris (1971)

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Harris (1971)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Harris",
    "case_name_short": "Harris",
    "case_name_full": "United States v. Harris",
    "input_case_name": "United States v. Harris (1971)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-06-28",
    "year": 1971,
    "docket": "30",
    "cluster_id": 108379,
    "lead_opinion_id": 108379,
    "sibling_ids": [
      108379,
      9883118,
      9883119,
      9883120,
      9883121
    ],
    "absolute_url": "/opinion/108379/united-states-v-harris/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "403 U.S. 573",
      "volume": "403",
      "reporter": "U.S.",
      "page": "573",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 2075",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2075",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 723",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 18",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "403 U.S. 573",
        "volume": "403",
        "reporter": "U.S.",
        "page": "573",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 2075",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "2075",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 2d 723",
        "volume": "29",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 18",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "403 U.S. 573",
    "official_selection": {
      "court_class": "scotus",
      "selected": "403 U.S. 573",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-583",
      "page": null,
      "quote": "--- # United States v. Harris (1971) *403 U.S. 573 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A federal tax investigator obtained a warrant to search Harris's premises for nontaxpaid liquor. The affidavit recited the affiant's knowledge of Harris's longstanding reputation as a trafficker in illicit whiskey and a tip from a confidential informant \u2014 who feared for his safety \u2014 stating that he had repeatedly, and recently, purchased illicit whiskey at the premises over the past two years. The Court of Appeals held the affidavit insufficient under *Aguilar v. Texas* and *Spinelli v. United States*. ## Issue May an informant's tip support probable cause for a warrant where it is corroborated by the affiant's knowledge of the suspect's reputation and by the informant's own admission \u2014 against his penal interest \u2014 of buying illicit whiskey at the premises? ## Rule Yes. The informant's statements",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-584",
      "page": null,
      "quote": "That the informant may be paid or promised a 'break' does not eliminate the residual risk and opprobrium of having admitted criminal conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-584b",
      "page": null,
      "quote": "itself and without more, implicated that property and furnished probable cause to search.",
      "star_marker": "584",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26583,
      "fragment": "#:~:text=itself%20and%20without%20more%2C%20implicated",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-583b",
      "page": null,
      "quote": "practical consideration of everyday life.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Harris (1971)",
    "varies_by_point": false,
    "scope_note": "The penal-interest reliability principle survives \u2014 a declaration against penal interest remains a recognized indicium of an informant's reliability, carried forward into the totality-of-the-circumstances test. The Aguilar-Spinelli two-pronged framework this plurality was eroding was later replaced by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brundidge",
          "cluster_id": 73678,
          "cite": [
            "170 F.3d 1350",
            "1999 U.S. App. LEXIS 5958",
            "1999 WL 181850"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence D. Lamorie Patricia L. Lamorie",
          "cluster_id": 729724,
          "cite": [
            "100 F.3d 547",
            "1996 U.S. App. LEXIS 28984",
            "1996 WL 637645"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hackleman v. State",
          "cluster_id": 2459738,
          "cite": [
            "919 S.W.2d 440",
            "1996 WL 60451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lauren Eric Wilhelm",
          "cluster_id": 715677,
          "cite": [
            "80 F.3d 116",
            "1996 U.S. App. LEXIS 6245",
            "1996 WL 149356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Czuprynski",
          "cluster_id": 656589,
          "cite": [
            "8 F.3d 1113",
            "1993 WL 454161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mellan",
          "cluster_id": 8717546,
          "cite": [
            "817 F. Supp. 1072"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane1_negative"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Mississippi",
          "cluster_id": 108718,
          "cite": [
            "35 L. Ed. 2d 297",
            "93 S. Ct. 1038",
            "410 U.S. 284",
            "1973 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Melson",
          "cluster_id": 2442934,
          "cite": [
            "638 S.W.2d 342",
            "1982 Tenn. LEXIS 431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 5687957,
          "cite": [
            "66 N.Y.2d 398",
            "488 N.E.2d 439",
            "497 N.Y.S.2d 618",
            "1985 N.Y. LEXIS 17918"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bower v. State",
          "cluster_id": 1625069,
          "cite": [
            "769 S.W.2d 887",
            "1989 Tex. Crim. App. LEXIS 6",
            "1989 WL 4325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1690639,
          "cite": [
            "709 So. 2d 512",
            "1998 WL 114500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randolph Jakobetz",
          "cluster_id": 577111,
          "cite": [
            "955 F.2d 786",
            "34 Fed. R. Serv. 876",
            "1992 U.S. App. LEXIS 322",
            "1992 WL 2126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bartolomeo",
          "cluster_id": 5684916,
          "cite": [
            "53 N.Y.2d 225",
            "423 N.E.2d 371",
            "440 N.Y.S.2d 894",
            "1981 N.Y. LEXIS 2477"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martin F. Burke",
          "cluster_id": 328036,
          "cite": [
            "517 F.2d 377",
            "1975 U.S. App. LEXIS 14661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Mills Stanert",
          "cluster_id": 452155,
          "cite": [
            "762 F.2d 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Frank Diecidue, Larry Neil Miller, Frank Boni, Jr., A/K/A \"Mustache Frankie,\" Manuel Gispert, Anthony Antone, and Homer Rex Davis",
          "cluster_id": 368882,
          "cite": [
            "603 F.2d 535",
            "4 Fed. R. Serv. 1294",
            "1979 U.S. App. LEXIS 11494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Martin",
          "cluster_id": 374716,
          "cite": [
            "615 F.2d 318",
            "1980 U.S. App. LEXIS 18767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lilly",
          "cluster_id": 1375322,
          "cite": [
            "461 S.E.2d 101",
            "194 W. Va. 595"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woodward v. State",
          "cluster_id": 2388927,
          "cite": [
            "668 S.W.2d 337",
            "1984 Tex. Crim. App. LEXIS 616"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
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
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warren G. Johnson",
          "cluster_id": 303789,
          "cite": [
            "461 F.2d 285",
            "1972 U.S. App. LEXIS 9023"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hanlon",
          "cluster_id": 5681186,
          "cite": [
            "36 N.Y.2d 549",
            "330 N.E.2d 631",
            "369 N.Y.S.2d 677",
            "1975 N.Y. LEXIS 1854"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 2467162,
          "cite": [
            "739 S.W.2d 813",
            "1987 Tex. Crim. App. LEXIS 739"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kirk C. Reivich",
          "cluster_id": 471842,
          "cite": [
            "793 F.2d 957",
            "1986 U.S. App. LEXIS 26468"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Arrington",
          "cluster_id": 1350177,
          "cite": [
            "319 S.E.2d 254",
            "311 N.C. 633",
            "1984 N.C. LEXIS 1750"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Couture",
          "cluster_id": 7891945,
          "cite": [
            "194 Conn. 530",
            "482 A.2d 300",
            "1984 Conn. LEXIS 695"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Harris (1971):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzQ0Mzg0MDAwMDAmcz0yMDY2NDIxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUmcz0yMTQxMDQzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108379 OR 9883118 OR 9883119 OR 9883120 OR 9883121)",
    "indexed_citing_opinions": 1258,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108379,
        "count": 1178,
        "count_source": "search"
      },
      {
        "opinion_id": 9883118,
        "count": 115,
        "count_source": "search"
      },
      {
        "opinion_id": 9883119,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883120,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9883121,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1806,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-harris-1971.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzMTc3MSZzPTQ2MjM2NjAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28108379+OR+9883118+OR+9883119+OR+9883120+OR+9883121%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108379,
        "cited_id": 97847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 277169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108379,
        "cited_id": 285442,
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
    "date_created": "2026-07-06T00:22:38Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:27:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:22:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Harris (1971)

```
<div>
<center><b><span class="citation" data-id="9883118"><a href="/opinion/108379/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">403 U.S. 573</a></span> (1971)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
HARRIS.</h1></center>
<center>No. 30.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 23, 1971</center>
<center>Decided June 28, 1971</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*574</span> <i>Beatrice Rosenberg</i> argued the cause for the United States. With her on the brief were <i>Solicitor General Griswold, Assistant Attorney General Wilson, Richard B. Stone,</i> and <i>Mervyn Hamburg.</i></p>
<p><i>Steven M. Umin,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./400/955/">400 U. S. 955</a></span>, argued the cause and filed a brief for respondent.</p>
<p><i>Frank G. Carrington, Jr.,</i> and <i>Alan S. Ganz</i> filed a brief for Americans for Effective Law Enforcement, Inc., as <i>amicus curiae</i> urging reversal.</p>
<p>MR. CHIEF JUSTICE BURGER announced the judgment of the Court and an opinion in which MR. JUSTICE BLACK and MR. JUSTICE BLACKMUN join, and in Part I of which <span class="star-pagination">*575</span> MR. JUSTICE STEWART joins, and in Part III of which MR. JUSTICE WHITE joins.</p>
<p>We granted certiorari in this case to consider the recurring question of what showing is constitutionally necessary to satisfy a magistrate that there is a substantial basis for crediting the report of an informant known to the police, but not identified to the magistrate, who purports to relate his personal knowledge of criminal activity.</p>
<p>In 1967 a federal tax investigator and a local constable entered the premises of respondent Harris, pursuant to a search warrant issued by a federal magistrate, and seized jugs of whiskey upon which the federal tax had not been paid. The warrant had been issued solely on the basis of the investigator's affidavit, which recited the following:</p>
<blockquote>"Roosevelt Harris has had a reputation with me for over 4 years as being a trafficker of nontaxpaid distilled spirits, and over this period I have received numerous information [<i>sic</i>] from all types of persons as to his activities. Constable Howard Johnson located a sizeable stash of illicit whiskey in an abandoned house under Harris' control during this period of time. This date, I have received information from a person who fears for their [<i>sic</i>] life and property should their name be revealed. I have interviewed this person, found this person to be a prudent person, and have, under a sworn verbal statement, gained the following information: This person has personal knowledge of and has purchased illicit whiskey from within the residence described, for a period of more than 2 years, and most recently within the past 2 weeks, has knowledge of a person who purchased illicit whiskey within the past two days from the house, has personal knowledge that the illicit whiskey is consumed by purchasers in the outbuilding known as and utilized as <span class="star-pagination">*576</span> the `dance hall,' and has seen Roosevelt Harris go to the other outbuilding, located about 50 yards from the residence, on numerous occasions, to obtain the whiskey for this person and other persons."</blockquote>
<p>Respondent was subsequently charged with possession of nontaxpaid liquor, in violation of <span class="citation no-link">26 U. S. C. § 5205</span> (a) (2). His pretrial motion to suppress the seized evidence on the ground that the affidavit was insufficient to establish probable cause was overruled, and he was convicted after a jury trial and sentenced to two years' imprisonment. The Court of Appeals for the Sixth Circuit reversed the conviction, holding that the information in the affidavit was insufficient to enable the magistrate to assess the informant's reliability and trustworthiness. <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d 796, 797</a></span> (1969).</p>
<p>The Court of Appeals relied on <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), in which we held that an affidavit based solely on the hearsay report of an unidentified informant must set forth "some of the underlying circumstances from which the officer concluded that the informant . . . was `credible' or his information `reliable.' " <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><i>Id.,</i> at 114</a></span>. It concluded that the affidavit was insufficient because no information was presented to enable the magistrate to evaluate the informant's reliability or trustworthiness. The court noted the absence of any allegation that the informant was a "truthful" person, but only an allegation that the informant was "prudent." Having found the informant's tip inadequate under <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> the court of Appeals, relying on <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), looked to the remaining allegations of the affidavit to determine whether they provided independent corroboration of the informant. The Court of Appeals held that the constable's prior discovery of a cache on respondent's property within the previous four years was too remote, and, <span class="star-pagination">*577</span> citing certain language from <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> it gave no weight whatever to the assertion that respondent had a general reputation known to the officer as a trafficker in illegal whiskey.</p>
<p>For the reasons stated below, we reverse the judgment of the Court of Appeals and reinstate the judgment of conviction.</p>
<p></p>
<h2>I</h2>
<p>In evaluating the showing of probable cause necessary to support a search warrant, against the Fourth Amendment's prohibition of unreasonable searches and seizures, we would do well to heed the sound admonition of <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> (1965):</p>
<blockquote>"[T]he Fourth Amendment's commands, like all constitutional requirements, are practical and not abstract. If the teachings of the Court's cases are to be followed and the constitutional policy served, affidavits for search warrants, such as the one involved here, must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. They are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area. A grudging or negative attitude by reviewing courts toward warrants will tend to discourage police officers from submitting their evidence to a judicial officer before acting." <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 108</a></span>.</blockquote>
<p><i>Aguilar</i> in no way departed from these sound principles. There a warrant was issued on nothing more than an affidavit reciting:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin, marijuana, <span class="star-pagination">*578</span> barbiturates and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#109" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span>.</blockquote>
<p>The affidavit, therefore, contained none of the underlying "facts or circumstances" from which the magistrate could find probable cause. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41, 47</a></span> (1933). On the contrary, the affidavit was a "mere affirmation of suspicion and belief" (<span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States"><i>Nathanson, supra,</i> at 46</a></span>) and gained nothing by the incorporation by reference of the informant's unsupported belief. See <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar, supra,</a></span></i> at 114 n. 4.</p>
<p>Significantly, the Court in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> cited with approval the affidavit upheld in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). That affidavit read in pertinent part as follows:</p>
<blockquote>"In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [<i>sic</i>] in the above mentioned places. The last time being August 20, 1957." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 267-268, n. 2</a></span>.</blockquote>
<p>The substance of the tip, held sufficient in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> closely parallels that here held insufficient by the Court <span class="star-pagination">*579</span> of Appeals. Both recount personal and recent<sup>[*]</sup> observations by an unidentified informant of criminal activity, factors showing that the information had been gained in a reliable manner, and serving to distinguish both tips from that held insufficient in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli, supra,</a></span></i> in which the affidavit failed to explain how the informant came by his information. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 416</a></span>.</p>
<p>The Court of Appeals seems to have believed, however, that there was no substantial basis for believing that the tip was truthful. Indeed, it emphasized that the affiant had never alleged that the informant was truthful, but only "prudent," a word that "signifies that he is circumspect in the conduct of his affairs, but reveals nothing about his credibility." <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d, at 797-798</a></span>. Such a construction of the affidavit is the very sort of hypertechnicalitythe "elaborate specificity once exacted under common law"condemned by this Court in <i><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">Ventresca</a></span>.</i> A policeman's affidavit "should not be judged as an entry in an essay contest," <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#438" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 438</a></span> (Fortas, J., dissenting), but, rather, must be judged by the facts it contains. While a bare statement by an affiant that he believed the informant to be truthful would not, in itself, provide a <i>factual</i> basis for crediting the report of an unnamed informant, we conclude that the affidavit in the present case contains an ample factual basis for believing the informant which, when coupled <span class="star-pagination">*580</span> with affiant's own knowledge of the respondent's background, afforded a basis upon which a magistrate could reasonably issue a warrant. The accusation by the informant was plainly a declaration against interest since it could readily warrant a prosecution and could sustain a conviction against the informant himself. This will be developed in Part III.</p>
<p></p>
<h2>II</h2>
<p>In determining what quantum of information is necessary to support a belief that an unidentified informant's information is truthful, <i>Jones</i> v. <i>United States, supra</i><i>,</i> is a suitable benchmark. The affidavit in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> recounted the tip of an anonymous informant, who claimed to have recently purchased narcotics from the defendant at his apartment, and described the apartment in some detail. After reciting the substance of the tip the affiant swore as follows:</p>
<blockquote>"Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.</blockquote>
<blockquote>"This same information, regarding the illicit narcotic traffic, conducted by [the defendant] has been given to the undersigned and to other officers of the narcotic squad by other sources of information.</blockquote>
<blockquote>"Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [<i>sic</i>] in the above apartment . . . ." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Id.,</a></span></i> at 268 n. 2.</blockquote>
<p>Mr. Justice Frankfurter, writing for the Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> upheld the warrant. Although the information in the affidavit was almost entirely hearsay, he concluded that <span class="star-pagination">*581</span> there was "substantial basis" for crediting the hearsay. The informant had previously given accurate information; his story was corroborated by "other sources" (albeit unnamed); additionally the defendant was known to the police as a user of narcotics. Justice Frankfurter emphasized the last two of these factors:</p>
<blockquote>"Corroboration through other sources of information reduced the chances of a reckless or prevaricating tale; that petitioner was a known user of narcotics made the charge against him much less subject to scepticism than would be such a charge against one without such a history." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 271</a></span>.</blockquote>
<p><i>Aguilar</i> cannot be read as questioning the "substantial basis" approach of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i> And unless <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> has somehow, without acknowledgment, been overruled by <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> there would be no basis whatever for a holding that the affidavit in the present case is wanting. The affidavit in the present case, like that in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> contained a substantial basis for crediting the hearsay. Both affidavits purport to relate the personal observations of the informanta factor that clearly distinguishes <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> in which the affidavit failed to explain how the informant came by his information. Both recite prior events within the affiant's own knowledgethe needle marks in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and Constable Johnson's prior seizure in the present caseindicating that the defendant had previously trafficked in contraband. These prior events again distinguish <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> in which no facts were supplied to support the assertion that Spinelli was "known . . . as a bookmaker, an associate of bookmakers, a gambler, and an associate of gamblers." <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#422" aria-description="Citation for case: Spinelli v. United States"><i>Spinelli, supra,</i> at 422</a></span>.</p>
<p>To be sure there is no averment in the present affidavit, as there was in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> that the informant had previously given "correct information," but this Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> never suggested that an averment of previous reliability was <span class="star-pagination">*582</span> necessary. Indeed, when the inquiry is, as it always must be in determining probable cause, whether the informant's <i>present</i> information is truthful or reliable, it is curious, at the very least, that MR. JUSTICE HARLAN would place such stress on vague attributes of "general background, employment . . . position in the community. . . ." (<i>Post,</i> at 600.) Were it not for some language in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> it is doubtful that any of these reputation attributes of the informant could be said to reveal any more about his present reliability than is afforded by the support of the officer's personal knowledge of the suspect. In <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>,</i> however, the Court rejected as entitled to no weight the "bald and unilluminating" assertion that the suspect was known to the affiant as a gambler. <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 414</a></span>. For this proposition the Court relied on <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). But a careful examination of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> shows that the <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> opinion did not fully reflect the critical points of what <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held since it was limited to holding that reputation, <i>standing alone,</i> was insufficient; it surely did not hold it irrelevant when supported by other information. This reading of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is confirmed by <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), in which the Court, in sustaining a finding of probable cause for a warrantless arrest, held proper the assertion of the searching officer that he had previously arrested the defendant for a similar offense and that the defendant had a reputation for hauling liquor. Such evidence would rarely be admissible at trial, but the Court took pains to emphasize the very different functions of criminal trials and preliminary determinations of probable cause. Trials are necessarily surrounded with evidentiary rules "developed to safeguard men from dubious and unjust convictions." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 174</a></span>. But before the trial we deal only with probabilities that "are not technical, they are the factual and practical considerations of <span class="star-pagination">*583</span> everyday life on which reasonable and prudent men, not legal technicians, act." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States"><i>Brinegar, supra,</i> at 175</a></span>.</p>
<p>We cannot conclude that a policeman's knowledge of a suspect's reputationsomething that policemen frequently know and a factor that impressed such a "legal technician" as Mr. Justice Frankfurteris not a "practical consideration of everyday life" upon which an officer (or a magistrate) may properly rely in assessing the reliability of an informant's tip. To the extent that <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span></i> prohibits the use of such probative information, it has no support in our prior cases, logic, or experience and we decline to apply it to preclude a magistrate from relying on a law enforcement officer's knowledge of a suspect's reputation.</p>
<p></p>
<h2>III</h2>
<p>Quite apart from the affiant's own knowledge of respondent's activities, there was an additional reason for crediting the informant's tip. Here the warrant's affidavit recited extrajudicial statements of a declarant, who feared for his life and safety if his identity was revealed, that over the past two years he had many times and recently purchased "illicit whiskey." These statements were against the informant's penal interest, for he thereby admitted major elements of an offense under the Internal Revenue Code. Section 5205 (a) (2), Title 26, United States Code, proscribes the sale, purchase, or possession of unstamped liquor.</p>
<p>Common sense in the important daily affairs of life would induce a prudent and disinterested observer to credit these statements. People do not lightly admit a crime and place critical evidence in the hands of the police in the form of their own admissions. Admissions of crime, like admissions against proprietary interests, carry their own indicia of credibilitysufficient at least to support a finding of probable cause to search. That the informant may be paid or promised a "break" does <span class="star-pagination">*584</span> not eliminate the residual risk and opprobrium of having admitted criminal conduct. Concededly admissions of crime do not always lend credibility to contemporaneous or later accusations of another. But here the informant's admission that over a long period and currently he had been buying illicit liquor on certain premises, itself and without more, implicated that property and furnished probable cause to search.</p>
<p>It may be that this informant's out-of-court declarations would not be admissible at respondent's trial under <i>Donnelly</i> v. <i>United States,</i> <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243</a></span> (1913), or under <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">391 U. S. 123</a></span> (1968). But <i>Donnelly's</i> implication that statements against penal interest are without value and <i>per se</i> inadmissible has been widely criticized; see the dissenting opinion of Mr. Justice Holmes in <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/#277" aria-description="Citation for case: Donnelly v. United States"><i>Donnelly, supra,</i> at 277</a></span>; 5 J. Wigmore, Evidence § 1477 (3d ed. 1940), and has been partially rejected in Rule 804 of the Proposed Rules of Evidence for the District Courts and Magistrates. More important, the issue in warrant proceedings is not guilt beyond reasonable doubt but probable cause for believing the occurrence of a crime and the secreting of evidence in specific premises. See <i>Brinegar</i> v. <i>United States, supra,</i> at 173. Whether or not <i><span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">Donnelly</a></span></i> is to survive as a rule of evidence in federal trials, it should not be extended to warrant proceedings to prevent magistrates from crediting, in all circumstances, statements of a declarant containing admissions of criminal conduct. As for <i><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span>,</i> that case rested on the Confrontation Clause of the Sixth Amendment which seems inapposite to <i>ex parte</i> search warrant proceedings under the Fourth Amendment.</p>
<p>It will not do to say that warrants may not issue on uncorroborated hearsay. This only avoids the issue of whether there is reason for crediting the out-of-court statement. Nor is it especially significant that neither <span class="star-pagination">*585</span> the name nor the person of the informant was produced before the magistrate. The police themselves almost certainly knew his name, the truth of the affidavit is not in issue, and <i>McCray</i> v. <i>Illinois,</i> <span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967), disposed of the claim that the informant must be produced whenever the defendant so demands.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE STEWART joins in Part I of THE CHIEF JUSTICE'S opinion and in the judgment of the Court.</p>
<p>MR. JUSTICE WHITE agrees with Part III of THE CHIEF JUSTICE'S opinion and has concluded that the affidavit, considered as a whole, was sufficient to support issuance of the warrant. He therefore concurs in the judgment of reversal.</p>
<p>MR. JUSTICE BLACK, concurring.</p>
<p>While I join the opinion of THE CHIEF JUSTICE which distinguishes this case from <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), I would go further and overrule those two cases and wipe their holdings from the books for the reasons, among others, set forth in the dissent of Mr. Justice Clark in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> which I joined, and my dissent in <i><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">Spinelli</a></span>.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the opinion of THE CHIEF JUSTICE and the judgment of the Court, but I add a personal comment in order to make very clear my posture as to <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), cited in several places in that opinion. I was a member of the 6-2 majority of the United States Court of Appeals for the Eighth Circuit in <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9452981"><a href="/opinion/277169/william-spinelli-v-united-states/" aria-description="Citation for case: William Spinelli v. United States">382 F. 2d 871</a></span> (1967), which this Court by a 5-3 vote reversed, with the pivotal Justice concluding his concurring <span class="star-pagination">*586</span> opinion, <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#429" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 429</a></span>, by the observation that, "Pending full-scale reconsideration of that case [<i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959)], on the one hand, or of the <i>Nathanson-Aguilar</i> cases on the other, I join the opinion of the Court and the judgment of reversal, especially since a vote to affirm would produce an evenly divided Court." Obviously, I then felt that the Court of Appeals had correctly decided the case. Nothing this Court said in <i>Spinelli</i> convinced me to the contrary. I continue to feel today that <i>Spinelli</i> at this level was wrongly decided and, like MR. JUSTICE BLACK, I would overrule it.</p>
<p>MR. JUSTICE HARLAN, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>This case presents the question of how our decisions in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), apply where magistrates in issuing search warrants are faced with the task of assessing the probable credibility of unidentified informants who purport to describe criminal activity of which they have personal knowledge, and where it does not appear that such informants have previously supplied accurate information to law enforcement officers.</p>
<p>I cannot agree that the affidavit here at issue provided a sufficient basis for an independent determination, by a neutral judicial officer, that probable cause existed. Accordingly, I would affirm the judgment of the Court of Appeals. Five members of this Court, however, for four separately expressed reasons, have concluded that the judgment below must be reversed. Some of the theories employed by those voting to reverse are wholly unlike any of the grounds urged by the Government.</p>
<p></p>
<h2>
<span class="star-pagination">*587</span> I</h2>
<p>Where, as in this case, the affiant states under oath that he has been informed of the existence of certain criminal activity, but has not observed that activity himself, a magistrate in discharging his duty to make an independent assessment of probable cause can properly issue a search warrant only if he concludes that; (a) the knowledge attributed to the informant, if true, would be sufficient to establish probable cause; (b) the affiant is likely relating truthfully what the informer said; and (c) it is reasonably likely that the informer's description of criminal behavior accurately reflects reality.<sup>[1]</sup></p>
<p>In the case before us, no one maintains that the magistrate's judgment as to elements (a) and (b) was not properly supported. Plainly the information set forth in the affidavit, if entitled to credit, establishes probable cause. And the magistrate was certainly entitled to rely on the agent's official status, his personal observation of the agent, and the oath administered to him by the magistrate in concluding that the affiant's assertions as to what he had been told by the informer were credible.</p>
<p>The final component of the probable cause equation, here involved, is that it must appear reasonably likely that the informer's claim that criminal conduct has occurred or is occurring is probably accurate. Our <span class="star-pagination">*588</span> cases establish that this element is satisfied only if there is reason to believe both that the informer is a truthful person generally and that he has based his particular conclusions in the matter at hand on reliable data, <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>; </i><i>Spinelli</i> v. <i>United States, supra</i><i>,</i> for it is not reasonable to invade another's premises on the basis of information, even if it appears quite damning when simply taken at face value, unless there is corroboration of its trustworthiness. The fact that the magistrate has determined that the agent probably truthfully reported what the informant conveyed cannot, of course, establish the credibility or reliability of the information itself. More immediately relevant here, our cases have established that where the affiant relies upon the assertions of confidants to establish probable cause, the affidavit must set forth facts which enable the magistrate to judge for himself both the probable credibility of the informant and the reliability of his information, for only if this condition is met can a reviewing court be satisfied that the magistrate has fulfilled his constitutional duty to render an independent determination that probable cause exists. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). Cf. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958); <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933); <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971).<sup>[2]</sup></p>
<p>The parties are in agreement with these principles and have not urged that they be re-examined. Indeed, I think these precepts follow ineluctably from the constitutional command that "no Warrants shall issue, but upon probable cause." Whether, in this case, either of <span class="star-pagination">*589</span> these tests of the trustworthiness of the informer's tip has been met is, however, vigorously disputed.</p>
<p></p>
<h2>II</h2>
<p>Although the Court of Appeals did not address itself to this contention, respondent claims that the affidavit is insufficient to establish the reliability of the evidence upon which the informant based his conclusions. Of course, most of these data come from alleged direct personal observation of the informant, surely a sufficient basis upon which to predicate a finding of reliability under any test. However, respondent stresses that the allegation of direct observation of the criminal activity does not necessarily purport to embrace a period less than two weeks prior to the issuance of the search warrant. Moreover, the reliability of the source of the information that a purchase was made "within the past two days" is not established and, it is argued, the other information was too stale to support the issuance of a warrant.</p>
<p>This argument is premised upon an overly technical view of the affidavit. The informant is said to have personally bought illegal whiskey from respondent "within the past 2 weeks," which could well include a point in time quite close to the issuance of the warrant. More importantly, the totality of the tip evidently reveals that the informer purported to describe an ongoing operation which he claimed he had personally observed over the course of two years. Giving due deference to the magistrate's determination of probable cause and reading the affidavit "in a commonsense and realistic fashion," <i>United States</i> v. <i>Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#108" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 108</a></span> (1965), I must conclude that the affidavit sets forth sufficient data to permit a magistrate to determine that, if the informer was likely telling the truth, information adequate to support a finding of probable cause was likely obtained in a reliable fashion.</p>
<p></p>
<h2>
<span class="star-pagination">*590</span> III</h2>
<p>I turn, then, to what the parties have treated as the crux of the controversy before us. Respondent contends, and the Court of Appeals so held, that the affidavit does not sufficiently set forth facts and circumstances from which the magistrate might properly have concluded that the informant, in purporting to detail his personal observation, was probably telling the truth. Conversely, the Government principally argues that two factors, singly or in combination, provided a factual basis for the magistrate's judgment that the tip was credible. First, the agent stated that he had "interviewed this person [and] found this person to be a prudent person." Second, the informant described the criminal activity in some detail and from his own personal knowledge.<sup>[3]</sup></p>
<p></p>
<h2>A</h2>
<p>The Government's first contention misconceives the basic thrust of this Court's decisions in the <i>Nathanson, Giordenello, Aguilar, Spinelli,</i> and <i><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span></i> cases, <i>supra.</i> The central proposition common to each of these decisions is that the determination of probable cause is to be made by the magistrate, not the affiant. That the agent-affiant determined the informer to be prudent cannot be a basis for sustaining this warrant unless magistrates are entitled to delegate their responsibilities to law enforcement officials. <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held that an affidavit <span class="star-pagination">*591</span> to the effect that the affiant "has cause to suspect and does believe" that illicit liquor was located on certain premises did not sufficiently apprise the issuing magistrate of the underlying "facts or circumstances" from which "<i>he</i> can find probable cause." <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S., at 47</a></span> (emphasis added). In <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> a sworn assertion that the informant was "a credible person" was held insufficient to enable the magistrate to assess that conclusion for himself. Only two Terms ago, we held a warrant constitutionally defective because "[t]hough the affiant swore that his confidant was `reliable,' he offered the magistrate no reason in support of this conclusion." <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>. Reading the assertion that the informer in this case was "prudent" in the broadest conceivable commonsense fashion, it does no more than claim he was "credible" or "reliable," <i>i. e.,</i> that he was likely telling the truth.<sup>[4]</sup> Such an assertion, however, is no more than a conclusion which the Constitution requires must be drawn independently by the magistrate. What this portion of the affidavit lacks are any of the underlying "facts or circumstances" that informed the agent's conclusion and whose presentation to the magistrate would enable him to assess the probability that this determination was sufficiently plausible to justify authorizing a search of respondent's premises.</p>
<p></p>
<h2>B</h2>
<p>Nor do I think this void is filled by the fact that the informant claimed to speak from his personal knowledge. <span class="star-pagination">*592</span> It is true that in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> the Court was not dealing with the sufficiency of the allegations respecting one or more of the above-described components of probable cause, but merely with a bare overall statement of the affiant that probable cause existed. Further, as the Government notes, our chief, but not sole, emphasis in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> was upon the absence of any evidence communicated by the affiant from which a magistrate could infer that the confidant gathered his evidence from a reliable source. From this, the Government contends that <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i>'s reliability-of-the-informer test is not applicable in full force where, as here, it does seem clear that the sources of the informer's belief, if truthfully reported, were reliable. I think this argument makes too much of the circumstances of our previous cases. The central point of the discussion of probable cause in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> is, as perhaps more precisely emphasized by our explicit twin holdings in <i>Spinelli,</i> see <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#416" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 416</a></span>, that the two elements necessary to establish the informer's trustworthinessnamely, that the tip relayed to the magistrate be both truthful and reliableare analytically severable. It is not possible to argue that since certain information, if true, would be trustworthy, therefore, it must be true. The possibility remains that the information might have been fabricated. This is why our cases require that there be a reasonable basis for crediting the accuracy of the observation related in the tip. In short, the requirement that the magistrate independently assess the probable credibility of the informant does not vanish where the source of the tip indicates that, if true, it is trustworthy.</p>
<p>This is not to say, however, that I think the fact of asserted personal observation can never play a role in determining whether that observation actually took place. I can perceive at least two ways in which, in circumstances <span class="star-pagination">*593</span> similar to those of this case, that information might be taken to bear upon the informer's credibility, as well as upon the reliability of his sources of information. For example, to the extent that the informant is somehow responsible to the affiant, the fact of asserted personal observation might be of some value to a magistrate in assessing the informer's credibility. In such circumstances, perhaps a magistrate could conclude that where the confidant claimed to speak from personal knowledge it is somewhat less likely that the informant was falsifying his report because, if the search yields no fruit, when called to account he would be unable to explain this away by impugning the veracity or reliability of his sources. However, no such relationship is revealed in this case.</p>
<p>Additionally, it might be of significance that the informant had given a more than ordinarily detailed description of the suspect's criminal activities. Although this would be more probative of the reliability of the information, it might also permissibly lead a magistrate, in an otherwise close case, to credit the accuracy of the account as well. I do not believe, however, that in this instance the relatively meager allegations of this character are, standing alone, enough to satisfy the credibility requirement essential to the sufficiency of this probable-cause affidavit. Reading this aspect of the affidavit in a not unduly circumspect manner, the allegations are of a character that would readily occur to a person prone to fabricate. To hold that this aspect of the affidavit, without more, would enable "a man of reasonable caution," <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#55" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 55</a></span> (1967), to conclude that there was adequate reason to believe the informant credible would open the door to the acceptance of little more than florid affidavits as justifying the issuance of search warrants.</p>
<p></p>
<h2>
<span class="star-pagination">*594</span> C</h2>
<p>Some members of the Court would reverse the judgment below on the grounds that the magistrate might properly have credited the informant's assertions because they confessed to the commission of a crime. This rationale is advanced notwithstanding the Government's failure even to suggest it.</p>
<p>Had this argument been pressed upon us, I would find it difficult to accept. First, the analogy to the hearsay exception is quite tenuous. The federal rule, although it is often criticized, is that declarations against penal interest do not fall within this exception. <i>Donnelly</i> v. <i>United States,</i> <span class="citation" data-id="97847"><a href="/opinion/97847/donnelly-v-united-states/" aria-description="Citation for case: Donnelly v. United States">228 U. S. 243</a></span> (1913). Moreover, because it has been thought that such statements should be relied upon by factfinders only when necessity justifies it, the rule universally requires a showing that the declarant cannot be produced personally before the trier of fact, C. McCormick, Evidence §§ 253, 257 (1954), an element not shown to be present here. See Part V, <i>infra.</i> Finally, we have not found any instance of the application of this rule where the witness declined to reveal to the trier of fact the identity of the declarant, presumably because without this knowledge it cannot be readily assumed that the declarant might have had reason to suspect the use of the statement would do him harm. Thus, while strict rules of evidence certainly do not govern magistrates' assessments of probable cause, it would require a rather extensive relaxation of them to permit reliance on this factor. And these rules cannot be completely relaxed, of course, since the basic thrust of <i>Spinelli, Aguilar, Nathanson, Whiteley,</i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello, supra,</a></span></i> is to prohibit the issuance of warrants upon mere uncorroborated hearsay. The simple statement by an affiant that an unspecified individual told the affiant that he and another had committed a <span class="star-pagination">*595</span> crime, where offered to prove the complicity of the third party, is little, if any, more than that.</p>
<p>Secondly, the rationale for this exception to the hearsay rule is that the fact that the declaration was against the speaker's self-interest tends to indicate that its substance is accurate. 5 J. Wigmore, Evidence § 1457 (3d ed. 1940). But where the declarant is also a police informant it seems at least as plausible to assume, without further enlightenment either as to the Government's general practice or as to the particular facts of this case, that the declarant-confidant at least believed he would receive absolution from prosecution for his confessed crime in return for his statement. (This, of course, would not be an objection where the declarant is not also the informant. See <i>Spinelli, supra,</i> at 425 (WHITE, J., concurring).) Thus, some showing that the informant did not possess illusions of immunity might well be essential.</p>
<p>Thirdly, the effect of adopting such a rule would be to encourage the Government to prefer as informants participants in criminal enterprises rather than ordinary citizens, a goal the Government specifically eschews in its brief in this case upon the explicit premise that such persons are often less reliable than those who obey the law. Brief for the United States 14.</p>
<p>In short, I am inclined to the view, although I would not decide the question here, that magistrates may not properly predicate a determination that an unnamed confidant is credible upon the bare fact that by giving information he also confessed to having committed a crime. More importantly at this juncture, it seems to me quite clear that no such rule should be injected into our federal jurisprudence in the absence of any representation by the Government that the factual assumptions underlying it do, indeed, comport with reality, and in the face of the Government's apparent explicit assertion, in this very <span class="star-pagination">*596</span> case, that those able to supply information sufficient to establish probable cause under such a new rule would tend to be less reliable than those who cannot. The necessity for this haste to embrace such a speculative theory, without any argument from those who will be affected by it, wholly escapes me.</p>
<p></p>
<h2>IV</h2>
<p>Finally, it is argued that even if the tip plus the affiant's assertion that the informant was "prudent" did not provide a reasonable basis for the magistrate's conclusion that the confidant was credible, two other factors would have sufficed. First, at some time in the past four or more years, in an abandoned house "under Harris' control," the local constable had located "a sizeable stash of illicit whiskey." While an assertion of "prior events within the affiant's own knowledge . . . indicating that the defendant had previously trafficked in contraband," <i>ante,</i> at 581, admittedly did not appear in the affidavit held insufficient in <i>Spinelli,</i> this hardly distinguishes that case in any purposeful manner. Surely, it cannot seriously be suggested that, once an individual has been convicted of bootlegging, any anonymous phone caller who states he has just personally witnessed another illicit sale (up to four years later) by that individual provides federal agents with probable cause to search the suspect's home. I can only conclude that this argument is a make-weight, intended to avoid the necessity of calling for an outright overruling of <i>Spinelli.</i></p>
<p>Secondly, the claim is made that a magistrate could conclude the confidant here was credible because the agent had "received numerous information from all types of persons as to [respondent's] activities." To rely on this factor alone, of course, is flatly inconsistent with <i>Spinelli,</i> where we held that "the allegation that Spinelli was `known' to the affiant and to other federal and local <span class="star-pagination">*597</span> law enforcement officers as a gambler and an associate of gamblers is but a bald and unilluminating assertion of suspicion that is entitled to no weight in appraising the magistrate's decision." <i>Spinelli, supra,</i> at 414. In the instant case, the affiant did not purport to "know" respondent was a dealer in illicit whiskey, nor did he identify the source of his information to that effect.</p>
<p>Nevertheless, the contention is advanced that this aspect of <i>Spinelli</i> had "no support in our prior cases, logic, or experience," <i>ante,</i> at 583, and thus should be discarded. However, <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> held that "[m]ere affirmance of belief or suspicion is not enough" to establish probable cause for issuance of a warrant to search a private dwelling. <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States">290 U. S., at 47</a></span>. It is argued that <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> "was limited to holding that reputation, <i>standing alone,</i> was insufficient." <i>Ante,</i> at 582. But this is the precise problem hereonly the respondent's reputation has been seriously invoked to establish the credibility of the informant, an element of probable cause entirely severable from the requirement that the confidant's source be reliable. See Parts I and III of this opinion.</p>
<p>A narrower view of <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is said to be confirmed by reading <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), to have "held proper the assertion of the searching officer that he had previously arrested the defendant for a similar offense and that the defendant had a reputation for hauling liquor." <i>Ante,</i> at 582. But <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> itself was very carefully limited to situations involving the arrest of those driving moving vehicles, <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 174, 176-177</a></span>, a problem that has typically been treated as <i>sui generis</i> by this Court. Further, the Court in <i><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">Brinegar</a></span></i> specifically held the arrest valid "[w]holly apart from [the agent's] knowledge that [the suspect] bore the general reputation of being engaged in liquor running." <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#170" aria-description="Citation for case: Brinegar v. United States"><i>Id.,</i> at 170</a></span>. While it is true that <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960), cites the fact that the informant's <span class="star-pagination">*598</span> "story was corroborated by other sources of information," the opinion nowhere suggests that this factor, standing alone, would have been sufficient to enable a magistrate to assess the confidant's reliability. At least equal emphasis was placed upon the informant's previously proved veracity and his tangible proof of actual observation of the illegal activity.</p>
<p>Thus, I conclude that <i>Spinelli</i> and <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>,</i> without contradiction, stand for the proposition that the magistrate could not establish the likely veracity of the unidentified informant on the grounds that his story coincided, in unspecified particulars, with rumors circulated by unknown third parties. I am not certain what is meant by the claim that such a rule of law is illogical. It would, indeed, be illogical to argue that the agent could not have relied upon information as to respondent's reputation that he deemed credible and reliable in concluding that the informant had likely told the truth. But it was not the agent's task to determine whether a search warrant should issue. This was the magistrate's responsibility. As to the magistrate, I confess that I do not comprehend, where the issue is whether the confidant is to be believed, how the agent's assertion that he had "received numerous information from all types of persons as to [respondent's] activities," can, as a matter of logic or experience, be accurately described as other than "a bald and unilluminating assertion of suspicion." It is, at best, a conclusory statement that respondent had a deserved reputation as a dealer in illicit whiskey. The Fourth Amendment, I repeat, requires that such conclusions be drawn, from the underlying facts and circumstances, by the magistrate, not the agent.</p>
<p></p>
<h2>V</h2>
<p>The Government has earnestly protested that the result below, if permitted to stand, will seriously hamper the <span class="star-pagination">*599</span> enforcement of the federal criminal law. It is said that if this affidavit is insufficient to support the issuance of a search warrant, it will be extremely difficult to meet the Fourth Amendment's standards where the informer, although apparently quite credible, has never before given accurate information to law enforcement officers, especially where he, or the agent, is unwilling to have the informant's identity disclosed. It would, indeed, be anomalous if the Fourth Amendment dictated such results, for it surely was never intended as a hindrance to fair, vigorous law enforcement. Further, I think there is much truth in the Government's supporting assertion that the ordinary citizen who has never before reported a crime to the police may, in fact, be more reliable than one who supplies information on a regular basis. "The latter is likely to be someone who is himself involved in criminal activity or is, at least, someone who enjoys the confidence of criminals." Government's Brief 14.<sup>[5]</sup></p>
<p>I do not, however, share the Government's concern that a judgment of affirmance would have such a constricting effect on legitimate federal law enforcement. For example, it would seem that such informers could often be brought before the magistrate where he could assess their credibility for himself. We cannot assume that the ordinary law-abiding citizen has qualms about this sort of cooperation with law enforcement officers. And I do not understand the Government to be asserting <span class="star-pagination">*600</span> that effective law enforcement will often dictate that the identity of informants be kept secret from federal magistrates themselves. Moreover, it will always be open to the officer to seek corroboration of the tip.</p>
<p>Beyond these considerations, I do not understand why a federal agent, who has determined a confidant to be "reliable," "credible," or "prudent" cannot lay before the magistrate the grounds upon which he based that judgment. I would not hold that a magistrate's determination that an informer is "prudent" is insufficient to support the issuance of a warrant. To the contrary, I would only insist that this judgment be that of the magistrate, not the law enforcement officer who seeks the warrant. Without violating the confidences of his source, the agent surely could describe for the magistrate such things as the informer's general background, employment, personal attributes that enable him to observe and relate accurately, position in the community, reputation with others, personal connection with the suspect, any circumstances which suggest the probable absence of any motivation to falsify, the apparent motivation for supplying the information, the presence or absence of a criminal record or association with known criminals, and the like.</p>
<p></p>
<h2>VI</h2>
<p>This affidavit is barren of anything that enabled the magistrate to judge for himself of the credibility of the informant. We should not countenance the issuance of a search warrant by a federal magistrate upon no more evidence than that presented here. A person who has not been shown to possess any of the common attributes of credibility, whose name cannot be disclosed to a magistrate, and whose information has not been corroborated is precisely the sort of informant whose tip should not be the sole basis for the issuance of a warrant, if the constitutional command that "no Warrants shall issue, but <span class="star-pagination">*601</span> upon probable cause" is to be respected. And the assertion that such a person may be believed where he confesses that he is a criminal or where his statements dovetail with other, unspecified rumors carries its own refutation. With all respect, such an analysis bespeaks more a firm hostility to <i>Aguilar, Nathanson,</i> and <i>Spinelli</i> than a careful judgment as to the principles those cases reflect. Despite all its surface detail, this affidavit cannot be sustained without cutting deeply into the core requirement of the Fourth Amendment that search warrants cannot issue except upon the independent finding of a neutral magistrate that probable cause exists.</p>
<p>For these reasons, I dissent.</p>
<h2>NOTES</h2>
<p>[*]  We reject the contention of respondent that the informant's observations were too stale to establish probable cause at the time the warrant was issued. The informant reported having purchased whiskey from respondent "within the past 2 weeks," which could well include purchases up to the date of the affidavit. Moreover, these recent purchases were part of a history of purchases over a two-year period. It was certainly reasonable for a magistrate, concerned only with a balancing of probabilities, to conclude that there was a reasonable basis for a search.</p>
<p>[1]  Of course where, as here, the affiant provides information in addition to the informant's tip, the magistrate could alternatively find probable cause, without examining the tip, if he can conclude that (a) the affiant is probably telling the truth and (b) the affidavit apart from the tip is sufficiently informative to establish probable cause. See <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/#414" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410, 414</a></span> (1969). Concededly, this latter element is not present here. Government's Brief 16. Without crediting the tip, the affidavit is insufficient.</p>
<p>[2]  <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> and <i><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">Whiteley</a></span></i> each involved an arrest warrant rather than a search warrant, but the analysis required to determine the validity of either is basically the same.</p>
<p>[3]  The Government makes brief reference to the assertion that the informant's verbal statement to the affiant was "sworn." Government's Brief 13 n. 2. I do not see how this affects the case. Surely there is no reason to suspect that this indicates the confidant anticipated potential perjury proceedings if he were subsequently proved a liar. Nor does that assertion reveal, in any meaningful sense, what sort of relationship this might have reflected or created between the agent and his informer.</p>
<p>[4]  The Court of Appeals in reversing respondent's conviction stated that "[t]he allegation that [the informant] is a `prudent person' signifies that he is circumspect in the conduct of his affairs, but reveals nothing about his credibility." <span class="citation" data-id="285442"><a href="/opinion/285442/united-states-v-roosevelt-hudson-harris/#797" aria-description="Citation for case: United States v. Roosevelt Hudson Harris">412 F. 2d 796, 797-798</a></span>. I consider this a too restrictive construction of the affidavit and cannot accept that aspect of the reasoning of the Court of Appeals.</p>
<p>[5]  Of course, the magistrate was presented no evidence that this is, in fact, such a case. Indeed, the very allegations in the affidavit to the effect that the informant here had been a frequent purchaser from respondent would suggest that he "is, at least, someone who enjoys the confidence of criminals." The Government's argument, as I understand it, is that the affidavit in this case is typical of those that can be produced by agents who rely on first-time informers not bound up themselves in criminal activity. As I point out below, if this had been the situation here, and that fact had been communicated to the magistrate, this would be a very different case.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Havens.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "5ed64834fbf117cd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Havens"}, "payload": {"all": [{"cite": "446 U.S. 620", "page": "620", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "446"}, {"cite": "100 S. Ct. 1912", "page": "1912", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "64 L. Ed. 2d 559", "page": "559", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "64"}, {"cite": "1980 U.S. LEXIS 103", "page": "103", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "446 U.S. 620", "official": {"cite": "446 U.S. 620", "page": "620", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "446"}, "official_selection_present": true, "record_id": "United States v. Havens"}}
{"assertion_id": "8e522041dff4002e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-627b", "record_id": "United States v. Havens"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-627b", "pinpoint_status": "slip-only", "quote": "We reaffirm this assessment of the competing interests, and hold that a defendant's statements made in response to proper cross-examination reasonably suggested by the defendant's direct examination are subject to otherwise proper impeachment by the government, albeit by evidence that has been illegally obtained and that is inadmissible on the government's direct case, or otherwise, as substantive evidence of guilt.", "quote_fidelity": "mismatch", "record_id": "United States v. Havens", "star_marker": null}}
{"assertion_id": "b6f0b4e62da87b4c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-627", "record_id": "United States v. Havens"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-627", "pinpoint_status": "slip-only", "quote": "; on cross, the Government asked whether he helped sew the swatches, he denied it, and the Government then introduced the suppressed T-shirt to impeach him. ## Issue Whether illegally seized evidence may be used to impeach a defendant's false statements first elicited on cross-examination, where that cross-examination was reasonably suggested by his direct testimony. ## Rule Yes. For impeachment,", "quote_fidelity": "mismatch", "record_id": "United States v. Havens", "star_marker": null}}
{"assertion_id": "bf17805fc109438a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Havens"}, "payload": {"as_of_content": "1980-05-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Havens", "scope_note": "Extends Walder's impeachment exception to cross-examination reasonably suggested by direct; remains good law.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Hay.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Hay
type: case
citation: "95 F.4th 1304 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir. 2024
court_level: coa
circuit: ca10
year: 2024
date_decided: 2024-03-19
docket: 22-3276
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9485331/united-states-v-hay/"
  cluster_id: 9485331
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Hay
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (pole cameras)"
related:
  - "[[Third-Party Doctrine & CSLI]]"
  - "[[Carpenter v. United States]]"
  - "[[Kyllo v. United States]]"
  - "[[United States v. Knotts]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - pole-camera
  - video-surveillance
  - carpenter
  - tenth-circuit
holding: "The Tenth Circuit affirmed, holding that a fixed pole camera trained on the exterior of Hay's home — recording roughly fifteen hours a day for sixty-eight days but capturing only what was visible to passersby in public view — was not a Fourth Amendment search under the circuit's Jackson rule, and that Carpenter's mosaic theory of the 'whole of physical movements' does not disturb that rule for conventional, single-location camera surveillance of a home's exterior."
---

# United States v. Hay

*95 F.4th 1304 (10th Cir. 2024)* (No. 22-3276) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9485331 → opinion 9951944 (95 F.4th 1304, decided 2024-03-19); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Bruce Hay, an Army veteran, was found permanently disabled by the Department of Veterans Affairs in 2006 and drew lifetime benefits. After an anonymous tip that he was faking, VA investigators surveilled him — tailing him, feigning a deer-poaching operation to watch him up close, and installing a motion-activated **pole camera** on a school rooftop across the street from his home. The camera recorded near-constant footage of his house as visible from the street — about fifteen hours a day for sixty-eight days. A Kansas jury convicted Hay of ten counts of stealing government property (18 U.S.C. § 641) and six counts of wire fraud (§ 1343). Hay moved for acquittal or a new trial, arguing among other things that the warrantless, months-long pole-camera surveillance violated the Fourth Amendment.

## Issue
Whether the government's warrantless installation of a fixed pole camera that recorded the exterior of Hay's home — continuously for sixty-eight days — was a Fourth Amendment search, in particular whether *[[Carpenter v. United States]]* extends its "whole of physical movements" mosaic theory to prolonged video surveillance of a residence visible to the public.

## Rule
Under the circuit's rule, camera surveillance capturing only what is exposed to public view is not a search: viewing settings in public view, or visible via generally available technology, does not constitute a search, while viewing private settings perceptible only through technology not in general public use does. Because the pole camera "could not capture footage of any activity that was not in public view, it did not violate the Fourth Amendment," and the extended duration did not change that logic. *[[Carpenter v. United States|Carpenter]]*'s narrow mosaic holding about historical cell-site data does not reach fixed camera surveillance of a home's exterior: "Our holding in *Jackson* that pole cameras trained on a house do not violate the Fourth Amendment remains binding law, and *Carpenter*, without more, does not disturb it." — 95 F.4th 1304, slip op. at 18. ^pin-op18

## Application
Hay's argument that sixty-eight days of continuous recording "painted an intimate portrait" of his life, cataloguing his habits and visitors, was "precluded by *Jackson*" — the length of the surveillance did not change the basic logic that camera surveillance of a home visible to passersby is not a search. *[[Carpenter v. United States|Carpenter]]* did not alter the equation: the Supreme Court called that decision "a narrow one" that did not call into question conventional surveillance techniques and tools such as security cameras. A pole camera fixed across the street came nowhere close to capturing the whole of Hay's physical movements — it saw only one location's exterior, and the moment Hay left home the camera could not track him. The court noted that no circuit had held extended exterior video surveillance of a house to be a search under *[[Carpenter v. United States|Carpenter]]*.

## Conclusion
**Affirmed.** Judge Tymkovich wrote for the panel (Tymkovich, Murphy, and Carson, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hay* is a leading data point on the **unsettled pole-camera question**: the Tenth Circuit (like the Fifth, Sixth, and Seventh) declines to extend *[[Carpenter v. United States|Carpenter]]*'s mosaic theory to fixed exterior camera surveillance of a home, while a First Circuit [[Reading and Citing Cases#en-banc|en banc]] court deadlocked and the Fourth Circuit found aerial city-wide tracking a search. Teach it as circuit-split / unsettled authority — never as a settled nationwide rule that pole cameras are categorically permissible.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (pole cameras)*

## Sources
- [*United States v. Hay*, 95 F.4th 1304 (10th Cir. 2024)](https://www.courtlistener.com/opinion/9485331/united-states-v-hay/) — pinpoint: slip op. at 18 (the *Jackson*-binding / *Carpenter*-does-not-disturb holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ee8e0fe8ef4ea2b4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Hay"}, "payload": {"all": [{"cite": "95 F.4th 1304", "page": "1304", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "95"}], "display": "95 F.4th 1304", "official": {"cite": "95 F.4th 1304", "page": "1304", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "95"}, "official_selection_present": true, "record_id": "United States v. Hay"}}
{"assertion_id": "19ac3dd5d765c910", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Hay"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Hay", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Hay

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hay",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hay",
    "case_name_short": "Hay",
    "case_name_full": "",
    "input_case_name": "United States v. Hay",
    "court": "10th Cir. 2024",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2024-03-19",
    "year": 2024,
    "docket": "22-3276",
    "cluster_id": 9485331,
    "lead_opinion_id": 9951944,
    "sibling_ids": [],
    "absolute_url": "/opinion/9485331/united-states-v-hay/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "95 F.4th 1304",
      "volume": "95",
      "reporter": "F.4th",
      "page": "1304",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "95 F.4th 1304",
        "volume": "95",
        "reporter": "F.4th",
        "page": "1304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "95 F.4th 1304",
    "official_selection": {
      "court_class": "state",
      "selected": "95 F.4th 1304",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:53:33Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hay--9485331",
      "to_record_id": "United States v. Hay",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hay

```
Appellate Case: 22-3276         Document: 010111018128    Date Filed: 03/19/2024    Page: 1
                                                                                    FILED
                                                                        United States Court of Appeals
                                                PUBLISH                         Tenth Circuit

                           UNITED STATES COURT OF APPEALS                     March 19, 2024

                                                                           Christopher M. Wolpert
                                 FOR THE TENTH CIRCUIT                         Clerk of Court
                             _________________________________

  UNITED STATES OF AMERICA,

         Plaintiff - Appellee,

  v.                                                           No. 22-3276

  BRUCE L. HAY,

         Defendant - Appellant.

  ----------------------------------------------------

  REPORTERS COMMITTEE FOR
  FREEDOM OF THE PRESS; FIRST
  AMENDMENT COALITION; FREEDOM
  OF THE PRESS FOUNDATION; THE
  MEDIA INSTITUTE; NATIONAL PRESS
  PHOTOGRAPHERS ASSOCIATION;
  THE NEWS LEADERS ASSOCIATON;
  NEWS/MEDIA ALLIANCE; RADIO
  TELEVISION DIGITAL NEWS
  ASSOCIATION; SOCIETY OF
  ENVIRONMENTAL JOURNALISTS,

          Amici Curiae.
                             _________________________________

                         Appeal from the United States District Court
                                  for the District of Kansas
                              (D.C. No. 2:19-CR-20044-JAR-1)
                           _________________________________

 Rachel Tennell, Debevoise & Plimpton LLP, New York, New York (Benjamin Leb and
 Anagha Sundararajan, Debevoise & Plimpton LLP, New York, New York; David A.
 O’Neil, Debevoise & Plimpton LLP, Washington, D.C.; and Melody Brandon, Federal
 Public Defender, and Paige A. Nichols, Assistant Federal Public Defender, Kansas
Appellate Case: 22-3276    Document: 010111018128         Date Filed: 03/19/2024    Page: 2



 Federal Public Defender’s Office, Topeka, Kansas, with her on the briefs) for Defendant-
 Appellant.

 Kevin J. Barber, United States Department of Justice, Criminal Division, Appellate
 Section, Washington, D.C. (Nicole M. Argentieri, Acting Assistant Attorney General,
 and Lisa H. Miller, Deputy Assistant Attorney General, United States Department of
 Justice, Criminal Division, Appellate Section, Washington, D.C.; and Kate E. Brubacher,
 United States Attorney, District of Kansas, and James A. Brown, Assistant United States
 Attorney, Appellate Chief, District of Kansas, Topeka, Kansas, with him on the brief) for
 Plaintiff-Appellee.

 Brett Max Kaufman, American Civil Liberties Union Foundation, New York, New York;
 Sharon Brett, American Civil Liberties Union of Kansas, Overland Park, Kansas; Tim
 Macdonald, American Civil Liberties Union of Colorado, Denver, Colorado; and Tom
 McBrien, Electronic Privacy Information Center, Washington, D.C., filed an Amicus
 Curiae Brief of American Civil Liberties Union, American Civil Liberties Union of
 Kansas, American Civil Liberties Union of Colorado, Brennan Center for Justice, Center
 for Democracy & Technology, and Electronic Privacy Information Center in Support of
 Defendant-Appellant.

 Katie Townsend, Counsel of Record for Amici Curiae, and Gabe Rottman, Grayson
 Clary, and Emily Hockett, Reporters Committee for Freedom of the Press, Washington,
 D.C., filed an Amicus Curiae Brief of The Reporters Committee for Freedom of the Press
 and 8 Media Organizations in Support of Defendant-Appellant.
                        _________________________________

 Before TYMKOVICH, MURPHY, and CARSON, Circuit Judges.
                  _________________________________

 TYMKOVICH, Circuit Judge.
                 _________________________________

       Does the Fourth Amendment permit the government to surveil a home for

 months on end without a warrant? This case requires us to decide.

       The Department of Veterans Affairs (VA) offers lifetime benefits to

 permanently disabled veterans. A Kansas jury convicted Bruce Hay of ten counts of

 stealing government property and six counts of wire fraud as part of a scheme to



                                             2
Appellate Case: 22-3276     Document: 010111018128         Date Filed: 03/19/2024        Page: 3



 defraud the VA by exaggerating his disability. As part of its investigation, VA

 agents installed a pole camera across the street from his house to film his activities.

        Mr. Hay appeals his conviction. He contends that (1) the evidence presented

 at trial is insufficient to support a conviction, (2) the VA’s installation of a pole

 camera violated his Fourth Amendment rights, and (3) the district judge wrongfully

 admitted evidence to the extent that it deprived him of a fair trial.

        We affirm the district court.

                                     I. Background

        Bruce Hay is a U.S. Army veteran. In 2005, while at home in Kansas, he was

 involved in a serious car accident. Doctors diagnosed him with “functional

 neurological disorder,” or FND, a psychological disorder that impaired his mobility.

 Following this diagnosis, Mr. Hay applied for disability benefits from the VA. In

 2006, the VA determined that Mr. Hay was permanently disabled and therefore

 entitled to benefits.

        Six years later, the VA Inspector General’s office received an anonymous tip

 alleging that Mr. Hay was not, in fact, permanently disabled. It initiated an

 investigation into Mr. Hay’s disability status. Mr. Hay lived in Osawatomie, a small

 town in eastern Kansas. To investigate Mr. Hay’s mobility, officers feigned an

 operation involving deer poaching on a nearby farm so that they could monitor Mr.

 Hay from a closer distance. They also tailed him to medical appointments and other

 events. For a more robust record of his daily activities, they installed a pole camera

 on a school rooftop across the street from Mr. Hay’s house. The camera was remote-
                                              3
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 4



 controlled and activated by motion, and it recorded near constant footage of Mr.

 Hay’s house as visible from across the street. All told, the camera captured 15 hours

 of footage per day for 68 days.

       Over the course of a six-year investigation, the VA finally developed enough

 evidence to suggest that Mr. Hay was faking his disability and that he was not

 entitled to disability benefits. Subsequently, a grand jury indicted Mr. Hay on ten

 counts of stealing government property in violation of 18 U.S.C. § 641 and six counts

 of wire fraud in violation of 18 U.S.C. § 1343. A jury found Mr. Hay guilty of all

 counts.

                                     II. Analysis

       Mr. Hay argues that he was entitled to a judgment of acquittal or a new trial

 for three reasons: (1) the evidence presented at trial was insufficient to support a

 conviction for stealing government property or for wire fraud; (2) the district court

 admitted pole camera footage that was obtained in violation of the Fourth

 Amendment; and (3) the district court admitted other incriminating evidence and

 testimony in violation of the Federal Rules of Evidence.

       A. Sufficiency of the evidence

              1. Stealing government property

       Mr. Hay first contends his conviction should be vacated because the

 government did not supply sufficient evidence to prove that he stole government

 property. In reviewing motions for a judgment of acquittal, we must consider

 whether “viewing the evidence in the light most favorable to the Government, any
                                            4
Appellate Case: 22-3276      Document: 010111018128         Date Filed: 03/19/2024    Page: 5



 rational trier of fact could have found the defendant guilty of the crime beyond a

 reasonable doubt.” United States v. Delgado-Uribe, 363 F.3d 1077, 1081 (10th Cir.

 2004).

          Mr. Hay was charged with fraudulently taking government property under

 18 U.S.C. § 641. That statute makes it a crime to take government property in four

 different ways. It applies to:

                Whoever [1] embezzles, [2] steals, [3] purloins, or
                [4] knowingly converts to his use or the use of another, or
                without authority, sells, conveys or disposes of any record,
                voucher, money, or thing of value of the United States or of
                any department or agency thereof, or any property made or
                being made under contract for the United States or any
                department or agency thereof.

 18 U.S.C. § 641 (brackets added).

          Mr. Hay argues that because his scheme involved fraud and deception, but not

 theft, the statute does not cover his misconduct. The question, then, is whether

 “steal[ing],” as used in the statute, encompasses acts of fraud and deception. It does.

          The term “‘steal’ may denote the criminal taking of personal property either by

 larceny, embezzlement, or false pretenses.” United States v. Turley, 352 U.S. 407, 412

 (1957) (citing Black’s Law Dictionary (4th ed. 1951)) (emphasis added). See also Steal,

 Black’s Law Dictionary (3d ed. 1933) (defining “steal” as “the criminal taking of

 personal property by larceny, embezzlement, or false pretenses.”). Accordingly, circuit

 courts have consistently affirmed convictions under 18 U.S.C. § 641 for submitting

 fraudulent paperwork to the government in order to obtain money. See United States v.

 Ransom, 642 F.3d 1285, 1289-1290 (10th Cir. 2011) (affirming conviction under

                                               5
Appellate Case: 22-3276      Document: 010111018128          Date Filed: 03/19/2024      Page: 6



 18 U.S.C. § 641 for falsification of government timesheets); United States v. Rivera-

 Ortiz, 14 F.4th 91, 101 (1st Cir. 2021) (affirming conviction under 18 U.S.C. § 641 for

 misrepresenting the defendant’s occupation on a social security disability insurance

 application); United States v. Oliver, 238 F.3d 471, 472-473 (3d Cir. 2001) (similar); and

 United States v. Dowl, 619 F.3d 494, 501-502 (5th Cir. 2010) (affirming conviction under

 18 U.S.C. § 641 for falsifying loan applications). Mr. Hay feigned a permanent disability

 to access government benefits. That qualifies as “stealing” under 18 U.S.C. § 641.

        Mr. Hay resists this conclusion, arguing that “none of the offenses enumerated in

 the statute—embezzlement, theft, conversion—extend to offenses that require, as

 necessary elements, proof of both a material misrepresentation and an intent to deceive.”

 Aplt. Br. at 23. According to Mr. Hay, the term “steal” refers to a “range of common-law

 theft offenses that all require the ‘wrongful taking’ of property without the consent of the

 owner.” Id. at 24-25 (citing United States v. Hill, 835 F.2d 759, 763 (10th Cir. 1987);

 C.R.S. Recovery, Inc. v. Laxton, 550 Fed. App’x 512, 513 (9th Cir. 2013); and Steal,

 Merriam-Webster Dictionary). Mr. Hay also distinguishes “stealing” from “fraud,”

 which “requires proof that the defendant obtained property by means of ‘false pretenses,

 representations, or promises’ that is ‘reasonably calculated to deceive persons of ordinary

 prudence.’” Id. at 25 (citing United States v. Cochran, 109 F.3d 660, 664 (10th Cir.

 1997); and Fraud, Black’s Law Dictionary (3d ed. 1933)).

        Mr. Hay’s definition of “stealing” is overly narrow and unsupported by the text of

 the statute or by precedent. As the Supreme Court explained in Turley, “steal[ing]”

 includes the “criminal taking of personal property . . . by . . . false pretenses.” Turley,

                                               6
Appellate Case: 22-3276     Document: 010111018128         Date Filed: 03/19/2024     Page: 7



 352 U.S. at 412. “[T]he courts interpreting [stolen and steal] have declared that they do

 not have a necessary common-law meaning coterminous with larceny and exclusive of

 other theft crimes.” Id. This reasoning forecloses Mr. Hay’s argument.

        Mr. Hay points to our decision in United States v. Hill, where we held that “while

 § 641 defines a broad crime against property, it nonetheless circumscribes the means by

 which that crime can be committed.” 835 F.2d 759, 763 (10th Cir. 1987) (internal

 citation omitted). But Hill does not help Mr. Hay because its analysis turns on an

 intrinsic distinction between conversion and stealing regarding how possession is

 obtained: “[o]ne who gains possession of property by wrongfully taking it from another

 steals. One who comes into possession of property by lawful means, but afterwards

 wrongfully exercises dominion over that property against the rights of the true owner,

 commits conversion.” Id. at 764 (internal citations omitted). Thus, we concluded, “proof

 that the defendant converted property of the government is not proof that he stole it. The

 concepts of stealing and conversion are mutually exclusive.” Id. (emphasis in original).

        Unlike in Hill, the government does not argue here that Mr. Hay both came into

 possession of property in a lawful manner (i.e. conversion) and also wrongfully took the

 property (i.e. stealing). Id. Rather, the government argues that Mr. Hay’s initial

 acquisition of government property was wrongful because it was obtained through false

 pretenses, thereby placing it within Hill’s definition of stealing. And as Turley made

 clear, “fraud” and “stealing” are not mutually exclusive—stealing encompasses

 wrongfully obtaining property through “false pretenses.” 352 U.S. at 412.



                                              7
Appellate Case: 22-3276     Document: 010111018128          Date Filed: 03/19/2024        Page: 8



        Separately, Mr. Hay argues that the absence of “fraud” in the statutory text implies

 that Congress did not intend for the statute to forbid stealing by means of fraud. He

 points to other statutes that forbid both “stealing” and “obtaining by fraud” as evidence

 that Congress treats these as two separate offenses. See 18 U.S.C. §§ 659, 665(a),

 666(a)(1)(A), 668(b)(1), and 670(a). He notes that Congress did not place 18 U.S.C.

 § 641 in the section of the criminal code that criminalizes fraud offenses more generally.

        Even if Congress considered “stealing” and “fraud” to be two separate offenses,

 the statute forbidding “stealing” would still forbid “fraud” wherever a defendant

 committed “fraud” as a strategy to steal. “Stealing,” as explained by the Supreme Court,

 means the taking of property “by larceny, embezzlement, or false pretenses”—an

 expansive definition. Turley, 352 U.S. at 412 (discussing the definition of “stolen” in the

 National Motor Vehicle Theft Act, 18 U.S.C. § 2312). And obviously, the actus reus of

 stealing can violate more than one federal criminal statute. For example, one might both

 steal explosives by wrongfully transporting them away and separately violate 18 U.S.C.

 § 842(a)(3)(A) (prohibiting possession of explosive materials without a license), or steal

 an armed vessel and also violate 18 U.S.C. § 964 by delivering it to a belligerent nation,

 or steal a drone while flying it off in a way that would recklessly interfere with the

 operation of a manned aircraft in violation of 18 U.S.C. § 39B(a)(2).

        Since 18 U.S.C. § 641 prohibits stealing government property by means of fraud or

 deception, the government presented sufficient evidence to support Mr. Hay’s conviction.




                                               8
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024   Page: 9



              2. Wire fraud

       The jury also found Mr. Hay guilty of six counts of wire fraud under 18 U.S.C.

 § 1343. He contends that the government presented insufficient evidence to show he

 intended to commit fraud.

       The federal wire fraud statute applies to

              [w]hoever, having devised or intending to devise any
              scheme or artifice to defraud, or for obtaining money or
              property by means of false or fraudulent pretenses,
              representations, or promises, transmits or causes to be
              transmitted by means of wire, radio, or television
              communication in interstate or foreign commerce, any
              writings, signs, signals, pictures, or sounds for the purpose
              of executing such scheme or artifice.

 18 U.S.C. § 1343. Any falsehood must be material to the scheme, Neder v. United

 States, 527 U.S. 1, 24 (1999), and the defendant must have intended to defraud.

 United States v. Hanson, 41 F.3d 580, 583 (10th Cir. 1994).

       At trial, the government presented evidence that Mr. Hay committed wire

 fraud by lying to the VA about the extent of his injuries to obtain benefits. While

 Mr. Hay does not dispute the statements alleged by the government, he argues that

 they were insufficient to establish materiality or intent.

       We disagree. A reasonable factfinder could conclude that Mr. Hay’s

 statements were material to the VA’s decision to assign him disability benefits. “A

 false statement is material when it has a natural tendency to influence, or is capable

 of influencing, the decision of the decisionmaking body to which it was addressed.”

 United States v. Williams, 934 F.3d 1122, 1128 (10th Cir. 2019) (internal quotation


                                             9
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 10



  marks omitted). VA officials testified multiple times that the agency considered Mr.

  Hay’s description of his disability when determining his disability status. See, e.g.,

  R. Vol. III at 325, 360, 398, and 412. Viewing this evidence in the light most

  favorable to the government, see Delgado-Uribe, 363 F.3d at 1077, a reasonable trier

  of fact could conclude that Mr. Hay’s statements to the government were material.

        Mr. Hay argues that the government has not met its burden of showing

  materiality since his “doctors also had access to his full medical records, including

  reports and test results” and it was “Mr. Hay’s doctors, not Mr. Hay himself, [who]

  diagnosed him with FND based on the evidence before them, and there is no evidence

  that this diagnosis was based solely on Mr. Hay’s self-reporting his symptoms.”

  Aplt. Br. at 36-37. This argument misapprehends the standard for materiality. The

  government did not bear the burden of proving that Mr. Hay’s false statements were

  decisive to the VA’s disability determination, only that they were “capable of

  influencing” that decision. Williams, 934 F.3d at 1128. Any negligence on the part

  of Mr. Hay’s doctors in this determination is entirely consistent with the materiality

  of Mr. Hay’s misstatements.

        A reasonable factfinder could also conclude that the discrepancy between

  Mr. Hay’s statements to the VA and his actual physical condition demonstrated an

  intent to defraud. The jury heard considerable evidence from agents and medical

  professionals that Mr. Hay systematically exaggerated his symptoms to obtain

  benefits. As one VA agent testified, Mr. Hay exhibited extreme mobility difficulties

  when at his benefits exams. He could only move with assistance from his wife and

                                             10
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 11



  climbed stairs one step at a time, with both feet on each stair. After his exam, when

  he believed that he was out of the VA’s sight, Mr. Hay drove over to a pawn shop,

  walked in without assistance of his cane or his wife, and walked out carrying a

  toolbox. As neurologist Dr. Danielle Baker put it, “there is a marked discrepancy in

  what both Mr. Hay and his wife have documented on forms and also demonstrated in

  evaluations, compensation benefit evaluations versus what was seen with actual

  every day daily functioning when surveillance was taken.” R. Vol. III at 850.

  Viewing this evidence in the light most favorable to the government, a reasonable

  trier of fact could conclude that Mr. Hay intended to defraud the government. See

  Delgado-Uribe, 363 F.3d at 1077.

        Mr. Hay also contends that the government has not carried its burden of

  showing intent, since he “was upfront with his doctors about his disabilities” and told

  his doctors that his “episodes only happened once or twice a week.” Aplt. Br. at 37.

  These points, accepted as true, do not warrant reversal. The government proved

  fraud at trial by showing that the chasm between the symptoms that Mr. Hay reported

  to the VA and the mobility he exhibited out of sight was so great as to be misleading.

  Even if Mr. Hay acknowledged some aptitude for physical activity to his doctors, it

  does not follow that the government’s exaggeration theory was unsupported by the

  evidence overall. That Mr. Hay admitted some ability to perform physical tasks is

  fully consistent with the jury’s conclusion that he exaggerated his physical condition.

                                        *    *   *



                                            11
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 12



        In sum, the evidence at trial was sufficient to support the convictions for theft

  of government property and wire fraud.

        B. Fourth Amendment

        Mr. Hay next argues that the district court should have suppressed evidence

  obtained from camera surveillance of his home under the Fourth Amendment. He

  contends that constant video surveillance of his home over several months constitutes

  an unreasonable search under emerging Supreme Court case law.

        As part of its investigation, the VA installed a pole-mounted camera across the

  street from Mr. Hay’s house. The camera was motion-activated and remote-

  controlled, and it produced footage of the front of Mr. Hay’s property. The camera

  could only view Mr. Hay’s property as visible from the street.

        The Fourth Amendment guarantees “[t]he right of the people to be secure in

  their persons, houses, papers, and effects, against unreasonable searches and

  seizures.” U.S. Const. amend. IV. “When an individual seeks to preserve something

  as private, and his expectation of privacy is one that society is prepared to recognize

  as reasonable, we have held that official intrusion into that private sphere generally

  qualifies as a search and requires a warrant supported by probable cause.” Carpenter

  v. United States, 585 U.S. 296, 304 (2018). Warrantless searches “are per se

  unreasonable under the Fourth Amendment—subject only to a few specifically

  established and well-delineated exceptions.” Arizona v. Grant, 556 U.S. 332, 338

  (2009).



                                             12
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 13



        “For much of our history, Fourth Amendment search doctrine was tied to

  common-law trespass and focused on whether the Government obtains information

  by physically intruding on a constitutionally protected area.” Carpenter, 585 U.S.

  at 304. In the 1960s and 1970s, however, the Supreme Court expanded the Fourth

  Amendment’s sphere of protection to situations where an individual “seeks to

  preserve something as private, and his expectation of privacy is one that society is

  prepared to recognize as reasonable.” Id. (citing Smith v. Maryland, 442 U.S. 735,

  740 (1979)). This “reasonableness” inquiry is the touchstone of modern Fourth

  Amendment analysis.

        For decades, the Supreme Court has held that individuals do not have a

  reasonable expectation of privacy in activity that occurs in public view. “The Fourth

  Amendment protection of the home has never been extended to require law

  enforcement officers to shield their eyes when passing by a home on public

  thoroughfares.” California v. Ciraolo, 476 U.S. 207, 213 (1986). For instance, the

  Fourth Amendment does not require a warrant to view property from the air, if “[a]ny

  member of the public flying in this airspace who glanced down could have seen

  everything that the[] officers observed.” Id. at 213-214; see also Dow Chemical Co.

  v. United States, 476 U.S. 227, 238-239 (1986) (holding that aerial view of an

  industrial plant did not violate the Fourth Amendment, even if “human vision is

  enhanced somewhat”).

        But the Supreme Court has required police obtain a warrant to view activities

  that are beyond public view and perceptible only through equipment outside of

                                            13
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024      Page: 14



  general commercial circulation. In Kyllo v. United States, the government surveilled

  a house using a thermal imaging camera. 533 U.S. 27, 34 (2001). In deeming this to

  be a search, the Court explained that when “the Government uses a device that is not

  in general public use, to explore details of the home that would previously have been

  unknowable without physical intrusion, the surveillance is a ‘search’ and is

  presumptively unreasonable without a warrant.” Id. at 40; see also id. at 39 (thermal

  vision “might disclose, for example, at what hour each night the lady of the house

  takes her daily sauna and bath—a detail that many would consider ‘intimate’”). The

  Supreme Court’s guideposts are clear: viewing of private settings, visible only with

  technology that is not in general public use, is considered a search; viewing settings

  that are in public view, or visible via generally available technology, does not

  constitute a search.

        We have already concluded that the use of a pole camera does not constitute a

  search if the camera can only capture activity in public view. In United States v.

  Jackson, we held that “[t]he use of video equipment and cameras to record activity

  visible to the naked eye does not ordinarily violate the Fourth Amendment.”

  213 F.3d 1269, 1280 (10th Cir. 2000) (citing Dow Chem. Co., 476 U.S. at 239 and

  Ciraolo, 476 U.S. at 213). We reasoned that “activity a person knowingly exposes to

  the public is not a subject of Fourth Amendment protection” and that the pole

  cameras at issue in that case “were incapable of viewing inside the houses, and were

  capable of observing only what any passerby would easily have been able to

  observe.” Id. at 1281. Although Jackson predates Kyllo, it is entirely consistent with

                                            14
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024       Page: 15



  the holding in Kyllo since videographic equipment is in general commercial

  circulation and available to the public at large.

        The facts of this case are not meaningfully different from those in Jackson.

  Both cases involve the extensive use of cameras surreptitiously filming the front of

  the house. While Mr. Hay noted at oral argument that the pole camera incidentally

  captured activity in his house, that activity occurred at night in front of the window

  and was therefore visible to any passerby. Since the pole camera could not capture

  footage of any activity that was not in public view, it did not violate the Fourth

  Amendment.

        To counter this, Mr. Hay argues that Jackson has been abrogated by the

  Supreme Court’s Carpenter decision. He contends that while limited video

  surveillance might not violate the Constitution, the government’s months-long,

  potentially limitless surveillance crosses the line. In Carpenter, the Supreme Court

  considered whether the government conducts a search when it accesses historical

  cell-site location information. There, the government subpoenaed cell phone data

  from the suspect’s wireless provider to track the suspect’s movement before, during,

  and after a crime. The Court found this to be a search covered by the Fourth

  Amendment. It explained that whenever a cell phone connects to a cell site, “it

  generates a time-stamped record known as cell-site location information,” the

  precision of which “depends on the size of the geographic area covered by the cell

  site.” Carpenter, 585 U.S. at 301. Since many people carry their cell phones with

  them wherever they go, cell-site location information “chronicle[s] a person’s past

                                             15
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024      Page: 16



  movements through the record of his cell phone signals.” Id. at 309. The Court

  found this unreasonable since “[w]hoever the suspect turns out to be, he has

  effectively been tailed every moment of every day for five years, and the police

  may—in the Government’s view—call upon the results of that surveillance without

  regard to the constraints of the Fourth Amendment.” Id. at 312.

        The Carpenter court distinguished the case from United States v. Knotts,

  where it found that planting a transmitter in a suspect’s car to aid in tracking the

  vehicle did not constitute a search. 460 U.S. 276, 282 (1983). There, the Court

  explained that “[a] person travelling in an automobile on public thoroughfares has no

  reasonable expectation of privacy in his movements from one place to another.” Id.

  at 281. Although the officers “relied not only on visual surveillance, but on the use

  of the beeper to signal the presence of [the] automobile to the police receiver,”

  “nothing in the Fourth Amendment prohibited the police from augmenting the

  sensory faculties bestowed upon them at birth” with the beeper. Id. at 282. The

  Carpenter court found that Knotts was not controlling on the question of cell site

  location information, since that opinion had acknowledged that “different

  constitutional principles may be applicable if twenty-four hour surveillance of any

  citizen of this country were possible.” Carpenter, 585 U.S. at 306-307 (citing

  Knotts, 460 U.S. at 283-284) (internal quotation marks and brackets omitted). It

  further noted that in a more recent case on vehicle tracking, “[a] majority of this

  Court has already recognized that individuals have a reasonable expectation of

  privacy in the whole of their physical movements.” Id. at 310 (citing United States v.

                                             16
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024      Page: 17



  Jones, 565 U.S. 400, 430 (2018) (Alito, J. concurring); and Jones, 565 U.S. at 415

  (Sotomayor, J., concurring)).

        The Carpenter court distinguished “pursu[ing] a suspect for a brief stretch,”

  which fell within a societal expectation of privacy, from “secretly monitor[ing] and

  catalogu[ing] every single movement of an individual’s car for a very long period,”

  which fell outside of it. Id. (citing Jones, 565 U.S. at 429-430 (Alito, J.,

  concurring)). It reasoned that “[a]llowing government access to cell-site records

  contravenes that expectation” because “[m]apping a cell phone’s location over the

  course of 127 days provides an all-encompassing record of the holder’s

  whereabouts.” Id. at 311. This in turn “provides an intimate window into a person’s

  life, revealing not only his particular movements, but through them his ‘familial,

  political, professional, religious, and sexual associations.’” Id. citing (Jones,

  565 U.S. at 415 (Sotomayor, J. concurring)). Further, unlike tracking devices in cars,

  “police need not even know in advance whether they want to follow a particular

  individual, or when,” since cell site location data allows the Government to “travel

  back in time to retrace a person’s whereabouts, subject only to the retention policies

  of the wireless carriers.” Id. at 312. The Carpenter court concluded that accessing

  cell site location information “invaded Carpenter’s reasonable expectation of privacy

  in the whole of his physical movements” and therefore constituted a search. Id.

  at 313.

        Mr. Hay contends that he has a similar reasonable expectation of privacy in the

  whole of his physical movements coming and going from his home, plus a heightened

                                             17
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 18



  expectation of privacy in the exterior to his home. According to Mr. Hay, the

  recording of his house for an extended period of time (68 days in this case) catalogs

  his habits, patterns, and visitors in a way that ordinary physical surveillance could

  not duplicate. As he puts it, “the footage obtained painted an intimate portrait of

  Mr. Hay’s personal life,” including “when he entered and exited his home; who

  visited him and his family,” and “what Mr. Hay did on his own front porch.” Aplt.

  Br. at 44. He acknowledges that this activity took place in public but argues that

  “[w]hile people subjectively lack an expectation of privacy in some discrete actions

  they undertake in unshielded areas around their homes, they do not expect that every

  such action will be observed and perfectly preserved for the future.” Id. at 45 (citing

  Commonwealth v. Mora, 150 N.E.3d 297, 306 (Mass. 2020)).

        This argument is precluded by Jackson. That the surveillance took place over

  an extended period of time does not change the basic logic of the opinion—camera

  surveillance of a home visible to passersby does not constitute a search. Nor does

  Carpenter change the equation. The Supreme Court expressly noted that its decision

  was “a narrow one:” “[w]e do not express a view on matters not before us: real-time

  CSLI or ‘tower dumps’ . . . or call into question conventional surveillance techniques

  and tools, such as security cameras.” Carpenter, 585 U.S. at 316 (emphasis added).

  Our holding in Jackson that pole cameras trained on a house do not violate the Fourth

  Amendment remains binding law, and Carpenter, without more, does not disturb it.

  In so holding, we are not alone. No circuit court has concluded that extended video

  surveillance of a house is a search under Carpenter. See United States v. Dennis,

                                             18
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 19



  41 F.4th 732, 740-741 (5th Cir. 2022) (finding no Fourth Amendment violation in the

  installation of cameras directed at front and back of defendant’s house); United States

  v. Tuggle, 4 F.4th 505, 523-524 (7th Cir. 2021) (finding no Fourth Amendment

  violation in government’s prolonged, round-the clock use of cameras capturing the

  exterior of defendant’s home); and United States v. Trice, 966 F.3d 506, 518-520

  (6th Cir. 2020) (finding no Fourth Amendment violation in installation of camera

  across the hallway from entrance of defendant’s apartment); cf. Leaders of a

  Beautiful Struggle v. Baltimore Police Dep’t, 2 F.4th 330, 341-342 (4th Cir. 2021)

  (en banc) (finding a Fourth Amendment violation in use of planes to record

  movements across an entire city). An en banc First Circuit deadlocked on the

  question, with an even number of judges reaching opposite conclusions. See United

  States v. Moore-Bush, 36 F.4th 320 (1st Cir. 2022) (en banc).

        Regardless, Mr. Hay’s privacy interests fall outside Carpenter’s rationale.

  Carpenter acknowledged that individuals have a privacy interest in “the whole of

  their physical movements.” Carpenter, 585 U.S. at 310. The pole camera across the

  street from Mr. Hay came nowhere close to capturing “the whole of his physical

  movements.” It could only capture his movements at a single location, outside his

  house. As soon as he left his house, the government could no longer track him by

  this means. And the Carpenter majority was particularly concerned by retrospective

  police searches of previously unidentified individuals—i.e. where the government

  would “travel back in time to retrace a person’s whereabouts, subject only to the

  retention policies of the wireless carriers.” Id. at 312. In this case, the government

                                             19
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 20



  did not delve into a preexisting data set on Mr. Hay’s whereabouts. It set up the

  camera while Mr. Hay was already under investigation as a prospective, not

  retrospective, investigative measure. The surveillance here merely enhances what

  law enforcement could always do—monitor a suspect’s movement in public view.

         Mr. Hay attempts to divine a new privacy interest by merging the one

  articulated in Carpenter (a retrospective “all encompassing record of the holder’s

  whereabouts,” 585 U.S. at 311), with the one identified in Kyllo and Ciraolo (privacy

  connected to one’s home). 533 U.S. at 31, 476 U.S. at 213; see also Lange v.

  California, 141 S. Ct. 2011, 2018 (2021) (“[W]hen it comes to the Fourth

  Amendment, the home is first among equals.” (citing Florida v. Jardines, 569 U.S. 1,

  6 (2013)).

         But the Supreme Court’s recognition of privacy interests in the home does not

  “require law enforcement officers to shield their eyes when passing by a home on

  public thoroughfares.” Ciraolo, 476 U.S. at 213. The government executes a search

  when it “uses a device that is not in general public use, to explore details of the home

  that would previously have been unknowable without physical intrusion,” Kyllo,

  533 U.S. at 40, but “[n]ow more than ever, cameras are ubiquitous, found in the

  hands and pockets of virtually all Americans, on the doorbells and entrances of

  homes, and on the walls and ceilings of businesses.” Tuggle, 4 F.4th at 516.

  Mr. Hay retains some privacy interests in the whole of his physical movements and in

  the interior of his home, but the pole camera at issue did not infringe upon either of

  those interests.

                                             20
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024      Page: 21



        The Supreme Court has defined a “search” under the Fourth Amendment not

  by a fixed point, but by “[w]hen an individual seeks to preserve something as private

  and his expectation of privacy is one that society is prepared to recognize as

  reasonable.” Carpenter, 585 U.S. at 304 (citing Smith, 442 U.S. at 740) (internal

  quotation marks omitted). “Current Fourth Amendment jurisprudence admits of a

  precarious circularity: Cutting-edge technologies will eventually and inevitably

  permeate society. In turn, society’s expectations of privacy will change as citizens

  increasingly rely on and expect these new technologies.” Tuggle, 4 F.4th at 527

  (upholding use of pole camera).

        Few technologies have expanded more rapidly than the ubiquitous camera,

  which is worn by police officers, built into cellphones that the Carpenter court called

  “almost a feature of human anatomy,” and strapped to front doors. United States v.

  Moore-Bush, 36 F.4th at 372 (Lynch, J., concurring) (citing Carpenter, 585 U.S.

  at 311). Cutting edge drone technology enables police to conduct discreet aerial

  investigations, see State v. Stevens, 210 N.E.3d 1154, 1157 (Ohio App. 2023), while

  satellite images of homes are free and readily available to citizens and law

  enforcement alike. See In re Murphy, No. 771 Sept. Term 2022, 2023 WL 2999975,

  at *6 (Md. App. 2023). Artificial intelligence software accelerates facial

  identification and pattern recognition to a previously unimaginable degree. As video

  cameras proliferate throughout society, regrettably, the reasonable expectation of

  privacy from filming is diminished.



                                            21
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024       Page: 22



        In conclusion, Mr. Hay had no reasonable expectation of privacy in a view of

  the front of his house. The district court did not err in denying suppression of that

  footage.

        C. Evidentiary rulings

        Finally, Mr. Hay argues that he is entitled to a new trial because of three

  erroneous evidentiary rulings by the district court. “We review a trial court’s

  evidentiary decisions for abuse of discretion. However, we subject to de novo review

  a trial court’s legal conclusions about the Federal Rules of Evidence.” United States

  v. Cherry, 217 F.3d 811, 814 (10th Cir. 2000).

        First, Mr. Hay argues that the district court erred in permitting the VA agents

  to narrate the contents of video footage. He argues that this testimony bolstered the

  impact of the footage by allowing non-expert opinion testimony outside the agent’s

  expertise. Federal Rule of Evidence 701(b), only permits lay testimony when it is:

               (a) rationally based on the witness’s perception;
               (b) helpful to clearly understanding the witness’s testimony
                   or to determining a fact in issue; and
               (c) not based on scientific, technical, or other specialized
                   knowledge within the scope of Rule 702.

  Fed. R. Evid. 701. Mr. Hay argues that the agents’ testimony did not satisfy the

  second condition, because “their impressions of the footage itself were

  inappropriate.” Aplt. Br. at 60.

        But Rule 701 does not prohibit lay testimony of impressions if those

  impressions are helpful to determining a fact in issue. Fed. R. Evid. 701(b). The

  district court did not abuse its discretion in concluding that the VA agents’

                                             22
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024    Page: 23



  impressions of what was occurring in the video, informed by their deep familiarity

  with the footage, would help the jury determine a fact in issue.

        Second, Mr. Hay argues that the district court erred by permitting the

  government to introduce his VA exam records, which included the doctors’

  assessment of his entitlement to disability benefits. According to Mr. Hay, these

  were out-of-court statements offered for their truth and therefore excludable under

  Fed. R. Evid. 801. The district court admitted these records under Fed. R. Evid.

  803(4)’s exception for “medical diagnosis or treatment.”1 Mr. Hay contends that the

  exception does not apply, because a medical assessment for the purpose of

  determining disability is not a “diagnosis.”

        We disagree. The dictionary definition of “diagnosis” means “the discovery of

  a patient’s illness or the determination of the nature of his disease from a study of his

  symptoms,” or “[t]he art or act of recognizing the presence of disease from its

  symptoms, and deciding as to its character, also the decision reached, for

  determination of type or condition through case or specimen study or conclusion

  arrived at through critical perception or scrutiny.” Diagnosis, Black’s Law

  Dictionary (4th rev. ed. 1968). Nothing in that definition suggests that making a

  disability determination for a given ailment precludes being “diagnosed” with that



  1
   Rule 803(4) provides that “[a] statement that: (A) is made for — and is reasonably
  pertinent to — medical diagnosis or treatment; and (B) describes medical history;
  past or present symptoms or sensations; their inception; or their general cause” is an
  exception to the rule against hearsay evidence.

                                             23
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 24



  ailment. Indeed, it seems to require as much. Rule 803(4) authorizes admission of

  the VA records.

        Third, Mr. Hay argues that the district court erred in admitting evidence from

  after the charging period. The indictment charged Mr. Hay with committing theft

  and fraud between 2011 and 2018. The district court, however, also admitted

  evidence of Mr. Hay’s behavior from after that period—a mechanic’s lien stating that

  he had worked as a farm manager from 1985 to 2020, and a video from 2021.

  Mr. Hay contends that this evidence was unduly prejudicial in violation of Fed. R.

  Evid. 403.

        Rule 403 permits a district court to “exclude relevant evidence if its probative

  value is substantially outweighed by a danger of one or more of the following: unfair

  prejudice, confusing the issues, misleading the jury, undue delay, wasting time, or

  needlessly presenting cumulative evidence.” “Assessing the probative value of the

  proffered evidence, and weighing any factors counseling against admissibility is a

  matter first for the district court’s sound judgment under Rules 401 and 403.”

  Sprint/United Management Co. v. Mendelsohn, 552 U.S. 379, 384 (2008) (quoting

  United States v. Abel, 469 U.S. 45, 54 (1984)) (brackets omitted). “This is

  particularly true with respect to Rule 403 since it requires an on-the-spot balancing of

  probative value and prejudice, potentially to exclude as unduly prejudicial some

  evidence that already has been found to be factually relevant.” Id. (internal quotation

  marks omitted). Accordingly, a “trial court has broad discretion to determine



                                            24
Appellate Case: 22-3276   Document: 010111018128        Date Filed: 03/19/2024    Page: 25



  whether prejudice inherent in otherwise relevant evidence outweighs its probative

  value.” United States v. Poole, 929 F.2d 1476, 1482 (10th Cir. 1991).

        The district court acted within its discretion in admitting evidence post-dating

  the charging period. The VA allotted benefits to Mr. Hay because it determined that

  he was “permanently disabled,” so any evidence that Mr. Hay was able to perform

  physical labor after that determination—whether or not it was within the charged

  period—was probative as to whether he had defrauded the VA.

                                   III. Conclusion

        We affirm the district court’s denial of a judgment of acquittal and

  admission of the contested evidence.




                                            25

```

---

## GROUP: _overhaul2/lake/cases/United States v. Henry.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "b19ba619192b3827", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Henry"}, "payload": {"all": [{"cite": "447 U.S. 264", "page": "264", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "447"}, {"cite": "100 S. Ct. 2183", "page": "2183", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 115", "page": "115", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 111", "page": "111", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "447 U.S. 264", "official": {"cite": "447 U.S. 264", "page": "264", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "447"}, "official_selection_present": true, "record_id": "United States v. Henry"}}
{"assertion_id": "23fdc7c1cf58aa41", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-270", "record_id": "United States v. Henry"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-270", "pinpoint_status": "slip-only", "quote": "incriminating statements from an indicted, incarcerated defendant, in violation of his Sixth Amendment right to counsel under *Massiah*, when it used a paid jailhouse informant posing as a fellow inmate. ## Rule Yes. The Sixth Amendment, as construed in [[Massiah v. United States]], bars the government from", "quote_fidelity": "mismatch", "record_id": "United States v. Henry", "star_marker": null}}
{"assertion_id": "3d72e2cdc2726341", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-274", "record_id": "United States v. Henry"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-274", "pinpoint_status": "slip-only", "quote": "By intentionally creating a situation likely to induce Henry to make incriminating statements without the assistance of counsel, the Government violated Henry's Sixth Amendment right to counsel.", "quote_fidelity": "mismatch", "record_id": "United States v. Henry", "star_marker": null}}
{"assertion_id": "4997322bea08be19", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Henry"}, "payload": {"as_of_content": "1980-06-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Henry", "scope_note": "Cabined by Kuhlmann v. Wilson (a passive 'listening post' informant who does not deliberately elicit does not violate the Sixth Amendment); Henry itself remains good law.", "varies_by_point": false}}
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
