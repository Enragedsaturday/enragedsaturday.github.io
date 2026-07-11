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

## GROUP: _overhaul2/lake/cases/Ashcroft v. al-Kidd.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Ashcroft v. al-Kidd"
type: case
citation: ""
parallel_cite: "179 L. Ed. 2d 1149; 131 S. Ct. 2074; 563 U.S. 731; 79 U.S.L.W. 4393; 22 Fla. L. Weekly Fed. S 1057"
neutral_cite: 2011 U.S. LEXIS 4021
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-05-31
docket: 10-98
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-05-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ashcroft v. al-Kidd
  varies_by_point: false
  scope_note: "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7344719/ashcroft-v-al-kidd/"
  cluster_id: 7344719
  opinion_id: 7262676
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Whren v. United States]]", "[[Malley v. Briggs]]", "[[Harlow v. Fitzgerald]]"]
aliases: ["al-Kidd v. Ashcroft", "Ashcroft v. Al-Kidd"]
tags: ["case", "section-1983", "bivens", "qualified-immunity", "material-witness", "pretext", "objective-reasonableness"]
holding: "An objectively reasonable arrest of a material witness on a valid warrant cannot be challenged as unconstitutional on the basis of the officer's subjective motive; subjective intent is irrelevant to Fourth Amendment reasonableness, and the contrary theory was not clearly established (QI)."
lake:
  record_id: Ashcroft v. al-Kidd
  status: verified
  projected_at: 2026-07-09
---

# Ashcroft v. al-Kidd

*563 U.S. 731 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Abdullah al-Kidd, a U.S. citizen, was arrested in 2003 on a federal material-witness warrant — ostensibly to secure his testimony in a terrorism prosecution — but was never called to testify. He sued former Attorney General John Ashcroft under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging that Ashcroft had adopted a policy of using the material-witness statute as a **pretext** to detain terrorism suspects whom the government lacked probable cause to charge, in violation of the Fourth Amendment. Ashcroft asserted [[Qualified Immunity|qualified immunity]].

## Issue
Whether an arrest made on a valid material-witness warrant can be challenged as unconstitutional based on the officer's alleged improper subjective motive — and, if the theory is doubtful, whether Ashcroft violated clearly established law.

## Rule
Fourth Amendment reasonableness is judged objectively, so subjective motive does not invalidate an otherwise-valid arrest. "Fourth Amendment reasonableness 'is predominantly an objective inquiry.' We ask whether 'the circumstances, viewed objectively, justify [the challenged] action.' If so, that action was reasonable 'whatever the subjective intent' motivating the relevant officials." — 563 U.S. at 736. ^pin-736

"We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive." — [*Id.* at 743](https://www.courtlistener.com/opinion/7344719/ashcroft-v-al-kidd/#:~:text=We%20hold%20that%20an%20objectively). ^pin-743

And [[Qualified Immunity|qualified immunity]] "protects 'all but the plainly incompetent or those who knowingly violate the law.'" — *Id.* (quoting [[Malley v. Briggs]], 475 U.S. at 341).

## Application
A warrant naming only al-Kidd, supported by individualized reasons to believe he was a material witness who might disappear, took the case outside the narrow special-needs/administrative-search exceptions where subjective purpose matters; the general rule that motive is irrelevant therefore governed. Even assuming the pretextual-material-witness theory could state a Fourth Amendment violation, it was not clearly established at the time — eight court-of-appeals judges had agreed with Ashcroft's position in a case of first impression — so he was entitled to [[Qualified Immunity|qualified immunity]], and the Court did not reach whether he also had absolute immunity.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. Subjective intent does not defeat an objectively reasonable, warrant-based arrest, and Ashcroft did not violate clearly established law; he was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *al-Kidd* extends the objective-reasonableness / motive-irrelevance principle of [[Whren v. United States]] beyond the traffic-stop context and is a leading modern statement of the "clearly established" standard within the [[Harlow v. Fitzgerald]] / [[Malley v. Briggs]] qualified-immunity line (its "high level of generality" admonition is quoted in [[Mullenix v. Luna]] and [[Messerschmidt v. Millender]]). No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Ashcroft v. al-Kidd*, 563 U.S. 731 (2011) — https://www.courtlistener.com/opinion/217703/ashcroft-v-al-kidd/ — pinpoints: 736, 743 (CL stores the slip opinion "563 U. S. ____ (2011)"; pins keyed to the official U.S. Reports pages — objective inquiry slip op. 3–4, holding/QI slip op. 12).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b89f609569ade2ca", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ashcroft v. al-Kidd"}, "payload": {"all": [{"cite": "179 L. Ed. 2d 1149", "page": "1149", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "179"}, {"cite": "2011 U.S. LEXIS 4021", "page": "4021", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2011"}, {"cite": "131 S. Ct. 2074", "page": "2074", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "131"}, {"cite": "563 U.S. 731", "page": "731", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "563"}, {"cite": "79 U.S.L.W. 4393", "page": "4393", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "79"}, {"cite": "22 Fla. L. Weekly Fed. S 1057", "page": "1057", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Ashcroft v. al-Kidd"}}
{"assertion_id": "7d1c3945c0ee2c33", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-736", "record_id": "Ashcroft v. al-Kidd"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-736", "pinpoint_status": "slip-only", "quote": "--- # Ashcroft v. al-Kidd *563 U.S. 731 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Abdullah al-Kidd, a U.S. citizen, was arrested in 2003 on a federal material-witness warrant — ostensibly to secure his testimony in a terrorism prosecution — but was never called to testify. He sued former Attorney General John Ashcroft under *Bivens*, alleging that Ashcroft had adopted a policy of using the material-witness statute as a **pretext** to detain terrorism suspects whom the government lacked probable cause to charge, in violation of the Fourth Amendment. Ashcroft asserted qualified immunity. ## Issue Whether an arrest made on a valid material-witness warrant can be challenged as unconstitutional based on the officer's alleged improper subjective motive — and, if the theory is doubtful, whether Ashcroft violated clearly established law. ## Rule Fourth Amendment reasonableness is judged objectively, so subjective motive does not invalidate an otherwise-valid arrest.", "quote_fidelity": "mismatch", "record_id": "Ashcroft v. al-Kidd", "star_marker": null}}
{"assertion_id": "8e3a6291bb8d32d6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-743", "record_id": "Ashcroft v. al-Kidd"}, "payload": {"fragment": "#:~:text=We%20hold%20that%20an%20objectively", "page": null, "pin_id": "pin-743", "pinpoint_status": "star-verified", "quote": "We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive.", "quote_fidelity": "matched", "record_id": "Ashcroft v. al-Kidd", "star_marker": "1161"}}
{"assertion_id": "7530a97a8a4ce4fd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ashcroft v. al-Kidd"}, "payload": {"as_of_content": "2011-05-31", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Ashcroft v. al-Kidd", "scope_note": "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement.", "varies_by_point": false}}
```

### lake record — Ashcroft v. al-Kidd

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ashcroft v. al-Kidd",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ashcroft v. al-Kidd",
    "case_name_short": "al-Kidd",
    "case_name_full": "JOHN D. ASHCROFT v. ABDULLAH al-KIDD",
    "input_case_name": "Ashcroft v. al-Kidd",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-05-31",
    "year": 2011,
    "docket": "10-98",
    "cluster_id": 7344719,
    "lead_opinion_id": 7262676,
    "sibling_ids": [
      7262676,
      7262677,
      7262678,
      7262679
    ],
    "absolute_url": "/opinion/7344719/ashcroft-v-al-kidd/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 217703,
        "score": 110,
        "case_name": "Ashcroft v. al-Kidd"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "179 L. Ed. 2d 1149",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2074",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 731",
        "volume": "563",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4393",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4393",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 1057",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1057",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4021",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "179 L. Ed. 2d 1149",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4021",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2074",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 731",
        "volume": "563",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4393",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4393",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 1057",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1057",
        "type": 1,
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
      "id": "pin-736",
      "page": null,
      "quote": "--- # Ashcroft v. al-Kidd *563 U.S. 731 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Abdullah al-Kidd, a U.S. citizen, was arrested in 2003 on a federal material-witness warrant \u2014 ostensibly to secure his testimony in a terrorism prosecution \u2014 but was never called to testify. He sued former Attorney General John Ashcroft under *Bivens*, alleging that Ashcroft had adopted a policy of using the material-witness statute as a **pretext** to detain terrorism suspects whom the government lacked probable cause to charge, in violation of the Fourth Amendment. Ashcroft asserted qualified immunity. ## Issue Whether an arrest made on a valid material-witness warrant can be challenged as unconstitutional based on the officer's alleged improper subjective motive \u2014 and, if the theory is doubtful, whether Ashcroft violated clearly established law. ## Rule Fourth Amendment reasonableness is judged objectively, so subjective motive does not invalidate an otherwise-valid arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-743",
      "page": null,
      "quote": "We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive.",
      "star_marker": "1161",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 52473,
      "fragment": "#:~:text=We%20hold%20that%20an%20objectively",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-05-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ashcroft v. al-Kidd",
    "varies_by_point": false,
    "scope_note": "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "George Trammell v. Kevin Fruge",
          "cluster_id": 4419631,
          "cite": [
            "868 F.3d 332",
            "2017 WL 3528437",
            "2017 U.S. App. LEXIS 15529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramona Hinojosa v. Brad Livingston",
          "cluster_id": 3155936,
          "cite": [
            "807 F.3d 657",
            "2015 U.S. App. LEXIS 20016",
            "2015 WL 7422990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MacDonald v. Town of Eastham",
          "cluster_id": 2656464,
          "cite": [
            "745 F.3d 8",
            "2014 WL 944707",
            "2014 U.S. App. LEXIS 4618"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Egbert v. Boule",
          "cluster_id": 6475794,
          "cite": [
            "596 U.S. 482",
            "142 S. Ct. 1793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Natasha Whitley v. John Hanna",
          "cluster_id": 1036944,
          "cite": [
            "726 F.3d 631",
            "2013 WL 4029134",
            "2013 U.S. App. LEXIS 16485"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Poole v. City of Shreveport",
          "cluster_id": 806839,
          "cite": [
            "691 F.3d 624",
            "2012 WL 3517357",
            "2012 U.S. App. LEXIS 17243"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DiStiso ex rel. DiStiso v. Cook",
          "cluster_id": 807074,
          "cite": [
            "691 F.3d 226",
            "2012 WL 3570755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derrick Newman v. James Guedry",
          "cluster_id": 3071815,
          "cite": [
            "703 F.3d 757",
            "2012 U.S. App. LEXIS 26205",
            "2012 WL 6634975"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael-Ryan Kruger v. State of Nebraska",
          "cluster_id": 3192229,
          "cite": [
            "820 F.3d 295",
            "2016 U.S. App. LEXIS 6326",
            "2016 WL 1376343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glik v. Cunniffe",
          "cluster_id": 612667,
          "cite": [
            "655 F.3d 78",
            "84 A.L.R. 6th 647",
            "39 Media L. Rep. (BNA) 2257",
            "2011 U.S. App. LEXIS 17841",
            "2011 WL 3769092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Cummings",
          "cluster_id": 4593291,
          "cite": [
            "917 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corey Hughes v. Michael Rodriguez",
          "cluster_id": 6461702,
          "cite": [
            "31 F.4th 1211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pratt Ex Rel. Estate of Pratt v. Harris County",
          "cluster_id": 3200293,
          "cite": [
            "822 F.3d 174",
            "2016 U.S. App. LEXIS 8049",
            "2016 WL 2343032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barbara Wyatt v. Rhonda Fletcher",
          "cluster_id": 873536,
          "cite": [
            "718 F.3d 496",
            "2013 WL 2371280",
            "2013 U.S. App. LEXIS 11045"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lamont Shepard v. T. Quillen",
          "cluster_id": 4315689,
          "cite": [
            "840 F.3d 686",
            "2016 U.S. App. LEXIS 19352",
            "2016 WL 6246873"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Irish v. Fowler",
          "cluster_id": 4803838,
          "cite": [
            "979 F.3d 65"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tucker v. City of Shreveport",
          "cluster_id": 4884106,
          "cite": [
            "998 F.3d 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Susan Doxtator v. Erik O'Brien",
          "cluster_id": 6623081,
          "cite": [
            "39 F.4th 852"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stamps Ex Rel. Estate of Stamps v. Town of Framingham",
          "cluster_id": 3175226,
          "cite": [
            "813 F.3d 27",
            "2016 U.S. App. LEXIS 2026",
            "2016 WL 457153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matalon v. Hynnes",
          "cluster_id": 3155905,
          "cite": [
            "806 F.3d 627",
            "2015 U.S. App. LEXIS 20008",
            "2015 WL 7280627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacob Pfaller v. Mark Amonette",
          "cluster_id": 9344950,
          "cite": [
            "55 F.4th 436"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Drumgold v. Callahan",
          "cluster_id": 816494,
          "cite": [
            "707 F.3d 28",
            "2013 U.S. App. LEXIS 2301",
            "2013 WL 376747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 106,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 106,
        "triage_read": 8,
        "triage_snippet_classified": 98
      },
      "lane2_top_cited": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MiZzPTk0MjE3NjMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287262676+OR+7262677+OR+7262678+OR+7262679%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
    "indexed_citing_opinions": 168,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7262676,
        "count": 168,
        "count_source": "search"
      },
      {
        "opinion_id": 7262677,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7262678,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7262679,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1746,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ashcroft-v-al-kidd.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNDU1NTcmcz05NDEyMTU0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287262676+OR+7262677+OR+7262678+OR+7262679%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T19:06:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:10:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ashcroft v. al-Kidd

```
<opinion type="majority">
<p id="b1252-6">OPINION OF THE COURT</p>
<p id="b1252-7">[<span class="citation no-link">563 U.S. 733</span>]</p>
<author id="b1252-8">Justice Scalia</author>
<p id="AdE0">delivered the opinion of the Court.</p>
<p id="b1252-9">We decide whether a former Attorney General enjoys immunity from suit for allegedly authorizing federal prosecutors to obtain valid material-witness warrants for detention of terrorism suspects whom they would otherwise lack probable cause to arrest.</p>
<p id="b1252-10">I</p>
<p id="b1252-11">The federal material-witness statute authorizes judges to “order the arrest of [a] person” whose testimony “is material in a criminal proceeding ... if it is shown that it may become impracticable to secure the presence of the person by subpoena.” <span class="citation no-link">18 U.S.C. § 3144</span>. Material witnesses enjoy the same constitutional right to pretrial release as other federal detainees, and federal law requires release if their testimony “can adequately be secured by deposition, and if further detention is not necessary to prevent a failure of justice.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b1252-12">[<span class="citation no-link">563 U.S. 734</span>]</p>
<p id="b1252-13">Because this case arises from a motion to dismiss, we accept as true the factual allegations in Abdullah al-Kidd’s complaint. The complaint alleges that, in the aftermath of the September 11th terrorist attacks, then-Attorney General John Ashcroft authorized federal prosecutors and law enforcement officials to use the material-witness statute to detain individuals with suspected ties to terrorist organizations. It is alleged that federal officials had no intention of calling most of these individuals as witnesses, and that they were detained, at Ashcroft’s direction, because federal officials suspected them of supporting terrorism but lacked sufficient evidence to charge them with a crime.</p>
<p id="b1252-19">It is alleged that this pretextual detention policy led to the material-witness arrest of al-Kidd, a native-born United States citizen. FBI agents apprehended him in March 2003 as he checked in for a flight to Saudi Arabia. Two days earlier, federal officials had informed a Magistrate Judge that, if al-Kidd boarded his flight, they believed information “crucial” to the prosecution of Sami Omar al-Hussayen would be lost. App. 64. Al-Kidd remained in federal custody for 16 days and on supervised release until al-Hussayen’s trial concluded 14 months later. Prosecutors never called him as a witness.</p>
<p id="b1252-20">In March 2005, al-Kidd filed this <em>Bivens </em>action, see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span>, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S. Ct. 1999</a></span>, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L. Ed. 2d 619</a></span> (1971), to challenge the constitutionality of Ashcroft’s alleged policy; <page-number citation-index="1" label="1155">*1155</page-number>he also asserted several other claims not relevant here against Ashcroft and others. Ashcroft filed a motion to dismiss based on absolute and qualified immunity, which the District Court denied. A divided panel of the United States Court of Appeals for the Ninth Circuit affirmed, holding that the Fourth Amendment prohibits pre-textual arrests absent probable cause of criminal wrongdoing, and that Ashcroft could not claim qualified or absolute immunity. See <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d 949</a></span> (2009).</p>
<p id="b1253-4">[<span class="citation no-link">563 U.S. 735</span>]</p>
<p id="b1253-5">Judge Bea dissented, <em>id,, </em>at 981, and eight judges dissented from the denial of rehearing en banc, see <span class="citation" data-id="8411499"><a href="/opinion/8440576/al-kidd-v-ashcroft/#1137" aria-description="Citation for case: Al-Kidd v. Ashcroft">598 F.3d 1129, 1137, 1142</a></span> (2010). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.S./562/980/">562 U.S. 980</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/415/">131 S. Ct. 415</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/321/">178 L. Ed. 2d 321</a></span> (2010).</p>
<p id="b1253-6">II</p>
<p id="b1253-7">Qualified immunity shields federal and state officials from money damages unless a plaintiff pleads facts showing (1) that the official violated a statutory or constitutional right, and (2) that the right was “clearly established” at the time of the challenged conduct. <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800, 818</a></span>, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S. Ct. 2727</a></span>, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">73 L. Ed. 2d 396</a></span> (1982). We recently reaffirmed that lower courts have discretion to decide which of the two prongs of qualified-immunity analysis to tackle first. See <em>Pearson </em>v. <em>Callahan, </em><span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#236" aria-description="Citation for case: Pearson v. Callahan">555 U.S. 223, 236</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span> (2009).</p>
<p id="b1253-8">Courts should think carefully before expending “scarce judicial resources” to resolve difficult and novel questions of constitutional or statutory interpretation that will “have no effect on the outcome of the case.” <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#236" aria-description="Citation for case: Pearson v. Callahan"><em>Id., </em>at 236-237</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span>; see <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#237" aria-description="Citation for case: Pearson v. Callahan"><em>id., </em>at 237-242</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span>. When, however, a court of appeals does address both prongs of qualified-immunity analysis, we have discretion to correct its errors at each step. Although not necessary to reverse an erroneous judgment, doing so ensures that courts do not insulate constitutional decisions at the frontiers of the law from our review or inadvertently undermine the values qualified immunity seeks to promote. The former occurs when the constitutional-law question is wrongly decided; the latter when what is not clearly established is held to be so. In this case, the Court of Appeals’ analysis at both steps of the qualified-immunity inquiry needs correction.</p>
<p id="b1253-10">A</p>
<p id="b1253-11">The Fourth Amendment protects “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” An arrest, of course, qualifies as a “seizure” of a “person” under this provision,</p>
<p id="b1253-12">[<span class="citation no-link">563 U.S. 736</span>]</p>
<p id="b1253-13"><em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200, 207-208</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">99 S. Ct. 2248</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L. Ed. 2d 824</a></span> (1979), and so must be reasonable under the circumstances. Al-Kidd does not assert that Government officials would have acted unreasonably if they had used a material-witness warrant to arrest him for the purpose of securing his testimony for trial. See Brief for Respondent 16-17; Tr. of Oral Arg. 20-22. He contests, however (and the Court of Appeals here rejected), the reasonableness of using the warrant to detain him as a suspected criminal.</p>
<p id="b1253-15">Fourth Amendment reasonableness “is predominantly an objective inquiry.” <em>Indianapolis </em>v. <em>Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span> (2000). We ask whether “the circumstances, viewed objectively, justify [the challenged] ac<page-number citation-index="1" label="1156">*1156</page-number>tion.” <em>Scott </em>v. <em>United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 138</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">98 S. Ct. 1717</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L. Ed. 2d 168</a></span> (1978). If so, that action was reasonable <em>“whatever </em>the subjective intent” motivating the relevant officials. <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#814" aria-description="Citation for case: Whren v. United States">517 U.S. 806, 814</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span> (1996). This approach recognizes that the Fourth Amendment regulates conduct rather than thoughts, <em>Bond </em>v. <em>United States, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U.S. 334, 338, n. 2</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">120 S. Ct. 1462</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">146 L. Ed. 2d 365</a></span> (2000); and it promotes evenhanded, uniform enforcement of the law, <em>Devenpeck </em>v. <em>Alford, </em><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/#153" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146, 153-154</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S. Ct. 588</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L. Ed. 2d 537</a></span> (2004).</p>
<p id="b1254-4">Two “limited exception [s]” to this rule are our special-needs and administrative-search cases, where “actual motivations” do matter. <em>United States </em>v. <em>Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#122" aria-description="Citation for case: United States v. Knights">534 U.S. 112, 122</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S. Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L. Ed. 2d 497</a></span> (2001) (internal quotation marks omitted). Ajudicial warrant and probable cause are not needed where the search or seizure is justified by “special needs, beyond the normal need for law enforcement,” such as the need to deter drug use in public schools, <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646, 653</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span> (1995) (internal quotation marks omitted), or the need to ensure that railroad employees engaged in train operations are not under the influence of drugs or alcohol, <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (1989); and where the search or seizure is in execution of an administrative warrant authorizing, for example, an inspection of fire-damaged premises to determine the cause,</p>
<p id="b1254-5">[<span class="citation no-link">563 U.S. 737</span>]</p>
<p id="b1254-6"><em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#294" aria-description="Citation for case: Michigan v. Clifford">464 U.S. 287, 294</a></span>, <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">104 S. Ct. 641</a></span>, <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">78 L. Ed. 2d 477</a></span> (1984) (plurality opinion), or an inspection of residential premises to ensure compliance with a housing code, <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#535" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 535-538</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S. Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L. Ed. 2d 930</a></span> (1967). But those exceptions do not apply where the officer’s purpose is not to attend to the special needs or to the investigation for which the administrative inspection is justified. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><em>Whren, supra, </em>at 811-812</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. The Government seeks to justify the present arrest on the basis of a properly issued judicial warrant—so that the special-needs and administrative-inspection cases cannot be the basis for a purpose inquiry here.</p>
<p id="b1254-9">Apart from those cases, we have almost uniformly rejected invitations to probe subjective intent. See <em>Brigham City </em>v. <em>Stuart, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#404" aria-description="Citation for case: Brigham City v. Stuart">547 U.S. 398, 404</a></span>, <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">126 S. Ct. 1943</a></span>, <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">164 L. Ed. 2d 650</a></span> (2006). There is one category of exception, upon which the Court of Appeals principally relied. In <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond, supra,</a></span> </em>we held that the Fourth Amendment could not condone suspicionless vehicle checkpoints set up for the purpose of detecting illegal narcotics. Although we had previously approved vehicle checkpoints set up for the purpose of keeping off the road unlicensed drivers, <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648, 663</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S. Ct. 1391</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L. Ed. 2d 660</a></span> (1979), or alcohol-impaired drivers, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U.S. 444</a></span>, <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">110 S. Ct. 2481</a></span>, <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">110 L. Ed. 2d 412</a></span> (1990); and for the purpose of interdicting those who illegally cross the border, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S. Ct. 3074</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L. Ed. 2d 1116</a></span> (1976); we found the drug-detection purpose in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>invalidating because it was “ultimately indistinguishable from the general <page-number citation-index="1" label="1157">*1157</page-number>interest in crime control,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 44</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. In the Court of Appeals’ view, <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>established that “ ‘programmatic purpose’ is relevant to Fourth Amendment analysis of programs of seizures without probable cause.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#968" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 968</a></span>.</p>
<p id="b1255-4">That was mistaken. It was not the absence of probable cause that triggered the invalidating-purpose inquiry in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>. </em>To the contrary, <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>explicitly said that it would approve checkpoint stops for “general crime control</p>
<p id="b1255-5">[<span class="citation no-link">563 U.S. 738</span>]</p>
<p id="b1255-6">purposes” that were based upon merely “some quantum of individualized suspicion.” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. Purpose was relevant in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>because  “programmatic purposes may be relevant to the validity of Fourth Amendment intrusions undertaken <em>pursuant to a general scheme without individualized, </em>suspicion,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#45" aria-description="Citation for case: City of Indianapolis v. Edmond"><em>id., </em>at 45-46</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span> (emphasis added).<footnotemark>1</footnotemark></p>
<p id="b1255-7">Needless to say, warrantless, “sus-picionless intrusions pursuant to a general scheme,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond"><em>id., </em>at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>, are far removed from the facts of this case. A warrant issued by a neutral Magistrate Judge authorized al-Kidd’s arrest. The affidavit accompanying the warrant application (as al-Kidd concedes) gave individualized reasons to believe that he was a material witness and that he would soon disappear. The existence of a judicial warrant based on individualized suspicion takes this case outside the domain of not only our special-needs and administrative-search cases, but of <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>as well.</p>
<p id="b1255-9">A warrant based on individualized suspicion<footnotemark>2</footnotemark> in fact grants more protection against the malevolent and the incompetent than existed in most of our cases eschewing inquiries into intent. In <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><em>Whren, supra, </em>at 813</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>, and <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/#153" aria-description="Citation for case: Devenpeck v. Alford"><em>Devenpeck, supra, </em>at 153</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S. Ct. 588</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L. Ed. 2d 537</a></span>, we declined to probe the motives behind seizures supported by probable cause but lacking a warrant approved by a detached magistrate. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 21-22</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S. Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L. Ed. 2d 889</a></span></p>
<p id="b1255-10">[<span class="citation no-link">563 U.S. 739</span>]</p>
<p id="b1255-11">(1968), and <em>Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#121" aria-description="Citation for case: United States v. Knights">534 U.S., at 121-122</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S. Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L. Ed. 2d 497</a></span>, applied an objective standard to war-rantless searches justified by a lesser showing of reasonable suspicion. We review even some suspicionless searches for objective reasonableness. See <em>Bond, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#335" aria-description="Citation for case: Bond v. United States">529 U.S., at 335-336, 338, n. 2</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">120 S. Ct. 1462</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">146 L. Ed. 2d 365</a></span>. If concerns about improper motives and pretext do not justify subjective inquiries in those less protective contexts, we see no reason to adopt that inquiry here.</p>
<p id="b1255-12">Al-Kidd would read our cases more narrowly. He asserts that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>es<page-number citation-index="1" label="1158">*1158</page-number>tablishes that we ignore subjective intent only when there exists “probable cause to believe that a violation of law has occurred,” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States">517 U.S., at 811</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, 135 L. Ed. 2d 89— which was not the case here. That is a distortion of <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>. </em>Our unanimous opinion held that we would not look behind an objectively reasonable traffic stop to determine whether racial profiling or a desire to investigate other potential crimes was the real motive. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 810, 813</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. In the course of our analysis, we dismissed Whren’s reliance on our inventory-search and administrative-inspection cases by explaining that those cases do not “endors[e] the principle that ulterior motives can invalidate police conduct that is justifiable on the basis of probable cause to believe that a violation of law has occurred,” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 811</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span> But to say that ulterior motives do <em>not </em>invalidate a search that is legitimate because of probable cause to believe a crime has occurred is not to say that it <em>does </em>invalidate all searches that are legitimate for other reasons.</p>
<p id="b1256-4">“[0]nly an undiscerning reader,” <em>ibid., </em>would think otherwise. We referred to probable cause to believe that a violation of law had occurred because that was the legitimating factor in the case at hand. But the analysis of our opinion swept broadly to reject inquiries into motive generally. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 812-815</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. We remarked that our special-needs and administrative-inspection cases are unusual in their concern for pretext, and do nothing more than “explain that the exemption from the need for probable cause (and warrant), which is accorded to searches made for the purpose of inventory</p>
<p id="b1256-6">[<span class="citation no-link">563 U.S. 740</span>]</p>
<p id="b1256-7">or administrative regulation, is not accorded to searches that are <em>not </em>made for those purposes,” <span class="citation no-link"><em>id., </em>at 811-812</span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. And our opinion emphasized that we had at that time (prior to <em>Edmond) </em>rejected every request to examine subjective intent outside the narrow context of special needs and administrative inspections. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U.S., at 812</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. Thus, al-Kidd’s approach adds an “only” to a sentence plucked from the <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>opinion, and then elevates that sentence (as so revised) over the remainder of the opinion, and over the consistent holdings of our other cases.</p>
<p id="b1256-8">Because al-Kidd concedes that individualized suspicion supported the issuance of the material-witness arrest warrant; and does not assert that his arrest would have been unconstitutional absent the alleged pretextual use of the warrant; we find no Fourth Amendment violation.<footnotemark>3</footnotemark> Efficient<footnotemark>4</footnotemark> and evenhanded application of the law de<page-number citation-index="1" label="1159">*1159</page-number>mands that we look to whether the arrest is objectively justified, rather than to the motive of the arresting officer.</p>
<p id="b1257-4">[<span class="citation no-link">563 U.S. 741</span>]</p>
<p id="b1257-5">B</p>
<p id="b1257-6">A Government official’s conduct violates clearly established law when, at the time of the challenged conduct, “[t]he contours of [a] right [are] sufficiently clear” that every “reasonable official would [have understood] that what he is doing violates that right.” <em>Anderson </em>v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635, 640</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">107 S. Ct. 3034</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">97 L. Ed. 2d 523</a></span> (1987). We do not require a case directly on point, but existing precedent must have placed the statutory or constitutional question beyond debate. See <em>ibid.; Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U.S. 335, 341</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">106 S. Ct. 1092</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">89 L. Ed. 2d 271</a></span> (1986). The constitutional question in this case falls far short of that threshold.</p>
<p id="b1257-7">At the time of al-Kidd’s arrest, not a single judicial opinion had held that pretext could render an objectively reasonable arrest pursuant to a material-witness warrant unconstitutional. A district-court opinion had suggested, in a footnoted dictum devoid of supporting citation, that using such a warrant for preventive detention of suspects “is an illegitimate use of the statute”—implying (we accept for the sake of argument) that the detention would therefore be unconstitutional. Uni<em>ted States </em>v. <em>Awadallah, </em><span class="citation" data-id="2518594"><a href="/opinion/2518594/united-states-v-awadallah/#77" aria-description="Citation for case: United States v. Awadallah">202 F. Supp. 2d 55, 77, n. 28</a></span> (SDNY 2002). The Court of Appeals thought nothing could “have given John Ashcroft fair[er] warning” that his conduct violated the Fourth Amendment, because the footnoted dictum <em>“callfed] out Ashcroft by name”! </em><span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#972" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 972-973</a></span> (internal quotation marks omitted; emphasis added). We will indulge the assumption (though it does not seem to us realistic) that Justice Department lawyers bring to the Attorney General’s personal attention all district judges’ footnoted speculations that boldly “call him out by name.” On that assumption, would it prove that for him (and for him only?) it became clearly established that pretextual use of the material-witness statute rendered the arrest unconstitutional? An extraordinary proposition. Even a district judge’s <em>ipse dixit </em>of a holding is not “controlling authority” in any jurisdiction, much less in the entire United States; and his <em>ipse dixit </em>of a footnoted dictum falls far short</p>
<p id="AuOq">[<span class="citation no-link">563 U.S. 742</span>]</p>
<p id="b1257-9">of what is necessary absent controlling authority: a robust “consensus of cases of persuasive authority.” <em>Wilson </em>v. <em>Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#617" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 617</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span> (1999).</p>
<p id="b1257-11">The Court of Appeals’ other cases “clearly establishing” the constitutional violation are, of course, those we rejected as irrelevant in our discussion of whether there was any constitutional violation at all. And the Court of Appeals’ reference to those cases here makes the same error of assuming that purpose is only disregarded when there is probable cause to suspect a violation of law.</p>
<p id="b1257-12">The Court of Appeals also found clearly established law lurking in the broad “history and purposes of the Fourth Amendment.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#971" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 971</a></span>. We have repeatedly told courts— <page-number citation-index="1" label="1160">*1160</page-number>and the Ninth Circuit in particular, see <em>Brosseau </em>v. <em>Haugen, </em><span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/#198" aria-description="Citation for case: Brosseau v. Haugen">543 U.S. 194, 198-199</a></span>, <span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">125 S. Ct. 596</a></span>, <span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">160 L. Ed. 2d 583</a></span> (2004) <em>(per </em>curiam)—not to define clearly established law at a high level of generality. See also, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne"><em>e.g., Wilson, supra, </em>at 615</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>; <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 639-640</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">107 S. Ct. 3034</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">97 L. Ed. 2d 523</a></span>; cf. <em>Sawyer </em>v. <em>Smith, </em><span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/#236" aria-description="Citation for case: Sawyer v. Smith">497 U.S. 227, 236</a></span>, <span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/" aria-description="Citation for case: Sawyer v. Smith">110 S. Ct. 2822</a></span>, <span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/" aria-description="Citation for case: Sawyer v. Smith">111 L. Ed. 2d 193</a></span> (1990). The general proposition, for example, that an unreasonable search or seizure violates the Fourth Amendment is of little help in determining whether the violative nature of particular conduct is clearly established. See <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span>, 201-202, <span class="citation multiple-matches"><a href="/c/S.%20Ct./121/2151/">121 S. Ct. 2151</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/150/272/">150 L. Ed. 2d 272</a></span> (2001); <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne"><em>Wilson, supra, </em>at 615</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>.</p>
<p id="b1258-4">The same is true of the Court of Appeals’ broad historical assertions. The Fourth Amendment was a response to the English Crown’s use of general warrants, which often allowed royal officials to search and seize whatever and whomever they pleased while investigating crimes or affronts to the Crown. See <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 481-485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S. Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L. Ed. 2d 431</a></span> (1965). According to the Court of Appeals, Ashcroft should have seen that a pre-textual warrant similarly “gut[s] the substantive protections of the Fourth Amendmen[t]” and allows the State “to arrest upon the executive’s mere suspicion.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#972" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 972</a></span>.</p>
<p id="b1258-5">Ashcroft must be forgiven for missing the parallel, which escapes us as well. The principal evil of the general warrant</p>
<p id="b1258-6">[<span class="citation no-link">563 U.S. 743</span>]</p>
<p id="b1258-7">was addressed by the Fourth Amendment’s particularity requirement, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><em>Stanford, supra, </em>at 485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S. Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L. Ed. 2d 431</a></span>, which Ashcroft’s alleged policy made no effort to evade. The warrant authorizing al-Kidd’s arrest named al-Kidd and only al-Kidd. It might be argued, perhaps, that when, in response to the English abuses, the Fourth Amendment said that warrants could only issue “on probable cause” it meant only probable cause to suspect a violation of law, and not probable cause to believe that the individual named in the warrant was a material witness. But that would make <em>all </em>arrests pursuant to material-witness warrants unconstitutional, whether pretextual or not—and that is not the position taken by al-Kidd in this case.</p>
<p id="b1258-9">While featuring a District Court’s footnoted dictum, the Court of Appeals made no mention of this Court’s affirmation in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>of the “pre-dominan [t]” rule that reasonableness is an objective inquiry, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. Nor did it mention <em>Whren’s </em>and <em>Knights’ </em>statements that subjective intent mattered in a very limited subset of our Fourth Amendment cases; or <em>Terry’s </em>objective evaluation of investigatory searches premised on reasonable suspicion rather than probable cause; or <em>Bond’s </em>objective evaluation of a suspicionless investigatory search. The Court of Appeals seems to have cherry-picked the aspects of our opinions that gave colorable support to the proposition that the unconstitutionality of the action here was clearly established.</p>
<p id="b1258-10">Qualified immunity gives government officials breathing room to make reasonable but mistaken judgments about open legal questions. When properly applied, it protects “all but the plainly incompetent or those who knowingly violate the law.” <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 341</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">106 S. Ct. 1092</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">89 L. Ed. 2d 271</a></span>. Ashcroft deserves neither label, not least because eight Court of Appeals judges agreed with <page-number citation-index="1" label="1161">*1161</page-number>his judgment in a case of first impression. See <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#618" aria-description="Citation for case: Wilson v. Layne"><em>Wilson, supra, </em>at 618</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>. He deserves qualified immunity even assuming—contrafactually—that his alleged detention policy violated the Fourth Amendment.</p>
<p id="b1259-4">[<span class="citation no-link">563 U.S. 744</span>]</p>
<p id="pArzU">
<img class="p" height="36" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ8AAAAlAQAAAAB0FFF3AAAAlElEQVR4nO3Ouw3CUAyF4T8WooWGHpiAFZiKMWAjxCx0VOkSoeBDh6/iK4WCgiLuPuv4gSTdVdQYbsBzceFTGQZ062jWIKk/rWJ1ghuwvB5isAJJupUfjuEGsC/OVyBJm3JwDDfgtdvGXIYBw7GNbgWS2u4cqxO8Efijj+UJMsCG4nyGMVlfRBpNJfSbQ3Nkjvxl5A3isMVNie1/OQAAAABJRU5ErkJggg==" width="271"/>
</p>
<p id="b1259-5">We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive. Because Ashcroft did not violate clearly established law, we need not address the more difficult question whether he enjoys absolute immunity. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b1259-7">It is so ordered.</p>
<p id="Acxs">Justice Kagan took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b1255-13">. The Court of Appeals also relied upon <em>Ferguson </em>v. <em>Charleston, </em><span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">532 U.S. 67</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">121 S. Ct. 1281</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">149 L. Ed. 2d 205</a></span> (2001), which held unconstitutional a program of mandatory drug testing of maternity patients. Like <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>, </em>that case involved a general scheme of searches without individualized suspicion. <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/#77" aria-description="Citation for case: Ferguson v. City of Charleston">532 U.S., at 77, n. 10</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">121 S. Ct. 1281</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">149 L. Ed. 2d 205</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b1255-14">. Justice Ginsburg suggests that our use of the word “suspicion” is peculiar because that word “ordinarily” means “that the person suspected has engaged in wrongdoing.” <em>Post, </em>at 749, n. 3, 179 L. Ed. 2d, at 1164 (opinion concurring in judgment). We disagree. No usage of the word is more common and idiomatic than a statement such as “I have a suspicion he knows something about the crime,” or even “I have a suspicion she is throwing me a surprise birthday party.” The many cases cited by Justice Ginsburg, <em>post, </em>at 749-750, n. 3, 179 L. Ed. 2d, at 1164-1165, which use the neutral word “suspicion” <em>in connection with </em>wrongdoing, prove nothing except that searches and seizures for reasons other than suspected wrongdoing are rare.</p>
</footnote>
<footnote label="3">
<p id="b1256-9">. The concerns of Justices Ginsburg and Sotomayor about the validity of the warrant in this case are beside the point. See <em>post, </em>at 748-749, 179 L. Ed. 2d, at 1163-1164 (Ginsburg, J., concurring in judgment); <em>post, </em>at 752, 179 L. Ed. 2d, at 1166 (Sotomayor, J., concurring in judgment). The validity of the warrant is not <em>our </em>“opening assumption,’’ <em>post, </em>at 749, 179 L. Ed. 2d, at 1164 (Ginsburg, J., concurring in judgment); it is the premise of al-Kidd’s argument. Al-Kidd does not claim that Ashcroft is liable because the FBI agents failed to obtain a valid warrant. He takes the validity of the warrant as a given, and argues that his arrest nevertheless violated the Constitution because it was motivated by an illegitimate purpose. His separate Fourth Amendment and statutory claims against the FBI agents who sought the material-witness warrant, which are the focus of both concurrences, are not before us.</p>
</footnote>
<footnote label="4">
<p id="b1256-10">. We may note in passing that al-Kidd alleges that the Attorney General authorized the use of material-witness warrants for detention of suspected terrorists, but not that he forbade the use of <page-number citation-index="1" label="1159">*1159</page-number>those warrants to detain material witnesses. Which means that if al-Kidd’s inquiry into actual motive is accepted, mere determination that the Attorney General promulgated the alleged policy would not alone decide the case. Al-Kidd would also have to prove that the officials who sought his material-arrest warrant were motivated by Ashcroft’s policy, not by a desire to call al-Kidd as a witness.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Atwater v. City of Lago Vista.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Atwater v. City of Lago Vista"
type: case
citation: ""
parallel_cite: "532 U.S. 318; 121 S. Ct. 1536; 149 L. Ed. 2d 549; 2001 Daily Journal DAR 3953; 2001 Colo. J. C.A.R. 2069; 14 Fla. L. Weekly Fed. S 193; 69 U.S.L.W. 4262"
neutral_cite: "2001 U.S. LEXIS 3366; 2001 Cal. Daily Op. Serv. 3203"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-04-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-04-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Atwater v. City of Lago Vista
  varies_by_point: false
  scope_note: "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2620702/atwater-v-city-of-lago-vista/"
  cluster_id: 2620702
  opinion_id: 2620702
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — Anchor (minor-offense custodial arrest on probable cause)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Whren v. United States]]", "[[Arkansas v. Sullivan]]", "[[Devenpeck v. Alford]]", "[[Tennessee v. Garner]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "misdemeanor", "seizure"]
holding: "A warrantless custodial arrest for a fine-only misdemeanor committed in the officer's presence, supported by probable cause, does not violate the Fourth Amendment; probable cause governs all arrests without individualized balancing."
lake:
  record_id: Atwater v. City of Lago Vista
  status: verified
  projected_at: 2026-07-06
