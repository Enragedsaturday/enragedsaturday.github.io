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

## GROUP: content/cases/Berger v. New York.md  (`case`, 7 assertions)

### content_page

```
---
title: "Berger v. New York"
type: case
citation: "388 U.S. 41 (1967)"
parallel_cite: "87 S. Ct. 1873; 18 L. Ed. 2d 1040"
neutral_cite: 1967 U.S. LEXIS 2964
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: 615
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Berger v. New York
  varies_by_point: false
  scope_note: "Good law as the constitutional baseline for electronic-surveillance warrants. Together with Katz it prompted Congress to enact Title III of the Omnibus Crime Control Act of 1968, which codified conforming wiretap standards."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107483/berger-v-new-york/"
  cluster_id: 107483
  opinion_id: 9423459
  identity_checked: true
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: "Key — Anchor"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-ref — electronic-surveillance floor)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[Katz v. United States]]", "[[Olmstead v. United States]]", "[[United States v. Karo]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "wiretap", "eavesdropping", "particularity", "surveillance"]
holding: "New York's permissive eavesdropping statute was unconstitutional for lack of particularity and safeguards; the case sets Fourth Amendment standards for electronic-surveillance warrants."
lake:
  record_id: Berger v. New York
  status: verified
  projected_at: 2026-07-06
---

# Berger v. New York

*388 U.S. 41 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Berger was convicted of conspiracy to bribe a state official, based on recordings obtained under eavesdrop orders issued pursuant to New York's permissive eavesdropping statute (§ 813-a). The statute allowed an *[[Common Legal Terms#ex-parte|ex parte]]* order, on "reasonable ground to believe that evidence of crime" might be obtained, authorizing 60-day installation of recording devices with possible extensions. Berger challenged the statute as authorizing general, exploratory electronic searches without Fourth Amendment [[Particularity|particularity]].

## Issue
Whether New York's permissive eavesdropping statute satisfies the Fourth Amendment, or whether its breadth and lack of [[Particularity|particularity]] render electronic surveillance under it unreasonable.

## Rule
The statute was unconstitutional for overbreadth: "We have concluded that the language of New York's statute is too broad in its sweep resulting in a trespassory intrusion into a constitutionally protected area and is, therefore, violative of the Fourth and Fourteenth Amendments." — 388 U.S. at 44. ^pin-44

It failed the Fourth Amendment's [[Particularity|particularity]] command: "New York's statute lacks this particularization. It merely says that a warrant may issue on reasonable ground to believe that evidence of crime may be obtained by the eavesdrop. It lays down no requirement for particularity in the warrant as to what specific crime has been or is being committed, nor 'the place to be searched,' or 'the persons or things to be seized' as specifically required by the Fourth Amendment." — *Id.* at 56. ^pin-56

## Application
The eavesdrop orders that captured Berger's conversations issued under a statute that named no particular crime, identified no particular conversations to be seized, and authorized continuous 60-day surveillance (extendable) on a single showing, with no requirement of prompt termination once the sought conversation was obtained and no return or notice. Because that scheme permitted exactly the kind of broad, exploratory rummaging the Fourth Amendment's [[Particularity|particularity]] requirement forbids, the surveillance — and the statute authorizing it — were unreasonable, and the recordings could not stand.

## Conclusion
New York's eavesdropping statute violated the Fourth and Fourteenth Amendments; the conviction was reversed. *Berger* (with [[Katz v. United States]], decided the same Term) established the [[Particularity|particularity]] and procedural safeguards electronic-surveillance authorizations must contain.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Marks the transition from the property-trespass approach of [[Olmstead v. United States]] toward the privacy framework completed in [[Katz v. United States]]; its standards shaped Title III of the Omnibus Crime Control Act of 1968 and the interior-monitoring analysis of [[United States v. Karo]].

## Appears on
- [[Electronic Surveillance and Title III]] — *Key — Anchor*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-ref — electronic-surveillance floor)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Berger v. New York*, 388 U.S. 41 (1967) — https://www.courtlistener.com/opinion/107483/berger-v-new-york/ — pinpoints: 44, 56.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d63439c14a8965ec", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "388 U.S. 41 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 2964", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1873; 18 L. Ed. 2d 1040", "title": "Berger v. New York", "year": "1967"}}
{"assertion_id": "0ecddad3ab8b0162", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Key — Anchor", "title": "Berger v. New York"}}
{"assertion_id": "4979268858cb8c11", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-ref — electronic-surveillance floor)", "title": "Berger v. New York"}}
{"assertion_id": "7c2fbe09e6ec9ff1", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "Berger v. New York"}}
{"assertion_id": "f035a5f524fe1d9a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "New York's permissive eavesdropping statute was unconstitutional for lack of particularity and safeguards; the case sets Fourth Amendment standards for electronic-surveillance warrants.", "title": "Berger v. New York"}}
{"assertion_id": "360a1c0d3b410a71", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Berger v. New York"}}
{"assertion_id": "d8727d20ed0e019a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Berger v. New York", "field_i_validity": "good_law", "scope_note": "Good law as the constitutional baseline for electronic-surveillance warrants. Together with Katz it prompted Congress to enact Title III of the Omnibus Crime Control Act of 1968, which codified conforming wiretap standards.", "title": "Berger v. New York", "varies_by_point": "false"}}
```

