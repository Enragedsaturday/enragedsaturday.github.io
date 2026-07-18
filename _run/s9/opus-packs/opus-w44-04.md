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

## GROUP: content/cases/Illinois v. Wardlow.md  (`case`, 5 assertions)

### content_page

```
---
title: "Illinois v. Wardlow"
type: case
citation: "528 U.S. 119 (2000)"
parallel_cite: "120 S. Ct. 673; 145 L. Ed. 2d 570"
neutral_cite: 2000 U.S. LEXIS 504
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2000
date_decided: 2000-01-19
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2000-01-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Illinois v. Wardlow
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/"
  cluster_id: 118326
  opinion_id: 9433881
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Terry v. Ohio]]", "[[Florida v. J.L.]]", "[[Alabama v. White]]", "[[Brown v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion", "terry-stop", "flight", "high-crime-area"]
holding: "Unprovoked headlong flight upon noticing police, combined with presence in a high-crime area, can furnish reasonable suspicion for a…"
lake:
  record_id: Illinois v. Wardlow
  status: verified
  projected_at: 2026-07-09
---

# Illinois v. Wardlow

*528 U.S. 119 (2000)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers in a four-car caravan converged on a Chicago area known for heavy narcotics trafficking. Officer Nolan saw Wardlow standing next to a building holding an opaque bag; when Wardlow looked at the officers, he fled. Nolan caught him, conducted a protective pat-down, felt a hard object, and found a handgun. Wardlow moved to suppress the gun, arguing the stop lacked reasonable suspicion.

## Issue
Whether unprovoked flight upon noticing the police, in an area of heavy narcotics trafficking, can furnish the reasonable suspicion needed for a *[[Terry v. Ohio|Terry]]* stop.

## Rule
Yes. "Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable suspicion." — 528 U.S. at 124. ^pin-124

"Headlong flight—wherever it occurs—is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such." — [*Id.*](https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/#:~:text=Headlong%20flight%E2%80%94wherever%20it%20occurs%E2%80%94is%20the) ^pin-124a

Location is also a relevant consideration: "An individual's presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. But officers are not required to ignore the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation." — *Id.* ^pin-124b

## Application
Wardlow was present in an area of heavy narcotics trafficking and engaged in unprovoked, headlong flight the moment he noticed the police. Taking those facts together — the high-crime location as context plus the evasive flight — Officer Nolan had reasonable suspicion that Wardlow was involved in criminal activity, justifying the *[[Terry v. Ohio|Terry]]* stop and the protective pat-down that uncovered the handgun.

## Conclusion
The stop was supported by reasonable suspicion; the judgment suppressing the handgun was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Wardlow* applies the reasonable-suspicion standard of [[Terry v. Ohio]], treating unprovoked flight in a high-crime area as supplying reasonable suspicion under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Illinois v. Wardlow*, 528 U.S. 119 (2000) — https://www.courtlistener.com/opinion/118326/illinois-v-wardlow/ — pinpoint: 124.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "82d8b78c134dcc8f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "528 U.S. 119 (2000)", "court": "U.S. Supreme Court", "neutral_cite": "2000 U.S. LEXIS 504", "official_citation_present": true, "parallel_cite": "120 S. Ct. 673; 145 L. Ed. 2d 570", "title": "Illinois v. Wardlow", "year": "2000"}}
{"assertion_id": "0aa548a081d6d726", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "Illinois v. Wardlow"}}
{"assertion_id": "4ecc589dd0b97f87", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Unprovoked headlong flight upon noticing police, combined with presence in a high-crime area, can furnish reasonable suspicion for a…", "title": "Illinois v. Wardlow"}}
{"assertion_id": "83aee763ee4bf2e0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Illinois v. Wardlow"}}
{"assertion_id": "df0c4490879aae4f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2000-01-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Illinois v. Wardlow", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Illinois v. Wardlow", "varies_by_point": "false"}}
```

### lake record — Illinois v. Wardlow

```json
{
  "schema_version": "s2.v1",
  "record_id": "Illinois v. Wardlow",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Illinois v. Wardlow",
    "case_name_short": "Wardlow",
    "case_name_full": "Illinois v. Wardlow",
    "input_case_name": "Illinois v. Wardlow",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2000-01-19",
    "year": 2000,
    "docket": null,
    "cluster_id": 118326,
    "lead_opinion_id": 9433881,
    "sibling_ids": [
      118326,
      9433881,
      9433882
    ],
    "absolute_url": "/opinion/118326/illinois-v-wardlow/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "528 U.S. 119",
      "volume": "528",
      "reporter": "U.S.",
      "page": "119",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 673",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 570",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "570",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. LEXIS 504",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "504",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "528 U.S. 119",
        "volume": "528",
        "reporter": "U.S.",
        "page": "119",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 673",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 570",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "570",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. LEXIS 504",
        "volume": "2000",
        "reporter": "U.S. LEXIS",
        "page": "504",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "528 U.S. 119",
    "official_selection": {
      "court_class": "scotus",
      "selected": "528 U.S. 119",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-124",
      "page": null,
      "quote": "--- # Illinois v. Wardlow *528 U.S. 119 (2000)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers in a four-car caravan converged on a Chicago area known for heavy narcotics trafficking. Officer Nolan saw Wardlow standing next to a building holding an opaque bag; when Wardlow looked at the officers, he fled. Nolan caught him, conducted a protective pat-down, felt a hard object, and found a handgun. Wardlow moved to suppress the gun, arguing the stop lacked reasonable suspicion. ## Issue Whether unprovoked flight upon noticing the police, in an area of heavy narcotics trafficking, can furnish the reasonable suspicion needed for a *Terry* stop. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-124a",
      "page": null,
      "quote": "Headlong flight\u2014wherever it occurs\u2014is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such.",
      "star_marker": "124",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10036,
      "fragment": "#:~:text=Headlong%20flight%E2%80%94wherever%20it%20occurs%E2%80%94is%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-124b",
      "page": null,
      "quote": "An individual's presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. But officers are not required to ignore the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-01-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Illinois v. Wardlow",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Connecticut State University Organization of Administrative Faculty, AFSCME, Council 4, Local 2836, AFL-CIO",
          "cluster_id": 10131753,
          "cite": [
            "349 Conn. 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Martin Eduardo Velasquezreyes",
          "cluster_id": 9481403,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane1_negative"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas Omar Midgette",
          "cluster_id": 796984,
          "cite": [
            "478 F.3d 616",
            "2007 U.S. App. LEXIS 4153",
            "2007 WL 572127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balentine v. State",
          "cluster_id": 1662103,
          "cite": [
            "71 S.W.3d 763",
            "2002 WL 496960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peso Chavez and Gregory Lee, Individually and on Behalf of All Persons Similarly Situated v. The Illinois State Police, Terrance W. Gainer, Individually and in His Official Capacity as Director of the Illinois State Police, Michael Snyders, Individually and in His Official Capacity as Illinois State Police Operation Valkyrie Coordinator, Edward Kresl, Individually and in His Official Capacity as District Commander of the Illinois State Police, and Larry Thomas, Daniel Gillette, Craig Graham, Robert P. Cessna, Robert Lauterbach, and Dale Fraher, Officers of the Illinois State Police, in Their Individual Capacities",
          "cluster_id": 773427,
          "cite": [
            "251 F.3d 612",
            "49 Fed. R. Serv. 3d 1127",
            "2001 U.S. App. LEXIS 10560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. City of New York",
          "cluster_id": 8439619,
          "cite": [
            "478 F.3d 76",
            "2007 U.S. App. LEXIS 2782",
            "2007 WL 415171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mendoza",
          "cluster_id": 2594735,
          "cite": [
            "6 P.3d 150",
            "99 Cal. Rptr. 2d 485",
            "24 Cal. 4th 130",
            "24 Cal. 130",
            "2000 Daily Journal DAR 9423",
            "2000 Cal. Daily Op. Serv. 7144",
            "2000 Cal. LEXIS 6118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. City Of New York",
          "cluster_id": 796947,
          "cite": [
            "478 F.3d 76"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Lee Davis",
          "cluster_id": 1043997,
          "cite": [
            "354 S.W.3d 718",
            "2011 Tenn. LEXIS 962"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Huggins",
          "cluster_id": 2575903,
          "cite": [
            "131 P.3d 995",
            "41 Cal. Rptr. 3d 593",
            "38 Cal. 4th 175",
            "2006 Cal. Daily Op. Serv. 2949",
            "2006 Daily Journal DAR 4247",
            "2006 Cal. LEXIS 4393"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
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
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. German Espinoza Montero-Camargo, United States of America v. Lorenzo Sanchez-Guillen",
          "cluster_id": 768288,
          "cite": [
            "208 F.3d 1122",
            "2000 Daily Journal DAR 3733",
            "2000 Cal. Daily Op. Serv. 2774",
            "2000 U.S. App. LEXIS 6494",
            "2000 WL 364861"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Illinois v. Wardlow:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118326 OR 9433881 OR 9433882) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjI2MzA3MjAwMDAwJnM9NDg5OTkwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118326+OR+9433881+OR+9433882%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118326 OR 9433881 OR 9433882)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjkmcz03NzE2MjQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118326+OR+9433881+OR+9433882%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118326 OR 9433881 OR 9433882)",
        "reviewed": 158,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 158,
        "triage_read": 3,
        "triage_snippet_classified": 155
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118326 OR 9433881 OR 9433882)",
    "indexed_citing_opinions": 2136,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118326,
        "count": 1819,
        "count_source": "search"
      },
      {
        "opinion_id": 9433881,
        "count": 347,
        "count_source": "search"
      },
      {
        "opinion_id": 9433882,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4171,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/illinois-v-wardlow.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0OTg2ODYmcz0xMDY1NjYyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118326+OR+9433881+OR+9433882%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118326,
        "cited_id": 94334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 94447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 111280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1420729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1439197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 1613365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2010084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2115969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2116553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2189647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2207148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118326,
        "cited_id": 2239930,
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
    "date_created": "2026-07-05T08:31:25Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:36:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:31:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Illinois v. Wardlow

```
<opinion type="majority">
<author id="b333-4"><page-number citation-index="1" label="121">*121</page-number>CHIEF Justice Rehnquist</author>
<p id="Apc">delivered the opinion of the Court.</p>
<p id="b333-5">Respondent Wardlow fled upon seeing police officers patrolling an area known for heavy narcotics trafficking. Two of the officers caught up with him, stopped him, and conducted a protective patdown search for weapons. Discovering a .38-caliber handgun, the officers arrested Wardlow. We hold that the officers’ stop did not violate the Fourth Amendment to the United States Constitution.</p>
<p id="b333-6">On September 9, 1995, Officers Nolan and Harvey were working as uniformed officers in the special operations section of the Chicago Police Department. The officers were driving the last car of a four-car caravan converging on an area known for heavy narcotics trafficking in order to investigate drug transactions. The officers were traveling together because they expected to find a crowd of people in the area, including lookouts and customers.</p>
<p id="b333-7">As the caravan passed 4035 West Van Burén, Officer Nolan observed respondent Wardlow standing next to the building <page-number citation-index="1" label="122">*122</page-number>holding an opaque bag. Respondent looked in the direction of the officers and fled. Nolan and Harvey turned their ear southbound, watched him as he ran through the gangway and an alley, and eventually cornered him on the street. Nolan then exited his ear and stopped respondent. He immediately conducted a protective patdown search for weapons because in his experience it was common for there to be weapons in the near vicinity of narcotics transactions. During the frisk, Officer Nolan squeezed the bag respondent was carrying and felt a heavy, hard object similar to the shape of a gun. The officer then opened the bag and discovered a .38-caliber handgun with five live rounds of ammunition. The officers arrested Wardlow.</p>
<p id="b334-5">The Illinois trial court denied respondent’s motion to suppress, finding the gun was recovered during a lawful stop and frisk. App. 14. Following a stipulated bench trial, Wardlow was convicted of unlawful use of a weapon by a felon. The Illinois Appellate Court reversed Wardlow’s conviction, concluding that the gun should have been suppressed because Officer Nolan did not have reasonable suspicion sufficient to justify an investigative stop pursuant to <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). <span class="citation" data-id="2116553"><a href="/opinion/2116553/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">287 Ill. App. 3d 367</a></span>, <span class="citation" data-id="2116553"><a href="/opinion/2116553/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">678 N. E. 2d 65</a></span> (1997).</p>
<p id="b334-6">The Illinois Supreme Court agreed. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d 306</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d 484</a></span> (1998). While rejecting the Appellate Court’s conclusion that Wardlow was not in a high crime area, the Illinois Supreme Court determined that sudden flight in such an area does not create a reasonable suspicion justifying a <em>Terry </em>stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#310" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d, at 310</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#486" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 486</a></span>. Relying on <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), the court explained that although police have the right to approach individuals and ask questions, the individual has no obligation to respond. The person may decline to answer and simply go on his or her way, and the refusal to respond, alone, does not provide a legitimate basis for an investigative stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#311" aria-description="Citation for case: People v. Wardlow">183 Ill. <page-number citation-index="1" label="123">*123</page-number>2d, at 311-312</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#486" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 486-487</a></span>. The court then determined that flight may simply be an exercise of this right to “go on one’s way,” and, thus, could not constitute reasonable suspicion justifying a <em>Terry </em>stop. <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#312" aria-description="Citation for case: People v. Wardlow">183 Ill. 2d, at 312</a></span>, <span class="citation" data-id="2115969"><a href="/opinion/2115969/people-v-wardlow/#487" aria-description="Citation for case: People v. Wardlow">701 N. E. 2d, at 487</a></span>.</p>
<p id="b335-5">The Illinois Supreme Court also rejected the argument that flight combined with the fact that it occurred in a high crime area supported a finding of reasonable suspicion because the “high crime area” factor was not sufficient standing alone to justify a <em>Terry </em>stop. Finding no independently suspicious circumstances to support an investigatory detention, the court held that the stop and subsequent arrest violated the Fourth Amendment. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./526/1097/">526 U. S. 1097</a></span> (1999), and now reverse.<footnotemark>1</footnotemark></p>
<p id="b335-6">This case, involving a brief encounter between a citizen and a police officer on a public street, is governed by the analysis we first applied in <em>Terry. </em>In <em>Terry, </em>we held that an officer may, consistent with the Fourth Amendment, conduct a brief, investigatory stop when the officer has a reasonable, articulable suspicion that criminal activity is afoot. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 30</a></span>. While “reasonable suspicion” is a less demanding standard than probable cause and requires a showing considerably less than preponderance of the evidence, the Fourth Amendment requires at least a minimal level of objective justification for making the stop. <em>United States </em>v. <em>Sokolow, </em><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989). The officer must be able <page-number citation-index="1" label="124">*124</page-number>to articulate more than an “inchoate and unparticularized suspicion or ‘hunch’” of criminal activity. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 27</a></span>.<footnotemark>2</footnotemark></p>
<p id="b336-5">Nolan and Harvey were among eight officers in a four-car caravan that was converging on an area known for heavy narcotics trafficking, and the officers anticipated encountering a large number of people in the area, including drug customers and individuals serving as lookouts. App. 8. It was in this context that Officer Nolan decided to investigate Wardlow after observing him flee. An individual’s presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. <em>Brown </em>v. <em>Texas, </em><span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/" aria-description="Citation for case: Brown v. Texas">443 U. S. 47</a></span> (1979). But officers are not required to <em>ignore </em>the relevant characteristics of a location in determining whether the circumstances are sufficiently suspicious to warrant further investigation. Accordingly, we have previously noted the fact that the stop occurred in a “high crime area” among the relevant contextual considerations in a <em>Terry </em>analysis. <em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#144" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 144, 147-148</a></span> (1972).</p>
<p id="b336-6">In this case, moreover, it was not merely respondent’s presence in an area of heavy narcotics trafficking that aroused the officers’ suspicion, but his unprovoked flight upon noticing the police. Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable suspicion. <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#885" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 885</a></span> (1975); <em>Florida </em>v. <em>Rodriguez, </em><span class="citation" data-id="9429786"><a href="/opinion/111280/florida-v-rodriguez/#6" aria-description="Citation for case: Florida v. Rodriguez">469 U. S. 1, 6</a></span> (1984) <em>(per curiam); United States </em>v. <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#8" aria-description="Citation for case: United States v. Sokolow"><em>Sokolow, supra, </em>at 8-9</a></span>. Headlong flight—wherever it occurs—is the consummate act of evasion: It is not necessarily indicative of wrongdoing, but it is certainly suggestive of such. In reviewing the propriety of an officer’s conduct, courts do not have available empirical studies dealing with inferences drawn from suspicious <page-number citation-index="1" label="125">*125</page-number>behavior, and we cannot reasonably demand scientific certainty from judges or law enforcement officers where none exists. Thus, the determination of reasonable suspicion must be based on eommonsense judgments and inferences about human behavior. See <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981). We conclude Officer Nolan was justified in suspecting that Wardlow was involved in criminal activity, and, therefore, in investigating further.</p>
<p id="b337-5">Such a holding is entirely consistent with our decision in <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U. S. 491</a></span> (1983), where we held that when an officer, without reasonable suspicion or probable cause, approaches an individual, the individual has a right to ignore the police and go about his business. <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#498" aria-description="Citation for case: Florida v. Royer"><em>Id., </em>at 498</a></span>. And any “refusal to cooperate, without more, does not furnish the minimal level of objective justification needed for a detention or seizure.” <em>Florida </em>v. <em>Bostick, </em><span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 437</a></span> (1991). But unprovoked flight is simply not a mere refusal to cooperate. Flight, by its very nature, is not “going about one’s business”; in fact, it is just the opposite. Allowing officers confronted with such flight to stop the fugitive and investigate further is quite consistent with the individual’s right to go about his business or to stay put and remain silent in the face of police questioning.</p>
<p id="b337-6">Respondent and <em>amici </em>also argue that there are innocent reasons for flight from police and that, therefore, flight is not necessarily indicative of ongoing criminal activity. This fact is undoubtedly true, but does not establish a violation of the Fourth Amendment. Even in <em>Terry, </em>the conduct justifying the stop was ambiguous and susceptible of an innocent explanation. The officer observed two individuals pacing back and forth in front of a store, peering into the window and periodically conferring. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#5" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 5-6</a></span>. All of this conduct was by itself lawful, but it also suggested that the individuals were casing the store for a planned robbery. <em>Terry </em>recognized that the officers could detain the individuals to resolve the ambiguity. <em>Id., </em>at 30.</p>
<p id="b338-4"><page-number citation-index="1" label="126">*126</page-number>In allowing such detentions, <em>Terry </em>accepts the risk that officers may stop innocent people. Indeed, the Fourth Amendment accepts that risk in connection with more drastic police action; persons arrested and detained on probable cause to believe they have committed a crime may turn out to be innocent. The <em>Terry </em>stop is a far more minimal intrusion, simply allowing the officer to briefly investigate further. If the officer does not learn facts rising to the level of probable cause, the individual must be allowed to go on his way. But in this case the officers found respondent in possession of a handgun, and arrested him for violation of an Illinois firearms statute. No question of the propriety of the arrest itself is before us.</p>
<p id="b338-5">The judgment of the Supreme Court of Illinois is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b338-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b335-7">The state courts have differed on whether unprovoked flight is sufficient grounds to constitute reasonable suspicion. See, <em>e. g., State </em>v. <em>Anderson, </em><span class="citation" data-id="9736767"><a href="/opinion/2207148/state-v-anderson/" aria-description="Citation for case: State v. Anderson">155 Wis. 2d 77</a></span>, <span class="citation" data-id="9736767"><a href="/opinion/2207148/state-v-anderson/" aria-description="Citation for case: State v. Anderson">454 N. W. 2d 763</a></span> (1990) (flight alone is sufficient); <em>Platt </em>v. <em>State, </em><span class="citation" data-id="9743977"><a href="/opinion/2239930/platt-v-state/" aria-description="Citation for case: Platt v. State">589 N. E. 2d 222</a></span> (Ind. 1992) (same); <em>Harris </em>v. <em>State, </em><span class="citation" data-id="1420729"><a href="/opinion/1420729/harris-v-state/" aria-description="Citation for case: Harris v. State">205 Ga. App. 813</a></span>, <span class="citation" data-id="1420729"><a href="/opinion/1420729/harris-v-state/" aria-description="Citation for case: Harris v. State">423 S. E. 2d 723</a></span> (1992) (flight in high crime area sufficient); <em>State </em>v. <em>Hicks, </em><span class="citation" data-id="1613365"><a href="/opinion/1613365/state-v-hicks/" aria-description="Citation for case: State v. Hicks">241 Neb. 357</a></span>, <span class="citation" data-id="1613365"><a href="/opinion/1613365/state-v-hicks/" aria-description="Citation for case: State v. Hicks">488 N. W. 2d 359</a></span> (1992) (flight is not enough); <em>State </em>v. <em>Tucker, </em>136 N. J. 158, <span class="citation" data-id="2010084"><a href="/opinion/2010084/state-v-tucker/" aria-description="Citation for case: State v. Tucker">642 A. 2d 401</a></span> (1994) (same); <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">424 Mich. 42</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d 451</a></span> (1985) (same); <em>People </em>v. <em>Wilson, </em><span class="citation" data-id="1439197"><a href="/opinion/1439197/people-v-wilson/" aria-description="Citation for case: People v. Wilson">784 P. 2d 325</a></span> (Colo. 1989) (same).</p>
</footnote>
<footnote label="2">
<p id="b336-7"> We granted certiorari solely on the question whether the initial stop was supported by reasonable suspicion. Therefore, we express no opinion as to the lawfulness of the frisk independently of the stop.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Immigration & Naturalization Service v. Lopez-Mendoza.md  (`case`, 5 assertions)

