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

## GROUP: content/cases/Byars v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Byars v. United States"
type: case
citation: "273 U.S. 28 (1927)"
parallel_cite: "47 S. Ct. 248; 71 L. Ed. 520"
neutral_cite: 1927 U.S. LEXIS 679
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1927
date_decided: 1927-01-03
docket: 72
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1927-01-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Byars v. United States
  varies_by_point: false
  scope_note: "Not overruled. Its core Fourth Amendment holdings — a conclusory affidavit cannot support a warrant, and an unconstitutional search is not validated by its fruits — survive. The federal-participation / silver-platter framework it operated within was superseded by Elkins v. United States (1960) and [[Mapp v. Ohio]] (1961), which extended exclusion to all illegally seized evidence regardless of which sovereign's officers searched."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/100980/byars-v-united-states/"
  cluster_id: 100980
  opinion_id: 100980
  identity_checked: true
homes:
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Historical"
  - page: "[[The Exclusionary Rule]]"
    role: "Related (cross-doctrine)"
related: ["[[Weeks v. United States]]", "[[Boyd v. United States]]", "[[Mapp v. Ohio]]", "[[Agnello v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "affidavit", "exclusionary-rule", "silver-platter"]
holding: "A warrant resting on a wholly conclusory affidavit is invalid; and where a federal officer participates in a state search under color of federal office, the search is in substance a federal undertaking bound by federal constitutional standards, so its fruits are inadmissible in federal court."
lake:
  record_id: Byars v. United States
  status: verified
  projected_at: 2026-07-06
---

# Byars v. United States

*273 U.S. 28 (1927)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Byars was convicted in federal court of possessing counterfeit whiskey strip stamps. The stamps were found while officers executed a state search warrant for intoxicating liquors, issued by a state municipal judge on an affidavit stating only that the affiant "has good reason to believe and does believe" liquor was present. The local officer in charge specifically asked a federal prohibition agent to come along; the agent participated in the search, personally found some of the stamps, and kept all of them for federal use. Byars moved to suppress.

## Issue
May evidence seized during a state search in which a federal officer actively participated — under a state warrant resting on a conclusory affidavit — be used against the defendant in a federal prosecution?

## Rule
No. The supporting affidavit was wholly conclusory, so "[t]he warrant clearly is bad if tested by the Fourth Amendment and the laws of the United States." — 273 U.S. at 29. ^pin-29

And "[a] search prosecuted in violation of the Constitution is not made lawful by what it brings to light." — *Id.* ^pin-29b

While "the mere participation in a state search of one who is a federal officer does not render it a federal undertaking, the court must be vigilant to scrutinize the attendant facts with an eye to detect and a hand to prevent violations of the Constitution by circuitous and indirect methods." — *Id.* at 32. ^pin-32

Where the federal officer participates under color of his office, "the search in substance and effect [is] a joint operation of the local and federal officers," treated as a federal search bound by federal standards. — *Id.* at 33. ^pin-33

The Government may use evidence "improperly seized by state officers operating entirely upon their own account[,]" "[b]ut the rule is otherwise when the federal government itself, through its agents acting as such, participates . . . in the wrongful search and seizure." — *Id.* at 33–34. ^pin-33b

## Application
The affidavit alleged only belief, with no facts, so the warrant failed Fourth Amendment standards. The federal agent had been specifically requested, participated as a federal officer, and took and kept the stamps — which bore no relation to any state offense — for the federal government, a practical concession that he acted in his federal character. The search was therefore in substance a federal operation; its fruits could not be admitted in the federal prosecution, and the unlawful search was not redeemed by the incriminating stamps it produced.

## Conclusion
The conviction rested on unconstitutionally seized evidence; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Byars* has not been overruled. Its Fourth Amendment principles — that a bare, conclusory affidavit cannot support a warrant, and that an unconstitutional search is not legitimized by its fruits — remain sound. The federal/state framework it applied (federal participation triggers federal standards; evidence from a state-only search could still be used — the "silver-platter" doctrine) was later overtaken: *[[Elkins v. United States]]* (1960) abolished the silver-platter doctrine, and [[Mapp v. Ohio]] (1961) applied the exclusionary rule to the States, so the federal-participation distinction is now of historical interest only.

## Appears on
- [[Probable Cause in the Affidavit]] — *Historical*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Byars v. United States*, 273 U.S. 28 (1927) — https://www.courtlistener.com/opinion/100980/byars-v-united-states/ — pinpoints: 29, 32, 33, 34.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "62de758ff322b7be", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "273 U.S. 28 (1927)", "court": "U.S. Supreme Court", "neutral_cite": "1927 U.S. LEXIS 679", "official_citation_present": true, "parallel_cite": "47 S. Ct. 248; 71 L. Ed. 520", "title": "Byars v. United States", "year": "1927"}}
{"assertion_id": "11450ed77fc7b1d8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrant resting on a wholly conclusory affidavit is invalid; and where a federal officer participates in a state search under color of federal office, the search is in substance a federal undertaking bound by federal constitutional standards, so its fruits are inadmissible in federal court.", "title": "Byars v. United States"}}
{"assertion_id": "423fbea32dc0e014", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Historical", "title": "Byars v. United States"}}
{"assertion_id": "6faed7244f6dff72", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Related (cross-doctrine)", "title": "Byars v. United States"}}
{"assertion_id": "7e51cc0fffd313b5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1927-01-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Byars v. United States", "field_i_validity": "good_law", "scope_note": "Not overruled. Its core Fourth Amendment holdings — a conclusory affidavit cannot support a warrant, and an unconstitutional search is not validated by its fruits — survive. The federal-participation / silver-platter framework it operated within was superseded by Elkins v. United States (1960) and [[Mapp v. Ohio]] (1961), which extended exclusion to all illegally seized evidence regardless of which sovereign's officers searched.", "title": "Byars v. United States", "varies_by_point": "false"}}
{"assertion_id": "e3d5e9fde8a2ba3f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Byars v. United States"}}
```

### lake record — Byars v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Byars v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Byars v. United States",
    "case_name_short": "Byars",
    "case_name_full": "Byars v. United States",
    "input_case_name": "Byars v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1927-01-03",
    "year": 1927,
    "docket": "72",
    "cluster_id": 100980,
    "lead_opinion_id": 100980,
    "sibling_ids": [
      100980
    ],
    "absolute_url": "/opinion/100980/byars-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "273 U.S. 28",
      "volume": "273",
      "reporter": "U.S.",
      "page": "28",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "47 S. Ct. 248",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "248",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 520",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "520",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1927 U.S. LEXIS 679",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "679",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "273 U.S. 28",
        "volume": "273",
        "reporter": "U.S.",
        "page": "28",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "47 S. Ct. 248",
        "volume": "47",
        "reporter": "S. Ct.",
        "page": "248",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "71 L. Ed. 520",
        "volume": "71",
        "reporter": "L. Ed.",
        "page": "520",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1927 U.S. LEXIS 679",
        "volume": "1927",
        "reporter": "U.S. LEXIS",
        "page": "679",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "273 U.S. 28",
    "official_selection": {
      "court_class": "scotus",
      "selected": "273 U.S. 28",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-29",
      "page": null,
      "quote": "liquor was present. The local officer in charge specifically asked a federal prohibition agent to come along; the agent participated in the search, personally found some of the stamps, and kept all of them for federal use. Byars moved to suppress. ## Issue May evidence seized during a state search in which a federal officer actively participated \u2014 under a state warrant resting on a conclusory affidavit \u2014 be used against the defendant in a federal prosecution? ## Rule No. The supporting affidavit was wholly conclusory, so",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-29b",
      "page": null,
      "quote": "[a] search prosecuted in violation of the Constitution is not made lawful by what it brings to light.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-32",
      "page": null,
      "quote": "the mere participation in a state search of one who is a federal officer does not render it a federal undertaking, the court must be vigilant to scrutinize the attendant facts with an eye to detect and a hand to prevent violations of the Constitution by circuitous and indirect methods.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-33",
      "page": null,
      "quote": "the search in substance and effect [is] a joint operation of the local and federal officers,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-33b",
      "page": null,
      "quote": "improperly seized by state officers operating entirely upon their own account[,]",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1927-01-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Byars v. United States",
    "varies_by_point": false,
    "scope_note": "Not overruled. Its core Fourth Amendment holdings \u2014 a conclusory affidavit cannot support a warrant, and an unconstitutional search is not validated by its fruits \u2014 survive. The federal-participation / silver-platter framework it operated within was superseded by Elkins v. United States (1960) and [[Mapp v. Ohio]] (1961), which extended exclusion to all illegally seized evidence regardless of which sovereign's officers searched.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Warren",
          "cluster_id": 2806866,
          "cite": [
            "87 Mass. App. Ct. 476"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mark Brock Palmer",
          "cluster_id": 603897,
          "cite": [
            "990 F.2d 490",
            "93 Daily Journal DAR 4307",
            "93 Cal. Daily Op. Serv. 2528",
            "1993 U.S. App. LEXIS 6868",
            "1993 WL 96500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rocky Dale McKeever Brenda Gayle McKeever and Stephen C. Newman",
          "cluster_id": 543114,
          "cite": [
            "905 F.2d 829",
            "1990 U.S. App. LEXIS 10558",
            "1990 WL 86435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wanda Anderson MacConnell United States of America v. Kenneth L. MacConnell",
          "cluster_id": 518789,
          "cite": [
            "868 F.2d 281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hawk",
          "cluster_id": 8922952,
          "cite": [
            "628 F.2d 1139"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steve Karathanos and John Karathanos",
          "cluster_id": 333763,
          "cite": [
            "531 F.2d 26"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "W. Thomas Holmes v. Waldon v. Burr, Sheriff of Pima County, Arizona",
          "cluster_id": 314071,
          "cite": [
            "486 F.2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fry v. State",
          "cluster_id": 2456043,
          "cite": [
            "493 S.W.2d 758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Robert Payne",
          "cluster_id": 291194,
          "cite": [
            "429 F.2d 169",
            "1970 U.S. App. LEXIS 8358"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Superior Court",
          "cluster_id": 2191869,
          "cite": [
            "275 Cal. App. 2d 489",
            "79 Cal. Rptr. 904",
            "1969 Cal. App. LEXIS 1940"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Melvin Corngold v. United States",
          "cluster_id": 273246,
          "cite": [
            "367 F.2d 1",
            "1966 U.S. App. LEXIS 4865"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Buys",
          "cluster_id": 6316251,
          "cite": [
            "42 Misc. 2d 154",
            "246 N.Y.S.2d 925",
            "1964 N.Y. Misc. LEXIS 2180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Chin Kay v. United States",
          "cluster_id": 259093,
          "cite": [
            "311 F.2d 317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Eastman",
          "cluster_id": 6311875,
          "cite": [
            "33 Misc. 2d 583",
            "228 N.Y.S.2d 156",
            "1962 N.Y. Misc. LEXIS 3424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane1_negative"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bumper v. North Carolina",
          "cluster_id": 107716,
          "cite": [
            "20 L. Ed. 2d 797",
            "88 S. Ct. 1788",
            "391 U.S. 543",
            "1968 U.S. LEXIS 1470",
            "46 Ohio Op. 2d 382"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanley v. Georgia",
          "cluster_id": 107898,
          "cite": [
            "22 L. Ed. 2d 542",
            "89 S. Ct. 1243",
            "394 U.S. 557",
            "1969 U.S. LEXIS 1972"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Di Re",
          "cluster_id": 104490,
          "cite": [
            "92 L. Ed. 2d 210",
            "68 S. Ct. 222",
            "332 U.S. 581",
            "1948 U.S. LEXIS 2667"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 104422,
          "cite": [
            "67 S. Ct. 1098",
            "331 U.S. 145",
            "91 L. Ed. 1399",
            "1947 U.S. LEXIS 2936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
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
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Go-Bart Importing Co. v. United States",
          "cluster_id": 101643,
          "cite": [
            "282 U.S. 344",
            "51 S. Ct. 153",
            "75 L. Ed. 374",
            "1931 U.S. LEXIS 842"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lefkowitz",
          "cluster_id": 101899,
          "cite": [
            "285 U.S. 452",
            "52 S. Ct. 420",
            "76 L. Ed. 877",
            "1932 U.S. LEXIS 446",
            "82 A.L.R. 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byars v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(100980) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0tMjQzOTkzNjAwMDAwJnM9MTk0MDk0MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28100980%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(100980)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDgmcz0xMDQwMDYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28100980%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(100980)",
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
    "complete_query": "cites:(100980)",
    "indexed_citing_opinions": 444,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 100980,
        "count": 444,
        "count_source": "search"
      }
    ],
    "citation_count": 701,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/byars-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQwNzU4MjQmcz0yNjUyODc2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28100980%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 100980,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100980,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100980,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100980,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100980,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 100980,
        "cited_id": 100711,
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
    "date_created": "2026-07-04T21:01:57Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:02:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:02:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:02:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Byars v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b102-17">
  Mr; Justice Sutherland
 </author>
<p id="ATG">
  delivered the opinion of the Court.
 </p>
<p id="b102-18">
  Petitioner was convicted in the federal district court for the southern district of Iowa upon two counts for unlaw
  <span citation-index="1" class="star-pagination" label="29"> 
   *29
   </span>
  fully having in-his possession with fraudulent intent) certain counterfeit strip stamps of the kind used upon whiskey bottled in bond. The stamps were admitted in evidence oven the objection of petitioner that they had been, obtained by an unlawful search and seizure. A timely-motion previously made by the petitioner to return or impound the stamps was overruled. The judgment of conviction was affirmed, by the court of appeals. 4 F. (2d) 507.
 </p>
<p id="b103-5">
  The stamps were found in executing a search warrant issued by the judge of a state municipal court and addressed to “ any peace officer of,Des Moines, Polk County, Iowa,” directing search for intoxicating liquors and instruments and materials used in the manufacture of such liquors. The information upon which the search warrant was issued states ■ only that affiant
  <em>
   “
  </em>
  has good reason to believe and does .believe the- defendant has .in his possession ” such intoxicating liquors, instruments and materials. The warrant clearly is bad if tested by the Fourth Amendment and the laws of the United States. C. 30, Title XI, §§ 3-6, <span class="citation no-link">40 Stat. 217</span>, 228-229; c. 85, Title II, § 2, <span class="citation no-link">41 Stat. 305</span>, 308. See
  <em>
   Ripper
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8774906"><a href="/opinion/8790952/ripper-v-united-states/#26" aria-description="Citation for case: Ripper v. United States">178 Fed. 24, 26</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Borkowski,
  </em>
  <span class="citation" data-id="8817957"><a href="/opinion/8832968/united-states-v-borkowski/#410" aria-description="Citation for case: United States v. Borkowski">268 Fed. 408, 410-411</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Kelly,
  </em>
  <span class="citation" data-id="8823440"><a href="/opinion/8838347/united-states-v-kelly/#486" aria-description="Citation for case: United States v. Kelly">277 Fed. 485, 486-489</a></span>. Whether it is good under the state law it is not necessary to inquire,! since' in no event could it constitute the basis for a federal search and seizure, as, under the facts hereinafter stated, it is insisted this was.
 </p>
<p id="b103-6">
  Nor is it material that the search was successful in revealing evidence of a violation of a federal statute; A search prosecuted in violation of the Constitution is not made lawful by what it brings to light; and the doctrine has never been recognized by this Court, nor can it be tolerated under our constitutional system, that evidences .of-crime discovered by a federal officer in making a séarch . without lawful warrant -may be used against the victim of
  <span citation-index="1" class="star-pagination" label="30"> 
   *30
   </span>
  the unlawful search where a timely challenge has been interposed.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#393" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 393</a></span>;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, 255
  </em>
  U. S. 298, 306;
  <em>
   Amos v. United States, 255
  </em>
  U. S. 313;
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States, 251
  </em>
  U. S. 385, 391;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  269 U. S, 20, 33.
 </p>
<p id="b104-4">
  The warrant directs the, officer to search certain described premises and, if . any of the liquors, instruments or materials set forth in the information are found, to seize the same and keep them until final action be had thereon. It was put into the hands of Mr. Densmore, a local officer in charge of the night liquor bureau of the police station in Des Moines, Iowa, and he, together with three others, proceeded to make the search in circumstances which can best be shown by quoting from the testimony given upon the hearing of the motion to impound or return the property seized. Mr. Densmore testified as follows:
 </p>
<p id="b104-5">
  “As I came down stairs, I asked the Captain about Mr. Adams who was there, and I asked him to go with me. Mr. Adams is the Federal Prohibition Agent, stationed here in Des Moines, Iowa, an officer of the government, operating under the Treasury Department. I met him after the warrant had been sued out, and asked him to go with me. I had the warrant at that time. It was in the police station of the city that I met Mr. Adams and requested him to come along. I had not discussed this case with Mr. Adams before that. He went with me from the city building on the search. As far as I know, he did not have any warrant or any authority to go into that residence other than the authority that I may have given him under the warrant I had. The search and seizure was made entirely upon the authority of the warrant that I had obtained at the City Hall. Arriving at the residence, I assigned each man a room. I assigned Adams a room. We found no intoxicating liquors there. The only thing, that we found that we took were the stamps in
  <span citation-index="1" class="star-pagination" label="31"> 
   *31
   </span>
  volved in this case. Mr. Taylor found part of them, and Mr. Adams found part of them. Mr. Adams kept the stamps he found in his possession and those found by Mr. Taylor were turned over to him right at that time. The ones that Adams found and the ones that were given to him were taken possession of by Adams right there in the house of A. J. Byars, immediately after the service. Neither myself or any of the other city officers had- possession of those stamps after that evening. There was never any prosecution attempted in the city courts or such courts as I was connected with so far as these stamps were involved.”
 </p>
<p id="b105-5">
  Mr. Adams, the federa,! prohibition agent, testified:
 </p>
<blockquote id="b105-6">
  “ I remember assisting in the search of the residence of A. J. Byars on the 22nd day of April, 1924.. Officers Dens-more, Taylor,, DeHaven and Davis were with me. I met them in the Captain’s office at the police station in the city of Des Moines and accompanied them to make the search. I-had no authority for going into the house other than the search warrant that the officers had secured from the state authorities. The only authority that I had for going into the house of Mr. Byars was on account of the search warrant that Mr. Densmore had. I searched the kitchen. I found some of the stamps that were involved in this case there in the kitchen. I took possession of them then and there, and have retained them ever since. I have retained +he stamps that I found and those that were handed me there in the house. I was not present with Mr. Taylor "in the room when' he found the stamps, but they were brought to me in the dining room by Mr. Taylor, and I took possession of them then and there, -.and I have retained possession of all the stamps from that time until this. They were never delivered to the state officers or used by "them. I do not know of any violation of any state law that they could be used for. • I knew there was no state law governing the possession of
  <span citation-index="1" class="star-pagination" label="32"> 
   *32
   </span>
  these stamps, and as a Federal Officer, I took possession of what I found, and those found by the State Officer, and have had them in my possession ever since and receipted to the Police officers at the Station that evening after the return from the raid, for the stamps found.”
 </blockquote>
<p id="b106-6">
  While it is true that the
  <em>
   mere
  </em>
  participation in a state search of one who is a federal officer does not render it a federal undertaking, the court must be vigilant to scrutinize the attendant facts with an eye to detect and a hand to prevent violations of the Constitution by circuitous and indirect methods. Constitutional provisions for the security of person and property are to bé liberally construed, and
  <em>
   “
  </em>
  it ■ is the duty of courts to be watchful for the constitutional rights of the citizen, and against any, stealthy encroachments thereon.”
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>;
  <em>
   Gouled
  </em>
  v.
  <em>
   United States, supra,
  </em>
  p. 304.
 </p>
<p id="b106-7">
  The attendant facts here reasonably suggest that the federal prohibition agent was not invited to join the state squad as a private person might have been, but was asked to participate and did participate as a federal enforcement officer, upon the chance,, which was subsequently realized, that something would be disclosed of official interest to him as such agent. The house to be searched contained only four
  <em>
   rooms
  </em>
  — a dining room, a kitchen and two' bedrooms. We are not prepared to accept the view that the local officer thought a. force of-four men would be insufficient to search these -limited premises; and it is significant, in that connection, that he did not ask his superior officer for additional help, but inquired particularly for Adams, who, he knew, was the federal agent. The stamps found were not within the purview of the state search warrant, nor did they relate in any way to a ■violation of state law. Those found by the agent were held by him as of right and without questidn; those found by the state officer were considered by both the local officer
  <span citation-index="1" class="star-pagination" label="33"> 
   *33
   </span>
  in charge and the federal agent as things which concerned the federal government alone and then and there were surrendered to the exclusive possession of the federal agent, — a practical concession that he was present in his federal character. We cannot avoid the conclusion that the participation of the agent in the search was under color of his federal office and that the search in substance and effect was a joint operation of the local and federal officers. In that view, so far as this inquiry is concerned, the effect is the same as though he had engaged in the undertaking as. one exclusively his own. Similar questions have been presented in a variety of forms to the lower federal courts, but nothing is to be gained by attempting to review the decisions, since each of them rests, as the present case does, upon its own peculiar facts. But see and compare
  <em>
   Flagg
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8799726"><a href="/opinion/8815246/flagg-v-united-states/#483" aria-description="Citation for case: Flagg v. United States">233 Fed. 481, 483</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Slusser,
  </em>
  <span class="citation" data-id="8819339"><a href="/opinion/8834327/united-states-v-slusser/#820" aria-description="Citation for case: United States v. Slusser">270 Fed. 818, 820</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Falloco,
  </em>
  <span class="citation" data-id="8823350"><a href="/opinion/8838257/united-states-v-falloco/#82" aria-description="Citation for case: United States v. Falloco">277 Fed. 75, 82</a></span>;
  <em>
   Legman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8834058"><a href="/opinion/8848718/legman-v-united-states/#476" aria-description="Citation for case: Legman v. United States">295 Fed. 474, 476-478</a></span>;
  <em>
   Marron
  </em>
  v.
  <em>
   United States,
  </em>
  8 F. (2d) 251, 259;
  <em>
   United States
  </em>
  v.
  <em>
   Brown,
  </em>
  <span class="citation" data-id="1508963"><a href="/opinion/1508963/united-states-v-brown/#631" aria-description="Citation for case: United States v. Brown">8 F.(2d) 630, 631</a></span>.
 </p>
<p id="b107-6">
  We do' not question the right of the federal government to avail itself of evidence improperly seized by state officers operating entirely upon their own account. But the rule is otherwise when the federal government itself, through its agents acting as such, participates ■ in the wrongful search and seizure. To hold the contrary would be to disregard the plain spirit and-purpose of the constitutional prohibitions intended to secure the people against unauthorized official action. The Fourth Amendment was adopted in view of long misuse of power in the matter of searches and seizures both in England and the colonies; and the assurance against any revival of it, so carefully embodied in the fundamental law, is not to be impaired by judicial sanction of equivocal methods,
  <span citation-index="1" class="star-pagination" label="34"> 
   *34
   </span>
  which, regarded superficially, may seem to escape the challenge of illegality but which, in reality, -strike at the substance of the constitutional right.
 </p>
<p id="b108-4">
<em>
   Judgment reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Byrd v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Byrd v. United States"
type: case
citation: "584 U.S. 395 (2018)"
parallel_cite: "138 S. Ct. 1518; 200 L. Ed. 2d 805"
neutral_cite: 2018 U.S. LEXIS 2803
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-05-14
docket: 16-1371
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-05-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Byrd v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4497658/byrd-v-united-states/"
  cluster_id: 4497658
  opinion_id: 4274911
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Jones v. United States]]", "[[Brendlin v. California]]"]
aliases: ["Byrd v. US"]
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "rental-car"]
holding: "A driver in lawful possession and control of a rental car generally has a reasonable expectation of privacy in it, even though he is not…"
lake:
  record_id: Byrd v. United States
  status: verified
  projected_at: 2026-07-06
---

# Byrd v. United States

*584 U.S. 395 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Terrence Byrd drove a car that a companion had rented; he was not listed as an authorized driver on the rental agreement. Troopers stopped him, learned he was not on the agreement, searched the car, and found body armor and heroin in the trunk. The lower courts held Byrd lacked any [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] because he was not an authorized renter.

## Issue
Whether a driver in otherwise lawful possession and control of a rental car has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it when he is not listed on the rental agreement.

## Rule
"The Court now holds that, as a general rule, someone in otherwise lawful possession and control of a rental car has a reasonable expectation of privacy in it even if the rental agreement does not list him or her as an authorized driver." — *Byrd v. United States*, 584 U.S. 395 (2018) (slip op., at 2). ^pin-op2

## Application
Byrd was the sole occupant in possession and control of the rental car, a situation the Court likened to one who is lent an apartment and can exclude others; not being listed on the agreement did not, by itself, defeat his expectation of privacy. The Court did not finally resolve his case, remanding to address the Government's argument that he was no better than a car thief — who would lack any legitimate expectation of privacy — and whether probable cause justified the search in any event.

## Conclusion
An unlisted but lawful driver generally has a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a rental car; the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Byrd* refines the standing framework of [[Rakas v. Illinois]] and [[Jones v. United States]] for the rental-car context.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Byrd v. United States*, 584 U.S. 395 (2018) — https://www.courtlistener.com/opinion/4497658/byrd-v-united-states/ — pinpoint: slip op., at 2 (CL carries the slip opinion; cluster 4497658 → opinion 4274911).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0aa2fafe8033894a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "584 U.S. 395 (2018)", "court": "U.S. Supreme Court", "neutral_cite": "2018 U.S. LEXIS 2803", "official_citation_present": true, "parallel_cite": "138 S. Ct. 1518; 200 L. Ed. 2d 805", "title": "Byrd v. United States", "year": "2018"}}
{"assertion_id": "161d211f7f07c0b2", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Progeny / Refinement", "title": "Byrd v. United States"}}
{"assertion_id": "5d93cd5cb92d202f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A driver in lawful possession and control of a rental car generally has a reasonable expectation of privacy in it, even though he is not…", "title": "Byrd v. United States"}}
{"assertion_id": "cd0732442df704cf", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Byrd v. United States"}}
{"assertion_id": "db343e6c1a9250e9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2018-05-14", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Byrd v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Byrd v. United States", "varies_by_point": "false"}}
```

