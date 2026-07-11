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

## GROUP: _overhaul2/lake/cases/Taylor v. Alabama.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Taylor v. Alabama"
type: case
citation: "457 U.S. 687 (1982)"
parallel_cite: "102 S. Ct. 2664; 73 L. Ed. 2d 314"
neutral_cite: 1982 U.S. LEXIS 138
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-23
docket: 81-5152
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Taylor v. Alabama
  varies_by_point: false
  scope_note: "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110760/taylor-v-alabama/"
  cluster_id: 110760
  opinion_id: 110760
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny (attenuation)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Brown v. Illinois]]", "[[Dunaway v. New York]]", "[[Wong Sun v. United States]]", "[[Davis v. Mississippi]]", "[[Kaupp v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation", "illegal-arrest", "confession"]
holding: "A confession obtained after a warrantless arrest made without probable cause must be suppressed as the fruit of the illegal arrest where no significant intervening event broke the causal chain; Miranda warnings, the passage of a few hours, and a later ex parte warrant did not attenuate the taint."
lake:
  record_id: Taylor v. Alabama
  status: verified
  projected_at: 2026-07-09
---

# Taylor v. Alabama

*457 U.S. 687 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Taylor was arrested without a warrant or probable cause for a grocery-store robbery, on an uncorroborated, second-hand tip. Held at the station, he was given [[Miranda and Custodial Interrogation|Miranda warnings]], questioned on several occasions over about six hours, fingerprinted, and put in a lineup. While he was in custody police matched his prints to prints from the scene and filed an arrest warrant *[[Common Legal Terms#ex-parte|ex parte]]*. After a brief visit with his girlfriend, he signed a confession. He moved to suppress it as the fruit of his illegal arrest. The confession was conceded "voluntary" for Fifth Amendment purposes.

## Issue
Whether a confession obtained after an arrest made without probable cause must be suppressed as a fruit of the illegal arrest, or whether [[Miranda and Custodial Interrogation|Miranda warnings]], the lapse of several hours, a visitor, and a later-filed warrant sufficiently attenuated the taint.

## Rule
The confession must be suppressed unless the taint is purged. "[A] confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is 'sufficiently an act of free will to purge the primary taint.'" — 457 U.S. at 690 (quoting *Brown v. Illinois*, 422 U.S. 590, 602). ^pin-690

A Fifth Amendment finding of voluntariness is "merely a threshold requirement for Fourth Amendment analysis"; were [[Miranda and Custodial Interrogation|Miranda warnings]] "viewed as a talisman that cured all Fourth Amendment violations," the guarantee would shrink to a "form of words." — [*Id.* at 690](https://www.courtlistener.com/opinion/110760/taylor-v-alabama/#:~:text=merely%20a%20threshold%20requirement%20for) (quoting *Brown*, 422 U.S. at 601, 603). ^pin-690b

## Application
The case was "a virtual replica of both *Brown* and *Dunaway*." "Petitioner was arrested without probable cause in the hope that something would turn up, and he confessed shortly thereafter without any meaningful intervening event." — *Id.* at 691. ^pin-691

The roughly six-hour interval was not significant where Taylor remained in custody, unrepresented, repeatedly questioned, fingerprinted, and placed in a lineup; the three [[Miranda and Custodial Interrogation|Miranda warnings]] did not break the chain; and the brief, emotionally fraught visit with his girlfriend did not free his will. The *[[Common Legal Terms#ex-parte|ex parte]]* arrest warrant filed mid-interrogation rested on fingerprints that "were themselves the fruit of petitioner's illegal arrest," so it could not supply [[Fruits and Attenuation|attenuation]]. The State failed to carry its burden of showing admissibility.

## Conclusion
The confession was the unattenuated fruit of the illegal arrest and should have been suppressed; the judgment of the Alabama Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Taylor* applies the [[Brown v. Illinois]] [[Fruits and Attenuation|attenuation]] factors and follows [[Dunaway v. New York]], reaffirming that a Fifth Amendment–voluntary confession can still be a suppressible Fourth Amendment fruit; the tainted fingerprints trace to [[Davis v. Mississippi]]. [[Kaupp v. Texas]] later applied the same analysis [[Common Legal Terms#per-curiam|per curiam]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny ([[Fruits and Attenuation|attenuation]])*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Taylor v. Alabama*, 457 U.S. 687 (1982) — https://www.courtlistener.com/opinion/110760/taylor-v-alabama/ — pinpoints: 690, 691, 692–693.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "477f6265442a5640", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Taylor v. Alabama"}, "payload": {"all": [{"cite": "457 U.S. 687", "page": "687", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "457"}, {"cite": "102 S. Ct. 2664", "page": "2664", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "73 L. Ed. 2d 314", "page": "314", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "73"}, {"cite": "1982 U.S. LEXIS 138", "page": "138", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1982"}], "display": "457 U.S. 687", "official": {"cite": "457 U.S. 687", "page": "687", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "457"}, "official_selection_present": true, "record_id": "Taylor v. Alabama"}}
{"assertion_id": "14b6a9673e4764ef", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-691", "record_id": "Taylor v. Alabama"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-691", "pinpoint_status": "slip-only", "quote": "a virtual replica of both *Brown* and *Dunaway*.", "quote_fidelity": "mismatch", "record_id": "Taylor v. Alabama", "star_marker": null}}
{"assertion_id": "312f3add21891e55", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-690b", "record_id": "Taylor v. Alabama"}, "payload": {"fragment": "#:~:text=merely%20a%20threshold%20requirement%20for", "page": null, "pin_id": "pin-690b", "pinpoint_status": "star-verified", "quote": "merely a threshold requirement for Fourth Amendment analysis", "quote_fidelity": "matched", "record_id": "Taylor v. Alabama", "star_marker": "690"}}
{"assertion_id": "a6384d7913747ba9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-690", "record_id": "Taylor v. Alabama"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-690", "pinpoint_status": "slip-only", "quote": "for Fifth Amendment purposes. ## Issue Whether a confession obtained after an arrest made without probable cause must be suppressed as a fruit of the illegal arrest, or whether Miranda warnings, the lapse of several hours, a visitor, and a later-filed warrant sufficiently attenuated the taint. ## Rule The confession must be suppressed unless the taint is purged.", "quote_fidelity": "mismatch", "record_id": "Taylor v. Alabama", "star_marker": null}}
{"assertion_id": "c5e81a46ed9f50dc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Taylor v. Alabama"}, "payload": {"as_of_content": "1982-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Taylor v. Alabama", "scope_note": "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law.", "varies_by_point": false}}
```

### lake record — Taylor v. Alabama

```json
{
  "schema_version": "s2.v1",
  "record_id": "Taylor v. Alabama",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Taylor v. Alabama",
    "case_name_short": "Taylor",
    "case_name_full": "Taylor v. Alabama",
    "input_case_name": "Taylor v. Alabama",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-23",
    "year": 1982,
    "docket": "81-5152",
    "cluster_id": 110760,
    "lead_opinion_id": 110760,
    "sibling_ids": [
      110760,
      9428855,
      9428856
    ],
    "absolute_url": "/opinion/110760/taylor-v-alabama/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "457 U.S. 687",
      "volume": "457",
      "reporter": "U.S.",
      "page": "687",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 2664",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2664",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 314",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 138",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "138",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "457 U.S. 687",
        "volume": "457",
        "reporter": "U.S.",
        "page": "687",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 2664",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2664",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 314",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "314",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 138",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "138",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "457 U.S. 687",
    "official_selection": {
      "court_class": "scotus",
      "selected": "457 U.S. 687",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-690",
      "page": null,
      "quote": "for Fifth Amendment purposes. ## Issue Whether a confession obtained after an arrest made without probable cause must be suppressed as a fruit of the illegal arrest, or whether Miranda warnings, the lapse of several hours, a visitor, and a later-filed warrant sufficiently attenuated the taint. ## Rule The confession must be suppressed unless the taint is purged.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-690b",
      "page": null,
      "quote": "merely a threshold requirement for Fourth Amendment analysis",
      "star_marker": "690",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9078,
      "fragment": "#:~:text=merely%20a%20threshold%20requirement%20for",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-691",
      "page": null,
      "quote": "a virtual replica of both *Brown* and *Dunaway*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Taylor v. Alabama",
    "varies_by_point": false,
    "scope_note": "Applies the Brown v. Illinois attenuation factors; the confession was conceded voluntary for Fifth Amendment purposes yet still suppressed as a Fourth Amendment fruit. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Rong He",
          "cluster_id": 4455505,
          "cite": [
            "2017 NY Slip Op 9172",
            "156 A.D.3d 907",
            "68 N.Y.S.3d 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Weems v. State",
          "cluster_id": 1629131,
          "cite": [
            "167 S.W.3d 350",
            "2005 WL 486548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
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
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corbin v. State",
          "cluster_id": 1636551,
          "cite": [
            "91 S.W.3d 383",
            "2002 Tex. App. LEXIS 7528",
            "2002 WL 31374687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cantu",
          "cluster_id": 22035,
          "cite": [
            "230 F.3d 148",
            "2000 WL 1481157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2364279,
          "cite": [
            "843 S.W.2d 252",
            "1992 Tex. App. LEXIS 3034",
            "1992 WL 357865"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane1_negative"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. State",
          "cluster_id": 1575568,
          "cite": [
            "829 S.W.2d 191",
            "1992 Tex. Crim. App. LEXIS 62",
            "1992 WL 55274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1733045,
          "cite": [
            "667 S.W.2d 137",
            "1984 Tex. Crim. App. LEXIS 610"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaupp v. Texas",
          "cluster_id": 127919,
          "cite": [
            "155 L. Ed. 2d 814",
            "123 S. Ct. 1843",
            "538 U.S. 626",
            "2003 U.S. LEXIS 3670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. State",
          "cluster_id": 2434027,
          "cite": [
            "724 S.W.2d 780",
            "1986 Tex. Crim. App. LEXIS 1216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harry Seidman",
          "cluster_id": 758049,
          "cite": [
            "156 F.3d 542",
            "159 L.R.R.M. (BNA) 2211",
            "1998 U.S. App. LEXIS 21924",
            "1998 WL 574761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Thomas Cherry",
          "cluster_id": 450747,
          "cite": [
            "759 F.2d 1196",
            "81 A.L.R. Fed. 303",
            "1985 U.S. App. LEXIS 29511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Armenta",
          "cluster_id": 1125086,
          "cite": [
            "948 P.2d 1280"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmy Dewitt Webster, Sr., Candido Daniel Santiago, Barry Weinreich, Joe Buhajla, Arthur Byron Murphy, and Clarence Royalston",
          "cluster_id": 445460,
          "cite": [
            "750 F.2d 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lanier v. State",
          "cluster_id": 1832223,
          "cite": [
            "450 So. 2d 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Green",
          "cluster_id": 739711,
          "cite": [
            "111 F.3d 515",
            "1997 WL 175484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
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
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lenin M. Jerez and Carlos M. Solis",
          "cluster_id": 737426,
          "cite": [
            "108 F.3d 684"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Manbeck, United States of America v. Kenneth Herring, United States of America v. Mark Huiet Sale, United States of America v. Lorenz Josephus Proden, United States of America v. Kermit Theodore Brogden, United States of America v. John Wesley Flannel, United States of America v. Gary Gallopo, United States of America v. John Benjamin Barton, Jr., Jessie Lee Mallory, and Arthur Duncan, United States of America v. John O'hare, Eddie Brantley, Thomas Earnest Folske, Thomas Sams Hightower, Timothy Allen Laxton, Harrell Lewis, Jr., and John Isidore Stevens, United States of America v. Aaron Douglas Staetter, John Michael Iyoob, James Anthony Hastings, and Gregory Michael Scott, United States of America v. David Martin Summerville",
          "cluster_id": 441989,
          "cite": [
            "744 F.2d 360",
            "1984 U.S. App. LEXIS 18698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Little v. State",
          "cluster_id": 1562842,
          "cite": [
            "758 S.W.2d 551",
            "1988 Tex. Crim. App. LEXIS 50",
            "1988 WL 23631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Iduarte",
          "cluster_id": 1487736,
          "cite": [
            "268 S.W.3d 544",
            "2008 Tex. Crim. App. LEXIS 1626",
            "2008 WL 4724143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Juarez v. State",
          "cluster_id": 1562920,
          "cite": [
            "758 S.W.2d 772",
            "1988 Tex. Crim. App. LEXIS 172",
            "1988 WL 98938"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Alabama:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110760 OR 9428855 OR 9428856) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzY3NzEyMDAwMDAmcz0xMTIwOTI0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110760+OR+9428855+OR+9428856%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110760 OR 9428855 OR 9428856)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0xMDI1NzM1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110760+OR+9428855+OR+9428856%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110760 OR 9428855 OR 9428856)",
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
    "complete_query": "cites:(110760 OR 9428855 OR 9428856)",
    "indexed_citing_opinions": 413,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110760,
        "count": 373,
        "count_source": "search"
      },
      {
        "opinion_id": 9428855,
        "count": 59,
        "count_source": "search"
      },
      {
        "opinion_id": 9428856,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 633,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/taylor-v-alabama.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1Mjk2MDUmcz00NDIxNDc4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110760+OR+9428855+OR+9428856%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110760,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 108538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 372011,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 374894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 1596133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110760,
        "cited_id": 1596287,
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
    "date_created": "2026-07-05T21:12:45Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:18:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:13:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Taylor v. Alabama

```
<div>
<center><b><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687</a></span> (1982)</b></center>
<center><h1>TAYLOR<br>
v.<br>
ALABAMA</h1></center>
<center>No. 81-5152.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 23, 1982.</center>
<center>Decided June 23, 1982.</center>
CERTIORARI TO THE SUPREME COURT OF ALABAMA
<p><span class="star-pagination">*688</span> <i>Robert M. Beno</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Thomas R. Allison,</i> Assistant Attorney General of Alabama, argued the cause for respondent. With him on the brief was <i>Charles A. Graddick,</i> Attorney General.<sup>[*]</sup></p>
<p><i>Fred E. Inbau, Wayne W. Schmidt, James P. Manak, Patrick F. Healy, William K. Lambie, Richard J. Brzeczek, Frank G. Carrington, Courtney A. Evans, Robert K. Corbin,</i> Attorney General of Arizona, and <i>Steven J. Twist,</i> Chief Assistant Attorney General, <i>Tyrone C. Fahner,</i> Attorney General of Illinois, and <i>Melbourne Noel,</i> Chief Assistant Attorney General, and <i>William L. Parker, Jr.,</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging affirmance.</p>
<p>JUSTICE MARSHALL delivered the opinion of the Court.</p>
<p>This case presents the narrow question whether petitioner's confession should have been suppressed as the fruit of an illegal arrest. The Supreme Court of Alabama held that the evidence was properly admitted. Because the decision below is inconsistent with our decisions in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), and <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), we reverse.</p>
<p></p>
<h2>I</h2>
<p>In 1978, a grocery store in Montgomery, Ala., was robbed. There had been a number of robberies in this area, and the police had initiated an intensive manhunt in an effort to apprehend the robbers. An individual who was at that time incarcerated on unrelated charges told a police officer that "he had heard that [petitioner] Omar Taylor was involved in the robbery." App. 4. This individual had never before given similar information to this officer, did not tell the officer where he had heard this information, and did not provide any details of the crime. This tip was insufficient to give <span class="star-pagination">*689</span> the police probable cause to obtain a warrant or to arrest petitioner.</p>
<p>Nonetheless, on the basis of this information, two officers arrested petitioner without a warrant. They told petitioner that he was being arrested in connection with the grocery-store robbery, searched him, and took him to the station for questioning. Petitioner was given the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). At the station, he was fingerprinted, readvised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, questioned, and placed in a lineup. The victims of the robbery were unable to identify him in the lineup. The police told petitioner that his fingerprints matched those on some grocery items that had been handled by one of the participants in the robbery. After a short visit with his girlfriend and a male companion, petitioner signed a waiver-of-rights form and executed a written confession. The form and the signed confession were admitted into evidence.</p>
<p>Petitioner objected to the admission of this evidence at his trial. He argued that his warrantless arrest was not supported by probable cause, that he had been involuntarily transported to the police station, and that the confession must be suppressed as the fruit of this illegal arrest. The trial court overruled this objection, and petitioner was convicted. On appeal, the Alabama Court of Criminal Appeals reversed, <span class="citation multiple-matches"><a href="/c/So.%202d/399/875/">399 So. 2d 875</a></span> (1980), holding that the facts of this case are virtually indistinguishable from those presented to this Court in <i>Dunaway</i> v. <i>New <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">York, supra</a></span></i><i>,</i> and that the confession should not have been admitted into evidence. The Alabama Supreme Court reversed the Court of Criminal Appeals, <span class="citation" data-id="1596133"><a href="/opinion/1596133/taylor-v-state/" aria-description="Citation for case: Taylor v. State">399 So. 2d 881</a></span> (1981), and we granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./454/963/">454 U. S. 963</a></span> (1981).</p>
<p></p>
<h2>II</h2>
<p>In <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra</a></span></i><i>,</i> and <i>Dunaway</i> v. <i>New <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">York, supra</a></span></i><i>,</i> the police arrested suspects without probable cause. The suspects were transported to police headquarters, advised of their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and interrogated. They confessed <span class="star-pagination">*690</span> within two hours of their arrest. This Court held that the confessions were not admissible at trial, reasoning that a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is " `sufficiently an act of free will to purge the primary taint.' " <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra,</a></span></i> at 602 (quoting <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 486</a></span> (1963)). See also <i>Dunaway</i> v. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York"><i>New York, supra,</i> at 217</a></span>. This Court identified several factors that should be considered in determining whether a confession has been purged of the taint of the illegal arrest: "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct." <i>Brown</i> v. <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Illinois, supra,</i> at 603-604</a></span> (citations and footnote omitted); <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 218</a></span>. The State bears the burden of proving that a confession is admissible. <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Ibid.</a></span></i></p>
<p>In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> this Court firmly established that the fact that the confession may be "voluntary" for purposes of the Fifth Amendment, in the sense that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given and understood, is not by itself sufficient to purge the taint of the illegal arrest. In this situation, a finding of "voluntariness" for purposes of the Fifth Amendment is merely a threshold requirement for Fourth Amendment analysis. See <i>Dunaway</i> v. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#217" aria-description="Citation for case: Dunaway v. New York"><i>New York, supra,</i> at 217</a></span>. The reason for this approach is clear: "[t]he exclusionary rule, . . . when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth" Amendment. <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#601" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 601</a></span>. If <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were viewed as a talisman that cured all Fourth Amendment violations, then the constitutional guarantee against unlawful searches and seizures would be reduced to a mere " `form of words.' " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span></i> at 603 (quoting <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#648" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 648</a></span> (1961)).</p>
<p>This case is a virtual replica of both <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>.</i> <span class="star-pagination">*691</span> Petitioner was arrested without probable cause in the hope that something would turn up, and he confessed shortly thereafter without any meaningful intervening event. The State's arguments to the contrary are unpersuasive. The State begins by focusing on the temporal proximity of the arrest and the confession. It observes that the length of time between the illegal arrest and the confession was six hours in this case, while in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> the incriminating statements were obtained within two hours. However, a difference of a few hours is not significant where, as here, petitioner was in police custody, unrepresented by counsel, and he was questioned on several occasions, fingerprinted, and subjected to a lineup. The State has not even demonstrated the amount of this time that was spent in interrogation, arguing only that petitioner "had every opportunity to consider his situation, to organize his thoughts, to contemplate his constitutional rights, and to exercise his free will." Brief for Respondent 11.</p>
<p>The State points to several intervening events that it argues are sufficient to break the connection between the illegal arrest and petitioner's confession. It observes that petitioner was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings three times. As our foregoing discussion of <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> demonstrates, however, the State's reliance on the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings is misplaced. The State also observes that petitioner visited with his girlfriend and a male companion before he confessed. This claim fares no better. According to the officer and petitioner, these two visitors were outside the interrogation room where petitioner was being questioned. After petitioner signed a waiver-of-rights form, he was allowed to meet with these visitors. The State fails to explain how this 5-to 10-minute visit, after which petitioner immediately recanted his former statements that he knew nothing about the robbery and signed the confession, could possibly have contributed to his ability to consider carefully and objectively his options and to exercise his free will. This suggestion <span class="star-pagination">*692</span> is particularly dubious in light of petitioner's uncontroverted testimony that his girlfriend was emotionally upset at the time of this visit.<sup>[1]</sup> If any inference could be drawn, it would be that this visit had just the opposite effect.</p>
<p>The State points to an arrest warrant filed after petitioner had been arrested and while he was being interrogated as another significant "intervening event." While petitioner was in custody, the police determined that the fingerprints on some grocery items matched those that they had taken from petitioner immediately after his arrest. Based on this comparison, an arrest warrant was filed. The filing of this warrant, however, is irrelevant to whether the confession was the fruit of the illegal arrest. This case is not like <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356</a></span> (1972), where the defendant was brought before a committing Magistrate who advised him of his rights and set bail. Here, the arrest warrant was filed <i>ex parte,</i> based on the comparison of the fingerprints found at the scene of the crime and petitioner's fingerprints, which had been taken immediately after his arrest. The initial fingerprints, <span class="star-pagination">*693</span> which were themselves the fruit of petitioner's illegal arrest, see <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), and which were used to extract the confession from petitioner, cannot be deemed sufficient "attenuation" to break the connection between the illegal arrest and the confession merely because they also formed the basis for an arrest warrant that was filed while petitioner was being interrogated.<sup>[2]</sup></p>
<p>Finally, the State argues that the police conduct here was not flagrant or purposeful, and that we should not follow our decisions in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> for that reason. However, we fail to see any relevant distinction between the conduct here and that in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>.</i> In this case, as in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the police effectuated an investigatory arrest without probable cause, based on an uncorroborated informant's tip, and involuntarily transported petitioner to the station for interrogation in the hope that something would turn up. The fact that the police did not physically abuse petitioner, or that the confession they obtained may have been "voluntary" for purposes of the Fifth Amendment, does not cure the illegality of the initial arrest. Alternatively, the State contends that the police conduct here argues for adopting a "good faith" exception to the exclusionary rule. To date, we have not recognized such an exception, and we decline to do so here.</p>
<p><span class="star-pagination">*694</span> In sum, petitioner's confession was the fruit of his illegal arrest. Under our decisions in <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois</a></span></i> and <i>Dunaway</i> v. <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">New York</a></span></i><i>,</i> the confession clearly should not have been admitted at his trial. Accordingly, we reverse the decision of the Alabama Supreme Court and remand this case for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE O'CONNOR, with whom THE CHIEF JUSTICE, JUSTICE POWELL, and JUSTICE REHNQUIST join, dissenting.</p>
<p>The Court holds today that Omar Taylor's detailed confession was the fruit of an illegal arrest, and consequently, should be suppressed. Because I conclude that neither the facts nor the law supports the Court's analysis, I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>In the course of their investigation of the Moseley robbery, Montgomery police questioned Charles Martin, who was being held on unrelated rape and robbery charges. Martin stated that "he had heard that Omar Taylor was involved in the robbery of Moseley's Grocery," Tr. 6, but the police made no attempt to establish either Martin's credibility as an informant or the reliability of the information he provided.<sup>[1]</sup></p>
<p>Based only on this tip, which did not provide probable cause, Sergeants Alford and Rutland arrested Taylor a little before 3 p.m. on January 4, 1979. At that time, they told him why he was being arrested and advised him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, but asked him no questions regarding the robbery. Tr. 20, 24. When they arrived at the police station, the officers turned Taylor over to detectives.</p>
<p>After Taylor had been fingerprinted and signed a form <span class="star-pagination">*695</span> acknowledging his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, Detective Wilson questioned him for about 15 minutes, Tr. 48, and placed him in a lineup before one of the victims, Mrs. Moseley. <i>Id.,</i> at 37-38. At the lineup, which lasted about an hour, <i>id.,</i> at 48, Mrs. Moseley was unable to identify the petitioner. Following the lineup, Detective Wilson told Taylor that his fingerprints matched the fingerprints removed from grocery items handled by one of the robbers. Nevertheless, the petitioner denied knowledge of the robbery.</p>
<p>Toward 9 p.m. that evening, Detective Hicks readvised Taylor of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, Tr. 25, and Taylor once again read and signed a form setting forth his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Tr. 28, 125. At no time did Taylor ask for a lawyer or indicate that he did not want to talk to police. <i>Id.,</i> at 28-29, 35, 40. During his 5- to 10-minute interview with Taylor, Detective Hicks confronted him with the fingerprint evidence. <i>Id.,</i> at 36. Hicks urged the petitioner to cooperate with the police, but carefully refrained from making him any promises, stating that at most he could inform the judge of the petitioners cooperation. <i>Id.,</i> at 31, 34. Taylor continued to deny involvement in the robbery. <i>Id.,</i> at 35-36.</p>
<p>Following this conversation, both the petitioner's girlfriend and his neighbor came to the police station and requested to speak with him. When Taylor indicated that he wanted to speak with his friends, Detective Hicks left them alone in his office for several minutes.<sup>[2]</sup> After that meeting, <span class="star-pagination">*696</span> the petitioner confessed to the crime, and signed a detailed written confession.<sup>[3]</sup></p>
<p>Before trial, the petitioner moved to suppress his confession, <span class="star-pagination">*697</span> arguing that it was the product of an illegal arrest, and that it had been obtained in violation of his Fifth and Sixth Amendment rights. The trial judge assumed that the arrest was illegal,<sup>[4]</sup> but found that the confession was voluntary, consistent with the Fifth and Sixth Amendments, and that "there were enough intervening factors between the arrest and confession" to overcome the taint of the illegal arrest. <i>Id.,</i> at 116. Accordingly, he admitted the confession.</p>
<p></p>
<h2>II</h2>
<p>Although the Court misapprehends the facts of the present case, it has stated correctly the controlling substantive law. In the Court's words, "a confession obtained through custodial interrogation after an illegal arrest should be excluded unless intervening events break the causal connection between the illegal arrest and the confession so that the confession is `sufficiently an act of free will to purge the primary taint.' " <i>Ante,</i> at 690 (quoting <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 602</a></span> (1975)).</p>
<p>In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> this Court emphasized that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings are an important factor . . . in determining whether the confession [was] obtained by exploitation of an illegal arrest." <i>Id.,</i> at 603.<sup>[5]</sup> The Court did not discount the significance <span class="star-pagination">*698</span> of other factors, however, noting that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings, <i>alone</i> and <i>per se,</i> cannot always make the act sufficiently a product of free will to break, for Fourth Amendment purposes, the causal connection between the illegality and the confession." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> Brown</i> holds, therefore, that not only <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, but also "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, and, particularly, the purpose and flagrancy of the official misconduct are all relevant." <i>Id.,</i> at 603-604 (footnotes and citations omitted).</p>
<p>In light of those factors, the <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> Court reviewed the record and found that "Brown's first statement was separated from his illegal arrest by less than two hours, and [that] there was no intervening event of significance whatsoever." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 604</a></span>. Moreover, the police conduct in arresting Brown was particularly egregious. The "impropriety of the arrest was obvious," and the "manner in which Brown's arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 605</a></span>. The Court held that as a consequence the confession should have been suppressed.</p>
<p>Four Terms later, in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#204" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 204</a></span> (1979), this Court reaffirmed the <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> rule that in order to use at trial statements obtained following an arrest on less than probable cause</p>
<blockquote>"the prosecution must show not only that the statements meet the Fifth Amendment voluntariness standard, but also that the causal connection between the statements and the illegal arrest is broken sufficiently to purge the primary taint of the illegal arrest."</blockquote>
<p>Finding the facts in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> to be "virtually a replica of the situation in <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York"><i>Brown," id.,</i> at 218</a></span>, the Court held that the petitioner's confession should have been suppressed. Critical to the Court's holding was its observation that the petitioner <span class="star-pagination">*699</span> "confessed without any intervening event of significance." <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Ibid.</a></span></i> See <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#219" aria-description="Citation for case: Dunaway v. New York"><i>id.,</i> at 219</a></span> ("No intervening events broke the connection between petitioner's illegal detention and his confession").</p>
<p></p>
<h2>III</h2>
<p>Our task is to apply the law as articulated in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> to the facts of this case.</p>
<p>The first significant consideration is that following his unlawful arrest, Taylor was warned on three separate occasions that he</p>
<blockquote>"had a right to remain silent, [and] anything he said could be used against him in a court of law[;] he had the right to have an attorney present, [and] if he could not afford one, the State would appoint one for him[;] he could answer questions but he could stop answering at any time." Tr. 23.</blockquote>
<p>Under <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> these warnings must be counted as "an important factor . . . in determining whether the confession [was] obtained by exploitation of an illegal arrest," <i>Brown</i> v. <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Illinois, supra,</i> at 603</a></span>, though they are, standing alone, insufficient to prove that the primary taint of an illegal arrest had been purged.</p>
<p>Second, in contrast to the facts in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> the facts in the present case show that the petitioner was not subjected to intimidating police misconduct. In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> police had broken into the petitioner's house and searched it. When the petitioner later came home, two officers pointed their guns at him and arrested him, leading the Court to conclude that "[t]he manner in which [the petitioner's] arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 605</a></span>. By contrast, nothing in the record before us indicates that the petitioner's arrest was violent, or designed to "cause surprise, fright, and confusion." Instead, Montgomery officers approached <span class="star-pagination">*700</span> Taylor, asked him his name, and told him that he was under arrest for the Moseley robbery. They then searched him, advised him of his rights, and took him to the police station.</p>
<p>Third, while in both <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> there was "no intervening event of significance whatsoever," <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>, in the present case Taylor's girlfriend and neighbor came to the police station and asked to speak with him. Before meeting with his two friends, the petitioner steadfastly had denied involvement in the Moseley robbery. Immediately following the meeting, the petitioner gave a complete and detailed confession of his participation in the armed robbery. This meeting between the petitioner and his two friends, as described by the police in their testimony at the suppression hearing, plainly constituted an intervening circumstance.</p>
<p>Finally, the record reveals that the petitioner spent most of the time between his arrest and confession by himself.<sup>[6]</sup> In <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span></i> and <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</i> by contrast, the defendants were interrogated continuously before they made incriminating statements.</p>
<p>In sum, when these four factors are considered together,<sup>[7]</sup> it is obvious that there is no sufficient basis on which to overturn the trial court's finding that "there were enough intervening factors" to overcome the taint of the illegal arrest. In fact, I believe it is clear that the State carried its burden of proof. The petitioner was warned of his rights to remain silent <span class="star-pagination">*701</span> and to have a lawyer present, and there is no dispute that he understood those rights or that he waived them voluntarily and without coercion. After receiving three sets of such warnings, he met with his girlfriend and neighbor, <i>at his request.</i> Following that meeting, at which no police officers were present, the petitioner decided to confess to his participation in the robbery. The petitioner's confession was not proximately caused by his illegal arrest, but was the product of a decision based both on knowledge of his constitutional rights and on the discussion with his friends. Accordingly, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Arthur F. Mathews</i> and <i>James E. Coleman, Jr.,</i> filed a brief for the American Civil Liberties Union as <i>amicus curiae</i> urging reversal.</p>
<p>[1]  According to petitioner, his girlfriend became upset upon hearing the officer advise petitioner to cooperate. App. 16. Contrary to the allegations in the dissent, at no point did the officer contradict petitioner's version of his girlfriend's emotional state or petitioner's statement that his girlfriend was present at the time the officer advised him to cooperate. In fact, the testimony from both petitioner and the officer with respect to this visit are consistent. The officer testified only that he advised petitioner to cooperate between the time petitioner signed a rights form at the commencement of this interrogation period and the time that petitioner signed the statement of confession. Tr. 31, 136-137. He also testified that during this same interval, he allowed the short visit between petitioner and his girlfriend. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Ibid.</a></span></i> The District Court made no findings of fact with respect to these incidents. In any event, even assuming the accuracy of the dissent's version of the facts, compare <i>post,</i> at 695, and n. 2, with Tr. 31, 136-137, the dissent offers no explanation for its conclusion that this 5-to 10-minute visit should be viewed as an intervening event that purges the taint of the illegal arrest.</p>
<p>[2]  Petitioner also raises an ambiguous objection to the admission of fingerprint evidence at his trial. The trial court granted petitioner's motion to suppress the initial fingerprints as the fruit of his illegal arrest under <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), and granted the State's motion to take petitioner's fingerprints at trial. The nature of petitioner's objection to the admission of any fingerprint evidence at trial is unclear, and it is also uncertain whether an objection to the procedure used for taking the second set of fingerprints has been properly preserved for our review. In any event, we need not reach this issue because we reverse the decision on the ground that the confession should not have been admitted. To the extent that petitioner still may challenge the fingerprinting procedure employed below, the state courts should be given the opportunity to address this challenge in the first instance.</p>
<p>[1]  The police, however, suspected Martin of complicity in the Moseley robbery, Tr. 15. It later developed that Martin had instigated, planned, and participated in the robbery.</p>
<p>[2]  The Court's rather different account of this meeting apparently stems from a decision to accept the testimony most favorable to the holding it wants to reach. That decision, however, runs counter to the longstanding practice of federal appellate courts to uphold the denial of the motion to suppress if, in the absence of any express findings by the district court, there is any reasonable view of the evidence to support it. See <i>United States</i> v. <i>Payton,</i> <span class="citation" data-id="374894"><a href="/opinion/374894/united-states-v-william-charles-payton/#923" aria-description="Citation for case: United States v. William Charles Payton">615 F. 2d 922, 923</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/969/">446 U. S. 969</a></span> (1980); <i>United States</i> v. <i>Vicknair,</i> <span class="citation" data-id="372011"><a href="/opinion/372011/united-states-v-vicknair/#376" aria-description="Citation for case: United States v. Vicknair">610 F. 2d 372, 376, n. 4</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/823/">449 U. S. 823</a></span> (1980). In the present case, the officer testified that Taylor's "girlfriend came to us and said she wanted to talk to Omar, and we told Omar she was outside and he wanted to talk to her. And at that time, we let him talk to her." Tr. 35. Detective Hicks specifically denied that he had urged Taylor to talk to his girlfriend. <i>Id.,</i> at 35, 133-134. The detective acknowledged that he had told the petitioner that he could inform the judge of the petitioner's cooperation, but he expressly denied making any other statements to Taylor or his girlfriend about "cooperation." <i>Id.,</i> at 31, 134.
</p>
<p>The petitioner, of course, had a vastly different version. He testified that the police had brought his girlfriend into the room and told him, in her presence, that he was facing 10 years to life in prison, but that if he cooperated they might be able to arrange a suspended sentence or probation. Upon hearing that remark, the petitioner's girlfriend became upset and began to cry, at which point the police left the petitioner alone with his friends. <i>Id.,</i> at 52. As we noted above, the police expressly denied making any such statements. More importantly, upon comparing the two versions, it becomes clear that in an effort to support its holding, the Court has parsed through the petitioner's story and plucked those tidbits that the police did not expressly contradict. This method of setting forth the facts of a case on appellate review hardly comports with the rule that an appellate court must adopt any reasonable view of the evidence that supports the trial court's ruling.</p>
<p>Since there is nothing unreasonable about the police account of the meeting between the petitioner and his friends, that version is the one we must accept on review. At the hearing, Detective Hicks testified that after Taylor asked to speak with his friends, the police left them alone together. There is no suggestion, other than the petitioner's discredited version of the meeting, that the police said anything to the petitioners girlfriend, or that she became upset. Thus, the Court errs in stating that the petitioner's girlfriend became upset because of statements made by the police, and in intimating that the police created a coercive atmosphere in which the petitioner could not carefully consider his options and, on the basis of his friends' advice, decide to confess to the robbery.</p>
<p>[3]  In that confession, the petitioner stated that Charles Martin approached him with guns and a plan to rob Moseley's Grocery. Taylor's role in the robbery was to distract Mr. Moseley by buying some groceries. Just before his accomplices pulled out their guns, Taylor put down the groceries and walked outside to see whether an approaching car was a police car. When he saw that it was not a police car, he began to reenter the store, but stopped when he saw the robbery taking place. Thereafter he fled, met his cofelons at a preassigned place, and took his share of the money. <i>Id.,</i> at 128-132.</p>
<p>[4]  In fact, the State did not seriously contend that the arrest had been based on probable cause. See <i>id.,</i> at 8, 10.</p>
<p>[5]  The holding in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> was derived from this Court's seminal decision in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), in which we rejected a "but for" test for determining whether to suppress evidence gathered following a Fourth Amendment violation.
</p>
<p>"We need not hold that all evidence is `fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is `whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.' Maguire, Evidence of Guilt, 221 (1959)." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 487-488</a></span>.</p>
<p>[6]  The petitioner confessed some six hours after his arrest. As JUSTICE STEVENS noted in his concurring opinion in <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the "temporal relationship between the arrest and the confession may be an ambiguous factor," <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#220" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 220</a></span>, for a lengthy detention could be used to exploit an illegal arrest at least as easily as a brief detention. In the present case, there seems to be nothing remarkable, one way or the other, about the length of detention.</p>
<p>[7]  The Court has taken each circumstance out of context and examined it to see whether it alone would be enough to purge the taint of the illegal arrest. The Court's failure to consider the circumstances of this case as a whole may have contributed to its erroneous conclusion.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Taylor v. Riojas.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Taylor v. Riojas"
type: case
citation: "592 U.S. 7 (2020)"
parallel_cite: "141 S. Ct. 52; 208 L. Ed. 2d 164"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2020
date_decided: 2020-11-02
docket: 19-1261
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2020-11-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Taylor v. Riojas
  varies_by_point: false
  scope_note: "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4802501/taylor-v-riojas/"
  cluster_id: 4802501
  opinion_id: 4582848
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Limiting"
related: ["[[White v. Pauly]]", "[[Mullenix v. Luna]]", "[[Harlow v. Fitzgerald]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "clearly-established", "obvious-case", "eighth-amendment"]
holding: "Qualified immunity can be defeated without a case directly on point where the constitutional violation is so obvious that any reasonable officer would have known the conduct was unlawful."
lake:
  record_id: Taylor v. Riojas
  status: verified
  projected_at: 2026-07-06
---

# Taylor v. Riojas

*592 U.S. 7 (2020)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Trent Taylor, a Texas inmate, alleged that for six days correctional officers confined him in two "shockingly unsanitary cells": the first covered nearly floor to ceiling in massive amounts of feces, and the second a frigid cell with only a clogged floor drain, where — left naked and without a bunk — he was forced to sleep in raw sewage that overflowed the drain. The Fifth Circuit held these conditions violated the Eighth Amendment but granted the officers [[Qualified Immunity|qualified immunity]] because no prior case had clearly established that such conditions, for "only six days," were unconstitutional.

## Issue
Whether officers were entitled to [[Qualified Immunity|qualified immunity]] for these conditions of confinement merely because no prior decision had specifically addressed materially similar facts.

## Rule
No. Where the unconstitutionality of conduct is obvious, [[Qualified Immunity|qualified immunity]] does not require a prior case on point. "no reasonable correctional officer could have concluded that, under the extreme circumstances of this case, it was constitutionally permissible to house Taylor in such deplorably unsanitary conditions for such an extended period of time." — 592 U.S. 7 (slip op., at 2). ^pin-7

Invoking *[[Hope v. Pelzer]]*, the Court reiterated that "a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question." "Confronted with the particularly egregious facts of this case, any reasonable officer should have realized that Taylor's conditions of confinement offended the Constitution." — *Id.* (slip op., at 3). ^pin-7b

## Application
The egregiousness of the conditions — cells teeming with human waste, with no necessity or [[Exigent Circumstances and Hot Pursuit|exigency]] shown and no reason the conditions could not have been mitigated — made the violation obvious, so the absence of a factually identical precedent did not entitle the officers to immunity. The Fifth Circuit's lone contrary case was "too dissimilar, in terms of both conditions and duration of confinement, to create any doubt about the obviousness of Taylor's right." The Court noted that an officer-by-officer analysis would still be required [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted, judgment [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). [[Qualified Immunity|Qualified immunity]] was wrongly granted; the obvious unconstitutionality of the conditions provided the officers fair warning even without a case directly on point.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Taylor* is a leading modern application of the *[[Hope v. Pelzer]]* "obvious case" route to defeating [[Qualified Immunity|qualified immunity]], a counterweight to the high-specificity decisions like [[Mullenix v. Luna]] and [[White v. Pauly]]. The same Term, the Court relied on it to GVR a related Fifth Circuit case (*McCoy v. Alamu*). No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Limiting*

## Sources
- *Taylor v. Riojas*, 592 U.S. 7 (2020) (per curiam) — https://www.courtlistener.com/opinion/4802501/taylor-v-riojas/ — pinpoint: slip op., at 2–3 (CL stores the slip opinion "592 U. S. ____ (2020)"; pin keyed to the official case-start page 7).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6409bdd91818c081", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Taylor v. Riojas"}, "payload": {"all": [{"cite": "592 U.S. 7", "page": "7", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "592"}, {"cite": "141 S. Ct. 52", "page": "52", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "208 L. Ed. 2d 164", "page": "164", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "208"}], "display": "592 U.S. 7", "official": {"cite": "592 U.S. 7", "page": "7", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "592"}, "official_selection_present": true, "record_id": "Taylor v. Riojas"}}
{"assertion_id": "32821e1279f14cd8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-7", "record_id": "Taylor v. Riojas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-7", "pinpoint_status": "slip-only", "quote": "were unconstitutional. ## Issue Whether officers were entitled to qualified immunity for these conditions of confinement merely because no prior decision had specifically addressed materially similar facts. ## Rule No. Where the unconstitutionality of conduct is obvious, qualified immunity does not require a prior case on point.", "quote_fidelity": "mismatch", "record_id": "Taylor v. Riojas", "star_marker": null}}
{"assertion_id": "5df96b31d7bc36b0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-7b", "record_id": "Taylor v. Riojas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-7b", "pinpoint_status": "slip-only", "quote": "a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question.", "quote_fidelity": "mismatch", "record_id": "Taylor v. Riojas", "star_marker": null}}
{"assertion_id": "8ce83f7e7d85f154", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Taylor v. Riojas"}, "payload": {"as_of_content": "2020-11-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Taylor v. Riojas", "scope_note": "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point.", "varies_by_point": false}}
```

### lake record — Taylor v. Riojas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Taylor v. Riojas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Taylor v. Riojas",
    "case_name_short": "Taylor",
    "case_name_full": "",
    "input_case_name": "Taylor v. Riojas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2020-11-02",
    "year": 2020,
    "docket": "19-1261",
    "cluster_id": 4802501,
    "lead_opinion_id": 4582848,
    "sibling_ids": [
      4582848
    ],
    "absolute_url": "/opinion/4802501/taylor-v-riojas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 7",
      "volume": "592",
      "reporter": "U.S.",
      "page": "7",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 52",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 164",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 7",
        "volume": "592",
        "reporter": "U.S.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 52",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 164",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 7",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 7",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-7",
      "page": null,
      "quote": "were unconstitutional. ## Issue Whether officers were entitled to qualified immunity for these conditions of confinement merely because no prior decision had specifically addressed materially similar facts. ## Rule No. Where the unconstitutionality of conduct is obvious, qualified immunity does not require a prior case on point.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-7b",
      "page": null,
      "quote": "a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-11-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Taylor v. Riojas",
    "varies_by_point": false,
    "scope_note": "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gail Stockton v. Milwaukee County, Wisconsin",
          "cluster_id": 7855452,
          "cite": [
            "44 F.4th 605"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Percy Taylor v. Joseph Ways",
          "cluster_id": 4888555,
          "cite": [
            "999 F.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Seth Michael Zakora v. Troy Chrisman",
          "cluster_id": 7855600,
          "cite": [
            "44 F.4th 452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguirre v. City of San Antonio",
          "cluster_id": 4876506,
          "cite": [
            "995 F.3d 395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marie Moderwell v. Cuyahoga Cnty., Ohio",
          "cluster_id": 4882339,
          "cite": [
            "997 F.3d 653"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cope v. Cogdill",
          "cluster_id": 4897232,
          "cite": [
            "3 F.4th 198"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David King v. Timothy Riley",
          "cluster_id": 9418866,
          "cite": [
            "76 F.4th 259"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Thorpe v. Harold Clarke",
          "cluster_id": 7454730,
          "cite": [
            "37 F.4th 926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trellus Richmond v. Mario J. Badia",
          "cluster_id": 7858519,
          "cite": [
            "47 F.4th 1172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James O'Doan v. Joshua Sanford",
          "cluster_id": 4865836,
          "cite": [
            "991 F.3d 1027"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. John Yost",
          "cluster_id": 9385401,
          "cite": [
            "63 F.4th 211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timothy Finley v. Erica Huss",
          "cluster_id": 9506473,
          "cite": [
            "102 F.4th 789"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernando Lopez v. Sheriff of Cook County",
          "cluster_id": 4872436,
          "cite": [
            "993 F.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terrance Prude v. Anthony Meli",
          "cluster_id": 9418547,
          "cite": [
            "76 F.4th 648"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan Jones v. George Solomon",
          "cluster_id": 9457388,
          "cite": [
            "90 F.4th 198"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Jackson v. City of Cleveland",
          "cluster_id": 9389985,
          "cite": [
            "64 F.4th 736"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Sabo v. Megan Erickson",
          "cluster_id": 10325326,
          "cite": [
            "128 F.4th 836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "LaChance v. Town of Charlton",
          "cluster_id": 4860892,
          "cite": [
            "990 F.3d 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4582848) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      },
      "lane2_top_cited": {
        "query": "cites:(4582848)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNCZzPTk0NzM1NTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284582848%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4582848)",
        "reviewed": 55,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 55,
        "triage_read": 0,
        "triage_snippet_classified": 55
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4582848)",
    "indexed_citing_opinions": 99,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4582848,
        "count": 99,
        "count_source": "search"
      }
    ],
    "citation_count": 420,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/taylor-v-riojas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5Mjk0NTYmcz0xMDAzNTcyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284582848%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4582848,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 758498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 4466815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9427304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9434318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9795093,
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
    "date_created": "2026-07-05T21:18:03Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:21:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Taylor v. Riojas

```
                     Cite as: 592 U. S. ____ (2020)                     1

                              Per Curiam

SUPREME COURT OF THE UNITED STATES
TRENT MICHAEL TAYLOR v. ROBERT RIOJAS, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
               No. 19–1261. Decided November 2, 2020

   PER CURIAM.
   Petitioner Trent Taylor is an inmate in the custody of the
Texas Department of Criminal Justice. Taylor alleges that,
for six full days in September 2013, correctional officers
confined him in a pair of shockingly unsanitary cells.1 The
first cell was covered, nearly floor to ceiling, in “ ‘massive
amounts’ of feces”: all over the floor, the ceiling, the win-
dow, the walls, and even “ ‘packed inside the water faucet.’ ”
Taylor v. Stevens, 946 F. 3d 211, 218 (CA5 2019). Fearing
that his food and water would be contaminated, Taylor did
not eat or drink for nearly four days. Correctional officers
then moved Taylor to a second, frigidly cold cell, which was
equipped with only a clogged drain in the floor to dispose of
bodily wastes. Taylor held his bladder for over 24 hours,
but he eventually (and involuntarily) relieved himself,
causing the drain to overflow and raw sewage to spill across
the floor. Because the cell lacked a bunk, and because Tay-
lor was confined without clothing, he was left to sleep naked
in sewage.
   The Court of Appeals for the Fifth Circuit properly held
that such conditions of confinement violate the Eighth
Amendment’s prohibition on cruel and unusual punish-
ment. But, based on its assessment that “[t]he law wasn’t
clearly established” that “prisoners couldn’t be housed in
——————
  1 The Fifth Circuit accepted Taylor’s “verified pleadings [as] competent

evidence at summary judgment.” Taylor v. Stevens, 946 F. 3d 211, 221
(2019). As is appropriate at the summary-judgment stage, facts that are
subject to genuine dispute are viewed in the light most favorable to Tay-
lor’s claim.
2                     TAYLOR v. RIOJAS

                          Per Curiam

cells teeming with human waste” “for only six days,” the
court concluded that the prison officials responsible for Tay-
lor’s confinement did not have “ ‘fair warning’ that their spe-
cific acts were unconstitutional.” 946 F. 3d, at 222 (quoting
Hope v. Pelzer, 536 U. S. 730, 741 (2002)).
   The Fifth Circuit erred in granting the officers qualified
immunity on this basis. “Qualified immunity shields an of-
ficer from suit when she makes a decision that, even if con-
stitutionally deficient, reasonably misapprehends the law
governing the circumstances she confronted.” Brosseau v.
Haugen, 543 U. S. 194, 198 (2004) (per curiam). But no rea-
sonable correctional officer could have concluded that, un-
der the extreme circumstances of this case, it was constitu-
tionally permissible to house Taylor in such deplorably
unsanitary conditions for such an extended period of time.
See Hope, 536 U. S., at 741 (explaining that “ ‘a general con-
stitutional rule already identified in the decisional law may
apply with obvious clarity to the specific conduct in ques-
tion’ ” (quoting United States v. Lanier, 520 U. S. 259, 271
(1997))); 536 U. S., at 745 (holding that “[t]he obvious cru-
elty inherent” in putting inmates in certain wantonly “de-
grading and dangerous” situations provides officers “with
some notice that their alleged conduct violate[s]” the Eighth
Amendment). The Fifth Circuit identified no evidence that
the conditions of Taylor’s confinement were compelled by
necessity or exigency. Nor does the summary-judgment
record reveal any reason to suspect that the conditions of
Taylor’s confinement could not have been mitigated, either
in degree or duration. And although an officer-by-officer
analysis will be necessary on remand, the record suggests
that at least some officers involved in Taylor’s ordeal were
deliberately indifferent to the conditions of his cells. See,
e.g., 946 F. 3d, at 218 (one officer, upon placing Taylor in
the first feces-covered cell, remarked to another that Taylor
was “ ‘going to have a long weekend’ ”); ibid., and n. 9 (an-
other officer, upon placing Taylor in the second cell, told
                      Cite as: 592 U. S. ____ (2020)                     3

                               Per Curiam

Taylor he hoped Taylor would “ ‘f***ing freeze’ ”).
  Confronted with the particularly egregious facts of this
case, any reasonable officer should have realized that Tay-
lor’s conditions of confinement offended the Constitution.2
We therefore grant Taylor’s petition for a writ of certiorari,
vacate the judgment of the Court of Appeals for the Fifth
Circuit, and remand the case for further proceedings con-
sistent with this opinion.
                                            It is so ordered.

  JUSTICE BARRETT took no part in the consideration or
decision of this case.

  JUSTICE THOMAS dissents.




——————
   2 In holding otherwise, the Fifth Circuit noted “ambiguity in the

caselaw” regarding whether “a time period so short [as six days] violated
the Constitution.” 946 F. 3d, at 222. But the case that troubled the Fifth
Circuit is too dissimilar, in terms of both conditions and duration of con-
finement, to create any doubt about the obviousness of Taylor’s right.
See Davis v. Scott, 157 F. 3d 1003, 1004 (CA5 1998) (no Eighth Amend-
ment violation where inmate was detained for three days in dirty cell
and provided cleaning supplies).
                  Cite as: 592 U. S. ____ (2020)             1

                ALITO, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
TRENT MICHAEL TAYLOR v. ROBERT RIOJAS, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
             No. 19–1261. Decided November 2, 2020

   JUSTICE ALITO, concurring in the judgment.
   Because the Court has granted the petition for a writ of
certiorari, I will address the question that the Court has
chosen to decide. But I find it hard to understand why the
Court has seen fit to grant review and address that ques-
tion.
                               I
   To see why this petition is ill-suited for review, it is im-
portant to review the procedural posture of this case. Peti-
tioner, an inmate in a Texas prison, sued multiple prison
officers and asserted a variety of claims, including both the
Eighth Amendment claim that the Court addresses (placing
and keeping him in filthy cells) and a related Eighth
Amendment claim (refusing to take him to a toilet). The
District Court granted summary judgment for the defend-
ants on all but one of petitioner’s claims under Federal Rule
of Civil Procedure 54(b), which permitted petitioner to ap-
peal the dismissed claims. On appeal, the Fifth Circuit af-
firmed as to all the claims at issue except the toilet-access
claim. On the claim concerning the conditions of peti-
tioner’s cells, the court held that the facts alleged in peti-
tioner’s verified complaint were sufficient to demonstrate
an Eighth Amendment violation, but it found that the offic-
ers were entitled to qualified immunity based primarily on
a statement in Hutto v. Finney, 437 U. S. 678 (1978), and
the Fifth Circuit’s decision in Davis v. Scott, 157 F. 3d 1003
(1998).
2                     TAYLOR v. RIOJAS

                ALITO, J., concurring in judgment

   The Court now reverses the affirmance of summary judg-
ment on the cell-conditions claim. Viewing the evidence in
the summary judgment record in the light most favorable
to petitioner, the Court holds that a reasonable corrections
officer would have known that it was unconstitutional to
confine petitioner under the conditions alleged. That ques-
tion, which turns entirely on an interpretation of the record
in one particular case, is a quintessential example of the
kind that we almost never review. As stated in our Rules,
“[a] petition for a writ of certiorari is rarely granted when
the asserted error consists of . . . the misapplication of a
properly stated rule of law,” this Court’s Rule 10. That is
precisely the situation here. The Court does not dispute
that the Fifth Circuit applied all the correct legal stand-
ards, but the Court simply disagrees with the Fifth Circuit’s
application of those tests to the facts in a particular record.
Every year, the courts of appeals decide hundreds if not
thousands of cases in which it is debatable whether the ev-
idence in a summary judgment record is just enough or not
quite enough to carry the case to trial. If we began to review
these decisions we would be swamped, and as a rule we do
not do so.
   Instead, we have well-known criteria for granting review,
and they are not met here. The question that the Court
decides is not one that has divided the lower courts, see this
Court’s Rule 10, and today’s decision adds virtually nothing
to the law going forward. The Court of Appeals held that
the conditions alleged by petitioner, if proved, would violate
the Eighth Amendment, and this put correctional officers
in the Fifth Circuit on notice that such conditions are intol-
erable. Thus, even without our intervention, qualified im-
munity would not be available in any similar future case.
   We have sometimes granted review and summarily re-
versed in cases where it appeared that the lower court had
conspicuously disregarded governing Supreme Court prec-
edent, but that is not the situation here. On the contrary,
                  Cite as: 592 U. S. ____ (2020)            3

                ALITO, J., concurring in judgment

as I explain below, it appears that the Court of Appeals
erred largely because it read too much into one of our
decisions.
   It is not even clear that today’s decision is necessary to
protect petitioner’s interests. We are generally hesitant to
grant review of non-final decisions, and there are grounds
for such wariness here. If we had denied review at this
time, petitioner may not have lost the opportunity to con-
test the grant of summary judgment on the issue of re-
spondents’ entitlement to qualified immunity on his cell-
conditions claim. His case would have been remanded for
trial on the claims that remained after the Fifth Circuit’s
decision (one of which sought relief that appears to overlap
with the relief sought on the cell-conditions claim), and if
he was dissatisfied with the final judgment, he may have
been able to seek review by this Court of the cell-conditions
qualified immunity issue at that time. Major League Base-
ball Players Assn. v. Garvey, 532 U. S. 504, 508, n. 1 (2001)
( per curiam). And of course, there is always the possibility
that he would have been satisfied with whatever relief he
obtained on the claims that went to trial.
   Today’s decision does not even conclusively resolve the is-
sue of qualified immunity on the cell-conditions claim be-
cause respondents are free to renew that defense at trial,
and if the facts petitioner alleges are not ultimately estab-
lished, the defense could succeed. Indeed, if petitioner can-
not prove the facts he alleges, he may not be able to show
that his constitutional rights were violated.
   In light of all this, it is not apparent why the Court has
chosen to grant review in this case.
                            II
  While I would not grant review on the question the Court
addresses, I agree that summary judgment should not have
been awarded on the issue of qualified immunity. We must
4                      TAYLOR v. RIOJAS

                 ALITO, J., concurring in judgment

view the summary judgment record in the light most favor-
able to petitioner, and when petitioner’s verified complaint
is read in this way, a reasonable fact-finder could infer not
just that the conditions in the cells in question were horrific
but that respondents chose to place and keep him in those
particular cells, made no effort to have the cells cleaned,
and did not explore the possibility of assignment to cells
with better conditions. A reasonable corrections officer
would have known that this course of conduct was uncon-
stitutional, and the cases on which respondents rely do not
show otherwise.
   Although this Court stated in Hutto that holding a pris-
oner in a “filthy” cell for “a few days” “might be tolerable,”
437 U. S., at 686–687, that equivocal and unspecific dictum
does not justify what petitioner alleges. There are degrees
of filth, ranging from conditions that are simply unpleasant
to conditions that pose a grave health risk, and the concept
of “a few days” is also imprecise. In addition, the statement
does not address potentially important factors, such as the
necessity of placing and keeping a prisoner in a particular
cell and the possibility of cleaning the cell before he is
housed there or during the course of that placement. A rea-
sonable officer could not think that this statement or the
Court of Appeals’ decision in Davis meant that it is consti-
tutional to place a prisoner in the filthiest cells imaginable
for up to six days despite the availability of other preferable
cells or despite the ability to arrange for cleaning of the cells
in question.
   For these reasons, I concur in the judgment.

```

---

## GROUP: _overhaul2/lake/cases/Tennessee v. Garner.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Tennessee v. Garner"
type: case
citation: "471 U.S. 1 (1985)"
parallel_cite: "105 S. Ct. 1694; 85 L. Ed. 2d 1; 53 U.S.L.W. 4410"
neutral_cite: 1985 U.S. LEXIS 195
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-03-27
docket: 83-1035
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-03-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Tennessee v. Garner
  varies_by_point: false
  scope_note: "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111397/tennessee-v-garner/"
  cluster_id: 111397
  opinion_id: 9429990
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Anchor"
related: ["[[Graham v. Connor]]", "[[Scott v. Harris]]"]
aliases: []
tags: ["case", "fourth-amendment", "use-of-force", "deadly-force", "seizure"]
holding: "Deadly force against an apparently unarmed, non-dangerous fleeing suspect is an unreasonable seizure; deadly force needs PC to believe the suspect poses a significant threat of death or serious injury."
lake:
  record_id: Tennessee v. Garner
  status: verified
  projected_at: 2026-07-06
---

# Tennessee v. Garner

*471 U.S. 1 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Memphis officer Elton Hymon shot 15-year-old Edward Garner in the back of the head as Garner—an apparently unarmed suspect whom Hymon was "reasonably sure" was unarmed—climbed a fence to flee a nighttime house burglary. A Tennessee statute authorized deadly force against any fleeing felon. Garner's father sued under 42 U.S.C. § 1983.

## Issue
Whether the Fourth Amendment permits the use of deadly force to prevent the escape of an apparently unarmed, non-dangerous fleeing felon.

## Rule
Deadly force to seize a fleeing suspect is constitutionally constrained. "We conclude that such force may not be used unless it is necessary to prevent the escape and the officer has probable cause to believe that the suspect poses a significant threat of death or serious physical injury to the officer or others." — 471 U.S. at 3. ^pin-3

Thus "[a] police officer may not seize an unarmed, nondangerous suspect by shooting him dead." — *Id.* at 11. ^pin-11

But "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force." — *Id.* ^pin-11a

## Application
Hymon shot Garner although he was reasonably sure Garner was unarmed and posed no immediate threat; a nighttime burglary alone did not make Garner dangerous. Seizing the unarmed, non-dangerous Garner by deadly force was therefore unreasonable, and the Tennessee statute was unconstitutional insofar as it authorized deadly force against such fleeing suspects.

## Conclusion
The use of deadly force against the unarmed, non-dangerous Garner was an unreasonable seizure; the statute was unconstitutional as applied, and the case was [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- [[Scott v. Harris]] later clarified that *Garner* "did not establish a magical on/off switch" but is an application of the [[Graham v. Connor]] objective-reasonableness standard. This is a clarification, not negative treatment; *Garner* remains binding.

## Appears on
- [[Use of Force]] — *Key — Anchor*

## Sources
- *Tennessee v. Garner*, 471 U.S. 1 (1985) — https://www.courtlistener.com/opinion/111397/tennessee-v-garner/ — pinpoints: 3, 11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "75ab20b0deb52ca7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Tennessee v. Garner"}, "payload": {"all": [{"cite": "471 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "471"}, {"cite": "105 S. Ct. 1694", "page": "1694", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "85 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "85"}, {"cite": "1985 U.S. LEXIS 195", "page": "195", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1985"}, {"cite": "53 U.S.L.W. 4410", "page": "4410", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "471 U.S. 1", "official": {"cite": "471 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "471"}, "official_selection_present": true, "record_id": "Tennessee v. Garner"}}
{"assertion_id": "143a63ed176cd6da", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-11", "record_id": "Tennessee v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-11", "pinpoint_status": "slip-only", "quote": "[a] police officer may not seize an unarmed, nondangerous suspect by shooting him dead.", "quote_fidelity": "mismatch", "record_id": "Tennessee v. Garner", "star_marker": null}}
{"assertion_id": "1da6cf1f7d2637d1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-11a", "record_id": "Tennessee v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-11a", "pinpoint_status": "slip-only", "quote": "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force.", "quote_fidelity": "mismatch", "record_id": "Tennessee v. Garner", "star_marker": null}}
{"assertion_id": "49140703fd690117", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-3", "record_id": "Tennessee v. Garner"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-3", "pinpoint_status": "slip-only", "quote": "was unarmed—climbed a fence to flee a nighttime house burglary. A Tennessee statute authorized deadly force against any fleeing felon. Garner's father sued under 42 U.S.C. § 1983. ## Issue Whether the Fourth Amendment permits the use of deadly force to prevent the escape of an apparently unarmed, non-dangerous fleeing felon. ## Rule Deadly force to seize a fleeing suspect is constitutionally constrained.", "quote_fidelity": "mismatch", "record_id": "Tennessee v. Garner", "star_marker": null}}
{"assertion_id": "fd777576ca04c21e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Tennessee v. Garner"}, "payload": {"as_of_content": "1985-03-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Tennessee v. Garner", "scope_note": "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch.", "varies_by_point": false}}
```

### lake record — Tennessee v. Garner

```json
{
  "schema_version": "s2.v1",
  "record_id": "Tennessee v. Garner",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Tennessee v. Garner",
    "case_name_short": "Garner",
    "case_name_full": "TENNESSEE v. GARNER Et Al.",
    "input_case_name": "Tennessee v. Garner",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-03-27",
    "year": 1985,
    "docket": "83-1035",
    "cluster_id": 111397,
    "lead_opinion_id": 9429990,
    "sibling_ids": [
      111397,
      9429990,
      9429991
    ],
    "absolute_url": "/opinion/111397/tennessee-v-garner/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "471 U.S. 1",
      "volume": "471",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 1694",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 1",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4410",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4410",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 195",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "195",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "471 U.S. 1",
        "volume": "471",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 1694",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "1694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 L. Ed. 2d 1",
        "volume": "85",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 195",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "195",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4410",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4410",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "471 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "471 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-3",
      "page": null,
      "quote": "was unarmed\u2014climbed a fence to flee a nighttime house burglary. A Tennessee statute authorized deadly force against any fleeing felon. Garner's father sued under 42 U.S.C. \u00a7 1983. ## Issue Whether the Fourth Amendment permits the use of deadly force to prevent the escape of an apparently unarmed, non-dangerous fleeing felon. ## Rule Deadly force to seize a fleeing suspect is constitutionally constrained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11",
      "page": null,
      "quote": "[a] police officer may not seize an unarmed, nondangerous suspect by shooting him dead.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-11a",
      "page": null,
      "quote": "[w]here the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-03-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Tennessee v. Garner",
    "varies_by_point": false,
    "scope_note": "Clarified (not limited) by Scott v. Harris: Garner is an application of Graham reasonableness, not a rigid on/off switch.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Krystal Wagner, Individually and as Administrator of the Estate of Shane Jensen v. State of Iowa and William L. Spece a/k/a Bill L. Spece",
          "cluster_id": 4844322,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane1_negative"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Graham",
          "cluster_id": 111500,
          "cite": [
            "87 L. Ed. 2d 114",
            "105 S. Ct. 3099",
            "473 U.S. 159",
            "1985 U.S. LEXIS 86",
            "53 U.S.L.W. 4966"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Canton v. Harris",
          "cluster_id": 112209,
          "cite": [
            "103 L. Ed. 2d 412",
            "109 S. Ct. 1197",
            "489 U.S. 378",
            "1989 U.S. LEXIS 1200",
            "57 U.S.L.W. 4270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brosseau v. Haugen",
          "cluster_id": 137736,
          "cite": [
            "160 L. Ed. 2d 583",
            "125 S. Ct. 596",
            "543 U.S. 194",
            "2004 U.S. LEXIS 8275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen King v. Eric Taylor",
          "cluster_id": 808337,
          "cite": [
            "694 F.3d 650",
            "2012 WL 3968371",
            "2012 U.S. App. LEXIS 19109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hamdi v. Rumsfeld",
          "cluster_id": 137001,
          "cite": [
            "159 L. Ed. 2d 578",
            "124 S. Ct. 2633",
            "542 U.S. 507",
            "2004 U.S. LEXIS 4761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 1732,
          "cite": [
            "176 L. Ed. 2d 1",
            "130 S. Ct. 1265",
            "559 U.S. 133",
            "2010 U.S. LEXIS 2201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kim D. Lee v. Luis Ferraro",
          "cluster_id": 75789,
          "cite": [
            "284 F.3d 1188",
            "2002 U.S. App. LEXIS 3438",
            "2002 WL 340670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott L. Matthews v. Leon E. Jones, Sr., Jefferson County Police Department, and Unknown Police Officer, Jefferson County Police Department",
          "cluster_id": 678528,
          "cite": [
            "35 F.3d 1046",
            "1994 U.S. App. LEXIS 25924",
            "1994 WL 509049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gibson v. County of Washoe, Nevada",
          "cluster_id": 777732,
          "cite": [
            "290 F.3d 1175",
            "2002 Cal. Daily Op. Serv. 4392",
            "2002 Daily Journal DAR 5649",
            "2002 U.S. App. LEXIS 9604"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
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
        "journal_ref": "Tennessee v. Garner:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111397 OR 9429990 OR 9429991) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk1Mzc2MDAwMDAwJnM9NDc2OTgyMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111397+OR+9429990+OR+9429991%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(111397 OR 9429990 OR 9429991)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NDMmcz03ODM4NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111397+OR+9429990+OR+9429991%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111397 OR 9429990 OR 9429991)",
        "reviewed": 128,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 128,
        "triage_read": 0,
        "triage_snippet_classified": 128
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111397 OR 9429990 OR 9429991)",
    "indexed_citing_opinions": 2005,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111397,
        "count": 1666,
        "count_source": "search"
      },
      {
        "opinion_id": 9429990,
        "count": 371,
        "count_source": "search"
      },
      {
        "opinion_id": 9429991,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4292,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/tennessee-v-garner.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzcwNjYmcz0xMDYyNjgyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111397+OR+9429990+OR+9429991%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111397,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 326345,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 332062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 341835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 342570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 366970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 420737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1215610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1572528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1800197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1802731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 1868014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2038641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2045742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2130642,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2151033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2169808,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2215247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2380557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 2609526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 3662921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 3895566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111397,
        "cited_id": 4004205,
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
    "date_created": "2026-07-05T21:21:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:24:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:21:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Tennessee v. Garner

```
<opinion type="majority">
<author id="b73-5">Justice White</author>
<p id="Ad">delivered the opinion of the Court.</p>
<p id="b73-6">This case requires us to determine the constitutionality of the use of deadly force to prevent the escape of an apparently unarmed suspected felon. We conclude that such force may not be used unless it is necessary to prevent the escape and the officer has probable cause to believe that the suspect poses a significant threat of death or serious physical injury to the officer or others.</p>
<p id="b73-10">HH</p>
<p id="b73-7">At about 10:45 p. m. on October 3, 1974, Memphis Police Officers Elton Hymon and Leslie Wright were dispatched to answer a “prowler inside call.” Upon arriving at the scene they saw a woman standing on her porch and gesturing toward the adjacent house.<footnotemark>1</footnotemark> She told them she had heard glass breaking and that “they” or “someone” was breaking in next door. While Wright radioed the dispatcher to say that they were on the scene, Hymon went behind the house. He heard a door slam and saw someone run across the backyard. The fleeing suspect, who was appellee-respondent’s decedent, Edward Garner, stopped at a 6-feet-high chain link fence at the edge of the yard. With the aid of a flashlight, Hymon was able to see Garner’s face and hands. He saw no sign of a weapon, and, though not certain, was “reasonably sure” and “figured” that Garner was unarmed. App. 41, 56; Record 219. He thought Garner was 17 or 18 years old and <page-number citation-index="1" label="4">*4</page-number>about 5' 5" <em>or 5' </em>7" tall.<footnotemark>2</footnotemark> While Garner was crouched at the base of the fence, Hymon called out “police, halt” and took a few steps toward him. Garner then began to climb over the fence. Convinced that if Garner made it over the fence he would elude capture,<footnotemark>3</footnotemark> Hymon shot him. The bullet hit Garner in the back of the head. Garner was taken by ambulance to a hospital, where he died on the operating table. Ten dollars and a purse taken from the house were found on his body.<footnotemark>4</footnotemark></p>
<p id="b74-5">In using deadly force to prevent the escape, Hymon was acting under the authority of a Tennessee statute and pursuant to Police Department policy. The statute provides that “[i]f, after notice of the intention to arrest the defendant, he either flee or forcibly resist, the officer may use all the necessary means to effect the arrest.” <span class="citation no-link">Tenn. Code Ann. <page-number citation-index="1" label="5">*5</page-number>§40-7-108</span> (1982).<footnotemark>5</footnotemark> The Department policy was slightly more restrictive than the statute, but still allowed the use of deadly force in cases of burglary. App. 140-144. The incident was reviewed by the Memphis Police Firearm’s Review Board and presented to a grand jury. Neither took any action. <span class="citation no-link"><em>Id., </em>at 57</span>.</p>
<p id="b75-5">Garner’s father then brought this action in the Federal District Court for the Western District of Tennessee, seeking damages under <span class="citation no-link">42 U. S. C. § 1983</span> for asserted violations of Garner’s constitutional rights. The complaint alleged that the shooting violated the Fourth, Fifth, Sixth, Eighth, and Fourteenth Amendments of the United States Constitution. It named as defendants Officer Hymon, the Police Department, its Director, and the Mayor and city of Memphis. After a 3-day bench trial, the District Court entered judgment for all defendants. It dismissed the claims against the Mayor and the Director for lack of evidence. It then concluded that Hymon’s actions were authorized by the Tennessee statute, which in turn was constitutional. Hymon had employed the only reasonable and practicable means of preventing Garner’s escape. Garner had “recklessly and heedlessly attempted to vault over the fence to escape, thereby assuming the risk of being fired upon.” App. to Pet. for Cert. A10.</p>
<p id="b75-6">The Court of Appeals for the Sixth Circuit affirmed with regard to Hymon, finding that he had acted in good-faith reliance on the Tennessee statute and was therefore within the scope of his qualified immunity. <span class="citation multiple-matches"><a href="/c/F.%202d/600/52/">600 F. 2d 52</a></span> (1979). It remanded for reconsideration of the possible liability of the city, however, in light of <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), which had come down after the District Court’s decision. The District Court was <page-number citation-index="1" label="6">*6</page-number>directed to consider whether a city enjoyed a qualified immunity, whether the use of deadly force and hollow point bullets in these circumstances was constitutional, and whether any unconstitutional municipal conduct flowed from a “policy or custom” as required for liability under <em>Monell. </em>600 F. 2d, at 54-55.</p>
<p id="b76-5">The District Court concluded that <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>did not affect its decision. While acknowledging some doubt as to the possible immunity of the city, it found that the statute, and Hymon’s actions, were constitutional. Given this conclusion, it declined to consider the “policy or custom” question. App. to Pet. for Cert. A37-A39.</p>
<p id="b76-6">The Court of Appeals reversed and remanded. <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d 240</a></span> (1983). It reasoned that the killing of a fleeing suspect is a “seizure” under the Fourth Amendment,<footnotemark>6</footnotemark> and is therefore constitutional only if “reasonable.” The Tennessee statute failed as applied to this case because it did not adequately limit the use of deadly force by distinguishing between felonies of different magnitudes — “the facts, as found, did not justify the use of deadly force under the Fourth Amendment.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department"><em>Id., </em>at 246</a></span>. Officers cannot resort to deadly force unless they “have probable cause ... to believe that the suspect [has committed a felony and] poses a threat to the safety of the officers or a danger to the community if left at large.” <em><span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">Ibid.</a></span></em><footnotemark><em>7</em></footnotemark></p>
<p id="b77-4"><page-number citation-index="1" label="7">*7</page-number>The State of Tennessee, which had intervened to defend the statute, see <span class="citation no-link">28 U. S. C. § 2403</span>(b), appealed to this Court. The city filed a petition for certiorari. We noted probable jurisdiction in the appeal and granted the petition. <span class="citation multiple-matches"><a href="/c/U.%20S./465/1098/">465 U. S. 1098</a></span> (1984).</p>
<p id="b77-5">II</p>
<p id="b77-6">Whenever an officer restrains the freedom of a person to walk away, he has seized that person. <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). While it is not always clear just when minimal police interference becomes a seizure, see <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), there can be no question that apprehension by the use of deadly force is a seizure subject to the reasonableness requirement of the Fourth Amendment.</p>
<p id="b77-7">A</p>
<p id="b77-8">A police officer may arrest a person if he has probable cause to believe that person committed a crime. <em>E. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976). Petitioners and appellant argue that if this requirement is satisfied the Fourth Amendment has nothing to say about <em>how </em>that seizure is made. This submission ignores the many cases in which this Court, by balancing the extent of the intrusion against the need for it, has examined the reasonableness of <page-number citation-index="1" label="8">*8</page-number>the manner in which a search or seizure is conducted. To determine the constitutionality of a seizure “[w]e must balance the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983); see <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 555</a></span> (1976). We have described “the balancing of competing interests” as “the key principle of the Fourth Amendment.” <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#700" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 700, n. 12</a></span> (1981). See also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967). Because one of the factors is the extent of the intrusion, it is plain that reasonableness depends on not only when a seizure is made, but also how it is carried out. <em>United States </em>v. <em>Ortiz, </em><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 895</a></span> (1975); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 28-29</a></span> (1968).</p>
<p id="b78-5">Applying these principles to particular facts, the Court has held that governmental interests did not support a lengthy detention of luggage, <em>United States </em>v. <em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place, supra,</a></span> </em>an airport seizure not “carefully tailored to its underlying justification,” <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#500" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 500</a></span> (1983) (plurality-opinion), surgery under general anesthesia to obtain evidence, <em>Winston </em>v. <em>Lee, </em><span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985), or detention for fingerprinting without probable cause, <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <em>Hayes </em>v. <em>Florida, </em><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">470 U. S. 811</a></span> (1985). On the other hand, under the same approach it has upheld the taking of fingernail scrapings from a suspect, <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291</a></span> (1973), an unannounced entry into a home to prevent the destruction of evidence, <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), administrative housing inspections without probable cause to believe that a code violation will be found, <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>and a blood test of a drunken-driving suspect, <em>Schmerber </em>v. <em>California, 384 </em>U. S. 757 (1966). In each of these cases, the question was whether <page-number citation-index="1" label="9">*9</page-number>the totality of the circumstances justified a particular sort of search or seizure.</p>
<p id="b79-5">B</p>
<p id="b79-6">The same balancing process applied in the cases cited above demonstrates that, notwithstanding probable cause to seize a suspect, an officer may not always do so by killing him. The intrusiveness of a seizure by means of deadly force is unmatched. The suspect’s fundamental interest in his own life need not be elaborated upon. The use of deadly force also frustrates the interest of the individual, and of society, in judicial determination of guilt and punishment. Against these interests are ranged governmental interests in effective law enforcement.<footnotemark>8</footnotemark> It is argued that overall violence will be reduced by encouraging the peaceful submission of suspects who know that they may be shot if they flee. Effectiveness in making arrests requires the resort to deadly <page-number citation-index="1" label="10">*10</page-number>force, or at least the meaningful threat thereof. “Being able to arrest such individuals is a condition precedent to the state’s entire system of law enforcement.” Brief for Petitioners 14.</p>
<p id="b80-5">Without in any way disparaging the importance of these goals, we are not convinced that the use of deadly force is a sufficiently productive means of accomplishing them to justify the killing of nonviolent suspects. Cf. <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span>. The use of deadly force is a self-defeating way of apprehending a suspect and so setting the criminal justice mechanism in motion. If successful, it guarantees that that mechanism will not be set in motion. And while the meaningful threat of deadly force might be thought to lead to the arrest of more live suspects by discouraging escape attempts,<footnotemark>9</footnotemark> the presently available evidence does not support this thesis.<footnotemark>10</footnotemark> The fact is that a majority of police de<page-number citation-index="1" label="11">*11</page-number>partments in this country have forbidden the use of deadly force against nonviolent suspects. See <em>infra, </em>at 18-19. If those charged with the enforcement of the criminal law have abjured the use of deadly force in arresting nondangerous felons, there is a substantial basis for doubting that the use of such force is an essential attribute of the arrest power in all felony cases. See <em>Schumann </em>v. <em>McGinn, </em><span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#472" aria-description="Citation for case: Schumann v. McGinn">307 Minn. 446, 472</a></span>, <span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#540" aria-description="Citation for case: Schumann v. McGinn">240 N. W. 2d 525, 540</a></span> (1976) (Rogosheske, J., dissenting in part). Petitioners and appellant have not persuaded us that shooting nondangerous fleeing suspects is so vital as to outweigh the suspect’s interest in his own life.</p>
<p id="b81-5">The use of deadly force to prevent the escape of all felony suspects, whatever the circumstances, is constitutionally unreasonable. It is not better that all felony suspects die than that they escape. Where the suspect poses no immediate threat to the officer and no threat to others, the harm resulting from failing to apprehend him does not justify the use of deadly force to do so. It is no doubt unfortunate when a suspect who is in sight escapes, but the fact that the police arrive a little late or are a little slower afoot does not always justify killing the suspect. A police officer may not seize an unarmed, nondangerous suspect by shooting him dead. The Tennessee statute is unconstitutional insofar as it authorizes the use of deadly force against such fleeing suspects.</p>
<p id="b81-6">It is not, however, unconstitutional on its face. Where the officer has probable cause to believe that the suspect poses a threat of serious physical harm, either to the officer or to others, it is not constitutionally unreasonable to prevent escape by using deadly force. Thus, if the suspect threatens the officer with a weapon or there is probable cause to believe that he has committed a crime involving the infliction or threatened infliction of serious physical harm, deadly force may be used if necessary to prevent escape, and if, where <page-number citation-index="1" label="12">*12</page-number>feasible, some warning has been given. As applied in such circumstances, the Tennessee statute would pass constitutional muster.</p>
<p id="b82-5">Ill</p>
<p id="b82-6">A</p>
<p id="b82-7">It is insisted that the Fourth Amendment must be construed in light of the common-law rule, which allowed the use of whatever force was necessary to effect the arrest of a fleeing felon, though not a misdemeanant. As stated in Hale’s posthumously published Pleas of the Crown:</p>
<blockquote id="b82-8">“[I]f persons that are pursued by these officers for felony or the just suspicion thereof . . . shall not yield themselves to these officers, but shall either resist or fly before they are apprehended or being apprehended shall rescue themselves and resist or fly, so that they cannot be otherwise apprehended, and are upon necessity slain therein, because they cannot be otherwise taken, it is no felony.” 2 M. Hale, Historia Placitorum Coronae 85 (1736).</blockquote>
<p id="b82-9">See also 4 W. Blackstone, Commentaries *289. Most American jurisdictions also imposed a flat prohibition against the use of deadly force to stop a fleeing misdemeanant, coupled with a general privilege <em>to </em>use such force to stop a fleeing felon. <em>E. g., Holloway </em>v. <em>Moser, </em><span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/" aria-description="Citation for case: Holloway v. . Moser">193 N. C. 185</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/" aria-description="Citation for case: Holloway v. . Moser">136 S. E. 375</a></span> (1927); <em>State </em>v. <em>Smith, </em><span class="citation" data-id="7111483"><a href="/opinion/7200219/state-v-smith/#535" aria-description="Citation for case: State v. Smith">127 Iowa 534, 535</a></span>, <span class="citation no-link">103 N. W. 944</span>, 945 (1905); <em>Reneau </em>v. <em>State, </em><span class="citation" data-id="8296393"><a href="/opinion/8328603/reneau-v-state/" aria-description="Citation for case: Reneau v. State">70 Tenn. 720</a></span> (1879); <em>Brooks </em>v. <em>Commonwealth, </em><span class="citation" data-id="6233531"><a href="/opinion/6364699/brooks-v-commonwealth/" aria-description="Citation for case: Brooks v. Commonwealth">61 Pa. 352</a></span> (1869); <em>Roberts </em>v. <em>State, </em><span class="citation" data-id="7998579"><a href="/opinion/8042047/roberts-v-state/" aria-description="Citation for case: Roberts v. State">14 Mo. 138</a></span> (1851); see generally R. Perkins &amp; R. Boyce, Criminal Law 1098-1102 (3d ed. 1982); Day, Shooting the Fleeing Felon: State of the Law, <span class="citation no-link">14 Crim. L. Bull. 285</span>, 286-287 (1978); Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 807-816 (1924). But see <em>Storey </em>v. <em>State, </em><span class="citation" data-id="6511386"><a href="/opinion/6634820/storey-v-state/" aria-description="Citation for case: Storey v. State">71 Ala. 329</a></span> (1882); <em>State </em>v. <em>Bryant, </em><span class="citation" data-id="3649744"><a href="/opinion/3903667/state-v-bryant/#328" aria-description="Citation for case: State v. . Bryant">65 N. C. 327, 328</a></span> (1871); <em>Caldwell </em>v. <em>State, </em><span class="citation" data-id="4892115"><a href="/opinion/5076532/caldwell-v-state/" aria-description="Citation for case: Caldwell v. State">41 Tex. 86</a></span> (1874).</p>
<p id="b83-4"><page-number citation-index="1" label="13">*13</page-number>The State and city argue that because this was the prevailing rule at the time of the adoption of the Fourth Amendment and for some time thereafter, and is still in force in some States, use of deadly force against a fleeing felon must be “reasonable.” It is true that this Court has often looked to the common law in evaluating the reasonableness, for Fourth Amendment purposes, of police activity. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-419</a></span> (1976); <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 111, 114</a></span> (1975); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149-153</a></span> (1925). On the other hand, it “has not simply frozen into constitutional law those law enforcement practices that existed at the time of the Fourth Amendment’s passage.” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 591, n. 33</a></span> (1980). Because of sweeping change in the legal and technological context, reliance on the common-law rule in this case would be a mistaken literalism that ignores the purposes of a historical inquiry.</p>
<p id="b83-5">B</p>
<p id="b83-6">It has been pointed out many times that the common-law rule is best understood in light of the fact that it arose at a time when virtually all felonies were punishable by death.<footnotemark>11</footnotemark> “Though effected without the protections and formalities of an orderly trial and conviction, the killing of a resisting or <page-number citation-index="1" label="14">*14</page-number>fleeing felon resulted in no greater consequences than those authorized for punishment of the felony of which the individual was charged or suspected.” American Law Institute, Model Penal Code §3.07, Comment 3, p. 56 (Tentative Draft No. 8, 1958) (hereinafter Model Penal Code Comment). Courts have also justified the common-law rule by emphasizing the relative dangerousness of felons. See, <em>e. g., Schumann </em>v. <em>McGinn, </em><span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#458" aria-description="Citation for case: Schumann v. McGinn">307 Minn., at 458</a></span>, <span class="citation" data-id="9738314"><a href="/opinion/2215247/schumann-v-mcginn/#533" aria-description="Citation for case: Schumann v. McGinn">240 N. W. 2d, at 533</a></span>; <em>Holloway </em>v. <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#187" aria-description="Citation for case: Holloway v. . Moser"><em>Moser, supra, </em>at 187</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#376" aria-description="Citation for case: Holloway v. . Moser">136 S. E., at 376</a></span> (1927).</p>
<p id="b84-5">Neither of these justifications makes sense today. Almost all crimes formerly punishable by death no longer are or can be. See, <em>e. g., Enmund </em>v. <em>Florida, </em><span class="citation" data-id="9428940"><a href="/opinion/110795/enmund-v-florida/" aria-description="Citation for case: Enmund v. Florida">458 U. S. 782</a></span> (1982); <em>Coker </em>v. <em>Georgia, </em><span class="citation" data-id="9426971"><a href="/opinion/109731/coker-v-georgia/" aria-description="Citation for case: Coker v. Georgia">433 U. S. 584</a></span> (1977). And while in earlier times “the gulf between the felonies and the minor offences was broad and deep,” 2 Pollock &amp; Maitland 467, n. 3; <em>Carroll </em>v. <em>United States, supra, </em>at 158, today the distinction is minor and often arbitrary. Many crimes classified as misdemeanors, or nonexistent, at common law are now felonies. Wilgus, 22 Mich. L. Rev., at 572-573. These changes have undermined the concept, which was questionable to begin with, that use of deadly force against a fleeing felon is merely a speedier execution of someone who has already forfeited his life. They have also made the assumption that a “felon” is more dangerous than a misdemeanant untenable. Indeed, numerous misdemeanors involve conduct more dangerous than many felonies.<footnotemark>12</footnotemark></p>
<p id="b84-6">There is an additional reason why the common-law rule cannot be directly translated to the present day. The common-law rule developed at a time when weapons were rudimentary. Deadly force could be inflicted almost solely in a hand-to-hand struggle during which, necessarily, the safety <page-number citation-index="1" label="15">*15</page-number>of the arresting officer was at risk. Handguns were not carried by police officers until the latter half of the last century. L. Kennett &amp; J. Anderson, The Gun in America 150-151 (1975). Only then did it become possible to use deadly force from a distance as a means of apprehension. As a practical matter, the use of deadly force under the standard articulation of the common-law rule has an altogether different meaning — and harsher consequences — now than in past centuries. See Wechsler &amp; Michael, A Rationale for the Law of Homicide: I, <span class="citation no-link">37 Colum. L. Rev. 701</span>, 741 (1937).<footnotemark>13</footnotemark></p>
<p id="b85-5">One other aspect of the common-law rule bears emphasis. It forbids the use of deadly force to apprehend a misde-meanant, condemning such action as disproportionately severe. See <em>Holloway </em>v. <em>Moser, </em><span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#187" aria-description="Citation for case: Holloway v. . Moser">193 N. C., at 187</a></span>, <span class="citation" data-id="3662921"><a href="/opinion/3916545/holloway-v-moser/#376" aria-description="Citation for case: Holloway v. . Moser">136 S. E., at 376</a></span>; <em>State </em>v. <em>Smith, </em><span class="citation" data-id="7111483"><a href="/opinion/7200219/state-v-smith/#535" aria-description="Citation for case: State v. Smith">127 Iowa, at 535</a></span>, 103 N. W., at 945. See generally Annot., 83 A. L. R. 3d 238 (1978).</p>
<p id="b85-6">In short, though the common-law pedigree of Tennessee’s rule is pure on its face, changes in the legal and technological context mean the rule is distorted almost beyond recognition when literally applied.</p>
<p id="b85-7">C</p>
<p id="b85-8">In evaluating the reasonableness of police procedures under the Fourth Amendment, we have also looked to pre<page-number citation-index="1" label="16">*16</page-number>vailing rules in individual jurisdictions. See, <em>e. g., United States </em>v. <em>Watson, </em><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson">423 U. S., at 421-422</a></span>. The rules in the States are varied. See generally Comment, <span class="citation no-link">18 Ga. L. Rev. 137</span>, 140-144 (1983). Some 19 States have codified the common-law rule,<footnotemark>14</footnotemark> though in two of these the courts have significantly limited the statute.<footnotemark>15</footnotemark> Four States, though without a relevant statute, apparently retain the common-law rule.<footnotemark>16</footnotemark> Two States have adopted the Model Penal Code’s <page-number citation-index="1" label="17">*17</page-number>provision verbatim.<footnotemark>17</footnotemark> Eighteen others allow, in slightly varying language, the use of deadly force only if the suspect has committed a felony involving the use or threat of physical or deadly force, or is escaping with a deadly weapon, or is likely to endanger life or inflict serious physical injury if not arrested.<footnotemark>18</footnotemark> Louisiana and Vermont, though without statutes or case law on point, do forbid the use of deadly force to prevent any but violent felonies.<footnotemark>19</footnotemark> The remaining States either have no relevant statute or case law, or have positions that are unclear.<footnotemark>20</footnotemark></p>
<p id="b88-4"><page-number citation-index="1" label="18">*18</page-number>It cannot be said that there is a constant or overwhelming trend away from the common-law rule. In recent years, some States have reviewed their laws and expressly rejected abandonment of the common-law rule.<footnotemark>21</footnotemark> Nonetheless, the long-term movement has been away from the rule that deadly force may be used against any fleeing felon, and that remains the rule in less than half the States.</p>
<p id="b88-5">This trend is more evident and impressive when viewed in light of the policies adopted by the police departments themselves. Overwhelmingly, these are more restrictive than the common-law rule. C. Milton, J. Halleck, J. Lardner, &amp; G. Abrecht, Police Use of Deadly Force 45-46 (1977). The Federal Bureau of Investigation and the New York City Police Department, for example, both forbid the use of firearms except when necessary to prevent death or grievous bodily harm. <span class="citation no-link"><em>Id., </em>at 40-41</span>; App. 88. For accreditation by the Commission on Accreditation for Law Enforcement Agencies, a department must restrict the use of deadly force to situations where “the officer reasonably believes that the action is in defense of human life ... or in defense of any person in immediate danger of serious physical injury.” Commission on Accreditation for Law Enforcement Agencies, Inc., Standards for Law Enforcement Agencies 1-2 (1983) (italics deleted). A 1974 study reported that the police department regulations in a majority of the large cities of the United States allowed the firing of a weapon only when a <page-number citation-index="1" label="19">*19</page-number>felon presented a threat of death or serious bodily harm. Boston Police Department, Planning &amp; Research Division, The Use of Deadly Force by Boston Police Personnel (1974), cited in <em>Mattis </em>v. <em>Schnarr, </em><span class="citation" data-id="341835"><a href="/opinion/341835/robert-dean-mattis-md-v-richard-r-schnarr-and-robert-marek-v-john-c/#1016" aria-description="Citation for case: Robert Dean Mattis, M.D. v. Richard R. Schnarr and Robert...">547 F. 2d 1007, 1016, n. 19</a></span> (CA8 1976), vacated as moot <em>sub nom. Ashcroft </em>v. Mattis, <span class="citation" data-id="109657"><a href="/opinion/109657/ashcroft-v-mattis/" aria-description="Citation for case: Ashcroft v. Mattis">431 U. S. 171</a></span> (1977). Overall, only 7.5% of departmental and municipal policies explicitly permit the use of deadly force against any felon; 86.8% explicitly do not. K. Matulia, A Balance of Forces: A Report of the International Association of Chiefs of Police 161 (1982) (table). See also Record 1108-1368 (written policies of 44 departments). See generally W. Geller &amp; K. Karales, Split-Second Decisions 33-42 (1981); Brief for Police Foundation et al. as <em>Amici Curiae. </em>In light of the rules adopted by those who must actually administer them, the older and fading common-law view is a dubious indicium of the constitutionality of the Tennessee statute now before us.</p>
<p id="b89-5">D</p>
<p id="b89-6">Actual departmental policies are important for an additional reason. We would hesitate to declare a police practice of long standing “unreasonable” if doing so would severely hamper effective law enforcement. But the indications are to the contrary. There has been no suggestion that crime has worsened in any way in jurisdictions that have adopted, by legislation or departmental policy, rules similar to that announced today. <em>Amici </em>note that “[a]fter extensive research and consideration, [they] have concluded that laws permitting police officers to use deadly force to apprehend unarmed, non-violent fleeing felony suspects actually do not protect citizens or law enforcement officers, do not deter crime or alleviate problems caused by crime, and do not improve the crime-fighting ability of law enforcement agencies.” <em>Id., </em>at 11. The submission is that the obvious state interests in apprehension are not sufficiently served to warrant the use of lethal weapons against all fleeing felons. See <em>supra, </em>at 10-11, and n. 10.</p>
<p id="b90-4"><page-number citation-index="1" label="20">*20</page-number>Nor do we agree with petitioners and appellant that the rule we have adopted requires the police to make impossible, split-second evaluations of unknowable facts. See Brief for Petitioners 25; Brief for Appellant 11. We do not deny the practical difficulties of attempting to assess the suspect’s dangerousness. However, similarly difficult judgments must be made by the police in equally uncertain circumstances. See, <em>e. g., Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20, 27</a></span>. Nor is there any indication that in States that allow the use of deadly force only against dangerous suspects, see nn. 15, 17-19, <em>supra, </em>the standard has been difficult to apply or has led to a rash of litigation involving inappropriate second-guessing of police officers’ split-second decisions. Moreover, the highly technical felony/misdemeanor distinction is equally, if not more, difficult to apply in the field. An officer is in no position to know, for example, the precise value of property stolen, or whether the crime was a first or second offense. Finally, as noted above, this claim must be viewed with suspicion in light of the similar self-imposed limitations of so many police departments.</p>
<p id="b90-5">IV</p>
<p id="b90-6">The District Court concluded that Hymon was justified in shooting Garner because state law allows, and the Federal Constitution does not forbid, the use of deadly force to prevent the escape of a fleeing felony suspect if no alternative means of apprehension is available. See App. to Pet. for Cert. A9-A11, A38. This conclusion made a determination of Garner’s apparent dangerousness unnecessary. The court did find, however, that Garner appeared to be unarmed, though Hymon could not be certain that was the case. <em>Id., </em>at A4, A23. See also App. 41, 56; Record 219. Restated in Fourth Amendment terms, this means Hymon had no articu-lable basis to think Garner was armed.</p>
<p id="b90-7">In reversing, the Court of Appeals accepted the District Court’s factual conclusions and held that “the facts, as found, did not justify the use of deadly force.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 246</a></span>. <page-number citation-index="1" label="21">*21</page-number>We agree. Officer Hymon could not reasonably have believed that Garner — young, slight, and unarmed — posed any threat. Indeed, Hymon never attempted to justify his actions on any basis other than the need to prevent an escape. The District Court stated in passing that “[t]he facts of this case did not indicate to Officer Hymon that Garner was ‘non-danger ous.’ ” App. to Pet. for Cert. A34. This conclusion is not explained, and seems to be based solely on the fact that Garner had broken into a house at night. However, the fact that Garner was a suspected burglar could not, without regard to the other circumstances, automatically justify the use of deadly force. Hymon did not have probable cause to believe that Garner, whom he correctly believed to be unarmed, posed any physical danger to himself or others.</p>
<p id="b91-5">The dissent argues that the shooting was justified by the fact that Officer Hymon had probable cause to believe that Garner had committed a nighttime burglary. <em>Post, </em>at 29, 32. While we agree that burglary is a serious crime, we cannot agree that it is so dangerous as automatically to justify the use of deadly force. The FBI classifies burglary as a “property” rather than a “violent” crime. See Federal Bureau of Investigation, Uniform Crime Reports, Crime in the United States 1 (1984).<footnotemark>22</footnotemark> Although the armed burglar would present a different situation, the fact that an unarmed suspect has broken into a dwelling at night does not automatically mean he is physically dangerous. This case demonstrates as much. See also <em>Solem </em>v. <em>Helm, </em><span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#296" aria-description="Citation for case: Solem v. Helm">463 U. S. 277, 296-297</a></span>, and nn. 22-23 (1983). In fact, the available statistics demonstrate that burglaries only rarely involve physical violence. During the 10-year period from 1973-1982, only 3.8% of all burglaries involved violent crime. Bureau of Justice Statistics, House<page-number citation-index="1" label="22">*22</page-number>hold Burglary 4 (1985).<footnotemark>23</footnotemark> See also T. Reppetto, Residential Crime 17, 105 (1974); Conklin &amp; Bittner, Burglary in a Suburb, 11 Criminology 208, 214 (1973).</p>
<p id="b92-5">V</p>
<p id="b92-6">We wish to make clear what our holding means in the context of this case. The complaint has been dismissed as to all the individual defendants. The State is a party only by virtue of <span class="citation no-link">28 U. S. C. § 2403</span>(b) and is not subject to liability. The possible liability of the remaining defendants — the Police Department and the city of Memphis — hinges on <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), and is left for remand. We hold that the statute is invalid insofar as it purported to give Hymon the authority to act as he did. As for the policy of the Police Department, the absence of any discussion of this issue by the courts below, and the uncertain state of the record, preclude any consideration of its validity.</p>
<p id="b92-7">The judgment of the Court of Appeals is affirmed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b92-8">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b73-9"> The owner of the house testified that no lights were on in the house, but that a back door light was on. Record 160. Officer Hymon, though uncertain, stated in his deposition that there were lights on in the house. <em>Id., </em>at 209.</p>
</footnote>
<footnote label="2">
<p id="b74-6"> In fact, Garner, an eighth-grader, was 15. He was 5' 4" tall and weighed somewhere around 100 or 110 pounds. App. to Pet. for Cert. A5.</p>
</footnote>
<footnote label="3">
<p id="b74-7"> When asked at trial why he fired, Hymon stated:</p>
<blockquote id="b74-8">“Well, first of all it was apparent to me from the little bit that I knew about the area at the time that he was going to get away because, number 1, I couldn’t get to him. My partner then couldn’t find where he was because, you know, he was late coming around. He didn’t know where I was talking about. I couldn’t get to him because of the fence here, I couldn’t have jumped this fence and come up, consequently jumped this fence and caught him before he got away because he was already up on the fence, just one leap and he was already over the fence, and so there is no way that I could have caught him.” App. 52.</blockquote>
<p id="b74-9">He also stated that the area beyond the fence was dark, that he could not have gotten over the fence easily because he was carrying a lot of equipment and wearing heavy boots, and that Garner, being younger and more energetic, could have outrun him. <em>Id., </em>at 53-54.</p>
</footnote>
<footnote label="4">
<p id="b74-10"> Garner had rummaged through one room in the house, in which, in the words of the owner, “[a]ll the stuff was out on the floors, all the drawers was pulled out, and stuff was scattered all over.” <em>Id., </em>at 34. The owner testified that his valuables were untouched but that, in addition to the purse and the 10 dollars, one of his wife’s rings was missing. The ring was not recovered. <em>Id., </em>at 34-35.</p>
</footnote>
<footnote label="5">
<p id="b75-7"> Although the statute does not say so explicitly, Tennessee law forbids the use of deadly force in the arrest of a misdemeanant. See <em>Johnson </em>v. <em>State, </em><span class="citation" data-id="3895566"><a href="/opinion/4132874/johnson-v-state/" aria-description="Citation for case: Johnson v. State">173 Tenn. 134</a></span>, <span class="citation" data-id="3895566"><a href="/opinion/4132874/johnson-v-state/" aria-description="Citation for case: Johnson v. State">114 S. W. 2d 819</a></span> (1938).</p>
</footnote>
<footnote label="6">
<p id="b76-7"> “The right of the people to be secure in their persons . . . against unreasonable searches and seizures, shall not be violated . . . .” U. S. Const., Arndt. 4.</p>
</footnote>
<footnote label="7">
<p id="b76-8"> The Court of Appeals concluded that the rule set out in the Model Penal Code “accurately states Fourth Amendment limitations on the use of deadly force against fleeing felons.” <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#247" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 247</a></span>. The relevant portion of the Model Penal Code provides:</p>
<blockquote id="b76-9">“The use of deadly force is not justifiable . . . unless (i) the arrest is for a felony; and (ii) the person effecting the arrest is authorized to act as a peace officer or is assisting a person whom he believes to be authorized to act as a peace officer; and (iii) the actor believes that the force employed creates no substantial risk of injury to innocent persons; and (iv) the actor believes <page-number citation-index="1" label="7">*7</page-number>that (1) the crime for which the arrest is made involved conduct including the use or threatened use of deadly force; or (2) there is a substantial risk that the person to be arrested will cause death or serious bodily harm if his apprehension is delayed.” American Law Institute, Model Penal Code §3.07(2)(b) (Proposed Official Draft 1962).</blockquote>
<p id="b77-10">The court also found that “[a]n analysis of the facts of this case under the Due Process Clause” required the same result, because the statute was not narrowly drawn to further a compelling state interest. <span class="citation" data-id="420737"><a href="/opinion/420737/cleamtee-garner-v-memphis-police-department/#246" aria-description="Citation for case: Cleamtee Garner v. Memphis Police Department">710 F. 2d, at 246-247</a></span>. The court considered the generalized interest in effective law enforcement sufficiently compelling only when the the suspect is dangerous. Finally, the court held, relying on <em>Owen </em>v. <em>City of Independence, </em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">445 U. S. 622</a></span> (1980), that the city was not immune.</p>
</footnote>
<footnote label="8">
<p id="b79-7"> The dissent emphasizes that subsequent investigation cannot replace immediate apprehension. We recognize that this is so, see n. 13, <em>infra; </em>indeed, that is the reason why there is any dispute. If subsequent arrest were assured, no one would argue that use of deadly force was justified. Thus, we proceed on the assumption that subsequent arrest is not likely. Nonetheless, it should be remembered that failure to apprehend at the scene does not necessarily mean that the suspect will never be caught.</p>
<p id="b79-8">In lamenting the inadequacy of later investigation, the dissent relies on the report of the President’s Commission on Law Enforcement and Administration of Justice. It is worth noting that, notwithstanding its awareness of this problem, the Commission itself proposed a policy for use of deadly force arguably even more stringent than the formulation we adopt today. See President’s Commission on Law Enforcement and Administration of Justice, Task Force Report: The Police 189 (1967). The Commission proposed that deadly force be used only to apprehend “perpetrators who, in the course of their crime threatened the use of deadly force, or if the officer believes there is a substantial risk that the person whose arrest is sought will cause death or serious bodily harm if his apprehension is delayed.” In addition, the officer would have “to know, as a virtual certainty, that the suspect committed an offense for which the use of deadly force is permissible.” <em><span class="citation" data-id="9427858"><a href="/opinion/110236/owen-v-city-of-independence/" aria-description="Citation for case: Owen v. City of Independence">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b80-6"> We note that the usual manner of deterring illegal conduct — through punishment — has been largely ignored in connection with flight from arrest. Arkansas, for example, specifically excepts flight from arrest from the offense of “obstruction of governmental operations.” The commentary notes that this “reflects the basic policy judgment that, absent the use of force or violence, a mere attempt to avoid apprehension by a law enforcement officer does not give rise to an independent offense.” Ark. Stat. Ann. § 41-2802(3)(a) (1977) and commentary. In the few States that do outlaw flight from an arresting officer, the crime is only a misdemeanor. See, <em>e. </em>g., <span class="citation no-link">Ind. Code § 35-44-3-3</span> (1982). Even forceful resistance, though generally a separate offense, is classified as a misdemeanor. <em>E. g., </em>Ill. Rev. Stat., ch. 38, ¶31-1 (1984); <span class="citation no-link">Mont. Code Ann. §45-7-301</span> (1984); N. H. Rev. Stat. Ann. §642:2 (Supp. 1983); Ore. Rev. Stat. §162.315 (1983).</p>
<p id="b80-7">This lenient approach does avoid the anomaly of automatically transforming every fleeing misdemeanant into a fleeing felon — subject, under the common-law rule, to apprehension by deadly force — solely by virtue of his flight. However, it is in real tension with the harsh consequences of flight in cases where deadly force is employed. For example, Tennessee does not outlaw fleeing from arrest. The Memphis City Code does, §22-34.1 (Supp. 17, 1971), subjecting the offender to a maximum fine of $50, § 1-8 (1967). Thus, Garner’s attempted escape subjected him to (a) a $50 fine, and (b) being shot.</p>
</footnote>
<footnote label="10">
<p id="b80-8"> See Sherman, Reducing Police Gun Use, in Control in the Police Organization 98, 120-123 (M. Punch ed. 1983); Fyfe, Observations on Police <page-number citation-index="1" label="11">*11</page-number>Deadly Force, 27 Crime &amp; Delinquency 376, 378-381 (1981); W. Geller &amp; K. Karales, Split-Second Decisions 67 (1981); App. 84 (affidavit of William Bracey, Chief of Patrol, New York City Police Department). See generally Brief for Police Foundation et al. as <em>Amici Curiae.</em></p>
</footnote>
<footnote label="11">
<p id="b83-7"> The roots of the concept of a “felony” lie not in capital punishment but in forfeiture. 2 F. Pollock &amp; F. Maitland, The History of English Law 465 (2d ed. 1909) (hereinafter Pollock &amp; Maitland). Not all felonies were always punishable by death. See <em>id., </em>at 466-467, n. 3. Nonetheless, the link was profound. Blackstone was able to write: “The idea of felony is indeed so generally connected with that of capital punishment, that we find it hard to separate them; and to this usage the interpretations of the law do now conform. And therefore if a statute makes any new offence felony, the law implies that is shall be punished with death, <em>viz. </em>by hanging, as well as with forfeiture . . . .” 4 W. Blackstone, Commentaries *98. See also R. Perkins &amp; R. Boyce, Criminal Law 14-15 (3d ed. 1982); 2 Pollock &amp; Maitland 511.</p>
</footnote>
<footnote label="12">
<p id="b84-7"> White-collar crime, for example, poses a less significant physical threat than, say, drunken driving. See <em>Welsh </em>v. <em>Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984); <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#755" aria-description="Citation for case: Welsh v. Wisconsin"><em>id., </em>at 755</a></span> (Blackmun, J., concurring). See Model Penal Code Comment, at 57.</p>
</footnote>
<footnote label="13">
<p id="b85-9"> It has been argued that sophisticated techniques of apprehension and increased communication between the police in different jurisdictions have made it more likely that an escapee will be caught than was once the case, and that this change has also reduced the “reasonableness” of the use of deadly force to prevent escape. <em>E. g., </em>Sherman, Execution Without Trial: Police Homicide and the Constitution, <span class="citation no-link">33 Vand. L. Rev. 71</span>, 76 (1980). We are unaware of any data that would permit sensible evaluation of this claim. Current arrest rates are sufficiently low, however, that we have some doubt whether in past centuries the failure to arrest at the scene meant that the police had missed their only chance in a way that is not presently the case. In 1983, 21% of the offenses in the Federal Bureau of Investigation crime index were cleared by arrest. Federal Bureau of Investigation, Uniform Crime Reports, Crime in the United States 159 (1984). The clearance rate for burglary was 15%. <em><span class="citation no-link">Ibid.</span></em></p>
</footnote>
<footnote label="14">
<p id="b86-5"> Ala. Code § 13A-3-27 (1982); Ark. Stat. Ann. § 41-510 (1977); Cal. Penal Code Ann. § 196 (West 1970); Conn. Gen. Stat. § 53a-22 (1972); <span class="citation no-link">Fla. Stat. § 776.05</span> (1983); <span class="citation no-link">Idaho Code § 19-610</span> (1979); <span class="citation no-link">Ind. Code § 35-41-3-3</span> (1982); <span class="citation no-link">Kan. Stat. Ann. § 21-3215</span> (1981); <span class="citation no-link">Miss. Code Ann. § 97-3-15</span>(d) (Supp. 1984); <span class="citation no-link">Mo. Rev. Stat. § 563.046</span> (1979); <span class="citation no-link">Nev. Rev. Stat. § 200.140</span> (1983); N. M. Stat. Ann. § 30-2-6 (1984); Okla. Stat., Tit. 21, §732 (1981); R. I. Gen. Laws § 12-7-9 (1981); S. D. Codified Laws §§ 22-16-32, 22-16-33 (1979); <em>Term. </em>Code Ann. § 40-7-108 (1982); Wash. Rev. Code § 9A. 16.040(3) (1977). Oregon limits use of deadly force to violent felons, but also allows its use against any felon if “necessary.” Ore. Rev. Stat. § 161.239 (1983). Wisconsin’s statute is ambiguous, but should probably be added to this list. <span class="citation no-link">Wis. Stat. § 939.45</span>(4) (1981-1982) (officer may use force necessary for “a reasonable accomplishment of a lawful arrest”). But see <em>Clark </em>v. <em>Ziedonis, </em><span class="citation" data-id="1802731"><a href="/opinion/1802731/clark-v-ziedonis/" aria-description="Citation for case: Clark v. Ziedonis">368 F. Supp. 544</a></span> (ED Wis. 1973), aff’d on other grounds, <span class="citation multiple-matches"><a href="/c/F.%202d/513/79/">513 F. 2d 79</a></span> (CA7 1975).</p>
</footnote>
<footnote label="15">
<p id="b86-6"> In California, the police may use deadly force to arrest only if the crime for which the arrest is sought was “a forcible and atrocious one which threatens death or serious bodily harm,” or there is a substantial risk that the person whose arrest is sought will cause death or serious bodily harm if apprehension is delayed. <em>Kortum </em>v. <em>Alkire, </em><span class="citation" data-id="2169808"><a href="/opinion/2169808/kortum-v-alkire/#333" aria-description="Citation for case: Kortum v. Alkire">69 Cal. App. 3d 325, 333</a></span>,<span class="citation" data-id="2169808"><a href="/opinion/2169808/kortum-v-alkire/#30" aria-description="Citation for case: Kortum v. Alkire">138 Cal. Rptr. 26, 30-31</a></span> (1977). See also <em>People </em>v. <em>Ceballos, </em><span class="citation" data-id="2609526"><a href="/opinion/2609526/people-v-ceballos/#476" aria-description="Citation for case: People v. Ceballos">12 Cal. 3d 470, 476-484</a></span>, <span class="citation" data-id="2609526"><a href="/opinion/2609526/people-v-ceballos/#245" aria-description="Citation for case: People v. Ceballos">526 P. 2d 241, 245-250</a></span> (1974); <em>Long Beach Police Officers Assn. </em>v. <em>Long Beach, </em><span class="citation" data-id="2130642"><a href="/opinion/2130642/long-beach-police-officers-assn-v-city-of-long-beach/#373" aria-description="Citation for case: Long Beach Police Officers Ass&#x27;n v. City of Long Beach">61 Cal. App. 3d 364, 373-374</a></span>, <span class="citation" data-id="2130642"><a href="/opinion/2130642/long-beach-police-officers-assn-v-city-of-long-beach/#353" aria-description="Citation for case: Long Beach Police Officers Ass&#x27;n v. City of Long Beach">132 Cal. Rptr. 348, 353-354</a></span> (1976). In Indiana, deadly force may be used only to prevent injury, the imminent danger of injury or force, or the threat of force. It is not permitted simply to prevent escape. <em>Rose </em>v. <em>State, </em><span class="citation" data-id="2038641"><a href="/opinion/2038641/rose-v-state/" aria-description="Citation for case: Rose v. State">431 N. E. 2d 521</a></span> (Ind. App. 1982).</p>
</footnote>
<footnote label="16">
<p id="b86-7"> These are Michigan, Ohio, Virginia, and West Virginia. <em>Werner </em>v. <em>Hartfelder, </em><span class="citation" data-id="9684994"><a href="/opinion/1800197/werner-v-hartfelder/" aria-description="Citation for case: Werner v. Hartfelder">113 Mich. App. 747</a></span>, <span class="citation" data-id="9684994"><a href="/opinion/1800197/werner-v-hartfelder/" aria-description="Citation for case: Werner v. Hartfelder">318 N. W. 2d 825</a></span> (1982); <em>State </em>v. <em>Foster, </em><span class="citation" data-id="9311644"><a href="/opinion/9316356/state-v-foster/#59" aria-description="Citation for case: State v. Foster">60 Ohio Misc. 46, 59-66</a></span>, <span class="citation" data-id="9311644"><a href="/opinion/9316356/state-v-foster/#255" aria-description="Citation for case: State v. Foster">396 N. E. 2d 246, 255-258</a></span> (Com. Pl. 1979) (citing cases); <em>Berry </em>v. <em>Hamman, </em><span class="citation" data-id="1215610"><a href="/opinion/1215610/berry-v-hamman/" aria-description="Citation for case: Berry v. Hamman">203 Va. 596</a></span>, <span class="citation" data-id="1215610"><a href="/opinion/1215610/berry-v-hamman/" aria-description="Citation for case: Berry v. Hamman">125 S. E. 2d 851</a></span> (1962); <em>Thompson </em>v. <em>Norfolk &amp; W. R. Co., </em><span class="citation" data-id="4004205"><a href="/opinion/4227643/thompson-v-norfolk-western-railway-co/#711" aria-description="Citation for case: Thompson v. Norfolk &amp; Western Railway Co.">116 W. Va. 705, 711-712</a></span>, <span class="citation" data-id="4004205"><a href="/opinion/4227643/thompson-v-norfolk-western-railway-co/#883" aria-description="Citation for case: Thompson v. Norfolk &amp; Western Railway Co.">182 S. E. 880, 883-884</a></span> (1935).</p>
</footnote>
<footnote label="17">
<p id="b87-5"> <span class="citation no-link">Haw. Rev. Stat. §703-307</span> (1976); <span class="citation no-link">Neb. Rev. Stat. §28-1412</span> (1979). Massachusetts probably belongs in this category. Though it once rejected distinctions between felonies, <em>Uraneck </em>v. <em>Lima, </em><span class="citation" data-id="6448649"><a href="/opinion/6574887/uraneck-v-lima/#750" aria-description="Citation for case: Uraneck v. Lima">359 Mass. 749, 750</a></span>, <span class="citation" data-id="6448649"><a href="/opinion/6574887/uraneck-v-lima/#671" aria-description="Citation for case: Uraneck v. Lima">269 N. E. 2d 670, 671</a></span> (1971), it has since adopted the Model Penal Code limitations with regard to private citizens, <em>Commonwealth </em>v. <em>Klein, </em><span class="citation" data-id="2045742"><a href="/opinion/2045742/commonwealth-v-klein/" aria-description="Citation for case: Commonwealth v. Klein">372 Mass. 823</a></span>, <span class="citation" data-id="2045742"><a href="/opinion/2045742/commonwealth-v-klein/" aria-description="Citation for case: Commonwealth v. Klein">363 N. E. 2d 1313</a></span> (1977), and seems to have extended that decision to police officers, <em>Julian </em>v. <em>Randazzo, </em><span class="citation" data-id="2151033"><a href="/opinion/2151033/julian-v-randazzo/" aria-description="Citation for case: Julian v. Randazzo">380 Mass. 391</a></span>, <span class="citation" data-id="2151033"><a href="/opinion/2151033/julian-v-randazzo/" aria-description="Citation for case: Julian v. Randazzo">403 N. E. 2d 931</a></span> (1980).</p>
</footnote>
<footnote label="18">
<p id="b87-6"> <span class="citation no-link">Alaska Stat. Ann. § 11.81.370</span>(a) (1983); <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-410</span> (1978); <span class="citation no-link">Colo. Rev. Stat. § 18-1-707</span> (1978); Del. Code Ann., Tit. 11, §467 (1979) (felony involving physical force <em>and </em>a substantial risk that the suspect will cause death or serious bodily injury <em>or </em>will never be recaptured); Ga. Code § 16-3-21(a) (1984); Ill. Rev. Stat., ch. 38, ¶7-5 (1984); <span class="citation no-link">Iowa Code § 804.8</span> (1983) (suspect has used or threatened deadly force in commission of a felony, or would use deadly force if not caught); Ky. Rev. Stat. § 503.090 (1984) (suspect committed felony involving use or threat of physical force likely to cause death or serious injury, <em>and </em>is likely to endanger life unless apprehended without delay); Me. Rev. Stat. Ann., Tit. 17-A, § 107 (1983) (commentary notes that deadly force may be used only “where the person to be arrested poses a threat to human life”); <span class="citation no-link">Minn. Stat. § 609.066</span> (1984); N. H. Rev. Stat. Ann. § 627:5(II) (Supp. 1983); N. J. Stat. Ann. § 2C-3-7 (West 1982); N. Y. Penal Law § 35.30 (McKinney Supp. 1984-1985); N. C. Gen. Stat. § 15A-401 (1983); N. D. Cent. Code § 12.1-05-07.2.d (1976); <span class="citation no-link">18 Pa. Cons. Stat. §508</span> (1982); <span class="citation no-link">Tex. Penal Code Ann. § 9.51</span>(c) (1974); <span class="citation no-link">Utah Code Ann. § 76-2-404</span> (1978).</p>
</footnote>
<footnote label="19">
<p id="b87-7"> See La. Rev. Stat. Ann. § 14:20(2) (West 1974); Vt. Stat. Ann., Tit. 13, § 2305 (1974 and Supp. 1984). A Federal District Court has interpreted the Louisiana statute to limit the use of deadly force against fleeing suspects to situations where “life itself is endangered or great bodily harm is threatened.” <em>Sauls </em>v. <em>Hutto, </em><span class="citation" data-id="1868014"><a href="/opinion/1868014/sauls-v-hutto/#132" aria-description="Citation for case: Sauls v. Hutto">304 F. Supp. 124, 132</a></span> (ED La. 1969).</p>
</footnote>
<footnote label="20">
<p id="b87-8"> These are Maryland, Montana, South Carolina, and Wyoming. A Maryland appellate court has indicated, however, that deadly force may not be used against a felon who “was in the process of fleeing and, at the <page-number citation-index="1" label="18">*18</page-number>time, presented no immediate danger to . . . anyone . . . <em>Giant Food, Inc. </em>v. <em>Scherry, </em><span class="citation" data-id="2380557"><a href="/opinion/2380557/giant-food-inc-v-scherry/#589" aria-description="Citation for case: Giant Food, Inc. v. Scherry">51 Md. App. 586, 589, 596</a></span>, <span class="citation" data-id="2380557"><a href="/opinion/2380557/giant-food-inc-v-scherry/#486" aria-description="Citation for case: Giant Food, Inc. v. Scherry">444 A. 2d 483, 486, 489</a></span> (1982).</p>
</footnote>
<footnote label="21">
<p id="b88-7"> In adopting its current statute in 1979, for example, Alabama expressly chose the common-law rule over more restrictive provisions. Ala. Code § 13A-3-27, Commentary, pp. 67-63 (1982). Missouri likewise considered but rejected a proposal akin to the Model Penal Code rule. See <em>Mattis </em>v. <em>Schnarr, </em><span class="citation" data-id="341835"><a href="/opinion/341835/robert-dean-mattis-md-v-richard-r-schnarr-and-robert-marek-v-john-c/#1022" aria-description="Citation for case: Robert Dean Mattis, M.D. v. Richard R. Schnarr and Robert...">547 F. 2d 1007, 1022</a></span> (CA8 1976) (Gibson, C. J., dissenting), vacated as moot <em>sub nom. Ashcroft </em>v. <em>Mattis, </em><span class="citation" data-id="109657"><a href="/opinion/109657/ashcroft-v-mattis/" aria-description="Citation for case: Ashcroft v. Mattis">431 U. S. 171</a></span> (1977). Idaho, whose current statute codifies the common-law rule, adopted the Model Penal Code in 1971, but abandoned it in 1972.</p>
</footnote>
<footnote label="22">
<p id="b91-6"> In a recent report, the Department of Corrections of the District of Columbia also noted that “there is nothing inherently dangerous or violent about the offense,” which is a crime against property. D. C. Department of Corrections, Prisoner Screening Project 2 (1985).</p>
</footnote>
<footnote label="23">
<p id="b92-11"> The dissent points out that three-fifths of all rapes in the home, three-fifths of all home robberies, and about a third of home assaults are committed by burglars. <em>Post, </em>at 26-27. These figures mean only that if one knows that a suspect committed a rape in the home, there is a good chance that the suspect is also a burglar. That has nothing to do with the question here, which is whether the fact that someone has committed a burglary indicates that he has committed, or might commit, a violent crime.</p>
<p id="b92-12">The dissent also points out that this 3.8% adds up to 2.8 million violent crimes over a 10-year period, as if to imply that today’s holding will let loose 2.8 million violent burglars. The relevant universe is, of course, far smaller. At issue is only that tiny fraction of cases where violence has <page-number citation-index="1" label="23">*23</page-number>taken place and an officer who has no other means of apprehending the suspect is unaware of its occurrence.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Terry v. Ohio.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Terry v. Ohio"
type: case
citation: "392 U.S. 1 (1968)"
parallel_cite: "88 S. Ct. 1868; 20 L. Ed. 2d 889; 44 Ohio Op. 2d 383"
neutral_cite: 1968 U.S. LEXIS 1345
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Terry v. Ohio
  varies_by_point: false
  scope_note: "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107729/terry-v-ohio/"
  cluster_id: 107729
  opinion_id: 9423752
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Anchor"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Proof Ladder]]"
    role: "Key — rung anchor"
related: ["[[United States v. Cortez]]", "[[United States v. Arvizu]]", "[[Illinois v. Wardlow]]", "[[Florida v. J.L.]]", "[[Hiibel v. Sixth Judicial Dist. Court]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion"]
holding: "An investigative stop and protective frisk require reasonable, articulable suspicion grounded in specific facts and rational inferences…"
lake:
  record_id: Terry v. Ohio
  status: verified
  projected_at: 2026-07-09
---

# Terry v. Ohio

*392 U.S. 1 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A veteran Cleveland detective watched two men repeatedly walk past and peer into a store window, conferring between passes — conduct he took to be casing the store for a daytime robbery. He approached, identified himself, asked their names, and when they "mumbled" he spun Terry around and patted down the outside of his clothing, feeling a pistol. Terry was charged with carrying a concealed weapon and moved to suppress the gun.

## Issue
Whether a police officer who lacks probable cause to arrest may, consistent with the Fourth Amendment, stop a person to investigate suspicious conduct and conduct a limited pat-down of the outer clothing for weapons.

## Rule
A brief investigative stop must rest on specific, objective facts, not a hunch: "in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion." — 392 U.S. at 21. ^pin-21

A protective frisk is permitted where the officer reasonably fears for safety: "the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger." — [*Id.* at 27](https://www.courtlistener.com/opinion/107729/terry-v-ohio/#:~:text=the%20issue%20is%20whether%20a). ^pin-27

The Court held that "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others' safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him." — *Id.* at 30. ^pin-30

## Application
On these facts the detective's observations — two men taking turns walking the same route and staring into the store window roughly a dozen times, then conferring — supplied specific, articulable facts warranting a brief stop and supporting a reasonable belief the men were contemplating a daylight robbery and were armed. Because that belief was reasonable, the limited pat-down of the outer clothing that produced Terry's pistol was a reasonable search, and the weapon was properly admitted.

## Conclusion
The stop and protective frisk were reasonable under the Fourth Amendment; Terry's conviction was affirmed. A weapons pat-down on reasonable suspicion is permissible without probable cause to arrest.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The reasonable-suspicion standard was elaborated in [[United States v. Cortez]] ("particularized and objective basis"; "whole picture") and [[United States v. Arvizu]] ([[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; no "divide-and-conquer"), and applied to flight in [[Illinois v. Wardlow]] and anonymous tips in [[Florida v. J.L.]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Anchor*
- [[Traffic Stops]] — *Related (cross-doctrine)*
- [[The Proof Ladder]] — *Key — rung anchor*

## Sources
- *Terry v. Ohio*, 392 U.S. 1 (1968) — https://www.courtlistener.com/opinion/107729/terry-v-ohio/ — pinpoints: 21, 27, 30.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d613feb93d3f0b01", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Terry v. Ohio"}, "payload": {"all": [{"cite": "392 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 1868", "page": "1868", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 889", "page": "889", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 1345", "page": "1345", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}, {"cite": "44 Ohio Op. 2d 383", "page": "383", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "44"}], "display": "392 U.S. 1", "official": {"cite": "392 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "392"}, "official_selection_present": true, "record_id": "Terry v. Ohio"}}
{"assertion_id": "96ada73d7fe969d2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-30", "record_id": "Terry v. Ohio"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-30", "pinpoint_status": "slip-only", "quote": "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others' safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him.", "quote_fidelity": "mismatch", "record_id": "Terry v. Ohio", "star_marker": null}}
{"assertion_id": "a0de22094a427224", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-27", "record_id": "Terry v. Ohio"}, "payload": {"fragment": "#:~:text=the%20issue%20is%20whether%20a", "page": null, "pin_id": "pin-27", "pinpoint_status": "star-verified", "quote": "the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger.", "quote_fidelity": "matched", "record_id": "Terry v. Ohio", "star_marker": "27"}}
{"assertion_id": "eb39b695d50fa35e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-21", "record_id": "Terry v. Ohio"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-21", "pinpoint_status": "slip-only", "quote": "he spun Terry around and patted down the outside of his clothing, feeling a pistol. Terry was charged with carrying a concealed weapon and moved to suppress the gun. ## Issue Whether a police officer who lacks probable cause to arrest may, consistent with the Fourth Amendment, stop a person to investigate suspicious conduct and conduct a limited pat-down of the outer clothing for weapons. ## Rule A brief investigative stop must rest on specific, objective facts, not a hunch:", "quote_fidelity": "mismatch", "record_id": "Terry v. Ohio", "star_marker": null}}
{"assertion_id": "6b1ec29cf0243927", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Terry v. Ohio"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Terry v. Ohio", "scope_note": "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow).", "varies_by_point": false}}
```

### lake record — Terry v. Ohio

```json
{
  "schema_version": "s2.v1",
  "record_id": "Terry v. Ohio",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Terry v. Ohio",
    "case_name_short": "Terry",
    "case_name_full": "Terry v. Ohio",
    "input_case_name": "Terry v. Ohio",
    "court": "U.S. Supreme Court",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107729,
    "lead_opinion_id": 9423752,
    "sibling_ids": [
      107729,
      9423752,
      9423753,
      9423754,
      9423755
    ],
    "absolute_url": "/opinion/107729/terry-v-ohio/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 1",
      "volume": "392",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1868",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 889",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 383",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "383",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1345",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1345",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 1",
        "volume": "392",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1868",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1868",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 889",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1345",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1345",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 383",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "383",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-21",
      "page": null,
      "quote": "he spun Terry around and patted down the outside of his clothing, feeling a pistol. Terry was charged with carrying a concealed weapon and moved to suppress the gun. ## Issue Whether a police officer who lacks probable cause to arrest may, consistent with the Fourth Amendment, stop a person to investigate suspicious conduct and conduct a limited pat-down of the outer clothing for weapons. ## Rule A brief investigative stop must rest on specific, objective facts, not a hunch:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-27",
      "page": null,
      "quote": "the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger.",
      "star_marker": "27",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 43222,
      "fragment": "#:~:text=the%20issue%20is%20whether%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-30",
      "page": null,
      "quote": "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others' safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Terry v. Ohio",
    "varies_by_point": false,
    "scope_note": "Foundational stop-and-frisk authority; repeatedly reaffirmed and refined (Cortez, Arvizu, Wardlow).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Terry v. Ohio:lane1_negative"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Wade",
          "cluster_id": 108713,
          "cite": [
            "35 L. Ed. 2d 147",
            "93 S. Ct. 705",
            "410 U.S. 113",
            "1973 U.S. LEXIS 159"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
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
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Atweri",
          "cluster_id": 10807071,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Terry v. Ohio:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzQ2NjYyNDAwMDAwJnM9MTA1NzMxMzgmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 100,
        "triage_read": 1,
        "triage_snippet_classified": 99
      },
      "lane2_top_cited": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNDE1JnM9MTA4ODk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzU0MDA2NDAwMDAwJnM9MTA2NDYyNjQmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)",
    "indexed_citing_opinions": 22182,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107729,
        "count": 19711,
        "count_source": "search"
      },
      {
        "opinion_id": 9423752,
        "count": 2968,
        "count_source": "search"
      },
      {
        "opinion_id": 9423753,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423754,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423755,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 37960,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/terry-v-ohio.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjYyMDg3MyZzPTIyMDM1NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107729+OR+9423752+OR+9423753+OR+9423754+OR+9423755%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T14:57:50Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:24:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T14:57:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Terry v. Ohio

```
<opinion type="majority">
<author id="b46-9">Mr. Chief Justice Warren</author>
<p id="Ao">delivered the opinion of the Court.</p>
<p id="b46-10">This case presents serious questions concerning the role of the Fourth Amendment in the confrontation on the street between the citizen and the policeman investigating suspicious circumstances.</p>
<p id="b46-11">Petitioner Terry was convicted of carrying a concealed weapon and sentenced to the statutorily prescribed term of one to three years in the penitentiary.<footnotemark>1</footnotemark> Following <page-number citation-index="1" label="5">*5</page-number>the denial of a pretrial motion to suppress, the prosecution introduced in evidence two revolvers and a number of bullets seized from Terry and a codefendant, Richard Chilton,<footnotemark>2</footnotemark> by Cleveland Police Detective Martin McFadden. At the hearing on the motion to suppress this evidence, Officer McFadden testified that while he was patrolling in plain clothes in downtown Cleveland at approximately 2:30 in the afternoon of October 31, 1963, his attention was attracted by two men, Chilton and Terry, standing on the corner of Huron Road and Euclid Avenue. He had never seen the two men before, and he was unable to say precisely what first drew his eye to them. However, he testified that he had been a policeman for 39 years and a detective for 35 and that he had been assigned to patrol this vicinity of downtown Cleveland for shoplifters and pickpockets for 30 years. He explained that he had developed routine habits of observation over the years and that he would “stand and watch people or walk and watch people at many intervals of the day.” He added: “Now, in this case when I looked over they didn’t look right to me at the time.”</p>
<p id="b47-5">His interest aroused, Officer McFadden took up a post of observation in the entrance to a store 300 to 400 feet <page-number citation-index="1" label="6">*6</page-number>away from the two men. “I get more purpose to watch them when I seen their movements,” he testified. He saw one of the men leave the other one and walk southwest on Huron Road, past some stores. The man paused for a moment and looked in a store window, then walked on a short distance, turned around and walked back toward the corner, pausing once again to look in the same store window. He rejoined his companion at the comer, and the two conferred briefly. Then the second man went through the same series of motions, strolling down Huron Road, looking in the same window, walking on a short distance, turning back, peering in the store window again, and returning to confer with the first man at the corner. The two men repeated this ritual alternately between five and six times apiece — in all, roughly a dozen trips. At one point, while the two were standing together on the corner, a third man approached them and engaged them briefly in conversation. This man then left the two others and walked west on Euclid Avenue. Chilton and Terry resumed their measured pacing, peering, and conferring. After this had gone on for 10 to 12 minutes, the two men walked off together, heading west on Euclid Avenue, following the path taken earlier by the third man.</p>
<p id="b48-5">By this time Officer McFadden had become thoroughly suspicious. He testified that after observing their elaborately casual and oft-repeated reconnaissance of the store window on Huron Road, he suspected the two men of “casing a job, a stick-up,” and that he considered it his duty as a police officer to investigate further. He added that he feared “they may have a gun.” Thus, Officer McEadden followed Chilton and Terry and saw them stop in front of Zucker’s store to talk to the same man who had conferred with them earlier on the street corner. Deciding that the situation was ripe for direct action, Officer McFadden approached the three men, iden<page-number citation-index="1" label="7">*7</page-number>tified himself as a police officer and asked for their names. At this point his knowledge was confined to what he had observed. He was not acquainted with any of the three men by name or by sight, and he had received no information concerning them from any other source. When the men “mumbled something” in response to his inquiries, Officer McFadden grabbed petitioner Terry, spun him around so that they were facing the other two, with Terry between McFadden and the others, and patted down the outside of his clothing. In the left breast pocket of Terry’s overcoat Officer McFadden felt a pistol. He reached inside the overcoat pocket, but was unable to remove the gun. At this point, keeping Terry between himself and the others, the officer ordered all three men to enter Zucker’s store. As they went in, he removed Terry’s overcoat completely, removed a .38-caliber revolver from the pocket and ordered all three men to face the wall with their hands raised. Officer McFadden proceeded to pat down the outer clothing of Chilton and the third man, Katz. He discovered another revolver in the outer pocket of Chilton’s overcoat, but no weapons were found on Katz. The officer testified that he only patted the men down to see whether they had weapons, and that he did not put his hands beneath the outer garments of either Terry or Chilton until he felt their guns. So far as appears from the record, he never placed his hands beneath Katz’ outer garments. Officer McFadden seized Chilton’s gun, asked the proprietor of the store to call a police wagon, and took all three men to the station, where Chilton and Terry were formally charged with carrying concealed weapons.</p>
<p id="b49-5">On the motion to suppress the guns the prosecution took the position that they had been seized following a search incident to a lawful arrest. The trial court rejected this theory, stating that it “would be stretching the facts beyond reasonable comprehension” to find that Officer <page-number citation-index="1" label="8">*8</page-number>McFadden had had probable cause to arrest the men before he patted them down for weapons. However, the court denied the defendants’ motion on the ground that Officer McFadden, on the basis of his experience, “had reasonable cause to believe . . . that the defendants were conducting themselves suspiciously, and some interrogation should be made of their action.” Purely for his own protection, the court held, the officer had the right to pat down the outer clothing of these men, who he had reasonable cause to believe might be armed. The court distinguished between an investigatory “stop” and an arrest, and between a “frisk” of the outer clothing for weapons and a full-blown search for evidence of crime. The frisk, it held, was essential to the proper performance of the officer’s investigatory duties, for without it “the answer to the police officer may be a bullet, and a loaded pistol discovered during the frisk is admissible.”</p>
<p id="b50-5">After the court denied their motion to suppress, Chilton and Terry waived jury trial and pleaded not guilty. The court adjudged them guilty, and the Court of Appeals for the Eighth Judicial District, Cuyahoga County, affirmed. <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114</a></span> (1966). The Supreme Court of Ohio dismissed their appeal on the ground that no “substantial constitutional question” was involved. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./387/929/">387 U. S. 929</a></span> (1967), to determine whether the admission of the revolvers in evidence violated petitioner’s rights under the Fourth Amendment, made applicable to the States by the Fourteenth. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). We affirm the conviction.</p>
<p id="b50-6">I.</p>
<p id="b50-7">The Fourth Amendment provides that “the right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .” This inestimable right of <page-number citation-index="1" label="9">*9</page-number>personal security belongs as much to the citizen on the streets of our cities as to the homeowner closeted in his study to dispose of his secret affairs. For, as this Court has always recognized,</p>
<blockquote id="b51-5">“No right is held more sacred, or is more carefully guarded, by the common law, than the right of every individual to the possession and control of his own person, free from all restraint or interference of others, unless by clear and unquestionable authority of law.” <em>Union Pac. R. Co. </em>v. <em>Botsford, </em><span class="citation" data-id="93149"><a href="/opinion/93149/union-pacific-railway-co-v-botsford/#251" aria-description="Citation for case: Union Pacific Railway Co. v. Botsford">141 U. S. 250, 251</a></span> (1891).</blockquote>
<p id="b51-6">We have recently held that “the Fourth Amendment protects people, not places,” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967), and wherever an individual may harbor a reasonable “expectation of privacy,” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><em>id., </em>at 361</a></span> (Mr. Justice Harlan, concurring), he is entitled to be free from unreasonable governmental intrusion. Of course, the specific content and incidents of this right must be shaped by the context in which it is asserted. For “what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). Unquestionably petitioner was entitled to the protection of the Fourth Amendment as he walked down the street in Cleveland. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964); <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span> (1948); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). The question is whether in all the circumstances of this on-the-street encounter, his right to personal security was violated by an unreasonable search and seizure.</p>
<p id="b51-7">We would be less than candid if we did not acknowledge that this question thrusts to the fore difficult and troublesome issues regarding a sensitive area of police activity — issues which have never before been squarely <page-number citation-index="1" label="10">*10</page-number>presented to this Court. Reflective of the tensions involved are the practical and constitutional arguments pressed with great vigor on both sides of the public debate over the power of the police to “stop and frisk”— as it is sometimes euphemistically termed — suspicious persons.</p>
<p id="b52-4">On the one hand, it is frequently argued that in dealing with the rapidly unfolding and often dangerous situations on city streets the police are in need of an escalating set of flexible responses, graduated in relation to the amount of information they possess. For this purpose it is urged that distinctions should be made between a “stop” and an “arrest” (or a “seizure” of a person), and between a “frisk” and a “search.” <footnotemark>3</footnotemark> Thus, it is argued, the police should be allowed to “stop” a person and detain him briefly for questioning upon suspicion that he may be connected with criminal activity. Upon suspicion that the person may be armed, the police should have the power to “frisk” him for weapons. If the “stop” and the “frisk” give rise to probable cause to believe that the suspect has committed a crime, then the police should be empowered to make a formal “arrest,” and a full incident “search” of the person. This scheme is justified in part upon the notion that a “stop” and a “frisk” amount to a mere “minor inconvenience and petty indignity,” <footnotemark>4</footnotemark> which can properly be imposed upon the <page-number citation-index="1" label="11">*11</page-number>citizen in the interest of effective law enforcement on the basis of a police officer's suspicion.<footnotemark>5</footnotemark></p>
<p id="b53-5">On the other side the argument is made that the authority of the police must be strictly circumscribed by the law of arrest and search as it has developed to date in the traditional jurisprudence of the Fourth Amendment.<footnotemark>6</footnotemark> It is contended with some force that there is not — and cannot be — a variety of police activity which does not depend solely upon the voluntary cooperation of the citizen and yet which stops short of an arrest based upon probable cause to make such an arrest. The heart of the Fourth Amendment, the argument runs, is a severe requirement of specific justification for any intrusion upon protected personal security, coupled with á highly developed system of judicial controls to enforce upon the agents of the State the commands of the Constitution. Acquiescence by the courts in the compulsion inherent <page-number citation-index="1" label="12">*12</page-number>in the field interrogation practices at issue here, it is urged, would constitute an abdication of judicial control over, and indeed an encouragement of, substantial interference with liberty and personal security by police officers whose judgment is necessarily colored by their primary involvement in “the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). This, it is argued, can only serve to exacerbate police-community tensions in the crowded centers of our Nation’s cities.<footnotemark>7</footnotemark></p>
<p id="b54-6">In this context we approach the issues in this case mindful of the limitations of the judicial function in controlling the myriad daily situations in which policemen and citizens confront each other on the street. The State has characterized the issue here as “the right of a police officer ... to make an on-the-street stop, interrogate and pat down for weapons (known in street vernacular as ‘stop and frisk’).”<footnotemark>8</footnotemark> But this is only partly accurate. For the issue is not the abstract propriety of the police conduct, but the admissibility against petitioner of the evidence uncovered by the search and seizure. Ever since its inception, the rule excluding evidence seized in violation of the Fourth Amendment has been recognized as a principal mode of discouraging lawless police conduct. See <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-393</a></span> (1914). Thus its major thrust is a deterrent one, see <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 629-635</a></span> (1965), and experience has taught that it is the only effective deterrent to police misconduct in the criminal context, and that without it the constitutional guarantee against unreasonable searches and seizures would be a mere “form of words.” <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961). The rule also serves another vital function — “the imperative of judicial integrity.” <em>Elkins </em><page-number citation-index="1" label="13">*13</page-number>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 222</a></span> (1960). Courts which sit under our Constitution cannot and will not be made party to lawless invasions of the constitutional rights of citizens by permitting unhindered governmental use of the fruits of such invasions. Thus in our system evidentiary rulings provide the context in which the judicial process of inclusion and exclusion approves some conduct as comporting with constitutional guarantees and disapproves other actions by state agents. A ruling admitting evidence in a criminal trial, we recognize, has the necessary effect of legitimizing the conduct which produced the evidence, while an application of the exclusionary rule withholds the constitutional imprimatur.</p>
<p id="b55-5">The exclusionary rule has its limitations, however, as a tool of judicial control. It cannot properly be invoked to exclude the products of legitimate police investigative techniques on the ground that much conduct which is closely similar involves unwarranted intrusions upon constitutional protections. Moreover, in some contexts the rule is ineffective as a deterrent. Street encounters between citizens and police officers are incredibly rich in diversity. They range from wholly friendly exchanges of pleasantries or mutually useful information to hostile confrontations of armed men involving arrests, or injuries, or loss of life. Moreover, hostile confrontations are not all of a piece. Some of them begin in a friendly enough manner, only to take a different turn upon the injection of some unexpected element into the conversation. Encounters are initiated by the police for a wide variety of purposes, some of which are wholly unrelated to a desire to prosecute for crime.<footnotemark>9</footnotemark> Doubtless some <page-number citation-index="1" label="14">*14</page-number>police “field interrogation” conduct violates the Fourth Amendment. But a stern refusal by this Court to condone such activity does not necessarily render it responsive to the exclusionary rule. Regardless of how effective the rule may be where obtaining convictions is an important objective of the police,<footnotemark>10</footnotemark> it is powerless to deter invasions of constitutionally guaranteed rights where the police either have no interest in prosecuting or are willing to forgo successful prosecution in the interest of serving some other goal.</p>
<p id="b56-6">Proper adjudication of cases in which the exclusionary rule is invoked demands a constant awareness of these limitations. The wholesale harassment by certain elements of the police community, of which minority groups, particularly Negroes, frequently complain,<footnotemark>11</footnotemark> will not be <page-number citation-index="1" label="15">*15</page-number>stopped by the exclusion of any evidence from any criminal trial. Yet a rigid and unthinking application of the exclusionary rule, in futile protest against practices which it can never be used effectively to control, may exact a high toll in human injury and frustration of efforts to prevent crime. No judicial opinion can comprehend the protean variety of the street encounter, and we can only judge the facts of the case before us. Nothing we say today is to be taken as indicating approval of police conduct outside the legitimate investigative sphere. Under our decision, courts still retain their traditional responsibility to guard against police conduct which is overbearing or harassing, or which trenches upon personal security without the objective evidentiary justification which the Constitution requires. When such conduct is identified, it must be condemned by the judiciary and its fruits must be excluded from evidence in criminal trials. And, of course, our approval of legitimate and restrained investigative conduct undertaken on the basis of ample factual justification should in no way discourage the employment of other remedies than the exclusionary rule to curtail abuses for which that sanction may prove inappropriate.</p>
<p id="b57-5">Having thus roughly sketched the perimeters of the constitutional debate over the limits on police investigative conduct in general and the background against which this case presents itself, we turn our attention to the quite narrow question posed by the facts before us: whether it is always unreasonable for a policeman to seize a person and subject him to a limited search for weapons unless there is probable cause for an arrest. <page-number citation-index="1" label="16">*16</page-number>Given the narrowness of this question, we have no occasion to canvass in detail the constitutional limitations upon the scope of a policeman’s power when he confronts a citizen without probable cause to arrest him.</p>
<p id="b58-6">II.</p>
<p id="b58-7">Our first task is to establish at what point in this encounter the Fourth Amendment becomes relevant. That is, we must decide whether and when Officer McFadden “seized” Terry and whether and when he conducted a “search.” There is some suggestion in the use of such terms as “stop” and “frisk” that such police conduct is outside the purview of the Fourth Amendment because neither action rises to the level of a “search” or “seizure” within the meaning of the Constitution.<footnotemark>12</footnotemark> We emphatically reject this notion. It is quite plain that the Fourth Amendment governs “seizures” of the person which do not eventuate in a trip to the station house and prosecution for crime — “arrests” in traditional terminology. It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has “seized” that person. And it is nothing less than sheer torture of the English language to suggest that a careful exploration of the outer surfaces of a person’s clothing all over his or her body in an attempt to find weapons is not a “search.” Moreover, it is simply fantastic to urge that such a procedure <page-number citation-index="1" label="17">*17</page-number>performed in public by a policeman while the citizen stands helpless, perhaps facing a wall with his hands raised, is a “petty indignity.” <footnotemark>13</footnotemark> It is a serious intrusion upon the sanctity of the person, which may inflict great indignity and arouse strong resentment, and it is not to be undertaken lightly.<footnotemark>14</footnotemark></p>
<p id="b59-5">The danger in the logic which proceeds upon distinctions between a “stop” and an “arrest,” or “seizure” of the person, and between a “frisk” and a “search” is twofold. It seeks to isolate from constitutional scrutiny the initial stages of the contact beween the policeman and the citizen. And by suggesting a rigid all-or-nothing model of justification and regulation under the Amendment, it obscures the utility of limitations upon the scope, as well as the initiation, of police action as a means of constitutional regulation.<footnotemark>15</footnotemark> This Court has held in <page-number citation-index="1" label="18">*18</page-number>the past that a search which is reasonable at its inception may violate the Fourth Amendment by virtue of its intolerable intensity and scope. <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> (1957); <em>Go-Bart Importing Co. </em>v. <page-number citation-index="1" label="19">*19</page-number><em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#356" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 356-358</a></span> (1931); see <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#586" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 586-587</a></span> (1948). The scope of the search must be “strictly tied to and justified by” the circumstances which rendered its initiation permissible. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring); see, <em>e. g., Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30-31</a></span> (1925).</p>
<p id="b61-5">The distinctions of classical “stop-and-frisk” theory thus serve to divert attention from the central inquiry under the Fourth Amendment — the reasonableness in all the circumstances of the particular governmental invasion of a citizen’s personal security. “Search” and “seizure” are not talismans. We therefore reject the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a “technical arrest” or a “full-blown search.”</p>
<p id="b61-6">In this case there can be no question, then, that Officer McFadden “seized” petitioner and subjected him to a “search” when he took hold of him and patted down the outer surfaces of his clothing. We must decide whether at that point it was reasonable for Officer McFadden to have interfered with petitioner’s personal security as he did.<footnotemark>16</footnotemark> And in determining whether the seizure and search were “unreasonable” our inquiry <page-number citation-index="1" label="20">*20</page-number>is a dual one — whether the officer's action was justified at its inception, and whether it was reasonably related in scope to the circumstances which justified the interference in the first place.</p>
<p id="b62-4">III.</p>
<p id="b62-5">If this case involved police conduct subject to the Warrant Clause of the Fourth Amendment, we would have to ascertain whether “probable cause” existed to justify the search and seizure which took place. However, that is not the case. We do not retreat from our holdings that the police must, whenever practicable, obtain advance judicial approval of searches and seizures through the warrant procedure, see, <em>e. g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96</a></span> (1964); <em>Chapman </em>v. <em>United States, </em><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span> (1961), or that in most instances failure to comply with the warrant requirement can only be excused by exigent circumstances, see, <em>e. g., Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (hot pursuit); cf. <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964). But we deal here with an entire rubric of police conduct — necessarily swift action predicated upon the on-the-spot observations of the officer on the beat — which historically has not been, and as a practical matter could not be, subjected to the warrant procedure. Instead, the conduct involved in this case must be tested by the Fourth Amendment's general proscription against unreasonable searches and seizures.<footnotemark>17</footnotemark></p>
<p id="b62-6">Nonetheless, the notions which underlie both the warrant procedure and the requirement of probable cause remain fully relevant in this context. In order to assess the reasonableness of Officer McFadden’s conduct as a general proposition, it is necessary “first to focus upon <page-number citation-index="1" label="21">*21</page-number>the governmental interest which allegedly justifies official intrusion upon the constitutionally protected interests of the private citizen,” for there is “no ready test for determining reasonableness other than by balancing the need to search [or seize] against the invasion which the search [or seizure] entails.” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). And in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion.<footnotemark>18</footnotemark> The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances.<footnotemark>19</footnotemark> And in making that assessment it is imperative that the facts be judged against an objective standard: would the facts <page-number citation-index="1" label="22">*22</page-number>available to the officer at the moment of the seizure or the search “warrant a man of reasonable caution in the belief” that the action taken was appropriate? Cf. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964).<footnotemark>20</footnotemark> Anything less would invite intrusions upon constitutionally guaranteed rights based on nothing more substantia] than inarticulate hunches, a result this Court has. consistently refused to sanction. See, <em>e. g., Beck </em>v. <em>Ohio, supra; Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959). And simple “'good faith on the part of the arresting officer is not enough.’ ... If subjective good faith alone were the test, the protections of the Fourth Amendment would evaporate, and the people would be 'secure in their persons, houses, papers, and effects,’ only in the discretion of the police.” <em>Beck </em>v. <em>Ohio, supra, </em>at 97.</p>
<p id="b64-5">Applying these principles to this case, we consider first the nature and extent of the governmental interests involved. One general interest is of course that of effective crime prevention and detection; it is this interest which underlies the recognition that a police officer may in appropriate circumstances and in an appropriate manner approach a person for purposes of investigating possibly criminal behavior even though there is no probable cause to make an arrest. It was this legitimate investigative function Officer McFadden was discharging when he decided to approach petitioner and his companions. He had observed Terry, Chilton, and Katz go through a series of acts, each of them perhaps innocent in itself, but which taken together warranted further investigation. There is nothing unusual in two men standing together on a street corner, perhaps waiting for someone. Nor is there anything suspicious about people <page-number citation-index="1" label="23">*23</page-number>in such circumstances strolling up and down the street, singly or in pairs. Store windows, moreover, are made to be looked in. But the story is quite different where, as here, two men hover about a street corner for an extended period of time, at the end of which it becomes apparent that they are not waiting for anyone or anything ; where these men pace alternately along an identical route, pausing to stare in the same store window roughly 24 times; where each completion of this route is followed immediately by a conference between the two men on the corner; where they are joined in one of these conferences by a third man who leaves swiftly; and where the two men finally follow the third and rejoin him a couple of blocks away. It would have been poor police work indeed for an officer of 30 years’ experience in the detection of thievery from stores in this same neighborhood to have failed to investigate this behavior further.</p>
<p id="b65-5">The crux of this case, however, is not the propriety of Officer McFadden’s taking steps to investigate petitioner’s suspicious behavior, but rather, whether there was justification for McFadden’s invasion of Terry’s personal security by searching him for weapons in the course of that investigation. We are now concerned with more than the governmental interest in investigating crime; in addition, there is the more immediate interest of the police officer in taking steps to assure himself that the person with whom he is dealing is not armed with a weapon that could unexpectedly and fatally be used against him. Certainly it would be unreasonable to require that police officers take unnecessary risks in the performance of their duties. American criminals have a long tradition of armed violence, and every year in this country many law enforcement officers are killed in the line of duty, and thousands more are wounded. <page-number citation-index="1" label="24">*24</page-number>Virtually all of these deaths and a substantial portion of the injuries are inflicted with guns and knives.<footnotemark>21</footnotemark></p>
<p id="b66-6">In view of these facts, we cannot blind ourselves to the need for law enforcement officers to protect themselves and other prospective victims of violence in situations where they may lack probable cause for an arrest. When an officer is justified in believing that the individual whose suspicious behavior he is investigating at close range is armed and presently dangerous to the officer or to others, it would appear to be clearly unreasonable to deny the officer the power to take necessary measures to determine whether the person is in fact carrying a weapon and to neutralize the threat of physical harm.</p>
<p id="b66-7">We must still consider, however, the nature and quality of the intrusion on individual rights which must be accepted if police officers are to be conceded the right to search for weapons in situations where probable cause to arrest for crime is lacking. Even a limited search of the outer clothing for weapons constitutes a severe, <page-number citation-index="1" label="25">*25</page-number>though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience. Petitioner contends that such an intrusion is permissible only incident to a lawful arrest, either for a crime involving the possession of weapons or for a crime the commission of which led the officer to investigate in the first place. However, this argument must be closely examined.</p>
<p id="b67-5">Petitioner does not argue that a police officer should refrain from making any investigation of suspicious circumstances until such time as he has probable cause to make an arrest; nor does he deny that police officers in properly discharging their investigative function may find themselves confronting persons who might well be armed and dangerous. Moreover, he does not say that an officer is always unjustified in searching a suspect to discover weapons. Rather, he says it is unreasonable for the policeman to take that step until such time as the situation evolves to a point where there is probable cause to make an arrest. When that point has been reached, petitioner would concede the officer’s right to conduct a search of the suspect for weapons, fruits or instrumentalities of the crime, or “mere” evidence, incident to the arrest.</p>
<p id="b67-6">There are two weaknesses in this line of reasoning, however. First, it fails to take account of traditional limitations upon the scope of searches, and thus recognizes no distinction in purpose, character, and extent between a search incident to an arrest and a limited search for weapons. The former, although justified in part by the acknowledged necessity to protect the arresting officer from assault with a concealed weapon, <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964), is also justified on other grounds, <em>ibid., </em>and can therefore involve a relatively extensive exploration of the person. A search for weapons in the absence of probable cause to <page-number citation-index="1" label="26">*26</page-number>arrest, however, must, like any other search, be strictly circumscribed by the exigencies which justify its initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring). Thus it must be limited to that which is necessary for the discovery of weapons which might be used to harm the officer or others nearby, and may realistically be characterized as something less than a “full” search, even though it remains a serious intrusion.</p>
<p id="b68-6">A second, and related, objection to petitioner’s argument is that it assumes that the law of arrest has already worked out the balance between the particular interests involved here — the neutralization of danger to the policeman in the investigative circumstance and the sanctity of the individual. But this is not so. An arrest is a wholly different kind of intrusion upon individual freedom from a limited search for weapons, and the interests each is designed to serve are likewise quite different. An arrest is the initial stage of a criminal prosecution. It is intended to vindicate society’s interest in having its laws obeyed, and it is inevitably accompanied by future interference with the individual’s freedom of movement, whether or not trial or conviction ultimately follows.<footnotemark>22</footnotemark> The protective search for weapons, on the other hand, constitutes a brief, though far from inconsiderable, intrusion upon the sanctity of the person. It does not follow that because an officer may lawfully arrest a person only when he is apprised of facts sufficient to warrant a belief that the person has committed or is committing a crime, the officer is equally unjustified, absent that kind of evidence, in making any intrusions short of an arrest. Moreover, a perfectly reasonable apprehension of danger may arise long before the officer is possessed of adequate information to justify taking a person into custody for <page-number citation-index="1" label="27">*27</page-number>the purpose of prosecuting him for a crime. Petitioner’s reliance on cases which have worked out standards of reasonableness with regard to “seizures” constituting arrests and searches incident thereto is thus misplaced. It assumes that the interests sought to be vindicated and the invasions of personal security may be equated in the two cases, and thereby ignores a vital aspect of the analysis of the reasonableness of particular types of conduct under the Fourth Amendment. See <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra.</a></span></em></p>
<p id="b69-5">Our evaluation of the proper balance that has to be struck in this type of case leads us to conclude that there must be a narrowly drawn authority to permit a reasonable search for weapons for the protection of the police officer, where he has reason to believe that he is dealing with an armed and dangerous individual, regardless of whether he has probable cause to arrest the individual for a crime. The officer need not be absolutely certain that the individual is armed; the issue is whether a reasonably prudent man in the circumstances would be warranted in the belief that his safety or that of others was in danger. Cf. <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> <em>(1964); Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-176</a></span> (1949); <em>Stacey </em>v. <em>Emery, </em><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (1878).<footnotemark>23</footnotemark> And in determining whether the officer acted reasonably in such circumstances, due weight must be given, not to his inchoate and unparticularized suspicion or “hunch,” but to the specific reasonable inferences which he is entitled to draw from the facts in light of his experience. Cf. <em>Brinegar </em>v. <em>United States supra.</em></p>
<p id="b69-6">IY.</p>
<p id="b69-7">We must now examine the conduct of Officer McFadden in this case to determine whether his search and seizure of petitioner were reasonable, both at their in<page-number citation-index="1" label="28">*28</page-number>ception and as conducted. He had observed Terry, together with Chilton and another man, acting in a manner he took to be preface to a “stick-up.” We think on the facts and circumstances Officer McFadden detailed before the trial judge a reasonably prudent man would have been warranted in believing petitioner was armed and thus presented a threat to the officer’s safety while he was investigating his suspicious behavior. The actions of Terry and Chilton were consistent with McFadden’s hypothesis that these men were contemplating a daylight robbery — which, it is reasonable to assume, would be likely to involve the use of weapons — and nothing in their conduct from the time he first noticed them until the time he confronted them and identified himself as a police officer gave him sufficient reason to negate that hypothesis. Although the trio had departed the original scene, there was nothing to indicate abandonment of an intent to commit a robbery at some point. Thus, when Officer McFadden approached the three men gathered before the display window at Zucker’s store he had observed enough to make it quite reasonable to fear that they were armed; and nothing in their response to his hailing them, identifying himself as a police officer, and asking their names served to dispel that reasonable belief. We cannot say his decision at that point to seize Terry and pat his clothing for weapons was the product of a volatile or inventive imagination, or was undertaken simply as an act of harassment; the record evidences the tempered act of a policeman who in the course of an investigation had to make a quick decision as to how to protect himself and others from possible danger, and took limited steps to do so.</p>
<p id="b70-5">The manner in which the seizure and search were conducted is, of course, as vital a part of the inquiry as whether they were warranted at all. The Fourth Amendment proceeds as much by limitations upon the <page-number citation-index="1" label="29">*29</page-number>scope of governmental action as by imposing preconditions upon its initiation. Compare <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#354" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 354-356</a></span> (1967). The entire deterrent purpose of the rule excluding evidence seized in violation of the Fourth Amendment rests on the assumption that “limitations upon the fruit to be gathered tend to limit the quest itself.” <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930); see, <em>e. g., Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 629-635</a></span> (1965); <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#216" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 216-221</a></span> (1960). Thus, evidence may not be introduced if it was discovered by means of a seizure and search which were not reasonably related in scope to the justification for their initiation. <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#310" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 310</a></span> (1967) (Mr. Justice Fortas, concurring).</p>
<p id="b71-5">We need not develop at length in this case, however, the limitations which the Fourth Amendment places upon a protective seizure and search for weapons. These limitations will have to be developed in the concrete factual circumstances of individual cases. See <em>Sibron </em>v. <em>New York, post, </em>p. 40, decided today. Suffice it to note that such a search, unlike a search without a warrant incident to a lawful arrest, is not justified by any need to prevent the disappearance or destruction of evidence of crime. See <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). The sole justification of the search in the present situation is the protection of the police officer and others nearby, and it must therefore be confined in scope to an intrusion reasonably designed to discover guns, knives, clubs, or other hidden instruments for the assault of the police officer.</p>
<p id="b71-6">The scope of the search in this case presents no serious problem in light of these standards. Officer McFadden patted down the outer clothing of petitioner and his two companions. He did not place his hands in their pockets or under the outer surface of their garments until he had <page-number citation-index="1" label="30">*30</page-number>felt weapons, and then he merely reached for and removed the guns. He never did invade Katz’ person beyond the outer surfaces of his clothes, since he discovered nothing in his pat-down which might have been a weapon. Officer McFadden confined his search strictly to what was minimally necessary to learn whether the men were armed and to disarm them once he discovered the weapons. He did not conduct a general exploratory search for whatever evidence of criminal activity he might find.</p>
<p id="b72-4">V.</p>
<p id="b72-5">We conclude that the revolver seized from Terry was properly admitted in evidence against him. At the time he seized petitioner and searched him for weapons, Officer McFadden had reasonable grounds to believe that petitioner was armed and dangerous, and it was necessary for the protection of himself and others to take swift measures to discover the true facts and neutralize the threat of harm if it materialized. The policeman carefully restricted his search to what was appropriate to the discovery of the particular items which he sought. Each case of this sort will, of course, have to be decided on its own facts. We merely hold today that where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot and that the persons with whom he is dealing may be armed and presently dangerous, where in the course of investigating this behavior he identifies himself as a policeman and makes reasonable inquiries, and where nothing in the initial stages of the encounter serves to dispel his reasonable fear for his own or others’ safety, he is entitled for the protection of himself and others in the area to conduct a carefully limited search of the outer clothing of such persons in an attempt to discover weapons which might be used to assault him. <page-number citation-index="1" label="31">*31</page-number>Such a search is a reasonable search under the Fourth Amendment, and any weapons seized may properly be introduced in evidence against the person from whom they were taken. <em>Affirmed.</em></p>
<judges id="b73-5">Mr. Justice Black concurs in the judgment and the opinion except where the opinion quotes from and relies upon this Court’s opinion in <em>Katz </em>v. <em>United States </em>and the concurring opinion in <em>Warden </em>v. <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span>.</em></judges>
<footnote label="1">
<p id="b46-12"> Ohio Rev. Code §2923.01 (1953) provides in part that “[n]o person shall carry a pistol, bowie knife, dirk, or other dangerous weapon concealed on or about his person.” An exception is made for properly authorized law enforcement officers.</p>
</footnote>
<footnote label="2">
<p id="b47-6"> Terry and Chilton were arrested, indicted, tried, and convicted together. They were represented by the same attorney, and they made a joint motion to suppress the guns. After the motion was denied, evidence was taken in the case against Chilton. This evidence consisted of the testimony of the arresting officer and of Chilton. It was then stipulated that this testimony would be applied to the ease against Terry, and no further evidence was introduced in that case. The trial judge considered the two eases together, rendered the decisions at the same time and sentenced the two men at the same time. They prosecuted their state court appeals together through the same attorney, and they petitioned this Court for cer-tiorari together. Following the grant of the writ upon this joint petition, Chilton died. Thus, only Terry’s conviction is here for review.</p>
</footnote>
<footnote label="3">
<p id="b52-5"> Both the trial court and the Ohio Court of Appeals in this case relied upon such a distinction. <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#125" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122, 125-130</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#117" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114, 117-120</a></span> (1966). See also, e. <em>g., People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32</a></span>, 252 N. Y. S. 2d 458 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965); Aspen, Arrest and Arrest Alternatives: Recent Trends, 1966 U. Ill. L. F. 241, 249-254; Warner, The Uniform Arrest Act, <span class="citation no-link">28 Va. L. Rev. 315</span> (1942); Note, Stop and Frisk in California, 18 Hastings L. J. 623, 629-632 (1967).</p>
</footnote>
<footnote label="4">
<p id="b52-6"> <em>People </em>v. <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#3" aria-description="Citation for case: People v. Rivera"><em>Rivera, supra, </em>n. 3</a></span>, at 447, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#36" aria-description="Citation for case: People v. Rivera">201 N. E. 2d, at 36</a></span>, 252 N. Y. S. 2d, at 464.</p>
</footnote>
<footnote label="5">
<p id="b53-6"> The theory is well laid out in the <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>opinion:</p>
<blockquote id="b53-7">“[T]he evidence needed to make the inquiry is not of the same degree of conclusiveness as that required for an arrest. The stopping of the individual to inquire is not an arrest and the ground upon which the police may make the inquiry may be less incriminating than the ground for an arrest for a crime known to have been committed. . . .</blockquote>
<blockquote id="b53-8">“And as the right to stop and inquire is to be justified for a cause less conclusive than that which would sustain an arrest, so the right to frisk may be justified as an incident to inquiry upon grounds of elemental safety and precaution which might not initially sustain a search. Ultimately the validity of the frisk narrows down to whether there is or is not a right by the police to touch the person questioned. The sense of exterior touch here involved is not very far different from the sense of sight or hearing — senses upon which police customarily act.” <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, 445, 447, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#34" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32, 34, 35</a></span>, 252 N. Y. S. 2d 458, 461, 463 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965).</blockquote>
</footnote>
<footnote label="6">
<p id="b53-9"> See, <em>e. g., </em>Foote, The Fourth Amendment: Obstacle or Necessity in the Law of Arrest?, 51 J. Crim. L. C. &amp; P. S. 402 (1960).</p>
</footnote>
<footnote label="7">
<p id="b54-7"> See n. 11, <em>infra.</em></p>
</footnote>
<footnote label="8">
<p id="b54-8"><em> </em>Brief for Respondent 2.</p>
</footnote>
<footnote label="9">
<p id="b55-6"> See L. Tiffany, D. McIntyre <em>&amp; </em>D. Rotenberg, Detection of Crime: Stopping and Questioning, Search and Seizure, Encouragement and Entrapment 18-56 (1967). This sort of police conduct may, for example, be designed simply to help an intoxicated person find his way home, with no intention of arresting him unless he becomes obstreperous. Or the police may be seeking to mediate a domestic <page-number citation-index="1" label="14">*14</page-number>quarrel which threatens to erupt into violence. They may accost a woman in an area known for prostitution as part of a harassment campaign designed to drive prostitutes away without the considerable difficulty involved in prosecuting them. Or they may be conducting a dragnet search of all teenagers in a particular section of the city for weapons because they have heard rumors of an impending gang fight.</p>
</footnote>
<footnote label="10">
<p id="b56-8"> See Tiffany, McIntyre &amp; Rotenberg, <em>supra, </em>n. 9, at 100-101; Comment, <span class="citation no-link">47 Nw. U. L. Rev. 493</span>, 497-499 (1952).</p>
</footnote>
<footnote label="11">
<p id="b56-9"> The President’s Commission on Law Enforcement and Administration of Justice found that “[i]n many communities, field interrogations are a major source of friction between the police and minority groups.” President’s Commission on Law Enforcement and Administration of Justice, Task Force Report: The Police 183 (1967). It was reported that the friction caused by “[mjisuse of field interrogations” increases “as more police departments adopt ‘aggressive patrol’ in which officers are encouraged routinely to stop and question persons on the street who are unknown to them, who are suspicious, or whose purpose for being abroad is not readily evident.” <em>Id., </em>at 184. While the frequency with which “frisking” forms a part of field interrogation practice varies tremendously with the locale, the objective of the interrogation, and the particular officer, see Tiffany, McIntyre &amp; Rotenberg, <em>supra, </em>n. 9, at 47-48, it cannot help but be a severely exacerbating factor in police-community ten<page-number citation-index="1" label="15">*15</page-number>sions. This is particularly true in situations where the “stop and frisk” of youths or minority group members is “motivated by the officers’ perceived need to maintain the power image of the beat officer, an aim sometimes accomplished by humiliating anyone who attempts to undermine police control of the streets.” <em>Ibid.</em></p>
</footnote>
<footnote label="12">
<p id="b58-8"> In this case, for example, the Ohio Court of Appeals stated that “we must be careful to distinguish that the ‘frisk’ authorized herein includes only a ‘frisk’ for a dangerous weapon. It by no means authorizes a search for contraband, evidentiary material, or anything else in the absence of reasonable grounds to arrest. Such a search is controlled by the requirements of the Fourth Amendment, and probable cause is essential.” <em>State </em>v. <em>Terry, </em><span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#130" aria-description="Citation for case: State v. Terry">5 Ohio App. 2d 122, 130</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#120" aria-description="Citation for case: State v. Terry">214 N. E. 2d 114, 120</a></span> (1966). See also, <em>e. g., Ellis </em>v. <em>United States, </em>105 U. S. App. D. C. <span class="citation" data-id="9446660"><a href="/opinion/247468/edward-j-ellis-v-united-states/#374" aria-description="Citation for case: Edward J. Ellis v. United States"><em>86, 88, 264 F. 2d </em>372, 374</a></span> (1959); Comment, 65 Col. L. Rev. 848, 860, and n. 81 (1965).</p>
</footnote>
<footnote label="13">
<p id="b59-6"> Consider the following apt description:</p>
<blockquote id="b59-7">“[T]he officer must feel with sensitive fingers every portion of the prisoner’s body. A thorough search must be made of the prisoner’s arms and armpits, waistline and .back, the groin and area about the testicles, and entire surface of the legs down to the feet.” Priar &amp; Martin, Searching and Disarming Criminals, 45 J. Crim. L. C. &amp; P. S. 481 (1954).</blockquote>
</footnote>
<footnote label="14">
<p id="b59-8"> See n. 11, <em>supra, </em>and accompanying text.</p>
<p id="b59-9">We have noted that the abusive practices which play a major, though by no means exclusive, role in creating this friction are not susceptible of control by means of the exclusionary rule, and cannot properly dictate our decision with respect to the powers of the police in genuine investigative and preventive situations. However, the degree of community resentment aroused by particular practices is clearly relevant to an assessment of the quality of the intrusion upon reasonable expectations of personal security caused by those practices.</p>
</footnote>
<footnote label="15">
<p id="b59-10"> These dangers are illustrated in part by the course of adjudication in the Court of Appeals of New York. Although its first decision in this area, <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32</a></span>, 252 N. Y. S. 2d 458 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965), rested squarely on the notion that a “frisk” was not a “search,” see nn. 3-5, <em>supra, </em>it was compelled to recognize in <em>People </em>v. <em>Taggart, </em><page-number citation-index="1" label="18">*18</page-number>20 N. Y. 2d 335, 342, <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/#586" aria-description="Citation for case: People v. Taggart">229 N. E. 2d 581, 586</a></span>, 283 N. Y. S. 2d 1, 8 (1967), that what it had actually authorized in <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>and subsequent decisions, see, e. <em>g., People </em>v. <em>Pugach, </em>15 N. Y. 2d 65, <span class="citation" data-id="5521569"><a href="/opinion/5674047/people-v-pugach/" aria-description="Citation for case: People v. Pugach">204 N. E. 2d 176</a></span>, 255 N. Y. S. 2d 833 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./380/936/">380 U. S. 936</a></span> (1965), was a "search” upon less than probable cause. However, in acknowledging that no valid distinction could be maintained on the basis of its cases, the Court of Appeals continued to distinguish between the two in theory. It still defined “search” as it had in <em><span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/" aria-description="Citation for case: People v. Rivera">Rivera</a></span> </em>— as an essentially unlimited examination of the person for any and all seizable items — and merely noted that the cases had upheld police intrusions which went far beyond the original limited conception of a “frisk.” Thus, principally because it failed to consider limitations upon the scope of searches in individual cases as a potential mode of regulation, the Court of Appeals in three short years arrived at the position that the Constitution must, in the name of necessity, be held to permit unrestrained rummaging about a person and his effects upon mere suspicion. It did apparently limit its holding to “cases involving serious personal injury or grave irreparable property damage,” thus excluding those involving “the enforcement of sumptuary laws, such as gambling, and laws of limited public consequence, such as narcotics violations, prostitution, larcenies of the ordinary kind, and the like.” <em>People </em>v. <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/#340" aria-description="Citation for case: People v. Taggart"><em>Taggart, supra, </em>at 340</a></span>, <span class="citation" data-id="3704293"><a href="/opinion/3954963/state-v-terry/#584" aria-description="Citation for case: State v. Terry">214 N. E. 2d, at 584</a></span>, 283 N. Y. S. 2d, at 6.</p>
<p id="AI">In our view the sounder course is to recognize that the Eourth Amendment governs all intrusions by agents of the public upon personal security, and to make the scope of the particular intrusion, in light of all the exigencies of the case, a central element in the analysis of reasonableness. Cf. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#183" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 183</a></span> (1949) (Mr. Justice Jackson, dissenting). Compare <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967). This seems preferable to an approach which attributes too much significance to an overly technical definition of “search,” and which turns in part upon a judge-made hierarchy of legislative enactments in the criminal sphere. Focusing the inquiry squarely on the dangers and demands of the particular situation also seems more likely to produce rules which are intelligible to the police and the public alike than requiring the officer in the heat of an unfolding encounter on the street to make a judgment as to which laws are "of limited public consequence.”</p>
</footnote>
<footnote label="16">
<p id="b61-7"> We thus decide nothing today concerning the constitutional propriety of an investigative “seizure” upon less than probable cause for purposes of “detention” and/or interrogation. Obviously, not all personal intercourse between policemen and citizens involves “seizures” of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a “seizure” has occurred. We cannot tell with any certainty upon this record whether any such “seizure” took place here prior to Officer McPadden’s initiation of physical contact for purposes of searching Terry for weapons, and we thus may assume that up to that point no intrusion upon constitutionally protected rights had occurred.</p>
</footnote>
<footnote label="17">
<p id="b62-7"> See generally Leagre, The Fourth Amendment and the Law of Arrest, 54 J. Crim. L. C. &amp; P. S. 393, 396-403 (1963).</p>
</footnote>
<footnote label="18">
<p id="b63-5"> This demand for specificity in the information upon which police action is predicated is the central teaching of this Court’s Fourth Amendment jurisprudence. See <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964); <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-37</a></span> (1963); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-484</a></span> (1963); <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100-102</a></span> (1959); <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 312-314</a></span> (1959); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-178</a></span> (1949); <em>Johnson v. United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15-17</a></span> (1948); <em>United States </em>v. <em>Di Re, </em><span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#593" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 593-595</a></span> (1948); <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931); <em>Dumbra </em>v. <em>United States, </em><span class="citation" data-id="100685"><a href="/opinion/100685/dumbra-v-united-states/#441" aria-description="Citation for case: Dumbra v. United States">268 U. S. 435, 441</a></span> (1925); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#159" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 159-162</a></span> (1925); <em>Stacey </em>v. <em>Emery, </em><span class="citation" data-id="89833"><a href="/opinion/89833/stacey-v-emery/#645" aria-description="Citation for case: Stacey v. Emery">97 U. S. 642, 645</a></span> (1878).</p>
</footnote>
<footnote label="19">
<p id="b63-6"> See, e. <em>g., Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#354" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 354-357</a></span> (1967) ; <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#54" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 54-60</a></span> (1967); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-15</a></span> (1948); cf. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-480</a></span> (1963). See also <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 110-115</a></span> (1964).</p>
</footnote>
<footnote label="20">
<p id="b64-6"> See also cases cited in n. 18, <em>supra.</em></p>
</footnote>
<footnote label="21">
<p id="b66-8"> Fifty-seven law enforcement officers were killed in the line of duty in this country in 1966, bringing the total to 335 for the seven-year period beginning with 1960. Also in 1966, there were 23,851 assaults on police officers, 9,113 of which resulted in injuries to the policemen. Fifty-five of the 57 officers killed in 1966 died from gunshot wounds, 41 of them inflicted by handguns easily secreted about the person. The remaining two murders were perpetrated by knives. See Federal Bureau of Investigation, Uniform Crime Reports for the United States — 1966, at 45-48, 152 and Table 51.</p>
<p id="b66-9">The easy availability of firearms to potential criminals in this country is well known and has provoked much debate. See, <em>e. g., </em>President’s Commission on Law Enforcement and Administration of Justice, The Challenge of Crime in a Free Society 239-243 (1967). Whatever the merits of gun-control proposals, this fact is relevant to an assessment of the need for some form of self-protective search power.</p>
</footnote>
<footnote label="22">
<p id="b68-7"> See generally <em>W. </em>LaFave, Arrest — The Decision to Take a Suspect into Custody 1-13 (1965).</p>
</footnote>
<footnote label="23">
<p id="b69-8"> See also cases cited in n. 18, <em>supra.</em></p>
</footnote>
</opinion>
```

---
