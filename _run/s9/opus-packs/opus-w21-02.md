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

## GROUP: _overhaul2/lake/cases/Vernonia School District 47J v. Acton.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Vernonia School District 47J v. Acton"
type: case
citation: "515 U.S. 646 (1995)"
parallel_cite: "115 S. Ct. 2386; 132 L. Ed. 2d 564"
neutral_cite: 1995 U.S. LEXIS 4275
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-06-26
docket: 94-590
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Vernonia School District 47J v. Acton
  varies_by_point: false
  scope_note: "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/"
  cluster_id: 117964
  opinion_id: 9433198
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[Board of Education v. Earls]]", "[[New Jersey v. T.L.O.]]", "[[Skinner v. Railway Labor Executives' Ass'n]]", "[[National Treasury Employees Union v. Von Raab]]"]
aliases: ["Vernonia v. Acton", "Acton"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "schools", "student-athletes"]
holding: "Suspicionless random drug testing of public-school student athletes is reasonable under the special-needs doctrine, given athletes'…"
lake:
  record_id: Vernonia School District 47J v. Acton
  status: verified
  projected_at: 2026-07-09
---

# Vernonia School District 47J v. Acton

*515 U.S. 646 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Faced with a sharp rise in student drug use led by the school's athletes, the Vernonia, Oregon school district adopted a Student Athlete Drug Policy conditioning participation in interscholastic sports on consent to suspicionless urinalysis — a test at the start of each season plus random weekly testing during the season. Seventh grader James Acton was denied a spot on the football team after he and his parents refused to sign the consent forms. The Actons sued, claiming the policy violated the Fourth Amendment.

## Issue
Whether a public school district's policy of random, suspicionless urinalysis drug testing of student athletes is a reasonable search under the Fourth Amendment.

## Rule
State-compelled urinalysis is a search, and "the ultimate measure of the constitutionality of a governmental search is 'reasonableness'" — judged, where there was no clear founding-era practice, by "balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests." — 515 U.S. at 652–653. ^pin-652

