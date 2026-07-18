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

## GROUP: content/cases/State v. Volle.md  (`case`, 4 assertions)

### content_page

```
---
title: "State v. Volle"
type: case
citation: ""
parallel_cite: ""
neutral_cite: ""
court: Kansas Supreme Court
court_level: state
circuit: ""
year: 2025
date_decided: 2025-12-12
docket: ""
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2025-12-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Volle
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10811858/state-v-volle/"
  cluster_id: 10811858
  opinion_id: 11278610
  identity_checked: false
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Recent development (role-based)"
related: ["[[Riley v. California]]", "[[Carpenter v. United States]]", "[[State v. Mansor]]"]
aliases: []
tags: ["case", "fourth-amendment", "digital-search", "computer-warrant", "particularity", "kansas"]
holding: "Because relevant information may be stored anywhere on a digital device, a warrant ordinarily cannot prescribe in advance exactly how…"
lake:
  record_id: State v. Volle
  status: under_review
  projected_at: 2026-07-06
---

# State v. Volle

*580 P.3d 1223 (Kan. 2025)* · Kansas Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In a first-degree murder investigation, police obtained a warrant to search Volle's cell phone. The warrant authorized creating a complete forensic image of the phone but limited the seizure to data related to the murder or identifying the phone's owner. Volle argued the warrant was unconstitutionally overbroad as to digital evidence.

## Issue
How the Fourth Amendment's [[Particularity|particularity]] requirement applies to a warrant to search a digital device—specifically, whether the warrant must prescribe the search method and how it must limit what may be seized.

## Rule
A digital warrant need not dictate the search method, but must limit the seizure. "Because relevant information may be stored anywhere on such a device, it is ordinarily impractical—and sometimes impossible—for a warrant to prescribe in advance how officers must locate that data." — 580 P.3d 1223 (Kan. 2025) (slip op., at 13). ^pin-13

As to what may be seized, "even though investigators may need to review broad portions of a device's contents to locate relevant material, the warrant must still include a meaningful limiting principle tying the authorized seizure to evidence of a specified offense." — *Id.* ^pin-13a

## Application
The warrant satisfied both aspects of [[Particularity|particularity]]: it authorized a full forensic image of the phone—a breadth recognized as practically necessary for digital searches—while expressly limiting the authorized seizure to data related to first-degree murder or identifying the phone's owner. That limiting principle kept the search anchored to the probable-cause showing and prevented the kind of exploratory rummaging the Fourth Amendment forbids, so Volle's overbreadth challenge failed.

## Conclusion
The digital warrant was sufficiently particular; the district court properly rejected Volle's overbreadth claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative**.
- A recent state development on digital-warrant [[Particularity|particularity]], coherent with the digital-privacy concerns of [[Riley v. California]] and [[Carpenter v. United States]] and the search-scope analysis of [[State v. Mansor]].

## Appears on
- [[Plain View Doctrine]] — *Recent development (role-based)*

## Sources
- *State v. Volle*, 580 P.3d 1223 (Kan. 2025) — https://www.courtlistener.com/opinion/10811858/state-v-volle/ (lead opinion id 11278610) — pinpoint: slip op. 13.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "43935fd10f18c15b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because relevant information may be stored anywhere on a digital device, a warrant ordinarily cannot prescribe in advance exactly how…", "title": "State v. Volle"}}
{"assertion_id": "f4f961140bb7295b", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Recent development (role-based)", "title": "State v. Volle"}}
{"assertion_id": "723fe759716fc9cb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2025-12-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "State v. Volle", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "State v. Volle", "varies_by_point": "false"}}
{"assertion_id": "cd94f8abd84cfb0b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "State v. Volle"}}
```

### lake record — State v. Volle

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Volle",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "State v. Volle",
    "case_name_short": "Volle",
    "case_name_full": "",
    "input_case_name": "State v. Volle",
    "court": "Kansas Supreme Court",
    "court_id": "kan",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2025-12-12",
    "year": 2025,
    "docket": null,
    "cluster_id": 10811858,
    "lead_opinion_id": 11278610,
    "sibling_ids": [
      11278610
    ],
    "absolute_url": "/opinion/10811858/state-v-volle/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    }
  },
  "pinpoints": [
    {
      "id": "pin-13",
      "page": null,
      "quote": "--- # State v. Volle *580 P.3d 1223 (Kan. 2025)* \u00b7 Kansas Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In a first-degree murder investigation, police obtained a warrant to search Volle's cell phone. The warrant authorized creating a complete forensic image of the phone but limited the seizure to data related to the murder or identifying the phone's owner. Volle argued the warrant was unconstitutionally overbroad as to digital evidence. ## Issue How the Fourth Amendment's particularity requirement applies to a warrant to search a digital device\u2014specifically, whether the warrant must prescribe the search method and how it must limit what may be seized. ## Rule A digital warrant need not dictate the search method, but must limit the seizure.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-13a",
      "page": null,
      "quote": "even though investigators may need to review broad portions of a device's contents to locate relevant material, the warrant must still include a meaningful limiting principle tying the authorized seizure to evidence of a specified offense.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-12-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Volle",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11278610) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR kan OR kanctapp)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(11278610)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11278610)",
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
    "complete_query": "cites:(11278610)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11278610,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-volle.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11278610,
        "cited_id": 157595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 165743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 172511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 505922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1163616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1199913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1284639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1288294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1369871,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 1379565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2331603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2517832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2542699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 2606277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 3196866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4022220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4266071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4348417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4471470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4526564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4680507,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4684947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 4707986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 5139220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 5288625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6346777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6348805,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 6350811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7619597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7923237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7923547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7924104,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 7924656,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9429558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9434728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9435413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9762923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9795487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11278610,
        "cited_id": 9796947,
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
    "date_created": "2026-07-05T20:34:10Z",
    "date_modified": "2026-07-06T13:38:39Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "official cite selection failed closed: no_official_class_citation",
      "legacy treatment migrated: good -> good_law",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation",
      "official cite selection failed closed: no_official_class_citation"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T13:38:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:35:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Volle

