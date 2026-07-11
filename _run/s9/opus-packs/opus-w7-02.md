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

## GROUP: _overhaul2/lake/cases/Mapp v. Ohio.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Mapp v. Ohio"
type: case
citation: "367 U.S. 643 (1961)"
parallel_cite: "81 S. Ct. 1684; 6 L. Ed. 2d 1081"
neutral_cite: 1961 U.S. LEXIS 812
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-10-09
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-06-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mapp v. Ohio
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106285/mapp-v-ohio/"
  cluster_id: 106285
  opinion_id: 106285
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Weeks v. United States]]", "[[Wolf v. Colorado]]", "[[United States v. Leon]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "incorporation", "fourteenth-amendment"]
holding: "The exclusionary rule applies to the States through the Fourteenth Amendment."
lake:
  record_id: Mapp v. Ohio
  status: verified
  projected_at: 2026-07-06
---

# Mapp v. Ohio

*367 U.S. 643 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Cleveland officers forced their way into Dollree Mapp's home without a valid warrant, searched it while looking for a bombing suspect and gambling materials, and found allegedly obscene materials, for which she was convicted. The Ohio courts admitted the unlawfully seized evidence, relying on *[[Wolf v. Colorado]]*, which had held the Fourth Amendment's exclusionary remedy was not binding on the States.

## Issue
Whether evidence obtained by a search and seizure that violates the Fourth Amendment is inadmissible in a state criminal prosecution.

## Rule
Yes. "We hold that all evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court." — 367 U.S. at 655. ^pin-655

Because the Fourth Amendment's right of privacy is enforceable against the States through the Due Process Clause of the Fourteenth Amendment, it is enforceable against them by the same sanction of exclusion used against the Federal Government.

## Application
The evidence used to convict Mapp was obtained in a warrantless, forcible entry and search of her home in violation of the Fourth Amendment. Under the rule announced here, that unlawfully seized evidence was inadmissible in the Ohio courts, so its admission could not stand. The Court overruled the contrary holding of *[[Wolf v. Colorado]]* to the extent it had left the States free to admit such evidence.