A school search may proceed without individualized suspicion under the "special needs" doctrine, and the relevant privacy expectation is reduced in the school setting and reduced further for athletes: "Legitimate privacy expectations are even less with regard to student athletes." — [*Id.* at 657](https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/#:~:text=%E2%80%9Cwhen-,special%20needs). ^pin-657

Weighing "the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met by the search," the Court held: "we conclude Vernonia's Policy is reasonable and hence constitutional." — *Id.* at 664–665. ^pin-665

## Application
On these facts the three factors favored the District. Student athletes have a decreased expectation of privacy: schoolchildren are already subject to physical exams and vaccinations, athletes dress and shower communally, and by "going out for the team" they voluntarily accept added regulation. The character of the intrusion was negligible — male students produced samples at a urinal observed only from behind, female students in an enclosed stall with a monitor listening for tampering, and results were screened only for drugs and disclosed to a limited set of school personnel, not law enforcement. And the governmental concern was immediate and important: deterring drug use among the very students leading a drug epidemic, with athletes at heightened physical risk. Balancing those factors, the random-testing policy was reasonable.

## Conclusion
The Policy was a reasonable search; the judgment of the Ninth Circuit invalidating it was reversed. The Court cautioned that its holding did not mean suspicionless testing would "readily pass constitutional muster in other contexts."

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Vernonia* was **extended** by [[Board of Education v. Earls]] (2002), which upheld suspicionless testing of students in all competitive extracurricular activities, not just athletics. It builds on the school-search framework of [[New Jersey v. T.L.O.]] and the drug-testing balancing of [[Skinner v. Railway Labor Executives' Ass'n]] and [[National Treasury Employees Union v. Von Raab]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Vernonia School District 47J v. Acton*, 515 U.S. 646 (1995) — https://www.courtlistener.com/opinion/117964/vernonia-school-district-47j-v-acton/ — pinpoints: 652–653, 657, 664–665.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "458ede4658705d29", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Vernonia School District 47J v. Acton"}, "payload": {"all": [{"cite": "515 U.S. 646", "page": "646", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "515"}, {"cite": "115 S. Ct. 2386", "page": "2386", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "115"}, {"cite": "132 L. Ed. 2d 564", "page": "564", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "1995 U.S. LEXIS 4275", "page": "4275", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1995"}], "display": "515 U.S. 646", "official": {"cite": "515 U.S. 646", "page": "646", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "515"}, "official_selection_present": true, "record_id": "Vernonia School District 47J v. Acton"}}
{"assertion_id": "2d57045aea3b13da", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-657", "record_id": "Vernonia School District 47J v. Acton"}, "payload": {"fragment": "#:~:text=%E2%80%9Cwhen-,special%20needs", "page": null, "pin_id": "pin-657", "pinpoint_status": "star-verified", "quote": "special needs", "quote_fidelity": "matched", "record_id": "Vernonia School District 47J v. Acton", "star_marker": "653"}}
{"assertion_id": "814e345a347d0512", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-665", "record_id": "Vernonia School District 47J v. Acton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-665", "pinpoint_status": "slip-only", "quote": "the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met by the search,", "quote_fidelity": "mismatch", "record_id": "Vernonia School District 47J v. Acton", "star_marker": null}}
{"assertion_id": "89c4804b23ef4b00", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-652", "record_id": "Vernonia School District 47J v. Acton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-652", "pinpoint_status": "slip-only", "quote": "--- # Vernonia School District 47J v. Acton *515 U.S. 646 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Faced with a sharp rise in student drug use led by the school's athletes, the Vernonia, Oregon school district adopted a Student Athlete Drug Policy conditioning participation in interscholastic sports on consent to suspicionless urinalysis — a test at the start of each season plus random weekly testing during the season. Seventh grader James Acton was denied a spot on the football team after he and his parents refused to sign the consent forms. The Actons sued, claiming the policy violated the Fourth Amendment. ## Issue Whether a public school district's policy of random, suspicionless urinalysis drug testing of student athletes is a reasonable search under the Fourth Amendment. ## Rule State-compelled urinalysis is a search, and", "quote_fidelity": "mismatch", "record_id": "Vernonia School District 47J v. Acton", "star_marker": null}}
{"assertion_id": "8877da5ead42ddbe", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Vernonia School District 47J v. Acton"}, "payload": {"as_of_content": "1995-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Vernonia School District 47J v. Acton", "scope_note": "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law.", "varies_by_point": false}}
```

### lake record — Vernonia School District 47J v. Acton

```json
{
  "schema_version": "s2.v1",
  "record_id": "Vernonia School District 47J v. Acton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Vernonia School District 47J v. Acton",
    "case_name_short": "Acton",
    "case_name_full": "VERNONIA SCHOOL DISTRICT 47J v. ACTON Et Ux., Guardians Ad Litem for ACTON",
    "input_case_name": "Vernonia School District 47J v. Acton",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-06-26",
    "year": 1995,
    "docket": "94-590",
    "cluster_id": 117964,
    "lead_opinion_id": 9433198,
    "sibling_ids": [
      117964,
      9433198,
      9433199,
      9433200
    ],
    "absolute_url": "/opinion/117964/vernonia-school-district-47j-v-acton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "515 U.S. 646",
      "volume": "515",
      "reporter": "U.S.",
      "page": "646",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "115 S. Ct. 2386",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "2386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 L. Ed. 2d 564",
        "volume": "132",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 4275",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "4275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "515 U.S. 646",
        "volume": "515",
        "reporter": "U.S.",
        "page": "646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 S. Ct. 2386",
        "volume": "115",
        "reporter": "S. Ct.",
        "page": "2386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 L. Ed. 2d 564",
        "volume": "132",
        "reporter": "L. Ed. 2d",
        "page": "564",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 4275",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "4275",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "515 U.S. 646",
    "official_selection": {
      "court_class": "scotus",
      "selected": "515 U.S. 646",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-652",
      "page": null,
      "quote": "--- # Vernonia School District 47J v. Acton *515 U.S. 646 (1995)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Faced with a sharp rise in student drug use led by the school's athletes, the Vernonia, Oregon school district adopted a Student Athlete Drug Policy conditioning participation in interscholastic sports on consent to suspicionless urinalysis \u2014 a test at the start of each season plus random weekly testing during the season. Seventh grader James Acton was denied a spot on the football team after he and his parents refused to sign the consent forms. The Actons sued, claiming the policy violated the Fourth Amendment. ## Issue Whether a public school district's policy of random, suspicionless urinalysis drug testing of student athletes is a reasonable search under the Fourth Amendment. ## Rule State-compelled urinalysis is a search, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-657",
      "page": null,
      "quote": "special needs",
      "star_marker": "653",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 12646,
      "fragment": "#:~:text=%E2%80%9Cwhen-,special%20needs",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-665",
      "page": null,
      "quote": "the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met by the search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Vernonia School District 47J v. Acton",
    "varies_by_point": false,
    "scope_note": "Extended to non-athlete competitive extracurriculars by Board of Education v. Earls (2002); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Moore v. Portland Public Schools",
          "cluster_id": 10143838,
          "cite": [
            "328 Or. App. 391"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 10018712,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 5293509,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Ryan Mark Thompson",
          "cluster_id": 4311783,
          "cite": [
            "886 N.W.2d 224",
            "2016 Minn. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sarah Beth Keller",
          "cluster_id": 4247956,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Blue",
          "cluster_id": 3185413,
          "cite": [
            "783 S.E.2d 524",
            "246 N.C. App. 259",
            "2016 N.C. App. LEXIS 293"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Morris",
          "cluster_id": 3185407,
          "cite": [
            "783 S.E.2d 528",
            "246 N.C. App. 349",
            "2016 N.C. App. LEXIS 291"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane1_negative"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis Ex Rel. LaShonda D. v. Monroe County Board of Education",
          "cluster_id": 118290,
          "cite": [
            "143 L. Ed. 2d 839",
            "119 S. Ct. 1661",
            "526 U.S. 629",
            "1999 U.S. LEXIS 3452",
            "12 Fla. L. Weekly Fed. S 280",
            "67 U.S.L.W. 4329",
            "1999 Colo. J. C.A.R. 2948",
            "99 Cal. Daily Op. Serv. 3861",
            "99 Daily Journal DAR 4931"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hedges v. Musco",
          "cluster_id": 767706,
          "cite": [
            "204 F.3d 109",
            "2000 U.S. App. LEXIS 2671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doe Ex Rel. Magee v. Covington County School District",
          "cluster_id": 626050,
          "cite": [
            "675 F.3d 849",
            "2012 U.S. App. LEXIS 6080",
            "2012 WL 976349"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tenenbaum v. Williams",
          "cluster_id": 7079141,
          "cite": [
            "193 F.3d 581",
            "1999 WL 822538"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Frederick",
          "cluster_id": 145707,
          "cite": [
            "168 L. Ed. 2d 290",
            "127 S. Ct. 2618",
            "551 U.S. 393",
            "2007 U.S. LEXIS 8514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Snider",
          "cluster_id": 1746280,
          "cite": [
            "608 N.W.2d 502",
            "239 Mich. App. 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
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
        "journal_ref": "Vernonia School District 47J v. Acton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkyOTQwODAwMDAwJnM9MjY1NDAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjYmcz03MDY5NTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 1,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117964 OR 9433198 OR 9433199 OR 9433200)",
    "indexed_citing_opinions": 895,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117964,
        "count": 778,
        "count_source": "search"
      },
      {
        "opinion_id": 9433198,
        "count": 129,
        "count_source": "search"
      },
      {
        "opinion_id": 9433199,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9433200,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1472,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/vernonia-school-district-47j-v-acton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MTA0Mzkmcz05NTA1OTgzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28117964+OR+9433198+OR+9433199+OR+9433200%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117964,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111835,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 111979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 319945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 669794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117964,
        "cited_id": 1559138,
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
    "date_created": "2026-07-06T03:50:22Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:53:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:50:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Vernonia School District 47J v. Acton

```
<opinion type="majority">
<author id="b694-9">Justice Scalia</author>
<p id="AIZ">delivered the opinion of the Court.</p>
<p id="b694-10">The Student Athlete Drug Policy adopted by School District 47J in the town of Vernonia, Oregon, authorizes random urinalysis drug testing of students who participate in the District’s school athletics programs. We granted certiorari to decide whether this violates the Fourth and Fourteenth Amendments to the United States Constitution.</p>
<p id="AR7">I</p>
<p id="b694-3">A</p>
<p id="b694-4">Petitioner Vernonia School District 47J (District) operates one high school and three grade schools in the logging community of Vernonia, Oregon. As elsewhere in small-town America, school sports play a prominent role in the town’s life, and student athletes are admired in their schools and in the community.</p>
<p id="b694-5">Drugs had not been a major problem in Vernonia schools. In the mid-to-late 1980’s, however, teachers and administrators observed a sharp increase in drug use. Students began to speak out about their attraction to the drug culture, and to boast that there was nothing the school could do about it. Along with more drugs came more disciplinary problems. <page-number citation-index="1" label="649">*649</page-number>Between 1988 and 1989 the number of disciplinary referrals in Vernonia schools rose to more than twice the number reported in the early 1980’s, and several students were suspended. Students became increasingly rude during class; outbursts of profane language became common.</p>
<p id="b695-5">Not only were student athletes included among the drug users but, as the District Court found, athletes were the leaders of the drug culture. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1357" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp. 1354, 1357</a></span> (Ore. 1992). This caused the District’s administrators particular concern, since drug use increases the risk of sports-related injury. Expert testimony at the trial confirmed the deleterious effects of drugs on motivation, memory, judgment, reaction, coordination, and performance. The high school football and wrestling coach witnessed a severe sternum injury suffered by a wrestler, and various omissions of safety procedures and misexecutions by football players, all attributable in his belief to the effects of drug use.</p>
<p id="b695-6">Initially, the District responded to the drug problem by offering special classes, speakers, and presentations designed to deter drug use. It even brought in a specially trained dog to detect drugs, but the drug problem persisted. According to the District Court:</p>
<blockquote id="AR5">“[T]he administration was at its wits end and ... a large segment of the student body, particularly those involved in interscholastic athletics, was in a state of rebellion. Disciplinary actions had reached ‘epidemic proportions.’ The coincidence of an almost three-fold increase in classroom disruptions and disciplinary reports along with the staff’s direct observations of students using drugs or glamorizing drug and alcohol use led the administration to the inescapable conclusion that the rebellion was being fueled by alcohol and drug abuse as well as the student’s misperceptions about the drug culture.” <em><span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/" aria-description="Citation for case: Acton v. Vernonia School District 47J">Ibid.</a></span></em></blockquote>
<p id="b695-8">At that point, District officials began considering a drug-testing program. They held a parent “input night” to dis<page-number citation-index="1" label="650">*650</page-number>cuss the proposed Student Athlete Drug Policy (Policy), and the parents in attendance gave their unanimous approval. The school board approved the Policy for implementation in the fall of 1989. Its expressed purpose is to prevent student athletes from using drugs, to protect their health and safety, and to provide drug users with assistance programs.</p>
<p id="b696-4">B</p>
<p id="b696-5">The Policy applies to all students participating in interscholastic athletics. Students wishing to play sports must sign a form consenting to the testing and must obtain the written consent of their parents. Athletes are tested at the beginning of the season for their sport. In addition, once each week of the season the names of the athletes are placed in a “pool” from which a student, with the supervision of two adults, blindly draws the names of 10% of the athletes for random testing. Those selected are notified and tested that same day, if possible.</p>
<p id="b696-6">The student to be tested completes a specimen control form which bears an assigned number. Prescription medications that the student is taking must be identified by providing a copy of the prescription or a doctor’s authorization. The student then enters an empty locker room accompanied by an adult monitor of the same sex. Each boy selected produces a sample at a urinal, remaining fully clothed with his back to the monitor, who stands approximately 12 to 15 feet behind the student. Monitors may (though do not always) watch the student while he produces the sample, and they listen for normal sounds of urination. Girls produce samples in an enclosed bathroom stall, so that they can be heard but not observed. After the sample is produced, it is given to the monitor, who checks it for temperature and tampering and then transfers it to a vial.</p>
<p id="b696-7">The samples are sent to an independent laboratory, which routinely tests them for amphetamines, cocaine, and marijuana. Other drugs, such as LSD, may be screened at the <page-number citation-index="1" label="651">*651</page-number>request of the District, but the identity of a particular student does not determine which drugs will be tested. The laboratory’s procedures are 99.94% accurate. The District follows strict procedures regarding the chain of custody and access to test results. The laboratory does not know the identity of the students whose samples it tests. It is authorized to mail written test reports only to the superintendent and to provide test results to District personnel by telephone only after the requesting official recites a code confirming his authority. Only the superintendent, principals, vice-principals, and athletic directors have access to test results, and the results are not kept for more than one year.</p>
<p id="b697-5">If a sample tests positive, a second test is administered as soon as possible to confirm the result. If the second test is negative, no further action is taken. If the second test is positive, the athlete’s parents are notified, and the school principal convenes a meeting with the student and his parents, at which the student is given the option of (1) participating for six weeks in an assistance program that includes weekly urinalysis, or (2) suffering suspension from athletics for the remainder of the current season and the next athletic season. The student is then retested prior to the start of the next athletic season for which he or she is eligible. The Policy states that a second offense results in automatic imposition of option (2); a third offense in suspension for the remainder of the current season and the next two athletic seasons.</p>
<p id="b697-6">C</p>
<p id="b697-7">In the fall of 1991, respondent James Acton, then a seventh grader, signed up to play football at one of the District’s grade schools. He was denied participation, however, because he and his parents refused to sign the testing consent forms. The Actons filed suit, seeking declaratory and in-junctive relief from enforcement of the Policy on the grounds that it violated the Fourth and Fourteenth Amendments to the United States Constitution and Article I, § 9, of the Ore<page-number citation-index="1" label="652">*652</page-number>gon Constitution. After a bench trial, the District Court entered an order denying the claims on the merits and dismissing the action. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1355" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1355</a></span>. The United States Court of Appeals for the Ninth Circuit reversed, holding that the Policy violated both the Fourth and Fourteenth Amendments and Article I, § 9, of the Oregon Constitution. <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d 1514</a></span> (1994). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./513/1013/">513 U. S. 1013</a></span> (1994).</p>
<p id="b698-5">II</p>
<p id="b698-6">The Fourth Amendment to the United States Constitution provides that the Federal Government shall not violate “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . .” We have held that the Fourteenth Amendment extends this constitutional guarantee to searches and seizures by state officers, <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span> (1960), including public school officials, <em>New Jersey </em>v. <em>T L. </em>O., <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 336-337</a></span> (1985). In <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#617" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 617</a></span> (1989), we held that state-compelled collection and testing of urine, such as that required by the Policy, constitutes a “search” subject to the demands of the Fourth Amendment. See also <em>Treasury Employees </em>v. <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#665" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S. 656, 665</a></span> (1989).</p>
<p id="b698-7">As the text of the Fourth Amendment indicates, the ultimate measure of the constitutionality of a governmental search is “reasonableness.” At least in a case such as this, where there was no clear practice, either approving or disapproving the type of search at issue, at the time the constitutional provision was enacted,<footnotemark>1</footnotemark> whether a particular search meets the reasonableness standard “ ‘is judged by balancing <page-number citation-index="1" label="653">*653</page-number>its intrusion on the individual’s Fourth Amendment interests against its promotion of legitimate governmental interests.’” <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra,</a></span> </em>at 619 (quoting <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979)). Where a search is undertaken by law enforcement officials to discover evidence of criminal wrongdoing, this Court has said that reasonableness generally requires the obtaining of a judicial warrant, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 619</a></span>. Warrants cannot be issued, of course, without the showing of probable cause required by the Warrant Clause. But a warrant is not required to establish the reasonableness of <em>all </em>government searches; and when a warrant is not required (and the Warrant Clause therefore not applicable), probable cause is not invariably required either. A search unsupported by probable cause can be constitutional, we have said, “when special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.” <em>Griffin </em>v. <em>Wisconsin, </em><span class="citation multiple-matches"><a href="/c/U.%20S./488/868/">488 U. S. 868</a></span>, 873 (1987) (internal quotation marks omitted).</p>
<p id="b699-5">We have found such “special needs” to exist in the public school context. There, the warrant requirement “would unduly interfere with the maintenance of the swift and informal disciplinary procedures [that are] needed,” and “strict adherence to the requirement that searches be based on probable cause” would undercut “the substantial need of teachers and administrators for freedom to maintain order in the schools.” <em>T L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340, 341</a></span>. The school search we approved in <em>T L. 0., </em>while not based on probable cause, <em>was </em>based on individualized <em>suspicion </em>of wrongdoing. As we explicitly acknowledged, however, “‘the Fourth Amendment imposes no irreducible requirement of such suspicion,’ ” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 342</a></span>, n. 8 (quoting <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560-561</a></span> (1976)). We have upheld sus-picionless searches and seizures to conduct drug testing of railroad personnel involved in train accidents, see <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra;</a></span> </em>to conduct random drug testing of federal customs officers who carry arms or are involved in drug interdiction, <page-number citation-index="1" label="654">*654</page-number>see <em>Von <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Raab, supra;</a></span> </em>and to maintain automobile checkpoints looking for illegal immigrants and contraband, <em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra,</a></span> </em>and drunk drivers, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U. S. 444</a></span> (1990).</p>
<p id="b700-7">1 — 1 1 — 1</p>
<p id="b700-3">The first factor to be considered is the nature of the privacy interest upon which the search here at issue intrudes. The Fourth Amendment does not protect all subjective expectations of privacy, but only those that society recognizes as “legitimate.” <em>T L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#338" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 338</a></span>. What expectations are legitimate varies, of course, with context, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 337</a></span>, depending, for example, upon whether the individual asserting the privacy interest is at home, at work, in a car, or in a public park. In addition, the legitimacy of certain privacy expectations vis-a-vis the State may depend upon the individual’s legal relationship with the State. For example, in <em>Griffin, supra, </em>we held that, although a “probationer’s home, like anyone else’s, is protected by the Fourth Amendment,” the supervisory relationship between probationer and State justifies “a degree of impingement upon [a probationer’s] privacy that would not be constitutional if applied to the public at large.” 483 U. S., at 873, 875. Central, in our view, to the present case is the fact that the subjects of the Policy are (1) children, who (2) have been committed to the temporary custody of the State as schoolmaster.</p>
<p id="b700-4">Traditionally at common law, and still today, unemanci-pated minors lack some of the most fundamental rights of self-determination — including even the right of liberty in its narrow sense, <em>i. e., </em>the right to come and go at will. They are subject, even as to their physical freedom, to the control of their parents or guardians. See 59 Am. Jur. 2d, Parent and Child §10 (1987). When parents place minor children in private schools for their education, the teachers and administrators of those schools stand <em>in loco parentis </em>over the children entrusted to them. In fact, the tutor or schoolmas<page-number citation-index="1" label="655">*655</page-number>ter is the very prototype of that status. As Blackstone describes it, a parent “may . . . delegate part of his parental authority, during his life, to the tutor or schoolmaster of his child; who is then <em>in loco parentis, </em>and has such a portion of the power of the parent committed to his charge, viz. that of restraint and correction, as may be necessary to answer the purposes for which he is employed.” 1 W. Blackstone, Commentaries on the Laws of England 441 (1769).</p>
<p id="b701-5">In <em>I L. O. </em>we rejected the notion that public schools, like private schools, exercise only parental power over their students, which of course is not subject to constitutional constraints. <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 336</a></span>. Such a view of things, we said, “is not entirely ‘consonant with compulsory education laws/ ” <em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">ibid.</a></span> </em>(quoting <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#662" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 662</a></span> (1977)), and is inconsistent with our prior decisions treating school officials as state actors for purposes of the Due Process and Free Speech Clauses, <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#336" aria-description="Citation for case: New Jersey v. T. L. O."><em>T L. O., supra, </em>at 336</a></span>. But while denying that the State’s power over schoolchildren is formally no more than the delegated power of their parents, <em>T. L. O. </em>did not deny, but indeed emphasized, that the nature of that power is custodial and tutelary, permitting a degree of supervision and control that could not be exercised over free adults. “[A] proper educational environment requires close supervision of schoolchildren, as well as the enforcement of rules against conduct that would be perfectly permissible if undertaken by an adult.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#339" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 339</a></span>. While we do not, of course, suggest that public schools as a general matter have such a degree of control over children as to give rise to a constitutional “duty to protect,” see <em>DeShaney </em>v. <em>Winnebago County Dept. of Social Servs., </em><span class="citation" data-id="9431570"><a href="/opinion/112202/deshaney-v-winnebago-county-department-of-social-services/#200" aria-description="Citation for case: DeShaney v. Winnebago County Department of Social Services">489 U. S. 189, 200</a></span> (1989), we have acknowledged that for many purposes “school authorities ac[t] <em>in loco parentis,” Bethel School Dist. No. 403 </em>v. <em>Fraser, </em><span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#684" aria-description="Citation for case: Bethel School District No. 403 v. Fraser">478 U. S. 675, 684</a></span> (1986), with the power and indeed the duty to “inculcate the habits and manners of civility,” <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#681" aria-description="Citation for case: Bethel School District No. 403 v. Fraser"><em>id., </em>at 681</a></span> (internal quotation marks omitted). Thus, while children assuredly do not “shed their constitutional <page-number citation-index="1" label="656">*656</page-number>rights ... at the schoolhouse gate,” <em>Tinker </em>v. <em>Des Moines Independent Community School Dist., </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#506" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 506</a></span> (1969), the nature of those rights is what is appropriate for children in school. See, <em>e. g., Goss </em>v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#581" aria-description="Citation for case: Goss v. Lopez">419 U. S. 565, 581-582</a></span> (1975) (due process for a student challenging disciplinary suspension requires only that the teacher “informally discuss the alleged misconduct with the student minutes after it has occurred”); <span class="citation" data-id="9430701"><a href="/opinion/111754/bethel-school-district-no-403-v-fraser/#683" aria-description="Citation for case: Bethel School District No. 403 v. Fraser"><em>Fraser, supra, </em>at 683</a></span> (“[I]t is a highly appropriate function of public school education to prohibit the use of vulgar and offensive terms in public discourse”); <em>Hazelwood School Dist. </em>v. <em>Kuhlmeier, </em><span class="citation" data-id="9431159"><a href="/opinion/111979/hazelwood-school-district-v-kuhlmeier/#273" aria-description="Citation for case: Hazelwood School District v. Kuhlmeier">484 U. S. 260, 273</a></span> (1988) (public school authorities may censor school-sponsored publications, so long as the censorship is “reasonably related to legitimate pedagogical concerns”); <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#682" aria-description="Citation for case: Ingraham v. Wright"><em>Ingraham, supra, </em>at 682</a></span> (“Imposing additional administrative safeguards [upon corporal punishment]... would ... entail a significant intrusion into an area of primary educational responsibility”).</p>
<p id="b702-5">Fourth Amendment rights, no less than First and Fourteenth Amendment rights, are different in public schools than elsewhere; the “reasonableness” inquiry cannot disregard the schools’ custodial and tutelary responsibility for children. For their own good and that of their classmates, public school children are routinely required to submit to various physical examinations, and to be vaccinated against various diseases. According to the American Academy of Pediatrics, most public schools “provide vision and hearing screening and dental and dermatological checks. . . . Others also mandate scoliosis screening at appropriate grade levels.” Committee on School Health, American Academy of Pediatrics, School Health: A Guide for Health Professionals 2 (1987). In the 1991-1992 school year, all 50 States required public school students to be vaccinated against diphtheria, measles, rubella, and polio. U. S. Dept, of Health &amp; Human Services, Public Health Service, Centers for Disease Control, State Immunization Requirements 1991-1992, p. 1. Particularly with regard to medical examinations and proce<page-number citation-index="1" label="657">*657</page-number>dures, therefore, “students within the school environment have a lesser expectation of privacy than members of the population generally.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#348" aria-description="Citation for case: New Jersey v. T. L. O."><em>I L. O., supra, </em>at 348</a></span> (Powell, J., concurring).</p>
<p id="b703-5">Legitimate privacy expectations are even less with regard to student athletes. School sports are not for the bashful. They require “suiting up” before each practice or event, and showering and changing afterwards. Public school locker rooms, the usual sites for these activities, are not notable for the privacy they afford. The locker rooms in Vernonia are typical: No individual dressing rooms are provided; shower heads are lined up along a wall, unseparated by any sort of partition or curtain; not even all the toilet stalls have doors. As the United States Court of Appeals for the Seventh Circuit has noted, there is “an element of ‘communal undress’ inherent in athletic participation,” <em>Schaill by Kross </em>v. <em>Tippecanoe County School Corp., </em><span class="citation" data-id="8966879"><a href="/opinion/8975213/schaill-ex-rel-kross-v-tippecanoe-county-school-corp/#1318" aria-description="Citation for case: Schaill ex rel. Kross v. Tippecanoe County School Corp.">864 F. 2d 1309, 1318</a></span> (1988).</p>
<p id="b703-6">There is an additional respect in which school athletes have a reduced expectation of privacy. By choosing to “go out for the team,” they voluntarily subject themselves to a degree of regulation even higher than that imposed on students generally. In Vernonia’s public schools, they must submit to a preseason physical exam (James testified that his included the giving of a urine sample, App. 17), they must acquire adequate insurance coverage or sign an insurance waiver, maintain a minimum grade point average, and comply with any “rules of conduct, dress, training hours and related matters as may be established for each sport by the head coach and athletic director with the principal’s approval.” Record, Exh. 2, p. 30, ¶ 8. Somewhat like adults who choose to participate in a “closely regulated industry,” students who voluntarily participate in school athletics have reason to expect intrusions upon normal rights and privileges, including privacy. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#627" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 627</a></span>; <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316</a></span> (1972).</p>
<p id="b704-7">
<page-number citation-index="1" label="658">*658</page-number>
<em>&gt;</em>
</p>
<p id="b704-3">Having considered the scope of the legitimate expectation of privacy at issue here, we turn next to the character of the intrusion that is complained of. We recognized in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>that collecting the samples for urinalysis intrudes upon “an excretory function traditionally shielded by great privacy.” 489 U. S., at 626. We noted, however, that the degree of intrusion depends upon the manner in which production of the urine sample is monitored. <em>Ibid. </em>Under the District’s Policy, male students produce samples at a urinal along a wall. They remain fully clothed and are only observed from behind, if at all. Female students produce samples in an enclosed stall, with a female monitor standing outside listening only for sounds of tampering. These conditions are nearly identical to those typically encountered in public restrooms, which men, women, and especially schoolchildren use daily. Under such conditions, the privacy interests compromised by the process of obtaining the urine sample are in our view negligible.</p>
<p id="b704-4">The other privacy-invasive aspect of urinalysis is, of course, the information it discloses concerning the state of the subject’s body, and the materials he has ingested. In this regard it is significant that the tests at issue here look only for drugs, and not for whether the student is, for example, epileptic, pregnant, or diabetic. See <em>id., </em>at 617. Moreover, the drugs for which the samples are screened are standard, and do not vary according to the identity of the student. And finally, the results of the tests are disclosed only to a limited class of school personnel who have a need to know; and they are not turned over to law enforcement authorities or used for any internal disciplinary function. <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1364" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1364</a></span>; see also <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/#1521" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d, at 1521</a></span>.<footnotemark>2</footnotemark></p>
<p id="b705-3"><page-number citation-index="1" label="659">*659</page-number>Respondents argue, however, that the District’s Policy is in fact more intrusive than this suggests, because it requires the students, if they are to avoid sanctions for a falsely positive test, to identify <em>in advance </em>prescription medications they are taking. We agree that this raises some cause for concern. In <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>we flagged as one of the salutary features of the Customs Service drug-testing program the fact that employees were not required to disclose medical information unless they tested positive, and, even then, the information was supplied to a licensed physician rather than to the Government employer. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#672" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 672-673, n. 2</a></span>. On the other hand, we have never indicated that requiring advance disclosure of medications is <em>per se </em>unreasonable. Indeed, in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>we held that it was not <em>“a </em>significant invasion of privacy.” 489 U. S., at 626, n. 7. It can be argued that, in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>the disclosure went only to the medical personnel taking the sample, and the Government personnel analyzing it, see <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#609" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>id., </em>at 609</a></span>, but see <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#610" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>id., </em>at 610</a></span> (railroad personnel responsible for forwarding the sample, and presumably accompanying information, to the Government’s testing lab); and that disclosure to teachers and coaches — to persons who personally <em>know </em>the student — is a greater invasion of privacy. Assuming for the sake of argu<page-number citation-index="1" label="660">*660</page-number>ment that both those propositions are true, we do not believe they establish a difference that respondents are entitled to rely on here.</p>
<p id="b706-5">The General Authorization Form that respondents refused to sign, which refusal was the basis for James’s exclusion from the sports program, said only (in relevant part): “I . . . authorize the Vernonia School District to conduct a test on a urine specimen which I provide to test for drugs and/or alcohol use. I also authorize the release of information concerning the results of such a test to the Vernonia School District and to the parents and/or guardians of the student.” App. 10-11. While the practice of the District seems to have been to have a school official take medication information from the student at the time of the test, see <em>id., </em>at 29, 42, that practice is not set forth in, or required by, the Policy, which says simply: “Student athletes who . . . are or have been taking prescription medication must provide verification (either by a copy of the prescription or by doctor’s authorization) prior to being tested.” <em>Id., </em>at 8. It may well be that, if and when James was selected for random testing at a time that he was taking medication, the School District would have permitted him to provide the requested information in a confidential manner — for example, in a sealed envelope delivered to the testing lab. Nothing in the Policy contradicts that, and when respondents choose, in effect, to challenge the Policy on its face, we will not assume the worst. Accordingly, we reach the same conclusion as in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>: </em>that the invasion of privacy was not significant.</p>
<p id="b706-6">V</p>
<p id="b706-7">Finally, we turn to consider the nature and immediacy of the governmental concern at issue here, and the efficacy of this means for meeting it. In both <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span> </em>and <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>we characterized the government interest motivating the search as “compelling.” <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 628</a></span> (interest in preventing railway accidents); <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#670" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 670</a></span> (in<page-number citation-index="1" label="661">*661</page-number>terest in ensuring fitness of customs officials to interdict drugs and handle firearms). Relying on these cases, the District Court held that because the District’s program also called for drug testing in the absence of individualized suspicion, the District “must demonstrate a ‘compelling need’ for the program.” <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1368" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1368</a></span>. The Court of Appeals appears to have agreed with this view. See <span class="citation" data-id="9486735"><a href="/opinion/669794/wayne-acton-and-judy-acton-guardians-ad-litem-for-james-acton-v-vernonia/#1526" aria-description="Citation for case: Wayne Acton and Judy Acton, Guardians Ad Litem for James...">23 F. 3d, at 1526</a></span>. It is a mistake, however, to think that the phrase “compelling state interest,” in the Fourth Amendment context, describes a fixed, minimum quantum of governmental concern, so that one can dispose of a case by answering in isolation the question: Is there a compelling state interest here? Rather, the phrase describes an interest that appears <em>important enough </em>to justify the particular search at hand, in light of other factors that show the search to be relatively intrusive upon a genuine expectation of privacy. Whether that relatively high degree of government concern is necessary in this case or not, we think it is met.</p>
<p id="b707-5">That the nature of the concern is important — indeed, perhaps compelling — can hardly be doubted. Deterring drug use by our Nation’s schoolchildren is at least as important as enhancing efficient enforcement of the Nation’s laws against the importation of drugs, which was the governmental concern in <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#668" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Von Raab, supra, </em>at 668</a></span>, or deterring drug use by engineers and trainmen, which was the governmental concern in <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#628" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 628</a></span>. School years are the time when the physical, psychological, and addictive effects of drugs are most severe. “Maturing nervous systems are more critically impaired by intoxicants than mature ones are; childhood losses in learning are lifelong and profound”; “children grow chemically dependent more quickly than adults, and their record of recovery is depressingly poor.” Hawley, The Bumpy Road to Drug-Free Schools, 72 Phi Delta Kap-pan 310, 314 (1990). See also Estroff, Schwartz, &amp; Hoff-mann, Adolescent Cocaine Abuse: Addictive Potential, Behavioral and Psychiatric Effects, 28 Clinical Pediatrics 550 <page-number citation-index="1" label="662">*662</page-number>(Dec. 1989); Kandel, Davies, Karus, &amp; Yamaguchi, The Consequences in Young Adulthood of Adolescent Drug Involvement, 43 Arch. Gen. Psychiatry 746 (Aug. 1986). And of course the effects of a drug-infested school are visited not just upon the users, but upon the entire student body and faculty, as the educational process is disrupted. In the present case, moreover, the necessity for the State to act is magnified by the fact that this evil is being visited not just upon individuals at large, but upon children for whom it has undertaken a special responsibility of care and direction. Finally, it must not be lost sight of that this program is directed more narrowly to drug use by school athletes, where the risk of immediate physical harm to the drug user or those with whom he is playing his sport is particularly high. Apart from psychological effects, which include impairment of judgment, slow reaction time, and a lessening of the perception of pain, the particular drugs screened by the District’s Policy have been demonstrated to pose substantial physical risks to athletes. Amphetamines produce an “artificially induced heart rate increase, [peripheral vasoconstriction, [b]lood pressure increase, and [mjasking of the normal fatigue response,” making them a “very dangerous drug when used during exercise of any type.” Hawkins, Drugs and Other Ingesta: Effects on Athletic Performance, in H. Appenzeller, Managing Sports and Risk Management Strategies 90, 90-91 (1993). Marijuana causes “[ijrregular blood pressure responses during changes in body position,” “[Reduction in the oxygen-carrying capacity of the blood,” and “[ijnhibition of the normal sweating responses resulting in increased body temperature.” <em>Id., </em>at 94. Cocaine produces “[vjasocon-striction[,] [e]levated blood pressure,” and “[possible coronary artery spasms and myocardial infarction.” <em>Ibid.</em></p>
<p id="b708-5">As for the immediacy of the District’s concerns: We are not inclined to question — indeed, we could not possibly find clearly erroneous — the District Court’s conclusion that “a large segment of the student body, particularly those in<page-number citation-index="1" label="663">*663</page-number>volved in interscholastic athletics, was in a state of rebellion,” that “[disciplinary actions had reached ‘epidemic proportions/” and that “the rebellion was being fueled by alcohol and drug abuse as well as by the student’s mispercep-tions about the drug culture.” <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1357" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1357</a></span>. That is an immediate crisis of greater proportions than existed in <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner</a></span>, </em>where we upheld the Government’s drug-testing program based on findings of drug use by railroad employees nationwide, without proof that a problem existed on the particular railroads whose employees were subject to the test. See <em>Skinner, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#607" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S., at 607</a></span>. And of much greater proportions than existed in <em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">Von Raab</a></span>, </em>where there was no documented history of drug use by any customs officials. See <em>Von Raab, </em><span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#673" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">489 U. S., at 673</a></span>; <span class="citation" data-id="9431609"><a href="/opinion/112220/national-treasury-employees-union-v-von-raab/#683" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>id., </em>at 683</a></span> (Scalia, J., dissenting).</p>
<p id="b709-5">As to the efficacy of this means for addressing the problem: It seems to us self-evident that a drug problem largely fueled by the “role model” effect of athletes’ drug use, and of particular danger to athletes, is effectively addressed by making sure that athletes do not use drugs. Respondents argue that a “less intrusive means to the same end” was available, namely, “drug testing on suspicion of drug use.” Brief for Respondents 45-46. We have repeatedly refused to declare that only the “least intrusive” search practicable can be reasonable under the Fourth Amendment. <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#629" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><em>Skinner, supra, </em>at 629, n. 9</a></span> (collecting cases). Respondents’ alternative entails substantial difficulties — if it is indeed practicable at all. It may be impracticable, for one thing, simply because the parents who are willing to accept random drug testing for athletes are not willing to accept accusatory drug testing for all students, which transforms the process into a badge of shame. Respondents’ proposal brings the risk that teachers will impose testing arbitrarily upon troublesome but not drug-likely students. It generates the expense of defending lawsuits that charge such arbitrary imposition, or that simply demand greater process before accusatory drug</p>
<p id="b710-6"><page-number citation-index="1" label="664">*664</page-number>testing is imposed. And not least of all, it adds to the ever-expanding diversionary duties of schoolteachers the new function of spotting and bringing to account drug abuse, a task for which they are ill prepared, and which is not readily compatible with their vocation. Cf. <em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">Skinner, supra,</a></span> </em>at 628 (quoting <span class="citation no-link">50 Fed. Reg. 31526</span> (1985)) (a drug impaired individual “will seldom display any outward ‘signs detectable by the lay person or, in many cases, even the physician’”); <em>Goss, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#594" aria-description="Citation for case: Goss v. Lopez">419 U. S., at 594</a></span> (Powell, J., dissenting) (“There is an ongoing relationship, one in which the teacher must occupy many roles — educator, adviser, friend, and, at times, parent-substitute. It is rarely adversary in nature . . .”) (footnote omitted). In many respects, we think, testing based on “suspicion” of drug use would not be better, but worse.<footnotemark>3</footnotemark></p>
<p id="b710-7">
<em>&gt;</em>
</p>
<p id="b710-3">Taking into account all the factors we have considered above — the decreased expectation of privacy, the relative unobtrusiveness of the search, and the severity of the need met <page-number citation-index="1" label="665">*665</page-number>by the search — we conclude Vernonia’s Policy is reasonable and hence constitutional.</p>
<p id="b711-5">We caution against the assumption that suspicionless drug testing will readily pass constitutional muster in other contexts. The most significant element in this case is the first we discussed: that the Policy was undertaken in furtherance of the government’s responsibilities, under a public school system, as guardian and tutor of children entrusted to its care.<footnotemark>4</footnotemark> Just as when the government conducts a search in its capacity as employer (a warrantless search of an absent employee’s desk to obtain an urgently needed file, for example), the relevant question is whether that intrusion upon privacy is one that a reasonable employer might engage in, see <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987); so also when the government acts as guardian and tutor the relevant question is whether the search is one that a reasonable guardian and tutor might undertake. Given the findings of need made by the District Court, we conclude that in the present case it is.</p>
<p id="b711-6">We may note that the primary guardians of Vernonia’s schoolchildren appear to agree. The record shows no objection to this districtwide program by any parents other than the couple before us here — even though, as we have described, a public meeting was held to obtain parents’ views. We find insufficient basis to contradict the judgment of Ver-nonia’s parents, its school board, and the District Court, as to what was reasonably in the interest of these children under the circumstances.</p>
<p id="ATj"><page-number citation-index="1" label="666">*666</page-number>* * *</p>
<p id="b712-4">The Ninth Circuit held that Vernonia’s Policy not only violated the Fourth Amendment, but also, by reason of that violation, contravened Article I, § 9, of the Oregon Constitution. Our conclusion that the former holding was in error means that the latter holding rested on a flawed premise. We therefore vacate the judgment, and remand the case to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p id="b712-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b698-8"> Not until 1852 did Massachusetts, the pioneer in the “common school” movement, enact a compulsory school-attendance law, and as late as the 1870’s only 14 States had such laws. R. Butts, Public Education in the United States From Revolution to Reform 102-103 (1978); 1 Children and Youth in America 467-468 (R. Bremner ed. 1970). The drug problem, and the technology of drug testing, are of course even more recent.</p>
</footnote>
<footnote label="2">
<p id="b704-5"> Despite the fact that, like routine school physicals and vaccinations— which the dissent apparently finds unobjectionable even though they “are both blanket searches of a sort,” <em>post, </em>at 682 — the search here is undertaken for prophylactic and distinctly wowpunitive purposes (protecting <page-number citation-index="1" label="659">*659</page-number>student athletes from injury, and deterring drug use in the student population), see <span class="citation" data-id="1559138"><a href="/opinion/1559138/acton-v-vernonia-school-district-47j/#1363" aria-description="Citation for case: Acton v. Vernonia School District 47J">796 F. Supp., at 1363</a></span>, the dissent would nonetheless lump this search together with “evidentiary” searches, which generally require probable cause, see <em>supra, </em>at 653, because, from the student’s perspective, the test may be “regarded” or “understood” as punishment, <em>post, </em>at 683-684. In light of the District Court’s findings regarding the purposes and consequences of the testing, any such perception is by definition an irrational one, which is protected nowhere else in the law. In any event, our point is not, as the dissent apparently believes, <em>post, </em>at 682-683, that <em>since </em>student vaccinations and physical exams are constitutionally reasonable, student drug testing must be so as well; but rather that, by reason of those prevalent practices, public school children in general, and student athletes in particular, have a diminished expectation of privacy. See <em>supra, </em>at 656-657.</p>
</footnote>
<footnote label="3">
<p id="b710-4"> There is no basis for the dissent’s insinuation that in upholding the District’s Policy we are equating the Fourth Amendment status of schoolchildren and prisoners, who, the dissent asserts, may have what it calls the “categorical protection” of a “strong preference for an individualized suspicion requirement,” <em>post, </em>at 681. The case on which it relies for that proposition, <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520</a></span> (1979), displays no stronger a preference for individualized suspicion than we do today. It reiterates the proposition on which we rely, that “‘elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all search-and-seizure powers.’” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish"><em>Id., </em>at 559</a></span>, n. 40 (quoting <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-557, n. 12</a></span> (1976)). Even Wolfish’s <em>arguendo </em>“assum[ption] that the existence of less intrusive alternatives is relevant to the determination of the reasonableness of the particular search method at issue,” <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S., at 559, n. 40</a></span>, does not support the dissent, for the opinion ultimately rejected the hypothesized alternative (as we do) on the ground that it would impair other policies important to the institution. See <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#560" aria-description="Citation for case: Bell v. Wolfish"><em>id., </em>at 560, n. 40</a></span> (monitoring of visits instead of conducting body searches would destroy “the confidentiality and intimacy that these visits are intended to afford”).</p>
</footnote>
<footnote label="4">
<p id="b711-7"> The dissent devotes a few meager paragraphs of its 21 pages to this central aspect of the testing program, see <em>post, </em>at 680-682, in the course of which it shows none of the interest in the original meaning of the Fourth Amendment displayed elsewhere in the opinion, see <em>post, </em>at 669-671. Of course at the time of the framing, as well as at the time of the adoption of the Fourteenth Amendment, children had substantially fewer “rights” than legislatures and courts confer upon them today. See 1 D. Kramer, Legal Rights of Children § 1.02, p. 9 (2d ed. 1994); Wald, Children’s Rights: A Framework for Analysis, 12 U. C. D. L. Rev. 255, 256 (1979).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Virginia v. Moore.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Virginia v. Moore"
type: case
citation: "553 U.S. 164 (2008)"
parallel_cite: "128 S. Ct. 1598; 170 L. Ed. 2d 559"
neutral_cite: 2008 U.S. LEXIS 3674
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2008
date_decided: 2008-04-23
docket: 06-1082
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2008-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Virginia v. Moore
  varies_by_point: false
  scope_note: "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145814/virginia-v-moore/"
  cluster_id: 145814
  opinion_id: 145814
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — a state-law arrest violation is not a Fourth Amendment violation"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
  - page: "[[The Exclusionary Rule]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Robinson]]", "[[Atwater v. City of Lago Vista]]", "[[Knowles v. Iowa]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "search-incident-to-arrest", "exclusionary-rule", "state-law"]
holding: "A warrantless arrest on probable cause for a crime committed in the officer's presence is reasonable under the Fourth Amendment even if state law forbade the arrest (requiring a summons); the search incident requires no additional justification, and a state-law-only violation does not trigger exclusion."
lake:
  record_id: Virginia v. Moore
  status: verified
  projected_at: 2026-07-06
---

# Virginia v. Moore

*553 U.S. 164 (2008)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers stopped Moore and determined he was driving on a suspended license — a misdemeanor for which Virginia law directed officers to issue a summons rather than make a custodial arrest. The officers arrested Moore anyway, searched him incident to the arrest, and found crack cocaine. Moore moved to suppress, arguing the arrest violated state law and the search was therefore invalid.

## Issue
Does the Fourth Amendment require suppression of evidence found in a search incident to an arrest that was based on probable cause but prohibited by state law, where state law required a citation instead of a custodial arrest?

## Rule
No. "[W]arrantless arrests for crimes committed in the presence of an arresting officer are reasonable under the Constitution, and . . . while States are free to regulate such arrests however they desire, state restrictions do not alter the Fourth Amendment's protections." — 128 S. Ct. at 1607. ^pin-1607

Because such an arrest is constitutionally valid, "officers may perform searches incident to constitutionally permissible arrests in order to ensure their safety and safeguard evidence" — a "search incident to the arrest requires no additional justification." — *Id.* (quoting *United States v. Robinson*). And because only state law, not the Constitution, was violated, "[t]hat Amendment does not require the exclusion of evidence obtained from a constitutionally permissible arrest." Reaffirming the rule, the Court held: "When officers have probable cause to believe that a person has committed a crime in their presence, the Fourth Amendment permits them to make an arrest, and to search the suspect in order to safeguard evidence and ensure their own safety." — *Id.* at 1608. ^pin-1608

## Application
The officers had probable cause to believe Moore was driving on a suspended license — an offense committed in their presence — so the arrest was reasonable under the Fourth Amendment even though Virginia law called for a summons. The Fourth Amendment is not a vehicle for enforcing state arrest law. Because the arrest was constitutionally permissible, the search incident to it required no additional justification, and the cocaine it produced was admissible. *[[Knowles v. Iowa]]* did not control, because Moore was arrested — and therefore the officers faced the custodial risks that justify a full search — rather than merely cited.

## Conclusion
The arrest and the search incident to it were constitutional; the Fourth Amendment did not require suppression. The judgment of the Supreme Court of Virginia was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Moore* remains controlling: a probable-cause arrest is Fourth-Amendment-reasonable regardless of contrary state arrest law, the search incident follows automatically, and a state-law-only violation does not trigger the exclusionary rule. It applies [[United States v. Robinson]] and runs alongside [[Atwater v. City of Lago Vista]] and [[Devenpeck v. Alford]]. No negative treatment.

## Appears on
- [[Arrest and Arrest Warrants]] — *Key*
- [[Seizure of the Person]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Virginia v. Moore*, 553 U.S. 164 (2008) — https://www.courtlistener.com/opinion/145814/virginia-v-moore/ — pinpoints (S. Ct. reporter, per CL copy): 1607, 1608.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "395b14108f9bce9e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Virginia v. Moore"}, "payload": {"all": [{"cite": "553 U.S. 164", "page": "164", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "553"}, {"cite": "128 S. Ct. 1598", "page": "1598", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "128"}, {"cite": "170 L. Ed. 2d 559", "page": "559", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "170"}, {"cite": "2008 U.S. LEXIS 3674", "page": "3674", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2008"}], "display": "553 U.S. 164", "official": {"cite": "553 U.S. 164", "page": "164", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "553"}, "official_selection_present": true, "record_id": "Virginia v. Moore"}}
{"assertion_id": "3aeabe33a5f369e8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1607", "record_id": "Virginia v. Moore"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1607", "pinpoint_status": "slip-only", "quote": "--- # Virginia v. Moore *553 U.S. 164 (2008)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Moore and determined he was driving on a suspended license — a misdemeanor for which Virginia law directed officers to issue a summons rather than make a custodial arrest. The officers arrested Moore anyway, searched him incident to the arrest, and found crack cocaine. Moore moved to suppress, arguing the arrest violated state law and the search was therefore invalid. ## Issue Does the Fourth Amendment require suppression of evidence found in a search incident to an arrest that was based on probable cause but prohibited by state law, where state law required a citation instead of a custodial arrest? ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Virginia v. Moore", "star_marker": null}}
{"assertion_id": "71d7026c673ea1ec", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1608", "record_id": "Virginia v. Moore"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1608", "pinpoint_status": "slip-only", "quote": "officers may perform searches incident to constitutionally permissible arrests in order to ensure their safety and safeguard evidence", "quote_fidelity": "mismatch", "record_id": "Virginia v. Moore", "star_marker": null}}
{"assertion_id": "22acbb76118ba14a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Virginia v. Moore"}, "payload": {"as_of_content": "2008-04-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Virginia v. Moore", "scope_note": "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation.", "varies_by_point": false}}
```

### lake record — Virginia v. Moore

```json
{
  "schema_version": "s2.v1",
  "record_id": "Virginia v. Moore",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Virginia v. Moore",
    "case_name_short": "Moore",
    "case_name_full": "Virginia v. Moore",
    "input_case_name": "Virginia v. Moore",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2008-04-23",
    "year": 2008,
    "docket": "06-1082",
    "cluster_id": 145814,
    "lead_opinion_id": 145814,
    "sibling_ids": [
      145814,
      9435233,
      9435234
    ],
    "absolute_url": "/opinion/145814/virginia-v-moore/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "553 U.S. 164",
      "volume": "553",
      "reporter": "U.S.",
      "page": "164",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "128 S. Ct. 1598",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "1598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "170 L. Ed. 2d 559",
        "volume": "170",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2008 U.S. LEXIS 3674",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "3674",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "553 U.S. 164",
        "volume": "553",
        "reporter": "U.S.",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "128 S. Ct. 1598",
        "volume": "128",
        "reporter": "S. Ct.",
        "page": "1598",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "170 L. Ed. 2d 559",
        "volume": "170",
        "reporter": "L. Ed. 2d",
        "page": "559",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2008 U.S. LEXIS 3674",
        "volume": "2008",
        "reporter": "U.S. LEXIS",
        "page": "3674",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "553 U.S. 164",
    "official_selection": {
      "court_class": "scotus",
      "selected": "553 U.S. 164",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1607",
      "page": null,
      "quote": "--- # Virginia v. Moore *553 U.S. 164 (2008)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Moore and determined he was driving on a suspended license \u2014 a misdemeanor for which Virginia law directed officers to issue a summons rather than make a custodial arrest. The officers arrested Moore anyway, searched him incident to the arrest, and found crack cocaine. Moore moved to suppress, arguing the arrest violated state law and the search was therefore invalid. ## Issue Does the Fourth Amendment require suppression of evidence found in a search incident to an arrest that was based on probable cause but prohibited by state law, where state law required a citation instead of a custodial arrest? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1608",
      "page": null,
      "quote": "officers may perform searches incident to constitutionally permissible arrests in order to ensure their safety and safeguard evidence",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2008-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Virginia v. Moore",
    "varies_by_point": false,
    "scope_note": "Controlling: an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law; the search incident follows and no suppression results from the state-law violation.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ragbir v. Homan",
          "cluster_id": 8443991,
          "cite": [
            "923 F.3d 53"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Islas",
          "cluster_id": 4597157,
          "cite": [
            "443 P.3d 274",
            "165 Idaho 260"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kelm",
          "cluster_id": 890265,
          "cite": [
            "2013 MT 115",
            "370 Mont. 61",
            "300 P.3d 687",
            "2013 WL 1804265",
            "2013 Mont. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mattos v. Agarano",
          "cluster_id": 615433,
          "cite": [
            "661 F.3d 433",
            "2011 WL 4908374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane1_negative"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York State Rifle & Pistol Assn., Inc. v. Bruen",
          "cluster_id": 6480696,
          "cite": [
            "597 U.S. 1",
            "142 S. Ct. 2111",
            "213 L. Ed. 2d 387"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
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
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Redd",
          "cluster_id": 2387024,
          "cite": [
            "48 Cal. 4th 691",
            "229 P.3d 101",
            "108 Cal. Rptr. 3d 192",
            "2010 Cal. LEXIS 3749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. City of Los Angeles",
          "cluster_id": 3053953,
          "cite": [
            "548 F.3d 1197",
            "2008 WL 4878904"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Quinn v. Young",
          "cluster_id": 2786042,
          "cite": [
            "780 F.3d 998",
            "2015 U.S. App. LEXIS 3959",
            "2015 WL 1089573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elliott v. State",
          "cluster_id": 7479349,
          "cite": [
            "824 S.E.2d 265",
            "305 Ga. 179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Ontario v. Quon",
          "cluster_id": 148797,
          "cite": [
            "177 L. Ed. 2d 216",
            "130 S. Ct. 2619",
            "560 U.S. 746",
            "2010 U.S. LEXIS 4972"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edgerly v. City and County of San Francisco",
          "cluster_id": 409,
          "cite": [
            "599 F.3d 946",
            "2010 U.S. App. LEXIS 5697",
            "2010 WL 986764"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Victor Garcia-Rodriguez",
          "cluster_id": 4400153,
          "cite": [
            "162 Idaho 271",
            "396 P.3d 700",
            "2017 WL 2569786",
            "2017 Ida. LEXIS 171"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bishop",
          "cluster_id": 2640962,
          "cite": [
            "203 P.3d 1203",
            "146 Idaho 804",
            "2009 Ida. LEXIS 19"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Buck v. City of Albuquerque",
          "cluster_id": 171480,
          "cite": [
            "549 F.3d 1269",
            "2008 U.S. App. LEXIS 25450",
            "2008 WL 5147474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stephen G. House",
          "cluster_id": 802697,
          "cite": [
            "684 F.3d 1173",
            "2012 U.S. App. LEXIS 12596",
            "2012 WL 2343665"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberal v. Estrada",
          "cluster_id": 183026,
          "cite": [
            "632 F.3d 1064",
            "2011 U.S. App. LEXIS 957",
            "2011 WL 149348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2637645,
          "cite": [
            "224 P.3d 55",
            "47 Cal. 4th 1104",
            "104 Cal. Rptr. 3d 727",
            "2010 Cal. LEXIS 114"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amobi v. District of Columbia Department of Corrections",
          "cluster_id": 2680783,
          "cite": [
            "410 U.S. App. D.C. 338",
            "755 F.3d 980",
            "38 I.E.R. Cas. (BNA) 1116",
            "2014 WL 2895933",
            "2014 U.S. App. LEXIS 12117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antoine Jones v. Steve Kirchner",
          "cluster_id": 4251490,
          "cite": [
            "835 F.3d 74",
            "2016 U.S. App. LEXIS 15759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Prince George's County, Md.",
          "cluster_id": 1029542,
          "cite": [
            "575 F.3d 426",
            "2009 U.S. App. LEXIS 16872",
            "2009 WL 2343614"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miguel Gutierrez v. Michael Kermon",
          "cluster_id": 2709559,
          "cite": [
            "722 F.3d 1003",
            "2013 WL 3481359",
            "2013 U.S. App. LEXIS 14101"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Virginia v. Moore:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145814 OR 9435233 OR 9435234) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjk3MzgyNDAwMDAwJnM9MjQ2NzYwOCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145814+OR+9435233+OR+9435234%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145814 OR 9435233 OR 9435234)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MiZzPTE4MDMzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145814+OR+9435233+OR+9435234%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145814 OR 9435233 OR 9435234)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 0,
        "triage_snippet_classified": 40
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145814 OR 9435233 OR 9435234)",
    "indexed_citing_opinions": 401,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145814,
        "count": 306,
        "count_source": "search"
      },
      {
        "opinion_id": 9435233,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9435234,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 795,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/virginia-v-moore.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTI3NTUmcz0xMDMyNTMyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145814+OR+9435233+OR+9435234%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145814,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 110127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1063368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1322589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 1344610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 3579530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145814,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T03:53:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:56:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:53:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Virginia v. Moore

```
(Slip Opinion)              OCTOBER TERM, 2007                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                           VIRGINIA v. MOORE

        CERTIORARI TO THE SUPREME COURT OF VIRGINIA

    No. 06–1082. Argued January 14, 2008—Decided April 23, 2008
Rather than issuing the summons required by Virginia law, police ar-
  rested respondent Moore for the misdemeanor of driving on a sus-
  pended license. A search incident to the arrest yielded crack cocaine,
  and Moore was tried on drug charges. The trial court declined to
  suppress the evidence on Fourth Amendment grounds. Moore was
  convicted. Ultimately, the Virginia Supreme Court reversed, reason-
  ing that the search violated the Fourth Amendment because the ar-
  resting officers should have issued a citation under state law, and the
  Fourth Amendment does not permit search incident to citation.
Held: The police did not violate the Fourth Amendment when they
 made an arrest that was based on probable cause but prohibited by
 state law, or when they performed a search incident to the arrest.
 Pp. 3–13.
    (a) Because the founding era’s statutes and common law do not
 support Moore’s view that the Fourth Amendment was intended to
 incorporate statutes, this is “not a case in which the claimant can
 point to a ‘clear answer [that] existed in 1791 and has been generally
 adhered to by the traditions of our society ever since,’ ” Atwater v.
 Lago Vista, 532 U. S. 318, 345. Pp. 3–5.
    (b) Where history provides no conclusive answer, this Court has
 analyzed a search or seizure in light of traditional reasonableness
 standards “by assessing, on the one hand, the degree to which it in-
 trudes upon an individual’s privacy and, on the other, the degree to
 which it is needed for the promotion of legitimate governmental in-
 terests.” Wyoming v. Houghton, 526 U. S. 295, 300. Applying that
 methodology, this Court has held that when an officer has probable
 cause to believe a person committed even a minor crime, the arrest is
 constitutionally reasonable. Atwater, supra, at 354. This Court’s de-
 cisions counsel against changing the calculus when a State chooses to
2                          VIRGINIA v. MOORE

                                  Syllabus

    protect privacy beyond the level required by the Fourth Amendment.
    See, e.g., Whren v. United States, 517 U. S. 35. United States v. Di
    Re, 332 U. S. 581, distinguished. Pp. 6–8.
       (c) The Court adheres to this approach because an arrest based on
    probable cause serves interests that justify seizure. Arrest ensures
    that a suspect appears to answer charges and does not continue a
    crime, and it safeguards evidence and enables officers to conduct an
    in-custody investigation. A State’s choice of a more restrictive
    search-and-seizure policy does not render less restrictive ones unrea-
    sonable, and hence unconstitutional. While States are free to require
    their officers to engage in nuanced determinations of the need for ar-
    rest as a matter of their own law, the Fourth Amendment should re-
    flect administrable bright-line rules. Incorporating state arrest rules
    into the Constitution would make Fourth Amendment protections as
    complex as the underlying state law, and variable from place to place
    and time to time. Pp. 8–11.
       (d) The Court rejects Moore’s argument that even if the Constitu-
    tion allowed his arrest, it did not allow the arresting officers to
    search him. Officers may perform searches incident to constitution-
    ally permissible arrests in order to ensure their safety and safeguard
    evidence. United States v. Robinson, 414 U. S. 218. While officers is-
    suing citations do not face the same danger, and thus do not have the
    same authority to search, Knowles v. Iowa, 525 U. S. 113, the officers
    arrested Moore, and therefore faced the risks that are “an adequate
    basis for treating all custodial arrests alike for purposes of search
    justification,” Robinson, supra, at 235. Pp. 11–13.
272 Va. 717, 636 S. E. 2d 395, reversed and remanded.

   SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and STEVENS, KENNEDY, SOUTER, THOMAS, BREYER, and ALITO, JJ.,
joined. GINSBURG, J., filed an opinion concurring in the judgment.
                        Cite as: 553 U. S. ____ (2008)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 06–1082
                                   _________________


    VIRGINIA, PETITIONER v. DAVID LEE MOORE
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       VIRGINIA

                                 [April 23, 2008] 


  JUSTICE SCALIA delivered the opinion of the Court.
  We consider whether a police officer violates the Fourth
Amendment by making an arrest based on probable cause
but prohibited by state law.
                             I
  On February 20, 2003, two City of Portsmouth police
officers stopped a car driven by David Lee Moore. They
had heard over the police radio that a person known as
“Chubs” was driving with a suspended license, and one of
the officers knew Moore by that nickname. The officers
determined that Moore’s license was in fact suspended,
and arrested him for the misdemeanor of driving on a
suspended license, which is punishable under Virginia law
by a year in jail and a $2,500 fine, Va. Code Ann. §§18.2–
11, 18.2–272, 46.2–301(C) (Lexis 2005). The officers sub-
sequently searched Moore and found that he was carrying
16 grams of crack cocaine and $516 in cash.1 See 272 Va.
——————
  1 The arresting officers did not perform a search incident to arrest

immediately upon taking Moore into custody, because each of them
mistakenly believed that the other had done so. App. 54–55; see also
id., at 33–34. They realized their mistake after arriving with Moore at
Moore’s hotel room, which they had obtained his consent to search, and
2                       VIRGINIA v. MOORE

                         Opinion of the Court

717, 636 S. E. 2d 395 (2006); 45 Va. App. 146, 609 S. E. 2d
74 (2005).
   Under state law, the officers should have issued Moore a
summons instead of arresting him. Driving on a sus-
pended license, like some other misdemeanors, is not an
arrestable offense except as to those who “fail or refuse to
discontinue” the violation, and those whom the officer
reasonably believes to be likely to disregard a summons,
or likely to harm themselves or others. Va. Code Ann.
§19.2–74 (Lexis 2004). The intermediate appellate court
found none of these circumstances applicable, and Virginia
did not appeal that determination. See 272 Va., at 720,
n. 3, 636 S. E. 2d, at 396–397, n. 3. Virginia also permits
arrest for driving on a suspended license in jurisdictions
where “prior general approval has been granted by order
of the general district court,” Va. Code Ann. §46.2–936;
Virginia has never claimed such approval was in effect in
the county where Moore was arrested.
   Moore was charged with possessing cocaine with the
intent to distribute it in violation of Virginia law. He filed
a pretrial motion to suppress the evidence from the arrest
search. Virginia law does not, as a general matter, require
suppression of evidence obtained in violation of state law.
See 45 Va. App., at 160–162, 609 S. E. 2d, at 82 (Annun-
ziata, J., dissenting). Moore argued, however, that sup-
pression was required by the Fourth Amendment. The
trial court denied the motion, and after a bench trial found
Moore guilty of the drug charge and sentenced him to a 5-
year prison term, with one year and six months of the
sentence suspended. The conviction was reversed by a
panel of Virginia’s intermediate court on Fourth Amend-
ment grounds, id., at 149–150, 609 S. E. 2d, at 76, rein-
stated by the intermediate court sitting en banc, 47 Va.
—————— 

they searched his person there. Ibid. Moore does not contend that this

delay violated the Fourth Amendment. 

                    Cite as: 553 U. S. ____ (2008)                   3

                         Opinion of the Court

App. 55, 622 S. E. 2d 253 (2005), and finally reversed
again by the Virginia Supreme Court, 272 Va., at 725, 636
S. E. 2d, at 400. The Court reasoned that since the arrest-
ing officers should have issued Moore a citation under
state law, and the Fourth Amendment does not permit
search incident to citation, the arrest search violated the
Fourth Amendment. Ibid. We granted certiorari. 551
U. S. ___ (2007).
                            II
  The Fourth Amendment protects “against unreasonable
searches and seizures” of (among other things) the person.
In determining whether a search or seizure is unreason-
able, we begin with history. We look to the statutes and
common law of the founding era to determine the norms
that the Fourth Amendment was meant to preserve. See
Wyoming v. Houghton, 526 U. S. 295, 299 (1999); Wilson v.
Arkansas, 514 U. S. 927, 931 (1995).
  We are aware of no historical indication that those who
ratified the Fourth Amendment understood it as a redun-
dant guarantee of whatever limits on search and seizure
legislatures might have enacted.2 The immediate object of
the Fourth Amendment was to prohibit the general war-
——————
   2 Atwater v. Lago Vista, 532 U. S. 318 (2001), rejected the view

JUSTICE GINSBURG advances that the legality of arrests for misdemean-
ors involving no breach of the peace “depended on statutory authoriza-
tion.” Post, at 1, n. 1 (opinion concurring in judgment). Atwater cited
both of the sources on which JUSTICE GINSBURG relies for a limited view
of common-law arrest authority, but it also identified and quoted
numerous treatises that described common-law authority to arrest for
minor misdemeanors without limitation to cases in which a statute
authorized arrest. See 532 U. S., at 330–332. Atwater noted that many
statutes authorized arrest for misdemeanors other than breaches of the
peace, but it concluded that the view of arrest authority as extending
beyond breaches of the peace also reflected judge-made common law.
Id., at 330–331. Particularly since Atwater considered the materials on
which JUSTICE GINSBURG relies, we see no reason to revisit the case’s
conclusion.
4                         VIRGINIA v. MOORE

                           Opinion of the Court

rants and writs of assistance that English judges had
employed against the colonists, Boyd v. United States, 116
U. S. 616, 624–627 (1886); Payton v. New York, 445 U. S.
573, 583–584 (1980). That suggests, if anything, that
founding-era citizens were skeptical of using the rules for
search and seizure set by government actors as the index
of reasonableness.
   Joseph Story, among others, saw the Fourth Amend-
ment as “little more than the affirmance of a great consti-
tutional doctrine of the common law,” 3 Commentaries on
the Constitution of the United States §1895, p. 748 (1833),
which Story defined in opposition to statutes, see Codifica-
tion of the Common Law in The Miscellaneous Writings of
Joseph Story 698, 699, 701 (W. Story ed. 1852). No early
case or commentary, to our knowledge, suggested the
Amendment was intended to incorporate subsequently
enacted statutes. None of the early Fourth Amendment
cases that scholars have identified sought to base a consti-
tutional claim on a violation of a state or federal statute
concerning arrest. See Davies, Recovering the Original
Fourth Amendment, 98 Mich. L. Rev. 547, 613–614
(1999);3 see also T. Taylor, Two Studies in Constitutional
Interpretation 44–45 (1969).
   Of course such a claim would not have been available
against state officers, since the Fourth Amendment was a
restriction only upon federal power, see Barron ex rel.
Tiernan v. Mayor of Baltimore, 7 Pet. 243 (1833). But
early Congresses tied the arrest authority of federal offi-
cers to state laws of arrest. See United States v. Di Re,
——————
  3 Of the early cases that Davies collects, see 98 Mich. L. Rev., at 613,

n. 174; id., at 614, n. 175, the lone decision to treat statutes as relevant
to the Fourth Amendment’s contours simply applied the principle that
statutes enacted in the years immediately before or after the Amend-
ment was adopted shed light on what citizens at the time of the Amend-
ment’s enactment saw as reasonable. Boyd v. United States, 116 U. S.
616, 622–623 (1886).
                     Cite as: 553 U. S. ____ (2008)                 5

                         Opinion of the Court

332 U. S. 581, 589 (1948); United States v. Watson, 423
U. S. 411, 420 (1976). Moreover, even though several
state constitutions also prohibited unreasonable searches
and seizures, citizens who claimed officers had violated
state restrictions on arrest did not claim that the viola-
tions also ran afoul of the state constitutions.4 The appar-
ent absence of such litigation is particularly striking in
light of the fact that searches incident to warrantless
arrests (which is to say arrests in which the officer was
not insulated from private suit) were, as one commentator
has put it, “taken for granted” at the founding, Taylor,
supra, at 45, as were warrantless arrests themselves,
Amar, Fourth Amendment First Principles, 107 Harv.
L. Rev. 757, 764 (1994).
   There are a number of possible explanations of why such
constitutional claims were not raised. Davies, for exam-
ple, argues that actions taken in violation of state law
could not qualify as state action subject to Fourth
Amendment constraints. 98 Mich. L. Rev., at 660–663.
Be that as it may, as Moore adduces neither case law nor
commentaries to support his view that the Fourth
Amendment was intended to incorporate statutes, this is
“not a case in which the claimant can point to ‘a clear
answer [that] existed in 1791 and has been generally
adhered to by the traditions of our society ever since.’ ”
Atwater v. Lago Vista, 532 U. S. 318, 345 (2001) (altera-
tion in original).


——————
  4 Massachusetts,  for example, had a state constitutional provision
paralleling the Fourth Amendment, but the litigants in the earliest
cases we have identified claiming violations of arrest statutes in the
Commonwealth did not argue that their arrests violated the Common-
wealth’s Constitution. See Brock v. Stimson, 108 Mass. 520 (1871);
Phillips v. Fadden, 125 Mass. 198 (1878); see also Tubbs v. Tukey, 57
Mass. 438 (1849) (asserting violation of state common law concerning
arrest but not asserting violation of state constitution).
6                   VIRGINIA v. MOORE

                     Opinion of the Court

                             III
                              A
  When history has not provided a conclusive answer, we
have analyzed a search or seizure in light of traditional
standards of reasonableness “by assessing, on the one
hand, the degree to which it intrudes upon an individual’s
privacy and, on the other, the degree to which it is needed
for the promotion of legitimate governmental interests.”
Houghton, 526 U. S., at 300; see also Atwater, 532 U. S., at
346. That methodology provides no support for Moore’s
Fourth Amendment claim. In a long line of cases, we have
said that when an officer has probable cause to believe a
person committed even a minor crime in his presence, the
balancing of private and public interests is not in doubt.
The arrest is constitutionally reasonable. Id., at 354; see
also, e.g., Devenpeck v. Alford, 543 U. S. 146, 152 (2004);
Gerstein v. Pugh, 420 U. S. 103, 111 (1975); Brinegar v.
United States, 338 U. S. 160, 164, 170, 175–176 (1949).
  Our decisions counsel against changing this calculus
when a State chooses to protect privacy beyond the level
that the Fourth Amendment requires. We have treated
additional protections exclusively as matters of state law.
In Cooper v. California, 386 U. S. 58 (1967), we reversed a
state court that had held the search of a seized vehicle to
be in violation of the Fourth Amendment because state
law did not explicitly authorize the search. We concluded
that whether state law authorized the search was irrele-
vant. States, we said, remained free “to impose higher
standards on searches and seizures than required by the
Federal Constitution,” id., at 62, but regardless of state
rules, police could search a lawfully seized vehicle as a
matter of federal constitutional law.
  In California v. Greenwood, 486 U. S. 35 (1988), we held
that search of an individual’s garbage forbidden by Cali-
fornia’s Constitution was not forbidden by the Fourth
Amendment. “[W]hether or not a search is reasonable
                 Cite as: 553 U. S. ____ (2008)           7

                     Opinion of the Court

within the meaning of the Fourth Amendment,” we said,
has never “depend[ed] on the law of the particular State in
which the search occurs.” Id., at 43. While “[i]ndividual
States may surely construe their own constitutions as
imposing more stringent constraints on police conduct
than does the Federal Constitution,” ibid., state law did
not alter the content of the Fourth Amendment.
   We have applied the same principle in the seizure con-
text. Whren v. United States, 517 U. S. 806 (1996), held
that police officers had acted reasonably in stopping a car,
even though their action violated regulations limiting the
authority of plainclothes officers in unmarked vehicles.
We thought it obvious that the Fourth Amendment’s
meaning did not change with local law enforcement prac-
tices—even practices set by rule. While those practices
“vary from place to place and from time to time,” Fourth
Amendment protections are not “so variable” and cannot
“be made to turn upon such trivialities.” Id., at 815.
   Some decisions earlier than these excluded evidence
obtained in violation of state law, but those decisions
rested on our supervisory power over the federal courts,
rather than the Constitution. In Di Re, 332 U. S. 581,
federal and state officers collaborated in an investigation
that led to an arrest for a federal crime. The Government
argued that the legality of an arrest for a federal offense
was a matter of federal law. Id., at 589. We concluded,
however, that since Congress had provided that arrests
with warrants must be made in accordance with state law,
the legality of arrests without warrants should also be
judged according to state-law standards. Id., at 589–590.
This was plainly not a rule we derived from the Constitu-
tion, however, because we repeatedly invited Congress to
change it by statute—saying that state law governs the
validity of a warrantless arrest “in [the] absence of an
applicable federal statute,” id., at 589, and that the Di Re
rule applies “except in those cases where Congress has
8                    VIRGINIA v. MOORE

                     Opinion of the Court

enacted a federal rule,” id., at 589–590.
  Later decisions did not expand the rule of Di Re. John-
son v. United States, 333 U. S. 10 (1948), relied on Di Re to
suppress evidence obtained under circumstances identical
in relevant respects to those in that case. See 333 U. S., at
12, 15, n. 5. And Michigan v. DeFillippo, 443 U. S. 31
(1979), upheld a warrantless arrest in a case where com-
pliance with state law was not at issue. While our opinion
said that “[w]hether an officer is authorized to make an
arrest ordinarily depends, in the first instance, on state
law,” it also said that a warrantless arrest satisfies the
Constitution so long as the officer has “probable cause to
believe that the suspect has committed or is committing a
crime.” Id., at 36. We need not pick and choose among the
dicta: Neither Di Re nor the cases following it held that
violations of state arrest law are also violations of the
Fourth Amendment, and our more recent decisions, dis-
cussed above, have indicated that when States go above
the Fourth Amendment minimum, the Constitution’s
protections concerning search and seizure remain the
same.
                            B
   We are convinced that the approach of our prior cases is
correct, because an arrest based on probable cause serves
interests that have long been seen as sufficient to justify
the seizure. Whren, supra, at 817; Atwater, supra, at 354.
Arrest ensures that a suspect appears to answer charges
and does not continue a crime, and it safeguards evidence
and enables officers to conduct an in-custody investiga-
tion. See W. LaFave, Arrest: The Decision to Take a
Suspect into Custody 177–202 (1965).
   Moore argues that a State has no interest in arrest
when it has a policy against arresting for certain crimes.
That is not so, because arrest will still ensure a suspect’s
appearance at trial, prevent him from continuing his
                 Cite as: 553 U. S. ____ (2008)            9

                     Opinion of the Court

offense, and enable officers to investigate the incident
more thoroughly. State arrest restrictions are more accu-
rately characterized as showing that the State values its
interests in forgoing arrests more highly than its interests
in making them, see, e.g., Dept. of Justice, National Insti-
tute of Justice, D. Whitcomb, B. Lewin, & M. Levine,
Issues and Practices: Citation Release 17 (Mar. 1984)
(describing cost savings as a principal benefit of citation-
release ordinances); or as showing that the State places a
higher premium on privacy than the Fourth Amendment
requires. A State is free to prefer one search-and-seizure
policy among the range of constitutionally permissible
options, but its choice of a more restrictive option does not
render the less restrictive ones unreasonable, and hence
unconstitutional.
   If we concluded otherwise, we would often frustrate
rather than further state policy. Virginia chooses to pro-
tect individual privacy and dignity more than the Fourth
Amendment requires, but it also chooses not to attach to
violations of its arrest rules the potent remedies that
federal courts have applied to Fourth Amendment viola-
tions. Virginia does not, for example, ordinarily exclude
from criminal trials evidence obtained in violation of its
statutes. See 45 Va. App., at 161, 609 S. E. 2d, at 82
(Annunziata, J., dissenting) (citing Janis v. Common-
wealth, 22 Va. App. 646, 651, 472 S. E. 2d 649, 652
(1996)). Moore would allow Virginia to accord enhanced
protection against arrest only on pain of accompanying
that protection with federal remedies for Fourth Amend-
ment violations, which often include the exclusionary rule.
States unwilling to lose control over the remedy would
have to abandon restrictions on arrest altogether. This is
an odd consequence of a provision designed to protect
against searches and seizures.
   Even if we thought that state law changed the nature of
the Commonwealth’s interests for purposes of the Fourth
10                   VIRGINIA v. MOORE

                     Opinion of the Court

Amendment, we would adhere to the probable-cause stan-
dard. In determining what is reasonable under the Fourth
Amendment, we have given great weight to the “essential
interest in readily administrable rules.” Atwater, 532
U. S., at 347. In Atwater, we acknowledged that nuanced
judgments about the need for warrantless arrest were
desirable, but we nonetheless declined to limit to felonies
and disturbances of the peace the Fourth Amendment rule
allowing arrest based on probable cause to believe a law
has been broken in the presence of the arresting officer.
Id., at 346–347. The rule extends even to minor misde-
meanors, we concluded, because of the need for a bright-
line constitutional standard. If the constitutionality of
arrest for minor offenses turned in part on inquiries as to
risk of flight and danger of repetition, officers might be
deterred from making legitimate arrests. Id., at 351. We
found little to justify this cost, because there was no “epi-
demic of unnecessary minor-offense arrests,” and hence “a
dearth of horribles demanding redress.” Id., at 353.
   Incorporating state-law arrest limitations into the Con-
stitution would produce a constitutional regime no less
vague and unpredictable than the one we rejected in
Atwater. The constitutional standard would be only as
easy to apply as the underlying state law, and state law
can be complicated indeed. The Virginia statute in this
case, for example, calls on law enforcement officers to
weigh just the sort of case-specific factors that Atwater
said would deter legitimate arrests if made part of the
constitutional inquiry. It would authorize arrest if a
misdemeanor suspect fails or refuses to discontinue the
unlawful act, or if the officer believes the suspect to be
likely to disregard a summons. Va. Code Ann. §19.2–
74.A.1. Atwater specifically noted the “extremely poor
judgment” displayed in arresting a local resident who
would “almost certainly” have discontinued the offense
and who had “no place to hide and no incentive to flee.”
                  Cite as: 553 U. S. ____ (2008)           11

                      Opinion of the Court

532 U. S., at 346–347. It nonetheless declined to make
those considerations part of the constitutional calculus.
Atwater differs from this case in only one significant re-
spect: It considered (and rejected) federal constitutional
remedies for all minor-misdemeanor arrests; Moore seeks
them in only that subset of minor-misdemeanor arrests in
which there is the least to be gained—that is, where the
State has already acted to constrain officers’ discretion
and prevent abuse. Here we confront fewer horribles than
in Atwater, and less of a need for redress.
   Finally, linking Fourth Amendment protections to state
law would cause them to “vary from place to place and
from time to time,” Whren, 517 U. S., at 815. Even at the
same place and time, the Fourth Amendment’s protections
might vary if federal officers were not subject to the same
statutory constraints as state officers. In Elkins v. United
States, 364 U. S. 206, 210–212 (1960), we noted the practi-
cal difficulties posed by the “silver-platter doctrine,” which
had imposed more stringent limitations on federal officers
than on state police acting independent of them. It would
be strange to construe a constitutional provision that did
not apply to the States at all when it was adopted to now
restrict state officers more than federal officers, solely
because the States have passed search-and-seizure laws
that are the prerogative of independent sovereigns.
   We conclude that warrantless arrests for crimes com-
mitted in the presence of an arresting officer are reason-
able under the Constitution, and that while States are free
to regulate such arrests however they desire, state restric-
tions do not alter the Fourth Amendment’s protections.
                              IV
  Moore argues that even if the Constitution allowed his
arrest, it did not allow the arresting officers to search him.
We have recognized, however, that officers may perform
searches incident to constitutionally permissible arrests in
12                   VIRGINIA v. MOORE

                      Opinion of the Court

order to ensure their safety and safeguard evidence.
United States v. Robinson, 414 U. S. 218 (1973). We have
described this rule as covering any “lawful arrest,” id., at
235, with constitutional law as the reference point. That
is to say, we have equated a lawful arrest with an arrest
based on probable cause: “A custodial arrest of a suspect
based on probable cause is a reasonable intrusion under
the Fourth Amendment; that intrusion being lawful, a
search incident to the arrest requires no additional justifi-
cation.” Ibid. (emphasis added). Moore correctly notes
that several important state-court decisions have defined
the lawfulness of arrest in terms of compliance with state
law. See Brief for Respondent 32–33 (citing People v.
Chiagles, 237 N. Y. 193, 197, 142 N. E. 583, 584 (1923);
People v. DeFore, 242 N. Y. 13, 17–19, 150 N. E. 585, 586
(1926)). But it is not surprising that States have used
“lawful” as shorthand for compliance with state law, while
our constitutional decision in Robinson used “lawful” as
shorthand for compliance with constitutional constraints.
   The interests justifying search are present whenever an
officer makes an arrest. A search enables officers to safe-
guard evidence, and, most critically, to ensure their safety
during “the extended exposure which follows the taking of
a suspect into custody and transporting him to the police
station.” Robinson, supra, at 234–235. Officers issuing
citations do not face the same danger, and we therefore
held in Knowles v. Iowa, 525 U. S. 113 (1998), that they do
not have the same authority to search. We cannot agree
with the Virginia Supreme Court that Knowles controls
here. The state officers arrested Moore, and therefore
faced the risks that are “an adequate basis for treating all
custodial arrests alike for purposes of search justification.”
Robinson, supra, at 235.
   The Virginia Supreme Court may have concluded that
Knowles required the exclusion of evidence seized from
Moore because, under state law, the officers who arrested
                 Cite as: 553 U. S. ____ (2008)           13

                     Opinion of the Court

Moore should have issued him a citation instead. This
argument might have force if the Constitution forbade
Moore’s arrest, because we have sometimes excluded
evidence obtained through unconstitutional methods in
order to deter constitutional violations. See Wong Sun v.
United States, 371 U. S. 471, 484–485, 488 (1963). But the
arrest rules that the officers violated were those of state
law alone, and as we have just concluded, it is not the
province of the Fourth Amendment to enforce state law.
That Amendment does not require the exclusion of evi-
dence obtained from a constitutionally permissible arrest.
                        *    *    *
  We reaffirm against a novel challenge what we have
signaled for more than half a century. When officers have
probable cause to believe that a person has committed a
crime in their presence, the Fourth Amendment permits
them to make an arrest, and to search the suspect in order
to safeguard evidence and ensure their own safety. The
judgment of the Supreme Court of Virginia is reversed,
and the case is remanded for further proceedings not
inconsistent with this opinion.
                                           It is so ordered.
                         Cite as: 553 U. S. ____ (2008)                              1

                    GINSBURG, J., concurring in judgment

      NOTICE: This opinion is subject to formal revision before publication in the
      preliminary print of the United States Reports. Readers are requested to
      notify the Reporter of Decisions, Supreme Court of the United States, Wash-
      ington, D. C. 20543, of any typographical or other formal errors, in order
      that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                    No. 06–1082
                                    _________________


     VIRGINIA, PETITIONER v. DAVID LEE MOORE
     ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                        VIRGINIA

                                  [April 23, 2008] 


  JUSTICE GINSBURG, concurring in the judgment.
  I find in the historical record more support for Moore’s
position than the Court does, ante, at 3–5.1 Further, our
decision in United States v. Di Re, 332 U. S. 581, 587–590
(1948), requiring suppression of evidence gained in a
search incident to an unlawful arrest, seems to me pinned
——————
  1 Under the common law prevailing at the end of the 19th century, it

appears that arrests for minor misdemeanors, typically involving no
breach of the peace, depended on statutory authorization. See Wilgus,
Arrest Without a Warrant, 22 Mich. L. Rev. 541, 674 (1924) (“Neither
[an officer] nor [a citizen], without statutory authority, may arrest [a
defendant] for . . . a misdemeanor which is not a [breach of the peace]”
(emphasis added)); 9 Halsbury, Laws of England §§608, 611–612, 615
(1909). See also Atwater v. Lago Vista, 532 U. S. 318, 342–345 (2001)
(noting 19th-century decisions upholding statutes extending war-
rantless arrest authority to misdemeanors, other than breaches of the
peace, committed in a police officer’s presence); Wilgus, supra, at 551
(warrantless misdemeanor arrests “made under authority of a statute
must conform strictly to its provisions; otherwise they will not be valid,
and the one arresting becomes a trespasser”).
  Noting colonial hostility to general warrants and writs of assistance,
the Court observes that “founding-era citizens were skeptical of using
the rules for search and seizure set by government actors as the index
of reasonableness.” Ante, at 4. The practices resisted by the citizenry,
however, served to invade the people’s privacy, not to shield it.
2                        VIRGINIA v. MOORE

                 GINSBURG, J., concurring in judgment

to the Fourth Amendment and not to our “supervisory
power,” ante, at 7.2 And I am aware of no “long line of
cases” holding that, regardless of state law, probable cause
renders every warrantless arrest for crimes committed in
the presence of an arresting officer “constitutionally rea-
sonable,” ante, at 6.3
  I agree with the Court’s conclusion and its reasoning,
however, to this extent. In line with the Court’s decision
——————
   2 The Court attributes Di Re’s suppression ruling to our “supervisory

power,” not to “a rule we derived from the Constitution.” Ante, at 7.
Justice Jackson, author of Di Re, however, did not mention “supervisory
power,” placed the decision in a Fourth Amendment context, see 332
U. S., at 585, and ended with a reminder that “our Constitution [places]
obstacles in the way of a too permeating police surveillance,” id., at 595.
The Di Re opinion, I recognize, is somewhat difficult to parse. Allied to
Di Re’s Fourth Amendment instruction, the Court announced a choice-
of-law rule not derived from the Constitution: When a state officer
makes a warrantless arrest for a federal crime, federal arrest law
governs the legality of the arrest; but absent a federal statute in point,
“the law of the state where an arrest without warrant takes place
determines its validity.” Id., at 588–589.
   3 Demonstrative of the “long line,” the Court lists Atwater, 532 U. S.,

at 354, Devenpeck v. Alford, 543 U. S. 146, 152 (2004), Brinegar v.
United States, 338 U. S. 160, 164, 170, 175–176 (1949), and Gerstein v.
Pugh, 420 U. S. 103, 111 (1975). Ante, at 6. But in all of these cases,
unlike Moore’s case, state law authorized the arrests. The warrantless
misdemeanor arrest in Atwater was authorized by Tex. Transp. Code
Ann. §543.001 (West 1999). See 532 U. S., at 323. The warrantless
misdemeanor arrest in Devenpeck was authorized by Wash. Rev. Code
Ann. §10.31.100 (Michie 1997). In Brinegar, whether the warrantless
arrest was for a misdemeanor or a felony, it was authorized by state
law. See Okla. Stat., Tit. 22, §196 (1941). Gerstein involved a challenge
to the State’s preliminary hearing procedures, not to the validity of a
particular arrest. See 420 U. S., at 105. The record does not indicate
whether the respondents’ offenses were committed in the officer’s
presence or whether the arrests were made under warrant. See id.,
at 105, n. 1. But it does indicate that the crimes involved were serious
felonies, see ibid., and state law authorized arrest without warrant
when “[a] felony has been committed and [the officer] reasonably
believes that the [apprehended] person committed it,” Fla. Stat. Ann.
§901.15(2) (West 1973).
                 Cite as: 553 U. S. ____ (2008)            3

              GINSBURG, J., concurring in judgment

in Atwater v. Lago Vista, 532 U. S. 318, 354 (2001), Vir-
ginia could have made driving on a suspended license an
arrestable offense. The Commonwealth chose not to do so.
Moore asks us to credit Virginia law on a police officer’s
arrest authority, but only in part. He emphasizes Vir-
ginia’s classification of driving on a suspended license as a
nonarrestable misdemeanor. Moore would have us ignore,
however, the limited consequences Virginia attaches to a
police officer’s failure to follow the Commonwealth’s sum-
mons-only instruction. For such an infraction, the officer
may be disciplined and the person arrested may bring a
tort suit against the officer. But Virginia law does not
demand the suppression of evidence seized by an officer
who arrests when he should have issued a summons.
  The Fourth Amendment, today’s decision holds, does not
put States to an all-or-nothing choice in this regard. A
State may accord protection against arrest beyond what
the Fourth Amendment requires, yet restrict the remedies
available when police deny to persons they apprehend the
extra protection state law orders. See ante, at 9. Because
I agree that the arrest and search Moore challenges vio-
lated Virginia law, but did not violate the Fourth Amend-
ment, I join the Court’s judgment.

```

---

## GROUP: _overhaul2/lake/cases/Walder v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Walder v. United States"
type: case
citation: "347 U.S. 62 (1954)"
parallel_cite: "74 S. Ct. 354; 98 L. Ed. 2d 503; 98 L. Ed. 503"
neutral_cite: 1954 U.S. LEXIS 2453
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1954
date_decided: 1954-02-01
docket: 121
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1954-02-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Walder v. United States
  varies_by_point: false
  scope_note: "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105188/walder-v-united-states/"
  cluster_id: 105188
  opinion_id: 105188
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor (impeachment exception)"
related: ["[[Weeks v. United States]]", "[[Agnello v. United States]]", "[[United States v. Havens]]", "[[James v. Illinois]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "impeachment-exception", "credibility"]
holding: "Illegally seized evidence, though inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping affirmative assertion beyond a denial of the charged offense; the exclusionary rule is a shield, not a license to commit perjury."
lake:
  record_id: Walder v. United States
  status: verified
  projected_at: 2026-07-09
---

# Walder v. United States

*347 U.S. 62 (1954)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In 1950 Walder was indicted for narcotics possession; a heroin capsule was suppressed as the product of an unlawful search, and that case was dismissed. In 1952 he was indicted for four other narcotics transactions. Testifying in his own defense, he volunteered on direct examination that he had never sold or possessed any narcotics in his life. On cross-examination the Government, over objection, asked about the 1950 capsule and then introduced the previously suppressed evidence — but solely to impeach his credibility, under a limiting instruction. He was convicted.

## Issue
Whether evidence obtained by an unlawful search and seizure, inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping claim that he never possessed narcotics.

## Rule
Yes. "It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the Government's possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the *Weeks* doctrine would be a perversion of the Fourth Amendment." — 347 U.S. at 65. ^pin-65

A defendant "must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it"; but "there is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government's disability to challenge his credibility." — [*Id.*](https://www.courtlistener.com/opinion/105188/walder-v-united-states/#:~:text=must%20be%20free%20to%20deny) ^pin-65b

## Application
Walder "went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics." That volunteered, perjurious assertion on his own direct examination opened the door, so the Government could use the unlawfully seized heroin to impeach his credibility — but only for impeachment, not as substantive proof of the charged offenses (hence the limiting instruction). The Court "sharply contrasted" this with *[[Agnello v. United States]]*, where the Government, after the defendant said nothing about the evidence on direct, tried to smuggle suppressed evidence in through its own cross-examination — which is impermissible.

## Conclusion
Because Walder himself opened the door with a sweeping false claim, the impeachment use of the suppressed evidence was proper; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Walder* is the origin of the **impeachment exception** to the exclusionary rule, built on [[Weeks v. United States]] and distinguishing [[Agnello v. United States]]. It was later extended to statements taken in violation of *[[Miranda v. Arizona|Miranda]]* ([[Harris v. New York]]) and to cross-examination reasonably suggested by direct in [[United States v. Havens]], and cabined to the defendant himself (no other defense witnesses) in [[James v. Illinois]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor (impeachment exception)*

## Sources
- *Walder v. United States*, 347 U.S. 62 (1954) — https://www.courtlistener.com/opinion/105188/walder-v-united-states/ — pinpoints: 65, 66.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bb1c5c6f0bdff8c7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Walder v. United States"}, "payload": {"all": [{"cite": "347 U.S. 62", "page": "62", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "347"}, {"cite": "74 S. Ct. 354", "page": "354", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "74"}, {"cite": "98 L. Ed. 2d 503", "page": "503", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "1954 U.S. LEXIS 2453", "page": "2453", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1954"}, {"cite": "98 L. Ed. 503", "page": "503", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}], "display": "347 U.S. 62", "official": {"cite": "347 U.S. 62", "page": "62", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "347"}, "official_selection_present": true, "record_id": "Walder v. United States"}}
{"assertion_id": "15418bf0c618a725", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-65b", "record_id": "Walder v. United States"}, "payload": {"fragment": "#:~:text=must%20be%20free%20to%20deny", "page": null, "pin_id": "pin-65b", "pinpoint_status": "star-verified", "quote": "must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it", "quote_fidelity": "matched", "record_id": "Walder v. United States", "star_marker": "65"}}
{"assertion_id": "de12792edb1d1f53", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-65", "record_id": "Walder v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-65", "pinpoint_status": "slip-only", "quote": "--- # Walder v. United States *347 U.S. 62 (1954)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In 1950 Walder was indicted for narcotics possession; a heroin capsule was suppressed as the product of an unlawful search, and that case was dismissed. In 1952 he was indicted for four other narcotics transactions. Testifying in his own defense, he volunteered on direct examination that he had never sold or possessed any narcotics in his life. On cross-examination the Government, over objection, asked about the 1950 capsule and then introduced the previously suppressed evidence — but solely to impeach his credibility, under a limiting instruction. He was convicted. ## Issue Whether evidence obtained by an unlawful search and seizure, inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping claim that he never possessed narcotics. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Walder v. United States", "star_marker": null}}
{"assertion_id": "40a7f55f7d984c52", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Walder v. United States"}, "payload": {"as_of_content": "1954-02-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Walder v. United States", "scope_note": "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois).", "varies_by_point": false}}
```

### lake record — Walder v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Walder v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Walder v. United States",
    "case_name_short": "Walder",
    "case_name_full": "Walder v. United States",
    "input_case_name": "Walder v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1954-02-01",
    "year": 1954,
    "docket": "121",
    "cluster_id": 105188,
    "lead_opinion_id": 105188,
    "sibling_ids": [
      105188
    ],
    "absolute_url": "/opinion/105188/walder-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "347 U.S. 62",
      "volume": "347",
      "reporter": "U.S.",
      "page": "62",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "74 S. Ct. 354",
        "volume": "74",
        "reporter": "S. Ct.",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 2d 503",
        "volume": "98",
        "reporter": "L. Ed. 2d",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 503",
        "volume": "98",
        "reporter": "L. Ed.",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1954 U.S. LEXIS 2453",
        "volume": "1954",
        "reporter": "U.S. LEXIS",
        "page": "2453",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "347 U.S. 62",
        "volume": "347",
        "reporter": "U.S.",
        "page": "62",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 S. Ct. 354",
        "volume": "74",
        "reporter": "S. Ct.",
        "page": "354",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 2d 503",
        "volume": "98",
        "reporter": "L. Ed. 2d",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1954 U.S. LEXIS 2453",
        "volume": "1954",
        "reporter": "U.S. LEXIS",
        "page": "2453",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 L. Ed. 503",
        "volume": "98",
        "reporter": "L. Ed.",
        "page": "503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "347 U.S. 62",
    "official_selection": {
      "court_class": "scotus",
      "selected": "347 U.S. 62",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-65",
      "page": null,
      "quote": "--- # Walder v. United States *347 U.S. 62 (1954)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In 1950 Walder was indicted for narcotics possession; a heroin capsule was suppressed as the product of an unlawful search, and that case was dismissed. In 1952 he was indicted for four other narcotics transactions. Testifying in his own defense, he volunteered on direct examination that he had never sold or possessed any narcotics in his life. On cross-examination the Government, over objection, asked about the 1950 capsule and then introduced the previously suppressed evidence \u2014 but solely to impeach his credibility, under a limiting instruction. He was convicted. ## Issue Whether evidence obtained by an unlawful search and seizure, inadmissible in the prosecution's case in chief, may be used to impeach a defendant who, on his own direct examination, makes a sweeping claim that he never possessed narcotics. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-65b",
      "page": null,
      "quote": "must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it",
      "star_marker": "65",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6673,
      "fragment": "#:~:text=must%20be%20free%20to%20deny",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1954-02-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Walder v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the impeachment exception; remains good law and was extended (Harris v. New York, Havens) and cabined (James v. Illinois).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "People v. Hopson",
          "cluster_id": 4405826,
          "cite": [
            "219 Cal. Rptr. 3d 717",
            "396 P.3d 1054",
            "3 Cal. 5th 424",
            "2017 WL 2837126",
            "2017 Cal. LEXIS 4894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Yoirlan Rojas",
          "cluster_id": 3217322,
          "cite": [
            "826 F.3d 1126",
            "100 Fed. R. Serv. 871",
            "2016 U.S. App. LEXIS 11688",
            "2016 WL 3513902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Richard Leroy Parker",
          "cluster_id": 4472828,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Agim Baftiri",
          "cluster_id": 774763,
          "cite": [
            "263 F.3d 856",
            "2001 U.S. App. LEXIS 19334",
            "2001 WL 987524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Paul A. Bilzerian",
          "cluster_id": 556608,
          "cite": [
            "926 F.2d 1285",
            "31 Fed. R. Serv. 1185",
            "1991 U.S. App. LEXIS 66",
            "1991 WL 430"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Jacobs",
          "cluster_id": 6049311,
          "cite": [
            "149 A.D.2d 112",
            "544 N.Y.S.2d 1011",
            "1989 N.Y. App. Div. LEXIS 10994"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. David Alexander, United States of America v. Everton Knight",
          "cluster_id": 518838,
          "cite": [
            "868 F.2d 492",
            "1989 U.S. App. LEXIS 1989",
            "1989 WL 13234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. May",
          "cluster_id": 1454345,
          "cite": [
            "748 P.2d 307",
            "44 Cal. 3d 309",
            "243 Cal. Rptr. 369",
            "1988 Cal. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane1_negative"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. New York",
          "cluster_id": 108272,
          "cite": [
            "28 L. Ed. 2d 1",
            "91 S. Ct. 643",
            "401 U.S. 222",
            "1971 U.S. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Hass",
          "cluster_id": 109221,
          "cite": [
            "43 L. Ed. 2d 570",
            "95 S. Ct. 1215",
            "420 U.S. 714",
            "1975 U.S. LEXIS 5"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Anderson",
          "cluster_id": 110298,
          "cite": [
            "65 L. Ed. 2d 86",
            "100 S. Ct. 2124",
            "447 U.S. 231",
            "1980 U.S. LEXIS 131"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Whiteside",
          "cluster_id": 111603,
          "cite": [
            "89 L. Ed. 2d 123",
            "106 S. Ct. 988",
            "475 U.S. 157",
            "1986 U.S. LEXIS 8",
            "54 U.S.L.W. 4194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. United States",
          "cluster_id": 105661,
          "cite": [
            "2 L. Ed. 2d 589",
            "78 S. Ct. 622",
            "356 U.S. 148",
            "1958 U.S. LEXIS 1286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ceccolini",
          "cluster_id": 109816,
          "cite": [
            "55 L. Ed. 2d 268",
            "98 S. Ct. 1054",
            "435 U.S. 268",
            "1978 U.S. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Havens",
          "cluster_id": 110267,
          "cite": [
            "64 L. Ed. 2d 559",
            "100 S. Ct. 1912",
            "446 U.S. 620",
            "1980 U.S. LEXIS 103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
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
        "journal_ref": "Walder v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris W. Gordon v. United States",
          "cluster_id": 277392,
          "cite": [
            "383 F.2d 936"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walder v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105188) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MjY3Mjk2MDAwMDAmcz0xNzMzMTc5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105188%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(105188)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTcmcz01NjMyMDEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105188%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105188)",
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
    "complete_query": "cites:(105188)",
    "indexed_citing_opinions": 638,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105188,
        "count": 638,
        "count_source": "search"
      }
    ],
    "citation_count": 1024,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/walder-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MTM2NjImcz00Njk2MTE1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105188%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105188,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 104607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105188,
        "cited_id": 230984,
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
    "date_created": "2026-07-06T03:56:50Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:59:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:57:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Walder v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b136-12">
  Mr. Justice Frankfurter
 </author>
<p id="A0M">
  delivered the opinion of the Court.
 </p>
<p id="b136-13">
  In May 1950, petitioner was indicted in the United States District Court for the Western District of Missouri for purchasing and possessing one grain of heroin. Claiming that the heroin capsule had been obtained through an unlawful search and seizure, petitioner moved
  <span citation-index="1" class="star-pagination" label="63"> 
   *63
   </span>
  to suppress it. The motion was granted, and shortly thereafter, on the Government’s motion, the case against petitioner was dismissed.
 </p>
<p id="b137-5">
  In January of 1952, petitioner was again indicted, this time for four other illicit transactions in narcotics. The Government’s case consisted principally of the testimony of two drug addicts who claimed to have procured the illicit stuff from petitioner under the direction of federal agents. The only witness for the defense was the defendant himself, petitioner here. He denied any narcotics dealings with the two Government informers and attributed the testimony against him to personal hostility.
 </p>
<p id="b137-6">
  Early on his direct examination petitioner testified as follows:
 </p>
<blockquote id="b137-7">
  “Q. Now, first, Mr. Walder, before we go further in your testimony, I want to you [sic] tell the Court and jury whether, not referring to these informers in this case, but whether you have ever sold any narcotics to anyone.
 </blockquote>
<blockquote id="b137-8">
  “A. I have never sold any narcotics to anyone in my life.
 </blockquote>
<blockquote id="b137-9">
  “Q. Have you ever had any narcotics in your possession, other than what may have been given to you by a physician for an ailment?
 </blockquote>
<blockquote id="b137-10">
  “A. No.
 </blockquote>
<blockquote id="b137-11">
  “Q. Now, I will ask you one more thing. Have you ever handed or given any narcotics to anyone as a gift or in any other manner without the receipt of any money or any other compensation?
 </blockquote>
<blockquote id="b137-12">
  “A. I have not.
 </blockquote>
<blockquote id="b137-13">
  “Q. Have you ever even acted as, say, have you acted as a conduit for the purpose of handling what you knew to be a narcotic from one person to another?
 </blockquote>
<blockquote id="b137-14">
  “A. No, sir.”
 </blockquote>
<p id="b138-4">
<span citation-index="1" class="star-pagination" label="64"> 
   *64
   </span>
  On cross-examination, in response to a question by Government counsel making reference to this direct testimony, petitioner reiterated his assertion that he had never purchased, sold or possessed any narcotics. Over the defendant’s objection, the Government then questioned him about the heroin capsule unlawfully seized from his home in his presence back in February 1950. The defendant stoutly denied that any narcotics were taken from him at that time.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The Government then put on the stand one of the officers who had participated in the unlawful search and seizure and also the chemist who had analyzed the heroin capsule there seized. The trial judge admitted this evidence, but carefully charged the jury that it was not to be used to determine whether the defendant had committed the crimes here charged, but solely for the purpose of impeaching the defendant’s credibility. The defendant was convicted, and the Court of Appeals for the Eighth Circuit affirmed, one judge dissenting. <span class="citation" data-id="9443562"><a href="/opinion/230984/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">201 F. 2d 715</a></span>. The question which divided that court, and the sole issue here, is whether the defendant’s assertion on direct examination that he had never possessed any narcotics opened the door, solely for the purpose of attacking the defendant’s credibility, to evidence of the heroin unlawfully seized in connection with the earlier proceeding. Because this question presents a novel aspect of the scope of the doctrine of
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./345/992/">345 U. S. 992</a></span>.
 </p>
<p id="b138-5">
  The Government cannot violate the Fourth Amendment
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  — in the only way in which the Government can do anything, namely through its agents — and use the fruits
  <span citation-index="1" class="star-pagination" label="65"> 
   *65
   </span>
  of such unlawful conduct to secure a conviction.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States, supra.
  </em>
  Nor can the Government make indirect use of such evidence for its case,
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, or support a conviction on evidence obtained through leads from the unlawfully obtained evidence, cf.
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>. All these methods are outlawed, and convictions obtained by means of them are invalidated, because they encourage the kind of society that is obnoxious to free men.
 </p>
<p id="b139-5">
  It is one thing to say that the Government cannot make an affirmative use of evidence unlawfully obtained. It is quite another to say that the defendant can turn the illegal method by which evidence in the' Government’s possession was obtained to his own advantage, and provide himself with a shield against contradiction of his untruths. Such an extension of the
  <em>
   <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>
  </em>
  doctrine would be a perversion of the Fourth Amendment.
 </p>
<p id="b139-6">
  Take the present situation. Of his own accord, the defendant went beyond a mere denial of complicity in the crimes of which he was charged and made the sweeping claim that he had never dealt in or possessed any narcotics. Of course, the Constitution guarantees a defendant the fullest opportunity to meet the accusation against him. He must be free to deny all the elements of the case against him without thereby giving leave to the Government to introduce by way of rebuttal evidence illegally secured by it, and therefore not available for its case in chief. Beyond that, however, there is hardly justification for letting the defendant affirmatively resort to perjurious testimony in reliance on the Government’s disability to challenge his credibility.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="Azo">
<span citation-index="1" class="star-pagination" label="66"> 
   *66
   </span>
  The situation here involved is to be sharply contrasted with that presented by
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>. There the Government, after having failed in its efforts to introduce the tainted evidence in its case in chief, tried to smuggle it in on cross-examination by asking the accused the broad question “Did you ever see narcotics before?”
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  After eliciting the expected denial, it sought to introduce evidence of narcotics located in the defendant’s home by means of an unlawful search and seizure, in order to discredit the defendant. In holding that the Government could no more work in this evidence on cross-examination than it could in its case in chief, the Court foreshadowed, perhaps unwittingly, the result we reach today:
 </p>
<blockquote id="b140-4">
  “And the contention that the evidence of the search and seizure was admissible in rebuttal is without merit. In his direct examination, Agnello was not asked and did not testify concerning the can of cocaine. In cross-examination, in answer to a question permitted over his objection, he said he had never seen it. He did nothing to waive his constitutional protection or to justify cross-examination in respect of the evidence claimed to have been obtained by the search. . . .” <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#35" aria-description="Citation for case: Agnello v. United States">269 U. S., at 35</a></span>.
 </blockquote>
<p id="b140-5">
  The judgment is
 </p>
<p id="b140-6">
<em>
   Affirmed.
  </em>
</p>
<judges id="b140-7">
  Mr. Justice Black and Mr. Justice Douglas dissent.
 </judges>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b138-6">
   This denial squarely contradicted the affidavit filed by the defendant in the earlier proceeding, in connection with his motion under Rule 41 (e) to suppress the evidence unlawfully seized.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b138-7">
   “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . .”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b139-7">
   Cf.
   <em>
    Michelson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">335 U. S. 469</a></span>, 479: “The price a defendant must pay for attempting to prove his good name is to throw open the entire subject which the law has kept closed for his
   <span citation-index="1" class="star-pagination" label="66"> 
    *66
    </span>
   benefit and to make himself vulnerable where the law otherwise shields him.”
  </p>
<p id="b140-9">
   The underlying rationale of the
   <em>
    <span class="citation" data-id="9420246"><a href="/opinion/104607/michelson-v-united-states/" aria-description="Citation for case: Michelson v. United States">Michelson</a></span>
   </em>
   case also disposes of the evidentiary question raised by petitioner, to wit, “whether defendant’s actual guilt under a former indictment which was dismissed may be proved by extrinsic evidence introduced to impeach him in a prosecution for a subsequent offense.”
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b140-10">
<em>
</em>
   Transcript of Record, p. 476,
   <em>
    Agnello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Walter v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Walter v. United States"
type: case
citation: "447 U.S. 649 (1980)"
parallel_cite: "100 S. Ct. 2395; 65 L. Ed. 2d 410"
neutral_cite: 1980 U.S. LEXIS 135
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-20
docket: 79-67
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Walter v. United States
  varies_by_point: false
  scope_note: "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110314/walter-v-united-states/"
  cluster_id: 110314
  opinion_id: 9428007
  identity_checked: true
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — scope limit"
related: ["[[United States v. Jacobsen]]"]
aliases: ["Walter v. US"]
tags: ["case", "fourth-amendment", "private-search", "scope", "search-definition"]
holding: "The government may not exceed the scope of a prior private search; the FBI's screening of films the private party had not viewed was a separate, unlawful search."
lake:
  record_id: Walter v. United States
  status: verified
  projected_at: 2026-07-09
---

# Walter v. United States

*447 U.S. 649 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Twelve sealed packages of 8-millimeter films were shipped by private carrier but misdelivered to L'Eggs Products, Inc. Employees opened the packages and found individual film boxes bearing suggestive drawings and explicit written descriptions of the contents; one employee opened a box and tried, without success, to view the film by holding it to the light. The employees turned the shipment over to the FBI, which — without a warrant — projected the films and used them to obtain obscenity convictions. The defendants moved to suppress.

## Issue
Whether the FBI's warrantless screening of films that a private party had received and inspected (but had not actually viewed) was a search requiring a warrant, or was instead authorized by the prior private search.

## Rule
The Government's later examination is measured against the scope of the prior private search: "the Government may not exceed the scope of the private search unless it has the right to make an independent search." — 447 U.S. at 657. ^pin-657

Projecting the films went beyond what the private party had done: "The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search." — *Id.* And that separate, warrantless viewing was unreasonable: "the unauthorized exhibition of the films constituted an unreasonable invasion of their owner's constitutionally protected interest in privacy. It was a search; there was no warrant; the owner had not consented; and there were no exigent circumstances." — [*Id.* at 654](https://www.courtlistener.com/opinion/110314/walter-v-united-states/#:~:text=The%20projection%20of%20the%20films). ^pin-654

## Application
On these facts the private parties had opened the packages and examined the boxes — including the suggestive labels — but had not actually viewed the films. The FBI therefore could lawfully do what the private parties had already done, but projecting the films revealed contents the private search had not exposed and significantly expanded that search. Because the labels supplied probable cause and a warrant could easily have been obtained, the warrantless screening — unsupported by consent or [[Exigent Circumstances and Hot Pursuit|exigency]] — was an unreasonable search, and the films had to be suppressed.

## Conclusion
The warrantless projection of the films exceeded the scope of the private search and was an unreasonable search; the convictions were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (judgment announced in a Stevens plurality).
- No negative treatment. The private-search principle — that government agents may not exceed the scope of an earlier private search without independent justification — was adopted and refined by [[United States v. Jacobsen]] (1984), which framed the inquiry as whether the official conduct exceeded the scope of the private search.

## Appears on
- [[Private and Foreign Searches]] — *Key — scope limit*

## Sources
- *Walter v. United States*, 447 U.S. 649 (1980) — https://www.courtlistener.com/opinion/110314/walter-v-united-states/ — pinpoints: 654, 657.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b8460077a1da25d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Walter v. United States"}, "payload": {"all": [{"cite": "447 U.S. 649", "page": "649", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "447"}, {"cite": "100 S. Ct. 2395", "page": "2395", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 410", "page": "410", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 135", "page": "135", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "447 U.S. 649", "official": {"cite": "447 U.S. 649", "page": "649", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "447"}, "official_selection_present": true, "record_id": "Walter v. United States"}}
{"assertion_id": "4e957c991aec8af8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-654", "record_id": "Walter v. United States"}, "payload": {"fragment": "#:~:text=The%20projection%20of%20the%20films", "page": null, "pin_id": "pin-654", "pinpoint_status": "star-verified", "quote": "The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search.", "quote_fidelity": "matched", "record_id": "Walter v. United States", "star_marker": "657"}}
{"assertion_id": "70747561b8153f9e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-657", "record_id": "Walter v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-657", "pinpoint_status": "slip-only", "quote": "--- # Walter v. United States *447 U.S. 649 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Twelve sealed packages of 8-millimeter films were shipped by private carrier but misdelivered to L'Eggs Products, Inc. Employees opened the packages and found individual film boxes bearing suggestive drawings and explicit written descriptions of the contents; one employee opened a box and tried, without success, to view the film by holding it to the light. The employees turned the shipment over to the FBI, which — without a warrant — projected the films and used them to obtain obscenity convictions. The defendants moved to suppress. ## Issue Whether the FBI's warrantless screening of films that a private party had received and inspected (but had not actually viewed) was a search requiring a warrant, or was instead authorized by the prior private search. ## Rule The Government's later examination is measured against the scope of the prior private search:", "quote_fidelity": "mismatch", "record_id": "Walter v. United States", "star_marker": null}}
{"assertion_id": "0f2e8db1e57132dc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Walter v. United States"}, "payload": {"as_of_content": "1980-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Walter v. United States", "scope_note": "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law.", "varies_by_point": false}}
```

### lake record — Walter v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Walter v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Walter v. United States",
    "case_name_short": "Walter",
    "case_name_full": "Walter v. United States",
    "input_case_name": "Walter v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-20",
    "year": 1980,
    "docket": "79-67",
    "cluster_id": 110314,
    "lead_opinion_id": 9428007,
    "sibling_ids": [
      110314,
      9428007,
      9428008,
      9428009
    ],
    "absolute_url": "/opinion/110314/walter-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "447 U.S. 649",
      "volume": "447",
      "reporter": "U.S.",
      "page": "649",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2395",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 410",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 135",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "447 U.S. 649",
        "volume": "447",
        "reporter": "U.S.",
        "page": "649",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2395",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 410",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "410",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 135",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "135",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "447 U.S. 649",
    "official_selection": {
      "court_class": "scotus",
      "selected": "447 U.S. 649",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-657",
      "page": null,
      "quote": "--- # Walter v. United States *447 U.S. 649 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Twelve sealed packages of 8-millimeter films were shipped by private carrier but misdelivered to L'Eggs Products, Inc. Employees opened the packages and found individual film boxes bearing suggestive drawings and explicit written descriptions of the contents; one employee opened a box and tried, without success, to view the film by holding it to the light. The employees turned the shipment over to the FBI, which \u2014 without a warrant \u2014 projected the films and used them to obtain obscenity convictions. The defendants moved to suppress. ## Issue Whether the FBI's warrantless screening of films that a private party had received and inspected (but had not actually viewed) was a search requiring a warrant, or was instead authorized by the prior private search. ## Rule The Government's later examination is measured against the scope of the prior private search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-654",
      "page": null,
      "quote": "The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search.",
      "star_marker": "657",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11610,
      "fragment": "#:~:text=The%20projection%20of%20the%20films",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Walter v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality (Stevens, J., announcing the judgment); private-search principle later adopted and refined in United States v. Jacobsen (1984); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Tyrone Davis",
          "cluster_id": 3212685,
          "cite": [
            "825 F.3d 1014",
            "2016 U.S. App. LEXIS 10661",
            "2016 WL 3245043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bruce",
          "cluster_id": 2803531,
          "cite": [
            "412 S.C. 504",
            "772 S.E.2d 753",
            "2015 S.C. LEXIS 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenschke v. State",
          "cluster_id": 1795866,
          "cite": [
            "116 S.W.3d 173",
            "2003 WL 21696528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Adderson Jarrett",
          "cluster_id": 782958,
          "cite": [
            "338 F.3d 339",
            "61 Fed. R. Serv. 1530",
            "2003 U.S. App. LEXIS 15017",
            "2003 WL 21744122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dawson v. State",
          "cluster_id": 1635091,
          "cite": [
            "106 S.W.3d 388",
            "2003 WL 21027168"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane1_negative"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kraft",
          "cluster_id": 2590211,
          "cite": [
            "5 P.3d 68",
            "99 Cal. Rptr. 2d 1",
            "23 Cal. 4th 978",
            "2000 Daily Journal DAR 8825",
            "2000 Cal. Daily Op. Serv. 6660",
            "2000 Cal. LEXIS 5822"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoker v. State",
          "cluster_id": 2464243,
          "cite": [
            "788 S.W.2d 1",
            "1989 Tex. Crim. App. LEXIS 167",
            "1989 WL 107536"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brimage v. State",
          "cluster_id": 2417512,
          "cite": [
            "918 S.W.2d 466",
            "1996 Tex. Crim. App. LEXIS 5",
            "1994 WL 511395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Belton",
          "cluster_id": 5685394,
          "cite": [
            "55 N.Y.2d 49",
            "432 N.E.2d 745",
            "447 N.Y.S.2d 873",
            "1982 N.Y. LEXIS 3067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
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
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Wuagneux",
          "cluster_id": 406519,
          "cite": [
            "683 F.2d 1343",
            "1982 U.S. App. LEXIS 16435",
            "11 Fed. R. Serv. 334"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bittaker",
          "cluster_id": 1179588,
          "cite": [
            "774 P.2d 659",
            "48 Cal. 3d 1046",
            "259 Cal. Rptr. 630",
            "1989 Cal. LEXIS 1462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Amador Rodriguez Chaidez, A/K/A Rodriguez Amador Chaidez and Amador Rodriguez",
          "cluster_id": 543654,
          "cite": [
            "906 F.2d 377",
            "1990 U.S. App. LEXIS 11006",
            "1990 WL 88172"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karyn Rene Walther, United States of America v. Graciela Barba-Barba",
          "cluster_id": 391946,
          "cite": [
            "652 F.2d 788",
            "1981 U.S. App. LEXIS 20059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Reid",
          "cluster_id": 2348536,
          "cite": [
            "811 A.2d 530",
            "571 Pa. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Elkins Carol Elkins, United States of America v. Carol Elkins James Elkins",
          "cluster_id": 778775,
          "cite": [
            "300 F.3d 638"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Christine, Perry Grabosky",
          "cluster_id": 408050,
          "cite": [
            "687 F.2d 749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell B. Allen",
          "cluster_id": 735355,
          "cite": [
            "106 F.3d 695",
            "1997 U.S. App. LEXIS 2129",
            "1997 WL 49827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miles v. State",
          "cluster_id": 1872653,
          "cite": [
            "241 S.W.3d 28",
            "2007 Tex. Crim. App. LEXIS 1456",
            "2007 WL 3010420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Finley",
          "cluster_id": 47945,
          "cite": [
            "477 F.3d 250",
            "72 Fed. R. Serv. 377",
            "2007 U.S. App. LEXIS 1806",
            "2007 WL 196531"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yong Hyon Kim",
          "cluster_id": 672873,
          "cite": [
            "27 F.3d 947",
            "1994 U.S. App. LEXIS 16298",
            "1994 WL 287235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conley v. State",
          "cluster_id": 1849099,
          "cite": [
            "790 So. 2d 773",
            "2001 WL 393827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Walter v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDE1MzcyODAwMDAwJnM9MjMwNTQ4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkmcz02NjE4MDYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
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
    "complete_query": "cites:(110314 OR 9428007 OR 9428008 OR 9428009)",
    "indexed_citing_opinions": 532,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110314,
        "count": 447,
        "count_source": "search"
      },
      {
        "opinion_id": 9428007,
        "count": 95,
        "count_source": "search"
      },
      {
        "opinion_id": 9428008,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428009,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 793,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/walter-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MTA1NTMmcz05NDIxNzEzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110314+OR+9428007+OR+9428008+OR+9428009%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110314,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 344085,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 363614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 365664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110314,
        "cited_id": 1484849,
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
    "date_created": "2026-07-06T03:59:28Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:05:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:59:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Walter v. United States

```
<opinion type="majority">
<author id="b693-7">Mr. Justice Stevens</author>
<p id="Auj">announced the judgment of the Court and delivered an opinion, in which Mr. Justice Stewart joined.</p>
<p id="b693-8">Having lawfully acquired possession of a dozen cartons of motion pictures, law enforcement officers viewed several reels of 8-millimeter film on a Government projector. Labels on the individual film boxes indicated that they contained obscene pictures. The question is whether the Fourth Amendment required the agents to obtain a warrant before they screened the films.</p>
<p id="b693-9">Only a few of the bizarre facts need be recounted. On September 25, 1975, 12 large, securely sealed packages containing 871 boxes of 8-millimeter film depicting homosexual activities were shipped by private carrier from St. Petersburg, Fla., to Atlanta, Ga. The shipment was addressed to “Leggs, Inc.,” <footnotemark>1</footnotemark> but was mistakenly delivered to a substation in the suburbs of Atlanta, where “L’Eggs Products, Inc.,” regularly received deliveries. Employees of the latter company opened <page-number citation-index="1" label="652">*652</page-number>each of the packages, finding the individual boxes of film. They examined the boxes, on one side of which were suggestive drawings, and on the other were explicit descriptions of the contents. One employee opened one or two of the boxes, and attempted without success to view portions of the film by holding it up to the light.<footnotemark>2</footnotemark> Shortly thereafter, they called a Federal Bureau of Investigation agent who picked up the packages on October 1,1975.</p>
<p id="b694-5">Thereafter, without making any effort to obtain a warrant or to communicate with the consignor or the consignee of the shipment, FBI agents viewed the films with a projector. The record does not indicate exactly when they viewed the films, but at least one of them was not screened until more than two months after the FBI had taken possession of the shipment.<footnotemark>3</footnotemark></p>
<p id="b694-6">On April 6, 1977, petitioners were indicted on obscenity charges relating to the interstate transportation of 5 of the 871 films in the shipment. A motion to suppress and return the films was denied, and petitioners were convicted on multiple counts of violating <span class="citation no-link">18 U. S. C. §§ 371</span>, 1462, and 1465. Over Judge Wisdom’s dissent, the Court of Appeals for the Fifth Circuit affirmed, <span class="citation" data-id="9465518"><a href="/opinion/363614/united-states-v-arthur-randall-sanders-jr-gulf-coast-news-agency-inc/" aria-description="Citation for case: United States v. Arthur Randall Sanders, Jr., Gulf Coast...">592 F. 2d 788</a></span>, and rehearing was denied, <span class="citation" data-id="365664"><a href="/opinion/365664/united-states-v-arthur-randall-sanders-jr-gulf-coast-news-agency-inc/" aria-description="Citation for case: United States v. Arthur Randall Sanders, Jr., Gulf Coast...">597 F. 2d 63</a></span> (1979). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/914/">444 U. S. 914</a></span>,<footnotemark>4</footnotemark> and now reverse.</p>
<p id="b695-4"><page-number citation-index="1" label="653">*653</page-number>In his concurrence in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#569" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 569</a></span>, Mr. Justice Stewart expressed the opinion that the war-rantless projection of motion picture films was an unconstitutional invasion of the privacy of the owner of the films. After noting that the agents in that case were lawfully present in the defendant’s home pursuant to a warrant to search for wagering paraphernalia, Mr. Justice Stewart wrote:</p>
<blockquote id="b695-5">“This is not a case where agents in the course of a lawful search came upon contraband, criminal activity, or criminal evidence in plain view. For the record makes clear that the contents of the films could not be determined by mere inspection. . . . After finding them, the agents spent some 50 minutes exhibiting them by means of the appellant’s projector in another upstairs room. Only then did the agents return downstairs and arrest the appellant.</blockquote>
<blockquote id="b695-6">“Even in the much-criticized case of <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>, the Court emphasized that 'exploratory searches . . . cannot be undertaken by officers with or without a warrant.’ <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#62" aria-description="Citation for case: United States v. Rabinowitz"><em>Id., </em>at 62</a></span>. This record presents a bald violation of that basic constitutional rule. To condone what happened here is to invite a government official to use a seemingly precise and legal warrant only as a ticket to get into a man’s home, and, once inside, to launch forth upon unconfined searches and indiscriminate seizures as if armed with all the unbridled and illegal power of a general warrant.</blockquote>
<blockquote id="b695-7">“Because the films were seized in violation of the Fourth and Fourteenth Amendments, they were inadmis<page-number citation-index="1" label="654">*654</page-number>sible in evidence at the appellant’s trial.” <em>Id., </em>at 571-572 (footnote omitted).</blockquote>
<p id="b696-5">Even though the cases before us involve no invasion of the privacy of the home, and notwithstanding that the nature of the contents of these films was indicated by descriptive material on their individual containers, we are nevertheless persuaded that the unauthorized exhibition of the films constituted an unreasonable invasion of their owner’s constitutionally protected interest in privacy. It was a search; there was no warrant; the owner had not consented; and there were no exigent circumstances.</p>
<p id="b696-6">It is perfectly obvious that the agents’ reason for viewing the films was to determine whether their owner was guilty of a federal offense. To be sure, the labels on the film boxes gave them probable cause to believe that the films were obscene and that their shipment in interstate commerce had offended the federal criminal code. But the labels were not sufficient to support a conviction and were not mentioned in the indictment. Further investigation — that is to say, a search of the contents of the films — was necessary in order to obtain the evidence which was to be used at trial.</p>
<p id="b696-7">The fact that FBI agents were lawfully in possession of the boxes of film did not give them authority to search their contents. Ever since 1878 when Mr. Justice Field’s opinion for the Court in <em>Ex parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727</a></span>, established that sealed packages in the mail cannot be opened without a warrant, it has been settled that an officer’s authority to possess a package is distinct from his authority to examine its contents.<footnotemark>5</footnotemark> See <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#758" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 758</a></span>; <em>United </em><page-number citation-index="1" label="655">*655</page-number><em>States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 10</a></span>. When the contents of the package are books or other materials arguably protected by the First Amendment, and when the basis for the seizure is disapproval of the message contained therein, it is especially important that this requirement be scrupulously observed.<footnotemark>6</footnotemark></p>
<p id="b698-4"><page-number citation-index="1" label="656">*656</page-number>Nor does the fact that the packages and one or more of the boxes had been opened by a private party before they were acquired by the FBI excuse the failure to obtain a search warrant. It has, of course, been settled since <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465</a></span>, that a wrongful search or seizure conducted by a private party does not violate the Fourth Amendment and that such private wrongdoing does not deprive the government of the right to use evidence that it has acquired lawfully. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487-490</a></span>. In these cases there was nothing wrongful about the Government’s acquisition of the packages or its examination of their contents to the extent that they had already been examined by third parties. Since that examination had uncovered the labels, and since the labels established probable cause to believe the films were obscene, the Government argues that the limited private search justified an unlimited official search. That argument must fail, whether we view the official search as an expansion of the private search or as an independent search supported by its own probable cause.</p>
<p id="b698-5">When an official search is properly authorized — whether by consent or by the issuance of a valid warrant — the scope of the search is limited by the terms of its authorization.<footnotemark>7</footnotemark> Consent <page-number citation-index="1" label="657">*657</page-number>to search a garage would not implicitly authorize a search of an adjoining house; a warrant to search for a stolen refrigerator would not authorize the opening of desk drawers. Because “indiscriminate searches and seizures conducted under the authority of ‘general warrants’ were the immediate evils that motivated the framing and adoption of the Fourth Amendment,” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 583</a></span>, that Amendment requires that the scope of every authorized search be particularly described.<footnotemark>8</footnotemark></p>
<p id="b699-5">If a properly authorized official search is limited by the particular terms of its authorization, at least the same kind of strict limitation must be applied to any official use of a private party’s invasion of another person’s privacy. Even though some circumstances — for example, if the results of the private search are in plain view when materials are turned over to the Government — may justify the Government’s reexamination of the materials, surely the Government may not exceed the scope of the private search unless it has the right to make an independent search. In these cases, the private party had not actually viewed the films. Prior to the Government screening, one could only draw inferences about what was on the films.<footnotemark>9</footnotemark> The projection of the films was a significant expansion of the search that had been conducted previously by a private party and therefore must be characterized as a separate search. That separate search was not supported by any exigency, or by a warrant even though one could have easily been obtained.<footnotemark>10</footnotemark></p>
<p id="b700-4"><page-number citation-index="1" label="658">*658</page-number>The Government claims, however, that because the packages had been opened by a private party, thereby exposing the descriptive labels on the boxes, petitioners no longer had any reasonable expectation of privacy in the films, and that the warrantless screening therefore did not invade any privacy interest protected by the Fourth Amendment. But petitioners expected no one except the intended recipient either to open the 12 packages or to project the films. The 12 cartons were securely wrapped and sealed, with no labels or markings to indicate the character of their contents.<footnotemark>11</footnotemark> There is no reason why the consignor of such a shipment would have any lesser expectation of privacy than the consignor of an ordinary locked suitcase.<footnotemark>12</footnotemark> The fact that the cartons were unexpectedly <page-number citation-index="1" label="659">*659</page-number>opened by a third party before the shipment was delivered to its intended consignee does not alter the consignor’s legitimate expectation of privacy. The private search merely frustrated that expectation in part.<footnotemark>13</footnotemark> It did not simply strip the remaining unfrustrated portion of that expectation of all Fourth Amendment protection.<footnotemark>14</footnotemark> Since the additional search conducted by the FBI — the screening of the films — was not supported by any justification, it violated that Amendment.</p>
<p id="b701-5">We therefore conclude that the rationale of Mr. Justice Stewart’s concurrence in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557</a></span>, <page-number citation-index="1" label="660">*660</page-number>is applicable to these cases and that it requires that the judgments of the Court of Appeals be reversed.</p>
<p id="b702-5">
<em>It is so ordered.</em>
</p>
<p id="b702-6">Mr. Justice Marshall concurs in the judgment.</p>
<footnote label="1">
<p id="b693-10"> There was no “Leggs, Inc.” “Leggs” was the nickname of a woman employed by one of petitioners’ companies. The packages indicated that the intended recipient would pick them up and pay for them at the carrier’s terminal in Atlanta.</p>
</footnote>
<footnote label="2">
<p id="b694-7"> Each reel was eight millimeters in width. Petitioner Walter informs us that, excluding three millimeters for sprocketing and one millimeter for the border, the film itself is only four millimeters wide. Brief for Petitioner in No. 79-67, p. 30, n. 8. Since the scenes depicted within the frame are necessarily even more minute, it is easy to understand why such films cannot be examined successfully with the naked eye.</p>
</footnote>
<footnote label="3">
<p id="b694-8"> The FBI had meanwhile received no request from the consignee or the consignor of the films for their return, but the agents had been told by employees of L’Eggs Products, Inc., that inquiries had been made as to their whereabouts.</p>
</footnote>
<footnote label="4">
<p id="b694-9"> The petition for certiorari in No. 79-67 presented 10 separate questions, and the petition in No. 79-148 presented 5 separate questions. Except <page-number citation-index="1" label="653">*653</page-number>with respect to the issues discussed in the text, we have determined that certiorari was improvidently granted. We therefore dismiss as to the other questions that have been briefed and argued. For purposes of decision, we accept the Government’s argument that the delivery of the films to the FBI by a third party was not a “seizure” subject to the warrant requirement of the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b696-8"><em> </em>“In th[e] enforcement [of regulations as to what may be transported in the mails], a distinction is to be made between different kinds of mail matter, — between what is intended to be kept free from inspection, such as letters, and sealed packages subject to letter postage; and what is open to inspection, such as newspapers, magazines, pamphlets, and other printed matter, purposely left in a condition to be examined. Letters and <page-number citation-index="1" label="655">*655</page-number>sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s own household. No law of Congress can place in the hands of officials connected with the postal service any authority to invade the secrecy of letters and such sealed packages in the mail; and all regulations adopted as to mail matter of this kind must be in subordination to the great principle embodied in the fourth amendment of the Constitution.” <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#732" aria-description="Citation for case: Ex Parte Jackson">96 U. S., at 732-733</a></span>.</p>
<p id="A6H">And later in his opinion, Mr. Justice Field again noted that “regulations excluding matter from the mail cannot be enforced in a way which would require or permit an examination into letters, or sealed packages subject to letter postage, without warrant, issued upon oath or affirmation, in the search for prohibited matter. . . .” <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#735" aria-description="Citation for case: Ex Parte Jackson"><em>Id., </em>at 735</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b697-10"> “This is the history which prompted the Court less than four years ago to remark that ‘[t]he use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new.’ <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, at 724</a></span>. ‘This history was, of course, part of the intellectual matrix within which our constitutional fabric was shaped. The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression.’ <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#729" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Id., </em>at 729</a></span>. As MR. Justice Douglas has put it, ‘The commands of our First Amendment (as well as the prohibitions of the Fourth and the Fifth) reflect the teachings of <em>Entick </em>v. <em>Carrington, </em>[19 How. St. Tr. 1029 (1765)]. These three amendments are indeed closely related, safeguarding not only privacy and protection against self-incrimination <page-number citation-index="1" label="656">*656</page-number>but "conscience and human dignity and freedom of expression as well.”’ <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#376" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 376</a></span> (dissenting opinion).</p>
<blockquote id="b698-7">“In short, what this history indispensably teaches is that the constitutional requirement that warrants must particularly describe the ‘things to be seized’ is to be accorded the most scrupulous exactitude when the ‘things’ are books, and the basis for their seizure is the ideas which they contain.” <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#484" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 484-485</a></span>.</blockquote>
<p id="b698-11">See also <em>Roaden </em>v. <em>Kentucky, </em><span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#501" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 501</a></span>. Although there were 871 reels of film in the shipment, there were only 25 different titles. Since only five of the titles were used as a basis for prosecution, it may be presumed that the other films were not obscene.</p>
</footnote>
<footnote label="7">
<p id="b698-12"> “The requirement that warrants shall particularly describe the things to be seized makes general searches under them impossible and prevents the seizure of one thing under a warrant describing another.” <em>Manon </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b699-6"> The Warrant Clause of the Fourth Amendment expressly provides that no warrant may issue except those “particularly describing the place to be searched, and the persons or things to be seized.”</p>
</footnote>
<footnote label="9">
<p id="pACiC"> Since the viewing was first done by the Government when it screened the films with a projector, we have no occasion to decide whether the Government would have been required to obtain a warrant had the private party been the first to view them.</p>
</footnote>
<footnote label="10">
<p id="b699-8"> The fact that the labels on the boxes established probable cause to believe the films were obscene clearly cannot excuse the failure to obtain a <page-number citation-index="1" label="658">*658</page-number>warrant; for if probable cause dispensed with the necessity of a warrant, one would never be needed.</p>
<p id="A-ej">Contrary to the dissent, <em>post, </em>at 665-666, n. 3, there were no impracticalities in these cases that would vitiate the warrant requirement. The inability to serve a warrant on the owner of property to be searched does not make execution of the warrant unlawful. See ALI, Model Code of Pre-Arraignment Procedure §220.3 (4) (Prop. Off. Draft 1975). Obviously, such inability does not render a warrant unnecessary under the Fourth Amendment. Nor is it clear in these cases that it would have been impossible to serve petitioners with a search warrant had the FBI made any effort to find them prior to screening the films. See n. 3, <em>supra.</em></p>
</footnote>
<footnote label="11">
<p id="b700-7"> For the same reason, one may not deem petitioners to have consented to the screening merely because the labels on the unexposed boxes were explicit.</p>
<p id="b700-8">Nor can petitioners’ failure to make a more prompt claim to the Gov- ■ emment for return of the films be fairly regarded as an abandonment of their interest in preserving the privacy of the shipment. As subsequent events have demonstrated, such a request could reasonably be expected to precipitate criminal proceedings. We cannot equate an unwillingness to invite a criminal prosecution with a voluntary abandonment of any interest in the contents of the cartons. In any event, the record in these cases does indicate that the defendants made a number of attempts to locate the films before they were examined by the FBI agents.</p>
</footnote>
<footnote label="12">
<p id="b700-9"> The consignor’s expectation of privacy in the contents of a carton delivered to a private carrier must be measured by the condition of the package at the time it was shipped unless there is reason to assume that <page-number citation-index="1" label="659">*659</page-number>it would be opened before it arrived at its destination. Thus, for example, if a gun case is delivered to a carrier, there could then be no expectation that the contents would remain private, cf. <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753, 764-765, n. 13</a></span>; but if the gun case were enclosed in a locked suitcase, the shipper would surely expect that the privacy of its contents would be respected.</p>
<p id="AHbV">The dissent asserts, <em>post, </em>at 665, that “[a]ny subjective expectation of privacy on the part of petitioners was undone ... by their own actions and the private search.” But it is difficult to understand how petitioners’ subjective expectation of privacy could have been altered in any way by subsequent events of which they were obviously unaware.</p>
</footnote>
<footnote label="13">
<p id="b701-8"> A partial invasion of privacy cannot automatically justify a total invasion. As Learned Hand noted in a somewhat different context: “It is true that when one has been arrested in his home or his office, his privacy has already been invaded; but that interest, though lost, is altogether separate from the interest in protecting his papers from indiscriminate rummage, even though both are customarily grouped together as parts of the 'right of privacy.’ ” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9638337"><a href="/opinion/1484849/united-states-v-rabinowitz/#735" aria-description="Citation for case: United States v. Rabinowitz">176 F. 2d 732, 735</a></span> (CA2 1949), rev’d, <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>. Judge Hand’s view was ultimately vindicated in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#768" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 768</a></span>, which specifically disapproved this Court’s decision in <em>Rabinowitz. </em>See also Mr. Justice Stewart’s opinion concurring in the result in <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#571" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 571-572</a></span>, quoted <em>supra, </em>at 653-654.</p>
</footnote>
<footnote label="14">
<p id="b701-9"> It is arguable that a third party’s inspection of the contents of “private books, papers, memoranda, etc.” could be so complete that there would be no additional search by the FBI when it re-examines the materials. Cf. <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#470" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 470</a></span>. But this is not such a case, because it was clearly necessary for the FBI to screen the films, which the private party had not done, in order to obtain the evidence needed to accomplish its law enforcement objectives.</p>
</footnote>
</opinion>
```

---
