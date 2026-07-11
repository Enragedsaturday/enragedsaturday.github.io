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

## GROUP: _overhaul2/lake/cases/Utah v. Strieff.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Utah v. Strieff"
type: case
citation: ""
parallel_cite: "579 U.S. 232; 136 S. Ct. 2056; 195 L. Ed. 2d 400; 84 U.S.L.W. 4430; 26 Fla. L. Weekly Fed. S 288"
neutral_cite: 2016 U.S. LEXIS 3926
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2016
date_decided: 2016-06-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2016-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Utah v. Strieff
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/8176208/utah-v-strieff/"
  cluster_id: 8176208
  opinion_id: 8137990
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Illinois]]", "[[Segura v. United States]]", "[[Herring v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "attenuation", "fruit-of-the-poisonous-tree", "arrest-warrant"]
holding: "Attenuation: discovery of a valid pre-existing arrest warrant during an unlawful stop was an intervening circumstance that attenuated…"
lake:
  record_id: Utah v. Strieff
  status: verified
  projected_at: 2026-07-09
---

# Utah v. Strieff

*579 U.S. 232 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an anonymous tip about drug activity at a house, Detective Fackrell conducted intermittent surveillance, observed visitors consistent with drug dealing, and stopped Strieff after he left the house. The State later conceded the stop lacked reasonable suspicion. During the stop, Fackrell ran Strieff's identification, discovered a valid outstanding arrest warrant for a traffic offense, arrested Strieff on that warrant, and — searching him incident to the arrest — found methamphetamine and drug paraphernalia. Strieff moved to suppress; the Utah Supreme Court ordered suppression, and the State sought review.

## Issue
Whether the discovery of a valid pre-existing arrest warrant during an unlawful investigatory stop attenuates the connection between the unlawful stop and evidence seized incident to the arrest on that warrant, making the evidence admissible.

## Rule
The [[Fruits and Attenuation|attenuation]] exception is governed by the three *[[Brown v. Illinois]]* factors. The Court looks to "the 'temporal proximity'" between the misconduct and the discovery of evidence; "the presence of intervening circumstances"; and, "'particularly' significant," "the purpose and flagrancy of the official misconduct." — 136 S. Ct. at 2061–2062. ^pin-2062

Here, the intervening-circumstances factor controlled: "the second factor, the presence of intervening circumstances, strongly favors the State" — the valid arrest warrant predated the stop and was entirely independent of it. — [136 S. Ct. at 2062](https://www.courtlistener.com/opinion/8176208/utah-v-strieff/#:~:text=the%20second%20factor%2C%20the%20presence). ^pin-2062a

## Application
Although temporal proximity favored suppression — only minutes passed between the unlawful stop and the search — the discovery of the valid, pre-existing arrest warrant was an intervening circumstance that strongly favored the State, and Officer Fackrell's conduct was at most negligent rather than purposeful or flagrant. On balance, the warrant broke the causal chain between the unlawful stop and the evidence, so the methamphetamine and paraphernalia found incident to the lawful arrest on that warrant were admissible.

## Conclusion
The discovery of the valid arrest warrant attenuated the connection between the unlawful stop and the seized evidence; the evidence was admissible, and the judgment of the Utah Supreme Court was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Strieff* applies the [[Fruits and Attenuation|attenuation]] doctrine of [[Brown v. Illinois]]: a valid pre-existing arrest warrant discovered during an unlawful stop is an intervening circumstance that, absent flagrant police misconduct, attenuates the taint of the illegal stop. (Justice Sotomayor filed a vigorous [[Common Legal Terms#dissenting-opinion|dissent]], but the decision is controlling law.)

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Utah v. Strieff*, 579 U.S. 232 (2016) — https://www.courtlistener.com/opinion/8176208/utah-v-strieff/ — pinpoints given to the parallel S. Ct. reporter (CourtListener star-paginates *Strieff* by 136 S. Ct.): 2061–2062. Cluster 8176208 → opinion 8137990.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c82cf54728c4c8ce", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Utah v. Strieff"}, "payload": {"all": [{"cite": "579 U.S. 232", "page": "232", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "579"}, {"cite": "136 S. Ct. 2056", "page": "2056", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "136"}, {"cite": "195 L. Ed. 2d 400", "page": "400", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "195"}, {"cite": "84 U.S.L.W. 4430", "page": "4430", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "84"}, {"cite": "26 Fla. L. Weekly Fed. S 288", "page": "288", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "2016 U.S. LEXIS 3926", "page": "3926", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Utah v. Strieff"}}
{"assertion_id": "393c69040634bfb7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-2062", "record_id": "Utah v. Strieff"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-2062", "pinpoint_status": "slip-only", "quote": "--- # Utah v. Strieff *579 U.S. 232 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip about drug activity at a house, Detective Fackrell conducted intermittent surveillance, observed visitors consistent with drug dealing, and stopped Strieff after he left the house. The State later conceded the stop lacked reasonable suspicion. During the stop, Fackrell ran Strieff's identification, discovered a valid outstanding arrest warrant for a traffic offense, arrested Strieff on that warrant, and — searching him incident to the arrest — found methamphetamine and drug paraphernalia. Strieff moved to suppress; the Utah Supreme Court ordered suppression, and the State sought review. ## Issue Whether the discovery of a valid pre-existing arrest warrant during an unlawful investigatory stop attenuates the connection between the unlawful stop and evidence seized incident to the arrest on that warrant, making the evidence admissible. ## Rule The attenuation exception is governed by the three *Brown v. Illinois* factors. The Court looks to", "quote_fidelity": "mismatch", "record_id": "Utah v. Strieff", "star_marker": null}}
{"assertion_id": "fdb6d89c30755ae2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-2062a", "record_id": "Utah v. Strieff"}, "payload": {"fragment": "#:~:text=the%20second%20factor%2C%20the%20presence", "page": null, "pin_id": "pin-2062a", "pinpoint_status": "star-verified", "quote": "the second factor, the presence of intervening circumstances, strongly favors the State", "quote_fidelity": "matched", "record_id": "Utah v. Strieff", "star_marker": "2062"}}
{"assertion_id": "af21fa831df93cc7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Utah v. Strieff"}, "payload": {"as_of_content": "2016-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Utah v. Strieff", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Utah v. Strieff

```json
{
  "schema_version": "s2.v1",
  "record_id": "Utah v. Strieff",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Utah v. Strieff",
    "case_name_short": "Strieff",
    "case_name_full": "UTAH v. Edward Joseph STRIEFF, Jr.",
    "input_case_name": "Utah v. Strieff",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2016-06-20",
    "year": 2016,
    "docket": null,
    "cluster_id": 8176208,
    "lead_opinion_id": 8137990,
    "sibling_ids": [
      8137990
    ],
    "absolute_url": "/opinion/8176208/utah-v-strieff/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 3214882,
        "score": 120,
        "case_name": "Utah v. Strieff"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "579 U.S. 232",
        "volume": "579",
        "reporter": "U.S.",
        "page": "232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2056",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "195 L. Ed. 2d 400",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4430",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 288",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "288",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. LEXIS 3926",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "3926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "579 U.S. 232",
        "volume": "579",
        "reporter": "U.S.",
        "page": "232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2056",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "195 L. Ed. 2d 400",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4430",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 288",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "288",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. LEXIS 3926",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "3926",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2062",
      "page": null,
      "quote": "--- # Utah v. Strieff *579 U.S. 232 (2016)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip about drug activity at a house, Detective Fackrell conducted intermittent surveillance, observed visitors consistent with drug dealing, and stopped Strieff after he left the house. The State later conceded the stop lacked reasonable suspicion. During the stop, Fackrell ran Strieff's identification, discovered a valid outstanding arrest warrant for a traffic offense, arrested Strieff on that warrant, and \u2014 searching him incident to the arrest \u2014 found methamphetamine and drug paraphernalia. Strieff moved to suppress; the Utah Supreme Court ordered suppression, and the State sought review. ## Issue Whether the discovery of a valid pre-existing arrest warrant during an unlawful investigatory stop attenuates the connection between the unlawful stop and evidence seized incident to the arrest on that warrant, making the evidence admissible. ## Rule The attenuation exception is governed by the three *Brown v. Illinois* factors. The Court looks to",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-2062a",
      "page": null,
      "quote": "the second factor, the presence of intervening circumstances, strongly favors the State",
      "star_marker": "2062",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23227,
      "fragment": "#:~:text=the%20second%20factor%2C%20the%20presence",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Utah v. Strieff",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Silveria and Travis",
          "cluster_id": 4774990,
          "cite": [
            "267 Cal. Rptr. 3d 303",
            "471 P.3d 412",
            "10 Cal. 5th 195"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dancy v. McGinley",
          "cluster_id": 4327925,
          "cite": [
            "843 F.3d 93",
            "2016 U.S. App. LEXIS 21753",
            "2016 WL 7118403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Hall v. City of Chicago",
          "cluster_id": 4738333,
          "cite": [
            "953 F.3d 945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tyslen Baker",
          "cluster_id": 4788854,
          "cite": [
            "976 F.3d 636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 4249369,
          "cite": [
            "835 F.3d 13",
            "2016 U.S. App. LEXIS 15275",
            "2016 WL 4410064"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Levin",
          "cluster_id": 4438375,
          "cite": [
            "874 F.3d 316",
            "2017 U.S. App. LEXIS 21354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oniel McKenzie",
          "cluster_id": 5092475,
          "cite": [
            "13 F.4th 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lambis",
          "cluster_id": 7321245,
          "cite": [
            "197 F. Supp. 3d 606",
            "2016 WL 3870940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ellis",
          "cluster_id": 4773617,
          "cite": [
            "469 P.3d 65"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelvin Baez",
          "cluster_id": 4843626,
          "cite": [
            "983 F.3d 1029"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Fiseku",
          "cluster_id": 8443878,
          "cite": [
            "915 F.3d 863"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mark McGill",
          "cluster_id": 4906577,
          "cite": [
            "8 F.4th 617"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Taurus Cooper",
          "cluster_id": 6248903,
          "cite": [
            "24 F.4th 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kyle Matthews",
          "cluster_id": 5064152,
          "cite": [
            "12 F.4th 647"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ramey",
          "cluster_id": 10607224,
          "cite": [
            "473 P.3d 13",
            "2020 NMCA 041"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McGovern",
          "cluster_id": 7862081,
          "cite": [
            "974 N.W.2d 595",
            "311 Neb. 705"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Latecia Watkins",
          "cluster_id": 5094052,
          "cite": [
            "13 F.4th 1202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Edwards",
          "cluster_id": 10606090,
          "cite": [
            "452 P.3d 413",
            "2019 NMCA 070"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremy Lillich",
          "cluster_id": 4903633,
          "cite": [
            "6 F.4th 869"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 10048684,
          "cite": [
            "482 Md. 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold William Barney Iii v. The State of Wyoming",
          "cluster_id": 9998680,
          "cite": [
            "2022 WY 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Malik Ngumezi",
          "cluster_id": 4808091,
          "cite": [
            "980 F.3d 1285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bray",
          "cluster_id": 4446093,
          "cite": [
            "902 N.W.2d 98",
            "297 Neb. 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Javier Garcia",
          "cluster_id": 4784058,
          "cite": [
            "974 F.3d 1071"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Utah v. Strieff:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(8137990) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 0,
        "triage_snippet_classified": 58
      },
      "lane2_top_cited": {
        "query": "cites:(8137990)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9NzMzNTgzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%288137990%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(8137990)",
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
    "complete_query": "cites:(8137990)",
    "indexed_citing_opinions": 79,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 8137990,
        "count": 79,
        "count_source": "search"
      }
    ],
    "citation_count": 424,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/utah-v-strieff.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0MTg2MTMmcz01MDkzMzg0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%288137990%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T03:39:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:43:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:40:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Utah v. Strieff (truncated)

```
<opinion type="majority">
<author id="p-8">Justice THOMAS delivered the opinion of the Court.</author>
<p id="p-9">To enforce the Fourth Amendment's prohibition against "unreasonable searches and seizures," this Court has at times required courts to exclude evidence obtained by unconstitutional police conduct. But the Court has also held that, even when there is a Fourth Amendment violation, this exclusionary rule does not apply when the costs of exclusion outweigh its deterrent benefits. In some cases, for example, the link between the unconstitutional conduct and the discovery of the evidence is too attenuated to justify suppression. The question in this case is whether this attenuation doctrine applies when an officer makes an unconstitutional investigatory stop; learns during that stop that the suspect is subject to a valid arrest warrant; and proceeds to arrest the suspect and seize incriminating evidence during a search incident to that arrest. We hold that the evidence the officer seized as part of the search incident to arrest is admissible because the officer's discovery of the arrest warrant attenuated the connection between the unlawful stop and the evidence seized incident to arrest.</p>
<p id="p-10">I</p>
<p id="p-11">This case began with an anonymous tip. In December 2006, someone called the South Salt Lake City police's drug-tip line to report "narcotics activity" at a particular residence. App. 15. Narcotics detective Douglas Fackrell investigated the tip. Over the course of about a week, Officer Fackrell conducted intermittent surveillance of the home. He observed visitors who left a few minutes after arriving at the house. These visits were sufficiently frequent to raise his suspicion that the occupants were dealing drugs.</p>
<p id="p-12"><a class="page-label" data-citation-index="1" data-label="2060" href="#p2060" id="p2060">*2060</a>One of those visitors was respondent Edward Strieff. Officer Fackrell observed Strieff exit the house and walk toward a nearby convenience store. In the store's parking lot, Officer Fackrell detained Strieff, identified himself, and asked Strieff what he was doing at the residence.</p>
<p id="p-13">As part of the stop, Officer Fackrell requested Strieff's identification, and Strieff produced his Utah identification card. Officer Fackrell relayed Strieff's information to a police dispatcher, who reported that Strieff had an outstanding arrest warrant for a traffic violation. Officer Fackrell then arrested Strieff pursuant to that warrant. When Officer Fackrell searched Strieff incident to the arrest, he discovered a baggie of methamphetamine and drug paraphernalia.</p>
<p id="p-14">The State charged Strieff with unlawful possession of methamphetamine and drug paraphernalia. Strieff moved to suppress the evidence, arguing that the evidence was inadmissible because it was derived from an unlawful investigatory stop. At the suppression hearing, the prosecutor conceded that Officer Fackrell lacked reasonable suspicion for the stop but argued that the evidence should not be suppressed because the existence of a valid arrest warrant attenuated the connection between the unlawful stop and the discovery of the contraband.</p>
<p id="p-15">The trial court agreed with the State and admitted the evidence. The court found that the short time between the illegal stop and the search weighed in favor of suppressing the evidence, but that two countervailing considerations made it admissible. First, the court considered the presence of a valid arrest warrant to be an " 'extraordinary intervening circumstance.' " App. to Pet. for Cert. 102 (quoting <em>United States v. Simpson,</em> <extracted-citation case-ids="31264" index="0" url="https://cite.case.law/f3d/439/490/#p496"><span class="citation" data-id="793479"><a href="/opinion/793479/united-states-v-bryan-lee-simpson/" aria-description="Citation for case: United States v. Bryan Lee Simpson">439 F.3d 490</a></span></extracted-citation>, 496 (C.A.8 2006) ). Second, the court stressed the absence of flagrant misconduct by Officer Fackrell, who was conducting a legitimate investigation of a suspected drug house.</p>
<p id="p-16">Strieff conditionally pleaded guilty to reduced charges of attempted possession of a controlled substance and possession of drug paraphernalia, but reserved his right to appeal the trial court's denial of the suppression motion. The Utah Court of Appeals affirmed. 2012 UT App ¶ 245, <extracted-citation case-ids="6980961" index="1" url="https://cite.case.law/p3d/286/317/"><span class="citation" data-id="9823262"><a href="/opinion/5308578/state-v-strieff/" aria-description="Citation for case: State v. Strieff">286 P.3d 317</a></span></extracted-citation>.</p>
<p id="p-17">The Utah Supreme Court reversed. 2015 UT ¶ 2, <extracted-citation case-ids="6842912" index="2" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">357 P.3d 532</a></span></extracted-citation>. It held that the evidence was inadmissible because only "a voluntary act of a defendant's free will (as in a confession or consent to search)" sufficiently breaks the connection between an illegal search and the discovery of evidence. <em><extracted-citation case-ids="6842912" index="3" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6842912" index="3" url="https://cite.case.law/p3d/357/532/"> at 536</extracted-citation>. Because Officer Fackrell's discovery of a valid arrest warrant did not fit this description, the court ordered the evidence suppressed. <em>Ibid</em> .</p>
<p id="p-18">We granted certiorari to resolve disagreement about how the attenuation doctrine applies where an unconstitutional detention leads to the discovery of a valid arrest warrant. 576 U.S. ----, <extracted-citation case-ids="12599313,12599314,12599315,12599316,12599317,12599318" index="4" url="https://cite.case.law/s-ct/136/27/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/27/">136 S.Ct. 27</a></span></extracted-citation>, <extracted-citation case-ids="12599248,12599313,12599314,12599315,12599451" index="5" url="https://cite.case.law/l-ed-2d/192/997/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/192/997/">192 L.Ed.2d 997</a></span></extracted-citation> (2015). Compare, <em>e.g.,</em> <em>United States v. Green,</em> <extracted-citation case-ids="11912832" index="6" url="https://cite.case.law/f3d/111/515/#p522"><span class="citation" data-id="739711"><a href="/opinion/739711/united-states-v-david-lee-green/" aria-description="Citation for case: United States v. David Lee Green">111 F.3d 515</a></span></extracted-citation>, 522-523 (C.A.7 1997) (holding that discovery of the warrant is a dispositive intervening circumstance where police misconduct was not flagrant), with, <em>e.g.,</em> <em>State v. Moralez,</em> <extracted-citation case-ids="12416938" index="7" url="https://cite.case.law/kan/297/397/#p415"><span class="citation" data-id="7923492"><a href="/opinion/7971077/state-v-moralez/" aria-description="Citation for case: State v. Moralez">297 Kan. 397</a></span></extracted-citation>, 415, <extracted-citation case-ids="12416938" index="8" url="https://cite.case.law/kan/297/397/#p415"><span class="citation" data-id="7923492"><a href="/opinion/7971077/state-v-moralez/" aria-description="Citation for case: State v. Moralez">300 P.3d 1090</a></span></extracted-citation>, 1102 (2013) (assigning little significance to the discovery of the warrant). We now reverse.</p>
<p id="p-19">II</p>
<p id="p-20">A</p>
<p id="p-21">The Fourth Amendment protects "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." Because officers who violated the <a class="page-label" data-citation-index="1" data-label="2061" href="#p2061" id="p2061">*2061</a>Fourth Amendment were traditionally considered trespassers, individuals subject to unconstitutional searches or seizures historically enforced their rights through tort suits or self-help. Davies, Recovering the Original Fourth Amendment, <extracted-citation index="9" url="https://cite.case.law/citations/?q=98%20Mich.%20L.%20Rev.%20547"><span class="citation no-link">98 Mich. L. Rev. 547</span></extracted-citation>, 625 (1999). In the 20th century, however, the exclusionary rule-the rule that often requires trial courts to exclude unlawfully seized evidence in a criminal trial-became the principal judicial remedy to deter Fourth Amendment violations. See, <em>e.g.,</em> <em>Mapp v. Ohio,</em> <extracted-citation case-ids="1785580" index="10" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span></extracted-citation>, 655, <extracted-citation case-ids="1785580" index="11" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S.Ct. 1684</a></span></extracted-citation>, <extracted-citation case-ids="1785580" index="12" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L.Ed.2d 1081</a></span></extracted-citation> (1961).</p>
<p id="p-22">Under the Court's precedents, the exclusionary rule encompasses both the "primary evidence obtained as a direct result of an illegal search or seizure" and, relevant here, "evidence later discovered and found to be derivative of an illegality," the so-called " 'fruit of the poisonous tree.' " <em>Segura v. United States,</em> <extracted-citation case-ids="11340278" index="13" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, 804, <extracted-citation case-ids="11340278" index="14" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="15" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation> (1984). But the significant costs of this rule have led us to deem it "applicable only ... where its deterrence benefits outweigh its substantial social costs." <em>Hudson v. Michigan,</em> <extracted-citation case-ids="3276422" index="16" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">547 U.S. 586</a></span></extracted-citation>, 591, <extracted-citation case-ids="3276422" index="17" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span></extracted-citation>, <extracted-citation case-ids="3276422" index="18" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">165 L.Ed.2d 56</a></span></extracted-citation> (2006) (internal quotation marks omitted). "Suppression of evidence ... has always been our last resort, not our first impulse." <em><extracted-citation case-ids="3276422" index="19" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">Ibid.</a></span></extracted-citation></em></p>
<p id="p-23">We have accordingly recognized several exceptions to the rule. Three of these exceptions involve the causal relationship between the unconstitutional act and the discovery of evidence. First, the independent source doctrine allows trial courts to admit evidence obtained in an unlawful search if officers independently acquired it from a separate, independent source. See <em>Murray v. United States,</em> <extracted-citation case-ids="1775229" index="20" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">487 U.S. 533</a></span></extracted-citation>, 537, <extracted-citation case-ids="1775229" index="21" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529</a></span></extracted-citation>, <extracted-citation case-ids="1775229" index="22" url="https://cite.case.law/us/487/533/#p537"><span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">101 L.Ed.2d 472</a></span></extracted-citation> (1988). Second, the inevitable discovery doctrine allows for the admission of evidence that would have been discovered even without the unconstitutional source. See <em>Nix v. Williams,</em> <extracted-citation case-ids="6201711" index="23" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U.S. 431</a></span></extracted-citation>, 443-444, <extracted-citation case-ids="6201711" index="24" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">104 S.Ct. 2501</a></span></extracted-citation>, <extracted-citation case-ids="6201711" index="25" url="https://cite.case.law/us/467/431/#p443"><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">81 L.Ed.2d 377</a></span></extracted-citation> (1984). Third, and at issue here, is the attenuation doctrine: Evidence is admissible when the connection between unconstitutional police conduct and the evidence is remote or has been interrupted by some intervening circumstance, so that "the interest protected by the constitutional guarantee that has been violated would not be served by suppression of the evidence obtained." <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#593" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra,</em> at 593</a></span>, <extracted-citation case-ids="3276422" index="26" url="https://cite.case.law/us/547/586/#p591"><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/" aria-description="Citation for case: Hudson v. Michigan">126 S.Ct. 2159</a></span></extracted-citation>.</p>
<p id="p-24">B</p>
<p id="p-25">Turning to the application of the attenuation doctrine to this case, we first address a threshold question: whether this doctrine applies at all to a case like this, where the intervening circumstance that the State relies on is the discovery of a valid, pre-existing, and untainted arrest warrant. The Utah Supreme Court declined to apply the attenuation doctrine because it read our precedents as applying the doctrine only "to circumstances involving an independent act of a defendant's 'free will' in confessing to a crime or consenting to a search." <extracted-citation case-ids="6842912" index="27" url="https://cite.case.law/p3d/357/532/"><span class="citation" data-id="2770744"><a href="/opinion/2770744/state-v-strieff/" aria-description="Citation for case: State v. Strieff">357 P.3d, at 544</a></span></extracted-citation>. In this Court, Strieff has not defended this argument, and we disagree with it, as well. The attenuation doctrine evaluates the causal link between the government's unlawful act and the discovery of evidence, which often has nothing to do with a defendant's actions. And the logic of our prior attenuation cases is not limited to independent acts by the defendant.</p>
<p id="p-26">It remains for us to address whether the discovery of a valid arrest warrant was a sufficient intervening event to break the causal chain between the unlawful stop and the discovery of drug-related evidence on Strieff's person. The three factors articulated in <a class="page-label" data-citation-index="1" data-label="2062" href="#p2062" id="p2062">*2062</a><em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="28" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="29" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="30" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975), guide our analysis. First, we look to the "temporal proximity" between the unconstitutional conduct and the discovery of evidence to determine how closely the discovery of evidence followed the unconstitutional search. <em><extracted-citation case-ids="9639" index="31" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="31" url="https://cite.case.law/us/422/590/"> at 603</extracted-citation>, <extracted-citation case-ids="9639" index="32" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Second, we consider "the presence of intervening circumstances." <em><extracted-citation case-ids="9639" index="33" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="33" url="https://cite.case.law/us/422/590/"> at 603-604</extracted-citation>, <extracted-citation case-ids="9639" index="34" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Third, and "particularly" significant, we examine "the purpose and flagrancy of the official misconduct." <em><extracted-citation case-ids="9639" index="35" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="35" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="36" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. In evaluating these factors, we assume without deciding (because the State conceded the point) that Officer Fackrell lacked reasonable suspicion to initially stop Strieff. And, because we ultimately conclude that the warrant breaks the causal chain, we also have no need to decide whether the warrant's existence alone would make the initial stop constitutional even if Officer Fackrell was unaware of its existence.</p>
<p id="p-27">1</p>
<p id="p-28">The first factor, temporal proximity between the initially unlawful stop and the search, favors suppressing the evidence. Our precedents have declined to find that this factor favors attenuation unless "substantial time" elapses between an unlawful act and when the evidence is obtained. <em>Kaupp v. Texas,</em> <extracted-citation case-ids="9031233" index="37" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">538 U.S. 626</a></span></extracted-citation>, 633, <extracted-citation case-ids="9031233" index="38" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="9031233" index="39" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">155 L.Ed.2d 814</a></span></extracted-citation> (2003) (<em>per curiam</em> ). Here, however, Officer Fackrell discovered drug contraband on Strieff's person only minutes after the illegal stop. See App. 18-19. As the Court explained in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</em> such a short time interval counsels in favor of suppression; there, we found that the confession should be suppressed, relying in part on the "less than two hours" that separated the unconstitutional arrest and the confession. <extracted-citation case-ids="9639" index="40" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 604</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="41" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>.</p>
<p id="p-29">In contrast, the second factor, the presence of intervening circumstances, strongly favors the State. In <em>Segura,</em> <extracted-citation case-ids="11340278" index="42" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="43" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="44" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation>, the Court addressed similar facts to those here and found sufficient intervening circumstances to allow the admission of evidence. There, agents had probable cause to believe that apartment occupants were dealing cocaine. <em><extracted-citation case-ids="11340278" index="45" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="45" url="https://cite.case.law/us/468/796/#p804"> at 799-800</extracted-citation>, <extracted-citation case-ids="11340278" index="46" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. They sought a warrant. In the meantime, they entered the apartment, arrested an occupant, and discovered evidence of drug activity during a limited search for security reasons. <em><extracted-citation case-ids="11340278" index="47" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="47" url="https://cite.case.law/us/468/796/#p804"> at 800-801</extracted-citation>, <extracted-citation case-ids="11340278" index="48" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. The next evening, the Magistrate Judge issued the search warrant. <em><extracted-citation case-ids="11340278" index="49" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Ibid.</a></span></extracted-citation></em> This Court deemed the evidence admissible notwithstanding the illegal search because the information supporting the warrant was "wholly unconnected with the [arguably illegal] entry and was known to the agents well before the initial entry." <em><extracted-citation case-ids="11340278" index="50" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="50" url="https://cite.case.law/us/468/796/#p804"> at 814</extracted-citation>, <extracted-citation case-ids="11340278" index="51" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-30"><em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span>,</em> of course, applied the independent source doctrine because the unlawful entry "did not contribute in any way to discovery of the evidence seized under the warrant." <em><extracted-citation case-ids="11340278" index="52" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="52" url="https://cite.case.law/us/468/796/#p804"> at 815</extracted-citation>, <extracted-citation case-ids="11340278" index="53" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. But the <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> Court suggested that the existence of a valid warrant favors finding that the connection between unlawful conduct and the discovery of evidence is "sufficiently attenuated to dissipate the taint." <em><extracted-citation case-ids="11340278" index="54" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Ibid.</a></span></extracted-citation></em> That principle applies here.</p>
<p id="p-31">In this case, the warrant was valid, it predated Officer Fackrell's investigation, and it was entirely unconnected with the stop. And once Officer Fackrell discovered the warrant, he had an obligation to arrest Strieff. "A warrant is a judicial mandate to an officer to conduct a search or make an arrest, and the officer has a sworn duty to carry out its provisions." <em>United States v. Leon,</em> <extracted-citation case-ids="11340969" index="55" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span></extracted-citation>, 920, n. 21, <extracted-citation case-ids="11340969" index="56" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="57" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span></extracted-citation> (1984) (internal quotation marks omitted). Officer <a class="page-label" data-citation-index="1" data-label="2063" href="#p2063" id="p2063">*2063</a>Fackrell's arrest of Strieff thus was a ministerial act that was independently compelled by the pre-existing warrant. And once Officer Fackrell was authorized to arrest Strieff, it was undisputedly lawful to search Strieff as an incident of his arrest to protect Officer Fackrell's safety. See <em>Arizona v. Gant,</em> <extracted-citation case-ids="3653882" index="58" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U.S. 332</a></span></extracted-citation>, 339, <extracted-citation case-ids="3653882" index="59" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">129 S.Ct. 1710</a></span></extracted-citation>, <extracted-citation case-ids="3653882" index="60" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">173 L.Ed.2d 485</a></span></extracted-citation> (2009) (explaining the permissible scope of searches incident to arrest).</p>
<p id="p-32">Finally, the third factor, "the purpose and flagrancy of the official misconduct," <em>Brown, <extracted-citation case-ids="9639" index="61" url="https://cite.case.law/us/422/590/">supra,</extracted-citation></em><extracted-citation case-ids="9639" index="61" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="62" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, also strongly favors the State. The exclusionary rule exists to deter police misconduct. <em>Davis v. United States,</em> <extracted-citation case-ids="5928256,12450488" index="63" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S. 229</a></span></extracted-citation>, 236-237, <extracted-citation case-ids="5928256,12450488" index="64" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>, <extracted-citation case-ids="12450488,5928256" index="65" url="https://cite.case.law/l-ed-2d/180/285/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span></extracted-citation> (2011). The third factor of the attenuation doctrine reflects that rationale by favoring exclusion only when the police misconduct is most in need of deterrence-that is, when it is purposeful or flagrant.</p>
<p id="p-33">Officer Fackrell was at most negligent. In stopping Strieff, Officer Fackrell made two good-faith mistakes. First, he had not observed what time Strieff entered the suspected drug house, so he did not know how long Strieff had been there. Officer Fackrell thus lacked a sufficient basis to conclude that Strieff was a short-term visitor who may have been consummating a drug transaction. Second, because he lacked confirmation that Strieff was a short-term visitor, Officer Fackrell should have asked Strieff whether he would speak with him, instead of demanding that Strieff do so. Officer Fackrell's stated purpose was to "find out what was going on [in] the house." App. 17. Nothing prevented him from approaching Strieff simply to ask. See <em>Florida v. Bostick,</em> <extracted-citation case-ids="1108039" index="66" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429</a></span></extracted-citation>, 434, <extracted-citation case-ids="1108039" index="67" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382</a></span></extracted-citation>, <extracted-citation case-ids="1108039" index="68" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span></extracted-citation> (1991) ("[A] seizure does not occur simply because a police officer approaches an individual and asks a few questions"). But these errors in judgment hardly rise to a purposeful or flagrant violation of Strieff's Fourth Amendment rights.</p>
<p id="p-34">While Officer Fackrell's decision to initiate the stop was mistaken, his conduct thereafter was lawful. The officer's decision to run the warrant check was a "negligibly burdensome precautio[n]" for officer safety. <em>Rodriguez v. United States,</em> 575 U.S. ----, ----, <extracted-citation case-ids="12588788" index="69" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct. 1609</a></span></extracted-citation>, 1616, <extracted-citation case-ids="12588788" index="70" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">191 L.Ed.2d 492</a></span></extracted-citation> (2015). And Officer Fackrell's actual search of Strieff was a lawful search incident to arrest. See <em>Gant, <extracted-citation case-ids="3653882" index="71" url="https://cite.case.law/us/556/332/#p339">supra,</extracted-citation></em><extracted-citation case-ids="3653882" index="71" url="https://cite.case.law/us/556/332/#p339"> at 339</extracted-citation>, <extracted-citation case-ids="3653882" index="72" url="https://cite.case.law/us/556/332/#p339"><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">129 S.Ct. 1710</a></span></extracted-citation>.</p>
<p id="p-35">Moreover, there is no indication that this unlawful stop was part of any systemic or recurrent police misconduct. To the contrary, all the evidence suggests that the stop was an isolated instance of negligence that occurred in connection with a bona fide investigation of a suspected drug house. Officer Fackrell saw Strieff leave a suspected drug house. And his suspicion about the house was based on an anonymous tip and his personal observations.</p>
<p id="p-36">Applying these factors, we hold that the evidence discovered on Strieff's person was admissible because the unlawful stop was sufficiently attenuated by the pre-existing arrest warrant. Although the illegal stop was close in time to Strieff's arrest, that consideration is outweighed by two factors supporting the State. The outstanding arrest warrant for Strieff's arrest is a critical intervening circumstance that is wholly independent of the illegal stop. The discovery of that warrant broke the causal chain between the unconstitutional stop and the discovery of evidence by compelling Officer Fackrell to arrest Strieff. And, it is especially significant that there is no evidence that Officer Fackrell's illegal stop reflected flagrantly unlawful police misconduct.</p>
<p id="p-37"><a class="page-label" data-citation-index="1" data-label="2064" href="#p2064" id="p2064">*2064</a>2</p>
<p id="p-38">We find Strieff's counterarguments unpersuasive.</p>
<p id="p-39">First, he argues that the attenuation doctrine should not apply because the officer's stop was purposeful and flagrant. He asserts that Officer Fackrell stopped him solely to fish for evidence of suspected wrongdoing. But Officer Fackrell sought information from Strieff to find out what was happening inside a house whose occupants were legitimately suspected of dealing drugs. This was not a suspicionless fishing expedition "in the hope that something would turn up." <em>Taylor v. Alabama,</em> <extracted-citation case-ids="6193489" index="73" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">457 U.S. 687</a></span></extracted-citation>, 691, <extracted-citation case-ids="6193489" index="74" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">102 S.Ct. 2664</a></span></extracted-citation>, <extracted-citation case-ids="6193489" index="75" url="https://cite.case.law/us/457/687/#p691"><span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">73 L.Ed.2d 314</a></span></extracted-citation> (1982).</p>
<p id="p-40">Strieff argues, moreover, that Officer Fackrell's conduct was flagrant because he detained Strieff without the necessary level of cause (here, reasonable suspicion). But that conflates the standard for an illegal stop with the standard for flagrancy. For the violation to be flagrant, more severe police misconduct is required than the mere absence of proper cause for the seizure. See, <em>e.g.,</em> <em>Kaupp,</em> <extracted-citation case-ids="9031233" index="76" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/#628" aria-description="Citation for case: Kaupp v. Texas">538 U.S., at 628</a></span>, 633</extracted-citation>, <extracted-citation case-ids="9031233" index="77" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation> (finding flagrant violation where a warrantless arrest was made in the arrestee's home after police were denied a warrant and at least some officers knew they lacked probable cause). Neither the officer's alleged purpose nor the flagrancy of the violation rise to a level of misconduct to warrant suppression.</p>
<p id="p-41">Second, Strieff argues that, because of the prevalence of outstanding arrest warrants in many jurisdictions, police will engage in dragnet searches if the exclusionary rule is not applied. We think that this outcome is unlikely. Such wanton conduct would expose police to civil liability. See <extracted-citation index="78" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> ; <em>Monell v. New York City Dept. of Social Servs.,</em> <extracted-citation case-ids="1490618" index="79" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U.S. 658</a></span></extracted-citation>, 690, <extracted-citation case-ids="1490618" index="80" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">98 S.Ct. 2018</a></span></extracted-citation>, <extracted-citation case-ids="1490618" index="81" url="https://cite.case.law/us/436/658/#p690"><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">56 L.Ed.2d 611</a></span></extracted-citation> (1978) ; see also <em>Segura,</em> <extracted-citation case-ids="11340278" index="82" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S., at 812</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="83" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. And in any event, the <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> factors take account of the purpose and flagrancy of police misconduct. Were evidence of a dragnet search presented here, the application of the <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> factors could be different. But there is no evidence that the concerns that Strieff raises with the criminal justice system are present in South Salt Lake City, Utah.</p>
<p id="p-42">* * *</p>
<p id="p-43">We hold that the evidence Officer Fackrell seized as part of his search incident to arrest is admissible because his discovery of the arrest warrant attenuated the connection between the unlawful stop and the evidence seized from Strieff incident to arrest. The judgment of the Utah Supreme Court, accordingly, is reversed.</p>
<p id="p-44"><em>It is so ordered.</em></p>
<p id="p-45">Justice SOTOMAYOR, with whom Justice GINSBURG joins as to Parts I, II, and III, dissenting.</p>
<p id="p-46">The Court today holds that the discovery of a warrant for an unpaid parking ticket will forgive a police officer's violation of your Fourth Amendment rights. Do not be soothed by the opinion's technical language: This case allows the police to stop you on the street, demand your identification, and check it for outstanding traffic warrants-even if you are doing nothing wrong. If the officer discovers a warrant for a fine you forgot to pay, courts will now excuse his illegal stop and will admit into evidence anything he happens to find by searching you after arresting you on the warrant. Because the Fourth Amendment should prohibit, not permit, such misconduct, I dissent.</p>
<p id="p-47">I</p>
<p id="p-48">Minutes after Edward Strieff walked out of a South Salt Lake City home, an officer stopped him, questioned him, and took his <a class="page-label" data-citation-index="1" data-label="2065" href="#p2065" id="p2065">*2065</a>identification to run it through a police database. The officer did not suspect that Strieff had done anything wrong. Strieff just happened to be the first person to leave a house that the officer thought might contain "drug activity." App. 16-19.</p>
<p id="p-49">As the State of Utah concedes, this stop was illegal. App. 24. The Fourth Amendment protects people from "unreasonable searches and seizures." An officer breaches that protection when he detains a pedestrian to check his license without any evidence that the person is engaged in a crime. <em>Delaware v. Prouse,</em> <extracted-citation case-ids="6187389" index="84" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span></extracted-citation>, 663, <extracted-citation case-ids="6187389" index="85" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="6187389" index="86" url="https://cite.case.law/us/440/648/#p663"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L.Ed.2d 660</a></span></extracted-citation> (1979) ; <em>Terry v. Ohio,</em> <extracted-citation case-ids="6167798" index="87" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span></extracted-citation>, 21, <extracted-citation case-ids="6167798" index="88" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="89" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span></extracted-citation> (1968). The officer deepens the breach when he prolongs the detention just to fish further for evidence of wrongdoing. <em>Rodriguez v. United States,</em> 575 U.S. ----, ---- - ----, <extracted-citation case-ids="12588788" index="90" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct. 1609</a></span></extracted-citation>, 1615-1616, <extracted-citation case-ids="12588788" index="91" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">191 L.Ed.2d 492</a></span></extracted-citation> (2015). In his search for lawbreaking, the officer in this case himself broke the law.</p>
<p id="p-50">The officer learned that Strieff had a "small traffic warrant." App. 19. Pursuant to that warrant, he arrested Strieff and, conducting a search incident to the arrest, discovered methamphetamine in Strieff's pockets.</p>
<p id="p-51">Utah charged Strieff with illegal drug possession. Before trial, Strieff argued that admitting the drugs into evidence would condone the officer's misbehavior. The methamphetamine, he reasoned, was the product of the officer's illegal stop. Admitting it would tell officers that unlawfully discovering even a "small traffic warrant" would give them license to search for evidence of unrelated offenses. The Utah Supreme Court unanimously agreed with Strieff. A majority of this Court now reverses.</p>
<p id="p-52">II</p>
<p id="p-53">It is tempting in a case like this, where illegal conduct by an officer uncovers illegal conduct by a civilian, to forgive the officer. After all, his instincts, although unconstitutional, were correct. But a basic principle lies at the heart of the Fourth Amendment: Two wrongs don't make a right. See <em>Weeks v. United States,</em> <extracted-citation case-ids="3672825" index="92" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span></extracted-citation>, 392, <extracted-citation case-ids="3672825" index="93" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span></extracted-citation>, <extracted-citation case-ids="3672825" index="94" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L.Ed. 652</a></span></extracted-citation> (1914). When "lawless police conduct" uncovers evidence of lawless civilian conduct, this Court has long required later criminal trials to exclude the illegally obtained evidence. <em>Terry,</em> <extracted-citation case-ids="6167798" index="95" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 12</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="96" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation> ; <em>Mapp v. Ohio,</em> <extracted-citation case-ids="1785580" index="97" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U.S. 643</a></span></extracted-citation>, 655, <extracted-citation case-ids="1785580" index="98" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">81 S.Ct. 1684</a></span></extracted-citation>, <extracted-citation case-ids="1785580" index="99" url="https://cite.case.law/us/367/643/#p655"><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">6 L.Ed.2d 1081</a></span></extracted-citation> (1961). For example, if an officer breaks into a home and finds a forged check lying around, that check may not be used to prosecute the homeowner for bank fraud. We would describe the check as " 'fruit of the poisonous tree.' " <em>Wong Sun v. United States,</em> <extracted-citation case-ids="450611" index="100" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S. 471</a></span></extracted-citation>, 488, <extracted-citation case-ids="450611" index="101" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>, <extracted-citation case-ids="450611" index="102" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">9 L.Ed.2d 441</a></span></extracted-citation> (1963). Fruit that must be cast aside includes not only evidence directly found by an illegal search but also evidence "come at by exploitation of that illegality." <em>Ibid</em> .</p>
<p id="p-54">This "exclusionary rule" removes an incentive for officers to search us without proper justification. <em>Terry,</em> <extracted-citation case-ids="6167798" index="103" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 12</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="104" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. It also keeps courts from being "made party to lawless invasions of the constitutional rights of citizens by permitting unhindered governmental use of the fruits of such invasions." <em><extracted-citation case-ids="6167798" index="105" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6167798" index="105" url="https://cite.case.law/us/392/1/#p21"> at 13</extracted-citation>, <extracted-citation case-ids="6167798" index="106" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. When courts admit only lawfully obtained evidence, they encourage "those who formulate law enforcement polices, and the officers who implement them, to incorporate Fourth Amendment ideals into their value system." <em>Stone v. Powell,</em> <extracted-citation case-ids="6178753" index="107" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U.S. 465</a></span></extracted-citation>, 492, <extracted-citation case-ids="6178753" index="108" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">96 S.Ct. 3037</a></span></extracted-citation>, <extracted-citation case-ids="6178753" index="109" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">49 L.Ed.2d 1067</a></span></extracted-citation> (1976). But when courts admit illegally obtained evidence as well, they reward "manifest neglect if not an open defiance of the prohibitions of the <a class="page-label" data-citation-index="1" data-label="2066" href="#p2066" id="p2066">*2066</a>Constitution." <em>Weeks,</em> <extracted-citation case-ids="3672825" index="110" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S., at 394</a></span></extracted-citation>, <extracted-citation case-ids="3672825" index="111" url="https://cite.case.law/us/232/383/#p392"><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span></extracted-citation>.</p>
<p id="p-55">Applying the exclusionary rule, the Utah Supreme Court correctly decided that Strieff's drugs must be excluded because the officer exploited his illegal stop to discover them. The officer found the drugs only after learning of Strieff's traffic violation; and he learned of Strieff's traffic violation only because he unlawfully stopped Strieff to check his driver's license.</p>
<p id="p-56">The court also correctly rejected the State's argument that the officer's discovery of a traffic warrant unspoiled the poisonous fruit. The State analogizes finding the warrant to one of our earlier decisions, <em>Wong Sun v. United States</em> . There, an officer illegally arrested a person who, days later, voluntarily returned to the station to confess to committing a crime. <extracted-citation case-ids="450611" index="112" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U.S., at 491</a></span></extracted-citation>, <extracted-citation case-ids="450611" index="113" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>. Even though the person would not have confessed "but for the illegal actions of the police," <em><extracted-citation case-ids="450611" index="114" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="450611" index="114" url="https://cite.case.law/us/371/471/#p488"> at 488</extracted-citation>, <extracted-citation case-ids="450611" index="115" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation> we noted that the police did not exploit their illegal arrest to obtain the confession, <em><extracted-citation case-ids="450611" index="116" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="450611" index="116" url="https://cite.case.law/us/371/471/#p488"> at 491</extracted-citation>, <extracted-citation case-ids="450611" index="117" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation><em>.</em> Because the confession was obtained by "means sufficiently distinguishable" from the constitutional violation, we held that it could be admitted into evidence. <em><extracted-citation case-ids="450611" index="118" url="https://cite.case.law/us/371/471/#p488">Id.,</extracted-citation></em><extracted-citation case-ids="450611" index="118" url="https://cite.case.law/us/371/471/#p488"> at 488, 491</extracted-citation>, <extracted-citation case-ids="450611" index="119" url="https://cite.case.law/us/371/471/#p488"><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">83 S.Ct. 407</a></span></extracted-citation>. The State contends that the search incident to the warrant-arrest here is similarly distinguishable from the illegal stop.</p>
<p id="p-57">But <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></em> explains why Strieff's drugs must be excluded. We reasoned that a Fourth Amendment violation may not color every investigation that follows but it certainly stains the actions of officers who exploit the infraction. We distinguished evidence obtained by innocuous means from evidence obtained by exploiting misconduct after considering a variety of factors: whether a long time passed, whether there were "intervening circumstances," and whether the purpose or flagrancy of the misconduct was "calculated" to procure the evidence. <em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="120" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, 603-604, <extracted-citation case-ids="9639" index="121" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="122" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975).</p>
<p id="p-58">These factors confirm that the officer in this case discovered Strieff's drugs by exploiting his own illegal conduct. The officer did not ask Strieff to volunteer his name only to find out, days later, that Strieff had a warrant against him. The officer illegally stopped Strieff and immediately ran a warrant check. The officer's discovery of a warrant was not some intervening surprise that he could not have anticipated. Utah lists over 180,000 misdemeanor warrants in its database, and at the time of the arrest, Salt Lake County had a "backlog of outstanding warrants" so large that it faced the "potential for civil liability." See Dept. of Justice, Bureau of Justice Statistics, Survey of State Criminal History Information Systems, 2014 (2015) (Systems Survey) (Table 5a), online at https://www.ncjrs.gov/pdffiles1/bjs/grants/249799.pdf (all Internet materials as last visited June 16, 2016); Inst. for Law and Policy Planning, Salt Lake County Criminal Justice System Assessment 6.7 (2004), online at http://www.slco.org/cjac/resources/SaltLakeCJSAfinal.pdf. The officer's violation was also calculated to procure evidence. His sole reason for stopping Strieff, he acknowledged, was investigative-he wanted to discover whether drug activity was going on in the house Strieff had just exited. App. 17.</p>
<p id="p-59">The warrant check, in other words, was not an "intervening circumstance" separating the stop from the search for drugs. It was part and parcel of the officer's illegal "expedition for evidence in the hope that something might turn up." <em>Brown,</em> <extracted-citation case-ids="9639" index="123" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 605</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="124" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Under our precedents, because the officer found Strieff's drugs by exploiting his own constitutional <a class="page-label" data-citation-index="1" data-label="2067" href="#p2067" id="p2067">*2067</a>violation, the drugs should be excluded.</p>
<p id="p-60">III</p>
<p id="p-61">A</p>
<p id="p-62">The Court sees things differently. To the Court, the fact that a warrant gives an officer cause to arrest a person severs the connection between illegal policing and the resulting discovery of evidence. <em>Ante,</em> at 2062-2063. This is a remarkable proposition: The mere existence of a warrant not only gives an officer legal cause to arrest and search a person, it also forgives an officer who, with no knowledge of the warrant at all, unlawfully stops that person on a whim or hunch.</p>
<p id="p-63">To explain its reasoning, the Court relies on <em>Segura v. United States,</em> <extracted-citation case-ids="11340278" index="125" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U.S. 796</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="126" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>, <extracted-citation case-ids="11340278" index="127" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">82 L.Ed.2d 599</a></span></extracted-citation> (1984). There, federal agents applied for a warrant to search an apartment but illegally entered the apartment to secure it before the judge issued the warrant. <em><extracted-citation case-ids="11340278" index="128" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="128" url="https://cite.case.law/us/468/796/#p804"> at 800-801</extracted-citation>, <extracted-citation case-ids="11340278" index="129" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. After receiving the warrant, the agents then searched the apartment for drugs. <em><extracted-citation case-ids="11340278" index="130" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="130" url="https://cite.case.law/us/468/796/#p804"> at 801</extracted-citation>, <extracted-citation case-ids="11340278" index="131" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>. The question before us was what to do with the evidence the agents then discovered. We declined to suppress it because "[t]he illegal entry into petitioners' apartment did not contribute in any way to discovery of the evidence seized under the warrant." <em><extracted-citation case-ids="11340278" index="132" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11340278" index="132" url="https://cite.case.law/us/468/796/#p804"> at 815</extracted-citation>, <extracted-citation case-ids="11340278" index="133" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-64">According to the majority, <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> involves facts "similar" to this case and "suggest[s]" that a valid warrant will clean up whatever illegal conduct uncovered it. <em>Ante,</em> at 2062 - 2063. It is difficult to understand this interpretation. In <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span>,</em> the agents' illegal conduct in entering the apartment had nothing to do with their procurement of a search warrant. Here, the officer's illegal conduct in stopping Strieff was essential to his discovery of an arrest warrant. <em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">Segura</a></span></em> would be similar only if the agents used information they illegally obtained from the apartment to procure a search warrant or discover an arrest warrant. Precisely because that was not the case, the Court admitted the untainted evidence. 468 U.S., at 814, <extracted-citation case-ids="11340278" index="134" url="https://cite.case.law/us/468/796/#p804"><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">104 S.Ct. 3380</a></span></extracted-citation>.</p>
<p id="p-65">The majority likewise misses the point when it calls the warrant check here a " 'negligibly burdensome precautio[n]' " taken for the officer's "safety." <em>Ante,</em> at 2063 (quoting <em><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Rodriguez</a></span>,</em> 575 U.S., at ----, <extracted-citation case-ids="12588788" index="135" url="https://cite.case.law/s-ct/135/1609/#p1616">135 S.Ct., at </extracted-citation>1615 ). Remember, the officer stopped Strieff without suspecting him of committing any crime. By his own account, the officer did not fear Strieff. Moreover, the safety rationale we discussed in <em><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Rodriguez</a></span>,</em> an opinion about highway patrols, is conspicuously absent here. A warrant check on a highway "ensur[es] that vehicles on the road are operated safely and responsibly." <em><extracted-citation case-ids="12588788" index="136" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12588788" index="137" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct., at 1615</a></span></extracted-citation>. We allow such checks during legal traffic stops because the legitimacy of a person's driver's license has a "close connection to roadway safety." <em><extracted-citation case-ids="12588788" index="138" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12588788" index="139" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">135 S.Ct., at 1615</a></span></extracted-citation>. A warrant check of a pedestrian on a sidewalk, "by contrast, is a measure aimed at 'detect[ing] evidence of ordinary criminal wrongdoing.' " <em><extracted-citation case-ids="12588788" index="140" url="https://cite.case.law/s-ct/135/1609/#p1616"><span class="citation" data-id="9806947"><a href="/opinion/2795278/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">Ibid.</a></span></extracted-citation></em> (quoting <em>Indianapolis v. Edmond,</em> <extracted-citation case-ids="9505377" index="141" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32</a></span></extracted-citation>, 40-41, <extracted-citation case-ids="9505377" index="142" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span></extracted-citation>, <extracted-citation case-ids="9505377" index="143" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span></extracted-citation> (2000) ). Surely we would not allow officers to warrant-check random joggers, dog walkers, and lemonade vendors just to ensure they pose no threat to anyone else.</p>
<p id="p-66">The majority also posits that the officer could not have exploited his illegal conduct because he did not violate the Fourth Amendment on purpose. Rather, he made "good-faith mistakes." <em>Ante,</em> at 2063. Never mind that the officer's sole purpose was to fish for evidence. The majority casts his unconstitutional actions as "negligent"</p>
<p id="p-67"><a class="page-label" data-citation-index="1" data-label="2068" href="#p2068" id="p2068">*2068</a>and therefore incapable of being deterred by the exclusionary rule. <em><extracted-citation case-ids="9505377" index="144" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Ibid.</a></span></extracted-citation></em></p>
<p id="p-68">But the Fourth Amendment does not tolerate an officer's unreasonable searches and seizures just because he did not know any better. Even officers prone to negligence can learn from courts that exclude illegally obtained evidence. <em>Stone,</em> <extracted-citation case-ids="6178753" index="145" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U.S., at 492</a></span></extracted-citation>, <extracted-citation case-ids="6178753" index="146" url="https://cite.case.law/us/428/465/#p492"><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">96 S.Ct. 3037</a></span></extracted-citation>. Indeed, they are perhaps the most in need of the education, whether by the judge's opinion, the prosecutor's future guidance, or an updated manual on criminal procedure. If the officers are in doubt about what the law requires, exclusion gives them an "incentive to err on the side of constitutional behavior." <em>United States v. Johnson,</em> <extracted-citation case-ids="6191611" index="147" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U.S. 537</a></span></extracted-citation>, 561, <extracted-citation case-ids="6191611" index="148" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">102 S.Ct. 2579</a></span></extracted-citation>, <extracted-citation case-ids="6191611" index="149" url="https://cite.case.law/us/457/537/#p561"><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">73 L.Ed.2d 202</a></span></extracted-citation> (1982).</p>
<p id="p-69">B</p>
<p id="p-70">Most striking about the Court's opinion is its insistence that the event here was "isolated," with "no indication that this unlawful stop was part of any systemic or recurrent police misconduct." <em>Ante,</em> at 2063. Respectfully, nothing about this case is isolated.</p>
<p id="p-71">Outstanding warrants are surprisingly common. When a person with a traffic ticket misses a fine payment or court appearance, a court will issue a warrant. See, <em>e.g.,</em> Brennan Center for Justice, Criminal Justice Debt 23 (2010), online at https://www.brennancenter.org/sites/default/files/legacy/Fees% 20and% 20Fines% 20FINAL.pdf. When a person on probation drinks alcohol or breaks curfew, a court will issue a warrant. See, <em>e.g.,</em> Human Rights Watch, Profiting from Probation 1, 51 (2014), online at https://www.hrw.org/report/2014/02/05/profiting-probation/americas-offender-funded-probation-industry. The States and Federal Government maintain databases with over 7.8 million outstanding warrants, the vast majority of which appear to be for minor offenses. See Systems Survey (Table 5a). Even these sources may not track the "staggering" numbers of warrants, " 'drawers and drawers' " full, that many cities issue for traffic violations and ordinance infractions. Dept. of Justice, Civil Rights Div., Investigation of the Ferguson Police Department 47, 55 (2015) (Ferguson Report), online at https://www.justice.gov/sites/default/files/opa/press-releases/attachments/2015/03/04/ferguson_police_department_report.pdf. The county in this case has had a "backlog" of such warrants. See <em>supra,</em> at 2066. The Department of Justice recently reported that in the town of Ferguson, Missouri, with a population of 21,000, 16,000 people had outstanding warrants against them. Ferguson Report, at 6, 55.</p>
<p id="p-72">Justice Department investigations across the country have illustrated how these astounding numbers of warrants can be used by police to stop people without cause. In a single year in New Orleans, officers "made nearly 60,000 arrests, of which about 20,000 were of people with outstanding traffic or misdemeanor warrants from neighboring parishes for such infractions as unpaid tickets." Dept. of Justice, Civil Rights Div., Investigation of the New Orleans Police Department 29 (2011), online at https://www.justice.gov/sites/default/files/crt/legacy/2011/03/17/nopd_report.pdf. In the St. Louis metropolitan area, officers "routinely" stop people-on the street, at bus stops, or even in court-for no reason other than "an officer's desire to check whether the subject had a municipal arrest warrant pending." Ferguson Report, at 49, 57<em>.</em> In Newark, New Jersey, officers stopped 52,235 pedestrians within a 4-year period and ran warrant checks on 39,308 of them. Dept. of Justice, Civil Rights Div., Investigation of the Newark Police Department 8, 19, n. 15 <a class="page-label" data-citation-index="1" data-label="2069" href="#p2069" id="p2069">*2069</a>(2014), online at https://www.justice.gov/sites/default/files/crt/legacy/2014/07/22/newark_ findings_7-22-14.pdf. The Justice Department analyzed these warrant-checked stops and reported that "approximately 93% of the stops would have been considered unsupported by articulated reasonable suspicion." <em>Id.,</em> at 9, n. 7.</p>
<p id="p-73">I do not doubt that most officers act in "good faith" and do not set out to break the law. That does not mean these stops are "isolated instance[s] of negligence," however. <em>Ante,</em> at 2063. Many are the product of institutionalized training procedures. The New York City Police Department long trained officers to, in the words of a District Judge, "stop and question first, develop reasonable suspicion later." <em>Ligon v. New York,</em> <extracted-citation case-ids="4328781" index="150" url="https://cite.case.law/f-supp-2d/925/478/#p537"><span class="citation" data-id="8706198"><a href="/opinion/8723002/ligon-v-city-of-new-york/" aria-description="Citation for case: Ligon v. City of New York">925 F.Supp.2d 478</a></span></extracted-citation>, 537-538 (S.D.N.Y.), stay granted on other grounds, <extracted-citation case-ids="3726977" index="151" url="https://cite.case.law/f3d/736/118/"><span class="citation" data-id="8412659"><a href="/opinion/8441531/ligon-ex-rel-jg-v-city-of-new-york/" aria-description="Citation for case: Ligon ex rel. J.G. v. City of New York">736 F.3d 118</a></span></extracted-citation> (C.A.2 2013). The Utah Supreme Court described as " 'routine procedure' or 'common practice' " the decision of Salt Lake City police officers to run warrant checks on pedestrians they detained without reasonable suspicion. <em>State v. Topanotes,</em> <extracted-citation case-ids="9096354" index="152" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">2003 UT 30</a></span></extracted-citation>, ¶ 2, <extracted-citation case-ids="9096354" index="153" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">76 P.3d 1159</a></span></extracted-citation>, 1160. In the related context of traffic stops, one widely followed police manual instructs officers looking for drugs to "run at least a warrants check on all drivers you stop. Statistically, narcotics offenders are ... more likely to fail to appear on simple citations, such as traffic or trespass violations, leading to the issuance of bench warrants. Discovery of an outstanding warrant gives you cause for an immediate custodial arrest and search of the suspect." C. Remsberg, Tactics for Criminal Patrol 205-206 (1995); C. Epp et al., Pulled Over 23, 33-36 (2014).</p>
<p id="p-74">The majority does not suggest what makes this case "isolated" from these and countless other examples. Nor does it offer guidance for how a defendant can prove that his arrest was the result of "widespread" misconduct. Surely it should not take a federal investigation of Salt Lake County before the Court would protect someone in Strieff's position.</p>
<p id="p-75">IV</p>
<p id="p-76">Writing only for myself, and drawing on my professional experiences, I would add that unlawful "stops" have severe consequences much greater than the inconvenience suggested by the name. This Court has given officers an array of instruments to probe and examine you. When we condone officers' use of these devices without adequate cause, we give them reason to target pedestrians in an arbitrary manner. We also risk treating members of our communities as second-class citizens.</p>
<p id="p-77">Although many Americans have been stopped for speeding or jaywalking, few may realize how degrading a stop can be when the officer is looking for more. This Court has allowed an officer to stop you for whatever reason he wants-so long as he can point to a pretextual justification after the fact. <em>Whren v. United States,</em> <extracted-citation case-ids="11746960" index="154" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span></extracted-citation>, 813, <extracted-citation case-ids="11746960" index="155" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S.Ct. 1769</a></span></extracted-citation>, <extracted-citation case-ids="11746960" index="156" url="https://cite.case.law/us/517/806/#p813"><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L.Ed.2d 89</a></span></extracted-citation> (1996). That justification must provide specific reasons why the officer suspected you were breaking the law, <em>Terry,</em> <extracted-citation case-ids="6167798" index="157" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 21</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="158" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation> but it may factor in your ethnicity, <em>United States v. Brignoni-Ponce,</em> <extracted-citation case-ids="9550" index="159" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span></extracted-citation>, 886-887, <extracted-citation case-ids="9550" index="160" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">95 S.Ct. 2574</a></span></extracted-citation>, <extracted-citation case-ids="9550" index="161" url="https://cite.case.law/us/422/873/#p886"><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">45 L.Ed.2d 607</a></span></extracted-citation> (1975), where you live, <em>Adams v. Williams,</em> <extracted-citation case-ids="9137003" index="162" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U.S. 143</a></span></extracted-citation>, 147, <extracted-citation case-ids="9137003" index="163" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">92 S.Ct. 1921</a></span></extracted-citation>, <extracted-citation case-ids="9137003" index="164" url="https://cite.case.law/us/407/143/#p147"><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">32 L.Ed.2d 612</a></span></extracted-citation> (1972), what you were wearing, <em>United States v. Sokolow,</em> <extracted-citation case-ids="605100" index="165" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U.S. 1</a></span></extracted-citation>, 4-5, <extracted-citation case-ids="605100" index="166" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">109 S.Ct. 1581</a></span></extracted-citation>, <extracted-citation case-ids="605100" index="167" url="https://cite.case.law/us/490/1/#p4"><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">104 L.Ed.2d 1</a></span></extracted-citation> (1989), and how you behaved, <em>Illinois v. Wardlow,</em> <extracted-citation case-ids="9476180" index="168" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">528 U.S. 119</a></span></extracted-citation>, 124-125, <extracted-citation case-ids="9476180" index="169" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">120 S.Ct. 673</a></span></extracted-citation>, <extracted-citation case-ids="9476180" index="170" url="https://cite.case.law/us/528/119/#p124"><span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/" aria-description="Citation for case: Illinois v. Wardlow">145 L.Ed.2d 570</a></span></extracted-citation> (2000). The officer does not even need to know which law you might have broken so long as he can later point to any possible infraction-even one that is minor, unrelated, or ambiguous. <em>Devenpeck v. Alford,</em> <a class="page-label" data-citation-index="1" data-label="2070" href="#p2070" id="p2070">*2070</a><extracted-citation case-ids="5916678" index="171" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146</a></span></extracted-citation>, 154-155, <extracted-citation case-ids="5916678" index="172" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S.Ct. 588</a></span></extracted-citation>, <extracted-citation case-ids="5916678" index="173" url="https://cite.case.law/us/543/146/#p154"><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L.Ed.2d 537</a></span></extracted-citation> (2004) ; <em>Heien v. North Carolina,</em> 574 U.S. ----, <extracted-citation case-ids="12593411" index="174" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">135 S.Ct. 530</a></span></extracted-citation>, <extracted-citation case-ids="12593411" index="175" url="https://cite.case.law/s-ct/135/530/"><span class="citation" data-id="9805193"><a href="/opinion/2760668/heien-v-north-carolina/" aria-description="Citation for case: Heien v. North Carolina">190 L.Ed.2d 475</a></span></extracted-citation> (2014).</p>
<p id="p-78">The indignity of the stop is not limited to an officer telling you that you look like a criminal. See Epp, Pulled Over, at 5. The officer may next ask for your "consent" to inspect your bag or purse without telling you that you can decline. See <em>Florida v. Bostick,</em> <extracted-citation case-ids="1108039" index="176" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">501 U.S. 429</a></span></extracted-citation>, 438, <extracted-citation case-ids="1108039" index="177" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">111 S.Ct. 2382</a></span></extracted-citation>, <extracted-citation case-ids="1108039" index="178" url="https://cite.case.law/us/501/429/#p434"><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/" aria-description="Citation for case: Florida v. Bostick">115 L.Ed.2d 389</a></span></extracted-citation> (1991). Regardless of your answer, he may order you to stand "helpless, perhaps facing a wall with [your] hands raised." <em>Terry,</em> <extracted-citation case-ids="6167798" index="179" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S., at 17</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="180" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>. If the officer thinks you might be dangerous, he may then "frisk" you for weapons. This involves more than just a pat down. As onlookers pass by, the officer may " 'feel with sensitive fingers every portion of [your] body. A thorough search [may] be made of [your] arms and armpits, waistline and back, the groin and area about the testicles, and entire surface of the legs down to the feet.' " <em><extracted-citation case-ids="6167798" index="181" url="https://cite.case.law/us/392/1/#p21">Id.,</extracted-citation></em><extracted-citation case-ids="6167798" index="181" url="https://cite.case.law/us/392/1/#p21"> at 17, n. 13</extracted-citation>, <extracted-citation case-ids="6167798" index="182" url="https://cite.case.law/us/392/1/#p21"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>.</p>
<p id="p-79">The officer's control over you does not end with the stop. If the officer chooses, he may handcuff you and take you to jail for doing nothing more than speeding, jaywalking, or "driving [your] pickup truck ... with [your] 3-year-old son and 5-year-old daughter ... without [your] seatbelt fastened." <em>Atwater v. Lago Vista,</em> <extracted-citation case-ids="9301256" index="183" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span></extracted-citation>, 323-324, <extracted-citation case-ids="9301256" index="184" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">121 S.Ct. 1536</a></span></extracted-citation>, <extracted-citation case-ids="9301256" index="185" url="https://cite.case.law/us/532/318/#p323"><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">149 L.Ed.2d 549</a></span></extracted-citation> (2001). At the jail, he can fingerprint you, swab DNA from the inside of your mouth, and force you to "shower with a delousing agent" while you "lift [your] tongue, hold out [your] arms, turn around, and lift [your] genitals." <em>Florence v. Board of Chosen Freeholders of County of Burlington,</em> 566 U.S. ----, ---- - ----, <extracted-citation case-ids="12189139" index="186" url="https://cite.case.law/us/566/318/#p1514"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">132 S.Ct. 1510</a></span></extracted-citation>, 1514, <extracted-citation case-ids="12189139" index="187" url="https://cite.case.law/us/566/318/#p1514"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">182 L.Ed.2d 566</a></span></extracted-citation> (2012) ; <em>Maryland v. King,</em> 569 U.S. ----, ----, <extracted-citation case-ids="12697054" index="188" url="https://cite.case.law/us/569/435/#p1980"><span class="citation" data-id="873669"><a href="/opinion/873669/maryland-v-king/" aria-description="Citation for case: Maryland v. King">133 S.Ct. 1958</a></span></extracted-citation>, 1980, <extracted-citation case-ids="12697054" index="189" url="https://cite.case.law/us/569/435/#p1980"><span class="citation" data-id="873669"><a href="/opinion/873669/maryland-v-king/" aria-description="Citation for case: Maryland v. King">186 L.Ed.2d 1</a></span></extracted-citation> (2013). Even if you are innocent, you will now join the 65 million Americans with an arrest record and experience the "civil death" of discrimination by employers, landlords, and whoever else conducts a background check. Chin, The New Civil Death, <extracted-citation index="190" url="https://cite.case.law/citations/?q=160%20U.%20Pa.%20L.%20Rev.%201789"><span class="citation no-link">160 U. Pa. L. Rev. 1789</span></extracted-citation>, 1805 (2012) ; see J. Jacobs, The Eternal Criminal Record 33-51 (2015); Young &amp; Petersilia, Keeping Track, <extracted-citation index="191" url="https://cite.case.law/citations/?q=129%20Harv.%20L.%20Rev.%201318"><span class="citation no-link">129 Harv. L. Rev. 1318</span></extracted-citation>, 1341-1357 (2016). And, of course, if you fail to pay bail or appear for court, a judge will issue a warrant to render you "arrestable on sight" in the future. A. Goffman, On the Run 196 (2014).</p>
<p id="p-80">This case involves a <em>suspicionless</em> stop, one in which the officer initiated this chain of events without justification. As the Justice Department notes, <em><extracted-citation case-ids="9096354" index="192" url="https://cite.case.law/p3d/76/1159/">supra,</extracted-citation></em> at 2068 - 2069, many innocent people are subjected to the humiliations of these unconstitutional searches. The white defendant in this case shows that anyone's dignity can be violated in this manner. See M. Gottschalk, Caught 119-138 (2015). But it is no secret that people of color are disproportionate victims of this type of scrutiny. See M. Alexander, The New Jim Crow 95-136 (2010). For generations, black and brown parents have given their children "the talk"-instructing them never to run down the street; always keep your hands where they can be seen; do not even think of talking back to a stranger-all out of fear of how an officer with a gun will react to them. See, <em>e.g.,</em> W.E.B. Du Bois, The Souls of Black Folk (1903); J. Baldwin, The Fire Next Time (1963); T. Coates, Between the World and Me (2015).</p>
<p id="p-81">By legitimizing the conduct that produces this double consciousness, this case tells everyone, white and black, guilty and innocent, that an officer can verify your legal status at any time. It says that your body is subject to invasion while courts excuse the violation of your rights. It <a class="page-label" data-citation-index="1" data-label="2071" href="#p2071" id="p2071">*2071</a>implies that you are not a citizen of a democracy but the subject of a carceral state, just waiting to be cataloged.</p>
<p id="p-82">We must not pretend that the countless people who are routinely targeted by police are "isolated." They are the canaries in the coal mine whose deaths, civil and literal, warn us that no one can breathe in this atmosphere. See L. Guinier &amp; G. Torres, The Miner's Canary 274-283 (2002). They are the ones who recognize that unlawful police stops corrode all our civil liberties and threaten all our lives. Until their voices matter too, our justice system will continue to be anything but.</p>
<p id="p-83">* * *</p>
<p id="p-84">I dissent.</p>
<p id="p-85">Justice KAGAN, with whom Justice GINSBURG joins, dissenting.</p>
<p id="p-86">If a police officer stops a person on the street without reasonable suspicion, that seizure violates the Fourth Amendment. And if the officer pats down the unlawfully detained individual and finds drugs in his pocket, the State may not use the contraband as evidence in a criminal prosecution. That much is beyond dispute. The question here is whether the prohibition on admitting evidence dissolves if the officer discovers, after making the stop but before finding the drugs, that the person has an outstanding arrest warrant. Because that added wrinkle makes no difference under the Constitution, I respectfully dissent.</p>
<p id="p-87">This Court has established a simple framework for determining whether to exclude evidence obtained through a Fourth Amendment violation: Suppression is necessary when, but only when, its societal benefits outweigh its costs. See <em>ante,</em> at 2060 - 2061; <em>Davis v. United States,</em> <extracted-citation case-ids="5928256,12450488" index="193" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S. 229</a></span></extracted-citation>, 237, <extracted-citation case-ids="5928256,12450488" index="194" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>, <extracted-citation case-ids="12450488,5928256" index="195" url="https://cite.case.law/l-ed-2d/180/285/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">180 L.Ed.2d 285</a></span></extracted-citation> (2011). The exclusionary rule serves a crucial function-to deter unconstitutional police conduct. By barring the use of illegally obtained evidence, courts reduce the temptation for police officers to skirt the Fourth Amendment's requirements. See <em>James v. Illinois,</em> <extracted-citation case-ids="11331446" index="196" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">493 U.S. 307</a></span></extracted-citation>, 319, <extracted-citation case-ids="11331446" index="197" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">110 S.Ct. 648</a></span></extracted-citation>, <extracted-citation case-ids="11331446" index="198" url="https://cite.case.law/us/493/307/#p319"><span class="citation" data-id="9431873"><a href="/opinion/112350/james-v-illinois/" aria-description="Citation for case: James v. Illinois">107 L.Ed.2d 676</a></span></extracted-citation> (1990). But suppression of evidence also "exacts a heavy toll": Its consequence in many cases is to release a criminal without just punishment. <em>Davis,</em> <extracted-citation case-ids="5928256,12450488" index="199" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">564 U.S., at 237</a></span></extracted-citation>, <extracted-citation case-ids="5928256,12450488" index="200" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">131 S.Ct. 2419</a></span></extracted-citation>. Our decisions have thus endeavored to strike a sound balance between those two competing considerations-rejecting the "reflexive" impulse to exclude evidence every time an officer runs afoul of the Fourth Amendment, <em><extracted-citation case-ids="5928256,12450488" index="201" url="https://cite.case.law/us/564/229/"><span class="citation" data-id="7263677"><a href="/opinion/7345713/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">id.,</a></span></extracted-citation></em><extracted-citation case-ids="5928256,12450488" index="201" url="https://cite.case.law/us/564/229/"> at 238</extracted-citation>, <extracted-citation case-ids="5928256,12450488" index="202" url="https://cite.case.law/us/564/229/"><span class="citation multiple-matches"><a href="/c/S.Ct./131/2419/">131 S.Ct. 2419</a></span></extracted-citation> but insisting on suppression when it will lead to "appreciable deterrence" of police misconduct, <em>Herring v. United States,</em> <extracted-citation case-ids="3679252" index="203" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">555 U.S. 135</a></span></extracted-citation>, 141, <extracted-citation case-ids="3679252" index="204" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">129 S.Ct. 695</a></span></extracted-citation>, <extracted-citation case-ids="3679252" index="205" url="https://cite.case.law/us/555/135/#p141"><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">172 L.Ed.2d 496</a></span></extracted-citation> (2009).</p>
<p id="p-88">This case thus requires the Court to determine whether excluding the fruits of Officer Douglas Fackrell's unjustified stop of Edward Strieff would significantly deter police from committing similar constitutional violations in the future. And as the Court states, that inquiry turns on application of the "attenuation doctrine," <em>ante,</em> at 2061 - 2062-our effort to "mark the point" at which the discovery of evidence "become[s] so attenuated" from the police misconduct that the deterrent benefit of exclusion drops below its cost. <em>United States v. Leon,</em> <extracted-citation case-ids="11340969" index="206" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U.S. 897</a></span></extracted-citation>, 911, <extracted-citation case-ids="11340969" index="207" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">104 S.Ct. 3405</a></span></extracted-citation>, <extracted-citation case-ids="11340969" index="208" url="https://cite.case.law/us/468/897/#p920"><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">82 L.Ed.2d 677</a></span></extracted-citation> (1984). Since <em>Brown v. Illinois,</em> <extracted-citation case-ids="9639" index="209" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span></extracted-citation>, 604-605, <extracted-citation case-ids="9639" index="210" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="211" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">45 L.Ed.2d 416</a></span></extracted-citation> (1975), three factors have guided that analysis. First, the closer the "temporal proximity" between the unlawful act and the discovery of evidence, the greater the deterrent value of suppression. <em><extracted-citation case-ids="9639" index="212" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="212" url="https://cite.case.law/us/422/590/"> at 603</extracted-citation>, <extracted-citation case-ids="9639" index="213" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Second, the more "purpose[ful]" or "flagran[t]" the police illegality, the clearer the necessity, and better the chance, of preventing similar misbehavior. <em><extracted-citation case-ids="9639" index="214" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="214" url="https://cite.case.law/us/422/590/"> at 604</extracted-citation>, <extracted-citation case-ids="9639" index="215" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>.</p>
<p id="p-89"><a class="page-label" data-citation-index="1" data-label="2072" href="#p2072" id="p2072">*2072</a>And third, the presence (or absence) of "intervening circumstances" makes a difference: The stronger the causal chain between the misconduct and the evidence, the more exclusion will curb future constitutional violations. <em><extracted-citation case-ids="9639" index="216" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="9639" index="216" url="https://cite.case.law/us/422/590/"> at 603-604</extracted-citation>, <extracted-citation case-ids="9639" index="217" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation>. Here, as shown below, each of those considerations points toward suppression: Nothing in Fackrell's discovery of an outstanding warrant so attenuated the connection between his wrongful behavior and his detection of drugs as to diminish the exclusionary rule's deterrent benefits.</p>
<p id="p-90">Start where the majority does: The temporal proximity factor, it forthrightly admits, "favors suppressing the evidence." <em>Ante,</em> at 2062. After all, Fackrell's discovery of drugs came just minutes after the unconstitutional stop. And in prior decisions, this Court has made clear that only the lapse of "substantial time" between the two could favor admission. <em>Kaupp v. Texas,</em> <extracted-citation case-ids="9031233" index="218" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">538 U.S. 626</a></span></extracted-citation>, 633, <extracted-citation case-ids="9031233" index="219" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">123 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="9031233" index="220" url="https://cite.case.law/us/538/626/#p633"><span class="citation" data-id="127919"><a href="/opinion/127919/kaupp-v-texas/" aria-description="Citation for case: Kaupp v. Texas">155 L.Ed.2d 814</a></span></extracted-citation> (2003) (<em>per curiam</em> ); see, <em>e.g.,</em> <em>Brown,</em> <extracted-citation case-ids="9639" index="221" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S., at 604</a></span></extracted-citation>, <extracted-citation case-ids="9639" index="222" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation> (suppressing a confession when "less than two hours" separated it from an unlawful arrest). So the State, by all accounts, takes strike one.</p>
<p id="p-91">Move on to the purposefulness of Fackrell's conduct, where the majority is less willing to see a problem for what it is. The majority chalks up Fackrell's Fourth Amendment violation to a couple of innocent "mistakes." <em>Ante,</em> at 2063. But far from a Barney Fife-type mishap, Fackrell's seizure of Strieff was a calculated decision, taken with so little justification that the State has never tried to defend its legality. At the suppression hearing, Fackrell acknowledged that the stop was designed for investigatory purposes-<em>i.e.,</em> to "find out what was going on [in] the house" he had been watching, and to figure out "what [Strieff] was doing there." App. 17-18. And Fackrell frankly admitted that he had no basis for his action except that Strieff "was coming out of the house." <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Id.,</a></span></em> at 17<em>.</em> Plug in Fackrell's and Strieff's names, substitute "stop" for "arrest" and "reasonable suspicion" for "probable cause," and this Court's decision in <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></em> perfectly describes this case:</p>
<blockquote id="p-92">"[I]t is not disputed that [Fackrell stopped Strieff] without [reasonable suspicion]. [He] later testified that [he] made the [stop] for the purpose of questioning [Strieff] as part of [his] investigation.... The illegality here ... had a quality of purposefulness. The impropriety of the [stop] was obvious. [A]wareness of that fact was virtually conceded by [Fackrell] when [he] repeatedly acknowledged, in [his] testimony, that the purpose of [his] action was 'for investigation': [Fackrell] embarked upon this expedition for evidence in the hope that something might turn up." 422 U.S., at 592, 605, <extracted-citation case-ids="9639" index="223" url="https://cite.case.law/us/422/590/"><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">95 S.Ct. 2254</a></span></extracted-citation> (some internal punctuation altered; footnote, citation, and paragraph break omitted).</blockquote>
<p id="p-93">In <em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>,</em> the Court held those facts to support suppression-and they do here as well. Swing and a miss for strike two.</p>
<p id="p-94">Finally, consider whether any intervening circumstance "br[oke] the causal chain" between the stop and the evidence. <em>Ante,</em> at 2062. The notion of such a disrupting event comes from the tort law doctrine of proximate causation. See <em>Bridge v. Phoenix Bond &amp; Indemnity Co.,</em> <extracted-citation case-ids="3674023" index="224" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">553 U.S. 639</a></span></extracted-citation>, 658-659, <extracted-citation case-ids="3674023" index="225" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">128 S.Ct. 2131</a></span></extracted-citation>, <extracted-citation case-ids="3674023" index="226" url="https://cite.case.law/us/553/639/#p658"><span class="citation" data-id="145799"><a href="/opinion/145799/bridge-v-phoenix-bond-indemnity-co/" aria-description="Citation for case: Bridge v. Phoenix Bond &amp; Indemnity Co.">170 L.Ed.2d 1012</a></span></extracted-citation> (2008) (explaining that a party cannot "establish [ ] proximate cause" when "an intervening cause break[s] the chain of causation between" the act and the injury); Kerr, Good Faith, New Law, and the Scope of the Exclusionary Rule, <extracted-citation index="227" url="https://cite.case.law/citations/?q=99%20Geo.%20L.J.%201077">99 Geo. L. J. 1077</extracted-citation>, 1099 (2011) (Fourth Amendment attenuation analysis "looks to <a class="page-label" data-citation-index="1" data-label="2073" href="#p2073" id="p2073">*2073</a>whether the constitutional violation was the proximate cause of the discovery of the evidence"). And as in the tort context, a circumstance counts as intervening only when it is unforeseeable-not when it can be seen coming from miles away. See W. Keeton, D. Dobbs, B. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts 312 (5th ed. 1984). For rather than breaking the causal chain, predictable effects (<em>e.g.,</em> X leads naturally to Y leads naturally to Z) are its very links.</p>
<p id="p-95">And Fackrell's discovery of an arrest warrant-the only event the majority thinks intervened-was an eminently foreseeable consequence of stopping Strieff. As Fackrell testified, checking for outstanding warrants during a stop is the "normal" practice of South Salt Lake City police. App. 18; see also <em>State v. Topanotes,</em> <extracted-citation case-ids="9096354" index="228" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">2003 UT 30</a></span></extracted-citation>, ¶ 2, <extracted-citation case-ids="9096354" index="229" url="https://cite.case.law/p3d/76/1159/"><span class="citation" data-id="2598446"><a href="/opinion/2598446/state-v-topanotes/" aria-description="Citation for case: State v. Topanotes">76 

[...TRUNCATED 5369 of 125369 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Uzuegbunam v. Preczewski.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Uzuegbunam v. Preczewski
type: case
citation: "592 U.S. 279 (2021)"
parallel_cite: "141 S. Ct. 792; 209 L. Ed. 2d 94"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 19-968
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
  opinion_url: "https://www.courtlistener.com/opinion/4861817/uzuegbunam-v-preczewski/"
  cluster_id: 4861817
  opinion_id: null
  identity_checked: true
lake:
  record_id: Uzuegbunam v. Preczewski
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - standing
  - nominal-damages
  - first-amendment
holding: "A plaintiff's request for nominal damages satisfies Article III's redressability requirement where his claim rests on a completed violation of a legal right, so a suit for a past constitutional injury is not moot merely because only nominal damages remain."
---

# Uzuegbunam v. Preczewski

*592 U.S. 279 (2021)* (No. 19-968) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4861817 → opinion 4665596; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "592 U. S. ____ (2021)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Chike Uzuegbunam, a student at Georgia Gwinnett College, was stopped by campus officials from distributing religious literature and later from speaking even within a designated "free speech zone," after officials invoked policies restricting on-campus speech. He and fellow student Joseph Bradford sued college officials under the First Amendment, seeking injunctive relief and nominal damages. The officials discontinued the challenged policies, which mooted the request for injunctive relief, and then argued that the students' remaining request for nominal damages could not by itself sustain standing. The Eleventh Circuit agreed and dismissed the case.

## Issue
Whether a plaintiff who seeks only nominal damages for a completed violation of a constitutional right retains Article III standing to pursue the suit.

## Rule
Article III standing requires a remedy likely to redress the plaintiff's injury. Looking to the forms of relief available at common law, the Court explained that a party whose rights were invaded could always recover nominal damages without proving actual damage, and that nominal damages are "not purely symbolic" but constitute relief on the merits. It therefore held: "Because nominal damages were available at common law in analogous circumstances, we conclude that a request for nominal damages satisfies the redressability element of standing where a plaintiff's claim is based on a completed violation of a legal right." — 592 U.S. 279 (slip op., at 11). ^pin-op

## Application
Uzuegbunam experienced a completed violation of his constitutional rights when the officials enforced the speech policies against him, and nominal damages can redress that past injury even though he did not or could not quantify the harm in economic terms. Redressability was thus satisfied. The Court did not decide whether Bradford, who self-censored rather than being directly enjoined, had likewise suffered a past, completed injury, leaving that question for the District Court.

## Conclusion
The judgment of the Eleventh Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Thomas, J., delivered the opinion of the Court, joined by Breyer, Alito, Sotomayor, Kagan, Gorsuch, Kavanaugh, and Barrett, JJ.; Kavanaugh, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Roberts, C.J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Uzuegbunam* is a standing decision that keeps § 1983 and other constitutional-tort suits for completed violations alive when only nominal damages remain, so a defendant cannot moot accountability by discontinuing the challenged conduct after the injury.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Uzuegbunam v. Preczewski*, 592 U.S. 279 (2021)](https://www.courtlistener.com/opinion/4861817/uzuegbunam-v-preczewski/) — pinpoint: slip op., at 11 (Opinion of the Court, Part III, holding; Thomas, J.). CL carries the slip opinion ("592 U. S. ____ (2021)"; cluster 4861817 → opinion 4665596); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a4e374ea543c1cb3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Uzuegbunam v. Preczewski"}, "payload": {"all": [{"cite": "592 U.S. 279", "page": "279", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "592"}, {"cite": "141 S. Ct. 792", "page": "792", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "209 L. Ed. 2d 94", "page": "94", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "209"}], "display": "592 U.S. 279", "official": {"cite": "592 U.S. 279", "page": "279", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "592"}, "official_selection_present": true, "record_id": "Uzuegbunam v. Preczewski"}}
{"assertion_id": "b90a65fbab54d011", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Uzuegbunam v. Preczewski"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Uzuegbunam v. Preczewski", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Uzuegbunam v. Preczewski

```json
{
  "schema_version": "s2.v1",
  "record_id": "Uzuegbunam v. Preczewski",
  "status": "under_review",
  "identity": {
    "case_name": "Uzuegbunam v. Preczewski",
    "case_name_short": "Uzuegbunam",
    "case_name_full": "",
    "input_case_name": "Uzuegbunam v. Preczewski",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "19-968",
    "cluster_id": 4861817,
    "lead_opinion_id": 4665596,
    "sibling_ids": [],
    "absolute_url": "/opinion/4861817/uzuegbunam-v-preczewski/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 279",
      "volume": "592",
      "reporter": "U.S.",
      "page": "279",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 792",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "792",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 94",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 279",
        "volume": "592",
        "reporter": "U.S.",
        "page": "279",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 792",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "792",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 94",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 279",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 279",
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
    "date_created": "2026-07-06T12:10:07Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "uzuegbunam-v-preczewski--4861817",
      "to_record_id": "Uzuegbunam v. Preczewski",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Uzuegbunam v. Preczewski

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

        UZUEGBUNAM ET AL. v. PRECZEWSKI ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

    No. 19–968.      Argued January 12, 2021—Decided March 8, 2021
Petitioners are former students of Georgia Gwinnett College who wished
  to exercise their religion by sharing their faith on campus while en-
  rolled there. In 2016, Chike Uzuegbunam talked with interested stu-
  dents and handed out religious literature on campus grounds. Uzueg-
  bunam stopped after a campus police officer informed him that campus
  policy prohibited distributing written religious materials outside areas
  designated for that purpose. A college official later explained to Uzueg-
  bunam that he could speak about his religion or distribute materials
  only in two designated speech areas on campus, and even then only
  after securing a permit. But when Uzuegbunam obtained the required
  permit and tried to speak in a free speech zone, a campus police officer
  again asked him to stop, this time saying that people had complained
  about his speech. Campus policy at that time prohibited using the free
  speech zone to say anything that “disturbs the peace and/or comfort of
  person(s).” The officer told Uzuegbunam that his speech violated cam-
  pus policy because it had led to complaints, and the officer threatened
  Uzuegbunam with disciplinary action if he continued. Uzuegbunam
  again complied with the order to stop speaking. Another student who
  shares Uzuegbunam’s faith, Joseph Bradford, decided not to speak
  about religion because of these events. Both Uzuegbunam and Brad-
  ford sued certain college officials charged with enforcement of the col-
  lege’s speech policies, arguing that these policies violated the First
  Amendment. As relevant here, the students sought injunctive relief
  and nominal damages. The college officials ultimately chose to discon-
  tinue the challenged policies rather than to defend them, and they
  sought dismissal on the ground that the policy change left the students
  without standing to sue. The parties agreed that the policy change
  rendered the students’ request for injunctive relief moot, but disputed
2                   UZUEGBUNAM v. PRECZEWSKI

                                  Syllabus

    whether the students had standing to maintain the suit based on their
    remaining claim for nominal damages. The Eleventh Circuit held that
    while a request for nominal damages can sometimes save a case from
    mootness, such as where a person pleads but fails to prove an amount
    of compensatory damages, the students’ plea for nominal damages
    alone could not by itself establish standing.
Held: A request for nominal damages satisfies the redressability element
 necessary for Article III standing where a plaintiff’s claim is based on
 a completed violation of a legal right. Pp. 3–12.
    (a) To establish Article III standing, the Constitution requires a
 plaintiff to identify an injury in fact that is fairly traceable to the chal-
 lenged conduct and to seek a remedy likely to redress that injury.
 Spokeo, Inc. v. Robins, 578 U. S. 330, 338. The dispute here concerns
 whether the remedy Uzuegbunam sought—nominal damages—can re-
 dress the completed constitutional violation that he alleges occurred
 when campus officials enforced the speech policies against him. The
 Court looks to the forms of relief awarded at common law to determine
 whether nominal damages can redress a past injury. The prevailing
 rule at common law was that a party whose rights are invaded can
 always recover nominal damages without furnishing evidence of actual
 damage. By permitting plaintiffs to pursue nominal damages when-
 ever they suffered a personal legal injury, the common law avoided the
 oddity of privileging small economic rights over important, but not eas-
 ily quantifiable, nonpecuniary rights. Pp. 3–8.
    (b) The common law did not require a plea for compensatory dam-
 ages as a prerequisite to an award of nominal damages. Nominal dam-
 ages are not purely symbolic. They are instead the damages awarded
 by default until the plaintiff establishes entitlement to some other
 form of damages. A single dollar often will not provide full redress,
 but the partial remedy satisfies the redressability requirement.
 Church of Scientology of Cal. v. United States, 506 U. S. 9, 13. Re-
 spondents’ argument that a plea for compensatory damages is neces-
 sary to confer jurisdiction also does not square with established prin-
 ciples of standing. And unlike an award of attorney’s fees and costs
 which may be the byproduct of a successful suit, an award of nominal
 damages constitutes relief on the merits. Pp. 8–11.
    (c) A request for redress in the form of nominal damages does not
 guarantee entry to court. In addition to redressability, the plaintiff
 must establish the other elements of standing and satisfy all other rel-
 evant requirements, such as pleading a cognizable cause of action.
 Uzuegbunam experienced a completed violation of his constitutional
 rights when respondents enforced their speech policies against him.
 Nominal damages can redress Uzuegbunam’s injury even if he cannot
 or chooses not to quantify that harm in economic terms. The Court
                      Cite as: 592 U. S. ____ (2021)                     3

                                 Syllabus

  does not decide whether Bradford can pursue nominal damages and
  leaves for the District Court to determine whether Bradford has estab-
  lished a past, completed injury. Pp. 11–12.

781 Fed. Appx. 824, reversed and remanded.

  THOMAS, J., delivered the opinion of the Court, in which BREYER, ALITO,
SOTOMAYOR, KAGAN, GORSUCH, KAVANAUGH, and BARRETT, JJ., joined.
KAVANAUGH, J., filed a concurring opinion. ROBERTS, C. J., filed a dissent-
ing opinion.
                        Cite as: 592 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–968
                                    _________________


    CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
         STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                                  [March 8, 2021]

   JUSTICE THOMAS delivered the opinion of the Court.
   At all stages of litigation, a plaintiff must maintain a per-
sonal interest in the dispute. The doctrine of standing gen-
erally assesses whether that interest exists at the outset,
while the doctrine of mootness considers whether it exists
throughout the proceedings. To demonstrate standing, the
plaintiff must not only establish an injury that is fairly
traceable to the challenged conduct but must also seek a
remedy that redresses that injury. And if in the course of
litigation a court finds that it can no longer provide a plain-
tiff with any effectual relief, the case generally is moot.
This case asks whether an award of nominal damages by
itself can redress a past injury. We hold that it can.
                             I
  According to the complaint, Chike Uzuegbunam is an
evangelical Christian who believes that an important part
of exercising his religion includes sharing his faith. In
2016, Uzuegbunam decided to share his faith at Georgia
Gwinnett College, a public college where he was enrolled as
a student. At an outdoor plaza on campus near the library
2               UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

where students often gather, Uzuegbunam engaged in con-
versations with interested students and handed out reli-
gious literature.
   A campus police officer soon informed Uzuegbunam that
campus policy prohibited distributing written religious ma-
terials in that area and told him to stop. Uzuegbunam com-
plied with the officer’s order. To learn more about this pol-
icy, he then visited the college’s Director of the Office of
Student Integrity, who was directly responsible for promul-
gating and enforcing the policy. When asked if Uzueg-
bunam could continue speaking about his religion if he
stopped distributing materials, the official said no. The of-
ficial explained that Uzuegbunam could speak about his re-
ligion or distribute materials only in two designated “free
speech expression areas,” which together make up just
0.0015 percent of campus. And he could do so only after
securing the necessary permit. Uzuegbunam then applied
for and received a permit to use the free speech zone.
   Twenty minutes after Uzuegbunam began speaking on
the day allowed by his permit, another campus police officer
again told him to stop, this time saying that people had
complained about his speech. Campus policy prohibited us-
ing the free speech zone to say anything that “disturbs the
peace and/or comfort of person(s).” App. to Pet. for Cert.
151(a). The officer told Uzuegbunam that his speech vio-
lated this policy because it had led to complaints. The of-
ficer threatened Uzuegbunam with disciplinary action if he
continued. Uzuegbunam again complied with the order to
stop speaking. Another student who shares Uzuegbunam’s
faith, Joseph Bradford, decided not to speak about religion
because of these events.
   Both students sued a number of college officials in charge
of enforcing the college’s speech policies, arguing that those
policies violated the First Amendment. As relevant here,
they sought nominal damages and injunctive relief. Re-
spondents initially attempted to defend the policy, stating
                  Cite as: 592 U. S. ____ (2021)              3

                      Opinion of the Court

that Uzuegbunam’s discussion of his religion “arguably rose
to the level of ‘fighting words.’ ” Id., at 155(a). But the col-
lege officials quickly abandoned that strategy and instead
decided to get rid of the challenged policies. They then
moved to dismiss, arguing that the suit was moot, because
of the policy change. The students agreed that injunctive
relief was no longer available, but they disagreed that the
case was moot. They contended that their case was still live
because they had also sought nominal damages. The Dis-
trict Court dismissed the case, holding that the students’
claim for nominal damages was insufficient by itself to es-
tablish standing.
   The Eleventh Circuit affirmed. 781 Fed. Appx. 824
(2019). It stated that a request for nominal damages can
save a case from mootness in certain circumstances, such
as where a person pleads but fails to prove an amount of
compensatory damages. But, because the students did not
request compensatory damages, their plea for nominal
damages could not by itself establish standing.
   We granted certiorari to consider whether a plaintiff who
sues over a completed injury and establishes the first two
elements of standing (injury and traceability) can establish
the third by requesting only nominal damages. 591 U. S.
___ (2020). We now reverse.
                               II
   To satisfy the “ ‘irreducible constitutional minimum’ ” of
Article III standing, a plaintiff must not only establish
(1) an injury in fact (2) that is fairly traceable to the chal-
lenged conduct, but he must also seek (3) a remedy that is
likely to redress that injury. Spokeo, Inc. v. Robins, 578
U. S. 330, 338 (2016); see also Gill v. Whitford, 585 U. S.
___, ___–___ (2018) (slip op., at 13–14). There is no dispute
that Uzuegbunam has established the first two elements.
The only question is whether the remedy he sought—nom-
inal damages—can redress the constitutional violation that
4               UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

Uzuegbunam alleges occurred when campus officials en-
forced the speech policies against him.
                                A
   In determining whether nominal damages can redress a
past injury, we look to the forms of relief awarded at com-
mon law. “Article III’s restriction of the judicial power to
‘Cases’ and ‘Controversies’ is properly understood to mean
‘cases and controversies of the sort traditionally amenable
to, and resolved by, the judicial process.’ ” Vermont Agency
of Natural Resources v. United States ex rel. Stevens, 529
U. S. 765, 774 (2000) (quoting Steel Co. v. Citizens for Better
Environment, 523 U. S. 83, 102 (1998)); cf. Memphis Com-
munity School Dist. v. Stachura, 477 U. S. 299, 306 (1986)
(relief for “§1983 plaintiffs . . . is ordinarily determined ac-
cording to principles derived from the common law of
torts”). The parties here agree that courts at common law
routinely awarded nominal damages. They, instead, dis-
pute what kinds of harms those damages could redress.
   Both sides agree that nominal damages historically could
provide prospective relief. The award of nominal damages
was one way for plaintiffs at common law to “obtain a form
of declaratory relief in a legal system with no general de-
claratory judgment act.” D. Laycock & R. Hasen, Modern
American Remedies 636 (5th ed. 2019). For example, a tres-
pass to land or water rights might raise a prospective threat
to a property right by creating the foundation for a future
claim of adverse possession or prescriptive easement.
Blanchard v. Baker, 8 Me. 253, 268 (1832) (“If an unlawful
diversion [of water] is suffered for twenty years, it ripens
into a right, which cannot be controverted”). By obtaining
a declaration of trespass, a property owner could “vindicate
his right by action” and protect against those future
threats. Ibid. Courts at common law would not declare
property boundaries in the abstract, “but the suit for nomi-
nal damages allowed them to do so indirectly.” Laycock,
                  Cite as: 592 U. S. ____ (2021)             5

                      Opinion of the Court

supra, at 636.
  The parties disagree, however, about whether nominal
damages alone could provide retrospective relief. Stressing
the declaratory function, respondents argue that nominal
damages by themselves redressed only continuing or
threatened injury, not past injury.
  But cases at common law paint a different picture. Early
courts required the plaintiff to prove actual monetary dam-
ages in every case: “[I]njuria & damnum [injury and dam-
age] are the two grounds for the having [of] all actions, and
without these, no action lieth.” Cable v. Rogers, 3 Bulst.
311, 312, 81 Eng. Rep. 259 (K. B. 1625). Later courts, how-
ever, reasoned that every legal injury necessarily causes
damage, so they awarded nominal damages absent evi-
dence of other damages (such as compensatory, statutory,
or punitive damages), and they did so where there was no
apparent continuing or threatened injury for nominal dam-
ages to redress. See, e.g., Barker v. Green, 2 Bing. 317, 130
Eng. Rep. 327 (C. P. 1824) (nominal damages awarded for
1-day delay in arrest because “if there was a breach of duty
the law would presume some damage”); Hatch v. Lewis, 2
F. & F. 467, 479, 485–486, 175 Eng. Rep. 1145, 1150, 1153
(N. P. 1861) (ineffective assistance by criminal defense at-
torney that does not prejudice the client); Dods v. Evans, 15
C. B. N. S. 621, 624, 627, 143 Eng. Rep. 929, 930–931 (C. P.
1864) (breach of contract); Marzetti v. Williams, 1 B. & Ad.
415, 417–418, 423–428, 109 Eng. Rep. 842, 843, 845–847
(K. B. 1830) (bank’s 1-day delay in paying on a check); id.,
at 424, 109 Eng. Rep., at 845 (recognizing that breach of
contract could create a continuing injury but determining
that the fact of breach of contract by itself justified nominal
damages).
  The latter approach was followed both before and after
ratification of the Constitution. An early case about voting
rights effectively illustrates this common-law understand-
ing. Faced with a suit pleading denial of the right to vote,
6               UZUEGBUNAM v. PRECZEWSKI

                       Opinion of the Court

the court rejected the plaintiff ’s claim because, among
other reasons, the plaintiff had not established actual dam-
ages. Ashby v. White, 2 Raym. Ld. 938, 941–943, 948, 92
Eng. Rep. 126, 129, 130, 133 (K. B. 1703). Dissenting, Lord
Holt argued that the common law inferred damages when-
ever a legal right was violated. Observing that the law rec-
ognized “not merely pecuniary” injury but also “personal in-
jury,” Lord Holt stated that “every injury imports a
damage” and that a plaintiff could always obtain damages
even if he “does not lose a penny by reason of the [viola-
tion].” Id., at 955, 92 Eng. Rep., at 137. Although Lord Holt
was in the minority, the House of Lords overturned the ma-
jority decision, thus validating Lord Holt’s position, 3 Salk.
17, 91 Eng. Rep. 665 (K. B. 1703), and this principle “laid
down . . . by Lord Holt” was followed “in many subsequent
cases,” Embrey v. Owen, 6 Exch. 353, 368, 155 Eng. Rep.
579, 585 (1851).
   The dissent correctly notes that English courts differed in
some respects from courts under our system, but Lord
Holt’s position also prevailed in courts on this side of the
Atlantic. Applying what he called Lord Holt’s “incontro-
vertible” reasoning, Justice Story explained that a prevail-
ing plaintiff “is entitled to a verdict for nominal damages”
whenever “no other [kind of damages] be proved.” Webb v.
Portland Mfg. Co., 29 F. Cas. 506, 508–509 (No. 17,322) (CC
Me. 1838). Because the common law recognized that “every
violation imports damage,” Justice Story reasoned that
“[t]he law tolerates no farther inquiry than whether there
has been the violation of a right.” Ibid. Justice Story also
made clear that this logic applied to both retrospective and
prospective relief. Id., at 507 (stating that nominal dam-
ages are available “wherever there is a wrong” and that, “[a]
fortiori, this doctrine applies where there is not only a vio-
lation of a right of the plaintiff, but the act of the defendant,
if continued, may become the foundation, by lapse of time,
of an adverse right”).
                  Cite as: 592 U. S. ____ (2021)             7

                      Opinion of the Court

   The dissent discounts Justice Story’s statement, saying
that he took a potentially contradictory position elsewhere
and asserted that both actual damages and a violation of a
legal right are required. Post, at 7–8 (opinion of ROBERTS,
C. J.). But in the same source the dissent cites, Justice
Story said that nominal damages are “presumed” “[w]here
the breach of duty is clear.” Commentaries on the Law of
Agency §217, p. 211 (1839). Justice Story adopted the same
position a few years later. Whipple v. Cumberland Mfg. Co.,
29 F. Cas. 934, 936 (No. 17,516) (CC Me. 1843) (stating that
it is “well-known and well-settled” that “wherever a wrong
is done to a right,” at minimum “nominal damages will be
given”). And other jurists declared that “[t]he principle that
every injury legally imports damage, was decisively settled,
in the case of Ashby.” Parker v. Griswold, 17 Conn. *288,
*304–*306 (1845) (citing many cases on both sides of the
Atlantic, including Webb and Marzetti). This history is
hardly one of “indeterminate sources.” Post, at 8.
   Admittedly, the rule allowing nominal damages for a vio-
lation of any legal right, though “decisively settled,” Parker,
17 Conn., at *304, was not universally followed—as is true
for most common-law doctrines. And some courts only fol-
lowed the rule in part, recognizing the availability of nomi-
nal damages but holding that the improper denial of nomi-
nal damages could be harmless error. Yet, even among
these courts, many adopted the rule in full whenever a per-
son proved that there was a violation of an “important
right.” E.g., Hecht v. Harrison, 5 Wyo. 279, 290, 40 P. 306,
309–310 (1895); accord, Reid v. Johnson, 132 Ind. 416, 419,
31 N. E. 1107, 1108 (1892) (“substantial right”). Nonethe-
less, the prevailing rule, “well established” at common law,
was “that a party whose rights are invaded can always re-
cover nominal damages without furnishing any evidence of
actual damage.” 1 T. Sedgwick, Measure of Damages 71,
n. a (7th ed. 1880); see also id., at 72 (citing Lord Holt’s
opinion in Ashby).
8              UZUEGBUNAM v. PRECZEWSKI

                     Opinion of the Court

   That this rule developed at common law is unsurprising
in the light of the noneconomic rights that individuals had
at that time. A contrary rule would have meant, in many
cases, that there was no remedy at all for those rights, such
as due process or voting rights, that were not readily reduc-
ible to monetary valuation. See D. Dobbs, Law of Remedies
§3.3(2) (3d ed. 2018) (nominal damages are often awarded
for a right “not economic in character and for which no sub-
stantial non-pecuniary award is available”); see also Carey
v. Piphus, 435 U. S. 247, 266–267 (1978) (awarding nominal
damages for a violation of procedural due process). By per-
mitting plaintiffs to pursue nominal damages whenever
they suffered a personal legal injury, the common law
avoided the oddity of privileging small-dollar economic
rights over important, but not easily quantifiable, nonpecu-
niary rights.
                              B
   Respondents and the dissent attempt to discount this his-
torical line of cases by contending that something other
than nominal damages provided redressability. They argue
instead that courts could award nominal damages only
when a plaintiff pleaded compensatory damages but failed
to prove a specific amount. In those circumstances, they
say, the plea for compensatory damages is what satisfied
the redressability requirement, and courts awarded nomi-
nal damages merely as a technical matter. We do not agree.
   To begin with, the cases themselves did not require a plea
for compensatory damages as a condition for receiving nom-
inal damages. Lord Holt spoke in categorical terms:
“[E]very injury imports a damage,” so a plaintiff who proved
a legal violation could always obtain some form of damages
because he “must of necessity have a means to vindicate
and maintain [the right].” Ashby, 2 Raym. Ld., at 953–955,
92 Eng. Rep., at 136–137. Justice Story’s language was no
less definitive: “The law tolerates no farther inquiry than
                  Cite as: 592 U. S. ____ (2021)            9

                      Opinion of the Court

whether there has been the violation of a right.” Webb, 29
F. Cas., at 508. When a right is violated, that violation “im-
ports damage in the nature of it” and “the party injured is
entitled to a verdict for nominal damages.” Id., at 508.
   Respondents and the dissent thus get the relationship be-
tween nominal damages and compensatory damages back-
wards. Nominal damages are not a consolation prize for the
plaintiff who pleads, but fails to prove, compensatory dam-
ages. They are instead the damages awarded by default
until the plaintiff establishes entitlement to some other
form of damages, such as compensatory or statutory dam-
ages. See, e.g., Dods, 15 C. B. N. S., at 621, 627, 143
Eng. Rep., at 929, 931 (prevailing plaintiff entitled to nom-
inal damages as a matter of law even where jury neglected
to find them); see also Stachura, 477 U. S., at 308 (rejecting
the argument that courts could presume, without proof,
damages greater than nominal).
   The argument that a claim for compensatory damages is
a prerequisite for an award of nominal damages also rests
on the flawed premise that nominal damages are purely
symbolic, a mere judicial token that provides no actual ben-
efit to the plaintiff. That contention is not without some
support. See, e.g., Stanton v. New York & Eastern R. Co.,
59 Conn. 272, 282, 22 A. 300, 303 (1890) (“Nominal damages
mean no damages at all. They exist only in name, and not
in amount”); but cf. ibid. (still recognizing that nominal
damages are appropriate when a right is violated). But this
view is against the weight of the history discussed above,
and we have already expressly rejected it. Despite being
small, nominal damages are certainly concrete. The dissent
says that “an award of nominal damages does not change [a
plaintiff’s] status or condition at all.” Post, at 3. But we
have already held that a person who is awarded nominal
damages receives “relief on the merits of his claim” and
“may demand payment for nominal damages no less than
10              UZUEGBUNAM v. PRECZEWSKI

                      Opinion of the Court

he may demand payment for millions of dollars in compen-
satory damages.” Farrar v. Hobby, 506 U. S. 103, 111, 113
(1992). Because nominal damages are in fact damages paid
to the plaintiff, they “affec[t] the behavior of the defendant
towards the plaintiff ” and thus independently provide re-
dress. Hewitt v. Helms, 482 U. S. 755, 761 (1987) (emphasis
deleted); accord, Mission Product Holdings, Inc. v. Temp-
nology, LLC, 587 U. S. ___, ___ (2019) (slip op., at 6) (“If
there is any chance of money changing hands, [the] suit re-
mains live”). True, a single dollar often cannot provide full
redress, but the ability “to effectuate a partial remedy” sat-
isfies the redressability requirement. Church of Scientology
of Cal. v. United States, 506 U. S. 9, 13 (1992).
   The next difficulty faced by respondents and the dissent
is their inability to square their argument with established
principles of standing. Because redressability is an “ ‘irre-
ducible’ ” component of standing, Spokeo, 578 U. S., at 338,
no federal court has jurisdiction to enter a judgment unless
it provides a remedy that can redress the plaintiff ’s injury.
Yet early courts routinely awarded nominal damages alone.
Certainly, no one seems to think that those judgments were
without legal effect. Those nominal damages necessarily
must have provided redress. Respondents contend that a
request for compensatory damages at the pleading stage
was what provided the basis for nominal damages at the
judgment stage. But a plaintiff must maintain a personal
interest in the dispute at every stage of litigation, including
when judgment is entered, Lujan v. Defenders of Wildlife,
504 U. S. 555, 561 (1992), and must do so “separately for
each form of relief sought,” Friends of the Earth, Inc. v.
Laidlaw Environmental Services (TOC), Inc., 528 U. S. 167,
185 (2000). As soon as a plea for compensatory damages
fails at the factfinding stage of litigation, that plea can no
longer support jurisdiction for a favorable judgment. The
dissent’s contrary assertion is unaccompanied by any cita-
tion.
                  Cite as: 592 U. S. ____ (2021)             11

                      Opinion of the Court

  Likewise, any analogy to attorney’s fees and costs fails.
A request for attorney’s fees or costs cannot establish stand-
ing because those awards are merely a “byproduct” of a suit
that already succeeded, not a form of redressability. Steel
Co., 523 U. S., at 107; see also Lewis v. Continental Bank
Corp., 494 U. S. 472, 480 (1990). In contrast, nominal dam-
ages are redress, not a byproduct.
                                III
   Because nominal damages were available at common law
in analogous circumstances, we conclude that a request for
nominal damages satisfies the redressability element of
standing where a plaintiff’s claim is based on a completed
violation of a legal right.
   The dissent worries that after today the Judiciary will be
required to weigh in on legal questions “whenever a plain-
tiff asks for a dollar.” Post, at 9. But petitioners still would
have satisfied redressability if instead of one dollar in nom-
inal damages they sought one dollar in compensation for a
wasted bus fare to travel to the free speech zone. The dis-
sent “would place a higher value on Article III” than a dol-
lar. Post, at 1; but see Sprint Communications Co. v. APCC
Services, Inc., 554 U. S. 269, 305 (2008) (ROBERTS, C. J., dis-
senting) (“Article III is worth a dollar”). But Congress abol-
ished the statutory amount-in-controversy requirement for
federal-question jurisdiction in 1980. Federal Question Ju-
risdictional Amendments Act, 94 Stat. 2369. And we have
never held that one applies as a matter of constitutional
law.
   This is not to say that a request for nominal damages
guarantees entry to court. Our holding concerns only re-
dressability. It remains for the plaintiff to establish the
other elements of standing (such as a particularized injury);
plead a cognizable cause of action, Planck v. Anderson, 5
T. R. 37, 41, 101 Eng. Rep. 21, 23 (K. B. 1792) (“if no [actual]
damage be sustained, the creditor has no cause of action”
12                UZUEGBUNAM v. PRECZEWSKI

                         Opinion of the Court

for some claims); and meet all other relevant requirements.
We hold only that, for the purpose of Article III standing,
nominal damages provide the necessary redress for a com-
pleted violation of a legal right.
  Applying this principle here is straightforward. For pur-
poses of this appeal, it is undisputed that Uzuegbunam ex-
perienced a completed violation of his constitutional rights
when respondents enforced their speech policies against
him. Because “every violation [of a right] imports damage,”
Webb, 29 F. Cas., at 509, nominal damages can redress
Uzuegbunam’s injury even if he cannot or chooses not to
quantify that harm in economic terms.*
  The judgment of the Court of Appeals is reversed, and the
case is remanded for further proceedings consistent with
this opinion.
                                             It is so ordered.




——————
  *We do not decide whether Bradford can pursue nominal damages.
Nominal damages go only to redressability and are unavailable where a
plaintiff has failed to establish a past, completed injury. The District
Court should determine in the first instance whether the enforcement
against Uzuegbunam also violated Bradford’s constitutional rights.
                 Cite as: 592 U. S. ____ (2021)            1

                   KAVANAUGH, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 19–968
                         _________________


   CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
        STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                        [March 8, 2021]

   JUSTICE KAVANAUGH, concurring.
   I agree with the Court that, as a matter of history and
precedent, a plaintiff’s request for nominal damages can
satisfy the redressability requirement for Article III stand-
ing and can keep an otherwise moot case alive. I write sep-
arately simply to note that I agree with THE CHIEF JUSTICE
and the Solicitor General that a defendant should be able
to accept the entry of a judgment for nominal damages
against it and thereby end the litigation without a resolu-
tion of the merits. Post, at 11 (ROBERTS, C. J., dissenting);
Brief for United States as Amicus Curiae 29–30.
                 Cite as: 592 U. S. ____ (2021)            1

                   ROBERTS, C. J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 19–968
                         _________________


   CHIKE UZUEGBUNAM, ET AL., PETITIONERS v.
        STANLEY C. PRECZEWSKI, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                        [March 8, 2021]

   CHIEF JUSTICE ROBERTS, dissenting.
   Petitioners Chike Uzuegbunam and Joseph Bradford
want to challenge the constitutionality of speech re-
strictions at Georgia Gwinnett College. There are just a few
problems: Uzuegbunam and Bradford are no longer stu-
dents at the college. The challenged restrictions no longer
exist. And the petitioners have not alleged actual damages.
The case is therefore moot because a federal court cannot
grant Uzuegbunam and Bradford “any effectual relief what-
ever.” Chafin v. Chafin, 568 U. S. 165, 172 (2013) (internal
quotation marks omitted).
   The Court resists this conclusion, holding that the peti-
tioners can keep pressing their claims because they have
asked for “nominal damages.” In the Court’s view, nominal
damages can save a case from mootness because any
amount of money—no matter how trivial—“can redress a
past injury.” Ante, at 1. But an award of nominal damages
does not alleviate the harms suffered by a plaintiff, and is
not intended to. If nominal damages can preserve a live
controversy, then federal courts will be required to give ad-
visory opinions whenever a plaintiff tacks on a request for
a dollar. Because I would place a higher value on Article
III, I respectfully dissent.
2               UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

                               I
   In urging the ratification of the Constitution, Alexander
Hamilton famously wrote that “the judiciary, from the na-
ture of its functions, will always be the least dangerous” of
“the different departments of power.” The Federalist
No. 78, p. 465 (C. Rossiter ed. 1961). This was so, Hamilton
explained, because the Judiciary “will be least in a capacity
to annoy or injure” “the political rights of the Constitution.”
Ibid. Whereas “[t]he executive not only dispenses the hon-
ors but holds the sword of the community,” and “[t]he legis-
lature not only commands the purse but prescribes the
rules by which the duties and rights of every citizen are to
be regulated,” the Judiciary “may truly be said to have nei-
ther FORCE nor WILL but merely judgment.” Ibid.
   But that power of judgment can nonetheless bind the Ex-
ecutive and Legislature—and the States. It is modest only
if confined to its proper sphere. As John Marshall empha-
sized during his one term in the House of Representatives,
“[i]f the judicial power extended to every question under the
constitution” or “to every question under the laws and trea-
ties of the United States,” then “[t]he division of power
[among the branches of Government] could exist no longer,
and the other departments would be swallowed up by the
judiciary.” 4 Papers of John Marshall 95 (C. Cullen ed.
1984) (quoted in DaimlerChrysler Corp. v. Cuno, 547 U. S.
332, 341 (2006)). To maintain adequate separation between
the Judiciary, on the one hand, and the political branches
and the States, on the other, Article III of the Constitution
authorizes federal courts to decide only “Cases” and
“Controversies”—that is, “cases of a Judiciary nature.”
2 Records of the Federal Convention of 1787, p. 430
(M. Farrand ed. 1966) (J. Madison).
   The case-or-controversy requirement imposes fundamen-
tal restrictions on who can invoke federal jurisdiction and
what types of disputes federal courts can resolve. As perti-
nent here, “when it is impossible for a court to grant any
                  Cite as: 592 U. S. ____ (2021)              3

                    ROBERTS, C. J., dissenting

effectual relief whatever to the prevailing party,” Chafin,
568 U. S., at 172 (internal quotation marks omitted), the
case is moot, and the court has no power to decide it, see
Spencer v. Kemna, 523 U. S. 1, 18 (1998). To decide a moot
case would be to give an advisory opinion, in violation of
“the oldest and most consistent thread in the federal law
of justiciability.” Flast v. Cohen, 392 U. S. 83, 96 (1968)
(internal quotation marks omitted).
   By insisting that judges be able to provide meaningful re-
dress to litigants, Article III ensures that federal courts ex-
ercise their authority only “as a necessity in the determina-
tion of real, earnest and vital controversy between
individuals.” Chicago & Grand Trunk R. Co. v. Wellman,
143 U. S. 339, 345 (1892); see Valley Forge Christian Col-
lege v. Americans United for Separation of Church and
State, Inc., 454 U. S. 464, 471 (1982) (“The constitutional
power of federal courts cannot be defined, and indeed has
no substance, without reference to the necessity ‘to adjudge
the legal rights of litigants in actual controversies.’ ” (quot-
ing Liverpool, New York & Philadelphia S. S. Co. v. Com-
missioners of Emigration, 113 U. S. 33, 39 (1885))). When
plaintiffs like Uzuegbunam and Bradford allege neither ac-
tual damages nor the prospect of future injury, an award of
nominal damages does not change their status or condition
at all. Such an award instead represents a judicial deter-
mination that the plaintiffs’ interpretation of the law is
correct—nothing more. The court in such a case is acting
not as an Article III court, but as a moot court, deciding
cases “in the rarified atmosphere of a debating society.”
Director, Office of Workers’ Compensation Programs v.
Perini North River Associates, 459 U. S. 297, 305 (1983)
(internal quotation marks omitted).
                           II
  The Court sees no problem with turning judges into ad-
vice columnists. In its view, the common law and (to a
4               UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

lesser extent) our cases require that federal courts open
their doors to any plaintiff who asks for a dollar. I part
ways with the Court regarding both the framework it ap-
plies and the result it reaches.
   Begin with the framework. The Court’s initial premise is
that we must “look to the forms of relief awarded at common
law” in order to decide “whether nominal damages can re-
dress a past injury.” Ante, at 4. Because the Court finds
that “nominal damages were available at common law in
analogous circumstances” to the ones before us, it “con-
clude[s] that a request for nominal damages satisfies the
redressability element of standing where a plaintiff ’s claim
is based on a completed violation of a legal right.” Ante, at
11.
   Any lessons that we learn from the common law, how-
ever, must be tempered by differences in constitutional de-
sign. The structure and function of 18th-century English
courts were in many respects irreconcilable with “the role
assigned to the judiciary in a tripartite allocation of power.”
Flast, 392 U. S., at 95. Perhaps most saliently, in England
“all jurisdictions of courts [were] either mediately or imme-
diately derived from the crown,” 1 W. Blackstone, Commen-
taries on the Laws of England 257 (1765), an organizational
principle the Framers explicitly rejected by separating the
Executive from the Judiciary. This difference in organiza-
tion yielded a difference in operation. To give just one ex-
ample, “English judicial practice with which early Ameri-
cans were familiar had long permitted the Crown to solicit
advisory opinions from judges.” R. Fallon, J. Manning, D.
Meltzer, & D. Shapiro, Hart and Wechsler’s The Federal
Courts and the Federal System 52 (7th ed. 2015). We would
not look to such practice for guidance today if a plaintiff
came into court arguing that advisory opinions were in fact
an appropriate form of Article III redress. We would know
that they are not. We likewise should know that a bare re-
quest for nominal damages is not justiciable because the
                  Cite as: 592 U. S. ____ (2021)            5

                   ROBERTS, C. J., dissenting

plaintiff cannot “benefit in a tangible way from the court’s
intervention.” Steel Co. v. Citizens for Better Environment,
523 U. S. 83, 103, n. 5 (1998) (internal quotation marks
omitted).
   We should of course consult founding-era decisions when
discerning the boundaries of our jurisdiction, for the Fram-
ers sought to limit the judicial power to “Cases” and “Con-
troversies,” as those terms were understood at the time.
See Coleman v. Miller, 307 U. S. 433, 460 (1939) (opinion of
Frankfurter, J.). No question. But that does not mean that
the requirements of Article III are “satisfied merely because
a party requests a court of the United States to declare its
legal rights, and has couched that request for forms of relief
historically associated with courts of law in terms that have
a familiar ring to those trained in the legal process.” Valley
Forge, 454 U. S., at 471. A focus on common law analogues
cannot obscure the significance of the establishment of an
independent Judiciary—a “remarkable transformation”
from a system with courts operating as “appendages of
crown power.” Gordon S. Wood, The Origins of Judicial Re-
view, 22 Suffolk U. L. Rev. 1293, 1304 (1988). That trans-
formation carries with it the need to cabin the jurisdiction
of the Judiciary to ensure it does not trespass on the prov-
ince of the political branches.
   It is in any event entirely unclear whether common law
courts would have awarded nominal damages in a case like
the one before us. There is no dispute that “nominal dam-
ages historically could provide prospective relief,” because
such awards allowed “plaintiffs at common law to ‘obtain a
form of declaratory relief in a legal system with no general
declaratory judgment act.’ ” Ante, at 4 (quoting D. Laycock
& R. Hasen, Modern American Remedies 636 (5th ed. 2019);
emphasis added); see Borchard, The Declaratory Judgment—
A Needed Procedural Reform, 28 Yale L. J. 1, 25–29 (1918)
(describing the development of declaratory judgments in
England in the second half of the 19th century). Yet the
6               UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

petitioners in this case no longer seek prospective relief.
Although they initially asked for a declaratory judgment
and a preliminary injunction, they abandoned those re-
quests once the college rescinded the challenged policies.
   The Court is correct to note that plaintiffs at common law
often received nominal damages for past violations of their
rights. Those awards, however, were generally limited to
situations in which prevailing plaintiffs tried and failed to
prove actual damages. See 1 D. Dobbs, Law of Remedies
§3.3(2), p. 296 (2d ed. 1993) (describing nominal damages
awards as “a rescue operation”). Notwithstanding the
Court’s protestations to the contrary, nominal damages in
such cases were in fact a “consolation prize,” ante, at 9,
awarded as a hook to allow prevailing plaintiffs to at least
recover attorney’s fees and costs. See W. Hale, Handbook
on the Law of Damages 30–31 (1896) (“The importance of
the right to recover nominal damages often consists in its
effect on costs.”); 1 T. Sedgwick, Measure of Damages §96,
p. 164 (9th ed. 1912) (“[T]hey are a mere peg to hang costs
on.” (internal quotation marks omitted)). The petitioners in
this case have asked to recover their fees and costs, but they
never sought actual damages, so the common law provides
little relevant support.
   On this last point, the Court acknowledges in several
places that the historical record is mixed as to whether legal
violations were actionable at all without a showing of com-
pensable harm. See ante, at 5, 7. And the Court does not
cite any case in which plaintiffs sought only nominal dam-
ages for purely retrospective injuries. The Court instead
relies on several decisions that contained live damages
claims, see Barker v. Green, 2 Bing. 317, 130 Eng. Rep. 327
(C. P. 1824) (“actual damage was the gist of the action”);
Hatch v. Lewis, 2 F. & F. 467, 469, 175 Eng. Rep. 1145, 1146
(N. P. 1861) (defendants’ ineffective assistance allegedly
caused plaintiff to be “deprived of the profits and emolu-
ments he might otherwise have obtained”); Dods v. Evans,
                  Cite as: 592 U. S. ____ (2021)            7

                   ROBERTS, C. J., dissenting

15 C. B. N. S. 621, 143 Eng. Rep. 929 (C. P. 1864) (action for
damages), or involved prospective harm to the plaintiff ’s
reputation, see Marzetti v. Williams, 1 B. & Ad. 415, 420,
109 Eng. Rep. 842, 844 (K. B. 1830) (bank’s failure to timely
pay “was injurious to the character of the plaintiff in his
trade”); see also C. Addison, Law of Torts 46–47 (1860) (def-
amation actionable without proof of damage).
   The Court also appeals to “categorical” and “definitive”
statements by Lord Chief Justice Holt and Justice Story,
that “every injury imports a damage,” Ashby v. White, 2
Raym. Ld. 938, 955, 92 Eng. Rep. 126, 137 (K. B. 1703), and
that “[t]he law tolerates no farther inquiry than whether
there has been the violation of a right,” Webb v. Portland
Mfg. Co., 29 F. Cas. 506, 508 (No. 17,322) (CC Me. 1838).
Ante, at 8–9. These statements, however, bear less weight
than the Court suggests. Lord Holt was alone in dissent in
Ashby (no shame there), and although his opinion has been
cited favorably by subsequent cases and commentary, his
colleagues disagreed with him. The Court writes that “the
House of Lords overturned the majority decision, thus vali-
dating Lord Holt’s position,” ante, at 6, but the House of
Lords likely paid scant attention to Lord Holt’s analysis. It
appears instead that the majority decision was reversed as
collateral damage in a Whig-Tory political dispute, and “lit-
tle weight was given to reasoning or eloquence.” 2 J. Camp-
bell, Lives of the Chief Justices of England 160 (1849).
(Ashby had tried to vote for a Whig candidate, and his ballot
had been rejected as part of a Tory election-rigging scheme.
Id., at 156–157.) Regardless, the House of Lords held that
Ashby “should recover his damages assessed by the jury” at
trial, suggesting that the fact of injury alone did not “im-
port” them. Ashby v. White, 1 Bro. P. C. 62, 64, 1 Eng. Rep.
417, 418 (1703).
   Justice Story is no more helpful to the Court—despite the
supposedly “definitive” nature of his statement in Webb—
as he took the position elsewhere in his writings that a legal
8               UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

violation alone was not sufficient to ground a lawsuit. See
Commentaries on the Law of Agency §236, p. 200 (1839)
(“[T]he rule applies, that though it is a wrong, it is without
any damage; and, to maintain an action, both must concur;
for damnum absque injuria, and injuria absque damno, are
equally objections to any recovery.”). Perhaps Justice
Story’s conflicting statements can be reconciled, see ante, at
7; Hessick, Standing, Injury in Fact, and Private Rights, 93
Cornell L. Rev. 275, 283, n. 38 (2008), but neither his com-
mentary nor Lord Holt’s dissent provides firm footing for
the position that a plaintiff could seek nominal damages
without alleging actual damages or prospective harm.
   At bottom, the Court relies on a handful of indeterminate
sources to justify a radical expansion of the judicial power.
The Court acknowledges that “the rule allowing nominal
damages for a violation of any legal right . . . was not uni-
versally followed,” ante, at 7, but even this concession un-
derstates the equivocal nature of the historical record. I
would require more before bursting the bounds of Article
III.
   The Court spends little time trying to reconcile its analy-
sis with modern justiciability principles. It cites in passing
our decisions in Carey v. Piphus, 435 U. S. 247 (1978), Mem-
phis Community School Dist. v. Stachura, 477 U. S. 299
(1986), and Farrar v. Hobby, 506 U. S. 103 (1992), but those
cases made no mention of Article III, and none involved a
standalone claim for nominal damages. The Court also con-
tends that nominal damages must provide redress because
courts would otherwise lack jurisdiction to award them,
even where a plaintiff tries and fails to prove actual dam-
ages. See ante, at 10. But a claim for actual damages pre-
serves a live controversy, see Memphis Light, Gas & Water
Div. v. Craft, 436 U. S. 1, 8–9 (1978), and a court does not
lose jurisdiction just because that claim ultimately fails.
   Finally, the Court argues that nominal damages provide
Article III relief because they “affec[t] the behavior of the
                  Cite as: 592 U. S. ____ (2021)              9

                    ROBERTS, C. J., dissenting

defendant towards the plaintiff ” by requiring “money
changing hands.” Ante, at 10 (internal quotation marks
omitted). If this were the standard, then the prospect of
attorney’s fees and costs would confer standing at the be-
ginning of a lawsuit and prevent mootness throughout—a
proposition we have squarely rejected. See Lewis v. Conti-
nental Bank Corp., 494 U. S. 472, 480 (1990). The Court
posits that “nominal damages are redress,” whereas fees
and costs “are merely a byproduct of a suit that already suc-
ceeded.” Ante, at 11 (internal quotation marks omitted).
This classification just begs the question of what qualifies
as redress. To satisfy Article III, redress must alleviate the
plaintiff ’s alleged injury in some way, either by compensat-
ing the plaintiff for a past loss or by preventing an ongoing
or future harm. Nominal damages do not serve these ends
where a plaintiff alleges only a completed violation of his
rights. They are not intended to approximate the value of
tangible or intangible harms, or the deterrent effect re-
quired to prevent future misconduct. And they are not cal-
culated with reference to either of these purposes. Because
such an award performs no remedial function—and because
“[r]elief that does not remedy the injury suffered cannot
bootstrap a plaintiff into federal court,” Steel Co., 523 U. S.,
at 107—nominal damages cannot preserve a live contro-
versy where a case is otherwise moot.
                              III
  Today’s decision risks a major expansion of the judicial
role. Until now, we have said that federal courts can review
the legality of policies and actions only as a necessary inci-
dent to resolving real disputes. Going forward, the Judici-
ary will be required to perform this function whenever a
plaintiff asks for a dollar. For those who want to know if
their rights have been violated, the least dangerous branch
will become the least expensive source of legal advice.
  In an effort to downplay these consequences, the Court
10              UZUEGBUNAM v. PRECZEWSKI

                    ROBERTS, C. J., dissenting

argues that plaintiffs who seek nominal damages will often
be able to seek actual damages as well. In this case, for
example, the Court notes that Uzuegbunam and Bradford
“would have satisfied redressability if instead of one dollar
in nominal damages they sought one dollar in compensation
for a wasted bus fare to travel to the free speech zone.”
Ante, at 11. Maybe they would have, and maybe they
should have. The Court is mistaken, however, to equate a
small amount of actual damages with the token award of
nominal damages. The former redresses a compensable
harm and satisfies Article III, while the latter is a legal fic-
tion with “no existence in point of quantity.” J. Mayne, Law
of Damages 27 (1856) (internal quotation marks omitted);
see Dobbs, Law of Remedies §3.3(2), at 294 (“Nominal dam-
ages are damages in name only . . . .”).
   The Court also insists that not every “request for nominal
damages guarantees entry to court.” Ante, at 11. Yet its
holding admits of no limiting principle. As then-Judge
McConnell remarked in an insightful concurrence on the is-
sue before us, “[i]t is hard to conceive of a case in which a
plaintiff would be unable to append a claim for nominal
damages, and thus insulate the case from the possibility of
mootness.” Utah Animal Rights Coalition v. Salt Lake City
Corp., 371 F. 3d 1248, 1266 (CA10 2004). The Court today
reinforces this point by emphasizing that “every violation of
a right imports damage,” ante, at 12 (emphasis added; al-
terations and internal quotation marks omitted)—even
though we have definitively and recently held that a plain-
tiff must allege a concrete injury even where his rights have
been violated, see Thole v. U. S. Bank N. A., 590 U. S. ___,
___ (2020) (slip op., at 5) (“This Court has rejected the ar-
gument that ‘a plaintiff automatically satisfies the injury-
in-fact requirement whenever a statute grants a person a
statutory right and purports to authorize that person to sue
to vindicate that right.’ ” (quoting Spokeo, Inc. v. Robins,
578 U. S. 330, 341 (2016))).
                  Cite as: 592 U. S. ____ (2021)           11

                   ROBERTS, C. J., dissenting

   The best that can be said for the Court’s sweeping excep-
tion to the case-or-controversy requirement is that it may
itself admit of a sweeping exception: Where a plaintiff asks
only for a dollar, the defendant should be able to end the
case by giving him a dollar, without the court needing to
pass on the merits of the plaintiff ’s claims. Although we
recently reserved the question whether a defendant can
moot a case by depositing the full amount requested by the
plaintiff, Campbell-Ewald Co. v. Gomez, 577 U. S. 153, 166
(2016), our cases have long suggested that he can, see, e.g.,
California v. San Pablo & Tulare R. Co., 149 U. S. 308, 313–
314 (1893). The United States agrees, arguing in its brief
in “support” of the petitioners that “the defendant should be
able to end the litigation without a resolution of the consti-
tutional merits, simply by accepting the entry of judgment
for nominal damages against him.” Brief for United States
as Amicus Curiae 29. The defendant can even file an offer
of judgment for one dollar, rendering the plaintiff liable for
any subsequent costs if he receives only nominal damages.
See Fed. Rule Civ. Proc. 68(d). This is a welcome caveat,
and it may ultimately save federal courts from issuing
reams of advisory opinions. But it also highlights the flim-
siness of the Court’s view of the separation of powers. The
scope of our jurisdiction should not depend on whether the
defendant decides to fork over a buck.
                        *     *    *
  Five years after Hamilton wrote Federalist No. 78, Secre-
tary of State Thomas Jefferson sent a letter on behalf of
President George Washington to Chief Justice John Jay
and the Associate Justices of the Supreme Court, asking for
advice about the Nation’s rights and obligations regarding
the ongoing war in Europe. Washington’s request must
have struck him as reasonable enough, since English sover-
eigns regularly sought advice from their courts. Yet the
12             UZUEGBUNAM v. PRECZEWSKI

                   ROBERTS, C. J., dissenting

Justices declined the entreaty, citing “the lines of separa-
tion drawn by the Constitution between the three depart-
ments of the government.” 3 Correspondence and Public
Papers of John Jay 488 (H. Johnston ed. 1891). For over
two centuries, the Correspondence of the Justices has stood
as a reminder that federal courts cannot give answers
simply because someone asks.
   The Judiciary is authorized “to say what the law is” only
because “[t]hose who apply [a] rule to particular cases, must
of necessity expound and interpret the rule.” Marbury v.
Madison, 1 Cranch 137, 177 (1803) (emphasis added). To-
day’s decision abandons that principle. When a plaintiff
brings a nominal damages claim in the absence of past dam-
ages or future harm, it is not “necessary to give an opinion
upon a question of law.” San Pablo, 149 U. S., at 314. It is
instead a “gratuitous” exercise of the judicial power, Simon
v. Eastern Ky. Welfare Rights Organization, 426 U. S. 26,
38 (1976), and expanding that power encroaches on the po-
litical branches and the States. Perhaps defendants will
wise up and moot such claims by paying a dollar, but it is
difficult to see that outcome as a victory for Article III.
Rather than encourage litigants to fight over farthings,
I would affirm the judgment of the Court of
Appeals.

```

---

## GROUP: _overhaul2/lake/cases/Vale v. Louisiana.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Vale v. Louisiana"
type: case
citation: "399 U.S. 30 (1970)"
parallel_cite: "90 S. Ct. 1969; 26 L. Ed. 2d 409"
neutral_cite: 1970 U.S. LEXIS 18
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-06-22
docket: 727
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1970-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vale v. Louisiana
  varies_by_point: false
  scope_note: "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108183/vale-v-louisiana/"
  cluster_id: 108183
  opinion_id: 108183
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Limiting"
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
related: ["[[Chimel v. California]]", "[[Shipley v. California]]", "[[Agnello v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "warrant-requirement", "exigent-circumstances"]
holding: "A search of a house cannot be justified as incident to an arrest made outside the house; a warrantless dwelling search requires a recognized exception, and a street arrest is not its own exigent circumstance."
lake:
  record_id: Vale v. Louisiana
  status: verified
  projected_at: 2026-07-09
---

# Vale v. Louisiana

*399 U.S. 30 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers holding two arrest warrants for Vale, and information that he lived at a specified address, set up surveillance of the house. They watched what they took to be a narcotics sale to the driver of a car at the curb, then approached. They arrested Vale on the front steps of the house, entered, made a cursory check that no one else was inside, and searched a rear bedroom, where they found narcotics.

## Issue
May a warrantless search of a house be justified as incident to an arrest made outside the house (on the front steps), or by the ready destructibility of narcotics, absent any exigent circumstance?

## Rule
No. A search "may be incident to an arrest ' "only if it is substantially contemporaneous with the arrest and is confined to the *immediate* vicinity of the arrest." ' " — 399 U.S. at 33 (quoting *Shipley v. California*). ^pin-33

"If a search of a house is to be upheld as incident to an arrest, that arrest must take place inside the house . . . not somewhere outside — whether two blocks away . . . twenty feet away . . . or on the sidewalk near the front steps." — *Id.* at 34. ^pin-34

Beyond the search-incident rationale, only "a few specifically established and well-delineated" situations let a warrantless dwelling search survive even on probable cause, and "[t]he burden rests on the State to show the existence of such an exceptional situation." — [*Id.*](https://www.courtlistener.com/opinion/108183/vale-v-louisiana/#:~:text=a%20few%20specifically%20established%20and) ^pin-34b

The Court "decline[d] to hold that an arrest on the street can provide its own 'exigent circumstance' so as to justify a warrantless search of the arrestee's house." — *Id.* at 35. ^pin-35

## Application
Vale was arrested on the front steps, not inside the dwelling, so the search of the rear bedroom was neither within the immediate vicinity of the arrest nor incident to it. Nor did any exception excuse the warrant: by the officers' own account they had satisfied themselves no one else was in the house when they entered, so there was no one to destroy evidence; no one consented; the officers were not responding to an emergency or in [[Exigent Circumstances and Hot Pursuit|hot pursuit]]; the seized goods were not in the process of destruction and were not about to be removed; and the officers who had obtained two arrest warrants had no apparent reason they could not also obtain a search warrant. The street arrest supplied no [[Exigent Circumstances and Hot Pursuit|exigency]] of its own.

## Conclusion
The warrantless search of the house was unconstitutional, and admitting its fruits was constitutional error. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Vale* remains the controlling statement that a search incident to a recent arrest cannot reach a dwelling when the arrest occurred outside it, and that the State bears the burden of justifying any warrantless home search. It applies the spatial limit of [[Chimel v. California]] and is regularly cited alongside [[Shipley v. California]] and [[Agnello v. United States]]. No negative treatment.

## Appears on
- [[SIA Persons]] — *Limiting*
- [[Arrest in the Home]] — *Related (cross-doctrine)*

## Sources
- *Vale v. Louisiana*, 399 U.S. 30 (1970) — https://www.courtlistener.com/opinion/108183/vale-v-louisiana/ — pinpoints: 33, 34, 35.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c33347c8a1ee10c5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Vale v. Louisiana"}, "payload": {"all": [{"cite": "399 U.S. 30", "page": "30", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "399"}, {"cite": "90 S. Ct. 1969", "page": "1969", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "90"}, {"cite": "26 L. Ed. 2d 409", "page": "409", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "1970 U.S. LEXIS 18", "page": "18", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1970"}], "display": "399 U.S. 30", "official": {"cite": "399 U.S. 30", "page": "30", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "399"}, "official_selection_present": true, "record_id": "Vale v. Louisiana"}}
{"assertion_id": "10b1c7a10a308c18", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-34b", "record_id": "Vale v. Louisiana"}, "payload": {"fragment": "#:~:text=a%20few%20specifically%20established%20and", "page": null, "pin_id": "pin-34b", "pinpoint_status": "star-verified", "quote": "a few specifically established and well-delineated", "quote_fidelity": "matched", "record_id": "Vale v. Louisiana", "star_marker": "34"}}
{"assertion_id": "9ccbdd4de51452ad", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-34", "record_id": "Vale v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-34", "pinpoint_status": "slip-only", "quote": "If a search of a house is to be upheld as incident to an arrest, that arrest must take place inside the house . . . not somewhere outside — whether two blocks away . . . twenty feet away . . . or on the sidewalk near the front steps.", "quote_fidelity": "mismatch", "record_id": "Vale v. Louisiana", "star_marker": null}}
{"assertion_id": "e2fccdf62bc0b3f1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-35", "record_id": "Vale v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-35", "pinpoint_status": "slip-only", "quote": "decline[d] to hold that an arrest on the street can provide its own 'exigent circumstance' so as to justify a warrantless search of the arrestee's house.", "quote_fidelity": "mismatch", "record_id": "Vale v. Louisiana", "star_marker": null}}
{"assertion_id": "fd10d273b8fa2551", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-33", "record_id": "Vale v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-33", "pinpoint_status": "slip-only", "quote": "--- # Vale v. Louisiana *399 U.S. 30 (1970)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers holding two arrest warrants for Vale, and information that he lived at a specified address, set up surveillance of the house. They watched what they took to be a narcotics sale to the driver of a car at the curb, then approached. They arrested Vale on the front steps of the house, entered, made a cursory check that no one else was inside, and searched a rear bedroom, where they found narcotics. ## Issue May a warrantless search of a house be justified as incident to an arrest made outside the house (on the front steps), or by the ready destructibility of narcotics, absent any exigent circumstance? ## Rule No. A search", "quote_fidelity": "mismatch", "record_id": "Vale v. Louisiana", "star_marker": null}}
{"assertion_id": "895d3dfd9d93fbe5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Vale v. Louisiana"}, "payload": {"as_of_content": "1970-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Vale v. Louisiana", "scope_note": "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it.", "varies_by_point": false}}
```

### lake record — Vale v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vale v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vale v. Louisiana",
    "case_name_short": "Vale",
    "case_name_full": "Vale v. Louisiana",
    "input_case_name": "Vale v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-06-22",
    "year": 1970,
    "docket": "727",
    "cluster_id": 108183,
    "lead_opinion_id": 108183,
    "sibling_ids": [
      108183,
      9424318,
      9424319
    ],
    "absolute_url": "/opinion/108183/vale-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "399 U.S. 30",
      "volume": "399",
      "reporter": "U.S.",
      "page": "30",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 1969",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1969",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 409",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 18",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "399 U.S. 30",
        "volume": "399",
        "reporter": "U.S.",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 1969",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "1969",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 L. Ed. 2d 409",
        "volume": "26",
        "reporter": "L. Ed. 2d",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 18",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "18",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "399 U.S. 30",
    "official_selection": {
      "court_class": "scotus",
      "selected": "399 U.S. 30",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-33",
      "page": null,
      "quote": "--- # Vale v. Louisiana *399 U.S. 30 (1970)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers holding two arrest warrants for Vale, and information that he lived at a specified address, set up surveillance of the house. They watched what they took to be a narcotics sale to the driver of a car at the curb, then approached. They arrested Vale on the front steps of the house, entered, made a cursory check that no one else was inside, and searched a rear bedroom, where they found narcotics. ## Issue May a warrantless search of a house be justified as incident to an arrest made outside the house (on the front steps), or by the ready destructibility of narcotics, absent any exigent circumstance? ## Rule No. A search",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-34",
      "page": null,
      "quote": "If a search of a house is to be upheld as incident to an arrest, that arrest must take place inside the house . . . not somewhere outside \u2014 whether two blocks away . . . twenty feet away . . . or on the sidewalk near the front steps.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-34b",
      "page": null,
      "quote": "a few specifically established and well-delineated",
      "star_marker": "34",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9600,
      "fragment": "#:~:text=a%20few%20specifically%20established%20and",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-35",
      "page": null,
      "quote": "decline[d] to hold that an arrest on the street can provide its own 'exigent circumstance' so as to justify a warrantless search of the arrestee's house.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1970-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Vale v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Applies Chimel's spatial limit to dwellings; still the controlling rule that a search incident to arrest cannot reach a house when the arrest occurs outside it.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People v. Shawn J. Sivertson",
          "cluster_id": 4396228,
          "cite": [
            "29 N.Y.3d 1006",
            "77 N.E.3d 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Frankie Dean Pair, Jr. v. State",
          "cluster_id": 2850893,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vela v. State",
          "cluster_id": 5248598,
          "cite": [
            "775 S.W.2d 11",
            "1989 Tex. App. LEXIS 1522",
            "1989 WL 61440"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baird",
          "cluster_id": 1281144,
          "cite": [
            "763 P.2d 1214",
            "94 Utah Adv. Rep. 40",
            "1988 Utah App. LEXIS 163",
            "1988 WL 116729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Livingston v. State",
          "cluster_id": 5243642,
          "cite": [
            "731 S.W.2d 744",
            "1987 Tex. App. LEXIS 7761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane1_negative"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. State",
          "cluster_id": 1960022,
          "cite": [
            "105 S.W.3d 609",
            "2003 Tex. Crim. App. LEXIS 75",
            "2003 WL 1918091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyman v. James",
          "cluster_id": 108223,
          "cite": [
            "27 L. Ed. 2d 408",
            "91 S. Ct. 381",
            "400 U.S. 309",
            "1971 U.S. LEXIS 106"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramey",
          "cluster_id": 1185860,
          "cite": [
            "545 P.2d 1333",
            "16 Cal. 3d 263",
            "127 Cal. Rptr. 629",
            "1976 Cal. LEXIS 220"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Webster Bivens v. Six Unknown Named Agents of the Federal Bureau of Narcotics",
          "cluster_id": 302266,
          "cite": [
            "456 F.2d 1339",
            "1972 U.S. App. LEXIS 10860"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Sangineto-Miranda, (87-5667) Luray Betts, (87-5668) Enrique Vargas, (87-5711) & Benjamin Nelson, (87-5712)",
          "cluster_id": 513263,
          "cite": [
            "859 F.2d 1501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Castillo, Aka: Luis Hong Rojas, United States of America v. Antonio De La Renta",
          "cluster_id": 517687,
          "cite": [
            "866 F.2d 1071"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Joe Whitten, John Elmer Gaiefsky, Jack Wayne Gish, Richard Lawrence Shimel",
          "cluster_id": 418069,
          "cite": [
            "706 F.2d 1000",
            "13 Fed. R. Serv. 384",
            "1983 U.S. App. LEXIS 27369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1162553,
          "cite": [
            "756 P.2d 221",
            "45 Cal. 3d 1268",
            "248 Cal. Rptr. 834",
            "1988 Cal. LEXIS 155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul Gary Rubin United States of America v. Louis Martin Agnes A/K/A Louis Martin",
          "cluster_id": 308715,
          "cite": [
            "474 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Servis v. Commonwealth",
          "cluster_id": 1349258,
          "cite": [
            "371 S.E.2d 156",
            "6 Va. App. 507",
            "5 Va. Law Rep. 37",
            "1988 Va. App. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Raymond Basurto",
          "cluster_id": 319510,
          "cite": [
            "497 F.2d 781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vale v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108183 OR 9424318 OR 9424319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MzY1NDQwMDAwMDAmcz0xMjI4MDgwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108183+OR+9424318+OR+9424319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(108183 OR 9424318 OR 9424319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYmcz0xMDU3NzI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108183+OR+9424318+OR+9424319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108183 OR 9424318 OR 9424319)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108183 OR 9424318 OR 9424319)",
    "indexed_citing_opinions": 631,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108183,
        "count": 565,
        "count_source": "search"
      },
      {
        "opinion_id": 9424318,
        "count": 90,
        "count_source": "search"
      },
      {
        "opinion_id": 9424319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1044,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vale-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ2ODE1NzMmcz00MjY1NTA3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108183+OR+9424318+OR+9424319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108183,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 107982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108183,
        "cited_id": 1714335,
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
    "date_created": "2026-07-06T03:43:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:47:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:43:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vale v. Louisiana

```
<div>
<center><b><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/" aria-description="Citation for case: Vale v. Louisiana">399 U.S. 30</a></span> (1970)</b></center>
<center><h1>VALE<br>
v.<br>
LOUISIANA.</h1></center>
<center>No. 727.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 4-5, 1970.</center>
<center>Decided June 22, 1970.</center>
APPEAL FROM THE SUPREME COURT OF LOUISIANA.
<p><i>Eberhard P. Deutsch,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./396/883/">396 U. S. 883</a></span>, argued the cause for appellant. With him on the brief was <i>Rene H. Himel, Jr.</i></p>
<p><span class="star-pagination">*31</span> <i>Louise Korns</i> argued the cause for appellee. With her on the brief were <i>Jack P. F. Gremillion,</i> Attorney General of Louisiana, and <i>Jim Garrison.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The appellant, Donald Vale, was convicted in a Louisiana court on a charge of possessing heroin and was sentenced as a multiple offender to 15 years' imprisonment at hard labor. The Louisiana Supreme Court affirmed the conviction, rejecting the claim that evidence introduced at the trial was the product of an unlawful search and seizure. <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/" aria-description="Citation for case: State v. Vale">252 La. 1056</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/" aria-description="Citation for case: State v. Vale">215 So. 2d 811</a></span>. We granted Vale's motion to proceed <i>in forma pauperis,</i> postponed consideration of the question of jurisdiction to the hearing of the case on the merits, and limited review to the search-and-seizure question. <span class="citation multiple-matches"><a href="/c/U.%20S./396/813/">396 U. S. 813</a></span>.<sup>[*]</sup></p>
<p>The evidence adduced at the pretrial hearing on a motion to suppress showed that on April 24, 1967, officers possessing two warrants for Vale's arrest and having information that he was residing at a specified address proceeded there in an unmarked car and set up a surveillance of the house. The evidence of what then took <span class="star-pagination">*32</span> place was summarized by the Louisiana Supreme Court as follows:</p>
<blockquote>"After approximately 15 minutes the officers observed a green 1958 Chevrolet drive up and sound the horn and after backing into a parking place, again blew the horn. At this juncture Donald Vale, who was well known to Officer Brady having arrested him twice in the previous month, was seen coming out of the house and walk up to the passenger side of the Chevrolet where he had a close brief conversation with the driver; and after looking up and down the street returned inside of the house. Within a few minutes he reappeared on the porch, and again cautiously looked up and down the street before proceeding to the passenger side of the Chevrolet, leaning through the window. From this the officers were convinced a narcotics sale had taken place. They returned to their car and immediately drove toward Donald Vale, and as they reached within approximately three cars lengths from the accused, (Donald Vale) he looked up and, obviously recognizing the officers, turned around, walking quickly toward the house. At the same time the driver of the Chevrolet started to make his get away when the car was blocked by the police vehicle. The three officers promptly alighted from the car, whereupon Officers Soule and Laumann called to Donald Vale to stop as he reached the front steps of the house, telling him he was under arrest. Officer Brady at the same time, seeing the driver of the Chevrolet, Arizzio Saucier, whom the officers knew to be a narcotic addict, place something hurriedly in his mouth, immediately placed him under arrest and joined his co-officers. Because of the transaction <span class="star-pagination">*33</span> they had just observed they, informed Donald Vale they were going to search the house, and thereupon advised him of his constitutional rights. After they all entered the front room, Officer Laumann made a cursory inspection of the house to ascertain if anyone else was present and within about three minutes Mrs. Vale and James Vale, mother and brother of Donald Vale, returned home carrying groceries and were informed of the arrest and impending search." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1067" aria-description="Citation for case: State v. Vale">252 La., at 1067-1068</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#815" aria-description="Citation for case: State v. Vale">215 So. 2d, at 815</a></span>. (Footnote omitted.)</blockquote>
<p>The search of a rear bedroom revealed a quantity of narcotics.</p>
<p>The Louisiana Supreme Court held that the search of the house did not violate the Fourth Amendment because it occurred "in the immediate vicinity of the arrest" of Donald Vale and was "substantially contemporaneous therewith . . . ." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La., at 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d, at 816</a></span>. We cannot agree. Last Term in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>, we held that when the search of a dwelling is sought to be justified as incident to a lawful arrest, it must constitutionally be confined to the area within the arrestee's reach at the time of his arrest"the area from within which he might gain possession of a weapon or destructible evidence." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. But even if <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> is not accorded retroactive effecta question on which we do not now express an opinionno precedent of this Court can sustain the constitutional validity of the search in the case before us.</p>
<p>A search may be incident to an arrest " `only if it is substantially contemporaneous with the arrest and is confined to the <i>immediate</i> vicinity of the arrest.' " <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/#819" aria-description="Citation for case: Shipley v. California">395 U. S. 818, 819</a></span>; <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. If a search of a house is to be upheld <span class="star-pagination">*34</span> as incident to an arrest, that arrest must take place <i>inside</i> the house, cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 32</a></span>, not somewhere outsidewhether two blocks away, <i>James</i> v. <i>Louisiana,</i> <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span>, twenty feet away, <i>Shipley</i> v. <i>California, supra</i><i>,</i> or on the sidewalk near the front steps. "Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant." <i>Agnello</i> v. <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States"><i>United States, supra,</i> at 33</a></span>. That basic rule "has never been questioned in this Court." <i>Stoner</i> v. <i>California, supra,</i> at 487 n. 5.</p>
<p>The Louisiana Supreme Court thought the search independently supportable because it involved narcotics, which are easily removed, hidden, or destroyed. It would be unreasonable, the Louisiana court concluded, "to require the officers under the facts of the case to first secure a search warrant before searching the premises, as time is of the essence inasmuch as the officers never know whether there is anyone on the premises to be searched who could very easily destroy the evidence." <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La., at 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d, at 816</a></span>. Such a rationale could not apply to the present case, since by their own account the arresting officers satisfied themselves that no one else was in the house when they first entered the premises. But entirely apart from that point, our past decisions make clear that only in "a few specifically established and well-delineated" situations, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>, may a warrantless search of a dwelling withstand constitutional scrutiny, even though the authorities have probable cause to conduct it. The burden rests on the State to show the existence of such an exceptional situation. <i>Chimel</i> v. <i>California, supra,</i> at 762; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. And the record before us discloses none.</p>
<p><span class="star-pagination">*35</span> There is no suggestion that anyone consented to the search. Cf. <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#628" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 628</a></span>. The officers were not responding to an emergency. <i>United States</i> v. <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Jeffers, supra,</i> at 52</a></span>; <i>McDonald</i> v. <i>United States, supra,</i> at 454. They were not in hot pursuit of a fleeing felon. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span>; <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 15</a></span>. The goods ultimately seized were not in the process of destruction. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span>; <i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>; </i><i>McDonald</i> v. <i>United States, supra,</i> at 455. Nor were they about to be removed from the jurisdiction. <i>Chapman</i> v. <i>United States, supra</i><i>; </i><i>Johnson</i> v. <i>United States, supra</i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>.</i></p>
<p>The officers were able to procure two warrants for Vale's arrest. They also had information that he was residing at the address where they found him. There is thus no reason, so far as anything before us appears, to suppose that it was impracticable for them to obtain a search warrant as well. Cf. <i>McDonald</i> v. <i>United States, supra,</i> at 454-455; <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705-706</a></span>; <i>Johnson</i> v. <i>United States, supra</i><i>; </i><i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>; <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span>; cf. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#42" aria-description="Citation for case: Ker v. California">374 U. S. 23, 42</a></span> (opinion of Clark, J.). We decline to hold that an arrest on the street can provide its own "exigent circumstance" so as to justify a warrantless search of the arrestee's house.</p>
<p>The Louisiana courts committed constitutional error in admitting into evidence the fruits of the illegal search. <i>Shipley</i> v. <i>California, supra,</i> at 819; <i>James</i> v. <i>Louisiana, supra,</i> at 37; <i>Ker</i> v. <i>California, supra,</i> at 30-34; <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. Accordingly, the judgment is <span class="star-pagination">*36</span> reversed and the case is remanded to the Louisiana Supreme Court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE BLACK, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Fourth Amendment to the United States Constitution prohibits only "unreasonable searches."<sup>[*]</sup> A warrant has never been thought to be an absolute requirement for a constitutionally proper search. Searches, whether with or without a warrant, are to be judged by whether they are reasonable, and, as I said, speaking for the Court in <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 366-367</a></span> (1964), common sense dictates that reasonableness varies with the circumstances of the search. See, <i>e. g., </i><i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). The Louisiana Supreme Court held not only that the police action here was reasonable but also that failure to conduct an immediate search would have been unreasonable. <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#1070" aria-description="Citation for case: State v. Vale">252 La. 1056, 1070</a></span>, <span class="citation" data-id="1714335"><a href="/opinion/1714335/state-v-vale/#816" aria-description="Citation for case: State v. Vale">215 So. 2d 811, 816</a></span>. With that view I am in complete agreement, for the following reasons.</p>
<p>The police, having warrants for Vale's arrest, were watching his mother's house from a short distance away. Not long after they began their vigil a car arrived, <span class="star-pagination">*37</span> sounded its horn, and backed into a parking space near the house. The driver did not get out, but instead honked the car horn again. Vale, who had been arrested twice the month before and against whom an indictment for a narcotics offense was then pending, came out of his mother's house and talked to the driver of the car. At the conclusion of the conversation Vale looked both ways, up and down the street, and then went back inside the house. When he reappeared he stopped before going to the car and stood, as one of the officers testified, "[l]ooking back and forth like to see who might be coming or who was in the neighborhood." He then walked to the car and leaned in.</p>
<p>From this behavior the officers were convinced that a narcotics transaction was taking place at that very moment. They drove down the street toward Vale and the parked car. When they came within a few car lengths of the two men Vale saw them and began to walk quickly back toward the house. At the same time the driver of the car attempted to pull away. The police brought both parties to the transaction to a stop. They then saw that the driver of the car was one Saucier, a known narcotics addict. He hurriedly placed something in his mouth, and apparently swallowed it. The police placed both Vale and Saucier under arrest.</p>
<p>At this point the police had probable cause to believe that Vale was engaged in a narcotics transfer, and that a supply of narcotics would be found in the house, to which Vale had returned after his first conversation, from which he had emerged furtively bearing what the police could readily deduce was a supply of narcotics, and toward which he hurried after seeing the police. But the police did not know then who else might be in the house. Vale's arrest took place near the house, and anyone observing from inside would surely have been alerted to destroy the stocks of contraband which <span class="star-pagination">*38</span> the police believed Vale had left there. The police had already seen Saucier, the narcotics addict, apparently swallow what Vale had given him. Believing that some evidence had already been destroyed and that other evidence might well be, the police were faced with the choice of risking the immediate destruction of evidence or entering the house and conducting a search. I cannot say that their decision to search was unreasonable. Delay in order to obtain a warrant would have given an accomplice just the time he needed.</p>
<p>That the arresting officers did, in fact, believe that others might be in the house is attested to by their actions upon entering the door left open by Vale. The police at once checked the small house to determine if anyone else was present. Just as they discovered the house was empty, however, Vale's mother and brother arrived. Now what had been a suspicion became a certainty: Vale's relatives were in possession and knew of his arrest. To have abandoned the search at this point, and left the house with Vale, would not have been the action of reasonable police officers. As MR. JUSTICE WHITE said, dissenting in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#775" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 775</a></span> (1969):</p>
<blockquote>"For the police to search the house while the evidence they had probable cause to search out and seize was still there cannot be considered unreasonable."</blockquote>
<p>In my view, whether a search incident to a lawful arrest is reasonable should still be determined by the facts and circumstances of each case. <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34-36</a></span> (1963); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63-64</a></span> (1950). For the reasons given above I am convinced that the search here was reasonable, even though Vale had not yet crossed the threshold of the house toward which he was headed.</p>
<p><span class="star-pagination">*39</span> Moreover, the circumstances here were sufficiently exceptional to justify a search, even if the search was not strictly "incidental" to an arrest. The Court recognizes that searches to prevent the destruction or removal of evidence have long been held reasonable by this Court. <i>Preston</i> v. <i>United States, supra</i><i>; </i><i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span> (1948); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). Whether the "exceptional circumstances" justifying such a search exist or not is a question that may be, as it is here, quite distinct from whether or not the search was incident to a valid arrest. See <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). It is thus unnecessary to determine whether the search was valid as incident to the arrest under either <i>Chimel</i> v. <i>California, supra</i><i>,</i> or under the pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> standard as interpreted in <i>Shipley</i> v. <i>California,</i> <span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/" aria-description="Citation for case: Shipley v. California">395 U. S. 818</a></span> (1969). It is only necessary to find that, given Vale's arrest in a spot readily visible to anyone in the house and the probable existence of narcotics inside, it was reasonable for the police to conduct an immediate search of the premises.</p>
<p>The Court, however, finds the search here unreasonable. First, the Court suggests that the contraband was not "in the process of destruction." None of the cases cited by the Court supports the proposition that "exceptional circumstances" exist only when the process of destruction has already begun. On the contrary we implied that those circumstances did exist when "evidence or contraband was <i>threatened</i> with removal or destruction." <i>Johnson</i> v. <i>United States, supra,</i> at 15 (emphasis added). See also <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/#615" aria-description="Citation for case: Chapman v. United States">365 U. S. 610, 615</a></span> (1961); <i>Hernandez</i> v. <i>United States,</i> <span class="citation" data-id="8874330"><a href="/opinion/8888212/hernandez-v-united-states/" aria-description="Citation for case: Hernandez v. United States">353 F. 2d 624</a></span> (C. A. 9th Cir. 1965), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1008/">384 U. S. 1008</a></span> (1966).</p>
<p><span class="star-pagination">*40</span> Second, the Court seems to argue that the search was unreasonable because the police officers had time to obtain a warrant. I agree that the opportunity to obtain a warrant is one of the factors to be weighed in determining reasonableness. <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948); <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 66</a></span> (BLACK, J., dissenting). But the record conclusively shows that there was no such opportunity here. As I noted above, once the officers had observed Vale's conduct in front of the house they had probable cause to believe that a felony had been committed and that immediate action was necessary. At no time after the events in front of Mrs. Vale's house would it have been prudent for the officers to leave the house in order to secure a warrant.</p>
<p>The Court asserts, however, that because the police obtained two warrants for Vale's arrest there is "no reason . . . to suppose that it was impracticable for them to obtain a search warrant as well." The difficulty is that the two arrest warrants on which the Court seems to rely so heavily were not issued because of any present misconduct of Vale's; they were issued because the bond had been increased for an earlier narcotics charge then pending against Vale. When the police came to arrest Vale, they knew only that his bond had been increased. There is nothing in the record to indicate that, absent the increased bond, there would have been probable cause for an arrest, much less a search. Probable cause for the search arose for the first time when the police observed the activity of Vale and Saucier in and around the house.</p>
<p>I do not suggest that all arrests necessarily provide the basis for a search of the arrestee's house. In this case there is far more than a mere street arrest. The police also observed Vale's use of the house as a base of operations for his commercial business, his attempt to <span class="star-pagination">*41</span> return hurriedly to the house on seeing the officers, and the apparent destruction of evidence by the man with whom Vale was dealing. Furthermore the police arrival and Vale's arrest were plainly visible to anyone within the house, and the police had every reason to believe that someone in the house was likely to destroy the contraband if the search were postponed.</p>
<p>This case raises most graphically the question how does a policeman protect evidence necessary to the State if he must leave the premises to get a warrant, allowing the evidence he seeks to be destroyed. The Court's answer to that question makes unnecessarily difficult the conviction of those who prey upon society.</p>
<h2>NOTES</h2>
<p>[*]  In his Notice of Appeal, Vale asserted that the Louisiana Supreme Court in affirming the conviction had relied upon a state statute, Article 225 of the Louisiana Code of Criminal Procedure (1967), which provides in pertinent part:
</p>
<p>"A peace officer making an arrest shall take from the person arrested all weapons and incriminating articles which he may have about his person."</p>
<p>Although the state court referred to this statute in the course of its opinion, we do not understand its decision to be grounded on the statute. We therefore dismiss the appeal and treat the papers as a petition for certiorari, which is hereby granted. <span class="citation no-link">28 U. S. C. § 2103</span>.</p>
<p>[*]  The Fourth Amendment says:
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Vega v. Tekoh.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Vega v. Tekoh"
type: case
citation: "597 U.S. 134 (2022)"
parallel_cite: "213 L. Ed. 2d 479; 142 S. Ct. 2095"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2022
date_decided: 2022-06-23
docket: 21-499
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2022-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vega v. Tekoh
  varies_by_point: false
  scope_note: "Recent controlling decision; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6480695/vega-v-tekoh/"
  cluster_id: 6480695
  opinion_id: 6352828
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny"
related: ["[[Chavez v. Martinez]]", "[[Dickerson v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "section-1983", "qualified-immunity"]
holding: "A violation of the Miranda rules is not itself a violation of the Fifth Amendment and does not provide a basis for a § 1983 damages claim against the officer who took an un-Mirandized statement."
lake:
  record_id: Vega v. Tekoh
  status: verified
  projected_at: 2026-07-06
---

# Vega v. Tekoh

*597 U.S. 134 (2022)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Deputy Vega questioned Terence Tekoh at his workplace about a reported sexual assault without giving [[Miranda and Custodial Interrogation|Miranda warnings]]; Tekoh wrote an apologetic statement that was admitted at his criminal trial. The jury acquitted. Tekoh then sued Vega under 42 U.S.C. § 1983, claiming the admission of his un-Mirandized statement violated his Fifth Amendment rights. The Ninth Circuit held that using an un-Mirandized statement at a criminal trial can support a § 1983 claim.

## Issue
Whether a plaintiff may sue a police officer under § 1983 based on the admission at a criminal trial of a statement obtained without [[Miranda and Custodial Interrogation|Miranda warnings]] — i.e., whether a *[[Miranda v. Arizona|Miranda]]* violation is a deprivation of a right "secured by the Constitution and laws" for § 1983 purposes.

## Rule
No. "A violation of the *Miranda* rules does not provide a basis for a § 1983 claim." — 597 U.S. at 134 (Held). ^pin-134

*[[Miranda v. Arizona|Miranda]]* imposed a set of *prophylactic* rules to protect the Fifth Amendment privilege; those rules are not themselves the constitutional right, so their breach is not, by itself, a constitutional deprivation. The Court declined to treat the *[[Miranda v. Arizona|Miranda]]* rules as federal "law" creating a § 1983 cause of action because the benefits would be slight and the costs substantial, and "*Miranda* and its progeny provide sufficient protection for the Fifth Amendment right against compelled self-incrimination."

Concluding: "Because a violation of *Miranda* is not itself a violation of the Fifth Amendment, and because we see no justification for expanding *Miranda* to confer a right to sue under § 1983, the judgment of the Court of Appeals is reversed." — *Id.* (Alito, J., for the Court) (concluding paragraph). ^pin-134a

## Application
Tekoh's § 1983 theory rested entirely on the admission of his un-Mirandized statement. Because a *[[Miranda v. Arizona|Miranda]]* violation is not equivalent to a Fifth Amendment violation, that admission — even assuming it was error — did not deprive Tekoh of a right secured by the Constitution and laws within the meaning of § 1983. The proper remedy for a *[[Miranda v. Arizona|Miranda]]* violation is suppression of the statement in the criminal case, not a § 1983 damages action against the interrogating officer.

## Conclusion
A *[[Miranda v. Arizona|Miranda]]* violation is not itself a constitutional violation and cannot ground a § 1983 suit. The Ninth Circuit's judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Vega* extends the logic of [[Chavez v. Martinez]] (the Self-Incrimination Clause is a trial right) and reaffirms that *[[Miranda v. Arizona|Miranda]]*'s rules, though constitutionally based (see [[Dickerson v. United States]]), are prophylactic and do not by themselves create § 1983 liability.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny*

## Sources
- *Vega v. Tekoh*, 597 U.S. 134 (2022) — https://www.courtlistener.com/opinion/6480695/vega-v-tekoh/ — pinpoints: 134 (Held); conclusion at end of opinion (Alito, J.). (CourtListener's copy is the slip opinion; official U.S. Reports internal pagination shown as "597 U.S. ____".)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ef52ec9b11d9bd71", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Vega v. Tekoh"}, "payload": {"all": [{"cite": "597 U.S. 134", "page": "134", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "597"}, {"cite": "213 L. Ed. 2d 479", "page": "479", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "213"}, {"cite": "142 S. Ct. 2095", "page": "2095", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}], "display": "597 U.S. 134", "official": {"cite": "597 U.S. 134", "page": "134", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "597"}, "official_selection_present": true, "record_id": "Vega v. Tekoh"}}
{"assertion_id": "cd69ed6c5d178785", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-134a", "record_id": "Vega v. Tekoh"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-134a", "pinpoint_status": "slip-only", "quote": "Concluding:", "quote_fidelity": "mismatch", "record_id": "Vega v. Tekoh", "star_marker": null}}
{"assertion_id": "fd27d738408b41c9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-134", "record_id": "Vega v. Tekoh"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-134", "pinpoint_status": "slip-only", "quote": "for § 1983 purposes. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Vega v. Tekoh", "star_marker": null}}
{"assertion_id": "733126260a2eada7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Vega v. Tekoh"}, "payload": {"as_of_content": "2022-06-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Vega v. Tekoh", "scope_note": "Recent controlling decision; good law.", "varies_by_point": false}}
```

### lake record — Vega v. Tekoh

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vega v. Tekoh",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vega v. Tekoh",
    "case_name_short": "Vega",
    "case_name_full": "",
    "input_case_name": "Vega v. Tekoh",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2022-06-23",
    "year": 2022,
    "docket": "21-499",
    "cluster_id": 6480695,
    "lead_opinion_id": 6352828,
    "sibling_ids": [
      6352828
    ],
    "absolute_url": "/opinion/6480695/vega-v-tekoh/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "597 U.S. 134",
      "volume": "597",
      "reporter": "U.S.",
      "page": "134",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "213 L. Ed. 2d 479",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2095",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "597 U.S. 134",
        "volume": "597",
        "reporter": "U.S.",
        "page": "134",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 479",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2095",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "597 U.S. 134",
    "official_selection": {
      "court_class": "scotus",
      "selected": "597 U.S. 134",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-134",
      "page": null,
      "quote": "for \u00a7 1983 purposes. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-134a",
      "page": null,
      "quote": "Concluding:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2022-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Vega v. Tekoh",
    "varies_by_point": false,
    "scope_note": "Recent controlling decision; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Ronald Fosnight v. Robert Jones",
          "cluster_id": 7441273,
          "cite": [
            "41 F.4th 916"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Holloway v. City of Milwaukee",
          "cluster_id": 7855045,
          "cite": [
            "43 F.4th 760"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Logan",
          "cluster_id": 9486489,
          "cite": [
            "2024 IL 129054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waukegan Potawatomi Casino, LLC v. City of Waukegan",
          "cluster_id": 10333614,
          "cite": [
            "128 F.4th 871"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Midland County",
          "cluster_id": 10116259,
          "cite": [
            "116 F.4th 384"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terence Tekoh v. County of Los Angeles",
          "cluster_id": 9418187,
          "cite": [
            "75 F.4th 1264"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coulter",
          "cluster_id": 6624576,
          "cite": [
            "41 F.4th 451"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Travis Lester",
          "cluster_id": 9494065,
          "cite": [
            "98 F.4th 768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Salter v. City of Detroit, Mich.",
          "cluster_id": 10361064,
          "cite": [
            "133 F.4th 527"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schaefer",
          "cluster_id": 10311854,
          "cite": [
            "563 P.3d 424",
            "2025 UT App 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dale E. Holloway, Jr. v. Governor, State of New Hampshire, et al.",
          "cluster_id": 10695608,
          "cite": [
            "2022 DNH 097"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Blackmon v. Gregory Jones",
          "cluster_id": 10360714,
          "cite": [
            "132 F.4th 522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zuniga De La Cruz v. Garland",
          "cluster_id": 9441968,
          "cite": [
            "86 F.4th 1236"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willey v. Springfield Twp.",
          "cluster_id": 10862344,
          "cite": [
            "2026 Ohio 1842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O.W. v. Marie Carr",
          "cluster_id": 10840933,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Loren Daniels",
          "cluster_id": 10770631,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rajeri Curry",
          "cluster_id": 10710491,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warren v. State",
          "cluster_id": 10679805,
          "cite": [
            "878 S.E.2d 438",
            "314 Ga. 598"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brandon Paul Janssen v. State of Florida",
          "cluster_id": 10661543,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Thomas Michael Pastor, Jr.",
          "cluster_id": 10658570,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "M.A. v. J.H.M.",
          "cluster_id": 10592887,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zachary Joseph Penna v. State of Florida",
          "cluster_id": 10419663,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Giovani Fuster Melendez",
          "cluster_id": 10367639,
          "cite": [
            "565 P.3d 1034"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrett Dale Reeves v. the State of Texas",
          "cluster_id": 10333815,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vega v. Tekoh:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6352828) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      },
      "lane2_top_cited": {
        "query": "cites:(6352828)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA2NjE1NDMmdD1vJmQ9MjAyNi0wNy0wNiZwPTI%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%286352828%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6352828)",
        "reviewed": 25,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 25,
        "triage_read": 0,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6352828)",
    "indexed_citing_opinions": 32,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6352828,
        "count": 32,
        "count_source": "search"
      }
    ],
    "citation_count": 154,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vega-v-tekoh.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MjUyODMmcz05NDM4NDI4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%286352828%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 6352828,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 110268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 4651954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 4692581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 7263680,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 8985601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9413177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9417767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9419051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9422515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9422839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9423233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9423964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9424454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9425260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9425753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9426587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9427972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9429930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9430786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9431937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9432786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9433984,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9434762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9435335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9485375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 6352828,
        "cited_id": 9842134,
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
    "date_created": "2026-07-06T03:47:05Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:50:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:47:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vega v. Tekoh

```
(Slip Opinion)              OCTOBER TERM, 2021                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                               VEGA v. TEKOH

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

       No. 21–499.      Argued April 20, 2022—Decided June 23, 2022
The case arose out of the interrogation of respondent, Terence Tekoh, by
  petitioner, Los Angeles County Sheriff ’s Deputy Carlos Vega. Deputy
  Vega questioned Tekoh at the medical center where Tekoh worked re-
  garding the reported sexual assault of a patient. Vega did not inform
  Tekoh of his rights under Miranda v. Arizona, 384 U. S. 436. Tekoh
  eventually provided a written statement apologizing for inappropri-
  ately touching the patient’s genitals. Tekoh was prosecuted for unlaw-
  ful sexual penetration. His written statement was admitted against
  him at trial. After the jury returned a verdict of not guilty, Tekoh sued
  Vega under 42 U. S. C. §1983, seeking damages for alleged violations
  of his constitutional rights. The Ninth Circuit held that the use of an
  un-Mirandized statement against a defendant in a criminal proceed-
  ing violates the Fifth Amendment and may support a §1983 claim
  against the officer who obtained the statement.
Held: A violation of the Miranda rules does not provide a basis for a
 §1983 claim. Pp. 4–16.
    (a) Section 1983 provides a cause of action against any person acting
 under color of state law who “subjects” a person “to the deprivation of
 any rights, privileges, or immunities secured by the Constitution and
 laws.” Tekoh argues that a violation of Miranda constitutes a violation
 of the Fifth Amendment right against compelled self-incrimination.
 That is wrong. Pp. 4–13.
    (1) In Miranda, the Court concluded that additional procedural pro-
 tections were necessary to prevent the violation of the Fifth Amend-
 ment right against self-incrimination when suspects who are in cus-
 tody are interrogated by the police. Miranda imposed a set of
 prophylactic rules requiring that custodial interrogation be preceded
2                             VEGA v. TEKOH

                                  Syllabus

    by now-familiar warnings and disallowing the use of statements ob-
    tained in violation of these new rules by the prosecution in its case-in-
    chief. 384 U. S., at 444, 479. Miranda did not hold that a violation of
    the rules it established necessarily constitute a Fifth Amendment vio-
    lation. That makes sense, as an un-Mirandized suspect in custody may
    make self-incriminating statements without any hint of compulsion.
    The Miranda Court stated that the Constitution did not itself require
    “adherence to any particular solution for the inherent compulsions of
    the interrogation process” and that its decision “in no way create[d] a
    constitutional straitjacket.” Id., at 467. Since Miranda, the Court has
    repeatedly described Miranda rules as “prophylactic.” Pp. 4–7.
       (2) After Miranda, the Court engaged in the process of charting the
    dimensions of these new prophylactic rules, and, in doing so, weighed
    the benefits and costs of any clarification of the prophylactic rules’
    scope. See Maryland v. Shatzer, 559 U. S. 98, 106. Some post-Mi-
    randa decisions found that the balance of interests justified re-
    strictions that would not have been possible if Miranda described the
    Fifth Amendment right as opposed to a set of rules designed to protect
    that right. For example, in Harris v. New York, 401 U. S. 222, 224–
    226, the Court held that a statement obtained in violation of Miranda
    could be used to impeach the testimony of a defendant, even though an
    involuntary statement obtained in violation of the Fifth Amendment
    could not have been employed in this way. In Michigan v. Tucker, 417
    U. S. 443, 450–452, n. 26, the Court held that the “fruits” of an un-
    Mirandized statement can be admitted. In doing so, the Court distin-
    guished police conduct that “abridge[s] [a person’s] constitutional priv-
    ilege against compulsory self-incrimination” from conduct that “de-
    part[s] only from the prophylactic standards later laid down by this
    Court in Miranda to safeguard that privilege.” 417 U. S., at 445–446.
    Similarly, in Oregon v. Elstad, 470 U. S. 298, the Court, following the
    reasoning in Tucker, refused to exclude a signed confession and em-
    phasized that an officer’s error “in administering the prophylactic Mi-
    randa procedures . . . should not breed the same irremediable conse-
    quences as police infringement of the Fifth Amendment itself.” Id., at
    309.
       While many of the Court’s decisions imposed limits on Miranda’s
    prophylactic rules, other decisions found that the balance of interests
    called for expansion. For example, in Doyle v. Ohio, 426 U. S. 610, the
    Court held that silence following a Miranda warning cannot be used
    to impeach. The Court acknowledged that Miranda warnings are
    “prophylactic,” 426 U. S., at 617, but it found that allowing the use of
    post-warning silence would undermine the warnings’ implicit promise
    that silence would not be used to convict. Id., at 618. Likewise, in
    Withrow v. Williams, 507 U. S. 680, the Court rejected an attempt to
                    Cite as: 597 U. S. ____ (2022)                      3

                               Syllabus

restrict Miranda’s application in collateral proceedings based on the
reasoning in Stone v. Powell, 428 U. S. 465 (1976). Once again ac-
knowledging that Miranda adopted prophylactic rules, the Court bal-
anced the competing interests and found that the costs of adopting a
Stone-like rule outweighed any benefits. In sum, the Court’s post-Mi-
randa cases acknowledge the prophylactic nature of the Miranda rules
and engage in cost-benefit analysis to define their scope. Pp. 7–11.
    (3) The Court’s decision in Dickerson v. United States, 530 U. S. 428,
did not upset the firmly established prior understanding of Miranda
as a prophylactic decision. Dickerson involved a federal statute, 18
U. S. C. §3501, that effectively overruled Miranda by making the ad-
missibility of a statement given during custodial interrogation turn
solely on whether it was made voluntarily. 530 U. S., at 431–432. The
Court held that Congress could not abrogate Miranda by statute be-
cause Miranda was a “constitutional decision” that adopted a “consti-
tutional rule,” 530 U. S., at 438–439, and the Court noted that these
rules could not have been made applicable to the States if they did not
have that status, see ibid. At the same time, the Court made it clear
that it was not equating a violation of the Miranda rules with an out-
right Fifth Amendment violation. Instead, the Dickerson Court de-
scribed the Miranda rules as “constitutionally based” with “constitu-
tional underpinnings,” 530 U. S., at 440, and n. 5. Those formulations
obviously avoided saying that a Miranda violation is the same as a
violation of the Fifth Amendment right. Miranda was a “constitutional
decision” and it adopted a “constitutional rule” in the sense that the
decision was based on the Court’s judgment about what is required to
safeguard that constitutional right. And when the Court adopts a con-
stitutional prophylactic rule of this nature, Dickerson concluded, the
rule has the status of a “La[w] of the United States” that is binding on
the States under the Supremacy Clause (as Miranda implicitly held,
since three of the four decisions it reversed came from state court, 384
U. S., at 491–494, 497–499), and the rule cannot be altered by ordinary
legislation. Dickerson thus asserted a bold and controversial claim—
that this Court has the authority to create constitutionally based
prophylactic rules that bind both federal and state courts—but Dick-
erson cannot be understood any other way consistent with the Court’s
prior decisions. Subsequent cases confirm that Dickerson did not up-
end the Court’s understanding of the Miranda rules as prophylactic.
In sum, a violation of Miranda does not necessarily constitute a viola-
tion of the Constitution, and therefore such a violation does not consti-
tute “the deprivation of [a] right . . . secured by the Constitution” for
purposes of §1983. Pp. 11–13.
    (b) A §1983 claim may also be based on “the deprivation of any rights
. . . secured by the . . . laws.” But the argument that Miranda rules
4                             VEGA v. TEKOH

                                  Syllabus

    constitute federal “law” that can provide the ground for a §1983 claim
    cannot succeed unless Tekoh can persuade the Court that this “law”
    should be expanded to include the right to sue for damages under
    §1983. “A judicially crafted” prophylactic rule should apply “only
    where its benefits outweigh its costs,” Shatzer, 559 U. S., at 106. Here,
    while the benefits of permitting the assertion of Miranda claims under
    §1983 would be slight, the costs would be substantial. For example,
    allowing a claim like Tekoh’s would disserve “judicial economy,” Park-
    lane Hosiery Co. v. Shore, 439 U. S. 322, 326, by requiring a federal
    judge or jury to adjudicate a factual question (whether Tekoh was in
    custody when questioned) that had already been decided by a state
    court. Allowing §1983 suits based on Miranda claims could also pre-
    sent many procedural issues. Miranda and its progeny provide suffi-
    cient protection for the Fifth Amendment right against compelled self-
    incrimination. Pp. 13–16.
985 F. 3d 713, reversed and remanded.

   ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and THOMAS, GORSUCH, KAVANAUGH, and BARRETT, JJ., joined. KAGAN,
J., filed a dissenting opinion, in which BREYER and SOTOMAYOR, JJ.,
joined.
                        Cite as: 597 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 21–499
                                    _________________


 CARLOS VEGA, PETITIONER v. TERENCE B. TEKOH
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                                  [June 23, 2022]

   JUSTICE ALITO delivered the opinion of the Court.
   This case presents the question whether a plaintiff may
sue a police officer under Rev. Stat. §1979, 42 U. S. C.
§1983, based on the allegedly improper admission of an “un-
Mirandized”1 statement in a criminal prosecution. The case
arose out of the interrogation of respondent, Terence Tekoh,
by petitioner, Los Angeles County Sheriff ’s Deputy Carlos
Vega. Deputy Vega questioned Tekoh at his place of em-
ployment and did not give him a Miranda warning. Tekoh
was prosecuted, and his confession was admitted into evi-
dence, but the jury returned a verdict of not guilty. Tekoh
then sued Vega under §1983, and the United States Court
of Appeals for the Ninth Circuit held that the use of Tekoh’s
un-Mirandized statement provided a valid basis for a §1983
claim against Vega. We now reject this extension of our
Miranda case law.
                             I
  In March 2014, Tekoh was working as a certified nursing
assistant at a Los Angeles medical center. When a female
patient accused him of sexually assaulting her, the hospital
——————
 1 See Miranda v. Arizona, 384 U. S. 436 (1966).
2                      VEGA v. TEKOH

                     Opinion of the Court

staff reported the accusation to the Los Angeles County
Sheriff ’s Department, and Deputy Vega responded. Vega
questioned Tekoh at length in the hospital, and Tekoh even-
tually provided a written statement apologizing for inap-
propriately touching the patient’s genitals. The parties dis-
pute whether Vega used coercive investigatory techniques
to extract the statement, but it is undisputed that he never
informed Tekoh of his rights under Miranda v. Arizona, 384
U. S. 436 (1966), which held that during a custodial inter-
rogation police officers must inform a suspect that “he has
the right to remain silent, that anything he says can be used
against him in a court of law, that he has the right to the
presence of an attorney, and that if he cannot afford an at-
torney one will be appointed for him prior to any question-
ing.” Id., at 479.
   Tekoh was arrested and charged in California state court
with unlawful sexual penetration. At Tekoh’s first trial, the
judge held that Miranda had not been violated because
Tekoh was not in custody when he provided the statement,
but the trial resulted in a mistrial. When Tekoh was re-
tried, a second judge again denied his request to exclude the
confession. This trial resulted in acquittal, and Tekoh then
brought this action under 42 U. S. C. §1983 against Vega
and several other defendants seeking damages for alleged
violations of his constitutional rights, including his Fifth
Amendment right against compelled self-incrimination.
   When this §1983 case was first tried, the jury returned a
verdict in favor of Vega, but the judge concluded that he had
given an improper jury instruction and thus granted a new
trial. Before the second trial, Tekoh asked the court to in-
struct the jury that it was required to find that Vega vio-
lated the Fifth Amendment right against compelled self-
incrimination if it determined that he took a statement
from Tekoh in violation of Miranda and that the statement
was then improperly used against Tekoh at his criminal
trial. The District Court declined, reasoning that Miranda
                 Cite as: 597 U. S. ____ (2022)            3

                     Opinion of the Court

established a prophylactic rule and that such a rule could
not alone provide a ground for §1983 liability. Instead, the
jury was asked to decide whether Tekoh’s Fifth Amendment
right had been violated. The court instructed the jury to
determine, based on “the totality of all the surrounding cir-
cumstances,” whether Tekoh’s statement had been “im-
properly coerced or compelled,” and the court explained
that “[a] confession is improperly coerced or compelled . . .
if a police officer uses physical or psychological force or
threats not permitted by law to undermine a person’s abil-
ity to exercise his or her free will.” App. to Pet. for Cert.
119a. The jury found in Vega’s favor, and Tekoh appealed.
   A Ninth Circuit panel reversed, holding that the “use of
an un-Mirandized statement against a defendant in a crim-
inal proceeding violates the Fifth Amendment and may
support a §1983 claim” against the officer who obtained the
statement. Tekoh v. County of Los Angeles, 985 F. 3d 713,
722 (2021). The panel acknowledged that this Court has
repeatedly said that Miranda adopted prophylactic rules
designed to protect against constitutional violations and
that the decision did not hold that the contravention of
those rules necessarily constitutes a constitutional viola-
tion. See 985 F. 3d, at 719–720. But the panel thought that
our decision in Dickerson v. United States, 530 U. S. 428
(2000), “made clear that the right of a criminal defendant
against having an un-Mirandized statement introduced in
the prosecution’s case in chief is indeed a right secured by
the Constitution.” 985 F. 3d, at 720. Therefore the panel
concluded that Tekoh could establish a violation of his Fifth
Amendment right against compelled self-incrimination
simply by showing that Miranda had been violated. See
985 F. 3d, at 720. The panel thus remanded the case for a
new trial.
   Vega’s petition for rehearing en banc was denied, but
Judge Bumatay, joined by six other judges, filed a dissent
4                       VEGA v. TEKOH

                      Opinion of the Court

from the denial of rehearing. Tekoh v. County of Los Ange-
les, 997 F. 3d 1260, 1261, 1264–1272 (CA9 2021). We then
granted certiorari. 595 U. S. ___ (2022).
                               II
   Section 1983 provides a cause of action against any per-
son acting under color of state law who “subjects” a person
or “causes [a person] to be subjected . . . to the deprivation
of any rights, privileges, or immunities secured by the Con-
stitution and laws.” The question we must decide is
whether a violation of the Miranda rules provides a basis
for a claim under §1983. We hold that it does not.
                               A
   If a Miranda violation were tantamount to a violation of
the Fifth Amendment, our answer would of course be differ-
ent. The Fifth Amendment, made applicable to the States
by the Fourteenth Amendment, Malloy v. Hogan, 378 U. S.
1, 6 (1964), provides that “[n]o person . . . shall be compelled
in any criminal case to be a witness against himself.” This
Clause “permits a person to refuse to testify against himself
at a criminal trial in which he is a defendant” and “also
‘privileges him not to answer official questions put to him
in any other proceeding, civil or criminal, formal or infor-
mal, where the answers might incriminate him in future
criminal proceedings.’ ” Minnesota v. Murphy, 465 U. S.
420, 426 (1984) (quoting Lefkowitz v. Turley, 414 U. S. 70,
77 (1973)). In addition, the right bars the introduction
against a criminal defendant of out-of-court statements ob-
tained by compulsion. See, e.g., Bram v. United States, 168
U. S. 532, 565 (1897); Miranda, 384 U. S., at 466; Michigan
v. Tucker, 417 U. S. 433, 440–442 (1974).
   In Miranda, the Court concluded that additional proce-
dural protections were necessary to prevent the violation of
this important right when suspects who are in custody are
interrogated by the police. To afford this protection, the
                 Cite as: 597 U. S. ____ (2022)            5

                     Opinion of the Court

Court required that custodial interrogation be preceded by
the now-familiar warnings mentioned above, and it directed
that statements obtained in violation of these new rules
may not be used by the prosecution in its case-in-chief. 384
U. S., at 444, 479.
  In this case, the Ninth Circuit held—and Tekoh now ar-
gues, Brief for Respondent 20—that a violation of Miranda
constitutes a violation of the Fifth Amendment right
against compelled self-incrimination, but that is wrong.
Miranda itself and our subsequent cases make clear that
Miranda imposed a set of prophylactic rules. Those rules,
to be sure, are “constitutionally based,” Dickerson, 530
U. S., at 440, but they are prophylactic rules nonetheless.
                              B
  Miranda itself was clear on this point. Miranda did not
hold that a violation of the rules it established necessarily
constitute a Fifth Amendment violation, and it is difficult
to see how it could have held otherwise. For one thing, it is
easy to imagine many situations in which an un-
Mirandized suspect in custody may make self-
incriminating statements without any hint of compulsion.
In addition, the warnings that the Court required included
components, such as notification of the right to have re-
tained or appointed counsel present during questioning,
that do not concern self-incrimination per se but are instead
plainly designed to safeguard that right. And the same is
true of Miranda’s detailed rules about the waiver of the
right to remain silent and the right to an attorney. 384
U. S., at 474–479.
  At no point in the opinion did the Court state that a vio-
lation of its new rules constituted a violation of the Fifth
Amendment right against compelled self-incrimination. In-
stead, it claimed only that those rules were needed to safe-
guard that right during custodial interrogation. See id., at
439 (describing its rules as “procedures which assure that
6                      VEGA v. TEKOH

                     Opinion of the Court

the individual is accorded his privilege under the Fifth
Amendment”); id., at 444 (describing rules as “procedural
safeguards”); id., at 457 (“appropriate safeguards”); id., at
458 (“adequate protective devices”); id., at 467 (“safe-
guards”).
   In accordance with this understanding of the nature of
the rules it imposed, the Miranda Court stated quite clearly
that the Constitution did not itself require “adherence to
any particular solution for the inherent compulsions of the
interrogation process” and that its decision “in no way cre-
ate[d] a constitutional straitjacket.” Ibid. The opinion
added that its new rules might not be needed if Congress or
the States adopted “other procedures which are at least as
effective,” ibid., and the opinion suggested that there might
not have been any actual Fifth Amendment violations in
the four cases that were before the Court. See id., at 457
(“In these cases, we might not find the defendants’ state-
ments to have been involuntary in traditional terms”). The
Court could not have said any of these things if a violation
of the Miranda rules necessarily constituted a violation of
the Fifth Amendment.
   Since Miranda, the Court has repeatedly described the
rules it adopted as “prophylactic.” See Howes v. Fields, 565
U. S. 499, 507 (2012); J. D. B. v. North Carolina, 564 U. S.
261, 269 (2011); Maryland v. Shatzer, 559 U. S. 98, 103
(2010); Montejo v. Louisiana, 556 U. S. 778, 794 (2009); Da-
vis v. United States, 512 U. S. 452, 458 (1994); Brecht v.
Abrahamson, 507 U. S. 619, 629 (1993); Withrow v. Wil-
liams, 507 U. S. 680, 691 (1993); McNeil v. Wisconsin, 501
U. S. 171, 176 (1991); Michigan v. Harvey, 494 U. S. 344,
350 (1990); Duckworth v. Eagan, 492 U. S. 195, 203 (1989);
Arizona v. Roberson, 486 U. S. 675, 681 (1988); Connecticut
v. Barrett, 479 U. S. 523, 528 (1987); Oregon v. Elstad, 470
U. S. 298, 309 (1985); New York v. Quarles, 467 U. S. 649,
654 (1984); South Dakota v. Neville, 459 U. S. 553, 564, n.
15 (1983); United States v. Henry, 447 U. S. 264, 274 (1980);
                      Cite as: 597 U. S. ____ (2022)                     7

                          Opinion of the Court

North Carolina v. Butler, 441 U. S. 369, 374 (1979); Brown
v. Illinois, 422 U. S. 590, 600 (1975); Michigan v. Tucker,
417 U. S., at 439; and Michigan v. Payne, 412 U. S. 47, 53
(1973).2
                               C
   After Miranda was handed down, the Court engaged in
the process of charting the dimensions of these new prophy-
lactic rules. As we would later spell out, this process en-
tailed a weighing of the benefits and costs of any clarifica-
tion of the rules’ scope. See Shatzer, 559 U. S., at 106 (“A
judicially crafted rule is ‘justified only by reference to its
prophylactic purpose,’ . . . and applies only where its bene-
fits outweigh its costs”).
   Some post-Miranda decisions found that the balance of
interests justified restrictions that would not have been
possible if Miranda represented an explanation of the
meaning of the Fifth Amendment right as opposed to a set
of rules designed to protect that right. For example, in Har-
ris v. New York, 401 U. S. 222, 224–226 (1971), the Court
held that a statement obtained in violation of Miranda
could be used to impeach the testimony of a defendant, even
though an involuntary statement obtained in violation of
the Fifth Amendment could not have been employed in this
way. See Mincey v. Arizona, 437 U. S. 385, 398 (1978)

——————
   2 Tekoh cites Orozco v. Texas, 394 U. S. 324 (1969), which characterized

the admission of an unwarned statement in the prosecutor’s case-in-chief
as a “flat violation of the Self-Incrimination Clause of the Fifth Amend-
ment as construed in Miranda.” Id., at 326 (emphasis added); Brief for
Respondent 21, 29. But the Court made this assertion in a three-para-
graph opinion without any additional analysis, and did not purport to go
beyond Miranda, which, as we have explained, does not support the prop-
osition that a Miranda violation equates to a Fifth Amendment violation.
See Orozco, 394 U. S., at 327 (“We do not . . . expand or extend to the
slightest extent our Miranda decision”). Likewise, the decision predates
the subsequent case law defining the scope of the Miranda rules. See
infra, this page and 8–11.
8                      VEGA v. TEKOH

                      Opinion of the Court

(“[A]ny criminal trial use against a defendant of his invol-
untary statement is a denial of due process of law” (empha-
sis deleted)). Engaging in the process we described in
Shatzer, the Harris Court considered the benefits of forbid-
ding impeachment but dismissed “the speculative possibil-
ity” that this would discourage “impermissible police con-
duct,” and on the other side of the scale, it feared that
barring impeachment would turn Miranda into “a license
to use perjury by way of a defense.” 401 U. S., at 225–226.
   A similar analysis was used in Michigan v. Tucker, 417
U. S. 443, 450–452, n. 26 (1974), where the Court held that
the “fruits” of an un-Mirandized statement can be admit-
ted. The Court noted that “the ‘fruits’ of police conduct
which actually infringe[s]” a defendant’s constitutional
rights must be suppressed. Id., at 445; see also Wong Sun
v. United States, 371 U. S. 471 (1963) (applying the rule in
the context of a Fourth Amendment violation). But the
Court distinguished police conduct that “abridge[s] [a per-
son’s] constitutional privilege against compulsory self-
incrimination” from conduct that “depart[s] only from the
prophylactic standards later laid down by this Court in Mi-
randa to safeguard that privilege.” 417 U. S., at 445–446.
Because there had been only a Miranda violation in that
case, the Wong Sun rule of automatic exclusion was found
to be inapplicable. See 417 U. S., at 445–446. Instead, the
Court asked whether the Miranda rules’ prophylactic pur-
poses justified the exclusion of the fruits of the violation,
and after “balancing the interests involved,” it held that ex-
clusion was not required. 417 U. S., at 447–452.
   In New York v. Quarles, 467 U. S. 649, 654–657 (1984),
the Court held that statements obtained in violation of Mi-
randa need not be suppressed when the questioning is con-
ducted to address an ongoing “public safety” concern. The
Court reasoned that Miranda warnings are “ ‘not them-
selves rights protected by the Constitution’ ” and that “the
need for answers to questions in a situation posing a threat
                      Cite as: 597 U. S. ____ (2022)                      9

                           Opinion of the Court

to the public safety outweigh[ed] the need for the prophy-
lactic rule.” 467 U. S., at 654, 657.
   Finally, in Elstad, 470 U. S. 298, the Court again distin-
guished between a constitutional violation and a violation
of Miranda. In that case, a suspect in custody was initially
questioned without receiving a Miranda warning, and the
statements made at that time were suppressed. 470 U. S.,
at 301–302. But the suspect was later given Miranda warn-
ings, chose to waive his Miranda rights, and signed a writ-
ten confession. 470 U. S., at 301. Asked to decide whether
this confession was admissible, the Court followed the rea-
soning in Tucker and again held that the fruit-of-the-
poisonous-tree rule that applies to constitutional violations
does not apply to violations of Miranda. 470 U. S., at 306–
309, 318. The Court refused to exclude the signed confes-
sion and emphasized that an officer’s error “in administer-
ing the prophylactic Miranda procedures . . . should not
breed the same irremediable consequences as police in-
fringement of the Fifth Amendment itself.” 3 Id., at 309.



——————
   3 Two other decisions fall into this same category, but in both there was

no opinion of the Court. In Chavez v. Martinez, 538 U. S. 760 (2003), the
suspect gave an un-Mirandized statement while in custody but was
never charged with a crime. The Court held that the suspect could not
bring a 42 U. S. C. §1983 claim against the officer who questioned him,
and Justice Souter, who cast the necessary fifth vote on the issue,
reached that conclusion based on “a realistic assessment of costs and
risks” of “expand[ing] protection of the privilege against compelled self-
incrimination to the point of the civil liability” at issue. 538 U. S., at
778–779 (opinion concurring in judgment).
   In United States v. Patane, 542 U. S. 630 (2004), the Court once again
held that Miranda does not require the suppression of the fruits of a un-
Mirandized statement made during custodial questioning, and two of the
five Justices in the majority engaged in the same type of balancing that
was used in Michigan v. Tucker, 417 U. S. 433 (1974), and Elstad. See
Patane, 542 U. S., at 644–645 (Kennedy, J., concurring in judgment); see
also id., at 641–644 (plurality opinion).
10                     VEGA v. TEKOH

                     Opinion of the Court

  It is hard to see how these decisions could stand if a vio-
lation of Miranda constituted a violation of the Fifth
Amendment.
                              D
   While these decisions imposed limits on Miranda’s
prophylactic rules, other decisions found that the balance of
interests called for expansion. In Doyle v. Ohio, 426 U. S.
610, 617–619 (1976), the Court held that silence following a
Miranda warning cannot be used to impeach. The Court
acknowledged that Miranda warnings are “prophylactic,”
426 U. S., at 617, and it recognized the prosecution’s need
to test a defendant’s exculpatory story through cross-
examination, id., at 616–618. But it found that allowing
the use of post-warning silence would undermine the warn-
ings’ implicit promise that silence would not be used to con-
vict. Id., at 618.
   Similarly, in Roberson, 486 U. S., at 682, the Court held
that a suspect’s post-warning request for counsel with re-
spect to one offense barred later interrogation without
counsel regarding a different offense. Describing the Mi-
randa rules as “prophylactic protections,” 486 U. S., at 681,
the Court concluded that both law enforcement and crimi-
nal defendants would benefit from a bright-line, id., at 681–
682.
   Finally, in Withrow v. Williams, 507 U. S. 680, the Court
rejected an attempt to restrict Miranda’s application in col-
lateral proceedings based on the reasoning in Stone v. Pow-
ell, 428 U. S. 465 (1976). In Stone, the Court had held that
a defendant who has had a full and fair opportunity to seek
suppression of evidence allegedly seized in violation of the
Fourth Amendment may not obtain federal habeas relief on
that ground, id., at 494–495, and in Withrow, a state prison
warden argued that a similar rule should apply to a habeas
petitioner who had been given an opportunity to litigate a
Miranda claim at trial, see 507 U. S., at 688–690. Once
                  Cite as: 597 U. S. ____ (2022)           11

                      Opinion of the Court

again acknowledging that Miranda adopted prophylactic
rules, the Court balanced the competing interests and
found that the costs of adopting the warden’s argument out-
weighed any benefits. On the cost side, the Court noted
that enforcing Miranda “safeguards ‘a fundamental trial
right” and furthers “the correct ascertainment of guilt” at
trial. 507 U. S., at 691–692. And on the other side, the
Court found that the adoption of a Stone-like rule “would
not significantly benefit the federal courts in their exercise
of habeas jurisdiction, or advance the cause of federalism in
any substantial way.” 507 U. S., at 693.
   Thus, all the post-Miranda cases we have discussed
acknowledged the prophylactic nature of the Miranda rules
and engaged in cost-benefit analysis to define the scope of
these prophylactic rules.
                              E
   Contrary to the decision below and Tekoh’s argument
here, see Brief for Respondent 24, our decision in Dickerson,
530 U. S. 428, did not upset the firmly established prior un-
derstanding of Miranda as a prophylactic decision. Dicker-
son involved a federal statute, 18 U. S. C. §3501, that effec-
tively overruled Miranda by making the admissibility of a
statement given during custodial interrogation turn solely
on whether it was made voluntarily. 530 U. S., at 431–432.
The Court held that Congress could not abrogate Miranda
by statute because Miranda was a “constitutional decision”
that adopted a “constitutional rule,” 530 U. S., at 438–439,
and the Court noted that these rules could not have been
made applicable to the States if it did not have that status,
see ibid.
   At the same time, however, the Court made it clear that
it was not equating a violation of the Miranda rules with
an outright Fifth Amendment violation. For one thing, it
reiterated Miranda’s observation that “the Constitution
would not preclude legislative solutions that differed from
12                          VEGA v. TEKOH

                           Opinion of the Court

the prescribed Miranda warnings but which were ‘at least
as effective in apprising accused persons’ ” of their rights.
530 U. S., at 440 (quoting Miranda, 384 U. S., at 467).
  Even more to the point, the Court rejected the dissent’s
argument that §3501 could not be held unconstitutional un-
less “Miranda warnings are required by the Constitution,
in the sense that nothing else will suffice to satisfy consti-
tutional requirements.” 530 U. S., at 442. The Court’s an-
swer, in substance, was that the Miranda rules, though not
an explication of the meaning of the Fifth Amendment
right, are rules that are necessary to protect that right (at
least until a better alternative is found and adopted). See
530 U. S., at 441–443. Thus, in the words of the Dickerson
Court, the Miranda rules are “constitutionally based” and
have “constitutional underpinnings.” 530 U. S., at 440, and
n. 5. But the obvious point of these formulations was to
avoid saying that a Miranda violation is the same as a vio-
lation of the Fifth Amendment right.
  What all this boils down to is basically as follows. The
Miranda rules are prophylactic rules that the Court found
to be necessary to protect the Fifth Amendment right
against compelled self-incrimination. In that sense, Mi-
randa was a “constitutional decision” and it adopted a “con-
stitutional rule” because the decision was based on the
Court’s judgment about what is required to safeguard that
constitutional right. And when the Court adopts a consti-
tutional prophylactic rule of this nature, Dickerson con-
cluded, the rule has the status of a “La[w] of the United
States” that is binding on the States under the Supremacy
Clause 4 (as Miranda implicitly held, since three of the four
decisions it reversed came from state court, 384 U. S., at
491–494, 497–499), and the rule cannot be altered by ordi-
nary legislation.

——————
 4 U. S. Const., Art. VI, §2.
                     Cite as: 597 U. S. ____ (2022)                    13

                          Opinion of the Court

  This was a bold and controversial claim of authority,5 but
we do not think that Dickerson can be understood any other
way without (1) taking the insupportable position that a
Miranda violation is tantamount to a violation of the Fifth
Amendment, (2) calling into question the prior decisions
that were predicated on the proposition that a Miranda vi-
olation is not the same as a constitutional violation, and (3)
excising from the United States Reports a mountain of
statements describing the Miranda rules as prophylactic.
  Subsequent cases confirm that Dickerson did not upend
the Court’s understanding of the Miranda rules as prophy-
lactic. See, e.g., supra, at 6–7 (collecting post-Dickerson
cases).
  In sum, a violation of Miranda does not necessarily con-
stitute a violation of the Constitution, and therefore such a
violation does not constitute “the deprivation of [a] right . . .
secured by the Constitution.” 42 U. S. C. §1983.
                              III
  This conclusion does not necessarily dictate reversal be-
cause a §1983 claim may also be based on “the deprivation
of any rights, privileges, or immunities secured by the . . .
laws.” (Emphasis added.) It may thus be argued that the
Miranda rules constitute federal “law” and that an abridg-
ment of those rules can therefore provide the ground for a


——————
   5 Whether this Court has the authority to create constitutionally based

prophylactic rules that bind both federal and state courts has been the
subject of debate among jurists and commentators. See, e.g., Dickerson,
530 U. S., at 445–446, 457–461 (Scalia, J., joined by THOMAS, J., dissent-
ing); D. Strauss, The Ubiquity of Prophylactic Rules, 55 U. Chi. L. Rev.
190 (1988); J. Grano, Prophylactic Rules in Criminal Procedure: A Ques-
tion of Article III Legitimacy, 80 Nw. U. L. Rev. 100 (1985); H. Mona-
ghan, Foreword: Constitutional Common Law, 89 Harv. L. Rev. 1 (1975).
But that is what the Court did in Miranda, and we do not disturb that
decision in any way. Rather, we accept it on its own terms, and for the
purpose of deciding this case, we follow its rationale.
14                           VEGA v. TEKOH

                           Opinion of the Court

§1983 claim. But whatever else may be said about this ar-
gument,6 it cannot succeed unless Tekoh can persuade us
that this “law” should be expanded to include the right to
sue for damages under §1983.
   As we have noted, “[a] judicially crafted” prophylactic
rule should apply “only where its benefits outweigh its
costs,” Shatzer, 559 U. S., at 106, and here, while the bene-
fits of permitting the assertion of Miranda claims under
§1983 would be slight, the costs would be substantial.
   Miranda rests on a pragmatic judgment about what is
needed to stop the violation at trial of the Fifth Amendment
right against compelled self-incrimination. That prophy-
lactic purpose is served by the suppression at trial of state-


——————
   6 “[Section] 1983 does not provide an avenue for relief every time a state

actor violates a federal law.” Rancho Palos Verdes v. Abrams, 544 U. S.
113, 119 (2005). If a §1983 plaintiff demonstrates that the federal stat-
ute “creates an individually enforceable right in the class of beneficiaries
to which he belongs,” this gives rise to “ ‘a rebuttable presumption that
the right is enforceable under §1983,’ ” and “[t]he defendant may defeat
this presumption by demonstrating that Congress did not intend that
remedy for a newly created right.” Id., at 120 (quoting Blessing v. Free-
stone, 520 U. S. 329, 341 (1997)). In this case, the “law” that could confer
the right in question is not a statute but judicially created prophylactic
rules. It could be argued that a judicially created prophylactic rule can-
not be the basis for a §1983 suit, but we need not decide that question
because, assuming that such rules can provide the basis for a §1983
claim, we would be led back to a question that is very much like the one
discussed supra, at 7–11, namely, whether the benefits of allowing such
a claim outweigh the costs.
   The dissent, by contrast, would apparently hold that a prophylactic
rule crafted by the Judiciary to protect a constitutional right, unlike a
statute that confers a personal right, is always cognizable under §1983.
There is no sound reason to give this preferred status to such prophylac-
tic rules. The dissent contends that the Miranda rules merit this special
treatment because they are “secured by” the Constitution, see post, at 5–
6, but in fact, as we have shown, those rules differ from the right secured
by the Fifth Amendment and are instead secured for prophylactic rea-
sons by decisions of this Court.
                  Cite as: 597 U. S. ____ (2022)           15

                      Opinion of the Court

ments obtained in violation of Miranda and by the applica-
tion of that decision in other recognized contexts. Allowing
the victim of a Miranda violation to sue a police officer for
damages under §1983 would have little additional deter-
rent value, and permitting such claims would cause many
problems.
   Allowing a claim like Tekoh’s would disserve “judicial
economy,” Parklane Hosiery Co. v. Shore, 439 U. S. 322, 326
(1979), by requiring a federal judge or jury to adjudicate a
factual question (whether Tekoh was in custody when ques-
tioned) that had already been decided by a state court. This
re-adjudication would not only be wasteful; it would under-
cut the “ ‘strong judicial policy against the creation of two
conflicting resolutions’ ” based on the same set of facts.
Heck v. Humphrey, 512 U. S. 477, 484 (1994). And it could
produce “unnecessary friction” between the federal and
state court systems by requiring the federal court enter-
taining the §1983 claim to pass judgment on legal and fac-
tual issues already settled in state court. See Preiser v. Ro-
driguez, 411 U. S. 475, 490–491 (1973).
   Allowing §1983 suits based on Miranda claims could also
present many procedural issues, such as whether a federal
court considering a §1983 claim would owe any deference to
a trial court’s factual findings; whether forfeiture and plain
error rules carry over from the criminal trial; whether
harmless-error rules apply; and whether civil damages are
available in instances where the unwarned statement had
no impact on the outcome of the criminal case.
   We therefore refuse to extend Miranda in the way Tekoh
requests. Miranda, Dickerson, and the other cases in that
line provide sufficient protection for the Fifth Amendment
right against compelled self-incrimination. “The identifica-
tion of a Miranda violation and its consequences . . . ought
to be determined at trial.” Chavez v. Martinez, 538 U. S.
760, 790 (2003) (Kennedy, J., concurring in part and dis-
senting in part). And except in unusual circumstances, the
16                     VEGA v. TEKOH

                     Opinion of the Court

“exclusion of unwarned statements” should be “a complete
and sufficient remedy.” Ibid.
                       *    *     *
  Because a violation of Miranda is not itself a violation of
the Fifth Amendment, and because we see no justification
for expanding Miranda to confer a right to sue under §1983,
the judgment of the Court of Appeals is reversed, and the
case is remanded for further proceedings consistent with
this opinion.
                                            It is so ordered.
                  Cite as: 597 U. S. ____ (2022)             1

                      KAGAN, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 21–499
                          _________________


CARLOS VEGA, PETITIONER v. TERENCE B. TEKOH
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                         [June 23, 2022]

   JUSTICE KAGAN, with whom JUSTICE BREYER and
JUSTICE SOTOMAYOR join, dissenting.
   The Court’s decision in Miranda v. Arizona, 384 U. S. 436
(1966), affords well-known protections to suspects who are
interrogated by police while in custody. Those protections
derive from the Constitution: Dickerson v. United States
tells us in no uncertain terms that Miranda is a “constitu-
tional rule.” 530 U. S. 428, 444 (2000). And that rule grants
a corresponding right: If police fail to provide the Miranda
warnings to a suspect before interrogating him, then he is
generally entitled to have any resulting confession excluded
from his trial. See 384 U. S., at 478–479. From those facts,
only one conclusion can follow—that Miranda’s protections
are a “right[ ]” “secured by the Constitution” under the fed-
eral civil rights statute. Rev. Stat. §1979, 42 U. S. C. §1983.
Yet the Court today says otherwise. It holds that Miranda
is not a constitutional right enforceable through a §1983
suit. And so it prevents individuals from obtaining any re-
dress when police violate their rights under Miranda. I re-
spectfully dissent.
   Miranda responded to problems stemming from the in-
terrogation of suspects “incommunicado” and “in a police-
dominated atmosphere.” Miranda, 384 U. S., at 445. In
such an environment, Miranda said, there are “pressures”
which may “compel [a suspect] to speak where he would not
otherwise do so freely.” Id., at 467. And so Miranda found
2                       VEGA v. TEKOH

                      KAGAN, J., dissenting

a “necessity for procedures which assure that the individual
is accorded his” Fifth Amendment privilege “not to be com-
pelled to incriminate himself.” Id., at 439. Miranda set out
protocols (including the now-familiar warnings) that would
safeguard the constitutional privilege against self-incrimi-
nation. See id., at 478–479. And Miranda held that if po-
lice failed to follow those requirements (without substitut-
ing equally effective ones), the prosecution could not use at
trial a statement obtained from the interrogation. See id.,
at 479.
   The question in this case is whether Miranda’s protec-
tions are a “right[ ]” that is “secured by the Constitution”
within the meaning of §1983. If the answer is yes, then a
person may sue a state actor who deprives him of the right.
In past cases, the Court has given a broad construction to
§1983’s broad language. See, e.g., Dennis v. Higgins, 498
U. S. 439, 443 (1991). Under §1983 (as elsewhere), a
“right[ ]” is anything that creates specific “obligations bind-
ing on [a] governmental unit” that an individual may ask
the judiciary to enforce. Id., at 449; see id., at 447, and n. 7.
And the phrase “secured by the Constitution” also has a ca-
pacious meaning. It refers to any right that is “protect[ed]
or ma[de] certain” by the country’s foundational charter.
Hague v. Committee for Industrial Organization, 307 U. S.
496, 527 (1939) (opinion of Stone, J.) (internal quotation
marks omitted).
   Begin with whether Miranda is “secured by the Constitu-
tion.” We know that it is, because the Court’s decision in
Dickerson says so. Dickerson tells us again and again that
Miranda is a “constitutional rule.” 530 U. S., at 444. It is
a “constitutional decision” that sets forth “ ‘concrete consti-
tutional guidelines.’ ” Id., at 432, 435 (quoting Miranda,
384 U. S., at 442). Miranda “is constitutionally based”; or
again, it has a “constitutional basis.” 530 U. S., at 439, n. 3,
440. It is “of constitutional origin”; it has “constitutional
underpinnings.” Id., at 439, n. 3, 440, n. 5. And—one
                      Cite as: 597 U. S. ____ (2022)                     3

                          KAGAN, J., dissenting

more—Miranda sets a “constitutional minimum.” 530
U. S., at 442. Over and over, Dickerson labels Miranda a
rule stemming from the Constitution.
   Dickerson also makes plain that Miranda has all the sub-
stance of a constitutional rule—including that it cannot be
“abrogate[d]” by any “legislation.” Miranda, 384 U. S., at
491; see Dickerson, 530 U. S., at 437. In Dickerson, the
Court considered a federal statute whose obvious purpose
was to override Miranda. Dickerson held that Miranda is
a “constitutional decision” that cannot be “overruled by”
any “Act of Congress.” 530 U. S., at 432. To be sure, Con-
gress may devise “legislative solutions that differ[ ] from the
prescribed Miranda warnings,” but only if those solutions
are “ ‘at least as effective.’ ” Id., at 440 (quoting Miranda,
384 U. S., at 467). Dickerson therefore instructs (as noted
above) that Miranda sets a “constitutional minimum.” 530
U. S., at 442. No statute may provide lesser protection than
that baseline.*
   And Dickerson makes clear that the constitutional sub-
stance of Miranda does not end there. Rules arising from
“the United States Constitution” are applicable in state-
court proceedings, but non-constitutional rules are not. See
530 U. S., at 438 (explaining that the Court “do[es] not hold
a supervisory power over the courts of the several States”).
Too, constitutional rules are enforceable in federal-court
habeas proceedings, where a prisoner is entitled to claim he
“is in custody in violation of the Constitution.” 28 U. S. C.
——————
   *Other constitutional rules, like Miranda, leave room for States to ex-
periment with procedures, so long as the procedures satisfy the constitu-
tionally mandated baseline. See County of Riverside v. McLaughlin, 500
U. S. 44, 58 (1991) (States may adopt different procedures for providing
probable-cause determinations for persons arrested without a warrant,
so long as those determinations are made promptly); Smith v. Robbins,
528 U. S. 259, 276–277 (2000) (States may adopt different procedures to
ensure effective appellate review for indigent defendants’ claims, “so long
as [the State] reasonably ensures that an indigent’s appeal will be re-
solved in a way that is related to the merit of that appeal”).
4                      VEGA v. TEKOH

                     KAGAN, J., dissenting

§2254(a). Miranda checks both boxes. The Court has “con-
sistently applied Miranda’s rule to prosecutions arising in
state courts.” Dickerson, 530 U. S., at 438. And prisoners
may claim Miranda violations in federal-court habeas pro-
ceedings. See 530 U. S., at 439, n. 3; Thompson v. Keohane,
516 U. S. 99, 107, n. 5 (1995). So Dickerson is unequivocal:
Miranda is set in constitutional stone.
   Miranda’s constitutional rule gives suspects a correlative
“right[ ].” §1983. Under Miranda, a suspect typically has a
right to be tried without the prosecutor using his un-
Mirandized statement. And we know how that right oper-
ates in the real world. Suppose a defendant standing trial
was able to show the court that he gave an un-Mirandized
confession during a custodial interrogation. The court
would have no choice but to exclude it from the prosecutor’s
case. As one judge below put it: “Miranda indisputably cre-
ates individual legal rights that are judicially enforceable.
(Any prosecutor who doubts this can try to introduce an un-
Mirandized confession and then watch what happens.)”
Tekoh v. County of Los Angeles, 997 F. 3d 1260, 1263 (CA9
2021) (Miller, J., concurring in denial of rehearing en banc).
   The majority basically agrees with everything I’ve just
explained.     It concurs that, per Dickerson, Miranda
“adopted a ‘constitutional rule.’ ” Ante, at 11 (quoting Dick-
erson, 530 U. S., at 439); see ante, at 12. How could it not?
That Miranda is a constitutional rule is what Dickerson
said (and said and said). The majority also agrees that Mi-
randa “directed that statements obtained in violation of
[its] rules may not be used by the prosecution in its case-in-
chief ”—which is simply another way of saying that Mi-
randa grants suspects a right to the exclusion of those
statements from the prosecutor’s case. Ante, at 5.
   So how does the majority hold that a violation of Miranda
is not a “deprivation of [a] right[ ]” “secured by the Consti-
tution”? §1983. How does it agree with my premises, but
                 Cite as: 597 U. S. ____ (2022)            5

                     KAGAN, J., dissenting

not my conclusion? The majority’s argument is that “a vio-
lation of Miranda does not necessarily constitute a violation
of the Constitution,” because Miranda’s rules are “prophy-
lactic.” Ante, at 13. The idea is that the Fifth Amendment
prohibits the use only of statements obtained by compul-
sion, whereas Miranda excludes non-compelled statements
too. See ante, at 4–5. That is why, the majority says, the
Court has been able to recognize exceptions permitting cer-
tain uses of un-Mirandized statements at trial (when it
could not do so for compelled statements). See ante, at 7–9.
   But none of that helps the majority’s case. Let’s assume,
as the majority says, that Miranda extends beyond—in or-
der to safeguard—the Fifth Amendment’s core guarantee.
Still, Miranda is enforceable through §1983. It remains a
constitutional rule, as Dickerson held (and the majority
agrees). And it grants the defendant a legally enforceable
entitlement—in a word, a right—to have his confession ex-
cluded. So, to refer back to the language of §1983, Miranda
grants a “right[ ]” “secured by the Constitution.” Whether
that right to have evidence excluded safeguards a yet
deeper constitutional commitment makes no difference to
§1983. The majority has no response to that point—except
to repeat what our argument assumes already. See ante, at
14, n. 6 (describing Miranda as prophylactic).
   Compare the majority’s holding today to a prior decision,
in which the Court “rejected [an] attempt[ ] to limit the
types of constitutional rights that are encompassed within ”
§1983. Dennis, 498 U. S., at 445. There, the Court held
that a plaintiff could sue under §1983 for a violation of the
so-called dormant Commerce Clause, which safeguards in-
terstate commerce. To the Court, it did not matter that the
Commerce Clause might be viewed as “merely allocat[ing]
power between the Federal and State Governments” over
interstate commerce, rather than as “confer[ring] ‘rights.’ ”
Id., at 447. Nor did it matter that the dormant Commerce
Clause’s protection is only “implied” by the constitutional
6                      VEGA v. TEKOH

                     KAGAN, J., dissenting

text. Ibid., n. 7. The dormant Commerce Clause, the Court
said, still provides a “right”—in the “ordinary” sense of be-
ing “ ‘[a] legally enforceable claim of one person against an-
other.’ ” Ibid. (quoting Black’s Law Dictionary 1324 (6th ed.
1990)). That describes Miranda to a tee. And if a right im-
plied from Congress’s constitutional authority over inter-
state commerce is enforceable under §1983, how could it be
that Miranda—which the Court has found necessary to
safeguard the personal protections of the Fifth Amend-
ment—is not also enforceable? The majority again has no
answer.
                         *     *    *
  Today, the Court strips individuals of the ability to seek
a remedy for violations of the right recognized in Miranda.
The majority observes that defendants may still seek “the
suppression at trial of statements obtained” in violation of
Miranda’s procedures. Ante, at 14–15. But sometimes,
such a statement will not be suppressed. And sometimes,
as a result, a defendant will be wrongly convicted and spend
years in prison. He may succeed, on appeal or in habeas, in
getting the conviction reversed. But then, what remedy
does he have for all the harm he has suffered? The point of
§1983 is to provide such redress—because a remedy “is a
vital component of any scheme for vindicating cherished
constitutional guarantees.” Gomez v. Toledo, 446 U. S. 635,
639 (1980). The majority here, as elsewhere, injures the
right by denying the remedy. See, e.g., Egbert v. Boule, 596
U. S. ___ (2022). I respectfully dissent.

```

---
