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

## GROUP: content/cases/Kirby v. Illinois.md  (`case`, 6 assertions)

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
{"assertion_id": "96cc328bb2ae1f12", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "406 U.S. 682 (1972)", "court": "U.S. Supreme Court", "neutral_cite": "1972 U.S. LEXIS 49", "official_citation_present": true, "parallel_cite": "92 S. Ct. 1877; 32 L. Ed. 2d 411", "title": "Kirby v. Illinois", "year": "1972"}}
{"assertion_id": "0b3cf626347363ae", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Anchor", "title": "Kirby v. Illinois"}}
{"assertion_id": "3128c507090f00c2", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny / Refinement", "title": "Kirby v. Illinois"}}
{"assertion_id": "3b97e9e9b9d991b0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment right to counsel attaches only at or after the initiation of adversary judicial criminal proceedings (formal charge,…", "title": "Kirby v. Illinois"}}
{"assertion_id": "2e9dab97d25e47df", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kirby v. Illinois"}}
{"assertion_id": "319114292dfbb479", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1972-06-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kirby v. Illinois", "field_i_validity": "good_law", "scope_note": "Plurality opinion; its attachment rule was subsequently adopted by a majority (e.g., Moore v. Illinois) and reaffirmed in Rothgery v. Gillespie County (2008).", "title": "Kirby v. Illinois", "varies_by_point": "false"}}
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

## GROUP: content/cases/Lozman v. City of Riviera Beach.md  (`case`, 5 assertions)

### content_page

```
---
title: Lozman v. City of Riviera Beach
type: case
citation: "585 U.S. 87 (2018)"
parallel_cite: "138 S. Ct. 1945; 201 L. Ed. 2d 342"
neutral_cite: 2018 U.S. LEXIS 3691
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-06-18
docket: No. 17-21
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
  opinion_url: "https://www.courtlistener.com/opinion/4508137/lozman-v-riviera-beach/"
  cluster_id: 4508137
  opinion_id: null
  identity_checked: true
lake:
  record_id: Lozman v. City of Riviera Beach
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Retaliatory Arrest]]"
    role: Anchor
related:
  - "[[Retaliatory Arrest]]"
  - "[[Nieves v. Bartlett]]"
tags:
  - case
  - first-amendment
  - retaliatory-arrest
  - probable-cause
  - section-1983
  - municipal-policy
holding: "Where a plaintiff alleges that a municipality arrested him pursuant to an official policy of retaliation, formed well before the arrest, in response to speech high in the hierarchy of First Amendment values, the existence of probable cause for the arrest does not bar his First Amendment retaliatory-arrest claim; the Court did not decide the elements of retaliatory-arrest claims in other contexts."
aliases:
  - Lozman v. City of Riviera Beach
  - "Lozman v. City of Riviera Beach (2018)"
  - Lozman v. Riviera Beach
---

# Lozman v. City of Riviera Beach

*585 U.S. 87 (2018)* (No. 17-21) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4508137 → lead opinion 4285390 (Kennedy, J.; 585 U.S. 87, decided June 18, 2018). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is the slip opinion (585 U.S. ___), so the pin is slip-style per S2 A3 — slip op. at 12 (the holding falls on slip page 12, before the "13" page header). S9 promotes. -->

## Background
Fane Lozman was an outspoken critic of the Riviera Beach, Florida city government: he had sued the City over open-meetings violations and repeatedly criticized officials in public. During the public-comment period of a City Council meeting, he refused to stop speaking and was arrested. Lozman alleged that, months earlier in a closed-door session, the City had formed an official policy to intimidate him in retaliation for his protected speech, and that his arrest carried out that policy. He conceded there was probable cause to arrest him. The Eleventh Circuit held that the existence of probable cause defeated his First Amendment retaliatory-arrest claim as a matter of law.

## Issue
Whether probable cause for an arrest bars a First Amendment retaliatory-arrest claim where the plaintiff alleges the arrest was made pursuant to an official municipal policy of retaliation.

## Rule
Deciding the case on a deliberately narrow ground, the Court held: "For these reasons, Lozman need not prove the absence of probable cause to maintain a claim of retaliatory arrest against the City." — slip op. at 12. ^pin-op12

## Application
The Court stressed how unusual Lozman's claim was: he alleged an *official municipal policy* of intimidation, premeditated and formed well before the arrest, directed at speech high in the hierarchy of First Amendment values (his petitioning and criticism of government), and supported by objective evidence able to survive summary judgment. In that limited class of cases the causation concerns that ordinarily attend retaliatory-arrest claims are diminished, and *Mt. Healthy* supplies the governing standard — so the mere existence of probable cause does not automatically defeat the claim. The Court expressly declined to define the elements of retaliatory-arrest claims in the more typical case of an on-the-spot arrest by an individual officer.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Kennedy, J., delivered the opinion of the Court; Thomas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Lozman* is narrow and fact-bound; it left the general probable-cause question open. The Court answered that broader question the next Term in *[[Nieves v. Bartlett]]* (2019): probable cause generally defeats a retaliatory-arrest claim, subject to a narrow exception where police typically exercise discretion not to arrest for the conduct at issue. Teach *Lozman* as the official-municipal-policy sliver and *[[Nieves v. Bartlett|Nieves]]* as the general rule.

## Appears on
- [[Retaliatory Arrest]] — *Anchor*

## Sources
- [*Lozman v. City of Riviera Beach*, 585 U.S. 87 (2018)](https://www.courtlistener.com/opinion/4508137/lozman-v-riviera-beach/) — pinpoint: slip op. at 12 (Kennedy, J., for the Court; the CL opinion text is the slip opinion, 585 U.S. ___, with the holding on slip page 12 — the U.S. Reports pagination is not present in the CL text, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c250bfc7b6993204", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "585 U.S. 87 (2018)", "court": "U.S. Supreme Court", "neutral_cite": "2018 U.S. LEXIS 3691", "official_citation_present": true, "parallel_cite": "138 S. Ct. 1945; 201 L. Ed. 2d 342", "title": "Lozman v. City of Riviera Beach", "year": "2018"}}
{"assertion_id": "aea120e23d7437c4", "dimension": "support", "kind": "home_role", "locator": {"home": "Retaliatory Arrest"}, "payload": {"home": "Retaliatory Arrest", "role": "Anchor", "title": "Lozman v. City of Riviera Beach"}}
{"assertion_id": "c6266f6ad59f4e97", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where a plaintiff alleges that a municipality arrested him pursuant to an official policy of retaliation, formed well before the arrest, in response to speech high in the hierarchy of First Amendment values, the existence of probable cause for the arrest does not bar his First Amendment retaliatory-arrest claim; the Court did not decide the elements of retaliatory-arrest claims in other contexts.", "title": "Lozman v. City of Riviera Beach"}}
{"assertion_id": "65e5c66af1433e6e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Lozman v. City of Riviera Beach", "varies_by_point": "false"}}
{"assertion_id": "de6190b8ba13d7f9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Lozman v. City of Riviera Beach"}}
```

### lake record — Lozman v. City of Riviera Beach

```json
{
  "schema_version": "s2.v1",
  "record_id": "Lozman v. City of Riviera Beach",
  "status": "under_review",
  "identity": {
    "case_name": "Lozman v. Riviera Beach",
    "case_name_short": "Lozman",
    "case_name_full": "",
    "input_case_name": "Lozman v. City of Riviera Beach",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-06-18",
    "year": 2018,
    "docket": "No. 17-21",
    "cluster_id": 4508137,
    "lead_opinion_id": 4285390,
    "sibling_ids": [],
    "absolute_url": "/opinion/4508137/lozman-v-riviera-beach/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "585 U.S. 87",
      "volume": "585",
      "reporter": "U.S.",
      "page": "87",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1945",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 342",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3691",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3691",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "585 U.S. 87",
        "volume": "585",
        "reporter": "U.S.",
        "page": "87",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1945",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1945",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 342",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "342",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3691",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3691",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "585 U.S. 87",
    "official_selection": {
      "court_class": "scotus",
      "selected": "585 U.S. 87",
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
    "date_created": "2026-07-06T13:17:07Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:17:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "lozman-v-city-of-riviera-beach--4508137",
      "to_record_id": "Lozman v. City of Riviera Beach",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Lozman v. City of Riviera Beach

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

     LOZMAN v. CITY OF RIVIERA BEACH, FLORIDA

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

     No. 17–21. Argued February 27, 2018—Decided June 18, 2018
After petitioner Lozman towed his floating home into a slip in a marina
  owned by the city of Riviera Beach, he became an outspoken critic of
  the City’s plan to use its eminent domain power to seize waterfront
  homes for private development and often made critical comments
  about officials during the public-comment period of city council meet-
  ings. He also filed a lawsuit alleging that the City Council’s approval
  of an agreement with developers violated Florida’s open-meetings
  laws. In June 2006 the Council held a closed-door session, in part to
  discuss Lozman’s lawsuit. He alleges that the meeting’s transcript
  shows that councilmembers devised an official plan to intimidate
  him, and that many of his subsequent disputes with city officials and
  employees were part of the City’s retaliation plan. Five months after
  the closed-door meeting, the Council held a public meeting. During
  the public-comment session, Lozman began to speak about the ar-
  rests of officials from other jurisdictions. When he refused a coun-
  cilmember’s request to stop making his remarks, the councilmember
  told the police officer in attendance to “carry him out.” The officer
  handcuffed Lozman and ushered him out of the meeting. The City
  contends that he was arrested for violating the City Council’s rules of
  procedure by discussing issues unrelated to the City and then refus-
  ing to leave the podium. Lozman claims that his arrest was to retali-
  ate for his lawsuit and his prior public criticisms of city officials. The
  State’s attorney determined that there was probable cause for his ar-
  rest, but decided to dismiss the charges.
     Lozman then filed suit under 42 U. S. C. §1983, alleging a number
  of incidents that, under his theory, showed the City’s purpose was to
  harass him, including by initiating an admiralty lawsuit against his
  floating home, see Lozman v. Riviera Beach, 568 U. S. 115. The jury
2                   LOZMAN v. RIVIERA BEACH

                                Syllabus

 returned a verdict for the City on all of the claims. The District
 Court instructed the jury that, for Lozman to prevail on his claim of a
 retaliatory arrest at the city council meeting, he had to prove that the
 arresting officer was motivated by impermissible animus against
 Lozman’s protected speech and that the officer lacked probable cause
 to make the arrest. The Eleventh Circuit affirmed, concluding that
 any error the District Court made when it instructed the jury to con-
 sider the officer’s retaliatory animus was harmless because the jury
 necessarily determined that the arrest was supported by probable
 cause when it found for the City on Lozman’s other claims. The ex-
 istence of probable cause, the court ruled, defeated a First Amend-
 ment claim for retaliatory arrest.
Held: The existence of probable cause does not bar Lozman’s First
 Amendment retaliation claim under the circumstances of this case.
 Pp. 5–13.
    (a) The issue here is narrow. Lozman concedes that there was
 probable cause for his arrest. Nonetheless, he claims, the arrest vio-
 lated the First Amendment because it was ordered in retaliation for
 his earlier, protected speech: his open-meetings lawsuit and his prior
 public criticisms of city officials. Pp. 5–6.
    (b) In a §1983 case, a city or other local governmental entity cannot
 be subject to liability unless the harm was caused in the implementa-
 tion of “official municipal policy.” Monell v. New York City Dept. of
 Social Servs., 436 U. S. 658, 691. The Court assumes that Lozman’s
 arrest was taken pursuant to an official city policy.
    Two major precedents bear on the issue whether the conceded ex-
 istence of probable cause for the arrest bars recovery regardless of
 any intent or purpose to retaliate for past speech. Lozman argues
 that the controlling rule is found in Mt. Healthy City Bd. of Ed. v.
 Doyle, 429 U. S. 274, a civil case in which a city board of education
 decided not to rehire an untenured teacher after a series of incidents,
 including a telephone call to a local radio station. The phone call was
 protected speech, but, the Court held, there was no liability unless
 the alleged constitutional violation was a but-for cause of the em-
 ployment termination. Id., at 285287. The City counters that the
 applicable precedent is Hartman v. Moore, 547 U. S. 250, where the
 Court held that a plaintiff alleging a retaliatory prosecution must
 show the absence of probable cause for the underlying criminal
 charge, id., at 265266. If there was probable cause, the case ends.
 If the plaintiff proves the absence of probable cause, then the Mt.
 Healthy test governs. Pp. 6–10.
    (c) Whether Hartman or Mt. Healthy governs here is a determina-
 tion that must await a different case. For Lozman’s claim is far
 afield from the typical retaliatory arrest claim, and the difficulties
                     Cite as: 585 U. S. ____ (2018)                      3

                                Syllabus

  that might arise if Mt. Healthy is applied to the mine run of arrests
  made by police officers are not present here. Lozman alleges that the
  City itself retaliated against him pursuant to an “official municipal
  policy” of intimidation. Monell, supra, at 691. The fact that he must
  prove the existence and enforcement of an official policy motivated by
  retaliation separates his claim from the typical retaliatory arrest
  claim. An official retaliatory policy can be long term and pervasive,
  unlike an ad hoc, on-the-spot decision by an individual officer. And it
  can be difficult to dislodge. A citizen can seek to have an individual
  officer disciplined or removed from service, but there may be little
  practical recourse when the government itself orchestrates the retali-
  ation. Lozman’s allegations, if proved, also alleviate the problems
  that the City says will result from applying Mt. Healthy in retaliatory
  arrest cases, for it is unlikely that the connection between the alleged
  animus and injury in a case like this will be “weakened . . . by [an of-
  ficial’s] legitimate consideration of speech,” Reichle v. Howards, 566
  U. S. 658, 668, and there is little risk of a flood of retaliatory arrest
  suits against high-level policymakers. Because Lozman alleges that
  the City deprived him of the right to petition, “ ‘one of the most pre-
  cious of the liberties safeguarded by the Bill of Rights,’ ” BE&K Con-
  str. Co. v. NLRB, 536 U. S. 516, 524, his speech is high in the hierar-
  chy of First Amendment values. On these facts, Mt. Healthy provides
  the correct standard for assessing a retaliatory arrest claim. On re-
  mand, the Eleventh Circuit may consider any arguments in support
  of the District Court’s judgment that have been preserved by the
  City, including whether a reasonable juror could find that the City
  formed a retaliatory policy to intimidate Lozman during its closed-
  door session, whether a reasonable juror could find that the arrest
  constituted an official act by the City, and whether, under Mt.
  Healthy, the City has proved that it would have arrested Lozman re-
  gardless of any retaliatory animus. Pp. 10–13.
681 Fed. Appx. 746, vacated and remanded.

  KENNEDY, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and GINSBURG, BREYER, ALITO, SOTOMAYOR, KAGAN, and GORSUCH,
JJ., joined. THOMAS, J., filed a dissenting opinion.
                       Cite as: 585 U. S. ____ (2018)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                   No. 17–21
                                  _________________


  FANE LOZMAN, PETITIONER v. CITY OF RIVIERA 

              BEACH, FLORIDA

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                                [June 18, 2018] 


   JUSTICE KENNEDY delivered the opinion of the Court.
   This case requires the Court to address the intersection
of principles that define when arrests are lawful and
principles that prohibit the government from retaliating
against a person for having exercised the right to free
speech. An arrest deprives a person of essential liberties,
but if there is probable cause to believe the person has
committed a criminal offense there is often no recourse for
the deprivation. See, e.g., Devenpeck v. Alford, 543 U. S.
146, 153 (2004). At the same time, the First Amendment
prohibits government officials from retaliating against
individuals for engaging in protected speech. Crawford-El
v. Britton, 523 U. S. 574, 592 (1998).
   The petitioner in this case alleges that high-level city
policymakers adopted a plan to retaliate against him for
protected speech and then ordered his arrest when he
attempted to make remarks during the public-comment
portion of a city council meeting. The petitioner now
concedes there was probable cause for the arrest. The
question is whether the presence of probable cause
bars petitioner’s retaliatory arrest claim under these
2                LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

circumstances.
                                I
   The city of Riviera Beach is on the Atlantic coast of
Florida, about 75 miles north of Miami. The petitioner
here is Fane Lozman. In 2006 Lozman towed his floating
home into a slip in the City-owned marina, where he
became a resident. Thus began his contentious relation-
ship with the City’s elected officials.
   Soon after his arrival Lozman became an outspoken
critic of the City’s plan to use its eminent domain power to
seize homes along the waterfront for private development.
Lozman often spoke during the public-comment period at
city council meetings and criticized councilmembers, the
mayor, and other public employees. He also filed a lawsuit
alleging that the Council’s approval of an agreement with
developers violated Florida’s open-meetings laws.
   In June 2006 the Council held a closed-door session, in
part to discuss the open-meetings lawsuit that Lozman
recently had filed. According to the transcript of the
meeting, Councilmember Elizabeth Wade suggested that
the City use its resources to “intimidate” Lozman and
others who had filed lawsuits against the City. App. 176.
Later in the meeting a different councilmember asked
whether there was “a consensus of what Ms. Wade is
saying,” and others responded in the affirmative. Id., at
181182. Lozman alleges that these remarks formed an
official plan to intimidate him. The City, on the other
hand, maintains that the only consensus reached during
the meeting was to invest the money and resources neces-
sary to prevail in the litigation against it.
   In all events, Lozman became embroiled in a number of
disputes with city officials and employees over the ensuing
years, many of which Lozman says were part of the City’s
plan of retaliation. The dispute that led to this litigation
took place in 2006. In November of that year, five months
                 Cite as: 585 U. S. ____ (2018)           3

                     Opinion of the Court

after the closed-door meeting where the “intimidate” com-
ment was made, the City Council held a public meeting.
The agenda included a public-comment session in which
citizens could address the Council for a few minutes. As
he had done on earlier occasions and would do more than
200 times over the coming years, see Tr. in No. 9:08–cv–
80134 (SD Fla.), Doc. 785, p. 61, Lozman stepped up to the
podium to give remarks. He began to discuss the recent
arrest of a former county official. Councilmember Wade
interrupted Lozman, directing him to stop making those
remarks. Lozman continued speaking, this time about the
arrest of a former official from the city of West Palm
Beach. Wade then called for the assistance of the police
officer in attendance. The officer approached Lozman and
asked him to leave the podium. Lozman refused. So
Wade told the officer to “carry him out.” The officer hand-
cuffed Lozman and ushered him out of the meeting. The
incident was recorded on video. See Record, Def. Exh. 505,
Doc. 687, available at https://www.supremecourt.gov/media/
video/mp4files/Lozman_v_RivieraBeach.mp4. According to
the City, Lozman was arrested because he violated the
City Council’s rules of procedure by discussing issues
unrelated to the City and then refused to leave the po-
dium. According to Lozman, the arrest was to retaliate for
his open-meetings lawsuit against the City and his prior
public criticisms of city officials.
   Under arrest, Lozman was escorted to police headquar-
ters. He was charged with disorderly conduct and resist-
ing arrest without violence and then released. Later, the
State’s attorney determined there was probable cause to
arrest Lozman for those offenses but decided to dismiss
the charges.
   Lozman filed this lawsuit under Rev. Stat. §1979, 42
U. S. C. §1983. The complaint described a number of
alleged incidents that, under Lozman’s theory, showed the
City’s purpose to harass him in different ways. These
4                LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

ranged from a city employee telling Lozman that his dog
needed a muzzle to the City’s initiation of an admiralty
lawsuit against Lozman’s floating home—the latter result-
ing in an earlier decision by this Court. See Lozman v.
Riviera Beach, 568 U. S. 115 (2013). The evidence and
arguments presented by both parties with respect to all
the matters alleged in Lozman’s suit consumed 19 days of
trial before a jury. The jury returned a verdict for the City
on all of the claims.
   Before this Court, Lozman seeks a reversal only as to
the City’s alleged retaliatory arrest at the November 2006
city council meeting. The District Court instructed the
jury that, for Lozman to prevail on this claim, he had to
prove that the arresting officer was himself motivated by
impermissible animus against Lozman’s protected speech
and that the officer lacked probable cause to make the
arrest. The District Court determined that the evidence
was insufficient as a matter of law to support probable
cause for the offenses charged at the time of the arrest
(disorderly conduct and resisting arrest without violence).
But the District Court concluded that there may have
been probable cause to arrest Lozman for violating a
Florida statute that prohibits interruptions or disturb-
ances in schools, churches, or other public assemblies.
Fla. Stat. §871.01 (2017). (The City had brought this
statute to the District Court’s attention during the course
of the litigation.) The District Court allowed the jury to
decide whether there was probable cause to arrest for the
public-disturbance offense.
   Judgment having been entered for the City after the
jury’s verdict, Lozman appealed. The Court of Appeals for
the Eleventh Circuit affirmed. 681 Fed. Appx. 746 (2017).
As relevant here, the Court of Appeals assumed that the
District Court erred when it instructed the jury that the
officer, rather than the City, must have harbored the
retaliatory animus. But the Court of Appeals held that
                 Cite as: 585 U. S. ____ (2018)           5

                     Opinion of the Court

any error was harmless because the jury necessarily de-
termined that the arrest was supported by probable cause
when it found for the City on some of Lozman’s other
claims—specifically, his claims that the arrest violated the
Fourth Amendment and state law. Id., at 751752. And,
under precedents which the Court of Appeals deemed
controlling, the existence of probable cause defeated a
First Amendment claim for retaliatory arrest. See id., at
752 (citing Dahl v. Holley, 312 F. 3d 1228, 1236 (CA11
2002)).
  This Court granted certiorari, 583 U. S. ___ (2017), on
the issue whether the existence of probable cause defeats a
First Amendment claim for retaliatory arrest under §1983.
The Court considered this issue once before, see Reichle v.
Howards, 566 U. S. 658, 663 (2012), but resolved the case
on different grounds.
                              II
   The issue before the Court is a narrow one. In this
Court Lozman does not challenge the constitutionality of
Florida’s statute criminalizing disturbances at public
assemblies. He does not argue that the statute is overly
broad, e.g., Terminiello v. Chicago, 337 U. S. 1 (1949);
Watchtower Bible & Tract Soc. of N. Y., Inc. v. Village of
Stratton, 536 U. S. 150 (2002); or that it impermissibly
targets speech based on its content or viewpoint, e.g.,
Texas v. Johnson, 491 U. S. 397 (1989); Cohen v. Califor-
nia, 403 U. S. 15 (1971); or that it was enforced in a way
that curtailed Lozman’s right to peaceful assembly, e.g.,
Brown v. Louisiana, 383 U. S. 131 (1966). Lozman, fur-
thermore, does not challenge the validity of the City Coun-
cil’s asserted limitations on the subjects speakers may
discuss during the public-comment portion of city council
meetings (although he continues to dispute whether those
limitations in fact existed).
   Instead Lozman challenges only the lawfulness of his
6                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

arrest, and even that challenge is a limited one. There is
no contention that the City ordered Lozman’s arrest to
discriminate against him based on protected classifica-
tions, or that the City denied Lozman his equal protection
rights by placing him in a “class of one.” See Village of
Willowbrook v. Olech, 528 U. S. 562 (2000) (per curiam).
Lozman, moreover, now concedes that there was probable
cause for the arrest. Although Lozman does not indicate
what facts he believes support this concession, it appears
that the existence of probable cause must be based on the
assumption that Lozman failed to depart the podium after
receiving a lawful order to leave.
   Lozman’s claim is that, notwithstanding the presence of
probable cause, his arrest at the city council meeting
violated the First Amendment because the arrest was
ordered in retaliation for his earlier, protected speech: his
open-meetings lawsuit and his prior public criticisms of
city officials. The question this Court is asked to consider
is whether the existence of probable cause bars that First
Amendment retaliation claim.
                              III
   It is well established that in a §1983 case a city or other
local governmental entity cannot be subject to liability at
all unless the harm was caused in the implementation of
“official municipal policy.” Monell v. New York City Dept.
of Social Servs., 436 U. S. 658, 691 (1978); see Los Angeles
County v. Humphries, 562 U. S. 29, 36 (2010). Lozman’s
§1983 damages claim is against only the City itself, based
on the acts of its officers and employees—here, the mem-
bers of the City Council. Lozman says that the City,
through its city councilmembers, formed an official policy
to retaliate against him and ordered his arrest. The Court
assumes in the discussion to follow that the arrest was
taken pursuant to an official city policy, but whether there
was such a policy and what its content may have been are
                  Cite as: 585 U. S. ____ (2018)             7

                      Opinion of the Court

issues not decided here.
  This brings the discussion to the issue the parties deem
central to the case: whether the conceded existence of
probable cause for the arrest bars recovery regardless of
any intent or purpose to retaliate for past speech. Two
major precedents could bear on this point, and the parties
disagree on which should be applicable here. The first is
this Court’s decision in Mt. Healthy City Bd. of Ed. v.
Doyle, 429 U. S. 274 (1977). See also Board of Comm’rs,
Wabaunsee Cty. v. Umbehr, 518 U. S. 668 (1996). Lozman
urges that the rule of Mt. Healthy should control and that
under it he is entitled to recover. The second is this
Court’s decision in Hartman v. Moore, 547 U. S. 250
(2006), which the City cites for the proposition that once
there is probable cause there can be no further claim that
the arrest was retaliation for protected speech.
  Mt. Healthy arose in a civil, not criminal, context. A city
board of education decided not to rehire an untenured
school teacher after a series of incidents indicating unpro-
fessional demeanor. 429 U. S., at 281283. One of the
incidents was a telephone call the teacher made to a local
radio station to report on a new school policy. Id., at 282.
Because the board of education did not suggest that the
teacher violated any established policy in making the call,
this Court accepted a finding by the District Court that
the call was protected speech. Id., at 284. The Court went
on to hold, however, that since the other incidents, stand-
ing alone, would have justified the dismissal, relief could
not be granted if the board could show that the discharge
would have been ordered even without reference to the
protected speech. Id., at 285287. In terms of precepts in
the law of torts, the Court held that even if retaliation
might have been a substantial motive for the board’s
action, still there was no liability unless the alleged consti-
tutional violation was a but-for cause of the employment
termination. Ibid.; see also Umbehr, supra, at 675.
8                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

   The City resists the applicability of the Mt. Healthy test
as the sole determinant here. It contends that, where
there was probable cause for the arrest, the applicable
precedent is Hartman—a case that was in the criminal
sphere and that turned on the existence of probable cause.
   The background in Hartman was that a company and its
chief executive, William Moore, had engaged in an exten-
sive lobbying and governmental relations campaign oppos-
ing a particular postal service policy. 547 U. S., at
252253. Moore and the company were later prosecuted
for violating federal statutes in the course of that lobbying.
Id., at 253254. After being acquitted, Moore filed suit
against five postal inspectors, alleging that they had
violated his First Amendment rights when they instigated
his prosecution in retaliation for his criticisms of the
Postal Service. Id., at 254. This Court held that a plain-
tiff alleging a retaliatory prosecution must show the ab-
sence of probable cause for the underlying criminal
charge. Id., at 265266. If there was probable cause, the
case ends. If the plaintiff proves the absence of probable
cause, then the Mt. Healthy test governs: The plaintiff
must show that the retaliation was a substantial or moti-
vating factor behind the prosecution, and, if that showing
is made, the defendant can prevail only by showing that
the prosecution would have been initiated without respect
to retaliation. See 547 U. S., at 265–266.
   The Court in Hartman deemed it necessary to inquire as
to the existence of probable cause because proving the link
between the defendant’s retaliatory animus and the plain-
tiff ’s injury in retaliatory prosecution cases “is usually
more complex than it is in other retaliation cases.” Id., at
261. An action for retaliatory prosecution “will not be
brought against the prosecutor, who is absolutely immune
from liability for the decision to prosecute.” Id., at
261262. Instead, the plaintiff must sue some other gov-
ernment official and prove that the official “induced the
                  Cite as: 585 U. S. ____ (2018)            9

                      Opinion of the Court

prosecutor to bring charges that would not have been
initiated without his urging.” Id., at 262. Noting that
inquiries with respect to probable cause are commonplace
in criminal cases, the Court determined that requiring
plaintiffs in retaliatory prosecution cases to prove the lack
of probable cause would help “bridge the gap between the
nonprosecuting government agent’s motive and the prose-
cutor’s action.” Id., at 263.
   The City’s argument here is that, just as probable cause
is a bar in retaliatory prosecution cases, so too should it be
a bar in this case, involving a retaliatory arrest. There is
undoubted force in the City’s position. Reichle, 566 U. S.,
at 667–668. There are on average about 29,000 arrests
per day in this country. Dept. of Justice–FBI, Uniform
Crime Report, Crime in the United States, 2016 (Fall
2017). In deciding whether to arrest, police officers often
make split-second judgments. The content of the suspect’s
speech might be a consideration in circumstances where
the officer must decide whether the suspect is ready to
cooperate, or, on the other hand, whether he may present
a continuing threat to interests that the law must protect.
See, e.g., District of Columbia v. Wesby, 583 U. S. ___, ___
(2018) (slip op., at 10) (“suspect’s untruthful and evasive
answers to police questioning could support probable
cause” (internal quotation marks omitted)).
   For these reasons retaliatory arrest claims, much like
retaliatory prosecution claims, can “present a tenuous
causal connection between the defendant’s alleged animus
and the plaintiff ’s injury.” Reichle, 566 U. S., at 668.
That means it can be difficult to discern whether an arrest
was caused by the officer’s legitimate or illegitimate con-
sideration of speech. Ibid. And the complexity of proving
(or disproving) causation in these cases creates a risk that
the courts will be flooded with dubious retaliatory arrest
suits. See Brief for District of Columbia et al. as Amici
Curiae 511.
10               LOZMAN v. RIVIERA BEACH

                     Opinion of the Court

   At the same time, there are substantial arguments that
Hartman’s framework is inapt in retaliatory arrest cases,
and that Mt. Healthy should apply without a threshold
inquiry into probable cause. For one thing, the causation
problem in retaliatory arrest cases is not the same as the
problem identified in Hartman. Hartman relied in part on
the fact that, in retaliatory prosecution cases, the causal
connection between the defendant’s animus and the prose-
cutor’s decision to prosecute is weakened by the “presump-
tion of regularity accorded to prosecutorial decisionmak-
ing.” 547 U. S., at 263. That presumption does not apply
in this context. See Reichle, supra, at 669. In addition,
there is a risk that some police officers may exploit the
arrest power as a means of suppressing speech. See Brief
for Institute for Free Speech as Amicus Curiae.
                             IV
   The parties’ arguments raise difficult questions about
the scope of First Amendment protections when speech is
made in connection with, or contemporaneously to, crimi-
nal activity. But whether in a retaliatory arrest case the
Hartman approach should apply, thus barring a suit
where probable cause exists, or, on the other hand, the
inquiry should be governed only by Mt. Healthy is a de-
termination that must await a different case. For Loz-
man’s claim is far afield from the typical retaliatory arrest
claim, and the difficulties that might arise if Mt. Healthy
is applied to the mine run of arrests made by police offi-
cers are not present here.
   Here Lozman does not sue the officer who made the
arrest. Indeed, Lozman likely could not have maintained
a retaliation claim against the arresting officer in these
circumstances, because the officer appears to have acted in
good faith, and there is no showing that the officer had
any knowledge of Lozman’s prior speech or any motive to
arrest him for his earlier expressive activities.
                   Cite as: 585 U. S. ____ (2018)             11

                       Opinion of the Court

   Instead Lozman alleges more governmental action than
simply an arrest. His claim is that the City itself retali-
ated against him pursuant to an “official municipal policy” of
intimidation. Monell, 436 U. S., at 691. In particular, he
alleges that the City, through its legislators, formed a
premeditated plan to intimidate him in retaliation for his
criticisms of city officials and his open-meetings lawsuit.
And he asserts that the City itself, through the same high
officers, executed that plan by ordering his arrest at the
November 2006 city council meeting.
   The fact that Lozman must prove the existence and
enforcement of an official policy motivated by retaliation
separates Lozman’s claim from the typical retaliatory
arrest claim. An official retaliatory policy is a particularly
troubling and potent form of retaliation, for a policy can be
long term and pervasive, unlike an ad hoc, on-the-spot
decision by an individual officer. An official policy also can
be difficult to dislodge. A citizen who suffers retaliation by
an individual officer can seek to have the officer disci-
plined or removed from service, but there may be little
practical recourse when the government itself orchestrates
the retaliation.      For these reasons, when retaliation
against protected speech is elevated to the level of official
policy, there is a compelling need for adequate avenues of
redress.
   In addition, Lozman’s allegations, if proved, alleviate
the problems that the City says will result from applying
Mt. Healthy in retaliatory arrest cases. The causation
problem in arrest cases is not of the same difficulty where,
as is alleged here, the official policy is retaliation for prior,
protected speech bearing little relation to the criminal
offense for which the arrest is made. In determining
whether there was probable cause to arrest Lozman for
disrupting a public assembly, it is difficult to see why a
city official could have legitimately considered that Loz-
man had, months earlier, criticized city officials or filed a
12                LOZMAN v. RIVIERA BEACH

                      Opinion of the Court

lawsuit against the City. So in a case like this one it is
unlikely that the connection between the alleged animus
and injury will be “weakened . . . by [an official’s] legiti-
mate consideration of speech.” Reichle, 566 U. S., at 668.
This unique class of retaliatory arrest claims, moreover,
will require objective evidence of a policy motivated by
retaliation to survive summary judgment. Lozman, for
instance, cites a transcript of a closed-door city council
meeting and a video recording of his arrest. There is thus
little risk of a flood of retaliatory arrest suits against high-
level policymakers.
   As a final matter, it must be underscored that this
Court has recognized the “right to petition as one of the
most precious of the liberties safeguarded by the Bill of
Rights.” BE&K Constr. Co. v. NLRB, 536 U. S. 516, 524
(2002) (internal quotation marks omitted). Lozman alleges
the City deprived him of this liberty by retaliating against
him for his lawsuit against the City and his criticisms of
public officials. Thus, Lozman’s speech is high in the
hierarchy of First Amendment values. See Connick v.
Myers, 461 U. S. 138, 145 (1983).
   For these reasons, Lozman need not prove the absence
of probable cause to maintain a claim of retaliatory arrest
against the City. On facts like these, Mt. Healthy provides
the correct standard for assessing a retaliatory arrest
claim. The Court need not, and does not, address the
elements required to prove a retaliatory arrest claim in
other contexts.
   This is not to say, of course, that Lozman is ultimately
entitled to relief or even a new trial. On remand, the
Court of Appeals, applying Mt. Healthy and other relevant
precedents, may consider any arguments in support of the
District Court’s judgment that have been preserved by the
City. Among other matters, the Court of Appeals may
wish to consider (1) whether any reasonable juror could
find that the City actually formed a retaliatory policy to
                 Cite as: 585 U. S. ____ (2018)           13

                     Opinion of the Court

intimidate Lozman during its June 2006 closed-door ses-
sion; (2) whether any reasonable juror could find that the
November 2006 arrest constituted an official act by the
City; and (3) whether, under Mt. Healthy, the City has
proved that it would have arrested Lozman regardless of
any retaliatory animus—for example, if Lozman’s conduct
during prior city council meetings had also violated valid
rules as to proper subjects of discussion, thus explaining
his arrest here.
   For these reasons, the judgment of the Court of Appeals
is vacated, and the case is remanded for further proceed-
ings consistent with this opinion.
                                            It is so ordered.
                  Cite as: 585 U. S. ____ (2018)            1

                     THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 17–21
                          _________________


  FANE LOZMAN, PETITIONER v. CITY OF RIVIERA 

              BEACH, FLORIDA

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

          APPEALS FOR THE ELEVENTH CIRCUIT

                         [June 18, 2018] 


   JUSTICE THOMAS, dissenting.
   We granted certiorari to decide “whether the existence
of probable cause defeats a First Amendment claim for
retaliatory arrest under [42 U. S. C.] §1983.” Ante, at 5.
Instead of resolving that question, the Court decides that
probable cause should not defeat a “unique class of retalia-
tory arrest claims.” Ante, at 12. To fall within this unique
class, a claim must involve objective evidence, of an official
municipal policy of retaliation, formed well before the
arrest, in response to highly protected speech, that has
little relation to the offense of arrest. See ante, at 11–12.
No one briefed, argued, or even hinted at the rule that the
Court announces today. Instead of dreaming up our own
rule, I would have answered the question presented and
held that plaintiffs must plead and prove a lack of prob-
able cause as an element of a First Amendment retaliatory-
arrest claim. I respectfully dissent.
                              I
  The petition for certiorari asked us to resolve whether
“the existence of probable cause defeat[s] a First Amend-
ment retaliatory-arrest claim as a matter of law.” Pet. for
Cert. i. That question has divided the federal courts for
decades. See id., at 10–13. We granted certiorari to con-
sider it six years ago in Reichle v. Howards, 566 U. S. 658,
2                    LOZMAN v. RIVIERA BEACH

                         THOMAS, J., dissenting

663 (2012). But we did not resolve it then because the
petitioner’s second question presented—whether qualified
immunity applied—fully resolved the case. Ibid. Since
Reichle, the split in the federal courts has widened. See
Pet. for Cert. 12–13. In this case, we again granted certio-
rari, 538 U. S. ___ (2017), this time only on the question of
probable cause, see Pet. for Cert. i.
  Yet the Court chooses not to resolve that question,
leaving in place the decades-long disagreement among the
federal courts. The parties concentrated all their argu-
ments on this question in their briefs and at oral argu-
ment. Neither party suggested that there was something
special about Fane Lozman’s claim that would justify a
narrower rule. See, e.g., Tr. of Oral Arg. 15–16 (refusing
to take the “fallback position” that this “is some special
kind of case”). Yet the Court does that work for them by
defining a “unique class of retaliatory arrest claims” that
do not require plaintiffs to plead and prove a lack of prob-
able cause. Ante, at 12.
  By my count, the Court has identified five conditions
that are necessary to trigger its new rule. First, there
must be “an ‘official municipal policy’ of intimidation.”
Ante, at 11 (quoting Monell v. New York City Dept. of
Social Servs., 436 U. S. 658, 691 (1978)). Second, the
policy must be “premeditated” and formed well before the
arrest—here, for example, the policy was formed “months
earlier.” Ante, at 11.1 Third, there must be “objective
evidence” of such a policy. Ante, at 12. Fourth, there must
be “little relation” between the “protected speech” that
prompted the retaliatory policy and “the criminal offense
——————
  1 This requirement suggests that the Court’s rule does not apply

when the “policy” that the plaintiff challenges is an on-the-spot decision
by a single official with final policymaking authority, like the “policy”
that this Court recognized in Pembaur v. Cincinnati, 475 U. S. 469
(1986). See id., at 484–485 (holding that a county prosecutor’s order to
forcibly enter the plaintiff’s clinic was a “municipal policy”).
                     Cite as: 585 U. S. ____ (2018)                     3

                         THOMAS, J., dissenting

for which the arrest is made.” Ante, at 11. Finally, the
protected speech that provoked the retaliatory policy must
be “high in the hierarchy of First Amendment values.”
Ante, at 12. Where all these features are present, the
Court explains, there is not the same “causation problem”
that exists for other retaliatory-arrest claims. Ante, at 11.
  I find it hard to believe that there will be many cases
where this rule will even arguably apply, and even harder
to believe that the plaintiffs in those cases will actually
prove all five requirements. Not even Lozman’s case is a
good fit, as the Court admits when it discusses the rele-
vant considerations for remand. See ante, at 12–13. In
my view, we should not have gone out of our way to fash-
ion a complicated rule with no apparent applicability to
this case or any other.
                               II
   Turning to the question presented, I would hold that
plaintiffs bringing a First Amendment retaliatory-arrest
claim must plead and prove an absence of probable cause.2
This Court has “repeatedly noted that 42 U. S. C. §1983
creates ‘ “a species of tort liability.” ’ ” Memphis Commu-
nity School Dist. v. Stachura, 477 U. S. 299, 305 (1986)
(footnote omitted). Accordingly, we “defin[e] the contours
and prerequisites of a §1983 claim” by “look[ing] first to
the common law of torts.” Manuel v. Joliet, 580 U. S. ___,
___ (2017) (slip op., at 12); see, e.g., Heck v. Humphrey,
512 U. S. 477, 484 (1994) (analogizing to the “common-law
cause of action for malicious prosecution”); id., at 491
(THOMAS, J., concurring) (emphasizing that the decision
——————
   2 I am skeptical that 42 U. S. C. §1983 recognizes a claim for retalia-

tory arrests under the First Amendment. I adhere to the view that “no
‘intent-based’ constitutional tort would have been actionable under the
§1983 that Congress enacted.” Crawford-El v. Britton, 523 U. S. 574,
612 (1998) (Scalia, J., dissenting). But because no party presses this
argument, I assume that such claims are actionable under §1983.
4                LOZMAN v. RIVIERA BEACH

                     THOMAS, J., dissenting

was “consistent . . . with the state of the common law at
the time §1983 was enacted”).
   When §1983 was enacted, there was no common-law tort
for retaliatory arrest in violation of the freedom of speech.
See Hartman v. Moore, 547 U. S. 250, 259 (2006). I would
therefore look to the common-law torts that “provid[e] the
closest analogy” to this claim. Heck, supra, at 484. The
closest analogs here are the three arrest-based torts under
the common law: false imprisonment, malicious prosecu-
tion, and malicious arrest. In defining the elements of
these three torts, 19th-century courts emphasized the
importance of probable cause.
   Consider first the tort of false imprisonment. Common-
law courts stressed the need to shape this tort with an
“indulgence” for peace officers, who are “specially charged
with a duty in the enforcement of the laws.” T. Cooley,
Law of Torts 175 (1880) (Cooley); see, e.g., Hogg v. Ward, 3
H. & N. 417, 423, 157 Eng. Rep. 533, 536 (Ex. 1858) (opin-
ion of Watson, B.) (stressing “the utmost importance that
the police throughout the country should be supported in
the execution of their duty”). Accordingly, private citizens
were always liable for false imprisonment if the arrestee
had not actually committed a felony, but constables were
“excused” if they had “made [the arrest] on reasonable
grounds of belief ”—i.e., probable cause. Cooley 175; ac-
cord, 2 C. Addison, Law of Torts §803, p. 18 (1876); 1 F.
Hilliard, The Law of Torts or Private Wrongs §18, pp. 207–
208, and n. (a) (1866). As Lord Mansfield explained, it
was “of great consequence to the police” that probable
cause shield officers from false-imprisonment claims, as “it
would be a terrible thing” if the threat of liability dissuaded
them from performing their official duties. Ledwith v.
Catchpole, 2 Cald. 291, 295 (K. B. 1783). This concern
outweighed “the mischief and inconvenience to the public”
from the reality that “[m]any an innocent man has and
may be taken up upon suspicion.” Ibid. Many State Su-
                  Cite as: 585 U. S. ____ (2018)            5

                     THOMAS, J., dissenting

preme Courts agreed with Lord Mansfield’s reasoning.
See, e.g., Burns v. Erben, 40 N. Y. 463, 469 (1869) (opinion
of Woodruff, J.) (quoting Ledwith); Brockway v. Crawford,
48 N. C. 433, 437 (1856) (“[The] exempt[ion] for responsi-
bility” for arrests based on probable cause “encourages . . .
a sharp look-out for the apprehension of felons”). As one
court put it, “How, in the great cities of this land, could
police power be exercised, if every peace officer is liable to
civil action for false imprisonment” whenever “persons
arrested upon probable cause shall afterwards be found
innocent?” Hawley v. Butler, 54 Barb. 490, 496 (N. Y. Sup.
1868).
   Courts also stressed the importance of probable cause
when defining the torts of malicious prosecution and
malicious arrest. See, e.g., Ahern v. Collins, 39 Mo. 145,
150 (1866) (holding that “malice and want of probable
cause are necessary ingredients of both”). For the tort of
malicious prosecution, courts emphasized the “necessity”
of both the “allegation” and “proof ” of probable cause, in
light of the public interest “that criminals should be
brought to justice.” Hogg v. Pinckney, 16 S. C. 387, 393
(1882); see also Chrisman v. Carney, 33 Ark. 316, 326
(1878) (“The existence of probable cause is of itself alone a
complete defense . . . . The interest which society has in
the enforcement of the criminal laws requires this rule”).
Similarly, if the element of probable cause were not
“strictly guarded,” “ill consequences would ensue to the
public, for no one would willingly undertake to vindicate a
breach of the public law and discharge his duty to society,
with the prospect of an annoying suit staring him in the
face.” Ventress v. Rosser, 73 Ga. 534, 541 (1884); accord,
Cardival v. Smith, 109 Mass. 158 (1872). The element of
probable cause also played an evidentiary role for both
torts. Lack of probable cause provided “evidence of malice,
though inconclusive,” Herman v. Brookerhoff, 8 Watts 240,
241 (Pa. 1839), because “[m]alice may be inferred from a
6                 LOZMAN v. RIVIERA BEACH

                      THOMAS, J., dissenting

total want of probable cause,” Ventress, supra, at 541;
accord, Ahern, supra, at 150.
  In sum, when §1983 was enacted, the common law
recognized probable cause as an important element for
ensuring that arrest-based torts did not unduly interfere
with the objectives of law enforcement. Common-law
courts were wary of “throw[ing] down the bars which
protect public officers from suits for acts done within the
scope of their duty and authority, by recognizing the right
of every one who chooses to imagine or assert that he is
aggrieved by their doings, to make use of an allegation
that they were malicious in motive to harass them with
suits on that ground.” Chelsey v. King, 74 Me. 164, 175–
176 (1882).
  Applying that principle here, it follows that plaintiffs
bringing a First Amendment retaliatory-arrest claim
under §1983 should have to plead and prove a lack of
probable cause. I see no justification for deviating from
the historical practice simply because an arrest claim is
framed in terms of the First Amendment. Even under a
First Amendment theory, “the significance of probable
cause or the lack of it looms large.” Hartman, 547 U. S., at
265. The presence of probable cause will tend to disprove
that the arrest was done out of retaliation for the plaintiff ’s
speech, and the absence of probable cause will tend to
prove the opposite. See id., at 261. Because “[p]robable
cause or its absence will be at least an evidentiary issue in
practically all such cases” and “[b]ecause showing [its]
absence . . . will have high probative force, and can be
made mandatory with little or no added cost,” the absence
of probable cause should be an “element” of the plaintiff ’s
case. Id., at 265–266; see also id., at 264, n. 10 (refusing
to carve out an exception for unusual cases).
  Moreover, as with the traditional arrest-based torts,
police officers need the safe harbor of probable cause in
the First Amendment context to be able to do their jobs
                  Cite as: 585 U. S. ____ (2018)            7

                     THOMAS, J., dissenting

effectively. Police officers almost always exchange words
with suspects before arresting them. And often a suspect’s
“speech provides evidence of a crime or suggests a poten-
tial threat.” Reichle, 566 U. S., at 668. If probable cause
were not required, the threat of liability might deter an
officer from arresting a suspected criminal who, for exam-
ple, has a political bumper sticker on his car, cf. Kilpatrick
v. United States, 432 Fed. Appx. 937 (CA11 2011); is par-
ticipating in a politically tinged protest, Morse v. San
Francisco Bay Area Rapid Transit Dist., 2014 WL 572352
(ND Cal., Feb. 11, 2014); or confronts and criticizes the
officer during the arrest of a third party, Holland v. San
Francisco, 2013 WL 968295 (ND Cal., Mar. 12, 2013).
Allowing plaintiffs to bring a retaliatory-arrest claim in
such circumstances, without pleading and proving a lack
of probable cause, would permit plaintiffs to harass offi-
cers with the kind of suits that common-law courts deemed
intolerable.
                      *    *    *
  Because we should have answered the question presented
and held that probable cause necessarily defeats First
Amendment retaliatory-arrest claims, I respectfully
dissent.

```

---

## GROUP: content/cases/Mallory v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Mallory v. United States"
type: case
citation: "354 U.S. 449 (1957)"
parallel_cite: "77 S. Ct. 1356; 1 L. Ed. 2d 1479"
neutral_cite: 1957 U.S. LEXIS 586
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1957
date_decided: 1957-06-24
docket: 521
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1957-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mallory v. United States
  varies_by_point: false
  scope_note: "Good law as the 'Mallory' half of the McNabb-Mallory federal prompt-presentment rule. A federal-court rule (Rule 5(a)), not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501's six-hour safe harbor, per Corley v. United States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105545/mallory-v-united-states/"
  cluster_id: 105545
  opinion_id: 105545
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[McNabb v. United States]]", "[[Corley v. United States]]", "[[County of Riverside v. McLaughlin]]", "[[Gerstein v. Pugh]]"]
aliases: []
tags: ["case", "fifth-amendment", "confessions", "mcnabb-mallory", "prompt-presentment", "rule-5a", "federal"]
holding: "A confession obtained from an arrestee during a period of unnecessary delay in bringing him before a committing magistrate, in violation of Federal Rule of Criminal Procedure 5(a), is inadmissible in a federal prosecution; delay used to give an opportunity to extract a confession is 'unnecessary delay.'"
lake:
  record_id: Mallory v. United States
  status: verified
  projected_at: 2026-07-06
---

# Mallory v. United States

*354 U.S. 449 (1957)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mallory, a nineteen-year-old of limited intelligence, was arrested in the early afternoon as a suspect in a rape and detained at police headquarters, within the vicinity of numerous committing magistrates. The police — who already had ample evidence treating him as the chief suspect — questioned him for about a half hour, then asked him to submit to a lie-detector test, without telling him of his rights to counsel or a preliminary examination or that he could remain silent. After roughly four more hours of detention and a polygraph examination, his story began to waver and he confessed in the evening. Only then, the next morning, was he arraigned. The confession was admitted and he was convicted of rape and sentenced to death.

## Issue
Whether a confession obtained during a period of unnecessary delay in bringing a federal arrestee before a committing magistrate, contrary to Federal Rule of Criminal Procedure 5(a), is admissible.

## Rule
No. Rule 5(a) requires prompt presentment, and an arrestee "is not to be taken to police headquarters in order to carry out a process of inquiry that lends itself, even if not so designed, to eliciting damaging statements to support the arrest and ultimately his guilt." — 354 U.S. at 454. ^pin-454

Delay to obtain a confession is "unnecessary": "The duty enjoined upon arresting officers to arraign 'without unnecessary delay' indicates that the command does not call for mechanical or automatic obedience. Circumstances may justify a brief delay between arrest and arraignment . . . . But the delay must not be of a nature to give opportunity for the extraction of a confession." — *Id.* at 455. ^pin-455

## Application
The circumstances "preclude a holding that arraignment was 'without unnecessary delay.'" Mallory was held for hours near available magistrates, questioned and polygraphed without being advised of his rights, and was not arraigned until after he had confessed — "when any judicial caution had lost its purpose." The Court would not subordinate the prompt-arraignment rule to the officers' discretion to find investigative reasons for delay; Rule 5(a) "stands . . . as a barrier" against using station-house interrogation to build the case before presentment.

## Conclusion
The confession was obtained during unnecessary presentment delay in violation of Rule 5(a) and was inadmissible; the conviction was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Mallory* is the second half of the **McNabb-Mallory** federal prompt-presentment rule, building on [[McNabb v. United States]]. It is a **federal-court** rule under Rule 5(a), not a constitutional rule binding the States. Congress later **modified** the rule with 18 U.S.C. §3501's six-hour safe harbor; the Court held §3501 "modified *McNabb-Mallory* without supplanting it" in [[Corley v. United States]]. The prompt-presentment concern is the confession-suppression analog to the prompt judicial probable-cause determination of [[Gerstein v. Pugh]] and [[County of Riverside v. McLaughlin]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *Mallory v. United States*, 354 U.S. 449 (1957) — https://www.courtlistener.com/opinion/105545/mallory-v-united-states/ — pinpoints: 454, 455.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3a1b3f936e75921b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "354 U.S. 449 (1957)", "court": "U.S. Supreme Court", "neutral_cite": "1957 U.S. LEXIS 586", "official_citation_present": true, "parallel_cite": "77 S. Ct. 1356; 1 L. Ed. 2d 1479", "title": "Mallory v. United States", "year": "1957"}}
{"assertion_id": "97c4fd3ab9e6930c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession obtained from an arrestee during a period of unnecessary delay in bringing him before a committing magistrate, in violation of Federal Rule of Criminal Procedure 5(a), is inadmissible in a federal prosecution; delay used to give an opportunity to extract a confession is 'unnecessary delay.'", "title": "Mallory v. United States"}}
{"assertion_id": "c28be864a4ae5d2a", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Anchor", "title": "Mallory v. United States"}}
{"assertion_id": "61aea6fc7e60e616", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1957-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mallory v. United States", "field_i_validity": "good_law", "scope_note": "Good law as the 'Mallory' half of the McNabb-Mallory federal prompt-presentment rule. A federal-court rule (Rule 5(a)), not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501's six-hour safe harbor, per Corley v. United States.", "title": "Mallory v. United States", "varies_by_point": "false"}}
{"assertion_id": "9985dac91b9eb359", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mallory v. United States"}}
```

### lake record — Mallory v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mallory v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mallory v. United States",
    "case_name_short": "Mallory",
    "case_name_full": "Mallory v. United States",
    "input_case_name": "Mallory v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1957-06-24",
    "year": 1957,
    "docket": "521",
    "cluster_id": 105545,
    "lead_opinion_id": 105545,
    "sibling_ids": [
      105545
    ],
    "absolute_url": "/opinion/105545/mallory-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "354 U.S. 449",
      "volume": "354",
      "reporter": "U.S.",
      "page": "449",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "77 S. Ct. 1356",
        "volume": "77",
        "reporter": "S. Ct.",
        "page": "1356",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 L. Ed. 2d 1479",
        "volume": "1",
        "reporter": "L. Ed. 2d",
        "page": "1479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1957 U.S. LEXIS 586",
        "volume": "1957",
        "reporter": "U.S. LEXIS",
        "page": "586",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "354 U.S. 449",
        "volume": "354",
        "reporter": "U.S.",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 S. Ct. 1356",
        "volume": "77",
        "reporter": "S. Ct.",
        "page": "1356",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 L. Ed. 2d 1479",
        "volume": "1",
        "reporter": "L. Ed. 2d",
        "page": "1479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1957 U.S. LEXIS 586",
        "volume": "1957",
        "reporter": "U.S. LEXIS",
        "page": "586",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "354 U.S. 449",
    "official_selection": {
      "court_class": "scotus",
      "selected": "354 U.S. 449",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-454",
      "page": null,
      "quote": "--- # Mallory v. United States *354 U.S. 449 (1957)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mallory, a nineteen-year-old of limited intelligence, was arrested in the early afternoon as a suspect in a rape and detained at police headquarters, within the vicinity of numerous committing magistrates. The police \u2014 who already had ample evidence treating him as the chief suspect \u2014 questioned him for about a half hour, then asked him to submit to a lie-detector test, without telling him of his rights to counsel or a preliminary examination or that he could remain silent. After roughly four more hours of detention and a polygraph examination, his story began to waver and he confessed in the evening. Only then, the next morning, was he arraigned. The confession was admitted and he was convicted of rape and sentenced to death. ## Issue Whether a confession obtained during a period of unnecessary delay in bringing a federal arrestee before a committing magistrate, contrary to Federal Rule of Criminal Procedure 5(a), is admissible. ## Rule No. Rule 5(a) requires prompt presentment, and an arrestee",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-455",
      "page": null,
      "quote": "The duty enjoined upon arresting officers to arraign 'without unnecessary delay' indicates that the command does not call for mechanical or automatic obedience. Circumstances may justify a brief delay between arrest and arraignment . . . . But the delay must not be of a nature to give opportunity for the extraction of a confession.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1957-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mallory v. United States",
    "varies_by_point": false,
    "scope_note": "Good law as the 'Mallory' half of the McNabb-Mallory federal prompt-presentment rule. A federal-court rule (Rule 5(a)), not a constitutional rule binding the States; later modified \u2014 not supplanted \u2014 by 18 U.S.C. \u00a73501's six-hour safe harbor, per Corley v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Fortunato",
          "cluster_id": 6580749,
          "cite": [
            "466 Mass. 500",
            "996 N.E.2d 457",
            "2013 WL 5451772",
            "2013 Mass. LEXIS 719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Garcia-Echaverria",
          "cluster_id": 786819,
          "cite": [
            "374 F.3d 440",
            "2004 U.S. App. LEXIS 13590",
            "2004 WL 1470466"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Doe",
          "cluster_id": 7071197,
          "cite": [
            "155 F.3d 1070",
            "98 Daily Journal DAR 9120",
            "98 Cal. Daily Op. Serv. 6585",
            "1998 U.S. App. LEXIS 20747",
            "1998 WL 527073"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo",
          "cluster_id": 733401,
          "cite": [
            "105 F.3d 117",
            "1997 U.S. App. LEXIS 311",
            "1997 WL 6366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario",
          "cluster_id": 6576998,
          "cite": [
            "422 Mass. 48",
            "661 N.E.2d 71",
            "1996 Mass. LEXIS 29"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Turner",
          "cluster_id": 1188941,
          "cite": [
            "878 P.2d 521",
            "8 Cal. 4th 137",
            "32 Cal. Rptr. 2d 762",
            "94 Daily Journal DAR 11425",
            "94 Cal. Daily Op. Serv. 6238",
            "1994 Cal. LEXIS 4151"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald James Causey",
          "cluster_id": 488057,
          "cite": [
            "818 F.2d 354"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jackson Warren v. City of Lincoln, Nebraska James Breen Sandra L. Myers and David M. Beggs",
          "cluster_id": 487192,
          "cite": [
            "816 F.2d 1254",
            "1987 U.S. App. LEXIS 5135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Woodson v. United States",
          "cluster_id": 1479594,
          "cite": [
            "488 A.2d 910",
            "1985 D.C. App. LEXIS 291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cooper",
          "cluster_id": 6006182,
          "cite": [
            "101 A.D.2d 1",
            "475 N.Y.S.2d 660",
            "1984 N.Y. App. Div. LEXIS 17786"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wilfred Joseph Jackson",
          "cluster_id": 421906,
          "cite": [
            "712 F.2d 1283",
            "1983 U.S. App. LEXIS 25258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane1_negative"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kent v. United States",
          "cluster_id": 107191,
          "cite": [
            "16 L. Ed. 2d 84",
            "86 S. Ct. 1045",
            "383 U.S. 541",
            "1966 U.S. LEXIS 2015"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Riverside v. McLaughlin",
          "cluster_id": 112585,
          "cite": [
            "114 L. Ed. 2d 49",
            "111 S. Ct. 1661",
            "500 U.S. 44",
            "1991 U.S. LEXIS 2528"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harrison v. United States",
          "cluster_id": 107736,
          "cite": [
            "20 L. Ed. 2d 1047",
            "88 S. Ct. 2008",
            "392 U.S. 219",
            "1968 U.S. LEXIS 1349"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The People v. Taylor",
          "cluster_id": 2244130,
          "cite": [
            "211 N.E.2d 673",
            "33 Ill. 2d 417",
            "1965 Ill. LEXIS 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walczyk v. Rio",
          "cluster_id": 2704,
          "cite": [
            "496 F.3d 139",
            "2007 WL 2199005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Blue",
          "cluster_id": 107238,
          "cite": [
            "16 L. Ed. 2d 510",
            "86 S. Ct. 1416",
            "384 U.S. 251",
            "1966 U.S. LEXIS 2952",
            "17 A.F.T.R.2d (RIA) 1032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1104481,
          "cite": [
            "461 So. 2d 686"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jaben v. United States",
          "cluster_id": 107058,
          "cite": [
            "14 L. Ed. 2d 345",
            "85 S. Ct. 1365",
            "381 U.S. 214",
            "1965 U.S. LEXIS 2427"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
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
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lara",
          "cluster_id": 2608464,
          "cite": [
            "432 P.2d 202",
            "67 Cal. 2d 365",
            "62 Cal. Rptr. 586",
            "1967 Cal. LEXIS 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez-Sanchez",
          "cluster_id": 1087948,
          "cite": [
            "128 L. Ed. 2d 319",
            "114 S. Ct. 1599",
            "511 U.S. 350",
            "1994 U.S. LEXIS 3300",
            "94 Daily Journal DAR 5866",
            "94 Cal. Daily Op. Serv. 3059",
            "8 Fla. L. Weekly Fed. S 83",
            "62 U.S.L.W. 4289"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wein",
          "cluster_id": 1202924,
          "cite": [
            "326 P.2d 457",
            "50 Cal. 2d 383",
            "1958 Cal. LEXIS 164"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mallory v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105545) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODI2NjU2MDAwMDAmcz0xMTg3MDYzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105545%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(105545)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTAmcz0yNjQ2MTcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105545%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105545)",
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
    "complete_query": "cites:(105545)",
    "indexed_citing_opinions": 942,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105545,
        "count": 942,
        "count_source": "search"
      }
    ],
    "citation_count": 1364,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mallory-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQyNTM5MDYmcz0yNjg2MTY4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105545%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105545,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105545,
        "cited_id": 104603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105545,
        "cited_id": 240267,
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
    "date_created": "2026-07-05T11:23:50Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:24:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:24:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:27:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:24:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mallory v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b489-11">
  Mr. Justice Frankfurter
 </author>
<p id="A4x6">
  delivered the opinion of the Court.
 </p>
<p id="b489-12">
  Petitioner was convicted of rape in the United States District Court for the District of Columbia, and, as authorized by the District Code, the jury imposed a
  <span citation-index="1" class="star-pagination" label="450"> 
   *450
   </span>
  death sentence. The Court of Appeals affirmed, one judge dissenting. 98 U. S. App. D. C. 406, <span class="citation" data-id="9842838"><a href="/opinion/240267/andrew-r-mallory-v-united-states/" aria-description="Citation for case: Andrew R. Mallory v. United States">236 F. 2d 701</a></span>. Since an important question involving the interpretation of the Federal Rules of Criminal Procedure was involved in this capital case, we granted the petition for certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./352/877/">352 U. S. 877</a></span>.
 </p>
<p id="b490-5">
  The rape occurred at six p. m. on April 7, 1954, in the basement of the apartment house inhabited by the victim. She had descended to the basement a few minutes previous to wash some laundry. Experiencing some difficulty in detaching a hose in the sink, she sought help from the janitor, who lived in a basement apartment with his wife, two grown sons, a younger son and the petitioner, his nineteen-year-old half-brother. Petitioner was alone in the apartment at the time. He detached the hose and returned to his quarters. Very shortly thereafter, a masked man, whose general features were identified to resemble those of petitioner and his two grown nephews, attacked the woman. She had heard no one descend the wooden steps that furnished the only means of entering the basement from above.
 </p>
<p id="b490-6">
  Petitioner and one of his grown nephews disappeared from the apartment house shortly after the crime was committed. The former was apprehended the following afternoon between two and two-thirty p. m. and was taken, along with his older nephews, also suspects, to police headquarters. At least four officers questioned him there in the presence of other officers for thirty to forty-five minutes, beginning the examination by telling him, according to his testimony, that his brother had said that he was the assailant. Petitioner strenuously denied his guilt. He spent the rest of the afternoon at headquarters, in the company of the other two suspects and his brother a good part of the time. About four p. m. the three suspects were asked to submit to “lie detector” tests, and they agreed. The officer in charge of the poly
  <span citation-index="1" class="star-pagination" label="451"> 
   *451
   </span>
  graph machine was not located for almost two hours, during which time the suspects received food and drink. The nephews were then examined first. Questioning of petitioner began just after eight p. m. Only he and the polygraph operator were present in' a small room, the door to which was closed.
 </p>
<p id="b491-5">
  Following almost an hour and one-half of steady interrogation, he “first stated that he could have done this crime, or that he might have done it. He finally stated that he was responsible . . . .” (Testimony of polygraph operator, R. 70.) Not until ten p. m., after petitioner had repeated his confession to other officers, did the police attempt to reach a United States Commissioner for the purpose of arraignment. Failing in this, they obtained petitioner's consent to examination by the deputy coroner, who noted no indicia of physical or psychological coercion. Petitioner was then confronted by the complaining witness and “[p]ractically every man in the Sex Squad,” and in response to questioning by three officers, he repeated the confession. Between eleven-thirty p. m. and twelve-thirty a. m. he dictated the confession to a typist. The next morning he was brought before a Commissioner. At the trial, which was delayed for a year because of doubt about petitioner’s capacity to understand the proceedings against him, the signed confession was introduced in evidence.
 </p>
<p id="b491-6">
  The case calls for the proper application of Rule 5 (a) of the Federal Rules of Criminal Procedure, promulgated in 1946, <span class="citation no-link">327 U. S. 821</span>. That Rule provides:
 </p>
<blockquote id="b491-7">
  “(a) Appearance before the Commissioner. An officer making an arrest under a warrant issued upon a complaint or any person making an arrest without a warrant shall take the arrested person without unnecessary delay before the nearest available commissioner or before any other nearby officer
  <span citation-index="1" class="star-pagination" label="452"> 
   *452
   </span>
  empowered to commit persons charged with offenses against the laws of the United States. When a person arrested without a warrant is brought before a commissioner or other officer, a complaint shall be filed forthwith.”
 </blockquote>
<p id="b492-6">
  This provision has both statutory and judicial antecedents for guidance in applying it. The requirement that arraignment be “without unnecessary delay” is a compendious restatement, without substantive change, of several prior specific federal statutory provisions.
  <em>
   (E. g.,
  </em>
  <span class="citation no-link">20 Stat. 327</span>, 341; <span class="citation no-link">48 Stat. 1008</span>; also <span class="citation no-link">28 Stat. 416</span>.) See Dession, The New Federal Rules of Criminal Procedure: I, 55 Yale L. J. 694, 707. Nearly all the States have similar enactments.
 </p>
<p id="b492-7">
  In
  <em>
   McNabb
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#343" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 343-344</a></span>, we spelled out the important reasons of policy behind this body of legislation:
 </p>
<blockquote id="b492-8">
  “The purpose of this impressively pervasive requirement of criminal procedure is plain. . . . The awful instruments of the criminal law cannot be entrusted to a single functionary. The complicated process of criminal justice is therefore divided into different parts, responsibility for which is separately vested in the various participants upon whom the criminal law relies for its vindication. Legislation such as this, requiring that the police must with reasonable promptness show legal cause for detaining arrested persons, constitutes an important safeguard — not only in assuring protection for the innocent but also in securing conviction of the guilty by methods that commend themselves to a progress sive and self-confident society. For this procedural requirement checks resort to those reprehensible practices known as the ‘third degree’ which, though universally rejected as indefensible, still find their
  <span citation-index="1" class="star-pagination" label="453"> 
   *453
   </span>
  way into use. It aims to avoid all the evil implications of secret interrogation of persons accused of crime.”
 </blockquote>
<p id="b493-5">
  Since such unwarranted detention led to tempting utilization of intensive interrogation, easily gliding into the evils of “the third degree,” the Court held that police detention of defendants beyond the time when a committing magistrate was readily accessible constituted “willful disobedience of law.” In order adequately to enforce the congressional requirement of prompt arraignment, it was deemed necessary to render inadmissible incriminating statements elicited from defendants during a period of unlawful detention.
 </p>
<p id="b493-6">
  In
  <em>
   Upshaw
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420236"><a href="/opinion/104603/upshaw-v-united-states/" aria-description="Citation for case: Upshaw v. United States">335 U. S. 410</a></span>, which came here after the Federal Rules of Criminal Procedure had been in operation, the Court made it clear that Rule 5 (a)’s standard of “without unnecessary delay” implied no relaxation of the
  <em>
   <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">McNabb</a></span>
  </em>
  doctrine.
 </p>
<p id="b493-7">
  The requirement of Rule 5 (a) is part of the procedure devised by Congress for safeguarding individual rights without hampering effective and intelligent law enforcement. Provisions related to Rule 5 (a) contemplate a procedure that allows arresting officers little more leeway than the interval between arrest and the ordinary administrative steps required to bring a suspect before the nearest available magistrate. Rule 4 (a) provides: “If it appears from the complaint that there is probable cause to believe that an offense has been committed and that the defendant has committed it, a warrant for the arrest of the defendant shall issue . . . .” Rule 4 (b) requires that the warrant “shall command that the defendant be arrested and brought before the nearest available commissioner.” And Rules 5 (b) and (c) reveal the function of the requirement of prompt arraignment:
 </p>
<blockquote id="b493-8">
  “(b) Statement by the Commissioner. The commissioner shall inform the defendant of the com
  <span citation-index="1" class="star-pagination" label="454"> 
   *454
   </span>
  plaint against him, of his right to retain counsel and of his right to have a preliminary examination. He shall also inform the defendant that he is not required to make a statement and that any statement made by him may be used against him. The commissioner shall allow the defendant reasonable time and opportunity to consult counsel and shall admit the defendant to bail as provided in these rules.
 </blockquote>
<blockquote id="b494-5">
  “(c) Preliminary Examination. The defendant shall not be called upon to plead. If the defendant waives preliminary examination, the commissioner shall forthwith hold him to answer in the district court. If the defendant does not waive examination, the commissioner shall hear the evidence within a reasonable time. The defendant may cross-examine witnesses against him and may introduce evidence in his own behalf. If from the evidence it appears to the commissioner that there is probable cause to believe that an offense has been committed and that the defendant has committed it, the commissioner shall forthwith hold him to answer in the district court; otherwise the commissioner shall discharge him. The commissioner shall admit the defendant to bail as provided in these rules.”
 </blockquote>
<p id="b494-6">
  The scheme for initiating a federal prosecution is plainly defined. The police may not arrest upon mere suspicion but only on “probable cause.” The next step in the proceeding is to arraign the arrested person before a judicial officer as quickly as possible so that he may be advised of his rights and so that the issue of probable cause may be promptly determined. The arrested person may, of course, be “booked” by the police. But he is not to be taken to police headquarters in order to carry out a process of inquiry that lends itself, even if not so designed, to eliciting damaging statements to support the arrest and ultimately his guilt.
 </p>
<p id="b495-4">
<span citation-index="1" class="star-pagination" label="455"> 
   *455
   </span>
  The duty enjoined upon arresting officers to arraign “without unnecessary delay” indicates that the command does not call for mechanical or automatic obedience. Circumstances may justify a brief delay between arrest and arraignment, as for instance, where the story volunteered by the accused is susceptible of quick verification through third parties. But the delay must not be of a nature to give opportunity for the extraction of a confession.
 </p>
<p id="b495-5">
  The circumstances of this case preclude a holding that arraignment was “without unnecessary delay.” Petitioner was arrested in the early afternoon and was detained at headquarters within the vicinity of numerous committing magistrates. Even though the police had ample evidence from other sources than the petitioner for regarding the petitioner as the chief suspect, they first questioned him for approximately a half hour. When this inquiry of a nineteen-year-old lad of limited intelligence produced no confession, the police asked him to submit to a “lie-detector” test. He was not told of his rights to counsel or to a preliminary examination before a magistrate, nor was he warned that he might keep silent and “that any statement made by him may be used against him.” After four hours of further detention at headquarters, during which arraignment could easily have been made in the same building in which the police headquarters were housed, petitioner was examined by the lie-detector operator for another hour and a half before his story began to waver. Not until he had confessed, when any judicial caution had lost its purpose, did the police arraign him.
 </p>
<p id="b495-6">
  We cannot sanction this extended delay, resulting in confession, without subordinating the general rule of prompt arraignment to the discretion of arresting officers in finding exceptional circumstances for its disregard. In every case where the police resort to interrogation of
  <span citation-index="1" class="star-pagination" label="456"> 
   *456
   </span>
  an arrested person and secure a confession, they may well claim, and quite sincerely, that they were merely trying to check on the information given by him. Against such a claim and the evil potentialities of the practice for which it is urged stands Rule 5 (a) as a barrier. Nor is there an escape from the constraint laid upon the police by that Rule in that two other suspects were involved for the same crime. Presumably, whomever the police arrest they must arrest on “probable cause.” It is not the function of the police to arrest, as it were, at large and to use an interrogating process at police headquarters in order to determine whom they should charge before a committing magistrate on “probable cause.”
 </p>
<p id="b496-5">
<em>
   Reversed and remanded.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Malloy v. Hogan.md  (`case`, 6 assertions)

### content_page

```
---
title: "Malloy v. Hogan"
type: case
citation: "378 U.S. 1 (1964)"
parallel_cite: "84 S. Ct. 1489; 12 L. Ed. 2d 653"
neutral_cite: 1964 U.S. LEXIS 993
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-15
docket: 110
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Malloy v. Hogan
  varies_by_point: false
  scope_note: "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106862/malloy-v-hogan/"
  cluster_id: 106862
  opinion_id: 106862
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[Miranda v. Arizona]]", "[[Mapp v. Ohio]]", "[[Brown v. Mississippi]]", "[[Wolf v. Colorado]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "incorporation", "self-incrimination", "voluntariness"]
holding: "The Fifth Amendment privilege against self-incrimination is enforceable against the States through the Fourteenth Amendment by the same standards that apply to the Federal Government; Twining and Adamson are overruled to that extent."
lake:
  record_id: Malloy v. Hogan
  status: verified
  projected_at: 2026-07-06
---

# Malloy v. Hogan

*378 U.S. 1 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Malloy, on probation for a state gambling misdemeanor, was called before a state inquiry into gambling. He refused to answer questions about his arrest and associates, invoking the privilege against self-incrimination. The Connecticut courts, relying on *Twining v. New Jersey* and *Adamson v. California*, held the privilege did not bind the State, found the questions non-incriminatory, and held him in contempt — imprisoning him until he answered. He sought [[Common Legal Terms#habeas-corpus|habeas corpus]].

## Issue
Whether the Fifth Amendment privilege against self-incrimination is safeguarded against state action by the Fourteenth Amendment, and by what standard.

## Rule
The privilege is incorporated against the States. "We hold today that the Fifth Amendment's exception from compulsory self-incrimination is also protected by the Fourteenth Amendment against abridgment by the States." — 378 U.S. at 6. ^pin-6

"The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement—the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence." — *Id.* at 8. ^pin-8

The same standard governs in both forums: the Fourteenth Amendment does not apply to the States merely "a 'watered-down, subjective version of the individual guarantees of the Bill of Rights.'" — *Id.* at 10–11. ^pin-10

## Application
Because the privilege binds the States by the same standard as the Federal Government, Connecticut could not imprison Malloy for contempt for declining to answer questions that might incriminate him, and its courts erred in measuring his claim against a less stringent, "watered-down" standard. Applying the federal test, his refusal was justified because truthful answers could have furnished a link in a chain of evidence connecting him to crime; the state inquiry could not compel him on pain of imprisonment.

## Conclusion
The Fifth Amendment privilege is enforceable against the States through the Fourteenth Amendment by the same standards as in federal proceedings; the contempt judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. *Twining* and *Adamson* were overruled to the extent they held otherwise.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Malloy* is a foundational incorporation decision: it harmonized the confession-voluntariness standard (rooted in [[Brown v. Mississippi]]) with the Fifth Amendment privilege and supplied the constitutional predicate for [[Miranda v. Arizona]] two years later. It draws on [[Mapp v. Ohio]] (which overruled [[Wolf v. Colorado]]) for the parallel incorporation of the Fourth Amendment.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Malloy v. Hogan*, 378 U.S. 1 (1964) — https://www.courtlistener.com/opinion/106862/malloy-v-hogan/ — pinpoints: 6, 8, 10–11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a484c7f671851194", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "378 U.S. 1 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 993", "official_citation_present": true, "parallel_cite": "84 S. Ct. 1489; 12 L. Ed. 2d 653", "title": "Malloy v. Hogan", "year": "1964"}}
{"assertion_id": "5704a1bd6d72c0d9", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (cross-doctrine)", "title": "Malloy v. Hogan"}}
{"assertion_id": "71abf754f1bb0d5c", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Anchor", "title": "Malloy v. Hogan"}}
{"assertion_id": "cc70664a52ee8216", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Fifth Amendment privilege against self-incrimination is enforceable against the States through the Fourteenth Amendment by the same standards that apply to the Federal Government; Twining and Adamson are overruled to that extent.", "title": "Malloy v. Hogan"}}
{"assertion_id": "8a8296f547b7e952", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-06-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Malloy v. Hogan", "field_i_validity": "good_law", "scope_note": "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point.", "title": "Malloy v. Hogan", "varies_by_point": "false"}}
{"assertion_id": "9edb6f5d1b582321", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Malloy v. Hogan"}}
```

### lake record — Malloy v. Hogan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Malloy v. Hogan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Malloy v. Hogan",
    "case_name_short": "Malloy",
    "case_name_full": "Malloy v. Hogan, Sheriff",
    "input_case_name": "Malloy v. Hogan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-15",
    "year": 1964,
    "docket": "110",
    "cluster_id": 106862,
    "lead_opinion_id": 106862,
    "sibling_ids": [
      106862,
      9422839,
      9422840
    ],
    "absolute_url": "/opinion/106862/malloy-v-hogan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 1",
      "volume": "378",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1489",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 653",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 993",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "993",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 1",
        "volume": "378",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1489",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 653",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 993",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "993",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-6",
      "page": null,
      "quote": "--- # Malloy v. Hogan *378 U.S. 1 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Malloy, on probation for a state gambling misdemeanor, was called before a state inquiry into gambling. He refused to answer questions about his arrest and associates, invoking the privilege against self-incrimination. The Connecticut courts, relying on *Twining v. New Jersey* and *Adamson v. California*, held the privilege did not bind the State, found the questions non-incriminatory, and held him in contempt \u2014 imprisoning him until he answered. He sought habeas corpus. ## Issue Whether the Fifth Amendment privilege against self-incrimination is safeguarded against state action by the Fourteenth Amendment, and by what standard. ## Rule The privilege is incorporated against the States.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-8",
      "page": null,
      "quote": "The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement\u2014the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-10",
      "page": null,
      "quote": "a 'watered-down, subjective version of the individual guarantees of the Bill of Rights.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Malloy v. Hogan",
    "varies_by_point": false,
    "scope_note": "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 10829752,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Deonte WB Ellison",
          "cluster_id": 9372742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8244686,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8242363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 7861363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamie Peterson v. David Heymes",
          "cluster_id": 4642776,
          "cite": [
            "931 F.3d 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heffington v. Moser",
          "cluster_id": 4531554,
          "cite": [
            "192 A.3d 900",
            "238 Md. App. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boykin v. Alabama",
          "cluster_id": 107951,
          "cite": [
            "23 L. Ed. 2d 274",
            "89 S. Ct. 1709",
            "395 U.S. 238",
            "1969 U.S. LEXIS 1434"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brady v. United States",
          "cluster_id": 108137,
          "cite": [
            "25 L. Ed. 2d 747",
            "90 S. Ct. 1463",
            "397 U.S. 742",
            "1970 U.S. LEXIS 45"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re GAULT",
          "cluster_id": 107439,
          "cite": [
            "18 L. Ed. 2d 527",
            "87 S. Ct. 1428",
            "387 U.S. 1",
            "1967 U.S. LEXIS 1478",
            "40 Ohio Op. 2d 378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santobello v. New York",
          "cluster_id": 108416,
          "cite": [
            "30 L. Ed. 2d 427",
            "92 S. Ct. 495",
            "404 U.S. 257",
            "1971 U.S. LEXIS 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pointer v. Texas",
          "cluster_id": 107014,
          "cite": [
            "13 L. Ed. 2d 923",
            "85 S. Ct. 1065",
            "380 U.S. 400",
            "1965 U.S. LEXIS 1481"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashe v. Swenson",
          "cluster_id": 108114,
          "cite": [
            "25 L. Ed. 2d 469",
            "90 S. Ct. 1189",
            "397 U.S. 436",
            "1970 U.S. LEXIS 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. California",
          "cluster_id": 107038,
          "cite": [
            "14 L. Ed. 2d 106",
            "85 S. Ct. 1229",
            "380 U.S. 609",
            "1965 U.S. LEXIS 1346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Benton v. Maryland",
          "cluster_id": 107980,
          "cite": [
            "23 L. Ed. 2d 707",
            "89 S. Ct. 2056",
            "395 U.S. 784",
            "1969 U.S. LEXIS 1167"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duncan v. Louisiana",
          "cluster_id": 107685,
          "cite": [
            "20 L. Ed. 2d 491",
            "88 S. Ct. 1444",
            "391 U.S. 145",
            "1968 U.S. LEXIS 1631",
            "45 Ohio Op. 2d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106862 OR 9422839 OR 9422840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTE2MjMzNjAwMDAwJnM9NDQ2MDI4MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106862+OR+9422839+OR+9422840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106862 OR 9422839 OR 9422840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTM0JnM9MTE4MzgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106862+OR+9422839+OR+9422840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106862 OR 9422839 OR 9422840)",
        "reviewed": 79,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 79,
        "triage_read": 1,
        "triage_snippet_classified": 78
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106862 OR 9422839 OR 9422840)",
    "indexed_citing_opinions": 2305,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106862,
        "count": 2083,
        "count_source": "search"
      },
      {
        "opinion_id": 9422839,
        "count": 274,
        "count_source": "search"
      },
      {
        "opinion_id": 9422840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3675,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/malloy-v-hogan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzc4NzImcz0xMDM2NzYzOSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106862+OR+9422839+OR+9422840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106862,
        "cited_id": 89245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 92032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 92834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94828,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 95204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 98977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100708,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 101836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105306,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 2354861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 2621051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 3321596,
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
    "date_created": "2026-07-05T11:27:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:31:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Malloy v. Hogan

```
<div>
<center><b><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U.S. 1</a></span> (1964)</b></center>
<center><h1>MALLOY<br>
v.<br>
HOGAN, SHERIFF.</h1></center>
<center>No. 110.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 5, 1964.</center>
<center>Decided June 15, 1964.</center>
CERTIORARI TO THE SUPREME COURT OF ERRORS OF CONNECTICUT.
<p><span class="star-pagination">*2</span> <i>Harold Strauch</i> argued the cause and filed a brief for petitioner.</p>
<p><i>John D. LaBelle,</i> State's Attorney for Connecticut, argued the cause for respondent. With him on the brief were <i>George D. Stoughton</i> and <i>Harry W. Hultgren, Jr.,</i> Assistant State's Attorneys.</p>
<p><i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union, as <i>amicus curiae,</i> urging reversal.</p>
<p>Briefs of <i>amici curiae,</i> urging affirmance, were filed by <i>Stanley Mosk,</i> Attorney General of California, <i>William E. James,</i> Assistant Attorney General, and <i>Gordon Ringer,</i> Deputy Attorney General, for the State of California; and by <i>Frank S. Hogan, Edward S. Silver, H. Richard Uviller, Michael R. Juviler, Aaron E. Koota</i> and <i>Irving P. Seidman</i> for the National District Attorneys' Association.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>In this case we are asked to reconsider prior decisions holding that the privilege against self-incrimination is not safeguarded against state action by the Fourteenth Amendment. <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>; <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>.<sup>[1]</sup></p>
<p><span class="star-pagination">*3</span> The petitioner was arrested during a gambling raid in 1959 by Hartford, Connecticut, police. He pleaded guilty to the crime of pool selling, a misdemeanor, and was sentenced to one year in jail and fined $500. The sentence was ordered to be suspended after 90 days, at which time he was to be placed on probation for two years. About 16 months after his guilty plea, petitioner was ordered to testify before a referee appointed by the Superior Court of Hartford County to conduct an inquiry into alleged gambling and other criminal activities in the county. The petitioner was asked a number of questions related to events surrounding his arrest and conviction. He refused to answer any question "on the grounds it may tend to incriminate me." The Superior Court adjudged him in contempt, and committed him to prison until he was willing to answer the questions. Petitioner's application for a writ of habeas corpus was denied by the Superior Court, and the Connecticut Supreme Court of Errors affirmed. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">150 Conn. 220</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d 744</a></span>. The latter court held that the Fifth Amendment's privilege against self-incrimination was not available to a witness in a state proceeding, that the Fourteenth Amendment extended no privilege to him, and that the petitioner had not properly invoked the privilege available under the Connecticut Constitution. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./373/948/">373 U. S. 948</a></span>. We reverse. We hold that the Fourteenth Amendment guaranteed the petitioner the protection of the Fifth Amendment's privilege against self-incrimination, and that under the applicable federal standard, the Connecticut Supreme Court of Errors erred in holding that the privilege was not properly invoked.</p>
<p><span class="star-pagination">*4</span> The extent to which the Fourteenth Amendment prevents state invasion of rights enumerated in the first eight Amendments has been considered in numerous cases in this Court since the Amendment's adoption in 1868. Although many Justices have deemed the Amendment to incorporate all eight of the Amendments,<sup>[2]</sup> the view which has thus far prevailed dates from the decision in 1897 in <i>Chicago, B. &amp; Q. R. Co.</i> v. <i>Chicago,</i> <span class="citation" data-id="9417760"><a href="/opinion/94648/chicago-burlington-quincy-railroad-v-chicago/" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. Chicago">166 U. S. 226</a></span>, which held that the Due Process Clause requires the States to pay just compensation for private property taken for public use.<sup>[3]</sup> It was on the authority of that decision that the Court said in 1908 in <i>Twining</i> v. <i>New <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Jersey, supra</a></span></i><i>,</i> that "it is possible that some of the personal rights safeguarded by the first eight Amendments <span class="star-pagination">*5</span> against National action may also be safeguarded against state action, because a denial of them would be a denial of due process of law." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#99" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 99</a></span>.</p>
<p>The Court has not hesitated to re-examine past decisions according the Fourteenth Amendment a less central role in the preservation of basic liberties than that which was contemplated by its Framers when they added the Amendment to our constitutional scheme. Thus, although the Court as late as 1922 said that "neither the Fourteenth Amendment nor any other provision of the Constitution of the United States imposes upon the States any restrictions about `freedom of speech' . . . ," <i>Prudential Ins. Co.</i> v. <i>Cheek,</i> <span class="citation" data-id="100023"><a href="/opinion/100023/prudential-insurance-co-of-america-v-cheek/#543" aria-description="Citation for case: Prudential Insurance Co. of America v. Cheek">259 U. S. 530, 543</a></span>, three years later <i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652</a></span>, initiated a series of decisions which today hold immune from state invasion every First Amendment protection for the cherished rights of mind and spiritthe freedoms of speech, press, religion, assembly, association, and petition for redress of grievances.<sup>[4]</sup></p>
<p>Similarly, <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>, decided in 1937, suggested that the rights secured by the Fourth Amendment were not protected against state action, citing, <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#324" aria-description="Citation for case: Palko v. Connecticut">302 U. S., at 324</a></span>, the statement of the Court in 1914 in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span>, that "the Fourth Amendment is not directed to individual misconduct of [state] officials." In 1961, however, the <span class="star-pagination">*6</span> Court held that in the light of later decisions,<sup>[5]</sup> it was taken as settled that ". . . the Fourth Amendment's right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth. . . ." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span>. Again, although the Court held in 1942 that in a state prosecution for a noncapital offense, "appointment of counsel is not a fundamental right," <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#471" aria-description="Citation for case: Betts v. Brady">316 U. S. 455, 471</a></span>; cf. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, only last Term this decision was re-examined and it was held that provision of counsel in all criminal cases was "a fundamental right, essential to a fair trial," and thus was made obligatory on the States by the Fourteenth Amendment. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#343" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 343-344</a></span>.<sup>[6]</sup></p>
<p>We hold today that the Fifth Amendment's exception from compulsory self-incrimination is also protected by the Fourteenth Amendment against abridgment by the States. Decisions of the Court since <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> and <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson</a></span></i> have departed from the contrary view expressed in those cases. We discuss first the decisions which forbid the use of coerced confessions in state criminal prosecutions.</p>
<p><i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, was the first case in which the Court held that the Due Process Clause prohibited the States from using the accused's coerced confessions against him. The Court in <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> felt impelled, in light of <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> to say that its conclusion did not involve the privilege against self-incrimination. "Compulsion by torture to extort a confession is a different matter." <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S., at 285</a></span>. But this distinction was soon <span class="star-pagination">*7</span> abandoned, and today the admissibility of a confession in a state criminal prosecution is tested by the same standard applied in federal prosecutions since 1897, when, in <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>, the Court held that "[i]n criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment to the Constitution of the United States, commanding that no person `shall be compelled in any criminal case to be a witness against himself.' " <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><i>Id.,</i> at 542</a></span>. Under this test, the constitutional inquiry is not whether the conduct of state officers in obtaining the confession was shocking, but whether the confession was "free and voluntary: that is, [it] must not be extracted by any sort of threats or violence, nor obtained by any direct or implied promises, however slight, nor by the exertion of any improper influence. . . ." <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><i>Id.,</i> at 542-543</a></span>; see also <i>Hardy</i> v. <i>United States,</i> <span class="citation" data-id="2621051"><a href="/opinion/2621051/hardy-v-united-states/#229" aria-description="Citation for case: Hardy v. United States">186 U. S. 224, 229</a></span>; <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1, 14</a></span>; <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#150" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 150</a></span>. In other words the person must not have been compelled to incriminate himself. We have held inadmissible even a confession secured by so mild a whip as the refusal, under certain circumstances, to allow a suspect to call his wife until he confessed. <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>.</p>
<p>The marked shift to the federal standard in state cases began with <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, where the Court spoke of the accused's "free choice to admit, to deny, or to refuse to answer." <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California"><i>Id.,</i> at 241</a></span>. See <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>. The shift reflects recognition that the American system of criminal prosecution is accusatorial, not inquisitorial, and that the Fifth Amendment privilege is its essential mainstay. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, <span class="star-pagination">*8</span> 541. Governments, state and federal, are thus constitutionally compelled to establish guilt by evidence independently and freely secured, and may not by coercion prove a charge against an accused out of his own mouth. Since the Fourteenth Amendment prohibits the States from inducing a person to confess through "sympathy falsely aroused," <i>Spano</i> v. <i>New York, supra,</i> at 323, or other like inducement far short of "compulsion by torture," <i>Haynes</i> v. <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Washington, supra</a></span></i><i>,</i> it follows <i>a fortiori</i> that it also forbids the States to resort to imprisonment, as here, to compel him to answer questions that might incriminate him. The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringementthe right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty, as held in <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> for such silence.</p>
<p>This conclusion is fortified by our recent decision in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, overruling <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, which had held "that in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure," <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#33" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 33</a></span>. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> held that the Fifth Amendment privilege against self-incrimination implemented the Fourth Amendment in such cases, and that the two guarantees of personal security conjoined in the Fourteenth Amendment to make the exclusionary rule obligatory upon the States. We relied upon the great case of <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, decided in 1886, which, considering the Fourth and Fifth Amendments as running "almost into each other," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States"><i>id.,</i> at 630</a></span>, held that "Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within <span class="star-pagination">*9</span> the condemnation of [those Amendments] . . . ." At 630. We said in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>:</i></p>
<blockquote>"We find that, as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an `intimate relation' in their perpetuation of `principles of humanity and civil liberty [secured] . . . only after years of struggle,' <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span>. . . . The philosophy of each Amendment and of each freedom is complementary to, although not dependent upon, that of the other in its sphere of influencethe very least that together they assure in either sphere is that no man is to be convicted on unconstitutional evidence." <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656-657</a></span>.</blockquote>
<p>In thus returning to the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> view that the privilege is one of the "principles of a free government," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#632" aria-description="Citation for case: Boyd v. United States">116 U. S., at 632</a></span>,<sup>[7]</sup><i>Mapp</i> necessarily repudiated the <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> concept of the privilege as a mere rule of evidence "best defended not as an unchangeable principle of universal justice but as a law proved by experience to be expedient." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#113" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 113</a></span>.</p>
<p>The respondent Sheriff concedes in his brief that under our decisions, particularly those involving coerced <span class="star-pagination">*10</span> confessions, "the accusatorial system has become a fundamental part of the fabric of our society and, hence, is enforceable against the States."<sup>[8]</sup> The State urges, however, that the availability of the federal privilege to a witness in a state inquiry is to be determined according to a less stringent standard than is applicable in a federal proceeding. We disagree. We have held that the guarantees of the First Amendment, <i>Gitlow</i> v. <i>New York, supra</i><i>; </i><i>Cantwell</i> v. <i>Connecticut,</i> <span class="citation" data-id="103355"><a href="/opinion/103355/cantwell-v-connecticut/" aria-description="Citation for case: Cantwell v. Connecticut">310 U. S. 296</a></span>; <i>Louisiana ex rel. Gremillion</i> v. <i>NAACP,</i> <span class="citation" data-id="9422214"><a href="/opinion/106240/louisiana-ex-rel-gremillion-v-national-assn-for-the-advancement-of/" aria-description="Citation for case: Louisiana Ex Rel. Gremillion v. National Ass&#x27;n for the...">366 U. S. 293</a></span>, the prohibition of unreasonable searches and seizures of the Fourth Amendment, <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, and the right to counsel guaranteed by the Sixth Amendment, <i>Gideon</i> v. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra</a></span></i><i>,</i> are all to be enforced against the States under the Fourteenth Amendment according to the same standards that protect those personal rights against federal encroachment. In the coerced confession cases, involving the policies of the privilege itself, there has been no suggestion that a confession might be considered coerced if used in a federal but not a state tribunal. The Court thus has rejected the notion that the Fourteenth Amendment applies to the States only a "watered-down, subjective version of the individual <span class="star-pagination">*11</span> guarantees of the Bill of Rights, "<i>Ohio ex rel. Eaton</i> v. <i>Price,</i> <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#275" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263, 275</a></span> (dissenting opinion). If <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>, and <i>Adamson</i> v. <i>California, supra</i><i>,</i> suggest such an application of the privilege against self-incrimination, that suggestion cannot survive recognition of the degree to which the <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> view of the privilege has been eroded. What is accorded is a privilege of refusing to incriminate one's self, and the feared prosecution may be by either federal or state authorities. <i>Murphy</i> v. <i>Waterfront Comm'n, post,</i> p. 52. It would be incongruous to have different standards determine the validity of a claim of privilege based on the same feared prosecution, depending on whether the claim was asserted in a state or federal court. Therefore, the same standards must determine whether an accused's silence in either a federal or state proceeding is justified.</p>
<p>We turn to the petitioner's claim that the State of Connecticut denied him the protection of his federal privilege. It must be considered irrelevant that the petitioner was a witness in a statutory inquiry and not a defendant in a criminal prosecution, for it has long been settled that the privilege protects witnesses in similar federal inquiries. <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547</a></span>; <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34</a></span>; <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>. We recently elaborated the content of the federal standard in <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span>:</i></p>
<blockquote>"The privilege afforded not only extends to answers that would in themselves support a conviction . . . but likewise embraces those which would furnish a link in the chain of evidence needed to prosecute . . . . [I]f the witness, upon interposing his claim, were required to prove the hazard . . . he would be compelled to surrender the very protection which the privilege is designed to guarantee. To sustain the privilege, it need only be evident from the implications of the question, in the setting in which it is <span class="star-pagination">*12</span> asked, that a responsive answer to the question or an explanation of why it cannot be answered might be dangerous because injurious disclosure could result." <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 486-487</a></span>.</blockquote>
<p>We also said that, in applying that test, the judge must be</p>
<blockquote>" `<i>perfectly clear,</i> from a careful consideration of all the circumstances in the case, that the witness is mistaken, and that the answer[s] <i>cannot possibly</i> have such tendency' to incriminate." <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#488" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 488</a></span>.</blockquote>
<p>The State of Connecticut argues that the Connecticut courts properly applied the federal standards to the facts of this case. We disagree.</p>
<p>The investigation in the course of which petitioner was questioned began when the Superior Court in Hartford County appointed the Honorable Ernest A. Inglis, formerly Chief Justice of Connecticut, to conduct an inquiry into whether there was reasonable cause to believe that crimes, including gambling, were being committed in Hartford County. Petitioner appeared on January 16 and 25, 1961, and in both instances he was asked substantially the same questions about the circumstances surrounding his arrest and conviction for pool selling in late 1959. The questions which petitioner refused to answer may be summarized as follows: (1) for whom did he work on September 11, 1959; (2) who selected and paid his counsel in connection with his arrest on that date and subsequent conviction; (3) who selected and paid his bondsman; (4) who paid his fine; (5) what was the name of the tenant of the apartment in which he was arrested; and (6) did he know John Bergoti. The Connecticut Supreme Court of Errors ruled that the answers to these questions could not tend to incriminate him because the defenses of double jeopardy and the running of the one-year statute of limitations on misdemeanors would defeat any prosecution growing out of his answers to the first <span class="star-pagination">*13</span> five questions. As for the sixth question, the court held that petitioner's failure to explain how a revelation of his relationship with Bergoti would incriminate him vitiated his claim to the protection of the privilege afforded by state law.</p>
<p>The conclusions of the Court of Errors, tested by the federal standard, fail to take sufficient account of the setting in which the questions were asked. The interrogation was part of a wide-ranging inquiry into crime, including gambling, in Hartford. It was admitted on behalf of the State at oral argumentand indeed it is obvious from the questions themselvesthat the State desired to elicit from the petitioner the identity of the person who ran the pool-selling operation in connection with which he had been arrested in 1959. It was apparent that petitioner might apprehend that if this person were still engaged in unlawful activity, disclosure of his name might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted.<sup>[9]</sup></p>
<p>Analysis of the sixth question, concerning whether petitioner knew John Bergoti, yields a similar conclusion. In the context of the inquiry, it should have been apparent to the referee that Bergoti was suspected by the State to be involved in some way in the subject matter of the investigation. An affirmative answer to the question <span class="star-pagination">*14</span> might well have either connected petitioner with a more recent crime, or at least have operated as a waiver of his privilege with reference to his relationship with a possible criminal. See <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/" aria-description="Citation for case: Rogers v. United States">340 U. S. 367</a></span>. We conclude, therefore, that as to each of the questions, it was "evident from the implications of the question, in the setting in which it [was] asked, that a responsive answer to the question or an explanation of why it [could not] be answered might be dangerous because injurious disclosure could result," <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 486-487</a></span>; see <i>Singleton</i> v. <i>United States,</i> <span class="citation" data-id="8922391"><a href="/opinion/8932238/singleton-v-united-states/" aria-description="Citation for case: Singleton v. United States">343 U. S. 944</a></span>.</p>
<p><i>Reversed.</i></p>
<p>While MR. JUSTICE DOUGLAS joins the opinion of the Court, he also adheres to his concurrence in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#345" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 345</a></span>.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE CLARK joins, dissenting.</p>
<p>Connecticut has adjudged this petitioner in contempt for refusing to answer questions in a state inquiry. The courts of the State, whose laws embody a privilege against self-incrimination, refused to recognize the petitioner's claim of privilege, finding that the questions asked him were not incriminatory. This Court now holds the contempt adjudication unconstitutional because, it is decided: (1) the Fourteenth Amendment makes the Fifth Amendment privilege against self-incrimination applicable to the States; (2) the federal standard justifying a claim of this privilege likewise applies to the States; and (3) judged by that standard the petitioner's claim of privilege should have been upheld.</p>
<p>Believing that the reasoning behind the Court's decision carries extremely mischievous, if not dangerous, consequences for our federal system in the realm of criminal <span class="star-pagination">*15</span> law enforcement, I must dissent. The importance of the issue presented and the serious incursion which the Court makes on time-honored, basic constitutional principles justify a full exposition of my reasons.</p>
<p></p>
<h2>I.</h2>
<p>I can only read the Court's opinion as accepting in fact what it rejects in theory: the application to the States, via the Fourteenth Amendment, of the forms of federal criminal procedure embodied within the first eight Amendments to the Constitution. While it is true that the Court deals today with only one aspect of state criminal procedure, and rejects the wholesale "incorporation" of such federal constitutional requirements, the logical gap between the Court's premises and its novel constitutional conclusion can, I submit, be bridged only by the additional premise that the Due Process Clause of the Fourteenth Amendment is a shorthand directive to this Court to pick and choose among the provisions of the first eight Amendments and apply those chosen, freighted with their entire accompanying body of federal doctrine, to law enforcement in the States.</p>
<p>I accept and agree with the proposition that continuing re-examination of the constitutional conception of Fourteenth Amendment "due process" of law is required, and that development of the community's sense of justice may in time lead to expansion of the protection which due process affords. In particular in this case, I agree that principles of justice to which due process gives expression, as reflected in decisions of this Court, prohibit a State, as the Fifth Amendment prohibits the Federal Government, from imprisoning a person <i>solely</i> because he refuses to give evidence which may incriminate him under the laws of the State.<sup>[1]</sup> I do not understand, however, <span class="star-pagination">*16</span> how this process of re-examination, which must refer always to the guiding standard of due process of law, including, of course, reference to the particular guarantees of the Bill of Rights, can be short-circuited by the simple device of incorporating into due process, without critical examination, the whole body of law which surrounds a specific prohibition directed against the Federal Government. The consequence of such an approach to due process as it pertains to the States is inevitably disregard of all relevant differences which may exist between state and federal criminal law and its enforcement. The ultimate result is compelled uniformity, which is inconsistent with the purpose of our federal system and which is achieved either by encroachment on the States' sovereign <span class="star-pagination">*17</span> powers or by dilution in federal law enforcement of the specific protections found in the Bill of Rights.</p>
<p></p>
<h2>II.</h2>
<p>As recently as 1961, this Court reaffirmed that "the Fifth Amendment's privilege against self-incrimination," <i>ante,</i> p. 3, was not applicable against the States. <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>. The question had been most fully explored in <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>. Since 1908, when <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> was decided, this Court has adhered to the view there expressed that "the exemption from compulsory self-incrimination in the courts of the States is not secured by any part of the Federal Constitution," <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#114" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 114</a></span>. <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 285</a></span>; <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#324" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 324</a></span>; <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>; <i>Knapp</i> v. <i>Schweitzer,</i> <span class="citation" data-id="9421673"><a href="/opinion/105741/knapp-v-schweitzer/#374" aria-description="Citation for case: Knapp v. Schweitzer">357 U. S. 371, 374</a></span>; <i><span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">Cohen, supra</a></span></i><i>.</i> Although none of these cases involved a commitment to prison for refusing to incriminate oneself under state law, and they are relevantly distinguishable from this case on that narrow ground,<sup>[2]</sup> it is perfectly clear from them that until today it has been regarded as settled law that the <i>Fifth Amendment</i> privilege did not, by any process of reasoning, apply <i>as such</i> to the States.</p>
<p>The Court suggests that this consistent line of authority has been undermined by the concurrent development of constitutional doctrine in the areas of coerced confessions and search and seizure. This is <i>post facto</i> reasoning at best. Certainly there has been no intimation until now that <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> has been tacitly overruled.</p>
<p>It was in <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi, supra</a></span></i><i>,</i> that this Court first prohibited the use of a coerced confession in a state criminal trial. The petitioners in <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> had been tortured <span class="star-pagination">*18</span> until they confessed. The Court was hardly making an artificial distinction when it said:</p>
<blockquote>". . . [T]he question of the right of the State to withdraw the privilege against self-incrimination is not here involved. The compulsion to which the quoted statements [from <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> and <i><span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Snyder, supra,</a></span></i>] refer is that of the <i>processes of justice</i> by which the accused may be called as a witness and required to testify. <i>Compulsion by torture</i> to extort a confession is a different matter."<sup>[3]</sup> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S., at 285</a></span>. (Emphasis supplied.)</blockquote>
<p>The majority is simply wrong when it asserts that this perfectly understandable distinction "was soon abandoned," <i>ante,</i> pp. 6-7. In none of the cases cited, <i>ante,</i> pp. 7-8, in which was developed the full sweep of the constitutional prohibition against the use of coerced confessions at state trials, was there anything to suggest that the Fifth Amendment was being made applicable to state proceedings. In <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, the privilege against self-incrimination is not mentioned. The relevant question before the Court was whether "the evidence [of coercion] requires that we set aside the finding of two courts and a jury, and adjudge the admission of the confessions so fundamentally unfair, so contrary to the common concept of ordered liberty, as to amount to a taking of life without due process of law." <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#238" aria-description="Citation for case: Lisenba v. California"><i>Id.,</i> at 238</a></span>. The question was the same in <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; the Court there adverted to the "third degree," <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#150" aria-description="Citation for case: Ashcraft v. Tennessee"><i>e. g., id.,</i> at 150, note 5</a></span>, and "secret inquisitorial practices," <span class="star-pagination">*19</span> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#152" aria-description="Citation for case: Ashcraft v. Tennessee"><i>id.,</i> at 152</a></span>. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>, is the same; the privilege against self-incrimination is not mentioned.<sup>[4]</sup> So too in <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>; and <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>. Finally, in <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, although the Court did recognize that "ours is an accusatorial and not an inquisitorial system," <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond"><i>id.,</i> at 541</a></span>, it is clear that the Court was concerned only with the problem of coerced confessions, see <i>ibid.;</i> the opinion includes nothing to support the Court's assertion here, <i>ante,</i> p. 7, that "the Fifth Amendment privilege is . . . [the] essential mainstay" of our system.</p>
<p>In <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson, supra,</a></span></i> the Court made it explicit that it did not regard the increasingly strict standard for determining the admissibility at trial of an out-of-court confession as undermining the holding of <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>.</i> After stating that "the due process clause does not protect, by virtue of its mere existence, the accused's freedom from giving testimony by compulsion in state trials that is secured to him against federal interference by the Fifth Amendment," the Court said: "The due process clause forbids compulsion to testify by fear of hurt, torture or exhaustion. It forbids any other type of coercion that falls within the scope of due process." <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S., at 54</a></span> <span class="star-pagination">*20</span> (footnotes omitted). Plainly, the Court regarded these two lines of cases as distinct. See also <i>Palko</i> v. <i>Connecticut, supra,</i> at 326, to the same effect.<sup>[5]</sup><i><span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">Cohen, supra,</a></span></i> which adhered to <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> was decided after all but a few of the confession cases which the Court mentions.</p>
<p>The coerced confession cases are relevant to the problem of this case not because they overruled <i>Twining sub silentio,</i> but rather because they applied the same standard of fundamental fairness which is applicable here. The recognition in them that federal supervision of state criminal procedures must be directly based on the requirements of due process is entirely inconsistent with the theory here espoused by the majority. The parallel treatment of federal and state cases involving coerced confessions resulted from the fact that the same demand of due process was applicable in both; it was not the consequence of the automatic engrafting of federal law construing constitutional provisions inapplicable to the States onto the Fourteenth Amendment.</p>
<p>The decision in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, that evidence unconstitutionally seized, see <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 28</a></span>, may not be used in a state criminal trial furnishes no "fortification," see <i>ante,</i> p. 8, for today's decision. The very passage from the <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> opinion which the Court quotes, <i>ante,</i> p. 9, makes explicit the distinct bases of the exclusionary rule as applied in federal and state courts:</p>
<blockquote>"We find that, as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an `intimate relation' <span class="star-pagination">*21</span> in their perpetuation of `principles of humanity and civil liberty [secured] . . . only after years of struggle,' <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span> (1897)." <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656-657</a></span> (footnote omitted). See also <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio"><i>id.,</i> at 655</a></span>.</blockquote>
<p>Although the Court discussed <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, a federal case involving both the Fourth and Fifth Amendments, nothing in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> supports the statement, <i>ante,</i> p. 8, that the Fifth Amendment was part of the basis for extending the exclusionary rule to the States. The elaboration of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, did in my view make the Fourth Amendment applicable to the States through the Fourteenth; but there is nothing in it to suggest that the Fifth Amendment went along as baggage.</p>
<p></p>
<h2>III.</h2>
<p>The previous discussion shows that this Court's decisions do not dictate the "incorporation" of the Fifth Amendment's privilege against self-incrimination into the Fourteenth Amendment. Approaching the question more broadly, it is equally plain that the line of cases exemplified by <i>Palko</i> v. <i>Connecticut, supra</i><i>,</i> in which this Court has reconsidered the requirements which the Due Process Clause imposes on the States in the light of current standards, furnishes no general theoretical framework for what the Court does today.</p>
<p>The view of the Due Process Clause of the Fourteenth Amendment which this Court has consistently accepted and which has "thus far prevailed," <i>ante,</i> p. 4, is that its requirements are as "old as a principle of civilized government," <i>Munn</i> v. <i>Illinois,</i> <span class="citation" data-id="9417073"><a href="/opinion/89446/munn-v-illinois/#123" aria-description="Citation for case: Munn v. Illinois">94 U. S. 113, 123</a></span>, the specific applications of which must be ascertained "by the gradual process of judicial inclusion and exclusion . . . ," <i>Davidson</i> v. <i>New Orleans,</i> <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/#104" aria-description="Citation for case: Davidson v. New Orleans">96 U. S. 97, 104</a></span>. Due process requires "observance of those general rules established in our system of jurisprudence for the security of private <span class="star-pagination">*22</span> rights." <i>Hagar</i> v. <i>Reclamation District No. 108,</i> <span class="citation" data-id="91153"><a href="/opinion/91153/hagar-v-reclamation-district-no-108/#708" aria-description="Citation for case: Hagar v. Reclamation District No. 108">111 U. S. 701, 708</a></span>. See <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#537" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 537</a></span>.</p>
<blockquote>"This court has never attempted to define with precision the words `due process of law' . . . . It is sufficient to say that there are certain immutable principles of justice which inhere in the very idea of free government which no member of the Union may disregard . . . ." <i>Holden</i> v. <i>Hardy,</i> <span class="citation" data-id="94828"><a href="/opinion/94828/holden-v-hardy/#389" aria-description="Citation for case: Holden v. Hardy">169 U. S. 366, 389</a></span>.</blockquote>
<p>It followed from this recognition that due process encompassed the fundamental safeguards of the individual against the abusive exercise of governmental power that some of the restraints on the Federal Government which were specifically enumerated in the Bill of Rights applied also against the States. But, while inclusion of a particular provision in the Bill of Rights might provide historical evidence that the right involved was traditionally regarded as fundamental, inclusion of the right in due process was otherwise entirely independent of the first eight Amendments:</p>
<blockquote>". . . [I]t is possible that some of the personal rights safeguarded by the first eight Amendments against National action may also be safeguarded against state action, because a denial of them would be a denial of due process of law. . . . <i>If this is so, it is not because those rights are enumerated in the first eight Amendments, but because they are of such a nature that they are included in the conception of due process of law.</i>" <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#99" aria-description="Citation for case: Twining v. New Jersey"><i>Twining, supra,</i> at 99</a></span>. (Emphasis supplied.)</blockquote>
<p>Relying heavily on <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> Mr. Justice Cardozo provided what may be regarded as a classic expression of this approach in <i>Palko</i> v. <i>Connecticut, supra</i><i>.</i> After considering a number of individual rights (including the right <span class="star-pagination">*23</span> not to incriminate oneself) which were "not of the very essence of a scheme of ordered liberty," <i>id.,</i> at 325, he said:</p>
<blockquote>"We reach a different plane of social and moral values when we pass to the privileges and immunities that have been taken over from the earlier articles of the federal bill of rights and brought within the Fourteenth Amendment by a process of absorption. These in their origin were effective against the federal government alone. If the Fourteenth Amendment has absorbed them, the process of absorption has had its source in the belief that neither liberty nor justice would exist if they were sacrificed." <i>Id.,</i> at 326.</blockquote>
<p>Further on, Mr. Justice Cardozo made the independence of the Due Process Clause from the provisions of the first eight Amendments explicit:</p>
<blockquote>"Fundamental . . . in the concept of due process, and so in that of liberty, is the thought that condemnation shall be rendered only after trial. <i>Scott</i> v. <i>McNeal,</i> <span class="citation" data-id="93930"><a href="/opinion/93930/scott-v-mcneal/" aria-description="Citation for case: Scott v. McNeal">154 U. S. 34</a></span>; <i>Blackmer</i> v. <i>United States,</i> <span class="citation" data-id="101836"><a href="/opinion/101836/blackmer-v-united-states/" aria-description="Citation for case: Blackmer v. United States">284 U. S. 421</a></span>. The hearing, moreover, must be a real one, not a sham or a pretense. <i>Moore</i> v. <i>Dempsey,</i> <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span>; <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>. For that reason, ignorant defendants in a capital case were held to have been condemned unlawfully when in truth, though not in form, they were refused the aid of counsel. <i>Powell</i> v. <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#67" aria-description="Citation for case: Powell v. Alabama"><i>Alabama, supra,</i> pp. 67, 68</a></span>. The decision did not turn upon the fact that the benefit of counsel would have been guaranteed to the defendants by the provisions of the Sixth Amendment if they had been prosecuted in a federal court. The decision turned upon the fact that in the particular situation laid before us in the evidence the benefit of counsel was essential to the substance of a hearing." <i>Id.,</i> at 327.</blockquote>
<p><span class="star-pagination">*24</span> It is apparent that Mr. Justice Cardozo's metaphor of "absorption" was <i>not</i> intended to suggest the transplantation of case law surrounding the specifics of the first eight Amendments to the very different soil of the Fourteenth Amendment's Due Process Clause. For, as he made perfectly plain, what the Fourteenth Amendment requires of the States does not basically depend on what the first eight Amendments require of the Federal Government.</p>
<p>Seen in proper perspective, therefore, the fact that First Amendment protections have generally been given equal scope in the federal and state domains or that in some areas of criminal procedure the Due Process Clause demands as much of the States as the Bill of Rights demands of the Federal Government, is only tangentially relevant to the question now before us. It is toying with constitutional principles to assert that the Court has "rejected the notion that the Fourteenth Amendment applies to the states only a `watered-down, subjective version of the individual guarantees of the Bill of Rights,' " <i>ante,</i> pp. 10-11. What the Court has, with the single exception of the <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> case, <i>supra,</i> p. 21; see <i>infra,</i> p. 26, consistently rejected is the notion that the Bill of Rights, as such, applies to the States in any aspect at all.</p>
<p>If one attends to those areas to which the Court points, <i>ante,</i> p. 10, in which the prohibitions against the state and federal governments have moved in parallel tracks, the cases in fact reveal again that the Court's usual approach has been to ground the prohibitions against state action squarely on due process, without intermediate reliance on any of the first eight Amendments. Although more recently the Court has referred to the First Amendment to describe the protection of free expression against state infringement, earlier cases leave no doubt that such references are "shorthand" for doctrines developed by another <span class="star-pagination">*25</span> route. In <i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#666" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652, 666</a></span>, for example, the Court said:</p>
<blockquote>"For present purposes we may and do assume that freedom of speech and of the presswhich are protected by the First Amendment from abridgment by Congressare among the fundamental personal rights and `liberties' protected by the due process clause of the Fourteenth Amendment from impairment by the States."</blockquote>
<p>The Court went on to consider the extent of those freedoms in the context of state interests. Mr. Justice Holmes, in dissent, said:</p>
<blockquote>"The general principle of free speech, it seems to me, must be taken to be included in the Fourteenth Amendment, in view of the scope that has been given to the word `liberty' as there used, although perhaps it may be accepted with a somewhat larger latitude of interpretation than is allowed to Congress by the sweeping language that governs or ought to govern the laws of the United States." <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#672" aria-description="Citation for case: Gitlow v. New York"><i>Id.,</i> at 672</a></span>.</blockquote>
<p>Chief Justice Hughes, in <i>De Jonge</i> v. <i>Oregon,</i> <span class="citation" data-id="102728"><a href="/opinion/102728/de-jonge-v-oregon/#364" aria-description="Citation for case: De Jonge v. Oregon">299 U. S. 353, 364</a></span>, gave a similar analysis:</p>
<blockquote>"Freedom of speech and of the press are fundamental rights which are safeguarded by the due process clause of the Fourteenth Amendment of the Federal Constitution. . . . The right of peaceable assembly is a right cognate to those of free speech and free press and is equally fundamental. As this Court said in <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>, 552: `The very idea of a government, republican in form, implies a right on the part of its citizens to meet peaceably for consultation in respect to public affairs and to petition for a redress of grievances.' The First Amendment of the Federal Constitution expressly guarantees that right against abridgment <span class="star-pagination">*26</span> by Congress. But explicit mention there does not argue exclusion elsewhere. For the right is one that cannot be denied without violating those fundamental principles of liberty and justice which lie at the base of all civil and political institutions,principles which the Fourteenth Amendment embodies in the general terms of its due process clause."</blockquote>
<p>The coerced confession and search and seizure cases have already been considered. The former, decided always directly on grounds of fundamental fairness, furnish no support for the Court's present views. <i>Ker</i> v. <i>California, supra</i><i>,</i> did indeed incorporate the Fourth Amendment's protection against invasions of privacy into the Due Process Clause. But that case should be regarded as the exception which proves the rule.<sup>[6]</sup> The right to counsel in state criminal proceedings, which this Court assured in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, does not depend on the Sixth Amendment. In <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#462" aria-description="Citation for case: Betts v. Brady">316 U. S. 455, 462</a></span>, this Court had said:</p>
<blockquote>"Due process of law is secured against invasion by the federal Government by the Fifth Amendment, and is safeguarded against state action in identical words by the Fourteenth. The phrase formulates a concept less rigid and more fluid than those envisaged in other specific and particular provisions of the Bill of Rights. Its application is less a matter of rule. Asserted denial is to be tested by an appraisal of the totality of facts in a given case. That which may, in one setting, constitute a denial of fundamental fairness, shocking to the universal sense of justice, may, in other circumstances, and in the light of other considerations, fall short of such denial." (Footnote omitted.)</blockquote>
<p><span class="star-pagination">*27</span> Although <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Gideon</a></span></i> overruled <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Betts</a></span>,</i> the constitutional approach in both cases was the same. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Gideon</a></span></i> was based on the Court's conclusion, contrary to that reached in <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Betts</a></span>,</i> that the appointment of counsel for an indigent criminal defendant <i>was</i> essential to the conduct of a fair trial, and was therefore part of due process. 372 U. S., at 342-345.</p>
<p>The Court's approach in the present case is in fact nothing more or less than "incorporation" in snatches. If, however, the Due Process Clause <i>is</i> something more than a reference to the Bill of Rights and protects only those rights which derive from fundamental principles, as the majority purports to believe, it is just as contrary to precedent and just as illogical to incorporate the provisions of the Bill of Rights one at a time as it is to incorporate them all at once.</p>
<p></p>
<h2>IV.</h2>
<p>The Court's undiscriminating approach to the Due Process Clause carries serious implications for the sound working of our federal system in the field of criminal law.</p>
<p>The Court concludes, almost without discussion, that "the same standards must determine whether an accused's silence in either a federal or state proceeding is justified," <i>ante,</i> p. 11. About all that the Court offers in explanation of this conclusion is the observation that it would be "incongruous" if different standards governed the assertion of a privilege to remain silent in state and federal tribunals. Such "incongruity," however, is at the heart of our federal system. The powers and responsibilities of the state and federal governments are not congruent; under our Constitution, they are not intended to be. Why should it be thought, as an <i>a priori</i> matter, that limitations on the investigative power of the States are in all respects identical with limitations on the investigative power of the Federal Government? This certainly <span class="star-pagination">*28</span> does not follow from the fact that we deal here with constitutional requirements; for the provisions of the Constitution which are construed are different.</p>
<p>As the Court pointed out in <i>Abbate</i> v. <i>United States,</i> <span class="citation" data-id="9421783"><a href="/opinion/105860/abbate-v-united-states/#195" aria-description="Citation for case: Abbate v. United States">359 U. S. 187, 195</a></span>, "the States under our federal system have the principal responsibility for defining and prosecuting crimes." The Court endangers this allocation of responsibility for the prevention of crime when it applies to the States doctrines developed in the context of federal law enforcement, without any attention to the special problems which the States as a group or particular States may face. If the power of the States to deal with local crime is unduly restricted, the likely consequence is a shift of responsibility in this area to the Federal Government, with its vastly greater resources. Such a shift, if it occurs, may in the end serve to weaken the very liberties which the Fourteenth Amendment safeguards by bringing us closer to the monolithic society which our federalism rejects. Equally dangerous to our liberties is the alternative of watering down protections against the Federal Government embodied in the Bill of Rights so as not unduly to restrict the powers of the States. The dissenting opinion in <i>Aguilar</i> v. <i>Texas, post,</i> p. 116, evidences that this danger is not imaginary. See my concurring opinion in <i>Aguilar, <span class="citation" data-id="9421783"><a href="/opinion/105860/abbate-v-united-states/" aria-description="Citation for case: Abbate v. United States">ibid.</a></span></i></p>
<p>Rather than insisting, almost by rote, that the Connecticut court, in considering the petitioner's claim of privilege, was required to apply the "federal standard," the Court should have fulfilled its responsibility under the Due Process Clause by inquiring whether the proceedings below met the demands of fundamental fairness which due process embodies. Such an approach may not satisfy those who see in the Fourteenth Amendment a set of easily applied "absolutes" which can afford a haven from unsettling doubt. It is, however, truer to the spirit which requires this Court constantly to re-examine fundamental <span class="star-pagination">*29</span> principles and at the same time enjoins it from reading its own preferences into the Constitution.</p>
<p>The Connecticut Supreme Court of Errors gave full and careful consideration to the petitioner's claim that he would incriminate himself if he answered the questions put to him. It noted that its decisions "from a time antedating the adoption of . . . [the Connecticut] constitution in 1818" had upheld a privilege to refuse to answer incriminating questions. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#223" aria-description="Citation for case: Malloy v. Hogan">150 Conn. 220, 223</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#746" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d 744, 746</a></span>. Stating that federal cases treating the Fifth Amendment privilege had "persuasive force" in interpreting its own constitutional provision, and citing <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>, in particular, the Supreme Court of Errors described the requirements for assertion of the privilege by quoting from one of its own cases, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#225" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 225</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 747</a></span>:</p>
<blockquote>"[A] witness . . . has the right to refuse to answer any question which would tend to incriminate him. But a mere claim on his part that the evidence will tend to incriminate him is not sufficient. . . . [He having] made his claim, it is then . . . [necessary for the judge] to determine in the exercise of a legal discretion whether, from the circumstances of the case and the nature of the evidence which the witness is called upon to give, there is reasonable ground to apprehend danger of criminal liability from his being compelled to answer. That danger `must be real and appreciable, with reference to the ordinary operation of law in the ordinary course of things not a danger of an imaginary and unsubstantial character, having reference to some extraordinary and barely possible contingency, so improbable that no reasonable man would suffer it to influence his conduct. We think that a merely remote and naked possibility, out of the ordinary course of law and such as no reasonable man would be affected by, <span class="star-pagination">*30</span> should not be suffered to obstruct the administration of justice. The object of the law is to afford to a party, called upon to give evidence in a proceeding <i>inter alios,</i> protection against being brought by means of his own evidence within the penalties of the law. But it would be to convert a salutary protection into a means of abuse if it were to be held that a mere imaginary possibility of danger, however remote and improbable, was sufficient to justify the withholding of evidence essential to the ends of justice.' Cockburn, C. J., in <i>Regina</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 330 . . . ." <i>McCarthy</i> v. <i>Clancy,</i> <span class="citation" data-id="3321596"><a href="/opinion/3326204/mccarthy-v-clancy/#488" aria-description="Citation for case: McCarthy v. Clancy">110 Conn. 482, 488-489</a></span>, <span class="citation" data-id="3321596"><a href="/opinion/3326204/mccarthy-v-clancy/#555" aria-description="Citation for case: McCarthy v. Clancy">148 A. 551, 555</a></span>.</blockquote>
<p>The court carefully applied the above standard to each question which the petitioner was asked. It dealt first with the question whether he knew John Bergoti. The court said:</p>
<blockquote>"Bergoti is nowhere described or in any way identified, either as to his occupation, actual or reputed, or as to any criminal record he may have had. . . . Malloy made no attempt even to suggest to the court how an answer to the question whether he knew Bergoti could possibly incriminate him. . . . On this state of the record the question was proper, and Malloy's claim of privilege, made without explanation, was correctly overruled. Malloy 'chose to keep the door tightly closed and to deny the court the smallest glimpse of the danger he apprehended. He cannot then complain that we see none.' <i>In re Pillo,</i> 11 N. J. 8, 22, <span class="citation" data-id="2335877"><a href="/opinion/2335877/in-re-pillo/" aria-description="Citation for case: In Re Pillo">93 A. 2d 176</a></span> . . . ." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#226" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 226-227</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748</a></span>.</blockquote>
<p>The remaining questions are summarized in the majority's opinion, <i>ante,</i> p. 12. All of them deal with the circumstances surrounding the petitioner's conviction on a gambling charge in 1959. The court declined to decide <span class="star-pagination">*31</span> "whether, on their face and apart from any consideration of Malloy's immunity from prosecution, the questions should or should not have been answered in the light of his failure to give any hint of explanation as to how answers to them could incriminate him." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#227" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 227</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748</a></span>. The court considered the State's claim that the petitioner's prior conviction was sufficient to clothe him with immunity from prosecution for other crimes to which the questions might pertain, but declined to rest its decision on that basis. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#227" aria-description="Citation for case: Malloy v. Hogan"><i>Id.,</i> at 227-229</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748-749</a></span>. The court concluded, however, that the running of the statute of limitations on misdemeanors committed in 1959 and the absence of any indication that Malloy had engaged in any crime other than a misdemeanor removed all appearance of danger of incrimination from the questions propounded concerning the petitioner's activities in 1959. The court summarized this conclusion as follows:</p>
<blockquote>"In all this, Malloy confounds vague and improbable possibilities of prosecution with reasonably appreciable ones. Under claims like his, it would always be possible to work out some finespun and improbable theory from which an outside chance of prosecution could be envisioned. Such claims are not enough to support a claim of privilege, at least where, as here, a witness suggests no rational explanation of his fears of incrimination, and the questions themselves, under all the circumstances, suggest none." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#230" aria-description="Citation for case: Malloy v. Hogan"><i>Id.,</i> at 230-231</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#750" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 750</a></span>.</blockquote>
<p>Peremptorily rejecting all of the careful analysis of the Connecticut court, this Court creates its own "finespun and improbable theory" about how these questions might have incriminated the petitioner. With respect to his acquaintance with Bergoti, this Court says only:</p>
<blockquote>"In the context of the inquiry, it should have been apparent to the referee that Bergoti was suspected <span class="star-pagination">*32</span> by the State to be involved in some way in the subject matter of the investigation. An affirmative answer to the question might well have either connected petitioner with a more recent crime, or at least have operated as a waiver of his privilege with reference to his relationship with a possible criminal." <i>Ante,</i> pp. 13-14.</blockquote>
<p>The other five questions, treated at length in the Connecticut court's opinion, get equally short shrift from this Court; it takes the majority, unfamiliar with Connecticut law and far removed from the proceedings below, only a dozen lines to consider the questions and conclude that they were incriminating:</p>
<blockquote>"The interrogation was part of a wide-ranging inquiry into crime, including gambling, in Hartford. It was admitted on behalf of the State at oral argument and indeed it is obvious from the questions themselvesthat the State desired to elicit from the petitioner the identity of the person who ran the pool-selling operation in connection with which he had been arrested in 1959. It was apparent that petitioner might apprehend that if this person were still engaged in unlawful activity, disclosure of his name might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted." (Footnote omitted.) <i>Ante,</i> p. 13.</blockquote>
<p>I do not understand how anyone could read the opinion of the Connecticut court and conclude that the state law which was the basis of its decision or the decision itself was lacking in fundamental fairness. The truth of the matter is that under any standardstate or federalthe commitment for contempt was proper. Indeed, as indicated above, there is every reason to believe that the Connecticut court did apply the <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span></i> standard <span class="star-pagination">*33</span> quoted approvingly in the majority's opinion. I entirely agree with my Brother WHITE, <i>post,</i> pp. 36-38, that if the matter is viewed only from the standpoint of the federal standard, such standard was fully satisfied. The Court's reference to a federal standard is, to put it bluntly, simply an excuse for the Court to substitute its own superficial assessment of the facts and state law for the careful and better informed conclusions of the state court. No one who scans the two opinions with an objective eye will, I think, reach any other conclusion.</p>
<p>I would affirm.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p></p>
<h2>I.</h2>
<p>The Fifth Amendment safeguards an important complex of values, but it is difficult for me to perceive how these values are served by the Court's holding that the privilege was properly invoked in this case. While purporting to apply the prevailing federal standard of incrimination the same standard of incrimination that the Connecticut courts appliedthe Court has all but stated that a witness' invocation of the privilege to any question is to be automatically, and without more, accepted. With deference, I prefer the rule permitting the judge rather than the witness to determine when an answer sought is incriminating.</p>
<p>The established rule has been that the witness' claim of the privilege is not final, for the privilege qualifies a citizen's general duty of disclosure only when his answers would subject him to danger from the criminal law. The privilege against self-incrimination or any other evidentiary privilege does not protect silence which is solely an expression of political protest, a desire not to inform, a fear of social obloquy or economic disadvantage or fear of prosecution for future crimes. <i>Smith</i> v. <i>United States,</i> <span class="star-pagination">*34</span> <span class="citation" data-id="104675"><a href="/opinion/104675/smith-v-united-states/#147" aria-description="Citation for case: Smith v. United States">337 U. S. 137, 147</a></span>; <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#605" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 605</a></span>. If the general duty to testify when subpoenaed is to remain and the privilege is to be retained as a protection against compelled incriminating answers, the trial judge must be permitted to make a meaningful determination of when answers tend to incriminate. See <i>The Queen</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 329-330 (1861); <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. I do not think today's decision permits such a determination.</p>
<p>Answers which would furnish a lead to other evidence needed to prosecute or convict a claimant of a crime clue evidencecannot be compelled, but "this protection must be confined to instances where the witness has reasonable cause to apprehend danger from a direct answer." <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, at 486</a></span>; <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. Of course the witness is not required to disclose so much of the danger as to render his privilege nugatory. But that does not justify a flat rule of no inquiry and automatic acceptance of the claim of privilege. In determining whether the witness has a reasonable apprehension, the test in the federal courts has been that the judge is to decide from the circumstances of the case, his knowledge of matters surrounding the inquiry and the nature of the evidence which is demanded from the witness. <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>; <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. Cf. <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/" aria-description="Citation for case: Rogers v. United States">340 U. S. 367</a></span>. This rule seeks and achieves a workable accommodation between what are obviously important competing interests. As Mr. Chief Justice Marshall said: "The principle which entitles the United States to the testimony of every citizen, and the principle by which every witness is privileged not to accuse himself, can neither of them be entirely disregarded. . . . When a question is propounded, it belongs to the court to consider and to decide whether any direct answer to it can implicate the witness." <i>In</i> <span class="star-pagination">*35</span> <i>re Willie,</i> 25 Fed. Cas. No. 14,692e, at 39-40. I would not only retain this rule but apply it in its present form. Under this test, Malloy's refusals to answer some, if not all, of the questions put to him were clearly not privileged.</p>
<p></p>
<h2>II.</h2>
<p>In November 1959, Malloy was arrested in a gambling raid in Hartford and was convicted of pool selling, an offense defined as occupying and keeping a building containing gambling apparatus. After a 90-day jail term, his one-year sentence was suspended and Malloy was placed on probation for two years. In early 1961, Malloy was summoned to appear in an investigation into whether crimes, including gambling, had been committed in Hartford County, and was asked various questions obviously and solely designed to ascertain who Malloy's associates were in connection with his pool-selling activities in Hartford in 1959. Malloy initially refused to answer virtually all the questions put to him, including such innocuous ones as whether he was the William Malloy arrested and convicted of pool selling in 1959. After he was advised to consult with counsel and did so, he declined to answer each one of the following questions on the ground that it would tend to incriminate him:</p>
<blockquote>"Q. Now, on September 11, 1959, when you were arrested at 600 Asylum Street, and the same arrest for which you were convicted in the Superior Court on November 5, 1959, for whom were you working?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. On September 11, 1959, when you were arrested, and the same arrest for which you were convicted in the Superior Court on November 5, 1959, who furnished the money to pay your fine when you were convicted in the Superior Court?</blockquote>
<blockquote>.....</blockquote>
<blockquote>
<span class="star-pagination">*36</span> "Q. After your arrest on September 11, 1959, and the same arrest for which you were convicted on November 5, 1959, who selected your bondsman?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. As a result of your arrest on September 11, 1959, and the same arrest for which you were convicted on November 5, 1959, who furnished the money to pay your fine?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Do you know whose apartment it was [that you were arrested in on September 11, 1959]?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Do you know John Bergoti?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. I ask you again, Mr. Malloy, now, so there will be no misunderstanding of what I want to know. When you were arrested on September 11, 1959, at 600 Asylum Street in Hartford, and the same arrest for which you were convicted in Superior Court on November 5, 1959, for whom were you working?"</blockquote>
<p>It was for refusing to answer these questions that Malloy was cited for contempt, the Connecticut courts noting that the privilege does not protect one against informing on friends or associates.</p>
<p>These were not wholly innocuous questions on their face, but they clearly were in light of the finding, of which Malloy was told, that he was immune from prosecution for any pool-selling activities in 1959. As the Connecticut Supreme Court of Errors found, the State bore its burden of proving that the statute of limitations barred any prosecution for any type of violation of the state pool-selling statute in 1959. Malloy advanced the claim before the Connecticut courts, and again before this Court, that he could perhaps be prosecuted for a conspiracy and that the statute of limitations on a felony was <span class="star-pagination">*37</span> five years. But the Connecticut courts were unable to find any state statute which Malloy's gambling activities in 1959 in Hartford, the subject of the inquiry, could have violated and Malloy has not yet pointed to one. Beyond this Malloy declined to offer any explanation or hint at how the answers sought could have incriminated him. In these circumstances it is wholly speculative to find that the questions about others, not Malloy, posed a substantial hazard of criminal prosecution to Malloy. Theoretically, under some unknown but perhaps possible conditions any fact is potentially incriminating. But if this be the rule, there obviously is no reason for the judge, rather than the witness, to pass on the claim of privilege. The privilege becomes a general one against answering distasteful questions.</p>
<p>The Court finds that the questions were incriminating because petitioner "might apprehend that if [his associates in 1959] were still engaged in unlawful activity, disclosure of [their names] might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted." <i>Ante,</i> p. 13. The assumption necessary to the above reasoning is that all persons, or all who have committed a misdemeanor, are continuously engaged in crime. This is but another way of making the claim of privilege automatic. It is not only unrealistic generally but peculiarly inappropriate in this case. Unlike cases relied on by the Court, like <i>Hoffman</i> v. <i>United States, supra</i><i>,</i> where the claimant was known to be involved in rackets in the area, which were the subject of the inquiry, and had a "broadly published police record," Malloy had no record as a felon. He had engaged once in an unlawful activitypool sellinga misdemeanor and was given a suspended sentence. He had been on probation since that time and was on probation at the time of the inquiry. Again, unlike <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span>,</i> nothing in these questions indicates petitioner <span class="star-pagination">*38</span> was called because he was suspected of criminal activities after 1959. There is no support at all in this record for the cynical assumption that he had committed criminal acts after his release in 1960.</p>
<p>Even on the Court's assumption that persons convicted of a misdemeanor are necessarily suspect criminals, sustaining the privilege in these circumstances is unwarranted, for Malloy placed no reliance on this theory in the courts below or in this Court. In order to allow the judge passing on the claim to understand how the answers sought are incriminating, I would at least require the claimant to state his grounds for asserting the privilege to questions seemingly irrelevant to any incriminating matters.</p>
<p>Adherence to the federal standard of incrimination stated in <i><span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">Mason</a></span></i> and <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman, supra,</a></span></i> in form only, while its content is eroded in application, is hardly an auspicious beginning for application of the privilege to the States. As was well stated in a closely analogous situation, "[t]o continue a rule which is honored by this Court only with lip service is not a healthy thing and in the long run will do disservice to the federal system." <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#351" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, at 351</a></span> (HARLAN, J., concurring).</p>
<p>I would affirm.</p>
<h2>NOTES</h2>
<p>[1]  In both cases the question was whether comment upon the failure of an accused to take the stand in his own defense in a state prosecution violated the privilege. It was assumed, but not decided, in both cases that such comment in a federal prosecution for a federal offense would infringe the provision of the Fifth Amendment that "no person. . . shall be compelled in any criminal case to be a witness against himself." For other statements by the Court that the Fourteenth Amendment does not apply the federal privilege in state proceedings, see <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/#127" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117, 127-129</a></span>; <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>.</p>
<p>[2]  Ten Justices have supported this view. See <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#346" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 346</a></span> (opinion of MR. JUSTICE DOUGLAS). The Court expressed itself as unpersuaded to this view in <i>In re Kemmler,</i> <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#448" aria-description="Citation for case: In Re Kemmler">136 U. S. 436, 448-449</a></span>; <i>McElvaine</i> v. <i>Brush,</i> <span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/#158" aria-description="Citation for case: McElvaine v. Brush">142 U. S. 155, 158-159</a></span>; <i>Maxwell</i> v. <i>Dow,</i> <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/#597" aria-description="Citation for case: Maxwell v. Dow">176 U. S. 581, 597-598</a></span>; <i>Twining</i> v. <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#96" aria-description="Citation for case: Twining v. New Jersey"><i>New Jersey, supra,</i> p. 96</a></span>. See <i>Spies</i> v. <i>Illinois,</i> <span class="citation" data-id="92032"><a href="/opinion/92032/spies-v-illinois/" aria-description="Citation for case: Spies v. Illinois">123 U. S. 131</a></span>. Decisions that particular guarantees were not safeguarded against state action by the Privileges and Immunities Clause or other provision of the Fourteenth Amendment are: <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#551" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542, 551</a></span>; <i>Prudential Ins. Co.</i> v. <i>Cheek,</i> <span class="citation" data-id="100023"><a href="/opinion/100023/prudential-insurance-co-of-america-v-cheek/#543" aria-description="Citation for case: Prudential Insurance Co. of America v. Cheek">259 U. S. 530, 543</a></span> (First Amendment); <i>Presser</i> v. <i>Illinois,</i> <span class="citation" data-id="91528"><a href="/opinion/91528/presser-v-illinois/#265" aria-description="Citation for case: Presser v. Illinois">116 U. S. 252, 265</a></span> (Second Amendment); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span> (Fourth Amendment); <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#538" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 538</a></span> (Fifth Amendment requirement of grand jury indictments); <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#328" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 328</a></span> (Fifth Amendment double jeopardy); <i>Maxwell</i> v. <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/#595" aria-description="Citation for case: Maxwell v. Dow"><i>Dow, supra,</i> at 595</a></span> (Sixth Amendment jury trial); <i>Walker</i> v. <i>Sauvinet,</i> <span class="citation" data-id="89245"><a href="/opinion/89245/walker-v-sauvinet/#92" aria-description="Citation for case: Walker v. Sauvinet">92 U. S. 90, 92</a></span> (Seventh Amendment jury trial); <i>In re <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">Kemmler, supra</a></span></i><i>; </i><i>McElvaine</i> v. <i><span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/" aria-description="Citation for case: McElvaine v. Brush">Brush, supra</a></span></i><i>; </i><i>O'Neil</i> v. <i>Vermont,</i> <span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/#332" aria-description="Citation for case: O&#x27;Neil v. Vermont">144 U. S. 323, 332</a></span> (Eighth Amendment prohibition against cruel and unusual punishment).</p>
<p>[3]  In <i>Barron</i> v. <i>Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span>, decided before the adoption of the Fourteenth Amendment, Chief Justice Marshall, speaking for the Court, held that this right was not secured against state action by the Fifth Amendment's provision: "Nor shall private property be taken for public use, without just compensation."</p>
<p>[4]  <i>E. g., </i><i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#666" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652, 666</a></span> (speech and press); <i>Lovell</i> v. <i>City of Griffin,</i> <span class="citation" data-id="102991"><a href="/opinion/102991/lovell-v-city-of-griffin/#450" aria-description="Citation for case: Lovell v. City of Griffin">303 U. S. 444, 450</a></span> (speech and press); <i>New York Times Co.</i> v. <i>Sullivan,</i> <span class="citation" data-id="9422744"><a href="/opinion/106761/new-york-times-co-v-sullivan/" aria-description="Citation for case: New York Times Co. v. Sullivan">376 U. S. 254</a></span> (speech and press); <i>Staub</i> v. <i>City of Baxley,</i> <span class="citation" data-id="9421529"><a href="/opinion/105608/staub-v-city-of-baxley/#321" aria-description="Citation for case: Staub v. City of Baxley">355 U. S. 313, 321</a></span> (speech); <i>Grosjean</i> v. <i>American Press Co.,</i> <span class="citation" data-id="102601"><a href="/opinion/102601/grosjean-v-american-press-co/#244" aria-description="Citation for case: Grosjean v. American Press Co.">297 U. S. 233, 244</a></span> (press); <i>Cantwell</i> v. <i>Connecticut,</i> <span class="citation" data-id="103355"><a href="/opinion/103355/cantwell-v-connecticut/#303" aria-description="Citation for case: Cantwell v. Connecticut">310 U. S. 296, 303</a></span> (religion); <i>De Jonge</i> v. <i>Oregon,</i> <span class="citation" data-id="102728"><a href="/opinion/102728/de-jonge-v-oregon/#364" aria-description="Citation for case: De Jonge v. Oregon">299 U. S. 353, 364</a></span> (assembly); <i>Shelton</i> v. <i>Tucker,</i> <span class="citation" data-id="9422089"><a href="/opinion/106142/shelton-v-tucker/#486" aria-description="Citation for case: Shelton v. Tucker">364 U. S. 479, 486</a></span> (association); <i>Louisiana ex rel. Gremillion</i> v. <i>NAACP,</i> <span class="citation" data-id="9422214"><a href="/opinion/106240/louisiana-ex-rel-gremillion-v-national-assn-for-the-advancement-of/#296" aria-description="Citation for case: Louisiana Ex Rel. Gremillion v. National Ass&#x27;n for the...">366 U. S. 293, 296</a></span> (association); <i>NAACP</i> v. <i>Button,</i> <span class="citation" data-id="9422512"><a href="/opinion/106514/national-assn-for-the-advancement-of-colored-people-v-button/" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">371 U. S. 415</a></span> (association and speech); <i>Brotherhood of Railroad Trainmen</i> v. <i>Virginia ex rel. Virginia State Bar,</i> <span class="citation" data-id="9422774"><a href="/opinion/106803/brotherhood-of-railroad-trainmen-v-virginia-ex-rel-virginia-state-bar/" aria-description="Citation for case: Brotherhood of Railroad Trainmen v. Virginia Ex Rel....">377 U. S. 1</a></span> (association).</p>
<p>[5]  See <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27-28</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span>.</p>
<p>[6]  See also <i>Robinson</i> v. <i>California,</i> <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/#666" aria-description="Citation for case: Robinson v. California">370 U. S. 660, 666</a></span>, which, despite <i>In re <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">Kemmler, supra</a></span></i><i>; </i><i>McElvaine</i> v. <i><span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/" aria-description="Citation for case: McElvaine v. Brush">Brush, supra</a></span></i><i>; </i><i>O'Neil</i> v. <i><span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/" aria-description="Citation for case: O&#x27;Neil v. Vermont">Vermont, supra</a></span></i><i>,</i> made applicable to the States the Eighth Amendment's ban on cruel and unusual punishments.</p>
<p>[7]  <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> had said of the privilege, ". . . any compulsory discovery by extorting the party's oath . . . to convict him of crime . . . is contrary to the principles of a free government. It is abhorrent to the instincts of an Englishman; it is abhorrent to the instincts of an American. It may suit the purposes of despotic power; but it cannot abide the pure atmosphere of political liberty and personal freedom." 116 U. S., at 631-632.
</p>
<p>Dean Griswold has said: "I believe the Fifth Amendment is, and has been through this period of crisis, an expression of the moral striving of the community. It has been a reflection of our common conscience, a symbol of the America which stirs our hearts." The Fifth Amendment Today 73 (1955).</p>
<p>[8]  The brief states further:
</p>
<p>"Underlying the decisions excluding coerced confessions is the implicit assumption that an accused is privileged against incriminating himself, either in the jail house, the grand jury room, or on the witness stand in a public trial. . . .</p>
<p>". . . It is fundamentally inconsistent to suggest, as the Court's opinions now suggest, that the State is entirely free to compel an accused to incriminate himself before a grand jury, or at the trial, but cannot do so in the police station. Frank recognition of the fact that the Due Process Clause prohibits the States from enforcing their laws by compelling the accused to confess, regardless of where such compulsion occurs, would not only clarify the principles involved in confession cases, but would assist the States significantly in their efforts to comply with the limitations placed upon them by the Fourteenth Amendment."</p>
<p>[9]  See <i>Greenberg</i> v. <i>United States,</i> <span class="citation" data-id="8922268"><a href="/opinion/8932115/greenberg-v-united-states/" aria-description="Citation for case: Greenberg v. United States">343 U. S. 918</a></span>, reversing <i>per curiam,</i> <span class="citation" data-id="228036"><a href="/opinion/228036/united-states-v-greenberg/" aria-description="Citation for case: United States v. Greenberg">192 F. 2d 201</a></span>; <i>Singleton</i> v. <i>United States,</i> <span class="citation" data-id="8922391"><a href="/opinion/8932238/singleton-v-united-states/" aria-description="Citation for case: Singleton v. United States">343 U. S. 944</a></span>, reversing <i>per curiam,</i> <span class="citation" data-id="228448"><a href="/opinion/228448/united-states-v-singleton/" aria-description="Citation for case: United States v. Singleton">193 F. 2d 464</a></span>. In <i>United States</i> v. <i>Coffey,</i> <span class="citation" data-id="229980"><a href="/opinion/229980/united-states-v-coffey/" aria-description="Citation for case: United States v. Coffey">198 F. 2d 438</a></span> (C. A. 3d Cir.), cited with approval in <i>Emspak</i> v. <i>United States,</i> <span class="citation" data-id="9421180"><a href="/opinion/105306/emspak-v-united-states/" aria-description="Citation for case: Emspak v. United States">349 U. S. 190</a></span>, the Court of Appeals for the Third Circuit stated:
</p>
<p>"in determining whether the witness really apprehends danger in answering a question, the judge cannot permit himself to be skeptical; rather must he be acutely aware that in the deviousness of crime and its detection incrimination may be approached and achieved by obscure and unlikely lines of inquiry." <span class="citation" data-id="229980"><a href="/opinion/229980/united-states-v-coffey/#440" aria-description="Citation for case: United States v. Coffey">198 F. 2d, at 440-441</a></span>.</p>
<p>[1]  That precise question has not heretofore been decided by this Court. <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>, and the cases which followed it, see <i>infra,</i> p. 17, all involved issues not precisely similar. Although the Court has stated broadly that an individual could "be required to incriminate himself in . . . state proceedings," <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/#127" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117, 127</a></span>, the context in which such statements were made was that the State had in each case recognized the right to remain silent. In <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining, supra,</a></span></i> until now the primary authority, the Court noted that "all the States of the Union have, from time to time, with varying form but uniform meaning, included the privilege in their constitutions, except the States of New Jersey and Iowa, and in those States it is held to be part of the existing law." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#92" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 92</a></span>.
</p>
<p>While I do not believe that the coerced confession cases furnish any basis for incorporating the Fifth Amendment into the Fourteenth, see <i>infra,</i> pp. 17-20, they do, it seems to me, carry an implication that coercion to incriminate oneself, even when under the forms of law, cf. <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 285</a></span>, discussed <i>infra,</i> pp. 17-18, is inconsistent with due process. Since every State already recognizes a privilege against self-incrimination so defined, see VIII Wigmore, Evidence (McNaughton rev. 1961), § 2252, the effect of including such a privilege in due process is only to create the possibility that a federal question, to be decided under the Due Process Clause, would be raised by a State's refusal to accept a claim of the privilege.</p>
<p>[2]  See note <span class="citation" data-id="91153"><a href="/opinion/91153/hagar-v-reclamation-district-no-108/" aria-description="Citation for case: Hagar v. Reclamation District No. 108">1, <i>supra.</i></a></span></p>
<p>[3]  Nothing in the opinion in <i>Brown</i> supports the Court's intimation here, <i>ante,</i> p. 6, that if <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> had not been on the books, reversal of the convictions would have been based on the Fifth Amendment. The Court made it plain in <i>Brown</i> that it regarded the trial use of a confession extracted by torture as on a par with domination of a trial by a mob, see, <i>e. g., </i><i>Moore</i> v. <i>Dempsey,</i> <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span>, where the trial "is a mere pretense," 297 U. S., at 286.</p>
<p>[4]  "And so, when a conviction in a state court is properly here for review, under a claim that a right protected by the Fourteenth Amendment has been denied, the question is not whether the record can be found to disclose an infraction of one of the specific provisions of the first eight amendments. To come concretely to the present case, the question is not whether the record permits a finding, by a tenuous process of psychological assumptions and reasoning, that Malinski by means of a confession was forced to self-incrimination in defiance of the Fifth Amendment. The exact question is whether the criminal proceedings which resulted in his conviction deprived him of the due process of law by which he was constitutionally entitled to have his guilt determined." <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#416" aria-description="Citation for case: Malinski v. New York"><i>Malinski, supra,</i> at 416</a></span> (opinion of Frankfurter, J.).</p>
<p>[5]  In <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson</a></span></i> and <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko, supra,</a></span></i> which adhered to the rule announced in <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining, supra,</a></span></i> the Court cited some of the very cases now relied on by the majority to show that <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> was gradually being eroded. <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#54" aria-description="Citation for case: Adamson v. California">332 U. S., at 54</a></span>, notes 12, 13; <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S., at 325, 326</a></span>.</p>
<p>[6]  Cf. the majority and dissenting opinions in <i>Aguilar</i> v. <i>Texas, post,</i> p. 108.</p>

</div>
```

---
