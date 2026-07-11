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

## GROUP: _overhaul2/lake/cases/Montejo v. Louisiana.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Montejo v. Louisiana"
type: case
citation: "556 U.S. 778 (2009)"
parallel_cite: "129 S. Ct. 2079; 173 L. Ed. 2d 955"
neutral_cite: 2009 U.S. LEXIS 3973
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-05-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-05-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Montejo v. Louisiana
  varies_by_point: false
  scope_note: "Montejo itself overruled Michigan v. Jackson; Montejo is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145873/montejo-v-louisiana/"
  cluster_id: 145873
  opinion_id: 145873
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Michigan v. Jackson]]", "[[Edwards v. Arizona]]", "[[McNeil v. Wisconsin]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "waiver", "interrogation"]
holding: "A defendant may validly waive his Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been…"
lake:
  record_id: Montejo v. Louisiana
  status: verified
  projected_at: 2026-07-06
---

# Montejo v. Louisiana

*556 U.S. 778 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Montejo was arrested for murder. At a preliminary "72-hour hearing," the court ordered the appointment of counsel. Before Montejo met his appointed lawyer, detectives read him his *[[Miranda v. Arizona|Miranda]]* rights; he agreed to accompany them to locate the murder weapon and, during the trip, wrote an inculpatory letter of apology to the victim's widow. He sought to suppress the letter under *[[Michigan v. Jackson]]* because police had initiated interrogation after counsel was appointed.

## Issue
Whether, once the Sixth Amendment right to counsel has attached and counsel has been appointed, a waiver of counsel during police-initiated interrogation is presumed invalid under *[[Michigan v. Jackson]]*.

## Rule
No — police are not categorically barred from initiating interrogation. The Court overruled the *[[Michigan v. Jackson]]* presumption and held that a defendant may waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been requested or appointed, provided the waiver is voluntary, knowing, and intelligent. A standard set of *[[Miranda v. Arizona|Miranda]]* warnings and waiver ordinarily suffices to relinquish the Sixth Amendment right, because the *Miranda–Edwards–Minnick* line already protects a defendant who does not wish to be questioned without counsel. "Michigan v. Jackson should be and now is overruled." — 556 U.S. at 797. ^pin-797

## Application
Because the *[[Michigan v. Jackson|Jackson]]* presumption no longer applies, the fact that counsel had been appointed at Montejo's 72-hour hearing did not by itself render his later waiver invalid. The Court did not decide admissibility itself; it [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] so that Montejo could argue — under *[[Edwards v. Arizona]]*, a theory he had not raised below — that he had earlier invoked his right to counsel and that his letter of apology should therefore be suppressed.