```
              IN THE SUPREME COURT OF THE STATE OF KANSAS

                                       No. 127,745

                                    STATE OF KANSAS,
                                        Appellee,

                                             v.

                                      JEREMY VOLLE,
                                         Appellant.


                              SYLLABUS BY THE COURT

1.
       The Fourth Amendment to the United States Constitution requires that "no
Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and
particularly describing the place to be searched, and the persons or things to be seized."
The scope of section 15 of the Kansas Constitution Bill of Rights is identical to that of
the Fourth Amendment to the United States Constitution.


2.
       A warrant satisfies the constitutional standard when it describes the evidence to be
searched with sufficient particularity to permit the executing officer to locate the same
from the face of the warrant. The standard, however, does not demand absolute precision;
it requires only that the warrant describe the property with as much specificity as the
government's knowledge and circumstances allow. The degree of specificity required
depends on the nature of the property and the facts known to officers at the time the
warrant issued.




                                             1
3.
          Separate from the method of search, the Fourth Amendment requires that a
warrant specify with particularity the type of evidence to be seized, and a valid warrant
must include a limiting principle that confines the authorized seizure to evidence of the
offense under investigation.


4.
          Courts evaluate electronic-device warrants under the same practical standard
applied to physical searches, asking only whether the description of items to be seized is
as particular as the circumstances reasonably allow. So long as the warrant contains a
clear limiting principle it is sufficiently particular.


5.
          Neither the Fourth Amendment nor section 15 of the Kansas Constitution Bill of
Rights mandate exclusion of unlawfully obtained evidence; the exclusionary rule is a
judicial deterrent, applied only when suppression would meaningfully deter police
misconduct.


6.
          Evidence is admissible under the inevitable discovery doctrine if the State proves
by a preponderance of the evidence that it would have been lawfully discovered absent
the unconstitutional conduct.


7.
          An inmate has no reasonable expectation of privacy in nonlegal outgoing mail that
is subject to inspection based on legitimate security or investigative purposes under jail
policy.


                                                2
8.
        An aiding-and-abetting instruction is proper when the evidence permits a
reasonable conclusion that the defendant knowingly and intentionally participated in a
criminal venture; mere presence or association is insufficient to establish accomplice
liability.


9.
        Cumulative trial errors, when considered together, may require reversal of the
defendant's convictions when the totality of the circumstances establish that the defendant
was substantially prejudiced by the errors and denied a fair trial.


10.
        A felony-murder conviction predicated on criminal discharge of a firearm at an
occupied motor vehicle is supported when the evidence shows a reckless discharge at an
occupied vehicle, even if the shooter's intent was directed at a person rather than the
vehicle itself.


11.
        Felony murder and reckless second-degree murder are distinct offenses under
K.S.A. 21-5109(d), and when both are found in the alternative, the convictions merge and
sentencing on the greater offense—felony murder—is proper.


        Appeal from Shawnee District Court; CHERYL RIOS, judge. Oral argument held September 9,
2025. Opinion filed December 12, 2025. Affirmed.


        Peter T. Maharry, of Kansas Appellate Defender Office, argued the cause and was on the briefs
for appellant.




                                                   3
        Carolyn A. Smith, assistant deputy district attorney, argued the cause, and Mike Kagay, district
attorney, and Kris W. Kobach, attorney general, were with her on the brief for appellee.


The opinion of the court was delivered by


        STANDRIDGE, J.: This is Jeremy Francis Volle's direct appeal following his
convictions for first-degree felony murder and criminal possession of a weapon. Volle
raises multiple claims of trial and sentencing error, including two evidentiary issues and
challenges to a jury instruction, sufficiency of the evidence, and sentencing. He also
argues cumulative error.


        For the reasons below, we affirm Volle's convictions and sentence. The district
court did not err in denying either of Volle's motions to suppress evidence or in
instructing the jury. In the absence of any error, Volle's cumulative error argument also
fails. Finally, the State presented sufficient evidence to support Volle's felony-murder
conviction, and the district court properly sentenced him for this crime.


                                                 FACTS


        In the early morning hours of May 27, 2021, Aaron Shepherd and his wife,
Megan, were driving around Topeka collecting scrap metal from dumpsters. While
Shepherd drove down the 1100 block of 17th Street, Megan slept in the front passenger
seat of their Ford Taurus. She woke up when Shepherd braked suddenly and she saw an
SUV speeding past. Shepherd told Megan that someone was chasing and shooting at
them, and he asked her to call 911. While Megan looked for her phone, Shepherd grabbed
Megan's BB gun, exited the car, and crouched near the open driver's side door as the
SUV drove by again. After the SUV passed, Shepherd tossed the BB gun back into the
car but remained outside, raising his arms and yelling. The SUV turned off 17th Street

                                                    4
and stopped. At this point, Megan saw a red laser beam hit Shepherd, heard a single
gunshot, and watched Shepherd fall to the ground. Shepherd was critically wounded and
later died at the hospital.


       Based on witness accounts of the shooting and video evidence collected from the
surrounding area, law enforcement identified a Chevy Trailblazer owned by Brandon
Croskey as the vehicle from which the gunshot was fired. Topeka Police Detective Jared
Strathman interviewed Croskey, who ultimately admitted involvement and identified
Volle as the shooter.


       The State charged Volle with criminal possession of a weapon and alternative
counts of first-degree felony murder and first-degree premeditated murder. To support the
felony-murder charge, the State alleged Volle killed Shepherd while committing the
inherently dangerous felony of criminal discharge of a firearm at an occupied motor
vehicle.


       The case proceeded to trial, where the jury heard conflicting testimony from
Croskey and Volle, with each implicating the other in the shooting.


       Croskey testified at trial, having previously pled guilty to reckless second-degree
murder and criminal discharge of a firearm at an occupied motor vehicle. As part of his
plea agreement, he agreed to provide truthful testimony for the State. Croskey testified
that around 4:30 a.m. on May 27, 2021, he was at a car wash at 21st and Wanamaker in
his Chevy Trailblazer, where he encountered Shepherd—a man he did not know—and
the two exchanged words. Croskey said he became upset and wanted to fight after
Shepherd called him a racial slur. Croskey left the car wash and called Volle to be his
backup in case Shepherd had a knife or gun.


                                              5
       Croskey went to Volle's house near 17th and Buchanan, and Volle eventually
came outside and got into the front passenger seat of the Trailblazer. Croskey started
driving and turned onto 17th Street, where he saw Shepherd's car and tried to cut him off.
After Shepherd drove around him, Croskey did a U-turn and caught up to Shepherd,
following close behind and then passing him when Shepherd slammed on his brakes.
Croskey did another U-turn and drove toward Shepherd's car. Croskey watched Shepherd
crouch between the open driver's side door and the car, holding what appeared to be a
firearm out the window. Croskey ducked down and then noticed Volle pulling a gun out
of his shorts pocket. Croskey testified he was shocked because he told Volle not to bring
a gun. Volle told Croskey to turn off 17th Street and stop so that he could take aim at
Shepherd. After Croskey did so, Volle leaned out of the passenger window, aimed the
laser on his gun at Shepherd, and fired one shot. Croskey then drove back to Volle's
house, where both men went inside and Croskey stayed for a few hours. Volle told
Croskey that he fired the shot because he wanted to see if the beam on his gun was
accurate. Volle also told Croskey not to contact the police and said that he should get rid
of his truck. Croskey later spray painted his Trailblazer blue but continued to drive it after
the shooting. When Croskey was interviewed by Detective Strathman, he did not
immediately identify Volle as the shooter because he was scared of Volle and feared what
Volle might do.


       Volle testified in his defense. He said he did not know Shepherd and denied
shooting him. Volle said Croskey arrived at his house upset about something, but he did
not know why Croskey wanted to meet up. Volle claimed he did not take a gun with him
when he got into Croskey's Trailblazer. He testified Croskey drove to 17th Street, tried to
cut off Shepherd's car, and then began following Shepherd. As they passed Shepherd's
car, Volle saw Shepherd pointing a gun at them but did not know it was a BB gun. After
Volle saw the gun, he was scared and told Croskey to take him home. Instead, Croskey
turned around and drove back toward Shepherd's car. Volle noticed Croskey had a gun in
                                              6
his hand as he drove by Shepherd, so Volle lay back in his seat. After turning off 17th
Street and coming to a stop, Croskey leaned over Volle and fired a single shot through
the passenger window. As Croskey drove away, Volle took the gun from the cup holder
and put it in his pocket because he recognized the gun as belonging to him. Volle did not
know that Croskey had the gun or how he had come to possess it. Volle assumed that the
mother of his children, who was friends with Croskey, loaned Croskey the gun.


       Volle said that when they went back to his house, they listened to the police
scanner for information about the shooting and later saw a news article confirming
Shepherd's death. Volle believed that Croskey was defending himself, because Croskey
told him that Shepherd had used a racial slur at the car wash and that Shepherd chased
Croskey with a gun. Volle did not want to cooperate with law enforcement because he
did not want to snitch on Croskey. Volle denied ever threatening Croskey after the
shooting or discouraging him from talking to the police. Volle claimed he told Croskey to
leave him out of it if he did talk to the police because he had nothing to do with the
shooting. According to Volle, Croskey did not seem afraid of him. Volle admitted that
videos from his phone after the shooting showed him wiping the gun for fingerprints and
talking to Croskey about looking for the shell casing and selling the gun or taking it "out
of commission." And Volle admitted that the videos captured him telling Croskey not to
leave in the morning before they could talk. Volle also said, "I think we're good," "I don't
think nobody saw the car," and, "Don't tell nobody, bro."


       A jury convicted Volle of first-degree felony murder, the alternative lesser
included offense of reckless second-degree murder, and criminal possession of a firearm.


       Before sentencing, Volle moved the district court to impose a sentence for reckless
second-degree murder because it was a more specific crime and therefore should control
his sentence under K.S.A. 21-5109(d). At sentencing, the court denied the motion,
                                             7
merged the murder convictions into a single conviction for felony murder, and imposed a
controlling sentence of life without the possibility of parole for 620 months.


        Volle directly appealed his convictions to this court. Jurisdiction is proper. See
K.S.A. 60-2101(b) (Supreme Court jurisdiction over direct appeals governed by K.S.A.
22-3601); K.S.A. 22-3601(b)(3)-(4) (life sentence and off-grid crime cases permitted to
be directly taken to Supreme Court); K.S.A. 21-5402(b) (first-degree murder is off-grid
person felony).


                                          ANALYSIS

        On appeal, Volle argues: (1) the district court erred in denying his motions to
suppress evidence, (2) the district court erred in instructing the jury on aiding and
abetting, (3) the cumulative effect of these errors deprived him of his constitutional right
to a fair trial, (4) the evidence was insufficient to support his conviction for first-degree
felony murder, and (5) the district court erred in sentencing Volle for his felony-murder
conviction rather than for reckless second-degree murder. We address each of Volle's
arguments in turn.


I. Motions to suppress

        Volle argues the district court erred when ruling on two motions to suppress
evidence: one regarding evidence law enforcement obtained from a search of his cell
phone and one regarding letters he wrote while in pretrial custody at the Shawnee County
Jail.


        When, as here, the material facts supporting a district court's decision on a motion
to suppress evidence are undisputed, suppression is a question of law subject to unlimited
appellate review. State v. Hanke, 307 Kan. 823, 827, 415 P.3d 966 (2018).
                                               8
       The Fourth Amendment to the United States Constitution and section 15 of the
Kansas Constitution Bill of Rights protect all persons against unreasonable searches and
seizures. State v. Baker, 306 Kan. 585, 589-90, 395 P.3d 422 (2017) (The Fourth
Amendment applies to the states through the Fourteenth Amendment.); State v. Daniel,
291 Kan. 490, 498, 242 P.3d 1186 (2010) (interpreting section 15 to provide the same
protections as the Fourth Amendment). The State bears the burden of proving the
lawfulness of a search and seizure. State v. Hillard, 315 Kan. 732, 747, 511 P.3d 883
(2022).


   A. Motion to suppress cell phone evidence


       After Croskey identified Volle as the shooter, law enforcement obtained a search
warrant for Volle's residence. When officers executed the search warrant, they found
Volle at the home and arrested him. At the time of his arrest, Volle had a black Samsung
cellular phone in his pocket. Law enforcement seized the phone and sought a separate
search warrant for it.


       In the affidavit in support of the search warrant for the phone, Detective Strathman
recounted the general investigation into the case and stated: "I am asking for a search
warrant for the phones as during my interview with [Croskey], he stated [Volle] had been
contacting him since the homicide occurred. Furthermore I know cellular devices are
capable of tracking movements through GPS if the location data is turned on." A district
court judge granted the State's application for a search warrant authorizing the following
search of Volle's cell phone:


       "Any and all electronically stored information, including but not limited to Call Logs,
       Text Messages, Multimedia Messaging, Pictures/videos, Messages, Information from

                                                   9
       Third Party Apps, Contacts Lists, device locations and any other form of electronically
       stored information associated with either crimes listed herein or identifying information
       to determine ownership of the searched devices.

       "Which items are contraband or are fruits, instrumentalities or evidence of K.S.A. 21-
       5402 Murder in the 1st Degree, are located in or upon:

       "Black Samsung cell phone IMEI 353327111435079 seized from Jeremy Volle."


       Before trial, Volle moved to suppress the cell phone evidence alleging the
affidavit lacked probable cause and contained factual misrepresentations, and the search
warrant was overbroad. As a result, Volle claimed the exclusionary rule applied and
required suppression of the evidence.


       After considering written and oral argument by the parties, the district court
denied Volle's motion to suppress. Although the district court agreed with Volle that the
affidavit failed to establish probable cause, it ultimately denied Volle's motion to
suppress after finding that the good-faith exception and, alternatively, the inevitable
discovery doctrine rendered the cell phone evidence admissible. The court also
determined that the warrant was not overbroad, contained no factual misrepresentations,
and was executed reasonably. Over Volle's objection at trial, the State introduced
evidence obtained from the search of Volle's cell phone.


       On appeal, Volle argues (1) the search warrant was overbroad, (2) the good-faith
exception does not apply because the affidavit contained factual misrepresentations, and
(3) the inevitable discovery doctrine is inapplicable because the evidence would not have
been discovered by lawful means absent the unconstitutional conduct.


       The State defends the district court's findings that the warrant was not overbroad,
that the affidavit contained no factual misrepresentations, and that the good-faith and
                                                   10
inevitable-discovery exceptions rendered the evidence admissible. The State further
asserts—without having filed a cross-appeal—that this court may nonetheless affirm the
district court's ruling as right for the wrong reason because, in its view, the affidavit itself
established sufficient probable cause to support the search.


       Before reaching the merits of the suppression issues, we must first determine
whether the State's probable-cause argument is properly before us. Kansas law requires
an appellee to cross-appeal a district court's adverse decisions before those rulings may
be challenged on appeal. Cooke v. Gillespie, 285 Kan. 748, 755, 176 P.3d 144 (2008); see
K.S.A. 60-2103(h) (cross-appeal required when "appellee desires to have a review of
rulings and decisions of which such appellee complains"). The State acknowledges that it
did not file a cross-appeal but contends that a cross-appeal was unnecessary because the
district court's finding of no probable cause was not an adverse ruling.


       The State's argument fails for two reasons. First, the governing statute does not
limit the cross-appeal requirement to "adverse" rulings. K.S.A. 2024 Supp. 60-2103(h)
provides that an appellee who seeks review of "rulings and decisions of which such
appellee complains" must file a notice of cross-appeal within 21 days after the notice of
appeal is filed. The statute's plain language encompasses any ruling the appellee seeks to
challenge, regardless of whether it altered the outcome of the judgment.


       Second, even if an "adverse" component were required, the district court's
determination that the warrant affidavit lacked probable cause was plainly adverse to the
State's position, even though the court ultimately denied the motion to suppress on other
grounds. See Merriam-Webster Online Dictionary (defining "adverse" as "opposed to
one's interests" or "unfavorable").




                                               11
       The State's failure to pursue a cross-appeal prevents us from reviewing the district
court's probable cause determination. See State v. Novotny, 297 Kan. 1174, 1181, 307
P.3d 1278 (2013) (holding appellee abandoned alternative grounds for affirming district
court's ultimately favorable suppression ruling when it failed to cross-appeal court's
adverse ruling on the alternative grounds). Accordingly, we decline to consider the State's
probable-cause argument.


          1. Suppression based on overbreadth


       Volle contends the district court should have suppressed evidence obtained from
his cell phone because the search warrant lacked the particularity required by the Fourth
Amendment. He argues the warrant was so sweeping that it allowed officers to search
"everything and anything" on his phone, leaving no meaningful limits on its scope.


       The Fourth Amendment to the United States Constitution requires that "no
Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and
particularly describing the place to be searched, and the persons or things to be seized."
"'The scope of Section 15 of the Kansas Constitution Bill of Rights is identical to that of
the Fourth Amendment to the United States Constitution.'" State v. Patterson, 304 Kan.
272, 275, 371 P.3d 893 (2016) (citing State v. LeFort, 248 Kan. 332, 334, 806 P.2d 986
[1991]; K.S.A. 2015 Supp. 22-2502[a] [authorizing the issuance of search warrants
"'which particularly describes a person, place or means of conveyance to be searched and
things to be seized'"]). A warrant satisfies the constitutional standard when it describes
the evidence to be searched "'with sufficient particularity to permit the executing officer
to locate the same from the face of the warrant.'" Patterson, 304 Kan. at 275 (citing
LeFort, 248 Kan. at 334-35).




                                             12
       The Fourth Amendment, however, does not demand absolute precision; it requires
only that the warrant describe the property "'with as much specificity as the government's
knowledge and circumstances allow.'" United States v. Riccardi, 405 F.3d 852, 862-63
(10th Cir. 2005) (citing United States v. Leary, 846 F.2d 592, 600 [10th Cir. 1988]). The
degree of specificity required depends on the nature of the property and the facts known
to officers at the time the warrant issued. 405 F.3d at 862. Kansas courts apply a
comparable standard, holding that "the test to prevent general searches is one of practical
accuracy rather than one of technical sufficiency, and absolute precision in the search
warrant is not required in identifying the property to be seized." State v. LeFort, 248 Kan.
332, 334-37, 806 P.2d 986 (1991); see also State v. Ames, 222 Kan. 88, 92, 563 P.2d
1034 (1977). Thus, so long as the warrant describes the evidence to be seized with as
much particularity as the circumstances reasonably allow, it satisfies both the Fourth
Amendment and Kansas constitutional standards.


       Although courts recognize that electronic devices pose unique challenges under
the Fourth Amendment's particularity requirement, they treat those challenges as part of
the circumstances that determine how particular a warrant need reasonably be. See, e.g.,
United States v. Burgess, 576 F.3d 1078, 1094 (10th Cir. 2009). Burgess explains that the
particularity requirement does not demand a warrant to specify the precise folders, file
paths, or search techniques officers must use when examining a digital device. Because
relevant information may be stored anywhere on such a device, it is ordinarily
impractical—and sometimes impossible—for a warrant to prescribe in advance how
officers must locate that data. 576 F.3d at 1094.


       But Burgess addresses only the method of executing a digital search; it does not
resolve the separate question of what evidence officers may seize. The Fourth
Amendment imposes a distinct requirement that the warrant describe with particularity
the type of evidence it authorizes officers to seize. Thus, even though investigators may
                                             13
need to review broad portions of a device's contents to locate relevant material, the
warrant must still include a meaningful limiting principle tying the authorized seizure to
evidence of a specified offense. See United States v. Palms, 21 F.4th 689, 698-99 (10th
Cir. 2021).


       Here, the warrant satisfied both aspects of the particularity requirement. It
permitted investigators to create a complete forensic image of the phone—a breadth that
Burgess recognizes as practically necessary—and it expressly limited the authorized
seizure to electronic data related to first-degree murder or identifying the phone's owner.
This limiting principle kept the search anchored to the probable-cause showing and
prevented the kind of exploratory rummaging the Fourth Amendment forbids.
Accordingly, the district court properly rejected Volle's overbreadth claim.


           2. Suppression based on inapplicability of the good-faith exception and the
              inevitable discovery doctrine

       Volle also claims the absence of probable cause barred admission of the cell phone
evidence and that neither the good-faith exception nor the inevitable discovery doctrine
justified its use. Before turning to the specific exceptions at issue, it helps to review the
principles governing the exclusionary rule and its role in enforcing Fourth Amendment
protections.


       Notably, neither the Fourth Amendment nor section 15 of the Kansas Constitution
Bill of Rights expressly prohibits evidence obtained in violation of their respective
protections. Rather, a judicially created remedy—the exclusionary rule—exists "to
prevent the use of unconstitutionally obtained evidence in a criminal proceeding against
the victim of the illegal search." Daniel, 291 Kan. at 496. This exclusionary rule protects
Fourth Amendment rights through deterrence and only applies when the rule's deterrent
effect will be achieved. Herring v. United States, 555 U.S. 135, 137, 129 S. Ct. 695, 172
                                              14
L. Ed. 2d 496 (2009) ("[S]uppression is not an automatic consequence of a Fourth
Amendment violation. Instead, the question turns on the culpability of the police and the
potential of exclusion to deter wrongful police conduct."); Daniel, 291 Kan. at 496
("'[A]pplication of the exclusionary rule properly has been restricted to those situations in
which its remedial purpose is effectively advanced.'"). Therefore, when considering
whether suppression is proper under the specific circumstances of each case, courts must
balance the deterrent effect of suppressing evidence against societal harms. Herring, 555
U.S. at 141.


       There are exceptions to the exclusionary rule which allow for the admission of
evidence that was obtained in violation of the Fourth Amendment. Relevant here, the
district court held the cell phone evidence was admissible under the good-faith exception
and the inevitable discovery doctrine. See Daniel, 291 Kan. at 497-500 (good-faith
exception); Baker, 306 Kan. at 591 (inevitable discovery doctrine). Volle challenges the
district court's conclusion that these exceptions applied. The question of whether an
exception to the exclusionary rule applies is a question of law, reviewed by this court
independently and without any required deference to the district court. See State v.
Hoeck, 284 Kan. 441, 447, 163 P.3d 252 (2007).


               i. Good-faith exception


       The United States Supreme Court first recognized the good-faith exception in
United States v. Leon, 468 U.S. 897, 920-25, 104 S. Ct. 3405, 82 L. Ed. 2d 677 (1984).
Under this exception, the Fourth Amendment exclusionary rule should not be applied to
bar evidence obtained by officers acting in reasonable reliance on a search warrant issued
by a detached and neutral magistrate but ultimately found to be invalid except where:




                                             15
       "'(1) the magistrate issuing the warrant was deliberately misled by false information; (2)
       the magistrate wholly abandoned his or her detached or neutral role; (3) there was so little
       indicia of probable cause contained in the affidavit that it was entirely unreasonable for
       the officers to believe the warrant was valid; or (4) the warrant so lacked specificity that
       officers could not determine the place to be searched or the items to be seized.'" State v.
       Hubbard, 309 Kan. 22, 33, 430 P.3d 956 (2018).


These circumstances should not occur often; the threshold to avoid application of the
Leon good-faith exception is high. State v. Zwickl, 306 Kan. 286, 295, 393 P.3d 621
(2017). Good faith is measured by an objective standard—how a reasonable law
enforcement officer would view the circumstances. Leon, 468 U.S. at 919-20.


       Because the State bears the burden of proving that the challenged police conduct
was permissible, the State must prove facts warranting application of the good-faith
exception. See Leon, 468 U.S. at 924; State v. Cleverly, 305 Kan. 598, 605, 385 P.3d 512
(2016). To satisfy its burden here, the State asserts that the warrant was not obviously
deficient and contends that law enforcement exhibited good faith in their investigative
efforts and in no way deliberately misled the judge who issued the warrant.


       Volle takes issue with the State's position, arguing the good-faith exception does
not apply because Detective Strathman deliberately misled the issuing judge by omitting
material information from the search warrant affidavit. As this court has recognized, a
deliberate omission may be equivalent to an affirmative misstatement if it misleads the
magistrate. State v. Probst, 247 Kan. 196, 206, 795 P.2d 393 (1990). A person attacking
an affidavit on the basis that it omitted information must prove that the omission was
both deliberate and material. State v. Colbert, 257 Kan. 896, 905, 896 P.2d 1089 (1995).
Thus, Volle must establish that inclusion of these omitted facts would have had some
bearing on the issuing judge's probable cause determination. See State v. Adams, 294
Kan. 171, 179, 273 P.3d 718 (2012); State v. Lockett, 232 Kan. 317, 320, 654 P.2d 433
                                                    16
(1982) (materiality determined by inquiring whether issuing judge would have found
probable cause if omitted material had been included).


       In support of his argument, Volle focuses on Detective Strathman's statement in
the affidavit that he was seeking a search warrant for Volle's phone because Croskey
stated during his interview that Volle had been contacting him since the shooting. He
contends this statement, which suggested there would be communication such as texts
between Volle and Croskey on Volle's phone, was misleading because Detective
Strathman omitted the following material information from the affidavit:


   • Croskey only gradually revealed more information during the interview and gave
       it in "varying shades of honesty."


   • When asked directly whether he shared text messages with Volle about the
       shooting, Croskey said "'I don't know, I don't think so.'"


   • When asked whether he sent anybody any text messages about the shooting,
       Croskey said, "'Huh-uh,'" and shook his head no.


Volle asserts that Detective Strathman's failure to include this information in the affidavit
constitutes a deliberate and material omission because including it would have led the
issuing judge to realize that no communication between Volle and Croskey would be
found on Volle's cell phone and thus deny the application for the warrant.


       But the record fails to support Volle's claim that Detective Strathman deliberately
withheld material information from the search warrant affidavit that would have had
some bearing on the issuing judge's probable cause determination. In the affidavit,
Detective Strathman recounted Croskey's statement that Volle had been contacting
                                             17
Croskey since the shooting. Notably, the information provided by Detective Strathman in
the affidavit was true regardless of whether Croskey and Volle exchanged text
messages—during Croskey's interview, he told Detective Strathman that Volle had tried
to contact him on his cell phone after the shooting and that he had Volle's number saved
in his phone. And despite Volle's suggestion otherwise, Croskey did not definitively deny
that he and Volle had exchanged text messages about the shooting. While Croskey
appeared relatively certain that he had not sent anyone else text messages about the
shooting, he could not say for sure whether he and Volle had texted about it.


       Moreover, it is unclear how any information about Croskey's honesty would have
impacted the court's decision to issue the warrant. If anything, these details, coupled with
Croskey's equivocation, could have reinforced an inference that Volle's phone contained
relevant communications. Thus, Detective Strathman's declaration in the search warrant
affidavit recounting Croskey's statement that Volle had been contacting him since the
shooting was not inaccurate or misleading, and the omitted information does not make it
so.


       In sum, there is no evidence to support Volle's claim that Detective Strathman's
omission was either deliberate or material such that it undermines the affidavit's
reliability. The warrant was not obviously deficient, and law enforcement acted in
objectively reasonable reliance on it. Because there was no misconduct to deter, the
good-faith exception applies. See Herring, 555 U.S. at 137 (purpose of the exclusionary
rule is to deter police misconduct). The district court did not err in finding that the good-
faith exception rendered the cell-phone evidence admissible.




                                              18
              ii. Inevitable discovery doctrine


       The inevitable discovery doctrine allows for the admission of unconstitutionally
obtained evidence if the evidence would have been discovered by lawful means absent
the unconstitutional conduct. Baker, 306 Kan. at 591 (explaining that "'punishment for an
act that does no harm is not required in order to deter harmful acts'"). The State must
establish inevitability by a preponderance of the evidence. 306 Kan. at 591.


       The district court held that the evidence from Volle's cell phone should not be
suppressed because it would have been discovered from an independent source—
Croskey's phone. Volle disagrees, arguing that the search of his phone was not inevitable.
He alleges that Croskey's phone only contained innocuous text message exchanges
between them that do not establish any basis for a search of Volle's phone.


       But Volle's argument ignores the fact that Croskey, the initial suspect in the
murder investigation, named Volle as the shooter during his interview with law
enforcement and said that he had been in contact with Volle before and after the shooting.
Based on this information, law enforcement sought a search warrant for the data on both
Croskey's and Volle's cell phones. So even if law enforcement had only searched
Croskey's phone, call logs and text messages from Croskey's phone around the time of
the murder would have ultimately led law enforcement to Volle and his phone. Therefore,
the district court did not err in finding the inevitable discovery doctrine applied.


              iii. Conclusion


       The district court properly admitted the cell-phone evidence under both the good-
faith and inevitable-discovery exceptions to the exclusionary rule. Thus, the district court
did not err in denying Volle's motion to suppress the cell phone evidence.
                                              19
    B.     Motion to suppress jail letters


         Volle also argues that the district court erred in denying his motion to suppress
evidence obtained from the search of his mail while in custody at the Shawnee County
Jail.


         Following Volle's arrest, he was held at the Shawnee County Jail. When inmates
arrive at the jail, they are provided with a physical copy of an Inmate Handbook. The
handbook may also be available in a digital format that inmates can access. The
handbook sets forth the jail's rules and expectations as well as inmate rights and
responsibilities. Relevant here, the handbook provides:


    • "You have the right to communicate with family, friends, and others via written
         correspondence, telephone calls, and/or visits according to facility rules,
         regulations, and schedules."


    • "You shall be allowed to correspond in writing with persons or organizations
         outside of this facility, unless there is a specific reason(s) to prohibit the
         correspondence to protect the safety and security of the recipient, the public, or the
         staff and inmates of the facility. Mail shall be limited to your personal
         correspondence with individuals outside the facility. All incoming and outgoing
         mail shall be subject to search at any time." (Emphasis added.)


         After Volle's arrest, Detective Strathman requested that the jail monitor Volle's
outgoing mail. According to the detective, it is common practice to monitor mail in cases
involving co-defendants "[p]artly because people that are incarcerated and don't have


                                                 20
access to the other party typically will go through somebody else to either send them a
message or something of that affect, or communicate about the case."


        After receiving the request from Detective Strathman, Shawnee County Jail
Lieutenant Matt Biltoft collected, opened, and scanned Volle's nonlegal mail and sent
digital copies to Detective Strathman. Two of Volle's outgoing letters caught the
detective's attention. The first letter was addressed to Destiny Baker and reads, in relevant
part:


                  "So, I'm not technically allowed to try to influence [Croskey] myself or threaten
        him, but if u were ta guide him N the direction he should prolly go it's not against the
        rules. Essentially you'll have to make him understand some things u already know. First
        and foremost-bein a snitch . . . is extremely dangerous 4 him.


                  "What's done is done tho now. He already wrote a statement and made up a story
        bcuz his mind was fucked up. They're prolly gonna offer him 60-120 months to testify on
        me. What they aren't gonna tell him is that they're gonna put him on the front page of the
        newspaper and everybody N prison will be waiting 4 him 2 get there. He'll only have 2
        choices—they both involve death just who's gonna b the cause of it? I'm not saying this ta
        try to threaten him, but he's a Topeka Crip. His own people aren't going ta let him walk
        around.


                  "He does have legal options tho. We know he was highly intoxicated when he
        talked to the police. That's called 'voluntary intoxication' and is enough to withdraw his
        statement mixed wit the fact that he was suicidal at the time of giving the statement. He
        needs to make his lawyer have a Jackson v. Denno hearing to get his statement
        withdrawn. Without his statement, the worst they can get him 4 is involuntary
        manslaughter & he could possibly go home the day of trial. Worst case scenario he'll
        have to do 32 months & if he withdraws his statement, from the second he steps foot N
        prison . . . he'll be treated like a God.



                                                     21
               "He does NOT have to testify against me (5th Amendment to the U.S.
       Constitution), but if he were to get on stand at my preliminary hearing on 8-18 & just told
       them that he was upset at me at the time he gave his statement & lied & told them it was
       me to try ta get me N trouble, that would also allow me to help him N the long run.


               "The reason I'm telling this all ta u is because he loves u more than he loves
       himself. U know he would do whatever u told him ta do. If u were to simply tell him that
       if he did the right thing & tell them that he lied u would b his chick through his whole
       prison sentence & you'd have a house 4 him to come home to. And on the other hand, if
       he were to go down a snitch, you'd never talk ta him again. You know how to work that
       nigga. U got me?"


The second letter was addressed to Noah Broja. It reads, in relevant part: "Bro do me a
HUGE favor and schedule visits 4 Brandon Croskey 4 as many as u can, under the name
DeathB4dishonor. Clog em up so he can't get any. And do it every few days."


       Based on the content of these letters, Detective Strathman requested and obtained
a search warrant to collect the original letters from Volle's property bag at the jail. Volle
filed a pretrial motion to suppress the letters, raising several constitutional arguments—
primarily, a violation of his right to privacy under the Fourth Amendment. After
considering the parties' written and oral arguments, the district court denied the motion.
Over Volle's objection at trial, the district court allowed the State to admit the letters into
evidence.


       As discussed, the Fourth Amendment prohibits unreasonable searches and
seizures. U.S. Const. amend. IV. But the Fourth Amendment is not implicated unless the
person invoking its protection had a justifiable, reasonable, or legitimate expectation of
privacy that was invaded by government action. Smith v. Maryland, 442 U.S. 735, 740,
99 S. Ct. 2577, 61 L. Ed. 2d 220 (1979); see Illinois v. Caballes, 543 U.S. 405, 408, 125

                                                   22
S. Ct. 834, 160 L. Ed. 2d 842 (2005) ("Official conduct that does not 'compromise any
legitimate interest in privacy' is not a search subject to the Fourth Amendment.").


       Ordinarily, the public at large has a legitimate expectation of privacy in letters and
other sealed packages. United States v. Jacobsen, 466 U.S. 109, 114, 104 S. Ct. 1652, 80
L. Ed. 2d 85 (1984). But the Fourth Amendment does not prohibit the examination of
prisoners' mail when it is prompted by reasonable justification. State v. Burnett, 300 Kan.
419, 442, 329 P.3d 1169 (2014) ("'[B]ecause of their reasonable concern for prison
security and inmates' diminished expectations of privacy, prison officials do not violate
the constitution when they read inmates' outgoing letters.'"); see United States v. Gordon,
168 F.3d 1222, 1228 (10th Cir. 1999) (The regulation of unprivileged incoming and
outgoing prison mail by prison officials is typically "an administrative matter in which
the courts will not intervene.").


       Volle argues the State failed to identify any reasonable justification for monitoring
his mail. Specifically, he contends Detective Strathman's request to monitor his mail as a
matter of "common practice" in multi-defendant cases was not connected to any
legitimate governmental interest. Without a reason for monitoring specific to him, Volle
contends the broad and sweeping request to seize all his mail violated his constitutional
rights under the Fourth Amendment.


       Courts generally assess whether a detainee has a reasonable expectation of privacy
in nonprivileged mail by examining the institution's policies. Burnett, 300 Kan. at 443-44
(finding defendant had no reasonable expectation that his letters would remain private
where defendant knew the jail reserved "'the right to monitor incoming/outgoing mail for
threats, escape plots, and other security concerns'"); State v. Matthews, 217 Kan. 654,
657-58, 538 P.2d 637 (1975) ("Since the letter was delivered to the jailer unsealed and


                                             23
with knowledge that it would be read [pursuant to jail policy], defendant has no claim of
any invasion of privacy.").


       Inmates at the Shawnee County Jail place outgoing mail in a communal box in
their living unit. The mailroom staff collects the letters and then sends them out of the
building. The inmate handbook—which Volle does not deny he received—provides that
all incoming and outgoing mail is subject to search at any time "to protect the safety and
security of the recipient, the public, or the staff and inmates of the facility." This policy
serves as a reasonable governmental justification for limiting Volle's already diminished
privacy interest. Moreover, Detective Strathman articulated an additional public-safety
rationale: in cases involving co-defendants, law enforcement monitors inmate mail to
prevent improper communications about the case. See State v. Mason, 268 Kan. 37, 41,
986 P.2d 387 (1999) ("[P]risoners' outgoing mail may be screened for information on
future criminal activities.").


       Under these circumstances, Volle lacked any legitimate expectation of privacy in
his nonlegal outgoing mail, and the State had a reasonable and specific justification for
monitoring it. Accordingly, the district court did not err in denying Volle's motion to
suppress the jail-letter evidence.


II. Aiding and abetting jury instruction

       Volle argues the district court committed reversible error when it sua sponte issued
a jury instruction on aiding and abetting.


       When analyzing jury instruction issues, appellate courts follow a three-step
process: (1) determining whether the appellate court can or should review the issue, in
other words, whether there is a lack of jurisdiction or a failure to preserve the issue for

                                              24
appeal; (2) considering the merits of the claim to determine whether error occurred
below; and (3) assessing whether any error requires reversal, in other words, whether the
error can be considered harmless. State v. Holley, 313 Kan. 249, 253, 485 P.3d 614
(2021); see K.S.A. 22-3414(3) ("No party may assign as error the giving or failure to give
an instruction . . . unless the party objects thereto before the jury retires to consider its
verdict . . . unless the instruction or the failure to give an instruction is clearly
erroneous.").


       At the first step, Volle objected to the instruction, which preserves the issue for
review. At the second step, we consider whether the aiding and abetting instruction was
legally and factually appropriate, using an unlimited standard of review of the entire
record. See Holley, 313 Kan. at 254. Neither party suggests that the instruction was
legally deficient in any way, so we assume that the instruction provided an accurate
recitation of Kansas' aiding and abetting law. State v. Broxton, 311 Kan. 357, 361, 461
P.3d 54 (2020) (To be legally appropriate, the instruction must fairly and accurately state
the applicable law.).


       Thus, our review at the second step focuses solely on whether the aiding and
abetting instruction was factually appropriate. To determine whether an instruction was
factually appropriate, we must decide whether there was sufficient evidence, viewed in
the light most favorable to the requesting party, to support the instruction. Holley, 313
Kan. at 255. Circumstantial evidence is enough to support a conviction of even the
gravest offense. In analyzing this issue, appellate courts do not reweigh the evidence,
resolve conflicts in the evidence, or pass on the credibility of witnesses. State v. Aguirre,
313 Kan. 189, 209, 485 P.3d 576 (2021).


       Though not requested by either party, the district court issued the following jury
instruction No. 8 on aiding and abetting:
                                                25
              "A person is criminally responsible for a crime committed by another if the
      person, either before or during its commission, and with the mental culpability required
      to commit the crime, intentionally aids the other person to commit the crime.


              "The person who is responsible for a crime committed by another is also
      responsible for any other crime committed in carrying out or attempting to carry out the
      intended crime, if the person could reasonably foresee the other crime as a probable
      consequence of committing or attempting to commit the intended crime.


              "All participants in a crime are equally responsible without regard to the extent of
      their participation. However, mere association with another person who actually commits
      the crime or mere presence in the vicinity of the crime is insufficient to make a person
      criminally responsible for the crime.


              "It is not a defense that others who participated in the commission of the crime
      has or has not been convicted of the crime, any lesser degree of the crime, or some other
      crime based on the same act."


See K.S.A. 21-5210; PIK Crim. 4th 52.140; PIK Crim. 4th 52.150.


      This instruction sets out several related principles of accomplice liability:


      (1) A person can be guilty of a crime someone else commits if they
          knowingly and intentionally help that person commit the crime;


      (2) A person who helps commit a crime is also responsible for any other
          crimes that happen while carrying out or trying to carry out the plan, if
          those other crimes could reasonably be expected to happen;



                                                  26
       (3) Everyone who takes part in a crime is equally responsible, no matter
          how much they were involved. But just being with someone who
          commits a crime, or simply being nearby, is not enough to make you
          guilty; and


       (4) It is not a defense that the other people involved were convicted of a
          different crime, a lesser crime, or weren't convicted at all.


If the jury unanimously agreed that Volle should be held responsible for Croskey's
criminal acts under these principles of accomplice liability, Volle was criminally
responsible for the murder even if he did not fire the shot that killed Shepherd.


       K.S.A. 21-5210(a) codifies this theory of liability: "A person is criminally
responsible for a crime committed by another if such person, acting with the mental
culpability required for the commission thereof, advises, hires, counsels or procures the
other to commit the crime or intentionally aids the other in committing the conduct
constituting the crime." But mere association with a bad actor cannot establish guilt
through accomplice liability. State v. Llamas, 298 Kan. 246, 253, 311 P.3d 399 (2013).
"'[T]o be guilty of aiding and abetting a defendant must willfully and knowingly associate
himself with the unlawful venture and willfully participate in it as he would in something
he wishes to bring about or to make succeed.'" Llamas, 298 Kan. at 253; see State v.
Simmons, 282 Kan. 728, 737-39, 148 P.3d 525 (2006) (witnesses who did not participate
in robbery were not accomplices; their mere presence during the planning stages and
receipt of stolen goods as incentives for their silence did not make them liable).


       An aiding-and-abetting instruction is factually appropriate if, based on the totality
of the evidence, the jury could reasonably conclude that the defendant aided and abetted
another in the commission of the crime. State v. Shields, 315 Kan. 814, 835, 511 P.3d 931
                                             27
(2022). Volle argues that the aiding and abetting instruction was not factually appropriate
because there was no evidence that he and Croskey acted together to shoot Shepherd.
Volle notes that he and Croskey presented conflicting testimony, each blaming the other
for the shooting and claiming they were unaware that the other person had a firearm or
was planning to use it to shoot Shepherd.


       But Volle's argument seeks to narrow the scope of accomplice liability to the act
of the shooting itself and ignores evidence of his actions both before and after the
shooting. Viewed in a light most favorable to the State (as the appellate party arguing in
favor of the instruction), sufficient evidence could support a jury's finding that Volle
willfully and knowingly associated with and participated in a criminal venture beyond
mere association. The State presented evidence that Croskey wanted to fight Shepherd
and contacted Volle to be his backup. Volle willingly got into Croskey's Trailblazer and
accompanied him to follow Shepherd. During this pursuit, Volle's gun was used to fire a
gunshot from the Trailblazer, killing Shepherd. After the shooting, Volle and Croskey
went to Volle's house, where they talked about the shooting and Volle wiped fingerprints
from the gun and discussed how to sell or destroy it. Volle never contacted the police to
report the shooting and told Croskey to leave him out of it if he decided to report it.


       Thus, even if the jury could not agree on who fired the fatal shot, sufficient
evidence could support a jury's finding that Volle aided and abetted Croskey in the
killing. See State v. Blevins, 313 Kan. 413, 428, 485 P.3d 1175 (2021) (conflicting
evidence creating ambiguity as to which party pulled the trigger rendered aiding and
abetting instruction factually appropriate); Llamas, 298 Kan. at 254 ("The requisite intent
to aid and abet the inherently dangerous felony may be inferred from circumstantial
evidence."). As a result, the aiding and abetting instruction was factually appropriate.
Because the instruction was both legally and factually appropriate, the district court did
not err in giving it.
                                             28
III. Cumulative error

       Volle argues that the cumulative effect of the errors alleged above warrants
reversal of his convictions.


       Cumulative trial errors, when considered together, may require reversal of the
defendant's convictions when the totality of the circumstances establish that the defendant
was substantially prejudiced by the errors and denied a fair trial. State v. Alfaro-Valleda,
314 Kan. 526, 551, 502 P.3d 66 (2022). But the cumulative error rule does not apply
when, as here, there are no errors. See State v. Lowry, 317 Kan. 89, 100, 524 P.3d 416
(2023).


IV. Sufficiency of the evidence

       Next, Volle challenges the sufficiency of the evidence supporting his conviction
for first-degree felony murder.


               "'When the sufficiency of the evidence is challenged in a criminal case, we
       review the evidence in a light most favorable to the State to determine whether a rational
       factfinder could have found the defendant guilty beyond a reasonable doubt. An appellate
       court does not reweigh evidence, resolve conflicts in the evidence, or pass on the
       credibility of witnesses.'" Aguirre, 313 Kan. at 209.


       K.S.A. 21-5402(a)(2) defines felony murder as "the killing of a human being
committed . . . in the commission of, attempt to commit, or flight from any inherently
dangerous felony." Criminal discharge of a firearm at an occupied motor vehicle is
included in the statutory list of inherently dangerous felonies. See K.S.A. 21-
5402(c)(1)(O); K.S.A. 21-6308(a)(1)(B).

                                                   29
       Consistent with this statutory definition and the principles of accomplice liability
previously discussed, the district court instructed the jury that to find Volle guilty of
felony murder, the State had to prove that (1) Volle or another for whose conduct he is
criminally responsible killed Shepherd and (2) the killing occurred while Volle or another
for whose conduct he is criminally responsible was committing criminal discharge of a
firearm at an occupied vehicle. The court also instructed the jury that to establish the
crime of criminal discharge of a firearm at an occupied vehicle, the State was required to
prove, in relevant part:


       "1. Mr. Volle or another for whose conduct he is criminally responsible discharged
       a firearm at an occupied vehicle.


       "2. Mr. Volle or another for whose conduct he is criminally responsible did so recklessly
       and without authority.


       "3. The vehicle was occupied by a human being at the time, whether or not Mr. Volle or
       another for whose conduct he is criminally responsible knew or had reason to know it
       was occupied."


See K.S.A. 21-6308(a)(1)(B).


       Volle argues that the evidence is insufficient to support his conviction for first-
degree felony murder because the State failed to prove the predicate offense it alleged to
support his felony-murder conviction—criminal discharge of a firearm at an occupied
motor vehicle. Volle claims the evidence showed that he shot only at Shepherd, not at a
vehicle.




                                                  30
       This court rejected the same argument in State v. Farmer, 285 Kan. 541, 175 P.3d
221 (2008), and recently affirmed that decision in State v. Levy, 313 Kan. 232, 485 P.3d
605 (2021).


       In Farmer, the defendant walked up to a vehicle window and shot the driver
multiple times both at close range and while backing away from the vehicle. He was
convicted of criminal discharge of a firearm at an occupied vehicle and felony murder.
On appeal, the defendant argued the evidence was insufficient to prove criminal
discharge of a firearm at an occupied vehicle because the evidence showed he fired at the
person in the vehicle, and not at the vehicle. 285 Kan. at 544-45.


       A majority of this court rejected the argument, holding that the prior version of the
criminal discharge statute did not require the State to prove that the shooter intended to
shoot the vehicle or building:


       "The statute was designed to cover situations where there are difficulties in proving the
       shooter's intent. According to Farmer's, and the dissent's, interpretation of the criminal
       discharge statute, there cannot be any evidence of intent to shoot at anything other than
       the occupied vehicle or building itself. In other words, there must be a complete absence
       of intent to hit an occupant of an occupied vehicle or building for the statute to apply.
       Such a construction eviscerates the criminal discharge statute by putting the focus right
       back on the shooter's intent, thus making it unavailable in the very situations it was
       designed to cover—situations where proof of intent to injure or kill is problematic."
       Farmer, 285 Kan. at 546-47.


       In dissent, Justice Beier concluded that the phrase "'at [a] . . . motor vehicle'" was
not ambiguous and required proof of a specific intent to shoot at the vehicle rather than
some other target. 285 Kan. at 556 (Beier, J., concurring in part and dissenting in part)



                                                    31
("[T]here is zero evidence that Farmer shot at the vehicle in which DeAundrey Neal
happened to be sitting rather than at Neal himself.").


       In Levy, the defendant exchanged gunfire with a rival gang, which resulted in the
shooting death of an innocent victim in a nearby truck. 313 Kan. at 232-33. Relying on
Justice Beier's analysis in the Farmer dissent, the defendant challenged his felony-murder
conviction by claiming the evidence was insufficient to support the predicate crime of
criminal discharge of a firearm at an occupied vehicle because the evidence showed only
that he intended to fire at a rival gang member, not at an occupied vehicle. 313 Kan. at
234-35. This court declined the defendant's invitation to revisit its decision in Farmer:


       "In Kansas, the crime of criminal discharge does not require a specific intent to shoot 'at a
       motor vehicle' as opposed to at some other target—whether that target is inside the
       vehicle, hiding behind the vehicle, or only nearby the vehicle. This conclusion is further
       supported by the legislative amendments to the criminal discharge statute altering the
       necessary state of mind to 'reckless.' Compare K.S.A. 2006 Supp. 21-4219(b)
       (criminalizing 'the malicious, intentional and unauthorized discharge of a firearm') with
       K.S.A. 2020 Supp. 21-6308(a)(1)(b) (changing the mens rea to 'reckless'). Putting all this
       together, a person has committed the crime of criminal discharge under K.S.A. 2020
       Supp. 21-6308(a)(1)(B) if: (1) that person recklessly and without authorization discharges
       a firearm; (2) that discharge was 'at a motor vehicle' independent of the shooter's intended
       target; and (3) a person was inside the vehicle." Levy, 313 Kan. at 236.


       Volle acknowledges this court's precedent in Farmer and Levy but disagrees with
the analysis in those cases, claiming it is contrary to the plain language of K.S.A. 21-
6308(a)(1)(B)—which requires that the firearm be discharged at an occupied vehicle—
and renders the phrase "at a motor vehicle" meaningless. He argues these cases were
wrongly decided because they focus on the shooter's intent rather than the shooter's
actions. Citing evidence in the record that the gun was only fired when its laser was
positioned on Shepherd and that no bullets hit Shepherd's car, Volle claims he did not
                                                    32
violate the statute because he did not fire at an occupied vehicle. Given the ambiguity of
K.S.A. 21-6308(a)(1)(B), Volle suggests the rule of lenity requires the statute to be
construed in his favor.


       Volle offers no compelling reason to deviate from our prior rulings in Farmer and
Levy. These decisions are not in conflict with K.S.A. 21-6308(a)(1)(B)'s plain language,
they do not render the phrase "at a motor vehicle" meaningless, and they do not focus on
the shooter's intent. To the contrary, Farmer and Levy both discussed how the criminal
discharge statute removed the focus from the shooter's intent. See Farmer, 285 Kan. at
546 ("The statute was designed to cover situations where there are difficulties in proving
the shooter's intent."); Levy, 313 Kan. at 236 (discussing legislative amendments to the
criminal discharge statute altering the necessary state of mind to "reckless").


       As discussed, to prove the offense of criminal discharge of a firearm at an
occupied motor vehicle, the State was required to prove that Volle (or another whose
conduct he was criminally responsible for): (1) recklessly discharged a firearm (2) at a
motor vehicle (3) with a person inside. See K.S.A. 21-6308(a)(1)(B); Levy, 313 Kan. at
236. The evidence presented at trial established that Shepherd was standing inside the
open driver's side door of his car when he was shot and that Megan was inside the car.
Although the shot did not hit the car, it need not do so to meet the elements of the crime
and does not negate the fact that the shot was fired at a motor vehicle occupied by
Megan. Viewing the evidence in the light most favorable to the State, a rational factfinder
could find Volle guilty beyond a reasonable doubt of the crime of criminal discharge of a
firearm at an occupied motor vehicle. As a result, the evidence was sufficient to support
Volle's felony-murder conviction.




                                             33
V. Sentencing


       Finally, Volle contends the district court erred when it sentenced him for his
felony-murder conviction because his conviction for reckless second-degree murder was
more specific and therefore should control his sentence under K.S.A. 21-5109(d).


       Resolving this issue requires statutory interpretation, which presents a question of
law over which appellate courts have unlimited review. State v. Betts, 316 Kan. 191, 197,
514 P.3d 341 (2022). When interpreting a statute, an appellate court must first attempt to
give effect to the intent of the Legislature through the statutory language enacted, giving
common words their ordinary meanings. When a statute is plain and unambiguous, an
appellate court should not speculate about the legislative intent behind that clear
language, and it should refrain from reading something into the statute that is not readily
found in its words. State v. Keys, 315 Kan. 690, 698, 510 P.3d 706 (2022).


       K.S.A. 21-5109(a) provides that a defendant may be charged with multiple crimes
stemming from the same conduct in different counts within a single complaint. But when
the crimes alleged "differ only in that one is defined to prohibit a designated kind of
conduct generally and the other to prohibit a specific instance of such conduct," the
defendant can be convicted only of one of the crimes and must be sentenced "according
to the terms of the more specific crime." K.S.A. 21-5109(d).


       Here, the jury found Volle guilty of felony murder and the alternative lesser
included offense of reckless second-degree murder. Felony murder is "the killing of a
human being committed . . . in the commission of, attempt to commit, or flight from any
inherently dangerous felony." K.S.A. 21-5402(a)(2). Reckless second-degree murder is
"the killing of a human being committed . . . unintentionally but recklessly under


                                             34
circumstances manifesting extreme indifference to the value of human life." K.S.A. 21-
5403(a)(2).


       Volle suggests that because his convictions for the two crimes were based on the
same conduct, reckless second-degree murder criminalizes more specific conduct since it
requires a mental state of recklessness, while felony murder does not require a culpable
mental state.


       Volle's argument misinterprets K.S.A. 21-5109(d). Although the same conduct
may support both felony murder and reckless second-degree murder, as it did here, the
felony-murder and reckless second-degree murder statutes are aimed at preventing
different conduct and require different elements of proof and different levels of mental
culpability. While both involve an unintentional killing, felony murder "requires proof
the defendant engaged in dangerous, felonious conduct and that a death occurred as a
result of that conduct." State v. Patterson, 311 Kan. 59, 67, 455 P.3d 792 (2020); see
K.S.A. 21-5402(a)(2) (felony murder requires proof of inherently dangerous felony). By
contrast, reckless second-degree murder does not require a defendant to engage in
dangerous, felonious conduct. Rather, the unintentional killing is borne out of reckless
conduct. State v. Deal, 293 Kan. 872, 883-84, 269 P.3d 1282 (2012); see K.S.A. 21-
5202(j) ("A person acts 'recklessly' or is 'reckless,' when such person consciously
disregards a substantial and unjustifiable risk that circumstances exist or that a result will
follow, and such disregard constitutes a gross deviation from the standard of care which a
reasonable person would exercise in the situation."); State v. Johnson, 304 Kan. 924, Syl.
¶ 5, 376 P.3d 70 (2016) (Reckless second-degree murder is not purposeful, willful, or
knowing, but results from an act performed with knowledge that the victim is in
imminent danger, although death is not foreseen.). In sum, neither crime is more general
nor more specific than the other because each targets a different theory of liability.
Because the reckless second-degree murder statute does not punish a more specific
                                              35
instance of conduct generally prohibited by the felony-murder statute, K.S.A. 21-5109(d)
does not apply to Volle's convictions.


       Moreover, although not discussed by either party, we find the district court
correctly sentenced Volle for felony murder based on Kansas' rules governing
convictions and sentencing for alternative charges. A defendant charged in the alternative
may be convicted of only one of the alternative offenses. State v. Garza, 290 Kan. 1021,
Syl. ¶ 5, 236 P.3d 501 (2010). When a jury returns guilty verdicts on two alternatively
charged counts, the doctrine of merger applies, and the district court must accept only the
verdict as to the greater charge. State v. Vargas, 313 Kan. 866, 873, 492 P.3d 412 (2021).


       The jury returned a verdict finding Volle guilty of both first-degree felony murder
and reckless second-degree murder—a lesser included offense of first-degree
premeditated murder, which the State had charged in the alternative. At sentencing, the
district court merged the murder convictions into a single conviction for first-degree
felony murder and sentenced Volle for that crime. Reckless second-degree murder is a
severity level 2, person felony. K.S.A. 21-5403(b)(2). First-degree murder is an off-grid
felony. K.S.A. 21-5402(b). Accordingly, the district court correctly applied the doctrine
of merger and sentenced Volle on the greater charge of felony murder.


       Finally, we acknowledge Volle's submission under Supreme Court Rule 6.09(b)
(2025 Kan. S. Ct. R. at 41) directing our attention to State v. Johnson, 321 Kan. ___,
2025 WL 3289978 (2025). Contrary to Volle's claim, Johnson's interpretation of K.S.A.
21-5109(d) aligns with—and confirms—the analysis and outcome we reach in this case.


       The judgment of the district court is affirmed.




                                            36

```

