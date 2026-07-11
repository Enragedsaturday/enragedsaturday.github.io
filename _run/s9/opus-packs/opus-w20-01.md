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

## GROUP: _overhaul2/lake/cases/United States v. Soto-Peguero.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Soto-Peguero"
type: case
citation: "978 F.3d 13 (2020)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, First Circuit"
court_level: coa
circuit: 1st
year: 2020
date_decided: 2020-10-19
docket: ""
authority_weight: "Binding in-circuit — 1st Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2020-10-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Soto-Peguero
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4798028/united-states-v-soto-peguero/"
  cluster_id: 4798028
  opinion_id: 4578375
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Recent development (role-based)"
related: ["[[Nix v. Williams]]", "[[United States v. Neugin]]", "[[Murray v. United States]]"]
aliases: ["United States v. Soto-Peguero (1st Cir. 2020)"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "inevitable-discovery", "search-warrant", "first-circuit"]
holding: "Illustrative application of inevitable discovery: government met its burden (agent would have sought and obtained a warrant regardless),…"
lake:
  record_id: United States v. Soto-Peguero
  status: verified
  projected_at: 2026-07-06
---

# United States v. Soto-Peguero

*978 F.3d 13 (1st Cir. 2020)* · U.S. Court of Appeals, First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While securing Soto-Peguero's apartment, Task Force members exceeded the scope of a [[Securing the Scene|protective sweep]] — manipulating an object in a vent and opening a black bag — and found heroin and a gun. The District Court agreed the search went beyond a lawful [[Securing the Scene|protective sweep]], but denied suppression under the inevitable-discovery exception, crediting Special Agent Rideout's testimony that he would have sought and obtained a search warrant regardless. Soto-Peguero appealed.

## Issue
Whether evidence found during a search that exceeded a lawful [[Securing the Scene|protective sweep]] was nonetheless admissible under the inevitable-discovery exception to the exclusionary rule.

## Rule
Under the inevitable-discovery exception, unlawfully obtained evidence is admissible where the government shows it would have been discovered by lawful means. The government carried that burden here: "Because Soto-Peguero has not succeeded in establishing that the United States failed to meet the requirements for applying the inevitable discovery doctrine, we affirm the District Court's denial of his motion to suppress." — *United States v. Soto-Peguero*, 978 F.3d 13 (1st Cir. 2020) (slip op., at 21). ^pin-op21

## Application
The decisive fact was that Soto-Peguero did not challenge Special Agent Rideout's testimony that he would have pursued a search warrant regardless of what the warrantless sweep turned up — and the record showed a warrant would have issued. Soto-Peguero's catalog of alleged officer misconduct during the entry did not defeat the doctrine on these facts. The heroin and gun therefore would inevitably have been discovered through a lawful warrant, so suppression was not required.

## Conclusion
The inevitable-discovery exception applied; the First Circuit affirmed the denial of Soto-Peguero's motion to suppress.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 1st Cir.**
- No negative treatment. *Soto-Peguero* is an illustrative application in which [[Inevitable Discovery and Independent Source|inevitable discovery]] **succeeded** — the government showed a warrant would have been sought and obtained — the mirror image of [[United States v. Neugin]] (10th Cir.), where the chain to discovery was too speculative.

## Appears on
- [[The Exclusionary Rule]] — *Recent development (role-based)*

