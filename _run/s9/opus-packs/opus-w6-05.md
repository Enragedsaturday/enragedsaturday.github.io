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

## GROUP: _overhaul2/lake/cases/Kirby v. Illinois.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Kirby v. Illinois"
type: case
citation: "406 U.S. 682 (1972)"
parallel_cite: "92 S. Ct. 1877; 32 L. Ed. 2d 411"
neutral_cite: 1972 U.S. LEXIS 49
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-06-07
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-06-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kirby v. Illinois
  varies_by_point: false
  scope_note: "Plurality opinion; its attachment rule was subsequently adopted by a majority (e.g., Moore v. Illinois) and reaffirmed in Rothgery v. Gillespie County (2008)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108554/kirby-v-illinois/"
  cluster_id: 108554
  opinion_id: 108554
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Anchor"
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Wade]]", "[[Gilbert v. California]]", "[[Massiah v. United States]]", "[[Rothgery v. Gillespie County]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "attachment", "eyewitness-identification", "showup"]
holding: "The Sixth Amendment right to counsel attaches only at or after the initiation of adversary judicial criminal proceedings (formal charge,…"
lake:
  record_id: Kirby v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Kirby v. Illinois

*406 U.S. 682 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Kirby and a companion were arrested on an unrelated matter, the robbery victim was brought to the police station and identified them in a one-on-one station-house showup. This identification occurred before Kirby had been indicted or otherwise formally charged with the robbery, and no counsel was present. The victim later repeated the identification at trial.

## Issue
Whether the Sixth Amendment right to counsel applies to a corporeal identification conducted before the accused has been indicted or formally charged — i.e., before the initiation of adversary judicial criminal proceedings.

## Rule
The right to counsel does not reach a pre-charge identification. As the plurality explained, all of the Court's right-to-counsel decisions "have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment." — 406 U.S. at 689 (plurality opinion). ^pin-689

It is the initiation of such proceedings that marks the point at which the accused faces the prosecutorial forces of the State and the right to counsel attaches.

## Application
Kirby's station-house showup took place after his arrest but before any indictment, information, preliminary hearing, or arraignment on the robbery — that is, before adversary judicial criminal proceedings had begun against him. Because the right to counsel had not yet attached at that point, the *Wade–Gilbert* rule requiring counsel at a post-indictment lineup did not apply, and the victim's identification was not subject to exclusion on that ground.

