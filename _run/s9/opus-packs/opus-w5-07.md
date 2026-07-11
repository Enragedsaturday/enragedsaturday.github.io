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

## GROUP: _overhaul2/lake/cases/Hiibel v. Sixth Judicial Dist. Court.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Hiibel v. Sixth Judicial Dist. Court"
type: case
citation: ""
parallel_cite: "542 U.S. 177; 124 S. Ct. 2451; 159 L. Ed. 2d 292; 17 Fla. L. Weekly Fed. S 406; 72 U.S.L.W. 4509"
neutral_cite: 2004 U.S. LEXIS 4385
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hiibel v. Sixth Judicial Dist. Court
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/"
  cluster_id: 136990
  opinion_id: 136990
  identity_checked: true
homes:
  - page: "[[Stop-and-Identify]]"
    role: "Key — Anchor"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key-on (during a valid Terry stop)"
related: ["[[Terry v. Ohio]]", "[[Berkemer v. McCarty]]", "[[Brown v. Texas]]"]
aliases: ["Hiibel v. Sixth Judicial District Court of Nevada", "Hiibel v. Sixth Judicial District Court of Nevada, Humboldt County"]
tags: ["case", "fourth-amendment", "terry-stop", "stop-and-identify", "reasonable-suspicion"]
holding: "A state stop-and-identify law compelling a suspect to give his name during a valid *Terry* stop is consistent with the Fourth Amendment."
lake:
  record_id: Hiibel v. Sixth Judicial Dist. Court
  status: verified
  projected_at: 2026-07-06
---

# Hiibel v. Sixth Judicial Dist. Court

*542 U.S. 177 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy investigating a reported domestic assault found Hiibel standing by a truck and, during a valid *[[Terry v. Ohio|Terry]]* stop, asked him eleven times to identify himself. Hiibel refused each time and was arrested and convicted under a Nevada "stop and identify" statute requiring a person detained on reasonable suspicion to disclose his name.

## Issue
Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *[[Terry v. Ohio|Terry]]* stop is consistent with the Fourth Amendment.

## Rule
Yes. "Obtaining a suspect's name in the course of a Terry stop serves important government interests." — 542 U.S. at 186. ^pin-186

The Court held that "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop." — *Id.* at 187. ^pin-187

Because the request for identity bears an immediate relation to the purpose and demands of the stop, "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures." — *Id.* at 188. ^pin-188

## Application
The deputy's request for Hiibel's name during a *[[Terry v. Ohio|Terry]]* stop based on reasonable suspicion of a domestic assault was a commonsense inquiry reasonably related to the circumstances justifying the stop — investigating the dispute and assessing safety. The Nevada statute did not change the stop's duration or location, so requiring Hiibel to give his name, on pain of arrest, did not contravene the Fourth Amendment.