### lake record — Byrd v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Byrd v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Byrd v. United States",
    "case_name_short": "Byrd",
    "case_name_full": "",
    "input_case_name": "Byrd v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-05-14",
    "year": 2018,
    "docket": "16-1371",
    "cluster_id": 4497658,
    "lead_opinion_id": 4274911,
    "sibling_ids": [
      4274911
    ],
    "absolute_url": "/opinion/4497658/byrd-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9337228,
        "score": 10,
        "case_name": "Byrd v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "584 U.S. 395",
      "volume": "584",
      "reporter": "U.S.",
      "page": "395",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1518",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1518",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 805",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "805",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 2803",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2803",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "584 U.S. 395",
        "volume": "584",
        "reporter": "U.S.",
        "page": "395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1518",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1518",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 805",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "805",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 2803",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2803",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "584 U.S. 395",
    "official_selection": {
      "court_class": "scotus",
      "selected": "584 U.S. 395",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op2",
      "page": null,
      "quote": "--- # Byrd v. United States *584 U.S. 395 (2018)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Terrence Byrd drove a car that a companion had rented; he was not listed as an authorized driver on the rental agreement. Troopers stopped him, learned he was not on the agreement, searched the car, and found body armor and heroin in the trunk. The lower courts held Byrd lacked any reasonable expectation of privacy because he was not an authorized renter. ## Issue Whether a driver in otherwise lawful possession and control of a rental car has a reasonable expectation of privacy in it when he is not listed on the rental agreement. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-05-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Byrd v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nat'l Credit Union Admin. Bd. v. U.S. Bank Nat'l Ass'n",
          "cluster_id": 4523095,
          "cite": [
            "898 F.3d 243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Dixon",
          "cluster_id": 4529808,
          "cite": [
            "901 F.3d 1322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joshua Saquan Maurice Eley v. Commonwealth of Virginia",
          "cluster_id": 4610383,
          "cite": [
            "826 S.E.2d 321",
            "70 Va. App. 158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charlie L. Green",
          "cluster_id": 4833880,
          "cite": [
            "981 F.3d 945"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lyle",
          "cluster_id": 8443943,
          "cite": [
            "919 F.3d 716"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armando Villanueva v. State of California",
          "cluster_id": 4851713,
          "cite": [
            "986 F.3d 1158"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The Keene Group, Inc. v. City of Cincinnati, Ohio",
          "cluster_id": 4884918,
          "cite": [
            "998 F.3d 306"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ethridge v. Bell",
          "cluster_id": 8242301,
          "cite": [
            "49 F.4th 674"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Quentin Ferebee",
          "cluster_id": 4747521,
          "cite": [
            "957 F.3d 406"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rex Hammond",
          "cluster_id": 4877368,
          "cite": [
            "996 F.3d 374"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wali Ebbin Rashee Ross",
          "cluster_id": 4763360,
          "cite": [
            "963 F.3d 1056"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Demetrius Brooks",
          "cluster_id": 4854998,
          "cite": [
            "987 F.3d 593"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Denzell Russell",
          "cluster_id": 6357516,
          "cite": [
            "26 F.4th 371"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nahach Garay",
          "cluster_id": 4661504,
          "cite": [
            "938 F.3d 1108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vitagliano v. County of Westchester",
          "cluster_id": 9408029,
          "cite": [
            "71 F.4th 130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Scheuerman",
          "cluster_id": 6236732,
          "cite": [
            "502 P.3d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martavis James",
          "cluster_id": 4898691,
          "cite": [
            "3 F.4th 1102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Balmy Lincoln Joseph",
          "cluster_id": 4800601,
          "cite": [
            "978 F.3d 1251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Maxim",
          "cluster_id": 4683972,
          "cite": [
            "454 P.3d 543",
            "165 Idaho 901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Rogers",
          "cluster_id": 9492473,
          "cite": [
            "97 F.4th 1038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Dixon",
          "cluster_id": 4844659,
          "cite": [
            "984 F.3d 814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ahmed Hammoud v. Equifax Information Servs.",
          "cluster_id": 8466966,
          "cite": [
            "52 F.4th 669"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert White",
          "cluster_id": 4763247,
          "cite": [
            "962 F.3d 1052"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gerald Schram",
          "cluster_id": 4528495,
          "cite": [
            "901 F.3d 1042"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Byrd v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4274911) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 96,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 96,
        "triage_read": 0,
        "triage_snippet_classified": 96
      },
      "lane2_top_cited": {
        "query": "cites:(4274911)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04JnM9OTQxMzEyMSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284274911%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4274911)",
        "reviewed": 63,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 63,
        "triage_read": 0,
        "triage_snippet_classified": 63
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4274911)",
    "indexed_citing_opinions": 124,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4274911,
        "count": 124,
        "count_source": "search"
      }
    ],
    "citation_count": 290,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/byrd-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NzM0MTcmcz05NDk2OTk4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284274911%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4274911,
        "cited_id": 31294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 142900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 212488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 214467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 551363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 676083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 751576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 774727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4274911,
        "cited_id": 794349,
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
    "date_created": "2026-07-04T21:07:32Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:07:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:07:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:10:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:07:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Byrd v. United States

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

                       BYRD v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE THIRD CIRCUIT

     No. 16–1371.      Argued January 9, 2018—Decided May 14, 2018
Latasha Reed rented a car in New Jersey while petitioner Terrence
  Byrd waited outside the rental facility. Her signed agreement
  warned that permitting an unauthorized driver to drive the car
  would violate the agreement. Reed listed no additional drivers on the
  form, but she gave the keys to Byrd upon leaving the building. He
  stored personal belongings in the rental car’s trunk and then left
  alone for Pittsburgh, Pennsylvania. After stopping Byrd for a traffic
  infraction, Pennsylvania State Troopers learned that the car was
  rented, that Byrd was not listed as an authorized driver, and that
  Byrd had prior drug and weapons convictions. Byrd also stated he
  had a marijuana cigarette in the car. The troopers proceeded to
  search the car, discovering body armor and 49 bricks of heroin in the
  trunk. The evidence was turned over to federal authorities, who
  charged Byrd with federal drug and other crimes. The District Court
  denied Byrd’s motion to suppress the evidence as the fruit of an un-
  lawful search, and the Third Circuit affirmed. Both courts concluded
  that, because Byrd was not listed on the rental agreement, he lacked
  a reasonable expectation of privacy in the car.
Held:
    1. The mere fact that a driver in lawful possession or control of a
  rental car is not listed on the rental agreement will not defeat his or
  her otherwise reasonable expectation of privacy. Pp. 6–13.
       (a) Reference to property concepts is instructive in “determining
  the presence or absence of the privacy interests protected by [the
  Fourth] Amendment.” Rakas v. Illinois, 439 U. S. 128, 144, n. 12.
  Pp. 6–7.
       (b) While a person need not always have a recognized common-
  law property interest in the place searched to be able to claim a rea-
2                       BYRD v. UNITED STATES

                                  Syllabus

    sonable expectation of privacy in it, see, e.g., Jones v. United States,
    362 U. S. 257, 259, legitimate presence on the premises, standing
    alone, is insufficient because it “creates too broad a gauge for meas-
    urement of Fourth Amendment rights,” Rakas, 439 U. S., at 142. The
    Court has not set forth a single metric or exhaustive list of relevant
    considerations, but “[l]egitimation of expectations of privacy must
    have a source outside of the Fourth Amendment, either by reference
    to concepts of real or personal property law or to understandings that
    are recognized and permitted by society.” Id., at 144, n. 12. These
    concepts may be linked. “One of the main rights attaching to proper-
    ty is the right to exclude others,” and “one who owns or lawfully pos-
    sesses or controls property will in all likelihood have a legitimate ex-
    pectation of privacy by virtue of the right to exclude.” Ibid. This
    general property-based concept guides resolution of the instant case.
    Pp. 8–9.
         (c) The Government’s contention that drivers who are not listed
    on rental agreements always lack an expectation of privacy in the car
    rests on too restrictive a view of the Fourth Amendment’s protections.
    But Byrd’s proposal that a rental car’s sole occupant always has an
    expectation of privacy based on mere possession and control would,
    without qualification, include thieves or others who have no reasona-
    ble expectation of privacy. Pp. 9–13.
            (1) The Government bases its claim that an unauthorized driv-
    er has no privacy interest in the vehicle on a misreading of Rakas.
    There, the Court disclaimed any intent to hold that passengers can-
    not have an expectation of privacy in automobiles, but found that the
    passengers there had not claimed “any legitimate expectation of pri-
    vacy in the areas of the car which were searched.” 439 U. S., at 150,
    n. 17. Byrd, in contrast, was the rental car’s driver and sole occu-
    pant. His situation is similar to the defendant in Jones, who had a
    reasonable expectation of privacy in his friend’s apartment because
    he “had complete dominion and control over the apartment and could
    exclude others from it.” Rakas, supra, at 149. The expectation of
    privacy that comes from lawful possession and control and the at-
    tendant right to exclude should not differ depending on whether a car
    is rented or owned by someone other than the person currently pos-
    sessing it, much as it did not seem to matter whether the defendant’s
    friend in Jones owned or leased the apartment he permitted the de-
    fendant to use in his absence. Pp. 9–11.
            (2) The Government also contends that Byrd had no basis for
    claiming an expectation of privacy in the rental car because his driv-
    ing of that car was so serious a breach of Reed’s rental agreement
    that the rental company would have considered the agreement “void”
    once he took the wheel. But the contract says only that the violation
                     Cite as: 584 U. S. ____ (2018)                     3

                                Syllabus

  may result in coverage, not the agreement, being void and the rent-
  er’s being fully responsible for any loss or damage, and the Govern-
  ment fails to explain what bearing this breach of contract, standing
  alone, has on expectations of privacy in the car. Pp. 11–12.
         (3) Central, though, to reasonable expectations of privacy in
  these circumstances is the concept of lawful possession, for a
  “ ‘wrongful’ presence at the scene of a search would not enable a de-
  fendant to object to the legality of the search,” Rakas, supra, at 141,
  n. 9. Thus, a car thief would not have a reasonable expectation of
  privacy in a stolen car no matter the degree of possession and control.
  The Court leaves for remand the Government’s argument that one
  who intentionally uses a third party to procure a rental car by a
  fraudulent scheme for the purpose of committing a crime is no better
  situated than a car thief. Pp. 12–13.
     2. Also left for remand is the Government’s argument that, even if
  Byrd had a right to object to the search, probable cause justified it in
  any event. The Third Circuit did not reach this question because it
  concluded, as an initial matter, that Byrd lacked a reasonable expec-
  tation of privacy in the rental car. That court has discretion as to the
  order in which the remanded questions are best addressed. Pp. 13–
  14.
679 Fed. Appx. 146, vacated and remanded.

   KENNEDY, J., delivered the opinion for a unanimous Court. THOMAS,
J., filed a concurring opinion, in which GORSUCH, J., joined. ALITO, J.,
filed a concurring opinion.
                        Cite as: 584 U. S. ____ (2018)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 16–1371
                                   _________________


 TERRENCE BYRD, PETITIONER v. UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE THIRD CIRCUIT
                                 [May 14, 2018]

  JUSTICE KENNEDY delivered the opinion of the Court.
  In September 2014, Pennsylvania State Troopers pulled
over a car driven by petitioner Terrence Byrd. Byrd was
the only person in the car. In the course of the traffic stop
the troopers learned that the car was rented and that
Byrd was not listed on the rental agreement as an author-
ized driver. For this reason, the troopers told Byrd they
did not need his consent to search the car, including its
trunk where he had stored personal effects. A search of
the trunk uncovered body armor and 49 bricks of heroin.
  The evidence was turned over to federal authorities,
who charged Byrd with distribution and possession of
heroin with the intent to distribute in violation of 21
U. S. C. §841(a)(1) and possession of body armor by a
prohibited person in violation of 18 U. S. C. §931(a)(1).
Byrd moved to suppress the evidence as the fruit of an
unlawful search. The United States District Court for the
Middle District of Pennsylvania denied the motion, and
the Court of Appeals for the Third Circuit affirmed. Both
courts concluded that, because Byrd was not listed on the
rental agreement, he lacked a reasonable expectation of
privacy in the car. Based on this conclusion, it appears
2                 BYRD v. UNITED STATES

                     Opinion of the Court

that both the District Court and Court of Appeals deemed
it unnecessary to consider whether the troopers had prob-
able cause to search the car.
   This Court granted certiorari to address the question
whether a driver has a reasonable expectation of privacy
in a rental car when he or she is not listed as an author-
ized driver on the rental agreement. The Court now holds
that, as a general rule, someone in otherwise lawful pos-
session and control of a rental car has a reasonable expec-
tation of privacy in it even if the rental agreement does
not list him or her as an authorized driver.
   The Court concludes a remand is necessary to address in
the first instance the Government’s argument that this
general rule is inapplicable because, in the circumstances
here, Byrd had no greater expectation of privacy than a
car thief. If that is so, our cases make clear he would lack
a legitimate expectation of privacy. It is necessary to
remand as well to determine whether, even if Byrd had a
right to object to the search, probable cause justified it in
any event.
                              I
  On September 17, 2014, petitioner Terrence Byrd and
Latasha Reed drove in Byrd’s Honda Accord to a Budget
car-rental facility in Wayne, New Jersey. Byrd stayed in
the parking lot in the Honda while Reed went to the
Budget desk and rented a Ford Fusion. The agreement
Reed signed required her to certify that she had a valid
driver’s license and had not committed certain vehicle-
related offenses within the previous three years. An ad-
dendum to the agreement, which Reed initialed, provides
the following restriction on who may drive the rental car:
    “I understand that the only ones permitted to drive
    the vehicle other than the renter are the renter’s
    spouse, the renter’s co-employee (with the renter’s
    permission, while on company business), or a person
                  Cite as: 584 U. S. ____ (2018)            3

                      Opinion of the Court

    who appears at the time of the rental and signs an Ad-
    ditional Driver Form. These other drivers must also
    be at least 25 years old and validly licensed.

    “PERMITTING AN UNAUTHORIZED DRIVER TO
    OPERATE THE VEHICLE IS A VIOLATION OF
    THE RENTAL AGREEMENT. THIS MAY RESULT
    IN ANY AND ALL COVERAGE OTHERWISE
    PROVIDED BY THE RENTAL AGREEMENT BEING
    VOID AND MY BEING FULLY RESPONSIBLE FOR
    ALL LOSS OR DAMAGE, INCLUDING LIABILITY
    TO THIRD PARTIES.” App. 19.
In filling out the paperwork for the rental agreement,
Reed did not list an additional driver.
  With the rental keys in hand, Reed returned to the
parking lot and gave them to Byrd. The two then left the
facility in separate cars—she in his Honda, he in the
rental car. Byrd returned to his home in Patterson, New
Jersey, and put his personal belongings in the trunk of the
rental car. Later that afternoon, he departed in the car
alone and headed toward Pittsburgh, Pennsylvania.
  After driving nearly three hours, or roughly half the
distance to Pittsburgh, Byrd passed State Trooper David
Long, who was parked in the median of Interstate 81 near
Harrisburg, Pennsylvania. Long was suspicious of Byrd
because he was driving with his hands at the “10 and 2”
position on the steering wheel, sitting far back from the
steering wheel, and driving a rental car. Long knew the
Ford Fusion was a rental car because one of its windows
contained a barcode. Based on these observations, he
decided to follow Byrd and, a short time later, stopped him
for a possible traffic infraction.
  When Long approached the passenger window of Byrd’s
car to explain the basis for the stop and to ask for identifi-
cation, Byrd was “visibly nervous” and “was shaking and
4                 BYRD v. UNITED STATES

                     Opinion of the Court

had a hard time obtaining his driver’s license.” Id., at 37.
He handed an interim license and the rental agreement to
Long, stating that a friend had rented the car. Long re-
turned to his vehicle to verify Byrd’s license and noticed
Byrd was not listed as an additional driver on the rental
agreement. Around this time another trooper, Travis
Martin, arrived at the scene. While Long processed Byrd’s
license, Martin conversed with Byrd, who again stated
that a friend had rented the vehicle. After Martin walked
back to Long’s patrol car, Long commented to Martin that
Byrd was “not on the renter agreement,” to which Martin
replied, “yeah, he has no expectation of privacy.” 3 App. to
Brief for Appellant in No. 16–1509 (CA3), at 21:40.
   A computer search based on Byrd’s identification re-
turned two different names. Further inquiry suggested
the other name might be an alias and also revealed that
Byrd had prior convictions for weapons and drug charges
as well as an outstanding warrant in New Jersey for a
probation violation. After learning that New Jersey did
not want Byrd arrested for extradition, the troopers asked
Byrd to step out of the vehicle and patted him down.
   Long asked Byrd if he had anything illegal in the car.
When Byrd said he did not, the troopers asked for his
consent to search the car. At that point Byrd said he had
a “blunt” in the car and offered to retrieve it for them. The
officers understood “blunt” to mean a marijuana cigarette.
They declined to let him retrieve it and continued to seek
his consent to search the car, though they stated they did
not need consent because he was not listed on the rental
agreement. The troopers then opened the passenger and
driver doors and began a thorough search of the passenger
compartment.
   Martin proceeded from there to search the car’s trunk,
including by opening up and taking things out of a large
cardboard box, where he found a laundry bag containing
body armor. At this point, the troopers decided to detain
                 Cite as: 584 U. S. ____ (2018)            5

                     Opinion of the Court

Byrd. As Martin walked toward Byrd and said he would
be placing him in handcuffs, Byrd began to run away. A
third trooper who had arrived on the scene joined Long
and Martin in pursuit. When the troopers caught up to
Byrd, he surrendered and admitted there was heroin in
the car. Back at the car, the troopers resumed their
search of the laundry bag and found 49 bricks of heroin.
  In pretrial proceedings Byrd moved to suppress the
evidence found in the trunk of the rental car, arguing that
the search violated his Fourth Amendment rights. Al-
though Long contended at a suppression hearing that the
troopers had probable cause to search the car after Byrd
stated it contained marijuana, the District Court denied
Byrd’s motion on the ground that Byrd lacked “standing”
to contest the search as an initial matter, 2015 WL
5038455, *2 (MD Pa., Aug. 26, 2015) (citing United States
v. Kennedy, 638 F. 3d 159, 165 (CA3 2011)). Byrd later
entered a conditional guilty plea, reserving the right to
appeal the suppression ruling.
  The Court of Appeals affirmed in a brief summary opin-
ion. 679 Fed. Appx. 146 (CA3 2017). As relevant here, the
Court of Appeals recognized that a “circuit split exists as
to whether the sole occupant of a rental vehicle has a
Fourth Amendment expectation of privacy when that
occupant is not named in the rental agreement”; but it
noted that Circuit precedent already had “spoken as to
this issue . . . and determined such a person has no expec-
tation of privacy and therefore no standing to challenge a
search of the vehicle.” Id., at 150 (citing Kennedy, supra,
at 167–168). The Court of Appeals did not reach the
probable-cause question.
  This Court granted Byrd’s petition for a writ of certio-
rari, 582 U. S. ___ (2017), to address the conflict among the
Courts of Appeals over whether an unauthorized driver
has a reasonable expectation of privacy in a rental car.
Compare United States v. Seeley, 331 F. 3d 471, 472 (CA5
6                 BYRD v. UNITED STATES

                     Opinion of the Court

2003) (per curiam); United States v. Wellons, 32 F. 3d 117,
119 (CA4 1994); United States v. Roper, 918 F. 2d 885,
887–888 (CA10 1990), with United States v. Smith, 263
F. 3d 571, 581–587 (CA6 2001); Kennedy, supra, at 165–
168, and with United States v. Thomas, 447 F. 3d 1191,
1196–1199 (CA9 2006); United States v. Best, 135 F. 3d
1223, 1225 (CA8 1998).
                             II
  Few protections are as essential to individual liberty as
the right to be free from unreasonable searches and sei-
zures. The Framers made that right explicit in the Bill of
Rights following their experience with the indignities and
invasions of privacy wrought by “general warrants and
warrantless searches that had so alienated the colonists
and had helped speed the movement for independence.”
Chimel v. California, 395 U. S. 752, 761 (1969). Ever
mindful of the Fourth Amendment and its history, the
Court has viewed with disfavor practices that permit
“police officers unbridled discretion to rummage at will
among a person’s private effects.” Arizona v. Gant, 556
U. S. 332, 345 (2009).
  This concern attends the search of an automobile. See
Delaware v. Prouse, 440 U. S. 648, 662 (1979). The Court
has acknowledged, however, that there is a diminished
expectation of privacy in automobiles, which often permits
officers to dispense with obtaining a warrant before con-
ducting a lawful search. See, e.g., California v. Acevedo,
500 U. S. 565, 579 (1991).
  Whether a warrant is required is a separate question
from the one the Court addresses here, which is whether
the person claiming a constitutional violation “has had his
own Fourth Amendment rights infringed by the search
and seizure which he seeks to challenge.” Rakas v. Illi-
nois, 439 U. S. 128, 133 (1978). Answering that question
requires examination of whether the person claiming the
                  Cite as: 584 U. S. ____ (2018)            7

                      Opinion of the Court

constitutional violation had a “legitimate expectation of
privacy in the premises” searched. Id., at 143. “Expecta-
tions of privacy protected by the Fourth Amendment, of
course, need not be based on a common-law interest in
real or personal property, or on the invasion of such an
interest.” Id., at 144, n. 12. Still, “property concepts” are
instructive in “determining the presence or absence of the
privacy interests protected by that Amendment.” Ibid.
   Indeed, more recent Fourth Amendment cases have
clarified that the test most often associated with legiti-
mate expectations of privacy, which was derived from the
second Justice Harlan’s concurrence in Katz v. United
States, 389 U. S. 347 (1967), supplements, rather than
displaces, “the traditional property-based understanding
of the Fourth Amendment.” Florida v. Jardines, 569 U. S.
1, 11 (2013). Perhaps in light of this clarification, Byrd
now argues in the alternative that he had a common-law
property interest in the rental car as a second bailee that
would have provided him with a cognizable Fourth
Amendment interest in the vehicle. But he did not raise
this argument before the District Court or Court of Ap-
peals, and those courts did not have occasion to address
whether Byrd was a second bailee or what consequences
might follow from that determination. In those courts he
framed the question solely in terms of the Katz test noted
above. Because this is “a court of review, not of first view,”
Cutter v. Wilkinson, 544 U. S. 709, 718, n. 7 (2005), it is
generally unwise to consider arguments in the first in-
stance, and the Court declines to reach Byrd’s contention
that he was a second bailee.
   Reference to property concepts, however, aids the Court
in assessing the precise question here: Does a driver of a
rental car have a reasonable expectation of privacy in the
car when he or she is not listed as an authorized driver on
the rental agreement?
8                 BYRD v. UNITED STATES

                     Opinion of the Court

                             III
                              A
   One who owns and possesses a car, like one who owns
and possesses a house, almost always has a reasonable
expectation of privacy in it. More difficult to define and
delineate are the legitimate expectations of privacy of
others.
   On the one hand, as noted above, it is by now well estab-
lished that a person need not always have a recognized
common-law property interest in the place searched to be
able to claim a reasonable expectation of privacy in it. See
Jones v. United States, 362 U. S. 257, 259 (1960); Katz,
supra, at 352; Mancusi v. DeForte, 392 U. S. 364, 368
(1968); Minnesota v. Olson, 495 U. S. 91, 98 (1990).
   On the other hand, it is also clear that legitimate pres-
ence on the premises of the place searched, standing alone,
is not enough to accord a reasonable expectation of privacy,
because it “creates too broad a gauge for measurement
of Fourth Amendment rights.” Rakas, 439 U. S., at 142;
see also id., at 148 (“We would not wish to be understood
as saying that legitimate presence on the premises is
irrelevant to one’s expectation of privacy, but it cannot be
deemed controlling”); Minnesota v. Carter, 525 U. S. 83, 91
(1998).
   Although the Court has not set forth a single metric or
exhaustive list of considerations to resolve the circum-
stances in which a person can be said to have a reasonable
expectation of privacy, it has explained that “[l]egitimation
of expectations of privacy by law must have a source out-
side of the Fourth Amendment, either by reference to
concepts of real or personal property law or to understand-
ings that are recognized and permitted by society.” Rakas,
439 U. S., at 144, n. 12. The two concepts in cases like
this one are often linked. “One of the main rights attach-
ing to property is the right to exclude others,” and, in the
main, “one who owns or lawfully possesses or controls
                 Cite as: 584 U. S. ____ (2018)            9

                     Opinion of the Court

property will in all likelihood have a legitimate expecta-
tion of privacy by virtue of the right to exclude.” Ibid.
(citing 2 W. Blackstone, Commentaries on the Laws of
England, ch. 1). This general property-based concept
guides resolution of this case.
                             B
   Here, the Government contends that drivers who are
not listed on rental agreements always lack an expectation
of privacy in the automobile based on the rental company’s
lack of authorization alone. This per se rule rests on too
restrictive a view of the Fourth Amendment’s protections.
Byrd, by contrast, contends that the sole occupant of a
rental car always has an expectation of privacy in it based
on mere possession and control. There is more to recom-
mend Byrd’s proposed rule than the Government’s; but,
without qualification, it would include within its ambit
thieves and others who, not least because of their lack of
any property-based justification, would not have a reason-
able expectation of privacy.
                              1
   Stripped to its essentials, the Government’s position is
that only authorized drivers of rental cars have expecta-
tions of privacy in those vehicles. This position is based on
the following syllogism: Under Rakas, passengers do not
have an expectation of privacy in an automobile glove
compartment or like places; an unauthorized driver like
Byrd would have been the passenger had the renter been
driving; and the unauthorized driver cannot obtain greater
protection when he takes the wheel and leaves the renter
behind. The flaw in this syllogism is its major premise, for
it is a misreading of Rakas.
   The Court in Rakas did not hold that passengers cannot
have an expectation of privacy in automobiles. To the
contrary, the Court disclaimed any intent to hold “that a
10                BYRD v. UNITED STATES

                     Opinion of the Court

passenger lawfully in an automobile may not invoke the
exclusionary rule and challenge a search of that vehicle
unless he happens to own or have a possessory interest in
it.” 439 U. S., at 150, n. 17 (internal quotation marks
omitted). The Court instead rejected the argument that
legitimate presence alone was sufficient to assert a Fourth
Amendment interest, which was fatal to the petitioners’
case there because they had “claimed only that they were
‘legitimately on [the] premises’ and did not claim that they
had any legitimate expectation of privacy in the areas of
the car which were searched.” Ibid.
   What is more, the Government’s syllogism is beside the
point, because this case does not involve a passenger at all
but instead the driver and sole occupant of a rental car.
As Justice Powell observed in his concurring opinion in
Rakas, a “distinction . . . may be made in some circum-
stances between the Fourth Amendment rights of passen-
gers and the rights of an individual who has exclusive
control of an automobile or of its locked compartments.”
Id., at 154. This situation would be similar to the defend-
ant in Jones, supra, who, as Rakas notes, had a reasonable
expectation of privacy in his friend’s apartment because he
“had complete dominion and control over the apartment
and could exclude others from it,” 439 U. S., at 149. Jus-
tice Powell’s observation was also consistent with the
majority’s explanation that “one who owns or lawfully
possesses or controls property will in all likelihood have a
legitimate expectation of privacy by virtue of [the] right to
exclude,” id., at 144, n. 12, an explanation tied to the
majority’s discussion of Jones.
   The Court sees no reason why the expectation of privacy
that comes from lawful possession and control and the
attendant right to exclude would differ depending on
whether the car in question is rented or privately owned
by someone other than the person in current possession of
it, much as it did not seem to matter whether the friend of
                 Cite as: 584 U. S. ____ (2018)          11

                     Opinion of the Court

the defendant in Jones owned or leased the apartment he
permitted the defendant to use in his absence. Both would
have the expectation of privacy that comes with the right
to exclude. Indeed, the Government conceded at oral
argument that an unauthorized driver in sole possession
of a rental car would be permitted to exclude third parties
from it, such as a carjacker. Tr. of Oral Arg. 48–49.
                               2
  The Government further stresses that Byrd’s driving the
rental car violated the rental agreement that Reed signed,
and it contends this violation meant Byrd could not have
had any basis for claiming an expectation of privacy in the
rental car at the time of the search. As anyone who has
rented a car knows, car-rental agreements are filled with
long lists of restrictions. Examples include prohibitions on
driving the car on unpaved roads or driving while using a
handheld cellphone. Few would contend that violating
provisions like these has anything to do with a driver’s
reasonable expectation of privacy in the rental car—as
even the Government agrees. Brief for United States 32.
  Despite this concession, the Government argues that
permitting an unauthorized driver to take the wheel of a
rental car is a breach different in kind from these others,
so serious that the rental company would consider the
agreement “void” the moment an unauthorized driver
takes the wheel. Id., at 4, 15, 16, 27. To begin with, that
is not what the contract says. It states: “Permitting an
unauthorized driver to operate the vehicle is a violation of
the rental agreement. This may result in any and all
coverage otherwise provided by the rental agreement
being void and my being fully responsible for all loss or
damage, including liability to third parties.” App. 24
(emphasis deleted).
  Putting the Government’s misreading of the contract
aside, there may be countless innocuous reasons why an
12                 BYRD v. UNITED STATES

                      Opinion of the Court

unauthorized driver might get behind the wheel of a rental
car and drive it—perhaps the renter is drowsy or inebriated
and the two think it safer for the friend to drive them to
their destination. True, this constitutes a breach of the
rental agreement, and perhaps a serious one, but the
Government fails to explain what bearing this breach of
contract, standing alone, has on expectations of privacy in
the car. Stated in different terms, for Fourth Amendment
purposes there is no meaningful difference between the
authorized-driver provision and the other provisions the
Government agrees do not eliminate an expectation of
privacy, all of which concern risk allocation between pri-
vate parties—violators might pay additional fees, lose
insurance coverage, or assume liability for damage result-
ing from the breach. But that risk allocation has little to
do with whether one would have a reasonable expectation
of privacy in the rental car if, for example, he or she other-
wise has lawful possession of and control over the car.
                               3
   The central inquiry at this point turns on the concept of
lawful possession, and this is where an important qualifi-
cation of Byrd’s proposed rule comes into play. Rakas
makes clear that “ ‘wrongful’ presence at the scene of a
search would not enable a defendant to object to the legal-
ity of the search.” 439 U. S., at 141, n. 9. “A burglar plying
his trade in a summer cabin during the off season,” for
example, “may have a thoroughly justified subjective
expectation of privacy, but it is not one which the law
recognizes as ‘legitimate.’ ” Id., at 143, n. 12. Likewise, “a
person present in a stolen automobile at the time of the
search may [not] object to the lawfulness of the search of
the automobile.” Id., at 141, n. 9. No matter the degree of
possession and control, the car thief would not have a
reasonable expectation of privacy in a stolen car.
   On this point, in its merits brief, the Government as-
                 Cite as: 584 U. S. ____ (2018)          13

                     Opinion of the Court

serts that, on the facts here, Byrd should have no greater
expectation of privacy than a car thief because he inten-
tionally used a third party as a strawman in a calculated
plan to mislead the rental company from the very outset,
all to aid him in committing a crime. This argument is
premised on the Government’s inference that Byrd knew
he would not have been able to rent the car on his own,
because he would not have satisfied the rental company’s
requirements based on his criminal record, and that he
used Reed, who had no intention of using the car for her
own purposes, to procure the car for him to transport
heroin to Pittsburgh.
   It is unclear whether the Government’s allegations, if
true, would constitute a criminal offense in the acquisition
of the rental car under applicable law. And it may be that
there is no reason that the law should distinguish between
one who obtains a vehicle through subterfuge of the type
the Government alleges occurred here and one who steals
the car outright.
   The Government did not raise this argument in the
District Court or the Court of Appeals, however. It relied
instead on the sole fact that Byrd lacked authorization to
drive the car. And it is unclear from the record whether
the Government’s inferences paint an accurate picture of
what occurred. Because it was not addressed in the Dis-
trict Court or Court of Appeals, the Court declines to reach
this question. The proper course is to remand for the
argument and potentially further factual development to
be considered in the first instance by the Court of Appeals
or by the District Court.
                              IV
  The Government argued in its brief in opposition to
certiorari that, even if Byrd had a Fourth Amendment
interest in the rental car, the troopers had probable cause
to believe it contained evidence of a crime when they
14                BYRD v. UNITED STATES

                     Opinion of the Court

initiated their search. If that were true, the troopers may
have been permitted to conduct a warrantless search of
the car in line with the Court’s cases concerning the auto-
mobile exception to the warrant requirement. See, e.g.,
Acevedo, 500 U. S., at 580. The Court of Appeals did not
reach this question because it concluded, as an initial
matter, that Byrd lacked a reasonable expectation of
privacy in the rental car.
   It is worth noting that most courts analyzing the ques-
tion presented in this case, including the Court of Appeals
here, have described it as one of Fourth Amendment
“standing,” a concept the Court has explained is not dis-
tinct from the merits and “is more properly subsumed
under substantive Fourth Amendment doctrine.” Rakas,
supra, at 139.
   The concept of standing in Fourth Amendment cases can
be a useful shorthand for capturing the idea that a person
must have a cognizable Fourth Amendment interest in the
place searched before seeking relief for an unconstitutional
search; but it should not be confused with Article III
standing, which is jurisdictional and must be assessed
before reaching the merits. Arizona Christian School
Tuition Organization v. Winn, 563 U. S. 125, 129 (2011)
(“To obtain a determination on the merits in federal court,
parties seeking relief must show that they have standing
under Article III of the Constitution”); see also Rakas,
supra, at 138–140. Because Fourth Amendment standing
is subsumed under substantive Fourth Amendment doc-
trine, it is not a jurisdictional question and hence need not
be addressed before addressing other aspects of the merits
of a Fourth Amendment claim. On remand, then, the
Court of Appeals is not required to assess Byrd’s reason-
able expectation of privacy in the rental car before, in its
discretion, first addressing whether there was probable
cause for the search, if it finds the latter argument has
been preserved.
                  Cite as: 584 U. S. ____ (2018)           15

                      Opinion of the Court

                              V
  Though new, the fact pattern here continues a well-
traveled path in this Court’s Fourth Amendment jurispru-
dence. Those cases support the proposition, and the Court
now holds, that the mere fact that a driver in lawful pos-
session or control of a rental car is not listed on the rental
agreement will not defeat his or her otherwise reasonable
expectation of privacy. The Court leaves for remand two
of the Government’s arguments: that one who intention-
ally uses a third party to procure a rental car by a fraudu-
lent scheme for the purpose of committing a crime is no
better situated than a car thief; and that probable cause
justified the search in any event. The Court of Appeals
has discretion as to the order in which these questions are
best addressed.
                     *    *     *
  The judgment of the Court of Appeals is vacated, and
the case is remanded for further proceedings consistent
with this opinion.
                                        It is so ordered.
                 Cite as: 584 U. S. ____ (2018)          1

                    THOMAS, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 16–1371
                         _________________


 TERRENCE BYRD, PETITIONER v. UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE THIRD CIRCUIT
                        [May 14, 2018]

   JUSTICE THOMAS, with whom JUSTICE GORSUCH joins,
concurring.
   Although I have serious doubts about the “reasonable
expectation of privacy” test from Katz v. United States,
389 U. S. 347, 360–361 (1967) (Harlan, J., concurring), I
join the Court’s opinion because it correctly navigates our
precedents, which no party has asked us to reconsider. As
the Court notes, Byrd also argued that he should prevail
under the original meaning of the Fourth Amendment
because the police interfered with a property interest that
he had in the rental car. I agree with the Court’s decision
not to review this argument in the first instance. In my
view, it would be especially “unwise” to reach that issue,
ante, at 7, because the parties fail to adequately address
several threshold questions.
   The Fourth Amendment guarantees the people’s right to
be secure from unreasonable searches of “their persons,
houses, papers, and effects.” With this language, the
Fourth Amendment gives “each person . . . the right to be
secure against unreasonable searches and seizures in his
own person, house, papers, and effects.” Minnesota v.
Carter, 525 U. S. 83, 92 (1998) (Scalia, J., concurring).
The issue, then, is whether Byrd can prove that the rental
car was his effect.
   That issue seems to turn on at least three threshold
questions. First, what kind of property interest do indi-
2                 BYRD v. UNITED STATES

                    THOMAS, J., concurring

viduals need before something can be considered “their . . .
effec[t]” under the original meaning of the Fourth
Amendment?       Second, what body of law determines
whether that property interest is present—modern state
law, the common law of 1791, or something else? Third, is
the unauthorized use of a rental car illegal or otherwise
wrongful under the relevant law, and, if so, does that
illegality or wrongfulness affect the Fourth Amendment
analysis?
   The parties largely gloss over these questions, but the
answers seem vitally important to assessing whether Byrd
can claim that the rental car is his effect. In an appropri-
ate case, I would welcome briefing and argument on these
questions.
                 Cite as: 584 U. S. ____ (2018)          1

                     ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 16–1371
                         _________________


 TERRENCE BYRD, PETITIONER v. UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE THIRD CIRCUIT
                        [May 14, 2018]

   JUSTICE ALITO, concurring.
   The Court holds that an unauthorized driver of a rental
car is not always barred from contesting a search of the
vehicle. Relevant questions bearing on the driver’s ability
to raise a Fourth Amendment claim may include: the
terms of the particular rental agreement, see ante, at 11–
12; the circumstances surrounding the rental, ante, at 13;
the reason why the driver took the wheel, ante, at 11–12;
any property right that the driver might have, ante, at 7;
and the legality of his conduct under the law of the State
where the conduct occurred, ante, at 12–13. On remand,
the Court of Appeals is free to reexamine the question
whether petitioner may assert a Fourth Amendment claim
or to decide the appeal on another appropriate ground.
Ante, at 14–15. On this understanding, I join the opinion
of the Court.

```

---

## GROUP: content/cases/Cady v. Dombrowski.md  (`case`, 6 assertions)

### content_page

```
---
title: "Cady v. Dombrowski"
type: case
citation: "413 U.S. 433 (1973)"
parallel_cite: "93 S. Ct. 2523; 37 L. Ed. 2d 706"
neutral_cite: 1973 U.S. LEXIS 48
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-21
docket: 72-586
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cady v. Dombrowski
  varies_by_point: false
  scope_note: "Vehicle caretaking holding intact; Caniglia v. Strom (2021) declined to extend Cady's caretaking rationale to the home."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108850/cady-v-dombrowski/"
  cluster_id: 108850
  opinion_id: 108850
  identity_checked: true
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Anchor"
  - page: "[[Inventory Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[South Dakota v. Opperman]]", "[[Caniglia v. Strom]]", "[[Colorado v. Bertine]]"]
aliases: []
tags: ["case", "fourth-amendment", "community-caretaking", "vehicle-search", "inventory"]
holding: "Origin of the 'community caretaking' concept: police perform many noncriminal caretaking functions with VEHICLES (disabled cars,…"
lake:
  record_id: Cady v. Dombrowski
  status: verified
  projected_at: 2026-07-06
---

# Cady v. Dombrowski

*413 U.S. 433 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dombrowski, an off-duty Chicago police officer, wrecked his car in rural Wisconsin. Local police, who believed department policy required off-duty officers to carry their service revolver and did not find it on him, had the disabled car towed and searched its trunk for the gun — to keep it out of the wrong hands. Instead they found evidence linking Dombrowski to a murder.

## Issue
Whether a warrantless search of an impounded, disabled vehicle for a firearm, undertaken to protect the public rather than to investigate crime, is reasonable under the Fourth Amendment.

## Rule
Police perform many noncriminal functions with vehicles: "Local police officers, unlike federal officers, frequently investigate vehicle accidents in which there is no claim of criminal liability and engage in what, for want of a better term, may be described as community caretaking functions, totally divorced from the detection, investigation, or acquisition of evidence relating to the violation of a criminal statute." — 413 U.S. at 441. ^pin-441

On these facts the caretaking search was reasonable: "Where, as here, the trunk of an automobile, which the officer reasonably believed to contain a gun, was vulnerable to intrusion by vandals, we hold that the search was not 'unreasonable' within the meaning of the Fourth and Fourteenth Amendments." — *Id.* at 448. ^pin-448

## Application
The officer reasonably believed the towed car's trunk held Dombrowski's service revolver, and the disabled vehicle, left at a private lot, was vulnerable to vandals who might take the gun. Searching the trunk to secure the weapon was a reasonable caretaking measure, not a criminal investigation, so the evidence found was admissible.

## Conclusion
The warrantless caretaking search of the vehicle was reasonable; the judgment granting [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the vehicle holding. [[Caniglia v. Strom]] (2021) **declined to extend** *Cady*'s community-caretaking rationale to warrantless entry of the home, stressing the "constitutional difference" between a vehicle and a home; *Cady*'s own holding remains good law.

## Appears on
- [[Community Caretaking]] — *Key — Anchor*

## Sources
- *Cady v. Dombrowski*, 413 U.S. 433 (1973) — https://www.courtlistener.com/opinion/108850/cady-v-dombrowski/ — pinpoints: 441, 448.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "577c4379cf55785c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "413 U.S. 433 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 48", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2523; 37 L. Ed. 2d 706", "title": "Cady v. Dombrowski", "year": "1973"}}
{"assertion_id": "192fbdd15fd9f9f9", "dimension": "support", "kind": "home_role", "locator": {"home": "Community Caretaking"}, "payload": {"home": "Community Caretaking", "role": "Key — Anchor", "title": "Cady v. Dombrowski"}}
{"assertion_id": "a08c2db53999216c", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Related (cross-doctrine)", "title": "Cady v. Dombrowski"}}
{"assertion_id": "d33c555730a2d5d4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Origin of the 'community caretaking' concept: police perform many noncriminal caretaking functions with VEHICLES (disabled cars,…", "title": "Cady v. Dombrowski"}}
{"assertion_id": "1fca964ace397187", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Cady v. Dombrowski", "field_i_validity": "good_law", "scope_note": "Vehicle caretaking holding intact; Caniglia v. Strom (2021) declined to extend Cady's caretaking rationale to the home.", "title": "Cady v. Dombrowski", "varies_by_point": "false"}}
{"assertion_id": "a1be362644b26351", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Cady v. Dombrowski"}}
```

### lake record — Cady v. Dombrowski

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cady v. Dombrowski",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cady v. Dombrowski",
    "case_name_short": "Cady",
    "case_name_full": "Cady, Warden v. Dombrowski",
    "input_case_name": "Cady v. Dombrowski",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-21",
    "year": 1973,
    "docket": "72-586",
    "cluster_id": 108850,
    "lead_opinion_id": 108850,
    "sibling_ids": [
      108850,
      9425411,
      9425412
    ],
    "absolute_url": "/opinion/108850/cady-v-dombrowski/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8993374,
        "score": 10,
        "case_name": "Cady v. Dombrowski"
      },
      {
        "cluster_id": 8992197,
        "score": 10,
        "case_name": "Cady v. Dombrowski"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 433",
      "volume": "413",
      "reporter": "U.S.",
      "page": "433",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2523",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 706",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 48",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "48",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 433",
        "volume": "413",
        "reporter": "U.S.",
        "page": "433",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2523",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 706",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 48",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "48",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 433",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 433",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-441",
      "page": null,
      "quote": "--- # Cady v. Dombrowski *413 U.S. 433 (1973)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dombrowski, an off-duty Chicago police officer, wrecked his car in rural Wisconsin. Local police, who believed department policy required off-duty officers to carry their service revolver and did not find it on him, had the disabled car towed and searched its trunk for the gun \u2014 to keep it out of the wrong hands. Instead they found evidence linking Dombrowski to a murder. ## Issue Whether a warrantless search of an impounded, disabled vehicle for a firearm, undertaken to protect the public rather than to investigate crime, is reasonable under the Fourth Amendment. ## Rule Police perform many noncriminal functions with vehicles:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-448",
      "page": null,
      "quote": "Where, as here, the trunk of an automobile, which the officer reasonably believed to contain a gun, was vulnerable to intrusion by vandals, we hold that the search was not 'unreasonable' within the meaning of the Fourth and Fourteenth Amendments.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cady v. Dombrowski",
    "varies_by_point": false,
    "scope_note": "Vehicle caretaking holding intact; Caniglia v. Strom (2021) declined to extend Cady's caretaking rationale to the home.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Armstrong",
          "cluster_id": 9410756,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4486934,
          "cite": [
            "2018 CO 27",
            "415 P.3d 815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Clarence E. Johnson",
          "cluster_id": 4343883,
          "cite": [
            "208 So. 3d 843",
            "2017 Fla. App. LEXIS 995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tonja Ames v. King County",
          "cluster_id": 4338436,
          "cite": [
            "846 F.3d 340",
            "2017 WL 127563"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tosh Toussaint",
          "cluster_id": 4259133,
          "cite": [
            "838 F.3d 503",
            "2016 U.S. App. LEXIS 17357",
            "2016 WL 5314862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mary Osborne v. State of Indiana",
          "cluster_id": 3203044,
          "cite": [
            "54 N.E.3d 428",
            "2016 WL 2756467"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Parks",
          "cluster_id": 4247757,
          "cite": [
            "2015 COA 158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane1_negative"
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
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
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
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
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
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
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
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Wilson",
          "cluster_id": 118086,
          "cite": [
            "137 L. Ed. 2d 41",
            "117 S. Ct. 882",
            "519 U.S. 408",
            "1997 U.S. LEXIS 1271"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
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
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elders",
          "cluster_id": 2353203,
          "cite": [
            "927 A.2d 1250",
            "192 N.J. 224",
            "2007 N.J. LEXIS 925"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Henrich",
          "cluster_id": 7030666,
          "cite": [
            "39 F.3d 912",
            "1994 WL 596643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins v. California",
          "cluster_id": 110558,
          "cite": [
            "69 L. Ed. 2d 744",
            "101 S. Ct. 2841",
            "453 U.S. 420",
            "1981 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tyronski Johnson",
          "cluster_id": 790485,
          "cite": [
            "410 F.3d 137",
            "2005 U.S. App. LEXIS 10600",
            "2005 WL 1345622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Villamonte-Marquez",
          "cluster_id": 110973,
          "cite": [
            "77 L. Ed. 2d 22",
            "103 S. Ct. 2573",
            "462 U.S. 579",
            "1983 U.S. LEXIS 68",
            "51 U.S.L.W. 4812"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laney v. State",
          "cluster_id": 1427607,
          "cite": [
            "117 S.W.3d 854",
            "2003 Tex. Crim. App. LEXIS 533",
            "2003 WL 22300456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cady v. Dombrowski:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108850 OR 9425411 OR 9425412) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQ2NjgxNjAwMDAwJnM9MzE1MjQwMyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108850+OR+9425411+OR+9425412%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108850 OR 9425411 OR 9425412)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzQmcz0yNzg3NTAwJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108850+OR+9425411+OR+9425412%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108850 OR 9425411 OR 9425412)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 0,
        "triage_snippet_classified": 42
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108850 OR 9425411 OR 9425412)",
    "indexed_citing_opinions": 1591,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108850,
        "count": 1398,
        "count_source": "search"
      },
      {
        "opinion_id": 9425411,
        "count": 237,
        "count_source": "search"
      },
      {
        "opinion_id": 9425412,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2466,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cady-v-dombrowski.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTM0ODYmcz05NTc2MDY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108850+OR+9425411+OR+9425412%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108850,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 104766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 241230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 307314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108850,
        "cited_id": 1848277,
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
    "date_created": "2026-07-04T21:10:52Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:11:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:11:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:15:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:11:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cady v. Dombrowski

```
<div>
<center><b><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U.S. 433</a></span> (1973)</b></center>
<center><h1>CADY, WARDEN<br>
v.<br>
DOMBROWSKI</h1></center>
<center>No. 72-586.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued March 21, 1973.</center>
<center>Decided June 21, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT
<p><span class="star-pagination">*434</span> <i>LeRoy L. Dalton,</i> Assistant Attorney General of Wisconsin, argued the cause for petitioner. With him on the briefs was <i>Robert W. Warren,</i> Attorney General.</p>
<p><i>William J. Mulligan,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./410/952/">410 U. S. 952</a></span>, argued the cause for respondent. With him on the brief was <i>David E. Leichtfuss.</i><sup>[*]</sup></p>
<p>Opinion of the Court by MR. JUSTICE REHNQUIST, announced by MR. JUSTICE BLACKMUN.</p>
<p>Respondent Chester J. Dombrowski, was convicted in a Wisconsin state court of first-degree murder of Herbert McKinney and sentenced to life imprisonment. The conviction was upheld on appeal, <i>State</i> v. <i>Dombrowski,</i> <span class="citation" data-id="1848277"><a href="/opinion/1848277/state-v-dombrowski/" aria-description="Citation for case: State v. Dombrowski">44 Wis. 2d 486</a></span>, <span class="citation" data-id="1848277"><a href="/opinion/1848277/state-v-dombrowski/" aria-description="Citation for case: State v. Dombrowski">171 N. W. 2d 349</a></span> (1969), the Wisconsin Supreme Court rejecting respondent's contention that certain evidence admitted at the trial had been unconstitutionally seized. Respondent then filed a petition for a writ of habeas corpus in federal district court, asserting the same constitutional claim. The District Court denied the petition but the United States Court of Appeals for the Seventh Circuit reversed, holding that one of the searches was unconstitutional under <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964), and the other unconstitutional <span class="star-pagination">*435</span> for unrelated reasons. <span class="citation" data-id="9459018"><a href="/opinion/307314/chester-j-dombrowski-v-elmer-o-cady/" aria-description="Citation for case: Chester J. Dombrowski v. Elmer O. Cady">471 F. 2d 280</a></span> (1972). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./409/1059/">409 U. S. 1059</a></span> (1972).</p>
<p></p>
<h2>I</h2>
<p>On September 9, 1969, respondent was a member of the Chicago, Illinois, police force and either owned or possessed a 1960 Dodge automobile. That day he drove from Chicago to West Bend, Wisconsin, the county seat of Washington County, located some hundred-odd miles northwest of Chicago. He was identified as having been in two taverns in the small town of Kewaskum, Wisconsin, seven miles north of West Bend, during the late evening of September 9 and the early morning of September 10. At some time before noon on the 10th, respondent's automobile became disabled, and he had it towed to a farm owned by his brother in Fond du Lac County, which adjoins Washington County on the north. He then drove back to Chicago early that afternoon with his brother in the latter's car.</p>
<p>Just before midnight of the same day, respondent rented a maroon 1967 Ford Thunderbird at O'Hare Field outside of Chicago, and apparently drove back to Wisconsin early the next morning. A tenant on his brother's farm saw a car answering the description of the rented car pull alongside the disabled 1960 Dodge at approximately 4 a. m. At approximately 9:30 a. m. on September 11, respondent purchased two towels, one light brown and the other blue, from a department store in Kewaskum.</p>
<p>From 7 to 10:15 p. m. of the 11th, respondent was in a steak house or tavern in West Bend. He ate dinner and also drank, apparently quite heavily. He left the tavern and drove the 1967 Thunderbird in a direction away from West Bend toward his brother's farm. On the way, respondent had an accident, with the Thunderbird breaking through a guard rail and crashing into a <span class="star-pagination">*436</span> bridge abutment. A passing motorist drove him into Kewaskum, and, after being let off in Kewaskum, respondent telephoned the police. Two police officers picked him up at a tavern and drove to the scene of the accident. On the way, the officers noticed that respondent appeared to be drunk; he offered three conflicting versions of how the accident occurred.</p>
<p>At the scene, the police observed the 1967 Thunderbird and took various measurements relevant to the accident. Respondent was, in the opinion of the officers, drunk. He had informed them that he was a Chicago police officer. The Wisconsin policemen believed that Chicago police officers were required by regulation to carry their service revolvers at all times. After calling a towtruck to remove the disabled Thunderbird, and not finding the revolver on respondent's person, one of the officers looked into the front seat and glove compartment of that car for respondent's service revolver. No revolver was found. The wrecker arrived and the Thunderbird was towed to a privately owned garage in Kewaskum, approximately seven miles from the West Bend police station. It was left outside by the wrecker, and no police guard was posted. At 11:33 p. m. on the 11th respondent was taken directly to the West Bend police station from the accident scene, and, after being interviewed by an assistant district attorney, to whom respondent again stated he was a Chicago policeman, respondent was formally arrested for drunken driving. Respondent was "in a drunken condition" and "incoherent at times." Because of his injuries sustained in the accident, the same two officers took respondent to a local hospital. He lapsed into an unexplained coma, and a doctor, fearing the possibility of complications, had respondent hospitalized overnight for observation. One of the policemen remained at the hospital as a guard, and the other, Officer Weiss, drove at some time after <span class="star-pagination">*437</span> 2 a. m. on the 12th to the garage to which the 1967 Thunderbird had been towed after the accident.</p>
<p>The purpose of going to the Thunderbird, as developed on the motion to suppress, was to look for respondent's service revolver. Weiss testified that respondent did not have a revolver when he was arrested, and that the West Bend authorities were under the impression that Chicago police officers were required to carry their service revolvers at all times. He stated that the effort to find the revolver was "standard procedure in our department."</p>
<p>Weiss opened the door of the Thunderbird and found, on the floor of the car, a book of Chicago police regulations and, between the two front seats, a flashlight which appeared to have "a few spots of blood on it." He then opened the trunk of the car, which had been locked, and saw various items covered with what was later determined to be type 0 blood. These included a pair of police uniform trousers, a pair of gray trousers, a nightstick with the name "Dombrowski" stamped on it, a raincoat, a portion of a car floor mat, and a towel. The blood on the car mat was moist. The officer removed these items to the police station.</p>
<p>When, later that day, respondent was confronted with the condition of the items discovered in the trunk, he requested the presence of counsel before making any statement. After conferring with respondent, a lawyer told the police that respondent "authorized me to state he believed there was a body lying near the family picnic area at the north end of his brother's farm."</p>
<p>Fond du Lac County police went to the farm and found, in a dump, the body of a male, later identified as the decedent McKinney, clad only in a sportshirt. The deceased's head was bloody; a white sock was found near the body. In observing the area, one officer looked through the window of the disabled 1960 Dodge, located <span class="star-pagination">*438</span> not far from where the body was found, and saw a pillowcase, backseat, and briefcase covered with blood. Police officials obtained, on the evening of the 12th, returnable within 48 hours, warrants to search the 1960 Dodge and the 1967 Thunderbird, as well as orders to impound both automobiles. The 1960 Dodge was examined at the farm on the 12th and then towed to the police garage where it was held as evidence. On the 13th, criminologists came from the Wisconsin Crime Laboratory in Madison and searched the Dodge; they seized the back and front seats, a white sock covered with blood, a part of a bloody rear floor mat, a briefcase, and a front floor mat. A return of the search warrant was filed in the county court on the 14th, but it did not recite that the sock and floor mat had been seized. At a hearing held on the 14th, the sheriff who executed the warrant did not specifically state that these two items had been seized.</p>
<p>At the trial, the State introduced testimony tending to establish that the deceased was first hit over the head and then shot with a .38-caliber gun, dying approximately an hour after the gunshot wound was inflicted; that death occurred at approximately 7 a. m. on the 11th, with a six-hour margin of error either way; that respondent owned two .38-caliber guns; that respondent had type A blood; that the deceased had type O blood and that the bloodstains found in the 1960 Dodge and on the items found in the two cars were type O.</p>
<p>The prosecution introduced the nightstick discovered in the 1967 Thunderbird, and testimony that it had traces of type O blood on it; the portion of the floor mat found in the 1967 car, with testimony that it matched the portion of the floor mat found in the 1960 Dodge; the bloody towel found in the 1967 car, with testimony that it was identical to one of the towels purchased by respondent on the 11th; the police uniform trousers; and the sock <span class="star-pagination">*439</span> found in the 1960 Dodge, with testimony that it was identical in composition and stitching to that found near the body of the deceased.</p>
<p>The State's case was based wholly on circumstantial evidence. The Supreme Court of Wisconsin, in reviewing the conviction on direct appeal, stated that "even though the evidence that led to his conviction was circumstantial, we have seldom seen a stronger collection of such evidence assembled and presented by the prosecution." <i>State</i> v. <i>Dombrowski,</i> <span class="citation" data-id="1848277"><a href="/opinion/1848277/state-v-dombrowski/#507" aria-description="Citation for case: State v. Dombrowski">44 Wis. 2d, at 507</a></span>, <span class="citation" data-id="1848277"><a href="/opinion/1848277/state-v-dombrowski/#360" aria-description="Citation for case: State v. Dombrowski">171 N. W. 2d, at 360</a></span>.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>The ultimate standard set forth in the Fourth Amendment is reasonableness. In construing this command, there has been general agreement that "except in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' unless it has been authorized by a valid search warrant." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). See <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span> (1971). One class of cases which constitutes at least a partial exception to this general rule is automobile searches. Although vehicles are "effects" within the meaning of the Fourth Amendment, "for the purposes of the Fourth Amendment there is a constitutional difference between houses and cars." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970). See <i>Carroll</i> v. <span class="star-pagination">*440</span> <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span> (1925). In <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 59</a></span> (1967), the identical proposition was stated in different language:</p>
<blockquote>"We made it clear in <i>Preston</i> [v. <i>United States</i><i>]</i> that whether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case and pointed out, in particular, that searches of cars that are constantly movable may make the search of a car without a warrant a reasonable one although the result might be the opposite in a search of a home, a store, or other fixed piece of property. <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#366" aria-description="Citation for case: Preston v. United States">376 U. S., at 366-367</a></span>."</blockquote>
<p>While these general principles are easily stated, the decisions of this Court dealing with the constitutionality of warrantless searches, especially when those searches are of vehicles, suggest that this branch of the law is something less than a seamless web.</p>
<p>Since this Court's decision in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), which overruled <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), and held that the provisions of the Fourth Amendment were applicable to the States through the Due Process Clause of the Fourteenth Amendment, the application of Fourth Amendment standards, originally intended to restrict only the Federal Government, to the States presents some difficulty when searches of automobiles are involved. The contact with vehicles by federal law enforcement officers usually, if not always, involves the detection or investigation of crimes unrelated to the operation of a vehicle. Cases such as <i>Carroll</i> v. <i>United States, supra</i><i>,</i> and <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949), illustrate the typical situations in which federal officials come into contact with and search vehicles. In both cases, members of a special federal unit charged with enforcing a particular federal criminal <span class="star-pagination">*441</span> statute stopped and searched a vehicle when they had probable cause to believe that the operator was violating that statute.</p>
<p>As a result of our federal system of government, however, state and local police officers, unlike federal officers, have much more contact with vehicles for reasons related to the operation of vehicles themselves. All States require vehicles to be registered and operators to be licensed. States and localities have enacted extensive and detailed codes regulating the condition and manner in which motor vehicles may be operated on public streets and highways.</p>
<p>Because of the extensive regulation of motor vehicles and traffic, and also because of the frequency with which a vehicle can become disabled or involved in an accident on public highways, the extent of police-citizen contact involving automobiles will be substantially greater than police-citizen contact in a home or office. Some such contacts will occur because the officer may believe the operator has violated a criminal statute, but many more will not be of that nature. Local police officers, unlike federal officers, frequently investigate vehicle accidents in which there is no claim of criminal liability and engage in what, for want of a better term, may be described as community caretaking functions, totally divorced from the detection, investigation, or acquisition of evidence relating to the violation of a criminal statute.</p>
<p>Although the original justification advanced for treating automobiles differently from houses, insofar as warrantless searches of automobiles by federal officers was concerned, was the vagrant and mobile nature of the former, <i>Carroll</i> v. <i>United States, supra</i><i>; </i><i>Brinegar</i> v. <i>United States, supra</i><i>;</i> cf. <i>Coolidge</i> v. <i>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra</a></span></i><i>; </i><i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>,</i> warrantless searches of vehicles by state officers have been sustained in cases in which the possibilities of the vehicle's being removed <span class="star-pagination">*442</span> or evidence in it destroyed were remote, if not nonexistent. See <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968) (District of Columbia police); <i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>.</i> The constitutional difference between searches of and seizures from houses and similar structures and from vehicles stems both from the ambulatory character of the latter and from the fact that extensive, and often noncriminal contact with automobiles will bring local officials in "plain view" of evidence, fruits, or instrumentalities of a crime, or contraband. Cf. <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972).</p>
<p>Here we must decide whether a "search"<sup>[]</sup> of the trunk of the 1967 Ford was unreasonable solely because the local officer had not previously obtained a warrant. And, if that be answered in the negative, we must then determine whether the warrantless search was unreasonable within the meaning of the Fourth and Fourteenth Amendments. In answering these questions, two factual considerations deserve emphasis. First, the police had exercised <span class="star-pagination">*443</span> a form of custody or control over the 1967 Thunderbird. Respondent's vehicle was disabled as a result of the accident, and constituted a nuisance along the highway. Respondent, being intoxicated (and later comatose), could not make arrangements to have the vehicle towed and stored. At the direction of the police, and for elemental reasons of safety, the automobile was towed to a private garage. Second, both the state courts and the District Court found as a fact that the search of the trunk to retrieve the revolver was "standard procedure in [that police] department," to protect the public from the possibility that a revolver would fall into untrained or perhaps malicious hands. Although the trunk was locked, the car was left outside, in a lot seven miles from the police station to which respondent had been taken, and no guard was posted over it. For reasons not apparent from the opinion of the Court of Appeals, that court concluded that as "no further evidence was needed to sustain" the drunk-driving charge, "[t]he search must therefore have been for incriminating evidence of other offenses." <span class="citation" data-id="9459018"><a href="/opinion/307314/chester-j-dombrowski-v-elmer-o-cady/#283" aria-description="Citation for case: Chester J. Dombrowski v. Elmer O. Cady">471 F. 2d, at 283</a></span>. While that court was obligated to exercise its independent judgment on the underlying constitutional issue presented by the facts of this case, it was not free on this record to disregard these findings of fact. Particularly in nonmetropolitan jurisdictions such as those involved here, enforcement of the traffic laws and supervision of vehicle traffic may be a large part of a police officer's job. We believe that the Court of Appeals should have accepted, as did the state courts and the District Court, the findings with respect to Officer Weiss' specific motivation and the fact that the procedure he followed was "standard."</p>
<p>The Court of Appeals relied, and respondent now relies, primarily on <i>Preston</i> v. <i>United States,</i> 376 U. S. 364 <span class="star-pagination">*444</span> (1964), to conclude that the warrantless search was unconstitutional and the seized items inadmissible. In that case, the police received a telephone call at 3 a. m. from a caller who stated that "three suspicious men acting suspiciously" had been in a car in the business district of Newport, Kentucky, for five hours; four policemen investigated and, after receiving evasive explanations and learning that the suspects were unemployed and apparently indigent, arrested the three for vagrancy. The automobile was cursorily searched, then towed to a police station and ultimately to a garage, where it was searched after the three men had been booked. That search revealed two revolvers in the glove compartment; a subsequent search of the trunk resulted in the seizure of various items later admitted in a prosecution for conspiracy to rob a federally insured bank. In that case the respondent attempted to justify the warrantless search of the trunk and seizure of the items therein "as incidental to a lawful arrest." <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States"><i>Id.,</i> at 367</a></span>. The Court rejected the asserted "search incident" justification for the warrantless search in the following terms:</p>
<blockquote>"But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." <i><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Ibid.</a></span></i>
</blockquote>
<p>It would be possible to interpret <i>Preston</i> broadly, and to argue that it stands for the proposition that on those facts there could have been no constitutional justification advanced for the search. But we take the opinion as written, and hold that it stands only for the proposition that the search challenged there could not be justified as one incident to an arrest. See <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>; </i><i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>.</i> We believe that the instant case is controlled by principles <span class="star-pagination">*445</span> that may be extrapolated from <i>Harris</i> v. <i>United States, supra</i><i>,</i> and <i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>.</i></p>
<p>In <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>,</i> petitioner was arrested for robbery. As petitioner's car had been identified leaving the site of the robbery, it was impounded as evidence. A regulation of the District of Columbia Police Department required that an impounded vehicle be searched, that all valuables be removed, and that a tag detailing certain information be placed on the vehicle. In compliance with this regulation, and without a warrant, an officer searched the car and, while opening one of the doors, spotted an automobile registration card, belonging to the victim, lying face up on the metal door stripping. This item was introduced into evidence at petitioner's trial for robbery. In rejecting the contention that the evidence was inadmissible, the Court stated:</p>
<blockquote>"The admissibility of evidence found as a result of a search under the police regulation is not presented by this case. The precise and detailed findings of the District Court, accepted by the Court of Appeals, were to the effect that the discovery of the card was not the result of a search of the car, but of a measure taken to protect the car while it was in police custody. Nothing in the Fourth Amendment requires the police to obtain a warrant in these narrow circumstances.</blockquote>
<blockquote>"Once the door had lawfully been opened, the registration card . . . was plainly visible. It has long been settled that objects falling in the plain view of an officer who has a right to be in the position to have that view are subject to seizure and may be introduced in evidence." <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S., at 236</a></span>.</blockquote>
<p>In <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>,</i> the petitioner was arrested for selling heroin, and his car impounded pending forfeiture proceedings. A week later, a police officer searched the car <span class="star-pagination">*446</span> and found, in the glove compartment, incriminating evidence subsequently admitted at petitioner's trial. This Court upheld the validity of the warrantless search and seizure with the following language:</p>
<blockquote>"This case is not <i>Preston,</i> nor is it controlled by it. Here the officers seized petitioner's car because they were required to do so by state law. They seized it because of the crime for which they arrested petitioner. They seized it to impound it and they had to keep it until forfeiture proceedings were concluded. Their subsequent search of the carwhether the State had `legal title' to it or notwas closely related to the reason petitioner was arrested, the reason his car had been impounded, and the reason it was being retained. The forfeiture of petitioner's car did not take place until over four months after it was lawfully seized. It would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own protection, to search it." <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>.</blockquote>
<p>These decisions, while not on all fours with the instant case, lead us to conclude that the intrusion into the trunk of the 1967 Thunderbird at the garage was not unreasonable within the meaning of the Fourth and Fourteenth Amendments solely because a warrant had not been obtained by Officer Weiss after he left the hospital. The police did not have actual, physical custody of the vehicle as in <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>,</i> but the vehicle had been towed there at the officers' directions. These officers in a rural area were simply reacting to the effect of an accidentone of the recurring practical situations that results from the operation of motor vehicles and with which local police officers must deal every day. The Thunderbird was not parked adjacent <span class="star-pagination">*447</span> to the dwelling place of the owner as in <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), nor simply momentarily unoccupied on a street. Rather, like an obviously abandoned vehicle, it represented a nuisance, and there is no suggestion in the record that the officers' action in exercising control over it by having it towed away was unwarranted either in terms of state law or sound police procedure.</p>
<p>In <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> the justification for the initial intrusion into the vehicle was to safeguard the owner's property, and in <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span></i> it was to guarantee the safety of the custodians. Here the justification, while different, was as immediate and constitutionally reasonable as those in <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>:</i> concern for the safety of the general public who might be endangered if an intruder removed a revolver from the trunk of the vehicle. The record contains uncontradicted testimony to support the findings of the state courts and District Court. Furthermore, although there is no record basis for discrediting such testimony, it was corroborated by the circumstantial fact that at the time the search was conducted Officer Weiss was ignorant of the fact that a murder, or any other crime, had been committed. While perhaps in a metropolitan area the responsibility to the general public might have been discharged by the posting of a police guard during the night, what might be normal police procedure in such an area may be neither normal nor possible in Kewaskum, Wisconsin. The fact that the protection of the public might, in the abstract, have been accomplished by "less intrusive" means does not, by itself, render the search unreasonable. Cf. <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>.</i></p>
<p>The Court's previous recognition of the distinction between motor vehicles and dwelling places leads us to conclude that the type of caretaking "search" conducted here of a vehicle that was neither in the custody nor on <span class="star-pagination">*448</span> the premises of its owner, and that had been placed where it was by virtue of lawful police action, was not unreasonable solely because a warrant had not been obtained. The Framers of the Fourth Amendment have given us only the general standard of "unreasonableness" as a guide in determining whether searches and seizures meet the standard of that Amendment in those cases where a warrant is not required. Very little that has been said in our previous decisions, see <i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>, </i><i>Harris</i> v. <i>United States, supra</i><i>, </i><i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>,</i> and very little that we might say here can usefully refine the language of the Amendment itself in order to evolve some detailed formula for judging cases such as this. Where, as here, the trunk of an automobile, which the officer reasonably believed to contain a gun, was vulnerable to intrusion by vandals, we hold that the search was not "unreasonable" within the meaning of the Fourth and Fourteenth Amendments.</p>
<p></p>
<h2>III</h2>
<p>The Wisconsin Supreme Court ruled that the sock and the portion of the floor mat were validly seized from the 1960 Dodge. The Fond du Lac county officer who looked through the window of the Dodge after McKinney's body had been found saw the bloody seat and briefcase, but not the sock or floor mat. Consequently, these two items were not listed in the application for the warrant, but the Dodge was the item "particularly described" to be searched in the warrant. The warrant was validly issued and the police were authorized to search the car. The reasoning of the Wisconsin Supreme Court was that although these items were not listed to be seized in the warrant, the warrant was valid and in executing it the officers discovered the sock and mat in plain view and therefore could constitutionally seize them without a warrant.</p>
<p><span class="star-pagination">*449</span> The Court of Appeals held that the seizure of the two items on September 13 could not be justified under the plain-view doctrine. The reasoning of that court hinged on its understanding that the warrant to search the Dodge had been returned and was <i>functus officio</i> by the time Officer Mauer of the Crime Laboratory came upon the sock and the floor mat. The court stated:</p>
<blockquote>"There was no continuing authority under the warrant issued the previous night [the 12th]. First, these items were not described in the warrant and presumably were not observed that night [the 12th]. Second, when the warrant was returnedbefore Mauer came on the sceneit was <i>functus officio.</i> A `new ball game,' so to speak, began when Mauer made his `inspection.'" <span class="citation" data-id="9459018"><a href="/opinion/307314/chester-j-dombrowski-v-elmer-o-cady/#286" aria-description="Citation for case: Chester J. Dombrowski v. Elmer O. Cady">471 F. 2d, at 286</a></span>.</blockquote>
<p>The record is so indisputably clear that the return of the warrant was filed on the 14th, not sometime prior to Mauer's search on the 13th, that we are somewhat at a loss to understand how the Court of Appeals arrived at its factual conclusion. The warrant to search the Dodge was issued on the 12th, and, although a return of the warrant was prepared by a Fond du Lac County officer at some time on the 13th (whether before or after Mauer's search is impossible to determine), it was not filed in the state court until the 14th, at which time a hearing was held. The seizures of the sock and the floor mat occurred while a valid warrant was outstanding, and thus could not be considered unconstitutional under the theory advanced below. As these items were constitutionally seized, we do not deem it constitutionally significant that they were not listed in the return of the warrant. The ramification of that "defect," if such it was, is purely a question of state law.</p>
<p>We therefore need not reach the question of whether the seizure of the two items from the Dodge would have <span class="star-pagination">*450</span> been valid because the entire car had been validly seized as evidence and impounded pursuant to a valid warrant, cf. <i>Harris</i> v. <i>United States, supra</i><i>; </i><i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>,</i> or whether a search of the back seat of this car, located as it was in an open field, required a search warrant at all. See <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#59" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 59</a></span> (1924).</p>
<p>The judgment of the Court of Appeals is <i>Reversed.</i></p>
<p>MR. JUSTICE BRENNAN, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE STEWART, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>In upholding the warrantless search of respondent's rented Thunderbird, the Court purports merely to rely on our prior decisions dealing with automobile searches. It is clear to me, however, that nothing in our prior decisions supports either the reasoning or the result of the Court's decision today. I therefore dissent and would hold the search of the Thunderbird unconstitutional under the Fourth and Fourteenth Amendments.</p>
<p>The relevant facts are these. Respondent, an off-duty Chicago policeman, was arrested by police on a charge of drunken driving following a one-car automobile accident in which respondent severely damaged his rented 1967 Thunderbird. The car was towed from the scene of the accident to a private garage and, some two and one-half hours later, one of the arresting officers drove to the garage and, without a search warrant or respondent's consent, conducted a thorough search of the car for the alleged purpose of finding respondent's service revolver which was not on respondent's person and had not been found during an initial search of the car at the scene of the accident. In the trunk of the car, the officer found and seized numerous items that eventually linked respondent to the death of one Herbert McKinney and <span class="star-pagination">*451</span> ultimately contributed to respondent's conviction for murder.</p>
<p>The Court begins its analysis by recognizing, as clearly it must, that the Fourth Amendment's prohibition against "unreasonable searches and seizures" is shaped by the warrant clause, and thus that a warrantless search of private property is per se "unreasonable" under the Fourth Amendment unless within one of the few specifically established and well-delineated exceptions. <i>Almeida-Sanchez</i> v. <i>United States, ante,</i> p. 266; <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span> (1967). At the same time, the Court also recognizes that one of the established exceptions to the warrant requirement is the search of an automobile on the highway where there is probable cause to support the search and "where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925). See also <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970); <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968). But the search of the Thunderbird plainly cannot be sustained under the "automobile exception," for our prior decisions make it clear that where, as in this case, there is no reasonable likelihood that the automobile would or could be moved, the "automobile exception" is simply irrelevant. <i>Coolidge</i> v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#461" aria-description="Citation for case: Coolidge v. New Hampshire"><i>New Hampshire, supra,</i> at 461</a></span>; <i>Carroll</i> v. <i>United States, supra,</i> at 156.</p>
<p>Another established exception to the warrant requirement is a search incident to a valid arrest. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). But the search of the Thunderbird cannot be sustained under this exception, because even assuming that such a search would have been within the permissible scope of a search incident to <span class="star-pagination">*452</span> an arrest for drunken driving, it is clear that under <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#368" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 368</a></span> (1964), "the search was too remote in time or place to have been made as incidental to the arrest."</p>
<p>A third exception to the warrant requirement is the seizure of evidence in "plain view." Thus, in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968), we upheld the seizure of an automobile registration card that fell within plain view of a police officer as he opened the door of an impounded automobile to roll up the windows. But, as we cautioned in <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Coolidge, supra,</i> at 466</a></span>, "[w]hat the `plain view' cases have in common is that the police officer in each of them had a prior justification for an intrusion in the course of which he came inadvertently across a piece of evidence incriminating the accused." In <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>,</i> the prior justification for the intrusion by the police was to roll up the windows and lock the doors "to protect the car while it was in police custody." <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S., at 236</a></span>. "[T]he discovery of the card was not the result of a search," we said, and "in these narrow circumstances" the "plain view" exception to the warrant requirement was fully applicable. In the present case, however, the sole purpose for the initial intrusion into the vehicle was to <i>search</i> for the gun. Thus, the seizure of the evidence from the trunk of the car can be sustained under the "plain view" doctrine only if the search for the gun was itself constitutional. Reliance on the "plain view" doctrine in this case is therefore misplaced since the antecedent search cannot be sustained.</p>
<p>Another exception to the warrant requirement is that which sustains a search in connection with the seizure of an automobile for purposes of forfeiture proceedings. In <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967), the Court upheld the warrantless search of an automobile after it had been lawfully impounded pursuant to a California statute mandating the seizure and forfeiture of any <span class="star-pagination">*453</span> vehicle used to facilitate the possession or transportation of narcotics. There, however, the police were authorized to treat the car in their custody as if it were their own, and the search was sustainable as an integral part of their right of retention. This case, of course, is poles away from <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>.</i> The Thunderbird was not subject to forfeiture proceedings. On the contrary, ownership of the car remained exclusively in respondent's lessor and the sole reason that the police took even temporary possession of the car was to remove it from the highway until respondent could claim it.</p>
<p>Clearly, therefore, the Court's decision today finds no support in any of the established exceptions. The police knew what they were looking for and had ample opportunity to obtain a warrant. Under those circumstances, our prior decisions make it clear that the Fourth Amendment required the police to obtain a warrant prior to the search. <i>Carroll</i> v. <i>United States, supra,</i> at 156. Thus, despite the Court's asserted adherence to the principles of our prior decisions, in fact the decision rests on a subjective view of what is deemed acceptable in the way of investigative functions performed by rural police officers. But the applicability of the Fourth Amendment cannot turn on fine-line distinctions between criminal and investigative functions. On the contrary, "[i]t is surely anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior," <i>Camara</i> v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Municipal Court, supra,</i> at 530</a></span>, for "[t]he basic purpose of [the Fourth] Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 528</a></span>. Thus, the fact that the professed purpose of the contested search was to protect the public safety rather than to gain incriminating evidence <span class="star-pagination">*454</span> does not of itself eliminate the necessity for compliance with the warrant requirement. Although a valid public interest may establish probable cause to search, <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara, supra,</a></span></i> and <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), make clear that, absent exigent circumstances, the search must be conducted pursuant to a "suitably restricted search warrant." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 539</a></span>. See also <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>.</i> And certainly there were no exigent circumstances to justify the warrantless search made of the Thunderbird. For even assuming that the officer had reason to believe that respondent's service revolver was in the Thunderbird, the police had left the car in the custody of a private garage and did not return to look for the gun until two and one-half hours later. Moreover, although the arresting officers were at all times aware that respondent was an off-duty Chicago policeman, the officers never once inquired of respondent as to whether he was carrying a gun and, if so, where it was located. I can only conclude, therefore, that what the Court does today in the name of an investigative automobile search is in fact a serious departure from established Fourth Amendment principles. And since in my view that departure is totally unjustified, I would affirm the judgment of the Court of Appeals invalidating the search of the Thunderbird and remand the case to the District Court for determination whether the evidence seized during the search of the Dodge and the farm was the fruit of the unlawful search of the Thunderbird. See <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<h2>NOTES</h2>
<p>[*]  <i>Robert L. Shevin,</i> Attorney General, and <i>A. S. Johnston,</i> Assistant Attorney General, filed a brief for the State of Florida as <i>amicus curiae</i> urging reversal.</p>
<p>[]  Petitioner argued before this Court that unlocking the trunk of the Ford did not constitute a "search" within the meaning of the Fourth Amendment. The thesis is that only an intrusion, into an area in which an individual has a reasonable expectation of privacy, with the specific intent of discovering evidence of a crime constitutes a search. Compare <i>Haerr</i> v. <i>United States,</i> <span class="citation" data-id="241230"><a href="/opinion/241230/charles-spencer-haerr-v-united-states/" aria-description="Citation for case: Charles Spencer Haerr v. United States">240 F. 2d 533</a></span> (CA5 1957), with <i>District of Columbia</i> v. <i>Little,</i> 85 U. S. App. D. C. 242, <span class="citation" data-id="9442232"><a href="/opinion/223783/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">178 F. 2d 13</a></span> (1949), aff'd on other grounds, <span class="citation" data-id="104766"><a href="/opinion/104766/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">339 U. S. 1</a></span> (1950). But see <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). Arguing that the officer's conduct constituted an "inspection" rather than a "search," petitioner relies on our decision in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968), to validate the initial intrusion into the trunk, and then the plain-view doctrine to justify the warrantless seizure of the items.
</p>
<p>We need not decide this issue. Petitioner conceded in the Court of Appeals that this intrusion was a search. Inasmuch as we believe that <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and other decisions control this case even if the intrusion is characterized as a search, we need not deal with petitioner's belated contention.</p>

</div>
```

---

## GROUP: content/cases/California v. Acevedo.md  (`case`, 6 assertions)

### content_page

```
---
title: "California v. Acevedo"
type: case
citation: "500 U.S. 565 (1991)"
parallel_cite: "111 S. Ct. 1982; 114 L. Ed. 2d 619"
neutral_cite: 1991 U.S. LEXIS 3016
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-06-03
docket: 89-1690
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-05-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: California v. Acevedo
  varies_by_point: false
  scope_note: "Adopted a unified container rule, overruling Arkansas v. Sanders; Acevedo itself is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112608/california-v-acevedo/"
  cluster_id: 112608
  opinion_id: 112608
  identity_checked: true
homes:
  - page: "[[Searching Effects and Containers]]"
    role: "Key — Container unification"
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[United States v. Ross]]", "[[United States v. Chadwick]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "containers", "probable-cause"]
holding: "Unified rule for containers in vehicles: police may search a container in a car without a warrant where they have PC to believe it holds…"
lake:
  record_id: California v. Acevedo
  status: verified
  projected_at: 2026-07-06
---

# California v. Acevedo

*500 U.S. 565 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police watched Acevedo leave an apartment they knew contained marijuana, carrying a brown paper bag the size of the marijuana packages. He put the bag in his car's trunk and drove off. Officers stopped the car, opened the trunk and the bag, and found marijuana. They had probable cause as to the bag but not necessarily as to the rest of the car.

## Issue
Whether police may search a container located in a vehicle without a warrant when they have probable cause to believe the container holds contraband, even if they lack probable cause to search the entire vehicle.

## Rule
"We therefore interpret *Carroll* as providing one rule to govern all automobile searches. The police may search an automobile and the containers within it where they have probable cause to believe contraband or evidence is contained." — 500 U.S. at 580. ^pin-580

## Application
The officers had probable cause to believe the brown paper bag in Acevedo's trunk held marijuana. Under the unified rule, that probable cause justified the warrantless search of the bag where it sat in the car; they did not need a warrant or separate probable cause as to the whole vehicle.

## Conclusion
The warrantless search of the container was permissible; the judgment suppressing the marijuana was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Acevedo*. It **overruled** *[[Arkansas v. Sanders]]* and replaced the prior container/vehicle distinction with one rule, building on [[Carroll v. United States]] and [[United States v. Ross]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *California v. Acevedo*, 500 U.S. 565 (1991) — https://www.courtlistener.com/opinion/112608/california-v-acevedo/ — pinpoint: 580.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f0726afda53f8196", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "500 U.S. 565 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 3016", "official_citation_present": true, "parallel_cite": "111 S. Ct. 1982; 114 L. Ed. 2d 619", "title": "California v. Acevedo", "year": "1991"}}
{"assertion_id": "2566e1dbc64e68bf", "dimension": "support", "kind": "home_role", "locator": {"home": "Searching Effects and Containers"}, "payload": {"home": "Searching Effects and Containers", "role": "Key — Container unification", "title": "California v. Acevedo"}}
{"assertion_id": "428dfa8e26009369", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Unified rule for containers in vehicles: police may search a container in a car without a warrant where they have PC to believe it holds…", "title": "California v. Acevedo"}}
{"assertion_id": "83ccf01abc2a76e2", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "California v. Acevedo"}}
{"assertion_id": "29db122f243f5170", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "California v. Acevedo"}}
{"assertion_id": "55e18ba0d62fc55b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-05-30", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "California v. Acevedo", "field_i_validity": "good_law", "scope_note": "Adopted a unified container rule, overruling Arkansas v. Sanders; Acevedo itself is good law.", "title": "California v. Acevedo", "varies_by_point": "false"}}
```

### lake record — California v. Acevedo

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Acevedo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "California v. Acevedo",
    "case_name_short": "Acevedo",
    "case_name_full": "California v. Acevedo",
    "input_case_name": "California v. Acevedo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-06-03",
    "year": 1991,
    "docket": "89-1690",
    "cluster_id": 112608,
    "lead_opinion_id": 112608,
    "sibling_ids": [
      112608,
      9432308,
      9432309,
      9432310,
      9432311
    ],
    "absolute_url": "/opinion/112608/california-v-acevedo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "500 U.S. 565",
      "volume": "500",
      "reporter": "U.S.",
      "page": "565",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1982",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1982",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 619",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 3016",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3016",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "500 U.S. 565",
        "volume": "500",
        "reporter": "U.S.",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1982",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1982",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 619",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "619",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 3016",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3016",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "500 U.S. 565",
    "official_selection": {
      "court_class": "scotus",
      "selected": "500 U.S. 565",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-580",
      "page": null,
      "quote": "--- # California v. Acevedo *500 U.S. 565 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police watched Acevedo leave an apartment they knew contained marijuana, carrying a brown paper bag the size of the marijuana packages. He put the bag in his car's trunk and drove off. Officers stopped the car, opened the trunk and the bag, and found marijuana. They had probable cause as to the bag but not necessarily as to the rest of the car. ## Issue Whether police may search a container located in a vehicle without a warrant when they have probable cause to believe the container holds contraband, even if they lack probable cause to search the entire vehicle. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-05-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "California v. Acevedo",
    "varies_by_point": false,
    "scope_note": "Adopted a unified container rule, overruling Arkansas v. Sanders; Acevedo itself is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane1_negative"
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
        "journal_ref": "California v. Acevedo:lane1_negative"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lampf, Pleva, Lipkind, Prupis & Petigrow v. Gilbertson",
          "cluster_id": 112628,
          "cite": [
            "115 L. Ed. 2d 321",
            "111 S. Ct. 2773",
            "501 U.S. 350",
            "1991 U.S. LEXIS 3629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muscarello v. United States",
          "cluster_id": 118224,
          "cite": [
            "141 L. Ed. 2d 111",
            "118 S. Ct. 1911",
            "524 U.S. 125",
            "1998 U.S. LEXIS 3879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wayne Gaskin, AKA \"Atiba,\" and Al Castle",
          "cluster_id": 785776,
          "cite": [
            "364 F.3d 438",
            "2004 U.S. App. LEXIS 7440",
            "2004 WL 818734"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gomez",
          "cluster_id": 2613548,
          "cite": [
            "932 P.2d 1",
            "122 N.M. 777",
            "1997 NMSC 006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Thompson",
          "cluster_id": 2630185,
          "cite": [
            "231 P.3d 289",
            "49 Cal. 4th 79",
            "109 Cal. Rptr. 3d 549",
            "2010 Cal. LEXIS 4884"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nevada v. Hicks",
          "cluster_id": 118454,
          "cite": [
            "150 L. Ed. 2d 398",
            "121 S. Ct. 2304",
            "533 U.S. 353",
            "2001 U.S. LEXIS 4669",
            "2001 Daily Journal DAR 6461",
            "14 Fla. L. Weekly Fed. S 430",
            "69 U.S.L.W. 4528",
            "2001 Cal. Daily Op. Serv. 5248",
            "2001 Colo. J. C.A.R. 3522"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ladson",
          "cluster_id": 1191947,
          "cite": [
            "979 P.2d 833"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reyes",
          "cluster_id": 1444172,
          "cite": [
            "968 P.2d 445",
            "80 Cal. Rptr. 2d 734",
            "19 Cal. 4th 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. United States",
          "cluster_id": 4497658,
          "cite": [
            "584 U.S. 395",
            "138 S. Ct. 1518",
            "200 L. Ed. 2d 805",
            "2018 U.S. LEXIS 2803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
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
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bruce Carneil Webster, A/K/A B-Love",
          "cluster_id": 759707,
          "cite": [
            "162 F.3d 308"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bullock",
          "cluster_id": 1599814,
          "cite": [
            "485 N.W.2d 866",
            "440 Mich. 15"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "California v. Acevedo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112608 OR 9432308 OR 9432309 OR 9432310 OR 9432311) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzY2ODQ4MDAwMDAwJnM9MjcwMjY2MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112608+OR+9432308+OR+9432309+OR+9432310+OR+9432311%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(112608 OR 9432308 OR 9432309 OR 9432310 OR 9432311)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTYmcz01ODgxMzAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112608+OR+9432308+OR+9432309+OR+9432310+OR+9432311%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112608 OR 9432308 OR 9432309 OR 9432310 OR 9432311)",
        "reviewed": 38,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 38,
        "triage_read": 0,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112608 OR 9432308 OR 9432309 OR 9432310 OR 9432311)",
    "indexed_citing_opinions": 854,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112608,
        "count": 726,
        "count_source": "search"
      },
      {
        "opinion_id": 9432308,
        "count": 142,
        "count_source": "search"
      },
      {
        "opinion_id": 9432309,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432310,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432311,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1409,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/california-v-acevedo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4Nzg3NzEmcz05OTk3OTMzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112608+OR+9432308+OR+9432309+OR+9432310+OR+9432311%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9432311,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 1666834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 9565373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432311,
        "cited_id": 9731130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 84781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 3579530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 5473240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 8373743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 9419996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432309,
        "cited_id": 9426247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 84781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 109615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 1666834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 3579530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 5473240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 8373743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 9426247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 9432308,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 9565373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112608,
        "cited_id": 9731130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 109615,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 111405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 112393,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 9431349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9432308,
        "cited_id": 9731130,
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
    "date_created": "2026-07-04T21:15:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T21:15:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T21:15:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T21:19:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T21:15:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — California v. Acevedo (truncated)

```
<div>
<center><b><span class="citation" data-id="9432308"><a href="/opinion/112608/california-v-acevedo/" aria-description="Citation for case: California v. Acevedo">500 U.S. 565</a></span> (1991)</b></center>
<center><h1>CALIFORNIA<br>
v.<br>
ACEVEDO</h1></center>
<center>No. 89-1690.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 8, 1991.</center>
<center>Decided May 30, 1991.</center>
CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, FOURTH APPELLATE DISTRICT
<p><span class="star-pagination">*566</span> <i>Robert M. Foster,</i> Supervising Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>John K. Van de Kamp,</i> Attorney General, <i>Richard B. Iglehart,</i> Chief Assistant Attorney General, <i>Harley D. Mayfield,</i> Senior Assistant Attorney General, and <i>Frederick R. Millar,</i> Supervising Deputy Attorney General.</p>
<p><i>Frederick Westcott Anderson</i> argued the cause for respondent. With him on the brief was <i>Jan Walls Anderson.</i></p>
<p>JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case requires us once again to consider the so-called "automobile exception" to the warrant requirement of the Fourth Amendment and its application to the search of a closed container in the trunk of a car.</p>
<p></p>
<h2>I</h2>
<p>On October 28, 1987, Officer Coleman of the Santa Ana, Cal., Police Department received a telephone call from a federal <span class="star-pagination">*567</span> drug enforcement agent in Hawaii. The agent informed Coleman that he had seized a package containing marijuana which was to have been delivered to the Federal Express Office in Santa Ana and which was addressed to J. R. Daza at 805 West Stevens Avenue in that city. The agent arranged to send the package to Coleman instead. Coleman then was to take the package to the Federal Express office and arrest the person who arrived to claim it.</p>
<p>Coleman received the package on October 29, verified its contents, and took it to the Senior Operations Manager at the Federal Express office. At about 10:30 a.m. on October 30, a man, who identified himself as Jamie Daza, arrived to claim the package. He accepted it and drove to his apartment on West Stevens. He carried the package into the apartment.</p>
<p>At 11:45 a.m., officers observed Daza leave the apartment and drop the box and paper that had contained the marijuana into a trash bin. Coleman at that point left the scene to get a search warrant. About 12:05 p.m., the officers saw Richard St. George leave the apartment carrying a blue knapsack which appeared to be half full. The officers stopped him as he was driving off, searched the knapsack, and found 1½ pounds of marijuana.</p>
<p>At 12:30 p.m., respondent Charles Steven Acevedo arrived. He entered Daza's apartment, stayed for about 10 minutes, and reappeared carrying a brown paper bag that looked full. The officers noticed that the bag was the size of one of the wrapped marijuana packages sent from Hawaii. Acevedo walked to a silver Honda in the parking lot. He placed the bag in the trunk of the car and started to drive away. Fearing the loss of evidence, officers in a marked police car stopped him. They opened the trunk and the bag, and found marijuana.<sup>[1]</sup></p>
<p><span class="star-pagination">*568</span> Respondent was charged in state court with possession of marijuana for sale, in violation of Cal. Health &amp; Safety Code Ann. § 11359 (West Supp. 1991). App. 2. He moved to suppress the marijuana found in the car. The motion was denied. He then pleaded guilty but appealed the denial of the suppression motion.</p>
<p>The California Court of Appeal, Fourth District, concluded that the marijuana found in the paper bag in the car's trunk should have been suppressed. <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/" aria-description="Citation for case: People v. Acevedo">216 Cal. App. 3d 586</a></span>, <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/" aria-description="Citation for case: People v. Acevedo">265 Cal. Rptr. 23</a></span> (1990). The court concluded that the officers had probable cause to believe that the paper bag contained drugs but lacked probable cause to suspect that Acevedo's car, itself, otherwise contained contraband. Because the officers' probable cause was directed specifically at the bag, the court held that the case was controlled by <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), rather than by <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982). Although the court agreed that the officers could seize the paper bag, it held that, under <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> they could not open the bag without first obtaining a warrant for that purpose. The court then recoguized "the anomalous nature" of the dichotomy between the rule in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and the rule in <i>Ross.</i> <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#592" aria-description="Citation for case: People v. Acevedo">216 Cal. App. 3d, at 592</a></span>, <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#27" aria-description="Citation for case: People v. Acevedo">265 Cal. Rptr., at 27</a></span>. That dichotomy dictates that if there is probable cause to search a car, then the entire carincluding any closed container found therein  may be searched without a warrant, but if there is probable cause only as to a container in the car, the container may be held but not searched until a warrant is obtained.</p>
<p>The Supreme Court of California denied the State's petition for review. App. E to Pet. for Cert. 33. On May 14, 1990, JUSTICE O'CONNOR stayed enforcement of the Court of Appeal's judgment pending the disposition of the State's petition for certiorari, and, if that petition were granted, the issuance of the mandate of this Court.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./498/807/">498 U. S. 807</a></span> (1990), to reexamine the law applicable to a closed container in an automobile, a <span class="star-pagination">*569</span> subject that has troubled courts and law enforcement officers since it was first considered in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>.</i></p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment protects the "right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." Contemporaneously with the adoption of the Fourth Amendment, the First Congress, and, later, the Second and Fourth Congresses, distinguished between the need for a warrant to search for contraband concealed in "a dwelling house or similar place" and the need for a warrant to search for contraband concealed in a movable vessel. See <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#151" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 151</a></span> (1925). See also <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#623" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 623-624</a></span> (1886). In <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> this Court established an exception to the warrant requirement for moving vehicles, for it recognized</p>
<blockquote>"a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>.</blockquote>
<p>It therefore held that a warrantless search of an automobile, based upon probable cause to believe that the vehicle contained evidence of crime in the light of an exigency arising out of the likely disappearance of the vehicle, did not contravene the Warrant Clause of the Fourth Amendment. See <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States"><i>id.,</i> at 158-159</a></span>.</p>
<p>The Court refined the exigency requirement in <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), when it held that the existence of exigent circumstances was to be determined at the time the automobile is seized. The car search at issue in <span class="star-pagination">*570</span> <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> took place at the police station, where the vehicle was immobilized, some time after the driver had been arrested. Given probable cause and exigent circumstances at the time the vehicle was first stopped, the Court held that the later warrantless search at the station passed constitutional muster. The validity of the later search derived from the ruling in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> that an immediate search without a warrant at the moment of seizure would have been permissible. See <i>Chambers,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 51</a></span>. The Court reasoned in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> that the police could search later whenever they could have searched earlier, had they so chosen. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Id.,</i> at 51-52</a></span>. Following <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> if the police have probable cause to justify a warrantless seizure of an automobile on a public roadway, they may conduct either an immediate or a delayed search of the vehicle.</p>
<p>In <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span>, decided in 1982, we held that a warrantless search of an automobile under the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine could include a search of a container or package found inside the car when such a search was supported by probable cause. The warrantless search of Ross' car occurred after an informant told the police that he had seen Ross complete a drug transaction using drugs stored in the trunk of his car. The police stopped the car, searched it, and discovered in the trunk a brown paper bag containing drugs. We decided that the search of Ross' car was not unreasonable under the Fourth Amendment: "The scope of a warrantless search based on probable cause is no narrowerand no broaderthan the scope of a search authorized by a warrant supported by probable cause." <i>Id.,</i> at 823. Thus, "[i]f probable cause justifies the search of a lawfully stopped vehicle, it justifies the search of every part of the vehicle and its contents that may conceal the object of the search." <i>Id.,</i> at 825. In <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> therefore, we clarified the scope of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine as properly including a "probing search" of compartments and containers within the automobile so long as the search is supported by probable cause. <i>Id.,</i> at 800.</p>
<p><span class="star-pagination">*571</span> In addition to this clarification, <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> distinguished the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine from the separate rule that governed the search of closed containers. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>. The Court had announced this separate rule, unique to luggage and other closed packages, bags, and containers, in <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). In <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> federal narcotics agents had probable cause to believe that a 200-pound double-locked footlocker contained marijuana. The agents tracked the locker as the defendants removed it from a train and carried it through the station to a waiting car. As soon as the defendants lifted the locker into the trunk of the car, the agents arrested them, seized the locker, and searched it. In this Court, the United States did not contend that the locker's brief contact with the automobile's trunk sufficed to make the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine applicable. Rather, the United States urged that the search of movable luggage could be considered analogous to the search of an automobile. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-12</a></span>.</p>
<p>The Court rejected this argument because, it reasoned, a person expects more privacy in his luggage and personal effects than he does in his automobile. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 13</a></span>. Moreover, it concluded that as "may often not be the case when automobiles are seized," secure storage facilities are usually available when the police seize luggage. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 13, n. 7</a></span>.</p>
<p>In <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), the Court extended <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i>'s rule to apply to a suitcase actually being transported in the trunk of a car. In <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> the police had probable cause to believe a suitcase contained marijuana. They watched as the defendant placed the suitcase in the trunk of a taxi and was driven away. The police pursued the taxi for several blocks, stopped it, found the suitcase in the trunk, and searched it. Although the Court had applied the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine to searches of integral parts of the automobile itself, (indeed, in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> contraband whiskey was in the upholstery of the seats, see <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#136" aria-description="Citation for case: Carroll v. United States">267 U. S., at 136</a></span>), it did not extend the doctrine to the warrantless search of personal luggage <span class="star-pagination">*572</span> "merely because it was located in an automobile lawfully stopped by the police." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#765" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 765</a></span>. Again, the <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> majority stressed the heightened privacy expectation in personal luggage and concluded that the presence of luggage in an automobile did not diminish the owner's expectation of privacy in his personal items. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#764" aria-description="Citation for case: Arkansas v. Sanders"><i>Id.,</i> at 764-765</a></span>. Cf. <i>California</i> v. <i>Carney,</i> <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U. S. 386</a></span> (1985).</p>
<p>In <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> the Court endeavored to distinguish between <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> which governed the <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> automobile search, and <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> which governed the <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> automobile search. It held that the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine covered searches of automobiles when the police had probable cause to search an entire vehicle, but that the <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> doctrine governed searches of luggage when the officers had probable cause to search only a container within the vehicle. Thus, in a <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> situation, the police could conduct a reasonable search under the Fourth Amendment without obtaining a warrant, whereas in a <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> situation, the police had to obtain a warrant before they searched.</p>
<p>JUSTICE STEVENS is correct, of course, that <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> involved the scope of an automobile search. See <i>post,</i> at 592. <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> held that closed containers encountered by the police during a warrantless search of a car pursuant to the automobile exception could also be searched. Thus, this Court in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> took the critical step of saying that closed containers in cars could be searched without a warrant because of their presence within the automobile. Despite the protection that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> purported to extend to closed containers, the privacy interest in those closed containers yielded to the broad scope of an automobile search.</p>
<p></p>
<h2>III</h2>
<p>The facts in this case closely resemble the facts in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>.</i> In <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> the police had probable cause to believe that drugs were stored in the trunk of a particular car. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#800" aria-description="Citation for case: United States v. Ross">456 U. S., at 800</a></span>. Here, the California Court of Appeal concluded that the police had probable cause to believe that respondent was <span class="star-pagination">*573</span> carrying marijuana in a bag in his car's trunk.<sup>[2]</sup> <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#590" aria-description="Citation for case: People v. Acevedo">216 Cal. App. 3d, at 590</a></span>, <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#25" aria-description="Citation for case: People v. Acevedo">265 Cal. Rptr., at 25</a></span>. Furthermore, for what it is worth, in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> as here, the drugs in the trunk were contained in a brown paper bag.</p>
<p>This Court in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> rejected <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i>'s distinction between containers and cars. It concluded that the expectation of privacy in one's vehicle is equal to one's expectation of privacy in the container, and noted that "the privacy interests in a car's trunk or glove compartment may be no less than those in a movable container." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#823" aria-description="Citation for case: United States v. Ross">456 U. S., at 823</a></span>. It also recognized that it was arguable that the same exigent circumstances that permit a warrantless search of an automobile would justify the warrantless search of a movable container. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross"><i>Id.,</i> at 809</a></span>. In deference to the rule of <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> however, the Court put that question to one side. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#809" aria-description="Citation for case: Arkansas v. Sanders"><i>Id.,</i> at 809-810</a></span>. It concluded that the time and expense of the warrant process would be misdirected if the police could search every cubic inch of an automobile until they discovered a paper sack, at which point the Fourth Amendment required them to take the sack to a magistrate for permission to look inside. We now must decide the question deferred in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>:</i> whether the Fourth Amendment requires the police to obtain a warrant to open the sack in a movable vehicle simply because they lack probable cause to search the entire car. We conclude that it does not.</p>
<p></p>
<h2>IV</h2>
<p>Dissenters in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> asked why the suitcase in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> was "more private, less difficult for police to seize and store, or in <span class="star-pagination">*574</span> any other relevant respect more properly subject to the warrant requirement, than a container that police discover in a probable-cause search of an entire automobile?" <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#839" aria-description="Citation for case: Arkansas v. Sanders"><i>Id.,</i> at 839-840</a></span>. We now agree that a container found after a general search of the automobile and a container found in a car after a limited search for the container are equally easy for the police to store and for the suspect to hide or destroy. In fact, we see no principled distinction in terms of either the privacy expectation or the exigent circumstances between the paper bag found by the police in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> and the paper bag found by the police here. Furthermore, by attempting to distinguish between a container for which the police are specifically searching and a container which they come across in a car, we have provided only minimal protection for privacy and have impeded effective law enforcement.</p>
<p>The line between probable cause to search a vehicle and probable cause to search a package in that vehicle is not always clear, and separate rules that govern the two objects to be searched may enable the police to broaden their power to make warrantless searches and disserve privacy interests. We noted this in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> in the context of a search of an entire vehicle. Recognizing that under <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> the "entire vehicle itself . . . could be searched without a warrant," we concluded that "prohibiting police from opening immediately a container in which the object of the search is most likely to be found and instead forcing them first to comb the entire vehicle would actually exacerbate the intrusion on privacy interests." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross">456 U. S., at 821, n. 28</a></span>. At the moment when officers stop an automobile, it may be less than clear whether they suspect with a high degree of certainty that the vehicle contains drugs in a bag or simply contains drugs. If the police know that they may open a bag only if they are actually searching the entire car, they may search more extensively <span class="star-pagination">*575</span> than they otherwise would in order to establish the general probable cause required by <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>.</i></p>
<p>Such a situation is not farfetched. In <i>United States</i> v. <i>Johns,</i> <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">469 U. S. 478</a></span> (1985), Customs agents saw two trucks drive to a private airstrip and approach two small planes. The agents drew near the trucks, smelled marijuana, and then saw in the backs of the trucks packages wrapped in a manner that marijuana smugglers customarily employed. The agents took the trucks to headquarters and searched the packages without a warrant. <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#481" aria-description="Citation for case: United States v. Johns"><i>Id.,</i> at 481</a></span>. Relying on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the defendants argued that the search was unlawful. <i>Id.,</i> at 482. The defendants contended that <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> was inapplicable because the agents lacked probable cause to search anything but the packages themselves and supported this contention by noting that a search of the entire vehicle never occurred. <i>Id.,</i> at 483. We rejected that argument and found <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> inapposite because the agents had probable cause to search the entire body of each truck, although they had chosen not to do so. <i>Id.,</i> at 482-483. We cannot see the benefit of a rule that requires law enforcement officers to conduct a more intrusive search in order to justify a less intrusive one.</p>
<p>To the extent that the <i>Chadwick-Sanders</i> rule protects privacy, its protection is minimal. Law enforcement officers may seize a container and hold it until they obtain a search warrant. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>. "Since the police, by hypothesis, have probable cause to seize the property, we can assume that a warrant will be routinely forthcoming in the overwhelming majority of cases." <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#770" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 770</a></span> (dissenting opinion). And the police often will be able to search containers without a warrant, despite the <i>Chadwick-Sanders</i> rule, as a search incident to a lawful arrest. In <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), the Court said:</p>
<blockquote>
<span class="star-pagination">*576</span> "[W]e hold that when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.</blockquote>
<blockquote>"It follows from this conclusion that the police may also examine the contents of any containers found within the passenger compartment." <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><i>Id.,</i> at 460</a></span> (footnote omitted).</blockquote>
<p>Under <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>,</i> the same probable cause to believe that a container holds drugs will allow the police to arrest the person transporting the container and search it.</p>
<p>Finally, the search of a paper bag intrudes far less on individual privacy than does the incursion sanctioned long ago in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i> In that case, prohibition agents slashed the upholstery of the automobile. This Court nonetheless found their search to be reasonable under the Fourth Amendment. If destroying the interior of an automobile is not unreasonable, we cannot conclude that looking inside a closed container is. In light of the minimal protection to privacy afforded by the <i>Chadwick-Sanders</i> rule, and our serious doubt whether that rule substantially serves privacy interests, we now hold that the Fourth Amendment does not compel separate treatment for an automobile search that extends only to a container within the vehicle.</p>
<p></p>
<h2>V</h2>
<p>The <i>Chadwick-Sanders</i> rule not only has failed to protect privacy but also has confused courts and police officers and impeded effective law enforcement. The conflict between the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine cases and the <i>Chadwick-Sanders</i> line has been criticized in academic commentary. See, <i>e. g.,</i> Gardner, Searches and Seizures of Automobiles and Their Contents: Fourth Amendment Considerations in a Post-<span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross"><i>Ross</i></a></span> World, <span class="citation no-link">62 Neb. L. Rev. 1</span> (1983); Latzer, Searching Cars and Their Contents: <i>United States</i> v. <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> <span class="citation no-link">18 Crim. L. Bull. 381</span> (1982); Kamisar, The "Automobile Search" Cases: The Court Does Little to Clarify the "Labyrinth" of Judicial Uncertainty, <span class="star-pagination">*577</span> in 3 The Supreme Court: Trends and Developments 1980-1981, p. 69 (D. Opperman ed. 1982). One leading authority on the Fourth Amendment, after comparing <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> with <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and its progeny, observed: "These two lines of authority cannot be completely reconciled, and thus how one comes out in the container-in-the-car situation depends upon which line of authority is used as a point of departure." 3 W. LaFave, Search and Seizure 53 (2d ed. 1987).</p>
<p>The discrepancy between the two rules has led to confusion for law enforcement officers. For example, when an officer, who has developed probable cause to believe that a vehicle contains drugs, begins to search the vehicle and immediately discovers a closed container, which rule applies? The defendant will argue that the fact that the officer first chose to search the container indicates that his probable cause extended only to the container and that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> therefore require a warrant. On the other hand, the fact that the officer first chose to search in the most obvious location should not restrict the propriety of the search. The <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> rule, as applied in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> has devolved into an anomaly such that the more likely the police are to discover drugs in a container, the less authority they have to search it. We have noted the virtue of providing "`"clear and unequivocal" guidelines to the law enforcement profession.'" <i>Minnick</i> v. <i>Mississippi,</i> <span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/#151" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146, 151</a></span> (1990), quoting <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#682" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675, 682</a></span> (1988). The <i>Chadwick-Sanders</i> rule is the antithesis of a "`clear and unequivocal' guideline."</p>
<p>JUSTICE STEVENS argues that the decisions of this Court evince a lack of confusion about the automobile exception. See <i>post,</i> at 594. The first case cited by the dissent, <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), however, did not involve an automobile at all. We considered in <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> the temporary detention of luggage in an airport. Not only was no automobile involved, but the defendant, Place, was waiting <span class="star-pagination">*578</span> at the airport to board his plane rather than preparing to leave the airport in a car. Any similarity to <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> in which the defendant was leaving the airport in a car, is remote at best. <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span></i> had nothing to do with the automobile exception and is inapposite.</p>
<p>Nor does JUSTICE STEVENS' citation of <i>Oklahoma</i> v. <i>Castleberry,</i> <span class="citation" data-id="111405"><a href="/opinion/111405/oklahoma-v-castleberry/" aria-description="Citation for case: Oklahoma v. Castleberry">471 U. S. 146</a></span> (1985), support his contention. <i><span class="citation" data-id="111405"><a href="/opinion/111405/oklahoma-v-castleberry/" aria-description="Citation for case: Oklahoma v. Castleberry">Castleberry</a></span></i> presented the same question about the application of the automobile exception to the search of a closed container that we face here. In <i><span class="citation" data-id="111405"><a href="/opinion/111405/oklahoma-v-castleberry/" aria-description="Citation for case: Oklahoma v. Castleberry">Castleberry</a></span>,</i> we affirmed by an equally divided court. That result illustrates this Court's continued struggle with the scope of the automobile exception rather than the absence of confusion in applying it.</p>
<p>JUSTICE STEVENS also argues that law enforcement has not been impeded because the Court has decided 29 Fourth Amendment cases since <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> in favor of the government. See <i>post,</i> at 600. In each of these cases, the government appeared as the petitioner. The dissent fails to explain how the loss of 29 cases below, not to mention the many others which this Court did not hear, did not interfere with law enforcement. The fact that the state courts and the Federal Courts of Appeals have been reversed in their Fourth Amendment holdings 29 times since 1982 further demonstrates the extent to which our Fourth Amendment jurisprudence has confused the courts.</p>
<p>Most important, with the exception of <i>United States</i> v. <i>Johns,</i> <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">469 U. S. 478</a></span> (1985), and <i>Texas</i> v. <i>Brown,</i> <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983), the Fourth Amendment cases cited by the dissent do not concern automobiles or the automobile exception. From <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> through <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> this Court has explained that automobile searches differ from other searches. The dissent fails to acknowledge this basic principle and so misconstrues and misapplies our Fourth Amendment case law.</p>
<p>The <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> dissenters predicted that the container rule would have "the perverse result of allowing fortuitous circumstances to control the outcome" of various searches. 433 <span class="star-pagination">*579</span> U. S., at 22. The rule also was so confusing that within two years after <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> this Court found it necessary to expound on the meaning of that decision and explain its application to luggage in general. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 761-764</a></span>. Again, dissenters bemoaned the "inherent opaqueness" of the difference between the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> principles and noted "the confusion to be created for all concerned." <i>Id.,</i> at 771. See also <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#425" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 425-426</a></span> (1981) (listing cases decided by Federal Courts of Appeals since <i>Chadwick</i> had been announced). Three years after <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>,</i> we returned in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> to "this troubled area," <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>, in order to assert that <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> had not cut back on <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>.</i></p>
<p>Although we have recognized firmly that the doctrine of <i>stare decisis</i> serves profoundly important purposes in our legal system, this Court has overruled a prior case on the comparatively rare occasion when it has bred confusion or been a derelict or led to anomalous results. See, <i>e. g., </i><i>Complete Auto Transit, Inc.</i> v. <i>Brady,</i> <span class="citation" data-id="109615"><a href="/opinion/109615/complete-auto-transit-inc-v-brady/#288" aria-description="Citation for case: Complete Auto Transit, Inc. v. Brady">430 U. S. 274, 288-289</a></span> (1977). <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> was explicitly undermined in <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>, and the existence of the dual regimes for automobile searches that uncover containers has proved as confusing as the <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span></i> dissenters predicted. We conclude that it is better to adopt one clear-cut rule to govern automobile searches and eliminate the warrant requirement for closed containers set forth in <i><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>.</i></p>
<p></p>
<h2>VI</h2>
<p>The interpretation of the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine set forth in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> now applies to all searches of containers found in an automobile. In other words, the police may search without a warrant if their search is supported by probable cause. The Court in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> put it this way:</p>
<blockquote>"The scope of a warrantless search of an automobile . . . is not defined by the nature of the container in which the contraband is secreted. Rather, it is defined by the object <span class="star-pagination">*580</span> of the search and the places in which there is probable cause to believe that it may be found." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>.</blockquote>
<p>It went on to note: "Probable cause to believe that a container placed in the trunk of a taxi contains contraband or evidence does not justify a search of the entire cab." <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span></i> We reaffirm that principle. In the case before us, the police had probable cause to believe that the paper bag in the automobile's trunk contained marijuana. That probable cause now allows a warrantless search of the paper bag. The facts in the record reveal that the police did not have probable cause to believe that contraband was hidden in any other part of the automobile and a search of the entire vehicle would have been without probable cause and unreasonable under the Fourth Amendment.</p>
<p>Our holding today neither extends the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine nor broadens the scope of the permissible automobile search delineated in <i>Carroll, Chambers,</i> and <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>.</i> It remains a "cardinal principle that `searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendmentsubject only to a few specifically established and well-delineated exceptions.'" <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978), quoting <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnotes omitted). We held in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>:</i> "The exception recognized in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> is unquestionably one that is `specifically established and well delineated.'" <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#825" aria-description="Citation for case: United States v. Ross">456 U. S., at 825</a></span>.</p>
<p>Until today, this Court has drawn a curious line between the search of an automobile that coincidentally turns up a container and the search of a container that coincidentally turns up in an automobile. The protections of the Fourth Amendment must not turn on such coincidences. We therefore interpret <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> as providing one rule to govern all automobile searches. The police may search an automobile and the containers within it where they have probable cause to believe contraband or evidence is contained.</p>
<p><span class="star-pagination">*581</span> The judgment of the California Court of Appeal is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE SCALIA, concurring in the judgment.</p>
<p>I agree with the dissent that it is anomalous for a briefcase to be protected by the "general requirement" of a prior warrant when it is being carried along the street, but for that same briefcase to become unprotected as soon as it is carried into an automobile. On the other hand, I agree with the Court that it would be anomalous for a locked compartment in an automobile to be unprotected by the "general requirement" of a prior warrant, but for an unlocked briefcase within the automobile to be protected. I join in the judgment of the Court because I think its holding is more faithful to the text and tradition of the Fourth Amendment, and if these anomalies in our jurisprudence are ever to be eliminated that is the direction in which we should travel.</p>
<p>The Fourth Amendment does not by its terms require a prior warrant for searches and seizures; it merely prohibits searches and seizures that are "unreasonable." What it explicitly states regarding warrants is by way of limitation upon their issuance rather than requirement of their use. See <i>Wakely</i> v. <i>Hart,</i> 6 Binney 316, 318 (Pa. 1814). For the warrant was a means of insulating officials from personal liability assessed by colonial juries. An officer who searched or seized without a warrant did so at his own risk; he would be liable for trespass, including exemplary damages, unless the jury found that his action was "reasonable." Amar, The Bill of Rights as a Constitution, 100 Yale L. J. 1131, 1178-1180 (1991); <i>Huckle</i> v. <i>Money,</i> 2 Wils. 205, 95 Eng. Rep. 768 (K. B. 1763). If, however, the officer acted pursuant to a proper warrant, he would be absolutely immune. See <i>Bell</i> v. <i>Clapp,</i> <span class="citation" data-id="5473240"><a href="/opinion/5628141/bell-v-clapp/" aria-description="Citation for case: Bell v. Clapp">10 Johns. 263</a></span> (N. Y. 1813); 4 W. Blackstone, Commentaries 288 (1769). By restricting the issuance of warrants, <span class="star-pagination">*582</span> the Framers endeavored to preserve the jury's role in regulating searches and seizures. Amar, <i>supra;</i> Posner, Rethinking the Fourth Amendment, 1981 S. Ct. Rev. 49, 72-73; see also T. Taylor, Two Studies in Constitutional Interpretation 41 (1969).</p>
<p>Although the Fourth Amendment does not explicitly impose the requirement of a warrant, it is of course textually possible to consider that implicit within the requirement of reasonableness. For some years after the (still continuing) explosion in Fourth Amendment litigation that followed our announcement of the exclusionary rule in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), our jurisprudence lurched back and forth between imposing a categorical warrant requirement and looking to reasonableness alone. (The opinions preferring a warrant involved searches of structures.) Compare <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947), with <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948); compare <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948), with <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950). See generally <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). By the late 1960's, the preference for a warrant had won out, at least rhetorically. See <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>; </i><i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971).</p>
<p>The victory was illusory. Even before today's decision, the "warrant requirement" had become so riddled with exceptions that it was basically unrecognizable. In 1985, one commentator cataloged nearly 20 such exceptions, including "searches incident to arrest . . . automobile searches . . . border searches . . . administrative searches of regulated businesses. . . exigent circumstances . . . search[es] incident to nonarrest when there is probable cause to arrest . . . boat boarding for document checks . . . welfare searches . . . inventory searches . . . airport searches . . . school search[es]. . . ." Bradley, Two Models of the Fourth Amendment, <span class="citation no-link">83 Mich. L. Rev. 1468</span>, 1473-1474 (footnotes omitted). Since then, we have added at least two more. <i>California</i> v. <i>Carney,</i> 471 <span class="star-pagination">*583</span> U. S. 386 (1985) (searches of mobile homes); <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987) (searches of offices of government employees). Our intricate body of law regarding "reasonable expectation of privacy" has been developed largely as a means of creating these exceptions, enabling a search to be denominated not a Fourth Amendment "search" and therefore not subject to the general warrant requirement. Cf. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#729" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><i>id.,</i> at 729</a></span> (SCALIA, J., concurring in judgment).</p>
<p>Unlike the dissent, therefore, I do not regard today's holding as some momentous departure, but rather as merely the continuation of an inconsistent jurisprudence that has been with us for years. Cases like <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), and <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), have taken the "preference for a warrant" seriously, while cases like <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), have not. There can be no clarity in this area unless we make up our minds, and unless the principles we express comport with the actions we take.</p>
<p>In my view, the path out of this confusion should be sought by returning to the first principle that the "reasonableness" requirement of the Fourth Amendment affords the protection that the common law afforded. See <i>County of Riverside</i> v. <i>McLaughlin, ante,</i> at 60 (SCALIA, J., dissenting); <i>People</i> v. <i>Chiagles,</i> <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#195" aria-description="Citation for case: People v. . Chiagles">237 N. Y. 193, 195</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">142 N. E. 583</a></span> (1923) (Cardozo, J.). Cf. <i>California</i> v. <i>Hodari D.,</i> <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#624" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 624-627</a></span> (1991). I have no difficulty with the proposition that that includes the requirement of a warrant, where the common law required a warrant; and it may even be that changes in the surrounding legal rules (for example, elimination of the common-law rule that reasonable, good-faith belief was no defense to absolute liability for trespass, <i>Little</i> v. <i>Barreme,</i> <span class="citation" data-id="84781"><a href="/opinion/84781/little-v-barreme/" aria-description="Citation for case: Little v. Barreme">2 Cranch 170</a></span> (1804) (Marshall, C. J.); see generally Amar, Of Sovereignty and Federalism, 96 Yale L. J. 1425, 1486-1487 (1987)), may make a warrant indispensable to reasonableness where it once was not. But the supposed "general <span class="star-pagination">*584</span> rule" that a warrant is always required does not appear to have any basis in the common law, see, <i>e. g., </i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#150" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 150-153</a></span>; <i>Gelston</i> v. <i>Hoyt,</i> <span class="citation" data-id="8373743"><a href="/opinion/8403401/gelston-v-hoyt/#310" aria-description="Citation for case: Gelston v. Hoyt">3 Wheat. 246, 310-311</a></span> (1818) (Story, J.); <i>Wakely, supra,</i> and confuses rather than facilitates any attempt to develop rules of reasonableness in light of changed legal circumstances, as the anomaly eliminated and the anomaly created by today's holding both demonstrate.</p>
<p>And there are more anomalies still. Under our precedents (as at common law), a person may be arrested outside the home on the basis of probable cause, without an arrest warrant. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-421</a></span> (1976); <i>Rohan</i> v. <i>Sawin,</i> <span class="citation no-link">59 Mass. 281</span> (1851). Upon arrest, the person, as well as the area within his grasp, may be searched for evidence related to the crime. <i>Chimel</i> v. <i>California, supra,</i> at 762-763; <i>People</i> v. <i><span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">Chiagles, supra</a></span></i> (collecting authority). Under these principles, if a known drug dealer is carrying a briefcase reasonably believed to contain marijuana (the unauthorized possession of which is a crime), the police may arrest him and search his person on the basis of probable cause alone. And, under our precedents, upon arrival at the station house, the police may inventory his possessions, including the briefcase, even if there is no reason to suspect that they contain contraband. <i>Illinois</i> v. <i>Lafayette,</i> <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983). According to our current law, however, the police may not, on the basis of the same probable cause, take the less intrusive step of stopping the individual on the street and demanding to see the contents of his briefcase. That makes no sense <i>a priori,</i> and in the absence of any common-law tradition supporting such a distinction, I see no reason to continue it.</p>
<p></p>
<h2>* * *</h2>
<p>I would reverse the judgment in the present case, not because a closed container carried inside a car becomes subject to the "automobile" exception to the general warrant requirement, <span class="star-pagination">*585</span> but because the search of a closed container, outside a privately owned building, with probable cause to believe that the container contains contraband, and when it in fact does contain contraband, is not one of those searches whose Fourth Amendment reasonableness depends upon a warrant. For that reason I concur in the judgment of the Court.</p>
<p>JUSTICE WHITE, dissenting.</p>
<p>Agreeing as I do with most of JUSTICE STEVENS' opinion and with the result he reaches, I dissent and would affirm the judgment below.</p>
<p>JUSTICE STEVENS, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>At the end of its opinion, the Court pays lipservice to the proposition that should provide the basis for a correct analysis of the legal question presented by this case: It is "`a cardinal principle that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendment  subject only to a few specifically established and well-delineated exceptions."' <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978), quoting <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnotes omitted)." <i>Ante,</i> at 580.</p>
<p>Relying on arguments that conservative judges have repeatedly rejected in past cases, the Court todaydespite its disclaimer to the contrary, <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">ibid.</a></span></i>  enlarges the scope of the automobile exception to this "cardinal principle," which undergirded our Fourth Amendment jurisprudence prior to the retirement of the author of the landmark opinion in <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). As a preface to my response to the Court's arguments, it is appropriate to restate the basis for the warrant requirement, the significance of the <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> case, and the reasons why the limitations on the automobile exception that were articulated in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982), represent a fair accommodation <span class="star-pagination">*586</span> between the basic rule requiring prior judicial approval of searches and the automobile exception.</p>
<p></p>
<h2>I</h2>
<p>The Fourth Amendment is a restraint on Executive power. The Amendment constitutes the Framers' direct constitutional response to the unreasonable law enforcement practices employed by agents of the British Crown. See <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#389" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 389-391</a></span> (1914); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span> (1886); 1 W. LaFave, Search and Seizure 3-5 (2d ed. 1987). Over the years  particularly in the period immediately after World War II and particularly in opinions authored by Justice Jackson after his service as a special prosecutor at the Nuremburg trials  the Court has recognized the importance of this restraint as a bulwark against police practices that prevail in totalitarian regimes. See, <i>e. g., </i><i>United States</i> v. <i>Di Re,</i> <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/#595" aria-description="Citation for case: United States v. Di Re">332 U. S. 581, 595</a></span> (1948); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#17" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 17</a></span> (1948).</p>
<p>This history is, however, only part of the explanation for the warrant requirement. The requirement also reflects the sound policy judgment that, absent exceptional circumstances, the decision to invade the privacy of an individual's personal effects should be made by a neutral magistrate rather than an agent of the Executive. In his opinion for the Court in <i>Johnson</i> v. <i>United States, id.,</i> at 13-14, Justice Jackson explained:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime."</blockquote>
<p>Our decisions have always acknowledged that the warrant requirement imposes a burden on law enforcement. And our <span class="star-pagination">*587</span> cases have not questioned that trained professionals normally make reliable assessments of the existence of probable cause to conduct a search. We have repeatedly held, however, that these factors are outweighed by the individual interest in privacy that is protected by advance judicial approval. The Fourth Amendment dictates that the privacy interest is paramount, no matter how marginal the risk of error might be if the legality of warrantless searches were judged only after the fact.</p>
<p>In the concluding paragraph of his opinion in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> Chief Justice Burger made the point this way:</p>
<blockquote>"Even though on this record the issuance of a warrant by a judicial officer was reasonably predictable, a line must be drawn. In our view, when no exigency is shown to support the need for an immediate search, the Warrant Clause places the line at the point where the property to be searched comes under the exclusive dominion of police authority. Respondents were therefore entitled to the protection of the Warrant Clause with the evaluation of a neutral magistrate, before their privacy interests in the contents of [their luggage] were invaded." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#15" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 15-16</a></span>.</blockquote>
<p>In <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the Department of Justice had mounted a frontal attack on the warrant requirement. The Government's principal contention was that "the Fourth Amendment Warrant Clause protects only interests traditionally identified with the home." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#6" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 6</a></span>. We categorically rejected that contention, relying on the history and text of the Amendment,<sup>[1]</sup> the policy underlying the warrant requirement,<sup>[2]</sup><span class="star-pagination">*588</span> and a line of cases spanning over a century of our jurisprudence.<sup>[3]</sup> We also rejected the Government's alternative argument that the rationale of our automobile search cases demonstrated the reasonableness of permitting warrantless searches of luggage.</p>
<p>We concluded that neither of the justifications for the automobile exception could support a similar exception for luggage. We first held that the privacy interest in luggage is "substantially greater than in an automobile." <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 13</a></span>. Unlike automobiles and their contents, we reasoned, "[l]uggage contents are not open to public view, except as a condition to a border entry or common carrier travel; nor is luggage subject to regular inspections and official scrutiny on a continuing basis." <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></i> Indeed, luggage is specifically intended to safeguard the privacy of personal effects, unlike an automobile, "whose primary function is transportation." <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></i></p>
<p>We then held that the mobility of luggage did not justify creating an additional exception to the Warrant Clause. Unlike an automobile, luggage can easily be seized and detained pending judicial approval of a search. Once the police have <span class="star-pagination">*589</span> luggage "under their exclusive control, there [i]s not the slightest danger that the [luggage] or its contents could [be] removed before a valid search warrant could be obtained.. . . With the [luggage] safely immobilized, it [i]s unreasonable to undertake the additional and greater intrusion of a search without a warrant" (footnote omitted). <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></i></p>
<p>Two Terms after <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> we decided a case in which the relevant facts were identical to those before the Court today. In <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), the police had probable cause to search a green suitcase that had been placed in the trunk of a taxicab at the Little Rock Airport. Several blocks from the airport, they stopped the cab, arrested the passengers, seized the suitcase and, without obtaining a warrant, opened and searched it.</p>
<p>The Arkansas Supreme Court held that the search was unconstitutional. Relying on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the state court had no difficulty in concluding that there was "nothing in this set of circumstances that would lend credence to an assertion of impracticability in obtaining a search warrant." <i>Sanders</i> v. <i>State,</i> <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#600" aria-description="Citation for case: Sanders v. State">262 Ark. 595, 600</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d 704, 706</a></span> (1977). Over the dissent of JUSTICE BLACKMUN and then-JUSTICE REHNQUIST, both of whom had also dissented in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> this Court affirmed. In his opinion for the Court, Justice Powell noted that the seizure of the green suitcase was entirely proper,<sup>[4]</sup> but that the State nevertheless had the burden of justifying the warrantless search,<sup>[5]</sup> and that it had "failed to <span class="star-pagination">*590</span> carry its burden of demonstrating the need for warrantless searches of luggage properly taken from automobiles." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#763" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 763</a></span>.</p>
<p>Chief Justice Burger wrote separately to identify the distinction between cases in which police have probable cause to believe contraband is located somewhere in a vehiclethe typical automobile exception caseand cases like <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> in which they had probable cause to search a particular container before it was placed in the car. He wrote:</p>
<blockquote>"Because the police officers had probable cause to believe that respondent's green suitcase contained marihuana before it was placed in the trunk of the taxicab, their duty to obtain a search warrant before opening it is clear under <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). The essence of our holding in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> is that there is a legitimate expectation of privacy in the contents of a trunk or suitcase accompanying or being carried by a person; that expectation of privacy is not diminished simply because the owner's arrest occurs in a public place. Whether arrested in a hotel lobby, an airport, a railroad terminal, or on a public street, as here, the owner has the right to expect that the contents of his luggage will not, without his consent, be exposed on demand of the police. . . .</blockquote>
<blockquote>"The breadth of the Court's opinion and its repeated references to the `automobile' from which respondent's suitcase was seized at the time of his arrest, however, might lead the reader to believeas the dissenters apparently dothat this case involves the `automobile' exception to the warrant requirement. See <i>ante,</i> at 762-765, and n. 14. It does not. Here, as in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> it was the <i>luggage</i> being transported by respondent at <span class="star-pagination">*591</span> the time of the arrest, not the automobile in which it was being carried, that was the suspected locus of the contraband." <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#766" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 766-767</a></span> (opinion concurring in judgment).</blockquote>
<p>Chief Justice Burger thus carefully explained that <i>Sanders,</i> which the Court overrules today, "simply d[id] not present the question of whether a warrant is required before opening luggage when the police have probable cause to believe contraband is located <i>somewhere</i> in the vehicle, but when they do not know whether, for example, it is inside a piece of luggage in the trunk, in the glove compartment, or concealed in some part of the car's structure." <i>Id.,</i> at 767. We confronted that question in <i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982).<sup>[6]</sup></p>
<p>We held in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> that "the scope of the warrantless search authorized by [the automobile] exception is no broader and no narrower than a magistrate could legitimately authorize by warrant." See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#825" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 825</a></span>. The inherent mobility of the vehicle justified the immediate search without a warrant, but did not affect the scope of the search. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 822</a></span>. Thus, the search could encompass containers, which might or might not conceal the object of the search, as well as the remainder of the vehicle. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 821</a></span>.</p>
<p>Our conclusion was supported not only by prior cases defining the proper scope of searches authorized by warrant, as well as cases involving the automobile exception, but also by practical considerations that apply to searches in which the police have only generalized probable cause to believe that contraband is somewhere in a vehicle. We explained that, in such instances, "prohibiting police from opening immediately a container in which the object of the search is most likely to be found and instead forcing them first to comb the entire vehicle would actually exacerbate the intrusion on privacy interests." <span class="star-pagination">*592</span> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><i>Id.,</i> at 821, n. 28</a></span>. Indeed, because "the police could never be certain that the contraband was not secreted in a yet undiscovered portion of the vehicle," the most likely result would be that "the vehicle would need to be secured while a warrant was obtained." <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ibid.</a></span></i></p>
<p>These concerns that justified our holding in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> are not implicated in cases like <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> in which the police have probable cause to search a <i>particular</i> container rather than the <i>entire</i> vehicle. Because the police can seize the container which is the object of their search, they have no need either to search or to seize the entire vehicle. Indeed, as even the Court today recognizes, they have no authority to do so. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S., at 824</a></span>; <i>ante,</i> at 580.</p>
<p>In reaching our conclusion in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> we therefore did not retreat at all from the holding in either <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> or <i>Sanders.</i> Instead, we expressly endorsed the reasoning in Chief Justice Burger's separate opinion in <i>Sanders.</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#813" aria-description="Citation for case: United States v. Ross">456 U. S., at 813-814</a></span>.<sup>[7]</sup> We explained repeatedly that <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> involved the <i>scope</i> of the warrantless search authorized by the automobile exception, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#800" aria-description="Citation for case: United States v. Ross"><i>id.,</i> at 800, 809, 817, 825</a></span>, and, unlike <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders,</i> did not involve the <i>applicability</i> of the exception to closed containers. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S., at 809-817</a></span>.</p>
<p>Thus, we recognized in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> had not created a special rule for container searches, but <span class="star-pagination">*593</span> rather had merely applied the cardinal principle that warrantless searches are <i>per se</i> unreasonable unless justified by an exception to the general rule. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#811" aria-description="Citation for case: United States v. Ross">456 U. S., at 811-812</a></span>.<sup>[8]</sup><i>Ross</i> dealt with the scope of the automobile exception; <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> were cases in which the exception simply did not apply.</p>
<p></p>
<h2>II</h2>
<p>In its opinion today, the Court recognizes that the police did not have probable cause to search respondent's vehicle and that a search of anything but the paper bag that respondent had carried from Daza's apartment and placed in the trunk of his car would have been unconstitutional. <i>Ante,</i> at 580. Moreover, as I read the opinion, the Court assumes that the police could not have made a warrantless inspection of the bag before it was placed in the car. See <i>ibid.</i> Finally, the Court also does not question the fact that, under our prior cases, it would have been lawful for the police to seize the container and detain it (and respondent) until they obtained a search warrant. <i>Ante,</i> at 575. Thus, all of the relevant facts that governed our decisions in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> are present here whereas the relevant fact that justified the vehicle search in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> is not present.</p>
<p>The Court does not attempt to identify any exigent circumstances that would justify its refusal to apply the general rule against warrantless searches. Instead, it advances these three arguments: First, the rules identified in the foregoing cases are confusing and anomalous. <i>Ante,</i> at 576-579. Second, the rules do not protect any significant interest in privacy. <i>Ante,</i> at 573-576. And, third, the rules impede effective <span class="star-pagination">*594</span> law enforcement. <i>Ante,</i> at 576-577. None of these arguments withstands scrutiny.</p>
<p></p>
<h2><i>The "Confusion"</i></h2>
<p>In the nine years since <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> was decided, the Court has considered three cases in which the police had probable cause to search a particular container and one in which they had probable cause to search two vehicles. The decisions in all four of those cases were perfectly straightforward and provide no evidence of confusion in the state or lower federal courts.</p>
<p>In <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we held that, although reasonable suspicion justifies the temporary detention of an airline passenger's luggage, the seizure in that particular case was unreasonable because of the prolonged delay in ascertaining the existence of probable cause. In the course of our opinion, we noted that the then-recent decision in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> had not modified the holding in <i>Sanders.</i> 462 U. S., at 701, n. 3. We also relied on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> for our conclusion that the temporary seizure of luggage is substantially less intrusive than a search of its contents. 462 U. S., at 706-707.</p>
<p>In <i>Oklahoma</i> v. <i>Castleberry,</i> <span class="citation" data-id="111405"><a href="/opinion/111405/oklahoma-v-castleberry/" aria-description="Citation for case: Oklahoma v. Castleberry">471 U. S. 146</a></span> (1985), police officers had probable cause to believe the defendant carried narcotics in blue suitcases in the trunk of his car. After arresting him, they opened the trunk, seized the suitcases, and searched them without a warrant. The state court held that the search was invalid, explaining:</p>
<blockquote>"If the officer has probable cause to believe there is contraband somewhere in the car, but he does not know exactly where, he may search the entire car as well as any containers found therein. <i>See </i><i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> . . . (1982); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>, . . . (1970); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> . . . (1925). If, on the other hand, the officer only has probable cause to believe there is contraband in a <span class="star-pagination">*595</span> specific container in the car, he must detain the container and delay his search until a search warrant is obtained. <i>See </i><i>United States</i> v. <i>Ross,</i> <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> . . . (1982); <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> . . . (1979); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> . . . (1977)." <i>Castleberry</i> v. <i>State,</i> <span class="citation" data-id="9565373"><a href="/opinion/1216822/castleberry-v-state/#724" aria-description="Citation for case: Castleberry v. State">678 P. 2d 720, 724</a></span> (Okla. 1984).</blockquote>
<p>This Court affirmed by an equally divided Court. <span class="citation multiple-matches"><a href="/c/U.%20S./471/146/">471 U. S. 146</a></span> (1985).</p>
<p>In the case the Court decides today, the California Court of Appeal also had no difficulty applying the critical distinction. Relying on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> it explained that "the officers had probable cause to believe marijuana would be found only in a brown lunch bag and nowhere else in the car. We are compelled to hold they should have obtained a search warrant before opening it." <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#592" aria-description="Citation for case: People v. Acevedo">216 Cal. App. 3d 586, 592</a></span>, <span class="citation" data-id="9731130"><a href="/opinion/2175164/people-v-acevedo/#27" aria-description="Citation for case: People v. Acevedo">265 Cal. Rptr. 23, 27</a></span> (1990).</p>
<p>In the case in which the police had probable cause to search two vehicles, <i>United States</i> v. <i>Johns,</i> <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/" aria-description="Citation for case: United States v. Johns">469 U. S. 478</a></span> (1985),<sup>[9]</sup> we rejected the respondent's reliance on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> with a straightforward explanation of why that case, unlike <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> did not involve an exception to the warrant requirement. We first expressed our agreement with the Court of Appeals that the Customs officers who had conducted the search had <span class="star-pagination">*596</span> probable cause to search the vehicles. <i>Id.,</i> at 482. We then explained:</p>
<blockquote>"Under the circumstances of this case, respondents' reliance on <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> is misplaced. . . . <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> . . . did not involve the exception to the warrant requirement recognized in <i>Carroll</i> v. <i>United States, supra</i><i>,</i> because the police had no probable cause to believe that the automobile, as contrasted to the footlocker, contained contraband. See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 11-12</a></span>. This point is underscored by our decision in <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>,</i> which held that notwithstanding <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> police officers may conduct a warrantless search of containers discovered in the course of a lawful vehicle search. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#810" aria-description="Citation for case: United States v. Ross">456 U. S., at 810-814</a></span>. Given our conclusion that the Customs officers had probable cause to believe that the pickup trucks contained contraband, <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> is simply inapposite. See <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>." <span class="citation" data-id="9429826"><a href="/opinion/111305/united-states-v-johns/#482" aria-description="Citation for case: United States v. Johns">469 U. S., at 482-483</a></span>.</blockquote>
<p>The decided cases thus provide no support for the Court's concern about "confusion." The Court instead relies primarily on predictions that were made by JUSTICE BLACKMUN in his dissenting opinions in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders.</i><sup>[10]</sup> The Court, however, cites no evidence that these predictions have in fact materialized or that anyone else has been unable to understand the "`inherent opaqueness,'" <i>ante,</i> at 579, of this uncomplicated issue. The only support offered by the Court, other than the unsubstantiated allegations of prior dissents, is three law review comments and a sentence from Professor LaFave's treatise. None of the law review pieces <span class="star-pagination">*597</span> criticize the holdings in <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders.</i><sup>[11]</sup> The sentence from Professor LaFave's treatise, at most, indicates that, as is often the case, there may be some factual situations at the margin of the relevant rules that are difficult to decide. Moreover, to the extent Professor LaFave criticizes our jurisprudence in this area, he is critical of <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> rather than <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> or <i>Sanders.</i> And he ultimately concludes that even <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> was correctly decided. See 3 W. LaFave, Search and Seizure 55-56 (2d ed. 1987).</p>
<p>The Court summarizes the alleged "anomaly" created by the coexistence of <i>Ross, Chadwick,</i> and <i>Sanders</i> with the statement that "the more likely the police are to discover drugs in a container, the less authority they have to search it." <i>Ante,</i> at 577. This juxtaposition is only anomalous, however, if one accepts the flawed premise that the degree to which the police are likely to discover contraband is correlated with their authority to search <i>without a warrant.</i> Yet, even proof beyond a reasonable doubt will not justify a warrantless search that is not supported by one of the exceptions to the warrant requirement. And, even when the police have a warrant or an exception applies, once the police possess probable cause, the extent to which they are more or less certain of the contents of a container has no bearing on their authority to search it.</p>
<p><span class="star-pagination">*598</span> To the extent there was any "anomaly" in our prior jurisprudence, the Court has "cured" it at the expense of creating a more serious paradox. For surely it is anomalous to prohibit a search of a briefcase while the owner is carrying it exposed on a public street yet to permit a search once the owner has placed the briefcase in the locked trunk of his car. One's privacy interest in one's luggage can certainly not be diminished by one's removing it from a public thoroughfare and placing itout of sightin a privately owned vehicle. Nor is the danger that evidence will escape increased if the luggage is in a car rather than on the street. In either location, if the police have probable cause, they are authorized to seize the luggage and to detain it until they obtain judicial approval for a search. Any line demarking an exception to the warrant requirement will appear blurred at the edges, but the Court has certainly erred if it believes that, by erasing one line and drawing another, it has drawn a clearer boundary.</p>
<p></p>
<h2><i>The Privacy Argument</i></h2>
<p>The Court's statement that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> provide only "minimal protection to privacy," <i>ante,</i> at 576, is also unpersuasive. Every citizen clearly has an interest in the privacy of the contents of his or her luggage, briefcase, handbag or any other container that conceals private papers and effects from public scrutiny. That privacy interest has been recognized repeatedly in cases spanning more than a century. See, <i>e. g., </i><i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#6" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 6-11</a></span>; <i>United States</i> v. <i>Van Leeuwen,</i> <span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/#251" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249, 251</a></span> (1970); <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878).</p>
<p>Under the Court's holding today, the privacy interest that protects the contents of a suitcase or a briefcase from a warrantless search when it is in public view simply vanishes when its owner climbs into a taxicab. Unquestionably the rejection of the <i>Sanders</i> line of cases by today's decision will result in a significant loss of individual privacy.</p>
<p><span class="star-pagination">*599</span> To support its argument that today's holding works only a minimal intrusion on privacy, the Court suggests that "[i]f the police know that they may open a bag only if they are actually searching the entire car, they may search more extensively than they otherwise would in order to establish the general probable cause required by <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span>.</i>" <i>Ante,</i> at 574-575. As I have already noted, see n. 9, <i>supra,</i> this fear is unexplained and inexplicable. Neither evidence uncovered in the course of a search nor the scope of the search conducted can be used to provide <i>post hoc</i> justification for a search unsupported by probable cause at its inception.</p>
<p>The Court also justifies its claim that its holding inflicts only minor damage by suggesting that, under <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), the police could have arrested respondent and searched his bag if respondent had placed the bag in the passenger compartment of the automobile instead of in the trunk. In <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>,</i> however, the justification for stopping the car and arresting the driver had nothing to do with the subsequent search, which was based on the potential danger to the arresting officer. The holding in <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span></i> was supportable under a straightforward application of the automobile exception. See <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#449" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 449-453</a></span> (1981) (STEVENS, J., dissenting). I would not extend <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span></i>'s holding to this case, in which the container which was protected from a warrantless search before it was placed in the carprovided the only justification for the arrest. Even accepting <i><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span></i>'s application to a case like this one, however, the Court's logic extends its holding to a container placed in the <i>trunk</i> of a vehicle, rather than in the passenger compartment. And the Court makes this extension without any justification whatsoever other than convenience to law enforcement.</p>
<p></p>
<h2><i>The Burden on Law Enforcement</i></h2>
<p>The Court's suggestion that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> have created a siguificant burden on effective law enforcement <span class="star-pagination">*600</span> is unsupported, inaccurate, and, in any event, an insufficient reason for creating a new exception to the warrant requirement.</p>
<p>Despite repeated claims that <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders</i> have "impeded effective law enforcement," <i>ante,</i> at 574, 576, the Court cites no authority for its contentions. Moreover, all evidence that does exist points to the contrary conclusion. In the years since <i><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span></i> was decided, the Court has heard argument in 30 Fourth Amendment cases involving narcotics.<sup>[12]</sup> In all but one, the government was the petitioner.<sup>[13]</sup> All save two involved a search or seizure without a warrant or with a defective warrant.<sup>[14]</sup> And, in all except three, the Court upheld the constitutionality of the search or seizure.<sup>[15]</sup></p>
<p><span class="star-pagination">*601</span> In the meantime, the flow of narcotics cases through the courts has steadily and dramatically increased.<sup>[16]</sup> See Annual Report of the Attorney General of the United States 21 (1989). No impartial observer could criticize this Court for hindering the progress of the war on drugs. On the contrary, decisions like the one the Court makes today will support the conclusion that this Court has become a loyal foot soldier in the Executive's fight against crime.</p>
<p>Even if the warrant requirement does inconvenience the police to some extent, that fact does not distinguish this constitutional requirement from any other procedural protection secured by the Bill of Rights. It is merely a part of the price that our society must pay in order to preserve its freedom. Thus, in a unanimous opinion that relied on both <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> and <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> Justice Stewart wrote:</p>
<blockquote>"Moreover, the mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment. Cf. <i>Coolidge</i> v. <i>New Hampshire,</i> [<span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#481" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 481</a></span> (1971)]. The investigation of crime would always be simplified if warrants were unnecessary. But the Fourth Amendment reflects the view of those who wrote the Bill of Rights that the privacy of a person's home and property may not be totally sacrificed in the name of maximum simplicity in enforcement of the criminal law. See <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#6" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 6-11</a></span>." <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 393</a></span>.</blockquote>
<p><span class="star-pagination">*602</span> It is too early to know how much freedom America has lost today. The magnitude of the loss is, however, not nearly as significant as the Court's willingness to inflict it without even a colorable basis for its rejection of prior law.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  When Officer Coleman returned with a warrant, the apartment was searched and bags of marijuana were found there. We are here concerned, of course, only with what was discovered in the automobile.</p>
<p>[2]  Although respondent now challenges this holding, we decline to second-guess the California courts, which have found probable cause. Respondent did not raise the probable-cause question in his Brief in Opposition nor did he cross-petition for resolution of the issue. He also did not raise the point in a cross-petition to the Supreme Court of California. We therefore do not consider the issue here. See <i>Lytle</i> v. <i>Household Mfg., Inc.,</i> <span class="citation" data-id="112393"><a href="/opinion/112393/lytle-v-household-manufacturing-inc/#551" aria-description="Citation for case: Lytle v. Household Manufacturing, Inc.">494 U. S. 545, 551, n. 3</a></span> (1990); <i>Heckler</i> v. <i>Campbell,</i> <span class="citation" data-id="9429191"><a href="/opinion/110930/heckler-v-campbell/#468" aria-description="Citation for case: Heckler v. Campbell">461 U. S. 458, 468-469, n. 12</a></span> (1983).</p>
<p>[1]  "Although the searches and seizures which deeply concerned the colonists, and which were foremost in the minds of the Framers, were those involving invasions of the home, it would be a mistake to conclude, as the Government contends, that the Warrant Clause was therefore intended to guard only against intrusions into the home. First, the Warrant Clause does not in terms distinguish between searches conducted in private homes and other searches. There is also a strong historical connection between the Warrant Clause and the initial clause of the Fourth Amendment, which draws no distinctions among `persons, houses, papers, and effects' in safeguarding against unreasonable searches and seizures." <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#8" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 8</a></span>.</p>
<p>[2]  "The judicial warrant has a significant role to play in that it provides the detached scrutiny of a neutral magistrate, which is a more reliable safeguard against improper searches than the hurried judgment of a law enforcement officer `engaged in the often competitive enterprise of ferreting out crime.' <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). Once a lawful search has begun, it is also far more likely that it will not exceed proper bounds when it is done pursuant to a judicial authorization `particularly describing the place to be searched and the persons or things to be seized.' Further, a warrant assures the individual whose property is searched or seized of the lawful authority of the executing officer, his need to search, and the limits of his power to search." <i>Id.,</i> at 9.</p>
<p>[3]  See <i>id.,</i> at 10-11. The earliest case cited by Chief Justice Burger was Justice Field's opinion in <i>Ex parte Jackson,</i> <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span> (1878).</p>
<p>[4]  "Having probable cause to believe that contraband was being driven away in the taxi, the police were justified in stopping the vehicle, searching it on the spot, and seizing the suitcase they suspected contained contraband. See <i>Chambers</i> v. <i>Maroney,</i> [<span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52</a></span> (1970)]. At oral argument, respondent conceded that the stopping of the taxi and the seizure of the suitcase were constitutionally unobjectionable. See Tr. of Oral Arg. 30, 44-46." <i>Arkansas</i> v. <i>Sanders,</i> <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 761-762</a></span>.</p>
<p>[5]  "[B]ecause each exception to the warrant requirement invariably impinges to some extent on the protective purpose of the Fourth Amendment, the few situations in which a search may be conducted in the absence of a warrant have been carefully delineated and `the burden is on those seeking the exemption to show the need for it.' <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951)." <i>Id.,</i> at 759-760.</p>
<p>[6]  In framing the question for decision we stated: "Unlike <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span></i> and <i>Sanders,</i> in this case police officers had probable cause to search respondent's entire vehicle." <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#817" aria-description="Citation for case: United States v. Ross">456 U. S., at 817</a></span>.</p>
<p>[7]  Moreover, we quoted the following paragraph from Justice Powell's opinion concurring in the judgment in the intervening case of <i>Robbins</i> v. <i>California,</i> <span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/" aria-description="Citation for case: Robbins v. California">453 U. S. 420</a></span> (1981):
</p>
<p>"`[W]hen the police have probable cause to search an automobile, rather than only to search a particular container that fortuitously is located in it, the exigencies that allow the police to search the entire automobile without a warrant support the warrantless search of every container found therein. See <i>post,</i> at 451, and n. 13 (STEVENS, J., dissentin

[...TRUNCATED 15262 of 135262 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