## Conclusion
The Louisiana Supreme Court correctly rejected Montejo's *[[Michigan v. Jackson|Jackson]]* claim, but the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] to allow Montejo to pursue an *[[Edwards v. Arizona|Edwards]]*-based suppression argument.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Montejo **overruled** [[Michigan v. Jackson]], eliminating the Sixth Amendment presumption against police-initiated interrogation after the right to counsel attaches; a defendant who does not wish to be questioned without counsel is now protected through the Fifth Amendment *[[Edwards v. Arizona|Edwards]]*/*[[Miranda v. Arizona|Miranda]]* regime.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Montejo v. Louisiana*, 556 U.S. 778 (2009) — https://www.courtlistener.com/opinion/145873/montejo-v-louisiana/ — pinpoint: 797 (CL opinion in slip-opinion format; U.S. Reports page per official citation).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "df186178762a6203", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Montejo v. Louisiana"}, "payload": {"all": [{"cite": "556 U.S. 778", "page": "778", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "556"}, {"cite": "129 S. Ct. 2079", "page": "2079", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "129"}, {"cite": "173 L. Ed. 2d 955", "page": "955", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "173"}, {"cite": "2009 U.S. LEXIS 3973", "page": "3973", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2009"}], "display": "556 U.S. 778", "official": {"cite": "556 U.S. 778", "page": "778", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "556"}, "official_selection_present": true, "record_id": "Montejo v. Louisiana"}}
{"assertion_id": "85d09f01c27766a7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-797", "record_id": "Montejo v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-797", "pinpoint_status": "slip-only", "quote": "the court ordered the appointment of counsel. Before Montejo met his appointed lawyer, detectives read him his *Miranda* rights; he agreed to accompany them to locate the murder weapon and, during the trip, wrote an inculpatory letter of apology to the victim's widow. He sought to suppress the letter under *Michigan v. Jackson* because police had initiated interrogation after counsel was appointed. ## Issue Whether, once the Sixth Amendment right to counsel has attached and counsel has been appointed, a waiver of counsel during police-initiated interrogation is presumed invalid under *Michigan v. Jackson*. ## Rule No — police are not categorically barred from initiating interrogation. The Court overruled the *Michigan v. Jackson* presumption and held that a defendant may waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been requested or appointed, provided the waiver is voluntary, knowing, and intelligent. A standard set of *Miranda* warnings and waiver ordinarily suffices to relinquish the Sixth Amendment right, because the *Miranda–Edwards–Minnick* line already protects a defendant who does not wish to be questioned without counsel.", "quote_fidelity": "mismatch", "record_id": "Montejo v. Louisiana", "star_marker": null}}
{"assertion_id": "82fade4c5948cb8c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Montejo v. Louisiana"}, "payload": {"as_of_content": "2009-05-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Montejo v. Louisiana", "scope_note": "Montejo itself overruled Michigan v. Jackson; Montejo is good law.", "varies_by_point": false}}
```

### lake record — Montejo v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Montejo v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Montejo v. Louisiana",
    "case_name_short": "Montejo",
    "case_name_full": "Montejo v. Louisiana",
    "input_case_name": "Montejo v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-05-26",
    "year": 2009,
    "docket": null,
    "cluster_id": 145873,
    "lead_opinion_id": 145873,
    "sibling_ids": [
      145873,
      9435335,
      9435336
    ],
    "absolute_url": "/opinion/145873/montejo-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 778",
      "volume": "556",
      "reporter": "U.S.",
      "page": "778",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 2079",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 955",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "955",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3973",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3973",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 778",
        "volume": "556",
        "reporter": "U.S.",
        "page": "778",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 2079",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "2079",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 955",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "955",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3973",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3973",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 778",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 778",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-797",
      "page": null,
      "quote": "the court ordered the appointment of counsel. Before Montejo met his appointed lawyer, detectives read him his *Miranda* rights; he agreed to accompany them to locate the murder weapon and, during the trip, wrote an inculpatory letter of apology to the victim's widow. He sought to suppress the letter under *Michigan v. Jackson* because police had initiated interrogation after counsel was appointed. ## Issue Whether, once the Sixth Amendment right to counsel has attached and counsel has been appointed, a waiver of counsel during police-initiated interrogation is presumed invalid under *Michigan v. Jackson*. ## Rule No \u2014 police are not categorically barred from initiating interrogation. The Court overruled the *Michigan v. Jackson* presumption and held that a defendant may waive the Sixth Amendment right to counsel during police-initiated interrogation even after counsel has been requested or appointed, provided the waiver is voluntary, knowing, and intelligent. A standard set of *Miranda* warnings and waiver ordinarily suffices to relinquish the Sixth Amendment right, because the *Miranda\u2013Edwards\u2013Minnick* line already protects a defendant who does not wish to be questioned without counsel.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-05-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Montejo v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Montejo itself overruled Michigan v. Jackson; Montejo is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "the State of Texas v. Kevin Castanedanieto",
          "cluster_id": 7857287,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cook v. State",
          "cluster_id": 10679925,
          "cite": [
            "870 S.E.2d 758",
            "313 Ga. 471"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dwight Smith",
          "cluster_id": 4452817,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gustavo Andres Vasquez v. State",
          "cluster_id": 4252017,
          "cite": [
            "501 S.W.3d 691",
            "2016 Tex. App. LEXIS 9349",
            "2016 WL 4483462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Francis",
          "cluster_id": 4243552,
          "cite": [
            "140 A.3d 927",
            "322 Conn. 247",
            "2016 Conn. LEXIS 231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Bergeron",
          "cluster_id": 3207734,
          "cite": [
            "824 F.3d 148",
            "2016 U.S. App. LEXIS 9732",
            "2016 WL 3031089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane1_negative"
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
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jae Lee v. United States",
          "cluster_id": 4403800,
          "cite": [
            "582 U.S. 357",
            "2017 U.S. LEXIS 4045",
            "137 S. Ct. 1958",
            "198 L. Ed. 2d 476",
            "26 Fla. L. Weekly Fed. S 733",
            "85 U.S.L.W. 4412",
            "2017 WL 2694701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Morrow v. Barry Balaski",
          "cluster_id": 891221,
          "cite": [
            "719 F.3d 160",
            "98 A.L.R. 6th 777",
            "2013 WL 2466892",
            "2013 U.S. App. LEXIS 11246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janus v. State, County, and Municipal Employees",
          "cluster_id": 4511640,
          "cite": [
            "585 U.S. 878",
            "138 S. Ct. 2448",
            "201 L. Ed. 2d 924",
            "2018 U.S. LEXIS 4028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loper Bright Enterprises v. Raimondo",
          "cluster_id": 10600041,
          "cite": [
            "603 U.S. 369"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loper Bright Enterprises v. Raimondo",
          "cluster_id": 9986254,
          "cite": [
            "603 U.S. 369"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cox",
          "cluster_id": 2345288,
          "cite": [
            "983 A.2d 666",
            "603 Pa. 223",
            "2009 Pa. LEXIS 2423"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby v. Dixon",
          "cluster_id": 616807,
          "cite": [
            "181 L. Ed. 2d 328",
            "132 S. Ct. 26",
            "565 U.S. 23",
            "2011 U.S. LEXIS 7926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lansing Schools Education Ass'n v. Lansing Board of Education",
          "cluster_id": 830370,
          "cite": [
            "487 Mich. 349"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hooks v. Workman",
          "cluster_id": 805977,
          "cite": [
            "689 F.3d 1148",
            "2012 WL 3140916",
            "2012 U.S. App. LEXIS 16150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 4746633,
          "cite": [
            "590 U.S. 83"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gamble v. United States",
          "cluster_id": 4630267,
          "cite": [
            "587 U.S. 678",
            "139 S. Ct. 1960",
            "204 L. Ed. 2d 322",
            "2019 U.S. LEXIS 4173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bonilla-Barraza",
          "cluster_id": 2625609,
          "cite": [
            "209 P.3d 1090",
            "2009 WL 1741945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1346679,
          "cite": [
            "697 S.E.2d 757",
            "287 Ga. 646",
            "2010 Fulton County D. Rep. 2574",
            "2010 Ga. LEXIS 484"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
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
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eldridge v. Johndrow",
          "cluster_id": 2775233,
          "cite": [
            "2015 UT 21",
            "345 P.3d 553",
            "2015 Utah LEXIS 67",
            "779 Utah Adv. Rep. 112",
            "2015 WL 404491"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ayers v. Hudson",
          "cluster_id": 176545,
          "cite": [
            "623 F.3d 301",
            "2010 U.S. App. LEXIS 20487",
            "2010 WL 3894463"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pecina, Alfredo Leyva",
          "cluster_id": 2947167,
          "cite": [
            "361 S.W.3d 68",
            "2012 WL 204293",
            "2012 Tex. Crim. App. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Howard Hawk Willis",
          "cluster_id": 4236316,
          "cite": [
            "496 S.W.3d 653",
            "2016 Tenn. LEXIS 405"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Montejo v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145873 OR 9435335 OR 9435336) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDM4NzMyODAwMDAwJnM9MjgyNjA1MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145873+OR+9435335+OR+9435336%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(145873 OR 9435335 OR 9435336)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MyZzPTgwNTkxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145873+OR+9435335+OR+9435336%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145873 OR 9435335 OR 9435336)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 0,
        "triage_snippet_classified": 49
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145873 OR 9435335 OR 9435336)",
    "indexed_citing_opinions": 391,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145873,
        "count": 307,
        "count_source": "search"
      },
      {
        "opinion_id": 9435335,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9435336,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 669,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/montejo-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTMwNDMmcz0xMDAxNzc3NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145873+OR+9435335+OR+9435336%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145873,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 117863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 118417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 134725,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 142900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145706,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 145744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 577034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145873,
        "cited_id": 1793654,
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
    "date_created": "2026-07-05T14:30:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:36:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:30:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Montejo v. Louisiana

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                       MONTEJO v. LOUISIANA

      CERTIORARI TO THE SUPREME COURT OF LOUISIANA

    No. 07–1529. Argued January 13, 2009—Decided May 26, 2009
At a preliminary hearing required by Louisiana law, petitioner Montejo
  was charged with first-degree murder, and the court ordered the ap
  pointment of counsel. Later that day, the police read Montejo his
  rights under Miranda v. Arizona, 384 U. S. 436, and he agreed to go
  along on a trip to locate the murder weapon. During the excursion,
  he wrote an inculpatory letter of apology to the victim’s widow. Upon
  returning, he finally met his court-appointed attorney. At trial, his
  letter was admitted over defense objection, and he was convicted and
  sentenced to death. Affirming, the State Supreme Court rejected his
  claim that the letter should have been suppressed under the rule of
  Michigan v. Jackson, 475 U. S. 625, which forbids police to initiate
  interrogation of a criminal defendant once he has invoked his right to
  counsel at an arraignment or similar proceeding. The court reasoned
  that Jackson’s prophylactic protection is not triggered unless the de
  fendant has actually requested a lawyer or has otherwise asserted
  his Sixth Amendment right to counsel; and that, since Montejo stood
  mute at his hearing while the judge ordered the appointment of
  counsel, he had made no such request or assertion.
Held:
    1. Michigan v. Jackson should be and now is overruled. Pp. 3–18.
       (a) The State Supreme Court’s interpretation of Jackson would
 lead to practical problems. Requiring an initial “invocation” of the
 right to counsel in order to trigger the Jackson presumption, as the
 court below did, might work in States that require an indigent defen
 dant formally to request counsel before an appointment is made, but
 not in more than half the States, which appoint counsel without re
 quest from the defendant. Pp. 3–6.
       (b) On the other hand, Montejo’s solution is untenable as a theo
 retical and doctrinal matter. Eliminating the invocation requirement
2                       MONTEJO v. LOUISIANA

                                  Syllabus

    entirely would depart fundamentally from the rationale of Jackson,
    whose presumption was created by analogy to a similar prophylactic
    rule established in Edwards v. Arizona, 451 U. S. 477, to protect the
    Fifth Amendment-based Miranda right. Both Edwards and Jackson
    are meant to prevent police from badgering defendants into changing
    their minds about the right to counsel once they have invoked it, but
    a defendant who never asked for counsel has not yet made up his
    mind in the first instance. Pp. 6–13.
          (c) Stare decisis does not require the Court to expand signifi
    cantly the holding of a prior decision in order to cure its practical de
    ficiencies. To the contrary, the fact that a decision has proved “un
    workable” is a traditional ground for overruling it. Payne v.
    Tennessee, 501 U. S. 808, 827. Beyond workability, the relevant fac
    tors include the precedent’s antiquity, the reliance interests at stake,
    and whether the decision was well reasoned. Pearson v. Callahan,
    555 U. S. ___, ___. The first two cut in favor of jettisoning Jackson:
    the opinion is only two decades old, and eliminating it would not up
    set expectations, since any criminal defendant learned enough to or
    der his affairs based on Jackson’s rule would also be perfectly capable
    of interacting with the police on his own. As for the strength of Jack
    son’s reasoning, when this Court creates a prophylactic rule to pro
    tect a constitutional right, the relevant “reasoning” is the weighing of
    the rule’s benefits against its costs. Jackson’s marginal benefits are
    dwarfed by its substantial costs. Even without Jackson, few badger
    ing-induced waivers, if any, would be admitted at trial because the
    Court has taken substantial other, overlapping measures to exclude
    them. Under Miranda, any suspect subject to custodial interrogation
    must be advised of his right to have a lawyer present. 384 U. S., at
    474. Under Edwards, once such a defendant “has invoked his
    [Miranda] right,” interrogation must stop. 451 U. S., at 484. And
    under Minnick v. Mississippi, 498 U. S. 146, no subsequent interro
    gation may take place until counsel is present. Id., at 153. These
    three layers of prophylaxis are sufficient. On the other side of the
    equation, the principal cost of applying Jackson’s rule is that crimes
    can go unsolved and criminals unpunished when uncoerced confes
    sions are excluded and when officers are deterred from even trying to
    obtain confessions. The Court concludes that the Jackson rule does
    not “pay its way,” United States v. Leon, 468 U. S. 897, 907–908, n. 6,
    and thus the case should be overruled. Pp. 13–18.
       2. Montejo should nonetheless be given an opportunity to contend
    that his letter of apology should have been suppressed under the Ed
    wards rule. He understandably did not pursue an Edwards objec
    tion, because Jackson offered broader protections, but the decision
    here changes the legal landscape. Pp. 18–19.
                     Cite as: 556 U. S. ____ (2009)                    3

                                Syllabus

06–1807 (La.), 974 So. 2d 1238, vacated and remanded.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, and ALITO, JJ., joined. ALITO, J., filed a
concurring opinion, in which KENNEDY, J., joined. STEVENS, J., filed a
dissenting opinion, in which SOUTER and GINSBURG, JJ., joined, and in
which BREYER, J., joined, except for n. 5. BREYER, J., filed a dissenting
opinion.
                        Cite as: 556 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1529
                                   _________________


          JESSE JAY MONTEJO, PETITIONER v. 

                     LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                                 [May 26, 2009] 


   JUSTICE SCALIA delivered the opinion of the Court.
   We consider in this case the scope and continued viabil
ity of the rule announced by this Court in Michigan v.
Jackson, 475 U. S. 625 (1986), forbidding police to initiate
interrogation of a criminal defendant once he has re
quested counsel at an arraignment or similar proceeding.
                              I
  Petitioner Jesse Montejo was arrested on September 6,
2002, in connection with the robbery and murder of Lewis
Ferrari, who had been found dead in his own home one
day earlier. Suspicion quickly focused on Jerry Moore, a
disgruntled former employee of Ferrari’s dry cleaning
business. Police sought to question Montejo, who was a
known associate of Moore.
  Montejo waived his rights under Miranda v. Arizona,
384 U. S. 436 (1966), and was interrogated at the sheriff’s
office by police detectives through the late afternoon and
evening of September 6 and the early morning of Septem
ber 7. During the interrogation, Montejo repeatedly
changed his account of the crime, at first claiming that he
2                     MONTEJO v. LOUISIANA

                          Opinion of the Court

had only driven Moore to the victim’s home, and ulti
mately admitting that he had shot and killed Ferrari in
the course of a botched burglary. These police interroga
tions were videotaped.
   On September 10, Montejo was brought before a judge
for what is known in Louisiana as a “72-hour hearing”—a
preliminary hearing required under state law.1 Although
the proceedings were not transcribed, the minute record
indicates what transpired: “The defendant being charged
with First Degree Murder, Court ordered N[o] Bond set in
this matter. Further, Court ordered the Office of Indigent
Defender be appointed to represent the defendant.” App.
to Pet. for Cert. 63a.
   Later that same day, two police detectives visited Mon
tejo back at the prison and requested that he accompany
them on an excursion to locate the murder weapon (which
Montejo had earlier indicated he had thrown into a lake).
After some back-and-forth, the substance of which re
mains in dispute, Montejo was again read his Miranda
rights and agreed to go along; during the excursion, he
wrote an inculpatory letter of apology to the victim’s
widow. Only upon their return did Montejo finally meet
his court-appointed attorney, who was quite upset that the
detectives had interrogated his client in his absence.
   At trial, the letter of apology was admitted over defense
objection. The jury convicted Montejo of first-degree mur
der, and he was sentenced to death.
   The Louisiana Supreme Court affirmed the conviction
and sentence. 06–1807 (1/16/08), 974 So. 2d 1238 (2008).
As relevant here, the court rejected Montejo’s argument
that under the rule of Jackson, supra, the letter should
——————
  1 “The sheriff or law enforcement officer having custody of an arrested

person shall bring him promptly, and in any case within seventy-two
hours from the time of the arrest, before a judge for the purpose of
appointment of counsel.” La. Code Crim. Proc. Ann., Art. 230.1(A)
(West Supp. 2009).
                 Cite as: 556 U. S. ____ (2009)            3

                     Opinion of the Court

have been suppressed. 974 So. 2d, at 1261. Jackson held
that “if police initiate interrogation after a defendant’s
assertion, at an arraignment or similar proceeding, of his
right to counsel, any waiver of the defendant’s right to
counsel for that police-initiated interrogation is invalid.”
475 U. S., at 636.
  Citing a decision of the United States Court of Appeals
for the Fifth Circuit, Montoya v. Collins, 955 F. 2d 279
(1992), the Louisiana Supreme Court reasoned that the
prophylactic protection of Jackson is not triggered unless
and until the defendant has actually requested a lawyer or
has otherwise asserted his Sixth Amendment right to
counsel. 974 So. 2d, at 1260–1261, and n. 68. Because
Montejo simply stood mute at his 72-hour hearing while
the judge ordered the appointment of counsel, he had
made no such request or assertion. So the proper inquiry,
the court ruled, was only whether he had knowingly,
intelligently, and voluntarily waived his right to have
counsel present during the interaction with the police. Id.,
at 1261. And because Montejo had been read his Miranda
rights and agreed to waive them, the Court answered that
question in the affirmative, 974 So. 2d, at 1262, and up
held the conviction.
  We granted certiorari. 554 U. S. ___ (2008).
                            II
   Montejo and his amici raise a number of pragmatic
objections to the Louisiana Supreme Court’s interpreta
tion of Jackson. We agree that the approach taken below
would lead either to an unworkable standard, or to arbi
trary and anomalous distinctions between defendants in
different States. Neither would be acceptable.
   Under the rule adopted by the Louisiana Supreme
Court, a criminal defendant must request counsel, or
otherwise “assert” his Sixth Amendment right at the
preliminary hearing, before the Jackson protections are
4                 MONTEJO v. LOUISIANA

                     Opinion of the Court

triggered. If he does so, the police may not initiate further
interrogation in the absence of counsel. But if the court on
its own appoints counsel, with the defendant taking no
affirmative action to invoke his right to counsel, then
police are free to initiate further interrogations provided
that they first obtain an otherwise valid waiver by the
defendant of his right to have counsel present.
   This rule would apply well enough in States that require
the indigent defendant formally to request counsel before
any appointment is made, which usually occurs after the
court has informed him that he will receive counsel if he
asks for it. That is how the system works in Michigan, for
example, Mich. Ct. Rule 6.005(A) (2009), whose scheme
produced the factual background for this Court’s decision
in Michigan v. Jackson. Jackson, like all other repre
sented indigent defendants in the State, had requested
counsel in accordance with the applicable state law.
   But many States follow other practices. In some two
dozen, the appointment of counsel is automatic upon a
finding of indigency, e.g., Kan. Stat. Ann. §22–4503(c)
(2007); and in a number of others, appointment can be
made either upon the defendant’s request or sua sponte by
the court, e.g., Del. Code Ann., Tit. 29, §4602(a) (2003).
See App. to Brief for National Legal Aid & Defender Assn.
et al. as Amici Curiae 1a–21a. Nothing in our Jackson
opinion indicates whether we were then aware that not all
States require that a defendant affirmatively request
counsel before one is appointed; and of course we had no
occasion there to decide how the rule we announced would
apply to these other States.
   The Louisiana Supreme Court’s answer to that unre
solved question is troublesome. The central distinction it
draws—between defendants who “assert” their right to
counsel and those who do not—is exceedingly hazy when
applied to States that appoint counsel absent request from
the defendant. How to categorize a defendant who merely
                 Cite as: 556 U. S. ____ (2009)            5

                     Opinion of the Court

asks, prior to appointment, whether he will be appointed
counsel? Or who inquires, after the fact, whether he has
been? What treatment for one who thanks the court after
the appointment is made? And if the court asks a defen
dant whether he would object to appointment, will a quick
shake of his head count as an assertion of his right?
  To the extent that the Louisiana Supreme Court’s rule
also permits a defendant to trigger Jackson through the
“acceptance” of counsel, that notion is even more mysteri
ous: How does one affirmatively accept counsel appointed
by court order? An indigent defendant has no right to
choose his counsel, United States v. Gonzalez-Lopez, 548
U. S. 140, 151 (2006), so it is hard to imagine what his
“acceptance” would look like, beyond the passive silence
that Montejo exhibited.
  In practice, judicial application of the Louisiana rule in
States that do not require a defendant to make a request
for counsel could take either of two paths. Courts might
ask on a case-by-case basis whether a defendant has
somehow invoked his right to counsel, looking to his con
duct at the preliminary hearing—his statements and
gestures—and the totality of the circumstances. Or,
courts might simply determine as a categorical matter
that defendants in these States—over half of those in the
Union—simply have no opportunity to assert their right to
counsel at the hearing and are therefore out of luck.
  Neither approach is desirable. The former would be
particularly impractical in light of the fact that, as amici
describe, preliminary hearings are often rushed, and are
frequently not recorded or transcribed. Brief for National
Legal Aid & Defender Assn. et al. 25–30. The sheer vol
ume of indigent defendants, see id., at 29, would render
the monitoring of each particular defendant’s reaction to
the appointment of counsel almost impossible. And some
times the defendant is not even present. E.g., La. Code
Crim. Proc. Ann., Art. 230.1(A) (West Supp. 2009) (allow
6                 MONTEJO v. LOUISIANA

                     Opinion of the Court

ing court to appoint counsel if defendant is “unable to
appear”). Police who did not attend the hearing would
have no way to know whether they could approach a par
ticular defendant; and for a court to adjudicate that ques
tion ex post would be a fact-intensive and burdensome
task, even if monitoring were possible and transcription
available. Because “clarity of . . . command” and “cer
tainty of . . . application” are crucial in rules that govern
law enforcement, Minnick v. Mississippi, 498 U. S. 146,
151 (1990), this would be an unfortunate way to proceed.
See also Moran v. Burbine, 475 U. S. 412, 425–426 (1986).
   The second possible course fares no better, for it would
achieve clarity and certainty only at the expense of intro
ducing arbitrary distinctions: Defendants in States that
automatically appoint counsel would have no opportunity
to invoke their rights and trigger Jackson, while those in
other States, effectively instructed by the court to request
counsel, would be lucky winners. That sort of hollow
formalism is out of place in a doctrine that purports to
serve as a practical safeguard for defendants’ rights.
                             III
  But if the Louisiana Supreme Court’s application of
Jackson is unsound as a practical matter, then Montejo’s
solution is untenable as a theoretical and doctrinal matter.
Under his approach, once a defendant is represented by
counsel, police may not initiate any further interrogation.
Such a rule would be entirely untethered from the original
rationale of Jackson.
                                A
  It is worth emphasizing first what is not in dispute or at
stake here. Under our precedents, once the adversary
judicial process has been initiated, the Sixth Amendment
guarantees a defendant the right to have counsel present
at all “critical” stages of the criminal proceedings. United
                 Cite as: 556 U. S. ____ (2009)           7

                     Opinion of the Court

States v. Wade, 388 U. S. 218, 227–228 (1967); Powell v.
Alabama, 287 U. S. 45, 57 (1932). Interrogation by the
State is such a stage. Massiah v. United States, 377 U. S.
201, 204–205 (1964); see also United States v. Henry, 447
U. S. 264, 274 (1980).
  Our precedents also place beyond doubt that the Sixth
Amendment right to counsel may be waived by a defen
dant, so long as relinquishment of the right is voluntary,
knowing, and intelligent. Patterson v. Illinois, 487 U. S.
285, 292, n. 4 (1988); Brewer v. Williams, 430 U. S. 387,
404 (1977); Johnson v. Zerbst, 304 U. S. 458, 464 (1938).
The defendant may waive the right whether or not he is
already represented by counsel; the decision to waive need
not itself be counseled. Michigan v. Harvey, 494 U. S. 344,
352–353 (1990). And when a defendant is read his
Miranda rights (which include the right to have counsel
present during interrogation) and agrees to waive those
rights, that typically does the trick, even though the
Miranda rights purportedly have their source in the Fifth
Amendment:
    “As a general matter . . . an accused who is admon
    ished with the warnings prescribed by this Court in
    Miranda . . . has been sufficiently apprised of the na
    ture of his Sixth Amendment rights, and of the conse
    quences of abandoning those rights, so that his waiver
    on this basis will be considered a knowing and intelli
    gent one.” Patterson, supra, at 296.
   The only question raised by this case, and the only one
addressed by the Jackson rule, is whether courts must
presume that such a waiver is invalid under certain cir
cumstances. 475 U. S., at 630, 633. We created such a
presumption in Jackson by analogy to a similar prophylac
tic rule established to protect the Fifth Amendment based
Miranda right to have counsel present at any custodial
interrogation. Edwards v. Arizona, 451 U. S. 477 (1981),
8                 MONTEJO v. LOUISIANA

                     Opinion of the Court

decided that once “an accused has invoked his right to
have counsel present during custodial interrogation . . .
[he] is not subject to further interrogation by the authori
ties until counsel has been made available,” unless he
initiates the contact. Id., at 484–485.
   The Edwards rule is “designed to prevent police from
badgering a defendant into waiving his previously as
serted Miranda rights,” Harvey, supra, at 350. It does this
by presuming his postassertion statements to be involun
tary, “even where the suspect executes a waiver and his
statements would be considered voluntary under tradi
tional standards.” McNeil v. Wisconsin, 501 U. S. 171, 177
(1991). This prophylactic rule thus “protect[s] a suspect’s
voluntary choice not to speak outside his lawyer’s pres
ence.” Texas v. Cobb, 532 U. S. 162, 175 (2001) (KENNEDY,
J., concurring).
   Jackson represented a “wholesale importation of the
Edwards rule into the Sixth Amendment.” Cobb, supra, at
175. The Jackson Court decided that a request for counsel
at an arraignment should be treated as an invocation of
the Sixth Amendment right to counsel “at every critical
stage of the prosecution,” 475 U. S., at 633, despite doubt
that defendants “actually inten[d] their request for counsel
to encompass representation during any further question
ing,” id., at 632–633, because doubts must be “resolved in
favor of protecting the constitutional claim,” id., at 633.
Citing Edwards, the Court held that any subsequent
waiver would thus be “insufficient to justify police
initiated interrogation.” 475 U. S., at 635. In other words,
we presume such waivers involuntary “based on the sup
position that suspects who assert their right to counsel are
unlikely to waive that right voluntarily” in subsequent
interactions with police. Harvey, supra, at 350.
   The dissent presents us with a revisionist view of Jack
son. The defendants’ request for counsel, it contends, was
important only because it proved that counsel had been
                     Cite as: 556 U. S. ____ (2009)                    9

                          Opinion of the Court

appointed. Such a non sequitur (nowhere alluded to in the
case) hardly needs rebuttal. Proceeding from this fanciful
premise, the dissent claims that the decision actually
established “a rule designed to safeguard a defendant’s
right to rely on the assistance of counsel,” post, at 6–7
(opinion of STEVENS, J.), not one “designed to prevent
police badgering,” post, at 7. To safeguard the right to
assistance of counsel from what? From a knowing and
voluntary waiver by the defendant himself? Unless the
dissent seeks to prevent a defendant altogether from
waiving his Sixth Amendment rights, i.e., to “imprison a
man in his privileges and call it the Constitution,” Adams
v. United States ex rel. McCann, 317 U. S. 269, 280
(1942)—a view with zero support in reason, history or case
law—the answer must be: from police pressure, i.e., badg
ering. The antibadgering rationale is the only way to
make sense of Jackson’s repeated citations of Edwards,
and the only way to reconcile the opinion with our waiver
jurisprudence.2
                            B
  With this understanding of what Jackson stands for and
whence it came, it should be clear that Montejo’s interpre
tation of that decision—that no represented defendant can
ever be approached by the State and asked to consent to
interrogation—is off the mark. When a court appoints
counsel for an indigent defendant in the absence of any
request on his part, there is no basis for a presumption
——————
   2 The dissent responds that Jackson also ensures that the defendant’s

counsel receives notice of any interrogation, post, at 6, n. 2.
But notice to what end? Surely not in order to protect some constitu
tional right to receive counsel’s advice regarding waiver of the right to
have counsel present. Contrary to the dissent’s intimations, neither the
advice nor the presence of counsel is needed in order to effectuate a
knowing waiver of the Sixth Amendment right. Our cases make clear
that the Miranda waivers typically suffice; indeed, even an unrepre
sented defendant can waive his right to counsel. See supra, at 7.
10                MONTEJO v. LOUISIANA

                     Opinion of the Court

that any subsequent waiver of the right to counsel will be
involuntary. There is no “initial election” to exercise the
right, Patterson, 487 U. S., at 291, that must be preserved
through a prophylactic rule against later waivers. No
reason exists to assume that a defendant like Montejo,
who has done nothing at all to express his intentions with
respect to his Sixth Amendment rights, would not be
perfectly amenable to speaking with the police without
having counsel present. And no reason exists to prohibit
the police from inquiring. Edwards and Jackson are
meant to prevent police from badgering defendants into
changing their minds about their rights, but a defendant
who never asked for counsel has not yet made up his mind
in the first instance.
  The dissent’s argument to the contrary rests on a flawed
a fortiori: “If a defendant is entitled to protection from
police-initiated interrogation under the Sixth Amendment
when he merely requests a lawyer, he is even more obvi
ously entitled to such protection when he has secured a
lawyer.” Post, at 3. The question in Jackson, however,
was not whether respondents were entitled to counsel
(they unquestionably were), but “whether respondents
validly waived their right to counsel,” 475 U. S., at 630;
and even if it is reasonable to presume from a defendant’s
request for counsel that any subsequent waiver of the right
was coerced, no such presumption can seriously be enter
tained when a lawyer was merely “secured” on the defen
dant’s behalf, by the State itself, as a matter of course. Of
course, reading the dissent’s analysis, one would have no
idea that Montejo executed any waiver at all.
  In practice, Montejo’s rule would prevent police-initiated
interrogation entirely once the Sixth Amendment right
attaches, at least in those States that appoint counsel
promptly without request from the defendant. As the
dissent in Jackson pointed out, with no expressed dis
agreement from the majority, the opinion “most assuredly
                 Cite as: 556 U. S. ____ (2009)          11

                     Opinion of the Court

[did] not hold that the Edwards per se rule prohibiting all
police-initiated interrogations applies from the moment
the defendant’s Sixth Amendment right to counsel at
taches, with or without a request for counsel by the defen
dant.” 475 U. S., at 640 (opinion of Rehnquist, J.). That
would have constituted a “shockingly dramatic restructur
ing of the balance this Court has traditionally struck
between the rights of the defendant and those of the larger
society.” Ibid.
  Montejo’s rule appears to have its theoretical roots in
codes of legal ethics, not the Sixth Amendment. The
American Bar Association’s Model Rules of Professional
Conduct (which nearly all States have adopted into law in
whole or in part) mandate that “a lawyer shall not com
municate about the subject of [a] representation with a
party the lawyer knows to be represented by another
lawyer in the matter, unless the lawyer has the consent of
the other lawyer or is authorized to do so by law or a court
order.” Model Rule 4.2 (2008). But the Constitution does
not codify the ABA’s Model Rules, and does not make
investigating police officers lawyers. Montejo’s proposed
rule is both broader and narrower than the Model Rule.
Broader, because Montejo would apply it to all agents of
the State, including the detectives who interrogated him,
while the ethical rule governs only lawyers. And nar
rower, because he agrees that if a defendant initiates
contact with the police, they may talk freely—whereas a
lawyer could be sanctioned for interviewing a represented
party even if that party “initiates” the communication and
consents to the interview. Model Rule 4.2, Comment 3.
  Montejo contends that our decisions support his inter
pretation of the Jackson rule. We think not. Many of the
cases he cites concern the substantive scope of the Sixth
Amendment—e.g., whether a particular interaction with
the State constitutes a “critical” stage at which counsel is
entitled to be present—not the validity of a Sixth Amend
12                     MONTEJO v. LOUISIANA

                          Opinion of the Court

ment waiver. See Maine v. Moulton, 474 U. S. 159 (1985);
Henry, 447 U. S. 264; Massiah, 377 U. S. 201; see also
Moran, 475 U. S. 412. Since everyone agrees that absent a
valid waiver, Montejo was entitled to a lawyer during the
interrogation, those cases do not advance his argument.
   Montejo also points to descriptions of the Jackson hold
ing in two later cases. In one, we noted that “analysis of
the waiver issue changes” once a defendant “obtains or
even requests counsel.” Harvey, 494 U. S., at 352. But
elsewhere in the same opinion, we explained that Jackson
applies “after a defendant requests assistance of counsel,”
494 U. S., at 349; “when a suspect charged with a crime
requests counsel outside the context of interrogation,” id.,
at 350; and to “suspects who assert their right to counsel,”
ibid. The accuracy of the “obtains” language is thus ques
tionable. Anyway, since Harvey held that evidence ob
tained in violation of the Jackson rule could be admitted
to impeach the defendant’s trial testimony, 494 U. S., at
346, the Court’s varying descriptions of when the rule was
violated were dicta. The dictum from the other decision,
Patterson, supra, at 290, n. 3, is no more probative.3
   The upshot is that even on Jackson’s own terms, it

——————
  3 In the cited passage, the Court noted that “[o]nce an accused has a

lawyer, a distinct set of constitutional safeguards aimed at preserving
the sanctity of attorney-client relationship takes effect.” Patterson, 487
U. S., at 290, n. 3. To support that proposition, the Court cited Maine
v. Moulton, 474 U. S. 159 (1985), which was not a case about waiver.
The passage went on to observe that “the analysis changes markedly
once an accused even requests the assistance of counsel,” 487 U. S., at
290, n. 3 (emphasis in original), this time citing Jackson. Montejo
infers from the “even requests” that having counsel is more conclusive of
the invalidity of uncounseled waiver than the mere requesting of
counsel. But the Patterson footnote did not suggest that the analysis
“changes” in both these scenarios (having a lawyer, versus requesting
one) with specific reference to the validity of waivers under the Sixth
Amendment. The citation of Moulton (a nonwaiver case) for the first
scenario suggests just the opposite.
                 Cite as: 556 U. S. ____ (2009)          13

                     Opinion of the Court

would be completely unjustified to presume that a defen
dant’s consent to police-initiated interrogation was invol
untary or coerced simply because he had previously been
appointed a lawyer.
                             IV
   So on the one hand, requiring an initial “invocation” of
the right to counsel in order to trigger the Jackson pre
sumption is consistent with the theory of that decision, but
(as Montejo and his amici argue, see Part II, supra) would
be unworkable in more than half the States of the Union.
On the other hand, eliminating the invocation require
ment would render the rule easy to apply but depart fun
damentally from the Jackson rationale.
   We do not think that stare decisis requires us to expand
significantly the holding of a prior decision—
fundamentally revising its theoretical basis in the proc
ess—in order to cure its practical deficiencies. To the
contrary, the fact that a decision has proved “unworkable”
is a traditional ground for overruling it. Payne v. Tennes
see, 501 U. S. 808, 827 (1991). Accordingly, we called for
supplemental briefing addressed to the question whether
Michigan v. Jackson should be overruled.
   Beyond workability, the relevant factors in deciding
whether to adhere to the principle of stare decisis include
the antiquity of the precedent, the reliance interests at
stake, and of course whether the decision was well rea
soned. Pearson v. Callahan, 555 U. S. ___, ___ (2009) (slip
op., at 8). The first two cut in favor of abandoning Jack
son: the opinion is only two decades old, and eliminating it
would not upset expectations. Any criminal defendant
learned enough to order his affairs based on the rule
announced in Jackson would also be perfectly capable of
interacting with the police on his own. Of course it is
likely true that police and prosecutors have been trained
to comply with Jackson, see generally Supplemental Brief
14                     MONTEJO v. LOUISIANA

                           Opinion of the Court

for Larry D. Thompson et al. as Amici Curiae, but that is
hardly a basis for retaining it as a constitutional require
ment. If a State wishes to abstain from requesting inter
views with represented defendants when counsel is not
present, it obviously may continue to do so.4
  Which brings us to the strength of Jackson’s reasoning.
When this Court creates a prophylactic rule in order to
protect a constitutional right, the relevant “reasoning” is
the weighing of the rule’s benefits against its costs. “The
value of any prophylactic rule . . . must be assessed not
only on the basis of what is gained, but also on the basis of
what is lost.” Minnick, 498 U. S., at 161 (SCALIA, J., dis
senting). We think that the marginal benefits of Jackson
(viz., the number of confessions obtained coercively that
are suppressed by its bright-line rule and would otherwise
have been admitted) are dwarfed by its substantial costs
(viz., hindering “society’s compelling interest in finding,
convicting, and punishing those who violate the law,”
Moran, supra, at 426).
  What does the Jackson rule actually achieve by way of
preventing unconstitutional conduct? Recall that the
purpose of the rule is to preclude the State from badgering
defendants into waiving their previously asserted rights.
See Harvey, supra, at 350; see also McNeil, 501 U. S., at
177. The effect of this badgering might be to coerce a
waiver, which would render the subsequent interrogation
a violation of the Sixth Amendment. See Massiah, supra,
at 204. Even though involuntary waivers are invalid even
——————
  4 The dissent posits a different reliance interest: “the public’s interest
in knowing that counsel, once secured, may be reasonably relied upon
as a medium between the accused and the power of the State,” post, at
9. We suspect the public would be surprised to learn that a criminal
can freely sign away his right to a lawyer, confess his crimes, and then
ask the courts to assume that the confession was coerced—on the
ground that he had, at some earlier point in time, made a pro forma
statement requesting that counsel be appointed on his behalf.
                 Cite as: 556 U. S. ____ (2009)           15

                     Opinion of the Court

apart from Jackson, see Patterson, 487 U. S., at 292, n. 4,
mistakes are of course possible when courts conduct case
by-case voluntariness review. A bright-line rule like that
adopted in Jackson ensures that no fruits of interrogations
made possible by badgering-induced involuntary waivers
are ever erroneously admitted at trial.
   But without Jackson, how many would be? The answer
is few if any. The principal reason is that the Court has
already taken substantial other, overlapping measures
toward the same end. Under Miranda’s prophylactic
protection of the right against compelled self
incrimination, any suspect subject to custodial interroga
tion has the right to have a lawyer present if he so re
quests, and to be advised of that right. 384 U. S., at 474.
Under Edwards’ prophylactic protection of the Miranda
right, once such a defendant “has invoked his right to have
counsel present,” interrogation must stop. 451 U. S., at
484. And under Minnick’s prophylactic protection of the
Edwards right, no subsequent interrogation may take
place until counsel is present, “whether or not the accused
has consulted with his attorney.” 498 U. S., at 153.
   These three layers of prophylaxis are sufficient. Under
the Miranda-Edwards-Minnick line of cases (which is not
in doubt), a defendant who does not want to speak to the
police without counsel present need only say as much
when he is first approached and given the Miranda warn
ings. At that point, not only must the immediate contact
end, but “badgering” by later requests is prohibited. If
that regime suffices to protect the integrity of “a suspect’s
voluntary choice not to speak outside his lawyer’s pres
ence” before his arraignment, Cobb, 532 U. S., at 175
(KENNEDY, J., concurring), it is hard to see why it would
not also suffice to protect that same choice after arraign
ment, when Sixth Amendment rights have attached. And
if so, then Jackson is simply superfluous.
   It is true, as Montejo points out in his supplemental
16                MONTEJO v. LOUISIANA

                     Opinion of the Court

brief, that the doctrine established by Miranda and Ed
wards is designed to protect Fifth Amendment, not Sixth
Amendment, rights. But that is irrelevant. What matters
is that these cases, like Jackson, protect the right to have
counsel during custodial interrogation—which right hap
pens to be guaranteed (once the adversary judicial process
has begun) by two sources of law. Since the right under
both sources is waived using the same procedure, Patter
son, supra, at 296, doctrines ensuring voluntariness of the
Fifth Amendment waiver simultaneously ensure the
voluntariness of the Sixth Amendment waiver.
   Montejo also correctly observes that the Miranda-
Edwards regime is narrower than Jackson in one respect:
The former applies only in the context of custodial interro
gation. If the defendant is not in custody then those deci
sions do not apply; nor do they govern other, noninterroga
tive types of interactions between the defendant and the
State (like pretrial lineups). However, those uncovered
situations are the least likely to pose a risk of coerced
waivers. When a defendant is not in custody, he is in
control, and need only shut his door or walk away to avoid
police badgering. And noninterrogative interactions with
the State do not involve the “inherently compelling pres
sures,” Miranda, supra, at 467, that one might reasonably
fear could lead to involuntary waivers.
   Jackson was policy driven, and if that policy is being
adequately served through other means, there is no reason
to retain its rule. Miranda and the cases that elaborate
upon it already guarantee not simply noncoercion in the
traditional sense, but what Justice Harlan referred to as
“voluntariness with a vengeance,” 384 U. S., at 505 (dis
senting opinion). There is no need to take Jackson’s fur
ther step of requiring voluntariness on stilts.
   On the other side of the equation are the costs of adding
the bright-line Jackson rule on top of Edwards and other
extant protections. The principal cost of applying any
                     Cite as: 556 U. S. ____ (2009)                   17

                          Opinion of the Court

exclusionary rule “is, of course, letting guilty and possibly
dangerous criminals go free . . . .” Herring v. United
States, 555 U. S. ___, ___ (2009) (slip op., at 6). Jackson
not only “operates to invalidate a confession given by the
free choice of suspects who have received proper advice of
their Miranda rights but waived them nonetheless,” Cobb,
supra, at 174–175 (KENNEDY, J., concurring), but also
deters law enforcement officers from even trying to obtain
voluntary confessions. The “ready ability to obtain unco
erced confessions is not an evil but an unmitigated good.”
McNeil, 501 U. S., at 181. Without these confessions,
crimes go unsolved and criminals unpunished. These are
not negligible costs, and in our view the Jackson Court
gave them too short shrift.5
   Notwithstanding this calculus, Montejo and his amici
urge the retention of Jackson. Their principal objection to
its elimination is that the Edwards regime which remains
will not provide an administrable rule. But this Court has
praised Edwards precisely because it provides “ ‘clear and
unequivocal’ guidelines to the law enforcement profes
sion,” Arizona v. Roberson, 486 U. S. 675, 682 (1988). Our
cases make clear which sorts of statements trigger its
protections, see Davis v. United States, 512 U. S. 452, 459
(1994), and once triggered, the rule operates as a bright
line. Montejo expresses concern that courts will have to
determine whether statements made at preliminary hear
ings constitute Edwards invocations—thus implicating all
the practical problems of the Louisiana rule we discussed
above, see Part II, supra. That concern is misguided. “We
——————
  5 The dissent claims that, in fact, few confessions have been sup

pressed by federal courts applying Jackson. Post, at 8. If so, that is
because, as the dissent boasts, “generations of police officers have been
trained to refrain from approaching represented defendants,” post, at 9,
n. 4. Anyway, if the rule truly does not hinder law enforcement or
make much practical difference, see post, at 7–9, and nn. 3–4, then
there is no reason to be particularly exercised about its demise.
18                 MONTEJO v. LOUISIANA

                      Opinion of the Court

have in fact never held that a person can invoke his
Miranda rights anticipatorily, in a context other than
‘custodial interrogation’. . . .” McNeil, supra, at 182, n. 3.
What matters for Miranda and Edwards is what happens
when the defendant is approached for interrogation, and
(if he consents) what happens during the interrogation—
not what happened at any preliminary hearing.
   In sum, when the marginal benefits of the Jackson rule
are weighed against its substantial costs to the truth
seeking process and the criminal justice system, we read
ily conclude that the rule does not “pay its way,” United
States v. Leon, 468 U. S. 897, 907–908, n. 6 (1984). Michi
gan v. Jackson should be and now is overruled.
                            V
   Although our holding means that the Louisiana Su
preme Court correctly rejected Montejo’s claim under
Jackson, we think that Montejo should be given an oppor
tunity to contend that his letter of apology should still
have been suppressed under the rule of Edwards. If Mon
tejo made a clear assertion of the right to counsel when
the officers approached him about accompanying them on
the excursion for the murder weapon, then no interroga
tion should have taken place unless Montejo initiated it.
Davis, supra, at 459. Even if Montejo subsequently agreed
to waive his rights, that waiver would have been invalid
had it followed an “unequivocal election of the right,”
Cobb, 532 U. S., at 176 (KENNEDY, J., concurring).
   Montejo understandably did not pursue an Edwards
objection, because Jackson served as the Sixth Amend
ment analogy to Edwards and offered broader protections.
Our decision today, overruling Jackson, changes the legal
landscape and does so in part based on the protections
already provided by Edwards. Thus we think that a re
mand is appropriate so that Montejo can pursue this
alternative avenue for relief. Montejo may also seek on
                 Cite as: 556 U. S. ____ (2009)          19

                     Opinion of the Court

remand to press any claim he might have that his Sixth
Amendment waiver was not knowing and voluntary, e.g.,
his argument that the waiver was invalid because it was
based on misrepresentations by police as to whether he
had been appointed a lawyer, cf. Moran, 475 U. S., at 428–
429. These matters have heightened importance in light
of our opinion today.
   We do not venture to resolve these issues ourselves, not
only because we are a court of final review, “not of first
view,” Cutter v. Wilkinson, 544 U. S. 709, 718, n. 7 (2005),
but also because the relevant facts remain unclear. Mon
tejo and the police gave inconsistent testimony about
exactly what took place on the afternoon of September 10,
2002, and the Louisiana Supreme Court did not make an
explicit credibility determination. Moreover, Montejo’s
testimony came not at the suppression hearing, but rather
only at trial, and we are unsure whether under state law
that testimony came too late to affect the propriety of the
admission of the evidence. These matters are best left for
resolution on remand.
   We do reject, however, the dissent’s revisionist legal
analysis of the “knowing and voluntary” issue. Post, at
10–14. In determining whether a Sixth Amendment
waiver was knowing and voluntary, there is no reason
categorically to distinguish an unrepresented defendant
from a represented one. It is equally true for each that, as
we held in Patterson, the Miranda warnings adequately
inform him “of his right to have counsel present during the
questioning,” and make him “aware of the consequences of
a decision by him to waive his Sixth Amendment rights,”
487 U. S., at 293. Somewhat surprisingly for an opinion
that extols the virtues of stare decisis, the dissent com
plains that our “treatment of the waiver question rests
entirely on the dubious decision in Patterson,” post, at 12.
The Court in Patterson did not consider the result dubious,
nor does the Court today.
20                MONTEJO v. LOUISIANA

                     Opinion of the Court

                        *     *     *
   This case is an exemplar of Justice Jackson’s oft quoted
warning that this Court “is forever adding new stories to
the temples of constitutional law, and the temples have a
way of collapsing when one story too many is added.”
Douglas v. City of Jeannette, 319 U. S. 157, 181 (1943)
(opinion concurring in result). We today remove Michigan
v. Jackson’s fourth story of prophylaxis.
   The judgment of the Louisiana Supreme Court is va
cated, and the case is remanded for further proceedings
not inconsistent with this opinion.
                                           It is so ordered.
                  Cite as: 556 U. S. ____ (2009)             1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE ALITO, with whom JUSTICE KENNEDY joins,
concurring.
   Earlier this Term, in Arizona v. Gant, 556 U. S. ___
(2009), the Court overruled New York v. Belton, 453 U. S.
454 (1981), even though that case had been on the books
for 28 years, had not been undermined by subsequent
decisions, had been recently reaffirmed and extended, had
proven to be eminently workable (indeed, had been
adopted for precisely that reason), and had engendered
substantial law enforcement reliance. See Gant, supra, at
___ (slip op., at 4) (ALITO, J., dissenting). The Court took
this step even though we were not asked to overrule Bel
ton and this new rule is almost certain to lead to a host of
problems. See Gant, supra, at ___ (slip op., at 10) (ALITO,
J., dissenting); Megginson v. United States, post, p. ___;
Grooms v. United States, post, p. ___.
   JUSTICE SCALIA, who cast the deciding vote to overrule
Belton, dismissed stare decisis concerns with the following
observation: “[I]t seems to me ample reason that the
precedent was badly reasoned and produces erroneous . . .
results.” Gant, supra, at ___ (slip op., at 3) (concurring
opinion). This narrow view of stare decisis provides
the only principle on which the decision in Gant can be
justified.
   In light of Gant, the discussion of stare decisis in today’s
2                    MONTEJO v. LOUISIANA

                        ALITO, J., concurring

dissent* is surprising. The dissent in the case at hand
criticizes the Court for “[a]cting on its own” in reconsider
ing Michigan v. Jackson, 475 U. S. 625 (1986). Post, at 4
(opinion of STEVENS, J.). But the same was true in Gant,
and in this case, the Court gave the parties and interested
amici the opportunity to submit supplemental briefs on
the issue, a step not taken in Gant.
  The dissent faults the Court for “cast[ing] aside the
reliance interests of law enforcement,” post, at 8–9, but in
Gant, there were real and important law enforcement
interests at stake. See 556 U. S., at ___ (slip op., at 5–6)
(ALITO, J., dissenting). Even the Court conceded that the
Belton rule had “been widely taught in police academies
and that law enforcement officers ha[d] relied on the rule
in conducting vehicle searches during the past 28 years.”
556 U. S., at ___ (slip op., at 16). And whatever else might
be said about Belton, it surely provided a bright-line rule.
  A month ago, none of this counted for much, but today
the dissent writes:
    “Jackson’s bright-line rule has provided law enforce
    ment officers with clear guidance, allowed prosecutors
    to quickly and easily assess whether confessions will
    be admissible in court, and assisted judges in deter
    mining whether a defendant’s Sixth Amendment
    rights have been violated by police interrogation.”
    Post, at 8.
 It is striking that precisely the same points were true in
Gant:
    “[Belton’s] bright-line rule ha[d] provided law en
    forcement officers with clear guidance, allowed prose

——————
  * One of the dissenters in the present case, JUSTICE BREYER, also
dissented in Gant and would have followed Belton on stare decisis
grounds. See 556 U. S., at ___ (slip op., at 1). Thus, he would not
overrule either Belton or Michigan v. Jackson, 475 U. S. 625 (1986).
                 Cite as: 556 U. S. ____ (2009)            3

                     ALITO, J., concurring

    cutors to quickly and easily assess whether [evidence
    obtained in a vehicle search] w[ould] be admissible in
    court, and assisted judges in determining whether a
    defendant’s [Fourth] Amendment rights ha[d] been
    violated by police interrogation.” Post, at 8.
  The dissent, finally, invokes Jackson’s antiquity, stating
that “the 23-year existence of a simple bright-line rule”
should weigh in favor of its retention. Post, at 9. But in
Gant, the Court had no compunction about casting aside a
28-year-old bright-line rule. I can only assume that the
dissent thinks that our constitutional precedents are like
certain wines, which are most treasured when they are
neither too young nor too old, and that Jackson, at 23, is
in its prime, whereas Belton, at 28, had turned brownish
and vinegary.
  I agree with the dissent that stare decisis should pro
mote “ ‘the evenhanded . . . development of legal princi
ples,’ ” post, at 6 (quoting Payne v. Tennessee, 501 U. S.
808, 827–828 (1991)). The treatment of stare decisis in
Gant fully supports the decision in the present case.
                  Cite as: 556 U. S. ____ (2009)            1

                     STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE STEVENS, with whom JUSTICE SOUTER and
JUSTICE GINSBURG join, and with whom JUSTICE BREYER
joins, except for footnote 5, dissenting.
   Today the Court properly concludes that the Louisiana
Supreme Court’s parsimonious reading of our decision in
Michigan v. Jackson, 475 U. S. 625 (1986), is indefensible.
Yet the Court does not reverse. Rather, on its own initia
tive and without any evidence that the longstanding Sixth
Amendment protections established in Jackson have
caused any harm to the workings of the criminal justice
system, the Court rejects Jackson outright on the ground
that it is “untenable as a theoretical and doctrinal mat
ter.” Ante, at 6. That conclusion rests on a misinterpreta
tion of Jackson’s rationale and a gross undervaluation of
the rule of stare decisis. The police interrogation in this
case clearly violated petitioner’s Sixth Amendment right
to counsel.
                               I
  The Sixth Amendment provides that “[i]n all criminal
prosecutions, the accused shall enjoy the right . . . to have
the Assistance of Counsel for his defence.” The right to
counsel attaches during “the initiation of adversary judi
cial criminal proceedings,” Rothgery v. Gillespie County,
554 U. S. ___, ___ (2008) (slip op., at 5) (internal quotation
2                  MONTEJO v. LOUISIANA

                     STEVENS, J., dissenting

marks omitted), and it guarantees the assistance of coun
sel not only during in-court proceedings but during all
critical stages, including postarraignment interviews with
law enforcement officers, see Patterson v. Illinois, 487
U. S. 285, 290 (1988).
   In Jackson, this Court considered whether the Sixth
Amendment bars police from interrogating defendants
who have requested the appointment of counsel at ar
raignment. Applying the presumption that such a request
constitutes an invocation of the right to counsel “at every
critical stage of the prosecution,” 475 U. S., at 633, we held
that “a defendant who has been formally charged with a
crime and who has requested appointment of counsel at
his arraignment” cannot be subject to uncounseled inter
rogation unless he initiates “exchanges or conversations
with the police,” id., at 626.
   In this case, petitioner Jesse Montejo contends that
police violated his Sixth Amendment right to counsel by
interrogating him following his “72-hour hearing” outside
the presence of, and without prior notice to, his lawyer.
The Louisiana Supreme Court rejected Montejo’s claim.
Relying on the fact that the defendants in Jackson had
“requested” counsel at arraignment, the state court held
that Jackson’s protections did not apply to Montejo be
cause his counsel was appointed automatically; Montejo
had not explicitly requested counsel or affirmatively ac
cepted the counsel appointed to represent him before he
submitted to police interrogation. 06–1807, pp. 28–29
(1/16/08), 974 So. 2d 1238, 1261.
   I agree with the majority’s conclusion that the Louisiana
Supreme Court’s decision, if allowed to stand, “would lead
either to an unworkable standard, or to arbitrary and
anomalous distinctions between defendants in different
States,” ante, at 3. Neither option is tolerable, and neither
is compelled by Jackson itself.
   Our decision in Jackson involved two consolidated cases,
                  Cite as: 556 U. S. ____ (2009)            3

                     STEVENS, J., dissenting

both arising in the State of Michigan. Under Michigan
law in effect at that time, when a defendant appeared for
arraignment the court was required to inform him that
counsel would be provided if he was financially needy and
he requested representation. Mich. Gen. Ct. Rule 785.4(1)
(1976). It was undisputed that the Jackson defendants
made such a “request” at their arraignment: one by com
pleting an affidavit of indigency, and the other by respond
ing affirmatively to a question posed to him by the court.
See App. in Michigan v. Jackson, O. T. 1984, No. 84–1531,
p. 168; App. in Michigan v. Bladel, O. T. 1984, No. 84–
1539, pp. 3a–4a. In neither case, however, was it clear
that counsel had actually been appointed at the arraign
ment. Thus, the defendants’ requests for counsel were
significant as a matter of state law because they served as
evidence that the appointment of counsel had been effec
tuated even in the absence of proof that defense counsel
had actual notice of the appointments.
   Unlike Michigan, Louisiana does not require a defen
dant to make a request in order to receive court-appointed
counsel. Consequently, there is no reason to place consti
tutional significance on the fact that Montejo neither
voiced a request for counsel nor affirmatively embraced
that appointment post hoc. Certainly our decision in
Jackson did not mandate such an odd rule. See ante, at 4
(acknowledging that we had no occasion to decide in Jack
son how its rule would apply in States that do not make
appointment of counsel contingent on affirmative request).
If a defendant is entitled to protection from police-initiated
interrogation under the Sixth Amendment when he
merely requests a lawyer, he is even more obviously enti
tled to such protection when he has secured a lawyer.
Indeed, we have already recognized as much. See Michi
gan v. Harvey, 494 U. S. 344, 352 (1990) (acknowledging
that “once a defendant obtains or even requests counsel,”
Jackson alters the waiver analysis); Patterson, 487 U. S.,
4                      MONTEJO v. LOUISIANA

                         STEVENS, J., dissenting

at 290, n. 3 (noting “as a matter of some significance” to
the constitutional analysis that defendant had “not re
tained, or accepted by appointment, a lawyer to represent
him at the time he was questioned by authorities” (em
phasis added)).1 Once an attorney-client relationship has
been established through the appointment or retention of
counsel, as a matter of federal law the method by which
the relationship was created is irrelevant: The existence of
a valid attorney-client relationship provides a defendant
with the full constitutional protection afforded by the
Sixth Amendment.
                             II
  Today the Court correctly concludes that the Louisiana
Supreme Court’s holding is “troublesome,” ante, at 4,
“impractical,” ante, at 5, and “unsound,” ante, at 6. In
stead of reversing the decision of the state court by simply
answering the question on which we granted certiorari in
a unanimous opinion, however, the majority has decided to
change the law. Acting on its own initiative, the majority
overrules Jackson to correct a “theoretical and doctrinal”
problem of its own imagining, see ante, at 6. A more
careful reading of Jackson and the Sixth Amendment
cases upon which it relied reveals that the rule announced
in Jackson protects a fundamental right that the Court
now dishonors.
  The majority’s decision to overrule Jackson rests on its
assumption that Jackson’s protective rule was intended to
“prevent police from badgering defendants into changing
their minds about their rights,” ante, at 10; see also ante,
——————
  1 In Patterson v. Illinois, we further explained, “[o]nce an accused has

a lawyer,” “a distinct set of constitutional safeguards aimed at preserv
ing the sanctity of the attorney-client relationship takes effect.” 487
U. S., at 290, n. 3 (citing Maine v. Moulton, 474 U. S. 159, 176 (1985)).
“Indeed,” we emphasized, “the analysis changes markedly once an
accused even requests the assistance of counsel.” 487 U. S., at 290, n. 3.
                 Cite as: 556 U. S. ____ (2009)            5

                    STEVENS, J., dissenting

at 13, just as the rule adopted in Edwards v. Arizona, 451
U. S. 477 (1981), was designed to prevent police from
coercing unindicted suspects into revoking their requests
for counsel at interrogation. Operating on that limited
understanding of the purpose behind Jackson’s protective
rule, the Court concludes that Jackson provides no safe
guard not already secured by this Court’s Fifth Amend
ment jurisprudence. See Miranda v. Arizona, 384 U. S.
436 (1966) (requiring defendants to be admonished of their
right to counsel prior to custodial interrogation); Edwards,
451 U. S. 477 (prohibiting police-initiated interrogation
following defendant’s invocation of the right to counsel).
   The majority’s analysis flagrantly misrepresents Jack
son’s underlying rationale and the constitutional interests
the decision sought to protect. While it is true that the
rule adopted in Jackson was patterned after the rule in
Edwards, 451 U. S., at 484–485, the Jackson opinion does
not even mention the anti-badgering considerations that
provide the basis for the Court’s decision today. Instead,
Jackson relied primarily on cases discussing the broad
protections guaranteed by the Sixth Amendment right to
counsel—not its Fifth Amendment counterpart. Jackson
emphasized that the purpose of the Sixth Amendment is
to “ ‘protec[t] the unaided layman at critical confrontations
with his adversary,’ ” 475 U. S., at 631 (quoting United
States v. Gouveia, 467 U. S. 180, 189 (1984)), by giving
him “ ‘the right to rely on counsel as a ‘medium’ between
him[self] and the State,’ ” 475 U. S., at 632 (quoting Maine
v. Moulton, 474 U. S. 159, 176 (1985)). Underscoring that
the commencement of criminal proceedings is a decisive
event that transforms a suspect into an accused within the
meaning of the Sixth Amendment, we concluded that
arraigned defendants are entitled to “at least as much
protection” during interrogation as the Fifth Amendment
affords unindicted suspects. See, e.g., 475 U. S., at 632
(“[T]he difference between the legal basis for the rule
6                      MONTEJO v. LOUISIANA

                         STEVENS, J., dissenting

applied in Edwards and the Sixth Amendment claim
asserted in these cases actually provides additional sup
port for the application of the rule in these circumstances”
(emphasis added)). Thus, although the rules adopted in
Edwards and Jackson are similar, Jackson did not rely on
the reasoning of Edwards but remained firmly rooted in
the unique protections afforded to the attorney-client
relationship by the Sixth Amendment.2
  Once Jackson is placed in its proper Sixth Amendment
context, the majority’s justifications for overruling the
decision crumble. Ordinarily, this Court is hesitant to
disturb past precedent and will do so only when a rule has
proven “outdated, ill-founded, unworkable, or otherwise
legitimately vulnerable to serious reconsideration.”
Vasquez v. Hillery, 474 U. S. 254, 266 (1986). While stare
decisis is not “an inexorable command,” we adhere to it as
“the preferred course because it promotes the evenhanded,
predictable, and consistent development of legal princi
ples, fosters reliance on judicial decisions, and contributes
to the actual and perceived integrity of the judicial proc
——————
    2 Themajority insists that protection from police badgering is the
only purpose the Jackson rule can plausibly serve. After all, it asks,
from what other evil would the rule guard? See ante, at 9. There are
two obvious answers. First, most narrowly, it protects the defendant
from any police-initiated interrogation without notice to his counsel, not
just from “badgering” which is not necessarily a part of police question
ing. Second, and of prime importance, it assures that any waiver of
counsel will be valid. The assistance offered by counsel protects a
defendant from surrendering his rights with an insufficient apprecia
tion of what those rights are and how the decision to respond to inter
rogation might advance or compromise his exercise of those rights
throughout the course of criminal proceedings. A lawyer can provide
her client with advice regarding the legal and practical options avail
able to him; the potential consequences, both good and bad, of choosing
to discuss his case with police; the likely effect of such a conversation on
the resolution of the charges against him; and an informed assessment
of the best course of action under the circumstances. Such assistance
goes far beyond mere protection against police badgering.
                     Cite as: 556 U. S. ____ (2009)                    7

                        STEVENS, J., dissenting

ess.” Payne v. Tennessee, 501 U. S. 808, 827–828 (1991).
   Paying lip service to the rule of stare decisis, the major
ity acknowledges that the Court must consider many
factors before taking the dramatic step of overruling a
past decision. See ante, at 12. Specifically, the majority
focuses on four considerations: the reasoning of the deci
sion, the workability of the rule, the reliance interests at
stake, and the antiquity of the precedent. The Court
exaggerates the considerations favoring reversal, however,
and gives short shrift to the valid considerations favoring
retention of the Jackson rule.
   First, and most central to the Court’s decision to over
rule Jackson, is its assertion that Jackson’s “ ‘reason
ing’ ”—which the Court defines as “the weighing of the
[protective] rule’s benefits against its costs,” ante, at 14—
does not justify continued application of the rule it cre
ated. The balancing test the Court performs, however,
depends entirely on its misunderstanding of Jackson as a
rule designed to prevent police badgering, rather than a
rule designed to safeguard a defendant’s right to rely on
the assistance of counsel.3
   Next, in order to reach the conclusion that the Jackson

——————
   3 Even accepting the majority’s improper framing of Jackson’s foun

dation, the Court fails to show that the costs of the rule are more than
negligible or differ from any other protection afforded by the right to
counsel. The majority assumes, without citing any empirical or even
anecdotal support, that any marginal benefits of the Jackson rule are
“dwarfed by its substantial costs,” which it describes as harm to “ ‘soci
ety’s compelling interest in finding, convicting, and punishing those
who violate the law.’ ” Ante, at 14 (quoting Moran v. Burbine, 475 U. S.
412, 426 (1986)). That assumption is highly dubious, particularly in
light of the fact that several amici with interest in law enforcement
have conceded that the application of Jackson’s protective rule rarely
impedes prosecution. See Supplemental Brief for Larry D. Thompson
et al. as Amici Curiae 6 (hereinafter Thompson Supplemental Brief);
Brief for United States as Amicus Curiae 12 (hereinafter United States
Brief).
8                    MONTEJO v. LOUISIANA

                       STEVENS, J., dissenting

rule is unworkable, the Court reframes the relevant in
quiry, asking not whether the Jackson rule as applied for
the past quarter century has proved easily administrable,
but instead whether the Louisiana Supreme Court’s
cramped interpretation of that rule is practically worka
ble. The answer to that question, of course, is no. When
framed more broadly, however, the evidence is overwhelm
ing that Jackson’s simple, bright-line rule has done more
to advance effective law enforcement than to undermine it.
  In a supplemental brief submitted by lawyers and
judges with extensive experience in law enforcement and
prosecution, amici Larry D. Thompson et al. argue per
suasively that Jackson’s bright-line rule has provided law
enforcement officers with clear guidance, allowed prosecu
tors to quickly and easily assess whether confessions will
be admissible in court, and assisted judges in determining
whether a defendant’s Sixth Amendment rights have been
violated by police interrogation. See generally Thompson
Supplemental Brief 6. While amici acknowledge that
“Jackson reduces opportunities to interrogate defendants”
and “may require exclusion of evidence that could support
a criminal conviction,” they maintain that “it is a rare case
where this rule lets a guilty defendant go free.” Ibid.
Notably, these representations are not contradicted by the
State of Louisiana or other amici, including the United
States. See United States Brief 12 (conceding that the
Jackson rule has not “resulted in the suppression of sig
nificant numbers of statements in federal prosecutions in
the past”).4 In short, there is substantial evidence sug
——————
  4 Further supporting the workability of the Jackson rule is the fact

that it aligns with the professional standards and norms that already
govern the behavior of police and prosecutors. Rules of Professional
Conduct endorsed by the American Bar Association (ABA) and by every
State Bar Association in the country prohibit prosecutors from making
direct contact with represented defendants in all but the most limited
of circumstances, see App. to Supplemental Brief for Public Defender
                     Cite as: 556 U. S. ____ (2009)                   9

                        STEVENS, J., dissenting

gesting that Jackson’s rule is not only workable, but also
desirable from the perspective of law enforcement.
   Turning to the reliance interests at stake in the case,
the Court rejects the interests of criminal defendants with
the flippant observation that any who are knowledgeable
enough to rely on Jackson are too savvy to need its protec
tions, and casts aside the reliance interests of law en
forcement on the ground that police and prosecutors re
main free to employ the Jackson rule if it suits them. See
ante, at 12. Again as a result of its mistaken understand
ing of the purpose behind Jackson’s protective rule, the
Court fails to identify the real reliance interest at issue in
this case: the public’s interest in knowing that counsel,
once secured, may be reasonably relied upon as a medium
between the accused and the power of the State. That
interest lies at the heart of the Sixth Amendment’s guar
antee, and is surely worthy of greater consideration than
it is given by today’s decision.
   Finally, although the Court acknowledges that “antiq
uity” is a factor that counsels in favor of retaining prece
dent, it concludes that the fact Jackson is “only two dec
ades old” cuts “in favor of abandoning” the rule it
established. Ante, at 13. I would have thought that the
——————
Service for the District of Columbia et al. as Amici Curiae 1a–15a
(setting forth state rules governing contact with represented persons);
ABA Model Rule of Professional Conduct 4.2 (2008); 28 U. S. C.
§530B(a) (making state rules of professional conduct applicable to
federal attorneys), and generations of police officers have been trained
to refrain from approaching represented defendants, both because
Jackson requires it and because, absent direction from prosecutors,
officers are reticent to interrogate represented defendants. See United
States Brief 11–12; see also Thompson Supplemental Brief 13 (citing
Federal Bureau of Investigation, Legal Handbook for Special Agents
§7–4.1(7) (2003)). Indeed, the United States concedes that a decision to
overrule the case “likely w[ill] not significantly alter the manner in
which federal law enforcement agents investigate indicted defendants.”
United States Brief 11–12.
10                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

23-year existence of a simple bright-line rule would be a
factor that cuts in the other direction.
  Despite the fact that the rule established in Jackson
remains relevant, well grounded in constitutional prece
dent, and easily administrable, the Court today rejects it
sua sponte. Such a decision can only diminish the public’s
confidence in the reliability and fairness of our system of
justice.5
                            III
   Even if Jackson had never been decided, it would be
clear that Montejo’s Sixth Amendment rights were vio
lated. Today’s decision eliminates the rule that “any
waiver of Sixth Amendment rights given in a discussion
initiated by police is presumed invalid” once a defendant
has invoked his right to counsel. Harvey, 494 U. S., at 349
(citing Jackson, 475 U. S., at 636). Nevertheless, under
the undisputed facts of this case, there is no sound basis
for concluding that Montejo made a knowing and valid
waiver of his Sixth Amendment right to counsel before
acquiescing in police interrogation following his 72-hour
hearing.    Because police questioned Montejo without
notice to, and outside the presence of, his lawyer, the
——————
  5 In his concurrence, JUSTICE ALITO assumes that my consideration of

the rule of stare decisis in this case is at odds with the Court’s recent
rejection of his reliance on that doctrine in his dissent in Arizona v.
Gant, 556 U. S. ___ (2009). While I agree that the reasoning in his
dissent supports my position in this case, I do not agree with his
characterization of our opinion in Gant. Contrary to his representation,
the Court did not overrule our precedent in New York v. Belton, 453
U. S. 454 (1981). Rather, we affirmed the narrow interpretation of
Belton’s holding adopted by the Arizona Supreme Court, rejecting the
broader interpretation adopted by other lower courts that had been
roundly criticized by judges and scholars alike. By contrast, in this
case the Court flatly overrules Jackson—a rule that has drawn virtu
ally no criticism—on its own initiative. The two cases are hardly
comparable. If they were, and if JUSTICE ALITO meant what he said in
Gant, I would expect him to join this opinion.
                 Cite as: 556 U. S. ____ (2009)          11

                    STEVENS, J., dissenting

interrogation violated Montejo’s right to counsel even
under pre-Jackson precedent.
   Our pre-Jackson case law makes clear that “the Sixth
Amendment is violated when the State obtains incriminat
ing statements by knowingly circumventing the accused’s
right to have counsel present in a confrontation between
the accused and a state agent.” Moulton, 474 U. S., at
176. The Sixth Amendment entitles indicted defendants
to have counsel notified of and present during critical
confrontations with the state throughout the pretrial
process. Given the realities of modern criminal prosecu
tion, the critical proceedings at which counsel’s assistance
is required more and more often occur outside the court
room in pretrial proceedings “where the results might well
settle the accused’s fate and reduce the trial itself to a
mere formality.” United States v. Wade, 388 U. S. 218,
224 (1967).
   In Wade, for instance, we held that because a post
indictment lineup conducted for identification purposes is
a critical stage of the criminal proceedings, a defendant
and his counsel are constitutionally entitled to notice of
the impending lineup. Accordingly, counsel’s presence is a
“requisite to conduct of the lineup, absent an intelligent
waiver.” Id., at 237 (internal quotation marks omitted).
The same reasoning applies to police decisions to interro
gate represented defendants. For if the Sixth Amendment
entitles an accused to such robust protection during a
lineup, surely it entitles him to such protection during a
custodial interrogation, when the stakes are as high or
higher. Cf. Spano v. New York, 360 U. S. 315, 326 (1959)
(Douglas, J., concurring) (“[W]hat use is a defendant’s
right to effective counsel at every stage of a criminal case
if, while he is held awaiting trial, he can be questioned in
the absence of counsel until he confesses?”).
   The Court avoids confronting the serious Sixth Amend
ment concerns raised by the police interrogation in this
12                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

case by assuming that Montejo validly waived his Sixth
Amendment rights before submitting to interrogation.6 It
does so by summarily concluding that “doctrines ensuring
voluntariness of the Fifth Amendment waiver simultane
ously ensure the voluntariness of the Sixth Amendment
waiver,” ante, at 15–16; thus, because Montejo was given
Miranda warnings prior to interrogation, his waiver was
presumptively valid. Ironically, while the Court faults
Jackson for blurring the line between this Court’s Fifth
and Sixth Amendment jurisprudence, it commits the same
error by assuming that the Miranda warnings given in
this case, designed purely to safeguard the Fifth Amend
ment right against self-incrimination, were somehow
adequate to protect Montejo’s more robust Sixth Amend
ment right to counsel.
    The majority’s cursory treatment of the waiver question
rests entirely on the dubious decision in Patterson, in
which we addressed whether, by providing Miranda warn
ings, police had adequately advised an indicted but unrep
resented defendant of his Sixth Amendment right to coun
sel. The majority held that “[a]s a general matter . . . an
accused who is admonished with the warnings prescribed
. . . in Miranda, . . . has been sufficiently apprised of the
nature of his Sixth Amendment rights, and of the conse
quences of abandoning those rights.” 487 U. S., at 296.
The Court recognized, however, that “because the Sixth
Amendment’s protection of the attorney-client relationship

——————
  6 The majority leaves open the possibility that, on remand, Montejo

may argue that his waiver was invalid because police falsely told him
he had not been appointed counsel. See ante, at 18. While such police
deception would obviously invalidate any otherwise valid waiver of
Montejo’s Sixth Amendment rights, Montejo has a strong argument
that, given his status as a represented criminal defendant, the Miranda
warnings given to him by police were insufficient to permit him to
make a knowing waiver of his Sixth Amendment rights even absent
police deception.
                     Cite as: 556 U. S. ____ (2009)                  13

                        STEVENS, J., dissenting

. . . extends beyond Miranda’s protection of the Fifth
Amendment right to counsel, . . . there will be cases where
a waiver which would be valid under Miranda will not
suffice for Sixth Amendment purposes.” Id., at 297, n. 9.
This is such a case.
    As I observed in Patterson, the conclusion that Miranda
warnings ordinarily provide a sufficient basis for a know
ing waiver of the right to counsel rests on the questionable
assumption that those warnings make clear to defendants
the assistance a lawyer can render during post-indictment
interrogation. See 487 U. S., at 307 (dissenting opinion).
Because Miranda warnings do not hint at the ways in
which a lawyer might assist her client during conversa
tions with the police, I remain convinced that the warn
ings prescribed in Miranda,7 while sufficient to apprise a
defendant of his Fifth Amendment right to remain silent,
are inadequate to inform an unrepresented, indicted de
fendant of his Sixth Amendment right to have a lawyer
present at all critical stages of a criminal prosecution. The
inadequacy of those warnings is even more obvious in the
case of a represented defendant. While it can be argued
that informing an indicted but unrepresented defendant of
his right to counsel at least alerts him to the fact that he is
entitled to obtain something he does not already possess,
providing that same warning to a defendant who has
already secured counsel is more likely to confound than
enlighten.8 By glibly assuming that that the Miranda
——————
  7 Under Miranda, a suspect must be “warned prior to any questioning

that he has the right to remain silent, that anything he says may be
used against him in court of law, that he has the right to the presence
of any attorney, and that if he cannot afford an attorney, one will be
appointed for him prior to any questioning if he so desires.” 384 U. S.,
at 479.
  8 With respect to vulnerable defendants, such as juveniles and those

with mental impairments of various kinds, amici National Association
of Criminal Defense Lawyers et al. assert that “[o]verruling Jackson
would be particularly detrimental . . . because of the confusing instruc
14                    MONTEJO v. LOUISIANA

                        STEVENS, J., dissenting

warnings given in this case were sufficient to ensure
Montejo’s waiver was both knowing and voluntary, the
Court conveniently avoids any comment on the actual
advice Montejo received, which did not adequately inform
him of his relevant Sixth Amendment rights or alert him
to the possible consequences of waiving those rights.
  A defendant’s decision to forgo counsel’s assistance and
speak openly with police is a momentous one. Given the
high stakes of making such a choice and the potential
value of counsel’s advice and mediation at that critical
stage of the criminal proceedings, it is imperative that a
defendant possess “a full awareness of both the nature of
the right being abandoned and the consequences of the
decision to abandon it,” Moran v. Burbine, 475 U. S. 412,
421 (1986), before his waiver is deemed valid. See Iowa v.
Tovar, 541 U. S. 77, 81 (2004); Johnson v. Zerbst, 304
U. S. 458, 464 (1938). Because the administration of
Miranda warnings was insufficient to ensure Montejo
understood the Sixth Amendment right he was being
asked to surrender, the record in this case provides no
basis for concluding that Montejo validly waived his right
to counsel, even in the absence of Jackson’s enhanced
protections.
                            IV
  The Court’s decision to overrule Jackson is unwar
ranted. Not only does it rests on a flawed doctrinal prem
——————
tions regarding counsel that they would receive. At the initial hearing,
they would likely learn that an attorney was being appointed for them,
In a later custodial interrogation, however, they would be informed in
the traditional manner of ‘their right to counsel’ and right to have
counsel ‘appointed’ if they are indigent, notwithstanding that counsel
had already been appointed in open court. These conflicting statements
would be confusing to anyone, but would be especially baffling to
defendants with mental disabilities or other impairments.” Supple
mental Brief for National Association of Criminal Defense Lawyers
et al. as Amici Curiae 7–8.
                Cite as: 556 U. S. ____ (2009)         15

                   STEVENS, J., dissenting

ise, but the dubious benefits it hopes to achieve are far
outweighed by the damage it does to the rule of law and
the integrity of the Sixth Amendment right to counsel.
Moreover, even apart from the protections afforded by
Jackson, the police interrogation in this case violated
Jesse Montejo’s Sixth Amendment right to counsel.
  I respectfully dissent.
                  Cite as: 556 U. S. ____ (2009)            1

                     BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 07–1529
                          _________________


         JESSE JAY MONTEJO, PETITIONER v. 

                    LOUISIANA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      LOUISIANA

                         [May 26, 2009] 


   JUSTICE BREYER, dissenting.
   I join JUSTICE STEVENS’ dissent except for footnote 5.
Although the principles of stare decisis are not inflexible, I
believe they bind the Court here. I reached a similar
conclusion in Arizona v. Gant, 556 U. S. ___, ___–___
(2009) (slip op., at 1–2) (BREYER, J., dissenting), and in
several other recent cases. See, e.g., Leegin Creative
Leather Products, Inc. v. PSKS, Inc., 551 U. S. 877, ___–
___ (2007) (slip op., at 17–19) (BREYER, J., dissenting);
Parents Involved in Community Schools v. Seattle School
Dist. No. 1, 551 U. S. 701, ___–___ (2007) (slip op., at 65–
66) (BREYER, J., dissenting); Federal Election Comm’n v.
Wisconsin Right to Life, Inc., 551 U. S. 449, ___–___ (2007)
(slip op., at 31–32) (SOUTER, J., dissenting); Bowles v.
Russell, 551 U. S. 205, 219–220 (2007) (SOUTER, J., dis
senting); Gonzales v. Carhart, 550 U. S. 124, 190–191
(2007) (GINSBURG, J., dissenting); District of Columbia v.
Heller, 554 U. S. ___, ___–___ (2008) (slip op. at 41–45)
(STEVENS, J., dissenting).

```