---

# Atwater v. City of Lago Vista

*532 U.S. 318 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gail Atwater was driving her pickup in Lago Vista, Texas, with her two young children; none of them was wearing a seatbelt, a misdemeanor punishable under Texas law only by a fine. Officer Turek stopped her, and rather than issue a citation, he handcuffed her, placed her in his squad car, and took her to the police station, where she was booked — required to remove her shoes, jewelry, and glasses, photographed, and held in a cell for about an hour before being taken to a magistrate and released on bond. She ultimately pleaded no contest and paid a $50 fine, then sued the City, the police chief, and Officer Turek under 42 U.S.C. § 1983, contending the custodial arrest was an unreasonable seizure.

## Issue
Whether the Fourth Amendment forbids a warrantless custodial arrest, supported by probable cause, for a minor criminal offense — such as a misdemeanor seatbelt violation punishable only by a fine — committed in the officer's presence.

## Rule
No. Probable cause governs all arrests, without case-by-case balancing: the Court "confirm[ed] today what our prior cases have intimated: the standard of probable cause 'applie[s] to all arrests, without the need to "balance" the interests and circumstances involved in particular situations.' . . . If an officer has probable cause to believe that an individual has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender." — 532 U.S. at 354. ^pin-354

That categorical rule yields to individualized review only where an arrest is "conducted in an extraordinary manner, unusually harmful to [the arrestee's] privacy or even physical interests" (quoting *Whren v. United States*).

## Application
There was no dispute that Officer Turek had probable cause: Atwater admitted that neither she nor her children were belted, a crime committed in his presence, so he was "authorized (not required, but authorized) to make a custodial arrest without balancing costs and benefits or determining whether or not Atwater's arrest was in some sense necessary." Nor was the arrest carried out in an extraordinary manner — she was handcuffed, taken to the station, booked in the ordinary way, and held about an hour before release on bond. As the Court concluded: "The arrest and booking were inconvenient and embarrassing to Atwater, but not so extraordinary as to violate the Fourth Amendment." — *Id.* at 355. ^pin-355