## Sources
- *United States v. Soto-Peguero*, 978 F.3d 13 (1st Cir. 2020) — https://www.courtlistener.com/opinion/4798028/united-states-v-soto-peguero/ — pinpoint given as slip-opinion page (CourtListener carries the slip opinion; cluster 4798028 → opinion 4578375).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3302cf806da29b7d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Soto-Peguero"}, "payload": {"all": [{"cite": "978 F.3d 13", "page": "13", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "978"}], "display": "978 F.3d 13", "official": {"cite": "978 F.3d 13", "page": "13", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "978"}, "official_selection_present": true, "record_id": "United States v. Soto-Peguero"}}
{"assertion_id": "4b8fadde3c54d7db", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op21", "record_id": "United States v. Soto-Peguero"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op21", "pinpoint_status": "slip-only", "quote": "--- # United States v. Soto-Peguero *978 F.3d 13 (1st Cir. 2020)* · U.S. Court of Appeals, First Circuit · **Binding in-circuit — 1st Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While securing Soto-Peguero's apartment, Task Force members exceeded the scope of a protective sweep — manipulating an object in a vent and opening a black bag — and found heroin and a gun. The District Court agreed the search went beyond a lawful protective sweep, but denied suppression under the inevitable-discovery exception, crediting Special Agent Rideout's testimony that he would have sought and obtained a search warrant regardless. Soto-Peguero appealed. ## Issue Whether evidence found during a search that exceeded a lawful protective sweep was nonetheless admissible under the inevitable-discovery exception to the exclusionary rule. ## Rule Under the inevitable-discovery exception, unlawfully obtained evidence is admissible where the government shows it would have been discovered by lawful means. The government carried that burden here:", "quote_fidelity": "mismatch", "record_id": "United States v. Soto-Peguero", "star_marker": null}}
{"assertion_id": "9cbe66133e39c82f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Soto-Peguero"}, "payload": {"as_of_content": "2020-10-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Soto-Peguero", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Soto-Peguero

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Soto-Peguero",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Soto-Peguero",
    "case_name_short": "Soto-Peguero",
    "case_name_full": "",
    "input_case_name": "United States v. Soto-Peguero",
    "court": "U.S. Court of Appeals, First Circuit",
    "court_id": "ca1",
    "court_level": "coa",
    "circuit": "1st",
    "state": null,
    "date_decided": "2020-10-19",
    "year": 2020,
    "docket": null,
    "cluster_id": 4798028,
    "lead_opinion_id": 4578375,
    "sibling_ids": [
      4578375
    ],
    "absolute_url": "/opinion/4798028/united-states-v-soto-peguero/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "978 F.3d 13",
      "volume": "978",
      "reporter": "F.3d",
      "page": "13",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "978 F.3d 13",
        "volume": "978",
        "reporter": "F.3d",
        "page": "13",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "978 F.3d 13",
    "official_selection": {
      "court_class": "coa",
      "selected": "978 F.3d 13",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op21",
      "page": null,
      "quote": "--- # United States v. Soto-Peguero *978 F.3d 13 (1st Cir. 2020)* \u00b7 U.S. Court of Appeals, First Circuit \u00b7 **Binding in-circuit \u2014 1st Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While securing Soto-Peguero's apartment, Task Force members exceeded the scope of a protective sweep \u2014 manipulating an object in a vent and opening a black bag \u2014 and found heroin and a gun. The District Court agreed the search went beyond a lawful protective sweep, but denied suppression under the inevitable-discovery exception, crediting Special Agent Rideout's testimony that he would have sought and obtained a search warrant regardless. Soto-Peguero appealed. ## Issue Whether evidence found during a search that exceeded a lawful protective sweep was nonetheless admissible under the inevitable-discovery exception to the exclusionary rule. ## Rule Under the inevitable-discovery exception, unlawfully obtained evidence is admissible where the government shows it would have been discovered by lawful means. The government carried that burden here:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-10-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Soto-Peguero",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Cruz-Ramos",
          "cluster_id": 4851346,
          "cite": [
            "987 F.3d 27"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. McKinney",
          "cluster_id": 4900948,
          "cite": [
            "5 F.4th 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Griffin",
          "cluster_id": 10761945,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez",
          "cluster_id": 5291287,
          "cite": [
            "16 F.4th 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Soto-Peguero:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4578375) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca1)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4578375)",
        "reviewed": 4,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4578375)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4578375)",
    "indexed_citing_opinions": 4,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4578375,
        "count": 4,
        "count_source": "search"
      }
    ],
    "citation_count": 4,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-soto-peguero.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 4,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4578375,
        "cited_id": 195103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 195255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 196856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 197057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 200733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 201990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 202008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 468097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 757241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 775404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 2684150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4194190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4376569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4465506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 4554929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 7243442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9429647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9441370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4578375,
        "cited_id": 9490523,
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
    "date_created": "2026-07-06T03:08:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:10:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:09:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Soto-Peguero

```
          United States Court of Appeals
                       For the First Circuit


No. 18-1897

                     UNITED STATES OF AMERICA,

                             Appellee,

                                 v.

                       ORISTEL SOTO-PEGUERO,

                       Defendant, Appellant.


          APPEAL FROM THE UNITED STATES DISTRICT COURT
                FOR THE DISTRICT OF MASSACHUSETTS

              [Hon. Rya W. Zobel, U.S. District Judge]


                               Before

                   Thompson, Kayatta, and Barron,
                           Circuit Judges.


     Jane Elizabeth Lee for appellant.
     Theodore B. Heinrich, Assistant United States Attorney, with
whom Andrew E. Lelling, United States Attorney, was on brief, for
appellee.


                          October 19, 2020
              BARRON, Circuit Judge.           In April 2018, Oristel Soto-

Peguero was convicted in the District of Massachusetts on three

counts related to distribution of heroin in violation of 21 U.S.C.

§ 841(a)(1) and § 846 and one count of discharging a firearm in

furtherance of a drug crime in violation of 18 U.S.C. § 924(c).

The District Court sentenced him to twenty-two years in prison.

Soto-Peguero now argues on appeal that the District Court erred in

denying his motion to suppress certain evidence at trial.                    He also

asserts that the District Court should not have concluded that he

was eligible for a two-level role enhancement under the United

States Sentencing Guidelines.             He thus asks us to vacate his

convictions and resulting sentence.             We affirm.

                                         I.

              We begin by summarizing the facts in the record, viewing

them in the light most favorable to the suppression ruling.                       See

United States v. Arnott, 758 F.3d 40, 43 (1st Cir. 2014).                          In

January 2015, a Task Force consisting of agents from the federal

Drug       Enforcement    Agency   ("DEA")      and    officers     from    several

Massachusetts       law    enforcement    agencies      were      engaged    in    an

investigation       of     potential     heroin       suppliers     in      Taunton,

Massachusetts.1          Pursuant to that joint investigation, between


       1
       We note that this investigation also led to the indictment
of Luis Guzman-Ortiz, whom a separate jury found guilty of
conspiring with Soto-Peguero to distribute heroin. Guzman-Ortiz
successfully filed a motion for acquittal on that charge pursuant


                                       - 2 -
January and July 2015, Task Force members used a series of wiretaps

to   investigate   Eddyberto    Mejia-Ramos,     a     suspected     local

trafficker.

          The   wiretaps   intercepted   a   number    of    conversations

between Mejia-Ramos and Soto-Peguero, which indicated that Soto-

Peguero was supplying Mejia-Ramos with heroin.              Members of the

Task Force suspected that Soto-Peguero's girlfriend, Mercedes

Cabral, sometimes transported the drugs to Mejia-Ramos.

          On the afternoon of July 6, 2015, Task Force members

intercepted conversations that indicated that Soto-Peguero would

deliver drugs to Mejia-Ramos's home later that day.          Specifically,

just before 9 p.m., Mejia-Ramos called Soto-Peguero and asked him

to come at 10 p.m. and "bring something heavy."        Soto-Peguero said

in response that he would "send the woman."          Then, at 9:38 p.m.,

he called Mejia-Ramos to let him know "the woman is on her way."

          Four minutes earlier, Cabral had left the apartment that

she shared with Soto-Peguero.   Several Task Force members followed

her as she drove in the direction of Mejia-Ramos's home.              They

then enlisted two Massachusetts State Police troopers to conduct

a traffic stop.    The troopers pulled Cabral over and determined

that she was driving on a suspended license.          In the process of


to Federal Rule of Criminal Procedure 29.        For our opinion
affirming the District Court's grant of the Rule 29 motion, see
United States v. Guzman-Ortiz, ___ F.3d ___, 2020 WL 5542135 (1st
Cir. 2020) [No. 19-1349].


                                - 3 -
arresting her, they discovered close to a kilogram of heroin in

her pocketbook.

             After Cabral's arrest, Special Agent Carl Rideout, the

DEA agent in charge of the Task Force, directed one of its members

to "freeze" Cabral and Soto-Peguero's residence in order to secure

it   while   he     obtained    a   search   warrant.     Task   Force    members

surrounded the apartment.            As they tried to gain entry, someone

fired a gun from inside the apartment out the front door.                   Task

Force members then managed to enter the premises, without a

warrant, and, while there, found substantial evidence of heroin

possession and trafficking.

             The following day, Special Agent Rideout applied for a

search   warrant      for    Soto-Peguero's      apartment.      The   affidavit

supporting the search warrant stated that during a "security sweep"

of the apartment, "officers observed in plain view two large brick

shaped objects believed to be kilograms of heroin, one in each

bedroom."    Additionally, the affidavit stated, a Task Force member

"moved one of the bricks" and "observed a firearm beneath it."

The Magistrate Judge granted the warrant application.

             Task    Force     members    thereafter    executed   that    search

warrant.     In doing so, they discovered additional heroin and other

evidence of drug trafficking.

             On March 23, 2016, a grand jury in the United States

District     Court    for    the    District     of   Massachusetts    issued   a


                                         - 4 -
superseding eight-count indictment.      Soto-Peguero was not named in

Counts One or Four,2 but he was charged with six counts: possession

with intent to distribute 100 grams of heroin in violation of 21

U.S.C. §§ 841(a)(1), 841(b)(1)(B)(i) (Count Two); possession with

intent to distribute one kilogram of heroin in violation of 21

U.S.C. §§ 841(a)(1), 841(b)(1)(A)(i) (Count Three); two counts of

conspiring to distribute and possess heroin in violation of 21

U.S.C. § 846 (Counts Five and Six); illegally possessing a firearm

in violation of 18 U.S.C. § 922(g)(1) (Count Seven); and using a

firearm during and in relation to a drug offense in violation of

18 U.S.C. § 924(c) (Count Eight).

          Soto-Peguero moved pursuant to the Fourth Amendment of

the United States Constitution to suppress, among other things,

the evidence that law enforcement had found at his apartment,

including both the drugs and gun discovered without a warrant on

the night Task Force members first entered his home, and the

further evidence that law enforcement uncovered pursuant to the

warrant that was later issued.    He contended that, as to the first

batch of evidence, "[n]o exigency justified the police's forced

entry" because even if the Task Force had waited to obtain a

warrant, there would have been no "great likelihood that evidence



     2 Count One was brought against Cabral and Count Four was
brought against Guzman-Ortiz, who was arrested at the same time as
Soto-Peguero.


                                 - 5 -
would [have] be[en] destroyed."         He also asserted that even if the

initial entry had been permissible, "the officers' subsequent

decision to search under the auspices of conducting a 'protective

sweep' [was] unsustainable" because "they had no basis to suspect

another person, let alone a dangerous person, was present."                   In

addition, Soto-Peguero challenged the contention that the drugs

and gun the Task Force recovered during the warrantless entry were

in "plain view" when law enforcement arrived.

             Soto-Peguero separately argued that the search warrant

itself was "defective" because it was "based on evidence that was

illegally obtained" during the course of the warrantless entry

into the apartment.        He thus contended that the evidence the Task

Force found after obtaining that warrant had to be suppressed

pursuant to the Fourth Amendment as well.

             In   reply,    the   United      States   argued   that     exigent

circumstances were present at the time of the initial entry into

the apartment because "[i]t was not unreasonable for DEA officers

to fear that Soto-Peguero might conclude that Cabral had been

arrested when Cabral did not arrive in Taunton, did not return

home, and was unable to communicate with Soto-Peguero."                     The

government    also   argued    that   Soto-Peguero     "created   a     distinct

exigency" when he fired a shot through the front door.                 Moreover,

the government contended that the scope of the protective sweep

was necessary because "having been fired at, the officers were


                                      - 6 -
entitled to account for the presence and location of the firearm

to ensure safety" and pointed out that Task Force members had

"testified [at the grand jury] that the heroin package in the front

bedroom was in plain view."

             Finally, the government contended that, even if the Task

Force members' conduct exceeded that of an appropriate protective

sweep, the exclusionary rule should not apply.                The government

argued there was "no doubt but that agents would have sought and

obtained [a warrant] whether or not they observed the kilograms of

heroin in [the] apartment during the sweep," and therefore that

the evidence "inevitably would have been revealed in some other

lawful way."     For that proposition, the government relied on the

inevitable     discovery     doctrine,    which    provides    that   evidence

obtained in violation of the Fourth Amendment is admissible "if it

ineluctably would have been revealed in some other (lawful) way, so

long as (i) the lawful means of its discovery are independent and

would necessarily have been employed, (ii) discovery by that means

is in fact inevitable, and (iii) application of the doctrine in a

particular case will not sully the prophylaxis of the Fourth

Amendment."     United States v. Zapata, 18 F.3d 971, 978 (1st Cir.

1994) (internal citations omitted).

             Soto-Peguero     responded      in   a   separate      memorandum,

arguing,     among   other    things,     that    applying    the   inevitable

discovery    doctrine   in    this   case    would,   in   fact,    "sully   the


                                     - 7 -
prophylaxis of the Fourth Amendment."         He contended that admitting

the evidence would incentivize police misconduct because it would

"assure[] police that they need not wait for a magistrate's

approval."      He argued that this is "what happened here" because

the officers "had little concern about prematurely prying open a

heating vent and rifling through a closed nightstand" since they

were confident a warrant would later issue.

             The District Court held a hearing on Soto-Peguero's

motion to suppress and heard testimony from both Soto-Peguero and

Task Force members who were involved in the warrantless entry and

the execution of the search warrant. The focus of that evidentiary

hearing   was    on   the   Task   Force   members'   and   the   defendant's

conflicting     accounts     regarding     what   transpired      during   the

warrantless entry of Soto-Peguero's home. There were three salient

points of disagreement:        whether the heroin that law enforcement

found in the front bedroom during the initial entry into the

apartment had been in plain view or was concealed by the cover of

an air vent; whether the heroin found in a black plastic bag in

the rear bedroom that same night had been between the bed and the

nightstand or in a drawer of the nightstand; and whether Special

Agent Meletis, of the DEA, looked inside the black plastic bag

during the warrantless entry, as he testified in the suppression

hearing, or only the next day after having obtained the search

warrant, as he testified before the grand jury in March of 2016.


                                     - 8 -
Soto-Peguero also testified at the hearing that, while he was

detained on the first floor of his apartment, it sounded "[l]ike

they were breaking stuff" upstairs and that his bed frame had been

intact prior to the search.

           Soto-Peguero and the United States then both filed post-

hearing briefs.     As relevant here, in addition to renewing the

objections from his motion to suppress, Soto-Peguero elaborated on

his assertion that the District Court "should not excuse the

officers' misconduct by applying the inevitable discovery rule."

In support of that contention, he pointed to what he characterized

as "[t]he fact that at least one officer testified inconsistently

about the scope of his search -- denying and then admitting that

he looked inside a black bag" and to what he contended was the

fact that the "officers[] unreasonabl[y] delay[ed] in seeking the

search warrant" because "they anticipated entering his home that

day,"   but   "rather   than       bothering   to    apply     for   judicial

authorization, they sent more than ten officers to prepare to

'secure' the apartment without a warrant."

           In its post-hearing filing, the United States contended

that the inevitable discovery doctrine's requirements were met.

First, the government repeated its contention that "there can be

no doubt but that agents would have sought and obtained [a search

warrant] whether or not they observed the kilograms of heroin in

[the]   apartment   during   the    sweep."    The    United    States   also


                                    - 9 -
reiterated that there was "no reason to discredit the testimony of

the officers" who averred that the heroin in the front bedroom was

in plain view.       The government then further contended -- in an

argument that appeared to invoke the distinct exception to the

exclusionary rule known as the independent source doctrine, see

Murray v. United States, 487 U.S. 533, 537 (1988) -- that even "if

the discovery of the heroin and firearm [were] excised from the

affidavit in support of the search warrant, there [was] still

overwhelming      probable    cause    to   justify   the   issuance   of   the

warrant."

            The   District     Court   denied    Soto-Peguero's   motion     to

suppress.    United States v. Soto-Peguero, 252 F. Supp. 3d 1, 14

(D. Mass. 2017).       First, the District Court found that exigent

circumstances justified the initial warrantless entry.            Id. at 11-

12.   The District Court concluded that if Cabral had failed to

return in a timely manner, and if Soto-Peguero had been unable to

reach her, he might have concluded that law enforcement was

"closing in" on him.         Id.

            The District Court also found that it was reasonable for

the Task Force members to delay in obtaining the warrant, even if

they had probable cause to search the apartment before Cabral

departed with some of the drugs.            Id. at 12.   Under Supreme Court

precedent, the District Court reasoned, there are "many entirely

proper reasons why police may not want to seek a search warrant as


                                      - 10 -
soon as the bare minimum of evidence needed to establish probable

cause is acquired."         Id. (quoting Kentucky v. King, 563 U.S. 452,

466-67 (2011)).       And, the District Court further determined, the

fact that "police might have foreseen the eventual entry" was not

enough    on    its   own    to   "prevent    application   of   the   exigent

circumstances doctrine."          Id. (quoting United States v. Samboy,

433 F.3d 154, 160 (1st Cir. 2005)).

               The District Court next explained, however, that it was

"not persuaded by the officers' account that a block of heroin was

sticking out of a floor vent."           Id. at 13.     The District Court

also declined to "resolve the conflicting evidence as to whether

a bag in the back bedroom containing heroin was in a drawer or

next to the bed."      Id.    "[E]ven accepting the government's version

of events as true," the court held that "manipulating an object in

a vent and opening a bag goes beyond the scope of a protective

sweep."   Id.

               Nevertheless, the District Court denied Soto-Peguero's

motion to suppress under the inevitable discovery exception to the

exclusionary rule.      The District Court concluded that, even if the

Task Force members had not found the heroin or the gun in their

warrantless search of Soto-Peguero's home, they would have found

that evidence after obtaining a search warrant. The District Court

credited Special Agent Rideout's testimony that he would have

pursued a warrant even if no evidence had been uncovered during


                                     - 11 -
the "protective sweep."         Id.     And the District Court concluded

that the Task Force had probable cause to support a warrant for

such a search even before a single member entered the apartment.

Id.    Therefore, according to the District Court, the government

had "demonstrate[d], to a high degree of probability," that the

evidence inevitably would have been discovered.             Id. (alteration

in original) (quoting United States v. Almeida, 434 F.3d 25, 29

(1st Cir. 2006)).

               The District Court did express disapproval of the fact

that Task Force members looked inside the vent and the bag.             But,

it went on to conclude that admitting the evidence was "unlikely

to    'erode    [Fourth   Amendment]    protections   or   encourage   police

misconduct.'" Id. at 14 (alteration in original) (quoting Almeida,

434 F.3d at 29).      Thus, it determined that admitting the evidence

would not "sully the prophylaxis of the Fourth Amendment" and

therefore "the deterrence rationale [did] not justify putting the

police in a worse position than they would have been had no

misconduct occurred."       Id. at 13-14 (first quoting Zapata, 18 F.3d

at 978; then quoting United States v. Silvestri, 787 F.2d 736, 740

(1st Cir. 1986)).          The District Court therefore denied Soto-

Peguero's suppression motion.

               The case proceeded to trial, which lasted six days.         On

April 2, 2018, the jury convicted Soto-Peguero on Counts Two,




                                      - 12 -
Three, Five, and Eight of the indictment, but acquitted him on

Count Six (conspiring with Guzman-Ortiz).3

             For   the      purposes      of     calculating       Soto-Peguero's

sentencing     range     under      the    Guidelines,       the     Presentence

Investigation Report ("PSR") that the United States Office of

Probation prepared grouped the first three counts of conviction

(Counts    Two,    Three,    and   Five)       separately   from    the   firearm

conviction (Count Eight).          The PSR determined that, based on the

quantity of heroin discovered, Soto-Peguero's base offense level

should be set at 32 for the three grouped charges.                  The PSR also

applied a two-level role enhancement under § 3B1.1(c) of the

Guidelines, because Soto-Peguero "directed his significant other

at the time, Mercedes Cabral, to deliver drugs for him on at least

four separate occasions."

             Soto-Peguero objected to the role enhancement both in

his sentencing memorandum and at the sentencing hearing.                     The

United States argued that Cabral was "clearly directed by Mr. Soto-

Peguero" and that it was "very plain that Mr. Soto-Peguero was

supervising" her activities.         The District Court agreed that Soto-

Peguero was "much more the head of the enterprise" than Cabral was

and upheld the role enhancement accordingly.




     3   Count Seven was dismissed prior to trial.


                                     - 13 -
           Including the role enhancement, and accounting for the

extent of Soto-Peguero's criminal record, the mandatory 10-year

prison sentence for his firearm charge, and his history of mental

health struggles and childhood abuse, the District Court sentenced

him to a total term of incarceration of 264 months with a five-

year term of supervised release and a $400 special assessment.

     The District Court entered judgment on September 12, 2018.

On September 18, 2018, Soto-Peguero filed a timely notice of

appeal.   We have jurisdiction over his appeal from his conviction

under 28 U.S.C. § 1291.   We have jurisdiction over his appeal from

his sentence under 18 U.S.C. § 3742(a).

                                II.

           When a district court denies a motion to suppress, we

review the legal questions de novo and evaluate the factfinding

for clear error.   United States v. Ackies, 918 F.3d 190, 197 (1st

Cir. 2019).

                                 A.

           Soto-Peguero first asserts that the Fourth Amendment

requires suppression of both the evidence the Task Force found the

night of the warrantless entry and the evidence uncovered the

following day pursuant to the search warrant.     He contends that

"[t]here was no information [in the warrant application], aside

from the illegally obtained evidence, supporting a finding that

enumerated evidence of contraband or of a crime would be found" at


                               - 14 -
his home.      Failing that, he argues that, at the very least, the

"closeness" of the question of whether probable cause existed

without the illegally obtained evidence "makes it impossible to

conclude . . . that the Magistrate's decision to issue the warrant

was unaffected by the illegal evidence."

              But, Soto-Peguero's focus on the warrant application is

misplaced.     The District Court held that the evidence at issue --

both the evidence discovered during the warrantless entry and the

evidence found the following day -- is admissible under the

inevitable     discovery      doctrine.       Under     that   exception       to   the

exclusionary     rule,   "[i]f      the    prosecution       can    establish    by   a

preponderance of the evidence that the information ultimately or

inevitably would have been discovered by lawful means . . . the

evidence should be received."             Nix v. Williams, 467 U.S. 431, 444

(1984).     In this case, that means the government must establish

that,   had    there   been    no    search     in    violation     of   the    Fourth

Amendment,     the   officers       inevitably       would   have   applied     for   a

warrant, obtained it, and discovered the evidence in question when

executing that warrant.          See United States v. Procopio, 88 F.3d

21, 27 (1st Cir. 1996) (applying the inevitable discovery doctrine

to admit the illegally uncovered contents of a briefcase where

there was "little reason to doubt that the local police would have

contacted federal agents, even without the information gleaned

during the search," and where it was "even more certain that


                                       - 15 -
federal agents . . . would have then sought a warrant to search

the briefcase").     Thus, because the Task Force members need not

have   actually   obtained   a   warrant   to   rely   on   the   inevitable

discovery exception, any defects in the warrant that they did

obtain the day after their initial warrantless entry of Soto-

Peguero's apartment are not directly relevant to the question of

whether the evidence at issue must be suppressed.           See Silvestri,

787 F.2d at 744 (contemplating situations where a warrantless

search is never followed by a warrant and yet the government relies

on the inevitable discovery doctrine).

            Moreover, here, the United States has made the required

showing under the inevitable discovery doctrine.            In that regard,

Soto-Peguero does not challenge Special Agent Rideout's testimony

that he would have pursued a warrant regardless of what was found

in securing the apartment.       He also does not argue that, if the

Task Force members had delayed entry until they obtained a valid

search warrant, they would not have found the evidence in question

upon its execution.

            To the extent that we can read Soto-Peguero's claim that

the warrant application would have been insufficient without the

illegally obtained evidence as an argument that the police did not

have probable cause to search his home before they entered it, we

disagree.    Soto-Peguero and Cabral lived together at the searched

location; he spoke to Mejia-Ramos on July 6, indicating that he


                                  - 16 -
would deliver heroin that day; he told Mejia-Ramos that Cabral was

on her way around 9:38 p.m., four minutes after she had left their

apartment; and Cabral was then stopped with close to a kilogram of

heroin in her pocketbook.      We thus agree with the District Court

that "the officers had sufficient probable cause" to substantiate

a   search    warrant   for   Soto-Peguero's    apartment   before   the

protective sweep even began.     Soto-Peguero, 252 F. Supp. 3d at 13.

                                   B.

             Soto-Peguero separately argues that the District Court

erred in insulating the evidence at issue from the exclusionary

rule by adverting to our precedent that, in analyzing whether to

admit evidence through the inevitable discovery doctrine, we must

also consider whether doing so would "encourage police misconduct"

and thereby "sully the prophylaxis of the Fourth Amendment."

United States v. Hughes, 640 F.3d 428, 440-41 (1st Cir. 2011)

(quoting Zapata, 18 F.3d at 978).       In undertaking that inquiry, we

need to "dwell[] closely on the facts" and look toward whether the

record establishes that law enforcement officers intentionally

violated the Fourth Amendment as well as the incentives, if any,

for them to act unconstitutionally.        United States v. Scott, 270

F.3d 30, 45 (1st Cir. 2001); see also Hughes, 640 F.3d at 441.

But, rather than develop an argument along those precise lines,

Soto-Peguero instead directs our attention to an out-of-circuit

case, United States v. Madrid, 152 F.3d 1034 (8th Cir. 1998).


                                 - 17 -
There, the Eighth Circuit recognized an exception to the inevitable

discovery    doctrine    because      police     behaved     egregiously          and

"exploited their presence" in the defendant's home.                 Id. at 1040.

Either way, Soto-Peguero's attempt to make the case that the

conduct by law enforcement here precludes us from affirming the

District Court's inevitable discovery ruling fails.

            Invoking    Madrid,   Soto-Peguero       cites   to     a    number    of

instances   of   purported    misconduct      that   he    argues       necessitate

suppression even if the inevitable discovery exception otherwise

would apply.     Specifically, he alleges that the Task Force members

"tore the residence apart," "destroy[ed] furniture," "open[ed]

drawers," "open[ed] containers," "pr[ied] the lid off [an] air

conditioning vent," and "used this illegally obtained evidence to

secure the warrant" during their first entry to his apartment.                    He

also contends that admitting this evidence would "make[] the court

complicit in the officers' false testimony at the suppression

hearing."

            Soto-Peguero     makes    the     allegation     that       Task   Force

members "tore the residence apart" and "destroy[ed] furniture" in

support of his Madrid-based argument for the first time on appeal.

Thus, our review of it is at most for plain error.                      See United

States v. Lara, 970 F.3d 68, 76 (1st Cir. 2020).              We find none, as

the District Court was not asked to make a finding about what, if

any, damage the Task Force members caused in going through the


                                     - 18 -
apartment during their initial entry and the District Court did

not do so on its own.           See United States v. Takesian, 945 F.3d

553, 563 (1st Cir. 2019) (explaining that "if an error pressed by

the appellant turns on 'a factual finding [he] neglected to ask

the district court to make, the error cannot be clear or obvious

unless' he shows that 'the desired factual finding is the only one

rationally supported by the record below'" (quoting United States

v. Olivier-Diaz, 13 F.3d 1, 5 (1st Cir. 1993))).

           We turn, then, to the aspects of Soto-Peguero's Madrid-

based   argument    that   rely       on   the   remaining    allegations       of

misconduct.      In part, Soto-Peguero relies on the assertion that

the record evidence indicates that Task Force members opened the

drawer of the nightstand and looked inside the floor vent when

they went through the apartment without a warrant.                   But, even

accepting that the evidence supports that understanding of their

conduct, it still "falls short of the blatant search through

personal effects in Madrid," just as we concluded the last time

that a criminal defendant asked us to follow the Eighth Circuit's

lead.   United States v. Dent, 867 F.3d 37, 41 (1st Cir. 2017); see

id.   (holding    that   when    an   officer    exceeded    the   scope   of   a

protective sweep by looking under an air mattress, that did not

bring the case within Madrid's purview).

           So, that leaves only Soto-Peguero's contentions that the

inclusion of a description of the evidence turned up during the


                                      - 19 -
warrantless entry in the warrant affidavit and "the officers' false

testimony" at the suppression hearing satisfy the Madrid standard,

at least when considered in the context of how the officers

conducted themselves at that time.      We assume, for the sake of

argument only, that the Eighth Circuit's holding that the officers

in Madrid "exploited their presence" in the defendant's home

extends to encompass this flavor of alleged misconduct.        Even

still, here, too, we are not persuaded.

            The affidavit attached to the search warrant application

did describe evidence that Task Force members uncovered pursuant

to what that affidavit characterized as a "security sweep."    And,

as Soto-Peguero notes, the District Court later found that some of

that evidence was obtained through methods that exceeded the scope

of such a sweep.   But, we do not see how this mismatch suffices to

support Soto-Peguero's Madrid-based suppression argument.       The

Task Force members had been shot at as they tried to enter the

residence and would later testify that they found the evidence

while trying to secure the apartment and locate the firearm in

question.    In such circumstances, we cannot say that the warrant

application's erroneous description of the means by which that

evidence had been acquired constitutes the kind of egregious

conduct that, per Madrid, could justify suppression.     Cf. United

States v. Paradis, 351 F.3d 21, 29 n.7 (1st Cir. 2003) (describing

scenarios in which a protective sweep might properly authorize an


                               - 20 -
officer to specifically search for weapons).    Consistent with this

conclusion, we note that the District Court made no finding here

that any law enforcement officer involved in the preparation of

the      warrant   application       either    knowingly    included

unconstitutionally obtained evidence or knowingly misdescribed

that evidence as having been lawfully obtained.

           With respect to Soto-Peguero's contention that Madrid

requires suppression here based on his allegation that Task Force

members gave false testimony at the suppression hearing, we are

likewise unpersuaded.   The District Court did explain that it was

not fully persuaded by the Task Force members' testimony at the

suppression hearing regarding what happened during the warrantless

entry.   But, the District Court also concluded that there was no

basis for finding on this record the kind of egregious or flagrant

official misconduct that would require suppression in order to not

sully the prophylaxis of the Fourth Amendment.     Soto-Peguero, 252

F. Supp. 3d at 13-14.   In the face of that ruling and the absence

of any finding by the District Court that the Task Force members

who testified at that hearing did so in bad faith, we see no basis

for requiring suppression even were we to accept Soto-Peguero's

argument that we should adopt the Madrid standard.

           Because Soto-Peguero has not succeeded in establishing

that the United States failed to meet the requirements for applying




                                 - 21 -
the inevitable discovery doctrine, we affirm the District Court's

denial of his motion to suppress.

                                           III.

            Soto-Peguero also challenges the fact that the Probation

Office   applied     a    two-level    role       enhancement     to       increase   the

Guidelines range for his drug possession-related crimes from 168-

210 months to 210-262 months.

            Under    § 3B1.1(c)       of     the       Guidelines,     a    defendant's

offense level is increased by two levels if "the defendant was an

organizer,      leader,     manager,       or     supervisor     in    any     criminal

activity"    involving      four      or    fewer       participants.          For    the

enhancement to apply, the government bears the burden of proving,

by a preponderance of the evidence, that "the criminal enterprise

involved at least two complicit participants (of whom the defendant

may be counted as one)" and that "the defendant, in committing the

offense,    exercised      control    over,       organized,     or    was    otherwise

responsible for superintending the activities of, at least one of

those other persons."         United States v. Cruz, 120 F.3d 1, 3 (1st

Cir.   1997).       "The   determination          of    an   individual's      role    in

committing an offense is necessarily fact-specific.                        Accordingly,

appellate review must be conducted with considerable deference."

Id. (internal citation omitted).                   Even a single instance of

managing the actions of others can substantiate the enhancement.

See United States v. Voccola, 99 F.3d 37, 44 (1st Cir. 1996).


                                       - 22 -
            Soto-Peguero         argues        that     the        entirety   of    the

government's case for the enhancement is that, on two occasions,

he stated that he was "sending" Cabral.                     He asserts that, beyond

that, there is nothing in the record to support the conclusion

that he and Cabral "were anything other than equal participants in

criminal activity."

            The    United      States    points       out   that    Soto-Peguero    had

"scores of communications" with Mejia-Ramos, while Cabral only

interacted with him to ask to which house she should go.                       On one

occasion, Mejia-Ramos contacted Soto-Peguero and told him the

heroin was poor quality.             Soto-Peguero replied:            "My woman is on

the way."       Later, Cabral retrieved what were presumably the

inferior drugs from Mejia-Ramos's cousin.                     On another occasion,

after Cabral dropped off a package, Mejia-Ramos called Soto-

Peguero    to     ask   what    he      had    sent.         Per    the   government's

characterization, "both Mejia-Ramos and his cousin treated Cabral

as   a   mere   delivery    person       and    engaged      only    Soto-Peguero    in

important business decisions."

            At sentencing, the District Court -- after presiding

over a six-day trial and observing both Soto-Peguero and Cabral

-- concluded that "Soto-Peguero was running the show."                        He "told

[Cabral] to go to Brockton or wherever it was on a number of

occasions."     That was where she "ultimately got caught."




                                         - 23 -
          Based on all the evidence cited by the United States,

and accounting for the fact that the District Court had the

opportunity to observe the witnesses and the defendant firsthand,

we cannot conclude that the District Court clearly erred in holding

that the government had shown by a preponderance of the evidence

that Soto-Peguero was managing or supervising Cabral on at least

one occasion.   We therefore affirm the District Court's decision.

                                     IV.

          As    described   above,    we   affirm   both   Soto-Peguero's

convictions and his sentence.




                                - 24 -

```

---

## GROUP: _overhaul2/lake/cases/United States v. Touset.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Touset"
type: case
citation: "890 F.3d 1227 (2018)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Eleventh Circuit"
court_level: coa
circuit: 11th
year: 2018
date_decided: 2018-05-23
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2018-05-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Touset
  varies_by_point: false
  scope_note: "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4500452/united-states-v-karl-touset/"
  cluster_id: 4500452
  opinion_id: 4277705
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Recent development (role-based)"
related: ["[[United States v. Ramsey]]", "[[United States v. Cotterman]]", "[[United States v. Flores-Montano]]", "[[Riley v. California]]"]
aliases: ["United States v. Touset (11th Cir. 2018)", "United States v. Karl Touset"]
tags: ["case", "fourth-amendment", "border-searches", "forensic-search", "electronic-devices", "eleventh-circuit", "circuit-split"]
holding: "The Fourth Amendment requires no suspicion — not even reasonable suspicion — for a forensic search of an electronic device at the…"
lake:
  record_id: United States v. Touset
  status: verified
  projected_at: 2026-07-06
---

# United States v. Touset

*890 F.3d 1227 (11th Cir. 2018)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Customs agents at the border forensically searched Touset's electronic devices and found child pornography. The investigation had begun with information that Touset made small Western Union payments to an entity in the Philippines (a country associated with child exploitation) that used an email address tied to child pornography. Touset moved to suppress, and the district court — following the Ninth Circuit's *[[United States v. Cotterman|Cotterman]]* — held that reasonable suspicion was required and was present.

## Issue
Whether the Fourth Amendment requires any suspicion — in particular, reasonable suspicion — for a forensic search of electronic devices at the international border.

## Rule
No. The border-search exception requires no suspicion for searches of property at the border, and that rule extends to forensic searches of electronic devices: "the Fourth Amendment does not require any suspicion for forensic searches of electronic devices at the border." — *United States v. Touset*, 890 F.3d 1227 (11th Cir. 2018) (Part III.A). ^pin-IIIa

The court declined to follow the Ninth Circuit's *[[United States v. Cotterman|Cotterman]]*, reasoning that the Supreme Court has never required suspicion to search **property** (as opposed to highly intrusive searches of the **person**) at the border, and that *[[Riley v. California]]* — a search-incident-to-arrest case — does not transplant a warrant or suspicion requirement to the border.

## Application
Touset's laptops, hard drives, and other devices were forensically searched at the border, where no suspicion is required to search property; the searches were therefore lawful. In the alternative, the court held that reasonable suspicion existed anyway — the Western Union payments to a Philippine entity associated with child exploitation supported the search. Either way, suppression was not warranted.

## Conclusion
No suspicion is required for forensic searches of electronic devices at the border; the Eleventh Circuit affirmed the denial of Touset's motion to suppress.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- No negative treatment within the circuit. **Circuit split:** *Touset* expressly rejects the Ninth Circuit's [[United States v. Cotterman]], which requires reasonable suspicion for forensic (as opposed to manual) searches of electronic devices at the border — a recognized split on suspicion requirements for device searches at the border.

## Appears on
- [[Border Searches]] — *Recent development (role-based)*

## Sources
- *United States v. Touset*, 890 F.3d 1227 (11th Cir. 2018) — https://www.courtlistener.com/opinion/4500452/united-states-v-karl-touset/ — CourtListener's text is paragraph-structured rather than reporter-paginated; the pinpoint is given by opinion section (Part III.A). Cluster 4500452 → opinion 4277705.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e6eb46712b1234d6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Touset"}, "payload": {"all": [{"cite": "890 F.3d 1227", "page": "1227", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "890"}], "display": "890 F.3d 1227", "official": {"cite": "890 F.3d 1227", "page": "1227", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "890"}, "official_selection_present": true, "record_id": "United States v. Touset"}}
{"assertion_id": "674157793084967d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-IIIa", "record_id": "United States v. Touset"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-IIIa", "pinpoint_status": "slip-only", "quote": "--- # United States v. Touset *890 F.3d 1227 (11th Cir. 2018)* · U.S. Court of Appeals, Eleventh Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs agents at the border forensically searched Touset's electronic devices and found child pornography. The investigation had begun with information that Touset made small Western Union payments to an entity in the Philippines (a country associated with child exploitation) that used an email address tied to child pornography. Touset moved to suppress, and the district court — following the Ninth Circuit's *Cotterman* — held that reasonable suspicion was required and was present. ## Issue Whether the Fourth Amendment requires any suspicion — in particular, reasonable suspicion — for a forensic search of electronic devices at the international border. ## Rule No. The border-search exception requires no suspicion for searches of property at the border, and that rule extends to forensic searches of electronic devices:", "quote_fidelity": "mismatch", "record_id": "United States v. Touset", "star_marker": null}}
{"assertion_id": "6821522a5b530ed0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Touset"}, "payload": {"as_of_content": "2018-05-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Touset", "scope_note": "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border.", "varies_by_point": false}}
```

### lake record — United States v. Touset

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Touset",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Karl Touset",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Karl TOUSET, Defendant-Appellant.",
    "input_case_name": "United States v. Touset",
    "court": "U.S. Court of Appeals, Eleventh Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2018-05-23",
    "year": 2018,
    "docket": null,
    "cluster_id": 4500452,
    "lead_opinion_id": 4277705,
    "sibling_ids": [
      4277705
    ],
    "absolute_url": "/opinion/4500452/united-states-v-karl-touset/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "890 F.3d 1227",
      "volume": "890",
      "reporter": "F.3d",
      "page": "1227",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "890 F.3d 1227",
        "volume": "890",
        "reporter": "F.3d",
        "page": "1227",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "890 F.3d 1227",
    "official_selection": {
      "court_class": "coa",
      "selected": "890 F.3d 1227",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-IIIa",
      "page": null,
      "quote": "--- # United States v. Touset *890 F.3d 1227 (11th Cir. 2018)* \u00b7 U.S. Court of Appeals, Eleventh Circuit \u00b7 **Binding in-circuit \u2014 11th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Customs agents at the border forensically searched Touset's electronic devices and found child pornography. The investigation had begun with information that Touset made small Western Union payments to an entity in the Philippines (a country associated with child exploitation) that used an email address tied to child pornography. Touset moved to suppress, and the district court \u2014 following the Ninth Circuit's *Cotterman* \u2014 held that reasonable suspicion was required and was present. ## Issue Whether the Fourth Amendment requires any suspicion \u2014 in particular, reasonable suspicion \u2014 for a forensic search of electronic devices at the international border. ## Rule No. The border-search exception requires no suspicion for searches of property at the border, and that rule extends to forensic searches of electronic devices:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-05-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Touset",
    "varies_by_point": false,
    "scope_note": "Circuit split: the 9th Cir. (United States v. Cotterman) requires reasonable suspicion for forensic device searches at the border.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jordan Jysae Pulido",
          "cluster_id": 10374408,
          "cite": [
            "133 F.4th 1256"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10017987,
          "cite": [
            "111 F.4th 1118"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bruce Mitchell Nicholson",
          "cluster_id": 6244823,
          "cite": [
            "24 F.4th 1341"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haitao Xiang",
          "cluster_id": 9397097,
          "cite": [
            "67 F.4th 895"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524074,
          "cite": [
            "103 F.4th 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Perkins",
          "cluster_id": 4761795,
          "cite": [
            "126 N.Y.S.3d 745",
            "184 A.D.3d 776",
            "2020 NY Slip Op 3425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4781994,
          "cite": [
            "973 F.3d 966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarissa Gilmore v. Georgia Department of Corrections",
          "cluster_id": 10631717,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Aaron Mason v. the State of Texas",
          "cluster_id": 10326280,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524075,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alasaad v. Wolf",
          "cluster_id": 4855246,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Adrian Tremayne Wilson",
          "cluster_id": 4800489,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Touset:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4277705) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(4277705)",
        "reviewed": 13,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 12,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4277705)",
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
    "complete_query": "cites:(4277705)",
    "indexed_citing_opinions": 13,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4277705,
        "count": 13,
        "count_source": "search"
      }
    ],
    "citation_count": 36,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-touset.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 13,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4277705,
        "cited_id": 2420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 76983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 77569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 77895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 78325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 78422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 112417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 145810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 147332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 151874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 203261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 416536,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 432317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 447050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 626016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 770469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 771007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 776207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 798197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 1267346,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 1460543,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4277705,
        "cited_id": 2680439,
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
    "date_created": "2026-07-06T03:10:06Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:13:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:10:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Touset

```
                Case: 17-11561       Date Filed: 05/23/2018       Page: 1 of 25


                                                                                   [PUBLISH]

                  IN THE UNITED STATES COURT OF APPEALS

                            FOR THE ELEVENTH CIRCUIT
                              ________________________

                                     No. 17-11561
                               ________________________

                      D.C. Docket No. 1:15-cr-00045-MHC-JKL-1



UNITED STATES OF AMERICA,

                                                                        Plaintiff-Appellee,
                                             versus

KARL TOUSET,

                                                                    Defendant-Appellant.

                               ________________________

                      Appeal from the United States District Court
                         for the Northern District of Georgia
                             _______________________

                                       (May 23, 2018)

Before WILLIAM PRYOR and JULIE CARNES, Circuit Judges, and
CORRIGAN, * District Judge.

WILLIAM PRYOR, Circuit Judge:



*
  Honorable Timothy J. Corrigan, United States District Judge for the Middle District of Florida,
sitting by designation.
              Case: 17-11561     Date Filed: 05/23/2018   Page: 2 of 25


      This appeal presents the question whether the Fourth Amendment requires

reasonable suspicion for a forensic search of an electronic device at the border.

U.S. Const. amend. IV. Karl Touset appeals the denial of his motions to suppress

the child pornography found on electronic devices that he carried with him when

he entered the country and the fruit of later searches. We recently held that the

Fourth Amendment does not require a warrant or probable cause for a forensic

search of a cell phone at the border. United States v. Vergara, 884 F.3d 1309 (11th

Cir. 2018). Touset argues that, in the light of the decision of the Supreme Court in

Riley v. California, 134 S. Ct. 2473 (2014), reasonable suspicion was required for

the forensic searches of his electronic devices. But our precedents about border

searches of property make clear that no suspicion is necessary to search electronic

devices at the border. Alternatively, the border agents had reasonable suspicion to

search Touset’s electronic devices. We affirm.

                                I. BACKGROUND

      After a series of investigations by private organizations and the government

suggested that Karl Touset was involved with child pornography, border agents

forensically searched his electronic devices after he arrived at the Atlanta airport

on an international flight. Xoom, a company that transmits money, identified

several people it suspected were involved with child pornography based on a

pattern of “frequent low money transfers to” individuals in “source countries for



                                          2
             Case: 17-11561     Date Filed: 05/23/2018   Page: 3 of 25


sex tourism and child pornography,” including the Philippines. Xoom alerted the

National Center for Missing and Exploited Children and notified Yahoo because

some of the people it suspected were involved with child pornography used Yahoo

email and messenger accounts.

      Yahoo then conducted its own investigation into the accounts identified by

Xoom and found a file with child pornography in the account for the email address

iloveyousomuch0820@yahoo.com. This email account listed a phone number in

the Philippines. Yahoo then sent tips to the National Center, which notified the

Cyber Crime Center of the Department of Homeland Security.

      While performing its own investigation, the Cyber Center subpoenaed

transaction data related to the iloveyousomuch0820@yahoo.com email account

and the Philippine phone number associated with it from several companies that

transmit money. One of those companies, Western Union, provided information

about an account associated with the Philippine phone number. The information

established that an account that listed Touset’s name and a post office box in

Marietta, Georgia, had sent three payments to the account associated with the

Philippine phone number. In March 2013, the account associated with Touset sent

a payment of $35 to the account associated with the Philippine phone number; in

April 2013, it sent another payment of $35; and in July 2013, it sent a payment of

$37. Based on this information, the Department placed a “look-out” on Touset so



                                         3
              Case: 17-11561    Date Filed: 05/23/2018    Page: 4 of 25


that his luggage and electronic devices would be searched when he returned to the

country.

      After Touset arrived on an international flight at the airport in Atlanta,

Georgia, on December 21, 2014, Derek Escobar, an officer of the Customs and

Border Protection Agency, inspected Touset’s luggage. Touset had two iPhones, a

camera, two laptops, two external hard drives, and two tablets. Escobar manually

inspected the iPhones and the camera, found no child pornography, and returned

those devices to Touset. But the Agency detained the remaining electronic devices,

and computer forensic analysts at the Department later searched them. Forensic

searches revealed child pornography on the two laptops and the two external hard

drives.

      Based on that information, Dianna Ford, a special agent of the Department,

obtained a warrant to search Touset’s home in Marietta, Georgia. Ford and about

14 other agents executed the warrant on January 28, 2015. During the execution of

the warrant, Ford and another agent read Touset his rights under Miranda v.

Arizona, 384 U.S. 436 (1966), and recorded an interview with him. Ford arrested

Touset after that interview.

      Evidence obtained by the government established that Touset purchased

thousands of images of child pornography. Over the course of several years,

Touset sent more than $55,000 to the Philippines for pornographic pictures, videos,



                                          4
              Case: 17-11561     Date Filed: 05/23/2018    Page: 5 of 25


and webcam sessions. In some webcam sessions, he instructed prepubescent girls

to display and manipulate their genitals. Touset also created an Excel spreadsheet

that documented the names, ages, and birthdates of those young girls as well as his

notes about them.

      A grand jury indicted Touset on three counts: knowingly receiving child

pornography, 18 U.S.C. § 2252(a)(2) & (b)(1); knowingly transporting and

shipping child pornography, 18 U.S.C. § 2252(a)(1) & (b)(1); and knowingly

possessing a computer and computer-storage device containing child pornography,

18 U.S.C. § 2252(a)(4)(B) & (b)(2). Touset initially pleaded not guilty to the

charges.

      Touset filed motions to suppress the evidence obtained from his electronic

devices at the border, as well as the fruit of those searches. After an evidentiary

hearing at which Escobar and Ford testified, the magistrate judge recommended

denying Touset’s motions to suppress. The magistrate judge explained that the

parties agreed that the government “needed reasonable suspicion of criminal

activity in order to lawfully detain for further analysis and search [Touset’s]

electronic devices.” The magistrate judge found that reasonable suspicion was

present because “[t]he collective information of the officers allowed the reasonable

inference that Touset had made three small payments through Western Union to an

entity in the Philippines, a country known for child exploitation,” and that entity



                                           5
              Case: 17-11561    Date Filed: 05/23/2018    Page: 6 of 25


“used an email address that had previously received or sent child pornography.”

And the magistrate judge rejected Touset’s argument that, because his most recent

payment to the Western Union account associated with the Philippine phone

number occurred about one-and-a-half years before his electronic devices were

searched, that evidence was stale. Instead, the magistrate judge found that the

evidence of Touset’s payments was not stale because “[f]iles on a computer are

less likely than other types of contraband to disappear over time and can often be

recovered even if they are deleted.”

      The district court adopted the magistrate judge’s report and recommendation

over Touset’s objections. The district court relied on the decision of the Ninth

Circuit in United States v. Cotterman, 709 F.3d 952, 968 (9th Cir. 2013) (en banc),

and concluded that reasonable suspicion is required for a forensic search of

electronic devices at the border. The district court found that reasonable suspicion

existed for the detention and forensic search of Touset’s electronic devices. And

the district court agreed with the magistrate judge that the evidence was not stale.

      Touset pleaded guilty to knowingly transporting child pornography, but

reserved his right to appeal the denial of his motion to suppress. The government

dismissed the other two counts. And the district court sentenced Touset to 120

months of imprisonment and supervision for life.




                                          6
              Case: 17-11561     Date Filed: 05/23/2018    Page: 7 of 25


                           II. STANDARD OF REVIEW

      “Because rulings on motions to suppress involve mixed questions of fact and

law, we review the district court’s factual findings for clear error, and its

application of the law to the facts de novo.” United States v. Ransfer, 749 F.3d 914,

921 (11th Cir. 2014) (quoting United States v. Bervaldi, 226 F.3d 1256, 1262 (11th

Cir. 2000)). We construe “all facts . . . in the light most favorable to the prevailing

party below.” Id. (quoting Bervaldi, 226 F.3d at 1262). And “[t]he individual

challenging the search bears the burdens of proof and persuasion.” United States v.

Newsome, 475 F.3d 1221, 1224 (11th Cir. 2007) (citation and internal quotation

marks omitted).

                                  III. DISCUSSION

      We divide our discussion in two parts. First, we explain that the Fourth

Amendment does not require any suspicion for forensic searches of electronic

devices at the border. Second, we explain that, in the alternative, the searches of

Touset’s electronic devices were supported by reasonable suspicion.

   A. The Fourth Amendment Permits Forensic Searches of Electronic Devices
                       at the Border Without Suspicion.

      The Fourth Amendment to the Constitution provides, “The right of the

people to be secure in their persons, houses, papers, and effects, against

unreasonable searches and seizures, shall not be violated, and no Warrants shall

issue, but upon probable cause . . . .” U.S. Const. amend. IV. Ordinarily,


                                           7
              Case: 17-11561    Date Filed: 05/23/2018    Page: 8 of 25


“reasonableness requires the obtaining of a judicial warrant.” United States v.

Vergara, 884 F.3d 1309, 1312 (11th Cir. 2018) (alteration adopted) (quoting Riley

v. California, 134 S. Ct. 2473, 2482 (2014)). But border searches are different. Id.

      As we recently reiterated, searches at the border of the country “‘never’

require probable cause or a warrant.” Id. (quoting United States v. Ramsey, 431

U.S. 606, 619 (1977)). The First Congress—the same one that proposed the Fourth

Amendment—empowered customs officials to stop and search without a warrant

any vessel or cargo suspected of illegally entering our nation. See Act of July 31,

1789, ch. 5, § 24, 1 Stat. 29, 43 (1789); Ramsey, 431 U.S. at 616–17 (“The

historical importance of the enactment of this customs statute by the same

Congress which proposed the Fourth Amendment is, we think, manifest.”); Boyd v.

United States, 116 U.S. 616, 623 (1886) (“[I]t is clear that the members of that

body did not regard searches and seizures of [contraband] as ‘unreasonable,’ and

they are not embraced within the prohibition of the [Fourth] [A]mendment.”). And

a year later, Congress expanded that power by permitting customs officials to

board vessels even before they reached the United States. See Act of Aug. 4, 1790,

ch. 35, § 31, 1 Stat. 145, 164–65 (1790); United States v. Villamonte-Marquez, 462

U.S. 579, 584 (1983).

      “Import restrictions and searches of persons or packages at the national

borders rest on different considerations and different rules of constitutional law



                                          8
              Case: 17-11561     Date Filed: 05/23/2018    Page: 9 of 25


from domestic regulations.” United States v. 12 200-Ft. Reels of Super 8MM. Film,

413 U.S. 123, 125 (1973). Congress has “broad powers . . . to prevent smuggling

and to prevent prohibited articles from entry,” id., under its plenary authority “[t]o

lay and collect Taxes, Duties, Imposts and Excises,” U.S. Const. art. I, § 8, cl. 1,

“[t]o regulate Commerce with foreign Nations,” id. art. I, § 8, cl. 3, and “[t]o

establish a[] uniform Rule of Naturalization,” id. art. I, § 8, cl. 4. And because

child pornography is unprotected by the First Amendment, “Congress may declare

it contraband and prohibit its importation.” United States v. Thirty-Seven

Photographs, 402 U.S. 363, 376–77 (1971) (plurality opinion); accord 12 200-Ft.

Reels, 413 U.S. at 128–29; see also Osborne v. Ohio, 495 U.S. 103, 111 (1990)

(“[W]e cannot fault [the government] for attempting to stamp out [child

pornography] at all levels in the distribution chain.”).

      Ordinarily, searches at the border are reasonable without suspicion “simply

by virtue of the fact that they occur at the border.” United States v. Alfaro-

Moncada, 607 F.3d 720, 728 (11th Cir. 2010) (quoting Denson v. United States,

574 F.3d 1318, 1339 (11th Cir. 2009)). The Supreme Court has held that it is

reasonable to conduct without suspicion “[r]outine searches of the persons and

effects of entrants” at our borders. United States v. Montoya de Hernandez, 473

U.S. 531, 538 (1985). And we have similarly explained that, at the border, routine

“pat-down search[es] or frisk[s]” and searches of “[a] traveler’s luggage,”



                                           9
             Case: 17-11561     Date Filed: 05/23/2018    Page: 10 of 25


“[i]ncoming international mail,” and “[v]ehicles” are all reasonable “without any

level of suspicion.” Alfaro-Moncada, 607 F.3d at 728 (collecting cases). A

traveler’s “right to be let alone neither prevents the search of his luggage nor the

seizure of unprotected, but illegal, materials when his possession of them is

discovered during . . . a search.” Thirty-Seven Photographs, 402 U.S. at 376

(plurality opinion).

      The Supreme Court has never required reasonable suspicion for a search of

property at the border, however non-routine and intrusive, and neither have we.

Although in one decision the Supreme Court required reasonable suspicion for the

prolonged detention of a person until she excreted the contraband that she was

suspected of “smuggling . . . in her alimentary canal” or submitted to an x-ray or

rectal examination, Montoya de Hernandez, 473 U.S. at 541; see also id. at 534–

35, it has never applied this requirement to property. Nor has it “been willing to

distinguish . . . between different types of property.” Cotterman, 709 F.3d at 975

(Callahan, J., concurring in part, dissenting in part, and concurring in the

judgment). Indeed, it held in United States v. Flores-Montano that the government

may “remove, disassemble, and reassemble a vehicle’s fuel tank” at the border

without any suspicion. 541 U.S. 149, 155 (2004). It explained that “the reasons that

might support a requirement of some level of suspicion in the case of highly

intrusive searches of the person—dignity and privacy interests of the person being



                                          10
             Case: 17-11561      Date Filed: 05/23/2018    Page: 11 of 25


searched—simply do not carry over to vehicles.” Id. at 152. And it rejected a

judicial attempt to distinguish between “routine” and “nonroutine” searches and to

craft “[c]omplex balancing tests to determine what [constitutes] a ‘routine’ search

of a vehicle, as opposed to a more ‘intrusive’ search of a person.” Id. We have

been similarly unwilling to distinguish between different kinds of property. For

example, we have upheld “a search without reasonable suspicion of a crew

member’s living quarters on a foreign cargo vessel that [wa]s entering this

country,” Alfaro-Moncada, 607 F.3d at 727, even though “[a] cabin is a crew

member’s home—and a home ‘receives the greatest Fourth Amendment

protection,’” id. at 729 (quoting United States v. McGough, 412 F.3d 1232, 1236

(11th Cir. 2005)); accord id. at 732.

      We see no reason why the Fourth Amendment would require suspicion for a

forensic search of an electronic device when it imposes no such requirement for a

search of other personal property. Just as the United States is entitled to search a

fuel tank for drugs, see Flores-Montano, 541 U.S. at 155, it is entitled to search a

flash drive for child pornography. And it does not make sense to say that electronic

devices should receive special treatment because so many people now own them or

because they can store vast quantities of records or effects. The same could be said

for a recreational vehicle filled with personal effects or a tractor-trailer loaded with

boxes of documents. Border agents bear the same responsibility for preventing the



                                           11
             Case: 17-11561      Date Filed: 05/23/2018    Page: 12 of 25


importation of contraband in a traveler’s possession regardless of advances in

technology. Indeed, inspection of a traveler’s property at the border “is an old

practice and is intimately associated with excluding illegal articles from the

country.” Thirty-Seven Photographs, 402 U.S. at 376 (plurality opinion).

      In contrast with searches of property, we have required reasonable suspicion

at the border only “for highly intrusive searches of a person’s body.” Alfaro-

Moncada, 607 F.3d at 729. Even though the Supreme Court has declined to decide

“what level of suspicion, if any, is required for [such] nonroutine border searches

[of a person],” Montoya de Hernandez, 473 U.S. at 541 n.4, we have required

reasonable suspicion for “a strip search or an x-ray examination,” Alfaro-Moncada,

607 F.3d at 729. We have defined the “intrusiveness” of a search of a person’s

body that requires reasonable suspicion “in terms of the indignity that will be

suffered by the person being searched,” in contrast with “whether one search will

reveal more than another.” United States v. Vega-Barvo, 729 F.2d 1341, 1345

(11th Cir. 1984); accord id. at 1346. And “we have isolated three factors which

contribute to the personal indignity endured by the person searched: (1) physical

contact between the searcher and the person searched; (2) exposure of intimate

body parts; and (3) use of force.” Id. at 1346.

      These factors are irrelevant to searches of electronic devices. A forensic

search of an electronic device is not like a strip search or an x-ray; it does not



                                           12
             Case: 17-11561      Date Filed: 05/23/2018    Page: 13 of 25


require border agents to touch a traveler’s body, to expose intimate body parts, or

to use any physical force against him. Although it may intrude on the privacy of

the owner, a forensic search of an electronic device is a search of property. And

our precedents do not require suspicion for intrusive searches of any property at the

border. See Alfaro-Moncada, 607 F.3d at 728–29, 732.

      To be sure, the Fourth and the Ninth Circuits have concluded—in divided

decisions—that the Fourth Amendment requires at least reasonable suspicion for

forensic searches of electronic devices at the border. United States v. Kolsuz, ___

F.3d ____, No. 16-4687, slip op. at 19 (4th Cir. May 9, 2018); Cotterman, 709

F.3d at 968. In Cotterman, the Ninth Circuit equated a forensic search to “a

computer strip search,” 709 F.3d at 966, and stated that “[s]uch a thorough and

detailed search of the most intimate details of one’s life is a substantial intrusion

upon personal privacy and dignity,” id. at 968. And it reasoned that

“[i]ntrusiveness includes both the extent of a search as well as the degree of

indignity that may accompany a search.” Id. at 967 (quoting United States v.

Ramos-Saenz, 36 F.3d 59, 61 n.3 (9th Cir. 1994)). The Fourth Circuit later

explained that the intervening decision of the Supreme Court in Riley “confirmed”

that reasoning. Kolsuz, slip op. at 21. And it revived the distinction between routine

and nonroutine searches of property, see id. at 19–24, that the Supreme Court

rejected in Flores-Montano, 541 U.S. at 152.



                                           13
             Case: 17-11561     Date Filed: 05/23/2018    Page: 14 of 25


      We are unpersuaded. Although the Supreme Court stressed in Riley that the

search of a cell phone risks a significant intrusion on privacy, our decision in

Vergara made clear that Riley, which involved the search-incident-to-arrest

exception, does not apply to searches at the border. 884 F.3d at 1312 (“[T]he

Supreme Court expressly limited its holding to the search-incident-to-arrest

exception.”). And our precedent considers only the “personal indignity” of a

search, not its extensiveness. Vega-Barvo, 729 F.2d at 1346. Again, we fail to see

how the personal nature of data stored on electronic devices could trigger this kind

of indignity when our precedent establishes that a suspicionless search of a home at

the border does not. See Alfaro-Moncada, 607 F.3d at 729, 732. Property and

persons are different. See Flores-Montano, 541 U.S. at 152.

      We are also unpersuaded that a traveler’s privacy interest should be given

greater weight than the “paramount interest [of the sovereign] in protecting . . . its

territorial integrity.” Id. at 153. The Ninth and Fourth Circuits stressed the former

interest and asserted that travelers have no practical options to protect their privacy

when traveling abroad. For example, the Ninth Circuit explained that it is

“impractical, if not impossible, for individuals to make meaningful decisions

regarding what digital content to expose to the scrutiny that accompanies

international travel” and that “removing files unnecessary to an impending trip” is

“a time-consuming task that may not even effectively erase the files.” Cotterman,



                                          14
             Case: 17-11561     Date Filed: 05/23/2018    Page: 15 of 25


709 F.3d at 965. The Fourth Circuit added that “it is neither ‘realistic nor

reasonable to expect the average traveler to leave his digital devices at home when

traveling.’” Kolsuz, slip op. at 21 (quoting United States v. Saboonchi, 990 F.

Supp. 2d 536, 556 (D. Md. 2014)). But a traveler’s “expectation of privacy is less

at the border,” Flores-Montano, 541 U.S. at 154, and the Fourth Amendment does

not guarantee the right to travel without great inconvenience, even within our

borders, see Corbett v. Transp. Sec. Admin., 767 F.3d 1171, 1179 (11th Cir. 2014)

(holding that airport screening “is a reasonable administrative search under the

Fourth Amendment”); see also Kolsuz, slip op. at 34 (Wilkinson, J., concurring in

the judgment) (“Our new world has brought inconvenience and intrusions on an

indiscriminate basis, which none of us welcome, but which most of us undergo in

the interest of assuring a larger common good.”). Anyone who has recently taken a

domestic flight likely experienced inconvenient screening procedures that require

passengers to unpack electronic devices, separate and limit liquids, gels, and

creams, remove their shoes, and walk through a full-body scanner. See Corbett,

767 F.3d at 1174 (explaining that a traveler must walk through a scanner or

undergo a pat-down in airports). Travelers “crossing a border . . . [are] on notice

that a search may be made,” Alfaro-Moncada, 607 F.3d at 732 (quoting United

States v. Hidalgo-Gato, 703 F.2d 1267, 1271 (11th Cir. 1983)), and they are free to

leave any property they do not want searched—unlike their bodies—at home.



                                          15
             Case: 17-11561     Date Filed: 05/23/2018   Page: 16 of 25


      In contrast with the diminished privacy interests of travelers, “[t]he

Government’s interest in preventing the entry of unwanted persons and effects is at

its zenith at the international border.” Flores-Montano, 541 U.S. at 152. As we

have explained, child pornography, no less than drugs or other kinds of contraband,

is prohibited from “enter[ing] the country,” Ramsey, 431 U.S. at 620, and the

government interest in stopping contraband at the border does not depend on

whether child pornography takes the form of digital files or physical photographs.

      Nothing in Riley undermines this interest. In Riley, the Supreme Court

explained that the rationales that support the search-incident-to-arrest exception—

namely the concerns of “harm to officers and destruction of evidence”—did not

“ha[ve] much force with respect to digital content on cell phones,” 134 S. Ct. at

2484, because “digital data” does not pose “comparable risks,” id. at 2485. But

“digital” child pornography poses the same exact “risk” of unlawful entry at the

border as its physical counterpart. If anything, the advent of sophisticated

technological means for concealing contraband only heightens the need of the

government to search property at the border unencumbered by judicial second-

guessing.

      Indeed, if we were to require reasonable suspicion for searches of electronic

devices, we would create special protection for the property most often used to

store and disseminate child pornography. With the advent of the internet, child



                                          16
               Case: 17-11561   Date Filed: 05/23/2018   Page: 17 of 25


pornography offenses overwhelmingly involve the use of electronic devices for the

receipt, storage, and distribution of unlawful images. See U.S. Sent’g Comm’n,

Federal Child Pornography Offenses 5, 71 (2012); see also United States v.

Williams, 553 U.S. 285, 307 (2008) (“Both the State and Federal Governments

have sought to suppress [child pornography] for many years, only to find it

proliferating through the new medium of the Internet.”). And law enforcement

officers routinely investigate child-pornography offenses by forensically searching

an individual’s electronic devices. See U.S. Sent’g Comm’n, supra, at 67–71. We

see no reason why we would permit traditional, invasive searches of all other kinds

of property, see Alfaro-Moncada, 607 F.3d at 724–25, 728, 732, but create a

special rule that will benefit offenders who now conceal contraband in a new kind

of property.

      After all, our nation has classified child pornography as contraband for good

reason. The possession of child pornography “harms and debases the most

defenseless of our citizens,” Williams, 553 U.S. at 307, in profound and lasting

ways. The harm that victims suffer during the production of child pornography “is

exacerbated by the[] circulation” of “a permanent record of the child[’s]

participation.” New York v. Ferber, 458 U.S. 747, 759 (1982); see also U.S. Sent’g

Comm’n, supra, at 118. Victims know that countless people may obtain their

images, see United States v. Pugh, 515 F.3d 1179, 1196 (11th Cir. 2008), and use



                                         17
             Case: 17-11561     Date Filed: 05/23/2018    Page: 18 of 25


them for sexual gratification, see U.S. Sent’g Comm’n, supra, at 113, 118. Victims

also know that their images may contribute to the abuse of new victims. See id.

The online promotion and sharing of child pornography validates the sexual

exploitation of children and “may incite or encourage others to sexually abuse

children.” United States v. Irey, 612 F.3d 1160, 1208 (11th Cir. 2010) (en banc);

see also U.S. Sent’g Comm’n, supra, at 312. And there is evidence that offenders

use child pornography to convince children to participate in their abuse. U.S.

Sent’g Comm’n, supra, at 312. Consumers of child pornography who “‘merely’ or

‘passively’ receive or possess child pornography directly contribute to this

continuing victimization.” Pugh, 515 F.3d at 1196 (quoting United States v. Goff,

501 F.3d 250, 259 (3d Cir. 2007)). And “[t]he greater the customer demand for

child pornography, the more that will be produced.” Irey, 612 F.3d at 1212

(quoting United States v. Goldberg, 491 F.3d 668, 672 (7th Cir. 2007)). We should

not invent heightened constitutional protection for travelers who cross our borders

with this contraband in tow.

      Of course, nothing prevents Congress from enacting laws that provide

greater protections than the Fourth Amendment requires. Indeed, Congress has

repeatedly exercised this power “to strike a balance between privacy and security

in the context of digital searches.” Kolsuz, slip op. at 32 (Wilkinson, J., concurring

in the judgment) (citing USA Freedom Act of 2015, Pub. L. No. 114-23, 129 Stat.



                                          18
             Case: 17-11561     Date Filed: 05/23/2018    Page: 19 of 25


268; Wiretap Act, Pub. L. No. 90-351, 82 Stat. 197 (1961), amended by Electronic

Communications Privacy Act of 1986, Pub. L. No. 99-508, 100 Stat. 1848, and

Communications Assistance for Law Enforcement Act, Pub. L. No. 103-414, 108

Stat. 4279 (1994) (codified as amended at 18 U.S.C. §§ 2510–2522 (2012)); Orin

S. Kerr, The Effect of Legislation on Fourth Amendment Protection, 115 Mich. L.

Rev. 1117, 1120 (2017)). The First Congress required officers to have “reason to

suspect” the concealment of “goods, wares or merchandise subject to duty” before

the officers could “enter any ship or vessel” “to search for, seize, and secure any

such goods, wares or merchandise.” Act of July 31, 1789, ch. 5, § 24, 1 Stat. at 43.

More recently, Congress enacted special protections for financial records in the

Right to Financial Privacy Act of 1978, Pub. L. No. 95-630, tit. XI, 92 Stat. 3641,

3697 (codified at 12 U.S.C. § 3408), and for cell tower location information in the

Stored Communications Act, Pub. L. No. 99-508, tit. II, 100 Stat. 1848, 1860

(1986) (codified at 18 U.S.C. §§ 2701–2712;); see also United States v. Davis, 785

F.3d 498, 519 (11th Cir. 2015) (en banc) (W. Pryor, J., concurring) (explaining that

the Stored Communications Act provides “additional protections” for that

information).

      Instead of “charging unnecessarily ahead,” we must allow Congress to

design the appropriate standard “through the more adaptable legislative process

and the wider lens of legislative hearings.” Kolsuz, slip op. at 30, 31 (Wilkinson, J.,



                                          19
              Case: 17-11561     Date Filed: 05/23/2018     Page: 20 of 25


concurring in the judgment). Such a “legislative process would be informed by

numerous representatives of the executive branch, who can lend their practical

insights and experience to the inquiry.” Id. at 33. “The dangers of judicial

standard-setting in an area as sensitive as border searches [are] . . . apparent.” Id.

“Simply put, we must apply the law and leave the task of developing new rules for

rapidly changing technologies to the branch most capable of weighing the costs

and benefits of doing so.” Davis, 785 F.3d at 520 (W. Pryor, J., concurring).

Judicial restraint is especially important in the context of border searches, “where

there is a longstanding historical practice . . . of deferring to the legislative and

executive branches.” Kolsuz, slip op. at 36 (Wilkinson, J., concurring in the

judgment).

        B. In the Alternative, Reasonable Suspicion Existed for the Forensic
                        Searches of Touset’s Electronic Devices.
      Alternatively, the district court correctly denied Touset’s motions to

suppress because the forensic searches of his electronic devices were supported by

reasonable suspicion. Touset argues that the government lacked reasonable

suspicion because the evidence that he sent three separate payments to the Western

Union account associated with a Philippine phone number was stale and because

the evidence did not show that he had possessed child pornography or would

possess it on his electronic devices. We disagree.




                                           20
              Case: 17-11561    Date Filed: 05/23/2018   Page: 21 of 25


      “Reasonable suspicion . . . must be based upon a ‘particularized and

objective basis for suspecting the particular person of criminal activity.’” Denson,

574 F.3d at 1341 (alteration adopted) (quoting United States v. Cortez, 449 U.S.

411, 417–18 (1981)). The “inquiry focuses on the information available to the

officers at the time of the stop.” United States v. Lewis, 674 F.3d 1298, 1305 (11th

Cir. 2012).

      The government had a “particularized and objective basis for suspecting”

that Touset possessed child pornography on his electronic devices. Denson, 574

F.3d at 1341 (citation and internal quotation marks omitted). The government

knew that Touset had sent three low-money transfers of $35, $35, and $37 to a

Western Union account; that the Western Union account was associated with a

Philippine phone number that was associated with the email account of

iloveyousomuch0820@yahoo.com; that the email account had contained an image

of child pornography; that the Philippines was a source country for child

pornography; that a pattern of “frequent low money transfers” is associated with

child pornography; and that Touset was traveling with nine electronic devices.

Together, this evidence provided reasonable suspicion for the forensic searches of

Touset’s electronic devices.

      The “staleness doctrine . . . requires that the information supporting the

government’s application for a warrant must show that probable cause exists at the



                                         21
             Case: 17-11561      Date Filed: 05/23/2018    Page: 22 of 25


time the warrant issues.” Bervaldi, 226 F.3d at 1264. And the staleness doctrine

also applies to reasonable suspicion. Id. at 1264–65; see also United States v.

Carter, 566 F.3d 970, 975 (11th Cir. 2009). “[S]taleness is an issue that courts

must decide by evaluating the facts of a particular case . . . .” United States v.

Domme, 753 F.2d 950, 953 (11th Cir. 1985). Courts consider “the length of time”

as well as “the nature of the suspected crime (discrete crimes or ongoing

conspiracy), habits of the accused, character of the items sought, and nature and

function of the premises to be searched.” Bervaldi, 226 F.3d at 1265 (citation and

internal quotation marks omitted). We have explained that “[t]here is no particular

rule or time limit for when information becomes stale.” Id.

      Our sister circuits have repeatedly rejected staleness challenges in appeals

involving child pornography. They have observed that “pedophiles rarely, if ever,

dispose of child pornography.” United States v. Zimmerman, 277 F.3d 426, 434 (3d

Cir. 2002); see also United States v. Burkhart, 602 F.3d 1202, 1206–07 (10th Cir.

2010); United States v. Morales-Aldahondo, 524 F.3d 115, 119 (1st Cir. 2008);

United States v. Hay, 231 F.3d 630, 636 (9th Cir. 2000). And probable cause of

involvement in electronic child pornography remains even longer because deleted

files can remain on electronic devices. See United States v. Frechette, 583 F.3d

374, 379 (6th Cir. 2009); Hay, 231 F.3d at 636. As the Tenth Circuit explained,

“information that a person received electronic images of child pornography is less



                                           22
             Case: 17-11561     Date Filed: 05/23/2018   Page: 23 of 25


likely than information about drugs, for example, to go stale because the electronic

images are not subject to spoilage or consumption.” Burkhart, 602 F.3d at 1207.

And other circuits have ruled that probable cause remained after passages of time

similar to the interval here. See, e.g., Frechette, 583 F.3d at 378–79 (16 months);

Morales-Aldahondo, 524 F.3d at 119 (three years).

      We are persuaded that the reasoning of our sister circuits applies in this

circumstance. The evidence that Touset made three separate payments to the

Western Union account associated with the Philippine phone number was not stale

about a year and a half later. That evidence suggested that Touset likely received

child pornography electronically and had child pornography stored on his

electronic devices.

                                IV. CONCLUSION

      We AFFIRM Touset’s judgment of conviction and sentence.




                                         23
             Case: 17-11561     Date Filed: 05/23/2018    Page: 24 of 25


CORRIGAN, District Judge, concurring in part and concurring in the judgment:

      I concur in the majority opinion, except as to Part III.A. As the Court notes,

the Fourth and Ninth Circuits have concluded that the Fourth Amendment requires

at least reasonable suspicion for forensic searches of electronic devices at the

border. See Maj. Op. at 13, citing United States v. Kolsuz, __ F.3d __, No. 16-

4687, slip op. at 19 (4th Cir. May 9, 2018), and United States v. Cotterman, 709

F.3d 952, 968 (9th Cir. 2013). In the district court, the government agreed that the

applicable Fourth Amendment test was whether there was reasonable suspicion of

criminal activity such that border agents could detain Touset’s electronic devices

for forensic analysis. The district court found reasonable suspicion and upheld the

search.

      However, on appeal, the government goes beyond its position in the district

court and argues that border agents need no justification whatsoever to detain (in

this case for seventeen days) and forensically search electronic devices of any

American citizen returning from abroad. This new-found government position

presents a different and difficult question, one not addressed by the Supreme Court

or (until today) any appellate court. In my view, this Court need not reach this

issue to decide this case. I therefore concur only in the Court’s alternative holding

that “the district court correctly denied Touset’s motions to suppress because the




                                          24
             Case: 17-11561    Date Filed: 05/23/2018   Page: 25 of 25


forensic searches of his electronic devices were supported by reasonable

suspicion.” Maj. Op. at 21.




                                        25

```

---

## GROUP: _overhaul2/lake/cases/United States v. Trent.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: United States v. Trent
type: case
citation: "No. 25-5770, slip op. (6th Cir. 2026)"
parallel_cite: ""
neutral_cite: ""
court: 6th Cir.
court_level: coa
circuit: ca6
year: 2026
date_decided: 2026-05-07
docket: 25-5770
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/"
  cluster_id: 10855903
  opinion_id: null
  identity_checked: false
lake:
  record_id: United States v. Trent
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: Key
related:
  - "[[Collective Knowledge and the Fellow-Officer Rule]]"
  - "[[Rodriguez v. United States]]"
  - "[[Whren v. United States]]"
tags:
  - case
  - fourth-amendment
  - collective-knowledge
  - fellow-officer-rule
  - traffic-stop
  - reasonable-suspicion
  - rodriguez-mission
  - sixth-circuit
  - unpublished
holding: "Under the collective-knowledge doctrine, the reasonable suspicion needed to prolong a completed traffic stop for a dog sniff may be imputed to the stopping officer from the knowledge of the investigating agents, even if the responding officer was unaware of the specific facts; because agents surveilling a methamphetamine 'turn-and-burn' operation had ample suspicion and the extension lasted only a minute or two, the brief prolongation was lawful and suppression was properly denied."
aliases:
  - United States v. Trent
  - "United States v. Trent (6th Cir. 2026)"
  - United States v. Mark Anthony Trent
---

# United States v. Trent

*No. 25-5770, slip op. (6th Cir. 2026)* · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10855903 → per curiam opinion 11323299 (No. 25-5770, NOT RECOMMENDED FOR PUBLICATION 26a0207n.06, decided May 7, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (unpublished 6th Cir. slip; no reporter cite — S2 A3). S9-REVERIFY: docket hand-reconstructed, then confirmed live against CL cluster 10855903 (caption/date/court/No. 25-5770); the S9 panel should re-verify the docket and holding before certification. -->

## Background
Investigators developed information from cooperating codefendants, informants, and recorded jail calls that Shaundra Hamilton was making "turn-and-burn" trips to Georgia to obtain methamphetamine for distribution in northeast Tennessee. Cell-phone pings and surveillance placed Mark Anthony Trent, driving a rented Ford Expedition, on such a trip; Homeland Security Special Agent Bulla coordinated with the Sullivan County Sheriff's Office to have Lieutenant Ford stop the vehicle and stage a canine unit. Ford stopped the Expedition for traffic violations around 2:00 a.m., finished a warning citation by about 2:10, and — after Trent and Hamilton declined consent — held them a minute or two until the dog arrived and alerted; the ensuing search found more than 18 kilograms of methamphetamine, a gun, and cash. The district court denied suppression.

## Issue
Whether Lieutenant Ford had reasonable suspicion to prolong the completed traffic stop for a dog sniff, where the facts establishing suspicion were known to the investigating agents rather than to Ford himself.

## Rule
Under *[[Rodriguez v. United States|Rodriguez]]*, prolonging a stop past its mission requires reasonable suspicion of additional wrongdoing, and the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] "includes the officer's own observations as well as information the officer receives from police reports, dispatch, and fellow officers." The court invoked the collective-knowledge doctrine: "Under the 'collective knowledge doctrine,' we may 'impute collective knowledge among multiple law enforcement agencies, even when the evidence demonstrates that the responding officer was wholly unaware of the specific facts that established reasonable suspicion.'" — slip op. at 4. ^pin-slip4

## Application
Although Lieutenant Ford himself may not have known every detail, the investigating officers collectively knew that Hamilton was running methamphetamine from Georgia, that Trent's rented vehicle had made two "turn-and-burn" Atlanta trips, that both had prior drug charges, and that the return route and license-plate cover fit trafficking patterns — knowledge imputed to Ford under the doctrine. Combined with Ford's own observation that the new rental's interior was heavily "trashed up," this supplied reasonable suspicion to extend the stop for the brief time until the canine arrived, so the one-to-two-minute prolongation was lawful.

## Conclusion
**Affirmed.** [[Common Legal Terms#per-curiam|Per curiam]] (McKeague, Readler, Bloomekatz, JJ.); the denial of suppression was upheld.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. **This is an unpublished, [[Common Legal Terms#per-curiam|per curiam]] disposition** ("NOT RECOMMENDED FOR PUBLICATION," 26a0207n.06) and is therefore non-precedential under Sixth Circuit I.O.P. 32.1(b) — persuasive only, notwithstanding the projected in-circuit authority weight. It is a clean illustration of the *[[Collective Knowledge and the Fellow-Officer Rule]]*: reasonable suspicion to extend a *[[Rodriguez v. United States|Rodriguez]]* stop may be supplied by the investigating team's collective knowledge, imputed to the officer on the scene.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key*

## Sources
- [*United States v. Mark Anthony Trent*, No. 25-5770, slip op. (6th Cir. 2026)](https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/) — pinpoint: slip op. at 4 (collective-knowledge doctrine imputes reasonable suspicion to the responding officer). Rule quote string-matched to the CL opinion text 2026-07-07. Unpublished 6th Cir. slip (26a0207n.06), non-precedential; no reporter cite (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "48d4907cb3ffc036", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Trent"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Trent", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Trent

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Trent",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Mark Anthony Trent",
    "case_name_short": "Trent",
    "case_name_full": "",
    "input_case_name": "United States v. Trent",
    "court": "6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": "2026-05-07",
    "year": 2026,
    "docket": "25-5770",
    "cluster_id": 10855903,
    "lead_opinion_id": 11323299,
    "sibling_ids": [],
    "absolute_url": "/opinion/10855903/united-states-v-mark-anthony-trent/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "coa",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 slip disposition. United States v. Mark Anthony Trent, 6th Cir. UNPUBLISHED No. 25-5770, decided 2026-05-07. CL cluster 10855903 Unpublished, citations[] empty (live-verified 2026-07-07). S9-REVERIFY FLAG: docket hand-reconstructed; CL cluster caption/date/court confirmed live, but the S9 panel should re-verify the docket number and the holding on the merits before certification.",
      "legs": [
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10855903/united-states-v-mark-anthony-trent/",
          "cite": "cluster 10855903 Unpublished, No. 25-5770, 2026-05-07, citations[] empty"
        },
        {
          "source": "Official court",
          "url": "https://www.opn.ca6.uscourts.gov/",
          "cite": "6th Cir. docket 71229065 (No. 25-5770), unpublished 2026-05-07"
        }
      ]
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
    "date_created": "2026-07-07T18:20:54Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "PRE-W5 audit: manually reconstructed identity from directly-verified CL cluster 10855903 (tool docket-collision on 25-5770 landed a wrong same-docket case; case_name rung did not surface Mark Anthony Trent). S9 re-verify."
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:20:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-trent--10855903",
      "to_record_id": "United States v. Trent",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Trent

```
                         NOT RECOMMENDED FOR PUBLICATION
                                File Name: 26a0207n.06

                                           No. 25-5770

                          UNITED STATES COURT OF APPEALS
                               FOR THE SIXTH CIRCUIT
                                                                                      FILED
                                                                                    May 07, 2026
UNITED STATES OF AMERICA,                              )                    KELLY L. STEPHENS, Clerk
                                                       )
       Plaintiff-Appellee,                             )
                                                       )    ON APPEAL FROM THE UNITED
