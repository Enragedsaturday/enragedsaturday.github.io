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

## GROUP: _overhaul2/lake/cases/Chapman v. United States (1961).json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Chapman v. United States (1961)"
type: case
citation: "365 U.S. 610 (1961)"
parallel_cite: "81 S. Ct. 776; 5 L. Ed. 2d 828"
neutral_cite: 1961 U.S. LEXIS 1396
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-04-03
docket: 175
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-04-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Chapman v. United States (1961)"
  varies_by_point: false
  scope_note: "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106197/chapman-v-united-states/"
  cluster_id: 106197
  opinion_id: 106197
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Progeny (third-party consent)"
related: ["[[Stoner v. California]]"]
aliases: ["Chapman v. United States"]
tags: ["case", "fourth-amendment", "consent", "third-party-consent", "landlord-tenant", "home"]
holding: "A landlord cannot give valid third-party consent to a search of premises currently leased to a tenant; a warrantless entry of the tenant's home on the landlord's authority alone violates the Fourth Amendment."
lake:
  record_id: "Chapman v. United States (1961)"
  status: verified
  projected_at: 2026-07-06
---

# Chapman v. United States (1961)

*365 U.S. 610 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Disambiguation:** This is *Chapman v. United States*, 365 U.S. 610 (1961) (landlord consent). Not to be confused with the unrelated *Chapman v. United States*, 500 U.S. 453 (1991) (LSD carrier-weight sentencing), which is not part of this corpus. A bare `[[Chapman v. United States]]` link resolves here.

## Background
Georgia officers, acting without a warrant but with the consent of the petitioner's landlord, forced open an unlocked window and searched the petitioner's rented house in his absence, finding an unregistered distillery and 1,300 gallons of mash. The landlord, on a social visit, had smelled mash and called police; before the entry he had not exercised any statutory option to forfeit the tenancy. Chapman was convicted of federal liquor-law violations on the seized evidence.

## Issue
Whether a landlord's consent can authorize a warrantless search of premises leased to and occupied by a tenant, rendering the search reasonable under the Fourth Amendment.

## Rule
No. A landlord has no right, absent an express covenant, "forcibly to enter the demised premises without the consent of the tenant," and cannot delegate such a right to police. To uphold a warrantless entry, search, and seizure on the landlord's authority "would reduce the [Fourth] Amendment to a nullity and leave [tenants'] homes secure only in the discretion of [landlords]." — 365 U.S. at 616–617 (quoting *Johnson v. United States*, 333 U.S. at 14). ^pin-617

"It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be [reversed]." — *Id.* at 618. ^pin-618

## Application
The landlord had merely entered to "view waste," but the entry was forcible (a window was forced) and its purpose was to search for distilling equipment, not to view waste; the landlord had not forfeited the tenancy and a nuisance abatement could proceed only on the solicitor-general's information. He therefore had no authority to enter or to consent, and his permission could not substitute for a warrant covering the tenant's home. The seizure was unlawful.

## Conclusion
The warrantless search authorized only by the landlord's consent violated the Fourth Amendment; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chapman*'s rule that a landlord cannot consent to a search of the tenant's occupied premises remains good law and is consistent with the later common-authority consent doctrine (*[[United States v. Matlock]]*) and reaffirmed in principle by [[Stoner v. California]] (hotel clerk) and *[[Georgia v. Randolph]]*.

## Appears on
- [[Consent Searches]] — *Progeny ([[Consent Searches|third-party consent]])*