## Conclusion
The warrantless custodial arrest for the fine-only seatbelt offense, supported by probable cause and executed in an ordinary manner, was reasonable; the [[Reading and Citing Cases#en-banc|en banc]] Court of Appeals' judgment for the defendants was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Atwater*'s categorical rule is extended by [[Virginia v. Moore]] (an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law) and is consistent with the objective, motive-irrelevant approach of [[Whren v. United States]], [[Arkansas v. Sullivan]] (its same-day companion), and [[Devenpeck v. Alford]].

## Appears on
- [[Arrest and Arrest Warrants]] — *Key — Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Atwater v. City of Lago Vista*, 532 U.S. 318 (2001) — https://www.courtlistener.com/opinion/2620702/atwater-v-city-of-lago-vista/ — pinpoints: 354, 355.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a2f25d9c4edd410a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Atwater v. City of Lago Vista"}, "payload": {"all": [{"cite": "532 U.S. 318", "page": "318", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "532"}, {"cite": "121 S. Ct. 1536", "page": "1536", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "149 L. Ed. 2d 549", "page": "549", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "149"}, {"cite": "2001 U.S. LEXIS 3366", "page": "3366", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}, {"cite": "2001 Daily Journal DAR 3953", "page": "3953", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2001"}, {"cite": "2001 Colo. J. C.A.R. 2069", "page": "2069", "reporter": "Colo. J. C.A.R.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2001"}, {"cite": "14 Fla. L. Weekly Fed. S 193", "page": "193", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "14"}, {"cite": "69 U.S.L.W. 4262", "page": "4262", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "69"}, {"cite": "2001 Cal. Daily Op. Serv. 3203", "page": "3203", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Atwater v. City of Lago Vista"}}
{"assertion_id": "03061ed34a3c9367", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-355", "record_id": "Atwater v. City of Lago Vista"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-355", "pinpoint_status": "slip-only", "quote": "(quoting *Whren v. United States*). ## Application There was no dispute that Officer Turek had probable cause: Atwater admitted that neither she nor her children were belted, a crime committed in his presence, so he was", "quote_fidelity": "mismatch", "record_id": "Atwater v. City of Lago Vista", "star_marker": null}}
{"assertion_id": "77fbd374ff210c4b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-354", "record_id": "Atwater v. City of Lago Vista"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-354", "pinpoint_status": "slip-only", "quote": "--- # Atwater v. City of Lago Vista *532 U.S. 318 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gail Atwater was driving her pickup in Lago Vista, Texas, with her two young children; none of them was wearing a seatbelt, a misdemeanor punishable under Texas law only by a fine. Officer Turek stopped her, and rather than issue a citation, he handcuffed her, placed her in his squad car, and took her to the police station, where she was booked — required to remove her shoes, jewelry, and glasses, photographed, and held in a cell for about an hour before being taken to a magistrate and released on bond. She ultimately pleaded no contest and paid a $50 fine, then sued the City, the police chief, and Officer Turek under 42 U.S.C. § 1983, contending the custodial arrest was an unreasonable seizure. ## Issue Whether the Fourth Amendment forbids a warrantless custodial arrest, supported by probable cause, for a minor criminal offense — such as a misdemeanor seatbelt violation punishable only by a fine — committed in the officer's presence. ## Rule No. Probable cause governs all arrests, without case-by-case balancing: the Court", "quote_fidelity": "mismatch", "record_id": "Atwater v. City of Lago Vista", "star_marker": null}}
{"assertion_id": "a72dfe1c5d84893f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Atwater v. City of Lago Vista"}, "payload": {"as_of_content": "2001-04-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Atwater v. City of Lago Vista", "scope_note": "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008).", "varies_by_point": false}}
```

### lake record — Atwater v. City of Lago Vista

```json
{
  "schema_version": "s2.v1",
  "record_id": "Atwater v. City of Lago Vista",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Atwater v. City of Lago Vista",
    "case_name_short": "Atwater",
    "case_name_full": "ATWATER Et Al. v. CITY OF LAGO VISTA Et Al.",
    "input_case_name": "Atwater v. City of Lago Vista",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-04-24",
    "year": 2001,
    "docket": null,
    "cluster_id": 2620702,
    "lead_opinion_id": 2620702,
    "sibling_ids": [
      2620702,
      9795084,
      9795085
    ],
    "absolute_url": "/opinion/2620702/atwater-v-city-of-lago-vista/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9199445,
        "score": 10,
        "case_name": "Atwater v. City of Lago Vista"
      },
      {
        "cluster_id": 9199444,
        "score": 10,
        "case_name": "Atwater v. City of Lago Vista"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "532 U.S. 318",
        "volume": "532",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1536",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1536",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 549",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "549",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 3953",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "3953",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 2069",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "2069",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 193",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4262",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4262",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 3366",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "3366",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Cal. Daily Op. Serv. 3203",
        "volume": "2001",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3203",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 318",
        "volume": "532",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1536",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1536",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 549",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "549",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 3366",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "3366",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 3953",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "3953",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 2069",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "2069",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 193",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4262",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4262",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Cal. Daily Op. Serv. 3203",
        "volume": "2001",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3203",
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
      "id": "pin-354",
      "page": null,
      "quote": "--- # Atwater v. City of Lago Vista *532 U.S. 318 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gail Atwater was driving her pickup in Lago Vista, Texas, with her two young children; none of them was wearing a seatbelt, a misdemeanor punishable under Texas law only by a fine. Officer Turek stopped her, and rather than issue a citation, he handcuffed her, placed her in his squad car, and took her to the police station, where she was booked \u2014 required to remove her shoes, jewelry, and glasses, photographed, and held in a cell for about an hour before being taken to a magistrate and released on bond. She ultimately pleaded no contest and paid a $50 fine, then sued the City, the police chief, and Officer Turek under 42 U.S.C. \u00a7 1983, contending the custodial arrest was an unreasonable seizure. ## Issue Whether the Fourth Amendment forbids a warrantless custodial arrest, supported by probable cause, for a minor criminal offense \u2014 such as a misdemeanor seatbelt violation punishable only by a fine \u2014 committed in the officer's presence. ## Rule No. Probable cause governs all arrests, without case-by-case balancing: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-355",
      "page": null,
      "quote": "(quoting *Whren v. United States*). ## Application There was no dispute that Officer Turek had probable cause: Atwater admitted that neither she nor her children were belted, a crime committed in his presence, so he was",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-04-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Atwater v. City of Lago Vista",
    "varies_by_point": false,
    "scope_note": "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Buckley",
          "cluster_id": 4468007,
          "cite": [
            "90 N.E.3d 767",
            "478 Mass. 861"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Stephens v. Nick Degiovanni, individually",
          "cluster_id": 4379656,
          "cite": [
            "852 F.3d 1298",
            "2017 U.S. App. LEXIS 5548",
            "2017 WL 1174381"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phyllis J. May v. City of Nahunta, Georgia",
          "cluster_id": 4339893,
          "cite": [
            "846 F.3d 1320",
            "2017 WL 218838",
            "2017 U.S. App. LEXIS 985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Pegg v. Grant Herrnberger",
          "cluster_id": 4335908,
          "cite": [
            "845 F.3d 112",
            "2017 WL 35722",
            "2017 U.S. App. LEXIS 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ted Phillips",
          "cluster_id": 4250252,
          "cite": [
            "834 F.3d 1176",
            "2016 WL 4435613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Campuzano",
          "cluster_id": 7428164,
          "cite": [
            "237 Cal. App. Supp. 4th 14",
            "188 Cal. Rptr. 3d 587",
            "2015 Cal. App. LEXIS 489"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florence v. Board of Chosen Freeholders of County of Burlington",
          "cluster_id": 626454,
          "cite": [
            "182 L. Ed. 2d 566",
            "132 S. Ct. 1510",
            "566 U.S. 318",
            "2012 U.S. LEXIS 2712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Deville v. Marcantel",
          "cluster_id": 65780,
          "cite": [
            "567 F.3d 156",
            "2009 U.S. App. LEXIS 9403",
            "2009 WL 1162586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxine Veatch v. Bartels Lutheran Home",
          "cluster_id": 181829,
          "cite": [
            "627 F.3d 1254",
            "2010 U.S. App. LEXIS 26270",
            "2010 WL 5293814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melvin Alan Wood v. Michael Kesler, individually and in his capacity as an Alabama State Trooper, Brian Jones",
          "cluster_id": 76122,
          "cite": [
            "323 F.3d 872",
            "2003 U.S. App. LEXIS 3857",
            "2003 WL 722756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy Williams v. Brandon Brooks",
          "cluster_id": 3167211,
          "cite": [
            "809 F.3d 936",
            "2016 U.S. App. LEXIS 68",
            "2016 WL 51409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aguilar",
          "cluster_id": 2650810,
          "cite": [
            "2013 IL 112116"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2620702 OR 9795084 OR 9795085) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzU1ODc1MjAwMDAwJnM9ODcyMTU0MSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282620702+OR+9795084+OR+9795085%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2620702 OR 9795084 OR 9795085)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTMmcz03OTI1MDUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282620702+OR+9795084+OR+9795085%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2620702 OR 9795084 OR 9795085)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 0,
        "triage_snippet_classified": 35
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2620702 OR 9795084 OR 9795085)",
    "indexed_citing_opinions": 701,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2620702,
        "count": 612,
        "count_source": "search"
      },
      {
        "opinion_id": 9795084,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9795085,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/atwater-v-city-of-lago-vista.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NjkwNiZzPTk0NTA1NDUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%282620702+OR+9795084+OR+9795085%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2620702,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 96744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 546349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 3585438,
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
    "date_created": "2026-07-04T19:10:49Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:16:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Atwater v. City of Lago Vista (truncated)

```
<div>
<center><b><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span> (2001)</b></center>
<center><h1>ATWATER et al.<br>
v.<br>
CITY OF LAGO VISTA et al.</h1></center>
<center>No. 99-1408.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued December 4, 2000.</center>
<center>Decided April 24, 2001.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
<p><span class="star-pagination">*320</span> <span class="star-pagination">*320</span> <span class="star-pagination">*321</span> <span class="star-pagination">*322</span> Souter, J., delivered the opinion of the Court, in which Rehnquist, C. J., and Scalia, Kennedy, and Thomas, JJ., joined. O'Connor, J., filed a dissenting opinion, in which Stevens, Ginsburg, and Breyer, JJ., joined, <i>post,</i> p. 360.</p>
<p><i>Robert C. DeCarli</i> argued the cause for petitioners. With him on the briefs were <i>Debra Irwin, Pamela McGraw,</i> and <i>Michael F. Sturley.</i> </p>
<p><i>R. James George, Jr.,</i> argued the cause for respondents. With him on the brief were <i>William W. Krueger III</i> and <i>Joanna R. Lippman.</i> </p>
<p><i>Gregory S. Coleman,</i> Solicitor General of Texas, argued the cause for the State of Texas et al. as <i>amici curiae</i> urging affirmance. With him on the brief were <i>John Cornyn,</i> Attorney General, <i>Andy Taylor,</i> First Assistant Attorney General, and <i>Lisa R. Eskow,</i> Assistant Attorney General, and the Attorneys General for their respective States as follows: <i>Mark Pryor</i> of Arkansas, <i>Ken Salazar</i> of Colorado, <i>M. Jane Brady</i> of Delaware, <i>Carla J. Stovall</i> of Kansas, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Joseph P. Mazurek</i> of Montana, <span class="star-pagination">*323</span> <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Charles M. Condon</i> of South Carolina, and <i>Mark L. Earley</i> of Virginia.<sup>[*]</sup></p>
<p>Justice Souter, delivered the opinion of the Court.</p>
<p>The question is whether the Fourth Amendment forbids a warrantless arrest for a minor criminal offense, such as a misdemeanor seatbelt violation punishable only by a fine. We hold that it does not.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>In Texas, if a car is equipped with safety belts, a frontseat passenger must wear one, <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span>(a) (1999), and the driver must secure any small child riding in front, § 545.413(b). Violation of either provision is "a misdemeanor punishable by a fine not less than $25 or more than $50." § 545.413(d). Texas law expressly authorizes "[a]ny peace officer [to] arrest without warrant a person found committing a violation" of these seatbelt laws, § 543.001, although it permits police to issue citations in lieu of arrest, §§ 543.003-543.005.</p>
<p>In March 1997, petitioner Gail Atwater was driving her pickup truck in Lago Vista, Texas, with her 3-year-old son and 5-year-old daughter in the front seat. None of them was <span class="star-pagination">*324</span> wearing a seatbelt. Respondent Bart Turek, a Lago Vista police officer at the time, observed the seatbelt violations and pulled Atwater over. According to Atwater's complaint (the allegations of which we assume to be true for present purposes), Turek approached the truck and "yell[ed]" something to the effect of "[w]e've met before" and "[y]ou're going to jail." App. 20.<sup>[1]</sup> He then called for backup and asked to see Atwater's driver's license and insurance documentation, which state law required her to carry. <span class="citation no-link">Tex. Transp. Code Ann. §§ 521.025</span>, 601.053 (1999). When Atwater told Turek that she did not have the papers because her purse had been stolen the day before, Turek said that he had "heard that story two-hundred times." App. 21.</p>
<p>Atwater asked to take her "frightened, upset, and crying" children to a friend's house nearby, but Turek told her, "[y]ou're not going anywhere." <i><span class="citation no-link">Ibid.</span></i> As it turned out, Atwater's friend learned what was going on and soon arrived to take charge of the children. Turek then handcuffed Atwater, placed her in his squad car, and drove her to the local police station, where booking officers had her remove her shoes, jewelry, and eyeglasses, and empty her pockets. Officers took Atwater's "mug shot" and placed her, alone, in a jail cell for about one hour, after which she was taken before a magistrate and released on $310 bond.</p>
<p>Atwater was charged with driving without her seatbelt fastened, failing to secure her children in seatbelts, driving without a license, and failing to provide proof of insurance. She ultimately pleaded no contest to the misdemeanor seatbelt offenses and paid a $50 fine; the other charges were dismissed.</p>
<p></p>
<h2>
<span class="star-pagination">*325</span> B</h2>
<p>Atwater and her husband, petitioner Michael Haas, filed suit in a Texas state court under <span class="citation no-link">42 U. S. C. § 1983</span> against Turek and respondents City of Lago Vista and Chief of Police Frank Miller. So far as concerns us, petitioners (whom we will simply call Atwater) alleged that respondents (for simplicity, the City) had violated Atwater's Fourth Amendment "right to be free from unreasonable seizure," App. 23, and sought compensatory and punitive damages.</p>
<p>The City removed the suit to the United States District Court for the Western District of Texas. Given Atwater's admission that she had "violated the law" and the absence of any allegation "that she was harmed or detained in any way inconsistent with the law," the District Court ruled the Fourth Amendment claim "meritless" and granted the City's summary judgment motion. No. A-97 CA 679 SS (WD Tex., Feb. 13, 1999), App. to Pet. for Cert. 50a63a. A panel of the United States Court of Appeals for the Fifth Circuit reversed. <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">165 F. 3d 380</a></span> (1999). It concluded that "an arrest for a first-time seat belt offense" was an unreasonable seizure within the meaning of the Fourth Amendment, <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/#387" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>id.,</i> at 387</a></span>, and held that Turek was not entitled to qualified immunity, <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/#389" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>id.,</i> at 389</a></span>.</p>
<p>Sitting en banc, the Court of Appeals vacated the panel's decision and affirmed the District Court's summary judgment for the City. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d 242</a></span> (CA5 1999). Relying on <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), the en banc court observed that, although the Fourth Amendment generally requires a balancing of individual and governmental interests, where "an arrest is based on probable cause then `with rare exceptions . . .the result of that balancing is not in doubt.' " <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 244</a></span> (quoting <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#817" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i> at 817</a></span>). Because "[n]either party dispute[d] that Officer Turek had probable cause to arrest Atwater," and because "there [was] no evidence in the record that Officer Turek conducted the arrest in an `extraordinary manner, unusually harmful' to Atwater's <span class="star-pagination">*326</span> privacy interests," the en banc court held that the arrest was not unreasonable for Fourth Amendment purposes. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 245</a></span>-246 (quoting <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i> at 818</a></span>).</p>
<p>Three judges issued dissenting opinions. On the understanding that citation is the "usual procedure" in a traffic stop situation, Judge Reynaldo Garza thought Atwater's arrest unreasonable, since there was no particular reason for taking her into custody. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/#246" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 246-247</a></span>. Judge Weiner likewise believed that "even with probable cause, [an] officer must have a plausible, articulable reason" for making a custodial arrest. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/#251" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>Id.,</i> at 251</a></span>. Judge Dennis understood the Fourth Amendment to have incorporated an earlier, common-law prohibition on warrantless arrests for misdemeanors that do not amount to or involve a "breach of the peace." <i><span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">Ibid.</a></span></i> </p>
<p>We granted certiorari to consider whether the Fourth Amendment, either by incorporating common-law restrictions on misdemeanor arrests or otherwise, limits police officers' authority to arrest without warrant for minor criminal offenses. <span class="citation multiple-matches"><a href="/c/U.%20S./530/1260/">530 U. S. 1260</a></span> (2000). We now affirm.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment safeguards "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." In reading the Amendment, we are guided by "the traditional protections against unreasonable searches and seizures afforded by the common law at the time of the framing," <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#931" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 931</a></span> (1995), since "[a]n examination of the common-law understanding of an officer's authority to arrest sheds light on the obviously relevant, if not entirely dispositive, consideration of what the Framers of the Amendment might have thought to be reasonable," <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 591</a></span> (1980) (footnote omitted). Thus, the first step here is to assess Atwater's claim that peace officers' authority to make warrantless arrests for misdemeanors was <span class="star-pagination">*327</span> restricted at common law (whether "common law" is understood strictly as law judicially derived or, instead, as the whole body of law extant at the time of the framing). Atwater's specific contention is that "founding-era common-law rules" forbade peace officers to make warrantless misdemeanor arrests except in cases of "breach of the peace," a category she claims was then understood narrowly as covering only those nonfelony offenses "involving or tending toward violence." Brief for Petitioners 13. Although her historical argument is by no means insubstantial, it ultimately fails.</p>
<p></p>
<h2>A</h2>
<p>We begin with the state of pre-founding English common law and find that, even after making some allowance for variations in the common-law usage of the term "breach of the peace,"<sup>[2]</sup> the "founding-era common-law rules" were not <span class="star-pagination">*328</span> nearly as clear as Atwater claims; on the contrary, the common-law commentators (as well as the sparsely reported cases) reached divergent conclusions with respect to officers' warrantless misdemeanor arrest power. Moreover, in the years leading up to American independence, Parliament repeatedly extended express warrantless arrest authority to cover misdemeanor-level offenses not amounting to or involving any violent breach of the peace.</p>
<p></p>
<h2>1</h2>
<p>Atwater's historical argument begins with our quotation from Halsbury in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), that</p>
<blockquote>"`[i]n cases of misdemeanor, a peace officer like a private person has at common law no power of arresting without a warrant except when a breach of the peace has been committed in his presence or there is reasonable ground for supposing that a breach of peace is about to be committed or renewed in his presence.' " <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Id.,</a></span></i> at 157 (quoting 9 Halsbury, Laws of England § 612, p. 299 (1909)).</blockquote>
<p><span class="star-pagination">*329</span> But the isolated quotation tends to mislead. In <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself we spoke of the common-law rule as only "sometimes expressed" that way, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#157" aria-description="Citation for case: Carroll v. United States">267 U. S., at 157</a></span>, and, indeed, in the very same paragraph, we conspicuously omitted any reference to a breach-of-the-peace limitation in stating that the "usual rule" at common law was that "a police officer [could] arrest without warrant . . . one guilty of a misdemeanor if committed in his presence." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 156-157</a></span>. Thus, what <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> illustrates, and what others have recognized, is that statements about the common law of warrantless misdemeanor arrest simply are not uniform. Rather, "[a]t common law there is a difference of opinion among the authorities as to whether this right to arrest [without a warrant] extends to all misdemeanors." American Law Institute, Code of Criminal Procedure, Commentary to § 21, p. 231 (1930).</p>
<p>On one side of the divide there are certainly eminent authorities supporting Atwater's position. In addition to Lord Halsbury, quoted in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> James Fitzjames Stephen and Glanville Williams both seemed to indicate that the common law confined warrantless misdemeanor arrests to actual breaches of the peace. See 1 J. Stephen, A History of the Criminal Law of England 193 (1883) ("The common law did not authorise the arrest of persons guilty or suspected of misdemeanours, except in cases of an actual breach of the peace either by an affray or by violence to an individual"); G. Williams, Arrest for Breach of the Peace, <span class="citation no-link">1954 Crim. L. Rev. 578</span>, 578 ("Apart from arrest for felony . . . , the only power of arrest at common law is in respect of breach of the peace"). See also <i>Queen</i> v. <i>Tooley,</i> 2 Ld. Raym. 1296, 1301, 92 Eng. Rep. 349, 352 (Q. B. 1710) ("[A] constable cannot arrest, but when he sees an actual breach of the peace; and if the affray be over, he cannot arrest").</p>
<p>Sir William Blackstone and Sir Edward East might also be counted on Atwater's side, although they spoke only to the sufficiency of breach of the peace as a condition to warrantless <span class="star-pagination">*330</span> misdemeanor arrest, not to its necessity. Blackstone recognized that at common law "[t]he constable . . . hath great original and inherent authority with regard to arrests," but with respect to nonfelony offenses said only that "[h]e may, without warrant, arrest any one for a breach of the peace, and carry him before a justice of the peace." 4 Blackstone 289. Not long after the framing of the Fourth Amendment, East characterized peace officers' common-law arrest power in much the same way: "A constable or other known conservator of the peace may lawfully interpose upon his own view to prevent a breach of the peace, or to quiet an affray . . . ." 1 E. East, Pleas of the Crown § 71, p. 303 (1803).</p>
<p>The great commentators were not unanimous, however, and there is also considerable evidence of a broader conception of common-law misdemeanor arrest authority unlimited by any breach-of-the-peace condition. Sir Matthew Hale, Chief Justice of King's Bench from 1671 to 1676,<sup>[3]</sup> wrote in his History of the Pleas of the Crown that, by his "original and inherent power," a constable could arrest without a warrant "for breach of the peace and some misdemeanors, less than felony." 2 M. Hale, Pleas of the Crown 88 (1736). Hale's view, posthumously published in 1736, reflected an understanding dating back at least 60 years before the appearance of his Pleas yet sufficiently authoritative to sustain a momentum extending well beyond the framing era in this country. See The Compleat Parish-Officer 11 (1744) ("[T]he Constable . . . may for Breach of the Peace, and some Misdemeanors less than Felony, imprison a Man"); R. Burn, The Justice of the Peace 271 (1837) ("A <i>constable</i> . . . may at common law, for treason, felony, breach of the peace, and some misdemeanors less than felony, <i>committed in his view,</i> apprehend the supposed offender without any warrant" (italics in original)); 1 J. Chitty, A Practical <span class="star-pagination">*331</span> Treatise on the Criminal Law 20 (5th ed. 1847) ("[A constable] may for treason, felony, breach of the peace, and some misdemeanors less than felony, committed in his view, apprehend the supposed offender <i>virtiute officii,</i> without any warrant"); 1 W. Russell, Crimes and Misdemeanors 725 (7th ed. 1909) (officer "may arrest any person who in his presence commits a misdemeanor or breach of the peace").<sup>[4]</sup></p>
<p>As will be seen later, the view of warrantless arrest authority as extending to at least "some misdemeanors" beyond breaches of the peace was undoubtedly informed by statutory provisions authorizing such arrests, but it reflected common law in the strict, judge-made sense as well, for such was the holding of at least one case reported before Hale had even become a judge but which, like Hale's own commentary, continued to be cited well after the ratification of the Fourth Amendment. In <i>Holyday</i> v. <i>Oxenbridge,</i> Cro. Car. 234, 79 Eng. Rep. 805 (1631), the Court of King's Bench held that even a private person (and thus <i>a fortiori</i> a peace officer<sup>[5]</sup>) needed no warrant to arrest a "common cheater" whom he discovered "cozen[ing] with false dice." The court expressly rejected the contention that warrantless arrests were improper "unless in felony," and said instead that "there was good cause [for] staying" the gambler and, more broadly, that "it is <i>pro bono publico</i> to stay such offenders." <i>Id.,</i>  at 805-806. In the edition nearest to the date of the Constitution's framing, Sergeant William Hawkins's widely read Treatise of the Pleas of the Crown generalized from <i>Holyday</i> that "from the reason of this case it seems to follow, <span class="star-pagination">*332</span> That the [warrantless] arrest of any other offenders . . . for offences in like manner scandalous and prejudicial to the public, may be justified." 2 Hawkins, ch. 12, § 20, at 122. A number of other common-law commentaries shared Hawkins's broad reading of <i>Holyday.</i> See The Law of Arrests 205 (2d ed. 1753) (In light of <i>Holyday,</i> "an Arrest of an Offender . . . for any Crime prejudicial to the Publick, seems to be justifiable"); 1 T. Cunningham, A New and Complete Law Dictionary (1771) (definition of "arrest") (same); 1 G. Jacob, The Law Dictionary 129 (1st Am. ed. 1811) (same). See generally C. Greaves, Law of Arrest Without a Warrant, in The Criminal Law Consolidation Acts, p. lxiii (1870) ("<i>[Holyday]</i> is rested upon the broad ground that `it is <i>pro bono publico</i> to stay such offenders,' which is equally applicable to every case of misdemeanor . . . ").<sup>[6]</sup></p>
<p>We thus find disagreement, not unanimity, among both the common-law jurists and the text writers who sought to pull the cases together and summarize accepted practice. Having reviewed the relevant English decisions, as well as English and colonial American legal treatises, legal dictionaries, and procedure manuals, we simply are not convinced that Atwater's is the correct, or even necessarily the better, reading of the common-law history.</p>
<p></p>
<h2>
<span class="star-pagination">*333</span> 2</h2>
<p>A second, and equally serious, problem for Atwater's historical argument is posed by the "divers Statutes," M. Dalton, Country Justice, ch. 170, § 4, p. 582 (1727), enacted by Parliament well before this Republic's founding that authorized warrantless misdemeanor arrests without reference to violence or turmoil. Quite apart from Hale and Blackstone, the legal background of any conception of reasonableness the Fourth Amendment's Framers might have entertained would have included English statutes, some centuries old, authorizing peace officers (and even private persons) to make warrantless arrests for all sorts of relatively minor offenses unaccompanied by violence. The so-called "nightwalker" statutes are perhaps the most notable examples. From the enactment of the Statute of Winchester in 1285, through its various readoptions and until its repeal in 1827,<sup>[7]</sup> night watchmen were authorized and charged "as . . . in Times past" to "watch the Town continually all Night, from the Sun-setting unto the Sun-rising" and were directed that "if any Stranger do pass by them, he shall be arrested until Morning . . . ." 13 Edw. I, ch. 4, §§ 5-6, 1 Statutes at Large 232-233; see also 5 Edw. III, ch. 14, 1 Statutes at Large 448 (1331) (confirming and extending the powers of watchmen). Hawkins emphasized that the Statute of Winchester "was made" not in derogation but rather "in affirmance of the common law," for "every private person may by the common law arrest any suspicious night-walker, and detain him till he give good account of himself . . . ." 2 Hawkins, ch. 13, § 6, at 130. And according to Blackstone, these watchmen had virtually limitless warrantless nighttime arrest power: "Watchmen, either those appointed by the statute of Winchester . . . or such as are mere assistants to the constable, may <i>virtute officii</i> arrest all offenders, and particularly nightwalkers, and commit them to custody till the morning." 4 Blackstone 289; see <span class="star-pagination">*334</span> also 2 Hale, Pleas of the Crown, at 97 (describing broad arrest powers of watchmen even over and above those conferred by the Statute of Winchester).<sup>[8]</sup> The Statute of Winchester, moreover, empowered peace officers not only to deal with nightwalkers and other nighttime "offenders," but periodically to "make Inquiry of all Persons being lodged in the Suburbs, or in foreign Places of the Towns." On that score, the Statute provided that "if they do find any that have lodged or received any Strangers or suspicious Person, against the Peace, the Bailiffs shall do Righttherein," 13 Edw. I, ch. 4, §§ 3-4, 1 Statutes at Large 232-233, which Hawkins understood "surely" to mean that officers could "lawfully arrest and detain any such stranger[s]," 2 Hawkins, ch. 13, § 12,at 134.</p>
<p>Nor were the nightwalker statutes the only legislative sources of warrantless arrest authority absent real or threatened violence, as the parties and their <i>amici</i> here seem to have assumed. On the contrary, following the Edwardian legislation and throughout the period leading up to the framing, Parliament repeatedly extended warrantless arrest power to cover misdemeanor-level offenses not involving any breach of the peace. One 16th-century statute, for instance, authorized peace officers to arrest persons playing "unlawful game[s]" like bowling, tennis, dice, and cards, and for good measure extended the authority beyond players to include persons "haunting" the "houses, places and alleys where such games shall be suspected to be holden, exercised, used <span class="star-pagination">*335</span> or occupied." 33 Hen. VIII, ch. 9, §§ 11-16, 5 Statutes at Large 84-85 (1541). A 17th-century act empowered "any person . . . whatsoever to seize and detain any . . . hawker, pedlar, petty chapman, or other trading person" found selling without a license. 8 &amp; 9 Wm. III, ch. 25, §§ 3, 8, 10 Statutes at Large 81-83 (1697). And 18th-century statutes authorized the warrantless arrest of "rogues, vagabonds, beggars, and other idle and disorderly persons" (defined broadly to include jugglers, palm readers, and unlicensed play actors), 17 Geo. II, ch. 5, §§ 1-2, 5, 18 Statutes at Large 144, 145-147 (1744); "horrid" persons who "profanely swear or curse," 19 Geo. II, ch. 21, § 3, 18 Statutes at Large 445 (1746); individuals obstructing "publick streets, lanes or open passages" with "pipes, butts, barrels, casks or other vessels" or an "empty cart, car, dray or other carriage," 30 Geo. II, ch. 22, §§ 5, 13, 22 Statutes at Large 107-108, 111 (1757); and, most significantly of all given the circumstances of the case before us, negligent carriage drivers, 27 Geo. II, ch. 16, § 7, 21 Statutes at Large 188 (1754). See generally S. Blackerby, The Justice of Peace: His Companion, or a Summary of all the Acts of Parliament (1723) (cataloguing statutes); S. Welch, An Essay on the Office of Constable 19-22 (1758) (describing same).</p>
<p>The significance of these early English statutes lies not in proving that any common-law rule barring warrantless misdemeanor arrests that might have existed would have been subject to statutory override; the sovereign Parliament could of course have wiped away any judge-made rule. The point is that the statutes riddle Atwater's supposed common-law rule with enough exceptions to unsettle any contention that the law of the mother country would have left the Fourth Amendment's Framers of a view that it would necessarily have been unreasonable to arrest without warrant for a misdemeanor unaccompanied by real or threatened violence.</p>
<p></p>
<h2>
<span class="star-pagination">*336</span> B</h2>
<p>An examination of specifically American evidence is to the same effect. Neither the history of the framing era nor subsequent legal development indicates that the Fourth Amendment was originally understood, or has traditionally been read, to embrace Atwater's position.</p>
<p></p>
<h2>1</h2>
<p>To begin with, Atwater has cited no particular evidence that those who framed and ratified the Fourth Amendment sought to limit peace officers' warrantless misdemeanor arrest authority to instances of actual breach of the peace, and our own review of the recent and respected compilations of framing-era documentary history has likewise failed to reveal any such design. See The Complete Bill of Rights 223 263 (N. Cogan ed. 1997) (collecting original sources); 5 The Founders' Constitution 219-244 (P. Kurland &amp; R. Lerner eds. 1987) (same). Nor have we found in any of the modern historical accounts of the Fourth Amendment's adoption any substantial indication that the Framers intended such a restriction. See, <i>e. g.,</i> L. Levy, Origins of the Bill of Rights 150-179 (1999); T. Taylor, Two Studies in Constitutional Interpretation 19-93 (1969); J. Landynski, Search and Seizure and the Supreme Court 19-48 (1966); N. Lasson, History and Development of the Fourth Amendment to the United States Constitution 79-105 (1937); Davies, Recovering the Original Fourth Amendment, <span class="citation no-link">98 Mich. L. Rev. 547</span> (1999); Amar, Fourth Amendment First Principles, <span class="citation no-link">107 Harv. L. Rev. 757</span> (1994); Bradley, Constitutional Theory of the Fourth Amendment, <span class="citation no-link">38 DePaul L. Rev. 817</span> (1989). Indeed, to the extent these modern histories address the issue, their conclusions are to the contrary. See Landynski, <i>supra,</i> at 45 (Fourth Amendment arrest rules are "based on common-law practice," which "dispensed with" a warrant requirement for misdemeanors "committed in the presence of the arresting officer"); Davies, <i>supra,</i> at 551 ("[T]he Framers did not address <span class="star-pagination">*337</span> warrantless intrusions at all in the Fourth Amendment or in the earlier state provisions; thus, they never anticipated that `unreasonable' might be read as a standard for warrantless intrusions").</p>
<p>The evidence of actual practice also counsels against Atwater's position. During the period leading up to and surrounding the framing of the Bill of Rights, colonial and state legislatures, like Parliament before them, <i>supra,</i> at 333-335, regularly authorized local peace officers to make warrantless misdemeanor arrests without conditioning statutory authority on breach of the peace. See, <i>e. g.,</i> First Laws of the State of Connecticut 214-215 (Cushing ed. 1982) (1784 compilation; exact date of Act unknown) (authorizing warrantless arrests of "all Persons unnecessarily travelling on the Sabbath or Lord's Day"); <i>id.,</i> at 23 ("such as are guilty of Drunkenness, profane Swearing, Sabbath-breaking, also vagrant Persons [and] unseasonable Night-walkers"); Digest of the Laws of the State of Georgia 1755-1800, p. 411 (H. Marbury &amp; W. Crawford eds. 1802) (1762 Act) (breakers of the Sabbath laws); <i>id.,</i> at 252 (1764 Act) (persons "gaming . . . in any licensed public house, or other house sellingliquors"); Colonial Laws of Massachusetts 139 (1889) (1646 Act) ("such as are overtaken with drink, swearing, Sabbath breaking, Lying, vagrant persons, [and] night-walkers"); Laws of the State of New Hampshire 549 (1800) (1799 Act) (persons "travelling unnecessarily" on Sunday); Digest of the Laws of New Jersey 1709-1838, pp. 585-586 (L. Elmer ed. 1838) (1799 Act) ("vagrants or vagabonds, common drunkards, common night-walkers, and common prostitutes," as well as fortunetellers and other practitioners of "crafty science"); Laws of the State of New York, 1777-1784, pp. 358-359 (1886) (1781 Act) ("hawker[s]" and "pedlar[s]"); Earliest Printed Laws of New York, 1665-1693, p. 133 (J. Cushing ed. 1978) (Duke of York's Laws, 1665-1675) ("such as are overtaken with Drink, Swearing, Sabbath breaking, Vagrant persons or night walkers"); 3 Laws of the Commonwealth of Pennsylvania 177-183 <span class="star-pagination">*338</span> (1810) (1794 Act) (persons "profanely curs[ing]," drinking excessively, "cock-fighting," or "play[ing] at cards, dice, billiards, bowls, shuffle-boards, or any game of hazard or address, for money").<sup>[9]</sup></p>
<p>What we have here, then, is just the opposite of what we had in <i>Wilson</i> v. <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span></i><i>.</i> There, we emphasized that during the founding era a number of States had "enacted statutes specifically embracing" the common-law knock-andannounce rule, <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 933</a></span>; here, by contrast, those very same States passed laws extending warrantless arrest authority to a host of nonviolent misdemeanors, and in so doing acted very much inconsistently with Atwater's claims about the Fourth Amendment's object. Of course, the Fourth <span class="star-pagination">*339</span> Amendment did not originally apply to the States, see <i>Barron</i> v. <i>Mayor of Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span> (1833), but that does not make state practice irrelevant in unearthing the Amendment's original meaning. A number of state constitutional search-and-seizure provisions served as models for the Fourth Amendment, see, <i>e. g.,</i> N. H. Const. of 1784, pt. I, Art. XIX; Pa. Const. of 1776 (Declaration of Rights), Art. X, and the fact that many of the original States with such constitutional limitations continued to grant their own peace officers broad warrantless misdemeanor arrest authority undermines Atwater's contention that the founding generation meant to bar federal law enforcement officers from exercising the same authority. Given the early state practice, it is likewise troublesome for Atwater's view that just one year after the ratification of the Fourth Amendment, Congress vested federal marshals with "the same powers in executing the laws of the United States, as sheriffs and their deputies in the several states have by law, in executing the laws of their respective states." Act of May 2, 1792, ch. 28, § 9, <span class="citation no-link">1 Stat. 265</span>. Thus, as we have said before in only slightly different circumstances, the Second Congress apparently "saw no inconsistency between the Fourth Amendment and legislation giving United States marshals the same power as local peace officers" to make warrantless arrests. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#420" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 420</a></span> (1976).<sup>[10]</sup></p>
<p>The record thus supports Justice Powell's observation that "[t]here is no historical evidence that the Framers or proponents of the Fourth Amendment, outspokenly opposed to the infamous general warrants and writs of assistance, were at <span class="star-pagination">*340</span> all concerned about warrantless arrests by local constables and other peace officers." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#429" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 429</a></span> (concurring opinion). We simply cannot conclude that the Fourth Amendment, as originally understood, forbade peace officers to arrest without a warrant for misdemeanors not amounting to or involving breach of the peace.</p>
<p></p>
<h2>2</h2>
<p>Nor does Atwater's argument from tradition pick up any steam from the historical record as it has unfolded since the framing, there being no indication that her claimed rule has ever become "woven . . . into the fabric" of American law. <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas"><i>Wilson, supra,</i> at 933</a></span>; see also <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U. S., at 590</a></span> (emphasizing "the clear consensus among the States adhering to [a] well-settled common-law rule"). The story, on the contrary, is of two centuries of uninterrupted (and largely unchallenged) state and federal practice permitting warrantless arrests for misdemeanors not amounting to or involving breach of the peace.</p>
<p>First, there is no support for Atwater's position in this Court's cases (apart from the isolated sentence in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i>  already explained). Although the Court has not had much to say about warrantless misdemeanor arrest authority, what little we have said tends to cut against Atwater's argument. In discussing this authority, we have focused on the circumstance that an offense was committed in an officer's presence, to the omission of any reference to a breach-of-the-peace limitation.<sup>[11]</sup> See, <i>e. g., </i><i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 418</a></span> ("The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony <span class="star-pagination">*341</span> committed in his presence . . ."); <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> 267 U. S., at 156 157 ("The usual rule is that a police officer may arrest without warrant one . . . guilty of a misdemeanor if committed in his presence"); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534, 536, n. 1</a></span> (1900) (noting common-law pedigree of state statute permitting warrantless arrest "[f]or a public offense committed or attempted in [officer's] presence"); <i>Kurtz</i> v. <i>Moffitt,</i>  <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#499" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 499</a></span> (1885) (common-law presence requirement); cf. also <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#756" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 756</a></span> (1984) (White, J., dissenting) ("`[A]uthority to arrest without a warrant in misdemeanor cases may be enlarged by statute' ").</p>
<p>Second, and again in contrast with <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,</i> it is not the case here that "[e]arly American courts . . .embraced" an accepted common-law rule with anything approaching unanimity. <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 933</a></span>. To be sure, Atwater has cited several 19th-century decisions that, at least at first glance, might seem to support her contention that "warrantless misdemeanor arrest was unlawful when not [for] a breach of the peace." Brief for Petitioners 17 (citing <i>Pow</i> v. <i>Beckner,</i> <span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/#478" aria-description="Citation for case: Pow v. Beckner">3 Ind. 475, 478</a></span> (1852), <i>Commonwealth</i>  v. <i>Carey,</i> <span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/#250" aria-description="Citation for case: Commonwealth v. Carey">66 Mass. 246, 250</a></span> (1853), and <i>Robison</i> v. <i>Miner,</i>  <span class="citation" data-id="7933442"><a href="/opinion/7980722/robison-v-miner/#556" aria-description="Citation for case: Robison v. Miner">68 Mich. 549, 556-559</a></span>, <span class="citation no-link">37 N. W. 21</span>, 25 (1888)). But none is ultimately availing. <i><span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/" aria-description="Citation for case: Pow v. Beckner">Pow</a></span></i> is fundamentally a "presence" case; it stands only for the proposition, not at issue here, see n. 11, <i>supra,</i> that a nonfelony arrest should be made while the offense is "in [the officer's] view and . . . still continuing" and not subsequently "upon vague information communicated to him." <span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/#478" aria-description="Citation for case: Pow v. Beckner">3 Ind., at 478</a></span>. The language Atwater attributes to <i><span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/" aria-description="Citation for case: Commonwealth v. Carey">Carey</a></span></i> ("[E]ven if he were a constable, he had no power to arrest for any misdemeanor without a warrant, except to stay a breach of the peace, or to prevent the commission of such an offense") is taken from the reporter's summary of one of the party's arguments, not from the opinion of the court. While the court in <i><span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/" aria-description="Citation for case: Commonwealth v. Carey">Carey</a></span></i> (through Chief Justice Shaw) said that "the old established rule of the common law" was that "a constable or other peace officer could not <span class="star-pagination">*342</span> arrest one without a warrant . . . if such crime were not an offence amounting in law to felony," it said just as clearly that the common-law rule could be "altered by the legislature" (notwithstanding Massachusetts's own Fourth Amendment equivalent in its State Constitution). <span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/#252" aria-description="Citation for case: Commonwealth v. Carey">66 Mass., at 252</a></span>. <i>Miner,</i> the third and final case upon which Atwater relies, was expressly overruled just six years after it was decided. In <i>Burroughs</i> v. <i>Eastman,</i> <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/" aria-description="Citation for case: Burroughs v. Eastman">101 Mich. 419</a></span>, <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/" aria-description="Citation for case: Burroughs v. Eastman">59 N. W. 817</a></span> (1894), the Supreme Court of Michigan held that the language from <i>Miner</i> upon which the plaintiff there (and presumably Atwater here) relied "should not be followed," and then went on to offer the following: "[T]he question has arisen in many of our sister states, and the power to authorize arrest on view for offenses not amounting to breaches of the peace has been affirmed. Our attention has been called to no case, nor have we in our research found one, in which the contrary doctrine has been asserted." <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/#425" aria-description="Citation for case: Burroughs v. Eastman">101 Mich., at 425</a></span>, <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/#819" aria-description="Citation for case: Burroughs v. Eastman">59 N. W., at 819</a></span> (collecting cases from, <i>e. g.,</i> Illinois, Indiana, Massachusetts, Minnesota, Missouri, New Hampshire, New York, Ohio, and Texas).</p>
<p>The reports may well contain early American cases more favorable to Atwater's position than the ones she has herself invoked. But more to the point, we think, are the numerous early- and mid-19th-century decisions expressly sustaining (often against constitutional challenge) state and local laws authorizing peace officers to make warrantless arrests for misdemeanors not involving any breach of the peace. See, <i>e. g., </i><i>Mayo</i> v. <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,</i> 1 N. H. 53 (1817) (upholding statute authorizing warrantless arrests of those unnecessarily traveling on Sunday against challenge based on state due process and search-and-seizure provisions); <i>Holcomb</i> v. <i>Cornish,</i> <span class="citation" data-id="6574474"><a href="/opinion/6694531/holcomb-v-cornish/" aria-description="Citation for case: Holcomb v. Cornish">8 Conn. 375</a></span> (1831) (upholding statute permitting warrantless arrests for "drunkenness, profane swearing, cursing or sabbath-breaking" against argument that "[t]he power of a justice of the peace to arrest and detain a citizen without complaint or warrant against him, is surely not given by the <span class="star-pagination">*343</span> common law"); <i>Jones</i> v. <i>Root,</i> <span class="citation" data-id="6410982"><a href="/opinion/6537262/jones-v-root/" aria-description="Citation for case: Jones v. Root">72 Mass. 435</a></span> (1856) (rebuffing constitutional challenge to statute authorizing officers "without a warrant [to] arrest any person or persons whom they may find in the act of illegally selling, transporting, or distributing intoxicating liquors"); <i>Main</i> v. <i>McCarty,</i> <span class="citation" data-id="6948242"><a href="/opinion/7044997/main-v-mccarty/#442" aria-description="Citation for case: Main v. McCarty">15 Ill. 441, 442</a></span> (1854) (concluding that a law expressly authorizing arrests for city-ordinance violations was "not repugnant to the constitution or the general provisions of law"); <i>White</i> v. <i>Kent,</i>  <span class="citation no-link">11 Ohio St. 550</span> (1860) (upholding municipal ordinance permitting warrantless arrest of any person found violating any city ordinance or state law); <i>Davis</i> v. <i>American Soc. for Prevention of Cruelty to Animals,</i> <span class="citation" data-id="3585438"><a href="/opinion/3603859/davis-v-american-society-for-prevention-of-cruelty-to-animals/" aria-description="Citation for case: Davis v. American Society for Prevention of Cruelty to...">75 N. Y. 362</a></span> (1878) (upholding statute permitting warrantless arrest for misdemeanor violation of cruelty-to-animals prohibition). See generally Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 550, and n. 54 (1924) (collecting cases and observing that "[t]he states may, by statute, enlarge the common law right to arrest without a warrant, and have quite generally done so or authorized municipalities to do so, as for example, an officer may be authorized by statute or ordinance to arrest without a warrant for various misdemeanors and violations of ordinances, other than breaches of the peace, if committed in his presence"); <span class="citation no-link"><i>id.,</i> at 706, nn. 570, 571</span> (collecting cases); 1 J. Bishop, New Criminal Procedure §§ 181, 183, pp. 101, n. 2, 103, n. 5 (4th ed. 1895) (same); W. Clark, Handbook of Criminal Procedure § 12, p. 50, n. 8 (2d ed. 1918) (same).</p>
<p>Finally, both the legislative tradition of granting warrantless misdemeanor arrest authority and the judicial tradition of sustaining such statutes against constitutional attack are buttressed by legal commentary that, for more than a century now, has almost uniformly recognized the constitutionality of extending warrantless arrest power to misdemeanors without limitation to breaches of the peace. See, <i>e. g.,</i> E. Fisher, Laws of Arrest § 59, p. 130 (1967) ("[I]t is generally recognized today that the common law authority to arrest without a warrant in misdemeanor cases may be enlarged by <span class="star-pagination">*344</span> statute, and this has been done in many of the states"); Wilgus, <i>supra,</i> at 705-706 ("Statutes and municipal charters have quite generally authorized an officer to arrest for any misdemeanor whether a breach of the peace or not, without a warrant, if committed in the officer's presence. Such statutes are valid" (footnote omitted)); Clark, <i>supra,</i> § 12, at 50 ("In most, if not all, the states there are statutes and city ordinances, which are clearly valid, authorizing officers to arrest for certain misdemeanors without a warrant, when committed in their presence"); J. Beale, Criminal Pleading and Practice § 21, p. 20, and n. 7 (1899) ("By statute the power of peace officers to arrest without a warrant is often extended to all misdemeanors committed in their presence." "Such a statute is constitutional"); 1 Bishop, <i>supra,</i> § 183, at 103 ("[T]he power of arrest extends, possibly, to any indictable wrong in [an officer's] presence. . . . And statutes and ordinances widely permit these arrests for violations of municipal by-laws"); J. Bassett, Criminal Pleading and Practice § 89, p. 104 (2d ed. 1885) ("[A]s to the lesser misdemeanors, except breaches of the peace, the power extends only so far as some statute gives it"). But cf. H. Vorhees, Law of Arrest § 131, pp. 78-79 (1904) (acknowledging that "by authority of statute, city charter, or ordinance, [an officer] may arrest without a warrant, one who . . . commits a misdemeanor other than a breach of the peace," but suggesting that courts look with "disfavor" on such legislative enactments "as interfering with the constitutional liberties of the subject").</p>
<p>Small wonder, then, that today statutes in all 50 States and the District of Columbia permit warrantless misdemeanor arrests by at least some (if not all) peace officers without requiring any breach of the peace,<sup>[12]</sup> as do a host of congressional enactments.<sup>[13]</sup> The American Law Institute <span class="star-pagination">*345</span> has long endorsed the validity of such legislation, see American Law Institute, Code of Criminal Procedure § 21(a), p. 28 (1930); American Law Institute, Model Code of PreArraignment Procedure § 120.1(1)(c), p. 13 (1975), and the consensus, as stated in the current literature, is that statutes "remov[ing] the breach of the peace limitation and thereby permit[ting] arrest without warrant for <i>any</i> misdemeanor committed in the arresting officer's presence" have "`never been successfully challenged and stan[d] as the law of the land.' " 3 W. LaFave, Search and Seizure § 5.1(b), pp. 13-14, and n. 76 (1996) (quoting <i>Higbee</i> v. <i>San Diego,</i> <span class="citation" data-id="546349"><a href="/opinion/546349/raymond-higbee-william-crenshaw-alexander-smogyi-roger-dennehy-v-city-of/#379" aria-description="Citation for case: Raymond Higbee William Crenshaw Alexander Smogyi Roger...">911 F. 2d 377, 379</a></span> (CA9 1990)) (emphasis in original; footnote omitted). This, therefore, simply is not a case in which the claimant can point to "a clear answer [that] existed in 1791 and has been generally adhered to by the traditions of our society ever since." <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/#60" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S. 44, 60</a></span> (1991) (Scalia, J., dissenting).</p>
<p></p>
<h2>III</h2>
<p>While it is true here that history, if not unequivocal, has expressed a decided, majority view that the police need not obtain an arrest warrant merely because a misdemeanor stopped short of violence or a threat of it, Atwater does not wager all on history.<sup>[14]</sup> Instead, she asks us to mint a new <span class="star-pagination">*346</span> rule of constitutional law on the understanding that when historical practice fails to speak conclusively to a claim grounded on the Fourth Amendment, courts are left to strike a current balance between individual and societal interests by subjecting particular contemporary circumstances to traditional standards of reasonableness. See <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 299-300</a></span> (1999); <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 652-653</a></span> (1995). Atwater accordingly argues for a modern arrest rule, one not necessarily requiring violent breach of the peace, but nonetheless forbidding custodial arrest, even upon probable cause, when conviction could not ultimately carry any jail time and when the government shows no compelling need for immediate detention.<sup>[15]</sup></p>
<p>If we were to derive a rule exclusively to address the uncontested facts of this case, Atwater might well prevail. She was a known and established resident of Lago Vista with no place to hide and no incentive to flee, and common sense says she would almost certainly have buckled up as a condition of driving off with a citation. In her case, the physical incidents of arrest were merely gratuitous humiliations imposed by a police officer who was (at best) exercising <span class="star-pagination">*347</span> extremely poor judgment. Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case.</p>
<p>But we have traditionally recognized that a responsible Fourth Amendment balance is not well served by standards requiring sensitive, case-by-case determinations of government need, lest every discretionary judgment in the field be converted into an occasion for constitutional review. See, <i>e. g., </i><i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 234-235</a></span> (1973). Often enough, the Fourth Amendment has to be applied on the spur (and in the heat) of the moment, and the object in implementing its command of reasonableness is to draw standards sufficiently clear and simple to be applied with a fair prospect of surviving judicial second-guessing months and years after an arrest or search is made. Courts attempting to strike a reasonable Fourth Amendment balance thus credit the government's side with an essential interest in readily administrable rules. See <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981) (Fourth Amendment rules "`ought to be expressed in terms that are readily applicable by the police in the context of the law enforcement activities in which they are necessarily engaged' " and not "`qualified by all sorts of ifs, ands, and buts' ").<sup>[16]</sup></p>
<p>At first glance, Atwater's argument may seem to respect the values of clarity and simplicity, so far as she claims that the Fourth Amendment generally forbids warrantless arrests for minor crimes not accompanied by violence or some <span class="star-pagination">*348</span> demonstrable threat of it (whether "minor crime" be defined as a fine-only traffic offense, a fine-only offense more generally, or a misdemeanor<sup>[17]</sup>). But the claim is not ultimately so simple, nor could it be, for complications arise the moment we begin to think about the possible applications of the several criteria Atwater proposes for drawing a line between minor crimes with limited arrest authority and others not so restricted.</p>
<p>One line, she suggests, might be between "jailable" and "fine-only" offenses, between those for which conviction could result in commitment and those for which it could not. The trouble with this distinction, of course, is that an officer on the street might not be able to tell. It is not merely that we cannot expect every police officer to know the details of frequently complex penalty schemes, see <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#431" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 431, n. 13</a></span> (1984) ("[O]fficers in the field frequently `have neither the time nor the competence to determine' the severity of the offense for which they are considering arresting a person"), but that penalties for ostensibly identical conduct can vary on account of facts difficult (if not impossible) to know at the scene of an arrest. Is this the first offense or is the suspect a repeat offender?<sup>[18]</sup> Is the weight of the marijuana a gram above or a gram below <span class="star-pagination">*349</span> the fine-only line?<sup>[19]</sup> Where conduct could implicate more than one criminal prohibition, which one will the district attorney ultimately decide to charge?<sup>[20]</sup> And so on.</p>
<p>But Atwater's refinements would not end there. She represents that if the line were drawn at nonjailable traffic offenses, her proposed limitation should be qualified by a proviso authorizing warrantless arrests where "necessary for enforcement of the traffic laws or when [an] offense would otherwise continue and pose a danger to others on the road." Brief for Petitioners 46 (internal quotation marks omitted). (Were the line drawn at misdemeanors generally, a comparable qualification would presumably apply.) The proviso only compounds the difficulties. Would, for instance, either exception apply to speeding? At oral argument, Atwater's counsel said that "it would not be reasonable to arrest a driver for speeding unless the speeding rose to the level of reckless driving." Tr. of Oral Arg. 16. But is it not fair to expect that the chronic speeder will speed again despite a citation in his pocket, and should that not qualify as showing that the "offense would . . . continue" under Atwater's rule? And why, as a constitutional matter, should we assume that only reckless driving will "pose a danger to others on the road" while speeding will not?</p>
<p><span class="star-pagination">*350</span> There is no need for more examples to show that Atwater's general rule and limiting proviso promise very little in the way of administrability. It is no answer that the police routinely make judgments on grounds like risk of immediate repetition; they surely do and should. But there is a world of difference between making that judgment in choosing between the discretionary leniency of a summons in place of a clearly lawful arrest, and making the same judgment when the question is the lawfulness of the warrantless arrest itself. It is the difference between no basis for legal action challenging the discretionary judgment, on the one hand, and the prospect of evidentiary exclusion or (as here) personal § 1983 liability for the misapplication of a constitutional standard, on the other. Atwater's rule therefore would not only place police in an almost impossible spot but would guarantee increased litigation over many of the arrests that would occur.<sup>[21]</sup> For all these reasons, Atwater's various distinctions between permissible and impermissible arrests for minor crimes strike us as "very unsatisfactory line[s]" to require police officers to draw on a moment's notice. <i>Carroll</i>  v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#157" aria-description="Citation for case: Carroll v. United States">267 U. S., at 157</a></span>.</p>
<p>One may ask, of course, why these difficulties may not be answered by a simple tie breaker for the police to follow in the field: if in doubt, do not arrest. The first answer is that in practice the tie breaker would boil down to something akin to a least-restrictive-alternative limitation, which is itself one of those "ifs, ands, and buts" rules, <i>New York</i>  v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S., at 458</a></span>, generally thought inappropriate in working out Fourth Amendment protection. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span>, <span class="star-pagination">*351</span> 629, n. 9 (1989) (collecting cases); <i>United States</i> v. <i>MartinezFuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557-558, n. 12</a></span> (1976) ("The logic of such elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all searchand-seizure powers"). Beyond that, whatever help the tie breaker might give would come at the price of a systematic disincentive to arrest in situations where even Atwater concedes that arresting would serve an important societal interest. An officer not quite sure that the drugs weighed enough to warrant jail time or not quite certain about a suspect's risk of flight would not arrest, even though it could perfectly well turn out that, in fact, the offense called for incarceration and the defendant was long gone on the day of trial. Multiplied many times over, the costs to society of such under enforcement could easily outweigh the costs to defendants of being needlessly arrested and booked, as Atwater herself acknowledges.<sup>[22]</sup></p>
<p>Just how easily the costs could outweigh the benefits may be shown by asking, as one Member of this Court did at oral argument, "how bad the problem is out there." Tr. of Oral Arg. 20. The very fact that the law has never jelled the way Atwater would have it leads one to wonder whether warrantless misdemeanor arrests need constitutional attention, <span class="star-pagination">*352</span> and there is cause to think the answer is no. So far as such arrests might be thought to pose a threat to the probable-cause requirement, anyone arrested for a crime without formal process, whether for felony or misdemeanor, is entitled to a magistrate's review of probable cause within 48 hours, <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/#55" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S., at 55-58</a></span>, and there is no reason to think the procedure in this case atypical in giving the suspect a prompt opportunity to request release, see <span class="citation no-link">Tex. Transp. Code Ann. § 543.002</span> (1999) (persons arrested for traffic offenses to be taken "immediately" before a magistrate). Many jurisdictions, moreover, have chosen to impose more restrictive safeguards through statutes limiting warrantless arrests for minor offenses. See, <i>e. g.,</i> <span class="citation no-link">Ala. Code § 32</span>-14 (1999); Cal. Veh. Code Ann. § 40504 (West 2000); <span class="citation no-link">Ky. Rev. Stat. Ann. §§ 431.015</span>(1), (2) (Michie 1999); La. Rev. Stat. Ann. § 32:391 (West 1989); Md. Transp. Code Ann. § 26-202(a)(2) (1999); S. D. Codified Laws § 32-33-2 (1998); <span class="citation no-link">Tenn. Code Ann. § 40</span>-7118(b)(1) (1997); <span class="citation no-link">Va. Code Ann. § 46.2-936</span> (Supp. 2000). It is of course easier to devise a minor-offense limitation by statute than to derive one through the Constitution, simply because the statute can let the arrest power turn on any sort of practical consideration without having to subsume it under a broader principle. It is, in fact, only natural that States should resort to this sort of legislative regulation, for, as Atwater's own <i>amici</i>  emphasize, it is in the interest of the police to limit pettyoffense arrests, which carry costs that are simply too great to incur without good reason. See Brief for Institute on Criminal Justice at the University of Minnesota Law School and Eleven Leading Experts on Law Enforcement and Corrections Administration and Policy as <i>Amici Curiae</i> 11 (the use of custodial arrests for minor offenses "[a]ctually [c]ontradicts [l]aw [e]nforcement [i]nterests"). Finally, and significantly, under current doctrine the preference for categorical treatment of Fourth Amendment claims gives way to individualized review when a defendant makes a colorable <span class="star-pagination">*353</span> argument that an arrest, with or without a warrant, was "conducted in an extraordinary manner, unusually harmful to [his] privacy or even physical interests." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States">517 U. S., at 818</a></span>; see also <i>Graham</i> v. <i>Connor,</i>  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 395-396</a></span> (1989) (excessive force actionable under § 1983).</p>
<p>The upshot of all these influences, combined with the good sense (and, failing that, the political accountability) of most local lawmakers and law-enforcement officials, is a dearth of horribles demanding redress. Indeed, when Atwater's counsel was asked at oral argument for any indications of comparably foolish, warrantless misdemeanor arrests, he could offer only one.<sup>[23]</sup> We are sure that there are others,<sup>[24]</sup> but just as surely the country is not confronting anything like an epidemic of unnecessary minor-offense arrests.<sup>[25]</sup> That fact caps the reasons for rejecting Atwater's request <span class="star-pagination">*354</span> for the development of a new and distinct body of constitutional law.</p>
<p>Accordingly, we confirm today what our prior cases have intimated: the standard of probable cause "applie[s] to all arrests, without the need to `balance' the interests and circumstances involved in particular situations." <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 208</a></span> (1979). If an officer has probable cause to believe that an individual has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender.</p>
<p></p>
<h2>IV</h2>
<p>Atwater's arrest satisfied constitutional requirements. There is no dispute that Officer Turek had probable cause to believe that Atwater had committed a crime in his presence. She admits that neither she nor her children were wearing seatbelts, as required by <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span> (1999). Turek was accordingly authorized (not required, but authorized) to make a custodial arrest without balancing costs and benefits or determining whether or not Atwater's arrest was in some sense necessary.</p>
<p>Nor was the arrest made in an "extraordinary manner, unusually harmful to [her] privacy or . . . physical interests." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States">517 U. S., at 818</a></span>. As our citations in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> make clear, the question whether a search or seizure is "extraordinary" turns, above all else, on the manner in which the search or seizure is executed. See <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">ibid.</a></span></i> (citing <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985) ("seizure by means of deadly force"), <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995) ("unannounced entry into a home"), <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984) ("entry into a home without a warrant"), and <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985) ("physical penetration of the body")). Atwater's arrest was surely "humiliating," as she says in her brief, but it was no more "harmful to . . . privacy or . . . physical interests" than the normal custodial arrest. She was handcuffed, placed in a squad car, and <span class="star-pagination">*355</span> taken to the local police station, where officers asked her to remove her shoes, jewelry, and glasses, and to empty her pockets. They then took her photograph and placed her in a cell, alone, for about an hour, after which she was taken before a magistrate, and released on $310 bond. The arrest and booking were inconvenient and embarrassing to Atwater, but not so extraordinary as to violate the Fourth Amendment.</p>
<p>The Court of Appeals's en banc judgment is affirmed.</p>
<p><i>It is so ordered.</i> </p>
<p>APPENDIX TO OPINION OF THE COURT</p>
<p>State Statutes Authorizing Warrantless Misdemeanor Arrests <span class="citation no-link">Ala. Code § 15-10-3</span>(a)(1) (Supp. 2000) (authorizing warrantless arrest for any "public offense" committed in the presence of the officer);</p>
<p><span class="citation no-link">Alaska Stat. Ann. § 12.25.030</span>(a)(1) (2000) ("for a crime committed . . . in the presence of the person making the arrest");</p>
<p><span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-3883</span>(a)(2) (Supp. 2000) (for a misdemeanor committed in the officer's presence);</p>
<p><span class="citation no-link">Ark. Code Ann. § 16-81-106</span>(b)(2)(a) (Supp. 1999) ("where a public offense is committed in [the officer's] presence");</p>
<p>Cal. Penal Code Ann. § 836(a)(1) (West Supp. 2001) (where "the person to be arrested has committed a public offense in the officer's presence");</p>
<p><span class="citation no-link">Colo. Rev. Stat. § 16</span>-3102(1)(b) (2000) (when "[a]ny crime has been or is being committed" in the officer's presence); <span class="citation no-link">Conn. Gen. Stat. § 54</span>-1f(a) (Supp. 2000) (for "any offense" when arrestee is taken in the act);</p>
<p>Del. Code Ann., Tit. 11, § 1904(a)(1) (1995) (for any misdemeanor committed in the officer's presence);</p>
<p><span class="star-pagination">*356</span> D. C. Code Ann. § 23-581(a)(1)(B) (1996) (where officer has probable cause to believe a person has committed an offense in the officer's presence);</p>
<p><span class="citation no-link">Fla. Stat. § 901.15</span>(1) (Supp. 2001) (for misdemeanor or ordinance violation committed in presence of the officer);</p>
<p><span class="citation no-link">Ga. Code Ann. § 17</span>-420(a) (Supp. 1996) ("for a crime . . . if the offense is committed in [the] officer's presence");</p>
<p><span class="citation no-link">Haw. Rev. Stat. § 803-5</span>(a) (1999) ("when the officer has probable cause to believe that [a] person has committed any offense");</p>
<p><span class="citation no-link">Idaho Code § 19-603</span>(1) (1997) ("[f]or a public offense committed or attempted in [officer's] presence");</p>
<p>Ill. Comp. Stat., ch. 725, § 5/107-2(1)(c) (1992) (when the officer "has reasonable grounds to believe that the person is committing or has committed an offense");</p>
<p><span class="citation no-link">Ind. Code § 35-33</span>-11(a)(4) (Supp. 2000) (when the officer has probable cause to believe a person "is committing or attempting to commit a misdemeanor in the officer's presence");</p>
<p><span class="citation no-link">Iowa Code § 804.7</span>(1) (1994) ("[f]or a public offense committed or attempted in the peace officer's presence");</p>
<p><span class="citation no-link">Kan. Stat. Ann. § 22-2401</span>(d) (1999 Cum. Supp.) (for "[a]ny crime, except a traffic infraction or a cigarette or tobacco infraction," committed in the officer's view);</p>
<p><span class="citation no-link">Ky. Rev. Stat. Ann. § 431.005</span>(1)(d) (Michie 1999) (for any offense punishable by confinement committed in the officer's presence); § 431.015(2) (Supp. 2000) (officer should generally issue citation rather than arrest for certain minor "violations");</p>
<p>La. Code Crim. Proc. Ann., Art. 213(3) (West 1991) (where the officer "has reasonable cause to believe that the person to be arrested has committed an offense");</p>
<p>Me. Rev. Stat. Ann., Tit. 15, § 704 (1980) ("persons found violating any law of the State or any legal ordinance or bylaw <span class="star-pagination">*357</span> of a town"); Tit. 17A, § 15(1)(B) (1983 and Supp. 2000) (for misdemeanors committed in the officer's presence);</p>
<p>Md. Ann. Code, Art. 27, § 594B(a) (1996 and 2000 Supp.) (any person who commits, or attempts to commit, "any felony or misdemeanor" in the presence of an officer);</p>
<p>Mass. Gen. Laws, ch. 276, § 28 (1997) (for designated misdemeanor offenses); ch. 272, § 60 (for littering offenses where identity of arrestee is not known to officer);</p>
<p><span class="citation no-link">Mich. Comp. Laws Ann. § 764.15</span>(1)(a) (West 2000) (for felony, misdemeanor, or ordinance violation committed in the officer's presence);</p>
<p><span class="citation no-link">Minn. Stat. § 629.34</span>(1)(c)(1) (Supp. 2001) ("when a public offense has been committed or attempted in the officer's presence");</p>
<p><span class="citation no-link">Miss. Code Ann. § 99</span>-37 (Supp. 1998) (for indictable offense committed in presence of officer); § 45-321(1)(a)(vi) (by Highway Safety Patrol Officers of "any person or persons committing or attempting to commit any misdemeanor, felony or breach of the peace within their presence or view");</p>
<p><span class="citation no-link">Mo. Rev. Stat. § 479.110</span> (2000) (of "any person who commits an offense in [the officer's] presence");</p>
<p><span class="citation no-link">Mont. Code Ann. § 46</span>-6311(1) (1997) (if "the officer has probable cause to believe that the person is committing an offense");</p>
<p><span class="citation no-link">Neb. Rev. Stat. § 29-404.02</span>(2)(d) (1995) (when the officer has probable cause to believe that the person has committed a misdemeanor in his presence);</p>
<p><span class="citation no-link">Nev. Rev. Stat. § 171.172</span> (1997) (in fresh pursuit of a person who commits "any criminal offense" in the presence of the officer);</p>
<p>N. H. Rev. Stat. Ann. § 614:7 (Supp. 2000) (in fresh pursuit of any person who has committed "any criminal offense" in the presence of the officer); § 594:10(I)(a) (upon probable <span class="star-pagination">*358</span> cause for misdemeanor or violation committed in officer's presence);</p>
<p>N. J. Stat. Ann. § 53:2-1 (West Supp. 2000) ("for violations of the law committed in [the officers'] presence");</p>
<p>N. M. Stat. Ann. § 3-13-2(A)(4)(d) (1999) ("any person in the act of violating the laws of the state or the ordinances of the municipality"); § 30-16-16(B) (1994) (for falsely obtaining services or accommodations); § 30-16-23 (of any person officer has probable cause to believe has committed the crime of shoplifting);</p>
<p>N. Y. Crim. Proc. Law §§ 140.10(1)(a) and (2) (McKinney Supp. 2001) (when officer has probable cause to believe any offense has been committed in his presence and probable cause to believe person to be arrested committed the offense);</p>
<p>N. C. Gen. Stat. § 15A-401(b) (1999) (where an officer has probable cause to believe the person has committed "a criminal offense" in the officer's presence and for misdemeanors out of the officers presence in certain circumstances);</p>
<p>N. D. Cent. Code § 29-06-15(1)(a) (Supp. 1999) ("[f]or a public offense, committed or attempted in the officer's presence");</p>
<p><span class="citation no-link">Ohio Rev. Code Ann. § 2935.03</span> (1997 and Supp. 2000) (of a person "found violating . . . a law of this state, an ordinance of a municipal corporation, or a resolution of a township");</p>
<p>but see § 2935.26 (1997) (providing that notwithstanding any other provision of the Revised Code, when a law enforcement officer is otherwise authorized to arrest a person for the commission of a minor misdemeanor, the officer shall not arrest the person, but shall issue a citation, except in specified circumstances);</p>
<p>Okla. Stat., Tit. 22, § 196(1) (Supp. 2001) ("[f]or a public offense, committed or attempted in [the officer's] presence");</p>
<p>Ore. Rev. Stat. § 133.310(1) (1997) (upon probable cause for any felony, Class A misdemeanor, or any other offense in the <span class="star-pagination">*359</span> officer's presence except "traffic infractions" and minor "violations");</p>
<p>Pa. Stat. Ann., Tit. 71, § 252(a) (Purdon 1990) ("for all violations of the law, including laws regulating the use of the highways, which they may witness");</p>
<p>R. I. Gen. Laws § 12-73 (2000) (for misdemeanors and petty misdemeanors where "[t]he officer has reasonable grounds to believe that [the] person cannot be arrested later, or [m]ay cause injury to himself or herself or others or loss or damage to property unless immediately arrested");</p>
<p>S. C. Code Ann. § 17-13-30 (1985) (of persons who, in the presence of the officer, "violate any of the criminal laws of this State if such arrest be made at the time of such violation of law or immediately thereafter");</p>
<p>S. D. Codified Laws § 23A-3-2 (1998) ("[f]or a public offense, other than a petty offense, committed or attempted in [the officer's] presence");</p>
<p><span class="citation no-link">Tenn. Code Ann. § 40</span>-7103(a)(1) (Supp. 2000) ("[f]or a public offense committed or a breach of the peace threatened in the officer's presence"); see also § 40-7118(b)(1) (1997) (officer who has arrested a person for the commission of a misdemeanor should generally issue a citation to such arrested person to appear in court in lieu of the continued custody and the taking of the arrested person before a magistrate);</p>
<p>Tex. Code Crim. Proc. Ann., Art. 14.01 (Vernon 1977) ("for any offense committed in his presence or within his view");</p>
<p><span class="citation no-link">Utah Code Ann. § 10</span>-3915 (1999) (for "any offense directly prohibited by the laws of this state or by ordinance"); § 77 7-2 (for any public offense committed in presence of officer);</p>
<p>Vt. Rule Crim. Proc. 3(a) (2000) (where officer has probable cause to believe that "a crime" is committed in his presence);</p>
<p>see also Rule 3(c) (law enforcement officer acting without warrant who is authorized to arrest a person for a misdemeanor should generally issue a citation to appear before a judicial officer in lieu of arrest);</p>
<p><span class="star-pagination">*360</span> <span class="citation no-link">Va. Code Ann. § 19.2-81</span> (2000) (of "any person who commits any crime in the presence of [an] officer");</p>
<p><span class="citation no-link">Wash. Rev. Code § 10.31.100</span> (Supp. 2001), as amended by 2000 Wash. Laws 119, § 4 (for misdemeanors committed in the presence of the officer);</p>
<p><span class="citation no-link">W. Va. Code § 62-10-9</span> (2000) ("for all violations of any of the criminal laws of the United States, or of this state, when committed in [an officer's] presence");</p>
<p><span class="citation no-link">Wis. Stat. § 968.07</span>(1)(d) (1998) (when "[t]here are reasonable grounds to believe that the person is committing or has committed a crime"); and</p>
<p><span class="citation no-link">Wyo. Stat. Ann. § 7</span>-2102(b)(i) (1999) (when "[a]ny criminal offense" is committed "in the officer's presence").</p>
<p>Justice O'Connor, with whom Justice Stevens, Justice Ginsburg, and Justice Breyer join, dissenting.</p>
<p>The Fourth Amendment guarantees the right to be free from "unreasonable searches and seizures." The Court recognizes that the arrest of Gail Atwater was a "pointless indignity" that served no discernible state interest, <i>ante,</i> at 347, and yet holds that her arrest was constitutionally permissible. Because the Court's position is inconsistent with the explicit guarantee of the Fourth Amendment, I dissent.</p>
<p></p>
<h2>I</h2>
<p>A full custodial arrest, such as the one to which Ms. Atwater was subjected, is the quintessential seizure. See <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 585</a></span> (1980). When a full custodial arrest is effected without a warrant, the plain language of the Fourth Amendment requires that the arrest be reasonable. See <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">ibid.</a></span></i> It is beyond cavil that "[t]he touchstone of our analysis under the Fourth Amendment is always `the reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security.' " <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 108-109</a></span> (1977) <i>(per curiam)</i> (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, 19 <span class="star-pagination">*361</span> (1968)). See also, <i>e. g., </i><i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#71" aria-description="Citation for case: United States v. Ramirez">523 U. S. 65, 71</a></span> (1998); <i>Maryland</i> v. <i>Wilson,</i> <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#411" aria-description="Citation for case: Maryland v. Wilson">519 U. S. 408, 411</a></span> (1997); <i>Ohio</i> v. <i>Robinette,</i> <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996); <i>Florida</i> v. <i>Jimeno,</i>  <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248, 250</a></span> (1991); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977).</p>
<p>We have "often looked to the common law in evaluating the reasonableness, for Fourth Amendment purposes, of police activity." <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 13</a></span> (1985). But history is just one of the tools we use in conducting the reasonableness inquiry. See <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 13-19</a></span>; see also <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#929" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 929</a></span> (1995); <i>Wyoming</i> v. <i>Houghton,</i>  <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#307" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 307</a></span> (1999) (Breyer, J., concurring). And when history is inconclusive, as the majority amply demonstrates it is in this case, see <i>ante,</i> at 326-345, we will "evaluate the search or seizure under traditional standards of reasonableness by assessing, on the one hand, the degree to which it intrudes upon an individual's privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests." <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 300</a></span>. See also, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 619</a></span> (1989); <i>Tennessee</i>  v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 8</a></span>; <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <i>Pennsylvania</i> v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Mimms, supra,</i> at 109</a></span>. In other words, in determining reasonableness, "[e]ach case is to be decided on its own facts and circumstances." <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931).</p>
<p>The majority gives a brief nod to this bedrock principle of our Fourth Amendment jurisprudence, and even acknowledges that "Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case." <i>Ante,</i> at 347. But instead of remedying this imbalance, the majority allows itself to be swayed by the worry that "every discretionary judgment in the field [will] be converted into an occasion for constitutional review." <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">Ibid.</a></span></i> It therefore mints a new rule that "[i]f an officer has probable cause to believe that an individual <span class="star-pagination">*362</span> has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender." <i>Ante,</i> at 354. This rule is not only unsupported by our precedent, but runs contrary to the principles that lie at the core of the Fourth Amendment.</p>
<p>As the majority tacitly acknowledges, we have never considered the precise question presented here, namely, the constitutionality of a warrantless arrest for an offense punishable only by fine. Cf. <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">ibid.</a></span></i> Indeed, on the rare occasions that Members of this Court have contemplated such an arrest, they have indicated disapproval. See, <i>e. g., </i><i>Gustafson</i>  v. <i>Florida,</i> <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266-267</a></span> (1973) (Stewart, J., concurring) ("[A] persuasive claim might have been made . . . that the custodial arrest of the petitioner for a minor traffic offense violated his rights under the Fourth and Fourteenth Amendments. But no such claim has been made"); <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#238" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 238, n. 2</a></span> (1973) (Powell, J., concurring) (the validity of a custodial arrest for a minor traffic offense is not "self-evident").</p>
<p>To be sure, we have held that the existence of probable cause is a necessary condition for an arrest. See <i>Dunaway</i>  v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979). And in the case of felonies punishable by a term of imprisonment, we have held that the existence of probable cause is also a sufficient condition for an arrest. See <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#416" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 416-417</a></span> (1976). In <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> however, there was a clear and consistently applied common law rule permitting warrantless felony arrests. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#417" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 417-422</a></span>. Accordingly, our inquiry ended there and we had no need to assess the reasonableness of such arrests by weighing individual liberty interests against state interests. Cf. <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 299-300</a></span>; <i>Tennessee</i> v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#26" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 26</a></span> (O'Connor, J., dissenting) (criticizing majority for disregarding undisputed common law rule).</p>
<p>Here, however, we have no such luxury. The Court's thorough exegesis makes it abundantly clear that warrantless <span class="star-pagination">*363</span> misdemeanor arrests were not the subject of a clear and consistently applied rule at common law. See, <i>e. g., ante,</i> at 332 (finding "disagreement, not unanimity, among both the common-law jurists and the text writers"); <i>ante,</i> at 335 (acknowledging that certain early English statutes serve only to "riddle Atwater's supposed common-law rule with enough exceptions to unsettle any contention [that there was a clear common-law rule barring warrantless arrests for misdemeanors that were not breaches of the peace]"). We therefore must engage in the balancing test required by the Fourth Amendment. See <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 299-300</a></span>. While probable cause is surely a necessary condition for warrantless arrests for fine-only offenses, see <i>Dunaway</i> v. <i>New York, supra,</i> at 213-214, any realistic assessment of the interests implicated by such arrests demonstrates that probable cause alone is not a sufficient condition. See <i>infra,</i>  at 364-366.</p>
<p>Our decision in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), is not to the contrary. The specific question presented there was whether, in evaluating the Fourth Amendment reasonableness of a traffic stop, the subjective intent of the police officer is a relevant consideration. <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#808" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 808, 814</a></span>. We held that it is not, and stated that "[t]he making of a traffic stop . . . is governed by the usual rule that probable cause to believe the law has been broken `outbalances' private interest in avoiding police contact." <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 818</a></span>.</p>
<p>We of course did not have occasion in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> to consider the constitutional preconditions for warrantless arrests for fine-only offenses. Nor should our words be taken beyond their context. There are significant qualitative differences between a traffic stop and a full custodial arrest. While both are seizures that fall within the ambit of the Fourth Amendment, the latter entails a much greater intrusion on an individual's liberty and privacy interests. As we have said, "[a] motorist's expectations, when he sees a policeman's light flashing behind him, are that he will be obliged to spend <span class="star-pagination">*364</span> a short period of time answering questions and waiting while the officer checks his license and registration, that he may be given a citation, but that in the end he most likely will be allowed to continue on his way." <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#437" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 437</a></span> (1984). Thus, when there is probable cause to believe that a person has violated a minor traffic law, there can be little question that the state interest in law enforcement will justify the relatively limited intrusion of a traffic stop. It is by no means certain, however, that where the offense is punishable only by fine, "probable cause to believe the law has been broken [will] `outbalanc[e]' private interest in avoiding" a full custodial arrest. <i>Whren</i> v. <i>United States, supra,</i> at 818. Justifying a full arrest by the same quantum of evidence that justifies a traffic stopeven though the offender cannot ultimately be imprisoned for her conductdefies any sense of proportionality and is in serious tension with the Fourth Amendment's proscription of unreasonable seizures.</p>
<p>A custodial arrest exacts an obvious toll on an individual's liberty and privacy, even when the period of custody is relatively brief. The arrestee is subject to a full search of her person and confiscation of her possessions. <i>United States</i> v. <i><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra</a></span></i><i>.</i> If the arrestee is the occupant of a car, the entire passenger compartment of the car, including packages therein, is subject to search as well. See <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981). The arrestee may be detained for up to 48 hours without having a magistrate determine whether there in fact was probable cause for the arrest. See <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S. 44</a></span> (1991). Because people arrested for all types of violent and nonviolent offenses may be housed together awaiting such review, this detention period is potentially dangerous. Rosazza &amp; Cook, Jail Intake: Managing A Critical FunctionPart One: Resources, 13 American Jails 35 (Mar./Apr. 1999). And once the period of custody is over, the fact of the arrest is a permanent <span class="star-pagination">*365</span> part of the public record. Cf. <i>Paul</i> v. <i>Davis,</i> <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U. S. 693</a></span> (1976).</p>
<p>We have said that "the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State's interest in arresting individuals suspected of committing that offense." <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#754" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 754, n. 14</a></span> (1984). If the State has decided that a fine, and not imprisonment, is the appropriate punishment for an offense, the State's interest in taking a person suspected of committing that offense into custody is surely limited, at best. This is not to say that the State will never have such an interest. A full custodial arrest may on occasion vindicate legitimate state interests, even if the crime is punishable only by fine. Arrest is the surest way to abate criminal conduct. It may also allow the police to verify the offender's identity and, if the offender poses a flight risk, to ensure her appearance at trial. But when such considerations are not present, a citation or summons may serve the State's remaining law enforcement interests every bit as effectively as an arrest. Cf. Lodging for State of Texas et al. as <i>Amici Curiae</i> (Texas Department of Public Safety, Student Handout, Traffic Law Enforcement 1 (1999)) ("Citations. . . . Definitiona means of getting violators to court without physical arrest. A citation should be used when it will serve this purpose except when by issuing a citation and releasing the violator, the safety of the public and/or the violator might be imperiled as in the case of D. W. I.").</p>
<p>Because a full custodial arrest is such a severe intrusion on an individual's liberty, its reasonableness hinges on "the degree to which it is needed for the promotion of legitimate governmental interests." <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S., at 300</a></span>. In light of the availability of citations to promote a State's interests when a fine-only offense has been committed, I cannot concur in a rule which deems a full custodial arrest to be reasonable in every circumstance. Giving police <span class="star-pagination">*366</span> officers constitutional carte blanche to effect an arrest whenever there is probable cause to believe a fine-only misdemeanor has been committed is irreconcilable with the Fourth Amendment's command that seizures be reasonable. Instead, I would require that when there is probable cause to believe that a fine-only offense has been committed, the police officer should issue a citation unless the officer is "able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant [the additional] intrusion" of a full custodial arrest. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span>.</p>
<p>The majority insists that a bright-line rule focused on probable cause is necessary to vindicate the State's interest in easily administrable law enforcement rules. See <i>ante,</i> at 347-351. Probable cause itself, however, is not a model of precision. "The quantum of information which constitutes probable causeevidence which would `warrant a man of reasonable caution in the belief' that a [crime] has been committedmust be measured by the facts of the particular case." <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479</a></span> (1963) (citation omitted). The rule I proposewhich merely requires a legitimate reason for the decision to escalate the seizure into a full custodial arrestthus does not undermine an otherwise "clear and simple" rule. Cf. <i>ante,</i> at 347.</p>
<p>While clarity is certainly a value worthy of consideration in our Fourth Amendment jurisprudence, it by no means trumps the values of liberty and privacy at the heart of the Amendment's protections. What the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> rule lacks in precision it makes up for in fidelity to the Fourth Amendment's command of reasonableness and sensitivity to the competing values protected by that Amendment. Over the past 30 years, it appears that the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> rule has been workable and easily applied by officers on the street.</p>
<p>At bottom, the majority offers two related reasons why a bright-line rule is necessary: the fear that officers who arrest for fine-only offenses will be subject to "personal [42 U. S. C.] <span class="star-pagination">*367</span> § 1983 liability for the misapplication of a constitutional standard," <i>ante,</i> at 350, and the resulting "systematic disincentive to arrest . . . where . . . arresting would serve an important societal interest," <i>ante,</i> at 351. These concerns are certainly valid, but they are more than adequately resolved by the doctrine of qualified immunity.</p>
<p>Qualified immunity was created to shield government officials from civil liability for the performance of discretionary functions so long as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known. See <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). This doctrine is "the best attainable accommodation of competing values," namely, the obligation to enforce constitutional guarantees and the need to protect officials who are required to exercise their discretion. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald"><i>Id.,</i> at 814</a></span>.</p>
<p>In <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635</a></span> (1987), we made clear that the standard of reasonableness for a search or seizure under the Fourth Amendment is distinct from the standard of reasonableness for qualified immunity purposes. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton"><i>Id.,</i> at 641</a></span>. If a law enforcement officer "reasonably but mistakenly conclude[s]" that the constitutional predicate for a search or seizure is present, he "should not be held personally liable." <i><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Ibid.</a></span></i> </p>
<p>This doctrine thus allays any concerns about liability or disincentives to arrest. If, for example, an officer reasonably thinks that a suspect poses a flight risk or might be a danger to the community if released, cf. <i>ante,</i> at 351, he may arrest without fear of the legal consequences. Similarly, if an officer reasonably concludes that a suspect may possess more than four ounces of marijuana and thus might be guilty of a felony, cf. <i>ante,</i> at 348-349, and n. 19, 351, the officer will be insulated from liability for arresting the suspect even if the initial assessment turns out to be factually incorrect. As we have said, "officials will not be liable for mere mistakes in judgment." <i>Butz</i> v. <i>Economou,</i> <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">438 U. S. 478</a></span>, 507 <span class="star-pagination">*368</span> (1978). Of course, even the specter of liability can entail substantial social costs, such as inhibiting public officials in the discharge of their duties. See, <i>e. g., </i><i>Harlow</i> v. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald"><i>Fitzgerald, supra,</i> at 814</a></span>. We may not ignore the central command of the Fourth Amendment, however, to avoid these costs.</p>
<p></p>
<h2>II</h2>
<p>The record in this case makes it abundantly clear that Ms. Atwater's arrest was constitutionally unreasonable. Atwater readily admitsas she did when Officer Turek pulled her overthat she violated Texas' seatbelt law. Brief for Petitioners 2-3; Record 381, 384. While Turek was justified in stopping Atwater, see <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#819" aria-description="Citation for case: Whren v. United States">517 U. S., at 819</a></span>, neither law nor reason supports his decision to arrest her instead of simply giving her a citation. The officer's actions cannot sensibly be viewed as a permissible means of balancing Atwater's Fourth Amendment interests with the State's own legitimate interests.</p>
<p>There is no question that Officer Turek's actions severely infringed Atwater's liberty and privacy. Turek was loud and accusatory from the moment he approached Atwater's car. Atwater's young children were terrified and hysterical. Yet when Atwater asked Turek to lower his voice because he was scaring the children, he responded by jabbing his finger in Atwater's face and saying, "You're going to jail." Record 382, 384. Having made the decision to arrest, Turek did not inform Atwater of her right to remain silent. <i>Id.,</i> at 390, 704. He instead asked for her license and insurance information. <i>Id.,</i> at 382. But cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>Atwater asked if she could at least take her children to a friend's house down the street before going to the police station. Record 384. But Turekwho had just castigated Atwater for not caring for her childrenrefused and said he would take the children into custody as well. <i>Id.,</i> at 384, 427, 704-705. Only the intervention of neighborhood <span class="star-pagination">*369</span> children who had witnessed the scene and summoned one of Atwater's friends saved the children from being hauled to jail with their mother. <i>Id.,</i> at 382, 385-386.</p>
<p>With the children gone, Officer Turek handcuffed Ms. Atwater with her hands behind her back, placed her in the police car, and drove her to the police station. <i>Id.,</i> at 386-387. Ironically, Turek did not secure Atwater in a seatbelt for the drive. <i>Id.,</i> at 386. At the station, Atwater was forced to remove her shoes, relinquish her possessions, and wait in a holding cell for about an hour. <i>Id.,</i> at 387, 706. A judge finally informed Atwater of her rights and the charges against her, and released her when she posted bond. <i>Id.,</i> at 387-388, 706. Atwater returned to the scene of the arrest, only to find that her car had been towed. <i>Id.,</i> at 389.</p>
<p>Ms. Atwater ultimately pleaded no contest to violating the seatbelt law and was fined $50. <i>Id.,</i> at 403. Even though that fine was the maximum penalty for her crime, <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span>(d) (1999), and even though Officer Turek has never articulated any justification for his actions, the city contends that arresting Atwater was constitutionally reasonable because it advanced two legitimate interests: "the enforcement of child safety laws and encouraging [Atwater] to appear for trial." Brief for Respondents 15.</p>
<p>It is difficult to see how arresting Atwater served either of these goals any more effectively than the issuance of a citation. With respect to the goal of law enforcement generally, Atwater did not pose a great danger to the community. She had been driving very slowlyapproximately 15 miles per hourin broad daylight on a residential street that had no other traffic. Record 380. Nor was she a repeat offender; until that day, she had received one traffic citation in her lifea ticket, more than 10 years earlier, for failure to signal a lane change. <span class="citation no-link"><i>Id.,</i> at 378</span>. Although Officer Turek had stopped Atwater approximately three months earlier because he thought that Atwater's son was not wearing a seatbelt, <span class="citation no-link"><i>id.,</i> at 420</span>, Turek had been mistaken, <span class="citation no-link"><i>id.,</i> at 379, 703</span>. <span class="star-pagination">*370</span> Moreover, Atwater immediately accepted responsibility and apologized for her conduct. <span class="citation no-link"><i>Id.,</i> at 381, 384, 420</span>. Thus, there was every indication that Atwater would have buckled herself and her children in had she been cited and allowed to leave.</p>
<p>With respect to the related goal of child welfare, the decision to arrest Atwater was nothing short of counterproductive. Atwater's children witnessed Officer Turek yell at their mother and threaten to take them all into custody. Ultimately, they were forced to leave her behind with Turek, knowing that she was being taken to jail. Understandably, the 3-year-old boy was "very, very, very traumatized." <span class="citation no-link"><i>Id.,</i>  at 393</span>. After the incident, he had to see a child psychologist regularly, who reported that the boy "felt very guilty that he couldn't stop this horrible thing . . . he was powerless to help his mother or sister." <span class="citation no-link"><i>Id.,</i> at 396</span>. Both of Atwater's children are now terrified at the sight of any police car. <span class="citation no-link"><i>Id.,</i>  at 393, 395</span>. According to Atwater, the arrest "just never leaves us. It's a conversation we have every other day, once a week, and it'sit raises its head constantly in our lives." <span class="citation no-link"><i>Id.,</i> at 395</span>.</p>
<p>Citing Atwater surely would have served the children's interests well. It would have taught Atwater to ensure that her children were buckled up in the future. It also would have taught the children an important lesson in accepting responsibility and obeying the law. Arresting Atwater, though, taught the children an entirely different lesson: that "the bad person could just as easily be the policeman as it could be the most horrible person they could imagine." <i><span class="citation no-link">Ibid.</span></i> </p>
<p>Respondents also contend that the arrest was necessary to ensure Atwater's appearance in court. Atwater, however, was far from a flight risk. A 16-year resident of Lago Vista, population 2,486, Atwater was not likely to abscond. See Record 376; Texas State Data Center, 1997 Total Population Estimates for Texas Places 15 (Sept. 1998). Although she <span class="star-pagination">*371</span> was unable to produce her driver's license because it had been stolen, she gave Officer Turek her license number and address. Record 386. In addition, Officer Turek knew from their previous encounter that Atwater was a local resident.</p>
<p>The city's justifications fall far short of rationalizing the extraordinary intrusion on Gail Atwater and her children. Measuring "the degree to which [Atwater's custodial arrest was] needed for the promotion of legitimate governmental interests," against "the degree to which it intrud[ed] upon [her] privacy," <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S., at 300</a></span>, it can hardly be doubted that Turek's actions were disproportionate to Atwater's crime. The majority's assessment that "Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case," <i>ante,</i> at 347, is quite correct. In my view, the Fourth Amendment inquiry ends there.</p>
<p></p>
<h2>III</h2>
<p>The Court's error, however, does not merely affect the disposition of this case. The <i>per se</i> rule that the Court creates has potentially serious consequences for the everyday lives of Americans. A broad range of conduct falls into the category of fine-only misdemeanors. In Texas alone, for example, disobeying any sort of traffic warning sign is a misdemeanor punishable only by fine, see <span class="citation no-link">Tex. Transp. Code Ann. § 472.022</span> (1999 and Supp. 2000-2001), as is failing to pay a highway toll, see § 284.070, and driving with expired license plates, see § 502.407. Nor are fine-only crimes limited to the traffic context. In several States, for example, littering is a criminal offense punishable only by fine. See, <i>e. g.,</i> Cal. Penal Code Ann. § 374.7 (West 1999); Ga. Code Ann. § 16 7-43 (1996); <span class="citation no-link">Iowa Code §§ 321.369</span>, 805.8(2)(af) (Supp. 2001).</p>
<p>To be sure, such laws are valid and wise exercises of the States' power to protect the public health and welfare. My concern lies not with the decision to enact or enforce these <span class="star-pagination">*372</span> laws, but rather with the manner in which they may be enforced. Under today's holding, when a police officer has probable cause to believe that a fine-only misdemeanor offense has occurred, that officer may stop the suspect, issue a citation, and let the person continue on her way. Cf. <i>Whren</i>  v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#806" aria-description="Citation for case: Whren v. United States">517 U. S., at 806</a></span>. Or, if a traffic violation, the officer may stop the car, arrest the driver, see <i>ante,</i> at 354, search the driver, see <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S., at 235</a></span>, search the entire passenger compartment of the car including any purse or package inside, see <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>, and impound the car and inventory all of its contents, see <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#374" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 374</a></span> (1987); <i>Florida</i> v. <i>Wells,</i> <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4-5</a></span> (1990). Although the Fourth Amendment expressly requires that the latter course be a reasonable and proportional response to the circumstances of the offense, the majority gives officers unfettered discretion to choose that course without articulating a single reason why such action is appropriate.</p>
<p>Such unbounded discretion carries with it grave potential for abuse. The majority takes comfort in the lack of evidence of "an epidemic of unnecessary minor-offense arrests." <i>Ante,</i> at 353, and n. 25. But the relatively small number of published cases dealing with such arrests proves little and should provide little solace. Indeed, as the recent debate over racial profiling demonstrates all too clearly, a relatively minor traffic infraction may often serve as an excuse for stopping and harassing an individual. After today, the arsenal available to any officer extends to a full arrest and the searches permissible concomitant to that arrest. An officer's subjective motivations for making a traffic stop are not relevant considerations in determining the reasonableness of the stop. See <i>Whren</i> v. <i>United States, supra,</i> at 813. But it is precisely because these motivations are beyond our purview that we must vigilantly ensure that officers' poststop actionswhich are properly within our reachcomport with the Fourth Amendment's guarantee of reasonableness.</p>
<p></p>
<h2>
<span class="star-pagination">*373</span> * * *</h2>
<p>The Court neglects the Fourth Amendment's express command in the name of administrative ease. In so doing, it cloaks the pointless indignity that Gail Atwater suffered with the mantle of reasonableness. I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the American Civil Liberties Union et al. by <i>Susan N. He

[...TRUNCATED 19712 of 139712 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Banks v. Dretke.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Banks v. Dretke"
type: case
citation: ""
parallel_cite: "540 U.S. 668; 124 S. Ct. 1256; 157 L. Ed. 2d 1166; 72 U.S.L.W. 4193; 17 Fla. L. Weekly Fed. S 153"
neutral_cite: 2004 U.S. LEXIS 1621
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-02-24
docket: 02-8286
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Banks v. Dretke
  varies_by_point: false
  scope_note: "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/131165/banks-v-dretke/"
  cluster_id: 131165
  opinion_id: 131165
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Strickler v. Greene]]", "[[Giglio v. United States]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]", "[[Napue v. Illinois]]"]
aliases: []
tags: ["case", "brady", "giglio", "impeachment-evidence", "informant", "prosecutorial-misconduct", "due-process"]
holding: "A Brady violation occurred where the State withheld that a key prosecution witness was a paid police informant and affirmatively represented it had disclosed everything; a defendant who reasonably relies on the prosecution's representations does not forfeit the claim by failing to discover the concealed evidence — 'prosecutor may hide, defendant must seek' is not tenable."
lake:
  record_id: Banks v. Dretke
  status: verified
  projected_at: 2026-07-06
---

# Banks v. Dretke

*540 U.S. 668 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Delma Banks was convicted of capital murder and sentenced to death in Texas. Two key prosecution witnesses, Robert Farr and Charles Cook, helped secure the conviction and death sentence. Farr — who supplied much of the evidence that Banks would commit future violence — was in fact a paid police informant, and the State had also withheld a transcript of a pretrial interview in which Cook's testimony was coached. Throughout trial and state postconviction proceedings the prosecution represented that it had disclosed everything and even denied that Farr was an informant. Banks raised the suppressed-evidence claims on federal [[Common Legal Terms#habeas-corpus|habeas]].

## Issue
Whether Banks established a Brady violation as to Farr's concealed informant status — and whether his failure, in state proceedings, to prove what the State had hidden barred federal [[Common Legal Terms#habeas-corpus|habeas]] relief.

## Rule
The Court reiterated *[[Brady v. Maryland|Brady]]*'s rule and the three-part test from [[Strickler v. Greene]]: a *[[Brady v. Maryland|Brady]]* "prosecutorial misconduct claim" has three essential components — "The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." — 540 U.S. at 691 (quoting *Strickler*, 527 U.S. at 281–282). ^pin-691

A defendant need not police the prosecution's honesty. "A rule thus declaring 'prosecutor may hide, defendant must seek,' is not tenable in a system constitutionally bound to accord defendants due process." — 540 U.S. at 696. ^pin-696

Where the State elects to call an informant as a witness, "[n]othing in *Roviaro*, or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion." — 540 U.S. at 698. ^pin-698

## Application
Farr was a paid informant and a key witness at both the guilt and penalty phases of Banks's capital trial, so his concealed status was favorable impeachment evidence; the State suppressed it, even affirmatively denying he was an informant; and the suppression prejudiced Banks at sentencing. Because the prosecution represented at trial and in postconviction that it had held nothing back, "[i]t was not incumbent on Banks to prove these representations false; rather, Banks was entitled to treat the prosecutor's submissions as truthful." His failure to obtain investigative assistance or to prove the concealment earlier therefore did not bar the claim — the State's own concealment supplied the "cause," and the same facts established the *[[Brady v. Maryland|Brady]]* prejudice. The Court reversed the dismissal of the Farr claim and the denial of a certificate of appealability on the Cook claim.

## Conclusion
Reversed in relevant part. Banks established (or was entitled to develop) a *[[Brady v. Maryland|Brady]]* violation as to Farr's concealed informant status; a defendant's reasonable reliance on the prosecution's representations excuses a failure to uncover the suppressed evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Ginsburg, J.; Thomas, J., joined in part by Scalia, J., concurring in part and dissenting in part).
- *Banks* sits in the [[Brady v. Maryland]] / [[Giglio v. United States]] impeachment-disclosure line and applies the [[Strickler v. Greene]] three-component framework and the materiality logic of [[Kyles v. Whitley]] and [[United States v. Bagley]]. It is the leading rejection of a "due diligence" defense to suppression. No negative treatment.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Banks v. Dretke*, 540 U.S. 668 (2004) — https://www.courtlistener.com/opinion/131165/banks-v-dretke/ — pinpoints: 691, 696, 698.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "62269c5ee5943d58", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Banks v. Dretke"}, "payload": {"all": [{"cite": "540 U.S. 668", "page": "668", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "540"}, {"cite": "124 S. Ct. 1256", "page": "1256", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "157 L. Ed. 2d 1166", "page": "1166", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "157"}, {"cite": "2004 U.S. LEXIS 1621", "page": "1621", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}, {"cite": "72 U.S.L.W. 4193", "page": "4193", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "72"}, {"cite": "17 Fla. L. Weekly Fed. S 153", "page": "153", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Banks v. Dretke"}}
{"assertion_id": "3e156e4d7294a4d8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-698", "record_id": "Banks v. Dretke"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-698", "pinpoint_status": "slip-only", "quote": "[n]othing in *Roviaro*, or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion.", "quote_fidelity": "mismatch", "record_id": "Banks v. Dretke", "star_marker": null}}
{"assertion_id": "5099dc7ca4dd955f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-696", "record_id": "Banks v. Dretke"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-696", "pinpoint_status": "slip-only", "quote": "A rule thus declaring 'prosecutor may hide, defendant must seek,' is not tenable in a system constitutionally bound to accord defendants due process.", "quote_fidelity": "mismatch", "record_id": "Banks v. Dretke", "star_marker": null}}
{"assertion_id": "588c85a3a90fc736", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-691", "record_id": "Banks v. Dretke"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-691", "pinpoint_status": "slip-only", "quote": "--- # Banks v. Dretke *540 U.S. 668 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Delma Banks was convicted of capital murder and sentenced to death in Texas. Two key prosecution witnesses, Robert Farr and Charles Cook, helped secure the conviction and death sentence. Farr — who supplied much of the evidence that Banks would commit future violence — was in fact a paid police informant, and the State had also withheld a transcript of a pretrial interview in which Cook's testimony was coached. Throughout trial and state postconviction proceedings the prosecution represented that it had disclosed everything and even denied that Farr was an informant. Banks raised the suppressed-evidence claims on federal habeas. ## Issue Whether Banks established a Brady violation as to Farr's concealed informant status — and whether his failure, in state proceedings, to prove what the State had hidden barred federal habeas relief. ## Rule The Court reiterated *Brady*'s rule and the three-part test from [[Strickler v. Greene]]: a *Brady*", "quote_fidelity": "mismatch", "record_id": "Banks v. Dretke", "star_marker": null}}
{"assertion_id": "a49ee5254cc15e35", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Banks v. Dretke"}, "payload": {"as_of_content": "2004-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Banks v. Dretke", "scope_note": "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim.", "varies_by_point": false}}
```

### lake record — Banks v. Dretke

```json
{
  "schema_version": "s2.v1",
  "record_id": "Banks v. Dretke",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Banks v. Dretke",
    "case_name_short": "Banks",
    "case_name_full": "Banks v. Dretke, Director, Texas Department of Criminal Justice, Correctional Institutions Division",
    "input_case_name": "Banks v. Dretke",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-02-24",
    "year": 2004,
    "docket": "02-8286",
    "cluster_id": 131165,
    "lead_opinion_id": 131165,
    "sibling_ids": [
      131165,
      9434551,
      9434552
    ],
    "absolute_url": "/opinion/131165/banks-v-dretke/",
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
        "cite": "540 U.S. 668",
        "volume": "540",
        "reporter": "U.S.",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1256",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1166",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4193",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4193",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 153",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "153",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 1621",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1621",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "540 U.S. 668",
        "volume": "540",
        "reporter": "U.S.",
        "page": "668",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 1256",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "1256",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "157 L. Ed. 2d 1166",
        "volume": "157",
        "reporter": "L. Ed. 2d",
        "page": "1166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 1621",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "1621",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "72 U.S.L.W. 4193",
        "volume": "72",
        "reporter": "U.S.L.W.",
        "page": "4193",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 Fla. L. Weekly Fed. S 153",
        "volume": "17",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "153",
        "type": 1,
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
      "id": "pin-691",
      "page": null,
      "quote": "--- # Banks v. Dretke *540 U.S. 668 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Delma Banks was convicted of capital murder and sentenced to death in Texas. Two key prosecution witnesses, Robert Farr and Charles Cook, helped secure the conviction and death sentence. Farr \u2014 who supplied much of the evidence that Banks would commit future violence \u2014 was in fact a paid police informant, and the State had also withheld a transcript of a pretrial interview in which Cook's testimony was coached. Throughout trial and state postconviction proceedings the prosecution represented that it had disclosed everything and even denied that Farr was an informant. Banks raised the suppressed-evidence claims on federal habeas. ## Issue Whether Banks established a Brady violation as to Farr's concealed informant status \u2014 and whether his failure, in state proceedings, to prove what the State had hidden barred federal habeas relief. ## Rule The Court reiterated *Brady*'s rule and the three-part test from [[Strickler v. Greene]]: a *Brady*",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-696",
      "page": null,
      "quote": "A rule thus declaring 'prosecutor may hide, defendant must seek,' is not tenable in a system constitutionally bound to accord defendants due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-698",
      "page": null,
      "quote": "[n]othing in *Roviaro*, or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Banks v. Dretke",
    "varies_by_point": false,
    "scope_note": "Good law. Reaffirms the Strickler three-component Brady test and holds the State cannot present an informant as a witness while concealing his informant status; a defendant's failure to ferret out concealed Brady material does not forfeit the claim.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 9435476,
          "cite": [
            "2023 Ohio 3894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anthony Juniper v. David Zook",
          "cluster_id": 4443845,
          "cite": [
            "876 F.3d 551"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joshua Frost v. Ron Van Boening",
          "cluster_id": 3187283,
          "cite": [
            "818 F.3d 469",
            "2016 WL 1085228",
            "2016 U.S. App. LEXIS 5077"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Randall Amado v. Terri Gonzalez",
          "cluster_id": 2683349,
          "cite": [
            "758 F.3d 1119",
            "2014 U.S. App. LEXIS 13710",
            "2014 WL 3377340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson",
          "cluster_id": 2659519,
          "cite": [
            "59 F. Supp. 3d 15",
            "2014 U.S. Dist. LEXIS 17008",
            "2014 WL 535461"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson",
          "cluster_id": 2659864,
          "cite": [
            "979 F. Supp. 2d 123",
            "2013 WL 5778318",
            "2013 U.S. Dist. LEXIS 153420"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timothy Hennis v. Frank Hemlick",
          "cluster_id": 621017,
          "cite": [
            "666 F.3d 270",
            "2012 WL 120054",
            "2012 U.S. App. LEXIS 923"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesse Gonzalez v. Robert Wong",
          "cluster_id": 618469,
          "cite": [
            "667 F.3d 965",
            "2011 U.S. App. LEXIS 24191",
            "2011 WL 6061514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Almada",
          "cluster_id": 177469,
          "cite": [
            "640 F.3d 931",
            "2011 WL 941606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mayle v. Felix",
          "cluster_id": 799989,
          "cite": [
            "162 L. Ed. 2d 582",
            "125 S. Ct. 2562",
            "545 U.S. 644",
            "2005 U.S. LEXIS 5016"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cone v. Bell",
          "cluster_id": 145883,
          "cite": [
            "173 L. Ed. 2d 701",
            "129 S. Ct. 1769",
            "556 U.S. 449",
            "2009 U.S. LEXIS 3298"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Goodman v. Praxair, Inc.",
          "cluster_id": 1426951,
          "cite": [
            "494 F.3d 458",
            "68 Fed. R. Serv. 3d 850",
            "2007 U.S. App. LEXIS 17631",
            "2007 WL 2121724"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo, United States of America v. Leonard A. Pelullo",
          "cluster_id": 789362,
          "cite": [
            "399 F.3d 197",
            "2005 WL 433589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lambert v. Blackwell",
          "cluster_id": 3013731,
          "cite": [
            "387 F.3d 210"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhoades v. State",
          "cluster_id": 874869,
          "cite": [
            "220 P.3d 1066",
            "148 Idaho 247",
            "2009 Ida. LEXIS 195"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Switzer",
          "cluster_id": 206098,
          "cite": [
            "179 L. Ed. 2d 233",
            "131 S. Ct. 1289",
            "562 U.S. 521",
            "2011 U.S. LEXIS 1905",
            "2011 D.A.R. 3506"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herbert Whitlock v. Charles Bruegge",
          "cluster_id": 801194,
          "cite": [
            "682 F.3d 567",
            "2012 WL 1939906",
            "2012 U.S. App. LEXIS 10825"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chenault",
          "cluster_id": 2710712,
          "cite": [
            "495 Mich. 142",
            "845 N.W.2d 731",
            "2014 Mich. LEXIS 601"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ketterer",
          "cluster_id": 2478526,
          "cite": [
            "2010 OH 3831",
            "126 Ohio St. 3d 448",
            "935 N.E.2d 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey Wogenstahl v. Betty Mitchell",
          "cluster_id": 621975,
          "cite": [
            "668 F.3d 307",
            "2012 WL 310819",
            "2012 U.S. App. LEXIS 1905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ketterer",
          "cluster_id": 2691519,
          "cite": [
            "2010 Ohio 3831"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zambrano",
          "cluster_id": 2517801,
          "cite": [
            "163 P.3d 4",
            "63 Cal. Rptr. 3d 297",
            "41 Cal. 4th 1082",
            "2007 Cal. LEXIS 8079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anton E. Barker v. Gary Fleming",
          "cluster_id": 791948,
          "cite": [
            "423 F.3d 1085",
            "2005 U.S. App. LEXIS 19372",
            "5 Cal. Daily Op. Serv. 8151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harm v. State",
          "cluster_id": 1893606,
          "cite": [
            "183 S.W.3d 403",
            "2006 Tex. Crim. App. LEXIS 117",
            "2006 WL 168374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Conway",
          "cluster_id": 2718013,
          "cite": [
            "763 F.3d 115",
            "2014 WL 3953234",
            "2014 U.S. App. LEXIS 15589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Joseph, Petitioner-Appellant/cross-Appellee v. Ralph Coyle, Warden, Respondent-Appellee/cross-Appellant",
          "cluster_id": 796039,
          "cite": [
            "469 F.3d 441",
            "2006 U.S. App. LEXIS 27697",
            "2006 WL 3250935"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Crow",
          "cluster_id": 4899382,
          "cite": [
            "4 F.4th 982"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Woods v. Stephen Sinclair",
          "cluster_id": 2720496,
          "cite": [
            "764 F.3d 1109",
            "2014 U.S. App. LEXIS 16386",
            "2014 WL 4179917"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Adams Hovey v. Robert L. Ayers, Jr., Acting Warden, California State Prison at San Quentin",
          "cluster_id": 795328,
          "cite": [
            "458 F.3d 892",
            "2006 WL 2325130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Byron Mitchell",
          "cluster_id": 785864,
          "cite": [
            "365 F.3d 215",
            "2004 U.S. App. LEXIS 8474",
            "2004 WL 908359"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lambert v. Blackwell",
          "cluster_id": 788147,
          "cite": [
            "387 F.3d 210",
            "2004 U.S. App. LEXIS 21176"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Socha v. Gary Boughton",
          "cluster_id": 2718114,
          "cite": [
            "763 F.3d 674",
            "2014 WL 3953932",
            "2014 U.S. App. LEXIS 15646"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Barton v. Warden, Southern Ohio Correctional Facility",
          "cluster_id": 2801073,
          "cite": [
            "786 F.3d 450",
            "2015 U.S. App. LEXIS 8020",
            "2015 WL 2262762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Banks v. Dretke:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(131165 OR 9434551 OR 9434552) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjg0MDc2ODAwMDAwJnM9MTc1MTI2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28131165+OR+9434551+OR+9434552%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(131165 OR 9434551 OR 9434552)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzYmcz0xMDQwNTUwJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28131165+OR+9434551+OR+9434552%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(131165 OR 9434551 OR 9434552)",
        "reviewed": 31,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 31,
        "triage_read": 2,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(131165 OR 9434551 OR 9434552)",
    "indexed_citing_opinions": 458,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 131165,
        "count": 390,
        "count_source": "search"
      },
      {
        "opinion_id": 9434551,
        "count": 79,
        "count_source": "search"
      },
      {
        "opinion_id": 9434552,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1115,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/banks-v-dretke.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3MTE0MDUmcz05NDg0MjQ5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28131165+OR+9434551+OR+9434552%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 131165,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 102436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 106997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 110662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 111862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 118359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 122258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1571252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1624564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 1637408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 131165,
        "cited_id": 2467197,
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
    "date_created": "2026-07-04T19:20:23Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:26:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:20:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Banks v. Dretke

```
<div>
<center><b><span class="citation" data-id="9434551"><a href="/opinion/131165/banks-v-dretke/" aria-description="Citation for case: Banks v. Dretke">540 U.S. 668</a></span> (2004)</b></center>
<center><h1>BANKS<br>
v.<br>
DRETKE, DIRECTOR, TEXAS DEPARTMENT OF CRIMINAL JUSTICE, CORRECTIONAL INSTITUTIONS DIVISION.</h1></center>
<center>No. 02-8286.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 8, 2003.</center>
<center>Decided February 24, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><span class="star-pagination">*669</span> <span class="star-pagination">*670</span> <span class="star-pagination">*671</span> <span class="star-pagination">*672</span> <span class="star-pagination">*673</span> <span class="star-pagination">*674</span> GINSBURG, J., delivered the opinion of the Court, in which REHNQUIST, C. J., and STEVENS, O'CONNOR, KENNEDY, SOUTER, and BREYER, JJ., joined, and in which SCALIA and THOMAS, JJ., joined as to Part III. THOMAS, J., filed an opinion concurring in part and dissenting in part, in which SCALIA, J., joined, <i>post,</i> p. 706.</p>
<p><i>George H. Kendall</i> argued the cause for petitioner. With him on the briefs were <i>Elaine R. Jones, Janai S. Nelson, Miriam Gohara,</i> and <i>Clifton L. Holmes.</i></p>
<p><i>Gena Bunn,</i> Assistant Attorney General of Texas, argued the cause for respondent. With her on the brief were <i>Greg Abbott,</i> Attorney General, <i>Barry R. McBee,</i> First Assistant Attorney General, <i>Jay Kimbrough,</i> Deputy Attorney General, and <i>Edward L. Marshall</i> and <i>Katherine D. Hayes,</i> Assistant Attorneys General.<sup>[*]</sup></p>
<p>JUSTICE [[author]]GINSBURG[[/author]] delivered the opinion of the Court.</p>
<p>Petitioner Delma Banks, Jr., was convicted of capital murder and sentenced to death. Prior to trial, the State advised <span class="star-pagination">*675</span> Banks's attorney there would be no need to litigate discovery issues, representing: "[W]e will, without the necessity of motions[,] provide you with all discovery to which you are entitled." App. 361, n. 1; App. to Pet. for Cert. A4 (both sources' internal quotation marks omitted). Despite that undertaking, the State withheld evidence that would have allowed Banks to discredit two essential prosecution witnesses. The State did not disclose that one of those witnesses was a paid police informant, nor did it disclose a pretrial transcript revealing that the other witness' trial testimony had been intensively coached by prosecutors and law enforcement officers.</p>
<p>Furthermore, the prosecution raised no red flag when the informant testified, untruthfully, that he never gave the police any statement and, indeed, had not talked to any police officer about the case until a few days before the trial. Instead of correcting the informant's false statements, the prosecutor told the jury that the witness "ha[d] been open and honest with you in every way," App. 140, and that his testimony was of the "utmost significance," <i>id.,</i> at 146. Similarly, the prosecution allowed the other key witness to convey, untruthfully, that his testimony was entirely unrehearsed. Through direct appeal and state collateral review proceedings, the State continued to hold secret the key witnesses' links to the police and allowed their false statements to stand uncorrected.</p>
<p>Ultimately, through discovery and an evidentiary hearing authorized in a federal habeas corpus proceeding, the long-suppressed evidence came to light. The District Court granted Banks relief from the death penalty, but the Court of Appeals reversed. In the latter court's judgment, Banks had documented his claims of prosecutorial misconduct too late and in the wrong forum; therefore he did not qualify for federal-court relief. We reverse that judgment. When police or prosecutors conceal significant exculpatory or impeaching <span class="star-pagination">*676</span> material in the State's possession, it is ordinarily incumbent on the State to set the record straight.</p>
<p></p>
<h2>I</h2>
<p>On April 14, 1980, police found the corpse of 16-year-old Richard Whitehead in Pocket Park, east of Nash, Texas, a town in the vicinity of Texarkana. <i>Id.,</i> at 8, 141.<sup>[1]</sup> A preliminary autopsy revealed that Whitehead had been shot three times. <i>Id.,</i> at 10. Bowie County Deputy Sheriff Willie Huff, lead investigator of the death, learned from two witnesses that Whitehead had been in the company of petitioner, 21-year-old Delma Banks, Jr., late on the evening of April 11. <i>Id.,</i> at 11-15, 144; <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (Tex. Crim. App. 1982) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/904/">464 U. S. 904</a></span> (1983). On April 23, Huff received a call from a confidential informant reporting that "Banks was coming to Dallas to meet an individual and get a weapon." App. 15. That evening, Huff and other officers followed Banks to South Dallas, where Banks visited a residence. <i>Ibid.;</i> Brief for Petitioner 3. Police stopped Banks's vehicle en route from Dallas, found a handgun in the car, and arrested the car's occupants. App. 16. Returning to the Dallas residence Banks had visited, Huff encountered and interviewed Charles Cook and recovered a second gun, a weapon Cook said Banks had left with him several days earlier. <i>Ibid.</i> Tests later identified the second gun as the Whitehead murder weapon. <i>Id.,</i> at 17.</p>
<p>In a May 21, 1980, pretrial hearing, Banks's counsel sought information from Huff concerning the confidential informant who told Huff that Banks would be driving to Dallas. <i>Id.,</i> at 21. Huff was unresponsive. <i>Ibid.</i> Any information that might reveal the identity of the informant, the prosecution <span class="star-pagination">*677</span> urged, was privileged. <i>Id.,</i> at 23. The trial court sustained the State's objection. <i>Id.,</i> at 24. Several weeks later, in a July 7, 1980, letter, the prosecution advised Banks's counsel that "[the State] will, without necessity of motions provide you with all discovery to which you are entitled." <i>Id.,</i> at 361, n. 1; App. to Pet. for Cert. A4 (both sources' internal quotation marks omitted).</p>
<p>The guilt phase of Banks's trial spanned two days in September 1980. See Brief for Petitioner 2; App. to Pet. for Cert. C3. Witnesses testified to seeing Banks and Whitehead together on April 11 in Whitehead's green Mustang, and to hearing gunshots in Pocket Park at 4 a.m. on April 12. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d, at 131</a></span>. Charles Cook testified that Banks arrived in Dallas in a green Mustang at about 8:15 a.m. on April 12, and stayed with Cook until April 14. App. 42-43, 47-53. Cook gave the following account of Banks's visit. On the morning of his arrival, Banks had blood on his leg and told Cook "he [had] got into it on the highway with a white boy." <i>Id.,</i> at 44. That night, Banks confessed to having "kill[ed] the white boy for the hell of it and take[n] his car and come to Dallas." <i>Id.,</i> at 48. During their ensuing conversation, Cook first noticed that "[Banks] had a pistol." <i>Id.,</i> at 49. Two days later, Banks left Dallas by bus. <i>Id.,</i> at 52-53. The next day, Cook abandoned the Mustang in West Dallas and sold Banks's gun to a neighbor. <i>Id.,</i> at 54. Cook further testified that, shortly before the police arrived at his residence to question him, Banks had revisited him and requested the gun. <i>Id.,</i> at 57.</p>
<p>On cross-examination, Cook three times represented that he had not talked to anyone about his testimony. <i>Id.,</i> at 59. In fact, however, Cook had at least one "pretrial practice sessio[n]" at which Huff and prosecutors intensively coached Cook for his appearance on the stand at Banks's trial. <i>Id.,</i> at 325, ¶ 10, 381-390; Joint Lodging Material 1-36 (transcript of pretrial preparatory session). The prosecution allowed Cook's misstatements to stand uncorrected. In its guilt-phase <span class="star-pagination">*678</span> summation, the prosecution told the jury "Cook brought you absolute truth." App. 84.</p>
<p>In addition to Cook, Robert Farr was a key witness for the prosecution. Corroborating parts of Cook's account, Farr testified to traveling to Dallas with Banks to retrieve Banks's gun. <i>Id.,</i> at 34-35. On cross-examination, defense counsel asked Farr whether he had "ever taken any money from some police officers," or "give[n] any police officers a statement." <i>Id.,</i> at 37-38. Farr answered no to both questions; he asserted emphatically that police officers had not promised him anything and that he had "talked to no one about this [case]" until a few days before trial. <i>Ibid.</i> These answers were untrue, but the State did not correct them. Farr was the paid informant who told Deputy Sheriff Huff that Banks would travel to Dallas in search of a gun. <i>Id.,</i> at 329; App. to Pet. for Cert. A4, A9. In a 1999 affidavit, Farr explained:</p>
<blockquote>"I assumed that if I did not help [Huff] with his investigation of Delma that he would have me arrested for drug charges. That's why I agreed to help [Huff]. I was afraid that if I didn't help him, I would be arrested. . . .</blockquote>
<blockquote>"Willie Huff asked me to help him find Delma's gun. I told [Huff] that he would have to pay me money right away for my help on the case. I think altogether he gave me about $200.00 for helping him. He paid me some of the money before I set Delma up. He paid me the rest after Delma was arrested and charged with murder. . . .</blockquote>
<blockquote>"In order to help Willie Huff, I had to set Delma up. I told Delma that I wanted to rob a pharmacy to get drugs and that I needed his gun to do it. I did not really plan to commit a robbery but I told Delma this so that he would give me his gun. . . . I convinced Delma to drive to Dallas with me to get the gun." App. 442-443, ¶¶ 6-8.</blockquote>
<p><span class="star-pagination">*679</span> The defense presented no evidence. App. to Pet. for Cert. A6. Banks was convicted of murder committed in the course of a robbery, in violation of <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(2) (1974). See App. to Pet. for Cert. C3.<sup>[2]</sup></p>
<p>The penalty phase ran its course the next day. <i><span class="citation no-link">Ibid.</span></i> Governed by the Texas statutory capital murder scheme applicable in 1980, the jury decided Banks's sentence by answering three "special issues." App. 142-143.<sup>[3]</sup> "If the jury unanimously answer[ed] `yes' to each issue submitted, the trial court [would be obliged to] sentence the defendant to death." <i>Penry</i> v. <i>Lynaugh,</i> <span class="citation" data-id="9842108"><a href="/opinion/112325/penry-v-lynaugh/#310" aria-description="Citation for case: Penry v. Lynaugh">492 U. S. 302, 310</a></span> (1989) (construing Texas' sentencing scheme); Tex. Code Crim. Proc. Ann., Arts. 37.071(c)-(e) (Vernon Supp. 1980). The critical question at the penalty phase in Banks's case was: "Do you find from the evidence beyond a reasonable doubt that there is a probability that the defendant, Delma Banks, Jr., would commit criminal acts of violence that would constitute a continuing threat to society?" App. 143 (internal quotation marks omitted).</p>
<p>On this question, the State offered two witnesses, Vetrano Jefferson and Robert Farr. <i>Id.,</i> at 104-113. Jefferson testified that, in early April 1980, Banks had struck him across <span class="star-pagination">*680</span> the face with a gun and threatened to kill him. <i>Id.,</i> at 104-106. Farr's testimony focused once more on the trip to Dallas to fetch Banks's gun. The gun was needed, Farr asserted, because "[w]e [Farr and Banks] were going to pull some robberies." <i>Id.,</i> at 108. According to Farr, Banks "said he would take care of it" if "there was any trouble during these burglaries." <i>Id.,</i> at 109. When the prosecution asked: "How did [Banks] say he would take care of it?" Farr responded: "[Banks] didn't go into any specifics, but he said it would be taken care of." <i>Ibid.</i></p>
<p>On cross-examination, defense counsel twice asked whether Farr had told Deputy Sheriff Huff of the Dallas trip. <i>Ibid.</i> The State remained silent as Farr twice perjuriously testified: "No, I did not." <i>Ibid.</i> Banks's counsel also inquired whether Farr had previously attempted to obtain prescription drugs by fraud, and, "up tight over that," would "testify to anything anybody want[ed] to hear." <i>Id.,</i> at 110. Farr first responded: "Can you prove it?" <i>Ibid.</i> Instructed by the court to answer defense counsel's questions, Farr again said: "No, I did not. . . ." <i>Ibid.</i></p>
<p>Two defense witnesses impeached Farr, but were, in turn, impeached themselves. James Kelley testified to Farr's attempts to obtain drugs by fraud; the prosecution impeached Kelley by eliciting his close relationship to Banks's girl-friend. <i>Id.,</i> at 124-129. Later, Kelley admitted to being drunk while on the stand. App. to Pet. for Cert. A13. Former Arkansas police officer Gary Owen testified that Farr, as a police informant in Arkansas, had given false information; the prosecution impeached Owen by bringing out his pending application for employment by defense counsel's private investigator. App. 129-131.</p>
<p>Banks's parents and acquaintances testified that Banks was a "respectful, churchgoing young man." App. to Pet. for Cert. A7; App. 137-139. Thereafter, Banks took the stand. He affirmed that he had "never before been convicted <span class="star-pagination">*681</span> of a felony." <i>Id.,</i> at 134.<sup>[4]</sup> Banks admitted striking Vetrano Jefferson in April 1980, and traveling to Dallas to obtain a gun in late April 1980. <i>Id.,</i> at 134-136. He denied, however, any intent to participate in robberies, asserting that Farr alone had planned to commit them. <i>Id.,</i> at 136-137. The prosecution suggested on cross-examination that Banks had been willing "to supply [Farr] the means and possible death weapon in an armed robbery case." <i>Id.,</i> at 137. Banks conceded as much. <i>Ibid.</i></p>
<p>During summation, the prosecution intimated that Banks had not been wholly truthful in this regard, suggesting that "a man doesn't travel two hundred miles, or whatever the distance is from here [Texarkana] to Dallas, Texas, to supply a person with a weapon." <i>Id.,</i> at 143. The State homed in on Farr's testimony that Banks said he would "take care" of any trouble arising during the robbery:</p>
<blockquote>"[Farr] said, `Man, you know, what i[f] there's trouble?' And [Banks] says, `Don't worry about it. I'll take care of it.' I think that speaks for itself, and I think you know what that means. . . . I submit to you beyond a reasonable doubt that the State has again met its burden of proof, and that the answer to question number two [propensity to commit violent criminal acts] should also be yes." <i>Id.,</i> at 140, 144. See also <i>id.,</i> at 146-147.</blockquote>
<p>Urging Farr's credibility, the prosecution called the jury's attention to Farr's admission, at trial, that he used narcotics. <i>Id.,</i> at 36, 140. Just as Farr had been truthful about his drug use, the prosecution suggested, he was also "open and honest with [the jury] in every way" in his penalty-phase testimony. <i>Id.,</i> at 140. Farr's testimony, the prosecution emphasized, was "of the utmost significance" because it <span class="star-pagination">*682</span> showed "[Banks] is a danger to friends and strangers, alike." <i>Id.,</i> at 146. Banks's effort to impeach Farr was ineffective, the prosecution further urged, because defense witness "Kelley kn[ew] nothing about the murder," and defense witness Owen "wish[ed] to please his future employers." <i>Id.,</i> at 148.</p>
<p>The jury answered yes to the three special issues, and the judge sentenced Banks to death. The Texas Court of Criminal Appeals denied Banks's direct appeal. <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#135" aria-description="Citation for case: Banks v. State">643 S. W. 2d, at 135</a></span>. Banks's first two state postconviction motions raised issues not implicated here; both were denied. <i>Ex parte Banks,</i> No. 13568-01 (Tex. Crim. App. 1984); <i>Ex parte Banks,</i> <span class="citation" data-id="9660579"><a href="/opinion/1624564/ex-parte-banks/#540" aria-description="Citation for case: Ex Parte Banks">769 S. W. 2d 539, 540</a></span> (Tex. Crim. App. 1989).</p>
<p>Banks's third state postconviction motion, filed January 13, 1992, presented questions later advanced in federal court and reiterated in the petition now before us. App. 150. Banks alleged "upon information and belief" that "the prosecution knowingly failed to turn over exculpatory evidence as required by [<i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963)]";<sup>[5]</sup> the withheld evidence, Banks asserted, "would have revealed Robert Farr as a police informant and Mr. Banks' arrest as a set-up." App. 180, ¶ 114 (internal quotation marks omitted). In support of this third state-court postconviction plea, Banks attached an unsigned affidavit from his girlfriend, Farr's sister-in-law Demetra Jefferson, which stated that Farr "was well-connected to law enforcement people," and consequently managed to stay out of "trouble" for illegally obtaining prescription drugs. <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#195" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 195, ¶ 7</a></span>. Banks alleged as well that during the guilt phase of his trial, the State deliberately withheld information "critical to the jury's assessment of Cook's credibility," including the "generous <span class="star-pagination">*683</span> `deal' [Cook had] cut with the prosecutors." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#152" aria-description="Citation for case: Brady v. Maryland"><i>Id.,</i> at 152, ¶ 2, 180, ¶ 114</a></span>.<sup>[6]</sup></p>
<p>The State's reply to Banks's pleading, filed October 6, 1992, "denie[d] each and every allegation of fact made by [Banks], except those supported by official court records and those specifically admitted." <i>Id.,</i> at 234; Tr. of Oral Arg. 32. "[N]othing was kept secret from the defense," the State represented. App. 234. While the reply specifically asserted that the State had made "no deal with Cook," <i>ibid.,</i> the State said nothing specific about Farr. Affidavits from Deputy Sheriff Huff and prosecutors accompanied the reply. <i>Id.,</i> at 241-243. The affiants denied any "deal, secret or otherwise, with Charles Cook," but they, too, like the State's pleading they supported, remained silent about Farr. <i>Ibid.</i></p>
<p>In February and July 1993 orders, the state postconviction court rejected Banks's claims. App. to Pet. for Cert. E1-E9, G1-G7. The court found that "there was no agreement between the State and the witness Charles Cook," but made no findings concerning Farr. <i>Id.,</i> at G2. In a January 10, 1996, one-page <i>per curiam</i> order, the Texas Court of Criminal Appeals upheld the lower court's disposition of Banks's motion. <i>Id.,</i> at D1.</p>
<p>On March 7, 1996, Banks filed the instant petition for a writ of habeas corpus in the United States District Court for the Eastern District of Texas. App. 248. He alleged multiple violations of his federal constitutional rights. App. to Pet. for Cert. C5-C7. Relevant here, Banks reasserted that the State had withheld material exculpatory evidence <span class="star-pagination">*684</span> "reveal[ing] Robert Farr as a police informant and Mr. Banks' arrest as a set-up." App. 260, ¶ 152 (internal quotation marks omitted). Banks also asserted that the State had concealed "Cook's enormous incentive to testify in a manner favorable to the [prosecution]." <i>Id.,</i> at 260, ¶ 153; App. to Pet. for Cert. C6-C7.<sup>[7]</sup> In June 1998, Banks moved for discovery and an evidentiary hearing to gain information from the State on the roles played and trial testimony provided by Farr and Cook. App. 262-266, 282-283, 286. The superintending Magistrate Judge allowed limited discovery regarding Cook, but found insufficient justification for inquiries concerning Farr. <i>Id.,</i> at 294-295.</p>
<p>Banks renewed his discovery and evidentiary hearing requests in February 1999. <i>Id.,</i> at 2, 300-331. This time, he proffered affidavits from both Farr and Cook to back up his claims that, as to each of these two key witnesses, the prosecution had wrongly withheld crucial exculpatory and impeaching evidence. <i>Id.,</i> at 322-331. Farr's affidavit affirmed that Farr had "set Delma up" by proposing the drive to Dallas and informing Deputy Sheriff Huff of the trip. <i>Id.,</i> at 329, ¶ 8, 442-443, ¶ 8; <i>supra,</i> at 678. Accounting for his unavailability earlier, Farr stated that less than a year after the Banks trial, he had left Texarkana, first for Oklahoma, then for California, because his police-informant work endangered his life. App. 330-331, 444; Pet. for Cert. 27, n. 12. Cook recalled that in preparation for his Banks trial testimony, he had participated in "three or four . . . practice sessions" at which prosecutors told him to testify "as they wanted [him] to, and that [he] would spend the rest of [his] life in prison if [he] did not." App. 325, ¶¶ 10-11.</p>
<p>On March 4, 1999, the Magistrate Judge issued an order establishing issues for an evidentiary hearing, <i>id.,</i> at 340, 346, at which she would consider Banks's claims that the State had withheld "crucial exculpatory and impeaching evidence" <span class="star-pagination">*685</span> concerning "two of the [S]tate's essential witnesses, Charles Cook and Robert Farr." <i>Id.,</i> at 340, 345 (internal quotation marks omitted). In anticipation of the hearing, the Magistrate Judge ordered disclosure of the Bowie County District Attorney's files. Brief for Petitioner 37-38; Tr. of June 7-8, 1999, Federal Evidentiary Hearing (ED Tex.), p. 30 (hereinafter Federal Evidentiary Hearing).</p>
<p>One item lodged in the District Attorney's files, turned over to Banks pursuant to the Magistrate Judge's disclosure order, was a 74-page transcript of a Cook interrogation. App. to Pet. for Cert. A10. The interrogation, conducted by Bowie County law enforcement officials and prosecutors, occurred in September 1980, shortly before the Banks trial. <i>Ibid.</i> The transcript revealed that the State's representatives had closely rehearsed Cook's testimony. In particular, the officials told Cook how to reconcile his testimony with affidavits to which he had earlier subscribed recounting Banks's visits to Dallas. See, <i>e. g.,</i> Joint Lodging Material 24 ("Your [April 1980] statement is obviously screwed up."); <i>id.,</i> at 26 ("[T]he way this statement should read is that. . . ."); <i>id.,</i> at 32 ("[L]et me tell you how this is going to work."); <i>id.,</i> at 36 ("That's not in your [earlier] statement."). Although the transcript did not bear on Banks's claim that the prosecution had a deal with Cook, it provided compelling evidence that Cook's testimony had been tutored by Banks's prosecutors. Without objection at the hearing, the Magistrate Judge admitted the September 1980 transcript into evidence. Brief for Petitioner 39; Federal Evidentiary Hearing 75-76.</p>
<p>Testifying at the evidentiary hearing, Deputy Sheriff Huff acknowledged, for the first time, that Farr was an informant and that he had been paid $200 for his involvement in the case. App. to Pet. for Cert. C43. As to Cook, a Banks trial prosecutor testified, in line with the State's consistent position, that no deal had been offered to gain Cook's trial testimony. <i>Id.,</i> at C45; Federal Evidentiary Hearing 52-53. <span class="star-pagination">*686</span> Defense counsel questioned the prosecutor about the September 1980 transcript, calling attention to discrepancies between the transcript and Cook's statements at trial. <i>Id.,</i> at 65-68. In a posthearing brief and again in proposed findings of fact and conclusions of law, Banks emphasized the suppression of the September 1980 transcript, noting the prosecution's obligation to disclose material, exculpatory evidence, and the assurance in this case that Banks would receive "all [the] discovery to which [Banks was] entitled." App. 360-361, and n. 1, 378-379 (internal quotation marks omitted); <i>supra,</i> at 677.</p>
<p>In a May 11, 2000, report and recommendation, the Magistrate Judge recommended a writ of habeas corpus with respect to Banks's death sentence, but not his conviction. App. to Pet. for Cert. C54. "[T]he State's failure to disclose Farr's informant status, coupled with trial counsel's dismal performance during the punishment phase," the Magistrate Judge concluded, "undermined the reliability of the jury's verdict regarding punishment." <i>Id.,</i> at C44. Finding no convincing evidence of a deal between the State and Cook, however, she recommended that the guilt-phase verdict remain undisturbed. <i>Id.,</i> at C46.</p>
<p>Banks moved to alter or amend the Magistrate Judge's report on the ground that it left unresolved a fully aired question, <i>i. e.,</i> whether Banks's rights were violated by the State's failure to disclose to the defense the prosecution's eve-of-trial interrogation of Cook. App. 398. That interrogation, Banks observed, could not be reconciled with Cook's insistence at trial that he had talked to no one about his testimony. <i>Id.,</i> at 400, n. 17; see <i>supra,</i> at 677.</p>
<p>The District Court adopted the Magistrate Judge's report and denied Banks's motion to amend the report. App. to Pet. for Cert. B6; App. 421-424. Concerning the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim, the District Court recognized that Banks had filed his federal petition in 1996, three years before he became aware of the September 1980 <span class="star-pagination">*687</span> transcript. App. 422-423. When the transcript surfaced in response to the Magistrate Judge's 1999 disclosure order, Banks raised that newly discovered, long withheld document in his proposed findings of fact and conclusions of law and, again, in his objections to the Magistrate Judge's report. <i>Id.,</i> at 423. The District Court concluded, however, that Banks had not properly pleaded a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim predicated on the withheld Cook rehearsal transcript. App. 422. When that <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim came to light, the District Court reasoned, Banks should have moved to amend or supplement his 1996 federal habeas petition specifically to include the 1999 discovery as a basis for relief. App. 423. Banks urged that a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim based on the September 1980 transcript had been aired by implied consent; under Federal Rule of Civil Procedure 15(b), he contended, the claim should have been treated as if raised in the pleadings. App. 433.<sup>[8]</sup> Banks sought, and the District Court denied, a certificate of appealability on this question. <i>Id.,</i> at 433, 436.</p>
<p>In an August 20, 2003, unpublished <i>per curiam</i> opinion, the Court of Appeals for the Fifth Circuit reversed the judgment of the District Court to the extent that it granted relief on the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and denied a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. App. to Pet. for Cert. A2, judgt. order reported at <span class="citation no-link">48 Fed. Appx. 104</span> (2002).<sup>[9]</sup> The <span class="star-pagination">*688</span> Court of Appeals observed that in his 1992 state-court postconviction application, Banks had not endeavored to develop the facts underpinning the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. App to Pet. for Cert. A19-A20. For that reason, the court held, the evidentiary proceeding ordered by the Magistrate Judge was unwarranted. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Ibid.</a></span></i> The Court of Appeals expressed no doubt that the prosecution had suppressed, prior to the federal habeas proceeding, Farr's informant status and his part in the fateful trip to Dallas. But Banks was not appropriately diligent in pursuing his state-court application, the Court of Appeals maintained. In the Fifth Circuit's view, Banks should have at that time attempted to locate Farr and question him; similarly, he should have asked to interview Deputy Sheriff Huff and other officers involved in investigating the crime. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A19, A22. If such efforts had proved unavailing, the Court of Appeals suggested, Banks might have applied to the state court for assistance. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A19. Banks's lack of diligence in pursuing his 1992 state-court plea, the Court of Appeals concluded, rendered the evidence uncovered in the federal habeas proceeding procedurally barred. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A22-A23.</p>
<p>In any event, the Fifth Circuit further concluded, Farr's status as an informant was not "materia[l]" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes. App. to Pet. for Cert. A32-A33. Banks had impeached Farr at trial by bringing out that he had been a police informant in Arkansas, and an unreliable one at that. <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Id.,</a></span></i> at A28, A32-A33; <i>supra,</i> at 680. Moreover, the Court of Appeals said, other witnesses had corroborated much of Farr's testimony against Banks. App. to Pet. for Cert. A32. Notably, Banks himself had acknowledged his willingness to get a gun for Farr's use in robberies. <i>Ibid.</i> In addition, the Fifth Circuit observed, the Magistrate Judge had relied on the cumulative effect of <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> error and the ineffectiveness of Banks's counsel at the penalty phase. App. to Pet. for Cert. A44. Banks himself, however, had not urged that position; he had argued <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and ineffective assistance of <span class="star-pagination">*689</span> counsel discretely, not cumulatively. App. to Pet. for Cert. A46-A47. Finally, in accord with the District Court, the Court of Appeals apparently regarded Rule 15(b) as inapplicable in habeas proceedings. App. to Pet. for Cert. A51-A52. The Fifth Circuit accordingly denied a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim. App. to Pet. for Cert. A52, A78.</p>
<p>With an execution date set for March 12, 2003, Banks applied to this Court for a writ of certiorari, presenting four issues: the tenability of his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim; a penalty-phase ineffective-assistance-of-counsel claim; the question whether, as to the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> transcript-suppression claim, a certificate of appealability was wrongly denied; and a claim of improper exclusion of minority jurors in violation of <i>Swain</i> v. <i>Alabama,</i> <span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">380 U. S. 202</a></span> (1965). Pet. for Cert. 23-24. We stayed Banks's execution on March 12, 2003, <span class="citation multiple-matches"><a href="/c/U.%20S./538/917/">538 U. S. 917</a></span>, and, on April 21, 2003, granted his petition on all questions other than his <i><span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">Swain</a></span></i> claim. <span class="citation multiple-matches"><a href="/c/U.%20S./538/977/">538 U. S. 977</a></span>. We now reverse the Court of Appeals' judgment dismissing Banks's Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and that Court's denial of a certificate of appealability on his Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.<sup>[10]</sup></p>
<p></p>
<h2>II</h2>
<p>We note, initially, that Banks's <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims arose under the regime in place prior to the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>. Turning to the tenability of those claims, we consider first Banks's Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim as it trains on his death sentence, see App. to Pet. for Cert. B6 (District Court granted habeas solely with respect to the capital sentence), and next, Banks's Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<p></p>
<h2>
<span class="star-pagination">*690</span> A</h2>
<p>To pursue habeas corpus relief in federal court, Banks first had to exhaust "the remedies available in the courts of the State." <span class="citation no-link">28 U. S. C. § 2254</span>(b) (1994 ed.); see <i>Rose</i> v. <i>Lundy,</i> <span class="citation" data-id="9428690"><a href="/opinion/110662/rose-v-lundy/#520" aria-description="Citation for case: Rose v. Lundy">455 U. S. 509, 520</a></span> (1982). Banks alleged in his January 1992 state-court application for a writ of habeas corpus that the prosecution knowingly failed to turn over exculpatory evidence involving Farr in violation of Banks's due process rights. App. 180. Banks thus satisfied the exhaustion requirement as to the legal ground for his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.<sup>[11]</sup></p>
<p>In state postconviction court, however, Banks failed to produce evidence establishing that Farr had served as a police informant in this case. As support for his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, Banks appended to his state-court application only Demetra Jefferson's hardly probative statement that Farr "was well-connected to law enforcement people." App. 195, ¶ 7; see <i>supra,</i> at 682. In the federal habeas forum, therefore, it was incumbent on Banks to show that he was not barred, by reason of the anterior state proceedings, from producing evidence to substantiate his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim. Banks "[would be] entitled to an evidentiary hearing [in federal court] if he [could] show cause for his failure to develop the <span class="star-pagination">*691</span> facts in state-court proceedings and actual prejudice resulting from that failure." <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#11" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1, 11</a></span> (1992).</p>
<p><i>Brady,</i> we reiterate, held that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. We set out in <i>Strickler</i> v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263, 281-282</a></span> (1999), the three components or essential elements of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> prosecutorial misconduct claim: "The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadvertently; and prejudice must have ensued." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 281-282</a></span>. "[C]ause and prejudice" in this case "parallel two of the three components of the alleged <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> violation itself." <i>Id.,</i> at 282. Corresponding to the second <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (evidence suppressed by the State), a petitioner shows "cause" when the reason for his failure to develop facts in state-court proceedings was the State's suppression of the relevant evidence; coincident with the third <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (prejudice), prejudice within the compass of the "cause and prejudice" requirement exists when the suppressed evidence is "material" for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#282" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 282</a></span>. As to the first <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> component (evidence favorable to the accused), beyond genuine debate, the suppressed evidence relevant here, Farr's paid informant status, qualifies as evidence advantageous to Banks. See App. to Pet. for Cert. A26 (Court of Appeals' recognition that "Farr's being a paid informant would certainly be favorable to Banks in attacking Farr's testimony"). Thus, if Banks succeeds in demonstrating "cause and prejudice," he will at the same time succeed in establishing the elements of his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> death penalty due process claim.</p>
<p></p>
<h2>
<span class="star-pagination">*692</span> B</h2>
<p>Our determination as to "cause" for Banks's failure to develop the facts in state-court proceedings is informed by <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>.</i><sup>[12]</sup> In that case, Virginia prosecutors told the petitioner, prior to trial, that "the prosecutor's files were open to the petitioner's counsel," thus "there was no need for a formal <i>[Brady]</i> motion." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#276" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 276</a></span>, n. 14 (quoting App. in <i>Strickler</i> v. <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Greene</a></span>,</i> O. T. 1998, No. 98-5864, pp. 212-213 (brackets in original)). The prosecution file given to the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner, however, did not include several documents prepared by an "importan[t]" prosecution witness, recounting the witness' initial difficulty recalling the events to which she testified at the petitioner's trial. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#273" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 273-275, 290</a></span>. Those absent-from-the-file documents could have been used to impeach the witness. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#273" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 273</a></span>. In state-court postconviction proceedings, the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner had unsuccessfully urged ineffective assistance of trial counsel based on counsel's failure to move, pretrial, for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. Answering that plea, the State asserted that a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> motion would have been superfluous, for the prosecution had maintained an open file policy pursuant to which it had disclosed all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#276" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 276, n. 14, 278</a></span>.</p>
<p>This Court determined that in the federal habeas proceedings, the <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> petitioner had shown cause for his failure to raise a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state court. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>. Three factors accounted for that determination:</p>
<blockquote>"(a) the prosecution withheld exculpatory evidence; (b) petitioner reasonably relied on the prosecution's open file policy as fulfilling the prosecution's duty to disclose such evidence; and (c) the [State] confirmed petitioner's reliance on the open file policy by asserting during state <span class="star-pagination">*693</span> habeas proceedings that petitioner had already received everything known to the government." <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Ibid.</a></span></i> (internal quotation marks omitted).<sup>[13]</sup></blockquote>
<p>This case is congruent with <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> in all three respects. First, the State knew of, but kept back, Farr's arrangement with Deputy Sheriff Huff. App. to Pet. for Cert. C43; Tr. of Oral Arg. 33; cf. <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#437" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419, 437</a></span> (1995) (prosecutors are responsible for "any favorable evidence known to the others acting on the government's behalf in the case, including the police"). Second, the State asserted, on the eve of trial, that it would disclose all <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material. App. 361, n. 1; see <i>supra,</i> at 677. As <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> instructs, Banks cannot be faulted for relying on that representation. See <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#283" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 283-284</a></span> (an "open file policy" is one factor that "explain[s] why trial counsel did not advance [a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i>] claim").</p>
<p>Third, in his January 1992 state habeas application, Banks asserted that Farr was a police informant and Banks's arrest, "a set-up." App. 180, ¶ 114 (internal quotation marks omitted). In its answer, the State denied Banks's assertion. <i>Id.,</i> at 234; see <i>supra,</i> at 683. The State thereby "confirmed" Banks's reliance on the prosecution's representation that it had fully disclosed all relevant information its file contained. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>; see <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 284</a></span> (state habeas counsel, as well as trial counsel, could reasonably rely on the State's representations). In short, because the State persisted in hiding Farr's informant status and misleadingly represented that it had complied in full with its <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> disclosure obligations, Banks had cause for failing to investigate, in state postconviction proceedings, Farr's connections to Deputy Sheriff Huff.</p>
<p><span class="star-pagination">*694</span> On the question of "cause," moreover, Banks's case is stronger than was the petitioner's in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> in a notable respect. As a prosecution witness in the guilt and penalty phases of Banks's trial, Farr repeatedly misrepresented his dealings with police; each time Farr responded untruthfully, the prosecution allowed his testimony to stand uncorrected. See <i>supra,</i> at 678-680. Farr denied taking money from or being promised anything by police officers, App. 37; he twice denied speaking with police officers, <i>id.,</i> at 38, and twice denied informing Deputy Sheriff Huff about Banks's trip to Dallas, <i>id.,</i> at 109. It has long been established that the prosecution's "deliberate deception of a court and jurors by the presentation of known false evidence is incompatible with rudimentary demands of justice." <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#153" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 153</a></span> (1972) (quoting <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935) <i>(per curiam)</i> (internal quotation marks omitted)). If it was reasonable for Banks to rely on the prosecution's full disclosure representation, it was also appropriate for Banks to assume that his prosecutors would not stoop to improper litigation conduct to advance prospects for gaining a conviction. See <i>Berger</i> v. <i>United States,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S. 78, 88</a></span> (1935); <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 284</a></span>.<sup>[14]</sup></p>
<p>The State presents three main arguments for distinguishing <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> on the issue of "cause," two of them endorsed <span class="star-pagination">*695</span> by the Court of Appeals. Brief for Respondent 15-20; App. to Pet. for Cert. A19, A22-A23; see <i>supra,</i> at 687-688. We conclude that none of these arguments accounts adequately for the State's concealment and misrepresentation regarding Farr's link to Deputy Sheriff Huff. The State first suggests that Banks's failure, during state postconviction proceedings, to "attempt to locate Farr and ascertain his true status," or to "interview the investigating officers, such as Deputy Huff, to ascertain Farr's status," undermines a finding of cause; the Fifth Circuit agreed. App. to Pet. for Cert. A22; Brief for Respondent 18-20. In the State's view, "[t]he question [of cause] revolves around Banks's conduct," particularly his lack of appropriate diligence in pursuing the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim before resorting to federal court. Brief for Respondent 14.<sup>[15]</sup></p>
<p>We rejected a similar argument in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>.</i> There, the State contended that examination of a witness' trial testimony, alongside a letter the witness published in a local newspaper, should have alerted the petitioner to the existence of undisclosed interviews of the witness by the police. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#284" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 284</a></span>, and n. 26. We found this contention insubstantial. In light of the State's open file policy, we noted, "it is especially unlikely that counsel would have suspected that additional impeaching evidence was being withheld." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#285" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 285</a></span>. Our decisions lend no support to the notion that defendants must scavenge for hints of undisclosed <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> material when the prosecution represents that all such material has been disclosed. As we observed in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> defense counsel has no "procedural obligation to assert constitutional error on the basis of mere suspicion that some prosecutorial <span class="star-pagination">*696</span> misstep may have occurred." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#286" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 286-287</a></span>. The "cause" inquiry, we have also observed, turns on events or circumstances "external to the defense." <i>Amadeo</i> v. <i>Zant,</i> <span class="citation" data-id="112078"><a href="/opinion/112078/amadeo-v-zant/#222" aria-description="Citation for case: Amadeo v. Zant">486 U. S. 214, 222</a></span> (1988) (quoting <i>Murray</i> v. <i>Carrier,</i> <span class="citation" data-id="9430624"><a href="/opinion/111727/murray-v-carrier/#488" aria-description="Citation for case: Murray v. Carrier">477 U. S. 478, 488</a></span> (1986)).</p>
<p>The State here nevertheless urges, in effect, that "the prosecution can lie and conceal and the prisoner still has the burden to . . . discover the evidence," Tr. of Oral Arg. 35, so long as the "potential existence" of a prosecutorial misconduct claim might have been detected, <i>id.,</i> at 36. A rule thus declaring "prosecutor may hide, defendant must seek," is not tenable in a system constitutionally bound to accord defendants due process. "Ordinarily, we presume that public officials have properly discharged their official duties." <i>Bracy</i> v. <i>Gramley,</i> <span class="citation" data-id="118123"><a href="/opinion/118123/bracy-v-gramley/#909" aria-description="Citation for case: Bracy v. Gramley">520 U. S. 899, 909</a></span> (1997) (quoting <i>United States</i> v. <i>Chemical Foundation, Inc.,</i> <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#14" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 14-15</a></span> (1926) (internal quotation marks omitted)). We have several times underscored the "special role played by the American prosecutor in the search for truth in criminal trials." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 281</a></span>; accord, <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#439" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 439-440</a></span>; <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#675" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 675, n. 6</a></span> (1985); <i>Berger,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S., at 88</a></span>. See also <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#484" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 484</a></span> (1928) (Brandeis, J., dissenting). Courts, litigants, and juries properly anticipate that "obligations [to refrain from improper methods to secure a conviction] . . . plainly rest[ing] upon the prosecuting attorney, will be faithfully observed." <i>Berger,</i> <span class="citation" data-id="102436"><a href="/opinion/102436/berger-v-united-states/#88" aria-description="Citation for case: Berger v. United States">295 U. S., at 88</a></span>. Prosecutors' dishonest conduct or unwarranted concealment should attract no judicial approbation. See <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#440" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 440</a></span> ("The prudence of the careful prosecutor should not . . . be discouraged.").</p>
<p>The State's second argument is a variant of the first. Specifically, the State argues, and the Court of Appeals accepted, that Banks cannot show cause because in the 1992 state-court postconviction proceedings, he failed to move for investigative assistance enabling him to inquire into Farr's <span class="star-pagination">*697</span> police connections, connections he then alleged, but failed to prove. Brief for Respondent 15-16; App. to Pet. for Cert. A19; see 1977 Tex. Gen. Laws ch. 789, § 2(d) (as amended) (instructing postconviction court to "designat[e] the issues of fact to be resolved," and giving the court discretion to "order affidavits, depositions, interrogatories, and hearings"). Armed in 1992 only with Demetra Jefferson's declaration that Farr was "well-connected to law enforcement people," App. 195, ¶ 7; see <i>supra,</i> at 682, Banks had little to proffer in support of a request for assistance from the state postconviction court. We assign no overriding significance to Banks's failure to invoke state-court assistance to which he had no clear entitlement. Cf. <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#286" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 286</a></span> ("Proper respect for state procedures counsels against a requirement that all possible claims be raised in state collateral proceedings, even when no known facts support them.").<sup>[16]</sup></p>
<p>Finally, relying on <i>Roviaro</i> v. <i>United States,</i> <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957), the State asserts that "disclosure [of an informant's identity] is not automatic," and, "[c]onsequently, it was Banks's duty to move for disclosure of otherwise privileged material." Brief for Respondent 17-18, n. 15. We need not linger over this argument. The issue of evidentiary law in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span></i> was whether (or when) the Government is obliged to reveal the identity of an undercover informer the Government does <i>not</i> call as a trial witness. <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#55" aria-description="Citation for case: Roviaro v. United States">353 U. S., at 55-56</a></span>. The Court there stated that no privilege obtains "[w]here the disclosure of an informer's identity, or of the contents of his communication, is relevant and helpful to the defense of an accused." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#60" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 60-61</a></span>. Accordingly, even though the informer in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span></i> did not testify, we held that disclosure <span class="star-pagination">*698</span> of his identity was necessary because he could have "amplif[ied] or contradict[ed] the testimony of government witnesses." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#64" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 64</a></span>.</p>
<p>Here, the State elected to call Farr as a witness. Indeed, he was a key witness at both guilt and punishment phases of Banks's capital trial. Farr's status as a paid informant was unquestionably "relevant"; similarly beyond doubt, disclosure of Farr's status would have been "helpful to [Banks's] defense." <span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#60" aria-description="Citation for case: Roviaro v. United States"><i>Id.,</i> at 60-61</a></span>. Nothing in <i><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">Roviaro</a></span>,</i> or any other decision of this Court, suggests that the State can examine an informant at trial, withholding acknowledgment of his informant status in the hope that defendant will not catch on, so will make no disclosure motion.</p>
<p>In summary, Banks's prosecutors represented at trial and in state postconviction proceedings that the State had held nothing back. Moreover, in state postconviction court, the State's pleading denied that Farr was an informant. App. 234; <i>supra,</i> at 683. It was not incumbent on Banks to prove these representations false; rather, Banks was entitled to treat the prosecutor's submissions as truthful. Accordingly, Banks has shown cause for failing to present evidence in state court capable of substantiating his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<p></p>
<h2>C</h2>
<p>Unless suppressed evidence is "material for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> purposes, [its] suppression [does] not give rise to sufficient prejudice to overcome [a] procedural default." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#282" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 282</a></span> (internal quotation marks omitted). Our touchstone on materiality is <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419</a></span> (1995). <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Kyles</a></span></i> instructed that the materiality standard for <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims is met when "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 435</a></span>. See also <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>id.,</i> at 434-435</a></span> ("A defendant need not demonstrate that after discounting the inculpatory evidence in light of the undisclosed evidence, there would not have been enough left <span class="star-pagination">*699</span> to convict."); accord, <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#290" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 290</a></span>. In short, Banks must show a "reasonable probability of a different result." <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span> (internal quotation marks omitted) (citing <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U. S., at 678</a></span>).</p>
<p>As the State acknowledged at oral argument, Farr was "paid for a critical role in the scenario that led to the indictment." Tr. of Oral Arg. 34. Farr's declaration, presented to the federal habeas court, asserts that Farr, not Banks, initiated the proposal to obtain a gun to facilitate the commission of robberies. See App. 442-443, ¶¶ 7-8; <i>supra,</i> at 678. Had Farr not instigated, upon Deputy Sheriff Huff's request, the Dallas excursion to fetch Banks's gun, the prosecution would have had slim, if any, evidence that Banks planned to "continue" committing violent acts. App. 147.<sup>[17]</sup> Farr's admission of his instigating role, moreover, would have dampened the prosecution's zeal in urging the jury to bear in mind Banks's "planning and acquisition of a gun to commit robbery," or Banks's "planned violence." <i>Ibid.;</i> see Tr. of Oral Arg. 50.<sup>[18]</sup></p>
<p><span class="star-pagination">*700</span> Because Banks had no criminal record, Farr's testimony about Banks's propensity to commit violent acts was crucial to the prosecution. Without that testimony, the State could not have underscored, as it did three times in the penalty phase, that Banks would use the gun fetched in Dallas to "take care" of trouble arising during the robberies. App. 140, 144, 146-147; see <i>supra,</i> at 681. The stress placed by the prosecution on this part of Farr's testimony, uncorroborated by any other witness, belies the State's suggestion that "Farr's testimony was adequately corroborated." Brief for Respondent 22-25. The prosecution's penalty-phase summation, moreover, left no doubt about the importance the State attached to Farr's testimony. What Farr told the jury, the prosecution urged, was "of the utmost significance" to show "[Banks] is a danger to friends and strangers, alike." App. 146.</p>
<p>In <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>, although the Court found "cause" for the petitioner's procedural default of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, it found the requisite "prejudice" absent, <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#292" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 292-296</a></span>. Regarding "prejudice," the contrast between <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> and Banks's case is marked. The witness whose impeachment was at issue in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> gave testimony that was in the main cumulative, <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#292" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 292</a></span>, and hardly significant <span class="star-pagination">*701</span> to one of the "two predicates for capital murder: [armed] robbery," <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#294" aria-description="Citation for case: Strickler v. Greene"><i>id.,</i> at 294</a></span>. Other evidence in the record, the Court found, provided strong support for the conviction even if the witness' testimony had been excluded entirely: Unlike the Banks prosecution, in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> "considerable forensic and other physical evidence link[ed] [the defendant] to the crime" and supported the capital murder conviction. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#293" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 293</a></span>. Most tellingly, the witness' testimony in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> "did not relate to [the petitioner's] eligibility for the death sentence"; it "was not relied upon by the prosecution at all during its closing argument at the penalty phase." <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#295" aria-description="Citation for case: Strickler v. Greene"><i>Id.,</i> at 295</a></span>. In contrast, Farr's testimony was the centerpiece of Banks's prosecution's penalty-phase case.</p>
<p>Farr's trial testimony, critical at the penalty phase, was cast in large doubt by the declaration Banks ultimately obtained from Farr and introduced in the federal habeas proceeding. See <i>supra,</i> at 678, 684. In the guilt phase of Banks's trial, Farr had acknowledged his narcotics use. App. 36. In the penalty phase, Banks's counsel asked Farr if, "drawn up tight over" previous drug-related activity, he would "testify to anything anybody want[ed] to hear"; Farr denied this. <i>Id.,</i> at 110; <i>supra,</i> at 680. Farr's declaration supporting Banks's federal habeas petition, however, vividly contradicts that denial: "I assumed that if I did not help [Huff] . . . he would have me arrested for drug charges." App. 442, ¶ 6. Had jurors known of Farr's continuing interest in obtaining Deputy Sheriff Huff's favor, in addition to his receipt of funds to "set [Banks] up," <i>id.,</i> at 442, ¶ 7, they might well have distrusted Farr's testimony, and, insofar as it was uncorroborated, disregarded it.</p>
<p>The jury, moreover, did not benefit from customary, truth-promoting precautions that generally accompany the testimony of informants. This Court has long recognized the "serious questions of credibility" informers pose. <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#757" aria-description="Citation for case: On Lee v. United States">343 U. S. 747, 757</a></span> (1952). See also Trott, Words of Warning for Prosecutors Using Criminals as Witnesses, <span class="star-pagination">*702</span> 47 Hastings L. J. 1381, 1385 (1996) ("Jurors suspect [informants'] motives from the moment they hear about them in a case, and they frequently disregard their testimony altogether as highly untrustworthy and unreliable. . . ."). We have therefore allowed defendants "broad latitude to probe [informants'] credibility by cross-examination" and have counseled submission of the credibility issue to the jury "with careful instructions." <i>On Lee,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#757" aria-description="Citation for case: On Lee v. United States">343 U. S., at 757</a></span>; accord, <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#311" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 311-312</a></span> (1966). See also 1A K. O'Malley, J. Grenig, &amp; W. Lee, Federal Jury Practice and Instructions, Criminal § 15.02 (5th ed. 2000) (jury instructions from the First, Fifth, Sixth, Seventh, Eighth, Ninth, and Eleventh Circuits on special caution appropriate in assessing informant testimony).</p>
<p>The State argues that "Farr was heavily impeached [at trial]," rendering his informant status "merely cumulative." Tr. of Oral Arg. 49; see Brief for Respondent 26-28; <i>post,</i> at 709, n. 3. The record suggests otherwise. Neither witness called to impeach Farr gave evidence directly relevant to Farr's part in Banks's trial. App. 124-133; <i>id.,</i> at 129 (prosecutor noted that Kelley lacked "personal knowledge with regard to this case on trial"). The impeaching witnesses, Kelley and Owen, moreover, were themselves impeached, as the prosecution stressed on summation. See <i>id.,</i> at 141, 148; <i>supra,</i> at 680, 682. Further, the prosecution turned to its advantage remaining impeachment evidence concerning Farr's drug use. On summation, the prosecution suggested that Farr's admission "that he used dope, that he shot," demonstrated that Farr had been "open and honest with [the jury] in every way." App. 140; <i>supra,</i> at 681.</p>
<p>At least as to the penalty phase, in sum, one can hardly be confident that Banks received a fair trial, given the jury's ignorance of Farr's true role in the investigation and trial of the case. See <i>Kyles,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley">514 U. S., at 434</a></span> ("The question is not whether the defendant would more likely than not have received a different verdict with the evidence, but whether in <span class="star-pagination">*703</span> its absence he received a fair trial, understood as a trial resulting in a verdict worthy of confidence."). On the record before us, one could not plausibly deny the existence of the requisite "reasonable probability of a different result" had the suppressed information been disclosed to the defense. <i><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">Ibid.</a></span></i> (internal quotation marks omitted) (citing <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U. S., at 678</a></span>); <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#290" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 290</a></span>. Accordingly, as to the suppression of Farr's informant status and its bearing on "the reliability of the jury's verdict regarding punishment," App. to Pet. for Cert. C44; <i>supra,</i> at 686, all three elements of a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim are satisfied.</p>
<p></p>
<h2>III</h2>
<p>Both the District Court and the Court of Appeals denied Banks a certificate of appealability with regard to his Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, which rested on the prosecution's suppression of the September 1980 Cook interrogation transcript. App. 422-423; App. to Pet. for Cert. A52, A78; <i>supra,</i> at 687, 689. See also Joint Lodging Material 1-36. The District Court and the Fifth Circuit concluded that Banks had not properly pleaded this claim because he had not sought leave to amend his petition, but had stated the claim only in other submissions, <i>i. e.,</i> in his proposed findings of fact and conclusions of law, and, again, in his objections to the Magistrate Judge's report. App. 422-423, 432-433; App. to Pet. for Cert. A51-A52; <i>supra,</i> at 687, 689. Banks contended, unsuccessfully, that evidence substantiating the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim had been aired before the Magistrate Judge; therefore the claim should have been treated as if raised in the pleadings, as Federal Rule of Civil Procedure 15(b) instructs. See App. to Pet. for Cert. A51-A52; <i>supra,</i> at 687, n. 8 (setting out text of Rule 15(b)). The Fifth Circuit stated its position on this point somewhat obliquely, but appears to have viewed Rule 15(b) as inapplicable in habeas proceedings; the State now concedes, however, that the question whether Rule 15(b) extends to habeas proceedings is one "jurists of reason would <span class="star-pagination">*704</span> find . . . debatable." Compare App. to Pet. for Cert. A52 (quoting <i>Slack</i> v. <i>McDaniel,</i> <span class="citation" data-id="9433937"><a href="/opinion/118359/slack-v-mcdaniel/#484" aria-description="Citation for case: Slack v. McDaniel">529 U. S. 473, 484</a></span> (2000)), with Tr. of Oral Arg. 45-46. We conclude that a certificate of appealability should have issued.</p>
<p>We have twice before referenced Rule 15(b)'s application in federal habeas proceedings. In <i>Harris</i> v. <i>Nelson,</i> <span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/#294" aria-description="Citation for case: Harris v. Nelson">394 U. S. 286, 294, n. 5</a></span> (1969), we noted that Rule 15(b)'s use in habeas proceedings is "noncontroversial." In <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 696</a></span>, and n. 7 (1993), we similarly assumed Rule 15(b)'s application to habeas petitions. There, however, the District Court had granted a writ of habeas corpus on a claim neither pleaded, considered at "an evidentiary hearing," nor "even argu[ed]" by the parties. <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#695" aria-description="Citation for case: Withrow v. Williams"><i>Id.,</i> at 695</a></span>. Given those circumstances, we held that there had been no trial of the claim by implied consent; the respondent warden, we observed, "was manifestly prejudiced by the District Court's failure to afford her an opportunity to present evidence bearing on th[e] claim's resolution." <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams"><i>Id.,</i> at 696</a></span>. Here, in contrast, the issue of the undisclosed Cook interrogation transcript was indeed aired before the Magistrate Judge and the transcript itself was admitted into evidence without objection. See <i>supra,</i> at 685.<sup>[19]</sup></p>
<p>The Court of Appeals found no authority for equating "an evidentiary hearing . . . with a trial" for Rule 15(b) purposes. App. to Pet. for Cert. A52. We see no reason why an evidentiary hearing should not qualify so long as the respondent gave "any sort of consent" and had a full and fair "opportunity <span class="star-pagination">*705</span> to present evidence bearing on th[e] claim's resolution." <i>Withrow,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#696" aria-description="Citation for case: Withrow v. Williams">507 U. S., at 696</a></span>. Nor do we find convincing the Fifth Circuit's view that applying Rule 15(b) in habeas proceedings would undermine the State's exhaustion and procedural default defenses. <i><span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/" aria-description="Citation for case: Withrow v. Williams">Ibid.</a></span></i> Under pre-AEDPA law, there was no inconsistency between Rule 15(b) and those defenses. That is doubtless why this Court's pre-AEDPA cases assumed Rule 15(b)'s application in habeas proceedings. See <i>ibid.; </i><i>Harris,</i> <span class="citation" data-id="9423958"><a href="/opinion/107877/harris-v-nelson/#294" aria-description="Citation for case: Harris v. Nelson">394 U. S., at 294, n. 5</a></span>.<sup>[20]</sup> We note in this regard that, while AEDPA forbids a finding that exhaustion has been waived unless the State expressly waives the requirement, <span class="citation no-link">28 U. S. C. § 2254</span>(b)(3), under pre-AEDPA law, exhaustion and procedural default defenses could be waived based on the State's litigation conduct. See <i>Gray</i> v. <i>Netherland,</i> <span class="citation" data-id="9433341"><a href="/opinion/118048/gray-v-netherland/#166" aria-description="Citation for case: Gray v. Netherland">518 U. S. 152, 166</a></span> (1996) (failure to raise procedural default in federal habeas court means the defense is lost); <i>Granberry</i> v. <i>Greer,</i> <span class="citation" data-id="111862"><a href="/opinion/111862/granberry-v-greer/#135" aria-description="Citation for case: Granberry v. Greer">481 U. S. 129, 135</a></span> (1987) ("if a full trial has been held in the district court and it is evident that a miscarriage of justice has occurred, it may . . . be appropriate for the court of appeals to hold that the nonexhaustion defense has been waived").</p>
<p>To obtain a certificate of appealability, a prisoner must "demonstrat[e] that jurists of reason could disagree with the district court's resolution of his constitutional claims or that jurists could conclude the issues presented are adequate to deserve encouragement to proceed further." <i>Miller-El</i> v. <i>Cockrell,</i> <span class="citation" data-id="9434356"><a href="/opinion/122258/miller-el-v-cockrell/#327" aria-description="Citation for case: Miller-El v. Cockrell">537 U. S. 322, 327</a></span> (2003). At least as to the application of Rule 15(b), this case surely fits that description. A certificate of appealability, therefore, should have issued.</p>
<p></p>
<h2>* * *</h2>
<p>For the reasons stated, the judgment of the United States Court of Appeals for the Fifth Circuit is reversed, and the <span class="star-pagination">*706</span> case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE THOMAS, with whom JUSTICE SCALIA joins, concurring in part and dissenting in part.</p>
<p>I join Part III of the Court's opinion, and respectfully dissent from Part II, which holds that Banks' claim under <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), relating to the nondisclosure of evidence that Farr accepted money from a police officer during the course of the investigation, warrants habeas relief. Although I find it to be a very close question, I cannot conclude that the nondisclosure of Farr's informant status was prejudicial under <i>Kyles</i> v. <i>Whitley,</i> <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U. S. 419</a></span> (1995), and <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</i><sup>[1]</sup></p>
<p>To demonstrate prejudice, Banks must show that "the favorable evidence could reasonably be taken to put the whole case in such a different light as to undermine confidence in the verdict." <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#435" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 435</a></span>. The undisclosed material consisted of evidence that "Willie Huff asked [Farr] to help him find [Banks'] gun," and that Huff "gave [Farr] about $200.00 for helping him." App. 442 (Farr Declaration). Banks contends that if Farr's receipt of $200 from Huff had been revealed to the defense, there would have been a "reasonable probability," <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#434" aria-description="Citation for case: Kyles v. Whitley"><i>Kyles, supra,</i> at 434</a></span>, that the jury would not have found "beyond a reasonable doubt that there <span class="star-pagination">*707</span> [was] a probability that the defendant, Delma Banks, Jr., would commit criminal acts of violence that would constitute a continuing threat to society." App. 143 (the second special issue presented to the jury) (internal quotation marks omitted).</p>
<p>I do not believe that there is a reasonable probability that the jury would have altered its finding. The jury was presented with the facts of a horrible crime. Banks, after meeting the victim, Richard Whitehead, a 16-year-old boy who had the misfortune of owning a car that Banks wanted, decided "to kill the person for the hell of it" and take his car. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (Tex. Crim. App. 1982) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./464/904/">464 U. S. 904</a></span> (1983). Banks proceeded to shoot Whitehead three times, twice in the head and once in the upper back. Banks fired one of the shots only 18 to 24 inches away from Whitehead. The jury was thus presented with evidence showing that Banks, apparently on a whim, executed Whitehead simply to get his car.</p>
<p>The jury was also presented with evidence, in the form of Banks' own testimony, that he was willing to abet another individual in obtaining a gun, with the full knowledge that this gun would aid future armed robberies. The colloquy between a prosecuting attorney and Banks makes it clear what Banks thought he was doing:</p>
<blockquote>"Q: You were going to supply him [Farr] your gun so he could do armed robberies?</blockquote>
<blockquote>"A: No, not supply him my gun. A gun.</blockquote>
<blockquote>"Q: In other words you didn't care if it was yours or whose, but you were going to be the man who got the gun to do armed robberies. Is that correct?</blockquote>
<blockquote>"A: He was going to do it.</blockquote>
<blockquote>"Q: I understand, but you were going to supply him the means and possible death weapon in an armed robbery case. Is that correct?</blockquote>
<blockquote>"A: Yes." App. 137 (cross-examination of Banks).</blockquote>
<p><span class="star-pagination">*708</span> Accordingly, the jury was also presented with Banks' willingness to assist others in committing deadly crimes. Indeed, the prosecution referenced this very fact at one point during its closing argument in its attempt to convince the jury that Banks posed a threat to commit violent acts in the future:</p>
<blockquote>"The testimony of Vetrano Jefferson and Robert Farr is of the utmost significance. Vetrano brought before you the scar on his face, put there by Delma Banks. . . . He also corroborates or supports the testimony of Robert Farr. You don't have to believe just Robert in order to find that Delma went to Dallas to get a pistol so that <i>somebody could do some robberies.</i> Marcus Jefferson told you that, too." <i>Id.,</i> at 146 (emphasis added).<sup>[2]</sup></blockquote>
<p>The jury also heard testimony that Banks had violently pistol-whipped and threatened to kill his brother-in-law one week before the murder. Banks now claims that this evidence should be discounted because his trial counsel failed to uncover that the brother-in-law was "responsible for the fight." Brief for Petitioner 33. But even if it is appropriate to mix-and-match the prejudice analysis of the <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and the claim under <i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668</a></span> (1984) (rather than to evaluate them independently, as distinct potential constitutional violations), Banks' response was vastly disproportional to his brother-in-law's actions.</p>
<p>In sum, the jury knew that Banks had murdered a 16-year-old on a whim, had violently attacked and threatened a relative shortly before the murder, and was willing to assist another individual in committing armed robberies by providing the "means and possible death weapon" for these robberies. App. 137. Even if the jury were to discredit entirely <span class="star-pagination">*709</span> Farr's testimony that Banks was planning more robberies,<sup>[3]</sup> in all likelihood the jury still would have found "beyond a reasonable doubt" that there "[was] a probability that [Banks] would commit criminal acts of violence that would constitute a continuing threat to society." <i>Id.,</i> at 143 (internal quotation marks omitted). The randomness and wantonness of the murder would perhaps, standing alone, mandate such a finding. Accordingly, I cannot find that the nondisclosure of the evidence was prejudicial.</p>
<p>Because Banks cannot show prejudice, I do not resolve whether he has cause to excuse his failure to present his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> evidence in state court, <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#11" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1, 11-12</a></span> (1992). But there are reasons to doubt the Court's conclusion that Banks can show cause. For instance, the Court concludes that "[t]his case is congruent with <i>Strickler</i> [v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263</a></span> (1999)]," <i>ante,</i> at 693, relying in part on the State's general denial of all of Banks' factual allegations contained in his January 1992 state habeas application. But, in the relevant state postconviction proceeding in <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span>,</i> the State alleged that the petitioner had already received "`<i>everything</i> known to the government,'" a statement that federal habeas proceedings established was clearly not true. <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span> (emphasis added). In the instant case, the particular allegation raised in Banks' state habeas application and denied by the State was that "the <span class="star-pagination">*710</span> prosecution <i>knowingly</i> failed to turn over exculpatory evidence <i>as required by </i><i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span> (1963)." App. 180 (emphasis added). The State, then, could have been denying only that the prosecution <i>knowingly</i> failed to turn over the evidence (there is, incidentally, very little evidence in the record tending to show that any prosecutor had actual knowledge of Huff's payment to Farr). Or, the State could have been denying only that it had failed to turn over evidence <i>in violation of</i> Brady, <i>i. e.,</i> that any evidence the prosecution did not turn over was not material (a position advanced by the State throughout the federal habeas process), see <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#281" aria-description="Citation for case: Strickler v. Greene"><i>Strickler, supra,</i> at 281</a></span> ("[S]trictly speaking, there is never a real `<span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland"><i>Brady</i></a></span> violation' unless the nondisclosure was so serious that there is a reasonable probability that the suppressed evidence would have produced a different verdict"). Either way, <i><span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">Strickler</a></span></i> does not clearly control, and the Court's reliance on it is less than compelling.</p>
<p>Because of the Court's disposition of Banks' Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, it does not address his claim of ineffective assistance of counsel, concluding that "any relief he could obtain on that claim would be cumulative." <i>Ante,</i> at 689, n. 10. As I would affirm the Court of Appeals on the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, I briefly discuss this ineffective-assistance claim. Although I find the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim a close call, I do not find this to be so as to the ineffective-assistance claim. Banks comes nowhere close to satisfying the prejudice prong of <i>Strickland</i> v. <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Washington, supra</a></span></i><i>.</i> The conclusory and uncorroborated claims of some level of physical abuse, the allegations that a bad skin condition negatively affected his childhood development, the evidence that he was a slow learner and possessed a willingness to please others, and the claim that Banks' brother-in-law was responsible for his own pistol-whipping and receipt of a death threat, are so unpersuasive that there is no reasonable probability that the jury would have come to the opposite conclusion with respect to the future <span class="star-pagination">*711</span> dangerousness special issue, even if presented with this evidence.</p>
<p>I therefore conclude that the Court of Appeals did not err when it denied relief to Banks based on his Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim and his <i><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span></i> claim. I would reverse the Court of Appeals only insofar as it did not grant a certificate of appealability on the Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for William G. Broaddus et al. by <i>William F. Sheehan;</i> and for John J. Gibbons et al. by <i>Peter Buscemi</i> and <i>Brooke Clagett.</i>
</p>
<p><i>A. P. Carlton, Jr., Lynn R. Coleman,</i> and <i>Matthew W. S. Estes</i> filed a brief for the American Bar Association as <i>amicus curiae.</i></p>
<p>[1]  Although a police officer testified Whitehead's body was found on April 14, App. 8, the Texas Court of Criminal Appeals stated the body was discovered on April 15. <i>Banks</i> v. <i>State,</i> <span class="citation" data-id="9662670"><a href="/opinion/1637408/banks-v-state/#131" aria-description="Citation for case: Banks v. State">643 S. W. 2d 129, 131</a></span> (1982) (en banc).</p>
<p>[2]  "A person commits an offense if he commits murder . . . and . . . the person intentionally commits the murder in the course of committing or attempting to commit kidnapping, burglary, robbery, aggravated rape, or arson." <span class="citation no-link">Tex. Penal Code Ann. § 19.03</span>(a)(2) (1974).</p>
<p>[3]  As set forth in Texas law, the three special issues were:
</p>
<p>"(1) whether the conduct of the defendant that caused the death of the deceased was committed deliberately and with the reasonable expectation that the death of the deceased or another would result;</p>
<p>"(2) whether there is a probability that the defendant would commit criminal acts of violence that would constitute a continuing threat to society; and</p>
<p>"(3) if raised by the evidence, whether the conduct of the defendant in killing the deceased was unreasonable in response to the provocation, if any, by the deceased." Tex. Code Crim. Proc. Ann., Arts. 37.071(b)(1)-(3) (Vernon Supp. 1980).</p>
<p>[4]  Banks, in fact, had no criminal record at all. App. 255, ¶ 115; App. to Pet. for Cert. C23. He also "had no history of violence or alcohol abuse and seemed to possess a self-control that would suggest no particular risk of future violence." <i><span class="citation no-link">Ibid.</span></i></p>
<p>[5]  <i>Brady</i> v. <i>Maryland,</i> <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83, 87</a></span> (1963), held that "the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution."</p>
<p>[6]  Banks also alleged ineffective assistance of counsel at both the guilt and penalty phases; insufficient evidence on the second penalty-phase special issue (Banks's propensity to commit violent criminal acts); and the exclusion of minority jurors in violation of <i>Swain</i> v. <i>Alabama,</i> <span class="citation" data-id="9422975"><a href="/opinion/106997/swain-v-alabama/" aria-description="Citation for case: Swain v. Alabama">380 U. S. 202</a></span> (1965). App. to Pet. for Cert. C5-C7. Banks filed two further state postconviction motions; both were denied. Brief for Respondent 6-7, nn. 6 and 7 (citing <i>Ex parte Banks,</i> No. 13568-03 (Tex. Crim. App. 1993) <i>(per curiam),</i> and <i>Ex parte Banks,</i> No. 13568-06 (Tex. Crim. App.), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./538/990/">538 U. S. 990</a></span> (2003)).</p>
<p>[7]  We hereinafter refer to these claims as the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> and Cook <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claims respectively. See <i>supra,</i> at 682, n. 5.</p>
<p>[8]  Federal Rule of Civil Procedure 15(b) provides: "When issues not raised by the pleadings are tried by express or implied consent of the parties, they shall be treated in all respects as if they had been raised in the pleadings. Such amendment of the pleadings as may be necessary to cause them to conform to the evidence and to raise these issues may be made upon motion of any party at any time. . . ." Rule 11 of the Rules Governing Section 2254 Cases in the United States District Courts provides that the Federal Rules of Civil Procedure apply "to the extent that they are not inconsistent with [habeas] rules."</p>
<p>[9]  The Fifth Circuit noted correctly that under <i>Lindh</i> v. <i>Murphy,</i> <span class="citation" data-id="9433497"><a href="/opinion/118135/lindh-v-murphy/#336" aria-description="Citation for case: Lindh v. Murphy">521 U. S. 320, 336-337</a></span> (1997), the standards of the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), <span class="citation no-link">110 Stat. 1214</span>, do not apply to Banks's petition. See App. to Pet. for Cert. A14-A15.</p>
<p>[10]  Our disposition of the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim, and our conclusion that a writ of habeas corpus should issue with respect to the death sentence, render it unnecessary to address Banks's claim of ineffective assistance of counsel at the penalty phase; any relief he could obtain on that claim would be cumulative.</p>
<p>[11]  Banks's federal habeas petition, the Court of Appeals said, stated a claim, only under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> that material exculpatory or impeachment evidence had been suppressed, not a claim under <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), that the prosecution had failed to correct Farr's false testimony. App. to Pet. for Cert. A29-A32; App. 259-260. In its view, the Court of Appeals explained, a <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim is distinct from a <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span></i> claim, App. to Pet. for Cert. A30; thus the two did not fit under one umbrella. But cf. <i>United States</i> v. <i>Bagley,</i> <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#679" aria-description="Citation for case: United States v. Bagley">473 U. S. 667, 679-680, n. 8</a></span> (1985); <i>United States</i> v. <i>Agurs,</i> <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U.S. 97, 103-104</a></span> (1976). On brief, the parties debate the issue. Brief for Petitioner 23-25; Brief for Respondent 21-22, n. 21. Because we conclude that Banks qualifies for relief under <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>,</i> we need not decide whether a <i><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span></i> claim, to warrant adjudication, must be separately pleaded.</p>
<p>[12]  Surprisingly, the Court of Appeals' <i>per curiam</i> opinion did not refer to <i>Strickler</i> v. <i>Greene,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/" aria-description="Citation for case: Strickler v. Greene">527 U. S. 263</a></span> (1999), the controlling precedent on the issue of "cause." App. to Pet. for Cert. A15-A33.</p>
<p>[13]  We left open the question "whether any one or two of these factors would be sufficient to constitute cause." <i>Strickler,</i> <span class="citation" data-id="9433839"><a href="/opinion/118307/strickler-v-greene/#289" aria-description="Citation for case: Strickler v. Greene">527 U. S., at 289</a></span>. We need not decide that question today.</p>
<p>[14]  In addition, Banks could have expected disclosure of Farr's informant status as a matter of state law if Farr in fact acted in that capacity. Under Texas law applicable at the time of Banks's trial, the State had an obligation to disclose the identity of an informant when "the informant . . . was present at the time of the offense or arrest . . . [or] was otherwise shown to be a material witness to the transaction. . . ." <i>Kemner</i> v. <i>State,</i> <span class="citation" data-id="9654256"><a href="/opinion/1571252/kemner-v-state/#408" aria-description="Citation for case: Kemner v. State">589 S. W. 2d 403, 408</a></span> (Tex. Crim. App. 1979) (quoting <i>Carmouche</i> v. <i>State,</i> <span class="citation" data-id="9779100"><a href="/opinion/2467197/carmouche-v-state/#703" aria-description="Citation for case: Carmouche v. State">540 S. W. 2d 701, 703</a></span> (Tex. Crim. App. 1976)); cf. Tex. Rule Evid. 508(c)(1) (2003) ("No privilege exists [for the identity of an informer] . . . if the informer appears as a witness for the public entity."). Farr was present when Banks was arrested. App. 443, ¶ 10. Further, as the prosecution noted in its penalty-phase summation, Farr's testimony was not only material, but "of the utmost significance." <i>Id.,</i> at 146.</p>
<p>[15]  The Court of Appeals also stated that, because "the State did not respond" to Banks's "Farr-was-an-informant contention" in its answer to the January 1992 state habeas application, Banks should have "further investigate[d]." App. to Pet. for Cert. A22. The Fifth Circuit's error in this regard is apparent. As earlier recounted, see <i>supra,</i> at 683, the State's answer indeed did deny Banks's allegation.</p>
<p>[16]  Furthermore, rather than conceding the need for factual development of the Farr <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim in state postconviction court, the State asserted that Banks's prosecutorial misconduct claims were meritless and procedurally barred in that tribunal. App. 234, 240. Having taken that position in 1992, the State can hardly fault Banks now for failing earlier to request assistance the State certainly would have opposed.</p>
<p>[17]  It bears reiteration here that Banks had no criminal record, <i>id.,</i> at 255, ¶ 115, "no history of violence or alcohol abuse," nothing indicative of "[any] particular risk of future violence." App. to Pet. for Cert. C23.
</p>
<p>It also appears that the remaining prosecution witness in the penalty phase, Vetrano Jefferson, had omitted crucial details from his 1980 testimony. In his September 1980 testimony, Vetrano Jefferson said that Banks had struck him with a pistol in early April 1980. App. 104-105; <i>supra,</i> at 679-680. In the federal habeas proceeding, Vetrano Jefferson elaborated that he, not Banks, had initiated that incident by making "disrespectful comments" about Demetra Jefferson, Banks's girlfriend. App. 337, ¶ 4. Vetrano Jefferson recounted that he "grew angry" when Banks objected to the comments, and only then did a fight ensue, in the course of which Banks struck Vetrano Jefferson. <i>Ibid.</i></p>
<p>[18]  On brief and at oral argument, the State suggests that "the damaging evidence was Banks's willing abetment of Farr's commission of a violent crime, <i>not</i> Banks's own intent to commit such an act." Brief for Respondent 25 (emphasis in original); Tr. of Oral Arg. 50. See also <i>post,</i> at 707-708 (THOMAS, J., concurring in part and dissenting in part). In the penalty-phase summation, however, the prosecution highlighted Banks's propensity to commit violent criminal acts, see App. 140, 144, 146-147, not his facilitation of others' criminal acts, see <i>id.,</i> at 141 ("[Banks] says, `I thought I would give [the gun] to them so they could do the robberies.' I don't believe you [the jury] believe that."); <i>id.,</i> at 143 ("a man doesn't travel two hundred miles . . . to supply [another] person with a weapon"). The special issue the prosecution addressed focused on what acts Banks would commit, not what harms he might facilitate: "Do you find from the evidence beyond a reasonable doubt that there is a probability that the defendant, Delma Banks, Jr., would <i>commit</i> criminal acts of violence that would constitute a continuing threat to society?" <i>Ibid.</i> (internal quotation marks omitted and emphasis added). It is therefore unsurprising that the prosecution did not rest on Banks's facilitation of others' criminal acts in urging the jury to answer the second special issue (propensity to commit violent criminal acts) in the affirmative.</p>
<p>[19]  See Federal Evidentiary Hearing 56-73. Examining one of Banks's prosecutors, counsel for Banks twice asked if Cook had been "instructed. . . on how to testify." <i>Id.,</i> at 56. See also <i>id.,</i> at 63-64 ("Texarkana law enforcement did not instruct Mr. Cook how to testify in this case. Is that your testimony today?"). To show that Cook had been coached, Banks's counsel called attention to discrepancies between portions of the September 1980 transcript and Cook's trial testimony. <i>Id.,</i> at 65-68. Concluding his examination, Banks's counsel emphasized the prosecution's duty to disclose the September 1980 transcript once Cook, while on the stand, stated that he had not been coached. <i>Id.,</i> at 73-74; App. 59; <i>supra,</i> at 677.</p>
<p>[20]  Banks's case provides no occasion to consider Rule 15(b)'s application under the AEDPA regime.</p>
<p>[1]  I do not address the possible application of the standard enunciated in <i>Giglio</i> v. <i>United States,</i> <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), since I agree with the Court of Appeals that the issue was not properly raised below, and since addressing this issue would go beyond the question on which certiorari was granted. See Brief for Petitioner (i) (stating the question presented as whether "the Fifth Circuit commit[ted] legal error in rejecting Banks' <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></i> claim  that the prosecution suppressed material witness impeachment evidence that prejudiced him in the penalty phase of his trial  on the grounds that: . . . the suppressed evidence was immaterial to Banks' death sentence").</p>
<p>[2]  Admittedly, the prosecution used more of its closing argument trying to convince the jury to believe Farr's testimony that Banks himself was planning more robberies. See <i>ante,</i> at 699-700, n. 18. This fact is one of the reasons I find the materiality question to be a close one.</p>
<p>[3]  It is quite possible that the jury already discredited this aspect of Farr's testimony. The jury knew, from the testimony of witnesses James Kelley and Officer Gary Owen, that Farr was generally dishonest, as it heard how he had lied about getting into an altercation with a doctor over false prescriptions, and had lied about his status as an informant for an Arkansas officer in other cases. The Court suggests that the witnesses providing this information were themselves "impeached." <i>Ante,</i> at 702. At best, though, they were only slightly impeached. The prosecution merely intimated that Owen was slanting his testimony in the hopes of being hired by the defense counsel's private investigator, App. 131, and that Kelley was doing the same as he was a "friend of [Banks'] family," <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#141" aria-description="Citation for case: Brady v. Maryland"><i>id.,</i> at 141</a></span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Beckwith v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Beckwith v. United States"
type: case
citation: "425 U.S. 341 (1976)"
parallel_cite: "96 S. Ct. 1612; 48 L. Ed. 2d 1; 37 A.F.T.R.2d (RIA) 1232"
neutral_cite: 1976 U.S. LEXIS 147
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-21
docket: 74-1243
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Beckwith v. United States
  varies_by_point: false
  scope_note: "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview — even of a criminal-investigation target in a private home — requires no Miranda warnings."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109430/beckwith-v-united-states/"
  cluster_id: 109430
  opinion_id: 9426365
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Orozco v. Texas]]", "[[Mathis v. United States (1968)]]", "[[Oregon v. Mathiason]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "focus", "irs", "noncustodial-interrogation"]
holding: "Miranda warnings are required by custody, not by the fact that an investigation has 'focused' on the suspect; a noncustodial interview by IRS special agents — even of a person who is the target of a criminal tax investigation, conducted in a private home — does not trigger Miranda."
lake:
  record_id: Beckwith v. United States
  status: verified
  projected_at: 2026-07-06
---

# Beckwith v. United States

*425 U.S. 341 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two special agents of the IRS Intelligence Division — the unit assigned only when there is some indication of criminal tax fraud — met Beckwith at about 8 a.m. in a private home where he occasionally stayed. They were invited in, identified themselves, said they investigate criminal tax violations, and told him they were investigating his income-tax liability for 1966–71. The senior agent read a partial advisement (that the Fifth Amendment barred compelling his answers, that anything he said could be used against him, and that he could seek an attorney before responding) but not full [[Miranda and Custodial Interrogation|Miranda warnings]]. The roughly three-hour interview was "friendly" and "relaxed," and Beckwith was neither arrested nor detained; he later supplied records. He moved to suppress, arguing that because he was the "focus" of a criminal investigation the encounter was the functional equivalent of custody.

## Issue
Whether a noncustodial interview by IRS special agents investigating potential criminal tax violations requires [[Miranda and Custodial Interrogation|Miranda warnings]] because the taxpayer is the "focus" of the investigation.

## Rule
No — Miranda turns on custody, not investigative focus. In its decisions after *[[Miranda v. Arizona|Miranda]]* "the Court specifically stressed that it was the *custodial* nature of the interrogation which triggered the necessity for adherence to the specific requirements of its *Miranda* holding." — 425 U.S. at 346 (citing [[Orozco v. Texas]] and [[Mathis v. United States (1968)]]). ^pin-346

"'It was the compulsive aspect of custodial interrogation, and not the strength or content of the government's suspicions at the time the questioning was conducted, which led the court to impose the *Miranda* requirements with regard to custodial questioning.'" — *Id.* at 346–347 (quoting *United States v. Caiello*, 420 F.2d 471, 473 (CA2 1969)). ^pin-347

*[[Miranda v. Arizona|Miranda]]* "implicitly defined 'focus' . . . as 'questioning initiated by law enforcement officers *after* a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.'" — *Id.* at 347 (quoting *Miranda*, 384 U.S. at 444).

## Application
"Although the 'focus' of an investigation may indeed have been on Beckwith at the time of the interview in the sense that it was his tax liability which was under scrutiny, he hardly found himself in the custodial situation described by the *Miranda* Court as the basis for its holding." The friendly, noncustodial home interview lacked the inherently coercive, police-dominated elements that *[[Miranda v. Arizona|Miranda]]* addressed; that the interview may have been the "starting point" for prosecution did not convert it into custody. No full [[Miranda and Custodial Interrogation|Miranda warnings]] were required, and the statements were admissible.

## Conclusion
A noncustodial interview does not require [[Miranda and Custodial Interrogation|Miranda warnings]] merely because the suspect is the focus of a criminal investigation; the judgment of conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Beckwith* fixes **custody** (not focus) as the Miranda trigger in the [[Miranda v. Arizona]] line, distinguishing [[Mathis v. United States (1968)]] (Miranda applies to an IRS interview of a person *in custody*) and harmonizing with the noncustodial station-house interview in [[Oregon v. Mathiason]] and the in-home custody of [[Orozco v. Texas]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Beckwith v. United States*, 425 U.S. 341 (1976) — https://www.courtlistener.com/opinion/109430/beckwith-v-united-states/ — pinpoints: 346, 347.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4cd7b0e2e54610b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Beckwith v. United States"}, "payload": {"all": [{"cite": "425 U.S. 341", "page": "341", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "425"}, {"cite": "96 S. Ct. 1612", "page": "1612", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "48 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "48"}, {"cite": "1976 U.S. LEXIS 147", "page": "147", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}, {"cite": "37 A.F.T.R.2d (RIA) 1232", "page": "1232", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "37"}], "display": "425 U.S. 341", "official": {"cite": "425 U.S. 341", "page": "341", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "425"}, "official_selection_present": true, "record_id": "Beckwith v. United States"}}
{"assertion_id": "479252e358afea98", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-347", "record_id": "Beckwith v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-347", "pinpoint_status": "slip-only", "quote": "'It was the compulsive aspect of custodial interrogation, and not the strength or content of the government's suspicions at the time the questioning was conducted, which led the court to impose the *Miranda* requirements with regard to custodial questioning.'", "quote_fidelity": "mismatch", "record_id": "Beckwith v. United States", "star_marker": null}}
{"assertion_id": "92ab48c4b51d4192", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-346", "record_id": "Beckwith v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-346", "pinpoint_status": "slip-only", "quote": "of the investigation. ## Rule No — Miranda turns on custody, not investigative focus. In its decisions after *Miranda*", "quote_fidelity": "mismatch", "record_id": "Beckwith v. United States", "star_marker": null}}
{"assertion_id": "b358a23d5fd309bb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Beckwith v. United States"}, "payload": {"as_of_content": "1976-04-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Beckwith v. United States", "scope_note": "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview — even of a criminal-investigation target in a private home — requires no Miranda warnings.", "varies_by_point": false}}
```

### lake record — Beckwith v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Beckwith v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Beckwith v. United States",
    "case_name_short": "Beckwith",
    "case_name_full": "Beckwith v. United States",
    "input_case_name": "Beckwith v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-21",
    "year": 1976,
    "docket": "74-1243",
    "cluster_id": 109430,
    "lead_opinion_id": 9426365,
    "sibling_ids": [
      109430,
      9426365,
      9426366,
      9426367
    ],
    "absolute_url": "/opinion/109430/beckwith-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 341",
      "volume": "425",
      "reporter": "U.S.",
      "page": "341",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1612",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 1",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1232",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 147",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 341",
        "volume": "425",
        "reporter": "U.S.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1612",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1612",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 1",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 147",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "147",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 A.F.T.R.2d (RIA) 1232",
        "volume": "37",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1232",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 341",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 341",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-346",
      "page": null,
      "quote": "of the investigation. ## Rule No \u2014 Miranda turns on custody, not investigative focus. In its decisions after *Miranda*",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-347",
      "page": null,
      "quote": "'It was the compulsive aspect of custodial interrogation, and not the strength or content of the government's suspicions at the time the questioning was conducted, which led the court to impose the *Miranda* requirements with regard to custodial questioning.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Beckwith v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; Miranda is triggered by custody, not by the investigation's 'focus' on the suspect. A noncustodial interview \u2014 even of a criminal-investigation target in a private home \u2014 requires no Miranda warnings.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. John Noehl and Analise Noehl",
          "cluster_id": 10618700,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
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
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lawrence Samuel Jr. v. State",
          "cluster_id": 3130658,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Charles",
          "cluster_id": 1563356,
          "cite": [
            "16 So. 3d 1166",
            "2009 La. LEXIS 2354",
            "2009 WL 2838411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
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
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Edward Uzenski",
          "cluster_id": 792949,
          "cite": [
            "434 F.3d 690",
            "69 Fed. R. Serv. 274",
            "2006 U.S. App. LEXIS 827",
            "2006 WL 73632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkerson, Ray Mitchell",
          "cluster_id": 2936737,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "White v. State",
          "cluster_id": 1777867,
          "cite": [
            "931 S.W.2d 736",
            "1996 Tex. App. LEXIS 4445",
            "1996 WL 580988"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane1_negative"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
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
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Beheler",
          "cluster_id": 111023,
          "cite": [
            "77 L. Ed. 2d 1275",
            "103 S. Ct. 3517",
            "463 U.S. 1121",
            "1983 U.S. LEXIS 114",
            "51 U.S.L.W. 3934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fare v. Michael C.",
          "cluster_id": 110117,
          "cite": [
            "61 L. Ed. 2d 197",
            "99 S. Ct. 2560",
            "442 U.S. 707",
            "1979 U.S. LEXIS 133"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1653372,
          "cite": [
            "836 S.W.2d 530",
            "1992 Tenn. LEXIS 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. State",
          "cluster_id": 1749178,
          "cite": [
            "306 S.W.3d 274",
            "2009 Tex. Crim. App. LEXIS 1441",
            "2009 WL 3365652"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Commonwealth",
          "cluster_id": 1227505,
          "cite": [
            "307 S.E.2d 864",
            "226 Va. 31",
            "1983 Va. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Matheny",
          "cluster_id": 2637091,
          "cite": [
            "46 P.3d 453",
            "2002 WL 1009210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Washington",
          "cluster_id": 109659,
          "cite": [
            "52 L. Ed. 2d 238",
            "97 S. Ct. 1814",
            "431 U.S. 181",
            "1977 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCambridge v. State",
          "cluster_id": 2437346,
          "cite": [
            "712 S.W.2d 499",
            "1986 Tex. Crim. App. LEXIS 1275"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marcus T. Baumann v. United States",
          "cluster_id": 410430,
          "cite": [
            "692 F.2d 565",
            "1982 U.S. App. LEXIS 24530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Chalan, Jr.",
          "cluster_id": 483901,
          "cite": [
            "812 F.2d 1302",
            "1987 U.S. App. LEXIS 2758",
            "22 Fed. R. Serv. 1200"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shiflet v. State",
          "cluster_id": 1745641,
          "cite": [
            "732 S.W.2d 622",
            "1985 Tex. Crim. App. LEXIS 1718"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John E. Kenny, Trenton P. Oelberg, and William L. Parker, Defendants",
          "cluster_id": 389261,
          "cite": [
            "645 F.2d 1323"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Joseph, Petitioner-Appellant/cross-Appellee v. Ralph Coyle, Warden, Respondent-Appellee/cross-Appellant",
          "cluster_id": 796039,
          "cite": [
            "469 F.3d 441",
            "2006 U.S. App. LEXIS 27697",
            "2006 WL 3250935"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1655134,
          "cite": [
            "740 S.W.2d 779",
            "1987 Tex. Crim. App. LEXIS 671",
            "1987 WL 1000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meek v. State",
          "cluster_id": 1577494,
          "cite": [
            "790 S.W.2d 618",
            "1990 Tex. Crim. App. LEXIS 84",
            "1990 WL 67493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beckwith v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MTQ1NzkyMDAwMDAmcz0xNTMwMTI4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODImcz0xOTAwMzU2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 1,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109430 OR 9426365 OR 9426366 OR 9426367)",
    "indexed_citing_opinions": 706,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109430,
        "count": 649,
        "count_source": "search"
      },
      {
        "opinion_id": 9426365,
        "count": 77,
        "count_source": "search"
      },
      {
        "opinion_id": 9426366,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426367,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1005,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/beckwith-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjUzNTI5ODgmcz00Mzc4NTI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109430+OR+9426365+OR+9426366+OR+9426367%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109430,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 281129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 281735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 285855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 288179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 289616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 292827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 294195,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 294580,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 299047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 310330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 322550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109430,
        "cited_id": 325001,
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
    "date_created": "2026-07-04T19:27:30Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:33:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:27:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Beckwith v. United States

```
<opinion type="majority">
<author id="b411-12">Mr. Chief Justice Burger</author>
<p id="AtZ">delivered the opinion of the Court.</p>
<p id="b411-13">The important issue presented in this case is whether a special agent of the Internal Revenue Service, investigating potential criminal income tax violations, must, in <page-number citation-index="1" label="342">*342</page-number>an interview with a taxpayer, not in custody, give the warnings called for by this Court’s decision in <em>Miranda </em>v. Arizona, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). We granted certiorari to resolve the conflict between the holding of the Court of Appeals in this case, which is consistent with the weight of authority on the issue,<footnotemark>1</footnotemark> and the position adopted by the United States Court of Appeals for the Seventh Circuit.<footnotemark>2</footnotemark></p>
<p id="b412-5">The District Court conducted a thorough inquiry into the facts surrounding the interview of petitioner before ruling on his motion to suppress the statements at issue. After a considerable amount of investigation, two special agents of the Intelligence Division of the Internal Revenue Service met with petitioner in a private home where petitioner occasionally stayed. The senior agent testified that they went to see petitioner at this private residence at 8 a. m. in order to spare petitioner the possible embarrassment of being interviewed at his place of employment which opened at 10 a. m. Upon their arrival, they identified themselves to the person answering the door and asked to speak to petitioner. The agents were invited into the house and, when petitioner entered the room where they were waiting, they introduced them<page-number citation-index="1" label="343">*343</page-number>selves and, according to the testimony of the senior agent, Beckwith then excused himself for a period in excess of five minutes, to finish dressing.<footnotemark>3</footnotemark> Petitioner then sat down at the dining room table with the agents; they presented their credentials and stated they were attached to the Intelligence Division and that one of their functions was to investigate the possibility of criminal tax fraud. They then informed petitioner that they were assigned to investigate his federal income tax liability for the years 1966 through 1971. The senior agent then read to petitioner from a printed card the following:</p>
<blockquote id="b413-5">“As a special agent, one of my functions is to investigate the possibility of criminal violations of the Internal Revenue laws, and related offenses.</blockquote>
<blockquote id="b413-6">“Under the Fifth Amendment to the Constitution of the United States, I cannot compel you to answer any questions or to submit any information if such answers or information might tend to incriminate you in any way. I also advise you that anything which you say and any information which you submit may be used against you in any criminal proceeding which may be undertaken. I advise you further that you may, if you wish, seek the assistance of an attorney before responding.” App. 65-66.</blockquote>
<p id="b413-7">Petitioner acknowledged that he understood his rights. The agents then interviewed him until about 11 o’clock. The agents described the conversation as “friendly” and “relaxed.” The petitioner noted that the agents did not “press” him on any question he could not or chose not to answer.</p>
<p id="b413-8">Prior to the conclusion of the interview, the senior agent requested that petitioner permit the agents to <page-number citation-index="1" label="344">*344</page-number>inspect certain records. Petitioner indicated that they were at his place of employment. The agents asked if they could meet him there later. Having traveled separately from petitioner, the agents met petitioner approximately 45 minutes later and the senior agent advised the petitioner that he was not required to furnish any books or records; petitioner, however, supplied the books to the agents.</p>
<p id="b414-5">Prior to trial, petitioner moved to suppress all statements he made to the agents or evidence derived from those statements on the ground that petitioner had not been given the warnings mandated by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The District Court ruled that he was entitled to such warnings “when the court finds as a fact that there were custodial circumstances.” The District Judge went on to find that “on this record . . . there is no evidence whatsoever of any such situation.” The Court of Appeals affirmed the judgment of conviction. 166 U. S. App. D. C. 361, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d 741</a></span> (1975). It noted that the reasoning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was based “in crucial part” on whether the suspect “has been taken into custody or otherwise deprived of his freedom in any significant way,” <em>id., </em>at 362, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#742" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 742</a></span>, citing <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 477</a></span>; and agreed with the District Court that “Beckwith was neither arrested nor detained against his will.” 166 U. S. App. D. C., at 362, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#742" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 742</a></span>. We agree with the analysis of the Court of Appeals<footnotemark>4</footnotemark> and, therefore, affirm its judgment.</p>
<p id="b414-6">Petitioner contends that the “entire starting point” for the criminal prosecution brought against him was secured from his own statements and disclosures during the interview with the Internal Revenue agents from the <page-number citation-index="1" label="345">*345</page-number>Intelligence Division. He correctly points out that cases are assigned to the Intelligence Division only when there is some indication of criminal fraud and that, especially since tax offenses rarely result in pretrial custody, the taxpayer is clearly the “focus” of a criminal investigation when a matter is assigned to the Intelligence Division. Given the complexity of the tax structure and the confusion on the part of taxpayers between the civil and criminal function of the Internal Revenue Service, such a confrontation, argues petitioner, places the taxpayer under “psychological restraints” which are the functional, and, therefore, the legal, equivalent of custody. In short we agree with Chief Judge Bazelon, speaking for a unanimous Court of Appeals, that</p>
<blockquote id="b415-5">“[t]he major thrust of Beckwith’s argument is that the principle of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em>Mathis </em>[<footnotemark>5</footnotemark>] should be extended to cover interrogation in non-custodial circumstances after a police investigation has focused on the suspect.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></em></blockquote>
<p id="b415-6">With the Court of Appeals, we “are not impressed with this argument in the abstract nor as applied to the particular facts of Beckwith’s interrogation.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>It goes far beyond the reasons for that holding and such an extension of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements would cut this Court’s holding in that case completely loose from its own explicitly stated rationale. The narrow issue before the Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was presented very precisely in the opening paragraph of that opinion — “the admissibility of statements obtained from an individual who is subjected to <em>custodial </em>police interrogation.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 439</a></span>.<footnotemark>6</footnotemark> (Emphasis supplied.) The Court concluded <page-number citation-index="1" label="346">*346</page-number>that compulsion is “inherent in custodial surroundings,” <footnotemark>7</footnotemark> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 458</a></span>, and, consequently, that special safeguards were required in the case of “incommunicado interrogation of individuals in a police-dominated atmosphere, resulting in self-incriminating statements without full warnings of constitutional rights.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 445</a></span>. In subsequent decisions, the Court specifically stressed that it was the <em>custodial </em>nature of the interrogation which triggered the necessity for adherence to the specific requirements of its <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding. <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324</a></span> (1969); <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968). See generally <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#247" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 247</a></span> (1973).</p>
<p id="b416-5">Petitioner’s argument that he was placed in the functional, and, therefore, legal, equivalent of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>situation asks us now to ignore completely that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was grounded squarely in the Court’s explicit and detailed assessment of the peculiar “nature and setting of . . . in-custody interrogation,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445</a></span>. That Courts of Appeals have so read <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is suggested by Chief Judge Lumbard in <em>United States </em>v. <em>Caiello, </em><span class="citation" data-id="9455181"><a href="/opinion/287949/united-states-v-richard-v-caiello/#473" aria-description="Citation for case: United States v. Richard v. Caiello">420 F. 2d 471, 473</a></span> (CA2 1969):</p>
<blockquote id="b416-6">“ Tt was the compulsive aspect of custodial interrogation, and not the strength or content of the government’s suspicions at the time the questioning was conducted, which led the court to impose the <page-number citation-index="1" label="347">*347</page-number><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements with regard to custodial questioning.' ”</blockquote>
<p id="b417-6"><em>Mathis </em>v. <em>United States, supra, </em>directly supports this conclusion in holding that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements are applicable to interviews with Internal Revenue agents concerning tax liability, <em>when the subject is in custody; </em>the Court thus squarely grounded its holding on the custodial aspects of the situation, not the subject matter of the interview.<footnotemark>8</footnotemark></p>
<p id="b417-7">An interview with Government agents in a situation such as the one shown by this record simply does not present the elements which the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court found so inherently coercive as to require its holding. Although the “focus” of an investigation may indeed have been on Beckwith at the time of the interview in the sense that it was his tax liability which was under scrutiny, he hardly found himself in the custodial situation described by the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court as the basis for its holding. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>implicitly defined “focus,” for its purposes, as “questioning initiated by law enforcement officers <em>after </em>a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. (Emphasis supplied.) It may well be true, as petitioner contends, that the “starting point” for the criminal prosecution was the information obtained from petitioner and the records exhibited by him. But this amounts to no more than saying that a tax return signed by a taxpayer can be the “starting point” for a prosecution.</p>
<p id="b417-8">We recognize, of course, that noncustodial interrogation might possibly in some situations, by virtue of some <page-number citation-index="1" label="348">*348</page-number>special circumstances, ,be characterized as one where “the behavior of . . . law enforcement officials was such as to overbear petitioner's will to resist and bring about confessions not freely self-determined-” <em>Rogers </em>v. <em>Richmond, </em><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#544" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 544</a></span> (1961). When such a claim is raised, it is the duty of an appellate court, including this Court, “to examine the entire record and make an independent determination of the ultimate issue of- voluntariness." <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741-742</a></span> (1966). Proof that some kind of warnings were given or that none were given would be relevant evidence only on the issue of whether the questioning was in fact coercive. <em>Frazier </em>v. <em>Cupp, </em><span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969); <em>Davis </em>v. <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#740" aria-description="Citation for case: Davis v. North Carolina"><em>North Carolina, supra, </em>at 740-741</a></span>. In the present case, however, as Chief Judge Bazelon noted, “[t]he entire interview was free of coercion,” 166 U. S. App. D. C., at 363, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#743" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 F. 2d, at 743</a></span> (footnote omitted).</p>
<p id="b418-6">Accordingly, the judgment of the Court of Appeals is</p>
<p id="b418-7">
<em>Affirmed.</em>
</p>
<p id="b418-8">Me. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b412-6"> See, <em>e. g., Taglianetti </em>v. <em>United States, </em><span class="citation" data-id="281129"><a href="/opinion/281129/louis-j-taglianetti-v-united-states/#566" aria-description="Citation for case: Louis J. Taglianetti v. United States">398 F. 2d 558, 566</a></span> (CA1 1968), aff'd on another ground, <span class="citation" data-id="107880"><a href="/opinion/107880/taglianetti-v-united-states/" aria-description="Citation for case: Taglianetti v. United States">394 U. S. 316</a></span> (1969); <em>United States </em>v. <em>Mackiewicz, </em><span class="citation" data-id="9453948"><a href="/opinion/281735/united-states-v-walter-p-mackiewicz-and-florence-b-mackiewicz/#221" aria-description="Citation for case: United States v. Walter P. MacKiewicz and Florence B....">401 F. 2d 219, 221-222</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./393/923/">393 U. S. 923</a></span> (1968); <em>United States </em>v. <em>Jaskiewicz, </em><span class="citation" data-id="292827"><a href="/opinion/292827/united-states-v-frank-a-jaskiewicz/#417" aria-description="Citation for case: United States v. Frank A. Jaskiewicz">433 F. 2d 415, 417-420</a></span> (CA3 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/1021/">400 U. S. 1021</a></span> (1971); <em>United States </em>v. <em>Browney, </em><span class="citation" data-id="9455236"><a href="/opinion/288179/united-states-v-hilton-g-browney/#51" aria-description="Citation for case: United States v. Hilton G. Browney">421 F. 2d 48, 51-52</a></span> (CA4 1970); <em>United States </em>v. <em>Prudden, </em><span class="citation" data-id="9455504"><a href="/opinion/289616/united-states-v-horton-r-prudden/#1027" aria-description="Citation for case: United States v. Horton R. Prudden">424 F. 2d 1021, 1027-1031</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/831/">400 U. S. 831</a></span> (1970); <em>United States </em>v. <em>Stribling, </em><span class="citation" data-id="9456470"><a href="/opinion/294580/united-states-v-george-y-stribling/#771" aria-description="Citation for case: United States v. George Y. Stribling">437 F. 2d 765, 771</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./402/973/">402 U. S. 973</a></span> (1971); <em>United States v. MacLeod, 436 F. </em>2d 947, 950 (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./402/907/">402 U. S. 907</a></span> (1971); <em>United States </em>v. <em>Robson, </em><span class="citation" data-id="310330"><a href="/opinion/310330/united-states-v-walter-c-robson/#16" aria-description="Citation for case: United States v. Walter C. Robson">477 F. 2d 13, 16</a></span> (CA9 1973); <em>Hensley </em>v. <em>United </em>States, <span class="citation" data-id="283275"><a href="/opinion/283275/eugene-v-hensley-v-united-states/#484" aria-description="Citation for case: Eugene v. Hensley v. United States">406 F. 2d 481, 484</a></span> (CA10 1968); but cf. <em>United States </em>v. <em>Lockyer, </em><span class="citation" data-id="299047"><a href="/opinion/299047/united-states-v-ralph-lockyer/#422" aria-description="Citation for case: United States v. Ralph Lockyer">448 F. 2d 417, 422</a></span> (CA10 1971).</p>
</footnote>
<footnote label="2">
<p id="b412-7"> <em>United States </em>v. <em>Dickerson, </em><span class="citation" data-id="9454740"><a href="/opinion/285855/united-states-v-albert-dickerson/" aria-description="Citation for case: United States v. Albert Dickerson">413 F. 2d 1111</a></span> (1969).</p>
</footnote>
<footnote label="3">
<p id="b413-9"> Petitioner claimed at the suppression hearing that he was fully-dressed when he first met the agents. The District Court did not explicitly resolve this conflict in testimony.</p>
</footnote>
<footnote label="4">
<p id="b414-7"> On petition for writ of certiorari to this Court, Beckwith does not challenge the further holding of the Court of Appeals that, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>question aside, the “entire interview was free of coercion,” 166 U. S. App. D. C., at 363, <span class="citation" data-id="325001"><a href="/opinion/325001/united-states-v-alvin-a-beckwith-jr-aka-alvin-a-beckwith/#743" aria-description="Citation for case: United States v. Alvin A. Beckwith, Jr., A/K/A Alvin A....">510 <em>F. </em>2d, at 743</a></span> (footnote omitted).</p>
</footnote>
<footnote label="5">
<p id="b415-7"><em> Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968).</p>
</footnote>
<footnote label="6">
<p id="b415-8"> The Court also stated: “The constitutional issue we decide . . . is the admissibility of statements obtained from a defendant questioned while in custody or otherwise deprived of his freedom of action <page-number citation-index="1" label="346">*346</page-number>in any significant way.” 384 U. S., at 445. The Court specifically defined “custodial interrogation” to mean “questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his <em>freedom </em>of action in any significant way.” <em>Id., </em>at 444.</p>
</footnote>
<footnote label="7">
<p id="b416-12"> The Court gave great weight to contemporaneous police manuals and concluded that custodial interrogation was “psychologically . . . oriented,” <em>id., </em>at 448, and that the principal psychological factor contributing to successful interrogation was isolating the suspect in unfamiliar surroundings “for no purpose other than to subjugate the individual to the will of his examiner.” <em>Id., </em>at 457.</p>
</footnote>
<footnote label="8">
<p id="b417-9"> Four Members of the Court joined Mr. Justice Black; the dissenters regarded <em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">Mathis</a></span> </em>as an extension of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>largely because the custody and the interrogation were in no way related and because a prisoner interrogated in prison was not in unfamiliar surroundings.</p>
</footnote>
</opinion>
```

---