v.                                                     )    STATES DISTRICT COURT FOR
                                                       )    THE EASTERN DISTRICT OF
MARK ANTHONY TRENT,                                    )    TENNESSEE
       Defendant-Appellant.                            )
                                                       )                                OPINION
                                                       )

Before: McKEAGUE, READLER, and BLOOMEKATZ, Circuit Judges.

       PER CURIAM. Mark Anthony Trent appeals the district court’s denial of his motion to

suppress evidence. As set forth below, we affirm the district court’s order denying his suppression

motion.

                                                I.

       Beginning in November 2023, law enforcement officers received information from

interviews with cooperating codefendants and other informants as well as from recorded jail calls

that Shaundra Hamilton was traveling to Georgia to obtain large quantities of methamphetamine

for distribution in northeast Tennessee. Based on that information, officers obtained a warrant to

“ping” the location of Hamilton’s cell phone and conducted surveillance at her residence in

Kingsport, Tennessee.

       On March 3, 2024, pings from Hamilton’s cell phone indicated that she traveled to the

Atlanta area for a short period of time and then came straight back—a “turn-and-burn” trip. That

evening, a black Ford Expedition arrived at Hamilton’s residence; officers identified Trent as the
No. 25-5770, United States v. Trent


renter of that vehicle. Criminal history checks revealed that both Trent and Hamilton had prior