### lake record — Berger v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Berger v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Berger v. New York",
    "case_name_short": "Berger",
    "case_name_full": "Berger v. New York",
    "input_case_name": "Berger v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": "615",
    "cluster_id": 107483,
    "lead_opinion_id": 9423459,
    "sibling_ids": [
      107483,
      9423459,
      9423460,
      9423461,
      9423462,
      9423463,
      9423464
    ],
    "absolute_url": "/opinion/107483/berger-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8967447,
        "score": 10,
        "case_name": "Berger v. New York"
      },
      {
        "cluster_id": 8967390,
        "score": 10,
        "case_name": "Berger v. New York"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 41",
      "volume": "388",
      "reporter": "U.S.",
      "page": "41",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1873",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1873",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1040",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2964",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2964",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 41",
        "volume": "388",
        "reporter": "U.S.",
        "page": "41",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1873",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1873",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1040",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2964",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2964",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 41",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 41",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-44",
      "page": null,
      "quote": "might be obtained, authorizing 60-day installation of recording devices with possible extensions. Berger challenged the statute as authorizing general, exploratory electronic searches without Fourth Amendment particularity. ## Issue Whether New York's permissive eavesdropping statute satisfies the Fourth Amendment, or whether its breadth and lack of particularity render electronic surveillance under it unreasonable. ## Rule The statute was unconstitutional for overbreadth:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-56",
      "page": null,
      "quote": "New York's statute lacks this particularization. It merely says that a warrant may issue on reasonable ground to believe that evidence of crime may be obtained by the eavesdrop. It lays down no requirement for particularity in the warrant as to what specific crime has been or is being committed, nor 'the place to be searched,' or 'the persons or things to be seized' as specifically required by the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Berger v. New York",
    "varies_by_point": false,
    "scope_note": "Good law as the constitutional baseline for electronic-surveillance warrants. Together with Katz it prompted Congress to enact Title III of the Omnibus Crime Control Act of 1968, which codified conforming wiretap standards.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hector Feliciano(074395)",
          "cluster_id": 3183943,
          "cite": [
            "224 N.J. 351",
            "132 A.3d 1245",
            "2016 N.J. LEXIS 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re the United States",
          "cluster_id": 8441402,
          "cite": [
            "724 F.3d 600",
            "58 Communications Reg. (P&F) 1292",
            "2013 WL 3914484",
            "2013 U.S. App. LEXIS 15510"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Rabb",
          "cluster_id": 5640827,
          "cite": [
            "16 N.Y.3d 145",
            "945 N.E.2d 447"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whisenhunt v. State",
          "cluster_id": 1881110,
          "cite": [
            "122 S.W.3d 295",
            "2003 WL 22053696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Triumph Capital Group, Inc.",
          "cluster_id": 8751433,
          "cite": [
            "211 F.R.D. 31",
            "2002 U.S. Dist. LEXIS 21615",
            "2002 WL 31487754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcraft v. State",
          "cluster_id": 1657870,
          "cite": [
            "934 S.W.2d 727",
            "1996 WL 474085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Juan Ramon MATTA-BALLESTEROS, Defendant-Appellant",
          "cluster_id": 709239,
          "cite": [
            "71 F.3d 754",
            "95 Daily Journal DAR 15853",
            "95 Cal. Daily Op. Serv. 9042",
            "43 Fed. R. Serv. 338",
            "1995 U.S. App. LEXIS 33475",
            "1995 WL 704693"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcraft v. State",
          "cluster_id": 1751133,
          "cite": [
            "900 S.W.2d 817",
            "1995 WL 257158"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Ricciardelli",
          "cluster_id": 610895,
          "cite": [
            "998 F.2d 8",
            "1993 U.S. App. LEXIS 14891",
            "1993 WL 210540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane1_negative"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harris",
          "cluster_id": 108379,
          "cite": [
            "29 L. Ed. 2d 723",
            "91 S. Ct. 2075",
            "403 U.S. 573",
            "1971 U.S. LEXIS 18"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Florida",
          "cluster_id": 108186,
          "cite": [
            "26 L. Ed. 2d 446",
            "90 S. Ct. 1893",
            "399 U.S. 78",
            "1970 U.S. LEXIS 98",
            "53 Ohio Op. 2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nixon v. Administrator of General Services",
          "cluster_id": 109729,
          "cite": [
            "53 L. Ed. 2d 867",
            "97 S. Ct. 2777",
            "433 U.S. 425",
            "1977 U.S. LEXIS 24",
            "2 Media L. Rep. (BNA) 2025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desist v. United States",
          "cluster_id": 107875,
          "cite": [
            "22 L. Ed. 2d 248",
            "89 S. Ct. 1030",
            "394 U.S. 244",
            "1969 U.S. LEXIS 2159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Krull",
          "cluster_id": 111835,
          "cite": [
            "94 L. Ed. 2d 364",
            "107 S. Ct. 1160",
            "480 U.S. 340",
            "1987 U.S. LEXIS 1061",
            "55 U.S.L.W. 4291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
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
        "journal_ref": "Berger v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107483 OR 9423459 OR 9423460 OR 9423461 OR 9423462 OR 9423463 OR 9423464) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mjk4MjA4MDAwMDAmcz03ODk1MTM5JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107483+OR+9423459+OR+9423460+OR+9423461+OR+9423462+OR+9423463+OR+9423464%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(107483 OR 9423459 OR 9423460 OR 9423461 OR 9423462 OR 9423463 OR 9423464)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzYmcz0yODE5MTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107483+OR+9423459+OR+9423460+OR+9423461+OR+9423462+OR+9423463+OR+9423464%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107483 OR 9423459 OR 9423460 OR 9423461 OR 9423462 OR 9423463 OR 9423464)",
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
    "complete_query": "cites:(107483 OR 9423459 OR 9423460 OR 9423461 OR 9423462 OR 9423463 OR 9423464)",
    "indexed_citing_opinions": 866,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107483,
        "count": 793,
        "count_source": "search"
      },
      {
        "opinion_id": 9423459,
        "count": 98,
        "count_source": "search"
      },
      {
        "opinion_id": 9423460,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423461,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423462,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423463,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423464,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1212,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/berger-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwNTcxNDcmcz00ODQwNzk2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107483+OR+9423459+OR+9423460+OR+9423461+OR+9423462+OR+9423463+OR+9423464%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107483,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 96746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 101222,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 102883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 103347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 103481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 105903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107025,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 223783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 227881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 228400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 1087658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 1524136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
        "cited_id": 1649610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107483,
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
    "date_created": "2026-07-04T19:40:23Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:40:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:40:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:47:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:40:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Berger v. New York

```
<opinion type="majority">
<author id="b79-4"><page-number citation-index="1" label="43">*43</page-number>Mr. Justice Clark</author>
<p id="AU3">delivered the opinion of the Court.</p>
<p id="b79-5">This writ tests the validity of New York’s permissive eavesdrop statute, N. Y. Code Crim. Proc. § 813-a,<footnotemark>1</footnotemark> under the Fourth, Fifth, Ninth, and Fourteenth Amendments. The claim is that the statute sets up a system of surveillance which involves trespassory intrusions into private, constitutionally protected premises, authorizes <page-number citation-index="1" label="44">*44</page-number>“general searches” for “mere evidence,” <footnotemark>2</footnotemark> and is an invasion of the privilege against self-incrimination. The trial court upheld the statute, the Appellate Division affirmed without opinion, 25 App. Div. 2d 718, 269 N. Y. S. 2d 368, and the Court of Appeals did likewise by a divided vote. 18 N. Y. 2d 638, <span class="citation" data-id="5523049"><a href="/opinion/5675397/people-v-berger/" aria-description="Citation for case: People v. Berger">219 N. E. 2d 295</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./385/967/">385 U. S. 967</a></span> (1966). We have concluded that the language of New York’s statute is too broad in its sweep resulting in a trespassory intrusion into a constitutionally protected area and is, therefore, violative of the Fourth and Fourteenth Amendments. This disposition obviates the necessity for any discussion of the other points raised.</p>
<p id="b80-5">I.</p>
<p id="b80-6">Berger, the petitioner, was convicted on two counts of conspiracy to bribe the Chairman of the New York State Liquor Authority. The case arose out of the complaint of one Ralph Pansini to the District Attorney’s office that agents of the State Liquor Authority had entered his bar and grill and without cause seized his books and records. Pansini asserted that the raid was in reprisal for his failure to pay a bribe for a liquor license. Numerous complaints had been filed with the District Attorney’s office charging the payment of bribes by applicants for liquor licenses. On the direction of that office, Pansini, while equipped with a “minifon” recording device, interviewed an employee of the Authority. The employee advised Pansini that the price for a license was $10,000 and suggested that he contact attorney Harry Neyer. Neyer subsequently told Pansini that he worked with the Authority employee before and that the latter was aware of the going rate on liquor licenses downtown.</p>
<p id="b81-5"><page-number citation-index="1" label="45">*45</page-number>On the basis of this evidence an eavesdrop order was obtained from a Justice of the State Supreme Court, as provided by § 813-a. The order permitted the installation, for a period of 60 days, of a recording device in Neyer’s office. On the basis of leads obtained from this eavesdrop a second order permitting the installation, for a like period, of a recording device in the office of one Harry Steinman was obtained. After some two weeks of eavesdropping a conspiracy was uncovered involving the issuance of liquor licenses for the Playboy and Tenement Clubs, both of New York City. Petitioner was indicted as “a go-between” for the principal conspirators, who though not named in the indictment were disclosed in a bill of particulars. Relevant portions of the recordings were received in evidence at the trial and were played to the jury, all over the objection of the petitioner. The parties have stipulated that the District Attorney “had no information upon which to proceed to present a case to the Grand Jury, or on the basis of which to prosecute” the petitioner except by the use of the eavesdrop evidence.</p>
<p id="b81-6">HH</p>
<p id="b81-3">Eavesdropping is an ancient practice which at common law was condemned as a nuisance. 4 Blackstone, Commentaries 168. At one time the eavesdropper listened by naked ear under the eaves of houses or their windows, or beyond their walls seeking out private discourse. The awkwardness and undignified manner of this method as well as its susceptibility to abuse was immediately recognized. Electricity, however, provided a better vehicle and with the advent of the telegraph surreptitious interception of messages began. As early as 1862 California found it necessary to prohibit the practice by statute. Statutes of California 1862, p. 288, CCLXII. During the Civil War General J. E. B. Stuart <page-number citation-index="1" label="46">*46</page-number>is reputed to have had his own eavesdropper along with him in the field whose job it was to intercept military communications of the opposing forces. Subsequently newspapers reportedly raided one another’s news gathering lines to save energy, time, and money. Racing news was likewise intercepted and flashed to bettors before the official result arrived.</p>
<p id="b82-5">The telephone brought on a new and more modern eavesdropper known as the “wiretapper.” Interception was made by a connection with a telephone line. This activity has been with us for three-quarters of a century. Like its cousins, wiretapping proved to be a commercial as well as a police technique. Illinois outlawed it in 1895 and in 1905 California extended its telegraph interception prohibition to the telephone. Some 50 years ago a New York legislative committee found that police, in cooperation with the telephone company, had been tapping telephone lines in New York despite an Act passed in 1895 prohibiting it. During prohibition days wiretaps were the principal source of information relied upon by the police as the basis for prosecutions. In 1934 the Congress outlawed the interception without authorization, and the divulging or publishing of the contents of wiretaps by passing § 605 of the Communications Act of 1934.<footnotemark>3</footnotemark> New York, in 1938, declared by constitutional amendment that “[t]he right of the people to be secure against unreasonable interception of telephone and telegraph communications shall not be violated,” but permitted by <em>ex parte </em>order of the Supreme Court of the State the interception of communications on a showing of “reasonable ground to believe that evidence of crime” might be obtained. N. Y. Const. Art. I, § 12.</p>
<p id="b82-6">Sophisticated electronic devices have now been developed (commonly known as “bugs”) which are capable of <page-number citation-index="1" label="47">*47</page-number>eavesdropping on anyone in almost any given situation. They are to be distinguished from “wiretaps” which are confined to the interception of telegraphic and telephonic communications. Miniature in size (%" x <em>%" x </em>%") — no larger than a postage stamp — these gadgets pick up whispers within a room and broadcast them half a block away to a receiver. It is said that certain types of electronic rays beamed at walls or glass windows are capable of catching voice vibrations as they are bounced off the surfaces. Since 1940 eavesdropping has become a big business. Manufacturing concerns offer complete detection systems which automatically record voices under almost any conditions by remote control. A microphone concealed in a book, a lamp, or other unsuspected place in a room, or made into a fountain pen, tie clasp, lapel button, or cuff link increases the range of these powerful wireless transmitters to a half mile. Receivers pick up the transmission with interference-free reception on a special wave frequency. And, of late, a combination mirror transmitter has been developed which permits not only sight but voice transmission up to 300 feet. Likewise, parabolic microphones, which can overhear conversations without being placed within the premises monitored, have been developed. See Westin, Science, Privacy, and Freedom: Issues and Proposals for the 1970's, 66 Col. L. Rev. 1003, 1005-1010.</p>
<p id="b83-5">As science developed these detection techniques, lawmakers, sensing the resulting invasion of individual privacy, have provided some statutory protection for the public. Seven States, California, Illinois, Maryland, Massachusetts, Nevada, New York, and Oregon, prohibit surreptitious eavesdropping by mechanical or electronic device.<footnotemark>4</footnotemark> However, all save Illinois permit official court-<page-number citation-index="1" label="48">*48</page-number>ordered eavesdropping. Some 36 States prohibit wiretapping.<footnotemark>5</footnotemark> But of these, 27 permit “authorized” interception of some type. Federal law, as we have seen, prohibits interception and divulging or publishing of the content of wiretaps without exception.<footnotemark>6</footnotemark> In sum, it is fair to say that wiretapping on the whole is outlawed, except for permissive use by law enforcement officials in <page-number citation-index="1" label="49">*49</page-number>some States; while electronic eavesdropping is — save for seven States — permitted both officially and privately. And, in six of the seven States electronic eavesdropping (“bugging”) is permissible on court order.</p>
<p id="b85-5">III.</p>
<p id="b85-6">The law, though jealous of individual privacy, has not kept pace with these advances in scientific knowledge. This is not to say that individual privacy has been relegated to a second-class position for it has been held since Lord Camden’s day that intrusions into it are “subversive of all the comforts of society.” <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, 1066 (1765). And the Founders so decided a quarter of a century later when they declared in the Fourth Amendment that the people had a right “to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . ..” Indeed, that right, they wrote, “shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” Almost a century thereafter this Court took specific and lengthy notice of <em>Entick </em>v. <em>Carrington, supra, </em>finding that its holding was undoubtedly familiar to and “in the minds of those who framed the Fourth Amendment . . . .” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-627</a></span> (1886). And after quoting from Lord Camden’s opinion at some length, Mr. Justice Bradley characterized it thus:</p>
<blockquote id="b85-7">“The principles laid down in this opinion affect the very essence of constitutional liberty and security. They reach farther than the concrete form of the case . . . they apply to all invasions on the part of the government and its employes of the sanctity of a man’s home and the privacies of life.” At 630.</blockquote>
<p id="b86-4"><page-number citation-index="1" label="50">*50</page-number><em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span> </em>held unconstitutional an Act of the Congress authorizing a court of the United States to require a defendant in a revenue case to produce in court his private books, invoices, and papers or else the allegations of the Government were to be taken as confessed. The Court found that “the essence of the offense . . , [was] the invasion of this sacred right which underlies and constitutes the essence of Lord Camden’s judgment.” <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Ibid.</a></span> </em>The Act — the Court found — violated the Fourth Amendment in that it authorized a general search contrary to the Amendment’s guarantee.</p>
<p id="b86-5">The Amendment, however, carried no criminal sanction, and the federal statutes not affording one, the Court in 1914 formulated and pronounced the federal exclusionary rule in <em>Weeks v. United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. Prohibiting the use in federal courts of any evidence seized in- violation of the Amendment, the Court held:</p>
<blockquote id="b86-6">“The effect of the Fourth Amendment is to put the courts of the United States . . . under limitations and restraints as to the exercise of such power . . . and to forever secure the people . . . against all unreasonable searches and seizures under the guise of law. This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all ... . The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures . . . should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.” At 391-392.</blockquote>
<p id="b86-7">IV.</p>
<p id="b86-8">The Court was faced with its first wiretap case in 1928, <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>. There <page-number citation-index="1" label="51">*51</page-number>the interception of Olmstead’s telephone line was accomplished without entry upon his premises and was, therefore, found not to be proscribed by the Fourth Amendment. The basis of the decision was that the Constitution did not forbid the obtaining of evidence by wiretapping unless it involved actual unlawful entry into the house. Statements in the opinion that a conversation passing over a telephone wire cannot be said to come within the Fourth Amendment’s enumeration of “persons, houses, papers, and effects” have been negated by our subsequent cases as hereinafter noted. They found “conversation” was within the Fourth Amendment’s protections, and that the use of electronic devices to capture it was a “search” within the meaning of the Amendment, and we so hold. In any event, Congress soon thereafter, and some say in answer to <em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">Olmstead</a></span>, </em>specifically prohibited the interception without authorization and the divulging or publishing of the contents of telephonic communications. And the <em>Nardone </em>cases, <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span> (1937) and <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939), extended the exclusionary rule to wiretap evidence offered in federal prosecutions.</p>
<p id="b87-5">The first “bugging” case reached the Court in 1942 in <em>Goldman </em>v. <em>United States, </em><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>. There the Court found that the use of a detectaphone placed against an office wall in order to hear private conversations in the office next door did not violate the Fourth Amendment because there was no physical trespass in connection with the relevant interception. And in <em>On Lee </em>v. <em>United States, </em><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span> (1952), we found that since “no trespass was committed” a conversation between Lee and a federal agent, occurring in the former’s laundry and electronically recorded, was not condemned by the Fourth Amendment. Thereafter in <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), the Court found “that the eavesdropping was accomplished by means of <page-number citation-index="1" label="52">*52</page-number>an unauthorized physical penetration into the premises occupied by the petitioners.” At 509. A spike a foot long with a microphone attached to it was inserted under a baseboard into a party wall until it made contact with the heating duct that ran through the entire house occupied by Silverman, making a perfect sounding board through which the conversations in question were overheard. Significantly, the Court held that its decision did “not turn upon the technicality of a trespass upon a party wall as a matter of local law. It is based upon the reality of an actual intrusion into a constitutionally protected area.” At 512.</p>
<p id="b88-6">In <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), the Court for the first time specifically held that verbal evidence may be the fruit of official illegality under the Fourth Amendment along with the more common tangible fruits of unwarranted intrusion. It used these words:</p>
<blockquote id="b88-7">“The exclusionary rule has traditionally barred from trial physical, tangible materials obtained either during or as a direct result of an unlawful invasion. It follows from our holding in <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>, that the Fourth Amendment may protect against the overhearing of verbal statements as well as against the more traditional seizure of ‘papers and effects.’ ” At 485.</blockquote>
<p id="b88-8">And in <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963), the Court confirmed that it had “in the past sustained instances of ‘electronic eavesdropping’ against constitutional challenge, when devices have been used to enable government agents to overhear conversations which would have been beyond the reach of the human ear. ... It has been insisted only that the electronic device not be planted by an unlawful physical invasion of a constitutionally protected area.” At 438-439. In <page-number citation-index="1" label="53">*53</page-number>this case a recording of a conversation between a federal agent and the petitioner in which the latter offered the agent a bribe was admitted in evidence. Rather than constituting “eavesdropping” the Court found that the recording “was used only to obtain the most reliable evidence possible of a conversation in which the Government’s own agent was a participant and which that agent was fully entitled to disclose.” At 439.</p>
<p id="AP">V.</p>
<p id="b89-6">It is now well settled that “the Fourth Amendment’s right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth” Amendment. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961). “The security of one’s privacy against arbitrary intrusion by the police — which is at the core of the Fourth Amendment — is basic to a free society.” <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span> (1949). And its “fundamental protections . . . are guaranteed . . . against invasion by the States.” <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481</a></span> (1965). This right has most recently received enunciation in <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>. “The basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials.” At 528. Likewise the Court has decided that while the “standards of reasonableness” required under the Fourth Amendment are the same under the Fourteenth, they “are not susceptible of Procrustean application . . . .” <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963). We said there that “the reasonableness of a search is . . . [to be determined] by the trial court from the facts and circumstances of the case and in the light of the 'fundamental criteria’ laid down by the Fourth Amendment and in opinions of this Court applying that Amendment.” <em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ibid.</a></span></em></p>
<p id="b90-3"><page-number citation-index="1" label="54">*54</page-number>We, therefore, turn to New York’s statute to determine the basis of the search and seizure authorized by it upon the order of a state supreme court justice, a county judge or general sessions judge of New York County. Section 813-a authorizes the issuance of an “ex parte order for eavesdropping” upon “oath or affirmation of a district attorney, or of the attorney-general or of an officer above the rank of sergeant of any police department of the state or of any political subdivision thereof . . . .” The oath must state “that there is reasonable ground to believe that evidence of crime may be thus obtained, and particularly describing the person or persons whose communications, conversations or discussions are to be overheard or recorded and the purpose thereof, and . . . identifying the particular telephone number or telegraph line involved.” The judge “may examine on oath the applicant and any other witness he may produce and shall satisfy himself of the existence of reasonable grounds for the granting of such application.” The order' must specify the duration of the eavesdrop — not exceeding two months unless extended— and “[a]ny such order together with the papers upon which the application was based, shall be delivered to and retained by the applicant as authority for the eaves-» dropping authorized therein.”</p>
<p id="b90-4">While New York’s statute satisfies the Fourth Amendment’s requirement that a neutral and detached authority be interposed between the police and the public, <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), the broad sweep of the statute is immediately observable. It permits the issuance of the order, or warrant for eavesdropping, upon the oath of the attorney general, the district attorney or any police officer above the rank of sergeant stating that “there is reasonable ground to believe that evidence of crime may be thus obtained . . . .” Such a requirement raises a serious <page-number citation-index="1" label="55">*55</page-number>probable-cause question under the Fourth Amendment. Under it warrants may only issue “but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” Probable cause under the Fourth Amendment exists where the facts and circumstances within the affiant’s knowledge, and of which he has reasonably trustworthy information, are sufficient unto themselves to warrant a man of reasonable caution to believe that an offense has been or is being committed. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925); <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931) ; <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949).</p>
<p id="b91-5">It is said, however, by the petitioner, and the State agrees, that the “reasonable ground” requirement of § 813-a “is undisputedly equivalent to the probable cause requirement of the Fourth Amendment.” This is indicated by <em>People </em>v. <em>Grossman, </em><span class="citation" data-id="6186214"><a href="/opinion/6317761/people-v-grossman/" aria-description="Citation for case: People v. Grossman">45 Misc. 2d 557</a></span>, 257 N. Y. S. 2d 266, reversed on other grounds, 27 App. Div. 2d 572, 276 N. Y. S. 2d 168. Also see <em>People </em>v. <em>Beshany, </em><span class="citation" data-id="6185305"><a href="/opinion/6316865/people-v-beshany/" aria-description="Citation for case: People v. Beshany">43 Misc. 2d 521</a></span>, 252 N. Y. S. 2d 110. While we have found no case on the point by New York’s highest court, we need not pursue the question further because we have concluded that the statute is deficient on its face in other respects. Since petitioner clearly has standing to challenge the statute, being indisputably affected by it, we need not consider either the sufficiency of the affidavits upon which the eavesdrop orders were based, or the standing of petitioner to attack the search and seizure made thereunder.</p>
<p id="b91-6">The Fourth Amendment commands that a warrant issue not only upon probable cause supported by oath or affirmation, but also “particularly describing the place to be searched, and the persons or things to be seized.” New York’s statute lacks this particularization. It merely says that a warrant may issue on reasonable <page-number citation-index="1" label="56">*56</page-number>ground to believe that evidence of crime may be obtained by the eavesdrop. It lays down no requirement for particularity in the warrant as to what specific crime has been or is being committed, nor “the place to be searched,” or “the persons or things to be seized” as specifically required by the Fourth Amendment. The need for particularity and evidence of reliability in the showing required when judicial authorization of a search is sought is especially great in the case of eavesdropping. By its very nature eavesdropping involves an intrusion on privacy that is broad in scope. As was said in <em>Osborn </em>v. <em>United States, </em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span> (1966), the “indiscriminate use of such devices in law enforcement raises grave constitutional questions under the Fourth and Fifth Amendments,” and imposes “a heavier responsibility on this Court in its supervision of the fairness of procedures . . . .” At 329, n. 7. There, two judges acting jointly authorized the installation of a device on the person of a prospective witness to record conversations between him and an attorney for a defendant then on trial in the United States District Court. The judicial authorization was based on an affidavit of the witness setting out in detail previous conversations between the witness and the attorney concerning the bribery of jurors in the case. The recording device was, as the Court said, authorized “under the most precise and discriminate circumstances, circumstances which fully met the 'requirement of particularity’ ” of the Fourth Amendment. The Court was asked to exclude the evidence of the recording of the conversations seized pursuant to the order on constitutional grounds, <em>Weeks </em>v. <em>United States, supra, </em>or in the exercise of supervisory power, <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span> (1943). The Court refused to do so finding that the recording, although an invasion of the privacy protected by the <page-number citation-index="1" label="57">*57</page-number>Fourth Amendment, was admissible because of the authorization of the judges, based upon “a detailed factual affidavit alleging the commission of a specific criminal offense directly and immediately affecting the administration of justice ... for the narrow and particularized purpose of ascertaining the truth of the affidavit’s allegations.” At 330. The invasion was lawful because there was sufficient proof to obtain a search warrant to make the search for the limited purpose outlined in the order of the judges. Through these “precise and discriminate” procedures the order authorizing the use of the electronic device afforded similar protections to those that are present in the use of conventional warrants authorizing the seizure of tangible evidence. Among other safeguards, the order described the type of conversation sought with particularity, thus indicating the specific objective of the Government in entering the constitutionally protected area and the limitations placed upon the officer executing the warrant. Under it the officer could not search unauthorized areas; likewise, once the property sought, and for which the order was issued, was found the officer could not use the order as a passkey to further search. In addition, the order authorized one limited intrusion rather than a series or a continuous surveillance. And, we note that a new order was issued when the officer sought to resume the search and probable cause was shown for the succeeding one. Moreover, the order was executed by the officer with dispatch, not over a prolonged and extended period. In this manner no greater invasion of privacy was permitted than was necessary under the circumstances. Finally the officer was required to and did make a return on the order showing how it was executed and what was seized. Through these strict precautions the danger of an unlawful search and seizure was minimized.</p>
<p id="b94-5"><page-number citation-index="1" label="58">*58</page-number>By contrast, New York’s statute lays down no such “precise and discriminate” requirements. Indeed, it authorizes the “indiscriminate use” of electronic devices as specifically condemned in <em><span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">Osborn</a></span>. </em>“The proceeding by search warrant is a drastic one,” <em>Sgro </em>v. <em>United States, </em><span class="citation" data-id="9418758"><a href="/opinion/101970/sgro-v-united-states/#210" aria-description="Citation for case: Sgro v. United States">287 U. S. 206, 210</a></span> (1932), and must be carefully circumscribed so as to prevent unauthorized invasions of “the sanctity of a man’s home and the privacies of life.” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span>. New York’s broadside authorization rather than being “carefully circumscribed” so as to prevent unauthorized invasions of privacy actually permits general searches by electronic devices, the truly offensive character of which was first condemned in <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, and which were then known as “general warrants.” The use of the latter was a motivating factor behind the Declaration of Independence. In view of the many cases commenting on the practice it is sufficient here to point out that under these “general warrants” customs officials were given blanket authority to conduct general searches for goods imported to the Colonies in violation of the tax laws of the Crown. The Fourth Amendment’s requirement that a warrant “particularly describ[e] the place to be searched, and the persons or things to be seized,” repudiated these general warrants and “makes general searches . . . impossible and prevents the seizure of one thing under a warrant describing another. As to what is to be taken, nothing is left to the discretion of the officer executing the warrant.” <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#196" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 196</a></span> (1927); <em>Stanford </em>v. <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas, supra.</a></span></em></p>
<p id="b94-6">We believe the statute here is equally offensive. First, as we have mentioned, eavesdropping is authorized without requiring belief that any particular offense has been or is being committed; nor that the “property” <page-number citation-index="1" label="59">*59</page-number>sought, the conversations, be particularly described. The purpose of the probable-cause requirement of the Fourth Amendment, to keep the state out of constitutionally protected areas until it has reason to believe that a specific crime has been or is being committed, is thereby wholly aborted. Likewise the statute’s failure to describe with particularity the conversations sought gives the officer a roving commission to “seize” any and all conversations. It is true that the statute requires the naming of “the person or persons whose communications, conversations or discussions are to be overheard or recorded . . . .” But this does no more than identify the person whose constitutionally protected area is to be invaded rather than “particularly describing” the communications, conversations, or discussions to be seized. As with general warrants this leaves too much to the discretion of the officer executing the order. Secondly, authorization of eavesdropping for a two-month period is the equivalent of a series of intrusions, searches, and seizures pursuant to a single showing of probable cause. Prompt execution is also avoided. During such a long and continuous (24 hours a day) period the conversations of any and all persons coming into the area covered by the device will be seized indiscriminately and without regard to their connection with the crime under investigation. Moreover, the statute permits, and there were authorized here, extensions of the original two-month period — presumably for two months each — on a mere showing that such extension is “in the public interest.” Apparently the original grounds on which the eavesdrop order was initially issued also form the basis of the renewal. This we believe insufficient without a showing of present probable cause for the continuance of the eavesdrop. Third, the statute places no termination date on the eavesdrop once the conversation sought is <page-number citation-index="1" label="60">*60</page-number>seized. This is left entirely in the discretion of the officer. Finally, the statute's procedure, necessarily because its success depends on secrecy, has no requirement for notice as do conventional warrants, nor does it overcome this defect by requiring some showing of special facts. On the contrary, it permits unconsented entry without any showing of exigent circumstances. Such a showing of exigency, in order to avoid notice, would appear more important in eavesdropping, with its inherent dangers, than that required when conventional procedures of search and seizure are utilized. Nor does the statute provide for a return on the warrant thereby leaving full discretion in the officer as to the use of seized conversations of innocent as well as guilty parties. In short, the statute's blanket grant of permission to eavesdrop is without adequate judicial supervision or protective procedures.</p>
<p id="b96-4">VI.</p>
<p id="b96-5">It is said with fervor that electronic eavesdropping is a most important technique of law enforcement and that outlawing it will severely cripple crime detection. The monumental report of the President’s Commission on Law Enforcement and Administration of Justice entitled “The Challenge of Crime in a Free Society” informs us that the majority of law enforcement officials say that this is especially true in the detection of organized crime. As the Commission reports, there can be no question about the serious proportions of professional criminal activity in this country. However, we have found no empirical statistics on the use of electronic devices (bugging) in the fight against organized crime. Indeed, there are even figures available in the wiretap category which indicate to the contrary. See District Attorney Silver’s Poll of New York Prosecutors, in Dash, Schwartz &amp; Knowlton, The Eavesdroppers 105, <em>117-119 </em><page-number citation-index="1" label="61">*61</page-number>(1959). Also see Semerjian, Proposals on Wiretapping in Light of Recent Senate Hearings, 45 B. U. L. Rev. 217, 229. As the Commission points out, “[w]iretapping was the mainstay of the New York attack against organized crime until Federal court decisions intervened. Recently chief reliance in some offices has been placed on bugging, where the information is to be used in court. Law enforcement officials believe that the successes achieved in some parts of the State are attributable primarily to a combination of dedicated and competent personnel and adequate legal tools; and that the failure to do more in New York has resulted primarily from the failure to commit additional resources of time and men,” rather than electronic devices. At 201-202. Moreover, Brooklyn's District Attorney Silver’s poll of the State of New York indicates that during the 12-year period (1942-1954) duly authorized wiretaps in bribery and corruption cases constituted only a small percentage of the whole. It indicates that this category involved only 10% of the total wiretaps. The overwhelming majority were in the categories of larceny, extortion, coercion, and blackmail, accounting for almost 50%. Organized gambling was about 11%. Statistics are not available on subsequent years. Dash, Schwartz &amp; Knowlton, <em>supra, </em>at 40.</p>
<p id="b97-5">An often repeated statement of District Attorney Hogan of New York County was made at a hearing before the Senate Judiciary Committee at which he advocated the amendment of the Communications Act of 1934, <em>supra, </em>so as to permit “telephonic interception” of conversations. As he testified, “Federal statutory law [the 1934 Act] has been interpreted in such a way as to bar us from divulging wiretap evidence, even in the courtroom in the course of criminal prosecution.” Mr. Hogan then said that “[wjithout it [wiretaps] my own office could not have convicted” “top figures in <page-number citation-index="1" label="62">*62</page-number>the underworld.” He then named nine persons his office had convicted and one on whom he had furnished "leads” secured from wiretaps to the authorities of New Jersey. Evidence secured from wiretaps, as Mr. Hogan said, was not admissible in “criminal prosecutions.” He was advocating that the Congress adopt a measure that would make it admissible; Hearings on S. 2813 and S. 1495, before the Senate Committee on the Judiciary, 87th Cong., 2d Sess., pp. 173, 174 (1962). The President’s Commission also emphasizes in its report the need for wiretapping in the investigation of organized crime because of the telephone’s “relatively free use” by those engaged in the business and the difficulty of infiltrating their organizations. P. 201. The Congress, though long importuned, has not amended the 1934 Act to permit it.</p>
<p id="b98-6">We are also advised by the Solicitor General of the United States that the Federal Government has abandoned the use of electronic eavesdropping for “prose-cutorial purposes.” See Supplemental Memorandum, <em>Schipani </em>v. <em>United States, </em>No. 504, October Term, 1966, <span class="citation" data-id="107323"><a href="/opinion/107323/schipani-v-united-states/" aria-description="Citation for case: Schipani v. United States">385 U. S. 372</a></span>. See also <em>Black </em>v. <em>United States, </em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">385 U. S. 26</a></span> (1966); <em>O’Brien </em>v. <em>United States, </em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">386 U. S. 345</a></span> (1967); <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="107456"><a href="/opinion/107456/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">387 U. S. 231</a></span> (1967); <em>Markis </em>v. <em>United States, </em><span class="citation" data-id="1524136"><a href="/opinion/1524136/markis-v-united-states/" aria-description="Citation for case: Markis v. United States">387 U. S. 425</a></span>; <em>Moretti </em>v. <em>United States, </em><span class="citation" data-id="1524136"><a href="/opinion/1524136/markis-v-united-states/" aria-description="Citation for case: Markis v. United States">387 U. S. 425</a></span>. Despite these actions of the Federal Government there has been no failure of law enforcement in that field.</p>
<p id="b98-7">As The Chief Justice said in concurring in the result in <em>Lopez </em>v. <em>United States, </em><span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>, “the fantastic advances in the field of electronic communication constitute a great danger to the privacy of the individual; . . . indiscriminate use of such devices in law enforcement raises grave constitutional questions under the Fourth and Fifth Amendments . . . .” At 441.</p>
<p id="b98-8">In any event we cannot forgive the requirements of the Fourth Amendment in the name of law enforcement. <page-number citation-index="1" label="63">*63</page-number>This is no formality that we require today but a fundamental rule that has long been recognized as basic to the privacy of every home in America. While “[t]he requirements of the Fourth Amendment are not inflexible, or obtusely unyielding to the legitimate needs of law enforcement,” <em>Lopez </em>v. <em>United States, supra, </em>at 464 (dissenting opinion of Brennan, J.), it is not asking too much that officers be required to comply with the basic command of the Fourth Amendment before the innermost secrets of one’s home or office are invaded. Few threats to liberty exist which are greater than that posed by the use of eavesdropping devices. Some may claim that without the use of such devices crime detection in certain areas may suffer some delays since eavesdropping is quicker, easier, and more certain. However, techniques and practices may well be developed that will operate just as speedily and certainly and — what is more important — without attending illegality.</p>
<p id="b99-5">It is said that neither a warrant nor a statute authorizing eavesdropping can be drawn so as to meet the Fourth Amendment’s requirements. If that be true then the “fruits” of eavesdropping devices are barred under the Amendment. On the other hand this Court has in the past, under specific conditions and circumstances, sustained the use of eavesdropping devices. See <em>Goldman </em>v. <em>United States, </em><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; <em>On Lee </em>v. <em>United States, </em><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>; <em>Lopez </em>v. <em>United States, supra; </em>and <em>Osborn </em>v. <em>United States, supra. </em>In the latter case the eavesdropping device was permitted where the “commission of a specific offense” was charged, its use was “under the most precise and discriminate circumstances” and the effective administration of justice in a federal court was at stake. The States are under no greater restrictions. The Fourth Amendment does not make the “precincts of the home or the office . . . sanctuaries where the law can never reach,” Douglas, J., dissenting in <em>Warden, </em><page-number citation-index="1" label="64">*64</page-number><em>Maryland Penitentiary </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#321" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 321</a></span>, but it does prescribe a constitutional standard that must be met before official invasion is permissible. Our concern with the statute here is whether its language permits a trespassory invasion of the home or office, by general warrant, contrary to the command of the Fourth Amendment. As it is written, we believe that it does.</p>
<p id="b100-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b79-6"> “§ 813-a. Ex parte order for eavesdropping</p>
<blockquote id="b79-7">“An ex parte order for eavesdropping as defined in subdivisions one and two of section seven hundred thirty-eight of the penal law may be issued by any justice of the supreme court or judge of a county court or of the court of general sessions of the county of New York upon oath or affirmation of a district attorney, or of the attorney-general or of an officer above the rank of sergeant of any police department of the state or of any political subdivision thereof, that there is reasonable ground to believe that evidence of crime may be thus obtained, and particularly describing the person or persons whose communications, conversations or discussions are to be overheard or recorded and the purpose thereof, and, in the case of a telegraphic or telephonic communication, identifying the particular telephone number or telegraph line involved. In connection with the issuance of such an order the justice or judge may examine on oath the applicant and any other witness he may produce and shall satisfy himself of the existence of reasonable grounds for the granting of such application. Any such order shall be effective for the time specified therein but not for a period of more than two months unless extended or renewed by the justice or judge who signed and issued the original order upon satisfying himself that such extension or renewal is in the public interest. Any such order together with the papers upon which the application was based, shall be delivered to and retained by the applicant as authority for the eavesdropping authorized therein. A true copy of such order shall at all times be retained in his possession by the judge or justice issuing the same, and, in the event of the denial of an application for such an order, a true copy of the papers upon which the application was based shall in like manner be retained by the judge or justice denying the same. As amended L. 1958, c. 676, eff. July 1, 1958.”</blockquote>
</footnote>
<footnote label="2">
<p id="b80-7"> This contention is disposed of in <em>Warden, Maryland Penitentiary </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, adversely to petitioner’s assertion here.</p>
</footnote>
<footnote label="3">
<p id="b82-7"> <span class="citation no-link">48 Stat. 1103</span>, <span class="citation no-link">47 U. S. C. § 605</span>.</p>
</footnote>
<footnote label="4">
<p id="b83-6"> Cal. Pen. Code §§ 653h-j; Ill. Rev. Stat., c. 38, §§ 14-1 to 14-7 (1965); Md. Ann. Code, Art. 27, § 125A (1957); Mass. Gen, Laws, <page-number citation-index="1" label="48">*48</page-number>c. 272, § 99 (Supp. 1966); <span class="citation no-link">Nev. Rev. Stat. § 200.650</span> (1963); N. Y. Pen. Law § 738 (Supp. 1966); Ore. Rev. Stat. § 165.540 (1) (c) (Supp. 1965).</p>
</footnote>
<footnote label="5">
<p id="b84-9"> Ala. Code, Tit. 48, § 414 (1958); <span class="citation no-link">Alaska Stat. § 42.20.100</span> (1962) ; Ark. Stat. Ann. § 73-1810 (1957); <span class="citation no-link">Cal. Pen. Code § 640</span>; <span class="citation no-link">Colo. Rev. Stat. Ann. § 40-4-17</span> (1963); Conn. Gen. Stat. Rev. § 53-140 (1958); Del. Code Ann., Tit. 11, §757 (Supp. 1966); <span class="citation no-link">Fla. Stat. §822.10</span> (1965); Hawaii Rev. Laws §309A-1 (Supp. 1963); <span class="citation no-link">Idaho Code Ann. §§18-6704</span>, 6705 (1947); Ill. Rev. Stat., c. 134, § 16 (1965) ; <span class="citation no-link">Iowa Code § 716.8</span> (1962); Ky. Rev. Stat. §433.430 (1962); La. Rev. Stat. § 14:322 (1950); Md. Ann. Code, Art. 35, §§92, 93 (1957); Mass. Gen. Laws, c. 272, §99 (Supp. 1966); Mich. Stat. Ann. §28.808 (1954); Mont. Rev. Codes Ann. §94^3203 (Supp. 1965); <span class="citation no-link">Neb. Rev. Stat. § 86-328</span> (1966); <span class="citation no-link">Nev. Rev. Stat. §§ 200.620</span>, 200.630 (1963); N. J. Rev. Stat. §2A:146-1 (1953); N. M. Stat. Ann. § 40A-12-1 (1964); N. Y. Pen. Law § 738 (Supp. 1966); N. C. Gen. Stat. § 14-155 (1953); N. D. Cent. Code § 8-10-07 (1959); <span class="citation no-link">Ohio Rev. Code Ann. §4931.28</span> (1954); Okla. Stat., Tit. 21, §1757 (1961); Ore. Rev. Stat. § 165.540 (1) (Supp. 1965); Pa. Stat. Ann., Tit. 15, § 2443 (1958); R. I. Gen. Laws Ann. § 11-35-12 (1956) ; S. D. Code § 13.4519 (1939); <span class="citation no-link">Tenn. Code Ann. § 65-2117</span> (1955); <span class="citation no-link">Utah Code Ann. §76-48-11</span> (1953); <span class="citation no-link">Va. Code Ann. §18.1-156</span> (1960 Repl. Vol.); Wis. Stat, § 134.39 (1963); <span class="citation no-link">Wyo. Stat. Ann. §37-259</span> (1957).</p>
</footnote>
<footnote label="6">
<p id="b84-10"> A recent Federal Communications Commission Regulation, <span class="citation no-link">31 Fed. Reg. 3400</span>, <span class="citation no-link">47 CFR § 2.701</span>, prohibits the use of “a device required to be licensed by section 301 of the Communications Act” for the purpose of eavesdropping. This regulation, however, exempts use under “lawful authority” by police officers and the sanctions are limited to loss of license and the imposition of a fine. The memorandum accompanying the regulation stated: “What constitutes a crime under State law reflecting State policy applicable to radio eavesdropping is, of course, unaffected by our rules.” <em>Id., </em>at 3399.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Berghuis v. Thompkins.md  (`case`, 5 assertions)

### content_page

```
---
title: "Berghuis v. Thompkins"
type: case
citation: ""
parallel_cite: "176 L. Ed. 2d 1098; 130 S. Ct. 2250; 560 U.S. 370; 22 Fla. L. Weekly Fed. S 375; 78 U.S.L.W. 4479"
neutral_cite: 2010 U.S. LEXIS 4379
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2010
date_decided: 2010-06-01
docket: 08-1470
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2010-06-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Berghuis v. Thompkins
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/6796082/berghuis-v-thompkins/"
  cluster_id: 6796082
  opinion_id: 6680916
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Anchor"
related: ["[[Davis v. United States]]", "[[North Carolina v. Butler]]", "[[Michigan v. Mosley]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "waiver", "invocation", "right-to-remain-silent"]
holding: "The right to remain silent must be invoked UNAMBIGUOUSLY; merely staying silent does not invoke it, and a suspect who answers questions…"
lake:
  record_id: Berghuis v. Thompkins
  status: verified
  projected_at: 2026-07-06
---

# Berghuis v. Thompkins

*560 U.S. 370 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Thompkins was arrested for a fatal shooting and given [[Miranda and Custodial Interrogation|Miranda warnings]], which he declined to sign an acknowledgment of. During an interrogation lasting about three hours he was nearly silent, saying almost nothing. Near the end an officer asked whether he prayed to God to forgive him for "shooting that boy down," and Thompkins answered "Yes." That answer was admitted at trial and he was convicted of first-degree murder.

## Issue
(1) Whether Thompkins invoked his right to remain silent by staying largely silent for nearly three hours; and (2) whether he waived that right by answering the officer's question after receiving and understanding the warnings.

## Rule
Silence alone does not invoke the right; the invocation must be unambiguous, just as for the right to counsel. "Had he made either of these simple, unambiguous statements [that he wanted to remain silent or did not want to talk], he would have invoked his 'right to cut off questioning.' . . . Here he did neither, so he did not invoke his right to remain silent." — 560 U.S. at 382. ^pin-382

And a suspect waives the right by an uncoerced statement after understanding the warnings: "In sum, a suspect who has received and understood the Miranda warnings, and has not invoked his Miranda rights, waives the right to remain silent by making an uncoerced statement to the police." — *Id.* at 388 (slip op., at 17). ^pin-388

## Application
Thompkins never said he wanted to remain silent or to stop the questioning, so his prolonged silence did not invoke the right. Because he had received the warnings and did not contend he failed to understand them, his uncoerced one-word answer to the officer's question was a course of conduct establishing an implied waiver. On these facts the statement was admissible, and the police were not required to obtain an express waiver before questioning him.

## Conclusion
Thompkins did not invoke his right to remain silent and waived it through his uncoerced answer; the state court's rejection of his Miranda claim was correct, and the Sixth Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Berghuis* extends the [[Davis v. United States]] unambiguous-invocation rule (originally about the right to counsel) to the right to remain silent, and confirms implied waiver under [[North Carolina v. Butler]] from an uncoerced statement by a suspect who understood the warnings.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Anchor*

## Sources
- *Berghuis v. Thompkins*, 560 U.S. 370 (2010) — https://www.courtlistener.com/opinion/147529/berghuis-v-thompkins/ — pinpoints: 382, 388 (CL carries the slip opinion; waiver holding at slip op. 17).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7bbe3b79969db991", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2010 U.S. LEXIS 4379", "official_citation_present": false, "parallel_cite": "176 L. Ed. 2d 1098; 130 S. Ct. 2250; 560 U.S. 370; 22 Fla. L. Weekly Fed. S 375; 78 U.S.L.W. 4479", "title": "Berghuis v. Thompkins", "year": "2010"}}
{"assertion_id": "15c73a06befde574", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The right to remain silent must be invoked UNAMBIGUOUSLY; merely staying silent does not invoke it, and a suspect who answers questions…", "title": "Berghuis v. Thompkins"}}
{"assertion_id": "3f674d0022b18a1f", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Anchor", "title": "Berghuis v. Thompkins"}}
{"assertion_id": "10db24cac6b26fc5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2010-06-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Berghuis v. Thompkins", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Berghuis v. Thompkins", "varies_by_point": "false"}}
{"assertion_id": "1df9fdf44fc47253", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Berghuis v. Thompkins"}}
```

### lake record — Berghuis v. Thompkins

```json
{
  "schema_version": "s2.v1",
  "record_id": "Berghuis v. Thompkins",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Berghuis v. Thompkins",
    "case_name_short": "Berghuis",
    "case_name_full": "MARY BERGHUIS, WARDEN v. VAN CHESTER THOMPKINS",
    "input_case_name": "Berghuis v. Thompkins",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2010-06-01",
    "year": 2010,
    "docket": "08-1470",
    "cluster_id": 6796082,
    "lead_opinion_id": 6680916,
    "sibling_ids": [
      6680916,
      6680917
    ],
    "absolute_url": "/opinion/6796082/berghuis-v-thompkins/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 147529,
        "score": 110,
        "case_name": "Berghuis v. Thompkins"
      },
      {
        "cluster_id": 7337135,
        "score": 10,
        "case_name": "Berghuis v. Thompkins"
      },
      {
        "cluster_id": 6788362,
        "score": 10,
        "case_name": "Berghuis v. Thompkins"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "176 L. Ed. 2d 1098",
        "volume": "176",
        "reporter": "L. Ed. 2d",
        "page": "1098",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2250",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 370",
        "volume": "560",
        "reporter": "U.S.",
        "page": "370",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 375",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4479",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4479",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. LEXIS 4379",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4379",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "176 L. Ed. 2d 1098",
        "volume": "176",
        "reporter": "L. Ed. 2d",
        "page": "1098",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. LEXIS 4379",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "4379",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 2250",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "2250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "560 U.S. 370",
        "volume": "560",
        "reporter": "U.S.",
        "page": "370",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 375",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "375",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 U.S.L.W. 4479",
        "volume": "78",
        "reporter": "U.S.L.W.",
        "page": "4479",
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
      "id": "pin-382",
      "page": null,
      "quote": "That answer was admitted at trial and he was convicted of first-degree murder. ## Issue (1) Whether Thompkins invoked his right to remain silent by staying largely silent for nearly three hours; and (2) whether he waived that right by answering the officer's question after receiving and understanding the warnings. ## Rule Silence alone does not invoke the right; the invocation must be unambiguous, just as for the right to counsel.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-388",
      "page": null,
      "quote": "In sum, a suspect who has received and understood the Miranda warnings, and has not invoked his Miranda rights, waives the right to remain silent by making an uncoerced statement to the police.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-06-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Berghuis v. Thompkins",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Williams v. Davis",
          "cluster_id": 7320834,
          "cite": [
            "192 F. Supp. 3d 732",
            "2016 WL 3523876"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Patton",
          "cluster_id": 2669580,
          "cite": [
            "287 Neb. 899"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hernandez",
          "cluster_id": 4497144,
          "cite": [
            "299 Neb. 896",
            "911 N.W.2d 524"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado, IN the INTEREST OF Minor Child: B.H. and B.H., Minor Child v. D.H.",
          "cluster_id": 10018910,
          "cite": [
            "488 P.3d 1026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Myers (Slip Opinion)",
          "cluster_id": 4498685,
          "cite": [
            "2018 Ohio 1903",
            "114 N.E.3d 1138",
            "154 Ohio St. 3d 405"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donald Dallas v. Warden",
          "cluster_id": 4767554,
          "cite": [
            "964 F.3d 1285"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oliver",
          "cluster_id": 182380,
          "cite": [
            "630 F.3d 397",
            "2011 U.S. App. LEXIS 289",
            "2011 WL 38035"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salts v. Epps",
          "cluster_id": 626317,
          "cite": [
            "676 F.3d 468",
            "2012 WL 1034026"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tench",
          "cluster_id": 7178800,
          "cite": [
            "123 N.E.3d 955",
            "156 Ohio St. 3d 85",
            "2018 Ohio 5205"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martin (Slip Opinion)",
          "cluster_id": 4425665,
          "cite": [
            "2017 Ohio 7556"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Davis",
          "cluster_id": 8443655,
          "cite": [
            "901 F.3d 578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Capers",
          "cluster_id": 180156,
          "cite": [
            "627 F.3d 470",
            "2010 U.S. App. LEXIS 24516",
            "2010 WL 4869768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Burries",
          "cluster_id": 4438267,
          "cite": [
            "900 N.W.2d 483",
            "297 Neb. 367"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damion Hayes v. Secretary, Florida Department of Corrections",
          "cluster_id": 5044093,
          "cite": [
            "10 F.4th 1203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 4799752,
          "cite": [
            "474 P.3d 722"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coombs",
          "cluster_id": 4393307,
          "cite": [
            "857 F.3d 439",
            "2017 U.S. App. LEXIS 8832",
            "2017 WL 2198118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 9427492,
          "cite": [
            "82 F.4th 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Farra",
          "cluster_id": 6464381,
          "cite": [
            "2022 Ohio 1421"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo",
          "cluster_id": 173724,
          "cite": [
            "617 F.3d 565",
            "2010 U.S. App. LEXIS 17281",
            "2010 WL 3260805"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sutton",
          "cluster_id": 10646144,
          "cite": [
            "319 Neb. 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hinkley",
          "cluster_id": 3006252,
          "cite": [
            "803 F.3d 85",
            "2015 U.S. App. LEXIS 17215",
            "2015 WL 5719626"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hinkson v. State",
          "cluster_id": 10367329,
          "cite": [
            "850 S.E.2d 41",
            "310 Ga. 388"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guillen",
          "cluster_id": 4877545,
          "cite": [
            "995 F.3d 1095"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Clifton",
          "cluster_id": 4400956,
          "cite": [
            "892 N.W.2d 112",
            "296 Neb. 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berghuis v. Thompkins:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(6680916 OR 6680917) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 131,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 131,
        "triage_read": 3,
        "triage_snippet_classified": 128
      },
      "lane2_top_cited": {
        "query": "cites:(6680916 OR 6680917)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMiZzPTEwMzY3NDQ5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%286680916+OR+6680917%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(6680916 OR 6680917)",
        "reviewed": 54,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 54,
        "triage_read": 0,
        "triage_snippet_classified": 54
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(6680916 OR 6680917)",
    "indexed_citing_opinions": 155,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 6680916,
        "count": 155,
        "count_source": "search"
      },
      {
        "opinion_id": 6680917,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1604,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/berghuis-v-thompkins.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5NDczODImcz0xMDA0NjM1OSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%286680916+OR+6680917%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T19:47:41Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:48:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:48:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:55:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:48:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Berghuis v. Thompkins

```
<opinion type="majority">
<p id="b1194-5">OPINION OF THE COURT</p>
<p id="b1194-6">[<span class="citation no-link">560 U.S. 373</span>]</p>
<author id="b1194-7">Justice Kennedy</author>
<p id="azto-dedup-0">delivered the opinion of the Court.</p>
<p id="b1194-8">The United States Court of Appeals for the Sixth Circuit, in a habeas corpus proceeding challenging a Michigan conviction for first-degree murder and certain other offenses, ruled that there had been two separate constitutional errors in the trial that led to the jury’s guilty verdict. First, the Court</p>
<p id="b1194-9">[<span class="citation no-link">560 U.S. 374</span>]</p>
<p id="b1194-10">of Appeals determined that a statement by the accused, relied on at trial by the prosecution, had been elicited in violation of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U.S. 436</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (1966). Second, it found that failure to ask for an instruction relating to testimony from an accomplice was ineffective assistance by defense counsel. See <em>Strickland </em>v. <em>Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U.S. 668</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span> (1984). Both of these contentions had been rejected in Michigan courts and in the habeas corpus proceedings before the United States District Court. Certiorari was granted to review the decision by the Court of Appeals on both points. The warden of a Michigan correctional facility is the petitioner here, and Van Chester Thompkins, who was convicted, is the respondent.</p>
<p id="b1194-11">I</p>
<p id="b1194-12">A</p>
<p id="b1194-13">On January 10, 2000, a shooting occurred outside a mall in Southfield, Michigan. Among the victims was Samuel Morris, who died from multiple gunshot wounds. The other victim, Frederick France, recovered from his injuries and later testified. Thompkins, who was a suspect, fled. About one year later he was found in Ohio and arrested there.</p>
<p id="b1194-18">Two Southfield police officers traveled to Ohio to interrogate Thomp-kins, then awaiting transfer to Michigan. The interrogation began around 1:30 p.m. and lasted about three hours. The interrogation was conducted in a room that was 8 by 10 feet, and Thompkins sat in a chair that resembled a school desk (it had an arm on it that swings around to provide a surface to write on). App. 144a-145a. At the beginning of the interrogation, one of the officers, Detective Helgert, presented Thompkins with a form derived from the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule. It stated:</p>
<blockquote id="b1194-19">“NOTIFICATION OF CONSTITUTIONAL RIGHTS AND STATEMENT</blockquote>
<blockquote id="b1194-20">“1. You have the right to remain silent.</blockquote>
<blockquote id="b1194-21">[<span class="citation no-link">560 U.S. 375</span>]</blockquote>
<blockquote id="b1194-22">“2. Anything you say can and will be used against you in a court of law.</blockquote>
<blockquote id="b1194-23">“3. You have a right to talk to a lawyer before answering any questions and you have the right to have a lawyer present with you while you are answering any questions.</blockquote>
<blockquote id="b1194-24">“4. If you cannot afford to hire a lawyer, one will be appointed to represent you before any questioning, if you wish one.</blockquote>
<blockquote id="b1195-3"><page-number citation-index="1" label="1107">*1107</page-number>“5. You have the right to decide at any time before or during questioning to use your right to remain silent and your right to talk with a lawyer while you are being questioned.” Brief for Petitioner 60 (some capitalization omitted).</blockquote>
<p id="b1195-4">Helgert asked Thompkins to read the fifth warning out loud. App. 8a. Thompkins complied. Helgert later said this was to ensure that Thomp-kins could read, and Helgert concluded that Thompkins understood English. <em><span class="citation no-link">Id.,</span> </em>at 9a. Helgert then read the other four <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings out loud and asked Thompkins to sign the form to demonstrate that he understood his rights. App. 8a-9a. Thomp-kins declined to sign the form. The record contains conflicting evidence about whether Thompkins then verbally confirmed that he understood the rights listed on the form. Compare <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span> </em>at 9a (at a suppression hearing, Helgert testified that Thompkins verbally confirmed that he understood his rights), with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">id.,</a></span> </em>at 148a (at trial, Helgert stated, “I don’t know that I orally asked him” whether Thomp-kins understood his rights).</p>
<p id="b1195-5">Officers began an interrogation. At no point during the interrogation did Thompkins say that he wanted to remain silent, that he did not want to talk with the police, or that he wanted an attorney. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 10a. Thompkins was “[¿largely” silent during the interrogation, which lasted about three hours. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at 19a. He did give a few limited verbal responses, however, such as “yeah,” “no,” or “I don’t know.” And on occasion he communicated by nodding his</p>
<p id="b1195-6">[<span class="citation no-link">560 U.S. 376</span>]</p>
<p id="b1195-7">head. <em><span class="citation no-link">Id.,</span> </em>at 23a. Thomp-kins also said that he “didn’t want a peppermint” that was offered to him by the police and that the chair he was “sitting in was hard <em>.’’Id., </em>at 152a.</p>
<p id="b1195-8">About 2 hours and 45 minutes into the interrogation, Helgert asked Thompkins, “Do you believe in God?” <em><span class="citation no-link">Id.,</span> </em>at 11a, 153a. Thompkins made eye contact with Helgert and said “Yes,” as his eyes “well[ed] up with tears.” <em><span class="citation no-link">Id.,</span> </em>at 11a. Helgert asked, “Do you pray to God?” Thompkins said <em>“Yes.’’Id., </em>at 11a, 153a. Helgert asked, “Do you pray to God to forgive you for shooting that boy down?” <em><span class="citation no-link">Id.,</span> </em>at 153a. Thompkins answered “Yes” and looked away. <em><span class="citation no-link">Ibid.</span> </em>Thompkins refused to make a written confession, and the interrogation ended about 15 minutes later. <em><span class="citation no-link">Id.,</span> </em>at 11a.</p>
<p id="b1195-9">Thompkins was charged with first-degree murder, assault with intent to commit murder, and certain firearms-related offenses. He moved to suppress the statements made during the interrogation. He argued that he had invoked his Fifth Amendment right to remain silent, requiring police to end the interrogation at once, see <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#103" aria-description="Citation for case: Michigan v. Mosley">423 U.S. 96, 103</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S. Ct. 321</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">46 L. Ed. 2d 313</a></span> (1975) (citing <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 474</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>), that he had not waived his right to remain silent, and that his inculpatory statements were involuntary. The trial court denied the motion.</p>
<p id="b1195-10">At trial, the prosecution’s theory was that Thompkins shot the victims from the passenger seat of a van driven by Eric Purifoy. Purifoy testified that he had been driving the van and that Thompkins was in the passenger seat while another man, one Myzell Woodward, was in the back. The defense strategy was to pin the blame on Purifoy. Purifoy testified he did not see who fired the weapon because the van was stopped and he was bending over near the floor when shots were fired. Purifoy explained that, just after the shooting, Thomp-kins, holding a pistol, told Purifoy, <page-number citation-index="1" label="1108">*1108</page-number>“What the hell you doing? Pull off.” Purifoy then drove away from the scene. App. 170a.</p>
<p id="b1196-4">[<span class="citation no-link">560 U.S. 377</span>]</p>
<p id="b1196-5">So that the Thompkins jury could assess Purifoy’s credibility and knowledge, the prosecution elicited testimony from Purifoy that he had been tried earlier for the shooting under an aiding-and-abetting theory. Purifoy and Detective Helgert testified that a jury acquitted him of the murder and assault charges, convicted him of carrying a concealed weapon in a motor vehicle, and hung on two other firearms offenses to which he later pleaded guilty. At Purifoy’s trial, the prosecution had argued that Purifoy was the driver and Thomp-kins was the shooter. This was consistent with the prosecution’s argument at Thompkins’ trial.</p>
<p id="b1196-6">After Purifoy’s trial had ended—but before Thompkins’ trial began—Puri-foy sent Thompkins some letters. The letters expressed Purifoy’s disappointment that Thompkins’ family thought Purifoy was a “snitch” and a “rat.” <em><span class="citation no-link">Id.,</span> </em>at 179a-180a. In one letter Purifoy offered to send a copy of his trial transcript to Thompkins as proof that Purifoy did not place the blame on Thompkins for the shooting. <span class="citation no-link">Id.,</span> at 180a. The letters also contained statements by Purifoy that claimed they were both innocent. <em><span class="citation no-link">Id.,</span> </em>at 178a-179a. At Thompkins’ trial, the prosecution suggested that one of Puri-foy’s letters appeared to give Thompkins a trial strategy. It was, the prosecution suggested, that Woodward shot the victims, allowing Puri-foy and Thompkins to say they dropped to the floor when the shooting started. <em>Id.., </em>at 187a-189a.</p>
<p id="b1196-7">During closing arguments, the prosecution suggested that Purifoy lied when he testified that he did not see Thompkins shoot the victims:</p>
<blockquote id="b1196-8">“Did Eric Purifoy’s Jury make the right decision? I’m not here to judge that. You are not bound by what his Jury found. Take his testimony for what it was, [a] twisted attempt to help not just an acquaintance but his tight buddy.” <em><span class="citation no-link">Id.,</span> </em>at 202a.</blockquote>
<p id="b1196-9">[<span class="citation no-link">560 U.S. 378</span>]</p>
<p id="b1196-10">Defense counsel did not object. Defense counsel also did not ask for an instruction informing the jury that it could consider evidence of the outcome of Purifoy’s trial only to assess Purifoy’s credibility, not to establish Thompkins’ guilt.</p>
<p id="b1196-11">The jury found Thompkins guilty on all counts. He was sentenced to life in prison without parole.</p>
<p id="b1196-12">B</p>
<p id="b1196-13">The trial court denied a motion for new trial filed by Thompkins’ appellate counsel. The trial court rejected the claim of ineffective assistance of trial counsel for failure to ask for a limiting instruction regarding the outcome of Purifoy’s trial, reasoning that this did not prejudice Thomp-kins. <em>Id.., </em>at 236a.</p>
<p id="b1196-14">Thompkins appealed this ruling, along with the trial court’s refusal to suppress his pretrial statements under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The Michigan Court of Appeals rejected the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>claim, ruling that Thompkins had not invoked his right to remain silent and had waived it. It also rejected the ineffective-assistance-of-counsel claim, finding that Thompkins failed to show that evidence of Purifoy’s conviction for firearms offenses resulted in prejudice. <em>People </em>v. <em>Thompkins, </em>No. 242478, (Feb. 3, 2004), App. to Pet. for Cert. 74a-82a. The Michigan Supreme Court denied discretionary review. <span class="citation multiple-matches"><a href="/c/Mich./471/866/">471 Mich. 866</a></span>, <span class="citation multiple-matches"><a href="/c/N.W.2d/683/676/">683 N.W.2d 676</a></span> (2004) (table).</p>
<p id="b1196-15">Thompkins filed a petition for a writ of habeas corpus in the United <page-number citation-index="1" label="1109">*1109</page-number>States District Court for the Eastern District of Michigan. The District Court rejected Thompkins’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and ineffective-assistance claims. App. to Pet. for Cert. 39a-72a. It noted that, [1] under the Antiterrorism and Effective Death Penalty Act of 1996 (AEDPA), a federal court cannot grant a petition for a writ of habeas corpus unless the state court’s adjudication of the merits was “contrary to, or involved an unreasonable application of, clearly established Federal law.” <span class="citation no-link">28 U.S.C. § 2254</span>(d)(1). The District Court reasoned that Thompkins did not invoke his right to remain silent and was not coerced into making statements</p>
<p id="almu-dedup-1">[<span class="citation no-link">560 U.S. 379</span>]</p>
<p id="b1197-4">during the interrogation. It held further that the Michigan Court of Appeals was not unreasonable in determining that Thompkins had waived his right to remain silent.</p>
<p id="b1197-6">The United States Court of Appeals for the Sixth Circuit reversed, ruling for Thompkins on both his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and ineffective-assistance-of-counsel claims. <span class="citation" data-id="1226412"><a href="/opinion/1226412/thompkins-v-berghuis/" aria-description="Citation for case: Thompkins v. Berghuis">547 F.3d 572</a></span> (2008). The Court of Appeals ruled that the state court, in rejecting Thompkins’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>claim, unreasonably applied clearly established federal law and based its decision on an unreasonable determination of the facts. See <span class="citation no-link">28 U.S.C. § 2254</span>(d). The Court of Appeals acknowledged that a waiver of the right to remain silent need not be express, as it can be “ ‘inferred from the actions and words of the person interrogated.’ ” <span class="citation" data-id="1226412"><a href="/opinion/1226412/thompkins-v-berghuis/" aria-description="Citation for case: Thompkins v. Berghuis">547 F.3d, at 582</a></span> (quoting <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U.S. 369, 373</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span> (1979)). The panel held, nevertheless, that the state court was unreasonable in finding an implied waiver in the circumstances here. The Court of Appeals found that the state court unreasonably determined the facts because “the evidence demonstrates that Thompkins was silent for two hours and forty-five minutes.” <span class="citation" data-id="1226412"><a href="/opinion/1226412/thompkins-v-berghuis/#586" aria-description="Citation for case: Thompkins v. Berghuis">547 F.3d, at 586</a></span>. According to the Court of Appeals, Thompkins’ “persistent silence for nearly three hours in response to questioning and repeated invitations to tell his side of the story offered a clear and unequivocal message to the officers: Thompkins did not wish to waive his rights.” <span class="citation" data-id="1226412"><a href="/opinion/1226412/thompkins-v-berghuis/#588" aria-description="Citation for case: Thompkins v. Berghuis"><em>Id., </em>at 588</a></span>.</p>
<p id="b1197-8">The Court of Appeals next determined that the state court unreasonably applied clearly established federal law by rejecting Thompkins’ ineffective-assistance-of-counsel claim based on counsel’s failure to ask for a limiting instruction regarding Purifoy’s acquittal. The Court of Appeals asserted that because Thomp-kins’ central strategy was to pin the blame on Purifoy, there was a reasonable probability that the result of Thompkins’ trial would have been different if there had been a limiting instruction regarding Purifoy’s acquittal.</p>
<p id="b1197-9">We granted certiorari. <span class="citation no-link">557 U.S. 965</span>, <span class="citation no-link">130 S. Ct. 48</span>, <span class="citation no-link">174 L. Ed. 2d 632</span> (2009).</p>
<p id="b1197-10">[<span class="citation no-link">560 U.S. 380</span>]</p>
<p id="b1197-11">II</p>
<p id="b1197-12">Under AEDPA, a federal court may not grant a habeas corpus application “with respect to any claim that was adjudicated on the merits in State court proceedings,” <span class="citation no-link">28 U.S.C. § 2254</span>(d), unless the state court’s decision “was contrary to, or involved an unreasonable application of, clearly established Federal law, as determined by the Supreme Court of the United States,” § 2254(d)(1), or “was based on an unreasonable determination of the facts in light of the evidence presented in the State court proceeding,” § 2254(d)(2). See <page-number citation-index="1" label="1110">*1110</page-number><em>Knowles </em>v. <em>Mirzayance, </em><span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/#114" aria-description="Citation for case: Knowles v. Mirzayance">556 U.S. 111, 114</a></span>, <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/" aria-description="Citation for case: Knowles v. Mirzayance">129 S. Ct. 1411</a></span>, <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/" aria-description="Citation for case: Knowles v. Mirzayance">173 L. Ed. 2d 251</a></span> (2009). The relevant state-court decision here is the Michigan Court of Appeals’ decision affirming Thomp-kins’ conviction and rejecting his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and ineffective-assistance-of-counsel claims on the merits.</p>
<p id="b1198-4">Ill</p>
<p id="b1198-5">The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court formulated a warning that must be given to suspects before they can be subjected to custodial interrogation. The substance of the warning still must be given to suspects today. A suspect in custody must be advised as follows:</p>
<blockquote id="b1198-6">“He must be warned prior to any questioning that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 479</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>.</blockquote>
<p id="b1198-7">All concede that the warning given in this case was in full compliance with these requirements. The dispute centers on the response—or nonre-sponse—from the suspect.</p>
<p id="b1198-8">A</p>
<p id="b1198-9">Thompkins makes various arguments that his answers to questions from the detectives were inadmissible. He first</p>
<p id="b1198-10">[<span class="citation no-link">560 U.S. 381</span>]</p>
<p id="b1198-11">contends that he “invoke [d] his privilege” to remain silent by not saying anything for a sufficient period of time, so the interrogation should have “cease[d]” before he made his inculpatory statements. <span class="citation no-link"><em>Id., </em>at 474</span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#103" aria-description="Citation for case: Michigan v. Mosley">423 U.S., at 103</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S. Ct. 321</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">46 L. Ed. 2d 313</a></span> (police must “ ‘scrupulously hono[r]’ ” this “critical safeguard” when the accused invokes his or her “ ‘right to cut off questioning’ ” (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 474, 479</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>)).</p>
<p id="b1198-13">This argument is unpersuasive. [4] In the context of invoking the <em>Miranda </em>right to counsel, the Court in <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#459" aria-description="Citation for case: Davis v. United States">512 U.S. 452, 459</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span> (1994), held that a suspect must do so “unambiguously.” If an accused makes a statement concerning the right to counsel “that is ambiguous or equivocal” or makes no statement, the police are not required to end the interrogation, <em>ibid., </em>or ask questions to clarify whether the accused wants to invoke his or her <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#461" aria-description="Citation for case: Davis v. United States">512 U.S., at 461-462</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>.</p>
<p id="b1198-14">The Court has not yet stated whether an invocation of the right to remain silent can be ambiguous or equivocal, but there is no principled reason to adopt different standards for determining when an accused has invoked the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to remain silent and the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel at issue in <em>Davis. See, e.g., Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#648" aria-description="Citation for case: Solem v. Stumes">465 U.S. 638, 648</a></span>, <span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/" aria-description="Citation for case: Solem v. Stumes">104 S. Ct. 1338</a></span>, <span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/" aria-description="Citation for case: Solem v. Stumes">79 L. Ed. 2d 579</a></span> (1984) (“[M]uch of the logic and language of <em>[Mosley],” </em>which discussed the <em>Miranda </em>right to remain silent, “could be applied to the invocation of the <em>[.Miranda </em>right to counsel]”). Both protect the privilege against compulsory self-incrimination, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 467-473</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>, by requiring an interrogation to cease when either right is invoked, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#103" aria-description="Citation for case: Michigan v. Mosley"><em>Mosley, supra, </em>at 103</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S. Ct. 321</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">46 L. Ed. 2d 313</a></span> (citing <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 474</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>); <em>Fare </em>v. <page-number citation-index="1" label="1111">*1111</page-number><em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U.S. 707, 719</a></span>, <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">99 S. Ct. 2560</a></span>, <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">61 L. Ed. 2d 197</a></span> (1979).</p>
<p id="b1199-4">There is good reason to require an accused who wants to invoke his or her right to remain silent to do so unambiguously. A requirement of an unambiguous invocation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights results in an objective inquiry that “avoid [s] difficulties of proof and . . . provide [s] guidance to officers” on how to proceed in the face of ambiguity. <em>Davis, </em>512 U.S.,</p>
<p id="b1199-5">[<span class="citation no-link">560 U.S. 382</span>]</p>
<p id="b1199-6">at 458-459, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>. If an ambiguous act, omission, or statement could require police to end the interrogation, police would be required to make difficult decisions about an accused’s unclear intent and face the consequence of suppression “if they guess wrong.” <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#461" aria-description="Citation for case: Davis v. United States"><em>Id., </em>at 461</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>. Suppression of a voluntary confession in these circumstances would place a significant burden on society’s interest in prosecuting criminal activity. See <em>id,, </em>at 459-461, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>; <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine">475 U.S. 412, 427</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span> (1986). Treating an ambiguous or equivocal act, omission, or statement as an invocation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights “might add marginally to <em>Miranda’s </em>goal of dispelling the compulsion inherent in custodial interrogation.” <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#425" aria-description="Citation for case: Moran v. Burbine">475 U.S., at 425</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>. But “as <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holds, full comprehension of the rights to remain silent and request an attorney are sufficient to dispel whatever coercion is inherent in the interrogation process.” <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine"><em>Id,, </em>at 427, 106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>; see <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#460" aria-description="Citation for case: Davis v. United States"><em>Davis, supra, </em>at 460</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>.</p>
<p id="b1199-8">Thompkins did not say that he wanted to remain silent or that he did not want to talk with the police. Had he made either of these simple, unambiguous statements, he would have invoked his “ ‘right to cut off questioning.’ ” <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#103" aria-description="Citation for case: Michigan v. Mosley"><em>Mosley, supra, </em>at 103</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">96 S. Ct. 321</a></span>, <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">46 L. Ed. 2d 313</a></span> (quoting <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 474</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>). Here he did neither, so he did not invoke his right to remain silent.</p>
<p id="b1199-10">B</p>
<p id="b1199-11">We next consider whether Thomp-kins waived his right to remain silent.  Even absent the accused’s invocation of the right to remain silent, the accused’s statement during a custodial interrogation is inadmissible at trial unless the prosecution can establish that the accused “in fact knowingly and voluntarily waived <em>[Miranda] </em>rights” when making the statement. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U.S., at 373</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. The waiver inquiry “has two distinct dimensions”: waiver must be “voluntary in the sense that it was the product of a free and deliberate choice rather than intimidation, coercion, or deception,” and “made with a full awareness of both the nature of the right</p>
<p id="AfoQ">[<span class="citation no-link">560 U.S. 383</span>]</p>
<p id="b1199-12">being abandoned and the consequences of the decision to abandon it.” <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 421</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>.</p>
<p id="b1199-13">Some language in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>could be read to indicate that waivers are difficult to establish absent an explicit written waiver or a formal, express oral statement. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>said “a valid waiver will not be presumed simply from the silence of the accused after warnings are given or simply from the fact that a confession was in fact eventually obtained.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 475</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>; see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 470</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (“No effective waiver . . . can be recognized unless specifically made after the <em>[Miranda] </em>warnings <page-number citation-index="1" label="1112">*1112</page-number>. . . have been given”). In addition, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>Court stated that “a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 475</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>.</p>
<p id="b1200-4">The course of decisions since <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>informed by the application of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings in the whole course of law enforcement, demonstrates that waivers can be established even absent formal or express statements of waiver that would be expected in, say, a judicial hearing to determine if a guilty plea has been properly entered. Cf. Fed. Rule Crim. Proc. 11. The main purpose of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is to ensure that an accused is advised of and understands the right to remain silent and the right to counsel. See <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#460" aria-description="Citation for case: Davis v. United States"><em>Davis, supra, </em>at 460</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>; <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 427</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>. Thus, “[i]f anything, our subsequent cases have reduced the impact of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule on legitimate law enforcement while reaffirming the decision’s core ruling that unwarned statements may not be used as evidence in the prosecution’s case in chief.” <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U.S. 428, 443-444</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">120 S. Ct. 2326</a></span>, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">147 L. Ed. 2d 405</a></span> (2000).</p>
<p id="b1200-5">One of the first cases to decide the meaning and import of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>with respect to the question of waiver was <em>North Carolina </em>v. <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span>. </em>The <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>Court, after discussing some of the problems created by the language in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>established certain important propositions. <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>interpreted the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>language concerning the “heavy burden”</p>
<p id="b1200-6">[<span class="citation no-link">560 U.S. 384</span>]</p>
<p id="b1200-7">to show waiver, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 475</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>, in accord with usual principles of determining waiver, which can include waiver implied from all the circumstances. See <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 373, 376</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. And in a later case, the Court stated that [7] this “heavy burden” is not more than the burden to establish waiver by a preponderance of the evidence. <em>Colorado </em>v. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#168" aria-description="Citation for case: Colorado v. Connelly">479 U.S. 157, 168</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span> (1986).</p>
<p id="b1200-9">The prosecution therefore does not need to show that a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights was express. An “implicit waiver” of the “right to remain silent” is sufficient to admit a suspect’s statement into evidence. <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#376" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 376</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>made clear that a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights may be implied through “the defendant’s silence, coupled with an understanding of his rights and a course of conduct indicating waiver.” <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U.S., at 373</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. The Court in <em>Butler </em>therefore “retreated” from the “language and tenor of the <em>Miranda </em>opinion,” which “suggested that the Court would require that a waiver ... be ‘specifically made.’ ” <em>Connecticut </em>v. <em>Barrett, </em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#531" aria-description="Citation for case: Connecticut v. Barrett">479 U.S. 523, 531-532</a></span>, <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">107 S. Ct. 828</a></span>, <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">93 L. Ed. 2d 920</a></span> (1987) (Brennan, J., concurring in judgment).</p>
<p id="b1200-10">If the State establishes that a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was given and the accused made an uncoerced statement, this showing, standing alone, is insufficient to demonstrate “a valid waiver” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 475</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. The prosecution must make the additional showing that the accused understood these rights. See <em>Colorado </em>v. <em>Spring, </em><span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/#573" aria-description="Citation for case: Colorado v. Spring">479 U.S. 564, 573-575</a></span>, <span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/" aria-description="Citation for case: Colorado v. Spring">107 S. Ct. 851</a></span>, <span class="citation" data-id="9430793"><a href="/opinion/111798/colorado-v-spring/" aria-description="Citation for case: Colorado v. Spring">93 L. Ed. 2d 954</a></span> (1987); <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#530" aria-description="Citation for case: Connecticut v. Barrett"><em>Barrett, supra, </em>at 530</a></span>, <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">107 <page-number citation-index="1" label="1113">*1113</page-number>S. Ct. 828</a></span>, <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/" aria-description="Citation for case: Connecticut v. Barrett">93 L. Ed. 2d 920</a></span>; <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U.S., at 421-422</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>. Cf. <em>Tague </em>v. <em>Louisiana, </em><span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/#469" aria-description="Citation for case: Tague v. Louisiana">444 U.S. 469, 469, 471</a></span>, <span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">100 S. Ct. 652</a></span>, <span class="citation" data-id="110179"><a href="/opinion/110179/tague-v-louisiana/" aria-description="Citation for case: Tague v. Louisiana">62 L. Ed. 2d 622</a></span> (1980) <em>(per curiam) </em>(no evidence that accused understood his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights); <em>Carnley </em>v. <em>Cochran, </em><span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#516" aria-description="Citation for case: Carnley v. Cochran">369 U.S. 506, 516</a></span>, <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">82 S. Ct. 884</a></span>, <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">8 L. Ed. 2d 70</a></span> (1962) (government could not show that accused “understandingly” waived his right to counsel in light of “silent record”). Where the prosecution shows that a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning was given and that it was understood by the accused, an accused’s uncoerced statement establishes an implied waiver of the right to remain silent.</p>
<p id="b1201-4">[<span class="citation no-link">560 U.S. 385</span>]</p>
<p id="b1201-5">Although <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>imposes on the police a rule that is both formalistic and practical when it prevents them from interrogating suspects without first providing them with a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, see <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine">475 U.S., at 427</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>, it does not impose a formalistic waiver procedure that a suspect must follow to relinquish those rights. As a general proposition, the law can presume that an individual who, with a full understanding of his or her rights, acts in a manner inconsistent with their exercise has made a deliberate choice to relinquish the protection those rights afford. See, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler"><em>e.g., Butler, supra, </em>at 372-376</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>; <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#169" aria-description="Citation for case: Colorado v. Connelly"><em>Connelly, supra, </em>at 169-170</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span> (“There is obviously no reason to require more in the way of a ‘volun-tariness’ inquiry in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver context than in the [due process] confession context”). The Court’s cases have recognized that a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights need only meet the standard of <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U.S. 458, 464</a></span>, <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">58 S. Ct. 1019</a></span>, <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">82 L. Ed. 1461</a></span> (1938). See <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 374-375</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>; <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 475-476</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span> (applying <em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span> </em>standard of intentional relinquishment of a known right). As <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>recognized, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#375" aria-description="Citation for case: North Carolina v. Butler">441 U.S., at 375-376</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights can therefore be waived through means less formal than a typical waiver on the record in a courtroom, cf. Fed. Rule Crim. Proc. 11, given the practical constraints and necessities of interrogation and the fact that <em>Miranda’s </em>main protection lies in advising defendants of their rights, see <em>Davis, </em><span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#460" aria-description="Citation for case: Davis v. United States">512 U.S., at 460</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>; <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine">475 U.S., at 427</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>.</p>
<p id="b1201-7">The record in this case shows that Thompkins waived his right to remain silent. There is no basis in this case to conclude that he did not understand his rights; and on these facts it follows that he chose not to invoke or rely on those rights when he did speak. First, there is no contention that Thompkins did not understand his rights; and from this it follows that he knew what he gave up when he spoke. See <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine"><em>id., </em>at 421</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>. There was more than enough evidence in the record to conclude that Thompkins understood his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Thompkins received a written copy of <em>the Miranda </em>warnings; Detective Hel-gert determined that Thompkins</p>
<p id="AzUqO">[<span class="citation no-link">560 U.S. 386</span>]</p>
<p id="b1201-8">could read and understand English; and Thompkins was given time to read the warnings. Thompkins, furthermore, read aloud the fifth warning, which stated that “you have the right to decide at any time before or during questioning to use your right to remain silent and your right to talk with a lawyer while you are being questioned.” Brief for Petitioner 60 <page-number citation-index="1" label="1114">*1114</page-number>(capitalization omitted). He was thus aware that his right to remain silent would not dissipate after a certain amount of time and that police would have to honor his right to be silent and his right to counsel during the whole course of interrogation. Those rights, the warning made clear, could be asserted at any time. Helgert, moreover, read the warnings aloud.</p>
<p id="b1202-4">Second, Thompkins’ answer to Detective Helgert’s question about whether Thompkins prayed to God for forgiveness for shooting the victim is a “course of conduct indicating waiver” of the right to remain silent. <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, </em>supra, at 373</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. If Thompkins wanted to remain silent, he could have said nothing in response to Hel-gert’s questions, or he could have unambiguously invoked his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and ended the interrogation. The fact that Thompkins made a statement about three hours after receiving a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning does not overcome the fact that he engaged in a course of conduct indicating waiver. [11] Police are not required to rewarn suspects from time to time. Thomp-kins’ answer to Helgert’s question about praying to God for forgiveness for shooting the victim was sufficient to show a course of conduct indicating waiver. This is confirmed by the fact that before then Thompkins had given sporadic answers to questions throughout the interrogation.</p>
<p id="b1202-5">Third, there is no evidence that Thompkins’ statement was coerced. See <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 421</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">106 S. Ct. 1135</a></span>, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">89 L. Ed. 2d 410</a></span>. Thompkins does not claim that police threatened or injured him during the interrogation or that he was in any way fearful. The interrogation was conducted in a standard-sized room in the middle of the afternoon. It is true that apparently he was in a</p>
<p id="b1202-8">[<span class="citation no-link">560 U.S. 387</span>]</p>
<p id="b1202-9">straight-backed chair for three hours, but there is no authority for the proposition that an interrogation of this length is inherently coercive. Indeed, even where interrogations of greater duration were held to be improper, they were accompanied, as this one was not, by other facts indicating coercion, such as an incapacitated and sedated suspect, sleep and food deprivation, and threats. Cf. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#163" aria-description="Citation for case: Colorado v. Connelly">479 U.S., at 163-164, n. 1</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span>. The fact that Helgert’s question referred to Thompkins’ religious beliefs also did not render Thompkins’ statement involuntary. [12] “[T]he Fifth Amendment privilege is not concerned ‘with moral and psychological pressures to confess emanating from sources other than official coercion.’ ” <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#170" aria-description="Citation for case: Colorado v. Connelly"><em>Id., </em>at 170</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span> (quoting <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#305" aria-description="Citation for case: Oregon v. Elstad">470 U.S. 298, 305</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">105 S. Ct. 1285</a></span>, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">84 L. Ed. 2d 222</a></span> (1985)). In these circumstances, Thompkins knowingly and voluntarily made a statement to police, so he waived his right to remain silent.</p>
<p id="b1202-10">C</p>
<p id="b1202-11">Thompkins next argues that, even if his answer to Detective Helgert could constitute a waiver of his right to remain silent, the police were not allowed to question him until they obtained a waiver first. <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>forecloses this argument. The <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>Court held that courts can infer a waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights “from the actions and words of the person interrogated.” <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U.S., at 373</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span>. This principle would be inconsistent with a rule that requires a waiver at the outset. The <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>Court thus rejected the rule proposed by the <em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler</a></span> </em>dissent, which would have “required] the police to obtain an express waiver of <em>[.Miranda </em><page-number citation-index="1" label="1115">*1115</page-number>rights] before proceeding with interrogation.” <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#379" aria-description="Citation for case: North Carolina v. Butler"><em>Id., </em>at 379</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">99 S. Ct. 1755</a></span>, <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">60 L. Ed. 2d 286</a></span> (Brennan, J., dissenting). This holding also makes sense given that  “the primary protection afforded suspects subject[ed] to custodial interrogation is the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings themselves.” <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/#460" aria-description="Citation for case: Davis v. United States"><em>Davis, supra, </em>at 460</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">114 S. Ct. 2350</a></span>, <span class="citation" data-id="9433017"><a href="/opinion/117863/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">129 L. Ed. 2d 362</a></span>. The <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rule and its requirements are met if a suspect receives adequate <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, understands them, and has an opportunity to invoke the rights before giving any answers or admissions. Any waiver, express or implied,</p>
<p id="b1203-4">[<span class="citation no-link">560 U.S. 388</span>]</p>
<p id="b1203-5">may be contradicted by an invocation at any time. If the right to counsel or the right to remain silent is invoked at any point during questioning, further interrogation must cease.</p>
<p id="b1203-7">Interrogation provides the suspect with additional information that can put his or her decision to waive, or not to invoke, into perspective. As questioning commences and then continues, the suspect has the opportunity to consider the choices he or she faces and to make a more informed decision, either to insist on silence or to cooperate. When the suspect knows that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights can be invoked at any time, he or she has the opportunity to reassess his or her immediate and long-term interests. Cooperation with the police may result in more favorable treatment for the suspect; the apprehension of accomplices; the prevention of continuing injury and fear; beginning steps toward relief or solace for the victims; and the beginning of the suspect’s own return to the law and the social order it seeks to protect.</p>
<p id="b1203-8">In order for an accused’s statement to be admissible at trial, police must have given the accused a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning. See <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#471" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 471</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. If that condition is established, the court can proceed to consider whether there has been an express or implied waiver of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 476</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">86 S. Ct. 1602</a></span>, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">16 L. Ed. 2d 694</a></span>. In making its ruling on the admissibility of a statement made during custodial questioning, the trial court, of course, considers whether there is evidence to support the conclusion that, from the whole course of questioning, an express or implied waiver has been established. Thus, after giving a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning, police may interrogate a suspect who has neither invoked nor waived his or her <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. On these premises, it follows the police were not required to obtain a waiver of Thompkins’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights before commencing the interrogation.</p>
<p id="b1203-10">D</p>
<p id="b1203-11">In sum,  a suspect who has received and understood the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, and has not invoked his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights,</p>
<p id="b1203-12">[<span class="citation no-link">560 U.S. 389</span>]</p>
<p id="b1203-13">waives the right to remain silent by making an uncoerced statement to the police. Thompkins did not invoke his right to remain silent and stop the questioning. Understanding his rights in full, he waived his right to remain silent by making a voluntary statement to the police. The police, moreover, were not required to obtain a waiver of Thomp-kins’ right to remain silent before interrogating him. The state court’s decision rejecting Thompkins’ <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>claim was thus correct under <em>de novo </em>review and therefore necessarily reasonable under the more deferential AEDPA standard of review, <span class="citation no-link">28 U.S.C. § 2254</span>(d). See <em>Knowles, </em><span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/#123" aria-description="Citation for case: Knowles v. Mirzayance">556 U.S., at 123-124</a></span>, <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/" aria-description="Citation for case: Knowles v. Mirzayance">129 S. Ct. 1411</a></span>, <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/" aria-description="Citation for case: Knowles v. Mirzayance">173 L. Ed. 2d 251</a></span> (state court’s <page-number citation-index="1" label="1116">*1116</page-number>decision was correct under <em>de novo </em>review and not unreasonable under AEDPA).</p>
<p id="b1204-4">IV</p>
<p id="b1204-5">The second issue in this case is whether Thompkins’ counsel provided ineffective assistance by failing to request a limiting instruction regarding how the jury could consider the outcome of Purifoy’s trial.  To establish ineffective assistance of counsel, a defendant “must show both deficient performance bu counsel and prejudice.” <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/#122" aria-description="Citation for case: Knowles v. Mirzayance"><em>Id.., </em>at 122, 129 S. Ct. 1411</a></span>, <span class="citation" data-id="145897"><a href="/opinion/145897/knowles-v-mirzayance/" aria-description="Citation for case: Knowles v. Mirzayance">173 L. Ed. 2d 251</a></span> (citing <em>Strickland, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#687" aria-description="Citation for case: Strickland v. Washington">466 U.S., at 687</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span>). To establish prejudice, a “defendant must show that there is a reasonable probability that, but for counsel’s unprofessional errors, the result of the proceeding would have been different.” <em>Strickland, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#694" aria-description="Citation for case: Strickland v. Washington">466 U.S., at 694</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span>. In assessing prejudice, courts “must consider the totality of the evidence before the judge or jury.” <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#695" aria-description="Citation for case: Strickland v. Washington"><em>Id., </em>at 695</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S. Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L. Ed. 2d 674</a></span>. The Court of Appeals, however, neglected to take into account the other evidence presented against Thomp-kins.</p>
<p id="b1204-6">The Court of Appeals determined that the state court was unreasonable, <span class="citation no-link">28 U.S.C. § 2254</span>(d), when it found that Thompkins suffered no prejudice from failure of defense counsel to request an instruction regarding Purifoy’s earlier acquittal of the murder and assault charges. The state court had rejected Thompkins’ claim that he was prejudiced by evidence of Purifoy’s earlier conviction for firearms offenses, noting that “the record does not disclose an attempt to argue</p>
<p id="b1204-7">[<span class="citation no-link">560 U.S. 390</span>]</p>
<p id="b1204-8">that conviction for an improper purpose.” App. to Pet. for Cert. 80a. It is unclear what prejudice standard the state court applied. The Court of Appeals ruled that the state court used the incorrect standard for assessing prejudice under <em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">Strickland</a></span> </em>because “[questions of the prosecution’s purpose or intent are completely irrelevant in . . . analyzing whether an error resulted in prejudice, which by definition concerns the error’s effect upon the outcome.” <span class="citation" data-id="1226412"><a href="/opinion/1226412/thompkins-v-berghuis/#591" aria-description="Citation for case: Thompkins v. Berghuis">547 F.3d, at 591-592</a></span> (emphasis deleted).</p>
<p id="b1204-10">Even if the state court used an incorrect legal standard, we need not determine whether AEDPA’s deferential standard of review, <span class="citation no-link">28 U.S.C. § 2254</span>(d), applies in this situation. Cf. <em>Williams </em>v. <em>Taylor, </em><span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#397" aria-description="Citation for case: Williams v. Taylor">529 U.S. 362, 397-398</a></span>, <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">120 S. Ct. 1495</a></span>, <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">146 L. Ed. 2d 389</a></span> (2000). That is because, even if AE-DPA deference does not apply, Thomp-kins cannot show prejudice under <em>de novo </em>review, the more favorable standard of review for Thompkins. [16] Courts cannot grant writs of habeas corpus under § 2254 by engaging only in <em>de novo </em>review when it is unclear whether AEDPA deference applies, § 2254(d). In those situations, courts must resolve whether AEDPA deference applies, because if it does, a habeas petitioner may not be entitled to a writ of habeas corpus under § 2254(d). Courts can, however, deny writs of habeas corpus under § 2254 by engaging in <em>de novo </em>review when it is unclear whether AEDPA deference applies, because a habeas petitioner will not be entitled to a writ of habeas corpus if his or her claim is rejected on <em>de novo </em>review, see § 2254(a).</p>
<p id="b1204-11">It seems doubtful that failure to request the instruction about the earlier acquittal or conviction was deficient representation; but on the assumption that it was, on this record Thompkins cannot show prejudice. The record establishes that it was not reasonably likely that the instruction would have made any difference in <page-number citation-index="1" label="1117">*1117</page-number>light of all the other evidence of guilt. The surviving victim, Frederick France, identified Thompkins as the shooter, and the identification was supported by a photograph taken from a surveillance camera.</p>
<p id="b1205-4">[<span class="citation no-link">560 U.S. 391</span>]</p>
<p id="b1205-5">Thomp-kins’ friend Omar Stephens testified that Thompkins confessed to him during a phone conversation, and the details of that confession were corroborated by evidence that Thomp-kins stripped the van and abandoned it after the shooting. The jury, moreover, was capable of assessing Puri-foy’s credibility, as it was instructed to do. The jury in Thompkins’ case could have concluded that the earlier jury in Purifoy’s case made a mistake, or alternatively, that Purifoy was not in fact guilty of the crime for which he had been charged. There was ample evidence in the record to support Thompkins’ guilt under either theory, and his jury was instructed to weigh ah of the evidence in determining whether there was guilt beyond a reasonable doubt. Under our <em>de novo </em>review of this record, Thompkins cannot show prejudice.</p>
<p id="pA5OPS">
<img class="p" height="55" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAVcAAAA3AQAAAACQyTRbAAAAoUlEQVR4nO2UMQrCQBBF3w6pJQcS9GZ6GA9h4WVMkTp2grLfIkXG4kNAUgg73fv7Z/gMwxaxthSrrdC8zfuT9+suPQRAPSfFw1Z5kaT9Q0tZqAFoyL0WCKBM0yJ4mPNex6R4QJKehxTRQg2A7piaPQTAmBUPAXDpkuIBSdrdU0QL8377PvVamOfeXmmUhYokvU/p2ULd6s5K+6ubt3n/3vsBAgnxWg7eVv0AAAAASUVORK5CYII=" width="344"/>
</p>
<p id="b1205-7">The judgment of the Court of Appeals is reversed, and the case is remanded with instructions to deny the petition.</p>
<p id="b1205-8">It is so ordered.</p>
</opinion>
```

---

## GROUP: content/cases/Berkemer v. McCarty.md  (`case`, 5 assertions)

### content_page

```
---
title: "Berkemer v. McCarty"
type: case
citation: "468 U.S. 420 (1984)"
parallel_cite: "104 S. Ct. 3138; 82 L. Ed. 2d 317; 52 U.S.L.W. 5023"
neutral_cite: 1984 U.S. LEXIS 140
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-02
docket: 83-710
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Berkemer v. McCarty
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111249/berkemer-v-mccarty/"
  cluster_id: 111249
  opinion_id: 9429728
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Anchor"
related: ["[[Miranda v. Arizona]]", "[[Howes v. Fields]]", "[[J.D.B. v. North Carolina]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "traffic-stop", "interrogation"]
holding: "(1) Miranda applies to ALL custodial interrogation regardless of the offense's severity — misdemeanors included; (2) the temporary,…"
lake:
  record_id: Berkemer v. McCarty
  status: under_review
  projected_at: 2026-07-06
---

# Berkemer v. McCarty

*468 U.S. 420 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An Ohio state trooper stopped McCarty for weaving on the highway, had him perform a field sobriety test (which he failed), and asked whether he had been using intoxicants — McCarty admitted to beer and marijuana. He was then formally arrested for a misdemeanor DUI, taken to jail, and made further incriminating statements. He received no [[Miranda and Custodial Interrogation|Miranda warnings]] at any point, and moved to suppress both the roadside statements and the jailhouse statements.

## Issue
(1) Whether Miranda's safeguards apply to custodial interrogation for a misdemeanor offense; and (2) whether roadside questioning of a motorist detained during an ordinary traffic stop is "custodial interrogation" requiring [[Miranda and Custodial Interrogation|Miranda warnings]].

## Rule
Miranda applies to custodial interrogation no matter how minor the offense: "We hold therefore that a person subjected to custodial interrogation is entitled to the benefit of the procedural safeguards enunciated in *Miranda*, regardless of the nature or severity of the offense of which he is suspected or for which he was arrested." — 468 U.S. at 434. ^pin-434

But an ordinary traffic stop is not Miranda custody: "The similarly noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not 'in custody' for the purposes of *Miranda*." — *Id.* at 440. ^pin-440

## Application
On these facts McCarty's jailhouse statements should have been suppressed: he was indisputably "in custody" once formally arrested and placed in the police car, yet was never warned, and the misdemeanor character of the DUI offense did not exempt that custodial interrogation from Miranda. His pre-arrest roadside statements, however, were admissible: the ordinary traffic stop was a brief, comparatively nonthreatening *[[Terry v. Ohio|Terry]]*-like detention rather than custody, so no warnings were required before the roadside questions.

## Conclusion
Miranda governs custodial interrogation regardless of offense severity, so the post-arrest jailhouse statements were inadmissible; but the roadside detention was not custody, so the pre-arrest statements were admissible. The judgment was resolved accordingly on these two grounds.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Berkemer* fixes two Miranda-custody rules: warnings are required for custodial interrogation regardless of offense severity, and an ordinary traffic stop is not custody. The custody inquiry was later refined by [[Howes v. Fields]] (imprisonment is not automatically custody) and [[J.D.B. v. North Carolina]] (a juvenile's age is relevant to the custody analysis).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Anchor*

## Sources
- *Berkemer v. McCarty*, 468 U.S. 420 (1984) — https://www.courtlistener.com/opinion/111249/berkemer-v-mccarty/ — pinpoints: 434, 440.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cfb65f831cf2d7c1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "468 U.S. 420 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 140", "official_citation_present": true, "parallel_cite": "104 S. Ct. 3138; 82 L. Ed. 2d 317; 52 U.S.L.W. 5023", "title": "Berkemer v. McCarty", "year": "1984"}}
{"assertion_id": "5c52a049976a149f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "(1) Miranda applies to ALL custodial interrogation regardless of the offense's severity — misdemeanors included; (2) the temporary,…", "title": "Berkemer v. McCarty"}}
{"assertion_id": "90e3a44817b46801", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Anchor", "title": "Berkemer v. McCarty"}}
{"assertion_id": "1492067aab528264", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Berkemer v. McCarty"}}
{"assertion_id": "d999c7d89a0d1f0a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-07-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Berkemer v. McCarty", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Berkemer v. McCarty", "varies_by_point": "false"}}
```

### lake record — Berkemer v. McCarty

```json
{
  "schema_version": "s2.v1",
  "record_id": "Berkemer v. McCarty",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Berkemer v. McCarty",
    "case_name_short": "Berkemer",
    "case_name_full": "BERKEMER, SHERIFF OF FRANKLIN COUNTY, OHIO v. McCARTY",
    "input_case_name": "Berkemer v. McCarty",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-02",
    "year": 1984,
    "docket": "83-710",
    "cluster_id": 111249,
    "lead_opinion_id": 9429728,
    "sibling_ids": [
      111249,
      9429728,
      9429729
    ],
    "absolute_url": "/opinion/111249/berkemer-v-mccarty/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9047277,
        "score": 10,
        "case_name": "Berkemer v. McCarty"
      },
      {
        "cluster_id": 9287487,
        "score": 10,
        "case_name": "Berkemer v. McCarty"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 420",
      "volume": "468",
      "reporter": "U.S.",
      "page": "420",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3138",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 317",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5023",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5023",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 140",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "140",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 420",
        "volume": "468",
        "reporter": "U.S.",
        "page": "420",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3138",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3138",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 317",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "317",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 140",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "140",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5023",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5023",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 420",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 420",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-434",
      "page": null,
      "quote": "requiring Miranda warnings. ## Rule Miranda applies to custodial interrogation no matter how minor the offense:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-440",
      "page": null,
      "quote": "The similarly noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not 'in custody' for the purposes of *Miranda*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Berkemer v. McCarty",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
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
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Chase Robert Griffin",
          "cluster_id": 9438185,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barksdale",
          "cluster_id": 4867083,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Siegert v. Gilley",
          "cluster_id": 112594,
          "cite": [
            "114 L. Ed. 2d 277",
            "111 S. Ct. 1789",
            "500 U.S. 226",
            "1991 U.S. LEXIS 2909",
            "59 U.S.L.W. 4465"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Trustees of State Univ. of NY v. Fox",
          "cluster_id": 112329,
          "cite": [
            "106 L. Ed. 2d 388",
            "109 S. Ct. 3028",
            "492 U.S. 469",
            "1989 U.S. LEXIS 3289",
            "57 U.S.L.W. 5015"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 118309,
          "cite": [
            "144 L. Ed. 2d 370",
            "119 S. Ct. 2090",
            "527 U.S. 373",
            "1999 U.S. LEXIS 4201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Taylor v. Freeland & Kronz",
          "cluster_id": 112725,
          "cite": [
            "118 L. Ed. 2d 280",
            "112 S. Ct. 1644",
            "503 U.S. 638",
            "1992 U.S. LEXIS 2546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yee v. City of Escondido",
          "cluster_id": 112719,
          "cite": [
            "118 L. Ed. 2d 153",
            "112 S. Ct. 1522",
            "503 U.S. 519",
            "1992 U.S. LEXIS 2115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Minjarez",
          "cluster_id": 2623400,
          "cite": [
            "81 P.3d 348",
            "2003 WL 22938909"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
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
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Berkemer v. McCarty:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111249 OR 9429728 OR 9429729) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk0MDgwMDAwMDAwJnM9MTAwMTkyNDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111249+OR+9429728+OR+9429729%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(111249 OR 9429728 OR 9429729)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Mjkmcz0zOTQxMzE2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111249+OR+9429728+OR+9429729%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111249 OR 9429728 OR 9429729)",
        "reviewed": 116,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 116,
        "triage_read": 5,
        "triage_snippet_classified": 111
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111249 OR 9429728 OR 9429729)",
    "indexed_citing_opinions": 3076,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111249,
        "count": 2653,
        "count_source": "search"
      },
      {
        "opinion_id": 9429728,
        "count": 474,
        "count_source": "search"
      },
      {
        "opinion_id": 9429729,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4858,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/berkemer-v-mccarty.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzODE3OTYmcz0xMDU5NzQ3NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111249+OR+9429728+OR+9429729%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111249,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 105591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 109930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111211,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 279036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 282815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 283849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 338963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 421705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 424072,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1146993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1158866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1217972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1220711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1223447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1262034,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1325690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1381407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1430357,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1592530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1725045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1935505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1939088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 1981202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2011645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2086722,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2102837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2380940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111249,
        "cited_id": 2452444,
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
    "date_created": "2026-07-04T19:55:03Z",
    "date_modified": "2026-07-06T07:20:20Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:59:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:55:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Berkemer v. McCarty

```
<opinion type="majority">
<author id="b464-10">Justice Marshall</author>
<p id="AuE">delivered the opinion of the Court.</p>
<p id="AsG">This case presents two related questions: First, does our decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), govern the admissibility of statements made during custodial interrogation by a suspect accused of a misdemeanor traffic <page-number citation-index="1" label="423">*423</page-number>offense? Second, does the roadside questioning of a motorist detained pursuant to a traffic stop constitute custodial interrogation for the purposes of the doctrine enunciated in Miranda?</p>
<p id="b465-5">I</p>
<p id="b465-6">A</p>
<p id="b465-7">The parties have stipulated to the essential facts. See App. to Pet. for Cert. A-l. On the evening of March 31, 1980, Trooper Williams of the Ohio State Highway Patrol observed respondent’s car weaving in and out of a lane on Interstate Highway 270. After following the car for two miles, Williams forced respondent to stop and asked him to get out of the vehicle. When respondent complied, Williams noticed that he was having difficulty standing. At that point, “Williams concluded that [respondent] would be charged with a traffic offense and, therefore, his freedom to leave the scene was terminated.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.,</a></span> </em>at A-2. However, respondent was not told that he would be taken into custody. Williams then asked respondent to perform a field sobriety test, commonly known as a “balancing test.” Respondent could not do so without falling.</p>
<p id="b465-8">While still at the scene of the traffic stop, Williams asked respondent whether he had been using intoxicants. Respondent replied that “he had consumed two beers and had smoked several joints of marijuana a short time before.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Respondent’s speech was slurred, and Williams had difficulty understanding him. Williams thereupon formally placed respondent under arrest and transported him in the patrol car to the Franklin County Jail.</p>
<p id="b465-9">At the jail, respondent was given an intoxilyzer test to determine the concentration of alcohol in his blood.<footnotemark>1</footnotemark> The test did not detect any alcohol whatsoever in respondent’s system. Williams then resumed questioning respondent <page-number citation-index="1" label="424">*424</page-number>in order to obtain information for inclusion in the State Highway Patrol Alcohol Influence Report. Respondent answered affirmatively a question whether he had been drinking. When then asked if he was under the influence of alcohol, he said, “I guess, barely.” <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Williams next asked respondent to indicate on the form whether the marihuana he had smoked had been treated with any chemicals. In the section of the report headed “Remarks,” respondent wrote, “No ang[el] dust or PCP in the pot. Rick McCarty.” App. 2.</p>
<p id="b466-5">At no point in this sequence of events did Williams or anyone else tell respondent that he had a right to remain silent, to consult with an attorney, and to have an attorney appointed for him if he could not afford one.</p>
<p id="b466-6">B</p>
<p id="b466-7">Respondent was charged with operating a motor vehicle while under the influence of alcohol and/or drugs in violation of <span class="citation no-link">Ohio Rev. Code Ann. §4511.19</span> (Supp. 1983). Under Ohio law, that offense is a first-degree misdemeanor and is punishable by fine or imprisonment for up to six months. § 2929.21 (1982). Incarceration for a minimum of three days is mandatory. §4511.99 (Supp. 1983).</p>
<p id="b466-8">Respondent moved to exclude the various incriminating statements he had made to Trooper Williams on the ground that introduction into evidence of those statements would violate the Fifth Amendment insofar as he had not been informed of his constitutional rights prior to his interrogation. When the trial court denied the motion, respondent pleaded “no contest” and was found guilty.<footnotemark>2</footnotemark> He was sentenced to 90 <page-number citation-index="1" label="425">*425</page-number>days in jail, 80 of which were suspended, and was fined $300, $100 of which were suspended.</p>
<p id="b467-5">On appeal to the Franklin County Court of Appeals, respondent renewed his constitutional claim. Relying on a prior decision by the Ohio Supreme Court, which held that the rule announced in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“is not applicable to misdemeanors,” <em>State </em>v. <em>Pyle, </em><span class="citation" data-id="6754230"><a href="/opinion/6864453/state-v-pyle/" aria-description="Citation for case: State v. Pyle">19 Ohio St. 2d 64</a></span>, <span class="citation" data-id="6754230"><a href="/opinion/6864453/state-v-pyle/" aria-description="Citation for case: State v. Pyle">249 N. E. 2d 826</a></span> (1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1007/">396 U. S. 1007</a></span> (1970), the Court of Appeals rejected respondent’s argument and affirmed his conviction. <em>State </em>v. <em>McCarty, </em>No. 80AP-680 (Mar. 10, 1981). The Ohio Supreme Court dismissed respondent’s appeal on the ground that it failed to present a “substantial constitutional question.” <em>State </em>v. <em>McCarty, </em>No. 81-710 (July 1, 1981).</p>
<p id="b467-6">Respondent then filed an action for a writ of habeas corpus in the District Court for the Southern District of Ohio.<footnotemark>3</footnotemark> The District Court dismissed the petition, holding that <em>“Miranda </em>warnings do not have to be given prior to in custody interrogation of a suspect arrested for a traffic offense.” <em>McCarty </em>v. <em>Herdman, </em>No. C-2-81-1118 (Dec. 11, 1981).</p>
<p id="b467-7">A divided panel of the Court of Appeals for the Sixth Circuit reversed, holding that <em>“Miranda </em>warnings must be given to <em>all </em>individuals prior to custodial interrogation, whether the offense investigated be a felony or a misdemeanor traffic offense.” <em>McCarty </em>v. <em>Herdman, </em><span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/#363" aria-description="Citation for case: Richard McCarty v. Captain Herdman">716 F. 2d 361, 363</a></span> (1983) (emphasis in original). In applying this principle to the facts of the case, the Court of Appeals distinguished between the statements made by respondent before and after his formal arrest.<footnotemark>4</footnotemark> The postarrest statements, the court ruled, were <page-number citation-index="1" label="426">*426</page-number>plainly inadmissible; because respondent was not warned of his constitutional rights prior to or “[a]t the point that Trooper Williams took [him] to the police station,” his ensuing admissions could not be used against him. <span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/#364" aria-description="Citation for case: Richard McCarty v. Captain Herdman"><em>Id., </em>at 364</a></span>. The court’s treatment of respondent’s prearrest statements was less clear. It eschewed a holding that “the mere stopping of a motor vehicle triggers <em>Miranda,” ibid., </em>but did not expressly rule that the statements made by respondent at the scene of the traffic stop could be used against him. In the penultimate paragraph of its opinion, the court asserted that “[t]he failure to advise [respondent] of his constitutional rights rendered <em>at least some </em>of his statements inadmissible,” <em>ibid, </em>(emphasis added), suggesting that the court was uncertain as to the status of the prearrest confessions.<footnotemark>5</footnotemark> “Because [respondent] was convicted on inadmissible evidence,” the court deemed it necessary to vacate his conviction and order the District Court to issue a writ of habeas corpus. <em><span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/" aria-description="Citation for case: Richard McCarty v. Captain Herdman">Ibid.</a></span></em><footnotemark><em>6</em></footnotemark><em> </em>However, the Court of Appeals did not specify which statements, if any, could be used against respondent in a retrial.</p>
<p id="b468-5">We granted certiorari to resolve confusion in the federal and state courts regarding the applicability of our ruling in <page-number citation-index="1" label="427">*427</page-number><em>Miranda to </em>interrogations involving minor offenses<footnotemark>7</footnotemark> and to questioning of motorists detained pursuant to traffic stops.<footnotemark>8</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./464/1038/">464 U. S. 1038</a></span> (1984).</p>
<p id="b470-8"><page-number citation-index="1" label="428">*428</page-number>II</p>
<p id="b470-3">The Fifth Amendment provides: “No person . . . shall be compelled in any criminal case to be a witness against himself . . . .” It is settled that this provision governs state as well as federal criminal proceedings. <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964).</p>
<p id="b470-4">In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court addressed the problem of how the privilege against compelled self-incrimination guaranteed by the Fifth Amendment could be protected from the coercive pressures that can be brought to bear upon a suspect in the context of custodial interrogation. The Court held:</p>
<blockquote id="b470-5">“[T]he prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of [a] defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination. By custodial interrogation, we mean questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way. As for the procedural safeguards to be employed, unless other fully effective means are devised to inform accused persons of their right of silence and to assure a continuous opportunity to exercise it, the <page-number citation-index="1" label="429">*429</page-number>following measures are required. Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 444</a></span> (footnote omitted).</blockquote>
<p id="b471-5">In the years since the decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>we have frequently reaffirmed the central principle established by that case: if the police take a suspect into custody and then ask him questions without informing him of the rights enumerated above, his responses cannot be introduced into evidence to establish his guilt.<footnotemark>9</footnotemark> See, <em>e. g., Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#466" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 466-467</a></span> (1981); <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#297" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 297-298</a></span> (1980) (dictum); <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#326" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324, 326-327</a></span> (1969); <em>Mathis </em>v. <em>United States, </em><span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/#3" aria-description="Citation for case: Mathis v. United States">391 U. S. 1, 3-5</a></span> (1968).<footnotemark>10</footnotemark></p>
<p id="b471-6">Petitioner asks us to carve an exception out of the foregoing principle. When the police arrest a person for allegedly committing a misdemeanor traffic offense and then ask him questions without telling him his constitutional rights, petitioner argues, his responses should be admissible against him.<footnotemark>11</footnotemark> We cannot agree.</p>
<p id="b472-4"><page-number citation-index="1" label="430">*430</page-number>One of the principal advantages of the doctrine that suspects must be given warnings before being interrogated while in custody is the clarity of that rule.</p>
<blockquote id="b472-5"><em>“Miranda’s </em>holding has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis.” <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979).</blockquote>
<p id="b472-6">The exception to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>proposed by petitioner would substantially undermine this crucial advantage of the doctrine. The police often are unaware when they arrest a person whether he may have committed a misdemeanor or a felony. Consider, for example, the reasonably common situation in which the driver of a car involved in an accident is taken into custody. Under Ohio law, both driving while under the influence of intoxicants and negligent vehicular homicide are misdemeanors, <span class="citation no-link">Ohio Rev. Code Ann. §§2903.07</span>, 4511.99 (Supp. 1983), while reckless vehicular homicide is a felony, §2903.06 (Supp. 1983). When arresting a person for causing a collision, the police may not know which of these offenses he may have committed. Indeed, the nature of his offense may depend upon circumstances unknowable to the police, such as whether the suspect has previously committed <page-number citation-index="1" label="431">*431</page-number>a similar offense<footnotemark>12</footnotemark> or has a criminal record of some other kind. It may even turn upon events yet to happen, such as whether a victim of the accident dies. It would be unreasonable to expect the police to make guesses as to the nature of the criminal conduct at issue before deciding how they may interrogate the suspect.<footnotemark>13</footnotemark></p>
<p id="b473-5">Equally importantly, the doctrinal complexities that would confront the courts if we accepted petitioner’s proposal would be Byzantine. Difficult questions quickly spring to mind: For instance, investigations into seemingly minor offenses sometimes escalate gradually into investigations into more serious matters;<footnotemark>14</footnotemark> at what point in the evolution of an affair of this sort would the police be obliged to give <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to a suspect in custody? What evidence would be necessary to establish that an arrest for a misdemeanor offense <page-number citation-index="1" label="432">*432</page-number>was merely a pretext to enable the police to interrogate the suspect (in hopes of obtaining information about a felony) without providing him the safeguards prescribed by <em>Mi</em>randa'?<footnotemark>15</footnotemark> The litigation necessary to resolve such matters would be time-consuming and disruptive of law enforcement. And the end result would be an elaborate set of rules, interlaced with exceptions and subtle distinctions, discriminating between different kinds of custodial interrogations.<footnotemark>16</footnotemark> Neither the police nor criminal defendants would benefit from such a development.</p>
<p id="b474-5">Absent a compelling justification we surely would be unwilling so seriously to impair the simplicity and clarity of the holding of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>Neither of the two arguments proffered by petitioner constitutes such a justification. Petitioner first contends that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are unnecessary when a suspect is questioned about a misdemeanor traffic offense, because the police have no reason to subject such a suspect to the sort of interrogation that most troubled the Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>We cannot agree that the dangers of police abuse are so slight in this context. For example, the offense of driving while intoxicated is increasingly regarded in many jurisdictions as a very serious matter.<footnotemark>17</footnotemark> Especially when the intoxicant at issue is a narcotic drug rather than alcohol, the police sometimes have difficulty obtaining evi- ' dence of this crime. Under such circumstances, the incentive for the police to try to induce the defendant to incrimi<page-number citation-index="1" label="433">*433</page-number>nate himself may well be substantial. Similar incentives are likely to be present when a person is arrested for a minor offense but the police suspect that a more serious crime may have been committed. See <em>supra, </em>at 431-432.</p>
<p id="b475-5">We do not suggest that there is any reason to think improper efforts were made in this case to induce respondent to make damaging admissions. More generally, we have no doubt that, in conducting most custodial interrogations of persons arrested for misdemeanor traffic offenses, the police behave responsibly and do not deliberately exert pressures upon the suspect to confess against his will. But the same might be said of custodial interrogations of persons arrested for felonies. The purposes of the safeguards prescribed by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are to <em>ensure </em>that the police do not coerce or trick captive suspects into confessing,<footnotemark>18</footnotemark> to relieve the “‘inherently compelling pressures’” generated by the custodial setting itself, “‘which work to undermine the individual’s will to resist,’ ”<footnotemark>19</footnotemark> and as much as possible to free courts from the task of scrutinizing individual cases to try to determine, after the fact, whether particular confessions were voluntary.<footnotemark>20</footnotemark> Those purposes are implicated as much by in-custody questioning of persons suspected of misdemeanors as they are by questioning of persons suspected of felonies.</p>
<p id="b476-4"><page-number citation-index="1" label="434">*434</page-number>Petitioner’s second argument is that law enforcement would be more expeditious and effective in the absence of a requirement that persons arrested for traffic offenses be informed of their rights. Again, we are unpersuaded. The occasions on which the police arrest and then interrogate someone suspected only of a misdemeanor traffic offense are rare. The police are already well accustomed to giving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to persons taken into custody. Adherence to the principle that <em>all </em>suspects must be given such warnings will not significantly hamper the efforts of the police to investigate crimes.</p>
<p id="b476-5">We hold therefore that a person subjected to custodial interrogation is entitled to the benefit of the procedural safeguards enunciated in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</em><footnotemark><em>21</em></footnotemark><em> </em>regardless of the nature or severity of the offense of which he is suspected or for which he was arrested.</p>
<p id="b476-6">The implication of this holding is that the Court of Appeals was correct in ruling that the statements made by respondent at the County Jail were inadmissible. There can be no question that respondent was “in custody” at least as of the moment he was formally placed under arrest and instructed to get into the police car. Because he was not informed of <page-number citation-index="1" label="435">*435</page-number>his constitutional rights at that juncture, respondent’s subsequent admissions should not have been used against him.</p>
<p id="AJb">h — I &gt; — ! 1 — t</p>
<p id="AXuc">To assess the admissibility of the self-incriminating statements made by respondent prior to his formal arrest, we are obliged to address a second issue concerning the scope of our decision in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>: </em>whether the roadside questioning of a motorist detained pursuant to a routine traffic stop should be considered “custodial interrogation.” Respondent urges that it should,<footnotemark>22</footnotemark> on the ground that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>by its terms applies whenever “a person has been taken into custody <em>or otherwise deprived of his freedom of action in any significant way,” </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span> (emphasis added); see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 467</a></span>.<footnotemark>23</footnotemark> <page-number citation-index="1" label="436">*436</page-number>Petitioner contends that a holding that every detained motorist must be advised of his rights before being questioned would constitute an unwarranted extension of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>doctriné.</p>
<p id="b478-5">It must be acknowledged at the outset that a traffic stop significantly curtails the “freedom of action” of the driver and the passengers, if any, of the detained vehicle. Under the law of most States, it is a crime either to ignore a policeman’s signal to stop one’s car or, once having stopped, to drive away without permission. <em>E. g., </em><span class="citation no-link">Ohio Rev. Code Ann. §4511.02</span> (1982).<footnotemark>24</footnotemark> Certainly few motorists would feel free either to disobey a directive to pull over or to leave the scene of a traffic stop without being told they might do so.<footnotemark>25</footnotemark> Partly for these reasons, we have long acknowledged that “stopping an automobile and detaining its occupants constitute a ‘sei<page-number citation-index="1" label="437">*437</page-number>zure’ within the meaning of [the Fourth] Amendment], even though the purpose of the stop is limited and the resulting detention quite brief.” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 663</a></span> (1979) (citations omitted).</p>
<p id="b479-5">However, we decline to accord talismanic power to the phrase in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion emphasized by respondent. Fidelity to the doctrine announced in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires that it be enforced strictly, but only in those types of situations in which the concerns that powered the decision are implicated. Thus, we must decide whether a traffic stop exerts upon a detained person pressures that sufficiently impair his free exercise of his privilege against self-incrimination to require that he be warned of his constitutional rights.</p>
<p id="b479-6">Two features of an ordinary traffic stop mitigate the danger that a person questioned will be induced “to speak where he would not otherwise do so freely,” <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. First, detention of a motorist pursuant to a traffic stop is presumptively temporary and brief. The vast majority of roadside detentions last only a few minutes. A motorist’s expectations, when he sees a policeman’s fight flashing behind him, are that he will be obliged to spend a short period of time answering questions and waiting while the officer checks his license and registration, that he may then be given a citation, but that in the end he most likely will be allowed to continue on his way.<footnotemark>26</footnotemark> In this respect, <page-number citation-index="1" label="438">*438</page-number>questioning incident to an ordinary traffic stop is quite different from stationhouse interrogation, which frequently is prolonged, and in which the detainee often is aware that questioning will continue until he provides his interrogators the answers they seek. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#451" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 451</a></span>.<footnotemark>27</footnotemark></p>
<p id="b480-5">Second, circumstances associated with the typical traffic stop are not such that the motorist feels completely at the mercy of the police. To be sure, the aura of authority surrounding an armed, uniformed officer and the knowledge that the officer has some discretion in deciding whether to issue a citation, in combination, exert some pressure on the detainee to respond to questions. But other aspects of the situation substantially offset these forces. Perhaps most importantly, the typical traffic stop is public, at least to some degree. Passersby, on foot or in other cars, witness the interaction of officer and motorist. This exposure to public view both reduces the ability of an unscrupulous policeman to use illegitimate means to elicit self-incriminating statements and diminishes the motorist’s fear that, if he does not cooperate, he will be subjected to abuse. The fact that the detained motorist typically is confronted by only one or at most two policemen further mutes his sense of vulnerability. In short, the atmo<page-number citation-index="1" label="439">*439</page-number>sphere surrounding an ordinary traffic stop is substantially less “police dominated” than that surrounding the kinds of interrogation at issue in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself, see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445, 491-498</a></span>, and in the subsequent cases in which we have applied <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em><footnotemark><em>28</em></footnotemark></p>
<p id="b481-5">In both of these respects, the usual traffic stop is more analogous to a so-called <em>“Terry </em>stop,” see <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), than to a formal arrest.<footnotemark>29</footnotemark> Under the Fourth Amendment, we have held, a policeman who lacks probable cause but whose “observations lead him reasonably to suspect” that a particular person has committed, is committing, or is about to commit a crime, may detain that person briefly<footnotemark>30</footnotemark> in order to “investigate the circumstances that provoke suspicion.” <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975). “[T]he stop and inquiry must be ‘reasonably related in scope to the justification for their initiation.’” <em>Ibid, </em>(quoting <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 29</a></span>.) Typically, this means that the officer may ask the detainee a moderate number of questions to determine his identity and to try to obtain information confirming or dispelling the officer’s suspicions. But the detainee is not obliged to respond. And, unless the detainee’s answers provide the officer with probable cause to arrest him,<footnotemark>31</footnotemark> he must then be <page-number citation-index="1" label="440">*440</page-number>released.<footnotemark>32</footnotemark> The comparatively nonthreatening character of detentions of this sort explains the absence of any suggestion in our opinions that <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stops are subject to the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The similarly noncoercive aspect of ordinary traffic stops prompts us to hold that persons temporarily detained pursuant to such stops are not “in custody” for the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b482-5">Respondent contends that to “exempt” traffic stops from the coverage of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>will open the way to widespread abuse. Policemen will simply delay formally arresting detained motorists, and will subject them to sustained and intimidating interrogation at the scene of their initial detention. Cf. <em>State </em>v. <em>Roberti, </em><span class="citation" data-id="9845476"><a href="/opinion/1262034/state-v-roberti/#95" aria-description="Citation for case: State v. Roberti">293 Ore. 59, 95</a></span>, <span class="citation" data-id="9845476"><a href="/opinion/1262034/state-v-roberti/#1125" aria-description="Citation for case: State v. Roberti">644 P. 2d 1104, 1125</a></span> (1982) (Linde, J., dissenting) (predicting the emergence of a rule that “a person has not been significantly deprived of freedom of action for <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>purposes as long as he is in his own car, even if it is surrounded by several patrol cars and officers with drawn weapons”), withdrawn on rehearing, <span class="citation" data-id="1381407"><a href="/opinion/1381407/state-v-roberti/" aria-description="Citation for case: State v. Roberti">293 Ore. 236</a></span>, <span class="citation" data-id="1381407"><a href="/opinion/1381407/state-v-roberti/" aria-description="Citation for case: State v. Roberti">646 P. 2d 1341</a></span> (1982), cert. pending, No. 82-315. The net result, respondent contends, will be a serious threat to the rights that the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>doctrine is designed to protect.</p>
<p id="b482-6">We are confident that the state of affairs projected by respondent will not come to pass. It is settled that the safeguards prescribed by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>become applicable as soon as a suspect’s freedom of action is curtailed to a “degree associated with formal arrest.” <em>California </em>v. <em>Beheler, </em><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <em>(per curiam). </em>If a motorist who has been detained pursuant to a traffic stop thereafter is subjected to treatment that renders him “in custody” for practical purposes, he will be entitled to the full panoply of protections prescribed by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See <em>Oregon </em>v. <em>Mathiason, </em><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <em>(per curiam).</em></p>
<p id="b483-4"><page-number citation-index="1" label="441">*441</page-number>Admittedly, our adherence to the doctrine just recounted will mean that the police and lower courts will continue occasionally to have difficulty deciding exactly when a suspect has been taken into custody. Either a rule that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>applies to all traffic stops or a rule that a suspect need not be advised of his rights until he is formally placed under arrest would provide a clearer, more easily administered line. However, each of these two alternatives has drawbacks that make it unacceptable. The first would substantially impede the enforcement of the Nation’s traffic laws — by compelling the police either to take the time to warn all detained motorists of their constitutional rights or to forgo use of self-incriminating statements made by those motorists — while doing little to protect citizens’ Fifth Amendment rights.<footnotemark>33</footnotemark> The second would enable the police to circumvent the constraints on custodial interrogations established by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
<p id="b483-5">Turning to the case before us, we find nothing in the record that indicates that respondent should have been given <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings at any point prior to the time Trooper Williams placed him under arrest. For the reasons indicated above, we reject the contention that the initial stop of respondent’s car, by itself, rendered him “in custody.” And respondent has failed to demonstrate that, at any time between the initial stop and the arrest, he was subjected to restraints comparable to those associated with a formal arrest. Only a short period of time elapsed between the stop and the arrest.<footnotemark>34</footnotemark> At no point during that interval was respondent <page-number citation-index="1" label="442">*442</page-number>informed that his detention would not be temporary. Although Trooper Williams apparently decided as soon as respondent stepped out of his car that respondent would be taken into custody and charged with a traffic offense, Williams never communicated his intention to respondent. A policeman’s unarticulated plan has no bearing on the question whether a suspect was “in custody” at a particular time; the only relevant inquiry is how a reasonable man in the suspect’s position would have understood his situation.<footnotemark>35</footnotemark> Nor do other aspects of the interaction of Williams and respondent support the contention that respondent was exposed to “custodial interrogation” at the scene of the stop. From aught that appears in the stipulation of facts, a single police officer asked respondent a modest number of questions and requested him to perform a simple balancing test at a location visible to passing motorists.<footnotemark>36</footnotemark> Treatment of this sort cannot fairly be characterized as the functional equivalent of formal arrest.</p>
<p id="b484-5">We conclude, in short, that respondent was not taken into custody for the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>until Williams arrested him. Consequently, the statements respondent made prior to that point were admissible against him.</p>
<p id="b484-6">IV</p>
<p id="b484-7">We are left with the question of the appropriate remedy. In his brief, petitioner contends that, if we agree with the <page-number citation-index="1" label="443">*443</page-number>Court of Appeals that respondent’s postarrest statements should have been suppressed but conclude that respondent’s prearrest statements were admissible, we should reverse the Court of Appeals’ judgment on the ground that the state trial court’s erroneous refusal to exclude the postarrest admissions constituted “harmless error” within the meaning of <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). Relying on <em>Milton </em>v. <em>Wainwright, </em><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), petitioner argues that the statements made by respondent at the police station “were merely recitations of what respondent had already admitted at the scene of the traffic arrest” and therefore were unnecessary to his conviction. Brief for Petitioner 25. We reject this proposed disposition of the case for three cumulative reasons.</p>
<p id="b485-5">First, the issue of harmless error was not presented to any of the Ohio courts, to the District Court, or to the Court of Appeals.<footnotemark>37</footnotemark> Though, when reviewing a judgment of a federal court, we have jurisdiction to consider an issue not raised below, see <em>Carlson </em>v. <em>Green, </em><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/#17" aria-description="Citation for case: Carlson v. Green">446 U. S. 14, 17, n. 2</a></span> (1980), we are generally reluctant to do so, <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#147" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 147, n. 2</a></span> (1970).<footnotemark>38</footnotemark></p>
<p id="b485-6">Second, the admissions respondent made at the scene of the traffic stop and the statements he made at the police station were not identical. Most importantly, though respondent at the scene admitted having recently drunk beer and smoked marihuana, not until questioned at the station did he <page-number citation-index="1" label="444">*444</page-number>acknowledge being under the influence of intoxicants, an essential element of the crime for which he was convicted.<footnotemark>39</footnotemark> This fact assumes significance in view of the failure of the intoxilyzer test to discern any alcohol in his blood.</p>
<p id="b486-5">Third, the case arises in a procedural posture that makes the use of harmless-error analysis especially difficult.<footnotemark>40</footnotemark> This is not a case in which a defendant, after denial of a suppression motion, is given a full trial resulting in his conviction. Rather, after the trial court ruled that all of respondent’s self-incriminating statements were admissible, respondent elected not to contest the prosecution’s case against him, while preserving his objection to the denial of his pretrial motion.<footnotemark>41</footnotemark> As a result, respondent has not yet had an opportunity to try to impeach the State’s evidence or to present evidence of his own. For example; respondent alleges that, at the time of his arrest, he had an injured back and a limp<footnotemark>42</footnotemark> and that those ailments accounted for his difficulty getting out of the car and performing the balancing test; because he pleaded “no contest,” he never had a chance to make that argument to a jury. It is difficult enough, on the basis of a complete record of a trial and the parties’ contentions regarding the relative importance of each portion of the evidence presented, to determine whether the erroneous admission of particular material affected the outcome. Without the benefit of such a record in this case, we decline to rule that <page-number citation-index="1" label="445">*445</page-number>the trial court’s refusal to suppress respondent’s postarrest statements “was harmless beyond a reasonable doubt.” See <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S., at 24</a></span>.</p>
<p id="b487-5">Accordingly, the judgment of the Court of Appeals is</p>
<p id="b487-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b465-10"> For a description of the technology associated with the intoxilyzer test, see <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#481" aria-description="Citation for case: California v. Trombetta">467 U. S. 479, 481-482</a></span> (1984).</p>
</footnote>
<footnote label="2">
<p id="b466-9"> <span class="citation no-link">Ohio Rev. Code Ann. §2937.07</span> (1982) provides, in pertinent part: “If the plea be ‘no contest’ or words of similar import in pleading to a misdemeanor, it shall constitute a stipulation that the judge or magistrate may-make [a] finding of guilty or not guilty from the explanation of circumstances, and if guilt be found, impose or continue for sentence accordingly.”</p>
<p id="b466-10">Ohio Rule of Criminal Procedure 12(H) provides: “The plea of no contest does not preclude a defendant from asserting upon appeal that the trial <page-number citation-index="1" label="425">*425</page-number>court prejudicially erred in ruling on a pretrial motion, including a pretrial motion to suppress evidence.”</p>
</footnote>
<footnote label="3">
<p id="b467-10"> On respondent’s motion, the state trial court stayed execution of respondent’s sentence pending the outcome of his application for a writ of habeas corpus. <em>State </em>v. <em><span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/" aria-description="Citation for case: Richard McCarty v. Captain Herdman">McCarty</a></span>, </em>No. 80-TF-C-123915 (Franklin County Mun. Ct., July 28, 1981).</p>
</footnote>
<footnote label="4">
<p id="b467-11"> In differentiating respondent’s various admissions, the Court of Appeals accorded no significance to the parties’ stipulation that respondent’s <page-number citation-index="1" label="426">*426</page-number>“freedom to leave the scene was terminated” at the moment Trooper Williams formed an intent to arrest respondent. The court reasoned that a “‘reasonable man’ test,” not a subjective standard, should control the determination of when a suspect is taken into custody for the purposes of <em>Miranda. McCarty </em>v. <em>Herdman, </em><span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/#362" aria-description="Citation for case: Richard McCarty v. Captain Herdman">716 F. 2d, at 362</a></span>, n. 1 (quoting <em>Lowe </em>v. <em>United States, </em><span class="citation" data-id="283849"><a href="/opinion/283849/arnold-lowe-v-united-states/#1397" aria-description="Citation for case: Arnold Lowe v. United States">407 F. 2d 1391, 1397</a></span> (CA9 1969)).</p>
</footnote>
<footnote label="5">
<p id="b468-10"> Judge Wellford, dissenting, observed: “As I read the opinion, the majority finds that McCarty was not in custody until he was formally placed under arrest.” <span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/#364" aria-description="Citation for case: Richard McCarty v. Captain Herdman">716 F. 2d, at 364</a></span>. The majority neither accepted nor disavowed this interpretation of its ruling.</p>
</footnote>
<footnote label="6">
<p id="b468-11"> Judge Wellford’s dissent was premised on his view that the incriminating statements made by respondent after he was formally taken into custody were “essentially repetitious” of the statements he made before his arrest. Reasoning that the prearrest statements were admissible, Judge Wellford argued that the trial court’s failure to suppress the postarrest statements was “harmless error.” <span class="citation" data-id="9471108"><a href="/opinion/424072/richard-mccarty-v-captain-herdman/#365" aria-description="Citation for case: Richard McCarty v. Captain Herdman"><em>Id., </em>at 365</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b469-5"> In <em>Clay v. Riddle, </em><span class="citation" data-id="9463049"><a href="/opinion/338963/gene-david-clay-v-walter-m-riddle-superintendent-virginia-state/" aria-description="Citation for case: Gene David Clay v. Walter M. Riddle, Superintendent,...">541 F. 2d 456</a></span> (1976), the Court of Appeals for the Fourth Circuit held that persons arrested for traffic offenses need not be given <em>Miranda </em>warnings. <span class="citation" data-id="9463049"><a href="/opinion/338963/gene-david-clay-v-walter-m-riddle-superintendent-virginia-state/#457" aria-description="Citation for case: Gene David Clay v. Walter M. Riddle, Superintendent,..."><em>Id., </em>at 457</a></span>. Several state courts have taken similar positions. See <em>State </em>v. <em>Bliss, </em><span class="citation" data-id="2011645"><a href="/opinion/2011645/state-v-bliss/#850" aria-description="Citation for case: State v. Bliss">238 A. 2d 848, 850</a></span> (Del. 1968); <em>County of Dade </em>v. <em>Callahan, </em><span class="citation" data-id="1110495"><a href="/opinion/1110495/county-of-dade-v-callahan/#507" aria-description="Citation for case: County of Dade v. Callahan">259 So. 2d 504, 507</a></span> (Fla. App. 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/So.%202d/265/50/">265 So. 2d 50</a></span> (Fla. 1972); <em>State </em>v. <em>Gabrielson, </em><span class="citation" data-id="9657081"><a href="/opinion/1592530/state-v-gabrielson/#796" aria-description="Citation for case: State v. Gabrielson">192 N. W. 2d 792, 796</a></span> (Iowa 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/912/">409 U. S. 912</a></span> (1972); <em>State </em>v. <em>Angelo, </em><span class="citation" data-id="1725045"><a href="/opinion/1725045/state-v-angelo/#254" aria-description="Citation for case: State v. Angelo">251 La. 250, 254-255</a></span>, <span class="citation" data-id="1725045"><a href="/opinion/1725045/state-v-angelo/#711" aria-description="Citation for case: State v. Angelo">203 So. 2d 710, 711-717</a></span> (1967); <em>State </em>v. <em>Neal, </em><span class="citation" data-id="9762397"><a href="/opinion/2380940/state-v-neal/#553" aria-description="Citation for case: State v. Neal">476 S. W. 2d 547, 553</a></span> (Mo. 1972); <em>State </em>v. <em>Macuk, </em>57 N. J. 1, 15-16, <span class="citation" data-id="1935505"><a href="/opinion/1935505/state-v-macuk/#9" aria-description="Citation for case: State v. MacUk">268 A. 2d 1, 9</a></span> (1970). Other state courts have refused to limit in this fashion the reach of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See <em>Campbell </em>v. <em>Superior Court, </em><span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/#552" aria-description="Citation for case: Campbell v. Superior Court">106 Ariz. 542, 552</a></span>, <span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/#695" aria-description="Citation for case: Campbell v. Superior Court">479 P. 2d 685, 695</a></span> (1971); <em>Commonwealth </em>v. <em>Brennan, </em><span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/#775" aria-description="Citation for case: Commonwealth v. Brennan">386 Mass. 772, 775</a></span>, <span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/#63" aria-description="Citation for case: Commonwealth v. Brennan">438 N. E. 2d 60, 63</a></span> (1982); <em>State </em>v. <em>Kinn, </em><span class="citation" data-id="1939088"><a href="/opinion/1939088/state-v-kinn/#35" aria-description="Citation for case: State v. Kinn">288 Minn. 31, 35</a></span>, <span class="citation" data-id="1939088"><a href="/opinion/1939088/state-v-kinn/#891" aria-description="Citation for case: State v. Kinn">178 N. W. 2d 888, 891</a></span> (1970); <em>State </em>v. <em>Lawson, </em><span class="citation" data-id="1220711"><a href="/opinion/1220711/state-v-lawson/#327" aria-description="Citation for case: State v. Lawson">285 N. C. 320, 327-328</a></span>, <span class="citation" data-id="1220711"><a href="/opinion/1220711/state-v-lawson/#848" aria-description="Citation for case: State v. Lawson">204 S. E. 2d 843, 848</a></span> (1974); <em>State </em>v. <em>Fields, </em><span class="citation" data-id="2086722"><a href="/opinion/2086722/state-v-fields/#409" aria-description="Citation for case: State v. Fields">294 N. W. 2d 404, 409</a></span> (N. D. 1980) <em>(Miranda </em>applicable at least to “more serious [traffic] offense[s] such as driving while intoxicated”); <em>State </em>v. <em>Buchholz, </em><span class="citation" data-id="6758378"><a href="/opinion/6867520/state-v-buchholz/#28" aria-description="Citation for case: State v. Buchholz">11 Ohio St. 3d 24, 28</a></span>, <span class="citation" data-id="6758378"><a href="/opinion/6867520/state-v-buchholz/#1226" aria-description="Citation for case: State v. Buchholz">462 N. E. 2d 1222, 1226</a></span> (1984) (overruling <em>State </em>v. <em>Pyle, </em><span class="citation" data-id="6754230"><a href="/opinion/6864453/state-v-pyle/" aria-description="Citation for case: State v. Pyle">19 Ohio St. 2d 64</a></span>, <span class="citation" data-id="6754230"><a href="/opinion/6864453/state-v-pyle/" aria-description="Citation for case: State v. Pyle">249 N. E. 2d 826</a></span> (1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1007/">396 U. S. 1007</a></span> (1970), and holding that <em>“Miranda </em>warnings must be given prior to any custodial interrogation regardless of whether the individual is suspected of committing a felony or misdemeanor”); <em>State </em>v. <em>Roberti, </em><span class="citation" data-id="9845476"><a href="/opinion/1262034/state-v-roberti/" aria-description="Citation for case: State v. Roberti">293 Ore. 59</a></span>, <span class="citation" data-id="9845476"><a href="/opinion/1262034/state-v-roberti/" aria-description="Citation for case: State v. Roberti">644 P. 2d 1104</a></span>, on rehearing, <span class="citation" data-id="1381407"><a href="/opinion/1381407/state-v-roberti/" aria-description="Citation for case: State v. Roberti">293 Ore. 236</a></span>, <span class="citation" data-id="1381407"><a href="/opinion/1381407/state-v-roberti/" aria-description="Citation for case: State v. Roberti">646 P. 2d 1341</a></span> (1982), cert. pending, No. 82-315; <em>Commonwealth </em>v. <em>Meyer, </em><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#305" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa. 297, 305-306</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#521" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d 517, 521</a></span> (1980); <em>Holman </em>v. <em>Cox, </em><span class="citation" data-id="9565687"><a href="/opinion/1217972/holman-v-cox/#1333" aria-description="Citation for case: Holman v. Cox">598 P. 2d 1331, 1333</a></span> (Utah 1979); <em>State </em>v. <em>Darnell, </em><span class="citation" data-id="1223447"><a href="/opinion/1223447/state-v-darnell/#628" aria-description="Citation for case: State v. Darnell">8 Wash. App. 627, 628</a></span>, <span class="citation" data-id="1223447"><a href="/opinion/1223447/state-v-darnell/#615" aria-description="Citation for case: State v. Darnell">508 P. 2d 613, 615</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1112/">414 U. S. 1112</a></span> (1973). 8</p>
</footnote>
<footnote label="8">
<p id="b469-6"> The lower courts have dealt with the problem of roadside questioning in a wide variety of ways. For a spectrum of positions, see <em>State </em>v. <em>Tellez, </em><span class="citation" data-id="9537916"><a href="/opinion/1146993/state-v-tellez/#256" aria-description="Citation for case: State v. Tellez">6 Ariz. App. 251, 256</a></span>, <span class="citation" data-id="9537916"><a href="/opinion/1146993/state-v-tellez/#696" aria-description="Citation for case: State v. Tellez">431 P. 2d 691, 696</a></span> (1967) <em>(.Miranda </em>warnings must be given as soon as the policeman has “reasonable grounds” to believe the detained motorist has committed an offense); <em>Newberry </em>v. <em>State, </em><span class="citation" data-id="9775988"><a href="/opinion/2452444/newberry-v-state/#461" aria-description="Citation for case: Newberry v. State">552 S. W. 2d 457, 461</a></span> (Tex. Crim. App. 1977) <em>(Miranda </em>applies when there is probable cause to arrest the driver and the policeman “consider[s the driver] to be in custody and would not... let him leave”); <em>State </em>v. <em>Roberti, </em>293 Ore., at 236, <span class="citation" data-id="1381407"><a href="/opinion/1381407/state-v-roberti/#1341" aria-description="Citation for case: State v. Roberti">646 P. 2d, at 1341</a></span> <em>(Miranda </em>applies as soon as the officer forms an intention to arrest the motorist); <em>People </em>v. <em>Ramirez, </em><span class="citation" data-id="1430357"><a href="/opinion/1430357/people-v-ramirez/#372" aria-description="Citation for case: People v. Ramirez">199 Colo. 367, 372, n. 5</a></span>, <span class="citation" data-id="1430357"><a href="/opinion/1430357/people-v-ramirez/#618" aria-description="Citation for case: People v. Ramirez">609 P. 2d 616, 618, n. 5</a></span> (1980) (en banc); <em>State </em>v. <span class="citation" data-id="1223447"><a href="/opinion/1223447/state-v-darnell/#629" aria-description="Citation for case: State v. Darnell"><em>Darnell, supra, </em>at 629-630</a></span>, <span class="citation" data-id="1223447"><a href="/opinion/1223447/state-v-darnell/#615" aria-description="Citation for case: State v. Darnell">508 P. 2d, at 615</a></span> (driver is “in custody” for <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>purposes at <page-number citation-index="1" label="428">*428</page-number>least by the time he is asked to take a field sobriety test); <em>Commonwealth </em>v. <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#307" aria-description="Citation for case: Commonwealth v. Meyer"><em>Meyer, supra, </em>at 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#521" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d, at 521-522</a></span> (warnings are required as soon as the motorist “reasonably believes his freedom of action is being restricted”); <em>Lowe </em>v. <em>United States, supra, </em>at 1394, 1396; <em>State </em>v. <em>Sykes, </em><span class="citation" data-id="1325690"><a href="/opinion/1325690/state-v-sykes/#205" aria-description="Citation for case: State v. Sykes">285 N. C. 202, 205-206</a></span>, <span class="citation" data-id="1325690"><a href="/opinion/1325690/state-v-sykes/#850" aria-description="Citation for case: State v. Sykes">203 S. E. 2d 849, 850</a></span> (1974) <em>(Miranda </em>is inapplicable to a traffic stop until the motorist is subjected to formal arrest or the functional equivalent thereof); <em>Allen </em>v. <em>United States, </em>129 U. S. App. D. C. 61, 63-64, <span class="citation" data-id="9453381"><a href="/opinion/279036/vance-v-allen-v-united-states/#478" aria-description="Citation for case: Vance v. Allen v. United States">390 F. 2d 476, 478-479</a></span> (“[S]ome inquiry can be made [without giving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings] as part of an investigation notwithstanding limited and brief restraints by the police in their effort to screen crimes from relatively routine mishaps”), modified, 131 U. S. App. <em>D. C. </em>358, <span class="citation" data-id="282815"><a href="/opinion/282815/vance-v-allen-v-united-states/" aria-description="Citation for case: Vance v. Allen v. United States">404 F. 2d 1335</a></span> (1968); <em>Holman </em>v. <span class="citation" data-id="9565687"><a href="/opinion/1217972/holman-v-cox/#1333" aria-description="Citation for case: Holman v. Cox"><em>Cox, supra, </em>at 1333</a></span> <em>(Miranda </em>applies upon formal arrest).</p>
</footnote>
<footnote label="9">
<p id="b471-7"> In <em>Harris </em>v. <em>New York, </em><span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), the Court did sanction use of statements obtained in violation of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to impeach the defendant who had made them. The Court was careful to note, however, that the jury had been instructed to consider the statements “only in passing on [the defendant’s] credibility and not as evidence of guilt.” <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#223" aria-description="Citation for case: Harris v. New York">401 U. S., at 223</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b471-8"> The one exception to this consistent line of decisions is <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984). The Court held in that case that, when the police arrest a suspect under circumstances presenting an imminent danger to the public safety, they may without informing him of his constitutional rights ask questions essential to elicit information necessary to neutralize the threat to the public. Once such information has' been obtained, the suspect must be given the standard warnings.</p>
</footnote>
<footnote label="11">
<p id="b471-9"> Not all of petitioner’s formulations of his proposal are consistent. At some points in his brief and at oral argument, petitioner appeared to advocate an exception solely for drunken-driving charges; at other points, he <page-number citation-index="1" label="430">*430</page-number>seemed to favor a line between felonies and misdemeanors. Because all of these suggestions suffer from similar infirmities, we do not differentiate among them in the ensuing discussion.</p>
</footnote>
<footnote label="12">
<p id="b473-6"> Thus, under Ohio law, while a first offense of negligent vehicular homicide is a misdemeanor, a second offense is a felony. <span class="citation no-link">Ohio Rev. Code Ann. § 2903.07</span> (Supp. 1983). In some jurisdictions, a certain number of convictions for drunken driving triggers a quantum jump in the status of the crime. In South Dakota, for instance, first and second offenses for driving while intoxicated are misdemeanors, but a third offense is a felony. See <em>Solem </em>v. <em>Helm, </em><span class="citation" data-id="9429310"><a href="/opinion/111000/solem-v-helm/#280" aria-description="Citation for case: Solem v. Helm">463 U. S. 277, 280, n. 4</a></span> (1983).</p>
</footnote>
<footnote label="13">
<p id="b473-7"> Cf. <em>Welsh </em>v. <em>Wisconsin, </em><span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#761" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 761</a></span> (1984) (White, J., dissenting) (observing that officers in the field frequently “have neither the time nor the competence to determine” the severity of the offense for which they are considering arresting a person).</p>
<p id="b473-8">It might be argued that the police would not need to make such guesses; whenever in doubt, they could ensure compliance with the law by giving the full <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. It cannot be doubted, however, that in some cases a desire to induce a suspect to reveal information he might withhold if informed of his rights would induce the police not to take the cautious course.</p>
</footnote>
<footnote label="14">
<p id="b473-9"> See, <em>e. g., United States </em>v. <em>Schultz, </em><span class="citation" data-id="2285332"><a href="/opinion/2285332/united-states-v-schultz/" aria-description="Citation for case: United States v. Schultz">442 F. Supp. 176</a></span> (Md. 1977) (investigation of erratic driving developed into inquiry into narcotics offenses and terminated in a charge of possession of a sawed-off shotgun); <em>United States </em>v. <em>Hatchel, </em><span class="citation" data-id="2596176"><a href="/opinion/2596176/united-states-v-hatchel/" aria-description="Citation for case: United States v. Hatchel">329 F. Supp. 113</a></span> (Mass. 1971) (investigation into offense of driving the wrong way on a one-way street yielded a charge of possession of a stolen car).</p>
</footnote>
<footnote label="15">
<p id="b474-6">Cf. <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#221" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 221, n. 1</a></span> (1973); <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#238" aria-description="Citation for case: United States v. Robinson"><em>id., </em>at 238, n. 2</a></span> (Powell, J., concurring) (discussing the problem of determining if a traffic arrest was used as a pretext to legitimate a warrantless search for narcotics).</p>
</footnote>
<footnote label="16">
<p id="b474-7"> Cf. <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#663" aria-description="Citation for case: New York v. Quarles">467 U. S., at 663-664</a></span> (O’Connor, J., concurring in judgment in part and dissenting in part).</p>
</footnote>
<footnote label="17">
<p id="b474-8"> See Brief for State of Ohio as <em>Amicus Curiae </em>18-21 (discussing the “National Epidemic Of Impaired Drivers” and the importance of stemming it); cf. <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#558" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 558-559</a></span> (1983); <em>Perez </em>v. <em>Campbell, </em><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/#657" aria-description="Citation for case: Perez. v. Campbell">402 U. S. 637, 657, 672</a></span> (1971) (Blackmun, J., concurring in part and dissenting in part).</p>
</footnote>
<footnote label="18">
<p id="b475-6"> See <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#299" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 299, 301</a></span> (1980); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 445-458</a></span> (1966).</p>
</footnote>
<footnote label="19">
<p id="b475-7"> <em>Minnesota </em>v. <em>Murphy, </em><span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#430" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 430</a></span> (1984) (quoting <em>Miranda </em>v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><em>Arizona, supra, </em>at 467</a></span>); see <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#467" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 467</a></span> (1981); <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187, n. 5</a></span> (1977).</p>
</footnote>
<footnote label="20">
<p id="b475-8"> Cf. Developments in the Law — Confessions, <span class="citation no-link">79 Harv. L. Rev. 935</span>, 954-984 (1966) (describing the difficulties encountered by state and federal courts, during the period preceding the decision in <em>Miranda, </em>in trying to distinguish voluntary from involuntary confessions).</p>
<p id="b475-9">We do not suggest that compliance with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>conclusively establishes the voluntariness of a subsequent confession. But cases in which a defendant can make a colorable argument that a self-incriminating statement was “compelled” despite the fact that the law enforcement authorities adhered to the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are rare.</p>
</footnote>
<footnote label="21">
<p id="b476-7"> The parties urge us to answer two questions concerning the precise scope of the safeguards required in circumstances of the sort involved in this case. First, we are asked to consider what a State must do in order to demonstrate that a suspect who might have been under the influence of drugs or alcohol when subjected to custodial interrogation nevertheless understood and freely waived his constitutional rights. Second, it is suggested that we decide whether an indigent suspect has a right, under the Fifth Amendment, to have an attorney appointed to advise him regarding his responses to custodial interrogation when the alleged offense about which he is being questioned is sufficiently minor that he would not have a right, under the Sixth Amendment, to the assistance of appointed counsel at trial, see <em>Scott </em>v. <em>Illinois, </em><span class="citation" data-id="9427479"><a href="/opinion/110032/scott-v-illinois/" aria-description="Citation for case: Scott v. Illinois">440 U. S. 367</a></span> (1979). We prefer to defer resolution of such matters to a case in which law enforcement authorities have at least attempted to inform the suspect of rights to which he is indisputably entitled.</p>
</footnote>
<footnote label="22">
<p id="ADS"> In his brief, respondent hesitates to embrace this proposition fully, advocating instead a more limited rule under which questioning of a suspect detained pursuant to a traffic stop would be deemed “custodial interrogation” if and only if the police officer had probable cause to arrest the motorist for a crime. See Brief for Respondent 39-40, 46. This ostensibly more modest proposal has little to recommend it. The threat to a citizen’s Fifth Amendment rights that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was designed to neutralize has little to do with the strength of an interrogating officer’s suspicions. And, by requiring a policeman conversing with a motorist constantly to monitor the information available to him to determine when it becomes sufficient to establish probable cause, the rule proposed by respondent would be extremely difficult to administer. Accordingly, we confine our attention below to respondent’s stronger argument: that all traffic stops are subject to the dictates of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="23">
<p id="ACnN"> It might be argued that, insofar as the Court of Appeals expressly held inadmissible only the statements made by respondent after his formal arrest, and respondent has not filed a cross-petition, respondent is dis-entitled at this juncture to assert that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings must be given to a detained motorist who has not been arrested. See, <em>e. g., United States </em>v. <em>Reliable Transfer Co., </em><span class="citation" data-id="109252"><a href="/opinion/109252/united-states-v-reliable-transfer-co/#401" aria-description="Citation for case: United States v. Reliable Transfer Co.">421 U. S. 397, 401, n. 2</a></span> (1975). However, three considerations, in combination, prompt us to consider the question highlighted by respondent. First, as indicated above, the Court of Appeals’ judgment regarding the time at which <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>became applicable is ambiguous; some of the court’s statements cast doubt upon the admissibility <page-number citation-index="1" label="436">*436</page-number>of respondent’s prearrest statements. See <em>swpra, </em>at 425-426. Without undue strain, the position taken by respondent before this Court thus might be characterized as an argument in support of the judgment below, which respondent is entitled to make. Second, the relevance of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to the questioning of a motorist detained pursuant to a traffic stop is an issue that plainly warrants our attention, and with regard to which the lower courts are in need of guidance. Third and perhaps most importantly, both parties have briefed and argued the question. Under these circumstances, we decline to interpret and apply strictly the rule that we will not address an argument advanced by a respondent that would enlarge his rights under a judgment, unless he has filed a cross-petition for certiorari.</p>
</footnote>
<footnote label="24">
<p id="b478-7"> Examples of similar provisions in other States are: <span class="citation no-link">Ariz. Rev. Stat. Ann. §§28-622</span>, 28-622.01 (1976 and Supp. 1983-1984); Cal. Veh. Code Ann. §§2800, 2800.1 (West Supp. 1984); Del. Code Ann., Tit. 21, §4103 (1979); <span class="citation no-link">Fla. Stat. §316.1935</span> (Supp. 1984); Ill. Rev. Stat., ch. 95%, ¶ 11-204 (1983); N. Y. Veh. &amp; Traf. Law § 1102 (McKinney Supp. 1983-1984); <span class="citation no-link">Nev. Rev. Stat. §484.348</span>(1) (1983); <span class="citation no-link">75 Pa. Cons. Stat. § 3733</span>(a) (1977); <span class="citation no-link">Wash. Rev. Code §46.61.020</span> (1983).</p>
</footnote>
<footnote label="25">
<p id="b478-8"> Indeed, petitioner frankly admits that “[n]o reasonable person would feel that he was free to ignore the visible and audible signal of a traffic safety enforcement officer .... Moreover, it is nothing short of sophistic to state that a motorist ordered by a police officer to step out of his vehicle would reasonably] or prudently believe that he was at liberty to ignore that command.” Brief for Petitioner 16-17.</p>
</footnote>
<footnote label="26">
<p id="b479-7"> State laws governing when a motorist detained pursuant to a traffic stop may or must be issued a citation instead of taken into custody vary significantly, see Y. Kamisar, W. LaFave, &amp; J. Israel, Modern Criminal Procedure 402, n. a (5th ed. 1980), but no State requires that a detained motorist be arrested unless he is accused of a specified serious crime, refuses to promise to appear in court, or demands to be taken before a magistrate. For a representative sample of these provisions, see <span class="citation no-link">Ariz. Rev. Stat. Ann. §§28-1053</span>, 28-1054 (1976); <span class="citation no-link">Ga. Code Ann. §40-13-53</span> (Supp. 1983); <span class="citation no-link">Kan. Stat. Ann. §§8-2105</span>, 8-2106 (1982); <span class="citation no-link">Nev. Rev. Stat. §§484.793</span>, 484.795, 484.797, 484.799, 484.805 (1983); Ore. Rev. Stat. § 484.353 (1983); S. D. Codified Laws § 32-33-2 (Supp. 1983); Tex. Rev. Civ. Stat. Ann., Art. 6701d, §§147, 148 (Vernon 1977); Va. Code <page-number citation-index="1" label="438">*438</page-number>§46.1-178 (Supp. 1983). Cf. National Committee on Uniform Traffic Laws and Ordinances, Uniform Vehicle Code and Model Traffic Ordinance §§ 16-203 — 16-206 (Supp. 1979) (advocating mandatory release on citation of all drivers except those charged with specified offenses, those who fail to furnish satisfactory self-identification, and those as to whom the officer has “reasonable and probable grounds to believe . . . will disregard a written promise to appear in court”).</p>
</footnote>
<footnote label="27">
<p id="b480-7"> The brevity and spontaneity of an ordinary traffic stop also reduces the danger that the driver through subterfuge will be made to incriminate himself. One of the investigative techniques that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was designed to guard against was the use by police of various kinds of trickery — such as “Mutt and Jeff” routines — to elicit confessions from suspects. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#448" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 448-455</a></span>. A police officer who stops a suspect on the highway has little chance to develop or implement a plan of this sort. Cf. LaFave, “Street Encounters” and the Constitution: <em>Terry, Sibron, Peters, </em>and Beyond, <span class="citation no-link">67 Mich. L. Rev. 39</span>, 99 (1968).</p>
</footnote>
<footnote label="28">
<p id="b481-6"> See <em>Orozco </em>v. <em>Texas, </em><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/#325" aria-description="Citation for case: Orozco v. Texas">394 U. S. 324, 325</a></span> (1969) (suspect arrested and questioned in his bedroom by four police officers); <em>Mathis </em>v. <em>United States, </em>391U. S. 1, 2-3 (1968) (defendant questioned by a Government agent while in jail).</p>
</footnote>
<footnote label="29">
<p id="b481-7"> No more is implied by this analogy than that most traffic stops resemble, in duration and atmosphere, the kind of brief detention authorized in <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>. </em>We of course do not suggest that a traffic stop supported by probable cause may not exceed the bounds set by the Fourth Amendment on the scope of a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop.</p>
</footnote>
<footnote label="30">
<p id="b481-8"> Nothing in this opinion is intended to refine the constraints imposed by the Fourth Amendment on the duration of such detentions. Cf. <em>Sharpe </em>v. <em>United States, </em><span class="citation" data-id="9470889"><a href="/opinion/421705/william-harris-sharpe-v-united-states-of-america-donald-davis-savage-v/" aria-description="Citation for case: William Harris Sharpe v. United States of America, Donald...">712 F. 2d 65</a></span> (CA4 1983), cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./467/1250/">467 U. S. 1250</a></span> (1984).</p>
</footnote>
<footnote label="31">
<p id="b481-9"> Cf. <em>Adams v. Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#148" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 148</a></span> (1972).</p>
</footnote>
<footnote label="32">
<p id="b482-7"> Cf. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 34</a></span> (White, J., concurring).</p>
</footnote>
<footnote label="33">
<p id="b483-6"> Contrast the minor burdens on law enforcement and significant protection of citizens’ rights effected by our holding that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>governs custodial interrogation of persons accused of misdemeanor traffic offenses. See <em>supra, </em>at 432-434.</p>
</footnote>
<footnote label="34">
<p id="b483-7"> Cf. <em>Commonwealth </em>v. <em>Meyer, </em><span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#301" aria-description="Citation for case: Commonwealth v. Meyer">488 Pa., at 301, 307</a></span>, <span class="citation" data-id="1981202"><a href="/opinion/1981202/commonwealth-v-meyer/#518" aria-description="Citation for case: Commonwealth v. Meyer">412 A. 2d, at 518-519, 522</a></span> (driver who was detained for over one-half hour, part of the time in a patrol car, held to have been in custody for the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>by the time he was questioned concerning the circumstances of an accident).</p>
</footnote>
<footnote label="35">
<p id="b484-8"> Cf. <em>Beckwith </em>v. <em>United States, </em><span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#346" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 346-347</a></span> (1976) (“ ‘It was the compulsive aspect of custodial interrogation, and not the strength or content of the government’s suspicions at the time the questioning was conducted, which led the Court to impose the <em>Miranda </em>requirements with regard to custodial questioning’ ”) (quoting <em>United States </em>v. <em>Caiello, </em><span class="citation" data-id="9455181"><a href="/opinion/287949/united-states-v-richard-v-caiello/#473" aria-description="Citation for case: United States v. Richard v. Caiello">420 F. 2d 471, 473</a></span> (CA2 1969)); <em>People </em>v. <em>P., </em>21 N. Y. 2d 1, 9-10, <span class="citation" data-id="9787785"><a href="/opinion/2590535/people-v-rodney-panonymous/#260" aria-description="Citation for case: People v. Rodney P.(Anonymous)">233 N. E. 2d 255, 260</a></span> (1967) (an objective, reasonable-man test is appropriate because, unlike a subjective test, it “is not solely dependent either on the self-serving declarations of the police officers or the defendant nor does it place upon the police the burden of anticipating the frailties or idiosyncracies of every person whom they question”).</p>
</footnote>
<footnote label="36">
<p id="b484-9"> Cf. <em>United States </em>v. <em>Schultz, </em><span class="citation" data-id="2285332"><a href="/opinion/2285332/united-states-v-schultz/#180" aria-description="Citation for case: United States v. Schultz">442 F. Supp., at 180</a></span> (suspect who was stopped for erratic driving, subjected to persistent questioning in the <page-number citation-index="1" label="443">*443</page-number>squad car about drinking alcohol and smoking marihuana, and denied permission to contact his mother held to have been in custody for the purposes of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>by the time he confessed to possession of a sawed-off shotgun).</p>
</footnote>
<footnote label="37">
<p id="b485-8"> Judge Wellford, dissenting in the Court of Appeals, did address the issue of harmless error, see n. 6, <em>supra, </em>but without the benefit of briefing by the parties. The majority of the panel of the Court of Appeals did not consider the question.</p>
</footnote>
<footnote label="38">
<p id="b485-9"> Nor did petitioner mention harmless error in his petition to this Court. Absent unusual circumstances, cf. n. 23, <em>supra, </em>we are chary of considering issues not presented in petitions for certiorari. See this Court’s Rule 21.1(a) (“Only the questions set forth in the petition or fairly included therein will be considered by the Court”).</p>
</footnote>
<footnote label="39">
<p id="b486-6"> This case is thus not comparable to <em>Milton </em>v. <em>Wainwright, </em><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), in which a confession presumed to be inadmissible contained no information not already provided by three admissible confessions. See <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/#375" aria-description="Citation for case: Milton v. Wainwright"><em>id., </em>at 375-376</a></span>.</p>
</footnote>
<footnote label="40">
<p id="b486-7"> Because we do not rule that the trial court’s error was harmless, we need not decide whether harmless-error analysis is even applicable to a case of this sort.</p>
</footnote>
<footnote label="41">
<p id="b486-8"> Under Ohio law, respondent had a right to pursue such a course. See n. 2, <em>supra.</em></p>
</footnote>
<footnote label="42">
<p id="b486-9"> Indeed, respondent points out that he told Trooper Williams of these ailments at the time of his arrest, and their existence was duly noted in the Alcohol Influence Report. See App. 2.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Birchfield v. North Dakota.md  (`case`, 6 assertions)

### content_page

```
---
title: "Birchfield v. North Dakota"
type: case
citation: "579 U.S. 438 (2016)"
parallel_cite: "195 L. Ed. 2d 560; 136 S. Ct. 2160"
neutral_cite: 2016 U.S. LEXIS 4058
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2016
date_decided: 2016-06-23
docket: 14-1468
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2016-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Birchfield v. North Dakota
  varies_by_point: false
  scope_note: "Good law. Refines the Schmerber/McNeely DUI-testing line: breath tests are valid as a search incident to arrest, blood tests are not; States may not criminalize refusal of a warrantless blood test."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/"
  cluster_id: 3216497
  opinion_id: 3216391
  identity_checked: true
homes:
  - page: "[[SIA Alcohol Tests]]"
    role: "Key — Anchor"
  - page: "[[Destruction of Evidence]]"
    role: "Related (blood draw needs exigency or warrant)"
related: ["[[Schmerber v. California]]", "[[Missouri v. McNeely]]", "[[Riley v. California]]", "[[Maryland v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "dui", "blood-draw", "breath-test", "implied-consent"]
holding: "A breath test may be administered as a search incident to a DUI arrest without a warrant, but a blood test may not be justified as a search incident to arrest (it needs a warrant or exigency); and a State may not impose criminal penalties for refusing a warrantless blood test."
lake:
  record_id: Birchfield v. North Dakota
  status: verified
  projected_at: 2026-07-06
---

# Birchfield v. North Dakota

*579 U.S. 438 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Three consolidated DUI cases tested States' implied-consent laws that attach consequences to refusing a chemical test. Danny Birchfield was criminally prosecuted under North Dakota law for refusing a warrantless **blood** test after a drunk-driving arrest. William Bernard was prosecuted for refusing a warrantless **breath** test in Minnesota. Steve Beylund submitted to a **blood** test after being told that refusal was a crime. Each argued that criminalizing or coercing submission to a warrantless test violated the Fourth Amendment.

## Issue
Whether the Fourth Amendment permits warrantless breath and blood tests incident to an arrest for drunk driving, and whether a State may impose criminal penalties on a motorist's refusal to submit to such a warrantless test.

## Rule
The intrusiveness of the test controls. "Because breath tests are significantly less intrusive than blood tests and in most cases amply serve law enforcement interests, we conclude that a breath test, but not a blood test, may be administered as a search incident to a lawful arrest for drunk driving." — 136 S. Ct. at 2185. ^pin-2185

A State may not criminalize refusal of the more intrusive (blood) test: "It is another matter, however, for a State not only to insist upon an intrusive blood test, but also to impose criminal penalties on the refusal to submit to such a test. There must be a limit to the consequences to which motorists may be deemed to have consented by virtue of a decision to drive on public roads." — *Id.* at 2185–2186. ^pin-2185a

## Application
Because a warrantless blood test cannot be justified as a [[Search Incident to Arrest|search incident to arrest]], Birchfield could not be criminally punished for refusing one, and implied consent could not be stretched to support that criminal penalty — his conviction was reversed. Bernard's refusal was of a **breath** test, which is a valid search incident to a DUI arrest, so Minnesota could criminalize his refusal — that judgment was affirmed. Beylund had submitted to a blood test under the partly inaccurate advice that refusal was itself a crime, so his case was [[Reading and Citing Cases#on-remand|remanded]] to reassess the voluntariness of his consent in light of the correct legal rule.

## Conclusion
Warrantless breath tests are permissible as searches incident to a DUI arrest; warrantless blood tests are not (absent a warrant or [[Exigent Circumstances and Hot Pursuit|exigency]]); and a State cannot impose criminal penalties for refusing a warrantless blood test. *Birchfield* refines the bodily-intrusion line of [[Schmerber v. California]] and [[Missouri v. McNeely]] for the specific context of DUI chemical testing.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Birchfield* is good law and itself refines [[Schmerber v. California]] and [[Missouri v. McNeely]]; it draws the controlling breath-vs-blood line for searches incident to a drunk-driving arrest.

## Appears on
- [[SIA Alcohol Tests]] — *Key — Anchor*
- [[Exigent Circumstances and Hot Pursuit]] — *Related (cross-doctrine)*

## Sources
- *Birchfield v. North Dakota*, 579 U.S. 438 (2016) (136 S. Ct. 2160) — https://www.courtlistener.com/opinion/3216497/birchfield-v-north-dakota/ — pinpoints: 136 S. Ct. 2185–2186. (CourtListener copy carries S. Ct. pagination.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a96fdeacb3164985", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "579 U.S. 438 (2016)", "court": "U.S. Supreme Court", "neutral_cite": "2016 U.S. LEXIS 4058", "official_citation_present": true, "parallel_cite": "195 L. Ed. 2d 560; 136 S. Ct. 2160", "title": "Birchfield v. North Dakota", "year": "2016"}}
{"assertion_id": "1740fd36b37e69f6", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Related (blood draw needs exigency or warrant)", "title": "Birchfield v. North Dakota"}}
{"assertion_id": "30a8bd37378a9389", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Alcohol Tests"}, "payload": {"home": "SIA Alcohol Tests", "role": "Key — Anchor", "title": "Birchfield v. North Dakota"}}
{"assertion_id": "d6c4822f0687b867", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A breath test may be administered as a search incident to a DUI arrest without a warrant, but a blood test may not be justified as a search incident to arrest (it needs a warrant or exigency); and a State may not impose criminal penalties for refusing a warrantless blood test.", "title": "Birchfield v. North Dakota"}}
{"assertion_id": "142110efcd617715", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2016-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Birchfield v. North Dakota", "field_i_validity": "good_law", "scope_note": "Good law. Refines the Schmerber/McNeely DUI-testing line: breath tests are valid as a search incident to arrest, blood tests are not; States may not criminalize refusal of a warrantless blood test.", "title": "Birchfield v. North Dakota", "varies_by_point": "false"}}
{"assertion_id": "d1828c74a1df62b6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Birchfield v. North Dakota"}}
```

### lake record — Birchfield v. North Dakota

```json
{
  "schema_version": "s2.v1",
  "record_id": "Birchfield v. North Dakota",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Birchfield v. N. Dakota. William Robert Bernard",
    "case_name_short": "Birchfield",
    "case_name_full": "Danny BIRCHFIELD, Petitioner v. NORTH DAKOTA. William Robert Bernard, Jr., Petitioner v. Minnesota. and Steve Michael Beylund, Petitioner v. Grant Levi, Director, North Dakota Department of Transportation.",
    "input_case_name": "Birchfield v. North Dakota",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2016-06-23",
    "year": 2016,
    "docket": "14-1468",
    "cluster_id": 3216497,
    "lead_opinion_id": 3216391,
    "sibling_ids": [
      3216391
    ],
    "absolute_url": "/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8424452,
        "score": 20,
        "case_name": "Birchfield v. Dakota"
      },
      {
        "cluster_id": 8423610,
        "score": 20,
        "case_name": "Birchfield v. Dakota"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "579 U.S. 438",
      "volume": "579",
      "reporter": "U.S.",
      "page": "438",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "195 L. Ed. 2d 560",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2160",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2160",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. LEXIS 4058",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "4058",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "579 U.S. 438",
        "volume": "579",
        "reporter": "U.S.",
        "page": "438",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "195 L. Ed. 2d 560",
        "volume": "195",
        "reporter": "L. Ed. 2d",
        "page": "560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. LEXIS 4058",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "4058",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 2160",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "2160",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "579 U.S. 438",
    "official_selection": {
      "court_class": "scotus",
      "selected": "579 U.S. 438",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2185",
      "page": null,
      "quote": "--- # Birchfield v. North Dakota *579 U.S. 438 (2016)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three consolidated DUI cases tested States' implied-consent laws that attach consequences to refusing a chemical test. Danny Birchfield was criminally prosecuted under North Dakota law for refusing a warrantless **blood** test after a drunk-driving arrest. William Bernard was prosecuted for refusing a warrantless **breath** test in Minnesota. Steve Beylund submitted to a **blood** test after being told that refusal was a crime. Each argued that criminalizing or coercing submission to a warrantless test violated the Fourth Amendment. ## Issue Whether the Fourth Amendment permits warrantless breath and blood tests incident to an arrest for drunk driving, and whether a State may impose criminal penalties on a motorist's refusal to submit to such a warrantless test. ## Rule The intrusiveness of the test controls.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-2185a",
      "page": null,
      "quote": "It is another matter, however, for a State not only to insist upon an intrusive blood test, but also to impose criminal penalties on the refusal to submit to such a test. There must be a limit to the consequences to which motorists may be deemed to have consented by virtue of a decision to drive on public roads.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Birchfield v. North Dakota",
    "varies_by_point": false,
    "scope_note": "Good law. Refines the Schmerber/McNeely DUI-testing line: breath tests are valid as a search incident to arrest, blood tests are not; States may not criminalize refusal of a warrantless blood test.",
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
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
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
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
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
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phipps",
          "cluster_id": 9440775,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kruse",
          "cluster_id": 4643214,
          "cite": [
            "303 Neb. 799",
            "931 N.W.2d 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Banks",
          "cluster_id": 6658146,
          "cite": [
            "434 P.3d 361",
            "364 Or. 332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hatfield",
          "cluster_id": 4505365,
          "cite": [
            "300 Neb. 152",
            "912 N.W.2d 731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cosino v. State",
          "cluster_id": 5447462,
          "cite": [
            "503 S.W.3d 592",
            "2016 Tex. App. LEXIS 11431",
            "2016 WL 6134461"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The Matter of Kevin B. Acevedo v. New York State Department of Motor Vehicles , The Matter of Michael W. Carney v. New York State Department of Motor Vehicles , The Matter of Caralyn A. Matsen v. New York State Department of Motor Vehicles",
          "cluster_id": 4390108,
          "cite": [
            "29 N.Y.3d 202",
            "77 N.E.3d 331"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hood",
          "cluster_id": 4541268,
          "cite": [
            "301 Neb. 207",
            "917 N.W.2d 880"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McCumber",
          "cluster_id": 4370918,
          "cite": [
            "295 Neb. 941",
            "893 N.W.2d 411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sloley v. VanBramer",
          "cluster_id": 4686314,
          "cite": [
            "945 F.3d 30"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Myers, D.",
          "cluster_id": 4410366,
          "cite": [
            "164 A.3d 1162",
            "2017 WL 3045867",
            "2017 Pa. LEXIS 1689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Corrin Kathleen Reynolds",
          "cluster_id": 4318256,
          "cite": [
            "504 S.W.3d 283",
            "2016 Tenn. LEXIS 821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schmidt",
          "cluster_id": 4330697,
          "cite": [
            "53 Kan. App. 2d 225",
            "385 P.3d 936",
            "2016 Kan. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pester",
          "cluster_id": 4312370,
          "cite": [
            "294 Neb. 995",
            "885 N.W.2d 713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
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
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McGinn",
          "cluster_id": 4623043,
          "cite": [
            "303 Neb. 224",
            "928 N.W.2d 391"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rothenberger",
          "cluster_id": 4259293,
          "cite": [
            "294 Neb. 810",
            "885 N.W.2d 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Glorianna Woodard",
          "cluster_id": 4428527,
          "cite": [
            "909 N.W.2d 299",
            "321 Mich. App. 377"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Delva",
          "cluster_id": 4396270,
          "cite": [
            "858 F.3d 135",
            "2017 WL 2366489",
            "2017 U.S. App. LEXIS 9645"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nielsen",
          "cluster_id": 4535193,
          "cite": [
            "301 Neb. 88",
            "917 N.W.2d 159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Hand, T.",
          "cluster_id": 10279074,
          "cite": [
            "2021 Pa. Super. 113",
            "252 A.3d 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 10048657,
          "cite": [
            "465 Md. 311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dawn M. Prado",
          "cluster_id": 4893130,
          "cite": [
            "960 N.W.2d 869",
            "2021 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wade Robertson v. Rise Pichon",
          "cluster_id": 4372525,
          "cite": [
            "849 F.3d 1173",
            "2017 WL 816886",
            "2017 U.S. App. LEXIS 3770"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roberto Pabon",
          "cluster_id": 4425184,
          "cite": [
            "871 F.3d 164",
            "2017 U.S. App. LEXIS 17471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cornwell",
          "cluster_id": 4257159,
          "cite": [
            "294 Neb. 799",
            "884 N.W.2d 722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Birchfield v. North Dakota:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3216391) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 177,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 177,
        "triage_read": 10,
        "triage_snippet_classified": 167
      },
      "lane2_top_cited": {
        "query": "cites:(3216391)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMSZzPTQ2ODkxNTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%283216391%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(3216391)",
        "reviewed": 58,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 58,
        "triage_read": 4,
        "triage_snippet_classified": 54
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(3216391)",
    "indexed_citing_opinions": 231,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3216391,
        "count": 231,
        "count_source": "search"
      }
    ],
    "citation_count": 1444,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/birchfield-v-north-dakota.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MDcwNzcmcz0xMDAxMzA0OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%283216391%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3216391,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 110126,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 111206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 134724,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 1180238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 1593988,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 1613688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 1845122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 1865553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 2770344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 2779207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 3836945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3216391,
        "cited_id": 4934771,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:01:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:01:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:05:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:01:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Birchfield v. North Dakota (truncated)

```
(Slip Opinion)              OCTOBER TERM, 2015                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                 BIRCHFIELD v. NORTH DAKOTA

   CERTIORARI TO THE SUPREME COURT OF NORTH DAKOTA

     No. 14–1468. Argued April 20, 2016—Decided June 23, 2016*
To fight the serious harms inflicted by drunk drivers, all States have
  laws that prohibit motorists from driving with a blood alcohol concen-
  tration (BAC) exceeding a specified level. BAC is typically deter-
  mined through a direct analysis of a blood sample or by using a ma-
  chine to measure the amount of alcohol in a person’s breath. To help
  secure drivers’ cooperation with such testing, the States have also
  enacted “implied consent” laws that require drivers to submit to BAC
  tests. Originally, the penalty for refusing a test was suspension of
  the motorist’s license. Over time, however, States have toughened
  their drunk-driving laws, imposing harsher penalties on recidivists
  and drivers with particularly high BAC levels. Because motorists
  who fear these increased punishments have strong incentives to re-
  ject testing, some States, including North Dakota and Minnesota,
  now make it a crime to refuse to undergo testing.
    In these cases, all three petitioners were arrested on drunk-driving
  charges. The state trooper who arrested petitioner Danny Birchfield
  advised him of his obligation under North Dakota law to undergo
  BAC testing and told him, as state law requires, that refusing to
  submit to a blood test could lead to criminal punishment. Birchfield
  refused to let his blood be drawn and was charged with a misde-
  meanor violation of the refusal statute. He entered a conditional
  guilty plea but argued that the Fourth Amendment prohibited crimi-
  nalizing his refusal to submit to the test. The State District Court re-
——————
  * Together with No. 14–1470, Bernard v. Minnesota, on certiorari to
the Supreme Court of Minnesota, and No. 14–1507, Beylund v. Levi,
Director, North Dakota Department of Transportation, also on certiorari
to the Supreme Court of North Dakota.
2                  BIRCHFIELD v. NORTH DAKOTA

                                 Syllabus

    jected his argument, and the State Supreme Court affirmed.
      After arresting petitioner William Robert Bernard, Jr., Minnesota
    police transported him to the station. There, officers read him Min-
    nesota’s implied consent advisory, which like North Dakota’s informs
    motorists that it is a crime to refuse to submit to a BAC test. Ber-
    nard refused to take a breath test and was charged with test refusal
    in the first degree. The Minnesota District Court dismissed the
    charges, concluding that the warrantless breath test was not permit-
    ted under the Fourth Amendment. The State Court of Appeals re-
    versed, and the State Supreme Court affirmed.
      The officer who arrested petitioner Steve Michael Beylund took
    him to a nearby hospital. The officer read him North Dakota’s im-
    plied consent advisory, informing him that test refusal in these cir-
    cumstances is itself a crime. Beylund agreed to have his blood
    drawn. The test revealed a BAC level more than three times the le-
    gal limit. Beylund’s license was suspended for two years after an
    administrative hearing, and on appeal, the State District Court re-
    jected his argument that his consent to the blood test was coerced by
    the officer’s warning. The State Supreme Court affirmed.
Held:
    1. The Fourth Amendment permits warrantless breath tests inci-
 dent to arrests for drunk driving but not warrantless blood tests.
 Pp. 13–36.
       (a) Taking a blood sample or administering a breath test is a
 search governed by the Fourth Amendment. See Skinner v. Railway
 Labor Executives’ Assn., 489 U. S. 602, 616–617; Schmerber v. Cali-
 fornia, 384 U. S. 757, 767–768. These searches may nevertheless be
 exempt from the warrant requirement if they fall within, as relevant
 here, the exception for searches conducted incident to a lawful arrest.
 This exception applies categorically, rather than on a case-by-case
 basis. Missouri v. McNeely, 569 U. S. ___, ___, n. 3. Pp. 14–16.
       (b) The search-incident-to-arrest doctrine has an ancient pedi-
 gree that predates the Nation’s founding, and no historical evidence
 suggests that the Fourth Amendment altered the permissible bounds
 of arrestee searches. The mere “fact of the lawful arrest” justifies “a
 full search of the person.” United States v. Robinson, 414 U. S. 218,
 235. The doctrine may also apply in situations that could not have
 been envisioned when the Fourth Amendment was adopted. In Riley
 v. California, 573 U. S. ___, the Court considered how to apply the
 doctrine to searches of an arrestee’s cell phone. Because founding era
 guidance was lacking, the Court determined “whether to exempt [the]
 search from the warrant requirement ‘by assessing, on the one hand,
 the degree to which it intrudes upon an individual’s privacy and, on
 the other, the degree to which it is needed for the promotion of legit-
                   Cite as: 579 U. S. ____ (2016)                     3

                              Syllabus

imate governmental interests.’ ” Id., at ___. The same mode of anal-
ysis is proper here because the founding era provides no definitive
guidance on whether blood and breath tests should be allowed inci-
dent to arrest. Pp. 16–20.
     (c) The analysis begins by considering the impact of breath and
blood tests on individual privacy interests. Pp. 20–23.
        (1) Breath tests do not “implicat[e] significant privacy con-
cerns.” Skinner, 489 U. S., at 626. The physical intrusion is almost
negligible. The tests “do not require piercing the skin” and entail “a
minimum of inconvenience.” Id., at 625. Requiring an arrestee to in-
sert the machine’s mouthpiece into his or her mouth and to exhale
“deep lung” air is no more intrusive than collecting a DNA sample by
rubbing a swab on the inside of a person’s cheek, Maryland v. King,
569 U. S. ___, ___, or scraping underneath a suspect’s fingernails,
Cupp v. Murphy, 412 U. S. 291. Breath tests, unlike DNA samples,
also yield only a BAC reading and leave no biological sample in the
government’s possession. Finally, participation in a breath test is not
likely to enhance the embarrassment inherent in any arrest. Pp. 20–
22.
        (2) The same cannot be said about blood tests. They “require
piercing the skin” and extract a part of the subject’s body, Skinner,
supra, at 625, and thus are significantly more intrusive than blowing
into a tube. A blood test also gives law enforcement a sample that
can be preserved and from which it is possible to extract information
beyond a simple BAC reading. That prospect could cause anxiety for
the person tested. Pp. 22–23.
     (d) The analysis next turns to the States’ asserted need to obtain
BAC readings. Pp. 23–33.
        (1) The States and the Federal Government have a “paramount
interest . . . in preserving [public highway] safety,” Mackey v.
Montrym, 443 U. S. 1, 17; and States have a compelling interest in
creating “deterrent[s] to drunken driving,” a leading cause of traffic
fatalities and injuries, id., at 18. Sanctions for refusing to take a
BAC test were increased because consequences like license suspen-
sion were no longer adequate to persuade the most dangerous offend-
ers to agree to a test that could lead to severe criminal sanctions. By
making it a crime to refuse to submit to a BAC test, the laws at issue
provide an incentive to cooperate and thus serve a very important
function. Pp. 23–25.
        (2) As for other ways to combat drunk driving, this Court’s de-
cisions establish that an arresting officer is not obligated to obtain a
warrant before conducting a search incident to arrest simply because
there might be adequate time in the particular circumstances to ob-
tain a warrant. The legality of a search incident to arrest must be
4                   BIRCHFIELD v. NORTH DAKOTA

                                  Syllabus

    judged on the basis of categorical rules. See e.g., Robinson, supra, at
    235. McNeely, supra, at ___, distinguished. Imposition of a warrant
    requirement for every BAC test would likely swamp courts, given the
    enormous number of drunk-driving arrests, with little corresponding
    benefit. And other alternatives—e.g., sobriety checkpoints and igni-
    tion interlock systems—are poor substitutes. Pp. 25–30.
             (3) Bernard argues that warrantless BAC testing cannot be
    justified as a search incident to arrest because that doctrine aims to
    prevent the arrestee from destroying evidence, while the loss of blood
    alcohol evidence results from the body’s metabolism of alcohol, a nat-
    ural process not controlled by the arrestee. In both instances, howev-
    er, the State is justifiably concerned that evidence may be lost. The
    State’s general interest in “evidence preservation” or avoiding “the
    loss of evidence,” Riley, supra, at ___, readily encompasses the me-
    tabolization of alcohol in the blood. Bernard’s view finds no support
    in Chimel v. California, 395 U. S. 752, 763, Schmerber, 384 U. S., at
    769, or McNeely, supra, at ___. Pp. 30–33.
          (e) Because the impact of breath tests on privacy is slight, and
    the need for BAC testing is great, the Fourth Amendment permits
    warrantless breath tests incident to arrests for drunk driving. Blood
    tests, however, are significantly more intrusive, and their reasona-
    bleness must be judged in light of the availability of the less invasive
    alternative of a breath test. Respondents have offered no satisfactory
    justification for demanding the more intrusive alternative without a
    warrant. In instances where blood tests might be preferable—e.g.,
    where substances other than alcohol impair the driver’s ability to op-
    erate a car safely, or where the subject is unconscious—nothing pre-
    vents the police from seeking a warrant or from relying on the exi-
    gent circumstances exception if it applies. Because breath tests are
    significantly less intrusive than blood tests and in most cases amply
    serve law enforcement interests, a breath test, but not a blood test,
    may be administered as a search incident to a lawful arrest for drunk
    driving. No warrant is needed in this situation. Pp. 33–35.
       2. Motorists may not be criminally punished for refusing to submit
    to a blood test based on legally implied consent to submit to them. It
    is one thing to approve implied-consent laws that impose civil penal-
    ties and evidentiary consequences on motorists who refuse to comply,
    but quite another for a State to insist upon an intrusive blood test
    and then to impose criminal penalties on refusal to submit. There
    must be a limit to the consequences to which motorists may be
    deemed to have consented by virtue of a decision to drive on public
    roads. Pp. 36–37.
       3. These legal conclusions resolve the three present cases. Birch-
    field was criminally prosecuted for refusing a warrantless blood
                     Cite as: 579 U. S. ____ (2016)                    5

                                Syllabus

  draw, and therefore the search that he refused cannot be justified as
  a search incident to his arrest or on the basis of implied consent. Be-
  cause there appears to be no other basis for a warrantless test of
  Birchfield’s blood, he was threatened with an unlawful search and
  unlawfully convicted for refusing that search. Bernard was criminal-
  ly prosecuted for refusing a warrantless breath test. Because that
  test was a permissible search incident to his arrest for drunk driving,
  the Fourth Amendment did not require officers to obtain a warrant
  prior to demanding the test, and Bernard had no right to refuse it.
  Beylund submitted to a blood test after police told him that the law
  required his submission. The North Dakota Supreme Court, which
  based its conclusion that Beylund’s consent was voluntary on the er-
  roneous assumption that the State could compel blood tests, should
  reevaluate Beylund’s consent in light of the partial inaccuracy of the
  officer’s advisory. Pp. 37–38.
No. 14–1468, 2015 ND 6, 858 N. W. 2d 302, reversed and remanded;
 No. 14–1470, 859 N. W. 2d 762, affirmed; No. 14–1507, 2015 ND 18,
 859 N. W. 2d 403, vacated and remanded.

   ALITO, J., delivered the opinion of the Court, in which ROBERTS, C. J,
and KENNEDY, BREYER, and KAGAN, JJ., joined. SOTOMAYOR, J., filed an
opinion concurring in part and dissenting in part, in which GINSBURG,
J., joined. THOMAS, J., filed an opinion concurring in the judgment in
part and dissenting in part.
                       Cite as: 579 U. S. ____ (2016)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash­
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                  Nos. 14–1468, 14–1470, and 14–1507
                                  _________________


            DANNY BIRCHFIELD, PETITIONER
14–1468                  v.
                   NORTH DAKOTA;
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                    NORTH DAKOTA




   WILLIAM ROBERT BERNARD, JR., PETITIONER
14–1470              v.
              MINNESOTA; AND
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      MINNESOTA




     STEVE MICHAEL BEYLUND, PETITIONER
14–1507               v.
     GRANT LEVI, DIRECTOR, NORTH DAKOTA
        DEPARTMENT OF TRANSPORTATION
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                    NORTH DAKOTA



                                [June 23, 2016]


  JUSTICE ALITO delivered the opinion of the Court.
  Drunk drivers take a grisly toll on the Nation’s roads,
claiming thousands of lives, injuring many more victims,
and inflicting billions of dollars in property damage every
2              BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

year. To fight this problem, all States have laws that
prohibit motorists from driving with a blood alcohol con­
centration (BAC) that exceeds a specified level. But de­
termining whether a driver’s BAC is over the legal limit
requires a test, and many drivers stopped on suspicion of
drunk driving would not submit to testing if given the
option. So every State also has long had what are termed
“implied consent laws.” These laws impose penalties on
motorists who refuse to undergo testing when there is
sufficient reason to believe they are violating the State’s
drunk-driving laws.
  In the past, the typical penalty for noncompliance was
suspension or revocation of the motorist’s license. The
cases now before us involve laws that go beyond that and
make it a crime for a motorist to refuse to be tested after
being lawfully arrested for driving while impaired. The
question presented is whether such laws violate the
Fourth Amendment’s prohibition against unreasonable
searches.
                               I
   The problem of drunk driving arose almost as soon as
motor vehicles came into use. See J. Jacobs, Drunk Driv­
ing: An American Dilemma 57 (1989) (Jacobs). New Jer­
sey enacted what was perhaps the Nation’s first drunk-
driving law in 1906, 1906 N. J. Laws pp. 186, 196, and
other States soon followed. These early laws made it
illegal to drive while intoxicated but did not provide a
statistical definition of intoxication. As a result, prosecu­
tors normally had to present testimony that the defendant
was showing outward signs of intoxication, like imbalance
or slurred speech. R. Donigan, Chemical Tests and the
Law 2 (1966) (Donigan). As one early case put it, “[t]he
effects resulting from the drinking of intoxicating liquors
are manifested in various ways, and before any one can be
shown to be under the influence of intoxicating liquor it is
                 Cite as: 579 U. S. ____ (2016)          3

                     Opinion of the Court

necessary for some witness to prove that some one or more
of these effects were perceptible to him.” State v. Noble,
119 Ore. 674, 677, 250 P. 833, 834 (1926).
   The 1930’s saw a continued rise in the number of motor
vehicles on the roads, an end to Prohibition, and not coin­
cidentally an increased interest in combating the growing
problem of drunk driving. Jones, Measuring Alcohol in
Blood and Breath for Forensic Purposes—A Historical
Review, 8 For. Sci. Rev. 13, 20, 33 (1996) (Jones). The
American Medical Association and the National Safety
Council set up committees to study the problem and ulti­
mately concluded that a driver with a BAC of 0.15% or
higher could be presumed to be inebriated. Donigan 21–
22. In 1939, Indiana enacted the first law that defined
presumptive intoxication based on BAC levels, using the
recommended 0.15% standard. 1939 Ind. Acts p. 309;
Jones 21. Other States soon followed and then, in re­
sponse to updated guidance from national organizations,
lowered the presumption to a BAC level of 0.10%. Don­
igan 22–23. Later, States moved away from mere pre­
sumptions that defendants might rebut, and adopted laws
providing that driving with a 0.10% BAC or higher was
per se illegal. Jacobs 69–70.
   Enforcement of laws of this type obviously requires the
measurement of BAC. One way of doing this is to analyze
a sample of a driver’s blood directly. A technician with
medical training uses a syringe to draw a blood sample
from the veins of the subject, who must remain still during
the procedure, and then the sample is shipped to a sepa­
rate laboratory for measurement of its alcohol concentra­
tion. See 2 R. Erwin, Defense of Drunk Driving Cases
§§17.03–17.04 (3d ed. 2015) (Erwin). Although it is possi­
ble for a subject to be forcibly immobilized so that a sam­
ple may be drawn, many States prohibit drawing blood
from a driver who resists since this practice helps “to
avoid violent confrontations.” South Dakota v. Neville,
4              BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

459 U. S. 553, 559 (1983).
   The most common and economical method of calculating
BAC is by means of a machine that measures the amount
of alcohol in a person’s breath. National Highway Traffic
Safety Admin. (NHTSA), E. Haire, W. Leaf, D. Preusser, &
M. Solomon, Use of Warrants to Reduce Breath Test Re­
fusals: Experiences from North Carolina 1 (No. 811461,
Apr. 2011). One such device, called the “Drunkometer,”
was invented and first sold in the 1930’s. Note, 30 N. C.
L. Rev. 302, 303, and n. 10 (1952). The test subject would
inflate a small balloon, and then the test analyst would
release this captured breath into the machine, which
forced it through a chemical solution that reacted to the
presence of alcohol by changing color. Id., at 303. The test
analyst could observe the amount of breath required to
produce the color change and calculate the subject’s breath
alcohol concentration and by extension, BAC, from this
figure. Id., at 303–304. A more practical machine, called
the “Breathalyzer,” came into common use beginning in
the 1950’s, relying on the same basic scientific principles.
3 Erwin §22.01, at 22–3; Jones 34.
   Over time, improved breath test machines were devel­
oped. Today, such devices can detect the presence of
alcohol more quickly and accurately than before, typically
using infrared technology rather than a chemical reaction.
2 Erwin §18A.01; Jones 36. And in practice all breath
testing machines used for evidentiary purposes must be
approved by the National Highway Traffic Safety Admin­
istration. See 1 H. Cohen & J. Green, Apprehending and
Prosecuting the Drunk Driver §7.04[7] (LexisNexis 2015).
These machines are generally regarded as very reliable
because the federal standards require that the devices
produce accurate and reproducible test results at a variety
of BAC levels, from the very low to the very high. 77 Fed.
Reg. 35747 (2012); 2 Erwin §18.07; Jones 38; see also
California v. Trombetta, 467 U. S. 479, 489 (1984).
                  Cite as: 579 U. S. ____ (2016)             5

                      Opinion of the Court

   Measurement of BAC based on a breath test requires
the cooperation of the person being tested. The subject
must take a deep breath and exhale through a mouthpiece
that connects to the machine. Berger, How Does it Work?
Alcohol Breath Testing, 325 British Medical J. 1403 (2002)
(Berger). Typically the test subject must blow air into the
device “ ‘for a period of several seconds’ ” to produce an
adequate breath sample, and the process is sometimes
repeated so that analysts can compare multiple samples to
ensure the device’s accuracy. Trombetta, supra, at 481;
see also 2 Erwin §21.04[2][b](L), at 21–14 (describing the
Intoxilyzer 4011 device as requiring a 12-second exhala­
tion, although the subject may take a new breath about
halfway through).
   Modern breath test machines are designed to capture
so-called “deep lung” or alveolar air. Trombetta, supra, at
481. Air from the alveolar region of the lungs provides the
best basis for determining the test subject’s BAC, for it is
in that part of the lungs that alcohol vapor and other
gases are exchanged between blood and breath. 2 Erwin
§18.01[2][a], at 18–7.
   When a standard infrared device is used, the whole
process takes only a few minutes from start to finish.
Berger 1403; 2 Erwin §18A.03[2], at 18A–14. Most evi­
dentiary breath tests do not occur next to the vehicle, at
the side of the road, but in a police station, where the
controlled environment is especially conducive to reliable
testing, or in some cases in the officer’s patrol vehicle or in
special mobile testing facilities. NHTSA, A. Berning et al.,
Refusal of Intoxication Testing: A Report to Congress 4,
and n. 5 (No. 811098, Sept. 2008).
   Because the cooperation of the test subject is necessary
when a breath test is administered and highly preferable
when a blood sample is taken, the enactment of laws
defining intoxication based on BAC made it necessary for
6                BIRCHFIELD v. NORTH DAKOTA

                        Opinion of the Court

States to find a way of securing such cooperation.1 So-
called “implied consent” laws were enacted to achieve this
result. They provided that cooperation with BAC testing
was a condition of the privilege of driving on state roads
and that the privilege would be rescinded if a suspected
drunk driver refused to honor that condition. Donigan
177. The first such law was enacted by New York in 1953,
and many other States followed suit not long thereafter.
Id., at 177–179. In 1962, the Uniform Vehicle Code also
included such a provision. Id., at 179. Today, “all 50
States have adopted implied consent laws that require
motorists, as a condition of operating a motor vehicle
within the State, to consent to BAC testing if they are
arrested or otherwise detained on suspicion of a drunk-
driving offense.” Missouri v. McNeely, 569 U. S. ___, ___
(2013) (plurality opinion) (slip op., at 18). Suspension or
revocation of the motorist’s driver’s license remains the
standard legal consequence of refusal. In addition, evi­
dence of the motorist’s refusal is admitted as evidence of
likely intoxication in a drunk-driving prosecution. See
ibid.
   In recent decades, the States and the Federal Govern­
ment have toughened drunk-driving laws, and those ef­
forts have corresponded to a dramatic decrease in alcohol-
related fatalities. As of the early 1980’s, the number of
annual fatalities averaged 25,000; by 2014, the most re­
cent year for which statistics are available, the number
had fallen to below 10,000. Presidential Commission on
Drunk Driving 1 (Nov. 1983); NHTSA, Traffic Safety
Facts, 2014 Data, Alcohol-Impaired Driving 2 (No. 812231,
Dec. 2015) (NHTSA, 2014 Alcohol-Impaired Driving). One

——————
    1 In
       addition, BAC may be determined by testing a subject’s urine,
which also requires the test subject’s cooperation. But urine tests
appear to be less common in drunk-driving cases than breath and blood
tests, and none of the cases before us involves one.
                 Cite as: 579 U. S. ____ (2016)           7

                     Opinion of the Court

legal change has been further lowering the BAC standard
from 0.10% to 0.08%. See 1 Erwin, §2.01[1], at 2–3 to 2–4.
In addition, many States now impose increased penalties
for recidivists and for drivers with a BAC level that ex­
ceeds a higher threshold. In North Dakota, for example,
the standard penalty for first-time drunk-driving offenders
is license suspension and a fine. N. D. Cent. Code Ann.
§39–08–01(5)(a)(1) (Supp. 2015); §39–20–04.1(1). But an
offender with a BAC of 0.16% or higher must spend at
least two days in jail. §39–08–01(5)(a)(2). In addition, the
State imposes increased mandatory minimum sentences
for drunk-driving recidivists. §§39–08–01(5)(b)–(d).
   Many other States have taken a similar approach, but
this new structure threatened to undermine the effective­
ness of implied consent laws. If the penalty for driving
with a greatly elevated BAC or for repeat violations ex­
ceeds the penalty for refusing to submit to testing, motor­
ists who fear conviction for the more severely punished
offenses have an incentive to reject testing. And in some
States, the refusal rate is high. On average, over one-fifth
of all drivers asked to submit to BAC testing in 2011
refused to do so. NHTSA, E. Namuswe, H. Coleman, & A.
Berning, Breath Test Refusal Rates in the United States—
2011 Update 1 (No. 811881, Mar. 2014). In North Dakota,
the refusal rate for 2011 was a representative 21%. Id.,
at 2. Minnesota’s was below average, at 12%. Ibid.
   To combat the problem of test refusal, some States have
begun to enact laws making it a crime to refuse to undergo
testing. Minnesota has taken this approach for decades.
See 1989 Minn. Laws p. 1658; 1992 Minn. Laws p. 1947.
And that may partly explain why its refusal rate now is
below the national average. Minnesota’s rate is also half
the 24% rate reported for 1988, the year before its first
criminal refusal law took effect. See Ross, Simon, Cleary,
Lewis, & Storkamp, Causes and Consequences of Implied
Consent Refusal, 11 Alcohol, Drugs and Driving 57, 69
8               BIRCHFIELD v. NORTH DAKOTA

                       Opinion of the Court

(1995). North Dakota adopted a similar law, in 2013, after
a pair of drunk-driving accidents claimed the lives of an
entire young family and another family’s 5- and 9-year-old
boys.2 2013 N. D. Laws pp. 1087–1088 (codified at §§39–
08–01(1)–(3)). The Federal Government also encourages
this approach as a means for overcoming the incentive
that drunk drivers have to refuse a test. NHTSA, Refusal
of Intoxication Testing, at 20.
                             II

                             A

   Petitioner Danny Birchfield accidentally drove his car
off a North Dakota highway on October 10, 2013. A state
trooper arrived and watched as Birchfield unsuccessfully
tried to drive back out of the ditch in which his car was
stuck. The trooper approached, caught a strong whiff of
alcohol, and saw that Birchfield’s eyes were bloodshot and
watery. Birchfield spoke in slurred speech and struggled
to stay steady on his feet. At the trooper’s request, Birch-
field agreed to take several field sobriety tests and per­
formed poorly on each. He had trouble reciting sections of
the alphabet and counting backwards in compliance with
the trooper’s directions.
   Believing that Birchfield was intoxicated, the trooper
informed him of his obligation under state law to agree to
a BAC test. Birchfield consented to a roadside breath test.
The device used for this sort of test often differs from the
machines used for breath tests administered in a police
station and is intended to provide a preliminary assess­
ment of the driver’s BAC. See, e.g., Berger 1403. Because
the reliability of these preliminary or screening breath
——————
  2 See Smith, Moving From Grief to Action: Two Families Push for

Stronger DUI Laws in N. D., Bismarck Tribune, Feb. 2, 2013, p. 1A;
Haga, Some Kind of Peace: Parents of Two Young Boys Killed in
Campground Accident Urge for Tougher DUI Penalties in N. D., Grand
Forks Herald, Jan. 15, 2013, pp. A1–A2.
                 Cite as: 579 U. S. ____ (2016)            9

                     Opinion of the Court

tests varies, many jurisdictions do not permit their numer­
ical results to be admitted in a drunk-driving trial as
evidence of a driver’s BAC. See generally 3 Erwin
§24.03[1]. In North Dakota, results from this type of test
are “used only for determining whether or not a further
test shall be given.” N. D. Cent. Code Ann. §39–20–14(3).
In Birchfield’s case, the screening test estimated that his
BAC was 0.254%, more than three times the legal limit of
0.08%. See §39–08–01(1)(a).
   The state trooper arrested Birchfield for driving while
impaired, gave the usual Miranda warnings, again ad­
vised him of his obligation under North Dakota law to
undergo BAC testing, and informed him, as state law
requires, see §39–20–01(3)(a), that refusing to take the
test would expose him to criminal penalties. In addition to
mandatory addiction treatment, sentences range from a
mandatory fine of $500 (for first-time offenders) to fines of
at least $2,000 and imprisonment of at least one year and
one day (for serial offenders). §39–08–01(5). These crimi­
nal penalties apply to blood, breath, and urine test refus­
als alike. See §§39–08–01(2), 39–20–01, 39–20–14.
   Although faced with the prospect of prosecution under
this law, Birchfield refused to let his blood be drawn. Just
three months before, Birchfield had received a citation for
driving under the influence, and he ultimately pleaded
guilty to that offense. State v. Birchfield, Crim. No. 30–
2013–CR–00720 (Dist. Ct. Morton Cty., N. D., Jan. 27,
2014). This time he also pleaded guilty—to a misde-
meanor violation of the refusal statute—but his plea was
a conditional one: while Birchfield admitted refusing the
blood test, he argued that the Fourth Amendment prohib­
ited criminalizing his refusal to submit to the test. The
State District Court rejected this argument and imposed a
sentence that accounted for his prior conviction. Cf. §39–
08–01(5)(b). The sentence included 30 days in jail (20 of
which were suspended and 10 of which had already been
10             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

served), 1 year of unsupervised probation, $1,750 in fine
and fees, and mandatory participation in a sobriety pro­
gram and in a substance abuse evaluation. App. to Pet.
for Cert. in No. 14–1468, p. 20a.
   On appeal, the North Dakota Supreme Court affirmed.
2015 ND 6, 858 N. W. 2d 302. The court found support for
the test refusal statute in this Court’s McNeely plurality
opinion, which had spoken favorably about “acceptable
‘legal tools’ with ‘significant consequences’ for refusing to
submit to testing.” 858 N. W. 2d, at 307 (quoting McNeely,
569 U. S., at ___ (slip op., at 18)).
                              B
  On August 5, 2012, Minnesota police received a report of
a problem at a South St. Paul boat launch. Three appar­
ently intoxicated men had gotten their truck stuck in the
river while attempting to pull their boat out of the water.
When police arrived, witnesses informed them that a man
in underwear had been driving the truck. That man
proved to be William Robert Bernard, Jr., petitioner in the
second of these cases. Bernard admitted that he had been
drinking but denied driving the truck (though he was
holding its keys) and refused to perform any field sobriety
tests. After noting that Bernard’s breath smelled of alco­
hol and that his eyes were bloodshot and watery, officers
arrested Bernard for driving while impaired.
  Back at the police station, officers read Bernard Minne­
sota’s implied consent advisory, which like North Dakota’s
informs motorists that it is a crime under state law to
refuse to submit to a legally required BAC test. See Minn.
Stat. §169A.51, subd. 2 (2014). Aside from noncriminal
penalties like license revocation, §169A.52, subd. 3, test
refusal in Minnesota can result in criminal penalties
ranging from no more than 90 days’ imprisonment and up
to a $1,000 fine for a misdemeanor violation to seven
years’ imprisonment and a $14,000 fine for repeat offend­
                 Cite as: 579 U. S. ____ (2016)           11

                     Opinion of the Court

ers, §169A.03, subd. 12; §169A.20, subds. 2–3; §169A.24,
subd. 2; §169A.27, subd. 2.
  The officers asked Bernard to take a breath test. After
he refused, prosecutors charged him with test refusal in
the first degree because he had four prior impaired-driving
convictions. 859 N. W. 2d 762, 765, n. 1 (Minn. 2015) (case
below). First-degree refusal carries the highest maximum
penalties and a mandatory minimum 3-year prison sen­
tence. §169A.276, subd. 1.
  The Minnesota District Court dismissed the charges on
the ground that the warrantless breath test demanded of
Bernard was not permitted under the Fourth Amendment.
App. to Pet. for Cert. in No. 14–1470, pp. 48a, 59a. The
Minnesota Court of Appeals reversed, id., at 46a, and the
State Supreme Court affirmed that judgment. Based on
the longstanding doctrine that authorizes warrantless
searches incident to a lawful arrest, the high court con­
cluded that police did not need a warrant to insist on a
test of Bernard’s breath. 859 N. W. 2d, at 766–772. Two
justices dissented. Id., at 774–780 (opinion of Page and
Stras, JJ.).
                               C
  A police officer spotted our third petitioner, Steve Mi­
chael Beylund, driving the streets of Bowman, North
Dakota, on the night of August 10, 2013. The officer saw
Beylund try unsuccessfully to turn into a driveway. In the
process, Beylund’s car nearly hit a stop sign before coming
to a stop still partly on the public road. The officer walked
up to the car and saw that Beylund had an empty wine
glass in the center console next to him. Noticing that
Beylund also smelled of alcohol, the officer asked him to
step out of the car. As Beylund did so, he struggled to
keep his balance.
  The officer arrested Beylund for driving while impaired
and took him to a nearby hospital. There he read Beylund
12             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

North Dakota’s implied consent advisory, informing him
that test refusal in these circumstances is itself a crime.
See N. D. Cent. Code Ann. §39–20–01(3)(a). Unlike the
other two petitioners in these cases, Beylund agreed to
have his blood drawn and analyzed. A nurse took a blood
sample, which revealed a blood alcohol concentration of
0.250%, more than three times the legal limit.
   Given the test results, Beylund’s driver’s license was
suspended for two years after an administrative hearing.
Beylund appealed the hearing officer’s decision to a North
Dakota District Court, principally arguing that his con­
sent to the blood test was coerced by the officer’s warning
that refusing to consent would itself be a crime. The
District Court rejected this argument, and Beylund again
appealed.
   The North Dakota Supreme Court affirmed. In re­
sponse to Beylund’s argument that his consent was insuf­
ficiently voluntary because of the announced criminal
penalties for refusal, the court relied on the fact that its
then-recent Birchfield decision had upheld the constitu­
tionality of those penalties. 2015 ND 18, ¶¶14–15, 859
N. W. 2d 403, 408–409. The court also explained that it
had found consent offered by a similarly situated motorist
to be voluntary, State v. Smith, 2014 ND 152, 849 N. W.
2d 599. In that case, the court emphasized that North
Dakota’s implied consent advisory was not misleading
because it truthfully related the penalties for refusal. Id.,
at 606.
   We granted certiorari in all three cases and consolidated
them for argument, see 577 U. S. ___ (2015), in order to
decide whether motorists lawfully arrested for drunk
driving may be convicted of a crime or otherwise penalized
for refusing to take a warrantless test measuring the
alcohol in their bloodstream.
                 Cite as: 579 U. S. ____ (2016)           13

                     Opinion of the Court

                             III
  As our summary of the facts and proceedings in these
three cases reveals, the cases differ in some respects.
Petitioners Birchfield and Beylund were told that they
were obligated to submit to a blood test, whereas petitioner
Bernard was informed that a breath test was required.
Birchfield and Bernard each refused to undergo a test and
was convicted of a crime for his refusal. Beylund complied
with the demand for a blood sample, and his license was
then suspended in an administrative proceeding based on
test results that revealed a very high blood alcohol level.
  Despite these differences, success for all three petition­
ers depends on the proposition that the criminal law ordi­
narily may not compel a motorist to submit to the taking
of a blood sample or to a breath test unless a warrant
authorizing such testing is issued by a magistrate. If, on
the other hand, such warrantless searches comport with
the Fourth Amendment, it follows that a State may crimi­
nalize the refusal to comply with a demand to submit to
the required testing, just as a State may make it a crime
for a person to obstruct the execution of a valid search
warrant. See, e.g., Conn. Gen. Stat. §54–33d (2009); Fla.
Stat. §933.15 (2015); N. J. Stat. Ann. §33:1–63 (West
1994); 18 U. S. C. §1501; cf. Bumper v. North Carolina,
391 U. S. 543, 550 (1968) (“When a law enforcement officer
claims authority to search a home under a warrant, he
announces in effect that the occupant has no right to resist
the search”). And by the same token, if such warrantless
searches are constitutional, there is no obstacle under
federal law to the admission of the results that they yield
in either a criminal prosecution or a civil or administrative
proceeding. We therefore begin by considering whether
the searches demanded in these cases were consistent
with the Fourth Amendment.
14              BIRCHFIELD v. NORTH DAKOTA

                      Opinion of the Court

                           IV
     The Fourth Amendment provides:
        “The right of the people to be secure in their per­
      sons, houses, papers, and effects, against unreasona­
      ble searches and seizures, shall not be violated, and
      no Warrants shall issue, but upon probable cause,
      supported by Oath or affirmation, and particularly
      describing the place to be searched, and the persons or
      things to be seized.”
  The Amendment thus prohibits “unreasonable searches,”
and our cases establish that the taking of a blood sam-
ple or the administration of a breath test is a search.
See Skinner v. Railway Labor Executives’ Assn., 489 U. S.
602, 616–617 (1989); Schmerber v. California, 384 U. S.
757, 767–768 (1966). The question, then, is whether the
warrantless searches at issue here were reasonable. See
Vernonia School Dist. 47J v. Acton, 515 U. S. 646, 652
(1995) (“As the text of the Fourth Amendment indicates,
the ultimate measure of the constitutionality of a govern­
mental search is ‘reasonableness’ ”).
  “[T]he text of the Fourth Amendment does not specify
when a search warrant must be obtained.” Kentucky v.
King, 563 U. S. 452, 459 (2011); see also California v.
Acevedo, 500 U. S. 565, 581 (1991) (Scalia, J., concur-
ring in judgment) (“What [the text] explicitly states regard-
ing warrants is by way of limitation upon their issuance
rather than requirement of their use”). But “this Court has
inferred that a warrant must [usually] be secured.” King,
563 U. S., at 459. This usual requirement, however, is
subject to a number of exceptions. Ibid.
  We have previously had occasion to examine whether
one such exception—for “exigent circumstances”—applies
in drunk-driving investigations. The exigent circum-
stances exception allows a warrantless search when an
emergency leaves police insufficient time to seek a warrant.
                 Cite as: 579 U. S. ____ (2016)          15

                     Opinion of the Court

Michigan v. Tyler, 436 U. S. 499, 509 (1978). It permits,
for instance, the warrantless entry of private property
when there is a need to provide urgent aid to those inside,
when police are in hot pursuit of a fleeing suspect, and
when police fear the imminent destruction of evidence.
King, supra, at 460.
   In Schmerber v. California, we held that drunk driving
may present such an exigency. There, an officer directed
hospital personnel to take a blood sample from a driver
who was receiving treatment for car crash injuries. 384
U. S., at 758. The Court concluded that the officer “might
reasonably have believed that he was confronted with an
emergency” that left no time to seek a warrant because
“the percentage of alcohol in the blood begins to diminish
shortly after drinking stops.” Id., at 770. On the specific
facts of that case, where time had already been lost taking
the driver to the hospital and investigating the accident,
the Court found no Fourth Amendment violation even
though the warrantless blood draw took place over the
driver’s objection. Id., at 770–772.
   More recently, though, we have held that the natural
dissipation of alcohol from the bloodstream does not al-
ways constitute an exigency justifying the warrantless
taking of a blood sample. That was the holding of Mis-
souri v. McNeely, 569 U. S. ___, where the State of Mis­
souri was seeking a per se rule that “whenever an officer
has probable cause to believe an individual has been
driving under the influence of alcohol, exigent circum­
stances will necessarily exist because BAC evidence is
inherently evanescent.” Id., at ___ (opinion of the Court)
(slip op., at 8). We disagreed, emphasizing that Schmerber
had adopted a case-specific analysis depending on “all of
the facts and circumstances of the particular case.” 569
U. S., at ___ (slip op., at 8). We refused to “depart from
careful case-by-case assessment of exigency and adopt the
categorical rule proposed by the State.” Id., at ___ (slip
16              BIRCHFIELD v. NORTH DAKOTA

                      Opinion of the Court

op., at 9).
   While emphasizing that the exigent-circumstances
exception must be applied on a case-by-case basis, the
McNeely Court noted that other exceptions to the warrant
requirement “apply categorically” rather than in a “case-
specific” fashion. Id., at ___, n. 3 (slip op., at 7, n. 3). One
of these, as the McNeely opinion recognized, is the long-
established rule that a warrantless search may be con­
ducted incident to a lawful arrest. See ibid. But the
Court pointedly did not address any potential justification
for warrantless testing of drunk-driving suspects except
for the exception “at issue in th[e] case,” namely, the
exception for exigent circumstances. Id., at ___ (slip op.,
at 5). Neither did any of the Justices who wrote separately.
See id., at ___–___ (KENNEDY, J., concurring in part)
(slip op., at 1–2); id., at ___–___ (ROBERTS, C. J., concur­
ring in part and dissenting in part) (slip op., at 1–11); id.,
at ___–___ (THOMAS, J., dissenting) (slip op., at 1–8).
   In the three cases now before us, the drivers were
searched or told that they were required to submit to a
search after being placed under arrest for drunk driving.
We therefore consider how the search-incident-to-arrest
doctrine applies to breath and blood tests incident to such
arrests.
                            V

                            A

  The search-incident-to-arrest doctrine has an ancient
pedigree. Well before the Nation’s founding, it was recog­
nized that officers carrying out a lawful arrest had the
authority to make a warrantless search of the arrestee’s
person. An 18th-century manual for justices of the peace
provides a representative picture of usual practice shortly
before the Fourth Amendment’s adoption:
     “[A] thorough search of the felon is of the utmost con­
     sequence to your own safety, and the benefit of the
                 Cite as: 579 U. S. ____ (2016)          17

                     Opinion of the Court

    public, as by this means he will be deprived of in­
    struments of mischief, and evidence may probably be
    found on him sufficient to convict him, of which, if he
    has either time or opportunity allowed him, he will
    besure [sic] to find some means to get rid of.” The
    Conductor Generalis 117 (J. Parker ed. 1788) (reprint­
    ing S. Welch, Observations on the Office of Constable
    19 (1754)).
  One Fourth Amendment historian has observed that,
prior to American independence, “[a]nyone arrested could
expect that not only his surface clothing but his body,
luggage, and saddlebags would be searched and, perhaps,
his shoes, socks, and mouth as well.” W. Cuddihy, The
Fourth Amendment: Origins and Original Meaning: 602–
1791, p. 420 (2009).
  No historical evidence suggests that the Fourth
Amendment altered the permissible bounds of arrestee
searches. On the contrary, legal scholars agree that “the
legitimacy of body searches as an adjunct to the arrest
process had been thoroughly established in colonial times,
so much so that their constitutionality in 1789 can not be
doubted.” Id., at 752; see also T. Taylor, Two Studies in
Constitutional Interpretation 28–29, 39, 45 (1969); Stuntz,
The Substantive Origins of Criminal Procedure, 105 Yale
L. J. 393, 401 (1995).
  Few reported cases addressed the legality of such
searches before the 19th century, apparently because the
point was not much contested. In the 19th century, the
subject came up for discussion more often, but court deci­
sions and treatises alike confirmed the searches’ broad
acceptance. E.g., Holker v. Hennessey, 141 Mo. 527, 539–
540, 42 S. W. 1090, 1093 (1897); Ex parte Hurn, 92 Ala.
102, 112, 9 So. 515, 519 (1891); Thatcher v. Weeks, 79 Me.
547, 548–549, 11 A. 599 (1887); Reifsnyder v. Lee, 44 Iowa
101, 103 (1876); F. Wharton, Criminal Pleading and Prac­
18             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

tice §60, p. 45 (8th ed. 1880); 1 J. Bishop, Criminal Proce­
dure §211, p. 127 (2d ed. 1872).
   When this Court first addressed the question, we too
confirmed (albeit in dicta) “the right on the part of the
Government, always recognized under English and Ameri­
can law, to search the person of the accused when legally
arrested to discover and seize the fruits or evidence of
crime.” Weeks v. United States, 232 U. S. 383, 392 (1914).
The exception quickly became a fixture in our Fourth
Amendment case law. But in the decades that followed,
we grappled repeatedly with the question of the authority
of arresting officers to search the area surrounding the
arrestee, and our decisions reached results that were not
easy to reconcile. See, e.g., United States v. Lefkowitz, 285
U. S. 452, 464 (1932) (forbidding “unrestrained” search of
room where arrest was made); Harris v. United States, 331
U. S. 145, 149, 152 (1947) (permitting complete search of
arrestee’s four-room apartment); United States v. Rab-
inowitz, 339 U. S. 56, 60–65 (1950) (permitting complete
search of arrestee’s office).
   We attempted to clarify the law regarding searches
incident to arrest in Chimel v. California, 395 U. S. 752,
754 (1969), a case in which officers had searched the ar­
restee’s entire three-bedroom house. Chimel endorsed a
general rule that arresting officers, in order to prevent the
arrestee from obtaining a weapon or destroying evidence,
could search both “the person arrested” and “the area
‘within his immediate control.’ ” Id., at 763. “[N]o compa­
rable justification,” we said, supported “routinely search­
ing any room other than that in which an arrest occurs—
or, for that matter, for searching through all the desk
drawers or other closed or concealed areas in that room
itself.” Ibid.
   Four years later, in United States v. Robinson, 414 U. S.
218 (1973), we elaborated on Chimel’s meaning. We noted
that the search-incident-to-arrest rule actually comprises
                 Cite as: 579 U. S. ____ (2016)           19

                     Opinion of the Court

“two distinct propositions”: “The first is that a search may
be made of the person of the arrestee by virtue of the
lawful arrest. The second is that a search may be made of
the area within the control of the arrestee.” 414 U. S., at
224. After a thorough review of the relevant common law
history, we repudiated “case-by-case adjudication” of the
question whether an arresting officer had the authority to
carry out a search of the arrestee’s person. Id., at 235.
The permissibility of such searches, we held, does not
depend on whether a search of a particular arrestee is
likely to protect officer safety or evidence: “The authority
to search the person incident to a lawful custodial arrest,
while based upon the need to disarm and to discover evi­
dence, does not depend on what a court may later decide
was the probability in a particular arrest situation that
weapons or evidence would in fact be found upon the
person of the suspect.” Ibid. Instead, the mere “fact of the
lawful arrest” justifies “a full search of the person.” Ibid.
In Robinson itself, that meant that police had acted per­
missibly in searching inside a package of cigarettes found
on the man they arrested. Id., at 236.
   Our decision two Terms ago in Riley v. California, 573
U. S. ___ (2014), reaffirmed “Robinson’s categorical rule”
and explained how the rule should be applied in situations
that could not have been envisioned when the Fourth
Amendment was adopted. Id., at ___ (slip op., at 9). Riley
concerned a search of data contained in the memory of a
modern cell phone. “Absent more precise guidance from
the founding era,” the Court wrote, “we generally deter­
mine whether to exempt a given type of search from the
warrant requirement ‘by assessing, on the one hand, the
degree to which it intrudes upon an individual’s privacy
and, on the other, the degree to which it is needed for the
promotion of legitimate governmental interests.’ ” Ibid.
   Blood and breath tests to measure blood alcohol concen­
tration are not as new as searches of cell phones, but here,
20                BIRCHFIELD v. NORTH DAKOTA

                         Opinion of the Court

as in Riley, the founding era does not provide any defini­
tive guidance as to whether they should be allowed inci­
dent to arrest.3 Lacking such guidance, we engage in the
same mode of analysis as in Riley: we examine “the degree
to which [they] intrud[e] upon an individual’s privacy and
. . . the degree to which [they are] needed for the promo­
tion of legitimate governmental interests.’ ” Ibid.
                            B
  We begin by considering the impact of breath and blood
tests on individual privacy interests, and we will discuss
each type of test in turn.
                               1
  Years ago we said that breath tests do not “implicat[e]
significant privacy concerns.” Skinner, 489 U. S., at 626.
That remains so today.
  First, the physical intrusion is almost negligible.
Breath tests “do not require piercing the skin” and entail
“a minimum of inconvenience.” Id., at 625. As Minnesota
describes its version of the breath test, the process re­
quires the arrestee to blow continuously for 4 to 15 sec­
onds into a straw-like mouthpiece that is connected by a
tube to the test machine. Brief for Respondent in No. 14–
1470, p. 20. Independent sources describe other breath
test devices in essentially the same terms. See supra, at 5.
The effort is no more demanding than blowing up a party
balloon.
  Petitioner Bernard argues, however, that the process is
nevertheless a significant intrusion because the arrestee
must insert the mouthpiece of the machine into his or her
——————
   3 At most, there may be evidence that an arrestee’s mouth could be

searched in appropriate circumstances at the time of the founding. See
W. Cuddihy, Fourth Amendment: Origins and Original Meaning: 602–
1791, p. 420 (2009). Still, searching a mouth for weapons or contraband
is not the same as requiring an arrestee to give up breath or blood.
                 Cite as: 579 U. S. ____ (2016)           21

                     Opinion of the Court

mouth. Reply Brief in No. 14–1470, p. 9. But there is
nothing painful or strange about this requirement. The
use of a straw to drink beverages is a common practice
and one to which few object.
   Nor, contrary to Bernard, is the test a significant intru­
sion because it “does not capture an ordinary exhalation of
the kind that routinely is exposed to the public” but in­
stead “ ‘requires a sample of “alveolar” (deep lung) air.’ ”
Brief for Petitioner in No. 14–1470, p. 24. Humans have
never been known to assert a possessory interest in or any
emotional attachment to any of the air in their lungs. The
air that humans exhale is not part of their bodies. Exha­
lation is a natural process—indeed, one that is necessary
for life. Humans cannot hold their breath for more than a
few minutes, and all the air that is breathed into a breath
analyzing machine, including deep lung air, sooner or
later would be exhaled even without the test. See gener-
ally J. Hall, Guyton and Hall Textbook of Medical Physiol­
ogy 519–520 (13th ed. 2016).
   In prior cases, we have upheld warrantless searches
involving physical intrusions that were at least as signifi­
cant as that entailed in the administration of a breath
test. Just recently we described the process of collecting a
DNA sample by rubbing a swab on the inside of a person’s
cheek as a “negligible” intrusion. Maryland v. King, 569
U. S. ___, ___ (2013) (slip op., at 8). We have also upheld
scraping underneath a suspect’s fingernails to find evi­
dence of a crime, calling that a “very limited intrusion.”
Cupp v. Murphy, 412 U. S. 291, 296 (1973). A breath test
is no more intrusive than either of these procedures.
   Second, breath tests are capable of revealing only one
bit of information, the amount of alcohol in the subject’s
breath. In this respect, they contrast sharply with the
sample of cells collected by the swab in Maryland v. King.
Although the DNA obtained under the law at issue in that
case could lawfully be used only for identification pur-
22              BIRCHFIELD v. NORTH DAKOTA

                      Opinion of the Court

poses, 569 U. S., at ___ (slip op., at 5), the process put into
the possession of law enforcement authorities a sample from
which a wealth of additional, highly personal information
could potentially be obtained. A breath test, by contrast,
results in a BAC reading on a machine, nothing more. No
sample of anything is left in the possession of the police.
  Finally, participation in a breath test is not an experi­
ence that is likely to cause any great enhancement in the
embarrassment that is inherent in any arrest. See Skin-
ner, supra, at 625 (breath test involves “a minimum of . . .
embarrassment”). The act of blowing into a straw is not
inherently embarrassing, nor are evidentiary breath tests
administered in a manner that causes embarrassment.
Again, such tests are normally administered in private at
a police station, in a patrol car, or in a mobile testing
facility, out of public view. See supra, at 5. Moreover,
once placed under arrest, the individual’s expectation of
privacy is necessarily diminished. Maryland v. King,
supra, at ___–___ (slip op., at 24–25).
  For all these reasons, we reiterate what we said in
Skinner: A breath test does not “implicat[e] significant
privacy concerns.” 489 U. S., at 626.
                               2
  Blood tests are a different matter. They “require pierc­
ing the skin” and extract a part of the subject’s body.
Skinner, supra, at 625; see also McNeely, 569 U. S., at ___
(opinion of the Court) (slip op., at 4) (blood draws are “a
compelled physical intrusion beneath [the defendant’s]
skin and into his veins”); id., at ___ (opinion of ROBERTS,
C. J.) (slip op., at 9) (blood draws are “significant bodily
intrusions”). And while humans exhale air from their
lungs many times per minute, humans do not continually
shed blood. It is true, of course, that people voluntarily
submit to the taking of blood samples as part of a physical
examination, and the process involves little pain or risk.
                 Cite as: 579 U. S. ____ (2016)           23

                     Opinion of the Court

See id., at ___ (plurality opinion) (slip op., at 16) (citing
Schmerber, 384 U. S., at 771). Nevertheless, for many, the
process is not one they relish. It is significantly more
intrusive than blowing into a tube. Perhaps that is why
many States’ implied consent laws, including Minnesota’s,
specifically prescribe that breath tests be administered in
the usual drunk-driving case instead of blood tests or give
motorists a measure of choice over which test to take. See
1 Erwin §4.06; Minn. Stat. §169A.51, subd. 3.
  In addition, a blood test, unlike a breath test, places in
the hands of law enforcement authorities a sample that
can be preserved and from which it is possible to extract
information beyond a simple BAC reading. Even if the
law enforcement agency is precluded from testing the
blood for any purpose other than to measure BAC, the
potential remains and may result in anxiety for the person
tested.
                           C
  Having assessed the impact of breath and blood testing
on privacy interests, we now look to the States’ asserted
need to obtain BAC readings for persons arrested for
drunk driving.
                              1
   The States and the Federal Government have a “para­
mount interest . . . in preserving the safety of . . . public
highways.” Mackey v. Montrym, 443 U. S. 1, 17 (1979).
Although the number of deaths and injuries caused by
motor vehicle accidents has declined over the years, the
statistics are still staggering. See, e.g., NHTSA, Traffic
Safety Facts 1995—Overview 2 (No. 95F7, 1995) (47,087
fatalities, 3,416,000 injuries in 1988); NHTSA, Traffic
Safety Facts, 2014 Data, Summary of Motor Vehicle
Crashes 1 (No. 812263, May 2016) (Table 1) (29,989 fatali­
ties, 1,648,000 injuries in 2014).
24             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

   Alcohol consumption is a leading cause of traffic fatali­
ties and injuries. During the past decade, annual fatali­
ties in drunk-driving accidents ranged from 13,582 deaths
in 2005 to 9,865 deaths in 2011. NHTSA, 2014 Alcohol-
Impaired Driving 2. The most recent data report a total of
9,967 such fatalities in 2014—on average, one death every
53 minutes. Id., at 1. Our cases have long recognized the
“carnage” and “slaughter” caused by drunk drivers. Ne-
ville, 459 U. S., at 558; Breithaupt v. Abram, 352 U. S.
432, 439 (1957).
   JUSTICE SOTOMAYOR’s partial dissent suggests that
States’ interests in fighting drunk driving are satisfied
once suspected drunk drivers are arrested, since such
arrests take intoxicated drivers off the roads where they
might do harm. See post, at 9 (opinion concurring in part
and dissenting in part). But of course States are not solely
concerned with neutralizing the threat posed by a drunk
driver who has already gotten behind the wheel. They
also have a compelling interest in creating effective “de­
terrent[s] to drunken driving” so such individuals make
responsible decisions and do not become a threat to others
in the first place. Mackey, supra, at 18.
   To deter potential drunk drivers and thereby reduce
alcohol-related injuries, the States and the Federal Gov­
ernment have taken the series of steps that we recounted
earlier. See supra, at 2–8. We briefly recapitulate. After
pegging inebriation to a specific level of blood alcohol,
States passed implied consent laws to induce motorists to
submit to BAC testing. While these laws originally pro­
vided that refusal to submit could result in the loss of the
privilege of driving and the use of evidence of refusal in a
drunk-driving prosecution, more recently States and the
Federal Government have concluded that these conse­
quences are insufficient. In particular, license suspension
alone is unlikely to persuade the most dangerous offend­
ers, such as those who drive with a BAC significantly
                 Cite as: 579 U. S. ____ (2016)          25

                     Opinion of the Court

above the current limit of 0.08% and recidivists, to agree
to a test that would lead to severe criminal sanctions.
NHTSA, Implied Consent Refusal Impact, pp. xvii, 83 (No.
807765, Sept. 1991); NHTSA, Use of Warrants for Breath
Test Refusal 1 (No. 810852, Oct. 2007). The laws at issue
in the present cases—which make it a crime to refuse to
submit to a BAC test—are designed to provide an incen­
tive to cooperate in such cases, and we conclude that they
serve a very important function.
                              2
  Petitioners and JUSTICE SOTOMAYOR contend that the
States and the Federal Government could combat drunk
driving in other ways that do not have the same impact on
personal privacy. Their arguments are unconvincing.
  The chief argument on this score is that an officer mak­
ing an arrest for drunk driving should not be allowed to
administer a BAC test unless the officer procures a search
warrant or could not do so in time to obtain usable test
results. The governmental interest in warrantless breath
testing, JUSTICE SOTOMAYOR claims, turns on “ ‘whether
the burden of obtaining a warrant is likely to frustrate the
governmental purpose behind the search.’ ” Post, at 3–4
(quoting Camara v. Municipal Court of City and County of
San Francisco, 387 U. S. 523, 533 (1967)).
  This argument contravenes our decisions holding that
the legality of a search incident to arrest must be judged
on the basis of categorical rules. In Robinson, for example,
no one claimed that the object of the search, a package of
cigarettes, presented any danger to the arresting officer or
was at risk of being destroyed in the time that it would
have taken to secure a search warrant. The Court never­
theless upheld the constitutionality of a warrantless
search of the package, concluding that a categorical rule
was needed to give police adequate guidance: “A police
officer’s determination as to how and where to search the
26             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

person of a suspect whom he has arrested is necessarily a
quick ad hoc judgment which the Fourth Amendment does
not require to be broken down in each instance into an
analysis of each step in the search.” 414 U. S., at 235; cf.
Riley, 573 U. S., at ___ (slip op., at 22) (“If police are to
have workable rules, the balancing of the competing inter­
ests must in large part be done on a categorical basis—not
in an ad hoc, case-by-case fashion by individual police
officers” (brackets, ellipsis, and internal quotation marks
omitted)).
  It is not surprising, then, that the language JUSTICE
SOTOMAYOR quotes to justify her approach comes not from
our search-incident-to-arrest case law, but a case that
addressed routine home searches for possible housing code
violations. See Camara, 387 U. S., at 526. Camara’s
express concern in the passage that the dissent quotes was
“whether the public interest demands creation of a general
exception to the Fourth Amendment’s warrant require­
ment.” Id., at 533 (emphasis added). Camara did not
explain how to apply an existing exception, let alone the
long-established exception for searches incident to a lawful
arrest, whose applicability, as Robinson and Riley make
plain, has never turned on case-specific variables such as
how quickly the officer will be able to obtain a warrant in
the particular circumstances he faces.
  In advocating the case-by-case approach, petitioners and
JUSTICE SOTOMAYOR cite language in our McNeely opin­
ion. See Brief for Petitioner in No. 14–1468, p. 14; post, at
12. But McNeely concerned an exception to the warrant
requirement—for exigent circumstances—that always
requires case-by-case determinations. That was the basis
for our decision in that case. 569 U. S., at ___ (slip op.,
at 9). Although JUSTICE SOTOMAYOR contends that the
categorical search-incident-to-arrest doctrine and case-by­
case exigent circumstances doctrine are actually parts of a
single framework, post, at 6–7, and n. 3, in McNeely the
                 Cite as: 579 U. S. ____ (2016)           27

                     Opinion of the Court

Court was careful to note that the decision did not address
any other exceptions to the warrant requirement, 569
U. S., at ___, n. 3 (slip op., at 7, n. 3).
   Petitioners and JUSTICE SOTOMAYOR next suggest that
requiring a warrant for BAC testing in every case in which
a motorist is arrested for drunk driving would not impose
any great burden on the police or the courts. But of course
the same argument could be made about searching
through objects found on the arrestee’s possession, which
our cases permit even in the absence of a warrant. What
about the cigarette package in Robinson? What if a motor­
ist arrested for drunk driving has a flask in his pocket?
What if a motorist arrested for driving while under the
influence of marijuana has what appears to be a mari-
juana cigarette on his person? What about an unmarked
bottle of pills?
   If a search warrant were required for every search
incident to arrest that does not involve exigent circum­
stances, the courts would be swamped. And even if we
arbitrarily singled out BAC tests incident to arrest for this
special treatment, as it appears the dissent would do, see
post, at 12–14, the impact on the courts would be consid­
erable. The number of arrests every year for driving
under the influence is enormous—more than 1.1 million in
2014. FBI, Uniform Crime Report, Crime in the United
States, 2014, Arrests 2 (Fall 2015). Particularly in sparsely
populated areas, it would be no small task for courts to
field a large new influx of warrant applications that could
come on any day of the year and at any hour. In many
jurisdictions, judicial officers have the authority to issue
warrants only within their own districts, see, e.g., Fed.
Rule Crim. Proc. 41(b); N. D. Rule Crim. Proc. 41(a)
(2016–2017), and in rural areas, some districts may have
only a small number of judicial officers.
   North Dakota, for instance, has only 51 state district
28                BIRCHFIELD v. NORTH DAKOTA

                          Opinion of the Court

judges spread across eight judicial districts.4 Those judges
are assisted by 31 magistrates, and there are no magis­
trates in 20 of the State’s 53 counties.5 At any given loca­
tion in the State, then, relatively few state officials have
authority to issue search warrants.6 Yet the State, with a
population of roughly 740,000, sees nearly 7,000 drunk-
driving arrests each year. Office of North Dakota Attor­
ney General, Crime in North Dakota, 2014, pp. 5, 47
(2015). With a small number of judicial officers author­
ized to issue warrants in some parts of the State, the
burden of fielding BAC warrant applications 24 hours per
day, 365 days of the year would not be the light burden
that petitioners and JUSTICE SOTOMAYOR suggest.
   In light of this burden and our prior search-incident-to­
arrest precedents, petitioners would at a minimum have to
show some special need for warrants for BAC testing. It is
therefore appropriate to consider the benefits that such
applications would provide. Search warrants protect
privacy in two main ways. First, they ensure that a
search is not carried out unless a neutral magistrate
makes an independent determination that there is proba­
ble cause to believe that evidence will be found. See, e.g.,
Riley, 573 U. S., at ___ (slip op., at 5). Second, if the mag­
istrate finds probable cause, the warrant limits the intru­
sion on privacy by specifying the scope of the search—that
is, the area that can be searched and the items that can be
sought. United States v. Chadwick, 433 U. S. 1, 9 (1977),

——————
   4 See North Dakota Supreme Court, All District Judges, http://

www.ndcourts.gov/court/districts/judges.htm (all Internet materials as
last visited June 21, 2016).
   5 See North Dakota Supreme Court, Magistrates, http://www.ndcourts.gov/

court/counties/magistra/members.htm.
   6 North Dakota Supreme Court justices apparently also have author-

ity to issue warrants statewide. See ND Op. Atty. Gen. 99–L–132, p. 2
(Dec. 30, 1999). But we highly doubt that they regularly handle search-
warrant applications, much less during graveyard shifts.
                 Cite as: 579 U. S. ____ (2016)          29

                     Opinion of the Court

abrogated on other grounds, Acevedo, 500 U. S. 565.
   How well would these functions be performed by the
warrant applications that petitioners propose? In order to
persuade a magistrate that there is probable cause for a
search warrant, the officer would typically recite the same
facts that led the officer to find that there was probable
cause for arrest, namely, that there is probable cause to
believe that a BAC test will reveal that the motorist’s
blood alcohol level is over the limit. As these three cases
suggest, see Part II, supra, the facts that establish proba­
ble cause are largely the same from one drunk-driving
stop to the next and consist largely of the officer’s own
characterization of his or her observations—for example,
that there was a strong odor of alcohol, that the motorist
wobbled when attempting to stand, that the motorist
paused when reciting the alphabet or counting backwards,
and so on. A magistrate would be in a poor position to
challenge such characterizations.
   As for the second function served by search warrants—
delineating the scope of a search—the warrants in ques­
tion here would not serve that function at all. In every
case the scope of the warrant would simply be a BAC test
of the arrestee. Cf. Skinner, 489 U. S., at 622 (“[I]n light
of the standardized nature of the tests and the minimal
discretion vested in those charged with administering the
program, there are virtually no facts for a neutral magis­
trate to evaluate”). For these reasons, requiring the police
to obtain a warrant in every case would impose a substan­
tial burden but no commensurate benefit.
   Petitioners advance other alternatives to warrantless
BAC tests incident to arrest, but these are poor substi­
tutes. Relying on a recent NHTSA report, petitioner
Birchfield identifies 19 strategies that he claims would be
at least as effective as implied consent laws, including
high-visibility sobriety checkpoints, installing ignition
interlocks on repeat offenders’ cars that would disable
30             BIRCHFIELD v. NORTH DAKOTA

                     Opinion of the Court

their operation when the driver’s breath reveals a suffi­
ciently high alcohol concentration, and alcohol treatment
programs. Brief for Petitioner in No. 14–1468, at 44–45.
But Birchfield ignores the fact that the cited report de­
scribes many of these measures, such as checkpoints, as
significantly more costly than test refusal penalties.
NHTSA, A. Goodwin et al., Countermeasures That Work:
A Highway Safety Countermeasures Guide for State
Highway Safety Offices, p. 1–7 (No. 811727, 7th ed. 2013).
Others, such as ignition interlocks, target only a segment
of the drunk-driver population. And still others, such as
treatment programs, are already in widespread use, see
id., at 1–8, including in North Dakota and Minnesota.
Moreover, the same NHTSA report, in line with the agen­
cy’s guidance elsewhere, stresses that BAC test refusal
penalties would be more effective if the consequences for
refusal were made more severe, including through the
addition of criminal penalties. Id., at 1–16 to 1–17.
                             3
  Petitioner Bernard objects to the whole idea of analyz­
ing breath and blood tests as searches incident to arrest.
That doctrine, he argues, does not protect the sort of gov­
ernmental interests that warrantless breath and blood
tests serve. On his reading, this Court’s precedents per­
mit a search of an arrestee solely to prevent the arrestee
from obtaining a weapon or taking steps to destroy evi­
dence. See Reply Brief in No. 14–1470, at 4–6. In Chimel,
for example, the Court derived its limitation for the scope
of the permitted search—“the area into which an arrestee
might reach”—from the principle that officers may rea­
sonably search “the area from within which he might gain
possession of a weapon or destructible evidence.” 395
U. S., at 763. Stopping an arrestee from destroying evi­
dence, Bernard argues, is critically different from prevent­
ing the loss of blood alcohol evidence as the result of the
                 Cite as: 579 U. S. ____ (2016)          31

                     Opinion of the Court

body’s metabolism of alcohol, a natural process over which
the arrestee has little control. Reply Brief in No. 14–1470,
at 5–6.
  The distinction that Bernard draws between an ar­
restee’s active destruction of evidence and the loss of
evidence due to a natural process makes little sense. In
both situations the State is justifiably concerned that
evidence may be lost, and Bernard does not explain why
the cause of the loss should be dispositive. And in fact
many of this Court’s post-Chimel cases have recognized
the State’s concern, not just in avoiding an arrestee’s
intentional destruction of evidence, but in “evidence
preservation” or avoiding “the loss of evidence” more gen­
erally. Riley, 573 U. S., at ___ (slip op., at 8); see also
Robinson, 414 U. S., at 234 (“the need to preserve evidence
on his person”); Knowles v. Iowa, 525 U. S. 113, 118–119
(1998) (“the need to discover and preserve evidence;” “the
concern for destruction or loss of evidence” (emphasis
added)); Virginia v. Moore, 553 U. S. 164, 176 (2008) (the
need to “safeguard evidence”). This concern for preserving
evidence or preventing its loss readily encompasses the
inevitable metabolization of alcohol in the blood.
  Nor is there any reason to suspect that Chimel’s use of
the word “destruction,” 395 U. S., at 763, was a deliberate
decision to rule out evidence loss that is mostly beyond the
arrestee’s control. The case did not involve any evidence
that was subject to dissipation through natural processes,
and there is no sign in the opinion that such a situation
was on the Court’s mind.
  Bernard attempts to derive more concrete support for
his position from Schmerber. In that case, the Court
stated that the “destruction of evidence under the direct
control of the accused” is a danger that is not present
“with respect to searches involving intrusions beyond the
body’s surface.” 384 U. S., at 769. Bernard reads this to
mean that an arrestee cannot be required “to take a chem­
32             BIRCHFIELD v. NORTH DAKOTA

                      Opinion of the Court

ical test” incident to arrest, Brief for Petitioner in No. 14–
1470, at 19, but by using the term “chemical test,” Ber­
nard obscures the fact that Schmerber’s passage was
addressed to the type of test at issue in that case, namely
a blood test. The Court described blood tests as “searches
involving intrusions beyond the body’s surface,” and it saw
these searches as implicating important “interests in
human dignity and privacy,” 384 U. S., at 769–770. Al-
though the Court appreciated as well that blood tests “in­
volv[e] virtually no risk, trauma, or pain,” id., at 771, its
point was that such searches still impinge on far more
sensitive interests than the typical search of the person of
an arrestee. Cf. supra, at 22–23. But breath tests, unlike
blood tests, “are not invasive of the body,” Skinner, 489
U. S., at 626 (emphasis added), and therefore the Court’s
comments in Schmerber are inapposite when it comes to
the type of test Bernard was asked to take. Schmerber did
not involve a breath test, and on the question of breath
tests’ legality, Schmerber said nothing.
   Finally, Bernard supports his distinction using a pas­
sage from the McNeely opinion, which distinguishes be­
tween “easily disposable evidence” over “which the suspect
has control” and evidence, like blood alcohol evidence, that
is lost through a natural process “in a gradual and rela­
tively predictable manner.” 569 U. S., at ___ (slip op., at
10); see Reply Brief in No. 14–1470, at 5–6. Bernard fails
to note the issue that this paragraph addressed. McNeely
concerned only one exception to the usual warrant re­
quirement, the exception for exigent circumstances, and as
previously discussed, that exception has always been
understood to involve an evaluation of the particular facts
of each case. Here, by contrast, we are concerned with the
search-incident-to-arrest exception, and as we made clear
in Robinson and repeated in McNeely itself, this authority
is categorical. It does not depend on an evaluation of the
threat to officer safety or the threat of evidence loss in a
                      Cite as: 579 U. S. ____ (2016)                     33

                           Opinion of the Court

particular case.7
  Having assessed the effect of BAC tests on privacy
interests and the need for such tests, we conclude that the
Fourth Amendment permits warrantless breath tests
incident to arrests for drunk driving. The impact of
breath tests on privacy is slight, and the need for BAC
testing is great.
  We reach a different conclusion with respect to blood
tests. Blood tests are significantly more intrusive, and
their reasonableness must be judged in light of the availa­
bility of the less invasive alternative of a breath test.
Respondents have offered no satisfactory justification for
demanding the more intrusive alternative without a
warrant.
  Neither respondents nor their amici dispute the effec­
——————
   7 JUSTICE SOTOMAYOR objects to treating warrantless breath tests as

searches incident to a lawful arrest on two additional grounds.
   First, she maintains that “[a]ll of this Court’s postarrest exceptions to
the warrant requirement require a law enforcement interest separate
from criminal investigation.” Post, at 14. At least with respect to the
search-incident-to-arrest doctrine, that is not true. As the historical
authorities discussed earlier attest, see Part V–A, supra, the doctrine
has always been understood as serving investigative ends, such as
“discover[ing] and seiz[ing] . . . evidences of crime.” Weeks v. United
States, 232 U. S. 383, 392 (1914); see also United States v. Robinson,
414 U. S. 218, 235 (1973) (emphasizing “the need . . . to discover evi­
dence”). Using breath tests to obtain evidence of intoxication is there­
fore well within the historical understanding of the doctrine’s purposes.
   Second, JUSTICE SOTOMAYOR contends that the search-incident-to­
arrest doctrine does not apply when “a narrower exception to the
warrant requirement adequately satisfies the governmental needs
asserted.” Post, at 7, n. 3; see also post, at 17–19. But while this
Court’s cases have certainly recognized that “more targeted” exceptions
to the warrant requirement may justify a warrantless search even
when the search-incident-to-arrest exception would not, Riley v. Cali-
fornia, 573 U. S. ___, ___ (2014) (slip op., at 14), JUSTICE SOTOMAYOR
cites no authority for the proposition that an exception to the warrant
requirement cannot apply simply because a “narrower” exception might
apply.
34             BIRCHFIELD v. NORTH DAKOTA

                      Opinion of the Court

tiveness of breath tests in measuring BAC. Breath tests
have been in common use for many years. Their results
are admissible in court and are widely credited by juries,
and respondents do not dispute their accuracy or utility.
What, then, is the justification for warrantless blood tests?
   One advantage of blood tests is their ability to detect not
just alcohol but also other substances that can impair a
driver’s ability to operate a car safely. See Brief for New
Jersey et al. as Amici Curiae 9; Brief for United States as
Amicus Curiae 6. A breath test cannot do this, but police
have other measures at their disposal when they have
reason to believe that a motorist may be under the influ­
ence of some other substance (for example, if a breath test
indicates that a clearly impaired motorist has little if any
alcohol in his blood). Nothing prevents the police from
seeking a warrant for a blood test when there is sufficient
time to do so in the particular circumstances or from
relying on the exigent circumstances exception to the
warrant requirement when there is not. See McNeely, 569
U. S., at ___–___ (slip op., at 22–23).
   A blood test also requires less driver participation than
a breath test. In order for a technician to take a blood
sample, all that is needed is for the subject to remain still,
either voluntarily or by being immobilized. Thus, it is
possible to extract a blood sample from a subject who
forcibly resists, but many States reasonably prefer not to
take this step. See, e.g., Neville, 459 U. S., at 559–560.
North Dakota, for example, tells us that it generally op­
poses this practice because of the risk of dangerous alter­
cations between police officers and arrestees in rural areas
where the arresting officer may not have backup. Brief for
Respondent in No. 14–1468, p. 29. Under current North
Dakota law, only in cases involving an accident that re­
sults in death or serious injury may blood be taken from
arrestees who resist. Compare N. D. Cent. Code Ann.
§§39–20–04(1), 39–20–01, with §39–20–01.1.
                     Cite as: 579 U. S. ____ (2016)                  35

                         Opinion of the Court

  It is true that a blood test, unlike a breath test, may be
administered to a person who is unconscious (perhaps as a
result of a crash) or who is unable to do what is needed to
take a breath test due to profound intoxication or injuries.
But we have no reason to believe that such situations are
common in drunk-driving arrests, and when they arise,
the police may apply for a warrant if need be.
  A breath test may also be ineffective if an arrestee
deliberately attempts to prevent an accurate reading by
failing to blow into the tube for the requisite length of time
or with the necessary force. But courts have held that
such conduct qualifies as a refusal to undergo testing, e.g.,
Andrews v. Turner, 52 Ohio St. 2d 31, 36–37, 368 N. E. 2d
1253, 1256–1257 (1977); In re Kunneman, 501 P. 2d 910,
910–911 (Okla. Civ. App. 1972); see generally 1 Erwin
§4.08[2] (collecting cases), and it may be prosecuted as
such. And again, a warrant for a blood test may be
sought.
  Because breath tests are significantly less intrusive
than blood tests and in most cases amply serve law en­
forcement interests, we conclude that a breath test, but
not a blood test, may be administered as a search incident
to a lawful arrest for drunk driving. As in all cases involv­
ing reasonable searches incident to arrest, a warrant is
not needed in this situation.8
——————
   8 JUSTICE THOMAS partly dissents from this holding, calling any dis­

tinction between breath and blood tests “an arbitrary line in the sand.”
Post, at 3 (opinion concurring in judgment in part and dissenting in
part). Adhering to a position that the Court rejected in McNeely,
JUSTICE THOMAS would hold that both breath and blood tests are
constitutional with or without a warrant because of the natural metab­
olization of alcohol in the bloodstream. Post, at 3–5. Yet JUSTICE
THOMAS does not dispute our conclusions that blood draws are more
invasive than breath tests, that breath tests generally serve state
interests in combating drunk driving as effectively as blood tests, and
that our decision in Riley calls for a balancing of individual privacy
interests and legitimate state interests to determine the reasonableness
36                BIRCHFIELD v. NORTH DAKOTA

                          Opinion of the Court

                              VI
   Having concluded that the search incident to arrest
doctrine does not justify the warrantless taking of a blood
sample, we must address respondents’ alternative argu­
ment that such tests are justified based on the driver’s
legally implied consent to submit to them. It is well estab­
lished that a search is reasonable when the subject con­
sents, e.g., Schneckloth v. Bustamonte, 412 U. S. 218, 219
(1973), and that sometimes consent to a search need not
be express but may be fairly inferred from context, cf.
Florida v. Jardines, 569 U. S. 1, ___–___ (2013) (slip op., at
6–7); Marshall v. Barlow’s, Inc., 436 U. S. 307, 313 (1978).
Our prior opinions have referred approvingly to the gen­
eral concept of implied-consent laws that impose civil
penalties and evidentiary consequences on motorists who
refuse to comply. See, e.g., McNeely, supra, at ___ (plural-
ity opinion) (slip op., at 18); Neville, supra, at 560. Peti­
tioners do not question the constitutionality of those laws,
and nothing we say here should be read to cast doubt on
them.
   It is another matter, however, for a State not only to
insist upon an intrusive blood test, but also to impose
criminal penalties on the refusal to submit to such a test.
There must be a limit to the consequences to which motor­
ists may be deemed to have consented by virtue of a deci­
sion to drive on public roads.
   Respondents and their amici all but concede this point.
North Dakota emphasizes that its law makes refusal a
misdemeanor and suggests that laws punishing refusal
——————
of the category of warrantless search that is at issue. Contrary to
JUSTICE THOMAS’s contention, this balancing does not leave law en­
forcement officers or lower courts with unpredictable rules, because it is
categorical and not “case-by-case,” post, at 3. Indeed, today’s decision
provides very clear guidance that the Fourth Amendment allows
warrantless breath tests, but as a general rule does not allow warrant-
less blood draws, incident to a lawful drunk-driving arrest.
                 Cite as: 579 U. S. ____ (2016)           37

                     Opinion of the Court

more severely would present a different issue. Brief for
Respondent in No. 14–1468, at 33–34. Borrowing from our
Fifth Amendment jurisprudence, the United States sug­
gests that motorists could be deemed to have consented to
only those conditions that are “reasonable” in that they
have a “nexus” to the privilege of driving and entail penal­
ties that are proportional to severity of the violation.
Brief for United States as Amicus Curiae 21–27. But in
the Fourth Amendment setting, this standard does not
differ in substance from the one that we apply, since rea­
sonableness is always the touchstone of Fourth Amend­
ment analysis, see Brigham City v. Stuart, 547 U. S. 398,
403 (2006). And applying this standard, we conclude that
motorists cannot be deemed to have consented to submit
to a blood test on pain of committing a criminal offense.
                            VII
  Our remaining task is to apply our legal conclusions to
the three cases before us.
  Petitioner Birchfield was criminally prosecuted for
refusing a warrantless blood draw, and therefore the
search he refused cannot be justified as a search incident
to his arrest or on the basis of implied consent. There is
no indication in the record or briefing that a breath test
would have failed to satisfy the State’s interests in acquir­
ing evidence to enforce its drunk-driving laws against
Birchfield. And North Dakota has not presented any case-
specific information to suggest that the exigent circum­
stances exception would have justified a warrantless
search. Cf. McNeely, 569 U. S., at ___–___ (slip op., at 20–
23). Unable to see any other basis on which to justify a
warrantless test of Birchfield’s blood, we conclude that
Birchfield was threatened with an unlawful search and
that the judgment affirming his conviction must be
reversed.
  Bernard, on the other hand, was criminally prosecuted
38                BIRCHFIELD v. NORTH DAKOTA

                          Opinion of the Court

for refusing a warrantless breath test. That test was a
permissible search incident to Bernard’s arrest for drunk
driving, an arrest whose legality Bernard has not con-
tested. Accordingly, the Fourth Amendment did not re­
quire officers to obtain a warrant prior to demanding the
test, and Bernard had no right to refuse it.
  Unlike the other petitioners, Beylund was not prose-
cuted for refusing a test. He submitted to a blood test after
police told him that the law required his submission, and
his license was then suspended and he was fined in an
administrative proceeding. The North Dakota Supreme
Court held that Beylund’s consent was voluntary on the
erroneous assumption that the State could permissibly
compel both blood and breath tests. Because voluntari­
ness of consent to a search must be “determined from the
totality of all the circumstances,” Schneckloth, supra, at
227, we leave it to the state court on remand to reevaluate
Beylund’s consent given the partial inaccuracy of the
officer’s advisory.9
  We accordingly reverse the judgment of the North Da­
kota Supreme Court in No. 14–1468 and remand the case for
further proceedings not inconsistent with this opinion. We
affirm the judgment of the Minnesota Supreme Court in
No. 14–1470. And we vacate the judgment of the North
Dakota Supreme Court in No. 14–1507 and remand the
case for further proceedings not inconsistent with this
opinion.
                                             It is so ordered.
——————
   9 If the court on remand finds that Beylund did not voluntarily con­

sent, it will have to address whether the evidence obtained in the
search must be suppressed when the search was carried out pursuant
to a state statute, see Heien v. North Carolina, 574 U. S. ___, ___–___
(2014) (slip op., at 8–10), and the evidence is offered in an administra­
tive rather than criminal proceeding, see Pennsylvania Bd. of Probation
and Parole v. Scott, 524 U. S. 357, 363–364 (1998). And as Beylund
notes, remedies may be available to him under state law. See Brief for
Petitioner in No. 14–1507, pp. 13–14.
                 Cite as: 579 U. S. ____ (2016)          1

                   Opinion of SOTOMAYOR, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

              Nos. 14–1468, 14–1470, and 14–1507
                         _________________


          DANNY BIRCHFIELD, PETITIONER
14–1468                v.
                 NORTH DAKOTA;
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                    NORTH DAKOTA




   WILLIAM ROBERT BERNARD, JR., PETITIONER
14–1470              v.
              MINNESOTA; AND
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      MINNESOTA




     STEVE MICHAEL BEYLUND, PETITIONER
14–1507               v.
     GRANT LEVI, DIRECTOR, NORTH DAKOTA
        DEPARTMENT OF TRANSPORTATION
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                    NORTH DAKOTA



                        [June 23, 2016] 


   JUSTICE SOTOMAYOR, with whom JUSTICE GINSBURG
joins, concurring in part and dissenting in part.
   The Court today considers three consolidated cases. I
join the majority’s disposition of Birchfield v. North Da-
kota, No. 14–1468, and Beylund v. Levi, No. 14–1507, in
which the Court holds that the search-incident-to-arrest
exception to the Fourth Amendment’s warrant require-
ment does not permit warrantless blood tests. But I dis-
2                 BIRCHFIELD v. NORTH DAKOTA

                       Opinion of SOTOMAYOR, J.

sent from the Court’s disposition of Bernard v. Minnesota,
No. 14–1470, in which the Court holds that the same
exception permits warrantless breath tests. Because no
governmental interest categorically makes it impractical
for an officer to obtain a warrant before measuring a
driver’s alcohol level, the Fourth Amendment prohibits
such searches without a warrant, unless exigent circum-
stances exist in a particular case.1
                            I

                            A

  As the Court recognizes, the proper disposition of this
case turns on whether the Fourth Amendment guarantees
a right not to be subjected to a warrantless breath test
after being arrested. The Fourth Amendment provides:
       “The right of the people to be secure in their persons,
       houses, papers, and effects, against unreasonable
       searches and seizures, shall not be violated, and no
       Warrants shall issue, but upon probable cause, sup-
       ported by Oath or affirmation, and particularly de-
       scribing the place to be searched, and the persons or
       things to be seized.”
   The “ultimate touchstone of the Fourth Amendment is
‘reasonableness.’ ” Brigham City v. Stuart, 547 U. S. 398,
403 (2006). A citizen’s Fourth Amendment right to be free
from “unreasonable searches” does not disappear upon
arrest. Police officers may want to conduct a range of
searches after placing a person under arrest. They may
want to pat the arrestee down, search her pockets and
purse, peek inside her wallet, scroll through her cellphone,
examine her car or dwelling, swab her cheeks, or take
——————
    1 Because I see no justification for warrantless blood or warrantless
breath tests, I also dissent from the parts of the majority opinion that
justify its conclusions with respect to blood tests on the availability of
warrantless breath tests. See ante, at 33-34.
                 Cite as: 579 U. S. ____ (2016)           3

                   Opinion of SOTOMAYOR, J.

blood and breath samples to determine her level of intoxi-
cation. But an officer is not authorized to conduct all of
these searches simply because he has arrested someone.
Each search must be separately analyzed to determine its
reasonableness.
   Both before and after a person has been arrested, war-
rants are the usual safeguard against unreasonable
searches because they guarantee that the search is not a
“random or arbitrary ac[t] of government agents,” but is
instead “narrowly limited in its objectives and scope.”
Skinner v. Railway Labor Executives’ Assn., 489 U. S. 602,
622 (1989). Warrants provide the “detached scrutiny of a
neutral magistrate, and thus ensur[e] an objective deter-
mination whether an intrusion is justified.” Ibid. And
they give life to our instruction that the Fourth Amend-
ment “is designed to prevent, not simply to redress, unlaw-
ful police action.” Steagald v. United States, 451 U. S.
204, 215 (1981) (internal quotation marks omitted).
   Because securing a warrant before a search is the rule of
reasonableness, the warrant requirement is “subject only
to a few specifically established and well-delineated excep-
tions.” Katz v. United States, 389 U. S. 347, 357 (1967).
To determine whether to “exempt a given type of search
from the warrant requirement,” this Court traditionally
“assess[es], on the one hand, the degree to which it in-
trudes upon an individual’s privacy and, on the other, the
degree to which it is needed for the promotion of legiti-
mate governmental interests.” Riley v. California, 573
U. S. ___, ___ (2014) (slip op., at 9) (internal quotation
marks omitted). In weighing “whether the public interest
demands creation of a general exception to the Fourth
Amendment’s warrant requirement, the question is not
whether the public interest justifies the type of search in
question,” but, more specifically, “whether the burden of
obtaining a warrant is likely to frustrate the governmental
purpose behind the search.” Camara v. Municipal Court
4                 BIRCHFIELD v. NORTH DAKOTA

                       Opinion of SOTOMAYOR, J.

of City and County of San Francisco, 387 U. S. 523, 533
(1967); see also Almeida-Sanchez v. United States, 413
U. S. 266, 282–283 (1973) (Powell, J., concurring) (noting
that in areas ranging from building inspections to auto-
mobile searches, the Court’s “general approach to excep-
tions to the warrant requirement” is to determine whether
a “ ‘warrant system can be constructed that would be
feasible and meaningful’ ”); United States v. United States
Dist. Court for Eastern Dist. of Mich., 407 U. S. 297, 315
(1972) (“We must . . . ask whether a warrant requirement
would unduly frustrate the [governmental interest]”).2
   Applying these principles in past cases, this Court has
recognized two kinds of exceptions to the warrant re-
quirement that are implicated here: (1) case-by-case ex-
ceptions, where the particularities of an individual case
justify a warrantless search in that instance, but not
others; and (2) categorical exceptions, where the common-
alities among a class of cases justify dispensing with the
warrant requirement for all of those cases, regardless of
their individual circumstances.
   Relevant here, the Court allows warrantless searches on
a case-by-case basis where the “exigencies” of the particu-
lar case “make the needs of law enforcement so compelling
that a warrantless search is objectively reasonable” in that
——————
  2 The Court is wrong to suggest that because the States are seeking

an extension of the “existing” search-incident-to-arrest exception rather
than the “creation” of a new exception for breath searches, this Court
need not determine whether the governmental interest in these searches
can be accomplished without excusing the warrant requirement. Ante,
at 26. To the contrary, as the very sentence the Court cites il-
lustrates, the question is always whether the particular “type of
search in question” is reasonable if conducted without a warrant.
Camara, 387 U. S., at 533. To answer that question, in every case,
courts must ask whether the “burden of obtaining a warrant is likely to
frustrate the governmental purpose behind the search.” Ibid. This
question may be answered based on existing doctrine, or it may require
the creation of new doctrine, but it must always be asked.
                  Cite as: 579 U. S. ____ (2016)            5

                    Opinion of SOTOMAYOR, J.

instance. Missouri v. McNeely, 569 U. S. ___, ___ (2013)
(slip op., at 5) (quoting Kentucky v. King, 563 U. S. 452,
460 (2011)). The defining feature of the exigent circum-
stances exception is that the need for the search becomes
clear only after “all of the facts and circumstances of the
particular case” have been considered in light of the “total-
ity of the circumstances.” 569 U. S., at ___ (slip op., at 8).
Exigencies can include officers’ “need to provide emer-
gency assistance to an occupant of a home, engage in ‘hot
pursuit’ of a fleeing suspect, or enter a burning building to
put out a fire and investigate its cause.” Id., at ___ (slip
op., at 5) (citations omitted).
    Exigencies can also arise in efforts to measure a driver’s
blood alcohol level. In Schmerber v. California, 384 U. S.
757 (1966), for instance, a man sustained injuries in a car
accident and was transported to the hospital. While there,
a police officer arrested him for drunk driving and ordered
a warrantless blood test to measure his blood alcohol
content. This Court noted that although the warrant
requirement generally applies to postarrest blood tests, a
warrantless search was justified in that case because
several hours had passed while the police investigated the
scene of the crime and Schmerber was taken to the hospi-
tal, precluding a timely securing of a warrant. Id., at 770–
771.
    This Court also recognizes some forms of searches in
which the governmental interest will “categorically” out-
weigh the person’s privacy interest in virtually any cir-
cumstance in which the search is conducted. Relevant
here is the search-incident-to-arrest exception.         That
exception allows officers to conduct a limited postarrest
search without a warrant to combat risks that could arise
in any arrest situation before a warrant could be obtained:
“ ‘to remove any weapons that the [arrestee] might seek to
use in order to resist arrest or effect his escape’ ” and to
“ ‘seize any evidence on the arrestee’s person in order to
6              BIRCHFIELD v. NORTH DAKOTA

                   Opinion of SOTOMAYOR, J.

prevent its concealment or destruction.’ ” Riley, 573 U. S.,
at ___ (slip op., at 6) (quoting Chimel v. California, 395
U. S. 752, 763 (1969)). That rule applies “categorical[ly]”
to all arrests because the need for the warrantless search
arises from the very “fact of the lawful arrest,” not from
the reason for arrest or the circumstances surrounding it.
United States v. Robinson, 414 U. S. 218, 225, 235 (1973).
   Given these different kinds of exceptions to the warrant
requirement, if some form of exception is necessary for a
particular kind of postarrest search, the next step is to ask
whether the governmental need to conduct a warrantless
search arises from “threats” that “ ‘lurk in all custodial
arrests’ ” and therefore “justif[ies] dispensing with the
warrant requirement across the board,” or, instead,
whether the threats “may be implicated in a particular
way in a particular case” and are therefore “better ad-
dressed through consideration of case-specific exceptions
to the warrant requirement, such as the one for exigent
circumstances.” Riley, 573 U. S., at ___ (slip op., at 11–12)
(alterations and internal quotation marks omitted).
   To condense these doctrinal considerations into a
straightforward rule, the question is whether, in light of
the individual’s privacy, a “legitimate governmental inter-
est” justifies warrantless searches—and, if so, whether
that governmental interest is adequately addressed by a
case-by-case exception or requires by its nature a categori-
cal exception to the warrant requirement.
                              B
  This Court has twice applied this framework in recent
terms. Riley v. California, 573 U. S. ___,addressed whether,
after placing a person under arrest, a police officer may
conduct a warrantless search of his cell phone data. Cali-
fornia asked for a categorical rule, but the Court rejected
that request, concluding that cell phones do not present
the generic arrest-related harms that have long justified
                    Cite as: 579 U. S. ____ (2016)                   7

                      Opinion of SOTOMAYOR, J.

the search-incident-to-arrest exception. The Court found
that phone data posed neither a danger to officer safety
nor a risk of evidence destruction once the physical phone
was secured. Id., at ___–___ (slip op., at 10–15). The
Court nevertheless acknowledged that the exigent circum-
stances exception might be available in a “now or never
situation.” Id., at ___ (slip op., at 15) (internal quotation
marks omitted). It emphasized that “[i]n light of the
availability of the exigent circumstances exception, there
is no reason to believe that law enforcement officers will
not be able to address” the rare needs that would require
an on-the-spot search. Id., at ___ (slip op., at 26).
   Similarly, Missouri v. McNeely, 569 U. S. ___,applied
this doctrinal analysis to a case involving police efforts to
measure drivers’ blood alcohol levels. In that case, Mis-
souri argued that the natural dissipation of alcohol in a
person’s blood justified a per se exigent circumstances
exception to the warrant requirement—in essence, a new
kind of categorical exception. The Court recognized that
exigencies could exist, like in Schmerber, that would jus-
tify warrantless searches. 569 U. S., at ___ (slip op., at 9).
But it also noted that in many drunk driving situations,
no such exigencies exist. Where, for instance, “the war-
rant process will not significantly increase the delay” in
testing “because an officer can take steps to secure a war-
rant” while the subject is being prepared for the test, there
is “no plausible justification for an exception to the war-
rant requirement.” Id., at ___ (slip op., at 10). The Court
thus found it unnecessary to “depart from careful case-by-
case assessment of exigency and adopt the categorical rule
proposed by the State.” Id., at ___ (slip op., at 9).3
——————
   3 The Court quibbles with our unremarkable statement that the cate-

gorical search-incident-to-arrest doctrine and the case-by-case exigent
circumstances doctrine are part of the same framework by arguing that
a footnote in McNeely was “careful to note that the decision did not
address any other exceptions to the warrant requirement.” Ante, at 26-
8                  BIRCHFIELD v. NORTH DAKOTA

                        Opinion of SOTOMAYOR, J.

                             II
  The States do not challenge McNeely’s holding that a
categorical exigency exception is not necessary to accom-
modate the governmental interests associated with the
dissipation of blood alcohol after drunk-driving arrests.
They instead seek to exempt breath tests from the war-
rant requirement categorically under the search-incident-
to-arrest doctrine. The majority agrees. Both are wrong.
  As discussed above, regardless of the exception a State
requests, the Court’s traditional framework asks whether,
in light of the privacy interest at stake, a legitimate gov-
——————
27 (citing McNeely, 569 U. S., at ___, n. 3 (slip op., at 7, n. 3)). That
footnote explains the difference between categorical exceptions and
case-by-case exceptions generally. Id., at ___, n. 3. It does nothing to
suggest that the two forms of exceptions should not be considered
together when analyzing whether it is reasonable to exempt categori-
cally a particular form of search from the Fourth Amendment’s warrant
requirement.
   It should go without saying that any analysis of whether to apply a
Fourth Amendment warrant exception must necessarily be compara-
tive. If a narrower exception to the warrant requirement adequately
satisfies the governmental needs asserted, a more sweeping exception
will be overbroad and could lead to unnecessary and “unreasonable
searches” under the Fourth Amendment. Contrary to the Court’s
suggestion that “no authority” supports this proposition, see ante, at 33
n. 8, our cases have often deployed this commonsense comparative
check. See Riley v. California, 573 U. S. ___, ___–___ (2014) (slip op., at
14–15) (rejecting the application of the search-incident-to-arrest excep-
tion because the exigency exception is a “more targeted wa[y] to ad-
dress [the government’s] concerns”); id., at ___ (slip op., at 11) (analyz-
ing whether the governmental interest can be “better addressed
through consideration of case-specific exceptions to the warrant re-
quirement”); id., at __ (slip op., at 26–27) (noting that “[i]n light of the
availability of the exigent circumstances exception, there is no reason
to believe that” the governmental interest cannot be satisfied without a
categorical search-incident-to-arrest exception); McNeely, 569 U. S., at
___ (slip op., at 9–10) (holding that the availability of the exigency
exception for circumstances that “make obtaining a warrant impracti-
cal” is “reason . . . not to accept the ‘considerable overgeneralization’
that a per se rule would reflect”).
                    Cite as: 579 U. S. ____ (2016)                 9

                      Opinion of SOTOMAYOR, J.

ernmental interest ever requires conducting breath
searches without a warrant—and, if so, whether that
governmental interest is adequately addressed by a case-
by-case exception or requires a categorical exception to the
warrant requirement. That framework directs the conclu-
sion that a categorical search-incident-to-arrest rule for
breath tests is unnecessary to address the States’ govern-
mental interests in combating drunk driving.
                              A
  Beginning with the governmental interests, there can be
no dispute that States must have tools to combat drunk
driving. See ante, at 2–8. But neither the States nor the
Court has demonstrated that “obtaining a warrant” in
cases not already covered by the exigent circumstances
exception “is likely to frustrate the governmental pur-
pose[s] behind [this] search.” Camara, 387 U. S., at 533.4
  First, the Court cites the governmental interest in pro-
tecting the public from drunk drivers. See ante, at 24.
But it is critical to note that once a person is stopped for
drunk driving and arrested, he no longer poses an imme-
diate threat to the public. Because the person is already
in custody prior to the administration of the breath test,
there can be no serious claim that the time it takes to
obtain a warrant would increase the danger that drunk
driver poses to fellow citizens.
  Second, the Court cites the governmental interest in
preventing the destruction or loss of evidence. See ante, at
30-31. But neither the Court nor the States identify any
practical reasons why obtaining a warrant after making
an arrest and before conducting a breath test compromises
the quality of the evidence obtained. To the contrary, the
delays inherent in administering reliable breath tests
——————
  4 Although Bernard’s case arises in Minnesota, North Dakota’s simi-

lar breath test laws are before this Court. I therefore consider both
States together.
10                BIRCHFIELD v. NORTH DAKOTA

                       Opinion of SOTOMAYOR, J.

generally provide ample time to obtain a warrant.
   There is a common misconception that breath tests are
conducted roadside, immediately after a driver is arrested.
While some preliminary testing is conducted roadside,
reliability concerns with roadside tests confine their use in
most circumstances to establishing probable cause for an
arrest. See 2 R. Erwin, Defense of Drunk Driving Cases
§18.08 (3d ed. 2015) (“Screening devices are . . . used when
it is impractical to utilize an evidential breath tester
(EBT) (e.g. at roadside or at various work sites)”). The
standard evidentiary breath test is conducted after a
motorist is arrested and transported to a police station,
governmental building, or mobile testing facility where
officers can access reliable, evidence-grade breath testing
machinery. Brief for Respondent in No. 14–1618, p. 8,
n. 2; National Highway Transportation Safety Admin.
(NHTSA), A. Berning et al., Refusal of Intoxication Test-
ing: A Report to Congress 4, and n. 5 (No. 811098, Sept.
2008). Transporting the motorist to the equipment site is
not the only potential delay in the process, however.
Officers must also observe the subject for 15 to 20 minutes
to ensure that “residual mouth alcohol,” which can inflate
results and expose the test to an evidentiary challenge at
trial, has dissipated and that the subject has not inserted
any food or drink into his mouth.5 In many States, includ-
ing Minnesota, officers must then give the motorist a
window of time within which to contact an attorney before
administering a test.6 Finally, if a breath test machine is
——————
  5 See  NHTSA and International Assn. of Chiefs of Police, DWI Detec-
tion and Standardized Field Sobriety Testing Participant Guide,
Session 7, p. 20 (2013).
   6 See Minn. Stat. §169A.51, subd. 2(4) (2014) (“[T]he person has the

right to consult with an attorney, but . . . this right is limited to the
extent that it cannot unreasonably delay administration of the test”);
see also Kuhn v. Commissioner of Public Safety, 488 N. W. 2d 838
(Minn. App. 1992) (finding 24 minutes insufficient time to contact an
                    Cite as: 579 U. S. ____ (2016)                11

                      Opinion of SOTOMAYOR, J.

not already active, the police officer must set it up. North
Dakota’s Intoxilyzer 8000 machine can take as long as 30
minutes to “warm-up.”7
  Because of these necessary steps, the standard breath
test is conducted well after an arrest is effectuated. The
Minnesota Court of Appeals has explained that nearly all
breath tests “involve a time lag of 45 minutes to two
hours.” State v. Larson, 429 N. W. 2d 674, 676 (Minn.
App. 1988); see also State v. Chirpich, 392 N. W. 2d 34, 37
(Minn. App. 1986). Both North Dakota and Minnesota
give police a 2-hour period from the time the motorist was
pulled over within which to administer a breath test.
N. D. Cent. Code Ann. §39–20–04.1(1) (2008); Minn. Stat.
§169A.20, subd. 1(5) (2014).8
  During this built-in window, police can seek warrants.
That is particularly true in light of “advances” in technol-
ogy that now permit “the more expeditious processing of
warrant applications.” McNeely, 569 U. S., at ___–___, and
n. 4 (slip op., at 11–12, and n. 4) (describing increased
availability of telephonic warrants); Riley, 573 U. S., at
___ (slip op., at 26) (describing jurisdictions that have
adopted an e-mail warrant system that takes less than 15
minutes); Minn. Rules Crim. Proc. 33.05, 36.01–36.08
(2010 and Supp. 2013) (allowing telephonic warrants); N.
D. Rules Crim. Proc. 41(c)(2)–(3) (2013) (same). Moreover,

counsel for North Dakota explained at oral argument that 

—————— 

attorney before being required to submit to a test).

  7 See Office of Attorney General, Crime Lab. Div., Chemical Test

Training Student Manual, Fall 2011–Spring 2012, p. 13 (2011).
  8 Many tests are conducted at the outer boundaries of that window.

See, e.g., Israel v. Commissioner of Public Safety, 400 N. W. 2d 428
(Minn. App. 1987) (57 minute poststop delay); Mosher v. Commissioner
of Public Safety, 2015 WL 3649344 (Minn. App., June 15, 2015) (119
minute postarrest delay); Johnson v. Commissioner of Public Safety,
400 N. W. 2d 195 (Minn. App. 1987) (96 minute postarrest delay);
Scheiterlein v. Commissioner of Public Safety, 2014 WL 3021278 (Minn.
App., July 7, 2014) (111 minute poststop delay).
12                BIRCHFIELD v. NORTH DAKOTA

                       Opinion of SOTOMAYOR, J.

the State uses a typical “on-call” system in which some
judges are available even during off-duty times.9 See Tr.
of Oral Arg. 42.
   Where “an officer can . . . secure a warrant while” the
motorist is being transported and the test is being pre-
pared, this Court has said that “there would be no plausi-
ble justification for an exception to the warrant require-
ment.” McNeely, 569 U. S., at ___ (slip op., at 10). Neither
the Court nor the States provide any evidence to suggest
that, in the normal course of affairs, obtaining a warrant
and conducting a breath test will exceed the allotted 2-
hour window.
   Third, the Court and the States cite a governmental
interest in minimizing the costs of gathering evidence of
drunk driving. But neither has demonstrated that requir-
ing police to obtain warrants for breath tests would impose
a sufficiently significant burden on state resources to
justify the elimination of the Fourth Amendment’s war-
rant requirement. The Court notes that North Dakota has
82 judges and magistrate judges who are authorized to
issue warrants. See ante, at 27-28. Because North Da-
kota has roughly 7,000 drunk-driving arrests annually, the
Court concludes that if police were required to obtain
warrants “for every search incident to arrest that does not
involve exigent circumstances, the courts would be
swamped.” Ante, at 27. That conclusion relies on inflated
numbers and unsupported inferences.
   Assuming that North Dakota police officers do not ob-
——————
  9 Counsel  for North Dakota represented at oral argument that in
“larger jurisdictions” it “takes about a half an hour” to obtain a war-
rant. Tr. of Oral Arg. 42. Counsel said that it is sometimes “harder to
get somebody on the phone” in rural jurisdictions, but even if it took
twice as long, the process of obtaining a warrant would be unlikely to
take longer than the inherent delays in preparing a motorist for testing
and would be particularly unlikely to reach beyond the 2-hour window
within which officers can conduct the test.
                     Cite as: 579 U. S. ____ (2016)                   13

                       Opinion of SOTOMAYOR, J.

tain warrants for any drunk-driving arrests today, and
assuming that they would need to obtain a warrant for
every drunk-driving arrest tomorrow, each of the State’s
82 judges and magistrate judges would need to issue fewer
than two extra warrants per week.10 Minnesota has nearly
the same ratio of judges to drunk-driving arrests, and so
would face roughly the same burden.11 These back-of-the-
envelope numbers suggest that the burden of obtaining a
warrant before conducting a breath test would be small in
both States.
  But even these numbers overstate the burden by a sig-
nificant degree. States only need to obtain warrants for
drivers who refuse testing and a significant majority of
drivers voluntarily consent to breath tests, even in States
without criminal penalties for refusal. In North Dakota,
only 21% of people refuse breath tests and in Minnesota,
only 12% refuse. NHTSA, E. Namuswe, H. Coleman, & A.
Berning, Breath Test Refusal Rates in the United States–
2011 Update 2 (No. 811881 2014). Including States that
impose only civil penalties for refusal, the average refusal
rate is slightly higher at 24%. Id., at 3. Say that North
Dakota’s and Minnesota’s refusal rates rise to double the
mean, or 48%. Each of their judges and magistrate judges
would need to issue fewer than one extra warrant a
——————
  10 Seven thousand annual arrests divided by 82 judges and magis-

trate judges is 85.4 extra warrants per judge and magistrate judge per
year. And 85.4 divided by 52 weeks is 1.64 extra warrants per judge
and magistrate judge per week.
  11 Minnesota has about 25,000 drunk-driving incidents each year.

Minn. Dept. of Public Safety, Office of Traffic Safety, Minn. Impaired
Driving Facts 2014, p. 2 (2015). In Minnesota, all judges not exercising
probate jurisdiction can issue warrants. Minn. Stat. §626.06 (2009).
But the state district court judges appear to do the lion’s share of that
work. So, conservatively counting only those judges, the State has 280
judges that can issue warrants. Minnesota Judicial Branch, Report to
the Community 23 (2015). Similar to North Dakota, that amounts to
1.72 extra warrants per judge per week.
14               BIRCHFIELD v. NORTH DAKOTA

                      Opinion of SOTOMAYOR, J.

week.12 That bears repeating: The Court finds a categori-
cal exception to the warrant requirement because each of
a State’s judges and magistrate judges would need to issue
less than one extra warrant a week.
   Fourth, the Court alludes to the need to collect evidence
conveniently. But mere convenience in investigating
drunk driving cannot itself justify an exception to the
warrant requirement. All of this Court’s postarrest excep-
tions to the warrant requirement require a law enforce-
ment in

[...TRUNCATED 19424 of 139424 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