### content_page

```
---
title: "Immigration & Naturalization Service v. Lopez-Mendoza"
type: case
citation: "468 U.S. 1032 (1984)"
parallel_cite: "104 S. Ct. 3479; 82 L. Ed. 2d 778; 52 U.S.L.W. 5190"
neutral_cite: 1984 U.S. LEXIS 156
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Immigration & Naturalization Service v. Lopez-Mendoza"
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/"
  cluster_id: 111265
  opinion_id: 9429772
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Janis]]", "[[United States v. Calandra]]", "[[Mapp v. Ohio]]"]
aliases: ["INS v. Lopez-Mendoza"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "deportation", "civil-proceedings"]
holding: "The exclusionary rule generally does NOT apply in civil deportation/removal proceedings: an admission of unlawful presence made after an…"
lake:
  record_id: "Immigration & Naturalization Service v. Lopez-Mendoza"
  status: verified
  projected_at: 2026-07-06
---

# Immigration & Naturalization Service v. Lopez-Mendoza

*468 U.S. 1032 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two respondents, Lopez-Mendoza and Sandoval-Sanchez, were arrested by INS agents and placed in civil deportation proceedings. Lopez-Mendoza objected only to the immigration judge's jurisdiction over his person, claiming his arrest was unlawful. Sandoval-Sanchez sought to suppress his admission of unlawful presence as the fruit of an assertedly unlawful arrest.

## Issue
Whether the Fourth Amendment exclusionary rule applies in a civil deportation proceeding so as to require suppression of the respondent's identity or of an admission obtained after an allegedly unlawful arrest.

## Rule
The exclusionary rule generally does not apply in civil deportation hearings. As to identity: "The 'body' or identity of a defendant or respondent in a criminal or civil proceeding is never itself suppressible as a fruit of an unlawful arrest, even if it is conceded that an unlawful arrest, search, or interrogation occurred." — 468 U.S. at 1039. ^pin-1039

As to evidence generally, applying a cost-benefit balance: "In these circumstances we are persuaded that the Janis balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS." — *Id.* at 1050. ^pin-1050

## Application
Lopez-Mendoza's challenge failed because his identity (his "body") is never suppressible, so the manner of his arrest did not bar the proceeding against him. As to Sandoval-Sanchez, the Court weighed the limited deterrent value of exclusion against its high social costs — including releasing persons whose continuing unlawful presence is itself an ongoing violation — and concluded the balance ran against applying the exclusionary rule, so his admission of unlawful presence was not suppressed.

## Conclusion
The exclusionary rule does not generally apply in INS civil deportation proceedings; the orders of deportation were upheld.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Lopez-Mendoza* applies the cost-benefit framework of [[United States v. Janis]] to civil deportation, confirming that the exclusionary rule of [[Mapp v. Ohio]] does not generally reach such proceedings.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *INS v. Lopez-Mendoza*, 468 U.S. 1032 (1984) — https://www.courtlistener.com/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/ — pinpoints: 1039, 1050.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a15802202c4860a2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "468 U.S. 1032 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 156", "official_citation_present": true, "parallel_cite": "104 S. Ct. 3479; 82 L. Ed. 2d 778; 52 U.S.L.W. 5190", "title": "Immigration & Naturalization Service v. Lopez-Mendoza", "year": "1984"}}
{"assertion_id": "2a30160bcbb4be64", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny / Refinement", "title": "Immigration & Naturalization Service v. Lopez-Mendoza"}}
{"assertion_id": "810e7f289bcb3949", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The exclusionary rule generally does NOT apply in civil deportation/removal proceedings: an admission of unlawful presence made after an…", "title": "Immigration & Naturalization Service v. Lopez-Mendoza"}}
{"assertion_id": "bbf6332e6a203c07", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Immigration & Naturalization Service v. Lopez-Mendoza"}}
{"assertion_id": "d3832ec8cd8a6bee", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Immigration & Naturalization Service v. Lopez-Mendoza", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Immigration & Naturalization Service v. Lopez-Mendoza", "varies_by_point": "false"}}
```

### lake record — Immigration & Naturalization Service v. Lopez-Mendoza