drug charges.

       Officers saw Trent and Hamilton leave her residence in the Ford Expedition on March 12,

2024. Trent and Hamilton traveled through Tennessee on Interstate 75 to the Atlanta area and then

came straight back via a different route through North Carolina on Interstate 26. Special Agent

John Bulla with Homeland Security Investigations, who was following the Ford Expedition,

communicated with the Sullivan County Sheriff’s Office (SCSO) about initiating a traffic stop

once the vehicle entered Tennessee and positioning a canine unit in the area.

       Around 2:00 a.m. on March 13, 2024, Lieutenant William Ford with the SCSO stopped the

Ford Expedition for speeding, crossing the fog line, and having an illegal license plate cover. After

speaking with Hamilton, the passenger, and Trent, the driver, and gathering identification and

vehicle information from them, Lieutenant Ford returned to his cruiser, called for the canine unit,

ran a records check through the National Crime Information Center, and wrote a warning citation

for the traffic violations. Upon learning from dispatch that Trent and Hamilton were “clear,”

Lieutenant Ford finished writing the citation and then exited his cruiser around 2:10 a.m. When he

saw the canine unit pass on the other side of the interstate, Lieutenant Ford placed the citation and

other documents on the hood of his cruiser and approached the Ford Expedition to ask Trent and

