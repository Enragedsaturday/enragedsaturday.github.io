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

## GROUP: _overhaul2/lake/cases/Fellers v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Fellers v. United States"
type: case
citation: "540 U.S. 519 (2004)"
parallel_cite: "124 S. Ct. 1019; 157 L. Ed. 2d 1016"
neutral_cite: 2004 U.S. LEXIS 825
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-01-26
docket: 02-6320
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Fellers v. United States
  varies_by_point: false
  scope_note: "Good law; unanimous. Remanded on the fruits question (whether Elstad's Fifth Amendment analysis governs a Sixth Amendment violation)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131158/fellers-v-united-states/"
  cluster_id: 131158
  opinion_id: 131158
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny"
related: ["[[Massiah v. United States]]", "[[Brewer v. Williams]]", "[[Oregon v. Elstad]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "massiah", "deliberate-elicitation"]
holding: "After indictment, officers who deliberately elicit incriminating statements from a defendant outside the presence of counsel and without a waiver violate the Sixth Amendment under Massiah — and the Sixth Amendment standard is deliberate elicitation, not Miranda 'interrogation,' so the absence of interrogation does not defeat the claim."
lake:
  record_id: Fellers v. United States
  status: verified
  projected_at: 2026-07-06
---

# Fellers v. United States

*540 U.S. 519 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a grand jury indicted Fellers, officers went to his home to arrest him and told him they were there to discuss his involvement in methamphetamine distribution and his charged co-conspirators. Fellers made inculpatory statements at home, without [[Miranda and Custodial Interrogation|Miranda warnings]] and without counsel. He was then taken to jail, given [[Miranda and Custodial Interrogation|Miranda warnings]], waived, and repeated the admissions. The Eighth Circuit held there was no Sixth Amendment problem because the officers "did not interrogate" him at home.

## Issue
Whether the Sixth Amendment is violated when, after indictment, officers deliberately elicit incriminating statements from a defendant outside counsel's presence even though there was no Miranda-style "interrogation."

## Rule
Yes — the Sixth Amendment standard is *deliberate elicitation*, not interrogation. Under *[[Massiah v. United States|Massiah]]*, an accused is denied the Sixth Amendment's protection when the government uses against him "evidence of his own incriminating words, which federal agents ... deliberately elicited from him after he had been indicted and in the absence of his counsel." — *[[Massiah v. United States]]*, 377 U.S. at 206 (quoted).

"We have consistently applied the deliberate-elicitation standard in subsequent Sixth Amendment cases ... and we have expressly distinguished this standard from the Fifth Amendment custodial-interrogation standard." — 540 U.S. at 524. ^pin-524

Because the deliberate-elicitation test does not require an "interrogation," the absence of interrogation does not defeat a Sixth Amendment claim.

## Application
"[T]here is no question that the officers in this case 'deliberately elicited' information from petitioner" — they came to his home specifically to discuss the charged conduct. Because that discussion occurred after indictment, outside counsel's presence, and without a waiver, the officers violated Fellers's Sixth Amendment rights, and the Eighth Circuit erred in treating the lack of interrogation as fatal. The Court did not itself decide whether the later jailhouse statements had to be suppressed as fruits; it [[Reading and Citing Cases#on-remand|remanded]] that Sixth Amendment fruits question (including whether *[[Oregon v. Elstad]]*'s Fifth Amendment analysis applies) to the Court of Appeals.

## Conclusion
The home statements were obtained in violation of the Sixth Amendment (deliberate elicitation post-indictment). The Eighth Circuit was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to address suppression of the jailhouse statements under the Sixth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Fellers* reaffirms the [[Massiah v. United States]] / [[Brewer v. Williams]] deliberate-elicitation line and keeps the Sixth Amendment analysis separate from *[[Miranda v. Arizona|Miranda]]* custody/interrogation; the open fruits question turns on [[Oregon v. Elstad]].

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny*

## Sources
- *Fellers v. United States*, 540 U.S. 519 (2004) — https://www.courtlistener.com/opinion/131158/fellers-v-united-states/ — pinpoint: 524 (quoting *Massiah*, 377 U.S. at 206).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a93f5ef5a1727513", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Fellers v. United States"}, "payload": {"all": [{"cite": "540 U.S. 519", "page": "519", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 1019", "page": "1019", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 1016", "page": "1016", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2004 U.S. LEXIS 825", "page": "825", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "540 U.S. 519", "official": {"cite": "540 U.S. 519", "page": "519", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "540"}, "official_selection_present": true, "record_id": "Fellers v. United States"}}
{"assertion_id": "17e1f0179fb02e26", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-524", "record_id": "Fellers v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-524", "pinpoint_status": "slip-only", "quote": "— *Massiah v. United States*, 377 U.S. at 206 (quoted).", "quote_fidelity": "mismatch", "record_id": "Fellers v. United States", "star_marker": null}}
{"assertion_id": "d5e570bf34afd6d3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Fellers v. United States"}, "payload": {"as_of_content": "2004-01-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Fellers v. United States", "scope_note": "Good law; unanimous. Remanded on the fruits question (whether Elstad's Fifth Amendment analysis governs a Sixth Amendment violation).", "varies_by_point": false}}
```

### lake record — Fellers v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Fellers v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Fellers v. United States",
    "case_name_short": "Fellers",
    "case_name_full": "Fellers v. United States",
    "input_case_name": "Fellers v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-01-26",
    "year": 2004,
    "docket": "02-6320",
    "cluster_id": 131158,
    "lead_opinion_id": 131158,
    "sibling_ids": [
      131158
    ],
    "absolute_url": "/opinion/131158/fellers-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "540 U.S. 519",
      "volume": "540",
      "reporter": "U.S.",
      "page": "519",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 1019",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1019",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1016",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1016",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 825",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "825",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 519",
        "volume": "540",
        "reporter": "U.S.",
        "page": "519",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1019",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1019",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1016",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1016",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 825",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "825",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "540 U.S. 519",
    "official_selection": {
      "court_class": "scotus",
      "selected": "540 U.S. 519",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-524",
      "page": null,
      "quote": "\u2014 *Massiah v. United States*, 377 U.S. at 206 (quoted).",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Fellers v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; unanimous. Remanded on the fruits question (whether Elstad's Fifth Amendment analysis governs a Sixth Amendment violation).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Fellers v. United States:lane1_negative"
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
        "journal_ref": "Fellers v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arabzadegan v. State",
          "cluster_id": 2166816,
          "cite": [
            "240 S.W.3d 44",
            "2007 WL 2066225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samuel Constanza Alvarado",
          "cluster_id": 793566,
          "cite": [
            "440 F.3d 191",
            "2006 U.S. App. LEXIS 6055",
            "2006 WL 598152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Briggs",
          "cluster_id": 2550075,
          "cite": [
            "12 A.3d 291",
            "608 Pa. 430",
            "2011 Pa. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
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
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ball",
          "cluster_id": 1742701,
          "cite": [
            "710 N.W.2d 592",
            "271 Neb. 140",
            "2006 Neb. LEXIS 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald A. Lehn v. Michael L. Holmes",
          "cluster_id": 785803,
          "cite": [
            "364 F.3d 862",
            "2004 U.S. App. LEXIS 7206",
            "2004 WL 787246"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rommy",
          "cluster_id": 2667,
          "cite": [
            "506 F.3d 108",
            "39 A.L.R. Fed. 2d 703",
            "2007 U.S. App. LEXIS 25732",
            "2007 WL 3243813"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaczmarek v. State",
          "cluster_id": 2508848,
          "cite": [
            "91 P.3d 16",
            "120 Nev. 314",
            "120 Nev. Adv. Rep. 37",
            "2004 Nev. LEXIS 42"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lopez",
          "cluster_id": 5640849,
          "cite": [
            "16 N.Y.3d 375",
            "947 N.E.2d 1155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. US Infrastructure, Inc.",
          "cluster_id": 78412,
          "cite": [
            "576 F.3d 1195",
            "2009 WL 2242622"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willis Randolph v. People of the State of California Attorney General of the State of California James Hamlet, Warden",
          "cluster_id": 787477,
          "cite": [
            "380 F.3d 1133",
            "2004 U.S. App. LEXIS 17470",
            "2004 WL 1852899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hornsby",
          "cluster_id": 621509,
          "cite": [
            "666 F.3d 296",
            "2012 WL 207065",
            "2012 U.S. App. LEXIS 1333"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles E. Sweeney, Jr. v. Steve Carter, Attorney General of Indiana",
          "cluster_id": 785430,
          "cite": [
            "361 F.3d 327"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cyril S. Plumman, Also Known as Steve Plumman",
          "cluster_id": 790451,
          "cite": [
            "409 F.3d 919",
            "67 Fed. R. Serv. 451",
            "2005 U.S. App. LEXIS 10146",
            "2005 WL 1309065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. State",
          "cluster_id": 1436051,
          "cite": [
            "843 A.2d 803",
            "380 Md. 1",
            "2004 Md. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re HV",
          "cluster_id": 894985,
          "cite": [
            "252 S.W.3d 319",
            "51 Tex. Sup. Ct. J. 736",
            "2008 Tex. LEXIS 316",
            "2008 WL 1147567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gore v. Secretary for the Department of Corrections",
          "cluster_id": 77743,
          "cite": [
            "492 F.3d 1273",
            "20 Fla. L. Weekly Fed. C 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Svondo Watson v. Donald Hulick, Warden, 1",
          "cluster_id": 797264,
          "cite": [
            "481 F.3d 537",
            "2007 U.S. App. LEXIS 7028",
            "2007 WL 879797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cornelius",
          "cluster_id": 2178207,
          "cite": [
            "856 A.2d 62",
            "2004 Pa. Super. 255",
            "2004 Pa. Super. LEXIS 2144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dewey v. State",
          "cluster_id": 2625182,
          "cite": [
            "169 P.3d 1149",
            "123 Nev. 483",
            "123 Nev. Adv. Rep. 47",
            "2007 Nev. LEXIS 58"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Norman v. State",
          "cluster_id": 2068009,
          "cite": [
            "976 A.2d 843",
            "2009 Del. LEXIS 306",
            "2009 WL 1676828"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Dennehy",
          "cluster_id": 151656,
          "cite": [
            "615 F.3d 1",
            "2010 U.S. App. LEXIS 15313",
            "2010 WL 2901805"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John J. Fellers",
          "cluster_id": 789225,
          "cite": [
            "397 F.3d 1090",
            "2005 U.S. App. LEXIS 2511",
            "2005 WL 350959"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dominique",
          "cluster_id": 5143838,
          "cite": [
            "960 A.2d 1160",
            "2008 ME 180",
            "2008 Me. LEXIS 185"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fellers v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131158) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 4,
        "triage_snippet_classified": 68
      },
      "lane2_top_cited": {
        "query": "cites:(131158)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05JnM9NTI4MDUyMCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28131158%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131158)",
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
    "complete_query": "cites:(131158)",
    "indexed_citing_opinions": 86,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131158,
        "count": 86,
        "count_source": "search"
      }
    ],
    "citation_count": 132,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/fellers-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjI0MzMxNTkmcz03ODQxMiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28131158%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131158,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131158,
        "cited_id": 777137,
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
    "date_created": "2026-07-05T03:24:43Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:24:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:24:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:28:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:24:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Fellers v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b732-10">
  Justice O’Connor
 </author>
<p id="Aid">
  delivered the opinion of the Court.
 </p>
<p id="AEC">
  After a grand jury indicted petitioner John J. Fellers, police officers arrested him at his home. During the course of the arrest, petitioner made several inculpatory statements.
  <span citation-index="1" class="star-pagination" label="521"> 
   *521
   </span>
  He argued that the officers deliberately elicited these statements from him outside the presence of counsel, and that the admission at trial of the fruits of those statements therefore violated his Sixth Amendment right to counsel. Petitioner contends that in rejecting this argument, the Court of Appeals for the Eighth Circuit improperly held that the Sixth Amendment right to counsel was “not applicable” because “the officers did not interrogate [petitioner] at his home.” <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#724" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d 721, 724</a></span> (2002). We granted the petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./538/905/">538 U. S. 905</a></span> (2003), and now reverse.
 </p>
<p id="ANy">
  I
 </p>
<p id="b733-3">
  On February 24, 2000, after a grand jury indicted petitioner for conspiracy to distribute methamphetamine, Lincoln Police Sergeant Michael Garnett and Lancaster County Deputy Sheriff Jeff Bliemeister went to petitioner’s home in Lincoln, Nebraska, to arrest him. App. 111. The officers knocked on petitioner’s door and, when petitioner answered, identified themselves and asked if they could come in.
  <em>
   Ibid.
  </em>
  Petitioner invited the officers into his living room.
  <em>
   Ibid.
  </em>
</p>
<p id="b733-4">
  The officers advised petitioner they had come to discuss his involvement in methamphetamine distribution.
  <em>
   Id.,
  </em>
  at 112. They informed petitioner that they had a federal warrant for his arrest and that a grand jury had indicted him for conspiracy to distribute methamphetamine.
  <em>
   Ibid.
  </em>
  The officers told petitioner that the indictment referred to his involvement with certain individuals, four of whom they named.
  <em>
   Ibid.
  </em>
  Petitioner then told the officers that he knew the four people and had used methamphetamine during his association with them.
  <em>
   Ibid.
  </em>
</p>
<p id="b733-5">
  After spending about 15 minutes in petitioner’s home, the officers transported petitioner to the Lancaster County jail.
  <em>
   Ibid.
  </em>
  There, the officers advised petitioner for the first time of his rights under
  <em>
   Miranda
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and
  <em>
   Patterson
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">487 U. S. 285</a></span> (1988). App. 112. Petitioner and the two officers signed a
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  waiver
  <span citation-index="1" class="star-pagination" label="522"> 
   *522
   </span>
  form, and petitioner then reiterated the inculpatory statements he had made earlier, admitted to having associated with other individuals implicated in the charged conspiracy, App. 29-39, and admitted to having loaned money to one of them even though he suspected that she was involved in drug transactions,
  <em>
   id.,
  </em>
  at 34..
 </p>
<p id="b734-5">
  Before trial, petitioner moved to suppress the inculpatory statements he made at his home and at the county jail. A Magistrate Judge conducted a hearing and recommended that the statements petitioner made at his home be suppressed because the officers had not informed petitioner of his
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  rights. App. 110-111. The Magistrate Judge found that petitioner made the statements in response to the officers’ “implicit] questions,” noting that the officers had told petitioner that the purpose of their visit was to discuss his use and distribution of methamphetamine.
  <em>
   Id.,
  </em>
  at 110. The Magistrate Judge further recommended that portions of petitioner’s jailhouse statement be suppressed as fruits of the prior failure to provide
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings. App. 110-111.
 </p>
<p id="b734-6">
  The District Court suppressed the “unwarned” statements petitioner made at his house but admitted petitioner’s jailhouse statements pursuant to
  <em>
   Oregon
  </em>
  v.
  <em>
   Elstad,
  </em>
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), concluding petitioner had knowingly and voluntarily waived his
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  rights before making the statements. App. 112-115.
 </p>
<p id="b734-7">
  Following a jury trial at which petitioner’s jailhouse statements were admitted into evidence, petitioner was convicted of conspiring to possess with intent to distribute methamphetamine. Petitioner appealed, arguing that his jailhouse statements should have been suppressed as fruits of the statements obtained at his home in violation of the Sixth Amendment. The Court of Appeals affirmed. <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d 721</a></span> (CA8 2002). With respect to petitioner’s argument that the officers’ failure to administer
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings at his home violated his Sixth Amendment right to counsel under
  <span citation-index="1" class="star-pagination" label="523"> 
   *523
   </span>
<em>
   <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">Patterson, supra,</a></span>
  </em>
  the Court of Appeals stated:
  <em>
   “Patterson
  </em>
  is not applicable here ... for the officers did not interrogate [petitioner] at his home.” 285 P. 3d, at 724. The Court of Appeals also concluded that the statements from the jail were properly admitted under the rule of
  <em>
   Elstad, supra.
  </em>
  <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#724" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d, at 724</a></span> (“‘Though
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made’ ” (quoting
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad"><em>
   Elstad, supra,
  </em>
  at 309</a></span>)).
 </p>
<p id="b735-5">
  Judge Riley filed a concurring opinion. He concluded that during their conversation at petitioner’s home, officers “deliberately elicited incriminating information” from petitioner. <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#726" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d, at 726-727</a></span>. That “post-indictment conduct outside the presence of counsel,” Judge Riley reasoned, violated petitioner’s Sixth Amendment rights.
  <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#727" aria-description="Citation for case: United States v. John J. Fellers"><em>
   Id.,
  </em>
  at 727</a></span>. Judge Riley nevertheless concurred in the judgment, concluding that the jailhouse statements were admissible under the rationale of
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  in light of petitioner’s knowing and voluntary waiver of his right to counsel. <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#727" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d, at 727</a></span>.
 </p>
<p id="AuL">
  II
 </p>
<p id="b735-1">
  The Sixth Amendment right to counsel is triggered at or after the time that judicial proceedings have been initiated . . . ‘whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.”’
  <em>
   Brewer
  </em>
  v.
  <em>
   Williams,
  </em>
  <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398</a></span> (1977) (quoting
  <em>
   Kirby
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972)). We have held that an accused is denied “the basic protections” of the Sixth Amendment “when there [is] used against him at his trial evidence of his own incriminating words, which federal agents . . . deliberately elicited from him after he had been indicted and in the absence of his counsel.”
  <em>
   Massiah
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 206</a></span> (1964); cf.
  <em>
   <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/" aria-description="Citation for case: Patterson v. Illinois">Patterson, supra</a></span>
  </em>
  (holding that the Sixth Amendment does not bar postindictment questioning in the absence of counsel if a defendant waives the right to counsel).
 </p>
<p id="b736-4">
<span citation-index="1" class="star-pagination" label="524"> 
   *524
   </span>
  We have consistently applied the deliberate-elicitation standard in subsequent Sixth Amendment cases, see
  <em>
   United States
  </em>
  v.
  <em>
   Henry,
  </em>
  <span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#270" aria-description="Citation for case: United States v. Henry">447 U. S. 264, 270</a></span> (1980) (“The question here is whether under the facts of this case a Government agent ‘deliberately elicited’ incriminating statements ... within the meaning of Massiah”);
  <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#399" aria-description="Citation for case: Brewer v. Williams"><em>
   Brewer, supra,
  </em>
  at 399</a></span> (finding a Sixth Amendment violation where a detective “deliberately and designedly set out to elicit information from [the suspect]”), and we have expressly distinguished this standard from the Fifth Amendment custodial-interrogation standard, see
  <em>
   Michigan
  </em>
  v.
  <em>
   Jackson,
  </em>
  <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#632" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 632, n. 5</a></span> (1986) (“[T]he Sixth Amendment provides a right to counsel... even when there is no interrogation and no Fifth Amendment applicability”);
  <em>
   Rhode Island
  </em>
  v.
  <em>
   Innis,
  </em>
  <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980) (“The definitions of ‘interrogation’ under the Fifth and Sixth Amendments, if indeed the term ‘interrogation’ is even apt in the Sixth Amendment context, are not necessarily interchangeable”); cf.
  <em>
   United States
  </em>
  v.
  <em>
   Wade,
  </em>
  <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967) (holding that the Sixth Amendment provides the right to counsel at a postindictment lineup even though the Fifth Amendment is not implicated).
 </p>
<p id="b736-5">
  The Court of Appeals erred in holding that the absence of an “interrogation” foreclosed petitioner’s claim that the jailhouse statements should have been suppressed as fruits of the statements taken from petitioner at his home. First, there is no question that the officers in this case “deliberately elicited” information from petitioner. Indeed, the officers, upon arriving at petitioner’s house, informed him that their purpose in coming was to discuss his involvement in the distribution of methamphetamine and his association with certain charged co-conspirators. <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/#723" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d, at 723</a></span>; App. 112. Because the ensuing discussion took place after petitioner had been indicted, outside the presence of counsel, and in the absence of any waiver of petitioner’s Sixth Amendment rights, the Court of Appeals erred in holding that the offi
  <span citation-index="1" class="star-pagination" label="525"> 
   *525
   </span>
  cers’ actions did not violate the Sixth Amendment standards established in
  <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States"><em>
   Massiah,
  </em>
  supra,</a></span> and its progeny. ■
 </p>
<p id="b737-5">
  Second, because of its erroneous determination that petitioner was not questioned in violation of Sixth Amendment standards, the Court of Appeals improperly conducted its “fruits” analysis under the Fifth Amendment. Specifically, it applied
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  to hold that the admissibility of the jailhouse statements turns solely on whether the statements were “ ‘knowingly and voluntarily made.’ ” <span class="citation" data-id="9494893"><a href="/opinion/777137/united-states-v-john-j-fellers/" aria-description="Citation for case: United States v. John J. Fellers">285 F. 3d, at 724</a></span> (quoting
  <em>
   Elstad,
  </em>
  <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 309</a></span>). The Court of Appeals did not reach the question whether the Sixth Amendment requires suppression of petitioner’s jailhouse statements on the ground that they were the fruits of previous questioning conducted in violation of the Sixth Amendment deliberate-elicitation standard. We have not had occasion to decide whether the rationale of
  <em>
   <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>
  </em>
  applies when a suspect makes incriminating statements after a knowing and voluntary waiver of his right to counsel notwithstanding earlier police questioning in violation of Sixth Amendment standards. We therefore remand to the Court of Appeals to address this issue in the first instance.
 </p>
<p id="b737-6">
  Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b737-7">
<em>
   It is so ordered.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Ferguson v. City of Charleston.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Ferguson v. City of Charleston"
type: case
citation: ""
parallel_cite: "532 U.S. 67; 121 S. Ct. 1281; 149 L. Ed. 2d 205; 2001 Daily Journal DAR 2839; 2001 Colo. J. C.A.R. 1427; 14 Fla. L. Weekly Fed. S 152; 69 U.S.L.W. 4184"
neutral_cite: 2001 U.S. LEXIS 2460
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-03-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ferguson v. City of Charleston
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118414/ferguson-v-city-of-charleston/"
  cluster_id: 118414
  opinion_id: 118414
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Indianapolis v. Edmond]]", "[[Chandler v. Miller]]", "[[Board of Education v. Earls]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "programmatic-purpose"]
holding: "Covertly drug-testing pregnant patients and reporting results to law enforcement is an unreasonable search; the special-needs exception…"
lake:
  record_id: Ferguson v. City of Charleston
  status: verified
  projected_at: 2026-07-06
---

# Ferguson v. City of Charleston

*532 U.S. 67 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A public hospital operated by the Medical University of South Carolina (MUSC), working with the Charleston police and prosecutor, adopted a policy under which maternity patients suspected of cocaine use were drug-tested without their consent; positive results were turned over to law enforcement, who used the threat of arrest and prosecution to press the women into treatment. Ten women who were tested and arrested challenged the policy as an unreasonable search.

## Issue
Whether a state hospital's nonconsensual, suspicionless drug testing of maternity patients to obtain evidence for law enforcement use fits within the "special needs" exception to the Fourth Amendment's warrant and probable-cause requirements.

## Rule
No. Where the immediate objective of a search program is to generate evidence for law enforcement, the special-needs exception does not apply, and the search is governed by the ordinary warrant/consent rule. The Court framed the narrow question as whether the State's interest could "justify a departure from the general rule that an official nonconsensual search is unconstitutional if not authorized by a valid warrant." — 532 U.S. at 70. ^pin-70

Although the program's ultimate goal may have been to get the women into treatment, "the immediate objective of the searches was to generate evidence *for law enforcement purposes* in order to reach that goal." — *Id.* at 83. ^pin-83

Because that immediate, law-enforcement purpose pervaded the policy, it fell outside the closely guarded category of permissible suspicionless searches.

## Application
The MUSC policy was developed with police and prosecutors, used chain-of-custody protocols, and delivered test results to officers who arrested the patients — so its immediate objective was to produce evidence for criminal enforcement, not a need divorced from ordinary law enforcement. Because the patients had not consented and no warrant authorized the testing, the suspicionless searches were unreasonable on these facts.

## Conclusion
The nonconsensual drug-testing policy was an unreasonable search; the judgment upholding it was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ferguson* applies the programmatic-purpose analysis of [[City of Indianapolis v. Edmond]]: a search program whose immediate purpose is ordinary law enforcement cannot be recharacterized as a "special need."

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *Ferguson v. City of Charleston*, 532 U.S. 67 (2001) — https://www.courtlistener.com/opinion/118414/ferguson-v-city-of-charleston/ — pinpoints: 70, 83.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9c4371fb95c85c68", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ferguson v. City of Charleston"}, "payload": {"all": [{"cite": "532 U.S. 67", "page": "67", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "532"}, {"cite": "121 S. Ct. 1281", "page": "1281", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "149 L. Ed. 2d 205", "page": "205", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "149"}, {"cite": "2001 U.S. LEXIS 2460", "page": "2460", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}, {"cite": "2001 Daily Journal DAR 2839", "page": "2839", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2001"}, {"cite": "2001 Colo. J. C.A.R. 1427", "page": "1427", "reporter": "Colo. J. C.A.R.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2001"}, {"cite": "14 Fla. L. Weekly Fed. S 152", "page": "152", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "14"}, {"cite": "69 U.S.L.W. 4184", "page": "4184", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "69"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Ferguson v. City of Charleston"}}
{"assertion_id": "5728aa7047daadb2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-70", "record_id": "Ferguson v. City of Charleston"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-70", "pinpoint_status": "slip-only", "quote": "exception to the Fourth Amendment's warrant and probable-cause requirements. ## Rule No. Where the immediate objective of a search program is to generate evidence for law enforcement, the special-needs exception does not apply, and the search is governed by the ordinary warrant/consent rule. The Court framed the narrow question as whether the State's interest could", "quote_fidelity": "mismatch", "record_id": "Ferguson v. City of Charleston", "star_marker": null}}
{"assertion_id": "d7b81fc821e5019a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-83", "record_id": "Ferguson v. City of Charleston"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-83", "pinpoint_status": "slip-only", "quote": "the immediate objective of the searches was to generate evidence *for law enforcement purposes* in order to reach that goal.", "quote_fidelity": "mismatch", "record_id": "Ferguson v. City of Charleston", "star_marker": null}}
{"assertion_id": "ce7c39488fcdf254", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ferguson v. City of Charleston"}, "payload": {"as_of_content": "2001-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Ferguson v. City of Charleston", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Ferguson v. City of Charleston

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ferguson v. City of Charleston",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ferguson v. City of Charleston",
    "case_name_short": "Ferguson",
    "case_name_full": "FERGUSON Et Al. v. CITY OF CHARLESTON Et Al.",
    "input_case_name": "Ferguson v. City of Charleston",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-03-21",
    "year": 2001,
    "docket": null,
    "cluster_id": 118414,
    "lead_opinion_id": 118414,
    "sibling_ids": [
      118414,
      9434054,
      9434055,
      9434056
    ],
    "absolute_url": "/opinion/118414/ferguson-v-city-of-charleston/",
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
        "cite": "532 U.S. 67",
        "volume": "532",
        "reporter": "U.S.",
        "page": "67",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1281",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 205",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 2839",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "2839",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 1427",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "1427",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 152",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "152",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4184",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4184",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 2460",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2460",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 67",
        "volume": "532",
        "reporter": "U.S.",
        "page": "67",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1281",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 205",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "205",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 2460",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "2460",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 2839",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "2839",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 1427",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "1427",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 152",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "152",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4184",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4184",
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
      "id": "pin-70",
      "page": null,
      "quote": "exception to the Fourth Amendment's warrant and probable-cause requirements. ## Rule No. Where the immediate objective of a search program is to generate evidence for law enforcement, the special-needs exception does not apply, and the search is governed by the ordinary warrant/consent rule. The Court framed the narrow question as whether the State's interest could",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-83",
      "page": null,
      "quote": "the immediate objective of the searches was to generate evidence *for law enforcement purposes* in order to reach that goal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ferguson v. City of Charleston",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Funk",
          "cluster_id": 4002857,
          "cite": [
            "896 N.E.2d 203",
            "177 Ohio App. 3d 814",
            "2008 Ohio 4086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Murray v. State",
          "cluster_id": 1656212,
          "cite": [
            "245 S.W.3d 37",
            "2007 WL 4462745"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Burroughs",
          "cluster_id": 1231391,
          "cite": [
            "648 S.E.2d 561",
            "185 N.C. App. 496",
            "2007 N.C. App. LEXIS 1811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weikert",
          "cluster_id": 202888,
          "cite": [
            "504 F.3d 1",
            "2007 U.S. App. LEXIS 18845",
            "2007 WL 2265660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Shreck",
          "cluster_id": 2509432,
          "cite": [
            "107 P.3d 1048",
            "2004 WL 2137067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reedy v. Evanson",
          "cluster_id": 152023,
          "cite": [
            "615 F.3d 197",
            "2010 U.S. App. LEXIS 15974",
            "2010 WL 2991378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony v. City of New York",
          "cluster_id": 8437661,
          "cite": [
            "339 F.3d 129",
            "2003 U.S. App. LEXIS 16279",
            "2003 WL 21864087"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kimler",
          "cluster_id": 163635,
          "cite": [
            "335 F.3d 1132",
            "2003 WL 21519916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of L. A. v. Patel",
          "cluster_id": 2811846,
          "cite": [
            "576 U.S. 409",
            "135 S. Ct. 2443",
            "192 L. Ed. 2d 435",
            "2015 U.S. LEXIS 4065",
            "83 U.S.L.W. 4520",
            "25 Fla. L. Weekly Fed. S 412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
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
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
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
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe v. Woodard",
          "cluster_id": 4578612,
          "cite": [
            "912 F.3d 1278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kerns v. Bader",
          "cluster_id": 619354,
          "cite": [
            "663 F.3d 1173",
            "2011 WL 6367728"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Athan",
          "cluster_id": 2622136,
          "cite": [
            "158 P.3d 27"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Garvin",
          "cluster_id": 2038191,
          "cite": [
            "847 N.E.2d 82",
            "219 Ill. 2d 104",
            "301 Ill. Dec. 423",
            "2006 Ill. LEXIS 328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lynch v. City of New York",
          "cluster_id": 1360513,
          "cite": [
            "589 F.3d 94",
            "30 I.E.R. Cas. (BNA) 124",
            "2009 U.S. App. LEXIS 26980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Toomer v. Garrett",
          "cluster_id": 1307887,
          "cite": [
            "574 S.E.2d 76",
            "155 N.C. App. 462",
            "2002 N.C. App. LEXIS 1613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Los Angeles v. Patel",
          "cluster_id": 2810524,
          "cite": [
            "576 U.S. 409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brandon Michael Lifshitz",
          "cluster_id": 786321,
          "cite": [
            "369 F.3d 173",
            "2004 WL 1043468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ferguson v. City of Charleston:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118414 OR 9434054 OR 9434055 OR 9434056) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcxNzA1NjAwMDAwJnM9Mjg0NDExMyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118414+OR+9434054+OR+9434055+OR+9434056%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(118414 OR 9434054 OR 9434055 OR 9434056)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NCZzPTc4MTc1MiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118414+OR+9434054+OR+9434055+OR+9434056%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118414 OR 9434054 OR 9434055 OR 9434056)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118414 OR 9434054 OR 9434055 OR 9434056)",
    "indexed_citing_opinions": 337,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118414,
        "count": 305,
        "count_source": "search"
      },
      {
        "opinion_id": 9434054,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9434055,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434056,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ferguson-v-city-of-charleston.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwMDAxNTcmcz00ODAzODQyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118414+OR+9434054+OR+9434055+OR+9434056%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118414,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 109592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 118100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 118263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 118397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 1327281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118414,
        "cited_id": 1357541,
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
    "date_created": "2026-07-05T03:28:28Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:28:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:28:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:33:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:28:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ferguson v. City of Charleston

```
<div>
<center><b><span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">532 U.S. 67</a></span> (2001)</b></center>
<center><h1>FERGUSON et al.<br>
v.<br>
CITY OF CHARLESTON et al.</h1></center>
<center>No. 99-936.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 4, 2000.</center>
<center>Decided March 21, 2001.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*69</span> <span class="star-pagination">*69</span> Stevens, J., delivered the opinion of the Court, in which O'Connor, Souter, Ginsburg, and Breyer, JJ., joined. Kennedy, J., filed an opinion concurring in the judgment, <i>post,</i> p. 86. Scalia, J., filed a dissenting opinion, in which Rehnquist, C. J., and Thomas, J., joined as to Part II, <i>post,</i> p. 91.</p>
<p><i>Priscilla J. Smith</i> argued the cause for petitioners. With her on the briefs were <i>Simon Heller, Lynn Paltrow, Susan Frietsche, David S. Cohen, Susan Dunn, David Rudovsky,</i>  and <i>Seth Kreimer.</i> </p>
<p><i>Robert H. Hood</i> argued the cause for respondents. With him on the brief were <i>Barbara Wynne Showers</i> and <i>Mary Agnes Hood Craig.</i><sup>[*]</sup></p>
<p>Justice Stevens, delivered the opinion of the Court.</p>
<p>In this case, we must decide whether a state hospital's performance of a diagnostic test to obtain evidence of a patient's criminal conduct for law enforcement purposes is an <span class="star-pagination">*70</span> unreasonable search if the patient has not consented to the procedure. More narrowly, the question is whether the interest in using the threat of criminal sanctions to deter pregnant women from using cocaine can justify a departure from the general rule that an official nonconsensual search is unconstitutional if not authorized by a valid warrant.</p>
<p></p>
<h2>I</h2>
<p>In the fall of 1988, staff members at the public hospital operated in the city of Charleston by the Medical University of South Carolina (MUSC) became concerned about an apparent increase in the use of cocaine by patients who were receiving prenatal treatment.<sup>[1]</sup> In response to this perceived increase, as of April 1989, MUSC began to order drug screens to be performed on urine samples from maternity patients who were suspected of using cocaine. If a patient tested positive, she was then referred by MUSC staff to the county substance abuse commission for counseling and treatment. However, despite the referrals, the incidence of cocaine use among the patients at MUSC did not appear to change.</p>
<p>Some four months later, Nurse Shirley Brown, the case manager for the MUSC obstetrics department, heard a news broadcast reporting that the police in Greenville, South Carolina, were arresting pregnant users of cocaine on the theory that such use harmed the fetus and was therefore child abuse.<sup>[2]</sup> Nurse Brown discussed the story with MUSC's general counsel, Joseph C. Good, Jr., who then contacted <span class="star-pagination">*71</span> Charleston Solicitor Charles Condon in order to offer MUSC's cooperation in prosecuting mothers whose children tested positive for drugs at birth.<sup>[3]</sup></p>
<p>After receiving Good's letter, Solicitor Condon took the first steps in developing the policy at issue in this case. He organized the initial meetings, decided who would participate, and issued the invitations, in which he described his plan to prosecute women who tested positive for cocaine while pregnant. The task force that Condon formed included representatives of MUSC, the police, the County Substance Abuse Commission and the Department of Social Services. Their deliberations led to MUSC's adoption of a 12-page document entitled "POLICY M-7," dealing with the subject of "Management of Drug Abuse During Pregnancy." App. to Pet. for Cert. A-53.</p>
<p>The first three pages of Policy M-7 set forth the procedure to be followed by the hospital staff to "identify/assist pregnant patients suspected of drug abuse." <i><span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">Id.,</a></span></i> at A-53 to A-56. The first section, entitled the "Identification of Drug Abusers," provided that a patient should be tested for cocaine through a urine drug screen if she met one or more of nine criteria.<sup>[4]</sup> It also stated that a chain of custody should <span class="star-pagination">*72</span> be followed when obtaining and testing urine samples, presumably to make sure that the results could be used in subsequent criminal proceedings. The policy also provided for education and referral to a substance abuse clinic for patients who tested positive. Most important, it added the threat of law enforcement intervention that "provided the necessary `leverage' to make the [p]olicy effective." Brief for Respondents 8. That threat was, as respondents candidly acknowledge, essential to the program's success in getting women into treatment and keeping them there.</p>
<p>The threat of law enforcement involvement was set forth in two protocols, the first dealing with the identification of drug use during pregnancy, and the second with identification of drug use after labor. Under the latter protocol, the police were to be notified without delay and the patient promptly arrested. Under the former, after the initial positive drug test, the police were to be notified (and the patient arrested) only if the patient tested positive for cocaine a second time or if she missed an appointment with a substance abuse counselor.<sup>[5]</sup> In 1990, however, the policy was modified at the behest of the solicitor's office to give the patient who tested positive during labor, like the patient who tested positive during a prenatal care visit, an opportunity to avoid arrest by consenting to substance abuse treatment.</p>
<p>The last six pages of the policy contained forms for the patients to sign, as well as procedures for the police to follow when a patient was arrested. The policy also prescribed in detail the precise offenses with which a woman could be charged, depending on the stage of her pregnancy. If the pregnancy was 27 weeks or less, the patient was to be charged with simple possession. If it was 28 weeks or more, she was to be charged with possession and distribution to a person under the age of 18in this case, the fetus. If she <span class="star-pagination">*73</span> delivered "while testing positive for illegal drugs," she was also to be charged with unlawful neglect of a child. App. to Pet. for Cert. A-62. Under the policy, the police were instructed to interrogate the arrestee in order "to ascertain the identity of the subject who provided illegal drugs to the suspect." <i><span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">Id.,</a></span></i> at A-63. Other than the provisions describing the substance abuse treatment to be offered to women who tested positive, the policy made no mention of any change in the prenatal care of such patients, nor did it prescribe any special treatment for the newborns.</p>
<p></p>
<h2>II</h2>
<p>Petitioners are 10 women who received obstetrical care at MUSC and who were arrested after testing positive for cocaine. Four of them were arrested during the initial implementation of the policy; they were not offered the opportunity to receive drug treatment as an alternative to arrest. The others were arrested after the policy was modified in 1990; they either failed to comply with the terms of the drug treatment program or tested positive for a second time. Respondents include the city of Charleston, law enforcement officials who helped develop and enforce the policy, and representatives of MUSC.</p>
<p>Petitioners' complaint challenged the validity of the policy under various theories, including the claim that warrantless and nonconsensual drug tests conducted for criminal investigatory purposes were unconstitutional searches. Respondents advanced two principal defenses to the constitutional claim: (1) that, as a matter of fact, petitioners had consented to the searches; and (2) that, as a matter of law, the searches were reasonable, even absent consent, because they were justified by special non-law-enforcement purposes. The District Court rejected the second defense because the searches in question "were not done by the medical university for independent purposes. [Instead,] the police came in and there was an agreement reached that the positive <span class="star-pagination">*74</span> screens would be shared with the police." App. 1248-1249. Accordingly, the District Court submitted the factual defense to the jury with instructions that required a verdict in favor of petitioners unless the jury found consent.<sup>[6]</sup> The jury found for respondents.</p>
<p>Petitioners appealed, arguing that the evidence was not sufficient to support the jury's consent finding. The Court of Appeals for the Fourth Circuit affirmed, but without reaching the question of consent. <span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">186 F. 3d 469</a></span> (1999). Disagreeing with the District Court, the majority of the appellate panel held that the searches were reasonable as a matter of law under our line of cases recognizing that "special needs" may, in certain exceptional circumstances, justify a search policy designed to serve non-law-enforcement ends.<sup>[7]</sup><span class="star-pagination">*75</span> On the understanding "that MUSC personnel conducted the urine drug screens for medical purposes wholly independent of an intent to aid law enforcement efforts,"<sup>[8]</sup><span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/#477" aria-description="Citation for case: Ferguson v. City of Charleston"><i>id.,</i> at 477</a></span>, the majority applied the balancing test used in <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), and <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), and concluded that the interest in curtailing the pregnancy complications and medical costs associated with maternal cocaine use outweighed what the majority termed a minimal intrusion on the privacy of the patients. In dissent, Judge Blake concluded that the "special needs" doctrine should not apply and <span class="star-pagination">*76</span> that the evidence of consent was insufficient to sustain the jury's verdict. <span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/#487" aria-description="Citation for case: Ferguson v. City of Charleston">186 F. 3d, at 487-488</a></span>.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./528/1187/">528 U. S. 1187</a></span> (2000), to review the appellate court's holding on the "special needs" issue. Because we do not reach the question of the sufficiency of the evidence with respect to consent, we necessarily assume for purposes of our decisionas did the Court of Appealsthat the searches were conducted without the informed consent of the patients. We conclude that the judgment should be reversed and the case remanded for a decision on the consent issue.</p>
<p></p>
<h2>III</h2>
<p>Because MUSC is a state hospital, the members of its staff are government actors, subject to the strictures of the Fourth Amendment. <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#335" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 335-337</a></span> (1985). Moreover, the urine tests conducted by those staff members were indisputably searches within the meaning of the Fourth Amendment. <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 617</a></span> (1989).<sup>[9]</sup> Neither the District Court nor the Court of Appeals concluded that any of the nine criteria used to identify the women to be searched provided either probable cause to believe that they were using cocaine, or even the basis for a reasonable suspicion of such use. Rather, the District Court and the Court of Appeals viewed the case as one involving MUSC's right <span class="star-pagination">*77</span> to conduct searches without warrants or probable cause.<sup>[10]</sup> Furthermore, given the posture in which the case comes to us, we must assume for purposes of our decision that the tests were performed without the informed consent of the patients.<sup>[11]</sup></p>
<p>Because the hospital seeks to justify its authority to conduct drug tests and to turn the results over to law enforcement agents without the knowledge or consent of the patients, this case differs from the four previous cases in which we have considered whether comparable drug tests "fit within the closely guarded category of constitutionally permissible suspicionless searches." <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#309" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305, 309</a></span> (1997). In three of those cases, we sustained drug tests for railway employees involved in train accidents, <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989), for United States Customs Service employees seeking promotion to certain sensitive positions, <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), and for high school students participating in interscholastic sports, <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995). In the fourth case, we struck down such testing for candidates for designated state offices as unreasonable. <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305</a></span> (1997).</p>
<p><span class="star-pagination">*78</span> In each of those cases, we employed a balancing test that weighed the intrusion on the individual's interest in privacy against the "special needs" that supported the program. As an initial matter, we note that the invasion of privacy in this case is far more substantial than in those cases. In the previous four cases, there was no misunderstanding about the purpose of the test or the potential use of the test results, and there were protections against the dissemination of the results to third parties.<sup>[12]</sup> The use of an adverse test result to disqualify one from eligibility for a particular benefit, such as a promotion or an opportunity to participate in an extracurricular activity, involves a less serious intrusion on privacy than the unauthorized dissemination of such results to third parties. The reasonable expectation of privacy enjoyed by the typical patient undergoing diagnostic tests in a hospital is that the results of those tests will not be shared with nonmedical personnel without her consent. See Brief for American Medical Association as <i>Amicus Curiae</i> 11; Brief for American Public Health Association et al. as <i>Amici Curiae</i> 6, 17-19.<sup>[13]</sup> In none of our prior cases was there any intrusion upon that kind of expectation.<sup>[14]</sup></p>
<p><span class="star-pagination">*79</span> The critical difference between those four drug-testing cases and this one, however, lies in the nature of the "special need" asserted as justification for the warrantless searches. In each of those earlier cases, the "special need" that was advanced as a justification for the absence of a warrant or individualized suspicion was one divorced from the State's general interest in law enforcement.<sup>[15]</sup> This point was emphasized <span class="star-pagination">*80</span> both in the majority opinions sustaining the programs in the first three cases,<sup>[16]</sup> as well as in the dissent in the <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span></i> case.<sup>[17]</sup> In this case, however, the central and indispensable feature of the policy from its inception was the use of law enforcement to coerce the patients into substance abuse treatment. This fact distinguishes this case from circumstances in which physicians or psychologists, in the <span class="star-pagination">*81</span> course of ordinary medical procedures aimed at helping the patient herself, come across information that under rules of law or ethics is subject to reporting requirements, which no one has challenged here. See, <i>e. g.,</i> Council on Ethical and Judicial Affairs, American Medical Association, PolicyFinder, Current Opinions E-5.05 (2000) (requiring reporting where "a patient threatens to inflict serious bodily harm to another person or to him or herself and there is a reasonable probability that the patient may carry out the threat"); <span class="citation no-link">Ark. Code Ann. § 12-12-602</span> (1999) (requiring reporting of intentionally inflicted knife or gunshot wounds); <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-3620</span> (Supp. 2000) (requiring "any . . . person having responsibility for the care or treatment of children" to report suspected abuse or neglect to a peace officer or child protection agency).<sup>[18]</sup></p>
<p>Respondents argue in essence that their ultimate purposenamely, protecting the health of both mother and childis a beneficent one. In <i><span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">Chandler</a></span>,</i> however, we did not simply accept the State's invocation of a "special need." Instead, we carried out a "close review" of the scheme at issue before concluding that the need in question was not "special," as that term has been defined in our cases. <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#322" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 322</a></span>. In this case, a review of the M-7 policy plainly reveals that the purpose actually served by the MUSC searches "is ultimately indistinguishable from the general interest in crime control." <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 44</a></span> (2000).</p>
<p>In looking to the programmatic purpose, we consider all the available evidence in order to determine the relevant primary purpose. See, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#45" aria-description="Citation for case: City of Indianapolis v. Edmond"><i>e. g., id.,</i> at 45-47</a></span>. In this case, as <span class="star-pagination">*82</span> Judge Blake put it in her dissent below, "it . . . is clear from the record that an initial and continuing focus of the policy was on the arrest and prosecution of drug-abusing mothers . . . ." <span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/#484" aria-description="Citation for case: Ferguson v. City of Charleston">186 F. 3d, at 484</a></span>. Tellingly, the document codifying the policy incorporates the police's operational guidelines. It devotes its attention to the chain of custody, the range of possible criminal charges, and the logistics of police notification and arrests. Nowhere, however, does the document discuss different courses of medical treatment for either mother or infant, aside from treatment for the mother's addiction.</p>
<p>Moreover, throughout the development and application of the policy, the Charleston prosecutors and police were extensively involved in the day-to-day administration of the policy. Police and prosecutors decided who would receive the reports of positive drug screens and what information would be included with those reports. App. 78-80, 145-146, 1058-1060. Law enforcement officials also helped determine the procedures to be followed when performing the screens.<sup>[19]</sup><i>Id.,</i> at 1052-1053. See also <i>id.,</i> at 26-27, 945. In the course of the policy's administration, they had access to Nurse Brown's medical files on the women who tested positive, routinely attended the substance abuse team's meetings, and regularly received copies of team documents discussing the women's progress. <i>Id.,</i> at 122-124, 609-610. Police took pains to coordinate the timing and circumstances of the arrests with MUSC staff, and, in particular, Nurse Brown. <i>Id.,</i> at 1057-1058.</p>
<p>While the ultimate goal of the program may well have been to get the women in question into substance abuse treatment <span class="star-pagination">*83</span> and off of drugs, the immediate objective of the searches was to generate evidence <i>for law enforcement purposes</i><sup>[20]</sup> in order to reach that goal.<sup>[21]</sup> The threat of law enforcement <span class="star-pagination">*84</span> may ultimately have been intended as a means to an end, but the direct and primary purpose of MUSC's policy was to ensure the use of those means. In our opinion, this distinction is critical. Because law enforcement involvement always serves some broader social purpose or objective, under respondents' view, virtually any nonconsensual suspicionless search could be immunized under the special needs doctrine by defining the search solely in terms of its ultimate, rather than immediate, purpose.<sup>[22]</sup> Such an approach is inconsistent with the Fourth Amendment. Given the primary purpose of the Charleston program, which was to use the threat of arrest and prosecution in order to force women into treatment, and given the extensive involvement of law enforcement officials at every stage of the policy, this case simply does not fit within the closely guarded category of "special needs."<sup>[23]</sup></p>
<p>The fact that positive test results were turned over to the police does not merely provide a basis for distinguishing our prior cases applying the "special needs" balancing approach to the determination of drug use. It also provides an affirmative reason for enforcing the strictures of the Fourth Amendment. While state hospital employees, like other citizens, may have a duty to provide the police with evidence <span class="star-pagination">*85</span> of criminal conduct that they inadvertently acquire in the course of routine treatment, when they undertake to obtain such evidence from their patients <i>for the specific purpose of incriminating those patients,</i> they have a special obligation to make sure that the patients are fully informed about their constitutional rights, as standards of knowing waiver require.<sup>[24]</sup> Cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>As respondents have repeatedly insisted, their motive was benign rather than punitive. Such a motive, however, cannot justify a departure from Fourth Amendment protections, given the pervasive involvement of law enforcement with the development and application of the MUSC policy. The stark <span class="star-pagination">*86</span> and unique fact that characterizes this case is that Policy M-7 was designed to obtain evidence of criminal conduct by the tested patients that would be turned over to the police and that could be admissible in subsequent criminal prosecutions. While respondents are correct that drug abuse both was and is a serious problem, "the gravity of the threat alone cannot be dispositive of questions concerning what means law enforcement officers may employ to pursue a given purpose." <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#42" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 42-43</a></span>. The Fourth Amendment's general prohibition against nonconsensual, warrantless, and suspicionless searches necessarily applies to such a policy. See, <i>e. g., </i><i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#308" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 308</a></span>; <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 619</a></span>.</p>
<p>Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Kennedy, concurring in the judgment.</p>
<p>I agree that the search procedure in issue cannot be sustained under the Fourth Amendment. My reasons for this conclusion differ somewhat from those set forth by the Court, however, leading to this separate opinion.</p>
<p></p>
<h2>I</h2>
<p>The Court does not dispute that the search policy at some level serves special needs, beyond those of ordinary law enforcement, such as the need to protect the health of mother and child when a pregnant mother uses cocaine. Instead, the majority characterizes these special needs as the "ultimate goal[s]" of the policy, as distinguished from the policy's "immediate purpose," the collection of evidence of drug use, which, the Court reasons, is the appropriate inquiry for the special needs analysis. <i>Ante,</i> at 81-84.</p>
<p>The majority views its distinction between the ultimate goal and immediate purpose of the policy as critical to its <span class="star-pagination">*87</span> analysis. <i>Ante,</i> at 83-84. The distinction the Court makes, however, lacks foundation in our special needs cases. All of our special needs cases have turned upon what the majority terms the policy's ultimate goal. For example, in <i>Skinner</i>  v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989), had we employed the majority's distinction, we would have identified as the relevant need the collection of evidence of drug and alcohol use by railway employees. Instead, we identified the relevant need as "[t]he Government's interest in regulating the conduct of railroad employees to ensure [railroad] safety." <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#620" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Id.,</i> at 620</a></span>. In <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), the majority's distinction should have compelled us to isolate the relevant need as the gathering of evidence of drug abuse by would-be drug interdiction officers. Instead, the special needs the Court identified were the necessities "to deter drug use among those eligible for promotion to sensitive positions within the [United States Customs] Service and to prevent the promotion of drug users to those positions." <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#666" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Id.,</i> at 666</a></span>. In <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995), the majority's distinction would have required us to identify the immediate purpose of gathering evidence of drug use by student-athletes as the relevant "need" for purposes of the special needs analysis. Instead, we sustained the policy as furthering what today's majority would have termed the policy's ultimate goal: "[d]eterring drug use by our Nation's schoolchildren," and particularly by student-athletes, because "the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high." <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#661" aria-description="Citation for case: Vernonia School District 47J v. Acton"><i>Id.,</i> at 661-662</a></span>.</p>
<p>It is unsurprising that in our prior cases we have concentrated on what the majority terms a policy's ultimate goal, rather than its proximate purpose. By very definition, in almost every case the immediate purpose of a search policy will be to obtain evidence. The circumstance that a particular search, like all searches, is designed to collect evidence <span class="star-pagination">*88</span> of some sort reveals nothing about the need it serves. Put a different way, although procuring evidence is the immediate result of a successful search, until today that procurement has not been identified as the special need which justifies the search.</p>
<p></p>
<h2>II</h2>
<p>While the majority's reasoning seems incorrect in the respects just discussed, I agree with the Court that the search policy cannot be sustained. As the majority demonstrates and well explains, there was substantial law enforcement involvement in the policy from its inception. None of our special needs precedents has sanctioned the routine inclusion of law enforcement, both in the design of the policy and in using arrests, either threatened or real, to implement the system designed for the special needs objectives. The special needs cases we have decided do not sustain the active use of law enforcement, including arrest and prosecutions, as an integral part of a program which seeks to achieve legitimate, civil objectives. The traditional warrant and probable-cause requirements are waived in our previous cases on the explicit assumption that the evidence obtained in the search is not intended to be used for law enforcement purposes. Most of those tested for drug use under the policy at issue here were not brought into direct contact with law enforcement. This does not change the fact, however, that, as a systemic matter, law enforcement was a part of the implementation of the search policy in each of its applications. Every individual who tested positive was given a letter explaining the policy not from the hospital but from the solicitor's office. Everyone who tested positive was told a second positive test or failure to undergo substance abuse treatment would result in arrest and prosecution. As the Court holds, the hospital acted, in some respects, as an institutional arm of law enforcement for purposes of the policy. Under these circumstances, while the policy may well have served legitimate needs unrelated to law enforcement, it had <span class="star-pagination">*89</span> as well a penal character with a far greater connection to law enforcement than other searches sustained under our special needs rationale.</p>
<p>In my view, it is necessary and prudent to be explicit in explaining the limitations of today's decision. The beginning point ought to be to acknowledge the legitimacy of the State's interest in fetal life and of the grave risk to the life and health of the fetus, and later the child, caused by cocaine ingestion. Infants whose mothers abuse cocaine during pregnancy are born with a wide variety of physical and neurological abnormalities. See Chiriboga, Brust, Bateman, &amp; Hauser, Dose-Response Effect of Fetal Cocaine Exposure on Newborn Neurologic Function, 103 Pediatrics 79 (1999) (finding that, compared with unexposed infants, cocaineexposed infants experienced higher rates of intrauterine growth retardation, smaller head circumference, global hypertonia, coarse tremor, and extensor leg posture). Prenatal exposure to cocaine can also result in developmental problems which persist long after birth. See Arendt, Angelopoulos, Salvator, &amp; Singer, Motor Development of Cocaine-exposed Children at Age Two Years, 103 Pediatrics 86 (1999) (concluding that, at two years of age, children who were exposed to cocaine in utero exhibited significantly less fine and gross motor development than those not so exposed); Chasnoff et al., Prenatal Exposure to Cocaine and Other Drugs: Outcome at Four to Six Years, 846 Annals of the New York Academy of Sciences 314, 319-320 (J. Harvey and B. Kosofsky eds. 1998) (finding that 4- to 6-year-olds who were exposed to cocaine in utero exhibit higher instances of depression, anxiety, social, thought, and attention problems, and delinquent and aggressive behaviors than their unexposed counterparts). There can be no doubt that a mother's ingesting this drug can cause tragic injury to a fetus and a child. There should be no doubt that South Carolina can impose punishment upon an expectant mother who has so little regard for her own unborn that she risks causing him <span class="star-pagination">*90</span> or her lifelong damage and suffering. The State, by taking special measures to give rehabilitation and training to expectant mothers with this tragic addiction or weakness, acts well within its powers and its civic obligations.</p>
<p>The holding of the Court, furthermore, does not call into question the validity of mandatory reporting laws such as child abuse laws which require teachers to report evidence of child abuse to the proper authorities, even if arrest and prosecution is the likely result. That in turn highlights the real difficulty. As this case comes to us, and as reputable sources confirm, see K. Farkas, Training Health Care and Human Services Personnel in Perinatal Substance Abuse, in Drug &amp; Alcohol Abuse Reviews, Substance Abuse During Pregnancy and Childhood 13, 27-28 (R. Watson ed. 1995); U. S. Dept. of Health and Human Services, Substance Abuse and Mental Health Services Administration, Pregnant, Substance-Using Women 48 (1993), we must accept the premise that the medical profession can adopt acceptable criteria for testing expectant mothers for cocaine use in order to provide prompt and effective counseling to the mother and to take proper medical steps to protect the child. If prosecuting authorities then adopt legitimate procedures to discover this information and prosecution follows, that ought not to invalidate the testing. One of the ironies of the case, then, may be that the program now under review, which gives the cocaine user a second and third chance, might be replaced by some more rigorous system. We must, however, take the case as it comes to us; and the use of handcuffs, arrests, prosecutions, and police assistance in designing and implementing the testing and rehabilitation policy cannot be sustained under our previous cases concerning mandatory testing.</p>
<p></p>
<h2>III</h2>
<p>An essential, distinguishing feature of the special needs cases is that the person searched has consented, though the usual voluntariness analysis is altered because adverse consequences <span class="star-pagination">*91</span> (<i>e. g.,</i> dismissal from employment or disqualification from playing on a high school sports team) will follow from refusal. The person searched has given consent, as defined to take into account that the consent was not voluntary in the full sense of the word. See <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#615" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 615</a></span>; <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#660" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 660-661</a></span>; <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#650" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 650-651</a></span>. The consent, and the circumstances in which it was given, bear upon the reasonableness of the whole special needs program.</p>
<p>Here, on the other hand, the question of consent, even with the special connotation used in the special needs cases, has yet to be decided. Indeed, the Court finds it necessary to take the unreal step of assuming there was no voluntary consent at all. Thus, we have erected a strange world for deciding the case.</p>
<p>My discussion has endeavored to address the permissibility of a law enforcement purpose in this artificial context. The role played by consent might have affected our assessment of the issues. My concurrence in the judgment, furthermore, should not be interpreted as having considered or resolved the important questions raised by Justice Scalia with reference to whether limits might be imposed on the use of the evidence if in fact it were obtained with the patient's consent and in the context of the special needs program. Had we the prerogative to discuss the role played by consent, the case might have been quite a different one. All are in agreement, of course, that the Court of Appeals will address these issues in further proceedings on remand.</p>
<blockquote>With these remarks, I concur in the judgment. Justice Scalia, with whom The Chief Justice and</blockquote>
<p>Justice Thomas join as to Part II, dissenting.</p>
<p>There is always an unappealing aspect to the use of doctors and nurses, ministers of mercy, to obtain incriminating evidence against the supposed objects of their ministration although here, it is correctly pointed out, the doctors and <span class="star-pagination">*92</span> nurses were ministering not just to the mothers but also to the children whom their cooperation with the police was meant to protect. But whatever may be the correct social judgment concerning the desirability of what occurred here, that is not the issue in the present case. The Constitution does not resolve all difficult social questions, but leaves the vast majority of them to resolution by debate and the democratic processwhich would produce a decision by the citizens of Charleston, through their elected representatives, to forbid or permit the police action at issue here. The question before us is a narrower one: whether, whatever the desirability of this police conduct, it violates the Fourth Amendment's prohibition of unreasonable searches and seizures. In my view, it plainly does not.</p>
<p></p>
<h2>I</h2>
<p>The first step in Fourth Amendment analysis is to identify the search or seizure at issue. What petitioners, the Court, and to a lesser extent the concurrence really object to is not the urine testing, but the hospital's reporting of positive drug-test results to police. But the latter is obviously not a search. At most it may be a "derivative use of the product of a past unlawful search," which, of course, "work[s] no new Fourth Amendment wrong" and "presents a question, not of rights, but of remedies." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974). There is only one act that could conceivably be regarded as a search of petitioners in the present case: the <i>taking</i> of the urine sample. I suppose the <i>testing</i>  of that urine for traces of unlawful drugs could be considered a search of sorts, but the Fourth Amendment protects only against searches of citizens' "persons, houses, papers, and effects"; and it is entirely unrealistic to regard urine as one of the "effects" (<i>i. e.,</i> part of the property) of the person who has passed and abandoned it. Cf. <i>California</i> v. <i>Greenwood,</i>  <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">486 U. S. 35</a></span> (1988) (garbage left at curb is not property protected by the Fourth Amendment). Some would argue, <span class="star-pagination">*93</span> I suppose, that testing of the urine is prohibited by some generalized privacy right "emanating" from the "penumbras" of the Constitution (a question that is not before us); but it is not even arguable that the testing of urine that has been lawfully obtained is a Fourth Amendment search. (I may add that, even if it were, the factors legitimizing the taking of the sample, which I discuss below, would likewise legitimize the testing of it.)</p>
<p>It is rudimentary Fourth Amendment law that a search which has been consented to is not unreasonable. There is no contention in the present case that the urine samples were extracted forcibly. The only conceivable bases for saying that they were obtained without consent are the contentions (1) that the consent was coerced by the patients' need for medical treatment, (2) that the consent was uninformed because the patients were not told that the tests would include testing for drugs, and (3) that the consent was uninformed because the patients were not told that the results of the tests would be provided to the police.<sup>[1]</sup> (When the court below said that it was reserving the factual issue of consent, see <span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/#476" aria-description="Citation for case: Ferguson v. City of Charleston">186 F. 3d 469, 476</a></span> (CA4 1999), it was referring at most to these threeand perhaps just to the last two.)</p>
<p><span class="star-pagination">*94</span> Under our established Fourth Amendment law, the last two contentions would not suffice, even without reference to the special-needs doctrine. The Court's analogizing of this case to <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and its claim that "standards of knowing waiver" apply, <i>ante,</i> at 85, are flatly contradicted by our jurisprudence, which shows that using lawfully (but deceivingly) obtained material for purposes other than those represented, and giving that material or information derived from it to the police, is not unconstitutional. In <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966), "[t]he argument [was] that [the informant's] failure to disclose his role as a government informant vitiated the consent that the petitioner gave" for the agent's access to evidence of criminal wrongdoing, <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#300" aria-description="Citation for case: Hoffa v. United States"><i>id.,</i> at 300</a></span>. We rejected that argument, because "the Fourth Amendment [does not protect] a wrongdoer's misplaced belief that a person to whom he voluntarily confides his wrongdoing will not reveal it." <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States"><i>Id.,</i> at 302</a></span>. Because the defendant had voluntarily provided access to the evidence, there was no reasonable expectation of privacy to invade. Abuse of trust is surely a sneaky and ungentlemanly thing, and perhaps there should be (as there are) laws against such conduct by the government. See, <i>e. g.,</i> <span class="citation no-link">50 U. S. C. § 403-7</span> (1994 ed., Supp. IV) (prohibiting the "Intelligence Community[`s]" use of journalists as agents). That, however, is immaterial for Fourth Amendment purposes, for "<i>however strongly</i> a defendant may trust an apparent colleague, his expectations in this respect are not protected by the Fourth Amendment when it turns out that the colleague is a government agent regularly communicating with the authorities." <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#749" aria-description="Citation for case: United States v. White">401 U. S. 745, 749</a></span> (1971) (emphasis added). The <i><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span></i> line of cases, I may note, does not distinguish between operations meant to catch a criminal in the act, and those meant only to gather evidence of prior wrongdoing. See, <i>e. g., </i><i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#440" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 440-443</a></span> (1976); cf. <i>Illinois</i> v. <i>Perkins,</i>  <span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/#298" aria-description="Citation for case: Illinois v. Perkins">496 U. S. 292, 298</a></span> (1990) (relying on <i>Hoffa</i> in holding the <span class="star-pagination">*95</span> <i>Miranda</i> rule did not require suppression of an inmate confession given an agent posing as a fellow prisoner).</p>
<p>Until today, we have <i>never</i> heldor even suggestedthat material which a person voluntarily entrusts to someone else cannot be given by that person to the police, and used for whatever evidence it may contain.<sup>[2]</sup> Without so much as discussing the point, the Court today opens a hole in our Fourth Amendment jurisprudence, the size and shape of which is entirely indeterminate. Today's holding would be remarkable enough if the confidential relationship violated by the police conduct were at least one protected by state law. It would be surprising to learn, for example, that in a State which recognizes a spousal evidentiary privilege the police cannot use evidence obtained from a cooperating husband or wife. But today's holding goes even beyond that, since there does not exist any physician-patient privilege in South Carolina. See, <i>e. g., </i><i>Peagler</i> v. <i>Atlantic Coast R. R. Co.,</i> 232 S. C. 274, <span class="citation" data-id="1327281"><a href="/opinion/1327281/peagler-v-atlantic-coast-line-railroad/" aria-description="Citation for case: Peagler v. Atlantic Coast Line Railroad">101 S. E. 2d 821</a></span> (1958). Since the Court declines even to discuss the issue, it leaves law enforcement officials entirely in the dark as to when they can use incriminating evidence obtained from "trusted" sources.<sup>[3]</sup> Presumably the <span class="star-pagination">*96</span> lines will be drawn in the case-by-case development of a whole new branch of Fourth Amendment jurisprudence, taking yet another social judgment (which confidential relationships ought not be invaded by the police) out of democratic control, and confiding it to the uncontrolled judgment of this Courtuncontrolled because there is no common-law precedent to guide it. I would adhere to our established law, which says that information obtained through violation of a relationship of trust is obtained consensually, and is hence not a search.<sup>[4]</sup></p>
<p><span class="star-pagination">*97</span> There remains to be considered the first possible basis for invalidating this search, which is that the patients were coerced to produce their urine samples by their necessitous circumstances, to wit, their need for medical treatment of their pregnancy. If that was coercion, it was not coercion applied by the governmentand if such nongovernmental coercion sufficed, the police would never be permitted to use the ballistic evidence obtained from treatment of a patient with a bullet wound. And the Fourth Amendment would invalidate those many state laws that require physicians to report gunshot wounds,<sup>[5]</sup> evidence of spousal abuse,<sup>[6]</sup> and (like the South Carolina law relevant here, see S. C. Code Ann. § 20-7-510 (2000)) evidence of child abuse.<sup>[7]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*98</span> II</h2>
<p>I think it clear, therefore, that there is no basis for saying that obtaining of the urine sample was unconstitutional. The special-needs doctrine is thus quite irrelevant, since it operates only to validate searches and seizures that are otherwise unlawful. In the ensuing discussion, however, I shall assume (contrary to legal precedent) that the taking of the urine sample was (either because of the patients' necessitous circumstances, or because of failure to disclose that the urine would be tested for drugs, or because of failure to disclose that the results of the test would be given to the police) coerced. Indeed, I shall even assume (contrary to common sense) that the testing of the urine constituted an unconsented search of the patients' effects. On those assumptions, the special-needs doctrine <i>would</i> become relevant; and, properly applied, would validate what was done here.</p>
<p>The conclusion of the Court that the special-needs doctrine is inapplicable rests upon its contention that respondents "undert[ook] to obtain [drug] evidence from their patients" not for any medical purpose, but "<i>for the specific purpose of incriminating those patients.</i> " <i>Ante,</i> at 85 (emphasis in original). In other words, the purported medical rationale was merely a pretext; there was no special need. See <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#621" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 621, n. 5</a></span> (1989). This contention contradicts the District Court's finding of fact that the goal of the testing policy "was not to arrest patients but to facilitate their treatment and protect both the mother and unborn child." App. to Pet. for Cert. A-38.<sup>[8]</sup> This finding is binding upon us unless clearly erroneous, <span class="star-pagination">*99</span> see Fed. Rule Civ. Proc. 52(a). Not only do I find it supportable; I think any other finding would have to be overturned.</p>
<p>The cocaine tests started in April 1989, <i>neither at police suggestion nor with police involvement.</i> Expectant mothers who tested positive were referred by hospital staff for substance-abuse treatment, <i>ante,</i> at 70 (opinion of the Court)an obvious health benefit to both mother and child. See App. 43 (testimony that a single use of cocaine can cause fetal damage). And, since "[i]nfants whose mothers abuse cocaine during pregnancy are born with a wide variety of physical and neurological abnormalities," <i>ante,</i> at 89 (Kennedy, J., concurring in judgment), which require medical attention, see Brief in Opposition A76-A77, the tests were of additional medical benefit in predicting needed postnatal treatment for the child. Thus, in their originbefore the police were in any way involvedthe tests had an immediate, not merely an "ultimate," <i>ante,</i> at 82 (opinion of the Court), purpose of improving maternal and infant health. Several months after the testing had been initiated, a nurse discovered that local police were arresting pregnant users of cocaine for child abuse, the hospital's general counsel wrote the county solicitor to ask "what, if anything, our Medical Center needs to do to assist you in this matter," App. 499 (South Carolina law requires child abuse to be reported, see S. C. Code Ann. § 20-7-510), the police suggested ways to avoid tainting evidence, and the hospital and police in conjunction used the testing program as a means of securing what the Court calls the "ultimate" health benefit of coercing drug-abusing mothers into drug treatment. See <i>ante,</i> at 70-73, 82. Why would there be any reason to believe that, once <span class="star-pagination">*100</span> this policy of using the drug tests for their "ultimate" health benefits had been adopted, use of them for their original, <i>immediate,</i> benefits somehow disappeared, and testing somehow became in its entirety nothing more than a "pretext" for obtaining grounds for arrest? On the face of it, this is incredible. The only evidence of the exclusively arrestrelated purpose of the testing adduced by the Court is that the police-cooperation policy <i>itself</i> does not describe how to care for cocaine-exposed infants. See <i>ante,</i> at 73, 82. But <i>of course</i> it does not, since that policy, adopted months after the cocaine testing was initiated, had as its only health object the "ultimate" goal of inducing drug treatment through threat of arrest. Does the Court really believe (or even <i>hope</i> ) that, once invalidation of the program challenged here has been decreed, drug testing will cease?</p>
<p>In sum, there can be no basis for the Court's purported ability to "distinguis[h] this case from circumstances in which physicians or psychologists, in the course of ordinary medical procedures aimed at helping the patient herself, come across information that . . . is subject to reporting requirements," <i>ante,</i> at 80-81, unless it is this: That the <i>addition</i> of a lawenforcement-related purpose <i>to</i> a legitimate medical purpose destroys applicability of the "special-needs" doctrine. But that is quite impossible, since the special-needs doctrine was developed, and is ordinarily employed, precisely to enable searches <i>by law enforcement officials</i> who, of course, ordinarily have a law enforcement objective. Thus, in <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987), a probation officer received a tip from a detective that petitioner, a felon on probation, possessed a firearm. Accompanied by police, he conducted a warrantless search of petitioner's home. The weapon was found and used as evidence in the probationer's trial for unlawful possession of a firearm. See <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#870" aria-description="Citation for case: Griffin v. Wisconsin"><i>id.,</i> at 870-872</a></span>. Affirming denial of a motion to suppress, we concluded that the "special need" of assuring compliance with terms of release <span class="star-pagination">*101</span> justified a warrantless search of petitioner's home. Notably, we observed that a probation officer is not</p>
<blockquote>"the police officer who normally conducts searches against the ordinary citizen. He is an employee of the State Department of Health and Social Services who, while assuredly charged with protecting the public interest, is also supposed to have in mind the welfare of the probationer . . . . In such a setting, we think it reasonable to dispense with the warrant requirement." <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#876" aria-description="Citation for case: Griffin v. Wisconsin"><i>Id.,</i> at 876-877</a></span>.</blockquote>
<p>Like the probation officer, the doctors here do not "ordinarily conduc[t] searches against the ordinary citizen," and they are "supposed to have in mind the welfare of the [mother and child]." That they have in mind in addition the provision of evidence to the police should make no difference. The Court suggests that if police involvement in this case was in some way incidental and after-the-fact, that would make a difference in the outcome. See <i>ante,</i> at 80-84. But in <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>,</i>  even more than here, police were involved in the search from the very beginning; indeed, the initial tip about the gun came from a detective. Under the factors relied upon by the Court, the use of evidence approved in <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> would have been permitted only if the parole officer had been untrained in chain-of-custody procedures, had not known of the possibility a gun was present, and had been unaccompanied by police when he simply happened upon the weapon. Why any or all of these is constitutionally significant is baffling.</p>
<p>Petitioners seek to distinguish <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> by observing that probationers enjoy a lesser expectation of privacy than does the general public. That is irrelevant to the point I make here, which is that the presence of a law enforcement purpose does not render the special-needs doctrine inapplicable. In any event, I doubt whether Griffin's reasonable expectation of privacy in his home was any less than petitioners' reasonable expectation of privacy in their urine taken, <span class="star-pagination">*102</span> or in the urine tests performed, in a hospitalespecially in a State such as South Carolina, which recognizes no physician-patient testimonial privilege and requires the physician's duty of confidentiality to yield to public policy, see <i>McCormick</i> v. <i>England,</i> 328 S. C. 627, 633, 640-642, <span class="citation" data-id="1357541"><a href="/opinion/1357541/mccormick-v-england/#434" aria-description="Citation for case: McCormick v. England">494 S. E. 2d 431, 434, 438-439</a></span> (App. 1997); and which requires medical conditions that indicate a violation of the law to be reported to authorities, see, <i>e. g.,</i> S. C. Code Ann. § 20-7-510 (2000) (child abuse). Cf. <i>Whalen</i> v. <i>Roe,</i> <span class="citation" data-id="9426661"><a href="/opinion/109592/whalen-v-roe/#597" aria-description="Citation for case: Whalen v. Roe">429 U. S. 589, 597-598</a></span> (1977) (privacy interest does not forbid government to require hospitals to provide, for law enforcement purposes, names of patients receiving prescriptions of frequently abused drugs).</p>
<p>The concurrence makes essentially the same basic error as the Court, though it puts the point somewhat differently: "The special needs cases we have decided," it says, "do not sustain the active use of law enforcement . . . as an integral part of a program which seeks to achieve legitimate, civil objectives." <i>Ante,</i> at 88. <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> shows that is not true. Indeed, <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> shows that there is not even any truth in the more limited proposition that our cases do not support application of the special-needs exception where the "legitimate, civil objectives" are sought only <i>through</i> the use of law enforcement means. (Surely the parole officer in <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i>  was using threat of reincarceration to assure compliance with parole.) But even if this latter proposition <i>were</i> true, it would invalidate what occurred here only if the drug testing sought exclusively the "ultimate" health benefits achieved by coercing the mothers into drug treatment through threat of prosecution. But in fact the drug testing sought, independently of law enforcement involvement, the "immediate" health benefits of identifying drug-impaired mother and child for necessary medical treatment. The concurrence concedes that if the testing is conducted for medical reasons, the fact that "prosecuting authorities <i>then</i> adopt legitimate procedures to discover this information and prosecution follows <span class="star-pagination">*103</span>. . . ought not to invalidate the testing." <i>Ante,</i> at 90 (emphasis added). But here the police involvement in each case did <i>take place after</i> the testing was conducted for independent reasons. Surely the concurrence cannot mean that no police-suggested procedures (such as preserving the chain of custody of the urine sample) can be applied until <i>after</i> the testing; or that the police-suggested procedures must have been <i>designed</i> after the testing. The facts in <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> (and common sense) show that this cannot be so. It seems to me that the only real distinction between what the concurrence must reasonably be thought to be approving, and what we have here, is that here the police took the lesser step of initially <i>threatening</i> prosecution rather than bringing it.</p>
<p></p>
<h2>* * *</h2>
<p>As I indicated at the outset, it is not the function of this Courtat least not in Fourth Amendment casesto weigh petitioners' privacy interest against the State's interest in meeting the crisis of "crack babies" that developed in the late 1980's. I cannot refrain from observing, however, that the outcome of a wise weighing of those interests is by no means clear. The initial goal of the doctors and nurses who conducted cocaine testing in this case was to refer pregnant drug addicts to treatment centers, and to prepare for necessary treatment of their possibly affected children. When the doctors and nurses agreed to the program providing test results to the police, they did so because (in addition to the fact that child abuse was required by law to be reported) they wanted to use the sanction of arrest as a strong incentive for their addicted patients to undertake drug-addiction treatment. And the police themselves used it for that benign purpose, as is shown by the fact that only 30 of 253 women testing positive for cocaine were ever arrested, and only 2 of those prosecuted. See App. 1125-1126. It would not be unreasonable to conclude that today's judgment, authorizing the assessment of damages against the county <span class="star-pagination">*104</span> solicitor and individual doctors and nurses who participated in the program, proves once again that no good deed goes unpunished.</p>
<p>But as far as the Fourth Amendment is concerned: There was no unconsented search in this case. And if there was, it would have been validated by the special-needs doctrine. For these reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the American Civil Liberties Union et al. by <i>Julie E. Sternberg, Steven R. Shapiro, Sara L. Mandelbaum, Catherine Weiss, Louise Melling, Louis M. Bograd, Martha F. Davis, Yolanda S. Wu,</i> and <i>Roslyn Powell;</i> for the American Medical Association by <i>Michael Ile, Anne Murphy,</i> and <i>Leonard Nelson;</i> for the American Public Health Association et al. by <i>Daniel N. Abrahamson</i>  and <i>David T. Goldberg;</i> for the NARAL Foundation et al. by <i>Nancy L. Perkins</i> and <i>Jodi Michael;</i> for the National Coalition for Child Protection Reform et al. by <i>Carolyn A. Kubitschek;</i> and for the Rutherford Institute by <i>John W. Whitehead</i> and <i>Steven H. Aden.</i> </p>
<p>[1]  As several witnesses testified at trial, the problem of "crack babies" was widely perceived in the late 1980's as a national epidemic, prompting considerable concern both in the medical community and among the general populace.</p>
<p>[2]  Under South Carolina law, a viable fetus has historically been regarded as a person; in 1995, the South Carolina Supreme Court held that the ingestion of cocaine during the third trimester of pregnancy constitutes criminal child neglect. <i>Whitner</i> v. <i>South Carolina,</i> 328 S. C. 1, <span class="citation" data-id="9615087"><a href="/opinion/1388496/whitner-v-state/" aria-description="Citation for case: Whitner v. State">492 S. E. 2d 777</a></span> (1995), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./523/1145/">523 U. S. 1145</a></span> (1998).</p>
<p>[3]  In his letter dated August 23, 1989, Good wrote: "Please advise us if your office is anticipating future criminal action and what if anything our Medical Center needs to do to assist you in this matter." App. to Pet. for Cert. A-67.</p>
<p>[4]  Those criteria were as follows:
</p>
<p>"1. No prenatal care</p>
<p>"2. Late prenatal care after 24 weeks gestation</p>
<p>"3. Incomplete prenatal care</p>
<p>"4. Abruptio placentae</p>
<p>"5. Intrauterine fetal death</p>
<p>"6. Preterm labor `of no obvious cause'</p>
<p>"7. IUGR [intrauterine growth retardation] `of no obvious cause'</p>
<p>"8. Previously known drug or alcohol abuse</p>
<p>"9. Unexplained congenital anomalies." <i>Id.,</i> at A-53 to A-54.</p>
<p>[5]  Despite the conditional description of the first category, when the policy was in its initial stages, a positive test was immediately reported to the police, who then promptly arrested the patient.</p>
<p>[6]  The instructions read: "THERE WERE NO SEARCH WARRANTS ISSUED BY A MAGISTRATE OR ANY OTHER PROPER JUDICIAL OFFICER TO PERMIT THESE URINE SCREENS TO BE TAKEN. THERE NOT BEING A WARRANT ISSUED, THEY ARE UNREASONABLE AND IN VIOLATION OF THE CONSTITUTION OF THE UNITED STATES, UNLESS THE DEFENDANTS HAVE SHOWN BY THE GREATER WEIGHT OR PREPONDERANCE OF THE EVIDENCE THAT THE PLAINTIFFS CONSENTED TO THOSE SEARCHES." App. 1314-1315. Under the judge's instructions, in order to find that the plaintiffs had consented to the searches, it was necessary for the jury to find that they had consented to the taking of the samples, to the testing for evidence of cocaine, and to the possible disclosure of the test results to the police. Respondents have not argued, as Justice Scalia does, that it is permissible for members of the staff of a public hospital to use diagnostic tests "deceivingly" to obtain incriminating evidence from their patients. See <i>post,</i> at 94 (dissenting opinion).</p>
<p>[7]  The term "special needs" first appeared in Justice Blackmun's opinion concurring in the judgment in <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 351</a></span> (1985). In his concurrence, Justice Blackmun agreed with the Court that there are limited exceptions to the probable-cause requirement, in which reasonableness is determined by "a careful balancing of governmental and private interests," but concluded that such a test should only be applied "in those exceptional circumstances in which special needs, beyond the normal need for law enforcement, make the warrant and probablecause requirement impracticable . . . ." <i><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">Ibid.</a></span></i> This Court subsequently adopted the "special needs" terminology in <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#720" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 720</a></span> (1987) (plurality opinion), and <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987), concluding that, in limited circumstances, a search unsupported by either warrant or probable cause can be constitutional when "special needs" other than the normal need for law enforcement provide sufficient justification. See also <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 652-653</a></span> (1995).</p>
<p>[8]  The majority stated that the District Court had made such a finding. <span class="citation" data-id="6983352"><a href="/opinion/7078423/ferguson-v-city-of-charleston/#477" aria-description="Citation for case: Ferguson v. City of Charleston">186 F. 3d, at 477</a></span>. The text of the relevant finding, made in the context of petitioners' now abandoned Title VI claim, reads as follows: "The policy was applied in all maternity departments at MUSC. Its goal was not to arrest patients but to facilitate their treatment and protect both the mother and unborn child." App. to Pet. for Cert. A-38. That finding, however, must be read in light of this comment by the District Court with respect to the Fourth Amendment claim:
</p>
<p>". . . THESE SEARCHES WERE NOT DONE BY THE MEDICAL UNIVERSITY FOR INDEPENDENT PURPOSES. IF THEY HAD BEEN, THEN THEY WOULD NOT IMPLICATE THE FOURTH AMENDMENT. OBVIOUSLY AS I POINT OUT THERE ON PAGE 4, NORMALLY URINE SCREENS AND BLOOD TESTS AND THAT TYPE OF THING CAN BE TAKEN BY HEALTH CARE PROVIDERS WITHOUT HAVING TO WORRY ABOUT THE FOURTH AMENDMENT. THE ONLY REASON THE FOURTH AMENDMENT IS IMPLICATED HERE IS THAT THE POLICE CAME IN AND THERE WAS AN AGREEMENT REACHED THAT THE POSITIVE SCREENS WOULD BE SHARED WITH THE POLICE. AND THEN THE SCREEN IS NOT DONE INDEPENDENT OF POLICE, IT'S DONE IN CONJUNCTION WITH THE POLICE AND THAT IMPLICATES THE FOURTH AMENDMENT." App. 1248-1249.</p>
<p>[9]  In arguing that the urine tests at issue were not searches, the dissent attempts to disaggregate the taking and testing of the urine sample from the reporting of the results to the police. See <i>post,</i> at 92. However, in our special needs cases, we have routinely treated urine screens taken by state agents as searches within the meaning of the Fourth Amendment even though the results were not reported to the police, see, <i>e. g., </i><i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/" aria-description="Citation for case: Chandler v. Miller">520 U. S. 305</a></span> (1997); <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995); <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 617</a></span> (1989); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), and respondents here do not contend that the tests were not searches. Rather, they argue that the searches were justified by consent and/or by special needs.</p>
<p>[10]  In a footnote to their brief, respondents do argue that the searches were not entirely suspicionless. Brief for Respondents 23, n. 13. They do not, however, point to any evidence in the record indicating that any of the nine search criteria was more apt to be caused by cocaine use than by some other factor, such as malnutrition, illness, or indigency. More significantly, their legal argument and the reasoning of the majority panel opinion rest on the premise that the policy would be valid even if the tests were conducted randomly.</p>
<p>[11]  The dissent would have us do otherwise and resolve the issue of consent in favor of respondents. Because the Court of Appeals did not discuss this issue, we think it more prudent to allow that court to resolve the legal and factual issues in the first instance, and we express no view on those issues. See, <i>e. g., </i><i>Glover</i> v. <i>United States,</i> <span class="citation" data-id="118397"><a href="/opinion/118397/glover-v-united-states/" aria-description="Citation for case: Glover v. United States">531 U. S. 198</a></span> (2001); <i>National Collegiate Athletic Assn.</i> v. <i>Smith,</i> <span class="citation" data-id="118263"><a href="/opinion/118263/national-collegiate-athletic-assn-v-smith/#470" aria-description="Citation for case: National Collegiate Athletic Assn. v. Smith">525 U. S. 459, 470</a></span> (1999).</p>
<p>[12]  <i>Chandler,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#312" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 312, 318</a></span>; <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>; <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#621" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 621, n. 5, 622, n. 6</a></span>; <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#663" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 663, 666-667, 672, n. 2</a></span>.</p>
<p>[13]  There are some circumstances in which state hospital employees, like other citizens, may have a duty to provide law enforcement officials with evidence of criminal conduct acquired in the course of routine treatment, see, <i>e. g.,</i> S. C. Code Ann. § 20-7-510 (2000) (physicians and nurses required to report to child welfare agency or law enforcement authority "when in the person's professional capacity the person" receives information that a child has been abused or neglected). While the existence of such laws might lead a patient to expect that members of the hospital staff might turn over evidence acquired in the course of treatment to which the patient had consented, they surely would not lead a patient to anticipate that hospital staff would intentionally set out to obtain incriminating evidence from their patients for law enforcement purposes.</p>
<p>[14]  In fact, we have previously recognized that an intrusion on that expectation may have adverse consequences because it may deter patients from receiving needed medical care. <i>Whalen</i> v. <i>Roe,</i> <span class="citation" data-id="9426661"><a href="/opinion/109592/whalen-v-roe/#599" aria-description="Citation for case: Whalen v. Roe">429 U. S. 589, 599-600</a></span> (1977). Cf<i>.</i> Poland, Dombrowski, Ager, &amp; Sokol, Punishing pregnant drug users: enhancing the flight from care, 31 Drug and Alcohol Dependence 199-203 (1993).</p>
<p>[15]  As The Chief Justice recently noted: "The `special needs' doctrine, which has been used to uphold certain suspicionless searches performed for reasons unrelated to law enforcement, is an exception to the general rule that a search must be based on individualized suspicion of wrongdoing." <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#54" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S. 32, 54</a></span> (2000) (dissenting opinion); see also nn. 16-17, <i>infra.</i> In <i>T. L. O.,</i> we made a point of distinguishing searches "carried out by school authorities acting alone and on their own authority" from those conducted "in conjunction with or at the behest of law enforcement agencies." <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341, n. 7</a></span>.
</p>
<p>The dissent, however, relying on <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987), argues that the special needs doctrine "is ordinarily employe[d], precisely to enable searches <i>by law enforcement officials</i> who, of course, ordinarily have a law enforcement objective." <i>Post,</i> at 100. Viewed in the context of our special needs case law and even viewed in isolation, <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> does not support the proposition for which the dissent invokes it. In other special needs cases, we have tolerated suspension of the Fourth Amendment's warrant or probable-cause requirement in part because there was no law enforcement purpose behind the searches in those cases, and there was little, if any, entanglement with law enforcement. See <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#620" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 620-621</a></span>; <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 665-666</a></span>; <i>Acton,</i>  <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>. Moreover, <i>after</i> our decision in <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>,</i> we reserved the question whether "routine use in criminal prosecutions of evidence obtained pursuant to the administrative scheme would give rise to an inference of pretext, or otherwise impugn the administrative nature of the . . . program." <i>Skinner,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#621" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 621, n. 5</a></span>. In <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> itself, this Court noted that "[a]lthough a probation officer is not an impartial magistrate, neither is he the police officer who normally conducts searches against the ordinary citizen." <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#876" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 876</a></span>. Finally, we agree with petitioners that <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span></i> is properly read as limited by the fact that probationers have a lesser expectation of privacy than the public at large. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#874" aria-description="Citation for case: Griffin v. Wisconsin"><i>Id.,</i> at 874-875</a></span>.</p>
<p>[16]  In <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989), this Court noted that "[t]he FRA has prescribed toxicological tests, not to assist in the prosecution of employees, but rather `to prevent accidents and casualties in railroad operations that result from impairment of employees by alcohol or drugs.' " <i><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Id.,</a></span></i> at 620-621 (quoting <span class="citation no-link">49 CFR § 219.1</span>(a) (1987)). Similarly, in <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989), we concluded that it was "clear that the Customs Service's drugtesting program is not designed to serve the ordinary needs of law enforcement. Test results may not be used in a criminal prosecution of the employee without the employee's consent." <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><i>Id.,</i> at 665-666</a></span>. In the same vein, in <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#658" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S., at 658</a></span>, we relied in part on the fact that "the results of the tests are disclosed only to a limited class of school personnel who have a need to know; and they are not turned over to law enforcement authorities or used for any internal disciplinary function" in finding the searches reasonable.</p>
<p>[17]  "Today's opinion speaks of a `closely guarded' class of permissible suspicionless searches which must be justified by a `special need.' But this term, as used in <i><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span></i> and <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> and on which the Court now relies, was used in a quite different sense than it is used by the Court today. In <i><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span></i> and <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span></i> it was used to describe a basis for a search apart from the regular needs of law enforcement, <i><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>,</i> [489 U. S.], at 620; <i><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>,</i> [489 U. S.], at 669. The `special needs' inquiry as delineated there has not required especially great `importan[ce],' [520 U. S.], at 318, unless one considers `the supervision of probationers,' or the `operation of a government office,' <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#620" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 620</a></span>, to be especially `important.' Under our precedents, if there was a proper governmental purpose other than law enforcement, there was a `special need,' and the Fourth Amendment then required the familiar balancing between that interest and the individual's privacy interest." <i>Chandler</i> v. <i>Miller,</i> <span class="citation" data-id="9433438"><a href="/opinion/118100/chandler-v-miller/#325" aria-description="Citation for case: Chandler v. Miller">520 U. S., at 325</a></span> (Rehnquist, C. J., dissenting).</p>
<p>[18]  Our emphasis on this distinction should make it clear that, contrary to the hyperbole in the dissent, we do not view these reporting requirements as "clearly bad." See <i>post,</i> at 95-96, n. 3. Those requirements are simply not in issue here.</p>
<p>[19]  Accordingly, the police organized a meeting with the staff of the police and hospital laboratory staffs, as well as Nurse Brown, in which the police went over the concept of a chain of custody system with the MUSC staff. App. 1052-1053.</p>
<p>[20]  We italicize those words lest our reasoning be misunderstood. See <i>post,</i> at 86-88 (Kennedy, J., concurring in judgment). In none of our previous special needs cases have we upheld the collection of evidence for criminal law enforcement purposes. Our essential point is the same as Justice Kennedy'sthe extensive entanglement of law enforcement cannot be justified by reference to legitimate needs.
</p>
<p>According to the dissent, the fact that MUSC performed tests prior to the development of Policy M-7 should immunize any subsequent testing policy despite the presence of a law enforcement purpose and extensive law enforcement involvement. See <i>post,</i> at 98-100. To say that any therapeutic purpose did not disappear is simply to miss the point. What matters is that under the new policy developed by the solicitor's office and MUSC, law enforcement involvement was the means by which that therapeutic purpose was to be met. Policy M-7 was, at its core, predicated on the use of law enforcement. The extensive involvement of law enforcement and the threat of prosecution were, as respondents admitted, essential to the program's success.</p>
<p>[21]  Accordingly, this case differs from <i>New York</i> v. <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/" aria-description="Citation for case: New York v. Burger">482 U. S. 691</a></span> (1987), in which the Court upheld a scheme in which police officers were used to carry out administrative inspections of vehicle dismantling businesses. That case involved an industry in which the expectation of privacy in commercial premises was "particularly attenuated" given the extent to which the industry in question was closely regulated. <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#700" aria-description="Citation for case: New York v. Burger"><i>Id.,</i> at 700</a></span>. More important for our purposes, the Court relied on the "plain administrative purposes" of the scheme to reject the contention that the statute was in fact "designed to gather evidence to enable convictions under the penal laws . . . ." <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#715" aria-description="Citation for case: New York v. Burger"><i>Id.,</i> at 715</a></span>. The discovery of evidence of other violations would have been merely incidental to the purposes of the administrative search. In contrast, in this case, the policy was specifically designed to gather evidence of violations of penal laws.
</p>
<p>This case also differs from the handful of seizure cases in which we have applied a balancing test to determine Fourth Amendment reasonableness. See, <i>e. g., </i><i>Michigan Dept. of State Police</i> v. <i>Sitz,</i> <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/#455" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444, 455</a></span> (1990); <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976). First, those cases involved roadblock seizures, rather than "the intrusive search of the body or the home." See <i>Indianapolis</i> v. <i>Edmond,</i> <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#54" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U. S., at 54-55</a></span> (Rehnquist, C. J., dissenting); <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 561</a></span> ("[W]e deal neither with searches nor with the sanctity of private dwellings, ordinarily afforded the most stringent Fourth Amendment protection"). Second, the Court explicitly distinguished the cases dealing with checkpoints from those dealing with "special needs." <i><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">Sitz</a></span>,</i> 496 U. S.,at 450.</p>
<p>[22]  Thus, under respondents' approach, any search to generate evidence for use by the police in enforcing general criminal laws would be justified by reference to the broad social benefits that those laws might bring about (or, put another way, the social harms that they might prevent).</p>
<p>[23]  It is especially difficult to argue that the program here was designed simply to save lives. <i>Amici</i> claim a near consensus in the medical community that programs of the sort at issue, by discouraging women who use drugs from seeking prenatal care, harm, rather than advance, the cause of prenatal health. See Brief for American Medical Association as <i>Amicus Curiae</i> 6-22; Brief for American Public Health Association et al. as <i>Amici Curiae</i> 17-21; Brief for NARAL Foundation et al. as <i>Amici Curiae</i> 18-19.</p>
<p>[24]  In fact, some MUSC staff made this distinction themselves. See Pl. Exh. No. 14, Hulsey, 11-17-89, Coke Committee, 1-2 ("The use of medically indicated tests for substance abuse, obtained in conventional manners, must be distinguished from mandatory screening and collection of evidence using such methods as chain of custody, etc. . . . The question is raised as to whether pediatricians should function as law enforcement officials. While the reporting of criminal activity to appropriate authorities may be required and/or ethically just, the active pursuit of evidence to be used against individuals presenting for medical care may not be proper").
</p>
<p>The dissent, however, mischaracterizes our opinion as holding that "material which a person voluntarily entrusts to someone else cannot be given by that person to the police, and used for whatever evidence it may contain." <i>Post,</i> at 95. But, as we have noted elsewhere, given the posture of the case, we must assume for purposes of decision that the patients did <i>not</i> consent to the searches, and we leave the question of consent for the Court of Appeals to determine. See n. 11<i>, supra.</i> </p>
<p>The dissent further argues that our holding "leaves law enforcement officials entirely in the dark as to when they can use incriminating evidence obtained from `trusted' sources." See <i>post,</i> at 95. With all due respect, we disagree. We do not address a case in which doctors independently complied with reporting requirements. Rather, as we point out above, in this case, medical personnel used the criteria set out in n. <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">4, <i>supra,</i></a></span> to collect evidence for law enforcement purposes, and law enforcement officers were extensively involved in the initiation, design, and implementation of the program. In such circumstances, the Fourth Amendment's general prohibition against nonconsensual, warrantless, and suspicionless searches applies in the absence of consent. We decline to accept the dissent's invitation to make a foray into dicta and address other situations not before us.</p>
<p>[1]  The Court asserts that it is improper to "disaggregate the taking and testing of the urine sample from the reporting of the results to the police," because "in our special needs cases, we have routinely treated urine screens taken by state agents as searches within the meaning of the Fourth Amendment." <i>Ante,</i> at 76, n. 9. But in all of those cases, the urine was obtained involuntarily. See <i>Chandler</i> v. <i>Miller,</i> 520 U. S.305 (1997); <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646</a></span> (1995); <i>Skinner</i>  v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989); <i>Treasury Employees</i> v. <i>Von Raab,</i> <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656</a></span> (1989). Where the taking of the urine sample is unconsented (and thus a Fourth Amendment search), the subsequent testing and reporting of the results to the police are obviously part of (or infected by) the same search; but where, as here, the taking of the sample was not a Fourth Amendment search, it is necessary to consider separately whether the testing and reporting were.</p>
<p>[2]  <i><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span></i> did say that the Fourth Amendment can be violated by "guileful as well as by forcible intrusions into a constitutionally protected area." 385 U. S.,at 301. The case it cited for that proposition, however, shows what it meant: <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921),found a Fourth Amendment violation where a Government agent who had obtained access to the defendant's office on pretext of a social visit carried away private papers. "Guile" (rather than force) had been used to <i>go beyond the scope of the consented access to evidence.</i> Whereas the search in <i><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span></i> was invalidated, the search was approved in <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">385 U. S. 206</a></span> (1966), where an equally guileful agent stayed within the bounds of the access to defendant's home, carrying away only a package of drugs that had been voluntarily provided.</p>
<p>[3]  The Court contends that its opinion does not leave law enforcement officials in the dark as to when they can use incriminating evidence from trusted sources, since it "do[es] not address a case in which doctors independently complied with reporting requirements," <i>ante,</i> at 85, n.24<i>.</i> I find it hard to understand how not addressing that point fails to leave it enshrouded in darknessunless the Court means that such reporting requirements are clearly bad. (If voluntary betrayal of a trust in mere <i>cooperation</i> with the police constitutes a Fourth Amendment search, surely betrayal of a trust <i>at the direction</i> of the legislature must be.) But in any event, reporting requirements are an infinitesimal part of the problem. What about a doctor'sor a spouse'svoluntary provision of information to the police, without the compulsion of a statute?</p>
<p>[4]  The Court contends that I am "mischaracteriz[ing]" its opinion, since the Court is merely "assum[ing] for purposes of decision that the patients did <i>not</i> consent to the searches, and [leaves] the question of consent for the Court of Appeals to determine." <i><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/" aria-description="Citation for case: Lewis v. United States">Ibid.</a></span></i> That is not responsive. The "question of consent" that the Court leaves open is whether the patients consented, not merely to the taking of the urine samples, but to the drug testing in particular, and to the provision of the results to the police. Consent to the taking of the samples aloneor even to the taking of the samples <i>plus</i> the drug testingdoes not suffice. The Court's contention that the question of the sufficiency of that more limited consent is not before us because respondents did not raise it, see <i>ante,</i> at 74, n. 6, is simply mistaken. Part II of respondents' brief, entitled "The Petitioners consented to the searches," argues that "Petitioners . . . freely and voluntarily . . . provided the urine samples"; that "each of the Petitioners signed a consent to treatment form which authorized the MUSC medical staff to conduct all necessary tests of those urine samplesincluding drug tests"; and that "[t]here is no precedent in this Court's Fourth Amendment search and seizure jurisprudence which imposes any . . . requirement that the searching agency inform the consenting party that the results of the search will be turned over to law enforcement." Brief for Respondents 38-39. The brief specifically <i>takes issue</i> with the District Court's charge to the jurywhich the Court chooses to accept as an unexaminable "given," see <i>ante,</i> at 74, n. 6that "the Respondents were required to show that the Petitioners consented to MUSC disclosing the information to law enforcement." Brief for Respondents 39.
</p>
<p>In sum, I think it clear that the Court's disposition requires the holding that violation of a relationship of trust constitutes a search. The opinion itself implies that in its description of the issue left for the Court of Appeals on remand, see <i>ante,</i> at 77, n. 11: whether "the tests were performed without the <i>informed</i> consent of the patients," <i>ante,</i> at 77 (emphasis added)informed, that is, that the urine would be tested for drugs and that the results would be given to the police<i>.</i> I am happy, of course, to accept the Court's illogical assurance that it intends no such holding, and urge the Court of Appeals on remand to do the same.</p>
<p>[5]  See, <i>e. g.,</i> Cal. Penal Code Ann. § 11160 (West Supp. 2001); N. Y. Penal Law § 265.25 (McKinney 2000); S. C. Code Ann. § 16-3-1072 (Supp. 2000).</p>
<p>[6]  See, <i>e. g.,</i> Cal. Penal Code Ann. § 11160 (West Supp. 2001); <span class="citation no-link">Colo. Rev. Stat. § 12-36-135</span> (2000).</p>
<p>[7]  The Court contends that I "would have us . . . resolve the issue of consent in favor of respondents," whereas the Court's opinion "more prudent[ly] allow[s] [the Court of Appeals] to resolve the legal and factual issues in the first instance, and . . . express[es] no view on those issues." <i>Ante,</i> at 77, n. 11. That is not entirely so. The Court does not resolve the factual issue whether there was consent to the drug testing and to providing the results to the police; and neither do I. But the Court <i>does</i>  resolve the legal issue whether <i>that</i> consent was necessary, see <i>ante,</i> at 77, 84-85, and n. 24; and so do I. Since the Court concludes it was necessary, the factual inquiry is left for the Fourth Circuit on remand. Since I conclude it was not necessary (and since no one contends that the taking of the urine sample was unconsented), there is on my analysis no factual consent issue remaining.</p>
<p>[8]  The Court believes that this finding "must be read in light of" the District Court's comment that "`these searches were not done by the medical university for independent purposes. . . . [T]he police came in and there was an agreement reached that the positive screens would be shared with the police. And then the screen is not done independent of police, it'sdone in conjunction with the police and that implicates the Fourth Amendment.' " <i>Ante,</i> at 75, n. 8, quoting App. 1247-1249. But all this shows is that the explicit finding of medical purpose was not a finding of <i>exclusive</i> medical purpose. As discussed later in text, the special-needs doctrine contains no such exclusivity requirement.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Fernandez v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Fernandez v. California"
type: case
citation: ""
parallel_cite: "134 S. Ct. 1126; 188 L. Ed. 2d 25; 82 U.S.L.W. 4102; 571 U.S. 292; 24 Fla. L. Weekly Fed. S 553"
neutral_cite: "2014 U.S. LEXIS 1636; 2014 WL 700100"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-02-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-02-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Fernandez v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2654534/fernandez-v-california/"
  cluster_id: 2654534
  opinion_id: 9798884
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Georgia v. Randolph]]", "[[Illinois v. Rodriguez]]", "[[United States v. Matlock]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "co-occupant", "third-party-consent"]
holding: "Randolph is limited to a PHYSICALLY PRESENT objector. Once the objecting occupant is lawfully removed (e.g., by arrest), the remaining…"
lake:
  record_id: Fernandez v. California
  status: verified
  projected_at: 2026-07-06