## Sources
- *Chapman v. United States*, 365 U.S. 610 (1961) — https://www.courtlistener.com/opinion/106197/chapman-v-united-states/ — pinpoints: 616–617, 618.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f833b132e9622604", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chapman v. United States (1961)"}, "payload": {"all": [{"cite": "365 U.S. 610", "page": "610", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "365"}, {"cite": "81 S. Ct. 776", "page": "776", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "5 L. Ed. 2d 828", "page": "828", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "5"}, {"cite": "1961 U.S. LEXIS 1396", "page": "1396", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}], "display": "365 U.S. 610", "official": {"cite": "365 U.S. 610", "page": "610", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "365"}, "official_selection_present": true, "record_id": "Chapman v. United States (1961)"}}
{"assertion_id": "0c000487eed1d161", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-617", "record_id": "Chapman v. United States (1961)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-617", "pinpoint_status": "slip-only", "quote": "--- # Chapman v. United States (1961) *365 U.S. 610 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Disambiguation:** This is *Chapman v. United States*, 365 U.S. 610 (1961) (landlord consent). Not to be confused with the unrelated *Chapman v. United States*, 500 U.S. 453 (1991) (LSD carrier-weight sentencing), which is not part of this corpus. A bare `[[Chapman v. United States]]` link resolves here. ## Background Georgia officers, acting without a warrant but with the consent of the petitioner's landlord, forced open an unlocked window and searched the petitioner's rented house in his absence, finding an unregistered distillery and 1,300 gallons of mash. The landlord, on a social visit, had smelled mash and called police; before the entry he had not exercised any statutory option to forfeit the tenancy. Chapman was convicted of federal liquor-law violations on the seized evidence. ## Issue Whether a landlord's consent can authorize a warrantless search of premises leased to and occupied by a tenant, rendering the search reasonable under the Fourth Amendment. ## Rule No. A landlord has no right, absent an express covenant,", "quote_fidelity": "mismatch", "record_id": "Chapman v. United States (1961)", "star_marker": null}}
{"assertion_id": "282349af5726244c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-618", "record_id": "Chapman v. United States (1961)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-618", "pinpoint_status": "slip-only", "quote": "It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be [reversed].", "quote_fidelity": "mismatch", "record_id": "Chapman v. United States (1961)", "star_marker": null}}
{"assertion_id": "450490c6b4bf4a9c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chapman v. United States (1961)"}, "payload": {"as_of_content": "1961-04-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chapman v. United States (1961)", "scope_note": "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph.", "varies_by_point": false}}
```

### lake record — Chapman v. United States (1961)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chapman v. United States (1961)",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chapman v. United States",
    "case_name_short": "Chapman",
    "case_name_full": "Chapman v. United States",
    "input_case_name": "Chapman v. United States (1961)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-04-03",
    "year": 1961,
    "docket": "175",
    "cluster_id": 106197,
    "lead_opinion_id": 106197,
    "sibling_ids": [
      106197,
      9422156,
      9422157,
      9422158
    ],
    "absolute_url": "/opinion/106197/chapman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 106282,
        "score": 20,
        "case_name": "Poe v. Ullman"
      },
      {
        "cluster_id": 106195,
        "score": 20,
        "case_name": "Ferguson v. Georgia"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 610",
      "volume": "365",
      "reporter": "U.S.",
      "page": "610",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 776",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "776",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 828",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1396",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 610",
        "volume": "365",
        "reporter": "U.S.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 776",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "776",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 828",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "828",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1396",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1396",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 610",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 610",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "--- # Chapman v. United States (1961) *365 U.S. 610 (1961)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> > **Disambiguation:** This is *Chapman v. United States*, 365 U.S. 610 (1961) (landlord consent). Not to be confused with the unrelated *Chapman v. United States*, 500 U.S. 453 (1991) (LSD carrier-weight sentencing), which is not part of this corpus. A bare `[[Chapman v. United States]]` link resolves here. ## Background Georgia officers, acting without a warrant but with the consent of the petitioner's landlord, forced open an unlocked window and searched the petitioner's rented house in his absence, finding an unregistered distillery and 1,300 gallons of mash. The landlord, on a social visit, had smelled mash and called police; before the entry he had not exercised any statutory option to forfeit the tenancy. Chapman was convicted of federal liquor-law violations on the seized evidence. ## Issue Whether a landlord's consent can authorize a warrantless search of premises leased to and occupied by a tenant, rendering the search reasonable under the Fourth Amendment. ## Rule No. A landlord has no right, absent an express covenant,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-618",
      "page": null,
      "quote": "It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be [reversed].",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-04-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chapman v. United States (1961)",
    "varies_by_point": false,
    "scope_note": "Landlord-cannot-consent rule remains good law; consistent with the later common-authority consent framework (Matlock) and reaffirmed in spirit by Stoner v. California and Georgia v. Randolph.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
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
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adrian Biera v. State",
          "cluster_id": 3096517,
          "cite": [
            "391 S.W.3d 204",
            "2012 WL 5199374",
            "2012 Tex. App. LEXIS 8782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. M. Santulli, LLC",
          "cluster_id": 5630495,
          "cite": [
            "29 Misc. 3d 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gibson",
          "cluster_id": 3975410,
          "cite": [
            "164 Ohio App. 3d 558",
            "2005 Ohio 6380",
            "843 N.E.2d 224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barocio v. State",
          "cluster_id": 1426797,
          "cite": [
            "117 S.W.3d 19",
            "2003 WL 21402504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barocio, Xavier Hernandez v. State",
          "cluster_id": 2928784,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edward Wilhelm v. John A. Boggs, Deputy, and Joseph Tanner, Deputy",
          "cluster_id": 777694,
          "cite": [
            "290 F.3d 822",
            "2002 U.S. App. LEXIS 9590",
            "2002 WL 1021362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richardson v. State",
          "cluster_id": 2446882,
          "cite": [
            "865 S.W.2d 944",
            "1993 Tex. Crim. App. LEXIS 167",
            "1993 WL 431499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Woodberry v. State",
          "cluster_id": 1510666,
          "cite": [
            "856 S.W.2d 453",
            "1993 Tex. App. LEXIS 1887",
            "1993 WL 117161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Broge",
          "cluster_id": 2062103,
          "cite": [
            "511 N.E.2d 1321",
            "159 Ill. App. 3d 127",
            "111 Ill. Dec. 26",
            "1987 Ill. App. LEXIS 2947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sonja Yvette Osunegbu",
          "cluster_id": 490555,
          "cite": [
            "822 F.2d 472",
            "1987 U.S. App. LEXIS 9851"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stoner v. California",
          "cluster_id": 106777,
          "cite": [
            "11 L. Ed. 2d 856",
            "84 S. Ct. 889",
            "376 U.S. 483",
            "1964 U.S. LEXIS 1579"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Poe v. Ullman",
          "cluster_id": 106282,
          "cite": [
            "6 L. Ed. 2d 989",
            "81 S. Ct. 1752",
            "367 U.S. 497",
            "1961 U.S. LEXIS 1953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
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
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxwell v. State",
          "cluster_id": 2105782,
          "cite": [
            "73 S.W.3d 278",
            "2002 Tex. Crim. App. LEXIS 84",
            "2002 WL 562264"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold B. Dorman v. United States",
          "cluster_id": 293653,
          "cite": [
            "435 F.2d 385",
            "140 U.S. App. D.C. 313",
            "1970 U.S. App. LEXIS 9785"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chapman v. United States (1961):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODY0NjcyMDAwMDAmcz0yMzI1MzI1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODImcz0xMTIwNjI0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
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
    "complete_query": "cites:(106197 OR 9422156 OR 9422157 OR 9422158)",
    "indexed_citing_opinions": 576,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106197,
        "count": 549,
        "count_source": "search"
      },
      {
        "opinion_id": 9422156,
        "count": 36,
        "count_source": "search"
      },
      {
        "opinion_id": 9422157,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422158,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 891,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chapman-v-united-states-1961.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1OTA1OTMmcz00NDM0NDU4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106197+OR+9422156+OR+9422157+OR+9422158%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106197,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 249324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106197,
        "cited_id": 3400993,
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
    "date_created": "2026-07-04T23:53:11Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:57:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:53:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chapman v. United States (1961)

```
<div>
<center><b><span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U.S. 610</a></span> (1961)</b></center>
<center><h1>CHAPMAN<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 175.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 23, 1961.</center>
<center>Decided April 3, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><i>J. Sewell Elliott</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Robert S. Erdahl</i> argued the cause for the United States. On the brief were <i>Solicitor General Rankin, Assistant Attorney General Wilkey, Beatrice Rosenberg</i> and <i>Kirby W. Patterson.</i></p>
<p>MR. JUSTICE WHITTAKER delivered the opinion of the Court.</p>
<p>Acting without a warrant but with the consent of the petitioner's landlord, Georgia law enforcement officers enteredthrough an unlocked windowand searched petitioner's rented house, in his absence, and there found and seized an unregistered "distillery" and 1,300 gallons of "mash." Soon afterward petitioner was indicted in <span class="star-pagination">*611</span> the District Court for the Middle District of Georgia for violations of the federal liquor laws.<sup>[1]</sup> He promptly moved the court for an order suppressing the use of the seized items as evidence at his impending criminal trial on the ground that they were obtained by an unlawful search and seizure. After hearing evidence, the court held that the search and seizure were lawful under federal standards and denied the motion.</p>
<p>At the subsequent trial, the evidence sought to be suppressed was offered and received, over petitioner's renewed objections. Upon that evidence, the jury found petitioner guilty, and the court sentenced him to imprisonment for a year and a day. On appeal, the Court of Appeals for the Fifth Circuit affirmed. <span class="citation" data-id="249324"><a href="/opinion/249324/elmer-samuel-chapman-v-united-states/" aria-description="Citation for case: Elmer Samuel Chapman v. United States">272 F. 2d 70</a></span>. To examine petitioner's claim that the courts below violated the standards governing admissibility of timely challenged evidence in federal courts, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./363/836/">363 U. S. 836</a></span>.</p>
<p>The relevant evidence is not controverted. It shows the following: One Bridgaman, and another, owned a dwelling house in a wooded area near the Macon, Georgia, airport, which they commonly rented through a rental agency. Understanding that the house had been rented to a new tenant, Bridgaman, on Sunday, February 16, 1958, went to the house for the purpose of inviting the tenants to attend church. Upon arrival he noted a strong "odor of mash" about the house. There was no response to his knock, and, although he tried to do so, he was unable to see into the house. He then returned to his home and, by telephone, advised the local police department of his observations. Soon afterward two local police officers, Harbin and Chance, arrived at Bridgaman's home, and the three then went to the rented <span class="star-pagination">*612</span> house. They noticed a strong odor of "whiskey mash" coming from the house. After their knock at the door failed to produce a response, they walked around the house and tried to look into it but were unable to do so because the shades were down. They found that all of the windows were locked, save one in the bathroom. The officers testified that Bridgaman told them "to go in the window and see what['s] what in there." Bridgaman's version of what he said was: "If it's what I think it is, what it smells like, yes, you can have my permission to go in." Thereupon they opened the bathroom window and, with the assistance of Bridgaman and Chance, Harbin entered the house through that opening. Upon entering the house he saw a complete and sizable distillery and 1,300 gallons of mash located in the living room. Apart from some accessories, containers and firewood, there was nothing else in the house. Harbin then called to Chance that he had found a large still and asked him "to go get some help." Chance immediately leftdropping Bridgaman at his hometo call the federal officers. While the federal officers were en route to the house, petitioner drove up, unlocked the front door, entered the house and was immediately arrested by Harbin. The federal officers soon arrived and took custody of petitioner. They also saved samples of the mash, took various pictures of the scene and then destroyed the still and its contents. Neither the state nor the federal officers had any warrant of any kind.</p>
<p>Although the decisions below were rendered prior to this Court's decision in <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span>, the doctrine of that case is not here involved, as the lower courts explicitly rested their determinations on the ground that the search and seizure, though made by state officers, were valid under federal standards. Hence, the only question here is whether those determinations were correct. We believe that they were not.</p>
<p><span class="star-pagination">*613</span> The Fourth Amendment to the United States Constitution provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>Until <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>, this Court had never directly decided, but had always assumed, "that one's house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest therein" (<span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States"><i>id.,</i> at 32</a></span>), but that case explicitly decided that "Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are . . . unlawful notwithstanding facts unquestionably showing probable cause." <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States"><i>Id.,</i> at 33</a></span>.</p>
<p>At least two decisions of this Court are closely relevant. <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, and <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>. In the <i><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></i> case, Federal agents had received "complaints" respecting activities at a certain garage in Baltimore and decided to "investigate." As they "approached the garage they got the odor of whiskey coming from within." Looking through a small opening, they saw a number of cardboard cases. Although they had no warrant of any kind, they "broke the fastening upon a door, entered and found one hundred twenty-two cases of whiskey. No one was within the place and there was no reason to think otherwise. While the search progressed, Taylor came from his house and was put under arrest. The search and seizure were undertaken with the hope of securing evidence upon which to indict and convict him." <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#5" aria-description="Citation for case: Taylor v. United States"><i>Id.,</i> at 5</a></span>.</p>
<p><span class="star-pagination">*614</span> In condemning that search and seizure, this Court said that the officers "had abundant opportunity [to obtain a warrant] and to proceed in an orderly way even after the odor had emphasized their suspicions; there was no probability of material change in the situation during the time necessary to secure such warrant. Moreover, a short period of watching would have prevented any such possibility. . . . Prohibition officers may rely on a distinctive odor as a physical fact indicative of possible crime; but its presence alone does not strip the owner of a building of constitutional guarantees against unreasonable search." The Court concluded that "in any view, the action of the agents was inexcusable and the seizure unreasonable. The evidence was obtained unlawfully and should have been suppressed." <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States"><i>Id.,</i> at 6</a></span>.</p>
<p>In the <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span></i> case, state narcotic agents, while in the hallway of a hotel, recognized a strong odor of burning opium coming from a particular room. Without knowing who was occupying the room, they knocked and, after some delay, the door was opened. The agents then entered the room and told the occupant "to consider [herself] under arrest because we are going to search the room." The search produced incriminating opium and smoking apparatus which was warm from recent use. The District Court refused to suppress that evidence and admitted it over defendant's objection at the trial and she was convicted. In reversing, this Court said:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. <span class="star-pagination">*615</span> Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. . . . The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.</blockquote>
<blockquote>"There are exceptional circumstances in which, on balancing the need for effective law enforcement against the right of privacy, it may be contended that a magistrate's warrant for search may be dispensed with. But this is not such a case." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-15</a></span>.</blockquote>
<p>Here, as in that case, "No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the constitutional requirement. No suspect was fleeing or likely to take flight. The search was of permanent premises, not of a movable vehicle. No evidence or contraband was threatened with removal or destruction, except perhaps the fumes which we suppose in time would disappear." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S., at 15</a></span>.</p>
<p>We think it must be concluded here, as it was in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>,</i> that "If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, <span class="star-pagination">*616</span> it is difficult to think of a case in which it should be required." <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#15" aria-description="Citation for case: Johnson v. United States">333 U. S., at 15</a></span>. See also <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>; <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">357 U. S. 493</a></span>.</p>
<p>Actually, the Government does not contend in this Court that this search and seizure, as such, met the standards of the Fourth Amendment. Instead, it says: "Our position is that when the landlord, paying a social call, found good reason to believe that the leased premises were being wasted and used for criminal purposes, he had authority to enter as a matter of right and to bring officers with him for this purpose." It says that, under the common law, a landlord has an absolute right to enter the demised premises "to view waste," and that he should be able to exercise that right through law enforcement officers to whom he has delegated his authority. But it cites no Georgia or other case holding that a landlord, in the absence of an express covenant so permitting, has a right forcibly to enter the demised premises without the consent of the tenant "to view waste." And, so far as our research discloses, no Georgia case so holds.</p>
<p>The only relevant authority cited by the Government is a statement from Tiffany, Landlord and Tenant (1910 ed.), § 3. b. (2), p. 9, that "It has also been said that [the landlord] may enter to `view waste,' that is, to determine whether waste has been committed, <i>provided at least that this does not involve the breaking of windows or doors</i> . . . ."<sup>[2]</sup> (Emphasis added.) There are several answers to this contention. First, here the landlord and the officers forced open a window to gain entry to the premises. Second, "their purpose in entering was [not to view waste but] to search for distilling equipment . . . ." <i>Jones</i> v. <i>United States, supra,</i> at 500. Third, to uphold <span class="star-pagination">*617</span> such an entry, search and seizure "without a warrant would reduce the [Fourth] Amendment to a nullity and leave [tenants'] homes secure only in the discretion of [landlords]." <i>Johnson</i> v. <i>United States, supra,</i> at 14. Moreover, "it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical. . . . [W]e ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266-267</a></span>.</p>
<p>After pointing to the fact that a Georgia statute (Title 58 Ga. Code § 106) provides that the unlawful manufacture of distilled liquor on rented premises shall work a forfeiture of the rights of the tenant, at the option of the landlord, and that another (Title 58 Ga. Code § 109) provides that use of a structure for that purpose constitutes a nuisance, the Government argues that, inasmuch as he used the demised premises for the illicit manufacture of distilled liquor, petitioner had forfeited all rights in the premises, and the landlord thus acquired the right forcibly to enter to abate the nuisance, and that he could and did delegate that right to the officers. But it is clear that, before the officers made the forcible entry, the landlord did not know that the premises were being used for the manufacture of liquor, nor had he exercised his statutory option to forfeit the tenancy for such a cause. And the Supreme Court of Georgia has held that a proceeding to abate a nuisance under § 109 "must proceed for the public on information filed by the solicitor-general of the circuit." <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/#417" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416, 417</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/#521" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520, 521</a></span>.</p>
<p><span class="star-pagination">*618</span> It follows that this search was unlawful, and since evidence obtained through that search was admitted at the trial, the judgment of the Court of Appeals must be</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE BLACK concurs in the result.</p>
<p>MR. JUSTICE FRANKFURTER, concurring in the judgment.</p>
<p>Since searches and seizures play such a frequent role in federal criminal trials, it is most important that the law on searches and seizures by which prosecutors and trial judges are to be guided should be as clear and unconfusing as the nature of the subject matter permits. The course of true law pertaining to searches and seizures, as enunciated here, has notto put it mildlyrun smooth. The Court's opinion in this case is hardly calculated, I regret to say, to contribute to clarification. The reasoning by which the Court reaches its result would be warranted were <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948), still law. While the Court does not explicitly rely on it, underlying the present decision is the approach of <i><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span>.</i> That decision was a short-lived deviation from the course of decisions preceding it and it was specifically overruled by <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950). Since the <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> case expresses the prevailing view, the decision in this case runs counter to it. The Court does rely on <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, although that case was seriously impaired by <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S., at 66</a></span>, dissenting opinion, at 85.</p>
<p>Surely it is fair to say that the lower courts and prosecutors have a right to proceed on the assumption, on the basis of controlling decisions, that whether or not a search is "unreasonable" turns on the circumstances presented by a particular situation, as a matter of substantive determination. On that test, I find it very difficult to conclude that a police officer may not deem adequate <span class="star-pagination">*619</span> the authorization of a landlord to enter his house without a search warrant where he has solid ground for believing that his lessee is utilizing the house as an illegal distillery. It seems to me that it is not at all "unreasonable" not to charge a local police officer with knowledge of the law of Georgia regarding the power of a landlord to abate a nuisance in his house. Apart from charging a policeman with knowledge of the local law relating to landlord and tenant, he certainly would not acquire that knowledge by reading the only Georgia case to which the Court's opinion refers, <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520</a></span>, a case which deals with the procedure of a solicitor general of a Georgia circuit in abating a nuisance by an injunction and tells nothing about the remedy of self-help by a landlord.</p>
<p>In joining the Court's judgment, I do so on the basis of the views set forth in my dissents in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#594" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 594</a></span>; <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span>; <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155</a></span>; <i>United States</i> v. <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#68" aria-description="Citation for case: United States v. Rabinowitz"><i>Rabinowitz, supra,</i> at 68</a></span>. As these opinions elucidate, the Fourth Amendment incorporates a guiding history that gives meaning to the phrase "unreasonable searches and seizures" contained within it far beyond the meaning of the phrase in isolation and taken from the context of that history and its gloss upon the Fourth Amendment. The Amendment in its entirety in the setting of that history decidedly does not leave the phrase "unreasonable searches and seizures" at large.</p>
<p>MR. JUSTICE CLARK, dissenting.</p>
<p>The Constitution condemns only an <i>unreasonable</i> search. As my Brother FRANKFURTER says, that determination "turns on the circumstances presented by a particular situation."<sup>[1]</sup></p>
<p><span class="star-pagination">*620</span> As I read the record, Bridgaman had rented a house to Chapman. On a Sunday morning he called at the house to invite Chapman to church services. However, Bridgaman found Chapman gone, the house locked up and an "awful scent" of whiskey mash all over the place, including an open but empty cellar. He reported these facts to state officers and, at his suggestion, two officers accompanied him to the house. They too smelled, as the Court says, "a strong odor of `whiskey mash' coming from the house."</p>
<p>Under Georgia law, the use of premises for the manufacture or the keeping of liquor for disposition works "a forfeiture of the rights of any lessee or tenant under any lease or contract for rent . . . ."<sup>[2]</sup> Bridgaman advised the officers he was the owner of the house, had it leased out, and "instructed" officer Harbin to enter it and "see what['s] what in there." The officers found a bathroom window unlocked. Bridgaman "told" the officers "to go in the window" and assisted in "boosting" officer Harbin into the window and on into the house. Inside, the officer found a still set up for operation and 1,300 gallons of whiskey mash in the vats. There was neither household furniture nor other evidence of residential occupancy.</p>
<p>The Court sets aside Chapman's conviction on the ground that this search without a warrant was "unreasonable." For the life of me I cannot see why this is true. I agree with a unanimous Court of Appeals that "under the circumstances of the search here made by the State officers, no illegality was shown."</p>
<p>The "reasonableness" of the search hinges on the rights of the landlord under Georgia law in such a situation. <span class="star-pagination">*621</span> This Court refuses to honor the clear language of § 106, apparently because the Government "cites no Georgia or other case" holding that a landlord may, under the circumstances here, enter on his premises. Instead, it bases its reversal on <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, and <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, involving entry by officers, unaccompanied by the landlord, into a <i>home</i> without a search warrant when there was ample time to secure one. This doctrine, established by <i>Trupiano</i> v. <i>United States,</i> <span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span> (1948), was repudiated and specifically overruled only two years later in <i>united States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, at 66</a></span>. Furthermore, none of the cases cited by the Court involve the landlord-tenant circumstance controlling here.</p>
<p>As to Georgia law, the Court itself finds that "no Georgia case" holds that landlords have a right of entry as was exercised by Bridgaman here. It says that, first, the window was forced, second, the entry was for purposes of search and, third, affirmance would " `leave [tenants'] homes secure only in the discretion of [landlords]' " (quoting from <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson, supra</a></span></i>). The obvious answer to that is: "Chapman was a tenant no more!" The statute provided for the forfeiture of his lease at his lessor's option when he began making whiskey on the premises. And Bridgaman so elected when he directed the officers to enter the house. It was Chapman who was the trespasser, not Bridgaman. The latter was merely repossessing his property, not abating a nuisance. Therefore, § 109 of the Georgia Code, cited by the Court, has no bearing here for that statute merely provides that the Attorney General "may" abate such a nuisance. It has no reference to landlords <i>qua</i> landlords. Indeed, the officers here could have abated the nuisance without judicial help by destroying the still and all of its paraphernalia under authority of 58 Ga. Code Ann. (Cum. <span class="star-pagination">*622</span> Supp. 1958) § 207.<sup>[3]</sup> Likewise, <i>Kilgore</i> v. <i>Paschall,</i> <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">202 Ga. 416</a></span>, <span class="citation" data-id="3400993"><a href="/opinion/3406573/kilgore-v-paschall/" aria-description="Citation for case: Kilgore v. Paschall">43 S. E. 2d 520</a></span>, also cited by the Court, is entirely inapposite. That case merely holds that the special statutory authorization, under an entirely different provision of the Georgia Code, § 110, to close up "blind tigers," <i>i. e.,</i> public places of disrepute where gambling, drinking, etc., are carried on, must be brought by the Solicitor of the county wherein they are located. But even if it did hold that actions under § 109 must be brought by the Solicitor, that ruling would have no effect here, precisely because the present factual situation does not come under § 109 but under § 106 and § 207, <i>supra.</i></p>
<p>Furthermore, there was ample reason for not getting a warrant here. It was Sunday afternoon and, as the Georgia officer testified, he had "never got one on Sunday." "I don't think you can." And this was buttressed by his further statements: "Well, I didn't feel no call to get one." "The man that owned the house, he was there and he told us to go in the window and see what['s] what in there, so we went on in." This shows a complete reliance by the officers on Bridgaman's direction to enter the house. This, I say, made the search entirely reasonable and therefore valid under the Fourth Amendment.</p>
<p>Every moment of every day, somewhere in the United States, a law enforcement officer is faced with the problem of search and seizure. He is anxious to obey the rules that circumscribe his conduct in this field. It is the duty of this Court to lay down those rules with such clarity and understanding that he may be able to follow them. For some years now the field has been muddy, but today the Court makes it a quagmire. It fashions a novel rule, supporting it with an old theory long since overruled. <span class="star-pagination">*623</span> If <i><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span></i> is no longer law the Court should say so. It is disastrous to law enforcement to leave at large the inconsistent rules laid down in these cases. It turns the wellsprings of democracylaw and orderinto a slough of frustration. It turns crime detection into a game of "cops and robbers." We hear much these days of an increasing crime rate and a breakdown in law enforcement. Some place the blame on police officers. I say there are others that must shoulder much of that responsibility.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation no-link">26 U. S. C. §§ 5601</span>, 5606.</p>
<p>[2]  Only ancient English cases are cited in support of the text.</p>
<p>[1]  I join in his opinion except for the last paragraph in which he concurs in the judgment of the Court.</p>
<p>[2]  58 Ga. Code Ann., § 106. Aside from eviction, there are no statutory procedural requirements as to forfeiture, the forfeit operating by virtue of § 106 at the option of the landlord.</p>
<p>[3]  Section 207 provides in pertinent part:
</p>
<p>"[W]henever said apparatus [for making liquor is] . . . found or discovered by any sheriff, . . . the same shall be summarily destroyed and rendered useless by him without any formal order of the court."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Chatrie v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: "Chatrie v. United States"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-06-29
docket: 25-112
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2026-06-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chatrie v. United States
  varies_by_point: false
  scope_note: "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 → lead opinion 11349205)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/"
  cluster_id: 10881683
  opinion_id: 11349205
  identity_checked: false
homes:
  - page: "[[Reverse-Keyword and Geofence Warrants]]"
    role: "Key — Anchor (geofence exposition home)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key — geofence (cross-ref)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carpenter v. United States]]", "[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[The Warrant Requirement]]", "[[Standing to Challenge a Search]]", "[[The Exclusionary Rule]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "third-party-doctrine"]
holding: "Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in the record of one's phone's location, even for a short period and even when the data is held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding."
lake:
  record_id: Chatrie v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Chatrie v. United States

*609 U.S. ___ (2026)* (No. 25-112) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-verified 2026-07-02: cluster 10881683 → lead opinion 11349205 — see frontmatter/Sources. -->

## Background
Investigating a 2019 armed robbery of a Midlothian, Virginia credit union, police obtained a **geofence warrant** directing Google to disclose **Location History** for every device within a 150-meter radius of the bank during a roughly one-hour window around the robbery. That "reverse-location" process ultimately identified Okello Chatrie. He moved to suppress, arguing that compelling Google to produce his Location History was a warrantless Fourth Amendment search. The Fourth Circuit — on rehearing **[[Reading and Citing Cases#en-banc|en banc]]**, splitting 7–7 on whether a search occurred — affirmed the denial of suppression (136 F.4th 100), teeing up the threshold question for the Supreme Court.

## Issue
Whether the government conducts a Fourth Amendment "search" when it acquires a person's Google Location History (geofence) data — records of a cell phone's location — held by a third-party provider.

## Rule
Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words: "An individual has a reasonable expectation of privacy in records about his cell phone's location, and police intrude on that constitutionally protected interest when they demand the information—even though for only a limited time, and from a third-party tech company." The protection holds **even for a limited time** and **even though a third party holds the records**. The Court rejected the argument that Location History (off by default / opt-in) is "voluntarily shared" and thus stripped of protection by the third-party doctrine, **applying and extending *[[Carpenter v. United States|Carpenter]]*** to bulk reverse-location data. *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) (slip op.). ^pin-op

Critically, the Court **did not** hold geofence warrants categorically unconstitutional. It **expressly declined** to decide whether *this* geofence warrant satisfied the Fourth Amendment's **probable-cause and [[Particularity|particularity]]** requirements, leaving that question for remand.

## Application
Police compelled Google to produce Location History for all devices in a geographic area and time window — an "all-encompassing" record of individuals' movements generated automatically and held by a third party. Under *[[Carpenter v. United States|Carpenter]]*'s logic, that acquisition invaded a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] and was therefore a search; the third-party/opt-in rationale the Fourth Circuit panel had relied on did not defeat that protection.

## Conclusion
Acquiring geofence Location History is a Fourth Amendment search. The judgment was **[[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]** for the lower courts to decide the **probable-cause and [[Particularity|particularity]]** of the geofence warrant — the question the Court left open. **Kagan, J.**, delivered the opinion of the Court, joined by Roberts, C.J., and Sotomayor, Kavanaugh, and Jackson, JJ.; Jackson, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]], joined by Sotomayor, J.; Gorsuch, J., concurred in the judgment (making the judgment **6–3**); Alito, J., dissented, joined by Thomas, J., as to Part I and by Barrett, J., as to Parts II–B, II–C–1, and II–C–2; Barrett, J., filed a separate [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** anchor on the geofence search-threshold question.
- **Doctrinal effect:** **RESOLVES** the former circuit split on whether acquiring geofence Location History is a *search* (5th Cir. *[[United States v. Smith (2024)|Smith]]* = yes; 4th Cir. [[Reading and Citing Cases#en-banc|en banc]] *Chatrie* = fractured) — **it is a search**. *[[Smith v. Maryland|Smith]]*'s further holding that geofence warrants are "modern-day general warrants" and **categorically unconstitutional** was **not** adopted; it is now the persuasive minority position feeding the **[[Reading and Citing Cases#on-remand|remanded]]** probable-cause/[[Particularity|particularity]] question — the new live frontier.
- **CL-confirm: VERIFIED (2026-07-02).** CourtListener **cluster** `10881683` **is** the genuine SCOTUS *Chatrie* (`scotus / 25-112 / 2026-06-29`); its lead opinion is `11349205`, against which the Rule quote above was matched verbatim. The earlier "corrupted object" warning was a cluster-vs-opinion ID mix-up: `10881683` is a *cluster* id, and fetching it from the `/opinions/` endpoint returns an unrelated case — use `/clusters/10881683/` or opinion `11349205` instead. See Sources.

## Appears on
- [[Reverse-Keyword and Geofence Warrants]] — *Key — Anchor (geofence exposition home)*
- [[Reasonable Expectation of Privacy]] — *Key — geofence (cross-ref)*
- [[Third-Party Doctrine & CSLI]] — *Key — Progeny / Refinement*

## Sources
- *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) — **slip opinion (PRIMARY):** https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf — decided June 29, 2026.
- SCOTUSblog case page — https://www.scotusblog.com/cases/chatrie-v-united-states/
- Justia, *Chatrie v. United States*, 609 U.S. ___ (2026) — https://supreme.justia.com/cases/federal/us/609/25-112/
- Cornell LII (Supreme Court text, No. 25-112) — https://www.law.cornell.edu/supremecourt/text/25-112
- Decision below: *United States v. Chatrie*, 136 F.4th 100 (4th Cir. 2025) (en banc) — https://www.courtlistener.com/opinion/10443725/united-states-v-okello-chatrie/
- CourtListener: *Chatrie v. United States* — https://www.courtlistener.com/opinion/10881683/chatrie-v-united-states/ — **verified 2026-07-02** (cluster 10881683 → lead opinion 11349205; case name, docket 25-112, and decision date 2026-06-29 confirmed against the cluster record and opinion text). The earlier "corrupted object" warning was a cluster-vs-opinion ID confusion: `10881683` is the **cluster** id and must not be fetched from the `/opinions/` endpoint (that resolves to an unrelated case); the lead **opinion** id is `11349205`.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "81f9b6abe369c0df", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op", "record_id": "Chatrie v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op", "pinpoint_status": "slip-only", "quote": "when it acquires a person's Google Location History (geofence) data — records of a cell phone's location — held by a third-party provider. ## Rule Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words:", "quote_fidelity": "mismatch", "record_id": "Chatrie v. United States", "star_marker": null}}
{"assertion_id": "66af6b12105f0489", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chatrie v. United States"}, "payload": {"as_of_content": "2026-06-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chatrie v. United States", "scope_note": "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 → lead opinion 11349205).", "varies_by_point": false}}
```

### lake record — Chatrie v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chatrie v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Chatrie v. United States",
    "case_name_short": "Chatrie",
    "case_name_full": "",
    "input_case_name": "Chatrie v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2026-06-29",
    "year": 2026,
    "docket": "25-112",
    "cluster_id": 10881683,
    "lead_opinion_id": 11349205,
    "sibling_ids": [
      11349205
    ],
    "absolute_url": "/opinion/10881683/chatrie-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op",
      "page": null,
      "quote": "when it acquires a person's Google Location History (geofence) data \u2014 records of a cell phone's location \u2014 held by a third-party provider. ## Rule Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**. In the Court's words:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2026-06-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chatrie v. United States",
    "varies_by_point": false,
    "scope_note": "New Binding \u2014 SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-verified 2026-07-02 (cluster 10881683 \u2192 lead opinion 11349205).",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11349205) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "audit_marker": null,
        "proposed_negative_events": 0
      },
      "lane2_top_cited": {
        "query": "cites:(11349205)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "audit_marker": null,
        "proposed_negative_events": 0
      },
      "lane3_recency": {
        "query": "cites:(11349205)",
        "reviewed": 0,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 0,
        "triage_read": 0,
        "triage_snippet_classified": 0
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(11349205)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11349205,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/private/tmp/cssi-lake-s2-live-smoke-20260704/progeny/chatrie-v-united-states.jsonl"
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "C",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T14:23:50Z",
    "date_modified": "2026-07-06T13:36:12Z",
    "warnings": [
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:36:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T14:24:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chatrie v. United States (truncated)

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                    CHATRIE v. UNITED STATES

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE FOURTH CIRCUIT

       No. 25–112.     Argued April 27, 2026—Decided June 29, 2026
On May 20, 2019, a man robbed a credit union in Midlothian, Virginia.
 Local police officers learned from witness interviews and surveillance
 footage that the robber had approached the credit union from a corner
 of an adjacent church while appearing to talk on a cell phone, but they
 could not find out anything more, and the robber remained at large.
 On June 14, the police officers applied to a Virginia magistrate for a
 geofence warrant directed to Google, which would require Google to
 hand over data about the cell phones located within a 150-meter radius
 of the credit union—the so-called “geofence”—near the time of the
 crime. The application described the cell-phone location data Google
 collects through a service called Location History, which records the
 location of a user’s cell phone every two minutes or so. The application
 also explained how that cell-phone location data could help identify the
 robber, possible accomplices, or additional witnesses. The warrant de-
 scribed a three-step process that the police would follow: at step one,
 Google would produce anonymized location data for all cell phones
 within the geofence 30 minutes before to 30 minutes after the robbery;
 at step two, officers would attempt to narrow the list, and Google would
 provide additional anonymized data for that narrowed list, consisting
 of cell-phone locations both inside and outside the geofence during a
 two-hour period surrounding the robbery; and at step three, officers
 would further narrow the list, and Google would turn over identifying
 information, including names and phone numbers, for users on the fi-
 nal list. The magistrate issued the warrant, and through this process,
 Google ultimately produced three cell-phone users’ identifying infor-
 mation, including petitioner Okello Chatrie, whose location data
 showed that he entered the geofence about ten minutes before the rob-
 bery and headed toward a residential area immediately after leaving
2                     CHATRIE v. UNITED STATES

                                  Syllabus

    the bank.
       Following further police work, a federal grand jury charged Chatrie
    with robbery and related firearms offenses, and he moved to suppress
    the information the police obtained from Google. According to Chatrie,
    the officers had acquired that data through a Fourth Amendment
    search, and the warrant ostensibly authorizing that search was inva-
    lid. The District Court found that the geofence warrant “plainly vio-
    lates the rights enshrined in [the Fourth] Amendment” but denied the
    motion based on the good-faith exception to the exclusionary rule. 590
    F. Supp. 3d 901, 905, 937–938. A divided panel of the Fourth Circuit
    affirmed on different reasoning, holding that no search occurred be-
    cause Chatrie “did not have a reasonable expectation of privacy in two
    hours’ worth of Location History data voluntarily exposed to Google.”
    107 F. 4th 319, 325. The Fourth Circuit granted rehearing en banc
    and affirmed in a one-sentence per curiam, with the court dividing
    evenly on whether a Fourth Amendment search had occurred. This
    Court granted certiorari solely on the question whether the police vio-
    lated the Fourth Amendment in obtaining Chatrie’s location data.
Held: Police officers conducted a Fourth Amendment search when they
 acquired Chatrie’s location data from Google because an individual has
 a reasonable expectation of privacy in his cell-phone location infor-
 mation. Pp. 10–33.
    (a) The Fourth Amendment protects individuals’ reasonable expec-
 tations of privacy, and governmental “intrusion into that private
 sphere generally qualifies as a search.” Carpenter v. United States,
 585 U. S. 296, 304. The Amendment’s “basic purpose” is “to safeguard
 the privacy and security of individuals against arbitrary invasions by
 governmental officials,” id., at 303, and it was designed “to place ob-
 stacles in the way of a too permeating police surveillance,” United
 States v. Di Re, 332 U. S. 581, 595. Pp. 10–29.
      (1) In Carpenter, this Court held that accessing cell-site location
 information (CSLI) constitutes a Fourth Amendment search because
 “individuals have a reasonable expectation of privacy in the whole of
 their physical movements,” 585 U. S., at 310. The Court reasoned that
 CSLI provides a “detailed” and “encyclopedic” portrait of a person’s
 whereabouts, id., at 309, and, with that, “an intimate window into a
 person’s life,” id., at 311. Because people “compulsively carry” their
 cell phones “all the time,” the Court explained, a cell phone “tracks
 nearly exactly the movements of its owner,” and thus “faithfully fol-
 lows” him not only through “public thoroughfares [but] into private
 residences, doctor’s offices, political headquarters, and other poten-
 tially revealing locales.” Ibid. The Court further observed that the
 “newfound tracking capacity” that CSLI gives the police “runs against
 everyone”—not just those “under investigation”—and “travel[s] back
                     Cite as: 609 U. S. ___ (2026)                      3

                               Syllabus

in time,” making possible a form of surveillance that would have been
unknown prior to the digital age, id., at 311–312. Carpenter accord-
ingly held that “[a]llowing government access to cell-site records con-
travenes” expectations of privacy. Id., at 311. Pp. 13–15.
     (2) Everything Carpenter relied on to find that law enforcement
officers conducted a Fourth Amendment search when they accessed
CSLI records applies as well or better to the police’s accessing of Loca-
tion History data. First, Location History provides an even more fine-
tuned picture of a person’s movements, pinpointing location within
around twenty meters rather than within sectors of one-eighth to four
square miles; it records location every two minutes or so for a daily
average of 720 chartings rather than 101; and it can estimate elevation
to reveal which floor of a building a phone is on. Second, Location His-
tory allows police to reconstruct “retrospective[ly],” and with no real
effort, people’s comings and goings in any area, enabling “tireless and
absolute surveillance” of any number of people in any number of
places. Carpenter, 585 U. S., at 312. And third, Location History im-
plicates personal privacy interests even more than CSLI, because Lo-
cation History is more the cell-phone user’s own. Most cell-phone users
have no awareness of CSLI records, and would never try to retrieve
them; by contrast, Google users regularly employ Location History as
a personal journal. In that way, Location History resembles other pri-
vate materials—e.g., emails, documents, photographs, or calendars—
that even if stored on Google’s servers, a user reasonably views as his
own and expects to be shielded from the “inquisitive eyes” of the gov-
ernment. Id., at 305. Pp. 16–18.
     (3) The Government’s argument that accessing only a short
amount of cell-phone location information does not count as a Fourth
Amendment search fails. “[E]ven short-term monitoring” can provide
“a wealth of detail about [a person’s] familial, political, professional,
religious, and sexual associations,” United States v. Jones, 565 U. S.
400, 415, and this Court has never understood Fourth Amendment
protections as kicking in only once an intrusion “goes too far,” Pennsyl-
vania Coal Co. v. Mahon, 260 U. S. 393, 415. Where the Fourth
Amendment applies, it applies regardless of “the quality or quantity of
information” the government obtains. Kyllo v. United States, 533 U. S.
27, 37. That approach makes all the more sense when, as with Loca-
tion History, law enforcement officials can select the time-limited set
of materials they want from an all-encompassing database. Pp. 18–23.
     (4) The Government argues that the so-called third-party doctrine
precludes Chatrie from invoking the Fourth Amendment’s protections.
The idea is that in “authoriz[ing] Google to collect, retain, and use” his
location information, Chatrie lost his legitimate expectation of privacy,
and therefore his right to complain of a search. Brief for United States
4                     CHATRIE v. UNITED STATES

                                  Syllabus

    15. But Carpenter refused to apply the third-party doctrine to CSLI,
    and no good reason exists to reach a different result for Location His-
    tory. In Carpenter, the Court rejected application of the third-party
    doctrine to CSLI because such information is “qualitatively different”
    from “telephone numbers and bank records,” 585 U. S., at 309—it is
    incomparably “revealing” and is “not truly ‘shared’ as one normally un-
    derstands the term” given that cell phones are “indispensable to par-
    ticipation in modern society,” id., at 315. Both differentiating features
    apply equally or better to Location History, which is even more “re-
    vealing” than CSLI and is “not truly shared” in the normal sense of
    wanting a third party to see or use it. Id., at 315. The exposure of that
    information to Google is merely what happens when a user avails him-
    self of one of the services on his cell phone. The Government’s argu-
    ment that generating Location History, unlike producing CSLI, is a
    voluntary choice is meritless. That argument ignores how and why
    Google users turn on Location History: Google repeatedly prompts us-
    ers to turn on the service, often warning that devices will not “work
    correctly” otherwise, 2 App. 140–141, while not disclosing in that
    prompt how frequently users’ location information would be recorded,
    how precise it would be, or how it might be given to the government.
    More generally, an app-by-app, feature-by-feature method of granting
    Fourth Amendment protection misapprehends the nature of modern
    cell-phone use, where nearly everything requires some kind of “affirm-
    ative act” beyond “powering up” a given app or service. The Govern-
    ment wishes to disconnect the activities people do on their cell phones
    from the mere act of carrying a turned-on cell phone (the thing that
    generates CSLI), with only the latter receiving assured Fourth Amend-
    ment protection. But the point of carrying smartphones is to use what
    is on them—as Carpenter said, to use the apps and “services they pro-
    vide.” 585 U. S., at 315. Accordingly, a cell-phone user is not to be
    viewed as sharing private information with third parties—which then
    can be freely passed on to the government—just by doing the ordinary
    things cell-phone users do. Pp. 24–29.
       (b) The conclusion that a Fourth Amendment search occurred does
    not resolve this case, because the Fourth Amendment prohibits only
    searches that are “unreasonable.” When law enforcement officials un-
    dertake a search to discover evidence of a crime, the reasonableness
    standard generally requires that they seek a warrant from “a neutral
    and detached magistrate,” Johnson v. United States, 333 U. S. 10, 14,
    who may issue a warrant only when “probable cause is properly estab-
    lished and the scope of the authorized search is set out with particu-
    larity,” Kentucky v. King, 563 U. S. 452, 459. The warrant issued here,
    as described earlier, was an uncommon, multi-step one, and the par-
    ties have contested the legality of each stage of the search process it
                      Cite as: 609 U. S. ___ (2026)                      5

                                Syllabus

  authorized. The Fourth Circuit did not address the questions that un-
  usual warrant raises. Because this is “a court of review, not of first
  view,” Cutter v. Wilkinson, 544 U. S. 709, 718, n. 7, the Court leaves it
  up to the Court of Appeals to decide whether, at each step of the search
  process, the warrant satisfied the Fourth Amendment’s requirements
  of particularity and probable cause. Pp. 29–32.
136 F. 4th 100, vacated and remanded.

   KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SOTOMAYOR, KAVANAUGH, and JACKSON, JJ., joined. JACKSON, J.,
filed a concurring opinion, in which SOTOMAYOR, J., joined. GORSUCH, J.,
filed an opinion concurring in the judgment. ALITO, J., filed a dissenting
opinion, in which THOMAS, J., joined as to Part I, and in which BARRETT,
J., joined as to Parts II–B, II–C–1, and II–C–2. BARRETT, J., filed a dis-
senting opinion.
                        Cite as: 609 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 25–112
                                   _________________


           OKELLO T. CHATRIE, PETITIONER v.
                   UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                                 [June 29, 2026]

   JUSTICE KAGAN delivered the opinion of the Court.
   In recent years, law enforcement officers have employed
so-called geofence warrants to obtain information that tech-
nology companies collect about their users’ cell-phone loca-
tions. Suppose that investigators know a crime was com-
mitted at a particular place and time, but do not have a
suspect. They may draw a “geofence”—a virtual perime-
ter—around the crime scene and get a warrant compelling
a company to hand over data about the cell phones located
in that area near the time of the crime. Following a process
specified in the warrant, the company will turn over the
cell-phone data and eventually identify by name one or
more of the users thus disclosed.
   The geofence warrant at issue here was directed to
Google, and used to solve a bank robbery. Hundreds of mil-
lions of Google users have activated a service called Loca-
tion History, which records the location of a user’s cell
phone every two minutes or so. Through a geofence war-
rant, police officers required Google to turn over Location
History data revealing cell phones within the vicinity of a
bank at around the time it was robbed. At the end of the
multi-step process described in the warrant, Google gave
2               CHATRIE v. UNITED STATES

                     Opinion of the Court

the police three names. The Federal Government soon
charged one of the individuals thus identified, petitioner
Okello Chatrie, with committing the crime.
   Today, we consider how the Fourth Amendment applies
to that use of a geofence warrant. Answering that question
in full would mean deciding whether the police conducted a
Fourth Amendment “search” when they acquired the cell-
phone data leading to Chatrie’s arrest and, if so, whether
that search was reasonable given the features of the war-
rant they employed. We decide the first part of that inquiry
today, concluding that the police conducted a search when
they gained access to Location History data. An individual
has a reasonable expectation of privacy in records about his
cell phone’s location, and police intrude on that constitu-
tionally protected interest when they demand the infor-
mation—even though for only a limited time, and from a
third-party tech company. We leave to the Court of Appeals
the further question whether, given the warrant issued, the
search here was reasonable, meaning that each of its steps
was properly described with particularity and found to be
supported by probable cause.
                            I
                            A
  Modern cell phones, we observed a dozen years ago, are
“such a pervasive and insistent part of daily life that the
proverbial visitor from Mars might conclude they were an
important feature of human anatomy.” Riley v. California,
573 U. S. 373, 385 (2014). Since then, the percentage of
Americans who own smartphones has only increased. To-
day, more than nine in ten Americans own a smartphone.
See W. Bishop, Pew Research Center, Mobile Fact Sheet
(Nov. 20, 2025) (91%); compare A. Smith, Pew Research
Center, Smartphone Ownership—2013 Update (June 5,
2013) (56%). That means they are likely addicted to apps
and other services, many of which collect and store
                    Cite as: 609 U. S. ____ (2026)                   3

                         Opinion of the Court

“detailed information about all aspects of a person’s life.”
Riley, 573 U. S., at 396.
  Among that information is a single fact most pertinent
here: where the user’s cell phone is located at a given time.
Apps of many kinds rely on that datum. Your maps app
wants to help you navigate from Point A (where you are) to
Point B (where you are going). Ride-sharing apps of course
track your location when you are using them, and often do
so even when you are not. Weather apps want to tell you
about local conditions. Fast-food apps want to identify the
closest burger and pizza joints. Fitness apps want to track
your running routes. And so on.
  This case concerns a form of cell-phone location data
called “Location History,” which Google apps collect and
store.1 Location History is what it sounds like—a time-
stamped record of every place a cell phone has been. Every
two minutes or so, Location History draws from an array of
sources to log a cell phone’s location. Those sources include
nearby Wi-Fi networks, Bluetooth beacons, and cell sites,
as well as GPS and IP address information. When com-
bined, the signals tracked can determine a cell phone’s lo-
cation within 20 meters. They can also ascertain a phone’s
elevation, and thus reveal which floor within a building the
phone is on. By all accounts, those features make Location
History “the most sweeping, granular, and comprehensive
tool” existing today for collecting and storing location data.
590 F. Supp. 3d 901, 907 (ED Va. 2022).
  Google repeatedly prompts users to enable Location His-
tory, and over 500 million users worldwide have done so.
The first prompt comes when a user initially establishes a
Google account. If that spur is ignored, another will arrive
when a user sets up a Google app—like Google Assistant,
——————
  1 Throughout this opinion, we describe how Location History worked at

the time the warrant at issue was executed. As noted below, Google has
since then instituted a significant change, which apparently insulates
Location History data from geofence warrants. See infra, at 4, n. 2.
4                  CHATRIE v. UNITED STATES

                         Opinion of the Court

Google Maps, or Google Photos—on his phone or other de-
vice. Android (though not iPhone) users are specifically
warned that their devices will not “work correctly” unless
they turn on Location History. 2 App. 140–141. And once
a user does so, the service runs—and runs constantly—in
the background. Regardless whether the user has a Google
app open—or whether he is using his phone at all—Loca-
tion History remains active. Indeed, it continues to work
even if the user deletes the app through which he first
turned it on. Location History stops only if a user affirma-
tively stops it. Sans that intervention, it tracks and tracks
and tracks a user’s cell phone (and other devices).
   Google stores all Location History data in the cloud, ra-
ther than on a user’s device—though that choice makes no
real difference to the user. “Cloud computing” refers to “the
capacity of Internet-connected devices to display data
stored on remote servers rather than on the device itself.”
Riley, 573 U. S., at 397. Because it exists, Google can store
information on its own servers, while the user can view it
as if stored on his cell phone. Such remote storage, we have
explained, is common: “Cell phone users often may not
know whether particular information is stored on the device
or in the cloud, and it generally makes little difference.”
Ibid. So, for example, Google usually stores users’ emails,
documents, and photographs on company servers instead of
on individual devices. See Brief for Google LLC as Amicus
Curiae 3, 37–38. And the same is true of the information
generated by Location History, which is stored in a single
central repository on Google’s servers.2 That data exists
someplace remote, but a user sees it—and the content
——————
   2 Except that in July 2025, years after the geofence warrant used in

this case, Google made a change: It now stores Location History data on
individual users’ devices rather than on its own servers. See Brief for
Google LLC as Amicus Curiae 2. Google represents that, as a result, it
is no longer capable of responding to geofence warrants that seek Loca-
tion History data. See ibid.
                 Cite as: 609 U. S. ____ (2026)            5

                     Opinion of the Court

Google creates from it—in the palm of his hand. The user
thus can access a “Timeline” showing where he has traveled
when; receive real-time updates about his daily commute;
and take advantage of maps and recommendations based
on his usual movements.
                              B
   In the last decade, Google’s Location History data has
also served another function, though this one unknown to
most users: That data, as obtained through a geofence war-
rant, can enable law enforcement officers to solve hard-to-
solve crimes. Such a warrant, as earlier described, seeks
information about the cell phones located in the vicinity of
a crime scene at around the time the crime was committed.
See supra, at 1. The goal, put simply, is to find out who was
there and so who might have done it. (There are usually
better ways to investigate an already-known suspect—like
seeking only his location data.) And the mechanism is to
use the offender’s cell phone as an identifying device. The
warrant specifies a timeframe and maps an area (with the
geofence as its perimeter), and demands information about
the cell phones—and their users—present within it. There
is some uncertainty about how often the technique in fact
works. See Brief for Orin S. Kerr as Amicus Curiae 14 (Kerr
Brief ). But its use among law enforcement officers has
flourished. Google received its first geofence warrant in
2016. See 590 F. Supp. 3d, at 914. Two years later, it re-
ceived 982; and two years after that, more than 11,000. See
Google, Supplemental Information on Geofence Warrants
in The United States (Aug. 2021), https://services.google.
com/fh/files/misc/supplemental_information_geofence_war-
rants_united_states.pdf (archived at https://perma.cc/
LN4P-KQJA). Though the details vary, each has made the
6                   CHATRIE v. UNITED STATES

                          Opinion of the Court

same essential demand: Tell us, through cell-phone location
data, who was there when a crime happened.3
   As those demands began to proliferate, Google worked
with law enforcement officials to develop a three-step pro-
tocol to govern geofence warrants. At the first step, Google
produces anonymized (i.e., no names attached) location
data for all cell phones (or other devices) within the
geofence—typically, a circle with a designated radius sur-
rounding a latitude/longitude coordinate—during a speci-
fied timeframe. That data generally includes each phone’s
latitude/longitude       coordinate    and      corresponding
timestamp; an estimate of that information’s accuracy; and
a description of the information’s source (e.g., a Wi-Fi net-
work, a cell site, or some other). The data at this stage
shows each user’s location, every two minutes or so, within
the geofence. At the second step of the process, officials re-
view the data produced and typically ask Google to provide
additional information for a subset of still-anonymized us-
ers. That new data is usually for a longer timeframe than
first specified; it also shows the user’s location outside, as
well as inside, the geofence. Finally, at the third step, offi-
cials demand the identities of a further subset of users—
their names, email addresses, and phone numbers. Thus,
the geofence warrant is designed to eventually produce a
select number of identified users suspected of committing
the crime under investigation.
                             C
  On May 20, 2019, at about 4:50 p.m., a man robbed a
credit union in Midlothian, Virginia. The robber presented
a teller with a handwritten note demanding $100,000,
——————
  3 Google is not the only tech company that has received geofence war-

rants; so have Apple, Lyft, Snapchat, and Uber, among others. See 136
F. 4th 100, 102, n. 1 (CA4 2025) (en banc) (Diaz, C. J., concurring). But
Google is the “most common recipient and the only one known to re-
spond.” Ibid.
                 Cite as: 609 U. S. ____ (2026)            7

                     Opinion of the Court

threatening to hurt her and her family if she did not com-
ply, and warning her that he had “boys on the lookout out
side.” 590 F. Supp. 3d, at 905–906. When the teller replied
that she did not have access to that amount of money, the
robber brandished a firearm. He ordered everyone in the
bank to the ground, and forced the bank’s manager to open
a safe and put $195,000 into a bag. The robber then left on
foot with the money.
   Local police officers responded to the scene and began an
investigation. They learned, from witness interviews and
surveillance-camera footage, that the robber had ap-
proached the credit union from a corner of an adjacent
church, while appearing to talk on a cell phone. But they
could not find out anything more, and the robber remained
at large.
   On June 14, the police officers thus applied to a Virginia
magistrate for a geofence warrant directed to Google. The
application described the cell-phone location data Google
collects, and explained how that data could lead to identify-
ing the robber, his possible accomplices, or additional wit-
nesses to the crime. Success was particularly likely here,
the application stated, because the robber appeared to be
using his phone when he entered the credit union, and may
even have been speaking with an accomplice. The officers’
proposed geofence was a circle with a radius of 150 meters
surrounding the credit union.
   The warrant application went on to describe the three-
step process that the police would follow to obtain the loca-
tion information sought. At step one, Google would produce
anonymized location data for all cell phones within the
geofence in the hour between 4:20 and 5:20 p.m. (30
minutes before to 30 minutes after the robbery). At step
two, police officers would “attempt to narrow down the list
[of devices] by reviewing the time stamped location coordi-
nates for each [device] and comparing that against the
known time and location information that is specific to this
8                CHATRIE v. UNITED STATES

                      Opinion of the Court

crime.” 2 App. 136. For that narrowed list, Google would
provide additional (but still anonymized) data—cell-phone
locations both inside and outside the geofence during a two-
hour period (so now from 3:50 to 5:50 p.m.). Finally, at step
three, police would again “attempt to narrow down the list
by comparing this additional information regarding travel
and time against the known time and location information
that is specific to this crime.” Id., at 137. And Google would
then turn over identifying information for each user on the
final list, including his name and phone number.
   The magistrate issued the warrant, and officers executed
it in the manner prescribed. At the first stage of the pro-
cess, Google gave up anonymized data for 19 users found
within the geofence during the hour within which the rob-
bery occurred. At the second stage, the officers winnowed
the list to nine users. And Google produced anonymized
data showing their movements both inside and outside the
geofence for the extended two-hour period. At the third and
last step, the police again narrowed the list, this time to
three users. Google responded with their identifying infor-
mation. One of the three was Chatrie. The location data
showed that he entered the geofenced area about ten
minutes before the robbery, and headed toward a residen-
tial area of town immediately after leaving the bank.
   Following further police work, a federal grand jury
charged Chatrie with robbery and related firearms of-
fenses. He moved to suppress the information that the po-
lice had obtained from Google. According to Chatrie, the
officers had acquired that data through a Fourth Amend-
ment search, and the warrant ostensibly authorizing that
search was invalid.
   The District Court mainly agreed with Chatrie’s Fourth
Amendment analysis, but still denied the motion to exclude
the Location History evidence. Even though “this particu-
lar geofence warrant plainly violates the rights enshrined
in [the Fourth] Amendment,” the court stated, the officers’
                  Cite as: 609 U. S. ____ (2026)             9

                      Opinion of the Court

reliance on it was not “objectively unreasonable.” 590
F. Supp. 3d, at 905, 938. And because that was so, the court
concluded, the good-faith exception to the exclusionary rule
permitted admission of the location data. See id., at 937–
938; United States v. Leon, 468 U. S. 897, 922–923 (1984)
(establishing good-faith exception).
   A divided panel of the Court of Appeals of the Fourth Cir-
cuit affirmed, but on different reasoning. The majority held
that the government did not conduct a search and therefore
did not need a warrant. That was so, the majority reasoned,
because Chatrie “did not have a reasonable expectation of
privacy in two hours’ worth of Location History data volun-
tarily exposed to Google.” 107 F. 4th 319, 325 (2024). Judge
Wynn dissented, arguing that “the police intrusion into
Chatrie’s Location History data” was “a search that trig-
gered the Fourth Amendment’s protections,” and that the
warrant issued was “so lacking in particularity and proba-
ble cause that it was invalid.” Id., at 339, 362, and n. 12.
   After granting rehearing en banc, the Fourth Circuit af-
firmed in a one-sentence per curiam. See 136 F. 4th 100,
101 (2025) (“The judgment of the district court is
AFFIRMED”). In multiple accompanying writings, the
court divided evenly (7 to 7) on whether a Fourth Amend-
ment search had occurred. Of the seven judges who thought
it had, most believed the geofence warrant defective. But
most also thought the exclusionary rule’s good-faith excep-
tion applied, so ruled against Chatrie anyway.
   We granted certiorari solely on the question whether the
police violated the Fourth Amendment in obtaining Cha-
trie’s location data, thus declining to consider the exclusion-
ary rule issue. See 607 U. S. 1148 (2026). The disputed
Fourth Amendment question divides into two parts. First,
did law enforcement officials conduct a search under the
Fourth Amendment when they acquired Chatrie’s location
data from Google? We hold that they did because an indi-
vidual has a legitimate expectation of privacy in his cell-
10                   CHATRIE v. UNITED STATES

                           Opinion of the Court

phone location data. Second, did the multi-step geofence
warrant issued here make that search reasonable? We
leave that question—which requires deciding whether the
warrant satisfied the Fourth Amendment’s probable cause
and particularity requirements at each stage of the search
process—to the Court of Appeals to address in the first in-
stance.4
                            II
  The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” The “basic
purpose” of that Amendment, our precedents say, is “to
——————
   4 In line with our grant of certiorari, we do not address whether the

good-faith exception to the exclusionary rule still allows the admission of
the Location History data in this case. That question remains for the
Fourth Circuit to consider anew, gleaning anything it thinks relevant
from our decision on the substantive Fourth Amendment issues.
   The principal dissent seeks to rehash our limited grant of certiorari,
but we see no reason to doubt it. We have Article III jurisdiction in this
case, as even the dissent concedes. See post, at 4, n. 2 (ALITO, J.). That
is because the Fourth Circuit is free to revisit the exclusionary rule issue
in light of our opinion and to provide Chatrie with relief. See Chafin v.
Chafin, 568 U. S. 165, 172 (2013) (Article III jurisdiction disappears only
when it becomes “impossible for the court to grant any effectual relief
whatever to the prevailing party”). So what does the dissent mean when
it continually labels this opinion “advisory” (post, at 1, 2, 4, 5, 6, 7)—a
term customarily used to describe opinions lacking a jurisdictional basis?
Apparently, the dissent’s objection is that we today decide a question in-
volving the Fourth Amendment when the odds are strong (so says the
dissent) that the Fourth Circuit will eventually, as it did before, resolve
this case on exclusionary rule grounds. But to repeat, the Fourth Circuit
may now consider anew, after review of our opinion, how the good-faith
exception applies here. And the very decision establishing that exception
held that courts should feel free to “resolv[e] the Fourth Amendment is-
sue” before the good-faith issue, either to better assess good faith or “to
guide future action by law enforcement officers and magistrates.” United
States v. Leon, 468 U. S. 897, 925 (1984). So contra the dissent, there is
nothing advisory (or otherwise improper) in today deciding the Fourth
Amendment issue on which we previously granted certiorari.
                      Cite as: 609 U. S. ____ (2026)                    11

                          Opinion of the Court

safeguard the privacy and security of individuals against
arbitrary invasions by governmental officials.” Carpenter
v. United States, 585 U. S. 296, 303 (2018) (quoting Camara
v. Municipal Court of City and County of San Francisco, 387
U. S. 523, 528 (1967)).
   That purpose is central to decisions about whether a
Fourth Amendment “search” has occurred. Our early
search doctrine focused on whether law enforcement offi-
cials “obtain[ed] information by physically intruding”—that
is, trespassing—on private property. United States v.
Jones, 565 U. S. 400, 406–407, n. 3 (2012); see id., at 404–
405. But the Court in Katz v. United States, 389 U. S. 347,
351 (1967), recognized that “the Fourth Amendment pro-
tects people, not places.” And so we have long held that
“property rights are not the sole measure” of a constitu-
tional violation; the Fourth Amendment “protect[s] certain
expectations of privacy as well.” Soldal v. Cook County, 506
U. S. 56, 64 (1992); Carpenter, 585 U. S., at 304. “When an
individual seeks to preserve something as private and his
expectation of privacy is one that society is prepared to rec-
ognize as reasonable,” then governmental “intrusion into
that private sphere generally qualifies as a search.” Ibid.5
——————
   5 The dissent suggests that this Court has tried to curtail Katz ever

since deciding it, see post, at 10–11 (ALITO, J.); more energetically, the
concurrence advocates overthrowing Katz and reverting to a solely prop-
erty-based approach, see post, at 1–2, 4 (GORSUCH, J., concurring in judg-
ment). But this Court has faithfully applied Katz for some 60 years. Our
decision in Carpenter v. United States, 585 U. S. 296 (2018), responded
to the same arguments made today (see, e.g., id., at 391–397 (GORSUCH,
J., dissenting)) by reaffirming that Katz had “discredited the premise
that property interests control” and that “privacy interests do not rise or
fall with property rights.” 585 U. S., at 304, n. 1. And in saying as much,
Carpenter had plenty of other decisions to cite. See, e.g., United States
v. Jones, 565 U. S. 400, 411 (2012) (refusing to “make trespass the exclu-
sive test”); Kyllo v. United States, 533 U. S. 27, 32 (2001) (stating that
the Court has “decoupled violation[s] of a person’s Fourth Amendment
rights from trespassory violation of his property”). Of course, sometimes
the privacy and property approaches will “align,” and an opinion
12                  CHATRIE v. UNITED STATES

                          Opinion of the Court

   Whether an expectation of privacy counts as legitimate is
less the result of any fixed set of rules than of “guideposts”
stretching back to the Fourth Amendment’s beginnings.
Id., at 305. From the founding onward, we have explained,
the Fourth Amendment has sought to secure the “privacies
of life” against the exercise of “arbitrary power.” Boyd v.
United States, 116 U. S. 616, 630 (1886); see Carpenter, 585
U. S., at 305. So too we have recognized, and repeatedly,
that the Amendment was designed “to place obstacles in the
way of a too permeating police surveillance.” United States
v. Di Re, 332 U. S. 581, 595 (1948); Carpenter, 585 U. S., at
305. Whatever the form of an attempted incursion, the
Fourth Amendment protects Americans’ long-held convic-
tion that no government official should have free access to
the most closely kept aspects of their lives.
   In recent decades, this Court has often confronted the
challenge of adhering to those principles in the face of new
technologies. “[I]nnovations in surveillance tools” have “en-
hanced the Government’s capacity to encroach upon areas
normally guarded from inquisitive eyes.” Ibid. The Court,
in response, has sought to “assure[ ] preservation of that de-
gree of privacy against government that existed when the
Fourth Amendment was adopted.” Kyllo v. United States,
533 U. S. 27, 34 (2001). So in one decision, we rejected a
“mechanical interpretation” of the Fourth Amendment to
hold that the use of a thermal imager to detect heat coming
——————
adopting the one will resemble, in whole or part, an opinion adopting the
other. Florida v. Jardines, 569 U. S. 1, 13 (2013) (KAGAN, J., concurring).
That is not because the privacy-based approach is groping toward the
more “coheren[t]” property-based one, as the concurrence suggests. Post,
at 8 (GORSUCH, J.). It is simply because property law “naturally enough
influence[s]” our “shared societal expectations” of what places and things
count as private and should be free from governmental intrusion. Geor-
gia v. Randolph, 547 U. S. 103, 111 (2006); see Carpenter, 585 U. S., at
304, n. 1 (“[P]roperty rights are often informative” in “determining which
expectations of privacy are legitimate”). And when such an alignment of
the two approaches occurs, then all the better.
                 Cite as: 609 U. S. ____ (2026)           13

                     Opinion of the Court

from a person’s home was a search in the constitutional
sense. Id., at 35. And in another, we held that the search
of a cell phone incident to arrest could not proceed without
a warrant (even though the search of a handbag could) be-
cause of the phone’s “vast quantities of personal infor-
mation.” Riley, 573 U. S., at 386. Most recently, in Carpen-
ter v. United States, this Court held that accessing a form
of cell-phone location information other than Location His-
tory is a Fourth Amendment search given individuals’ rea-
sonable expectations of privacy. See 585 U. S., at 310–313.
   We begin with Carpenter in considering the Govern-
ment’s front-line position here: that no warrant was needed
to get Location History data from Google (although the po-
lice “prophylactically secured” one) because no Fourth
Amendment search ever took place. See Brief for United
States 14. We then explain why the result we reached in
Carpenter once again follows. Contrary to the Govern-
ment’s view, an individual has a legitimate expectation of
privacy in the information Location History collects about
his cell phone’s—meaning his own—movements. The police
invade that expectation, and thus conduct a search, when
they acquire that information, even though for only a lim-
ited period of time and even though via a third-party tech
company.
                              A
  The question presented in Carpenter was “whether the
Government conducts a search under the Fourth Amend-
ment when it accesses historical cell phone records that pro-
vide a comprehensive chronicle of the user’s past move-
ments.” 585 U. S., at 300. The cell-phone records at issue
were what is known as cell-site location information (CSLI).
As we explained, CSLI is a “time-stamped record” gener-
ated each time a cell phone connects to a cell site. Id., at
301. Wireless carriers collect and store that information for
their own business purposes (such as finding weak spots in
14                 CHATRIE v. UNITED STATES

                         Opinion of the Court

their networks). But CSLI can also benefit law enforce-
ment, because it identifies an individual’s approximate lo-
cation every time his phone makes a connection. In Car-
penter, police officers investigating a string of Radio Shack
robberies ordered a wireless carrier of a known suspect to
turn over his CSLI records for a seven-day period (without
first getting a warrant). Those records showed, as the Gov-
ernment later put it, that the suspect, Timothy Carpenter,
was “right where the . . . robbery was at the exact time of
the robbery.” Id., at 303. Carpenter moved to exclude the
CSLI records, arguing that the Government acquired them
through an unconstitutional search.
   The Court began its analysis by reviewing what it had
said about a different way of tracking “physical location and
movements”: the use of a GPS device to monitor a vehicle.
Id., at 306. In United States v. Jones, 565 U. S. 400, five
Justices had agreed that such tracking counts as a Fourth
Amendment search because “individuals have a reasonable
expectation of privacy in the whole of their physical move-
ments.” Carpenter, 585 U. S., at 310; see Jones, 565 U. S.,
at 430 (ALITO, J., concurring in judgment); id., at 415
(SOTOMAYOR, J., concurring).6 That made sense, the Car-
penter Court thought, even though the movements occurred
in public. Prior to the digital age, pursuing a suspect “for
any extended period of time was difficult and costly and
therefore rarely undertaken.” 585 U. S., at 310 (quoting
Jones, 565 U. S., at 429 (opinion of ALITO, J.)). As a result,
“society’s expectation has been that law enforcement agents
and others would not—and indeed, in the main, simply
could not—secretly monitor and catalogue every single
movement of an individual’s car.” Carpenter, 585 U. S., at
310 (quoting Jones, 565 U. S., at 430 (opinion of ALITO, J.)).

——————
  6 An overlapping set of five Justices decided the case on a different

ground, based on the Government’s physical trespass of the vehicle. See
Jones, 565 U. S., at 404–405.
                      Cite as: 609 U. S. ____ (2026)                     15

                           Opinion of the Court

A new technology should not transform what individuals
had reasonably thought they could withhold from the Gov-
ernment.
   It followed a fortiori, Carpenter held, that “[a]llowing gov-
ernment access to cell-site records contravenes” expecta-
tions of privacy. 585 U. S., at 311. To an even greater de-
gree than GPS monitoring, CSLI can provide a full “record
of the holder’s whereabouts” and, with that, “an intimate
window into a person’s life.” Ibid. People, after all, “regu-
larly leave their vehicles,” but they “compulsively carry”
their cell phones “all the time.” Ibid. A cell phone thus
“tracks nearly exactly the movements of its owner”: It
“faithfully follows” him not only through “public thorough-
fares [but] into private residences, doctor’s offices, political
headquarters, and other potentially revealing locales.”
Ibid. What is more, the “newfound tracking capacity” that
CSLI gives the police “runs against everyone”—not just
those “under investigation”—and “travel[s] back in time.”
Id., at 312. Police officers need not decide in advance (as
they do with GPS devices) who they want to follow and
when. Instead, they can easily and cheaply—with “just the
click of a button”—reconstruct any person’s movements
“retrospective[ly].” Id., at 311–312. What in the past was
“unknowable” suddenly becomes open to view, presenting
formerly unimaginable “privacy concerns.” Ibid. The Court
thus concluded: “[W]hen the Government accessed CSLI
from the wireless carriers”—thereby obtaining a “detailed
log” of where Carpenter had gone for seven days—“it in-
vaded Carpenter’s reasonable expectation of privacy in the
whole of his physical movements.” Id., at 312–313.7
——————
  7 A significant fraction of the dissent is devoted to relitigating Carpen-

ter, from which its author dissented. See post, at 1, 8–10, 13–14, 19–21
(ALITO, J.). Carpenter, the dissent complains today, “extended the Fourth
Amendment’s warrant requirement to encompass a category of govern-
ment investigations that it had never previously covered”: The decision
“thus reflected a stark departure from both traditional Fourth
16                  CHATRIE v. UNITED STATES

                          Opinion of the Court

                               B
  The resemblances between CSLI and Location History, in
their relationship to personal privacy, practically leap off
the page. Everything Carpenter relied on to find that law
enforcement officers conducted a Fourth Amendment
search when they accessed wireless carriers’ CSLI records
applies as well or better to the police’s accessing of Google’s
Location History data.
  First, Location History provides an even more fine-tuned
picture of a person’s movements than CSLI. Carpenter
noted that through CSLI records, police could “achieve[ ]
near perfect surveillance” of an individual holding a cell
phone. Id., at 311–312. But Location History is nearer per-
fect still. Here is one way of comparing the two: At any
given time, CSLI placed Carpenter within a “sector ranging
from one-eighth to four square miles,” whereas Location
History pinpointed Chatrie’s location within around twenty
meters, which is less than two percent of a mile. Id., at 312;
see 1 App. 45, 3 id., at 173–174. Or here is another
——————
Amendment principles and this Court’s 20th-century doctrine.” Post, at
13. In leveling that charge, the dissent re-ups arguments, point-for-
point, that Carpenter specifically rejected. Compare post, at 8, 13 (main-
taining that compelled document-production orders are never searches),
with 585 U. S., at 317–318 (rejecting that view); compare also post, at 9,
13 (contending that the Fourth Amendment never protects documents
held by third parties), with 585 U. S., at 313–316 (likewise rejecting that
view). In light of that outlook, it is perhaps not so surprising that the
dissent criticizes today’s decision as “rely[ing] primarily” on Carpenter,
rather than on earlier Fourth Amendment decisions. Post, at 13. But on
that supposed offense, we plead guilty as charged. Carpenter is the most
recent decision of this Court to consider the Fourth Amendment’s appli-
cation to new surveillance technologies—indeed, to law enforcement’s
use of those technologies to create a “chronicle of [a cell-phone] user’s
past movements.” 585 U. S., at 300. What would be grounds for com-
plaint is if this decision did not “rely primarily” on Carpenter. Post, at
13. And as the next section of this opinion shows, the more one delves
into the technologies at issue, the closer the parallels become. See infra
this page and 17–18.
                   Cite as: 609 U. S. ____ (2026)             17

                       Opinion of the Court

measure: CSLI logged Carpenter’s location an average of
101 times a day, whereas Location History commonly rec-
ords a person’s location every two minutes, for a daily aver-
age of 720 chartings. See Carpenter, 585 U. S., at 302; 136
F. 4th, at 151 (Berner, J., concurring). Or finally, a third:
Unlike CSLI, Location History can estimate a phone’s ele-
vation—so, for example, can tell whether someone has gone
into a doctor’s office on the first floor of a multi-story build-
ing, or a private apartment on the tenth. Of course, the
accuracy of each of the two techniques may vary in different
places and at different times. But across the board Location
History is the far more precise measure. When the Carpen-
ter Court said that CSLI provides a “detailed” and “encyclo-
pedic” portrait of a person’s whereabouts, it did not know
what further technology was on the horizon. 585 U. S., at
309.
   And next, Location History also allows police officers to
reconstruct “retrospective[ly],” and with no real effort, peo-
ple’s comings and goings in any area. Id., at 312. As with
CSLI, the Government need not decide in advance the kind
of surveillance it should undertake, whether of a person or
a site. “Whoever the suspect turns out to be,” Carpenter
said of CSLI, “he has effectively been tailed every moment
of every day.” Ibid. Likewise, as this case shows, wherever
a location of interest turns out to be (whether a crime scene
or a protest march or even a private home), it has effectively
been surveilled for the same boundless time. Google’s Lo-
cation History will be available to chart the movements of
many individuals—or a few or one—within the vicinity,
again at the “click of a button.” Id., at 311. Recall that in
Jones, it was thought notable that law enforcement officials
of an earlier age usually could not monitor every movement
of an individual’s car, as a GPS device does. See supra, at
14–15; 565 U. S., at 430 (opinion of ALITO, J.); see also Car-
penter, 585 U. S., at 312 (“In the past, attempts to recon-
struct a person’s [prior] movements were limited”). Far less
18               CHATRIE v. UNITED STATES

                      Opinion of the Court

could those officials ever perform the “tireless and absolute
surveillance” of any number of people in any number of
places, public and private, that Location History can accom-
plish. Ibid. If the one kind of intrusion clashes with “soci-
ety’s expectation[s]” of what counts as private, so must the
other. Jones, 565 U. S., at 430 (opinion of ALITO, J.).
   Indeed, Location History records implicate those privacy
interests still more than CSLI data because the former is
more the individual’s own. Most cell-phone users have no
awareness of CSLI records, and anyway would never try to
retrieve them. The records are instead the province of wire-
less carriers, which maintain them for an array of business
functions. See Carpenter, 585 U. S., at 301; supra, at 13–
14. Location History information is different. No doubt,
Google itself uses those records to improve the quality of its
apps. But Google users, too, regularly employ Location His-
tory—for example, “to remind themselves of a restaurant
they ate at two weeks ago, the time they were last at a
friend’s home, the sites they saw on vacation, or the dis-
tance they walked on a particular day.” Brief for Google
LLC as Amicus Curiae 8. The records thus serve as a per-
sonal journal of a user’s movements, which that user con-
sults (and even can edit) for his own purposes. See id., at
10. In that way, Location History resembles other private
materials—think of emails, documents, photographs, or
calendars—that even if stored on Google’s servers, a user
reasonably views as his own. And as a result, that he rea-
sonably expects to be shielded from the “inquisitive eyes” of
the government. Carpenter, 585 U. S., at 305.
                            C
  The Government, not much contesting any of the above,
principally argues on a different ground: that accessing
only a short amount of cell-phone location information
(whether Location History or CSLI) does not count as a
Fourth Amendment search. (The dissent likewise contends
                      Cite as: 609 U. S. ____ (2026)                    19

                          Opinion of the Court

that the “duration” of data obtained here is too brief for a
search to have happened. Post, at 14 (ALITO, J.); see post,
at 15–16.) Recall that Carpenter involved seven days’ worth
of location data. See supra, at 14–15. And in deciding that
case, this Court reserved the issue whether there was a
more “limited period for which the Government may obtain”
such data “free from Fourth Amendment scrutiny.” 585
U. S., at 310, n. 3.8 The Government now claims that the
answer is yes, and that the two hours’ worth of Location
History acquired here falls within the Constitution-free
zone. In the Government’s view, a person has no reasonable
expectation of privacy in “that short a time window” of lo-
cation data, because his “short-term” movements will “re-
veal[ ] little about the details of [his] personal life.” Brief for
United States 12, 20; see id., at 20 (“A single stop at a doc-
tor’s office, for example, does not in itself identify the reason
for the visit”). The Government cites in support United
States v. Knotts, 460 U. S. 276, 282 (1983), in which the
Court held that police officers’ use of a beeper to assist an
hours-long tail of a car did not bring the Fourth Amend-
ment into play. The lesson the Government draws is that
law enforcement officials accessing Location History should
receive a Fourth Amendment grace period of some number
of hours.
——————
   8 In comparing Carpenter and this case, the dissent sometimes treats

the former as involving not 7 days but instead 127 days of location data.
See post, at 13, 14, 15 (ALITO, J.). But there is no basis for doing so. To
be sure, one of the two wireless carriers involved in the case had turned
over 127 days of data, as the Court noted. See 585 U. S., at 302. But the
other was ordered to turn over only 7 days, and the Court could not have
been clearer that its holding applied whenever the Government accessed
a week or more of CSLI data (with everything below that amount re-
served). See id., at 310, n. 3 (“It is sufficient for our purposes today to
hold that accessing seven days of CSLI constitutes a Fourth Amendment
search”). The dissent acknowledges that fact (post, at 15, n. 4), even as
it repeatedly invokes the 127-day figure to make its comparative argu-
ment sound stronger.
20               CHATRIE v. UNITED STATES

                      Opinion of the Court

   But to begin, the Government is wrong about the inca-
pacity of short-term location information to reveal private
matters. “[R]epeated patterns,” in the Government’s phras-
ing, are not all that individuals wish to, and reasonably ex-
pect to, keep to themselves. Brief for United States 20. Re-
turn here to another of Jones’s insights: “[E]ven short-term
monitoring” of a person’s physical movements can provide
“a wealth of detail about [his] familial, political, profes-
sional, religious, and sexual associations.” 565 U. S., at 415
(opinion of SOTOMAYOR, J.). Consider just a few trips that
a person is apt to think “indisputably private”: to “the psy-
chiatrist, the plastic surgeon, the abortion clinic, the AIDS
treatment center, the strip club, the criminal defense attor-
ney, [or] the by-the-hour motel.” Ibid. And unlike a GPS
device, Location History enables police officers to focus on
precisely those sites—to see, in a given time block, who
shows up. Similarly, Location History—even two hours of
it—allows officers to target one-off events of potential inter-
est: a gun show, say, or a political rally.
   Still more fundamentally, we have never understood
Fourth Amendment protections as kicking in only once an
intrusion “goes too far.” Pennsylvania Coal Co. v. Mahon,
260 U. S. 393, 415 (1922) (adopting that approach for regu-
latory takings). Where the Fourth Amendment applies, it
applies—regardless of “the quality or quantity of infor-
mation” the government obtains. Kyllo, 533 U. S., at 37.
So, for example, this Court held that thermal imaging qual-
ified as a search even though it did not, and was not likely
to, detect “private activities” or “intimate details.” Ibid.
The Amendment, we analogized, makes “no exception” for
the officer “who barely cracks open the front door and sees
nothing but the nonintimate rug on the vestibule floor.”
Ibid. And likewise, the Amendment does not give agents a
pass if their wiretap is of limited duration and thus less
likely to intrude on private matters. Indeed, in our seminal
                     Cite as: 609 U. S. ____ (2026)                    21

                          Opinion of the Court

wiretap case, the police obtained only 18 minutes of record-
ings. See Katz, 389 U. S., at 354, n. 14.
   That approach makes all the more sense when, as with
Location History, officials can select the time-limited set of
materials they want from an all-encompassing database.
Then, the durational bounds on the data actually acquired
do little to address the Fourth Amendment’s concern about
“a too permeating police surveillance.” Di Re, 332 U. S., at
595; see supra, at 12. What creates that concern is that the
government can access all of a cell-phone user’s movements,
in both public and private places—that it possesses a vir-
tual panopticon with which to scrutinize its citizens’ activi-
ties. The sweep of the official invasion is not made less be-
cause the government, with the benefit of hindsight, can
pinpoint exactly which few hours of movements it wants to
review. That feature of accessing location data is, indeed,
more a practical benefit to the government than a limit on
its intrusive powers.9
   And contra the Government, Knotts does not support the
view that accessing two hours of Location History is not a
search. There, police officers put a beeper in a car to help
them follow it from Minnesota to Wisconsin. The Court de-
cided that the beeper did not turn the tail into a search, but
was explicit in keeping its holding cabined to that rudimen-
tary technology. The defendant had argued that a ruling
against him would enable officials to conduct “surveillance
——————
  9 The Government’s grace-period approach to Fourth Amendment pro-

tection would also create a host of line-drawing questions. At what point,
exactly, would a non-search become a search? In two hours, or six hours,
or one day, or six days? And how often would the clock reset? If, say, the
limit was six hours, could an officer request location data from 6 a.m. to
noon, and then again from 12:30 to 6:30 p.m.? And if there were concur-
rent federal and state investigations of a crime, as there could have been
here, would law enforcement access to Location History data double?
The approach the Government offers would “keep defendants and judges
guessing for years to come.” Riley v. California, 573 U. S. 373, 401
(2014).
22                   CHATRIE v. UNITED STATES

                           Opinion of the Court

of any citizen of this country” free from the strictures of the
Fourth Amendment. 460 U. S., at 283. The Court took the
concern seriously, stating that if technology progressed so
as to allow more sophisticated surveillance, “different con-
stitutional principles” could well apply. Id., at 284. And
three decades later, five Justices in two opinions found that
they did. When faced in Jones with a GPS device—which
unlike the beeper allowed remote monitoring—they de-
cided, notwithstanding Knotts, that privacy was implicated
and a search had occurred. See supra, at 14–15. Yet even
that was not all. When six years further on, the Carpenter
Court held that accessing CSLI was a search, it recounted
the Knotts-to-Jones progression to explain why Knotts did
not stand in its way. See 585 U. S., at 306–307 (Knotts “was
careful to distinguish between the rudimentary tracking fa-
cilitated by the beeper and more sweeping modes of surveil-
lance”). For the third time, we reach the same conclusion
today.
   And still another feature of Knotts makes it inapt here:
that the surveillance there was confined to public roads.
That fact was crucial to the Court’s decision: “A person trav-
eling in an automobile on public thoroughfares has no rea-
sonable expectation of privacy,” Knotts explained, because
the car is always “in plain view.” 460 U. S., at 281. By con-
trast, the movements that Location History reveals are not
limited to public streets. Recall what Carpenter observed:
A “cell phone faithfully follows its owner beyond public
thoroughfares and into private residences, doctor’s offices,
[and] political headquarters.” 585 U. S., at 311; see supra,
at 15.10 In one of those places—a private residence—this
——————
   10 The dissent replies that the “limited geofence procedure” authorized

by the warrant here distinguishes this case from Carpenter because “the
geofence’s boundaries” centered on “a public place.” Post, at 16 (ALITO,
J.). But as an initial matter, those boundaries were defined by a warrant.
If accessing Location History does not count as a Fourth Amendment
search, as the dissent generally suggests (see, e.g., post, at 12, 17), there
                     Cite as: 609 U. S. ____ (2026)                    23

                          Opinion of the Court

Court has held even beeper technology to count as a search
because it could reveal “whether a particular article—or a
person, for that matter” was in the home “at a particular
time.” United States v. Karo, 468 U. S. 705, 716 (1984). If
that is so, accessing Location History must also be a
search—even if for only two hours—because that data can
far more reliably show someone within a home (indeed, on
a specific floor). The Government replies with an odd argu-
ment. It thinks that “tracking [someone] into a private res-
idence”—yes, even for two hours—would “probably” be a
search, but tells us not to worry because Chatrie did not go
home. Tr. of Oral Arg. 98, 134. That approach, however, is
foreign to the way the Fourth Amendment works. Whether
something is a search does not depend on what it finds. See
Di Re, 332 U. S., at 595 (“[A] search is not to be made legal
by what it turns up. In law it is good or bad when it starts”).
An officer, after all, cannot know the fruits of a given sur-
veillance in advance. The surveillance must be either a
search or not regardless. The Government’s concession
thus gives away its argument that, for purposes of the
Fourth Amendment, two hours of cell-phone location data
is not enough.


——————
will not be a warrant (or any other means) to limit the scope of what law
enforcement can demand. And even putting that aside, the dissent’s ar-
gument is wrong because it ignores how this geofence warrant actually
worked. The geofence was not limited to the bank; it also included a
nearby church. 590 F. Supp. 3d 901, 918 (ED Va. 2022); cf. Brief for
Google LLC as Amicus Curiae 12 (noting that, in Google’s experience, it
is “common for a geofence to cover private homes, apartment buildings,
. . . hotels, [and] places of worship”). And regardless, the Location His-
tory data the police obtained at the second stage of the search process
was not constrained by the geofence. In fact, it showed individuals’ trips
to private residences, a school, and a hospital. See 590 F. Supp. 3d, at
923–924. So the geofence’s boundaries do not somehow turn Location
History into a public-movements-only technology or ensure a less “com-
prehensive” log than in Carpenter. Post, at 16.
24               CHATRIE v. UNITED STATES

                      Opinion of the Court

                               D
  The Government has an additional argument, which in
Carpenter was its “primary” one—that the so-called third-
party doctrine precludes Chatrie from invoking the Fourth
Amendment’s protections. 585 U. S., at 313. (Here too the
dissent reiterates the Government’s view. See post, at 11–
12, 17 (ALITO, J.).) The idea is that in “authoriz[ing] Google
to collect, retain, and use” his location information, Chatrie
lost his legitimate expectation of privacy, and therefore his
right to complain of a search—regardless whether it was for
two hours, two weeks, or two years. Brief for United States
15. The problem for the Government—and presumably the
reason that its primary assertion in Carpenter has here be-
come a secondary one—is that Carpenter refused to apply
the third-party doctrine to CSLI, and no good reason exists
to reach a different result for Location History.
  The third-party doctrine traces to two cases involving in-
formation provided by customers to a bank and telephone
company, and then turned over to law enforcement officials.
In United States v. Miller, 425 U. S. 435 (1976), this Court
held that a bank depositor had no reasonable expectation of
privacy in canceled checks and deposit slips in his bank’s
possession, because the records were “voluntarily conveyed
to the bank[ ] and exposed to [its] employees in the ordinary
course of business.” Id., at 442. The depositor, the Court
explained, had “take[n] the risk, in revealing his affairs to
another,” that the third party would in turn provide that
information to the government. Id., at 443. A few years
later, the Court in Smith v. Maryland, 442 U. S. 735 (1979),
applied that principle to hold that a (landline) telephone
subscriber lacked a legitimate expectation of privacy in the
phone numbers he dialed. Once again, the Court reasoned
that the subscriber had “voluntarily conveyed [the dialed
numbers] to the telephone company,” and so relinquished
his Fourth Amendment right. Id., at 744.
                  Cite as: 609 U. S. ____ (2026)           25

                      Opinion of the Court

   In Carpenter, however, the Court rejected the Govern-
ment’s contention that the third-party doctrine likewise
governed the acquisition of CSLI. The Court acknowledged
that a cell-phone user “continuously reveals his location” to
a third-party wireless carrier. 585 U. S., at 309. But it held
that cell-phone location information is “qualitatively differ-
ent” from “telephone numbers and bank records.” Ibid.
Those differences fell along two axes. First, the Court ex-
plained, the “nature” of CSLI is incomparably “revealing.”
Id., at 314. There is “a world of difference” between the “ex-
haustive chronicle of location information casually collected
by wireless carriers” and “the limited types of personal in-
formation addressed in Smith and Miller.” Ibid. The for-
mer thus “implicates privacy concerns far beyond” the lat-
ter. Id., at 315. And second, the Court continued, “[c]ell
phone location information is not truly ‘shared’ as one nor-
mally understands the term.” Ibid. Because “cell phones
and the services they provide” are “such a pervasive and
insistent part of daily life”—“indispensable to participation
in modern society”—a person can hardly help but generate
a “trail of location data.” Ibid. “[I]n no meaningful sense,”
the Court thought, does that mean a person “voluntar[il]y
expos[es]” to any third party a “comprehensive dossier of
his physical movements.” Ibid.
   Both differentiating features highlighted in Carpenter
apply equally or better to Location History. As noted above,
Location History is even more “revealing” than CSLI, be-
cause it provides a yet more precise record of an individual’s
movements. See supra, at 16–17. Access to that record en-
ables officials to undertake nearly perfect, retrospective
surveillance of countless persons and places. See supra, at
17–18. And for Location History, that surveillance is based
on information that a user reasonably understands as his
own, even though stored on Google’s servers—much like his
emails, photos, and calendar entries. See supra, at 18.
Likewise, the information is “not truly shared,” in the
26               CHATRIE v. UNITED STATES

                     Opinion of the Court

normal sense of wanting a third party to see or use it. Car-
penter, 585 U. S., at 315. The exposure of that information
to Google is merely what happens when a user avails him-
self of one of the services on his cell phone. Or said a bit
differently, it is the automatic price of conventional cell-
phone usage—which, just as Carpenter noted, is a “perva-
sive and insistent part of daily life.” Ibid. So just as the
third-party doctrine did not apply in Carpenter, it does not
apply here.
   The Government contests that conclusion on Carpenter’s
second axis alone: It claims that generating Location His-
tory, unlike producing CSLI, is a voluntary choice on the
user’s part. Although carrying a cell phone may be indis-
pensable in modern society, the Government argues, using
Location History is not. Rather, Location History is an “op-
tional add-on,” which a user must enable by an “affirmative
act” beyond “powering up” a phone. Brief for United States
13, 22 (quoting Carpenter, 585 U. S., at 315). In support,
the Government emphasizes that only around one-third of
current Google accountholders have activated the service.
See Brief for United States 22; see 1 App. 45. That goes to
show, says the Government, that people can “live[ ] without”
Location History. Brief for United States 22; see Tr. of Oral
Arg. 92. And if that is true (the Government says), people
who do use the feature have indeed “voluntar[il]y expos[ed]”
all of their movements. Carpenter, 585 U. S., at 315.
   But as an initial matter, that argument ignores some per-
tinent facts about how and why Google users turn on Loca-
tion History. As described earlier, Google prompts a user,
and repeatedly, to turn on the service—when he sets up a
Google account, when he sets up an Android phone, and
when he sets up a Google app. See supra, at 3–4. The
prompt often informs him that his device will not “work cor-
rectly” unless he does so. 2 App. 140–141. By contrast, it
does not tell him quite what he is signing up for: “how fre-
quently Google would record [his] location”; “how precise
                  Cite as: 609 U. S. ____ (2026)           27

                      Opinion of the Court

Location History can be”; or how Google might give all that
minute-by-minute location information to the government.
590 F. Supp. 3d, at 936; 136 F. 4th, at 128 (Wynn, J., con-
curring in judgment). In those circumstances, it is hard to
see how any user is, in the normal sense, “sharing” with
third parties a comprehensive catalog of his physical move-
ments. Carpenter, 585 U. S., at 314. And that is so regard-
less of how many others ignore Google’s entreaties. The
Government’s estimation of that number is almost surely
overstated: It appears to include, for example, the many
millions of Google accountholders in foreign countries like
China where collecting Location History is illegal. See 4
Joint App. in No. 22–4489 (CA4), pp. 845, 848. But in any
event, the raw user totals for Location History—one-third,
two-thirds, or someplace in between—are not the most apt
measure of whether that service’s enlistees have, as the
Government claims, self-consciously “assumed the risk of
sharing” all their movements with others. Brief for United
States 12.
  More generally, the Government’s approach to Fourth
Amendment protection would raise a host of workability is-
sues. At the top of the list: What percentage of users would
have to sign up for a service to make doing so non-volun-
tary? The Government posited at argument that if 80 per-
cent of active Google accountholders had enabled Location
History, the case would be “much closer.” Tr. of Oral. Arg.
92. After all, the Government candidly noted, even pos-
sessing a cell phone is not truly “indispensable” (to use Car-
penter’s word): “[S]omething like 90 percent of people have
[them].” Tr. of Oral. Arg. 92. So where to draw the line?
And after that, the questions only multiply. Would a user
lose Fourth Amendment protection if a highly popular cell-
phone feature became less so over time? What if the use of
a given feature is ubiquitous among (but only among) a sub-
set of the population (say, an age cohort), and an individual
defendant is a member of that class? Would it be enough if
28               CHATRIE v. UNITED STATES

                      Opinion of the Court

the lion’s share of cell-phone users enabled a feature similar
to the one at issue—so, for example, any location-tracking
service, whether Google’s or some other company’s? And
finally, a more basic inquiry: In such a world, how is any-
one—whether a cell-phone user or a police officer—to know
in advance (which is when the knowledge is useful) whether
enrollees in a given service will be found to have Fourth
Amendment protection in the information that service col-
lects? To ask all these questions about the Government’s
approach is to know that it is on the wrong track.
   And there is yet a deeper problem: The Government’s
app-by-app, feature-by-feature method of granting Fourth
Amendment protection misapprehends the very nature of
modern cell-phone use. Pretty much everything a person
does on a smartphone requires some kind of opt-in—an “af-
firmative act” beyond “powering up” to utilize a given app
or service. Carpenter, 585 U. S., at 315. Consider sending
an email on Gmail, uploading a photo to Google Photos, or
adding a calendar entry to Google Calendar. None happens
solely by dint of the phone’s operation; each requires, as Lo-
cation History does, an “optional add-on.” Brief for United
States 13. And each activity, like using Location History,
results in sharing information with a third-party tech com-
pany—turning over private materials to live on that com-
pany’s servers. The Government wishes to disconnect all
those uses from the mere act of carrying a turned-on cell
phone (the thing that generates CSLI), with only the latter
receiving assured Fourth Amendment protection. But that
is to imagine that all of us are living in dumb flip-phone
days. The point of carrying smartphones is to use what is
on them—as Carpenter said, to use the apps and “services
they provide.” 585 U. S., at 315. That is what has become
a “pervasive and insistent”—even “indispensable”—“part of
daily life.” Ibid.; Riley, 573 U. S., at 385. And so that is
what Carpenter insulated from the third-party doctrine. A
cell-phone user is not to be viewed as sharing private
                     Cite as: 609 U. S. ____ (2026)                    29

                          Opinion of the Court

information with third parties—which then can be freely
passed on to the government—just by doing the ordinary
things cell-phone users do.
                        *     *    *
  For all those reasons, we hold that police officers invade
a cell-phone user’s reasonable expectation of privacy when
they access his Location History. It does not matter if the
time period scrutinized was only two hours. Nor does it
matter that the materials obtained were handed over by a
third-party tech company. When the government “accesses
historical cell phone” location information—Location His-
tory as much as CSLI—it “conducts a search under the
Fourth Amendment.” Carpenter, 585 U. S., at 300.
                              III
   That conclusion does not resolve this case, because the
Fourth Amendment prohibits only searches that are “un-
reasonable.” When law enforcement officials undertake a
search to discover evidence of a crime, the reasonableness
standard generally requires that they seek a warrant from
“a neutral and detached magistrate.” Johnson v. United
States, 333 U. S. 10, 14 (1948); see Vernonia School Dist.
47J v. Acton, 515 U. S. 646, 653 (1995).11 That requirement
subjects the officials’ assessment of a search’s propriety to
the “deliberate, impartial judgment of a judicial officer.”
United States v. Grubbs, 547 U. S. 90, 99 (2006). The mag-
istrate, in turn, may issue a warrant only when “probable
cause is properly established and the scope of the author-
ized search is set out with particularity.” Kentucky v. King,
563 U. S. 452, 459 (2011).
——————
  11 Our precedents recognize exceptions to that rule—most prominently,

“when the exigencies of the situation make the needs of law enforcement
so compelling that [a] warrantless search is objectively reasonable.” Car-
penter, 585 U. S., at 319. Today’s decision does not call into doubt, in
such circumstances, a warrantless geofence search. See id., at 320 (not-
ing the same for “warrantless access to CSLI”).
30               CHATRIE v. UNITED STATES

                      Opinion of the Court

   When officers have obtained a warrant, as they did here,
a search’s legality will thus depend on whether a magis-
trate has properly found probable cause to support a partic-
ularly described search. “[P]robable cause is a fluid con-
cept—turning on the assessment of probabilities in
particular factual contexts—not readily, or even usefully,
reduced to a neat set of legal rules.” Illinois v. Gates, 462
U. S. 213, 232 (1983). But a magistrate must always deter-
mine that there is a “fair probability that contraband or ev-
idence of a crime will be found” in the place searched. Id.,
at 238. That means determining, to the requisite “fair prob-
ability,” both that the place searched will have the materi-
als sought and that those materials will contain evidence
“aid[ing]” in a criminal’s “apprehension or conviction.” Mes-
serschmidt v. Millender, 565 U. S. 535, 551, 552, n. 7 (2012);
see Zurcher v. Stanford Daily, 436 U. S. 547, 556 (1978)
(“The critical element” is whether there is the requisite
“cause to believe that the specific ‘things’ to be searched for
and seized are located” in the targeted place). The particu-
larity requirement, for its part, ensures that the search will
be of an appropriate scope—that it is “carefully tailored to
its justifications, and will not take on the character of the
wide-ranging exploratory searches the Framers intended to
prohibit.” Maryland v. Garrison, 480 U. S. 79, 84 (1987).
That requirement typically looks to such matters as the ge-
ographic and durational expanse of the search. See id., at
84–85; Karo, 468 U. S., at 718. And it too must take account
of “particular factual contexts,” including in surveillance
cases the nature of the technology to be used. Gates, 462
U. S., at 232; see, e.g., Karo, 468 U. S., at 718; see generally
Kerr Brief 17–20.
   The warrant issued here, as described earlier, was an un-
common, multi-step one. See supra, at 7–8. The first step
it laid out authorized police officers to obtain location data
for all cell phones inside the designated geofence within a
one-hour timeframe. The second step entitled the officers
                 Cite as: 609 U. S. ____ (2026)           31

                     Opinion of the Court

to obtain additional data (two hours, both inside and out-
side the geofence) for a subset of those phones—of the offic-
ers’ own choosing. And the third step enabled them to ob-
tain personal identifying information (including names,
email addresses, and phone numbers) for a further subset—
again of their selection. As to how the officers would make
their choices at the second and third steps—how they would
pick the users subject to more intense scrutiny—the war-
rant said very little. In toto: They would “attempt to narrow
down the list by reviewing the time stamped location coor-
dinates for each [device] and comparing that against the
known time and location information that is specific to this
crime.” 2 App. 136; see id., at 137; supra, at 7–8.
   The parties have contested the legality of each stage of
that process. Chatrie analogizes the first step to an “uncon-
stitutional general warrant,” and argues that in any event
the search at that step was both insufficiently described by
the warrant and lacking in probable cause. Brief for Cha-
trie 12; see id., at 13. As to steps two and three, Chatrie
contends that the warrant left too much authority to police
officers—and too little to the magistrate—to define the
search’s scope and determine whether cause for it existed.
See id., at 13–14. The Government, for its part, defends the
warrant at every step as seeking “particularized infor-
mation from Google’s database” based on “probable cause to
believe that Google had information” that would help solve
a crime. Brief for United States 14. And the Government
urges that the discretion given to the officers at steps two
and three fell within the bounds of reasonableness. See id.,
at 46.
   We leave all of those questions to the Court of Appeals to
decide in the first instance. Because the Fourth Circuit
panel concluded that no search had occurred, it did not ad-
dress whether the geofence warrant issued here validly au-
thorized each stage of the search process. Nor did the en
banc court’s one-sentence per curiam opinion speak to that
32               CHATRIE v. UNITED STATES

                     Opinion of the Court

issue. We are, as we have said many times before, “a court
of review, not of first view.” Cutter v. Wilkinson, 544 U. S.
709, 718, n. 7 (2005). It is therefore now up to the Court of
Appeals to decide whether, at each step of the search pro-
cess, the warrant satisfied the Fourth Amendment’s re-
quirements of particularity and probable cause.
                              IV
   In his famed and vindicated dissent, Justice Brandeis ex-
plained why a wiretap was a search, subject to Fourth
Amendment requirements. See Olmstead v. United States,
277 U. S. 438, 471 (1928). Those who drafted the Amend-
ment could not have imagined such a technology. But they
understood, Justice Brandeis wrote, a matter of more trans-
cendent importance: that Americans had “as against the
Government, the right to be let alone” and that the Fourth
Amendment must protect against “every unjustifiable in-
trusion by the Government upon the privacy of the individ-
ual, whatever the means employed.” Id., at 478.
   Far more recently, this Court in Carpenter invoked Jus-
tice Brandeis’s opinion in explaining why law enforcement
officials could not have “unrestricted access to a wireless
carrier’s database of physical location information.” 585
U. S., at 320. Said Carpenter: “[T]he Court is obligated—as
‘[s]ubtler and more far-reaching means of invading privacy
have become available to the Government’—to ensure that
the ‘progress of science’ does not erode Fourth Amendment
protections.” Ibid. (quoting 277 U. S., at 473–474 (dissent-
ing opinion)). For new technological tools, the Court con-
tinued, may “risk[ ] Government encroachment of the sort
the Framers, after consulting the lessons of history, drafted
the Fourth Amendment to prevent.” 585 U. S., at 320.
   Today’s decision follows from the same judicial obliga-
tion, to guard against the same risk of undue encroach-
ment. The Fourth Amendment applies, too, when officials
tap into Google’s “database of physical location
                  Cite as: 609 U. S. ____ (2026)                 33

                      Opinion of the Court

information.” Ibid. That database is new, but the principle
covering it is not: That principle is instead the one our his-
tory has given. The Fourth Amendment must, as ever, pro-
tect against unjustified governmental intrusion on the pri-
vacy of the individual.
  For the reasons stated, we vacate the judgment of the
Court of Appeals and remand the case for further proceed-
ings consistent with this opinion.
                                                   It is so ordered.
                 Cite as: 609 U. S. ____ (2026)           1

                    JACKSON, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 25–112
                         _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                        [June 29, 2026]

  JUSTICE JACKSON, with whom JUSTICE SOTOMAYOR joins,
concurring.
  I agree with the Court that law enforcement officers con-
ducted a search when they accessed petitioner Chatrie’s Lo-
cation History. I write separately because I would have
gone further to explain that this search violated the Fourth
Amendment. As the Court observes, “[w]hen officers have
obtained a warrant,” the validity of a search turns on
“whether a magistrate has properly found probable cause to
support a particularly described search.” Ante, at 30. In
my view, it is clear that at a minimum the second and third
stages of the search process here did not satisfy this foun-
dational requirement.
  At step two, the warrant authorized officers to access an
additional hour’s worth of Location History, unbounded by
the geofence’s perimeter. Though the warrant stated that
officers would “attempt to narrow down the list” of devices
subject to this step, there was no explicit requirement that
they do so. 2 App. 136 (emphasis added). Nor did the war-
rant set forth any criteria that officers would use in their
narrowing efforts. Ibid.
  The same infirmities carried over to step three. At this
step, the warrant authorized officers to access “identifying
account information,” including the username, date of
birth, account number, and any email addresses or
2                CHATRIE v. UNITED STATES

                    JACKSON, J., concurring

telephone numbers associated with the account. Id., at 137.
Once again, the warrant stated only that officers would “at-
tempt to narrow down the list,” without setting forth any
criteria for doing so. Ibid. (emphasis added).
   This “uncommon, multi-step” process, ante, at 30, meant
that officers conducted key portions of the search outside
the supervision of “a neutral and detached magistrate,”
Johnson v. United States, 333 U. S. 10, 14 (1948). Put dif-
ferently, officers could obtain additional, sensitive infor-
mation at steps two and three without having to convince a
magistrate that there was probable cause to believe this
particular information would uncover evidence related to
the crime. In this way, the warrant left “too much to the
discretion of the officer[s] executing the order,” giving them
a “roving commission” to collect more data absent any jus-
tification to a magistrate. Berger v. New York, 388 U. S. 41,
59 (1967).
   The facts of this case illustrate why the lack of magiste-
rial oversight is dangerous. When executing steps two and
three, law enforcement initially sought unbounded data
and account information from all 19 devices identified at
step one. See 590 F. Supp. 3d 901, 921 (ED Va. 2022).
Nothing in the warrant prevented officers from obtaining
this broad set of data; they narrowed the list only because
Google insisted on it. The officers eventually settled on re-
questing data from nine devices at step two, but even this
shorter list may have been overbroad. For three of the nine
devices, the location data showed the users’ movements to
and from sensitive spaces—namely, residences, a school,
and a hospital. See id., at 923. Given how it was written,
the warrant itself provided no “judicial check” on law en-
forcement’s determination that probable cause justified this
intrusion. Steagald v. United States, 451 U. S. 204, 220
(1981).
                  Cite as: 609 U. S. ____ (2026)            3

                     JACKSON, J., concurring

                         *     *    *
  The Court correctly observes that allowing the Govern-
ment to “access all of a cell-phone user’s movements” with-
out limit essentially arms it with “a virtual panopticon with
which to scrutinize its citizens’ activities.” Ante, at 21. It
is for this reason that law enforcement and courts must
carefully abide by the Fourth Amendment’s instruction that
“no Warrants shall issue, but upon probable cause, sup-
ported by Oath or affirmation, and particularly describing
the place to be searched, and the persons or things to be
seized.” The Fourth Circuit should keep this instruction in
mind on remand when evaluating the constitutionality of
the multi-step search that occurred here, especially at steps
two and three.
                  Cite as: 609 U. S. ____ (2026)              1

               GORSUCH, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 25–112
                          _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                         [June 29, 2026]

  JUSTICE GORSUCH, concurring in the judgment.
  I agree with the Court’s judgment that the government’s
examination of Okello Chatrie’s Location History data
amounted to a search for purposes of the Fourth Amend-
ment. But respectfully, I would reach that conclusion by a
different route.
                              I
  To decide whether a Fourth Amendment search took
place in this case, the Court once again invokes a test first
advanced in a solo concurrence in Katz v. United States, 389
U. S. 347 (1967). Under that test, a search occurs when the
government intrudes on an “expectation of privacy” that
“society is prepared to recognize as ‘reasonable.’ ” Id., at 361
(Harlan, J., concurring).
  If Katz has become a familiar feature of our law, it seems
to me no more persuasive for it. Consider just a few of its
problems, beginning with this: It has no basis in the Con-
stitution’s text or history. The Fourth Amendment’s pro-
tections do not depend on “the breach of some abstract ‘ex-
pectation of privacy’ whose contours are left to the judicial
imagination.” Carpenter v. United States, 585 U. S. 296,
391 (2018) (GORSUCH, J., dissenting). Instead, the Fourth
Amendment speaks in more concrete terms, protecting an
individual’s person, house, papers, and effects from
2                CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

unreasonable searches and seizures. Ibid. No surprise,
then, that it’s hard to find anything like the Katz test in the
law leading up to the Fourth Amendment’s adoption—or
anything much like it in this Court’s jurisprudence before
the 1960s.       See Carpenter, 585 U. S., at 391–392
(GORSUCH, J., dissenting).
   Even if I could overlook that problem with Katz, I still
wouldn’t know how to apply it. As the Court has candidly
admitted, it has never been able to identify a “single rubric”
that might “definitively resolv[e] which expectations of pri-
vacy are entitled to protection.” Carpenter, 585 U. S., at 304
(majority opinion). Maybe Katz poses an empirical ques-
tion, tagging reasonable expectations of privacy to those
privacy expectations “people actually have.” Carpenter, 585
U. S., at 392 (GORSUCH, J., dissenting). Or maybe the ques-
tion is a normative one, asking what expectations reasona-
ble people “should . . . have.” Ibid. In truth, nobody knows
and, either way, this Court is the wrong body for the task.
We aren’t equipped to make empirical assessments about
what most Americans think. Nor is it our job to enforce our
own normative judgments, as opposed to those embodied in
the Constitution and laws. Id., at 392–394.
   If this weren’t trouble enough, we’ve also adorned Katz
with an equally indefensible qualification called the third
party doctrine. Under its terms, the Court has held, an in-
dividual maintains no “reasonable expectation of privacy”
in information he shares with others. Accordingly, the gov-
ernment may freely search a person’s papers and effects
without triggering any Fourth Amendment scrutiny so long
as they are entrusted to the care of someone else. See Smith
v. Maryland, 442 U. S. 735, 743–744 (1979); United States
v. Miller, 425 U. S. 435, 442–443 (1976).
   Much as with Katz itself, this Court has never offered a
persuasive justification for its offshoot. Carpenter, 585
U. S., at 389–390 (GORSUCH, J., dissenting). Nor do I see
how it might. Do we seriously mean to suggest that most
                  Cite as: 609 U. S. ____ (2026)             3

               GORSUCH, J., concurring in judgment

Americans think they have no “reasonable expectation of
privacy” in records held for them by their banks or pharma-
cists or doctors or technology companies? If not, on what
authority might we rule that the American people should
not reasonably expect privacy in materials like those? Re-
ally, the third party doctrine amounts to little more than a
“doubtful application of Katz that lets the government
search almost whatever it wants whenever it wants.” Id.,
at 391.
   As it did eight years ago in Carpenter, the Court today
largely ignores these problems. It simply declares that Mr.
Chatrie enjoyed a reasonable expectation of privacy in his
Location History because authorities could have used it to
create “a virtual panopticon.” Ante, at 21. And it tells us
that the third party doctrine does not apply to this case be-
cause Mr. Chatrie did “ ‘not truly shar[e]’ ” his Location His-
tory with Google. Ante, at 25–26 (quoting Carpenter, 585
U. S., at 315 (majority opinion)).
   Count me unpersuaded. Why does tracking Mr. Chatrie’s
movements digitally over an hour or two invade his reason-
able expectation of privacy when an officer tailing him for
the same length of time would not? See United States v.
Knotts, 460 U. S. 276, 281–283 (1983). Why is Location His-
tory data Mr. Chatrie voluntarily shared with Google not
“truly shared” when a person’s bank records are? See Mil-
ler, 425 U. S., at 440–443. Does the Court just mean to give
Katz’s third party doctrine a quiet burial by suggesting to-
day that any information shared over “smartphones” using
“apps and services” falls outside its reach? Ante, at 28 (in-
ternal quotation marks omitted). And what does any of this
have to do with the Fourth Amendment’s terms anyway?
Even if Katz and its battered third party doctrine may
straggle on today, they leave our Fourth Amendment juris-
prudence about where the Court’s obscenity doctrine stood
in the 1960s: We know a “reasonable expectation of
4                CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

privacy” (and an exception to the third party doctrine) when
we see it.
                               II
   Rather than employ Katz and its third party doctrine, I
would take a different approach. To decide whether the
Fourth Amendment is in play, I would consult its terms,
asking first whether Location History qualifies as one of
Mr. Chatrie’s papers or effects, and then asking whether
the government searched those papers or effects. This tra-
ditional approach remains very much part of our law. See
Byrd v. United States, 584 U. S. 395, 403 (2018). Indeed,
we have expressly recognized that Katz and its progeny
“supplemen[t] rather than displac[e]” traditional Fourth
Amendment principles. Carpenter, 585 U. S., at 403 (ma-
jority opinion); see also Soldal v. Cook County, 506 U. S. 56,
64–65 (1992); United States v. Jones, 565 U. S. 400, 406–
407 (2012); Florida v. Jardines, 569 U. S. 1, 11 (2013).
   Thanks to Katz’s prominence today, of course, litigants
sometimes fail to press more traditional Fourth Amend-
ment arguments. See, e.g., Carpenter, 585 U. S., at 406
(GORSUCH, J., dissenting). But whatever his faults (possi-
bly including bank robbery), Mr. Chatrie has not forfeited
that line of attack in this case. In fact, he begins his brief
before us by contending that the Fourth Amendment is im-
plicated here precisely because the government enlisted
Google to search his “papers and effects.” See Brief for Pe-
titioner 15, 33.
   I agree with that assessment. Set aside whether Location
History data qualifies as among Mr. Chatrie’s “papers,” and
consider whether it at least constitutes one of his “effects.”
Based on the evidence the parties have put before us, it ap-
pears the word “effects” was understood at the time of the
Fourth Amendment’s adoption to embrace most any kind of
personal property. See, e.g., M. Brady, The Lost “Effects”
of the Fourth Amendment: Giving Personal Property Due
                  Cite as: 609 U. S. ____ (2026)            5

               GORSUCH, J., concurring in judgment

Protection, 125 Yale L. J. 946, 985–987 (2016) (“[E]arly
sources indicate that the term ‘effects’ meant ‘personal
property’ in common and colloquial usage”); L. Donohue,
The Original Fourth Amendment, 83 U. Chi. L. Rev. 1181,
1301 (2016) (effects meant “personal property or posses-
sions,” including “commercial items and goods”); Brief for
United States 32 (suggesting that “effects” excludes certain
real property like so-called open fields (citing Oliver v.
United States, 466 U. S. 170 (1984))).
   As I see it, Mr. Chatrie’s Location History data qualifies
as his personal property. To appreciate why, start with
this. As Google puts it, and no one seriously disputes, Lo-
cation History serves as a “diary” or map “of a person’s trav-
els.” Brief for Google LLC as Amicus Curiae 3–4. At the
time of the events in question, Mr. Chatrie’s agreement
with Google referred to Location History as “your” (mean-
ing, the user’s) “information.” 1 App. 72 (emphasis added).
Under the parties’ agreement, too, Mr. Chatrie was free to
“review” and “edit” his location data. Id., at 19. He was
even free to export or delete that data “from Google’s serv-
ers at will.” Ibid. Beyond all that, Google promised to pro-
tect his information against “unauthorized access, altera-
tion, disclosure, or destruction.” Id., at 71. Put simply, Mr.
Chatrie had the rights to enjoy, manage, alter, dispose, and
exclude others from what amounted to an electronic diary
or map of his travels. And as someone who held that many
“sticks in the bundle of rights . . . commonly characterized
as property”—including the “most treasured” and “essen-
tial” right to exclude—he has a strong claim that the Loca-
tion History data was his personal property. Cedar Point
Nursery v. Hassid, 594 U. S. 139, 149–150 (2021) (internal
quotation marks omitted).
   Next, notice what statutory and case law have to say on
the subject. The investigation of Mr. Chatrie unfolded in
Virginia. That State’s Computer Crimes Act expressly de-
scribes “computer data” as a form of “[p]roperty.” Va. Code
6                 CHATRIE v. UNITED STATES

               GORSUCH, J., concurring in judgment

Ann. §18.2–152.2 (2021). Altering or making an unauthor-
ized copy of computer data can constitute the crime of “com-
puter trespass” (another property law concept). §§18.2–
152.4(A)(3), (6). And the State provides a right to sue for
anyone “whose property or person is injured” by violations
of the Act (again suggesting a right to exclude). §18.2–
152.12(A).
   Nor is Virginia some outlier. In Texas, “computer . . .
data” can constitute “[p]roperty.” Tex. Penal Code Ann.
§33.01(16) (West Cum. Supp. 2025). State law likewise
criminalizes “knowingly access[ing] . . . a computer, com-
puter network, or computer system . . . with the intent to
obtain or use a file, data, or proprietary information” for a
prohibited purpose. §33.02(b–1)(2)(C) (West 2016). Once
more, as well, those whose “property has been injured” by
certain computer crimes may bring a “civil cause of action.”
Tex. Civ. Prac. & Rem. Code Ann. §143.001 (West 2019).
Georgia has a similar regime. See Ga. Code Ann. §§16–9–
93(b), (g) (2018) (criminalizing “[c]omputer [t]respass” and
providing a private right of action for such violations). And,
it appears, so do many other States. See Brief for Cato In-
stitute as Amicus Curiae 14–15, and n. 5 (“Today, more
than half of states . . . treat digital records and data as per-
sonal property,” and “[m]any” of them “make it illegal for
private actors to access or convert another person’s digital
data”); see also, e.g., People v. Seymour, 536 P. 3d 1260,
1273 (Colo. 2023) (finding that “law enforcement’s copying
of [the defendant’s] search history meaningfully interfered
with his possessory interest in that data”); Integrated Direct
Marketing, LLC v. May, 2016 Ark. 281, p. 6, 495 S. W. 3d
73, 76 (“[U]nder Arkansas law, intangible property, such as
electronic data, . . . can be converted”); cf. Thyroff v. Nation-
wide Mut. Ins. Co., 8 N. Y. 3d 283, 292–293, 864 N. E. 2d
1272, 1278 (2007) (holding that “electronic records that
were stored on a computer and were indistinguishable from
printed documents” are “subject to a claim of conversion”).
                   Cite as: 609 U. S. ____ (2026)              7

               GORSUCH, J., concurring in judgment

   To be sure, pursuant to its agreement with Mr. Chatrie,
Google stored his Location History data on its servers and
was free to use it for certain purposes. Brief for United
States 34–36. But an individual need not have “complete
ownership or exclusive control” before he can assert a
Fourth Amendment challenge against the search of real
property. Carpenter, 585 U. S., at 401 (GORSUCH, J., dis-
senting). Instead, we have long recognized, a “tenan[t] [or]
resident family membe[r]” who does not enjoy “fee simple
title” in a house has a sufficient interest in it to give rise to
a Fourth Amendment right. Ibid. And I fail to see why the
law should differ markedly when it comes to personal prop-
erty. If you “[t]oss your keys to a valet at a restaurant” or
“[a]sk your neighbor to look after your dog while you travel,”
you may entrust your personal property to another and li-
cense him to do certain things with it, much as Mr. Chatrie
did with his Location History data. Id., at 399. But that
hardly means that property is no longer yours. Ibid.
   Nor does it matter that those who wrote the Fourth
Amendment might not have imagined an electronic diary or
map of one’s travels. As with other laws, the terms found
in the Fourth Amendment carry their original public mean-
ing and can bear more applications than its drafters might
have expected or intended. See id., at 400. So just as the
First Amendment protects speech over the internet today
no less than it did speech delivered in the town square in
1791, it should hardly come as a surprise that the Fourth
Amendment might protect as personal “effects” electronic
diaries of one’s travels as it always has more traditional
ones. See Kyllo v. United States, 533 U. S. 27, 40 (2001)
(observing that a “search” of a home can take place not just
by physical entry but also by the external use of thermal-
imaging devices).
   Because Mr. Chatrie’s Location History data is his effect,
it is subject to the Fourth Amendment’s restrictions when
the government searches it. So, was there a search? The
8                CHATRIE v. UNITED STATES

              GORSUCH, J., concurring in judgment

government conducts a search when it “ ‘look[s] over or
through for the purpose of finding something.’ ” Id., at 32,
n. 1 (quoting N. Webster, An American Dictionary of the
English Language 66 (1828) (reprint 6th ed. 1989)). Under
our precedents, none of which the government asks us to
overrule, a search equally transpires when government of-
ficials enlist private parties in that task. See Skinner v.
Railway Labor Executives’ Assn., 489 U. S. 602, 614 (1989)
(Fourth Amendment “protects against” searches “effected”
by a private party “if the private party acted as an instru-
ment or agent of the Government”). And that’s exactly
what occurred here: The government conducted a search
both when it compelled Google to rummage through Mr.
Chatrie’s data at “step one,” and when it later examined
that data for itself and demanded more data yet from
Google at “step two.” See ante, at 7–8 (describing the step-
wise process in which the searches were conducted in this
case).
                             *
  I might have hoped that the Court would have pursued a
more traditional approach to the Fourth Amendment today.
But look carefully and you will see hints of it at work even
in the Court’s opinion. Why is the Court so protective of
Location History data, email, and electronically stored pho-
tos and calendars? See ante, at 25–26. Because, it turns
out, “a user reasonably understands” all those things “as
his own.” Ante, at 25. Put another way, they are his effects.
And why does the Court hold Mr. Chatrie’s effects protected
by the Fourth Amendment even though a third party stores
them? Because, the Court says, those effects remain his
“even though [they are] stored on Google’s servers.” Ibid.
Put another way, entrusting your effects to a third party for
certain agreed purposes doesn’t mean they are no longer
yours. While more work may lie ahead to bring coherence
                Cite as: 609 U. S. ____ (2026)         9

             GORSUCH, J., concurring in judgment

to our Fourth Amendment jurisprudence, perhaps this is a
start.
                  Cite as: 609 U. S. ____ (2026)            1

                      ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 25–112
                          _________________


         OKELLO T. CHATRIE, PETITIONER v.
                 UNITED STATES
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE FOURTH CIRCUIT
                         [June 29, 2026]

   JUSTICE ALITO, with whom JUSTICE THOMAS joins as to
Part I and with whom JUSTICE BARRETT joins as to Parts
II–B, II–C–1, and II–C–2, dissenting.
   Eight years ago, I warned that this Court’s decision in
Carpenter v. United States, 585 U. S. 296 (2018), would pro-
duce one of two outcomes. Either the Court would need to
clarify Carpenter’s limits in a future decision, or Carpenter
would usher in “revolutionary developments” in our doc-
trine by giving criminal suspects a “protected Fourth
Amendment interest in any sensitive personal information
about them that is collected and owned by third parties.”
Id., at 385 (ALITO, J., dissenting). Today, the Court takes
the country down the latter path. In doing so, the Court
sheds Carpenter’s self-imposed boundaries and further de-
stabilizes longstanding Fourth Amendment jurisprudence.
   To make matters worse, the majority does all this in an
advisory opinion. Although today’s decision will send seis-
mic waves through our Fourth Amendment doctrine, not
one iota of the majority opinion will affect the outcome of
this case. The Court knows this and does not claim other-
wise. Indeed, by refusing to review the one question that
could have at least theoretically given Chatrie some hope of
relief, the Court carefully set the stage for its planned per-
formance: striking a pose as a great champion of privacy in
2                CHATRIE v. UNITED STATES

                      ALITO, J., dissenting

the digital age. I cannot support this irresponsible esca-
pade.
                               I
  The Court should not have granted certiorari in this case,
and under any faithful application of our precedents, it
should now either dismiss this petition or affirm the deci-
sion below based on the “good-faith exception” to the exclu-
sionary rule. Instead, the Court issues an advisory opinion
concerning a now-obsolete “geofence” procedure. Last
Term, the Court worried out loud about rushing in to judge
“new technologies with transformative capabilities” that we
barely understand. TikTok Inc. v. Garland, 604 U. S. 56,
62 (2025) (per curiam). In cases involving such technology,
the Court proclaimed, we should take care not to “ ‘embar-
rass the future.’ ” Ibid. (quoting Northwest Airlines, Inc. v.
Minnesota, 322 U. S. 292, 300 (1944)). Today, the Court ex-
hibits no such modesty.
                             A
  It has long been established that federal courts may not
issue “advisory opinions” that do not bear on the rights of
the litigants before them. Lewis v. Continental Bank Corp.,
494 U. S. 472, 477 (1990). At the appellate stage, this prin-
ciple means that courts should resolve only those questions
on which a favorable ruling would provide a litigant redress
from the judgment below. See Food Marketing Institute v.
Argus Leader Media, 588 U. S. 427, 432–433 (2019). The
question on which the Court granted certiorari in this case
cannot satisfy this requirement under any colorable view of
the law. The Court should therefore decline to answer it.
  Okello Chatrie’s ongoing stake in this case stems from his
conviction for robbing a bank and brandishing a firearm.
On appeal, Chatrie challenged those convictions on only one
ground. He argued that the District Court erred in denying
his motion to suppress the fruits of the geofence procedure
                     Cite as: 609 U. S. ____ (2026)                    3

                          ALITO, J., dissenting

that led to his identification as the bank robber.1 So, unless
he can show that this evidence should be suppressed, he
cannot obtain any relief. And his chances of making the
showing needed to justify suppression are virtually zero.
  The police obtained information about Chatrie’s location
at the time of the robbery pursuant to a warrant issued by
a neutral magistrate. And when evidence is obtained under
such a warrant, a defendant seeking suppression must
overcome the good-faith exception to the exclusionary rule.
United States v. Leon, 468 U. S. 897, 923 (1984). A majority
of the Court of Appeals for the Fourth Circuit, sitting en
banc, held that Chatrie could not do so. 136 F. 4th 100, 101
(2025) (Diaz, C. J., concurring); id., at 114 (Niemeyer, J.,
concurring); id., at 115 (King, J., concurring); id., at 115,
n. 1 (Winn, J., concurring in judgment); id., at 142 (Hey-
tens, J., concurring). That holding suffices to affirm the
District Court’s admission of the geofence evidence and
thus independently supports the Fourth Circuit’s judg-
ment. Accordingly, any review by this Court should concern
an issue that could at least plausibly disturb that good-faith
holding. Cf. Stewart v. IHT Ins. Agcy. Group, LLC, 990
F. 3d 455, 457 (CA6 2021).
  On this score, today’s decision fails. The majority does
not dispute the Fourth Circuit’s good-faith analysis, and
nothing in its opinion casts a shred of doubt on that holding.
See ante, at 10, n. 4. To overcome the good-faith exception,
Chatrie would need to show that either (1) the affidavit sup-
porting the geofence warrant was knowingly or recklessly

——————
  1 The majority characterizes the issue as whether the Government may

introduce the location information that the police obtained through the
geofence procedure. But Chatrie also sought to suppress all the fruits of
that location information, and these could potentially include a firearm
matching one used in the crime, nearly $100,000 of currency in bands
bearing the bank teller’s signature, and his confession to the crime. See
Defendant’s Motion to Suppress in No. 3:19–cr–00130 (ED Va.), ECF
Doc. 29; Statement of Facts, ECF Doc. 229, p. 3.
4                     CHATRIE v. UNITED STATES

                             ALITO, J., dissenting

false, (2) the magistrate rubber-stamped the warrant appli-
cation, (3) the affidavit was “ ‘bare bones,’ ” or (4) the war-
rant application was so facially deficient that no reasonable
officer would rely on it. Leon, 468 U. S., at 923, and n. 24.
Yet nothing in the majority opinion touches on any of these
matters. Thus, nothing in today’s decision bears on the
Fourth Circuit’s good-faith holding. And because that hold-
ing independently supports the judgment below, the Court’s
opinion is advisory.2
   This outcome was guaranteed as soon as this Court
granted certiorari. When seeking review in this Court,
Chatrie recognized that dislodging the Fourth Circuit’s
judgment required that he prevail on the good-faith issue,
so his petition asked us to alter the good-faith exception.
See Pet. for Cert. i, 34–37 (asking the Court to create a
carve-out to the good-faith exception). Yet the Court ex-
cluded the good-faith issue from its grant of certiorari, 607
U. S. 1148 (2026), ensuring that any opinion would be advi-
sory. Indeed, even if the Court were to decide that the

——————
   2 I do not contend that the Court lacks Article III jurisdiction over this

case as a formal matter. Chatrie’s conviction suffices to render this liti-
gation a “case or controversy,” regardless of the question on which the
Court granted certiorari. The majority opinion is nonetheless advisory—
not because I think “the odds are strong” that Chatrie will lose on re-
mand, contra, ante, at 10, n. 4., but because the majority opinion does
not disturb the basis for the Fourth Circuit’s judgment and thus Cha-
trie’s conviction. This Court’s longstanding policy against issuing advi-
sory opinions on constitutional issues is not limited to cases where we
lack jurisdiction. See, e.g., Rescue Army v. Municipal Court of Los Ange-
les, 331 U. S. 549, 568 (1947) (holding that the Court possessed jurisdic-
tion over a case but nonetheless declining to exercise it because the
Court’s policy against issuing gratuitous constitutional opinions “has not
been limited to jurisdictional determinations”); Liverpool, New York &
Philadelphia S. S. Co. v. Commissioners of Emigration, 113 U. S. 33, 39
(1885) (“In the exercise of [its] jurisdiction, [this Court] is bound . . . never
to anticipate a question of constitutional law in advance of the necessity
of deciding it”). An opinion composed exclusively of dicta is no less advi-
sory simply because the Court has jurisdiction to pronounce such dicta.
                  Cite as: 609 U. S. ____ (2026)            5

                      ALITO, J., dissenting

warrant in this case was deficient, there would be no color-
able argument on remand that all reasonable officers would
have correctly predicted that outcome. See Leon, 468 U. S.,
at 923. After all, this Court has never provided guidance
on how to apply the Warrant Clause when the police re-
quest geolocation data from a third party. See Carpenter,
585 U. S., at 316–320 (noting only that such a warrant re-
quires probable cause). Accordingly, it would be nearly im-
possible for Chatrie to prove that the police here (and, by
extension, every other officer who ever relied on this type of
geofence warrant) acted in bad faith. See Davis v. United
States, 564 U. S. 229, 240 (2011) (Fourth Amendment vio-
lations “trigger the harsh sanction of exclusion only when
they are deliberate . . . and culpable”). In sum, no resolu-
tion of the question on which the Court granted certiorari
could have disturbed the Fourth Circuit’s good-faith hold-
ing and, thus, its judgment.
   The Court therefore erred by granting certiorari, and we
should now dismiss this petition as improvidently granted.
See Conway v. California Adult Authority, 396 U. S. 107,
110 (1969) (per curiam) (dismissing when resolving the is-
sue addressed in the petition would produce an advisory
opinion). Alternatively, this Court could affirm the decision
below on good-faith grounds. Although the Court did not
grant certiorari on this question, we may affirm a judgment
on any ground supported by the record, and we would not
be the court of “first view” on the good-faith issue. Upper
Skagit Tribe v. Lundgren, 584 U. S. 554, 560–561 (2018).
The Government properly presented this issue below, the
District Court admitted the contested evidence on good-
faith grounds, a majority of the en banc Fourth Circuit
voted to affirm on that basis, and the Government contin-
ued to press good faith at the petition and merits stages in
this Court. See Government’s Response in Opposition to
Defendant’s Motion for Suppression, ECF Doc. 41, p. 21;
590 F. Supp. 3d 901, 937 (ED Va. 2022); Brief in Opposition
6                CHATRIE v. UNITED STATES

                      ALITO, J., dissenting

13; Brief for United States 47–48. This Court therefore has
every reason to affirm on that ground.
  Instead, the Court charges forward to decide the question
presented, even though the majority cannot discern any im-
pact that its decision has on the Fourth Circuit’s judgment.
See ante, at 10, n. 4. The majority thus issues a plainly ad-
visory opinion, violating this Court’s “oldest and most con-
sistent” justiciability rule. Flast v. Cohen, 392 U. S. 83, 96
(1968) (internal quotation marks omitted).
                               B
   Advisory-opinion concerns aside, our prudential certio-
rari considerations further counseled against granting cer-
tiorari. Writs of certiorari are discretionary, and we reserve
them for “compelling” cases in which the court below “has
decided an important question of federal law.” This Court’s
Rule 10. The question in this case does not qualify.
   Chatrie’s petition asked whether the geofence procedure
that the police used here comports with the Fourth Amend-
ment. The answer to this question has scarcely any ongoing
significance. Google, the Government, and the majority all
agree that Google has modified its Location History service
in a manner that forecloses future use of this geofence pro-
cedure. Ante, at 4, n. 2; Brief for Google LLC as Amicus
Curiae 2; Brief for United States 42, n. 3. Chatrie does not
offer any evidence to the contrary. See Tr. of Oral Arg. 17–
18; Brief for Petitioner 5; Pet. for Cert. 10–11. As a result,
Fourth Amendment challenges to this geofence procedure
will likely pass into obscurity soon.
   This Court has long been averse to granting certiorari on
questions “that time [will] soon bury.” Darr v. Burford, 339
U. S. 200, 227 (1950) (Frankfurter, J., dissenting). This
aversion applies with special force here given this case’s
subject matter. The Fourth Amendment’s application to
surveillance technology turns on the “unique nature” of the
technology involved and the way in which the police use it
                  Cite as: 609 U. S. ____ (2026)             7

                      ALITO, J., dissenting

to collect information. Carpenter, 585 U. S., at 309. For
instance, when determining whether law enforcement’s use
of a technology requires a warrant or is otherwise “unrea-
sonable,” this Court has considered the technology’s capa-
bilities, prevalence, costliness, conspicuousness, intrusive-
ness, precision, accuracy, security, and comprehensiveness.
See, e.g., Kyllo v. United States, 533 U. S. 27, 34–35 (2001);
United States v. Jones, 565 U. S. 400, 429–431 (2012)
(ALITO, J., concurring in judgment); Maryland v. King, 569
U. S. 435, 446–465 (2013); Birchfield v. North Dakota, 579
U. S. 438, 461–464 (2016); Carpenter, 585 U. S., at 310–313.
Because these qualities vary from one technology to the
next, the specific application of the Fourth Amendment
does as well. Such variability renders this case all the less
suitable for our review. Whatever one’s jurisprudential
views about the Fourth Amendment in the digital age, a
case concerning a now-obsolete geofence procedure is an
odd vehicle for pronouncin

[...TRUNCATED 29626 of 149626 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Chavez v. Martinez.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Chavez v. Martinez"
type: case
citation: "538 U.S. 760 (2003)"
parallel_cite: "123 S. Ct. 1994; 155 L. Ed. 2d 984"
neutral_cite: 2003 U.S. LEXIS 4274
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-05-27
docket: 01-1444
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-05-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Chavez v. Martinez
  varies_by_point: false
  scope_note: "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/127927/chavez-v-martinez/"
  cluster_id: 127927
  opinion_id: 127927
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Key — Progeny"
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Related (cross-doctrine)"
related: ["[[Vega v. Tekoh]]", "[[Dickerson v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "section-1983", "qualified-immunity"]
holding: "The Self-Incrimination Clause is a trial right: coercive police questioning that produces no statement used against the suspect in a criminal case is not, by itself, a completed Fifth Amendment violation, so it cannot ground a § 1983 claim. Any remedy for the coercion lies (if at all) in substantive due process — remanded."
lake:
  record_id: Chavez v. Martinez
  status: verified
  projected_at: 2026-07-09
---

# Chavez v. Martinez

*538 U.S. 760 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Chavez questioned Martinez, who had been shot during a police encounter and was receiving emergency treatment, persistently and without [[Miranda and Custodial Interrogation|Miranda warnings]] while Martinez screamed in pain and begged for treatment. Martinez was never charged with a crime and his statements were never used against him in any criminal proceeding. He sued under 42 U.S.C. § 1983, alleging the coercive interrogation violated his Fifth and Fourteenth Amendment rights; the Ninth Circuit denied Chavez [[Qualified Immunity|qualified immunity]].

## Issue
Whether coercive police questioning that yields no statement ever used against the suspect in a criminal case violates the Fifth Amendment's Self-Incrimination Clause (or substantive due process) so as to support a § 1983 damages action.

## Rule
No completed Self-Incrimination Clause violation occurs from the questioning alone. The Fifth Amendment provides that no person "shall be compelled in any criminal case to be a witness against himself," and a plurality concluded: "We fail to see how, based on the text of the Fifth Amendment, Martinez can allege a violation of this right, since Martinez was never prosecuted for a crime, let alone compelled to be a witness against himself in a criminal case." — 538 U.S. at 766 (plurality opinion). ^pin-766

Statements compelled by interrogation may not be used at trial, "but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs" — the privilege is "a fundamental trial right." — [*Id.* at 767](https://www.courtlistener.com/opinion/127927/chavez-v-martinez/#:~:text=but%20it%20is%20not%20until%20their) (plurality op.) (quoting *United States v. Verdugo-Urquidez*). ^pin-767

Because the constitutional self-incrimination claim failed, the officer could not be liable under § 1983 on that theory. A separate question — whether the coercive interrogation independently violated **substantive due process** ("shocks the conscience") — was left open and [[Reading and Citing Cases#on-remand|remanded]].

## Application
On Martinez's own facts the Self-Incrimination Clause was never triggered: he was never prosecuted and his answers were never admitted as testimony against him in a criminal case, so he "was never made to be a 'witness' against himself." Accordingly his § 1983 claim premised on a Fifth Amendment self-incrimination violation could not proceed, and Chavez was entitled to [[Qualified Immunity|qualified immunity]] on that claim. The Court [[Reading and Citing Cases#on-remand|remanded]] Martinez's substantive-due-process claim for the lower courts to address in the first instance.

## Conclusion
Coercive interrogation, standing alone and without use of the statements in a criminal case, is not a completed Fifth Amendment violation and cannot support a § 1983 self-incrimination claim. The judgment was reversed in part and the case [[Reading and Citing Cases#on-remand|remanded]] on the due-process theory. (Fractured Court; Justice Thomas announced the judgment, with Justice Souter (joined by Justice Breyer) supplying the controlling rationale and the remand.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The Self-Incrimination-as-trial-right holding was carried forward and sharpened in [[Vega v. Tekoh]] (a Miranda violation is not itself a § 1983-actionable constitutional deprivation). *Chavez* remains the anchor for "no § 1983 self-incrimination claim absent use of the statement in a criminal case."

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny*
- [[Due-Process Voluntariness of Confessions]] — *Related (cross-doctrine)*

## Sources
- *Chavez v. Martinez*, 538 U.S. 760 (2003) — https://www.courtlistener.com/opinion/127927/chavez-v-martinez/ — pinpoints: 766, 767 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ab9b9b413315adf", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chavez v. Martinez"}, "payload": {"all": [{"cite": "538 U.S. 760", "page": "760", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "538"}, {"cite": "123 S. Ct. 1994", "page": "1994", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "123"}, {"cite": "155 L. Ed. 2d 984", "page": "984", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "155"}, {"cite": "2003 U.S. LEXIS 4274", "page": "4274", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2003"}], "display": "538 U.S. 760", "official": {"cite": "538 U.S. 760", "page": "760", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "538"}, "official_selection_present": true, "record_id": "Chavez v. Martinez"}}
{"assertion_id": "7d6c57ef5718fbcd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-767", "record_id": "Chavez v. Martinez"}, "payload": {"fragment": "#:~:text=but%20it%20is%20not%20until%20their", "page": null, "pin_id": "pin-767", "pinpoint_status": "slip-only", "quote": "but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs", "quote_fidelity": "matched", "record_id": "Chavez v. Martinez", "star_marker": null}}
{"assertion_id": "e6b9efc43cd29e2a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-766", "record_id": "Chavez v. Martinez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-766", "pinpoint_status": "slip-only", "quote": "--- # Chavez v. Martinez *538 U.S. 760 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Chavez questioned Martinez, who had been shot during a police encounter and was receiving emergency treatment, persistently and without Miranda warnings while Martinez screamed in pain and begged for treatment. Martinez was never charged with a crime and his statements were never used against him in any criminal proceeding. He sued under 42 U.S.C. § 1983, alleging the coercive interrogation violated his Fifth and Fourteenth Amendment rights; the Ninth Circuit denied Chavez qualified immunity. ## Issue Whether coercive police questioning that yields no statement ever used against the suspect in a criminal case violates the Fifth Amendment's Self-Incrimination Clause (or substantive due process) so as to support a § 1983 damages action. ## Rule No completed Self-Incrimination Clause violation occurs from the questioning alone. The Fifth Amendment provides that no person", "quote_fidelity": "mismatch", "record_id": "Chavez v. Martinez", "star_marker": null}}
{"assertion_id": "904426814925355e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chavez v. Martinez"}, "payload": {"as_of_content": "2003-05-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Chavez v. Martinez", "scope_note": "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law.", "varies_by_point": false}}
```

### lake record — Chavez v. Martinez

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chavez v. Martinez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Chavez v. Martinez",
    "case_name_short": "Chavez",
    "case_name_full": "Chavez v. Martinez",
    "input_case_name": "Chavez v. Martinez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-05-27",
    "year": 2003,
    "docket": "01-1444",
    "cluster_id": 127927,
    "lead_opinion_id": 127927,
    "sibling_ids": [
      127927,
      9434450,
      9434451,
      9434452,
      9434453,
      9434454,
      9434455
    ],
    "absolute_url": "/opinion/127927/chavez-v-martinez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 127891,
        "score": 20,
        "case_name": "Ben Chavez v. Oliverio Martinez"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "538 U.S. 760",
      "volume": "538",
      "reporter": "U.S.",
      "page": "760",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "123 S. Ct. 1994",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 984",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 4274",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "4274",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "538 U.S. 760",
        "volume": "538",
        "reporter": "U.S.",
        "page": "760",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 S. Ct. 1994",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 984",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "984",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 4274",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "4274",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "538 U.S. 760",
    "official_selection": {
      "court_class": "scotus",
      "selected": "538 U.S. 760",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-766",
      "page": null,
      "quote": "--- # Chavez v. Martinez *538 U.S. 760 (2003)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Chavez questioned Martinez, who had been shot during a police encounter and was receiving emergency treatment, persistently and without Miranda warnings while Martinez screamed in pain and begged for treatment. Martinez was never charged with a crime and his statements were never used against him in any criminal proceeding. He sued under 42 U.S.C. \u00a7 1983, alleging the coercive interrogation violated his Fifth and Fourteenth Amendment rights; the Ninth Circuit denied Chavez qualified immunity. ## Issue Whether coercive police questioning that yields no statement ever used against the suspect in a criminal case violates the Fifth Amendment's Self-Incrimination Clause (or substantive due process) so as to support a \u00a7 1983 damages action. ## Rule No completed Self-Incrimination Clause violation occurs from the questioning alone. The Fifth Amendment provides that no person",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-767",
      "page": null,
      "quote": "but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 21039,
      "fragment": "#:~:text=but%20it%20is%20not%20until%20their",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-05-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Chavez v. Martinez",
    "varies_by_point": false,
    "scope_note": "Fractured decision; the Self-Incrimination holding was reaffirmed and clarified by Vega v. Tekoh (2022). Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anthony Johnson v. Edward Winstead",
          "cluster_id": 4526340,
          "cite": [
            "900 F.3d 428"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kelly Park v. Karen Thompson",
          "cluster_id": 4375052,
          "cite": [
            "851 F.3d 910",
            "2017 WL 971806",
            "2017 U.S. App. LEXIS 4426"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marrero-Rodriguez v. Municipality of San Juan",
          "cluster_id": 799410,
          "cite": [
            "677 F.3d 497",
            "2012 U.S. App. LEXIS 9273",
            "2012 WL 1571234"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Uribe",
          "cluster_id": 5810602,
          "cite": [
            "199 Cal. App. 4th 836",
            "132 Cal. Rptr. 3d 102",
            "2011 Cal. App. LEXIS 1253"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 3065383,
          "cite": [
            "593 F.3d 841",
            "2010 WL 293758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane1_negative"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patane",
          "cluster_id": 137003,
          "cite": [
            "159 L. Ed. 2d 667",
            "124 S. Ct. 2620",
            "542 U.S. 630",
            "2004 U.S. LEXIS 4577"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Fontanes",
          "cluster_id": 203857,
          "cite": [
            "568 F.3d 263",
            "2009 U.S. App. LEXIS 12716",
            "2009 WL 1547737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harold Hall v. City of Los Angeles",
          "cluster_id": 809053,
          "cite": [
            "697 F.3d 1059",
            "83 Fed. R. Serv. 3d 930",
            "2012 WL 4335936",
            "2012 U.S. App. LEXIS 19980"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dias v. City and County of Denver",
          "cluster_id": 172192,
          "cite": [
            "567 F.3d 1169",
            "2009 U.S. App. LEXIS 11163",
            "2009 WL 1490359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Higazy v. Templeton",
          "cluster_id": 1384819,
          "cite": [
            "505 F.3d 161",
            "2007 WL 3024811"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crowe v. County of San Diego",
          "cluster_id": 148932,
          "cite": [
            "608 F.3d 406",
            "2010 U.S. App. LEXIS 12917",
            "2010 WL 2431842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
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
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Neal",
          "cluster_id": 2588587,
          "cite": [
            "72 P.3d 280",
            "1 Cal. Rptr. 3d 650",
            "31 Cal. 4th 63",
            "2003 Daily Journal DAR 7693",
            "2003 Cal. Daily Op. Serv. 6149",
            "2003 Cal. LEXIS 4426",
            "2003 WL 21639167"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Seering",
          "cluster_id": 1787414,
          "cite": [
            "701 N.W.2d 655",
            "2005 Iowa Sup. LEXIS 105",
            "2005 WL 1790924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew Livers v. Tim Dunning",
          "cluster_id": 811594,
          "cite": [
            "700 F.3d 340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hopkins v. Bonvicino",
          "cluster_id": 1448451,
          "cite": [
            "573 F.3d 752",
            "2009 U.S. App. LEXIS 15689",
            "2009 WL 2052987"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knight Ex Rel. Kerr v. Miami-Dade County",
          "cluster_id": 4389467,
          "cite": [
            "856 F.3d 795",
            "103 Fed. R. Serv. 388",
            "97 Fed. R. Serv. 3d 1086",
            "2017 WL 1755573",
            "2017 U.S. App. LEXIS 8036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffrey McKinley v. City of Mansfield",
          "cluster_id": 789901,
          "cite": [
            "404 F.3d 418",
            "22 I.E.R. Cas. (BNA) 1254",
            "2005 U.S. App. LEXIS 5875",
            "2005 WL 819969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sornberger v. City Of Knoxville",
          "cluster_id": 792982,
          "cite": [
            "434 F.3d 1006",
            "2006 U.S. App. LEXIS 1394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Earle",
          "cluster_id": 37873,
          "cite": [
            "405 F.3d 278",
            "2005 WL 730071"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence Antelope, United States of America v. Lawrence Antelope",
          "cluster_id": 789030,
          "cite": [
            "395 F.3d 1128",
            "2005 WL 170738"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Chavez v. Martinez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MzkzNjAwMDAwJnM9MjU5MDM5OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDcmcz0xMzQ2MzEyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 2,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(127927 OR 9434450 OR 9434451 OR 9434452 OR 9434453 OR 9434454 OR 9434455)",
    "indexed_citing_opinions": 403,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 127927,
        "count": 326,
        "count_source": "search"
      },
      {
        "opinion_id": 9434450,
        "count": 85,
        "count_source": "search"
      },
      {
        "opinion_id": 9434451,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434452,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434453,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434454,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434455,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 902,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/chavez-v-martinez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTkwMDkmcz0xMDAyNzkyNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28127927+OR+9434450+OR+9434451+OR+9434452+OR+9434453+OR+9434454+OR+9434455%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 127927,
        "cited_id": 88493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 93425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 108882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 110821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111549,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 112924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 121146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 244463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 340844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 516470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 583447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 676039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 775485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1634761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1635158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 1992428,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127927,
        "cited_id": 2285307,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T23:57:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:04:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:58:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Chavez v. Martinez (truncated)

```
<p class="case_cite"><span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">538 U.S. 760</a></span></p>
    <p class="parties">CHAVEZ<br>v.<br>MARTINEZ.</p>
    <p class="docket">No. 01-1444.</p>
    <p class="court">Supreme Court of United States.</p>
    <p class="date">Argued December 4, 2002.</p>
    <p class="date">Decided May 27, 2003.</p>
    <div class="prelims">
      <p class="indent">While respondent Martinez was being treated for gunshot wounds received during an altercation with police, he was interrogated by petitioner Chavez, a patrol supervisor. Martinez admitted that he used heroin and had taken an officer's gun during the incident. At no point was Martinez given <i>Miranda</i> warnings. Although he was never charged with a crime, and his answers were never used against him in any criminal proceeding, Martinez filed a <span class="citation no-link">42 U. S. C. &#167; 1983</span> suit, maintaining, among other things, that Chavez's actions violated his Fifth Amendment right not to be "compelled in any criminal case to be a witness against himself," and his Fourteenth Amendment substantive due process right to be free from coercive questioning. The District Court ruled that Chavez was not entitled to qualified immunity, and the Ninth Circuit affirmed, finding that Chavez's coercive questioning violated Martinez's Fifth Amendment rights even though his statements were not used against him in a criminal proceeding, and that a police officer violates due process when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial.</p>
      <p class="indent"><i>Held:</i> The judgment is reversed, and the case is remanded.</p>
      <p class="indent"><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852</a></span>, reversed and remanded.</p>
      <p class="indent">JUSTICE THOMAS, joined by THE CHIEF JUSTICE, JUSTICE O'CONNOR, and JUSTICE SCALIA, concluded in Part II-A that Chavez did not deprive Martinez of his Fifth Amendment rights. Pp. 766-773.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">(a) An officer is entitled to qualified immunity if his alleged conduct did not violate a constitutional right. See <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span>, 201. The text of the Fifth Amendment's Self-Incrimination Clause cannot support the Ninth Circuit's view that mere compulsive questioning violates the Constitution. A "criminal case" at the very least requires the initiation of legal proceedings, and police questioning does not constitute such a case. Statements compelled by police interrogation may not be used against a defendant in a criminal case, but it is not until such use that the Self-Incrimination Clause is violated, see <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span>. Martinez was never made to be a "witness" against himself because his statements were never admitted as testimony against him in a criminal case. Nor was he ever placed under oath and exposed to "`the cruel trilemma of self-accusation, perjury or contempt.'" <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span>. Pp. 766-767.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">(b) The Ninth Circuit's approach is also irreconcilable with this Court's case law. The government may compel witnesses to testify at trial or before a grand jury, on pain of contempt, so long as the witness is not the target of the criminal case in which he testifies, see, <i>e. g., Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#443" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 443</a></span>; and this Court has long permitted the compulsion of incriminating testimony so long as the statements (or evidence derived from them) cannot be used against the speaker in a criminal case, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#458" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 458</a></span>. Martinez was no more compelled in a criminal case to be a witness against himself than an immunized witness forced to testify on pain of contempt. That an immunized witness knows that his statements may not be used against him, while Martinez likely did not, does not make the immunized witness' statements any less compelled and lends no support to the Ninth Circuit's conclusion that coercive police interrogations alone violate the Fifth Amendment. Moreover, those subjected to coercive interrogations have an automatic protection from the use of their involuntary statements in any subsequent criminal trial, <i>e. g., Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 307-308</a></span>, which is coextensive with the use and derivative use immunity mandated by <i>Kastigar.</i> Pp. 767-770.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">(c) The fact that the Court has permitted the Fifth Amendment privilege to be asserted in noncriminal cases does not alter the conclusion in this case. Judicially created prophylactic rules &#8212; such as the rule allowing a witness to insist on an immunity agreement before being compelled to give testimony in noncriminal cases, and the exclusionary rule &#8212; are designed to safeguard the core constitutional right protected by the Self-Incrimination Clause. They do not extend the scope of that right itself, just as violations of such rules do not violate a person's constitutional rights. Accordingly, Chavez's failure to read <i>Miranda</i> warnings to Martinez did not violate Martinez's constitutional rights and cannot be grounds for a &#167; 1983 action. And the absence of a "criminal case" in which Martinez was compelled to be a "witness" against himself defeats his core Fifth Amendment claim. Pp. 770-773.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">JUSTICE SOUTER delivered the opinion of the Court with respect to Part II, concluding that the issue whether Martinez may pursue a claim of liability for a substantive due process violation should be addressed on remand. Pp. 779-780.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">JUSTICE SOUTER, joined by JUSTICE BREYER, concluded in Part I that Martinez's claim that his questioning alone was a violation of the Fifth and Fourteenth Amendments subject to redress by a <span class="citation no-link">42 U. S. C. &#167; 1983</span> damages action, though outside the core of Fifth Amendment protection, could be recognized if a core guarantee, or the judicial capacity to protect it, would be placed at risk absent complementary protection, see, <i>e. g., McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span>. However, Martinez cannot make the "powerful showing" necessary to expand protection of the privilege against self-incrimination to the point of the civil liability he requests. Inherent in his purely Fifth Amendment claim is the risk of global application in every instance of interrogation producing a statement inadmissible under the Fifth and Fourteenth Amendments, or violating one of the complementary rules this Court has accepted in aid of the core privilege. And Martinez has offered no reason to believe that this new rule is necessary in aid of the basic guarantee. Pp. 777-779.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">THOMAS, J., announced the judgment of the Court and delivered an opinion, which was joined by REHNQUIST, C. J., in full, by O'CONNOR, J., as to Parts I and II-A, and by SCALIA, J., as to Parts I and II. SOUTER, J., delivered an opinion, Part II of which was for the Court and was joined by STEVENS, KENNEDY, GINSBURG, and BREYER, JJ., and Part I of which concurred in the judgment and was joined by BREYER, J., <i>post,</i> p. 777. SCALIA, J., filed an opinion concurring in part in the judgment, <i>post,</i> p. 780. STEVENS, J., filed an opinion concurring in part and dissenting in part, <i>post,</i> p. 783. KENNEDY, J., filed an opinion concurring in part and dissenting in part, which was joined by STEVENS, J., in full and by GINSBURG, J., as to Parts II and III, <i>post,</i> p. 789. GINSBURG, J., filed an opinion concurring in part and dissenting in part, <i>post,</i> p. 799.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.</p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent"><i>Lawrence S. Robbins</i> argued the cause for petitioner. With him on the briefs were <i>Roy T. Englert, Jr., Kathryn S. Zecca, Alan E. Wisotsky, Jeffrey Held,</i> and <i>Gary L. Gillig.</i></p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent"><i>Deputy Solicitor General Clement</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Assistant Attorney General Chertoff, Assistant Attorney General McCallum, John P. Elwood, Barbara L. Herwig,</i> and <i>Peter R. Maier.</i></p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent"><i>Richard S. Paz</i> argued the cause for respondent. With him on the brief was <i>Sonia Mercado.</i><a class="footnote" href="#fn-s-3" id="fn-s-3_ref">*</a></p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">JUSTICE THOMAS announced the judgment of the Court and delivered an opinion.<a class="footnote" href="#fn-s-4" id="fn-s-4_ref">*</a></p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">This case involves a <span class="citation no-link">42 U. S. C. &#167; 1983</span> suit arising out of petitioner Ben Chavez's allegedly coercive interrogation of respondent Oliverio Martinez. The United States Court of Appeals for the Ninth Circuit held that Chavez was not entitled to a defense of qualified immunity because he violated Martinez's clearly established constitutional rights. We conclude that Chavez did not deprive Martinez of a constitutional right.</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">* On November 28, 1997, police officers Maria Pe&#241;a and Andrew Salinas were near a vacant lot in a residential area of Oxnard, California, investigating suspected narcotics activity. While Pe&#241;a and Salinas were questioning an individual, they heard a bicycle approaching on a darkened path that crossed the lot. They ordered the rider, respondent Martinez, to dismount, spread his legs, and place his hands behind his head. Martinez complied. Salinas then conducted a patdown frisk and discovered a knife in Martinez's waistband. An altercation ensued.<a class="footnote" href="#fn1" id="fn1_ref">1</a></p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">There is some dispute about what occurred during the altercation. The officers claim that Martinez drew Salinas' gun from its holster and pointed it at them; Martinez denies this. Both sides agree, however, that Salinas yelled, "`He's got my gun!'" App. to Pet. for Cert. 3a. Pe&#241;a then drew her gun and shot Martinez several times, causing severe injuries that left Martinez permanently blinded and paralyzed from the waist down. The officers then placed Martinez under arrest.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Petitioner Chavez, a patrol supervisor, arrived on the scene minutes later with paramedics. Chavez accompanied Martinez to the hospital and then questioned Martinez there while he was receiving treatment from medical personnel. The interview lasted a total of about 10 minutes, over a 45-minute period, with Chavez leaving the emergency room for periods of time to permit medical personnel to attend to Martinez.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">At first, most of Martinez's answers consisted of "I don't know," "I am dying," and "I am choking." App. 14, 17, 18. Later in the interview, Martinez admitted that he took the gun from the officer's holster and pointed it at the police. <span class="citation no-link"><i>Id.,</i> at 16</span>. He also admitted that he used heroin regularly. <span class="citation no-link"><i>Id.,</i> at 18</span>. At one point, Martinez said "I am not telling you anything until they treat me," yet Chavez continued the interview. <span class="citation no-link"><i>Id.,</i> at 14</span>. At no point during the interview was Martinez given warnings under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). App. to Pet. for Cert. 4a.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">Martinez was never charged with a crime, and his answers were never used against him in any criminal prosecution. Nevertheless, Martinez filed suit under Rev. Stat. &#167; 1979, <span class="citation no-link">42 U. S. C. &#167; 1983</span>, maintaining that Chavez's actions violated his Fifth Amendment right not to be "compelled in any criminal case to be a witness against himself," as well as his Fourteenth Amendment substantive due process right to be free from coercive questioning. The District Court granted summary judgment to Martinez as to Chavez's qualified immunity defense on both the Fifth and Fourteenth Amendment claims. Chavez took an interlocutory appeal to the Ninth Circuit, which affirmed the District Court's denial of qualified immunity. <i>Martinez</i> v. <i>Oxnard,</i> <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852</a></span> (2001). Applying <i>Saucier</i> v. <i>Katz,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./533/194/">533 U. S. 194</a></span> (2001), the Ninth Circuit first concluded that Chavez's actions, as alleged by Martinez, deprived Martinez of his rights under the Fifth and Fourteenth Amendments. The Ninth Circuit did not attempt to explain how Martinez had been "compelled in any criminal case to be a witness against himself." Instead, the Ninth Circuit reiterated the holding of an earlier Ninth Circuit case, <i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1229" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1229</a></span> (1992) (en banc), that "the Fifth Amendment's purpose is to prevent coercive interrogation practices that are destructive of human dignity," <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d, at 857</a></span> (internal quotation marks omitted), and found that Chavez's "coercive questioning" of Martinez violated his Fifth Amendment rights, "[e]ven though Martinez's statements were not used against him in a criminal proceeding," <i><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">ibid.</a></span></i> As to Martinez's due process claim, the Ninth Circuit held that "a police officer violates the Fourteenth Amendment when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial." <i><span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">Ibid.</a></span></i></p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">The Ninth Circuit then concluded that the Fifth and Fourteenth Amendment rights asserted by Martinez were clearly established by federal law, explaining that a reasonable officer "would have known that persistent interrogation of the suspect despite repeated requests to stop violated the suspect's Fifth and Fourteenth Amendment right to be free from coercive interrogation." <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#858" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police..."><i>Id.,</i> at 858</a></span>.</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./535/1111/">535 U. S. 1111</a></span> (2002).</p>
    </div>
    <p>II</p>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">In deciding whether an officer is entitled to qualified immunity, we must first determine whether the officer's alleged conduct violated a constitutional right. See <i>Katz,</i> 533 U. S., at 201. If not, the officer is entitled to qualified immunity, and we need not consider whether the asserted right was "clearly established." <i>Ibid.</i> We conclude that Martinez's allegations fail to state a violation of his constitutional rights.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p>* 1</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The Fifth Amendment, made applicable to the States by the Fourteenth Amendment, <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), requires that "[n]o person ... shall be compelled <i>in any criminal case</i> to be a <i>witness</i> against himself." U. S. Const., Amdt. 5 (emphases added). We fail to see how, based on the text of the Fifth Amendment, Martinez can allege a violation of this right, since Martinez was never prosecuted for a crime, let alone compelled to be a witness against himself in a criminal case.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Although Martinez contends that the meaning of "criminal case" should encompass the entire criminal investigatory process, including police interrogations, Brief for Respondent 23, we disagree. In our view, a "criminal case" at the very least requires the initiation of legal proceedings. See <i>Blyew</i> v. <i>United States,</i> <span class="citation" data-id="9416852"><a href="/opinion/88493/blyew-v-united-states/#595" aria-description="Citation for case: Blyew v. United States">13 Wall. 581, 595</a></span> (1872) ("The words `case' and `cause' are constantly used as synonyms in statutes and judicial decisions, each meaning <i>a proceeding in court, a suit, or action</i>" (emphasis added)); Black's Law Dictionary 215 (6th ed. 1990) (defining "[c]ase" as "[a] general term for an action, cause, suit, or controversy at law ...; a question <i>contested before a court of justice</i>" (emphasis added)). We need not decide today the precise moment when a "criminal case" commences; it is enough to say that police questioning does not constitute a "case" any more than a private investigator's precomplaint activities constitute a "civil case." Statements compelled by police interrogations of course may not be used against a defendant at trial, see <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 286</a></span> (1936), but it is not until their use in a criminal case that a violation of the Self-Incrimination Clause occurs, see <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990) ("The privilege against self-incrimination guaranteed by the Fifth Amendment is <i>a fundamental trial right</i> of criminal defendants. Although conduct by law enforcement officials prior to trial may ultimately impair that right, <i>a constitutional violation occurs only at trial</i>" (emphases added; citations omitted)); <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#692" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 692</a></span> (1993) (describing the Fifth Amendment as a "`trial right'"); <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#705" aria-description="Citation for case: Withrow v. Williams"><i>id.,</i> at 705</a></span> (O'CONNOR, J., concurring in part and dissenting in part) (describing "true Fifth Amendment claims" as "the extraction <i>and use</i> of compelled testimony" (emphasis altered)).</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Here, Martinez was never made to be a "witness" against himself in violation of the Fifth Amendment's Self-Incrimination Clause because his statements were never admitted as testimony against him in a criminal case. Nor was he ever placed under oath and exposed to "`the cruel trilemma of self-accusation, perjury or contempt.'" <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span> (1974) (quoting <i>Murphy</i> v. <i>Waterfront Comm'n of N. Y. Harbor,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964)). The text of the Self-Incrimination Clause simply cannot support the Ninth Circuit's view that the mere use of compulsive questioning, without more, violates the Constitution.</p>
    </div>
    <p>2</p>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Nor can the Ninth Circuit's approach be reconciled with our case law. It is well established that the government may compel witnesses to testify at trial or before a grand jury, on pain of contempt, so long as the witness is not the target of the criminal case in which he testifies. See <i>Minnesota</i> v. <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#427" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 427</a></span> (1984); <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#443" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 443</a></span> (1972). Even for persons who have a legitimate fear that their statements may subject them to criminal prosecution, we have long permitted the compulsion of incriminating testimony so long as those statements (or evidence derived from those statements) cannot be used against the speaker in any criminal case. See <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#602" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 602-604</a></span> (1896); <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#458" aria-description="Citation for case: Kastigar v. United States"><i>Kastigar, supra,</i> at 458</a></span>; <i>United States</i> v. <i>Balsys,</i> <span class="citation" data-id="9433709"><a href="/opinion/118242/united-states-v-balsys/#671" aria-description="Citation for case: United States v. Balsys">524 U. S. 666, 671-672</a></span> (1998). We have also recognized that governments may penalize public employees and government contractors (with the loss of their jobs or government contracts) to induce them to respond to inquiries, so long as the answers elicited (and their fruits) are immunized from use in any criminal case against the speaker. See <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#84" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 84-85</a></span> (1973) ("[T]he State may insist that [contractors] ... either respond to relevant inquiries about the performance of their contracts or suffer cancellation"); <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#806" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 806</a></span> (1977) ("Public employees may constitutionally be discharged for refusing to answer potentially incriminating questions concerning their official duties if they have not been required to surrender their constitutional immunity" against later use of statements in criminal proceedings).<a class="footnote" href="#fn2" id="fn2_ref">2</a> By contrast, no "penalty" may ever be imposed on someone who exercises his core Fifth Amendment right not to be a "witness" against himself in a "criminal case." See <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#614" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 614</a></span> (1965) (the trial court's and the prosecutor's comments on the defendant's failure to testify violates the Self-Incrimination Clause of the Fifth Amendment). Our holdings in these cases demonstrate that, contrary to the Ninth Circuit's view, mere coercion does not violate the text of the Self-Incrimination Clause absent use of the compelled statements in a criminal case against the witness.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">We fail to see how Martinez was any more "compelled in any criminal case to be a witness against himself" than an immunized witness forced to testify on pain of contempt. One difference, perhaps, is that the immunized witness <i>knows</i> that his statements will not, and may not, be used against him, whereas Martinez likely did not. But this does not make the statements of the immunized witness any less "compelled" and lends no support to the Ninth Circuit's conclusion that coercive police interrogations, absent the use of the involuntary statements in a criminal case, violate the Fifth Amendment's Self-Incrimination Clause. Moreover, our cases provide that those subjected to coercive police interrogations have an <i>automatic</i> protection from the use of their involuntary statements (or evidence derived from their statements) in any subsequent criminal trial. <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 307-308</a></span> (1985); <i>United States</i> v. <i>Blue,</i> <span class="citation" data-id="107238"><a href="/opinion/107238/united-states-v-blue/#255" aria-description="Citation for case: United States v. Blue">384 U. S. 251, 255</a></span> (1966); <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span> (1954); <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#155" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 155</a></span> (1944). See also <i>Pillsbury Co.</i> v. <i>Conboy,</i> <span class="citation" data-id="9428983"><a href="/opinion/110821/pillsbury-co-v-conboy/#278" aria-description="Citation for case: Pillsbury Co. v. Conboy">459 U. S. 248, 278</a></span> (1983) (Blackmun, J., concurring in judgment); <i>Williams</i> v. <i>United States,</i> <span class="citation" data-id="9424503"><a href="/opinion/108301/williams-v-united-states/#662" aria-description="Citation for case: Williams v. United States">401 U. S. 646, 662</a></span> (1971) (Brennan, J., concurring in result). This protection is, in fact, coextensive with the use and derivative use immunity mandated by <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></i> when the government compels testimony from a reluctant witness. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S., at 453</a></span>. Accordingly, the fact that Martinez did not <i>know</i> his statements could not be used against him does not change our view that no violation of the Fifth Amendment's Self-Incrimination Clause occurred here.</p>
    </div>
    <p>3</p>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">Although our cases have permitted the Fifth Amendment's self-incrimination privilege to be asserted in noncriminal cases, see <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#444" aria-description="Citation for case: Kastigar v. United States"><i>id.,</i> at 444-445</a></span> (recognizing that the "Fifth Amendment privilege against compulsory self-incrimination ... <i>can be asserted in any proceeding,</i> civil or criminal, administrative or judicial, investigatory or adjudicatory ..."); <i>Lefkowitz</i> v. <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley"><i>Turley, supra,</i> at 77</a></span> (stating that the Fifth Amendment privilege allows one "not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings"), that does not alter our conclusion that a violation of the constitutional <i>right</i> against self-incrimination occurs only if one has been compelled to be a witness against himself in a criminal case.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">In the Fifth Amendment context, we have created prophylactic rules designed to safeguard the core constitutional right protected by the Self-Incrimination Clause. See, <i>e. g., Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 444</a></span> (describing the "procedural safeguards" required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as "not themselves rights protected by the Constitution but ... measures to insure that the right against compulsory self-incrimination was protected" to "provide practical reinforcement for the right"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span> (stating that "[t]he <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule ... serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself"). Among these rules is an evidentiary privilege that protects witnesses from being forced to give incriminating testimony, even in noncriminal cases, unless that testimony has been immunized from use and derivative use in a future criminal proceeding before it is compelled. See <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States"><i>Kastigar, supra,</i> at 453</a></span>; <i>Maness</i> v. <i>Meyers,</i> <span class="citation" data-id="9425898"><a href="/opinion/109130/maness-v-meyers/#461" aria-description="Citation for case: Maness v. Meyers">419 U. S. 449, 461-462</a></span> (1975) (noting that the Fifth Amendment privilege may be asserted if one is "compelled to produce evidence which later <i>may</i> be used against him as an accused in a criminal action" (emphasis added)).</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">By allowing a witness to insist on an immunity agreement <i>before</i> being compelled to give incriminating testimony in a noncriminal case, the privilege preserves the core Fifth Amendment right from invasion by the use of that compelled testimony in a subsequent criminal case. See <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 440-441</a></span> ("Testimony obtained in civil suits, or before administrative or legislative committees, could [absent a grant of immunity] prove so incriminating that a person compelled to give such testimony might readily be convicted on the basis of those disclosures in a subsequent criminal proceeding"). Because the failure to assert the privilege will often forfeit the right to exclude the evidence in a subsequent "criminal case," see <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#440" aria-description="Citation for case: Minnesota v. Murphy">465 U. S., at 440</a></span>; <i>Garner</i> v. <i>United States,</i> <span class="citation" data-id="9426311"><a href="/opinion/109400/garner-v-united-states/#650" aria-description="Citation for case: Garner v. United States">424 U. S. 648, 650</a></span> (1976) (failure to claim privilege against self-incrimination before disclosing incriminating information on tax returns forfeited the right to exclude that information in a criminal prosecution); <i>United States</i> v. <i>Kordel,</i> <span class="citation" data-id="108066"><a href="/opinion/108066/united-states-v-kordel/#7" aria-description="Citation for case: United States v. Kordel">397 U. S. 1, 7</a></span> (1970) (criminal defendant forfeited his right to assert Fifth Amendment privilege with regard to answers he gave to interrogatories in a prior civil proceeding), it is necessary to allow assertion of the privilege prior to the commencement of a "criminal case" to safeguard the core Fifth Amendment trial right. If the privilege could not be asserted in such situations, testimony given in those judicial proceedings would be deemed "voluntary," see <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/#371" aria-description="Citation for case: Rogers v. United States">340 U. S. 367, 371</a></span> (1951); <i>United States</i> v. <i>Monia,</i> <span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/#427" aria-description="Citation for case: United States v. Monia">317 U. S. 424, 427</a></span> (1943); hence, insistence on a prior grant of immunity is essential to memorialize the fact that the testimony had indeed been compelled and therefore protected from use against the speaker in any "criminal case."</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">Rules designed to safeguard a constitutional right, however, do not extend the scope of the constitutional right itself, just as violations of judicially crafted prophylactic rules do not violate the constitutional rights of any person. As we explained, we have allowed the Fifth Amendment privilege to be asserted by witnesses in noncriminal cases in order to safeguard the core constitutional right defined by the Self-Incrimination Clause &#8212; the right not to be compelled in any criminal case to be a witness against oneself.<a class="footnote" href="#fn3" id="fn3_ref">3</a> We have likewise established the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule as a prophylactic measure to prevent violations of the right protected by the text of the Self-Incrimination Clause &#8212; the admission into evidence in a criminal case of confessions obtained through coercive custodial questioning. See <i>Warren</i> v. <i>Lincoln,</i> <span class="citation" data-id="9478572"><a href="/opinion/516470/jackson-warren-v-city-of-lincoln-nebraska-james-breen-sandra-l-myers-and/#1442" aria-description="Citation for case: Jackson Warren v. City of Lincoln, Nebraska James Breen...">864 F. 2d 1436, 1442</a></span> (CA8 1989) (alleged <i>Miranda</i> violation not actionable under &#167; 1983); <i>Giuffre</i> v. <i>Bissell,</i> <span class="citation" data-id="676039"><a href="/opinion/676039/james-j-giuffre-v-nicholas-bissell-richard-thornburg-robert-smith-russ/#1256" aria-description="Citation for case: James J. Giuffre v. Nicholas Bissell Richard Thornburg...">31 F. 3d 1241, 1256</a></span> (CA3 1994) (same); <i>Bennett</i> v. <i>Passic,</i> <span class="citation" data-id="340844"><a href="/opinion/340844/howard-smith-bennett-v-albert-passic-sheriff-etc/#1263" aria-description="Citation for case: Howard Smith Bennett v. Albert Passic, Sheriff, Etc.">545 F. 2d 1260, 1263</a></span> (CA10 1976) (same); see also <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#686" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 686</a></span> (1984) (Marshall, J., dissenting) ("All the Fifth Amendment forbids is the introduction of coerced statements at trial"). Accordingly, Chavez's failure to read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to Martinez did not violate Martinez's constitutional rights and cannot be grounds for a &#167; 1983 action. See <i>Connecticut</i> v. <i>Barrett,</i> <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#528" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 528</a></span> (1987) (<i>Miranda</i>'s warning requirement is "not itself required by the Fifth Amendmen[t] ... but is instead justified only by reference to its prophylactic purpose"); <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 444</a></span> (<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s safeguards "were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected"). And the absence of a "criminal case" in which Martinez was compelled to be a "witness" against himself defeats his core Fifth Amendment claim. The Ninth Circuit's view that mere compulsion violates the Self-Incrimination Clause, see <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d, at 857</a></span>; <i>California Attorneys for Criminal Justice</i> v. <i>Butts,</i> <span class="citation" data-id="6984365"><a href="/opinion/7079352/california-attorneys-for-criminal-justice-v-butts/#1045" aria-description="Citation for case: California Attorneys for Criminal Justice v. Butts">195 F. 3d 1039, 1045-1046</a></span> (1999); <i>Cooper,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1243" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d, at 1243-1244</a></span>, finds no support in the text of the Fifth Amendment and is irreconcilable with our case law.<a class="footnote" href="#fn4" id="fn4_ref">4</a> Because we find that Chavez's alleged conduct did not violate the Self-Incrimination Clause, we reverse the Ninth Circuit's denial of qualified immunity as to Martinez's Fifth Amendment claim.</p>
    </div>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">Our views on the proper scope of the Fifth Amendment's Self-Incrimination Clause do not mean that police torture or other abuse that results in a confession is constitutionally permissible so long as the statements are not used at trial; it simply means that the Fourteenth Amendment's Due Process Clause, rather than the Fifth Amendment's Self-Incrimination Clause, would govern the inquiry in those cases and provide relief in appropriate circumstances.<a class="footnote" href="#fn5" id="fn5_ref">5</a></p>
    </div>
    <p class="center">B</p>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">The Fourteenth Amendment provides that no person shall be deprived "of life, liberty, or property, without due process of law." Convictions based on evidence obtained by methods that are "so brutal and so offensive to human dignity" that they "shoc[k] the conscience" violate the Due Process Clause. <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172, 174</a></span> (1952) (overturning conviction based on evidence obtained by involuntary stomach pumping). See also <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#435" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 435</a></span> (1957) (reiterating that evidence obtained through conduct that "`shock[s] the conscience'" may not be used to support a criminal conviction). Although <i><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span></i> did not establish a civil remedy for abusive police behavior, we recognized in <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#846" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 846</a></span> (1998), that deprivations of liberty caused by "the most egregious official conduct," <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#846" aria-description="Citation for case: County of Sacramento v. Lewis"><i>id.,</i> at 846, 847-848, n. 8</a></span>, may violate the Due Process Clause. While we rejected, in <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span>,</i> a &#167; 1983 plaintiff's contention that a police officer's deliberate indifference during a high-speed chase that caused the death of a motorcyclist violated due process, <i>id.,</i> at 854, we left open the possibility that unauthorized police behavior in other contexts might "shock the conscience" and give rise to &#167; 1983 liability. <i>Id.,</i> at 850.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">We are satisfied that Chavez's questioning did not violate Martinez's due process rights. Even assuming, <i>arguendo,</i> that the persistent questioning of Martinez somehow deprived him of a liberty interest, we cannot agree with Martinez's characterization of Chavez's behavior as "egregious" or "conscience shocking." As we noted in <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span>,</i> the official conduct "most likely to rise to the conscience-shocking level" is the "conduct intended to injure in some way unjustifiable by any government interest." <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis"><i>Id.,</i> at 849</a></span>. Here, there is no evidence that Chavez acted with a purpose to harm Martinez by intentionally interfering with his medical treatment. Medical personnel were able to treat Martinez throughout the interview, App. to Pet. for Cert. 4a, 18a, and Chavez ceased his questioning to allow tests and other procedures to be performed. <i><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Id.,</a></span></i> at 4a. Nor is there evidence that Chavez's conduct exacerbated Martinez's injuries or prolonged his stay in the hospital. Moreover, the need to investigate whether there had been police misconduct constituted a justifiable government interest given the risk that key evidence would have been lost if Martinez had died without the authorities ever hearing his side of the story.</p>
    </div>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">The Court has held that the Due Process Clause also protects certain "fundamental liberty interest[s]" from deprivation by the government, regardless of the procedures provided, unless the infringement is narrowly tailored to serve a compelling state interest. <i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702, 721</a></span> (1997). Only fundamental rights and liberties which are "`deeply rooted in this Nation's history and tradition'" and "`implicit in the concept of ordered liberty'" qualify for such protection. <i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Ibid.</a></span></i> Many times, however, we have expressed our reluctance to expand the doctrine of substantive due process, see <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#842" aria-description="Citation for case: County of Sacramento v. Lewis"><i>Lewis, supra,</i> at 842</a></span>; <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#720" aria-description="Citation for case: Washington v. Glucksberg"><i>Glucksberg, supra,</i> at 720</a></span>; <i>Albright</i> v. <i>Oliver,</i> <span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/#271" aria-description="Citation for case: Albright v. Oliver">510 U. S. 266, 271</a></span> (1994); <i>Reno</i> v. <i>Flores,</i> <span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/#302" aria-description="Citation for case: Reno v. Flores">507 U. S. 292, 302</a></span> (1993); in large part "because guideposts for responsible decisionmaking in this unchartered area are scarce and open-ended," <i>Collins</i> v. <i>Harker Heights,</i> <span class="citation" data-id="112699"><a href="/opinion/112699/collins-v-city-of-harker-heights/#125" aria-description="Citation for case: Collins v. City of Harker Heights">503 U. S. 115, 125</a></span> (1992). See also <i>Regents of Univ. of Mich.</i> v. <i>Ewing,</i> <span class="citation" data-id="9430245"><a href="/opinion/111549/regents-of-the-university-of-michigan-v-ewing/#225" aria-description="Citation for case: Regents of the University of Michigan v. Ewing">474 U. S. 214, 225-226</a></span> (1985).</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent"><i><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></i> requires a "`careful description'" of the asserted fundamental liberty interest for the purposes of substantive due process analysis; vague generalities, such as "the right not to be talked to," will not suffice. <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/#721" aria-description="Citation for case: Washington v. Glucksberg">521 U. S., at 721</a></span>. We therefore must take into account the fact that Martinez was hospitalized and in severe pain during the interview, but also that Martinez was a critical nonpolice witness to an altercation resulting in a shooting by a police officer, and that the situation was urgent given the perceived risk that Martinez might die and crucial evidence might be lost. In these circumstances, we can find no basis in our prior jurisprudence, see, <i>e. g., Miranda,</i> 384 U. S., at 477-478 ("It is an act of responsible citizenship for individuals to give whatever information they may have to aid in law enforcement"), or in our Nation's history and traditions to suppose that freedom from unwanted police questioning is a right so fundamental that it cannot be abridged absent a "compelling state interest." <span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/#302" aria-description="Citation for case: Reno v. Flores"><i>Flores, supra,</i> at 302</a></span>. We have never required such a justification for a police interrogation, and we decline to do so here. The lack of any "guideposts for responsible decisionmaking" in this area, and our oft-stated reluctance to expand the doctrine of substantive due process, further counsel against recognizing a new "fundamental liberty interest" in this case.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">We conclude that Martinez has failed to allege a violation of the Fourteenth Amendment, and it is therefore unnecessary to inquire whether the right asserted by Martinez was clearly established.</p>
    </div>
    <p>III</p>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">Because Chavez did not violate Martinez's Fifth and Fourteenth Amendment rights, he was entitled to qualified immunity. The judgment of the Court of Appeals for the Ninth Circuit is therefore reversed, and the case is remanded for further proceedings.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">
        <i>It is so ordered.</i>
      </p>
    </div>
    <div class="footnotes">
      <div class="footnote">
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn-s-3">
        <a class="footnote" href="#fn-s-3_ref">*</a>
        <p> Briefs of<i>amici curiae</i> urging reversal were filed for the State of California <i>ex rel.</i> Bill Lockyer by <i>Mr. Lockyer,</i> Attorney General, <i>pro se, Robert R. Anderson,</i> Chief Assistant Attorney General, <i>Jo Graves,</i> Senior Assistant Attorney General, <i>Stan Cross,</i> Supervising Deputy Attorney General, and <i>Lee E. Seale</i> and <i>Patrick J. Whalen,</i> Deputy Attorneys General; for the City of Escondido by <i>Jeffrey R. Epp</i> and <i>Richard J. Schneider;</i> for 50 California Cities et al. by <i>Girard Fisher;</i> for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger</i> and <i>Charles L. Hobson;</i> and for the National Association of Police Organizations by <i>Devallis Rutledge</i> and <i>William J. Johnson.</i></p>
        <p class="indent">Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union Foundation et al. by <i>Mark D. Rosenbaum, Steven R. Shapiro, Susan N. Herman, John T. Philipsborn,</i> and <i>Erwin Chemerinsky;</i> for the Association of Trial Lawyers of America by <i>Jeffrey L. Needle;</i> and for the National Police Accountability Project et al. by <i>Susan R. Klein</i> and <i>Michael Avery.</i></p>
      </div>
      <div class="footnote" id="fn-s-4">
        <a class="footnote" href="#fn-s-4_ref">*</a>
        <p> THE CHIEF JUSTICE joins this opinion in its entirety. JUSTICE O'CONNOR joins Parts I and II-A of this opinion. JUSTICE SCALIA joins Parts I and II of this opinion</p>
      </div>
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> The parties disagree over what triggered the altercation. The officers maintain that Martinez ran away from them and that they tackled him while in pursuit; Martinez asserts that he never attempted to flee and Salinas tackled him without warning</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> The government may not, however, penalize public employees and government contractors to induce them to waive their<i>immunity</i> from the use of their compelled statements in subsequent criminal proceedings. See <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968); <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70</a></span> (1973), and this is true even though immunity is not itself a right secured by the text of the Self-Incrimination Clause, but rather a prophylactic rule we have constructed to protect the Fifth Amendment's right from invasion. See Part II-A-3, <i>infra.</i> Once an immunity waiver is signed, the signatory is unable to assert a Fifth Amendment objection to the subsequent use of his statements in a criminal case, even if his statements were in fact compelled. A waiver of immunity is therefore a prospective waiver of the core self-incrimination right in any subsequent criminal proceeding, and States cannot condition public employment on the waiver of constitutional rights, <i>Lefkowitz, supra,</i> at 85.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> That the privilege is a prophylactic one does not alter our penalty cases jurisprudence, which allows such privilege to be asserted prior to, and outside of, criminal proceedings</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> It is JUSTICE KENNEDY'S indifference to the text of the Self-Incrimination Clause, as well as a conspicuous absence of a single citation to the actual text of the Fifth Amendment, that permits him to adopt the Ninth Circuit's interpretation</p>
        <p class="indent"><i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), on which JUSTICE KENNEDY and JUSTICE GINSBURG rely in support of their reading of the Fifth Amendment, was a case addressing the <i>admissibility</i> of a coerced confession under the <i>Due Process</i> Clause. <i><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span></i> did not even mention the Fifth Amendment or the Self-Incrimination Clause, and refutes JUSTICE KENNEDY'S and JUSTICE GINSBURG'S assertions that their interpretation of that Clause would have been known to any reasonable officer at the time Chavez conducted his interrogation.</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> We also do not see how, in light of<i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), JUSTICE KENNEDY can insist that "the Self-Incrimination Clause is applicable at the time and place police use compulsion to extract a statement from a suspect" while at the same time maintaining that the use of "torture or its equivalent in an attempt to induce a statement" violates the Due Process Clause. <i>Post,</i> at 795, 796 (opinion concurring in part and dissenting in part). <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> foreclosed the use of substantive due process analysis in claims involving the use of excessive force in effecting an arrest and held that such claims are governed <i>solely</i> by the Fourth Amendment's prohibitions against "unreasonable" seizures, because the Fourth Amendment provided the explicit source of constitutional protection against such conduct. <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S., at 394-395</a></span>. If, as JUSTICE KENNEDY believes, the Fifth Amendment's Self-Incrimination Clause governs coercive police interrogation even absent use of compelled statements in a criminal case, then <i><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span></i> suggests that the Due Process Clause would not.</p>
        <p>JUSTICE SOUTER delivered an opinion, Part II of which is the opinion of the Court and Part I of which is an opinion concurring in the judgment.<a class="footnote" href="#fn-s-5" id="fn-s-5_ref">*</a></p>
      </div>
      <div class="footnote" id="fn-s-5">
        <a class="footnote" href="#fn-s-5_ref">*</a>
        <p class="indent"> Respondent Martinez's claim under <span class="citation no-link">42 U. S. C. &#167; 1983</span> for violation of his privilege against compelled self-incrimination should be rejected and his case remanded for further proceedings. I write separately because I believe that our decision requires a degree of discretionary judgment greater than JUSTICE THOMAS acknowledges. As he points out, the text of the Fifth Amendment (applied here under the doctrine of Fourteenth Amendment incorporation) focuses on courtroom use of a criminal defendant's compelled, self-incriminating testimony, and the core of the guarantee against compelled self-incrimination is the exclusion of any such evidence. JUSTICE GINSBURG makes it clear that the present case is very close to<i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), and Martinez's testimony would clearly be inadmissible if offered in evidence against him. But Martinez claims more than evidentiary protection in asking this Court to hold that the questioning alone was a completed violation of the Fifth and Fourteenth Amendments subject to redress by an action for damages under &#167; 1983.</p>
        <p class="indent">To recognize such a constitutional cause of action for compensation would, of course, be well outside the core of Fifth Amendment protection, but that alone is not a sufficient reason to reject Martinez's claim. As Justice Harlan explained in his dissent in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), "extension[s]" of the bare guarantee may be warranted, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#510" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 510</a></span>, if clearly shown to be desirable means to protect the basic right against the invasive pressures of contemporary society, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#515" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 515</a></span>. In this light, we can make sense of a variety of Fifth Amendment holdings: barring compulsion to give testimonial evidence in a civil proceeding, see <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/#40" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34, 40</a></span> (1924); requiring a grant of immunity in advance of any testimonial proffer, see <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#446" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 446-447</a></span> (1972); precluding threats or impositions of penalties that would undermine the right to immunity, see, <i>e. g., Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/#284" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280, 284-285</a></span> (1968); <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 77-79</a></span> (1973); <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#804" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 804-806</a></span> (1977); <i>McKune</i> v. <i>Lile,</i> <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#35" aria-description="Citation for case: McKune v. Lile">536 U. S. 24, 35</a></span> (2002) (plurality opinion); and conditioning admissibility on warnings and waivers to promote intelligent choices and to simplify subsequent inquiry into voluntariness, see <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda, supra.</a></span></i> All of this law is outside the Fifth Amendment's core, with each case expressing a judgment that the core guarantee, or the judicial capacity to protect it, would be placed at some risk in the absence of such complementary protection.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> do not, however, believe that Martinez can make the "powerful showing," subject to a realistic assessment of costs and risks, necessary to expand protection of the privilege against compelled self-incrimination to the point of the civil liability he asks us to recognize here. See<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#515" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 515, 517</a></span> (Harlan, J., dissenting). The most obvious drawback inherent in Martinez's purely Fifth Amendment claim to damages is its risk of global application in every instance of interrogation producing a statement inadmissible under Fifth and Fourteenth Amendment principles, or violating one of the complementary rules we have accepted in aid of the privilege against evidentiary use. If obtaining Martinez's statement is to be treated as a stand-alone violation of the privilege subject to compensation, why should the same not be true whenever the police obtain any involuntary self-incriminating statement, or whenever the government so much as threatens a penalty in derogation of the right to immunity, or whenever the police fail to honor <i>Miranda?</i><a class="footnote" href="#fn-s-6" id="fn-s-6_ref">*</a> Martinez offers no limiting principle or reason to foresee a stopping place short of liability in all such cases.</p>
        <p class="indent">Recognizing an action for damages in every such instance not only would revolutionize Fifth and Fourteenth Amendment law, but would beg the question that must inform every extension or recognition of a complementary rule in service of the core privilege: why is this new rule necessary in aid of the basic guarantee? Martinez has offered no reason to believe that the guarantee has been ineffective in all or many of those circumstances in which its vindication has depended on excluding testimonial admissions or barring penalties. And I have no reason to believe the law has been systemically defective in this respect.</p>
        <p class="indent">But if there is no failure of efficacy infecting the existing body of Fifth Amendment law, any argument for a damages remedy in this case must depend not on its Fifth Amendment feature but upon the particular charge of outrageous conduct by the police, extending from their initial encounter with Martinez through the questioning by Chavez. That claim, however, if it is to be recognized as a constitutional one that may be raised in an action under &#167; 1983, must sound in substantive due process. See generally <i>County of Sacramento</i> v. <i>Lewis,</i> <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 849</a></span> (1998) ("[C]onduct intended to injure in some way unjustifiable by any government interest is the sort of official action most likely to rise to the conscience-shocking level"). Here, it is enough to say that JUSTICE STEVENS shows that Martinez has a serious argument in support of such a position.</p>
        <p>II</p>
        <p class="indent">Whether Martinez may pursue a claim of liability for a substantive due process violation is thus an issue that should be addressed on remand, along with the scope and merits of any such action that may be found open to him.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn-s-6">
        <a class="footnote" href="#fn-s-6_ref">*</a>
        <p> JUSTICE BREYER joins this opinion in its entirety. JUSTICE STEVENS, JUSTICE KENNEDY, and JUSTICE GINSBURG join Part II of this opinion</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p> The question whether the absence of<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings may be a basis for a &#167; 1983 action under any circumstance is not before the Court.</p>
        <p class="indent">JUSTICE SCALIA, concurring in part in the judgment.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> agree with the Court's rejection of Martinez's Fifth Amendment claim, that is, his claim that Chavez violated his right not to be compelled in any criminal case to be a witness against himself<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a> See <i>ante,</i> at 766-767 (plurality opinion); <i>ante,</i> at 777-779 (SOUTER, J., concurring in judgment). And without a violation of the right protected by the text of the Self-Incrimination Clause (what the plurality and JUSTICE SOUTER call the Fifth Amendment's "core"), Martinez's <span class="citation no-link">42 U. S. C. &#167; 1983</span> action is doomed. Section 1983 does not provide remedies for violations of judicially created prophylactic rules, such as the rule of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), as the Court today holds, see <i>ante,</i> at 772 (plurality opinion); <i>post,</i> at 789-790 (KENNEDY, J., concurring in part and dissenting in part); nor is it concerned with "extensions" of constitutional provisions designed to safeguard actual constitutional rights, cf. <i>ante,</i> at 777-778 (SOUTER, J., concurring in judgment).<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> Rather, a plaintiff seeking redress through &#167; 1983 must establish the violation of a federal constitutional or statutory <i>right.</i> See <i>Blessing</i> v. <i>Freestone,</i> <span class="citation" data-id="9842134"><a href="/opinion/118101/blessing-v-freestone/#340" aria-description="Citation for case: Blessing v. Freestone">520 U. S. 329, 340</a></span> (1997); <i>Golden State Transit Corp.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="9431857"><a href="/opinion/112341/golden-state-transit-corp-v-city-of-los-angeles/#106" aria-description="Citation for case: Golden State Transit Corp. v. City of Los Angeles">493 U. S. 103, 106</a></span> (1989).</p>
        <p class="indent">My reasons for rejecting Martinez's Fifth Amendment claim are those set forth in JUSTICE THOMAS'S opinion. I join Parts I and II of that opinion, including Part II-B, which deals with substantive due process. Consideration and rejection of that constitutional claim is absolutely necessary to support reversal of the Ninth Circuit's judgment. For after discussing (and erroneously deciding) Martinez's Fifth Amendment claim, the Ninth Circuit continued as follows:</p>
        <p class="indent">"Likewise, a police officer violates the Fourteenth Amendment when he obtains a confession by coercive conduct, regardless of whether the confession is subsequently used at trial. `The due process violation caused by coercive behavior of law-enforcement officers in pursuit of a confession is <i>complete with the coercive behavior itself.... The actual use or attempted use of that coerced statement in a court of law is not necessary to complete the affront to the Constitution.' Cooper v. Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d at 1244-45</a></span> (emphasis added). Mr. Martinez has thus stated a <i>prima facie</i> case that Sergeant Chavez violated his Fifth and Fourteenth Amendment rights to be free from police coercion in pursuit of a confession." <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852, 857</a></span> (2001).</p>
        <p class="indent">It seems to me impossible to interpret this passage as anything other than an invocation of the doctrine of "substantive due process," which makes unlawful certain government conduct, regardless of whether the procedural guarantees of the Fifth Amendment (or the guarantees of any of the other provisions of the Bill of Rights) have been violated. See <i>Washington</i> v. <i>Glucksberg,</i> <span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U. S. 702</a></span> (1997). To be sure, the term "substantive due process" is not used in the quoted passage, but the passage's technically false dichotomy between Fifth Amendment and Fourteenth Amendment rights uses "Fourteenth Amendment rights" as a stand-in for <i>that aspect</i> of the Fourteenth Amendment which consists of the doctrine of substantive due process. (JUSTICE THOMAS uses similar shorthand in the concluding sentence of his analysis: "Our views on the proper scope of the Fifth Amendment's Self-Incrimination Clause do not mean that police torture or other abuse that results in a confession is constitutionally permissible so long as the statements are not used at trial; it simply means that the Fourteenth Amendment's Due Process Clause, rather than the Fifth Amendment's Self-Incrimination Clause, would govern the inquiry in those cases." <i>Ante,</i> at 773.) What other <i>possible meaning</i> could the passage possess? Surely the Ninth Circuit was not expending a paragraph to make the utterly useless observation that, in addition to violating the Fifth Amendment (because that is incorporated in the Fourteenth) Chavez violated the Fourteenth Amendment (because that incorporates the Fifth). That <i>substantive due process</i> was the point is confirmed by the fact that the sole authority cited to support violation of "the Fourteenth Amendment" is <i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1244-1245</a></span> (1992), a Ninth Circuit case that explicitly recognized a substantive-due-process right to be free from coercive police questioning. See <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1244" aria-description="Citation for case: Cooper v. Dupnik"><i>id.,</i> at 1244-1250</a></span>.</p>
        <p class="indent">Since the Ninth Circuit's Fourteenth Amendment holding rested upon substantive due process, we are without authority to disturb that court's judgment solely because of our disagreement with its Fifth Amendment (Self-Incrimination Clause) analysis; the substantive-due-process holding provides an independent ground supporting the decision that Chavez was not entitled to qualified immunity. While JUSTICE SOUTER declines to address that independent ground &#8212; even though the parties extensively briefed the issue, Brief for Petitioner 21-36; Brief for Respondent 29-40; Reply Brief for Petitioner 8-12; Brief for United States as <i>Amicus Curiae</i> 17-23, and even though JUSTICE STEVENS discusses it in dissent, <i>post,</i> at 787-788 (opinion concurring in part and dissenting in part) &#8212; I believe that addressing it, and resolving it against respondent, is essential to the Court's disposition, which reverses the Ninth Circuit's judgment in its entirety.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> therefore see no basis for a remand to determine "[w]hether Martinez may pursue a claim of liability for a substantive due process violation."<i>Ante,</i> at 779 (majority opinion). That question has already been decided by the Ninth Circuit, and we today reverse its decision. My disagreement with the Court, however, is of little consequence, because Martinez will not be able to prevail on remand by raising anew his substantive-due-process claim. Not only is the claim meritless, as JUSTICE THOMAS demonstrates, <i>ante,</i> at 774-776, but Martinez already had his chance to press a substantive-due-process theory in the Court of Appeals and chose not to, even though Ninth Circuit precedent clearly established substantive due process (including &#8212; contrary to the Government's assertion at oral argument, see Tr. of Oral Arg. 26 &#8212; a "shocks the conscience" criterion) as an available theory of liability under the Fourteenth Amendment. See <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1248" aria-description="Citation for case: Cooper v. Dupnik"><i>Cooper, supra,</i> at 1248</a></span> ("There is a second Fourteenth Amendment substantive due process yardstick available to Cooper as a theory of &#167; 1983 liability. The test is whether the Task Force's conduct `shocks the conscience'"). Nowhere did respondent's appellate brief mention the words "substantive due process"; the only rights it asserted were the right against self-incrimination and the right to warnings under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Appellees' Responding Brief in No. 00-56520 (CA9), pp. 28-32, 36-43. If, as JUSTICE SOUTER apparently believes, the opinion below did not address respondent's "substantive due process" claim, that claim has been forfeited.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> While occasionally referring to this as a "Fifth Amendment claim," a convention commonly followed, JUSTICE THOMAS and JUSTICE SOUTER acknowledge that technically it is a Fourteenth Amendment claim, since it is only<i>through</i> the Fourteenth Amendment that the Fifth is "made applicable to the States," <i>ante,</i> at 766 (opinion of THOMAS, J.), citing <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964).</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> Still less does &#167; 1983 provide a remedy for actions inconsistent with the perceived "purpose" of a constitutional provision. Cf<i>Martinez</i> v. <i>Oxnard,</i> <span class="citation" data-id="775485"><a href="/opinion/775485/oliverio-martinez-v-city-of-oxnard-oxnard-police-department-art-lopez/#857" aria-description="Citation for case: Oliverio Martinez v. City of Oxnard Oxnard Police...">270 F. 3d 852, 857</a></span> (CA9 2001) ("[T]he Fifth Amendment's purpose is to prevent coercive interrogation practices that are destructive of human dignity" (internal quotation marks omitted)).</p>
        <p class="indent">JUSTICE STEVENS, concurring in part and dissenting in part.</p>
        <p class="indent">As a matter of fact, the interrogation of respondent was the functional equivalent of an attempt to obtain an involuntary confession from a prisoner by torturous methods. As a matter of law, that type of brutal police conduct constitutes an immediate deprivation of the prisoner's constitutionally protected interest in liberty. Because these propositions are so clear, the District Court and the Court of Appeals correctly held that petitioner is not entitled to qualified immunity.</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p class="indent"> What follows is an English translation of portions of the tape-recorded questioning in Spanish that occurred in the emergency room of the hospital when, as is evident from the text, both parties believed that respondent was about to die:</p>
        <p class="indent">"Chavez: What happened? Olivero, tell me what happened.</p>
        <p class="indent">"O[liverio] M[artinez]: I don't know.</p>
        <p class="indent">"Chavez: I don't know what happened (sic)?</p>
        <p class="indent">"O.M.: Ay! I am dying. Ay! What are you doing to me?</p>
        <p class="indent">"No, ...! (unintelligible scream).</p>
        <p class="indent">"Chavez: What happened, sir?</p>
        <p class="indent">"O.M.: My foot hurts ...</p>
        <p class="indent">"Chavez: Olivera. Sir, what happened?</p>
        <p class="indent">"O.M.: I am choking.</p>
        <p class="indent">"Chavez: Tell me what happened.</p>
        <p class="indent">"O.M.: I don't know.</p>
        <p class="indent">"Chavez: `I don't know.'</p>
        <p class="indent">"O.M.: My leg hurts.</p>
        <p class="indent">"Chavez: I don't know what happened (sic)?</p>
        <p class="indent">"O.M.: It hurts ...</p>
        <p class="indent">"Chavez: Hey, hey look.</p>
        <p class="indent">"O.M.: I am choking.</p>
        <p class="indent">"Chavez: Can you hear? look listen, I am Benjamin Chavez with the police here in Oxnard, look.</p>
        <p class="indent">"O. M.: I am dying, please.</p>
        <p class="indent">"Chavez: OK, yes, tell me what happened. If you are going to die, tell me what happened. Look I need to tell (sic) what happened.</p>
        <p class="indent">"O. M.: I don't know.</p>
        <p class="indent">"Chavez: You don't know, I don't know what happened (sic)? Did you talk to the police?</p>
        <p class="indent">"O. M.: Yes.</p>
        <p class="indent">"Chavez: What happened with the police?</p>
        <p class="indent">"O. M.: We fought.</p>
        <p class="indent">"Chavez: Huh? What happened with the police?</p>
        <p class="indent">"O. M.: The police shot me.</p>
        <p class="indent">"Chavez: Why?</p>
        <p class="indent">"O. M.: Because I was fighting with him.</p>
        <p class="indent">"Chavez: Oh, why were you fighting with the police?</p>
        <p class="indent">"O. M.: I am dying ...</p>
        <p class="indent">"Chavez: OK, yes you are dying, but tell me why you are fighting, were you fighting with the police?</p>
        <p>. . . . .</p>
        <p class="indent">"O. M.: Doctor, please I want air, I am dying.</p>
        <p class="indent">"Chavez: OK, OK. I want to know if you pointed the gun [to yourself] at the police.</p>
        <p class="indent">"O. M.: Yes.</p>
        <p class="indent">"Chavez: Yes, and you pointed it [to yourself]? (sic) at the police pointed the gun? (sic) Huh?</p>
        <p class="indent">"O. M.: I am dying, please . . .</p>
        <p>. . . . .</p>
        <p class="indent">"Chavez: OK, listen, listen I want to know what happened, ok??</p>
        <p class="indent">"O. M.: I want them to treat me.</p>
        <p class="indent">"Chavez: OK, they are do it (sic), look when you took out the gun from the tape (sic) of the police ...</p>
        <p class="indent">"O. M.: I am dying ...</p>
        <p class="indent">"Chavez: Ok, look, what I want to know if you took out (sic) the gun of the police?</p>
        <p class="indent">"O. M.: I am not telling you anything until they treat me.</p>
        <p class="indent">"Chavez: Look, tell me what happened, I want to know, look well don't you want the police know (sic) what happened with you? "O. M.: Uuuggghhh! my belly hurts ...</p>
        <p>. . . . .</p>
        <p class="indent">"Chavez: Nothing, why did you run (sic) from the police?</p>
        <p class="indent">"O. M.: I don't want to say anything anymore.</p>
        <p class="indent">"Chavez: No?</p>
        <p class="indent">"O. M.: I want them to treat me, it hurts a lot, please.</p>
        <p class="indent">"Chavez: You don't want to tell (sic) what happened with you over there?</p>
        <p class="indent">"O. M.: I don't want to die, I don't want to die.</p>
        <p class="indent">"Chavez: Well if you are going to die tell me what happened, and right now you think you are going to die?</p>
        <p class="indent">"O. M.: No.</p>
        <p class="indent">"Chavez: No, do you think you are going to die?</p>
        <p class="indent">"O. M.: Aren't you going to treat me or what?</p>
        <p class="indent">"Chavez: Look, think you are going to die, (sic) that's all I want to know, if you think you are going to die? Right now, do you think you are going to die?</p>
        <p class="indent">"O. M.: My belly hurts, please treat me.</p>
        <p class="indent">"Chavez: Sir?</p>
        <p class="indent">"O. M.: If you treat me I tell you everything, if not, no.</p>
        <p class="indent">"Chavez: Sir, I want to know if you think you are going to die right now?</p>
        <p class="indent">"O. M.: I think so.</p>
        <p class="indent">"Chavez: You think (sic) so? Ok. Look, the doctors are going to help you with all they can do, Ok?. That they can do.</p>
        <p class="indent">"O. M.: Get moving, I am dying, can't you see me? come on.</p>
        <p class="indent">"Chavez: Ah, huh, right now they are giving you medication." App. 8-22.</p>
        <p class="indent">The sound recording of this interrogation, which has been lodged with the Court, vividly demonstrates that respondent was suffering severe pain and mental anguish throughout petitioner's persistent questioning.</p>
        <p class="center">II</p>
        <p class="indent">The Due Process Clause of the Fourteenth Amendment protects individuals against state action that either "`shocks the conscience,' <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 172</a></span> (1952), or interferes with rights `implicit in the concept of ordered liberty,' <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 325-326</a></span> (1937)." <i>United States</i> v. <i>Salerno,</i> <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno">481 U. S. 739, 746</a></span> (1987). In <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko</a></span>,</i> the majority of the Court refused to hold that every violation of the Fifth Amendment satisfied the second standard. In a host of other cases, however, the Court has held that unusually coercive police interrogation procedures do violate that standard.<a class="footnote" href="#fn1-2" id="fn1-2_ref">1</a></p>
        <p class="indent">By its terms, the Fifth Amendment itself has no application to the States. It is, however, one source of the protections against state actions that deprive individuals of rights "implicit in the concept of ordered liberty" that the Fourteenth Amendment guarantees. Indeed, as I pointed out in my dissent in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#371" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 371</a></span> (1985), it is the most specific provision in the Bill of Rights "that protects all citizens from the kind of custodial interrogation that was once employed by the Star Chamber, by `the Germans of the 1930's and early 1940's,' and by some of our own police departments only a few decades ago."<a class="footnote" href="#fn2-2" id="fn2-2_ref">2</a> Whenever it occurs, as it did here, official interrogation of that character is a classic example of a violation of a constitutional right "implicit in the concept of ordered liberty."<a class="footnote" href="#fn3-1" id="fn3-1_ref">3</a></p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> respectfully dissent, but for the reasons articulated by JUSTICE KENNEDY,<i>post,</i> at 799, concur in Part II of JUSTICE SOUTER'S opinion.</p>
        <p>Notes:</p>
      </div>
      <div class="footnote" id="fn1-2">
        <a class="footnote" href="#fn1-2_ref">1</a>
        <p> JUSTICE O'CONNOR listed many of these cases, as well as cases from state courts, in<i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312-313, n. 3</a></span> (1985): <i>"Darwin</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423713"><a href="/opinion/107694/darwin-v-connecticut/" aria-description="Citation for case: Darwin v. Connecticut">391 U. S. 346</a></span> (1968) (suspect interrogated for 48 hours incommunicado while officers denied access to counsel); <i>Beecher</i> v. <i>Alabama,</i> <span class="citation" data-id="9423505"><a href="/opinion/107526/beecher-v-alabama/#36" aria-description="Citation for case: Beecher v. Alabama">389 U. S. 35, 36</a></span> (1967) (officer fired rifle next to suspect's ear and said `If you don't tell the truth I am going to kill you'); <i>Clewis</i> v. <i>Texas,</i> <span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707</a></span> (1967) (suspect was arrested without probable cause, interrogated for nine days with little food or sleep, and gave three unwarned `confessions' each of which he immediately retracted); <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#439" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 439-440, n. 3</a></span> (1961) (mentally retarded youth interrogated incommunicado for a week `during which time he was frequently ill, fainted several times, vomited blood on the floor of the police station and was twice taken to the hospital on a stretcher').... <i>Cagle</i> v. <i>State,</i> <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#4" aria-description="Citation for case: Cagle v. State">45 Ala. App. 3, 4</a></span>, <span class="citation" data-id="1635158"><a href="/opinion/1635158/cagle-v-state/#120" aria-description="Citation for case: Cagle v. State">221 So. 2d 119, 120</a></span> (1969) (police interrogated wounded suspect at police station for one hour before obtaining statement, took him to hospital to have his severe wounds treated, only then giving the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings; suspect prefaced second statement with `I have already give the Chief a statement and I might as well give one to you, too'), cert. denied, <span class="citation multiple-matches"><a href="/c/Ala./284/727/">284 Ala. 727</a></span>, <span class="citation multiple-matches"><a href="/c/So.%202d/221/121/">221 So. 2d 121</a></span> (1969); <i>People</i> v. <i>Saiz,</i> <span class="citation" data-id="9558965"><a href="/opinion/1196896/people-v-saiz/" aria-description="Citation for case: People v. Saiz">620 P. 2d 15</a></span> (Colo. 1980) (two hours' unwarned custodial interrogation of 16-year-old in violation of state law requiring parent's presence, culminating in visit to scene of crime); <i>People</i> v. <i>Bodner,</i> 75 App. Div. 2d 440, 430 N. Y. S. 2d 433 (1980) (confrontation at police station and at scene of crime between police and retarded youth with mental age of eight or nine); <i>State</i> v. <i>Badger,</i> <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#441" aria-description="Citation for case: State v. Badger">141 Vt. 430, 441</a></span>, <span class="citation" data-id="2285307"><a href="/opinion/2285307/state-v-badger/#343" aria-description="Citation for case: State v. Badger">450 A. 2d 336, 343</a></span> (1982) (unwarned `close and intense' station house questioning of 15-year-old, including threats and promises, resulted in confession at 1:20 a.m.; court held `[w]arnings ... were insufficient to cure such blatant abuse or compensate for the coercion in this case')."</p>
      </div>
      <div class="footnote" id="fn2-2">
        <a class="footnote" href="#fn2-2_ref">2</a>
        <p> Adding to the cases cited by JUSTICE O'CONNOR, I appended this footnote: "See,<i>e. g., Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954); <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> (1945); <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944); <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span> (1942); <i>Vernon</i> v. <i>Alabama,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./313/547/">313 U. S. 547</a></span> (1941); <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span> (1940); <i>Canty</i> v. <i>Alabama,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./309/629/">309 U. S. 629</a></span> (1940); <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span> (1940); <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936); <i>Wakat</i> v. <i>Harlib,</i> <span class="citation" data-id="244463"><a href="/opinion/244463/leslie-george-wakat-v-peter-f-harlib-irwin-haviland-harold-t-thompsen/" aria-description="Citation for case: Leslie George Wakat v. Peter F. Harlib, Irwin Haviland,...">253 F. 2d 59</a></span> (CA7 1958); <i>People</i> v. <i>La Frana,</i> <span class="citation" data-id="1992428"><a href="/opinion/1992428/people-v-la-frana/" aria-description="Citation for case: People v. La Frana">4 Ill. 2d 261</a></span>, <span class="citation" data-id="1992428"><a href="/opinion/1992428/people-v-la-frana/" aria-description="Citation for case: People v. La Frana">122 N. E. 2d 583</a></span> (1954); cf. <i>People</i> v. <i>Portelli,</i> 15 N. Y. 2d 235, <span class="citation" data-id="5521593"><a href="/opinion/5674064/people-v-portelli/" aria-description="Citation for case: People v. Portelli">205 N. E. 2d 857</a></span> (1965) (potential witness tortured by police). Such custodial interrogation is, of course, closer to that employed by the Soviet Union than that which our constitutional scheme tolerates. See <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#15" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 15-16</a></span> (1970) (opinion of Douglas, J.) (`In [Russia] detention <i>incommunicado</i> is the common practice, and the period of permissible detention now extends for nine months. Where there is custodial interrogation, it is clear that the critical stage of the trial takes place long before the courtroom formalities commence. That is apparent to one who attends criminal trials in Russia. Those that I viewed never put in issue the question of guilt; guilt was an issue resolved in the inner precincts of a prison under questioning by the police')." <i>Id.,</i> at 371-372, n. 19 (dissenting opinion).</p>
      </div>
      <div class="footnote" id="fn3-1">
        <a class="footnote" href="#fn3-1_ref">3</a>
        <p> A person's constitutional right to remain silent is an interest in liberty that is protected against federal impairment by the Fifth Amendment and from state impairment by the Due Process Clause of the Fourteenth Amendment. JUSTICE THOMAS' opinion is fundamentally flawed in two respects. It incorrectly assumes that the claim it rejects is not a due process claim,<i>ante,</i> at 772-773, and it incorrectly assumes that coercive interrogation is not unconstitutional when it occurs because it merely violates a judge-made "prophylactic" rule. But the violation in this case is far more serious than a mere failure to advise respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights; moreover, the Court disavowed the "prophylactic" characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#437" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 437-439</a></span> (2000).</p>
        <p class="indent">JUSTICE KENNEDY, with whom JUSTICE STEVENS joins, and with whom JUSTICE GINSBURG joins as to Parts II and III, concurring in part and dissenting in part.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> single police interrogation now presents us with two issues: first, whether failure to give a required warning under<i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), was itself a completed constitutional violation actionable under <span class="citation no-link">42 U. S. C. &#167; 1983</span>; and second, whether an actionable violation arose at once under the Self-Incrimination Clause (applicable to the States through the Fourteenth Amendment) when the police, after failing to warn, used severe compulsion or extraordinary pressure in an attempt to elicit a statement or confession.</p>
      </div>
      <div class="footnote">
        <a class="footnote">I</a>
        <p class="indent"> agree with JUSTICE THOMAS that failure to give a<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning does not, without more, establish a completed violation when the unwarned interrogation ensues. As to the second aspect of the case, which does not involve the simple failure to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning, it is my respectful submission that JUSTICE SOUTER and JUSTICE THOMAS are incorrect. They conclude that a violation of the Self-Incrimination Clause does not arise until a privileged statement is introduced at some later criminal proceeding.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> constitutional right is traduced the moment torture or its close equivalents are brought to bear. Constitutional protection for a tortured suspect is not held in abeyance until some later criminal proceeding takes place. These are the premises of this separate opinion</p>
      </div>
      <div class="footnote">
        <a class="footnote">*</a>
        <p class="indent"> The<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning, as is now well settled, is a constitutional requirement adopted to reduce the risk of a coerced confession and to implement the Self-Incrimination Clause. <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 444</a></span> (2000); <i>Miranda</i> v. <i>Arizona, supra,</i> at 467. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> mandates a rule of exclusion. It must be so characterized, for it has significant exceptions that can only be assessed and determined in the course of trial. Unwarned custodial interrogation does not in every instance violate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> See, <i>e. g., New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984) (statement admissible if questioning was immediately necessary for public safety). Furthermore, statements secured in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are admissible in some instances. See, <i>e. g., Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971) (statement admissible for purposes of impeachment). The identification of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation and its consequences, then, ought to be determined at trial. The exclusion of unwarned statements, when not within an exception, is a complete and sufficient remedy.</p>
        <p>II</p>
        <p class="indent">JUSTICE SOUTER and JUSTICE THOMAS are wrong, in my view, to maintain that in all instances a violation of the Self-Incrimination Clause simply does not occur unless and until a statement is introduced at trial, no matter how severe the pain or how direct and commanding the official compulsion used to extract it.</p>
        <p class="indent">It must be remembered that the Self-Incrimination Clause of the Fifth Amendment is applicable to the States in its full text through the Due Process Clause of the Fourteenth Amendment. <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#6" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 6</a></span> (1964); <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#615" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 615</a></span> (1965). The question is the proper interpretation of the Self-Incrimination Clause in the context of the present dispute.</p>
        <p class="indent">Our cases and our legal tradition establish that the Self-Incrimination Clause is a substantive constraint on the conduct of the government, not merely an evidentiary rule governing the work of the courts. The Clause must provide more than mere assurance that a compelled statement will not be introduced against its declarant in a criminal trial. Otherwise there will be too little protection against the compulsion the Clause prohibits. The Clause protects an individual from being forced to give answers demanded by an official in any context when the answers might give rise to criminal liability in the future. "It can be asserted in any proceeding, civil or criminal, administrative or judicial, investigatory or adjudicatory; and it protects against any disclosures that the witness reasonably believes could be used in a criminal prosecution or could lead to other evidence that might be so used." <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#444" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 444-445</a></span> (1972) (footnotes omitted). The decision in <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></i> described the Self-Incrimination Clause as an exemption from the testimonial duty. <i><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span></i> As the duty is immediate, so must be the privilege. Furthermore, the exercise of the privilege depends on what the witness reasonably believes will be the future use of a statement. <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#445" aria-description="Citation for case: Kastigar v. United States"><i>Id.,</i> at 445</a></span>. Again, this indicates the existence of a present right.</p>
        <p class="indent">The Clause provides both assurance that a person will not be compelled to testify against himself in a criminal proceeding and a continuing right against government conduct intended to bring about self-incrimination. <i>Lefkowitz</i> v. <i>Turley,</i> <span class="citation" data-id="108882"><a href="/opinion/108882/lefkowitz-v-turley/#77" aria-description="Citation for case: Lefkowitz v. Turley">414 U. S. 70, 77</a></span> (1973) ("The Amendment not only protects the individual against being involuntarily called as a witness against himself in a criminal prosecution but also privileges him not to answer official questions put to him in any other proceeding, civil or criminal, formal or informal, where the answers might incriminate him in future criminal proceedings"); accord, <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542-543</a></span> (1897); <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span> (1892). The principle extends to forbid policies which exert official compulsion that might induce a person into forfeiting his rights under the Clause. <i>Lefkowitz</i> v. <i>Cunningham,</i> <span class="citation" data-id="9426845"><a href="/opinion/109683/lefkowitz-v-cunningham/#806" aria-description="Citation for case: Lefkowitz v. Cunningham">431 U. S. 801, 806</a></span> (1977) ("These cases settle that government cannot penalize assertion of the constitutional privilege against compelled self-incrimination by imposing sanctions to compel testimony which has not been immunized"); accord, <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280</a></span> (1968); <i>Gardner</i> v. <i>Broderick,</i> <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#279" aria-description="Citation for case: Gardner v. Broderick">392 U. S. 273, 279</a></span> (1968). JUSTICE SOUTER and JUSTICE THOMAS acknowledge a future privilege. <i>Ante,</i> at 777-778; <i>ante,</i> at 769. That does not end the matter. A future privilege does not negate a present right.</p>
        <p class="indent">Their position finds some support in a single statement in <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990) ("Although conduct by law enforcement officials prior to trial may ultimately impair that right [against compelled self-incrimination], a constitutional violation occurs only at trial"). That case concerned the application of the Fourth Amendment, and the extent of the right secured under the Self-Incrimination Clause was not then before the Court. <i><span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/" aria-description="Citation for case: United States v. Verdugo-Urquidez">Ibid.</a></span></i> Furthermore, <i><span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/" aria-description="Citation for case: United States v. Verdugo-Urquidez">Verdugo-Urquidez</a></span></i> involved a prosecution in the United States arising from a criminal investigation in another country, <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#274" aria-description="Citation for case: United States v. Verdugo-Urquidez"><i>id.,</i> at 274-275</a></span>, so there was a special reason for the Court to be concerned about the application of the Clause in that context, <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#269" aria-description="Citation for case: United States v. Verdugo-Urquidez"><i>id.,</i> at 269</a></span> (noting the Court had "rejected the claim that aliens are entitled to Fifth Amendment rights outside the sovereign territory of the United States" (citing <i>Johnson</i> v. <i>Eisentrager,</i> <span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">339 U. S. 763</a></span> (1950))). In any event, the decision cannot be read to support the proposition that the application of the Clause is limited in the way JUSTICE SOUTER and JUSTICE THOMAS describe today.</p>
      </div>
      <div class="footnote">
        <a class="footnote">A</a>
        <p class="indent"> recent case illustrates that a violation of the Self-Incrimination Clause may have immediate consequences. Just last Term, nine Justices all proceeded from the premise that a present, completed violation of the Self-Incrimination Clause could occur if an incarcerated prisoner were required to admit to past crimes on pain of forfeiting certain privileges or being assigned harsher conditions of confinement<i>McKune</i> v. <i>Lile,</i> <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/" aria-description="Citation for case: McKune v. Lile">536 U. S. 24</a></span> (2002); <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#48" aria-description="Citation for case: McKune v. Lile"><i>id.,</i> at 48</a></span> (O'CONNOR, J., concurring in judgment); <span class="citation" data-id="9434264"><a href="/opinion/121146/mckune-v-lile/#54" aria-description="Citation for case: McKune v. Lile"><i>id.,</i> at 54</a></span> (STEVENS, J., dissenting). Although there was disagreement over whether a violation occurred in the circumstances of that case, there was no disagreement that a present violation could have taken place. No Member of the Court suggested that the absence of a pending criminal proceeding made the Self-Incrimination Clause inquiry irrelevant.</p>
        <p class="indent">This is not to say all questions as to the meaning and extent of the Clause are simple of resolution, or that all of the cited cases are easy to reconcile. Many questions about the application of the Self-Incrimination Clause are close and difficult. There are instances, moreover, when incriminating statements can be required from a reluctant witness, see, <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/#276" aria-description="Citation for case: Gardner v. Broderick"><i>e. g., Gardner, supra,</i> at 276</a></span>, and others where information may be required even absent a promise of immunity, see, <i>e. g., Shapiro</i> v. <i>United States,</i> <span class="citation" data-id="9420211"><a href="/opinion/104585/shapiro-v-united-states/#19" aria-description="Citation for case: Shapiro v. United States">335 U. S. 1, 19</a></span> (1948). JUSTICE SOUTER and JUSTICE THOMAS are correct to note that testimony may be ordered, on pain of contempt, if appropriate immunity is granted. It does not follow that the Clause establishes no present right. The immunity rule simply shows that the right is not absolute.</p>
        <p class="indent">The conclusion that the Self-Incrimination Clause is not violated until the government seeks to use a statement in some later criminal proceeding strips the Clause of an essential part of its force and meaning. This is no small matter. It should come as an unwelcome surprise to judges, attorneys, and the citizenry as a whole that if a legislative committee or a judge in a civil case demands incriminating testimony without offering immunity, and even imposes sanctions for failure to comply, that the witness and counsel cannot insist the right against compelled self-incrimination is applicable then and there. JUSTICE SOUTER and JUSTICE THOMAS, I submit, should be more respectful of the understanding that has prevailed for generations now. To tell our whole legal system that when conducting a criminal investigation police officials can use severe compulsion or even torture with no present violation of the right against compelled self-incrimination can only diminish a celebrated provision in the Bill of Rights. A Constitution survives over time because the people share a common, historic commitment to certain simple but fundamental principles which preserve their freedom. Today's decision undermines one of those respected precepts.</p>
        <p class="indent">Dean Griswold explained the place the Self-Incrimination Clause has secured in our legal heritage:</p>
        <p class="indent">"The Fifth Amendment has been very nearly a lone sure rock in a time of storm. It has been one thing which has held quite firm, although something like a juggernaut has pushed upon it. It has, thus, through all its vicissitudes, been a symbol of the ultimate moral sense of the community, upholding the best in us, when otherwise there was a good deal of wavering under the pressures of the times." E. Griswold, The Fifth Amendment Today 73 (1955).</p>
        <p class="indent">It damages the law, and the vocabulary with which we impart our legal tradition from one generation to the next, to downgrade our understanding of what the Fifth Amendment requires.</p>
        <p class="indent">There is some authority, it must be acknowledged, for the proposition that the act of torturing to obtain a confession is not comprehended within the Self-Incrimination Clause itself. In <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), the Court held that convictions based upon tortured confessions could not stand, but it identified the Due Process Clause, and not the Self-Incrimination Clause, as the source for its ruling. <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi"><i>Id.,</i> at 285</a></span>. The Court interpreted the Self-Incrimination Clause as limited to "the processes of justice by which the accused may be called as a witness and required to testify. Compulsion by torture to extort a confession is a different matter." <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Ibid.</a></span></i> The decision in <i>Brown</i> antedated the incorporation of the Clause and the ensuing understanding of its fundamental role in our legal system.</p>
        <p class="indent">The views expressed by JUSTICE SOUTER and JUSTICE THOMAS also have some academic support. Professor McNaughton, in his revision of Professor Wigmore's treatise on the law of evidence, recites various rationales for the Self-Incrimination Clause, declaring all of them insufficient. 8 J. Wigmore, Evidence &#167; 2251 (J. McNaughton rev. ed. 1961). The 11th justification he discusses is the prevention of torture, <i>id.,</i> at 315, a practice Professor McNaughton simply assures us will not be revived, <i>ibid.</i></p>
        <p class="indent">This is not convincing. The Constitution is based upon the theory that when past abuses are forbidden the resulting right has present meaning. A police officer's interrogation is different in a formal sense from interrogation ordered by an official inquest, but the close relation between the two ought not to be so quickly discounted. Even if some think the abuses of the Star Chamber cannot revive, the specter of Sheriff Screws, see <i>Screws</i> v. <i>United States,</i> <span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U. S. 91</a></span> (1945), or of the deputies who beat the confessions out of the defendants in <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi</a></span>,</i> is not so easily banished. See <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#312" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 312, n. 3</a></span> (1985); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#371" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 371-372, n. 19

[...TRUNCATED 18337 of 138337 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Chiaverini v. City of Napoleon.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Chiaverini v. City of Napoleon
type: case
citation: "602 U.S. 556 (2024)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2024
date_decided: ""
docket: 23-50
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
  opinion_url: "https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/"
  cluster_id: 10600074
  opinion_id: 11066663
  identity_checked: true
lake:
  record_id: Chiaverini v. City of Napoleon
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Key
related:
  - "[[Thompson v. Clark]]"
  - "[[Heck v. Humphrey]]"
  - "[[Malicious Prosecution under the Fourth Amendment]]"
tags:
  - case
  - fourth-amendment
  - malicious-prosecution
  - section-1983
  - probable-cause
holding: "The presence of probable cause for one charge does not categorically defeat a Fourth Amendment malicious-prosecution claim under §1983 challenging a separate, baseless charge; courts evaluate each charge on its own."
---

# Chiaverini v. City of Napoleon

*602 U.S. 556 (2024)* (No. 23-50) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10600074 → opinion 11066663; quotes string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Jascha Chiaverini, who ran a jewelry store in Napoleon, Ohio, was charged by local police with three offenses arising from his purchase of a ring: two misdemeanors (receiving stolen property and dealing in precious metals without a license) and a felony count of money laundering. The officers obtained an arrest warrant and Chiaverini was detained for three days; the charges were later dismissed after the county prosecutors failed to present the case to a grand jury in time. He sued the officers under 42 U.S.C. § 1983, alleging a Fourth Amendment malicious-prosecution claim and contending that the felony money-laundering charge lacked probable cause. The District Court granted the officers summary judgment, and the Sixth Circuit affirmed on the ground that probable cause supporting the two misdemeanor charges defeated the malicious-prosecution claim as to any charge.

## Issue
Whether the presence of probable cause for one charge in a criminal proceeding categorically defeats a Fourth Amendment malicious-prosecution claim under § 1983 that is based on a separate charge lacking probable cause.

## Rule
A Fourth Amendment malicious-prosecution claim under § 1983 — the claim recognized in *[[Thompson v. Clark]]* — requires a plaintiff to show that an official brought a charge without probable cause that caused an unreasonable seizure of his person. The existence of probable cause for one charge does not categorically defeat that claim as to another, baseless charge. Drawing on both Fourth Amendment law (an invalid charge that starts or prolongs a detention is an unreasonable seizure even when a valid charge is also brought) and the common-law malicious-prosecution tort as it stood in 1871 (which assessed probable cause charge by charge), the Court held that "[c]onsistent with both the Fourth Amendment and traditional common-law practice, courts should evaluate suits like Chiaverini's charge by charge." — 602 U.S. at 562. ^pin-562

## Application
The Sixth Circuit's categorical rule — that a single valid charge insulates officers from a malicious-prosecution claim based on any other charge, however baseless — drew support from neither half of the claim's name, and even the defendant officers and the United States agreed it was wrong. The Court did not, however, resolve the separate **causation** element: whether the assertedly invalid felony charge actually caused Chiaverini's three-day detention given the concededly valid misdemeanor charges. Because the parties advanced competing causation tests (a taint theory, a but-for test, and a stricter "could-have-authorized" test) that the court below had not addressed, the Court left that question for the Sixth Circuit [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment of the Court of Appeals was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for further proceedings on the causation question. Kagan, J., delivered the opinion of the Court; Thomas, J., joined by Alito, J., dissented, adhering to the view that a malicious-prosecution claim cannot be based on the Fourth Amendment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. The decision [[Reading and Citing Cases#vacated|vacated]] the Sixth Circuit's judgment and [[Reading and Citing Cases#on-remand|remanded]]; the Fourth Amendment causation standard for multi-charge malicious-prosecution claims remains open in the lower courts.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Key*

## Sources
- [*Chiaverini v. City of Napoleon*, 602 U.S. 556 (2024)](https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/) — pinpoint: 562 (charge-by-charge holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.
- [*Thompson v. Clark*, 596 U.S. 36 (2022)](https://www.courtlistener.com/opinion/6457347/thompson-v-clark/) — the Fourth Amendment malicious-prosecution claim on which *Chiaverini* builds.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2548d2122c26648d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Chiaverini v. City of Napoleon"}, "payload": {"all": [{"cite": "602 U.S. 556", "page": "556", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "602"}], "display": "602 U.S. 556", "official": {"cite": "602 U.S. 556", "page": "556", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "602"}, "official_selection_present": true, "record_id": "Chiaverini v. City of Napoleon"}}
{"assertion_id": "c28c336f330a6402", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Chiaverini v. City of Napoleon"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Chiaverini v. City of Napoleon", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Chiaverini v. City of Napoleon

```json
{
  "schema_version": "s2.v1",
  "record_id": "Chiaverini v. City of Napoleon",
  "status": "under_review",
  "identity": {
    "case_name": "Chiaverini v. City of Napoleon",
    "case_name_short": "Chiaverini",
    "case_name_full": "",
    "input_case_name": "Chiaverini v. City of Napoleon",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "23-50",
    "cluster_id": 10600074,
    "lead_opinion_id": 11066663,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600074/chiaverini-v-city-of-napoleon/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "602 U.S. 556",
      "volume": "602",
      "reporter": "U.S.",
      "page": "556",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "602 U.S. 556",
        "volume": "602",
        "reporter": "U.S.",
        "page": "556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "602 U.S. 556",
    "official_selection": {
      "court_class": "scotus",
      "selected": "602 U.S. 556",
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
    "date_created": "2026-07-06T12:12:08Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "chiaverini-v-city-of-napoleon--10600074",
      "to_record_id": "Chiaverini v. City of Napoleon",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Chiaverini v. City of Napoleon

```
                   PRELIMINARY PRINT

             Volume 602 U. S. Part 1
                             Pages 556–571




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                               June 20, 2024


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
556                      OCTOBER TERM, 2023

                                  Syllabus


CHIAVERINI et al. v. CITY OF NAPOLEON, OHIO,
                     et al.
certiorari to the united states court of appeals for
                  the sixth circuit
       No. 23–50. Argued April 15, 2024—Decided June 20, 2024
This case involves a dispute between petitioner Jascha Chiaverini and po-
  lice offcers from Napoleon, Ohio. The offcers charged Chiaverini, a
  jewelry store owner, with three crimes: receiving stolen property, a mis-
  demeanor; dealing in precious metals without a license, also a misde-
  meanor; and money laundering, a felony. After obtaining a warrant,
  the police arrested Chiaverini and detained him for three days. But
  county prosecutors later dropped the case. Chiaverini, believing that
  his arrest and detention were unjustifed, then sued the offcers, alleging
  what is known as a Fourth Amendment malicious-prosecution claim
  under 42 U. S. C. § 1983. To prevail on this claim, he had to show that
  the offcers brought criminal charges against him without probable
  cause, leading to an unreasonable seizure of his person. The District
Page Proof Pending Publication
  Court, however, granted summary judgment to the offcers, and the
  Court of Appeals for the Sixth Circuit affrmed. The Court of Appeals
  held that Chiaverini's prosecution was supported by probable cause. In
  holding this, the court did not address whether the offcers had prob-
  able cause to bring the money-laundering charge. In its view, there
  was clearly probable cause to charge Chiaverini with the two misde-
  meanors. And so long as one charge was supported by probable cause,
  it thought, a malicious-prosecution claim based on any other charge
  must fail.
Held: The presence of probable cause for one charge in a criminal pro-
 ceeding does not categorically defeat a Fourth Amendment malicious-
 prosecution claim relating to another, baseless charge. The parties, and
 the United States as amicus curiae, all agree with this conclusion,
 which follows from both the Fourth Amendment and traditional
 common-law practice.
    Under the Fourth Amendment, a pretrial detention counts as an un-
 reasonable seizure, and so is illegal, unless it is based on probable cause.
 See Manuel v. Joliet, 580 U. S. 357, 364–369. Even when a detention
 is justifed at the outset, moreover, it may become unreasonably pro-
 longed if the reason for it lapses. Rodriguez v. United States, 575 U. S.
 348, 354–357. So if an invalid charge causes a detention to start or
 continue, then the Fourth Amendment is violated. Bringing the invalid
 charge alongside a valid one does not categorically preclude this possi-
                      Cite as: 602 U. S. 556 (2024)                   557

                                Syllabus

  bility. As the starkest possible example, consider a person detained on
  a drug offense supported by probable cause and a gun offense that is
  not. If the prosecutor drops the (valid) drug charge, leaving the person
  in jail on the (invalid) gun charge alone, then the baseless charge has
  caused a constitutional violation by unreasonably extending the deten-
  tion. The person should not be categorically barred from bringing a
  Fourth Amendment malicious-prosecution claim just because the base-
  less charge was brought along with a good one.
     The same conclusion follows from the common-law principles govern-
  ing malicious-prosecution suits. This Court has analogized claims like
  Chiaverini's to the common-law tort of malicious prosecution, and has
  explained that the tort can inform courts' understanding of this type of
  claim. Thompson v. Clark, 596 U. S. 36, 43–44. A plaintiff bringing a
  common-law malicious-prosecution suit had to show that an offcial initi-
  ated a charge without probable cause. But he did not have to show
  that every charge brought against him lacked an adequate basis. See,
  e. g., Barron v. Mason, 31 Vt. 189, 198 (it was no “defen[s]e that there
  was probable cause for part of the prosecution”).
     These uncontested points suffce to doom the Sixth Circuit's categori-
  cal rule barring a Fourth Amendment malicious-prosecution claim if any

Page Proof Pending Publication
  charge is valid. Of course, a Fourth Amendment malicious-prosecution
  suit depends not just on an unsupported charge, but on that charge's
  causing a seizure—like the arrest and three-day detention here. The
  parties and amicus curiae offer three different views of how that causa-
  tion element is met when a valid charge is also in the picture. But this
  issue is not properly before the Court, so the Sixth Circuit should ad-
  dress it on remand. Pp. 561–565.
Vacated and remanded.

   Kagan, J., delivered the opinion of the Court, in which Roberts, C. J.,
and Sotomayor, Kavanaugh, Barrett, and Jackson, JJ., joined.
Thomas, J., fled a dissenting opinion, in which Alito, J., joined, post,
p. 565. Gorsuch, J., fled a dissenting opinion, post, p. 569.

  Easha Anand argued the cause for petitioners. With her
on the briefs were Jeffrey L. Fisher, Pamela S. Karlan, Mi-
chael H. Stahl, and George C. Rogers.
  Vivek Suri argued the cause for the United States as ami-
cus curiae urging vacatur and remand. With him on the
brief were Solicitor General Prelogar, Assistant Attorney
General Clarke, Principal Deputy Assistant Attorney Gen-
558             CHIAVERINI v. CITY OF NAPOLEON

                          Opinion of the Court

eral Boynton, Deputy Solicitor General Gannon, Mark B.
Stern, Erin H. Flynn, and Brant S. Levine.
  Megan M. Wold argued the cause for respondents. With
her on the brief were Teresa L. Grigsby and Jennifer A.
McHugh.*

   Justice Kagan delivered the opinion of the Court.
  This case involves what is often called a Fourth Amend-
ment malicious-prosecution claim under 42 U. S. C. § 1983.
To succeed on such a claim, a plaintiff must show that a gov-
ernment offcial charged him without probable cause, leading
to an unreasonable seizure of his person. See Thompson v.
Clark, 596 U. S. 36, 43, and n. 2 (2022). The question pre-
sented here arises when the offcial brings multiple charges,
only one of which lacks probable cause. Do the valid
charges insulate the offcial from a Fourth Amendment
malicious-prosecution claim relating to the invalid charge?
Page         Proof Pending Publication
 *Briefs of amici curiae urging reversal were fled for the Cato Institute
by Steve Art and David B. Owens; for the Constitutional Accountability
Center by Elizabeth B. Wydra, Brianne J. Gorod, and Brian R. Frazelle;
for the Institute for Justice by Marie Miller, Anya Bidwell, and Patrick
Jaicomo; for the National Association of Criminal Defense Lawyers by
Zachary D. Tripp, Joshua M. Wesneski, and Jeffrey T. Green; and for the
National Police Accountability Project by Charles A. Rothfeld and Eugene
R. Fidell.
   Briefs of amici curiae urging affrmance were fled for the State of Iowa
et al. by Brenna Bird, Attorney General of Iowa, Eric Wessan, Solicitor
General, Patrick C. Valencia, Deputy Solicitor General, and Alexa Den
Herder, Assistant Solicitor General, and by the Attorneys General for
their respective States as follows: Steve Marshall of Alabama, Tim Griffn
of Arkansas, Ashley Moody of Florida, Christopher M. Carr of Georgia,
Raúl R. Labrador of Idaho, Todd Rokita of Indiana, Kris Kobach of Kan-
sas, Russell Coleman of Kentucky, Elizabeth B. Murrill of Louisiana,
Austin Knudsen of Montana, Michael T. Hilgers of Nebraska, Dave Yost
of Ohio, Gentner Drummond of Oklahoma, Alan Wilson of South Caro-
lina, Marty J. Jackley of South Dakota, Jonathan Skrmetti of Tennessee,
Ken Paxton of Texas, and Sean D. Reyes of Utah; and for the Local Gov-
ernment Legal Center et al. by Gregory G. Garre.
                   Cite as: 602 U. S. 556 (2024)             559

                      Opinion of the Court

The answer is no: The valid charges do not create a categori-
cal bar. We leave for another day the follow-on question of
how to determine in those circumstances whether the base-
less charge caused the requisite seizure.

                                I
   This dispute began with a set of peculiar interactions be-
tween a jewelry store owner and police offcers in Napoleon,
Ohio. See generally App. to Pet. for Cert. 2a–7a. The jew-
eler, Jascha Chiaverini, bought a ring for $45 from a (petty)
jewel thief. The ring's rightful owners found out about the
sale, and asked Chiaverini to return their property. Chiav-
erini said no, so the owners contacted the police. Two off-
cers, on a later visit to the store, directed Chiaverini to sur-
render the ring to its owners. But Chiaverini refused their
request too, saying that it contradicted a letter he had just
received from the police department telling him to retain the
Page Proof Pending Publication
ring as evidence. And when repeating his refusal to another
offcer the next day, Chiaverini suggested (for reasons un-
clear) that he was operating his store without a license. The
result of that (shall we say, unproftable) exchange was that
the police turned their attention from the original theft to
Chiaverini's business.
   Soon afterward, the offcers launched a criminal proceed-
ing against Chiaverini in municipal court. They fled three
complaints, each charging him with a separate offense. Two
were misdemeanors: receiving stolen property and dealing
in precious metals without a license. The third was a felony:
money laundering. To support their accompanying applica-
tion for an arrest warrant, the offcers submitted an affdavit
making the case for probable cause on all three charges, but
focusing on the felony. See App. 16–17. For that charge to
succeed, Chiaverini must have known when he bought the
ring that the transaction involved the proceeds of unlawful
activity. See Ohio Rev. Code Ann. § 1315.55(A)(1) (Lexis
2018). In support of that element, the offcers averred that
560          CHIAVERINI v. CITY OF NAPOLEON

                     Opinion of the Court

Chiaverini always suspected the ring was stolen. The judge
issued the requested warrant, and the offcers arrested Chi-
averini. He remained in custody for three days, until his
arraignment. At a later preliminary hearing, the judge
heard testimony about the evidence supporting the offcers'
probable-cause allegations. See App. to Pet. for Cert. 6a–
7a. The offcers maintained that Chiaverini had admitted in
their interview to suspecting the ring was stolen; Chiaverini
denied making any such statement. At the hearing's conclu-
sion, the judge again found probable cause, and set the three
charges for trial.
   The county prosecutors, though, decided that they had
higher priorities. They failed to present the case to a grand
jury in the required time. The court therefore dismissed
the charges.
   But Chiaverini decided not to let matters lie. After all,
he had been arrested and held for three days, he thought
Page Proof Pending Publication
unjustifably. So he sued the offcers under § 1983, alleging
what is known as a Fourth Amendment claim for malicious
prosecution. To prevail on that claim, he had to show
(among other things) that the offcers brought criminal
charges against him without probable cause. See Thomp-
son, 596 U. S., at 43–44. In addressing that issue, he gave
special attention to the felony charge for money laundering.
According to Chiaverini, the offcers lacked probable cause
for that charge for two reasons. First, they had no reason
to think he knew the ring was stolen; indeed, he said, their
claim that he had admitted as much was an out-and-out lie.
And second, they could not show—as, in his view, Ohio law
required—that the ring was worth more than $1,000; its
value was far less, more in line with its $45 purchase price.
So Chiaverini concluded that his suit satisfed the “without
probable cause” element of a Fourth Amendment malicious-
prosecution claim.
   After the District Court granted summary judgment to
the offcers, the Court of Appeals for the Sixth Circuit af-
                   Cite as: 602 U. S. 556 (2024)             561

                      Opinion of the Court

frmed. It did so without addressing either of Chiaverini's
arguments about the felony charge's basis. In the Sixth Cir-
cuit's view, there was clearly probable cause to support the
two misdemeanor charges the offcers had fled. See App.
to Pet. for Cert. 11a–16a. And because that was true, the
court thought, the validity of the felony charge did not mat-
ter. “So long as probable cause supports at least one charge
against Chiaverini (like his receipt-of-stolen-property viola-
tion),” then his malicious-prosecution claim “based on other
charges (like his money-laundering charge) also fail[s].” Id.,
at 10a. Or said another way, a single valid charge in a pro-
ceeding would insulate offcers from a Fourth Amendment
malicious-prosecution claim relating to any other charges, no
matter how baseless.
   In taking that position, the Sixth Circuit stepped out on
its own. Three other Courts of Appeals have held that the
presence of probable cause for one charge does not automati-
cally defeat a Fourth Amendment malicious-prosecution
Page Proof Pending Publication
claim alleging the absence of probable cause for another
charge. See Williams v. Aguirre, 965 F. 3d 1147, 1159–1162
(CA11 2020); Johnson v. Knorr, 477 F. 3d 75, 83–85 (CA3
2007); Posr v. Doherty, 944 F. 2d 91, 100 (CA2 1991).
   We granted certiorari to resolve that circuit split, 601
U. S. ––– (2023), and we now vacate the decision below.

                                II
   Section 1983 enables an individual to recover damages
from a state or local offcial for the deprivation of a constitu-
tional right. Such a suit is of course premised on a constitu-
tional violation. But its elements and rules may also be
shaped by common-law tort principles, against whose back-
drop § 1983 was enacted. See Manuel v. Joliet, 580 U. S.
357, 370 (2017). To determine the precise contours of a con-
stitutional claim under § 1983, we have held, a court should
identify the “most analogous” common-law tort to the consti-
tutional harm alleged. Ibid. And the court should incorpo-
562          CHIAVERINI v. CITY OF NAPOLEON

                      Opinion of the Court

rate that tort's requirements to the extent consistent with
“the values and purposes of the constitutional right at issue.”
Ibid.; Thompson, 596 U. S., at 43.
   The claim Chiaverini brought—a Fourth Amendment
malicious-prosecution claim—emerged from that method.
The constitutional violation alleged in such a suit is a type
of unreasonable seizure—an arrest and detention of a person
based on a criminal charge lacking probable cause. In
Thompson v. Clark, we analogized a suit alleging that
Fourth Amendment wrong to the common-law tort of mali-
cious prosecution. See id., at 43–44. The “gravamen” of
both, we reasoned, is “the wrongful initiation of charges
without probable cause” (though in the Fourth Amendment
context, those charges must cause a seizure as well). Id.,
at 43, and n. 2. Because of that similarity, the malicious-
prosecution tort can inform a court's understanding of the
kind of claim Chiaverini has brought.
Page Proof Pending Publication
   The question here is whether a Fourth Amendment
malicious-prosecution claim may succeed when a baseless
charge is accompanied by a valid charge. The Court of Ap-
peals, as described above, answered that question with a cat-
egorical no: Even if the felony count lacked probable cause,
the Sixth Circuit held, Chiaverini could not recover because
the misdemeanor counts were adequately supported. See
supra, at 560–561. But a funny thing happened on the way
to this Court. The offcers now agree with Chiaverini that
there is no such fat bar. See Brief for Offcers 24–27; Brief
for Chiaverini 2–3. And the United States as amicus cu-
riae also argues that the Sixth Circuit rule is wrong. See
Brief for United States 10. We agree with them all. Con-
sistent with both the Fourth Amendment and traditional
common-law practice, courts should evaluate suits like Chi-
averini's charge by charge.
   Consider frst how that result follows from established
Fourth Amendment law. Under that Amendment, a pretrial
detention (like the one Chiaverini suffered) must be based
                   Cite as: 602 U. S. 556 (2024)           563

                      Opinion of the Court

on probable cause. See Manuel, 580 U. S., at 364–369.
Otherwise, such a detention counts as an unreasonable sei-
zure. And even when a detention is justifed at the outset,
it may become unreasonably prolonged if the reason for it
lapses. See Rodriguez v. United States, 575 U. S. 348, 354–
357 (2015). So if an invalid charge—say, one fabricated by
police offcers—causes a detention either to start or to con-
tinue, then the Fourth Amendment is violated. And that is
so even when a valid charge has also been brought (although,
as soon noted, that charge may well complicate the causation
issue, see infra, at 564–565). Take the starkest possible ex-
ample. A person is detained on two charges—a drug offense
supported by probable cause and a gun offense built on lies.
The prosecutor, for whatever reason, drops the (valid) drug
charge, leaving the person in jail on the (invalid) gun charge
alone. The inclusion of the baseless charge—though
brought along with a good charge—has thus caused a consti-
Page Proof Pending Publication
tutional violation, by unreasonably extending the pretrial
detention. Even the Napoleon offcers agree, offering a sim-
ilar example. See Brief for Offcers 25; see also Brief for
United States 17–18. So the bringing of one valid charge in
a criminal proceeding should not categorically preclude a
claim based on the Fourth Amendment.
   And the same conclusion follows from the common-law
principles governing malicious-prosecution suits when § 1983
was enacted. As noted above, a plaintiff in such a suit had
to show that an offcial initiated a charge without probable
cause. See Thompson, 596 U. S., at 44; supra, at 562. He
did not have to show, however, that every charge brought
against him lacked an adequate basis. Rather, courts in
that era assessed probable cause charge by charge. “[I]f
groundless charges” are “coupled with others which are well
founded,” explained one State Supreme Court, the ground-
less ones could still “constitute a valid cause of action.”
Boogher v. Bryant, 86 Mo. 42, 49 (1885). Another agreed: It
was no “defen[s]e that there was probable cause for part of
564          CHIAVERINI v. CITY OF NAPOLEON

                      Opinion of the Court

the prosecution.” Barron v. Mason, 31 Vt. 189, 198 (1858).
Or as a leading treatise from the era summarized the rule:
“It is not necessary that the whole proceedings be utterly
groundless.” 2 S. Greenleaf, Law of Evidence 400 (10th ed.
1868); see 1 F. Hilliard, Law of Torts or Private Wrongs
§ 1, p. 435, n. (b) (4th ed. 1874). One bad charge, even if
joined with good ones, was enough to satisfy the malicious-
prosecution tort's “without probable cause” element.
   All that dooms the Sixth Circuit's categorical rule barring
a Fourth Amendment malicious-prosecution claim if any
charge is valid. That rule receives support from neither
half of the claim's name—neither from the Fourth Amend-
ment nor from the malicious-prosecution tort we have in-
voked as an analogy. And the question is not close, as
shown by the parties' decision not to contest it in this Court.
   The parties, almost needless to say, have found a sub-
stitute ground of disagreement, involving the element of cau-
Page Proof Pending Publication
sation. As noted earlier, a Fourth Amendment malicious-
prosecution suit depends not just on an unsupported charge,
but on that charge's causing a seizure—like the arrest and
three-day detention here. See supra, at 562. The parties
and amicus curiae offer three different views of how that
causation element is met when a valid charge is also in the
picture. Chiaverini's test is the easiest to satisfy. On his
view, when both valid and invalid charges are brought before
a judge for a probable cause determination, the warrant the
judge issues is irretrievably tainted; so any detention de-
pending on that warrant is the result of the invalid charge.
See Reply Brief 10–11 (citing Williams, 965 F. 3d, at 1165);
Tr. of Oral Arg. 5–6, 26–28. The United States disagrees,
arguing for the use of a but-for test to discover whether the
invalid charge, apart from the valid ones, caused a detention.
See id., at 41–43. The question then would be whether the
judge “in fact [would] have authorized” the detention had
the invalid charge not been present. Id., at 43. And fnally,
the offcers urge a still stricter test. In their view, the ques-
                  Cite as: 602 U. S. 556 (2024)           565

                     Thomas, J., dissenting

tion is whether the judge, absent the invalid charge, could
have legally authorized the detention—regardless of what he
really would have done. See Brief for Offcers 20–21.
   But that new dispute is not now ft for our resolution.
The test for fnding causation is no part of the question we
agreed to review. For that reason, it was not fully briefed.
And most important, the court below did not address the
matter, nor have many others. “[W]e are a court of review,
not of frst view.” Cutter v. Wilkinson, 544 U. S. 709, 718,
n. 7 (2005). So we leave the causation question in the hands
of the Sixth Circuit, as it further considers Chiaverini's
Fourth Amendment malicious-prosecution claim.
   We accordingly vacate the judgment of the Court of Ap-
peals and remand the case for further proceedings consistent
with this opinion.
                                            It is so ordered.

  Justice Thomas, with whom Justice Alito joins,
Page
dissenting. Proof Pending Publication
   Jascha Chiaverini sued several city offcials for damages
under 42 U. S. C. § 1983. He alleged that they violated his
Fourth Amendment rights by subjecting him to a mali-
cious prosecution. I continue to adhere to my belief that a
“malicious prosecution claim cannot be based on the Fourth
Amendment.” Manuel v. Joliet, 580 U. S. 357, 378 (2017)
(Alito, J., joined by Thomas, J., dissenting). Accordingly, I
would affrm the dismissal of Chiaverini's claim.
   To raise a successful claim under § 1983, a plaintiff must
allege the deprivation of “rights, privileges, or immunities
secured” to him by the Constitution. 42 U. S. C. § 1983.
“In order to fesh out the elements of th[e alleged] constitu-
tional tort,” the Court generally analogizes to common-law
torts. Manuel, 580 U. S., at 378 (opinion of Alito, J.); see
also Heck v. Humphrey, 512 U. S. 477, 483–484 (1994). In
this case, Chiaverini claims that he was seized without prob-
able cause in violation of the Fourth Amendment. Chiaver-
566           CHIAVERINI v. CITY OF NAPOLEON

                       Thomas, J., dissenting

ini principally relies on this Court's decision in Thompson v.
Clark, 596 U. S. 36 (2022), to argue that the appropriate tort
analog for this claim is malicious prosecution. In Thomp-
son, the Court held that malicious prosecution, a tort ad-
dressing “the wrongful initiation of charges without proba-
ble cause,” is most analogous to a Fourth Amendment
unreasonable-seizure claim. Id., at 43.
   Thompson was wrongly decided. A malicious-prosecution
claim bears little resemblance to an unreasonable seizure
under the Fourth Amendment. Consider what is required
to establish a claim of malicious prosecution. A plaintiff
must show that “(i) the suit or proceeding was `instituted
without any probable cause'; (ii) the `motive in instituting'
the suit `was malicious,' . . . ; and (iii) the prosecution `termi-
nated in the acquittal or discharge of the accused.' ” Id.,
at 44 (quoting T. Cooley, Law of Torts 181 (1880)). These
elements have no overlap with what is required to establish
Page Proof Pending Publication
a Fourth Amendment seizure violation.
   First, an unreasonable seizure can occur without any
prosecution—for instance, if a person “is arrested without
probable cause” and “released before any charges are fled.”
596 U. S., at 51–52 (Alito, J., dissenting). Second, an unrea-
sonable seizure does not depend on the seizing offcial's mo-
tives. “[W]hile subjective bad faith, i.e., malice, is the core
element of a malicious prosecution claim, it is frmly estab-
lished that the Fourth Amendment standard of reasonable-
ness is fundamentally objective.” Manuel, 580 U. S., at 379
(opinion of Alito, J.). Thus, “[i]f a law enforcement offcer
makes an arrest without probable cause, the arrest is unrea-
sonable and therefore unconstitutional even if the offcer har-
bors no ill will for the arrestee. Likewise, if an offcer
makes an arrest with probable cause, there is no Fourth
Amendment violation regardless of the `actual motivations
of the individual offcers involved.' ” Thompson, 596 U. S.,
at 52 (opinion of Alito, J.) (quoting Whren v. United States,
517 U. S. 806, 813 (1996)). Third, an unreasonable seizure
                   Cite as: 602 U. S. 556 (2024)           567

                     Thomas, J., dissenting

violates the Constitution regardless of how any subsequent
prosecution is resolved. See Manuel, 580 U. S., at 379 (opin-
ion of Alito, J.).
   Nor is an unreasonable seizure necessary to prove a
malicious-prosecution claim. A malicious prosecution can
occur without any seizure at all. For example, “[t]here are
cases in which defendants charged with nonviolent crimes
agree to appear for arraignment and are then released pend-
ing trial on their own recognizance. These defendants . . .
may bring a common-law suit for malicious prosecution . . . ,
but they are not seized.” Thompson, 596 U. S., at 52–53.
And, “since a malicious-prosecution claim does not require a
seizure, it obviously does not require proof that the per-
son bringing suit was seized without probable cause.” Id.,
at 53.
   Malicious prosecution is therefore not an appropriate tort
analog for a § 1983 claim alleging a seizure in violation of
Page Proof Pending Publication
the Fourth Amendment. The Court has never provided a
fulsome explanation for why it has concluded otherwise.
When the Court frst recognized a malicious-prosecution
claim under the Fourth Amendment in Thompson, it essen-
tially adopted the holdings of certain lower courts. Id., at
43. The Court offered two meager sentences to justify
doing so. It reasoned that “the gravamen of the Fourth
Amendment claim for malicious prosecution . . . is the wrong-
ful initiation of charges without probable cause. And the
wrongful initiation of charges without probable cause is like-
wise the gravamen of the tort of malicious prosecution.”
Ibid. That is incorrect. A malicious-prosecution claim pro-
tects against the malicious initiation of charges, but the
Fourth Amendment protects against unreasonable searches
and seizures—it does not matter whether the offcial acted
with malice or charges are ever initiated. See id., at 54–
55 (opinion of Alito, J.). Today, the Court rests solely on
Thompson's mistaken reasoning to conclude that Chiaverini
can raise his claim. See ante, at 562.
568             CHIAVERINI v. CITY OF NAPOLEON

                          Thomas, J., dissenting

   The Court's decision to forge ahead with combining the
malicious-prosecution and Fourth Amendment frameworks
will inevitably create confusion. As I have explained, an un-
reasonable seizure under the Fourth Amendment requires a
seizure; a malicious-prosecution claim does not. Supra, at
566. To resolve this mismatch, the Court has decided that
a plaintiff must show that a malicious prosecution caused an
unreasonable seizure. See Thompson, 596 U. S., at 43, n. 2;
ante, at 558, 564. While that grafting solved one problem,
it created several more. Because the Court has mixed two
distinct legal frameworks, it is unclear what doctrines actu-
ally govern its requirement that a malicious prosecution
cause a seizure. For example, if a plaintiff has multiple
charges, how does a court determine whether a particular
unfounded charge caused the seizure? See ante, at 564–565
(listing three possible causation theories). What type of ev-
idence is relevant? See Brief for Petitioners 40 (arguing
Page Proof Pending Publication
that Chiaverini would not have been seized absent the un-
founded charge since a similar defendant with a credible
charge was not seized). And, what happens if an unfounded
charge merely changes the nature of the seizure? See Brief
for United States as Amicus Curiae 18 (arguing that an un-
founded charge causes a seizure if it results in a more force-
ful arrest). The Court's claim for malicious prosecution
under the Fourth Amendment requires resolving these ques-
tions and more. To date, the Court has offered little guid-
ance on how to do so.* And, because the claim at issue is
the Court's own creation, lower courts cannot turn to the

   *The Court purports to offer some guidance today by rejecting the
Sixth Circuit's “categorical rule barring a Fourth Amendment malicious-
prosecution claim if any charge is valid.” Ante, at 564. But, it is not
clear that the Sixth Circuit even has such a rule. See Howse v. Hodous,
953 F. 3d 402, 409, n. 3 (2020) (recognizing that the underlying inquiry is
whether an unfounded charge “change[s] the nature of the seizure”); see
2023 WL 152477, *4 (Jan. 11, 2023) (citing Howse). It is thus unclear what,
if any, doctrinal progress today's decision makes.
                    Cite as: 602 U. S. 556 (2024)             569

                      Gorsuch, J., dissenting

common law or Fourth Amendment doctrine for answers.
Instead, they are left to make their best guess at how the
Court would defne its novel claim.
  I would take a far simpler course. Instead of forcing a
square peg into a round hole by judging an unreasonable
seizure based on the malicious-prosecution tort, I would
“hold that a malicious-prosecution claim may not be brought
under the Fourth Amendment.” Thompson, 596 U. S., at 60
(opinion of Alito, J.). I respectfully dissent.

  Justice Gorsuch, dissenting.
  Section 1983 performs vital work by permitting individu-
als to vindicate their constitutional rights in federal court.
But it does not authorize this Court to expound new rights
of its own creation. As this Court has put it, § 1983 does
not turn the Constitution into a “ ` “font of tort law.” ' ” Al-
bright v. Oliver, 510 U. S. 266, 284 (1994) (Kennedy, J., con-
Page Proof Pending Publication
curring in judgment) (quoting Parratt v. Taylor, 451 U. S.
527, 544 (1981)).
  Despite that settled rule, the Court today doubles down
on a new tort of its own recent invention—what it calls a
“Fourth Amendment malicious-prosecution” cause of action.
Ante, at 558; see Thompson v. Clark, 596 U. S. 36, 43–44
(2022). Respectfully, it is hard to know where this tort
comes from. Stare for as long as you like at the Fourth
Amendment and you won't see anything about prosecutions,
malicious or otherwise. Instead, the Amendment provides
that “[t]he right of the people to be secure . . . against unrea-
sonable searches and seizures, shall not be violated.”
  As its language suggests, the Fourth Amendment supplies
nothing like a common-law claim for malicious prosecution.
Ante, at 566 (Thomas, J., dissenting); see Cordova v. Albu-
querque, 816 F. 3d 645, 662–663 (CA10 2016) (Gorsuch, J.,
concurring in judgment). Just consider some of the differ-
ences. This Court has long held that the touchstone of the
Fourth Amendment is objective reasonableness. But a
570          CHIAVERINI v. CITY OF NAPOLEON

                     Gorsuch, J., dissenting

common-law malicious-prosecution claim focuses on the
defendant's subjective intent. Ante, at 566 (opinion of
Thomas, J.). The Fourth Amendment addresses the per-
missibility of a seizure. But a common-law malicious-
prosecution claim can (and usually does) proceed without
one. Ante, at 567. A seizure in violation of the Fourth
Amendment can (and often does) take place without the initi-
ation of any judicial process. But the whole point of a
malicious-prosecution claim is to contest the appropriateness
of past judicial proceedings. Ante, at 566. For all these
reasons, it's “pretty hard to see how you might squeeze any-
thing that looks quite like the common law tort of malicious
prosecution into the Fourth Amendment.” Cordova, 816
F. 3d, at 663 (opinion of Gorsuch, J.).
   That is not to say no constitutional hook exists for a § 1983
claim addressing the malicious use of process. Rather, it
seems to me only that such a claim would be more properly
Page Proof Pending Publication
housed in the Fourteenth Amendment. See Albright, 510
U. S., at 283 (opinion of Kennedy, J.). After all, unlike the
Fourth Amendment, that provision does focus on judicial
proceedings, guaranteeing those who come before our courts
“due process” of law. See ibid.; Thompson, 596 U. S., at 43,
n. 2; Cordova, 816 F. 3d, at 662 (opinion of Gorsuch, J.). In-
hering in due process is a promise that courts will respect,
at the least, those “customary procedures to which freemen
were entitled by the old law of England.” Sessions v. Di-
maya, 584 U. S. 148, 176 (2018) (Gorsuch, J., concurring in
part and concurring in judgment) (internal quotation marks
omitted). And the common law has long recognized a tort
of malicious prosecution to protect against the abuse of judi-
cial proceedings. Albright, 510 U. S., at 283 (opinion of
Kennedy, J.).
   Admittedly, a procedural due process claim for malicious
prosecution may come with its own set of limitations. After
all, when a State provides exactly the tort claim the plaintiff
seeks, it provides him with all the process he is due. See
                    Cite as: 602 U. S. 556 (2024)             571

                      Gorsuch, J., dissenting

id., at 284; Cordova, 816 F. 3d, at 662 (opinion of Gorsuch, J.).
And, consistent with the common law, many States recognize
claims for malicious prosecution. Indeed, the relevant State
here (Ohio) permits such a cause of action. Notably, too,
unlike the tort this Court seeks to cobble together under the
aegis of the Fourth Amendment, Ohio's tort does not require
a plaintiff to prove that he was seized. Compare Trussell
v. General Motors Corp., 53 Ohio St. 3d 142, 145–146, 559
N. E. 2d 732, 735–736 (1990), with ante, at 558 (majority opin-
ion). Of course, should a State fail to provide a malicious-
prosecution claim to secure his procedural due process
rights, or a fair forum for entertaining such a claim, a federal
court may need to act to vindicate § 1983 and the promise of
procedural due process. Cordova, 816 F. 3d, at 665 (opinion
of Gorsuch, J.). But in many cases (this one included), a
State malicious-prosecution claim may be both easier for a
plaintiff to prove than anything the Court today provides
and suffcient to ensure any process he is due. Albright, 510
Page Proof Pending Publication
U. S., at 285–286 (opinion of Kennedy, J.); Cordova, 816 F. 3d,
at 662 (opinion of Gorsuch, J.).
   For these reasons, I respectfully dissent.
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 557, line 3: “gun” is replaced with “(valid) drug”
p. 557, line 4: “drug” is replaced with “(invalid) gun”

```

---