---

## GROUP: _overhaul2/lake/cases/Mooney v. Holohan.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Mooney v. Holohan"
type: case
citation: "294 U.S. 103 (1935)"
parallel_cite: "55 S. Ct. 340; 79 L. Ed. 791; 98 A.L.R. 406"
neutral_cite: 1935 U.S. LEXIS 40
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1935
date_decided: 1935-01-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1935-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mooney v. Holohan
  varies_by_point: false
  scope_note: "Good law as to its core due-process principle — the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)"
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/102372/mooney-v-holohan/"
  cluster_id: 102372
  opinion_id: 102372
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor (historical origin)"
related: ["[[Napue v. Illinois]]", "[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[Banks v. Dretke]]", "[[Glossip v. Oklahoma]]"]
aliases: []
tags: ["case", "brady", "giglio", "napue", "perjured-testimony", "prosecutorial-misconduct", "due-process", "historical"]
holding: "The knowing use of perjured testimony by the prosecution to obtain a conviction violates Fourteenth Amendment due process — a 'deliberate deception of court and jury' is as inconsistent with justice as obtaining a conviction by intimidation. (Leave to file the original habeas petition was denied for failure to exhaust state remedies.)"
lake:
  record_id: Mooney v. Holohan
  status: under_review
  projected_at: 2026-07-06
