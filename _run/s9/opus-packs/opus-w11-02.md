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

## GROUP: _overhaul2/lake/cases/Silverman v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Silverman v. United States"
type: case
citation: "365 U.S. 505 (1961)"
parallel_cite: "81 S. Ct. 679; 5 L. Ed. 2d 734; 97 A.L.R. 2d 1277"
neutral_cite: 1961 U.S. LEXIS 1605
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-03-06
docket: 66
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-03-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Silverman v. United States
  varies_by_point: false
  scope_note: "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106187/silverman-v-united-states/"
  cluster_id: 106187
  opinion_id: 106187
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Key — Progeny / Refinement"
related: ["[[Katz v. United States]]", "[[United States v. Jones]]", "[[Olmstead v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "trespass", "electronic-surveillance"]
holding: "A 'spike mike' physically penetrating the wall into the house was a search — an unauthorized physical intrusion into a constitutionally protected area, not measured by 'technical trespass' niceties."
lake:
  record_id: Silverman v. United States
  status: verified
  projected_at: 2026-07-09
---

# Silverman v. United States

*365 U.S. 505 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
To overhear conversations of Silverman and others suspected of a gambling operation, police drove a "spike mike" through a party wall until it contacted a heating duct, turning the home's duct system into a giant microphone. The overheard conversations were used against the petitioners at trial.

## Issue
Whether using a spike mike that physically penetrates a wall to listen to conversations inside a home is a Fourth Amendment search.

## Rule
A physical intrusion into the home to eavesdrop is a search. "[T]he eavesdropping was accomplished by means of an unauthorized physical penetration into the premises occupied by the petitioners." — 365 U.S. at 509. ^pin-509

The Court distinguished its earlier electronic-surveillance decisions because there the eavesdropping "had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area." — [*Id.* at 510](https://www.courtlistener.com/opinion/106187/silverman-v-united-states/#:~:text=had%20not%20been%20accomplished%20by). ^pin-510

And the result did not depend on property-law technicalities: "In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law .... Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law." — *Id.* at 511. ^pin-511

## Application
The officers heard the petitioners' conversations only by usurping part of the home's heating system—a physical intrusion into the house itself—so the surveillance was a search regardless of whether it amounted to a technical trespass. The evidence should have been suppressed, and the convictions were reversed.

## Conclusion
The spike-mike intrusion into the home was an unconstitutional search; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Silverman*'s actual-intrusion holding predates [[Katz v. United States]], which supplemented it with the reasonable-expectation-of-privacy test; the property-based trespass approach *Silverman* exemplifies was reaffirmed as an independent test in [[United States v. Jones]], and it marks the boundary of the wiretap rule of [[Olmstead v. United States]].

## Appears on
- [[Trespass]] — *Key — Progeny / Refinement*

## Sources
- *Silverman v. United States*, 365 U.S. 505 (1961) — https://www.courtlistener.com/opinion/106187/silverman-v-united-states/ — pinpoints: 509, 510, 511.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ebe8460de76aadaa", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Silverman v. United States"}, "payload": {"all": [{"cite": "365 U.S. 505", "page": "505", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "365"}, {"cite": "81 S. Ct. 679", "page": "679", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "5 L. Ed. 2d 734", "page": "734", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "5"}, {"cite": "1961 U.S. LEXIS 1605", "page": "1605", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1961"}, {"cite": "97 A.L.R. 2d 1277", "page": "1277", "reporter": "A.L.R. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "97"}], "display": "365 U.S. 505", "official": {"cite": "365 U.S. 505", "page": "505", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "365"}, "official_selection_present": true, "record_id": "Silverman v. United States"}}
{"assertion_id": "0b585aeecfebe33d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-509", "record_id": "Silverman v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-509", "pinpoint_status": "slip-only", "quote": "through a party wall until it contacted a heating duct, turning the home's duct system into a giant microphone. The overheard conversations were used against the petitioners at trial. ## Issue Whether using a spike mike that physically penetrates a wall to listen to conversations inside a home is a Fourth Amendment search. ## Rule A physical intrusion into the home to eavesdrop is a search.", "quote_fidelity": "mismatch", "record_id": "Silverman v. United States", "star_marker": null}}
{"assertion_id": "28dbd39bc44c367d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-511", "record_id": "Silverman v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-511", "pinpoint_status": "slip-only", "quote": "In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law .... Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law.", "quote_fidelity": "mismatch", "record_id": "Silverman v. United States", "star_marker": null}}
{"assertion_id": "5016c5bb6d49e6b4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-510", "record_id": "Silverman v. United States"}, "payload": {"fragment": "#:~:text=had%20not%20been%20accomplished%20by", "page": null, "pin_id": "pin-510", "pinpoint_status": "star-verified", "quote": "had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area.", "quote_fidelity": "matched", "record_id": "Silverman v. United States", "star_marker": "510"}}
{"assertion_id": "0bb1f55c39668bb7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Silverman v. United States"}, "payload": {"as_of_content": "1961-03-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Silverman v. United States", "scope_note": "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones.", "varies_by_point": false}}
```

### lake record — Silverman v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Silverman v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Silverman v. United States",
    "case_name_short": "Silverman",
    "case_name_full": "SILVERMAN Et Al. v. UNITED STATES",
    "input_case_name": "Silverman v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-03-06",
    "year": 1961,
    "docket": "66",
    "cluster_id": 106187,
    "lead_opinion_id": 106187,
    "sibling_ids": [
      106187,
      9422144,
      9422145,
      9422146
    ],
    "absolute_url": "/opinion/106187/silverman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 505",
      "volume": "365",
      "reporter": "U.S.",
      "page": "505",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 679",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "679",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 734",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "734",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 A.L.R. 2d 1277",
        "volume": "97",
        "reporter": "A.L.R. 2d",
        "page": "1277",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1605",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1605",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 505",
        "volume": "365",
        "reporter": "U.S.",
        "page": "505",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 679",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "679",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 734",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "734",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1605",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1605",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 A.L.R. 2d 1277",
        "volume": "97",
        "reporter": "A.L.R. 2d",
        "page": "1277",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 505",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 505",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-509",
      "page": null,
      "quote": "through a party wall until it contacted a heating duct, turning the home's duct system into a giant microphone. The overheard conversations were used against the petitioners at trial. ## Issue Whether using a spike mike that physically penetrates a wall to listen to conversations inside a home is a Fourth Amendment search. ## Rule A physical intrusion into the home to eavesdrop is a search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-510",
      "page": null,
      "quote": "had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area.",
      "star_marker": "510",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11264,
      "fragment": "#:~:text=had%20not%20been%20accomplished%20by",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-511",
      "page": null,
      "quote": "In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law .... Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-03-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Silverman v. United States",
    "varies_by_point": false,
    "scope_note": "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones.",
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
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edgar Parral-Dominguez",
          "cluster_id": 2819835,
          "cite": [
            "794 F.3d 440",
            "2015 U.S. App. LEXIS 12697",
            "2015 WL 4479530"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 2736404,
          "cite": [
            "152 So. 3d 619",
            "2014 Fla. App. LEXIS 14965",
            "2014 WL 4723562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyllo v. United States",
          "cluster_id": 118443,
          "cite": [
            "150 L. Ed. 2d 94",
            "121 S. Ct. 2038",
            "533 U.S. 27",
            "2001 U.S. LEXIS 4487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estes v. Texas",
          "cluster_id": 107083,
          "cite": [
            "14 L. Ed. 2d 543",
            "85 S. Ct. 1628",
            "381 U.S. 532",
            "1965 U.S. LEXIS 2339",
            "1 Media L. Rep. (BNA) 1187",
            "6 Rad. Reg. 2d (P & F) 2104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. United States District Court for the Eastern District of Michigan",
          "cluster_id": 108581,
          "cite": [
            "32 L. Ed. 2d 752",
            "92 S. Ct. 2125",
            "407 U.S. 297",
            "1972 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jardines",
          "cluster_id": 856347,
          "cite": [
            "185 L. Ed. 2d 495",
            "133 S. Ct. 1409",
            "569 U.S. 1",
            "2013 U.S. LEXIS 2542",
            "24 Fla. L. Weekly Fed. S 117",
            "81 U.S.L.W. 4209",
            "2013 WL 1196577"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzI5OTU1MjAwMDAwJnM9MjY5OTY1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NTEmcz0xMTA4ODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
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
    "complete_query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
    "indexed_citing_opinions": 819,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106187,
        "count": 741,
        "count_source": "search"
      },
      {
        "opinion_id": 9422144,
        "count": 94,
        "count_source": "search"
      },
      {
        "opinion_id": 9422145,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422146,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1326,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/silverman-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzM0NDUmcz05NDUxMzU5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106187,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 102883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 228400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 250199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 2443377,
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
    "date_created": "2026-07-05T19:36:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:43:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Silverman v. United States

```
<div>
<center><b><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U.S. 505</a></span> (1961)</b></center>
<center><h1>SILVERMAN ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 66.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 5, 1960.</center>
<center>Decided March 6, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><i>Edward Bennett Williams</i> argued the cause for petitioners. With him on the briefs was <i>Agnes A. Neill.</i></p>
<p><i>John F. Davis</i> argued the cause for the United States. On the briefs were <i>Solicitor General Rankin, Assistant Attorney General Wilkey, Beatrice Rosenberg, J. F. Bishop</i> and <i>Julia P. Cooper.</i></p>
<p><span class="star-pagination">*506</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioners were tried and found guilty in the District Court for the District of Columbia upon three counts of an indictment charging gambling offenses under the District of Columbia Code. At the trial police officers were permitted to describe incriminating conversations engaged in by the petitioners at their alleged gambling establishment, conversations which the officers had overheard by means of an electronic listening device. The convictions were affirmed by the Court of Appeals, 107 U. S. App. D. C. 144, <span class="citation" data-id="9447215"><a href="/opinion/250199/julius-silverman-v-united-states-of-america-meyer-schwartz-v-united/" aria-description="Citation for case: Julius Silverman v. United States of America, Meyer...">275 F. 2d 173</a></span>, and we granted certiorari to consider the contention that the officers' testimony as to what they had heard through the electronic instrument should not have been admitted into evidence. <span class="citation multiple-matches"><a href="/c/U.%20S./363/801/">363 U. S. 801</a></span>.</p>
<p>The record shows that in the spring of 1958 the District of Columbia police had reason to suspect that the premises at 408 21st Street, N. W., in Washington, were being used as the headquarters of a gambling operation. They gained permission from the owner of the vacant adjoining row house to use it as an observation post. From this vantage point for a period of at least three consecutive days in April 1958, the officers employed a so-called "spike mike" to listen to what was going on within the four walls of the house next door.</p>
<p>The instrument in question was a microphone with a spike about a foot long attached to it, together with an amplifier, a power pack, and earphones. The officers inserted the spike under a baseboard in a second-floor room of the vacant house and into a crevice extending several inches into the party wall, until the spike hit something solid "that acted as a very good sounding board." The record clearly indicates that the spike made contact with a heating duct serving the house occupied <span class="star-pagination">*507</span> by the petitioners, thus converting their entire heating system into a conductor of sound. Conversations taking place on both floors of the house were audible to the officers through the earphones, and their testimony regarding these conversations, admitted at the trial over timely objection, played a substantial part in the petitioners' convictions.<sup>[1]</sup></p>
<p>Affirming the convictions, the Court of Appeals held that the trial court had not erred in admitting the officers' testimony. The court was of the view that the officers' use of the spike mike had violated neither the Communications Act of 1934, <span class="citation no-link">47 U. S. C. § 605</span>, cf. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span>, nor the petitioners' rights under the Fourth Amendment, cf. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>.</p>
<p>In reaching these conclusions the court relied primarily upon our decisions in <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>, and <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>. Judge Washington dissented, believing that, even if the petitioners' Fourth Amendment rights had not been abridged, the officers' conduct had transgressed the standards of due process guaranteed by the Fifth Amendment. Cf. <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>As to the inapplicability of § 605 of the Communications Act of 1934, we agree with the Court of Appeals. That section provides that ". . . no person not being <span class="star-pagination">*508</span> authorized by the sender shall intercept any communication and divulge or publish the existence, contents, substance, purport, effect, or meaning of such intercepted communication to any person . . . ." While it is true that much of what the officers heard consisted of the petitioners' share of telephone conversations, we cannot say that the officers intercepted these conversations within the meaning of the statute.</p>
<p>Similar contentions have been rejected here at least twice before. In <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#131" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 131</a></span>, the Court said: "Here the apparatus of the officers was not in any way connected with the telephone facilities, there was no interference with the communications system, there was no interception of any message. All that was heard through the microphone was what an eavesdropper, hidden in the hall, the bedroom, or the closet, might have heard. We do not suppose it is illegal to testify to what another person is heard to say merely because he is saying it into a telephone." In <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S. 129, 134</a></span>, it was said that "The listening in the next room to the words of [the petitioner] as he talked into the telephone receiver was no more the interception of a wire communication, within the meaning of the Act, than would have been the overhearing of the conversation by one sitting in the same room."</p>
<p>In presenting here the petitioners' Fourth Amendment claim, counsel has painted with a broad brush. We are asked to reconsider our decisions in <i>Goldman</i> v. <i>United States, supra</i><i>,</i> and <i>On Lee</i> v. <i>United States, supra</i><i>.</i> We are told that re-examination of the rationale of those cases, and of <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>, from which they stemmed, is now essential in the light of recent and projected developments in the science of electronics. We are favoured with a description of "a device known as the parabolic microphone which can pick up a conversation three hundred yards away." We are told of a <span class="star-pagination">*509</span> "still experimental technique whereby a room is flooded with a certain type of sonic wave," which, when perfected, "will make it possible to overhear everything said in a room without ever entering it or even going near it." We are informed of an instrument "which can pick up a conversation through an open office window on the opposite side of a busy street."<sup>[2]</sup></p>
<p>The facts of the present case, however, do not require us to consider the large questions which have been argued. We need not here contemplate the Fourth Amendment implications of these and other frightening paraphernalia which the vaunted marvels of an electronic age may visit upon human society. Nor do the circumstances here make necessary a re-examination of the Court's previous decisions in this area. For a fair reading of the record in this case shows that the eavesdropping was accomplished by means of an unauthorized physical penetration into the premises occupied by the petitioners. As Judge Washington pointed out without contradiction in the Court of Appeals: "Every inference, and what little direct evidence there was, pointed to the fact that the spike made contact with the heating duct, as the police admittedly hoped it would. Once the spike touched the heating duct, the duct became in effect a giant microphone, running through the entire house occupied by appellants." 107 U. S. App. D. C., at 150, <span class="citation" data-id="9447215"><a href="/opinion/250199/julius-silverman-v-united-states-of-america-meyer-schwartz-v-united/#179" aria-description="Citation for case: Julius Silverman v. United States of America, Meyer...">275 F. 2d, at 179</a></span>.</p>
<p>Eavesdropping accomplished by means of such a physical intrusion is beyond the pale of even those decisions in <span class="star-pagination">*510</span> which a closely divided Court has held that eavesdropping accomplished by other electronic means did not amount to an invasion of Fourth Amendment rights. In <i>Goldman</i> v. <i>United States, supra</i><i>,</i> the Court held that placing a detectaphone against an office wall in order to listen to conversations taking place in the office next door did not violate the Amendment. In <i>On Lee</i> v. <i>United States, supra</i><i>,</i> a federal agent, who was acquainted with the petitioner, entered the petitioner's laundry and engaged him in an incriminating conversation. The agent had a microphone concealed upon his person. Another agent, stationed outside with a radio receiving set, was tuned in on the conversation, and at the petitioner's subsequent trial related what he had heard. These circumstances were held not to constitute a violation of the petitioner's Fourth Amendment rights.</p>
<p>But in both <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> and <i><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">On Lee</a></span></i> the Court took pains explicitly to point out that the eavesdropping had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area. In <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> there had in fact been a prior physical entry into the petitioner's office for the purpose of installing a different listening apparatus, which had turned out to be ineffective. The Court emphasized that this earlier physical trespass had been of no relevant assistance in the later use of the detectaphone in the adjoining office. <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S., at 134-135</a></span>. And in <i><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">On Lee</a></span>,</i> as the Court said, ". . . no trespass was committed." The agent went into the petitioner's place of business "with the consent, if not by the implied invitation, of the petitioner." <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#751" aria-description="Citation for case: On Lee v. United States">343 U. S., at 751-752</a></span>.</p>
<p>The absence of a physical invasion of the petitioner's premises was also a vital factor in the Court's decision in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>. In holding that the wiretapping there did not violate the Fourth Amendment, the Court noted that "[t]he insertions <span class="star-pagination">*511</span> were made without trespass upon any property of the defendants. They were made in the basement of the large office building. The taps from house lines were made in the streets near the houses." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#457" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 457</a></span>. "There was no entry of the houses or offices of the defendants." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 464</a></span>. Relying upon these circumstances, the Court reasoned that "[t]he intervening wires are not part of [the defendant's] house or office any more than are the highways along which they are stretched." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#465" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 465</a></span>.</p>
<p>Here, by contrast, the officers overheard the petitioners' conversations only by usurping part of the petitioners' house or officea heating system which was an integral part of the premises occupied by the petitioners, a usurpation that was effected without their knowledge and without their consent. In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law relating to party walls.<sup>[3]</sup> Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law. See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266</a></span>; <i>On Lee</i> v. <i>United States, supra,</i> at 752; <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454</a></span>.</p>
<p>The Fourth Amendment, and the personal rights which it secures, have a long history. At the very core stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion. <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials 1029, 1066; <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-630</a></span>.<sup>[4]</sup> This <span class="star-pagination">*512</span> Court has never held that a federal officer may without warrant and without consent physically entrench into a man's office or home, there secretly observe or listen, and relate at the man's subsequent criminal trial what was seen or heard.</p>
<p>A distinction between the detectaphone employed in <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> and the spike mike utilized here seemed to the Court of Appeals too fine a one to draw. The court was "unwilling to believe that the respective rights are to be measured in fractions of inches." But decision here does not turn upon the technicality of a trespass upon a party wall as a matter of local law. It is based upon the reality of an actual intrusion into a constitutionally protected area. What the Court said long ago bears repeating now: "It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>. We find no occasion to re-examine <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> here, but we decline to go beyond it, by even a fraction of an inch.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>My trouble with <i>stare decisis</i> in this field is that it leads us to a matching of cases on irrelevant facts. An electronic device on the outside wall of a house is a permissible invasion of privacy according to <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>, while an electronic device that penetrates the wall, as here, is not. Yet the invasion <span class="star-pagination">*513</span> of privacy is as great in one case as in the other. The concept of "an unauthorized physical penetration into the premises," on which the present decision rests, seems to me to be beside the point. Was not the wrong in both cases done when the intimacies of the home were tapped, recorded, or revealed? The depth of the penetration of the electronic deviceeven the degree of its remoteness from the inside of the houseis not the measure of the injury. There is in each such case a search that should be made, if at all, only on a warrant issued by a magistrate. I stated my views in <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>, and adhere to them. Our concern should not be with the trivialities of the local law of trespass, as the opinion of the Court indicates. But neither should the command of the Fourth Amendment be limited by nice distinctions turning on the kind of electronic equipment employed. Rather our sole concern should be with whether the privacy of the home was invaded. Since it was invaded here, and since no search warrant was obtained as required by the Fourth Amendment and Rule 41 of the Federal Rules of Criminal Procedure, I agree with the Court that the judgment of conviction must be set aside.</p>
<p>MR. JUSTICE CLARK and MR. JUSTICE WHITTAKER, concurring.</p>
<p>In view of the determination by the majority that the unauthorized physical penetration into petitioners' premises constituted sufficient trespass to remove this case from the coverage of earlier decisions, we feel obliged to join in the Court's opinion.</p>
<h2>NOTES</h2>
<p>[1]  Alleging that the conversations thus overheard had been the basis for a search warrant under which other incriminating evidence was discovered at 408 21st Street, N. W., the petitioners sought unsuccessfully to suppress the evidence obtained upon execution of the warrant. It is the Government's position that there were ample grounds to support the search warrant, even without what was overheard by means of the spike mike. We deal here only with the admissibility at the trial of the officers' testimony as to what they heard by means of the listening device, leaving a determination of the warrant's validity to abide the event of a new trial.</p>
<p>[2]  See Hearings before the Subcommittee on Constitutional Rights of the Committee on the Judiciary, United States Senate, 85th Cong., 2d Sess., on Wiretapping, Eavesdropping, and the Bill of Rights; Hearings before Subcommittee No. 5 of the Committee on the Judiciary, House of Representatives, 84th Cong., 1st Sess., on Wiretapping; Dash, Schwartz and Knowlton, The Eavesdroppers (Rutgers University Press, 1959), pp. 346-358.</p>
<p>[3]  See <i>Fowler</i> v. <i>Koehler,</i> 43 App. D. C. 349.</p>
<p>[4]  William Pitt's eloquent description of this right has been often quoted. The late Judge Jerome Frank made the point in more contemporary language: "A man can still control a small part of his environment, his house; he can retreat thence from outsiders, secure in the knowledge that they cannot get at him without disobeying the Constitution. That is still a sizable hunk of libertyworth protecting from encroachment. A sane, decent, civilized society must provide some such oasis, some shelter from public scrutiny, some insulated enclosure, some enclave, some inviolate place which is a man's castle." <i>United States</i> v. <i>On Lee,</i> <span class="citation" data-id="9443046"><a href="/opinion/228400/united-states-v-on-lee/#315" aria-description="Citation for case: United States v. On Lee">193 F. 2d 306, 315-316</a></span> (dissenting opinion).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Silverthorne Lumber Co. v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Silverthorne Lumber Co. v. United States"
type: case
citation: "251 U.S. 385 (1920)"
parallel_cite: "40 S. Ct. 182; 64 L. Ed. 319"
neutral_cite: 1920 U.S. LEXIS 1685
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1920
date_decided: 1920-03-01
docket: 358
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1920-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Silverthorne Lumber Co. v. United States
  varies_by_point: false
  scope_note: "Foundational good law; origin of both the fruit-of-the-poisonous-tree rule and the independent-source exception, applied continuously through Wong Sun, Murray, and modern attenuation cases."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/99506/silverthorne-lumber-co-v-united-states/"
  cluster_id: 99506
  opinion_id: 99506
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Anchor (fruit of the poisonous tree origin; independent source)"
related: ["[[Weeks v. United States]]", "[[Nardone v. United States]]"]
aliases: ["Silverthorne Lumber Co v United States"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "independent-source"]
holding: "Evidence obtained through an unconstitutional search may not be used at all — directly or indirectly — and the government may not exploit knowledge gained from its own illegal seizure; but facts learned from a genuinely independent source may still be proved (the independent-source exception)."
lake:
  record_id: Silverthorne Lumber Co. v. United States
  status: verified
  projected_at: 2026-07-06
