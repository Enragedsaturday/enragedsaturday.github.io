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

## GROUP: content/cases/Kaupp v. Texas.md  (`case`, 7 assertions)

### content_page

```
---
title: "Kaupp v. Texas"
type: case
citation: "538 U.S. 626 (2003)"
parallel_cite: "123 S. Ct. 1843; 155 L. Ed. 2d 814"
neutral_cite: 2003 U.S. LEXIS 3670
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2003
date_decided: 2003-05-05
docket: 02-5636
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2003-05-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kaupp v. Texas
  varies_by_point: false
  scope_note: "Per curiam application of Dunaway/Brown: a 3 a.m. station-house removal without probable cause is an arrest; the confession is its fruit absent attenuation. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/127919/kaupp-v-texas/"
  cluster_id: 127919
  opinion_id: 127919
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[Dunaway v. New York]]", "[[Brown v. Illinois]]", "[[Wong Sun v. United States]]", "[[Hayes v. Florida]]", "[[Taylor v. Alabama]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "probable-cause", "exclusionary-rule", "fruit-of-the-poisonous-tree", "consent"]
holding: "Awakening a 17-year-old at 3 a.m. and transporting him, handcuffed and in his underwear, to the station for interrogation without probable cause is an arrest; his 'Okay' was mere submission to authority, not consent, and the ensuing confession must be suppressed unless the State shows the taint was purged."
lake:
  record_id: Kaupp v. Texas
  status: verified
  projected_at: 2026-07-06
---

# Kaupp v. Texas

*538 U.S. 626 (2003)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a 14-year-old girl's murder, detectives suspected the 17-year-old Kaupp but lacked probable cause. About 3 a.m., at least three officers went to his home, were let in by his father, woke him with "we need to go and talk," handcuffed him, and took him — shoeless and in his underwear in January — to a patrol car, then to the crime scene and the sheriff's office. After [[Miranda and Custodial Interrogation|Miranda warnings]] and confrontation with a co-suspect's statement, he admitted some involvement. The Texas courts treated the encounter as consensual and admitted the confession.

## Issue
Whether removing a suspect from his home and transporting him to the station for interrogation, without probable cause, was an arrest requiring probable cause — and, if so, whether his confession must be suppressed as the fruit of that illegal arrest.

## Rule
Yes; an involuntary station-house transport for questioning is an arrest. "Such involuntary transport to a police station for questioning is 'sufficiently like arres[t] to invoke the traditional rule that arrests may constitutionally be made only on probable cause.'" — 538 U.S. at 630 (quoting *Hayes v. Florida*, 470 U.S. 811, 816). ^pin-630

Once the arrest is unlawful for want of probable cause, "well-established precedent requires suppression of the confession unless that confession was 'an act of free will [sufficient] to purge the primary taint of the unlawful invasion,'" with the burden on the State. — *Id.* at 632–633 (quoting *Wong Sun v. United States*, 371 U.S. 471, 486). ^pin-632

## Application
The facts pointed to arrest "even more starkly than the facts in *Dunaway*." "A 17-year-old boy was awakened in his bedroom at three in the morning by at least three police officers, one of whom stated 'we need to go and talk.' He was taken out in handcuffs, without shoes, dressed only in his underwear in January, placed in a patrol car, driven to the scene of a crime and then to the sheriff's offices, where he was taken into an interrogation room and questioned." — *Id.* at 631. ^pin-631

Kaupp's "'Okay'" was "no showing of consent" but "a mere submission to a claim of lawful authority"; the test is objective, so the officers' safety rationale and Kaupp's lack of resistance did not convert the seizure into a consensual encounter. Because he was arrested without probable cause, the confession had to be suppressed unless the State demonstrated purgation of the taint — an inquiry the state courts never reached, and which [[Miranda and Custodial Interrogation|Miranda warnings]] alone would not satisfy.

## Conclusion
[[Common Legal Terms#per-curiam|Per curiam]]: Kaupp was arrested within the meaning of the Fourth Amendment without probable cause; the consent finding was error. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] for the *[[Brown v. Illinois|Brown]]* [[Fruits and Attenuation|attenuation]] determination.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Kaupp* is a [[Common Legal Terms#per-curiam|per curiam]] application of [[Dunaway v. New York]] and the [[Brown v. Illinois]] / [[Wong Sun v. United States]] [[Fruits and Attenuation|attenuation]] line, mirroring [[Taylor v. Alabama]], and it relies on [[Hayes v. Florida]] for the "sufficiently like arrest" standard.

## Appears on
- [[Seizure of the Person]] — *Key — Progeny*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Kaupp v. Texas*, 538 U.S. 626 (2003) — https://www.courtlistener.com/opinion/127919/kaupp-v-texas/ — pinpoints: 630, 631, 632–633.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cfb4eac136d5a2df", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "538 U.S. 626 (2003)", "court": "U.S. Supreme Court", "neutral_cite": "2003 U.S. LEXIS 3670", "official_citation_present": true, "parallel_cite": "123 S. Ct. 1843; 155 L. Ed. 2d 814", "title": "Kaupp v. Texas", "year": "2003"}}
{"assertion_id": "162cbcf4ce882942", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key — Progeny", "title": "Kaupp v. Texas"}}
{"assertion_id": "30c3cb3b8844d44e", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (cross-doctrine)", "title": "Kaupp v. Texas"}}
{"assertion_id": "98df97186c8cd52d", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Related (cross-doctrine)", "title": "Kaupp v. Texas"}}
{"assertion_id": "df5b2024db782294", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Awakening a 17-year-old at 3 a.m. and transporting him, handcuffed and in his underwear, to the station for interrogation without probable cause is an arrest; his 'Okay' was mere submission to authority, not consent, and the ensuing confession must be suppressed unless the State shows the taint was purged.", "title": "Kaupp v. Texas"}}
{"assertion_id": "27c79b1f2c5d5830", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2003-05-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kaupp v. Texas", "field_i_validity": "good_law", "scope_note": "Per curiam application of Dunaway/Brown: a 3 a.m. station-house removal without probable cause is an arrest; the confession is its fruit absent attenuation. Good law.", "title": "Kaupp v. Texas", "varies_by_point": "false"}}
{"assertion_id": "36a7a7f2855f73b9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kaupp v. Texas"}}
```