## Conclusion
Affirmed: there is no Sixth Amendment right to counsel at an identification conducted before the initiation of adversary judicial criminal proceedings.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Although announced in a [[Common Legal Terms#plurality-opinion|plurality opinion]], *Kirby*'s attachment rule was adopted by a majority of the Court (e.g., *[[Moore v. Illinois]]*) and **reaffirmed in [[Rothgery v. Gillespie County]]** (2008). It cabins the right-to-counsel-at-lineups rule of [[United States v. Wade]] and [[Gilbert v. California]] to **post-attachment** confrontations.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Anchor*
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *Kirby v. Illinois*, 406 U.S. 682 (1972) — https://www.courtlistener.com/opinion/108554/kirby-v-illinois/ — pinpoint: 689 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b09cb3f2445aa89a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kirby v. Illinois"}, "payload": {"all": [{"cite": "406 U.S. 682", "page": "682", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "406"}, {"cite": "92 S. Ct. 1877", "page": "1877", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "32 L. Ed. 2d 411", "page": "411", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "32"}, {"cite": "1972 U.S. LEXIS 49", "page": "49", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "406 U.S. 682", "official": {"cite": "406 U.S. 682", "page": "682", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "406"}, "official_selection_present": true, "record_id": "Kirby v. Illinois"}}
{"assertion_id": "18e35ab229bad558", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-689", "record_id": "Kirby v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-689", "pinpoint_status": "slip-only", "quote": "--- # Kirby v. Illinois *406 U.S. 682 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Kirby and a companion were arrested on an unrelated matter, the robbery victim was brought to the police station and identified them in a one-on-one station-house showup. This identification occurred before Kirby had been indicted or otherwise formally charged with the robbery, and no counsel was present. The victim later repeated the identification at trial. ## Issue Whether the Sixth Amendment right to counsel applies to a corporeal identification conducted before the accused has been indicted or formally charged — i.e., before the initiation of adversary judicial criminal proceedings. ## Rule The right to counsel does not reach a pre-charge identification. As the plurality explained, all of the Court's right-to-counsel decisions", "quote_fidelity": "mismatch", "record_id": "Kirby v. Illinois", "star_marker": null}}
{"assertion_id": "4a81341f89eb0036", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kirby v. Illinois"}, "payload": {"as_of_content": "1972-06-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kirby v. Illinois", "scope_note": "Plurality opinion; its attachment rule was subsequently adopted by a majority (e.g., Moore v. Illinois) and reaffirmed in Rothgery v. Gillespie County (2008).", "varies_by_point": false}}
```

### lake record — Kirby v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kirby v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kirby v. Illinois",
    "case_name_short": "Kirby",
    "case_name_full": "Kirby v. Illinois",
    "input_case_name": "Kirby v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-06-07",
    "year": 1972,
    "docket": null,
    "cluster_id": 108554,
    "lead_opinion_id": 108554,
    "sibling_ids": [
      108554,
      9424906,
      9424907,
      9424908,
      9424909,
      9424910
    ],
    "absolute_url": "/opinion/108554/kirby-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8987094,
        "score": 20,
        "case_name": "Kirby v. Illinois"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "406 U.S. 682",
      "volume": "406",
      "reporter": "U.S.",
      "page": "682",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 1877",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 411",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 49",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "406 U.S. 682",
        "volume": "406",
        "reporter": "U.S.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 1877",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "1877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 L. Ed. 2d 411",
        "volume": "32",
        "reporter": "L. Ed. 2d",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 49",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "406 U.S. 682",
    "official_selection": {
      "court_class": "scotus",
      "selected": "406 U.S. 682",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-689",
      "page": null,
      "quote": "--- # Kirby v. Illinois *406 U.S. 682 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Kirby and a companion were arrested on an unrelated matter, the robbery victim was brought to the police station and identified them in a one-on-one station-house showup. This identification occurred before Kirby had been indicted or otherwise formally charged with the robbery, and no counsel was present. The victim later repeated the identification at trial. ## Issue Whether the Sixth Amendment right to counsel applies to a corporeal identification conducted before the accused has been indicted or formally charged \u2014 i.e., before the initiation of adversary judicial criminal proceedings. ## Rule The right to counsel does not reach a pre-charge identification. As the plurality explained, all of the Court's right-to-counsel decisions",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-06-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kirby v. Illinois",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; its attachment rule was subsequently adopted by a majority (e.g., Moore v. Illinois) and reaffirmed in Rothgery v. Gillespie County (2008).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Guillermo Hernandez Ruiz v. State of Iowa",
          "cluster_id": 4501180,
          "cite": [
            "912 N.W.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Neary-French",
          "cluster_id": 4247088,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McLean",
          "cluster_id": 6078787,
          "cite": [
            "109 A.D.3d 670",
            "970 N.Y.S.2d 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McLean",
          "cluster_id": 6078786,
          "cite": [
            "109 A.D.3d 670",
            "970 N.Y.S.2d 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basu",
          "cluster_id": 2662288,
          "cite": [
            "881 F. Supp. 2d 1",
            "2012 WL 2244875",
            "2012 U.S. Dist. LEXIS 84114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dario Ramiro Acevedo v. State",
          "cluster_id": 3128772,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Moore, 07ca093 (11-26-2008)",
          "cluster_id": 3983329,
          "cite": [
            "2008 Ohio 6238"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane1_negative"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doggett v. United States",
          "cluster_id": 112780,
          "cite": [
            "120 L. Ed. 2d 520",
            "112 S. Ct. 2686",
            "505 U.S. 647",
            "1992 U.S. LEXIS 4362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. State",
          "cluster_id": 2413967,
          "cite": [
            "928 S.W.2d 482",
            "1996 Tex. Crim. App. LEXIS 19",
            "1996 WL 71513"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Villanueva",
          "cluster_id": 4247666,
          "cite": [
            "2016 COA 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kleindienst v. Mandel",
          "cluster_id": 108612,
          "cite": [
            "33 L. Ed. 2d 683",
            "92 S. Ct. 2576",
            "408 U.S. 753",
            "1972 U.S. LEXIS 22"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Satterwhite v. Texas",
          "cluster_id": 112080,
          "cite": [
            "100 L. Ed. 2d 284",
            "108 S. Ct. 1792",
            "486 U.S. 249",
            "1988 U.S. LEXIS 2474",
            "56 U.S.L.W. 4470"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
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
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. State",
          "cluster_id": 1683166,
          "cite": [
            "495 S.W.2d 949",
            "1973 Tex. Crim. App. LEXIS 2642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie Sevier v. Kenneth Turner",
          "cluster_id": 440363,
          "cite": [
            "742 F.2d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bing",
          "cluster_id": 5690131,
          "cite": [
            "76 N.Y.2d 331",
            "558 N.E.2d 1011",
            "559 N.Y.S.2d 474",
            "1990 N.Y. LEXIS 1488"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mandujano",
          "cluster_id": 109442,
          "cite": [
            "48 L. Ed. 2d 212",
            "96 S. Ct. 1768",
            "425 U.S. 564",
            "1976 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirby v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108554 OR 9424906 OR 9424907 OR 9424908 OR 9424909 OR 9424910) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU5NDg4MDAwMDAwJnM9Mjg5MzMyOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108554+OR+9424906+OR+9424907+OR+9424908+OR+9424909+OR+9424910%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(108554 OR 9424906 OR 9424907 OR 9424908 OR 9424909 OR 9424910)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMjAmcz03NjI2MjgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108554+OR+9424906+OR+9424907+OR+9424908+OR+9424909+OR+9424910%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108554 OR 9424906 OR 9424907 OR 9424908 OR 9424909 OR 9424910)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108554 OR 9424906 OR 9424907 OR 9424908 OR 9424909 OR 9424910)",
    "indexed_citing_opinions": 2037,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108554,
        "count": 1884,
        "count_source": "search"
      },
      {
        "opinion_id": 9424906,
        "count": 208,
        "count_source": "search"
      },
      {
        "opinion_id": 9424907,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424908,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424909,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424910,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3001,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kirby-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczODA1ODcmcz0xMDI3ODc1OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108554+OR+9424906+OR+9424907+OR+9424908+OR+9424909+OR+9424910%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108554,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 108420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 281459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 281672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 284146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 285891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 290198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 290711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 290752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 291123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 291198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 295963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 301056,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1147816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1159535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1395727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1434555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1559532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1605190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1605345,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1714361,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1753794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1778052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1935989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 1996605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2173439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2173626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2178575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2212706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2237741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2267026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2457586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 2619489,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108554,
        "cited_id": 3756832,
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
    "date_created": "2026-07-05T10:05:39Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:11:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kirby v. Illinois

```
<div>
<center><b><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U.S. 682</a></span> (1972)</b></center>
<center><h1>KIRBY<br>
v.<br>
ILLINOIS.</h1></center>
<center>No. 70-5061.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 11, 1971.</center>
<center>Reargued March 20-21, 1972.</center>
<center>Decided June 7, 1972.</center>
CERTIORARI TO THE APPELLATE COURT OF ILLINOIS, FIRST DISTRICT.
<p><span class="star-pagination">*683</span> <i>Jerold S. Solovy</i> argued the cause for petitioner on the reargument and <i>Michael P. Seng</i> argued the cause on the original argument. <i>Messrs. Solovy</i> and <i>Seng</i> were on the briefs for petitioner.</p>
<p><i>James B. Zagel,</i> Assistant Attorney General of Illinois, reargued the cause for respondent. With him on the brief were <i>William J. Scott,</i> Attorney General, <i>Joel M. Flaum,</i> First Assistant Attorney General, and <i>E. James Gildea,</i> Assistant Attorney General.</p>
<p><i>Ronald M. George,</i> Deputy Attorney General, argued the cause on the reargument for the State of California as <i>amicus curiae</i> urging affirmance. With him on the brief were <i>Evelle J. Younger,</i> Attorney General, and <i>William E. James,</i> Assistant Attorney General.</p>
<p>MR. JUSTICE STEWART announced the judgment of the Court and an opinion in which THE CHIEF JUSTICE, MR. JUSTICE BLACKMUN, and MR. JUSTICE REHNQUIST join.</p>
<p>In <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>, this Court held "that a post-indictment pretrial lineup at which the accused is exhibited to identifying witnesses is a critical stage of the criminal prosecution; that police conduct of such a lineup without notice to and in the absence of his counsel denies the accused his Sixth [and Fourteenth] Amendment right to counsel and calls in question the admissibility at trial of the in-court identifications of the accused by witnesses who attended the lineup." <i>Gilbert</i> v. <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California"><i>California, supra,</i> at 272</a></span>. Those cases further held that no "in-court identifications" are admissible in evidence if their "source" is a lineup conducted in violation of this constitutional standard. "Only a <i>per se</i> exclusionary rule as to such testimony can be an effective sanction," the Court said, "to assure that law <span class="star-pagination">*684</span> enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 273</a></span>. In the present case we are asked to extend the <i>Wade-Gilbert per se</i> exclusionary rule to identification testimony based upon a police station showup that took place <i>before</i> the defendant had been indicted or otherwise formally charged with any criminal offense.</p>
<p>On February 21, 1968, a man named Willie Shard reported to the Chicago police that the previous day two men had robbed him on a Chicago street of a wallet containing, among other things, traveler's checks and a Social Security card. On February 22, two police officers stopped the petitioner and a companion, Ralph Bean, on West Madison Street in Chicago.<sup>[1]</sup> When asked for identification, the petitioner produced a wallet that contained three traveler's checks and a Social Security card, all bearing the name of Willie Shard. Papers with Shard's name on them were also found in Bean's possession. When asked to explain his possession of Shard's property, the petitioner first said that the traveler's checks were "play money," and then told the officers that he had won them in a crap game. The officers then arrested the petitioner and Bean and took them to a police station.</p>
<p>Only after arriving at the police station, and checking the records there, did the arresting officers learn of the Shard robbery. A police car was then dispatched to Shard's place of employment, where it picked up Shard and brought him to the police station. Immediately upon entering the room in the police station where the petitioner and Bean were seated at a table, Shard positively identified them as the men who had <span class="star-pagination">*685</span> robbed him two days earlier. No lawyer was present in the room, and neither the petitioner nor Bean had asked for legal assistance, or been advised of any right to the presence of counsel.</p>
<p>More than six weeks later, the petitioner and Bean were indicted for the robbery of Willie Shard. Upon arraignment, counsel was appointed to represent them, and they pleaded not guilty. A pretrial motion to suppress Shard's identification testimony was denied, and at the trial Shard testified as a witness for the prosecution. In his testimony he described his identification of the two men at the police station on February 22,<sup>[2]</sup> and identified them again in the courtroom as the men <span class="star-pagination">*686</span> who had robbed him on February 20.<sup>[3]</sup> He was cross-examined at length regarding the circumstances of his identification of the two defendants. Cf. <i>Pointer</i> v. <i>Texas,</i> <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. The jury found both defendants guilty, and the petitioner's conviction was affirmed on appeal. <i>People</i> v. <i>Kirby</i> <span class="citation" data-id="2173439"><a href="/opinion/2173439/people-v-kirby/" aria-description="Citation for case: People v. Kirby">121 Ill. App. 2d 323</a></span>, <span class="citation" data-id="2173439"><a href="/opinion/2173439/people-v-kirby/" aria-description="Citation for case: People v. Kirby">257 N. E. 2d 589</a></span>.<sup>[4]</sup> The Illinois appellate court held that the admission of Shard's testimony was not error, relying upon an earlier decision of the Illinois Supreme Court, <i>People</i> v. <i>Palmer,</i> <span class="citation" data-id="1996605"><a href="/opinion/1996605/the-people-v-palmer/" aria-description="Citation for case: The People v. Palmer">41 Ill. 2d 571</a></span>, <span class="citation" data-id="1996605"><a href="/opinion/1996605/the-people-v-palmer/" aria-description="Citation for case: The People v. Palmer">244 N. E. 2d 173</a></span>, holding that the <i>Wade-Gilbert per se</i> exclusionary rule is not applicable to pre-indictment confrontations. <span class="star-pagination">*687</span> We granted certiorari, limited to this question. <span class="citation multiple-matches"><a href="/c/U.%20S./402/995/">402 U. S. 995</a></span>.<sup>[5]</sup></p>
<p></p>
<h2>I</h2>
<p>We note at the outset that the constitutional privilege against compulsory self-incrimination is in no way implicated here. The Court emphatically rejected the claimed applicability of that constitutional guarantee in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> itself:</p>
<blockquote>"Neither the lineup itself nor anything shown by this record that Wade was required to do in the lineup violated his privilege against self-incrimination. We have only recently reaffirmed that the privilege `protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature . . . .' <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761</a></span>. . . ." 388 U. S., at 221.</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"We have no doubt that compelling the accused merely to exhibit his person for observation by a prosecution witness prior to trial involves no compulsion of the accused to give evidence having testimonial significance. It is compulsion of the accused <span class="star-pagination">*688</span> to exhibit his physical characteristics, not compulsion to disclose any knowledge he might have. . . ." <i>Id.,</i> at 222.</blockquote>
<p>It follows that the doctrine of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, has no applicability whatever to the issue before us; for the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision was based exclusively upon the Fifth and Fourteenth Amendment privilege against compulsory self-incrimination, upon the theory that custodial <i>interrogation</i> is inherently coercive.</p>
<p>The <i>Wade-Gilbert</i> exclusionary rule, by contrast, stems from a quite different constitutional guaranteethe guarantee of the right to counsel contained in the Sixth and Fourteenth Amendments. Unless all semblance of principled constitutional adjudication is to be abandoned, therefore, it is to the decisions construing that guarantee that we must look in determining the present controversy.</p>
<p>In a line of constitutional cases in this Court stemming back to the Court's landmark opinion in <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, it has been firmly established that a person's Sixth and Fourteenth Amendment right to counsel attaches only at or after the time that adversary judicial proceedings have been initiated against him. See <i>Powell</i> v. <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama, supra</a></span></i><i>; </i><i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>; <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>; <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>.</p>
<p>This is not to say that a defendant in a criminal case has a constitutional right to counsel only at the trial itself. The <i><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Powell</a></span></i> case makes clear that the right attaches at the time of arraignment,<sup>[6]</sup> and the Court <span class="star-pagination">*689</span> has recently held that it exists also at the time of a preliminary hearing. <i>Coleman</i> v. <i>Alabama, supra</i><i>.</i> But the point is that, while members of the Court have differed as to existence of the right to counsel in the contexts of some of the above cases, <i>all</i> of those cases have involved points of time at or after the initiation of adversary judicial criminal proceedingswhether by way of formal charge, preliminary hearing, indictment, information, or arraignment.</p>
<p>The only seeming deviation from this long line of constitutional decisions was <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>. But <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> is not apposite here for two distinct reasons. First, the Court in retrospect perceived that the "prime purpose" of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was not to vindicate the constitutional right to counsel as such, but, like <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> "to guarantee full effectuation of the privilege against self-incrimination . . . ." <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#729" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 729</a></span>. Secondly, and perhaps even more important for purely practical purposes, the Court has limited the holding of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> to its own facts, <i>Johnson</i> v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#733" aria-description="Citation for case: Johnson v. New Jersey"><i>New Jersey, supra,</i> at 733-734</a></span>, and those facts are not remotely akin to the facts of the case before us.</p>
<p>The initiation of judicial criminal proceedings is far from a mere formalism. It is the starting point of our whole system of adversary criminal justice. For it is only then that the government has committed itself to prosecute, and only then that the adverse positions of government and defendant have solidified. It is then that a defendant finds himself faced with the prosecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law. <span class="star-pagination">*690</span> It is this point, therefore, that marks the commencement of the "criminal prosecutions" to which alone the explicit guarantees of the Sixth Amendment are applicable.<sup>[7]</sup> See <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#66" aria-description="Citation for case: Powell v. Alabama">287 U. S., at 66-71</a></span>; <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#324" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 324</a></span> (DOUGLAS, J., concurring).</p>
<p>In this case we are asked to import into a routine police investigation an absolute constitutional guarantee historically and rationally applicable only after the onset of formal prosecutorial proceedings. We decline to do so. Less than a year after <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> were decided, the Court explained the rule of those decisions as follows: "The rationale of those cases was that an accused is entitled to counsel at any `critical stage of the <i>prosecution,</i>' and that a post-indictment lineup is such a `critical stage.' " (Emphasis supplied.) <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#382" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 382-383</a></span>. We decline to depart from that rationale today by imposing a <i>per se</i> exclusionary rule upon testimony concerning an identification that took place long before the commencement of any prosecution whatever.</p>
<p></p>
<h2>II</h2>
<p>What has been said is not to suggest that there may not be occasions during the course of a criminal investigation when the police do abuse identification procedures. Such abuses are not beyond the reach of the Constitution. As the Court pointed out in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> itself, it is always necessary to "scrutinize <i>any</i> pretrial confrontation <span class="star-pagination">*691</span>. . . ." 388 U. S., at 227. The Due Process Clause of the Fifth and Fourteenth Amendments forbids a lineup that is unnecessarily suggestive and conducive to irreparable mistaken identification. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span>; <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span>.<sup>[8]</sup> When a person has not been formally charged with a criminal offense, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> strikes the appropriate constitutional balance between the right of a suspect to be protected from prejudicial procedures and the interest of society in the prompt and purposeful investigation of an unsolved crime.</p>
<p><i>The judgment is affirmed.</i></p>
<p>MR. CHIEF JUSTICE BURGER, concurring.</p>
<p>I agree that the right to counsel attaches as soon as criminal charges are formally made against an accused and he becomes the subject of a "criminal prosecution." Therefore, I join in the plurality opinion and in the judgment. Cf. <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#21" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 21</a></span> (dissenting opinion).</p>
<p>MR. JUSTICE POWELL, concurring in the result.</p>
<p>As I would not extend the <i>Wade-Gilbert per se</i> exclusionary rule, I concur in the result reached by the Court.</p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>After petitioner and Ralph Bean were arrested, police officers brought Willie Shard, the robbery victim, to a room in a police station where petitioner and Bean were seated at a table with two other police officers. Shard testified at trial that the officers who brought him to the <span class="star-pagination">*692</span> room asked him if petitioner and Bean were the robbers and that he indicated they were. The prosecutor asked him, "And you positively identified them at the police station, is that correct?" Shard answered, "Yes." Consequently, the question in this case is whether, under <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), it was constitutional error to admit Shard's testimony that he identified petitioner at the pretrial station-house showup when that showup was conducted by the police without advising petitioner that he might have counsel present. <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> held, in the context of a post-indictment lineup, that "[o]nly a <i>per se</i> exclusionary rule as to such testimony can be an effective sanction to assure that law enforcement authorities will respect the accused's constitutional right to the presence of his counsel at the critical lineup." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 273</a></span>. I would apply <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> and the principles of its companion case, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and reverse.<sup>[1]</sup></p>
<p>In <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> after concluding that the lineup conducted in that case did not violate the accused's right against self-incrimination, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#221" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 221-223</a></span>,<sup>[2]</sup> the Court addressed <span class="star-pagination">*693</span> the argument "that the assistance of counsel at the lineup was indispensable to protect Wade's most basic right as a criminal defendanthis right to a fair trial at which the witnesses against him might be meaningfully cross-examined," <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#223" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 223-224</a></span>. The Court began by emphasizing that the Sixth Amendment guarantee "encompasses counsel's assistance whenever necessary to assure a meaningful `defence.' " <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#225" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 225</a></span>. After reviewing <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932); <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961); and <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the Court, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#225" aria-description="Citation for case: United States v. Wade">388 U. S., at 225</a></span>, focused upon two cases that involved the right against self-incrimination:</p>
<blockquote>"In <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, we drew upon the rationale of <i><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">Hamilton</a></span></i> and <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> in holding that the right to counsel was guaranteed at the point where the accused, prior to arraignment, was subjected to secret interrogation despite repeated requests to see his lawyer. We again noted the necessity of counsel's presence if the accused was to have a fair opportunity to present a defense at the trial itself . . . ." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#225" aria-description="Citation for case: United States v. Wade">388 U. S., at 225-226</a></span>.<sup>[3]</sup></blockquote>
<p></p>
<h2>.....</h2>
<blockquote>
<span class="star-pagination">*694</span> "[I]n <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the rules established for custodial interrogation included the right to the presence of counsel. The result was rested on our finding that this and the other rules were necessary to safeguard the privilege against self-incrimination from being jeopardized by such interrogation." <i>Id.,</i> at 226.</blockquote>
<p>The Court then pointed out that "nothing decided or said in the opinions in [<span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois"><i>Escobedo</i></a></span> and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>] links the right to counsel only to protection of Fifth Amendment rights." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> To the contrary, the Court said, those decisions simply reflected the constitutional</p>
<blockquote>"principle that in addition to counsel's presence at trial, the accused is guaranteed that he need not stand alone against the State at any stage of the prosecution, formal or informal, in court or out, where counsel's absence might derogate from the accused's right to a fair trial. The security of that right is as much the aim of the right to counsel as it is of the other guarantees of the Sixth Amendment. . . ." <i>Id.,</i> at 226-227.</blockquote>
<p>This analysis led to the Court's formulation of the controlling principle for pretrial confrontations:</p>
<blockquote>"In sum, the principle of <i>Powell</i> v. <i>Alabama</i> and succeeding cases requires that we scrutinize <i>any</i> pretrial confrontation of the accused to determine whether the presence of his counsel is necessary to preserve the defendant's basic right to a fair trial as affected by his right meaningfully to cross-examine the witnesses against him and to have effective assistance of counsel at the trial itself. It calls upon us to analyze whether potential substantial prejudice to defendant's rights inheres in the particular confrontation and the ability of counsel to help avoid that prejudice." <i>Id.,</i> at 227 (emphasis in original).</blockquote>
<p><span class="star-pagination">*695</span> It was that constitutional principle that the Court applied in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> to pretrial confrontations for identification purposes. The Court first met the Government's contention that a confrontation for identification is "a mere preparatory step in the gathering of the prosecution's evidence," much like the scientific examination of fingerprints and blood samples. The Court responded that in the latter instances "the accused has the opportunity for a meaningful confrontation of the Government's case at trial through the ordinary processes of cross-examination of the Government's expert witnesses and the presentation of the evidence of his own experts." The accused thus has no right to have counsel present at such examinations: "they are not critical stages since there is minimal risk that his counsel's absence at such stages might derogate from his right to a fair trial." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#227" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 227-228</a></span>.</p>
<p>In contrast, the Court said, "the confrontation compelled by the State between the accused and the victim or witnesses to a crime to elicit identification evidence is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 228</a></span>. Most importantly, "the accused's inability effectively to reconstruct at trial any unfairness that occurred at the lineup may deprive him of his only opportunity meaningfully to attack the credibility of the witness' courtroom identification." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#231" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 231-232</a></span>. The Court's analysis of pretrial confrontations for identification purposes produced the following conclusion:</p>
<blockquote>"Insofar as the accused's conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination <span class="star-pagination">*696</span> which is an essential safeguard to his right to confront the witnesses against him. <i>Pointer</i> v. <i>Texas,</i> <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. And even though cross-examination is a precious safeguard to a fair trial, it cannot be viewed as an absolute assurance of accuracy and reliability. Thus in the present context, where so many variables and pitfalls exist, the first line of defense must be the prevention of unfairness and the lessening of the hazards of eye-witness identification at the lineup itself. The trial which might determine the accused's fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness`that's the man.' " <i>Id.,</i> at 235-236.</blockquote>
<p>The Court then applied that conclusion to the specific facts of the case. "Since it appears that there is grave potential for prejudice, intentional or not, in the pretrial lineup, which may not be capable of reconstruction at trial, and since presence of counsel itself can often avert prejudice and assure a meaningful confrontation at trial, there can be little doubt that for Wade the post-indictment lineup was a critical stage of the prosecution at which he was `as much entitled to such aid [of counsel] . . . as at the trial itself.' " <i>Id.,</i> at 236-237.</p>
<p>While it should go without saying, it appears necessary, in view of the plurality opinion today, to re-emphasize that <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> did not require the presence of counsel at pretrial confrontations for identification purposes simply on the basis of an abstract consideration of the words "criminal prosecutions" in the Sixth Amendment. Counsel is required at those confrontations because "the <span class="star-pagination">*697</span> dangers inherent in eyewitness identification and the suggestibility inherent in the context of the pretrial identification," <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 235</a></span>,<sup>[4]</sup> mean that protection must be afforded to the "most basic right [of] a criminal defendant his right to a fair trial at which the witnesses against him might be meaningfully cross-examined," <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 224</a></span>. Indeed, the Court expressly stated that "[l]egislative or other regulations, such as those of local police departments, which eliminate the risks of abuse and unintentional suggestion at lineup proceedings and the impediments to meaningful confrontation at trial may also remove the basis for regarding the stage as `critical.' " <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#239" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 239</a></span>; see <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">id.,</a></span></i> at 239 n. 30; <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California">388 U. S., at 273</a></span>. Hence, "the initiation of adversary judicial criminal proceedings," <i>ante,</i> at 689, is completely irrelevant to whether counsel is necessary at a pretrial confrontation for identification in order to safeguard the accused's constitutional rights to confrontation and the effective assistance of counsel at his trial.</p>
<p>In view of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> it is plain, and the plurality today does not attempt to dispute it, that there inhere in a confrontation <span class="star-pagination">*698</span> for identification conducted after arrest<sup>[5]</sup> the identical hazards to a fair trial that inhere in such a confrontation conducted "after the onset of formal prosecutorial proceedings." <i>Id.,</i> at 690. The plurality apparently considers an arrest, which for present purposes we must assume to be based upon probable cause, to be nothing more than part of "a routine police investigation," <i>ibid.,</i> and thus not "the starting point of our whole system of adversary criminal justice," <i>id.,</i> at 689.<sup>[6]</sup> An arrest, according to the plurality, does not face the accused "with the prosecutorial forces of organized society," nor immerse him "in the intricacies of substantive and procedural criminal law." Those consequences ensue, says the plurality, only with "[t]he initiation of judicial criminal proceedings," "[f]or it is only then that the government has committed itself to prosecute, and only then that the adverse positions of government and defendant have solidified." <i>Ibid.</i><sup>[7]</sup> If these propositions do not amount to <span class="star-pagination">*699</span> "mere formalism," <i>ibid.,</i> it is difficult to know how to characterize them.<sup>[8]</sup> An arrest evidences the belief of the police that the perpetrator of a crime has been caught. A post-arrest confrontation for identification is not "a mere preparatory step in the gathering of the prosecution's evidence." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#227" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 227</a></span>. A primary, and frequently sole, purpose of the confrontation for identification at that stage is to accumulate proof to buttress the conclusion of the police that they have the offender in hand. The plurality offers no reason, and I can think of none, for concluding that a post-arrest confrontation for identification, unlike a post-charge confrontation, is not among those "critical confrontations of the accused by the prosecution at pretrial proceedings where the results might well settle the accused's fate and reduce the trial itself to a mere formality." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 224</a></span>.</p>
<p>The highly suggestive form of confrontation employed in this case underscores the point. This showup was particularly fraught with the peril of mistaken <span class="star-pagination">*700</span> identification. In the setting of a police station squad room where all present except petitioner and Bean were police officers, the danger was quite real that Shard's understandable resentment might lead him too readily to agree with the police that the pair under arrest, and the only persons exhibited to him, were indeed the robbers. "It is hard to imagine a situation more clearly conveying the suggestion to the witness that the one presented is believed guilty by the police." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#234" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 234</a></span>. The State had no case without Shard's identification testimony,<sup>[9]</sup> and safeguards against that consequence were therefore of critical importance. Shard's testimony itself demonstrates the necessity for such safeguards. On direct examination, Shard identified petitioner and Bean not as the alleged robbers on trial in the courtroom, but as the pair he saw at the police station. His testimony thus lends strong support to the observation, quoted by the Court in <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade">388 U. S., at 229</a></span>, that "[i]t is a matter of common experience that, once a witness has picked out the accused at the line-up, he is not likely to go back on his word later on, so that in practice the issue of identity may (in the absence of other relevant evidence) for all practical purposes be determined there and then, before the trial." Williams &amp; Hammelmann, Identification Parades, Part I, [1963] Crim. L. Rev. 479, 482.</p>
<p>The plurality today "decline[s] to depart from [the] rationale" of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert. Ante,</i> at 690. The plurality discovers that "rationale" not by consulting those decisions themselves, which would seem to be the appropriate course, but by reading one sentence in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#382" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 382-383</a></span> (1968), where no right-to-counsel claim was either asserted or considered. The "rationale" the plurality discovers is, apparently, <span class="star-pagination">*701</span> that a post-indictment confrontation for identification is part of the prosecution. The plurality might have discovered a different "rationale" by reading one sentence in <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S. 440, 442</a></span> (1969), a case decided after <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> where the Court explained that in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> "this Court held that because of the possibility of unfairness to the accused in the way a lineup is conducted, a lineup is a `critical stage' in the prosecution, at which the accused must be given the opportunity to be represented by counsel." In <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span>,</i> moreover, although the Court mentioned that the lineups took place after the accused's arrest, it did not say whether they were also after the information was filed against him.<sup>[10]</sup> Instead, the Court simply pointed out that under <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> were "applicable only to lineups conducted after those cases were decided." <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S., at 442</a></span>. Similarly, in <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), another case involving a pre-<span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade"><i>Wade</i></a></span> lineup, no member of the Court saw any significance in whether the accused had been formally charged with a crime before the lineup was held.<sup>[11]</sup></p>
<p><span class="star-pagination">*702</span> The plurality might also have discovered a different "rationale" for <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> had it examined <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>,</i> decided the same day. In <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> the confrontation for identification took place one day after the accused's arrest. Although the accused was first brought to an arraignment, it "was postponed until [he] could retain counsel." 388 U. S., at 295. Hence, in the plurality's terms today, the confrontation was held "before the commencement of any prosecution." <i>Ante,</i> at 690.<sup>[12]</sup> Yet in that circumstance the Court in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> <span class="star-pagination">*703</span> stated that the accused raised "the same alleged constitutional errors in the admission of allegedly tainted identification evidence that were before us" in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>.</i> The Court therefore found that the case "provide[d] a vehicle for deciding the extent to which the rules announced in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i>requiring the exclusion of identification evidence which is tainted by exhibiting the accused to identifying witnesses before trial in the absence of his counselare to be applied retroactively." 388 U. S., at 294. Indeed, the Court's explicit holding was "that <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> affect only those cases and all future cases which involve confrontations for identification purposes conducted in the absence of counsel after this date. The rulings of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> are therefore inapplicable in the present case." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#296" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 296</a></span>. Hence, the accused in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> did not receive the benefit of the new exclusionary rules because they were not applied retroactively; he was not denied their benefit because his confrontation took place before he had "been formally charged with a criminal offense." <i>Ante,</i> at 691. Moreover, in the course of its retroactivity discussion, 388 U. S., at 296-301, the Court repeated the phrase "pretrial confrontations for identification" or its equivalent no less than 10 times. Not once did the Court so much as hint that <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> applied only to confrontations after the accused "had been indicted or otherwise formally charged with [a] criminal offense." <i>Ante,</i> at 684. In fact, at one point the Court summarized <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> as holding "that the confrontation [for identification] is a `critical stage,' and that counsel <span class="star-pagination">*704</span> is required at <i>all</i> confrontations." 388 U. S., at 298 (emphasis added).</p>
<p><i>Wade</i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>,</i> of course, happened to involve post-indictment confrontations. Yet even a cursory perusal of the opinions in those cases reveals that nothing at all turned upon that particular circumstance.<sup>[13]</sup> In short, it is fair to conclude that rather than "declin[ing] to depart from [the] rationale" of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert, ante,</i> at 690, the plurality today, albeit purporting to be engaged in "principled constitutional adjudication," <i>id.,</i> at 688, refuses even to recognize that "rationale." For my part, I do not agree that we "extend" <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert, id.,</i> at 684, by holding that the principles of those cases apply to confrontations for identification conducted after arrest.<sup>[14]</sup> Because Shard testified at trial <span class="star-pagination">*705</span> about his identification of petitioner at the police station showup, the exclusionary rule of <i>Gilbert,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California">388 U. S., at 272-274</a></span>, requires reversal.</p>
<p>MR. JUSTICE WHITE, dissenting.</p>
<p><i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), govern this case and compel reversal of the judgment below.</p>
<h2>NOTES</h2>
<p>[1]  The officers stopped the petitioner and his companion because they thought the petitioner was a man named Hampton, who was "wanted" in connection with an unrelated criminal offense. The legitimacy of this stop and the subsequent arrest is not before us.</p>
<p>[2]  "Q. All right. Now, Willie, calling your attention to February 22, 1968, did you receive a call from the police asking you to come down to the station?
</p>
<p>"A. Yes, I did.</p>
<p>.....</p>
<p>"Q. When you went down there, what if anything, happened, Willie?</p>
<p>"A. Well, I seen the two men was down there who robbed me.</p>
<p>.....</p>
<p>"Q. Who took you to the police station?</p>
<p>"A. The policeman picked me up.</p>
<p>.....</p>
<p>"MR. POMARO: Q. When you went to the police station did you see the two defendants?</p>
<p>"A. Yes, I did.</p>
<p>"Q. Do you see them in Court today?</p>
<p>"A. Yes, sir.</p>
<p>"Q. Point them out, please?</p>
<p>"A. Yes, that one there and the other one. (Indicating.)</p>
<p>"MR. POMARO: Indicating for the record the defendants Bean and Kirby.</p>
<p>"Q. And you positively identified them at the police station, is that correct?</p>
<p>"A. Yes.</p>
<p>"Q. Did any police officer make any suggestion to you whatsoever?</p>
<p>.....</p>
<p>"THE WITNESS: No, they didn't."</p>
<p>[3]  "Q. Willie, when you looked back, when you were walking down the street and first saw the defendants, when you looked back, did you see them then?
</p>
<p>"A. Yes, I seen them.</p>
<p>"Q. Did you get a good look at them then?</p>
<p>"A. Yes, I did.</p>
<p>"Q. All right. Now, when they grabbed you and took your money, did you see them then?</p>
<p>"A. Yes, I did.</p>
<p>"Q. Did you get a good look at them then?</p>
<p>"A. Yes.</p>
<p>"Q. Both of them?</p>
<p>"A. Correct.</p>
<p>"Q. When they walked away did you see them then?</p>
<p>"A. Yes.</p>
<p>"Q. Did you look at them, Willie?</p>
<p>"A. Yes.</p>
<p>"Q. Did you get a good look at them?</p>
<p>"A. Yes.</p>
<p>"Q. Are those the same two fellows? Look at them, Willie.</p>
<p>"A. Correct.</p>
<p>"Q. Are those the same two that robbed you?</p>
<p>"A. Yes.</p>
<p>"Q. You are sure, Willie?</p>
<p>"A. Yes."</p>
<p>[4]  Bean's conviction was reversed. <i>People</i> v. <i>Bean,</i> <span class="citation" data-id="9730814"><a href="/opinion/2173626/people-v-bean/" aria-description="Citation for case: People v. Bean">121 Ill. App. 2d 332</a></span>, <span class="citation" data-id="9730814"><a href="/opinion/2173626/people-v-bean/" aria-description="Citation for case: People v. Bean">257 N. E. 2d 562</a></span>.</p>
<p>[5]  The issue of the applicability of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> to pre-indictment confrontation has severely divided the courts. Compare <i>State</i> v. <i>Fields,</i> <span class="citation" data-id="2619642"><a href="/opinion/2619642/state-v-fields/" aria-description="Citation for case: State v. Fields">104 Ariz. 486</a></span>, <span class="citation" data-id="2619642"><a href="/opinion/2619642/state-v-fields/" aria-description="Citation for case: State v. Fields">455 P. 2d 964</a></span>; <i>Perkins</i> v. <i>State,</i> <span class="citation" data-id="1147816"><a href="/opinion/1147816/perkins-v-state/" aria-description="Citation for case: Perkins v. State">228 So. 2d 382</a></span> (Fla.); <i>Buchanan</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1205361"><a href="/opinion/1205361/buchanan-v-commonwealth/" aria-description="Citation for case: Buchanan v. Commonwealth">210 Va. 664</a></span>, <span class="citation" data-id="1205361"><a href="/opinion/1205361/buchanan-v-commonwealth/" aria-description="Citation for case: Buchanan v. Commonwealth">173 S. E. 2d 792</a></span>; <i>State</i> v. <i>Walters,</i> <span class="citation" data-id="1778052"><a href="/opinion/1778052/state-v-walters/" aria-description="Citation for case: State v. Walters">457 S. W. 2d 817</a></span> (Mo.), with <i>United States</i> v. <i>Greene,</i> 139 U. S. App. D. C. 9, <span class="citation" data-id="9455829"><a href="/opinion/291198/united-states-v-ronald-s-greene/" aria-description="Citation for case: United States v. Ronald S. Greene">429 F. 2d 193</a></span>; <i>Rivers</i> v. <i>United States,</i> <span class="citation" data-id="281672"><a href="/opinion/281672/willie-samuel-rivers-v-united-states/" aria-description="Citation for case: Willie Samuel Rivers v. United States">400 F. 2d 935</a></span> (CA5); <i>United States</i> v. <i>Phillips,</i> <span class="citation" data-id="9455735"><a href="/opinion/290711/united-states-v-jimmie-dale-phillips/" aria-description="Citation for case: United States v. Jimmie Dale Phillips">427 F. 2d 1035</a></span> (CA9); <i>Commonwealth</i> v. <i>Guillory,</i> <span class="citation" data-id="2212706"><a href="/opinion/2212706/commonwealth-v-guillory/" aria-description="Citation for case: Commonwealth v. Guillory">356 Mass. 591</a></span>, <span class="citation" data-id="2212706"><a href="/opinion/2212706/commonwealth-v-guillory/" aria-description="Citation for case: Commonwealth v. Guillory">254 N. E. 2d 427</a></span>; <i>People</i> v. <i>Fowler,</i> <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/" aria-description="Citation for case: People v. Fowler">1 Cal. 3d 335</a></span>, <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/" aria-description="Citation for case: People v. Fowler">461 P. 2d 643</a></span>; <i>Palmer</i> v. <i>State,</i> <span class="citation" data-id="1559532"><a href="/opinion/1559532/palmer-v-state/" aria-description="Citation for case: Palmer v. State">5 Md. App. 691</a></span>, <span class="citation" data-id="1559532"><a href="/opinion/1559532/palmer-v-state/" aria-description="Citation for case: Palmer v. State">249 A. 2d 482</a></span>; <i>People</i> v. <i>Hutton,</i> <span class="citation" data-id="1605190"><a href="/opinion/1605190/people-v-hutton/" aria-description="Citation for case: People v. Hutton">21 Mich. App. 312</a></span>, <span class="citation" data-id="1605190"><a href="/opinion/1605190/people-v-hutton/" aria-description="Citation for case: People v. Hutton">175 N. W. 2d 860</a></span>; <i>Commonwealth</i> v. <i>Whiting,</i> <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">439 Pa. 205</a></span>, <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">266 A. 2d 738</a></span>; <i>In re Holley,</i> 107 R. I. 615, <span class="citation" data-id="1935989"><a href="/opinion/1935989/in-re-holley/" aria-description="Citation for case: In Re Holley">268 A. 2d 723</a></span>; <i>Hayes</i> v. <i>State,</i> <span class="citation" data-id="9658400"><a href="/opinion/1605345/hayes-v-states/" aria-description="Citation for case: Hayes v. States">46 Wis. 2d 93</a></span>, <span class="citation" data-id="9658400"><a href="/opinion/1605345/hayes-v-states/" aria-description="Citation for case: Hayes v. States">175 N. W. 2d 625</a></span>.</p>
<p>[6]  "[D]uring perhaps the most critical period of the proceedings against these defendants, that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation were vitally important, the defendants did not have the aid of counsel in any real sense, although they were as much entitled to such aid during that period as at the trial itself." <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 57</a></span>.</p>
<p>[7]  "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defense." U. S. Const., Amdt. VI.</p>
<p>[8]  In view of our limited grant of certiorari, we do not consider whether there might have been a deprivation of due process in the particularized circumstances of this case. That question remains open for inquiry in a federal habeas corpus proceeding.</p>
<p>[1]  There is no room here for the application of the harmless-error doctrine. Because the admission of Shard's testimony about his showup identification thus requires reversal, there is no need for me to consider whether a remand would otherwise be necessary to afford the State an opportunity to demonstrate that Shard's in-court identification of petitioner, if that is what it was, see <i>ante,</i> at 686 n. 3, had an independent source. See <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#239" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 239-242</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 272</a></span> (1967).</p>
<p>[2]  The plurality asserts that in view of that holding in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> "the doctrine of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, has no applicability whatever to the issue before us." <i>Ante,</i> at 688. That assertion is necessary for the plurality because <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires the presence of counsel before "the time that adversary judicial proceedings have been initiated against" the accused. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The assertion is nonetheless erroneous, for <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> specifically relied upon <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in establishing the constitutional principle that controls the applicability of the Sixth Amendment guarantee of the right to counsel at pretrial confrontations. See 388 U. S., at 226-227.</p>
<p>[3]  The plurality asserts that "<span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois"><i>Escobedo</i></a></span> is not apposite here." <i>Ante,</i> at 689. It was, of course, "apposite" in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>.</i> Hence, to say that <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#733" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 733-734</a></span> (1966), a case decided before <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> "limited the holding of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> to its own facts," <i>ante,</i> at 689, even if true, is to say nothing at all that is relevant to the present case. The plurality also utilizes <i>Johnson</i> for the proposition "that the `prime purpose' of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was not to vindicate the constitutional right to counsel as such, but, like <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> `to guarantee full effectuation of the privilege against self-incrimination. . . .' " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> In view of <i>Wade's</i> specific reliance upon <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> that, obviously, is no distinction either. Moreover, it implies that the purpose of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> was "to vindicate the constitutional right to counsel as such." That was not the purpose of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> as my extended summary of the opinion demonstrates.</p>
<p>[4]  The plurality refers to "occasions during the course of a criminal investigation when the police do abuse identification procedures" and asserts that "[s]uch abuses are not beyond the reach of the Constitution." <i>Ante,</i> at 690. The constitutional principles established in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> however, are not addressed solely to police "abuses," as <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> explicitly pointed out:
</p>
<p>"The few cases that have surfaced therefore reveal the existence of a process attended with hazards of serious unfairness to the criminal accused and strongly suggest the plight of the more numerous defendants who are unable to ferret out suggestive influences in the secrecy of the confrontation. We do not assume that these risks are the result of police procedures intentionally designed to prejudice an accused. Rather we assume they derive from the dangers inherent in eyewitness identification and the suggestibility inherent in the context of the pretrial identification." 388 U. S., at 234-235.</p>
<p>[5]  This case does not require me to consider confrontations that take place before custody, see, <i>e. g., </i><i>Bratten</i> v. <i>Delaware,</i> <span class="citation" data-id="1428383"><a href="/opinion/1428383/bratten-v-state-of-delaware/" aria-description="Citation for case: Bratten v. State of Delaware">307 F. Supp. 643</a></span> (Del. 1969); <i>People</i> v. <i>Cesarz,</i> <span class="citation" data-id="9885094"><a href="/opinion/2237741/the-people-v-cesarz/" aria-description="Citation for case: The PEOPLE v. Cesarz">44 Ill. 2d 180</a></span>, <span class="citation" data-id="9885094"><a href="/opinion/2237741/the-people-v-cesarz/" aria-description="Citation for case: The PEOPLE v. Cesarz">255 N. E. 2d 1</a></span> (1969); <i>State</i> v. <i>Moore,</i> 111 N. J. Super. 528, <span class="citation" data-id="2267026"><a href="/opinion/2267026/state-v-moore/" aria-description="Citation for case: State v. Moore">269 A. 2d 534</a></span> (1970), nor accidental confrontations not arranged by the police, see, <i>e. g., </i><i>United States</i> v. <i>Pollack,</i> <span class="citation" data-id="290752"><a href="/opinion/290752/united-states-v-shelby-louis-pollack/" aria-description="Citation for case: United States v. Shelby Louis Pollack">427 F. 2d 1168</a></span> (CA5 1970); <i>State</i> v. <i>Bibbs,</i> <span class="citation" data-id="1753794"><a href="/opinion/1753794/state-v-bibbs/" aria-description="Citation for case: State v. Bibbs">461 S. W. 2d 755</a></span> (Mo. 1970), nor on-the-scene encounters shortly after the crime, see, <i>e. g., </i><i>Russell</i> v. <i>United States,</i> 133 U. S. App. D. C. 77, <span class="citation" data-id="9454412"><a href="/opinion/284146/bobby-russell-v-united-states/" aria-description="Citation for case: Bobby Russell v. United States">408 F. 2d 1280</a></span> (1969); <i>United States</i> v. <i>Davis,</i> <span class="citation" data-id="281459"><a href="/opinion/281459/united-states-v-james-douglas-davis/" aria-description="Citation for case: United States v. James Douglas Davis">399 F. 2d 948</a></span> (CA2 1968).</p>
<p>[6]  Cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 477</a></span> (1966) (emphasis added):
</p>
<p>"The principles announced today deal with the protection which must be given to the privilege against self-incrimination when the individual is first subjected to police interrogation <i>while in custody at the station or otherwise deprived of his freedom of action in any significant way. It is at this point that our adversary system of criminal proceedings commences,</i> distinguishing itself at the outset from the inquisitorial system recognized in some countries."</p>
<p>[7]  The plurality concludes that "[i]t is this point, therefore, that marks the commencement of the `criminal prosecutions' to which alone the explicit guarantees of the Sixth Amendment are applicable." <i>Ante,</i> at 690. This Court has taken the contrary position with respect to the speedy-trial guarantee of the Sixth Amendment: "Invocation of the speedy trial provision thus need not await indictment, information, or other formal charge. But we decline to extend the reach of the amendment to the period prior to arrest." "In the case before us, neither appellee was arrested, charged, or otherwise subjected to formal restraint prior to indictment. It was this event, therefore, which transformed the appellees into `accused' defendants who are subject to the speedy trial protections of the Sixth Amendment." <i>United States</i> v. <i>Marion,</i> <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#321" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 321, 325</a></span> (1971).</p>
<p>[8]  As the California Supreme Court pointed out, with an eye toward the real world, "the establishment of the date of formal accusation as the time wherein the right to counsel at lineup attaches could only lead to a situation wherein substantially all lineups would be conducted prior to indictment or information." <i>People</i> v. <i>Fowler,</i> <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/#344" aria-description="Citation for case: People v. Fowler">1 Cal. 3d 335, 344</a></span>, <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/#650" aria-description="Citation for case: People v. Fowler">461 P. 2d 643, 650</a></span> (1969).</p>
<p>[9]  Bean took the stand and testified that he and petitioner found Shard's traveler's checks and Social Security card two hours before their arrest strewn upon the ground in an alley.</p>
<p>[10]  In fact, the lineups in <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> took place before the information was filed. The crime occurred on January 25, 1966. After the accused was arrested, he was exhibited to the witness in two lineups, both conducted within two weeks of January 25. The information was not filed until March 17. <i>Foster</i> v. <i>California</i><i>,</i> No. 47, O. T. 1968, Brief for Respondent 3-8.</p>
<p>[11]  In fact, the lineup in <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> took place before the accused were formally charged. The crime occurred on July 24, 1966. The accused were arrested on September 29, and the lineup was held on October 1. The preliminary hearing was not until October 14, and the indictments were not returned until November 11. <i>Coleman</i> v. <i>Alabama</i><i>,</i> No. 72, O. T. 1969, Brief for Petitioners 5-7; App. 84; see <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#26" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 26</a></span> (STEWART, J., joined by BURGER, C. J., dissenting).
</p>
<p>On those facts, the plurality opinion adverted to the timing of the lineup only to the extent of pointing out that it was held "about two months after the assault and seven months before petitioners' trial." <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#3" aria-description="Citation for case: Coleman v. Alabama"><i>Id.,</i> at 3</a></span> (BRENNAN, J., joined by DOUGLAS, WHITE, and MARSHALL, JJ.). The plurality opinion then simply noted that "[p]etitioners concede that since the lineup occurred before [<span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade"><i>Wade</i></a></span> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i>] were decided . . . , they cannot invoke the holding of those cases requiring the exclusion of in-court identification evidence which is tainted by exhibiting the accused to identifying witnesses before trial in the absence of counsel." <i>Id.,</i> at 3-4.</p>
<p>Mr. Justice Black in his concurring opinion took no notice at all of when the lineup was conducted. Instead, reiterating his view that <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> "should be held fully retroactive," he insisted "that petitioners in this pre-<span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade"><i>Wade</i></a></span> case were entitled to court-appointed counsel at the time of the lineup in which they participated and that Alabama's failure to provide such counsel violated petitioners' rights under the Sixth and Fourteenth Amendments." <i>Id.,</i> at 13. Nor did Mr. Justice Harlan refer to the timing of the lineup in expressing his "dissent from the refusal to accord petitioners the benefit of the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> holding, neither petitioner having been afforded counsel at the police `lineup' identification." Mr. Justice Harlan's summary of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>,</i> like that of the prevailing opinion, did not limit its "rationale" to post-charge confrontations: "The <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> rule requires the exclusion of any in-court identification preceded by a pretrial lineup where the accused was not represented by counsel, unless the in-court identification is found to be derived from a source `independent' of the tainted pretrial viewing." <i>Id.,</i> at 21.</p>
<p>[12]  The chain of events in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> was as follows: The crime occurred on the night of August 23, 1961. The accused was arrested on the afternoon of August 24 and appeared for arraignment on the morning of August 25. The arraignment was postponed until August 31 so that he could retain counsel. The confrontation with the witness took place about noon on August 25. At the arraignment on August 31, the committing magistrate appointed counsel for the accused and set the felony examination for September 1. That examination was never held, for on August 31 the indictment was returned. <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno</a></span></i><i>,</i> No. 254, O. T. 1966, Brief for Respondent 34.</p>
<p>[13]  The <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> dissenters found no such limitation: "The rule applies to any lineup, to any other techniques employed to produce an identification and a <i>fortiori</i> to a face-to-face encounter between the witness and the suspect alone, regardless of when the identification occurs, in time or place, and whether before or after indictment or information." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#251" aria-description="Citation for case: United States v. Wade">388 U. S., at 251</a></span> (WHITE, J., joined by Harlan and STEWART, JJ., dissenting in part and concurring in part).</p>
<p>[14]  The plurality rather surprisingly asserts that "[t]he issue of the applicability of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> to pre-indictment confrontation has <i>severely</i> divided the courts." <i>Ante,</i> at 687 n. 5 (emphasis added). As the plurality's citations reveal, there are decisions from five States, including Illinois, that have refused to apply <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> to pre-indictment confrontations for identification. Ranged against those five, however, are decisions from at least 13 States. See <i>People</i> v. <i>Fowler,</i> <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/" aria-description="Citation for case: People v. Fowler">1 Cal. 3d 335</a></span>, <span class="citation" data-id="9541533"><a href="/opinion/1159535/people-v-fowler/" aria-description="Citation for case: People v. Fowler">461 P. 2d 643</a></span> (1969); <i>State</i> v. <i>Singleton,</i> <span class="citation" data-id="1714361"><a href="/opinion/1714361/state-v-singleton/" aria-description="Citation for case: State v. Singleton">253 La. 18</a></span>, <span class="citation" data-id="1714361"><a href="/opinion/1714361/state-v-singleton/" aria-description="Citation for case: State v. Singleton">215 So. 2d 838</a></span> (1968); <i>Commonwealth</i> v. <i>Guillory,</i> <span class="citation" data-id="2212706"><a href="/opinion/2212706/commonwealth-v-guillory/" aria-description="Citation for case: Commonwealth v. Guillory">356 Mass. 591</a></span>, <span class="citation" data-id="2212706"><a href="/opinion/2212706/commonwealth-v-guillory/" aria-description="Citation for case: Commonwealth v. Guillory">254 N. E. 2d 427</a></span> (1970); <i>Palmer</i> v. <i>State,</i> <span class="citation" data-id="1559532"><a href="/opinion/1559532/palmer-v-state/" aria-description="Citation for case: Palmer v. State">5 Md. App. 691</a></span>, <span class="citation" data-id="1559532"><a href="/opinion/1559532/palmer-v-state/" aria-description="Citation for case: Palmer v. State">249 A. 2d 482</a></span> (1969); <i>People</i> v. <i>Hutton,</i> <span class="citation" data-id="1605190"><a href="/opinion/1605190/people-v-hutton/" aria-description="Citation for case: People v. Hutton">21 Mich. App. 312</a></span>, <span class="citation" data-id="1605190"><a href="/opinion/1605190/people-v-hutton/" aria-description="Citation for case: People v. Hutton">175 N. W. 2d 860</a></span> (1970); <i>Thompson</i> v. <i>State,</i> <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">85 Nev. 134</a></span>, <span class="citation" data-id="9629152"><a href="/opinion/1434555/thompson-v-state/" aria-description="Citation for case: Thompson v. State">451 P. 2d 704</a></span> (1969); <i>State</i> v. <i>Wright,</i> <span class="citation" data-id="1395727"><a href="/opinion/1395727/state-v-wright/" aria-description="Citation for case: State v. Wright">274 N. C. 84</a></span>, <span class="citation" data-id="1395727"><a href="/opinion/1395727/state-v-wright/" aria-description="Citation for case: State v. Wright">161 S. E. 2d 581</a></span> (1968); <i>State</i> v. <i>Isaacs,</i> <span class="citation" data-id="3756832"><a href="/opinion/4002685/state-v-isaacs/" aria-description="Citation for case: State v. Isaacs">24 Ohio App. 2d 115</a></span>, <span class="citation" data-id="3756832"><a href="/opinion/4002685/state-v-isaacs/" aria-description="Citation for case: State v. Isaacs">265 N. E. 2d 327</a></span> (1970); <i>Commonwealth</i> v. <i>Whiting,</i> <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">439 Pa. 205</a></span>, <span class="citation" data-id="2178575"><a href="/opinion/2178575/commonwealth-v-whiting/" aria-description="Citation for case: Commonwealth v. Whiting">266 A. 2d 738</a></span> (1970); <i>In re Holley,</i> 107 R. I. 615, <span class="citation multiple-matches"><a href="/c/A.%202d/268/723/">268 A. 2d 723</a></span> (1970); <i>Martinez</i> v. <i>State,</i> <span class="citation" data-id="2457586"><a href="/opinion/2457586/martinez-v-state/" aria-description="Citation for case: Martinez v. State">437 S. W. 2d 842</a></span> (Tex. Ct. Crim. App. 1969); <i>State</i> v. <i>Hicks,</i> <span class="citation" data-id="2619489"><a href="/opinion/2619489/state-v-hicks/" aria-description="Citation for case: State v. Hicks">76 Wash. 2d 80</a></span>, <span class="citation" data-id="2619489"><a href="/opinion/2619489/state-v-hicks/" aria-description="Citation for case: State v. Hicks">455 P. 2d 943</a></span> (1969); <i>Hayes</i> v. <i>State,</i> <span class="citation" data-id="9658400"><a href="/opinion/1605345/hayes-v-states/" aria-description="Citation for case: Hayes v. States">46 Wis. 2d 93</a></span>, <span class="citation" data-id="9658400"><a href="/opinion/1605345/hayes-v-states/" aria-description="Citation for case: Hayes v. States">175 N. W. 2d 625</a></span> (1970).
</p>
<p>In addition, <i>every</i> United States Court of Appeals that has confronted the question has applied <i>Wade</i> and <i>Gilbert</i> to pre-indictment confrontations. See <i>United States</i> v. <i>Greene,</i> 139 U. S. App. D. C. 9, <span class="citation" data-id="9455829"><a href="/opinion/291198/united-states-v-ronald-s-greene/" aria-description="Citation for case: United States v. Ronald S. Greene">429 F. 2d 193</a></span> (1970); <i>Cooper</i> v. <i>Picard,</i> <span class="citation" data-id="291123"><a href="/opinion/291123/charles-f-cooper-v-philip-j-picard-superintendent-massachusetts/" aria-description="Citation for case: Charles F. Cooper v. Philip J. Picard, Superintendent,...">428 F. 2d 1351</a></span> (CA1 1970); <i>United States</i> v. <i>Ayers,</i> <span class="citation" data-id="290198"><a href="/opinion/290198/united-states-v-dewey-joseph-ayers/" aria-description="Citation for case: United States v. Dewey Joseph Ayers">426 F. 2d 524</a></span> (CA2 1970); <i>Government of Virgin Islands</i> v. <i>Callwood,</i> <span class="citation" data-id="295963"><a href="/opinion/295963/government-of-the-virgin-islands-v-charles-callwood/" aria-description="Citation for case: Government of the Virgin Islands v. Charles Callwood">440 F. 2d 1206</a></span> (CA3 1971); <i>Rivers</i> v. <i>United States,</i> <span class="citation" data-id="281672"><a href="/opinion/281672/willie-samuel-rivers-v-united-states/" aria-description="Citation for case: Willie Samuel Rivers v. United States">400 F. 2d 935</a></span> (CA5 1968); <i>United States</i> v. <i>Broadhead,</i> <span class="citation" data-id="285891"><a href="/opinion/285891/united-states-v-donald-a-broadhead/" aria-description="Citation for case: United States v. Donald A. Broadhead">413 F. 2d 1351</a></span> (CA7 1969); <i>United States</i> v. <i>Phillips,</i> <span class="citation" data-id="9455735"><a href="/opinion/290711/united-states-v-jimmie-dale-phillips/" aria-description="Citation for case: United States v. Jimmie Dale Phillips">427 F. 2d 1035</a></span> (CA9 1970); <i>Wilson</i> v. <i>Gaffney,</i> <span class="citation" data-id="301056"><a href="/opinion/301056/charles-j-wilson-aka-james-griffin-v-r-j-gaffney-warden/" aria-description="Citation for case: Charles J. Wilson, A/K/A James Griffin v. R. J. Gaffney,...">454 F. 2d 142</a></span> (CA10 1972). As Chief Judge Lewis, speaking for the Court of Appeals for the Tenth Circuit, put it in the last-cited case:</p>
<p>"In both <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> the lineups were conducted after indictments had been returned; in the case at bar, the lineup occurred before petitioner had been formally charged. But surely the assistance of counsel, now established as an absolute post-indictment right does not arise or attach because of the return of an indictment. The confrontation of a lineup . . . cannot have a constitutional distinction based upon the lodging of a formal charge. Every reason set forth by the Supreme Court in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> . . . for the assistance of counsel post-indictment has equal or more impact when projected against a pre-indictment atmosphere. We hold that petitioner had a right to counsel at the lineup here considered." <i>Id.,</i> at 144.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Kirk v. Louisiana.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Kirk v. Louisiana"
type: case
citation: "536 U.S. 635 (2002)"
parallel_cite: "122 S. Ct. 2458; 153 L. Ed. 2d 599; 2002 D.A.R. 7071"
neutral_cite: 2002 U.S. LEXIS 4682
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kirk v. Louisiana
  varies_by_point: false
  scope_note: "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121167/kirk-v-louisiana/"
  cluster_id: 121167
  opinion_id: 121167
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Progeny"
related: ["[[Payton v. New York]]", "[[Steagald v. United States]]", "[[Welsh v. Wisconsin]]", "[[Kentucky v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "warrant", "exigent-circumstances", "per-curiam"]
holding: "Absent exigent circumstances, police may not enter a home to make a warrantless arrest; a lawful home entry requires a warrant or probable cause plus exigent circumstances (reaffirming Payton)."
lake:
  record_id: Kirk v. Louisiana
  status: verified
  projected_at: 2026-07-06
---

# Kirk v. Louisiana

*536 U.S. 635 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After an anonymous tip that drugs were being sold from Kirk's apartment, officers watched the apartment, saw what appeared to be several drug purchases, and stopped one buyer on the street nearby. Fearing that evidence would be destroyed, they entered Kirk's apartment without a warrant, arrested him, frisked him (finding a cocaine vial in his underwear), and observed contraband in plain view; only then did they obtain a search warrant. The Louisiana Court of Appeal upheld the entry and search without deciding whether [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] existed, reasoning that the officers had probable cause to arrest and that the incriminating evidence was found on Kirk's person incident to the arrest.

## Issue
Whether police may make a warrantless entry into a home to arrest a suspect — and conduct a search incident to that arrest — without either a warrant or [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], so long as they have probable cause to arrest.

## Rule
No. The Fourth Amendment draws a firm line at the home's threshold: under *[[Payton v. New York]]*, "[a]bsent exigent circumstances," the "firm line at the entrance to the house . . . may not reasonably be crossed without a warrant." — 536 U.S. at 636 (quoting *Payton*). ^pin-636

Accordingly, "police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal's ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated *Payton*." — *Id.* at 638. ^pin-638

## Application
The officers had neither an arrest warrant nor a search warrant when they entered Kirk's home, arrested him, and searched him. They invoked a fear that evidence would be destroyed, but the Louisiana court never determined whether such [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] actually existed; it treated the [[Exigent Circumstances and Hot Pursuit|exigency]] question as irrelevant because the cocaine and money were recovered from Kirk's person in a [[Search Incident to Arrest|search incident to arrest]]. That analysis inverted *[[Payton v. New York|Payton]]*: the lawfulness of the warrantless home entry — the predicate for the arrest and the search incident to it — turned precisely on whether [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] justified crossing the threshold. The Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for the [[Exigent Circumstances and Hot Pursuit|exigency]] assessment, expressing no opinion on whether [[Exigent Circumstances and Hot Pursuit|exigency]] was in fact present or on the State's independent-source argument.

## Conclusion
A warrantless entry into a home to arrest requires probable cause plus [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] (or a warrant); because the state court never decided the [[Exigent Circumstances and Hot Pursuit|exigency]] question, its judgment violated *[[Payton v. New York|Payton]]* and was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Kirk* is a straightforward reaffirmation of [[Payton v. New York]]; it operates alongside [[Steagald v. United States]] (search warrant needed to arrest in a third party's home), [[Welsh v. Wisconsin]] ([[Exigent Circumstances and Hot Pursuit|exigency]] narrowly applied to minor offenses), and [[Kentucky v. King]] (police-created-[[Exigent Circumstances and Hot Pursuit|exigency]] limits).

## Appears on
- [[Arrest in the Home]] — *Progeny*

## Sources
- *Kirk v. Louisiana*, 536 U.S. 635 (2002) (per curiam) — https://www.courtlistener.com/opinion/121167/kirk-v-louisiana/ — pinpoints: 636, 638.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "154ecde2e3316a46", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kirk v. Louisiana"}, "payload": {"all": [{"cite": "536 U.S. 635", "page": "635", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "536"}, {"cite": "122 S. Ct. 2458", "page": "2458", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "153 L. Ed. 2d 599", "page": "599", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "153"}, {"cite": "2002 U.S. LEXIS 4682", "page": "4682", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}, {"cite": "2002 D.A.R. 7071", "page": "7071", "reporter": "D.A.R.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2002"}], "display": "536 U.S. 635", "official": {"cite": "536 U.S. 635", "page": "635", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "536"}, "official_selection_present": true, "record_id": "Kirk v. Louisiana"}}
{"assertion_id": "3cd856a1f7e1aa11", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-638", "record_id": "Kirk v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-638", "pinpoint_status": "slip-only", "quote": "police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal's ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated *Payton*.", "quote_fidelity": "mismatch", "record_id": "Kirk v. Louisiana", "star_marker": null}}
{"assertion_id": "45192af11e7457d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-636", "record_id": "Kirk v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-636", "pinpoint_status": "slip-only", "quote": "--- # Kirk v. Louisiana *536 U.S. 635 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip that drugs were being sold from Kirk's apartment, officers watched the apartment, saw what appeared to be several drug purchases, and stopped one buyer on the street nearby. Fearing that evidence would be destroyed, they entered Kirk's apartment without a warrant, arrested him, frisked him (finding a cocaine vial in his underwear), and observed contraband in plain view; only then did they obtain a search warrant. The Louisiana Court of Appeal upheld the entry and search without deciding whether exigent circumstances existed, reasoning that the officers had probable cause to arrest and that the incriminating evidence was found on Kirk's person incident to the arrest. ## Issue Whether police may make a warrantless entry into a home to arrest a suspect — and conduct a search incident to that arrest — without either a warrant or exigent circumstances, so long as they have probable cause to arrest. ## Rule No. The Fourth Amendment draws a firm line at the home's threshold: under *Payton v. New York*,", "quote_fidelity": "mismatch", "record_id": "Kirk v. Louisiana", "star_marker": null}}
{"assertion_id": "c79e814e973e9b42", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kirk v. Louisiana"}, "payload": {"as_of_content": "2002-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kirk v. Louisiana", "scope_note": "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances.", "varies_by_point": false}}
```

### lake record — Kirk v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kirk v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kirk v. Louisiana",
    "case_name_short": "Kirk",
    "case_name_full": "Kirk v. Louisiana",
    "input_case_name": "Kirk v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-24",
    "year": 2002,
    "docket": null,
    "cluster_id": 121167,
    "lead_opinion_id": 121167,
    "sibling_ids": [
      121167
    ],
    "absolute_url": "/opinion/121167/kirk-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 635",
      "volume": "536",
      "reporter": "U.S.",
      "page": "635",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2458",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 599",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 D.A.R. 7071",
        "volume": "2002",
        "reporter": "D.A.R.",
        "page": "7071",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4682",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4682",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 635",
        "volume": "536",
        "reporter": "U.S.",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2458",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 599",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4682",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4682",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 D.A.R. 7071",
        "volume": "2002",
        "reporter": "D.A.R.",
        "page": "7071",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 635",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 635",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-636",
      "page": null,
      "quote": "--- # Kirk v. Louisiana *536 U.S. 635 (2002)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After an anonymous tip that drugs were being sold from Kirk's apartment, officers watched the apartment, saw what appeared to be several drug purchases, and stopped one buyer on the street nearby. Fearing that evidence would be destroyed, they entered Kirk's apartment without a warrant, arrested him, frisked him (finding a cocaine vial in his underwear), and observed contraband in plain view; only then did they obtain a search warrant. The Louisiana Court of Appeal upheld the entry and search without deciding whether exigent circumstances existed, reasoning that the officers had probable cause to arrest and that the incriminating evidence was found on Kirk's person incident to the arrest. ## Issue Whether police may make a warrantless entry into a home to arrest a suspect \u2014 and conduct a search incident to that arrest \u2014 without either a warrant or exigent circumstances, so long as they have probable cause to arrest. ## Rule No. The Fourth Amendment draws a firm line at the home's threshold: under *Payton v. New York*,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-638",
      "page": null,
      "quote": "police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal's ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated *Payton*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kirk v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam. Reaffirms Payton v. New York: absent exigent circumstances, police may not make a warrantless entry into a home to arrest; they need either a warrant or probable cause plus exigent circumstances.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
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
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Hogan v. City of Corpus Christi, Texas",
          "cluster_id": 1033766,
          "cite": [
            "722 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fleming",
          "cluster_id": 2488640,
          "cite": [
            "76 So. 3d 417",
            "2011 La. LEXIS 3008",
            "2011 WL 6309435"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Forbes",
          "cluster_id": 5938198,
          "cite": [
            "71 A.D.3d 1519",
            "897 N.Y.S.2d 352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gallagher v. City of Winlock Washington",
          "cluster_id": 8688333,
          "cite": [
            "287 F. App'x 568"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Martins",
          "cluster_id": 201656,
          "cite": [
            "413 F.3d 139",
            "2005 U.S. App. LEXIS 12704",
            "2005 WL 1502939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guy Christopher Brooks",
          "cluster_id": 786149,
          "cite": [
            "367 F.3d 1128",
            "2004 U.S. App. LEXIS 9349",
            "2004 WL 1066612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Estrada v. State",
          "cluster_id": 1795405,
          "cite": [
            "116 S.W.3d 370",
            "2003 Tex. App. LEXIS 7427",
            "2003 WL 22023640"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janet Feliciano v. City of Miami Beach",
          "cluster_id": 819741,
          "cite": [
            "707 F.3d 1244",
            "2013 WL 425445",
            "2013 U.S. App. LEXIS 2524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Steelman",
          "cluster_id": 1891638,
          "cite": [
            "93 S.W.3d 102",
            "2002 Tex. Crim. App. LEXIS 206",
            "2002 WL 31398545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl D. Lyons v. City of Xenia, Christine Keith, Officer Matthew Foubert, Officer",
          "cluster_id": 791266,
          "cite": [
            "417 F.3d 565",
            "2005 U.S. App. LEXIS 16034",
            "2005 WL 1846994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Coffin v. Stacy Brandau",
          "cluster_id": 3048939,
          "cite": [
            "642 F.3d 999",
            "2011 U.S. App. LEXIS 11353",
            "2011 WL 2162997"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saleem Bashir v. Rockdale County, Georgia",
          "cluster_id": 77293,
          "cite": [
            "445 F.3d 1323",
            "2006 U.S. App. LEXIS 9311",
            "2006 WL 962608"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clifton Myers A/K/A Samuel Jenkins, Clifton Myers",
          "cluster_id": 779561,
          "cite": [
            "308 F.3d 251",
            "2002 U.S. App. LEXIS 21264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loria v. Gorman",
          "cluster_id": 7108550,
          "cite": [
            "306 F.3d 1271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Meeks",
          "cluster_id": 1057727,
          "cite": [
            "262 S.W.3d 710",
            "2008 Tenn. LEXIS 575",
            "2008 WL 4007429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burke v. Town of Walpole",
          "cluster_id": 201555,
          "cite": [
            "405 F.3d 66",
            "2005 U.S. App. LEXIS 7105",
            "2005 WL 949688"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin McClain George Brandt, III Jason Davis",
          "cluster_id": 793976,
          "cite": [
            "444 F.3d 556",
            "2006 U.S. App. LEXIS 32292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theodore E. Loria v. Charles Gorman, Individually and in His Capacity as a Police Officer for the City of Rochester, Robert Nitchman, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester, Mark Wiater, George Markert, Individually and in His Capacity as a Police Officer for the City of Rochester, Vasquez, Individually and in His Capacity as a Police Officer for the City of Rochester, Debra Stritzel, Individually and in Her Capacity as an Employee of the City of Rochester, Theodore E. Loria v. Dale Feor, Individually and in His Capacity as a Police Officer for the City of Rochester, City of Rochester",
          "cluster_id": 779429,
          "cite": [
            "306 F.3d 1271",
            "2002 U.S. App. LEXIS 20458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Com.",
          "cluster_id": 1058715,
          "cite": [
            "639 S.E.2d 217",
            "273 Va. 26",
            "2007 Va. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Cloutier",
          "cluster_id": 4421636,
          "cite": [
            "869 F.3d 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sandoval v. Las Vegas Metropolitan Police Department",
          "cluster_id": 2681571,
          "cite": [
            "756 F.3d 1154",
            "2014 WL 2936254",
            "2014 U.S. App. LEXIS 12395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McBride",
          "cluster_id": 2483841,
          "cite": [
            "928 N.E.2d 1027",
            "14 N.Y.3d 440",
            "902 N.Y.S.2d 830"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Demetrius Pruitt",
          "cluster_id": 795278,
          "cite": [
            "458 F.3d 477",
            "2006 U.S. App. LEXIS 20555",
            "2006 WL 2320962"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bates v. Harvey",
          "cluster_id": 77969,
          "cite": [
            "518 F.3d 1233",
            "2008 U.S. App. LEXIS 4559",
            "2008 WL 565774"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kirk v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121167) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 128,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 10,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 128,
        "triage_read": 11,
        "triage_snippet_classified": 117
      },
      "lane2_top_cited": {
        "query": "cites:(121167)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MSZzPTI3MjMzMDUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121167%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121167)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121167)",
    "indexed_citing_opinions": 164,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121167,
        "count": 164,
        "count_source": "search"
      }
    ],
    "citation_count": 292,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kirk-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3NTcmcz00NDczNzY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28121167%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121167,
        "cited_id": 110235,
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
    "date_created": "2026-07-05T10:11:46Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:16:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kirk v. Louisiana

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b685-10">
  Per Curiam.
 </author>
<p id="b685-11">
  Police officers entered petitioner’s home, where they arrested and searched him. The officers had neither an arrest warrant nor a search warrant. Without deciding whether exigent circumstances had been present, the Louisiana Court of Appeal concluded that the warrantless entry, arrest, and search did not violate the Fourth Amendment of the Federal Constitution because there had been probable cause to arrest petitioner. 00-0190 (La. App. 11/15/00), <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/" aria-description="Citation for case: State v. Kirk">773 So. 2d 259</a></span>. The court’s reasoning plainly violates our holding in
  <em>
   Payton
  </em>
<span citation-index="1" class="star-pagination" label="636"> 
   *636
   </span>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 590</a></span> (1980), that “[a]bsent exigent circumstances,” the “firm line at the entrance to the house ... may not reasonably be crossed without a warrant.” We thus grant the petition for a writ of certiorari and reverse the Court of Appeal’s conclusion that the officers’ actions were lawful, absent exigent circumstances.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
</p>
<p id="b686-5">
  On an evening in March 1998, police officers observed petitioner’s apartment based on an anonymous citizen complaint that drug sales were occurring there. After witnessing what appeared to be several drug purchases and allowing the buyers to leave the scene, the officers stopped one of the buyers on the street outside petitioner’s residence. The officers later testified that “[b]ecause the stop took place within a block of the apartment, [they] feared that evidence would be destroyed and ordered that the apartment be entered.” 00-0190, at 2, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#261" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 261</a></span>. Thus, “[t]hey immediately knocked on the door of the apartment, arrested-the defendant, searched him thereto and discovered the cocaine and the money.”
  <em>
   Id.,
  </em>
  at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>. Although the officers sought and obtained a search warrant while they detained petitioner in his home, they only obtained this warrant after they had entered his home, arrested him, frisked him, found a drug vial in his underwear, and observed contraband in plain view in the apartment.
 </p>
<p id="b686-6">
  Based on these events, petitioner was charged in a Louisiana court with possession of cocaine with intent to distribute. He filed a pretrial motion to suppress evidence obtained by the police as a result of their warrantless entry, arrest, and search. After holding a suppression hearing, the trial court denied this motion. Petitioner was convicted and sentenced to 15 years at hard labor.
 </p>
<p id="b686-7">
  On direct review to the Louisiana Court of Appeal, petitioner challenged the trial court's suppression ruling. He argued that the police were not justified in entering his home
  <span citation-index="1" class="star-pagination" label="637"> 
   *637
   </span>
  without a warrant absent exigent circumstances. The Court of Appeal acknowledged petitioner’s argument: “[Petitioner] makes a long argument that there were not exigent circumstances for entering the apartment without a warrant.”
  <em>
   Id.,
  </em>
  at 2, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#261" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 261</a></span>. The court, however, declined to decide whether exigent circumstances had been present, because “the evidence required to prove that the defendant possessed cocaine with the intent to distribute, namely the cocaine and the money, was not found in the apartment, but on his person.”
  <em>
   <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/" aria-description="Citation for case: State v. Kirk">Ibid.</a></span>
  </em>
  The court concluded that because “[t]he officers had probable cause to arrest and properly searched the defendant incident thereto . . . [, t]he trial court properly denied the motion to suppress.”
  <em>
   Id.,
  </em>
  at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>.
 </p>
<p id="b687-5">
  The Louisiana Supreme Court denied review by a vote of 4 to 3. In a written dissent, Chief Justice Calogero explained:
 </p>
<blockquote id="b687-6">
  “The Fourth Amendment to the United States constitution has drawn a firm line at the entrance to the home, and thus, the police need both probable cause to either arrest or search and exigent circumstances to justify a nonconsensual warrantless intrusion into private premises. . . . Here, the defendant was arrested inside an apartment, without a warrant, and the state has not demonstrated that exigent circumstances were present. Consequently, defendant’s arrest was unconstitutional, and his motion to suppress should have been granted.” App. to Pet. for Cert. 1-2.
 </blockquote>
<p id="b687-7">
  We agree with Chief Justice Calogero that the Court of Appeal clearly erred by concluding that petitioner’s arrest and the search “incident thereto,” 00-0190, at 4, <span class="citation" data-id="1704719"><a href="/opinion/1704719/state-v-kirk/#263" aria-description="Citation for case: State v. Kirk">773 So. 2d, at 263</a></span>, were constitutionally permissible. In
  <em>
   Payton,
  </em>
  we examined whether the Fourth Amendment was violated by a state statute that authorized officers to “enter a private residence without a warrant and with force, if necessary, to make a routine felony arrest.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#574" aria-description="Citation for case: Payton v. New York">445 U. S., at 574</a></span>. We deter
  <span citation-index="1" class="star-pagination" label="638"> 
   *638
   </span>
  mined that “the reasons for upholding warrantless arrests in a public place do not apply to warrantless invasions of the privacy of the home.”
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#576" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 576</a></span>. We held that because “the Fourth Amendment has drawn a firm line at the entrance to the house ... [, a]bsent exigent circumstances, that threshold may not reasonably be crossed without a warrant.”
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 590</a></span>. And we noted that an arrest warrant founded on probable cause, as well as a search warrant, would suffice for entry.
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#603" aria-description="Citation for case: Payton v. New York"><em>
   Id.,
  </em>
  at 603</a></span>.
 </p>
<p id="b688-5">
  Here, the police had neither an arrest warrant for petitioner, nor a search warrant for petitioner’s apartment, when they entered his home, arrested him, and searched him. The officers testified at the suppression hearing that the reason for their actions was a fear that evidence would be destroyed, but the Louisiana Court of Appeal did not determine that such exigent circumstances were present. Rather, the court, in respondent’s own words, determined “thát the defendant’s argument that there were no exigent circumstances to justify the warrantless entry of the apartment was irrelevant” to the constitutionality of the officers’ actions. Brief in Opposition 2-3. As
  <em>
   Payton
  </em>
  makes plain, police officers need either a warrant or probable cause plus exigent circumstances in order to make a lawful entry into a home. The Court of Appeal’s ruling to the contrary, and consequent failure to assess whether exigent circumstances were present in this case, violated
  <em>
   Payton.
  </em>
</p>
<p id="b688-6">
  Petitioner and respondent both dispute at length whether exigent circumstances were, in fact, present. We express no opinion on that question, nor on respondent’s argument that any Fourth Amendment violation was cured because the police had an “independent source” for the recovered evidence. Brief in Opposition 8. Rather, we reverse the Court of Appeal’s judgment that exigent circumstances were not required to justify the officers’ conduct, and remand for further proceedings not inconsistent with this opinion.
 </p>
<p id="b688-7">
<em>
   It is so ordered.
  </em>
</p>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b686-8">
   We also grant petitioner's motion for leave to proceed
   <em>
    in forma pauperis.
   </em>
</p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Knight v. Jacobson.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Knight v. Jacobson
type: case
citation: "300 F.3d 1272 (2002)"
parallel_cite: ""
neutral_cite: ""
court: 11th Cir. 2002
court_level: coa
circuit: ca11
year: 2002
date_decided: 2002-09-18
docket: 01-15506
authority_weight: "Binding in-circuit — 11th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/"
  cluster_id: 778847
  opinion_id: null
  identity_checked: true
lake:
  record_id: Knight v. Jacobson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entry to Arrest]]"
    role: "Key — constructive-entry (11th Cir. narrow side: officer's body, not his voice, stays outside the threshold, 300 F.3d at 1277)"
  - page: "[[Arrest in the Home]]"
    role: "Related — constructive-entry cross-ref"
related:
  - "[[Entry to Arrest]]"
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[United States v. Watson]]"
tags:
  - case
  - fourth-amendment
  - arrest
  - warrantless-arrest
  - payton
  - threshold
  - home
holding: "Payton's warrant requirement for in-home arrests is not violated when an officer standing outside the home orders a suspect to step outside and then arrests him without a warrant — Payton keeps the officer's body, not his voice, outside the threshold."
---

# Knight v. Jacobson

*300 F.3d 1272 (11th Cir. 2002)* (No. 01-15506) · U.S. Court of Appeals for the Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 778847 → opinion 778847 (300 F.3d 1272, decided 2002-09-18); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Miami Officer Dennis Jacobson, investigating a report from Arthur Knight's ex-girlfriend, went to Knight's home. Knight came to the door in response to a knock; Jacobson, standing outside, told him to step outside. Knight complied, stepped out, and was arrested without a warrant. Knight sued under § 1983, contending the warrantless arrest violated *[[Payton v. New York]]*. The district court denied the officer summary judgment on [[Qualified Immunity|qualified immunity]], and Jacobson appealed.

## Issue
Whether *[[Payton v. New York|Payton]]*'s prohibition on warrantless in-home arrests is violated when an officer outside the home directs a suspect to step outside and then arrests him without a warrant.

## Rule
The Eleventh Circuit reversed, answering "no." *[[Payton v. New York|Payton]]* draws "a firm line at the entrance to the house" that officers may not cross without a warrant absent [[Exigent Circumstances and Hot Pursuit|exigency]] — but the arrest here happened outside that line. "*Payton* keeps the officer's body outside the threshold, not his voice. It does not prevent a law enforcement officer from telling a suspect to step outside his home and then arresting him without a warrant." — 300 F.3d at 1277.

## Application
Because Officer Jacobson never crossed the threshold and Knight was arrested just outside his door after voluntarily stepping out at the officer's request, no in-home arrest occurred. The public-place arrest was governed by the ordinary rule permitting warrantless arrests on probable cause, not by *[[Payton v. New York|Payton]]*'s in-home warrant requirement, so the officer was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The denial of summary judgment was **reversed**; Officer Jacobson was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Knight v. Jacobson* marks the boundary of the *[[Payton v. New York|Payton]]* rule: the constitutional protection attaches to physical entry across the threshold, so an officer's summons to a suspect to come outside — followed by a warrantless arrest supported by probable cause under *[[United States v. Watson]]* — does not offend the Fourth Amendment.

## Appears on
- [[Entry to Arrest]] — *Key*
- [[Arrest in the Home]] — *Related*

## Sources
- [*Knight v. Jacobson*, 300 F.3d 1272 (11th Cir. 2002)](https://www.courtlistener.com/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/) — pinpoint: 1277 (Opinion of the Court); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ad09146e51f6f8ee", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Knight v. Jacobson"}, "payload": {"all": [{"cite": "300 F.3d 1272", "page": "1272", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "300"}], "display": "300 F.3d 1272", "official": {"cite": "300 F.3d 1272", "page": "1272", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "300"}, "official_selection_present": true, "record_id": "Knight v. Jacobson"}}
{"assertion_id": "7a2cc7f37ccd5bda", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Knight v. Jacobson"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Knight v. Jacobson", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Knight v. Jacobson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Knight v. Jacobson",
  "status": "under_review",
  "identity": {
    "case_name": "Arthur Knight v. Jacobson, Officer, Badge 3359, Individual",
    "case_name_short": "",
    "case_name_full": "Arthur KNIGHT, Plaintiff-Appellee, v. JACOBSON, Officer, Badge # 3359, Individual, Defendant-Appellant",
    "input_case_name": "Knight v. Jacobson",
    "court": "11th Cir. 2002",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "ca11",
    "state": null,
    "date_decided": "2002-09-18",
    "year": 2002,
    "docket": "01-15506",
    "cluster_id": 778847,
    "lead_opinion_id": 778847,
    "sibling_ids": [],
    "absolute_url": "/opinion/778847/arthur-knight-v-jacobson-officer-badge-3359-individual/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "300 F.3d 1272",
      "volume": "300",
      "reporter": "F.3d",
      "page": "1272",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "300 F.3d 1272",
        "volume": "300",
        "reporter": "F.3d",
        "page": "1272",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "300 F.3d 1272",
    "official_selection": {
      "court_class": "state",
      "selected": "300 F.3d 1272",
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
    "date_created": "2026-07-06T05:46:16Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "knight-v-jacobson--778847",
      "to_record_id": "Knight v. Jacobson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Knight v. Jacobson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b1221-25">
  CARNES, Circuit Judge:
 </author>
<p id="b1221-26">
  This appeal by a law enforcement officer from the denial of qualified immunity presents us with these three issues: 1) whether there was an absence of probable cause for the officer’s arrest of the plaintiff; 2) whether non-compliance with state law in making an arrest is itself enough to violate
  <span citation-index="1" class="star-pagination" label="1274"> 
   *1274
   </span>
  the Fourth Amendment; and 3) whether the restrictions that
  <em>
   Payton v. New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">63 L.Ed.2d 639</a></span> (1980), places upon warrantless arrests are violated when an officer arrests a suspect who has stepped outside his home at the officer’s command. We answer each of those questions “no.”
 </p>
<p id="b1222-3">
  Miami Police Officer Dennis Jacobson investigated a report from Arthur Knight’s ex-girlfriend that Knight, who lived next door to her, had called and threatened to kill her. She recounted to Jacobson that Knight had told her that not only was he going to kill her, but that he was going to enjoy killing her and would derive great pleasure from it. Officer Jacobson interviewed the woman; she recounted those facts to him and convinced him that she feared for her life. The woman also told Officer Jacobson about other incidents involving Knight that had caused her to bring criminal charges against him, and she gave Jacobson the case numbers for two of the cases that had resulted from her previous complaints against Knight. She was visibly upset and told Officer Jacobson that she feared for her life. Based on everything he heard and his observations of the woman’s demeanor, Officer Jacobson left her apartment, went next door and knocked on Knight’s door. He told Knight to step outside, and when he did, Jacobson arrested him on the spot without first obtaining a warrant. The arrest took place at 2:00 a.m. on June 25, 1996.
 </p>
<p id="b1222-4">
  Knight’s arrest did not result in prosecution, but it did result in Knight filing a lawsuit against Jacobson under <span class="citation no-link">42 U.S.C. § 1983</span> claiming an unconstitutional arrest.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Knight contends that Officer Jacobson’s arrest of him violated the Fourth Amendment. The district court initially granted Officer Jacobson summary judgment but later took it back in an order issued under Rule 60(b)(3), the procedural details of which are not relevant to the issues that are now before us. Insofar as Officer Jacobson’s appeal from the denial of qualified immunity on the unconstitutional arrest claim is concerned—the only appeal before us—the dispositive issues are the three we stated in the opening paragraph of this opinion.
 </p>
<p id="b1222-7">
  An officer sued for having made an arrest without probable cause is entitled to qualified immunity if there was arguable probable cause for the arrest, which is a more lenient standard than probable cause.
  <em>
   See Jones v. Cannon,
  </em>
  <span class="citation" data-id="73740"><a href="/opinion/73740/jones-v-cannon/" aria-description="Citation for case: Jones v. Cannon">174 F.3d 1271</a></span>, 1283 n. 3 (11th Cir.1999) (“Arguable probable cause, not the higher standard of actual probable cause, governs the qualified immunity inquiry.”);
  <em>
   Montoute v. Carr,
  </em>
  <span class="citation" data-id="71806"><a href="/opinion/71806/montoute-v-city-of-sebring/#184" aria-description="Citation for case: Montoute v. City of Sebring">114 F.3d 181, 184</a></span> (11th Cir.1997) (“In order to be entitled to qualified immunity from a Fourth Amendment claim, an officer need not have actual probable cause but only ‘arguable probable cause,’ i.e., the facts and circumstances must be such that the officer reasonably could have believed that probable cause existed.”). The difference in the two standards is immaterial in this case because Officer Jacobson had probable cause to arrest Knight.
 </p>
<p id="b1222-8">
  Probable cause is “defined in terms of facts and circumstances sufficient to warrant a prudent man in believing that the suspect had committed or was committing an offense.”
  <em>
   Gerstein v. Pugh,
  </em>
  <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103, 111</a></span>, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#862" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854, 862</a></span>, <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span> (1975) (internal quotation marks, citation, and brackets omitted). A prudent
  <span citation-index="1" class="star-pagination" label="1275"> 
   *1275
   </span>
  man in Officer Jacobson’s place would have been warranted in believing that Knight had committed the crime of misdemeanor assault. Florida law defines misdemeanor assault as “an intentional, unlawful threat by word or act to do violence to the person of another, coupled with an apparent ability to do so, and in doing some act which creates a well-founded fear in such other person that such violence is imminent.” <span class="citation no-link">Fla. Stat. Ann. § 784.011</span>.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b1223-5">
  By the time he finished talking with Knight’s ex-girlfriend, Officer Jacobson had heard enough to warrant a prudent person in believing that Knight had intentionally threatened to do violence to her and that Knight, who lived next door to her, had an apparent ability to carry out the threat, and in making it had created a well-founded fear in her that violence was imminent. Knight was never convicted or even prosecuted for that crime or any other stemming from the arrest, but that does not matter.
  <em>
   See Baker v. McCollan,
  </em>
  <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#145" aria-description="Citation for case: Baker v. McCollan">443 U.S. 137, 145</a></span>, <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#2695" aria-description="Citation for case: Baker v. McCollan">99 S.Ct. 2689, 2695</a></span>, <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/" aria-description="Citation for case: Baker v. McCollan">61 L.Ed.2d 433</a></span> (1979) (“The Constitution does not guarantee that only the guilty will be arrested. If it did, § 1983 would provide a cause of action for every defendant acquitted—indeed, for every suspect released.”);
  <em>
   Von Stein v. Brescher,
  </em>
  <span class="citation" data-id="542392"><a href="/opinion/542392/charles-h-von-stein-v-george-a-brescher/" aria-description="Citation for case: Charles H. Von Stein v. George A. Brescher">904 F.2d 572</a></span>, 578 n. 9 (11th Cir.1990) (“‘Probable cause’ defines a radically different standard than ‘beyond a reasonable doubt,’ and while an arrest must stand on more than suspicion, the arresting officer need not have in hand evidence sufficient to obtain a conviction.”);
  <em>
   United States v. Pantoja-Soto,
  </em>
  <span class="citation" data-id="9472437"><a href="/opinion/439177/united-states-v-fulgencio-pantoja-soto-raul-pal-sali-nelio-a-nunez-and/" aria-description="Citation for case: United States v. Fulgencio Pantoja-Soto, Raul Pal-Sali,...">739 F.2d 1520</a></span>, 1524 n. 7 (11th Cir.1984) (same). When Knight was arrested in the early morning hours of July 25, 1996, there was probable cause to believe he had committed the crime of misdemean- or assault.
 </p>
<p id="b1223-8">
  Knight’s principal argument to the contrary maintains that under Florida law an assault cannot occur if the threat is made over the telephone. For that proposition he relies on
  <em>
   Trowell v. Meads,
  </em>
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/" aria-description="Citation for case: Trowell v. Meads">618 So.2d 351</a></span> (Fla. 1st DCA 1993), which is readily distinguishable. In
  <em>
   <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/" aria-description="Citation for case: Trowell v. Meads">Trowell</a></span>
  </em>
  the plaintiff sought a permanent restraining order against her former husband, contending that he had assaulted her by making threats during a telephone conversation while he was involuntarily confined in a Florida state mental hospital.
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/#351" aria-description="Citation for case: Trowell v. Meads"><em>
   Id.
  </em>
  at 351</a></span>. In a two-paragraph opinion, the district court of appeals concluded that under those facts there had been no assault.
  <span class="citation" data-id="1802074"><a href="/opinion/1802074/trowell-v-meads/#351" aria-description="Citation for case: Trowell v. Meads"><em>
   Id.
  </em>
  at 351-52</a></span>. The facts in this case are different. Unlike the former husband in
  <em>
   Tro-well,
  </em>
  Knight was not involuntarily confined and therefore without any apparent ability to inflict violence and create a well-founded fear that the threatened violence was imminent. Instead, Knight was free and unconfined and conveniently located right next door to the target of his threat. Knight’s contention that Officer Jacobson had no probable cause to arrest him is unfounded.
 </p>
<p id="b1223-9">
  Knight also contends that his arrest, even if supported by probable cause, violated the Fourth Amendment because it was not done in accord with state law.
  <span citation-index="1" class="star-pagination" label="1276"> 
   *1276
   </span>
  With an exception or two not relevant here, Florida law authorizes warrantless arrests for misdemeanors only if they are committed in the officer’s presence. <span class="citation no-link">Fla. Stat. Ann. § 901.15</span>(1). The misdemeanor assault in this case was not. From those two premises Knight concludes that his arrest violated the Fourth Amendment. However, there is another premise essential to that conclusion which is not correct, and it is the proposition that an arrest supported by probable cause in circumstances where arrest is not permitted under state law violates the Fourth Amendment.
 </p>
<p id="b1224-4">
  Section 1983 does not create a remedy for every wrong committed under the color of state law, but only for those that deprive a plaintiff of a federal right.
  <em>
   See Paul v. Davis,
  </em>
  <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#698" aria-description="Citation for case: Paul v. Davis">424 U.S. 693, 698-99</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#1159" aria-description="Citation for case: Paul v. Davis">96 S.Ct. 1155, 1159</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">47 L.Ed.2d 405</a></span> (1976). There is no federal right not to be arrested in violation of state law.
  <em>
   See Pyles v. Raisor,
  </em>
  <span class="citation" data-id="9488345"><a href="/opinion/700474/teresa-a-pyles-v-robert-s-raisor-ray-l-sabbatine/#1215" aria-description="Citation for case: Teresa A. Pyles v. Robert S. Raisor, Ray L. Sabbatine">60 F.3d 1211, 1215</a></span> (6th Cir.1995) (holding that federal law, not state law, determines the validity of arrests under the Fourth Amendment);
  <em>
   Fields v. City of South Houston,
  </em>
  922 F.2d at 1183, 1189 (5th Cir.1991) (same);
  <em>
   Barry v. Fowler,
  </em>
  902 F.2d at 770, 772 (9th Cir.1990) (same);
  <em>
   McKinney v. George,
  </em>
  <span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d 1183, 1188</a></span> (7th Cir.1984) (same);
  <em>
   Street v. Surdyka,
  </em>
  <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/#370" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d 368, 370-73</a></span> (4th Cir.1974) (same). While the violation of state law may (or may not) give rise to a state tort claim, it is not enough by itself to support a claim under section 1983.
  <em>
   See Barry,
  </em>
  902 F.2d at 773 (“While Barry may have a remedy under state law [for the warrantless arrest], she has faded to allege a federal constitutional or federal statutory violation”);
  <em>
   Diamond v. Marland,
  </em>
  <span class="citation" data-id="1416667"><a href="/opinion/1416667/diamond-v-marland/#439" aria-description="Citation for case: Diamond v. Marland">395 F.Supp. 432, 439</a></span> (S.D.Ga.1976) (“Even if a police officer violates a state arrest statute, he would not be hable under [§ 1983] unless he also violated federal constitutional law governing warrantless arrests.”);
  <em>
   see also Paul v. Davis,
  </em>
  <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#699" aria-description="Citation for case: Paul v. Davis">424 U.S. at 699</a></span>, <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#1159" aria-description="Citation for case: Paul v. Davis">96 S.Ct. at 1159</a></span> (rejecting the argument that “every legally cognizable injury which may have been inflicted by a state official acting ‘under color of law’ establishes] a violation of the Fourteenth Amendment”);
  <em>
   Lovins v. Lee,
  </em>
  <span class="citation" data-id="70285"><a href="/opinion/70285/lovins-v-lee/" aria-description="Citation for case: Lovins v. Lee">53 F.3d 1208</a></span>, 1210 — 1211 (11th Cir.1995) (holding that while the plaintiff may have a claim under state law against defendants because they acted contrary to state law in releasing an inmate who harmed her, that violation of state law did not give her a federal constitutional claim).
 </p>
<p id="b1224-7">
  The only authority Knight cites in support of his contention that violation of state law governing arrests automatically contravenes the Fourth Amendment is a Supreme Court case that applied state arrest law to determine the validity of an arrest for a federal offense when there was no federal statute governing the situation.
  <em>
   See Johnson v. United States,
  </em>
  <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U.S. 10</a></span>, 15 n. 5, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#370" aria-description="Citation for case: Johnson v. United States">68 S.Ct. 367, 370</a></span>, <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">92 L.Ed. 436</a></span> (1948);
  <em>
   see also United States v. Di Re,
  </em>
  <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#589" aria-description="Citation for case: United States v. Di Re">332 U.S. 581, 589</a></span>, <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#226" aria-description="Citation for case: United States v. Di Re">68 S.Ct. 222, 226</a></span>, <span class="citation no-link">92 L.Ed. 210</span> (1948). Borrowing state arrest procedure standards in those circumstances is a different matter from holding that those state law standards define constitutional mínimums. As the Fourth Circuit concluded: “The use of state law in such cases seems clearly to be based on non-constitutional considerations.”
  <em>
   Street,
  </em>
  <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d at 372</a></span> n. 7.
  <em>
   See also
  </em>
  3 Wayne R. La Fave, Search and Seizure § 5.1(b), at 22 (3d ed,1996)(same). We reject the notion that the Florida law procedures governing warrantless arrests are written into the federal Constitution.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b1225-3">
<span citation-index="1" class="star-pagination" label="1277"> 
   *1277
   </span>
  Knight’s final contention is that his arrest violated the Fourth Amendment as explicated in
  <em>
   Payton v. New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. 573, 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. 1371, 1382</a></span> (1980), which held that a warrantless arrest inside the home of a suspect is presumptively unreasonable unless exigent circumstances justify the intrusion. This part of Knight’s case founders on the facts, because Knight was not arrested inside his home, but just outside the door of it after he stepped out as instructed by Officer Jacobson.
 </p>
<p id="b1225-4">
  The rule of
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  is that there is “a firm line at the entrance to the house,” and absent exigent circumstances “that threshold may not reasonably be crossed without a warrant.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U.S. at 590</a></span>, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#1382" aria-description="Citation for case: Payton v. New York">100 S.Ct. at 1382</a></span>. Officer Jacobson never crossed that threshold or went over the line at the entrance to the house. As Knight himself testified in deposition: “There was a knock on my door, I came to the door, and Officer Jacobson said, “What are you doing?’ I said, T am in here, can I help you?’ He told me to step outside; I stepped outside; he walked around me a full circle and he told me to put my hands on the car ... And then he handcuffed me. And then he put me in the car.”
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b1225-7">
<em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  keeps the officer’s body outside the threshold, not his voice. It does not prevent a law enforcement officer from telling a suspect to step outside his home and then arresting him without a warrant. In that situation, the officer never crosses “the firm line at the entrance to the house” which is where
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  drew the line.
  <em>
   See United States v. Berkowitz,
  </em>
  <span class="citation" data-id="9481419"><a href="/opinion/557342/united-states-v-marvin-berkowitz/#1386" aria-description="Citation for case: United States v. Marvin Berkowitz">927 F.2d 1376, 1386</a></span> (7th Cir.1991)
  <em>
   (Payton
  </em>
  prohibits only a warrantless
  <em>
   entry
  </em>
  into the
  <em>
   home, “not
  </em>
  a policeman’s use of his voice to convey a message of arrest from outside the home.” (emphasis in original)).
  <em>
   See also United States v. Carrion,
  </em>
  <span class="citation" data-id="482020"><a href="/opinion/482020/united-states-v-anthony-nicholas-carrion-and-fred-solmor/#1128" aria-description="Citation for case: United States v. Anthony Nicholas Carrion and Fred Solmor">809 F.2d 1120, 1128</a></span> (5th Cir.1987) (arrest of suspect in doorway of home is reasonable and not contrary to Payton);
  <em>
   McKinney v. George,
  </em>
  <span class="citation" data-id="430916"><a href="/opinion/430916/raymond-lee-mckinney-v-velma-george/#1188" aria-description="Citation for case: Raymond Lee McKinney v. Velma George">726 F.2d 1183, 1188</a></span> (7th Cir.1984) (arrest of suspect who opened the door in response to officers’ knocks and who was arrested outside his home is reasonable and not contrary to
  <em>
   Payton); United States v. Whitten,
  </em>
  <span class="citation" data-id="418069"><a href="/opinion/418069/united-states-v-kenneth-joe-whitten-john-elmer-gaiefsky-jack-wayne-gish/#1015" aria-description="Citation for case: United States v. Kenneth Joe Whitten, John Elmer...">706 F.2d 1000, 1015</a></span> (9th Cir.1983) (doorway is
  <span citation-index="1" class="star-pagination" label="1278"> 
   *1278
   </span>
  a public place not subject to
  <em>
   <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
  </em>
  restriction);
  <em>
   United States v. Botero,
  </em>
  <span class="citation" data-id="362276"><a href="/opinion/362276/united-states-v-diego-botero-united-states-of-america-v-robert-dennis/#432" aria-description="Citation for case: United States v. Diego Botero, United States of America...">589 F.2d 430, 432</a></span> (9th Cir.1978) (arrest of suspect in doorway after the suspect answers the door is reasonable).
  <em>
   See generally
  </em>
  3 Wayne R. La Fave, Search and Seizure § 6.1(e), at 254-263 (3d ed.1996).
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b1226-4">
  The order of the district court denying .Officer Jacobson’s motion for summary judgment based on qualified immunity is REVERSED, and the case is REMANDED with directions that summary judgment be entered for him on that basis.
 </p>





<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b1222-5">
   . Knight says that the arrest involved in this case is just one of four warrantless arrests that represent a pattern of harassment by the City of Miami, Jacobson, and another defendant in this lawsuit. We are concerned only with the arrest that occurred on June 25, 1996, and with the issues arising from it as they relate to Officer Jacobson, the only defendant before us in this appeal.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b1223-6">
<em>
    .
   </em>
   Knight contends that he was arrested for misdemeanor assault, while Officer Jacobson says the arrest was for the crime of domestic violence. We need not resolve that dispute, because Jacobson prevails even under Knight’s theory, and it is irrelevant which crime he thought he was arresting Knight for at the time.
   <em>
    See Lee v. Ferraro,
   </em>
   <span class="citation" data-id="75789"><a href="/opinion/75789/kim-d-lee-v-luis-ferraro/#1196" aria-description="Citation for case: Kim D. Lee v. Luis Ferraro">284 F.3d 1188, 1196</a></span> (11th Cir.) C'[W]hen an officer makes an arrest, which is properly supported by probable cause to arrest lor a certain offense, neither his subjective reliance on an offense for which no probable cause exists nor his verbal announcement of the wrong offense vitiates the arrest.” (internal marks omitted) (quoting
   <em>
    United States v. Saunders,
   </em>
   <span class="citation" data-id="310037"><a href="/opinion/310037/united-states-v-mansfield-saunders/#7" aria-description="Citation for case: United States v. Mansfield Saunders">476 F.2d 5, 7</a></span> (5th Cir.1973)))
   <em>
    reh’g and reh’g en banc denied,
   </em>
   <span class="citation no-link">37 Fed.Appx. 503</span> (11th Cir. May 13, 2002) (No. 00-16054).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b1224-5">
   . About warrantless arrests for misdemeanors, we decide only the issue framed by Knight's argument, which is that violation of a state law restriction on such arrests violates the Fourth Amendment because state law has been contravened. Knight has not argued, and so we do not decide, whether an arrest
   <span citation-index="1" class="star-pagination" label="1277"> 
    *1277
    </span>
   for a misdemeanor not committed in the officer’s presence violates the Fourth Amendment itself irrespective of state law. We note in passing, however, that every circuit that has addressed the issue has held that the Fourth Amendment does not include an in-the-presence requirement for warrantless misdemeanor arrests.
   <em>
    See Pyles v. Raisor,
   </em>
   <span class="citation" data-id="9488345"><a href="/opinion/700474/teresa-a-pyles-v-robert-s-raisor-ray-l-sabbatine/#1215" aria-description="Citation for case: Teresa A. Pyles v. Robert S. Raisor, Ray L. Sabbatine">60 F.3d 1211, 1215</a></span> (6th Cir.1995) (“Pyles' rights under Kentucky law, including her right as an alleged misdemeanant to be arrested only when the misdemeanor is committed in the presence of the arresting officer, are not grounded in the federal Constitution and will not support a § 1983 claim.");
   <em>
    Fields v. City of South Houston,
   </em>
   922 F.2d at 1183, 1189 (5th Cir.1991) (“The United States Constitution does not require a warrant for misdemeanors not occurring in the presence of the arresting officer.”);
   <em>
    Barry v. Fowler,
   </em>
   902 F.2d at 770, 772 (9th Cir.1990) ("The requirement that a misdemeanor must have occurred in the officer's presence to justify a warrantless arrest is not grounded in the Fourth Amendment.”);
   <em>
    Street v. Surdyka,
   </em>
   <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/#372" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">492 F.2d 368, 372</a></span> (4th Cir.1974) ("We do not think the Fourth Amendment should now be interpreted to prohibit warrantless arrests for misdemeanors committed outside an officer’s presence.”).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b1225-9">
   . Knight did say that Officer Jacobson eventually went inside the apartment, but he made clear that happened after the arrest had been made and was done for the purpose of retrieving Knight’s identification. Knight testified: "Then Jacobson—the other one, his partner stayed in there [at his ex-girlfriend’s apartment] and then because he was asking me do I have ID and I told him my ID was inside on my dresser. He went in, he got my <span class="citation" data-id="317151"><a href="/opinion/317151/george-b-street-v-officer-leo-surdyka-baltimore-city-police-department/" aria-description="Citation for case: George B. Street v. Officer Leo Surdyka, Baltimore City...">ID.</a></span> Or my driver’s license.” At oral argument, Knight again conceded that no officer stepped inside the home until after he had been arrested. Knight has not argued that Officer Jacobson's entry into the apartment after the arrest had been made and for the purpose of retrieving Knight's identification violated the
   <em>
    <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>
   </em>
   rule.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b1226-13">
   . Some courts have held that when the suspect leaves his home because of coercive tactics by the police, the arrest is illegal.
   <em>
    See, e.g., United States v. Morgan,
   </em>
   <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1166" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1166-67</a></span> (6th Cir.1984) (holding that a war-rantless arrest made after the suspect stepped outside the home was unconstitutional because of the coercive tactics used by the police, which included having nine officers surround the home, flooding the home with spotlights, and summoning the suspect through a bullhorn). There were no such tactics in this case, just a simple direction by one officer that Knight step outside.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Knowles v. Iowa.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Knowles v. Iowa"
type: case
citation: "525 U.S. 113 (1998)"
parallel_cite: "119 S. Ct. 484; 142 L. Ed. 2d 492"
neutral_cite: 1998 U.S. LEXIS 8068
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1998
date_decided: 1998-12-08
docket: 97-7597
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1998-12-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Knowles v. Iowa
  varies_by_point: false
  scope_note: "Controlling: there is no 'search incident to citation' — issuing a citation, without a custodial arrest, does not authorize a full search."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118250/knowles-v-iowa/"
  cluster_id: 118250
  opinion_id: 118250
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Limiting"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Robinson]]", "[[Pennsylvania v. Mimms]]", "[[Maryland v. Wilson]]", "[[Virginia v. Moore]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "traffic-stops", "citation"]
holding: "Issuing a traffic citation, without a custodial arrest, does not authorize a search incident to arrest; neither the officer-safety nor the evidence-preservation rationale supports a full search where the driver is merely cited."
lake:
  record_id: Knowles v. Iowa
  status: verified
  projected_at: 2026-07-09
---

# Knowles v. Iowa

*525 U.S. 113 (1998)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An Iowa officer stopped Knowles for driving 43 mph in a 25 mph zone and issued him a citation rather than arresting him, although Iowa law authorized either course. Relying on an Iowa statute the state courts read to permit a "search incident to citation," the officer then conducted a full search of the car and found marijuana and a pipe under the driver's seat. Knowles was arrested on drug charges. At the [[Common Legal Terms#suppression-hearing|suppression hearing]] the officer conceded he had neither Knowles' consent nor probable cause to search.

## Issue
Does the Fourth Amendment permit an officer to conduct a full search of a vehicle incident to the issuance of a traffic citation, where the driver has not been placed under custodial arrest?

## Rule
No. The question "is whether such a procedure authorizes the officer, consistently with the Fourth Amendment, to conduct a full search of the car. We answer this question 'no.' " — 525 U.S. at 113. ^pin-113

The two rationales for the search-incident exception — officer safety and the preservation of evidence — do not support the search: "neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case." — [*Id.* at 116–17](https://www.courtlistener.com/opinion/118250/knowles-v-iowa/#:~:text=neither%20of%20these%20underlying%20rationales). ^pin-116

A traffic stop's officer-safety concern is lower than a custodial arrest's and is met by lesser measures (ordering occupants out, a *[[Terry v. Ohio|Terry]]* frisk on reasonable suspicion, a *[[Michigan v. Long]]* protective search). And as to evidence, "[o]nce Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained." — *Id.* at 118. ^pin-118

The Court refused to extend *[[United States v. Robinson|Robinson]]*'s bright-line full-search rule "to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so." — [*Id.* at 118–19](https://www.courtlistener.com/opinion/118250/knowles-v-iowa/#:~:text=to%20a%20situation%20where%20the). ^pin-119

## Application
Knowles was cited, not arrested, and the officer had neither consent nor probable cause. Because a brief traffic stop poses a lesser safety risk — addressable by ordering the driver out, a frisk on reasonable suspicion, or a protective vehicle search — and because issuing the speeding citation had already secured all evidence of that offense, neither search-incident rationale applied. The "search incident to citation" had no constitutional basis.

## Conclusion
The full search of the car was unconstitutional; the judgment of the Iowa Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Knowles* remains controlling: there is no "search incident to citation." It cabins [[United States v. Robinson]]'s [[Common Legal Terms#bright-line-rule|bright-line rule]] to actual custodial arrests and is the contrast point in [[Virginia v. Moore]] (full search permitted because Moore was *arrested*). No negative treatment.

## Appears on
- [[SIA Persons]] — *Limiting*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *Knowles v. Iowa*, 525 U.S. 113 (1998) — https://www.courtlistener.com/opinion/118250/knowles-v-iowa/ — pinpoints: 113, 116–117, 118, 119.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9025b71ea73f0abd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Knowles v. Iowa"}, "payload": {"all": [{"cite": "525 U.S. 113", "page": "113", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "525"}, {"cite": "119 S. Ct. 484", "page": "484", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "142 L. Ed. 2d 492", "page": "492", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}, {"cite": "1998 U.S. LEXIS 8068", "page": "8068", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1998"}], "display": "525 U.S. 113", "official": {"cite": "525 U.S. 113", "page": "113", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "525"}, "official_selection_present": true, "record_id": "Knowles v. Iowa"}}
{"assertion_id": "23939fc1d2671998", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-118", "record_id": "Knowles v. Iowa"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-118", "pinpoint_status": "slip-only", "quote": "[o]nce Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained.", "quote_fidelity": "mismatch", "record_id": "Knowles v. Iowa", "star_marker": null}}
{"assertion_id": "72618aadd8fe3157", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-116", "record_id": "Knowles v. Iowa"}, "payload": {"fragment": "#:~:text=neither%20of%20these%20underlying%20rationales", "page": null, "pin_id": "pin-116", "pinpoint_status": "star-verified", "quote": "neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case.", "quote_fidelity": "matched", "record_id": "Knowles v. Iowa", "star_marker": "117"}}
{"assertion_id": "c1d5c824326e1e58", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-113", "record_id": "Knowles v. Iowa"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-113", "pinpoint_status": "slip-only", "quote": "the officer then conducted a full search of the car and found marijuana and a pipe under the driver's seat. Knowles was arrested on drug charges. At the suppression hearing the officer conceded he had neither Knowles' consent nor probable cause to search. ## Issue Does the Fourth Amendment permit an officer to conduct a full search of a vehicle incident to the issuance of a traffic citation, where the driver has not been placed under custodial arrest? ## Rule No. The question", "quote_fidelity": "mismatch", "record_id": "Knowles v. Iowa", "star_marker": null}}
{"assertion_id": "e301abe2e560c2dc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-119", "record_id": "Knowles v. Iowa"}, "payload": {"fragment": "#:~:text=to%20a%20situation%20where%20the", "page": null, "pin_id": "pin-119", "pinpoint_status": "star-verified", "quote": "to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so.", "quote_fidelity": "matched", "record_id": "Knowles v. Iowa", "star_marker": "119"}}
{"assertion_id": "159ddf3acda7e4f4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Knowles v. Iowa"}, "payload": {"as_of_content": "1998-12-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Knowles v. Iowa", "scope_note": "Controlling: there is no 'search incident to citation' — issuing a citation, without a custodial arrest, does not authorize a full search.", "varies_by_point": false}}
```

### lake record — Knowles v. Iowa

```json
{
  "schema_version": "s2.v1",
  "record_id": "Knowles v. Iowa",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Knowles v. Iowa",
    "case_name_short": "Knowles",
    "case_name_full": "Knowles v. Iowa",
    "input_case_name": "Knowles v. Iowa",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1998-12-08",
    "year": 1998,
    "docket": "97-7597",
    "cluster_id": 118250,
    "lead_opinion_id": 118250,
    "sibling_ids": [
      118250
    ],
    "absolute_url": "/opinion/118250/knowles-v-iowa/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9179844,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9179843,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9170706,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      },
      {
        "cluster_id": 9168391,
        "score": 20,
        "case_name": "Knowles v. Iowa"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "525 U.S. 113",
      "volume": "525",
      "reporter": "U.S.",
      "page": "113",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 484",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 492",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1998 U.S. LEXIS 8068",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "8068",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "525 U.S. 113",
        "volume": "525",
        "reporter": "U.S.",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 484",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 L. Ed. 2d 492",
        "volume": "142",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1998 U.S. LEXIS 8068",
        "volume": "1998",
        "reporter": "U.S. LEXIS",
        "page": "8068",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "525 U.S. 113",
    "official_selection": {
      "court_class": "scotus",
      "selected": "525 U.S. 113",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "the officer then conducted a full search of the car and found marijuana and a pipe under the driver's seat. Knowles was arrested on drug charges. At the suppression hearing the officer conceded he had neither Knowles' consent nor probable cause to search. ## Issue Does the Fourth Amendment permit an officer to conduct a full search of a vehicle incident to the issuance of a traffic citation, where the driver has not been placed under custodial arrest? ## Rule No. The question",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-116",
      "page": null,
      "quote": "neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case.",
      "star_marker": "117",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 7271,
      "fragment": "#:~:text=neither%20of%20these%20underlying%20rationales",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-118",
      "page": null,
      "quote": "[o]nce Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-119",
      "page": null,
      "quote": "to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so.",
      "star_marker": "119",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14092,
      "fragment": "#:~:text=to%20a%20situation%20where%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1998-12-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Knowles v. Iowa",
    "varies_by_point": false,
    "scope_note": "Controlling: there is no 'search incident to citation' \u2014 issuing a citation, without a custodial arrest, does not authorize a full search.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Solorio",
          "cluster_id": 10133534,
          "cite": [
            "304 Or. App. 666",
            "468 P.3d 522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Evans",
          "cluster_id": 2802206,
          "cite": [
            "786 F.3d 779",
            "15 Cal. Daily Op. Serv. 4997",
            "2015 U.S. App. LEXIS 8293",
            "2015 WL 2385010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William A. Nash, Jr. and David Lewis",
          "cluster_id": 2736697,
          "cite": [
            "100 A.3d 157",
            "2014 D.C. App. LEXIS 393"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Danielle Kelly v. State of Indiana",
          "cluster_id": 2644345,
          "cite": [
            "997 N.E.2d 1045",
            "2013 WL 6122278",
            "2013 Ind. LEXIS 904"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 2487584,
          "cite": [
            "79 So. 3d 1013",
            "2012 La. LEXIS 268",
            "2012 WL 415483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Samuel Cendejas Fernandez v. State",
          "cluster_id": 3130718,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fernandez v. State",
          "cluster_id": 1748290,
          "cite": [
            "306 S.W.3d 354",
            "2010 Tex. App. LEXIS 1039",
            "2010 WL 520810"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Triston Lee Harris",
          "cluster_id": 1052778,
          "cite": [
            "280 S.W.3d 832",
            "2008 Tenn. Crim. App. LEXIS 112"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane1_negative"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. United States",
          "cluster_id": 2795278,
          "cite": [
            "575 U.S. 348",
            "135 S. Ct. 1609",
            "191 L. Ed. 2d 492",
            "2015 U.S. LEXIS 2807",
            "83 U.S.L.W. 4241",
            "25 Fla. L. Weekly Fed. S 191"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Bennett v. City of Eastpointe",
          "cluster_id": 790530,
          "cite": [
            "410 F.3d 810",
            "2005 U.S. App. LEXIS 10587",
            "2005 WL 1384366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Jay Hill and Malcolm Scott Hill",
          "cluster_id": 766585,
          "cite": [
            "195 F.3d 258",
            "1999 U.S. App. LEXIS 24597",
            "1999 WL 781810"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Menotti v. City of Seattle",
          "cluster_id": 3032002,
          "cite": [
            "409 F.3d 1113",
            "2005 WL 1300994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eleuterio Lopez-Moreno, Also Known as Eleuterio Lopez",
          "cluster_id": 791593,
          "cite": [
            "420 F.3d 420",
            "2005 U.S. App. LEXIS 16564",
            "2005 WL 1864257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 1195377,
          "cite": [
            "997 P.2d 13",
            "93 Haw. 87",
            "2000 Haw. LEXIS 97"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
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
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2087727,
          "cite": [
            "745 A.2d 856",
            "1999 Del. LEXIS 445",
            "1999 WL 1259008"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. Buono",
          "cluster_id": 145221,
          "cite": [
            "176 L. Ed. 2d 634",
            "130 S. Ct. 1803",
            "559 U.S. 700",
            "2010 U.S. LEXIS 3674"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Floyd v. City of Crystal Springs",
          "cluster_id": 1711298,
          "cite": [
            "749 So. 2d 110",
            "1999 WL 1063627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. City of Buena Park",
          "cluster_id": 1227729,
          "cite": [
            "560 F.3d 1012",
            "2009 U.S. App. LEXIS 6394",
            "2009 WL 764568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. State",
          "cluster_id": 853407,
          "cite": [
            "745 N.E.2d 775",
            "2001 Ind. LEXIS 300",
            "2001 WL 371941"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Knowles v. Iowa:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118250) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMyNjE3NjAwMDAwJnM9NzkyNTU2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118250%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118250)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAmcz0yNzc4NzcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118250%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118250)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 0,
        "triage_snippet_classified": 18
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118250)",
    "indexed_citing_opinions": 490,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118250,
        "count": 490,
        "count_source": "search"
      }
    ],
    "citation_count": 801,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/knowles-v-iowa.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4NzI1MjImcz03ODU1MzIyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118250%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118250,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1734862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1833134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 1877452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118250,
        "cited_id": 2075076,
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
    "date_created": "2026-07-05T10:19:41Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:24:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:21:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Knowles v. Iowa

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b298-7">
  CHIEF Justice Rehnquist
 </author>
<p id="A-N9">
  delivered the opinion of the Court.
 </p>
<p id="b298-8">
  An Iowa police officer stopped petitioner Knowles for speeding, but issued him a citation rather than arresting him. The question presented is whether such a procedure authorizes the officer, consistently with the Fourth Amendment, to conduct a foil search of the car. We answer this question "no.”
 </p>
<p id="b298-9">
  Knowles was stopped in Newton, Iowa, after having been clocked driving 43 miles per hour on a road where the speed limit was 25 miles per hour. The police officer issued a citation to Knowles, although under Iowa law he might have arrested him. The officer then conducted a foil search of the car, and under the driver’s seat he found a bag of marijuana and a “pot pipe.” Knowles was then arrested and charged with violation of state laws dealing with controlled substances.
 </p>
<p id="b298-10">
  Before trial, Knowles moved to suppress the evidence so obtained. He argued that the search could not be sustained under the "search incident to arrest” exception recognized in
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), because he had not been placed under arrest.. At the hearing on the motion to suppress, the police officer conceded that he had
  <span citation-index="1" class="star-pagination" label="115"> 
   *115
   </span>
  neither Knowles’ consent nor probable cause to conduct the search. He relied on Iowa law dealing with such searches.
 </p>
<p id="b299-5">
  <span class="citation no-link">Iowa Code Ann. § 321.485</span>(l)(a) (West 1997) provides that Iowa peace officers having cause to believe that a person has violated any traffic or motor vehicle equipment law may arrest the person and immediately take the person before a magistrate. Iowa law also authorizes the far more usual practice of issuing a citation in lieu of arrest or in lieu of continued custody after an initial arrest.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  See <span class="citation no-link">Iowa Code Ann. §805.1</span>(1) (West Supp. 1997). Section 805.1(4) provides that the issuance of a citation in lieu of an arrest “does not affect the officer’s authority to conduct an otherwise lawful search.” The Iowa Supreme Court has interpreted this provision as providing authority to officers to conduct a full-blown search of an automobile and driver in those cases where police elect not to make a custodial arrest and instead issue a citation — that is, a search incident to citation. See
  <em>
   State
  </em>
  v.
  <em>
   Meyer,
  </em>
  <span class="citation" data-id="1734862"><a href="/opinion/1734862/state-v-meyer/#879" aria-description="Citation for case: State v. Meyer">543 N. W. 2d 876, 879</a></span> (1996);
  <em>
   State
  </em>
  v.
  <em>
   Becker,
  </em>
  <span class="citation" data-id="2075076"><a href="/opinion/2075076/state-v-becker/#607" aria-description="Citation for case: State v. Becker">458 N. W. 2d 604, 607</a></span> (1990).
 </p>
<p id="b299-6">
  Based on this authority, the trial court denied the motion to suppress and found Knowles guilty. The Supreme Court of Iowa, sitting en bane, affirmed by a divided vote. <span class="citation" data-id="9687529"><a href="/opinion/1833134/state-v-knowles/" aria-description="Citation for case: State v. Knowles">569 N. W. 2d 601</a></span> (1997). Relying on its earlier opinion in
  <em>
   State
  </em>
  v.
  <em>
   Doran,
  </em>
  <span class="citation" data-id="9691123"><a href="/opinion/1877452/state-v-doran/" aria-description="Citation for case: State v. Doran">563 N. W. 2d 620</a></span> (1997), the Iowa Supreme Court upheld the constitutionality of the search under a bright-line “search incident to citation” exception to the Fourth Amendment’s warrant requirement, reasoning that so long as the
  <span citation-index="1" class="star-pagination" label="116"> 
   *116
   </span>
  arresting officer had probable cause to make a custodial arrest, there need not in fact have been a custodial arrest. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./523/1019/">523 U. S. 1019</a></span> (1998), and we now reverse.
 </p>
<p id="b300-5">
  The State contends that Knowles has challenged Iowa Code’s §805.1(4) only “on its face” and not “as applied,” in which case, the argument continues, his challenge would run afoul of
  <em>
   Sibron
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968). But in his motion to suppress, Knowles argued that “[bjeeause the officer had no probable cause and no search warrant, and the search cannot otherwise be justified under the Fourth Amendment, the search of the car was unconstitutional.” App. 7. Knowles did not argue below, and does not argue here, that the statute could never be lawfully applied. The question we therefore address is whether the search at issue, authorized as it was by state law, nonetheless violates the Fourth Amendment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b300-6">
  In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra,</a></span>
  </em>
  we noted the two historical rationales for the “search incident to arrest” exception: (1) the need to disarm the suspect in order to take him into custody, and (2) the need to preserve evidence for later use at trial. <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S., at 234</a></span>. See also
  <em>
   United States
  </em>
  v.
  <em>
   Edwards,
  </em>
  <span class="citation" data-id="9425658"><a href="/opinion/108995/united-states-v-edwards/#802" aria-description="Citation for case: United States v. Edwards">415 U. S. 800, 802-803</a></span> (1974);
  <em>
   Chimel
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762-763</a></span> (1969);
  <em>
   Preston
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964);
  <span citation-index="1" class="star-pagination" label="117"> 
   *117
   </span>
<em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1926);
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914). But neither of these underlying rationales for the search incident to arrest exception is sufficient to justify the search in the present case.
 </p>
<p id="b301-5">
  We have recognized that the first rationale — officer safety — is “‘both legitimate and weighty,’”
  <em>
   Maryland
  </em>
  v.
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#412" aria-description="Citation for case: Maryland v. Wilson">519 U. S. 408, 412</a></span> (1997) (quoting
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 110</a></span> (1977)
  <em>
   (per curiam)).
  </em>
  The threat to officer safety from issuing a traffic citation, however, is a good deal less than in the ease of a custodial arrest. In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>,
  </em>
  we stated that a custodial arrest involves “danger to an officer” because of “the extended exposure which follows the taking of a suspect into custody and transporting him to the police station.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S., at 234-235</a></span>. We recognized that “[t]he danger to the police officer flows from the faet of the arrest, and its attendant proximity, stress, and uncertainty, and not from the grounds for arrest.”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson"><em>
   Id.,
  </em>
  at 234, n. 5</a></span>. A routine traffic stop, on the other hand,' is a relatively brief encounter and “is more analogous to a so-called
  <em>
   ‘Terry
  </em>
  stop’ . . . than to a formal arrest.”
  <em>
   Berkemer
  </em>
  v.
  <em>
   McCarty,
  </em>
  <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984). See also
  <em>
   Cupp
  </em>
  v.
  <em>
   Murphy,
  </em>
  <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#296" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 296</a></span> (1973) (“Where there is no formal arrest... a person might well be less hostile to the police and less likely to take conspicuous, immediate steps to destroy incriminating evidence”).
 </p>
<p id="b301-6">
  This is not to say that the concern for officer safety is absent in the ease of a routine traffic stop. It plainly is not. See
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><em>
   Mimms, supra,
  </em>
  at 110</a></span>;
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#413" aria-description="Citation for case: Maryland v. Wilson"><em>
   Wilson, supra,
  </em>
  at 413-414</a></span>. But while the concern for officer safety in this context may justify the “minimal” additional intrusion of ordering a driver and passengers out of the car, it does not by itself justify the often considerably greater intrusion attending a full field-type search. Even without the search authority Iowa urges, officers have other, independent bases to search for weapons and protect themselves from danger. For example, they
  <span citation-index="1" class="star-pagination" label="118"> 
   *118
   </span>
  may order out of a vehicle both the driver,
  <em>
   Mimms, swpra,
  </em>
  at Ill, and any passengers,
  <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#414" aria-description="Citation for case: Maryland v. Wilson"><em>
   Wilson, supra,
  </em>
  at 414</a></span>; perform a “patdown” of a driver and any passengers upon reasonable suspicion that they may be armed and dangerous,
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); conduct a
  <em>
   “Terry
  </em>
  patdown” of the passenger compartment of a vehicle upon reasonable suspicion that an occupant is dangerous and may gain immediate control of a weapon,
  <em>
   Michigan
  </em>
  v.
  <em>
   Long,
  </em>
  <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049</a></span> (1983); and even conduct a full search of the passenger compartment, including any containers therein, pursuant to a custodial arrest,
  <em>
   New York
  </em>
  v.
  <em>
   Belton,
  </em>
  <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 460</a></span> (1981).
 </p>
<p id="b302-5">
  Nor has Iowa shown the second justification for the authority to search incident to arrest — the need to discover and preserve evidence. Once Knowles was stopped for speeding and issued a citation, all the evidence necessary to prosecute that offense had been obtained. No further evidence of excessive speed was going to be found either on the person of the offender or in the passenger compartment of the car.
 </p>
<p id="b302-6">
  Iowa nevertheless argues that a “search incident to citation” is justified because a suspect who is subject to a routine traffic stop may attempt to hide or destroy evidence related to his identity
  <em>
   (e. g.,
  </em>
  a driver’s license or vehicle registration), or destroy evidence of another, as yet undetected crime. As for the destruction of evidence relating to identity, if a police officer is not satisfied with the identification furnished by the driver, this may be a basis for arresting him rather than merely issuing a citation. As for destroying evidence of other crimes, the possibility that an officer would stumble onto evidence wholly unrelated to the speeding offense seems remote.
 </p>
<p id="b302-7">
  In
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>,
  </em>
  we held that the authority to conduct a full field search as incident to an arrest was a “bright-line rule,” which was based on the concern for officer safety and destruction or loss of evidence, but which did not depend in every case upon the existence of either concern. Here we
  <span citation-index="1" class="star-pagination" label="119"> 
   *119
   </span>
  are asked to extend that “bright-line rule” to a situation where the concern for officer safety is not present to the same extent and the concern for destruction or loss of evidence is not present at all. We decline to do so. The judgment of the- Supreme Court of Iowa is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b303-4">
<em>
   It is so ordered.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b299-7">
   Iowa law permits the issuance of a citation in lieu of arrest for most offenses for which an accused person would be "eligible for bail.” See <span class="citation no-link">Iowa Code Ann. §805.1</span>(1) (West Supp. 1997). In addition to traffic and motor vehicle equipment violations, this would permit the issuance of a citation in lieu of arrest for such serious felonies as second-degree burglary, §713.5 (West Supp. 1997), and first-degree theft, §714.2(1) (West 1993), both bailable offenses under Iowa law. See §811.1 (West Supp. 1997) (listing all nonbailable offenses). The practice in Iowa of permitting citation in lieu of arrest is consistent with law reform efforts. See 3 W. LaFave, Search and Seizure § 5.2(h), p. 99, and n. 151 (3d ed. 1996).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b300-7">
   Iowa also contends that Knowles’ challenge is precluded because he failed to seek review of a separate decision of the Iowa Supreme Court, which affirmed his conviction for possession of drug paraphernalia in violation of a city ordinance. That decision, Iowa argues, resulted from the same search at issue here, rejected the same Fourth Amendment challenge Knowles now makes, and, under principles of res judicata, bars his present challenge. Even if Knowles’ failure to seek certiorari review of this decision could preclude his present challenge, Iowa waived this argument by failing to raise it in its brief in opposition to the petition for certiorari. See this Court’s Rule 15.2;
   <em>
    Oklahoma City
   </em>
   v.
   <em>
    Tuttle,
   </em>
   <span class="citation" data-id="9430039"><a href="/opinion/111441/city-of-oklahoma-v-tuttle/#816" aria-description="Citation for case: City of Oklahoma v. Tuttle">471 U. S. 808, 816</a></span> (1985) (“Nonjurisdietional defects of this sort should be brought to our attention
   <em>
    no later
   </em>
   than in respondent’s brief in opposition to the petition for certiorari; if
   <em>
    not,
   </em>
   we consider it within our discretion to deem the defect waived”).
  </p>
</div></div></opinion>
```

---