---

# Silverthorne Lumber Co. v. United States

*251 U.S. 385 (1920)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents, "without a shadow of authority," arrested the Silverthornes and made "a clean sweep" of all the books and papers at their company's office. The District Court ordered the originals returned but allowed the Government to keep photographs and copies. The Government then issued fresh subpoenas to compel production of the very documents it had unlawfully examined and copied. When the Silverthornes refused, they were held in contempt.

## Issue
Whether the Government, having unlawfully seized and copied a party's documents, may use the knowledge so gained to subpoena the same documents through "regular" process — i.e., whether the Fourth Amendment bars indirect as well as direct use of illegally obtained evidence.

## Rule
No. Illegally obtained evidence may not be used even indirectly. "The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all." — 251 U.S. at 392. ^pin-392

The bar is not absolute, however: "Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it in the way proposed." — *Id.* ^pin-392b

To allow the subpoena would "reduce[] the Fourth Amendment to a form of words." — *Id.* ^pin-392c

## Application
The Government conceded the seizure was unlawful but argued it could study and copy the papers, then subpoena the originals "in a more regular form." The Court rejected the idea that the Constitution protects only physical possession and not the advantages gained by the forbidden act. Because the subpoenas rested entirely on knowledge derived from the illegal seizure — not from any [[Inevitable Discovery and Independent Source|independent source]] — they could not be enforced, and the contempt could not stand.

## Conclusion
The Government could not exploit its unlawful seizure to compel production of the documents; the contempt judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Silverthorne* is the origin of the **fruit-of-the-poisonous-tree** doctrine and, in the same breath, the **independent-source** exception. Both principles run forward through [[Nardone v. United States]] (which coined the "fruit" label), *[[Wong Sun v. United States]]*, and *[[Murray v. United States]]*, and remain foundational good law.

## Appears on
- [[The Exclusionary Rule]] — *Anchor ([[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]] origin; [[Inevitable Discovery and Independent Source|independent source]])*