```json
{
  "schema_version": "s2.v1",
  "record_id": "Immigration & Naturalization Service v. Lopez-Mendoza",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "case_name_short": "Lopez-Mendoza",
    "case_name_full": "IMMIGRATION AND NATURALIZATION SERVICE v. LOPEZ-MENDOZA Et Al.",
    "input_case_name": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-05",
    "year": 1984,
    "docket": null,
    "cluster_id": 111265,
    "lead_opinion_id": 9429772,
    "sibling_ids": [
      111265,
      9429772,
      9429773,
      9429774,
      9429775,
      9429776
    ],
    "absolute_url": "/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9287486,
        "score": 20,
        "case_name": "Immigration & Naturalization Service v. Lopez-Mendoza"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 1032",
      "volume": "468",
      "reporter": "U.S.",
      "page": "1032",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3479",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 778",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5190",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 156",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "156",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 1032",
        "volume": "468",
        "reporter": "U.S.",
        "page": "1032",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3479",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 778",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 156",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "156",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5190",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 1032",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 1032",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1039",
      "page": null,
      "quote": "--- # Immigration & Naturalization Service v. Lopez-Mendoza *468 U.S. 1032 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Two respondents, Lopez-Mendoza and Sandoval-Sanchez, were arrested by INS agents and placed in civil deportation proceedings. Lopez-Mendoza objected only to the immigration judge's jurisdiction over his person, claiming his arrest was unlawful. Sandoval-Sanchez sought to suppress his admission of unlawful presence as the fruit of an assertedly unlawful arrest. ## Issue Whether the Fourth Amendment exclusionary rule applies in a civil deportation proceeding so as to require suppression of the respondent's identity or of an admission obtained after an allegedly unlawful arrest. ## Rule The exclusionary rule generally does not apply in civil deportation hearings. As to identity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1050",
      "page": null,
      "quote": "In these circumstances we are persuaded that the Janis balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Immigration & Naturalization Service v. Lopez-Mendoza",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gonzaga-Ortega v. Holder",
          "cluster_id": 808514,
          "cite": [
            "694 F.3d 1069",
            "2012 WL 4040247",
            "2012 U.S. App. LEXIS 19329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Conteh v. Gonzales",
          "cluster_id": 202370,
          "cite": [
            "461 F.3d 45",
            "2006 U.S. App. LEXIS 21422",
            "2006 WL 2406942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. St. Cyr",
          "cluster_id": 118452,
          "cite": [
            "150 L. Ed. 2d 347",
            "121 S. Ct. 2271",
            "533 U.S. 289",
            "2001 U.S. LEXIS 4670",
            "2001 Cal. Daily Op. Serv. 5235",
            "2001 Daily Journal DAR 6475",
            "2001 Colo. J. C.A.R. 3473",
            "69 U.S.L.W. 4510",
            "14 Fla. L. Weekly Fed. S 401"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reno v. Flores",
          "cluster_id": 112833,
          "cite": [
            "123 L. Ed. 2d 1",
            "113 S. Ct. 1439",
            "507 U.S. 292",
            "1993 U.S. LEXIS 2399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. United States",
          "cluster_id": 803270,
          "cite": [
            "183 L. Ed. 2d 351",
            "132 S. Ct. 2492",
            "567 U.S. 387",
            "2012 U.S. LEXIS 4872",
            "80 U.S.L.W. 4539",
            "23 Fla. L. Weekly Fed. S 437",
            "2012 WL 2368661",
            "95 Empl. Prac. Dec. (CCH) 44,539",
            "115 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. United States",
          "cluster_id": 118278,
          "cite": [
            "143 L. Ed. 2d 424",
            "119 S. Ct. 1307",
            "526 U.S. 314",
            "1999 U.S. LEXIS 2348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Peque",
          "cluster_id": 5642633,
          "cite": [
            "22 N.Y.3d 168",
            "3 N.E.3d 617"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Svitlana Denko v. Immigration and Naturalization Service",
          "cluster_id": 784396,
          "cite": [
            "351 F.3d 717",
            "2003 U.S. App. LEXIS 24605",
            "2003 WL 22879815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mayfield v. United States",
          "cluster_id": 594,
          "cite": [
            "599 F.3d 964",
            "2010 U.S. App. LEXIS 6015",
            "2010 WL 1052341"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
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
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emmanuel Senyo Agyeman v. Immigration & Naturalization Service",
          "cluster_id": 778380,
          "cite": [
            "296 F.3d 871",
            "2002 Daily Journal DAR 8261",
            "2002 Cal. Daily Op. Serv. 6569",
            "2002 U.S. App. LEXIS 14740",
            "2002 WL 1611190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 8437415,
          "cite": [
            "327 F.3d 56"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. 4492 South Livonia Road",
          "cluster_id": 8983256,
          "cite": [
            "889 F.2d 1258",
            "1989 U.S. App. LEXIS 17524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julio Lozada v. Immigration and Naturalization Service",
          "cluster_id": 511756,
          "cite": [
            "857 F.2d 10",
            "1988 U.S. App. LEXIS 12733",
            "1988 WL 94706"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. National Center for Immigrants' Rights, Inc.",
          "cluster_id": 112668,
          "cite": [
            "116 L. Ed. 2d 546",
            "112 S. Ct. 551",
            "502 U.S. 183",
            "1991 U.S. LEXIS 7178",
            "60 U.S.L.W. 4052",
            "91 Daily Journal DAR 15426"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramiro Cruz Espinoza v. Immigration & Naturalization Service",
          "cluster_id": 686823,
          "cite": [
            "45 F.3d 308"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. $191,910.00 in U.S. Currency, Bruce R. Morgan, Claimant-Appellee",
          "cluster_id": 663161,
          "cite": [
            "16 F.3d 1051",
            "94 Daily Journal DAR 2139",
            "94 Cal. Daily Op. Serv. 1214",
            "1994 U.S. App. LEXIS 2681",
            "1994 WL 46744"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Laduke v. Alan C. Nelson, Etc.",
          "cluster_id": 452994,
          "cite": [
            "762 F.2d 1318",
            "1985 U.S. App. LEXIS 19963",
            "53 U.S.L.W. 2625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez Lara v. Lyons",
          "cluster_id": 4983177,
          "cite": [
            "10 F.4th 19"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Immigration & Naturalization Service v. Lopez-Mendoza:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQzNjc2ODAwMDAwJnM9NzkzNzM2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzMmcz01NTY0MDkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
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
    "complete_query": "cites:(111265 OR 9429772 OR 9429773 OR 9429774 OR 9429775 OR 9429776)",
    "indexed_citing_opinions": 715,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111265,
        "count": 619,
        "count_source": "search"
      },
      {
        "opinion_id": 9429772,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9429773,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429774,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429775,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429776,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1189,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/immigration-and-naturalization-service-v-lopez-mendoza.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMDM0NzEmcz05Mzg4MzQxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111265+OR+9429772+OR+9429773+OR+9429774+OR+9429775+OR+9429776%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111265,
        "cited_id": 93665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 97876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 104978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 105227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 105684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 107043,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 111223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 280943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 324058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 328798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 331113,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 350514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 352273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 364939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 374682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 399492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 421840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 427728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 1428147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111265,
        "cited_id": 1600515,
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
    "date_created": "2026-07-05T08:36:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:42:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:36:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Immigration & Naturalization Service v. Lopez-Mendoza

```
<opinion type="majority">
<author id="b1076-4">Justice O’Connor</author>
<p id="AgK">announced the judgment of the Court and delivered the opinion of the Court with respect to Parts I, II, III, and IV, and an opinion with respect to Part V, in which Justice Blackmun, Justice Powell, and Justice Rehnquist joined.<footnotemark>*</footnotemark></p>
<p id="b1076-5">This litigation requires us to decide whether an admission of unlawful presence in this country made subsequently to an allegedly unlawful arrest must be excluded as evidence in a civil deportation hearing. We hold that the exclusionary rule need not be applied in such a proceeding.</p>
<p id="b1076-6">I</p>
<p id="b1076-7">Respondents Adan Lopez-Mendoza and Elias Sandoval-Sanchez, both citizens of Mexico, were summoned to separate deportation proceedings in California and Washington, and both were ordered deported. They challenged the regularity of those proceedings on grounds related to the lawfulness of their respective arrests by officials of the Immigration and Naturalization Service (INS). On administrative appeal the Board of Immigration Appeals (BIA), an agency of the Department of Justice, affirmed the deportation orders.</p>
<p id="b1076-8">The Court of Appeals for the Ninth Circuit, sitting en banc, reversed Sandoval-Sanchez’ deportation order and vacated and remanded Lopez-Mendoza’s deportation order. <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d 1059</a></span> (1983). It ruled that Sandoval-Sanchez’ admission of his illegal presence in this country was the fruit of an unlawful arrest, and that the exclusionary rule applied in a deportation proceeding. Lopez-Mendoza’s deportation order was vacated and his case remanded to the BIA to <page-number citation-index="1" label="1035">*1035</page-number>determine whether the Fourth Amendment had been violated in the course of his arrest. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1037/">464 U. S. 1037</a></span> (1984).</p>
<p id="b1077-5">A</p>
<p id="b1077-6">Respondent Lopez-Mendoza was arrested in 1976 by INS agents at his place of employment, a transmission repair shop in San Mateo, Cal. Responding to a tip, INS investigators arrived at the shop shortly before 8 a. m. The agents had not sought a warrant to search the premises or to arrest any of its occupants. The proprietor of the shop firmly refused to allow the agents to interview his employees during working hours. Nevertheless, while one agent engaged the proprietor in conversation another entered the shop and approached Lopez-Mendoza. In response to the agent’s questioning, Lopez-Mendoza gave his name and indicated that he was from Mexico with no close family ties in the United States. The agent then placed him under arrest. Lopez-Mendoza underwent further questioning at INS offices, where he admitted he was born in Mexico, was still a citizen of Mexico, and had entered this country without inspection by immigration authorities. Based on his answers, the agents prepared a “Record of Deportable Alien” (Form 1-213), and an affidavit which Lopez-Mendoza executed, admitting his Mexican nationality and his illegal entry into this country.</p>
<p id="b1077-7">A hearing was held before an Immigration Judge. Lopez-Mendoza’s counsel moved to terminate the proceeding on the ground that Lopez-Mendoza had been arrested illegally. The judge ruled that the legality of the arrest was not relevant to the deportation proceeding and therefore declined to rule on the legality of Lopez-Mendoza’s arrest. <em>Matter of Lopez-Mendoza, </em>No. A22 452 208 (INS, Dec. 21, 1977), reprinted in App. to Pet. for Cert. 97a. The Form 1-213 and the affidavit executed by Lopez-Mendoza were received into evidence without objection from Lopez-Mendoza. On the basis of this evidence the Immigration Judge found Lopez-<page-number citation-index="1" label="1036">*1036</page-number>Mendoza deportable. Lopez-Mendoza was granted the option of voluntary departure.</p>
<p id="b1078-5">The BIA dismissed Lopez-Mendoza’s appeal. It noted that “[t]he mere fact of an illegal arrest has no bearing on a subsequent deportation proceeding,” <em>In re Lopez-Mendoza, </em>No. A22 452 208 (BIA, Sept. 19, 1979), reprinted in App. to Pet. for Cert. 100a, 102a, and observed that Lopez-Mendoza had not objected to the admission into evidence of Form 1-213 and the affidavit he had executed. <em>Id., </em>at 103a. The BIA also noted that the exclusionary rule is not applied to redress the injury to the privacy of the search victim, and that the BIA had previously concluded that application of the rule in deportation proceedings to deter unlawful INS conduct was inappropriate. <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec. 70</a></span> (BIA 1979).</p>
<p id="b1078-6">The Court of Appeals vacated the order of deportation and remanded for a determination whether Lopez-Mendoza’s Fourth Amendment rights had been violated when he was arrested.</p>
<p id="b1078-7">B</p>
<p id="b1078-8">Respondent Sandoval-Sanchez (who is not the same individual who was involved in <em>Matter of Sandoval, supra) </em>was arrested in 1977 at his place of employment, a potato processing plant in Pasco, Wash. INS Agent Bower and other officers went to the plant, with the permission of its personnel manager, to check for illegal aliens. During a change in shift, officers stationed themselves at the exits while Bower and a uniformed Border Patrol agent entered the plant. They went to the lunchroom and identified themselves as immigration officers. Many people in the room rose and headed for the exits or milled around; others in the plant left their equipment and started running; still others who were entering the plant turned around and started walking back out. The two officers eventually stationed themselves at the main entrance to the plant and looked for passing employees who averted their heads, avoided eye contact, or tried to hide <page-number citation-index="1" label="1037">*1037</page-number>themselves in a group. Those individuals were addressed with innocuous questions in English. Any who could not respond in English and who otherwise aroused Agent Bower’s suspicions were questioned in Spanish as to their right to be in the United States.</p>
<p id="b1079-5">Respondent Sandoval-Sanchez was in a line of workers entering the plant. Sandoval-Sanchez testified that he did not realize that immigration officers were checking people entering the plant, but that he did see standing at the plant entrance a man in uniform who appeared to be a police officer. Agent Bower testified that it was probable that he, not his partner, had questioned Sandoval-Sanchez at the plant, but that he could not be absolutely positive. The employee he thought he remembered as Sandoval-Sanchez had been “very evasive,” had averted his head, turned around, and walked away when he saw Agent Bower. App. 137, 138. Bower was certain that no one was questioned about his status unless his actions had given the agents reason to believe that he was an undocumented alien.</p>
<p id="b1079-6">Thirty-seven employees, including Sandoval-Sanchez, were briefly detained at the plant and then taken to the county jail. About one-third immediately availed themselves of the option of voluntary departure and were put on a bus to Mexico. Sandoval-Sanchez exercised his right to a deportation hearing. Sandoval-Sanchez was then questioned further, and Agent Bower recorded Sandoval-Sanchez’ admission of unlawful entry. Sandoval-Sanchez contends he was not aware that he had a right to remain silent.</p>
<p id="b1079-7">At his deportation hearing Sandoval-Sanchez contended that the evidence offered by the INS should be suppressed as the fruit of an unlawful arrest. The Immigration Judge considered and rejected Sandoval-Sanchez’ claim that he had been illegally arrested, but ruled in the alternative that the legality of the arrest was not relevant to the deportation hearing. <em>Matter of Sandoval-Sanchez, </em>No. A22 346 925 <page-number citation-index="1" label="1038">*1038</page-number>(INS, Oct. 7, 1977), reprinted in App. to Pet. for Cert. 104a. Based on the written record of Sandoval-Sanchez’ admissions the Immigration Judge found him deportable and granted him voluntary departure. The BIA dismissed Sandoval-Sanchez’ appeal. <em>In re Sandoval-Sanchez, </em>No. A22 346 925 (BIA, Feb. 21, 1980). It concluded that the circumstances of the arrest had not affected the voluntariness of his recorded admission, and again declined to invoke the exclusionary rule, relying on its earlier decision in <em>Matter of Sandoval, supra.</em></p>
<p id="b1080-7">On appeal the Court of Appeals concluded that Sandoval-Sanchez’ detention by the immigration officers violated the Fourth Amendment, that the statements he made were a product of that detention, and that the exclusionary rule barred their use in a deportation hearing. The deportation order against Sandoval-Sanchez was accordingly reversed.</p>
<p id="b1080-8">f — n J — 4</p>
<p id="b1080-3">A deportation proceeding is a purely civil action to determine eligibility to remain in this country, not to punish an unlawful entry, though entering or remaining unlawfully in this country is itself a crime. <span class="citation no-link">8 U. S. C. §§ 1302</span>,1306, 1325. The deportation hearing looks prospectively to the respondent’s right to remain in this country in the future. Past conduct is relevant only insofar as it may shed light on the respondent’s right to remain. See <span class="citation no-link">8 U. S. C. §§ 1251</span>, 1252(b); <em>Bugajewitz </em>v. <em>Adams, </em><span class="citation" data-id="97876"><a href="/opinion/97876/bugajewitz-v-adams/#591" aria-description="Citation for case: Bugajewitz v. Adams">228 U. S. 585, 591</a></span> (1913); <em>Fong Yue Ting </em>v. <em>United States, </em><span class="citation" data-id="9417622"><a href="/opinion/93665/fong-yue-ting-v-united-states/#730" aria-description="Citation for case: Fong Yue Ting v. United States">149 U. S. 698, 730</a></span> (1893).</p>
<p id="b1080-4">A deportation hearing is held before an immigration judge. The judge’s sole power is to order deportation; the judge cannot adjudicate guilt or punish the respondent for any crime related to unlawful entry into or presence in this country. Consistent with the civil nature of the proceeding, various protections that apply in the context of a criminal trial do not apply in a deportation hearing. The respondent must be given “a reasonable opportunity to be present at [the] proceeding,” but if the respondent fails to avail himself <page-number citation-index="1" label="1039">*1039</page-number>of that opportunity the hearing may proceed in his absence. <span class="citation no-link">8 U. S. C. § 1252</span>(b). In many deportation cases the INS must show only identity and alienage; the burden then shifts to the respondent to prove the time, place, and manner of his entry. See <span class="citation no-link">8 U. S. C. § 1361</span>; <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec. 70</a></span> (BIA 1979). A decision of deportability need be based only on “reasonable, substantial, and probative evidence,” <span class="citation no-link">8 U. S. C. § 1252</span>(b)(4). The BIA for its part has required only “clear, unequivocal and convincing” evidence of the respondent’s deportability, not proof beyond a reasonable doubt. <span class="citation no-link">8 CFR §242.14</span>(a) (1984). The Courts of Appeals have held, for example that the absence of <em>Miranda </em>warnings does not render an otherwise voluntary statement by the respondent inadmissible in a deportation case. <em>Navia-Duran </em>v. <em>INS, </em><span class="citation" data-id="352273"><a href="/opinion/352273/maria-irma-navia-duran-v-immigration-and-naturalization-service/#808" aria-description="Citation for case: Maria Irma Navia-Duran v. Immigration and Naturalization...">568 F. 2d 803, 808</a></span> (CA1 1977); <em>Avila-Gallegos </em>v. <em>INS, </em><span class="citation" data-id="331113"><a href="/opinion/331113/miguel-avila-gallegos-v-immigration-and-naturalization-service/#667" aria-description="Citation for case: Miguel Avila-Gallegos v. Immigration and Naturalization...">525 F. 2d 666, 667</a></span> (CA2 1975); <em>Chavez-Raya </em>v. <em>INS, </em><span class="citation" data-id="328798"><a href="/opinion/328798/ampara-chavez-raya-and-gloria-quintanar-de-chavez-v-immigration-and/#399" aria-description="Citation for case: Ampara Chavez-Raya and Gloria Quintanar De Chavez v....">519 F. 2d 397, 399-401</a></span> (CA7 1975). See also <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#236" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 236-237</a></span> (1960) (search permitted incidental to an arrest pursuant to an administrative warrant issued by the INS); <em>Galvan </em>v. <em>Press, </em><span class="citation" data-id="9421085"><a href="/opinion/105227/galvan-v-press/#531" aria-description="Citation for case: Galvan v. Press">347 U. S. 522, 531</a></span> (1954) <em>(Ex Post Facto </em>Clause has no application to deportation); <em>Carlson </em>v. <em>Landon, </em><span class="citation" data-id="9420689"><a href="/opinion/104978/carlson-v-landon/#544" aria-description="Citation for case: Carlson v. Landon">342 U. S. 524, 544-546</a></span> (1952) (Eighth Amendment does not require bail to be granted in certain deportation cases); <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S. 149, 157</a></span> (1923) (involuntary confessions admissible at deportation hearing). In short, a deportation hearing is intended to provide a streamlined determination of eligibility to remain in this country, nothing more. The purpose of deportation is not to punish past transgressions but rather to put an end to a continuing violation of the immigration laws.</p>
<p id="b1081-5">III</p>
<p id="b1081-6">The “body” or identity of a defendant or respondent in a criminal or civil proceeding is never itself suppressible as a fruit of an unlawful arrest, even if it is conceded that an unlawful arrest, search, or interrogation occurred. See <em>Ger-</em><page-number citation-index="1" label="1040">*1040</page-number><em>stein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/#522" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519, 522</a></span> (1952); <em>United States ex rel. Bilokumsky </em>v. <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#158" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod"><em>Tod, supra, </em>at 158</a></span>. A similar rule applies in forfeiture proceedings directed against contraband or forfeitable property. See, <em>e. g., United States </em>v. <em>Eighty-Eight Thousand, Five Hundred Dollars, </em><span class="citation" data-id="399492"><a href="/opinion/399492/united-states-v-eighty-eight-thousand-five-hundred-dollars-appeal-of/" aria-description="Citation for case: United States v. Eighty-Eight Thousand, Five Hundred...">671 F. 2d 293</a></span> (CA8 1982); <em>United States </em>v. <em>One (1) 1971 Harley-Davidson Motorcycle, </em><span class="citation" data-id="324058"><a href="/opinion/324058/united-states-v-one-1-1971-harley-davidson-motorcycle-serial-4a25791h1/" aria-description="Citation for case: United States v. One (1) 1971 Harley-Davidson Motorcycle...">508 F. 2d 351</a></span> (CA9 1974); <em>United States </em>v. <em>One 1965 Buick, </em><span class="citation" data-id="280943"><a href="/opinion/280943/united-states-v-one-1965-buick-etc-wilbur-dean-and-delores-dean/" aria-description="Citation for case: United States v. One 1965 Buick, Etc., Wilbur Dean and...">397 F. 2d 782</a></span> (CA6 1968).</p>
<p id="b1082-7">On this basis alone the Court of Appeals’ decision as to respondent Lopez-Mendoza must be reversed. At his deportation hearing Lopez-Mendoza objected only to the fact that he had been summoned to a deportation hearing following an unlawful arrest; he entered no objection to the evidence offered against him. The BIA correctly ruled that “[t]he mere fact of an illegal arrest has no bearing on a subsequent deportation proceeding.”<footnotemark>1</footnotemark> <em>In re Lopez-Mendoza, </em>No. A22 452 208 (BIA, Sept. 19, 1979), reprinted in App. to Pet. for Cert. 102a.</p>
<p id="b1082-8"><em>&gt; </em>HH</p>
<p id="b1082-3">Respondent Sandoval-Sanchez has a more substantial claim. He objected not to his compelled presence at a deportation proceeding, but to evidence offered at that proceeding. The general rule in a criminal proceeding is that statements and other evidence obtained as a result of an unlawful, warrantless arrest are suppressible if the link between the <page-number citation-index="1" label="1041">*1041</page-number>evidence and the unlawful conduct is not too attenuated. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The reach of the exclusionary rule beyond the context of a criminal prosecution, however, is less clear. Although this Court has once stated in dictum that “[i]t may be assumed that evidence obtained by the [Labor] Department through an illegal search and seizure cannot be made the basis of a finding in deportation proceedings,” <em>United States ex rel. Bilokumsky </em>v. <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#155" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod"><em>Tod, supra, </em>at 155</a></span>, the Court has never squarely addressed the question before. Lower court decisions dealing with this question are sparse.<footnotemark>2</footnotemark></p>
<p id="b1083-5">In <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976), this Court set forth a framework for deciding in what types of proceeding application of the exclusionary rule is appropriate. Imprecise as the exercise may be, the Court recognized in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>that there is no choice but to weigh the likely social benefits of excluding unlawfully seized evidence against the likely costs. On the benefit side of the balance “the ‘prime purpose’ of the [exclusionary] rule, if not the sole one, ‘is to deter future unlawful police conduct.’ ” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#446" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 446</a></span>, quoting <em>United States </em>v. Calandra, <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974). On the cost side there is the loss of often probative evidence and all of the secondary costs that flow from the less accurate or more cumbersome adjudication that therefore occurs.</p>
<p id="b1083-6">At stake in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>was application of the exclusionary rule in a federal civil tax assessment proceeding following, the unlawful seizure of evidence by state, not federal, officials. The Court noted at the outset that “[i]n the complex and tur<page-number citation-index="1" label="1042">*1042</page-number>bulent history of the rule, the Court never has applied it to exclude evidence from a civil proceeding, federal or state.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis">428 U. S., at 447</a></span> (footnote omitted). Two factors in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>suggested that the deterrence value of the exclusionary rule in the context of that case was slight. First, the state law enforcement officials were already “punished” by the exclusion of the evidence in the state criminal trial as a result of the same conduct. <em>Id,., </em>at 448. Second, the evidence was also excludable in any federal criminal trial that might be held. Both factors suggested that further application of the exclusionary rule in the federal civil proceeding would contribute little more to the deterrence of unlawful conduct by state officials. On the cost side of the balance, <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>focused simply on the loss of “concededly relevant and reliable evidence.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#447" aria-description="Citation for case: United States v. Janis"><em>Id., </em>at 447</a></span>. The Court concluded that, on balance, this cost outweighed the likely social benefits achievable through application of the exclusionary rule in the federal civil proceeding.</p>
<p id="b1084-5">While it seems likely that the deterrence value of applying the exclusionary rule in deportation proceedings would be higher than it was in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>it is also quite clear that the social costs would be very much greater as well. Applying the <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span> </em>balancing test to the benefits and costs of excluding concededly reliable evidence from a deportation proceeding, we therefore reach the same conclusion as in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>.</em></p>
<p id="b1084-6">The likely deterrence value of the exclusionary rule in deportation proceedings is difficult to assess. On the one hand, a civil deportation proceeding is a civil complement to a possible criminal prosecution, and to this extent it resembles the civil proceeding under review in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>. </em>The INS does not suggest that the exclusionary rule should not continue to apply in criminal proceedings against an alien who unlawfully enters or remains in this country, and the prospect of losing evidence that might otherwise be used in a criminal prosecution undoubtedly supplies some residual deterrent to unlawful conduct by INS officials. But it must be acknowledged <page-number citation-index="1" label="1043">*1043</page-number>that only a very small percentage of arrests of aliens are intended or expected to lead to criminal prosecutions. Thus the arresting officer’s primary objective, in practice, will be to use evidence in the civil deportation proceeding. Moreover, here, in contrast to <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>the agency officials who effect the unlawful arrest are the same officials who subsequently bring the deportation action. As recognized in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>the exclusionary rule is likely to be most effective when applied to such “intrasovereign” violations.</p>
<p id="b1085-5">Nonetheless, several other factors significantly reduce the likely deterrent value of the exclusionary rule in a civil deportation proceeding. First, regardless of how the arrest is effected, deportation will still be possible when evidence not derived directly from the arrest is sufficient to support deportation. As the BIA has recognized, in many deportation proceedings “the sole matters necessary for the Government to establish are the respondent’s identity and alienage — at which point the burden shifts to the respondent to prove the time, place and manner of entry.” <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/#79" aria-description="Citation for case: SANDOVAL">17 I. &amp; N. Dec., at 79</a></span>. Since the person and identity of the respondent are not themselves suppressible, see <em>supra, </em>at 1039-1040, the INS must prove only alienage, and that will sometimes be possible using evidence gathered independently of, or sufficiently attenuated from, the original arrest. See <em>Matter of Sandoval, supra, </em>at 79; see, <em>e. g., Avila-Gallegos </em>v. <span class="citation" data-id="331113"><a href="/opinion/331113/miguel-avila-gallegos-v-immigration-and-naturalization-service/" aria-description="Citation for case: Miguel Avila-Gallegos v. Immigration and Naturalization..."><em>INS, 525 </em>F. 2d 666</a></span> (CA2 1975). The INS’s task is simplified in this regard by the civil nature of the proceeding. As Justice Brandéis stated: “Silence is often evidence of the most persuasive character. . . . [T]here is no rule of law which prohibits officers charged with the administration of the immigration law from drawing an inference from the silence of one who is called upon to speak. ... A person arrested on the preliminary warrant is not protected by a presumption of citizenship comparable to the presumption of innocence in a criminal case. There is no provision which forbids drawing an adverse inference from the fact of stand<page-number citation-index="1" label="1044">*1044</page-number>ing mute.” <em>United States ex rel. Bilokumsky </em>v. <em>Tod, </em><span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#163" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U. S., at 163-154</a></span>.</p>
<p id="b1086-5">The second factor is a practical one. In the course of a year the average INS agent arrests almost 500 illegal aliens. Brief for Petitioner 38. Over 97.5% apparently agree to voluntary deportation without a formal hearing. <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1071" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d, at 1071, n. 17</a></span>. Among the remainder who do request a formal hearing (apparently a dozen or so in all, per officer, per year) very few challenge the circumstances of their arrests. As noted by the Court of Appeals, “the BIA was able to find only two reported immigration cases since 1899 in which the [exclusionary] rule was applied to bar unlawfully seized evidence, only one other case in which the rule’s application was specifically addressed, and fewer than fifty BIA proceedings since 1952 in which a Fourth Amendment challenge to the introduction of evidence was even raised.” <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1071" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service"><em>Id., </em>at 1071</a></span>. Every INS agent knows, therefore, that it is highly unlikely that any particular arrestee will end up challenging the lawfulness of his arrest in a formal deportation proceeding. When an occasional challenge is brought, the consequences from the point of view of the officer’s overall arrest and deportation record will be trivial. In these circumstances, the arresting officer is most unlikely to shape his conduct in anticipation of the exclusion of evidence at a formal deportation hearing.</p>
<p id="b1086-6">Third, and perhaps most important, the INS has its own comprehensive scheme for deterring Fourth Amendment violations by its officers. Most arrests of illegal aliens away from the border occur during farm, factory, or other workplace surveys. Large numbers of illegal aliens are often arrested at one time, and conditions are understandably chaotic. See Brief for Petitioner in <em>INS </em>v. <em>Delgado, </em>O. T. 1983, No. 82-1271, pp. 3-5. To safeguard the rights of those who are lawfully present at inspected workplaces the INS has developed rules restricting stop, interrogation, and arrest practices. <em>Id., </em>at 7, n. 7, 32-40, and n. 25. These <page-number citation-index="1" label="1045">*1045</page-number>regulations require that no one be detained without reasonable suspicion of illegal alienage, and that no one be arrested unless there is an admission of illegal alienage or other strong evidence thereof. New immigration officers receive instruction and examination in Fourth Amendment law, and others receive periodic refresher courses in law. Brief for Petitioner 39-40. Evidence seized through intentionally unlawful conduct is excluded by Department of Justice policy from the proceeding for which it was obtained. See Memorandum from Benjamin R. Civiletti to Heads of Offices, Boards, Bureaus and Divisions, Violations of Search and Seizure Law (Jan. 16, 1981). The INS also has in place a procedure for investigating and punishing immigration officers who commit Fourth Amendment violations. See Office of General Counsel, INS, U. S. Dept, of Justice, The Law of Arrest, Search, and Seizure for Immigration Officers 35 (Jan. 1983). The INS’s attention to Fourth Amendment interests cannot guarantee that constitutional violations will not occur, but it does reduce the likely deterrent value of the exclusionary rule. Deterrence must be measured at the margin.</p>
<p id="b1087-5">Finally, the deterrent value of the exclusionary rule in deportation proceedings is undermined by the availability of alternative remedies for institutional practices by the INS that might violate Fourth Amendment rights. The INS is a single agency, under central federal control, and engaged in operations of broad scope but highly repetitive character. The possibility of declaratory relief against the agency thus offers a means for challenging the validity of INS practices, when standing requirements for bringing such an action can be met. Cf. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984).</p>
<p id="b1087-6">Respondents contend that retention of the exclusionary rule is necessary to safeguard the Fourth Amendment rights of ethnic Americans, particularly the Hispanic-Americans lawfully in this country. We recognize that respondents raise here legitimate and important concerns. But application of the exclusionary rule to civil deportation proceedings <page-number citation-index="1" label="1046">*1046</page-number>can be justified only if the rule is likely to add significant protection to these Fourth Amendment rights. The exclusionary rule provides no remedy for completed wrongs; those lawfully in this country can be interested in its application only insofar as it may serve as an effective deterrent to future INS misconduct. For the reasons we have discussed we conclude that application of the rule in INS civil deportation proceedings, as in the circumstances discussed in <em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis</a></span>, </em>“is unlikely to provide significant, much less substantial, additional deterrence.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S., at 458</a></span>. Important as it is to protect the Fourth Amendment rights of all persons, there is no convincing indication that application of the exclusionary rule in civil deportation proceedings will contribute materially to that end.</p>
<p id="b1088-5">On the other side of the scale, the social costs of applying the exclusionary rule in deportation proceedings are both unusual and significant. The first cost is one that is unique to continuing violations of the law. Applying the exclusionary rule in proceedings that are intended not to punish past transgressions but to prevent their continuance or renewal would require the courts to close their eyes to ongoing violations of the law. This Court has never before accepted costs of this character in applying the exclusionary rule.</p>
<p id="b1088-6">Presumably no one would argue that the exclusionary rule should be invoked to prevent an agency from ordering corrective action at a leaking hazardous waste dump if the evidence underlying the order had been improperly obtained, or to compel police to return contraband explosives or drugs to their owner if the contraband had been unlawfully seized. On the rare occasions that it has considered costs of this type the Court has firmly indicated that the exclusionary rule does not extend this far. See <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#54" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 54</a></span> (1951); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#710" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 710</a></span> (1948). The rationale for these holdings is not difficult to find. “Both <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>and <em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span> </em>concerned objects the possession of which, without more, constitutes a crime. The re<page-number citation-index="1" label="1047">*1047</page-number>possession of such <em>per se </em>contraband by Jeffers and Trupiano would have subjected them to criminal penalties. The return of the contraband would clearly have frustrated the express public policy against the possession of such objects.” <em>One 1958 Plymouth Sedan </em>v. <em>Pennsylvania, </em><span class="citation" data-id="9423021"><a href="/opinion/107043/one-1958-plymouth-sedan-v-pennsylvania/#699" aria-description="Citation for case: One 1958 Plymouth Sedan v. Pennsylvania">380 U. S. 693, 699</a></span> (1965) (footnote omitted). Precisely the same can be said here. Sandoval-Sanchez is a person whose unregistered presence in this country, without more, constitutes a crime.<footnotemark>3</footnotemark> His release within our borders would immediately subject him to criminal penalties. His release would clearly frustrate the express public policy against an alien’s unregistered presence in this country. Even the objective of deterring Fourth Amendment violations should not require such a result. The constable’s blunder may allow the criminal to go free, but we have never suggested that it allows the criminal to continue in the commission of an ongoing crime. When the crime in question involves unlawful presence in this country, the criminal may go free, but he should not go free within our borders.<footnotemark>4</footnotemark></p>
<p id="b1090-4"><page-number citation-index="1" label="1048">*1048</page-number>Other factors also weigh against applying the exclusionary rule in deportation proceedings. The INS currently operates a deliberately simple deportation hearing system, streamlined to permit the quick resolution of very large numbers of deportation actions, and it is against this backdrop that the costs of the exclusionary rule must be assessed. The costs of applying the exclusionary rule, like the benefits, must be measured at the margin.</p>
<p id="b1090-5">The average immigration judge handles about six deportation hearings per day. Brief for Petitioner 27, n. 16. Neither the hearing officers nor the attorneys participating in those hearings are likely to be well versed in the intricacies of Fourth Amendment law. The prospect of even occasional invocation of the exclusionary rule might significantly change and complicate the character of these proceedings. The BIA has described the practical problems as follows:</p>
<blockquote id="b1090-6">“Absent the applicability of the exclusionary rule, questions relating to deportability routinely involve simple factual allegations and matters of proof. When Fourth Amendment issues are raised at deportation hearings, the result is a diversion of attention from the main issues which those proceedings were created to resolve, both in terms of the expertise of the administrative decision makers and of the structure of the forum to accommodate inquiries into search and seizure questions. The result frequently seems to be a long, confused record in which the issues are not clearly defined and in which there is voluminous testimony .... The ensuing delays and inordinate amount of time spent on such cases at all levels has an adverse impact on the effective adminis<page-number citation-index="1" label="1049">*1049</page-number>tration of the immigration laws .... This is particularly true in a proceeding where delay may be the only ‘defense’ available and where problems already exist with the use of dilatory tactics.” <em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">Matter of Sandoval</a></span>, </em>17 I. &amp; N., at 80 (footnote omitted).</blockquote>
<p id="b1091-5">This sober assessment of the exclusionary rule’s likely costs, by the agency that would have to administer the rule in at least the administrative tiers of its application, cannot be brushed off lightly.</p>
<p id="b1091-6">The BIA’s concerns are reinforced by the staggering dimension of the problem that the INS confronts. Immigration officers apprehend over one million deportable aliens in this country every year. <span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/#85" aria-description="Citation for case: SANDOVAL">Id., at 85</a></span>. A single agent may arrest many illegal aliens every day. Although the investigatory burden does not justify the commission of constitutional violations, the officers cannot be expected to compile elaborate, contemporaneous, written reports detailing the circumstances of every arrest. At present an officer simply completes a “Record of Deportable Alien” that is introduced to prove the INS’s case at the deportation hearing; the officer rarely must attend the hearing. Fourth Amendment suppression hearings would undoubtedly require considerably more, and the likely burden on the administration of the immigration laws would be correspondingly severe.</p>
<p id="b1091-7">Finally, the INS advances the credible argument that applying the exclusionary rule to deportation proceedings might well result in the suppression of large amounts of information that had been obtained entirely lawfully. INS arrests occur in crowded and confused circumstances. Though the INS agents are instructed to follow procedures that adequately protect Fourth Amendment interests, agents will usually be able to testify only to the fact that they followed INS rules. The demand for a precise account of exactly what happened in each particular arrest would plainly preclude mass arrests, even when the INS is confronted, <page-number citation-index="1" label="1050">*1050</page-number>as it often is, with massed numbers of ascertainably illegal aliens, and even when the arrests can be and are conducted in full compliance with all Fourth Amendment requirements.</p>
<p id="b1092-5">In these circumstances we are persuaded that the <em>Jams </em>balance between costs and benefits comes out against applying the exclusionary rule in civil deportation hearings held by the INS. By all appearances the INS has already taken sensible and reasonable steps to deter Fourth Amendment violations by its officers, and this makes the likely additional deterrent value of the exclusionary rule small. The costs of applying the exclusionary rule in the context of civil deportation hearings are high. In particular, application of the exclusionary rule in cases such as Sandoval-Sanchez’, would compel the courts to release from custody persons who would then immediately resume their commission of a crime through their continuing, unlawful presence in this country. “There comes a point at which courts, consistent with their duty to administer the law, cannot continue to create barriers to law enforcement in the pursuit of a supervisory role that is properly the duty of the Executive and Legislative Branches.” <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#459" aria-description="Citation for case: United States v. Janis">428 U. S., at 459</a></span>. That point has been reached here.</p>
<p id="b1092-6">y</p>
<p id="b1092-7">We do not condone any violations of the Fourth Amendment that may have occurred in the arrests of respondents Lopez-Mendoza or Sandoval-Sanchez. Moreover, no challenge is raised here to the INS’s own internal regulations. Cf. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210</a></span> (1984). Our conclusions concerning the exclusionary rule’s value might change, if there developed good reason to believe that Fourth Amendment violations by INS officers were widespread. Cf. <em>United States </em>v. <em>Leon, ante, </em>at 928 (Blackmun, J., concurring). Finally, we do not deal here with egregious violations of Fourth Amendment or other liberties that might transgress notions of fundamental fairness and undermine <page-number citation-index="1" label="1051">*1051</page-number>the probative value of the evidence obtained.<footnotemark>5</footnotemark> Cf. <em>Rochin </em>v. <em>California, </em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952). At issue here is the exclusion of credible evidence gathered in connection -with peaceful arrests by INS officers. We hold that evidence derived from such arrests need not be suppressed in an INS civil deportation hearing.</p>
<p id="b1093-5">The judgment of the Court of Appeals is therefore</p>
<p id="b1093-6">
<em>Reversed.</em>
</p>
<footnote label="*">
<p id="b1076-9">The Chief Justice joins all but Part V of this opinion.</p>
</footnote>
<footnote label="1">
<p id="b1082-4"> The Court of Appeals brushed over Lopez-Mendoza’s failure to object to the evidence in an apparently unsettled footnote of its decision. The Court of Appeals was initially of the view that a motion to terminate a proceeding on the ground that the arrest of the respondent was unlawful is, “for all practical purposes,” the same as a motion to suppress evidence as the fruit of an unlawful arrest. Slip opinion, at 1765, n. 1 (Apr. 25, 1983). In the bound report of its opinion, however, the Court of Appeals takes a somewhat different view, stating in a revised version of the same footnote that “the only reasonable way to interpret the motion to terminate is as one that includes both a motion to suppress and a motion to dismiss.” <span class="citation" data-id="8916793"><a href="/opinion/8927000/lopez-mendoza-v-immigration-naturalization-service/#1060" aria-description="Citation for case: Lopez-Mendoza v. Immigration &amp; Naturalization Service">705 F. 2d 1059, 1060, n. 1</a></span> (1983).</p>
</footnote>
<footnote label="2">
<p id="b1083-7"> In <em>United States </em>v. <em>Wong Quong Wong, </em><span class="citation" data-id="9336336"><a href="/opinion/9340976/united-states-v-wong-quong-wong/" aria-description="Citation for case: United States v. Wong Quong Wong">94 F. 832</a></span> (Vt. 1899), a District Judge excluded letters seized from the appellant in a civil deportation proceeding. In <em>Ex parte Jackson, </em><span class="citation" data-id="8815099"><a href="/opinion/8830191/ex-parte-jackson/" aria-description="Citation for case: Ex parte Jackson">263 F. 110</a></span> (Mont.), appeal dism’d <em>sub nom. Andrews </em>v. <em>Jackson, </em><span class="citation" data-id="8817491"><a href="/opinion/8832507/andrews-v-jackson/" aria-description="Citation for case: Andrews v. Jackson">267 F. 1022</a></span> (CA9 1920), another District Judge granted habeas corpus relief on the ground that papers and pamphlets used against the habeas petitioner in a deportation proceeding had been unlawfully seized. <em>Wong Chung Che </em>v. <em>INS, </em><span class="citation" data-id="350514"><a href="/opinion/350514/wong-chung-che-and-wong-pui-tong-v-immigration-and-naturalization-service/" aria-description="Citation for case: Wong Chung Che and Wong Pui Tong v. Immigration and...">565 F. 2d 166</a></span> (CA11977), held that papers obtained by INS agents in an unlawful search are inadmissible in deportation proceedings.</p>
</footnote>
<footnote label="3">
<p id="b1089-5"> Sandoval-Sanchez was arrested on June 23, 1977. His deportation hearing was held on October 7, 1977. By that time he was under a duty to apply for registration as an alien. A failure to do so plainly constituted a continuing crime. <span class="citation no-link">8 U. S. C. §§ 1302</span>, 1306. Sandoval-Sanchez was not, of course, prosecuted for this crime, and we do not know whether or not he did make the required application. But it is safe to assume that the exclusionary rule would never be at issue in a deportation proceeding brought against an alien who entered the country unlawfully and then voluntarily admitted to his unlawful presence in an application for registration.</p>
<p id="b1089-6">Sandoval-Sanchez was also not prosecuted for his initial illegal entry into this country, an independent crime under <span class="citation no-link">8 U. S. C. § 1326</span>. We need not decide whether or not remaining in this country following an illegal entry is a continuing or a completed crime under § 1325. The question is academic, of course, since in either event the unlawful entry remains both punishable and continuing grounds for deportation. See <span class="citation no-link">8 U. S. C. § 1251</span>(a)(2).</p>
</footnote>
<footnote label="4">
<p id="b1089-7"> Similarly, in <em>Sure-Tan, Inc. </em>v. <em>NLRB, </em><span class="citation" data-id="9842062"><a href="/opinion/111223/sure-tan-inc-v-national-labor-relations-board/" aria-description="Citation for case: Sure-Tan, Inc. v. National Labor Relations Board">467 U. S. 883</a></span> (1984), the Court concluded that an employer can be guilty of an unfair labor practice in his dealings with an alien notwithstanding the alien’s illegal presence in this country. Retrospective sanctions against the employer may accord<page-number citation-index="1" label="1048">*1048</page-number>ingly be imposed by the National Labor Relations Board to further the public policy against unfair labor practices. But while he maintains the status of an illegal alien, the employee is plainly not entitled to the prospective relief — reinstatement and continued employment — that probably would be granted to other victims of similar unfair labor practices.</p>
</footnote>
<footnote label="5">
<p id="b1093-9"> We note that subsequent to its decision in <em>Matter of Sandoval, </em><span class="citation" data-id="6075329"><a href="/opinion/6208751/sandoval/" aria-description="Citation for case: SANDOVAL">17 I. <em>&amp; </em>N. Dec. 70</a></span> (1979), the BIA held that evidence will be excluded if the circumstances surrounding a particular arrest and interrogation would render use of the evidence obtained thereby “fundamentally unfair” and in violation of due process requirements of the Fifth Amendment. <em>Matter of Toro, </em>17 I. &amp;. N. Dec. 340, 343 (1980). See also <em>Matter of Garcia, </em><span class="citation" data-id="6075297"><a href="/opinion/6208719/garcia/#321" aria-description="Citation for case: GARCIA">17 I. &amp; N. Dec. 319, 321</a></span> (1980) (suppression of admission of alienage obtained after request for counsel had been repeatedly refused); <em>Matter of Ramira-Cordova, </em>No. A21 095 659 (Feb. 21, 1980) (suppression of evidence obtained as a result of a nighttime warrantless entry into the aliens’ residence).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/J.D.B. v. North Carolina.md  (`case`, 5 assertions)