---

# Fernandez v. California

*571 U.S. 292 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers investigating a robbery followed a suspect to an apartment and heard sounds of a fight inside. Roxanne Rojas answered the door appearing battered. Fernandez stepped forward and told the officers they had no right to enter. The officers arrested him for assaulting Rojas and removed him from the scene; about an hour later they returned and obtained Rojas's consent to search the apartment, where they found gang paraphernalia, a knife, and ammunition tying Fernandez to the robbery.

## Issue
Whether the rule of [[Georgia v. Randolph]] — that a physically present co-occupant's express objection defeats another occupant's consent — bars a search later consented to by the remaining occupant after the objecting occupant has been lawfully removed from the premises by arrest.

## Rule
No. *[[Georgia v. Randolph|Randolph]]*'s objecting-occupant rule operates only while the objector is physically present; once he has been lawfully removed, the consent of the remaining occupant controls. "We therefore hold that an occupant who is absent due to a lawful detention or arrest stands in the same shoes as an occupant who is absent for any other reason." — 571 U.S. at 303. ^pin-303

Read on its own terms, the *[[Georgia v. Randolph|Randolph]]* "holding unequivocally requires the presence of the objecting occupant in every situation other than the one mentioned in the dictum discussed above." — *Id.* ^pin-303a

## Application
Fernandez was not present to object when Rojas consented, because the police had lawfully arrested him for assaulting her and removed him from the apartment. Because his earlier objection did not survive his lawful, objectively justified removal, Rojas's voluntary consent as a co-occupant authorized the search on these facts.