---

## GROUP: content/cases/Tanzin v. Tanvir.md  (`case`, 5 assertions)

### content_page

```
---
title: Tanzin v. Tanvir
type: case
citation: "592 U.S. 43 (2020)"
parallel_cite: "141 S. Ct. 486; 208 L. Ed. 2d 295"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2020
date_decided: ""
docket: 19-71
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
  opinion_url: "https://www.courtlistener.com/opinion/4837663/tanzin-v-tanvir/"
  cluster_id: 4837663
  opinion_id: null
  identity_checked: true
lake:
  record_id: Tanzin v. Tanvir
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - rfra
  - federal-officer-liability
  - money-damages
  - first-amendment
holding: "The Religious Freedom Restoration Act's authorization of 'appropriate relief against a government' permits a plaintiff to recover money damages against federal officials sued in their individual capacities for burdening religious exercise."
---

# Tanzin v. Tanvir

*592 U.S. 43 (2020)* (No. 19-71) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4837663 → opinion 4641442; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "592 U. S. ____ (2020)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Muhammad Tanvir and other practicing Muslims alleged that FBI agents placed them on the No Fly List in retaliation for their refusal to act as informants against their religious communities. They sued under the Religious Freedom Restoration Act (RFRA), seeking injunctive relief against the agents in their official capacities and money damages against the agents in their individual capacities. The District Court held that RFRA does not authorize monetary relief and dismissed the individual-capacity claims; the Second Circuit reversed, holding that RFRA's remedies provision reaches money damages against government officials.

## Issue
Whether RFRA's authorization of "appropriate relief against a government" includes claims for money damages against federal officials sued in their individual capacities.

## Rule
RFRA lets a person whose religious exercise is unlawfully burdened "obtain appropriate relief against a government," and expressly defines "government" to include an "official (or other person acting under color of law) of the United States." The phrase "under color of law" carries the meaning long given it in the 42 U.S.C. § 1983 context, where it permits suits against officials in their individual capacities; and "appropriate relief" is open-ended and context-dependent, with damages historically available against government officials. The Court framed and answered the question directly: the issue "is whether 'appropriate relief' includes claims for money damages against Government officials in their individual capacities. We hold that it does." — 592 U.S. 43 (slip op., at 1). ^pin-op

## Application
When RFRA was enacted its definition of "government" included state and local officials, and to restore the pre-*Smith* protections and the right to vindicate them by a claim, its remedies had to encompass at least the relief available under § 1983 — which has always allowed damages for clearly established First Amendment violations. The *Sossamon* presumption against damages did not apply, because a suit against officials in their individual capacities does not implicate sovereign immunity.

## Conclusion
The judgment of the Second Circuit was **affirmed**. Thomas, J., delivered the opinion of the Court, in which all other Members joined, except Barrett, J., who took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Tanzin* establishes a money-damages remedy against federal officers personally under RFRA, paralleling the individual-capacity exposure long recognized under § 1983 and sharpening the stakes of official conduct that substantially burdens religious exercise.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Tanzin v. Tanvir*, 592 U.S. 43 (2020)](https://www.courtlistener.com/opinion/4837663/tanzin-v-tanvir/) — pinpoint: slip op., at 1 (Opinion of the Court, holding; Thomas, J.). CL carries the slip opinion ("592 U. S. ____ (2020)"; cluster 4837663 → opinion 4641442); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1a0702a1c9581548", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "592 U.S. 43 (2020)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "141 S. Ct. 486; 208 L. Ed. 2d 295", "title": "Tanzin v. Tanvir", "year": "2020"}}
{"assertion_id": "3214570d55646935", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Religious Freedom Restoration Act's authorization of 'appropriate relief against a government' permits a plaintiff to recover money damages against federal officials sued in their individual capacities for burdening religious exercise.", "title": "Tanzin v. Tanvir"}}
{"assertion_id": "c6244556ca61d8b4", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Tanzin v. Tanvir"}}
{"assertion_id": "515ba5b2fecf5d32", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Tanzin v. Tanvir", "varies_by_point": "false"}}
{"assertion_id": "6b07c082b51e1062", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Tanzin v. Tanvir"}}
```