### content_page

```
---
title: "J.D.B. v. North Carolina"
type: case
citation: "564 U.S. 261 (2011)"
parallel_cite: "180 L. Ed. 2d 310; 131 S. Ct. 2394"
neutral_cite: 2011 U.S. LEXIS 4557
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-06-16
docket: 09-11121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: J.D.B. v. North Carolina
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7345714/j-d-b-v-north-carolina/"
  cluster_id: 7345714
  opinion_id: 7263680
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Yarborough v. Alvarado]]", "[[Berkemer v. McCarty]]", "[[Miranda v. Arizona]]", "[[Stansbury v. California]]"]
aliases: ["In re J.D.B."]
tags: ["case", "fifth-amendment", "miranda", "custody", "juveniles", "age"]
holding: "A child's age is a relevant factor in the Miranda custody analysis when it was known to or objectively apparent to the officer — because…"
lake:
  record_id: J.D.B. v. North Carolina
  status: verified
  projected_at: 2026-07-06
---

# J.D.B. v. North Carolina

*564 U.S. 261 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
J.D.B., a 13-year-old seventh-grader, was removed from his classroom by a uniformed officer, taken to a closed conference room, and questioned by police and school officials for thirty to forty-five minutes about neighborhood break-ins. He was not given *[[Miranda v. Arizona|Miranda]]* warnings, was not told he could leave or call a guardian, and ultimately confessed. The North Carolina courts held his age was irrelevant to whether he was in custody.

## Issue
Whether a child's age is relevant to the *[[Miranda v. Arizona|Miranda]]* custody analysis when that age is known to, or objectively apparent to, the officer who questions the child.

## Rule
Yes. "It is beyond dispute that children will often feel bound to submit to police questioning when an adult in the same circumstances would feel free to leave. Seeing no reason for police officers or courts to blind themselves to that commonsense reality, we hold that a child's age properly informs the Miranda custody analysis." — *J.D.B. v. North Carolina*, 564 U.S. 261 (2011) (slip op., at 1). ^pin-op1

Including age keeps the analysis objective: "So long as the child's age was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances 'unknowable' to them . . . nor to 'anticipat[e] the frailties or idiosyncrasies' of the particular suspect whom they question." — *Id.* (slip op., at 11). ^pin-op11

## Application
J.D.B.'s age — 13 — was known to the officers, who questioned him at his school; because age is an objective fact bearing on how a reasonable child in his position would have understood the situation, the state courts erred in excluding it from the custody inquiry. The Court did not itself decide whether J.D.B. was in custody; it [[Reading and Citing Cases#on-remand|remanded]] for the state courts to address custody taking account of all the circumstances, including his age.

## Conclusion
A child's age, when known or objectively apparent, must be considered in the *[[Miranda v. Arizona|Miranda]]* custody analysis; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *J.D.B.* distinguishes [[Yarborough v. Alvarado]] and brings a child's age into the objective custody test of [[Miranda v. Arizona]] and [[Berkemer v. McCarty]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *J.D.B. v. North Carolina*, 564 U.S. 261 (2011) — https://www.courtlistener.com/opinion/218925/j-d-b-v-north-carolina/ — pinpoints given as slip-opinion pages (slip op., at 1, 11); CourtListener carries the slip opinion, paginated by slip page (opinion 218925).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b3f55408f546b5b2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "564 U.S. 261 (2011)", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 4557", "official_citation_present": true, "parallel_cite": "180 L. Ed. 2d 310; 131 S. Ct. 2394", "title": "J.D.B. v. North Carolina", "year": "2011"}}
{"assertion_id": "8c74cc99d9b896de", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A child's age is a relevant factor in the Miranda custody analysis when it was known to or objectively apparent to the officer — because…", "title": "J.D.B. v. North Carolina"}}
{"assertion_id": "8dce00aa7868ebc6", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "J.D.B. v. North Carolina"}}
{"assertion_id": "1ec9e01584ad80ad", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-06-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "J.D.B. v. North Carolina", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "J.D.B. v. North Carolina", "varies_by_point": "false"}}
{"assertion_id": "cccdb60e74e4f8cf", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "J.D.B. v. North Carolina"}}
```

### lake record — J.D.B. v. North Carolina