### lake record — Kaupp v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kaupp v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kaupp v. Texas",
    "case_name_short": "Kaupp",
    "case_name_full": "Kaupp v. Texas",
    "input_case_name": "Kaupp v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2003-05-05",
    "year": 2003,
    "docket": "02-5636",
    "cluster_id": 127919,
    "lead_opinion_id": 127919,
    "sibling_ids": [
      127919
    ],
    "absolute_url": "/opinion/127919/kaupp-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 127896,
        "score": 20,
        "case_name": "Robert Kaupp v. Texas"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "538 U.S. 626",
      "volume": "538",
      "reporter": "U.S.",
      "page": "626",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "123 S. Ct. 1843",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 814",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "814",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2003 U.S. LEXIS 3670",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "3670",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "538 U.S. 626",
        "volume": "538",
        "reporter": "U.S.",
        "page": "626",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 S. Ct. 1843",
        "volume": "123",
        "reporter": "S. Ct.",
        "page": "1843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "155 L. Ed. 2d 814",
        "volume": "155",
        "reporter": "L. Ed. 2d",
        "page": "814",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2003 U.S. LEXIS 3670",
        "volume": "2003",
        "reporter": "U.S. LEXIS",
        "page": "3670",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "538 U.S. 626",
    "official_selection": {
      "court_class": "scotus",
      "selected": "538 U.S. 626",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-630",
      "page": null,
      "quote": "handcuffed him, and took him \u2014 shoeless and in his underwear in January \u2014 to a patrol car, then to the crime scene and the sheriff's office. After Miranda warnings and confrontation with a co-suspect's statement, he admitted some involvement. The Texas courts treated the encounter as consensual and admitted the confession. ## Issue Whether removing a suspect from his home and transporting him to the station for interrogation, without probable cause, was an arrest requiring probable cause \u2014 and, if so, whether his confession must be suppressed as the fruit of that illegal arrest. ## Rule Yes; an involuntary station-house transport for questioning is an arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-632",
      "page": null,
      "quote": "well-established precedent requires suppression of the confession unless that confession was 'an act of free will [sufficient] to purge the primary taint of the unlawful invasion,'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-631",
      "page": null,
      "quote": "even more starkly than the facts in *Dunaway*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2003-05-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kaupp v. Texas",
    "varies_by_point": false,
    "scope_note": "Per curiam application of Dunaway/Brown: a 3 a.m. station-house removal without probable cause is an arrest; the confession is its fruit absent attenuation. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Jenkins",
          "cluster_id": 9998064,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mercedes-De la Cruz",
          "cluster_id": 2803337,
          "cite": [
            "787 F.3d 61",
            "2015 U.S. App. LEXIS 8624",
            "2015 WL 3378255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Baldwin v. State",
          "cluster_id": 1427878,
          "cite": [
            "278 S.W.3d 367",
            "2009 Tex. Crim. App. LEXIS 318",
            "2009 WL 605368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. St. Germain",
          "cluster_id": 8455684,
          "cite": [
            "107 F. App'x 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kaupp, Robert Justin v. State",
          "cluster_id": 2930629,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane1_negative"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia-Cantu",
          "cluster_id": 1769810,
          "cite": [
            "253 S.W.3d 236",
            "2008 Tex. Crim. App. LEXIS 581",
            "2008 WL 1958956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 1654613,
          "cite": [
            "760 N.W.2d 35",
            "277 Neb. 37"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vernon Snype, Marisa Hicks",
          "cluster_id": 793658,
          "cite": [
            "441 F.3d 119",
            "69 Fed. R. Serv. 817",
            "2006 U.S. App. LEXIS 6909"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny L. Marshall v. Secretary, Florida Department of Corrections",
          "cluster_id": 4237860,
          "cite": [
            "828 F.3d 1277",
            "2016 U.S. App. LEXIS 12812",
            "2016 WL 3742164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
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
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Celis",
          "cluster_id": 2581042,
          "cite": [
            "93 P.3d 1027",
            "16 Cal. Rptr. 3d 85",
            "33 Cal. 4th 667",
            "2004 Cal. Daily Op. Serv. 6680",
            "2004 Daily Journal DAR 9051",
            "2004 Cal. LEXIS 6771"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Beauchamp",
          "cluster_id": 615987,
          "cite": [
            "659 F.3d 560",
            "2011 U.S. App. LEXIS 21498",
            "2011 WL 5041918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1867862,
          "cite": [
            "2006 WI 98",
            "717 N.W.2d 729",
            "294 Wis. 2d 1",
            "2006 Wisc. LEXIS 393",
            "2006 WL 1900137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 172784,
          "cite": [
            "584 F.3d 935",
            "2009 U.S. App. LEXIS 23296",
            "2009 WL 3381528"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. State",
          "cluster_id": 1384700,
          "cite": [
            "252 S.W.3d 571",
            "2008 Tex. App. LEXIS 2009",
            "2008 WL 731598"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Glass",
          "cluster_id": 1878755,
          "cite": [
            "136 S.W.3d 496",
            "2004 WL 1244459"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bailey",
          "cluster_id": 2654019,
          "cite": [
            "743 F.3d 322",
            "2014 WL 657932"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. De Jesus-Batres",
          "cluster_id": 38073,
          "cite": [
            "410 F.3d 154",
            "2005 U.S. App. LEXIS 8702",
            "2005 WL 1155677"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 76311,
          "cite": [
            "345 F.3d 1285",
            "2003 U.S. App. LEXIS 19457",
            "2003 WL 22158086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kaupp v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(127919) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 195,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 195,
        "triage_read": 10,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(127919)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NiZzPTc5NTY2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28127919%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(127919)",
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
    "complete_query": "cites:(127919)",
    "indexed_citing_opinions": 246,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 127919,
        "count": 246,
        "count_source": "search"
      }
    ],
    "citation_count": 414,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kaupp-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzOTI0JnM9NDY0MzMwOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28127919%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 127919,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 111382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 127919,
        "cited_id": 112631,
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
    "date_created": "2026-07-05T09:12:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:15:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kaupp v. Texas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b721-6">
<span citation-index="1" class="star-pagination" label="627"> 
   *627
   </span>
  Per Curiam.
 </author>
<p id="b721-7">
  This case turns on the Fourth Amendment rule that a confession “obtained by exploitation of an illegal arrest” may not be used against a criminal defendant.
  <em>
   Brown
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 603</a></span> (1975). After a 14-year-old girl disappeared in January 1999, the Harris County Sheriff’s Department learned she had had a sexual relationship with her 19-year-old half brother, who had been in the company of petitioner Robert Kaupp, then 17 years old, on the day of the girl’s disappearance. On January 26th, deputy sheriffs questioned the brother and Kaupp at headquarters; Kaupp was cooperative and was permitted to leave, but the brother
  <span citation-index="1" class="star-pagination" label="628"> 
   *628
   </span>
  failed a polygraph examination (his third such failure). Eventually he confessed that he had fatally stabbed his half sister and placed her body in a drainage ditch. He implicated Kaupp in the crime.
 </p>
<p id="b722-5">
  Detectives immediately tried but failed to obtain a warrant to question Kaupp.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Detective Gregory Pinkins nevertheless decided (in his words) to “get [Kaupp] in and confront him with what [the brother] had said.” App. A to Pet. for Cert. 2. In the company of two other plainclothes detectives and three uniformed officers, Pinkins went to Kaupp’s house at approximately 3 a.m. on January 27th. After Kaupp’s father let them in, Pinkins, with at least two other officers, went to Kaupp’s bedroom, awakened him with a flashlight, identified himself, and said, “‘we need to go and talk.’”
  <em>
   <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Ibid.</a></span>
  </em>
  Kaupp said “‘Okay.’”
  <em>
   <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Ibid.</a></span>
  </em>
  The two officers then handcuffed Kaupp and led him, shoeless and dressed only in boxer shorts and a T-shirt, out of his house and into a patrol car. The State points to nothing in the record indicating Kaupp was told that he was free to decline to go with the officers.
 </p>
<p id="b722-6">
  They stopped for 5 or 10 minutes where the victim’s body had just been found, in anticipation of confronting Kaupp with the brother’s confession, and then went on to the sheriff’s headquarters. There, they took Kaupp to an interview room, removed his handcuffs, and advised him of his rights under
  <em>
   Miranda
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Kaupp first denied any involvement in the victim’s disappearance, but 10
  <span citation-index="1" class="star-pagination" label="629"> 
   *629
   </span>
  or 15 minutes into the interrogation, told of the brother’s confession, he admitted having some part in the crime. He did not, however, acknowledge causing the fatal wound or confess to murder, for which he was later indicted.
 </p>
<p id="b723-5">
  After moving unsuccessfully to suppress his confession as the fruit of an illegal arrest, Kaupp was convicted and sentenced to 55 years’ imprisonment. The State Court of Appeals affirmed the conviction by unpublished opinion, concluding that no arrest had occurred until after the confession. The state court said that Kaupp consented to go with the officers when he answered “'Okay’” to Pinkins’s statement that “‘we need to go and talk.’” App. A to Pet. for Cert. 2, 6. The court saw no contrary significance in the subsequent handcuffing and removal to the patrol car, given the practice of the sheriff’s department in “routinely” using handcuffs for safety purposes when transporting individuals, as officers had done with Kaupp only the day before.
  <em>
   Id.,
  </em>
  at 6. The court observed that “a reasonable person in [Kaupp’s] position would not believe that being put in handcuffs was a significant restriction on his freedom of movement.”
  <em>
   Ibid.
  </em>
  Finally, the state court noted that Kaupp “did not resist the use of handcuffs or act in a manner consistent with anything other than full cooperation.”
  <em>
   Id.,
  </em>
  at 6-7. Kaupp appealed, but the Court of Criminal Appeals of Texas denied discretionary review. App. B to Pet. for Cert. We grant the motion for leave to proceed
  <em>
   informa pauperis,
  </em>
  grant the petition for certiorari, and vacate the judgment below.
 </p>
<p id="b723-6">
  A seizure of the person within the meaning of the Fourth and Fourteenth Amendments occurs when, “taking into account all of the circumstances surrounding the encounter, the police conduct would ‘have communicated to a reasonable person that he was not at liberty to ignore the police presence and go about his business.’”
  <em>
   Florida
  </em>
  v.
  <em>
   Bostick,
  </em>
  <span class="citation" data-id="9842116"><a href="/opinion/112631/florida-v-bostick/#437" aria-description="Citation for case: Florida v. Bostick">501 U. S. 429, 437</a></span> (1991) (quoting
  <em>
   Michigan
  </em>
  v.
  <em>
   Chesternut,
  </em>
  <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#569" aria-description="Citation for case: Michigan v. Chesternut">486 U. S. 567, 569</a></span> (1988)). This test is derived from Justice
  <span citation-index="1" class="star-pagination" label="630"> 
   *630
   </span>
  Stewart’s opinion in
  <em>
   United States
  </em>
  v.
  <em>
   Mendenhall,
  </em>
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544</a></span> (1980), see
  <em>
   California
  </em>
  v.
  <em>
   Hodari D.,
  </em>
  <span class="citation" data-id="9432255"><a href="/opinion/112579/california-v-hodari-d/#627" aria-description="Citation for case: California v. Hodari D.">499 U. S. 621, 627-628</a></span> (1991), which gave several “[e]xamples of circumstances that might indicate a seizure, even where the person did not attempt to leave,” including “the threatening presence of several officers, the display of a weapon by an officer, some physical touching of the person of the citizen, or the use of language or tone of voice indicating that compliance with the officer’s request might be compelled.”
  <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall"><em>
   Mendenhall, supra,
  </em>
  at 554</a></span>.
 </p>
<p id="b724-5">
  Although certain seizures may be justified on something less than probable cause, see,
  <em>
   e. g., Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), we have never “sustained against Fourth Amendment challenge the involuntary removal of a suspect from his home to a police station and his detention there for investigative purposes ... absent probable cause or judicial authorization.”
  <em>
   Hayes
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#815" aria-description="Citation for case: Hayes v. Florida">470 U. S. 811, 815</a></span> (1985);
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  cf.
  <em>
   Payton
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 589-590</a></span> (1980); compare
  <em>
   Florida
  </em>
  v.
  <em>
   Royer,
  </em>
  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#499" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 499</a></span> (1983) (plurality opinion) (“[The police] may [not] seek to verify [mere] suspicions by means that approach the conditions of arrest”), with
  <em>
   United States
  </em>
  v.
  <em>
   Sokolow,
  </em>
  <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989) (“[T]he police can stop and briefly detain a person for investigative purposes if the officer has a reasonable suspicion supported by articulable facts that criminal activity ‘may be afoot,’ even if the officer lacks probable cause” (quoting
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio"><em>
   Terry, supra,
  </em>
  at 30</a></span>)). Such involuntary transport to a police station for questioning is “sufficiently like arres[t] to invoke the traditional rule that arrests may constitutionally be made only on probable cause.”
  <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#816" aria-description="Citation for case: Hayes v. Florida"><em>
   Hayes, supra,
  </em>
  at 816</a></span>.
 </p>
<p id="b724-6">
  The State does not claim to have had probable cause here, and a straightforward application of the test just mentioned shows beyond cavil that Kaupp was arrested within the
  <span citation-index="1" class="star-pagination" label="631"> 
   *631
   </span>
  meaning of the Fourth Amendment, there being evidence of every one of the probative circumstances mentioned by Justice Stewart in Mendenhall.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  A 17-year-old boy was awakened in his bedroom at three in the morning by at least three police officers, one of whom stated “‘we need to go and talk.’” He was taken out in handcuffs, without shoes, dressed only in his underwear in January, placed in a patrol car, driven to the scene of a crime and then to the sheriff’s offices, where he was taken into an interrogation room and questioned. This evidence points to arrest even more starkly than the facts in
  <em>
   Dunaway
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#212" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 212</a></span> (1979), where the petitioner “was taken from a neighbor’s home to a police car, transported to a police station, and placed in an interrogation room.” There we held it clear that the detention was “in important respects indistinguishable from a traditional arrest” and therefore required probable cause or judicial authorization to be legal.
  <em>
   <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">Ibid.</a></span>
  </em>
  The same is, if anything, even clearer here.
 </p>
<p id="b725-5">
  Contrary reasons mentioned by the state courts are no answer to the facts. Kaupp’s “ ‘Okay’ ” in response to Pin-kins’s statement is no showing of consent under the circumstances. Pinkins offered Kaupp no choice, and a group of police officers rousing an adolescent out of bed in the middle of the night with the words “ ‘we need to go and talk’ ” presents no option but “to go.” There is no reason to think Kaupp’s answer was anything more than “a mere submission to a claim of lawful authority.”
  <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer"><em>
   Royer, supra,
  </em>
  at 497</a></span> (plurality opinion); see also
  <em>
   Schneckloth
  </em>
  v.
  <em>
   Bustamante,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226, 233-234</a></span> (1973). If reasonable doubt were possible
  <span citation-index="1" class="star-pagination" label="632"> 
   *632
   </span>
  on this point, the ensuing events would resolve it: removal from one’s house in handcuffs on a January night with nothing on but underwear for a trip to a crime scene on the way to an interview room at law enforcement headquarters. Even “an initially consensual encounter . . . can be transformed into a seizure or detention within the meaning of the Fourth Amendment.”
  <em>
   INS
  </em>
  v.
  <em>
   Delgado,
  </em>
  <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984); see
  <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#815" aria-description="Citation for case: Hayes v. Florida"><em>
   Hayes, supra,
  </em>
  at 815-816</a></span> (“[A]t some point in the investigative process, police procedures can qualitatively and quantitatively be so intrusive with respect to a suspect’s freedom of movement and privacy interests as to trigger the full protection of the Fourth and Fourteenth Amendments”). It cannot seriously be suggested that when the detectives began to question Kaupp, a reasonable person in his situation would have thought he was sitting in the interview room as a matter of choice, free to change his mind and go home to bed.
 </p>
<p id="b726-5">
  Nor is it significant, as the state court thought, that the sheriff’s department “routinely” transported individuals, including Kaupp on one prior occasion, while handcuffed for safety of the officers, or that Kaupp “did not resist the use of handcuffs or act in a manner consistent with anything other than full cooperation.” App. A to Pet. for Cert. 6. The test is an objective one, see,
  <em>
   e. g., Chesternut,
  </em>
  <span class="citation" data-id="9431339"><a href="/opinion/112095/michigan-v-chesternut/#574" aria-description="Citation for case: Michigan v. Chesternut">486 U. S., at 574</a></span>, and stressing the officers’ motivation of self-protection does not speak to how their actions would reasonably be understood. As for the lack of resistance, failure to struggle with a cohort of deputy sheriffs is not a waiver of Fourth Amendment protection, which does not require the perversity of resisting arrest or assaulting a police officer.
 </p>
<p id="b726-6">
  Since Kaupp was arrested before he was questioned, and because the State does not even claim that the sheriff’s department had probable cause to detain him at that point, well-established precedent requires suppression of the confession unless that confession was “an act of free will [sufficient] to purge the primary taint of the unlawful invasion.”
  <span citation-index="1" class="star-pagination" label="633"> 
   *633
   </span>
<em>
   Wong Sun
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 486</a></span> (1963). Demonstrating such purgation is, of course, a function of circumstantial evidence, with the burden of persuasion on the State. See
  <em>
   Brown,
  </em>
  <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>. Relevant considerations include observance of
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,
  </em>
  “[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, and, particularly, the purpose and flagrancy of the official misconduct.” <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 603-604</a></span> (footnotes and citation omitted).
 </p>
<p id="b727-5">
  The record before us shows that only one of these considerations, the giving of
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings, supports the State, and we held in
  <em>
   <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>
  </em>
  that
  <em>
   “Miranda
  </em>
  warnings,
  <em>
   alone
  </em>
  and
  <em>
   -per se,
  </em>
  cannot always ... break, for Fourth Amendment purposes, the causal connection between the illegality and the confession.” <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 603</a></span> (emphasis in original); see also
  <em>
   Taylor
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#699" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687, 699</a></span> (1982) (O’Connor, J., dissenting) (noting that, although
  <em>
   <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>
  </em>
  warnings are an important factor, “they are, standing alone, insufficient”). All other factors point the opposite way. There is no indication from the record that any substantial time passed between Kaupp’s removal from his home in handcuffs and his confession after only 10 or 15 minutes of interrogation. In the interim, he remained in his partially clothed state in the physical custody of a number of officers, some of whom, at least, were conscious that they lacked probable cause to arrest. See
  <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois"><em>
   Brown, supra,
  </em>
  at 604-605</a></span>. In fact, the State has not even alleged “any meaningful intervening event” between the illegal arrest and Kaupp’s confession.
  <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#691" aria-description="Citation for case: Taylor v. Alabama"><em>
   Taylor, supra,
  </em>
  at 691</a></span>. Unless, on remand, the State can point to testimony undisclosed on the record before us, and weighty enough to carry the State’s burden despite the clear force of the evidence shown here, the confession must be suppressed.
 </p>
<p id="b727-6">
  The judgment of the State Court of Appeals is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b727-7">
<em>
   It is so ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b722-7">
   The detectives applied to the district attorney’s office for a “pocket warrant,” which they described as authority to take Kaupp into custody for questioning. App. 3 to App. D to Pet. for Cert. 6 (trial transcript). The detectives did not seek a conventional arrest warrant, as they did not believe they had probable cause for Kaupp’s arrest. See
   <em>
    <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/" aria-description="Citation for case: Taylor v. Alabama">ibid.</a></span>
   </em>
   As the trial court later explained, the detectives had no evidence or motive to corroborate the brother’s allegations of Kaupp’s involvement, see App. C to Pet. for Cert. 2; the brother had previously failed three polygraph examinations, while, only two days earlier, Kaupp had voluntarily taken and passed one, in which he denied his involvement, see
   <em>
    id.,
   </em>
   at 1-2.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b724-7">
   We have, however, left open the possibility that, “under circumscribed procedures,” a court might validly authorize a seizure on less than probable cause when the object is fingerprinting.
   <em>
    Hayes,
   </em>
   <span class="citation" data-id="9429967"><a href="/opinion/111382/hayes-v-florida/#817" aria-description="Citation for case: Hayes v. Florida">470 U. S., at 817</a></span>.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b725-6">
   On the record before us, it is possible to debate whether the law enforcement officers were armed. The State Court of Appeals not only described them as armed but said specifically that PinWns’s weapon was visible, though not drawn, when he confronted Kaupp in the bedroom. See App. A to Pet. for Cert. 6. But at least one officer testified before the trial court that they went to Kaupp’s house unarmed. See App. 3 to App. D to Pet. for Cert. 8 (trial transcript).
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Kyllo v. United States.md  (`case`, 8 assertions)

### content_page

```
---
title: "Kyllo v. United States"
type: case
citation: "533 U.S. 27 (2001)"
parallel_cite: "121 S. Ct. 2038; 150 L. Ed. 2d 94"
neutral_cite: 2001 U.S. LEXIS 4487
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-06-11
docket: 99-8508
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-06-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kyllo v. United States
  varies_by_point: false
  scope_note: "Good law; a cornerstone of the modern search-definition line, reinforced by Jones (2012), Jardines (2013), and Carpenter (2018)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118443/kyllo-v-united-states/"
  cluster_id: 118443
  opinion_id: 118443
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Key"
  - page: "[[Aerial and Enhanced Surveillance]]"
    role: "Key — enhanced-sensor limit"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Related (cross-doctrine)"
related: ["[[Katz v. United States]]", "[[California v. Ciraolo]]", "[[Florida v. Jardines]]", "[[United States v. Jones]]", "[[Carpenter v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "home", "thermal-imaging", "surveillance", "technology"]
holding: "Using sense-enhancing technology not in general public use to explore details of a home's interior that could not otherwise be obtained without physical intrusion is a Fourth Amendment search, presumptively unreasonable without a warrant."
lake:
  record_id: Kyllo v. United States
  status: verified
  projected_at: 2026-07-09
---

# Kyllo v. United States

*533 U.S. 27 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Suspecting that Danny Kyllo was growing marijuana indoors under high-intensity lamps, a federal agent used a thermal-imaging device (an Agema Thermovision 210) from a public street to scan Kyllo's home. The scan showed that the roof over the garage and a side wall were relatively warm compared with the rest of the home and neighboring units, consistent with grow lamps. Relying on the imaging together with tips and utility records, agents obtained a warrant, searched the home, and found a marijuana-growing operation. Kyllo moved to suppress.

## Issue
Whether the use of a thermal-imaging device aimed at a private home from a public street, to detect relative amounts of heat within the home, constitutes a "search" within the meaning of the Fourth Amendment.

## Rule
Yes. "We think that obtaining by sense-enhancing technology any information regarding the interior of the home that could not otherwise have been obtained without physical 'intrusion into a constitutionally protected area' . . . constitutes a search — at least where (as here) the technology in question is not in general public use." — 533 U.S. at 34. ^pin-34

The Court declined to limit the rule to "intimate" details, because "[i]n the home, our cases show, *all* details are intimate details, because the entire area is held safe from prying government eyes." — [*Id.* at 37](https://www.courtlistener.com/opinion/118443/kyllo-v-united-states/#:~:text=details%2C%20because). ^pin-37

It therefore held: "Where, as here, the Government uses a device that is not in general public use, to explore details of the home that would previously have been unknowable without physical intrusion, the surveillance is a 'search' and is presumptively unreasonable without a warrant." — *Id.* at 40. ^pin-40

## Application
The agent used a thermal imager — a device not in general public use — to learn about the relative warmth of areas inside Kyllo's home, information that could not have been obtained without physically entering. That the device measured only heat radiating from exterior surfaces did not save it, any more than the eavesdropping in *[[Katz v. United States|Katz]]* was permissible because it captured only sound at the booth's exterior; and because the target was a home, the relative warmth of its rooms counted as an intimate detail. The thermal scan was thus a search, and being warrantless it was presumptively unreasonable.

## Conclusion
The thermal imaging was an unlawful warrantless search; the case was [[Reading and Citing Cases#on-remand|remanded]] to determine whether, without the thermal evidence, the warrant was supported by probable cause. *Kyllo* anchors the rule that technological surveillance revealing a home's interior is a Fourth Amendment search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Kyllo* remains good law and is a cornerstone of the modern search-definition line: its concern with privacy-eroding technology and home sanctity informs [[United States v. Jones]] (2012), [[Florida v. Jardines]] (2013), and [[Carpenter v. United States]] (2018).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Key*
- [[Aerial and Enhanced Surveillance]] — *Key — enhanced-sensor limit*
- [[Curtilage]] — *Related (cross-doctrine)*
- [[Third-Party Doctrine & CSLI]] — *Related (cross-doctrine)*

## Sources
- *Kyllo v. United States*, 533 U.S. 27 (2001) — https://www.courtlistener.com/opinion/118443/kyllo-v-united-states/ — pinpoints: 34, 37, 40.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10e633a89a620d26", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "533 U.S. 27 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 4487", "official_citation_present": true, "parallel_cite": "121 S. Ct. 2038; 150 L. Ed. 2d 94", "title": "Kyllo v. United States", "year": "2001"}}
{"assertion_id": "224f12413d284945", "dimension": "support", "kind": "home_role", "locator": {"home": "Aerial and Enhanced Surveillance"}, "payload": {"home": "Aerial and Enhanced Surveillance", "role": "Key — enhanced-sensor limit", "title": "Kyllo v. United States"}}
{"assertion_id": "3b51ff37ccaa5006", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Related (cross-doctrine)", "title": "Kyllo v. United States"}}
{"assertion_id": "6350bae58c870b45", "dimension": "support", "kind": "home_role", "locator": {"home": "Curtilage"}, "payload": {"home": "Curtilage", "role": "Related (cross-doctrine)", "title": "Kyllo v. United States"}}
{"assertion_id": "71418ee1b0d304e8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Using sense-enhancing technology not in general public use to explore details of a home's interior that could not otherwise be obtained without physical intrusion is a Fourth Amendment search, presumptively unreasonable without a warrant.", "title": "Kyllo v. United States"}}
{"assertion_id": "88ac6214a97e1fc2", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Key", "title": "Kyllo v. United States"}}
{"assertion_id": "26da44b0f8ecc274", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-06-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Kyllo v. United States", "field_i_validity": "good_law", "scope_note": "Good law; a cornerstone of the modern search-definition line, reinforced by Jones (2012), Jardines (2013), and Carpenter (2018).", "title": "Kyllo v. United States", "varies_by_point": "false"}}
{"assertion_id": "e52f0d945883266c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Kyllo v. United States"}}
```

### lake record — Kyllo v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kyllo v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kyllo v. United States",
    "case_name_short": "Kyllo",
    "case_name_full": "Kyllo v. United States",
    "input_case_name": "Kyllo v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-06-11",
    "year": 2001,
    "docket": "99-8508",
    "cluster_id": 118443,
    "lead_opinion_id": 118443,
    "sibling_ids": [
      118443,
      9434104,
      9434105
    ],
    "absolute_url": "/opinion/118443/kyllo-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "533 U.S. 27",
      "volume": "533",
      "reporter": "U.S.",
      "page": "27",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 2038",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "2038",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "150 L. Ed. 2d 94",
        "volume": "150",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 4487",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4487",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "533 U.S. 27",
        "volume": "533",
        "reporter": "U.S.",
        "page": "27",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 2038",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "2038",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "150 L. Ed. 2d 94",
        "volume": "150",
        "reporter": "L. Ed. 2d",
        "page": "94",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 4487",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4487",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "533 U.S. 27",
    "official_selection": {
      "court_class": "scotus",
      "selected": "533 U.S. 27",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-34",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-37",
      "page": null,
      "quote": "details, because",
      "star_marker": "37",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 21798,
      "fragment": "#:~:text=details%2C%20because",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-40",
      "page": null,
      "quote": "Where, as here, the Government uses a device that is not in general public use, to explore details of the home that would previously have been unknowable without physical intrusion, the surveillance is a 'search' and is presumptively unreasonable without a warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-06-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kyllo v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; a cornerstone of the modern search-definition line, reinforced by Jones (2012), Jardines (2013), and Carpenter (2018).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Pond",
          "cluster_id": 9416983,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane1_negative"
      },
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
        "journal_ref": "Kyllo v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Goldberg",
          "cluster_id": 10134107,
          "cite": [
            "309 Or. App. 660",
            "483 P.3d 671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. Washington",
          "cluster_id": 145641,
          "cite": [
            "165 L. Ed. 2d 224",
            "126 S. Ct. 2266",
            "547 U.S. 813",
            "2006 U.S. LEXIS 4886"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Heller",
          "cluster_id": 145777,
          "cite": [
            "171 L. Ed. 2d 637",
            "128 S. Ct. 2783",
            "554 U.S. 570",
            "2008 U.S. LEXIS 5268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Steelman",
          "cluster_id": 1891638,
          "cite": [
            "93 S.W.3d 102",
            "2002 Tex. Crim. App. LEXIS 206",
            "2002 WL 31398545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Warshak",
          "cluster_id": 181032,
          "cite": [
            "631 F.3d 266",
            "2010 U.S. App. LEXIS 25415",
            "2010 WL 5071766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Atkinson v. City of Mountain View",
          "cluster_id": 819982,
          "cite": [
            "709 F.3d 1201",
            "2013 WL 462381",
            "2013 U.S. App. LEXIS 2703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sewn Newton",
          "cluster_id": 786350,
          "cite": [
            "369 F.3d 659",
            "2004 U.S. App. LEXIS 10343",
            "2004 WL 1161747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caballes",
          "cluster_id": 2192166,
          "cite": [
            "851 N.E.2d 26",
            "221 Ill. 2d 282",
            "303 Ill. Dec. 128",
            "2006 Ill. LEXIS 625"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. Rosenthal v. Poe",
          "cluster_id": 1794984,
          "cite": [
            "98 S.W.3d 194",
            "2003 Tex. Crim. App. LEXIS 37",
            "2003 WL 291926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
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
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernandez v. California",
          "cluster_id": 2654534,
          "cite": [
            "188 L. Ed. 2d 25",
            "134 S. Ct. 1126",
            "2014 U.S. LEXIS 1636",
            "82 U.S.L.W. 4102",
            "571 U.S. 292",
            "24 Fla. L. Weekly Fed. S 553",
            "2014 WL 700100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kyllo v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118443 OR 9434104 OR 9434105) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTE0OTM3NjAwMDAwJnM9NDQ1Njc4OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118443+OR+9434104+OR+9434105%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118443 OR 9434104 OR 9434105)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTgmcz03ODkwNzImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118443+OR+9434104+OR+9434105%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118443 OR 9434104 OR 9434105)",
        "reviewed": 78,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 78,
        "triage_read": 1,
        "triage_snippet_classified": 77
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118443 OR 9434104 OR 9434105)",
    "indexed_citing_opinions": 990,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118443,
        "count": 796,
        "count_source": "search"
      },
      {
        "opinion_id": 9434104,
        "count": 211,
        "count_source": "search"
      },
      {
        "opinion_id": 9434105,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1843,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kyllo-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MTA5NDUmcz0xMDYxNTMxNSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118443+OR+9434104+OR+9434105%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118443,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 112067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 670592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 687649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 690298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 701846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 706029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 718297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
        "cited_id": 766078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118443,
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
    "date_created": "2026-07-05T10:39:42Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:39:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:39:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:42:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:39:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kyllo v. United States

```
<div>
<center><b><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">533 U.S. 27</a></span> (2001)</b></center>
<center><h1>KYLLO<br>
v.<br>
UNITED STATES</h1></center>
<center>No. 99-8508.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued February 20, 2001.</center>
<center>Decided June 11, 2001.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*28</span> <span class="star-pagination">*29</span> Scalia, J., delivered the opinion of the Court, in which Souter, Thomas, Ginsburg, and Breyer, JJ., joined. Stevens, J., filed a dissenting opinion, in which Rehnquist, C. J., and O'Connor and Kennedy, JJ., joined, <i>post,</i> p. 41.</p>
<p><i>Kenneth Lerner,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./531/955/">531 U. S. 955</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Deputy Solicitor General Dreeben</i> argued the cause for the United States. With him on the brief were former <i>Solicitor General Waxman, Assistant Attorney General Robinson, Irving L. Gornstein,</i> and <i>Deborah Watson.</i><sup>[*]</sup></p>
<p>Justice Scalia, delivered the opinion of the Court.</p>
<p>This case presents the question whether the use of a thermal-imaging device aimed at a private home from a public street to detect relative amounts of heat within the home constitutes a "search" within the meaning of the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>In 1991 Agent William Elliott of the United States Department of the Interior came to suspect that marijuana was being grown in the home belonging to petitioner Danny Kyllo, part of a triplex on Rhododendron Drive in Florence, Oregon. Indoor marijuana growth typically requires highintensity lamps. In order to determine whether an amount of heat was emanating from petitioner's home consistent with the use of such lamps, at 3:20 a.m. on January 16, 1992, Agent Elliott and Dan Haas used an Agema Thermovision 210 thermal imager to scan the triplex. Thermal imagers detect infrared radiation, which virtually all objects emit but which is not visible to the naked eye. The imager converts radiation into images based on relative warmthblack <span class="star-pagination">*30</span> is cool, white is hot, shades of gray connote relative differences; in that respect, it operates somewhat like a video camera showing heat images. The scan of Kyllo's home took only a few minutes and was performed from the passenger seat of Agent Elliott's vehicle across the street from the front of the house and also from the street in back of the house. The scan showed that the roof over the garage and a side wall of petitioner's home were relatively hot compared to the rest of the home and substantially warmer than neighboring homes in the triplex. Agent Elliott concluded that petitioner was using halide lights to grow marijuana in his house, which indeed he was. Based on tips from informants, utility bills, and the thermal imaging, a Federal Magistrate Judge issued a warrant authorizing a search of petitioner's home, and the agents found an indoor growing operation involving more than 100 plants. Petitioner was indicted on one count of manufacturing marijuana, in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). He unsuccessfully moved to suppress the evidence seized from his home and then entered a conditional guilty plea.</p>
<p>The Court of Appeals for the Ninth Circuit remanded the case for an evidentiary hearing regarding the intrusiveness of thermal imaging. On remand the District Court found that the Agema 210 "is a non-intrusive device which emits no rays or beams and shows a crude visual image of the heat being radiated from the outside of the house"; it "did not show any people or activity within the walls of the structure"; "[t]he device used cannot penetrate walls or windows to reveal conversations or human activities"; and "[n]o intimate details of the home were observed." Supp. App. to Pet. for Cert. 39-40. Based on these findings, the District Court upheld the validity of the warrant that relied in part upon the thermal imaging, and reaffirmed its denial of the motion to suppress. A divided Court of Appeals initially reversed, <span class="citation" data-id="6966699"><a href="/opinion/7062647/united-states-v-kyllo/" aria-description="Citation for case: United States v. Kyllo">140 F. 3d 1249</a></span> (1998), but that <span class="star-pagination">*31</span> opinion was withdrawn and the panel (after a change in composition) affirmed, <span class="citation" data-id="9492483"><a href="/opinion/766078/united-states-v-danny-lee-kyllo/" aria-description="Citation for case: United States v. Danny Lee Kyllo">190 F. 3d 1041</a></span> (1999), with Judge Noonan dissenting. The court held that petitioner had shown no subjective expectation of privacy because he had made no attempt to conceal the heat escaping from his home, <span class="citation" data-id="9492483"><a href="/opinion/766078/united-states-v-danny-lee-kyllo/#1046" aria-description="Citation for case: United States v. Danny Lee Kyllo"><i>id.,</i>  at 1046</a></span>, and even if he had, there was no objectively reasonable expectation of privacy because the imager "did not expose any intimate details of Kyllo's life," only "amorphous `hot spots' on the roof and exterior wall," <span class="citation" data-id="9492483"><a href="/opinion/766078/united-states-v-danny-lee-kyllo/#1047" aria-description="Citation for case: United States v. Danny Lee Kyllo"><i>id.,</i> at 1047</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./530/1305/">530 U. S. 1305</a></span> (2000).</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." "At the very core" of the Fourth Amendment "stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion." <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961). With few exceptions, the question whether a warrantless search of a home is reasonable and hence constitutional must be answered no. See <i>Illinois</i> v. <i>Rodriguez,</i> <span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#181" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177, 181</a></span> (1990); <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980).</p>
<p>On the other hand, the antecedent question whether or not a Fourth Amendment "search" has occurred is not so simple under our precedent. The permissibility of ordinary visual surveillance of a home used to be clear because, well into the 20th century, our Fourth Amendment jurisprudence was tied to common-law trespass. See, <i>e. g., </i><i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S. 129, 134-136</a></span> (1942); <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 464-466</a></span> (1928). Cf. <i>Silverman</i> v. <i>United States, supra,</i> at 510-512 (technical trespass not necessary for Fourth Amendment violation; it suffices if there is "actual intrusion into a constitutionally protected area"). Visual surveillance was unquestionably lawful because "`the <span class="star-pagination">*32</span> eye cannot by the laws of England be guilty of a trespass.' " <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#628" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 628</a></span> (1886) (quoting <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765)). We have since decoupled violation of a person's Fourth Amendment rights from trespassory violation of his property, see <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143</a></span> (1978), but the lawfulness of warrantless visual surveillance of a home has still been preserved. As we observed in <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 213</a></span> (1986), "[t]he Fourth Amendment protection of the home has never been extended to require law enforcement officers to shield their eyes when passing by a home on public thoroughfares."</p>
<p>One might think that the new validating rationale would be that examining the portion of a house that is in plain public view, while it is a "search"<sup>[1]</sup> despite the absence of trespass, is not an "unreasonable" one under the Fourth Amendment. See <i>Minnesota</i> v. <i>Carter,</i> <span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#104" aria-description="Citation for case: Minnesota v. Carter">525 U. S. 83, 104</a></span> (1998) (Breyer, J., concurring in judgment). But in fact we have held that visual observation is no "search" at all perhaps in order to preserve somewhat more intact our doctrine that warrantless searches are presumptively unconstitutional. See <i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/#234" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227, 234-235, 239</a></span> (1986). In assessing when a search is not a search, we have applied somewhat in reverse the principle first enunciated in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> involved eavesdropping by means of an electronic listening device placed on the outside of a telephone bootha location not within the catalog ("persons, houses, papers, and effects") that the Fourth Amendment protects against unreasonable searches. We held that the <span class="star-pagination">*33</span> Fourth Amendment nonetheless protected Katz from the warrantless eavesdropping because he "justifiably relied" upon the privacy of the telephone booth. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>. As Justice Harlan's oft-quoted concurrence described it, a Fourth Amendment search occurs when the government violates a subjective expectation of privacy that society recognizes as reasonable. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span>. We have subsequently applied this principle to hold that a Fourth Amendment search does <i>not</i> occureven when the explicitly protected location of a <i>house</i> is concernedunless "the individual manifested a subjective expectation of privacy in the object of the challenged search," and "society [is] willing to recognize that expectation as reasonable." <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo"><i>Ciraolo, supra,</i> at 211</a></span>. We have applied this test in holding that it is not a search for the police to use a pen register at the phone company to determine what numbers were dialed in a private home, <i>Smith</i> v. <i>Maryland,</i> <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#743" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 743-744</a></span> (1979), and we have applied the test on two different occasions in holding that aerial surveillance of private homes and surrounding areas does not constitute a search, <i><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">Ciraolo, supra;</a></span> </i><i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">488 U. S. 445</a></span> (1989).</p>
<p>The present case involves officers on a public street engaged in more than naked-eye surveillance of a home. We have previously reserved judgment as to how much technological enhancement of ordinary perception from such a vantage point, if any, is too much. While we upheld enhanced aerial photography of an industrial complex in <i>Dow Chemical,</i> we noted that we found "it important that this is <i>not</i> an area immediately adjacent to a private home, where privacy expectations are most heightened," 476 U. S., at 237, n. 4 (emphasis in original).</p>
<p></p>
<h2>III</h2>
<p>It would be foolish to contend that the degree of privacy secured to citizens by the Fourth Amendment has been <span class="star-pagination">*34</span> entirely unaffected by the advance of technology. For example, as the cases discussed above make clear, the technology enabling human flight has exposed to public view (and hence, we have said, to official observation) uncovered portions of the house and its curtilage that once were private. See <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Ciraolo, supra,</i> at 215</a></span>. The question we confront today is what limits there are upon this power of technology to shrink the realm of guaranteed privacy.</p>
<p>The <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> testwhether the individual has an expectation of privacy that society is prepared to recognize as reasonablehas often been criticized as circular, and hence subjective and unpredictable. See 1 W. LaFave, Search and Seizure § 2.1(d), pp. 393-394 (3d ed. 1996); Posner, The Uncertain Protection of Privacy by the Supreme Court, 1979 S. Ct. Rev. 173, 188; <span class="citation" data-id="9433723"><a href="/opinion/118249/minnesota-v-carter/#97" aria-description="Citation for case: Minnesota v. Carter"><i>Carter, supra,</i> at 97</a></span> (Scalia, J., concurring). But see <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois"><i>Rakas, supra,</i> at 143-144, n. 12</a></span>. While it may be difficult to refine <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> when the search of areas such as telephone booths, automobiles, or even the curtilage and uncovered portions of residences is at issue, in the case of the search of the interior of homesthe prototypical and hence most commonly litigated area of protected privacy there is a ready criterion, with roots deep in the common law, of the minimal expectation of privacy that <i>exists,</i> and that is acknowledged to be <i>reasonable.</i> To withdraw protection of this minimum expectation would be to permit police technology to erode the privacy guaranteed by the Fourth Amendment. We think that obtaining by senseenhancing technology any information regarding the interior of the home that could not otherwise have been obtained without physical "intrusion into a constitutionally protected area," <i>Silverman,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#512" aria-description="Citation for case: Silverman v. United States">365 U. S., at 512</a></span>, constitutes a search at least where (as here) the technology in question is not in general public use. This assures preservation of that degree of privacy against government that existed when the Fourth Amendment was adopted. On the basis of this criterion, the <span class="star-pagination">*35</span> information obtained by the thermal imager in this case was the product of a search.<sup>[2]</sup></p>
<p>The Government maintains, however, that the thermal imaging must be upheld because it detected "only heat radiating from the external surface of the house," Brief for United States 26. The dissent makes this its leading point, see <i>post,</i> at 41, contending that there is a fundamental difference between what it calls "off-the-wall" observations and "through-the-wall surveillance." But just as a thermal imager captures only heat emanating from a house, so also a powerful directional microphone picks up only sound emanating from a houseand a satellite capable of scanning from many miles away would pick up only visible light emanating from a house. We rejected such a mechanical interpretation of the Fourth Amendment in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> where the eavesdropping device picked up only sound waves that reached the exterior of the phone booth. Reversing that approach would leave the homeowner at the mercy of advancing technology including imaging technology that could discern all human <span class="star-pagination">*36</span> activity in the home. While the technology used in the present case was relatively crude, the rule we adopt must take account of more sophisticated systems that are already in use or in development.<sup>[3]</sup> The dissent's reliance on the distinction between "off-the-wall" and "through-the-wall" observation is entirely incompatible with the dissent's belief, which we discuss below, that thermal-imaging observations of the intimate details of a home are impermissible. The most sophisticated thermal-imaging devices continue to measure heat "off-the-wall" rather than "through-the-wall"; the dissent's disapproval of those more sophisticated thermalimaging devices, see <i>post,</i> at 49, is an acknowledgment that there is no substance to this distinction. As for the dissent's extraordinary assertion that anything learned through "an inference" cannot be a search, see <i>post,</i> at 44, that would validate even the "through-the-wall" technologies that the dissent purports to disapprove. Surely the dissent does not believe that the through-the-wall radar or ultrasound technology produces an 8-by-10 Kodak glossy that needs no analysis (<i>i. e.,</i> the making of inferences). And, of course, the novel proposition that inference insulates a search is blatantly contrary to <i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">468 U. S. 705</a></span> (1984), where the police "inferred" from the activation of a beeper that a certain can of ether was in the home. The police activity <span class="star-pagination">*37</span> was held to be a search, and the search was held unlawful.<sup>[4]</sup></p>
<p>The Government also contends that the thermal imaging was constitutional because it did not "detect private activities occurring in private areas," Brief for United States 22. It points out that in <i>Dow Chemical</i> we observed that the enhanced aerial photography did not reveal any "intimate details." 476 U. S., at 238. <i>Dow Chemical,</i> however, involved enhanced aerial photography of an industrial complex, which does not share the Fourth Amendment sanctity of the home. The Fourth Amendment's protection of the home has never been tied to measurement of the quality or quantity of information obtained. In <i><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span>,</i> for example, we made clear that any physical invasion of the structure of the home, "by even a fraction of an inch," was too much, <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#512" aria-description="Citation for case: Silverman v. United States">365 U. S., at 512</a></span>, and there is certainly no exception to the warrant requirement for the officer who barely cracks open the front door and sees nothing but the nonintimate rug on the vestibule floor. In the home, our cases show, <i>all</i> details are intimate details, because the entire area is held safe from prying government eyes. Thus, in <i><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">Karo, supra,</a></span></i> the only thing detected was a can of ether in the <span class="star-pagination">*38</span> home; and in <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321</a></span> (1987), the only thing detected by a physical search that went beyond what officers lawfully present could observe in "plain view" was the registration number of a phonograph turntable. These were intimate details because they were details of the home, just as was the detail of how warmor even how relatively warmKyllo was heating his residence.<sup>[5]</sup></p>
<p>Limiting the prohibition of thermal imaging to "intimate details" would not only be wrong in principle; it would be impractical in application, failing to provide "a workable accommodation between the needs of law enforcement and the interests protected by the Fourth Amendment," <i>Oliver</i>  v. <i>United States,</i> <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#181" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 181</a></span> (1984). To begin with, there is no necessary connection between the sophistication of the surveillance equipment and the "intimacy" of the details that it observeswhich means that one cannot say (and the police cannot be assured) that use of the relatively crude equipment at issue here will always be lawful. The Agema Thermovision 210 might disclose, for example, at what hour each night the lady of the house takes her daily sauna and batha detail that many would consider "intimate"; and a much more sophisticated system might detect nothing more intimate than the fact that someone left a closet light on. We could not, in other words, develop a rule approving only that through-the-wall surveillance which identifies objects no smaller than 36 by 36 inches, but would have to develop a jurisprudence specifying which <span class="star-pagination">*39</span> home activities are "intimate" and which are not. And even when (if ever) that jurisprudence were fully developed, no police officer would be able to know <i>in advance</i> whether his through-the-wall surveillance picks up "intimate" details and thus would be unable to know in advance whether it is constitutional.</p>
<p>The dissent's proposed standardwhether the technology offers the "functional equivalent of actual presence in the area being searched," <i>post,</i> at 47would seem quite similar to our own at first blush. The dissent concludes that <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i>  was such a case, but then inexplicably asserts that if the same listening device only revealed the volume of the conversation, the surveillance would be permissible, <i>post,</i> at 49-50. Yet if, without technology, the police could not discern volume without being actually present in the phone booth, Justice Stevens should conclude a search has occurred. Cf. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#735" aria-description="Citation for case: United States v. Karo">468 U. S., at 735</a></span> (Stevens, J., concurring in part and dissenting in part) ("I find little comfort in the Court's notion that no invasion of privacy occurs until a listener obtains some significant information by use of the device. . . . A bathtub is a less private area when the plumber is present even if his back is turned"). The same should hold for the interior heat of the home if only a person present in the home could discern the heat. Thus the driving force of the dissent, despite its recitation of the above standard, appears to be a distinction among different types of informationwhether the "homeowner would even care if anybody noticed," <i>post,</i> at 50. The dissent offers no practical guidance for the application of this standard, and for reasons already discussed, we believe there can be none. The people in their houses, as well as the police, deserve more precision.<sup>[6]</sup></p>
<p><span class="star-pagination">*40</span> We have said that the Fourth Amendment draws "a firm line at the entrance to the house," <i>Payton,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U. S., at 590</a></span>. That line, we think, must be not only firm but also bright which requires clear specification of those methods of surveillance that require a warrant. While it is certainly possible to conclude from the videotape of the thermal imaging that occurred in this case that no "significant" compromise of the homeowner's privacy has occurred, we must take the long view, from the original meaning of the Fourth Amendment forward.</p>
<blockquote>"The Fourth Amendment is to be construed in the light of what was deemed an unreasonable search and seizure when it was adopted, and in a manner which will conserve public interests as well as the interests and rights of individual citizens." <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925).</blockquote>
<p>Where, as here, the Government uses a device that is not in general public use, to explore details of the home that would previously have been unknowable without physical intrusion, the surveillance is a "search" and is presumptively unreasonable without a warrant.</p>
<p>Since we hold the Thermovision imaging to have been an unlawful search, it will remain for the District Court to determine whether, without the evidence it provided, the search warrant issued in this case was supported by probable causeand if not, whether there is any other basis for supporting admission of the evidence that the search pursuant to the warrant produced.</p>
<p></p>
<h2>
<span class="star-pagination">*41</span> * * *</h2>
<p>The judgment of the Court of Appeals is reversed; the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Stevens, with whom The Chief Justice, Justice O'Connor, and Justice Kennedy join, dissenting.</p>
<p>There is, in my judgment, a distinction of constitutional magnitude between "through-the-wall surveillance" that gives the observer or listener direct access to information in a private area, on the one hand, and the thought processes used to draw inferences from information in the public domain, on the other hand. The Court has crafted a rule that purports to deal with direct observations of the inside of the home, but the case before us merely involves indirect deductions from "off-the-wall" surveillance, that is, observations of the exterior of the home. Those observations were made with a fairly primitive thermal imager that gathered data exposed on the outside of petitioner's home but did not invade any constitutionally protected interest in privacy.<sup>[1]</sup> Moreover, I believe that the supposedly "bright-line" rule the Court has created in response to its concerns about future technological developments is unnecessary, unwise, and inconsistent with the Fourth Amendment.</p>
<p></p>
<h2>I</h2>
<p>There is no need for the Court to craft a new rule to decide this case, as it is controlled by established principles from <span class="star-pagination">*42</span> our Fourth Amendment jurisprudence. One of those core principles, of course, is that "searches and seizures <i>inside a home</i> without a warrant are presumptively unreasonable." <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 586</a></span> (1980) (emphasis added). But it is equally well settled that searches and seizures of property in plain view are presumptively reasonable. See <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><i>id.,</i> at 586-587</a></span>.<sup>[2]</sup> Whether that property is residential or commercial, the basic principle is the same: "`What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection.' " <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#213" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207, 213</a></span> (1986) (quoting <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967)); see <i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/#449" aria-description="Citation for case: Florida v. Riley">488 U. S. 445, 449-450</a></span> (1989); <i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#40" aria-description="Citation for case: California v. Greenwood">486 U. S. 35, 40-41</a></span> (1988); <i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/#235" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227, 235-236</a></span> (1986); <i>Air Pollution Variance Bd. of Colo.</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974). That is the principle implicated here.</p>
<p>While the Court "take[s] the long view" and decides this case based largely on the potential of yet-to-be-developed technology that might allow "through-the-wall surveillance," <i>ante,</i> at 38-40; see <i>ante,</i> at 36, n. 3, this case involves nothing more than off-the-wall surveillance by law enforcement officers to gather information exposed to the general public from the outside of petitioner's home. All that the infrared camera did in this case was passively measure heat emitted <span class="star-pagination">*43</span> from the exterior surfaces of petitioner's home; all that those measurements showed were relative differences in emission levels, vaguely indicating that some areas of the roof and outside walls were warmer than others. As still images from the infrared scans show, see Appendix, <i>infra,</i>  no details regarding the interior of petitioner's home were revealed. Unlike an x-ray scan, or other possible "throughthe-wall" techniques, the detection of infrared radiation emanating from the home did not accomplish "an unauthorized physical penetration into the premises," <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#509" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 509</a></span> (1961), nor did it "obtain information that it could not have obtained by observation from outside the curtilage of the house," <i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#715" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 715</a></span> (1984).</p>
<p>Indeed, the ordinary use of the senses might enable a neighbor or passerby to notice the heat emanating from a building, particularly if it is vented, as was the case here. Additionally, any member of the public might notice that one part of a house is warmer than another part or a nearby building if, for example, rainwater evaporates or snow melts at different rates across its surfaces. Such use of the senses would not convert into an unreasonable search if, instead, an adjoining neighbor allowed an officer onto her property to verify her perceptions with a sensitive thermometer. Nor, in my view, does such observation become an unreasonable search if made from a distance with the aid of a device that merely discloses that the exterior of one house, or one area of the house, is much warmer than another. Nothing more occurred in this case.</p>
<p>Thus, the notion that heat emissions from the outside of a dwelling are a private matter implicating the protections of the Fourth Amendment (the text of which guarantees the right of people "to be secure <i>in</i> their . . . houses" against unreasonable searches and seizures (emphasis added)) is not only unprecedented but also quite difficult to take seriously. Heat waves, like aromas that are generated in a kitchen, or <span class="star-pagination">*44</span> in a laboratory or opium den, enter the public domain if and when they leave a building. A subjective expectation that they would remain private is not only implausible but also surely not "one that society is prepared to recognize as `reasonable.' " <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring).</p>
<p>To be sure, the homeowner has a reasonable expectation of privacy concerning what takes place within the home, and the Fourth Amendment's protection against physical invasions of the home should apply to their functional equivalent. But the equipment in this case did not penetrate the walls of petitioner's home, and while it did pick up "details of the home" that were exposed to the public, <i>ante,</i> at 38, it did not obtain "any information regarding the <i>interior</i> of the home," <i>ante,</i> at 34 (emphasis added). In the Court's own words, based on what the thermal imager "showed" regarding the outside of petitioner's home, the officers "concluded" that petitioner was engaging in illegal activity inside the home. <i>Ante,</i> at 30. It would be quite absurd to characterize their thought processes as "searches," regardless of whether they inferred (rightly) that petitioner was growing marijuana in his house, or (wrongly) that "the lady of the house [was taking] her daily sauna and bath." <i>Ante,</i> at 38. In either case, the only conclusions the officers reached concerning the interior of the home were at least as indirect as those that might have been inferred from the contents of discarded garbage, see <i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">486 U. S. 35</a></span> (1988), or pen register data, see <i>Smith</i> v. <i>Maryland,</i>  <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735</a></span> (1979), or, as in this case, subpoenaed utility records, see <span class="citation" data-id="9492483"><a href="/opinion/766078/united-states-v-danny-lee-kyllo/#1043" aria-description="Citation for case: United States v. Danny Lee Kyllo">190 F. 3d 1041, 1043</a></span> (CA9 1999). For the first time in its history, the Court assumes that an inference can amount to a Fourth Amendment violation. See <i>ante,</i>  at 36-37.<sup>[3]</sup></p>
<p><span class="star-pagination">*45</span> Notwithstanding the implications of today's decision, there is a strong public interest in avoiding constitutional litigation over the monitoring of emissions from homes, and over the inferences drawn from such monitoring. Just as "the police cannot reasonably be expected to avert their eyes from evidence of criminal activity that could have been observed by any member of the public," <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/#41" aria-description="Citation for case: California v. Greenwood">486 U. S., at 41</a></span>, so too public officials should not have to avert their senses or their equipment from detecting emissions in the public domain such as excessive heat, traces of smoke, suspicious odors, odorless gases, airborne particulates, or radioactive emissions, any of which could identify hazards to the community. In my judgment, monitoring such emissions with "sense-enhancing technology," <i>ante,</i> at 34, and drawing useful conclusions from such monitoring, is an entirely reasonable public service.</p>
<p>On the other hand, the countervailing privacy interest is at best trivial. After all, homes generally are insulated to keep heat in, rather than to prevent the detection of heat going out, and it does not seem to me that society will suffer from a rule requiring the rare homeowner who both intends to engage in uncommon activities that produce extraordinary amounts of heat, and wishes to conceal that production from outsiders, to make sure that the surrounding area is well insulated. Cf. <i>United States</i> v. <i>Jacobsen,</i> <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#122" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 122</a></span> (1984) ("The concept of an interest in privacy that society is prepared to recognize as reasonable is, by its very nature, critically different from the mere expectation, however well <span class="star-pagination">*46</span> justified, that certain facts will not come to the attention of the authorities"). The interest in concealing the heat escaping from one's house pales in significance to "the chief evil against which the wording of the Fourth Amendment is directed," the "physical entry of the home," <i>United States</i> v. <i>United States Dist. Court for Eastern Dist. of Mich.,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972), and it is hard to believe that it is an interest the Framers sought to protect in our Constitution.</p>
<p>Since what was involved in this case was nothing more than drawing inferences from off-the-wall surveillance, rather than any "through-the-wall" surveillance, the officers' conduct did not amount to a search and was perfectly reasonable.<sup>[4]</sup></p>
<p></p>
<h2>II</h2>
<p>Instead of trying to answer the question whether the use of the thermal imager in this case was even arguably unreasonable, the Court has fashioned a rule that is intended to provide essential guidance for the day when "more sophisticated systems" gain the "ability to `see' through walls and other opaque barriers." <i>Ante,</i> at 36, and n. 3. The newly minted rule encompasses "obtaining [1] by senseenhancing technology [2] any information regarding the interior of the home [3] that could not otherwise have been obtained without physical intrusion into a constitutionally protected area . . . [4] at least where (as here) the technology in question is not in general public use." <i>Ante,</i> at 34 (internal quotation marks omitted). In my judgment, the <span class="star-pagination">*47</span> Court's new rule is at once too broad and too narrow, and is not justified by the Court's explanation for its adoption. As I have suggested, I would not erect a constitutional impediment to the use of sense-enhancing technology unless it provides its user with the functional equivalent of actual presence in the area being searched.</p>
<p>Despite the Court's attempt to draw a line that is "not only firm but also bright," <i>ante,</i> at 40, the contours of its new rule are uncertain because its protection apparently dissipates as soon as the relevant technology is "in general public use," <i>ante,</i> at 34. Yet how much use is general public use is not even hinted at by the Court's opinion, which makes the somewhat doubtful assumption that the thermal imager used in this case does not satisfy that criterion.<sup>[5]</sup> In any event, putting aside its lack of clarity, this criterion is somewhat perverse because it seems likely that the threat to privacy will grow, rather than recede, as the use of intrusive equipment becomes more readily available.</p>
<p>It is clear, however, that the category of "sense-enhancing technology" covered by the new rule, <i>ibid.,</i> is far too broad. It would, for example, embrace potential mechanical substitutes for dogs trained to react when they sniff narcotics. But in <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#707" aria-description="Citation for case: United States v. Place">462 U. S. 696, 707</a></span> (1983), we held that a dog sniff that "discloses only the presence or absence of narcotics" does "not constitute a `search' within the meaning of the Fourth Amendment," and it must follow that sense-enhancing equipment that identifies nothing but illegal <span class="star-pagination">*48</span> activity is not a search either. Nevertheless, the use of such a device would be unconstitutional under the Court's rule, as would the use of other new devices that might detect the odor of deadly bacteria or chemicals for making a new type of high explosive, even if the devices (like the dog sniffs) are "so limited both in the manner in which" they obtain information and "in the content of the information" they reveal. <i><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Ibid.</a></span></i> If nothing more than that sort of information could be obtained by using the devices in a public place to monitor emissions from a house, then their use would be no more objectionable than the use of the thermal imager in this case.</p>
<p>The application of the Court's new rule to "any information regarding the interior of the home," <i>ante,</i> at 34, is also unnecessarily broad. If it takes sensitive equipment to detect an odor that identifies criminal conduct and nothing else, the fact that the odor emanates from the interior of a home should not provide it with constitutional protection. See <i>supra,</i> at 47 and this page. The criterion, moreover, is too sweeping in that information "regarding" the interior of a home apparently is not just information obtained through its walls, but also information concerning the outside of the building that could lead to (however many) inferences "regarding" what might be inside. Under that expansive view, I suppose, an officer using an infrared camera to observe a man silently entering the side door of a house at night carrying a pizza might conclude that its interior is now occupied by someone who likes pizza, and by doing so the officer would be guilty of conducting an unconstitutional "search" of the home.</p>
<p>Because the new rule applies to information regarding the "interior" of the home, it is too narrow as well as too broad. Clearly, a rule that is designed to protect individuals from the overly intrusive use of sense-enhancing equipment should not be limited to a home. If such equipment <span class="star-pagination">*49</span> did provide its user with the functional equivalent of access to a private placesuch as, for example, the telephone booth involved in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> or an office buildingthen the rule should apply to such an area as well as to a home. See <i>Katz,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span> ("[T]he Fourth Amendment protects people, not places").</p>
<p>The final requirement of the Court's new rule, that the information "could not otherwise have been obtained without physical intrusion into a constitutionally protected area," <i>ante,</i> at 34 (internal quotation marks omitted), also extends too far as the Court applies it. As noted, the Court effectively treats the mental process of analyzing data obtained from external sources as the equivalent of a physical intrusion into the home. See <i>supra,</i> at 44. As I have explained, however, the process of drawing inferences from data in the public domain should not be characterized as a search.</p>
<p>The two reasons advanced by the Court as justifications for the adoption of its new rule are both unpersuasive. First, the Court suggests that its rule is compelled by our holding in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> because in that case, as in this, the surveillance consisted of nothing more than the monitoring of waves emanating from a private area into the public domain. See <i>ante,</i> at 35. Yet there are critical differences between the cases. In <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the electronic listening device attached to the outside of the phone booth allowed the officers to pick up the content of the conversation inside the booth, making them the functional equivalent of intruders because they gathered information that was otherwise available only to someone inside the private area; it would be as if, in this case, the thermal imager presented a view of the heat-generating activity inside petitioner's home. By contrast, the thermal imager here disclosed only the relative amounts of heat radiating from the house; it would be as if, in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the listening device disclosed only the relative <span class="star-pagination">*50</span> volume of sound leaving the booth, which presumably was discernible in the public domain.<sup>[6]</sup> Surely, there is a significant difference between the general and well-settled expectation that strangers will not have direct access to the contents of private communications, on the one hand, and the rather theoretical expectation that an occasional homeowner would even care if anybody noticed the relative amounts of heat emanating from the walls of his house, on the other. It is pure hyperbole for the Court to suggest that refusing to extend the holding of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> to this case would leave the homeowner at the mercy of "technology that could discern all human activity in the home." <i>Ante,</i> at 35-36.</p>
<p>Second, the Court argues that the permissibility of "through-the-wall surveillance" cannot depend on a distinction between observing "intimate details" such as "the lady of the house [taking] her daily sauna and bath," and noticing only "the nonintimate rug on the vestibule floor" or "objects no smaller than 36 by 36 inches." <i>Ante,</i> at 37, 38-39. This entire argument assumes, of course, that the thermal imager in this case could or did perform "through-thewall surveillance" that could identify any detail "that would previously have been unknowable without physical intrusion." <i>Ante,</i> at 39-40. In fact, the device could not, see n. 1, <i>supra,</i> and did not, see Appendix, <i>infra,</i> enable its user to identify either the lady of the house, the rug on the vestibule floor, or anything else inside the house, whether smaller or larger than 36 by 36 inches. Indeed, the vague thermal images of petitioner's home that are reproduced in the Appendix were submitted by him to the District Court as part of an expert report raising the question whether the device could even take "accurate, consistent infrared images" of the <span class="star-pagination">*51</span> <i>outside</i> of his house. Defendant's Exh. 107, p. 4. But even if the device could reliably show extraordinary differences in the amounts of heat leaving his home, drawing the inference that there was something suspicious occurring inside the residencea conclusion that officers far less gifted than Sherlock Holmes would readily drawdoes not qualify as "through-the-wall surveillance," much less a Fourth Amendment violation.</p>
<p></p>
<h2>III</h2>
<p>Although the Court is properly and commendably concerned about the threats to privacy that may flow from advances in the technology available to the law enforcement profession, it has unfortunately failed to heed the tried and true counsel of judicial restraint. Instead of concentrating on the rather mundane issue that is actually presented by the case before it, the Court has endeavored to craft an all-encompassing rule for the future. It would be far wiser to give legislators an unimpeded opportunity to grapple with these emerging issues rather than to shackle them with prematurely devised constitutional constraints.</p>
<blockquote>I respectfully dissent. [Appendix to opinion of Stevens, J., follows this page.]</blockquote>
<p><span class="star-pagination">*52</span> APPENDIX TO OPINION OF STEVENS, J.</p>
<p>(Images and text reproduced from defendant's exhibit 107) Top left: Infrared image of a video frame from the videotape submitted as evidence in this case. The thermogram indicates the suspect house as it appeared with the Gain and contrast in its default setting. Only the outline of the house is visible. The camera used was the Thermovision 210. Top Right: Infrared image of a subsequent videoframe taken from the videotape. The gain and contrast settings have been increased in order to make the walls and roof of the structure appear hotter than what it actually is. Bottom Left: Infrared image of the opposite side of the suspects house. The thermogram is also taken from the same videotape. The camera settings are in the default mode and the outline of the house is barely visible. Only the hot electrical transformer and the street light are identifiable. Bottom Right: The same image, but with the gain and contrast increased. This change in camera settings cause any object to appear hotter than what it actually is. The arrow indicates the overloading of an area immediately around a hot object in this case the electrical transformer and the streetlight. This overloading of the image is an inherent design flaw in the camera itself.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the Liberty Project by <i>Julie M. Carpenter;</i> and for the National Association of Criminal Defense Lawyers et al. by <i>James J. Tomkovicz, Lisa B. Kemler,</i> and <i>Steven R. Shapiro.</i> </p>
<p>[1]  When the Fourth Amendment was adopted, as now, to "search" meant "[t]o look over or through for the purpose of finding something; to explore; to examine by inspection; as, to <i>search</i> the house for a book; to <i>search</i> the wood for a thief." N. Webster, An American Dictionary of the English Language 66 (1828) (reprint 6th ed. 1989).</p>
<p>[2]  The dissent's repeated assertion that the thermal imaging did not obtain information regarding the interior of the home, <i>post,</i> at 43, 44 (opinion of Stevens, J.), is simply inaccurate. A thermal imager reveals the relative heat of various rooms in the home. The dissent may not find that information particularly private or important, see <i>post,</i> at 43-44, 45, 49-50, but there is no basis for saying it is not information regarding the interior of the home. The dissent's comparison of the thermal imaging to various circumstances in which outside observers might be able to perceive, without technology, the heat of the homefor example, by observing snowmelt on the roof, <i>post,</i> at 43is quite irrelevant. The fact that equivalent information could sometimes be obtained by other means does not make lawful the use of means that violate the Fourth Amendment. The police might, for example, learn how many people are in a particular house by setting up year-round surveillance; but that does not make breaking and entering to find out the same information lawful. In any event, on the night of January 16, 1992, no outside observer could have discerned the relative heat of Kyllo's home without thermal imaging.</p>
<p>[3]  The ability to "see" through walls and other opaque barriers is a clear, and scientifically feasible, goal of law enforcement research and development. The National Law Enforcement and Corrections Technology Center, a program within the United States Department of Justice, features on its Internet Website projects that include a "RadarBased Through-the-Wall Surveillance System," "Handheld Ultrasound Through the Wall Surveillance," and a "Radar Flashlight" that "will enable law enforcement officers to detect individuals through interior building walls." www.nlectc.org/techproj/ (visited May 3, 2001). Some devices may emit low levels of radiation that travel "through-the-wall," but others, such as more sophisticated thermal-imaging devices, are entirely passive, or "off-the-wall" as the dissent puts it.</p>
<p>[4]  The dissent asserts, <i>post,</i> at 44-45, n. 3, that we have misunderstood its point, which is not that inference <i>insulates</i> a search, but that inference alone is <i>not</i> a search. If we misunderstood the point, it was only in a good-faith effort to render the point germane to the case at hand. The issue in this case is not the police's allegedly unlawful inferencing, but their allegedly unlawful thermal-imaging measurement of the emanations from a house. We say such measurement is a search; the dissent says it is not, because an inference is not a search. We took that to mean that, since the technologically enhanced emanations had to be the basis of inferences before anything inside the house could be known, the use of the emanations could not be a search. But the dissent certainly knows better than we what it intends. And if it means only that an inference is not a search, we certainly agree. That has no bearing, however, upon whether hi-tech measurement of emanations from a house is a search.</p>
<p>[5]  The Government cites our statement in <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986), noting apparent agreement with the State of California that aerial surveillance of a house's curtilage could become "`invasive' " if "`modern technology' " revealed "`those intimate associations, objects or activities otherwise imperceptible to police or fellow citizens.' " <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Id.,</i> at 215</a></span>, n.3 (quoting Brief for State of California 14-15). We think the Court's focus in this secondhand dictum was not upon intimacy but upon otherwise-imperceptibility, which is precisely the principle we vindicate today.</p>
<p>[6]  The dissent argues that we have injected potential uncertainty into the constitutional analysis by noting that whether or not the technology is in general public use may be a factor. See <i>post,</i> at 47. That quarrel, however, is not with us but with this Court's precedent. See <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#215" aria-description="Citation for case: California v. Ciraolo"><i>Ciraolo, supra,</i> at 215</a></span> ("In an age where private and commercial flight in the public airways is routine, it is unreasonable for respondent to expect that his marijuana plants were constitutionally protected from being observed with the naked eye from an altitude of 1,000 feet"). Given that we can quite confidently say that thermal imaging is not "routine," we decline in this case to reexamine that factor.</p>
<p>[1]  After an evidentiary hearing, the District Court found: "[T]he use of the thermal imaging device here was not an intrusion into Kyllo's home. No intimate details of the home were observed, and there was no intrusion upon the privacy of the individuals within the home. The device used cannot penetrate walls or windows to reveal conversations or human activities. The device recorded only the heat being emitted from the home." Supp. App. to Pet. for Cert. 40.</p>
<p>[2]  Thus, for example, we have found consistent with the Fourth Amendment, even absent a warrant, the search and seizure of garbage left for collection outside the curtilage of a home, <i>California</i> v. <i>Greenwood,</i> <span class="citation" data-id="9431296"><a href="/opinion/112067/california-v-greenwood/" aria-description="Citation for case: California v. Greenwood">486 U. S. 35</a></span> (1988); the aerial surveillance of a fenced-in backyard from an altitude of 1,000 feet, <i>California</i> v. <i>Ciraolo,</i> <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U. S. 207</a></span> (1986); the aerial observation of a partially exposed interior of a residential greenhouse from 400 feet above, <i>Florida</i> v. <i>Riley,</i> <span class="citation" data-id="9431518"><a href="/opinion/112175/florida-v-riley/" aria-description="Citation for case: Florida v. Riley">488 U. S. 445</a></span> (1989); the aerial photography of an industrial complex from several thousand feet above, <i>Dow Chemical Co.</i> v. <i>United States,</i> <span class="citation" data-id="9430504"><a href="/opinion/111667/dow-chemical-co-v-united-states-ex-rel-administrator/" aria-description="Citation for case: Dow Chemical Co. v. United States Ex Rel. Administrator">476 U. S. 227</a></span> (1986); and the observation of smoke emanating from chimney stacks, <i>Air Pollution Variance Bd. of Colo.</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861</a></span> (1974).</p>
<p>[3]  Although the Court credits us with the "novel proposition that inference insulates a search," <i>ante,</i> at 36, our point simply is that an inference cannot <i>be</i> a search, contrary to the Court's reasoning. See <i>supra</i>  this page. Thus, the Court's use of <i>United States</i> v. <i>Karo,</i> <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">468 U. S. 705</a></span> (1984), to refute a point we do not make underscores the fact that the Court has no real answer (either in logic or in law) to the point we do make. Of course, <i><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/" aria-description="Citation for case: United States v. Karo">Karo</a></span></i> itself does not provide any support for the Court's view that inferences can amount to unconstitutional searches. The illegality in that case was "the monitoring of a beeper in a private residence" to obtain information that "could not have [been] obtained by observation from outside," <span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#714" aria-description="Citation for case: United States v. Karo"><i>id.,</i> at 714-715</a></span>, rather than any thought processes that flowed from such monitoring.</p>
<p>[4]  This view comports with that of all the Courts of Appeals that have resolved the issue. See <span class="citation" data-id="9492483"><a href="/opinion/766078/united-states-v-danny-lee-kyllo/" aria-description="Citation for case: United States v. Danny Lee Kyllo">190 F. 3d 1041</a></span> (CA9 1999); <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9488415"><a href="/opinion/701846/united-states-v-theodore-robinson-sr/" aria-description="Citation for case: United States v. Theodore Robinson, Sr.">62 F. 3d 1325</a></span> (CA11 1995) (upholding warrantless use of thermal imager); <i>United States</i> v. <i>Myers,</i> <span class="citation" data-id="687649"><a href="/opinion/687649/united-states-v-dale-e-myers/" aria-description="Citation for case: United States v. Dale E. Myers">46 F. 3d 668</a></span> (CA7 1995) (same); <i>United States</i> v. <i>Ishmael,</i> <span class="citation" data-id="690298"><a href="/opinion/690298/united-states-v-rohn-martin-ishmael-and-debra-k-ishmael/" aria-description="Citation for case: United States v. Rohn Martin Ishmael and Debra K. Ishmael">48 F. 3d 850</a></span> (CA5 1995) (same); <i>United States</i> v. <i>Pinson,</i>  <span class="citation" data-id="670592"><a href="/opinion/670592/united-states-v-joseph-pinson/" aria-description="Citation for case: United States v. Joseph Pinson">24 F. 3d 1056</a></span> (CA8 1994) (same). But see <i>United States</i> v. <i>Cusumano,</i>  <span class="citation" data-id="9488608"><a href="/opinion/706029/united-states-v-christopher-paul-cusumano-united-states-of-america-v/" aria-description="Citation for case: United States v. Christopher Paul Cusumano, United States...">67 F. 3d 1497</a></span> (CA10 1995) (warrantless use of thermal imager violated Fourth Amendment), vacated and decided on other grounds, <span class="citation" data-id="9489149"><a href="/opinion/718297/united-states-v-christopher-paul-cusumano-united-states-of-america-v/" aria-description="Citation for case: United States v. Christopher Paul Cusumano, United States...">83 F. 3d 1247</a></span> (CA10 1996) (en banc).</p>
<p>[5]  The record describes a device that numbers close to a thousand manufactured units; that has a predecessor numbering in the neighborhood of 4,000 to 5,000 units; that competes with a similar product numbering from 5,000 to 6,000 units; and that is "readily available to the public" for commercial, personal, or law enforcement purposes, and is just an 800number away from being rented from "half a dozen national companies" by anyone who wants one. App. 18. Since, by virtue of the Court's new rule, the issue is one of first impression, perhaps it should order an evidentiary hearing to determine whether these facts suffice to establish "general public use."</p>
<p>[6]  The use of the latter device would be constitutional given <i>Smith</i> v. <i><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">Maryland</a></span>,</i> 442 U. S.735, 741 (1979),which upheld the use of pen registers to record numbers dialed on a phone because, unlike "the listening device employed in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> . .. pen registers do not acquire the <i>contents</i>  of communications."</p>

</div>
```

---

## GROUP: content/cases/Los Angeles County v. Rettele.md  (`case`, 7 assertions)

### content_page

```
---
title: "Los Angeles County v. Rettele"
type: case
citation: ""
parallel_cite: "550 U.S. 609; 127 S. Ct. 1989; 167 L. Ed. 2d 974; 75 U.S.L.W. 3619; 20 Fla. L. Weekly Fed. S 281"
neutral_cite: 2007 U.S. LEXIS 5900
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2007
date_decided: 2007-05-21
docket: 06-605
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2007-05-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Los Angeles County v. Rettele
  varies_by_point: false
  scope_note: "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command — including ordering them, unclothed, out of bed for a few minutes — to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145728/los-angeles-county-california-v-rettele/"
  cluster_id: 145728
  opinion_id: 145728
  identity_checked: true
homes:
  - page: "[[Detention and Search of Persons at the Scene]]"
    role: "Key — Progeny"
  - page: "[[Securing the Scene]]"
    role: "Related (scene-securing overlap)"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Summers]]", "[[Muehler v. Mena]]", "[[Bailey v. United States]]"]
aliases: ["Los Angeles County, California v. Rettele"]
tags: ["case", "fourth-amendment", "securing-the-scene", "warrant-execution", "detention", "qualified-immunity"]
holding: "Officers executing a valid search warrant may briefly detain the occupants and exercise unquestioned command of the situation to protect themselves — including ordering unclothed occupants out of bed for a few minutes while securing the room — without violating the Fourth Amendment, provided the detention is not prolonged."
lake:
  record_id: Los Angeles County v. Rettele
  status: verified
  projected_at: 2026-07-06
---

# Los Angeles County v. Rettele

*550 U.S. 609 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Sheriff's deputies obtained a valid warrant to search a house in a fraud/identity-theft investigation; the suspects were African-American and one was believed to own a handgun. Unknown to the deputies, the house had recently been sold to Rettele and Sadler, who were white. Executing the warrant in the early morning, deputies entered the bedroom and ordered Rettele and Sadler — naked in bed — to get up and stand, holding them at gunpoint for a couple of minutes while securing the room before letting them dress. Realizing the suspects were not there, the deputies left within 15 minutes. The Retteles sued under § 1983.

## Issue
Do deputies executing a valid search warrant violate the Fourth Amendment by briefly detaining the home's occupants at gunpoint — including ordering them, unclothed, out of bed — while securing the residence?

## Rule
No. "The deputies needed a moment to secure the room and ensure that other persons were not close by or did not present a danger," and "[d]eputies were not required to turn their backs to allow Rettele and Sadler to retrieve clothing or to cover themselves with the sheets[;] [r]ather, '[t]he risk of harm to both the police and the occupants is minimized if the officers routinely exercise unquestioned command of the situation.'" — 127 S. Ct. at 1993 (quoting *Michigan v. Summers*). ^pin-1993

The detention may not be prolonged beyond necessity, but here there was "no accusation that the detention . . . was prolonged[;] [t]he deputies left the home less than 15 minutes after arriving." — *Id.* ^pin-1993b

The governing principle: "When officers execute a valid warrant and act in a reasonable manner to protect themselves from harm . . . , the Fourth Amendment is not violated." — *Id.* at 1993–94. ^pin-1994

And because "respondents' constitutional rights were not violated, 'there is no necessity for further inquiries concerning qualified immunity.'" — *Id.* at 1994. ^pin-1994b

## Application
The deputies reasonably believed armed suspects might be inside, so ordering the occupants out of bed and briefly holding them while securing the room was a reasonable safety measure. That the occupants turned out to be innocent, of a different race than the suspects, and unclothed did not make the brief detention unreasonable: valid warrants issue on probable cause, not certainty, and innocent residents sometimes bear the cost. The occupants were unclothed for only about two minutes and the whole episode lasted under 15 minutes — far shorter and less restrictive than the two-to-three-hour handcuff detention upheld in *[[Muehler v. Mena]]*. No constitutional violation occurred.

## Conclusion
The deputies' conduct in executing the valid warrant did not violate the Fourth Amendment; the judgment of the Ninth Circuit was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. (Justice Stevens, joined by Justice Ginsburg, would have reversed solely on qualified-immunity grounds.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Rettele* remains controlling on the authority to detain occupants and secure the scene while executing a warrant, applying [[Michigan v. Summers]] and situating the intrusion below the detention upheld in [[Muehler v. Mena]]. The scope of *[[Michigan v. Summers|Summers]]* detention authority was later cabined geographically in [[Bailey v. United States]]. No negative treatment.

## Appears on
- [[Securing the Scene]] — *Progeny*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Los Angeles County v. Rettele*, 550 U.S. 609 (2007) (per curiam) — https://www.courtlistener.com/opinion/145728/los-angeles-county-california-v-rettele/ — pinpoints (S. Ct. reporter, per CL copy): 1993, 1994.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "066ba0a5b78eb80d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2007 U.S. LEXIS 5900", "official_citation_present": false, "parallel_cite": "550 U.S. 609; 127 S. Ct. 1989; 167 L. Ed. 2d 974; 75 U.S.L.W. 3619; 20 Fla. L. Weekly Fed. S 281", "title": "Los Angeles County v. Rettele", "year": "2007"}}
{"assertion_id": "01dc3b154a8c745d", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Related (cross-doctrine)", "title": "Los Angeles County v. Rettele"}}
{"assertion_id": "3ad0bfa19efe6f52", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers executing a valid search warrant may briefly detain the occupants and exercise unquestioned command of the situation to protect themselves — including ordering unclothed occupants out of bed for a few minutes while securing the room — without violating the Fourth Amendment, provided the detention is not prolonged.", "title": "Los Angeles County v. Rettele"}}
{"assertion_id": "ddd30d4abfc2c429", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (scene-securing overlap)", "title": "Los Angeles County v. Rettele"}}
{"assertion_id": "dfb0a4f1216e8289", "dimension": "support", "kind": "home_role", "locator": {"home": "Detention and Search of Persons at the Scene"}, "payload": {"home": "Detention and Search of Persons at the Scene", "role": "Key — Progeny", "title": "Los Angeles County v. Rettele"}}
{"assertion_id": "530fc4954715c07d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Los Angeles County v. Rettele"}}
{"assertion_id": "dc25ee725e5d472e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2007-05-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Los Angeles County v. Rettele", "field_i_validity": "good_law", "scope_note": "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command — including ordering them, unclothed, out of bed for a few minutes — to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged.", "title": "Los Angeles County v. Rettele", "varies_by_point": "false"}}
```

### lake record — Los Angeles County v. Rettele

```json
{
  "schema_version": "s2.v1",
  "record_id": "Los Angeles County v. Rettele",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Los Angeles County, California v. Rettele",
    "case_name_short": "Rettele",
    "case_name_full": "LOS ANGELES COUNTY, CALIFORNIA, Et Al. v. RETTELE Et Al.",
    "input_case_name": "Los Angeles County v. Rettele",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-05-21",
    "year": 2007,
    "docket": "06-605",
    "cluster_id": 145728,
    "lead_opinion_id": 145728,
    "sibling_ids": [
      145728,
      9435063,
      9435064
    ],
    "absolute_url": "/opinion/145728/los-angeles-county-california-v-rettele/",
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
        "cite": "550 U.S. 609",
        "volume": "550",
        "reporter": "U.S.",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 1989",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 974",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "974",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 U.S.L.W. 3619",
        "volume": "75",
        "reporter": "U.S.L.W.",
        "page": "3619",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 Fla. L. Weekly Fed. S 281",
        "volume": "20",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2007 U.S. LEXIS 5900",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "5900",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "550 U.S. 609",
        "volume": "550",
        "reporter": "U.S.",
        "page": "609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 1989",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "1989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "167 L. Ed. 2d 974",
        "volume": "167",
        "reporter": "L. Ed. 2d",
        "page": "974",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2007 U.S. LEXIS 5900",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "5900",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "75 U.S.L.W. 3619",
        "volume": "75",
        "reporter": "U.S.L.W.",
        "page": "3619",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 Fla. L. Weekly Fed. S 281",
        "volume": "20",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "281",
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
      "id": "pin-1993",
      "page": null,
      "quote": "--- # Los Angeles County v. Rettele *550 U.S. 609 (2007)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Sheriff's deputies obtained a valid warrant to search a house in a fraud/identity-theft investigation; the suspects were African-American and one was believed to own a handgun. Unknown to the deputies, the house had recently been sold to Rettele and Sadler, who were white. Executing the warrant in the early morning, deputies entered the bedroom and ordered Rettele and Sadler \u2014 naked in bed \u2014 to get up and stand, holding them at gunpoint for a couple of minutes while securing the room before letting them dress. Realizing the suspects were not there, the deputies left within 15 minutes. The Retteles sued under \u00a7 1983. ## Issue Do deputies executing a valid search warrant violate the Fourth Amendment by briefly detaining the home's occupants at gunpoint \u2014 including ordering them, unclothed, out of bed \u2014 while securing the residence? ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1993b",
      "page": null,
      "quote": "no accusation that the detention . . . was prolonged[;] [t]he deputies left the home less than 15 minutes after arriving.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1994",
      "page": null,
      "quote": "When officers execute a valid warrant and act in a reasonable manner to protect themselves from harm . . . , the Fourth Amendment is not violated.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1994b",
      "page": null,
      "quote": "respondents' constitutional rights were not violated, 'there is no necessity for further inquiries concerning qualified immunity.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2007-05-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Los Angeles County v. Rettele",
    "varies_by_point": false,
    "scope_note": "Controlling: officers executing a valid warrant may briefly detain occupants and exercise unquestioned command \u2014 including ordering them, unclothed, out of bed for a few minutes \u2014 to secure the scene without violating the Fourth Amendment, so long as the detention is not prolonged.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curley v. Klem",
          "cluster_id": 1362944,
          "cite": [
            "499 F.3d 199",
            "2007 U.S. App. LEXIS 20213",
            "2007 WL 2404803"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Elgin",
          "cluster_id": 1456587,
          "cite": [
            "578 F.3d 526",
            "2009 U.S. App. LEXIS 18724",
            "2009 WL 2525565"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Thompson",
          "cluster_id": 2056760,
          "cite": [
            "985 A.2d 928",
            "604 Pa. 198",
            "2009 Pa. LEXIS 2793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weigel v. Broad",
          "cluster_id": 171335,
          "cite": [
            "544 F.3d 1143",
            "2008 U.S. App. LEXIS 21877",
            "2008 WL 4631920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baird v. Renbarger",
          "cluster_id": 1188789,
          "cite": [
            "576 F.3d 340",
            "2009 U.S. App. LEXIS 17215",
            "2009 WL 2357882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colbruno v. Kessler",
          "cluster_id": 4636000,
          "cite": [
            "928 F.3d 1155"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mlodzinski Ex Rel. J.M. v. Lewis",
          "cluster_id": 2451581,
          "cite": [
            "648 F.3d 24",
            "2011 U.S. App. LEXIS 11117",
            "2011 WL 2150741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ganias",
          "cluster_id": 3207604,
          "cite": [
            "824 F.3d 199",
            "117 A.F.T.R.2d (RIA) 1841",
            "2016 U.S. App. LEXIS 9706",
            "2016 WL 3031285"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jennings",
          "cluster_id": 1313899,
          "cite": [
            "544 F.3d 815",
            "2008 U.S. App. LEXIS 19560",
            "2008 WL 4192887"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennifer Cox v. Evansville Police Department and The City of Evansville Babi Beyer v. The City of Fort Wayne",
          "cluster_id": 4534961,
          "cite": [
            "107 N.E.3d 453"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Norris",
          "cluster_id": 216168,
          "cite": [
            "640 F.3d 295",
            "2011 U.S. App. LEXIS 9222",
            "2011 WL 1675801"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Z. J. v. Kansas City Brd of Police Comm",
          "cluster_id": 4642838,
          "cite": [
            "931 F.3d 672"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brian Lawrence",
          "cluster_id": 2805131,
          "cite": [
            "788 F.3d 234",
            "2015 U.S. App. LEXIS 9160",
            "2015 WL 3463089"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Erin Osmon v. United States",
          "cluster_id": 9392722,
          "cite": [
            "66 F.4th 144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Yanez-Marquez v. Loretta Lynch",
          "cluster_id": 2808824,
          "cite": [
            "789 F.3d 434",
            "2015 U.S. App. LEXIS 10107",
            "2015 WL 3719105"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kennedy v. State",
          "cluster_id": 2546934,
          "cite": [
            "338 S.W.3d 84",
            "2011 Tex. App. LEXIS 1755",
            "2011 WL 832122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Siciliano",
          "cluster_id": 203974,
          "cite": [
            "578 F.3d 61",
            "2009 U.S. App. LEXIS 19121",
            "2009 WL 2605704"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bancroft v. City of Mount Vernon",
          "cluster_id": 2308267,
          "cite": [
            "672 F. Supp. 2d 391",
            "2009 U.S. Dist. LEXIS 112652",
            "2009 WL 4277268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez v. Canales",
          "cluster_id": 1359367,
          "cite": [
            "574 F.3d 1169",
            "2009 D.A.R. 11",
            "2009 U.S. App. LEXIS 16897"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jennen",
          "cluster_id": 1303041,
          "cite": [
            "596 F.3d 594",
            "2010 U.S. App. LEXIS 3784",
            "2010 WL 625041"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rush v. City of Mansfield",
          "cluster_id": 2474513,
          "cite": [
            "771 F. Supp. 2d 827",
            "2011 U.S. Dist. LEXIS 13689",
            "2011 WL 609802"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Cortes",
          "cluster_id": 1470540,
          "cite": [
            "566 F.3d 767",
            "2009 U.S. App. LEXIS 11656",
            "2009 WL 1424106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Los Angeles County v. Rettele:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145728 OR 9435063 OR 9435064) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 59,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 59,
        "triage_read": 3,
        "triage_snippet_classified": 56
      },
      "lane2_top_cited": {
        "query": "cites:(145728 OR 9435063 OR 9435064)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9MTczNDc3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145728+OR+9435063+OR+9435064%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145728 OR 9435063 OR 9435064)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145728 OR 9435063 OR 9435064)",
    "indexed_citing_opinions": 91,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145728,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9435063,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9435064,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 229,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/los-angeles-county-v-rettele.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYyNTk3NDUmcz00NjA5ODM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145728+OR+9435063+OR+9435064%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145728,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 675827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 726621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 781793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 782720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145728,
        "cited_id": 1654997,
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
    "date_created": "2026-07-05T11:01:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:05:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:01:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Los Angeles County v. Rettele

```
                 Cite as: 550 U. S. ____ (2007)          1

                            Per Curiam

SUPREME COURT OF THE UNITED STATES
   LOS ANGELES COUNTY, CALIFORNIA, ET AL. v. 

             MAX RETTELE ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

              No. 06–605.    Decided May 21, 2007 


  PER CURIAM.
  Deputies of the Los Angeles County Sheriff’s Depart
ment obtained a valid warrant to search a house, but they
were unaware that the suspects being sought had moved
out three months earlier. When the deputies searched the
house, they found in a bedroom two residents who were of
a different race than the suspects. The deputies ordered
these innocent residents, who had been sleeping un
clothed, out of bed. The deputies required them to stand
for a few minutes before allowing them to dress.
  The residents brought suit under Rev. Stat. §1979, 42
U. S. C. §1983, naming the deputies and other parties and
accusing them of violating the Fourth Amendment right to
be free from unreasonable searches and seizures. The
District Court granted summary judgment to all named
defendants. The Court of Appeals for the Ninth Circuit
reversed, concluding both that the deputies violated the
Fourth Amendment and that they were not entitled to
qualified immunity because a reasonable deputy would
have stopped the search upon discovering that respon
dents were of a different race than the suspects and be
cause a reasonable deputy would not have ordered respon
dents from their bed. We grant the petition for certiorari
and reverse the judgment of the Court of Appeals by this
summary disposition.
                         I
  From September to December 2001, Los Angeles County
2            LOS ANGELES COUNTY v. RETTELE

                        Per Curiam

Sheriff’s Department Deputy Dennis Watters investigated
a fraud and identity-theft crime ring. There were four
suspects of the investigation. One had registered a 9
millimeter Glock handgun. The four suspects were known
to be African-Americans.
   On December 11, Watters obtained a search warrant for
two houses in Lancaster, California, where he believed he
could find the suspects. The warrant authorized him to
search the homes and three of the suspects for documents
and computer files. In support of the search warrant an
affidavit cited various sources showing the suspects re
sided at respondents’ home. The sources included De
partment of Motor Vehicles reports, mailing address list
ings, an outstanding warrant, and an Internet telephone
directory. In this Court respondents do not dispute the
validity of the warrant or the means by which it was
obtained.
   What Watters did not know was that one of the houses
(the first to be searched) had been sold in September to a
Max Rettele. He had purchased the home and moved into
it three months earlier with his girlfriend Judy Sadler and
Sadler’s 17-year-old son Chase Hall. All three, respon
dents here, are Caucasians.
   On the morning of December 19, Watters briefed six
other deputies in preparation for the search of the houses.
Watters informed them they would be searching for three
African-American suspects, one of whom owned a regis
tered handgun. The possibility a suspect would be armed
caused the deputies concern for their own safety. Watters
had not obtained special permission for a night search, so
he could not execute the warrant until 7 a.m. See Cal.
Penal Code Ann. §1533 (West 2000). Around 7:15 Watters
and six other deputies knocked on the door and announced
their presence. Chase Hall answered. The deputies en
tered the house after ordering Hall to lie face down on the
ground.
                 Cite as: 550 U. S. ____ (2007)           3

                          Per Curiam

   The deputies’ announcement awoke Rettele and Sadler.
The deputies entered their bedroom with guns drawn and
ordered them to get out of their bed and to show their
hands. They protested that they were not wearing clothes.
Rettele stood up and attempted to put on a pair of sweat
pants, but deputies told him not to move. Sadler also
stood up and attempted, without success, to cover herself
with a sheet. Rettele and Sadler were held at gunpoint for
one to two minutes before Rettele was allowed to retrieve
a robe for Sadler. He was then permitted to dress. Rettele
and Sadler left the bedroom within three to four minutes
to sit on the couch in the living room.
   By that time the deputies realized they had made a
mistake. They apologized to Rettele and Sadler, thanked
them for not becoming upset, and left within five minutes.
They proceeded to the other house the warrant authorized
them to search, where they found three suspects. Those
suspects were arrested and convicted.
   Rettele and Sadler, individually and as guardians ad
litem for Hall, filed this §1983 suit against Los Angeles
County, the Los Angeles County Sheriff’s Department,
Deputy Watters, and other members of the sheriff’s de
partment. Respondents alleged petitioners violated their
Fourth Amendment rights by obtaining a warrant in
reckless fashion and conducting an unreasonable search
and detention. The District Court held that the warrant
was obtained by proper procedures and the search was
reasonable. It concluded in the alternative that any
Fourth Amendment rights the deputies violated were not
clearly established and that, as a result, the deputies were
entitled to qualified immunity.
   On appeal respondents did not challenge the validity of
the warrant; they did argue that the deputies had con
ducted the search in an unreasonable manner. A divided
panel of the Court of Appeals for the Ninth Circuit re
versed in an unpublished opinion. 186 Fed. Appx. 765
4           LOS ANGELES COUNTY v. RETTELE

                        Per Curiam

(2006). The majority held that
    “because (1) no African-Americans lived in [respon
    dents’] home; (2) [respondents], a Caucasian couple,
    purchased the residence several months before the
    search and the deputies did not conduct an ownership
    inquiry; (3) the African-American suspects were not
    accused of a crime that required an emergency search;
    and (4) [respondents] were ordered out of bed naked
    and held at gunpoint while the deputies searched
    their bedroom for the suspects and a gun, we find that
    a reasonable jury could conclude that the search and
    detention were ‘unnecessarily painful, degrading, or
    prolonged,’ and involved ‘an undue invasion of pri
    vacy,’ Franklin v. Foxworth, 31 F. 3d 873, 876 (9th
    Cir. 1994).” Id., at 766.
Turning to whether respondents’ Fourth Amendment
rights were clearly established, the majority held that a
reasonable deputy should have known the search and
detention were unlawful.
  Judge Cowen dissented. In his view the deputies had
authority to detain respondents for the duration of the
search and were justified in ordering respondents from
their bed because weapons could have been concealed
under the bedcovers. He also concluded that, assuming
a constitutional violation, the law was not clearly
established.
  The Court of Appeals denied rehearing and rehearing en
banc.
                             II
  Because respondents were of a different race than the
suspects the deputies were seeking, the Court of Appeals
held that “[a]fter taking one look at [respondents], the
deputies should have realized that [respondents] were not
the subjects of the search warrant and did not pose a
threat to the deputies’ safety.” Ibid. We need not pause
                 Cite as: 550 U. S. ____ (2007)            5

                          Per Curiam

long in rejecting this unsound proposition. When the
deputies ordered respondents from their bed, they had no
way of knowing whether the African-American suspects
were elsewhere in the house. The presence of some Cau
casians in the residence did not eliminate the possibility
that the suspects lived there as well. As the deputies
stated in their affidavits, it is not uncommon in our society
for people of different races to live together. Just as peo
ple of different races live and work together, so too might
they engage in joint criminal activity. The deputies, who
were searching a house where they believed a suspect
might be armed, possessed authority to secure the prem
ises before deciding whether to continue with the search.
  In Michigan v. Summers, 452 U. S. 692 (1981), this
Court held that officers executing a search warrant for
contraband may “detain the occupants of the premises
while a proper search is conducted.” Id., at 705. In weigh
ing whether the search in Summers was reasonable the
Court first found that “detention represents only an in
cremental intrusion on personal liberty when the search of
a home has been authorized by a valid warrant.” Id., at
703. Against that interest, it balanced “preventing flight
in the event that incriminating evidence is found”; “mini
mizing the risk of harm to the officers”; and facilitating
“the orderly completion of the search.” Id., at 702–703; see
Muehler v. Mena, 544 U. S. 93 (2005).
  In executing a search warrant officers may take reason
able action to secure the premises and to ensure their own
safety and the efficacy of the search. Id., at 98–100; see
also id., at 103 (KENNEDY, J., concurring); Summers,
supra, at 704–705. The test of reasonableness under the
Fourth Amendment is an objective one. Graham v. Con
nor, 490 U. S. 386, 397 (1989) (addressing the reasonable
ness of a seizure of the person). Unreasonable actions
include the use of excessive force or restraints that cause
unnecessary pain or are imposed for a prolonged and
6            LOS ANGELES COUNTY v. RETTELE

                         Per Curiam

unnecessary period of time. Mena, supra, at 100; Graham,
supra, at 396–399.
   The orders by the police to the occupants, in the context
of this lawful search, were permissible, and perhaps nec
essary, to protect the safety of the deputies. Blankets and
bedding can conceal a weapon, and one of the suspects was
known to own a firearm, factors which underscore this
point. The Constitution does not require an officer to
ignore the possibility that an armed suspect may sleep
with a weapon within reach. The reports are replete with
accounts of suspects sleeping close to weapons. See
United States v. Enslin, 327 F. 3d 788, 791 (CA9 2003)
(“When [the suspect] put his hands in the air and began to
sit up, his movement shifted the covers and the marshals
could see a gun in the bed next to him”); see also United
States v. Jones, 336 F. 3d 245, 248 (CA3 2003) (suspect
kept a 9-millimeter Luger under his pillow while he slept);
United States v. Hightower, 96 F. 3d 211 (CA7 1996) (sus
pect kept a loaded five-shot handgun under his pillow);
State v. Willis, 36,759–KA, p. 3 (La. App. 4/9/03), 843
So. 2d 592, 595 (officers “pulled back the bed covers and
found a .38 caliber Model 10 Smith and Wesson revolver
located near where defendant’s left hand had been”); State
v. Kypreos, 115 Wash. App. 207, 61 P. 3d 352 (2002) (sus
pect kept a handgun in the bed).
   The deputies needed a moment to secure the room and
ensure that other persons were not close by or did not
present a danger. Deputies were not required to turn
their backs to allow Rettele and Sadler to retrieve clothing
or to cover themselves with the sheets. Rather, “[t]he risk
of harm to both the police and the occupants is minimized
if the officers routinely exercise unquestioned command of
the situation.” Summers, 452 U. S., at 702–703.
   This is not to say, of course, that the deputies were free
to force Rettele and Sadler to remain motionless and
standing for any longer than necessary. We have recog
                 Cite as: 550 U. S. ____ (2007)            7

                          Per Curiam

nized that “special circumstances, or possibly a prolonged
detention” might render a search unreasonable. See id.,
at 705, n. 21. There is no accusation that the detention
here was prolonged. The deputies left the home less than
15 minutes after arriving. The detention was shorter and
less restrictive than the 2- to 3-hour handcuff detention
upheld in Mena. See 544 U. S., at 100. And there is no
allegation that the deputies prevented Sadler and Rettele
from dressing longer than necessary to protect their
safety. Sadler was unclothed for no more than two min
utes, and Rettele for only slightly more time than that.
Sadler testified that once the police were satisfied that no
immediate threat was presented, “they wanted us to get
dressed and they were pressing us really fast to hurry up
and get some clothes on.” Deposition of Judy Lorraine
Sadler in No. CV–0206262–RSWL (RNBX) (CD Cal., June
10, 2003), Doc. 26, Exh. 4, p. 55.
  The Fourth Amendment allows warrants to issue on
probable cause, a standard well short of absolute cer
tainty. Valid warrants will issue to search the innocent,
and people like Rettele and Sadler unfortunately bear the
cost. Officers executing search warrants on occasion enter
a house when residents are engaged in private activity;
and the resulting frustration, embarrassment, and hu
miliation may be real, as was true here. When officers
execute a valid warrant and act in a reasonable manner to
protect themselves from harm, however, the Fourth
Amendment is not violated.
  As respondents’ constitutional rights were not violated,
“there is no necessity for further inquiries concerning
qualified immunity.” Saucier v. Katz, 533 U. S. 194, 201
(2001). The judgment of the Court of Appeals is reversed,
and the case is remanded for further proceedings consis
tent with this opinion.
                                            It is so ordered.
  JUSTICE SOUTER would deny the petition for a writ of
certiorari.
                      Cite as: 550 U. S. ____ (2007)                     1

                  STEVENS, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
    LOS ANGELES COUNTY, CALIFORNIA, ET AL. v. 

              MAX RETTELE ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

                  No. 06–605.    Decided May 21, 2007 


   JUSTICE STEVENS, with whom JUSTICE GINSBURG joins,
concurring in the judgment.
   This case presents two separate questions: (1) whether
the four circumstances identified in the Court of Appeals’
unpublished opinion established a genuine issue of mate
rial fact as to whether the seizure violated respondents’
Fourth Amendment rights, see ante, at 4; (2) whether the
officers were nevertheless entitled to qualified immunity
because the right was not clearly established. The fact
that the judges on the Court of Appeals disagreed on both
questions convinces me that they should not have an
nounced their decision in an unpublished opinion.
   In answering the first question, the Ninth Circuit major
ity relied primarily on Franklin v. Foxworth, 31 F. 3d 873
(CA9 1994). As Judge Cowen’s discussion of Franklin
demonstrates, that case surely does not clearly establish
the unconstitutionality of the officers’ conduct.* Conse
——————
   * See 186 Fed. Appx. 765, 767 (2006) (dissenting opinion) (“In Frank
lin v. Foxworth, 31 F.3d 873 (9th Cir. 1994), we found unconstitutional
the officers’ failure to provide clothing to a gravely ill man before
exposing his genitals to twenty-three strangers for over two hours,
under circumstances where there was no reason why the man was not
given clothing. Id. at 876–78. We concluded that the detention was
conducted in ‘a manner that wantonly and callously subjected an
obviously ill and incapacitated person to entirely unnecessary and
unjustifiable degradation and suffering.’ Id. at 878. Here, in contrast,
Plaintiffs were not gravely ill, and their brief exposure, which lasted, at
most, three or four minutes, was outweighed by the safety risks associ
ated with allowing two occupants to remain in bed under covers during
2               LOS ANGELES COUNTY v. RETTELE

                  STEVENS, J., concurring in judgment

quently, regardless of the proper answer to the constitu
tional question, the defendants were entitled to qualified
immunity. I would reverse on that ground and disavow
the unwise practice of deciding constitutional questions in
advance of the necessity for doing so. See County of Sac
ramento v. Lewis, 523 U. S. 833, 859 (1998) (STEVENS, J.,
concurring in judgment). Accordingly, I concur in the
Court’s judgment.




—————— 

execution of a search warrant”). 


```

---

## GROUP: content/cases/New York v. Class.md  (`case`, 7 assertions)

### content_page

```
---
title: "New York v. Class"
type: case
citation: "475 U.S. 106 (1986)"
parallel_cite: "106 S. Ct. 960; 89 L. Ed. 2d 81; 54 U.S.L.W. 4178"
neutral_cite: 1986 U.S. LEXIS 5
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-02-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1986-02-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New York v. Class
  varies_by_point: false
  scope_note: "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111600/new-york-v-class/"
  cluster_id: 111600
  opinion_id: 9430353
  identity_checked: true
homes:
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
  - page: "[[Plain View Doctrine]]"
    role: "Related (cross-doctrine)"
related: ["[[Pennsylvania v. Mimms]]", "[[Delaware v. Prouse]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "vehicle", "vin", "traffic-stop", "reasonable-expectation-of-privacy"]
holding: "There is no reasonable expectation of privacy in a VIN required by law to be visible; reaching into the car to move papers obscuring the VIN was a minimal but reasonable search."
lake:
  record_id: New York v. Class
  status: verified
  projected_at: 2026-07-09
---

# New York v. Class

*475 U.S. 106 (1986)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers stopped Class for two traffic violations. When Class exited the car, an officer reached into the passenger compartment to move papers on the dashboard that obscured the Vehicle Identification Number (VIN). In doing so he saw the handle of a gun protruding from under the seat. Class moved to suppress the gun, arguing the reach-in was an unconstitutional search.

## Issue
Whether an officer's entry into the passenger compartment of a lawfully stopped car to move papers obscuring the VIN — a number required by law to be visible — violates the Fourth Amendment.

## Rule
There is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the VIN itself: "because of the important role played by the VIN in the pervasive governmental regulation of the automobile and the efforts by the Federal Government to ensure that the VIN is placed in plain view, we hold that there was no reasonable expectation of privacy in the VIN." — 475 U.S. at 114. ^pin-114

The minimal intrusion to read it was reasonable: "We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations." — [*Id.* at 119](https://www.courtlistener.com/opinion/111600/new-york-v-class/#:~:text=We%20hold%20that%20this%20search). ^pin-119

## Application
The VIN is required by federal regulation to be visible from outside the car, so Class had no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in it, and placing papers over it did not create one. Although reaching into the passenger compartment was itself a minimal "search" of a space that retains some Fourth Amendment protection, it was reasonable here: the officers had observed two traffic violations, and had Class stayed in the car they could simply have asked him to move the papers. Because the intrusion was limited to the area where the VIN sits and was justified by the traffic violations, it was permissible — and the gun seen in the course of that lawful, minimal entry was admissible.

## Conclusion
Reading the obscured VIN by a brief reach into the car was a reasonable, minimal search; the gun was admissible. There is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a legally mandated, publicly visible VIN.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Builds on the diminished vehicle-privacy line ([[South Dakota v. Opperman]]) and the traffic-stop officer-safety/authority cases ([[Pennsylvania v. Mimms]], [[Delaware v. Prouse]]).

## Appears on
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*
- [[Traffic Stops]] — *Related (cross-doctrine)*
- [[Plain View Doctrine]] — *Related (cross-doctrine)*

## Sources
- *New York v. Class*, 475 U.S. 106 (1986) — https://www.courtlistener.com/opinion/111600/new-york-v-class/ — pinpoints: 114, 119.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "420d180d59a9ba41", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "475 U.S. 106 (1986)", "court": "U.S. Supreme Court", "neutral_cite": "1986 U.S. LEXIS 5", "official_citation_present": true, "parallel_cite": "106 S. Ct. 960; 89 L. Ed. 2d 81; 54 U.S.L.W. 4178", "title": "New York v. Class", "year": "1986"}}
{"assertion_id": "138c37299fcf2cd2", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Related (cross-doctrine)", "title": "New York v. Class"}}
{"assertion_id": "5a09c2d022acf73a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no reasonable expectation of privacy in a VIN required by law to be visible; reaching into the car to move papers obscuring the VIN was a minimal but reasonable search.", "title": "New York v. Class"}}
{"assertion_id": "7bc868313d9d5316", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Related (cross-doctrine)", "title": "New York v. Class"}}
{"assertion_id": "fe690e5ebcb795c1", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Expectation of Privacy"}, "payload": {"home": "Reasonable Expectation of Privacy", "role": "Related (cross-doctrine)", "title": "New York v. Class"}}
{"assertion_id": "883955d65ffe5a32", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1986-02-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "New York v. Class", "field_i_validity": "good_law", "scope_note": "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable.", "title": "New York v. Class", "varies_by_point": "false"}}
{"assertion_id": "ae5653d729f3a5c8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New York v. Class"}}
```

### lake record — New York v. Class

```json
{
  "schema_version": "s2.v1",
  "record_id": "New York v. Class",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New York v. Class",
    "case_name_short": "Class",
    "case_name_full": "New York v. Class",
    "input_case_name": "New York v. Class",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-02-25",
    "year": 1986,
    "docket": null,
    "cluster_id": 111600,
    "lead_opinion_id": 9430353,
    "sibling_ids": [
      111600,
      9430353,
      9430354,
      9430355,
      9430356
    ],
    "absolute_url": "/opinion/111600/new-york-v-class/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "475 U.S. 106",
      "volume": "475",
      "reporter": "U.S.",
      "page": "106",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 960",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "960",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 81",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "81",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4178",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4178",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 5",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "475 U.S. 106",
        "volume": "475",
        "reporter": "U.S.",
        "page": "106",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 960",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "960",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 2d 81",
        "volume": "89",
        "reporter": "L. Ed. 2d",
        "page": "81",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 5",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4178",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4178",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "475 U.S. 106",
    "official_selection": {
      "court_class": "scotus",
      "selected": "475 U.S. 106",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "--- # New York v. Class *475 U.S. 106 (1986)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers stopped Class for two traffic violations. When Class exited the car, an officer reached into the passenger compartment to move papers on the dashboard that obscured the Vehicle Identification Number (VIN). In doing so he saw the handle of a gun protruding from under the seat. Class moved to suppress the gun, arguing the reach-in was an unconstitutional search. ## Issue Whether an officer's entry into the passenger compartment of a lawfully stopped car to move papers obscuring the VIN \u2014 a number required by law to be visible \u2014 violates the Fourth Amendment. ## Rule There is no reasonable expectation of privacy in the VIN itself:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-119",
      "page": null,
      "quote": "We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations.",
      "star_marker": "119",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33755,
      "fragment": "#:~:text=We%20hold%20that%20this%20search",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1986-02-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New York v. Class",
    "varies_by_point": false,
    "scope_note": "Good law; no reasonable expectation of privacy in a VIN required by law to be visible, and a minimal intrusion to read it during a lawful traffic stop is reasonable.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. McCarthy",
          "cluster_id": 4746120,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
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
        "journal_ref": "New York v. Class:lane1_negative"
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
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Werra",
          "cluster_id": 212993,
          "cite": [
            "638 F.3d 326",
            "2011 U.S. App. LEXIS 5741",
            "2011 WL 982384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 3064806,
          "cite": [
            "580 F.3d 847",
            "2009 WL 2857199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Friedman v. Boucher",
          "cluster_id": 1459727,
          "cite": [
            "568 F.3d 1119",
            "2009 U.S. App. LEXIS 13440",
            "2009 WL 1758366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed, 23221 (6-27-2007)",
          "cluster_id": 4002592,
          "cite": [
            "2007 Ohio 3243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 5828324,
          "cite": [
            "17 A.D.3d 166",
            "793 N.Y.S.2d 353",
            "2005 N.Y. App. Div. LEXIS 3731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Alvarez",
          "cluster_id": 6231565,
          "cite": [
            "308 A.D.2d 184",
            "764 N.Y.S.2d 42",
            "2003 N.Y. App. Div. LEXIS 9160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Condon v. Reno",
          "cluster_id": 2967145,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. DeLaCruz",
          "cluster_id": 6151173,
          "cite": [
            "242 A.D.2d 410",
            "662 N.Y.S.2d 300",
            "1997 N.Y. App. Div. LEXIS 8505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Jeffrey Howard VAN POYCK, Defendant-Appellant",
          "cluster_id": 713090,
          "cite": [
            "77 F.3d 285",
            "96 Cal. Daily Op. Serv. 1091",
            "96 Daily Journal DAR 1850",
            "1996 U.S. App. LEXIS 2518",
            "1996 WL 69841"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. State",
          "cluster_id": 1713874,
          "cite": [
            "906 S.W.2d 620",
            "1995 WL 515837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lidster",
          "cluster_id": 131154,
          "cite": [
            "157 L. Ed. 2d 843",
            "124 S. Ct. 885",
            "540 U.S. 419",
            "2004 U.S. LEXIS 656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Venham",
          "cluster_id": 3973805,
          "cite": [
            "645 N.E.2d 831",
            "96 Ohio App. 3d 649",
            "1994 Ohio App. LEXIS 4118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis Dayton Holt",
          "cluster_id": 774866,
          "cite": [
            "264 F.3d 1215",
            "2001 Colo. J. C.A.R. 4452",
            "2001 U.S. App. LEXIS 19759",
            "2001 WL 1013251"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terry King and Valerie Jean Burdex",
          "cluster_id": 604813,
          "cite": [
            "990 F.2d 1552",
            "1993 U.S. App. LEXIS 6056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jacoby, T., Aplt.",
          "cluster_id": 4429713,
          "cite": [
            "170 A.3d 1065"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
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
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spencer Ray Tilmon",
          "cluster_id": 666028,
          "cite": [
            "19 F.3d 1221",
            "1994 U.S. App. LEXIS 5598",
            "1994 WL 93939"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Torres",
          "cluster_id": 5689682,
          "cite": [
            "74 N.Y.2d 224",
            "544 N.Y.S.2d 796",
            "543 N.E.2d 61",
            "1989 N.Y. LEXIS 886"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. MacOn",
          "cluster_id": 1681383,
          "cite": [
            "957 So. 2d 1280",
            "2007 WL 1575004"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 5689813,
          "cite": [
            "74 N.Y.2d 773",
            "545 N.Y.S.2d 90",
            "543 N.E.2d 733",
            "1989 N.Y. LEXIS 882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio Civil Service Employees Association v. Richard P. Seiter",
          "cluster_id": 512622,
          "cite": [
            "858 F.2d 1171",
            "3 I.E.R. Cas. (BNA) 1623",
            "1988 U.S. App. LEXIS 13585",
            "1988 WL 100808"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1175765,
          "cite": [
            "721 P.2d 1357",
            "301 Or. 268",
            "1986 Ore. LEXIS 1453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stroud",
          "cluster_id": 1390081,
          "cite": [
            "720 P.2d 436",
            "106 Wash. 2d 144",
            "1986 Wash. LEXIS 1204"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New York v. Class:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTIzNzQ0MDAwMDAmcz02ODcyMjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjAmcz0yOTY4Nzg4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111600 OR 9430353 OR 9430354 OR 9430355 OR 9430356)",
    "indexed_citing_opinions": 433,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111600,
        "count": 374,
        "count_source": "search"
      },
      {
        "opinion_id": 9430353,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9430354,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430355,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430356,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 729,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-york-v-class.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcyNTc2NSZzPTQ4ODQwNDgmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111600+OR+9430353+OR+9430354+OR+9430355+OR+9430356%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111600,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111600,
        "cited_id": 2566781,
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
    "date_created": "2026-07-05T15:38:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:43:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New York v. Class

```
<opinion type="majority">
<author id="b189-10">Justice O’Connor</author>
<p id="A09">delivered the opinion of the Court.</p>
<p id="b189-11">In this case, we must decide whether, in order to observe a Vehicle Identification Number (VIN) generally visible from outside an automobile, a police officer may reach into the passenger compartment of a vehicle to move papers obscuring the VIN after its driver has been stopped for a traffic violation and has exited the car. We hold that, in these circumstances, the police officer’s action does not violate the Fourth Amendment.</p>
<p id="b189-12">I</p>
<p id="b189-13">On the afternoon of May 11, 1981, New York City police officers Lawrence Meyer and William McNamee observed re<page-number citation-index="1" label="108">*108</page-number>spondent Benigno Class driving above the speed limit in a car with a cracked windshield. Both driving with a cracked windshield and speeding are traffic violations under New York law. See N. Y. Veh. &amp; Traf. Law §§375(22), 1180(d) (McKinney 1970). Respondent followed the officers’ ensuing directive to pull over. Respondent then emerged from his car and approached Officer Meyer. Officer McNamee went directly to respondent’s vehicle. Respondent provided Officer Meyer with a registration certificate and proof of insurance, but stated that he had no driver’s license.</p>
<p id="b190-5">Meanwhile, Officer McNamee opened the door of respondent’s car to look for the VIN, which is located on the left doorjamb in automobiles manufactured before 1969. When the officer did not find the VIN on the doorjamb, he reached into the interior of respondent’s car to move some papers obscuring the area of the dashboard where the VIN is located in later model automobiles. In doing so, Officer McNamee saw the handle of a gun protruding about one inch from underneath the driver’s seat. The officer seized the gun, and respondent was promptly arrested. Respondent was also issued summonses for his traffic violations.</p>
<p id="b190-6">It is undisputed that the police officers had no reason to suspect that respondent’s car was stolen, that it contained contraband, or that respondent had committed an offense other than the traffic violations. Nor is it disputed that respondent committed the traffic violations with which he was charged, and that, as of the day of the arrest, he had not been issued a valid driver’s license.</p>
<p id="b190-7">After the state trial court denied a motion to suppress the gun as evidence, respondent was convicted of criminal possession of a weapon in the third degree. See N. Y. Penal Law § 265.02(4) (McKinney 1980). The Appellate Division of the New York Supreme Court upheld the conviction without opinion. 97 App. Div. 2d 741, 468 N. Y. S. 2d 892 (1983). The New York Court of Appeals reversed. It reasoned that the police officer’s “intrusion . . . was undertaken to obtain <page-number citation-index="1" label="109">*109</page-number>information and it exposed . . . hidden areas” of the car, and “therefore constituted a search.” 63 N. Y. 2d 491, 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d 1009, 1011</a></span> (1984). Although it recognized that a search for a VIN generally involves a minimal intrusion because of its limited potential locations, and agreed that there is a compelling law enforcement interest in positively identifying vehicles involved in accidents or automobile thefts, the court thought it decisive that the facts of this case “reveal no reason for the officer to suspect other criminal activity [besides the traffic infractions] or to act to protect his own safety.” <em>Id., </em>at 495-496, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1012" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1012</a></span>. The state statutory provision that authorizes officers to demand that drivers reveal their VIN “provided no justification for the officer’s entry of [respondent’s] car.” <em>Id., </em>at 497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1013" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1013</a></span>. If the officer had taken advantage of that statute and asked to see the VIN, respondent could have moved the papers away himself and no intrusion would have occurred. In the absence of any justification for the search besides the traffic infractions, the New York Court of Appeals ruled that the gun must be excluded from evidence.</p>
<p id="b191-5">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./471/1003/">471 U. S. 1003</a></span> (1985), and now reverse.</p>
<p id="b191-6">II</p>
<p id="b191-7">Respondent asserts that this Court is without jurisdiction to hear this case because the decision of the New York Court of Appeals rests on an adequate and independent state ground. We disagree.</p>
<p id="b191-8">The opinion of the New York Court of Appeals mentions the New York Constitution but once, and then only in direct conjunction with the United States Constitution. 63 N. Y. 2d, at 493, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1010" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1010</a></span>. Cf. <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1043" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1043</a></span> (1983). The opinion below makes use of both federal and New York cases in its analysis, generally citing both for the same proposition. See, <em>e. g., </em>63 N. Y. 2d, at 494, 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1011</a></span>. The opinion lacks the requisite “plain statement” that it rests on state grounds. <page-number citation-index="1" label="110">*110</page-number><em>Michigan </em>v. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1042" aria-description="Citation for case: Michigan v. Long"><em>Long, supra, </em>at 1042, 1044</a></span>. Accordingly, our holding in <em>Michigan </em>v. <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span> </em>is directly applicable here:</p>
<blockquote id="b192-5">“[WJhen ... a state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law, and when the adequacy and independence of any possible state law ground is not clear from the face of the opinion, we will accept as the most reasonable explanation that the state court decided the case the way it did because it believed that federal law required it to do so.” <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040-1041</a></span>.</blockquote>
<p id="b192-6">See also <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#389" aria-description="Citation for case: California v. Carney">471 U. S. 386, 389, n. 1</a></span> (1985).</p>
<p id="b192-7">Respondent’s claim that the opinion below rested on independent and adequate state <em>statutory </em>grounds is also without merit. The New York Court of Appeals did not hold that §401 of New York’s Vehicle and Traffic Law prohibited the search at issue here, but, in rejecting an assertion of petitioner, merely held that § 401 “provided no justification” for a search. 63 N. Y. 2d, at 497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1013" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1013</a></span> (emphasis added). In determining that the police officer’s action was prohibited, the court below looked to the Federal Constitution, not the State’s statute. Moreover, New York adheres to the general rule that, when statutory construction can resolve a case, courts should not decide constitutional issues. See <em>Ashwander </em>v. <em>TV A, </em><span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#346" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 346-347</a></span> (1936) (Brandéis, J., concurring); <em>In re Peters </em>v. <em>New York City Housing Authority, </em><span class="citation" data-id="2566781"><a href="/opinion/2566781/matter-of-peters-v-new-york-city-hous-auth/#527" aria-description="Citation for case: MATTER OF PETERS v. New York City Hous. Auth.">307 N. Y. 519, 527</a></span>, <span class="citation" data-id="2566781"><a href="/opinion/2566781/matter-of-peters-v-new-york-city-hous-auth/#531" aria-description="Citation for case: MATTER OF PETERS v. New York City Hous. Auth.">121 N. E. 2d 529, 531</a></span> (1954). Since the New York Court of Appeals discussed both statutory and constitutional grounds, we may infer that the court believed the statutory issue insufficient to resolve the case. The discussion of the statute therefore could not have constituted an independent and adequate state ground.</p>
<p id="b193-10"><page-number citation-index="1" label="111">*111</page-number>i — I <em>h-i</em></p>
<p id="b193-3">A</p>
<p id="b193-4">The officer here, after observing respondent commit two traffic violations and exit the car, attempted to determine the VIN of respondent’s automobile. In reaching to remove papers obscuring the VIN, the officer intruded into the passenger compartment of the vehicle.</p>
<p id="b193-5">The VIN consists of more than a dozen digits, unique to each vehicle and required on all cars and trucks. See <span class="citation no-link">49 CFR §571.115</span> (1984). The VIN is roughly analogous to a serial number, but it can be deciphered to reveal not only the place of the automobile in the manufacturer’s production run, but also the make, model, engine type, and place of manufacture of the vehicle. See § 565.4.</p>
<p id="b193-6">The VIN is a significant thread in the web of regulation of the automobile. See generally <span class="citation no-link">43 Fed. Reg. 2189</span> (1978). The ease with which the VIN allows identification of a particular vehicle assists the various levels of government in many ways. For the Federal Government, the VIN improves the efficacy of recall campaigns, and assists researchers in determining the risks of driving various makes and models of automobiles. In combination with state insurance laws, the VIN reduces the number of those injured in accidents who go uncompensated for lack of insurance. In conjunction with the State’s registration requirements and safety inspections, the VIN helps to ensure that automobile operators are driving safe vehicles. By making automobile theft more difficult, the VIN safeguards not only property but also life and limb. See <span class="citation no-link">33 Fed. Reg. 10207</span> (1968) (noting that stolen vehicles are disproportionately likely to be involved in automobile accidents).</p>
<p id="b193-7">To facilitate the VIN’s usefulness for these laudable governmental purposes, federal law requires that the VIN be placed in the plain view of someone <em>outside </em>the automobile:</p>
<blockquote id="b194-4"><page-number citation-index="1" label="112">*112</page-number>“The VIN for passenger cars [manufactured after 1969] shall be located inside the passenger compartment. It shall be readable, without moving any part of the vehicle, through the vehicle glazing under daylight lighting conditions by an observer having 20/20 vision (Snellen) whose eye point is located <em>outside the vehicle </em>adjacent to the left windshield pillar. Each character in the VIN subject to this paragraph shall have a minimum height of 4 mm.” <span class="citation no-link">49 CFR §571.115</span> (S4.6) (1984) (emphasis added).</blockquote>
<p id="b194-5">In <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 658</a></span> (1979), we recognized the “vital interest” in highway safety and the various programs that contribute to that interest. In light of the important interests served by the VIN, the Federal and State Governments are amply justified in making it a part of the web of pervasive regulation that surrounds the automobile, and in requiring its placement in an area ordinarily in plain view from outside the passenger compartment.</p>
<p id="b194-6">B</p>
<p id="b194-7">A citizen does not surrender all the protections of the Fourth Amendment by entering an automobile. See <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 663</a></span>; <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span> (1973). Nonetheless, the State’s intrusion into a particular area, whether in an automobile or elsewhere, cannot result in a Fourth Amendment violation unless the area is one in which there is a “constitutionally protected reasonable expectation of privacy.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967) (Harlan, J., concurring). See <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#177" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 177-180</a></span> (1984); <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985).</p>
<p id="b194-8">The Court has recognized that the physical characteristics of an automobile and its use result in a lessened expectation of privacy therein:</p>
<blockquote id="b194-9">“One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom <page-number citation-index="1" label="113">*113</page-number>serves as one’s residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view.” <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).</blockquote>
<p id="b195-4">Moreover, automobiles are justifiably the subject of pervasive regulation by the State. Every operator of a motor vehicle must expect that the State, in enforcing its regulations, will intrude to some extent upon that operator’s privacy:</p>
<blockquote id="b195-5">“Automobiles, unlike homes, are subject to pervasive and continuing governmental regulation and controls, including periodic inspection and licensing requirements. As an everyday occurrence, police stop and examine vehicles when license plates or inspection stickers have expired, or if other violations, such as exhaust fumes or excessive noise, are noted, or if headlights or other safety equipment are not in proper working order.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1976).</blockquote>
<p id="b195-6">See also <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U. S., at 392</a></span>.</p>
<p id="b195-7">The factors that generally diminish the reasonable expectation of privacy in automobiles are applicable <em>a fortiori </em>to the VIN. As we have discussed above, the VIN plays an important part in the pervasive regulation by the government of the automobile. A motorist must surely expect that such regulation will on occasion require the State to determine the VIN of his or her vehicle, and the individual’s reasonable expectation of privacy in the VIN is thereby diminished. This is especially true in the case of a driver who has committed a traffic violation. See <em>Delaware </em>v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span> (“The foremost method of enforcing traffic and vehicle safety regulations ... is acting upon observed violations. <em>Vehicle stops for traffic violations occur countless times each day; and on these occasions, licenses and registration papers are subject to inspection and drivers without them will be as</em><page-number citation-index="1" label="114">*114</page-number><em>certained”) </em>(emphasis added). In addition, it is unreasonable to have an expectation of privacy in an object required by law to be located in a place ordinarily in plain view from the exterior of the automobile. The VIN’s mandated visibility makes it more similar to the exterior of the car than to the trunk or glove compartment. The exterior of a car, of course, is thrust into the public eye, and thus to examine it does not constitute a “search.” See <em>Cardwell </em>v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#588" aria-description="Citation for case: Cardwell v. Lewis"><em>Lewis, supra, </em>at 588-589</a></span>. In sum, because of the important role played by the VIN in the pervasive governmental regulation of the automobile and the efforts by the Federal Government to ensure that the VIN is placed in plain view, we hold that there was no reasonable expectation of privacy in the VIN.</p>
<p id="b196-5">We think it makes no difference that the papers in respondent’s car obscured the VIN from the plain view of the officer. We have recently emphasized that efforts to restrict access to an area do not generate a reasonable expectation of privacy where none would otherwise exist. See <em>Oliver </em>v. <em>United States, supra, </em>at 182-184 (placement of “No Trespassing” signs on secluded property does not create “legitimate privacy interest” in marihuana fields). Here, where the object at issue is an identification number behind the transparent windshield of an automobile driven upon the public roads, we believe that the placement of the obscuring papers was insufficient to create a privacy interest in the VIN. The mere viewing of the formerly obscured VIN was not, therefore, a violation of the Fourth Amendment.</p>
<p id="b196-6">C</p>
<p id="b196-7">The evidence that respondent sought to have suppressed was not the VIN, however, but a gun, the handle of which the officer saw from the interior of the car while reaching for the papers that covered the VIN. While the interior of an automobile is not subject to the same expectations of privacy that exist with respect to one’s home, a car’s interior as a whole is nonetheless subject to Fourth Amendment protec<page-number citation-index="1" label="115">*115</page-number>tion from unreasonable intrusions by the police. We agree with the New York Court of Appeals that the intrusion into that space constituted a “search.” 63 N. Y. 2d, at 495, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1011" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1011</a></span>. Cf. <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 653</a></span> (“[Shopping an automobile and detaining its occupants constitute a ‘seizure’. . . even though the purpose of the stop is limited and the resulting detention quite brief”). We must decide, therefore, whether this search was constitutionally permissible.</p>
<p id="b197-5">If respondent had remained in the car, the police would have been justified in asking him to move the papers obscuring the VIN. New York law authorizes a demand by officers to see the VIN, see 63 N. Y. 2d, at 496-497, <span class="citation" data-id="5536542"><a href="/opinion/5687406/people-v-class/#1012" aria-description="Citation for case: People v. Class">472 N. E. 2d, at 1012-1013</a></span>, and even if the state law were not explicit on this point we have no difficulty in concluding that a demand to inspect the VIN, like a demand to see license and registration papers, is within the scope of police authority pursuant to a traffic violation stop. See <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>Prouse, supra, </em>at 659</a></span>. If respondent had stayed in his vehicle and acceded to such a request from the officer, the officer would not have needed to intrude into the passenger compartment. Respondent chose, however, to exit the vehicle without removing the papers that covered the VIN; the officer chose to conduct his search without asking respondent to return to the car. We must therefore decide whether the officer acted within the bounds of the Fourth Amendment in conducting the search. We hold that he did.</p>
<p id="b197-6">Keeping the driver of a vehicle in the car during a routine traffic stop is probably the typical police practice. See D. Schultz &amp; D. Hunt, Traffic Investigation and Enforcement 17 (1983). Nonetheless, out of a concern for the safety of the police, the Court has held that officers may, consistent with the Fourth Amendment, exercise their discretion to require a driver who commits a traffic violation to exit the vehicle even though they lack any particularized reason for believing the driver possesses a weapon. <em>Pennsylvania </em>v. <em>Mimms, </em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 <page-number citation-index="1" label="116">*116</page-number>U. S. 106, 108-111</a></span> (1977) <em>(per curiam). </em>While we impute to respondent no propensity for violence, and while we are conscious of the fact that respondent here voluntarily left the vehicle, the facts of this case may be used to illustrate one of the principal justifications for the discretion given police officers by <em>Pennsylvania </em>v. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>: </em>while in the driver’s seat, respondent had a loaded pistol at hand. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>allows an officer to guard against that possibility by requiring the driver to exit the car briefly. Clearly, <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>also allowed the officers here to detain respondent briefly outside the car that he voluntarily exited while they completed their investigation.</p>
<p id="b198-5">The question remains, however, as to whether the officers could not only effect the seizure of respondent necessary to detain him briefly outside the vehicle, but also effect a search for the VIN that may have been necessary only because of that detention. The pistol beneath the seat did not, of course, disappear when respondent closed the car door behind him. To have returned respondent immediately to the automobile would have placed the officers in the same situation that the holding in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>allows officers to avoid — permitting an individual being detained to have possible access to a dangerous weapon and the benefit of the partial concealment provided by the car’s exterior. See <em>Pennsylvania </em>v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#110" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Mimms, supra, </em>at 110</a></span>. In light of the danger to the officers’ safety that would have been presented by returning respondent immediately to his car, we think the search to obtain the VIN was not prohibited by the Fourth Amendment.</p>
<p id="b198-6">The Fourth Amendment by its terms prohibits “unreasonable” searches and seizures. We have noted:</p>
<blockquote id="b198-7">“[T]here is ‘no ready test for determining reasonableness other than by balancing the need to search [or seize] against the invasion which the search [or seizure] entails.’ <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). And in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with <page-number citation-index="1" label="117">*117</page-number>rational inferences from those facts, justifiably warrant that intrusion.” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968) (footnote omitted) (brackets as in <em>Terry).</em></blockquote>
<p id="b199-5">This test generally means that searches must be conducted pursuant to a warrant backed by probable cause. See <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#105" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102, 105-109</a></span> (1965); <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#714" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 714-715</a></span> (1984). When a search or seizure has as its immediate object a search for a weapon, however, we have struck the balance to allow the weighty interest in the safety of police officers to justify war-rantless searches based only on a reasonable suspicion of criminal activity. See <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra;</a></span> Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972). Such searches are permissible despite their substantial intrusiveness. See <em>Terry </em>v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><em>Ohio, supra, </em>at 24-25</a></span> (search was “a severe, though brief, intrusion upon cherished personal security, and . . . must surely [have] b[een] an annoying, frightening, and perhaps humiliating experience”).</p>
<p id="b199-6">When the officer’s safety is less directly served by the detention, something more than objectively justifiable suspicion is necessary to justify the intrusion if the balance is to tip in favor of the legality of the governmental intrusion. In <em>Pennsylvania </em>v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#107" aria-description="Citation for case: Pennsylvania v. Mimms"><em>Mimms, supra, </em>at 107</a></span>, the officers had personally observed the seized individual in the commission of a traffic offense before requesting that he exit his vehicle. In <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#693" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 693</a></span> (1981), the officers had obtained a warrant to search the house that the person seized was leaving when they came upon him. While the facts in <em>Pennsylvania </em>v. <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>and <em>Michigan </em>v. <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>differ in some respects from the facts of this case, the similarities are strong enough that the balancing of governmental interests against governmental intrusion undertaken in those cases is also appropriate here. All three of the factors involved in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span> </em>and <em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span> </em>are present in this case: the safety of the officers was served by the governmental intrusion; the intrusion was minimal; and the search stemmed <page-number citation-index="1" label="118">*118</page-number>from some probable cause focusing suspicion on the individual affected by the search. Indeed, here the officers’ probable cause stemmed from directly observing respondent commit a violation of the law.</p>
<p id="b200-5">When we undertake the necessary balancing of “the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion,” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983), the conclusion that the search here was permissible follows. As we recognized in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 658</a></span>, the governmental interest in highway safety served by obtaining the VIN is of the first order, and the particular method of obtaining the VIN here was justified by a concern for the officers’ safety. The “critical” issue of the intrusiveness of the government’s action, <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#722" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 722</a></span> (Blackmun, J., concurring in judgment), also here weighs in favor of allowing the search. The search was focused in its objective and no more intrusive than necessary to fulfill that objective. The search was far less intrusive than a formal arrest, which would have been permissible for a traffic offense under New York law, see N. Y. Veh. &amp; Traf. Law § 155 (McKinney Supp. 1986); N. Y. Crim. Proc. Law §140.10(1) (McKinney 1981), and little more intrusive than a demand that respondent — under the eyes of the officers — move the papers himself. The VIN, which was the clear initial objective of the officer, is by law present in one of two locations — either inside the doorjamb, or atop the dashboard and thus ordinarily in plain view of someone outside the automobile. Neither of those locations is subject to a reasonable expectation of privacy. The officer here checked both those locations, and only those two locations. The officer did not root about the interior of respondent’s automobile before proceeding to examine the VIN. He did not reach into any compartments or open any containers. He did not even intrude into the interior at all until after he had checked the doorjamb for <page-number citation-index="1" label="119">*119</page-number>the VIN. When he did intrude, the officer simply reached directly for the unprotected space where the VIN was located to move the offending papers. We hold that this search was sufficiently unintrusive to be constitutionally permissible in light of the lack of a reasonable expectation of privacy in the VIN and the fact that the officers observed respondent commit two traffic violations. Any other conclusion would expose police officers to potentially grave risks without significantly reducing the intrusiveness of the ultimate conduct — viewing the VIN — which, as we have said, the officers were entitled, to do as part of an undoubtedly justified traffic stop.</p>
<p id="b201-5">We note that our holding today does not authorize police officers to enter a vehicle to obtain a dashboard-mounted VIN when the VIN is visible from outside the automobile. If the VIN is in the plain view of someone outside the vehicle, there is no justification for governmental intrusion into the passenger compartment to see it.<footnotemark>*</footnotemark></p>
<p id="b201-6">The judgment of the New York Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b201-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b201-8">Petitioner invites us to hold that respondent’s status as an unlicensed driver deprived him of any reasonable expectations of privacy in the vehicle, because the officers would have been within their discretion to have prohibited respondent from driving the ear away, to have impounded the ear, and to have later conducted an inventory search thereof. Cf. <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976) (police may conduct inventory search of car impounded for multiple parking violations); <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">467 U. S. 431</a></span> (1984) (discussing the “inevitable discovery” exception to the exclusionary rule). Petitioner also argues that there can be no Fourth Amendment violation here because the police could have arrested respondent, see N. Y. Veh. &amp; Traf. Law §155 (McKinney Supp. 1986); N. Y. Crim. Proc. Law §140.10(1) (McKinney 1981), and could then have searched the passenger compartment at the time of arrest, cf. <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), or arrested respondent and searched the car after impounding it pursuant to the arrest, see <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973). We do not, however, reach those questions here.</p>
</footnote>
</opinion>
```

---