## Conclusion
The warrantless search was reasonable; with the objecting occupant lawfully removed before the remaining occupant consented, *[[Georgia v. Randolph|Randolph]]* did not bar the search, and the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Fernandez* confines [[Georgia v. Randolph]] to a **physically present** objector — it limits *[[Georgia v. Randolph|Randolph]]*'s reach but does not disturb its core rule that a present, objecting co-occupant defeats a co-tenant's consent.

## Appears on
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *Fernandez v. California*, 571 U.S. 292 (2014) — https://www.courtlistener.com/opinion/2654534/fernandez-v-california/ — pinpoint: 303 (cluster 2654534 → lead opinion 9798884).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "01aa426ff1174efe", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Fernandez v. California"}, "payload": {"all": [{"cite": "134 S. Ct. 1126", "page": "1126", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}, {"cite": "188 L. Ed. 2d 25", "page": "25", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "188"}, {"cite": "2014 U.S. LEXIS 1636", "page": "1636", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "82 U.S.L.W. 4102", "page": "4102", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "82"}, {"cite": "571 U.S. 292", "page": "292", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "571"}, {"cite": "24 Fla. L. Weekly Fed. S 553", "page": "553", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "2014 WL 700100", "page": "700100", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2014"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Fernandez v. California"}}
{"assertion_id": "33ceaabe7e2efc14", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-303", "record_id": "Fernandez v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-303", "pinpoint_status": "slip-only", "quote": "--- # Fernandez v. California *571 U.S. 292 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers investigating a robbery followed a suspect to an apartment and heard sounds of a fight inside. Roxanne Rojas answered the door appearing battered. Fernandez stepped forward and told the officers they had no right to enter. The officers arrested him for assaulting Rojas and removed him from the scene; about an hour later they returned and obtained Rojas's consent to search the apartment, where they found gang paraphernalia, a knife, and ammunition tying Fernandez to the robbery. ## Issue Whether the rule of [[Georgia v. Randolph]] — that a physically present co-occupant's express objection defeats another occupant's consent — bars a search later consented to by the remaining occupant after the objecting occupant has been lawfully removed from the premises by arrest. ## Rule No. *Randolph*'s objecting-occupant rule operates only while the objector is physically present; once he has been lawfully removed, the consent of the remaining occupant controls.", "quote_fidelity": "mismatch", "record_id": "Fernandez v. California", "star_marker": null}}
{"assertion_id": "9324f8ded2d1a751", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-303a", "record_id": "Fernandez v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-303a", "pinpoint_status": "slip-only", "quote": "holding unequivocally requires the presence of the objecting occupant in every situation other than the one mentioned in the dictum discussed above.", "quote_fidelity": "mismatch", "record_id": "Fernandez v. California", "star_marker": null}}
{"assertion_id": "460bdea0f0f1f7aa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Fernandez v. California"}, "payload": {"as_of_content": "2014-02-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Fernandez v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Fernandez v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Fernandez v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Fernandez v. California",
    "case_name_short": "Fernandez",
    "case_name_full": "Walter FERNANDEZ, Petitioner v. CALIFORNIA.",
    "input_case_name": "Fernandez v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-02-25",
    "year": 2014,
    "docket": null,
    "cluster_id": 2654534,
    "lead_opinion_id": 9798884,
    "sibling_ids": [
      2654534,
      9798884,
      9798885,
      9798886
    ],
    "absolute_url": "/opinion/2654534/fernandez-v-california/",
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
        "cite": "134 S. Ct. 1126",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1126",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 25",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "25",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4102",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4102",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "571 U.S. 292",
        "volume": "571",
        "reporter": "U.S.",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 553",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "553",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 1636",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "1636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 700100",
        "volume": "2014",
        "reporter": "WL",
        "page": "700100",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 1126",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "1126",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "188 L. Ed. 2d 25",
        "volume": "188",
        "reporter": "L. Ed. 2d",
        "page": "25",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 1636",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "1636",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4102",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4102",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "571 U.S. 292",
        "volume": "571",
        "reporter": "U.S.",
        "page": "292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 553",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "553",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 WL 700100",
        "volume": "2014",
        "reporter": "WL",
        "page": "700100",
        "type": 7,
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
      "id": "pin-303",
      "page": null,
      "quote": "--- # Fernandez v. California *571 U.S. 292 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers investigating a robbery followed a suspect to an apartment and heard sounds of a fight inside. Roxanne Rojas answered the door appearing battered. Fernandez stepped forward and told the officers they had no right to enter. The officers arrested him for assaulting Rojas and removed him from the scene; about an hour later they returned and obtained Rojas's consent to search the apartment, where they found gang paraphernalia, a knife, and ammunition tying Fernandez to the robbery. ## Issue Whether the rule of [[Georgia v. Randolph]] \u2014 that a physically present co-occupant's express objection defeats another occupant's consent \u2014 bars a search later consented to by the remaining occupant after the objecting occupant has been lawfully removed from the premises by arrest. ## Rule No. *Randolph*'s objecting-occupant rule operates only while the objector is physically present; once he has been lawfully removed, the consent of the remaining occupant controls.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-303a",
      "page": null,
      "quote": "holding unequivocally requires the presence of the objecting occupant in every situation other than the one mentioned in the dictum discussed above.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-02-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Fernandez v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Bodie Witzlib",
          "cluster_id": 2825238,
          "cite": [
            "796 F.3d 799",
            "2015 U.S. App. LEXIS 13811",
            "2015 WL 4664340"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quartavious Davis",
          "cluster_id": 2798570,
          "cite": [
            "785 F.3d 498",
            "2015 WL 2058977"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Byseem T. Coles (070653)",
          "cluster_id": 2674841,
          "cite": [
            "218 N.J. 322",
            "95 A.3d 136",
            "2014 N.J. LEXIS 1079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Michael Lamb (071262)",
          "cluster_id": 2674840,
          "cite": [
            "218 N.J. 300",
            "95 A.3d 123",
            "2014 N.J. LEXIS 1078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Harris",
          "cluster_id": 2780548,
          "cite": [
            "234 Cal. App. 4th 671",
            "184 Cal. Rptr. 3d 198",
            "2015 Cal. App. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Richard",
          "cluster_id": 2723972,
          "cite": [
            "300 Kan. 715",
            "333 P.3d 179",
            "2014 Kan. LEXIS 498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 8443247,
          "cite": [
            "854 F.3d 197",
            "2017 WL 1379188",
            "2017 U.S. App. LEXIS 6579"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lange v. California",
          "cluster_id": 4894054,
          "cite": [
            "594 U.S. 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Luis W. Lebron v. Secretary of the Florida Department of Children and Families",
          "cluster_id": 2756970,
          "cite": [
            "772 F.3d 1352",
            "96 Fed. R. Serv. 113",
            "2014 U.S. App. LEXIS 22815",
            "2014 WL 6782734"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. Commonwealth",
          "cluster_id": 2959682,
          "cite": [
            "776 S.E.2d 760",
            "290 Va. 277",
            "2015 Va. LEXIS 115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kamaal Mallory",
          "cluster_id": 2723305,
          "cite": [
            "765 F.3d 373",
            "2014 U.S. App. LEXIS 17228",
            "2014 WL 4347198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
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
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fine v. ESPN, Inc.",
          "cluster_id": 7305676,
          "cite": [
            "11 F. Supp. 3d 209",
            "42 Media L. Rep. (BNA) 1564",
            "2014 U.S. Dist. LEXIS 44533",
            "2014 WL 1312261"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conroy v. Caron",
          "cluster_id": 7327330,
          "cite": [
            "275 F. Supp. 3d 328"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davon Peyton",
          "cluster_id": 2657561,
          "cite": [
            "409 U.S. App. D.C. 26",
            "745 F.3d 546",
            "2014 WL 1099576",
            "2014 U.S. App. LEXIS 5296"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Michael Cushing(073925)",
          "cluster_id": 4244110,
          "cite": [
            "226 N.J. 187",
            "140 A.3d 1281",
            "2016 N.J. LEXIS 723"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "UNITED STATES v. DAVID D. LEWIS",
          "cluster_id": 4281856,
          "cite": [
            "147 A.3d 236",
            "2016 D.C. App. LEXIS 369",
            "2016 WL 5539892"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cordero-Rosario",
          "cluster_id": 2798310,
          "cite": [
            "786 F.3d 64",
            "2015 U.S. App. LEXIS 7365",
            "2015 WL 1965871"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Denson",
          "cluster_id": 2765319,
          "cite": [
            "775 F.3d 1214",
            "2014 WL 7380656",
            "2014 U.S. App. LEXIS 24616"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In re Telephone Information Needed for a Criminal Investigation",
          "cluster_id": 7314782,
          "cite": [
            "119 F. Supp. 3d 1011",
            "2015 U.S. Dist. LEXIS 99871",
            "2015 WL 4594558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Varriale v. State",
          "cluster_id": 2828520,
          "cite": [
            "444 Md. 400",
            "119 A.3d 824",
            "2015 Md. LEXIS 561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jason Long",
          "cluster_id": 2827389,
          "cite": [
            "797 F.3d 558",
            "2015 U.S. App. LEXIS 14264",
            "2015 WL 4774786"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Stock",
          "cluster_id": 4407126,
          "cite": [
            "2017 CO 80",
            "397 P.3d 386",
            "2017 WL 2837129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fernandez v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2654534 OR 9798884 OR 9798885 OR 9798886) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 2,
        "triage_snippet_classified": 81
      },
      "lane2_top_cited": {
        "query": "cites:(2654534 OR 9798884 OR 9798885 OR 9798886)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yJnM9MTA4MDk3ODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282654534+OR+9798884+OR+9798885+OR+9798886%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2654534 OR 9798884 OR 9798885 OR 9798886)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2654534 OR 9798884 OR 9798885 OR 9798886)",
    "indexed_citing_opinions": 104,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2654534,
        "count": 67,
        "count_source": "search"
      },
      {
        "opinion_id": 9798884,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9798885,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9798886,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 230,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/fernandez-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjczMDg4Njcmcz00ODk0NDA2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282654534+OR+9798884+OR+9798885+OR+9798886%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2654534,
        "cited_id": 1734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 1755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 109925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 625222,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 798254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 1262290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 1399467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 1403682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 3293980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2654534,
        "cited_id": 3864956,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T03:33:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:34:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:34:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:37:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:34:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Fernandez v. California

```
<opinion type="majority">
<author id="p-10">Justice ALITO delivered the opinion of the Court.</author>
<p id="p-11"><a class="page-label" data-citation-index="1" data-label="294" href="#p294" id="p294">*294</a>Our cases firmly establish that police officers may search jointly occupied premises if one of the occupants<footnotemark>1</footnotemark> consents. See <em>United States v. Matlock,</em> <extracted-citation case-ids="6172884" index="0" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U.S. 164</a></span></extracted-citation>, <extracted-citation case-ids="6172884" index="1" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">94 S.Ct. 988</a></span></extracted-citation>, <extracted-citation case-ids="6172884" index="2" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">39 L.Ed.2d 242</a></span></extracted-citation> (1974). In <em>Georgia v. Randolph,</em> <extracted-citation case-ids="3275967" index="3" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="4" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="5" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span></extracted-citation> (2006), we recognized a narrow exception to this rule, holding that the consent of one occupant is insufficient when another occupant is present and objects to the search. In this case, we consider whether <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> applies <a class="page-label" data-citation-index="1" data-label="1130" href="#p1130" id="p1130">*1130</a>if the objecting occupant is absent when another occupant consents. Our opinion in <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> took great pains to emphasize that its holding was limited to situations in which the objecting occupant is physically present. We therefore refuse to extend <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> to the very different situation in this case, where consent was provided by an abused woman well after her male partner had been removed from the apartment they shared. <a class="page-label" data-citation-index="1" data-label="295" href="#p295" id="p295">*295</a>I</p>
<p id="p-12">A</p>
<p id="p-13">The events involved in this case occurred in Los Angeles in October 2009. After observing Abel Lopez cash a check, petitioner Walter Fernandez approached Lopez and asked about the neighborhood in which he lived. When Lopez responded that he was from Mexico, Fernandez laughed and told Lopez that he was in territory ruled by the "D.F.S.," <em>i.e.,</em> the "Drifters" gang. App. 4-5. Petitioner then pulled out a knife and pointed it at Lopez' chest. Lopez raised his hand in self-defense, and petitioner cut him on the wrist.</p>
<p id="p-14">Lopez ran from the scene and called 911 for help, but petitioner whistled, and four men emerged from a nearby apartment building and attacked Lopez. After knocking him to the ground, they hit and kicked him and took his cell phone and his wallet, which contained $400 in cash.</p>
<p id="p-15">A police dispatch reported the incident and mentioned the possibility of gang involvement, and two Los Angeles police officers, Detective Clark and Officer Cirrito, drove to an alley frequented by members of the Drifters. A man who appeared scared walked by the officers and said: " '[T]he guy is in the apartment.' " <em>Id.,</em> at 5. The officers then observed a man run through the alley and into the building to which the man was pointing. A minute or two later, the officers heard sounds of screaming and fighting coming from that building.</p>
<p id="p-16">After backup arrived, the officers knocked on the door of the apartment unit from which the screams had been heard. Roxanne Rojas answered the door. She was holding a baby and appeared to be crying. Her face was red, and she had a large bump on her nose. The officers also saw blood on her shirt and hand from what appeared to be a fresh injury. Rojas told the police that she had been in a fight. Officer Cirrito asked if anyone else was in the apartment, and Rojas said that her 4-year-old son was the only other person present.</p>
<p id="p-17"><a class="page-label" data-citation-index="1" data-label="296" href="#p296" id="p296">*296</a>After Officer Cirrito asked Rojas to step out of the apartment so that he could conduct a protective sweep, petitioner appeared at the door wearing only boxer shorts. Apparently agitated, petitioner stepped forward and said, " 'You don't have any right to come in here. I know my rights.' " <em>Id.,</em> at 6. Suspecting that petitioner had assaulted Rojas, the officers removed him from the apartment and then placed him under arrest. Lopez identified petitioner as his initial attacker, and petitioner was taken to the police station for booking.</p>
<p id="p-18">Approximately one hour after petitioner's arrest, Detective Clark returned to the apartment and informed Rojas that petitioner had been arrested. Detective Clark requested and received both oral and written consent from Rojas to search the premises.<footnotemark>2</footnotemark> In the apartment, the police <a class="page-label" data-citation-index="1" data-label="1131" href="#p1131" id="p1131">*1131</a>found Drifters gang paraphernalia, a butterfly knife, clothing worn by the robbery suspect, and ammunition. Rojas' young son also showed the officers where petitioner had hidden a sawed-off shotgun.</p>
<p id="p-19">B</p>
<p id="p-20">Petitioner was charged with robbery, Cal.Penal Code Ann. § 211 (West 2008), infliction of corporal injury on a spouse, cohabitant, or child's parent, § 273.5(a), possession of a firearm by a felon, § 12021(a)(1)(West 2009), possession of a <a class="page-label" data-citation-index="1" data-label="297" href="#p297" id="p297">*297</a>short-barreled shotgun, § 12020(a)(1), and felony possession of ammunition, § 12316(b)(1).</p>
<p id="p-21">Before trial, petitioner moved to suppress the evidence found in the apartment, but after a hearing, the court denied the motion. Petitioner then pleaded <em>nolo contendere</em> to the firearms and ammunition charges. On the remaining counts-for robbery and infliction of corporal injury-he went to trial and was found guilty by a jury. The court sentenced him to 14 years of imprisonment.</p>
<p id="p-22">The California Court of Appeal affirmed. <extracted-citation case-ids="4257830" index="6" url="https://cite.case.law/cal-app-4th/208/100/"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">208 Cal.App.4th 100</a></span></extracted-citation>, <extracted-citation index="7" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">145 Cal.Rptr.3d 51</a></span></extracted-citation> (2012). Because <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> did not overturn our prior decisions recognizing that an occupant may give effective consent to search a shared residence, the court agreed with the majority of the federal circuits that an objecting occupant's physical presence is "indispensible to the decision in <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> ." <em><extracted-citation index="8" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Id.,</a></span></extracted-citation></em><extracted-citation index="8" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"> at 122</extracted-citation>, <extracted-citation index="9" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">145 Cal.Rptr.3d, at 66</a></span></extracted-citation>.<footnotemark>3</footnotemark> And because petitioner was not present when Rojas consented, the court held that petitioner's <a class="page-label" data-citation-index="1" data-label="298" href="#p298" id="p298">*298</a>suppression motion had been properly denied. <em><extracted-citation index="10" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">Id.,</a></span></extracted-citation></em><extracted-citation index="10" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"> at 121</extracted-citation>, <extracted-citation index="11" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">145 Cal.Rptr.3d, at 65</a></span></extracted-citation>.</p>
<p id="p-23">The California Supreme Court denied the petition for review, and we granted certiorari. 569 U.S. ----, <extracted-citation case-ids="12698369,12698370,12698376,12696459,12696465" index="12" url="https://cite.case.law/s-ct/133/2388/"><span class="citation multiple-matches"><a href="/c/S.Ct./133/2388/">133 S.Ct. 2388</a></span></extracted-citation>, <extracted-citation case-ids="12698368,12698369,12698370,12698372,12698375,12698364,12698365,12698366" index="13" url="https://cite.case.law/l-ed-2d/185/1103/"><span class="citation" data-id="9344351"><a href="/opinion/9348895/jones-v-us-postal-serv/" aria-description="Citation for case: Jones v. U.S. Postal Serv.">185 L.Ed.2d 1103</a></span></extracted-citation> (2013).</p>
<p id="p-24">II</p>
<p id="p-25">A</p>
<p id="p-26">The Fourth Amendment prohibits unreasonable searches and seizures and provides that a warrant may not be issued <a class="page-label" data-citation-index="1" data-label="1132" href="#p1132" id="p1132">*1132</a>without probable cause, but "the text of the Fourth Amendment does not specify when a search warrant must be obtained." <em>Kentucky v. King,</em> 563 U.S. ----, ----, <extracted-citation case-ids="5911971,12458997" index="14" url="https://cite.case.law/s-ct/131/1849/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, 1856, <extracted-citation case-ids="5911971,12458997" index="15" url="https://cite.case.law/s-ct/131/1849/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011). Our cases establish that a warrant is generally required for a search of a home, <em>Brigham City v. Stuart,</em> <extracted-citation case-ids="3275413" index="16" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">547 U.S. 398</a></span></extracted-citation>, 403, <extracted-citation case-ids="3275413" index="17" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">126 S.Ct. 1943</a></span></extracted-citation>, <extracted-citation case-ids="3275413" index="18" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">164 L.Ed.2d 650</a></span></extracted-citation> (2006), but "the ultimate touchstone of the Fourth Amendment is 'reasonableness,' " <em><extracted-citation case-ids="3275413" index="19" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">ibid.</a></span></extracted-citation></em> ; see also <em>Michigan v. Fisher,</em> <extracted-citation case-ids="3639144" index="20" url="https://cite.case.law/us/558/45/#p47"><span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/" aria-description="Citation for case: Michigan v. Fisher">558 U.S. 45</a></span></extracted-citation>, 47, <extracted-citation case-ids="3639144" index="21" url="https://cite.case.law/us/558/45/#p47"><span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/" aria-description="Citation for case: Michigan v. Fisher">130 S.Ct. 546</a></span></extracted-citation>, <extracted-citation case-ids="3639144" index="22" url="https://cite.case.law/us/558/45/#p47"><span class="citation" data-id="9413217"><a href="/opinion/1755/michigan-v-fisher/" aria-description="Citation for case: Michigan v. Fisher">175 L.Ed.2d 410</a></span></extracted-citation> (2009) (<em>per curiam</em> ). And certain categories of permissible warrantless searches have long been recognized.</p>
<p id="p-27">Consent searches occupy one of these categories. "Consent searches are part of the standard investigatory techniques of law enforcement agencies" and are "a constitutionally permissible and wholly legitimate aspect of effective police activity." <em>Schneckloth v. Bustamonte,</em> <extracted-citation case-ids="6172008" index="23" url="https://cite.case.law/us/412/218/#p228"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span></extracted-citation>, 228, 231-232, <extracted-citation case-ids="6172008" index="24" url="https://cite.case.law/us/412/218/#p228"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="25" url="https://cite.case.law/us/412/218/#p228"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span></extracted-citation> (1973). It would be unreasonable-indeed, absurd-to require police officers to obtain a warrant when the sole owner or occupant of a house or apartment voluntarily consents to a search. The owner of a home has a right to allow others to enter and examine the premises, and there is no reason why the owner should not be permitted to extend this same privilege to police officers if that is the owner's choice. Where the owner believes that he or she is under suspicion, the owner may want the police to search the premises so that their suspicions are dispelled. This may be particularly important where the owner has a strong interest in the apprehension of the perpetrator of a crime and believes <a class="page-label" data-citation-index="1" data-label="299" href="#p299" id="p299">*299</a>that the suspicions of the police are deflecting the course of their investigation. An owner may want the police to search even where they lack probable cause, and if a warrant were always required, this could not be done. And even where the police could establish probable cause, requiring a warrant despite the owner's consent would needlessly inconvenience everyone involved-not only the officers and the magistrate but also the occupant of the premises, who would generally either be compelled or would feel a need to stay until the search was completed. <em>Michigan v. Summers,</em> <extracted-citation case-ids="1313927" index="26" url="https://cite.case.law/us/452/692/#p701"><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U.S. 692</a></span></extracted-citation>, 701, <extracted-citation case-ids="1313927" index="27" url="https://cite.case.law/us/452/692/#p701"><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">101 S.Ct. 2587</a></span></extracted-citation>, <extracted-citation case-ids="1313927" index="28" url="https://cite.case.law/us/452/692/#p701"><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">69 L.Ed.2d 340</a></span></extracted-citation> (1981).<footnotemark>4</footnotemark></p>
<p id="p-28">While it is clear that a warrantless search is reasonable when the sole occupant of a house or apartment consents, what happens when there are two or more occupants? Must they all consent? Must they all be asked? Is consent by one occupant enough? The Court faced that problem 40 years ago in <em>United States v. Matlock,</em> <extracted-citation case-ids="6172884" index="29" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U.S. 164</a></span></extracted-citation>, <extracted-citation case-ids="6172884" index="30" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">94 S.Ct. 988</a></span></extracted-citation>, <extracted-citation case-ids="6172884" index="31" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">39 L.Ed.2d 242</a></span></extracted-citation> (1974).</p>
<p id="p-29">In that case, Matlock and a woman named Graff were living together in a house that was also occupied by several of Graff's siblings and by her mother, who had rented the house. While in the front yard of the house, Matlock was arrested for bank robbery and was placed in a squad car. Although the police could have easily asked him for consent to search the room that he and Graff shared, they did not do so. Instead, they knocked on the door and obtained Graff's permission to search. The search yielded incriminating <a class="page-label" data-citation-index="1" data-label="1133" href="#p1133" id="p1133">*1133</a>evidence, which the defendant sought to suppress, but this Court held that Graff's consent justified the warrantless search. As the Court put it, "the consent of one who possesses <a class="page-label" data-citation-index="1" data-label="300" href="#p300" id="p300">*300</a>common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared." <em><extracted-citation case-ids="6172884" index="32" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6172884" index="32" url="https://cite.case.law/us/415/164/"> at 170</extracted-citation>, <extracted-citation case-ids="6172884" index="33" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">94 S.Ct. 988</a></span></extracted-citation>.</p>
<p id="p-30">In <em>Illinois v. Rodriguez,</em> <extracted-citation case-ids="6214176" index="34" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">497 U.S. 177</a></span></extracted-citation>, <extracted-citation case-ids="6214176" index="35" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">110 S.Ct. 2793</a></span></extracted-citation>, <extracted-citation case-ids="6214176" index="36" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">111 L.Ed.2d 148</a></span></extracted-citation> (1990), the Court reaffirmed and extended the <em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Matlock</a></span></em> holding. In <em><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">Rodriguez</a></span>,</em> a woman named Fischer told police officers that she had been assaulted by Rodriguez in what she termed " 'our' apartment." <extracted-citation case-ids="6214176" index="37" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">497 U.S., at 179</a></span></extracted-citation>, <extracted-citation case-ids="6214176" index="38" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">110 S.Ct. 2793</a></span></extracted-citation>. She also informed the officers that Rodriguez was asleep in the apartment, and she then accompanied the officers to that unit. When they arrived, the officers could have knocked on the door and awakened Rodriguez, and had they done so, Rodriguez might well have surrendered at the door and objected to the officers' entry. Instead, Fischer unlocked the door, the officers entered without a warrant, and they saw drug paraphernalia and containers filled with white powder in plain view.</p>
<p id="p-31">After the search, the police learned that Fischer no longer resided at the apartment, and this Court held that she did not have common authority over the premises at the time in question. The Court nevertheless held that the warrantless entry was lawful because the police reasonably believed that Fischer was a resident. <em><extracted-citation case-ids="6214176" index="39" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6214176" index="39" url="https://cite.case.law/us/497/177/"> at 188-189</extracted-citation>, <extracted-citation case-ids="6214176" index="40" url="https://cite.case.law/us/497/177/"><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">110 S.Ct. 2793</a></span></extracted-citation>.</p>
<p id="p-32">B</p>
<p id="p-33">While consent by one resident of jointly occupied premises is generally sufficient to justify a warrantless search, we recognized a narrow exception to this rule in <em>Georgia v. Randolph,</em> <extracted-citation case-ids="3275967" index="41" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="42" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="43" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span></extracted-citation> (2006). In that case, police officers responded to the Randolphs' home after receiving a report of a domestic dispute. When the officers arrived, Janet Randolph informed the officers that her estranged husband, Scott Randolph, was a cocaine user and that there were "items of drug evidence" in the house. <em><extracted-citation case-ids="3275967" index="44" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Id.</a></span></extracted-citation></em> , at 107, <extracted-citation case-ids="3275967" index="45" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (internal quotation marks omitted). The officers first asked Scott for consent to search, but he "unequivocally refused." <em><extracted-citation case-ids="3275967" index="46" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Ibid.</a></span></extracted-citation></em> The officers then turned to Janet, and <a class="page-label" data-citation-index="1" data-label="301" href="#p301" id="p301">*301</a>she consented to the search, which produced evidence that was later used to convict Scott for possession of cocaine.</p>
<p id="p-34">Without questioning the prior holdings in <em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Matlock</a></span></em> and <em><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">Rodriguez</a></span>,</em> this Court held that Janet Randolph's consent was insufficient under the circumstances to justify the warrantless search. The Court reiterated the proposition that a person who shares a residence with others assumes the risk that "any one of them may admit visitors, with the consequence that a guest obnoxious to one may nevertheless be admitted in his absence by another." 547 U.S., at 111, <extracted-citation case-ids="3275967" index="47" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>. But the Court held that "<em>a physically present inhabitant's</em> express refusal of consent to a police search [of his home] is dispositive as to him, regardless of the consent of a fellow occupant." <em><extracted-citation case-ids="3275967" index="48" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Id.</a></span></extracted-citation></em> , at 122-123, <extracted-citation case-ids="3275967" index="49" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (emphasis added).</p>
<p id="p-35">The Court's opinion went to great lengths to make clear that its holding was limited to situations in which the objecting occupant is present. Again and again, the opinion of the Court stressed this controlling factor. See <em><extracted-citation case-ids="3275967" index="50" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 106, <extracted-citation case-ids="3275967" index="51" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("present at the scene"); <em><extracted-citation case-ids="3275967" index="52" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">ibid.</a></span></extracted-citation></em> ("physically present"); <em><extracted-citation case-ids="3275967" index="53" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 108, <extracted-citation case-ids="3275967" index="54" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("a co-tenant who is present"); <em><extracted-citation case-ids="3275967" index="55" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 109, <extracted-citation case-ids="3275967" index="56" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("physically present"); <em><extracted-citation case-ids="3275967" index="57" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 114, <extracted-citation case-ids="3275967" index="58" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("a present and objecting co-tenant"); <em><extracted-citation case-ids="3275967" index="59" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 119, <extracted-citation case-ids="3275967" index="60" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (a co-tenant "standing at the door and <a class="page-label" data-citation-index="1" data-label="1134" href="#p1134" id="p1134">*1134</a>expressly refusing consent"); <em><extracted-citation case-ids="3275967" index="61" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 120, <extracted-citation case-ids="3275967" index="62" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("a physically present resident"), <em><extracted-citation case-ids="3275967" index="63" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 121, <extracted-citation case-ids="3275967" index="64" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("a physically present fellow tenant objects"); <em><extracted-citation case-ids="3275967" index="65" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">ibid.</a></span></extracted-citation></em> ("[A] potential defendant with self-interest in objecting is at the door and objects"); <em><extracted-citation case-ids="3275967" index="66" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 122, <extracted-citation case-ids="3275967" index="67" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> ("[A] physically present inhabitant's express refusal of consent to a police search is dispositive as to him"). The Court's opinion could hardly have been clearer on this point, and the separate opinion filed by Justice BREYER, whose vote was decisive, was equally unambiguous. See <em><extracted-citation case-ids="3275967" index="68" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">id.</a></span></extracted-citation></em> , at 126, <extracted-citation case-ids="3275967" index="69" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (concurring) ("The Court's opinion does not apply where the objector is not present 'and object[ing]' ").</p>
<p id="p-36">III</p>
<p id="p-37">In this case, petitioner was not present when Rojas consented, but petitioner still contends that <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> is <a class="page-label" data-citation-index="1" data-label="302" href="#p302" id="p302">*302</a>controlling. He advances two main arguments. First, he claims that his absence should not matter since he was absent only because the police had taken him away. Second, he maintains that it was sufficient that he objected to the search while he was still present. Such an objection, he says, should remain in effect until the objecting party "no longer wishes to keep the police out of his home." Brief for Petitioner 8. Neither of these arguments is sound.</p>
<p id="p-38">A</p>
<p id="p-39">We first consider the argument that the presence of the objecting occupant is not necessary when the police are responsible for his absence. In <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span>,</em> the Court suggested in dictum that consent by one occupant might not be sufficient if "there is evidence that the police have removed the potentially objecting tenant from the entrance for the sake of avoiding a possible objection." 547 U.S., at 121, <extracted-citation case-ids="3275967" index="70" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>. We do not believe the statement should be read to suggest that improper motive may invalidate objectively justified removal. Hence, it does not govern here.</p>
<p id="p-40">The <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> dictum is best understood not to require an inquiry into the subjective intent of officers who detain or arrest a potential objector but instead to refer to situations in which the removal of the potential objector is not objectively reasonable. As petitioner acknowledges, see Brief for Petitioner 25, our Fourth Amendment cases "have repeatedly rejected" a subjective approach. <em>Brigham City,</em> <extracted-citation case-ids="3275413" index="71" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">547 U.S., at 404</a></span></extracted-citation>, <extracted-citation case-ids="3275413" index="72" url="https://cite.case.law/us/547/398/#p403"><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">126 S.Ct. 1943</a></span></extracted-citation> (alteration and internal quotation marks omitted). "Indeed, we have never held, outside limited contexts such as an 'inventory search or administrative inspection ..., that an officer's motive invalidates objectively justifiable behavior under the Fourth Amendment.' " <em><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">King</a></span>,</em> 563 U.S., at ----, <extracted-citation case-ids="5911971,12458997" index="73" url="https://cite.case.law/s-ct/131/1849/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct., at 1859</a></span></extracted-citation>.</p>
<p id="p-41">Petitioner does not claim that the <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> Court meant to break from this consistent practice, and we do not think that it did. And once it is recognized that the test is one of objective reasonableness, petitioner's argument collapses.</p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="303" href="#p303" id="p303">*303</a>He does not contest the fact that the police had reasonable grounds for removing him from the apartment so that they could speak with Rojas, an apparent victim of domestic violence, outside of petitioner's potentially intimidating presence. In fact, he does not even contest the existence of probable cause to place him under arrest. We therefore hold that an occupant who is absent due to a lawful detention or arrest stands in the same shoes as an occupant who is absent for any other reason.</p>
<p id="p-43">This conclusion does not "make a mockery of <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span>,</em> " as petitioner protests. Brief for Petitioner 9. It simply accepts <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> on its own terms. The <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> holding unequivocally requires the <a class="page-label" data-citation-index="1" data-label="1135" href="#p1135" id="p1135">*1135</a>presence of the objecting occupant in every situation other than the one mentioned in the dictum discussed above.</p>
<p id="p-44">B</p>
<p id="p-45">This brings us to petitioner's second argument, viz., that his objection, made at the threshold of the premises that the police wanted to search, remained effective until he changed his mind and withdrew his objection. This argument is inconsistent with <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> 's reasoning in at least two important ways. First, the argument cannot be squared with the "widely shared social expectations" or "customary social usage" upon which the <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> holding was based. See 547 U.S., at 111, 121, <extracted-citation case-ids="3275967" index="74" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>. Explaining why consent by one occupant could not override an objection by a physically present occupant, the <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> Court stated:</p>
<blockquote id="p-46">"[I]t is fair to say that a caller standing at the door of shared premises would have no confidence that one occupant's invitation was a sufficiently good reason to enter when a fellow tenant stood there saying, 'stay out.' Without some very good reason, no sensible person would go inside under those conditions." <em><extracted-citation case-ids="3275967" index="75" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="3275967" index="75" url="https://cite.case.law/us/547/103/"> at 113</extracted-citation>, <extracted-citation case-ids="3275967" index="76" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>.</blockquote>
<p id="p-47">It seems obvious that the calculus of this hypothetical caller would likely be quite different if the objecting tenant <a class="page-label" data-citation-index="1" data-label="304" href="#p304" id="p304">*304</a>was not standing at the door. When the objecting occupant is standing at the threshold saying "stay out," a friend or visitor invited to enter by another occupant can expect at best an uncomfortable scene and at worst violence if he or she tries to brush past the objector. But when the objector is not on the scene (and especially when it is known that the objector will not return during the course of the visit), the friend or visitor is much more likely to accept the invitation to enter.<footnotemark>5</footnotemark> Thus, petitioner's argument is inconsistent with <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> 's reasoning.</p>
<p id="p-48">Second, petitioner's argument would create the very sort of practical complications that <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> sought to avoid. The <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> Court recognized that it was adopting a "formalis[tic]" rule, but it did so in the interests of "simple clarity" and administrability. <em><extracted-citation case-ids="3275967" index="77" url="https://cite.case.law/us/547/103/">Id.,</extracted-citation></em><extracted-citation case-ids="3275967" index="77" url="https://cite.case.law/us/547/103/"> at 121, 122</extracted-citation>, <extracted-citation case-ids="3275967" index="78" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>.</p>
<p id="p-49">The rule that petitioner would have us adopt would produce a plethora of practical problems. For one thing, there is the question of duration. Petitioner argues that an objection, once made, should last until it is withdrawn by the objector, but such a rule would be unreasonable. Suppose that a husband and wife owned a house as joint tenants and that the husband, after objecting to a search of the house, <a class="page-label" data-citation-index="1" data-label="305" href="#p305" id="p305">*305</a>was convicted and sentenced to a 15-year prison term. Under petitioner's proposed rule, the wife would be unable to consent to a search of the house 10 years <a class="page-label" data-citation-index="1" data-label="1136" href="#p1136" id="p1136">*1136</a>after the date on which her husband objected. We refuse to stretch <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> to such strange lengths.</p>
<p id="p-50">Nor are we persuaded to hold that an objection lasts for a "reasonable" time. "[I]t is certainly unusual for this Court to set forth precise time limits governing police action," <em>Maryland v. Shatzer,</em> <extracted-citation case-ids="3582023" index="79" url="https://cite.case.law/us/559/98/#p110"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">559 U.S. 98</a></span></extracted-citation>, 110, <extracted-citation case-ids="3582023" index="80" url="https://cite.case.law/us/559/98/#p110"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">130 S.Ct. 1213</a></span></extracted-citation>, <extracted-citation case-ids="3582023" index="81" url="https://cite.case.law/us/559/98/#p110"><span class="citation" data-id="9413177"><a href="/opinion/1734/maryland-v-shatzer/" aria-description="Citation for case: Maryland v. Shatzer">175 L.Ed.2d 1045</a></span></extracted-citation> (2010), and what interval of time would be reasonable in this context? A week? A month? A year? Ten years?</p>
<p id="p-51">Petitioner's rule would also require the police and ultimately the courts to determine whether, after the passage of time, an objector still had "common authority" over the premises, and this would often be a tricky question. Suppose that an incarcerated objector and a consenting co-occupant were joint tenants on a lease. If the objector, after incarceration, stopped paying rent, would he still have "common authority," and would his objection retain its force? Would it be enough that his name remained on the lease? Would the result be different if the objecting and consenting lessees had an oral month-to-month tenancy?</p>
<p id="p-52">Another problem concerns the procedure needed to register a continuing objection. Would it be necessary for an occupant to object while police officers are at the door? If presence at the time of consent is not needed, would an occupant have to be present at the premises when the objection was made? Could an objection be made pre-emptively? Could a person like Scott Randolph, suspecting that his estranged wife might invite the police to view his drug stash and paraphernalia, register an objection in advance? Could this be done by posting a sign in front of the house? Could a standing objection be registered by serving notice on the chief of police?</p>
<p id="p-53">Finally, there is the question of the particular law enforcement officers who would be bound by an objection. Would <a class="page-label" data-citation-index="1" data-label="306" href="#p306" id="p306">*306</a>this set include just the officers who were present when the objection was made? Would it also apply to other officers working on the same investigation? Would it extend to officers who were unaware of the objection? How about officers assigned to different but arguably related cases? Would it be limited by law enforcement agency?</p>
<p id="p-54">If <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> is taken at its word-that it applies only when the objector is standing in the door saying "stay out" when officers propose to make a consent search-all of these problems disappear.</p>
<p id="p-55">In response to these arguments, petitioner argues that <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> 's requirement of physical presence is not without its own ambiguity. And we acknowledge that if, as we conclude, <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> requires presence on the premises to be searched, there may be cases in which the outer boundary of the premises is disputed. The Court confronted a similar problem last Term in <em>Bailey v. United States,</em> 568 U.S. ----, <extracted-citation case-ids="12407374" index="82" url="https://cite.case.law/us/568/186/"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">133 S.Ct. 1031</a></span></extracted-citation>, <extracted-citation case-ids="12407374" index="83" url="https://cite.case.law/us/568/186/"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">185 L.Ed.2d 19</a></span></extracted-citation> (2013), but despite arguments similar to those now offered by petitioner, the Court adopted a rule that applies only when the affected individual is near the premises being searched. Having held that a premises rule is workable in that context, we see no ground for reaching a different conclusion here.</p>
<p id="p-56">C</p>
<p id="p-57">Petitioner argues strenuously that his expansive interpretation of <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> would not hamper law enforcement because in most cases where officers have probable cause to arrest a physically present objector they also have probable cause to search the premises that the objector does not want them to enter, see Brief for Petitioner 20-23, but this argument misunderstands <a class="page-label" data-citation-index="1" data-label="1137" href="#p1137" id="p1137">*1137</a>the constitutional status of consent searches. A warrantless consent search is reasonable and thus consistent with the Fourth Amendment irrespective of the availability of a warrant. Even with modern technological advances, the warrant procedure imposes burdens on the officers who wish to search, the magistrate who must review <a class="page-label" data-citation-index="1" data-label="307" href="#p307" id="p307">*307</a>the warrant application, and the party willing to give consent. When a warrantless search is justified, requiring the police to obtain a warrant may "unjustifiably interfer[e] with legitimate law enforcement strategies." <em><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">King</a></span>,</em> 563 U.S., at ----, <extracted-citation case-ids="5911971,12458997" index="84" url="https://cite.case.law/s-ct/131/1849/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct., at 1860</a></span></extracted-citation>. Such a requirement may also impose an unmerited burden on the person who consents to an immediate search, since the warrant application procedure entails delay. Putting the exception the Court adopted in <em><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Randolph</a></span></em> to one side, the lawful occupant of a house or apartment should have the right to invite the police to enter the dwelling and conduct a search. Any other rule would trample on the rights of the occupant who is willing to consent. Such an occupant may want the police to search in order to dispel "suspicion raised by sharing quarters with a criminal." 547 U.S., at 116, <extracted-citation case-ids="3275967" index="85" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>; see also <em>Schneckloth,</em> <extracted-citation case-ids="6172008" index="86" url="https://cite.case.law/us/412/218/#p228"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S., at 243</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="87" url="https://cite.case.law/us/412/218/#p228"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation> (evidence obtained pursuant to a consent search "may insure that a wholly innocent person is not wrongly charged with a criminal offense"). And an occupant may want the police to conduct a thorough search so that any dangerous contraband can be found and removed. In this case, for example, the search resulted in the discovery and removal of a sawed-off shotgun to which Rojas' 4-year-old son had access.</p>
<p id="p-58">Denying someone in Rojas' position the right to allow the police to enter <em>her</em> home would also show disrespect for her independence. Having beaten Rojas, petitioner would bar her from controlling access to her own home until such time as he chose to relent. The Fourth Amendment does not give him that power.</p>
<p id="p-59">* * *</p>
<p id="p-60">The judgment of the California Court of Appeal is affirmed.</p>
<p id="p-61"><em>It is so ordered.</em></p>
<footnote label="1">
<p id="p-88">We use the terms "occupant," "resident," and "tenant" interchangeably to refer to persons having "common authority" over premises within the meaning of <em><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Matlock</a></span></em> . See <em>United States v. Matlock,</em> <extracted-citation case-ids="6172884" index="88" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U.S. 164</a></span></extracted-citation>, 171, n. 7, <extracted-citation case-ids="6172884" index="89" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">94 S.Ct. 988</a></span></extracted-citation>, <extracted-citation case-ids="6172884" index="90" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">39 L.Ed.2d 242</a></span></extracted-citation> (1974).</p>
</footnote>
<footnote label="2">
<p id="p-89">Both petitioner and the dissent suggest that Rojas' consent was coerced. <em>Post,</em> at 1143, n. 5 (opinion of GINSBURG, J.). But the trial court found otherwise, App. 152, and the correctness of that finding is not before us. In suggesting that Rojas' consent was coerced, the dissent recites portions of Rojas' testimony from the suppression hearing that the trial judge appears to have rejected. <em><extracted-citation case-ids="6172884" index="91" url="https://cite.case.law/us/415/164/"><span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">Ibid.</a></span></extracted-citation></em> Similarly, the jury plainly did not find Rojas to be credible. At trial, she testified for the defense and told the jury, among other things, that the wounds observed by the officers who came to her door were not inflicted by petitioner but by a woman looking for petitioner during a fight. <extracted-citation case-ids="4257830" index="92" url="https://cite.case.law/cal-app-4th/208/100/"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">208 Cal.App.4th 100</a></span></extracted-citation>, 109-110, <extracted-citation index="93" url="https://cite.case.law/citations/?q=145%20Cal.%20Rptr.%203d%2051"><span class="citation" data-id="5666705"><a href="/opinion/5811236/people-v-fernandez/" aria-description="Citation for case: People v. Fernandez">145 Cal.Rptr.3d 51</a></span></extracted-citation>, 56 (2012). The jury obviously did not believe this testimony because it found petitioner guilty of inflicting corporal injury on her.</p>
</footnote>
<footnote label="3">
<p id="p-90">See <em>United States v. Cooke,</em> <extracted-citation case-ids="3748697" index="94" url="https://cite.case.law/f3d/674/491/#p498"><span class="citation" data-id="625222"><a href="/opinion/625222/united-states-v-cooke/" aria-description="Citation for case: United States v. Cooke">674 F.3d 491</a></span></extracted-citation>, 498 (C.A.5 2012) ("<em>Randolph</em> was a narrow exception to the general <em>Matlock</em> rule permitting cotenant consent, relevant only as to physically present objectors"); <em>United States v. Hudspeth,</em> <extracted-citation case-ids="3555361" index="95" url="https://cite.case.law/f3d/518/954/#p960"><span class="citation" data-id="9621916"><a href="/opinion/1403682/united-states-v-hudspeth/" aria-description="Citation for case: United States v. Hudspeth">518 F.3d 954</a></span></extracted-citation>, 960 (C.A.8 2008) (concluding that "the narrow holding of <em>Randolph,</em> which repeatedly referenced the defendant's physical presence <em>and</em> immediate objection is inapplicable"); <em>United States v. Henderson,</em> <extracted-citation case-ids="5764572" index="96" url="https://cite.case.law/f3d/536/776/#p777"><span class="citation" data-id="9620355"><a href="/opinion/1399467/united-states-v-henderson/" aria-description="Citation for case: United States v. Henderson">536 F.3d 776</a></span></extracted-citation>, 777 (C.A.7 2008) (recognizing that "<em>Randolph</em> left the bulk of third-party consent law in place; its holding applies only when the defendant is both present and objects to the search of his home"); <em>United States v. McKerrell,</em> <extracted-citation case-ids="3469242" index="97" url="https://cite.case.law/f3d/491/1221/#p1227"><span class="citation" data-id="798254"><a href="/opinion/798254/united-states-v-jack-wayne-mckerrell-jr/" aria-description="Citation for case: United States v. Jack Wayne McKerrell Jr.">491 F.3d 1221</a></span></extracted-citation>, 1227 (C.A.10 2007) ("<em>Randolph</em> carefully delineated the narrow circumstances in which its holding applied, and ... <em>Randolph</em> consciously employed a rule requiring an express objection by a present co-tenant"); but see <em>United States v. Murphy,</em> <extracted-citation case-ids="3641181" index="98" url="https://cite.case.law/f3d/516/1117/#p1124"><span class="citation" data-id="1262290"><a href="/opinion/1262290/united-states-v-murphy/" aria-description="Citation for case: United States v. Murphy">516 F.3d 1117</a></span></extracted-citation>, 1124-1125 (C.A.9 2008) (holding that "when a co-tenant objects to a search and another party with common authority subsequently gives consent to that search in the absence of the first co-tenant the search is invalid as to the objecting co-tenant" because "[o]nce a co-tenant has registered his objection, his refusal to grant consent remains effective barring some objective manifestation that he has changed his position and no longer objects").</p>
</footnote>
<footnote label="4">
<p id="p-91">A main theme of the dissent is that the police in this case had probable cause to search the apartment and therefore could have obtained a warrant. Of course, this will not always be so in cases in which one occupant consents to a search and the other objects, and the dissent does not suggest that a warrant should be required only when probable cause is present. As a result, the dissent's repeated references to the availability of a warrant in this case are beside the point.</p>
</footnote>
<footnote label="5">
<p id="p-92">Although the dissent intimates that "customary social usage" goes further than this, see <em>post,</em> at 1140, the dissent provides no support for this doubtful proposition. In the present case, for example, suppose that Rojas had called a relative, a friend, a supportive neighbor, or a person who works for a group that aids battered women and had invited that individual to enter and examine the premises while petitioner was in jail. Would any of those invitees have felt that it was beyond Rojas' authority to extend that invitation over petitioner's objection?</p>
<p id="p-93">Instead of attempting to show that such persons would have felt it improper to accept this invitation, the dissent quickly changes the subject and says that "conjectures about social behavior shed little light on the constitutionality" of the search in this case. <em>Post,</em> at 1140. But the holding in <em>Georgia v. Randolph,</em> <extracted-citation case-ids="3275967" index="99" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="100" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="101" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span></extracted-citation> (2006), was based on "widely shared social expectations" and "customary social usage." See <em><extracted-citation case-ids="3275967" index="102" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">Id.</a></span></extracted-citation></em> , at 111, 121, <extracted-citation case-ids="3275967" index="103" url="https://cite.case.law/us/547/103/"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>. Thus, the dissent simply fails to come to grips with the reasoning of the precedent on which it relies.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Flippo v. West Virginia.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Flippo v. West Virginia"
type: case
citation: "528 U.S. 11 (1999)"
parallel_cite: "120 S. Ct. 7; 145 L. Ed. 2d 16"
neutral_cite: 1999 U.S. LEXIS 6924
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-10-18
docket: 98-8770
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-10-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Flippo v. West Virginia
  varies_by_point: false
  scope_note: "Per curiam. Reaffirms Mincey v. Arizona and Thompson v. Louisiana; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1854815/flippo-v-west-virginia/"
  cluster_id: 1854815
  opinion_id: 1854815
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[Mincey v. Arizona]]", "[[Thompson v. Louisiana]]", "[[Michigan v. Tyler]]", "[[Michigan v. Clifford]]"]
aliases: []
tags: ["case", "fourth-amendment", "crime-scene", "warrant-requirement", "homicide", "emergency-aid"]
holding: "There is no general 'crime-scene exception' to the warrant requirement; a warrantless search of a secured homicide scene (including opening a closed briefcase) is invalid unless a recognized exception applies."
lake:
  record_id: Flippo v. West Virginia
  status: under_review
  projected_at: 2026-07-06
---

# Flippo v. West Virginia

*528 U.S. 11 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While vacationing at a state-park cabin, the petitioner called 911 to report that he and his wife had been attacked. Police found him outside, injured, and found his wife dead inside with fatal head wounds. Officers secured the area, took the petitioner to the hospital, and — after a photographer arrived — reentered and "processed the crime scene" for over 16 hours, photographing, collecting evidence, and opening a closed briefcase from which they seized incriminating photographs. The trial court denied suppression, reasoning that officers who secure a homicide crime scene may thoroughly search "anything and everything found within the crime scene area."

## Issue
Whether police who have secured a homicide crime scene may conduct a warrantless general search of the premises and its contents under a "crime-scene exception" to the warrant requirement.

## Rule
No. "A warrantless search by the police is invalid unless it falls within one of the narrow and well-delineated exceptions to the warrant requirement, . . . none of which the trial court invoked here." — 528 U.S. at 13–14. ^pin-13

The crime-scene rationale conflicts with *[[Mincey v. Arizona|Mincey]]*: "This position squarely conflicts with *Mincey* v. *Arizona*, . . . where we rejected the contention that there is a 'murder scene exception' to the Warrant Clause of the Fourth Amendment. . . . [W]e rejected any general 'murder scene exception' as 'inconsistent with the Fourth and Fourteenth Amendments.' . . . *Mincey* controls here." — *Id.* at 14. ^pin-14

## Application
The trial court upheld the search solely as a permissible search of a secured "homicide crime scene," invoking no recognized warrant exception. That is exactly the "crime-scene exception" *[[Mincey v. Arizona|Mincey]]* and *[[Thompson v. Louisiana|Thompson]]* rejected. Police could have made a warrantless entry to render aid and a prompt search for other victims or a killer, but the prolonged general search of the cabin and the opening of a closed briefcase were not justified on that basis. The Court left open, for remand, whether consent or some other recognized exception might apply.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). There is no general crime-scene exception; the warrantless processing of the secured homicide scene required a recognized exception, which the trial court never identified.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Flippo* reaffirms [[Mincey v. Arizona]] and [[Thompson v. Louisiana]] and is consistent with the fire-scene warrant rules of [[Michigan v. Tyler]] and [[Michigan v. Clifford]].

## Appears on
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Flippo v. West Virginia*, 528 U.S. 11 (1999) — https://www.courtlistener.com/opinion/1854815/flippo-v-west-virginia/ — pinpoints: 13, 14.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f7443dff50608e02", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Flippo v. West Virginia"}, "payload": {"all": [{"cite": "528 U.S. 11", "page": "11", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "528"}, {"cite": "120 S. Ct. 7", "page": "7", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "120"}, {"cite": "145 L. Ed. 2d 16", "page": "16", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "145"}, {"cite": "1999 U.S. LEXIS 6924", "page": "6924", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "528 U.S. 11", "official": {"cite": "528 U.S. 11", "page": "11", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "528"}, "official_selection_present": true, "record_id": "Flippo v. West Virginia"}}
{"assertion_id": "b16e0d31b064bef6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-13", "record_id": "Flippo v. West Virginia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-13", "pinpoint_status": "slip-only", "quote": "to the warrant requirement. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Flippo v. West Virginia", "star_marker": null}}
{"assertion_id": "c84c8cc6f6f1f0b2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-14", "record_id": "Flippo v. West Virginia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-14", "pinpoint_status": "slip-only", "quote": "This position squarely conflicts with *Mincey* v. *Arizona*, . . . where we rejected the contention that there is a 'murder scene exception' to the Warrant Clause of the Fourth Amendment. . . . [W]e rejected any general 'murder scene exception' as 'inconsistent with the Fourth and Fourteenth Amendments.' . . . *Mincey* controls here.", "quote_fidelity": "mismatch", "record_id": "Flippo v. West Virginia", "star_marker": null}}
{"assertion_id": "113cfa4d05aa4bf8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Flippo v. West Virginia"}, "payload": {"as_of_content": "1999-10-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Flippo v. West Virginia", "scope_note": "Per curiam. Reaffirms Mincey v. Arizona and Thompson v. Louisiana; no negative treatment.", "varies_by_point": false}}
```

### lake record — Flippo v. West Virginia

```json
{
  "schema_version": "s2.v1",
  "record_id": "Flippo v. West Virginia",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Flippo v. West Virginia",
    "case_name_short": "Flippo",
    "case_name_full": "Flippo v. West Virginia",
    "input_case_name": "Flippo v. West Virginia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-10-18",
    "year": 1999,
    "docket": "98-8770",
    "cluster_id": 1854815,
    "lead_opinion_id": 1854815,
    "sibling_ids": [
      1854815
    ],
    "absolute_url": "/opinion/1854815/flippo-v-west-virginia/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "528 U.S. 11",
      "volume": "528",
      "reporter": "U.S.",
      "page": "11",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "120 S. Ct. 7",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 16",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "16",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 6924",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "6924",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "528 U.S. 11",
        "volume": "528",
        "reporter": "U.S.",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "120 S. Ct. 7",
        "volume": "120",
        "reporter": "S. Ct.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "145 L. Ed. 2d 16",
        "volume": "145",
        "reporter": "L. Ed. 2d",
        "page": "16",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 6924",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "6924",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "528 U.S. 11",
    "official_selection": {
      "court_class": "scotus",
      "selected": "528 U.S. 11",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-13",
      "page": null,
      "quote": "to the warrant requirement. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-14",
      "page": null,
      "quote": "This position squarely conflicts with *Mincey* v. *Arizona*, . . . where we rejected the contention that there is a 'murder scene exception' to the Warrant Clause of the Fourth Amendment. . . . [W]e rejected any general 'murder scene exception' as 'inconsistent with the Fourth and Fourteenth Amendments.' . . . *Mincey* controls here.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-10-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Flippo v. West Virginia",
    "varies_by_point": false,
    "scope_note": "Per curiam. Reaffirms Mincey v. Arizona and Thompson v. Louisiana; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane1_negative"
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
        "journal_ref": "Flippo v. West Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kory Ray Smith",
          "cluster_id": 788425,
          "cite": [
            "389 F.3d 944",
            "2004 U.S. App. LEXIS 24343",
            "2004 WL 2660594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Torrez v. State",
          "cluster_id": 1450090,
          "cite": [
            "34 S.W.3d 10",
            "2000 WL 1723658"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
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
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 6889013,
          "cite": [
            "92 Ohio St. 3d 146",
            "749 N.E.2d 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wear",
          "cluster_id": 2231471,
          "cite": [
            "893 N.E.2d 631",
            "229 Ill. 2d 545",
            "323 Ill. Dec. 359",
            "2008 Ill. LEXIS 636"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Coulter",
          "cluster_id": 2335569,
          "cite": [
            "67 S.W.3d 3",
            "2001 Tenn. Crim. App. LEXIS 485"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ryon",
          "cluster_id": 2626315,
          "cite": [
            "108 P.3d 1032",
            "137 N.M. 174",
            "2005 NMSC 005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Earl Davis",
          "cluster_id": 2968788,
          "cite": [
            "690 F.3d 226",
            "2012 WL 3518479",
            "2012 U.S. App. LEXIS 17217"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Wayne Banks",
          "cluster_id": 797384,
          "cite": [
            "482 F.3d 733",
            "2007 U.S. App. LEXIS 8525",
            "2007 WL 1097954"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thompson",
          "cluster_id": 2639507,
          "cite": [
            "135 P.3d 3",
            "43 Cal. Rptr. 3d 750",
            "38 Cal. 4th 811",
            "2006 Cal. Daily Op. Serv. 4587",
            "2006 Daily Journal DAR 6776",
            "2006 Cal. LEXIS 6515"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "RDS v. State",
          "cluster_id": 1057801,
          "cite": [
            "245 S.W.3d 356",
            "2008 Tenn. LEXIS 28",
            "2008 WL 315568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Arturo D.",
          "cluster_id": 2585222,
          "cite": [
            "38 P.3d 433",
            "115 Cal. Rptr. 2d 581",
            "27 Cal. 4th 60",
            "2002 Cal. Daily Op. Serv. 647",
            "2002 Daily Journal DAR 833",
            "2002 Cal. LEXIS 273"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robey v. Superior Court",
          "cluster_id": 944930,
          "cite": [
            "56 Cal. 4th 1218",
            "302 P.3d 574",
            "158 Cal. Rptr. 3d 261",
            "2013 WL 3214712",
            "2013 Cal. LEXIS 5387"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 10685818,
          "cite": [
            "2001 Ohio 132",
            "92 Ohio St. 3d 146"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warren Green, IV",
          "cluster_id": 4520277,
          "cite": [
            "897 F.3d 173"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Susan Stricker v. Twp. Of Cambridge",
          "cluster_id": 815266,
          "cite": [
            "710 F.3d 350",
            "2013 WL 141695"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Clarke",
          "cluster_id": 4322781,
          "cite": [
            "842 F.3d 288",
            "2016 WL 6819688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brock",
          "cluster_id": 2291360,
          "cite": [
            "327 S.W.3d 645",
            "2009 Tenn. Crim. App. LEXIS 496",
            "2009 WL 1850883"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Lee Hutchison",
          "cluster_id": 3169888,
          "cite": [
            "482 S.W.3d 893"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNair v. Commonwealth",
          "cluster_id": 1066057,
          "cite": [
            "521 S.E.2d 303",
            "31 Va. App. 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matthews",
          "cluster_id": 1031087,
          "cite": [
            "591 F.3d 230",
            "2009 U.S. App. LEXIS 28764",
            "2009 WL 5173719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 620931,
          "cite": [
            "667 F.3d 477",
            "2012 WL 104912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ovieda",
          "cluster_id": 4647505,
          "cite": [
            "250 Cal. Rptr. 3d 754",
            "446 P.3d 262",
            "7 Cal. 5th 1034"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathan Rice v. Reliastar Life Insurance Co.",
          "cluster_id": 2745906,
          "cite": [
            "770 F.3d 1122",
            "59 Employee Benefits Cas. (BNA) 2369",
            "2014 U.S. App. LEXIS 20581",
            "2014 WL 5431994"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Flippo v. West Virginia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1854815) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 75,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 75,
        "triage_read": 5,
        "triage_snippet_classified": 70
      },
      "lane2_top_cited": {
        "query": "cites:(1854815)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNSZzPTQzMDExOTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%281854815%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(1854815)",
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
    "complete_query": "cites:(1854815)",
    "indexed_citing_opinions": 94,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1854815,
        "count": 94,
        "count_source": "search"
      }
    ],
    "citation_count": 198,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/flippo-v-west-virginia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2Njk5MjYmcz00NDUyNTc3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%281854815%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1854815,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1854815,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1854815,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1854815,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T03:37:52Z",
    "date_modified": "2026-07-06T07:43:20Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:38:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:38:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:41:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:38:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Flippo v. West Virginia

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b223-10">
  Per Curiam.
 </author>
<p id="b223-11">
  Petitioner’s motion to suppress evidence seized in a warrantless search of a “homicide crime scene” was denied on the ground that the police were entitled to make a thorough search of any crime scene and the objects found
  <span citation-index="1" class="star-pagination" label="12"> 
   *12
   </span>
  there. Because the rule applied directly conflicts with
  <em>
   Mincey
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we reverse.
 </p>
<p id="b224-5">
  One night in 1996, petitioner and his wife were vacationing at a cabin in a state park. After petitioner called 911 to report that they had been attacked, the police arrived to find petitioner waiting outside the cabin, with injuries to his head and legs. After questioning him, an officer entered the building and found the body of petitioner’s wife, with fatal head wounds. The officers closed off the area, took petitioner to the hospital, and searched the exterior and environs of the cabin for footprints or signs of forced entry. When a police photographer arrived at about 5:30 a.m., the officers reentered the building and proceeded to “process the crime scene.” Brief in Opposition 5. For over 16 hours, they took photographs, collected evidence, and searched through the contents of the cabin. According to the trial court, “[a]t the crime scene, the investigating officers found on a table in Cabin 13, among other things, a briefcase, which they, in the ordinary course of investigating a homicide, opened, wherein they found and seized various photographs and negatives.” Indictment No. 96-F-119 (Cir. Ct. Fayette County, W. Va., May 28, 1997), App. A to Pet. for Cert., p. 2.
 </p>
<p id="b224-6">
  Petitioner was indicted for the murder of his wife and moved to suppress the photographs and negatives discovered in an envelope in the closed briefcase during the search.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  He argued that the police had obtained no warrant, and that no exception to the warrant requirement justified the search and seizure.
 </p>
<p id="b225-4">
<span citation-index="1" class="star-pagination" label="13"> 
   *13
   </span>
  In briefs to the trial court, petitioner contended that
  <em>
   Mincey
  </em>
  v.
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Arizona, supra,</a></span>
  </em>
  rejects a “crime scene exception” to the warrant requirement of the Fourth Amendment. The State also cited
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>;
  </em>
  it argued that the police may-conduct an immediate investigation of a crime scene to preserve evidence from intentional or accidental destruction,
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona"><em>
   id.,
  </em>
  at 394</a></span>, and characterized the police activity in this case as “crime scene search and inventory,” Brief in Opposition 12. The State also relied on the “plain view” exception,
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey, supra,</a></span>
  </em>
  at 393 (citing
  <em>
   Michigan
  </em>
  v.
  <em>
   Tyler,
  </em>
  <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U.S. 499, 509-510</a></span> (1978)), noting only, however, that the briefcase was unlocked.
 </p>
<p id="b225-5">
  In denying the motion, the trial court said nothing about inventory or plain view, but instead approved the search as one of a “homicide crime scene”:
 </p>
<blockquote id="b225-6">
  “The Court also concludes that investigating officers, having secured, for investigative purposes, the homicide crime scene, were clearly within the law to conduet a thorough investigation and examination of anything and everything found within the crime scene area. The examination of [the] briefcase found on the table near the body of a homicide victim in this case is clearly something an investigating officer could lawfully examine.” App. A to Pet. for Cert., at 3.
 </blockquote>
<p id="b225-7">
  After hearing an oral presentation of petitioner’s petition for appeal of this ruling, and with the full record before it, the Supreme Court of Appeals of West Virginia denied discretionary review. No. 982196 (Jan. 13, 1999), App. B to Pet. for Cert.
 </p>
<p id="b225-8">
  A warrantless search by the police is invalid unless it falls within one of the narrow and well-delineated exceptions to the warrant requirement,
  <em>
   Katz
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967), none of which the trial court invoked
  <span citation-index="1" class="star-pagination" label="14"> 
   *14
   </span>
  here.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  It simply found that after the homicide crime scene was secured for investigation, a search of “anything and everything found within the crime scene area” was “within the law.” App. A to Pet. for Cert., at 3.
 </p>
<p id="b226-5">
  This position squarely conflicts with
  <em>
   Mincey
  </em>
  v.
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Arizona, supra,</a></span>
  </em>
  where we rejected the contention that there is a “murder scene exception” to the Warrant Clause of the Fourth Amendment. We noted that police may make war-rantless entries onto premises if they reasonably believe a person is in need of immediate aid and may make prompt warrantless searches of a homicide scene for possible other victims or a killer on the premises,
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#392" aria-description="Citation for case: Mincey v. Arizona"><em>
   id.,
  </em>
  at 392</a></span>, but we rejected any general “murder scene exception” as “inconsistent with the Fourth and Fourteenth Amendments— ... the warrantless search of Mincey’s apartment was not constitutionally permissible simply because a homicide had recently occurred there.”
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#395" aria-description="Citation for case: Mincey v. Arizona"><em>
   Id.,
  </em>
  at 395</a></span>; see also
  <em>
   Thompson
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="111282"><a href="/opinion/111282/thompson-v-louisiana/#21" aria-description="Citation for case: Thompson v. Louisiana">469 U. S. 17, 21</a></span> (1984)
  <em>
   (per curiam). Mincey
  </em>
  controls here.
 </p>
<p id="b226-6">
  Although the trial court made no attempt to distinguish
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>,
  </em>
  the State contends that the trial court’s ruling is supportable on the theory that petitioner’s direction of the police to the scene of the attack implied consent to search as
  <span citation-index="1" class="star-pagination" label="15"> 
   *15
   </span>
  they did. As in
  <em>
   Thompson
  </em>
  v.
  <span class="citation" data-id="111282"><a href="/opinion/111282/thompson-v-louisiana/#23" aria-description="Citation for case: Thompson v. Louisiana"><em>
   Louisiana, supra,
  </em>
  at 23</a></span>, however, we express no opinion on whether the search here might be justified as consensual, as “the issue of consent is ordinarily a factual issue unsuitable for our consideration in the first instance.” Nor, of course, do we take any position on the applicability of any other exception to the warrant rule, or the harmlessness
  <em>
   vel non
  </em>
  of any error in receiving this evidence. Any such matters, properly raised, may be resolved on remand. <span class="citation" data-id="111282"><a href="/opinion/111282/thompson-v-louisiana/#21" aria-description="Citation for case: Thompson v. Louisiana">469 U. S., at 21</a></span>; see also
  <em>
   United States
  </em>
  v.
  <em>
   Matlock,
  </em>
  <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U. S. 164</a></span> (1974).
 </p>
<p id="b227-5">
  The motion for leave to proceed
  <em>
   in forma pauperis
  </em>
  and the petition for a writ of certiorari are granted, the judgment of the Circuit Court of West Virginia, Payette County, is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b227-6">
<em>
   It is so ordered.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b224-7">
   The photographs included several taken of a man who appears to be taking off his jeans. Hie was later identified as Joel Boggess, a friend of petitioner and a member of the congregation of which petitioner was the minister. At trial, the prosecution introduced the photographs as evidence of petitioner’s relationship with Mr. Boggess and argued that the victim’s displeasure with this relationship was one of the reasons that petitioner may have been motivated to kill her.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b226-7">
   The State suggests that the trial court’s finding that the search was “within the law” could be read as premised on the theories of plain view, exigent circumstances, and inventory that the State advanced below. No trace of this reasoning appears in the trial court’s opinion, which instead appears to undermine the State’s interpretation. It seems implausible that the court found that there was a risk of intentional or accidental destruction of evidence at a “secured” crime scene or that the authorities were performing a mere inventory search when the premises had been secured for “investigative purposes” and the officers opened the briefcase “in the ordinary course of investigating a homicide.” Nor does the court’s validation of “investiga[ting] and examin[ing]... anything and everything found within the crime scene area,” including photographs inside a closed briefcase, apparently rest on the plain-view exception. App. A to Pet. for Cert., at 2, 3.
  </p>
</div></div></opinion>
```

---