### lake record — Tanzin v. Tanvir

```json
{
  "schema_version": "s2.v1",
  "record_id": "Tanzin v. Tanvir",
  "status": "under_review",
  "identity": {
    "case_name": "Tanzin v. Tanvir",
    "case_name_short": "Tanzin",
    "case_name_full": "",
    "input_case_name": "Tanzin v. Tanvir",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2020,
    "docket": "19-71",
    "cluster_id": 4837663,
    "lead_opinion_id": 4641442,
    "sibling_ids": [],
    "absolute_url": "/opinion/4837663/tanzin-v-tanvir/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 43",
      "volume": "592",
      "reporter": "U.S.",
      "page": "43",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 486",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 295",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 43",
        "volume": "592",
        "reporter": "U.S.",
        "page": "43",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 486",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 295",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "295",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 43",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 43",
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
    "date_created": "2026-07-06T12:09:45Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:09:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "tanzin-v-tanvir--4837663",
      "to_record_id": "Tanzin v. Tanvir",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Tanzin v. Tanvir

```
(Slip Opinion)              OCTOBER TERM, 2020                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                  TANZIN ET AL. v. TANVIR ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE SECOND CIRCUIT

   No. 19–71.      Argued October 6, 2020—Decided December 10, 2020
The Religious Freedom Restoration Act of 1993 (RFRA) was enacted in
  the wake of Employment Div., Dept. of Human Resources of Ore. v.
  Smith, 494 U. S. 872, to provide a remedy to redress Federal Govern-
  ment violations of the right to free exercise under the First Amend-
  ment. Respondents are practicing Muslims who sued under RFRA,
  claiming that federal agents placed them on the No Fly List for refus-
  ing to act as informants against their religious communities. They
  sought injunctive relief against the agents in their official capacities
  and monetary damages against the agents in their individual capaci-
  ties. As relevant here, the District Court found that RFRA does not
  permit monetary relief and dismissed their individual-capacity claims.
  The Second Circuit reversed, holding that RFRA’s remedies provision
  encompasses money damages against Government officials.
Held: RFRA’s express remedies provision permits litigants, when appro-
 priate, to obtain money damages against federal officials in their indi-
 vidual capacities. Pp. 3–9.
    (a) RFRA’s text provides that persons may sue and “obtain appro-
 priate relief against a government,” 42 U. S. C. §2000bb–1(c), includ-
 ing an “official (or other person acting under color of law) of the United
 States,” §2000bb–2(1). RFRA supplants the ordinary meaning of “gov-
 ernment” with a different, express definition that includes “official[s].”
 It then underscores that “official[s]” are “person[s].” Under RFRA’s
 definition, relief that can be executed against an “official . . . of the
 Unites States” is “relief against a government.” This reading is con-
 firmed by RFRA’s use of the phrase “persons acting under color of law,”
 which has long been interpreted by this Court in the 42 U. S. C. §1983
 context to permit suits against officials in their individual capacities.
 See, e.g., Memphis Community School Dist. v. Stachura, 477 U. S. 299,
2                           TANZIN v. TANVIR

                                  Syllabus

    305–306. Pp. 3–5.
       (b) RFRA’s term “appropriate relief” is “open-ended” on its face;
    thus, what relief is “ ‘appropriate’ ” is “inherently context dependent.”
    Sossamon v. Texas, 563 U. S. 277, 286. In the context of suits against
    Government officials, damages have long been awarded as appropriate
    relief, and though more limited today, they remain an appropriate
    form of relief. The availability of damages under §1983 is particularly
    salient here. When Congress first enacted RFRA, the definition of
    “government” included state and local officials. In order to reinstate
    the pre-Smith substantive protections of the First Amendment and the
    right to vindicate those protections by a claim, §2000bb(b), the reme-
    dies provision must have encompassed at least the same forms of relief
    authorized by §1983. Because damages claims have always been avail-
    able under §1983 for clearly established violations of the First Amend-
    ment, that means RFRA provides, as one avenue for relief, a right to
    seek damages against Government employees. The presumption in
    Sossamon, 563 U. S. 277, is inapplicable because this case does not in-
    volve sovereign immunity. Pp. 5–9.
894 F. 3d 449, affirmed.

  THOMAS, J., delivered the opinion of the Court, in which all other Mem-
bers joined, except BARRETT, J., who took no part in the consideration or
decision of the case.
                        Cite as: 592 U. S. ____ (2020)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–71
                                    _________________


 FNU TANZIN, ET AL., PETITIONERS v. MUHAMMAD
                 TANVIR, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                               [December 10, 2020]

   JUSTICE THOMAS delivered the opinion of the Court.
   The Religious Freedom Restoration Act of 1993 (RFRA)
prohibits the Federal Government from imposing substan-
tial burdens on religious exercise, absent a compelling in-
terest pursued through the least restrictive means. 107
Stat. 1488, 42 U. S. C. §2000bb et seq. It also gives a person
whose religious exercise has been unlawfully burdened the
right to seek “appropriate relief.” The question here is
whether “appropriate relief ” includes claims for money
damages against Government officials in their individual
capacities. We hold that it does.
                               I
                              A
  RFRA secures Congress’ view of the right to free exercise
under the First Amendment, and it provides a remedy to
redress violations of that right. Congress passed the Act in
the wake of this Court’s decision in Employment Div., Dept.
of Human Resources of Ore. v. Smith, 494 U. S. 872, 885–
890 (1990), which held that the First Amendment tolerates
neutral, generally applicable laws that burden or prohibit
2                     TANZIN v. TANVIR

                      Opinion of the Court

religious acts even when the laws are unsupported by a nar-
rowly tailored, compelling governmental interest. See
§2000bb(a). RFRA sought to counter the effect of that hold-
ing and restore the pre-Smith “compelling interest test” by
“provid[ing] a claim . . . to persons whose religious exercise
is substantially burdened by government.” §§2000bb(b)(1)–
(2). That right of action enables a person to “obtain appro-
priate relief against a government.” §2000bb–1(c). A “ ‘gov-
ernment’ ” is defined to include “a branch, department,
agency, instrumentality, and official (or other person acting
under color of law) of the United States.” §2000bb–2(1).
                               B
   Respondents Muhammad Tanvir, Jameel Algibhah, and
Naveed Shinwari are practicing Muslims who claim that
Federal Bureau of Investigation agents placed them on the
No Fly List in retaliation for their refusal to act as inform-
ants against their religious communities. Respondents
sued various agents in their official capacities, seeking re-
moval from the No Fly List. They also sued the agents in
their individual capacities for money damages. According
to respondents, the retaliation cost them substantial sums
of money: airline tickets wasted and income from job oppor-
tunities lost.
   More than a year after respondents sued, the Department
of Homeland Security informed them that they could now
fly, thus mooting the claims for injunctive relief. The Dis-
trict Court then dismissed the individual-capacity claims
for money damages, ruling that RFRA does not permit mon-
etary relief.
   The Second Circuit reversed. 894 F. 3d 449 (2018). It
determined that RFRA’s express remedies provision, com-
bined with the statutory definition of “Government,” au-
thorizes claims against federal officials in their individual
capacities. Relying on our precedent and RFRA’s broad pro-
tections for religious liberty, the court concluded that the
                  Cite as: 592 U. S. ____ (2020)              3

                      Opinion of the Court

open-ended phrase “appropriate relief ” encompasses
money damages against officials. We granted certiorari,
589 U. S. ___ (2019), and now affirm.
                              II
  As usual, we start with the statutory text. E.g., Mission
Product Holdings, Inc. v. Tempnology, LLC, 587 U. S. ___,
___ (2019) (slip op., at 8). A person whose exercise of reli-
gion has been unlawfully burdened may “obtain appropri-
ate relief against a government.” 42 U. S. C. §2000bb–1(c).
                                 A
   We first have to determine if injured parties can sue Gov-
ernment officials in their personal capacities. RFRA’s text
provides a clear answer: They can. Persons may sue and
obtain relief “against a government,” §2000bb–1(c), which
is defined to include “a branch, department, agency, instru-
mentality, and official (or other person acting under color of
law) of the United States.” §2000bb–2(1) (emphasis added).
   The Government urges us to limit lawsuits against offi-
cials to suits against them in their official, not personal, ca-
pacities. A lawsuit seeking damages from employees in
their individual capacities, the Government argues, is not
really “against a government” because relief “can be exe-
cuted only against the official’s personal assets.” Kentucky
v. Graham, 473 U. S. 159, 166 (1985).
   The problem with this otherwise plausible argument is
that Congress supplanted the ordinary meaning of “govern-
ment” with a different, express definition. “ ‘When a statute
includes an explicit definition, we must follow that defini-
tion,’ even if it varies from a term’s ordinary meaning.” Dig-
ital Realty Trust, Inc. v. Somers, 583 U. S. ___, ___ (slip op.,
at 9) (quoting Burgess v. United States, 553 U. S. 124, 130
(2008)). For example, if a statute defines a “State” to in-
clude territories and districts, that addition to the plain
meaning controls. See, e.g., 15 U. S. C. §267. So too here.
4                     TANZIN v. TANVIR

                      Opinion of the Court

A “government,” under RFRA, extends beyond the term’s
plain meaning to include officials. And the term “official”
does not refer solely to an office, but rather to the actual
person “who is invested with an office.” 10 Oxford English
Dictionary 733 (2d ed. 1989). Under RFRA’s definition, re-
lief that can be executed against an “official . . . of the
United States” is “relief against a government.” 42 U. S. C.
§§2000bb–1(c), 2000bb–2(1).
   Not only does the term “government” encompass officials,
it also authorizes suits against “other person[s] acting un-
der color of law.” §2000bb–2(1). The right to obtain relief
against “a person” cannot be squared with the Govern-
ment’s reading that relief must always run against the
United States. Moreover, the use of the phrase “official (or
other person . . . )” underscores that “official[s]” are treated
like “person[s].” Ibid. (emphasis added). In other words,
the parenthetical clarifies that “a government” includes
both individuals who are officials acting under color of law
and other, additional individuals who are nonofficials act-
ing under color of law. Here, respondents sued the former.
   The legal “backdrop against which Congress enacted”
RFRA confirms the propriety of individual-capacity suits.
Stewart v. Dutra Constr. Co., 543 U. S. 481, 487 (2005). The
phrase “persons acting under color of law” draws on one of
the most well-known civil rights statutes: 42 U. S. C. §1983.
That statute applies to “person[s] . . . under color of any
statute,” and this Court has long interpreted it to permit
suits against officials in their individual capacities. See,
e.g., Memphis Community School Dist. v. Stachura, 477
U. S. 299, 305–306, and n. 8 (1986). Because RFRA uses
the same terminology as §1983 in the very same field of civil
rights law, “it is reasonable to believe that the terminology
bears a consistent meaning.” A. Scalia & B. Garner, Read-
ing Law: The Interpretation of Legal Texts 323 (2012). A
suit against an official in his personal capacity is a suit
against a person acting under color of law. And a suit
                  Cite as: 592 U. S. ____ (2020)             5

                      Opinion of the Court

against a person acting under color of law is a suit against
“a government,” as defined under RFRA. §2000bb–1(c).
                               B
   The question then becomes what “appropriate relief ” en-
tails. Without a statutory definition, we turn to the
phrase’s plain meaning at the time of enactment. See FCC
v. AT&T Inc., 562 U. S. 397, 403 (2011). “Appropriate”
means “[s]pecially fitted or suitable, proper.” 1 Oxford Eng-
lish Dictionary, at 586; see also Merriam-Webster’s Colle-
giate Dictionary 57 (10th ed. 1996) (“especially suitable or
compatible”). Because this language is “open-ended” on its
face, what relief is “ ‘appropriate’ ” is “inherently context
dependent.” Sossamon v. Texas, 563 U. S. 277, 286 (2011)
(interpreting identical language).
   In the context of suits against Government officials, dam-
ages have long been awarded as appropriate relief. In the
early Republic, “an array of writs . . . allowed individuals to
test the legality of government conduct by filing suit
against government officials” for money damages “payable
by the officer.” Pfander & Hunt, Public Wrongs and Private
Bills: Indemnification and Govt Accountability in the Early
Republic, 85 N. Y. U. L. Rev. 1862, 1871–1875 (2010); see
id., at 1875, n. 52 (collecting cases). These common-law
causes of action remained available through the 19th cen-
tury and into the 20th. See, e.g., Little v. Barreme, 2 Cranch
170 (1804); Elliott v. Swartwout, 10 Pet. 137 (1836); Mitch-
ell v. Harmony, 13 How. 115 (1852); Buck v. Colbath, 3
Wall. 334 (1866); Belknap v. Schild, 161 U. S. 10 (1896);
Philadelphia Co. v. Stimson, 223 U. S. 605, 619–620 (1912)
(“The exemption of the United States from suit does not pro-
tect its officers from personal liability to persons whose
rights of property they have wrongfully invaded”).
   Though more limited, damages against federal officials
remain an appropriate form of relief today. In 1988 the
Westfall Act foreclosed common-law claims for damages
6                     TANZIN v. TANVIR

                      Opinion of the Court

against federal officials, 28 U. S. C. §2679, but it left open
claims for constitutional violations and certain statutory vi-
olations. §§2679(b)(2)(A)–(B). Indeed, the Act expressly
contemplates that a statute could authorize an action for
damages against Government employees. §2679(b)(2)(B)
(explaining that the displacement of remedies “does not ex-
tend or apply to a civil action against an employee of the
Government . . . which is brought for a violation of a statute
of the United States under which such action against an in-
dividual is otherwise authorized”).
   Damages are also commonly available against state and
local government officials. In 1871, for example, Congress
passed the precursor to §1983, imposing liability on any
person who, under color of state law, deprived another of a
constitutional right. 17 Stat. 13; see also Myers v. Ander-
son, 238 U. S. 368, 379, 383 (1915) (affirming award of dam-
ages against state election officials). By the time Congress
enacted RFRA, this Court had interpreted the modern ver-
sion of §1983 to permit monetary recovery against officials
who violated “clearly established” federal law. E.g., Procu-
nier v. Navarette, 434 U. S. 555, 561–562 (1978); Siegert v.
Gilley, 500 U. S. 226, 231 (1991).
   This availability of damages under §1983 is particularly
salient in light of RFRA’s origins. When first enacted,
RFRA defined “ ‘government’ ” to include an “official (or
other person acting under color of law) of the United States,
a State, or a subdivision of a State.” 107 Stat. 1489 (empha-
sis added). It made no distinction between state and federal
officials. After this Court held that RFRA could not be en-
forced against the States, see City of Boerne v. Flores, 521
U. S. 507, 511 (1997), Congress narrowly amended the def-
inition “by striking ‘a State, or a subdivision of a State.’ ”
114 Stat. 806. That context is important because RFRA
made clear that it was reinstating both the pre-Smith sub-
stantive protections of the First Amendment and the right
to vindicate those protections by a claim. §2000bb(b).
                  Cite as: 592 U. S. ____ (2020)            7

                      Opinion of the Court

There is no doubt that damages claims have always been
available under §1983 for clearly established violations of
the First Amendment. See, e.g., Sause v. Bauer, 585 U. S.
___ (2018) (per curiam) (reversing grant of qualified im-
munity in a case seeking damages under §1983 based on
alleged violations of free exercise rights and Fourth Amend-
ment rights); Murphy v. Missouri Dept. of Corrections, 814
F. 2d 1252, 1259 (CA8 1987) (remanding to enter judgment
for plaintiffs on a §1983 free speech and free exercise claims
and to determine and order “appropriate relief, which . . .
may, if appropriate, include an award” of damages). Given
that RFRA reinstated pre-Smith protections and rights,
parties suing under RFRA must have at least the same av-
enues for relief against officials that they would have had
before Smith. That means RFRA provides, as one avenue
for relief, a right to seek damages against Government em-
ployees.
   A damages remedy is not just “appropriate” relief as