```json
{
  "schema_version": "s2.v1",
  "record_id": "J.D.B. v. North Carolina",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "J. D. B. v. North Carolina",
    "case_name_short": "",
    "case_name_full": "J. D. B. v. NORTH CAROLINA",
    "input_case_name": "J.D.B. v. North Carolina",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-06-16",
    "year": 2011,
    "docket": "09-11121",
    "cluster_id": 7345714,
    "lead_opinion_id": 7263680,
    "sibling_ids": [
      7263680,
      7263681
    ],
    "absolute_url": "/opinion/7345714/j-d-b-v-north-carolina/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 218925,
        "score": 120,
        "case_name": "J. D. B. v. North Carolina"
      },
      {
        "cluster_id": 7342486,
        "score": 20,
        "case_name": "J. D. B. v. North Carolina"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "564 U.S. 261",
      "volume": "564",
      "reporter": "U.S.",
      "page": "261",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "180 L. Ed. 2d 310",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "310",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2394",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4557",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4557",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "180 L. Ed. 2d 310",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "310",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4557",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4557",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2394",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "564 U.S. 261",
        "volume": "564",
        "reporter": "U.S.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "564 U.S. 261",
    "official_selection": {
      "court_class": "scotus",
      "selected": "564 U.S. 261",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # J.D.B. v. North Carolina *564 U.S. 261 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background J.D.B., a 13-year-old seventh-grader, was removed from his classroom by a uniformed officer, taken to a closed conference room, and questioned by police and school officials for thirty to forty-five minutes about neighborhood break-ins. He was not given *Miranda* warnings, was not told he could leave or call a guardian, and ultimately confessed. The North Carolina courts held his age was irrelevant to whether he was in custody. ## Issue Whether a child's age is relevant to the *Miranda* custody analysis when that age is known to, or objectively apparent to, the officer who questions the child. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op11",
      "page": null,
      "quote": "So long as the child's age was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances 'unknowable' to them . . . nor to 'anticipat[e] the frailties or idiosyncrasies' of the particular suspect whom they question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "J.D.B. v. North Carolina",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Mattis",
          "cluster_id": 9459197,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re E.W.",
          "cluster_id": 2770572,
          "cite": [
            "198 Vt. 311",
            "2015 VT 7",
            "114 A.3d 112",
            "2015 Vt. LEXIS 7"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Aalim (Slip Opinion)",
          "cluster_id": 4394360,
          "cite": [
            "2017 Ohio 2956",
            "150 Ohio St. 3d 489"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 2690164,
          "cite": [
            "2014 Ohio 849",
            "138 Ohio St. 3d 478",
            "8 N.E.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sara Dees v. County of San Diego",
          "cluster_id": 4756523,
          "cite": [
            "960 F.3d 1145"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rachel Scanlon v. County of Los Angeles",
          "cluster_id": 9471587,
          "cite": [
            "92 F.4th 781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 5145789,
          "cite": [
            "55 A.3d 432",
            "2012 ME 126",
            "2012 Me. LEXIS 126"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Soderman",
          "cluster_id": 4841363,
          "cite": [
            "983 F.3d 369"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Boyer v. Darrel Vannoy, Warden",
          "cluster_id": 4409622,
          "cite": [
            "863 F.3d 428",
            "2017 U.S. App. LEXIS 12764",
            "2017 WL 3016043"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado, Petitioner/Cross-Respondent, IN the INTEREST OF T.B., Respondent/Cross-Petitioner",
          "cluster_id": 10018886,
          "cite": [
            "489 P.3d 752"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
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
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. G.O.",
          "cluster_id": 9480222,
          "cite": [
            "543 P.3d 1096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bush",
          "cluster_id": 9450931,
          "cite": [
            "231 N.E.3d 569",
            "2023 Ohio 4473"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bermudez",
          "cluster_id": 6589872,
          "cite": [
            "83 Mass. App. Ct. 46",
            "980 N.E.2d 462",
            "2012 Mass. App. LEXIS 294"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. J.H.-M.",
          "cluster_id": 10376010,
          "cite": [
            "566 P.3d 847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re T.D.S.",
          "cluster_id": 9476954,
          "cite": [
            "2024 Ohio 595"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jimmie Bowen v. Secretary, Florida Department of Corrections",
          "cluster_id": 9475524,
          "cite": [
            "92 F.4th 1328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ervin Leggette",
          "cluster_id": 9357989,
          "cite": [
            "57 F.4th 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matter of Luis P.",
          "cluster_id": 10688544,
          "cite": [
            "32 N.Y.3d 1165",
            "2018 NY Slip Op 08427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campos-Ayala",
          "cluster_id": 9514436,
          "cite": [
            "105 F.4th 235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond Lewis v. Chance Andes",
          "cluster_id": 9483149,
          "cite": [
            "95 F.4th 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Heatherington",
          "cluster_id": 6462570,
          "cite": [
            "2022 Ohio 1375"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jorge Leal",
          "cluster_id": 4893446,
          "cite": [
            "1 F.4th 545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re R.C.",
          "cluster_id": 4745406,
          "cite": [
            "2020 Ohio 1486"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Logan T. Kruckenberg Anderson",
          "cluster_id": 10111918,
          "cite": [
            "2024 WI App 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "J.D.B. v. North Carolina:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7263680 OR 7263681) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 3,
        "triage_snippet_classified": 66
      },
      "lane2_top_cited": {
        "query": "cites:(7263680 OR 7263681)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xJnM9NzMzNTgzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287263680+OR+7263681%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7263680 OR 7263681)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 1,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7263680 OR 7263681)",
    "indexed_citing_opinions": 80,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7263680,
        "count": 80,
        "count_source": "search"
      },
      {
        "opinion_id": 7263681,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 563,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/j-d-b-v-north-carolina.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NDk2MjImcz05NDcxNTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287263680+OR+7263681%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T08:42:32Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:46:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:43:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — J.D.B. v. North Carolina

```
<opinion type="majority">
<p id="b360-4">OPINION OF THE COURT</p>
<p id="b360-5">[<span class="citation no-link">564 U.S. 264</span>]</p>
<author id="b360-6">Justice Sotomayor</author>
<p id="ARdO">delivered the opinion of the Court.</p>
<p id="b360-7">This case presents the question whether the age of a child subjected to police questioning is relevant to the custody analysis of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (1966). It is beyond dispute that children will often feel bound to submit to police questioning when an adult in the same circumstances</p>
<p id="b360-15">[<span class="citation no-link">564 U.S. 265</span>]</p>
<p id="b360-16">would feel free to leave. Seeing no reason for police officers or courts to blind themselves to that <page-number citation-index="1" label="319">*319</page-number>commonsense reality, we hold that  a child’s age properly informs the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis.</p>
<p id="b361-4">I</p>
<p id="b361-5">A</p>
<p id="b361-6">Petitioner J. D. B. was a 13-year-old, seventh-grade student attending class at Smith Middle School in Chapel Hill, North Carolina, when he was removed from his classroom by a uniformed police officer, escorted to a closed-door conference room, and questioned by police for at least half an hour.</p>
<p id="b361-7">This was the second time that police questioned J. D. B. in the span of a week. Five days earlier, two home break-ins occurred, and various items were stolen. Police stopped and questioned J. D. B. after he was seen behind a residence in the neighborhood where the crimes occurred. That same day, police also spoke to J. D. B.’s grandmother—his legal guardian—as well as his aunt.</p>
<p id="b361-8">Police later learned that a digital camera matching the description of one of the stolen items had been found at J. D. B.’s middle school and seen in J. D. B.’s possession. Investigator DiCostanzo, the juvenile investigator with the local police force who had been assigned to the case, went to the school to question J. D. B. Upon arrival, DiCostanzo informed the uniformed police officer on detail to the school (a so-called school resource officer), the assistant principal, and an administrative intern that he was there to question J. D. B. about the break-ins. Although DiCostanzo asked the school administrators to verify J. D. B.’s date of birth, address, and parent contact information from school records, neither the police officers nor the school administrators contacted J. D. B.’s grandmother.</p>
<p id="b361-10">The uniformed officer interrupted J. D. B.’s afternoon social studies class, removed J. D. B. from the classroom, and</p>
<p id="b361-11">[<span class="citation no-link">564 U.S. 266</span>]</p>
<p id="b361-12">escorted him to a school conference room.<footnotemark>1</footnotemark> There, J. D. B. was met by DiCostanzo, the assistant principal, and the administrative intern. The door to the conference room was closed. With the two police officers and the two administrators present, J. D. B. was questioned for the next 30 to 45 minutes. Prior to the commencement of questioning, J. D. B. was given neither <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings nor the opportunity to speak to his grandmother. Nor was he informed that he was free to leave the room.</p>
<p id="b361-13">Questioning began with small talk— discussion of sports and J. D. B.’s family life. DiCostanzo asked, and J. D. B. agreed, to discuss the events of the prior weekend. Denying any wrongdoing, J. D. B. explained that he had been in the neighborhood where the crimes occurred because he was seeking work mowing lawns. DiCostanzo pressed J. D. B. for additional detail about his efforts to obtain work; asked J. D. B. to explain a prior incident, when one of the victims returned home to find J. D. B. behind her house; and confronted J. D. B. with the stolen camera. The assistant principal urged J. D. B. to “do the right thing,” warning J. D. B. that “the truth always comes out in the end.”App. 99a, 112a.</p>
<p id="b362-3"><page-number citation-index="1" label="320">*320</page-number>Eventually, J. D. B. asked whether he would “still be in trouble” if he returned the “stuff.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>In response, DiCostanzo explained that return of the stolen items would be helpful, but “this thing is going to court” regardless. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 112a; <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span> </em>(“[W]hat’s done is done[;] now you need to help yourself by making it right”); see also <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span> </em>at 99a. DiCostanzo then warned that he may need to seek a secure custody order if he believed that J. D. B. would continue to break into other homes. When J. D. B. asked what a secure custody</p>
<p id="b362-4">[<span class="citation no-link">564 U.S. 267</span>]</p>
<p id="b362-5">order was, DiCostanzo explained that “it’s where you get sent to juvenile detention before court.” <em><span class="citation no-link">Id.,</span> </em>at 112a.</p>
<p id="b362-6">After learning of the prospect of juvenile detention, J. D. B. confessed that he and a friend were responsible for the break-ins. DiCostanzo only then informed J. D. B. that he could refuse to answer the investigator’s questions and that he was free to leave.<footnotemark>2</footnotemark> Asked whether he understood, J. D. B. nodded and provided further detail, including information about the location of the stolen items. Eventually J. D. B. wrote a statement, at DiCostanzo’s request. When the bell rang indicating the end of the school-day, J. D. B. was allowed to leave to catch the bus home.</p>
<p id="b362-7">B</p>
<p id="b362-8">Two juvenile petitions were filed against J. D. B., each alleging one count of breaking and entering and one count of larceny. J. D. B.’s public defender moved to suppress his statements and the evidence derived therefrom, arguing that suppression was necessary because J. D. B. had been “interrogated by police in a custodial setting without being afforded <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning[s],” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 89a, and because his</p>
<p id="b362-10">[<span class="citation no-link">564 U.S. 268</span>]</p>
<p id="b362-11">statements were involuntary under the totality of the circumstances test, <em><span class="citation no-link">id.,</span> </em>at 142a; see <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218, 226</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S. Ct. 2041</a></span>, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L. Ed. 2d 854</a></span> (1973) (due process precludes admission of a confession where “a defendant’s will was overborne” by the circumstances of the interrogation). After a suppression hearing at which DiCostanzo and J. D. B. testified, the trial court denied the motion, deciding that J. D. B. was not in custody at the time of the schoolhouse interrogation and that his statements were voluntary. As a result, J. D. B. entered a transcript of admission to all four counts, renewing his objection enial of his motion to suppress, and the court adjudicated J. D. B. delinquent.</p>
<p id="b362-12">A divided panel of the North Carolina Court of Appeals affirmed. <em>In re J. D. B., </em><span class="citation" data-id="8899249"><a href="/opinion/8911477/in-re-jdb/" aria-description="Citation for case: In re J.D.B.">196 N.C. App. 234</a></span>, <span class="citation" data-id="8899249"><a href="/opinion/8911477/in-re-jdb/" aria-description="Citation for case: In re J.D.B.">674 S.E.2d 795</a></span> (2009). The North Carolina Supreme Court held, over two dissents, that J. D. B. was not in custody when he confessed, “declin<page-number citation-index="1" label="321">*321</page-number>[ing] to extend the test for custody to include consideration of the age ... of an individual subjected to questioning by police.” <em>In re J. D. B., </em><span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#672" aria-description="Citation for case: In re J.D.B.">363 N.C. 664, 672</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#140" aria-description="Citation for case: In re J.D.B.">686 S.E.2d 135, 140</a></span> (2009) <footnotemark>3</footnotemark></p>
<p id="b363-4">We granted certiorari to determine whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis includes consideration of a juvenile suspect’s age. <span class="citation multiple-matches"><a href="/c/U.S./562/1001/">562 U.S. 1001</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/502/">131 S. Ct. 502</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/368/">178 L. Ed. 2d 368</a></span> (2010).</p>
<p id="b363-5">II</p>
<p id="b363-6">A</p>
<p id="b363-7">Any police interview of an individual suspected of a crime has “coercive aspects to it.” <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U.S. 492, 495</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">97 S. Ct. 711</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">50 L. Ed. 2d 714</a></span> (1977) <em>(per curiam). </em>Only those interrogations that occur while a suspect is in police custody, however, “heighte[n] the risk” that statements obtained are not the</p>
<p id="b363-8">[<span class="citation no-link">564 U.S. 269</span>]</p>
<p id="b363-9">product of the suspect’s free choice. <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428, 435</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span> (2000).</p>
<p id="b363-10">By its very nature, custodial police interrogation entails “inherently compelling pressures.” <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 467</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. Even for an adult, the physical and psychological isolation of custodial interrogation can “undermine the individual’s will to resist and . . . compel him to speak where he would not otherwise do so freely.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Indeed, the pressure of custodial interrogation is so immense that it “can induce a frighteningly high percentage of people to confess to crimes they never committed.” <em>Corley </em>v. <em>United States, </em><span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/#321" aria-description="Citation for case: Corley v. United States">556 U.S. 303, 321</a></span>, <span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/" aria-description="Citation for case: Corley v. United States">129 S. Ct. 1558</a></span>, <span class="citation" data-id="145888"><a href="/opinion/145888/corley-v-united-states/" aria-description="Citation for case: Corley v. United States">173 L. Ed. 2d 443</a></span> (2009) (citing Drizin <em>&amp; </em>Leo, The Problem of False Confessions in the Post-DNA World, <span class="citation no-link">82 N.C. L. Rev. 891</span>, 906-907 (2004)); see also <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 455, n. 23</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. That risk is all the more troubling—and recent studies suggest, all the more acute—when the subject of custodial interrogation is a juvenile. See Brief for Center on Wrongful Convictions of Youth et al. as <em>Amici Curiae </em>21-22 (collecting empirical studies that “illustrate the heightened risk of false confessions from youth”).</p>
<p id="b363-12">Recognizing that the inherently coercive nature of custodial interrogation “blurs the line between voluntary and involuntary statements,” <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 435</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span>, this Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>adopted a set of prophylactic measures designed to safeguard the constitutional guarantee against self-incrimination. Prior to questioning, a suspect “must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 444</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see also <em>Florida </em>v. <em>Powell, </em><span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/#60" aria-description="Citation for case: Florida v. Powell">559 U.S. 50, 60</a></span>, <span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/" aria-description="Citation for case: Florida v. Powell">130 S. Ct. 1195</a></span>, <span class="citation" data-id="9413180"><a href="/opinion/1736/florida-v-powell/" aria-description="Citation for case: Florida v. Powell">175 L. Ed. 2d 1009</a></span> (2010) (“The four warnings <em>Miranda </em>requires are invariable, but this Court has not dictated the words in which the essential information must be conveyed”). And, if a suspect makes a statement during custodial interrogation, the burden is on the Government to show, as a “prerequisitje]” to the statement’s admissibility as evi<page-number citation-index="1" label="322">*322</page-number>dence</p>
<p id="b364-4">[<span class="citation no-link">564 U.S. 270</span>]</p>
<p id="b364-5">in the Government’s case in chief, that the defendant “voluntarily, knowingly and intelligently” waived his <em>rights.</em><footnotemark><em>4</em></footnotemark><em> Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 444, 475-476</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 443-444</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span>.</p>
<p id="b364-6">Because these measures protect the individual against the coercive nature of custodial interrogation, they are required “ ‘only where there has been such a restriction on a person’s freedom as to render him “in custody.” ’ ” <em>Stansbury </em>v. <em>California, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U.S. 318, 322</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span> (1994) <em>(per curiam) </em>(quoting <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U.S., at 495</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">97 S. Ct. 711</a></span>, <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">50 L. Ed. 2d 714</a></span>). As we have repeatedly emphasized,  whether a suspect is “in custody” is an objective inquiry.</p>
<blockquote id="b364-7">“Two discrete inquiries are essential to the determination: first, what were the circumstances surrounding the interrogation; and second, given those circumstances, would a reasonable person have felt he or she was at liberty to terminate the interrogation and leave. Once the scene is set and the players’ lines and actions are reconstructed, the court must apply an objective test to resolve the ultimate inquiry: was there a formal arrest or restraint on freedom of movement of the degree associated with formal arrest.” <em>Thompson </em>v. <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U.S. 99, 112</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span> (1995) (internal quotation marks, alteration, and footnote omitted).</blockquote>
<p id="b364-8">See also <em>Yarborough </em>v. <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#662" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S. 652, 662-663</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (2004); <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U.S., at 323</a></span>; <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U.S. 420, 442</a></span>, and n. 35, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (1984).  Rather than demarcate a limited set of relevant circumstances, we have required police officers and courts to “examine all of the circumstances</p>
<p id="b364-10">[<span class="citation no-link">564 U.S. 271</span>]</p>
<p id="anf-dedup-1">surrounding the interrogation,” <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U.S., at 322</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>, including any circumstance that “would have affected how a reasonable person” in the suspect’s position “would perceive his or her freedom to leave,” <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California"><em>id., </em>at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. On the other hand, the “subjective views harbored by either the interrogating officers or the person being questioned” are irrelevant. <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California"><em>Id., </em>at 323</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. The test, in other words, involves no consideration of the “actual mindset” of the particular suspect subjected to police questioning. <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#667" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 667</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>; see also <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U.S. 1121, 1125, n. 3</a></span>, <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">103 S. Ct. 3517</a></span>, <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">77 L. Ed. 2d 1275</a></span> (1983) <em>(per curiam).</em></p>
<p id="b364-11">The benefit of the objective custody analysis is that it is “designed to give clear guidance to the police.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. But see <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 441</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (recognizing the “occasional!] . . . difficulty” that police and courts nonetheless have in “deciding exactly when a suspect has been taken into custody”). Police must make in-the-moment judgments as to <page-number citation-index="1" label="323">*323</page-number>when to administer <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. By limiting analysis to the objective circumstances of the interrogation, and asking how a reasonable person in the suspect’s position would understand his freedom to terminate questioning and leave, the objective test avoids burdening police with the task of anticipating the idiosyncrasies of every individual suspect and divining how those particular traits affect each person’s subjective state of mind. See <em>id., </em>at 430-431, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (officers are not required to “make guesses” as to circumstances “unknowable” to them at the time); <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (officers are under no duty “to consider . . . contingent psychological factors when deciding when suspects should be advised of their <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights”).</p>
<p id="b365-5">B</p>
<p id="b365-6">The State and its <em>amici </em>contend that a child’s age has no place in the custody analysis, no matter how young the child subjected to police questioning. We cannot agree.  In some circumstances, a child’s age “would have affected how a reasonable</p>
<p id="b365-7">[<span class="citation no-link">564 U.S. 272</span>]</p>
<p id="b365-8">person” in the suspect’s position “would perceive his or her freedom to leave.” <em>Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California">511 U.S., at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. That is, a reasonable child subjected to police questioning will sometimes feel pressured to submit when a reasonable adult would feel free to go. We think it clear that courts can account for that reality without doing any damage to the objective nature of the custody analysis.</p>
<p id="b365-9">A child’s age is far “more than a chronological fact.” <em>Eddings </em>v. <em>Oklahoma, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S. 104, 115</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span> (1982); accord, <em>Gall </em>v. <em>United States, </em><span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/#58" aria-description="Citation for case: Gall v. United States">552 U.S. 38, 58</a></span>, <span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">128 S. Ct. 586</a></span>, <span class="citation" data-id="9435287"><a href="/opinion/145843/gall-v-united-states/" aria-description="Citation for case: Gall v. United States">169 L. Ed. 2d 445</a></span> (2007); <em>Roper </em>v. <em>Simmons, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S. 551, 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span> (2005); <em>Johnson </em>v. <em>Texas, </em><span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/#367" aria-description="Citation for case: Johnson v. Texas">509 U.S. 350, 367</a></span>, <span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/" aria-description="Citation for case: Johnson v. Texas">113 S. Ct. 2658</a></span>, <span class="citation" data-id="9432871"><a href="/opinion/112897/johnson-v-texas/" aria-description="Citation for case: Johnson v. Texas">125 L. Ed. 2d 290</a></span> (1993). It is a fact that “generates commonsense conclusions about behavior and perception.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#674" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 674</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (Breyer, J., dissenting). Such conclusions apply broadly to children as a class. And, they are self-evident to anyone who was a child once himself, including any police officer or judge.</p>
<p id="b365-11">Time and again, this Court has drawn these commonsense conclusions for itself. We have observed that children “generally are less mature and responsible than adults,” <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115-116</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>; that they “often lack the experience, perspective, and judgment to recognize and avoid choices that could be detrimental to them,” <em>Bellotti </em>v. <em>Baird, </em><span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/#635" aria-description="Citation for case: Bellotti v. Baird">443 U.S. 622, 635</a></span>, <span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/" aria-description="Citation for case: Bellotti v. Baird">99 S. Ct. 3035</a></span>, <span class="citation" data-id="9427704"><a href="/opinion/110145/bellotti-v-baird/" aria-description="Citation for case: Bellotti v. Baird">61 L. Ed. 2d 797</a></span> (1979) (plurality opinion); that they “are more vulnerable or susceptible to . . . outside pressures” than adults, <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span>; and so on. See <em>Graham </em>v. <em>Florida, </em><span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/#68" aria-description="Citation for case: Graham v. Florida">560 U.S. 48, 68</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">130 S. Ct. 2011</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">176 L. Ed. 2d 825</a></span> (2010) (finding no reason to “reconsider” these observations about the common “nature of juveniles”). Addressing the specific context of police interrogation, we have observed that events that “would leave a man cold and unimpressed can overawe and overwhelm a lad in his early teens.” <em>Haley </em>v. <em>Ohio, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U.S. 596, 599</a></span>, <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">68 S. Ct. 302</a></span>, <span class="citation no-link">92 L. Ed. 224</span> (1948) (plurality opinion); see also <em>Gallegos </em>v. <em>Colorado, </em><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#54" aria-description="Citation for case: Gallegos v. Colorado">370 U.S. 49, 54</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">82 S. Ct. 1209</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">8 L. Ed. 2d 325</a></span> (1962) <page-number citation-index="1" label="324">*324</page-number>(  “[N]o matter how sophisticated,” a juvenile subject of police interrogation “cannot be compared” to an</p>
<p id="AU2E">[<span class="citation no-link">564 U.S. 273</span>]</p>
<p id="b366-4">adult subject). Describing no one child in particular, these observations restate what “any parent knows”—indeed, what any person knows—about children generally. <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span>.<footnotemark>5</footnotemark></p>
<p id="b366-6">Our various statements to this effect are far from unique. The law has historically reflected the same assumption that children characteristically lack the capacity to exercise mature judgment and possess only an incomplete ability to understand the world around them. See, <em>e.g., </em>1 W. Blackstone, Commentaries on the Laws of England *464-*465 (hereinafter Blackstone) (explaining that limits on children’s legal capacity under the common law “secure them from hurting themselves by their own improvident acts”). Like this Court’s own generalizations, the legal disqualifications placed on children as a <em>class—e.g., </em>limitations on their ability to alienate property, enter a binding contract enforceable against them, and marry without parental consent—exhibit the settled understanding that the differentiating characteristics of youth are universal.<footnotemark>6</footnotemark></p>
<p id="b366-8">[<span class="citation no-link">564 U.S. 274</span>]</p>
<p id="b366-9">Indeed,  even where a “reasonable person” standard otherwise applies, the common law has reflected the reality that children are not adults. In negligence suits, for instance, where liability turns on what an objectively reasonable person would do in the circumstances, “[a]ll American jurisdictions accept the idea that a person’s childhood is a relevant circumstance” to be considered. Restatement (Third) of Torts § 10, Comment <em>b, </em>p. 117 (2005); see also <em>id., </em>Reporters’ Note, pp. 121-122 (collecting cases); Restatement (Second) of Torts § 283A, Comment <em>b, </em>p. 15 (1963-1964) (“[T]here is a wide basis of community experience upon which it is possible, as a practical matter, to determine what is to be expected of [children]”).</p>
<p id="b366-10">As this discussion establishes,  “[o]ur history is replete with laws and judicial recognition” that children cannot be viewed simply as miniature adults. <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115-116</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>. We see no justification for taking a different course here. So long as the child’s age <page-number citation-index="1" label="325">*325</page-number>was known to the officer at the time of the interview, or would have been objectively apparent to any reasonable officer, including age as part of the custody analysis requires officers neither to consider circumstances “unknowable” to them, <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 430</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>, nor to “anticipat[e] the frailties or idiosyncrasies” of the particular suspect whom they question, <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#662" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 662</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span> (internal quotation marks omitted). The same “wide basis of community experience” that makes it possible, as an objective matter, “to determine what is to be expected” of children in other contexts, Restatement (Second) of Torts § 283A, at 15; see <em>supra, </em>at 273, 180 L. Ed. 2d, at 324, and n. 6, likewise makes it possible to know what to expect of children subjected to police questioning.</p>
<p id="b367-4">[<span class="citation no-link">564 U.S. 275</span>]</p>
<p id="b367-5">In other words, a child’s age differs from other personal characteristics that, even when known to police, have no objectively discernible relationship to a reasonable person’s understanding of his freedom of action. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Alvarado</a></span> </em>holds, for instance, that a suspect’s prior interrogation history with law enforcement has no role to play in the custody analysis because such experience could just as easily lead a reasonable person to feel free to walk away as to feel compelled to stay in place. <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. Because the effect in any given case would be “contingent [on the] psycholog [y]” of the individual suspect, the Court explained, such experience cannot be considered without compromising the objective nature of the custody analysis. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Ibid.</a></span> </em>A child’s age, however, is different. Precisely because childhood yields objective conclusions like those we have drawn ourselves— among others, that children are “most susceptible to influence,” <em>Eddings, </em><span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/#115" aria-description="Citation for case: Eddings v. Oklahoma">455 U.S., at 115</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">102 S. Ct. 869</a></span>, <span class="citation" data-id="9428650"><a href="/opinion/110641/eddings-v-oklahoma/" aria-description="Citation for case: Eddings v. Oklahoma">71 L. Ed. 2d 1</a></span>, and “outside pressures,” <em>Roper, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S., at 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, 161 L. Ed. 2d 1—considering age in the custody analysis in no way involves a determination of how youth “subjectively affect[s] the mindset” of any particular child, Brief for Respondent 14.<footnotemark>7</footnotemark></p>
<p id="b367-7">In fact, in many cases involving juvenile suspects, the custody analysis would be nonsensical absent some consideration of the suspect’s age. This case is a prime example. Were the court precluded from taking J. D. B.’s youth into account, it would be forced to evaluate the circumstances present here through the eyes of a reasonable person of average years. In other words, how would a reasonable adult understand his situation, after being removed from a seventh-grade social studies class by a uniformed school resource</p>
<p id="a3j-dedup-0">[<span class="citation no-link">564 U.S. 276</span>]</p>
<p id="b367-8">officer; being encouraged by his assistant principal to “do the right thing”; and being warned by a police investigator of the prospect of juvenile detention and separation from his guardian and primary caretaker? To describe such an inquiry is to demonstrate its absurdity. Neither officers nor courts can reasonably evaluate the effect of objective circumstances that, by their nature, are specific to children with<page-number citation-index="1" label="326">*326</page-number>out accounting for the age of the child subjected to those circumstances.</p>
<p id="b368-4">Indeed, although the dissent suggests that concerns “regarding the application of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody rule to minors can be accommodated by considering the unique circumstances present when minors are questioned in school,” <em>post, </em>at 297, 180 L. Ed. 2d, at 339 (opinion of Alito, J.),  the effect of the schoolhouse setting cannot be disentangled from the identity of the person questioned. A student— whose presence at school is compulsory and whose disobedience at school is cause for disciplinary action—is in a far different position than, say, a parent volunteer on school grounds to chaperone an event, or an adult from the community on school grounds to attend a basketball game. Without asking whether the person “questioned in school” is a “minor,” <em>ibid., </em>the coercive effect of the schoolhouse setting is unknowable.</p>
<p id="b368-5">Our prior decision in <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">Alvarado</a></span> </em>in no way undermines these conclusions. In that case, we held that a state-court decision that failed to mention a 17-year-old’s age as part of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis was not objectively unreasonable under the deferential standard of review set forth by the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>. Like the North Carolina Supreme Court here, see <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#672" aria-description="Citation for case: In re J.D.B.">363 N.C., at 672</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#140" aria-description="Citation for case: In re J.D.B.">686 S.E.2d, at 140</a></span>,  we observed that accounting for a juvenile’s age in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis “could be viewed as creating a subjective inquiry,” <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>. We said nothing, however, of whether such a view would be correct under the law. Cf. <em>Renico </em>v. <em>Lett, </em><span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/#778" aria-description="Citation for case: Renico v. Lett">559 U.S. 766, 778, n. 3</a></span>, <span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/" aria-description="Citation for case: Renico v. Lett">130 S. Ct. 1855</a></span>, <span class="citation" data-id="6680078"><a href="/opinion/6795263/renico-v-lett/" aria-description="Citation for case: Renico v. Lett">176 L. Ed. 2d 678</a></span> (2010) (“[W]hether</p>
<p id="b368-7">[<span class="citation no-link">564 U.S. 277</span>]</p>
<p id="b368-8">the [state court] was right or wrong is not the pertinent question under AEDPA”). To the contrary, Justice O’Connor’s concurring opinion explained that a suspect’s age may indeed “be relevant to the ‘custody’ inquiry.” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#669" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 669</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>.</p>
<p id="b368-9">Reviewing the question <em>de novo </em>today, we hold that  so long as the child’s age was known to the officer at the time of police questioning, or would have been objectively apparent to a reasonable officer, its inclusion in the custody analysis is consistent with the objective nature of that test.<footnotemark>8</footnotemark> This is not to say that a child’s age will be a determinative, or even a significant, factor in every case. Cf. <em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">ibid.</a></span> </em>(O’Connor, J., concurring) (explaining that a state-court decision omitting any mention of the defendant’s age was not unreasonable under AEDPA’s deferential standard of review where the defendant “was almost 18 years old at the time of his <page-number citation-index="1" label="327">*327</page-number>interview”); <em>post, </em>at 296, 180 L. Ed. 2d, at 339 (suggesting that “teenagers nearing the age of majority” are likely to react to an interrogation as would a “typical 18-year-old in similar circumstances”). It is, however, a reality that courts cannot simply ignore.</p>
<p id="b369-4">III</p>
<p id="b369-5">The State and its <em>amici </em>offer numerous reasons that courts must blind themselves to a juvenile defendant’s age. None is persuasive.</p>
<p id="b369-6">[<span class="citation no-link">564 U.S. 278</span>]</p>
<p id="b369-7">To start, the State contends that a child’s age must be excluded from the custody inquiry because age is a personal characteristic specific to the suspect himself rather than an “external” circumstance of the interrogation. Brief for Respondent 21; see also <em>id., </em>at 18-19 (distinguishing “personal characteristics” from “objective facts related to the interrogation itself’ such as the location and duration of the interrogation). Despite the supposed significance of this distinction, however, at oral argument counsel for the State suggested without hesitation that  at least some undeniably personal characteristics—for instance, whether the individual being questioned is blind—are circumstances relevant to the custody analysis. See Tr. of Oral Arg. 41. Thus, the State’s quarrel cannot be that age is a personal characteristic, without more.<footnotemark>9</footnotemark></p>
<p id="b369-8">The State further argues that age is irrelevant to the custody analysis because it “go[es] to how a suspect may internalize and perceive the circumstances of an interrogation.” Brief for Respondent 12; see also Brief for United States as <em>Amicus Curiae </em>21 (hereinafter U. S. Brief) (arguing that a child’s age has no place in the custody analysis because it goes to whether a suspect is “particularly susceptible” to the external circumstances of the interrogation (some internal quotation marks omitted)). But the same can be said of every objective circumstance that the State agrees is relevant to the custody analysis: Each circumstance goes to how a reasonable person would “internalize and perceive” every other. See, <em>e.g., Stansbury, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#325" aria-description="Citation for case: Stansbury v. California">511 U.S., at 325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>. Indeed, this is the very reason that we ask whether the objective circumstances “add up to custody,” <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#113" aria-description="Citation for case: Thompson v. Keohane">516 U.S., at 113</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span>, instead of evaluating the circumstances one by one.</p>
<p id="b369-10">[<span class="citation no-link">564 U.S. 279</span>]</p>
<p id="b369-11">In the same vein, the State and its <em>amici </em>protest that the “effect of... age on [the] perception of custody is internal,” Brief for Respondent 20, or “psychological,” U. S. Brief 21.  But the whole point of the custody analysis is to determine whether, given the circumstances, “a reasonable person [would] have felt he or she was ... at liberty to terminate the interrogation and leave.” <em>Keohane, </em><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/#112" aria-description="Citation for case: Thompson v. Keohane">516 U.S., at 112</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">116 S. Ct. 457</a></span>, <span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">133 L. Ed. 2d 383</a></span>. Because the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody inquiry turns on the mindset of a reasonable person in the suspect’s position, it cannot be the case that a circumstance is subjective simply because it has an “internal” or “psychological” impact on perception. Were that so, <page-number citation-index="1" label="328">*328</page-number>there would be no objective circumstances to consider at all.</p>
<p id="b370-4">Relying on our statements that the objective custody test is “designed to give clear guidance to the police,” <em>Alvarado, </em><span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/#668" aria-description="Citation for case: Yarborough v. Alvarado">541 U.S., at 668</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">124 S. Ct. 2140</a></span>, <span class="citation" data-id="9434617"><a href="/opinion/134748/yarborough-v-alvarado/" aria-description="Citation for case: Yarborough v. Alvarado">158 L. Ed. 2d 938</a></span>, the State next argues that a child’s age must be excluded from the analysis in order to preserve clarity. Similarly, the dissent insists that the clarity of the custody analysis will be destroyed unless a “one-size-fits-all reasonable-person test” applies. <em>Post, </em>at 293, 180 L. Ed. 2d, at 337. In reality, however, ignoring a juvenile defendant’s age will often make the inquiry more artificial, see <em>supra, </em>at 275-276, 180 L. Ed. 2d, at 325-326, and thus only add confusion. And in any event, a child’s age, when known or apparent, is hardly an obscure factor to assess. Though the State and the dissent worry about gradations among children of different ages, that concern cannot justify ignoring a child’s age altogether. Just as police officers are competent to account for other objective circumstances that are a matter of degree such as the length of questioning or the number of officers present, so too are they competent to evaluate the effect of relative age. Indeed, they are competent to do so even though an interrogation room lacks the “reflective atmosphere of a [jury] deliberation room,” <em>post, </em>at 295, 180 L. Ed. 2d, at 338. The same is true of judges, including those whose childhoods have long since passed, see <em>post, </em>at 293, 180 L. Ed. 2d, at 337. In short, officers and judges need no imaginative powers, knowledge of developmental psychology, training in cognitive science, or expertise</p>
<p id="atz-dedup-0">[<span class="citation no-link">564 U.S. 280</span>]</p>
<p id="b370-6">in social and cultural anthropology to account for a child’s age. They simply need the common sense to know that a 7-year-old is not a 13-year-old and neither is an adult.</p>
<p id="b370-8">There is, however, an even more fundamental flaw with the State’s plea for clarity and the dissent’s singular focus on simplifying the analysis:  Not once have we excluded from the custody analysis a circumstance that we determined was relevant and objective, simply to make the fault line between custodial and noncustodial “brighter.” Indeed, were the guiding concern clarity and nothing else, the custody test would presumably ask only whether the suspect had been placed under formal arrest. <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#441" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 441</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>; see <em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">ibid.</a></span> </em>(acknowledging the “occasional!] . . . difficulty” police officers confront in determining when a suspect has been taken into custody). But we have rejected that “more easily administered line,” recognizing that it would simply “enable the police to circumvent the constraints on custodial interrogations established by Miranda.” <em>Ibid.; </em>see also <em>ibid., </em>n. 33.<footnotemark>10</footnotemark></p>
<p id="b370-9">Finally, the State and the dissent suggest that excluding age from the custody analysis comes at no cost to <page-number citation-index="1" label="329">*329</page-number>juveniles’ constitutional rights because the due process voluntariness test independently accounts for a child’s youth. To be sure,  that test permits consideration of a child’s age, and it erects its own barrier to admission of a defendant’s inculpatory statements at trial. See <em>Gallegos, </em><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#53" aria-description="Citation for case: Gallegos v. Colorado">370 U.S., at 53-55</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">82 S. Ct. 1209</a></span>, <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">8 L. Ed. 2d 325</a></span>; <em>Haley, </em><span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U.S., at 599-601</a></span>, <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">68 S. Ct. 302</a></span>, <span class="citation no-link">92 L. Ed. 224</span> (plurality opinion); see also <em>post,</em></p>
<p id="b371-4">[<span class="citation no-link">564 U.S. 281</span>]</p>
<p id="b371-5">at 297, 180 L. Ed. 2d, at 340 (“[C]ourts should be instructed to take particular care to ensure that [young children’s] incriminating statements were not obtained involuntarily”). But <em>Miranda’s </em>procedural safeguards exist precisely because the voluntariness test is an inadequate barrier when custodial interrogation is at stake. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 458</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (“Unless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice”); <em>Dickerson, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#442" aria-description="Citation for case: Dickerson v. United States">530 U.S., at 442</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span> (“[R]eliance on the traditional totality-of-the-circumstances test raise [s] a risk of overlooking an involuntary custodial confession”); see also <em>supra, </em>at 268-270, 180 L. Ed. 2d, at 321-322. To hold, as the State requests, that a child’s age is never relevant to whether a suspect has been taken into custody—and thus to ignore the very real differences between children and adults—would be to deny children the full scope of the procedural safeguards that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>guarantees to adults.</p>
<p id="pA12W">
<img class="p" height="64" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVIAAABAAQAAAABgx8JmAAAAqklEQVR4nO2TPQrCQBCFd0Ow1TKl5gTiDTyVbY6QG2muIxbpXCT6LDLrTOGDNIsIM0349n2zP5CJCEtrqBarIZR2k10kkN2bjQkUvu+j7nWNgbj3jemnAABAOq3xKQIX2Xd13ms7BWkaYOo75H1Dax9MILsHGxMQ97nbaspA3Ok4asygnj+pazRmEOe5eF2Tnksgz0U1mSsyKPWfxT+dY3fdddddd939hfsGZXGCQnMUtgoAAAAASUVORK5CYII=" width="337"/>
</p>
<p id="b371-12">The question remains whether J. D. B. was in custody when police interrogated him. We remand for the state courts to address that question, this time taking account of all of the relevant circumstances of the interrogation, including J. D. B.’s age at the time. The judgment of the North Carolina Supreme Court is reversed, and the case is remanded for proceedings not inconsistent with this opinion.</p>
<p id="b371-13">It is so ordered.</p>
<p id="b371-6">SEPARATE OPINION</p>
<footnote label="1">
<p id="b361-14">. Although the State suggests that the “record is unclear as to who brought J. D. B. to the conference room, and the trial court made no factual findings on this specific point,’’ Brief for Respondent 3, n. 1, the State agreed at the certiorari stage that “the SRO [school resource officer] escorted petitioner’’ to the room, Brief in Opposition 3.</p>
</footnote>
<footnote label="2">
<p id="b362-13">. The North Carolina Supreme Court noted that the trial court’s factual findings were “uncontested and therefore . . . binding’’ on it. <em>In re J. D. B., </em><span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#668" aria-description="Citation for case: In re J.D.B.">363 N.C. 664, 668</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#137" aria-description="Citation for case: In re J.D.B.">686 S.E.2d 135, 137</a></span> (2009). The court described the sequence of events set forth in the text. See <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#670" aria-description="Citation for case: In re J.D.B."><em>id., </em>at 670-671</a></span>, <span class="citation" data-id="6722655"><a href="/opinion/6835533/in-re-jdb/#139" aria-description="Citation for case: In re J.D.B.">686 S.E.2d, at 139</a></span> (“Immediately following J. D. B.’s initial confession, Investigator DiCostanzo informed J. D. B. that he did not have to speak with him and that he was free to leave’’ (internal quotation marks and alterations omitted)). Though less than perfectly explicit, the trial court’s order indicates a finding that J. D. B. initially confessed prior to DiCostanzo’s warnings. See App. 99a.</p>
<p id="Aq_o">Nonetheless, both parties’ submissions to this Court suggest that the warnings came after DiCostanzo raised the possibility of a secure custody order but before J. D. B. confessed for the first time. See Brief for Petitioner 5; Brief for Respondent 5. Because we remand for a determination whether J. D. B. was in custody under the proper analysis, the state courts remain free to revisit whether the trial court made a conclusive finding of fact in this respect.</p>
</footnote>
<footnote label="3">
<p id="b363-13">. J. D. B.’s challenge in the North Carolina Supreme Court focused on the lower courts’ conclusion that he was not in custody for purposes of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (1966). The North Carolina Supreme Court did not address the trial court’s holding that the statements were voluntary, and that question is not before us.</p>
</footnote>
<footnote label="4">
<p id="b364-12">. <em>Amici </em>on behalf of J. D. B. question whether children of all ages can comprehend <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and suggest that additional procedural safeguards may be necessary to protect their <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Brief for Juvenile Law Center et al. 13-14, n. 7. Whatever the merit of that contention, it has no relevance here, where no <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were administered at all.</p>
</footnote>
<footnote label="5">
<p id="b366-11">. Although citation to social science and cognitive science authorities is unnecessary to establish these commonsense propositions, the literature confirms what experience bears out. See, <em>e.g., Graham </em>v. <em>Florida, </em><span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/#68" aria-description="Citation for case: Graham v. Florida">560 U.S. 48, 68</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">130 S. Ct. 2011</a></span>, <span class="citation" data-id="6680682"><a href="/opinion/6795859/graham-v-florida/" aria-description="Citation for case: Graham v. Florida">176 L. Ed. 2d 825</a></span> (2010) (“[D]evelopments in psychology and brain science continue to show fundamental differences between juvenile and adult minds”).</p>
</footnote>
<footnote label="6">
<p id="b366-12">. See, <em>e.g., </em>1 E. Farnsworth, Contracts § 4.4, p. 379, and n. 1 (1990) (“Common law courts early announced the prevailing view that a minor’s contract is ‘voidable’ at the instance of the minor” (citing 8 W. Holdsworth, History of English Law 51 (1926))); 1 D. Kramer, Legal Rights of Children § 8.1, p. 663 (rev. 2d ed. 2005) (“[W]hile minor children have the right to acquire and own property, they are considered incapable of property management” (footnote omitted)); 2 J. Kent, Commentaries on American Law *78-*79, *90 (G. Comstock ed., 11th ed. 1867); see generally <em>id., </em>at *233 (explaining that, under the common law, “[t]he necessity of guardians results from the inability of infants to take care of themselves . . . and this inability continues, in contemplation of law, until the infant has attained the age of [21] ”); 1 Blackstone *465 (“It is generally true, that an infant can neither aliene his lands, nor do any legal act, nor make a deed, nor indeed any manner of contract, that will bind him”); <em>Roper </em>v. <em>Simmons, </em><span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/#569" aria-description="Citation for case: Roper v. Simmons">543 U.S. 551, 569</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">125 S. Ct. 1183</a></span>, <span class="citation" data-id="9434739"><a href="/opinion/137749/roper-v-simmons/" aria-description="Citation for case: Roper v. Simmons">161 L. Ed. 2d 1</a></span> (2005) (“In recognition of the comparative immaturity and irresponsibility of juveniles, almost every State prohibits those under 18 years of age from voting, serving on juries, or marrying without parental consent”).</p>
</footnote>
<footnote label="7">
<p id="b367-10">. Thus, contrary issent’s protestations, today’s holding neither invites consideration of whether a particular suspect is “unusually meek or <em>compliant," post, </em>at 289, 180 L. Ed. 2d, at 335 (opinion of Alito, J.), nor “ ‘expand[s]’ ’’ the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>custody analysis, <em>post, </em>at 289, 180 L. Ed. 2d, at 334, into a test that requires officers to anticipate and account for a suspect’s every personal characteristic, see <em>post, </em>at 291-292, 180 L. Ed. 2d, at 335-336.</p>
</footnote>
<footnote label="8">
<p id="b368-10">.  This approach does not undermine the basic principle that an interrogating officer’s unarticulated, internal thoughts are never—in and of themselves—objective circumstances of an interrogation. See <em>supra, </em>at 270-271, 180 L. Ed. 2d, at 322-323; <em>Stansbury </em>v. <em>California, </em><span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California">511 U.S. 318, 323</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span> (1994) <em>(per curiam). </em>Unlike a child’s youth, an officer’s purely internal thoughts have no conceivable effect on how a reasonable person in the suspect’s position would understand his freedom of action. See <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#323" aria-description="Citation for case: Stansbury v. California"><em>id., </em>at 323-325</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">114 S. Ct. 1526</a></span>, <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">128 L. Ed. 2d 293</a></span>; <em>Berkemer </em>v. <em>McCarty, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U.S. 420, 442</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span> (1984). Rather than “overtur[n]” that settled principle, <em>post, </em>at 293, 180 L. Ed. 2d, at 337, the limitation that a child’s age may inform the custody analysis only when known or knowable simply reflects our unwillingness to require officers to “make guesses’’ as to circumstances “unknowable’’ to them in deciding when to give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, <em>Berkemer, </em><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U.S., at 430-431</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S. Ct. 3138</a></span>, <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L. Ed. 2d 317</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b369-12">. The State’s purported distinction between blindness and age—that taking account of a suspect’s youth requires a court “to get into the mind’’ of the child, whereas taking account of a suspect’s blindness does not, Tr. of Oral Arg. 41-42—is mistaken. In either case, the question becomes how a reasonable person would understand the circumstances, either from the perspective of a blind person or, as here, a 13-year-old child.</p>
</footnote>
<footnote label="10">
<p id="b370-10">. Contrary issent’s intimation, see <em>post, </em>at 288, 180 L. Ed. 2d, at 334,  <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>does not answer the question whether a child’s age is an objective circumstance relevant to the custody analysis. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>simply holds that warnings must be given once a suspect is in custody, without “paus[ing] to inquire in individual cases whether the defendant was aware of his rights without a warning being given.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 468</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 468-469</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (“Assessments of the knowledge the defendant possessed, based on information as to age, education, intelligence, or prior contact with authorities, can never be more than speculation; a warning is a clearcut fact” (footnote omitted)). That conclusion says nothing about whether age properly informs whether a child is in custody in the first place.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Jacobson v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Jacobson v. United States"
type: case
citation: "503 U.S. 540 (1992)"
parallel_cite: "112 S. Ct. 1535; 118 L. Ed. 2d 174"
neutral_cite: 1992 U.S. LEXIS 2117
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1992
date_decided: 1992-04-06
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1992-04-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Jacobson v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112720/jacobson-v-united-states/"
  cluster_id: 112720
  opinion_id: 9432514
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Sorrells v. United States]]", "[[Sherman v. United States]]", "[[Hampton v. United States]]", "[[Mathews v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "inducement", "due-process"]
holding: "Where the government induces the crime, it must prove the defendant was predisposed to commit it INDEPENDENT of, and PRIOR TO, the…"
lake:
  record_id: Jacobson v. United States
  status: verified
  projected_at: 2026-07-06
---

# Jacobson v. United States

*503 U.S. 540 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jacobson lawfully ordered magazines containing images of nude boys before such material became illegal. After the law changed, two government agencies, through a series of fictitious organizations and a pen pal, spent about two and a half years sending him mailings probing and stoking his attitudes about child erotica and decrying censorship. Eventually he ordered a magazine depicting child pornography and was arrested. He raised the entrapment defense.

## Issue
Whether the government proved that Jacobson was predisposed to commit the crime independent of, and prior to, the government's lengthy inducement, as required to defeat an entrapment defense.

## Rule
Where the government induces the crime, it must prove predisposition that predates its own conduct. "Government agents may not originate a criminal design, implant in an innocent person's mind the disposition to commit a criminal act, and then induce commission of the crime so that the Government may prosecute." — 503 U.S. at 548. ^pin-548

"Where the Government has induced an individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents." — *Id.* at 548–549. ^pin-548a

## Application
The only evidence of Jacobson's predisposition arose after the government's two-and-a-half-year campaign of mailings; his earlier, then-legal purchases did not show he was disposed to order illegal child pornography before the government approached him. Because the prosecution failed to prove predisposition independent of, and prior to, that sustained inducement, the government had implanted the disposition it then prosecuted, and the entrapment defense was established as a matter of law.

## Conclusion
The government failed to prove predisposition predating its inducement; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Jacobson* refines the subjective entrapment test of [[Sorrells v. United States]] and [[Sherman v. United States]] by requiring that predisposition exist before the government's first approach.

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Jacobson v. United States*, 503 U.S. 540 (1992) — https://www.courtlistener.com/opinion/112720/jacobson-v-united-states/ — pinpoints: 548, 549.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "455f95803649dd20", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "503 U.S. 540 (1992)", "court": "U.S. Supreme Court", "neutral_cite": "1992 U.S. LEXIS 2117", "official_citation_present": true, "parallel_cite": "112 S. Ct. 1535; 118 L. Ed. 2d 174", "title": "Jacobson v. United States", "year": "1992"}}
{"assertion_id": "609ad7d1a2e04dae", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where the government induces the crime, it must prove the defendant was predisposed to commit it INDEPENDENT of, and PRIOR TO, the…", "title": "Jacobson v. United States"}}
{"assertion_id": "d6ef23d02440cdb1", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key — Progeny / Refinement", "title": "Jacobson v. United States"}}
{"assertion_id": "411bb52f6534bf82", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1992-04-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Jacobson v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Jacobson v. United States", "varies_by_point": "false"}}
{"assertion_id": "5b396c8f3b1a6714", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Jacobson v. United States"}}
```

### lake record — Jacobson v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jacobson v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Jacobson v. United States",
    "case_name_short": "Jacobson",
    "case_name_full": "Jacobson v. United States",
    "input_case_name": "Jacobson v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1992-04-06",
    "year": 1992,
    "docket": null,
    "cluster_id": 112720,
    "lead_opinion_id": 9432514,
    "sibling_ids": [
      112720,
      9432514,
      9432515
    ],
    "absolute_url": "/opinion/112720/jacobson-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "503 U.S. 540",
      "volume": "503",
      "reporter": "U.S.",
      "page": "540",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "112 S. Ct. 1535",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 L. Ed. 2d 174",
        "volume": "118",
        "reporter": "L. Ed. 2d",
        "page": "174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. LEXIS 2117",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "2117",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "503 U.S. 540",
        "volume": "503",
        "reporter": "U.S.",
        "page": "540",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 S. Ct. 1535",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "1535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "118 L. Ed. 2d 174",
        "volume": "118",
        "reporter": "L. Ed. 2d",
        "page": "174",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. LEXIS 2117",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "2117",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "503 U.S. 540",
    "official_selection": {
      "court_class": "scotus",
      "selected": "503 U.S. 540",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-548",
      "page": null,
      "quote": "--- # Jacobson v. United States *503 U.S. 540 (1992)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Jacobson lawfully ordered magazines containing images of nude boys before such material became illegal. After the law changed, two government agencies, through a series of fictitious organizations and a pen pal, spent about two and a half years sending him mailings probing and stoking his attitudes about child erotica and decrying censorship. Eventually he ordered a magazine depicting child pornography and was arrested. He raised the entrapment defense. ## Issue Whether the government proved that Jacobson was predisposed to commit the crime independent of, and prior to, the government's lengthy inducement, as required to defeat an entrapment defense. ## Rule Where the government induces the crime, it must prove predisposition that predates its own conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-548a",
      "page": null,
      "quote": "Where the Government has induced an individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-04-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Jacobson v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Barta",
          "cluster_id": 2774293,
          "cite": [
            "776 F.3d 931",
            "2015 WL 350672",
            "2015 U.S. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Delgado-Marrero",
          "cluster_id": 2652872,
          "cite": [
            "744 F.3d 167",
            "2014 WL 522462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eric Curtin",
          "cluster_id": 798060,
          "cite": [
            "489 F.3d 935",
            "73 Fed. R. Serv. 646",
            "2007 U.S. App. LEXIS 12110",
            "2007 WL 1500295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eduardo Sandoval-Mendoza",
          "cluster_id": 796368,
          "cite": [
            "472 F.3d 645",
            "2006 U.S. App. LEXIS 31815",
            "2006 WL 3783435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 3952337,
          "cite": [
            "808 N.E.2d 488",
            "156 Ohio App. 3d 714",
            "2004 Ohio 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gutierrez",
          "cluster_id": 32172,
          "cite": [
            "343 F.3d 415",
            "2003 U.S. App. LEXIS 16694",
            "2003 WL 21940783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Dodd",
          "cluster_id": 770267,
          "cite": [
            "225 F.3d 340",
            "2000 U.S. App. LEXIS 21423"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Lee Brooks",
          "cluster_id": 769099,
          "cite": [
            "215 F.3d 842",
            "2000 U.S. App. LEXIS 13688",
            "2000 WL 764784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Free Speech Coalition v. Reno",
          "cluster_id": 7079655,
          "cite": [
            "198 F.3d 1083",
            "1999 WL 1206649"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hawkins v. Freeman",
          "cluster_id": 2966971,
          "cite": [
            "166 F.3d 267",
            "1999 WL 21325"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 7058791,
          "cite": [
            "134 F.3d 975",
            "98 Daily Journal DAR 763",
            "98 Cal. Daily Op. Serv. 555",
            "48 Fed. R. Serv. 924",
            "1998 U.S. App. LEXIS 832",
            "1998 WL 19640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vazquez v. State",
          "cluster_id": 1799192,
          "cite": [
            "700 So. 2d 5",
            "1997 WL 361832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne A. Washington",
          "cluster_id": 735397,
          "cite": [
            "106 F.3d 983",
            "323 U.S. App. D.C. 175",
            "46 Fed. R. Serv. 719",
            "1997 U.S. App. LEXIS 3057"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sprouse",
          "cluster_id": 1119600,
          "cite": [
            "983 P.2d 771",
            "1999 Colo. J. C.A.R. 3329",
            "1999 Colo. LEXIS 553",
            "1999 WL 391087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. United States",
          "cluster_id": 145638,
          "cite": [
            "165 L. Ed. 2d 299",
            "126 S. Ct. 2437",
            "548 U.S. 1",
            "2006 U.S. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William D. Davis, United States of America v. Curry James Williams",
          "cluster_id": 679513,
          "cite": [
            "36 F.3d 1424",
            "94 Daily Journal DAR 13648",
            "1994 U.S. App. LEXIS 27168",
            "1994 WL 525969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony N. Matteo v. Superintendent, Sci Albion the District Attorney of the County of Chester the Attorney General of the State of Pennsylvania",
          "cluster_id": 762628,
          "cite": [
            "171 F.3d 877",
            "1999 U.S. App. LEXIS 5163",
            "1999 WL 164152"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gendron",
          "cluster_id": 195225,
          "cite": [
            "18 F.3d 955",
            "1994 WL 50975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brand",
          "cluster_id": 8439509,
          "cite": [
            "467 F.3d 179",
            "71 Fed. R. Serv. 672",
            "2006 U.S. App. LEXIS 25887",
            "2006 WL 2981524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hilario Mendoza-Salgado, United States of America v. Ramon Edwardo Garcia",
          "cluster_id": 583725,
          "cite": [
            "964 F.2d 993",
            "35 Fed. R. Serv. 1029",
            "1992 U.S. App. LEXIS 10413",
            "1992 WL 101352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gifford",
          "cluster_id": 195222,
          "cite": [
            "17 F.3d 462",
            "1994 WL 46738"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Carter",
          "cluster_id": 1795509,
          "cite": [
            "974 So. 2d 181",
            "2008 WL 80764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ram Singh",
          "cluster_id": 696216,
          "cite": [
            "54 F.3d 1182",
            "1995 U.S. App. LEXIS 13496",
            "1995 WL 325249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, Plaintiff-Appellee-Cross-Appellant v. Joe Garza-Juarez and Esteban Garza-Juarez, Defendants-Appellants-Cross-Appellees",
          "cluster_id": 606075,
          "cite": [
            "992 F.2d 896",
            "93 Daily Journal DAR 5160",
            "93 Cal. Daily Op. Serv. 2972",
            "1993 U.S. App. LEXIS 8960"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Al Kassar",
          "cluster_id": 613957,
          "cite": [
            "660 F.3d 108",
            "2011 U.S. App. LEXIS 19357",
            "2011 WL 4375654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wise",
          "cluster_id": 21510,
          "cite": [
            "221 F.3d 140",
            "2000 U.S. App. LEXIS 18282",
            "2000 WL 1041236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Squillacote",
          "cluster_id": 2967273,
          "cite": [
            "221 F.3d 542",
            "2000 WL 1139526"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Jacquez Lamarr, United States of America v. Guy A. Dillard, United States of America v. Maurice L. Mallory, A/K/A Darrell Lee Lawson",
          "cluster_id": 712191,
          "cite": [
            "75 F.3d 964",
            "43 Fed. R. Serv. 1014",
            "1996 U.S. App. LEXIS 2316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brace",
          "cluster_id": 15106,
          "cite": [
            "145 F.3d 247",
            "1998 WL 333453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimenez Recio",
          "cluster_id": 122255,
          "cite": [
            "154 L. Ed. 2d 744",
            "123 S. Ct. 819",
            "537 U.S. 270",
            "2003 U.S. LEXIS 901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stephanie Cannon, Also Known as Stephanie Lynch, United States of America v. Keith Anthony Cannon, United States of America v. Stephanie Cannon, Also Known as Stephanie Lynch, United States of America v. Keith Anthony Cannon",
          "cluster_id": 721470,
          "cite": [
            "88 F.3d 1495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Davis",
          "cluster_id": 662451,
          "cite": [
            "15 F.3d 1393",
            "1994 WL 32296"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Charles Jones",
          "cluster_id": 770998,
          "cite": [
            "231 F.3d 508",
            "2000 Cal. Daily Op. Serv. 8848",
            "2000 Daily Journal DAR 11717",
            "2000 U.S. App. LEXIS 27330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Munoz v. State",
          "cluster_id": 1676101,
          "cite": [
            "629 So. 2d 90",
            "1993 WL 406367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lively",
          "cluster_id": 1119419,
          "cite": [
            "921 P.2d 1035"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jacobson v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112720 OR 9432514 OR 9432515) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MjYyNDMyMDAwMDAmcz03MTQ4MzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112720+OR+9432514+OR+9432515%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(112720 OR 9432514 OR 9432515)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NiZzPTE1MDk1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112720+OR+9432514+OR+9432515%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112720 OR 9432514 OR 9432515)",
        "reviewed": 11,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 11,
        "triage_read": 1,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112720 OR 9432514 OR 9432515)",
    "indexed_citing_opinions": 428,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112720,
        "count": 369,
        "count_source": "search"
      },
      {
        "opinion_id": 9432514,
        "count": 60,
        "count_source": "search"
      },
      {
        "opinion_id": 9432515,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 691,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/jacobson-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwMTMzOTEmcz00ODA2NDMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112720+OR+9432514+OR+9432515%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112720,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 107685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 108839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 109939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 110794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 112012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 112417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 230738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 342581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 416501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 417704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 445246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 527667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 549820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112720,
        "cited_id": 556376,
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
    "date_created": "2026-07-05T08:46:20Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:52:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:46:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Jacobson v. United States

```
<opinion type="majority">
<author id="ArMK"><page-number citation-index="1" label="542">*542</page-number>Justice White</author>
<p id="Anh">delivered the opinion of the Court.</p>
<p id="AzeW">On September 24, 1987, petitioner Keith Jacobson was indicted for violating a provision of the Child Protection Act of 1984 (Act), <span class="citation no-link">Pub. L. 98-292, 98</span> Stat. 204, which criminalizes the knowing receipt through the mails of a “visual depiction [that] involves the use of a minor engaging in sexually explicit conduct. . . .” <span class="citation no-link">18 U. S. C. § 2252</span>(a)(2)(A). Petitioner defended on the ground that the Government entrapped him into committing the crime through a series of communications from undercover agents that spanned the 26 months preceding his arrest. Petitioner was found guilty after a jury trial. The Court of Appeals affirmed his conviction, holding that the Government had carried its burden of proving beyond reasonable doubt that petitioner was predisposed to break the law and hence was not entrapped.</p>
<p id="Ayo">Because the Government overstepped the line between setting a trap for the “unwary innocent” and the “unwary criminal,” <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S. 369, 372</a></span> (1958), and as a matter of law failed to establish that petitioner was independently predisposed to commit the crime for which he was arrested, we reverse the Court of Appeals’ judgment affirming his conviction.</p>
<p id="AqC">I</p>
<p id="A7S5">In February 1984, petitioner, a 56-year-old veteran-turned-farmer who supported his elderly father in Nebraska, ordered two magazines and a brochure from a California adult bookstore. The magazines, entitled Bare Boys I and Bare Boys II, contained photographs of nude preteen and <page-number citation-index="1" label="543">*543</page-number>teenage boys. The contents of the magazines startled petitioner, who testified that he had expected to receive photographs of “young men 18 years or older.” Tr. 425. On cross-examination, he explained his response to the magazines:</p>
<blockquote id="b599-4">“[PROSECUTOR]: [Y]ou were shocked and surprised that there were pictures of very young boys without clothes on, is that correct?</blockquote>
<blockquote id="b599-5">“[JACOBSON]: Yes, I was.</blockquote>
<blockquote id="b599-6">“[PROSECUTOR]: Were you offended?</blockquote>
<blockquote id="b599-7">“[JACOBSON]: I was not offended because I thought these were a nudist type publication. Many of the pictures were out in a rural or outdoor setting. There was — I didn’t draw any sexual connotation or connection with that.” <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#463" aria-description="Citation for case: Sherman v. United States"><em>Id., </em>at 463</a></span>.</blockquote>
<p id="b599-8">The young men depicted in the magazines were not engaged in sexual activity, and petitioner’s receipt of the magazines was legal under both federal and Nebraska law. Within three months, the law with respect to child pornography changed; Congress passed the Act illegalizing the receipt through the mails of sexually explicit depictions of children. In the very month that the new provision became law, postal inspectors found petitioner’s name on the mailing list of the California bookstore that had mailed him Bare Boys I and II. There followed over the next 2V2 years repeated efforts by two Government agencies, through five fictitious organizations and a bogus pen pal, to explore petitioner’s willingness to break the new law by ordering sexually explicit photographs of children through the mail.</p>
<p id="b599-9">The Government began its efforts in January 1985 when a postal inspector sent petitioner a letter supposedly from the American Hedonist Society, which in fact was a fictitious organization. The letter included a membership application and stated the Society’s doctrine: that members had the <page-number citation-index="1" label="544">*544</page-number>“right to read what we desire, the right to discuss similar interests with those who share our philosophy, and finally that we have the right to seek pleasure without restrictions being placed on us by outdated puritan morality.” Record, Government Exhibit 7. Petitioner enrolled in the organization and returned a sexual attitude questionnaire that asked him to rank on a scale of one to four his enjoyment of various sexual materials, with one being “really enjoy,” two being “enjoy,” three being “somewhat enjoy,” and four being “do not enjoy.” Petitioner ranked the entry “[p]re-teen sex” as a two, but indicated that he was opposed to pedophilia. <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span></em></p>
<p id="b600-5">For a time, the Government left petitioner alone. But then a new “prohibited mailing specialist” in the Postal Service found petitioner’s name in a file, Tr. 328-331, and in May 1986, petitioner received a solicitation from a second fictitious consumer research company, “Midlands ■ Data Research,” seeking a response from those who “believe in the joys of sex and the complete awareness of those lusty and youthful lads and lasses of the neophite <em>[sic] </em>age.” Record, Government Exhibit 8. The letter never explained whether “neophite” referred to minors or young adults. Petitioner responded: “Please feel free to send me more information, I am interested in teenage sexuality. Please keep my name confidential.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span></em></p>
<p id="b600-6">Petitioner then heard from yet another Government creation, “Heartland Institute for a New Tomorrow” (HINT), which proclaimed that it was “an organization founded to protect and promote sexual freedom and freedom of choice. We believe that arbitrarily imposed legislative sanctions restricting <em>your </em>sexual freedom should be rescinded through the legislative process.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Defendant’s Exhibit 102. The letter also enclosed a second survey. Petitioner indicated that his interest in “[pjreteen sex-homosexual” material was above average, but not high. In response to another question, petitioner wrote: “Not only sexual expression but freedom of the press is under attack. We must be ever vigilant <page-number citation-index="1" label="545">*545</page-number>to counter attack right wing fundamentalists who are determined to curtail our freedoms.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 9.</p>
<p id="b601-5">HINT replied, portraying itself as a lobbying organization seeking to repeal “all statutes which regulate sexual activities, except those laws which deal with violent behavior, such as rape. HINT is also lobbying to eliminate any legal definition of ‘the age of consent.’ ” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Defendant’s Exhibit 113. These lobbying efforts were to be funded by sales from a catalog to be published in the future “offering the sale of various items which we believe you will find to be both interesting and stimulating.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Ibid.</a></span> </em>HINT also provided computer matching of group members with similar survey responses; and, although petitioner was supplied with a list of potential “pen pals,” he did not initiate any correspondence.</p>
<p id="b601-6">Nevertheless, the Government’s “prohibited mailing specialist” began writing to petitioner, using the pseudonym “Carl Long.” The letters employed a tactic known as “mirroring,” which the inspector described as “reflect[ing] whatever the interests are of the person we are writing to.” Tr. 342. Petitioner responded at first, indicating that his interest was primarily in “male-male items.” Record, Government Exhibit 9A. Inspector “Long” wrote back:</p>
<blockquote id="b601-7">“My interests too are primarily male-male items. Are you satisfied with the type of VCR tapes available? Personally, I like the amateur stuff better if its <em>[sic] </em>well produced as it can get more kinky and also seems more real. I think the actors enjoy it more.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 13.</blockquote>
<p id="b601-8">Petitioner responded:</p>
<blockquote id="b601-9">“As far as my likes are concerned, I like good looking young guys (in their late teens and early 20’s) doing their thing together.” <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Id.,</a></span> </em>Government Exhibit 14.</blockquote>
<p id="b601-10">Petitioner’s letters to “Long” made no reference to child pornography. After writing two letters, petitioner discontinued the correspondence.</p>
<p id="b602-4"><page-number citation-index="1" label="546">*546</page-number>By March 1987, 34 months had passed since the Government obtained petitioner’s name from the mailing list of the California bookstore, and 26 months had passed since the Postal Service had commenced its mailings to petitioner. Although petitioner had responded to surveys and letters, the Government had no evidence that petitioner had ever intentionally possessed or been exposed to child pornography. The Postal Service had not checked petitioner’s mail to determine whether he was receiving questionable mailings from persons — other than the Government — involved in the child pornography industry. Tr. 348.</p>
<p id="b602-5">At this point, a second Government agency, the Customs Service, included petitioner in its own child pornography sting, “Operation Borderline,” after receiving his name on lists submitted by the Postal Service. <em>Id., </em>at 71-72. Using the name of a fictitious Canadian company called “Produit Outaouais,” the Customs Service mailed petitioner a brochure advertising photographs of young boys engaging in sex. Record, Government Exhibit 22. Petitioner placed an order that was never filled. <em>Id., </em>Government Exhibit 24.</p>
<p id="b602-6">The Postal Service also continued its efforts in the Jacobson case, writing to petitioner as the “Far Eastern Trading Company Ltd.” The letter began:</p>
<blockquote id="b602-7">“As many of you know, much hysterical nonsense has appeared in the American media concerning ‘pornography’ and what must be done to stop it from coming across your borders. This brief letter does not allow us to give much comments; however, why is your government spending millions of dollars to exercise international censorship while tons of drugs, which makes yours the world’s most crime ridden country are passed through easily.” <em>Id., </em>Government Exhibit 1.</blockquote>
<p id="b602-8">The letter went on to say:</p>
<blockquote id="b602-9">“[W]e have devised a method of getting these to you without prying eyes of U. S. Customs seizing your <page-number citation-index="1" label="547">*547</page-number>mail. . . . After consultations with American solicitors, we have been advised that once we have posted our material through your system, it cannot be opened for any inspection without authorization of a judge.” <em>Ibid.</em></blockquote>
<p id="b603-5">The letter invited petitioner to send for more information. It also asked petitioner to sign an affirmation that he was “not a law enforcement officer or agent of the U. S. Government acting in an undercover capacity for the purpose of entrapping Far Eastern Trading Company, its agents or customers.” Petitioner responded. <em>Ibid. </em>A catalog was sent, <em>id., </em>Government Exhibit 2, and petitioner ordered Boys Who Love Boys, <em>id., </em>Government Exhibit 3, a pornographic magazine depicting young boys engaged in various sexual activities. Petitioner was arrested after a controlled delivery of a photocopy of the magazine.</p>
<p id="b603-6">When petitioner was asked at trial why he placed such an order, he explained that the Government had succeeded in piquing his curiosity:</p>
<blockquote id="b603-7">“Well, the statement was made of all the trouble and the hysteria over pornography and I wanted to see what the material was. It didn’t describe the — I didn’t know for sure what kind of sexual action they were referring to in the Canadian letter.” Tr. 427-428.</blockquote>
<p id="b603-8">In petitioner’s home, the Government found the Bare Boys magazines and materials that the Government had sent to him in the course of its protracted investigation, but no other materials that would indicate that petitioner collected, or was actively interested in, child pornography.</p>
<p id="b603-9">Petitioner was indicted for violating <span class="citation no-link">18 U. S. C. § 2252</span>(a) (2)(A). The trial court instructed the jury on the petitioner’s entrapment defense,<footnotemark>1</footnotemark> petitioner was convicted, and a di<page-number citation-index="1" label="548">*548</page-number>vided Court of Appeals for the Eighth Circuit, sitting en banc, affirmed, concluding that “Jacobson was not entrapped as a matter of law.” <span class="citation" data-id="9480896"><a href="/opinion/549820/united-states-v-keith-m-jacobson/#470" aria-description="Citation for case: United States v. Keith M. Jacobson">916 F. 2d 467, 470</a></span> (1990). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./499/974/">499 U. S. 974</a></span> (1991).</p>
<p id="b604-3">II</p>
<p id="ArF">There can be no dispute about the evils of child pornography or the difficulties that laws and law enforcement have encountered in eliminating it. See generally <em>Osborne </em>v. <em>Ohio, </em><span class="citation" data-id="9431982"><a href="/opinion/112417/osborne-v-ohio/#110" aria-description="Citation for case: Osborne v. Ohio">495 U. S. 103, 110</a></span> (1990); <em>New York </em>v. <em>Ferber, </em><span class="citation" data-id="9428936"><a href="/opinion/110794/new-york-v-ferber/#759" aria-description="Citation for case: New York v. Ferber">458 U. S. 747, 759-760</a></span> (1982). Likewise, there can be no dispute that the Government may use undercover agents to enforce the law. “It is well settled that the fact that officers or employees of the Government merely afford opportunities or facilities for the commission of the offense does not defeat the prosecution. Artifice and stratagem may be employed to catch those engaged in criminal enterprises.” <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 441</a></span> (1932); <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>; <em>United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 435-436</a></span> (1973).</p>
<p id="b604-4">In their zeal to enforce the law, however, Government agents may not originate a criminal design, implant in an innocent person’s mind the disposition to commit a criminal act, and then induce commission of the crime so that the Government may prosecute. <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>; <span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States"><em>Sherman, supra, </em>at 372</a></span>. Where the Government has induced an <page-number citation-index="1" label="549">*549</page-number>individual to break the law and the defense of entrapment is at issue, as it was in this case, the prosecution must prove beyond reasonable doubt that the defendant was disposed to commit the criminal act prior to first being approached by Government agents. <em>United States </em>v. <em>Whole, </em>288 U. S. App. D. C. 261, 263-264, <span class="citation" data-id="556376"><a href="/opinion/556376/united-states-v-donald-whoie/#1483" aria-description="Citation for case: United States v. Donald Whoie">925 F. 2d 1481, 1483-1484</a></span> (1991).<footnotemark>2</footnotemark></p>
<p id="b605-5">Thus, an agent deployed to stop the traffic in illegal drugs may offer the opportunity to buy or sell drugs and, if the offer is accepted, make an arrest on the spot or later. In <page-number citation-index="1" label="550">*550</page-number>such a typical case, or in a more elaborate “sting” operation involving government-sponsored fencing where the defendant is simply provided with the opportunity to commit a crime, the entrapment defense is of little use because the ready commission of the criminal act amply demonstrates the defendant’s predisposition. See <em>United States </em>v. <em>Sherman, </em><span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/#882" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880, 882</a></span> (CA2 1952). Had the agents in this case simply offered petitioner the opportunity to order child pornography through the mails, and petitioner — who must be presumed to know the law — had promptly availed himself of this criminal opportunity, it is unlikely that his entrapment defense would have warranted a jury instruction. <em>Mathews </em>v. <em>United States, </em><span class="citation" data-id="9431220"><a href="/opinion/112012/mathews-v-united-states/#66" aria-description="Citation for case: Mathews v. United States">485 U. S. 58, 66</a></span> (1988).</p>
<p id="b606-5">But that is not what happened here. By the time petitioner finally placed his order, he had already been the target of 26 months of repeated mailings and communications from Government agents and fictitious organizations. Therefore, although he had become predisposed to break the law by May 1987, it is our view that the Government did not prove that this predisposition was independent and not the product of the attention that the Government had directed at petitioner since January 1985. <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>; <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#372" aria-description="Citation for case: Sherman v. United States">356 U. S., at 372</a></span>.</p>
<p id="b606-6">The prosecution’s evidence of predisposition falls into two categories: evidence developed prior to the Postal Service’s mail campaign, and that developed during the course of the investigation. The sole piece of preinvestigation evidence is petitioner’s 1984 order and receipt of the Bare Boys magazines. But this is scant if any proof of petitioner’s predisposition to commit an illegal act, the criminal character of which a defendant is presumed to know. It may indicate a predisposition to view sexually oriented photographs that are responsive to his sexual tastes; but evidence that merely indicates a generic inclination to act within a broad range, not all of which is criminal, is of little probative value in establishing predisposition.</p>
<p id="b607-4"><page-number citation-index="1" label="551">*551</page-number>Furthermore, petitioner was acting within the law at the time he received these magazines. Receipt through the mails of sexually explicit depictions of children for noncommercial use did not become illegal under federal law until May 1984, and Nebraska had no law that forbade petitioner’s possession of such material until 1988. <span class="citation no-link">Neb. Rev. Stat. § 28-813.01</span> (1989). Evidence of predisposition to do what once was lawful is not, by itself, sufficient to show predisposition to do what is now illegal, for there is a common understanding that most people obey the law even when they disapprove of it. This obedience may reflect a generalized respect for legality or the fear of prosecution, but for whatever reason, the law’s prohibitions are matters of consequence. Hence, the fact that petitioner legally ordered and received the Bare Boys magazines does little to further the Government’s burden of proving that petitioner was predisposed to commit a criminal act. This is particularly true given petitioner’s unchallenged testimony that he did not know until they arrived that the magazines would depict minors.</p>
<p id="b607-5">The prosecution’s evidence gathered during the investigation also fails to carry the ■ Government’s burden. Petitioner’s responses to the many communications prior to the ultimate criminal act were at most indicative of certain personal inclinations, including a predisposition to view photographs of preteen sex and a willingness to promote a given agenda by supporting lobbying organizations. Even so, petitioner’s responses hardly support an inference that he would commit the crime of receiving child pornography through the mails.<footnotemark>3</footnotemark> Furthermore, a person’s inclinations and “fantasies . . . are <page-number citation-index="1" label="552">*552</page-number>his own and beyond the reach of government. . . <em>Paris Adult Theatre I </em>v. <em>Slaton, </em><span class="citation" data-id="9425382"><a href="/opinion/108839/paris-adult-theatre-i-v-slaton/#67" aria-description="Citation for case: Paris Adult Theatre I v. Slaton">413 U. S. 49, 67</a></span> (1973); <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#565" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 565-566</a></span> (1969).</p>
<p id="b608-5">On the other hand, the strong arguable inference is that, by waving the banner of individual rights and disparaging the legitimacy and constitutionality of efforts to restrict the availability of sexually explicit materials, the Government not only excited petitioner’s interest in sexually explicit materials banned by law but also exerted substantial pressure on petitioner to obtain and read such material as part of a fight against censorship and the infringement of individual rights. For instance, HINT described itself as “an organization founded to protect and promote sexual freedom and freedom of choice” and stated that “the most appropriate means to accomplish [its] objectives is to promote honest dialogue among concerned individuals and to continue its lobbying efforts with State Legislators.” Record, Defendant’s Exhibit 113. These lobbying efforts were to be financed through catalog sales. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Ibid.</a></span> </em>Mailings from the equally fictitious American Hedonist Society, <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">id.,</a></span> </em>Government Exhibit 7, and the correspondence from the nonexistent Carl Long, <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">id.,</a></span> </em>Defendant’s Exhibit 5, endorsed these themes.</p>
<p id="b608-6">Similarly, the two solicitations in the spring of 1987 raised the spectre of censorship while suggesting that petitioner ought to be allowed to do what he had been solicited to do. The mailing from the Customs Service referred to “the worldwide ban and intense enforcement on this type of material,” observed that “what was legal and commonplace is now an ‘underground’ and secretive service,” and emphasized that “[t]his environment forces us to take extreme measures” to ensure delivery. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Id.,</a></span> </em>Government Exhibit 22. The Postal Service solicitation described the concern about child pornography as “hysterical nonsense,” decried “international censorship,” and assured petitioner, based on consultation with “American solicitors,” that an order that had been posted could not be opened for inspection without au<page-number citation-index="1" label="553">*553</page-number>thorization of a judge. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Id.,</a></span> </em>Government Exhibit 1. It further asked petitioner to affirm that he was not a Government agent attempting to entrap the mail order company or its customers. <em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">Ibid.</a></span> </em>In these particulars, both Government solicitations suggested that receiving this material was something that petitioner ought to be allowed to do.</p>
<p id="b609-5">Petitioner’s ready response to these solicitations cannot be enough to establish beyond reasonable doubt that he was predisposed, prior to the Government acts intended to create predisposition, to commit the crime of receiving child pornography through the mails. See <em>Sherman, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/#374" aria-description="Citation for case: Sherman v. United States">356 U. S., at 374</a></span>. The evidence that petitioner was ready and willing to commit the offense came only after the Government had devoted 2V2 years to convincing him that he had or should have the right to engage in the very behavior proscribed by law. Rational jurors could not say beyond a reasonable doubt that petitioner possessed the requisite predisposition prior to the Government’s investigation and that it existed independent of the Government’s many and varied approaches to petitioner. As was explained in <em>Sherman, </em>where entrapment was found as a matter of law, “the Government [may not] pla[y] on the weaknesses of an innocent party and beguil[e] him into committing crimes which he otherwise would not have attempted.” <em>Id., </em>at 376.</p>
<p id="b609-6">Law enforcement officials go too far when they “implant in the mind of an innocent person the <em>disposition </em>to commit the alleged offense and induce its commission in order that they may prosecute.” <em>Sorrells, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 442</a></span> (emphasis added). Like the <em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span> </em>Court, we are “unable to conclude that it was the intention of the Congress in enacting this statute that its processes of detection and enforcement should be abused by the instigation by government officials of an act on the part of persons otherwise innocent in order to lure them to its commission and to punish them.” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#448" aria-description="Citation for case: Sorrells v. United States"><em>Id., </em>at 448</a></span>. When the Government’s quest for convictions leads to the apprehension of an otherwise law-abiding citizen who, if <page-number citation-index="1" label="554">*554</page-number>left to his own devices, likely would have never run afoul of the law, the courts should intervene.</p>
<p id="b610-5">Because we conclude that this is such a case and that the prosecution failed, as a matter of law, to adduce evidence to support the jury verdict that petitioner was predisposed, independent of the Government’s acts and beyond a reasonable doubt, to violate the law by receiving child pornography through the mails, we reverse the Court of Appeals’ judgment affirming the conviction of Keith Jacobson.</p>
<p id="b610-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b603-10"> The jury was instructed:</p>
<blockquote id="b603-11">“As mentioned, one of the issues in this case is whether the defendant was entrapped. If the defendant was entrapped he must be found not <page-number citation-index="1" label="548">*548</page-number>guilty. The government has the burden of proving beyond a reasonable doubt that the defendant was not entrapped.</blockquote>
<blockquote id="b604-6">“If the defendant before contact with law-enforcement officers or their agents did not have any intent or disposition to commit the crime charged and was induced or persuaded by law-enforcement officers o[r] their agents to commit that crime, then he was entrapped. On the other hand, if the defendant before contact with law-enforcement officers or their agents did have an intent or disposition to commit the crime; charged, then he was not entrapped even though law-enforcement officers or their agents provided a favorable opportunity to commit the crime or made committing the crime easier or even participated in acts essential to the crime.” App. 11-12.</blockquote>
</footnote>
<footnote label="2">
<p id="b605-6"> Inducement is not at issue in this case. The Government does not dispute that it induced petitioner to commit the crime. The sole issue is whether the Government carried its burden of proving that petitioner was predisposed to violate the law <em>before </em>the Government intervened. The dissent is mistaken in claiming that this is an innovation in entrapment law and in suggesting that the Government’s conduct prior to the moment of solicitation is irrelevant. See <em>post, </em>at 556-557. The Court rejected these arguments six decades ago in <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932), when the Court wrote that the Government may not punish an individual “for an alleged offense which is the product of the creative activity of its own officials” and that in such a case the Government “is in no position to object to evidence of the activities of its representatives in relation to the accused . . . .” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#451" aria-description="Citation for case: Sorrells v. United States"><em>Id., </em>at 451</a></span>. Indeed, the proposition that the accused must be predisposed prior to contact with law enforcement officers is so firmly established that the Government conceded the point at oral argument, submitting that the evidence it developed during the course of its investigation was probative because it indicated petitioner’s state of mind <em>prior </em>to the commencement of the Government’s investigation. See Tr. of Oral Arg. 41, 49.</p>
<p id="b605-7">This long-established standard in no way encroaches upon Government investigatory activities. Indeed, the Government’s internal guidelines for undercover operations provide that an inducement to commit a crime should not be offered unless:</p>
<blockquote id="b605-8">“(a) [Tjhere is a reasonable indication, based on information developed through informants or other means, that the subject is engaging, has engaged, or is likely to engage in illegal activity of a similar type; <em>or</em></blockquote>
<blockquote id="b605-9">“(b) The opportunity for illegal activity has been structured so that there is reason for believing that-persons drawn to the opportunity, or brought to it, are predisposed to engage in the contemplated illegal activity.” Attorney General’s Guidelines on FBI Undercover Operations (Dec. 31,1980), reprinted in S. Rep. No. 97-682, p. 551 (1982).-</blockquote>
</footnote>
<footnote label="3">
<p id="b607-6"> We do not hold, as the dissent suggests, see <em>post, </em>at 559-560, that the Government was required to prove that petitioner knowingly violated the law. We simply conclude that proof that petitioner engaged in legal conduct and possessed certain generalized personal inclinations is not sufficient evidence to prove beyond a reasonable doubt that he would have been predisposed to commit the crime charged independent of the Government’s coaxing.</p>
</footnote>
</opinion>
```

---