---

# Mooney v. Holohan

*294 U.S. 103 (1935)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Tom Mooney, convicted in California in connection with the 1916 San Francisco Preparedness Day bombing, sought leave to file an original petition for a writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] in the Supreme Court. He alleged that the State had knowingly used perjured testimony to obtain his conviction and had deliberately suppressed evidence that would have impeached that testimony, in violation of the Fourteenth Amendment.

## Issue
Whether the knowing use of perjured testimony (and suppression of impeaching evidence) by state prosecutors to procure a conviction violates due process — and whether the petitioner could pursue that claim by an original [[Common Legal Terms#habeas-corpus|habeas]] petition in the Supreme Court without first exhausting state remedies.

## Rule
Knowing use of perjured testimony violates due process. The Fourteenth Amendment "is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation." — 294 U.S. at 112. ^pin-112

The Court also confirmed that prosecutorial conduct counts as state action: "the action of prosecuting officers on behalf of the State … may constitute state action within the purview of the Fourteenth Amendment." — *Id.*

## Application
The Court accepted that the alleged conduct — if proven — would violate due process, articulating the principle that a conviction obtained through testimony the State knows to be perjured cannot stand. But it did not reach the truth of Mooney's allegations. Because relief by [[Common Legal Terms#habeas-corpus|habeas corpus]] appeared to be available in the California courts and Mooney had not shown that the State afforded no corrective judicial process, the Court held it should not entertain an original petition; leave to file was denied without prejudice to an application to the state courts.

## Conclusion
Leave to file the original [[Common Legal Terms#habeas-corpus|habeas]] petition was denied for failure to exhaust available state remedies. The decision is foundational not for its procedural disposition but for its due-process holding: a state may not knowingly use perjured testimony to obtain a conviction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- *Mooney* is the **historical origin** of the prosecutorial-honesty line in due process. Its knowing-perjury rule was extended and refined by [[Napue v. Illinois]] (duty to correct false testimony) and [[Giglio v. United States]] (applies to impeachment of cooperating witnesses), applied most recently in [[Glossip v. Oklahoma]] (2025), and runs alongside the affirmative-disclosure duty of [[Brady v. Maryland]] and [[Banks v. Dretke]]. The core principle remains good law.

## Appears on
- [[Brady and Giglio]] — *Key — Anchor (historical origin)*

## Sources
- *Mooney v. Holohan*, 294 U.S. 103 (1935) (per curiam) — https://www.courtlistener.com/opinion/102372/mooney-v-holohan/ — pinpoint: 112.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "19586de6086a42dd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mooney v. Holohan"}, "payload": {"all": [{"cite": "294 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "294"}, {"cite": "55 S. Ct. 340", "page": "340", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "55"}, {"cite": "79 L. Ed. 791", "page": "791", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "79"}, {"cite": "1935 U.S. LEXIS 40", "page": "40", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1935"}, {"cite": "98 A.L.R. 406", "page": "406", "reporter": "A.L.R.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "98"}], "display": "294 U.S. 103", "official": {"cite": "294 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "294"}, "official_selection_present": true, "record_id": "Mooney v. Holohan"}}
{"assertion_id": "e15a04573eaaefc6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-112", "record_id": "Mooney v. Holohan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-112", "pinpoint_status": "slip-only", "quote": "--- # Mooney v. Holohan *294 U.S. 103 (1935)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tom Mooney, convicted in California in connection with the 1916 San Francisco Preparedness Day bombing, sought leave to file an original petition for a writ of habeas corpus in the Supreme Court. He alleged that the State had knowingly used perjured testimony to obtain his conviction and had deliberately suppressed evidence that would have impeached that testimony, in violation of the Fourteenth Amendment. ## Issue Whether the knowing use of perjured testimony (and suppression of impeaching evidence) by state prosecutors to procure a conviction violates due process — and whether the petitioner could pursue that claim by an original habeas petition in the Supreme Court without first exhausting state remedies. ## Rule Knowing use of perjured testimony violates due process. The Fourteenth Amendment", "quote_fidelity": "mismatch", "record_id": "Mooney v. Holohan", "star_marker": null}}
{"assertion_id": "5e50c9722df81ae1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mooney v. Holohan"}, "payload": {"as_of_content": "1935-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mooney v. Holohan", "scope_note": "Good law as to its core due-process principle — the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)", "varies_by_point": false}}
```

### lake record — Mooney v. Holohan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mooney v. Holohan",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Mooney v. Holohan",
    "case_name_short": "Mooney",
    "case_name_full": "Mooney v. Holohan, Warden",
    "input_case_name": "Mooney v. Holohan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1935-01-21",
    "year": 1935,
    "docket": null,
    "cluster_id": 102372,
    "lead_opinion_id": 102372,
    "sibling_ids": [
      102372
    ],
    "absolute_url": "/opinion/102372/mooney-v-holohan/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "294 U.S. 103",
      "volume": "294",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "55 S. Ct. 340",
        "volume": "55",
        "reporter": "S. Ct.",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 L. Ed. 791",
        "volume": "79",
        "reporter": "L. Ed.",
        "page": "791",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 A.L.R. 406",
        "volume": "98",
        "reporter": "A.L.R.",
        "page": "406",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1935 U.S. LEXIS 40",
        "volume": "1935",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "294 U.S. 103",
        "volume": "294",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 S. Ct. 340",
        "volume": "55",
        "reporter": "S. Ct.",
        "page": "340",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 L. Ed. 791",
        "volume": "79",
        "reporter": "L. Ed.",
        "page": "791",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1935 U.S. LEXIS 40",
        "volume": "1935",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 A.L.R. 406",
        "volume": "98",
        "reporter": "A.L.R.",
        "page": "406",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "294 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "294 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-112",
      "page": null,
      "quote": "--- # Mooney v. Holohan *294 U.S. 103 (1935)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tom Mooney, convicted in California in connection with the 1916 San Francisco Preparedness Day bombing, sought leave to file an original petition for a writ of habeas corpus in the Supreme Court. He alleged that the State had knowingly used perjured testimony to obtain his conviction and had deliberately suppressed evidence that would have impeached that testimony, in violation of the Fourteenth Amendment. ## Issue Whether the knowing use of perjured testimony (and suppression of impeaching evidence) by state prosecutors to procure a conviction violates due process \u2014 and whether the petitioner could pursue that claim by an original habeas petition in the Supreme Court without first exhausting state remedies. ## Rule Knowing use of perjured testimony violates due process. The Fourteenth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1935-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mooney v. Holohan",
    "varies_by_point": false,
    "scope_note": "Good law as to its core due-process principle \u2014 the precursor of the Napue/Giglio knowing-perjury line and the Brady disclosure line. (Its procedural holding remitting the petitioner to state habeas reflects 1935 exhaustion practice.)",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Antonio Smith v. State of Indiana",
          "cluster_id": 2812363,
          "cite": [
            "34 N.E.3d 1211",
            "2015 Ind. LEXIS 567",
            "2015 WL 3929923"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guzman v. Secretary, Department of Corrections",
          "cluster_id": 618520,
          "cite": [
            "663 F.3d 1336",
            "2011 U.S. App. LEXIS 24465",
            "2011 WL 6061337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Napper, Ex Parte Lawrence James",
          "cluster_id": 2943007,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Krizan-Wilson",
          "cluster_id": 2275981,
          "cite": [
            "321 S.W.3d 619",
            "2010 WL 2483784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Carolyn Sue Krizan-Wilson",
          "cluster_id": 2992921,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McKithen v. Brown",
          "cluster_id": 1458192,
          "cite": [
            "565 F. Supp. 2d 440",
            "2008 U.S. Dist. LEXIS 55094",
            "2008 WL 2791852"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brady v. Maryland",
          "cluster_id": 106598,
          "cite": [
            "10 L. Ed. 2d 215",
            "83 S. Ct. 1194",
            "373 U.S. 83",
            "1963 U.S. LEXIS 1615"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Zerbst",
          "cluster_id": 103050,
          "cite": [
            "304 U.S. 458",
            "58 S. Ct. 1019",
            "82 L. Ed. 1461",
            "1938 U.S. LEXIS 896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Giglio v. United States",
          "cluster_id": 108471,
          "cite": [
            "31 L. Ed. 2d 104",
            "92 S. Ct. 763",
            "405 U.S. 150",
            "1972 U.S. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Napue v. Illinois",
          "cluster_id": 105912,
          "cite": [
            "3 L. Ed. 2d 1217",
            "79 S. Ct. 1173",
            "360 U.S. 264",
            "1959 U.S. LEXIS 811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donnelly v. DeChristoforo",
          "cluster_id": 109024,
          "cite": [
            "40 L. Ed. 2d 431",
            "94 S. Ct. 1868",
            "416 U.S. 637",
            "1974 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Allen",
          "cluster_id": 108110,
          "cite": [
            "25 L. Ed. 2d 353",
            "90 S. Ct. 1057",
            "397 U.S. 337",
            "1970 U.S. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buckley v. Fitzsimmons",
          "cluster_id": 112894,
          "cite": [
            "125 L. Ed. 2d 209",
            "113 S. Ct. 2606",
            "509 U.S. 259",
            "1993 U.S. LEXIS 4400"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haguer v. Committee for Industrial Organization",
          "cluster_id": 103226,
          "cite": [
            "307 U.S. 496",
            "59 S. Ct. 954",
            "83 L. Ed. 1423",
            "1939 U.S. LEXIS 1067",
            "4 L.R.R.M. (BNA) 501"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
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
        "journal_ref": "Mooney v. Holohan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(102372) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAxMDQ2NDAwMDAwJnM9MTI3MjQyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28102372%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(102372)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODQmcz0xMTE2MDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28102372%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(102372)",
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
    "complete_query": "cites:(102372)",
    "indexed_citing_opinions": 1195,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 102372,
        "count": 1195,
        "count_source": "search"
      }
    ],
    "citation_count": 1838,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mooney-v-holohan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1MzMyNTYmcz01MzA0MTMwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28102372%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 102372,
        "cited_id": 91149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 95992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 101335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 2620727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3302184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3303533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3308686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102372,
        "cited_id": 3309150,
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
    "date_created": "2026-07-05T14:36:03Z",
    "date_modified": "2026-07-06T08:25:38Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:39:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:36:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mooney v. Holohan

```
<?xml version="1.0" encoding="utf-8"?>
<opinion data-order="7" data-type="opinion" id="x999-1" type="majority">
<author id="b159-8">
<span citation-index="1" class="star-pagination" label="109"> 
   *109
   </span>
  Per Curiam.
 </author>
<p id="b159-9">
  Thomas J. Mooney asks leave to file petition for an original writ of
  <em>
   habeas corpus.
  </em>
  He states that he is unlawfully restrained of his liberty by the State of California under a commitment pursuant to a conviction, in February, 1917, of murder in the first degree and sentence of death subsequently commuted to life imprisonment. He submits the record of proceedings set forth in his petition for a writ of
  <em>
   habeas corpus
  </em>
  presented to the District
  <span citation-index="1" class="star-pagination" label="110"> 
   *110
   </span>
  Court of the United States for the Northern District of California and dismissed upon the ground that the petitioner had not exhausted his legal remedies in the state court. Applications to the Judges of the Circuit Court of Appeals for the Ninth Circuit for allowance of an appeal to that Court from the judgment of dismissal have severally been denied.
 </p>
<p id="b160-6">
  Petitioner charges that the State holds him in confinement without due process of law in violation of the Fourteenth Amendment of the Constitution of the United States. The grounds of his charge are, in substance, that the sole basis of his conviction was perjured testimony, which was knowingly used by the prosecuting authorities in order to obtain that conviction, and also that these authorities deliberately suppressed evidence which would have impeached and refuted the testimony thus given against him. He alleges that he could not by reasonable diligence have discovered prior to the denial of his motion for a new trial, and his appeal to the Supreme Court of the State, the evidence which was subsequently developed and which proved the testimony against him to have been perjured. Petitioner urges that the
  <em>
   “
  </em>
  knowing use ” by the State of perjured testimony to obtain the conviction and the deliberate suppression of evidence to impeach that testimony constituted a denial of due process of law. Petitioner further contends that the State deprives him of his liberty without due process of law by its failure, in the circumstances set forth, to provide any corrective judicial process by which a conviction so obtained may be set aside.
 </p>
<p id="b160-7">
  In support of his serious charges, petitioner submits a •chronological history of the trials, appeals and other judicial proceedings connected with his conviction, and of his applications for executive clemency. He sets forth the evidence which, as he contends, proves the perjury
  <span citation-index="1" class="star-pagination" label="111"> 
   *111
   </span>
  of the witnesses upon whose testimony he was convicted and the knowledge on the part of the prosecuting authorities of that perjury and the suppression by those authorities of impeaching evidence at their command. He also submits what he insists are admissions by the State that the testimony offered against him was perjured and that his conviction was unjustified. In amplification of these statements, he asks leave to incorporate in his petition, by reference, the voluminous details of the various proceedings as they were presented with his petition to the District Court.
 </p>
<p id="b161-6">
  In response to our rule to show cause why leave to file the petition should not be granted, the respondent has made return by the Attorney General of the State. With this return, he submits an appendix of exhibits setting forth the consent filed by the Attorney General with the Supreme Court of the State on July 30, 1917, that the judgment of conviction be reversed and the cause remanded for a new trial, the subsequent opinions of that Court upon the cases presented to it, the statements of Governors of the State on applications for executive clemency made on behalf of this petitioner and of one Billings (who had been jointly indicted with petitioner and was separately tried and convicted), and the reports of Justices of the Supreme Court of the State, and communications addressed by them, to the Governors of the State in connection with such applications.
 </p>
<p id="b161-7">
  The return does not put in issue any of the facts alleged in the petition. The return is in the nature of a demurrer. It submits that the petitioner “ has failed, to raise a Federal question and that, consequently, leave to file the petition should be denied.” Reviewing decisions relating to due process, the Attorney General insists that the petitioner’s argument is vitiated by the fallacy “ that the acts or omissions of- a prosecuting- attorney can ever,
  <span citation-index="1" class="star-pagination" label="112"> 
   *112
   </span>
<em>
   in and by themselves,
  </em>
  amount either to due process of law or to a denial of due process of law.” The Attorney-General states that if the acts or omissions of a prosecuting attorney “have the effect of withholding from a defendant the notice which must be accorded him under the due process clause, or if they have the effect of preventing a defendant from presenting such evidence as he possesses in defense of the accusation against him, then such acts or omissions of the prosecuting attorney may be regarded as
  <em>
   resulting
  </em>
  in a denial of due process of law.” And, “ conversely,” the Attorney General contends that “ it is only where an act or omission operates so as to deprive a defendant of notice or so as to deprive him of an opportunity to present such evidence as he has, that it can be said that due process of law has been denied.”
 </p>
<p id="A9S">
  Without attempting at this time to deal with the question at length, we deem it sufficient for the present purpose to say that we are unable to approve this narrow view of the requirement of due process. That requirement, in safeguarding the liberty of the citizen against deprivation through the action of the State, embodies the fundamental conceptions of justice which lie at the base of our civil and political institutions.
  <em>
   Hebert
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U. S. 312, 316, 317</a></span>. It is a requirement that cannot be deemed tó be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation. And the action of prosecuting officers on behalf of the State, like that of adminis
  <span citation-index="1" class="star-pagination" label="113"> 
   *113
   </span>
  trative officers in the execution of its laws, may constitute state action within the purview of the Fourteenth Amendment. That Amendment governs any action of a State, “ whether through its legislature, through its courts, or through its executive or administrative officers.”
  <em>
   Carter
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="95255"><a href="/opinion/95255/carter-v-texas/#447" aria-description="Citation for case: Carter v. Texas">177 U. S. 442, 447</a></span>;
  <em>
   Rogers
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="95992"><a href="/opinion/95992/rogers-v-alabama/#231" aria-description="Citation for case: Rogers v. Alabama">192 U. S. 226, 231</a></span>;
  <em>
   Chicago, Burlington &amp; Quincy R. Co.
  </em>
  v.
  <em>
   Chicago,
  </em>
  <span class="citation" data-id="9417760"><a href="/opinion/94648/chicago-burlington-quincy-railroad-v-chicago/#233" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. Chicago">166 U. S. 226, 233, 234</a></span>.
 </p>
<p id="b163-6">
  Reasoning from the premise that the petitioner has failed to show a denial of due process in the circumstances set forth in his petition, the Attorney General urges that the State was not required to afford any corrective judicial process to remedy the alleged wrong. The argument falls with the premise.
  <em>
   Frank
  </em>
  v.
  <em>
   Mangum,
  </em>
  <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#335" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 335</a></span>;
  <em>
   Moore
  </em>
  v.
  <em>
   Dempsey,
  </em>
  <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/#90" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86, 90, 91</a></span>.
 </p>
<p id="b163-7">
  We are not satisfied, however, that the State of California has failed to provide such corrective judicial process. The prerogative writ of
  <em>
   habeas corpus
  </em>
  is available in that State. Constitution of California, Art. I, § 5; Art. VI, § 4. No decision of the Supreme Court of California has been brought to our attention holding that the state court is without power to issue this historic remedial process when it appears that one is deprived of his liberty without due process of law in violation of the Constitution of the United States. Upon the state courts, equally with the courts of the Union, rests the obligation to guard and enforce every right secured by that Constitution.
  <em>
   Robb
  </em>
  v.
  <em>
   Connolly,
  </em>
  <span class="citation" data-id="91149"><a href="/opinion/91149/robb-v-connolly/#637" aria-description="Citation for case: Robb v. Connolly">111 U. S. 624, 637</a></span>. In view of the dominant requirement of the Fourteenth Amendment, we are not at liberty to assume that the State has denied to its court jurisdiction to redress the prohibited wrong upon a proper showing and in an appropriate proceeding for that purpose.
 </p>
<p id="b163-8">
  The decisions of the Supreme Court of California in relation to petitioner’s conviction have dealt with the ques
  <span citation-index="1" class="star-pagination" label="114"> 
   *114
   </span>
  tions presented to that Court within the limitations of particular appellate procedure. When there was submitted to that Court the consent of the Attorney General to the reversal of the judgment against petitioner and to the granting of a new trial, the Court pointed out that no motion had been made by the defendant and that his appeal was awaiting hearing.
  <em>
   People
  </em>
  v. Mooney, <span class="citation" data-id="3302184"><a href="/opinion/3302906/people-v-mooney/" aria-description="Citation for case: People v. Mooney">175 Cal. 666</a></span>; <span class="citation" data-id="3302184"><a href="/opinion/3302906/people-v-mooney/" aria-description="Citation for case: People v. Mooney">166 Pac. 999</a></span>. When, again in advance of the hearing of his appeal, the defendant made his motion solely upon the ground of the Attorney General’s consent, the Court held that its jurisdiction on appeal was limited to a determination whether there had been any error of law in the proceedings of the trial court and that the Court was confined to the record sent to it by the court below.
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3303533"><a href="/opinion/3304127/people-v-mooney/" aria-description="Citation for case: People v. Mooney">176 Cal. 105</a></span>; <span class="citation" data-id="3303533"><a href="/opinion/3304127/people-v-mooney/" aria-description="Citation for case: People v. Mooney">167 Pac. 696</a></span>. On the appeal, the Court thus dealing with the record before it, found that the verdict was supported by the testimony presented and that no ground appeared for reversal.
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3308686"><a href="/opinion/3308670/people-v-mooney/" aria-description="Citation for case: People v. Mooney">177 Cal. 642</a></span>; <span class="citation" data-id="3308686"><a href="/opinion/3308670/people-v-mooney/" aria-description="Citation for case: People v. Mooney">171 Pac. 690</a></span>. When, later, the defendant moved to set aside the judgment, and sought a certificate of probable cause on his appeal from an order denying his motion, the Court held that the general averments against the fairness of the trial were insufficient, but the Court did not place its denial of the application entirely upon that ground. The Court concluded that the proceeding by way of motion to set aside the judgment after it had become final and a motion for a new trial had been denied, and the time therefor had expired, was “in the nature of an application for a writ of
  <em>
   cor cm nobis,
  </em>
  at common law.” The Court thought that such a writ did not lie to correct any error in the judgment of the Court nor to contradict or put in issue any fact directly passed upon and affirmed by the judgment itself. The Court, adopting the opinion of the court below, concluded that the judgment could not be set aside because it was predicated upon
  <span citation-index="1" class="star-pagination" label="115"> 
   *115
   </span>
  perjured testimony or because material evidence was concealed or suppressed; that the fraud in such a case was not such fraud as was
  <em>
   “
  </em>
  extrinsic to the record ” and that it was only in cases of extrinsic fraud that the relief sought could be had. It was apparently in relation to such an application that the Court said that the injured party was “ without remedy.”
  <em>
   People
  </em>
  v.
  <em>
   Mooney,
  </em>
  <span class="citation" data-id="3309150"><a href="/opinion/3309089/people-v-mooney/" aria-description="Citation for case: People v. Mooney">178 Cal. 525</a></span>; <span class="citation" data-id="3309150"><a href="/opinion/3309089/people-v-mooney/" aria-description="Citation for case: People v. Mooney">174 Pac. 325</a></span>. And it was with respect to that proceeding, that the writ of certiorari was denied by this Court.
  <em>
   Mooney
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="8143670"><a href="/opinion/8181751/mooney-v-california/" aria-description="Citation for case: Mooney v. California">248 U. S. 579</a></span>. The subsequent communications from the Justices of the Supreme Court in connection with applications for executive clemency were of an advisory character and were not judicial judgments under the requirements of the Constitution of the United States.
 </p>
<p id="b165-6">
  We do not find that petitioner has applied to the state court for a writ of
  <em>
   habeas corpus
  </em>
  upon the grounds stated in his petition here. That corrective judicial process has not been invoked and it is not shown to be unavailable. Despite the many proceedings taken on behalf of the petitioner, an application for the prerogative writ now asserted to be peculiarly suited to the circumstances disclosed by his petition has not been made to the state court. Orderly procedure, governed by principles we have repeatedly announced, requires that before this Court is asked to issue a writ of
  <em>
   habeas corpus,
  </em>
  in the case of a person held under a state commitment, recourse should be had to whatever judicial remedy afforded by the State may still remain open.
  <em>
   Davis
  </em>
  v.
  <em>
   Burke,
  </em>
  <span class="citation" data-id="95368"><a href="/opinion/95368/davis-v-burke/#402" aria-description="Citation for case: Davis v. Burke">179 U. S. 399, 402</a></span>;
  <em>
   Urquhart
  </em>
  v.
  <em>
   Brown,
  </em>
  <span class="citation" data-id="2620727"><a href="/opinion/2620727/urquhart-v-brown/#181" aria-description="Citation for case: Urquhart v. Brown">205 U. S. 179, 181, 182</a></span>;
  <em>
   U. S. ex rel. Kennedy
  </em>
  v.
  <em>
   Tyler,
  </em>
  <span class="citation" data-id="100710"><a href="/opinion/100710/united-states-ex-rel-kennedy-v-tyler/#17" aria-description="Citation for case: United States Ex Rel. Kennedy v. Tyler">269 U. S. 13, 17</a></span>. See, also,
  <em>
   Bryant
  </em>
  v.
  <em>
   Zimmerman,
  </em>
  <span class="citation" data-id="101335"><a href="/opinion/101335/new-york-ex-rel-bryant-v-zimmerman/#70" aria-description="Citation for case: New York Ex Rel. Bryant v. Zimmerman">278 U. S. 63, 70</a></span>.
 </p>
<p id="b165-7">
  Accordingly, leave to file the petition is denied, but without prejudice.
 </p>
<p id="b165-8">
<em>
   Leave denied.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Moore v. Illinois.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Moore v. Illinois
type: case
citation: "434 U.S. 220 (1977)"
parallel_cite: "98 S. Ct. 458; 54 L. Ed. 2d 424"
neutral_cite: 1977 U.S. LEXIS 163
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-12-12
docket: No. 76-5344
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
  opinion_url: "https://www.courtlistener.com/opinion/109757/moore-v-illinois/"
  cluster_id: 109757
  opinion_id: null
  identity_checked: true
lake:
  record_id: Moore v. Illinois
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Lineups and the Right to Counsel]]"
    role: Anchor
related:
  - "[[Lineups and the Right to Counsel]]"
  - "[[United States v. Wade]]"
  - "[[Gilbert v. California]]"
  - "[[Kirby v. Illinois]]"
tags:
  - case
  - sixth-amendment
  - right-to-counsel
  - identification
  - critical-stage
  - preliminary-hearing
holding: "The Sixth Amendment right to counsel attaches to a corporeal identification conducted after the initiation of adversary judicial criminal proceedings, so admitting an in-court reference to an uncounseled identification made of the accused at a preliminary hearing — a critical stage — violated his right to counsel under Wade and Gilbert."
aliases:
  - Moore v. Illinois
  - "Moore v. Illinois (1977)"
---

# Moore v. Illinois