viewed through the lens of suits against Government em-
ployees. It is also the only form of relief that can remedy
some RFRA violations. For certain injuries, such as re-
spondents’ wasted plane tickets, effective relief consists of
damages, not an injunction. See, e.g., DeMarco v. Davis,
914 F. 3d 383, 390 (CA5 2019) (destruction of religious prop-
erty); Yang v. Sturner, 728 F. Supp. 845 (RI 1990), opinion
withdrawn 750 F. Supp. 558 (RI 1990) (autopsy of son that
violated Hmong beliefs). Given the textual cues just noted,
it would be odd to construe RFRA in a manner that prevents
courts from awarding such relief. Had Congress wished to
limit the remedy to that degree, it knew how to do so. See,
e.g., 29 U. S. C. §1132(a)(3) (providing for “appropriate eq-
uitable relief ”); 42 U. S. C. §2000e–5(g)(1) (providing for
“equitable relief as the court deems appropriate”); 15
U. S. C. §78u(d)(5) (providing for “any equitable relief that
8                          TANZIN v. TANVIR

                           Opinion of the Court

may be appropriate or necessary”).*
   Our opinion in Sossamon does not change this analysis.
Sossamon held that a State’s acceptance of federal funding
did not waive sovereign immunity to suits for damages un-
der a related statute—the Religious Land Use and Institu-
tionalized Persons Act of 2000—which also permits “ ‘appro-
priate relief.’ ” 563 U. S., at 280, 282. The obvious
difference is that this case features a suit against individu-
als, who do not enjoy sovereign immunity.
   The Government also posits that we should be wary of
damages against government officials because these
awards could raise separation-of-powers concerns. But this
exact remedy has coexisted with our constitutional system
since the dawn of the Republic. To be sure, there may be
policy reasons why Congress may wish to shield Govern-
ment employees from personal liability, and Congress is
free to do so. But there are no constitutional reasons why
we must do so in its stead.
   To the extent the Government asks us to create a new
policy-based presumption against damages against individ-
ual officials, we are not at liberty to do so. Congress is best
suited to create such a policy. Our task is simply to inter-
pret the law as an ordinary person would. Although back-
ground presumptions can inform the understanding of a
word or phrase, those presumptions must exist at the time
of enactment. We cannot manufacture a new presumption
now and retroactively impose it on a Congress that acted 27
years ago.

——————
  * Both the Government and respondents agree that government offi-
cials are entitled to assert a qualified immunity defense when sued in
their individual capacities for money damages under RFRA. Indeed, re-
spondents emphasize that the “qualified immunity defense was created
for precisely these circumstances,” Brief for Respondents 22, and is a
“powerful shield” that “protects all but the plainly incompetent or those
who flout clearly established law,” Tr. of Oral Arg. 42; see District of Co-
lumbia v. Wesby, 583 U. S. ___, ___–___ (2018) (slip op., at 13–15).
                  Cite as: 592 U. S. ____ (2020)             9

                      Opinion of the Court

                         *     *     *
  We conclude that RFRA’s express remedies provision per-
mits litigants, when appropriate, to obtain money damages
against federal officials in their individual capacities. The
judgment of the United States Court of Appeals for the Sec-
ond Circuit is affirmed.
                                              It is so ordered.

  JUSTICE BARRETT took no part in the consideration or
decision of this case.

```

---

## GROUP: content/cases/Taylor v. Riojas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Taylor v. Riojas"
type: case
citation: "592 U.S. 7 (2020)"
parallel_cite: "141 S. Ct. 52; 208 L. Ed. 2d 164"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2020
date_decided: 2020-11-02
docket: 19-1261
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2020-11-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Taylor v. Riojas
  varies_by_point: false
  scope_note: "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4802501/taylor-v-riojas/"
  cluster_id: 4802501
  opinion_id: 4582848
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Limiting"
related: ["[[White v. Pauly]]", "[[Mullenix v. Luna]]", "[[Harlow v. Fitzgerald]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "clearly-established", "obvious-case", "eighth-amendment"]
holding: "Qualified immunity can be defeated without a case directly on point where the constitutional violation is so obvious that any reasonable officer would have known the conduct was unlawful."
lake:
  record_id: Taylor v. Riojas
  status: verified
  projected_at: 2026-07-06
---

# Taylor v. Riojas

*592 U.S. 7 (2020)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Trent Taylor, a Texas inmate, alleged that for six days correctional officers confined him in two "shockingly unsanitary cells": the first covered nearly floor to ceiling in massive amounts of feces, and the second a frigid cell with only a clogged floor drain, where — left naked and without a bunk — he was forced to sleep in raw sewage that overflowed the drain. The Fifth Circuit held these conditions violated the Eighth Amendment but granted the officers [[Qualified Immunity|qualified immunity]] because no prior case had clearly established that such conditions, for "only six days," were unconstitutional.

## Issue
Whether officers were entitled to [[Qualified Immunity|qualified immunity]] for these conditions of confinement merely because no prior decision had specifically addressed materially similar facts.

## Rule
No. Where the unconstitutionality of conduct is obvious, [[Qualified Immunity|qualified immunity]] does not require a prior case on point. "no reasonable correctional officer could have concluded that, under the extreme circumstances of this case, it was constitutionally permissible to house Taylor in such deplorably unsanitary conditions for such an extended period of time." — 592 U.S. 7 (slip op., at 2). ^pin-7

Invoking *[[Hope v. Pelzer]]*, the Court reiterated that "a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question." "Confronted with the particularly egregious facts of this case, any reasonable officer should have realized that Taylor's conditions of confinement offended the Constitution." — *Id.* (slip op., at 3). ^pin-7b

## Application
The egregiousness of the conditions — cells teeming with human waste, with no necessity or [[Exigent Circumstances and Hot Pursuit|exigency]] shown and no reason the conditions could not have been mitigated — made the violation obvious, so the absence of a factually identical precedent did not entitle the officers to immunity. The Fifth Circuit's lone contrary case was "too dissimilar, in terms of both conditions and duration of confinement, to create any doubt about the obviousness of Taylor's right." The Court noted that an officer-by-officer analysis would still be required [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted, judgment [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). [[Qualified Immunity|Qualified immunity]] was wrongly granted; the obvious unconstitutionality of the conditions provided the officers fair warning even without a case directly on point.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Taylor* is a leading modern application of the *[[Hope v. Pelzer]]* "obvious case" route to defeating [[Qualified Immunity|qualified immunity]], a counterweight to the high-specificity decisions like [[Mullenix v. Luna]] and [[White v. Pauly]]. The same Term, the Court relied on it to GVR a related Fifth Circuit case (*McCoy v. Alamu*). No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Limiting*

## Sources
- *Taylor v. Riojas*, 592 U.S. 7 (2020) (per curiam) — https://www.courtlistener.com/opinion/4802501/taylor-v-riojas/ — pinpoint: slip op., at 2–3 (CL stores the slip opinion "592 U. S. ____ (2020)"; pin keyed to the official case-start page 7).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0cefecab8cb5e96d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "592 U.S. 7 (2020)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "141 S. Ct. 52; 208 L. Ed. 2d 164", "title": "Taylor v. Riojas", "year": "2020"}}
{"assertion_id": "051a6af16ab226c0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Qualified immunity can be defeated without a case directly on point where the constitutional violation is so obvious that any reasonable officer would have known the conduct was unlawful.", "title": "Taylor v. Riojas"}}
{"assertion_id": "26147ba472b3e3ca", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Limiting", "title": "Taylor v. Riojas"}}
{"assertion_id": "d42041908bbc7c5b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2020-11-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Taylor v. Riojas", "field_i_validity": "good_law", "scope_note": "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point.", "title": "Taylor v. Riojas", "varies_by_point": "false"}}
{"assertion_id": "d50f09f6673690dd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Taylor v. Riojas"}}
```