## Sources
- *Silverthorne Lumber Co. v. United States*, 251 U.S. 385 (1920) — https://www.courtlistener.com/opinion/99506/silverthorne-lumber-co-v-united-states/ — pinpoint: 392.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f856ddfdaa08ccaa", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Silverthorne Lumber Co. v. United States"}, "payload": {"all": [{"cite": "251 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "251"}, {"cite": "40 S. Ct. 182", "page": "182", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "40"}, {"cite": "64 L. Ed. 319", "page": "319", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "64"}, {"cite": "1920 U.S. LEXIS 1685", "page": "1685", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1920"}], "display": "251 U.S. 385", "official": {"cite": "251 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "251"}, "official_selection_present": true, "record_id": "Silverthorne Lumber Co. v. United States"}}
{"assertion_id": "58754aa1dcbe538a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392c", "record_id": "Silverthorne Lumber Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392c", "pinpoint_status": "slip-only", "quote": "reduce[] the Fourth Amendment to a form of words.", "quote_fidelity": "mismatch", "record_id": "Silverthorne Lumber Co. v. United States", "star_marker": null}}
{"assertion_id": "ef2ebf6e7f057039", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392", "record_id": "Silverthorne Lumber Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392", "pinpoint_status": "slip-only", "quote": "process — i.e., whether the Fourth Amendment bars indirect as well as direct use of illegally obtained evidence. ## Rule No. Illegally obtained evidence may not be used even indirectly.", "quote_fidelity": "mismatch", "record_id": "Silverthorne Lumber Co. v. United States", "star_marker": null}}
{"assertion_id": "f9474d83bfdeb2cc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-392b", "record_id": "Silverthorne Lumber Co. v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-392b", "pinpoint_status": "slip-only", "quote": "Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it in the way proposed.", "quote_fidelity": "mismatch", "record_id": "Silverthorne Lumber Co. v. United States", "star_marker": null}}
{"assertion_id": "561f908bdc6a83de", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Silverthorne Lumber Co. v. United States"}, "payload": {"as_of_content": "1920-01-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Silverthorne Lumber Co. v. United States", "scope_note": "Foundational good law; origin of both the fruit-of-the-poisonous-tree rule and the independent-source exception, applied continuously through Wong Sun, Murray, and modern attenuation cases.", "varies_by_point": false}}
```

### lake record — Silverthorne Lumber Co. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Silverthorne Lumber Co. v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Silverthorne Lumber Co. v. United States",
    "case_name_short": "",
    "case_name_full": "Silverthorne Lumber Company, Inc., Et Al. v. United States",
    "input_case_name": "Silverthorne Lumber Co. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1920-03-01",
    "year": 1920,
    "docket": "358",
    "cluster_id": 99506,
    "lead_opinion_id": 99506,
    "sibling_ids": [
      99506
    ],
    "absolute_url": "/opinion/99506/silverthorne-lumber-co-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "251 U.S. 385",
      "volume": "251",
      "reporter": "U.S.",
      "page": "385",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "40 S. Ct. 182",
        "volume": "40",
        "reporter": "S. Ct.",
        "page": "182",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 319",
        "volume": "64",
        "reporter": "L. Ed.",
        "page": "319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1920 U.S. LEXIS 1685",
        "volume": "1920",
        "reporter": "U.S. LEXIS",
        "page": "1685",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "251 U.S. 385",
        "volume": "251",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 S. Ct. 182",
        "volume": "40",
        "reporter": "S. Ct.",
        "page": "182",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 319",
        "volume": "64",
        "reporter": "L. Ed.",
        "page": "319",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1920 U.S. LEXIS 1685",
        "volume": "1920",
        "reporter": "U.S. LEXIS",
        "page": "1685",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "251 U.S. 385",
    "official_selection": {
      "court_class": "scotus",
      "selected": "251 U.S. 385",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-392",
      "page": null,
      "quote": "process \u2014 i.e., whether the Fourth Amendment bars indirect as well as direct use of illegally obtained evidence. ## Rule No. Illegally obtained evidence may not be used even indirectly.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-392b",
      "page": null,
      "quote": "Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government's own wrong cannot be used by it in the way proposed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-392c",
      "page": null,
      "quote": "reduce[] the Fourth Amendment to a form of words.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1920-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Silverthorne Lumber Co. v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational good law; origin of both the fruit-of-the-poisonous-tree rule and the independent-source exception, applied continuously through Wong Sun, Murray, and modern attenuation cases.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Serrano (A173250)",
          "cluster_id": 10135658,
          "cite": [
            "324 Or. App. 453",
            "527 P.3d 54"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Junior Wardrick",
          "cluster_id": 784262,
          "cite": [
            "350 F.3d 446",
            "2003 U.S. App. LEXIS 23669",
            "2003 WL 22789492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane1_negative"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Branzburg v. Hayes",
          "cluster_id": 108611,
          "cite": [
            "33 L. Ed. 2d 626",
            "92 S. Ct. 2646",
            "408 U.S. 665",
            "1972 U.S. LEXIS 132",
            "24 Rad. Reg. 2d (P & F) 2125",
            "1 Media L. Rep. (BNA) 2617"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
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
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nardone v. United States",
          "cluster_id": 103259,
          "cite": [
            "308 U.S. 338",
            "60 S. Ct. 266",
            "84 L. Ed. 307",
            "1939 U.S. LEXIS 1132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fahy v. Connecticut",
          "cluster_id": 106699,
          "cite": [
            "11 L. Ed. 2d 171",
            "84 S. Ct. 229",
            "375 U.S. 85",
            "1963 U.S. LEXIS 128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. United States District Court for the Eastern District of Michigan",
          "cluster_id": 108581,
          "cite": [
            "32 L. Ed. 2d 752",
            "92 S. Ct. 2125",
            "407 U.S. 297",
            "1972 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Agnello v. United States",
          "cluster_id": 100711,
          "cite": [
            "269 U.S. 20",
            "46 S. Ct. 4",
            "70 L. Ed. 145",
            "1925 U.S. LEXIS 2",
            "51 A.L.R. 409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverthorne Lumber Co. v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(99506) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDA0NDAwMDAwMDAwJnM9Nzc1NDA0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2899506%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(99506)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU1JnM9MTEwMjMwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2899506%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(99506)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(99506)",
    "indexed_citing_opinions": 1487,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 99506,
        "count": 1487,
        "count_source": "search"
      }
    ],
    "citation_count": 2373,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/silverthorne-lumber-co-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxNzA2Mzgmcz0xMDEzNTY1OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%2899506%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 99506,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 99506,
        "cited_id": 98094,
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
    "date_created": "2026-07-05T19:43:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:43:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:43:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:46:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:43:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Silverthorne Lumber Co. v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b430-5">
  Mr. Justice Holmes
 </author>
<p id="AGe">
  delivered the opinion of the court.
 </p>
<p id="b430-6">
  This is a writ of error brought to reverse a judgment of the District Court fining the Silverthorne Lumber Company two hundred and fifty dollars for contempt of court and ordering Frederick W. Silverthorne to be imprisoned until he should purge himself of a similar contempt. The contempt in question was a refusal to obey subpoenas and an order of Court to produce books and documents of the company before the grand ,ury to be used in regard to alleged violation of the statutes of the United States by the said Silverthorne and his father. One ground of the refusal was that the order of the Court infringed the rights of the parties under the Fourth Amendment of the Constitution of the United States.
 </p>
<p id="b430-7">
  The facts are smple. An indictment upon a single specific charge having been brought against the two Silverthornes mentioned, they both were arrested at their homes early in the morning of February 25, 1919, and were .detained in custody a number of horns. While they were thus detained representatives of the Department of Justice and the United States marshal without a shadow of authority went to the office of their company and made a clean sweep of all the books, papers and documents found there. All the employees were taken or directed to go to the office of the District Attorney of the United States to which also the books, &amp;e., were taken at once. An application was made as soon as might be to the District
  <span citation-index="1" class="star-pagination" label="391"> 
   *391
   </span>
  Court for a return of what thus had been taken unlawfully. It was opposed by the District Attorney so far as he had found evidence against the plaintiffs in error, and it was stated that the evidence so obtained was before the grand jury. Color had been given by the District Attorney to the approach of those concerned in the act by an invalid subpoena for certain documents relating to the charge in the indictment then on file. Thus the case is not that of knowledge acquired through the wrongful act of a stranger, but it must .be assumed that the Government planned or at all events ratified the whole performance. Photographs and copies of material papers were made and a new indictment was framed based upon the knowledge thus obtained. The District Court ordered a return of the originals but impounded the photographs and copies. Subpoenas.to produce the originals then were served and on the refusal of the plaintiffs in error to produce them the Court made an order that the subpoenas should be complied with, although it had found that all the papers had been seized in violation of the parties’ constitutional rights. The refusal to obey this order is the contempt alleged. The Government now, while in form repudiating and condemning the illegal seizure, seeks to maintain its right to avail itself of the knowledge obtained by that means which otherwise it would not have had. .
 </p>
<p id="b431-4">
  The proposition could not be presented more nakedly. It is' that although of course its seizure was an outrage which the Government now regrets, it may study the papers before it returns them, copy them, and then may use the knowledge that it has gained to call upon the owners in a more regular form to produce them; that the protection of the Constitution covers the physical possession but not any advantages that the Government can gain over the object of its pursuit by doing the forbidden act.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, to be sure, had established that laying the papers directly before the grand jury was
  <span citation-index="1" class="star-pagination" label="392"> 
   *392
   </span>
  unwarranted, but it is taken to mean only that two steps are required instead of one. In our opinion such is not the .law. It reduces the Fourth Amendment to a form of words. <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 393</a></span>. The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all. Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others, but the knowledge gained by the Government’s own wrong cannot bé used by it in the way proposed. The numerous decisions, like
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>, holding that a collateral inquiry into the mode in which evidence has been got will not be allowed when the question is raised for the first time at the trial, are no authority in the present proceeding, as is explained in
  <em>
   Weeks
  </em>
  v.
  <em>
   United
  </em>
  States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#394" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 394, 395</a></span>. Whether some of those decisions have gone too far or have given wrong reasons it is unnecessary to inquire; the principle applicable to the present case seems to us plain. It is stated satisfactorily in
  <em>
   Flagg
  </em>
  v.
  <em>
   United States,
  </em>
  233 Fed. Rep. 481, 483. In
  <em>
   Linn
  </em>
  v.
  <em>
   United States,
  </em>
  251 Fed. Rep. 476, 480, it was thought that a different rule applied to a corporation, on the ground that it was not privileged from producing its books and papers. But the rights of a corporation against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way.
 </p>
<p id="b432-6">
<em>
   Judgment reversed.
  </em>
</p>
<judges id="b432-7">
  The Chief Justice and Mr. Justice Pitney dissent.
 </judges>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Simmons v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Simmons v. United States"
type: case
citation: "390 U.S. 377 (1968)"
parallel_cite: "88 S. Ct. 967; 19 L. Ed. 2d 1247"
neutral_cite: 1968 U.S. LEXIS 2167
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-03-18
docket: 55
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-03-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Simmons v. United States
  varies_by_point: false
  scope_note: "Both holdings — the photographic-identification due-process standard and the immunity for suppression-hearing testimony — remain good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107636/simmons-v-united-states/"
  cluster_id: 107636
  opinion_id: 107636
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny"
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Stovall v. Denno]]", "[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[Jones v. United States]]", "[[Alderman v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "fifth-amendment", "standing", "eyewitness-identification", "photographic-identification", "due-process"]
holding: "A pretrial photographic identification violates due process only if it was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification; and a defendant's testimony given to establish Fourth Amendment standing at a suppression hearing may not be used against him at trial on guilt."
lake:
  record_id: Simmons v. United States
  status: verified
  projected_at: 2026-07-06
---

# Simmons v. United States

*390 U.S. 377 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Simmons, Andrews, and Garrett were tried for the armed robbery of a federally insured Chicago savings and loan. Two issues bear on this wiki. First, the FBI showed bank-employee eyewitnesses group photographs the day after the robbery, and Simmons argued the photographic procedure was so suggestive that it tainted the in-court identifications. Second, Garrett, to establish standing to suppress a suitcase of incriminating evidence, testified at a pretrial [[Common Legal Terms#suppression-hearing|suppression hearing]] that the suitcase was his; the Government used that admission against him at trial.

## Issue
(1) When does a pretrial photographic identification procedure deny due process; and (2) whether testimony a defendant gives at a [[Common Legal Terms#suppression-hearing|suppression hearing]] to establish [[Standing to Challenge a Search|Fourth Amendment standing]] may be admitted against him at trial on the issue of guilt.

## Rule
Two holdings. On identification: "convictions based on eyewitness identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." — 390 U.S. at 384. ^pin-384

On suppression-hearing testimony: a defendant should not have to trade one right for another. "[W]e find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection." — *Id.* at 394. ^pin-394

## Application
Applying the identification standard, Simmons's claim failed: the robbery occurred in a well-lit bank where five employees saw the robber for up to five minutes; the witnesses were shown at least six photographs each, separately, the next day while memories were fresh, with no suggestion of whom the FBI suspected; and all five identified Simmons. There was "little chance" of misidentification, so the procedure did not deny due process. As to Garrett, his suppression-hearing testimony admitting ownership of the suitcase was "a strong piece of evidence against [him]"; forcing him to choose between asserting his Fourth Amendment claim and his Fifth Amendment privilege was intolerable, so that testimony could not be used against him at trial.

## Conclusion
The judgment was affirmed as to Simmons (the photographic procedure was not impermissibly suggestive) and reversed as to Garrett (his suppression-hearing testimony was immunized from use on the issue of guilt).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Simmons* "very substantial likelihood of irreparable misidentification" standard, drawn from [[Stovall v. Denno]], carries into [[Neil v. Biggers]] and [[Manson v. Brathwaite]]; the suppression-hearing testimonial-immunity rule is the standing companion cited in [[Alderman v. United States]] and rests on the standing predicate of [[Jones v. United States]].

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny*
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *Simmons v. United States*, 390 U.S. 377 (1968) — https://www.courtlistener.com/opinion/107636/simmons-v-united-states/ — pinpoints: 384, 394.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4f93cef88272b3f5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Simmons v. United States"}, "payload": {"all": [{"cite": "390 U.S. 377", "page": "377", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "390"}, {"cite": "88 S. Ct. 967", "page": "967", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "19 L. Ed. 2d 1247", "page": "1247", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "19"}, {"cite": "1968 U.S. LEXIS 2167", "page": "2167", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}], "display": "390 U.S. 377", "official": {"cite": "390 U.S. 377", "page": "377", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "390"}, "official_selection_present": true, "record_id": "Simmons v. United States"}}
{"assertion_id": "613e8560d7569b0c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-394", "record_id": "Simmons v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-394", "pinpoint_status": "slip-only", "quote": "[W]e find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.", "quote_fidelity": "mismatch", "record_id": "Simmons v. United States", "star_marker": null}}
{"assertion_id": "cd5475adc93d37a5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-384", "record_id": "Simmons v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-384", "pinpoint_status": "slip-only", "quote": "--- # Simmons v. United States *390 U.S. 377 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Simmons, Andrews, and Garrett were tried for the armed robbery of a federally insured Chicago savings and loan. Two issues bear on this wiki. First, the FBI showed bank-employee eyewitnesses group photographs the day after the robbery, and Simmons argued the photographic procedure was so suggestive that it tainted the in-court identifications. Second, Garrett, to establish standing to suppress a suitcase of incriminating evidence, testified at a pretrial suppression hearing that the suitcase was his; the Government used that admission against him at trial. ## Issue (1) When does a pretrial photographic identification procedure deny due process; and (2) whether testimony a defendant gives at a suppression hearing to establish Fourth Amendment standing may be admitted against him at trial on the issue of guilt. ## Rule Two holdings. On identification:", "quote_fidelity": "mismatch", "record_id": "Simmons v. United States", "star_marker": null}}
{"assertion_id": "ce9b6a73daae16bf", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Simmons v. United States"}, "payload": {"as_of_content": "1968-03-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Simmons v. United States", "scope_note": "Both holdings — the photographic-identification due-process standard and the immunity for suppression-hearing testimony — remain good law.", "varies_by_point": false}}
```

### lake record — Simmons v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Simmons v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Simmons v. United States",
    "case_name_short": "Simmons",
    "case_name_full": "SIMMONS Et Al v. UNITED STATES",
    "input_case_name": "Simmons v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-03-18",
    "year": 1968,
    "docket": "55",
    "cluster_id": 107636,
    "lead_opinion_id": 107636,
    "sibling_ids": [
      107636,
      9423638,
      9423639,
      9423640
    ],
    "absolute_url": "/opinion/107636/simmons-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "390 U.S. 377",
      "volume": "390",
      "reporter": "U.S.",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 967",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1247",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 2167",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "390 U.S. 377",
        "volume": "390",
        "reporter": "U.S.",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 967",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 1247",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "1247",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 2167",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "2167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "390 U.S. 377",
    "official_selection": {
      "court_class": "scotus",
      "selected": "390 U.S. 377",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-384",
      "page": null,
      "quote": "--- # Simmons v. United States *390 U.S. 377 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Simmons, Andrews, and Garrett were tried for the armed robbery of a federally insured Chicago savings and loan. Two issues bear on this wiki. First, the FBI showed bank-employee eyewitnesses group photographs the day after the robbery, and Simmons argued the photographic procedure was so suggestive that it tainted the in-court identifications. Second, Garrett, to establish standing to suppress a suitcase of incriminating evidence, testified at a pretrial suppression hearing that the suitcase was his; the Government used that admission against him at trial. ## Issue (1) When does a pretrial photographic identification procedure deny due process; and (2) whether testimony a defendant gives at a suppression hearing to establish Fourth Amendment standing may be admitted against him at trial on the issue of guilt. ## Rule Two holdings. On identification:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-394",
      "page": null,
      "quote": "[W]e find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-03-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Simmons v. United States",
    "varies_by_point": false,
    "scope_note": "Both holdings \u2014 the photographic-identification due-process standard and the immunity for suppression-hearing testimony \u2014 remain good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Farook",
          "cluster_id": 9352623,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Farook",
          "cluster_id": 6466318,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fontanez",
          "cluster_id": 4610750,
          "cite": [
            "120 N.E.3d 707",
            "482 Mass. 22"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neil v. Biggers",
          "cluster_id": 108639,
          "cite": [
            "34 L. Ed. 2d 401",
            "93 S. Ct. 375",
            "409 U.S. 188",
            "1972 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockett v. Ohio",
          "cluster_id": 109935,
          "cite": [
            "57 L. Ed. 2d 973",
            "98 S. Ct. 2954",
            "438 U.S. 586",
            "1978 U.S. LEXIS 133",
            "9 Ohio Op. 3d 26"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darden v. Wainwright",
          "cluster_id": 111717,
          "cite": [
            "91 L. Ed. 2d 144",
            "106 S. Ct. 2464",
            "477 U.S. 168",
            "1986 U.S. LEXIS 113"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tibbs v. Florida",
          "cluster_id": 110731,
          "cite": [
            "72 L. Ed. 2d 652",
            "102 S. Ct. 2211",
            "457 U.S. 31",
            "1982 U.S. LEXIS 116",
            "50 U.S.L.W. 4607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110382,
          "cite": [
            "66 L. Ed. 2d 722",
            "101 S. Ct. 764",
            "449 U.S. 539",
            "1981 U.S. LEXIS 62",
            "49 U.S.L.W. 4133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Stincer",
          "cluster_id": 111928,
          "cite": [
            "96 L. Ed. 2d 631",
            "107 S. Ct. 2658",
            "482 U.S. 730",
            "1987 U.S. LEXIS 2727",
            "55 U.S.L.W. 4901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. United States",
          "cluster_id": 108760,
          "cite": [
            "36 L. Ed. 2d 208",
            "93 S. Ct. 1565",
            "411 U.S. 223",
            "1973 U.S. LEXIS 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGautha v. California",
          "cluster_id": 108329,
          "cite": [
            "28 L. Ed. 2d 711",
            "91 S. Ct. 1454",
            "402 U.S. 183",
            "1971 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Foster v. California",
          "cluster_id": 107890,
          "cite": [
            "22 L. Ed. 2d 402",
            "89 S. Ct. 1127",
            "394 U.S. 440",
            "1969 U.S. LEXIS 2050"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conner v. State",
          "cluster_id": 2335623,
          "cite": [
            "67 S.W.3d 192",
            "2001 Tex. Crim. App. LEXIS 61",
            "2001 WL 1043248"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chaffin v. Stynchcombe",
          "cluster_id": 108793,
          "cite": [
            "36 L. Ed. 2d 714",
            "93 S. Ct. 1977",
            "412 U.S. 17",
            "1973 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Simmons v. United States:lane2_top_cited"
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
        "journal_ref": "Simmons v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDg3NzIxNjAwMDAwJnM9NDM3MDE0MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01ODImcz0xOTYwODExJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 0,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107636 OR 9423638 OR 9423639 OR 9423640)",
    "indexed_citing_opinions": 4614,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107636,
        "count": 4208,
        "count_source": "search"
      },
      {
        "opinion_id": 9423638,
        "count": 509,
        "count_source": "search"
      },
      {
        "opinion_id": 9423639,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423640,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6701,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/simmons-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTIyNzkmcz0xMDEyMjc0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107636+OR+9423638+OR+9423639+OR+9423640%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107636,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 105517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 106512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 107512,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 240852,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 261271,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 262814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 271407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 274369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 276553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 278761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1178843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1472609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1509817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1542459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1569514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107636,
        "cited_id": 1609276,
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
    "date_created": "2026-07-05T19:46:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:49:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:46:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Simmons v. United States

```
<div>
<center><b><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U.S. 377</a></span> (1968)</b></center>
<center><h1>SIMMONS ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 55.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 15, 1968.</center>
<center>Decided March 18, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*379</span> <i>Raymond J. Smith</i> argued the cause for petitioners. With him on the brief were <i>John Powers Crowley</i> and <i>George F. Callaghan.</i></p>
<p><i>Solicitor General Griswold</i> argued the cause for the United States. With him on the brief were <i>Assistant Attorney General Vinson, Beatrice Rosenberg</i> and <i>Mervyn Hamburg.</i></p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>This case presents issues arising out of the petitioners trial and conviction in the United States District Court for the Northern District of Illinois for the armed robbery of a federally insured savings and loan association.</p>
<p>The evidence at trial showed that at about 1:45 p. m. <span class="star-pagination">*380</span> on February 27, 1964, two men entered a Chicago savings and loan association. One of them pointed a gun at a teller and ordered her to put money into a sack which the gunman supplied. The men remained in the bank about five minutes. After they left, a bank employee rushed to the street and saw one of the men sitting on the passenger side of a departing white 1960 Thunderbird automobile with a large scrape on the right door. Within an hour police located in the vicinity a car matching this description. They discovered that it belonged to a Mrs. Rey, sister-in-law of petitioner Simmons. She told the police that she had loaned the car for the afternoon to her brother, William Andrews.</p>
<p>At about 5:15 p. m. the same day, two FBI agents came to the house of Mrs. Mahon, Andrews' mother, about half a block from the place where the car was then parked.<sup>[1]</sup> The agents had no warrant, and at trial it was disputed whether Mrs. Mahon gave them permission to search the house. They did search, and in the basement they found two suitcases, of which Mrs. Mahon disclaimed any knowledge. One suitcase contained, among other items, a gun holster, a sack similar to the one used in the robbery, and several coin cards and bill wrappers from the bank which had been robbed.</p>
<p>The following morning the FBI obtained from another of Andrews' sisters some snapshots of Andrews and of petitioner Simmons, who was said by the sister to have been with Andrews the previous afternoon. These snapshots were shown to the five bank employees who had witnessed the robbery. Each witness identified pictures of Simmons as representing one of the robbers. A week or two later, three of these employees identified photographs <span class="star-pagination">*381</span> of petitioner Garrett as depicting the other robber, the other two witnesses stating that they did not have a clear view of the second robber.</p>
<p>The petitioners, together with William Andrews, subsequently were indicted and tried for the robbery, as indicated. Just prior to the trial, Garrett moved to suppress the Government's exhibit consisting of the suitcase containing the incriminating items. In order to establish his standing so to move, Garrett testified that, although he could not identify the suitcase with certainty, it was similar to one he had owned, and that he was the owner of clothing found inside the suitcase. The District Court denied the motion to suppress. Garrett's testimony at the "suppression" hearing was admitted against him at trial.</p>
<p>During the trial, all five bank employee witnesses identified Simmons as one of the robbers. Three of them identified Garrett as the second robber, the other two testifying that they did not get a good look at the second robber. The District Court denied the petitioners' request under <span class="citation no-link">18 U. S. C. § 3500</span> (the so-called Jencks Act) for production of the photographs which had been shown to the witnesses before trial.</p>
<p>The jury found Simmons and Garrett, as well as Andrews, guilty as charged. On appeal, the Court of Appeals for the Seventh Circuit affirmed as to Simmons and Garrett, but reversed the conviction of Andrews on the ground that there was insufficient evidence to connect him with the robbery. <span class="citation" data-id="274369"><a href="/opinion/274369/united-states-v-robert-james-garrett-thomas-earl-simmons-and-william-earl/" aria-description="Citation for case: United States v. Robert James Garrett, Thomas Earl...">371 F. 2d 296</a></span>.</p>
<p>We granted certiorari as to Simmons and Garrett, <span class="citation" data-id="8959716"><a href="/opinion/8968302/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">388 U. S. 906</a></span>, to consider the following claims. First, Simmons asserts that his pretrial identification by means of photographs was in the circumstances so unnecessarily suggestive and conducive to misidentification as to deny him due process of law, or at least to require reversal of his conviction in the exercise of our supervisory power <span class="star-pagination">*382</span> over the lower federal courts. Second, both petitioners contend that the District Court erred in refusing defense requests for production under <span class="citation no-link">18 U. S. C. § 3500</span> of the pictures of the petitioners which were shown to eyewitnesses prior to trial. Third, Garrett urges that his constitutional rights were violated when testimony given by him in support of his "suppression" motion was admitted against him at trial. For reasons which follow, we affirm the judgment of the Court of Appeals as to Simmons, but reverse as to Garrett.</p>
<p></p>
<h2>I.</h2>
<p>The facts as to the identification claim are these. As has been noted previously, FBI agents on the day following the robbery obtained from Andrews' sister a number of snapshots of Andrews and Simmons. There seem to have been at least six of these pictures, consisting mostly of group photographs of Andrews, Simmons, and others. Later the same day, these were shown to the five bank employees who had witnessed the robbery at their place of work, the photographs being exhibited to each employee separately. Each of the five employees identified Simmons from the photographs. At later dates, some of these witnesses were again interviewed by the FBI and shown indeterminate numbers of pictures. Again, all identified Simmons. At trial, the Government did not introduce any of the photographs, but relied upon in-court identification by the five eyewitnesses, each of whom swore that Simmons was one of the robbers.</p>
<p>In support of his argument, Simmons looks to last Term's "lineup" decisions<i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <i>Gilbert</i> v. <i>California,</i> 388 U. S. 263in which this Court first departed from the rule that the manner of an extra-judicial identification affects only the weight, not the admissibility, of identification testimony at trial. The rationale of those cases was that an <span class="star-pagination">*383</span> accused is entitled to counsel at any "critical stage of the prosecution," and that a post-indictment lineup is such a "critical stage." See 388 U. S., at 236-237. Simmons, however, does not contend that he was entitled to counsel at the time the pictures were shown to the witnesses. Rather, he asserts simply that in the circumstances the identification procedure was so unduly prejudicial as fatally to taint his conviction. This is a claim which must be evaluated in light of the totality of surrounding circumstances. See <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, at 302</a></span>; <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span>. Viewed in that context, we find the claim untenable.</p>
<p>It must be recognized that improper employment of photographs by police may sometimes cause witnesses to err in identifying criminals. A witness may have obtained only a brief glimpse of a criminal, or may have seen him under poor conditions. Even if the police subsequently follow the most correct photographic identification procedures and show him the pictures of a number of individuals without indicating whom they suspect, there is some danger that the witness may make an incorrect identification. This danger will be increased if the police display to the witness only the picture of a single individual who generally resembles the person he saw, or if they show him the pictures of several persons among which the photograph of a single such individual recurs or is in some way emphasized.<sup>[2]</sup> The chance of misidentification is also heightened if the police indicate to the witness that they have other evidence that one of the persons pictured committed the crime.<sup>[3]</sup> Regardless of how the initial misidentification comes about, the witness thereafter is apt to retain in his memory the image of the photograph rather than of the person actually <span class="star-pagination">*384</span> seen, reducing the trustworthiness of subsequent lineup or courtroom identification.<sup>[4]</sup></p>
<p>Despite the hazards of initial identification by photograph, this procedure has been used widely and effectively in criminal law enforcement, from the standpoint both of apprehending offenders and of sparing innocent suspects the ignominy of arrest by allowing eyewitnesses to exonerate them through scrutiny of photographs. The danger that use of the technique may result in convictions based on misidentification may be substantially lessened by a course of cross-examination at trial which exposes to the jury the method's potential for error. We are unwilling to prohibit its employment, either in the exercise of our supervisory power or, still less, as a matter of constitutional requirement. Instead, we hold that each case must be considered on its own facts, and that convictions based on eyewitness identification at trial following a pretrial identification by photograph will be set aside on that ground only if the photographic identification procedure was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification. This standard accords with our resolution of a similar issue in <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#301" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 301-302</a></span>, and with decisions of other courts on the question of identification by photograph.<sup>[5]</sup></p>
<p>Applying the standard to this case, we conclude that petitioner Simmons' claim on this score must fail. In the first place, it is not suggested that it was unnecessary for the FBI to resort to photographic identification in this instance. A serious felony had been committed. The perpetrators were still at large. The inconclusive clues which law enforcement officials possessed led to <span class="star-pagination">*385</span> Andrews and Simmons. It was essential for the FBI agents swiftly to determine whether they were on the right track, so that they could properly deploy their forces in Chicago and, if necessary, alert officials in other cities. The justification for this method of procedure was hardly less compelling than that which we found to justify the "one-man lineup" in <i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>.</i></p>
<p>In the second place, there was in the circumstances of this case little chance that the procedure utilized led to misidentification of Simmons. The robbery took place in the afternoon in a well-lighted bank. The robbers wore no masks. Five bank employees had been able to see the robber later identified as Simmons for periods ranging up to five minutes. Those witnesses were shown the photographs only a day later, while their memories were still fresh. At least six photographs were displayed to each witness. Apparently, these consisted primarily of group photographs, with Simmons and Andrews each appearing several times in the series. Each witness was alone when he or she saw the photographs. There is no evidence to indicate that the witnesses were told anything about the progress of the investigation, or that the FBI agents in any other way suggested which persons in the pictures were under suspicion.</p>
<p>Under these conditions, all five eyewitnesses identified Simmons as one of the robbers. None identified Andrews, who apparently was as prominent in the photographs as Simmons. These initial identifications were confirmed by all five witnesses in subsequent viewings of photographs and at trial, where each witness identified Simmons in person. Notwithstanding cross-examination, none of the witnesses displayed any doubt about their respective identifications of Simmons. Taken together, these circumstances leave little room for doubt that the identification of Simmons was correct, even though the identification procedure employed may have in some <span class="star-pagination">*386</span> respects fallen short of the ideal.<sup>[6]</sup> We hold that in the factual surroundings of this case the identification procedure used was not such as to deny Simmons due process of law or to call for reversal under our supervisory authority.</p>
<p></p>
<h2>II.</h2>
<p>It is next contended, by both petitioners, that in any event the District Court erred in refusing a defense request that the photographs shown to the witnesses prior to trial be turned over to the defense for purposes of cross-examination. This claim to production is based on <span class="citation no-link">18 U. S. C. § 3500</span>, the so-called Jencks Act. That Act, passed in response to this Court's decision in <i>Jencks</i> v. <i>United States,</i> <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>, provides that after a witness has testified for the Government in a federal criminal prosecution the Government must, on request of the defense, produce any "statement . . . of the witness in the possession of the United States which relates to the subject matter as to which the witness has testified." For the Act's purposes, as they relate to this case, a "statement" is defined as "a written statement made by said witness and signed or otherwise adopted or approved by him . . . ."</p>
<p><span class="star-pagination">*387</span> Written statements of this kind were taken from all five eyewitnesses by the FBI on the day of the robbery. Apparently none were taken thereafter. When these statements were produced by the Government at trial pursuant to § 3500, the defense also claimed the right to look at the photographs "under 3500." The District Judge denied these requests.</p>
<p>The petitioners' theory seems to be that the photographs were incorporated in the written statements of the witnesses, and that they therefore had to be produced under § 3500. The legislative history of the Jencks Act does confirm that photographs must be produced if they constitute a part of a written statement.<sup>[7]</sup> However, the record in this case does not bear out the petitioners' claim that the pictures involved here were part of the statements which were approved by the witnesses and, therefore, producible under § 3500. It appears that all such statements were made on the day of the robbery. At that time, the FBI and police had no pictures of the petitioners. The first pictures were not acquired and shown to the witnesses until the morning of the following day. Hence, they could not possibly have been a part of the statements made and approved by the witnesses the day of the robbery.</p>
<p>The petitioners seem also to suggest that, quite apart from § 3500, the District Court's refusal of their request for the photographs amounted to an abuse of discretion. The photographs were not referred to by the Government in its case-in-chief. They were first asked for by the defense after the direct examination of the first eyewitness, <span class="star-pagination">*388</span> on the second day of the trial. When the defense requested the pictures, counsel for the Government noted that there were a "multitude" of pictures and stated that it might be difficult to identify those which were shown to particular witnesses. However, he indicated that the Government was willing to furnish all of the pictures, if they could be found. The District Court, referring to the fact that production of the photographs was not required under § 3500, stated that it would not stop the trial in order to have the pictures made available.</p>
<p>Although the pictures might have been of some assistance to the defense, and although it doubtless would have been preferable for the Government to have labeled the pictures shown to each witness and kept them available for trial,<sup>[8]</sup> we hold that in the circumstances the refusal of the District Court to order their production did not amount to an abuse of discretion, at least as to petitioner Simmons.<sup>[9]</sup> The defense surely knew that photographs had played a role in the identification process. Yet there was no attempt to have the pictures produced prior to trial pursuant to Fed. Rule Crim. Proc. 16. When production of the pictures was sought at trial, the defense did not explain why they were <span class="star-pagination">*389</span> needed, but simply argued that production was required under § 3500. Moreover, the strength of the eyewitness identifications of Simmons renders it highly unlikely that nonproduction of the photographs caused him any prejudice.</p>
<p></p>
<h2>III.</h2>
<p>Finally, it is contended that it was reversible error to allow the Government to use against Garrett on the issue of guilt the testimony given by him upon his unsuccessful motion to suppress as evidence the suitcase seized from Mrs. Mahon's basement and its contents. That testimony established that Garrett was the owner of the suitcase.<sup>[10]</sup></p>
<p>In order to effectuate the Fourth Amendment's guarantee of freedom from unreasonable searches and seizures, this Court long ago conferred upon defendants in federal prosecutions the right, upon motion and proof, to have excluded from trial evidence which had been secured by means of an unlawful search and seizure. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. More recently, this Court has held that "the exclusionary rule is an essential part of both the Fourth and Fourteenth Amendments. . . ." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#657" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 657</a></span>.</p>
<p>However, we have also held that rights assured by the Fourth Amendment are personal rights, and that they may be enforced by exclusion of evidence only at the instance of one whose own protection was infringed by the search and seizure. See, <i>e. g., </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#260" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 260-261</a></span>. At one time, a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor of <span class="star-pagination">*390</span> the seized property or that he had a possessory interest in the searched premises.<sup>[11]</sup> In part to avoid having to resolve the issue presented by this case, we relaxed those standing requirements in two alternative ways in <i>Jones</i> v. <i>United States, supra</i><i>.</i> First, we held that when, as in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> possession of the seized evidence is itself an essential element of the offense with which the defendant is charged, the Government is precluded from denying that the defendant has the requisite possessory interest to challenge the admission of the evidence. Second, we held alternatively that the defendant need have no possessory interest in the searched premises in order to have standing; it is sufficient that he be legitimately on those premises when the search occurs. Throughout this case, petitioner Garrett has justifiably, and without challenge from the Government, proceeded on the assumption that the standing requirements must be satisfied.<sup>[12]</sup> On that premise, he contends that testimony given by a defendant to meet such requirements should not be admissible against him at trial on the question of guilt or innocence. We agree.</p>
<p>Under the standing rules set out in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> there will be occasions, even in prosecutions for nonpossessory offenses, when a defendant's testimony will be needed to establish standing. This case serves as an example. <span class="star-pagination">*391</span> Garrett evidently was not in Mrs. Mahon's house at the time his suitcase was seized from her basement. The only, or at least the most natural, way in which he could found standing to object to the admission of the suitcase was to testify that he was its owner.<sup>[13]</sup> Thus, his testimony is to be regarded as an integral part of his Fourth Amendment exclusion claim. Under the rule laid down by the courts below, he could give that testimony only by assuming the risk that the testimony would later be admitted against him at trial. Testimony of this kind, which links a defendant to evidence which the Government considers important enough to seize and to seek to have admitted at trial, must often be highly prejudicial to a defendant. This case again serves as an example, for Garrett's admitted ownership of a suitcase which only a few hours after the robbery was found to contain money wrappers taken from the victimized bank was undoubtedly a strong piece of evidence against him. Without his testimony, the Government might have found it hard to prove that he was the owner of the suitcase.<sup>[14]</sup></p>
<p>The dilemma faced by defendants like Garrett is most extreme in prosecutions for possessory crimes, for then the testimony required for standing itself proves an element of the offense. We eliminated that Hobson's choice in <i>Jones</i> v. <i>United States, supra</i><i>,</i> by relaxing the standing requirements. This Court has never considered squarely the question whether defendants charged with nonpossessory crimes, like Garrett, are entitled to be relieved <span class="star-pagination">*392</span> of their dilemma entirely.<sup>[15]</sup> The lower courts which have considered the matter, both before and after <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> have with two exceptions agreed with the holdings of the courts below that the defendant's testimony may be admitted when, as here, the motion to suppress has failed.<sup>[16]</sup> The reasoning of some of these courts would seem to suggest that the testimony would be admissible even if the motion to suppress had succeeded,<sup>[17]</sup> but the only court which has actually decided that question held that when the motion to suppress succeeds the testimony given in support of it is excludable as a "fruit" of the unlawful search.<sup>[18]</sup> The rationale for admitting the testimony when the motion fails has been that the testimony is voluntarily given and relevant, and that it is therefore entitled to admission on the same basis as any other prior testimony or admission of a party.<sup>[19]</sup></p>
<p>It seems obvious that a defendant who knows that his testimony may be admissible against him at trial will sometimes be deterred from presenting the testimonial proof of standing necessary to assert a Fourth Amendment <span class="star-pagination">*393</span> claim. The likelihood of inhibition is greatest when the testimony is known to be admissible regardless of the outcome of the motion to suppress. But even in jurisdictions where the admissibility of the testimony depends upon the outcome of the motion, there will be a deterrent effect in those marginal cases in which it cannot be estimated with confidence whether the motion will succeed. Since search-and-seizure claims depend heavily upon their individual facts,<sup>[20]</sup> and since the law of search and seizure is in a state of flux,<sup>[21]</sup> the incidence of such marginal cases cannot be said to be negligible. In such circumstances, a defendant with a substantial claim for the exclusion of evidence may conclude that the admission of the evidence, together with the Government's proof linking it to him, is preferable to risking the admission of his own testimony connecting himself with the seized evidence.</p>
<p>The rule adopted by the courts below does not merely impose upon a defendant a condition which may deter him from asserting a Fourth Amendment objectionit imposes a condition of a kind to which this Court has always been peculiarly sensitive. For a defendant who wishes to establish standing must do so at the risk that the words which he utters may later be used to incriminate him. Those courts which have allowed the admission of testimony given to establish standing have reasoned that there is no violation of the Fifth Amendment's Self-Incrimination Clause because the testimony was voluntary.<sup>[22]</sup> As an abstract matter, this may well be true. A defendant is "compelled" to testify in support of a motion to suppress only in the sense that if he <span class="star-pagination">*394</span> refrains from testifying he will have to forgo a benefit, and testimony is not always involuntary as a matter of law simply because it is given to obtain a benefit.<sup>[23]</sup> However, the assumption which underlies this reasoning is that the defendant has a choice: he may refuse to testify and give up the benefit.<sup>[24]</sup> When this assumption is applied to a situation in which the "benefit" to be gained is that afforded by another provision of the Bill of Rights, an undeniable tension is created. Thus, in this case Garrett was obliged either to give up what he believed, with advice of counsel, to be a valid Fourth Amendment claim or, in legal effect, to waive his Fifth Amendment privilege against self-incrimination. In these circumstances, we find it intolerable that one constitutional right should have to be surrendered in order to assert another. We therefore hold that when a defendant testifies in support of a motion to suppress evidence on Fourth Amendment grounds, his testimony may not thereafter be admitted against him at trial on the issue of guilt unless he makes no objection.</p>
<p>For the foregoing reasons, we affirm the judgment of the Court of Appeals so far as it relates to petitioner Simmons. We reverse the judgment with respect to petitioner Garrett, and as to him remand the case to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL took no part in the consideration or decision of this case.</p>
<p><span class="star-pagination">*395</span> MR. JUSTICE BLACK, concurring in part and dissenting in part.</p>
<p>I concur in affirmance of the conviction of Simmons but dissent from reversal of Garrett's conviction. I shall first discuss Simmons' case.</p>
<p>1. Simmons' chief claim is that his "pretrial identification [was] so unnecessarily suggestive and conducive to irreparable mistaken identification, that he was denied due process of law." The Court rejects this contention. I agree with the Court but for quite different reasons. The Court's opinion rests on a lengthy discussion of inferences that the jury could have drawn from the evidence of identifying witnesses. A mere summary reading of the evidence as outlined by this Court shows that its discussion is concerned with the weight of the testimony given by the identifying witnesses. The weight of the evidence, however, is not a question for the Court but for the jury, and does not raise a due process issue. The due process question raised by Simmons is, and should be held to be, frivolous. The identifying witnesses were all present in the bank when it was robbed and all saw the robbers. The due process contention revolves around the circumstances under which these witnesses identified pictures of the robbers shown to them, and these circumstances are relevant only to the weight the identification was entitled to be given. The Court, however, considers Simmons' contention on the premise that a denial of due process could be found in the "totality of circumstances" of the picture identification. I do not believe the Due Process Clause or any other constitutional provision vests this Court with any such wide-ranging, uncontrollable power. A trial according to due process of law is a trial according to the "law of the land"the law as enacted by the Constitution or the Legislative Branch of Government, and not "laws" formulated by the courts according to <span class="star-pagination">*396</span> the "totality of the circumstances." Simmons' due process claim here should be denied because it is frivolous.<sup>[*]</sup> For these reasons I vote to affirm Simmons' conviction.</p>
<p>2. I agree with the Court, in part for reasons it assigns, that the District Court did not commit error in declining to permit the photographs used to be turned over to the defense for purposes of cross-examination.</p>
<p>3. The Court makes new law in reversing Garrett's conviction on the ground that it was error to allow the Government to use against him testimony he had given upon his unsuccessful motion to suppress evidence allegedly seized in violation of the Fourth Amendment. The testimony used was Garrett's statement in the suppression hearing that he was the owner of a suitcase which contained money wrappers taken from the bank that was robbed. The Court is certainly guilty of no overstatement in saying that this "was undoubtedly a strong piece of evidence against [Garrett]." <i>Ante,</i> at 391. In fact, one might go further and say that this testimony, along with the statements of the eyewitnesses against him, showed beyond all question that Garrett was one of the bank robbers. The question then is whether the Government is barred from offering a truthful statement made by a defendant at a suppression hearing in order to prevent the defendant from winning an acquittal on the false premise that he is not the owner of the property he has already sworn that he owns. My answer to this question is "No." The Court's answer is "Yes" on the premise that "a defendant who knows that his testimony may be admissible against him at trial will sometimes <span class="star-pagination">*397</span> be deterred from presenting the testimonial proof of standing necessary to assert a Fourth Amendment claim." <i>Ante,</i> at 392-393.</p>
<p>For the Court, though not for me, the question seems to be whether the disadvantages associated with deterring a defendant from testifying on a motion to suppress are significant enough to offset the advantages of permitting the Government to use such testimony when relevant and probative to help convict the defendant of a crime. The Court itself concedes, however, that the deterrent effect on which it relies comes into play, at most, only in "marginal cases" in which the defendant cannot estimate whether the motion to suppress will succeed. <i>Ante,</i> at 393. The value of permitting the Government to use such testimony is, of course, so obvious that it is usually left unstated, but it should not for that reason be ignored. The standard of proof necessary to convict in a criminal case is high, and quite properly so, but for this reason highly probative evidence such as that involved here should not lightly be held inadmissible. For me the importance of bringing guilty criminals to book is a far more crucial consideration than the desirability of giving defendants every possible assistance in their attempts to invoke an evidentiary rule which itself can result in the exclusion of highly relevant evidence.</p>
<p>This leaves for me only the possible contention that Garrett's testimony was inadmissible under the Fifth Amendment because it was compelled. Of course, I could never accept the Court's statement that "testimony is not always involuntary as a matter of law simply because it is given to obtain a benefit." <i>Ante,</i> at 394. No matter what Professor Wigmore may have thought about the subject, it has always been clear to me that any threat of harm or promise of benefit is sufficient to render a defendant's statement involuntary. See <i>Shotwell</i> <span class="star-pagination">*398</span> <i>Mfg. Co.</i> v. <i>United States,</i> <span class="citation" data-id="106512"><a href="/opinion/106512/shotwell-manufacturing-co-v-united-states/#367" aria-description="Citation for case: Shotwell Manufacturing Co. v. United States">371 U. S. 341, 367</a></span> (1963) (dissenting opinion). The reason why the Fifth Amendment poses no bar to acceptance of Garrett's testimony is not, therefore, that a promise of benefit is not generally fatal. Rather, the answer is that the privilege against self-incrimination has always been considered a privilege that can be waived, and the validity of the waiver is, of course, not undermined by the inevitable fact that by testifying, a defendant can obtain the "benefit" of a chance to help his own case by the testimony he gives. When Garrett took the stand at the suppression hearing, he validly surrendered his privilege with respect to the statements he actually made at that time, and since these statements were therefore not "compelled," they could be used against him for any subsequent purpose.</p>
<p>The consequence of the Court's holding, it seems to me, is that defendants are encouraged to come into court, either in person or through other witnesses, and swear falsely that they do not own property, knowing at the very moment they do so that they have already sworn precisely the opposite in a prior court proceeding. This is but to permit lawless people to play ducks and drakes with the basic principles of the administration of criminal law.</p>
<p>There is certainly no language in the Fourth Amendment which gives support to any such device to hobble law enforcement in this country. While our Constitution does provide procedural safeguards to protect defendants from arbitrary convictions, that governmental charter holds out no promises to stultify justice by erecting barriers to the admissibility to relevant evidence voluntarily given in a court of justice. Under the first principles of ethics and morality a defendant who secures a court order by telling the truth should not be allowed to seek a court advantage later based on a premise <span class="star-pagination">*399</span> directly opposite to his prior solemn judicial oath. This Court should not lend the prestige of its high name to such a justice-defeating stratagem. I would affirm Garrett's conviction.</p>
<p>MR. JUSTICE WHITE, concurring in part and dissenting in part.</p>
<p>I concur in Parts I and II of the Court's opinion but dissent from the reversal of Garrett's conviction substantially for the reasons given by MR. JUSTICE BLACK in his separate opinion.</p>
<h2>NOTES</h2>
<p>[1]  Mrs. Mahon also testified that at about 3:30 p. m. the same day six men with guns forced their way into and ransacked her house. However, these men were never identified, and they apparently took nothing.</p>
<p>[2]  See P. Wall, Eye-Witness Identification in Criminal Cases 74-77 (1965).</p>
<p>[3]  See <i>id.,</i> at 82-83.</p>
<p>[4]  See <i>id.,</i> at 68-70.</p>
<p>[5]  See, <i>e. g., </i><i>People</i> v. <i>Evans,</i> <span class="citation" data-id="1178843"><a href="/opinion/1178843/people-v-evans/" aria-description="Citation for case: People v. Evans">39 Cal. 2d 242</a></span>, <span class="citation" data-id="1178843"><a href="/opinion/1178843/people-v-evans/" aria-description="Citation for case: People v. Evans">246 P. 2d 636</a></span>.</p>
<p>[6]  The reliability of the identification procedure could have been increased by allowing only one or two of the five eyewitnesses to view the pictures of Simmons. If thus identified, Simmons could later have been displayed to the other eyewitnesses in a lineup, thus permitting the photographic identification to be supplemented by a corporeal identification, which is normally more accurate. See P. Wall, Eye-Witness Identification in Criminal Cases 83 (1965); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 531. Also, it probably would have been preferable for the witnesses to have been shown more than six snapshots, for those snapshots to have pictured a greater number of individuals, and for there to have been proportionally fewer pictures of Simmons. See Wall, <i>supra,</i> at 74-82; Williams, <i>supra,</i> at 530.</p>
<p>[7]  In the discussion of the bill on the floor of the Senate, Senator O'Mahoney, sponsor of the bill in the Senate, stated that photographs <i>per se</i> were not required to be produced under the bill, but that "[i]f the pictures have anything to do with the statement of the witness . . . of course that would be part of it . . . ." 103 Cong. Rec. 16489.</p>
<p>[8]  See P. Wall, Eye-Witness Identification in Criminal Cases 84 (1965); Williams, Identification Parades, [1955] Crim. L. Rev. 525, 530.</p>
<p>[9]  Garrett was also initially identified from photographs, but at a later date than Simmons. He was identified by fewer witnesses than was Simmons, and even those witnesses had less opportunity to see him during the robbery than they did Simmons. The record is opaque as to the number and type of photographs of Garrett which were shown to these witnesses, and as to the circumstances of the showings. However, it is unnecessary to decide whether Garrett was prejudiced by the District Court's failure to order production of the pictures at trial, since we are reversing Garrett's conviction on other grounds.</p>
<p>[10]  Although petitioner Simmons objected at trial to the admission of Garrett's testimony, the claim was not pressed on his behalf here. Garrett did not mention Simmons in his testimony, and the District Court instructed the jury to consider the testimony only with reference to Garrett.</p>
<p>[11]  See, <i>e. g., </i><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States">362 U. S. 257, at 262</a></span>; Edwards, Standing to Suppress Unreasonably Seized Evidence, <span class="citation no-link">47 Nw. U. L. Rev. 471</span> (1952).</p>
<p>[12]  It has been suggested that the adoption of a "police-deterrent" rationale for the exclusionary rule, see <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>, logically dictates that a defendant should be able to object to the admission against him of <i>any</i> unconstitutionally seized evidence. See Comment, Standing to Object to an Unreasonable Search and Seizure, <span class="citation no-link">34 U. Chi. L. Rev. 342</span> (1967); Note, Standing to Object to an Unlawful Search and Seizure, 1965 Wash. U. L. Q. 488. However, that argument is not advanced in this case, and we do not consider it.</p>
<p>[13]  The record shows that Mrs. Mahon, the owner of the premises from which the suitcase was taken, disclaimed all knowledge of its presence there and of its ownership.</p>
<p>[14]  The Government concedes that there were no identifying marks on the outside of the suitcase. See Brief for the United States 33.</p>
<p>[15]  In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the only reference to the subject was a statement that "[The defendant] has been faced . . . with the chance that the allegations made on the motion to suppress may be used against him at the trial, although that they may is by no means an inevitable holding . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States">362 U. S., at 262</a></span>.</p>
<p>[16]  See <i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>; <i>Kaiser</i> v. <i>United States,</i> <span class="citation" data-id="1542459"><a href="/opinion/1542459/kaiser-v-united-states/" aria-description="Citation for case: Kaiser v. United States">60 F. 2d 410</a></span>; <i>Fowler</i> v. <i>United States,</i> <span class="citation" data-id="240852"><a href="/opinion/240852/harvey-gene-fowler-v-united-states-of-america-two-cases-haskell-d/" aria-description="Citation for case: Harvey Gene Fowler v. United States of America, (Two...">239 F. 2d 93</a></span>; <i>Monroe</i> v. <i>United States,</i> <span class="citation" data-id="261271"><a href="/opinion/261271/henry-monroe-v-united-states/" aria-description="Citation for case: Henry Monroe v. United States">320 F. 2d 277</a></span>; <i>United States</i> v. <i>Taylor,</i> <span class="citation" data-id="262814"><a href="/opinion/262814/united-states-v-gerald-j-taylor-clifton-a-hammond-and-john-w-butler/" aria-description="Citation for case: United States v. Gerald J. Taylor, Clifton A. Hammond,...">326 F. 2d 277</a></span>; <i>United States</i> v. <i>Airdo,</i> <span class="citation" data-id="276553"><a href="/opinion/276553/united-states-v-dominic-daniel-alrdo/" aria-description="Citation for case: United States v. Dominic Daniel Alrdo">380 F. 2d 103</a></span>; <i>United States</i> v. <i>Lindsly,</i> <span class="citation" data-id="1509817"><a href="/opinion/1509817/united-states-v-lindsly/" aria-description="Citation for case: United States v. Lindsly">7 F. 2d 247</a></span>, rev'd on other grounds, <span class="citation" data-id="6832764"><a href="/opinion/6936013/lindsly-v-united-states/" aria-description="Citation for case: Lindsly v. United States">12 F. 2d 771</a></span>. Contra, see <i>Bailey</i> v. <i>United States,</i> 128 U. S. App. D. C. 354, <span class="citation" data-id="8878268"><a href="/opinion/8891974/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">389 F. 2d 305</a></span>; <i>United States</i> v. <i>Lewis,</i> <span class="citation" data-id="1609276"><a href="/opinion/1609276/united-states-v-lewis/#810" aria-description="Citation for case: United States v. Lewis">270 F. Supp. 807, 810, n. 1</a></span> (dictum).</p>
<p>[17]  See, <i>e. g., </i><i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>; <i>Monroe</i> v. <i>United States,</i> <span class="citation" data-id="261271"><a href="/opinion/261271/henry-monroe-v-united-states/" aria-description="Citation for case: Henry Monroe v. United States">320 F. 2d 277</a></span>.</p>
<p>[18]  See <i>Safarik</i> v. <i>United States,</i> <span class="citation" data-id="1472609"><a href="/opinion/1472609/safarik-v-united-states/" aria-description="Citation for case: Safarik v. United States">62 F. 2d 892</a></span>, rehearing denied, <span class="citation" data-id="6854259"><a href="/opinion/6957046/safarik-v-united-states/" aria-description="Citation for case: Safarik v. United States">63 F. 2d 369</a></span>. Accord, <i>Fowler</i> v. <i>United States,</i> <span class="citation" data-id="240852"><a href="/opinion/240852/harvey-gene-fowler-v-united-states-of-america-two-cases-haskell-d/" aria-description="Citation for case: Harvey Gene Fowler v. United States of America, (Two...">239 F. 2d 93</a></span> (dictum); cf. <i>Fabri</i> v. <i>United States,</i> <span class="citation" data-id="6836858"><a href="/opinion/6940021/fabri-v-united-states/" aria-description="Citation for case: Fabri v. United States">24 F. 2d 185</a></span>.</p>
<p>[19]  See cases cited in n. 16, <i>supra.</i></p>
<p>[20]  See, <i>e. g., </i><i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#63" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 63</a></span>.</p>
<p>[21]  <i>E. g.,</i> compare <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, with <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; compare <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, with <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>.</p>
<p>[22]  See, <i>e. g., </i><i>Heller</i> v. <i>United States,</i> <span class="citation" data-id="1569514"><a href="/opinion/1569514/heller-v-united-states/" aria-description="Citation for case: Heller v. United States">57 F. 2d 627</a></span>.</p>
<p>[23]  For example, testimony given for his own benefit by a plaintiff in a civil suit is admissible against him in a subsequent criminal prosecution. See 4 Wigmore, Evidence § 1066 (3d ed. 1940); 8 <i>id.,</i> § 2276 (McNaughton rev. 1961).</p>
<p>[24]  <i>Ibid.</i></p>
<p>[*]  Although Simmons' "questions presented" raise no such contention, the Court declines to use its "supervisory power" to hold Simmons' rights were violated by the identification methods. One must look to the Constitution in vain, I think, to find a "supervisory power" in this Court to reverse cases like this on such a ground.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Skinner v. Railway Labor Executives' Ass'n.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Skinner v. Railway Labor Executives' Ass'n"
type: case
citation: "489 U.S. 602 (1989)"
parallel_cite: "109 S. Ct. 1402; 103 L. Ed. 2d 639; 4 I.E.R. Cas. (BNA) 224; 1989 CCH OSHD 28,476; 57 U.S.L.W. 4324; 13 OSHC (BNA) 2065; 130 L.R.R.M. (BNA) 2857; 49 Empl. Prac. Dec. (CCH) 38,791"
neutral_cite: 1989 U.S. LEXIS 1568
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-03-21
docket: 87-1555
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Skinner v. Railway Labor Executives' Ass'n"
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112219/skinner-v-railway-labor-executives-assn/"
  cluster_id: 112219
  opinion_id: 112219
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[National Treasury Employees Union v. Von Raab]]", "[[Vernonia School District 47J v. Acton]]", "[[Board of Education v. Earls]]", "[[Griffin v. Wisconsin]]", "[[Ferguson v. City of Charleston]]"]
aliases: ["Skinner v. Railway Labor Executives' Assn.", "Skinner v. Railway Labor Executives' Association", "Skinner v. Railway Labor Executives Association"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "administrative-search"]
holding: "Suspicionless drug/alcohol testing of railway employees after accidents is reasonable under the special-needs doctrine."
lake:
  record_id: "Skinner v. Railway Labor Executives' Ass'n"
  status: verified
  projected_at: 2026-07-06
---

# Skinner v. Railway Labor Executives' Ass'n

*489 U.S. 602 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal Railroad Administration regulations required blood and urine testing of railroad employees involved in major accidents, and authorized breath and urine testing on reasonable suspicion of impairment. A railway-labor group challenged the suspicionless post-accident testing as an unreasonable search.

## Issue
Whether suspicionless drug and alcohol testing of railroad employees following accidents is reasonable under the Fourth Amendment as a special-needs search.

## Rule
Where special needs make individualized suspicion impracticable, a search may be reasonable without it. "In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion." — 489 U.S. at 624. ^pin-624

The Court treated railroad-safety regulation as presenting "special needs, beyond the normal need for law enforcement," that justified departing from the warrant and probable-cause requirements.

## Application
The Court found the intrusion of blood and breath tests minimal and the urine-collection procedures regulated to limit intrusiveness, while the government's interest in railroad safety—where an impaired employee's momentary lapse could be catastrophic—was compelling. On that balance, the suspicionless post-accident testing was reasonable without a warrant or individualized suspicion.

## Conclusion
The post-accident toxicological testing program was a reasonable special-needs search and was upheld.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided with its companion [[National Treasury Employees Union v. Von Raab]]; the special-needs framework was applied to schools in [[Vernonia School District 47J v. Acton]] and [[Board of Education v. Earls]] (and to probation in [[Griffin v. Wisconsin]]), and its limit—a programmatic law-enforcement purpose defeats the exception—was drawn in [[Ferguson v. City of Charleston]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Skinner v. Railway Labor Executives' Ass'n*, 489 U.S. 602 (1989) — https://www.courtlistener.com/opinion/112219/skinner-v-railway-labor-executives-assn/ — pinpoint: 624.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0aed2bee852f7122", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Skinner v. Railway Labor Executives' Ass'n"}, "payload": {"all": [{"cite": "489 U.S. 602", "page": "602", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "489"}, {"cite": "109 S. Ct. 1402", "page": "1402", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "103 L. Ed. 2d 639", "page": "639", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "1989 U.S. LEXIS 1568", "page": "1568", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "4 I.E.R. Cas. (BNA) 224", "page": "224", "reporter": "I.E.R. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "4"}, {"cite": "1989 CCH OSHD 28,476", "page": "28,476", "reporter": "CCH OSHD", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "1989"}, {"cite": "57 U.S.L.W. 4324", "page": "4324", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}, {"cite": "13 OSHC (BNA) 2065", "page": "2065", "reporter": "OSHC (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "13"}, {"cite": "130 L.R.R.M. (BNA) 2857", "page": "2857", "reporter": "L.R.R.M. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "130"}, {"cite": "49 Empl. Prac. Dec. (CCH) 38,791", "page": "38,791", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "489 U.S. 602", "official": {"cite": "489 U.S. 602", "page": "602", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "489"}, "official_selection_present": true, "record_id": "Skinner v. Railway Labor Executives' Ass'n"}}
{"assertion_id": "a4b1738cf7b49a21", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-624", "record_id": "Skinner v. Railway Labor Executives' Ass'n"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-624", "pinpoint_status": "slip-only", "quote": "--- # Skinner v. Railway Labor Executives' Ass'n *489 U.S. 602 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal Railroad Administration regulations required blood and urine testing of railroad employees involved in major accidents, and authorized breath and urine testing on reasonable suspicion of impairment. A railway-labor group challenged the suspicionless post-accident testing as an unreasonable search. ## Issue Whether suspicionless drug and alcohol testing of railroad employees following accidents is reasonable under the Fourth Amendment as a special-needs search. ## Rule Where special needs make individualized suspicion impracticable, a search may be reasonable without it.", "quote_fidelity": "mismatch", "record_id": "Skinner v. Railway Labor Executives' Ass'n", "star_marker": null}}
{"assertion_id": "58859da03ca775bd", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Skinner v. Railway Labor Executives' Ass'n"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Skinner v. Railway Labor Executives' Ass'n", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Skinner v. Railway Labor Executives' Ass'n

```json
{
  "schema_version": "s2.v1",
  "record_id": "Skinner v. Railway Labor Executives' Ass'n",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Skinner v. Railway Labor Executives' Assn.",
    "case_name_short": "Skinner",
    "case_name_full": "SKINNER, SECRETARY OF TRANSPORTATION, Et Al. v. RAILWAY LABOR EXECUTIVES\u2019 ASSOCIATION Et Al.",
    "input_case_name": "Skinner v. Railway Labor Executives' Ass'n",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": "87-1555",
    "cluster_id": 112219,
    "lead_opinion_id": 112219,
    "sibling_ids": [
      112219,
      9431606,
      9431607,
      9431608
    ],
    "absolute_url": "/opinion/112219/skinner-v-railway-labor-executives-assn/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 602",
      "volume": "489",
      "reporter": "U.S.",
      "page": "602",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1402",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 639",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 224",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "224",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,476",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,476",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4324",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4324",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 OSHC (BNA) 2065",
        "volume": "13",
        "reporter": "OSHC (BNA)",
        "page": "2065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 L.R.R.M. (BNA) 2857",
        "volume": "130",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2857",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,791",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,791",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1568",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1568",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 602",
        "volume": "489",
        "reporter": "U.S.",
        "page": "602",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1402",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1402",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 639",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1568",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1568",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 224",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "224",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,476",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,476",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4324",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4324",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 OSHC (BNA) 2065",
        "volume": "13",
        "reporter": "OSHC (BNA)",
        "page": "2065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 L.R.R.M. (BNA) 2857",
        "volume": "130",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2857",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,791",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,791",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 602",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 602",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-624",
      "page": null,
      "quote": "--- # Skinner v. Railway Labor Executives' Ass'n *489 U.S. 602 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal Railroad Administration regulations required blood and urine testing of railroad employees involved in major accidents, and authorized breath and urine testing on reasonable suspicion of impairment. A railway-labor group challenged the suspicionless post-accident testing as an unreasonable search. ## Issue Whether suspicionless drug and alcohol testing of railroad employees following accidents is reasonable under the Fourth Amendment as a special-needs search. ## Rule Where special needs make individualized suspicion impracticable, a search may be reasonable without it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Skinner v. Railway Labor Executives' Ass'n",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Bell",
          "cluster_id": 10747468,
          "cite": [
            "2025 ND 201"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Everson v. Leis",
          "cluster_id": 1464717,
          "cite": [
            "556 F.3d 484",
            "2009 U.S. App. LEXIS 3288",
            "2009 WL 414625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Allegheny v. American Civil Liberties Union",
          "cluster_id": 112331,
          "cite": [
            "106 L. Ed. 2d 472",
            "109 S. Ct. 3086",
            "492 U.S. 573",
            "1989 U.S. LEXIS 3468",
            "57 U.S.L.W. 5045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rossignol v. Voorhaar",
          "cluster_id": 2967705,
          "cite": [
            "316 F.3d 516",
            "2003 WL 124775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Parkell v. Carl Danberg",
          "cluster_id": 4248660,
          "cite": [
            "833 F.3d 313",
            "2016 U.S. App. LEXIS 15092",
            "2016 WL 4375620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
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
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Consolidated Rail Corporation v. Railway Labor Executives' Assn.",
          "cluster_id": 112300,
          "cite": [
            "105 L. Ed. 2d 250",
            "109 S. Ct. 2477",
            "491 U.S. 299",
            "1989 U.S. LEXIS 3000",
            "57 U.S.L.W. 4742",
            "131 L.R.R.M. (BNA) 2601",
            "50 Empl. Prac. Dec. (CCH) 39,068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Skinner v. Railway Labor Executives' Ass'n:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDU0MDI1NjAwMDAwJnM9MzE3Mzc0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOTQmcz0xNDY0MzY2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 1,
        "triage_snippet_classified": 41
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112219 OR 9431606 OR 9431607 OR 9431608)",
    "indexed_citing_opinions": 1507,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112219,
        "count": 1348,
        "count_source": "search"
      },
      {
        "opinion_id": 9431606,
        "count": 184,
        "count_source": "search"
      },
      {
        "opinion_id": 9431607,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431608,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2566,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/skinner-v-railway-labor-executives-ass-n.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwOTI5Nzcmcz0xMDI4MzgzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112219+OR+9431606+OR+9431607+OR+9431608%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112219,
        "cited_id": 92312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 96033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 97451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 98973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 99296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 103875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 104914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 337776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 473627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 477827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 480401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 482045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 497255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 497335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 498019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 501767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 502437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 504461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 506184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 1215534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 1908384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2307499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2370062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112219,
        "cited_id": 2372481,
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
    "date_created": "2026-07-05T20:56:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:59:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:57:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Skinner v. Railway Labor Executives' Ass'n (truncated)

```
<div>
<center><b><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602</a></span> (1989)</b></center>
<center><h1>SKINNER, SECRETARY OF TRANSPORTATION, ET AL.<br>
v.<br>
RAILWAY LABOR EXECUTIVES' ASSOCIATION ET AL.</h1></center>
<center>No. 87-1555.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 2, 1988</center>
<center>Decided March 21, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*605</span> <i>Attorney General Thornburgh</i> argued the cause for petitioners. On the briefs were <i>Solicitor General Fried, Assistant Attorney General Bolton, Deputy Solicitor General Merrill, Deputy Assistant Attorneys General Spears</i> and <i>Cynkar, Lawrence S. Robbins, Leonard Schaitman, Marc Richman, B. Wayne Vance, S. Mark Lindsey,</i> and <i>Daniel Carey Smith.</i></p>
<p><i>Lawrence M. Mann</i> argued the cause for respondents. With him on the brief were <i>W. David Holsberry, Harold A. Ross,</i> and <i>Clinton J. Miller III.</i><sup>[*]</sup></p>
<p>Briefs <i>of amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>James D. Holzhauer, John A. Powell, Stephen R. Shapiro, Harvey Grossman,</i> and <i>Edward M. Chen;</i> and for the American Federation of Labor and Congress of Industrial Organizations by <i>David Silberman</i> and <i>Laurence Gold.</i></p>
<p><i>Scott D. Raphael</i> filed a brief for the Aircraft Owners &amp; Pilots Association as <i>amicus curiae.</i></p>
<p><span class="star-pagination">*606</span> JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>The Federal Railroad Safety Act of 1970 authorizes the Secretary of Transportation to "prescribe, as necessary, appropriate rules, regulations, orders, and standards for all areas of railroad safety." <span class="citation no-link">84 Stat. 971</span>, <span class="citation no-link">45 U. S. C. § 431</span>(a). Finding that alcohol and drug abuse by railroad employees poses a serious threat to safety, the Federal Railroad Administration (FRA) has promulgated regulations that mandate blood and urine tests of employees who are involved in certain train accidents. The FRA also has adopted regulations that do not require, but do authorize, railroads to administer breath and urine tests to employees who violate certain safety rules. The question presented by this case is whether these regulations violate the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>The problem of alcohol use on American railroads is as old as the industry itself, and efforts to deter it by carrier rules began at least a century ago. For many years, railroads have prohibited operating employees from possessing alcohol or being intoxicated while on duty and from consuming alcoholic beverages while subject to being called for duty. More recently, these proscriptions have been expanded to forbid possession or use of certain drugs. These restrictions are <span class="star-pagination">*607</span> embodied in "Rule G," an industry-wide operating rule promulgated by the Association of American Railroads, and are enforced, in various formulations, by virtually every railroad in the country. The customary sanction for Rule G violations is dismissal.</p>
<p>In July 1983, the FRA expressed concern that these industry efforts were not adequate to curb alcohol and drug abuse by railroad employees. The FRA pointed to evidence indicating that on-the-job intoxication was a significant problem in the railroad industry.<sup>[1]</sup> The FRA also found, after a review of accident investigation reports, that from 1972 to 1983 "the nation's railroads experienced at least 21 significant train accidents involving alcohol or drug use as a probable cause or contributing factor," and that these accidents "resulted in 25 fatalities, 61 non-fatal injuries, and property damage estimated at $19 million (approximately $27 million in 1982 dollars)." <span class="citation no-link">48 Fed. Reg. 30726</span> (1983). The FRA further identified "an additional 17 fatalities to operating employees working on or around rail rolling stock that involved alcohol or drugs as a contributing factor." <i><span class="citation no-link">Ibid.</span></i> In light of these problems, the FRA solicited comments from interested parties on a various regulatory approaches to the problems of alcohol and drug abuse throughout the Nation's railroad system.</p>
<p>Comments submitted in response to this request indicated that railroads were able to detect a relatively small number of Rule G violations, owing, primarily, to their practice of <span class="star-pagination">*608</span> relying on observation by supervisors and co-workers to enforce the rule. <span class="citation no-link">49 Fed. Reg. 24266</span>-24267 (1984). At the same time, "industry participants . . . confirmed that alcohol and drug use [did] occur on the railroads with unacceptable frequency," and available information from all sources "suggest[ed] that the problem includ[ed] `pockets' of drinking and drug use involving multiple crew members (before and during work), sporadic cases of individuals reporting to work impaired, and repeated drinking and drug use by individual employees who are chemically or psychologically dependent on those substances." <i>Id.,</i> at 24253-24254. "Even without the benefit of regular post-accident testing," the FRA "identified 34 fatalities, 66 injuries and over $28 million in property damage (in 1983 dollars) that resulted from the errors of alcohol and drug-impaired employees in 45 train accidents and train incidents during the period 1975 through 1983." <i>Id.,</i> at 24254. Some of these accidents resulted in the release of hazardous materials and, in one case, the ensuing pollution required the evacuation of an entire Louisiana community. <i>Id.,</i> at 24254, 24259. In view of the obvious safety hazards of drug and alcohol use by railroad employees, the FRA announced in June 1984 its intention to promulgate federal regulations on the subject.</p>
<p></p>
<h2>B</h2>
<p>After reviewing further comments from representatives of the railroad industry, labor groups, and the general public, the FRA, in 1985, promulgated regulations addressing the problem of alcohol and drugs on the railroads. The final regulations apply to employees assigned to perform service subject to the Hours of Service Act, ch. 2939, <span class="citation no-link">34 Stat. 1415</span>, as amended, <span class="citation no-link">45 U. S. C. § 61</span> <i>et seq.</i> The regulations prohibit covered employees from using or possessing alcohol or any controlled substance. <span class="citation no-link">49 CFR § 219.101</span>(a)(1) (1987). The regulations further prohibit those employees from reporting for covered service while under the influence of, or <span class="star-pagination">*609</span> impaired by, alcohol, while having a blood alcohol concentration of 0.04 or more, or while under the influence of, or impaired by, any controlled substance. § 219.101(a)(2). The regulations do not restrict, however, a railroad's authority to impose an absolute prohibition on the presence of alcohol or any drug in the body fluids of persons in its employ, § 219.101(c), and, accordingly, they do not "replace Rule G or render it unenforceable." <span class="citation no-link">50 Fed. Reg. 31538</span> (1985).</p>
<p>To the extent pertinent here, two subparts of the regulations relate to testing. Subpart C, which is entitled "Post-Accident Toxicological Testing," is mandatory. It provides that railroads "shall take all practicable steps to assure that all covered employees of the railroad directly involved . . . provide blood and urine samples for toxicological testing by FRA," § 219.203(a), upon the occurrence of certain specified events. Toxicological testing is required following a "major train accident," which is defined as any train accident that involves (i) a fatality, (ii) the release of hazardous material accompanied by an evacuation or a reportable injury, or (iii) damage to railroad property of $500,000 or more. § 219.201 (a)(1). The railroad has the further duty of collecting blood and urine samples for testing after an "impact accident," which is defined as a collision that results in a reportable injury, or in damage to railroad property of $50,000 or more. § 219.201(a)(2). Finally, the railroad is also obligated to test after "[a]ny train incident that involves a fatality to any on-duty railroad employee." § 219.201(a)(3).</p>
<p>After occurrence of an event which activates its duty to test, the railroad must transport all crew members and other covered employees directly involved in the accident or incident to an independent medical facility, where both blood and urine samples must be obtained from each employee.<sup>[2]</sup> After <span class="star-pagination">*610</span> the samples have been collected, the railroad is required to ship them by prepaid air freight to the FRA laboratory for analysis. § 219.205(d). There, the samples are analyzed using "state-of-the-art equipment and techniques" to detect and measure alcohol and drugs.<sup>[3]</sup> The FRA proposes to place primary reliance on analysis of blood samples, as blood is "the only available body fluid . . . that can provide a clear indication not only of the presence of alcohol and drugs but also their current impairment effects." <span class="citation no-link">49 Fed. Reg. 24291</span> (1984). Urine samples are also necessary, however, because drug traces remain in the urine longer than in blood, and in some cases it will not be possible to transport employees to a medical facility before the time it takes for certain drugs to be eliminated from the bloodstream. In those instances, a "positive urine test, taken with specific information on the pattern of elimination for the particular drug and other information on the behavior of the employee and the circumstances of the accident, may be crucial to the determination of" the cause of an accident. <i><span class="citation no-link">Ibid.</span></i></p>
<p>The regulations require that the FRA notify employees of the results of the tests and afford them an opportunity to respond in writing before preparation of any final investigative report. See § 219.211(a)(2). Employees who refuse to provide required blood or urine samples may not perform covered <span class="star-pagination">*611</span> service for nine months, but they are entitled to a hearing concerning their refusal to take the test. § 219.213.</p>
<p>Subpart D of the regulations, which is entitled "Authorization to Test for Cause," is permissive. It authorizes railroads to require covered employees to submit to breath or urine tests in certain circumstances not addressed by Subpart C. Breath or urine tests, or both, may be ordered (1) after a reportable accident or incident, where a supervisor has a "reasonable suspicion" that an employee's acts or omissions contributed to the occurrence or severity of the accident or incident, § 219.301(b)(2); or (2) in the event of certain specific rule violations, including noncompliance with a signal and excessive speeding, § 219.301(b)(3). A railroad also may require breath tests where a supervisor has a "reasonable suspicion" that an employee is under the influence of alcohol, based upon specific, personal observations concerning the appearance, behavior, speech, or body odors of the employee. § 219.301(b)(1). Where impairment is suspected, a railroad, in addition, may require urine tests, but only if two supervisors make the appropriate determination, § 219.301(c)(2)(i), and, where the supervisors suspect impairment due to a substance other than alcohol, at least one of those supervisors must have received specialized training in detecting the signs of drug intoxication, § 219.301(c)(2)(ii).</p>
<p>Subpart D further provides that whenever the results of either breath or urine tests are intended for use in a disciplinary proceeding, the employee must be given the opportunity to provide a blood sample for analysis at an independent medical facility. § 219.303(c). If an employee declines to give a blood sample, the railroad may presume impairment, absent persuasive evidence to the contrary, from a positive showing of controlled substance residues in the urine. The railroad must, however, provide detailed notice of this presumption to its employees, and advise them of their right to provide a contemporaneous blood sample. As in the case of samples procured under Subpart C, the regulations set forth <span class="star-pagination">*612</span> procedures for the collection of samples, and require that samples "be analyzed by a method that is reliable within known tolerances." § 219.307(b).</p>
<p></p>
<h2>C</h2>
<p>Respondents, the Railway Labor Executives' Association and various of its member labor organizations, brought the instant suit in the United States District Court for the Northern District of California, seeking to enjoin the FRA's regulations on various statutory and constitutional grounds. In a ruling from the bench, the District Court granted summary judgment in petitioners' favor. The court concluded that railroad employees "have a valid interest in the integrity of their own bodies" that deserved protection under the Fourth Amendment. App. to Pet. for Cert. 53a. The court held, however, that this interest was outweighed by the competing "public and governmental interest in the . . . promotion of. . . railway safety, safety for employees, and safety for the general public that is involved with the transportation." <i>Id.,</i> at 52a. The District Court found respondents' other constitutional and statutory arguments meritless.</p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed. <i>Railway Labor Executives' Assn.</i> v. <i>Burnley,</i> <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d 575</a></span> (1988). The court held, first, that tests mandated by a railroad in reliance on the authority conferred by Subpart D involve sufficient Government action to implicate the Fourth Amendment, and that the breath, blood, and urine tests contemplated by the FRA regulations are Fourth Amendment searches. The court also "agre[ed] that the exigencies of testing for the presence of alcohol and drugs in blood, urine or breath require prompt action which precludes obtaining a warrant." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#583" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 583</a></span>. The court further held that "accommodation of railroad employees' privacy interest with the significant safety concerns of the government does not require adherence to a probable cause requirement," and, accordingly, that the legality of the searches contemplated by <span class="star-pagination">*613</span> the FRA regulations depends on their reasonableness under all the circumstances. <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#587" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 587</a></span>.</p>
<p>The court concluded, however, that particularized suspicion is essential to a finding that toxicological testing of railroad employees is reasonable. <i><span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">Ibid.</a></span></i> A requirement of individualized suspicion, the court stated, would impose "no insuperable burden on the government," <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>id.,</i> at 588</a></span>, and would ensure that the tests are confined to the detection of current impairment, rather than to the discovery of "the metabolites of various drugs, which are not evidence of current intoxication and may remain in the body for days or weeks after the ingestion of the drug." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 588-589</a></span>. Except for the provisions authorizing breath and urine tests on a "reasonable suspicion" of drug or alcohol impairment, <span class="citation no-link">49 CFR §§ 219.301</span>(b)(1) and (c)(2) (1987), the FRA regulations did not require a showing of individualized suspicion, and, accordingly, the court invalidated them.</p>
<p>Judge Alarcon dissented. He criticized the majority for "fail[ing] to engage in [a] balancing of interests" and for focusing instead "solely on the degree of impairment of the workers' privacy interests." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#597" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 597</a></span>. The dissent would have held that "the government's compelling need to assure railroad safety by controlling drug use among railway personnel outweighs the need to protect privacy interests." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#596" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 596</a></span>.</p>
<p>We granted the federal parties' petition for a writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./486/1042/">486 U. S. 1042</a></span> (1988), to consider whether the regulations invalidated by the Court of Appeals violate the Fourth Amendment. We now reverse.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." The Amendment guarantees the privacy, dignity, and security of persons against certain arbitrary <span class="star-pagination">*614</span> and invasive acts by officers of the Government or those acting at their direction. <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). See also <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-654</a></span> (1979); <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976). Before we consider whether the tests in question are reasonable under the Fourth Amendment, we must inquire whether the tests are attributable to the Government or its agents, and whether they amount to searches or seizures. We turn to those matters.</p>
<p></p>
<h2>A</h2>
<p>Although the Fourth Amendment does not apply to a search or seizure, even an arbitrary one, effected by a private party on his own initiative, the Amendment protects against such intrusions if the private party acted as an instrument or agent of the Government. See <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113-114</a></span> (1984); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 487</a></span> (1971). See also <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475</a></span> (1921). A railroad that complies with the provisions of Subpart C of the regulations does so by compulsion of sovereign authority, and the lawfulness of its acts is controlled by the Fourth Amendment. Petitioners contend, however, that the Fourth Amendment is not implicated by Subpart D of the regulations, as nothing in Subpart D compels any testing by private railroads.</p>
<p>We are unwilling to conclude, in the context of this facial challenge, that breath and urine tests required by private railroads in reliance on Subpart D will not implicate the Fourth Amendment. Whether a private party should be deemed an agent or instrument of the Government for Fourth Amendment purposes necessarily turns on the degree of the Government's participation in the private party's activities, cf. <i>Lustig</i> v. <i>United States,</i> <span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#78" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 78-79</a></span> (1949) (plurality opinion); <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#32" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 32-33</a></span> (1927), a question that can only be resolved "in light of all the circumstances," <i>Coolidge</i> v. <i>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span></i> <span class="star-pagination">*615</span> at 487. The fact that the Government has not compelled a private party to perform a search does not, by itself, establish that the search is a private one. Here, specific features of the regulations combine to convince us that the Government did more than adopt a passive position toward the underlying private conduct.</p>
<p>The regulations, including those in Subpart D, pre-empt state laws, rules, or regulations covering the same subject matter, <span class="citation no-link">49 CFR § 219.13</span>(a) (1987), and are intended to supersede "any provision of a collective bargaining agreement, or arbitration award construing such an agreement," <span class="citation no-link">50 Fed. Reg. 31552</span> (1985). They also confer upon the FRA the right to receive certain biological samples and test results procured by railroads pursuant to Subpart D. § 219.11(c). In addition, a railroad may not divest itself of, or otherwise compromise by contract, the authority conferred by Subpart D. As the FRA explained, such "authority . . . is conferred for the purpose of promoting the public safety, and a railroad may not shackle itself in a way inconsistent with its duty to promote the public safety." <span class="citation no-link">50 Fed. Reg. 31552</span> (1985). Nor is a covered employee free to decline his employer's request to submit to breath or urine tests under the conditions set forth in Subpart D. See § 219.11(b). An employee who refuses to submit to the tests must be withdrawn from covered service. See 4 App. to Field Manual 18.</p>
<p>In light of these provisions, we are unwilling to accept petitioners' submission that tests conducted by private railroads in reliance on Subpart D will be primarily the result of private initiative. The Government has removed all legal barriers to the testing authorized by Subpart D, and indeed has made plain not only its strong preference for testing, but also its desire to share the fruits of such intrusions. In addition, it has mandated that the railroads not bargain away the authority to perform tests granted by Subpart D. These are clear indices of the Government's encouragement, endorsement, <span class="star-pagination">*616</span> and participation, and suffice to implicate the Fourth Amendment.</p>
<p></p>
<h2>B</h2>
<p>Our precedents teach that where, as here, the Government seeks to obtain physical evidence from a person, the Fourth Amendment may be relevant at several levels. See, <i>e. g., </i><i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#8" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 8</a></span> (1973). The initial detention necessary to procure the evidence may be a seizure of the person, <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969), if the detention amounts to a meaningful interference with his freedom of movement. <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984); <i>United States</i> v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><i>Jacobsen, supra,</i> at 113, n. 5</a></span>. Obtaining and examining the evidence may also be a search, see <i>Cupp</i> v. <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy"><i>Murphy, supra,</i> at 295</a></span>; <i>United States</i> v. <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#8" aria-description="Citation for case: United States v. Dionisio"><i>Dionisio, supra,</i> at 8, 13-14</a></span>, if doing so infringes an expectation of privacy that society is prepared to recognize as reasonable, see, <i>e. g., </i><i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#43" aria-description="Citation for case: California v. Greenwood">486 U. S. 35, 43</a></span> (1988); <i>United States</i> v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><i>Jacobsen, supra,</i> at 113</a></span>.</p>
<p>We have long recognized that a "compelled intrusio[n] into the body for blood to be analyzed for alcohol content" must be deemed a Fourth Amendment search. See <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 767-768</a></span> (1966). See also <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 760</a></span> (1985). In light of our society's concern for the security of one's person, see, <i>e. g., </i><i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968), it is obvious that this physical intrusion, penetrating beneath the skin, infringes an expectation of privacy that society is prepared to recognize as reasonable. The ensuing chemical analysis of the sample to obtain physiological data is a further invasion of the tested employee's privacy interests. Cf. <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#324" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 324-325</a></span> (1987). Much the same is true of the breath-testing procedures required under Subpart D of the regulations. Subjecting a person to a breathalyzer test, which generally requires the production of alveolar or "deep lung" breath for chemical analysis, see, <i>e. g., </i><i>California</i> v. <span class="star-pagination">*617</span> <i>Trombetta,</i> <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#481" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 481</a></span> (1984), implicates similar concerns about bodily integrity and, like the blood-alcohol test we considered in <i>Schmerber,</i> should also be deemed a search, see 1 W. LaFave, Search and Seizure § 2.6(a), p. 463 (1987). See also <i>Burnett</i> v. <i>Anchorage,</i> <span class="citation" data-id="480401"><a href="/opinion/480401/peter-burnett-and-daniel-c-ryan-v-municipality-of-anchorage-raymond-roop/#1449" aria-description="Citation for case: Peter Burnett and Daniel C. Ryan v. Municipality of...">806 F. 2d 1447, 1449</a></span> (CA9 1986); <i>Shoemaker</i> v. <i>Handel,</i> <span class="citation" data-id="473627"><a href="/opinion/473627/shoemaker-v-handel/#1141" aria-description="Citation for case: Shoemaker v. Handel">795 F. 2d 1136, 1141</a></span> (CA3), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./479/986/">479 U. S. 986</a></span> (1986).</p>
<p>Unlike the blood-testing procedure at issue in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> the procedures prescribed by the FRA regulations for collecting and testing urine samples do not entail a surgical intrusion into the body. It is not disputed, however, that chemical analysis of urine, like that of blood, can reveal a host of private medical facts about an employee, including whether he or she is epileptic, pregnant, or diabetic. Nor can it be disputed that the process of collecting the sample to be tested, which may in some cases involve visual or aural monitoring of the act of urination, itself implicates privacy interests. As the Court of Appeals for the Fifth Circuit has stated:</p>
<blockquote>"There are few activities in our society more personal or private than the passing of urine. Most people describe it by euphemisms if they talk about it at all. It is a function traditionally performed without public observation; indeed, its performance in public is generally prohibited by law as well as social custom." <i>National Treasury Employees Union</i> v. <i>Von Raab,</i> <span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-v-raab/#175" aria-description="Citation for case: National Treasury Employees Union v. Raab">816 F. 2d 170, 175</a></span> (1987).</blockquote>
<p>Because it is clear that the collection and testing of urine intrudes upon expectations of privacy that society has long recognized as reasonable, the Federal Courts of Appeals have concluded unanimously, and we agree, that these intrusions must be deemed searches under the Fourth Amendment.<sup>[4]</sup></p>
<p><span class="star-pagination">*618</span> In view of our conclusion that the collection and subsequent analysis of the requisite biological samples must be deemed Fourth Amendment searches, we need not characterize the employer's antecedent interference with the employee's freedom of movement as an independent Fourth Amendment seizure. As our precedents indicate, not every governmental interference with an individual's freedom of movement raises such constitutional concerns that there is a seizure of the person. See <i>United States</i> v. <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#9" aria-description="Citation for case: United States v. Dionisio"><i>Dionisio, supra,</i> at 9-11</a></span> (grand jury subpoena, though enforceable by contempt, does not effect a seizure of the person); <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#21" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 21</a></span> (1973) (same). For present purposes, it suffices to note that any limitation on an employee's freedom of movement that is necessary to obtain the blood, urine, or breath samples contemplated by the regulations must be considered in assessing the intrusiveness of the searches effected by the Government's testing program. Cf. <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707-709</a></span> (1983).</p>
<p></p>
<h2>III</h2>
<p></p>
<h2>A</h2>
<p>To hold that the Fourth Amendment is applicable to the drug and alcohol testing prescribed by the FRA regulations <span class="star-pagination">*619</span> is only to begin the inquiry into the standards governing such intrusions. <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#719" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 719</a></span> (1987) (plurality opinion); <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 337</a></span> (1985). For the Fourth Amendment does not proscribe all searches and seizures, but only those that are unreasonable. <i>United States</i> v. <i>Sharpe,</i> <span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/#682" aria-description="Citation for case: United States v. Sharpe">470 U. S. 675, 682</a></span> (1985); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California">384 U. S., at 768</a></span>. What is reasonable, of course, "depends on all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself." <i>United States</i> v. <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#537" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 537</a></span> (1985). Thus, the permissibility of a particular practice "is judged by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests." <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 654</a></span>; <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976).</p>
<p>In most criminal cases, we strike this balance in favor of the procedures described by the Warrant Clause of the Fourth Amendment. See <i>United States</i> v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 701</a></span>, and n. 2; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315</a></span> (1972). Except in certain well-defined circumstances, a search or seizure in such a case is not reasonable unless it is accomplished pursuant to a judicial warrant issued upon probable cause. See, <i>e. g., </i><i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980); <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978). We have recognized exceptions to this rule, however, "when `special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.' " <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987), quoting <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 351 (BLACKMUN, J., concurring in judgment). When faced with such special needs, we have not hesitated to balance the governmental and privacy interests to assess the practicality of the warrant and probable-cause requirements in the particular context. See, <i>e. g., </i><i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 873</a></span> (search of probationer's home); <i>New York</i> v. <span class="star-pagination">*620</span> <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#699" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 699-703</a></span> (1987) (search of premises of certain highly regulated businesses); <i>O'Connor</i> v. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#721" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><i>Ortega, supra,</i> at 721-725</a></span> (work-related searches of employees' desks and offices); <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 337-342 (search of student's property by school officials); <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#558" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 558-560</a></span> (1979) (body cavity searches of prison inmates).</p>
<p>The Government's interest in regulating the conduct of railroad employees to ensure safety, like its supervision of probationers or regulated industries, or its operation of a government office, school, or prison, "likewise presents `special needs' beyond normal law enforcement that may justify departures from the usual warrant and probable-cause requirements." <i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 873-874</a></span>. The hours of service employees covered by the FRA regulations include persons engaged in handling orders concerning train movements, operating crews, and those engaged in the maintenance and repair of signal systems. <span class="citation no-link">50 Fed. Reg. 31511</span> (1985). It is undisputed that these and other covered employees are engaged in safety-sensitive tasks. The FRA so found, and respondents conceded the point at oral argument. Tr. of Oral Arg. 46-47. As we have recognized, the whole premise of the Hours of Service Act is that "[t]he length of hours of service has direct relation to the efficiency of the human agencies upon which protection [of] life and property necessarily depends." <i>Baltimore &amp; Ohio R. Co.</i> v. <i>ICC,</i> <span class="citation" data-id="8142539"><a href="/opinion/8180620/baltimore-ohio-railroad-v-interstate-commerce-commission/#619" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Interstate Commerce Commission">221 U. S. 612, 619</a></span> (1911). See also <i>Atchison, T. &amp; S. F. R. Co.</i> v. <i>United States,</i> <span class="citation" data-id="98973"><a href="/opinion/98973/atchison-topeka-santa-fe-railway-co-v-united-states/#342" aria-description="Citation for case: Atchison, Topeka &amp; Santa Fe Railway Co. v. United States">244 U. S. 336, 342</a></span> (1917) ("[I]t must be remembered that the purpose of the act was to prevent the dangers which must necessarily arise to the employee and to the public from continuing men in a dangerous and hazardous business for periods so long as to render them unfit to give that service which is essential to the protection of themselves and those entrusted to their care").</p>
<p>The FRA has prescribed toxicological tests, not to assist in the prosecution of employees, but rather "to prevent accidents <span class="star-pagination">*621</span> and casualties in railroad operations that result from impairment of employees by alcohol or drugs." <span class="citation no-link">49 CFR § 219.1</span>(a) (1987).<sup>[5]</sup> This governmental interest in ensuring the safety of the traveling public and of the employees themselves plainly justifies prohibiting covered employees from using alcohol or drugs on duty, or while subject to being called for duty. This interest also "require[s] and justif[ies] the exercise of supervision to assure that the restrictions are in fact observed." <i>Griffin</i> v. <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#875" aria-description="Citation for case: Griffin v. Wisconsin"><i>Wisconsin, supra,</i> at 875</a></span>. The question that remains, then, is whether the Government's need to monitor compliance with these restrictions justifies the privacy intrusions at issue absent a warrant or individualized suspicion.</p>
<p></p>
<h2>B</h2>
<p>An essential purpose of a warrant requirement is to protect privacy interests by assuring citizens subject to a search <span class="star-pagination">*622</span> or seizure that such intrusions are not the random or arbitrary acts of government agents. A warrant assures the citizen that the intrusion is authorized by law, and that it is narrowly limited in its objectives and scope. See, <i>e. g., </i><i>New York</i> v. <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#703" aria-description="Citation for case: New York v. Burger"><i>Burger, supra,</i> at 703</a></span>; <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977); <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>. A warrant also provides the detached scrutiny of a neutral magistrate, and thus ensures an objective determination whether an intrusion is justified in any given case. See <i>United States</i> v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 9</a></span>. In the present context, however, a warrant would do little to further these aims. Both the circumstances justifying toxicological testing and the permissible limits of such intrusions are defined narrowly and specifically in the regulations that authorize them, and doubtless are well known to covered employees. Cf. <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S. 311, 316</a></span> (1972). Indeed, in light of the standardized nature of the tests and the minimal discretion vested in those charged with administering the program, there are virtually no facts for a neutral magistrate to evaluate. Cf. <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#376" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 376</a></span> (1987) (BLACKMUN, J., concurring).<sup>[6]</sup></p>
<p><span class="star-pagination">*623</span> We have recognized, moreover, that the government's interest in dispensing with the warrant requirement is at its strongest when, as here, "the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search." <i>Camara</i> v. <i>Municipal Court of San Francisco, supra,</i> at 533. See also <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span>; <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#603" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 603</a></span> (1981). As the FRA recognized, alcohol and other drugs are eliminated from the bloodstream at a constant rate, see <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), and blood and breath samples taken to measure whether these substances were in the bloodstream when a triggering event occurred must be obtained as soon as possible. See <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S., at 770-771</a></span>. Although the metabolites of some drugs remain in the urine for longer periods of time and may enable the FRA to estimate whether the employee was impaired by those drugs at the time of a covered accident, incident, or rule violation, <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), the delay necessary to procure a warrant nevertheless may result in the destruction of valuable evidence.</p>
<p>The Government's need to rely on private railroads to set the testing process in motion also indicates that insistence on a warrant requirement would impede the achievement of the Government's objective. Railroad supervisors, like school officials, see <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 339-340, and hospital administrators, see <i>O'Connor</i> v. <i>Ortega,</i> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#722" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 722</a></span>, are not in the business of investigating violations of the criminal laws or enforcing administrative codes, and otherwise have little occasion to become familiar with the intricacies of this Court's Fourth Amendment jurisprudence. "Imposing unwieldy warrant procedures . . . upon supervisors, <span class="star-pagination">*624</span> who would otherwise have no reason to be familiar with such procedures, is simply unreasonable." <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">Ibid.</a></span></i></p>
<p>In sum, imposing a warrant requirement in the present context would add little to the assurances of certainty and regularity already afforded by the regulations, while significantly hindering, and in many cases frustrating, the objectives of the Government's testing program. We do not believe that a warrant is essential to render the intrusions here at issue reasonable under the Fourth Amendment.</p>
<p></p>
<h2>C</h2>
<p>Our cases indicate that even a search that may be performed without a warrant must be based, as a general matter, on probable cause to believe that the person to be searched has violated the law. See <i>New Jersey</i> v. <i>T. L. O., supra,</i> at 340. When the balance of interests precludes insistence on a showing of probable cause, we have usually required "some quantum of individualized suspicion" before concluding that a search is reasonable. See, <i>e. g., </i><i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span>. We made it clear, however, that a showing of individualized suspicion is not a constitutional floor, below which a search must be presumed unreasonable. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 561</a></span>. In limited circumstances, where the privacy interests implicated by the search are minimal, and where an important governmental interest furthered by the intrusion would be placed in jeopardy by a requirement of individualized suspicion, a search may be reasonable despite the absence of such suspicion. We believe this is true of the intrusions in question here.</p>
<p>By and large, intrusions on privacy under the FRA regulations are limited. To the extent transportation and like restrictions are necessary to procure the requisite blood, breath, and urine samples for testing, this interference alone is minimal given the employment context in which it takes place. Ordinarily, an employee consents to significant restrictions in his freedom of movement where necessary for <span class="star-pagination">*625</span> his employment, and few are free to come and go as they please during working hours. See, <i>e. g., </i><i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#218" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 218</a></span>. Any additional interference with a railroad employee's freedom of movement that occurs in the time it takes to procure a blood, breath, or urine sample for testing cannot, by itself, be said to infringe significant privacy interests.</p>
<p>Our decision in <i>Schmerber</i> v. <i>California, supra</i><i>,</i> indicates that the same is true of the blood tests required by the FRA regulations. In that case, we held that a State could direct that a blood sample be withdrawn from a motorist suspected of driving while intoxicated, despite his refusal to consent to the intrusion. We noted that the test was performed in a reasonable manner, as the motorist's "blood was taken by a physician in a hospital environment according to accepted medical practices." <i>Id.,</i> at 771. We said also that the intrusion occasioned by a blood test is not significant, since such "tests are a commonplace in these days of periodic physical examinations and experience with them teaches that the quantity of blood extracted is minimal, and that for most people the procedure involves virtually no risk, trauma, or pain." <i>Ibid. Schmerber</i> thus confirmed "society's judgment that blood tests do not constitute an unduly extensive imposition on an individual's privacy and bodily integrity." <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#762" aria-description="Citation for case: Winston v. Lee">470 U. S., at 762</a></span>. See also <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#563" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 563</a></span> (1983) ("The simple blood-alcohol test is . . . safe, painless, and commonplace"); <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#436" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 436</a></span> (1957) ("The blood test procedure has become routine in our everyday life").</p>
<p>The breath tests authorized by Subpart D of the regulations are even less intrusive than the blood tests prescribed by Subpart C. Unlike blood tests, breath tests do not require piercing the skin and may be conducted safely outside a hospital environment and with a minimum of inconvenience or embarrassment. Further, breath tests reveal the level of alcohol in the employee's bloodstream and nothing more. <span class="star-pagination">*626</span> Like the blood-testing procedures mandated by Subpart C, which can be used only to ascertain the presence of alcohol or controlled substances in the bloodstream, breath tests reveal no other facts in which the employee has a substantial privacy interest. Cf. <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#123" aria-description="Citation for case: United States v. Jacobsen">466 U. S., at 123</a></span>; <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S., at 707</a></span>. In all the circumstances, we cannot conclude that the administration of a breath test implicates significant privacy concerns.</p>
<p>A more difficult question is presented by urine tests. Like breath tests, urine tests are not invasive of the body and, under the regulations, may not be used as an occasion for inquiring into private facts unrelated to alcohol or drug use.<sup>[7]</sup> We recognize, however, that the procedures for collecting the necessary samples, which require employees to perform an excretory function traditionally shielded by great privacy, raise concerns not implicated by blood or breath tests. While we would not characterize these additional privacy concerns as minimal in most contexts, we note that the regulations endeavor to reduce the intrusiveness of the collection process. The regulations do not require that samples be furnished under the direct observation of a monitor, despite the desirability of such a procedure to ensure the integrity of the sample. See <span class="citation no-link">50 Fed. Reg. 31555</span> (1985). See also Field Manual B-15, D-1. The sample is also collected in a medical environment, by personnel unrelated to the railroad <span class="star-pagination">*627</span> employer, and is thus not unlike similar procedures encountered often in the context of a regular physical examination.</p>
<p>More importantly, the expectations of privacy of covered employees are diminished by reason of their participation in an industry that is regulated pervasively to ensure safety, a goal dependent, in substantial part, on the health and fitness of covered employees. This relation between safety and employee fitness was recognized by Congress when it enacted the Hours of Service Act in 1907, <i>Baltimore &amp; Ohio R. Co.</i> v. <i>ICC,</i> <span class="citation" data-id="8142539"><a href="/opinion/8180620/baltimore-ohio-railroad-v-interstate-commerce-commission/#619" aria-description="Citation for case: Baltimore &amp; Ohio Railroad v. Interstate Commerce Commission">221 U. S., at 619</a></span>, and also when it authorized the Secretary to "test . . . railroad facilities, equipment, rolling stock, operations, <i>or persons,</i> as he deems necessary to carry out the provisions" of the Federal Railroad Safety Act of 1970. <span class="citation no-link">45 U. S. C. § 437</span>(a) (emphasis added). It has also been recognized by state governments,<sup>[8]</sup> and has long been reflected in industry practice, as evidenced by the industry's promulgation and enforcement of Rule G. Indeed, the FRA found, and the Court of Appeals acknowledged, see <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#585" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 585</a></span>, that "most railroads require periodic physical examinations for train and engine employees and certain other employees." <span class="citation no-link">49 Fed. Reg. 24278</span> (1984). See also <i>Railway Labor Executives Assn.</i> v. <i>Norfolk &amp; Western R. Co.,</i> <span class="citation" data-id="497335"><a href="/opinion/497335/railway-labor-executives-association-v-norfolk-and-western-railway-company/#705" aria-description="Citation for case: Railway Labor Executives Association v. Norfolk and...">833 F. 2d 700, 705-706</a></span> (CA7 1987); <i>Brotherhood of Maintenance of</i> <span class="star-pagination">*628</span> <i>Way Employees, Lodge 16</i> v. <i>Burlington Northern R. Co.,</i> <span class="citation" data-id="477827"><a href="/opinion/477827/brotherhood-of-maintenance-of-way-employees-lodge-16-v-burlington/#1024" aria-description="Citation for case: Brotherhood Of Maintenance Of Way Employees, Lodge 16 v....">802 F. 2d 1016, 1024</a></span> (CA8 1986).</p>
<p>We do not suggest, of course, that the interest in bodily security enjoyed by those employed in a regulated industry must always be considered minimal. Here, however, the covered employees have long been a principal focus of regulatory concern. As the dissenting judge below noted: "The reason is obvious. An idle locomotive, sitting in the round-house, is harmless. It becomes lethal when operated negligently by persons who are under the influence of alcohol or drugs." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#593" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 593</a></span>. Though some of the privacy interests implicated by the toxicological testing at issue reasonably might be viewed as significant in other contexts, logic and history show that a diminished expectation of privacy attaches to information relating to the physical condition of covered employees and to this reasonable means of procuring such information. We conclude, therefore, that the testing procedures contemplated by Subparts C and D pose only limited threats to the justifiable expectations of privacy of covered employees.</p>
<p>By contrast, the Government interest in testing without a showing of individualized suspicion is compelling. Employees subject to the tests discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences. Much like persons who have routine access to dangerous nuclear power facilities, see, <i>e. g., </i><i>Rushton</i> v. <i>Nebraska Public Power Dist.,</i> <span class="citation" data-id="504461"><a href="/opinion/504461/warren-h-rushton-and-david-l-lostroh-v-nebraska-public-power-district/#566" aria-description="Citation for case: Warren H. Rushton and David L. Lostroh v. Nebraska Public...">844 F. 2d 562, 566</a></span> (CA8 1988); <i>Alverado</i> v. <i>Washington Public Power Supply System,</i> <span class="citation" data-id="1215534"><a href="/opinion/1215534/alverado-v-washington-public-power-supply-system/#436" aria-description="Citation for case: Alverado v. Washington Public Power Supply System">111 Wash. 2d 424, 436</a></span>, <span class="citation" data-id="1215534"><a href="/opinion/1215534/alverado-v-washington-public-power-supply-system/#433" aria-description="Citation for case: Alverado v. Washington Public Power Supply System">759 P. 2d 427, 433-434</a></span> (1988), cert. pending, No. 88-645, employees who are subject to testing under the FRA regulations can cause great human loss before any signs of impairment become noticeable to supervisors or others. An impaired employee, the FRA found, will seldom display any outward "signs detectable by the lay person or, in many cases, even the physician." <span class="citation no-link">50 Fed. Reg. 31526</span> (1985). This view finds <span class="star-pagination">*629</span> ample support in the railroad industry's experience with Rule G, and in the judgment of the courts that have examined analogous testing schemes. See, <i>e. g., </i><i>Brotherhood of Maintenance Way Employees, Lodge 16</i> v. <i>Burlington Northern R. Co., supra,</i> at 1020. Indeed, while respondents posit that impaired employees might be detected without alcohol or drug testing,<sup>[9]</sup> the premise of respondents' lawsuit is that even the occurrence of a major calamity will not give rise to a suspicion of impairment with respect to any particular employee.</p>
<p>While no procedure can identify all impaired employees with ease and perfect accuracy, the FRA regulations supply an effective means of deterring employees engaged in safety-sensitive tasks from using controlled substances or alcohol in the first place. <span class="citation no-link">50 Fed. Reg. 31541</span> (1985). The railroad industry's experience with Rule G persuasively shows, and common sense confirms, that the customary dismissal sanction <span class="star-pagination">*630</span> that threatens employees who use drugs or alcohol while on duty cannot serve as an effective deterrent unless violators know that they are likely to be discovered. By ensuring that employees in safety-sensitive positions know they will be tested upon the occurrence of a triggering event, the timing of which no employee can predict with certainty, the regulations significantly increase the deterrent effect of the administrative penalties associated with the prohibited conduct, cf. <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#876" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S., at 876</a></span>, concomitantly increasing the likelihood that employees will forgo using drugs or alcohol while subject to being called for duty.</p>
<p>The testing procedures contemplated by Subpart C also help railroads obtain invaluable information about the causes of major accidents, see <span class="citation no-link">50 Fed. Reg. 31541</span> (1985), and to take appropriate measures to safeguard the general public. Cf. <i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 510</a></span> (1978) (noting that prompt investigation of the causes of a fire may uncover continuing dangers and thereby prevent the fire's recurrence); <i>Michigan</i> v. <i>Clifford,</i> <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#308" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 308</a></span> (1984) (REHNQUIST, J., dissenting) (same). Positive test results would point toward drug or alcohol impairment on the part of members of the crew as a possible cause of an accident, and may help to establish whether a particular accident, otherwise not drug related, was made worse by the inability of impaired employees to respond appropriately. Negative test results would likewise furnish invaluable clues, for eliminating drug impairment as a potential cause or contributing factor would help establish the significance of equipment failure, inadequate training, or other potential causes, and suggest a more thorough examination of these alternatives. Tests performed following the rule violations specified in Subpart D likewise can provide valuable information respecting the causes of those transgressions, which the FRA found to involve "the potential for a serious train accident or grave personal injury, or both." <span class="citation no-link">50 Fed. Reg. 31553</span> (1985).</p>
<p><span class="star-pagination">*631</span> A requirement of particularized suspicion of drug or alcohol use would seriously impede an employer's ability to obtain this information, despite its obvious importance. Experience confirms the FRA's judgment that the scene of a serious rail accident is chaotic. Investigators who arrive at the scene shortly after a major accident has occurred may find it difficult to determine which members of a train crew contributed to its occurrence. Obtaining evidence that might give rise to the suspicion that a particular employee is impaired, a difficult endeavor in the best of circumstances, is most impracticable in the aftermath of a serious accident. While events following the rule violations that activate the testing authority of Subpart D may be less chaotic, objective indicia of impairment are absent in these instances as well. Indeed, any attempt to gather evidence relating to the possible impairment of particular employees likely would result in the loss or deterioration of the evidence furnished by the tests. Cf. <i>Michigan</i> v. <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#293" aria-description="Citation for case: Michigan v. Clifford"><i>Clifford, supra,</i> at 293, n. 4</a></span> (plurality opinion); <i>Michigan</i> v. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler"><i>Tyler, supra,</i> at 510</a></span>. It would be unrealistic, and inimical to the Government's goal of ensuring safety in rail transportation, to require a showing of individualized suspicion in these circumstances.</p>
<p>Without quarreling with the importance of these governmental interests, the Court of Appeals concluded that the postaccident testing regulations were unreasonable because "[b]lood and urine tests intended to establish drug use other than alcohol . . . cannot measure current drug intoxication or degree of impairment." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#588" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley">839 F. 2d, at 588</a></span>. The court based its conclusion on its reading of certain academic journals that indicate that the testing of urine can disclose only drug metabolites, which "may remain in the body for days or weeks after the ingestion of the drug." <span class="citation" data-id="8958111"><a href="/opinion/8966762/railway-labor-executives-assn-v-burnley/#589" aria-description="Citation for case: Railway Labor Executives&#x27; Ass&#x27;n v. Burnley"><i>Id.,</i> at 589</a></span>. We find this analysis flawed for several reasons.</p>
<p>As we emphasized in <i>New Jersey</i> v. <i>T. L. O</i><i>.,</i> "it is universally recognized that evidence, to be relevant to an inquiry, need not conclusively prove the ultimate fact in issue, but <span class="star-pagination">*632</span> only have `any tendency to make the existence of any fact that is of consequence to the determination [of the point in issue] more probable or less probable than it would be without the evidence.' " <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#345" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 345</a></span>, quoting Fed. Rule Evid. 401. Even if urine test results disclosed nothing more specific than the recent use of controlled substances by a covered employee, this information would provide the basis for further investigative work designed to determine whether the employee used drugs at the relevant times. See Field Manual B-4. The record makes clear, for example, that a positive test result, coupled with known information concerning the pattern of elimination for the particular drug and information that may be gathered from other sources about the employee's activities, may allow the FRA to reach an informed judgment as to how a particular accident occurred. See <i>supra,</i> at 609-610.</p>
<p>More importantly, the Court of Appeals overlooked the FRA's policy of placing principal reliance on the results of blood tests, which unquestionably can identify very recent drug use, see, <i>e. g.,</i> <span class="citation no-link">49 Fed. Reg. 24291</span> (1984), while relying on urine tests as a secondary source of information designed to guard against the possibility that certain drugs will be eliminated from the bloodstream before a blood sample can be obtained. The court also failed to recognize that the FRA regulations are designed not only to discern impairment but also to deter it. Because the record indicates that blood and urine tests, taken together, are highly effective means of ascertaining on-the-job impairment and of deterring the use of drugs by railroad employees, we believe the Court of Appeals erred in concluding that the postaccident testing regulations are not reasonably related to the Government objectives that support them.<sup>[10]</sup></p>
<p><span class="star-pagination">*633</span> We conclude that the compelling Government interests served by the FRA's regulations would be significantly hindered if railroads were required to point to specific facts giving rise to a reasonable suspicion of impairment before testing a given employee. In view of our conclusion that, on the present record, the toxicological testing contemplated by the regulations is not an undue infringement on the justifiable expectations of privacy of covered employees, the Government's compelling interests outweigh privacy concerns.</p>
<p></p>
<h2>IV</h2>
<p>The possession of unlawful drugs is a criminal offense that the Government may punish, but it is a separate and far more dangerous wrong to perform certain sensitive tasks while under the influence of those substances. Performing those tasks while impaired by alcohol is, of course, equally dangerous, though consumption of alcohol is legal in most other contexts. The Government may take all necessary and reasonable regulatory steps to prevent or deter that hazardous conduct, and since the gravamen of the evil is performing certain functions while concealing the substance in the body, it may be necessary, as in the case before us, to examine the body or its fluids to accomplish the regulatory purpose. The necessity to perform that regulatory function with respect to railroad employees engaged in safety-sensitive tasks, and the reasonableness of the system for doing so, have been established in this case.</p>
<p>Alcohol and drug tests conducted in reliance on the authority of Subpart D cannot be viewed as private action outside the reach of the Fourth Amendment. Because the testing procedures mandated or authorized by Subparts C and D effect <span class="star-pagination">*634A</span> searches of the person, they must meet the Fourth Amendment's reasonableness requirement. In light of the limited discretion exercised by the railroad employers under the regulations, the surpassing safety interests served by toxicological tests in this context, and the diminished expectation of privacy that attaches to information pertaining to the fitness of covered employees, we believe that it is reasonable to conduct such tests in the absence of a warrant or reasonable suspicion that any particular employee may be impaired. We hold that the alcohol and drug tests contemplated by Subparts C and D of the FRA's regulations are reasonable within the meaning of the Fourth Amendment. The judgment of the Court of Appeals is accordingly reversed.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*634B</span> JUSTICE STEVENS, concurring in part and concurring in the judgment.</p>
<p>In my opinion the public interest in determining the causes of serious railroad accidents adequately supports the validity of the challenged regulations. I am not persuaded, however, that the interest in deterring the use of alcohol or drugs is either necessary or sufficient to justify the searches authorized by these regulations.</p>
<p>I think it a dubious proposition that the regulations significantly deter the use of alcohol and drugs by hours of service employees. Most people  and I would think most railroad employees as well  do not go to work with the expectation that they may be involved in a major accident, particularly one causing such catastrophic results as loss of life or the release of hazardous material requiring an evacuation. Moreover, even if they are conscious of the possibilities that such an accident might occur and that alcohol or drug use might be a contributing factor, if the risk of serious personal injury does not deter their use of these substances, it seems highly unlikely that the additional threat of loss of employment would have any effect on their behavior.</p>
<p><span class="star-pagination">*635</span> For this reason, I do not join the portions of Part III of the Court's opinion that rely on a deterrence rationale; I do, however, join the balance of the opinion and the Court's judgment.</p>
<p>JUSTICE MARSHALL, with whom JUSTICE BRENNAN joins, dissenting.</p>
<p>The issue in this case is not whether declaring a war on illegal drugs is good public policy. The importance of ridding our society of such drugs is, by now, apparent to all. Rather, the issue here is whether the Government's deployment in that war of a particularly Draconian weapon  the compulsory collection and chemical testing of railroad workers' blood and urine  comports with the Fourth Amendment. Precisely because the need for action against the drug scourge is manifest, the need for vigilance against unconstitutional excess is great. History teaches that grave threats to liberty often come in times of urgency, when constitutional rights seem too extravagant to endure. The World War II relocation-camp cases, <i>Hirabayashi</i> v. <i>United States,</i> <span class="citation" data-id="9419386"><a href="/opinion/103875/hirabayashi-v-united-states/" aria-description="Citation for case: Hirabayashi v. United States">320 U. S. 81</a></span> (1943); <i>Korematsu</i> v. <i>United States,</i> <span class="citation" data-id="9419548"><a href="/opinion/104040/korematsu-v-united-states/" aria-description="Citation for case: Korematsu v. United States">323 U. S. 214</a></span> (1944), and the Red scare and McCarthy-era internal subversion cases, <i>Schenck</i> v. <i>United States,</i> <span class="citation" data-id="99296"><a href="/opinion/99296/schenck-v-united-states/" aria-description="Citation for case: Schenck v. United States">249 U. S. 47</a></span> (1919); <i>Dennis</i> v. <i>United States,</i> <span class="citation" data-id="9420605"><a href="/opinion/104914/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">341 U. S. 494</a></span> (1951), are only the most extreme reminders that when we allow fundamental freedoms to be sacrificed in the name of real or perceived exigency, we invariably come to regret it.</p>
<p>In permitting the Government to force entire railroad crews to submit to invasive blood and urine tests, even when it lacks any evidence of drug or alcohol use or other wrongdoing, the majority today joins those shortsighted courts which have allowed basic constitutional rights to fall prey to momentary emergencies. The majority holds that the need of the Federal Railroad Administration (FRA) to deter and diagnose train accidents outweighs any "minimal" intrusions on personal dignity and privacy posed by mass toxicological testing of persons who have given no indication whatsoever of <span class="star-pagination">*636</span> impairment. <i>Ante,</i> at 624. In reaching this result, the majority ignores the text and doctrinal history of the Fourth Amendment, which require that highly intrusive searches of this type be based on probable cause, not on the evanescent cost-benefit calculations of agencies or judges. But the majority errs even under its own utilitarian standards, trivializing the raw intrusiveness of, and overlooking serious conceptual and operational flaws in, the FRA's testing program. These flaws cast grave doubts on whether that program, though born of good intentions, will do more than ineffectually symbolize the Government's opposition to drug use.</p>
<p>The majority purports to limit its decision to postaccident testing of workers in "safety-sensitive" jobs, <i>ante,</i> at 620, much as it limits its holding in the companion case to the testing of transferees to jobs involving drug interdiction or the use of firearms. <i>Treasury Employees</i> v. <i>Von Raab, post,</i> at 664. But the damage done to the Fourth Amendment is not so easily cabined. The majority's acceptance of dragnet blood and urine testing ensures that the first, and worst, casualty of the war on drugs will be the precious liberties of our citizens. I therefore dissent.</p>
<p></p>
<h2>I</h2>
<p>The Court today takes its longest step yet toward reading the probable-cause requirement out of the Fourth Amendment. For the fourth time in as many years, a majority holds that a " `special nee[d], beyond the normal need for law enforcement,' " makes the " `requirement' " of probable cause " `impracticable.' " <i>Ante,</i> at 619 (citations omitted). With the recognition of "[t]he Government's interest in regulating the conduct of railroad employees to ensure safety" as such a need, <i>ante,</i> at 620, the Court has now permitted "special needs" to displace constitutional text in each of the four categories of searches enumerated in the Fourth Amendment: searches of "persons," <i>ante,</i> at 613-614; "houses," <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868</a></span> (1987); "papers," <i>O'Connor</i> v. <i>Ortega,</i> <span class="star-pagination">*637</span> <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987); and "effects," <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985).</p>
<p>The process by which a constitutional "requirement" can be dispensed with as "impracticable" is an elusive one to me. The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated; and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The majority's recitation of the Amendment, remarkably, leaves off after the word "violated," <i>ante,</i> at 613, but the remainder of the Amendment  the Warrant Clause  is not so easily excised. As this Court has long recognized, the Framers intended the provisions of that Clause  a warrant and probable cause  to "provide the yardstick against which official searches and seizures are to be measured." <i>T. L. O., supra,</i> at 359-360 (opinion of BRENNAN, J.). Without the content which those provisions give to the Fourth Amendment's overarching command that searches and seizures be "reasonable," the Amendment lies virtually devoid of meaning, subject to whatever content shifting judicial majorities, concerned about the problems of the day, choose to give to that supple term. See <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213</a></span> (1979) ("[T]he protections intended by the Framers could all too easily disappear in the consideration and balancing of the multifarious circumstances presented by different cases"). Constitutional requirements like probable cause are not fair-weather friends, present when advantageous, conveniently absent when "special needs" make them seem not.</p>
<p>Until recently, an unbroken line of cases had recognized probable cause as an indispensable prerequisite for a full-scale search, regardless of whether such a search was conducted pursuant to a warrant or under one of the recognized exceptions to the warrant requirement. <i>T. L. O., supra,</i> at 358 <span class="star-pagination">*638</span> and 359, n. 3 (opinion of BRENNAN, J.); see also <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span> (1970). Only where the government action in question had a "substantially less intrusive" impact on privacy, <i>Dunaway,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#210" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 210</a></span>, and thus clearly fell short of a full-scale search, did we relax the probable-cause standard. <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#214" aria-description="Citation for case: Dunaway v. New York"><i>Id.,</i> at 214</a></span> ("For all but those narrowly defined intrusions, the requisite `balancing' . . . is embodied in the principle that seizures are `reasonable' only if supported by probable cause"); see also <i>T. L. O., supra,</i> at 360 (opinion of BRENNAN, J.). Even in this class of cases, we almost always required the government to show some individualized suspicion to justify the search.<sup>[1]</sup> The few searches which we upheld in the absence of individualized justification were routinized, fleeting, and nonintrusive encounters conducted pursuant to regulatory programs which entailed no contact with the person.<sup>[2]</sup></p>
<p><span class="star-pagination">*639</span> In the four years since this Court, in <i>T. L. O.,</i> first began recognizing "special needs" exceptions to the Fourth Amendment, the clarity of Fourth Amendment doctrine has been badly distorted, as the Court has eclipsed the probable-cause requirement in a patchwork quilt of settings: public school principals' searches of students' belongings, <i>T. L. O.;</i> public employers' searches of employees' desks, <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O'Connor</a></span>;</i> and probation officers' searches of probationers' homes, <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>.</i><sup>[3]</sup> Tellingly, each time the Court has found that "special needs" counseled ignoring the literal requirements of the Fourth Amendment for such full-scale searches in favor of a formless and unguided "reasonableness" balancing inquiry, it has concluded that the search in question satisfied that test. I have joined dissenting opinions in each of these cases, protesting the "jettison[ing of] . . . the only standard that finds support in the text of the Fourth Amendment" and predicting that the majority's "Rohrschach-like `balancing test' " portended "a dangerous weakening of the purpose of the Fourth Amendment to protect the privacy and security of our citizens." <i>T. L. O., supra,</i> at 357-358 (opinion of BRENNAN, J.).</p>
<p>The majority's decision today bears out that prophecy. After determining that the Fourth Amendment applies to the FRA's testing regime, the majority embarks on an extended inquiry into whether that regime is "reasonable," an inquiry in which it balances " `all of the circumstances surrounding the search or seizure and the nature of the search or seizure itself.' " <i>Ante,</i> at 619, quoting <i>United States</i> v. <i>Montoya de</i> <span class="star-pagination">*640</span> <i>Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#537" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 537</a></span> (1985). The result is "special needs" balancing analysis' deepest incursion yet into the core protections of the Fourth Amendment. Until today, it was conceivable that, when a government search was aimed at a person and not simply the person's possessions, balancing analysis had no place. No longer: with nary a word of explanation or acknowledgment of the novelty of its approach, the majority extends the "special needs" framework to a regulation involving compulsory blood withdrawal and urinary excretion, and chemical testing of the bodily fluids collected through these procedures. And until today, it was conceivable that a prerequisite for surviving "special needs" analysis was the existence of individualized suspicion. No longer: in contrast to the searches in <i>T. L. O., O'Connor,</i> and <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">Griffin</a></span>,</i> which were supported by individualized evidence suggesting the culpability of the persons whose property was searched,<sup>[4]</sup> the regulatory regime upheld today requires the postaccident collection and testing of the blood and urine of <i>all</i> covered employees  even if every member of this group gives every indication of sobriety and attentiveness.</p>
<p>In widening the "special needs" exception to probable cause to authorize searches of the human body unsupported by <i>any</i> evidence of wrongdoing, the majority today completes the process begun in <i>T. L. O.</i> of eliminating altogether the probable-cause requirement for civil searches  those undertaken for reasons "beyond the normal need for law enforcement." <i>Ante,</i> at 619 (citations omitted). In its place, the majority substitutes a manipulable balancing inquiry under which, upon the mere assertion of a "special need," even the deepest dignitary and privacy interests become vulnerable <span class="star-pagination">*641</span> to governmental incursion. See <i><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/" aria-description="Citation for case: Griffin v. Wisconsin">ibid.</a></span></i> (distinguishing criminal from civil searches). By its terms, however, the Fourth Amendment  unlike the Fifth and Sixth  does not confine its protections to either criminal or civil actions. Instead, it protects generally "[t]he right of the people to be secure."<sup>[5]</sup></p>
<p>The fact is that the malleable "special needs" balancing approach can be justified only on the basis of the policy results it allows the majority to reach. The majority's concern with the railroad safety problems caused by drug and alcohol abuse is laudable; its cavalier disregard for the text of the Constitution is not. There is no drug exception to the Constitution, any more than there is a communism exception or an exception for other real or imagined sources of domestic unrest. <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 455</a></span> (1971). Because abandoning the explicit protections of the Fourth Amendment seriously imperils "the right to be let alone  the most comprehensive of rights and the right most valued by civilized men," <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#478" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 478</a></span> (1928) (Brandeis, J., dissenting), I reject the majority's "special needs" rationale as unprincipled and dangerous.</p>
<p></p>
<h2>II</h2>
<p>The proper way to evaluate the FRA's testing regime is to use the same analytic framework which we have traditionally used to appraise Fourth Amendment claims involving fullscale searches, at least until the recent "special needs" cases. Under that framework, we inquire, serially, whether a <span class="star-pagination">*642</span> search has taken place, see, <i>e. g., </i><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350-353</a></span> (1967); whether the search was based on a valid warrant or undertaken pursuant to a recognized exception to the warrant requirement, see, <i>e. g., </i><i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#748" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 748-750</a></span> (1984); whether the search was based on probable cause or validly based on lesser suspicion because it was minimally intrusive, see, <i>e. g., </i><i>Dunaway,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S., at 208-210</a></span>; and, finally, whether the search was conducted in a reasonable manner, see, <i>e. g., </i><i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#763" aria-description="Citation for case: Winston v. Lee">470 U. S. 753, 763-766</a></span> (1985). See also <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#354" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 354-355</a></span> (opinion of BRENNAN, J.) (summarizing analytic framework).</p>
<p>The majority's threshold determination that "covered" railroad employees have been searched under the FRA's testing program is certainly correct. <i>Ante,</i> at 616-618. Who among us is not prepared to consider reasonable a person's expectation of privacy with respect to the extraction of his blood, the collection of his urine, or the chemical testing of these fluids? <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984).<sup>[6]</sup> The majority's ensuing conclusion that the warrant requirement may be dispensed with, however, conveniently overlooks the fact that there are three distinct searches at issue. Although the importance of collecting blood and urine samples before drug or alcohol metabolites disappear justifies waiving the warrant requirement for those two searches under the narrow "exigent circumstances" exception, see <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770</a></span> (1966) ("[T]he delay necessary to obtain a warrant . . . threaten[s] `the destruction of evidence' "), no such exigency prevents railroad officials from securing a warrant before chemically testing the samples they obtain. Blood and urine do not spoil if <span class="star-pagination">*643</span> properly collected and preserved, and there is no reason to doubt the ability of railroad officials to grasp the relatively simple procedure of obtaining a warrant authorizing, where appropriate, chemical analysis of the extracted fluids. It is therefore wholly unjustified to dispense with the warrant requirement for this final search. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#761" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 761-764</a></span> (1969) (exigency exception permits warrantless searches only to the extent that exigency exists).</p>
<p>It is the probable-cause requirement, however, that the FRA's testing regime most egregiously violates, a fact which explains the majority's ready acceptance and expansion of the countertextual "special needs" exception. By any measure, the FRA's highly intrusive collection and testing procedures qualify as full-scale personal searches. Under our precedents, a showing of probable cause is therefore clearly required. But even if these searches were viewed as entailing only minimal intrusions on the order, say, of a police stop-and-frisk, the FRA's program would still fail to pass constitutional muster, for we have, without exception, demanded that even minimally intrusive searches of the person be founded on individualized suspicion. See <i>supra,</i> at 638, and n. 1. The federal parties concede it does not satisfy this standard. Brief for Federal Parties 18. Only if one construes the FRA's collection and testing procedures as akin to the routinized and fleeting regulatory interactions which we have permitted in the absence of individualized suspicion, see n. 2, <i>supra,</i> might these procedures survive constitutional scrutiny. Presumably for this reason, the majority likens this case to <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976), which upheld brief automobile stops at the border to ascertain the validity of motorists' residence in the United States. <i>Ante,</i> at 624. Case law and common sense reveal both the bankruptcy of this absurd analogy and the constitutional imperative of adhering to the textual standard of probable cause to evaluate the FRA's multifarious full-scale searches.</p>
<p><span class="star-pagination">*644</span> Compelling a person to submit to the piercing of his skin by a hypodermic needle so that his blood may be extracted significantly intrudes on the "personal privacy and dignity against unwarranted intrusion by the State" against which the Fourth Amendment protects. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#767" aria-description="Citation for case: Schmerber v. California"><i>Schmerber, supra,</i> at 767</a></span>. As we emphasized in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1968), "Even a limited search of the outer clothing . . . constitutes a severe, though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience." We have similarly described the taking of a suspect's fingernail scrapings as a " `severe, though brief, intrusion upon cherished personal security.' " <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#295" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 295</a></span> (1973) (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 24-25</a></span>, and upholding this procedure upon a showing of probable cause). The government-compelled withdrawal of blood, involving as it does the added aspect of physical invasion, is surely no less an intrusion. The surrender of blood on demand is, furthermore, hardly a quotidian occurrence. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 557</a></span> (routine stops involve "quite limited" intrusion).</p>
<p>In recognition of the intrusiveness of this procedure, we specifically required in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> that police have evidence of a drunken-driving suspect's impairment before forcing him to endure a blood test:</p>
<blockquote>"The interests in human dignity and privacy which the Fourth Amendment protects forbid any such intrusions on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear . . . ." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S., at 769-770</a></span>.</blockquote>
<p><i>Schmerber</i> strongly suggested that the "clear indication" needed to justify a compulsory blood test amounted to a showing of probable cause, which "plainly" existed in that case. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#768" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 768</a></span>. Although subsequent cases interpreting <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> have differed over whether a showing of individualized <span class="star-pagination">*645</span> suspicion would have sufficed, compare <i>Winston,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/#760" aria-description="Citation for case: Winston v. Lee">470 U. S., at 760</a></span> (<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> "noted the importance of probable cause"), with <i>Montoya de Hernandez,</i> <span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#540" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S., at 540</a></span> (<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> "indicate[d] the necessity for particularized suspicion"), by any reading, <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> clearly forbade compulsory blood tests on any lesser showing than individualized suspicion. Exactly why a blood test which, if conducted on one person, requires a showing of at least individualized suspicion may, if conducted on many persons, be based on no showing whatsoever, the majority does not  and cannot  explain.<sup>[7]</sup></p>
<p>Compelling a person to produce a urine sample on demand also intrudes deeply on privacy and bodily integrity. Urination is among the most private of activities. It is generally forbidden in public, eschewed as a matter of conversation, and performed in places designed to preserve this tradition of <span class="star-pagination">*646</span> personal seclusion. Cf. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span> (border-stop questioning involves no more than "some annoyance" and is neither "frightening" nor "offensive"). The FRA, however, gives scant regard to personal privacy, for its Field Manual instructs supervisors monitoring urination that railroad workers must provide urine samples "<i>under direct observation</i> by the physician/technician." Federal Railroad Administration, United States Dept. of Transportation, Field Manual: Control of Alcohol and Drug Use in Railroad Operations D-5 (1986) (emphasis added).<sup>[8]</sup> That the privacy interests offended by compulsory and supervised urine collection are profound is the overwhelming judgment of the lower courts and commentators. As Professor  later Solicitor General  Charles Fried has written:</p>
<blockquote>"[I]n our culture the excretory functions are shielded by more or less absolute privacy, so much so that situations in which this privacy is violated are experienced as extremely distressing, as detracting from one's dignity and self esteem." Privacy, 77 Yale L. J. 475, 487 (1968).<sup>[9]</sup></blockquote>
<p>The majority's characterization of the privacy interests implicated by urine collection as "minimal," <i>ante,</i> at 624, is nothing <span class="star-pagination">*647</span> short of startling. This characterization is, furthermore, belied by the majority's own prior explanation of why compulsory urination constitutes a search for the purposes of the Fourth Amendment:</p>
<blockquote>" `There are few activities in our society more personal or private than the passing of urine. Most people describe it by euphemisms if they talk about it at all. It is a function traditionally performed without public observation; indeed, its performance in public is generally prohibited by law as well as social custom.' " <i>Ante,</i> at 617, quoting <i>National Treasury Employees Union</i> v. <i>Von Raab,</i> <span class="citation" data-id="486563"><a href="/opinion/486563/national-treasury-employees-union-v-raab/#175" aria-description="Citation for case: National Treasury Employees Union v. Raab">816 F. 2d 170, 175</a></span> (CA5 1987).</blockquote>
<p>The fact that the majority can invoke this powerful passage in the context of deciding that a search has occurred, and then ignore it in deciding that the privacy interests this search implicates are "minimal," underscores the shameless manipulability of its balancing approach.</p>
<p>Finally, the chemical analysis the FRA performs upon the blood and urine samples implicates strong privacy interests apart from those intruded upon by the collection of bodily fluids. Technological advances have made it possible to uncover, through analysis of chemical compounds in these fluids, not only drug or alcohol use, but also medical disorders such as epilepsy, diabetes, and clinical depression. Cf. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 558</a></span>, quoting <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 880</a></span> (1975) (checkpoint inquiry involves only " `a brief question or two' " about motorist's residence). As the Court of Appeals for the District of Columbia Circuit has observed: "[S]uch tests may provide Government officials with a periscope through which they can peer into an individual's behavior in her private life, even in her own home." <i>Jones</i> v. <i>McKenzie,</i> 266 U. S. App. D. C. 85, 89, <span class="citation" data-id="497255"><a href="/opinion/497255/juanita-m-jones-v-floretta-dukes-mckenzie-superintendent-of-schools/#339" aria-description="Citation for case: Juanita M. Jones v. Floretta Dukes McKenzie...">833 F. 2d 335, 339</a></span> (1987); see also <i>Capua</i> v. <i>Plainfield,</i> <span class="citation" data-id="1908384"><a href="/opinion/1908384/capua-v-city-of-plainfield/#1511" aria-description="Citation for case: Capua v. City of Plainfield">643 F. Supp. 1507, 1511</a></span> (NJ 1986) (urine testing is "form of surveillance" which "reports on a person's off-duty activities just as surely as someone had been present and <span class="star-pagination">*648</span> watching"). The FRA's requirement that workers disclose the medications they have taken during the 30 days prior to chemical testing further impinges upon the confidentiality customarily attending personal health secrets.</p>
<p>By any reading of our precedents, the intrusiveness of these three searches demands that they  like other full-scale searches  be justified by probable cause. It is no answer to suggest, as does the majority, that railroad workers have relinquished the protection afforded them by this Fourth Amendment requirement, either by "participat[ing] in an industry that is regulated pervasively to ensure safety" or by undergoing periodic fitness tests pursuant to state law or to collective-bargaining agreements. <i>Ante,</i> at 627.</p>
<p>Our decisions in the regulatory search area refute the suggestion that the heavy regulation of the railroad industry eclipses workers' rights under the Fourth Amendment to insist upon a showing of probable cause when their bodily fluids are being extracted. This line of cases has exclusively involved searches of employer <i>property,</i> with respect to which "[c]ertain industries have such a history of government oversight that no reasonable expectation of privacy could exist for a <i>proprietor</i> over the <i>stock</i> of such an enterprise." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 313</a></span> (1978) (emphasis added; citation omitted), quoted in <i>New York</i> v. <i>Burger,</i> <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#700" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 700</a></span> (1987). Never have we intimated that regulatory searches reduce employees' right of privacy in their <i>persons.</i> See <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 537</a></span> (1967) ("[T]he inspections are [not] personal in nature"); cf. <i>Donovan</i> v. <i>Dewey,</i> <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#598" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 598-599</a></span> (1981); <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Marshall, supra,</i> at 313</a></span>. As the Court pointed out in <i><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">O'Connor</a></span>,</i> individuals do not lose Fourth Amendment rights at the workplace gate, 480 U. S., at 716-718; see also <i>Oliver</i> v. <i>United States,</i> <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178, n. 8</a></span> (1984), any more than they relinquish these rights at the schoolhouse door, <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#333" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 333</a></span>, or the hotel room threshold, <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 301</a></span> (1966). These rights mean <span class="star-pagination">*649</span> little indeed if, having passed through these portals, an individual may remain subject to a suspicionless search of his person justified solely on the grounds that the government already is permitted to conduct a search of the inanimate contents of the surrounding area. In holding that searches of persons may fall within the category of regulatory searches permitted in the absence of probable cause or even individualized suspicion, the majority sets a dangerous and ill-conceived precedent.</p>
<p>The majority's suggestion that railroad workers' privacy is only minimally invaded by the collection and testing of their bodily fluids because they undergo periodic fitness tests, <i>ante,</i> at 624-625, is equally baseless. As an initial matter, even if participation in these fitness tests did render "minimal" an employee's "interest in bodily security," <i>ante,</i> at 628, such minimally intrusive searches of the person require, under our precedents, a justificatory showing of individualized suspicion. See <i>supra,</i> at 637. More fundamentally, railroad employees are <i>not</i> routinely required to submit to blood or urine tests to gain or to maintain employment, and railroad employers do not ordinarily have access to employees' blood or urine, and certainly not for the purpose of ascertaining drug or alcohol usage. That railroad employees sometimes undergo tests of eyesight, hearing, skill, intelligence, and agility, <i>ante,</i> at 627, n. 8, hardly prepares them for Government demands to submit to the extraction of blood, to excrete under supervision, or to have these bodily fluids tested for the physiological and psychological secrets they may contain. Surely employees who release basic information about their financial and personal history so that employers may ascertain their "ethical fitness" do not, by so doing, relinquish their expectations of privacy with respect to their personal letters and diaries, revealing though these papers may be of their character.</p>
<p>I recognize that invalidating the full-scale searches involved in the FRA's testing regime for failure to comport with the Fourth Amendment's command of probable cause <span class="star-pagination">*650</span> may hinder the Government's attempts to make rail transit as safe as humanly possible. But constitutional rights have their consequences, and one is that efforts to maximize the public welfare, no matter how well intentioned, must always be pursued within constitutional boundaries. Were the police freed from the constraints of the Fourth Amendment for just one day to seek out evidence of criminal wrongdoing, the resulting convictions and incarcerations would probably prevent thousands of fatalities. Our refusal to tolerate this specter reflects our shared belief that even beneficent governmental power  whether exercised to save money, save lives, or make the trains run on time  must always yield to "a resolute loyalty to constitutional safeguards." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 273</a></span> (1973). The Constitution demands no less loyalty here.</p>
<p></p>
<h2>III</h2>
<p>Even accepting the majority's view that the FRA's collection and testing program is appropriately analyzed under a multifactor balancing test, and not under the literal terms of the Fourth Amendment, I would still find the program invalid. The benefits of suspicionless blood and urine testing are far outstripped by the costs imposed on personal liberty by such sweeping searches. Only by erroneously deriding as "minimal" the privacy and dignity interests at stake, and by uncritically inflating the likely efficacy of the FRA's testing program, does the majority strike a different balance.</p>
<p>For the reasons stated above, I find nothing minimal about the intrusion on individual liberty that occurs whenever the Government forcibly draws and analyzes a person's blood and urine. Several aspects of the FRA's testing program exacerbate the intrusiveness of these procedures. Most strikingly, the agency's regulations not only do not forbid, but, in fact, appear to invite criminal prosecutors to obtain the blood and urine samples drawn by the FRA and use them as the basis of criminal investigations and trials. See 49 CFR <span class="star-pagination">*651</span> § 219.211(d) (1987) ("Each sample . . . may be made available to . . . a party in litigation upon service of appropriate compulsory process on the custodian of the sample . . ."). This is an unprecedented invitation, leaving open the possibility of criminal prosecutions based on suspicionless searches of the human body. Cf. <i>Treasury Employees, post,</i> at 666 (Customs Service drug-testing program prohibits use of test results in criminal prosecutions); <i>Camara,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 537</a></span>.</p>
<p>To be sure, the majority acknowledges, in passing, the possibility of criminal prosecutions, <i>ante,</i> at 621, n. 5, but it refuses to factor this possibility into its Fourth Amendment balancing process, stating that "the record does not disclose that [<span class="citation no-link">49 CFR § 219.211</span>(d) (1987)] was intended to be, or actually has been, so used." <i><span class="citation no-link">Ibid.</span></i> This demurrer is highly disingenuous. The federal parties concede that they find "no prohibition on the release of FRA testing results to prosecutors." Brief for Federal Parties 10, n. 15. The absence of prosecutions to date  which is likely due to the fact that the FRA's regulations have been held invalid for much of their brief history  hardly proves that prosecutors will not avail themselves of the FRA's invitation in the future. If the majority really views the impact of FRA testing on privacy interests as minimal even if these tests generate criminal prosecutions, it should say so. If the prospect of prosecutions would lead the majority to reassess the validity of the testing program with prosecutions as part of the balance, it should say so, too, or condition its approval of that program on the nonrelease of test results to prosecutors. In ducking this important issue, the majority gravely disserves both the values served by the Fourth Amendment and the rights of those persons whom the FRA searches. Furthermore, the majority's refusal to restrict the release of test results casts considerable doubt on the conceptual basis of its decision  that the "special need" of railway safety is one "beyond the <span class="star-pagination">*652</span> normal need for law enforcement." <i>Ante,</i> at 619 (citations omitted).<sup>[10]</sup></p>
<p>The majority also overlooks needlessly intrusive aspects of the testing process itself. Although the FRA requires the collection and testing of both blood and urine, the agency concedes that mandatory urine tests  unlike blood tests  do not measure current impairment and therefore cannot differentiate on-duty impairment from prior drug or alcohol use which has ceased to affect the user's behavior. See <span class="citation no-link">49 CFR § 219.309</span>(2) (1987) (urine test may reveal use of drugs or alcohol as much as 60 days prior to sampling). Given that the FRA's stated goal is to ascertain current impairment, and not to identify persons who have used substances in their spare time sufficiently in advance of their railroad duties to pose no risk of on-duty impairment, § 219.101(a), mandatory urine testing seems wholly excessive. At the very least, the FRA could limit its use of urinalysis to confirming findings of current impairment suggested by a person's blood tests. The additional invasion caused by automatically testing urine as well as blood hardly ensures that privacy interests "will be invaded no more than is necessary." <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 343</a></span>.</p>
<p>The majority's trivialization of the intrusions on worker privacy posed by the FRA's testing program is matched at the other extreme by its blind acceptance of the Government's assertion that testing will "dete[r] employees engaged in safety-sensitive tasks from using controlled substances or alcohol," and "help railroads obtain invaluable information <span class="star-pagination">*653</span> about the causes of major accidents." <i>Ante,</i> at 629, 630. With respect, first, to deterrence, it is simply implausible that testing employees <i>after</i> major accidents occur, <span class="citation no-link">49 CFR § 219.201</span>(a)(1) (1987), will appreciably discourage them from using drugs or alcohol. As JUSTICE STEVENS observes in his concurring opinion:</p>
<blockquote>"Most people  and I would think most railroad employees as well  do not go to work with the expectation that they may be involved in a major accident, particularly one causing such catastrophic results as loss of life or the release of hazardous material requiring an evacuation. Moreover, even if they are conscious of the possibilities that such an accident might occur and that alcohol or drug use might be a contributing factor, if the risk of serious personal injury does not deter their use of these substances, it seems highly unlikely that the additional threat of loss of employment would have any effect on their behavior." <i>Ante,</i> at 634.</blockquote>
<p>Under the majority's deterrence rationale, people who skip school or work to spend a sunny day at the zoo will not taunt the lions because their truancy or absenteeism might be discovered in the event they are mauled. It is, of course, the fear of the accident, not the fear of a postaccident revelation, that deters. The majority's credulous acceptance of the FRA's deterrence rationale is made all the more suspect by the agency's failure to introduce, in an otherwise ample administrative record, <i>any</i> studies explaining or supporting its theory of accident deterrence.</p>
<p>The poverty of the majority's deterrence rationale leaves the Government's interest in diagnosing the causes of major accidents as the sole remaining justification for the FRA's testing program. I do not denigrate this interest, but it seems a slender thread from which to hang such an intrusive program, particularly given that the knowledge that one or more workers were impaired at the time of

[...TRUNCATED 32430 of 152430 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