## Conclusion
The conviction, resting on unconstitutionally seized evidence, was reversed. The federal exclusionary rule of *[[Weeks v. United States|Weeks]]* applies to the States through the Fourteenth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Mapp* extended the [[Weeks v. United States]] exclusionary rule to the States and overruled the contrary portion of [[Wolf v. Colorado]]. The exclusionary rule remains good law, though later cases have narrowed its **scope** through the [[The Good-Faith Exception|good-faith exception]] ([[United States v. Leon]]) and a culpability requirement for deterrence ([[Herring v. United States]]) — refinements of the remedy, not abrogations of *Mapp*.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Mapp v. Ohio*, 367 U.S. 643 (1961) — https://www.courtlistener.com/opinion/106285/mapp-v-ohio/ — pinpoint: 655.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "519ff73242972410", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mapp v. Ohio"}, "payload": {"all": [{"cite": "367 U.S. 643", "page": "643", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "367"}, {"cite": "81 S. Ct. 1684", "page": "1684", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "6 L. Ed. 2d 1081", "page": "1081", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "6"}, {"cite": "1961 U.S. LEXIS 812", "page": "812", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}], "display": "367 U.S. 643", "official": {"cite": "367 U.S. 643", "page": "643", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "367"}, "official_selection_present": true, "record_id": "Mapp v. Ohio"}}
{"assertion_id": "980d25e98dfea5b3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-655", "record_id": "Mapp v. Ohio"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-655", "pinpoint_status": "slip-only", "quote": "--- # Mapp v. Ohio *367 U.S. 643 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cleveland officers forced their way into Dollree Mapp's home without a valid warrant, searched it while looking for a bombing suspect and gambling materials, and found allegedly obscene materials, for which she was convicted. The Ohio courts admitted the unlawfully seized evidence, relying on *Wolf v. Colorado*, which had held the Fourth Amendment's exclusionary remedy was not binding on the States. ## Issue Whether evidence obtained by a search and seizure that violates the Fourth Amendment is inadmissible in a state criminal prosecution. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Mapp v. Ohio", "star_marker": null}}
{"assertion_id": "05576641b05bb574", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mapp v. Ohio"}, "payload": {"as_of_content": "1961-06-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mapp v. Ohio", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Mapp v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mapp v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mapp v. Ohio",
    "case_name_short": "Mapp",
    "case_name_full": "Mapp v. Ohio",
    "input_case_name": "Mapp v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-10-09",
    "year": 1961,
    "docket": null,
    "cluster_id": 106285,
    "lead_opinion_id": 106285,
    "sibling_ids": [
      106285,
      9422279,
      9422280,
      9422281,
      9422282
    ],
    "absolute_url": "/opinion/106285/mapp-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8951163,
        "score": 20,
        "case_name": "Mapp v. Ohio"
      },
      {
        "cluster_id": 6861770,
        "score": 20,
        "case_name": "Mapp v. Ohio"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "367 U.S. 643",
      "volume": "367",
      "reporter": "U.S.",
      "page": "643",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 1684",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1081",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 812",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "812",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "367 U.S. 643",
        "volume": "367",
        "reporter": "U.S.",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 1684",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1081",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1081",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 812",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "812",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "367 U.S. 643",
    "official_selection": {
      "court_class": "scotus",
      "selected": "367 U.S. 643",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-655",
      "page": null,
      "quote": "--- # Mapp v. Ohio *367 U.S. 643 (1961)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Cleveland officers forced their way into Dollree Mapp's home without a valid warrant, searched it while looking for a bombing suspect and gambling materials, and found allegedly obscene materials, for which she was convicted. The Ohio courts admitted the unlawfully seized evidence, relying on *Wolf v. Colorado*, which had held the Fourth Amendment's exclusionary remedy was not binding on the States. ## Issue Whether evidence obtained by a search and seizure that violates the Fourth Amendment is inadmissible in a state criminal prosecution. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-06-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mapp v. Ohio",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Mapp v. Ohio:lane1_negative"
      },
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
        "journal_ref": "Mapp v. Ohio:lane1_negative"
      },
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
        "journal_ref": "Mapp v. Ohio:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. Iqbal",
          "cluster_id": 145875,
          "cite": [
            "173 L. Ed. 2d 868",
            "129 S. Ct. 1937",
            "556 U.S. 662",
            "2009 U.S. LEXIS 3472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re WINSHIP",
          "cluster_id": 108111,
          "cite": [
            "25 L. Ed. 2d 368",
            "90 S. Ct. 1068",
            "397 U.S. 358",
            "1970 U.S. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gideon v. Wainwright",
          "cluster_id": 106545,
          "cite": [
            "9 L. Ed. 2d 799",
            "83 S. Ct. 792",
            "372 U.S. 335",
            "1963 U.S. LEXIS 1942",
            "93 A.L.R. 2d 733",
            "23 Ohio Op. 2d 258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
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
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mapp v. Ohio:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjE3NTgwODAwMDAwJnM9NDg3MDgyOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MDY1JnM9MTA3OTgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
        "reviewed": 134,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 134,
        "triage_read": 2,
        "triage_snippet_classified": 132
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106285 OR 9422279 OR 9422280 OR 9422281 OR 9422282)",
    "indexed_citing_opinions": 5734,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106285,
        "count": 5215,
        "count_source": "search"
      },
      {
        "opinion_id": 9422279,
        "count": 658,
        "count_source": "search"
      },
      {
        "opinion_id": 9422280,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422281,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422282,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 9090,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mapp-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNzI2MDImcz0xMDU5NDg2NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106285+OR+9422279+OR+9422280+OR+9422281+OR+9422282%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9422282,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422282,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 98058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 105911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9417418,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9420649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106285,
        "cited_id": 9422279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 98058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 101320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 105911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422279,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422280,
        "cited_id": 9420649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422281,
        "cited_id": 3780866,
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
    "date_created": "2026-07-05T11:39:19Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:42:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mapp v. Ohio (truncated)

```
<div>
<center><b><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span> (1961)</b></center>
<center><h1>MAPP<br>
v.<br>
OHIO.</h1></center>
<center>No. 236.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29, 1961.</center>
<center>Decided June 19, 1961.</center>
APPEAL FROM THE SUPREME COURT OF OHIO.
<p><i>A. L. Kearns</i> argued the cause for appellant. With him on the brief was <i>Walter L. Greene.</i></p>
<p><i>Gertrude Bauer Mahon</i> argued the cause for appellee. With her on the brief was <i>John T. Corrigan.</i></p>
<p><i>Bernard A. Berkman</i> argued the cause for the American Civil Liberties Union et al., as <i>amici curiae,</i> urging reversal. With him on the brief was <i>Rowland Watts.</i></p>
<p>MR. JUSTICE CLARK delivered the opinion of the Court.</p>
<p>Appellant stands convicted of knowingly having had in her possession and under her control certain lewd and lascivious books, pictures, and photographs in violation of § 2905.34 of Ohio's Revised Code.<sup>[1]</sup> As officially stated in the syllabus to its opinion, the Supreme Court of Ohio found that her conviction was valid though "based primarily upon the introduction in evidence of lewd and lascivious books and pictures unlawfully seized during an unlawful search of defendant's home . . . ." <span class="citation no-link">170 Ohio St. 427</span>-428, <span class="citation no-link">166 N. E. 2d 387</span>, 388.</p>
<p><span class="star-pagination">*644</span> On May 23, 1957, three Cleveland police officers arrived at appellant's residence in that city pursuant to information that "a person [was] hiding out in the home, who was wanted for questioning in connection with a recent bombing, and that there was a large amount of policy paraphernalia being hidden in the home." Miss Mapp and her daughter by a former marriage lived on the top floor of the two-family dwelling. Upon their arrival at that house, the officers knocked on the door and demanded entrance but appellant, after telephoning her attorney, refused to admit them without a search warrant. They advised their headquarters of the situation and undertook a surveillance of the house.</p>
<p>The officers again sought entrance some three hours later when four or more additional officers arrived on the scene. When Miss Mapp did not come to the door immediately, at least one of the several doors to the house was forcibly opened<sup>[2]</sup> and the policemen gained admittance. Meanwhile Miss Mapp's attorney arrived, but the officers, having secured their own entry, and continuing in their defiance of the law, would permit him neither to see Miss Mapp nor to enter the house. It appears that Miss Mapp was halfway down the stairs from the upper floor to the front door when the officers, in this highhanded manner, broke into the hall. She demanded to see the search warrant. A paper, claimed to be a warrant, was held up by one of the officers. She grabbed the "warrant" and placed it in her bosom. A struggle ensued in which the officers recovered the piece of paper and as a result of which they handcuffed appellant because she had been "belligerent" <span class="star-pagination">*645</span> in resisting their official rescue of the "warrant" from her person. Running roughshod over appellant, a policeman "grabbed" her, "twisted [her] hand," and she "yelled [and] pleaded with him" because "it was hurting." Appellant, in handcuffs, was then forcibly taken upstairs to her bedroom where the officers searched a dresser, a chest of drawers, a closet and some suitcases. They also looked into a photo album and through personal papers belonging to the appellant. The search spread to the rest of the second floor including the child's bedroom, the living room, the kitchen and a dinette. The basement of the building and a trunk found therein were also searched. The obscene materials for possession of which she was ultimately convicted were discovered in the course of that widespread search.</p>
<p>At the trial no search warrant was produced by the prosecution, nor was the failure to produce one explained or accounted for. At best, "There is, in the record, considerable doubt as to whether there ever was any warrant for the search of defendant's home." 170 Ohio St., at 430, 166 N. E. 2d, at 389. The Ohio Supreme Court believed a "reasonable argument" could be made that the conviction should be reversed "because the `methods' employed to obtain the [evidence] . . . were such as to `offend "a sense of justice," ' " but the court found determinative the fact that the evidence had not been taken "from defendant's person by the use of brutal or offensive physical force against defendant." 170 Ohio St., at 431, 166 N. E. 2d, at 389-390.</p>
<p>The State says that even if the search were made without authority, or otherwise unreasonably, it is not prevented from using the unconstitutionally seized evidence at trial, citing <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), in which this Court did indeed hold "that in a prosecution in a State court for a State crime the Fourteenth Amendment <span class="star-pagination">*646</span> does not forbid the admission of evidence obtained by an unreasonable search and seizure." At p. 33. On this appeal, of which we have noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./364/868/">364 U. S. 868</a></span>, it is urged once again that we review that holding.<sup>[3]</sup></p>
<p></p>
<h2>I.</h2>
<p>Seventy-five years ago, in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), considering the Fourth<sup>[4]</sup> and Fifth Amendments as running "almost into each other"<sup>[5]</sup> on the facts before it, this Court held that the doctrines of those Amendments</p>
<blockquote>"apply to all invasions on the part of the government and its employes of the sanctity of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, <span class="star-pagination">*647</span> that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property . . . . Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within the condemnation . . . [of those Amendments]."</blockquote>
<p>The Court noted that</p>
<blockquote>"constitutional provisions for the security of person and property should be liberally construed. . . . It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon." At p. 635.</blockquote>
<p>In this jealous regard for maintaining the integrity of individual rights, the Court gave life to Madison's prediction that "independent tribunals of justice . . . will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." I Annals of Cong. 439 (1789). Concluding, the Court specifically referred to the use of the evidence there seized as "unconstitutional." At p. 638.</p>
<p>Less than 30 years after <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>,</i> this Court, in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), stated that</p>
<blockquote>"the Fourth Amendment . . . put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints [and] . . . forever secure[d] the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law . . . and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws." At pp. 391-392.</blockquote>
<p><span class="star-pagination">*648</span> Specifically dealing with the use of the evidence unconstitutionally seized, the Court concluded:</p>
<blockquote>"If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land." At p. 393.</blockquote>
<p>Finally, the Court in that case clearly stated that use of the seized evidence involved "a denial of the constitutional rights of the accused." At p. 398. Thus, in the year 1914, in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, this Court "for the first time" held that "in a federal prosecution the Fourth Amendment barred the use of evidence secured through an illegal search and seizure." <i>Wolf</i> v. <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado"><i>Colorado, supra,</i> at 28</a></span>. This Court has ever since required of federal law officers a strict adherence to that command which this Court has held to be a clear, specific, and constitutionally requiredeven if judicially implieddeterrent safeguard without insistence upon which the Fourth Amendment would have been reduced to "a form of words." Holmes, J., <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920). It meant, quite simply, that "conviction by means of unlawful seizures and enforced confessions . . . should find no sanction in the judgments of the courts . . .," <i>Weeks</i> v. <i>United States, supra,</i> at 392, and that such evidence "shall not be used at all." <i>Silverthorne Lumber Co.</i> v. <i>United States, supra,</i> at 392.</p>
<p><span class="star-pagination">*649</span> There are in the cases of this Court some passing references to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule as being one of evidence. But the plain and unequivocal language of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i>and its later paraphrase in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i>to the effect that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule is of constitutional origin, remains entirely undisturbed. In <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927), a unanimous Court declared that "the doctrine [cannot] . . . be tolerated <i>under our constitutional system,</i> that evidences of crime discovered by a federal officer in making a search without lawful warrant may be used against the victim of the unlawful search where a timely challenge has been interposed." At pp. 29-30 (emphasis added). The Court, in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), in unmistakable language restated the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule:</p>
<blockquote>"The striking outcome of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case and those which followed it was the sweeping declaration that the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction if obtained by government officers through a violation of the Amendment." At p. 462.</blockquote>
<p>In <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943), we note this statement:</p>
<blockquote>"[A] conviction in the federal courts, the foundation of which is evidence obtained in disregard of liberties deemed fundamental by the Constitution, cannot stand. <i>Boyd</i> v. <i>United States</i> . . . <i>Weeks</i> v. <i>United States</i> . . . And this Court has, on Constitutional grounds, set aside convictions, both in the federal and state courts, which were based upon confessions `secured by protracted and repeated questioning of ignorant and untutored persons, in whose minds the power of officers was greatly magnified' <span class="star-pagination">*650</span>. . . or `who have been unlawfully held incommunicado without advice of friends or counsel'. . . ." At pp. 339-340.</blockquote>
<p>Significantly in <i><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">McNabb</a></span>,</i> the Court did then pass on to formulate a rule of evidence, saying, "[i]n the view we take of the case, however, it becomes unnecessary to reach the Constitutional issue [for] . . . [t]he principles governing the admissibility of evidence in federal criminal trials have not been restricted . . . to those derived solely from the Constitution." At pp. 340-341.</p>
<p></p>
<h2>II.</h2>
<p>In 1949, 35 years after <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> was announced, this Court, in <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado, supra</a></span></i><i>,</i> again for the first time,<sup>[6]</sup> discussed the effect of the Fourth Amendment upon the States through the operation of the Due Process Clause of the Fourteenth Amendment. It said:</p>
<blockquote>"[W]e have no hesitation in saying that were a State affirmatively to sanction such police incursion into privacy it would run counter to the guaranty of the Fourteenth Amendment." At p. 28.</blockquote>
<p>Nevertheless, after declaring that the "security of one's privacy against arbitrary intrusion by the police" is "implicit in the concept of ordered liberty' and as such enforceable against the States through the Due Process Clause," cf. <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span> (1937), and announcing that it "stoutly adhere[d]" to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> decision, the Court decided that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule would not then be imposed upon the States as "an essential ingredient of the right." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 27-29</a></span>. The Court's reasons for not considering essential to the <span class="star-pagination">*651</span> right to privacy, as a curb imposed upon the States by the Due Process Clause, that which decades before had been posited as part and parcel of the Fourth Amendment's limitation upon federal encroachment of individual privacy, were bottomed on factual considerations.</p>
<p>While they are not basically relevant to a decision that the exclusionary rule is an essential ingredient of the Fourth Amendment as the right it embodies is vouchsafed against the States by the Due Process Clause, we will consider the current validity of the factual grounds upon which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was based.</p>
<p>The Court in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> first stated that "[t]he contrariety of views of the States" on the adoption of the exclusionary rule of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> was "particularly impressive" (at p. 29); and, in this connection, that it could not "brush aside the experience of States which deem the incidence of such conduct by the police too slight to call for a deterrent remedy . . . by overriding the [States'] relevant rules of evidence." At pp. 31-32. While in 1949, prior to the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, almost two-thirds of the States were opposed to the use of the exclusionary rule, now, despite the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, more than half of those since passing upon it, by their own legislative or judicial decision, have wholly or partly adopted or adhered to the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule. See <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, Appendix, pp. 224-232 (1960). Significantly, among those now following the rule is California, which, according to its highest court, was "compelled to reach that conclusion because other remedies have completely failed to secure compliance with the constitutional provisions . . . ." <i>People</i> v. <i>Cahan,</i> <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#445" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434, 445</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#911" aria-description="Citation for case: People v. Cahan">282 P. 2d 905, 911</a></span> (1955). In connection with this California case, we note that the second basis elaborated in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> in support of its failure to enforce the exclusionary doctrine against the States was that "other means of protection" have been afforded "the <span class="star-pagination">*652</span> right to privacy."<sup>[7]</sup> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#30" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 30</a></span>. The experience of California that such other remedies have been worthless and futile is buttressed by the experience of other States. The obvious futility of relegating the Fourth Amendment to the protection of other remedies has, moreover, been <span class="star-pagination">*653</span> recognized by this Court since <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> See <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#137" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 137</a></span> (1954).</p>
<p>Likewise, time has set its face against what <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> called the "weighty testimony" of <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (1926). There Justice (then Judge) Cardozo, rejecting adoption of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule in New York, had said that "[t]he Federal rule as it stands is either too strict or too lax." <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#22" aria-description="Citation for case: People v. Defore">242 N. Y., at 22</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E., at 588</a></span>. However, the force of that reasoning has been largely vitiated by later decisions of this Court. These include the recent discarding of the "silver platter" doctrine which allowed federal judicial use of evidence seized in violation of the Constitution by state agents, <i>Elkins</i> v. <i>United States, supra</i><i>;</i> the relaxation of the formerly strict requirements as to standing to challenge the use of evidence thus seized, so that now the procedure of exclusion, "ultimately referable to constitutional safeguards," is available to anyone even "legitimately on [the] premises" unlawfully searched, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span> (1960); and, finally, the formulation of a method to prevent state use of evidence unconstitutionally seized by federal agents, <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span> (1956). Because there can be no fixed formula, we are admittedly met with "recurring questions of the reasonableness of searches," but less is not to be expected when dealing with a Constitution, and, at any rate, "[r]easonableness is in the first instance for the [trial court] . . . to determine." <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63</a></span> (1950).</p>
<p>It, therefore, plainly appears that the factual considerations supporting the failure of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> Court to include the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule when it recognized the enforceability of the right to privacy against the States in 1949, while not basically relevant to the constitutional consideration, could not, in any analysis, now be deemed controlling.</p>
<p></p>
<h2>
<span class="star-pagination">*654</span> III.</h2>
<p>Some five years after <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> in answer to a plea made here Term after Term that we overturn its doctrine on applicability of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule, this Court indicated that such should not be done until the States had "adequate opportunity to adopt or reject the [<span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States"><i>Weeks</i></a></span>] rule." <i>Irvine</i> v. <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#134" aria-description="Citation for case: Irvine v. California"><i>California, supra,</i> at 134</a></span>. There again it was said:</p>
<blockquote>"Never until June of 1949 did this Court hold the basic search-and-seizure prohibition in any way applicable to the states under the Fourteenth Amendment." <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Ibid.</a></span></i>
</blockquote>
<p>And only last Term, after again carefully re-examining the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> doctrine in <i>Elkins</i> v. <i>United States, supra</i><i>,</i> the Court pointed out that "the controlling principles" as to search and seizure and the problem of admissibility "seemed clear" (at p. 212) until the announcement in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> "that the Due Process Clause of the Fourteenth Amendment does not itself require state courts to adopt the exclusionary rule" of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case. At p. 213. At the same time, the Court pointed out, "the underlying constitutional doctrine which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> established . . . that the Federal Constitution . . . prohibits unreasonable searches and seizures by state officers" had undermined the "foundation upon which the admissibility of stateseized evidence in a federal trial originally rested . . . ." <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Ibid.</a></span></i> The Court concluded that it was therefore obliged to hold, although it chose the narrower ground on which to do so, that all evidence obtained by an unconstitutional search and seizure was inadmissible in a federal court regardless of its source. Today we once again examine <i>Wolf's</i> constitutional documentation of the right to privacy free from unreasonable state intrusion, and, after its dozen years on our books, are led by it to close the only <span class="star-pagination">*655</span> courtroom door remaining open to evidence secured by official lawlessness in flagrant abuse of that basic right, reserved to all persons as a specific guarantee against that very same unlawful conduct. We hold that all evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court.</p>
<p></p>
<h2>IV.</h2>
<p>Since the Fourth Amendment's right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth, it is enforceable against them by the same sanction of exclusion as is used against the Federal Government. Were it otherwise, then just as without the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule the assurance against unreasonable federal searches and seizures would be "a form of words," valueless and undeserving of mention in a perpetual charter of inestimable human liberties, so too, without that rule the freedom from state invasions of privacy would be so ephemeral and so neatly severed from its conceptual nexus with the freedom from all brutish means of coercing evidence as not to merit this Court's high regard as a freedom "implicit in the concept of ordered liberty." At the time that the Court held in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> that the Amendment was applicable to the States through the Due Process Clause, the cases of this Court, as we have seen, had steadfastly held that as to federal officers the Fourth Amendment included the exclusion of the evidence seized in violation of its provisions. Even <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> "stoutly adhered" to that proposition. The right to privacy, when conceded operatively enforceable against the States, was not susceptible of destruction by avulsion of the sanction upon which its protection and enjoyment had always been deemed dependent under the <i>Boyd, Weeks</i> and <i>Silverthorne</i> cases. Therefore, in extending the substantive protections of due process to all constitutionally unreasonable searchesstate or federalit was <span class="star-pagination">*656</span> logically and constitutionally necessary that the exclusion doctrinean essential part of the right to privacybe also insisted upon as an essential ingredient of the right newly recognized by the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case. In short, the admission of the new constitutional right by <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> could not consistently tolerate denial of its most important constitutional privilege, namely, the exclusion of the evidence which an accused had been forced to give by reason of the unlawful seizure. To hold otherwise is to grant the right but in reality to withhold its privilege and enjoyment. Only last year the Court itself recognized that the purpose of the exclusionary rule "is to deterto compel respect for the constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States, supra,</i> at 217.</p>
<p>Indeed, we are aware of no restraint, similar to that rejected today, conditioning the enforcement of any other basic constitutional right. The right to privacy, no less important than any other right carefully and particularly reserved to the people, would stand in marked contrast to all other rights declared as "basic to a free society." <i>Wolf</i> v. <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado"><i>Colorado, supra,</i> at 27</a></span>. This Court has not hesitated to enforce as strictly against the States as it does against the Federal Government the rights of free speech and of a free press, the rights to notice and to a fair, public trial, including, as it does, the right not to be convicted by use of a coerced confession, however logically relevant it be, and without regard to its reliability. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> (1961). And nothing could be more certain than that when a coerced confession is involved, "the relevant rules of evidence" are overridden without regard to "the incidence of such conduct by the police," slight or frequent. Why should not the same rule apply to what is tantamount to coerced testimony by way of unconstitutional seizure of goods, papers, effects, documents, etc.? We find that, <span class="star-pagination">*657</span> as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an "intimate relation"<sup>[8]</sup> in their perpetuation of "principles of humanity and civil liberty [secured] . . . only after years of struggle," <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span> (1897). They express "supplementing phases of the same constitutional purposeto maintain inviolate large areas of personal privacy." <i>Feldman</i> v. <i>United States,</i> <span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#489" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 489-490</a></span> (1944). The philosophy of each Amendment and of each freedom is complementary to, although not dependent upon, that of the other in its sphere of influencethe very least that together they assure in either sphere is that no man is to be convicted on unconstitutional evidence. Cf. <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#173" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 173</a></span> (1952).</p>
<p></p>
<h2>V.</h2>
<p>Moreover, our holding that the exclusionary rule is an essential part of both the Fourth and Fourteenth Amendments is not only the logical dictate of prior cases, but it also makes very good sense. There is no war between the Constitution and common sense. Presently, a federal prosecutor may make no use of evidence illegally seized, but a State's attorney across the street may, although he supposedly is operating under the enforceable prohibitions of the same Amendment. Thus the State, by admitting evidence unlawfully seized, serves to encourage disobedience to the Federal Constitution which it is bound to uphold. Moreover, as was said in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>,</i> "[t]he very essence of a healthy federalism depends upon the avoidance of needless conflict between <span class="star-pagination">*658</span> state and federal courts." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#221" aria-description="Citation for case: Elkins v. United States">364 U. S., at 221</a></span>. Such a conflict, hereafter needless, arose this very Term, in <i>Wilson</i> v. <i>Schnettler,</i> <span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">365 U. S. 381</a></span> (1961), in which, and in spite of the promise made by <i><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">Rea</a></span>,</i> we gave full recognition to our practice in this regard by refusing to restrain a federal officer from testifying in a state court as to evidence unconstitutionally seized by him in the performance of his duties. Yet the double standard recognized until today hardly put such a thesis into practice. In non-exclusionary States, federal officers, being human, were by it invited to and did, as our cases indicate, step across the street to the State's attorney with their unconstitutionally seized evidence. Prosecution on the basis of that evidence was then had in a state court in utter disregard of the enforceable Fourth Amendment. If the fruits of an unconstitutional search had been inadmissible in both state and federal courts, this inducement to evasion would have been sooner eliminated. There would be no need to reconcile such cases as <i><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">Rea</a></span></i> and <i><span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">Schnettler</a></span>,</i> each pointing up the hazardous uncertainties of our heretofore ambivalent approach.</p>
<p>Federal-state cooperation in the solution of crime under constitutional standards will be promoted, if only by recognition of their now mutual obligation to respect the same fundamental criteria in their approaches. "However much in a particular case insistence upon such rules may appear as a technicality that inures to the benefit of a guilty person, the history of the criminal law proves that tolerance of shortcut methods in law enforcement impairs its enduring effectiveness." <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#313" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 313</a></span> (1958). Denying shortcuts to only one of two cooperating law enforcement agencies tends naturally to breed legitimate suspicion of "working arrangements" whose results are equally tainted. <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span> (1927); <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span> (1949).</p>
<p><span class="star-pagination">*659</span> There are those who say, as did Justice (then Judge) Cardozo, that under our constitutional exclusionary doctrine "[t]he criminal is to go free because the constable has blundered." <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y., at 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E., at 587</a></span>. In some cases this will undoubtedly be the result.<sup>[9]</sup> But, as was said in <i><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>,</i> "there is another considerationthe imperative of judicial integrity." <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S., at 222</a></span>. The criminal goes free, if he must, but it is the law that sets him free. Nothing can destroy a government more quickly than its failure to observe its own laws, or worse, its disregard of the charter of its own existence. As Mr. Justice Brandeis, dissenting, said in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 485</a></span> (1928): "Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. . . . If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy." Nor can it lightly be assumed that, as a practical matter, adoption of the exclusionary rule fetters law enforcement. Only last year this Court expressly considered that contention and found that "pragmatic evidence of a sort" to the contrary was not wanting. <i>Elkins</i> v. <i>United States, supra,</i> at 218. The Court noted that</p>
<blockquote>"The federal courts themselves have operated under the exclusionary rule of <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> for almost half a century; <span class="star-pagination">*660</span> yet it has not been suggested either that the Federal Bureau of Investigation<sup>[10]</sup> has thereby been rendered ineffective, or that the administration of criminal justice in the federal courts has thereby been disrupted. Moreover, the experience of the states is impressive. . . . The movement towards the rule of exclusion has been halting but seemingly inexorable." <i>Id.,</i> at 218-219.</blockquote>
<p>The ignoble shortcut to conviction left open to the State tends to destroy the entire system of constitutional restraints on which the liberties of the people rest.<sup>[11]</sup> Having once recognized that the right to privacy embodied in the Fourth Amendment is enforceable against the States, and that the right to be secure against rude invasions of privacy by state officers is, therefore, constitutional in origin, we can no longer permit that right to remain an empty promise. Because it is enforceable in the same manner and to like effect as other basic rights secured by the Due Process Clause, we can no longer permit it to be revocable at the whim of any police officer who, in the name of law enforcement itself, chooses to suspend its enjoyment. Our decision, founded on reason and truth, gives to the individual no more than that which the Constitution guarantees him, to the police officer no less than that to which honest law enforcement is entitled, and, to the courts, that judicial integrity so necessary in the true administration of justice.</p>
<p>The judgment of the Supreme Court of Ohio is reversed and the cause remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p><span class="star-pagination">*661</span> MR. JUSTICE BLACK, concurring.</p>
<p>For nearly fifty years, since the decision of this Court in <i>Weeks</i> v. <i>United States</i><i>,</i><sup>[1]</sup> federal courts have refused to permit the introduction into evidence against an accused of his papers and effects obtained by "unreasonable searches and seizures" in violation of the Fourth Amendment. In <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i><i>,</i> decided in 1948, however, this Court held that "in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure."<sup>[2]</sup> I concurred in that holding on these grounds:</p>
<blockquote>"For reasons stated in my dissenting opinion in <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#68" aria-description="Citation for case: Adamson v. California">332 U. S. 46, 68</a></span>, I agree with the conclusion of the Court that the Fourth Amendment's prohibition of `unreasonable searches and seizures' is enforceable against the states. Consequently, I should be for reversal of this case if I thought the Fourth Amendment not only prohibited `unreasonable searches and seizures,' but also, of itself, barred the use of evidence so unlawfully obtained. But I agree with what appears to be a plain implication of the Court's opinion that the federal exclusionary rule is not a command of the Fourth Amendment but is a judicially created rule of evidence which Congress might negate."<sup>[3]</sup></blockquote>
<p>I am still not persuaded that the Fourth Amendment, standing alone, would be enough to bar the introduction into evidence against an accused of papers and effects seized from him in violation of its commands. For the Fourth Amendment does not itself contain any provision expressly precluding the use of such evidence, and I am <span class="star-pagination">*662</span> extremely doubtful that such a provision could properly be inferred from nothing more than the basic command against unreasonable searches and seizures. Reflection on the problem, however, in the light of cases coming before the Court since <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> has led me to conclude that when the Fourth Amendment's ban against unreasonable searches and seizures is considered together with the Fifth Amendment's ban against compelled self-incrimination, a constitutional basis emerges which not only justifies but actually requires the exclusionary rule.</p>
<p>The close interrelationship between the Fourth and Fifth Amendments, as they apply to this problem,<sup>[4]</sup> has long been recognized and, indeed, was expressly made the ground for this Court's holding in <i>Boyd</i> v. <i>United States</i><i>.</i><sup>[5]</sup> There the Court fully discussed this relationship and declared itself "unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself."<sup>[6]</sup> It was upon this ground that Mr. Justice Rutledge largely relied in his dissenting opinion in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case.<sup>[7]</sup> And, although I rejected the argument at that time, its force has, for me at least, become compelling with the more thorough understanding of the problem brought on by recent cases. In the final analysis, it seems to me that the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine, though perhaps not required by the express language of the Constitution strictly construed, is amply justified from an historical standpoint, soundly based in reason, <span class="star-pagination">*663</span> and entirely consistent with what I regard to be the proper approach to interpretation of our Bill of Rightsan approach well set out by Mr. Justice Bradley in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case:</p>
<blockquote>"[C]onstitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of the courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."<sup>[8]</sup></blockquote>
<p>The case of <i>Rochin</i> v. <i>California</i><i>,</i><sup>[9]</sup> which we decided three years after the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case, authenticated, I think, the soundness of Mr. Justice Bradley's and Mr. Justice Rutledge's reliance upon the interrelationship between the Fourth and Fifth Amendments as requiring the exclusion of unconstitutionally seized evidence. In the <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> case, three police officers, acting with neither a judicial warrant nor probable cause, entered Rochin's home for the purpose of conducting a search and broke down the door to a bedroom occupied by Rochin and his wife. Upon their entry into the room, the officers saw Rochin pick up and swallow two small capsules. They immediately seized him and took him in handcuffs to a hospital where the capsules <span class="star-pagination">*664</span> were recovered by use of a stomach pump. Investigation showed that the capsules contained morphine and evidence of that fact was made the basis of his conviction of a crime in a state court.</p>
<p>When the question of the validity of that conviction was brought here, we were presented with an almost perfect example of the interrelationship between the Fourth and Fifth Amendments. Indeed, every member of this Court who participated in the decision of that case recognized this interrelationship and relied on it, to some extent at least, as justifying reversal of Rochin's conviction. The majority, though careful not to mention the Fifth Amendment's provision that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself," showed at least that it was not unaware that such a provision exists, stating: "Coerced confessions offend the community's sense of fair play and decency . . . . It would be a stultification of the responsibility which the course of constitutional history has cast upon this Court to hold that in order to convict a man the police cannot extract by force what is in his mind but can extract what is in his stomach."<sup>[10]</sup> The methods used by the police thus were, according to the majority, "too close to the rack and the screw to permit of constitutional differentiation,"<sup>[11]</sup> and the case was reversed on the ground that these methods had violated the Due Process Clause of the Fourteenth Amendment in that the treatment accorded Rochin was of a kind that "shocks the conscience," "offend[s] `a sense of justice' " and fails to "respect certain decencies of civilized conduct."<sup>[12]</sup></p>
<p>I concurred in the reversal of the <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> case, but on the ground that the Fourteenth Amendment made the Fifth Amendment's provision against self-incrimination <span class="star-pagination">*665</span> applicable to the States and that, given a broad rather than a narrow construction, that provision barred the introduction of this "capsule" evidence just as much as it would have forbidden the use of words Rochin might have been coerced to speak.<sup>[13]</sup> In reaching this conclusion I cited and relied on the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case, the constitutional doctrine of which was, of course, necessary to my disposition of the case. At that time, however, these views were very definitely in the minority for only MR. JUSTICE DOUGLAS and I rejected the flexible and uncertain standards of the "shock-the-conscience test" used in the majority opinion.<sup>[14]</sup></p>
<p>Two years after <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span>,</i> in <i>Irvine</i> v. <i>California</i><i>,</i><sup>[15]</sup> we were again called upon to consider the validity of a conviction based on evidence which had been obtained in a manner clearly unconstitutional and arguably shocking to the conscience. The five opinions written by this Court in that case demonstrate the utter confusion and uncertainty that had been brought about by the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> decisions. In concurring, MR. JUSTICE CLARK emphasized the unsatisfactory nature of the Court's "shock-the-conscience test," saying that this "test" "makes for such uncertainty and unpredictability that it would be impossible to foretellother than by guessworkjust how brazen the invasion of the intimate privacies of one's home must be in order to shock itself into the protective arms of the Constitution. In truth, the practical result of this <i>ad hoc</i> approach is simply that when five Justices are sufficiently revolted by local police action, a conviction is overturned and a guilty man may go free."<sup>[16]</sup></p>
<p><span class="star-pagination">*666</span> Only one thing emerged with complete clarity from the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> casethat is that seven Justices rejected the "shock-the-conscience" constitutional standard enunciated in the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> cases. But even this did not lessen the confusion in this area of the law because the continued existence of mutually inconsistent precedents together with the Court's inability to settle upon a majority opinion in the <i><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">Irvine</a></span></i> case left the situation at least as uncertain as it had been before.<sup>[17]</sup> Finally, today, we clear up that uncertainty. As I understand the Court's opinion in this case, we again reject the confusing "shock-the-conscience" standard of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> and <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> cases and, instead, set aside this state conviction in reliance upon the precise, intelligible and more predictable constitutional doctrine enunciated in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. I fully agree with Mr. Justice Bradley's opinion that the two Amendments upon which the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine rests are of vital importance in our constitutional scheme of liberty and that both are entitled to a liberal rather than a niggardly interpretation. The courts of the country are entitled to know with as much certainty as possible what scope they cover. The Court's opinion, in my judgment, dissipates the doubt and uncertainty in this field of constitutional law and I am persuaded, for this and other reasons stated, to depart from my prior views, to accept the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> doctrine as controlling in this state case and to join the Court's judgment and opinion which are in accordance with that constitutional doctrine.</p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>Though I have joined the opinion of the Court, I add a few words. This criminal proceeding started with a lawless search and seizure. The police entered a home <span class="star-pagination">*667</span> forcefully, and seized documents that were later used to convict the occupant of a crime.</p>
<p>She lived alone with her fifteen-year-old daughter in the second-floor flat of a duplex in Cleveland. At about 1:30 in the afternoon of May 23, 1957, three policemen arrived at this house. They rang the bell, and the appellant, appearing at her window, asked them what they wanted. According to their later testimony, the policemen had come to the house on information from "a confidential source that there was a person hiding out in the home, who was wanted for questioning in connection with a recent bombing."<sup>[1]</sup> To the appellant's question, however, they replied only that they wanted to question her and would not state the subject about which they wanted to talk.</p>
<p>The appellant, who had retained an attorney in connection with a pending civil matter, told the police she would call him to ask if she should let them in. On her attorney's advice, she told them she would let them in only when they produced a valid search warrant. For the next two and a half hours, the police laid siege to the house. At four o'clock, their number was increased to at least seven. Appellant's lawyer appeared on the scene; and one of the policemen told him that they now had a search warrant, but the officer refused to show it. Instead, going to the back door, the officer first tried to kick it in and, when that proved unsuccessful, he broke the glass in the door and opened it from the inside.</p>
<p>The appellant, who was on the steps going up to her flat, demanded to see the search warrant; but the officer refused to let her see it although he waved a paper in front of her face. She grabbed it and thrust it down the front of her dress. The policemen seized her, took the paper <span class="star-pagination">*668</span> from her, and had her handcuffed to another officer. She was taken upstairs, thus bound, and into the larger of the two bedrooms in the apartment; there she was forced to sit on the bed. Meanwhile, the officers entered the house and made a complete search of the four rooms of her flat and of the basement of the house.</p>
<p>The testimony concerning the search is largely nonconflicting. The approach of the officers; their long wait outside the home, watching all its doors; the arrival of reinforcements armed with a paper;<sup>[2]</sup> breaking into the house; putting their hands on appellant and handcuffing her; numerous officers ransacking through every room and piece of furniture, while the appellant sat, a prisoner in her own bedroom. There is direct conflict in the testimony, however, as to where the evidence which is the basis of this case was found. To understand the meaning of that conflict, one must understand that this case is based on the knowing possession<sup>[3]</sup> of four little pamphlets, a couple of photographs and a little pencil doodleall of which are alleged to be pornographic.</p>
<p>According to the police officers who participated in the search, these articles were found, some in appellant's <span class="star-pagination">*669</span> dressers and some in a suitcase found by her bed. According to appellant, most of the articles were found in a cardboard box in the basement; one in the suitcase beside her bed. All of this material, appellantand a friend of herssaid were odds and ends belonging to a recent boarder, a man who had left suddenly for New York and had been detained there. As the Supreme Court of Ohio read the statute under which appellant is charged, she is guilty of the crime whichever story is true.</p>
<p>The Ohio Supreme Court sustained the conviction even though it was based on the documents obtained in the lawless search. For in Ohio evidence obtained by an unlawful search and seizure is admissible in a criminal prosecution at least where it was not taken from the "defendant's person by the use of brutal or offensive force against defendant." <i>State</i> v. <i>Mapp,</i> <span class="citation no-link">170 Ohio St. 427</span>, 166 N. E. 2d, at 388, syllabus 2; <i>State</i> v. <i>Lindway,</i> <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span>. This evidence would have been inadmissible in a federal prosecution. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>. For, as stated in the former decision, "The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints . . . ." <i>Id.,</i> 391-392. It was therefore held that evidence obtained (which in that case was documents and correspondence) from a home without any warrant was not admissible in a federal prosecution.</p>
<p>We held in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, that the Fourth Amendment was applicable to the States by reason of the Due Process Clause of the Fourteenth Amendment. But a majority held that the exclusionary rule of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case was not required of the States, that they could apply such sanctions as they chose. That position had the necessary votes to carry the day. But with all respect it was not the voice of reason or principle.</p>
<p><span class="star-pagination">*670</span> As stated in the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> case, if evidence seized in violation of the Fourth Amendment can be used against an accused, "his right to be secure against such searches and seizures is of no value, and . . . might as well be stricken from the Constitution." <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S., at 393</a></span>.</p>
<p>When we allowed States to give constitutional sanction to the "shabby business" of unlawful entry into a home (to use an expression of Mr. Justice Murphy, <i>Wolf</i> v. <i>Colorado</i><i>,</i> at 46), we did indeed rob the Fourth Amendment of much meaningful force. There are, of course, other theoretical remedies. One is disciplinary action within the hierarchy of the police system, including prosecution of the police officer for a crime. Yet as Mr. Justice Murphy said in <i>Wolf</i> v. <i>Colorado</i><i>,</i> at 42, "Self-scrutiny is a lofty ideal, but its exaltation reaches new heights if we expect a District Attorney to prosecute himself or his associates for well-meaning violations of the search and seizure clause during a raid the District Attorney or his associates have ordered."</p>
<p>The only remaining remedy, if exclusion of the evidence is not required, is an action of trespass by the homeowner against the offending officer. Mr. Justice Murphy showed how onerous and difficult it would be for the citizen to maintain that action and how meagre the relief even if the citizen prevails. <span class="citation multiple-matches"><a href="/c/U.%20S./338/42/">338 U. S. 42</a></span>-44. The truth is that trespass actions against officers who make unlawful searches and seizures are mainly illusory remedies.</p>
<p>Without judicial action making the exclusionary rule applicable to the States, <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i> in practical effect reduced the guarantee against unreasonable searches and seizures to "a dead letter," as Mr. Justice Rutledge said in his dissent. See 338 U. S., at 47.</p>
<p><i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado, supra</a></span></i><i>,</i> was decided in 1949. The immediate result was a storm of constitutional controversy which only today finds its end. I believe that this is an appropriate case in which to put an end to the asymmetry which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> imported into the law. See <span class="star-pagination">*671</span> <i>Stefanelli</i> v. <i>Minard,</i> <span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117</a></span>; <i>Rea</i> v. <i>United States,</i> <span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>; <i>Elkins</i> v. <i>United States, supra</i><i>; </i><i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span>. It is an appropriate case because the facts it presents showas would few other cases the casual arrogance of those who have the untrammelled power to invade one's home and to seize one's person.</p>
<p>It is also an appropriate case in the narrower and more technical sense. The issues of the illegality of the search and the admissibility of the evidence have been presented to the state court and were duly raised here in accordance with the applicable Rule of Practice.<sup>[4]</sup> The question was raised in the notice of appeal, the jurisdictional statement and in appellant's brief on the merits.<sup>[5]</sup> It is true that argument was mostly directed to another issue in the case, but that is often the fact. See <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#535" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 535-540</a></span>. Of course, an earnest advocate of a position always believes that, had he only an additional opportunity for argument, his side would win. But, subject to the sound discretion of a court, all argument must at last come to a halt. This is especially so as to an issue about which this Court said last year that "The arguments of its antagonists and of its proponents have been so many times marshalled as to require no lengthy elaboration here." <i>Elkins</i> v. <i>United States, supra,</i> 216.</p>
<p>Moreover, continuance of <i>Wolf</i> v. <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Colorado</a></span></i> in its full vigor breeds the unseemly shopping around of the kind revealed in <i>Wilson</i> v. <i>Schnettler,</i> <span class="citation" data-id="9422132"><a href="/opinion/106180/wilson-v-schnettler/" aria-description="Citation for case: Wilson v. Schnettler">365 U. S. 381</a></span>. Once evidence, inadmissible in a federal court, is admissible in <span class="star-pagination">*672</span> a state court a "double standard" exists which, as the Court points out, leads to "working arrangements" that undercut federal policy and reduce some aspects of law enforcement to shabby business. The rule that supports that practice does not have the force of reason behind it.</p>
<p>Memorandum of MR. JUSTICE STEWART.</p>
<p>Agreeing fully with Part I of MR. JUSTICE HARLAN'S dissenting opinion, I express no view as to the merits of the constitutional issue which the Court today decides. I would, however, reverse the judgment in this case, because I am persuaded that the provision of § 2905.34 of the Ohio Revised Code, upon which the petitioner's conviction was based, is, in the words of MR. JUSTICE HARLAN, not "consistent with the rights of free thought and expression assured against state action by the Fourteenth Amendment."</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE FRANKFURTER and MR. JUSTICE WHITTAKER join, dissenting.</p>
<p>In overruling the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case the Court, in my opinion, has forgotten the sense of judicial restraint which, with due regard for <i>stare decisis,</i> is one element that should enter into deciding whether a past decision of this Court should be overruled. Apart from that I also believe that the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> rule represents sounder Constitutional doctrine than the new rule which now replaces it.</p>
<p></p>
<h2>I.</h2>
<p>From the Court's statement of the case one would gather that the central, if not controlling, issue on this appeal is whether illegally state-seized evidence is Constitutionally admissible in a state prosecution, an issue which would of course face us with the need for re-examining <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> However, such is not the situation. For, although that question was indeed raised here and below among appellant's subordinate points, the new and <span class="star-pagination">*673</span> pivotal issue brought to the Court by this appeal is whether § 2905.34 of the Ohio Revised Code making criminal the <i>mere</i> knowing possession or control of obscene material,<sup>[1]</sup> and under which appellant has been convicted, is consistent with the rights of free thought and expression assured against state action by the Fourteenth Amendment.<sup>[2]</sup> That was the principal issue which was decided by the Ohio Supreme Court,<sup>[3]</sup> which was tendered by appellant's Jurisdictional Statement,<sup>[4]</sup> and which was briefed<sup>[5]</sup> and argued<sup>[6]</sup> in this Court.</p>
<p><span class="star-pagination">*674</span> In this posture of things, I think it fair to say that five members of this Court have simply "reached out" to overrule <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i> With all respect for the views of the majority, and recognizing that <i>stare decisis</i> carries different <span class="star-pagination">*675</span> weight in Constitutional adjudication than it does in nonconstitutional decision, I can perceive no justification for regarding this case as an appropriate occasion for re-examining <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i></p>
<p>The action of the Court finds no support in the rule that decision of Constitutional issues should be avoided wherever possible. For in overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> the Court, instead of passing upon the validity of Ohio's § 2905.34, has simply chosen between two Constitutional questions. Moreover, I submit that it has chosen the more difficult and less appropriate of the two questions. The Ohio statute which, as construed by the State Supreme Court, punishes knowing possession or control of obscene material, irrespective of the purposes of such possession or control (with exceptions not here applicable)<sup>[7]</sup> and irrespective of whether the accused had any reasonable opportunity to rid himself of the material after discovering that it was obscene,<sup>[8]</sup> surely presents a Constitutional <span class="star-pagination">*676</span> question which is both simpler and less far-reaching than the question which the Court decides today. It seems to me that justice might well have been done in this case without overturning a decision on which the administration of criminal law in many of the States has long justifiably relied.</p>
<p>Since the demands of the case before us do not require us to reach the question of the validity of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> I think this case furnishes a singularly inappropriate occasion for reconsideration of that decision, if reconsideration is indeed warranted. Even the most cursory examination will reveal that the doctrine of the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> case has been of continuing importance in the administration of state criminal law. Indeed, certainly as regards its "non-exclusionary" aspect, <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> did no more than articulate the then existing assumption among the States that the federal cases enforcing the exclusionary rule "do not bind [the States], for they construe provisions of the Federal Constitution, the Fourth and Fifth Amendments, not applicable to the States." <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#20" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 20</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span>. Though, of course, not reflecting the full measure of this continuing reliance, I find that during the last three Terms, for instance, the issue of the inadmissibility of illegally state-obtained evidence appears on an average of about fifteen times per Term just in the <i>in forma pauperis</i> cases summarily disposed of by us. This would indicate both that the issue which is now being decided may well have untoward practical ramifications respecting state cases long since disposed of in reliance on <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> and that were we determined to re-examine that doctrine we would not lack future opportunity.</p>
<p>The occasion which the Court has taken here is in the context of a case where the question was briefed not at all and argued only extremely tangentially. The unwisdom of overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> without full-dress argument <span class="star-pagination">*677</span> is aggravated by the circumstance that that decision is a comparatively recent one (1949) to which three members of the present majority have at one time or other expressly subscribed, one to be sure with explicit misgivings.<sup>[9]</sup> I would think that our obligation to the States, on whom we impose this new rule, as well as the obligation of orderly adherence to our own processes would demand that we seek that aid which adequate briefing and argument lends to the determination of an important issue. It certainly has never been a postulate of judicial power that mere altered disposition, or subsequent membership on the Court, is sufficient warrant for overturning a deliberately decided rule of Constitutional law.</p>
<p>Thus, if the Court were bent on reconsidering <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> I think that there would soon have presented itself an appropriate opportunity in which we could have had the benefit of full briefing and argument. In any event, at the very least, the present case should have been set down for reargument, in view of the inadequate briefing and argument we have received on the <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> point. To all intents and purposes the Court's present action amounts to a summary reversal of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> without argument.</p>
<p>I am bound to say that what has been done is not likely to promote respect either for the Court's adjudicatory process or for the stability of its decisions. Having been unable, however, to persuade any of the majority to a different procedural course, I now turn to the merits of the present decision.</p>
<p></p>
<h2>
<span class="star-pagination">*678</span> II.</h2>
<p>Essential to the majority's argument against <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> is the proposition that the rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, excluding in federal criminal trials the use of evidence obtained in violation of the Fourth Amendment, derives not from the "supervisory power" of this Court over the federal judicial system, but from Constitutional requirement. This is so because no one, I suppose, would suggest that this Court possesses any general supervisory power over the state courts. Although I entertain considerable doubt as to the soundness of this foundational proposition of the majority, cf. <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 39-40</a></span> (concurring opinion), I shall assume, for present purposes, that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule "is of constitutional origin."</p>
<p>At the heart of the majority's opinion in this case is the following syllogism: (1) the rule excluding in federal criminal trials evidence which is the product of an illegal search and seizure is "part and parcel" of the Fourth Amendment; (2) <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> held that the "privacy" assured against federal action by the Fourth Amendment is also protected against state action by the Fourteenth Amendment; and (3) it is therefore "logically and constitutionally necessary" that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule should also be enforced against the States.<sup>[10]</sup></p>
<p>This reasoning ultimately rests on the unsound premise that because <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> carried into the States, as part of "the concept of ordered liberty" embodied in the Fourteenth Amendment, the principle of "privacy" underlying the Fourth Amendment (338 U. S., at 27), it must follow that whatever configurations of the Fourth Amendment have been developed in the particularizing federal precedents are likewise to be deemed a part of "ordered liberty," <span class="star-pagination">*679</span> and as such are enforceable against the States. For me, this does not follow at all.</p>
<p>It cannot be too much emphasized that what was recognized in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was not that the Fourth Amendment <i>as such</i> is enforceable against the States as a facet of due process, a view of the Fourteenth Amendment which, as <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> itself pointed out (338 U. S., at 26), has long since been discredited, but the principle of privacy "which is at the core of the Fourth Amendment." (<i>Id.,</i> at 27.) It would not be proper to expect or impose any precise equivalence, either as regards the scope of the right or the means of its implementation, between the requirements of the Fourth and Fourteenth Amendments. For the Fourth, unlike what was said in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> of the Fourteenth, does not state a general principle only; it is a particular command, having its setting in a pre-existing legal context on which both interpreting decisions and enabling statutes must at least build.</p>
<p>Thus, even in a case which presented simply the question of whether a particular search and seizure was constitutionally "unreasonable"say in a tort action against state officerswe would not be true to the Fourteenth Amendment were we merely to stretch the general principle of individual privacy on a Procrustean bed of federal precedents under the Fourth Amendment. But in this instance more than that is involved, for here we are reviewing not a determination that what the state police did was Constitutionally permissible (since the state court quite evidently assumed that it was not), but a determination that appellant was properly found guilty of conduct which, for present purposes, it is to be assumed the State could Constitutionally punish. Since there is not the slightest suggestion that Ohio's policy is "affirmatively to sanction . . . police incursion into privacy" (338 U. S., at 28), compare <i>Marcus</i> v. <i>Search Warrants, post,</i> p. 717, what the Court is now doing is to impose <span class="star-pagination">*680</span> upon the States not only federal substantive standards of "search and seizure" but also the basic federal remedy for violation of those standards. For I think it entirely clear that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule is but a remedy which, by penalizing past official misconduct, is aimed at deterring such conduct in the future.</p>
<p>I would not impose upon the States this federal exclusionary remedy. The reasons given by the majority for now suddenly turning its back on <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> seem to me notably unconvincing.</p>
<p>First, it is said that "the factual grounds upon which <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was based" have since changed, in that more States now follow the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule than was so at the time <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> was decided. While that is true, a recent survey indicates that at present one-half of the States still adhere to the common-law non-exclusionary rule, and one, Maryland, retains the rule as to felonies. Berman and Oberst, Admissibility of Evidence Obtained by an Unconstitutional Search and Seizure, 55 N. W. L. Rev. 525, 532-533. But in any case surely all this is beside the point, as the majority itself indeed seems to recognize. Our concern here, as it was in <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> is not with the desirability of that rule but only with the question whether the States are Constitutionally free to follow it or not as they may themselves determine, and the relevance of the disparity of views among the States on this point lies simply in the fact that the judgment involved is a debatable one. Moreover, the very fact on which the majority relies, instead of lending support to what is now being done, points away from the need of replacing voluntary state action with federal compulsion.</p>
<p>The preservation of a proper balance between state and federal responsibility in the administration of criminal justice demands patience on the part of those who might like to see things move faster among the States in this respect. Problems of criminal law enforcement vary <span class="star-pagination">*681</span> widely from State to State. One State, in considering the totality of its legal picture, may conclude that the need for embracing the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule is pressing because other remedies are unavailable or inadequate to secure compliance with the substantive Constitutional principle involved. Another, though equally solicitous of Constitutional rights, may choose to pursue one purpose at a time, allowing all evidence relevant to guilt to be brought into a criminal trial, and dealing with Constitutional infractions by other means. Still another may consider the exclusionary rule too rough-and-ready a remedy, in that it reaches only unconstitutional intrusions which eventuate in criminal prosecution of the victims. Further, a State after experimenting with the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule for a time may, because of unsatisfactory experience with it, decide to revert to a non-exclusionary rule. And so on. From the standpoint of Constitutional permissibility in pointing a State in one direction or another, I do not see at all why "time has set its face against" the considerations which led Mr. Justice Cardozo, then chief judge of the New York Court of Appeals, to reject for New York in <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span>, the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule. For us the question remains, as it has always been, one of state power, not one of passing judgment on the wisdom of one state course or another. In my view this Court should continue to forbear from fettering the States with an adamant rule which may embarrass them in coping with their own peculiar problems in criminal law enforcement.</p>
<p>Further, we are told that imposition of the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule on the States makes "very good sense," in that it will promote recognition by state and federal officials of their "mutual obligation to respect the same fundamental criteria" in their approach to law enforcement, and will avoid " `needless conflict between state and federal courts.' " Indeed the majority now finds an incongruity <span class="star-pagination">*682</span> in <i>Wolf's</i> discriminating perception between the demands of "ordered liberty" as respects the basic right of "privacy" and the means of securing it among the States. That perception, resting both on a sensitive regard for our federal system and a sound recognition of this Court's remoteness from particular state problems, is for me the strength of that decision.</p>
<p>An approach which regards the issue as one of achieving procedural symmetry or of serving administrative convenience surely disfigures the boundaries of this Court's functions in relation to the state and federal courts. Our role in promulgating the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule and its extensions in such cases as <i>Rea, Elkins,</i> and <i>Rios</i><sup>[11]</sup> was quite a different one than it is here. There, in implementing the Fourth Amendment, we occupied the position of a tribunal having the ultimate responsibility for developing the standards and procedures of judicial administration within the judicial system over which it presides. Here we review state procedures whose measure is to be taken not against the specific substantive commands of the Fourth Amendment but under the flexible contours of the Due Process Clause. I do not believe that the Fourteenth Amendment empowers this Court to mould state remedies effectuating the right to freedom from "arbitrary intrusion by the police" to suit its own notions of how things should be done, as, for instance, the California Supreme Court did in <i>People</i> v. <i>Cahan,</i> <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span>, with reference to procedures in the California courts or as this Court did in <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> for the lower federal courts.</p>
<p>A state conviction comes to us as the complete product of a sovereign judicial system. Typically a case will have been tried in a trial court, tested in some final appellate <span class="star-pagination">*683</span> court, and will go no further. In the comparatively rare instance when a conviction is reviewed by us on due process grounds we deal then with a finished product in the creation of which we are allowed no hand, and our task, far from being one of over-all supervision, is, speaking generally, restricted to a determination of whether the prosecution was Constitutionally fair. The specifics of trial procedure, which in every mature legal system will vary greatly in detail, are within the sole competence of the States. I do not see how it can be said that a trial becomes unfair simply because a State determines that evidence may be considered by the trier of fact, regardless of how it was obtained, if it is relevant to the one issue with which the trial is concerned, the guilt or innocence of the accused. Of course, a court may use its procedures as an incidental means of pursuing other ends than the correct resolution of the controversies before it. Such indeed is the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule, but if a State does not choose to use its courts in this way, I do not believe that this Court is empowered to impose this much-debated procedure on local courts, however efficacious we may consider the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> rule to be as a means of securing Constitutional rights.</p>
<p>Finally, it is said that the overruling of <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> is supported by the established doctrine that the admission in evidence of an involuntary confession renders a state conviction Constitutionally invalid. Since such a confession may often be entirely reliable, and therefore of the greatest relevance to the issue of the trial, the argument continues, this doctrine is ample warrant in precedent that the way evidence was obtained, and not just its relevance, is Constitutionally significant to the fairness of a trial. I believe this analogy is not a true one. The "coerced confession" rule is certainly not a rule that any illegally obtained statements may not be used in evidence. I would suppose that a statement which is procured during <span class="star-pagination">*684</span> a period of illegal detention, <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>, is, as much as unlawfully seized evidence, illegally obtained, but this Court has consistently refused to reverse state convictions resting on the use of such statements. Indeed it would seem the Court laid at rest the very argument now made by the majority when in <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, a state-coerced confession case, it said (at 235):</p>
<blockquote>"It may be assumed [that the] treatment of the petitioner [by the police] . . . deprived him of his liberty without due process and that the petitioner would have been afforded preventive relief if he could have gained access to a court to seek it.</blockquote>
<blockquote>"But illegal acts, as such, committed in the course of obtaining a confession . . . do not furnish an answer to the constitutional question we must decide.. . . The gravamen of his complaint is the unfairness of the <i>use</i> of his confessions, and what occurred in their procurement is relevant only as it bears on that issue." (Emphasis supplied.)</blockquote>
<p>The point, then, must be that in requiring exclusion of an involuntary statement of an accused, we are concerned not with an appropriate remedy for what the police have done, but with something which is regarded as going to the heart of our concepts of fairness in judicial procedure. The operative assumption of our procedural system is that "Ours is the accusatorial as opposed to the inquisitorial system. Such has been the characteristic of Anglo-American criminal justice since it freed itself from practices borrowed by the Star Chamber from the Continent whereby the accused was interrogated in secret for hours on end." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span>. See <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 541</a></span>. The pressures brought to bear against an accused leading to a confession, unlike an unconstitutional violation of privacy, do not, apart <span class="star-pagination">*685</span> from the use of the confession at trial, necessarily involve independent Constitutional violations. What is crucial is that the trial defense to which an accused is entitled should not be rendered an empty formality by reason of statements wrung from him, for then "a prisoner. . . [has been] made the deluded instrument of his own conviction." 2 Hawkins, Pleas of the Crown (8th ed., 1824), c. 46, § 34. That this is a <i>procedural right,</i> and that its violation occurs at the time his improperly obtained statement is admitted at trial, is manifest. For without this right all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.</p>
<p>This, and not the disciplining of the police, as with illegally seized evidence, is surely the true basis for excluding a statement of the accused which was unconstitutionally obtained. In sum, I think the coerced confession analogy works strongly <i>against</i> what the Court does today.</p>
<p>In conclusion, it should be noted that the majority opinion in this case is in fact an opinion only for the <i>judgment</i> overruling <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>,</i> and not for the basic rationale by which four members of the majority have reached that result. For my Brother BLACK is unwilling to subscribe to their view that the <i><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span></i> exclusionary rule derives from the Fourth Amendment itself (see <i>ante,</i> p. 661), but joins the majority opinion on the premise that its end result can be achieved by bringing the Fifth Amendment to the aid of the Fourth (see <i>ante,</i> pp. 662-665).<sup>[12]</sup> On that score I need only say that whatever the validity of <span class="star-pagination">*686</span> the "Fourth-Fifth Amendment" correlation which the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case (<span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>) found, see 8 Wigmore, Evidence (3d ed. 1940), § 2184, we have only very recently again reiterated the long-established doctrine of this Court that the Fifth Amendment privilege against self-incrimination is not applicable to the States. See <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>.</p>
<p>I regret that I find so unwise in principle and so inexpedient in policy a decision motivated by the high purpose of increasing respect for Constitutional rights. But in the last analysis I think this Court can increase respect for the Constitution only if it rigidly respects the limitations which the Constitution places upon it, and respects as well the principles inherent in its own processes. In the present case I think we exceed both, and that our voice becomes only a voice of power, not of reason.</p>
<h2>NOTES</h2>
<p>[1]  The statute provides in pertinent part that
</p>
<p>"No person shall knowingly . . . have in his possession or under his control an obscene, lewd, or lascivious book [or] . . . picture . . . .</p>
<p>"Whoever violates this section shall be fined not less than two hundred nor more than two thousand dollars or imprisoned not less than one nor more than seven years, or both."</p>
<p>[2]  A police officer testified that "we did pry the screen door to gain entrance"; the attorney on the scene testified that a policeman "tried . . . to kick in the door" and then "broke the glass in the door and somebody reached in and opened the door and let them in"; the appellant testified that "The back door was broken."</p>
<p>[3]  Other issues have been raised on this appeal but, in the view we have taken of the case, they need not be decided. Although appellant chose to urge what may have appeared to be the surer ground for favorable disposition and did not insist that <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> be overruled, the <i>amicus curiae,</i> who was also permitted to participate in the oral argument, did urge the Court to overrule <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>.</i></p>
<p>[4]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[5]  The close connection between the concepts later embodied in these two Amendments had been noted at least as early as 1765 by Lord Camden, on whose opinion in <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials 1029, the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> court drew heavily. Lord Camden had noted, at 1073:
</p>
<p>"It is very certain, that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent as well as the guilty, would be both cruel and unjust; and it should seem, that search for evidence is disallowed upon the same principle. There too the innocent would be confounded with the guilty."</p>
<p>[6]  See, however,<i>National Safe Deposit Co.</i> v. <i>Stead,</i> <span class="citation" data-id="98058"><a href="/opinion/98058/national-safe-deposit-co-v-stead/" aria-description="Citation for case: National Safe Deposit Co. v. Stead">232 U. S. 58</a></span> (1914), and <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904).</p>
<p>[7]  Less than half of the States have any criminal provisions relating directly to unreasonable searches and seizures. The punitive sanctions of the 23 States attempting to control such invasions of the right of privacy may be classified as follows:
</p>
<p><i>Criminal Liability of Affiant for Malicious Procurement of Search Warrant.</i>Ala. Code, 1958, Tit. 15, § 99; Alaska Comp. Laws Ann., 1949, § 66-7-15; Ariz. Rev. Stat. Ann., 1956, § 13-1454; <span class="citation no-link">Cal. Pen. Code § 170</span>; Fla. Stat., 1959, § 933.16; Ga. Code Ann., 1953, § 27-301; Idaho Code Ann., 1948, § 18-709; Iowa Code Ann., 1950, § 751.38; Minn. Stat. Ann., 1947, § 613.54; Mont. Rev. Codes Ann., 1947, § 94-35-122; <span class="citation no-link">Nev. Rev. Stat. §§ 199.130</span>, 199.140; N. J. Stat. Ann., 1940, § 33:1-64; N. Y. Pen. Law § 1786, N. Y. Code Crim. Proc. § 811; N. C. Gen. Stat., 1953, § 15-27 (applies to "officers" only); N. D. Century Code Ann., 1960, §§ 12-17-08, 29-29-18; Okla. Stat., 1951, Tit. 21, § 585, Tit. 22, § 1239; Ore. Rev. Stat. § 141.990; S. D. Code, 1939 (Supp. 1960), § 34.9904; Utah Code Ann., 1953, § 77-54-21.</p>
<p><i>Criminal Liability of Magistrate Issuing Warrant Without Supporting Affidavit.</i>N. C. Gen. Stat., 1953, § 15-27; Va. Code Ann., 1960 Replacement Volume, § 19.1-89.</p>
<p><i>Criminal Liability of Officer Willfully Exceeding Authority of Search Warrant.</i>Fla. Stat. Ann., 1944, § 933.17; Iowa Code Ann., 1950, § 751.39; Minn. Stat. Ann., 1947, § 613.54; <span class="citation no-link">Nev. Rev. Stat. § 199.450</span>; N. Y. Pen. Law § 1847, N. Y. Code Crim. Proc. § 812; N. D. Century Code Ann., 1960, §§ 12-17-07, 29-29-19; Okla. Stat., 1951, Tit. 21, § 536, Tit. 22, § 1240; S. D. Code, 1939 (Supp. 1960), § 34.9905; Tenn. Code Ann., 1955, § 40-510; Utah Code Ann., 1953, § 77-54-22.</p>
<p><i>Criminal Liability of Officer for Search with Invalid Warrant or no Warrant.</i>Idaho Code Ann., 1948, § 18-703; Minn. Stat. Ann., 1947, §§ 613.53, 621.17; Mo. Ann. Stat., 1953, § 558.190; Mont. Rev. Codes Ann., 1947, § 94-3506; N. J. Stat. Ann., 1940, § 33:1-65; N. Y. Pen. Law § 1846; N. D. Century Code Ann., 1960, § 12-17-06; Okla. Stat. Ann., 1958, Tit. 21, § 535; Utah Code Ann., 1953, § 76-28-52; Va. Code Ann., 1960 Replacement Volume, § 19.1-88; <span class="citation no-link">Wash. Rev. Code §§ 10.79.040</span>, 10.79.045.</p>
<p>[8]  But compare <i>Waley</i> v. <i>Johnston,</i> <span class="citation" data-id="103660"><a href="/opinion/103660/waley-v-johnston/#104" aria-description="Citation for case: Waley v. Johnston">316 U. S. 101, 104</a></span>, and <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#236" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 236</a></span>, with <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>.</p>
<p>[9]  As is always the case, however, state procedural requirements governing assertion and pursuance of direct and collateral constitutional challenges to criminal prosecutions must be respected. We note, moreover, that the class of state convictions possibly affected by this decision is of relatively narrow compass when compared with <i>Burns</i> v. <i>Ohio,</i> <span class="citation" data-id="9421835"><a href="/opinion/105911/burns-v-ohio/" aria-description="Citation for case: Burns v. Ohio">360 U. S. 252</a></span>, <i>Griffin</i> v. <i>Illinois,</i> <span class="citation" data-id="9421263"><a href="/opinion/105382/griffin-v-illinois/" aria-description="Citation for case: Griffin v. Illinois">351 U. S. 12</a></span>, and <i>Herman</i> v. <i>Claudy,</i> <span class="citation" data-id="105336"><a href="/opinion/105336/pennsylvania-ex-rel-herman-v-claudy/" aria-description="Citation for case: Pennsylvania Ex Rel. Herman v. Claudy">350 U. S. 116</a></span>. In those cases the same contention was urged and later proved unfounded. In any case, further delay in reaching the present result could have no effect other than to compound the difficulties.</p>
<p>[10]  See the remarks of Mr. Hoover, Director of the Federal Bureau of Investigation, FBI Law Enforcement Bulletin, September, 1952, pp. 1-2, quoted in <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 218-219, note 8</a></span>.</p>
<p>[11]  Cf. <i>Marcus</i> v. <i>Search Warrant, post,</i> p. 717.</p>
<p>[1]  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, decided in 1914.</p>
<p>[2]  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#33" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 33</a></span>.</p>
<p>[3]  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado"><i>Id.,</i> at 39-40</a></span>.</p>
<p>[4]  The interrelationship between the Fourth and the Fifth Amendments in this area does not, of course, justify a narrowing in the interpretation of either of these Amendments with respect to areas in which they operate separately. See <i>Feldman</i> v. <i>United States,</i> <span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#502" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 502-503</a></span> (dissenting opinion); <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#374" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 374-384</a></span> (dissenting opinion).</p>
<p>[5]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p>[6]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 633</a></span>.</p>
<p>[7]  338 U. S., at 47-48.</p>
<p>[8]  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S., at 635</a></span>. As the Court points out, Mr. Justice Bradley's approach to interpretation of the Bill of Rights stemmed directly from the spirit in which that great charter of liberty was offered for adoption on the floor of the House of Representatives by its framer, James Madison: "If they [the first ten Amendments] are incorporated into the Constitution, independent tribunals of justice will consider themselves in a peculiar manner the guardians of those rights; they will be an impenetrable bulwark against every assumption of power in the Legislative or Executive; they will be naturally led to resist every encroachment upon rights expressly stipulated for in the Constitution by the declaration of rights." I Annals of Congress 439 (1789).</p>
<p>[9]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>.</p>
<p>[10]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#173" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 173</a></span>.</p>
<p>[11]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 172</a></span>.</p>
<p>[12]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 172, 173</a></span>.</p>
<p>[13]  <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California"><i>Id.,</i> at 174-177</a></span>.</p>
<p>[14]  For the concurring opinion of MR. JUSTICE DOUGLAS see <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#177" aria-description="Citation for case: Rochin v. California"><i>id.,</i> at 177-179</a></span>.</p>
<p>[15]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>[16]  <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#138" aria-description="Citation for case: Irvine v. California"><i>Id.,</i> at 138</a></span>.</p>
<p>[17]  See also <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66-68</a></span> (dissenting opinion).</p>
<p>[1]  This "confidential source" told the police, in the same breath, that "there was a large amount of policy paraphernalia being hidden in the home."</p>
<p>[2]  The purported warrant has disappeared from the case. The State made no attempt to prove its existence, issuance or contents, either at the trial or on the hearing of a preliminary motion to suppress. The Supreme Court of Ohio said: "There is, in the record, considerable doubt as to whether there ever was <i>any</i> warrant for the search of defendant's home. . . . Admittedly . . . there was no warrant authorizing a search . . . for any `lewd, or lascivious book . . . print, [or] picture.' " <span class="citation no-link">170 Ohio St. 427</span>, 430, <span class="citation no-link">166 N. E. 2d 387</span>, 389. (Emphasis added.)</p>
<p>[3]  Ohio Rev. Code, § 2905.34: "No person shall knowingly . . . have in his possession or under his control an obscene, lewd, or lascivious book, magazine, pamphlet, paper, writing, advertisement, circular, print, picture . . . or drawing . . . of an indecent or immoral nature. . . . Whoever violates this section shall be fined not less than two hundred nor more than two thousand dollars or imprisoned not less than one nor more than seven years, or both."</p>
<p>[4]  "The notice of appeal . . . shall set forth the questions presented by the appeal . . . . Only the questions set forth in the notice of appeal or fairly comprised therein will be considered by the court." Rule 10 (2) (c), Rules of the Supreme Court of the United States.</p>
<p>[5]  "Did the conduct of the police in procuring the books, papers and pictures placed in evidence by the Prosecution violate Amendment IV, Amendment V, and Amendment XIV Section 1 of the United States Constitution . . . ?"</p>
<p>[1]  The material parts of that law are quoted in note 1 of the Court's opinion. <i>Ante,</i> p. 643.</p>
<p>[2]  In its note 3, <i>ante,</i> p. 646, the Court, it seems to me, has turned upside down the relative importance of appellant's reliance on the various points made by him on this appeal.</p>
<p>[3]  See <span class="citation no-link">170 Ohio St. 427</span>, <span class="citation no-link">166 N. E. 2d 387</span>. Because of the unusual provision of the Ohio Constitution requiring "the concurrence of at least all but one of the judges" of the Ohio Supreme Court before a state law is held unconstitutional (except in the case of affirmance of a holding of unconstitutionality by the Ohio Court of Appeals), Ohio Const., Art. IV, § 2, the State Supreme Court was compelled to uphold the constitutionality of § 2905.34, despite the fact that four of its seven judges thought the statute offensive to the Fourteenth Amendment.</p>
<p>[4]  Respecting the "substantiality" of the federal questions tendered by this appeal, appellant's Jurisdictional Statement contained the following:
</p>
<p>"The Federal questions raised by this appeal are substantial for the following reasons:</p>
<p>"The Ohio Statute under which the defendant was convicted violates one's sacred right to own and hold property, which has been held inviolate by the Federal Constitution. The right of the individual `to read, to believe or disbelieve, and to think without governmental supervision is one of our basic liberties, but to dictate to the mature adult what books he may have in his own private library seems to be a clear infringement of the constitutional rights of the individual' (Justice Herbert's dissenting Opinion, Appendix `A'). Many convictions have followed that of the defendant in the State Courts of Ohio based upon this very same statute. Unless this Honorable Court hears this matter and determines once and for all that the Statute is unconstitutional as defendant contends, there will be many such appeals. When Sections 2905.34, 2905.37 and 3767.01 of the Ohio Revised Code [the latter two Sections providing exceptions to the coverage of § 2905.34 and related provisions of Ohio's obscenity statutes] are read together, . . . they obviously contravene the Federal and State constitutional provisions; by being convicted under the Statute involved herein, and in the manner in which she was convicted, Defendant-Appellant has been denied due process of law; a sentence of from one (1) to seven (7) years in a penal institution for alleged violation of this unconstitutional section of the Ohio Revised Code deprives the defendant of her right to liberty and the pursuit of happiness, contrary to the Federal and State constitutional provisions, for circumstances which she herself did not put in motion, and is a cruel and unusual punishment 