Hamilton for consent to search the vehicle; they declined. Around 2:11 a.m., the canine unit

arrived. Lieutenant Ford directed Trent and Hamilton to exit the vehicle so that the dog could

perform a free air sniff; they refused. When Trent and Hamilton eventually exited the Ford

Expedition around 2:18 a.m., the dog performed an exterior sniff of the vehicle and alerted by

sitting at the driver door. The officers then searched the Ford Expedition and found 19 bags of




                                                -2-
No. 25-5770, United States v. Trent


methamphetamine with a total weight exceeding 18 kilograms, a loaded gun, cash, and drug

paraphernalia.

       A federal grand jury subsequently returned a multi-defendant, multi-count indictment

charging Trent with drug, money-laundering, and firearm offenses. Following his indictment,

Trent moved to suppress the evidence seized from the Ford Expedition on March 13, 2024, arguing

that the officers unreasonably extended the duration of the traffic stop beyond the time necessary

to address the alleged traffic violations. A magistrate judge conducted an evidentiary hearing and

issued a report recommending the denial of Trent’s suppression motion. Over Trent’s objection,

the district court adopted the magistrate judge’s report and recommendation and denied the motion.

       Trent entered a conditional guilty plea to possession with intent to distribute 50 grams or

more of methamphetamine, in violation of 21 U.S.C. § 841(a)(1) and (b)(1)(A), reserving his right

to appeal the district court’s denial of his suppression motion. See Fed. R. Crim. P. 11(a)(2). The

district court sentenced Trent to 218 months of imprisonment followed by five years of supervised

release.

                                                II.

       In this timely appeal, Trent challenges the district court’s denial of his motion to suppress

the evidence discovered during the March 13, 2024, traffic stop. On appeal from the denial of a

suppression motion, we review the district court’s factual findings for clear error and its legal

conclusions de novo. United States v. Guerrero, 168 F.4th 454, 459–60 (6th Cir. 2026). Whether

reasonable suspicion exists is a mixed question of law and fact, which we review de novo. United

States v. Taylor, 121 F.4th 590, 594 (6th Cir. 2024).

       The Fourth Amendment protects against “unreasonable searches and seizures” by

government officials. U.S. Const. amend. IV. A traffic stop is a reasonable seizure “where the


                                               -3-
No. 25-5770, United States v. Trent


police have probable cause to believe a traffic violation has occurred,” regardless of “the actual

motivations of the individual officers involved.” Whren v. United States, 517 U.S. 806, 810, 813

(1996). Trent does not dispute the legality of the initial traffic stop by Lieutenant Ford.

        Trent instead argues that Lieutenant Ford, after completing the purpose of the traffic stop,

unlawfully extended his detention without reasonable suspicion to conduct a dog sniff. An initially

lawful “traffic stop ‘can become unlawful if it is prolonged beyond the time reasonably required

to complete th[e] mission’ of issuing a warning ticket.” Rodriguez v. United States, 575 U.S. 348,

354–55 (2015) (alteration in original) (quoting Illinois v. Caballes, 543 U.S. 405, 407 (2005)).

“To prolong a traffic stop beyond its original ‘mission,’ police must have reasonable suspicion of

additional wrongdoing.” United Sates v. Jordan, 100 F.4th 714, 718 (6th Cir. 2024) (quoting

Rodriguez, 575 U.S. at 355). “A reasonable suspicion exists when, based on the totality of the

circumstances, a police officer has ‘a particularized and objective basis for suspecting the

particular person stopped of criminal activity.’” United States v. Smith, 140 F.4th 316, 319 (6th

Cir. 2025) (quoting United States v. Gross, 662 F.3d 393, 399 (6th Cir. 2011)). The totality of the

circumstances “includes the officer’s own observations as well as information the officer receives

from police reports, dispatch, and fellow officers.” United States v. McCallister, 39 F.4th 368,

374 (6th Cir. 2022). “It also ‘involves commonsense judgments and inferences about human

behavior, as well as inferences the officer may draw based on his experience and specialized

training.’” Taylor, 121 F.4th at 595 (quoting McCallister, 39 F.4th at 374).

        Lieutenant Ford’s mission effectively ended at approximately 2:10 a.m. when he exited his

cruiser after writing the citation. But contrary to Trent’s argument, Lieutenant Ford had reasonable

suspicion of additional wrongdoing to prolong the traffic stop until the canine unit arrived a minute

or two later.


                                                -4-
No. 25-5770, United States v. Trent


       Under the “collective knowledge doctrine,” we may “impute collective knowledge among

multiple law enforcement agencies, even when the evidence demonstrates that the responding

officer was wholly unaware of the specific facts that established reasonable suspicion.” United

States v. Lyons, 687 F.3d 754, 766 (6th Cir. 2012). At the time of initial traffic stop, law

enforcement officers had received information from multiple sources that Hamilton was traveling

to and from Georgia to obtain large quantities of methamphetamine for distribution in northeast

Tennessee. Officers had observed Trent’s rental vehicle at Hamilton’s residence, and the pings

from her cell phone indicated that Trent and Hamilton had made “turn-and-burn” trips to the

Atlanta area in that vehicle on March 3, 2024, and again on March 12, 2024. Special Agent Bulla

testified that drug traffickers often use rental vehicles and license plate covers, like the one on the

Ford Expedition, and take different routes, like Trent and Hamilton did on their return trip, to avoid

detection by law enforcement. Special Agent Bulla also knew about Trent’s and Hamilton’s prior

drug charges. As for Lieutenant Ford’s own observations, he testified that the Ford Expedition’s

interior was “very trashed up for it to be a brand new vehicle” but “normal” for a vehicle involved

in drug trafficking.

       Trent argues that reasonable suspicion to prolong the traffic stop was lacking because law

enforcement officers did not directly observe him engaging in any drug-trafficking activities.

According to Trent, the trip to the Atlanta area “gave rise to no more than a hunch of criminal

activity.” As the district court pointed out, direct observation of drug-trafficking activities is

relevant but not required to establish reasonable suspicion. See, e.g., United States v. Williams, 68

F.4th 304, 308–09 (6th Cir. 2023). Based on the totality of the circumstances, Lieutenant Ford

had reasonable suspicion to prolong the traffic stop to conduct a dog sniff.




                                                 -5-
No. 25-5770, United States v. Trent


                                            III.

       For these reasons, we AFFIRM the district court’s denial of Trent’s motion to suppress

evidence.




                                            -6-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Tuggle.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Tuggle"
type: case
citation: "4 F.4th 505 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, Seventh Circuit"
court_level: coa
circuit: 7th
year: 2021
date_decided: 2021-07-14
docket: 20-2352
authority_weight: "Binding in-circuit — 7th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-07-14
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Tuggle
  varies_by_point: false
  scope_note: "Issue of first impression; courts split on long-term pole-camera surveillance."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4899735/united-states-v-travis-tuggle/"
  cluster_id: 4899735
  opinion_id: 4703514
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Related (cross-doctrine — pole camera)"
related: ["[[California v. Ciraolo]]", "[[California v. Greenwood]]", "[[Carpenter v. United States]]", "[[United States v. Jones]]"]
aliases: ["United States v. Tuggle (7th Cir. 2021)", "United States v. Travis Tuggle"]
tags: ["case", "fourth-amendment", "plain-view", "pole-camera", "surveillance", "mosaic-theory", "seventh-circuit"]
holding: "Long-term pole-camera surveillance of a home's exterior did not violate the Fourth Amendment under existing doctrine, BUT the court…"
lake:
  record_id: United States v. Tuggle
  status: verified
  projected_at: 2026-07-06
---

# United States v. Tuggle

*4 F.4th 505 (7th Cir. 2021)* · U.S. Court of Appeals, Seventh Circuit · **Binding in-circuit — 7th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Suspecting Travis Tuggle of drug trafficking, the government surveilled him for eighteen months without a warrant, installing three cameras on public property that captured the exterior of his home. When the footage was used to prosecute him, Tuggle moved to suppress it as a Fourth Amendment violation. Whether prolonged warrantless pole-camera surveillance of a home's exterior is a "search" was an issue of first impression in the Seventh Circuit.

## Issue
Whether the warrantless use of pole cameras to observe the exterior of a home on a long-term basis amounts to a "search" under the Fourth Amendment.

## Rule
No, under current doctrine: "we hold that the extensive pole camera surveillance in this case did not constitute a search under the current understanding of the Fourth Amendment." — *United States v. Tuggle*, 4 F.4th 505 (7th Cir. 2021) (slip op., at 5). ^pin-op5

The cameras captured only what was exposed to public view from a place the government was lawfully entitled to occupy. The court declined to adopt the "mosaic theory" — that aggregated long-term surveillance becomes a search — holding current Supreme Court precedent did not support it.

## Application
The three pole cameras recorded only the outside of Tuggle's home — areas exposed to public view — from public property where officers were lawfully entitled to be. Even aggregated over eighteen months, that surveillance was not a search under existing Supreme Court precedent, and the court would not treat the accumulated footage as a search under a mosaic theory. The footage was therefore admissible against Tuggle.

## Conclusion
The warrantless long-term pole-camera surveillance of the home's exterior did not constitute a Fourth Amendment search; the Seventh Circuit affirmed. The court nonetheless flagged at length the privacy dangers of pervasive aggregated surveillance, inviting legislative and further judicial attention.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 7th Cir.**
- No negative treatment within the circuit. *Tuggle* joins most federal courts of appeals in holding that pole-camera surveillance of a residence's exterior is not a search, while expressly flagging the unresolved tension with the [[Carpenter v. United States]] / [[United States v. Jones]] mosaic theory for long-term digital surveillance. Courts remain split on the question.

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*
- [[Aerial and Enhanced Surveillance]] — *Related (cross-doctrine — pole camera)*