## Conclusion
Hiibel's conviction did not violate the Fourth Amendment; the judgment was affirmed. A state may require disclosure of one's name during a valid *[[Terry v. Ohio|Terry]]* stop.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hiibel* builds on [[Terry v. Ohio]], confirming that identity questions are a routine and permissible part of a *[[Terry v. Ohio|Terry]]* stop and that a state may attach a criminal sanction to a refusal, so long as the request is reasonably related to the circumstances justifying the stop.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.*, 542 U.S. 177 (2004) — https://www.courtlistener.com/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/ — pinpoints: 186, 187, 188.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5700d94dfa3f4061", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hiibel v. Sixth Judicial Dist. Court"}, "payload": {"all": [{"cite": "542 U.S. 177", "page": "177", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "542"}, {"cite": "124 S. Ct. 2451", "page": "2451", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "159 L. Ed. 2d 292", "page": "292", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "159"}, {"cite": "2004 U.S. LEXIS 4385", "page": "4385", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}, {"cite": "17 Fla. L. Weekly Fed. S 406", "page": "406", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "72 U.S.L.W. 4509", "page": "4509", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "72"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Hiibel v. Sixth Judicial Dist. Court"}}
{"assertion_id": "078ef690290d2162", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-188", "record_id": "Hiibel v. Sixth Judicial Dist. Court"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-188", "pinpoint_status": "slip-only", "quote": "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.", "quote_fidelity": "mismatch", "record_id": "Hiibel v. Sixth Judicial Dist. Court", "star_marker": null}}
{"assertion_id": "1819278ce4fb0e36", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-187", "record_id": "Hiibel v. Sixth Judicial Dist. Court"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-187", "pinpoint_status": "slip-only", "quote": "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop.", "quote_fidelity": "mismatch", "record_id": "Hiibel v. Sixth Judicial Dist. Court", "star_marker": null}}
{"assertion_id": "897c364ec6c648ca", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-186", "record_id": "Hiibel v. Sixth Judicial Dist. Court"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-186", "pinpoint_status": "slip-only", "quote": "statute requiring a person detained on reasonable suspicion to disclose his name. ## Issue Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *Terry* stop is consistent with the Fourth Amendment. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Hiibel v. Sixth Judicial Dist. Court", "star_marker": null}}
{"assertion_id": "76d3a9daaa40bd70", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hiibel v. Sixth Judicial Dist. Court"}, "payload": {"as_of_content": "2004-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hiibel v. Sixth Judicial Dist. Court", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Hiibel v. Sixth Judicial Dist. Court

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hiibel v. Sixth Judicial Dist. Court",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
    "case_name_short": "Hiibel",
    "case_name_full": "HIIBEL v. SIXTH JUDICIAL DISTRICT COURT OF NEVADA, HUMBOLDT COUNTY, Et Al.",
    "input_case_name": "Hiibel v. Sixth Judicial Dist. Court",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-21",
    "year": 2004,
    "docket": null,
    "cluster_id": 136990,
    "lead_opinion_id": 136990,
    "sibling_ids": [
      136990,
      9434645,
      9434646,
      9434647
    ],
    "absolute_url": "/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 177",
        "volume": "542",
        "reporter": "U.S.",
        "page": "177",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2451",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2451",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 292",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4385",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4385",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 406",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "406",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4509",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4509",
        "type": 4,
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
      "id": "pin-186",
      "page": null,
      "quote": "statute requiring a person detained on reasonable suspicion to disclose his name. ## Issue Whether a state stop-and-identify law that compels a suspect to disclose his name during a valid *Terry* stop is consistent with the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-187",
      "page": null,
      "quote": "[t]he principles of Terry permit a State to require a suspect to disclose his name in the course of a Terry stop.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188",
      "page": null,
      "quote": "[a] state law requiring a suspect to disclose his name in the course of a valid Terry stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hiibel v. Sixth Judicial Dist. Court",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 4460263,
          "cite": [
            "2018 Ohio 164",
            "104 N.E.3d 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kareen Rasul Griffin",
          "cluster_id": 809546,
          "cite": [
            "696 F.3d 1354",
            "2012 WL 4496817",
            "2012 U.S. App. LEXIS 20543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Bryant",
          "cluster_id": 2959736,
          "cite": [
            "179 L. Ed. 2d 93",
            "131 S. Ct. 1143",
            "562 U.S. 344",
            "2011 U.S. LEXIS 1713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
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
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koch v. City of Del City",
          "cluster_id": 616534,
          "cite": [
            "660 F.3d 1228",
            "2011 U.S. App. LEXIS 22095",
            "2011 WL 5176164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady, Davy v. Sheahan, Michael",
          "cluster_id": 2999846,
          "cite": [
            "467 F.3d 1057",
            "2006 WL 3113670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hosvaldo Lopez",
          "cluster_id": 797423,
          "cite": [
            "482 F.3d 1067",
            "2007 WL 725641",
            "2007 U.S. App. LEXIS 5709"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pineiro",
          "cluster_id": 1980861,
          "cite": [
            "853 A.2d 887",
            "181 N.J. 13",
            "2004 N.J. LEXIS 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Center for Bio-Ethical Reform, Inc. v. Los Angeles County Sheriff Department",
          "cluster_id": 1235108,
          "cite": [
            "533 F.3d 780",
            "2008 U.S. App. LEXIS 13975",
            "2008 WL 2599683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Kerwick, Stacie Michelle",
          "cluster_id": 2948618,
          "cite": [
            "393 S.W.3d 270",
            "2013 WL 690840",
            "2013 Tex. Crim. App. LEXIS 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Noe",
          "cluster_id": 623700,
          "cite": [
            "672 F.3d 1185",
            "2012 WL 604170",
            "2012 U.S. App. LEXIS 3927"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Arnold",
          "cluster_id": 797722,
          "cite": [
            "486 F.3d 177",
            "73 Fed. R. Serv. 583",
            "2007 U.S. App. LEXIS 11616",
            "2007 WL 1452230"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Waters v. B. Madson",
          "cluster_id": 4609057,
          "cite": [
            "921 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Turner v. Driver",
          "cluster_id": 4349754,
          "cite": [
            "848 F.3d 678",
            "2017 WL 650186",
            "2017 U.S. App. LEXIS 2769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Derrick L. Foster",
          "cluster_id": 787028,
          "cite": [
            "376 F.3d 577",
            "65 Fed. R. Serv. 1",
            "2004 U.S. App. LEXIS 15267",
            "2004 WL 1606725"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. City of New York",
          "cluster_id": 2828542,
          "cite": [
            "798 F.3d 94",
            "2015 U.S. App. LEXIS 14517",
            "2015 WL 4924395"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hiibel v. Sixth Judicial Dist. Court:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEzNDUyODAwMDAwJnM9Mjk5MTYwNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTMmcz0xNDI3ODc4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(136990 OR 9434645 OR 9434646 OR 9434647)",
    "indexed_citing_opinions": 480,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 136990,
        "count": 392,
        "count_source": "search"
      },
      {
        "opinion_id": 9434645,
        "count": 95,
        "count_source": "search"
      },
      {
        "opinion_id": 9434646,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434647,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 890,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hiibel-v-sixth-judicial-dist-court.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NjEyODUmcz05NDI4NDMyJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28136990+OR+9434645+OR+9434646+OR+9434647%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 136990,
        "cited_id": 93149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 108965,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 136990,
        "cited_id": 2621305,
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
    "date_created": "2026-07-05T07:06:13Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:10:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:06:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hiibel v. Sixth Judicial Dist. Court

```
<div>
<center><b><span class="citation" data-id="9434645"><a href="/opinion/136990/hiibel-v-sixth-judicial-dist-court-of-nev-humboldt-cty/" aria-description="Citation for case: Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.">542 U.S. 177</a></span> (2004)</b></center>
<center><h1>HIIBEL<br>
v.<br>
SIXTH JUDICIAL DISTRICT COURT OF NEVADA, HUMBOLDT COUNTY, ET AL.</h1></center>
<center>No. 03-5554.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 22, 2004.</center>
<center>Decided June 21, 2004.</center>
CERTIORARI TO THE SUPREME COURT OF NEVADA.
<p><span class="star-pagination">*178</span> <span class="star-pagination">*179</span> KENNEDY, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and O'CONNOR, SCALIA, and THOMAS, JJ., joined. STEVENS, J., filed a dissenting opinion, <i>post,</i> p. 191. BREYER, J., filed a dissenting opinion, in which SOUTER and GINSBURG, JJ., joined, <i>post,</i> p. 197.</p>
<p><i>Robert E. Dolan</i> argued the cause for petitioner. With him on the briefs were <i>James P. Logan, Jr.,</i> and <i>Harriet E. Cummings.</i></p>
<p><i>Conrad Hafen,</i> Senior Deputy Attorney General of Nevada, argued the cause for respondents. With him on the brief were <i>Brian Sandoval,</i> Attorney General, and <i>David Allison.</i></p>
<p><i>Sri Srinivasan</i> argued the cause for the United States as <i>amicus curiae</i> urging affirmance. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General</i> <span class="star-pagination">*180</span> <i>Wray, Deputy Solicitor General Dreeben,</i> and <i>Joel M. Gershowitz.</i><sup>[*]</sup></p>
<p>JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>The petitioner was arrested and convicted for refusing to identify himself during a stop allowed by <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). He challenges his conviction under the Fourth and Fifth Amendments to the United States Constitution, applicable to the States through the Fourteenth Amendment.</p>
<p></p>
<h2>I</h2>
<p>The sheriff's department in Humboldt County, Nevada, received an afternoon telephone call reporting an assault. The caller reported seeing a man assault a woman in a red and silver GMC truck on Grass Valley Road. Deputy Sheriff Lee Dove was dispatched to investigate. When the officer arrived at the scene, he found the truck parked on the side of the road. A man was standing by the truck, and a young woman was sitting inside it. The officer observed skid marks in the gravel behind the vehicle, leading him to believe it had come to a sudden stop.</p>
<p>The officer approached the man and explained that he was investigating a report of a fight. The man appeared to be <span class="star-pagination">*181</span> intoxicated. The officer asked him if he had "any identification on [him]," which we understand as a request to produce a driver's license or some other form of written identification. The man refused and asked why the officer wanted to see identification. The officer responded that he was conducting an investigation and needed to see some identification. The unidentified man became agitated and insisted he had done nothing wrong. The officer explained that he wanted to find out who the man was and what he was doing there. After continued refusals to comply with the officer's request for identification, the man began to taunt the officer by placing his hands behind his back and telling the officer to arrest him and take him to jail. This routine kept up for several minutes: The officer asked for identification 11 times and was refused each time. After warning the man that he would be arrested if he continued to refuse to comply, the officer placed him under arrest.</p>
<p>We now know that the man arrested on Grass Valley Road is Larry Dudley Hiibel. Hiibel was charged with "willfully resist[ing], delay[ing] or obstruct[ing] a public officer in discharging or attempting to discharge any legal duty of his office" in violation of Nev. Rev. Stat. (NRS) § 199.280 (2003). The government reasoned that Hiibel had obstructed the officer in carrying out his duties under § 171.123, a Nevada statute that defines the legal rights and duties of a police officer in the context of an investigative stop. Section 171.123 provides in relevant part:</p>
<blockquote>"1. Any peace officer may detain any person whom the officer encounters under circumstances which reasonably indicate that the person has committed, is committing or is about to commit a crime.</blockquote>
<blockquote>.   .   .   .   .</blockquote>
<blockquote>"3. The officer may detain the person pursuant to this section only to ascertain his identity and the suspicious circumstances surrounding his presence abroad. Any person so detained shall identify himself, but may not <span class="star-pagination">*182</span> be compelled to answer any other inquiry of any peace officer."</blockquote>
<p>Hiibel was tried in the Justice Court of Union Township. The court agreed that Hiibel's refusal to identify himself as required by § 171.123 "obstructed and delayed Dove as a public officer in attempting to discharge his duty" in violation of § 199.280. App. 5. Hiibel was convicted and fined $250. The Sixth Judicial District Court affirmed, rejecting Hiibel's argument that the application of § 171.123 to his case violated the Fourth and Fifth Amendments. On review the Supreme Court of Nevada rejected the Fourth Amendment challenge in a divided opinion. <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">118 Nev. 868</a></span>, <span class="citation multiple-matches"><a href="/c/P.%203d/59/1201/">59 P. 3d 1201</a></span> (2002). Hiibel petitioned for rehearing, seeking explicit resolution of his Fifth Amendment challenge. The petition was denied without opinion. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./540/965/">540 U. S. 965</a></span> (2003).</p>
<p></p>
<h2>II</h2>
<p>NRS § 171.123(3) is an enactment sometimes referred to as a "stop and identify" statute. See <span class="citation no-link">Ala. Code § 15-5-30</span> (West 2003); <span class="citation no-link">Ark. Code Ann. § 5-71-213</span>(a)(1) (2004); <span class="citation no-link">Colo. Rev. Stat. § 16-3-103</span>(1) (2003); Del. Code Ann., Tit. 11, §§ 1902(a), 1321(6) (2003); <span class="citation no-link">Fla. Stat. § 856.021</span>(2) (2003); <span class="citation no-link">Ga. Code Ann. § 16-11-36</span>(b) (2003); Ill. Comp. Stat., ch. 725, § 5/107-14 (2004); <span class="citation no-link">Kan. Stat. Ann. § 22-2402</span>(1) (2003); La. Code Crim. Proc. Ann., Art. 215.1(A) (West 2004); <span class="citation no-link">Mo. Rev. Stat. § 84.710</span>(2) (2003); <span class="citation no-link">Mont. Code Ann. § 46-5-401</span>(2)(a) (2003); <span class="citation no-link">Neb. Rev. Stat. § 29-829</span> (2003); N. H. Rev. Stat. Ann. §§ 594:2 and 644:6 (Lexis 2003); N. M. Stat. Ann. § 30-22-3 (2004); <span class="citation no-link">N.Y. Crim. Proc. Law § 140.50</span>(1) (West 2004); N. D. Cent. Code § 29-29-21 (2003); R. I. Gen. Laws § 12-7-1 (2003); <span class="citation no-link">Utah Code Ann. § 77-7-15</span> (2003); Vt. Stat. Ann., Tit. 24, § 1983 (Supp. 2003); <span class="citation no-link">Wis. Stat. § 968.24</span> (2003). See also Note, Stop and Identify Statutes: A New Form of an Inadequate Solution to an Old Problem, 12 Rutgers L. J. 585 (1981); Note, Stop-and-Identify Statutes After <i>Kolender v. Lawson:</i> Exploring <span class="star-pagination">*183</span> the Fourth and Fifth Amendment Issues, <span class="citation no-link">69 Iowa L. Rev. 1057</span> (1984).</p>
<p>Stop and identify statutes often combine elements of traditional vagrancy laws with provisions intended to regulate police behavior in the course of investigatory stops. The statutes vary from State to State, but all permit an officer to ask or require a suspect to disclose his identity. A few States model their statutes on the Uniform Arrest Act, a model code that permits an officer to stop a person reasonably suspected of committing a crime and "demand of him his name, address, business abroad and whither he is going." Warner, The Uniform Arrest Act, <span class="citation no-link">28 Va. L. Rev. 315</span>, 344 (1942). Other statutes are based on the text proposed by the American Law Institute as part of the Institute's Model Penal Code. See ALI, Model Penal Code § 250.6, Comment 4, pp. 392-393 (1980). The provision, originally designated § 250.12, provides that a person who is loitering "under circumstances which justify suspicion that he may be engaged or about to engage in crime commits a violation if he refuses the request of a peace officer that he identify himself and give a reasonably credible account of the lawfulness of his conduct and purposes." § 250.12 (Tent. Draft No. 13) (1961). In some States, a suspect's refusal to identify himself is a misdemeanor offense or civil violation; in others, it is a factor to be considered in whether the suspect has violated loitering laws. In other States, a suspect may decline to identify himself without penalty.</p>
<p>Stop and identify statutes have their roots in early English vagrancy laws that required suspected vagrants to face arrest unless they gave "a good Account of themselves," 15 Geo. 2, ch. 5, § 2 (1744), a power that itself reflected common-law rights of private persons to "arrest any suspicious night-walker, and detain him till he give a good account of himself...." 2 W. Hawkins, Pleas of the Crown, ch. 13, § 6, p. 130. (6th ed. 1787). In recent decades, the Court has found constitutional infirmity in traditional vagrancy laws. <span class="star-pagination">*184</span> In <i>Papachristou</i> v. <i>Jacksonville,</i> <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S. 156</a></span> (1972), the Court held that a traditional vagrancy law was void for vagueness. Its broad scope and imprecise terms denied proper notice to potential offenders and permitted police officers to exercise unfettered discretion in the enforcement of the law. See <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/#167" aria-description="Citation for case: Papachristou v. City of Jacksonville"><i>id.,</i> at 167-171</a></span>.</p>
<p>The Court has recognized similar constitutional limitations on the scope and operation of stop and identify statutes. In <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 52</a></span> (1979), the Court invalidated a conviction for violating a Texas stop and identify statute on Fourth Amendment grounds. The Court ruled that the initial stop was not based on specific, objective facts establishing reasonable suspicion to believe the suspect was involved in criminal activity. See <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>id.,</i> at 51-52</a></span>. Absent that factual basis for detaining the defendant, the Court held, the risk of "arbitrary and abusive police practices" was too great and the stop was impermissible. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#52" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 52</a></span>. Four Terms later, the Court invalidated a modified stop and identify statute on vagueness grounds. See <i>Kolender</i> v. <i>Lawson,</i> <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">461 U. S. 352</a></span> (1983). The California law in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> required a suspect to give an officer "`credible and reliable'" identification when asked to identify himself. <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/#360" aria-description="Citation for case: Kolender v. Lawson"><i>Id.,</i> at 360</a></span>. The Court held that the statute was void because it provided no standard for determining what a suspect must do to comply with it, resulting in "`virtually unrestrained power to arrest and charge persons with a violation.'" <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Ibid.</a></span></i> (quoting <i>Lewis</i> v. <i>New Orleans,</i> <span class="citation" data-id="9425601"><a href="/opinion/108965/lewis-v-city-of-new-orleans/#135" aria-description="Citation for case: Lewis v. City of New Orleans">415 U. S. 130, 135</a></span> (1974) (Powell, J., concurring in result)).</p>
<p>The present case begins where our prior cases left off. Here there is no question that the initial stop was based on reasonable suspicion, satisfying the Fourth Amendment requirements noted in <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span>.</i> Further, the petitioner has not alleged that the statute is unconstitutionally vague, as in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span>.</i> Here the Nevada statute is narrower and more precise. The statute in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> had been interpreted to require a suspect to give the officer "credible and reliable" <span class="star-pagination">*185</span> identification. In contrast, the Nevada Supreme Court has interpreted NRS § 171.123(3) to require only that a suspect disclose his name. See <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#875" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">118 Nev., at 875</a></span>, <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#1206" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">59 P. 3d, at 1206</a></span> (opinion of Young, C.J.) ("The suspect is not required to provide private details about his background, but merely to state his name to an officer when reasonable suspicion exists"). As we understand it, the statute does not require a suspect to give the officer a driver's license or any other document. Provided that the suspect either states his name or communicates it to the officer by other means  a choice, we assume, that the suspect may make  the statute is satisfied and no violation occurs. See <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#876" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of..."><i>id.,</i> at 876-877</a></span>, <span class="citation" data-id="8045666"><a href="/opinion/8085804/hiibel-v-sixth-judicial-district-court-of-the-state-of-nevada/#1206" aria-description="Citation for case: Hiibel v. Sixth Judicial District Court of the State of...">59 P. 3d, at 1206-1207</a></span>.</p>
<p></p>
<h2>III</h2>
<p>Hiibel argues that his conviction cannot stand because the officer's conduct violated his Fourth Amendment rights. We disagree.</p>
<p>Asking questions is an essential part of police investigations. In the ordinary course a police officer is free to ask a person for identification without implicating the Fourth Amendment. "[I]nterrogation relating to one's identity or a request for identification by the police does not, by itself, constitute a Fourth Amendment seizure." <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 216</a></span> (1984). Beginning with <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court has recognized that a law enforcement officer's reasonable suspicion that a person may be involved in criminal activity permits the officer to stop the person for a brief time and take additional steps to investigate further. <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado"><i>Delgado, supra,</i> at 216</a></span>; <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975). To ensure that the resulting seizure is constitutionally reasonable, a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop must be limited. The officer's action must be "`justified at its inception, and ... reasonably related in scope to the circumstances which justified the interference in the first place.'" <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>). For example, the seizure cannot <span class="star-pagination">*186</span> continue for an excessive period of time, see <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709</a></span> (1983), or resemble a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 212</a></span> (1979).</p>
<p>Our decisions make clear that questions concerning a suspect's identity are a routine and accepted part of many <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops. See <i>United States</i> v. <i>Hensley,</i> <span class="citation" data-id="9429804"><a href="/opinion/111294/united-states-v-hensley/#229" aria-description="Citation for case: United States v. Hensley">469 U. S. 221, 229</a></span> (1985) ("[T]he ability to briefly stop [a suspect], ask questions, or check identification in the absence of probable cause promotes the strong government interest in solving crimes and bringing offenders to justice"); <i>Hayes</i> v. <i>Florida,</i> <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#816" aria-description="Citation for case: Hayes v. Florida">470 U. S. 811, 816</a></span> (1985) ("[I]f there are articulable facts supporting a reasonable suspicion that a person has committed a criminal offense, that person may be stopped in order to identify him, to question him briefly, or to detain him briefly while attempting to obtain additional information"); <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972) ("A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time").</p>
<p>Obtaining a suspect's name in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop serves important government interests. Knowledge of identity may inform an officer that a suspect is wanted for another offense, or has a record of violence or mental disorder. On the other hand, knowing identity may help clear a suspect and allow the police to concentrate their efforts elsewhere. Identity may prove particularly important in cases such as this, where the police are investigating what appears to be a domestic assault. Officers called to investigate domestic disputes need to know whom they are dealing with in order to assess the situation, the threat to their own safety, and possible danger to the potential victim.</p>
<p>Although it is well established that an officer may ask a suspect to identify himself in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it has been an open question whether the suspect can be arrested <span class="star-pagination">*187</span> and prosecuted for refusal to answer. See <i>Brown,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas">443 U. S., at 53, n. 3</a></span>. Petitioner draws our attention to statements in prior opinions that, according to him, answer the question in his favor. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> Justice White stated in a concurring opinion that a person detained in an investigative stop can be questioned but is "not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 34</a></span>. The Court cited this opinion in dicta in <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984), a decision holding that a routine traffic stop is not a custodial stop requiring the protections of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). In the course of explaining why <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops have not been subject to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court suggested reasons why <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops have a "nonthreatening character," among them the fact that a suspect detained during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop "is not obliged to respond" to questions. See <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty"><i>Berkemer, supra,</i> at 439, 440</a></span>. According to petitioner, these statements establish a right to refuse to answer questions during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop.</p>
<p>We do not read these statements as controlling. The passages recognize that the Fourth Amendment does not impose obligations on the citizen but instead provides rights against the government. As a result, the Fourth Amendment itself cannot require a suspect to answer questions. This case concerns a different issue, however. Here, the source of the legal obligation arises from Nevada state law, not the Fourth Amendment. Further, the statutory obligation does not go beyond answering an officer's request to disclose a name. See NRS § 171.123(3) ("Any person so detained shall identify himself, but may not be compelled to answer any other inquiry of any peace officer"). As a result, we cannot view the dicta in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> or Justice White's concurrence in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> as answering the question whether a State can compel a suspect to disclose his name during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop.</p>
<p>The principles of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> permit a State to require a suspect to disclose his name in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. The reasonableness <span class="star-pagination">*188</span> of a seizure under the Fourth Amendment is determined "by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate government interests." <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979). The Nevada statute satisfies that standard. The request for identity has an immediate relation to the purpose, rationale, and practical demands of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. The threat of criminal sanction helps ensure that the request for identity does not become a legal nullity. On the other hand, the Nevada statute does not alter the nature of the stop itself: it does not change its duration, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 709</a></span>, or its location, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York"><i>Dunaway, supra,</i> at 212</a></span>. A state law requiring a suspect to disclose his name in the course of a valid <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop is consistent with Fourth Amendment prohibitions against unreasonable searches and seizures.</p>
<p>Petitioner argues that the Nevada statute circumvents the probable-cause requirement, in effect allowing an officer to arrest a person for being suspicious. According to petitioner, this creates a risk of arbitrary police conduct that the Fourth Amendment does not permit. Brief for Petitioner 28-33. These are familiar concerns; they were central to the opinion in <i><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">Papachristou</a></span>,</i> and also to the decisions limiting the operation of stop and identify statutes in <i><span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/" aria-description="Citation for case: Kolender v. Lawson">Kolender</a></span></i> and <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Brown</a></span>.</i> Petitioner's concerns are met by the requirement that a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop must be justified at its inception and "reasonably related in scope to the circumstances which justified" the initial stop. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>. Under these principles, an officer may not arrest a suspect for failure to identify himself if the request for identification is not reasonably related to the circumstances justifying the stop. The Court noted a similar limitation in <i><span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/" aria-description="Citation for case: Hayes v. Florida">Hayes</a></span>,</i> where it suggested that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> may permit an officer to determine a suspect's identity by compelling the suspect to submit to fingerprinting only if there is "a reasonable basis for believing that fingerprinting will establish or negate the suspect's connection with that crime." 470 U. S., at 817. It is clear in this case that the <span class="star-pagination">*189</span> request for identification was "reasonably related in scope to the circumstances which justified" the stop. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 20</a></span>. The officer's request was a commonsense inquiry, not an effort to obtain an arrest for failure to identify after a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop yielded insufficient evidence. The stop, the request, and the State's requirement of a response did not contravene the guarantees of the Fourth Amendment.</p>
<p></p>
<h2>IV</h2>
<p>Petitioner further contends that his conviction violates the Fifth Amendment's prohibition on compelled self-incrimination. The Fifth Amendment states that "[n]o person ... shall be compelled in any criminal case to be a witness against himself." To qualify for the Fifth Amendment privilege, a communication must be testimonial, incriminating, and compelled. See <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 34-38</a></span> (2000).</p>
<p>Respondents urge us to hold that the statements NRS § 171.123(3) requires are nontestimonial, and so outside the Clause's scope. We decline to resolve the case on that basis. "[T]o be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information." <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U.S. 201, 210</a></span> (1988). See also <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#35" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 35</a></span>. Stating one's name may qualify as an assertion of fact relating to identity. Production of identity documents might meet the definition as well. As we noted in <i><span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/" aria-description="Citation for case: United States v. Hubbell">Hubbell</a></span>,</i> acts of production may yield testimony establishing "the existence, authenticity, and custody of items [the police seek]." <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#41" aria-description="Citation for case: United States v. Hubbell"><i>Id.,</i> at 41</a></span>. Even if these required actions are testimonial, however, petitioner's challenge must fail because in this case disclosure of his name presented no reasonable danger of incrimination.</p>
<p>The Fifth Amendment prohibits only compelled testimony that is incriminating. See <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#598" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 598</a></span> (1896) (noting that where "the answer of the witness will not directly show his infamy, but only <i>tend</i> to disgrace him, <span class="star-pagination">*190</span> he is bound to answer"). A claim of Fifth Amendment privilege must establish</p>
<blockquote>"`reasonable ground to apprehend danger to the witness from his being compelled to answer . . . . [T]he danger to be apprehended must be real and appreciable, with reference to the ordinary operation of law in the ordinary course of things,  not a danger of an imaginary and unsubstantial character, having reference to some extraordinary and barely possible contingency, so improbable that no reasonable man would suffer it to influence his conduct.'" <i><span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/" aria-description="Citation for case: Brown v. Walker">Id.,</a></span></i> at 599-600 (quoting <i>Queen</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 330, 121 Eng. Rep. 730, 738 (Q. B. 1861) (Cockburn, C. J.)).</blockquote>
<p>As we stated in <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441, 445</a></span> (1972), the Fifth Amendment privilege against compulsory self-incrimination "protects against any disclosures that the witness reasonably believes could be used in a criminal prosecution or could lead to other evidence that might be so used." Suspects who have been granted immunity from prosecution may, therefore, be compelled to answer; with the threat of prosecution removed, there can be no reasonable belief that the evidence will be used against them. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 453</a></span>.</p>
<p>In this case petitioner's refusal to disclose his name was not based on any articulated real and appreciable fear that his name would be used to incriminate him, or that it "would furnish a link in the chain of evidence needed to prosecute" him. <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, 486</a></span> (1951). As best we can tell, petitioner refused to identify himself only because he thought his name was none of the officer's business. Even today, petitioner does not explain how the disclosure of his name could have been used against him in a criminal case. While we recognize petitioner's strong belief that he should not have to disclose his identity, the Fifth <span class="star-pagination">*191</span> Amendment does not override the Nevada Legislature's judgment to the contrary absent a reasonable belief that the disclosure would tend to incriminate him.</p>
<p>The narrow scope of the disclosure requirement is also important. One's identity is, by definition, unique; yet it is, in another sense, a universal characteristic. Answering a request to disclose a name is likely to be so insignificant in the scheme of things as to be incriminating only in unusual circumstances. See <i>Baltimore City Dept. of Social Servs.</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#555" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 555</a></span> (1990) (suggesting that "fact[s] the State could readily establish" may render "any testimony regarding existence or authenticity [of them] insufficiently incriminating"); cf. <i>California</i> v. <i>Byers,</i> <span class="citation" data-id="9424566"><a href="/opinion/108335/california-v-byers/#432" aria-description="Citation for case: California v. Byers">402 U. S. 424, 432</a></span> (1971) (opinion of Burger, C. J.). In every criminal case, it is known and must be known who has been arrested and who is being tried. Cf. <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#601" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 601-602</a></span> (1990) (principal opinion of Brennan, J.). Even witnesses who plan to invoke the Fifth Amendment privilege answer when their names are called to take the stand. Still, a case may arise where there is a substantial allegation that furnishing identity at the time of a stop would have given the police a link in the chain of evidence needed to convict the individual of a separate offense. In that case, the court can then consider whether the privilege applies, and, if the Fifth Amendment has been violated, what remedy must follow. We need not resolve those questions here.</p>
<p>The judgment of the Nevada Supreme Court is <i>Affirmed.</i></p>
<p>JUSTICE STEVENS, dissenting.</p>
<p>The Nevada law at issue in this case imposes a narrow duty to speak upon a specific class of individuals. The class includes only those persons detained by a police officer "under circumstances which reasonably indicate that the person has committed, is committing or is about to commit a <span class="star-pagination">*192</span> crime"<sup>[1]</sup>  persons who are, in other words, targets of a criminal investigation. The statute therefore is directed not "at the public at large," but rather "at a highly selective group inherently suspect of criminal activities." <i>Albertson</i> v. <i>Subversive Activities Control Bd.,</i> <span class="citation" data-id="9423096"><a href="/opinion/107110/albertson-v-subversive-activities-control-board/#79" aria-description="Citation for case: Albertson v. Subversive Activities Control Board">382 U. S. 70, 79</a></span> (1965).</p>
<p>Under the Nevada law, a member of the targeted class "may not be compelled to answer" any inquiry except a command that he "identify himself."<sup>[2]</sup> Refusal to identify oneself upon request is punishable as a crime.<sup>[3]</sup> Presumably the statute does not require the detainee to answer any other question because the Nevada Legislature realized that the Fifth Amendment prohibits compelling the target of a criminal investigation to make any other statement. In my judgment, the broad constitutional right to remain silent, which derives from the Fifth Amendment's guarantee that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself,"<sup>[4]</sup> is not as circumscribed as the Court suggests, and does not admit even of the narrow exception defined by the Nevada statute.</p>
<p>"[T]here can be no doubt that the Fifth Amendment privilege is available outside of criminal court proceedings and serves to protect persons in all settings in which their freedom of action is curtailed in any significant way from being compelled to incriminate themselves." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467</a></span> (1966). It is a "settled principle" that "the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes," but <span class="star-pagination">*193</span> "they have no right to compel them to answer." <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 727, n. 6</a></span> (1969). The protections of the Fifth Amendment are directed squarely toward those who are the focus of the government's investigative and prosecutorial powers. In a criminal trial, the indicted defendant has an unqualified right to refuse to testify and may not be punished for invoking that right. See <i>Carter</i> v. <i>Kentucky,</i> <span class="citation" data-id="9428216"><a href="/opinion/110426/carter-v-kentucky/#299" aria-description="Citation for case: Carter v. Kentucky">450 U. S. 288, 299-300</a></span> (1981). The unindicted target of a grand jury investigation enjoys the same constitutional protection even if he has been served with a subpoena. See <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#767" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 767-768</a></span> (2003). So does an arrested suspect during custodial interrogation in a police station. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>.</p>
<p>There is no reason why the subject of police interrogation based on mere suspicion, rather than probable cause, should have any lesser protection. Indeed, we have said that the Fifth Amendment's protections apply with equal force in the context of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stops, see <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), where an officer's inquiry "must be `reasonably related in scope to the justification for [the stop's] initiation.'" <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984) (some internal quotation marks omitted). "Typically, this means that the officer may ask the detainee a moderate number of questions to determine his identity and to try to obtain information confirming or dispelling the officer's suspicions. But the detainee is not obliged to respond." <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Ibid.</a></span></i> See also <i>Terry,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 34</a></span> (White, J., concurring) ("Of course, the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest, although it may alert the officer to the need for continued observation"). Given our statements to the effect that citizens are not required to respond to police officers' questions during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, it is no surprise that petitioner assumed, as have we, that he had a right not to disclose his identity.</p>
<p>The Court correctly observes that a communication does not enjoy the Fifth Amendment privilege unless it is testimonial. <span class="star-pagination">*194</span> Although the Court declines to resolve this question, <i>ante,</i> at 189, I think it clear that this case concerns a testimonial communication. Recognizing that whether a communication is testimonial is sometimes a "difficult question," <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#214" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 214-215</a></span> (1988), we have stated generally that "[i]t is the `extortion of information from the accused,' the attempt to force him `to disclose the contents of his own mind,' that implicates the Self-Incrimination Clause," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 211</a></span> (citations omitted). While "[t]he vast majority of verbal statements thus will be testimonial and, to that extent at least, will fall within the privilege," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 213-214</a></span>, certain acts and physical evidence fall outside the privilege.<sup>[5]</sup> In all instances, we have afforded Fifth Amendment protection if the disclosure in question was being admitted because of its content rather than some other aspect of the communication.<sup>[6]</sup></p>
<p>Considered in light of these precedents, the compelled statement at issue in this case is clearly testimonial. It is significant that the communication must be made in response <span class="star-pagination">*195</span> to a question posed by a police officer. As we recently explained, albeit in the different context of the Sixth Amendment's Confrontation Clause, "[w]hatever else the term [`testimonial'] covers, it applies at a minimum . . . to police interrogations." <i>Crawford</i> v. <i>Washington,</i> <span class="citation" data-id="9434566"><a href="/opinion/134724/crawford-v-washington/#68" aria-description="Citation for case: Crawford v. Washington">541 U. S. 36, 68</a></span> (2004). Surely police questioning during a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop qualifies as an interrogation, and it follows that responses to such questions are testimonial in nature.</p>
<p>Rather than determining whether the communication at issue is testimonial, the Court instead concludes that the State can compel the disclosure of one's identity because it is not "incriminating." <i>Ante,</i> at 189. But our cases have afforded Fifth Amendment protection to statements that are "incriminating" in a much broader sense than the Court suggests. It has "long been settled that [the Fifth Amendment's] protection encompasses compelled statements that lead to the discovery of incriminating evidence even though the statements themselves are not incriminating and are not introduced into evidence." <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 37</a></span> (2000). By "incriminating" we have meant disclosures that "could be used in a criminal prosecution or could lead to other evidence that might be so used," <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 445</a></span> (1972)  communications, in other words, that "would furnish a link in the chain of evidence needed to prosecute the claimant for a federal crime," <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, 486</a></span> (1951). Thus, "[c]ompelled testimony that communicates information that may `lead to incriminating evidence' is privileged even if the information itself is not inculpatory." <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 38</a></span> (quoting <i>Doe,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#208" aria-description="Citation for case: Doe v. United States">487 U. S., at 208, n. 6</a></span>).</p>
<p>Given a proper understanding of the category of "incriminating" communications that fall within the Fifth Amendment privilege, it is clear that the disclosure of petitioner's identity is protected. The Court reasons that we should not assume that the disclosure of petitioner's "name would be used to incriminate him, or that it would furnish a link in [a] <span class="star-pagination">*196</span> chain of evidence needed to prosecute him." <i>Ante,</i> at 190 (internal quotation marks omitted). But why else would an officer ask for it? And why else would the Nevada Legislature require its disclosure only when circumstances "reasonably indicate that the person has committed, is committing or is about to commit a crime"?<sup>[7]</sup> If the Court is correct, then petitioner's refusal to cooperate did not impede the police investigation. Indeed, if we accept the predicate for the Court's holding, the statute requires nothing more than a useless invasion of privacy. I think that, on the contrary, the Nevada Legislature intended to provide its police officers with a useful law enforcement tool, and that the very existence of the statute demonstrates the value of the information it demands.</p>
<p>A person's identity obviously bears informational and incriminating worth, "even if the [name] itself is not inculpatory." <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#38" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 38</a></span>. A name can provide the key to a broad array of information about the person, particularly in the hands of a police officer with access to a range of law enforcement databases. And that information, in turn, can be tremendously useful in a criminal prosecution. It is therefore quite wrong to suggest that a person's identity provides a link in the chain to incriminating evidence "only in unusual circumstances." <i>Ante,</i> at 191.</p>
<p>The officer in this case told petitioner, in the Court's words, that "he was conducting an investigation and needed to see some identification." <i>Ante,</i> at 181. As the target of that investigation, petitioner, in my view, acted well within his rights when he opted to stand mute. Accordingly, I respectfully dissent.</p>
<p><span class="star-pagination">*197</span> JUSTICE BREYER, with whom JUSTICE SOUTER and JUSTICE GINSBURG join, dissenting.</p>
<p>Notwithstanding the vagrancy statutes to which the majority refers, see <i>ante,</i> at 183-184, this Court's Fourth Amendment precedents make clear that police may conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop only within circumscribed limits. And one of those limits invalidates laws that compel responses to police questioning.</p>
<p>In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court considered whether police, in the absence of probable cause, can stop, question, or frisk an individual at all. The Court recognized that the Fourth Amendment protects the "`right of every individual to the possession and control of his own person.'" <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></i> at 9 (quoting <i>Union Pacific R. Co.</i> v. <i>Botsford,</i> <span class="citation" data-id="93149"><a href="/opinion/93149/union-pacific-railway-co-v-botsford/#251" aria-description="Citation for case: Union Pacific Railway Co. v. Botsford">141 U. S. 250, 251</a></span> (1891)). At the same time, it recognized that in certain circumstances, public safety might require a limited "seizure," or stop, of an individual against his will. The Court consequently set forth conditions circumscribing when and how the police might conduct a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop. They include what has become known as the "reasonable suspicion" standard. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20-22</a></span>. Justice White, in a separate concurring opinion, set forth further conditions. Justice White wrote: "Of course, the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest, although it may alert the officer to the need for continued observation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 34</a></span>.</p>
<p>About 10 years later, the Court, in <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979), held that police lacked "any reasonable suspicion" to detain the particular petitioner and require him to identify himself. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas"><i>Id.,</i> at 53</a></span>. The Court noted that the trial judge had asked the following: "`I'm sure [officers conducting a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop] should ask everything they possibly could find out. <i>What I'm asking is what's the State's interest in putting a man in jail because he doesn't want to answer.</i> ...'" <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#54" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 54</a></span> (Appendix to opinion of the Court) (emphasis in <span class="star-pagination">*198</span> original). The Court referred to Justice White's <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> concurrence. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#53" aria-description="Citation for case: Brown v. Texas">443 U. S., at 53, n. 3</a></span>. And it said that it "need not decide" the matter. <i><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">Ibid.</a></span></i></p>
<p>Then, five years later, the Court wrote that an "officer may ask the <i>[Terry]</i> detainee a moderate number of questions to determine his identity and to try to obtain information confirming or dispelling the officer's suspicions. <i>But the detainee is not obliged to respond.</i>" <i>Berkemer</i> v. <i>Mc</i><i>Carty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#439" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 439</a></span> (1984) (emphasis added). See also <i>Kolender</i> v. <i>Lawson,</i> <span class="citation" data-id="9429183"><a href="/opinion/110926/kolender-v-lawson/#365" aria-description="Citation for case: Kolender v. Lawson">461 U. S. 352, 365</a></span> (1983) (Brennan, J., concurring) (<span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio"><i>Terry</i></a></span> suspect "must be free to ... decline to answer the questions put to him"); <i>Illinois</i> v. <i>Wardlow,</i> <span class="citation" data-id="9433881"><a href="/opinion/118326/illinois-v-wardlow/#125" aria-description="Citation for case: Illinois v. Wardlow">528 U. S. 119, 125</a></span> (2000) (stating that allowing officers to stop and question a fleeing person "is quite consistent with the individual's right to go about his business or to stay put and remain silent in the face of police questioning").</p>
<p>This lengthy history  of concurring opinions, of references, and of clear explicit statements  means that the Court's statement in <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span>,</i> while technically dicta, is the kind of strong dicta that the legal community typically takes as a statement of the law. And that law has remained undisturbed for more than 20 years.</p>
<p>There is no good reason now to reject this generation-old statement of the law. There are sound reasons rooted in Fifth Amendment considerations for adhering to this Fourth Amendment legal condition circumscribing police authority to stop an individual against his will. See <i>ante,</i> at 192-196 (STEVENS, J., dissenting). Administrative considerations also militate against change. Can a State, in addition to requiring a stopped individual to answer "What's your name?" also require an answer to "What's your license number?" or "Where do you live?" Can a police officer, who must know how to make a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop, keep track of the constitutional answers? After all, answers to any of these questions may, or may not, incriminate, depending upon the circumstances.</p>
<p><span class="star-pagination">*199</span> Indeed, as the Court points out, a name itself  even if it is not "Killer Bill" or "Rough 'em up Harry"  will sometimes provide the police with "a link in the chain of evidence needed to convict the individual of a separate offense." <i>Ante,</i> at 191. The majority reserves judgment about whether compulsion is permissible in such instances. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></i> How then is a police officer in the midst of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> stop to distinguish between the majority's ordinary case and this special case where the majority reserves judgment?</p>
<p>The majority presents no evidence that the rule enunciated by Justice White and then by the <i><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">Berkemer</a></span></i> Court, which for nearly a generation has set forth a settled <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-stop condition, has significantly interfered with law enforcement. Nor has the majority presented any other convincing justification for change. I would not begin to erode a clear rule with special exceptions.</p>
<p>I consequently dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the American Civil Liberties Union by <i>Steven R. Shapiro, Lawrence S. Lustberg,</i> and <i>Mark A. Berman;</i> for the Cato Institute by <i>Timothy Lynch</i> and <i>M. Christine Klein;</i> for the National Law Center on Homelessness &amp; Poverty et al. by <i>Carter G. Phillips, Edward R. McNicholas,</i> and <i>Rebecca K. Troth;</i> and for John Gilmore by <i>James P. Harrison.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the National Association of Police Organizations by <i>Joel D. Bertocchi</i> and <i>Philip Allen Lacovara.</i></p>
<p>Briefs of <i>amici curiae</i> were filed for the Electronic Frontier Foundation by <i>Robert Weisberg;</i> for the Electronic Privacy Information Center et al. by <i>Marc Rotenberg</i> and <i>David L. Sobel;</i> and for Privacy Activism et al. by <i>William M. Simpich.</i></p>
<p>[1]  <span class="citation no-link">Nev. Rev. Stat. § 171.123</span>(1) (2003).</p>
<p>[2]  § 171.123(3).</p>
<p>[3]  In this case, petitioner was charged with violating § 199.280, which makes it a crime to "willfully resis[t], dela[y] or obstruc[t] a public officer in discharging or attempting to discharge any legal duty of his office." A violation of that provision is a misdemeanor unless a dangerous weapon is involved.</p>
<p>[4]  The Fifth Amendment's protection against compelled self-incrimination applies to the States through the Fourteenth Amendment's Due Process Clause. See <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#6" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 6</a></span> (1964).</p>
<p>[5]  A suspect may be made, for example, to provide a blood sample, <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 765</a></span> (1966), a voice exemplar, <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 7</a></span> (1973), or a handwriting sample, <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967).</p>
<p>[6]  See <i>Pennsylvania</i> v. <i>Muniz,</i> <span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#598" aria-description="Citation for case: Pennsylvania v. Muniz">496 U.S. 582, 598-599</a></span> (1990) (respondent's answer to the "birthday question" was protected because the "content of his truthful answer supported an inference that his mental faculties were impaired"); <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 211, n. 10</a></span> (1988) ("The content itself must have testimonial significance"); <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#410" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 410-411</a></span> (1976) ("[H]owever incriminating the contents of the accountant's workpapers might be, the act of producing them  the only thing which the taxpayer is compelled to do  would not itself involve testimonial self-incrimination"); <i>Gilbert,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S., at 266-267</a></span> ("A mere handwriting exemplar, in contrast to the content of what is written, like the voice or body itself, is an identifying physical characteristic outside its protection"); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#223" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 223</a></span> (1967) ("[I]t deserves emphasis that this case presents no question of the admissibility in evidence of anything Wade said or did at the lineup which implicates his privilege").</p>
<p>[7]  <span class="citation no-link">Nev. Rev. Stat. § 171.123</span>(1) (2003). The Court suggests that furnishing identification also allows the investigating officer to assess the threat to himself and others. See <i>ante,</i> at 186. But to the extent that officer or public safety is immediately at issue, that concern is sufficiently alleviated by the officer's ability to perform a limited patdown search for weapons. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 25-26</a></span> (1968).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Hill v. California.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Hill v. California"
type: case
citation: "401 U.S. 797 (1971)"
parallel_cite: "91 S. Ct. 1106; 28 L. Ed. 2d 484; 27 A.F.T.R.2d (RIA) 1006"
neutral_cite: 1971 U.S. LEXIS 59
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-04-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-04-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hill v. California
  varies_by_point: false
  scope_note: "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108305/hill-v-california/"
  cluster_id: 108305
  opinion_id: 108305
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Progeny"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Brinegar v. United States]]", "[[Chimel v. California]]", "[[Heien v. North Carolina]]", "[[Maryland v. Garrison]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "mistaken-identity", "search-incident-to-arrest"]
holding: "An arrest of the wrong person is valid where police have probable cause to arrest one person and reasonably, in good faith, mistake the arrestee for that person; the search incident to that arrest is likewise valid."
lake:
  record_id: Hill v. California
  status: verified
  projected_at: 2026-07-09
---

# Hill v. California

*401 U.S. 797 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police had probable cause to arrest Hill for robbery and had his address and a verified physical description. At Hill's apartment they encountered Miller, who matched the description of Hill. Miller insisted he was Miller, not Hill, and produced identification, but his explanation for being in the locked apartment was unconvincing, and a pistol and a loaded ammunition clip lay in plain view. Believing Miller was Hill, the officers arrested him and searched the apartment incident to the arrest, seizing evidence later used to convict the actual Hill. Hill moved to suppress, arguing the arrest of the wrong man was invalid and the search therefore unlawful.

## Issue
Whether an arrest is valid — and a search incident to it lawful — when police have probable cause to arrest one person but, reasonably and in good faith, arrest a different person whom they mistake for the suspect.

## Rule
Yes. The Court adopted the rule that "[w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest." — 401 U.S. at 802. ^pin-802

Good faith alone is not enough; the test is objective reasonableness: "sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time." — [*Id.* at 804](https://www.courtlistener.com/opinion/108305/hill-v-california/#:~:text=sufficient%20probability%2C%20not%20certainty%2C%20is). ^pin-804

A valid arrest of the mistaken person supports a search incident to it: "the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed." — [*Id.* at 804–805](https://www.courtlistener.com/opinion/108305/hill-v-california/#:~:text=the%20police%20were%20entitled%20to). ^pin-804b

## Application
The officers had unquestionable probable cause to arrest Hill, a verified description, and his address. When they found Miller — who fit that description, gave an unconvincing account of his presence, and had a pistol and ammunition in plain view — their belief that Miller was Hill was an understandable, objectively reasonable mistake, not mere subjective good faith. Because the arrest was therefore valid, the search incident to it (judged under pre-*[[Chimel v. California|Chimel]]* scope, which the Court declined to apply retroactively here) was also valid, and the seized evidence was admissible against Hill.

## Conclusion
The reasonable, good-faith arrest of the wrong man was valid, as was the search incident to it; the judgment was affirmed. Fourth Amendment reasonableness tolerates an understandable mistake of identity where police have probable cause to arrest the intended suspect.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hill*'s reasonable-mistake principle applies the practical probable-cause standard of [[Brinegar v. United States]] and parallels [[Maryland v. Garrison]] (reasonable mistake as to the apartment to be searched) and [[Heien v. North Carolina]] (reasonable mistake of law); the search-incident analysis tracks [[Chimel v. California]].

## Appears on
- [[Probable Cause]] — *Progeny*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Hill v. California*, 401 U.S. 797 (1971) — https://www.courtlistener.com/opinion/108305/hill-v-california/ — pinpoints: 802, 804–805.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43ecc7fb9f8d0828", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hill v. California"}, "payload": {"all": [{"cite": "401 U.S. 797", "page": "797", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "401"}, {"cite": "91 S. Ct. 1106", "page": "1106", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "28 L. Ed. 2d 484", "page": "484", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "28"}, {"cite": "1971 U.S. LEXIS 59", "page": "59", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}, {"cite": "27 A.F.T.R.2d (RIA) 1006", "page": "1006", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "27"}], "display": "401 U.S. 797", "official": {"cite": "401 U.S. 797", "page": "797", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "401"}, "official_selection_present": true, "record_id": "Hill v. California"}}
{"assertion_id": "38ea6b2791f22c97", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-802", "record_id": "Hill v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-802", "pinpoint_status": "slip-only", "quote": "--- # Hill v. California *401 U.S. 797 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to arrest Hill for robbery and had his address and a verified physical description. At Hill's apartment they encountered Miller, who matched the description of Hill. Miller insisted he was Miller, not Hill, and produced identification, but his explanation for being in the locked apartment was unconvincing, and a pistol and a loaded ammunition clip lay in plain view. Believing Miller was Hill, the officers arrested him and searched the apartment incident to the arrest, seizing evidence later used to convict the actual Hill. Hill moved to suppress, arguing the arrest of the wrong man was invalid and the search therefore unlawful. ## Issue Whether an arrest is valid — and a search incident to it lawful — when police have probable cause to arrest one person but, reasonably and in good faith, arrest a different person whom they mistake for the suspect. ## Rule Yes. The Court adopted the rule that", "quote_fidelity": "mismatch", "record_id": "Hill v. California", "star_marker": null}}
{"assertion_id": "41dd552e076989ad", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-804", "record_id": "Hill v. California"}, "payload": {"fragment": "#:~:text=sufficient%20probability%2C%20not%20certainty%2C%20is", "page": null, "pin_id": "pin-804", "pinpoint_status": "star-verified", "quote": "sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time.", "quote_fidelity": "matched", "record_id": "Hill v. California", "star_marker": "804"}}
{"assertion_id": "9c21a818115624bf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-804b", "record_id": "Hill v. California"}, "payload": {"fragment": "#:~:text=the%20police%20were%20entitled%20to", "page": null, "pin_id": "pin-804b", "pinpoint_status": "star-verified", "quote": "the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed.", "quote_fidelity": "matched", "record_id": "Hill v. California", "star_marker": "804"}}
{"assertion_id": "982a918fa9dd53fe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hill v. California"}, "payload": {"as_of_content": "1971-04-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hill v. California", "scope_note": "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness.", "varies_by_point": false}}
```

### lake record — Hill v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hill v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hill v. California",
    "case_name_short": "Hill",
    "case_name_full": "Hill v. California",
    "input_case_name": "Hill v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-04-05",
    "year": 1971,
    "docket": null,
    "cluster_id": 108305,
    "lead_opinion_id": 108305,
    "sibling_ids": [
      108305,
      9424518,
      9424519
    ],
    "absolute_url": "/opinion/108305/hill-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 797",
      "volume": "401",
      "reporter": "U.S.",
      "page": "797",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 1106",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 484",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 A.F.T.R.2d (RIA) 1006",
        "volume": "27",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1006",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 59",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "59",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 797",
        "volume": "401",
        "reporter": "U.S.",
        "page": "797",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 1106",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 484",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 59",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "59",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "27 A.F.T.R.2d (RIA) 1006",
        "volume": "27",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1006",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 797",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 797",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-802",
      "page": null,
      "quote": "--- # Hill v. California *401 U.S. 797 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police had probable cause to arrest Hill for robbery and had his address and a verified physical description. At Hill's apartment they encountered Miller, who matched the description of Hill. Miller insisted he was Miller, not Hill, and produced identification, but his explanation for being in the locked apartment was unconvincing, and a pistol and a loaded ammunition clip lay in plain view. Believing Miller was Hill, the officers arrested him and searched the apartment incident to the arrest, seizing evidence later used to convict the actual Hill. Hill moved to suppress, arguing the arrest of the wrong man was invalid and the search therefore unlawful. ## Issue Whether an arrest is valid \u2014 and a search incident to it lawful \u2014 when police have probable cause to arrest one person but, reasonably and in good faith, arrest a different person whom they mistake for the suspect. ## Rule Yes. The Court adopted the rule that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-804",
      "page": null,
      "quote": "sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time.",
      "star_marker": "804",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9745,
      "fragment": "#:~:text=sufficient%20probability%2C%20not%20certainty%2C%20is",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-804b",
      "page": null,
      "quote": "the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed.",
      "star_marker": "804",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10677,
      "fragment": "#:~:text=the%20police%20were%20entitled%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-04-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hill v. California",
    "varies_by_point": false,
    "scope_note": "Good law. When police have probable cause to arrest one person and reasonably, in good faith, mistake another for that person, the arrest of the second person is valid, and so is the ensuing search incident to arrest. Sufficient probability, not certainty, is the touchstone of Fourth Amendment reasonableness.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Hill v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Damian D.",
          "cluster_id": 6578334,
          "cite": [
            "434 Mass. 725",
            "752 N.E.2d 679",
            "2001 Mass. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mendenhall v. Riser",
          "cluster_id": 21122,
          "cite": [
            "213 F.3d 226",
            "2000 WL 691548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane1_negative"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia Court of Appeals v. Feldman",
          "cluster_id": 110889,
          "cite": [
            "75 L. Ed. 2d 206",
            "103 S. Ct. 1303",
            "460 U.S. 462",
            "1983 U.S. LEXIS 150",
            "51 U.S.L.W. 4285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Illinois",
          "cluster_id": 108497,
          "cite": [
            "31 L. Ed. 2d 551",
            "92 S. Ct. 1208",
            "405 U.S. 645",
            "1972 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chevron Oil Co. v. Huson",
          "cluster_id": 108406,
          "cite": [
            "30 L. Ed. 2d 296",
            "92 S. Ct. 349",
            "404 U.S. 97",
            "1971 U.S. LEXIS 95"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wood v. Georgia",
          "cluster_id": 110425,
          "cite": [
            "67 L. Ed. 2d 220",
            "101 S. Ct. 1097",
            "450 U.S. 261",
            "1981 U.S. LEXIS 76",
            "49 U.S.L.W. 4218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Evans",
          "cluster_id": 1538821,
          "cite": [
            "165 Conn. 61",
            "327 A.2d 576",
            "1973 Conn. LEXIS 709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Outboard Marine Corp.",
          "cluster_id": 762789,
          "cite": [
            "172 F.3d 531",
            "1999 U.S. App. LEXIS 5444",
            "1999 WL 164061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manganiello v. City of New York",
          "cluster_id": 2522805,
          "cite": [
            "612 F.3d 149",
            "2010 U.S. App. LEXIS 15156",
            "2010 WL 2884967"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buchanan v. Kentucky",
          "cluster_id": 111947,
          "cite": [
            "97 L. Ed. 2d 336",
            "107 S. Ct. 2906",
            "483 U.S. 402",
            "1987 U.S. LEXIS 2877",
            "55 U.S.L.W. 5026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patricia Scott v. Clay County, Tennessee Chinn Anderson Billy Pierce Michael Thompson",
          "cluster_id": 767897,
          "cite": [
            "205 F.3d 867",
            "2000 U.S. App. LEXIS 2965",
            "2000 WL 228300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harvey",
          "cluster_id": 1343416,
          "cite": [
            "187 S.E.2d 706",
            "281 N.C. 1",
            "1972 N.C. LEXIS 1321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
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
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glenn v. City of Tyler",
          "cluster_id": 23151,
          "cite": [
            "242 F.3d 307",
            "2001 U.S. App. LEXIS 2585",
            "2001 WL 102270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atkins v. City of Chicago",
          "cluster_id": 183500,
          "cite": [
            "631 F.3d 823",
            "2011 U.S. App. LEXIS 1459",
            "2011 WL 206155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hill v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108305 OR 9424518 OR 9424519) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTU0MzM2MDAwMDAmcz0yMTA0Njg2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108305+OR+9424518+OR+9424519%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(108305 OR 9424518 OR 9424519)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzkmcz00OTA1OTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108305+OR+9424518+OR+9424519%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108305 OR 9424518 OR 9424519)",
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
    "complete_query": "cites:(108305 OR 9424518 OR 9424519)",
    "indexed_citing_opinions": 451,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108305,
        "count": 400,
        "count_source": "search"
      },
      {
        "opinion_id": 9424518,
        "count": 55,
        "count_source": "search"
      },
      {
        "opinion_id": 9424519,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 766,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hill-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY5NDk5NzMmcz00NzkwNjE5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108305+OR+9424518+OR+9424519%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108305,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 107889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 1129895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108305,
        "cited_id": 1428394,
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
    "date_created": "2026-07-05T07:10:37Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:14:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:10:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hill v. California

```
<div>
<center><b><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U.S. 797</a></span> (1971)</b></center>
<center><h1>HILL<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 51.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 19, 1970</center>
<center>Reargued October 21, 1970</center>
<center>Decided April 5, 1971</center>
CERTIORARI TO THE SUPREME COURT OF CALIFORNIA.
<p><span class="star-pagination">*798</span> <i>Joseph Amato,</i> appointed by the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./396/999/">396 U. S. 999</a></span>, reargued the cause for petitioner.</p>
<p><i>Ronald M. George,</i> Deputy Attorney General of California, reargued the cause for respondent. With him on the brief were <i>Thomas C. Lynch,</i> Attorney General, and <i>William E. James,</i> Assistant Attorney General.</p>
<p><i>Keith C. Monroe</i> filed a brief for the Orange County Criminal Courts Bar Association et al. as <i>amici curiae</i> urging reversal. <i>Duke W. Dunbar,</i> Attorney General, <i>pro se,</i> and <i>John P. Moore,</i> Deputy Attorney General, filed a brief for the Attorney General of Colorado et al. as <i>amici curiae.</i></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>On June 4, 1966, four armed men robbed a residence in Studio City, California. On June 5, Alfred Baum and Richard Bader were arrested for possession of narcotics; at the time of their arrest, they were driving petitioner Hill's car, and a search of the car produced property stolen in the Studio City robbery the day before. Bader and Baum both admitted taking part in the June 4 robbery, and both implicated Hill. Bader told the police that he was sharing an apartment with Hill at 9311 <span class="star-pagination">*799</span> Sepulveda Boulevard. He also stated that the guns used in the robbery and other stolen property were in the apartment. On June 6, Baum and Bader again told the police that Hill had been involved in the June 4 robbery.</p>
<p>One of the investigating officers then checked official records on Hill, verifying his prior association with Bader, his age and physical description, his address, and the make of his car. The information the officer uncovered corresponded with the general descriptions by the robbery victims and the statements made by Baum and Bader.</p>
<p>Hill concedes that this information gave the police probable cause to arrest him, and the police undertook to do so on June 6. Four officers went to the Sepulveda Boulevard apartment, verified the address, and knocked. One of the officers testified: "The door was opened and a person who fit the description exactly of Archie Hill, as I had received it from both the cards and from Baum and Bader, answered the door. . . . We placed him under arrest for robbery."</p>
<p>The police had neither an arrest nor a search warrant. After arresting the man who answered the door, they asked him whether he was Hill and where the guns and stolen goods were. The arrestee replied that he was not Hill, that his name was Miller, that it was Hill's apartment and that he was waiting for Hill. He also claimed that he knew nothing about any stolen property or guns, although the police testified that an automatic pistol and a clip of ammunition were lying in plain view on a coffee table in the living room where the arrest took place. The arrestee then produced identification indicating that he was in fact Miller, but the police were unimpressed and proceeded to search the apartment living room, bedroom, kitchen area, and bathfor a period which one officer described as "a couple of hours."</p>
<p>During the course of the search, the police seized several <span class="star-pagination">*800</span> items: rent receipts and personal correspondence bearing Hill's name from a dresser drawer in the bedroom; a starter pistol, two switchblade knives, a camera and case stolen in the Studio City robbery, and two hoodmasks made from white T-shirts, all from the bedroom; a .22-caliber revolver from under the living room sofa; and two pages of petitioner Hill's diary from a bedroom dresser drawer.<sup>[1]</sup></p>
<p><span class="star-pagination">*801</span> On October 20, 1966, Hill was found guilty of robbery on the basis of evidence produced at the preliminary hearing and the trial.<sup>[2]</sup> Eyewitnesses to the robbery were unable to identify Hill; the only substantial evidence of his guilt consisted of the items seized in the search of his apartment. In sustaining the admissibility of the evidence, the trial judge ruled that the arresting officers had acted in the good-faith belief that Miller was in fact Hill.<sup>[3]</sup> The District Court of Appeal agreed that the officers acted in good faith and that the arrest of Miller was valid but nonetheless thought the incident search of Hill's apartment unreasonable under the Fourth Amendment. <span class="citation no-link">67 Cal. Rptr. 389</span> (1968).<sup>[4]</sup> The California Supreme Court in turn reversed, sustaining both the arrest and the search. <span class="citation multiple-matches"><a href="/c/Cal.%202d/69/550/">69 Cal. 2d 550</a></span>, <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/" aria-description="Citation for case: People v. Hill">446 P. 2d 521</a></span> (1968). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./396/818/">396 U. S. 818</a></span> (1969), and now affirm the judgment of the California Supreme Court.</p>
<p></p>
<h2>
<span class="star-pagination">*802</span> I</h2>
<p>Petitioner argues that <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), decided after his conviction was affirmed by the California Supreme Court, should be applied to his case, which is before us on direct review. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> narrowed the permissible scope of searches incident to arrest, but in <i>Williams</i> v. <i>United States</i> and <i>Elkanich</i> v. <i>United States, ante,</i> p. 646, we held <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> inapplicable to searches occurring before the date of decision in that caseregardless of whether a case was still on direct review when <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was decided, see <i>Williams, supra,</i> or whether a <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> challenge was asserted in a subsequent collateral attack on a conviction. See <i>Elkanich, supra.</i> We also stated that in light of past decisions there was no difference in constitutional terms between state and federal prisoners insofar as retroactive application to their cases of a new interpretation of the Bill of Rights is concerned. <i>Ante,</i> at 656. The search of Hill's apartment, permissible in scope under pre-<span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California"><i>Chimel</i></a></span> standards, will not be retrospectively invalidated because of that decision.</p>
<p></p>
<h2>II</h2>
<p>Based on our own examination of the record, we find no reason to disturb either the findings of the California courts that the police had probable cause to arrest Hill and that the arresting officers had a reasonable, goodfaith belief that the arrestee Miller was in fact Hill, or the conclusion that "[w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest." <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#553" aria-description="Citation for case: People v. Hill">69 Cal. 2d, at 553</a></span>, <span class="citation" data-id="1129895"><a href="/opinion/1129895/people-v-hill/#523" aria-description="Citation for case: People v. Hill">446 P. 2d, at 523</a></span>.<sup>[5]</sup> The police unquestionably had probable <span class="star-pagination">*803</span> cause to arrest Hill; they also had his address and a verified description. The mailbox at the indicated address listed Hill as the occupant of the apartment. Upon gaining entry to the apartment, they were confronted with one who fit the description of Hill received from various sources.<sup>[6]</sup> That person claimed he was Miller, not Hill. But aliases and false identifications are not uncommon.<sup>[7]</sup> Moreover, there was a lock on the door and Miller's explanation for his mode of entry was not convincing.<sup>[8]</sup> He also denied knowledge of firearms in the apartment although a pistol and loaded ammunition clip were in plain view in the room.<sup>[9]</sup> The upshot was that the officers <span class="star-pagination">*804</span> in good faith believed Miller was Hill and arrested him. They were quite wrong as it turned out, and subjective good-faith belief would not in itself justify either the arrest or the subsequent search. But sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers' mistake was understandable and the arrest a reasonable response to the situation facing them at the time.</p>
<p>Nor can we agree with petitioner that however valid the arrest of Miller, the subsequent search violated the Fourth Amendment. It is true that Miller was not Hill; nor did Miller have authority or control over the premises, although at the very least he was Hill's guest. But the question is not what evidence would have been admissible against Hill (or against Miller for that matter) if the police, with probable cause to arrest Miller, had arrested him in Hill's apartment and then carried out the search at issue. Here there was probable cause to arrest Hill and the police arrested Miller in Hill's apartment, reasonably believing him to be Hill. In these circumstances the police were entitled to do what the law would have allowed them to do if Miller had in fact been Hill, that is, to search incident to arrest and to seize evidence of the crime the police had probable cause to believe Hill had committed. When judged in accordance with "the factual and practical considerations of everyday life on which reasonable and prudent men, not <span class="star-pagination">*805</span> legal technicians, act," <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175</a></span> (1949), the arrest and subsequent search were reasonable and valid under the Fourth Amendment.</p>
<p></p>
<h2>III</h2>
<p>Finally, in his brief in this Court, petitioner argues that the admission in evidence of the two pages of his diary Pages which contained what amounted to a confession of the robberyviolated the Fifth Amendment under <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886). Counsel for Hill conceded at oral argument that the Fifth Amendment issue was not raised at trial. Nor was the issue raised, briefed, or argued in the California appellate courts.<sup>[10]</sup> The petition for certiorari likewise ignored it. In this posture of the case, the question, although briefed and argued here, is not properly before us. In <i>Cardinale</i> v. <i>Louisiana,</i> <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S. 437</a></span> (1969), certiorari was granted to consider the constitutionality of a Louisiana statute, but at oral argument it developed that the federal question had never been raised, preserved, or passed upon in the state courts. Relying on a long line of cases, we dismissed the writ for want of jurisdiction. <span class="citation" data-id="107889"><a href="/opinion/107889/cardinale-v-louisiana/#439" aria-description="Citation for case: Cardinale v. Louisiana">394 U. S., at 439</a></span>. In addition, we stated that there were sound policy reasons for adhering to such a rule. In the context of that case, we indicated the desirability of allowing state courts to pass first on the constitutionality of state statutes in light of a federal constitutional challenge; this assures both an adequate record and that the States have first opportunity to provide a definitive interpretation of their statutes. We also indicated that a federal habeas corpus remedy might remain if no state procedure for raising the issue was available following dismissal of the writ. These considerations are no less applicable in this <span class="star-pagination">*806</span> case. We therefore do not reach the Fifth Amendment question and affirm the judgment of the Supreme Court of California.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACK concurs in the result.</p>
<p>MR. JUSTICE DOUGLAS took no part in the consideration or the decision of this case.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE MARSHALL joins, concurring in part and dissenting in part.</p>
<p>I agree with the Court's opinion except for its conclusion that the <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> case is not to be applied to this one.</p>
<p>Two Terms ago, in <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), we held that a search without a warrant, but incident to a lawful arrest, must be narrowly confined in scope if it is to pass constitutional muster. In such circumstances, we said:</p>
<blockquote>"There is ample justification . . . for a search of the arrestee's person and the area `within his immediate control'construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.</blockquote>
<blockquote>"There is no comparable justification, however, for routinely searching any room other than that in which an arrest occursor, for that matter, for searching through all the desk drawers or other closed or concealed areas in that room itself. Such searches, in the absence of well-recognized exceptions, may be made only under the authority of a search warrant. The `adherence to judicial processes' mandated by the Fourth Amendment requires no less." <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span> (footnote omitted).</blockquote>
<p><span class="star-pagination">*807</span> The search here involved, fully described in the Court's opinion, plainly exceeded the bounds set forth in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>.</i> The State contends that the search here was consistent with <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> because conducted in the evening when it was not possible to obtain a search warrant. Whatever validity such a limiting principle might have in other contexts, it certainly cannot properly be invoked here. Baum and Bader had implicated Hill at least 24 hours prior to the search of Hill's apartment. Moreover, the State does not explain why it would not have been possible to observe the apartment after the mistaken arrest of Miller as Hill and then test before a magistrate the validity of their belief that they had probable cause for the issuance of a warrant authorizing a complete search of the apartment.</p>
<p>Because I believe this case reveals an obvious violation of <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> and because I consider we are duty bound to apply the principles there enunciated to cases, like this one, before us on direct review, see my separate opinion in <i>Mackey</i> v. <i>United States</i> (and companion cases), <i>ante,</i> p. 675, decided today, I am compelled to cast my vote for reversal of the judgment of the Supreme Court of California.</p>
<h2>NOTES</h2>
<p>[1]  All of these items, except the rent receipts and correspondence, were later introduced in evidence at the preliminary examination involving Baum, Bader, and Hill. A radio stolen in the Studio City robbery was also introduced, since it was found in Hill's car when Baum and Bader were arrested. Finally, the State introduced two handwriting exemplars executed by petitioner Hill after his arrest. Although the rent receipts and personal correspondence were not introduced in evidence, one of the officers who participated in the arrest and search at the Hill apartment testified that in the same drawer where he found the diary pages "there were rent receipts, numerous stack of rent receipts at this particular apartment, made out to Archie Hill, and there were several other pieces of paper, correspondence, notes from girls, and so forth, all to an Archie or an Archie Hill." No objection was offered to this testimony.
</p>
<p>Thereafter, petitioner's case was severed from that of Baum and Bader. Hill waived a jury and submitted the case for trial on the transcript of the preliminary hearing and the exhibits there introduced. The State called one additional witness at trialOfficer Gastaldowho gave a more complete version of the investigation of the robbery and of the arrest of the man who turned out to be Miller. The two diary pages seized in Hill's apartment contained what was in effect a full confession of his participation in the Studio City robbery. The additional testimony of Officer Gastaldo was critical in establishing the legality of the arrest and subsequent search. After hearing this testimony, the trial judge denied petitioner's motion to suppress the items seized, including, of course, the diary pages. Hill presented no further evidence at trial, and was found guilty as charged. A motion for a new trial was subsequently denied, and petitioner's appeals in the California courts followed.</p>
<p>In his brief in this Court, petitioner attacks the admission of the diary pages on a ground never advanced below. For the reasons expressed in Part III of this opinion, we do not rule upon these contentions.</p>
<p>[2]  See n. 1, <i>supra.</i></p>
<p>[3]  The trial judge stated:
</p>
<p>"I have fully reviewed the evidence. I have determined that the officer in good faith believed that the defendant, or that the person who was arrestednot the defendant in this casewas believed by the officer in good faith to be Mr. Hill, and that whether or not this document consisting of two pages of the private diary of Mr. Hill should be admitted depends on whether or not at the time of the arrest and the search of the premises, the officer acted in good faith."</p>
<p>[4]  Justice Ford stated:
</p>
<p>"While the doctrine of probable cause assures a balance between the rights of the individual and those of the government with respect to the matter of arrest, the constitutional protection against unreasonable searches, particularly of a person's home, would be less than complete if a plenary search could be justified as incident to an arrest of a person mistakenly believed by an officer to be in immediate charge of the premises. Such a case is not one where the right of privacy must reasonably yield to the right of search." 67 Cal. Rptr., at 391.</p>
<p>[5]  The California Supreme Court relied on <i>People</i> v. <i>Kitchens,</i> <span class="citation" data-id="9627771"><a href="/opinion/1428394/people-v-kitchens/#263" aria-description="Citation for case: People v. Kitchens">46 Cal. 2d 260, 263-264</a></span>, <span class="citation" data-id="9627771"><a href="/opinion/1428394/people-v-kitchens/#19" aria-description="Citation for case: People v. Kitchens">294 P. 2d 17, 19-20</a></span> (1956); <i>People</i> v. <i>Miller,</i> <span class="citation" data-id="2204229"><a href="/opinion/2204229/people-v-miller/" aria-description="Citation for case: People v. Miller">193 Cal. App. 2d 838</a></span>, <span class="citation" data-id="2204229"><a href="/opinion/2204229/people-v-miller/" aria-description="Citation for case: People v. Miller">14 Cal. Rptr. 704</a></span> (1961), and <i>People</i> v. <i>Campos,</i> <span class="citation" data-id="2192813"><a href="/opinion/2192813/people-v-campos/" aria-description="Citation for case: People v. Campos">184 Cal. App. 2d 489</a></span>, <span class="citation" data-id="2192813"><a href="/opinion/2192813/people-v-campos/" aria-description="Citation for case: People v. Campos">7 Cal. Rptr. 513</a></span> (1960). See also <i>People</i> v. <i>Lopez,</i> <span class="citation" data-id="9736481"><a href="/opinion/2205719/people-v-lopez/" aria-description="Citation for case: People v. Lopez">269 Cal. App. 2d 461</a></span>, 468 n. 2, <span class="citation" data-id="9736481"><a href="/opinion/2205719/people-v-lopez/" aria-description="Citation for case: People v. Lopez">74 Cal. Rptr. 740</a></span>, 744 n. 2 (1969) (dictum).</p>
<p>[6]  At the preliminary hearing and trial, the only disparities in description established were that Miller was two inches taller and 10 pounds heavier than Hill.</p>
<p>[7]  In denying the motion to suppress, the trial judge took judicial notice of the fact "that those who are apprehended and are arrested many times attempt to avoid arrest by giving false identification."</p>
<p>[8]  Petitioner points out that the officers had no idea how Miller gained access to the Hill apartment, and asserts that it was improper for them to assume that he was lawfully there. It is undisputed that Miller was the only occupant of the apartment. One of the officers testified that there was a lock on the door and that he had asked Miller how he had gotten into the apartment; Miller made no specific reply, except to reiterate that he had come in and was waiting for Hill, the tenant.</p>
<p>[9]  Petitioner also claims that it was unreasonable for the officers to disregard Miller's proffered identification. However, Miller's answer to the question about firearms could reasonably be regarded as evasive, and his subsequent production of identification as therefore entitled to little weight. Petitioner stresses that Miller was subsequently booked in his own name when taken to the station house, arguing that this demonstrates that the officers' belief that Miller was Hill was unreasonable. However, the trial judge found that the arresting officer was not responsible for the booking procedures under which Miller would be booked under whatever name he gave at the station house. This conclusion is buttressed by the fact that Miller was not released from custody for a day and a half, after a thorough check of his identification revealed that he had in fact told the truth about his identity, despite his evasiveness in dealing with the officers at the apartment.</p>
<p>[10]  Tr. of Oral Rearg. 34-35.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Hoffa v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hoffa v. United States"
type: case
citation: "385 U.S. 293 (1966)"
parallel_cite: "87 S. Ct. 408; 17 L. Ed. 2d 374"
neutral_cite: 1966 U.S. LEXIS 2778
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-12-12
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hoffa v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/"
  cluster_id: 107318
  opinion_id: 9423305
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Kuhlmann v. Wilson]]", "[[Illinois v. Perkins]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "informants", "attachment"]
holding: "A defendant has no Sixth Amendment claim when a government informant elicits statements **before** the right has attached; planting an informant raises no 6A problem pre-attachment."
lake:
  record_id: Hoffa v. United States
  status: verified
  projected_at: 2026-07-09
---

# Hoffa v. United States

*385 U.S. 293 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During Hoffa's "Test Fleet" trial, a local union official, Edward Partin, was with Hoffa's entourage and reported to the government that Hoffa made statements about attempting to bribe jurors. Hoffa was later convicted of jury tampering largely on Partin's testimony. Hoffa argued, among other things, that the government violated his Sixth Amendment right to counsel by failing to arrest him as soon as it had probable cause, which (he said) would have caused the right to attach before the statements were made.

## Issue
Whether the government violates the Sixth Amendment right to counsel when an informant obtains incriminating statements before adversary proceedings have begun, where the government did not arrest or charge the suspect earlier even though it may have had grounds to do so.

## Rule
No. The Court rejected the contention that the government must arrest a suspect as soon as it has probable cause so that the right to counsel will attach: "There is no constitutional right to be arrested." — 385 U.S. at 310. ^pin-310

"The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long." — [*Id.*](https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/#:~:text=The%20police%20are%20not%20required) ^pin-310a

## Application
On these facts no adversary proceedings on the jury-tampering charge had begun when Hoffa spoke in Partin's presence, and the government had no duty to arrest or charge him earlier to trigger the right to counsel. Because the Sixth Amendment right had not attached as to that offense when the statements were made, the use of Partin to gather and report them was no violation of Hoffa's right to counsel.

## Conclusion
The convictions were affirmed. There is no Sixth Amendment violation where an informant elicits statements before the right to counsel has attached.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hoffa* fixes the pre-attachment boundary that frames the deliberate-elicitation rule of [[Massiah v. United States]]; the Sixth Amendment is offense-specific and attaches only at the initiation of adversary judicial proceedings.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Hoffa v. United States*, 385 U.S. 293 (1966) — https://www.courtlistener.com/opinion/107318/hoffa-v-united-states/ — pinpoint: 310.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d164fbc0dea99e0a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hoffa v. United States"}, "payload": {"all": [{"cite": "385 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "385"}, {"cite": "87 S. Ct. 408", "page": "408", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "17 L. Ed. 2d 374", "page": "374", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "1966 U.S. LEXIS 2778", "page": "2778", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}], "display": "385 U.S. 293", "official": {"cite": "385 U.S. 293", "page": "293", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "385"}, "official_selection_present": true, "record_id": "Hoffa v. United States"}}
{"assertion_id": "099b0819c5e54600", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-310a", "record_id": "Hoffa v. United States"}, "payload": {"fragment": "#:~:text=The%20police%20are%20not%20required", "page": null, "pin_id": "pin-310a", "pinpoint_status": "star-verified", "quote": "The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long.", "quote_fidelity": "matched", "record_id": "Hoffa v. United States", "star_marker": "310"}}
{"assertion_id": "1354caa3c8a1cad5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-310", "record_id": "Hoffa v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-310", "pinpoint_status": "slip-only", "quote": "trial, a local union official, Edward Partin, was with Hoffa's entourage and reported to the government that Hoffa made statements about attempting to bribe jurors. Hoffa was later convicted of jury tampering largely on Partin's testimony. Hoffa argued, among other things, that the government violated his Sixth Amendment right to counsel by failing to arrest him as soon as it had probable cause, which (he said) would have caused the right to attach before the statements were made. ## Issue Whether the government violates the Sixth Amendment right to counsel when an informant obtains incriminating statements before adversary proceedings have begun, where the government did not arrest or charge the suspect earlier even though it may have had grounds to do so. ## Rule No. The Court rejected the contention that the government must arrest a suspect as soon as it has probable cause so that the right to counsel will attach:", "quote_fidelity": "mismatch", "record_id": "Hoffa v. United States", "star_marker": null}}
{"assertion_id": "aff37993a7328bad", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hoffa v. United States"}, "payload": {"as_of_content": "1966-12-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hoffa v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Hoffa v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hoffa v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hoffa v. United States",
    "case_name_short": "Hoffa",
    "case_name_full": "Hoffa v. United States",
    "input_case_name": "Hoffa v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-12-12",
    "year": 1966,
    "docket": null,
    "cluster_id": 107318,
    "lead_opinion_id": 9423305,
    "sibling_ids": [
      107318,
      9423305,
      9423306
    ],
    "absolute_url": "/opinion/107318/hoffa-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8963329,
        "score": 20,
        "case_name": "Hoffa v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 293",
      "volume": "385",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 408",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 374",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2778",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2778",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 293",
        "volume": "385",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 408",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "408",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 374",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "374",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2778",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2778",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-310",
      "page": null,
      "quote": "trial, a local union official, Edward Partin, was with Hoffa's entourage and reported to the government that Hoffa made statements about attempting to bribe jurors. Hoffa was later convicted of jury tampering largely on Partin's testimony. Hoffa argued, among other things, that the government violated his Sixth Amendment right to counsel by failing to arrest him as soon as it had probable cause, which (he said) would have caused the right to attach before the statements were made. ## Issue Whether the government violates the Sixth Amendment right to counsel when an informant obtains incriminating statements before adversary proceedings have begun, where the government did not arrest or charge the suspect earlier even though it may have had grounds to do so. ## Rule No. The Court rejected the contention that the government must arrest a suspect as soon as it has probable cause so that the right to counsel will attach:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-310a",
      "page": null,
      "quote": "The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long.",
      "star_marker": "310",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 32674,
      "fragment": "#:~:text=The%20police%20are%20not%20required",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hoffa v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Sosa",
          "cluster_id": 9447945,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bernard West v. United States",
          "cluster_id": 2735560,
          "cite": [
            "100 A.3d 1076",
            "2014 D.C. App. LEXIS 382",
            "2014 WL 4636023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fausto Camacho (072525)",
          "cluster_id": 2708330,
          "cite": [
            "218 N.J. 533",
            "95 A.3d 635",
            "2014 WL 3819161",
            "2014 N.J. LEXIS 804"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Preston v. State",
          "cluster_id": 2686475,
          "cite": [
            "218 Md. App. 60",
            "96 A.3d 800",
            "2014 WL 3736529",
            "2014 Md. App. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agbodjan",
          "cluster_id": 8716573,
          "cite": [
            "871 F. Supp. 2d 95",
            "2012 WL 2552140"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Caldwell v. Cablevision Systems Corp.",
          "cluster_id": 5969116,
          "cite": [
            "86 A.D.3d 46",
            "925 N.Y.2d 103"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Miranda",
          "cluster_id": 6580219,
          "cite": [
            "458 Mass. 100",
            "934 N.E.2d 222",
            "2010 Mass. LEXIS 685"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander",
          "cluster_id": 167490,
          "cite": [
            "447 F.3d 1290",
            "2006 U.S. App. LEXIS 11993",
            "2006 WL 1314663"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cabral",
          "cluster_id": 6579075,
          "cite": [
            "443 Mass. 171",
            "819 N.E.2d 951",
            "2005 Mass. LEXIS 1"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane1_negative"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nixon",
          "cluster_id": 109101,
          "cite": [
            "41 L. Ed. 2d 1039",
            "94 S. Ct. 3090",
            "418 U.S. 683",
            "1974 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marion",
          "cluster_id": 108420,
          "cite": [
            "30 L. Ed. 2d 468",
            "92 S. Ct. 455",
            "404 U.S. 307",
            "1971 U.S. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lovasco",
          "cluster_id": 109682,
          "cite": [
            "52 L. Ed. 2d 752",
            "97 S. Ct. 2044",
            "431 U.S. 783",
            "1977 U.S. LEXIS 107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weatherford v. Bursey",
          "cluster_id": 109590,
          "cite": [
            "51 L. Ed. 2d 30",
            "97 S. Ct. 837",
            "429 U.S. 545",
            "1977 U.S. LEXIS 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andresen v. Maryland",
          "cluster_id": 109522,
          "cite": [
            "49 L. Ed. 2d 627",
            "96 S. Ct. 2737",
            "427 U.S. 463",
            "1976 U.S. LEXIS 78"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 109433,
          "cite": [
            "48 L. Ed. 2d 71",
            "96 S. Ct. 1619",
            "425 U.S. 435",
            "1976 U.S. LEXIS 148",
            "37 A.F.T.R.2d (RIA) 1261"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 108304,
          "cite": [
            "28 L. Ed. 2d 453",
            "91 S. Ct. 1122",
            "401 U.S. 745",
            "1971 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
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
        "journal_ref": "Hoffa v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107318 OR 9423305 OR 9423306) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDUwMzY0ODAwMDAwJnM9MjQ4MDM5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107318+OR+9423305+OR+9423306%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107318 OR 9423305 OR 9423306)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTUmcz0yMDE0MDM0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107318+OR+9423305+OR+9423306%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107318 OR 9423305 OR 9423306)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 1,
        "triage_snippet_classified": 11
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107318 OR 9423305 OR 9423306)",
    "indexed_citing_opinions": 1482,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107318,
        "count": 1364,
        "count_source": "search"
      },
      {
        "opinion_id": 9423305,
        "count": 145,
        "count_source": "search"
      },
      {
        "opinion_id": 9423306,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2107,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hoffa-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NzkwMTMmcz02NDc0NzI5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107318+OR+9423305+OR+9423306%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107318,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 225410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 232188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 235478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 268758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107318,
        "cited_id": 272323,
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
    "date_created": "2026-07-05T07:14:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:19:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:15:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hoffa v. United States

```
<opinion type="majority">
<author id="b398-11">Mr. Justice Stewart</author>
<p id="AM2">delivered the opinion of the Court.</p>
<p id="b398-12">Over a period of several weeks in the late autumn of 1962 there took place in a federal court in Nashville, Tennessee, a trial by jury in which James Hoffa was charged with violating a provision of the Taft-Hartley Act. That trial, known in the present record as the Test Fleet trial, ended with a hung jury. The petitioners now before <em>us </em>— James <em>Hoffa, </em>Thomas Parks, Larry Campbell, and Ewing King — were tried and convicted <page-number citation-index="1" label="295">*295</page-number>in 1964 for endeavoring to bribe members of that jury.<footnotemark>1</footnotemark> The convictions were affirmed by the Court of Appeals.<footnotemark>2</footnotemark> A substantial element in the Government’s proof that led to the convictions of these four petitioners was contributed by a witness named Edward Partin, who testified to several incriminating statements which he said petitioners Hoffa and King had made in his presence during the course of the Test Fleet trial. Our grant of certiorari was limited to the single issue of whether the Government’s use in this case of evidence supplied by Partin operated to invalidate these convictions. <span class="citation multiple-matches"><a href="/c/U.%20S./382/1024/">382 U. S. 1024</a></span>.</p>
<p id="b399-5">The specific question before us, as framed by counsel for the petitioners, is this:</p>
<blockquote id="b399-6">“Whether evidence obtained by the Government by means of deceptively placing a secret informer in the quarters and councils of a defendant during one criminal trial so violates the defendant’s Fourth, Fifth and Sixth Amendment rights that suppression of such evidence is required in a subsequent trial of the same defendant on a different charge.”</blockquote>
<p id="b399-7">At the threshold the Government takes issue with the way this question is worded, refusing to concede that it “ ‘placed’ the informer anywhere, much less that it did so., ‘deceptively.’ ” In the view we take of the matter, however, a resolution of this verbal controversy is unnecessary to a decision of the constitutional issues before üs. The-basic facts are clear enough, and a lengthy discussion of the detailed minutiae to which a large portion of the' briefs and oral arguments was addressed would serve only to divert attention from the real issues before us.</p>
<p id="b400-3"><page-number citation-index="1" label="296">*296</page-number>The controlling facts can be briefly stated. The Test Fleet trial, in which James Hoffa was the sole individual defendant, was in progress between October 22 and December 23, 1962, in Nashville, Tennessee. James Hoffa was president of the International Brotherhood of Teamsters. During the course of the trial he occupied a three-room suite in the Andrew Jackson Hotel in Nashville. One of his constant companions throughout the trial was the petitioner King, president of the Nashville local of the Teamsters Union. Edward Partin, a resident of Baton Rouge, Louisiana, and a local Teamsters Union official there, made repeated visits to Nashville during the period of the trial. On these visits he frequented the Hoffa hotel suite, and was continually in the company of Hoffa and his associates, including King, in and around the hotel suite, the hotel lobby, the courthouse, and elsewhere in Nashville. During this period Partin made frequent reports to a federal agent named Sheridan concerning conversations he said Hoffa and King had had with him and with each other, disclosing endeavors to bribe members of the Test Fleet jury. Partin’s reports and his subsequent testimony at the petitioners’ trial unquestionably contributed, directly or indirectly, to the convictions of all four of the petitioners.<footnotemark>3</footnotemark></p>
<p id="b401-4"><page-number citation-index="1" label="297">*297</page-number>The chain of circumstances which led Partin to be in Nashville during the Test Fleet trial extended back at least to September of 1962. At that time Partin was in jail in Baton Rouge on a state criminal charge. He was <page-number citation-index="1" label="298">*298</page-number>also under a federal indictment for embezzling union funds, and other indictments for state offenses were pending against him. Between that time and Partin’s initial visit to Nashville on October 22 he was released on bail on the state criminal charge, and proceedings under the federal indictment were postponed. On October 8, Partin telephoned Hoffa in Washington, D. C., to discuss local union matters and Partin’s difficulties with the authorities. In the course of this conversation Partin asked if he could see Hoffa to confer about these problems, and Hoffa acquiesced. Partin again called Hoffa on October 18 and arranged to meet him in Nashville. During this period Partin also consulted on several occasions with federal law enforcement agents, who told him that Hoffa might attempt to tamper with the Test Fleet jury, and asked him to be on the lookout in Nashville for such attempts and to report to the federal authorities any evidence of wrongdoing that he discovered. Partin agreed to do so.</p>
<p id="b402-5">After the Test Fleet trial was completed, Partin’s wife received four monthly installment payments of $300 from government funds, and the state and federal charges against Partin were either dropped or not actively pursued.</p>
<p id="b402-6">Reviewing these circumstances in detail, the Govern-"inent insists the fair inference is that Partin went to Nashville on his own initiative to discuss union busi- „ ness and his own problems with Hoffa, that Partin ultimately cooperated closely with federal authorities only after he discovered evidence of jury tampering in the [ Test Fleet trial, that the payments to Partin’s wife were -simply in partial reimbursement of Partin’s subsequent out-of-pocket expenses, and that the failure to prosecute Partin on the state and federal charges had no necessary connection with his services as an informer. The findings of the trial court support this version of the <page-number citation-index="1" label="299">*299</page-number>facts,<footnotemark>4</footnotemark> and these findings were accepted by the Court of Appeals as “supported by substantial evidence.” 349 F. 2d, at 36. But whether or not the Government “placed” Partin with Hoffa in Nashville during the Test Fleet trial, we proceed upon the premise that Partin was a government informer from the time he first arrived in Nashville on October 22, and that the Government compensated him for his services as such. It is upon that premise that we consider the constitutional issues presented.</p>
<p id="b403-5">Before turning to those issues we mention an additional preliminary contention of the Government. The <page-number citation-index="1" label="300">*300</page-number>petitioner Hoffa was the only individual defendant in the Test Fleet case, and Partin had conversations during the Test Fleet trial only with him and with the petitioner King. So far as appears, Partin never saw either of the other two petitioners during that period. Consequently, the Government argues that, of the four petitioners, only Hoffa has standing to raise a claim that his Sixth Amendment right to counsel in the Test Fleet trial was impaired, and only he and King have standing with respect to the other constitutional claims. Cf. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 487-488, 491-492</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 259-267</a></span>. It is clear, on the other hand, that Partin’s reports to the agent Sheridan uncovered leads that made possible the development of evidence against petitioners Parks and Campbell. But we need not pursue the nuances of these “standing” questions, because it is evident in any event that none of the petitioners can prevail unless the petitioner Hoffa prevails. For that reason, the ensuing discussion is confined to the claims of the petitioner Hoffa (hereinafter petitioner), all of which he clearly has standing to invoke.</p>
<p id="b404-4">I.</p>
<p id="b404-5">It is contended that only by violating the petitioner’s rights under the Fourth Amendment was Partin able to hear the petitioner’s incriminating statements in the hotel suite, and that Partin’s testimony was therefore inadmissible under the exclusionary rule of <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. The argument is that Partin’s failure to disclose his role as a government informer vitiated the consent that the petitioner gave to Partin’s repeated entries into the suite, and that by listening to the petitioner’s statements Partin conducted an illegal “search” for verbal evidence.</p>
<p id="b405-4"><page-number citation-index="1" label="301">*301</page-number>The preliminary steps of this argument are on solid ground. A hotel room can clearly be the object of Fourth Amendment protection as much as a home or an office. <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. The Fourth Amendment can certainly be violated by guileful as well as by forcible intrusions into a constitutionally protected area. <em>Gouled </em>v. <em>United States, 255 </em>U. S. 298. And the protections of the Fourth Amendment are surely not limited to tangibles, but can extend as well to oral statements. <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>.</p>
<p id="b405-5">Where the argument falls is in its misapprehension of the fundamental nature and scope of Fourth Amendment protection. What the Fourth Amendment protects is the security a man relies upon when he places himself or his property within a constitutionally protected area, be it his home or his office, his hotel room or his automobile.<footnotemark>5</footnotemark> There he is protected from unwarranted governmental intrusion. And when he puts something in his filing cabinet, in his desk drawer, or in his pocket, he has the right to know it will be secure from an unreasonable search or an unreasonable seizure. So it was that the Fourth Amendment could not tolerate the warrantless search of the hotel room in <em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span>, </em>the purloining of the petitioner’s private papers in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>, </em>or the surreptitious electronic surveillance in <em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span>. </em>Countless other cases which have come to this Court ovér the years have involved a myriad of differing factual contexts in which the protections of the Fourth Amendment have been appropriately invoked. No doubt the future will bring countless others. By nothing we say here do we either foresee or foreclose factual <page-number citation-index="1" label="302">*302</page-number>situations to which the Fourth Amendment may be applicable.</p>
<p id="b406-4">In the present case, however, it is evident that no interest legitimately protected by the Fourth Amendment is involved. It is obvious that the petitioner was not relying on the security of his hotel suite when he made the incriminating statements to Partin or in Partin's presence. Partin did not enter the suite by force or by stealth. He was not a surreptitious eavesdropper. Partin was in the suite by invitation, and every conversation which he heard was either directed to him or knowingly carried on in his presence. The petitioner, in a word, was not relying on the security of the hotel room; he was relying upon his misplaced confidence that Partin would not reveal his wrongdoing.<footnotemark>6</footnotemark> As counsel for the petitioner himself points out, some of the communications with Partin did not take place in the suite at all, but in the “hall of the hotel,” in the “Andrew Jackson Hotel lobby,” and “at the courthouse.”</p>
<p id="b406-5">Neither this Court nor any member of it has ever expressed the view that the Fourth Amendment protects a wrongdoer’s misplaced belief that a person to whom he voluntarily confides his wrongdoing will not reveal it. Indeed, the Court unanimously rejected that very contention less than four years ago in <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>. In that case the petitioner had" been convicted of attempted bribery of an internal revenue agent named Davis. The Court was divided with regard to the admissibility in evidence of a surreptitious electronic recording of an incriminating conversation Lopez had had in his private office with Davis. But there was no dissent from the view that testimony <page-number citation-index="1" label="303">*303</page-number>about the conversation by Davis himself was clearly admissible.</p>
<p id="b407-5">As the Court put it, “Davis was not guilty of an unlawful invasion of petitioner’s office simply because his apparent willingness to accept a bribe was not real. Compare <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span>. He was in the office with petitioner’s consent, and while there he did not violate the privacy of the office by seizing something surreptitiously without petitioner’s knowledge. Compare <em>Gouled </em>v. <em>United States, supra. </em>The only evidence obtained consisted of statements made by Lopez to Davis, statements which Lopez knew full well could be used against him by Davis if he wished. ...” <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#438" aria-description="Citation for case: Lopez v. United States">373 U. S., at 438</a></span>. In the words of the dissenting opinion in <em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">Lopez</a></span>, </em>“The risk of being overheard by an eavesdropper or betrayed by an informer or deceived as to the identity of one with whom one deals is probably inherent in the conditions of human society. It is the kind of risk we necessarily assume whenever we speak.” <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#465" aria-description="Citation for case: Lopez v. United States"><em>Id., </em>at 465</a></span>. See also <em>Lewis </em>v. <em>United States, ante, </em>p. 206.</p>
<p id="b407-6">Adhering to these views, we hold that no right protected by the Fourth Amendment was violated in the present case.</p>
<p id="b407-7">II.</p>
<p id="b407-8">The petitioner argues that his right under the Fifth Amendment not to “be compelled in any criminal case to be a witness against himself” was violated by the admission of Partin’s testimony. The claim is without merit.</p>
<p id="b407-9">There have been sharply differing views within the Court as to the ultimate reach of the Fifth Amendment right against compulsory self-incrimination. Some of those differences were aired last Term in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#499" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 499, 504, 526</a></span>. But since at least as long ago as 1807, when Chief Justice Marshall first <page-number citation-index="1" label="304">*304</page-number>gave attention to the matter in the trial of Aaron Burr,<footnotemark>7</footnotemark> all have agreed that a necessary element of compulsory self-incrimination is some kind of compulsion. Thus, in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case, dealing with the Fifth Amendment’s impact upon police interrogation of persons in custody, the Court predicated its decision upon the conclusion “that without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual’s will to resist and to compel him to speak where he would not otherwise do so freely. . . .” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>.</p>
<p id="b408-6">In the present case no claim has been or could be made that the petitioner’s incriminating statements were the product of any sort of coercion, legal or factual. The petitioner’s conversations with Partin and in Partin’s presence were wholly voluntary. For that reason, if for no other, it is clear that no right protected by the Fifth Amendment privilege against compulsory self-incrimination was violated in this case.</p>
<p id="b408-7">III.</p>
<p id="b408-8">The petitioner makes two separate claims under the Sixth Amendment, and we give them separate consideration.</p>
<p id="b408-9">A.</p>
<p id="b408-10">During the course of the Test Fleet trial the petitioner’s lawyers used his suite as a place to confer with him and with each other, to interview witnesses, and to plan the following day’s trial strategy. Therefore, <page-number citation-index="1" label="305">*305</page-number>argues the petitioner, Partin’s presence in and around the suite violated the petitioner’s Sixth Amendment i right to counsel, because an essential ingredient thereof is the right of a defendant and his counsel to prepare for trial without intrusion upon their confidential relationship by an agent of the Government, the defendant’s i trial adversary. Since Partin’s presence in the suite thus I violated the Sixth Amendment, the argument continues, any evidence acquired by reason of his presence there I was constitutionally tainted and therefore inadmissible <em>I </em>against the petitioner in this case. We reject this <em>I </em>argument.</p>
<p id="b409-6">In the first place, it is far from clear to what extent Partin was present at conversations or conferences of the petitioner’s counsel. Several of the petitioner’s Test Fleet lawyers testified at the hearing on the motion to suppress Partin’s testimony in the present case. Most of them said that Partin had heard or had been in a position to hear at least some of the lawyers’ discussions during the Test Fleet trial. On the other hand, Partin himself testified that the lawyers “would move you out” when they wanted to discuss the case, and denied that he made any effort to “get into or be present at any conversations between lawyers or anything of that sort,” other than engaging in such banalities as “how things looked,” or “how does it look?” He said he might have heard some of the lawyers’ conversations, but he didn’t know what they were talking about, “because I wasn’t interested in what they had to say about the case.” He testified that he did not report any of the lawyers’ conversations to Sheridan, because the latter “wasn’t interested in what the attorneys said.” Partin’s testimony was largely confirmed by Sheridan. Sheridan did testify, however, to one occasion when Partin told him about a group of prospective character witnesses being interviewed in the suite by one of the petitioner’s lawyers, who “was going <page-number citation-index="1" label="306">*306</page-number>over” some written “questions and answers” with them. This information was evidently relayed by Sheridan to the chief government attorney at the Test Fleet trial.<footnotemark>8</footnotemark></p>
<p id="b410-6">The District Court in the present case apparently credited Partin’s testimony, finding “there has been no interference by the government with any attorney-client relationship of any defendant in this case.” The Court of Appeals accepted this finding. 349 F. 2d, at 36. In view of Sheridan’s testimony about Partin’s report of the interviews with the prospective character witnesses, however, we proceed here on the hypothesis that Partin did observe and report to Sheridan at least some of the L.activities of defense counsel in the Test Fleet trial.</p>
<p id="b410-7">The proposition that a surreptitious invasion by a government agent into the legal camp of the defense may violate the protection of the Sixth Amendment has found expression in two cases decided by the Court of Appeals for the District of Columbia Circuit, <em>Caldwell </em>v. <em>Unite</em>d <em>States, </em>92 U. S. App. D. C. 355, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">205 F. 2d 879</a></span>, and <em>Coplon </em>v. <em>United States, </em>89 U. S. App. D. C. 103, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749</a></span>. Both of those cases dealt with government intrusion of the grossest kind upon the confidential relationship between the defendant and his counsel. In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>, </em>the <page-number citation-index="1" label="307">*307</page-number>defendant alleged that government agents deliberately-intercepted telephone consultations between the defendant and her lawyer before and during trial. In <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>the agent, “[i]n his dual capacity as defense assistant and Government agent. . . gained free access to the planning of the defense. . . . Neither his dealings with the defense nor his reports to the prosecution were limited to the proposed unlawful acts of the defense: they covered many matters connected with the impending trial.” 92 U. S. App. D. C., at 356, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#880" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 880</a></span>.</p>
<p id="b411-5">’ We may assume that the <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>cases : were rightly decided, and further assume, without deciding, that the Government’s activities during the Test ¡Fleet trial were sufficiently similar to what went on in j <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>to invoke the rule of those decisions, f Consequently, if the Test Fleet trial had resulted in a j conviction instead of a hung jury, the conviction would j presumptively have been set aside as constitutionally ; defective. Cf. <em>Black </em>v. <em>United States, ante, </em>p. 26.</p>
<p id="b411-6">! But a holding that it follows from this presumption Cthat the petitioner’s conviction in the present case should be set aside would be both unprecedented and irrational. In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>and in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>the Court of Appeals held [that the Government’s intrusion upon the defendant’s ¡relationship with his lawyer “invalidates the trial at [which it occurred.” 89 U. S. App. D. C., at 114, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/#759" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d, at 759</a></span>; 92 U. S. App. D. C., at 357, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#881" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 881</a></span>. In both of those cases the court directed a new trial,<footnotemark>9</footnotemark> and the second trial in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>resulted in a conviction which this Court declined to review. 95 U. S. App. D. C. 35, <span class="citation" data-id="9444417"><a href="/opinion/235478/bennie-c-caldwell-v-united-states/" aria-description="Citation for case: Bennie C. Caldwell v. United States">218 F. 2d 370</a></span>, <span class="citation multiple-matches"><a href="/c/U.%20S./349/930/">349 U. S. 930</a></span>. The argument here, therefore, goes far beyond anything decided in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>or in <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>. </em>For if the petitioner’s argument were accepted, <page-number citation-index="1" label="308">*308</page-number>not only could there have been no new conviction on the existing charges in <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span>, </em>but not even a conviction on other and different charges against the same defendant.</p>
<p id="b412-6">It is possible to imagine a case in which the prosecution might so pervasively insinuate itself into the councils of the defense as to make a new trial on the same charges impermissible under the Sixth Amendment.<footnotemark>10</footnotemark> But even if it were further arguable that a situation could be hypothesized in which the Government’s previous activities in undermining a defendant’s Sixth Amendment rights at one trial would make evidence obtained thereby inadmissible in a different trial on other charges, the case now before us does not remotely approach such a situation.</p>
<p id="b412-7">This is so because of the clinching basic fact in the present case that none of the petitioner’s incriminating • statements which Partin heard were made in the presence of counsel, in the hearing of counsel, or in connection in any way with the legitimate defense of the Test Fleet prosecution. The petitioner’s statements related to the commission of a quite separate offense— attempted bribery of jurors — and the statements were made to Partin out of the presence of any lawyers.</p>
<p id="b412-8">Even assuming, therefore, as we have, that there might have been a Sixth Amendment violation which might have made invalid a conviction, if there had been one, in the Test Fleet case, the evidence supplied by Partin in the present case was in no sense the “fruit” of any such violation. In <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span>, a case involving exclusion of evidence under <page-number citation-index="1" label="309">*309</page-number>the Fourth Amendment, the Court stated that “the more apt question in such a case is ‘whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.’ Maguire, Evidence of Guilt, 221 (1959).” <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488</a></span>.</p>
<p id="b413-5">Even upon the premise that this same strict standard of excludability should apply under the Sixth Amendment — a question we need not decide — it is clear that Partin’s evidence in this case was not the consequence of any “exploitation” of a Sixth Amendment violation. The petitioner’s incriminating statements to which Partin testified in this case were totally unrelated in both time and subject matter to any assumed intrusion by Partin into the conferences of the petitioner’s counsel in the Test Fleet trial. These incriminating statements, all of them made out of the presence or hearing of any of the petitioner’s counsel, embodied the very antithesis of any legitimate defense in the Test Fleet trial.</p>
<p id="b413-6">B.</p>
<p id="b413-7">The petitioner’s second argument under the Sixth Amendment needs no extended discussion. That argument goes as follows: Not later than October 25, 1962, the Government had sufficient ground for taking the petitioner into custody and charging him with endeavors to tamper with the Test Fleet jury. Had the Government done so, it could not have continued to question the petitioner without observance of his Sixth Amendment right to counsel. <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>. Therefore, the argument concludes, evidence of statements <page-number citation-index="1" label="310">*310</page-number>made by the petitioner subsequent to October 25 was inadmissible, because the Government acquired that evidence only by flouting the petitioner’s Sixth Amendment right to counsel.</p>
<p id="b414-6">Nothing in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>, </em>in <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span>, </em>or in any other case that has come to our attention, even remotely suggests this novel and paradoxical constitutional doctrine, and we decline to adopt it now. There is no constitutional right to be arrested.<footnotemark>11</footnotemark> The police are not required to guess at their peril the precise moment at which they have probable cause to arrest a suspect, risking a violation of the Fourth Amendment if they act too soon, and a violation of the Sixth Amendment if they wait too long. Law enforcement officers are under no constitutional duty to call a halt to a criminal investigation the moment they have the minimum evidence to establish probable cause, a quantum of evidence which may fall far short of the amount necessary to support a criminal conviction.</p>
<p id="b414-7">IV.</p>
<p id="b414-8">Finally, the petitioner claims that even if there was no violation — “as separately measured by each such Amendment” — of the Fourth Amendment, the compulsory self-incrimination clause of the Fifth Amendment, or of the Sixth Amendment in this case, the judgment of conviction must nonetheless be reversed. The argument is based upon the Due Process Clause of the Fifth Amendment. The “totality” of the Government’s conduct during the Test Fleet trial operated, it is said, to “ ‘offend those canons of decency and fairness which express the notions of justice of English-speaking peoples <page-number citation-index="1" label="311">*311</page-number>even toward those charged with the most heinous offenses’ <em>(Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span>).”</p>
<p id="b415-5">The argument boils down to a general attack upon the use of a government informer as “a shabby thing in any case,” and to the claim that in the circumstances of this particular case the risk that Partin’s testimony might be perjurious was very high. Insofar as the general attack upon the use of informers is based upon historic “notions” of “English-speaking peoples,” it is without historical foundation. In the words of Judge Learned Hand, “Courts have countenanced the use of informers from time immemorial; in cases of conspiracy, or in other cases when the crime consists of preparing for another crime, it is usually necessary to rely upon them or upon accomplices because the criminals will almost certainly proceed covertly. . . .” <em>United States </em>v. <em>Dennis, </em><span class="citation" data-id="9442514"><a href="/opinion/225410/united-states-v-dennis/#224" aria-description="Citation for case: United States v. Dennis">183 F. 2d 201, at 224</a></span>.</p>
<p id="b415-6">This is not to say that a secret government informer is to the slightest degree more free from all relevant constitutional restrictions than is any other government agent. See <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>. It <em>is </em>to say that the use of secret informers is not <em>per se </em>unconstitutional.</p>
<p id="b415-7">The petitioner is quite correct in the contention that Partin, perhaps even more than most informers, may have had motives to lie. But it does not follow that his testimony was untrue, nor does it follow that his testimony was constitutionally inadmissible. The established safeguards of the Anglo-American legal system leave the veracity of a witness to be tested by cross-examination, and the credibility of his testimony to be determined by a properly instructed jury. At the trial of this case, Partin was subjected to rigorous cross-examination, and the extent and nature of his dealings with federal and state authorities were insistently ex<page-number citation-index="1" label="312">*312</page-number>plored.<footnotemark>12</footnotemark> The trial judge instructed the jury, both specifically<footnotemark>13</footnotemark> and generally,<footnotemark>14</footnotemark> with regard to assessing Partin’s credibility. The Constitution does not require us to upset the jury’s verdict.</p>
<p id="b416-4">
<em>Affirmed.</em>
</p>
<judges id="b416-5">Mr. Justice White and Mr. Justice Fortas took no part in the consideration or decision of these cases.</judges>
<p id="b416-6">[For opinion of Mr. Justice Douglas, see <em>post, </em>p. 340.]</p>
<footnote label="1">
<p id="b399-8"> Petitioners Hoffa, Parks, and Campbell were convicted under <span class="citation no-link">18 U. S. C. § 1503</span> for endeavoring corruptly to influence Test Fleet juror Gratín Fields. Petitioners Hoffa and King Were convicted of a similar offense involving Test Fleet juror Mrs. James M. Paschal.</p>
</footnote>
<footnote label="2">
<p id="b399-9"> <span class="citation" data-id="268758"><a href="/opinion/268758/united-states-v-james-r-hoffa-united-states-of-america-v-thomas-ewing/" aria-description="Citation for case: United States v. James R. Hoffa, United States of America...">349 F. 2d 20</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b400-4"> Partin testified at the trial of this case that petitioners Hoffa and King had made the following statements during the course of the Test Fleet trial:</p>
<p id="b400-5">On October 22, the day Partin first arrived in Nashville, King told him that a meeting had been “set up on the jury that night.” That evening Hoffa told Partin that he wanted Partin to stay in Nashville in order to call on some people. Hoffa explained “that they was going to get to one juror or try to get to a few scattered jurors and take their chances.” The next day Partin was told by Hoffa that Hoffa might want him “to pass something for him.” As Hoffa said this, he hit his rear pocket with his hand. On October 25, the day after Test Fleet juror James Tippens had reported to the trial judge that he had been approached with a bribe offer, <page-number citation-index="1" label="297">*297</page-number>Partin asked Hoffa about his wanting Partin to “pass something.” Hoffa replied, “The dirty bastards went in and told the Judge that his neighbor had offered him $10,000,” and added, “We are going to have to lay low for a few days.” King told Partin on October 26 that he intended to influence a female juror, Mrs. Paschal, in Hoffa’s favor, and added that the juror and her husband, a highway patrolman, “loved money, and $10,000.00 [is] a lot of money.” Hoffa informed Partin on October 29 that he “would pay 15 or $20,000, whatever — whatever it cost to get to the jury.” On November 5, in Partin’s presence, Hoffa berated King for failing in his promises to "get the patrolman.” King then told Partin that he was arranging a meeting with the highway patrolman, but on November 7 King admitted to Partin that he had not yet contacted the highway patrolman and that Hoffa had been complaining “about not getting to the jury.” Hoffa criticized King in the presence of Partin on November 14 for “not making a contact like he told him he would,” adding that he “wanted some insurance.” Later the same day, King told Partin that he had arranged to meet with the highway patrolman, and that he had prepared a cover story to allay suspicion. On November 15 Hoffa asked King in Partin’s presence whether he had “made the contacts.” King related to Partin on November 20 a meeting that King had had with juror Paschal’s husband, stating that the highway patrolman wanted a promotion rather than money. The same day Hoffa told Partin that he was disturbed because “the Highway Patrolman wouldn’t take the money,”' adding that if he had “taken the money it would have pinned him down and he couldn’t have backed up.”</p>
<p id="b401-6">There was other evidence at the trial that petitioner Campbell, a union associate of Hoffa’s, and petitioner Parks, Campbell’s uncle, had made bribe offers to Gratín Fields, a Negro juror. On November 7, according to Partin, Hoffa told Partin that he had “the colored male juror in [his] hip pocket,” and that Campbell “took care of it.” Hoffa told Partin that Campbell, a Negro, was related to Fields, and that while Fields had refused the bribe he would not “go against his own people.” Hoffa concluded, “ [IJt looks like our best bet is a hung jury unless we can get to the foreman of the jury. If they have a hung jury, it will be the same as acquittal because they will never try the ease again.”</p>
</footnote>
<footnote label="4">
<p id="b403-6"> In denying the defense motion to suppress Partin’s testimony, the trial court stated: “I would further find that the government did not place this witness Mr. Partin in the defendants’ midst or have anything to do with placing him in their midst, rather that he was knowingly and voluntarily placed in their midst by one of the defendants.”</p>
<p id="b403-7">The trial court’s memorandum denying a motion for a new trial contained the following statement:</p>
<blockquote id="b403-8">“The action of the Court in denying the motions of the defendants to suppress the testimony of the witness Partin is complained of in Grounds 41 and 42 of the motions for new trial. It is contended that one of the findings of fact of the Court with respect to the motion to suppress was rendered incorrect by subsequent evidence in the case. It is contended that the telephone transcriptions of the telephone calls between Partin and Hoffa on October 8 and 18, 1962, established that the defendant Hoffa did not invite Partin to Nashville. The telephone transcriptions reflect that the defendant Hoffa agreed to an appointment to see Partin in Nashville. Even if the defendant Hoffa did not initiate the invitation of Partin to come to Nashville, but rather Partin solicited the invitation, this does not in any way alter the Court’s finding that the Government did not place or keep Partin with the defendant Hoffa. . . . The Government requested of Partin only that he report information of jury tampering or other illegal activity of which he became aware. Partin voluntarily furnished such information. He remained in Nashville or returned to Nashville either at the request or with the consent of the defendant Hoffa and not at the instruction of the Government.”</blockquote>
</footnote>
<footnote label="5">
<p id="b405-6"> We do not deal here with the law of arrest under the Fourth Amendment.</p>
</footnote>
<footnote label="6">
<p id="b406-6"> The applicability of the Fourth Amendment if Partin had been a stranger to the petitioner is a question we do not decide. Cf. <em>Lewis </em>v. <em>United States, ante, </em>p. 206.</p>
</footnote>
<footnote label="7">
<p id="b408-11"> “Many links frequently compose that chain of testimony which is necessary to convict any individual of a crime. It appears to the court to be the true sense of the rule that no witness is <em>com-pellable </em>to furnish any one of them against himself. . . .” <em>In re Willie, </em><span class="citation" data-id="8638363"><a href="/opinion/8658512/united-states-v-burr/#40" aria-description="Citation for case: United States v. Burr">25 Fed. Cas. 38, 40</a></span> (No. 14,692e) (C. C. D. Va. 1807). (Emphasis supplied.)</p>
</footnote>
<footnote label="8">
<p id="b410-8"> Petitioner maintains that the cross-examination of one of these character witnesses at the Test Fleet trial shows that the prosecution availed itself of the information transmitted by Partin. The following exchange between the prosecutor and witness occurred:</p>
<blockquote id="b410-9">Q. “Did [defense counsel] give you anything to read, Mr. Sammut?”</blockquote>
<blockquote id="b410-10">A. “No, sir, not even a newspaper.”</blockquote>
<blockquote id="b410-11">Q. “Not even a newspaper? I am not talking about newspapers, I am talking with respect to your testimony. Did they give you anything to read with respect to your testimony?”</blockquote>
<blockquote id="b410-12">A. “After I talked to them.”</blockquote>
<blockquote id="b410-13">Q. “They gave you written questions and answers, didn’t they?”</blockquote>
<blockquote id="b410-14">A. “The questions that they asked me and the questions that I answered.”</blockquote>
</footnote>
<footnote label="9">
<p id="b411-7"> In <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span>, </em>the grant of a new trial was conditioned on the defendant’s proof of her wiretapping allegations.</p>
</footnote>
<footnote label="10">
<p id="b412-9"> In the <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>case, the Court of Appeals implicitly recognized the possibility of a case arising in which a showing could be made of “prejudice to the defense of such a nature as would necessarily render a subsequent trial unfair to the accused.” 92 U. S. App. D. <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#355" aria-description="Citation for case: Caldwell v. United States">C. 355, 357, n. 11, 205 F. 2d 879, 881-882, n. 11</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b414-9"> We put to one side the extraordinary problems that would have arisen if the petitioner had been arrested and charged during the progress of the Test Fleet trial.</p>
</footnote>
<footnote label="12">
<p id="b416-7"> Partin underwent cross-examination for an entire week. The defense was afforded wide latitude to probe Partin's background, character, and ties to the authorities; it was permitted to explore matters that are normally excludable, for example, whether Partin had been charged with a crime in 1942, even though that charge had never been prosecuted.</p>
</footnote>
<footnote label="13">
<p id="b416-8"> The judge instructed the jury that it was petitioner’s contention that he “did not invite Edward Partin to come to Nashville, Tennessee, during the trial of [the Test Fleet case]' but that the said Edward Partin came of his own accord under the pretense of attempting to convince Mr. Hoffa that the Teamsters local union in Baton Rouge, Louisiana should not be placed in trusteeship by reason of Partin’s being under indictment and other misconduct on Partin’s part, but for the real purpose of fabricating evidence against Hoffa in order to serve his own purposes and interests.”</p>
</footnote>
<footnote label="14">
<p id="b416-9"> The jury was instructed: “You should carefully scrutinize the testimony given and the circumstances under which each witness has testified, and every matter in evidence which tends to indicate whether the witness is worthy of belief. Consider each witness’ intelligence, his motives, state of mind, his demeanor and manner while on the witness stand. Consider also any relation each witness may bear to either side of the case .... All evidence of a witness whose self-interest is shown from either benefits received, detriments suffered, threats or promises made, or any attitude of the witness which might tend to prompt testimony either favorable or unfavorable to the accused should be considered with caution and weighed with care.”</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Hope v. Pelzer.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hope v. Pelzer"
type: case
citation: "536 U.S. 730 (2002)"
parallel_cite: "122 S. Ct. 2508; 153 L. Ed. 2d 666"
neutral_cite: 2002 U.S. LEXIS 4884
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2002
date_decided: 2002-06-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2002-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hope v. Pelzer
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/121169/hope-v-pelzer/"
  cluster_id: 121169
  opinion_id: 9434318
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Harlow v. Fitzgerald]]", "[[Saucier v. Katz]]", "[[City of Tahlequah v. Bond]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "clearly-established-law", "fair-warning"]
holding: "A right can be clearly established **without a factually identical case** — in an 'obvious case,' officials have fair warning even in novel circumstances (the QI 'obvious case' escape hatch)."
lake:
  record_id: Hope v. Pelzer
  status: verified
  projected_at: 2026-07-09
---

# Hope v. Pelzer

*536 U.S. 730 (2002)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Alabama prison guards twice handcuffed inmate Larry Hope to a "hitching post" for extended periods — once for about seven hours, shirtless in the sun, with little water and no bathroom breaks. Hope sued the guards under § 1983 for an Eighth Amendment violation; the guards claimed [[Qualified Immunity|qualified immunity]], and the Eleventh Circuit had granted it on the ground that no earlier case had "materially similar" facts.

## Issue
Whether [[Qualified Immunity|qualified immunity]] protects officials whenever no prior case has "materially similar" facts, or whether a right can be clearly established without such a factually identical precedent.

## Rule
A right may be clearly established without a factually identical case. "[O]fficials can still be on notice that their conduct violates established law even in novel factual circumstances." — 536 U.S. at 741. ^pin-741

The controlling inquiry is fair warning: "the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional." — [*Id.*](https://www.courtlistener.com/opinion/121169/hope-v-pelzer/#:~:text=the%20salient%20question%20that%20the) ^pin-741a

## Application
The Court held the guards had fair warning that handcuffing Hope to the hitching post was unlawful: binding circuit precedent, an Alabama Department of Corrections regulation, and a Justice Department report had all condemned the practice, and the wantonness of the conduct was obvious. Although no prior decision involved the identical hitching-post facts, the state of the law gave the guards fair warning, so they were not entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
The guards were not entitled to [[Qualified Immunity|qualified immunity]]; the Eleventh Circuit's "materially similar" requirement was rejected and its judgment reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hope* refines the "clearly established law" prong of [[Harlow v. Fitzgerald]] and [[Saucier v. Katz]], supplying the "fair warning" / obvious-case route to overcoming [[Qualified Immunity|qualified immunity]] even without a factually identical precedent.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Hope v. Pelzer*, 536 U.S. 730 (2002) — https://www.courtlistener.com/opinion/121169/hope-v-pelzer/ — pinpoint: 741.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6a36a85bd13279f4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hope v. Pelzer"}, "payload": {"all": [{"cite": "536 U.S. 730", "page": "730", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "536"}, {"cite": "122 S. Ct. 2508", "page": "2508", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "122"}, {"cite": "153 L. Ed. 2d 666", "page": "666", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "153"}, {"cite": "2002 U.S. LEXIS 4884", "page": "4884", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2002"}], "display": "536 U.S. 730", "official": {"cite": "536 U.S. 730", "page": "730", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "536"}, "official_selection_present": true, "record_id": "Hope v. Pelzer"}}
{"assertion_id": "98848fcc626429aa", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-741a", "record_id": "Hope v. Pelzer"}, "payload": {"fragment": "#:~:text=the%20salient%20question%20that%20the", "page": null, "pin_id": "pin-741a", "pinpoint_status": "star-verified", "quote": "the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional.", "quote_fidelity": "matched", "record_id": "Hope v. Pelzer", "star_marker": "741"}}
{"assertion_id": "c2bb0ff3b96b700a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-741", "record_id": "Hope v. Pelzer"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-741", "pinpoint_status": "slip-only", "quote": "facts, or whether a right can be clearly established without such a factually identical precedent. ## Rule A right may be clearly established without a factually identical case.", "quote_fidelity": "mismatch", "record_id": "Hope v. Pelzer", "star_marker": null}}
{"assertion_id": "bf611fb2b4a1a327", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hope v. Pelzer"}, "payload": {"as_of_content": "2002-06-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hope v. Pelzer", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Hope v. Pelzer

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hope v. Pelzer",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hope v. Pelzer",
    "case_name_short": "Hope",
    "case_name_full": "HOPE v. PELZER Et Al.",
    "input_case_name": "Hope v. Pelzer",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2002-06-27",
    "year": 2002,
    "docket": null,
    "cluster_id": 121169,
    "lead_opinion_id": 9434318,
    "sibling_ids": [
      121169,
      9434318,
      9434319
    ],
    "absolute_url": "/opinion/121169/hope-v-pelzer/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 119432,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 119246,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 9271893,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      },
      {
        "cluster_id": 9268772,
        "score": 20,
        "case_name": "Hope v. Pelzer"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "536 U.S. 730",
      "volume": "536",
      "reporter": "U.S.",
      "page": "730",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "122 S. Ct. 2508",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2508",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 666",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "666",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 U.S. LEXIS 4884",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "536 U.S. 730",
        "volume": "536",
        "reporter": "U.S.",
        "page": "730",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "122 S. Ct. 2508",
        "volume": "122",
        "reporter": "S. Ct.",
        "page": "2508",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "153 L. Ed. 2d 666",
        "volume": "153",
        "reporter": "L. Ed. 2d",
        "page": "666",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. LEXIS 4884",
        "volume": "2002",
        "reporter": "U.S. LEXIS",
        "page": "4884",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "536 U.S. 730",
    "official_selection": {
      "court_class": "scotus",
      "selected": "536 U.S. 730",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-741",
      "page": null,
      "quote": "facts, or whether a right can be clearly established without such a factually identical precedent. ## Rule A right may be clearly established without a factually identical case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-741a",
      "page": null,
      "quote": "the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional.",
      "star_marker": "741",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17898,
      "fragment": "#:~:text=the%20salient%20question%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hope v. Pelzer",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iko v. Shreve",
          "cluster_id": 1026358,
          "cite": [
            "535 F.3d 225",
            "2008 U.S. App. LEXIS 16607",
            "2008 WL 3018444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Berkshire v. Debra Dahl",
          "cluster_id": 4635241,
          "cite": [
            "928 F.3d 520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randall v. Scott",
          "cluster_id": 149841,
          "cite": [
            "610 F.3d 701",
            "76 Fed. R. Serv. 3d 1566",
            "30 I.E.R. Cas. (BNA) 1544",
            "2010 U.S. App. LEXIS 13377",
            "93 Empl. Prac. Dec. (CCH) 43,922",
            "2010 WL 2595585"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herbert L. Board v. Karl Farnham, Jr.",
          "cluster_id": 788844,
          "cite": [
            "394 F.3d 469",
            "2005 U.S. App. LEXIS 101",
            "2005 WL 18109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bingham v. Thomas",
          "cluster_id": 613095,
          "cite": [
            "654 F.3d 1171",
            "2011 U.S. App. LEXIS 18293",
            "2011 WL 3862101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terri Vinyard v. Steve Wilson",
          "cluster_id": 76029,
          "cite": [
            "311 F.3d 1340",
            "2002 U.S. App. LEXIS 23576",
            "2002 WL 31521208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
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
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Blake",
          "cluster_id": 168392,
          "cite": [
            "469 F.3d 910",
            "34 Media L. Rep. (BNA) 2505",
            "2006 U.S. App. LEXIS 28144",
            "2006 WL 3291688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dean Effarage Farrow v. Dr. West",
          "cluster_id": 76092,
          "cite": [
            "320 F.3d 1235",
            "2003 U.S. App. LEXIS 2163",
            "22 Fla. L. Weekly Fed. C 582"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gobert v. Caldwell",
          "cluster_id": 45544,
          "cite": [
            "463 F.3d 339",
            "2006 U.S. App. LEXIS 22216",
            "2006 WL 2474846"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mann v. Taser International, Inc.",
          "cluster_id": 78530,
          "cite": [
            "588 F.3d 1291",
            "2009 U.S. App. LEXIS 26155",
            "2009 WL 4279713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goebert v. Lee County",
          "cluster_id": 77881,
          "cite": [
            "510 F.3d 1312",
            "2007 U.S. App. LEXIS 29513",
            "2007 WL 4458122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dodds v. Richardson",
          "cluster_id": 158503,
          "cite": [
            "614 F.3d 1185",
            "2010 U.S. App. LEXIS 16326",
            "2010 WL 3064002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Scinto, Sr. v. Warden Stansberry",
          "cluster_id": 4318473,
          "cite": [
            "841 F.3d 219",
            "101 Fed. R. Serv. 1229",
            "2016 U.S. App. LEXIS 19936",
            "2016 WL 6543368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gary Blankenhorn v. City of Orange Andy Romero Dung Nguyen Garrett Ross Tamara South Gray, Sergeant Montano, Officer Kayano, Officer Roman, Officer",
          "cluster_id": 797658,
          "cite": [
            "485 F.3d 463",
            "2007 U.S. App. LEXIS 10856",
            "2007 D.A.R. 6484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laura Skop v. City of Atlanta, Georgia",
          "cluster_id": 77695,
          "cite": [
            "485 F.3d 1130",
            "2007 U.S. App. LEXIS 10341",
            "2007 WL 1288012"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holloman Ex Rel. Holloman v. Harland",
          "cluster_id": 76571,
          "cite": [
            "370 F.3d 1252",
            "2004 WL 1178465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkie v. Robbins",
          "cluster_id": 145705,
          "cite": [
            "168 L. Ed. 2d 389",
            "127 S. Ct. 2588",
            "551 U.S. 537",
            "2007 U.S. LEXIS 8513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hope v. Pelzer:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(121169 OR 9434318 OR 9434319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjM5NTI2NDAwMDAwJnM9NTMwNjc5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28121169+OR+9434318+OR+9434319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(121169 OR 9434318 OR 9434319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTQmcz0xNjcwODgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28121169+OR+9434318+OR+9434319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(121169 OR 9434318 OR 9434319)",
        "reviewed": 163,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 163,
        "triage_read": 1,
        "triage_snippet_classified": 162
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(121169 OR 9434318 OR 9434319)",
    "indexed_citing_opinions": 1902,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 121169,
        "count": 1518,
        "count_source": "search"
      },
      {
        "opinion_id": 9434318,
        "count": 397,
        "count_source": "search"
      },
      {
        "opinion_id": 9434319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4984,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hope-v-pelzer.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzOTA5OTYmcz0xMDYwMTg0NCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28121169+OR+9434318+OR+9434319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 121169,
        "cited_id": 70757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 72332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 105659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 110518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 112693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 321166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 396175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 484321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 673540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 682819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 711049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 772146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 1087956,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 2314799,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 121169,
        "cited_id": 2503952,
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
    "date_created": "2026-07-05T07:19:38Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T07:26:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T07:20:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hope v. Pelzer

```
<opinion type="majority">
<author id="b783-8">Justice Stevens</author>
<p id="ARXe">delivered the opinion of the Court.</p>
<p id="b783-9">The Court of Appeals for the Eleventh Circuit concluded that petitioner Larry Hope, a former prison inmate at the Limestone Prison in Alabama, was subjected to cruel and unusual punishment when prison guards twice handcuffed him to a hitching post to sanction him for disruptive conduct. Because that conclusion was not supported by earlier cases with “materially similar” facts, the court held that the respondents were entitled to qualified immunity, and therefore affirmed summary judgment in their favor. We granted cer-tiorari to determine whether the Court of Appeals’ qualified immunity holding comports with our decision in <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">520 U. S. 259</a></span> (1997).</p>
<p id="b783-10">I</p>
<p id="b783-3">In 1995, Alabama was the only State that followed the practice of chaining inmates to one another in work squads. It was also the only State that handcuffed prisoners to “hitching posts” if they either refused to work or otherwise disrupted work squads.<footnotemark>1</footnotemark> Hope was handcuffed to a hitching <page-number citation-index="1" label="734">*734</page-number>post on two occasions. On May 11, 1995, while Hope was working in a chain gang near an interstate highway, he got into an argument with another inmate. Both men were taken back to the Limestone prison and handcuffed to a hitching post. Hope was released two hours later, after the guard captain determined that the altercation had been caused by the other inmate. During his two hours on the post, Hope was offered drinking water and a bathroom break every 15 minutes, and his responses to these offers were recorded on an activity log. Because he was only slightly taller than the hitching post, his arms were above shoulder height and grew tired from being handcuffed so high. Whenever he tried moving his arms to improve his circulation, the handcuffs cut into his wrists, causing pain and discomfort.</p>
<p id="b784-5">On June 7, 1995, Hope was punished more severely. He took a nap during the morning bus ride to the chain gang’s worksite, and when it arrived he was less than prompt in responding to an order to get off the bus. An exchange of vulgar remarks led to a wrestling match with a guard. Four other guards intervened, subdued Hope, handcuffed him, placed him in leg irons and transported him back to the prison where he was put on the hitching post. The guards made him take off his shirt, and he remained shirtless all <page-number citation-index="1" label="735">*735</page-number>day while the sun burned his skin.<footnotemark>2</footnotemark> He remained attached to the post for approximately seven hours. During this 7-hour period, he was given water only once or twice and was given no bathroom breaks.<footnotemark>3</footnotemark> At one point, a guard taunted Hope about his thirst. According to Hope’s affidavit: “[The guard] first gave water to some dogs, then brought the water cooler closer to me, removed its lid, and kicked the cooler over, spilling the water onto the ground.” App. 11.</p>
<p id="b785-5">Hope filed suit under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>, in the United States District Court for the Northern District of Alabama against three guards involved in the May incident, one of whom also handcuffed him to the hitching post in June. The case was referred to a Magistrate Judge who treated the responsive affidavits filed by the defendants as a motion for summary judgment. Without deciding whether “the very act of placing him on a restraining bar for a period of hours as a form of punishment” had violated the Eighth Amendment, the Magistrate concluded that the guards were entitled to qualified immunity.<footnotemark>4</footnotemark> Supplemental App. to Pet. for Cert. 21. The District Court agreed, and entered judgment for respondents.</p>
<p id="b785-6">The United States Court of Appeals for the Eleventh Circuit affirmed. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d 975</a></span> (2001). Before reaching the <page-number citation-index="1" label="736">*736</page-number>qualified immunity issue, however, it answered the constitutional question that the District Court had bypassed. The court found that the use of the hitching post for punitive purposes violated the Eighth Amendment. Nevertheless, applying Circuit precedent concerning qualified immunity, the court stated that “‘the federal law by which the government official’s conduct should be evaluated must be preexisting, obvious and mandatory,’” and established, not by “ ‘abstractions,’ ” but by cases that are “ ‘materially similar’ ” to the facts in the case in front of us.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran"><em>Id., </em>at 981</a></span>. The court then concluded that the facts in the two precedents on which Hope primarily <em>relied </em>— Ort v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d 318</a></span> (CA11 1987), and <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span> (CA5 1974) — “[tjhough analogous,” were not “ ‘materially similar’ to Hope’s situation.’ ” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. We granted certio-rari to review the Eleventh Circuit’s qualified immunity holding. <span class="citation multiple-matches"><a href="/c/U.%20S./534/1073/">534 U. S. 1073</a></span> (2002).</p>
<p id="b786-7">II</p>
<p id="b786-3">The threshold inquiry a court must undertake m a qualified immunity analysis is whether plaintiff’s allegations, if true, establish a constitutional violation. <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001). The Court of Appeals held that “the policy and practice of cuffing an inmate to a hitching post or similar stationary object for a period of time that surpasses that necessary to quell a threat or restore order is a violation of the Eighth Amendment.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 980-981</a></span>. The court rejected respondents’ submission that Hope could have ended his shackling by offering to return to work, finding instead that the purpose of the practice was punitive,<footnotemark>5</footnotemark> and that the circumstances of his confinement created <page-number citation-index="1" label="737">*737</page-number>a substantial risk of harm of which the officers were aware. Moreover, the court relied on Circuit precedent condemning similar practices<footnotemark>6</footnotemark> and the results of a United States Department of Justice (DOJ) report that found Alabama’s systematic use of the hitching post to be improper corporal punishment.<footnotemark>7</footnotemark> We agree with the Court of Appeals that the attachment of Hope to the hitching post under the circumstances alleged in this case violated the Eighth Amendment.</p>
<p id="b787-5">“ ‘[T]he unnecessary and wanton infliction of pain ... constitutes cruel and unusual punishment forbidden by the Eighth Amendment.’ ” <em>Whitley </em>v. <em>Albers, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312, 319</a></span> (1986) (some internal quotation marks omitted). We have said that “[a]mong ‘unnecessary and wanton’ inflictions of pain are those that are ‘totally without penological justification.’” <em>Rhodes </em>v. <em>Chapman, </em><span class="citation" data-id="9428405"><a href="/opinion/110518/rhodes-v-chapman/#346" aria-description="Citation for case: Rhodes v. Chapman">452 U. S. 337, 346</a></span> (1981). In making this determination in the context of prison condi<page-number citation-index="1" label="738">*738</page-number>tions, we must ascertain whether the officials involved acted with “deliberate indifference” to the inmates’ health or safety. <em>Hudson </em>v. <em>McMillian, </em><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/#8" aria-description="Citation for case: Hudson v. McMillian">503 U. S. 1, 8</a></span> (1992). We may infer the existence of this subjective state of mind from the fact that the risk of harm is obvious. <em>Farmer </em>v. <em>Brennan, </em><span class="citation" data-id="9527063"><a href="/opinion/1087956/farmer-v-brennan/#842" aria-description="Citation for case: Farmer v. Brennan">511 U. S. 825, 842</a></span> (1994).</p>
<p id="b788-5">As the facts are alleged by Hope, the Eighth Amendment violation is obvious. Any safety concerns had long since abated by the time petitioner was handcuffed to the hitching post because Hope had already been subdued, handcuffed, placed in leg irons, and transported back to the prison. He was separated from his work squad and not given the opportunity to return to work. Despite the clear lack of an emergency situation, the respondents knowingly subjected him to a substantial risk of physical harm, to unnecessary pain caused by the handcuffs and the restricted position of confinement for a 7-hour period, to unnecessary exposure to the heat of the sun, to prolonged thirst and taunting, and to a deprivation of bathroom breaks that created a risk of particular discomfort and humiliation.<footnotemark>8</footnotemark> The use of the hitching post under these circumstances violated the “basic concept underlying the Eighth Amendment[, which] is nothing less than-the dignity of man.” <em>Trop </em>v. <em>Dulles, </em><span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/#100" aria-description="Citation for case: Trop v. Dulles">356 U. S. 86, 100</a></span> (1958). This punitive treatment amounts to gratuitous infliction of “wanton and unnecessary” pain that our precedent clearly prohibits.</p>
<p id="b789-8"><page-number citation-index="1" label="739">*739</page-number>H-l HH I — I</p>
<p id="b789-3">Despite their participation m this constitutionally impermissible conduct, respondents may nevertheless be shielded from liability for civil damages if their actions did not violate “clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). In assessing whether the Eighth Amendment violation here met the <em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Harlow</a></span> </em>test, the Court of Appeals required that the facts of previous cases be “‘materially similar’ to Hope’s situation.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. This rigid gloss on the qualified immunity standard, though supported by Circuit precedent,<footnotemark>9</footnotemark> is not consistent with our cases.</p>
<p id="b789-4">As we have explained, qualified immunity operates “to ensure that before they are subjected to suit, officers are on notice their conduct is unlawful.” <em>Saucier </em>v. <em>Katz, </em>533 U. S., at 206. For a constitutional right to be clearly established, its contours “must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, see <em>Mitchell </em>[v. <em>Forsyth, </em><span class="citation" data-id="9430106"><a href="/opinion/111481/mitchell-v-forsyth/" aria-description="Citation for case: Mitchell v. Forsyth">472 U. S. 511</a></span>,] 535, n. 12; but it is to say that in the light of pre-existing law the unlawfulness must be apparent.” <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 640</a></span> (1987).</p>
<p id="b789-5">Officers sued in a civil action for damages under <span class="citation no-link">42 U. S. C. § 1983</span> have the same right to fair notice as do defendants charged with the criminal offense defined in <span class="citation no-link">18 U. S. C. §242</span>. Section 242 makes it a crime for a state official to act “willfully” and under color of law to deprive a person of rights protected by the Constitution. In <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">520 U. S. 259</a></span> (1997), we held that the defendant was entitled <page-number citation-index="1" label="740">*740</page-number>to “fair warning” that his conduct deprived his victim of a constitutional right, and that the standard for determining the adequacy of that warning was the same as the standard for determining whether a constitutional right was “clearly established” in civil litigation under § 1983.<footnotemark>10</footnotemark></p>
<p id="b790-5">In <em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/" aria-description="Citation for case: United States v. Lanier">Lanier</a></span>, </em>the Court of Appeals had held that the indictment did not charge an offense under § 242 because the constitutional right allegedly violated had not been identified in any earlier case involving a factual situation “ ‘fundamentally similar’” to the one in issue. <em>Id., </em>at 263 (citing <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="9488829"><a href="/opinion/711049/united-states-v-david-w-lanier/#1393" aria-description="Citation for case: United States v. David W. Lanier">73 F. 3d 1380, 1393</a></span> (CA6 1996)). The Court of Appeals had assumed that the defendant in a criminal case was entitled to a degree of notice “ ‘substantially higher than the “clearly established” standard used to judge qualified immunity’ ” in civil cases under § 1983. <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#263" aria-description="Citation for case: United States v. Lanier">520 U. S., at 263</a></span>. We reversed, explaining that the “fair warning” requirement is identical under §242 and the qualified immunity standard. We pointed out that we had “upheld convictions under § 241 or §242 despite notable factual distinctions between the precedents relied on and the cases then before the Court, so long as the prior decisions gave reasonable warning that the conduct then at issue violated constitutional rights.” <em>Id., </em>at 269. We explained:</p>
<blockquote id="b790-6">“This is not to say, of course, that the single warning standard points to a single level of specificity sufficient in every instance. In some circumstances, as when an <page-number citation-index="1" label="741">*741</page-number>earlier case expressly leaves open whether a general rule applies to the particular type of conduct at issue, a very high degree of prior factual particularity may be necessary. But general statements of the law are not inherently incapable of giving fair and clear warning, and in other instances a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question, even though ‘the very action in question has [not] previously been held unlawful/ <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 640</a></span>.” <em>Id., </em>at 270-271 (citation omitted).</blockquote>
<p id="b791-5">Our opinion in <em>Lanier </em>thus makes clear that officials can still be on notice that their conduct violates established law even in novel factual circumstances. Indeed, in <em>Lanier, </em>we expressly rejected a requirement that previous cases be “fundamentally similar.” Although earlier cases involving “fundamentally similar” facts can provide especially strong support for a conclusion that the law is clearly established, they are not necessary to such a finding. The same is true of cases with “materially similar” facts. Accordingly, pursuant to <em>Lanier, </em>the salient question that the Court of Appeals ought to have asked is whether the state of the law in 1995 gave respondents fair warning that their alleged treatment of Hope was unconstitutional. It is to this question that we now turn.</p>
<p id="b791-6">IV</p>
<p id="b791-7">The use of the hitching post as alleged by Hope “unnecessarily] and wanton[ly] inflicted pain,” <em>Whitley, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span> (internal quotation marks omitted), and thus was a clear violation of the Eighth Amendment. See Part II, <em>supra. </em>Arguably, the violation was so obvious that our own Eighth Amendment cases gave respondents fair warning that their conduct violated the Constitution. Regardless, in light of binding Eleventh Circuit precedent, an Alabama Department of Corrections (ADOC) regulation, and a DOJ report <page-number citation-index="1" label="742">*742</page-number>informing the ADOC of the constitutional infirmity in its use of the hitching post, we readily conclude that the respondents’ conduct violated “clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>.</p>
<p id="b792-5">Cases decided by the Court of Appeals for the Fifth Circuit before 1981 are binding precedent in the Eleventh Circuit today. See <em>Bonner </em>v. <em>Prichard, </em><span class="citation" data-id="396175"><a href="/opinion/396175/larry-bonner-v-city-of-prichard-alabama/" aria-description="Citation for case: Larry Bonner v. City of Prichard, Alabama">661 F. 2d 1206</a></span> (CA11 1981). In one of those cases, decided in 1974, the Court of Appeals reviewed a District Court decision finding a number of constitutional violations in the administration of Mississippi’s prisons. <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span>. That opinion squarely held that several of those “forms of corporal punishment run afoul of the Eighth Amendment [and] offend contemporary concepts of decency, human dignity, and precepts of civilization which we profess to possess.” <em>Id., </em>at 1806. Among those forms of punishment were “handcuffing inmates to the fence and to cells for long periods of time, . . . and forcing inmates to stand, sit or lie on crates, stumps, or otherwise maintain awkward positions for prolonged periods.” <em>Ibid. </em>The fact that <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>found several forms of punishment impermissible does not, as respondents suggest, lessen the force of its holding with respect to handcuffing inmates to cells or fences for long periods of time. Nor, for the purpose of providing fair notice to reasonable officers administering punishment for past misconduct, is there any reason to draw a constitutional distinction between a practice of handcuffing an inmate to a fence for prolonged periods and handcuffing him to a hitching post for seven hours. The Court of Appeals’ conclusion to the contrary exposes the danger of a rigid, overreliance on factual similarity. As the Government submits in its brief <em>amicus curiae: </em>“No reasonable officer could have concluded that the constitutional holding of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>turned on the fact that inmates were handcuffed to fences or the bars of cells, rather than a specially designed metal bar designated for shackling. If anything, the use of <page-number citation-index="1" label="743">*743</page-number>a designated hitching post highlights the constitutional problem.” Brief for United States as <em>Amicus Curiae </em>22. In light of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span>, </em>the unlawfulness of the alleged conduct should have been apparent to respondents.</p>
<p id="b793-5">The reasoning, though not the holding, in a case decided by the Eleventh Circuit in 1987 sent the same message to reasonable officers in that Circuit. In <em>Ort </em>v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d 318</a></span>, the Court of Appeals held that an officer’s temporary denials of drinking water to an inmate who repeatedly refused to do his share of the work assigned to a farm squad “should not be viewed as punishment in the strict sense, but instead as necessary coercive measures undertaken to obtain compliance with a reasonable prison rule, <em>i. e., </em>the requirement that all inmates perform their assigned farm squad duties.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#325" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 325</a></span>. “The officer’s clear motive was to encourage Ort to comply with the rules and to do the work required of him, after which he would receive the water like everyone else.” <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ibid.</a></span> </em>The court cautioned, however, that a constitutional violation might have been present “if later, once back at the prison, officials had decided to deny [Ort] water as punishment for his refusal to work.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#326" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 326</a></span>. So too would a violation have occurred if the method of coercion reached a point of severity such that the recalcitrant prisoner’s health was at risk. <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ibid.</a></span> </em>Although the facts of the case are not identical, Ort]s premise is that “physical abuse directed at [a] prisoner <em>after </em>he terminate^] his resistance to authority would constitute an actionable eighth amendment violation.” <span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#324" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony..."><em>Id., </em>at 324</a></span>. This premise has clear applicability in this case. Hope was not restrained at the worksite until he was willing to return to work. Rather, he was removed back to the prison and placed under conditions that threatened his health. <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>therefore gave fair warning to respondents that their conduct crossed the line of what is constitutionally permissible.</p>
<p id="b793-6">Relevant to the question whether <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>provided fair warning to respondents that their conduct violated the Constitu<page-number citation-index="1" label="744">*744</page-number>tion is a regulation promulgated by ADOC in 1993.<footnotemark>11</footnotemark> The regulation authorizes the use of the hitching post when an inmate refuses to work or is otherwise disruptive to a work squad. It provides that an activity log should be completed for each such inmate, detailing his responses to offers of water and bathroom breaks every 15 minutes. Such a log was completed and maintained for petitioner’s shackling in May, but the record contains no such log for the 7-hour shackling in June and the record indicates that the periodic offers contemplated by the regulation were not made. App. 43-48. The regulation also states that an inmate “will be allowed to join his assigned squad” whenever he tells an officer “that he is ready to go to work.” <em>Id., </em>at 103. The findings in <em>Austin </em>v. <em>Hopper, </em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1244" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d 1210, 1244-1246</a></span> (MD Ala. 1998), as well as the record in this case, indicate that this important provision of the regulation was frequently ignored by corrections officers. If regularly observed, a requirement that would effectively give the inmate the keys to the handcuffs that attached him to the hitching post would have made this case more analogous to the practice upheld in <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span>, </em>rather than the kind of punishment <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>described as impermissible. A course of conduct that tends to prove that the requirement was merely a sham, or that respondents could ignore it with impunity, provides equally strong support for the conclusion that they were fully aware of the wrongful character of their conduct.</p>
<p id="b794-5">Respondents violated clearly established law. Our conclusion that “a reasonable person would have known,” <em>Harlow, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S., at 818</a></span>, of the violation is buttressed by the fact that the DOJ specifically advised the ADOC of the unconstitutionality of its practices before the incidents in this case took place. The DOJ had conducted a study in 1994 of Alabama’s use of the hitching post. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#979" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 979</a></span>. <page-number citation-index="1" label="745">*745</page-number>Among other findings, the DOJ report noted that ADOC’s officers consistently failed to comply with the policy of immediately releasing any inmate from the hitching post who agrees to return to work. The DOJ concluded that the systematic use of the restraining bar in Alabama constituted improper corporal punishment. <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Accordingly, the DOJ advised the ADOC to cease use of the hitching post in order to meet constitutional standards. The ADOC replied that it thought the post could permissibly be used “ ‘to preserve prison security and discipline.’ ” <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>In response, the DOJ informed the ADOC that, “‘[although an emergency situation may warrant drastic action by corrections staff, our experts found that the “rail” is being used systematically as an improper punishment for relatively trivial offenses. Therefore, we have concluded that the use of the “rail” is without penological justification.”’ <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Although there is nothing in the record indicating that the DOJ’s views were communicated to respondents, this exchange lends support to the view that reasonable officials in the ADOC should have realized that the use of the hitching post under the circumstances alleged by Hope violated the Eighth Amendment prohibition against cruel and unusual punishment.</p>
<p id="b795-5">The obvious cruelty inherent in this practice should have provided respondents with some notice that their alleged conduct violated Hope’s constitutional protection against cruel and unusual punishment. Hope was treated in a way antithetical to human dignity — he was hitched to a post for an extended period of time in a position that was painful, and under circumstances that were both degrading and dangerous. This wanton treatment was not done of necessity, but as punishment for prior conduct. Even if there might once have been a question regarding the constitutionality of this practice, the Eleventh Circuit precedent of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>and <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span>, </em>as well as the DOJ report condemning the practice, put a reasonable officer on notice that the use of the hitching <page-number citation-index="1" label="746">*746</page-number>post under the circumstances alleged by Hope was unlawful. The “fair and clear warning,” <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#271" aria-description="Citation for case: United States v. Lanier">520 U. S., at 271</a></span>, that these cases provided was sufficient to preclude the defense of qualified immunity at the summary judgment stage.</p>
<p id="b796-5">V</p>
<p id="b796-6">In response to Justice Thomas’ thoughtful dissent, we make the following three observations. The first is that in granting certiorari to review the summary judgment entered in favor of the officers, we did not take any question about the sufficiency of pleadings and affidavits to raise a genuine possibility that the three named officers were responsible for the punitive acts of shackling alleged. All questions raised by petitioner (the plaintiff against whom summary judgment was entered) go to the application of the standard that no immunity is available for official acts when “it would be clear to a reasonable officer that his conduct was unlawful in the situation he confronted.” <em>Saucier </em>v. <em>Katz, </em>533 U. S., at 202. The officers’ brief in opposition to certiorari likewise addressed only the legal standard of what is clearly established. The resulting focus in the case was the Eleventh Circuit’s position, that a violation is not clearly established unless it is the subject of a prior case of liability on facts “ ‘materially similar’ ” to those charged. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#981" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 981</a></span>. We did not take, and do not pass upon, the questions whether or to what extent the three named officers may be held responsible for the acts charged, if proved. Nothing in our decision forecloses any defense other than qualified immunity on the ground relied upon by the Court of Appeals.</p>
<p id="b796-7">Second, we may address the immunity question on the assumption that the act of field discipline charged on each occasion was handcuffing Hope to a hitching post for an extended period apparently to inflict gratuitous pain or discomfort, with no justification in threatened harm or a continuing refusal to work. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran"><em>Id., </em>at 980</a></span> (on neither occasion did Hope “refus[e] to work or encourag[e] other inmates to refuse to <page-number citation-index="1" label="747">*747</page-number>work”). The Court of Appeals clearly held the act of cuffing petitioner to the hitching post itself to suffice as an unconstitutional act: “We find that cuffing an inmate to a hitching post for a period of time extending past that required to address an immediate danger or threat is a violation of the Eighth Amendment.” <em><span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">Ibid.</a></span> </em>Although the court continued that “[t]his violation is exacerbated by the lack of proper clothing, water, or bathroom breaks,” <em>ibid., </em>this embellishment was not the basis of its decision, and our own decision adequately rests on the same assumption that sufficed for the Court of Appeals.</p>
<p id="b797-5">Third, in applying the objective immunity test of what a reasonable officer would understand, the significance of federal judicial precedent is a function in part of the Judiciary’s structure. The unreported District Court opinions cited by the officers are distinguishable on their own terms.<footnotemark>12</footnotemark> But regardless, they would be no match for the Circuit precedents<footnotemark>13</footnotemark> in <em>Gates </em>v. <em>Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/#1306" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d, at 1306</a></span>, which held that “handcuffing inmates to the fence and to cells for long periods of time” was unconstitutional, and <em>Ort </em>v. <em>White, </em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/#326" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">813 F. 2d, at 326</a></span>, which suggested that it would be unconstitutional to inflict gratuitous pain on an inmate (by refusing him water) when punishment was unnecessary to enforce <page-number citation-index="1" label="748">*748</page-number>on-the-spot discipline. The vitality of <em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">Gates</a></span> </em>and <em><span class="citation" data-id="484321"><a href="/opinion/484321/anthony-ort-v-warden-jd-white-ron-sutton-tony-holliday-officer-truman/" aria-description="Citation for case: Anthony Ort v. Warden J.D. White, Ron Sutton, Tony...">Ort</a></span> </em>could not seriously be questioned in light of our own decisions holding that gratuitous infliction of punishment is unconstitutional, even in the prison context, see <em>supra, </em>at 787 (citing <em>Whitley </em>v. <em>Albers, </em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span>; <em>Rhodes </em>v. <em>Chapman, </em><span class="citation" data-id="9428405"><a href="/opinion/110518/rhodes-v-chapman/#346" aria-description="Citation for case: Rhodes v. Chapman">452 U. S., at 346</a></span>).</p>
<p id="b798-5">The judgment of the Court of Appeals is reversed.</p>
<p id="b798-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b783-5"> In its review of the summary judgment, the Court of Appeals viewed the facts in the light most favorable to Hope, the nonmoving party. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#977" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d 975, 977</a></span> (CA11 2001) (case below). We do the same. <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201 (2001). The Court of Appeals also referenced facts established in <em>Austin </em>v. <em>Hopper, </em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d 1210</a></span> (MD Ala. 1998). <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#978" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 978, n. 6</a></span>. This was appropriate because <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>is a class-action suit brought by Alabama prisoners, including Hope, and the District Court opinion in that case discusses Hope’s allegations at some length. <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1247" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1247-1248</a></span>. In their summary judgment papers, both Hope and respondents referenced the findings in <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span>, </em>and thus those <page-number citation-index="1" label="734">*734</page-number>findings are part of the record in this case. See, <em>e. g., </em>Plaintiff’s Preliminary Response to Defendants’ Special Report, Record 30; Defendants’ Response to Court Order, App. 61. Accordingly, for purposes of our review of the grant of summary judgment, the <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>findings may also be assumed true, and we reference them when appropriate.</p>
<p id="AtqJ">As <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Austin</a></span> </em>explained, the hitching post is a horizontal bar “‘made of sturdy, nonflexible material,”’ placed between 45 and 57 inches from the ground. Inmates are handcuffed to the hitching post in a standing position and remain standing the entire time they are placed on the post. Most inmates are shackled to the hitching post with their two hands relatively close together and at face level. <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1241" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1241-1242</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b785-7"> “The most repeated complaint of the hitching post, however, was the strain it produced on inmates’ muscles by forcing them to remain in a standing position with their arms raised in a stationary position for a long period of time. In addition to their exposure to sunburn, dehydration, and muscle aches, the inmates are also placed in substantial pain when the sun heats the handcuffs that shackle them to the hitching post, or heats the hitching post itself. Several of the inmates described the way in which the handcuffs burned and chafed their skin during their placement on the post.” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1248" aria-description="Citation for case: Austin v. Hopper"><em>Id., </em>at 1248</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b785-8"> The Court of Appeals noted that respondents had not produced any activity log for this incident, despite the policy that required that such a log be maintained. <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#977" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 977, n. 1</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b785-9"> Supplemental App. to Pet. for Cert. 21-27.</p>
</footnote>
<footnote label="5">
<p id="b786-4"> In reaching this conclusion, the Court of Appeals stated: “While the DOC claims that Hope would have been released from the hitching post had he asked to return to work, the evidence suggests this is not the case. First, Hope never refused to work. During the May incident, he was the victim in an altercation on the work site, but he never refused to do his <page-number citation-index="1" label="737">*737</page-number>job. During the June incident, Hope was involved in an altercation with prison guards. There is nothing in the record, however, claiming that he refused to work or encouraged other inmates to refuse to work. Therefore, it is not clear that the solution to his hitching post problem was to ask to return to work. Second, Hope was placed in a car and driven back to Limestone to be cuffed to the hitching post on both occasions. Given the facts, it is improbable that had Hope said, T want to go back to work,’ a prison guard would have left his post at Limestone to drive Hope back to the work site. It is more likely that the guards left Hope on the post until his work detail returned to teach the other inmates a lesson.” <span class="citation" data-id="772146"><a href="/opinion/772146/larry-hope-v-mark-pelzer-gene-mcclaran/#980" aria-description="Citation for case: Larry Hope v. Mark Pelzer, Gene McClaran">240 F. 3d, at 980</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b787-11"> “Since abolishing the pillory over a century ago, our system of justice has consistently moved away from forms of punishment similar to hitching posts in prisons. In <em>Gates v. Collier, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d 1291</a></span> (5th Cir. 1974), in regard to ‘handcuffing inmates to the fence and to cells for long periods of time’ and other such punishments, we stated that ‘[w]e have ho difficulty in reaching the conclusion that these forms of corporal punishment run afoul of the Eighth Amendment, offend contemporary concepts of decency, human dignity, and-precepts of civilization which we profess to possess.’ <em>Gates, </em><span class="citation" data-id="321166"><a href="/opinion/321166/nazareth-gates-and-united-states-of-america-plaintiff-intervenor-appellee/#1306" aria-description="Citation for case: Nazareth Gates, and United States of America,...">501 F. 2d at 1306</a></span>.” <em>Id., </em>at 979.</p>
</footnote>
<footnote label="7">
<p id="b787-12"> The DOJ report apparently was not before the District Court in this case, but the Court of Appeals took judicial notice of the report and referenced it throughout the decision below. <em>Id., </em>at 979, n. 8.</p>
</footnote>
<footnote label="8">
<p id="b788-6"> The awareness of the risk of harm attributable to any individual respondent may be evaluated in part by considering the pattern of treatment that inmates generally received when attached to the hitching post. In <em>Austin </em>v. <em><span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/" aria-description="Citation for case: Austin v. Hopper">Hopper</a></span>, </em>the District Court cited examples of humiliating incidents resulting from the denial of bathroom breaks. One inmate “was not permitted to use the restroom or to change his clothing for four and one-half hours after he had defecated on himself.” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1246" aria-description="Citation for case: Austin v. Hopper">15 F. Supp. 2d, at 1246</a></span>. “Moreover, certain corrections officers not only ignored or denied inmates’ requests for water or access to toilet facilities, but taunted them while they were clearly suffering from dehydration ....” <span class="citation" data-id="2314799"><a href="/opinion/2314799/austin-v-hopper/#1247" aria-description="Citation for case: Austin v. Hopper"><em>Id., </em>at 1247</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b789-6"> See, <em>e. g., Suissa </em>v. <em>Fulton County, </em><span class="citation" data-id="70757"><a href="/opinion/70757/suissa-v-fulton-county-ga/" aria-description="Citation for case: Suissa v. Fulton County, GA">74 F. 3d 266</a></span>-270 (CA11 1996); <em>Lassiter </em>v. <em>Alabama A&amp;M Univ. Bd. of Trustees, </em><span class="citation" data-id="673540"><a href="/opinion/673540/albert-e-lassiter-v-alabama-a-m-university-board-of-trustees-douglas/#1150" aria-description="Citation for case: Albert E. Lassiter v. Alabama a &amp; M University, Board of...">28 F. 3d 1146, 1150</a></span> (CA11 1994); <em>Hill </em>v. <em>Dekalb Regional Youth Detention Center, </em><span class="citation" data-id="6932906"><a href="/opinion/7030810/hill-v-dekalb-regional-youth-detention-center/#1185" aria-description="Citation for case: Hill v. Dekalb Regional Youth Detention Center">40 F. 3d 1176, 1185</a></span> (CA11 1994).</p>
</footnote>
<footnote label="10">
<p id="b790-7"> “[T]he object of the ‘clearly established’ immunity standard is not different from that of ‘fair warning’ as it relates to law ‘made specific’ for the purpose of validly applying § 242. The fact that one has a civil and the other a criminal law role is of no significance; both serve the same objective, and in effect the qualified immunity test is simply the adaptation of the fair warning standard to give officials (and, ultimately, governments) the same protection from civil liability and its consequences that individuals have traditionally possessed in the face of vague criminal statutes. To require something clearer than ‘clearly established’ would, then, call for something beyond ‘fair warning.’” <span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#270" aria-description="Citation for case: United States v. Lanier">520 U. S., at 270-271</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b794-6"> The regulation was not provided to the District Court, but it was added to the record at the request of the Court of Appeals. See App. 100-106.</p>
</footnote>
<footnote label="12">
<p id="b797-6"> In three of the decisions, the inmates were given the choice between working or being restrained. See <em>Whitson </em>v. <em>Gillikin, </em>No. CV-93-H-1517-NE (ND Ala., Jan. 24, 1994), p. 4, App. 84; <em>Dale </em>v. <em>Murphy, </em>No. CV-85-1091-H-S (SD Ala., Feb. 4, 1986), p. 2; <em>Ashby </em>v. <em>Dees, </em>No. CV-94-U-0605-NE (ND Ala., Dec. 27, 1994), p. 6. In others, the inmates were offered regular water and bathroom breaks. See <em>Lane </em>v. <em>Findley, </em>No. CV-93-C-1741-S (ND Ala., Aug. 4, 1994), p. 9; <em>Williamson </em>v. <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>No. CV-92-H-675-N (MD Ala., Aug. 18, 1993), p. 2; <em>Hollis </em>v. <em>Folsom, </em>No. CV-94-T-0052-N (MD Ala., Nov. 4, 1994), p. 9. Finally, in <em>Vinson </em>v. <em>Thompson, </em>No. CV-94-A-268-N (MD Ala., Dec. 9,1994), the inmate was restrained for approximately 45 minutes. <em>Id., </em>at 2.</p>
</footnote>
<footnote label="13">
<p id="b797-7"> There are apparently no decisions on similar facts from other Circuits, presumably because Alabama is the only State to authorize the use of the hitching post in its prison system.</p>
</footnote>
</opinion>
```

---