[...TRUNCATED 6758 of 126758 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Marbury v. Madison.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Marbury v. Madison"
type: case
citation: "5 U.S. 137 (1803)"
parallel_cite: "2 L. Ed. 60; 1 Cranch 137"
neutral_cite: 1803 U.S. LEXIS 352
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1803
date_decided: 1803-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1803-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Marbury v. Madison
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/84759/marbury-v-madison/"
  cluster_id: 84759
  opinion_id: 84759
  identity_checked: false
homes:
  - page: "[[The Federal Court System]]"
    role: "Key — Anchor"
related: []
aliases: []
tags: ["case", "constitutional-law", "judicial-review", "federal-courts", "separation-of-powers"]
holding: "Establishes judicial review: it is the province and duty of the judiciary to say what the law is, and a law repugnant to the…"
lake:
  record_id: Marbury v. Madison
  status: under_review
  projected_at: 2026-07-09
---

# Marbury v. Madison

*5 U.S. (1 Cranch) 137 (1803)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In the final days of the Adams administration, William Marbury was appointed a justice of the peace, but his commission was not delivered before Jefferson took office, and the new Secretary of State, Madison, withheld it. Marbury sued directly in the Supreme Court for a writ of mandamus to compel delivery, invoking a power the Judiciary Act of 1789 purported to grant the Court.

## Issue
Whether the Supreme Court could issue the writ — and, underlying that, whether a court may decline to give effect to an Act of Congress that conflicts with the Constitution.

## Rule
The judiciary determines what the law is and must disregard a statute that conflicts with the Constitution. "It is emphatically the province and duty of the judicial department to say what the law is." — 5 U.S. (1 Cranch) at 177. ^pin-177

And because the Constitution is supreme, "an act of the legislature, repugnant to the constitution, is void." — [*Id.*](https://www.courtlistener.com/opinion/84759/marbury-v-madison/#:~:text=an%20act%20of%20the%20legislature%2C%20repugnant%20to%20the%20constitution%2C%20is%20void.) ^pin-177a

## Application
Marbury was entitled to his commission and mandamus was a proper remedy, but the provision of the Judiciary Act of 1789 that purported to authorize the Supreme Court to issue mandamus in an original action enlarged the Court's original jurisdiction beyond what Article III allows. Confronting that conflict between the statute and the Constitution, the Court applied the principle that it must follow the Constitution and treat the repugnant statutory grant as void; it therefore lacked jurisdiction to issue the writ.

## Conclusion
The Court denied the writ for want of jurisdiction, holding the jurisdiction-expanding statute unconstitutional and establishing the power of judicial review.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Marbury* is the foundational source of judicial review and remains undisturbed; it anchors the structure of the federal court system and the courts' authority to measure statutes against the Constitution.

## Appears on
- [[The Federal Court System]] — *Key — Anchor*

## Sources
- *Marbury v. Madison*, 5 U.S. (1 Cranch) 137 (1803) — https://www.courtlistener.com/opinion/84759/marbury-v-madison/ — pinpoint: 177.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c48eaafcdff4114f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Marbury v. Madison"}, "payload": {"all": [{"cite": "5 U.S. 137", "page": "137", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "5"}, {"cite": "2 L. Ed. 60", "page": "60", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "2"}, {"cite": "1 Cranch 137", "page": "137", "reporter": "Cranch", "selected_official": false, "source": "cluster.citations[]", "type": 5, "volume": "1"}, {"cite": "1803 U.S. LEXIS 352", "page": "352", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1803"}], "display": "5 U.S. 137", "official": {"cite": "5 U.S. 137", "page": "137", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "5"}, "official_selection_present": true, "record_id": "Marbury v. Madison"}}
{"assertion_id": "5abca5619633bc8b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-177", "record_id": "Marbury v. Madison"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-177", "pinpoint_status": "slip-only", "quote": "--- # Marbury v. Madison *5 U.S. (1 Cranch) 137 (1803)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In the final days of the Adams administration, William Marbury was appointed a justice of the peace, but his commission was not delivered before Jefferson took office, and the new Secretary of State, Madison, withheld it. Marbury sued directly in the Supreme Court for a writ of mandamus to compel delivery, invoking a power the Judiciary Act of 1789 purported to grant the Court. ## Issue Whether the Supreme Court could issue the writ — and, underlying that, whether a court may decline to give effect to an Act of Congress that conflicts with the Constitution. ## Rule The judiciary determines what the law is and must disregard a statute that conflicts with the Constitution.", "quote_fidelity": "mismatch", "record_id": "Marbury v. Madison", "star_marker": null}}
{"assertion_id": "cc2e5b4d430ebe43", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-177a", "record_id": "Marbury v. Madison"}, "payload": {"fragment": "#:~:text=an%20act%20of%20the%20legislature%2C%20repugnant%20to%20the%20constitution%2C%20is%20void.", "page": null, "pin_id": "pin-177a", "pinpoint_status": "star-verified", "quote": "an act of the legislature, repugnant to the constitution, is void.", "quote_fidelity": "matched", "record_id": "Marbury v. Madison", "star_marker": "177"}}
{"assertion_id": "fcf3aa5f7fd38438", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Marbury v. Madison"}, "payload": {"as_of_content": "1803-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Marbury v. Madison", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Marbury v. Madison

```json
{
  "schema_version": "s2.v1",
  "record_id": "Marbury v. Madison",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Marbury v. Madison",
    "case_name_short": "Marbury",
    "case_name_full": "WILLIAM MARBURY v. JAMES MADISON, Secretary of State of the United States",
    "input_case_name": "Marbury v. Madison",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1803-02-24",
    "year": 1803,
    "docket": null,
    "cluster_id": 84759,
    "lead_opinion_id": 84759,
    "sibling_ids": [
      84759
    ],
    "absolute_url": "/opinion/84759/marbury-v-madison/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "5 U.S. 137",
      "volume": "5",
      "reporter": "U.S.",
      "page": "137",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2 L. Ed. 60",
        "volume": "2",
        "reporter": "L. Ed.",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cranch 137",
        "volume": "1",
        "reporter": "Cranch",
        "page": "137",
        "type": 5,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1803 U.S. LEXIS 352",
        "volume": "1803",
        "reporter": "U.S. LEXIS",
        "page": "352",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "5 U.S. 137",
        "volume": "5",
        "reporter": "U.S.",
        "page": "137",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 L. Ed. 60",
        "volume": "2",
        "reporter": "L. Ed.",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 Cranch 137",
        "volume": "1",
        "reporter": "Cranch",
        "page": "137",
        "type": 5,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1803 U.S. LEXIS 352",
        "volume": "1803",
        "reporter": "U.S. LEXIS",
        "page": "352",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "5 U.S. 137",
    "official_selection": {
      "court_class": "scotus",
      "selected": "5 U.S. 137",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-177",
      "page": null,
      "quote": "--- # Marbury v. Madison *5 U.S. (1 Cranch) 137 (1803)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In the final days of the Adams administration, William Marbury was appointed a justice of the peace, but his commission was not delivered before Jefferson took office, and the new Secretary of State, Madison, withheld it. Marbury sued directly in the Supreme Court for a writ of mandamus to compel delivery, invoking a power the Judiciary Act of 1789 purported to grant the Court. ## Issue Whether the Supreme Court could issue the writ \u2014 and, underlying that, whether a court may decline to give effect to an Act of Congress that conflicts with the Constitution. ## Rule The judiciary determines what the law is and must disregard a statute that conflicts with the Constitution.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-177a",
      "page": null,
      "quote": "an act of the legislature, repugnant to the constitution, is void.",
      "star_marker": "177",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 52598,
      "fragment": "#:~:text=an%20act%20of%20the%20legislature%2C%20repugnant%20to%20the%20constitution%2C%20is%20void.",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1803-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Marbury v. Madison",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Savage v. N.C. Dep't of Transp.",
          "cluster_id": 10658754,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Douglas Bienvenu v. 1 and 2 87184 C/W John Doe v. 1 and 2 87515",
          "cluster_id": 9541526,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of the Welfare of the Children of: L. K. and A. S., Parents",
          "cluster_id": 10707173,
          "cite": [
            "9 N.W.3d 174"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Booker",
          "cluster_id": 137739,
          "cite": [
            "160 L. Ed. 2d 621",
            "125 S. Ct. 738",
            "543 U.S. 220",
            "2005 U.S. LEXIS 628"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
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
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Taylor",
          "cluster_id": 145122,
          "cite": [
            "146 L. Ed. 2d 389",
            "120 S. Ct. 1495",
            "529 U.S. 362",
            "2000 U.S. LEXIS 2837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Younger v. Harris",
          "cluster_id": 108263,
          "cite": [
            "27 L. Ed. 2d 669",
            "91 S. Ct. 746",
            "401 U.S. 37",
            "1971 U.S. LEXIS 136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas Ass'n of Business v. Texas Air Control Board",
          "cluster_id": 1515115,
          "cite": [
            "852 S.W.2d 440",
            "1993 WL 54269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Hood",
          "cluster_id": 104272,
          "cite": [
            "327 U.S. 678",
            "66 S. Ct. 773",
            "90 L. Ed. 939",
            "1946 U.S. LEXIS 2569",
            "13 A.L.R. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Ryan",
          "cluster_id": 625711,
          "cite": [
            "182 L. Ed. 2d 272",
            "132 S. Ct. 1309",
            "566 U.S. 1",
            "2012 U.S. LEXIS 2317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seminole Tribe of Florida v. Florida",
          "cluster_id": 118011,
          "cite": [
            "134 L. Ed. 2d 252",
            "116 S. Ct. 1114",
            "517 U.S. 44",
            "1996 U.S. LEXIS 2165",
            "96 Cal. Daily Op. Serv. 2125",
            "96 Daily Journal DAR 3499",
            "64 U.S.L.W. 4167",
            "9 Fla. L. Weekly Fed. S 484",
            "34 Collier Bankr. Cas. 2d 1199",
            "42 ERC (BNA) 1289",
            "67 Empl. Prac. Dec. (CCH) 43,952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "TransUnion LLC v. Ramirez",
          "cluster_id": 4894912,
          "cite": [
            "594 U.S. 413",
            "210 L. Ed. 2d 568",
            "141 S. Ct. 2190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. Alabama",
          "cluster_id": 106997,
          "cite": [
            "13 L. Ed. 2d 759",
            "85 S. Ct. 824",
            "380 U.S. 202",
            "1965 U.S. LEXIS 1668"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. McCormack",
          "cluster_id": 107969,
          "cite": [
            "23 L. Ed. 2d 491",
            "89 S. Ct. 1944",
            "395 U.S. 486",
            "1969 U.S. LEXIS 3103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez",
          "cluster_id": 117927,
          "cite": [
            "131 L. Ed. 2d 626",
            "115 S. Ct. 1624",
            "514 U.S. 549",
            "1995 U.S. LEXIS 3039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DaimlerChrysler Corp. v. Cuno",
          "cluster_id": 145658,
          "cite": [
            "164 L. Ed. 2d 589",
            "126 S. Ct. 1854",
            "547 U.S. 332",
            "2006 U.S. LEXIS 3956"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Glucksberg",
          "cluster_id": 118144,
          "cite": [
            "138 L. Ed. 2d 772",
            "117 S. Ct. 2258",
            "521 U.S. 702",
            "1997 U.S. LEXIS 4039",
            "11 Fla. L. Weekly Fed. S 190",
            "97 Cal. Daily Op. Serv. 5008",
            "97 Daily Journal DAR 8150",
            "65 U.S.L.W. 4669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Planned Parenthood of Southeastern Pa. v. Casey",
          "cluster_id": 112786,
          "cite": [
            "120 L. Ed. 2d 674",
            "112 S. Ct. 2791",
            "505 U.S. 833",
            "1992 U.S. LEXIS 4751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clinton v. Jones",
          "cluster_id": 118115,
          "cite": [
            "137 L. Ed. 2d 945",
            "117 S. Ct. 1636",
            "520 U.S. 681",
            "1997 U.S. LEXIS 3254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Watson",
          "cluster_id": 109352,
          "cite": [
            "46 L. Ed. 2d 598",
            "96 S. Ct. 820",
            "423 U.S. 411",
            "1976 U.S. LEXIS 121"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDonald v. City of Chicago",
          "cluster_id": 149702,
          "cite": [
            "177 L. Ed. 2d 894",
            "130 S. Ct. 3020",
            "561 U.S. 742",
            "2010 U.S. LEXIS 5523",
            "22 Fla. L. Weekly Fed. S 619",
            "78 U.S.L.W. 4844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Boerne v. Flores",
          "cluster_id": 118140,
          "cite": [
            "138 L. Ed. 2d 624",
            "117 S. Ct. 2157",
            "521 U.S. 507",
            "1997 U.S. LEXIS 4035",
            "65 U.S.L.W. 4612",
            "97 Daily Journal DAR 7973",
            "1997 Colo. J. C.A.R. 1329",
            "97 Cal. Daily Op. Serv. 4904",
            "11 Fla. L. Weekly Fed. S 140",
            "70 Empl. Prac. Dec. (CCH) 44,785",
            "74 Fair Empl. Prac. Cas. (BNA) 62"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Citizens United v. Federal Election Commission",
          "cluster_id": 1741,
          "cite": [
            "175 L. Ed. 2d 753",
            "130 S. Ct. 876",
            "558 U.S. 310",
            "2010 U.S. LEXIS 766",
            "22 Fla. L. Weekly Fed. S 73",
            "78 U.S.L.W. 4078",
            "187 L.R.R.M. (BNA) 2961",
            "159 Lab. Cas. (CCH) 10,166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raines v. Byrd",
          "cluster_id": 118146,
          "cite": [
            "138 L. Ed. 2d 849",
            "117 S. Ct. 2312",
            "521 U.S. 811",
            "1997 U.S. LEXIS 4040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "IN RE INITIATIVE PETITION NO. 448, STATE QUESTION NO. 836; THE OKLAHOMA REPUBLICAN PARTY v. SETTER",
          "cluster_id": 10676729,
          "cite": [
            "2025 OK 56"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Marbury v. Madison:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(84759) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzEyMDE2MDAwMDAwJnM9OTQ4OTk5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2884759%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(84759)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE4JnM9MTE3OTE2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2884759%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(84759)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzE5NzkyMDAwMDAwJnM9OTk5OTk5MyZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%2884759%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(84759)",
    "indexed_citing_opinions": 3102,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 84759,
        "count": 3102,
        "count_source": "search"
      }
    ],
    "citation_count": 6020,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/marbury-v-madison.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0NjkzOSZzPTEwNjQ1Mjk5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2884759%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T11:42:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:46:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:42:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Marbury v. Madison

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<p id="b173-13">
<em>
   Opinion of
  </em>
</p>
<author id="Abzf">
<em>
   the court.
  </em>
</author>
<p id="b173-14">
  At the last term on the affidavits then read and filed with the clerk, a rule was granted in this case, requiring the secretary of state to shew cause why a mandamus
  <span citation-index="1" class="star-pagination" label="154"> 
   *154
   </span>
  should not issue, directing him to deliver to William Marbury his commission as a justice of the peace for the county of Washington in the district of Columbia.
 </p>
<p id="b174-5">
  No cause has been shewn, and the present motion is for a mandamus. The peculiar delicacy of this case, the novelty of some of its circumstances, and the real difficulty attending the points which occur in it, require a complete exposition of the principles, on which the opinion to be given by the court, is founded.
 </p>
<p id="b174-6">
  These principles have been, on the side of the applicant, very ably argued at the bar. In rendering the opinion of the court, there will be some departure in form, though not in substance, from the points stated in that argument.
 </p>
<p id="b174-7">
  In the order in which the court has viewed this subject, the following questions have been considered and decided.
 </p>
<p id="b174-8">
  1st. Has the applicant a right to the commission he demands ?
 </p>
<p id="b174-9">
  2dly. If he has a right, and that right has been violated, do the laws of his country afford him a remedy?
 </p>
<p id="b174-10">
  3dly. If they do afford him a remedy, is it a
  <em>
   mandamus
  </em>
  issuing from this court?
 </p>
<p id="b174-11">
  The first object of enquiry is,
 </p>
<p id="b174-12">
  1st. Has the applicant a right to the commission he demands?
 </p>
<p id="b174-13">
  His right originates in an act of congress passed in February 1801, concerning the district of Columbia.
 </p>
<p id="b174-14">
  After dividing the district into two counties, the 11th section of this law, enacts, “ that there shall be appointed in and for each of the said counties, such number of discreet persons to be justices of the peace as the president of the United States shall, from time to time, think expedient, to continue in office for five years.
 </p>
<p id="b175-2">
<span citation-index="1" class="star-pagination" label="155"> 
   *155
   </span>
  It appears, from the affidavits, that in compliance with this law, a commission for William Marbury as justice of peace for the country of Washington, was signed by John Adams, then president of the United States; after which the seal of the United States was affixed to it; but the commission has never reached the person for whom it was made out.
 </p>
<p id="b175-10">
  In order to determine whether he is entitled to this commission, it becomes necessary to enquire whether he has been appointed to the office. For if he has been appointed, the law continues him in office for five years, and he is entitled to the possession of those evidences of office, which, being completed, became his property.
 </p>
<p id="b175-11">
  The 2d section of the 2d article of the constitution, declares, that, “ the president shall nominate, and, by “ and with the advice and consent of the senate, shall “ appoint ambassadors, other public ministers and consuls, “ and all other officers of the United States, whose ap- “ pointments are not otherwise provided for.”
 </p>
<p id="b175-13">
  The third section declares, that “ he shall commission “ all the officers of the United States.”
 </p>
<p id="b175-14">
  An act of congress directs the secretary of state to keep the seal of the United States, “ to make out and record, and affix the said seal to all civil commissions to officers of the United States, to be appointed by the President, by and with the
  <em>
   consent
  </em>
  of the senate, or by the President alone; provided that the said seal shall not be affixed to any commission before the same shall have been signed by the President of the United States.”
 </p>
<p id="b175-15">
  These are the clauses of the constitution and laws of the United States, which affect this part of the case. They seem to contemplate three distinct operations:
 </p>
<p id="b175-17">
  1st, The nomination. This is the sole act of the President, and is completely voluntary.
 </p>
<p id="b175-18">
  2d. The appointment. This is also the act of the President, and is also a voluntary act, though it can only be performed by and with the advice and consent of the senate.
 </p>
<p id="b176-2">
<span citation-index="1" class="star-pagination" label="156"> 
   *156
   </span>
  3d. The commission. To grant a commission to a person appointed, might perhaps be deemed a duty enjoined by the constitution. " He shall," says that instrument, " commission all the officers of the United States."
 </p>
<p id="b176-3">
  The acts of appointing to office, and commissioning the person appointed, can scarcely be considered as one and the same; since the power to perform them is given in two separate and distinct sections of the constitution. The distinction between the appointment and the commission will be rendered more apparent, by adverting to that provision in the second section of the second article of the constitution, which authorizes congress " to vest, by law, the appointment of such inferior officers, as they think proper, in the President alone, in the courts of law, or in the heads of departments ;" thus contemplating cases where the law may direct the President to commission an officer appointed by the courts, or by the heads of departments. In such a case, to issue a commission would be apparently a duty distinct from the appointment, the performance of which, perhaps, could not legally be refused.
 </p>
<p id="b176-4">
  Although that clause of the constitution which requires the President to commission all the officers of the United States, may never have been applied to officers appointed otherwise than by himself, yet it would be difficult to deny the legislative power to apply it to such cases. Of consequence the constitutional distinction between the appointment to an office and the commission of an officer, who has been appointed, remains the same as if in practice the President had commissioned officers appointed by an authority other than his own.
 </p>
<p id="b176-5">
  It follows too, from the existence of this distinction, that, if an appointment was to be evidenced by any public act, other than the commission, the performance of such public act would create the officer; and if he was not removeable at the will of the President, would either give him a right to his commission, or enable him to perform the duties without it.
 </p>
<p id="b176-6">
  These observations are premised solely for the purpose of rendering more intelligible those which apply more directly to the particular case under consideration.
 </p>
<p id="b177-3">
<span citation-index="1" class="star-pagination" label="157"> 
   *157
   </span>
  This is an appointment made by the President, by and with the advice and consent of the senate, and is evidenced by no act but the commission itself. In such a case therefore the commission and the appointment seem inseparable; it being almost impossible to shew an appointment otherwise than by proving the existence of a commission; still the commission is not necessarily the appointment ; though conclusive evidence of it.
 </p>
<p id="b177-11">
  But at what stage does it amount to this conclusive evidence ?
 </p>
<p id="b177-12">
  The answer to this question seems an obvious one. The appointment being the sole act of the President, must be completely evidenced, when it is shewn that he has done every thing to be performed by him.
 </p>
<p id="b177-14">
  Should the commission, instead of being evidence of an appointment, even be considered as constituting the appointment itself; still it would be made when the last act to be done by the President was performed, or, at furthest, when the commission was complete.
 </p>
<p id="b177-15">
  The last act to be done by the President, is the signature of the commission. He has then acted on the advice and consent of the senate to his own nomination. The time for deliberation has then passed. He has decided. His judgment, on the advice and consent of the senate concurring with his nomination, has been made, and the officer is appointed. This appointment is evidenced by an open, unequivocal act; and being the last act required from the person making it, necessarily excludes the idea of its being, so far as respects the appointment, an inchoate and incomplete transaction.
 </p>
<p id="b177-17">
  Some point of time must be taken when the power of the executive over an officer, not removeable at his will, must cease. That point of time must be when the constitutional power of appointment has been exercised. And this power has been exercised when the last act, required from the person possessing the power, has been performed. This last act is the signature of the commission. This idea seems to have prevailed with the legislature, when the act passed, converting the department
  <span citation-index="1" class="star-pagination" label="158"> 
   *158
   </span>
  of foreign affairs into the department of state. By that act it is enacted, that the secretary of state shall keep that seal of the United States, and shall make out and re- " cord, and shall affix the said seal to all civil commissions “ to officers of the United States, to be appointed by the “ President:" "Provided that the said seal shall not be af- “ fixed to any commission, before the same shall have been “ signed by the President of the United States; nor to “ any other instrument or act, without the special war- “ rant of the President therefor.”
 </p>
<p id="b178-13">
  The signature is a warrant for affixing the great seal to the commission; and the great seal is only to be affixed to an instrument which is complete. It attests, by an act supposed to be of public notoriety, the verity of the Presidential signature.
 </p>
<p id="b178-14">
  It is never to be affixed till the commission is signed, because the signature, which gives force and effect to the commission, is conclusive evidence that the appointment is made.
 </p>
<p id="b178-15">
  The commission being signed, the subsequent duty of the secretary of state is prescribed by law, and not to be guided by the will of the President. He is to affix the seal of the United States to the commission, and is to record it.
 </p>
<p id="b178-16">
  This is not a proceeding which may be varied, if the judgment of the executive shall suggest one more eligible; but is a precise course accurately marked out by law, and is to be strictly pursued. It is the duty of the secretary of state to conform to the law, and in this he is an officer of the United States, bound to obey the laws. He acts, in this respect, as has been very properly stated at the bar, under the authority of law, and not by the instructions of the President. It is a ministerial act which the law enjoins on 3 particular officer for a particular purpose.
 </p>
<p id="b178-17">
  If it should be supposed, that the solemnity of affixing the seal, is necessary not only to the validity of the commission, but even to the completion of an appointment, still when the seal is affixed the appointment is made, and
  <span citation-index="1" class="star-pagination" label="159"> 
   *159
   </span>
  the commission is valid. No other solemnity is required by law ; no other act is to be performed on the part of government. All that the executive can do to invest the person with his office, is done; and unless the appointment be then made, the executive cannot make one without the co-operation of others.
 </p>
<p id="b179-4">
  After searching anxiously for the principles on which a contrary opinion may be supported, none have been found which appear of sufficient force to maintain the opposite doctrine.
 </p>
<p id="b179-5">
  Such as the imagination of the court could suggest, have been very deliberately examined, and after allowing them all the weight which it appears possible to give them, they do not shake the opinion which has been formed.
 </p>
<p id="b179-6">
  In considering this question, it has been conjectured that the commission may have been assimilated to a deed, to the validity of which, delivery is essential.
 </p>
<p id="b179-7">
  This idea is founded on the supposition that the commission is not merely
  <em>
   evidence
  </em>
  of an appointment, but is itself the actual appointment; a supposition by no means unquestionable. But for the purpose of examining this objection fairly, let it be conceded, that the principle, claimed for its support, is established.
 </p>
<p id="b179-8">
  The appointment being, under the constitution, to be made by the President
  <em>
   personally,
  </em>
  the delivery of the deed of appointment, if necessary to its completion, must be made by the President also. It is not necessary that the livery should be made personally to the grantee of the office : It never is so made. The law would seem to contemplate that it should be made to the secretary of state, since it directs the secretary to affix the seal to the commission
  <em>
   after
  </em>
  it shall have been signed by the President. If then the act of livery be necessary to give validity to the commission, it has been delivered when executed and given to the secretary for the purpose of being sealed, recorded, and transmitted to the party.
 </p>
<p id="b179-9">
  But in all cases of letters patent, certain solemnities are required by law, which solemnities are the evidences
  <span citation-index="1" class="star-pagination" label="160"> 
   *160
   </span>
  of the validity of the instrument. A formal delivery to the person is not among them. In cases of commissions, the sign manual of the President, and the seal of the United States, are those solemnities. This objection therefore does not touch the case.
 </p>
<p id="b180-7">
  It has also occurred as possible, and barely possible, that the transmission of the commission, and the acceptance thereof, might be deemed necessary to complete the right of the plaintiff.
 </p>
<p id="b180-8">
  The transmission of the commission, is a practice directed by convenience, but not by law. It cannot therefore be necessary to constitute the appointment which must precede it, and which is the mere act of the President. If the executive required that every person appointed to an office, should himself take means to procure his commission, the appointment would not be the less valid on that account. The appointment is the sole act of the President; the transmission of the commission is the sole act of the officer to whom that duty is assigned, and may be accelerated or retarded by circumstances which can have no influence on the appointment. A commission is transmitted to a person already appointed ; not to a person to be appointed or not, as the letter enclosing the commission should happen to get into the post-office and reach him in safety, or to miscarry.
 </p>
<p id="b180-9">
  It may have some tendency to elucidate this point, to enquire, whether the possession of the original commission be indispensably necessary to authorize a person, appointed to any office, to perform the duties of that office. If it was necessary, then a loss of the commission would lose the office. Not only negligence, but accident or fraud, fire or theft, might deprive an individual of his office. In such a case, I presume it could not be doubted, but that a copy from the record of the office of the secretary of state, would be, to every intent and purpose, equal to the original. The act of congress has expressly made it so. To give that copy validity, it would not be necessary to prove that the original had been transmitted and afterwards lost. The copy would be complete evidence that the original had existed, and that the appointment had been made, but, not that the original had been transmitted. If indeed it should appear that
  <span citation-index="1" class="star-pagination" label="161"> 
   *161
   </span>
  the original had been mislaid in the office of state, that circumstance would not affect the operation of the copy. When all the requisites have been performed which authorize a recording officer to record any instrument whatever, and the order for that purpose has been given, the instrument is, in law, considered as recorded, although the manual labour of inserting it in a book kept for that purpose may not have been performed.
 </p>
<p id="b181-9">
  In the case of commissions, the law orders the secretary of state to record them. When therefore they are signed and sealed, the order for their being recorded is given; and whether inserted in the book or not, they are in law recorded.
 </p>
<p id="b181-10">
  A copy of this record is declared equal to the original, and the fees, to be paid by a person requiring a copy, are ascertained by law. Can a keeper of a public record, erase therefrom a commission which has been recorded ? Or can he refuse a copy thereof to a person demanding it on the terms prescribed by law ?
 </p>
<p id="b181-12">
  Such a copy would, equally with the original, authorize the justice of peace to proceed in the performance of his duty, because it would, equally with the original, attest his appointment.
 </p>
<p id="b181-13">
  If the transmission of a commission be not considered as necessary to give validity to an appointment; still less is its acceptance. The appointment is the sole act of the President; the acceptance is the sole act of the officer, and is, in plain common sense, posterior to the appointment. As he may resign, so may he refuse to accept : but neither the one, nor the other, is capable of rendering the appointment a non-entity.
 </p>
<p id="b181-14">
  That this is the understanding of the government, is apparent from the whole tenor of its conduct.
 </p>
<p id="b181-15">
  A commission bears date, and the salary of the officer commences from his appointment; not from the transmission or acceptance of his commission. When a person, appointed to any office, refuses to accept that office, the successor is nominated in the place of the person who
  <span citation-index="1" class="star-pagination" label="162"> 
   *162
   </span>
  has declined to accept, and not in the place of the person who had been previously in office, and had created the original vacancy.
 </p>
<p id="b182-6">
  It is therefore decidedly the opinion of the court, that when a commission has been signed by the President, the appointment is made ; and that the commission is complete, when the seal of the United States has been affixed to it by the secretary of state.
 </p>
<p id="b182-7">
  Where an officer is removeable at the will of the executive, the circumstance which completes his appointment is of no concern; because the act is at any time revocable; and the commission may be arrested, if still in the office. But when the officer is not removeable at the will of the executive, the appointment is not revocable, and cannot be annulled. It has conferred legal rights which cannot be resumed.
 </p>
<p id="b182-8">
  The discretion of the executive is to be exercised until the appointment has been made. But having once made the appointment, his power over the office is terminated in all cases, where, by law, the officer is not removeable by him. The right to the office is
  <em>
   then
  </em>
  in the person appointed, and he has the absolute, unconditional, power of accepting or rejecting it.
 </p>
<p id="b182-9">
  Mr. Marbury, then, since his commission was signed by the President, and sealed by the secretary of state, was appointed; and as the law creating the office, gave the officer a right to hold for five years, independent of the executive, the appointment was not revocable; but vested in the officer legal rights, which are protected by the laws of his country.
 </p>
<p id="b182-10">
  To withhold his commission, therefore, is an act deemed by the court not warranted by law, but violative of a vested legal right.
 </p>
<p id="b182-11">
  This brings
  <em>
   us
  </em>
  to the second enquiry
  <em>
   ;
  </em>
  which is,
 </p>
<p id="b182-12">
  2dly. If he has a right, and that right has been violated, do the laws of his country afford him a remedy?
 </p>
<p id="b183-2">
<span citation-index="1" class="star-pagination" label="163"> 
   *163
   </span>
  The very essence of civil liberty certainly consists in the right of every individual to claim the protection of the laws, whenever he receives an injury. One of the first duties of government is to afford that protection. In Great Britain the king himself is sued in the respectful form of a petition, and he never fails to comply with the judgment of his court.
 </p>
<p id="b183-3">
  In the 3d vol. of his commentaries, p. 23, Blackstone states two cases in which a remedy is afforded by mere operation of law.
 </p>
<p id="b183-4">
  “In all other cases,” he says, “it is a general and indis-“putable rule, that where there is a legal right, there is “ also a legal remedy by suit or action at law, whenever “that right is invaded.”
 </p>
<p id="b183-5">
  And afterwards, p. 109, of the same vol. he says, “I "am next to consider such injuries as are cognizable by “the courts of the common law. And herein I shall for "the present only remark, that all possible injuries what-"soever, that did not fall within the exclusive cognizance “of either the ecclesiastical, military, or maritime tribu-"nals, are for that very reason, within the cognizance "of the common law courts of justice; for it is a settled "and invariable principle in the laws of England, that "every right, when withheld, must have a remedy, and “every injury its proper redress.”
 </p>
<p id="b183-6">
  The government of the United States has been emphatically termed a government of laws, and not of men. It will certainly cease to deserve this high appellation, if the laws furnish no remedy for the violation of a vested legal right.
 </p>
<p id="b183-8">
  If this obloquy is to be cast on the jurisprudence of our country, it must arise from the peculiar character of the case.
 </p>
<p id="b183-9">
  It behoves us then to enquire whether there be in its composition any ingredient which shall exempt it from legal investigation, or exclude the injured party from legal redress. In pursuing this enquiry the first question which presents itself, is, whether this can be arranged
  <span citation-index="1" class="star-pagination" label="164"> 
   *164
   </span>
  with that class of cases which come under the description of
  <em>
   damnum absque
  </em>
  injuria—a loss without an injury.
 </p>
<p id="Ada">
  This description of cases never has been considered, and it is believed never can be considered, as comprehending offices of trust, of honor or of profit. The office of justice of peace in the district of Columbia is such an office; it is therefore worthy of the attention and guardianship of the laws. It has received that attention and guardianship. It has been created by special act of congress, and has been secured, so far as the laws can give security to the person appointed to fill it, for five years. It is not then on account of the worthlessness of the thing pursued, that the injured party can be alleged to be without remedy.
 </p>
<p id="b184-7">
  Is it in the nature of the transaction ? Is the act of delivering or withholding a commission to be considered as a mere political act, belonging to the executive department alone, for the performance of which, entire confidence is placed by our constitution in the supreme executive; and for any misconduct respecting which, the injured individual has no remedy.
 </p>
<p id="b184-8">
  That there may be such cases is not to be questioned; but that every act of duty, to be performed in any of the great departments of government, constitutes such a case, is not to be admitted.
 </p>
<p id="b184-9">
  By the act concerning invalids, passed in June, 1794, vol. 3. p. 112, the secretary at war is ordered to place on the pension list, all persons whose names are contained in a report previously made by him to congress. If he should refuse to do so, would the wounded veteran be without remedy ? Is it to be contended that where the law in precise terms, directs the performance of an act, in which an individual is interested, the law is incapable of securing obedience to its mandate ? Is it on account of the character of the person against whom the complaint is made ? Is it to be contended that the heads of departments are not amenable to the laws of their country ?
 </p>
<p id="b184-10">
  Whatever the practice on particular occasions may be, the theory of this principle will certainly never be main
  <span citation-index="1" class="star-pagination" label="165"> 
   *165
   </span>
  tained. No act of the legislature confers so extraordinary a privilege, nor can it derive countenance from the doctrines of the common law. After stating that personal injury from the king to a subject is presumed to be impossible, Blackstone, vol. 3. p. 255, says, “but injuries “to the rights of property can scarcely be committed by “the crown without the intervention of its officers; for "whom, the law, in matters of right, entertains no re-“spect or delicacy; but furnishes various methods of de-"tecting the errors and misconduct of those agents, by "whom the king has been deceived and induced to do a “temporary injustice.”
 </p>
<p id="b185-4">
  By the act passed in 1796, authorising the sale of the lands above the mouth of Kentucky river (vol. 3d. p. 2991 the purchaser, on paying his purchase money, becomes completely entitled to the property purchased; and on producing to the secretary of state, the receipt of the treasurer upon a certificate required by the law, the president of the United States is authorised to grant him a patent. It is further enacted that all patents shall be countersigned by the secretary of state, and recorded in his office. If the secretary of state should choose to withhold this patent; or the patent being lost, should refuse a copy of it; can it be imagined that the law furnishes to the injured person no remedy?
 </p>
<p id="b185-6">
  It is not believed that any person whatever would attempt to maintain such a proposition.
 </p>
<p id="b185-7">
  It follows then that the question, whether the legality of an act of the head of a department be examinable in a court of justice or not, must always depend on the nature of that act.
 </p>
<p id="b185-8">
  If some acts be examinable, and others not, there must be some rule of law to guide the court in the exercise of its jurisdiction.
 </p>
<p id="b185-9">
  In some instances there may be difficulty in applying the rule to particular cases; but there cannot, it is believed, be much difficulty in laying down the rule.
 </p>
<p id="b185-10">
  By the constitution of the United States, the President is invested with certain important political powers, in the
  <span citation-index="1" class="star-pagination" label="166"> 
   *166
   </span>
  exercise of which he is to use his own discretion, and is accountable only to his country in his political character, and to his own conscience. To aid him in the performance of these duties, he is authorized to appoint certain officers, who act by his authority and in conformity with his orders.
 </p>
<p id="b186-7">
  In such cases, their acts are his acts; and whatever opinion may be entertained of the manner in which executive discretion may be used, still there exists, and can exist, no power to control that discretion. The subjects are political. They respect the nation, not individual rights, and being entrusted to the executive, the decision of the executive is conclusive. The application of this remark will be perceived by adverting to the act of congress for establishing the department of foreign affairs. This officer, as his duties were prescribed by that act, is to conform precisely to the will of the President. He is the mere organ by whom that will is communicated. The acts of such an officer, as an officer, can never be examinable by the courts.
 </p>
<p id="b186-8">
  But when the legislature proceeds to impose on that officer other duties; when he is directed peremptorily to perform certain acts; when the rights of individuals are dependent on the performance of those acts; he is so far the officer of the law; is amenable to the laws for his conduct; and cannot at his discretion sport away the vested rights of others.
 </p>
<p id="b186-9">
  The conclusion from this reasoning is, that where the heads of departments are the political or confidential agents of the executive, merely to execute the will of the President, or rather to act in cases in which the executive possesses a constitutional or legal discretion, nothing can be more perfectly clear than that their acts are only politically examinable. But where a specific duty is assigned by law, and individual rights depend upon the performance of that duty, it seems equally clear that the individual who considers himself injured, has a right to resort to the laws of his country for a remedy.
 </p>
<p id="b186-10">
  If this be the rule, let us enquire how it applies to the case under the consideration of the court.
 </p>
<p id="b187-2">
<span citation-index="1" class="star-pagination" label="167"> 
   *167
   </span>
  The power of nominating to the senate, and the power of appointing the person nominated, are political powers, to be exercised by the President according to his own discretion. When he has made an appointment, he has exercised his whole power, and his discretion has been completely applied to the case. If, by law, the officer be removable at the will of the President, then a new appointment may be immediately made, and the rights of the officer are terminated. But as a fact which has existed cannot be made never to have existed, the appointment cannot be annihilated; and consequently if the officer is by law not removable at the will of the President; the rights he has acquired are protected by the law, and are not resumable by the President. They cannot be extinguished by executive authority, and he has the privilege of asserting them in like manner as if they had been derived from any other source.
 </p>
<p id="b187-5">
  The question whether a right has vested or not, is, in its nature, judicial, and must be tried by the judicial authority. It, for example, Mr. Marbury had taken the oaths of a magistrate, and proceeded to act as one; in consequence of which a suit had been instituted against him, in which his defence had depended on his being a magistrate; the validity of his appointment must have been determined by judicial authority.
 </p>
<p id="b187-6">
  So, if he conceives that, by virtue of his appointment, he has a legal right, either to the commission which has been made out for him, or to a copy of that commission, it is equally a question examinable in a court, and the decision of the court upon it must depend on the opinion entertained of his appointment.
 </p>
<p id="b187-7">
  That question has been discussed, and the opinion is, that the latest point of time which can be taken as that at which the appointment was complete, and evidenced, was when, after the signature of the president, the seal of the United States was affixed to the commission.
 </p>
<p id="b187-8">
  It is then the opinion of the court,
 </p>
<p id="b187-9">
  1st. That by signing the commission of Mr. Marbury, the president of the United States appointed him a justice
  <span citation-index="1" class="star-pagination" label="168"> 
   *168
   </span>
  of peace, for the county of Washington in the district of Columbia; and that the seal of the United States, affixed thereto by the secretary of state, is conclusive testimony of the verity of the signature, and of the completion of the appointment; and that the appointment conferred on him a legal right to the office for the space of five years.
 </p>
<p id="b188-5">
  2dly. That, having this legal title to the office, he has a consequent right to the commission; a refusal to deliver which, is a plain violation of that right, for which the laws of his country afford him a remedy.
 </p>
<p id="b188-6">
  It remains to be enquired whether,
 </p>
<p id="b188-7">
  3dly. He is entitled to the remedy for which he applies. This depends on,
 </p>
<p id="b188-8">
  1st. The nature of the writ applied for, and,
 </p>
<p id="b188-9">
  2dly. The power of this court.
 </p>
<p id="b188-10">
  1st. The nature of the writ.
 </p>
<p id="b188-11">
  Blackstone, in the 3d volume of his commentaries, page 110, defines a mandamus to be, “a command is-“suing in the king’s name from the court of king’s bench, "and directed to any person, corporation, or inferior "court of judicature within the king’s dominions, re-"quiring them to do some particular thing therein speci-"fied, which appertains to their office and duty, and “which the court of king’s bench has previously deter-“mined, or at least supposes, to be consonant to right “and justice.”
 </p>
<p id="b188-12">
  Lord Mansfield, in 3d Burrows 1266, in the case of the
  <em>
   King v.
  </em>
  Baker,
  <em>
   et al.
  </em>
  states with much precision and explicitness the cases in which this writ may be used.
 </p>
<p id="b188-13">
  “ Whenever,” says that very able judge, “there is a “right to execute an office, perform a service, or exercise “ a franchise (more especially if it be in a matter of pub-“lic concern, or attended with profit) and a person is “kept out of possession, or dispossessed of such right, and
  <span citation-index="1" class="star-pagination" label="169"> 
   *169
   </span>
  "has no other specific legal remedy, this court ought "to assist by mandamus, upon reasons of justice, as the “writ expresses, and upon reasons of public policy, to "preserve peace, order and good government.” In the same case he says, “this writ ought to be used upon all “occasions where the law has established no specific “remedy, and where in justice and good government “there ought to be one.”
 </p>
<p id="b189-6">
  In addition to the authorities now particularly cited, many others were relied on at the bar, which show how far the practice has conformed to the general doctrines that have been just quoted.
 </p>
<p id="b189-7">
  This writ, if awarded, would be directed to an officer of government, and its mandate to him would be, to use the words of Blackstone, “to do a particular thing “therein specified, which appertains to his office and “duty and which the court has previously determined, “or at least supposes, to be consonant to right and jus-“tice.” Or, in the words of Lord Mansfield, the applicant, in this case, has a right to execute an office of public concern, and is kept out of possession of that right.
 </p>
<p id="b189-9">
  These circumstances certainly concur in this case.
 </p>
<p id="b189-10">
  Still, to render the mandamus a proper remedy, the officer to whom it is to be directed, must be one to whom, on legal principles, such writ may be directed; and the person applying for it must be without any other specific and legal remedy.
 </p>
<p id="b189-11">
  1st. With respect to the officer to whom it would be directed. The intimate political relation, subsisting between the president of the United States and the heads of departments, necessarily renders any legal investigation of the acts of one of those high officers peculiarly irksome, as well as delicate; and excites some hesitation with respect to the propriety of entering into such investigation. Impressions are often received without much reflection or examination, and it is not wonderful that in such a case, as this, the assertion, by an individual, of his legal claims, in a court of justice; to which claims it is the duty of that court to attend; should at first view be considered
  <span citation-index="1" class="star-pagination" label="170"> 
   *170
   </span>
  by some, as an attempt to intrude into the cabinet, and to intermeddle with the prerogatives of the executive.
 </p>
<p id="A0I">
  It is scarcely necessary for the court to disclaim all pretensions to such a jurisdiction. An extravagance, so absurd and excessive, could not have been entertained for a moment. The province of the court is, solely, to decide on the rights of individuals, not to enquire how the executive, or executive officers, perform duties in which they have a discretion. Questions, in their nature political, or which are, by the constitution and laws, submitted to the executive, can never be made in this court.
 </p>
<p id="AC">
  But, if this be not such a question; if so far from being an intrusion into the secrets of the cabinet, it respects a paper, which, according to law, is upon record, and to a copy of which the law gives a right, on the payment of ten cents; if it be no intermeddling with a subject, over which the executive can be considered as having exercised any control; what is there in the exalted station of the officer, which shall bar a citizen from asserting, in a court of justice, his legal rights, or shall forbid a court to listen to the claim
  <em>
   ;
  </em>
  or to issue a mandamus, directing the performance of a duty, not depending on executive discretion, but on particular acts of congress and the general principles of law?
 </p>
<p id="b190-9">
  If one of the heads of departments commits any illegal act, under color of his office, by which an individual sustains an injury, it cannot be pretended that his office alone exempts him from being sued in the ordinary mode of proceeding, and being compelled to obey the judgment of the law. How then can his office exempt him from this particular mode of deciding on the legality of his conduct, if the case be such a case as would, were any other individual the party complained of, authorize the process?
 </p>
<p id="b190-10">
  It is not by the office of the person to whom the writ is directed, but the nature of the thing to be done that the propriety or impropriety of issuing a mandamus, is to be determined. Where the head of a department acts in a case, in which executive discretion is to be exercised; in which he is the mere organ of executive will; it is
  <span citation-index="1" class="star-pagination" label="171"> 
   *171
   </span>
  again repeated, that any application to a court to control, in any respect, his conduct, would be rejected without hesitation.
 </p>
<p id="b191-4">
  But where he is directed by law to do a certain act affecting the absolute rights of individuals, in the performance of which he is not placed under the particular direction of the President, and the performance of which, the President cannot lawfully forbid, and therefore is never presumed to have forbidden; as for example, to record a commission, or a patent for land, which has received all the legal solemnities; or to give a copy of such record; in such cases, it is not perceived on what ground the courts of the country are further excused from the duty of giving judgment, that right be done to an injured individual, than if the same services were to be performed by a person not the head of a department.
 </p>
<p id="b191-5">
  This opinion seems not now, for the first time, to be taken up in this country.
 </p>
<p id="b191-6">
  It must be well recollected that in 1792, an act passed, directing the secretary at war to place on the pension list such disabled officers and soldiers as should be reported to him, by the circuit courts, which act, so far as the duty was imposed on the courts, was deemed unconstitutional; but some of the judges, thinking that the law might be executed by them in the character of commissioners, proceeded to act and to report in that character.
 </p>
<p id="b191-7">
  This law being deemed unconstitutional at the circuits, was repealed, and a different system was established; but the question whether those persons, who had been reported by the judges, as commissioners, were entitled, in consequence of that report, to be placed on the pension list, was a legal question, properly determinable in the courts, although the act of placing such persons on the list was to be performed by the head of a department.
 </p>
<p id="b191-8">
  That this question might be properly settled, congress passed an act in February, 1793, making it the duty of the secretary of war, in conjunction with the attorney general, to take such measures, as might be necessary to obtain an adjudication of the supreme court of the United
  <span citation-index="1" class="star-pagination" label="172"> 
   *172
   </span>
  States on the validity of any such rights, claimed under the act aforesaid.
 </p>
<p id="AYPn">
  After the passage of this act, a mandamus was moved for, to be directed to the secretary at war, commanding him to place on the pension list, a person stating himself to be on the report of the judges.
 </p>
<p id="b192-7">
  There is, therefore, much reason to believe, that this mode of trying the legal right of the complainant, was deemed by the head of a department, and by the highest law officer of the United States, the most proper which could be selected for the purpose.
 </p>
<p id="b192-8">
  When the subject was brought before the court the decision was, not that a mandamus would not lie to the head of a department, directing him to perform an act, enjoined by law, in the performance of which an individual had a vested interest; but that a mandamus ought not to issue in that case—the decision necessarily to be made if the report of the commissioners did not confer on the applicant a legal right.
 </p>
<p id="b192-16">
  The judgment in that case, is understood to have decided the merits of all claims of that description; and the persons on the report of the commissioners found it necessary to pursue the mode prescribed by the law subsequent to that which had been deemed unconditional, in order to place themselves on the pension list.
 </p>
<p id="b192-17">
  The doctrine, therefore, now advanced, is by no means a novel one.
 </p>
<p id="b192-18">
  It is true that the mandamus, now moved for, is not for the performance of an act expressly enjoined by statute.
 </p>
<p id="b192-19">
  It is to deliver a commission; on which subject the acts of Congress are silent. This difference is not considered as affecting the case. It has already been stated that the applicant has, to that commission, a vested legal right, of which the executive cannot deprive him. He has been appointed to an office, from which he is not removable at the will of the executive; and being so
  <span citation-index="1" class="star-pagination" label="173"> 
   *173
   </span>
  appointed, he has a right to the commission which the secretary has received from the president for his use. The act of congress does not indeed order the secretary of state to send it to him, but it is placed in his hands for the person entitled to it; and cannot be more lawfully withheld by him, than by any other person.
 </p>
<p id="b193-5">
  It was at first doubted whether the action of
  <em>
   detinue
  </em>
  was not a specific legal remedy for the commission which has been withheld from Mr. Marbury; in which case a mandamus would be improper. But this doubt has yielded to the consideration that the judgment in
  <em>
   detinue
  </em>
  is for the thing itself,
  <em>
   or
  </em>
  its value. The value of a public office not to be sold, is incapable of being ascertained; and the applicant has a right to the office itself, or to nothing. He will obtain the office by obtaining the commission, or a copy of it from the record.
 </p>
<p id="b193-6">
  This, then, is a plain case for a mandamus, either to deliver the commission, or a copy of it from the record ; and it only remains to be enquired,
 </p>
<p id="b193-7">
  Whether it can issue from this court.
 </p>
<p id="b193-8">
  The act to establish the judicial courts of the United States authorizes the supreme court “to issue writs of “mandamus, in cases warranted by the principles and “usages of law, to any courts appointed, or persons hold-"ing office, under the authority of the United States.”
 </p>
<p id="b193-10">
  The secretary of state, being a person holding an office under the authority of the United States, is precisely within the letter of the description; and if this court is not authorized to issue a writ of mandamus to such an officer, it must be because the law is unconstitutional, and therefore absolutely incapable of conferring the authority, and assigning the duties which its words purport to confer and assign.
 </p>
<p id="b193-11">
  The constitution vests the whole judicial power of the United States in one supreme court, and such inferior courts as congress shall, from time to time, ordain and establish. This power is expressly extended to all cases arising under the laws of the United States; and consequently, in some form, may be exercised over the present
  <span citation-index="1" class="star-pagination" label="174"> 
   *174
   </span>
  case; because the right claimed is given by a law of the United States.
 </p>
<p id="AA-t">
  In the distribution of this power it is declared that “the “supreme court shall have original jurisdiction in all “cases affecting ambassadors, other public ministers and “consuls, and those in which a state shall be a party. “In all other cases, the supreme court shall have appellate “jurisdiction.”
 </p>
<p id="b194-5">
  It has been insisted, at the bar, that as the original grant of jurisdiction, to the supreme and inferior courts, is general, and the clause, assigning original jurisdiction, to the supreme court, contains no negative or restrictive words; the power remains to the legislature, to assign original jurisdiction to that court in other cases than those specified in the article which has been recited; provided those cases belong to the judicial power of the United States.
 </p>
<p id="b194-6">
  If it had been intended to leave it in the discretion of the legislature to apportion the judicial power between the supreme and inferior courts according to the will of that body, it would certainly have been useless to have proceeded further than to have defined the judicial power, and the tribunals in which it should be vested. The subsequent part of the section is mere surplussage, is entirely without meaning, if such is to be the construction. If congress remains at liberty to give this court appellate jurisdiction, where the constitution has declared their jurisdiction shall be original; and original jurisdiction where the constitution has declared it shall be appellate; the distribution of jurisdiction, made in the constitution, is form without substance.
 </p>
<p id="b194-7">
  Affirmative words are often, in their operation, negative of other objects than those affirmed; and in this case, a negative or exclusive sense must be given to them or they have no operation at all.
 </p>
<p id="b194-8">
  It cannot be presumed that any clause in the constitution is intended to be without effect; and therefore such a construction is inadmissible, unless the words require it.
 </p>
<p id="b195-2">
<span citation-index="1" class="star-pagination" label="175"> 
   *175
   </span>
  If the solicitude of the convention, respecting our peace with foreign powers, induced a provision that the supreme court should take original jurisdiction in cases which might be supposed to affect them; yet the clause would have proceeded no further than to provide for such cases, if no further restriction on the powers of congress had been intended. That they should have appellate jurisdiction in all other cases, with such exceptions as congress might make, is no restriction; unless the words be deemed exclusive of original jurisdiction.
 </p>
<p id="b195-3">
  When an instrument organizing fundamentally a judicial system, divides it into one supreme, and so many inferior courts as the legislature may ordain and establish; then enumerates its powers, and proceeds so far to distribute them, as to define the jurisdiction of the supreme court by declaring the cases in which it shall take original jurisdiction, and that in others it shall take appellate jurisdiction; the plain import of the words seems to be, that in one class of cases its jurisdiction is original, and not appellate; in the other it is appellate, and not original. If any other construction would render the clause inoperative, that is an additional reason for rejecting such other construction, and for adhering to their obvious meaning.
 </p>
<p id="b195-4">
  To enable this court then to issue a mandamus, it must be shewn to be an exercise of appellate jurisdiction, or to be necessary to enable them to exercise appellate jurisdiction.
 </p>
<p id="b195-5">
  It has been stated at the bar that the appellate jurisdiction may be exercised in a variety of forms, and that if it be the will of the legislature that a mandamus should be used for that purpose, that will must be obeyed. This is true, yet the jurisdiction must be appellate, not original.
 </p>
<p id="b195-7">
  It is the essential criterion of appellate jurisdiction, that it revises and corrects the proceedings in a cause already instituted, and does not create that cause. Although, therefore, a mandamus may be directed to courts, yet to issue such a writ to an officer for the delivery of a paper, is in effect the same as to sustain an original action
  <em>
   for
  </em>
  that paper, and therefore seems not
  <em>
   to
  </em>
  belong to
  <span citation-index="1" class="star-pagination" label="176"> 
   *176
   </span>
  appellate, but to original jurisdiction. Neither is it necessary in such a case as this, to enable the court to exercise its appellate jurisdiction.
 </p>
<p id="b196-5">
  The authority, therefore, given to the supreme court, by the act establishing the judicial courts of the United States, to issue writs of mandamus to public officers, appears not to be warranted by the constitution; and it becomes necessary to enquire whether a jurisdiction, so conferred, can be exercised.
 </p>
<p id="b196-6">
  The question, whether an act, repugnant to the constitution, can become the law of the land, is a question deeply interesting to the United States; but, happily, not of an intricacy proportioned to its interest. It seems only necessary to recognise certain principles, supposed to have been long and well established, to decide it.
 </p>
<p id="b196-7">
  That the people have an original right to establish, for their future government, such principles as, in their opinion, shall most conduce to their own happiness, is the basis, on which the whole American fabric has been erected. The exercise of this original right is a very great exertion; nor can it, nor ought it to be, frequently repeated. The principles, therefore, so established, are deemed fundamental. And as the authority, from which they proceed, is supreme, and can seldom act, they are designed to be permanent.
 </p>
<p id="b196-8">
  This original and supreme will organizes the government, and assigns,to different departments, their respective powers. It may either stop here; or establish certain limits not to be transcended by those departments.
 </p>
<p id="b196-9">
  The government of the United States is of the latter description. The powers of the legislature are defined, and limited; and that those limits may not be mistaken, or forgotten, the constitution is written. To what purpose are powers limited, and to what purpose is that limitation committed to writing, if these limits may, at any time, be passed by those intended to be restrained? The distinction, between a government with limited and unlimited powers, is abolished, if those limits do not confine the persons on whom they are imposed, and if acts pro
  <span citation-index="1" class="star-pagination" label="177"> 
   *177
   </span>
  hibited and acts allowed, are of equal obligation. It is a proposition too plain to be contested, that the constitution controls any legislative act repugnant to it; or, that the legislature may alter the constitution by an ordinary act.
 </p>
<p id="b197-3">
  Between these alternatives there is no middle ground. The constitution is either a superior, paramount law, unchangeable by ordinary means, or it is on a level with ordinary legislative acts, and like other acts, is alterable when the legislature shall please to alter it.
 </p>
<p id="b197-5">
  If the former part of the alternative be true, then a legislative act contrary to the constitution is not law: if the latter part be true, then written constitutions are absurd attempts, on the part of the people, to limit a power, in its own nature illimitable.
 </p>
<p id="b197-6">
  Certainly all those who have framed written constitutions contemplate them as forming the fundamental and paramount law of the nation, and consequently the theory of every such government must be, that an act of the legislature, repugnant to the constitution, is void.
 </p>
<p id="b197-7">
  This theory is essentially attached to a written constitution, and is consequently to be considered, by this court, as one of the fundamental principles of our society. It is not therefore to be lost fight of in the further consideration of this subject.
 </p>
<p id="b197-8">
  If an act of the legislature, repugnant to the constitution, is void, does it, notwithstanding its invalidity, bind the courts, and oblige them to give it effect? Or, in other words, though it be not law, does it constitute a rule as operative as if it was a law ? This would be to overthrow in fact what was established in theory; and would seem, at first view, an absurdity too gross to be insisted on. It shall, however, receive a more attentive consideration.
 </p>
<p id="b197-9">
  It is emphatically the province and duty of the judicial department to say what the law is. Those who apply the use to particular cases, must of necessity expound and interpret that rule. If two laws conflict with each other, the courts must decide on the operation of each.
 </p>
<p id="AIn">
<span citation-index="1" class="star-pagination" label="178"> 
   *178
   </span>
  So if a law be in opposition to the constitution; if both the law and the constitution apply to a particular case, so that the court must either decide that case conformably to the law, disregarding the constitution; or conformably to the constitution, disregarding the law; the court must determime which of these conflicting rules governs the case. This is of the very essence of judicial duty.
 </p>
<p id="b198-6">
  If then the courts are to regard the constitution; and the constitution is superior to any ordinary act of the legislature; the constitution, and not such ordinary act, must govern the case to which they both apply.
 </p>
<p id="b198-7">
  Those then who controvert the principle that the constitution is to be considered, in court, as a paramount law, are reduced to the necessity of maintaining that courts must close their eyes on the constitution, and see only the law.
 </p>
<p id="b198-8">
  This doctrine would subvert the very foundation of all written constitutions. It would declare that an act, which, according to the principles and theory of our government, is entirely void; is yet, in practice, completely obligatory, It would declare, that if the legislature shall do what is expressly forbiden, such act, notwithstanding the express prohibition, is in reality effectual. It would be giving to the legislature a practical and real omnipotence, with the same breath which professes to restrict their powers within narrow limits. It is prescribing limits, and declaring that those limits may be passed at pleasure.
 </p>
<p id="b198-9">
  That it thus reduces to nothing what we have deemed the greatest improvement on political institutions—a written constitution—would of itself be sufficient, in America, where written constitutions have been viewed with so much reverence, for rejecting the construction. But the peculiar expressions of the constitution of the United States furnish additional arguments in favour of its rejection.
 </p>
<p id="b198-10">
  The judicial power of the United States is extended to all cases arising under the constitution.
 </p>
<p id="b199-3">
<span citation-index="1" class="star-pagination" label="179"> 
   *179
   </span>
  Could it be the intention of those who gave this power, to say that, in using it, the constitution should not be looked into? That a case arising under the constitution should be decided without examining the instrument under which it arises?
 </p>
<p id="b199-4">
  This is too extravagant to be maintained.
 </p>
<p id="b199-5">
  In some cases then, the constitution must be looked into by the judges. And if they can open it at all, what part of it are they forbidden to read, or to obey?
 </p>
<p id="b199-6">
  There are many other parts of the constitution which serve to illustrate this subject.
 </p>
<p id="b199-7">
  It is declared that “ no tax or duty shall be laid on arti-“cles exported from any state.” Suppose a duty on the export of cotton, of tobacco, or of flour; and a suit instituted to recover it. Ought judgment to be rendered in such a case? ought the judges to close their eyes on the constitution, and only see the law.
 </p>
<p id="b199-8">
  The constitution declares that “no bill of attainder or "ex
  <em>
   post facto
  </em>
  law shall be passed.”
 </p>
<p id="b199-9">
  If, however, such a bill should be passed and a person should be prosecuted under it; must the court condemn to death those victims whom the constitution endeavours to preserve?
 </p>
<p id="b199-10">
  “No person,” says the constitution, “shall be convicted “of treason unless on the testimony of two witnesses to the same overt act, or on confession in open court.”
 </p>
<p id="b199-12">
  Here the language of the constitution is addressed especially to the courts. It prescribes, directly for them, a rule of evidence not to be departed from. If the legislature should change that rule, and declare
  <em>
   one
  </em>
  witness, or a confession
  <em>
   out
  </em>
  of court, sufficient for conviction, must the constitutional principles yield to the legislative act?
 </p>
<p id="b199-13">
  From these, and many other selections which might be made, it is apparent, that the framers of the consti
  <span citation-index="1" class="star-pagination" label="180"> 
   *180
   </span>
  tution contemplated that instrument, as a rule for the government of courts, as well as of the legislature.
 </p>
<p id="AY9">
  Why otherwise does it direct the judges to take an oath to support it ? This oath certainly applies, in an especial manner, to their conduct in their official character. How immoral to impose it on them, if they were to be used as the instruments, and the knowing instruments, for violating what they swear to support!
 </p>
<p id="b200-6">
  The oath of office, too, imposed by the legislature, is completely demonstrative of the legislative opinion on this subject. It is in these words, “I do solemnly “swear that I will administer justice without respect “to persons, and do equal right to the poor and to the “rich; and that I will faithfully and impartially discharge “all the duties incumbent on me as accord-“ing to the best of my abilities and understanding, agree-“ably to
  <em>
   the constitution,
  </em>
  and laws of the United States.”
 </p>
<p id="b200-8">
  Why does a judge swear to discharge his duties agreably to the constitution of the United States, if that constitution forms no rule for his government? if it is closed upon him, and cannot be inspected by him?
 </p>
<p id="b200-9">
  If such be the real state of things, this is worse than solemn mockery. To prescribe, or to take this oath, becomes equally a crime.
 </p>
<p id="b200-10">
  It is also not entirely unworthy of observation, that in declaring what shall be the
  <em>
   supreme
  </em>
  law of the land, the
  <em>
   constitution
  </em>
  itself is first mentioned; and not the laws of the United States generally, but those only which shall be made in
  <em>
   pursuance
  </em>
  of the constitution, have that rank.
 </p>
<p id="b200-11">
  Thus, the particular phraseology of the constitution of the United States confirms and strengthens the principle, supposed to be essential to all written constitutions, that a law repugnant to the constitution is void; and that
  <em>
   courts,
  </em>
  as well as other departments, are bound by that instrument.
 </p>
<p id="b200-12">
  The rule must be discharged.
 </p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Marcus v. Search Warrant.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Marcus v. Search Warrant
type: case
citation: "367 U.S. 717 (1961)"
parallel_cite: "81 S. Ct. 1708; 6 L. Ed. 2d 1127"
neutral_cite: 1961 U.S. LEXIS 813
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-06-19
docket: No. 225
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
  opinion_url: "https://www.courtlistener.com/opinion/106287/marcus-v-search-warrant-of-property/"
  cluster_id: 106287
  opinion_id: null
  identity_checked: true
lake:
  record_id: Marcus v. Search Warrant
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Anchor
related:
  - "[[The Warrant Requirement]]"
  - "[[A Quantity of Copies of Books v. Kansas]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - particularity
  - general-warrant
  - obscenity
  - first-amendment
holding: "Warrants to seize allegedly obscene publications that issue on a police officer's conclusory complaint, without any judicial scrutiny of the materials or a prior adversary hearing, and that leave the selection of what to seize to the executing officers' discretion, operate as general warrants and lack the safeguards the Constitution demands."
aliases:
  - Marcus v. Search Warrant
  - "Marcus v. Search Warrant of Property (1961)"
  - Marcus v. Search Warrant of Property at 104 East Tenth Street
---

# Marcus v. Search Warrant

*367 U.S. 717 (1961)* (No. 225) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 106287 → combined opinion 106287 (Brennan, J.; 367 U.S. 717, decided June 19, 1961). Full case name: Marcus v. Search Warrant of Property at 104 East Tenth Street, Kansas City, Missouri. Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*732`). S9 promotes. -->

## Background
On the strength of a single police officer's conclusory complaints that certain magazines were obscene, Missouri judges issued warrants authorizing their seizure. Officers then searched newsstands and a distributor and seized roughly 11,000 copies of some 280 publications, deciding item by item, on their own judgment, what to take. No judge examined the materials before issuing the warrants, and no adversary hearing on obscenity preceded the seizure. The publisher and distributors challenged the seizures.

## Issue
Whether Missouri's procedures for seizing allegedly obscene publications — warrants issued on a conclusory complaint, without judicial review of the materials or a prior adversary determination of obscenity, and leaving the choice of what to seize to the officers — satisfied the constitutional requirements governing searches and seizures.

## Rule
The Court held the warrants were, in effect, general warrants that delegated the seizure decision to the executing officers: "The warrants gave the broadest discretion to the executing officers; they merely repeated the language of the statute and the complaints, specified no publications, and left to the individual judgment of each of the many police officers involved the selection of such magazines as in his view constituted 'obscene . . . publications.'" — 367 U.S. at 732. ^pin-732

## Application
Because the warrants named no particular items and no judge had scrutinized the materials, each officer made ad hoc, on-the-spot decisions about what was obscene — the standardless discretion the [[Particularity|particularity]] requirement exists to prevent. That defect was especially grave where the seizures swept in presumptively protected expression, without any prior adversary hearing to separate protected from unprotected material. The procedures therefore lacked the safeguards due process demands to keep nonobscene material from being suppressed.

## Conclusion
The judgment was **reversed**. Brennan, J., delivered the opinion of the Court; Black, J. (joined by Douglas, J.), concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Marcus* is a **warrant-requirement anchor**: it enforces the [[Particularity|particularity]] command by condemning warrants that leave the choice of what to seize to the officer's discretion — the modern echo of the general-warrant abuses that produced the Fourth Amendment. Its First Amendment overlay — heightened procedural safeguards when the thing seized is expression — was developed in *[[A Quantity of Copies of Books v. Kansas]]* (1964) and *[[Roaden v. Kentucky]]* (1973). Teach it for the core lesson that a warrant must particularly describe what may be seized.

## Appears on
- [[Particularity]] — *Anchor*

## Sources
- [*Marcus v. Search Warrant of Property at 104 East Tenth Street, Kansas City, Missouri*, 367 U.S. 717 (1961)](https://www.courtlistener.com/opinion/106287/marcus-v-search-warrant/) — pinpoint: 732 (Brennan, J., for the Court; the CL opinion text carries the reporter star `*732` immediately before the quoted sentence). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2c7522c7877169e0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Marcus v. Search Warrant"}, "payload": {"all": [{"cite": "367 U.S. 717", "page": "717", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "367"}, {"cite": "81 S. Ct. 1708", "page": "1708", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "6 L. Ed. 2d 1127", "page": "1127", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "6"}, {"cite": "1961 U.S. LEXIS 813", "page": "813", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}], "display": "367 U.S. 717", "official": {"cite": "367 U.S. 717", "page": "717", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "367"}, "official_selection_present": true, "record_id": "Marcus v. Search Warrant"}}
{"assertion_id": "d9f3e68fefc92e4f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Marcus v. Search Warrant"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Marcus v. Search Warrant", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Marcus v. Search Warrant

```json
{
  "schema_version": "s2.v1",
  "record_id": "Marcus v. Search Warrant",
  "status": "under_review",
  "identity": {
    "case_name": "Marcus v. Search Warrant of Property",
    "case_name_short": "Marcus",
    "case_name_full": "MARCUS Et Al. v. SEARCH WARRANT OF PROPERTY AT 104 EAST TENTH STREET, KANSAS CITY, MISSOURI, Et Al.",
    "input_case_name": "Marcus v. Search Warrant",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-06-19",
    "year": 1961,
    "docket": "No. 225",
    "cluster_id": 106287,
    "lead_opinion_id": 9422285,
    "sibling_ids": [],
    "absolute_url": "/opinion/106287/marcus-v-search-warrant-of-property/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "367 U.S. 717",
      "volume": "367",
      "reporter": "U.S.",
      "page": "717",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 1708",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1127",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 813",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "813",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "367 U.S. 717",
        "volume": "367",
        "reporter": "U.S.",
        "page": "717",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 1708",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1127",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 813",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "813",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "367 U.S. 717",
    "official_selection": {
      "court_class": "scotus",
      "selected": "367 U.S. 717",
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
    "date_created": "2026-07-06T13:43:51Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "marcus-v-search-warrant--106287",
      "to_record_id": "Marcus v. Search Warrant",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Marcus v. Search Warrant

```
<opinion type="majority">
<author id="b754-10">Mr. Justice Brennan</author>
<p id="AU7">delivered the opinion of the Court.</p>
<p id="b754-11">This appeal presents the question whether due process under the Fourteenth Amendment was denied the appellants by the application in this case of Missouri’s procedures authorizing the search for and seizure of allegedly obscene publications preliminarily to their destruction by burning or otherwise if found by a court to be obscene. The procedures are statutory, but are supplemented by a rule of the Missouri Supreme Court.<footnotemark>1</footnotemark> The warrant for search for and seizure of obscene material issues on a sworn complaint filed with a judge or magis<page-number citation-index="1" label="719">*719</page-number>trate.<footnotemark>2</footnotemark> If the complainant states “positively and not upon information or belief,” or states “evidential facts from which such judge or magistrate determines the existence of probable cause” to believe that obscene material “is being held or kept in any place or in any building,” “such judge or magistrate shall issue a search warrant directed to any peace officer commanding him to search the place therein described and to seize and bring before such judge or magistrate the personal property therein described.” <footnotemark>3</footnotemark> The owner of the property is not afforded a <page-number citation-index="1" label="720">*720</page-number>hearing before the warrant issues; the proceeding is <em>ex parte. </em>However, the judge or magistrate issuing the warrant must fix a date, not less than five nor more than 20 days after the seizure, for a hearing to determine whether the seized material is obscene.<footnotemark>4</footnotemark> The owner of the material may appear at such hearing and defend <page-number citation-index="1" label="721">*721</page-number>against the charge.<footnotemark>5</footnotemark> No time limit' is provided within which the judge must announce his decision. If the judge finds that the material is obscene, he is required to order it to be publicly destroyed, by burning or otherwise; if he finds that it is not obscene, he shall order its return to its owner.<footnotemark>6</footnotemark></p>
<p id="b757-5">The Missouri Supreme Court sustained the validity of the procedures as applied in this case. <span class="citation" data-id="5024262"><a href="/opinion/5201171/search-warrant-of-property-at-5-west-12th-street-kansas-city-v-marcus/" aria-description="Citation for case: Search Warrant of Property at 5 West 12th Street, Kansas...">334 S. W. 2d 119</a></span>. The appellants brought this appeal here under <span class="citation no-link">28 U. S. C. § 1257</span> (2). We postponed consideration of the question of our jurisdiction to the hearing of the case on the merits. <span class="citation multiple-matches"><a href="/c/U.%20S./364/811/">364 U. S. 811</a></span>. We hold that the appeal is properly here, see <em>Dahnke-Walker Milling Co. </em>v. <em>Bondurant, </em><span class="citation" data-id="9418469"><a href="/opinion/99884/dahnke-walker-milling-co-v-bondurant/" aria-description="Citation for case: Dahnke-Walker Milling Co. v. Bondurant">257 U. S. 282</a></span>, and turn to the merits.</p>
<p id="b757-6">Appellant, Kansas City News Distributors, managed by appellant, Homer Smay, is a wholesale distributor of magazines, newspapers and books in the Kansas City area. The other appellants operate five retail newsstands <page-number citation-index="1" label="722">*722</page-number>in Kansas City. In October 1957, Police Lieutenant Coughlin of the Kansas City Police Department Vice Squad was conducting an investigation into the distribution of allegedly obscene magazines. On October 8, 1957, he visited Distributors’ place of business and showed Smay a list of magazines. Smay admitted that his company distributed all but one of the magazines on the list. The following day, October 9, Lieutenant Coughlin visited the five newsstands and purchased one magazine at each.<footnotemark>7</footnotemark> On October 10 the officer signed and filed six sworn complaints in the Circuit Court of Jackson County, stating in each complaint that “of his own knowledge” the appellant named therein, at its stated place of business, “kept for the purpose of [sale] . . . obscene . . . publications . . . .” No copy of any magazine on Lieutenant Coughlin’s list, or purchased by him at the newsstands, was filed with the complaint or shown to the circuit judge. The circuit judge issued six search warrants authorizing, as to the premises of the appellant named in each, “any peace officer in the State of Missouri . . . [to] search the said premises . . . within 10 days after the issuance of this warrant by day or night, and . . . seize . . . [obscene materials] and take same into your possession . . . .”</p>
<p id="b758-6">All of the warrants were executed on October 10, but by different law enforcement officers. Lieutenant Coughlin with two other Kansas City police officers, and an officer of the Jackson County Sheriff’s Patrol, executed the warrant against Distributors. Distributors’ stock of magazines runs “into hundreds of thousands . . . [p]robably closer to a million copies.” The officers examined the publications in the stock on the main floor of the establishment, <page-number citation-index="1" label="723">*723</page-number>not confining themselves to Lieutenant Coughlin’s original list. They seized all magazines which “[i]n our judgment” were obscene; when an officer thought “a magazine . . . ought to be picked up” he seized all copies of it. After three hours the examination was completed and the magazines seized were “hauled away in a truck and put on the 15th floor of the courthouse.” A substantially similar procedure was followed at each of the five newsstands. Approximately 11,000 copies of 280 publications, principally magazines but also some books and photographs, were seized at the six places.<footnotemark>8</footnotemark></p>
<p id="b759-5">The circuit judge fixed October 17 for the hearing, which was later continued to October 23. Timely motions were made by the appellants to quash the search warrants and to suppress as evidence the property seized, and for the immediate return of the property. The motions were rested on a number of grounds but we are concerned only with the challenge to the application of the procedures in the context of the protections for free speech and press assured against state abridgment by the Fourteenth Amendment.<footnotemark>9</footnotemark> Unconstitutionality in violation of the Fourteenth Amendment was asserted because the procedures as applied (1) allowed a seizure by police officers “without notice or any hearing afforded to the movants prior to seizure for the purpose of determining whether or not these . . . publications are ob<page-number citation-index="1" label="724">*724</page-number>scene . . .,” and (2) because they “allowed police officers and deputy sheriffs to decide and make a judicial determination after the warrant was issued as to which . . . magazines were . . . obscene . . . and were subject to seizure, impairing movants’ freedom of speech and publication.” The circuit judge reserved rulings on the motions and heard testimony of the police officers concerning the events surrounding the issuance and execution of the several warrants. On December 12, 1957, the circuit judge filed an unreported opinion in which he overruled the several motions and found that 100 of the 280 seized items were obscene. A judgment thereupon issued directing that the 100 items, and all copies thereof, “shall be retained by the Sheriff of Jackson County ... as necessary evidence for the purpose of possible criminal prosecution or prosecutions, and, when such necessity no longer exists, said Sheriff . . . shall publicly destroy the same by burning within thirty days thereafter”; it ordered further that the 180 items not found to be obscene, and all copies thereof, “shall be returned forthwith by the Sheriff ... to the rightful owner or owners . . . .”</p>
<p id="b760-4">I.</p>
<p id="b760-5">The use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new. Historically the struggle for freedom of speech and press in England was bound up with the issue of the scope of the search and seizure power. See generally Siebert, Freedom of the Press in England, 1476-1776; Hanson, Government and the Press, 1695-1763. It was a principal instrument for the enforcement of the Tudor licensing system. The Stationers’ Company was incorporated in 1557 to help implement that system and was empowered “to make search whenever it shall please them in any place, shop, <page-number citation-index="1" label="725">*725</page-number>house, chamber, or building or any printer, binder or bookseller whatever within our kingdom of England or the dominions of the same of or for any books or things printed, or to be printed, and to seize, take hold, burn, or turn to the proper use of the foresaid community, all and several those books and things which are or shall be printed contrary to the form of any statute, act, or proclamation, made or to be made <em>. . . </em><footnotemark>10</footnotemark></p>
<p id="b761-5">An order of council confirmed and expanded the Company’s power in 1566,<footnotemark>11</footnotemark> and the Star Chamber reaffirmed it in 1586 by a decree “That it shall be lawful for the wardens of the said Company for the time being or any two of the said Company thereto deputed by the said wardens, to make search in all workhouses, shops, warehouses of printers, booksellers, bookbinders, or where they shall have reasonable cause of suspicion, and all books [etc.] . . . contrary to . . . these present ordinances to stay and take to her Majesty’s use . . . .”<footnotemark>12</footnotemark> Books thus seized were taken to Stationers’ Hall where they were inspected by ecclesiastical officers, who decided whether they should be burnt. These powers were exercised under the Tudor censorship to suppress both Catholic and Puritan dissenting literature.<footnotemark>13</footnotemark></p>
<p id="b761-6">Each succeeding regime during turbulent Seventeenth Century England used the search and seizure power to suppress publications. James I commissioned the ecclesiastical judges comprising the Court of High Commission “to enquire and search for ... all heretical, schismatical and seditious books, libels, and writings, <em>and all other books, pamphlets and portraitures offensive to the state or set forth without sufficient and lawful authority in that </em><page-number citation-index="1" label="726">*726</page-number><em>behalf, </em>. . . and the same books [etc.] and their printing-presses themselves likewise to seize <em>and so to order and dispose of them ... as they may not after serve or be employed for any such unlawful use .. ..” </em><footnotemark>14</footnotemark> The Star Chamber decree of 1637, re-enacting the requirement that all books be licensed, continued the broad powers of the Stationers' Company to enforce the licensing laws.<footnotemark>15</footnotemark> During the political overturn of the 1640’s Parliament on several occasions asserted the necessity of a broad search and seizure power to control printing. Thus an order of 1648 gave power to the searchers “to search in any house or place where there is just cause of suspicion, that Presses are kept and employed in the printing of Scandalous and lying Pamphlets, . . . [and] to seize such scandalous and lying pamphlets as they find upon search <em>. . . .” </em><footnotemark>16</footnotemark> The Restoration brought a new licensing act in 1662. Under its authority “messengers of the press” operated under the secretaries of state, who issued executive warrants for the seizure of persons and papers. These warrants, while sometimes specific in content, often gave the most general discretionary authority. For example, a warrant to Roger L’Estrange, the Surveyor of the Press, empowered him to “seize all seditious books and libels and to apprehend the authors, contrivers, printers, publishers, and dispersers of them,” and to “search any house, shop, printing room, chamber, warehouse, etc. for seditious, scandalous or unlicensed pictures, books, or papers, to bring away or deface the same, and the letter press, taking away all the copies . . . .” <footnotemark>17</footnotemark> Another warrant gave L’Estrange power to “search for <page-number citation-index="1" label="727">*727</page-number>&amp; seize authors, contrivers, printers, . . . publishers, dispensers, &amp; concealers of treasonable, schismaticall, seditious or unlicensed books, libells, pamphlets, or papers . . . together with all copys exemplaryes of such Books, libells, pamphlets or paper as aforesaid.” <footnotemark>18</footnotemark></p>
<p id="AV-M">Although increasingly attacked, the licensing system was continued in effect for a time even after the Revolution of 1688 and executive warrants continued to issue for the search for and seizure of offending books. The Stationers’ Company was also ordered “to make often and diligent searches in all such places you or any of you shall know or have any probable reason to suspect, and to seize all unlicensed, scandalous books and pamphlets . . . .” <footnotemark>19</footnotemark> And even when the device of prosecution for seditious libel replaced licensing as the principal governmental control of the press,<footnotemark>20</footnotemark> it too was enforced with the aid of general warrants — authorizing either the arrest of all persons connected with the publication of a particular libel and the search of their premises, or the seizure of all the papers of a named person alleged to be connected with the publication of a libel.<footnotemark>21</footnotemark></p>
<p id="b764-4"><page-number citation-index="1" label="728">*728</page-number>Enforcement through general warrants was finally judicially condemned in England. This was the consequence of the struggle of the 1760’s between the Crown and the opposition press led by John Wilkes, author and editor of the North Briton. From this struggle came the great case of <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, which this Court has called “one of the landmarks of English liberty.” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626</a></span>. A warrant based on a charge of seditious libel issued for the arrest of Entick, writer for an opposition paper, and for the seizure of all his papers. The officers executing the warrant ransacked Entick’s home for four hours and carted away great quantities of books and papers. Lord Camden declared the general warrant for the seizure of papers contrary to the common law, despite its long history. Camden said: “This power so assumed by the secretary of state is an execution upon all the party’s papers, in the first instance. His house is rifled; his most valuable secrets are taken out of his possession, before the paper for which he is charged is found to be criminal by any competent jurisdiction, and before he is convicted either of writing, publishing, or being concerned in the paper.” At 1064. Camden expressly dismissed the contention that such a warrant could be justified on the grounds that it was “necessary for the ends of government to lodge such a power with a state <em>officer; </em>and . . . better to prevent the publication before than to punish the offender afterwards.” At 1073. In <em>Wilkes </em>v. <em>Wood, </em>19 How. St. Tr. 1153, Camden also condemned the general warrants employed against John Wilkes for his publication of issue No. 45 of the North Briton. He declared that these warrants, calling for the arrest of unnamed persons connected with the alleged libel and seizure of their papers, amounted to a “discretionary power given to messengers to search wherever their suspicions may chance to fall. If such a power is <page-number citation-index="1" label="729">*729</page-number>truly invested in a secretary of state, and he can delegate this power, it certainly may affect the person and property of every man in this kingdom, and is totally subversive of the liberty of the subject.” <em>Id., </em>1167.<footnotemark>22</footnotemark></p>
<p id="b765-5">This history was, of course, part of the intellectual matrix within which our own constitutional fabric was shaped. The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression. For the serious hazard of suppression of innocent expression inhered in the discretion confided in the officers authorized to exercise the power.</p>
<p id="b765-6">II.</p>
<p id="b765-7">The question here is whether the use by Missouri in this case of the search and seizure power to suppress <page-number citation-index="1" label="730">*730</page-number>obscene publications involved abuses inimical to protected expression. We held in <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/#485" aria-description="Citation for case: Roth v. United States">354 U. S. 476, 485</a></span>,<footnotemark>23</footnotemark> that “obscenity is not within the area of constitutionally protected speech or press.” But in <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>itself we expressly recognized the complexity of the test of obscenity fashioned in that case, and the vital necessity in its application of safeguards to prevent denial of “the protection of freedom of speech and press for material which does not treat sex in a manner appealing to prurient interest.” <em>Id., </em>p. 488. We have since held that a State’s power to suppress obscenity is limited by the constitutional protections for free expression. In <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#155" aria-description="Citation for case: Smith v. California">361 U. S. 147, 155</a></span>, we said, “The existence of the State’s power to prevent the distribution of obscene matter does not mean that there can be no constitutional barrier to any form of practical exercise of that power,” inasmuch as “our holding in <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>does not recognize any state power to restrict the dissemination of books which are not obscene.” <em>Id., </em>p. 152. We therefore held that a State may not impose absolute criminal liability on a bookseller for the possession of obscene material, even if it may dispense with the element of <em>scienter </em>in dealing with such evils as impure food and drugs. We remarked the distinction between the cases: “There is no specific constitutional inhibition against making the distributors of food the strictest censors of their merchandise, but the constitutional guarantees of the freedom of speech and of the press stand in the way of imposing a similar requirement on the bookseller.” <em>Id., </em>pp. 152-153. The Missouri Supreme Court’s assimilation of obscene literature to gambling paraphernalia or other contraband for purposes of search and seizure does not therefore answer the appellants’ constitutional claim, but merely restates the issue <page-number citation-index="1" label="731">*731</page-number>whether obscenity may be treated in the same way. The authority to the police officers under the warrants issued in this case, broadly to seize “obscene . . . publications,” poses problems not raised by the warrants to seize “gambling implements” and “all intoxicating liquors” involved in the cases cited by the Missouri Supreme Court. <span class="citation" data-id="5024262"><a href="/opinion/5201171/search-warrant-of-property-at-5-west-12th-street-kansas-city-v-marcus/#125" aria-description="Citation for case: Search Warrant of Property at 5 West 12th Street, Kansas...">334 S. W. 2d, at 125</a></span>. For the use of these warrants implicates questions whether the procedures leading to their issuance and surrounding their execution were adequate to avoid suppression of constitutionally protected publications. “. . . [T]he line between speech unconditionally guaranteed and speech which may legitimately be regulated, suppressed, or punished is finely drawn. . . . The separation of legitimate from illegitimate speech calls for . . . sensitive tools . . . .” <em>Speiser </em>v. <em>Randall, </em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525</a></span>.<footnotemark>24</footnotemark> It follows that, under the Fourteenth Amendment, a State is not free to adopt whatever procedures it pleases for dealing with obscenity as here involved without regard to the possible consequences for constitutionally protected speech.</p>
<p id="b767-5">We believe that Missouri’s procedures as applied in this case lacked the safeguards which due process demands to assure nonobscene material the constitutional protection to which it is entitled. Putting to one side the fact that no opportunity was afforded the appellants to elicit and contest the reasons for the officer’s belief, or otherwise to argue against the propriety of the seizure to the issuing judge, still the warrants issued on the strength <page-number citation-index="1" label="732">*732</page-number>of the conclusory assertions of a single police officer, without any scrutiny by the judge of any materials considered by the complainant to be obscene. The warrants gave the broadest discretion to the executing officers; they merely repeated the language of the statute and the complaints, specified no publications, and left to the individual judgment of each of the many police officers involved the selection of such magazines as in his view constituted “obscene . . . publications.” So far as appears from the record, none of the officers except Lieutenant Coughlin had previously examined any of the publications which were subsequently seized. It is plain that in many instances, if not in all, each officer actually made <em>ad hoc </em>decisions on the spot and, gauged by the number of publications seized and the time spent in executing the warrants, each decision was made with little opportunity for reflection and deliberation. As to publications seized because they appeared on the Lieutenant’s list, we know nothing of the basis for the original judgment that they were obscene. It is no reflection on the good faith or judgment of the officers to conclude that the task they were assigned was simply an impossible one to perform with any realistic expectation that the obscene might be accurately separated from the constitutionally protected. They were provided with no guide to the exercise of informed discretion, because there was no step in the procedure before seizure designed to focus searchingly on the question of obscenity. See generally 1 Chafee, Government and Mass Communications, pp. 200-218. In consequence there were suppressed and withheld from the market for over two months 180 publications not found obscene.<footnotemark>25</footnotemark> The fact that only one-third of the <page-number citation-index="1" label="733">*733</page-number>publications seized were finally condemned strengthens the conclusion that discretion to seize allegedly obscene materials cannot be confided to law enforcement officials without greater safeguards than were here operative. Procedures which sweep so broadly and with so little discrimination are obviously deficient in techniques required by the Due Process Clause of the Fourteenth Amendment to prevent erosion of the constitutional guarantees.<footnotemark>26</footnotemark></p>
<p id="b770-5"><page-number citation-index="1" label="734">*734</page-number>III.</p>
<p id="b770-6">The reliance of the Missouri Supreme Court upon <em>Kingsley Books, Inc., </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S. 436</a></span>, is misplaced. The differences in the procedures under the New York statute upheld in that case and the Missouri procedures as applied here are marked. They amount to the distinction between “a 'limited injunctive remedy,’ under closely defined procedural safeguards, against the sale and distribution of written and printed matter found after due trial to be obscene,” <span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/#437" aria-description="Citation for case: Kingsley Books, Inc. v. Brown"><em>Kingsley Books, supra, </em>at 437</a></span>, and a scheme which in operation inhibited the circulation of publications indiscriminately because of the <page-number citation-index="1" label="735">*735</page-number>absence of any such safeguards. <em>First, </em>the New York injunctive proceeding was initiated by a complaint filed with the court which charged that a particular named obscene publication had been displayed, and to which were annexed copies of the publication alleged to be obscene.<footnotemark>27</footnotemark> The court, in restraining distribution pending final judicial determination of the claim, thus had the allegedly obscene material before it and could exercise an independent check on the judgment of the prosecuting authority at a point before any restraint took place. <em>Second, </em>the restraints in <em>Kingsley Books, </em>both temporary and permanent, ran only against the named publication ; no catchall restraint against the distribution of all “obscene” material was imposed on the defendants there, comparable to the warrants here which authorized a mass seizure and the removal of a broad range of items from circulation.<footnotemark>28</footnotemark> <em>Third, Kingsley Books </em>does not support the proposition that the State may impose the extensive <page-number citation-index="1" label="736">*736</page-number>restraints imposed here on the distribution of these publications prior to an adversary proceeding on the issue of obscenity, irrespective of whether or not the material is legally obscene. This Court expressly noted there that the State was not attempting to punish the distributors for disobedience of any interim order entered before hearing. The Court pointed out that New York might well construe its own law as not imposing any punishment for violation of an interim order were the book found not obscene after due trial. 354 U. S., at 443, n. 2. But there is no doubt that an effective restraint — indeed the most effective restraint possible — was imposed prior to hearing on the circulation of the publications in this case, because all copies on which the police could lay their hands were physically removed from the newsstands and from the premises of the wholesale distributor. An opportunity comparable to that which the distributor in <em>Kingsley Books </em>might have had to circulate the publication despite the interim restraint and then raise the claim of nonobscenity by way of defense to a prosecution for doing so was never afforded these appellants because the copies they possessed were taken away. Their ability to circulate their publications was left to the chance of securing other copies, themselves subject to mass seizure under other such warrants. The public’s opportunity to obtain the publications was thus determined by the distributor’s readiness and ability to outwit the police by obtaining and selling other copies before they in turn could be seized. In addition to its unseemliness, we do not believe that this kind of enforced competition affords a reasonable likelihood that nonobscene publications, entitled to constitutional protection, will reach the public. A distributor may have every reason to believe that a publication is constitutionally protected and will be so held after judicial hearing, but his belief is unavailing as against the contrary judgment of <page-number citation-index="1" label="737">*737</page-number>the police officer who seizes it from him.<footnotemark>29</footnotemark> Finally, a subdivision of the New York statute in <em>Kingsley Books </em>required that a judicial decision on the merits of obscenity be made within two days of trial, which in turn was required to be within one day of the joinder of issue on the request for an injunction.<footnotemark>30</footnotemark> In contrast, the Missouri statutory scheme drawn in question here has no limitation on the time within which decision must be made, only a provision for rapid trial of the issue of obscenity. And in fact over two months elapsed between seizure and decision.<footnotemark>31</footnotemark> In these circumstances the restraint on the circu<page-number citation-index="1" label="738">*738</page-number>lation of publications was far more thoroughgoing and drastic than any restraint upheld by this Court in <em>Kingsley Books.</em></p>
<p id="b774-6">Mass seizure in the fashion of this case was thus effected without any safeguards to protect legitimate expression. The judgment of the Missouri Supreme Court sustaining the condemnation of the 100 publications therefore cannot be sustained. We have no occasion to reach the question of the correctness of the finding that the publications are obscene. Nor is it necessary for us to decide in this case whether Missouri lacks all power under its statutory scheme to seize and condemn obscene material. Since a violation of the Fourteenth Amendment infected the proceedings, in order to vindicate appellants’ constitutional rights the judgment is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b774-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b754-12"> These procedures are separate from and in addition to the State’s criminal statutes. See <em>State </em>v. <em>Mac Sales Co., </em><span class="citation" data-id="1484628"><a href="/opinion/1484628/state-v-mac-sales-co/" aria-description="Citation for case: State v. Mac Sales Co.">263 S. W. 2d 860</a></span>. The criminal statutes are Mo. Rev. Stat., §§563.270, 563.280, 563.290; see also § 563.310.</p>
</footnote>
<footnote label="2">
<p id="b755-5"> Mo. Rev. Stat., §542.380, in pertinent part provides:</p>
<p id="b755-6">“Upon complaint being made, on oath, in writing, to any officer authorized to issue process for the apprehension of offenders, that any of the property or articles herein named are kept within the county of such officer, if he shall be satisfied that there is reasonable ground for such complaint, shall issue a warrant to the sheriff or any constable of the county, directing him to search for and seize any of the following property or articles:</p>
<p id="b755-7">“(2) Any of the following articles, kept for the purpose of being sold, published, exhibited, given away or otherwise distributed or circulated, viz.: obscene, lewd, licentious, indecent or lascivious books, pamphlets, ballads, papers, drawings, lithographs, engravings, pictures, models, casts, prints or other articles or publications of an indecent, immoral or scandalous character, or any letters, handbills, cards, circulars, books, pamphlet's or advertisements or notices of any kind giving information, directly or indirectly, when, where, how or of whom any of such things can be obtained.” These procedures also govern seizure and condemnation of gambling paraphernalia, contraceptive devices, and tools and other articles used to manufacture or produce such items. Fraudulent, forged, and counterfeited writings and other articles, and the instruments used to make them, are also declared contraband and subject to seizure. § 542.440.</p>
</footnote>
<footnote label="3">
<p id="b755-8"> Missouri Supreme Court Rule 33.01 of the Rules of Criminal Procedure provides:</p>
<p id="b755-9">“(a) If a complaint in writing be filed with the judge or magistrate of any court having original jurisdiction to try criminal offenses stating that personal property . . . the seizure of which under search warrant is now or may hereafter be authorized by any statute of this <page-number citation-index="1" label="720">*720</page-number>State, is being held or kept at any place or in any building . . . within the territorial jurisdiction of such judge or magistrate, and if such complaint be verified by the oath or affirmation of the complainant and states such facts positively and not upon information or belief; or if the same be supported by written affidavits verified by oath or affirmation stating evidential facts from which such judge or magistrate determines the existence of probable cause, then such judge or magistrate shall issue a search warrant directed to any peace officer commanding him to search the place therein described and to seize and bring before such judge or magistrate the personal property therein described.</p>
<p id="b756-8">“ (b) The complainant and the warrant issued thereon must contain a description of the personal property to be searched for and seized and a description of the place to be searched, in sufficient detail and particularity to enable the officer serving the warrant to readily ascertain and identify the same.”</p>
</footnote>
<footnote label="4">
<p id="b756-9"> Mo. Rev. Stat., §542.400 provides:</p>
<p id="b756-10">“The judge or magistrate issuing the warrant shall set a day, not less than five days nor more than twenty days after the date of such service and seizure, for determining whether such property is the kind of property mentioned in section 542.380, and shall order the officer having such property in charge to retain possession of the same until after such hearing. Written notice of the date and place of such hearing shall be given, at least five days before such date, by posting a copy of such notice in a conspicuous place upon the premises in which such property is seized, and by delivering a copy of such notice to any person claiming an interest in such property, whose name may be known to the person making the complaint or to the officer'issuing or serving such warrant, or leaving the same at the usual place of abode of such person with any member of his family or household above the age of fifteen years. Such notice shall be signed by the magistrate or judge or by the clerk of the court of such judge.”</p>
</footnote>
<footnote label="5">
<p id="b757-7"> Mo. Rev. Stat., § 542.410 provides:</p>
<p id="b757-8">“Rights of property owner. — The owner or owners of such property may appear at such hearing and defend against the charges as to the nature and use of the property so seized, and such judge or magistrate shall determine, from the evidence produced at such hearing, whether the property is the kind of property m'entioned in section 542.380.”</p>
</footnote>
<footnote label="6">
<p id="b757-9"> Mo. Rev. Stat., § 542.420 provides:</p>
<p id="b757-10">“Disposition of property. — If the judge or magistrate hearing such cause shall determine that the property or articles are of the kind mentioned in section 542.380, he shall cause the same to be publicly destroyed, by burning or otherwise, and if he find that such property is not of the kind mentioned, he shall order the same returned to its owner. If it appears that it may be necessary to use such articles or property as evidence in any criminal prosecution, the judge or magistrate shall order the officer having possession of them to retain such possession until such necessity no longer exists, and they shall neither be destroyed nor returned to the owner until they are no longer needed as such evidence.”</p>
</footnote>
<footnote label="7">
<p id="b758-7"> He bought a copy of the same magazine at three of the stands, a copy of another edition of this magazine at a fourth stand, and a copy of one other magazine at the fifth stand;</p>
</footnote>
<footnote label="8">
<p id="b759-6"> The publications seized included so-called “girlie” magazines, nudist magazines, treatises and manuals on sex, photography magazines, cartoon and joke books and still photographs.</p>
</footnote>
<footnote label="9">
<p id="b759-7"> Because of the result which we reach, it is unnecessary to decide other constitutional questions raised by the appellants, (1) whether the Missouri statutes are invalid on their face as authorizing an unconstitutional censorship and previous restraint of publications; (2) whether the Missouri courts applied an unconstitutional test of obscenity; and (3) whether the publications condemned are obscene under the test of <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b761-7"> 1 Arber, Transcript of the Registers of the Company of Stationers of London, 1554 — 1640 A. D., p. xxxi.</p>
</footnote>
<footnote label="11">
<p id="b761-8"> Elton, The Tudor Constitution, p. 106.</p>
</footnote>
<footnote label="12">
<p id="b761-9"> Elton, <em>supra, </em>pp. 182-183.</p>
</footnote>
<footnote label="13">
<p id="b761-10"> Siebert, <em>supra, </em>pp. 83, 85-86, 97.</p>
</footnote>
<footnote label="14">
<p id="b762-6"> Siebert, <em>supra, </em>p. 139, citing Pat. Roll, 9 Jac. I, Pt. 18; <em>id., </em>II, Pt. 15.</p>
</footnote>
<footnote label="15">
<p id="b762-7"> 4 Arber, <em>supra, </em>pp. 529-536.</p>
</footnote>
<footnote label="16">
<p id="b762-8"> Siebert, <em>supra, </em>214-215, note 72.</p>
</footnote>
<footnote label="17">
<p id="b762-9"> Siebert, <em>supra, </em>p. 254, citing Minute Entry Book 5, p. 177.</p>
</footnote>
<footnote label="18">
<p id="b763-5"> Siebert, <em>supra, </em>p. 256, citing Entry Book, Chas. II, 1664, Vol. 21, p. 21; also Vol. 16, p. 130.</p>
</footnote>
<footnote label="19">
<p id="b763-6"> Cal. St. P., Dom. Ser., 1690-1691, p. 74.</p>
</footnote>
<footnote label="20">
<p id="b763-7"> One of the primary objections to licensing was its enforcement through search and seizure. The House of Commons’ list of reasons why the licensing act should not be renewed included: “Because that Act subjects all Mens Houses, as well Peers as Commoners, to be searched at any Time, either by Day or Night, by a Warrant under the Sign Manual, or under the Hand of One of the Secretaries of State, directed to any Messenger, if such Messenger shall upon probable Reason suspect that there are any unlicensed Books there; and the Houses of all Persons free of the Company of Stationers are subject to the like Search, on a Warrant from the Master and Wardens of the said Company, or any One of them.” 15 Journals of the House of Lords, April 18, 1695, p. 546.</p>
</footnote>
<footnote label="21">
<p id="b763-8"> Siebert, <em>supra, </em>pp. 374 — 376.</p>
</footnote>
<footnote label="22">
<p id="b765-8"> A contemporary London pamphlet summed up the widespread indignation against the use of the general warrant for the seizure of papers: “In such a party-crime, as a public libel, who can endure this assumed authority of taking all papers indiscriminately? . . . where there is even a charge against one particular paper, to seize <em>all, </em>of every kind, is extravagant, unreasonable and inquisitorial. It is infamous in theory, and downright tyranny and despotism in practice.” Father of Candor, A Letter Concerning Libels, Warrants, and the Seizure of Papers, p. 48 (2d ed. 1764, J. Almon printer).</p>
<p id="b765-9">See generally Lasson, The History and Development of the Fourth Amendment, pp'. 42-50; Hanson, Government and the Press, 1695-1763, pp. 29-32, 49-50. An even broader form of general warrant was the writ of assistance, which met such vigorous opposition in the American Colonies prior to the Revolution. Unlike the warrants of the North Briton affair and <em>Entick </em>v. <em>Carrington, </em>which were at least concerned with a particular designated libel, these writs empowered the executing officer to seize any illegally imported goods or merchandise. Moreover, in addition to authorizing search without limit of place, they had no fixed duration. In effect, complete discretion was given to the executing officials; in the words of James Otis, their use placed “the liberty of every man in the hands of every petty officer.” Tudor, Life of James Otis (1823), p. 66. See Lasson, <em>supra, </em>pp. 51-78.</p>
</footnote>
<footnote label="23">
<p id="b766-6"> This holding applied also to the obscenity question raised under the Fourteenth Amendment in <em>Alberts </em>v. <em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/" aria-description="Citation for case: Smith v. California">California</a></span>, </em>decided in the same opinion.</p>
</footnote>
<footnote label="24">
<p id="b767-6"> Lord Camden in <em>Entick </em>v. <em>Carrington </em>recognized that there was no justification for the abuse of the search and seizure power in suppressing seditious libel, even if the view were accepted that “men ought not to be allowed to have such evil instruments in their keeping.” 19 How. St. Tr., at 1072. He said, “If [libels may be seized], I am afraid, that all the inconveniences of a general seizure will follow upon a right allowed to seize a part. The search in such cases will be general, and every house will fall under the power of a secretary of state to be rummaged before proper conviction.” <em>Id.., </em>at 1071.</p>
</footnote>
<footnote label="25">
<p id="b768-6"> Among the publications ordered returned were such titles as “The Dawn of Rational Sex Ethics,” “Sex Symbolism,” “Notes on Cases of Sexual Suppression,” “Your Affections, Emotions and Feel<page-number citation-index="1" label="733">*733</page-number>ings,” “Sexual Impotence, Its Causes and Treatments,” “The Psychology of Sex Life,” “Freud on Sleep and Sexual Dreams,” “The Determination of Sex,” “Sex and Psychoanalysis,” “Artificial Insemination,” “Syphilis, A Treatise for the American Public,” “What You Should Know About Sexual Impotency,” “Variations in Sexual Behavior,” “Sex Life in Marriage,” “Psychopathia Sexualis,” “The Sex Technique in Marriage,” “Sexual Deviations,” “Sex Practice in Later Years,” and “Marriage, Sex, and Family Problems.”</p>
</footnote>
<footnote label="26">
<p id="b769-5"> English practice in such cases has placed greater restraint on the seizure power. Seizure of obscene material, as a prelude to condemnation, was authorized there by Lord Campbell’s Obscene Publications Act of 1857, 20 &amp; 21 Vict., c. 83. As originally proposed, that statute would have allowed search for and seizure of obscene matter either under authority granted by magistrates or on warrants granted by the Chief Commissioner of Police. Moreover, the affidavit for obtaining a warrant would have been required to contain merely the statement that the person making it had reasonable ground for suspicion that obscene publications were kept on the premises to be searched. See 146 Hansard’s Parliamentary Debates, 3d Series, p. 866. These provisions met vigorous opposition in Parliament. A number of members emphasized that the difficulty of defining obscenity made broad search powers in police hands extremely dangerous. See <em>id., </em>pp. 330-332, 1360-1362, 147 Hansard, <em>supra, </em>pp. 1863-1864. As a result, amendments were adopted removing the grant of authority to the police commissioner to authorize a search and seizure, requiring greater specificity in the allegations before a warrant could be issued, and providing that warrants could issue only for the seizure of books the publication of which would constitute a common-law misdemeanor. Lord Lyndhurst, draftsman of these amendments, explained: “I have now provided that the person shall swear that he has reason to believe, and that he does believe, that there are such publications in <page-number citation-index="1" label="734">*734</page-number>such a place, and shall further state to the magistrate the reasons which lead to that belief. Nor does it stop there. The most material Amendment is, that he must state what the publications are, and that they are of such a nature that, if published, the party publishing them will be guilty of a misdemeanour. The magistrate must also be satisfied that the case is a proper one for a prosecution 146 Hansard, <em>supra, </em>at p. 1360. The Lord Chancellor summarized the effect of the changes: “As the Bill now stood, these search-warrants would only be granted after great precautions . . . .” <em>Id., </em>p. 1362.</p>
<p id="b770-8">According to a recent summary of procedures to obtain a warrant under that Act, a police officer would ordinarily buy copies of a work he suspected of obscenity. They would be examined by the police and sent to the Director of Public Prosecutions. The latter would return them with advice as to whether a warrant should be applied for. If a decision were made to seek a warrant, the publications would be laid before a magistrate with the sworn affidavit of the officer, in order that he might be satisfied that they were of the character necessary to justify seizure. See Memorandum of the Association of Chief Police Officers of England and Wales, Minutes of Evidence Taken Before the Select Committee of the House of Commons on the Obscene Publications Bill, 1956-1957, pp. 132-136. See also, <em>id., </em>p. 23.</p>
<p id="b770-9">The Act was replaced by the Obscene Publications Act of 1959, 7 &amp; 8 Eliz. II, c. 66. See 23 Mod. L. Bev. 285.</p>
</footnote>
<footnote label="27">
<p id="b771-5"> The feasibility of particularization in complaint and warrant in a ease such as the present is apparent, since the publications were sold on newsstands distributing to the public. Compare Lord Camden’s remark in <em>Entick </em>v. <em>Carrington, </em>directed to the contention that a general warrant might be justifiable as a means of uncovering evidence of crime: “If ... a right of search for the sake of discovering evidence ought in any case to be allowed, this crime [seditious libel] above all others ought to be excepted, as wanting such a discovery less than any other. It is committed in open daylight, and in the face of the world; . . .” 19 How. St. Tr., at 1074.</p>
</footnote>
<footnote label="28">
<p id="b771-6"> The trial judge in <em>Kingsley Books </em>refused to enjoin the distribution of future issues of the publication in question, stating: “[u]nless the work be before the court at the time of the hearing at which the injunction is sought, it is inappropriate to make a judicial determination with respect to it. In respect of this feature of the case, the plaintiff seeks a likely trespass upon a constitutionally protected area, and the court must reject that prayer.” <span class="citation" data-id="5432110"><a href="/opinion/5589878/burke-v-kingsley-books-inc/#168" aria-description="Citation for case: Burke v. Kingsley Books, Inc.">208 Misc. 150, 168-169</a></span>, 142 N. Y. S. 2d 735, 751. Cf. <em>Near </em>v. <em>Minnesota ex rel. Olson, </em><span class="citation" data-id="9418724"><a href="/opinion/101773/near-v-minnesota-ex-rel-olson/" aria-description="Citation for case: Near v. Minnesota Ex Rel. Olson">283 U. S. 697</a></span>.</p>
</footnote>
<footnote label="29">
<p id="b773-4"> Cf. Freund, The Supreme Court and Civil Liberties, <span class="citation no-link">4 Vand. L. Rev. 533</span>, 539.</p>
<p id="b773-5">Blackstone’s often-quoted formulation of the principle of freedom of the press, though restricted to the prohibition of <em>“previous </em>restraints upon publications,” nevertheless acknowledged the importance of an adjudicatory procedure as a protection against the suppression of inoffensive publications. He wrote: “to punish (as the law does at present) any dangerous or offensive writings, which, when published, shall <em>on a fair and impartial trial be adjudged of a pernicious tendency, </em>is necessary for the preservation of peace and good order . . . .” 4 Commentaries, pp. 151-152. (Emphasis added.) Compare Butler, J., dissenting in <em>Near </em>v. <em>Minnesota ex rel. <span class="citation" data-id="9418724"><a href="/opinion/101773/near-v-minnesota-ex-rel-olson/" aria-description="Citation for case: Near v. Minnesota Ex Rel. Olson">Olson, supra,</a></span> </em>p. 723: “The decision of the Court in this case declares Minnesota and every other State powerless to restrain by injunction the business of publishing and circulating among the people malicious, scandalous and defamatory periodicals that <em>in due course of judicial procedure has been adjudged to be a public nuisance.’’ </em>(Emphasis added.)</p>
</footnote>
<footnote label="30">
<p id="b773-6"> This provision was not directly implicated in <em>Kingsley Books </em>because the parties had waived the provision for immediate trial.</p>
</footnote>
<footnote label="31">
<p id="b773-7"> Compare the objection of the House of Commons to renewal of licensing: “Because that Act appoints no Time wherein the Archbishop, or Bishop of London, shall appoint a learned Man, or that One or more of the Company of Stationers shall go to the Customhouse, to view imported Books; so that they or either of them may delay it till the Importer may be undone, by having so great a Part of his Stock lie dead . . . .” 15 Journals of the House of Lords, April 18, 1695, p. 546.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Marshall v. Barlow's Inc.json  (`lake-record`, 6 assertions)

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
{"assertion_id": "1c1444b7a934b593", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Marshall v. Barlow's Inc"}, "payload": {"all": [{"cite": "436 U.S. 307", "page": "307", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "436"}, {"cite": "98 S. Ct. 1816", "page": "1816", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "56 L. Ed. 2d 305", "page": "305", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}, {"cite": "1978 U.S. LEXIS 26", "page": "26", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}, {"cite": "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434", "page": "20434", "reporter": "Envtl. L. Rep. (Envtl. Law Inst.)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "8"}, {"cite": "6 OSHC (BNA) 1571", "page": "1571", "reporter": "OSHC (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "6"}], "display": "436 U.S. 307", "official": {"cite": "436 U.S. 307", "page": "307", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "436"}, "official_selection_present": true, "record_id": "Marshall v. Barlow's Inc"}}
{"assertion_id": "8a2daae3f23410ff", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-324", "record_id": "Marshall v. Barlow's Inc"}, "payload": {"fragment": "#:~:text=do%20not%20suffice%20to%20justify", "page": null, "pin_id": "pin-324", "pinpoint_status": "star-verified", "quote": "do not suffice to justify warrantless inspections under OSHA or vitiate the general constitutional requirement that for a search to be reasonable a warrant must be obtained.", "quote_fidelity": "matched", "record_id": "Marshall v. Barlow's Inc", "star_marker": "324"}}
{"assertion_id": "a912a916f966e59b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-325", "record_id": "Marshall v. Barlow's Inc"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-325", "pinpoint_status": "slip-only", "quote": "We hold that Barlow's was entitled to a declaratory judgment that the Act is unconstitutional insofar as it purports to authorize inspections without warrant or its equivalent.", "quote_fidelity": "mismatch", "record_id": "Marshall v. Barlow's Inc", "star_marker": null}}
{"assertion_id": "eacd55f28fd00635", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-311", "record_id": "Marshall v. Barlow's Inc"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-311", "pinpoint_status": "slip-only", "quote": "--- # Marshall v. Barlow's, Inc. *436 U.S. 307 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An OSHA inspector arrived at Barlow's, Inc., an electrical and plumbing business in Idaho, to inspect the nonpublic work area for safety violations. There was no complaint; the firm had simply come up in OSHA's selection process. The owner asked whether the inspector had a warrant; he had none, so the owner refused entry, invoking the Fourth Amendment. Section 8(a) of the Occupational Safety and Health Act purported to authorize such inspections without any warrant. ## Issue Whether OSHA may constitutionally authorize warrantless inspections of the nonpublic areas of an employer's premises over the employer's objection. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Marshall v. Barlow's Inc", "star_marker": null}}
{"assertion_id": "fbc7160e4b560bed", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-313", "record_id": "Marshall v. Barlow's Inc"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-313", "pinpoint_status": "slip-only", "quote": "unless some recognized exception to the warrant requirement applies, *See v. Seattle* would require a warrant to conduct the inspection sought in this case.", "quote_fidelity": "mismatch", "record_id": "Marshall v. Barlow's Inc", "star_marker": null}}
{"assertion_id": "866d4da94dd2c463", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Marshall v. Barlow's Inc"}, "payload": {"as_of_content": "1978-05-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Marshall v. Barlow's Inc", "scope_note": "Good law. OSHA § 8(a)'s warrantless-inspection authorization held unconstitutional; the administrative-warrant requirement for ordinary workplaces stands.", "varies_by_point": false}}
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