### lake record — Taylor v. Riojas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Taylor v. Riojas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Taylor v. Riojas",
    "case_name_short": "Taylor",
    "case_name_full": "",
    "input_case_name": "Taylor v. Riojas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2020-11-02",
    "year": 2020,
    "docket": "19-1261",
    "cluster_id": 4802501,
    "lead_opinion_id": 4582848,
    "sibling_ids": [
      4582848
    ],
    "absolute_url": "/opinion/4802501/taylor-v-riojas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 7",
      "volume": "592",
      "reporter": "U.S.",
      "page": "7",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 52",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 164",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 7",
        "volume": "592",
        "reporter": "U.S.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 52",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "52",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "208 L. Ed. 2d 164",
        "volume": "208",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 7",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 7",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-7",
      "page": null,
      "quote": "were unconstitutional. ## Issue Whether officers were entitled to qualified immunity for these conditions of confinement merely because no prior decision had specifically addressed materially similar facts. ## Rule No. Where the unconstitutionality of conduct is obvious, qualified immunity does not require a prior case on point.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-7b",
      "page": null,
      "quote": "a general constitutional rule already identified in the decisional law may apply with obvious clarity to the specific conduct in question.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2020-11-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Taylor v. Riojas",
    "varies_by_point": false,
    "scope_note": "Per curiam; good law on the 'obvious case' route to defeating qualified immunity without a case directly on point.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gail Stockton v. Milwaukee County, Wisconsin",
          "cluster_id": 7855452,
          "cite": [
            "44 F.4th 605"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Percy Taylor v. Joseph Ways",
          "cluster_id": 4888555,
          "cite": [
            "999 F.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Seth Michael Zakora v. Troy Chrisman",
          "cluster_id": 7855600,
          "cite": [
            "44 F.4th 452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguirre v. City of San Antonio",
          "cluster_id": 4876506,
          "cite": [
            "995 F.3d 395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marie Moderwell v. Cuyahoga Cnty., Ohio",
          "cluster_id": 4882339,
          "cite": [
            "997 F.3d 653"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cope v. Cogdill",
          "cluster_id": 4897232,
          "cite": [
            "3 F.4th 198"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "David King v. Timothy Riley",
          "cluster_id": 9418866,
          "cite": [
            "76 F.4th 259"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Thorpe v. Harold Clarke",
          "cluster_id": 7454730,
          "cite": [
            "37 F.4th 926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trellus Richmond v. Mario J. Badia",
          "cluster_id": 7858519,
          "cite": [
            "47 F.4th 1172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James O'Doan v. Joshua Sanford",
          "cluster_id": 4865836,
          "cite": [
            "991 F.3d 1027"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. John Yost",
          "cluster_id": 9385401,
          "cite": [
            "63 F.4th 211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timothy Finley v. Erica Huss",
          "cluster_id": 9506473,
          "cite": [
            "102 F.4th 789"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernando Lopez v. Sheriff of Cook County",
          "cluster_id": 4872436,
          "cite": [
            "993 F.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terrance Prude v. Anthony Meli",
          "cluster_id": 9418547,
          "cite": [
            "76 F.4th 648"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan Jones v. George Solomon",
          "cluster_id": 9457388,
          "cite": [
            "90 F.4th 198"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Jackson v. City of Cleveland",
          "cluster_id": 9389985,
          "cite": [
            "64 F.4th 736"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Sabo v. Megan Erickson",
          "cluster_id": 10325326,
          "cite": [
            "128 F.4th 836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "LaChance v. Town of Charlton",
          "cluster_id": 4860892,
          "cite": [
            "990 F.3d 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Taylor v. Riojas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4582848) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      },
      "lane2_top_cited": {
        "query": "cites:(4582848)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNCZzPTk0NzM1NTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284582848%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4582848)",
        "reviewed": 55,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 55,
        "triage_read": 0,
        "triage_snippet_classified": 55
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4582848)",
    "indexed_citing_opinions": 99,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4582848,
        "count": 99,
        "count_source": "search"
      }
    ],
    "citation_count": 420,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/taylor-v-riojas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5Mjk0NTYmcz0xMDAzNTcyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284582848%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4582848,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 758498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 4466815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9427304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9434318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4582848,
        "cited_id": 9795093,
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
    "date_created": "2026-07-05T21:18:03Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:21:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:18:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Taylor v. Riojas

```
                     Cite as: 592 U. S. ____ (2020)                     1

                              Per Curiam

SUPREME COURT OF THE UNITED STATES
TRENT MICHAEL TAYLOR v. ROBERT RIOJAS, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
               No. 19–1261. Decided November 2, 2020

   PER CURIAM.
   Petitioner Trent Taylor is an inmate in the custody of the
Texas Department of Criminal Justice. Taylor alleges that,
for six full days in September 2013, correctional officers
confined him in a pair of shockingly unsanitary cells.1 The
first cell was covered, nearly floor to ceiling, in “ ‘massive
amounts’ of feces”: all over the floor, the ceiling, the win-
dow, the walls, and even “ ‘packed inside the water faucet.’ ”
Taylor v. Stevens, 946 F. 3d 211, 218 (CA5 2019). Fearing
that his food and water would be contaminated, Taylor did
not eat or drink for nearly four days. Correctional officers
then moved Taylor to a second, frigidly cold cell, which was
equipped with only a clogged drain in the floor to dispose of
bodily wastes. Taylor held his bladder for over 24 hours,
but he eventually (and involuntarily) relieved himself,
causing the drain to overflow and raw sewage to spill across
the floor. Because the cell lacked a bunk, and because Tay-
lor was confined without clothing, he was left to sleep naked
in sewage.
   The Court of Appeals for the Fifth Circuit properly held
that such conditions of confinement violate the Eighth
Amendment’s prohibition on cruel and unusual punish-
ment. But, based on its assessment that “[t]he law wasn’t
clearly established” that “prisoners couldn’t be housed in
——————
  1 The Fifth Circuit accepted Taylor’s “verified pleadings [as] competent

evidence at summary judgment.” Taylor v. Stevens, 946 F. 3d 211, 221
(2019). As is appropriate at the summary-judgment stage, facts that are
subject to genuine dispute are viewed in the light most favorable to Tay-
lor’s claim.
2                     TAYLOR v. RIOJAS

                          Per Curiam

cells teeming with human waste” “for only six days,” the
court concluded that the prison officials responsible for Tay-
lor’s confinement did not have “ ‘fair warning’ that their spe-
cific acts were unconstitutional.” 946 F. 3d, at 222 (quoting
Hope v. Pelzer, 536 U. S. 730, 741 (2002)).
   The Fifth Circuit erred in granting the officers qualified
immunity on this basis. “Qualified immunity shields an of-
ficer from suit when she makes a decision that, even if con-
stitutionally deficient, reasonably misapprehends the law
governing the circumstances she confronted.” Brosseau v.
Haugen, 543 U. S. 194, 198 (2004) (per curiam). But no rea-
sonable correctional officer could have concluded that, un-
der the extreme circumstances of this case, it was constitu-
tionally permissible to house Taylor in such deplorably
unsanitary conditions for such an extended period of time.
See Hope, 536 U. S., at 741 (explaining that “ ‘a general con-
stitutional rule already identified in the decisional law may
apply with obvious clarity to the specific conduct in ques-
tion’ ” (quoting United States v. Lanier, 520 U. S. 259, 271
(1997))); 536 U. S., at 745 (holding that “[t]he obvious cru-
elty inherent” in putting inmates in certain wantonly “de-
grading and dangerous” situations provides officers “with
some notice that their alleged conduct violate[s]” the Eighth
Amendment). The Fifth Circuit identified no evidence that
the conditions of Taylor’s confinement were compelled by
necessity or exigency. Nor does the summary-judgment
record reveal any reason to suspect that the conditions of
Taylor’s confinement could not have been mitigated, either
in degree or duration. And although an officer-by-officer
analysis will be necessary on remand, the record suggests
that at least some officers involved in Taylor’s ordeal were
deliberately indifferent to the conditions of his cells. See,
e.g., 946 F. 3d, at 218 (one officer, upon placing Taylor in
the first feces-covered cell, remarked to another that Taylor
was “ ‘going to have a long weekend’ ”); ibid., and n. 9 (an-
other officer, upon placing Taylor in the second cell, told
                      Cite as: 592 U. S. ____ (2020)                     3

                               Per Curiam

Taylor he hoped Taylor would “ ‘f***ing freeze’ ”).
  Confronted with the particularly egregious facts of this
case, any reasonable officer should have realized that Tay-
lor’s conditions of confinement offended the Constitution.2
We therefore grant Taylor’s petition for a writ of certiorari,
vacate the judgment of the Court of Appeals for the Fifth
Circuit, and remand the case for further proceedings con-
sistent with this opinion.
                                            It is so ordered.

  JUSTICE BARRETT took no part in the consideration or
decision of this case.

  JUSTICE THOMAS dissents.




——————
   2 In holding otherwise, the Fifth Circuit noted “ambiguity in the

caselaw” regarding whether “a time period so short [as six days] violated
the Constitution.” 946 F. 3d, at 222. But the case that troubled the Fifth
Circuit is too dissimilar, in terms of both conditions and duration of con-
finement, to create any doubt about the obviousness of Taylor’s right.
See Davis v. Scott, 157 F. 3d 1003, 1004 (CA5 1998) (no Eighth Amend-
ment violation where inmate was detained for three days in dirty cell
and provided cleaning supplies).
                  Cite as: 592 U. S. ____ (2020)             1

                ALITO, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
TRENT MICHAEL TAYLOR v. ROBERT RIOJAS, ET AL.
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
             No. 19–1261. Decided November 2, 2020

   JUSTICE ALITO, concurring in the judgment.
   Because the Court has granted the petition for a writ of
certiorari, I will address the question that the Court has
chosen to decide. But I find it hard to understand why the
Court has seen fit to grant review and address that ques-
tion.
                               I
   To see why this petition is ill-suited for review, it is im-
portant to review the procedural posture of this case. Peti-
tioner, an inmate in a Texas prison, sued multiple prison
officers and asserted a variety of claims, including both the
Eighth Amendment claim that the Court addresses (placing
and keeping him in filthy cells) and a related Eighth
Amendment claim (refusing to take him to a toilet). The
District Court granted summary judgment for the defend-
ants on all but one of petitioner’s claims under Federal Rule
of Civil Procedure 54(b), which permitted petitioner to ap-
peal the dismissed claims. On appeal, the Fifth Circuit af-
firmed as to all the claims at issue except the toilet-access
claim. On the claim concerning the conditions of peti-
tioner’s cells, the court held that the facts alleged in peti-
tioner’s verified complaint were sufficient to demonstrate
an Eighth Amendment violation, but it found that the offic-
ers were entitled to qualified immunity based primarily on
a statement in Hutto v. Finney, 437 U. S. 678 (1978), and
the Fifth Circuit’s decision in Davis v. Scott, 157 F. 3d 1003
(1998).
2                     TAYLOR v. RIOJAS

                ALITO, J., concurring in judgment

   The Court now reverses the affirmance of summary judg-
ment on the cell-conditions claim. Viewing the evidence in
the summary judgment record in the light most favorable
to petitioner, the Court holds that a reasonable corrections
officer would have known that it was unconstitutional to
confine petitioner under the conditions alleged. That ques-
tion, which turns entirely on an interpretation of the record
in one particular case, is a quintessential example of the
kind that we almost never review. As stated in our Rules,
“[a] petition for a writ of certiorari is rarely granted when
the asserted error consists of . . . the misapplication of a
properly stated rule of law,” this Court’s Rule 10. That is
precisely the situation here. The Court does not dispute
that the Fifth Circuit applied all the correct legal stand-
ards, but the Court simply disagrees with the Fifth Circuit’s
application of those tests to the facts in a particular record.
Every year, the courts of appeals decide hundreds if not
thousands of cases in which it is debatable whether the ev-
idence in a summary judgment record is just enough or not
quite enough to carry the case to trial. If we began to review
these decisions we would be swamped, and as a rule we do
not do so.
   Instead, we have well-known criteria for granting review,
and they are not met here. The question that the Court
decides is not one that has divided the lower courts, see this
Court’s Rule 10, and today’s decision adds virtually nothing
to the law going forward. The Court of Appeals held that
the conditions alleged by petitioner, if proved, would violate
the Eighth Amendment, and this put correctional officers
in the Fifth Circuit on notice that such conditions are intol-
erable. Thus, even without our intervention, qualified im-
munity would not be available in any similar future case.
   We have sometimes granted review and summarily re-
versed in cases where it appeared that the lower court had
conspicuously disregarded governing Supreme Court prec-
edent, but that is not the situation here. On the contrary,
                  Cite as: 592 U. S. ____ (2020)            3

                ALITO, J., concurring in judgment

as I explain below, it appears that the Court of Appeals
erred largely because it read too much into one of our
decisions.
   It is not even clear that today’s decision is necessary to
protect petitioner’s interests. We are generally hesitant to
grant review of non-final decisions, and there are grounds
for such wariness here. If we had denied review at this
time, petitioner may not have lost the opportunity to con-
test the grant of summary judgment on the issue of re-
spondents’ entitlement to qualified immunity on his cell-
conditions claim. His case would have been remanded for
trial on the claims that remained after the Fifth Circuit’s
decision (one of which sought relief that appears to overlap
with the relief sought on the cell-conditions claim), and if
he was dissatisfied with the final judgment, he may have
been able to seek review by this Court of the cell-conditions
qualified immunity issue at that time. Major League Base-
ball Players Assn. v. Garvey, 532 U. S. 504, 508, n. 1 (2001)
( per curiam). And of course, there is always the possibility
that he would have been satisfied with whatever relief he
obtained on the claims that went to trial.
   Today’s decision does not even conclusively resolve the is-
sue of qualified immunity on the cell-conditions claim be-
cause respondents are free to renew that defense at trial,
and if the facts petitioner alleges are not ultimately estab-
lished, the defense could succeed. Indeed, if petitioner can-
not prove the facts he alleges, he may not be able to show
that his constitutional rights were violated.
   In light of all this, it is not apparent why the Court has
chosen to grant review in this case.
                            II
  While I would not grant review on the question the Court
addresses, I agree that summary judgment should not have
been awarded on the issue of qualified immunity. We must
4                      TAYLOR v. RIOJAS

                 ALITO, J., concurring in judgment

view the summary judgment record in the light most favor-
able to petitioner, and when petitioner’s verified complaint
is read in this way, a reasonable fact-finder could infer not
just that the conditions in the cells in question were horrific
but that respondents chose to place and keep him in those
particular cells, made no effort to have the cells cleaned,
and did not explore the possibility of assignment to cells
with better conditions. A reasonable corrections officer
would have known that this course of conduct was uncon-
stitutional, and the cases on which respondents rely do not
show otherwise.
   Although this Court stated in Hutto that holding a pris-
oner in a “filthy” cell for “a few days” “might be tolerable,”
437 U. S., at 686–687, that equivocal and unspecific dictum
does not justify what petitioner alleges. There are degrees
of filth, ranging from conditions that are simply unpleasant
to conditions that pose a grave health risk, and the concept
of “a few days” is also imprecise. In addition, the statement
does not address potentially important factors, such as the
necessity of placing and keeping a prisoner in a particular
cell and the possibility of cleaning the cell before he is
housed there or during the course of that placement. A rea-
sonable officer could not think that this statement or the
Court of Appeals’ decision in Davis meant that it is consti-
tutional to place a prisoner in the filthiest cells imaginable
for up to six days despite the availability of other preferable
cells or despite the ability to arrange for cleaning of the cells
in question.
   For these reasons, I concur in the judgment.

```

---

## GROUP: content/cases/The GEO Group, Inc. v. Menocal.md  (`case`, 5 assertions)

### content_page

```
---
title: "The GEO Group, Inc. v. Menocal"
type: case
citation: "No. 24-758, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 24-758
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
  opinion_url: "https://www.courtlistener.com/opinion/10800194/geo-group-inc-v-menocal/"
  cluster_id: 10800194
  opinion_id: null
  identity_checked: false
lake:
  record_id: "The GEO Group, Inc. v. Menocal"
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - federal-contractor
  - yearsley
  - collateral-order
  - appellate-jurisdiction
  - derivative-immunity
  - supreme-court
holding: "Because the Yearsley doctrine gives a federal contractor a potential merits defense rather than an immunity from suit, a district court order denying Yearsley protection is not immediately appealable under the collateral-order doctrine; it neither resolves an issue separate from the merits nor is effectively unreviewable after final judgment."
aliases:
  - "The GEO Group, Inc. v. Menocal"
  - "GEO Group, Inc. v. Menocal"
  - GEO Group v. Menocal
---

# The GEO Group, Inc. v. Menocal

*No. 24-758, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10800194 → majority opinion 11266870 (No. 24-758, decided Feb. 25, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
GEO Group operates a private immigration-detention facility in Aurora, Colorado, under contract with U.S. Immigration and Customs Enforcement (ICE). Former detainee Alejandro Menocal brought a class action alleging GEO's detainee work policies violated a federal forced-labor bar and Colorado's unjust-enrichment law. GEO argued the suit was barred by *Yearsley v. W.A. Ross Construction Co.*, which shields a federal contractor from liability for conduct the Government lawfully "authorized and directed." The district court held the contract did not direct the challenged policies and that a trial was necessary; the Tenth Circuit dismissed GEO's immediate appeal for lack of jurisdiction.

## Issue
Whether a district court order denying a federal contractor's *Yearsley* defense is immediately appealable under the collateral-order doctrine.

## Rule
The courts of appeals may hear appeals only from "final decisions," 28 U.S.C. § 1291, subject to a narrow collateral-order exception for rulings that (1) conclusively determine the disputed question, (2) resolve an important issue completely separate from the merits, and (3) are effectively unreviewable on appeal from a final judgment. The Court held: "Because *Yearsley* provides federal contractors a potential merits defense rather than an immunity from suit, a pretrial order denying *Yearsley* protection is not immediately appealable." — slip op. at 1. ^pin-slip1

## Application
Unlike qualified or sovereign immunity — which confer a right *not to stand trial* and so justify immediate review — *Yearsley* supplies only a defense to liability on the merits. An order rejecting it therefore does not resolve a question "completely separate from the merits," and any error can be corrected on appeal from final judgment; the ruling flunks the collateral-order test. The interest in avoiding piecemeal appeals controls.

## Conclusion
**Affirmed.** Justice Kagan wrote for a unanimous Court (9–0); the Tenth Circuit's dismissal for lack of jurisdiction was upheld.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *GEO Group* sharpens the line between an "immunity from suit" (immediately appealable, like [[Qualified Immunity|qualified immunity]] in § 1983 litigation) and a mere "merits defense" (not appealable until final judgment), classifying *Yearsley* federal-contractor protection as the latter.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Geo Group, Inc. v. Menocal*, No. 24-758, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10800194/geo-group-inc-v-menocal/) — pinpoint: slip op. at 1 (Yearsley is a merits defense, not an appealable immunity). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "477280eb1de56771", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 24-758, slip op. (U.S. 2026)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "The GEO Group, Inc. v. Menocal", "year": "2026"}}
{"assertion_id": "703788d35447eda6", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "The GEO Group, Inc. v. Menocal"}}
{"assertion_id": "780ebd162e86dc79", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because the Yearsley doctrine gives a federal contractor a potential merits defense rather than an immunity from suit, a district court order denying Yearsley protection is not immediately appealable under the collateral-order doctrine; it neither resolves an issue separate from the merits nor is effectively unreviewable after final judgment.", "title": "The GEO Group, Inc. v. Menocal"}}
{"assertion_id": "7e2d6388775d82d4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "The GEO Group, Inc. v. Menocal", "varies_by_point": "false"}}
{"assertion_id": "ab59eb743d32e5f0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "The GEO Group, Inc. v. Menocal"}}
```

### lake record — The GEO Group, Inc. v. Menocal

```json
{
  "schema_version": "s2.v1",
  "record_id": "The GEO Group, Inc. v. Menocal",
  "status": "under_review",
  "identity": {
    "case_name": "Geo Group, Inc. v. Menocal",
    "case_name_short": "Menocal",
    "case_name_full": "",
    "input_case_name": "The GEO Group, Inc. v. Menocal",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "24-758",
    "cluster_id": 10800194,
    "lead_opinion_id": 11266870,
    "sibling_ids": [],
    "absolute_url": "/opinion/10800194/geo-group-inc-v-menocal/",
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
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 24-758, decided 2026-02-25 (607 U.S. ___; Kagan, 9-0). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/24-758",
          "cite": "No. 24-758, decided 2026-02-25"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/607/24-758/",
          "cite": "607 U.S. ___ (2026) placeholder"
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
    "date_created": "2026-07-06T12:13:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "the-geo-group-inc-v-menocal--10800194",
      "to_record_id": "The GEO Group, Inc. v. Menocal",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — The GEO Group, Inc. v. Menocal

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

             GEO GROUP, INC. v. MENOCAL ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

 No. 24–758.      Argued November 10, 2025—Decided February 25, 2026


Petitioner GEO Group operates a private detention facility in Aurora,
  Colorado, under a contract with U. S. Immigration and Customs En-
  forcement (ICE). Respondent Alejandro Menocal, a former detainee at
  the Aurora facility, initiated this class action, alleging GEO’s work pol-
  icies for detainees violate a federal bar on forced labor and Colorado’s
  prohibition on unjust enrichment. GEO responded that the suit must
  be dismissed under Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18,
  which held that a federal contractor cannot be held liable for conduct
  that the Government has lawfully “authorized and directed” the con-
  tractor to perform. Id., at 20–21. GEO argued that ICE had author-
  ized and directed it to carry out the challenged labor policies. But the
  District Court did not read GEO’s contract with the Government to
  instruct GEO to adopt those policies. The District Court thus con-
  cluded that the Yearsley doctrine did not relieve GEO of legal respon-
  sibility and a trial would be necessary. GEO immediately filed an ap-
  peal, which the Court of Appeals for the Tenth Circuit dismissed for
  lack of jurisdiction, holding that an order denying Yearsley protection
  does not qualify for interlocutory review under Cohen v. Beneficial In-
  dustrial Loan Corp., 337 U. S. 541.
Held: Because Yearsley provides federal contractors a potential merits
 defense rather than an immunity from suit, a pretrial order denying
 Yearsley protection is not immediately appealable. Pp. 3–12.
    (a) The courts of appeals have jurisdiction over appeals from “final
 decisions of the district courts.” 28 U. S. C. §1291. A decision gener-
 ally is “final” only when it “resolves the entire case”—when it “ends the
 litigation” on the merits or otherwise. Ritzen Group, Inc. v. Jackson
2                     GEO GROUP, INC. v. MENOCAL

                                    Syllabus

    Masonry, LLC, 589 U. S. 35, 37–38. That final-judgment rule, by pre-
    venting piecemeal appeals, “promotes the efficient administration of
    justice” and “preserves the proper balance between trial and appellate
    courts.” Microsoft Corp. v. Baker, 582 U. S. 23, 36–37.
       Under the collateral-order doctrine, however, a “small class” of deci-
    sions are treated as “final”—and thus immediately appealable—even
    though they do not end a case. Cohen, 337 U. S., at 546. To get imme-
    diate review, a prejudgment order must satisfy the three conditions
    this Court has “distilled” from Cohen. Will v. Hallock, 546 U. S. 345,
    349. The order must “(1) conclusively determine the disputed question,
    (2) resolve an important issue completely separate from the merits of
    the action, and (3) be effectively unreviewable on appeal from a final
    judgment.” Van Cauwenberghe v. Biard, 486 U. S. 517, 522.
       Whether the denial of a pretrial request to dismiss a case like the
    one here can satisfy Cohen’s third condition will generally turn on
    whether the defendant has asserted a defense to liability or instead an
    immunity from suit. A party asserting a merits defense advances some
    reason why his conduct was not unlawful and he should not be found
    liable. But a party asserting an immunity need not challenge the mer-
    its of the charge against him: his claim of immunity does not turn on
    his conduct’s legality. That difference entails another. Because it en-
    sures a defendant need not “answer for his conduct” in court at all, an
    immunity is in its “essence” an “entitlement not to stand trial.” Mitch-
    ell v. Forsyth, 472 U. S. 511, 525–526. A liability defense, by contrast,
    does not allow the defendant to escape legal proceedings, because it is
    through them that the asserted defense is addressed and liability fi-
    nally determined. And that divergence matters for Cohen’s third con-
    dition, which requires that the order involve a right that “would be
    irretrievably lost absent an immediate appeal.” Van Cauwenberghe,
    486 U. S., at 524. The right not to stand trial is irretrievably lost once
    trial occurs, but the right to a finding of non-liability can be effectively
    vindicated after trial, through reversal of an adverse final judgment.
    So, if a defendant asserts a liability defense, Cohen is likely to block an
    immediate appeal; if he asserts an immunity, Cohen will likely allow
    it. Pp. 3–7.
       (b) Does Yearsley offer federal contractors a merits defense or in-
    stead an immunity? Menocal says a defense, because Yearsley gives
    contractors only a way to show that their conduct complied with the
    law. GEO says an immunity—more specifically, “derivative sovereign
    immunity”—where the Government’s own immunity extends to con-
    tractors who meet specified conditions. Brief for GEO 15.
       Yearsley provides a potential defense to liability, not an immunity
    from suit. In Yearsley, the Court held that a contractor that had
    flooded the Yearsleys’ property while performing work “authorized and
                       Cite as: 607 U. S. ___ (2026)                       3

                                 Syllabus

  directed by the Government” was not liable to the landowner. 309
  U.S., at 20. The Court explained that a contractor acting as an agent
  of the Government could be held liable for injurious conduct in only
  two circumstances: when “he exceeded his authority” or when that au-
  thority “was not validly conferred.” Id., at 21. The Court found neither
  circumstance obtained in Yearsley, because the contractor received a
  lawful authorization and stayed within the bounds of the authority
  given. That reasoning describes a defense, not an immunity: Years-
  ley’s protection runs out when the contractor may have violated the
  law—when the contractor either acted under an illegal authorization
  or exceeded the scope of a legal one. Yearsley thus ensures that it will
  never shield unlawful conduct, in the way that all immunities do.
     GEO’s contrary view—that it enjoys “derivative sovereign immun-
  ity”—would put Yearsley in conflict with the general rule that sover-
  eign immunity is not transferrable to government agents. The Court
  has repeatedly held that the Government’s immunity from suit “does
  not extend to those that act[ ] in its name,” Sloan Shipyards Corp. v.
  United States Shipping Bd. Emergency Fleet Corporation, 258 U. S.
  549, 568, or do its work, Keifer & Keifer v. Reconstruction Finance Cor-
  poration, 306 U. S. 381, 388, including by “reason of a contract” with
  the Government, Brady v. Roosevelt S. S. Co., 317 U. S. 575, 583; see
  also Hopkins v. Clemson, 221 U. S. 636, 642–643. The whole thrust of
  those decisions is to deny that government agents can assert—whether
  always or sometimes—a “derived” form of sovereign immunity. In-
  stead, sovereign immunity belongs alone to the Government. Pp. 7–
  11.
     (c) Once Yearsley is properly understood as a merits defense, the
  question before the Court almost answers itself. Like the denial of
  other defenses, a district court’s denial of Yearsley protection is not im-
  mediately appealable under §1291. Such a ruling is not, as Cohen’s
  third condition demands, “effectively unreviewable on appeal from a
  final judgment.” Van Cauwenberghe, 486 U. S., at 522. The right that
  a merits defense affords is to a finding of non-liability. And that
  right—unlike the right not to stand trial—is fully vindicable on appeal
  from a final judgment. Accordingly, the finality rule of §1291 precludes
  interlocutory review of a Yearsley denial. Pp. 11–12.
Affirmed and remanded.

KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and SOTOMAYOR, GORSUCH, KAVANAUGH, BARRETT, and JACKSON, JJ.,
joined, and in which THOMAS, J., joined as to Parts I and III. THOMAS, J.,
filed an opinion concurring in part and concurring in the judgment.
ALITO, J., filed an opinion concurring in the judgment.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–758
                                   _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                              [February 25, 2026]

  JUSTICE KAGAN delivered the opinion of the Court.
  In Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18, 20
(1940), this Court held that a federal contractor cannot be
held liable for conduct that the Government has lawfully
“authorized and directed” the contractor to perform. Ra-
ther, liability may attach only if the authorization was un-
lawful or if the contractor acted outside its scope. See id.,
at 20–21.
  The question here is whether a contractor may take an
immediate appeal of a district court’s pretrial order denying
Yearsley protection. The answer is no. Because Yearsley
provides a defense to liability, not an immunity from suit,
an order denying its protection can be effectively reviewed
after a final judgment. So appellate review of such an or-
der, as of most pretrial rulings, must await completion of
the district court’s proceedings.
                            I
   Petitioner GEO Group operates a private detention facil-
ity in Aurora, Colorado, under a contract with U. S. Immi-
gration and Customs Enforcement (ICE). The facility holds
individuals whose immigration proceedings are pending.
2               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

Respondent Alejandro Menocal was detained there in 2014.
Soon afterward, he initiated this class action on behalf of
the Aurora facility’s detainees.
   The suit challenges two policies GEO used to put the de-
tainees to work, thereby reducing its own labor costs. First,
the so-called Sanitation Policy required detainees to clean,
without any pay, all the facility’s common areas. A de-
tainee’s failure to perform his assigned tasks led to escalat-
ing sanctions, up to 72 hours in solitary confinement. Sec-
ond, the so-called Voluntary Work Program offered $1 per
day to detainees for other kinds of needed work, such as
preparing food and doing laundry. Menocal’s complaint al-
leged that the former policy violated a federal bar on forced
labor and that the latter breached Colorado’s prohibition on
unjust enrichment.
   Following discovery, the District Court addressed GEO’s
contention that Yearsley required the suit’s dismissal. That
was so, the argument ran, because ICE had by contract “au-
thorized and directed” GEO to carry out the two challenged
policies. Defendant’s Cross-Motion for Summary Judgt. in
No. 14–2887 (D Colo., June 25, 2020), ECF Doc. 284, p. 17.
But the District Court did not read the government contract
that way. Nothing in its terms, the court found, instructed
GEO to adopt the work rules at issue. Rather, in “inde-
pendently develop[ing] and implement[ing]” those rules,
GEO “far exceeded its contractual obligations.”           635
F. Supp. 3d 1151, 1173 (Colo. 2022). So the Yearsley doc-
trine, the District Court concluded, did not relieve GEO of
legal responsibility. Instead, a trial would be necessary to
address whether GEO’s policies violated the referenced
bans on forced labor or unjust enrichment.
   GEO immediately filed an appeal, but the Court of Ap-
peals for the Tenth Circuit dismissed it for lack of jurisdic-
tion. See 2024 WL 4544184 (Oct. 22, 2024). Appellate ju-
risdiction, the court explained, seldom extends to an order
that does not terminate the litigation at issue. Such an
                  Cite as: 607 U. S. ____ (2026)             3

                      Opinion of the Court

order qualifies for interlocutory review only if it satisfies
three conditions deriving from this Court’s decision in Co-
hen v. Beneficial Industrial Loan Corp., 337 U. S. 541
(1949). And an order denying Yearsley protection, the
Tenth Circuit held, does not do so. The court saw no need
to address the first or third Cohen conditions because it con-
cluded that a Yearsley denial flunked the second: Such a
ruling is not (as Cohen demands) “completely separate from
the merits” of the suit. 2024 WL 4544184, *7. That is be-
cause, the court reasoned, an inquiry into what the Govern-
ment instructed the contractor to do is relevant to both
Yearsley’s application and the “lawfulness of the contrac-
tor’s challenged actions.” Id., at *8.
  We granted certiorari, 605 U. S. 968 (2025), to resolve
whether a pretrial order denying Yearsley protection to a
government contractor is immediately appealable. Like the
Tenth Circuit, we hold that it is not. But unlike the Tenth
Circuit, we focus on the third Cohen condition, which re-
quires an order to be effectively unreviewable on appeal
from a final judgment.
                               II
   “Finality as a condition of review is an historic character-
istic of federal appellate procedure.” Cobbledick v. United
States, 309 U. S. 323, 324 (1940). Originating in the First
Judiciary Act of 1789, the finality requirement is now codi-
fied in 28 U. S. C. §1291. The courts of appeals, that section
provides, have jurisdiction over appeals from “final deci-
sions of the district courts.” And a decision generally is “fi-
nal” under §1291 only when it “resolves the entire case”—
when it “ends the litigation” (on the merits or otherwise)
and “leaves nothing for the court to do but execute the judg-
ment.” Ritzen Group, Inc. v. Jackson Masonry, LLC, 589
U. S. 35, 37–38 (2020). That final-judgment rule, by pre-
venting piecemeal appeals, “promotes the efficient admin-
istration of justice” and “preserves the proper balance
4               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

between trial and appellate courts.” Microsoft Corp. v.
Baker, 582 U. S. 23, 36–37 (2017).
   For a “small class” of decisions, however, the finality rule
gives ground and allows interlocutory appeals. Cohen, 337
U. S., at 546. Section 1291, we have often explained, re-
quires a “practical rather than a technical construction,”
and thus may treat as “final” certain decisions that do not
end a case. Mohawk Industries, Inc. v. Carpenter, 558 U. S.
100, 106 (2009) (quoting Cohen, 337 U. S., at 546). We iden-
tify those decisions by category, not case-specific circum-
stances. See Mohawk, 558 U. S., at 107. And we erect a
high bar. A non-terminal order may be appealed, Cohen
held, only if it “finally determine[s] claims of right separa-
ble from, and collateral to, rights asserted in the action, too
important to be denied review and too independent of the
cause itself to require that appellate consideration be de-
ferred.” 337 U. S., at 546. That so-called collateral-order
doctrine, we have since underscored, is “narrow,” “strin-
gent,” and of “modest scope.” Digital Equipment Corp. v.
Desktop Direct, Inc., 511 U. S. 863, 868 (1994); Will v. Hal-
lock, 546 U. S. 345, 350 (2006).
   To keep it that way, this Court has “distilled” the Cohen
ruling into three non-negotiable conditions. Will, 546 U. S.,
at 349. A pre-judgment order, to get immediate review,
must “(1) conclusively determine the disputed question, (2)
resolve an important issue completely separate from the
merits of the action, and (3) be effectively unreviewable on
appeal from a final judgment.” Van Cauwenberghe v.
Biard, 486 U. S. 517, 522 (1988). Failure on any component
of that three-part test is fatal.
   When, as here, an order denies a pretrial request to dis-
miss, appealability under Cohen will generally turn on
whether the defendant has asserted a defense to liability or
instead an immunity from suit. See Mitchell v. Forsyth, 472
U. S. 511, 526–527 (1985). If a defense, Cohen is likely to
block an immediate appeal; if an immunity, Cohen will
                      Cite as: 607 U. S. ____ (2026)                     5

                          Opinion of the Court

likely allow it. To show why, we describe below the differ-
ence between a merits defense and an immunity; what that
difference entails for the right to avoid trial; and how that
right matters in applying the third Cohen condition. Once
that is done, it becomes clear why, as later described, the
parties here mainly contest whether Yearsley offers an im-
munity or just a merits defense. See infra, at 7–8.1
   To start, a party asserting a merits defense in a lawsuit
makes a fundamentally different kind of argument than a
party asserting an immunity. The former advances some
reason why his conduct was not unlawful—or said other-
wise, why under the law he did nothing wrong. And so, that
defendant says, he should not be found liable: Because he
obeyed the law, he should not, for example, have to pay
damages. By contrast, a party asserting an immunity
“makes no challenge” to “the merits of the charge against
him.” Abney v. United States, 431 U. S. 651, 659 (1977).
That defendant need never say he followed the law, because
his claim of immunity does not turn on his conduct’s legal-
ity. “[A]n immunity frees one who enjoys it from a lawsuit
whether or not he acted wrongly.” Richardson v. McKnight,
521 U. S. 399, 403 (1997). A classic example is sovereign
immunity: It shields the Government from suit (absent a
waiver) regardless whether the Government violated the
law. See, e.g., FDIC v. Meyer, 510 U. S. 471, 475 (1994).2
——————
  1 Note that one category of cases exists outside this dichotomy: a non-

merits-based defense that also is not an immunity. On occasion, this
Court has decided that a defense, although barring suit irrespective of
the merits, still fails to qualify as an immunity because it does not serve
sufficiently “weighty public objective[s].” Will v. Hallock, 546 U. S. 345,
353 (2006) (so holding with respect to the Federal Tort Claims Act’s judg-
ment bar). That “public interest” wrinkle, however, never arises if the
defense is on the merits—which, as we will explain, is the case here.
  2 Qualified immunity is, in the respect relevant here, the same. That

doctrine shields a defendant even when the claim against him “in fact
has merit”—or otherwise said, even when he violated the law—so long
as the law at that time was not “clearly established.” Camreta v. Greene,
6                 GEO GROUP, INC. v. MENOCAL

                         Opinion of the Court

   That difference between a merits defense and an immun-
ity entails another: The latter, but not the former, is in its
“essence” an “entitlement not to stand trial.” Mitchell, 472
U. S., at 525. Because an immunity applies irrespective of
the merits, the protection it offers is not a simple finding of
non-liability. Rather, the immunity ensures that the de-
fendant need not “answer for his conduct” in court at all—
that he avoids, in addition to liability, all the usual “bur-
dens of litigation,” including a trial. Id., at 525–526. And
so we typically describe the protection in just that way: as
an immunity “from suit.” Id., at 526 (emphasis in original);
see, e.g., Thacker v. TVA, 587 U. S. 218, 221 (2019); Jam v.
International Finance Corp., 586 U. S. 199, 202 (2019). A
“mere defense” to liability, as we have noted, offers some-
thing different, and of lesser value. Mitchell, 472 U. S., at
526. Because it establishes that the defendant acted law-
fully, a valid defense leads to a judgment of non-liability.
But it does not allow the defendant to escape the varied ri-
gors and costs of legal proceedings. Indeed, it is in and
through those proceedings that the asserted defense is ad-
dressed and liability finally determined.
   And that divergence—in whether the defendant pos-
sesses a right not to stand trial—matters for the third Co-
hen condition. Again, that condition states that a non-ter-
minal order may be appealed when issued only if it is
“effectively unreviewable on appeal from a final judgment.”
Van Cauwenberghe, 486 U. S., at 522; see supra, at 4. For
that to be true, we have explained, the order must involve
a right that “would be irretrievably lost absent an immedi-
ate appeal.” Van Cauwenberghe, 486 U. S., at 524. The
right to avoid trial fits that description. It is irretrievably
lost once trial occurs, even supposing the defendant were to

——————
563 U. S. 692, 705 (2011). “Like other forms of immunity,” then, quali-
fied immunity offers protection “even when [the defendant] acts unlaw-
fully.” Brief for United States as Amicus Curiae 23.
                      Cite as: 607 U. S. ____ (2026)                        7

                           Opinion of the Court

prevail on the merits. And so, in the ordinary case, the de-
nial of an immunity is immediately appealable. See ibid.;
Abney, 431 U. S., at 659–660. But the right to a finding of
non-liability stands on a different footing: It can be effec-
tively vindicated after a trial has occurred, through the re-
versal of an adverse final judgment. And so the denial of a
merits defense is generally appealable only once trial-court
proceedings have ended. See Van Cauwenberghe, 486 U. S.,
at 524; Mitchell, 472 U. S., at 526.
   In short, then, distinguishing between a merits defense
and an immunity from suit, in the way described above, of-
fers a ready way of determining whether the denial of a re-
quest to dismiss a case can satisfy Cohen’s third condition
for interlocutory review.3
                           III
 For just that reason, the parties here mainly dispute
whether our Yearsley decision offers federal contractors a
——————
   3 By the same token, that distinction is likely to determine whether the

other two Cohen conditions are met, though we need not here address
the reasons in any detail. See Puerto Rico Aqueduct and Sewer Authority
v. Metcalf & Eddy, Inc., 506 U. S. 139, 144 (1993) (“Once it is established
that” a State is “immune from suit in federal court, it follows that the
elements of the Cohen collateral order doctrine are satisfied”). Recall
that Cohen’s second condition, on which the Court of Appeals relied, de-
mands that the order “resolve an important issue completely separate
from the merits of the action.” Van Cauwenberghe v. Biard, 486 U. S.
517, 522 (1988); see supra, at 4. A decision on a defense, addressing the
legality of the defendant’s conduct, goes directly to the suit’s merits—
whereas a decision on an immunity, applying regardless of that conduct’s
legality, does not. Similarly for the first condition, which is that the or-
der “conclusively determine the disputed question.” Van Cauwenberghe,
486 U. S., at 522. When a defense turns on contested facts, as is often
true, a pretrial order denying it functions only to defer its resolution until
trial. By contrast, we have held, a pretrial denial of an immunity always
acts as a “fully consummated decision” because nothing can then happen
to avert “the trial the defendant maintains is barred.” Mitchell v. For-
syth, 472 U. S. 511, 527 (1985) (quoting Abney v. United States, 431 U. S.
651, 659 (1977)).
8               GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

merits defense or instead an immunity. Menocal (sup-
ported by the United States as amicus curiae) says a de-
fense, because Yearsley gives contractors only a way to show
that their conduct complied with the law. GEO says an im-
munity—more specifically, “derivative sovereign immun-
ity.” Brief for GEO 15. Under Yearsley, GEO contends, the
Government’s own immunity extends to contractors who
meet specified conditions, thereby giving them the “right
not to stand trial.” Brief for GEO 15. So which is it—a de-
fense or an immunity?
   Yearsley involved a suit by landowners against a federal
contractor for flooding their property. The Government had
hired the contractor to redirect the Missouri River in order
to improve its navigation. The construction company, as
specified in the contract, built dikes in a part of the river
near where the Yearsleys owned a farm. The result, as ex-
pected, was to wash away almost 100 acres of their land.
The Yearsleys did not dispute that the contractor’s work
was “all authorized and directed by the Government.” 309
U. S., at 20. Nonetheless, they sued the contractor for
money damages.
   This Court held that there was “no liability on the part of
the contractor.” Id., at 21. Drawing from multiple prece-
dents involving agency law, the Court explained that a con-
tractor acting as an agent of the Government could be held
liable for injurious conduct in only two circumstances: when
“he exceeded his authority” or when that authority “was not
validly conferred.” Ibid. Here, neither circumstance ob-
tained. As to the second, the Court explained that the Gov-
ernment had “validly” authorized the company to flood the
Yearsleys’ land, because the Government itself possessed
that legal right and had properly delegated it by contract.
Id., at 21–22. And as to the first, the Court concluded that
all the company’s work had stayed within the bounds of the
authority given: The Government had provided instruc-
tions, and the contractor had merely “execut[ed] its will.”
                 Cite as: 607 U. S. ____ (2026)            9

                     Opinion of the Court

Id., at 20–21. Given both those facts—the Government’s
lawful authorization and the contractor’s compliance with
it—the Court could see “no ground for holding [the contrac-
tor] liable.” Id., at 22.
   That reasoning describes a defense, not an immunity.
Yearsley provides protection to a contractor when it has re-
ceived a lawful authorization and acted according to its
terms—meaning, when the contractor has acted within le-
gal bounds. So in invoking Yearsley, the contractor is mak-
ing the argument of a merits defense—that it is not liable
because it has complied with the law. See supra, at 5. Con-
versely, Yearsley’s protection runs out when the contractor
may have violated the law—when the contractor either
acted under an illegal authorization or exceeded the scope
of a legal one. By drawing the line there, Yearsley ensures
that it will never shield unlawful conduct, in the way that
all immunities do. See supra, at 5. In short, because Years-
ley protects a contractor only when—and only because—it
has acted lawfully, Yearsley operates as a defense to liabil-
ity on the merits. And that is consistent with all Yearsley’s
language. The decision never refers to an “immunity,” or
otherwise suggests that the defendant receives a pass from
legal proceedings; it asks only whether the contractor may
be found “liable.” 309 U. S., at 21–22.
   Still more, GEO’s contrary view would put Yearsley in
conflict with the general rule that sovereign immunity is
not transferrable to agents, including contractors, of a gov-
ernment. As Justice Holmes once explained, the Federal
Government’s immunity from a suit (absent a statute
providing otherwise) “does not extend to those that act[ ] in
its name.” Sloan Shipyards Corp. v. United States Ship-
ping Bd. Emergency Fleet Corporation, 258 U. S. 549, 568
(1922). The Court repeated that precept in the Term just
before Yearsley: “[T]he government does not become the
conduit of its immunity in suits against its agents” just be-
cause “they do [the government’s] work.” Keifer & Keifer v.
10              GEO GROUP, INC. v. MENOCAL

                      Opinion of the Court

Reconstruction Finance Corporation, 306 U. S. 381, 388
(1939). Rather, the “exceptional freedom from legal respon-
sibility” that sovereign immunity offers is “confined” to the
sovereign entity itself. Ibid. Or again, a few Terms after
Yearsley: A private contractor cannot obtain “[i]mmunity
from suit” by “reason of a contract” it made with the Gov-
ernment. Brady v. Roosevelt S. S. Co., 317 U. S. 575, 583
(1943). GEO tries to bypass those holdings by arguing that
they preclude a contractor from asserting only “uncondi-
tional” sovereign immunity, not the (supposed) “derivative
sovereign immunity” Yearsley offers, which is conditioned
on compliance with the Government’s lawful directives. Re-
ply Brief 6–7. But the proposed distinction is strained. The
whole thrust of the decisions is to deny that government
agents can assert—whether always or sometimes—a “de-
rived” form of sovereign immunity. Rather, the Court in-
sisted, sovereign immunity belongs alone to the Govern-
ment.
   And another, pre-Yearsley decision proves the point, by
relegating a state agent that had asserted sovereign im-
munity to a merits defense, whose contours anticipated
what Yearsley would offer. See Hopkins v. Clemson, 221
U. S. 636 (1911). Oddly enough, the suit challenged the
same kind of conduct involved in Yearsley: The government
agent had flooded a person’s land. The State itself, the
Court noted, would have had “immunity from [a] suit”
based on such conduct. 221 U. S., at 642. But an agent
working on the State’s behalf could not “avail itself ” of that
special “exemption” from “judicial process.” Id., at 642, 645.
“[I]mmunity from suit,” the Court explained, “is a high at-
tribute of sovereignty—a prerogative of the State itself ”—
which cannot be invoked by the State’s agents. Id., at 642–
643. Yet all was not lost: The agent got something. Alt-
hough the agent was “not exempt from suit,” it could “suc-
cessfully defend” against the charges by showing the “law-
ful authority under which [it] acted.” Id., at 643. Those
                      Cite as: 607 U. S. ____ (2026)                    11

                          Opinion of the Court

terms evoke the ones Yearsley used later. See 309 U. S., at
22 (precluding liability for a contractor “acting under” “val-
idly conferred” authority); supra, at 8. And they function
not, as GEO posits, to condition the transfer of sovereign
immunity, but to describe something different—as the
Court made explicit, a merits “defen[se].” Hopkins, 221
U. S., at 643.4
   Once Yearsley is understood in that way—as a merits de-
fense—the question before us almost answers itself: No, a
district court’s denial of Yearsley protection is not immedi-
ately appealable under §1291. Like the denial of other de-
fenses, such a ruling is not, as Cohen’s third condition de-
mands, “effectively unreviewable on appeal from a final
judgment.” Van Cauwenberghe, 486 U. S., at 522. The
right that a merits defense affords is to a finding of non-
liability. And that right—unlike the right not to stand
trial—is fully vindicable on appeal from a final judgment.
See Swint v. Chambers County Comm’n, 514 U. S. 35, 43
(1995); supra, at 6. All an appellate court need do at that

——————
  4 GEO counters that two of our decisions refer to Yearsley as offering

“immunity,” see Brief for GEO 17, 23, but that argument makes far too
much of one piece of loose language. The first cited case, Brady v. Roo-
sevelt S. S. Co., 317 U. S. 575 (1943), mainly cuts against GEO. As noted
above, the Court there rejected the view that a government contractor
obtains “[i]mmunity from suit” by virtue of its contractual relation. Id.,
at 583; see supra, at 10. The Court then turned to Yearsley, finding it
not to apply because the suit alleged negligent conduct, outside what the
Government had authorized. In that half-paragraph, the decision once
refers to Yearsley as providing a “certain immunity.” 317 U. S., at 583.
But it apparently used that term in a colloquial sense, as something of a
synonym for “protection.” The Court’s fuller description of Yearsley ex-
plains that it relieves the contractor of “liability,” without suggesting
that it also offers a pass from litigation. 317 U. S., at 583. And the sec-
ond cited case, Campbell-Ewald Co. v. Gomez, 577 U. S. 153 (2016), gives
GEO even less to work with. That decision merely quotes the imprecise
phrase in Brady on the way to rejecting another contractor’s claim (even
more expansive than GEO’s) to share in the Government’s sovereign im-
munity. 577 U. S., at 166.
12                 GEO GROUP, INC. v. MENOCAL

                          Opinion of the Court

point is reverse the erroneous liability finding. So the final-
ity rule of §1291 precludes interlocutory review of a Years-
ley denial.5
   For those reasons, we hold that the Court of Appeals
lacked jurisdiction over GEO’s appeal. If eventually found
liable, GEO may of course appeal the District Court’s rejec-
tion of its asserted Yearsley defense. But GEO must wait
until then. A Yearsley denial is not appealable before the
trial court’s proceedings have ended.
   We therefore affirm the judgment of the Court of Appeals
and remand the case for further proceedings consistent
with this opinion.
                                                      It is so ordered.




——————
   5 This holding still allows review of a given Yearsley denial by means

of §1292(b)’s separate appeal-certification process. Under that provision,
a district court may find that the special difficulty and importance of an
otherwise unappealable order counsels in favor of immediate review, and
an appellate court may accept that determination. Here, though, the
District Court saw no reason to act under §1292(b).
                  Cite as: 607 U. S. ____ (2026)              1

                      Opinion of THOMAS, J.

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–758
                          _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                       [February 25, 2026]

   JUSTICE THOMAS, concurring in part and concurring in
the judgment.
   I concur in Parts I and III of the Court’s opinion and in
its judgment. I agree with the Court that Yearsley v. W. A.
Ross Constr. Co., 309 U. S. 18 (1940), and similar decisions
establish a defense from liability and not an immunity from
suit. See ante, at 8–9. Orders rejecting Yearsley defenses
are therefore unlike the orders denying immunities that
this Court has already held to be immediately appealable.
Because no other statute or rule authorized an interlocu-
tory appeal here, the Court correctly affirms the Tenth Cir-
cuit’s dismissal. I do not join Part II because “[w]e need not,
and in my view should not, further justify our holding by
applying” the collateral-order doctrine established by Co-
hen v. Beneficial Industrial Loan Corp., 337 U. S. 541
(1949). Mohawk Industries, Inc. v. Carpenter, 558 U. S.
100, 115 (2009) (THOMAS, J., concurring in part and concur-
ring in judgment). I remain of the view that we should not
expand the Cohen collateral order doctrine beyond orders
that our precedents have already held to be immediately
appealable.
   The Cohen collateral-order doctrine, which allows federal
courts to exercise appellate jurisdiction over certain inter-
locutory orders, conflicts with Congress’s authority over
federal appellate jurisdiction. U. S. Const., Art. I, §8, cl. 9;
2               GEO GROUP, INC. v. MENOCAL

                     Opinion of THOMAS, J.

Art. III, §1. By statute, parties generally cannot appeal be-
fore final judgment. See 28 U. S. C. §1291; ante, at 3–4.
Congress has established certain exceptions to that final-
judgment rule that allow parties to appeal some interlocu-
tory orders immediately. E.g., §1292(a)(1). It has also au-
thorized this Court to create further exceptions through
rulemaking. §1292(e). Cohen’s collateral-order doctrine al-
lows judges to create additional exceptions by judicial opin-
ion, which bypasses “ ‘Congress’s designation of the rule-
making process as the way to define or refine when a
district court ruling is “final” and when an interlocutory or-
der is appealable.’ ” Mohawk Industries, 558 U. S., at 114–
115 (opinion of THOMAS, J.) (quoting Swint v. Chambers
County Comm’n, 514 U. S. 35, 48 (1995)). For that reason,
if an interlocutory order “is not on all fours with orders we
previously have held to be appealable under the collateral
order doctrine,” it should not be immediately appealable.
Mohawk Industries, 558 U. S., at 115 (opinion of THOMAS,
J.).
                  Cite as: 607 U. S. ____ (2026)             1

                ALITO, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–758
                          _________________


THE GEO GROUP, INC., PETITIONER v. ALEJANDRO
             MENOCAL, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                      [February 25, 2026]

   JUSTICE ALITO, concurring in the judgment.
   I agree with the Court that the defense conferred by
Yearsley v. W. A. Ross Constr. Co., 309 U. S. 18 (1940), is
not an “immunity from suit.” I therefore agree that an or-
der denying a Yearsley defense is not a “collateral order”
subject to immediate appeal. But I would not rest these
conclusions solely on the fact that Yearsley’s applicability
“turn[s] on [the defendant’s] conduct’s legality.” Ante, at 5.
Under the collateral-order doctrine, defendants may some-
times appeal the denial of a defense immediately when do-
ing so is necessary to vindicate important constitutional or
public-policy interests. And this rule holds true even if the
defense at issue turns on the legality of the defendant’s con-
duct. Thus, I cannot join the opinion of the Court, but I
concur in the judgment because deferring appellate review
of Yearsley rulings until final judgment does not imperil im-
portant constitutional or public-policy interests.
                                I
   Since 1789, Congress has generally limited the universe
of appealable orders to “final decrees and judgments.” Act
of Sept. 24, 1789, 1 Stat. 84. Today, this “final-judgment
rule” limits the jurisdiction of federal courts of appeals. See
28 U. S. C. §1291. The Court has long given this limit a
“practical rather than a technical construction.” Cohen v.
2               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

Beneficial Industrial Loan Corp., 337 U. S. 541, 546 (1949).
Consistent with that approach, our decision in Cohen held
that certain interlocutory orders—now known as collateral
orders—are sufficiently “final” that a party may appeal
them before litigation reaches final judgment. Id., at 546–
547.
  Our collateral-order doctrine establishes three criteria
that an order must satisfy to qualify for immediate appeal.
The order must (1) “conclusively determine [a] disputed
question,” (2) resolve an issue “separate from the merits of
the action,” and (3) be “effectively unreviewable on appeal
from a final judgment.” Coopers & Lybrand v. Livesay, 437
U. S. 463, 468 (1978). Whether a given order satisfies these
criteria does not turn on the “facts of a particular case.”
Carroll v. United States, 354 U. S. 394, 405 (1957). Rather,
the criteria must be satisfied for the “entire category” of or-
ders. Digital Equipment Corp. v. Desktop Direct, Inc., 511
U. S. 863, 868 (1994).
                               A
   Initially, this Court applied the “effectively unreviewa-
ble” requirement to capture orders that would become moot
by the time of final judgment. See Cohen, 337 U. S., at 546.
For those orders, a strict application of the final-judgment
rule “would practically defeat the right to any review at all.”
Cobbledick v. United States, 309 U. S. 323, 324–325 (1940).
We first applied this reasoning in Cohen, which involved a
district-court order that excused the plaintiffs from a litiga-
tion-bond requirement. 337 U. S., at 544–547. Applicable
state law required the plaintiffs to post such a bond to se-
cure their obligation to pay the defendant’s litigation ex-
penses and attorney’s fees if their claims failed. Cohen held
that the order excusing the plaintiffs from posting that
bond was immediately appealable because it would “not be
merged in final judgment.” Id., at 546. Regardless of who
prevailed at final judgment, the question whether the
                  Cite as: 607 U. S. ____ (2026)             3

                ALITO, J., concurring in judgment

plaintiffs had to post a bond would be moot. If the defend-
ant prevailed, an appeal would not relieve it from the plain-
tiffs’ failure to post a bond. And if the plaintiffs prevailed,
the defendant would not be entitled to recover its legal
costs. Thus, if orders denying requests for litigation bonds
were not subject to immediate appeal, those orders would
never receive appellate review.
   This conception of the collateral-order doctrine’s “effec-
tively unreviewable” requirement informed our decision in
Swift & Co. Packers v. Compania Colombiana Del Caribe,
S. A., 339 U. S. 684 (1950). There, we held that the Fifth
Circuit had appellate jurisdiction over a lower court’s order
vacating the attachment of a foreign vessel. Id., at 685–
689. That vessel, which the libelants attached while it
passed through U. S.-controlled waters, served as security
for their claims against the foreign defendant. In this re-
spect, the vessel resembled the bond in Cohen. As was the
case with the bond order, an immediate appeal was the only
means for appellate review of the order vacating the attach-
ment of the vessel. If the libelants in Swift did not prevail
at final judgment, the court’s vacatur of the attachment or-
der would become moot. And if the libelants did prevail,
any appellate review of the attachment issue would be an
“empty rite,” as the vessel would have likely departed U. S.
jurisdiction. 339 U. S., at 689.
   The same reasoning explains our jurisdictional holding in
Stack v. Boyle, 342 U. S. 1 (1951), which extended Cohen to
an order denying a criminal defendant’s motion to modify
his pretrial bail-bond amount. 342 U. S., at 3. Once a court
renders final judgment in a criminal case, the conditions
governing the defendant’s pretrial release become moot. By
that juncture, the defendant has either been released from
custody or begun a sentence of incarceration. Thus, if there
were to be any appellate review of bail, it would need to oc-
cur before final judgment.
4               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

   In sum, our early collateral-order cases applied the “ef-
fectively unreviewable” requirement narrowly. It captured
those orders that would be unreviewable on appeal from a
final judgment on account of mootness.
                               B
   Over the ensuing decades, the Court expanded its appli-
cation of the “effectively unreviewable” requirement to in-
clude orders that undoubtedly would not become moot by
final judgment. For example, in Abney v. United States, 431
U. S. 651 (1977), and Helstoski v. Meanor, 442 U. S. 500
(1979), the Court held that denials of defenses under the
Double Jeopardy Clause and Speech or Debate Clause sat-
isfied Cohen even though these protections could be “vindi-
cated on an appeal following final judgment.” Abney, 431
U. S., at 660. Like most criminal-law defenses, double-jeop-
ardy and speech-or-debate issues merge into the final judg-
ment, and a reviewing court can grant meaningful relief on
these grounds by reversing a defendant’s conviction. Abney
and Helstoski nevertheless held that denials of relief under
these two Clauses were collateral orders.
   Our holdings in these cases relied on the premise that
those two protections were not merely shields from criminal
liability. They were instead “guarantee[s] against being . . .
put to trial” at all. Abney, 431 U. S., at 661; accord, Hel-
stoski, 442 U. S., at 508 (“[T]he Speech or Debate Clause
was designed to protect Congressmen . . . from the burden
of defending themselves” (internal quotation marks omit-
ted)). Thus, although a court could review these defenses
on appeal from a final judgment, a court could not fully vin-
dicate their protections at that time. By the time of final
judgment, the defendant would have already been exposed
to trial, thereby suffering the very harm that these defenses
exist to prevent. This line of reasoning sufficed to render
the orders in Abney and Helstoski “effectively
                 Cite as: 607 U. S. ____ (2026)            5

                ALITO, J., concurring in judgment

unreviewable” on appeal from a final judgment. See Abney,
431 U. S., at 662.
   This doctrinal development had important implications
for our collateral-order jurisprudence. Under Abney and
Helstoski’s logic, once a court designates a defense as an
“immunity from suit,” that defense satisfies the third col-
lateral-order criterion. Digital Equipment, 511 U. S., at
870. We have likewise recognized that an order denying an
immunity from suit will also satisfy the other two collat-
eral-order requirements. See ante, at 7, n. 1. The denial of
an immunity satisfies the first criterion because it “conclu-
sively determine[s]” that a defendant may go to trial. Coop-
ers & Lybrand, 437 U. S., at 468. See Helstoski, 442 U. S.,
at 507 (“Once a motion to dismiss is denied, there is nothing
the Member can do under the [Speech or Debate] Clause . . .
to prevent the trial”). And a “claim of immunity is concep-
tually distinct from the merits,” so an order denying an im-
munity claim satisfies the second requirement. Mitchell v.
Forsyth, 472 U. S. 511, 527 (1985). For these reasons, fed-
eral courts have consistently held that denials of an immun-
ity are collateral orders subject to immediate appeal. See,
e.g., Nixon v. Fitzgerald, 457 U. S. 731, 742 (1982) (Presi-
dential civil immunity); Mitchell, 472 U. S., at 530 (quali-
fied immunity); Puerto Rico Aqueduct and Sewer Authority
v. Metcalf & Eddy, Inc., 506 U. S. 139, 143 (1993) (state and
territorial sovereign immunity); Kilburn v. Socialist Peo-
ple’s Libyan Arab Jamahiriya, 376 F. 3d 1123, 1126 (CADC
2004) (foreign sovereign immunity).
   Given that the designation of a defense as an immunity
is dispositive under the collateral-order doctrine, our Court
has stringently guarded the designation. See Midland As-
phalt Corp. v. United States, 489 U. S. 794, 801 (1989). Af-
ter all, “virtually every right that could be enforced appro-
priately by pretrial dismissal” could be loosely described as
an immunity from suit. Digital Equipment, 511 U. S., at
873. But treating every such right as an immunity would
6               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

permit the “narrow” collateral-order doctrine to “swallow”
the final judgment rule in “virtually every case.” Id., at 868,
873 (internal quotation marks omitted). Our Court has
therefore recognized the need to distinguish “between a
right not to be tried and a right whose remedy requires the
dismissal of charges.” United States v. Hollywood Motor
Car Co., 458 U. S. 263, 269 (1982) (per curiam). And we
have explained that determining whether a defense consti-
tutes an immunity requires an evaluation of “the value of
the interests” that an immediate appeal would advance.
Digital Equipment, 511 U. S., at 878–879. Specifically, we
explained in Will v. Hallock, 546 U. S. 345 (2006), that a
defense “should be treated as an immunity demanding the
protection of a collateral order appeal” only if wrongly al-
lowing a suit to proceed would “imperil a substantial public
interest.” Id., at 353; see also Lauro Lines s.r.l. v. Chasser,
490 U. S. 495, 502 (1989) (Scalia, J., concurring) (“The rea-
son” that a right fails the third requirement of the collat-
eral-order doctrine “is, quite simply, that the law does not
deem the right important enough”).
   Our collateral-order decisions reflect this approach. We
have applied the immunity label to defenses when allowing
an immediate appeal was necessary to preserve “some par-
ticular value of a high order,” such as “honoring the separa-
tion of powers, preserving the efficiency of government and
the initiative of its officials, respecting a State’s dignitary
interests, and mitigating the government’s advantage” over
individual defendants in high-stakes matters. Will, 546
U. S., at 352–353; see, e.g., Nixon, 457 U. S., at 742–743,
749, 758 (citing separation-of-powers concerns when allow-
ing an appeal of an order denying Presidential immunity);
Mitchell, 472 U. S., at 526 (explaining that the avoidance of
distraction, overdeterrence, and timidity in Government
service justified immediate appeals of orders denying qual-
ified immunity); Puerto Rico Aqueduct and Sewer Author-
ity, 506 U. S., at 146 (allowing an appeal of an order
                  Cite as: 607 U. S. ____ (2026)            7

                ALITO, J., concurring in judgment

denying sovereign immunity to “ ‘prevent the indignity of
subjecting a State to the coercive process of judicial tribu-
nals’ ”). In contrast, we have declined to designate defenses
as immunities when postponing appellate review to final
judgment would not imperil important interests. See, e.g.,
Will, 546 U. S., at 353 (holding that the interest in shorten-
ing troublesome litigation is insufficient to treat a defense
as an immunity); Mohawk Industries, Inc. v. Carpenter, 558
U. S. 100, 108–113 (2009) (acknowledging that the attor-
ney-client privilege serves important public interests but
declining to designate it as an immunity because deferring
appeals would not meaningfully harm those interests).
  As these decisions illustrate, we have been cautious in re-
cent years about expanding the collateral-order doctrine,
but we have not closed the book on Cohen. Just two Terms
ago, we designated another defense as an immunity and
evaluated it in an interlocutory posture. See Trump v.
United States, 603 U. S. 593, 635 (2024) (citing Mitchell,
472 U. S., at 524–530); 603 U. S., at 654–655 (BARRETT, J.,
concurring in part). The test for determining whether a de-
fense constitutes an immunity therefore remains keyed to
the interests that an immediate appeal would vindicate. If
postponing review of a wrongly denied defense would un-
dermine important constitutional or policy interests, that
defense constitutes an immunity.
                             II
  Under this framework, the Yearsley doctrine is not an im-
munity from suit. Permitting immediate appeals of orders
denying Yearsley defenses is not necessary to vindicate any
sufficiently important constitutional or public-policy inter-
ests.
                            A
  As the majority correctly explains, Yearsley shields de-
fendants from damages actions for conduct that federal law
8               GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

authorized. See Campbell-Ewald Co. v. Gomez, 577 U. S.
153, 166–167 (2016). Although this protection is important
for a range of Government operations, it does not meet the
threshold to be designated an immunity.
   First, postponing appellate review of Yearsley’s applica-
bility until final judgment would not create significant sep-
aration-of-powers problems. To be sure, the possibility that
courts might impose liability for conduct that Congress au-
thorized presents some conflict between those two branches
of Government. Likewise, incorrect contractor-liability ad-
judications can interfere with Executive Branch operations.
But these risks of error arise anytime a court misapplies a
federal statute or entertains an action involving a Govern-
ment contractor. Moreover, these risks pale in comparison
to the separation-of-powers concerns that motivated the ap-
plication of the collateral-order doctrine in other immunity
contexts. See, e.g., Helstoski, 442 U. S., at 502 (concerning
a Congressman who was exposed to criminal liability based
on his decision to introduce a bill in the House of Represent-
atives).
   Yearsley does not implicate sovereign-dignity interests,
either. Although GEO Group describes Yearsley as confer-
ring “derivative sovereign immunity” on contractors, Brief
for Petitioner 10, this label is a poor fit. Sovereign immun-
ity protects governments from the indignity of being sub-
jected to a court’s jurisdiction. Puerto Rico Aqueduct and
Sewer Authority, 506 U. S., at 146. We have never de-
scribed the Yearsley doctrine in those terms, nor have we
suggested that it limits courts’ jurisdiction over contractors.
Cf. Yearsley, 309 U. S., at 19 (noting without disagreement
that the lower court exercised jurisdiction over the case);
Campbell-Ewald Co., 577 U. S., at 165–166 (concluding
that the lower court had jurisdiction over a case before de-
termining whether Yearsley applied). Rather, Yearsley
merely shields contractors from exposure for conduct that
federal law authorized. I therefore agree with the majority
                     Cite as: 607 U. S. ____ (2026)                   9

                   ALITO, J., concurring in judgment

that the Yearsley doctrine “derives” from the Government’s
lawmaking authority, not its sovereign immunity. See
ante, at 9–10; cf. Campbell-Ewald Co., 577 U. S., at 166–
167; Sloan Shipyards Corp. v. United States Shipping Bd.
Emergency Fleet Corporation, 258 U. S. 549, 566–567
(1922).
   Last, unlike with qualified immunity, allowing immedi-
ate appeals of Yearsley denials is not necessary to prevent
overdeterrence, timidity, and distraction in Government
service. That is not to say that these concerns are entirely
absent when plaintiffs bring damages actions against Gov-
ernment contractors. As this Court recognized in Filarsky
v. Delia, 566 U. S. 377 (2012), the public has an interest in
preventing overdeterrence, timidity, and distraction in
Government functions no matter the “nature of [the defend-
ant’s] particular relationship with the government.” Id., at
389–392. But our doctrine already accommodates these
concerns by allowing contractors to invoke qualified im-
munity. Ibid.; Campbell-Ewald Co., 577 U. S., at 167. In-
deed, qualified immunity provides a greater protection to
contractors than Yearsley does. Whereas Yearsley shields
only those contractors who act within the bounds of their
legal authorization, qualified immunity protects “all but the
plainly incompetent or those who knowingly violate the
law.” Malley v. Briggs, 475 U. S. 335, 341 (1986). And as
the defense’s name indicates, contractors may immediately
appeal denials of qualified immunity. Mitchell, 472 U. S.,
at 530. Because qualified immunity already vindicates the
public interest in avoiding overdeterrence, timidity, and
distraction among contractors, there is no overriding inter-
est in also allowing immediate appeals of orders denying
Yearsley’s more modest protections.*           Cf. Mohawk
——————
 *Although Government contractors may generally assert qualified im-
munity, this Court has held that “private prison guards” may not in Rev.
10                 GEO GROUP, INC. v. MENOCAL

                    ALITO, J., concurring in judgment

Industries, Inc., 558 U. S., at 109–112 (declining to treat the
attorney-client privilege as an immunity because other “es-
tablished mechanisms for appellate review” were availa-
ble).
  In sum, allowing immediate appeals of orders denying
Yearsley defenses is not necessary to vindicate any im-
portant constitutional or public-policy interests. Accord-
ingly, the Yearsley doctrine is not an immunity from suit.
And because Yearsley issues can be reviewed on an appeal
from a final judgment, these orders do not otherwise satisfy
the third collateral-order requirement.
                               B
   Rather than conducting the public-interest inquiry that
our immunity case law employs, the majority trains most of
its analysis on a single question: Whether the Yearsley doc-
trine “turn[s] on [the defendant’s] conduct’s legality.” Ante,
at 5. Because the Yearsley doctrine does, the majority con-
cludes that it fails to satisfy the third collateral-order re-
quirement. That analysis is oversimplified.
   Of course, whether a defense turns on the legality of a
defendant’s conduct can be relevant to the collateral-order
analysis. For example, the degree of overlap between a
——————
Stat. §1979, 42 U. S. C. §1983 cases. See Richardson v. McKnight, 521
U. S. 399, 412 (1997). Separately, this Court has not decided whether
corporate-contractor defendants like GEO Group may invoke qualified
immunity. But see United Pet Supply, Inc. v. Chattanooga, 768 F. 3d
464, 484, n. 3 (CA6 2014) (noting that the Sixth Circuit has entertained
corporate defendants’ assertions of qualified immunity). Perhaps the
public interest would be well-served by allowing appeals of orders deny-
ing Yearsley defenses to those defendants who cannot invoke qualified
immunity. Even so, our doctrine requires us to decide whether Yearsley
denials are collateral orders as a category, not “as applied” to particular
defendants. If, however, most defendants who invoke Yearsley could not
invoke qualified immunity, the collateral-order analysis might be differ-
ent. For example, if corporate contractors could never invoke qualified
immunity, then there would be a stronger argument that denials of
Yearsley defenses should be immediately appealable.
                  Cite as: 607 U. S. ____ (2026)             11

                 ALITO, J., concurring in judgment

defense and a defendant’s conduct can bear on whether an
order is “ ‘separate from the merits of the action.’ ” Ante, at
7, n. 1; but see Mitchell, 472 U. S., at 527. It is also true
that certain “immunities from suit” are jurisdictional bars
that shield a defendant from judicial process regardless of
whether it acted lawfully. See, e.g., 28 U. S. C. § 1604 (cod-
ifying foreign sovereign immunity as a jurisdictional bar);
Seminole Tribe of Fla. v. Florida, 517 U. S. 44, 72–73 (1996)
(treating state sovereign immunity as a jurisdictional
limit).
   Nonetheless, the majority’s rule cannot fully explain our
collateral-order case law. For instance, qualified immunity
is an immunity from suit, yet its applicability can and often
does turn on whether a defendant violated the law. See
District of Columbia v. Wesby, 583 U. S. 48, 62–63 (2018).
Indeed, before this Court decided Pearson v. Callahan, 555
U. S. 223 (2009), a court evaluating a qualified-immunity
defense had to resolve the legality of the defendant’s alleged
conduct. Id., at 232; see, e.g., Scott v. Harris, 550 U. S. 372,
377 (2007). We nevertheless treated (and continue to treat)
denials of qualified immunity as collateral orders.
   On the other side of the ledger, we have held that several
defenses are not immunities even though they do not turn
on the legality of the defendant’s conduct. For instance, this
Court has held that neither the Federal Tort Claims Act’s
judgment bar nor a criminal defendant’s right against vin-
dictive prosecution qualifies as an immunity from suit, even
though neither defense concerns a defendant’s challenged
conduct. See Will, 546 U. S., at 353–355; Hollywood Motor
Car Co., 458 U. S., at 267–270; see also Digital Equipment
Corp., 511 U. S., at 884 (holding that a lower court’s refusal
to enforce a settlement agreement against a plaintiff ’s
claims was not a collateral order).
   In short, although the majority’s focus—whether a de-
fense turns on the legality of the defendant’s conduct—can
12              GEO GROUP, INC. v. MENOCAL

                ALITO, J., concurring in judgment

be relevant in the collateral-order analysis, it is not dispos-
itive of whether a defense constitutes an immunity.
                          *    *      *
   Because postponing appellate review of Yearsley issues
until final judgment would not imperil important constitu-
tional or public-policy interests, I concur in the judgment of
the Court.

```

---