*434 U.S. 220 (1977)* (No. 76-5344) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109757 → combined opinion 109757 (Powell, J.; 434 U.S. 220, decided Dec. 12, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*231` precedes the quoted sentence). S9 promotes. -->

## Background
A rape victim identified the petitioner as her assailant at a preliminary hearing. He appeared before the judge without counsel; the victim was told in advance that the man being brought before the bench was the suspect, and she identified him in that one-on-one setting. At trial she testified to that preliminary-hearing identification. The petitioner argued that conducting the identification without counsel, after formal proceedings had begun, violated his Sixth Amendment right to counsel under *[[United States v. Wade]]* and *[[Gilbert v. California]]*.

## Issue
Whether the Sixth Amendment right to counsel applies to a corporeal identification conducted at a preliminary hearing held after the initiation of adversary judicial criminal proceedings.

## Rule
Applying the rule of *[[United States v. Wade|Wade]]*, *[[Gilbert v. California|Gilbert]]*, and *[[Kirby v. Illinois]]* — that the right to counsel attaches to identifications conducted at or after the initiation of adversary judicial proceedings — the Court held: "Here, as in those cases, petitioner's Sixth Amendment rights were violated by a corporeal identification conducted after the initiation of adversary judicial criminal proceedings and in the absence of counsel." — 434 U.S. at 231. ^pin-231

## Application
The preliminary hearing marked the initiation of adversary judicial proceedings: the State had committed to prosecute, and the petitioner faced its prosecutorial forces at a hearing where counsel could have moved to dismiss and to suppress. Under *[[Kirby v. Illinois|Kirby]]*, the *Wade–Gilbert* right had therefore attached, and the Court of Appeals erred in confining that right to post-indictment identifications. Counsel's presence might also have blunted the identification's extreme suggestiveness. The uncounseled corporeal identification thus violated the Sixth Amendment.

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] (for the state courts to consider [[Inevitable Discovery and Independent Source|independent source]] and harmless error). Powell, J., delivered the opinion of the Court; Blackmun, J., concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Moore* applies the *[[United States v. Wade|Wade]]*–*[[Gilbert v. California|Gilbert]]*–*[[Kirby v. Illinois|Kirby]]* framework to a preliminary-hearing show-up: once adversary judicial proceedings begin, a corporeal identification is a **critical stage** requiring counsel. Teach it for the attachment line — the right runs from the initiation of formal proceedings (by formal charge, preliminary hearing, indictment, information, or arraignment), not from arrest alone.

## Appears on
- [[Lineups and the Right to Counsel]] — *Anchor*

## Sources
- [*Moore v. Illinois*, 434 U.S. 220 (1977)](https://www.courtlistener.com/opinion/109757/moore-v-illinois/) — pinpoint: 231 (Powell, J., for the Court; the CL opinion text carries the reporter star `*231` immediately before the quoted sentence). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "97c1cc0a307be5b6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Moore v. Illinois"}, "payload": {"all": [{"cite": "434 U.S. 220", "page": "220", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "434"}, {"cite": "98 S. Ct. 458", "page": "458", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "54 L. Ed. 2d 424", "page": "424", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "54"}, {"cite": "1977 U.S. LEXIS 163", "page": "163", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "434 U.S. 220", "official": {"cite": "434 U.S. 220", "page": "220", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "434"}, "official_selection_present": true, "record_id": "Moore v. Illinois"}}
{"assertion_id": "b9741691ced7e983", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Moore v. Illinois"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Moore v. Illinois", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Moore v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Moore v. Illinois",
  "status": "under_review",
  "identity": {
    "case_name": "Moore v. Illinois",
    "case_name_short": "Moore",
    "case_name_full": "Moore v. Illinois",
    "input_case_name": "Moore v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-12-12",
    "year": 1977,
    "docket": "No. 76-5344",
    "cluster_id": 109757,
    "lead_opinion_id": 9427017,
    "sibling_ids": [],
    "absolute_url": "/opinion/109757/moore-v-illinois/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "434 U.S. 220",
      "volume": "434",
      "reporter": "U.S.",
      "page": "220",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 458",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 424",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 163",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "163",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "434 U.S. 220",
        "volume": "434",
        "reporter": "U.S.",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 458",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 424",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 163",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "163",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "434 U.S. 220",
    "official_selection": {
      "court_class": "scotus",
      "selected": "434 U.S. 220",
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
    "date_created": "2026-07-06T13:45:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "moore-v-illinois--109757",
      "to_record_id": "Moore v. Illinois",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Moore v. Illinois

```
<opinion type="majority">
<author id="b393-10">Mr. Justice Powell</author>
<p id="A-i">delivered the opinion of the Court.</p>
<p id="b393-11">Petitioner was convicted of rape and related offenses. At trial the complaining witness testified on direct examination by the prosecution that she had identified petitioner at a preliminary hearing at which he was not represented by counsel. The State Supreme Court affirmed petitioner's convictions, and the Federal District Court and Court of Appeals denied habeas corpus relief. We granted certiorari because of an apparent conflict between the decisions below and our holdings with respect to the right to counsel at corporeal identifications in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> <em>(1967); </em>and <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972). We reverse.</p>
<p id="b393-12">I</p>
<p id="b393-13">The victim of the offenses in question lived in an apartment on the South Side of Chicago. Shortly after noon on December 14, 1967, she awakened from a nap to find a man standing in the doorway to her bedroom holding a knife. The man entered the bedroom, threw her face down on the bed, and <page-number citation-index="1" label="222">*222</page-number>choked her until she was quiet. After covering his face with a bandana, the intruder partially undressed the victim, forced her to commit oral sodomy, and raped her. Then he left, taking a guitar and a flute from the apartment.</p>
<p id="b394-5">When police arrived, the victim gave them a description of her assailant. Although she did not know who he was and had seen his face for only 10 to 15 seconds during the attack, she thought he was the same man who had made offensive remarks to her in a neighborhood bar the night before. She also gave police a notebook she had found next to her bed after the attack.</p>
<p id="b394-6">In the week that followed, police showed the victim two groups of photographs of men. From the first group of 200 she picked about 30 who resembled her assailant in height, weight, and build. From the second group of about 10, she picked two or three. One of these was of petitioner. Police also found a letter in the notebook that the victim had given them. Investigation revealed that it was written by a woman with whom petitioner had been staying. The letter had been taken from the woman’s home in her absence, and petitioner appeared to be the only other person who had access to the home.</p>
<p id="b394-7">On the evening of December 20, 1967, police arrested petitioner at his apartment and held him overnight pending a preliminary hearing to determine whether he should be bound over to the grand jury and to set bail. The next morning, a policeman accompanied the victim to the Circuit Court of Cook County (First Municipal District) for the hearing. The policeman told her she was going to view a suspect and should identify him if she could. He also had her sign a complaint that named petitioner as her assailant. At the hearing, petitioner’s name was called and he was led before the bench. The judge told petitioner that he was charged with rape and deviate sexual behavior. The judge then called the victim, who had been in the courtroom waiting for the case to be called, to come before the bench. The State’s Attorney stated <page-number citation-index="1" label="223">*223</page-number>that police had found evidence linking petitioner with the offenses charged. He asked the victim whether she saw her assailant in the courtroom, and she pointed at petitioner. The State’s Attorney then requested a continuance of the hearing because more time was needed to check fingerprints. The judge granted the continuance and fixed bail. Petitioner was not represented by counsel at this hearing, and the court'did not offer to appoint counsel.</p>
<p id="b395-5">At a subsequent hearing, petitioner was bound over to the grand jury, which indicted him for rape, deviate sexual behavior, burglary, and robbery. Counsel was appointed, and he moved to suppress the victim’s identification of petitioner because it had been elicited at the preliminary hearing through an unnecessarily suggestive procedure at which petitioner was not represented by counsel.<footnotemark>1</footnotemark> After an evidentiary hearing the trial court denied the motion on the ground that the prosecution had shown an independent basis for the victim’s identification.</p>
<p id="b395-6">At trial, the victim testified on direct examination by the prosecution that she had identified petitioner as her assailant at the preliminary hearing. She also testified that the defendant on trial was the man who had raped her. The prosecution’s other evidence linking petitioner with the crimes was the letter found in the victim’s apartment. Defense counsel stipulated that petitioner had taken the letter from his woman friend’s home, but he presented evidence that petitioner might have lost the notebook containing the letter at the neighborhood bar the night before the attack. The defense theory was that the victim, who also was in the bar that night, could have picked up the notebook by mistake and taken it home. <page-number citation-index="1" label="224">*224</page-number>The defense also called witnesses who testified that petitioner was with them in a college lunchroom in another part of Chicago at the time the attack was committed.</p>
<p id="b396-5">The jury found petitioner guilty on all four counts, thus rejecting his theory and alibi. The trial court sentenced him to 30 to 50 years in prison. The Illinois Supreme Court affirmed. <em>People </em>v. <em>Moore, </em><span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/" aria-description="Citation for case: People v. Moore">51 Ill. 2d 79</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/" aria-description="Citation for case: People v. Moore">281 N. E. 2d 294</a></span> (1972). It rejected petitioner’s argument that the victim’s identification testimony should have been excluded, on the ground that the prosecution had shown an “independent basis” for the identification. <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#86" aria-description="Citation for case: People v. Moore"><em>Id., </em>at 86</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#298" aria-description="Citation for case: People v. Moore">281 N. E. 2d, at 298</a></span>. After this Court denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./409/979/">409 U. S. 979</a></span> (1972), petitioner sought a writ of habeas corpus from the Federal District Court. He contended that admission of the identification testimony at trial violated his Sixth and Fourteenth Amendment rights. Relying on the transcript from the state proceedings, the District Court denied the writ in an unpublished opinion, again on the ground that the prosecution had shown an independent basis for the identification. App. 31-35. The Court of Appeals for the Seventh Circuit affirmed in an unpublished opinion, <em>United States ex rel. Moore </em>v. <em>Illinois, </em><span class="citation" data-id="334955"><a href="/opinion/334955/u-s-ex-rel-moore-v-people-of-state-of-illinois/" aria-description="Citation for case: U. S. Ex Rel. Moore v. People of State of Illinois">534 F. 2d 331</a></span> (1976), and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./429/1061/">429 U. S. 1061</a></span> (1977).</p>
<p id="b396-6">II</p>
<p id="b396-7"><em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), held that a pretrial corporeal identification conducted after a suspect has been indicted is a critical stage in a criminal prosecution at which the Sixth Amendment entitles the accused to the presence of counsel. The Court emphasized the dangers inherent in a pretrial identification conducted in the absence of counsel. Persons who conduct the identification procedure may suggest, intentionally or unintentionally, that they expect the witness to identify the accused. Such a suggestion, coming Jrom a police officer or prosecutor, can lead a witness to make <page-number citation-index="1" label="225">*225</page-number>a mistaken identification. The witness then will be predisposed to adhere to this identification in subsequent testimony at trial. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 229, 235-236</a></span>. If an accused’s counsel is present at the pretrial identification, he can serve both his client’s and the prosecution’s interests by objecting to suggestive features of a procedure before they influence a witness’ identification. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 236, 238</a></span>. In view of the “variables and pitfalls” that exist at an uncounseled pretrial identification, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>id., </em>at 235</a></span>, the <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>Court reasoned:</p>
<blockquote id="b397-5">“[T]he first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused’s fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness — ‘that’s the man.’ ” <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 235-236</a></span>.</blockquote>
<p id="b397-6"><em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and its companion case, <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), also considered the admissibility of evidence derived from a corporeal identification conducted in violation of the accused’s right to counsel. In <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>, </em>witnesses to a robbery who had identified the defendant at an uncounseled pretrial lineup testified at trial on direct examination by the prosecution that he was the man who had committed the robbery. The prosecution did not elicit from the witnesses the fact that they had identified the defendant at the pretrial lineup. Nevertheless, because of the likelihood that the witnesses’ in-court identifications were based on their observations of the defendant at the uncounseled lineup rather than at the scene of the crime, the Court held that this testimony should have been excluded unless the prosecution could “establish by clear and convincing evidence that the in-court identifications <page-number citation-index="1" label="226">*226</page-number>were based upon observations of the suspect other than the lineup identification.” 388 U. S., at 240.<footnotemark>2</footnotemark></p>
<p id="b398-5"><em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>differed from <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>in one critical respect. In <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>the prosecution did elicit testimony in its case-in-chief that witnesses had identified the accused at an uncounseled pretrial lineup. The Court recognized that such testimony would “enhance the impact of [a witness’] in-court identification on the jury and seriously aggravate whatever derogation exists of the accused’s right to a fair trial.” 388 U. S., at 273-274. Because “[t]hat testimony [was] the direct result of the illegal lineup 'come at by exploitation of [the primary] illegality [,]’ <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>,” the prosecution was “not entitled to an opportunity to show that the testimony had an independent source.” <em>Id., </em>at 272-273; see also <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span> </em>at 240 n. 32. The Court announced this exclusionary rule in the belief that such a sanction is necessary “to assure that law enforcement authorities will respect the accused’s constitutional right to the presence of his counsel at the critical lineup.” <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><em>Gilbert, supra, </em>at 273</a></span>. The Court therefore reversed the conviction and remanded to the state court for a determination of whether admission of this evidence was harmless constitutional error under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#274" aria-description="Citation for case: Gilbert v. California">388 U. S., at 274</a></span>.</p>
<p id="b398-6">In <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), the plurality opinion made clear that the right to counsel announced in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>attaches only to corporeal identifications Conducted “at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.” <page-number citation-index="1" label="227">*227</page-number><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. This is so because the initiation of such proceedings “marks the commencement of the 'criminal prosecutions’ to which alone the explicit guarantees of the Sixth Amendment are applicable.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#690" aria-description="Citation for case: Kirby v. Illinois"><em>Id., </em>at 690</a></span>. Thus, in <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>the plurality held that the prosecution’s evidence of a robbery victim’s one-on-one stationhouse identification of an uncoun-seled suspect shortly after the suspect’s arrest was admissible because adversary judicial criminal proceedings had not yet been initiated. In such cases, however, due process protects the accused against the introduction of evidence of, or tainted by, unreliable pretrial identifications obtained through unnecessarily suggestive procedures. <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#690" aria-description="Citation for case: Kirby v. Illinois"><em>Id., </em>at 690-691</a></span>; <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972); <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967); see generally <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977).<footnotemark>3</footnotemark></p>
<p id="b399-5">III</p>
<p id="b399-6">In the instant case, petitioner argues that the preliminary hearing at which the victim identified him marked the initiation of adversary judicial criminal proceedings against him. Hence, under <em>Wade, Gilbert, </em>and <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>, </em>he was entitled to the presence of counsel at that confrontation. Moreover, the <page-number citation-index="1" label="228">*228</page-number>prosecution introduced evidence of this uncounseled corporeal identification at trial in its case-in-chief. Petitioner contends that under <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>, </em>this evidence should have been excluded without regard to whether there was an “independent source” for it.</p>
<p id="b400-5">The Court of Appeals took a different view of the case. It read <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>as holding that evidence of a corporeal identification conducted in the absence of defense counsel must be excluded only if the identification is made after the defendant is <em>indicted. </em>App. 45-46. Such a reading cannot be squared with <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>itself, which held that an accused’s rights under <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>attach to identifications conducted “at or after the initiation of adversary judicial criminal proceedings,” including proceedings instituted “by way of formal charge [or] preliminary hearing.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. The prosecution in this case was commenced under Illinois law when the victim’s complaint was filed in court. See Ill. Rev. Stat., ch. 38, § 111 (1975). The purpose of the preliminary hearing was to determine whether there was probable cause to bind petitioner over to the grand jury and to set bail. §§ 109-1, 109-3. Petitioner had the right to oppose the prosecution at that hearing by moving to dismiss the charges and to suppress the evidence against him. § 109-3 (e). He faced counsel for the State, who elicited the victim’s identification, summarized the State’s other evidence against petitioner, and urged that the State be given more time to marshal its evidence. It is plain that “the government ha[d] committed itself to prosecute,” and that petitioner found “himself faced with the prosecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois"><em>Kirby, supra, </em>at 689</a></span>. The State candidly concedes that this preliminary hearing. marked the “initiation of adversary judicial criminal proceedings” against petitioner, Brief for Respondent 8, and n. 1; Tr. of Oral Arg. 32, 34, and it hardly could contend otherwise. The Court of Appeals therefore erred in holding <page-number citation-index="1" label="229">*229</page-number>that petitioner’s rights under <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>had not yet attached at the time of the preliminary hearing.</p>
<p id="b401-5">The Court of Appeals also suggested that <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>did not apply here because the “in-court identification could hardly be considered a line-up.” App. 45. The meaning of this statement is not entirely clear. If the court meant that a one-on-one identification procedure, as distinguished from a lineup, is not subject to the counsel requirement, it was mistaken. Although <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>both involved lineups, <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>clearly contemplated that counsel would be required in both situations: “The pretrial confrontation for purpose of identification may take the form of a lineup ... or presentation of the suspect alone to the witness .... It is obvious that risks of suggestion attend either form of confrontation . . . .” 388 U. S., at 229; see also <em>id., </em>at 251 (White, J., dissenting in part and concurring in part); cf. <em>Stovall </em>v. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra;</a></span> Kirby </em>v. <em>Illinois. </em>Indeed, a one-on-one confrontation generally is thought to present greater risks of mistaken identification than a lineup. <em>E. g., </em>P. Wall, EyeWitness Identification in Criminal Cases 27-40 (1965); Williams &amp; Hammelmann, Identification Parades — I, Crim. L. Rev. 479, 480-481 (1963). There is no reason, then, to hold that a one-on-one identification procedure is not subject to the same requirements as a lineup.</p>
<p id="b401-6">If the court believed that petitioner did not have a right to counsel at this identification procedure because it was conducted in the course of a judicial proceeding, we do not agree. The reasons supporting Wade’s holding that a corporeal identification is a critical stage of a criminal prosecution for Sixth Amendment purposes apply with equal force to this identification. It is difficult to imagine a more suggestive manner in which to present a suspect to a witness for their critical first confrontation than was employed in this case. The victim, who had seen her assailant for only 10 to 15 seconds, was asked to make her identification after she was told that she <page-number citation-index="1" label="230">*230</page-number>was going to view a suspect, after she was told his name and heard it called as he was led before the bench, and after she heard the prosecutor recite the evidence believed to implicate petitioner.<footnotemark>4</footnotemark> Had petitioner been represented by counsel, some or all of this suggestiveness could have been avoided.<footnotemark>5</footnotemark></p>
<p id="b403-4"><page-number citation-index="1" label="231">*231</page-number>In sum, we are unpersuaded by the reasons advanced by -the Court of Appeals for distinguishing the identification procedure in this case from those considered in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>. </em>Here, as in those cases, petitioner’s Sixth Amendment rights were violated by a corporeal identification conducted after the initiation of adversary judicial criminal proceedings and in the absence of counsel. The courts below thought that the victim’s testimony at trial that she had identified petitioner at an uncounseled pretrial confrontation was admissible even if petitioner’s rights had been violated, because there was an “independent source” for the victim’s identification at the uncounseled confrontation. <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#86" aria-description="Citation for case: People v. Moore">51 Ill. 2d, at 86</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#298" aria-description="Citation for case: People v. Moore">281 N. E. 2d, at 298</a></span>; App. 35 (District Court), 45-46 (Court of Appeals).<footnotemark>6</footnotemark> But <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>held that the prosecution cannot buttress its case-in-chief by introducing evidence of a pretrial identification made in violation of the accused’s Sixth Amendment rights, even if it can prove that the pretrial identification had an independent source. “That testimony is the direct result of the illegal lineup 'come at by exploitation of [the primary] illegality,’ ” <em>Gilbert, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California">388 U. S., at 272-273</a></span>, and the prosecution is “therefore not entitled to an opportunity to show that the testimony had an independent source.” <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><em>Id., </em>at 273</a></span>. Because the prosecution made use of such testimony <page-number citation-index="1" label="232">*232</page-number>in this case, petitioner is entitled to the benefit of the strict rule of <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>.</em></p>
<p id="b404-5">IV</p>
<p id="b404-6">In view of the violation of petitioner’s Sixth and Fourteenth Amendment right to counsel at the pretrial corporeal identification, and of the prosecution’s exploitation at trial of evidence derived directly from that violation, we reverse the judgment of the Court of Appeals and remand for a determination of whether the failure to exclude that evidence was harmless constitutional error under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). See <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#274" aria-description="Citation for case: Gilbert v. California"><em>Gilbert, supra, </em>at 274</a></span>. That court also will be free on remand to re-examine the other issues presented by the petition, upon which we do not pass.<footnotemark>7</footnotemark></p>
<p id="b404-7">
<em>Reversed and remanded.</em>
</p>
<judges id="b404-8">Me. Justice Stevens took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b395-7"> Counsel for petitioner explicitly drew the court’s attention to our then recent decision in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967): “If we may look at the Wade case, Your Honor, it has as its holding, Your Honor, the requirement that a defendant have an attorney at an identification procedure . . . .” Trial Transcript 132.</p>
</footnote>
<footnote label="2">
<p id="b398-7"> Among the factors to be considered in making this determination are “the prior opportunity to observe the alleged criminal act, the existence of any discrepancy between any pre-lineup description and the defendant’s actual description, any identification prior to lineup of another person, the identification by picture of the defendant prior to the lineup, failure to identify the defendant on a prior occasion, and the lapse of time between the alleged act and the lineup identification.” 388 U. S., at 241.</p>
</footnote>
<footnote label="3">
<p id="b399-7"> In <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">413 U. S. 300</a></span> (1973), the Court held that the Sixth Amendment does not require that defense counsel be present when a witness views police or prosecution photographic arrays. . A photographic showing, unlike a corporeal identification, is not a “trial-like adversary confrontation” between an accused and agents of the government; hence, “no possibility arises that the accused might be misled by his lack of familiarity with the law or overpowered by his professional adversary.” <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#317" aria-description="Citation for case: United States v. Ash"><em>Id., </em>at 317</a></span>. Moreover, even without attending the prosecution’s photographic showing, defense counsel has an equal chance to prepare for trial by presenting his own photographic displays to witnesses before trial. But “[duplication by defense counsel is a safeguard that normally is not available when a formal confrontation occurs.” <em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">Id.,</a></span> </em>at 318 n. 10. An accused nevertheless is entitled to due process protection against the introduction of evidence of, or tainted by, unreliable identifications elicited through unnecessarily suggestive photographic displays. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#320" aria-description="Citation for case: United States v. Ash"><em>Id., </em>at 320</a></span>; <em>Manson </em>v. <em>Brathwaite; Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968).</p>
</footnote>
<footnote label="4">
<p id="b402-5"> Immediately before the State's Attorney asked the victim to identify petitioner, he stated:</p>
<p id="b402-6">“This is an allegation of rape and deviate sexual assault. It’s a home invasion of an apartment in Hyde Park and the victim was raped and forced to commit an oral copulation. Taken from her was a guitar and other instruments. When the defendant was arrested upon an arrest warrant signed by the Judge of the Court, the articles, the guitar and other instruments were found in the apartment, as were the clothes described of the man that attacked her that day.” App. 48-49.</p>
<p id="b402-7">It appears from the record that although a guitar and a flute were found in petitioner’s apartment when he was arrested, they were not the ones taken from the victim’s apartment and they were not introduced into evidence at petitioner’s trial. Transcript of Proceedings at Hearing of Feb. 5, 1968, p. 10; Trial Transcript 4A-45, 400-401. Neither was any clothing.</p>
</footnote>
<footnote label="5">
<p id="b402-8"> For example, counsel could have requested that the hearing be postponed until a lineup could be arranged at which the victim would view petitioner in a less suggestive setting. See, <em>e. g., United States </em>v. <em>Ravich, </em><span class="citation" data-id="288484"><a href="/opinion/288484/united-states-v-ronald-raymond-ravich-and-edward-mcconnell/#1202" aria-description="Citation for case: United States v. Ronald Raymond Ravich and Edward McConnell">421 F. 2d 1196, 1202-1203</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/834/">400 U. S. 834</a></span> (1970); <em>Mason </em>v. <em>United States, </em>134 U. S. App. D. C. 280, 283 n. 19, <span class="citation" data-id="286150"><a href="/opinion/286150/william-r-mason-v-united-states/" aria-description="Citation for case: William R. Mason v. United States">414 F. 2d 1176</a></span>, 1179 n. 19 (1969). Short of that, counsel could have asked that the victim be excused from the courtroom while the charges were read and the evidence against petitioner was recited, and that petitioner be seated with other people in the audience when the victim attempted an identification. See <em>Allen </em>v. <em>Rhay, </em><span class="citation" data-id="292225"><a href="/opinion/292225/gordon-m-allen-and-v-b-j-rhay-superintendent-of-the-washington-state/#1165" aria-description="Citation for case: Gordon M. Allen, and v. B. J. Rhay, Superintendent of the...">431 F. 2d 1160, 1165</a></span> (CA9 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/834/">404 U. S. 834</a></span> (1971). Counsel might have sought to cross-examine the victim to test her identification before it hardened. Cf. <em>Haberstroh </em>v. <em>Montanye, </em><span class="citation" data-id="317684"><a href="/opinion/317684/ralph-benno-haberstroh-v-superintendent-montanye-attica-correctional/#485" aria-description="Citation for case: Ralph Benno Haberstroh v. Superintendent Montanye, Attica...">493 F. 2d 483, 485</a></span> (CA2 1974); <em>United States ex rel. Riffert </em>v. <em>Rundle, </em><span class="citation" data-id="305033"><a href="/opinion/305033/united-states-of-america-ex-rel-james-r-riffert-v-alfred-t-rundle/#1351" aria-description="Citation for case: United States of America Ex Rel. James R. Riffert v....">464 F. 2d 1348, 1351</a></span> (CA3 1972), cert. denied <em>sub nom. Riffert </em>v. <em>Johnson, </em><span class="citation" data-id="8989309"><a href="/opinion/8996932/riffert-v-johnson/" aria-description="Citation for case: Riffert v. Johnson">415 U. S. 927</a></span> (1974). Because it is in the prosecution’s interest as well as the accused’s that witnesses’ identifications remain untainted, see <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#238" aria-description="Citation for case: United States v. Wade">388 U. S., at 238</a></span>, we cannot assume that such requests would have been in vain. Such requests ordinarily are addressed to the sound discretion of the court, see <em>United States </em>v. <span class="citation" data-id="288484"><a href="/opinion/288484/united-states-v-ronald-raymond-ravich-and-edward-mcconnell/#1203" aria-description="Citation for case: United States v. Ronald Raymond Ravich and Edward McConnell"><em>Ravich, supra, </em>at 1203</a></span>; we express no <page-number citation-index="1" label="231">*231</page-number>opinion as to whether the preliminary hearing court would have been required to grant any such requests.</p>
</footnote>
<footnote label="6">
<p id="b403-7"> The existence of an “independent source” was thought to be demonstrated by the victim’s selection of a picture of petitioner from the second photographic array. The courts below and the parties here have not been certain as to how many pictures the victim actually selected from that array. Although there is some ambiguity in the record, compare Trial Transcript 110-111, 113-114, 167, 290-292, 294, 307-308, 421, 454, with <em>id., </em>at 155-156, 158, 231-232, we think a fair reading indicates that the victim selected more than one photograph and that she did not make a positive identification of petitioner from them. But resolution of this factual issue is not necessary to our decision in this case.</p>
</footnote>
<footnote label="7">
<p id="b404-11"> In addition to his <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>argument, petitioner urges that the victim’s in-court identification was tainted by the prior uncounseled identification, see <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>; </em>that the in-court identification was the unreliable product of an unnecessarily suggestive identification procedure and should have been excluded under the Due Process Clause of the Fourteenth Amendment, see <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977); and that the trial court’s denial of a transcript of the preliminary hearing was prejudicial constitutional error, see <em>Roberts </em>v. <em>LaVallee, </em><span class="citation" data-id="9423508"><a href="/opinion/107527/roberts-v-lavallee/" aria-description="Citation for case: Roberts v. LaVallee">389 U. S. 40</a></span> (1967).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Moran v. Burbine.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Moran v. Burbine"
type: case
citation: "475 U.S. 412 (1986)"
parallel_cite: "106 S. Ct. 1135; 89 L. Ed. 2d 410; 54 U.S.L.W. 4265"
neutral_cite: 1986 U.S. LEXIS 32
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-03-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-03-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Moran v. Burbine
  varies_by_point: false
  scope_note: "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111614/moran-v-burbine/"
  cluster_id: 111614
  opinion_id: 111614
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[North Carolina v. Butler]]", "[[Edwards v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver"]
holding: "A Miranda waiver is valid even though police failed to tell the suspect that an attorney was trying to reach him; events outside the…"
lake:
  record_id: Moran v. Burbine
  status: verified
  projected_at: 2026-07-09
---

# Moran v. Burbine

*475 U.S. 412 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Burbine was arrested for a burglary; police then connected him to a murder. While he was in custody, his sister obtained a public defender, who telephoned the station and was told Burbine would not be questioned until the next day. Unaware of the call and never told of it, Burbine was given *[[Miranda v. Arizona|Miranda]]* warnings, waived his rights, and confessed to the murder.

## Issue
Whether a *[[Miranda v. Arizona|Miranda]]* waiver is invalid because police failed to inform the suspect that an attorney was trying to reach him, or because police misled the attorney about whether questioning would occur.

## Rule
No. A waiver is valid if it is voluntary, knowing, and intelligent, judged by a two-part inquiry: "First, the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it." — 475 U.S. at 421. ^pin-421

Information withheld from the suspect cannot bear on that inquiry: "Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right." — [*Id.* at 422](https://www.courtlistener.com/opinion/111614/moran-v-burbine/#:~:text=Events%20occurring%20outside%20of%20the). ^pin-422

## Application
Burbine's waiver was voluntary — there was no coercion — and knowing and intelligent, because he was repeatedly advised of and understood his rights. The police failure to tell him of the attorney's call, and any deception of the attorney, occurred outside his presence and were unknown to him, so they could not undermine his comprehension or the validity of his waiver. The Court also held that the Sixth Amendment had not attached because adversary judicial proceedings had not begun, and the police conduct did not violate due process on these facts. The confession was admissible.

## Conclusion
The waiver was valid and the confession admissible; the First Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Moran* supplies the canonical two-dimensional (voluntary + knowing/intelligent) standard for a valid *[[Miranda v. Arizona|Miranda]]* waiver, applied in cases such as [[North Carolina v. Butler]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Moran v. Burbine*, 475 U.S. 412 (1986) — https://www.courtlistener.com/opinion/111614/moran-v-burbine/ — pinpoints: 421, 422.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "31b4d5bbdb1056ea", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Moran v. Burbine"}, "payload": {"all": [{"cite": "475 U.S. 412", "page": "412", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "475"}, {"cite": "106 S. Ct. 1135", "page": "1135", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "89 L. Ed. 2d 410", "page": "410", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "1986 U.S. LEXIS 32", "page": "32", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "54 U.S.L.W. 4265", "page": "4265", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}], "display": "475 U.S. 412", "official": {"cite": "475 U.S. 412", "page": "412", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "475"}, "official_selection_present": true, "record_id": "Moran v. Burbine"}}
{"assertion_id": "0194f58f584f8a82", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-421", "record_id": "Moran v. Burbine"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-421", "pinpoint_status": "slip-only", "quote": "--- # Moran v. Burbine *475 U.S. 412 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Burbine was arrested for a burglary; police then connected him to a murder. While he was in custody, his sister obtained a public defender, who telephoned the station and was told Burbine would not be questioned until the next day. Unaware of the call and never told of it, Burbine was given *Miranda* warnings, waived his rights, and confessed to the murder. ## Issue Whether a *Miranda* waiver is invalid because police failed to inform the suspect that an attorney was trying to reach him, or because police misled the attorney about whether questioning would occur. ## Rule No. A waiver is valid if it is voluntary, knowing, and intelligent, judged by a two-part inquiry:", "quote_fidelity": "mismatch", "record_id": "Moran v. Burbine", "star_marker": null}}
{"assertion_id": "2e3b6c7f0d3fcd3d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-422", "record_id": "Moran v. Burbine"}, "payload": {"fragment": "#:~:text=Events%20occurring%20outside%20of%20the", "page": null, "pin_id": "pin-422", "pinpoint_status": "star-verified", "quote": "Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right.", "quote_fidelity": "matched", "record_id": "Moran v. Burbine", "star_marker": "422"}}
{"assertion_id": "5cf9cf80d0d4d195", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Moran v. Burbine"}, "payload": {"as_of_content": "1986-03-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Moran v. Burbine", "scope_note": "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment.", "varies_by_point": false}}
```

### lake record — Moran v. Burbine

```json
{
  "schema_version": "s2.v1",
  "record_id": "Moran v. Burbine",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Moran v. Burbine",
    "case_name_short": "Moran",
    "case_name_full": "Moran, Superintendent, Rhode Island Department of Corrections v. Burbine",
    "input_case_name": "Moran v. Burbine",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-03-10",
    "year": 1986,
    "docket": null,
    "cluster_id": 111614,
    "lead_opinion_id": 111614,
    "sibling_ids": [
      111614,
      9842071,
      9842072
    ],
    "absolute_url": "/opinion/111614/moran-v-burbine/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 412",
      "volume": "475",
      "reporter": "U.S.",
      "page": "412",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 1135",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 410",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4265",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4265",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 32",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "32",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 412",
        "volume": "475",
        "reporter": "U.S.",
        "page": "412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 1135",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "1135",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 410",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 32",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "32",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4265",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4265",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 412",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 412",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-421",
      "page": null,
      "quote": "--- # Moran v. Burbine *475 U.S. 412 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Burbine was arrested for a burglary; police then connected him to a murder. While he was in custody, his sister obtained a public defender, who telephoned the station and was told Burbine would not be questioned until the next day. Unaware of the call and never told of it, Burbine was given *Miranda* warnings, waived his rights, and confessed to the murder. ## Issue Whether a *Miranda* waiver is invalid because police failed to inform the suspect that an attorney was trying to reach him, or because police misled the attorney about whether questioning would occur. ## Rule No. A waiver is valid if it is voluntary, knowing, and intelligent, judged by a two-part inquiry:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-422",
      "page": null,
      "quote": "Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right.",
      "star_marker": "422",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 20840,
      "fragment": "#:~:text=Events%20occurring%20outside%20of%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-03-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Moran v. Burbine",
    "varies_by_point": false,
    "scope_note": "Canonical statement of the two-dimensional Miranda-waiver standard; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9352546,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9329344,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 8465498,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 10018645,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 4731163,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane1_negative"
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
        "journal_ref": "Moran v. Burbine:lane1_negative"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. Marsh",
          "cluster_id": 111865,
          "cite": [
            "95 L. Ed. 2d 176",
            "107 S. Ct. 1702",
            "481 U.S. 200",
            "1987 U.S. LEXIS 1812",
            "55 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "in Int. of B.H",
          "cluster_id": 4889275,
          "cite": [
            "2021 CO 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Murray",
          "cluster_id": 111728,
          "cite": [
            "91 L. Ed. 2d 434",
            "106 S. Ct. 2661",
            "477 U.S. 527",
            "1986 U.S. LEXIS 67",
            "54 U.S.L.W. 4833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heitman v. State",
          "cluster_id": 2461257,
          "cite": [
            "815 S.W.2d 681",
            "60 U.S.L.W. 2074",
            "1991 Tex. Crim. App. LEXIS 160",
            "1991 WL 111761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Male Juvenile (95-Cr-1074)",
          "cluster_id": 744606,
          "cite": [
            "121 F.3d 34",
            "1997 U.S. App. LEXIS 19219",
            "1997 WL 416548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richardson v. State",
          "cluster_id": 853754,
          "cite": [
            "717 N.E.2d 32",
            "1999 Ind. LEXIS 918",
            "1999 WL 784001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
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
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Maryland",
          "cluster_id": 118184,
          "cite": [
            "140 L. Ed. 2d 294",
            "118 S. Ct. 1151",
            "523 U.S. 185",
            "1998 U.S. LEXIS 1605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Penry v. State",
          "cluster_id": 2372264,
          "cite": [
            "903 S.W.2d 715",
            "1995 WL 68622"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beverly A. Seymour v. Diane Walker,respondent-Appellee",
          "cluster_id": 770145,
          "cite": [
            "224 F.3d 542",
            "2000 U.S. App. LEXIS 20170",
            "2000 WL 1154017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. District Court in & for First Judicial District, Jefferson County",
          "cluster_id": 1138536,
          "cite": [
            "785 P.2d 141",
            "14 Brief Times Rptr. 75",
            "1990 Colo. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Moran v. Burbine:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111614 OR 9842071 OR 9842072) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTYyMjg0ODAwMDAwJnM9NDYzNzA0NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111614+OR+9842071+OR+9842072%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111614 OR 9842071 OR 9842072)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NTMmcz0xNDU2MjgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111614+OR+9842071+OR+9842072%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111614 OR 9842071 OR 9842072)",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 0,
        "triage_snippet_classified": 109
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111614 OR 9842071 OR 9842072)",
    "indexed_citing_opinions": 1991,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111614,
        "count": 1730,
        "count_source": "search"
      },
      {
        "opinion_id": 9842071,
        "count": 297,
        "count_source": "search"
      },
      {
        "opinion_id": 9842072,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3340,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/moran-v-burbine.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjk1Mzcmcz0xMDU5Njc4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111614+OR+9842071+OR+9842072%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111614,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 107978,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108613,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 109825,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 111553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 303738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 436102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 446925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1169436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1174756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1320570,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1345918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1467753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1525657,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1688778,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1715629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1843028,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1847051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1869337,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1955294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 1996598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2055814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2238115,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2267415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2314564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111614,
        "cited_id": 2499246,
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
    "date_created": "2026-07-05T14:39:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:43:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:39:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Moran v. Burbine (truncated)

```
<div>
<center><b><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">475 U.S. 412</a></span> (1986)</b></center>
<center><h1>MORAN, SUPERINTENDENT, RHODE ISLAND DEPARTMENT OF CORRECTIONS<br>
v.<br>
BURBINE</h1></center>
<center>No. 84-1485.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 13, 1985</center>
<center>Decided March 10, 1986</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIRST CIRCUIT
<p><span class="star-pagination">*414</span> <i>Constance L. Messore,</i> Special Assistant Attorney General of Rhode Island, argued the cause for petitioner. With her on the briefs was <i>Arlene Violet,</i> Attorney General.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Acting Solicitor General Fried, Assistant Attorney General Trott, Andrew J. Pincus,</i> and <i>Sara Criscitelli.</i></p>
<p><i>Robert B. Mann</i> argued the cause for respondent. With him on the brief was <i>William F. Reilly.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*415</span> JUSTICE O'CONNOR delivered the opinion of the Court.</p>
<p>After being informed of his rights pursuant to <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and after executing a series of written waivers, respondent confessed to the murder of a young woman. At no point during the course of the interrogation, which occurred prior to arraignment, did he request an attorney. While he was in police custody, his sister attempted to retain a lawyer to represent him. The attorney telephoned the police station and received assurances that respondent would not be questioned further until the next day. In fact, the interrogation session that yielded the inculpatory statements began later that evening. The question presented is whether either the conduct of the police or respondent's <span class="star-pagination">*416</span> ignorance of the attorney's efforts to reach him taints the validity of the waivers and therefore requires exclusion of the confessions.</p>
<p></p>
<h2>I</h2> <p>On the morning of March 3, 1977, Mary Jo Hickey was found unconscious in a factory parking lot in Providence, Rhode Island. Suffering from injuries to her skull apparently inflicted by a metal pipe found at the scene, she was rushed to a nearby hospital. Three weeks later she died from her wounds.</p>
<p>Several months after her death, the Cranston, Rhode Island, police arrested respondent and two others in connection with a local burglary. Shortly before the arrest, Detective Ferranti of the Cranston police force had learned from a confidential informant that the man responsible for Ms. Hickey's death lived at a certain address and went by the name of "Butch." Upon discovering that respondent lived at that address and was known by that name, Detective Ferranti informed respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. When respondent refused to execute a written waiver, Detective Ferranti spoke separately with the two other suspects arrested on the breaking and entering charge and obtained statements further implicating respondent in Ms. Hickey's murder. At approximately 6 p.m., Detective Ferranti telephoned the police in Providence to convey the information he had uncovered. An hour later, three officers from that department arrived at the Cranston headquarters for the purpose of questioning respondent about the murder.</p>
<p>That same evening, at about 7:45 p.m., respondent's sister telephoned the Public Defender's Office to obtain legal assistance for her brother. Her sole concern was the breaking and entering charge, as she was unaware that respondent was then under suspicion for murder. She asked for Richard Casparian who had been scheduled to meet with respondent earlier that afternoon to discuss another charge unrelated to either the break-in or the murder. As soon as the conversation <span class="star-pagination">*417</span> ended, the attorney who took the call attempted to reach Mr. Casparian. When those efforts were unsuccessful, she telephoned Allegra Munson, another Assistant Public Defender, and told her about respondent's arrest and his sister's subsequent request that the office represent him.</p>
<p>At 8:15 p.m., Ms. Munson telephoned the Cranston police station and asked that her call be transferred to the detective division. In the words of the Supreme Court of Rhode Island, whose factual findings we treat as presumptively correct, <span class="citation no-link">28 U. S. C. § 2254</span>(d), the conversation proceeded as follows:</p>
<blockquote>"A male voice responded with the word `Detectives.' Ms. Munson identified herself and asked if Brian Burbine was being held; the person responded affirmatively. Ms. Munson explained to the person that Burbine was represented by attorney Casparian who was not available; she further stated that she would act as Burbine's legal counsel in the event that the police intended to place him in a lineup or question him. The unidentified person told Ms. Munson that the police would not be questioning Burbine or putting him in a lineup and that they were through with him for the night. Ms. Munson was not informed that the Providence Police were at the Cranston police station or that Burbine was a suspect in Mary's murder." <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#23" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 23-24</a></span> (1982).</blockquote>
<p>At all relevant times, respondent was unaware of his sister's efforts to retain counsel and of the fact and contents of Ms. Munson's telephone conversation.</p>
<p>Less than an hour later, the police brought respondent to an interrogation room and conducted the first of a series of interviews concerning the murder. Prior to each session, respondent was informed of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and on three separate occasions he signed a written form acknowledging that he understood his right to the presence of an attorney and explicitly indicating that he "[did] not want an attorney <span class="star-pagination">*418</span> called or appointed for [him]" before he gave a statement. App. to Pet. for Cert. 94, 103, 107. Uncontradicted evidence at the suppression hearing indicated that at least twice during the course of the evening, respondent was left in a room where he had access to a telephone, which he apparently declined to use. Tr. of Suppression Hearing 23, 85. Eventually, respondent signed three written statements fully admitting to the murder.</p>
<p>Prior to trial, respondent moved to suppress the statements. The court denied the motion, finding that respondent had received the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and had "knowingly, intelligently, and voluntarily waived his privilege against self-incrimination [and] his right to counsel." App. to Pet. for Cert. 116. Rejecting the contrary testimony of the police, the court found that Ms. Munson did telephone the detective bureau on the evening in question, but concluded that "there was no . . . conspiracy or collusion on the part of the Cranston Police Department to secrete this defendant from his attorney." <i>Id.,</i> at 114. In any event, the court held, the constitutional right to request the presence of an attorney belongs solely to the defendant and may not be asserted by his lawyer. Because the evidence was clear that respondent never asked for the services of an attorney, the telephone call had no relevance to the validity of the waiver or the admissibility of the statements.</p>
<p>The jury found respondent guilty of murder in the first degree, and he appealed to the Supreme Court of Rhode Island. A divided court rejected his contention that the Fifth and Fourteenth Amendments to the Constitution required the suppression of the inculpatory statements and affirmed the conviction. Failure to inform respondent of Ms. Munson's efforts to represent him, the court held, did not undermine the validity of the waivers. "It hardly seems conceivable that the additional information that an attorney whom he did not know had called the police station would have added significantly to the quantum of information necessary for the <span class="star-pagination">*419</span> accused to make an informed decision as to waiver." <i>State</i> v. <i>Burbine</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#29" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 29</a></span> (1982). Nor, the court concluded, did <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> or any other decision of this Court independently require the police to honor Ms. Munson's request that interrogation not proceed in her absence. In reaching that conclusion, the court noted that because two different police departments were operating in the Cranston station house on the evening in question, the record supported the trial court's finding that there was no "conspiracy or collusion" to prevent Ms. Munson from seeing respondent. <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#30" aria-description="Citation for case: State v. Burbine">451 A. 2d, at 30, n. 5</a></span>. In any case, the court held, the right to the presence of counsel belongs solely to the accused and may not be asserted by "benign third parties, whether or not they happen to be attorneys." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#28" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 28</a></span>.</p>
<p>After unsuccessfully petitioning the United States District Court for the District of Rhode Island for a writ of habeas corpus, <span class="citation" data-id="1869337"><a href="/opinion/1869337/burbine-v-moran/" aria-description="Citation for case: Burbine v. Moran">589 F. Supp. 1245</a></span> (1984), respondent appealed to the Court of Appeals for the First Circuit. That court reversed. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d 178</a></span> (1985). Finding it unnecessary to reach any arguments under the Sixth and Fourteenth Amendments, the court held that the police's conduct had fatally tainted respondent's "otherwise valid" waiver of his Fifth Amendment privilege against self-incrimination and right to counsel. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#184" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 184</a></span>. The court reasoned that by failing to inform respondent that an attorney had called and that she had been assured that no questioning would take place until the next day, the police had deprived respondent of information crucial to his ability to waive his rights knowingly and intelligently. The court also found that the record would support "no other explanation for the refusal to tell Burbine of Attorney Munson's call than . . . deliberate or reckless irresponsibility." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 185</a></span>. This kind of "blameworthy action by the police," the court concluded, together with respondent's ignorance of the telephone call, "vitiate[d] any claim that [the] waiver of counsel was knowing and voluntary." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 185, 187</a></span>.</p>
<p><span class="star-pagination">*420</span> We granted certiorari to decide whether a prearraignment confession preceded by an otherwise valid waiver must be suppressed either because the police misinformed an inquiring attorney about their plans concerning the suspect or because they failed to inform the suspect of the attorney's efforts to reach him. <span class="citation multiple-matches"><a href="/c/U.%20S./471/1098/">471 U. S. 1098</a></span> (1985). We now reverse.</p>
<p></p>
<h2>II</h2>
<p>In <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> the Court recognized that custodial interrogations, by their very nature, generate "compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. To combat this inherent compulsion, and thereby protect the Fifth Amendment privilege against self-incrimination, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposed on the police an obligation to follow certain procedures in their dealings with the accused. In particular, prior to the initiation of questioning, they must fully apprise the suspect of the State's intention to use his statements to secure a conviction, and must inform him of his rights to remain silent and to "have counsel present . . . if [he] so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 468-470</a></span>. Beyond this duty to inform, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires that the police respect the accused's decision to exercise the rights outlined in the warnings. "If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, [or if he] states that he wants an attorney, the interrogation must cease." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 473-474</a></span>. See also <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981).</p>
<p>Respondent does not dispute that the Providence police followed these procedures with precision. The record amply supports the state-court findings that the police administered the required warnings, sought to assure that respondent understood his rights, and obtained an express written waiver prior to eliciting each of the three statements. Nor does respondent contest the Rhode Island courts' determination that he at no point requested the presence of a lawyer. <span class="star-pagination">*421</span> He contends instead that the confessions must be suppressed because the police's failure to inform him of the attorney's telephone call deprived him of information essential to his ability to knowingly waive his Fifth Amendment rights. In the alternative, he suggests that to fully protect the Fifth Amendment values served by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we should extend that decision to condemn the conduct of the Providence police. We address each contention in turn.</p>
<p></p>
<h2>A</h2>
<p>Echoing the standard first articulated in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938), <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holds that "[t]he defendant may waive effectuation" of the rights conveyed in the warnings "provided the waiver is made voluntarily, knowingly and intelligently." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444, 475</a></span>. The inquiry has two distinct dimensions. <i>Edwards</i> v. <i>Arizona, supra,</i> at 482; <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 404</a></span> (1977). First, the relinquishment of the right must have been voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception. Second, the waiver must have been made with a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it. Only if the "totality of the circumstances surrounding the interrogation" reveals both an uncoerced choice and the requisite level of comprehension may a court properly conclude that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights have been waived. <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#725" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 725</a></span> (1979). See also <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 374-375</a></span> (1979).</p>
<p>Under this standard, we have no doubt that respondent validly waived his right to remain silent and to the presence of counsel. The voluntariness of the waiver is not at issue. As the Court of Appeals correctly acknowledged, the record is devoid of any suggestion that police resorted to physical or psychological pressure to elicit the statements. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#184" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 184</a></span>. Indeed it appears that it was respondent, and not the <span class="star-pagination">*422</span> police, who spontaneously initiated the conversation that led to the first and most damaging confession. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#180" aria-description="Citation for case: Brian K. Burbine v. John Moran"><i>Id.,</i> at 180</a></span>. Cf. <i>Edwards</i> v. <i>Arizona, supra</i><i>.</i> Nor is there any question about respondent's comprehension of the full panoply of rights set out in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and of the potential consequences of a decision to relinquish them. Nonetheless, the Court of Appeals believed that the "[d]eliberate or reckless" conduct of the police, in particular their failure to inform respondent of the telephone call, fatally undermined the validity of the otherwise proper waiver. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#187" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 187</a></span>. We find this conclusion untenable as a matter of both logic and precedent.</p>
<p>Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right. Under the analysis of the Court of Appeals, the same defendant, armed with the same information and confronted with precisely the same police conduct, would have knowingly waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights had a lawyer not telephoned the police station to inquire about his status. Nothing in any of our waiver decisions or in our understanding of the essential components of a valid waiver requires so incongruous a result. No doubt the additional information would have been useful to respondent; perhaps even it might have affected his decision to confess. But we have never read the Constitution to require that the police supply a suspect with a flow of information to help him calibrate his self-interest in deciding whether to speak or stand by his rights. See, <i>e. g., </i><i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316-317</a></span> (1985); <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). Cf. <i>Hill</i> v. <i>Lockhart,</i> <span class="citation" data-id="9430227"><a href="/opinion/111539/hill-v-lockhart/#56" aria-description="Citation for case: Hill v. Lockhart">474 U. S. 52, 56</a></span> (1985); <i>McMann</i> v. <i>Richardson,</i> <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#769" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 769</a></span> (1970). Once it is determined that a suspect's decision not to rely on his rights was uncoerced, that he at all times knew he could stand mute and request a lawyer, and that he was aware of the State's intention to use his statements to secure a conviction, the analysis <span class="star-pagination">*423</span> is complete and the waiver is valid as a matter of law.<sup>[1]</sup> The Court of Appeals' conclusion to the contrary was in error.</p>
<p>Nor do we believe that the level of the police's culpability in failing to inform respondent of the telephone call has any bearing on the validity of the waivers. In light of the state-court findings that there was no "conspiracy or collusion" on the part of the police, <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#30" aria-description="Citation for case: State v. Burbine">451 A. 2d, at 30, n. 5</a></span>, we have serious doubts about whether the Court of Appeals was free to conclude that their conduct constituted "deliberate or reckless irresponsibility." <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 185</a></span>; see <span class="citation no-link">28 U. S. C. § 2254</span>(d). But whether intentional or inadvertent, the state of mind of the police is irrelevant to the question of the intelligence and voluntariness of respondent's election to abandon his rights. Although highly inappropriate, even deliberate deception of an attorney could not possibly affect a suspect's decision to waive his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights unless he were at least aware of the incident. Compare <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#481" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478, 481</a></span> (1964) (excluding confession where police incorrectly told the <i>suspect</i> that his lawyer " `didn't want to see' him"). Nor was the failure to inform respondent of the telephone call the kind of "trick[ery]" that can vitiate the validity of a waiver. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span>. Granting that the "deliberate or reckless" withholding of information is objectionable as a <span class="star-pagination">*424</span> matter of ethics, such conduct is only relevant to the constitutional validity of a waiver if it deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them. Because respondent's voluntary decision to speak was made with full awareness and comprehension of all the information <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires the police to convey, the waivers were valid.</p>
<p></p>
<h2>B</h2>
<p>At oral argument respondent acknowledged that a constitutional rule requiring the police to inform a suspect of an attorney's efforts to reach him would represent a significant extension of our precedents. Tr. of Oral Arg. 32-33. He contends, however, that the conduct of the Providence police was so inimical to the Fifth Amendment values <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> seeks to protect that we should read that decision to condemn their behavior. Regardless of any issue of waiver, he urges, the Fifth Amendment requires the reversal of a conviction if the police are less than forthright in their dealings with an attorney or if they fail to tell a suspect of a lawyer's unilateral efforts to contact him. Because the proposed modification ignores the underlying purposes of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules and because we think that the decision as written strikes the proper balance between society's legitimate law enforcement interests and the protection of the defendant's Fifth Amendment rights, we decline the invitation to further extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s reach.</p>
<p>At the outset, while we share respondent's distaste for the deliberate misleading of an officer of the court, reading <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to forbid police deception of an <i>attorney</i> "would cut [the decision] completely loose from its own explicitly stated rationale." <i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). As is now well established, "[t]he . . . <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are `not themselves rights protected by the Constitution but [are] instead measures to insure that the [suspect's] right against compulsory self-incrimination [is] protected.' " <span class="star-pagination">*425</span> <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984), quoting <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974). Their objective is not to mold police conduct for its own sake. Nothing in the Constitution vests in us the authority to mandate a code of behavior for state officials wholly unconnected to any federal right or privilege. The purpose of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings instead is to dissipate the compulsion inherent in custodial interrogation and, in so doing, guard against abridgment of the suspect's Fifth Amendment rights. Clearly, a rule that focuses on how the police treat an attorney  conduct that has no relevance at all to the degree of compulsion experienced by the defendant during interrogation  would ignore both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s mission and its only source of legitimacy.</p>
<p>Nor are we prepared to adopt a rule requiring that the police inform a suspect of an attorney's efforts to reach him. While such a rule might add marginally to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s goal of dispelling the compulsion inherent in custodial interrogation, overriding practical considerations counsel against its adoption. As we have stressed on numerous occasions, "[o]ne of the principal advantages" of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is the ease and clarity of its application. <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984); see also <i>New York</i> v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#662" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 662-664</a></span> (concurring opinion); <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 718</a></span>. We have little doubt that the approach urged by respondent and endorsed by the Court of Appeals would have the inevitable consequence of muddying <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s otherwise relatively clear waters. The legal questions it would spawn are legion: To what extent should the police be held accountable for knowing that the accused has counsel? Is it enough that someone in the station house knows, or must the interrogating officer himself know of counsel's efforts to contact the suspect? Do counsel's efforts to talk to the suspect concerning one criminal investigation trigger the obligation to inform the defendant before interrogation may proceed on a wholly separate matter? We are unwilling to modify <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in a <span class="star-pagination">*426</span> manner that would so clearly undermine the decision's central "virtue of informing police and prosecutors with specificity. . . what they may do in conducting [a] custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible." <i>Fare</i> v. <i>Michael C., supra,</i> at 718.</p>
<p>Moreover, problems of clarity to one side, reading <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to require the police in each instance to inform a suspect of an attorney's efforts to reach him would work a substantial and, we think, inappropriate shift in the subtle balance struck in that decision. Custodial interrogations implicate two competing concerns. On the one hand, "the need for police questioning as a tool for effective enforcement of criminal laws" cannot be doubted. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225</a></span> (1973). Admissions of guilt are more than merely "desirable," <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#186" aria-description="Citation for case: United States v. Washington">431 U. S., at 186</a></span>; they are essential to society's compelling interest in finding, convicting, and punishing those who violate the law. On the other hand, the Court has recognized that the interrogation process is "inherently coercive" and that, as a consequence, there exists a substantial risk that the police will inadvertently traverse the fine line between legitimate efforts to elicit admissions and constitutionally impermissible compulsion. <i>New York</i> v. <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#656" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 656</a></span>. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> attempted to reconcile these opposing concerns by giving the <i>defendant</i> the power to exert some control over the course of the interrogation. Declining to adopt the more extreme position that the actual presence of a lawyer was necessary to dispel the coercion inherent in custodial interrogation, see Brief for American Civil Liberties Union as <i>Amicus Curiae</i> in <i>Miranda</i> v. <i>Arizona</i><i>,</i> O. T. 1965, No. 759, pp. 22-31, the Court found that the suspect's Fifth Amendment rights could be adequately protected by less intrusive means. Police questioning, often an essential part of the investigatory process, could continue in its traditional form, the Court held, but only if the suspect clearly understood <span class="star-pagination">*427</span> that, at any time, he could bring the proceeding to a halt or, short of that, call in an attorney to give advice and monitor the conduct of his interrogators.</p>
<p>The position urged by respondent would upset this carefully drawn approach in a manner that is both unnecessary for the protection of the Fifth Amendment privilege and injurious to legitimate law enforcement. Because, as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holds, full comprehension of the rights to remain silent and request an attorney are sufficient to dispel whatever coercion is inherent in the interrogation process, a rule requiring the police to inform the suspect of an attorney's efforts to contact him would contribute to the protection of the Fifth Amendment privilege only incidentally, if at all. This minimal benefit, however, would come at a substantial cost to society's legitimate and substantial interest in securing admissions of guilt. Indeed, the very premise of the Court of Appeals was not that awareness of Ms. Munson's phone call would have dissipated the coercion of the interrogation room, but that it might have convinced respondent not to speak at all. <span class="citation" data-id="446925"><a href="/opinion/446925/brian-k-burbine-v-john-moran/#185" aria-description="Citation for case: Brian K. Burbine v. John Moran">753 F. 2d, at 185</a></span>. Because neither the letter nor purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> require this additional handicap on otherwise permissible investigatory efforts, we are unwilling to expand the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules to require the police to keep the suspect abreast of the status of his legal representation.</p>
<p>We acknowledge that a number of state courts have reached a contrary conclusion. Compare <i>State</i> v. <i>Jones,</i> <span class="citation" data-id="1174756"><a href="/opinion/1174756/state-v-jones/" aria-description="Citation for case: State v. Jones">19 Wash. App. 850</a></span>, <span class="citation" data-id="1174756"><a href="/opinion/1174756/state-v-jones/" aria-description="Citation for case: State v. Jones">578 P. 2d 71</a></span> (1978), with <i>State</i> v. <i>Beck,</i> <span class="citation" data-id="9647546"><a href="/opinion/1525657/state-v-beck/" aria-description="Citation for case: State v. Beck">687 S. W. 2d 155</a></span> (Mo. 1985) (en banc). We recognize also that our interpretation of the Federal Constitution, if given the dissent's expansive gloss, is at odds with the policy recommendations embodied in the American Bar Association Standards of Criminal Justice. Cf. ABA Standards for Criminal Justice 5-7.1 (2d ed. 1980). Notwithstanding the dissent's protestations, however, our interpretive duties go well beyond deferring to the numerical preponderance of lower court decisions or to the subconstitutional recommendations <span class="star-pagination">*428</span> of even so esteemed a body as the American Bar Association. See <i>Nix</i> v. <i>Whiteside, ante,</i> at 189 (BLACKMUN, J., concurring in judgment). Nothing we say today disables the States from adopting different requirements for the conduct of its employees and officials as a matter of state law. We hold only that the Court of Appeals erred in construing the Fifth Amendment to the Federal Constitution to require the exclusion of respondent's three confessions.</p>
<p></p>
<h2>III</h2>
<p>Respondent also contends that the Sixth Amendment requires exclusion of his three confessions.<sup>[2]</sup> It is clear, of course, that, absent a valid waiver, the defendant has the right to the presence of an attorney during any interrogation occurring after the first formal charging proceeding, the point at which the Sixth Amendment right to counsel initially attaches. <i>United States</i> v. <i>Gouveia,</i> <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#187" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 187</a></span> (1984); <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972) (opinion of Stewart, J.). See <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#400" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 400-401</a></span>. And we readily agree that once the right <i>has</i> attached, it follows that the police may not interfere with the efforts of a defendant's attorney to act as a " `medium' between [the suspect] and the State" during the interrogation. <i>Maine</i> v. <i>Moulton,</i> <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 176</a></span> (1985); see <i>Brewer</i> v. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#401" aria-description="Citation for case: Brewer v. Williams"><i>Williams, supra,</i> at 401, n. 8</a></span>. The difficulty for respondent is that the interrogation sessions that yielded the inculpatory statements took place <i>before</i> the initiation of "adversary judicial proceedings." <i>United States</i> v. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#192" aria-description="Citation for case: United States v. Gouveia"><i>Gouveia, supra,</i> at 192</a></span>. He contends, however, that this circumstance is not fatal to his Sixth Amendment claim. At least in some situations, he argues, the Sixth Amendment protects the integrity of the <span class="star-pagination">*429</span> attorney-client relationship<sup>[3]</sup> regardless of whether the prosecution has in fact commenced "by way of formal charge, preliminary hearing, indictment, information or arraignment." 467 U. S., at 188. Placing principal reliance on a footnote in <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#465" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 465, n. 35</a></span>, and on <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), he maintains that <i>Gouveia, Kirby,</i> and our other "critical stage" cases, concern only the narrow question of when the right <i>to</i> counsel  that is, to the appointment or presence of counsel  attaches. The right to non-interference with an attorney's dealings with a criminal suspect, he asserts, arises the moment that the relationship is formed, or, at the very least, once the defendant is placed in custodial interrogation.</p>
<p>We are not persuaded. At the outset, subsequent decisions foreclose any reliance on <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> and <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for the proposition that the Sixth Amendment right, in any of its manifestations, applies prior to the initiation of adversary judicial proceedings. Although <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was originally decided as a Sixth Amendment case, "the Court in retrospect perceived that the `prime purpose' of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> was not to vindicate the constitutional right to counsel as such, but, like <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> `to guarantee full effectuation of the privilege against self-incrimination . . . .' " <i>Kirby</i> v. <i>Illinois, supra,</i> <span class="star-pagination">*430</span> at 689, quoting <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#729" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 729</a></span> (1966). Clearly then, <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> provides no support for respondent's argument. Nor, of course, does <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the holding of which rested exclusively on the Fifth Amendment. Thus, the decision's brief observation about the reach of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i>'s Sixth Amendment analysis is not only dictum, but reflects an understanding of the case that the Court has expressly disavowed. See also, <i>United States</i> v. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia"><i>Gouveia, supra,</i> at 188, n. 5</a></span>; Y. Kamisar, Police Interrogation and Confessions 217-218, n. 94 (1980).</p>
<p>Questions of precedent to one side, we find respondent's understanding of the Sixth Amendment both practically and theoretically unsound. As a practical matter, it makes little sense to say that the Sixth Amendment right to counsel attaches at different times depending on the fortuity of whether the suspect or his family happens to have retained counsel prior to interrogation. Cf. <span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#220" aria-description="Citation for case: United States v. Gouveia"><i>id.,</i> at 220-221</a></span>. More importantly, the suggestion that the existence of an attorney-client relationship itself triggers the protections of the Sixth Amendment misconceives the underlying purposes of the right to counsel. The Sixth Amendment's intended function is not to wrap a protective cloak around the attorney-client relationship for its own sake any more than it is to protect a suspect from the consequences of his own candor. Its purpose, rather, is to assure that in any "criminal prosecutio[n]," U. S. Const., Amdt. 6, the accused shall not be left to his own devices in facing the " `prosecutorial forces of organized society.' " <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton, supra,</a></span></i> at 170 (quoting <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>). By its very terms, it becomes applicable only when the government's role shifts from investigation to accusation. For it is only then that the assistance of one versed in the "intricacies . . . of law," <i>ibid.,</i> is needed to assure that the prosecution's case encounters "the crucible of meaningful adversarial testing." <i>United States</i> v. <i>Cronic,</i> <span class="citation" data-id="111169"><a href="/opinion/111169/united-states-v-cronic/#656" aria-description="Citation for case: United States v. Cronic">466 U. S. 648, 656</a></span> (1984).</p>
<p><span class="star-pagination">*431</span> Indeed, in <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span></i><i>,</i> decided this Term, the Court again confirmed that looking to the initiation of adversary judicial proceedings, far from being mere formalism, is fundamental to the proper application of the Sixth Amendment right to counsel. There, we considered the constitutional implications of a surreptitious investigation that yielded evidence pertaining to two crimes. For one, the defendant had been indicated; for the other, he had not. Concerning the former, the Court reaffirmed that after the first charging proceeding the government may not deliberately elicit incriminating statements from an accused out of the presence of counsel. See also <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). The Court made clear, however, that the evidence concerning the crime for which the defendant had not been indicted  evidence obtained in precisely the same manner from the identical suspect  would be admissible at a trial limited to those charges. <i>Maine</i> v. <i>Moulton,</i> <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#180" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 180</a></span>, and n. 16. The clear implication of the holding, and one that confirms the teaching of <i><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia</a></span>,</i> is that the Sixth Amendment right to counsel does not attach until after the initiation of formal charges. Moreover, because Moulton already had legal representation, the decision all but forecloses respondent's argument that the attorney-client relationship itself triggers the Sixth Amendment right.</p>
<p>Respondent contends, however, that custodial interrogations require a different rule. Because confessions elicited during the course of police questioning often seal a suspect's fate, he argues, the need for an advocate  and the concomitant right to noninterference with the attorney-client relationship  is at its zenith, regardless of whether the State has initiated the first adversary judicial proceeding. We do not doubt that a lawyer's presence could be of value to the suspect; and we readily agree that if a suspect confesses, his attorney's case at trial will be that much more difficult. But these concerns are no more decisive in this context than they were for the equally damaging preindictment lineup <span class="star-pagination">*432</span> at issue in <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>,</i> or the statements pertaining to the unindicted crime elicted from the defendant in <i>Maine</i> v. <i><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/" aria-description="Citation for case: Maine v. Moulton">Moulton</a></span></i><i>.</i> Compare <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#226" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 226-227</a></span> (1967) (Sixth Amendment attaches at postindictment lineup); <i>Massiah</i> v. <i>United States, supra</i> (after indictment, police may not elicit statements from suspect out of the presence of counsel). For an interrogation, no more or less than for any other "critical" pretrial event, the possibility that the encounter may have important consequences at trial, standing alone, is insufficient to trigger the Sixth Amendment right to counsel. As <i><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/" aria-description="Citation for case: United States v. Gouveia">Gouveia</a></span></i> made clear, until such time as the " `government has committed itself to prosecute, and . . . the adverse positions of government and defendant have solidified' " the Sixth Amendment right to counsel does not attach. 467 U. S., at 189 (quoting <i>Kirby</i> v. <i>Illinois, supra,</i> at 689).</p>
<p>Because, as respondent acknowledges, the events that led to the inculpatory statements preceded the formal initiation of adversary judicial proceedings, we reject the contention that the conduct of the police violated his rights under the Sixth Amendment.</p>
<p></p>
<h2>IV</h2>
<p>Finally, respondent contends that the conduct of the police was so offensive as to deprive him of the fundamental fairness guaranteed by the Due Process Clause of the Fourteenth Amendment. Focusing primarily on the impropriety of conveying false information to an attorney, he invites us to declare that such behavior should be condemned as violative of canons fundamental to the " `traditions and conscience of our people.' " <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#169" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 169</a></span> (1952), quoting <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span> (1934). We do not question that on facts more egregious than those presented here police deception might rise to a level of a due process violation. Accordingly, JUSTICE STEVENS' <span class="star-pagination">*433</span> apocalyptic suggestion that we have approved any and all forms of police misconduct is demonstrably incorrect.<sup>[4]</sup> We hold only that, on these facts, the challenged conduct falls short of the kind of misbehavior that so shocks the sensibilities <span class="star-pagination">*434A</span> of civilized society as to warrant a federal intrusion into the criminal processes of the States.</p>
<p>We hold therefore that the Court of Appeals erred in finding that the Federal Constitution required the exclusion of the three inculpatory statements. Accordingly, we reverse and remand for proceedings consistent with this opinion.</p>
<p><i>So ordered.</i></p>
<p><span class="star-pagination">*434B</span> JUSTICE STEVENS, with whom JUSTICE BRENNAN and JUSTICE MARSHALL join, dissenting.</p>
<p>This case poses fundamental questions about our system of justice. As this Court has long recognized, and reaffirmed only weeks ago, "ours is an accusatorial and not an inquisitorial system." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985).<sup>[1]</sup> The Court's opinion today represents a startling departure from that basic insight.</p>
<p><span class="star-pagination">*435</span> The Court concludes that the police may deceive an attorney by giving her false information about whether her client will be questioned, and that the police may deceive a suspect by failing to inform him of his attorney's communications and efforts to represent him.<sup>[2]</sup> For the majority, this conclusion, though "distaste[ful]," <i>ante,</i> at 424, is not even debatable. The deception of the attorney is irrelevant because the attorney has no right to information, accuracy, honesty, or fairness in the police response to her questions about her client. The deception of the client is acceptable, because, although the information would affect the client's assertion of his rights, the client's actions in ignorance of the availability of his attorney are voluntary, knowing, and intelligent; additionally, society's interest in apprehending, prosecuting, and punishing criminals outweighs the suspect's interest in information regarding his attorney's efforts to communicate with him. Finally, even mendacious police interference in the communications between a suspect and his lawyer does not violate any notion of fundamental fairness because it does not shock the conscience of the majority.</p>
<p>The case began in March 1977 with the discovery of Mary Jo Hickey, unconscious and disheveled in a deserted parking lot, lying in a pool of blood, with semen on her clothes, her dentures broken, and a piece of heavy, bloodstained metal nearby. Days later, Brian Burbine, then 20 years old, went to Maine and stayed with friends. According to the friends' testimony at trial, he was upset, and described a night out with Hickey, who was then 35. After several drinks, <span class="star-pagination">*436</span> Burbine told them, a ride home turned into a violent encounter; he hit Hickey several times and threw her out of the car. Three weeks after she was discovered in the parking lot, Hickey died. Three months later, after the 21-hour period of detention by the Cranston and Providence, Rhode Island, police that is the focus of this dispute, Burbine was charged with her murder, and ultimately found guilty of it.</p>
<p>The murder of Mary Jo Hickey was a vicious crime, fully meriting a sense of outrage and a desire to find and prosecute the perpetrator swiftly and effectively. Indeed, by the time Burbine was arrested on an unrelated breaking-and-entering charge, the Hickey murder had been the subject of a local television special.<sup>[3]</sup> Not surprisingly, Detective Ferranti, the Cranston Detective who "broke" the case, was rewarded with a special commendation for his efforts.<sup>[4]</sup></p>
<p>The recognition that ours is an accusatorial, and not an inquisitorial system nevertheless requires that the government's actions, even in responding to this brutal crime, respect those liberties and rights that distinguish this society from most others. As Justice Jackson observed shortly after his return from Nuremberg, cases of this kind present "a real dilemma in a free society . . . for the defendant is shielded by such safeguards as no system of law except the Anglo-American concedes to him."<sup>[5]</sup> Justice Frankfurter similarly <span class="star-pagination">*437</span> emphasized that it is "a fair summary of history to say that the safeguards of liberty have been forged in controversies involving not very nice people."<sup>[6]</sup> And, almost a century and a half ago, Macaulay observed that the guilt of Titus Oates could not justify his conviction by improper methods: "That Oates was a bad man is not a sufficient excuse; for the guilty are almost always the first to suffer those hardships which are afterwards used as precedents against the innocent."<sup>[7]</sup></p>
<p>The Court's holding focuses on the period after a suspect has been taken into custody and before he has been charged with an offense. The core of the Court's holding is that police interference with an attorney's access to her client during that period is not unconstitutional. The Court reasons that a State has a compelling interest, not simply in custodial interrogation, but in lawyer-free, incommunicado custodial interrogation. Such incommunicado interrogation is so important that a lawyer may be given false information that prevents her presence and representation; it is so important that police may refuse to inform a suspect of his attorney's <span class="star-pagination">*438</span> communications and immediate availability.<sup>[8]</sup> This conclusion flies in the face of this Court's repeated expressions of deep concern about incommunicado questioning.<sup>[9]</sup> Until <span class="star-pagination">*439</span> today, incommunicado questioning has been viewed with the strictest scrutiny by this Court; today, incommunicado questioning is embraced as a societal goal of the highest order that justifies police deception of the shabbiest kind.</p>
<p>It is not only the Court's ultimate conclusion that is deeply disturbing; it is also its manner of reaching that conclusion. The Court completely rejects an entire body of law on the subject  the many carefully reasoned state decisions that have come to precisely the opposite conclusion.<sup>[10]</sup> The Court <span class="star-pagination">*440</span> similarly dismisses the fact that the police deception which it sanctions quite clearly violates the American Bar Association's Standards for Criminal Justice<sup>[11]</sup>  Standards which <span class="star-pagination">*441</span> THE CHIEF JUSTICE has described as "the single most comprehensive and probably the most monumental undertaking in the field of criminal justice ever attempted by the American legal profession in our national history,"<sup>[12]</sup> and which this Court frequently finds helpful.<sup>[13]</sup> And, of course, the Court dismisses the fact that the American Bar Association has emphatically endorsed the prevailing state-court position and expressed its serious concern about the effect that a contrary view  a view, such as the Court's, that exalts incommunicado interrogation, sanctions police deception, and demeans the right to consult with an attorney  will have in police stations and courtrooms throughout this Nation.<sup>[14]</sup> Of greatest importance, the Court misapprehends or rejects the central principles that have, for several decades, animated this Court's decisions concerning incommunicado interrogation.<sup>[15]</sup></p>
<p>Police interference with communications between an attorney and his client is a recurrent problem. The factual variations in the many state-court opinions condemning this interference as a violation of the Federal Constitution suggest the <span class="star-pagination">*442</span> variety of contexts in which the problem emerges. In Oklahoma, police led a lawyer to several different locations while they interrogated the suspect;<sup>[16]</sup> in Oregon, police moved a suspect to a new location when they learned that his lawyer was on his way;<sup>[17]</sup> in Illinois, authorities failed to tell a suspect that his lawyer had arrived at the jail and asked to see him;<sup>[18]</sup> in Massachusetts, police did not tell suspects that their lawyers were at or near the police station.<sup>[19]</sup> In all these cases, the police not only failed to inform the suspect, but also misled the attorneys. The scenarios vary, but the core problem of police interference remains. "Its recurrence suggests that it has roots in some condition fundamental and general to our criminal system." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#57" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 57</a></span> (1949) (Jackson, J., concurring in result).</p>
<p>The near-consensus of state courts and the legal profession's Standards about this recurrent problem lends powerful support to the conclusion that police may not interfere with communications between an attorney and the client whom they are questioning. Indeed, at least two opinions from this Court seemed to express precisely that view.<sup>[20]</sup> The Court today flatly rejects that widely held view and responds to this recurrent problem by adopting the most restrictive interpretation of the federal constitutional restraints on police <span class="star-pagination">*443</span> deception, misinformation, and interference in attorney-client communications.</p>
<p>The exact reach of the Court's opinion is not entirely clear because, on the one hand, it indicates that more egregious forms of police deception might violate the Constitution, <i>ante,</i> at 432, while, on the other hand, it endeavors to make its disposition of this case palatable by making findings of fact concerning the voluntariness of Burbine's confessions that the trial judge who heard the evidence declined to make.<sup>[21]</sup> Before addressing the legal issues, it therefore seems appropriate to make certain additional comments about what the record discloses concerning the incriminating statements made by Burbine during the 21-hour period that he was detained by the Cranston and Providence police on June 29 and June 30, 1977.</p>
<p></p>
<h2>I</h2>
<p>As the majority points out, with respect to attorney Munson's telephone call, the Rhode Island Supreme Court's summary of factual findings provides the common ground for analysis:</p>
<blockquote>"At approximately 8:15 [on June 29, 1977], Ms. Munson called the Cranston police station and asked that her call be transferred to the detective division. A male voice responded with the word `Detectives.' Ms. Munson identified herself and asked if Brian Burbine was being held; the person responded affirmatively. Ms. Munson explained to the person that Burbine was represented by attorney Casparian who was not available; she further stated that she would act as Burbine's legal counsel in the event that the police intended to place him in a lineup or question him. The unidentified person told Ms. Munson that the police would not be questioning Burbine or putting him in a lineup and that they were <span class="star-pagination">*444</span> through with him for the night. Ms. Munson was not informed that the Providence police were at the Cranston police station or that Burbine was a suspect in Mary's murder. The trial justice found as a fact that Ms. Munson did make the call, but further found that there was no collusion or conspiracy on the part of the police `to secrete [Burbine] from his attorney . . . .' " <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#23" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 23-24</a></span> (1982).<sup>[22]</sup></blockquote>
<p>Although this paragraph accurately describes attorney Munson's 8:15 call, the significance of the false response to her inquiry is best understood in the context of the events that were then proceeding in the police station. The difficulty in reconstructing some of those events illustrates the need for strict presumptions regarding the consequences of custodial interrogation  a need this Court has repeatedly recognized.<sup>[23]</sup></p>
<p><span class="star-pagination">*445</span> On June 27, 1977, an unidentified person advised Detective Ferranti that a man known as "Butch," who lived at 306 New York Avenue in Providence, was responsible for the death of Mary Jo Hickey. The record does not explain why Ferranti, who was a member of the Cranston Police Force, was informed about a crime that occurred in Providence.</p>
<p>At about 3 p.m. on June 29, 1977, Cranston police officers apprehended respondent Burbine and two other men (DiOrio and Sparks) in "a burned out building in the Cranston area." S. H. 6, 180. The three men were taken to the Cranston police station, charged with "breaking and entering," and placed in separate rooms. After noticing that DiOrio and Burbine lived at 306 New York Avenue in Providence, Detective Ferranti talked to DiOrio and was told that Burbine was the only "Butch" at that address. <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#146" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 146-147</a></span>.</p>
<p>At approximately 4:30, Ferranti "went in the room where Burbine was" and asked him "if there was anybody that he knew by the name of Butch on the street, and he said he was the only Butch." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#148" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 148</a></span>.<sup>[24]</sup> After the brief questioning about the identity of "Butch," Detective Ferranti left Burbine in the interrogation room  where he remained until about 9 p.m.<sup>[25]</sup>  and interrogated DiOrio and Sparks. They both "made damaging statements relative to Burbine being involved in the murder in Providence"; Ferranti therefore "immediately contacted Providence Police." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#149" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 149-150</a></span>. The Providence officers  Captain Wilson (the Chief of Detectives), Lieutenant Gannon, and Detective Trafford  responded promptly, and arrived at the Cranston station between <span class="star-pagination">*446</span> 6 and 7 p.m. Lieutenant Gannon testified that, as he drove to the Cranston police station, he knew that he might not be able to question Burbine "[i]f for some reason he didn't want to give me a statement, if for some reason he chose to get an attorney and the attorney informed us that he didn't want him to give a statement." Trial Tr. 407.</p>
<p>After arriving at the station, the three Providence officers, as well as Ferranti and a second Cranston officer (Lieutenant Ricard), either remained in the large central room in the basement of the Cranston police station, or participated in the questioning of DiOrio and Sparks in interrogation rooms adjacent to that large central room.</p>
<p>It was at this point  with Burbine alone in another adjacent room, with Providence police on hand, with police from two Departments questioning Sparks and DiOrio about Burbine's involvement in the Hickey homicide  that attorney Munson telephoned. Her call arrived at 8:15; she asked for "Detectives," and was told that the police "would not be questioning Burbine" and that they were "through" with him for the night. These statements were false. Moreover, she was not told that Burbine would be questioned about a homicide rather than the breaking-and-entering charge on which he had been arrested, and she was not told that Providence police were at the Cranston police station preparing to question Burbine about a Providence crime.</p>
<p>At about 9, some 45 minutes after Munson received the assurance that the police were "through" with Burbine, the officers completed their questioning of DiOrio and Sparks and were prepared to question Burbine. There is no dispute about the fact that Burbine was brought into the central room at about 9, that all five police officers were then present, and that Burbine appeared somewhat upset and professed that he " `didn't do anything wrong.' " S. H. 21. Detective Ferranti testified that this statement was in response to questions from the Providence police about the Hickey <span class="star-pagination">*447</span> homicide;<sup>[26]</sup> Lieutenant Gannon of the Providence police testified that the statement was about the Hickey homicide, but that Providence police did not question Burbine and that they merely saw Burbine being escorted by Ferranti.<sup>[27]</sup> Burbine was not told that attorney Munson had called and had asked about him; nor was he told that Munson had been informed that the police were through with him for the night. After his protestations, Burbine was taken into another interrogation room.</p>
<p>Detective Ferranti then went into that room and, according to the testimony of the Providence officers, spent either "ten minutes" or from "five to ten minutes" alone with Burbine.<sup>[28]</sup> The record does not tell us whether he told Burbine that Sparks and DiOrio had just given statements implicating him in the Hickey homicide. Nor does it resolve the question whether Burbine's decision to confess was made <i>before</i> his session with Ferranti or <i>as a result</i> of that session. The Court evidently makes the former assumption, for it asserts that Burbine "initiated" this encounter. <i>Ante,</i> at 421-422. However, the state courts made no finding about this <span class="star-pagination">*448</span> "initiation" by Burbine. Detective Ferranti testified that Burbine banged and kicked on the door, S. H. 153-154; Lieutenant Gannon testified that he "believed" there was a knocking or some communication from Burbine, <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#22" aria-description="Citation for case: State v. Burbine"><i>id.,</i> at 22</a></span>, but he was "not sure." <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#66" aria-description="Citation for case: State v. Burbine"><i>Id.,</i> at 66</a></span>.<sup>[29]</sup> None of the other officers, who were apparently in the large room adjacent to Burbine's, corroborated this testimony by mentioning any "banging," "kicking," or other noise from Burbine's direction. In all events, some minutes later, Detective Ferranti came back out of the room and indicated that Burbine wanted to talk.</p>
<p>Lieutenant Gannon and Detective Trafford of the Providence police accompanied Detective Ferranti "back into the room." During the period between 9:30 and 10:20 p.m., they administered <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and typed out a four-page statement which Burbine signed, waiving his constitutional rights, acknowledging his responsibility for the death of Hickey, and reciting his version of that event. Ferranti alternately testified that Burbine was "coherent" and "incoherent" at the time of this questioning. <i>Id.,</i> at 157-158; Trial Tr. 198, 208-209. Apparently for the first time since his arrival at the station in the afternoon, the police then brought Burbine some food. S. H. 160, Trial Tr. 205.</p>
<p>After obtaining Burbine's signature on the first written statement at 10:20 p.m., the police were still not "through" with Burbine. Burbine's first statement included no mention of the clothes that he had been wearing, or of a glass that was found with Hickey's purse a few blocks from the homicide. Soon after the completion of the first statement, and after the Providence and Cranston officers had discussed the first statement and expressed pleasure with their success,<sup>[30]</sup><span class="star-pagination">*449</span> Gannon, Trafford, and Ferranti again questioned Burbine. They ascertained that he was wearing his "red toke" and "black windbreaker" at the time, and that Hickey had left the bar with a glass in hand.<sup>[31]</sup> At 11:20 p.m., Burbine signed the second statement.</p>
<p>The following morning, the officers obtained a warrant, conducted a search of Burbine's residence, and seized the clothing that he had described in the second statement. In the meantime, Burbine was arraigned in Cranston court on the charge for which he had been arrested. Still without counsel, Burbine pleaded guilty to malicious damage. After the Cranston proceeding, Providence officers instantly arrested him for the Hickey homicide. Trial Tr. 501. Burbine was taken to the Providence police station, where he executed a third waiver of rights and identified the coat and jacket that the officers had seized. Shortly after noon, Major Leyden called the Public Defender's Office and requested counsel for Burbine because he would be placed in a lineup. <i>Id.,</i> at 423.</p>
<p>Thus, although there are a number of ambiguities in the record, the state-court findings established (1) that attorney Munson made her call at about 8:15 p.m.; (2) that she was given false information; (3) that Burbine was not told of her <span class="star-pagination">*450</span> call; and (4) that he was thereafter given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, waived his rights, and signed three incriminating statements without receiving any advice from an attorney. The remainder of the record underscores two points. The first is the context of the call  a context in which two Police Departments were on the verge of resolving a highly publicized, hauntingly brutal homicide and in which, as Lieutenant Gannon testified, the police were aware that counsel's advice to remain silent might be an obstacle to obtaining a confession. The second is the extent of the uncertainty about the events that motivated Burbine's decision to waive his rights. The lawyer-free privacy of the interrogation room, so exalted by the majority, provides great difficulties in determining what actually transpired. It is not simply the ambiguity that is troublesome; if so, the problem would be not unlike other difficult evidentiary problems. Rather, the particularly troublesome aspect is that the ambiguity arises in the very situation  incommunicado interrogation  for which this Court has developed strict presumptions and for which this Court has, in the past, imposed the heaviest burden of justification on the government. It is in this context, and the larger context of our accusatorial system, that the deceptive conduct of the police must be evaluated.</p>
<p></p>
<h2>II</h2>
<p>Well-settled principles of law lead inexorably to the conclusion that the failure to inform Burbine of the call from his attorney makes the subsequent waiver of his constitutional rights invalid. Analysis should begin with an acknowledgment that the burden of proving the validity of a waiver of constitutional rights is always on the <i>government.</i><sup>[32]</sup> When <span class="star-pagination">*451</span> such a waiver occurs in a custodial setting, that burden is an especially heavy one because custodial interrogation is inherently coercive,<sup>[33]</sup> because disinterested witnesses are seldom available to describe what actually happened,<sup>[34]</sup> and because history has taught us that the danger of overreaching during incommunicado interrogation is so real.<sup>[35]</sup></p>
<p>In applying this heavy presumption against the validity of waivers, this Court has sometimes relied on a case-by-case totality of the circumstances analysis.<sup>[36]</sup> We have found, however, that some custodial interrogation situations require strict presumptions against the validity of a waiver. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> established that a waiver is not valid in the absence of certain warnings. <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), similarly established that a waiver is not valid if police <span class="star-pagination">*452</span> initiate questioning after the defendant has invoked his right to counsel. In these circumstances, the waiver is invalid as a matter of law even if the evidence overwhelmingly establishes, as a matter of fact, that "a suspect's decision not to rely on his rights was uncoerced, that he at all times knew that he could stand mute and request a lawyer, and that he was aware of the State's intention to use his statements to secure a conviction," see <i>ante,</i> at 422. In light of our decision in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> the Court is simply wrong in stating that "the analysis is complete and the waiver is valid as a matter of law" when these facts have been established. <i>Ante,</i> at 422-423.<sup>[37]</sup> Like the failure to give warnings and like police initiation of interrogation after a request for counsel, police deception of a suspect through omission of information regarding attorney communications greatly exacerbates the inherent problems of incommunicado interrogation and requires a clear principle to safeguard the presumption against the waiver of constitutional rights. As in those situations, the police deception should render a subsequent waiver invalid.</p>
<p>Indeed, as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself makes clear, proof that the required warnings have been given is a necessary, but by no means sufficient, condition for establishing a valid waiver. As the Court plainly stated in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> "any evidence that the accused was threatened, tricked, or cajoled into a waiver will, of course, show that the defendant did not voluntarily waive his privilege. The requirement of warnings and waiver of rights is a fundamental with respect to the Fifth <span class="star-pagination">*453</span> Amendment privilege and not simply a preliminary ritual to existing methods of interrogation." 384 U. S., at 476.</p>
<p>In this case it would be perfectly clear that Burbine's waiver was invalid if, for example, Detective Ferranti had "threatened, tricked, or cajoled" Burbine in their private preconfession meeting  perhaps by misdescribing the statements obtained from DiOrio and Sparks  even though, under the Court's truncated analysis of the issue, Burbine fully understood his rights. For <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> clearly condemns threats or trickery that cause a suspect to make an unwise waiver of his rights even though he fully understands those rights. In my opinion there can be no constitutional distinction  as the Court appears to draw, <i>ante,</i> at 423-424  between a deceptive misstatement and the concealment by the police of the critical fact that an attorney retained by the accused or his family has offered assistance, either by telephone or in person.<sup>[38]</sup></p>
<p>Thus, the Court's truncated analysis, which relies in part on a distinction between deception accomplished by means of an omission of a critically important fact and deception by means of a misleading statement, is simply untenable. If, as the Court asserts, "the analysis is at an end" as soon as the suspect is provided with enough information to have the <i>capacity</i> to understand and exercise his rights, I see no reason why the police should not be permitted to make the same kind of misstatements to the suspect that they are apparently allowed to make to his lawyer. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, clearly <span class="star-pagination">*454</span> establishes that both kinds of deception vitiate the suspect's waiver of his right to counsel.<sup>[39]</sup></p>
<p>As the Court notes, the question is whether the deceptive police conduct "deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Ante,</i> at 424. This question has been resoundingly answered time and time again by the state courts that, with rare exceptions,<sup>[40]</sup> have correctly understood the meaning of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion.<sup>[41]</sup> The majority's <span class="star-pagination">*455</span> blithe assertion of "no doubt" about the outcome of this case, <i>ante,</i> at 421, simply ignores the prevailing view of the state courts that have considered this issue. Particularly in an opinion that relies on a desire to avoid "a federal intrusion into the criminal processes of the States," <i>ante,</i> at 434, one would expect at least some indication why, in the majority's view, so many state courts have been so profoundly wrong on this precise issue. Unlike the majority, the state courts have realized that attorney communication to the police <span class="star-pagination">*456</span> about the client is an event that has a direct "bearing" on the knowing and intelligent waiver of constitutional rights. As the Oregon Supreme Court has explained: "To pass up an abstract offer to call some unknown lawyer is very different from refusing to talk with an identified attorney actually available to provide at least initial assistance and advice, whatever might be arranged in the long run. A suspect indifferent to the first offer may well react quite differently to the second." <i>State</i> v. <i>Haynes,</i> <span class="citation" data-id="9578898"><a href="/opinion/1320570/state-v-haynes/#72" aria-description="Citation for case: State v. Haynes">288 Ore. 59, 72</a></span>, <span class="citation" data-id="9578898"><a href="/opinion/1320570/state-v-haynes/#278" aria-description="Citation for case: State v. Haynes">602 P. 2d 272, 278</a></span> (1979), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/945/">446 U. S. 945</a></span> (1980).<sup>[42]</sup></p>
<p>In short, settled principles about construing waivers of constitutional rights and about the need for strict presumptions in custodial interrogations, as well as a plain reading of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion itself, overwhelmingly support the conclusion reached by almost every state court that has considered the matter  a suspect's waiver of his right to counsel is invalid if police refuse to inform the suspect of his counsel's communications.</p>
<p></p>
<h2>III</h2>
<p>The Court makes the alternative argument that requiring police to inform a suspect of his attorney's communications to <span class="star-pagination">*457</span> and about him is not required because it would upset the careful "balance" of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Despite its earlier notion that the attorney's call is an "outside event" that has "no bearing" on a knowing and intelligent waiver, the majority does acknowledge that information of attorney Munson's call "would have been useful to respondent" and "might have affected his decision to confess." <i>Ante,</i> at 422.<sup>[43]</sup> Thus, a rule requiring the police to inform a suspect of an attorney's call would have two predictable effects. It would serve "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s goal of dispelling the compulsion inherent in custodial interrogation," <i>ante,</i> at 425, and it would disserve the goal of custodial interrogation because it would result in fewer confessions. By a process of balancing these two concerns, the Court finds the benefit to the individual outweighed by the "substantial cost to society's legitimate and substantial interest in securing admissions of guilt." <i>Ante,</i> at 427.</p>
<p>The Court's balancing approach is profoundly misguided. The cost of suppressing evidence of guilt will always make the value of a procedural safeguard appear "minimal," "marginal," or "incremental." Indeed, the value of any trial at all seems like a "procedural technicality" when balanced against the interest in administering prompt justice to a murderer or a rapist caught redhanded. The individual interest in procedural safeguards that minimize the risk of error is easily discounted when the fact of guilt appears certain beyond doubt.</p>
<p>What is the cost of requiring the police to inform a suspect of his attorney's call? It would decrease the likelihood that custodial interrogation will enable the police to obtain a confession. This is certainly a real cost, but it is the same cost that this Court has repeatedly found necessary to preserve <span class="star-pagination">*458</span> the character of our free society and our rejection of an inquisitorial system. Three examples illustrate the point.</p>
<p>In <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), we excluded a confession by a defendant who had not been permitted to consult with his lawyer, and whose lawyer had not been permitted to see him. We emphasized the "lesson of history" that our system of justice is not founded on a fear that a suspect will exercise his rights. "If the exercise of constitutional rights will thwart the effectiveness of a system of law enforcement, then there is something very wrong with that system." <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/#490" aria-description="Citation for case: Escobedo v. Illinois"><i>Id.,</i> at 490</a></span>. In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we similarly stressed this character of our system, despite its "cost," by unequivocally holding that an individual has an absolute right to refuse to respond to police interrogation and to have the assistance of counsel during any questioning.<sup>[44]</sup> Thus, as a matter of law, the assumed right of the police to interrogate a suspect is no right at all; at best, it is a mere privilege terminable at the will of the suspect. And, more recently in <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979), the Court corrected the long-held but mistaken view of the police that they have some sort of right to take any suspect <span class="star-pagination">*459</span> into custody for the purpose of questioning him even though they may not have probable cause to arrest.<sup>[45]</sup></p>
<p>Just as the "cost" does not justify taking a suspect into custody or interrogating him without giving him warnings simply because police desire to question him, so too the "cost" does not justify permitting police to withhold from a suspect knowledge of an attorney's communication, even though that communication would have an unquestionable effect on the suspect's exercise of his rights. The "cost" that concerns the Court amounts to nothing more than an acknowledgement that the law enforcement interest in obtaining convictions suffers whenever a suspect exercises the rights that are afforded by our system of criminal justice. In other words, it is the fear that an individual may exercise his rights that tips the scales of justice for the Court today. The principle that ours is an accusatorial, not an inquisitorial, system, however, has repeatedly led the Court to reject that fear as a valid reason for inhibiting the invocation of rights.</p>
<p>If the Court's cost-benefit analysis were sound, it would justify a repudiation of the right to a warning about counsel itself. There is only a difference in degree between a presumption that advice about the immediate availability of a lawyer would not affect the voluntariness of a decision to confess, and a presumption that every citizen knows that he has a right to remain silent and therefore no warnings of any kind are needed. In either case, the withholding of information serves precisely the same law enforcement interests. And in both cases, the cost can be described as nothing more than <span class="star-pagination">*460</span> an incremental increase in the risk that an individual will make an unintelligent waiver of his rights.</p>
<p>In cases like <i>Escobedo, Miranda,</i> and <i><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Dunaway</a></span>,</i> the Court has viewed the balance from a much broader perspective. In all these cases  indeed, whenever the distinction between an inquisitorial and an accusatorial system of justice is implicated  the law enforcement interest served by incommunicado interrogation has been weighed against the interest in individual liberty that is threatened by such practices. The balance has never been struck by an evaluation of empirical data of the kind submitted to legislative decisionmakers  indeed, the Court relies on no such data today. Rather, the Court has evaluated the quality of the conflicting rights and interests. In the past, that kind of balancing process has led to the conclusion that the police have <i>no right</i> to compel an individual to respond to custodial interrogation, and that the interest in liberty that is threatened by incommunicado interrogation is so precious that special procedures must be followed to protect it. The Court's contrary conclusion today can only be explained by its failure to appreciate the value of the liberty that an accusatorial system seeks to protect.</p>
<p></p>
<h2>IV</h2>
<p>The Court also argues that a rule requiring the police to inform a suspect of an attorney's efforts to reach him would have an additional cost: it would undermine the "clarity" of the rule of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case. <i>Ante,</i> at 425-426. This argument is not supported by any reference to the experience in the States that have adopted such a rule. The Court merely professes concern about its ability to answer three quite simple questions.<sup>[46]</sup></p>
<p><span class="star-pagination">*461</span> Moreover, the Court's evaluation of the interest in "clarity" is rather one-sided. For a police officer with a printed card containing the exact text he is supposed to recite, perhaps the rule is clear. But the interest in clarity that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision was intended to serve is not merely for the benefit of the police. Rather, the decision was also, and primarily, intended to provide adequate guidance to the person in custody who is being asked to waive the protections afforded by the Constitution.<sup>[47]</sup> Inevitably, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision also serves the judicial interest in clarifying the inquiry <span class="star-pagination">*462</span> into what actually transpired during a custodial interrogation.<sup>[48]</sup> Under the Court's conception of the interest in clarity, however, the police would presumably prevail whenever they could convince the trier of fact that a required ritual was performed before the confession was obtained.</p>
<p></p>
<h2>V</h2>
<p>At the time attorney Munson made her call to the Cranston police station, she was acting as Burbine's attorney. Under ordinary principles of agency law the deliberate deception of Munson was tantamount to deliberate deception of her client.<sup>[49]</sup> If an attorney makes a mistake in the course of her representation of her client, the client must accept the consequences of that mistake.<sup>[50]</sup> It is equally clear that when an attorney makes an inquiry on behalf of her client, the client is entitled to a truthful answer. Surely the client must have the same remedy for a false representation to his lawyer that he would have if he were acting <i>pro se</i> and had propounded the question himself.</p>
<p>The majority brushes aside the police deception involved in the misinformation of attorney Munson. It is irrelevant to the Fifth Amendment analysis, concludes the majority, because that right is personal; it is irrelevant to the Sixth <span class="star-pagination">*463</span> Amendment analysis, continues the majority, because the Sixth Amendment does not apply until formal adversary proceedings have begun.</p>
<p>In my view, as a matter of law, the police deception of Munson was tantamount to deception of Burbine himself. It constituted a violation of Burbine's right to have an attorney present during the questioning that began shortly thereafter. The existence of that right is undisputed.<sup>[51]</sup> Whether the source of that right is the Sixth Amendment, the Fifth Amendment, or a combination of the two is of no special importance, for I do not understand the Court to deny the existence of the right.</p>
<p>The pertinent question is whether police deception of the attorney is utterly irrelevant to that right. In my judgment, it blinks at reality to suggest that misinformation which prevented the presence of an attorney has no bearing on the protection and effectuation of the right to counsel in custodial interrogation. The majority parses the role of attorney and suspect so narrowly that the deception of the attorney is of no <span class="star-pagination">*464</span> constitutional significance. In other contexts, however, the Court does not hesitate to recognize an identity between the interest of attorney and accused.<sup>[52]</sup> The character of the attorney-client relationship requires rejection of the Court's notion that the attorney is some entirely distinct, completely severable entity and that deception of the attorney is irrelevant to the right of counsel in custodial interrogation.<sup>[53]</sup></p>
<p><span class="star-pagination">*465</span> The possible reach of the Court's opinion is stunning. For the majority seems to suggest that police may deny counsel all access to a client who is being held. At least since <i>Escobedo</i> v. <i>Illinois</i><i>,</i> it has been widely accepted that police may not simply deny attorneys access to their clients who are in custody. This view has survived the recasting of <i><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span></i> from a Sixth Amendment to a Fifth Amendment case that the majority finds so critically important. That this prevailing view is shared <i>by the police</i> can be seen in the state-court opinions detailing various forms of police deception of attorneys.<sup>[54]</sup> For, if there were no obligation to give attorneys access, there would be no need to take elaborate steps to avoid access, such as shuttling the suspect to a different location,<sup>[55]</sup> or taking the lawyer to different locations;<sup>[56]</sup> police could simply refuse to allow the attorneys to see the suspects. But the law enforcement profession has apparently believed, quite rightly in my view, that denying lawyers access to their clients is impermissible. The Court today seems to assume that this view was error  that, from the federal constitutional perspective, the lawyer's access is, as a question from the Court put it in oral argument, merely "a matter of prosecutorial grace." Tr. of Oral Arg. 32. Certainly, nothing in the Court's Fifth and Sixth Amendment analysis acknowledges that there is <i>any</i> federal constitutional bar to an absolute denial of lawyer access to a suspect who is in police custody.</p>
<p>In sharp contrast to the majority, I firmly believe that the right to counsel at custodial interrogation is infringed by police treatment of an attorney that prevents or impedes the attorney's representation of the suspect at that interrogation.</p>
<p></p>
<h2>
<span class="star-pagination">*466</span> VI</h2>
<p>The Court devotes precisely five sentences to its conclusion that the police interference in the attorney's representation of Burbine did not violate the Due Process Clause. In the majority's view, the due process analysis is a simple "shock the conscience" test. Finding its conscience troubled,<sup>[57]</sup> but not shocked, the majority rejects the due process challenge.</p>
<p>In a variety of circumstances, however, the Court has given a more thoughtful consideration to the requirements of due process. For instance, we have concluded that use of a suspect's post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings silence against him violates the due process requirement of fundamental fairness because such use breaches an implicit promise that "silence will carry no penalty."<sup>[58]</sup> Similarly, we have concluded that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment."<sup>[59]</sup> We have also concluded that vindictive prosecution violates due process;<sup>[60]</sup> so too does vindictive sentencing.<sup>[61]</sup> Indeed, we have emphasized that analysis of the "voluntariness" of a confession is frequently a "convenient shorthand" for reviewing objectionable police methods under the rubric of the due process requirement of fundamental fairness.<sup>[62]</sup> What emerges from <span class="star-pagination">*467</span> these cases is not the majority's simple "shock the conscience" test, but the principle that due process requires fairness, integrity, and honor in the operation of the criminal justice system, and in its treatment of the citizen's cardinal constitutional protections.</p>
<p>In my judgment, police interference in the attorney-client relationship is the type of governmental misconduct on a matter of central importance to the administration of justice that the Due Process Clause prohibits. Just as the police cannot impliedly promise a suspect that his silence will not be used against him and then proceed to break that promise, so too police cannot tell a suspect's attorney that they will not question the suspect and then proceed to question him. Just as the government cannot conceal from a suspect material and exculpatory evidence, so too the government cannot conceal from a suspect the material fact of his attorney's communication.</p>
<p><span class="star-pagination">*468</span> Police interference with communications between an attorney and his client violates the due process requirement of fundamental fairness. Burbine's attorney was given completely false information about the lack of questioning; moreover, she was not told that her client would be questioned regarding a murder charge about which she was unaware. Burbine, in turn, was not told that his attorney had phoned and that she had been informed that he would not be questioned. Quite simply, the Rhode Island police effectively drove a wedge between an attorney and a suspect through misinformation and omissions.</p>
<p>The majority does not "question that on facts more egregious than those presented here police deception might rise to a level of a due process violation." <i>Ante,</i> at 432. In my view, the police deception disclosed by this record plainly does rise to that level.</p>
<p></p>
<h2>VII</h2>
<p>This case turns on a proper appraisal of the role of the lawyer in our society. If a lawyer is seen as a nettlesome obstacle to the pursuit of wrongdoers  as in an inquisitorial society  then the Court's decision today makes a good deal of sense. If a lawyer is seen as an aid to the understanding and protection of constitutional rights  as in an accusatorial society  then today's decision makes no sense at all.</p>
<p>Like the conduct of the police in the Cranston station on the evening of June 29, 1977, the Court's opinion today serves the goal of insuring that the perpetrator of a vile crime is punished. Like the police on that June night as well, however, the Court has trampled on well-established legal principles and flouted the spirit of our accusatorial system of justice.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the State of California et al. by <i>John K. Van de Kamp,</i> Attorney General of California, <i>Steve White,</i> Chief Assistant Attorney General, <i>Karl S. Mayer,</i> Assistant Attorney General, and <i>Ann K. Jensen</i> and <i>Dane R. Gillette,</i> Deputy Attorneys General, <i>Charles A. Graddick,</i> Attorney General of Alabama, <i>Norman C. Gorsuch,</i> Attorney General of Alaska, <i>Robert K. Corbin,</i> Attorney General of Arizona, <i>Duane Woodard,</i> Attorney General of Colorado, <i>Austin J. McGuigan,</i> Chief State's Attorney of Connecticut, <i>Charles M. Oberly III,</i> Attorney General of Delaware, <i>Neil F. Hartigan,</i> Attorney General of Illinois, <i>Linley E. Pearson,</i> Attorney General of Indiana, <i>Robert T. Stephan,</i> Attorney General of Kansas, <i>William J. Guste, Jr.,</i> Attorney General of Louisiana, <i>James E. Tierney,</i> Attorney General of Maine, <i>Stephen H. Sachs,</i> Attorney General of Maryland, <i>Stanley D. Steinborn,</i> Attorney General of Michigan, <i>William L. Webster,</i> Attorney General of Missouri, <i>Mike Greeley,</i> Attorney General of Montana, <i>Stephen E. Merrill,</i> Attorney General of New Hampshire, <i>Irwin I. Kimmelman,</i> Attorney General of New Jersey, <i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Nicholas J. Spaeth,</i> Attorney General of North Dakota, <i>Leroy S. Zimmerman,</i> Attorney General of Pennsylvania, <i>Travis Medlock,</i> Attorney General of South Carolina, <i>Mark V. Meierhenry,</i> Attorney General of South Dakota, <i>W. J. Michael Cody,</i> Attorney General of Tennessee, <i>Jim Mattox,</i> Attorney General of Texas, <i>Gerald L. Baliles,</i> Attorney General of Virginia, <i>Jeffrey L. Amestoy,</i> Attorney General of Vermont, <i>Charlie Brown,</i> Attorney General of West Virginia, <i>Bronson C. La Follette,</i> Attorney General of Wisconsin, <i>A. G. McClintock,</i> Attorney General of Wyoming, <i>Richard G. Opper,</i> Attorney General of Guam, <i>J'Ada M. Finch-Sheen,</i> Attorney General of the Virgin Islands, and <i>Jack E. Yelverton;</i> and for Americans for Effective Law Enforcement, Inc., by <i>David Crump, Daniel B. Hales, Fred E. Inbau, Wayne W. Schmidt,</i> and <i>James P. Manak.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the American Bar Association by <i>William W. Falsgraf, Steven H. Goldblatt,</i> and <i>Charles G. Cole;</i> for the National Association of Criminal Defense Lawyers et al. by <i>Judith H. Mizner, Nancy Gertner,</i> and <i>Scott Baldwin;</i> and for the National Legal Aid and Defender Association et al. by <i>Kim R. Fawcett, James R. Neuhard, Jack D. Novik,</i> and <i>John A. MacFadyen.</i></p>
<p>[1]  The dissent incorrectly reads our analysis of the components of a valid waiver to be inconsistent with the Court's holding in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). <i>Post,</i> at 452. When a suspect <i>has</i> requested counsel, the interrogation must cease, regardless of any question of waiver, unless the suspect himself initiates the conversation. In the course of its lengthy exposition, however, the dissent never comes to grips with the crucial distinguishing feature of this case  that Burbine at no point requested the presence of counsel, as was his right under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to do. We do not quarrel with the dissent's characterization of police interrogation as a "privilege terminable at the will of the suspect." <i>Post,</i> at 458. We reject, however, the dissent's entirely undefended suggestion that the Fifth Amendment "right to counsel" requires anything more than that the police inform the suspect of his right to representation and honor his request that the interrogation cease until his attorney is present. See, <i>e. g., </i><i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975).</p>
<p>[2]  Petitioner does not argue that respondent's valid waiver of his Fifth Amendment right to counsel necessarily served to waive his parallel rights under the Sixth Amendment. Accordingly, we have no occasion to consider whether a waiver for one purpose necessarily operates as a general waiver of the right to counsel for all purposes.</p>
<p>[3]  Notwithstanding the Rhode Island Supreme Court's finding that, as a matter of state law, no attorney-client relationship existed between respondent and Ms. Munson, the Sixth Amendment issue is properly before us. <i>State</i> v. <i>Burbine,</i> <span class="citation" data-id="9752699"><a href="/opinion/2314564/state-v-burbine/#29" aria-description="Citation for case: State v. Burbine">451 A. 2d 22, 29</a></span> (1982). Petitioner now concedes that such a relationship existed and invites us to decide the Sixth Amendment question based on that concession. Of course, a litigant's concession cannot be used to circumvent the rule that this Court may not disregard a state court's interpretation of state law. Respondent's argument, however, does not focus on whether an attorney-client relationship actually existed as a formal matter of state law. He argues instead that, on the particular facts of this case, the Sixth Amendment right to counsel has been violated. In any event, even if the existence of an attorney-client relationship could somehow independently trigger the Sixth Amendment right to counsel, a position we reject, the type of circumstances that would give rise to the right would certainly have a federal definition.</p>
<p>[4]  Among its other failings, the dissent declines to follow <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), a decision that categorically forecloses JUSTICE STEVENS' major premise  that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires the police to inform a suspect of any and all information that would be useful to a decision whether to remain silent or speak with the police. See also <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). The dissent also launches a novel "agency" theory of the Fifth Amendment under which any perceived deception of a lawyer is automatically treated as deception of his or her client. This argument entirely disregards the elemental and established proposition that the privilege against compulsory self-incrimination is, by hypothesis, a personal one that can only be invoked by the individual whose testimony is being compelled.
</p>
<p>Most importantly, the dissent's misreading of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself is breathtaking in its scope. For example, it reads <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as creating an undifferentiated right to the presence of an attorney that is triggered automatically by the initiation of the interrogation itself. <i>Post,</i> at 463. Yet, as both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and subsequent decisions construing <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> make clear beyond refute, " `the interrogation must cease until an attorney is present' <i>only</i> `[i]f the individual states that he wants an attorney.' " <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975) (emphasis added), quoting <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. The dissent condemns us for embracing "incommunicado questioning . . . as a societal goal of the highest order that justifies police deception of the shabbiest kind." <i>Post,</i> at 439. We, of course, do nothing of the kind. As any reading of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> reveals, the decision, rather than proceeding from the premise that the rights and needs of the defendant are paramount to all others, embodies a carefully crafted balance designed to fully protect <i>both</i> the defendant's and society's interests. The dissent may not share our view that the Fifth Amendment rights of the defendant are amply protected by application of <i>Miranda as written.</i> But the dissent is "simply wrong," <i>post,</i> at 452, in suggesting that exclusion of Burbine's three confessions follows perfunctorily from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s mandate. Y. Kamisar, Police Interrogation and Confessions 217-218, n. 94 (1980).</p>
<p>Quite understandably, the dissent is outraged by the very idea of police deception of a lawyer. Significantly less understandable is its willingness to misconstrue this Court's constitutional holdings in order to implement its subjective notions of sound policy.</p>
<p>[1]  Justice Frankfurter succinctly explained the character of that distinction in his opinion in <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#54" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 54</a></span> (1949):
</p>
<p>"Ours is the accusatorial as opposed to the inquisitorial system. Such has been the characteristic of Anglo-American criminal justice since it freed itself from practices borrowed by the Star Chamber from the Continent whereby an accused was interrogated in secret for hours on end. See Ploscowe, <i>The Development of Present-Day Criminal Procedures in Europe and America,</i> <span class="citation no-link">48 Harv. L. Rev. 433</span>, 457-458, 467-473 (1935). Under our system society carries the burden of proving its charge against the accused not out of his own mouth. It must establish its case, not by interrogation of the accused even under judicial safeguards, but by evidence independently secured through skillful investigation. `The law will not suffer a prisoner to be made the deluded instrument of his own conviction.' 2 Hawkins, Pleas of the Crown, c. 46, § 34 (8th ed. 1824). The requirement of specific charges, their proof beyond a reasonable doubt, the protection of the accused from confessions extorted through whatever form of police pressures, the right to a prompt hearing before a magistrate, the right to assistance of counsel, to be supplied by government when circumstances make it necessary, the duty to advise an accused of his constitutional rights  these are all characteristics of the accusatorial system and manifestations of its demands. Protracted, systematic and uncontrolled subjection of an accused to interrogation by the police for the purpose of eliciting disclosures or confession is subversive of the accusatorial system."</p>
<p>See generally <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7-8</a></span> (1964); <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540-541</a></span> (1961); <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-545</a></span> (1897).</p>
<p>[2]  I agree with the majority that, in considering "the type of circumstances" that give rise to constitutional rights in this area, the relationship between an attorney and suspect has "a federal definition." <i>Ante,</i> at 429, n. 3. In my view, for federal constitutional purposes, members of a suspect's family may provide a lawyer with authority to act on a suspect's behalf while the suspect is in custody.</p>
<p>[3]  Tr. of Suppression Hearing 167 (S. H.).</p>
<p>[4]  <i>Id.,</i> at 168.</p>
<p>[5]  "Amid much that is irrelevant or trivial, one serious situation seems to me to stand out in these cases. The suspect neither had nor was advised of his right to get counsel. This presents a real dilemma in a free society. To subject one without counsel to questioning which may and is intended to convict him is a real peril to individual freedom. To bring in a lawyer means a real peril to solution of the crime, because, under our adversary system, he deems that his sole duty is to protect his client  guilty or innocent  and that in such a capacity he owes no duty whatever to help society solve its crime problem. Under this conception of criminal procedure, any lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to police under any circumstances.
</p>
<p>"If the State may arrest on suspicion and interrogate without counsel, there is no denying the fact that it largely negates the benefits of the constitutional guaranty of the right to assistance of counsel. Any lawyer who has ever been called into a case after his client has `told all' and turned any evidence he has over to the Government, knows how helpless he is to protect his client against the facts thus disclosed.</p>
<p>"I suppose the view one takes will turn on what one thinks should be the right of an accused person against the State. Is it his right to have the judgment on the facts? Or is it his right to have a judgment based on only such evidence as he cannot conceal from the authorities, who cannot compel him to testify in court and also cannot question him before? Our system comes close to the latter by any interpretation, for the defendant is shielded by such safeguards as no system of law

[...TRUNCATED 60237 of 180237 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