## Sources
- *United States v. Tuggle*, 4 F.4th 505 (7th Cir. 2021) — https://www.courtlistener.com/opinion/4899735/united-states-v-travis-tuggle/ — pinpoint given as slip-opinion page (CourtListener carries the slip opinion; cluster 4899735 → opinion 4703514).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6c7c1f863b93ac79", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Tuggle"}, "payload": {"all": [{"cite": "4 F.4th 505", "page": "505", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}], "display": "4 F.4th 505", "official": {"cite": "4 F.4th 505", "page": "505", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "4"}, "official_selection_present": true, "record_id": "United States v. Tuggle"}}
{"assertion_id": "b75a39b737a3122f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op5", "record_id": "United States v. Tuggle"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op5", "pinpoint_status": "slip-only", "quote": "under the Fourth Amendment. ## Rule No, under current doctrine:", "quote_fidelity": "mismatch", "record_id": "United States v. Tuggle", "star_marker": null}}
{"assertion_id": "7c3482dbac0646a9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Tuggle"}, "payload": {"as_of_content": "2021-07-14", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Tuggle", "scope_note": "Issue of first impression; courts split on long-term pole-camera surveillance.", "varies_by_point": false}}
```

### lake record — United States v. Tuggle

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Tuggle",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Travis Tuggle",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Tuggle",
    "court": "U.S. Court of Appeals, Seventh Circuit",
    "court_id": "ca7",
    "court_level": "coa",
    "circuit": "7th",
    "state": null,
    "date_decided": "2021-07-14",
    "year": 2021,
    "docket": "20-2352",
    "cluster_id": 4899735,
    "lead_opinion_id": 4703514,
    "sibling_ids": [
      4703514
    ],
    "absolute_url": "/opinion/4899735/united-states-v-travis-tuggle/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "4 F.4th 505",
      "volume": "4",
      "reporter": "F.4th",
      "page": "505",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "4 F.4th 505",
        "volume": "4",
        "reporter": "F.4th",
        "page": "505",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "4 F.4th 505",
    "official_selection": {
      "court_class": "coa",
      "selected": "4 F.4th 505",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op5",
      "page": null,
      "quote": "under the Fourth Amendment. ## Rule No, under current doctrine:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-07-14",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Tuggle",
    "varies_by_point": false,
    "scope_note": "Issue of first impression; courts split on long-term pole-camera surveillance.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Elizabeth Alicea v. County of Cook",
          "cluster_id": 9452942,
          "cite": [
            "88 F.4th 1209"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis",
          "cluster_id": 7441167,
          "cite": [
            "41 F.4th 732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hay",
          "cluster_id": 9485331,
          "cite": [
            "95 F.4th 1304"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Moore-Bush",
          "cluster_id": 6476395,
          "cite": [
            "36 F.4th 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harry",
          "cluster_id": 10352104,
          "cite": [
            "130 F.4th 342"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pondexter-Moore v. District of Columbia Housing Authority",
          "cluster_id": 10830726,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lane",
          "cluster_id": 10796201,
          "cite": [
            "347 Or. App. 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Demetrius Green",
          "cluster_id": 10652265,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rolando Antuain Williamson",
          "cluster_id": 10332827,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sidor",
          "cluster_id": 10145062,
          "cite": [
            "558 P.3d 621"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Alaska v. John William Mckelvey III",
          "cluster_id": 9485153,
          "cite": [
            "544 P.3d 632"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Tuggle:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4703514) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca7)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(4703514)",
        "reviewed": 11,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 11,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4703514)",
        "reviewed": 9,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 9,
        "triage_read": 0,
        "triage_snippet_classified": 9
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4703514)",
    "indexed_citing_opinions": 11,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4703514,
        "count": 11,
        "count_source": "search"
      }
    ],
    "citation_count": 16,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-tuggle.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 11,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4703514,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 152441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 204000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 489983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 672897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 777810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 781890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 1027565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 2709321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 2739791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 3173994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4158218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4176845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4453948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4459782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4549954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 4681147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8312922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8410718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8414506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8704503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 8710762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9429102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9429751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9430504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9431296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9434104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9435359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9441476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9493097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9501842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9558712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9804255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9821499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4703514,
        "cited_id": 9878508,
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
    "date_created": "2026-07-06T03:13:56Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:15:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:14:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Tuggle

```
                               In the

    United States Court of Appeals
                 For the Seventh Circuit
                     ____________________
No. 20-2352
UNITED STATES OF AMERICA,
                                                   Plaintiff-Appellee,
                                 v.

TRAVIS TUGGLE,
                                               Defendant-Appellant.
                     ____________________

         Appeal from the United States District Court for the
                    Central District of Illinois.
            No. 16-cr-20070 — James E. Shadid, Judge.
                     ____________________

       ARGUED MAY 12, 2021 — DECIDED JULY 14, 2021
                ____________________

   Before FLAUM, HAMILTON, and BRENNAN, Circuit Judges.
    FLAUM, Circuit Judge. One day, in a not-so-distant future,
millions of Americans may well wake up in a smart-home-
dotted nation. As they walk out their front doors, cameras in-
stalled on nearby doorbells, vehicles, and municipal traﬃc
lights will sense and record their movements, documenting
their departure times, catching glimpses of their phone
screens, and taking note of the people that accompany them.
2                                                   No. 20-2352

    These future Americans will traverse their communities
under the perpetual gaze of cameras. Camera-studded streets,
highways, and transit networks will generate precise infor-
mation about each vehicle and its passengers, for example, re-
cording peoples’ everyday routes and deviations therefrom.
Upon arrival at their workplaces, schools, and appointments,
cameras on buildings will observe their attire and belongings
while body cameras donned on the vests of police and secu-
rity oﬃcers will record snippets of face-to-face or phone con-
versations. That same network of cameras will continue to
capture Americans from many angles as they run errands and
rendezvous to various social gatherings. By the end of the
day, millions of unblinking eyes will have discerned Ameri-
cans’ occupations and daily routines, the people and groups
with whom they associate, the businesses they frequent, their
recreational activities, and much more.
    The setting described above is not yet a total reality. None-
theless, we are steadily approaching a future with a constella-
tion of ubiquitous public and private cameras accessible to the
government that catalog the movements and activities of all
Americans. Foreseeable expansion in technological capabili-
ties and the pervasive use of ever-watching surveillance will
reduce Americans’ anonymity, transforming what once
seemed like science ﬁction into fact. Constitutionally and stat-
utorily mandated protections stand as critical bulwarks in
preserving individual privacy vis-à-vis the government in
this surveillance society. To date, however, such measures
have been challenged by the pace of technological develop-
ments.
    The Framers of the Constitution sought “to place obstacles
in the way of a too permeating police surveillance.” United
No. 20-2352                                                   3

States v. Di Re, 332 U.S. 581, 595 (1948). That central aim ani-
mated their eﬀorts, embodied in the Fourth Amendment to
the Constitution, to preserve the “right of the people to be se-
cure in their persons, houses, papers, and eﬀects, against un-
reasonable searches and seizures.” For most of our country’s
history, the concept of a “search” was tied to common-law
trespass, in other words, physical touch. Over time, however,
the evolution of technology raised complicated questions re-
garding the appropriate interpretation and scope of the
Fourth Amendment. Chief among those questions: What con-
stitutes a search in a digital society whose technology empow-
ers near-perfect surveillance without the need for physical
touch?
    To grapple with the enhanced technological capacity of
law enforcement investigations, the Supreme Court followed
Justice Harlan’s concurrence in Katz v. United States, 389 U.S.
347 (1967), and expanded its understanding of Fourth
Amendment protections. The resulting Katz test, containing
subjective and objective components, instructs courts to as-
sess ﬁrst whether a person has “exhibited an actual (subjec-
tive) expectation of privacy’” and second, whether that “ex-
pectation be one that society is prepared to recognize as ‘rea-
sonable.’” Id. at 361 (Harlan, J., concurring).
    Despite its best intentions, this expectations-based Katz
test has paved the way for a perilous circularity for new tech-
nology. Speciﬁcally, our current formulation of a Fourth
Amendment search often turns on whether a used technology
becomes widespread. Stated diﬀerently, as society’s uptake of
a new technology waxes—cars, GPS devices, cameras, and the
Internet come to mind—expectations of privacy in those tech-
nologies wane. In today’s interconnected, globalized, and
4                                                  No. 20-2352

increasingly digital world, for example, Americans largely ac-
cept that cell phones will track their locations, their Internet
usage will leave digital footprints, and ever-watching ﬁxed
cameras will monitor their movements. These evolving expec-
tations thus continually undermine themselves.
    As long as the government moves discreetly with the
times, its use of advanced technologies will likely not breach
society’s reconstituted (non)expectations of privacy. The up-
shot: the Katz test as currently interpreted may eventually af-
ford the government ever-wider latitude over the most so-
phisticated, intrusive, and all-knowing technologies with
lessening constitutional constraints.
    These observations bring us to the instant case, a harbin-
ger of the challenge to apply Fourth Amendment protections
to accommodate forthcoming technological changes. Suspect-
ing defendant Travis Tuggle’s involvement in drug traﬃck-
ing, the government surveilled him for eighteen months with-
out a warrant. The oﬃcers installed three cameras on public
property that captured the outside of Tuggle’s home. When
the government used the resulting footage to prosecute Tug-
gle, Tuggle moved to suppress the footage as violative of his
Fourth Amendment right.
    Tuggle’s case presents an issue of ﬁrst impression for this
Court: whether the warrantless use of pole cameras to observe
a home on either a short- or long-term basis amounts to a
“search” under the Fourth Amendment. The answer—and
even how to reach it—is the subject of disagreement among
our sister circuits and counterparts in state courts. Their di-
vergent answers reﬂect the complexity and uncertainty of the
prolonged use of this technology and others like it. Neverthe-
less, most federal courts of appeals that have weighed in on
No. 20-2352                                                   5

the issue have concluded that pole camera surveillance does
not constitute a Fourth Amendment search.
    Ultimately, bound by Supreme Court precedent and with-
out other statutory or jurisprudential means to cabin the gov-
ernment’s surveillance techniques presented here, we hold
that the extensive pole camera surveillance in this case did not
constitute a search under the current understanding of the
Fourth Amendment. In short, the government’s use of a tech-
nology in public use, while occupying a place it was lawfully
entitled to be, to observe plainly visible happenings, did not
run afoul of the Fourth Amendment. Therefore, we aﬃrm the
district court’s denial of Tuggle’s motion to suppress.

                      I.   Background

    Between 2013 and 2016, several law enforcement agencies
investigated a large methamphetamine distribution conspir-
acy in central Illinois that resulted in Tuggle’s prosecution.
The focus of this appeal is the government’s warrantless use
of three video cameras affixed to nearby utility poles to mon-
itor Tuggle’s residence.
    The government installed three cameras on public prop-
erty that viewed Tuggle’s home. Agents mounted two cam-
eras on a pole in an alley next to his residence and a third on
a pole one block south of the other two cameras. The first two
cameras viewed the front of Tuggle’s home and an adjoining
parking area. The third camera also viewed the outside of his
home but primarily captured a shed owned by Tuggle’s co-
conspirator and codefendant, Joshua Vaultonburg.
  Together, the three cameras captured nearly eighteen
months of footage by recording Tuggle’s property between
6                                                 No. 20-2352

2014 and 2016. Law enforcement agents installed the first
camera in August 2014, the second in December 2015, and the
third in September 2015. The officers left the three cameras on
their respective poles until March 2016.
     The cameras offered several advantages to the govern-
ment’s investigation of the drug conspiracy. While in use, the
cameras recorded around the clock. Rudimentary lighting
technology improved the quality of overnight footage, alt-
hough the cameras did not have infrared or audio capabilities.
Law enforcement agents could also remotely zoom, pan, and
tilt the cameras and review the camera footage in real time,
though the footage captured only the exterior of Tuggle’s
house. While officers frequently monitored the live feed dur-
ing business hours, they could later review all the footage,
which the government stored at the Federal Bureau of Inves-
tigation office in Springfield, Illinois. More generally, the
cameras had the practical advantage of enabling the govern-
ment to surveil Tuggle’s home without conspicuously de-
ploying agents to perform traditional visual or physical sur-
veillance on the lightly traveled roads of Tuggle’s residential
neighborhood.
    The cameras provided substantial video evidence that
supported the government’s eventual indictment of Tuggle
(and others). The officers tallied over 100 instances of what
they suspected were deliveries of methamphetamine to Tug-
gle’s residence. Camera footage depicted individuals arriving
at Tuggle’s home, carrying various items inside, and leaving
only with smaller versions of those items or sometimes noth-
ing at all. After these alleged “drops,” different individuals
would soon arrive, enter the home, and purportedly pay for
and pick up methamphetamine. Several witnesses
No. 20-2352                                                    7

corroborated these activities. Further evidencing a drug oper-
ation, the recordings showed Tuggle carrying items to Vaul-
tonburg’s shed across the street. All told, the investigating of-
ficers determined that Tuggle’s conspiracy distributed over
twenty kilograms of highly pure methamphetamine.
    Relying heavily on the video evidence, the officers secured
and executed search warrants on several locations, including
Tuggle’s house. A grand jury subsequently indicted him on
two counts: (1) a violation of 21 U.S.C. § 841(a)(1) and
(b)(1)(A) for conspiring to distribute, and possess with intent
to distribute, at least 50 grams of methamphetamine and at
least 500 grams of a mixture containing methamphetamine,
and (2) a violation of 21 U.S.C. § 856(a)(1) for maintaining a
drug-involved premises.
    Before trial, Tuggle moved to suppress the evidence ob-
tained from the pole cameras, arguing that the use of the cam-
eras constituted a warrantless search in violation of the
Fourth Amendment. The district court denied the motion in a
written opinion explaining its view that the camera usage did
not constitute a search. Thereafter, Tuggle twice moved for
the district court to reconsider, but the court denied both mo-
tions on grounds that they raised no novel arguments. The
day before trial, Tuggle entered a conditional guilty plea,
pleading guilty to both counts but reserving his right to ap-
peal the court’s denials of his motions to suppress. The district
court then sentenced him to 360 months’ imprisonment on
Count 1 and a concurrent 240 months’ imprisonment on
Count 2.
   This timely appeal followed.
8                                                    No. 20-2352

                      II.   Discussion

    The issue before us on appeal is whether the district court
correctly denied Tuggle’s motion to suppress. That issue calls
for a “dual standard of review” under which “we review legal
conclusions de novo but findings of fact for clear error.”
United States v. Edgeworth, 889 F.3d 350, 353 (7th Cir. 2018) (ci-
tation omitted).
    The Fourth Amendment provides, in part, for “[t]he right
of the people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” U.S.
Const. amend. IV. “Warrantless searches ‘are per se unreason-
able under the Fourth Amendment—subject only to a few
specifically established and well-delineated exceptions.’”
United States v. Edwards, 769 F.3d 509, 513 (7th Cir. 2014)
(quoting Arizona v. Gant, 556 U.S. 332, 338 (2009)). The gov-
ernment did not seek a warrant for the cameras here, and no
exception to the warrant requirement applies, so the diposi-
tive question is whether a Fourth Amendment search oc-
curred.
    The Supreme Court has developed two distinct paths to
identify a search: “[a] search occurs either when the govern-
ment physically intrudes without consent upon ‘a constitu-
tionally protected area in order to obtain information,’ or
‘when an expectation of privacy that society is prepared to
consider reasonable is infringed.’” United States v. Thompson,
811 F.3d 944, 948 (7th Cir. 2016) (some internal quotation
marks and citations omitted) (first quoting United States v.
Jones, 565 U.S. 400, 407 (2012); and then quoting United States
v. Karo, 468 U.S. 705, 712 (1984)). The first path, a physical in-
trusion, is not relevant because the parties agree that the
No. 20-2352                                                    9

government did not physically intrude on Tuggle’s property
by attaching the cameras to the utility poles on public prop-
erty.
    We therefore focus on the second path to finding a search,
a government infringement upon an expectation of privacy
that society is prepared to consider reasonable. This path de-
rives from Justice Harlan’s famous concurrence in Katz, which
determined that “a person has a constitutionally protected
reasonable expectation of privacy” where that person “ex-
hibit[s] an actual (subjective) expectation of privacy … that
society is prepared to recognize as ‘reasonable.’” 389 U.S. at
360–61 (Harlan, J., concurring); see also Smith v. Maryland,
442 U.S. 735, 740 (1979) (adopting Justice Harlan’s Katz test).
The Supreme Court later clarified that “Katz posits a two-part
inquiry: first, has the individual manifested a subjective ex-
pectation of privacy in the object of the challenged search?
Second, is society willing to recognize that expectation as rea-
sonable?” California v. Ciraolo, 476 U.S. 207, 211 (1986). As
“[t]he party seeking suppression,” Tuggle “bears the burden
of establishing that he had a reasonable expectation of privacy
in what was searched.” United States v. Scott, 731 F.3d 659, 663
(7th Cir. 2013).
    On appeal, Tuggle presents two different, but related, ar-
guments that the government’s use of the three pole cameras
to monitor the activities in front of and outside his house con-
stituted a search under the Fourth Amendment. First, he ar-
gues that the warrantless pole camera surveillance of his res-
idence, irrespective of the length of that surveillance use, vio-
lated his Fourth Amendment rights. Second, he argues—rely-
ing on the mosaic theory—that the “long-term, warrantless
surveillance over a period of approximately eighteen
10                                                No. 20-2352

months” amounted to a Fourth Amendment violation. We
consider each argument in turn.
      A. The Isolated Use of Cameras
    Tuggle first frames the issue as “whether the use of war-
rantless pole camera surveillance of Mr. Tuggle’s private res-
idence violated his Fourth Amendment rights?” For present
purposes, we will consider only whether the isolated use of
pole cameras—by which we mean the use of pole cameras ir-
respective of the length of that use—constitutes a Fourth
Amendment search. In other words, we ask: Did the Fourth
Amendment preclude law enforcement officers from the iso-
lated use of pole cameras on public property without a war-
rant to observe Tuggle’s private home?
    Framed as such, the answer is clearly no. At the outset, we
note that Tuggle likely has not, at Katz’s first prong, “exhib-
ited an actual (subjective) expectation of privacy” in the go-
ings-on outside of his home. Katz, 389 U.S. at 361 (Harlan, J.,
concurring). Nothing in the record suggests that Tuggle
erected any fences or otherwise tried to shield his yard or
driveway from public view, which might have signaled he
feared the wandering eye or camera lens on the street. We
therefore do not confront the more challenging situation in
which the government intentionally places cameras to see over
a fence to observe a private residence in a manner unavailable
to a ground-level passerby. See generally United States v. Cue-
vas-Sanchez, 821 F.2d 248, 251 (5th Cir. 1987) (concluding that
defendant “manifested the subjective expectation of privacy
in his backyard” because “he erected fences around [it],
screening the activity within from views of casual observers,”
and “the area monitored by the camera fell within the curti-
lage of his home, an area protected by traditional fourth
No. 20-2352                                                      11

amendment analysis”). Nevertheless, courts have not uni-
formly applied the subjective prong of the Katz test, and some
legal scholars have called its significance in resolving cases
into question. See generally Orin S. Kerr, Katz Has Only One
Step: The Irrelevance of Subjective Expectations, 82 U. Chi. L. Rev.
113, 113 (2015) (arguing that “the majority of judicial opinions
applying Katz do not even mention the subjective-expecta-
tions test; opinions that mention the test usually do not apply
it; and even when courts apply it, the test makes no difference
to the results”). Thus, we primarily focus our attention on
Katz’s objective inquiry.
    As to that objective prong—those privacy expectations so-
ciety is willing to accept as reasonable—“[t]he expectation of
privacy does not extend to ‘[w]hat a person knowingly ex-
poses to the public, even in his own home or office.’” Thomp-
son, 811 F.3d at 949 (quoting Katz, 389 U.S. at 351). The Su-
preme Court has made clear that “[t]he Fourth Amendment
protection of the home has never been extended to require
law enforcement officers to shield their eyes when passing by
a home on public thoroughfares.” Ciraolo, 476 U.S. at 213; see
also Kyllo v. United States, 533 U.S. 27, 32 (2001) (“[V]isual ob-
servation is no ‘search’ at all.”); California v. Greenwood,
486 U.S. 35, 41 (1988) (“[P]olice cannot reasonably be expected
to avert their eyes from evidence of criminal activity that
could have been observed by any member of the public.”). We
have also observed that home dwellers do not generally enjoy
a “reasonable expectation of privacy in [their] driveway[s].”
See United States v. Evans, 27 F.3d 1219, 1228–29 (7th Cir. 1994)
(collecting cases); see also United States v. French, 291 F.3d 945,
955 (7th Cir. 2002) (holding defendant had “no reasonable ex-
pectation of privacy in the driveway and gravel walkways”
leading to his home).
12                                                  No. 20-2352

    In this case, Tuggle knowingly exposed the areas captured
by the three cameras. Namely, the outside of his house and
his driveway were plainly visible to the public. He therefore
did not have an expectation of privacy that society would be
willing to accept as reasonable in what happened in front of
his home. See Evans, 27 F.3d at 1228. The Fourth Amendment
accordingly did not require officers to “shield their eyes” (or
their cameras) when passing by Tuggle’s “home on public
thoroughfares.” See Ciraolo, 476 U.S. at 213.
   Tuggle’s argument that the cameras transformed other-
wise lawful visual surveillance into unconstitutional techno-
logical surveillance does not undermine our conclusion that
the isolated use of pole cameras here did not constitute a
search. Specifically, Tuggle argues that “[w]hile the ‘fruits’ of
the pole cameras could have been achieved by traditional vis-
ual or physical surveillance, the use of technology change[d]
the reasonableness of the expectation of privacy.” See Jones,
565 U.S. at 412 (“It may be that achieving the same result
through electronic means, without an accompanying tres-
pass, is an unconstitutional invasion of privacy ….”).
    To be sure, the Supreme Court has cautioned that the gov-
ernment’s use of some technologies falls within the ambit of
the Fourth Amendment, but the Court has also affirmed that
“[n]othing in the Fourth Amendment prohibit[s] the police
from augmenting the sensory faculties bestowed upon them
at birth with such enhancement as science and technology af-
forded them in” certain instances. United States v. Knotts,
460 U.S. 276, 282 (1983).
   The prototypical example of impermissible technology for
Fourth Amendment purposes is the government’s use of a
thermal imaging device that detects relative heat levels within
No. 20-2352                                                   13

a residence. The Supreme Court held the use of the device to
be an unlawful search in violation of the Fourth Amendment
in Kyllo v. United States. 533 U.S. at 40. While the thermal im-
aging device did not physically intrude on the defendant’s
property, the Court expressed concern about “leav[ing] the
homeowner at the mercy of advancing technology.” Id. at 35.
The Court therefore held that governmental use of “a device
that is not in general public use, to explore details of the home
that would previously have been unknowable without phys-
ical intrusion,” constitutes a Fourth Amendment search “and
is presumptively unreasonable without a warrant.” Id. at 40.
    Despite the Kyllo standard, the Supreme Court has rou-
tinely approved of law enforcement officers’ use of cameras
to aid investigations. In Dow Chemical Co. v. United States,
476 U.S. 227 (1986), the Supreme Court held “that the taking
of aerial photographs of [a 2,000-acre] industrial plant com-
plex from navigable airspace is not a search prohibited by the
Fourth Amendment.” Id. at 239. The Court acknowledged that
“the technology of photography has changed in this century,”
id. at 231, and said:
       It may well be … that surveillance of private
       property by using highly sophisticated surveil-
       lance equipment not generally available to the
       public, such as satellite technology, might be
       constitutionally proscribed absent a warrant.
       But the photographs here are not so revealing of
       intimate details as to raise constitutional con-
       cerns. Although they undoubtedly give [the
       government] more detailed information than
       naked-eye views, they remain limited to an out-
       line of the facility’s buildings and equipment.
14                                                  No. 20-2352

Id. at 238. To that end, the Court noted that “[t]he mere fact
that human vision is enhanced somewhat, at least to the de-
gree here, does not give rise to constitutional problems” be-
cause the aerial photography cameras did not raise the “far
more serious questions” presented by a device that could
“penetrate walls or windows so as to hear and record confi-
dential discussions.” Id. at 238–39.
    On the same day it issued Dow Chemical, the Supreme
Court held in California v. Ciraolo that law enforcement did not
violate the Fourth Amendment when it observed and photo-
graphed the defendant’s marijuana plants while flying 1,000
feet overhead in a private plane. 476 U.S. at 209–10. The Court
explained that although the defendant may have demon-
strated a subjective expectation of privacy by erecting fences,
society was not prepared to accept that expectation as reason-
able because the government surveilled “within public navi-
gable airspace … in a physically nonintrusive manner.” Id. at
213. In other words, “[a]ny member of the public flying in this
airspace who glanced down could have seen everything that
these officers observed.” Id. at 213–14. The Court did not even
consider the impact of the camera—thus assuming it was en-
tirely permissible for officers to use cameras in that place in
which they were lawfully entitled to be.
   Despite the prevalence of cameras in today’s society, we
have not identified in our own precedent any cases in which
we squarely evaluated the constitutionality of the govern-
ment’s use of remote cameras, pole cameras, or the like, to aid
law enforcement surveillance. We have, however, acknowl-
edged the commonplace role cameras have in our society. Cf.
United States v. Paxton, 848 F.3d 803, 812 (7th Cir. 2017) (“[W]e
are fast approaching a day when police interactions with
No. 20-2352                                                                  15

civilians, including detainees, will be recorded from begin-
ning to end, and for a variety of important ends.”). Thus, the
question of whether the isolated use of pole cameras, without
a warrant, on public property is constitutional is an issue of
first impression. Our sister circuits, including the Fourth and
the Tenth Circuits, that have considered governmental reli-
ance on cameras to observe the exteriors of private homes
have held such uses to be constitutional. 1
    We likewise conclude that, under a straightforward appli-
cation of Kyllo, the isolated use of pole cameras here did not
run afoul of Fourth Amendment protections. Today, cameras
are in “general public use.” Kyllo, 533 U.S. at 40. Now more
than ever, cameras are ubiquitous, found in the hands and
pockets of virtually all Americans, on the doorbells and en-
trances of homes, and on the walls and ceilings of businesses.
See Carpenter v. United States, 138 S. Ct. 2206, 2220 (2018) (de-
clining to “call into question conventional surveillance tech-
niques and tools, such as security cameras” (emphasis added));
Paxton, 848 F.3d at 812. To that point, if some thirty years ago
extensive aerial photography of a 2,000-acre industrial prop-
erty, see Dow Chem., 476 U.S. at 229, or of marijuana plants oth-
erwise concealed at ground level, see Ciraolo, 476 U.S. at 209,
did not qualify as Fourth Amendment searches, then certainly


    1 See, e.g., United States v. Vankesteren, 553 F.3d 286, 287 (4th Cir. 2009)
(holding the government had not violated the defendant’s Fourth Amend-
ment rights through use of “a hidden, fixed-range, motion-activated video
camera placed in the [defendant’s] open fields”); United States v. Jackson,
213 F.3d 1269, 1282 (10th Cir.) (holding that “evidence obtained from the
video cameras installed on the telephone poles and the recordings made
in the undercover FBI car were not introduced in violation of … the Fourth
Amendment”), vacated on other grounds, 531 U.S. 1033 (2000).
16                                                  No. 20-2352

ground-level video footage of an unobstructed home from a
public vantage point is not a search.
    While the video cameras in this case “undoubtedly g[a]ve
[the government] more detailed information than naked-eye
views,” they did not do so to a degree that “give[s] rise to con-
stitutional problems.” See Dow Chem., 476 U.S. at 238. The gov-
ernment only used the cameras to identify who visited Tug-
gle’s house and what they carried, all things that a theoretical
officer could have observed without a camera. Cf. Thompson,
811 F.3d at 950 (“The video cameras in this case captured
nothing more than what the informant could see with his na-
ked eye.”). That the government could replay the footage and
remotely control the camera does not affect our analysis be-
cause these features are a far cry from the “highly sophisti-
cated surveillance equipment not generally available to the
public” that animated the Dow Chemical decision. 476 U.S. at
238. The cameras did not “penetrate walls or windows so as
to hear and record confidential” information, id. at 239, nor
did they “explore details of the home that would previously
have been unknowable without physical intrusion,” Kyllo,
553 U.S. at 40.
    In sum, the government used a commonplace technology,
located where officers were lawfully entitled to be, and cap-
tured events observable to any ordinary passerby. The gov-
ernment did not invade an expectation of privacy that society
would be prepared to accept as reasonable. Accordingly, the
isolated use of pole cameras here did not constitute a Fourth
Amendment search.
No. 20-2352                                                    17

       B. The Prolonged, Round-the-Clock Use of Cameras
    The more challenging question is Tuggle’s second theory
of a Fourth Amendment violation: that the prolonged and un-
interrupted use of those cameras constituted a search. Tuggle
characterizes this theory in two ways. First, he argues more
generally that the “long-term use of the pole cameras over an
extended period of approximately eighteen months violates
the Fourth Amendment.” Second, he asserts that “[a]pplying
the mosaic theory, the use of warrantless pole cameras con-
tinuously for over [eighteen] months is unconstitutional un-
der the Fourth Amendment.” While framed differently, both
Tuggle’s theories functionally ask whether the mosaic theory
supports finding a Fourth Amendment search here. To an-
swer that question, we will begin by explaining the mosaic
theory and noting that while the theory has gained some ju-
dicial traction the Supreme Court has yet to affirmatively re-
quire lower courts to apply it. Then, we will outline how other
courts have disagreed over whether prolonged pole camera
surveillance constitutes a Fourth Amendment search. Draw-
ing on those discussions—and noting our reservations—we
will finally address why the prolonged use of pole cameras
here did not constitute a Fourth Amendment search.
          1. The Mosaic Theory Generally
    In its simplest form, the mosaic theory attempts to capture
the idea that the “government can learn more from a given
slice of information if it can put that information in the context
of a broader pattern, a mosaic.” Matthew B. Kugler & Lior Ja-
cob Strahilevitz, Actual Expectations of Privacy, Fourth Amend-
ment Doctrine, and the Mosaic Theory, 2015 Sup. Ct. Rev. 205,
205 (2015). Thus, it “holds that, when it comes to people’s rea-
sonable expectations of privacy, the whole is greater than the
18                                                      No. 20-2352

sum of its parts.” Id.; see also David Gray & Danielle Keats Cit-
ron, A Shattered Looking Glass: The Pitfalls and Potential of the
Mosaic Theory of Fourth Amendment Privacy, 14 N.C. J. L. &
Tech. 381, 415 (2013) (“The mosaic theory …. recognizes that,
although a collection of dots is sometimes nothing more than
a collection of dots, some collections of dots, when assessed
holistically, are A Sunday Afternoon on the Island of La Grande
Jatte.”); Orin S. Kerr, The Mosaic Theory of the Fourth Amend-
ment, 111 Mich. L. Rev. 311, 313 (2012). For present purposes,
we ground our discussion in these high-level articulations of
the mosaic theory although we note that justices, judges, and
academics vary in how they define and (even whether they
explicitly) refer to the theory and its principles.
    Some judges and justices have relied on mosaic-like rea-
soning, but the Supreme Court has not bound lower courts to
apply the mosaic theory. The theory first emerged in Fourth
Amendment jurisprudence in United States v. Maynard,
615 F.3d 544 (D.C. Cir. 2010). The D.C. Circuit considered
whether the government’s tracking of the defendant’s car for
twenty-eight days by installing a global positioning system
(“GPS”) device onto his car without a valid warrant consti-
tuted a search under the Fourth Amendment. Id. at 555. The
court invoked the “mosaic theory,” id. at 562, to determine
that the surveillance constituted a Fourth Amendment search:
       [W]e hold the whole of a person’s movements
       over the course of a month is not actually ex-
       posed to the public because the likelihood a
       stranger would observe all those movements is
       not just remote, it is essentially nil. It is one thing
       for a passerby to observe or even to follow
       someone during a single journey as he goes to
No. 20-2352                                                   19

       the market or returns home from work. It is an-
       other thing entirely for that stranger to pick up
       the scent again the next day and the day after
       that, week in and week out, dogging his prey
       until he has identified all the places, people,
       amusements, and chores that make up that per-
       son’s hitherto private routine.
Id. at 560. The D.C. Circuit continued:
       Prolonged surveillance reveals types of infor-
       mation not revealed by short-term surveillance,
       such as what a person does repeatedly, what he
       does not do, and what he does ensemble. These
       types of information can each reveal more about
       a person than does any individual trip viewed
       in isolation. Repeated visits to a church, a gym,
       a bar, or a bookie tell a story not told by any sin-
       gle visit, as does one’s not visiting any of these
       places over the course of a month. The sequence
       of a person’s movements can reveal still more; a
       single trip to a gynecologist’s office tells little
       about a woman, but that trip followed a few
       weeks later by a visit to a baby supply store tells
       a different story. A person who knows all of an-
       other’s travels can deduce whether he is a
       weekly church goer, a heavy drinker, a regular
       at the gym, an unfaithful husband, an outpa-
       tient receiving medical treatment, an associate
       of particular individuals or political groups—
       and not just one such fact about a person, but all
       such facts.
Id. at 562 (footnote omitted).
20                                                    No. 20-2352

    Reviewing the issue of GPS monitoring under a different
name, United States v. Jones, a majority of the Supreme Court
affirmed Maynard on a narrow “property-based” theory, see
565 U.S. at 404–11, declining to rely on the mosaic theory, see
id. at 412–13. Specifically, the Jones majority held that the gov-
ernment had effected a physical trespass on private property
by attaching the device on the defendant’s vehicle without a
warrant. Id. at 404–07.
    Concurring in the judgment, however, Justice Alito—
joined by Justices Ginsburg, Breyer, and Kagan—endorsed
the mosaic theory’s logic and rejected the majority’s stringent
reliance on a trespass theory. In Justice Alito’s view, the GPS
monitoring crossed a constitutional line, wherever that line
might be:
       [R]elatively short-term monitoring of a person’s
       movements on public streets accords with ex-
       pectations of privacy that our society has recog-
       nized as reasonable. But the use of longer term
       GPS monitoring in investigations of most of-
       fenses impinges on expectations of privacy. For
       such offenses, society’s expectation has been
       that law enforcement agents and others would
       not—and indeed, in the main, simply could
       not—secretly monitor and catalogue every sin-
       gle movement of an individual’s car for a very
       long period.
Id. at 430 (Alito, J., concurring) (citation omitted). As he wrote,
“the line was surely crossed before the 4–week mark” of the
government’s tracking of “every movement that [the defend-
ant] made in the vehicle he was driving.” Id. While describing
Justice Alito’s Jones concurrence as “cryptic,” scholars have
No. 20-2352                                                    21

read his opinion to “echo[] the D.C. Circuit’s mosaic approach
in Maynard.” Kerr, The Mosaic Theory, supra, at 327.
    Writing separately, Justice Sotomayor joined the majority
but similarly asserted that finding a search was not contingent
on a “trespassory intrusion[] on property.” Jones, 565 U.S. at
414 (Sotomayor, J., concurring). For Justice Sotomayor, the
unique investigatory capabilities of GPS monitoring—includ-
ing its inexpensiveness, precision, and efficiency—posed seri-
ous concerns: “GPS monitoring generates a precise, compre-
hensive record of a person’s public movements that reflects a
wealth of detail about her familial, political, professional, re-
ligious, and sexual associations.” Id. at 415. She explained:
       I would take these attributes of GPS monitoring
       into account when considering the existence of
       a reasonable societal expectation of privacy in
       the sum of one’s public movements. I would ask
       whether people reasonably expect that their
       movements will be recorded and aggregated in
       a manner that enables the government to ascer-
       tain, more or less at will, their political and reli-
       gious beliefs, sexual habits, and so on. I do not
       regard as dispositive the fact that the govern-
       ment might obtain the fruits of GPS monitoring
       through lawful conventional surveillance tech-
       niques.
Id. at 416. As with Justice Alito’s concurring opinion, scholars
argue that “[t]his passage clearly echoes the mosaic theory.”
Kerr, The Mosaic Theory, supra, at 328.
   Drawing on the reasoning of these Jones concurrences,
some scholars have argued that Chief Justice Roberts’s
22                                                   No. 20-2352

unanimous opinion in Riley v. California, 573 U.S. 373 (2014),
further illustrates support for the mosaic theory. Riley held
that the police may not, without a warrant, search digital in-
formation on an arrestee’s seized phone. Id. at 386. “Explain-
ing why the arrestee’s wallet could be searched but his cell
phone could not, Roberts offered an argument that is much
akin to the mosaic theory: …. [‘]The sum of an individual’s
private life can be reconstructed through a thousand photo-
graphs labeled with dates, locations, and descriptions; the
same cannot be said of a photograph or two of loved ones
tucked into a wallet.[’]” See Kugler & Strahilevitz, supra, at 208
(quoting Riley, 573 U.S. at 394).
    Most recently, a five-justice majority of the Supreme Court
held in Carpenter v. United States that the government’s collec-
tion of a defendant’s cell-site location information (“CSLI”)
(the time-stamped records a mobile phone makes every time
it connects to radio antennas known as cell sites) for a period
of 127 days amounted to a search under the Fourth Amend-
ment. 138 S. Ct. at 2211–12, 2220. The Court determined that
this investigative practice violated the defendant’s reasonable
expectation of privacy because it provided “an all-encom-
passing record of the holder’s whereabouts,” uncovering “an
intimate window into a person’s life, revealing not only his
particular movements, but through them his ‘familial, politi-
cal, professional, religious, and sexual associations.’” Id. at
2217 (quoting Jones, 565 U.S. at 415 (Sotomayor, J., concur-
ring)). The Court emphasized that “[a] majority of this Court
has already recognized that individuals have a reasonable ex-
pectation of privacy in the whole of their physical move-
ments.” Id. (citing Justice Alito’s and Justice Sotomayor’s Jones
concurrences). Scholars describe the Carpenter majority as ef-
fectively “endors[ing] the mosaic theory of privacy.” Paul
No. 20-2352                                                                 23

Ohm, The Many Revolutions of Carpenter, 32 Harv. J.L. & Tech.
357, 373 (2019).
    Despite garnering passing endorsement from some—if
not most—of the justices in the various opinions in Jones, Ri-
ley, and Carpenter, the theory has not received the Court’s full
and affirmative adoption. At a minimum, the Supreme Court
has not yet required lower courts to apply it. Moreover, many
courts that have considered the theory have expressed disap-
proval,2 although not without exception.3 Additionally, the


    2 See, e.g., United States v. Howard, 426 F. Supp. 3d 1247, 1255–56 (M.D.
Ala. 2019) (declining to apply the mosaic theory, in part, because “[t]he
idea that constitutionality could hinge on the duration of a ‘search’ has
puzzled a Supreme Court justice, several circuit judges, three district
courts, two state supreme courts, and one of the nation’s leading Fourth
Amendment scholars” (footnotes omitted)), aff’d, No. 20-10877, 2021 WL
2155414 (11th Cir. May 27, 2021); State v. Muhammad, 451 P.3d 1060, 1073
(Wash. 2019) (rejecting government’s argument invoking mosaic theory
and criticizing the theory as eluding a “workable analysis” because
“[r]ather than offering analysis based on a reasonable expectation of pri-
vacy, the mosaic theory instead requires a case-by-case, ad hoc determi-
nation of whether the length of time of a cell phone ping violated the
Fourth Amendment”); Tracey v. State, 152 So. 3d 504, 520 (Fla. 2014) (re-
jecting mosaic theory and “conclud[ing] that basing the determination as
to whether warrantless real time cell site location tracking violates the
Fourth Amendment on the length of the time the cell phone is monitored
is not a workable analysis”).
    3 See, e.g., Commonwealth v. McCarthy, 142 N.E.3d 1090, 1102–03 (Mass.

2020) (“This aggregation principle or mosaic theory is wholly consistent
with the statement in Katz, 389 U.S. at 351, 88 S.Ct. 507, that ‘[w]hat a per-
son knowingly exposes to the public … is not a subject of Fourth Amend-
ment protection,’ because the whole of one’s movements, even if they are
all individually public, are not knowingly exposed in the aggregate.” (al-
terations in original)); United States v. Diggs, 385 F. Supp. 3d 648, 652 (N.D.
24                                                            No. 20-2352

mainstream academic view has urged courts to reject the the-
ory. 4 Accordingly, whether or not the theory has merit from a
theoretical or policy standpoint, Tuggle has not presented us
with binding caselaw indicating that we must apply the mo-
saic theory.
            2. Prolonged Pole Camera Surveillance in Other
               Courts
    Having noted the reluctance of some courts to adopt the
mosaic theory, we now turn to the specific issue at hand: the
constitutionality of prolonged pole camera surveillance. Like
the isolated use of pole cameras, the government’s prolonged
use of pole cameras to surveil someone’s home presents an
issue of first impression for this Court. We therefore begin by
surveying the decisions of courts that have addressed long-
term pole camera or video surveillance.


Ill. 2019) (relying on the “scope of the reasonable expectation of privacy
identified by the Jones concurrences and reaffirmed in Carpenter” to find a
search based on government’s use of GPS data), reconsideration denied, No.
18 CR 185, 2020 WL 208826 (N.D. Ill. Jan. 14, 2020); State v. Jones, 2017 SD
59, ¶ 29, 903 N.W.2d 101, 110 (“The information gathered through the use
of targeted, long-term video surveillance will necessarily include a mosaic
of intimate details of the person’s private life and associations.”).
     4See, e.g., Kerr, The Mosaic Theory, supra, at 344, 353 (detailing case
against mosaic theory in favor of a “sequential approach to Fourth
Amendment analysis” and concluding that “despite … good intentions,
the mosaic theory represents a Pandora’s Box that courts should leave
closed”); Kugler & Strahilevitz, supra, at 259–60 (illustrating, empirically,
“that very large majorities of the American public do not conceptualize
Fourth Amendment expectations of privacy in a manner that is congenial
to the ‘mosaic theory’”). But see generally Gray & Citron, supra, at 411–28
(responding to prominent criticism of, and defending, mosaic theory).
No. 20-2352                                                                 25

    Federal circuit, federal district, and state courts have splin-
tered on how to treat police use of cameras on public property
(or, with consent, on private property) to record what hap-
pens outside one’s home. That said, not all the cases we dis-
cuss specifically addressed the issue of the government using
cameras to paint a mosaic of a person’s private life, nor did all
the cases deal specifically with pole cameras.
    Our sister circuits have almost uniformly declined to find
Fourth Amendment searches in situations similar to the one
presented here. For example, in United States v. Houston,
813 F.3d 282 (6th Cir. 2016), the Sixth Circuit concluded the
government’s use of pole cameras installed on public prop-
erty and trained on the defendant’s home for ten weeks did
not constitute a Fourth Amendment search. Id. at 287–88. The
Sixth Circuit reasoned the defendant did not have a “reason-
able expectation of privacy in video footage recorded by a
camera that was located on top of a public utility pole and that
captured the same views enjoyed by passersby on public
roads.” Id. The Sixth Circuit emphasized that the agents “only
observed what [the defendant] made public to any person
traveling on the roads surrounding the farm” and that the
camera accomplished what agents “stationed … round-the-
clock” could have observed. Id. at 288. Furthermore, they ex-
plicitly rejected that the duration of surveillance altered their
analysis “because the Fourth Amendment does not punish
law enforcement for using technology to more efficiently con-
duct their investigations.” Id. 5


    5 See also United States v. Trice, 966 F.3d 506, 516 (6th Cir. 2020) (reaf-
firming Houston post-Carpenter), cert. denied, 141 S. Ct. 1395 (2021). But see
United States v. Anderson-Bagshaw, 509 F. App’x 396, 405 (6th Cir.
26                                                             No. 20-2352

    In harmony with the Sixth Circuit, the First,6 Fourth,7 and
Tenth 8 Circuits (and arguably the Ninth Circuit 9) have simi-
larly approved of governmental use of cameras, but we again


2012) (“[W]e confess some misgivings about a rule that would allow the
government to conduct long-term video surveillance of a person’s back-
yard without a warrant. Few people, it seems, would expect that the gov-
ernment can constantly film their backyard for over three weeks using a
secret camera that can pan and zoom and stream a live image to govern-
ment agents.”).
     6See, e.g., United States v. Bucci, 582 F.3d 108, 116–17 (1st Cir. 2009)
(holding defendant did not establish “a reasonable objective expectation
of privacy” that was invaded by eight-month long video surveillance of
his home from a utility pole). But see United States v. Moore-Bush, 982 F.3d
50, 50 (1st Cir. 2020) (mem.) (scheduling en banc hearing for March 23,
2021, to review panel decision affirming Bucci on stare decisis grounds).
     7The Fourth Circuit held that the government’s use of “a hidden,
fixed-range, motion-activated video camera placed in the [defendant’s]
open fields” did not violate the Fourth Amendment. Vankesteren, 553 F.3d
at 287, 288–91. This decision, however, did not turn on how long the gov-
ernment used the camera.
     8The Tenth Circuit held that “evidence obtained from the video cam-
eras installed on the telephone poles and the recordings made in the un-
dercover FBI car were not introduced in violation of … the Fourth Amend-
ment.” Jackson, 213 F.3d at 1282; see also United States v. Cantu, 684 F. App’x
703, 703 (10th Cir. 2017) (unpublished) (reaffirming Jackson’s holding that
warrantless video surveillance did not constitute search). Like the Fourth
Circuit in Vankesteren, however, neither Jackson nor Cantu centered on the
mosaic or a like theory.
     9In holding that footage obtained from surveillance camera installed
without warrant in a common area of hospital did not constitute Fourth
Amendment search, the Ninth Circuit reasoned “the defendant had no ob-
jectively reasonable expectation of privacy that would preclude video sur-
veillance of activities already visible to the public.” See United States v.
Gonzalez, 328 F.3d 543, 548 (9th Cir. 2003).
No. 20-2352                                                               27

note these cases did not squarely address the same factual and
legal circumstances presented here.
    Furthermore, the only circuit to require the government to
seek a court order authorizing video surveillance is the Fifth
Circuit, which, decades before Jones and Carpenter, found the
government’s use of a pole camera for more than thirty days
to record the exterior of defendant’s home “qualif[ied] as a
search under the [F]ourth [A]mendment ….” See Cuevas-
Sanchez, 821 F.2d at 251. Significantly, however, the govern-
ment positioned the camera in that case to look over a ten-
foot-tall fence and capture images unviewable to passersby.
See id. Thus, for now, no federal circuit court has found a
Fourth Amendment search based on long-term use of pole
cameras on public property to view plainly visible areas of a
person’s home. To part ways with our sister circuits that have
spoken to pole cameras, then, would likely create a circuit
split, which “generally requires quite solid justification; we
do not lightly conclude that our sister circuits are wrong.” An-
drews v. Chevy Chase Bank, 545 F.3d 570, 576 (7th Cir. 2008).
    Federal district courts are mixed on whether pole cam-
era surveillance constitutes a search. Following the trend lines
of the federal circuit courts, district courts in the Seventh Cir-
cuit have found no Fourth Amendment searches when
law enforcement officers made extended use of pole cam-
eras. 10 Some federal district courts outside the Seventh Circuit


    10  See, e.g., United States v. Kubasiak, No. 18-CR-120, 2018 WL 4846761,
at *3, *7 (E.D. Wis. Oct. 5, 2018) (finding monthslong use of a camera in-
stalled on defendant’s neighbor’s property was not a Fourth Amendment
search because footage revealed “only what the neighbor, or a police of-
ficer standing in the neighbor’s house, could have seen”); United States v.
28                                                            No. 20-2352




Kay, No. 17-CR-16, 2018 WL 3995902, at *1, *3 (E.D. Wis. Aug. 21, 2018)
(concluding eighty-seven days of pole camera surveillance “[did] not con-
stitute a Fourth Amendment search” and noting “nearly every federal
court which has addressed the issue has held that pole camera surveil-
lance of a person’s driveway or the exterior of his residence does not vio-
late the person’s reasonable expectation of privacy”); United States v.
Tirado, No. 16-CR-168, 2018 WL 1806056, at *3–4 (E.D. Wis. Apr. 16, 2018)
(finding three-month use of pole camera was not a search because, prior
to Carpenter, “the Seventh Circuit ha[d] not so held [that to be unconstitu-
tional], and the other circuit courts of appeal ha[d] rejected such claims”);
see also generally United States v. Harris, No. 17-CR-175, 2021 WL 268322
(E.D. Wis. Jan. 27, 2021) (finding warrantless video surveillance cameras
in and outside of defendant’s apartment complex did not amount to
Fourth Amendment search because “[u]nlike [the CSLI in Carpenter], the
video surveillance did not track the totality of the defendant’s move-
ments” (citation omitted)).
No. 20-2352                                                                 29

agree that use of pole cameras does not constitute a search.11
Nevertheless, that view is not unanimous. 12



    11  See, e.g., United States v. Flores, No. 19-CR-364, 2021 WL 1312583, at
*8 (N.D. Ga. Apr. 8, 2021) (finding no Fourth Amendment search from
pole camera footage because “[t]he images of a single, fixed location cap-
tured by the pole camera in this case d[id] not equate with the activities
revealed by cell-site location information considered by the Court in Car-
penter”); United States v. Edmonds, 438 F. Supp. 3d 689, 694 (S.D. W. Va.
2020) (“declin[ing] to adopt the Defendant’s proposed blanket rule that a
warrant is required for use of a pole camera placed in a public location
with a view available to the public”); United States v. Mazzara, No. 16 CR.
576, 2017 WL 4862793, at *10–12 (S.D.N.Y. Oct. 27, 2017) (finding that
twenty-one-month “video surveillance at issue … did not violate any ex-
pectation of privacy that modern society is prepared to recognize as rea-
sonable under Katz and its progeny”); United States v. Pratt, No. 16-CR-
20677-06, 2017 WL 2403570, at *4 (E.D. Mich. June 2, 2017) (“Continuous
camera surveillance of private property does raise privacy concerns and
is evocative of an ‘Orwellian state.’ But there are mitigating factors and
controlling precedent which justify denial of the motion to suppress here.”
(citation omitted)); United States v. Gilliam, No. 12-CR-93, 2015 WL
5178197, at *9 (W.D. Pa. Sept. 4, 2015) (finding no “objectively reasonable
expectation of privacy when the images captured by the pole camera were
visible to any person who was located in the public street looking at his
home”); United States v. Brooks, 911 F. Supp. 2d 836, 843 (D. Ariz. 2012)
(“[L]aw enforcement’s use of the pole camera did not violate the Fourth
Amendment ….”).
    12 See, e.g., United States v. Houston, 965 F. Supp. 2d 855, 898 (E.D. Tenn.

2013) (finding that “warrantless video surveillance of the curtilage of [the
Defendant’s home], beyond fourteen (14) days violated the Defendant’s
reasonable expectation of privacy”); United States v. Vargas, 2014 U.S. Dist.
LEXIS 184672, *27 (E.D. Wash. Dec. 15, 2014) (“[L]aw enforcement’s video
surveillance of [the defendant’s] front yard for six weeks with a camera
that could zoom and record violated his reasonable expectation of privacy:
an expectation that society is prepared to recognize as reasonable.”).
30                                                               No. 20-2352

   State courts likewise disagree whether pole camera use
constitutes a search. Some state courts have joined the chorus
determining that pole camera use does not qualify as a Fourth
Amendment search. 13 However, other state supreme and ap-
pellate courts have found the use of pole cameras for varying
durations violates the Fourth Amendment. 14 Mirroring this
array of opinions, scholars and students have puzzled over
how the law ought to treat pole camera surveillance. 15


     13 See, e.g., State v. Duvernay, 2017-Ohio-4219, 92
                                                       N.E.3d 262, 269–70, at
¶ 25 (3d Dist.) (affirming an Ohio “trial court’s determination that law en-
forcement’s use of the pole camera [for nine days] did not violate [the de-
fendant’s] Fourth Amendment right to privacy”).
     14 See, e.g., State v. Jones, 903 N.W.2d at 111–13 (holding that govern-
ment had executed a search through “the warrantless use of a pole camera
to surveil a suspect’s activities outside his residence for two months”); Peo-
ple v. Tafoya, 2019 COA 176, ¶¶ 2, 33–52, No. 17CA1243, 2019 WL 6333762,
at *1, *6–10 (holding that “the continuous, three-month-long use of the
pole camera constituted a search under the Fourth Amendment”), cert.
granted, No. 20SC9, 2020 WL 4343762 (Colo. June 27, 2020); cf. Common-
wealth v. Mora, 150 N.E.3d 297, 302 (Mass. 2020) (concluding that “contin-
uous, long-term pole camera surveillance targeted at the residences of [the
defendants] well may have been a search within the meaning of the Fourth
Amendment, a question we do not reach, but certainly was a search under
art. 14” of the Massachusetts Declaration of Rights); Commonwealth v.
Comenzo, No. 1482CR01050, 2021 WL 616548, at *8 (Mass. Super. Jan. 11,
2021) (“[T]he seventeen-day video surveillance in this case would have
required a warrant under Mora.”).
     15 See, e.g., Taylor H. Wilson, Jr., Note, The Mosaic Theory's Two Steps:
Surveying Carpenter in the Lower Courts, 99 Tex. L. Rev. Online 155, 173–75
(2021) (discussing the “close case” pole camera surveillance presents un-
der the mosaic theory); Aparna Bhattacharya, Note, The Impact of Carpen-
ter v. United States on Digital Age Technologies, 29 S. Cal. Interdisc. L.J. 489,
501–07 (2020) (discussing and applying Carpenter to pole camera
No. 20-2352                                                                   31

             3. The Pole Camera Surveillance Here Was Not a
                Search Under the Mosaic Theory
   Having outlined the theoretical and jurisprudential un-
derpinnings of the mosaic theory and various courts’ treat-
ment of pole camera footage, we now turn to Tuggle’s case.
The thrust of Tuggle’s argument—rooted in the mosaic the-
ory—is that the government’s use of the three pole cameras
unconstitutionally “captured the whole of Mr. Tuggle’s
movements.” See Carpenter, 138 S. Ct. at 2217 (“[I]ndividuals
have a reasonable expectation of privacy in the whole of their
physical movements.”). Even if we accepted the mosaic the-
ory, however—and we do not go that far—current Supreme
Court precedent does not support Tuggle’s argument.
   Of course, the stationary cameras placed around Tuggle’s
house captured an important sliver of Tuggle’s life, but they
did not paint the type of exhaustive picture of his every move-
ment that the Supreme Court has frowned upon. If the facts
and concurrences of Jones and Carpenter set the benchmarks,
then the surveillance in this case pales in comparison.


surveillance); Matthew Tokson, The Next Wave of Fourth Amendment Chal-
lenges After Carpenter, 59 Washburn L.J. 1, 17–19 (2020) (predicting the Su-
preme Court will “rule that [pole camera] surveillance violates the Fourth
Amendment”); Taylor Cutteridge, Comment, Now You See Me: An Exami-
nation of the Legality of Police Use of Utility Pole Surveillance Cameras, 48 Cap.
U. L. Rev. 75, 102 (2020) (concluding that the Supreme Court should hold
pole camera surveillance does “not constitute a search under the Fourth
Amendment”); Tiffany M. Russo, Comment, Searches and Seizures As Ap-
plied to Changing Digital Technologies: A Look at Pole Camera Surveillance,
12 Seton Hall Cir. Rev. 114, 115–18 (2015) (arguing that courts should
broadly apply Ciraolo’s holding—that the defendant did not have an ob-
jectively reasonable expectation of privacy when his marijuana crop was
visible to the naked eye—to video surveillance).
32                                                   No. 20-2352

    In those cases, the justices expressed concerns about sur-
veillance leading to “a precise, comprehensive record of a per-
son’s public movements that reflects a wealth of detail about
her familial, political, professional, religious, and sexual asso-
ciations.” See Jones, 565 U.S. at 415 (Sotomayor, J., concurring)
(emphasis added); Carpenter, 138 S. Ct. at 2217 (same). Follow-
ing this reasoning, many justices saw the GPS and CSLI tech-
nologies in Jones and Carpenter as capable of capturing the
whole of the defendants’ movements, therefore implicating
the Fourth Amendment. The CSLI at issue in Carpenter even
tracked the defendant’s movement through not only public
areas, but also private places, which the Court likened to “at-
tach[ing] an ankle monitor to the phone’s user.” 138 S. Ct. at
2218.
    Unlike those technologies, the cameras here exposed no
details about where Tuggle traveled, what businesses he fre-
quented, with whom he interacted in public, or whose homes
he visited, among many other intimate details of his life. If
anything, far from capturing the “whole of his physical move-
ments,” id. at 2219, or his “public movements,” Jones, 565 U.S.
at 415 (Sotomayor, J., concurring), the cameras only high-
lighted Tuggle’s lack of movement, surveying only the time
he spent at home and thus not illuminating what occurred
when he moved from his home.
   Beyond the justices’ “cryptic” embrace of the mosaic the-
ory, Kerr, The Mosaic Theory, supra, at 326, the theory, in its
inception, drew a distinction between the “passerby … ob-
serv[ing] or even … follow[ing] someone during a single jour-
ney as he goes to the market or returns home from work” and
the far more problematic “stranger [who] pick[s] up the scent
again the next day and the day after that, week in and week
No. 20-2352                                                    33

out, dogging his prey until he has identified all the places,
people, amusements, and chores that make up that person’s
hitherto private routine.” Maynard, 615 F.3d at 560. The pole
cameras in this case likely lie somewhere between these ex-
tremes but more closely resemble the former. In one sense, the
recordings painted a whole picture of the happenings outside
Tuggle’s front door by recording nonstop for eighteen
months. See, e.g., State v. Jones, 903 N.W.2d at 111 (“[O]fficers
[were] able to ‘capture[] something not actually exposed to
public view—the aggregate of all of [the defendant’s] coming
and going from the home, all of his visitors, all of his cars, all
of their cars, and all of the types of packages or bags he carried
and when.’” (some alterations in original) (quoting United
States v. Garcia-Gonzalez, No. 14-10296, 2015 WL 5145537, at *5
(D. Mass. Sept. 1, 2015))). In another important sense, how-
ever, the footage only depicted one small part of a much
larger whole: Tuggle’s life or the “whole of his physical move-
ments.” Carpenter, 138 S. Ct. at 2219. Given their immobile na-
ture, the cameras could not make out an exhaustive record of
Tuggle’s “hitherto private routine,” Maynard, 615 F.3d at 560,
because much if not most of the relevant details occurred out-
side of the immediate area in front of Tuggle’s home.
    The prospective and nonhistorical use of the pole cameras
here further distinguishes them from the technologies in cases
where the Supreme Court relied on mosaic-styled arguments,
which had retrospective capabilities. In Riley v. California, the
Court determined that the government had unlawfully
searched the defendant’s phone based in part on the widening
“gulf between physical practicability and digital capacity” of
phones. 573 U.S. at 394. The court noted the immense amount
of information and data that phones contain, including “pho-
tographs, picture messages, text messages, Internet browsing
34                                                 No. 20-2352

history, a calendar, a thousand-entry phone book, and so on.”
Id. As for Internet browsing, the court said it could “reveal an
individual’s private interests or concerns.” Id. at 395. Fore-
shadowing the main issue in Carpenter, the Court commented
that “[h]istoric location information is a standard feature on
many smart phones and can reconstruct someone’s specific
movements down to the minute, not only around town but
also within a particular building,” essentially allowing the
government to go back in time. Id. at 396.
    The Supreme Court brought this idea to the fore in Carpen-
ter when it highlighted CSLI’s “retrospective quality” that
“gives police access to a category of information otherwise
unknowable.” 138 S. Ct. at 2218. The advent of CSLI-like tech-
nology therefore allows the government to “travel back in
time to retrace a person’s whereabouts,” obviating what
would have been previous “attempts to reconstruct a person’s
movements [that] were limited by a dearth of records and the
frailties of recollection.” Id. at 2218. We recently suggested
that Carpenter should be read narrowly to proscribe only the
collection of historical CSLI but not real-time CSLI. See United
States v. Hammond, 996 F.3d 374, 383 (7th Cir. 2021) (conclud-
ing that government only searched defendant when it col-
lected “historical CSLI,” but otherwise finding no search in
government’s collection of defendant’s “real-time CSLI”).
   By the logic of Riley and Carpenter, and our recent obser-
vations in Hammond, the pole camera surveillance here did
not run afoul of the Fourth Amendment because the govern-
ment could not “travel back in time to retrace [Tuggle’s]
whereabouts,” Carpenter, 138 S. Ct. at 2218, to say nothing of
the thorny questions presented by a pre-existing network of
No. 20-2352                                                            35

government cameras. 16 The government had to decide ex ante
to collect the video footage by installing the cameras. The gov-
ernment did not tap into an expansive, pre-existing database
of video footage of Tuggle’s home akin to the Internet brows-
ing history and extensive photos stored on cell phones con-
sidered in Riley, or the expansive CSLI in Carpenter. Until the
Supreme Court or Congress instructs otherwise, we will read
Carpenter as limited to the unique features of the historical
CSLI at issue there, as distinct from the real-time video foot-
age here. See Hammond, 996 F.3d at 387 (“The ‘narrow’ Carpen-
ter decision did not determine whether the collection of real-
time CSLI constitutes a Fourth Amendment search.”). The
majority opinion in Carpenter itself offers support for this in-
terpretation, as it stated that the Court was not “call[ing] into
question conventional surveillance techniques and tools, such
as security cameras.” 138 S. Ct. at 2220 (emphasis added).
Whether pole cameras are the same as security cameras is ir-
relevant because the cameras here would clearly qualify as a
“conventional surveillance technique[].”See id.
    We emphasize, however, that our decision in Tuggle’s
case does not rest on the premise that the government could
have—in theory—obtained the same surveillance by station-
ing an agent atop the utility poles outside Tuggle’s home, thus
rendering the decision to instead use pole cameras constitu-
tional. See Houston, 813 F.3d at 289 (“[I]t is only the possibility


    16 See, e.g., Rebecca Lipman, Protecting Privacy with Fourth Amendment
Use Restrictions, 25 Geo. Mason L. Rev. 412, 436–37 (2018) (“Cameras have
existed for a long time; networks of cameras blanketing an entire metro
area that are equipped with facial recognition technology have not. Such
a network could allow law enforcement to search for any individual, any-
where in a city, going back for weeks or months ….” (footnotes omitted)).
36                                                  No. 20-2352

that a member of the public may observe activity from a pub-
lic vantage point—not the actual practicability of law enforce-
ment’s doing so without technology—that is relevant for
Fourth Amendment purposes.”). This fiction contravenes the
Fourth Amendment and Katz’s command to assess reasona-
bleness. To assume that the government would, or even
could, allocate thousands of hours of labor and thousands of
dollars to station agents atop three telephone poles to con-
stantly monitor Tuggle’s home for eighteen months defies the
reasonable limits of human nature and finite resources. In our
view, the premise that the government could realistically ac-
complish the pole camera surveillance here for more than a
few days is a fiction that courts should not rely on to limit the
Fourth Amendment’s protections. See Jones, 565 U.S. at 416
(Sotomayor, J., concurring) (“I do not regard as dispositive the
fact that the government might obtain the fruits of GPS mon-
itoring through lawful conventional surveillance tech-
niques.”). We thus close the door on the notion that surveil-
lance accomplished through technological means is constitu-
tional simply because the government could theoretically ac-
complish the same surveillance—no matter how laborious—
through some nontechnological means.
    Although we now hold that the pole camera surveillance
of the exterior of Tuggle’s home did not constitute a Fourth
Amendment search, we are not without unease about the im-
plications of that surveillance for future cases. The eighteen-
month duration of the government’s pole camera surveil-
lance—roughly four and twenty times the duration of the
data collection in Carpenter and Jones, respectively—is con-
cerning, even if permissible.
No. 20-2352                                                  37

    That concern presents us with an obvious line-drawing
problem: How much pole camera surveillance is too much?
Most might agree that eighteen months (roughly 554 days) is
questionable, but what about 250 days? 100 days? 20 days? 1
day? See also Kerr, The Mosaic Theory, supra, at 329–43 (detail-
ing the “remarkable set of novel and difficult questions”
posed by the mosaic theory). Despite the inherent problems
with drawing an arbitrary line, the status quo in which the
government may freely observe citizens outside their homes
for eighteen months challenges the Fourth Amendment’s
stated purpose of preserving people’s right to “be secure in
their persons, houses, papers, and effects.” Drawing our own
line, however, risks violating Supreme Court precedent and
interfering with Congress’s policy-making function, which
would exceed our mandate to apply the law. United States v.
Cuevas-Perez, 640 F.3d 272, 276, 285 (7th Cir. 2011) (Flaum, J.,
concurring) (“The matter is, as they say, above our pay
grade.”), judgment vacated, 565 U.S. 1189 (2012).
    Beyond the line-drawing issues, we conclude by sounding
a note of caution regarding the current trajectory of Fourth
Amendment jurisprudence. As technological capabilities ad-
vance, our confidence that the Fourth Amendment (as cur-
rently understood by the courts) will adequately protect indi-
vidual privacy from government intrusion diminishes. Kyllo,
533 U.S. at 33–34 (“It would be foolish to contend that the de-
gree of privacy secured to citizens by the Fourth Amendment
has been entirely unaffected by the advance of technology.”).
Current Fourth Amendment jurisprudence admits of a pre-
carious circularity: Cutting-edge technologies will eventually
and inevitably permeate society. In turn, society’s expecta-
tions of privacy will change as citizens increasingly rely on
and expect these new technologies. Once a technology is
38                                                 No. 20-2352

widespread, the Constitution may no longer serve as a back-
stop preventing the government from using that technology
to access massive troves of previously inaccessible private in-
formation because doing so will no longer breach society’s
newly minted expectations. With the advent of digital, cloud-
based, and smart capabilities, these new technologies will sel-
dom contravene the traditional limitations imposed by the
Fourth Amendment on physical invasions. Jones, 565 U.S. at
404–11.
    Cameras are a perfect example of the circularity. In 1791,
no one would expect—because the technology did not exist—
that the government could capture a still (or moving) image
of a citizen at a given time or place. Even once invented and
introduced to society, few would have expected that the gov-
ernment would use then-unwieldy and expensive cameras to
aid in fast-moving law enforcement investigations. Eventu-
ally, cameras grew so sophisticated, discrete, portable, and in-
expensive that they pervaded society. By that point, the gov-
ernment’s use of cameras was entirely unsurprising, even
though the Framers might have balked at such a prospect
when they penned the Fourth Amendment. See David Alan
Sklansky, Too Much Information: How Not to Think About Pri-
vacy and the Fourth Amendment, 102 Cal. L. Rev. 1069, 1085
(2014) (“Cameras mounted in public and semi-public
places … are increasingly unremarkable, their presence taken
for granted.”). In other words, once society sparks the prome-
thean fire—shifting its expectations in response to technolog-
ical developments—the government receives license under
current Fourth Amendment jurisprudence to act with greater
constitutional impunity.
No. 20-2352                                                                39

    Barring a transformation in governing law, we expect this
chronicle of cameras to repeat itself again and again with the
evolution of far more invasive technologies. Today’s pole
cameras will be tomorrow’s body cameras, 17 “protracted lo-
cation tracking using [automatic license plate readers],”18
drones, 19 facial recognition, 20 Internet-of-Things and smart
devices, 21 and so much more that we cannot even begin to

    17 See Erik Nielsen, Comment, Fourth Amendment Implications of Police-

Worn Body Cameras, 48 St. Mary’s L.J. 115, 120 (2016) (“[T]he increased use
of widespread video recording, although intended to prevent misconduct
of police officers, creates concerns over the Fourth Amendment rights of
individuals to be free from unreasonable searches.”).
    18 See Samuel D. Hodge, Jr., Big Brother Is Watching: Law Enforcement’s
Use of Digital Technology in the Twenty-First Century, 89 U. Cin. L. Rev. 30,
40 (2020) (“[L]icense plate reader databases provide the opportunity for
institutionalized abuse by allowing anyone who has access to the infor-
mation to snoop into an individual’s daily activities, habits, or present and
past relationships.”).
    19 See Jennifer M. Bentley, Note, Policing the Police: Balancing the Right
to Privacy Against the Beneficial Use of Drone Technology, 70 Hastings L.J.
249, 251 (2018) (“[D]rones are … potent tools that can be used to invade
privacy and conduct highly intrusive surveillance.”).
    20See Andrew Guthrie Ferguson, Facial Recognition and the Fourth
Amendment, 105 Minn. L. Rev. 1105, 1108 (2021) (asserting that “the Fourth
Amendment will not save us from the privacy threat created by facial
recognition surveillance”).
    21 See Eunice Park, Objects, Places and Cyber-Spaces Post-Carpenter: Ex-
tending the Third-Party Doctrine Beyond CSLI: A Consideration of IoT and
DNA, 21 Yale J.L. & Tech. 1, 58 (2019) (arguing that “clarity [in Fourth
Amendment jurisprudence] is needed for the vast array of unregulated
technologies growing in popularity, and for those yet to emerge”); An-
drew Guthrie Ferguson, The “Smart” Fourth Amendment, 102 Cornell L.
Rev. 547, 631 (2017) (“In a world that needs both smart devices and the
40                                                            No. 20-2352

envision. New technologies of this sort will not disappear, nor
will the complicated Fourth Amendment problems that ac-
company them. If anything, we should expect technology to
continue to grow exponentially. And if current technologies
are any indication, that technological growth will predictably
have an inverse and inimical relationship with individual pri-
vacy from government intrusion, presenting serious concerns
for Fourth Amendment protections.
    Assuming as much, it might soon be time to revisit the
Fourth Amendment test established in Katz. See Cuevas-Perez,
640 F.3d at 276 (Flaum, J., concurring) (“If the doctrine needs
clarifying, tweaking, or an overhaul in light of technologies
employed by law enforcement, that additional guidance
should come from the Supreme Court.”). Indeed, almost four
decades ago, when considering a respondent’s argument that
“twenty-four hour surveillance of any citizen of this country
will be possible, without judicial knowledge or supervision,”
the Court reserved judgement because, “if such dragnet type
law enforcement practices as respondent envisions should
eventually occur, there will be time enough then to determine
whether different constitutional principles may be applica-
ble.” Knotts, 460 U.S. at 283–84. As this case illustrates, round-
the-clock surveillance for eighteen months is now unextraor-
dinary.
    This could also be an apt area for Congress to legislate be-
cause, as some have noted, “Congress has significant institu-
tional advantages over the courts in trying to regulate privacy

Fourth Amendment, there … needs to be a new theory to protect the data
trails we leave behind. Without such a theory, data trails will exist outside
of Fourth Amendment protection, and an intrusive sensor surveillance
system will be created without any constitutional restraints.”).
No. 20-2352                                                     41

in new technologies.” Kerr, The Mosaic Theory, supra, at 350;
see also Kyllo, 533 U.S. at 51 (Stevens, J., dissenting) (“It would
be far wiser to give legislators an unimpeded opportunity to
grapple with these emerging issues rather than to shackle
them with prematurely devised constitutional constraints.”);
Carpenter, 138 S. Ct. at 2246 (Thomas, J., dissenting) (“With no
sense of irony, the Court invalidates this [statutory] regime
today—the one that society actually created in the form of its
elected representatives in Congress.” (internal quotation
marks and citation omitted)); Cuevas-Perez, 640 F.3d at 286
(Flaum, J., concurring) (“[T]he unsettled, evolving expecta-
tions in this realm, combined with the fast pace of technolog-
ical change, may make the legislature the branch of govern-
ment that is best suited, and best situated, to act.”).
   For now, though, we will continue to faithfully apply our
current understanding of the Constitution and the Supreme
Court’s precedent. With respect to the pole cameras in this
case, that understanding requires that we find no search in
violation of the Fourth Amendment. The district court there-
fore did not err in denying Tuggle’s motion to suppress. As
such, we have no need to consider the government’s fallback
argument that, even if there were a Fourth Amendment
search, the good faith exception to the exclusionary rule
would apply.

                     III.   Conclusion

   For these reasons, we AFFIRM the district court’s denial of
Tuggle’s motion to suppress.

```

---
