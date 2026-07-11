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

## GROUP: _overhaul2/lake/cases/Kaupp v. Texas.json  (`lake-record`, 5 assertions)

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
{"assertion_id": "ba712695a3d20ea5", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kaupp v. Texas"}, "payload": {"all": [{"cite": "538 U.S. 626", "page": "626", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "538"}, {"cite": "123 S. Ct. 1843", "page": "1843", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "123"}, {"cite": "155 L. Ed. 2d 814", "page": "814", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "155"}, {"cite": "2003 U.S. LEXIS 3670", "page": "3670", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2003"}], "display": "538 U.S. 626", "official": {"cite": "538 U.S. 626", "page": "626", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "538"}, "official_selection_present": true, "record_id": "Kaupp v. Texas"}}
{"assertion_id": "059931dd8c3f426e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-631", "record_id": "Kaupp v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-631", "pinpoint_status": "slip-only", "quote": "even more starkly than the facts in *Dunaway*.", "quote_fidelity": "mismatch", "record_id": "Kaupp v. Texas", "star_marker": null}}
{"assertion_id": "2fd2ed9908bf1b7a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-632", "record_id": "Kaupp v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-632", "pinpoint_status": "slip-only", "quote": "well-established precedent requires suppression of the confession unless that confession was 'an act of free will [sufficient] to purge the primary taint of the unlawful invasion,'", "quote_fidelity": "mismatch", "record_id": "Kaupp v. Texas", "star_marker": null}}
{"assertion_id": "9c00575b27f2a401", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-630", "record_id": "Kaupp v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-630", "pinpoint_status": "slip-only", "quote": "handcuffed him, and took him — shoeless and in his underwear in January — to a patrol car, then to the crime scene and the sheriff's office. After Miranda warnings and confrontation with a co-suspect's statement, he admitted some involvement. The Texas courts treated the encounter as consensual and admitted the confession. ## Issue Whether removing a suspect from his home and transporting him to the station for interrogation, without probable cause, was an arrest requiring probable cause — and, if so, whether his confession must be suppressed as the fruit of that illegal arrest. ## Rule Yes; an involuntary station-house transport for questioning is an arrest.", "quote_fidelity": "mismatch", "record_id": "Kaupp v. Texas", "star_marker": null}}
{"assertion_id": "0e35d7b79613477b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kaupp v. Texas"}, "payload": {"as_of_content": "2003-05-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kaupp v. Texas", "scope_note": "Per curiam application of Dunaway/Brown: a 3 a.m. station-house removal without probable cause is an arrest; the confession is its fruit absent attenuation. Good law.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Kingsley v. Hendrickson.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Kingsley v. Hendrickson"
type: case
citation: ""
parallel_cite: "576 U.S. 389; 135 S. Ct. 2466; 192 L. Ed. 2d 416; 25 Fla. L. Weekly Fed. S 401; 83 U.S.L.W. 4515"
neutral_cite: 2015 U.S. LEXIS 4073
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-06-22
docket: 14-6368
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kingsley v. Hendrickson
  varies_by_point: false
  scope_note: "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2811847/kingsley-v-hendrickson/"
  cluster_id: 2811847
  opinion_id: 9808641
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
related: ["[[Graham v. Connor]]", "[[County of Sacramento v. Lewis]]"]
aliases: []
tags: ["case", "use-of-force", "pretrial-detainee", "objective-reasonableness", "fourteenth-amendment", "section-1983"]
holding: "A pretrial detainee's Fourteenth Amendment excessive-force claim requires only that the force purposely or knowingly used against him was objectively unreasonable; no subjective awareness of unreasonableness need be shown."
lake:
  record_id: Kingsley v. Hendrickson
  status: verified
  projected_at: 2026-07-06
---

# Kingsley v. Hendrickson

*576 U.S. 389 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Michael Kingsley, a pretrial detainee in a Wisconsin jail, refused to remove paper covering the light fixture in his cell. Officers forcibly removed him to a receiving cell, where — Kingsley alleged — they slammed his head against a concrete bunk and used a Taser on him. He sued under § 1983 for excessive force. The jury was instructed that he had to prove the officers "recklessly" disregarded his safety (a subjective element) and returned a verdict for the officers; the Seventh Circuit affirmed.

## Issue
Whether a pretrial detainee's excessive-force claim under the Fourteenth Amendment requires proof that the officers were subjectively aware that their use of force was unreasonable, or only that the force was objectively unreasonable.

## Rule
Only objective unreasonableness need be shown. "we agree with the dissenting appeals court judge, the Seventh Circuit's jury instruction committee, and Kingsley, that a pretrial detainee must show only that the force purposely or knowingly used against him was objectively unreasonable." — 576 U.S. at 396-397 (135 S. Ct. at 2473). ^pin-397

The use of force must be deliberate (purposeful or knowing, not accidental), but its reasonableness is judged from the perspective of a reasonable officer on the scene, on a non-exhaustive set of factors — not on the officer's subjective intent. This differs from the Eighth Amendment standard for convicted prisoners, which asks whether force was applied maliciously and sadistically.

## Application
Because the jury had been told to apply a subjective standard, asking whether the officers were aware their force was unreasonable, the instructions were erroneous: Kingsley needed to prove only that the deliberate force used against him was objectively unreasonable in light of the facts the officers confronted (the need for force, the threat reasonably perceived, his resistance, the injury, and efforts to temper the response). The Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for consideration under the correct objective standard.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. A pretrial detainee's Fourteenth Amendment excessive-force claim is governed by an objective-reasonableness standard, with no requirement to prove the officers' subjective intent to punish or awareness of unreasonableness.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Kingsley* extends an objective-reasonableness approach akin to [[Graham v. Connor]] to the pretrial-detention setting and distinguishes the [[County of Sacramento v. Lewis]] line on substantive-due-process culpability. Several circuits have since extended its objective framework to pretrial-detainee conditions and medical-care claims. No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Kingsley v. Hendrickson*, 576 U.S. 389 (2015) — https://www.courtlistener.com/opinion/2811847/kingsley-v-hendrickson/ — pinpoint: 396-397 (135 S. Ct. at 2473, CL page-label confirmed; lead opinion id 9808641).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "de1aafd715692218", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kingsley v. Hendrickson"}, "payload": {"all": [{"cite": "576 U.S. 389", "page": "389", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "576"}, {"cite": "135 S. Ct. 2466", "page": "2466", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "192 L. Ed. 2d 416", "page": "416", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "192"}, {"cite": "2015 U.S. LEXIS 4073", "page": "4073", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "25 Fla. L. Weekly Fed. S 401", "page": "401", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}, {"cite": "83 U.S.L.W. 4515", "page": "4515", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "83"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Kingsley v. Hendrickson"}}
{"assertion_id": "8e1cff498ee25f3b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-397", "record_id": "Kingsley v. Hendrickson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-397", "pinpoint_status": "slip-only", "quote": "disregarded his safety (a subjective element) and returned a verdict for the officers; the Seventh Circuit affirmed. ## Issue Whether a pretrial detainee's excessive-force claim under the Fourteenth Amendment requires proof that the officers were subjectively aware that their use of force was unreasonable, or only that the force was objectively unreasonable. ## Rule Only objective unreasonableness need be shown.", "quote_fidelity": "mismatch", "record_id": "Kingsley v. Hendrickson", "star_marker": null}}
{"assertion_id": "80638b34f4597d06", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kingsley v. Hendrickson"}, "payload": {"as_of_content": "2015-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kingsley v. Hendrickson", "scope_note": "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment.", "varies_by_point": false}}
```

### lake record — Kingsley v. Hendrickson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kingsley v. Hendrickson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kingsley v. Hendrickson",
    "case_name_short": "Kingsley",
    "case_name_full": "Michael B. KINGSLEY, Petitioner v. Stan HENDRICKSON, Et Al.",
    "input_case_name": "Kingsley v. Hendrickson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-06-22",
    "year": 2015,
    "docket": "14-6368",
    "cluster_id": 2811847,
    "lead_opinion_id": 9808641,
    "sibling_ids": [
      2811847,
      9808641,
      9808642
    ],
    "absolute_url": "/opinion/2811847/kingsley-v-hendrickson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8174063,
        "score": 20,
        "case_name": "Kingsley v. Hendrickson"
      },
      {
        "cluster_id": 8172260,
        "score": 20,
        "case_name": "Kingsley v. Hendrickson"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "576 U.S. 389",
        "volume": "576",
        "reporter": "U.S.",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2466",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2466",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 416",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 401",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4515",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4515",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 4073",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4073",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "576 U.S. 389",
        "volume": "576",
        "reporter": "U.S.",
        "page": "389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 2466",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "2466",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "192 L. Ed. 2d 416",
        "volume": "192",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 4073",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "4073",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 401",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "401",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4515",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4515",
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
      "id": "pin-397",
      "page": null,
      "quote": "disregarded his safety (a subjective element) and returned a verdict for the officers; the Seventh Circuit affirmed. ## Issue Whether a pretrial detainee's excessive-force claim under the Fourteenth Amendment requires proof that the officers were subjectively aware that their use of force was unreasonable, or only that the force was objectively unreasonable. ## Rule Only objective unreasonableness need be shown.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kingsley v. Hendrickson",
    "varies_by_point": false,
    "scope_note": "Good law: pretrial-detainee excessive-force claims use a purely objective-reasonableness standard under the Fourteenth Amendment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Foster v. Commissioner of Correction (No. 1)",
          "cluster_id": 4758096,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darnell v. City of New York",
          "cluster_id": 4369355,
          "cite": [
            "849 F.3d 17",
            "2017 WL 676521",
            "2017 U.S. App. LEXIS 2911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfredo Miranda v. County of Lake",
          "cluster_id": 4525558,
          "cite": [
            "900 F.3d 335"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mary Gordon v. County of Orange",
          "cluster_id": 4493836,
          "cite": [
            "888 F.3d 1118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barton Ex Rel. Estate of Barton v. Taber",
          "cluster_id": 3198370,
          "cite": [
            "820 F.3d 958",
            "2016 WL 1658098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tapanga Hardeman v. David Wathen",
          "cluster_id": 4647629,
          "cite": [
            "933 F.3d 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Mays v. Thomas Dart",
          "cluster_id": 4783259,
          "cite": [
            "974 F.3d 810"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heriberto Rodriguez v. County of Los Angeles",
          "cluster_id": 4502306,
          "cite": [
            "891 F.3d 776"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tammy Brawner v. Scott Cnty., Tenn.",
          "cluster_id": 5106013,
          "cite": [
            "14 F.4th 585"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melisa Richmond v. Rubab Huq",
          "cluster_id": 4480081,
          "cite": [
            "885 F.3d 928"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Sandoval v. County of San Diego",
          "cluster_id": 4847368,
          "cite": [
            "985 F.3d 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shane Horton v. City of Santa Maria",
          "cluster_id": 4586718,
          "cite": [
            "915 F.3d 592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frost v. New York City Police Department",
          "cluster_id": 4805103,
          "cite": [
            "980 F.3d 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
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
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Denise Coley v. Lucas County, Ohio",
          "cluster_id": 2829693,
          "cite": [
            "799 F.3d 530",
            "2015 FED App. 0200P",
            "2015 U.S. App. LEXIS 14702",
            "2015 WL 4978463"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Short v. J. Hartman",
          "cluster_id": 9450747,
          "cite": [
            "87 F.4th 593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Darden v. City of Fort Worth, Texas",
          "cluster_id": 4461803,
          "cite": [
            "880 F.3d 722"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Julie Helphenstine v. Lewis County",
          "cluster_id": 9374379,
          "cite": [
            "60 F.4th 305"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry Alderson v. Concordia Parish Corrtl Facil, e",
          "cluster_id": 4347641,
          "cite": [
            "848 F.3d 415",
            "2017 WL 541006",
            "2017 U.S. App. LEXIS 2382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Altony Brooks v. Captain Jacumin",
          "cluster_id": 4618747,
          "cite": [
            "924 F.3d 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joan Kedra v. Richard Schroeter",
          "cluster_id": 4446761,
          "cite": [
            "876 F.3d 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Danzel Stearns v. Inmate Services Corporation",
          "cluster_id": 4749382,
          "cite": [
            "957 F.3d 902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kingsley v. Hendrickson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2811847 OR 9808641 OR 9808642) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk0Mjg4MDAwMDAwJnM9NDM5MDAxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282811847+OR+9808641+OR+9808642%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(2811847 OR 9808641 OR 9808642)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcmcz00NDg2MTU3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%282811847+OR+9808641+OR+9808642%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2811847 OR 9808641 OR 9808642)",
        "reviewed": 73,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 73,
        "triage_read": 0,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2811847 OR 9808641 OR 9808642)",
    "indexed_citing_opinions": 284,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2811847,
        "count": 113,
        "count_source": "search"
      },
      {
        "opinion_id": 9808641,
        "count": 174,
        "count_source": "search"
      },
      {
        "opinion_id": 9808642,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4145,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kingsley-v-hendrickson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMTQwOTMmcz0xMDI5MTA2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282811847+OR+9808641+OR+9808642%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2811847,
        "cited_id": 77039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 111904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 112924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 118144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 149651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 312370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2811847,
        "cited_id": 718230,
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
    "date_created": "2026-07-05T09:19:13Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:19:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:59:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:05:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:59:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kingsley v. Hendrickson

```
<opinion type="majority">
<author id="p-11">Justice BREYERdelivered the opinion of the Court.</author>
<p id="p-12">In this case, an individual detained in a jail prior to trial brought a claim under Rev. Stat. § 1979, <extracted-citation index="0" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, against several jail officers, alleging that they used excessive force against him, in violation of the Fourteenth Amendment's Due Process Clause. The officers concede that they intended to use the force that they used. But the parties disagree about whether the force used was excessive.</p>
<p id="p-13">The question before us is whether, to prove an excessive force claim, a pretrial detainee must show that the officers were <em>subjectively</em>aware that their use of force was unreasonable, or only that the officers' use of that force was <em>objectively</em>unreasonable. We conclude that the latter standard is the correct one.</p>
<p id="p-14">I</p>
<p id="p-15">A</p>
<p id="p-16">Some but not all of the facts are undisputed: Michael Kingsley, the petitioner, was arrested on a drug charge and detained in a Wisconsin county jail prior to trial. On the evening of May 20, 2010, an officer performing a cell check noticed a piece of paper covering the light fixture above Kingsley's bed. The officer told Kingsley to remove it; Kingsley refused; subsequently other officers told Kingsley to remove the paper; and each time Kingsley refused. The next morning, the jail administrator, Lieutenant Robert Conroy, ordered Kingsley to remove the paper. Kingsley once again refused. Conroy then told Kingsley that officers would remove the paper and that he would be moved to a receiving cell in the interim.</p>
<p id="p-17">Shortly thereafter, four officers, including respondents Sergeant Stan Hendrickson and Deputy Sheriff Fritz Degner, approached the cell and ordered Kingsley to stand, back up to the door, and keep his hands behind him. When Kingsley refused to comply, the officers handcuffed him, forcibly removed him from the cell, carried him to a receiving cell, and placed him face down on a bunk with his hands handcuffed behind his back.</p>
<p id="p-18">The parties' views about what happened next differ. The officers testified that Kingsley resisted their efforts to remove his handcuffs. Kingsley testified that he did not resist. All agree that Sergeant Hendrickson placed his knee in Kingsley's back and Kingsley told him in impolite language to get off. Kingsley testified that Hendrickson and Degner then slammed his head into the concrete bunk-an allegation the officers deny.</p>
<p id="p-19">The parties agree, however, about what happened next: Hendrickson directed Degner to stun Kingsley with a Taser; Degner applied a Taser to Kingsley's back for approximately five seconds; the officers then left the handcuffed Kingsley alone in the receiving cell; and officers returned to the cell 15 minutes later and removed Kingsley's handcuffs.</p>
<p id="p-20">B</p>
<p id="p-21">Based on these and related events, Kingsley filed a § 1983complaint in Federal District Court claiming (among other <a class="page-label" data-citation-index="1" data-label="2471" href="#p2471" id="p2471">*2471</a>things) that Hendrickson and Degner used excessive force against him, in violation of the Fourteenth Amendment's Due Process Clause. The officers moved for summary judgment, which the District Court denied, stating that "a reasonable jury could conclude that [the officers] acted with malice and intended to harm [Kingsley] when they used force against him." <em>Kingsley v. Josvai,</em>No. 10-cv-832-bbc (WD Wis., Nov. 16, 2011), App to Pet. for Cert. 66a-67a. Kingsley's excessive force claim accordingly proceeded to trial. At the conclusion of the trial, the District Court instructed the jury as follows:</p>
<blockquote id="p-22">"Excessive force means force <em>applied recklessly</em>that is unreasonable in light of the facts and circumstances of the time. Thus, to succeed on his claim of excessive use of force, plaintiff must prove each of the following factors by a preponderance of the evidence:</blockquote>
<blockquote id="p-23">"(1) Defendants used force on plaintiff;</blockquote>
<blockquote id="p-24">"(2) Defendants' use of force was unreasonable in light of the facts and circumstances at the time;</blockquote>
<blockquote id="p-25">"(3) Defendants knew that using force presented a risk of harm to plaintiff, but they recklessly disregarded plaintiff's safety by failing to take reasonable measures to minimize the risk of harm to plaintiff; and</blockquote>
<blockquote id="p-26">"(4) Defendants' conduct caused some harm to plaintiff.</blockquote>
<blockquote id="p-27">"In deciding whether one or more defendants used 'unreasonable' force against plaintiff, you must consider whether it was unreasonable from the perspective of a reasonable officer facing the same circumstances that defendants faced. You must make this decision based on what defendants knew at the time of the incident, not based on what you know now.</blockquote>
<blockquote id="p-28">"Also, in deciding whether one or more defendants used unreasonable force and acted with <em>reckless disregard of plaintiff's rights</em>, you may consider factors such as:</blockquote>
<blockquote id="p-29">"• The need to use force;</blockquote>
<blockquote id="p-30">"• The relationship between the need to use force and the amount of force used;</blockquote>
<blockquote id="p-31">"• The extent of plaintiff's injury;</blockquote>
<blockquote id="p-32">"• Whether defendants reasonably believed there was a threat to the safety of staff or prisoners; and</blockquote>
<blockquote id="p-33">"• Any efforts made by defendants to limit the amount of force used." App. 277-278 (emphasis added).</blockquote>
<p id="p-34">The jury found in the officers' favor.</p>
<p id="p-35">On appeal, Kingsley argued that the correct standard for judging a pretrial detainee's excessive force claim is objective unreasonableness. And, the jury instruction, he said, did not hew to that standard. A panel of the Court of Appeals disagreed, with one judge dissenting. The majority held that the law required a "subjective inquiry" into the officer's state of mind. There must be " 'an actual intent to violate [the plaintiff's] rights or reckless disregard for his rights.' " <extracted-citation case-ids="4120237" index="1" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d 443</a></span></extracted-citation>, 451 (C.A.7 2014)(quoting <em>Wilson v. Williams,</em><extracted-citation case-ids="11645248" index="2" url="https://cite.case.law/f3d/83/870/#p875"><span class="citation" data-id="718230"><a href="/opinion/718230/jackie-wilson-v-james-k-williams/" aria-description="Citation for case: Jackie Wilson v. James K. Williams">83 F.3d 870</a></span></extracted-citation>, 875 (C.A.7 1996)). The dissent would have used instructions promulgated by the Committee on Pattern Civil Jury Instructions of the Seventh Circuit, which require a pretrial detainee claiming excessive force to show only that the use of force was objectively unreasonable. <extracted-citation case-ids="4120237" index="3" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/#455" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d, at 455</a></span></extracted-citation>(opinion of Hamilton, J.); see Pattern Civ. Jury Instr. § 7.08 (2009). The dissent further stated that the District Court's use of the word "reckless" in the jury instruction added "an unnecessary and confusing element." <extracted-citation case-ids="4120237" index="4" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d, at 455</a></span></extracted-citation>.</p>
<p id="p-36">Kingsley filed a petition for certiorari asking us to determine whether the requirements <a class="page-label" data-citation-index="1" data-label="2472" href="#p2472" id="p2472">*2472</a>of a § 1983excessive force claim brought by a pretrial detainee must satisfy the subjective standard or only the objective standard. In light of disagreement among the Circuits, we agreed to do so. Compare, <em>e.g.,</em> <em>Murray v. Johnson No. 260,</em><extracted-citation index="5" url="https://cite.case.law/citations/?q=367%20Fed.%20Appx.%20196"><span class="citation" data-id="3804"><a href="/opinion/3804/murray-v-johnson-260/" aria-description="Citation for case: Murray v. Johnson 260">367 Fed.Appx. 196</a></span></extracted-citation>, 198 (C.A.2 2010); <em>Bozeman v. Orum,</em><extracted-citation case-ids="8938554" index="6" url="https://cite.case.law/f3d/422/1265/#p1271"><span class="citation" data-id="9415944"><a href="/opinion/77039/willie-h-bozeman-v-silas-orum-iii/" aria-description="Citation for case: Willie H. Bozeman v. Silas Orum, III">422 F.3d 1265</a></span></extracted-citation>, 1271 (C.A.11 2005)(<em>per curiam</em>), with <em>Aldini v. Johnson,</em><extracted-citation case-ids="3691423" index="7" url="https://cite.case.law/f3d/609/858/#p865"><span class="citation" data-id="149651"><a href="/opinion/149651/aldini-v-johnson/" aria-description="Citation for case: Aldini v. Johnson">609 F.3d 858</a></span></extracted-citation>, 865-866 (C.A.6 2010); <em>Young v. Wolfe,</em><extracted-citation index="8" url="https://cite.case.law/citations/?q=478%20Fed.%20Appx.%20354"><span class="citation" data-id="798412"><a href="/opinion/798412/john-young-v-aron-wolfe/" aria-description="Citation for case: John Young v. Aron Wolfe">478 Fed.Appx. 354</a></span></extracted-citation>, 356 (C.A.9 2012).</p>
<p id="p-37">II</p>
<p id="p-38">A</p>
<p id="p-39">We consider a legally requisite state of mind. In a case like this one, there are, in a sense, two separate state-of-mind questions. The first concerns the defendant's state of mind with respect to his physical acts-<em>i.e.,</em>his state of mind with respect to the bringing about of certain physical consequences in the world. The second question concerns the defendant's state of mind with respect to whether his use of force was "excessive." Here, as to the first question, there is no dispute. As to the second, whether to interpret the defendant's physical acts in the world as involving force that was "excessive," there is a dispute. We conclude with respect to that question that the relevant standard is objective not subjective. Thus, the defendant's state of mind is not a matter that a plaintiff is required to prove.</p>
<p id="p-40">Consider the series of physical events that take place in the world-a series of events that might consist, for example, of the swing of a fist that hits a face, a push that leads to a fall, or the shot of a Taser that leads to the stunning of its recipient. No one here denies, and we must assume, that, as to the series of events that have taken place in the world, the defendant must possess a purposeful, a knowing, or possibly a reckless state of mind. That is because, as we have stated, "liability for <em>negligently</em>inflicted harm is categorically beneath the threshold of constitutional due process." <em>County of Sacramento v. Lewis,</em><extracted-citation case-ids="11504410" index="9" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span></extracted-citation>, 849, <extracted-citation case-ids="11504410" index="10" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="11" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">140 L.Ed.2d 1043</a></span></extracted-citation> (1998)(emphasis added). See also <em>Daniels v. Williams,</em><extracted-citation case-ids="6204748" index="12" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">474 U.S. 327</a></span></extracted-citation>, 331, <extracted-citation case-ids="6204748" index="13" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">106 S.Ct. 662</a></span></extracted-citation>, <extracted-citation case-ids="6204748" index="14" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">88 L.Ed.2d 662</a></span></extracted-citation> (1986)("Historically, this guarantee of due process has been applied to <em>deliberate</em> decisions of government officials to deprive a person of life, liberty, or property"). Thus, if an officer's Taser goes off by accident or if an officer unintentionally trips and falls on a detainee, causing him harm, the pretrial detainee cannot prevail on an excessive force claim. But if the use of force is deliberate-<em>i.e.,</em> purposeful or knowing-the pretrial detainee's claim may proceed. In the context of a police pursuit of a suspect the Court noted, though without so holding, that recklessness in some cases might suffice as a standard for imposing liability. See <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#849" aria-description="Citation for case: County of Sacramento v. Lewis"><em>Lewis, supra,</em>at 849</a></span>, <extracted-citation case-ids="11504410" index="15" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Whether that standard might suffice for liability in the case of an alleged mistreatment of a pretrial detainee need not be decided here; for the officers do not dispute that they acted purposefully or knowingly with respect to the force they used against Kingsley.</p>
<p id="p-41">We now consider the question before us here-the defendant's state of mind with respect to the proper <em>interpretation</em> of the force (a series of events in the world) that the defendant deliberately (not accidentally or negligently) used. In deciding whether the force deliberately used is, constitutionally speaking, "excessive," should courts use an objective standard only, or instead a subjective standard that takes into account a defendant's state of mind? It is with respect to <em>this</em> question that we hold that courts must use an <a class="page-label" data-citation-index="1" data-label="2473" href="#p2473" id="p2473">*2473</a>objective standard. In short, we agree with the dissenting appeals court judge, the Seventh Circuit's jury instruction committee, and Kingsley, that a pretrial detainee must show only that the force purposely or knowingly used against him was objectively unreasonable.</p>
<p id="p-42">A court (judge or jury) cannot apply this standard mechanically. See <span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#850" aria-description="Citation for case: County of Sacramento v. Lewis"><em>Lewis, supra,</em>at 850</a></span>, <extracted-citation case-ids="11504410" index="16" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Rather, objective reasonableness turns on the "facts and circumstances of each particular case." <em>Graham v. Connor,</em><extracted-citation case-ids="605535" index="17" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 396, <extracted-citation case-ids="605535" index="18" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="19" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989). A court must make this determination from the perspective of a reasonable officer on the scene, including what the officer knew at the time, not with the 20/20 vision of hindsight. See <em><extracted-citation case-ids="605535" index="20" url="https://cite.case.law/us/490/386/#p396">ibid</extracted-citation></em><extracted-citation case-ids="605535" index="20" url="https://cite.case.law/us/490/386/#p396">.</extracted-citation> A court must also account for the "legitimate interests that stem from [the government's] need to manage the facility in which the individual is detained," appropriately deferring to "policies and practices that in th[e] judgment" of jail officials "are needed to preserve internal order and discipline and to maintain institutional security." <em>Bell v. Wolfish,</em><extracted-citation case-ids="1780223" index="21" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. 520</a></span></extracted-citation>, 540, 547, <extracted-citation case-ids="1780223" index="22" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="23" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">60 L.Ed.2d 447</a></span></extracted-citation> (1979).</p>
<p id="p-43">Considerations such as the following may bear on the reasonableness or unreasonableness of the force used: the relationship between the need for the use of force and the amount of force used; the extent of the plaintiff's injury; any effort made by the officer to temper or to limit the amount of force; the severity of the security problem at issue; the threat reasonably perceived by the officer; and whether the plaintiff was actively resisting. See, <em>e.g.,</em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#396" aria-description="Citation for case: Graham v. Connor"><em>Graham, supra,</em>at 396</a></span>, <extracted-citation case-ids="605535" index="24" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. We do not consider this list to be exclusive. We mention these factors only to illustrate the types of objective circumstances potentially relevant to a determination of excessive force.</p>
<p id="p-44">B</p>
<p id="p-45">Several considerations have led us to conclude that the appropriate standard for a pretrial detainee's excessive force claim is solely an objective one. For one thing, it is consistent with our precedent. We have said that "the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment." <em>Graham,</em> <em>supra,</em>at 395, n. 10, <extracted-citation case-ids="605535" index="25" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. And in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span>,</em>we explained that such "punishment" can consist of actions taken with an "expressed intent to punish." <extracted-citation case-ids="1780223" index="26" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S., at 538</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="27" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. But the <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>Court went on to explain that, in the absence of an expressed intent to punish, a pretrial detainee can nevertheless prevail by showing that the actions are not "rationally related to a legitimate nonpunitive governmental purpose" or that the actions "appear excessive in relation to that purpose."<span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#561" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 561</a></span>, <extracted-citation case-ids="1780223" index="28" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>Court applied this latter objective standard to evaluate a variety of prison conditions, including a prison's practice of double-bunking. In doing so, it did not consider the prison officials' subjective beliefs about the policy. <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#541" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 541-543</a></span>, <extracted-citation case-ids="1780223" index="29" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Rather, the Court examined objective evidence, such as the size of the rooms and available amenities, before concluding that the conditions were reasonably related to the legitimate purpose of holding detainees for trial and did not appear excessive in relation to that purpose. <em><extracted-citation case-ids="1780223" index="30" url="https://cite.case.law/us/441/520/#p540">Ibid</extracted-citation></em><extracted-citation case-ids="1780223" index="30" url="https://cite.case.law/us/441/520/#p540">.</extracted-citation></p>
<p id="p-46"><em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s focus on "punishment" does not mean that proof of intent (or motive) to punish is required for a pretrial detainee to prevail on a claim that his due process rights were violated. Rather, as <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>itself shows (and as our later precedent affirms), a pretrial detainee can prevail by providing only objective evidence that the challenged governmental action is not rationally related <a class="page-label" data-citation-index="1" data-label="2474" href="#p2474" id="p2474">*2474</a>to a legitimate governmental objective or that it is excessive in relation to that purpose. Cf. <em>Block v. Rutherford,</em><extracted-citation case-ids="11339397" index="31" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">468 U.S. 576</a></span></extracted-citation>, 585-586, <extracted-citation case-ids="11339397" index="32" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">104 S.Ct. 3227</a></span></extracted-citation>, <extracted-citation case-ids="11339397" index="33" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">82 L.Ed.2d 438</a></span></extracted-citation> (1984)(where there was no suggestion that the purpose of jail policy of denying contact visitation was to punish inmates, the Court need only evaluate whether the policy was "reasonably related to legitimate governmental objectives" and whether it appears excessive in relation to that objective); <em>Schall v. Martin,</em><extracted-citation case-ids="6198853" index="34" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">467 U.S. 253</a></span></extracted-citation>, 269-271, <extracted-citation case-ids="6198853" index="35" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>, <extracted-citation case-ids="6198853" index="36" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">81 L.Ed.2d 207</a></span></extracted-citation> (1984)(similar); see also <em>United States v. Salerno,</em><extracted-citation case-ids="6222105" index="37" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">481 U.S. 739</a></span></extracted-citation>, 747, <extracted-citation case-ids="6222105" index="38" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>, <extracted-citation case-ids="6222105,1148012" index="39" url="https://cite.case.law/l-ed-2d/95/697/"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">95 L.Ed.2d 697</a></span></extracted-citation> (1987)("[T]he punitive/regulatory distinction <em>turns on</em>'whether an alternative purpose to which [the restriction] may rationally be connected is assignable for it, and whether it appears excessive in relation to the alternative purpose assigned [to it]' " (quoting <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#269" aria-description="Citation for case: Schall v. Martin"><em>Schall, supra,</em>at 269</a></span>, <extracted-citation case-ids="6198853" index="40" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>; emphasis added and some internal quotation marks omitted)). The Court did not suggest in any of these cases, either by its words or its analysis, that its application of <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s objective standard should involve subjective considerations. Our standard is also consistent with our use of an objective "excessive force" standard where officers apply force to a person who, like Kingsley, has been accused but not convicted of a crime, but who, unlike Kingsley, is free on bail. See <em>Graham, <extracted-citation case-ids="605535" index="41" url="https://cite.case.law/us/490/386/#p396">supra</extracted-citation></em><extracted-citation case-ids="605535" index="41" url="https://cite.case.law/us/490/386/#p396">.</extracted-citation></p>
<p id="p-47">For another thing, experience suggests that an objective standard is workable. It is consistent with the pattern jury instructions used in several Circuits. We are also told that many facilities, including the facility at issue here, train officers to interact with all detainees as if the officers' conduct is subject to an objective reasonableness standard. See Brief for Petitioner 26; App. 247-248; Brief for Former Corrections Administrators and Experts as <em>Amici Curiae</em>8-18.</p>
<p id="p-48">Finally, the use of an objective standard adequately protects an officer who acts in good faith. We recognize that "[r]unning a prison is an inordinately difficult undertaking," <em>Turner v. Safley,</em><extracted-citation case-ids="6210045" index="42" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">482 U.S. 78</a></span></extracted-citation>, 84-85, <extracted-citation case-ids="6210045" index="43" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">107 S.Ct. 2254</a></span></extracted-citation>, <extracted-citation case-ids="6210045" index="44" url="https://cite.case.law/us/482/78/#p84"><span class="citation" data-id="9431005"><a href="/opinion/111904/turner-v-safley/" aria-description="Citation for case: Turner v. Safley">96 L.Ed.2d 64</a></span></extracted-citation> (1987), and that "safety and order at these institutions requires the expertise of correctional officials, who must have substantial discretion to devise reasonable solutions to the problems they face," <em>Florence v. Board of Chosen Freeholders of County of Burlington,</em>566 U.S. ----, ----, <extracted-citation case-ids="12189139" index="45" url="https://cite.case.law/us/566/318/#p1515"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">132 S.Ct. 1510</a></span></extracted-citation>, 1515, <extracted-citation case-ids="12189139" index="46" url="https://cite.case.law/us/566/318/#p1515"><span class="citation" data-id="9485643"><a href="/opinion/626454/florence-v-board-of-chosen-freeholders-of-county-of-burlington/" aria-description="Citation for case: Florence v. Board of Chosen Freeholders of County of...">182 L.Ed.2d 566</a></span></extracted-citation> (2012). Officers facing disturbances "are often forced to make split-second judgments-in circumstances that are tense, uncertain, and rapidly evolving." <em>Graham,</em><extracted-citation case-ids="605535" index="47" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S., at 397</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="48" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>. For these reasons, we have stressed that a court must judge the reasonableness of the force used from the perspective and with the knowledge of the defendant officer. We have also explained that a court must take account of the legitimate interests in managing a jail, acknowledging as part of the objective reasonableness analysis that deference to policies and practices needed to maintain order and institutional security is appropriate. See Part II-A, <em>supra.</em>And we have limited liability for excessive force to situations in which the use of force was the result of an intentional and knowing act (though we leave open the possibility of including a "reckless" act as well). <em><extracted-citation case-ids="605535" index="49" url="https://cite.case.law/us/490/386/#p396">Ibid.</extracted-citation></em> Additionally, an officer enjoys qualified immunity and is not liable for excessive force unless he has violated a "clearly established" right, such that "it would [have been] clear to a reasonable officer that his conduct was unlawful in the situation he confronted." <em>Saucier v. Katz,</em><extracted-citation case-ids="9313023" index="50" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span></extracted-citation>, 202, <extracted-citation case-ids="9313023" index="51" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/S.Ct./121/2151/">121 S.Ct. 2151</a></span></extracted-citation>, <extracted-citation case-ids="9313023" index="52" url="https://cite.case.law/us/533/194/#p202"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/150/272/">150 L.Ed.2d 272</a></span></extracted-citation> (2001); see also Brief for United States as <em>Amicus Curiae</em>27-28. It is unlikely (though theoretically possible)</p>
<p id="p-49"><a class="page-label" data-citation-index="1" data-label="2475" href="#p2475" id="p2475">*2475</a>that a plaintiff could overcome these hurdles where an officer acted in good faith.</p>
<p id="p-50">C</p>
<p id="p-51">Respondents believe that the relevant legal standard should be subjective, <em>i.e.,</em>that the plaintiff must prove that the use of force was not "applied in a good-faith effort to maintain or restore discipline" but, rather, was applied "maliciously and sadistically to cause harm." Brief for Respondents 27. And they refer to several cases that they believe support their position. See <em>id.,</em>at 26-31 (citing <em>Whitley v. Albers,</em><extracted-citation case-ids="6202378" index="53" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">475 U.S. 312</a></span></extracted-citation>, <extracted-citation case-ids="6202378" index="54" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">106 S.Ct. 1078</a></span></extracted-citation>, <extracted-citation case-ids="6202378" index="55" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">89 L.Ed.2d 251</a></span></extracted-citation> (1986); <em>Hudson v. McMillian,</em><extracted-citation case-ids="6219215" index="56" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">503 U.S. 1</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="57" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="58" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">117 L.Ed.2d 156</a></span></extracted-citation> (1992); <em>Lewis,</em><extracted-citation case-ids="11504410" index="59" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S. 833</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="60" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="61" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">140 L.Ed.2d 1043</a></span></extracted-citation>; <em>Johnson v. Glick,</em><extracted-citation case-ids="1318048" index="62" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F.2d 1028</a></span></extracted-citation> (C.A.2 1973)).</p>
<p id="p-52">The first two of these cases, however, concern excessive force claims brought by convicted prisoners under the Eighth Amendment's Cruel and Unusual Punishment Clause, not claims brought by pretrial detainees under the Fourteenth Amendment's Due Process Clause. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><em>Whitley, supra,</em>at 320</a></span>, <extracted-citation case-ids="6202378" index="63" url="https://cite.case.law/us/475/312/"><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">106 S.Ct. 1078</a></span></extracted-citation>; <span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/#6" aria-description="Citation for case: Hudson v. McMillian"><em>Hudson, supra,</em>at 6-7</a></span>, <extracted-citation case-ids="6219215" index="64" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>. The language of the two Clauses differs, and the nature of the claims often differs. And, most importantly, pretrial detainees (unlike convicted prisoners) cannot be punished at all, much less "maliciously and sadistically<em>.</em>" <em>Ingraham v. Wright,</em><extracted-citation case-ids="12126861" index="65" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U.S. 651</a></span></extracted-citation>, 671-672, n. 40, <extracted-citation case-ids="12126861" index="66" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">97 S.Ct. 1401</a></span></extracted-citation>, <extracted-citation case-ids="12126861" index="67" url="https://cite.case.law/us/430/651/#p671"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">51 L.Ed.2d 711</a></span></extracted-citation> (1977); <em>Graham,</em> <em>supra,</em>at 395, n. 10, <extracted-citation case-ids="605535" index="68" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation> (1989); see also 4 W. Blackstone, Commentaries *300 ("[I]f the offence be not bailable, or the party cannot find bail, he is to be committed to the county [jail] ... [b]ut ... only for safe custody, and not for punishment"). Thus, there is no need here, as there might be in an Eighth Amendment case, to determine when punishment is unconstitutional. <em><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span></em>and <em>Hudson</em>are relevant here only insofar as they address the practical importance of taking into account the legitimate safety-related concerns of those who run jails. And, as explained above, we believe we have done so.</p>
<p id="p-53"><em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span></em>does not prove respondents' point, either. There, the Court considered a claim that a police officer had violated due process by causing a death during a high-speed automobile chase aimed at apprehending a suspect. We wrote that "[j]ust as a purpose to cause harm is needed for Eighth Amendment liability in a [prison] riot case, so it ought to be needed for due process liability in a pursuit case." <extracted-citation case-ids="11504410" index="69" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S., at 854</a></span></extracted-citation>, <extracted-citation case-ids="11504410" index="70" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. Respondents contend that this statement shows that the Court embraced a standard for due process claims that requires a showing of subjective intent. Brief for Respondents 30-31. Other portions of the <em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">Lewis</a></span></em>opinion make clear, however, that this statement referred to the defendant's intent to commit the <em>acts</em> in question, not to whether the force intentionally used was "excessive." <extracted-citation case-ids="11504410" index="71" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">523 U.S., at 854</a></span></extracted-citation>, and n. 13, <extracted-citation case-ids="11504410" index="72" url="https://cite.case.law/us/523/833/#p849"><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/" aria-description="Citation for case: County of Sacramento v. Lewis">118 S.Ct. 1708</a></span></extracted-citation>. As explained above, the parties here do not dispute that respondents' use of force was intentional. See Part II-A, <em>supra</em>.</p>
<p id="p-54">Nor does <em><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></em>provide respondents with significant support. In that case Judge Friendly, writing for the Second Circuit, considered an excessive force claim brought by a pretrial detainee under the Fourteenth Amendment's Due Process Clause. Judge Friendly pointed out that the "management by a few guards of large numbers of prisoners" in an institution "may require and justify the occasional use of a degree of intentional force." <extracted-citation case-ids="1318048" index="73" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F.2d, at 1033</a></span></extracted-citation>. He added that, in determining whether that intentional use of force "crosse[s]" the "constitutional line," a court should look:</p>
<blockquote id="p-55"><a class="page-label" data-citation-index="1" data-label="2476" href="#p2476" id="p2476">*2476</a>"to such factors as [ (1) ] the need for the application of force, [ (2) ] the relationship between the need and the amount of force that was used, [ (3) ] the extent of injury inflicted, and [ (4) ] whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm." <em><extracted-citation case-ids="1318048" index="74" url="https://cite.case.law/f2d/481/1028/"><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Ibid.</a></span></extracted-citation></em></blockquote>
<p id="p-56">This statement does not suggest that the fourth factor (malicious and sadistic purpose to cause harm) is a <em>necessary</em>condition for liability. To the contrary, the words "such ... as" make clear that the four factors provide examples of some considerations, among others, that might help show that the use of force was excessive.</p>
<p id="p-57">Respondents believe these cases nonetheless help them make a broader point-namely, that a subjective standard "protects against a relative flood of claims," many of them perhaps unfounded, brought by pretrial detainees. Brief for Respondents 38. But we note that the Prison Litigation Reform Act of 1995, 42 U.S.C. § 1997e, which is designed to deter the filing of frivolous litigation against prison officials, applies to both pretrial detainees and convicted prisoners. Nor is there evidence of a rash of unfounded filings in Circuits that use an objective standard.</p>
<p id="p-58">We acknowledge that our view that an objective standard is appropriate in the context of excessive force claims brought by pretrial detainees pursuant to the Fourteenth Amendment may raise questions about the use of a subjective standard in the context of excessive force claims brought by convicted prisoners. We are not confronted with such a claim, however, so we need not address that issue today.</p>
<p id="p-59">III</p>
<p id="p-60">We now consider the lawfulness of the jury instruction given in this case in light of our adoption of an objective standard for pretrial detainees' excessive force claims. See Part II-A, <em>supra</em>. That jury instruction defined "excessive force" as "force applied recklessly that is unreasonable in light of the facts and circumstances of the time." App. 277. It required Kingsley to show that the officers "recklessly disregarded [Kingsley's] safety." <em>Id.,</em>at 278. And it suggested that Kingsley must show the defendants "acted with reckless disregard of [Kingsley's] rights," while telling the jury that it could consider several objective factors in making this determination. <em>Ibid</em>.</p>
<p id="p-61">Kingsley argues that the jury instruction is faulty because the word "reckless" suggests a need to prove that respondents acted with a certain subjective state of mind with respect to the excessive or nonexcessive nature of the force used, contrary to what we have just held. Reply Brief 20-22. Respondents argue that irrespective of our holding, any error in the instruction was harmless. Brief for Respondents 57-58. And the Solicitor General suggests that, because the instructions defined "recklessness" with reference to objective factors, those instructions effectively embody our objective standard and did not confuse the jury. Brief for United States as <em>Amicus Curiae</em>28-32.</p>
<p id="p-62">We agree with Kingsley that the instructions were erroneous. "[R]eckles[s] disregar[d] [of Kingsley's] safety" was listed as an additional requirement, beyond the need to find that "[respondents'] use of force was unreasonable in light of the facts and circumstances at the time." App. 278. See also <em>ibid.</em>(Kingsley had to show respondents "used unreasonable force <em>and</em>acted with reckless disregard of [Kingsley's] rights" (emphasis added)). And in determining whether respondents "acted with reckless disregard of [Kingsley's] rights," the jury was instructed to "consider <a class="page-label" data-citation-index="1" data-label="2477" href="#p2477" id="p2477">*2477</a>... [w]hether [respondents] reasonably <em>believed</em>there was a threat to the safety of staff or prisoners." <em>Ibid.</em>(emphasis added). Together, these features suggested the jury should weigh respondents' subjective reasons for using force and subjective views about the excessiveness of the force. As we have just held, that was error. But because the question whether that error was harmless may depend in part on the detailed specifics of this case, we leave that question for the Court of Appeals to resolve in the first instance.</p>
<p id="p-63">The decision of the Court of Appeals is vacated, and the case is remanded for proceedings consistent with this opinion.</p>
<p id="p-64"><em>It is so ordered.</em></p>
<p id="p-65">Justice SCALIA, with whom THE CHIEF JUSTICE and Justice THOMAS join, dissenting.</p>
<p id="p-66">The Constitution contains no freestanding prohibition of excessive force. There are, however, four constitutional provisions that we have said forbid the use of excessive force in certain circumstances. The Fourth Amendment prohibits it when it makes a search or seizure "unreasonable." The Eighth Amendment prohibits it when it constitutes "cruel and unusual" punishment. The Fifth and Fourteenth Amendments prohibit it (or, for that matter, any use of force) when it is used to "deprive" someone of "life, liberty, or property, without due process of law."</p>
<p id="p-67">This is a Fourteenth Amendment case. The Fifth Amendment applies only to federal actors; Kingsley forfeited any argument under the Fourth Amendment by failing to raise it below; and he acknowledges that the Eighth Amendment standard is inapplicable, Brief for Petitioner 27, n. 8. The only question before us is whether a pretrial detainee's due process rights are violated when "the force purposely or knowingly used against him [is] objectively unreasonable." <em>Ante,</em> at 2473. In my view, the answer is no. Our cases hold that the intentional infliction of punishment upon a pretrial detainee may violate the Fourteenth Amendment; but the infliction of "objectively unreasonable" force, without more, is not the intentional infliction of punishment.</p>
<p id="p-68">In <em>Bell v. Wolfish,</em><extracted-citation case-ids="1780223" index="75" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. 520</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="76" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="77" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">60 L.Ed.2d 447</a></span></extracted-citation> (1979), we held that the Due Process Clause forbids holding pretrial detainees in conditions that "amount to punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 535</a></span>, <extracted-citation case-ids="1780223" index="78" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Conditions amount to punishment, we explained, when they are "imposed for the purpose of punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#538" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 538</a></span>, <extracted-citation case-ids="1780223" index="79" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. Acting with the intent to punish means taking a " 'deliberate act intended to chastise or deter.' " <em>Wilson v. Seiter,</em><extracted-citation case-ids="1107993" index="80" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">501 U.S. 294</a></span></extracted-citation>, 300, <extracted-citation case-ids="1107993" index="81" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">111 S.Ct. 2321</a></span></extracted-citation>, <extracted-citation case-ids="1107993" index="82" url="https://cite.case.law/us/501/294/#p300"><span class="citation" data-id="9432339"><a href="/opinion/112626/wilson-v-seiter/" aria-description="Citation for case: Wilson v. Seiter">115 L.Ed.2d 271</a></span></extracted-citation> (1991)(quoting <em>Duckworth v. Franzen,</em><extracted-citation case-ids="1531408" index="83" url="https://cite.case.law/f2d/780/645/#p652"><span class="citation" data-id="462687"><a href="/opinion/462687/junior-ray-duckworth-cross-appellants-v-gayle-franzen-cross-appellees/" aria-description="Citation for case: Junior Ray Duckworth, Cross-Appellants v. Gayle Franzen,...">780 F.2d 645</a></span></extracted-citation>, 652 (C.A.7 1985)); see also <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#537" aria-description="Citation for case: Bell v. Wolfish"><em>Bell, supra,</em>at 537-538</a></span>, <extracted-citation case-ids="1780223" index="84" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The Court in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>recognized that intent to punish need not be "expressed," <extracted-citation case-ids="1780223" index="85" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S. at 538</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="86" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>, but may be established with circumstantial evidence. More specifically, if the condition of confinement being challenged "is not reasonably related to a legitimate goal-if it is arbitrary or purposeless-a court permissibly may infer that the purpose of the governmental action is punishment." <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#539" aria-description="Citation for case: Bell v. Wolfish"><em>Id.,</em>at 539</a></span>, <extracted-citation case-ids="1780223" index="87" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. We endorsed the same inference when we applied <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>'s intent-to-punish test in challenges brought by pretrial detainees against jailhouse security policies, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#560" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 560-562</a></span>, <extracted-citation case-ids="1780223" index="88" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>; <em>Block v. Rutherford,</em><extracted-citation case-ids="11339397" index="89" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">468 U.S. 576</a></span></extracted-citation>, 583-584, <extracted-citation case-ids="11339397" index="90" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">104 S.Ct. 3227</a></span></extracted-citation>, <extracted-citation case-ids="11339397" index="91" url="https://cite.case.law/us/468/576/#p585"><span class="citation" data-id="9429742"><a href="/opinion/111254/block-v-rutherford/" aria-description="Citation for case: Block v. Rutherford">82 L.Ed.2d 438</a></span></extracted-citation> (1984), and statutes permitting pretrial detention, <em>Schall v. Martin,</em><extracted-citation case-ids="6198853" index="92" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">467 U.S. 253</a></span></extracted-citation>, 255, 269, <extracted-citation case-ids="6198853" index="93" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>, <extracted-citation case-ids="6198853" index="94" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">81 L.Ed.2d 207</a></span></extracted-citation> (1984); <em>United States v. Salerno,</em><extracted-citation case-ids="6222105" index="95" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">481 U.S. 739</a></span></extracted-citation>, 741, 746-747, <extracted-citation case-ids="6222105" index="96" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>, <extracted-citation case-ids="6222105,1148012" index="97" url="https://cite.case.law/l-ed-2d/95/697/"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">95 L.Ed.2d 697</a></span></extracted-citation> (1987).</p>
<p id="p-69"><a class="page-label" data-citation-index="1" data-label="2478" href="#p2478" id="p2478">*2478</a>In light of these cases, I agree with the Court that "the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment." <em>Graham v. Connor,</em><extracted-citation case-ids="605535" index="98" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span></extracted-citation>, 395, n. 10, <extracted-citation case-ids="605535" index="99" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">109 S.Ct. 1865</a></span></extracted-citation>, <extracted-citation case-ids="605535" index="100" url="https://cite.case.law/us/490/386/#p396"><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">104 L.Ed.2d 443</a></span></extracted-citation> (1989)(citing <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish"><em>Bell, supra,</em>at 535-539</a></span>, <extracted-citation case-ids="1780223" index="101" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>). I disagree, however, that any intentional application of force that is objectively unreasonable in degree is a use of excessive force that "amount[s] to punishment." <em>Bell,</em><extracted-citation case-ids="1780223" index="102" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">441 U.S., at 535</a></span></extracted-citation>, <extracted-citation case-ids="1780223" index="103" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The Court reaches that conclusion by misreading <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>as forbidding States to take <em>any</em> harmful action against pretrial detainees that is not "reasonably related to a legitimate goal." <em><extracted-citation case-ids="1780223" index="104" url="https://cite.case.law/us/441/520/#p540">Id</extracted-citation></em><extracted-citation case-ids="1780223" index="104" url="https://cite.case.law/us/441/520/#p540">., at 539</extracted-citation>, <extracted-citation case-ids="1780223" index="105" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>.</p>
<p id="p-70"><em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>endorsed this "reasonable relation" inference in the context of a challenge <em>to conditions of a confinement</em>-specifically, challenges to the State's policy of housing two people in each cell, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#528" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 528</a></span>, 99 S.Ct. 1861and various security policies, <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#548" aria-description="Citation for case: Bell v. Wolfish"><em>id.,</em>at 548-549, 553, 555, 558, 560-562</a></span>, <extracted-citation case-ids="1780223" index="106" url="https://cite.case.law/us/441/520/#p540"><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">99 S.Ct. 1861</a></span></extracted-citation>. The conditions in which pretrial detainees are held, and the security policies to which they are subject, are the result of considered deliberation by the authority imposing the detention. If those conditions and policies lack any reasonable relationship to a legitimate, nonpunitive goal, it is logical to infer a punitive intent. And the same logic supports finding a punitive intent in statutes authorizing detention that lacks any reasonable relationship to a valid government interest. <span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/#269" aria-description="Citation for case: Schall v. Martin"><em>Schall, supra,</em>at 269</a></span>, <extracted-citation case-ids="6198853" index="107" url="https://cite.case.law/us/467/253/#p269"><span class="citation" data-id="9429639"><a href="/opinion/111198/schall-v-martin/" aria-description="Citation for case: Schall v. Martin">104 S.Ct. 2403</a></span></extracted-citation>; <span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/#746" aria-description="Citation for case: United States v. Salerno"><em>Salerno, supra,</em>at 746-747</a></span>, <extracted-citation case-ids="6222105" index="108" url="https://cite.case.law/us/481/739/#p747"><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">107 S.Ct. 2095</a></span></extracted-citation>.</p>
<p id="p-71">It is <em>illogical,</em>however, automatically to infer punitive intent from the fact that a prison guard used more force against a pretrial detainee than was necessary. That could easily have been the result of a misjudgment about the degree of force required to maintain order or protect other inmates, rather than the product of an intent to punish the detainee for his charged crime (or for any other behavior). An officer's decision regarding how much force to use is made "in haste, under pressure, and frequently without the luxury of a second chance," <em>Hudson v. McMillian,</em><extracted-citation case-ids="6219215" index="109" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">503 U.S. 1</a></span></extracted-citation>, 6, <extracted-citation case-ids="6219215" index="110" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">112 S.Ct. 995</a></span></extracted-citation>, <extracted-citation case-ids="6219215" index="111" url="https://cite.case.law/us/503/1/"><span class="citation" data-id="9432474"><a href="/opinion/112693/hudson-v-mcmillian/" aria-description="Citation for case: Hudson v. McMillian">117 L.Ed.2d 156</a></span></extracted-citation> (1992)(internal quotation marks omitted), not after the considered thought that precedes detention-policy determinations like those at issue in <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span>,</em><em>Block,</em><em>Schall,</em>and <em><span class="citation" data-id="9430976"><a href="/opinion/111891/united-states-v-salerno/" aria-description="Citation for case: United States v. Salerno">Salerno</a></span></em>. That an officer used more force than necessary might be <em>evidence</em>that he acted with intent to punish, but it is no more than that.</p>
<p id="p-72">In sum: <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>makes intent to punish the focus of its due-process analysis. Objective reasonableness of the force used is nothing more than a heuristic for identifying this intent. That heuristic makes good sense for considered decisions by the detaining authority, but is much weaker in the context of excessive-force claims. Kingsley does not argue that respondents actually intended to punish him, and his reliance on <em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/" aria-description="Citation for case: Bell v. Wolfish">Bell</a></span></em>to infer such an intent is misplaced.</p>
<p id="p-73">Kingsley claims that "the protections of due process ... extend beyond the narrow context of 'punishment.' " Brief for Petitioner 15. Unquestionably. A State would plainly violate the Due Process Clause if it extended a detainee's confinement because it believed him mentally ill (not as "punishment"), without giving him the constitutionally guaranteed processes that must precede the deprivation of liberty. But Kingsley does not claim deprivation of liberty in that normal sense of that word-the right to walk about free. He claims that the Due Process Clause confers, on pretrial detainees, a substantive "liberty" interest that consists of freedom from objectively unreasonable force. Kingsley seeks relief, in other words, under <a class="page-label" data-citation-index="1" data-label="2479" href="#p2479" id="p2479">*2479</a>the doctrine of "substantive due process," through which we have occasionally recognized "liberty" interests other than freedom from incarceration or detention, that "cannot be limited at all, except by provisions that are 'narrowly tailored to serve a compelling state interest.' " <em>Kerry v. Din,</em> --- U.S. ----, ----, <extracted-citation case-ids="12590180" index="112" url="https://cite.case.law/s-ct/135/2128/#p2133"><span class="citation" data-id="2808292"><a href="/opinion/2808292/kerry-v-din/" aria-description="Citation for case: Kerry v. Din">135 S.Ct. 2128</a></span></extracted-citation>, 2133, --- L.Ed.2d ---- (2015)(plurality opinion) (quoting <em>Reno v. Flores,</em><extracted-citation case-ids="6228898" index="113" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">507 U.S. 292</a></span></extracted-citation>, 301-302, <extracted-citation case-ids="6228898" index="114" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">113 S.Ct. 1439</a></span></extracted-citation>, <extracted-citation case-ids="6228898" index="115" url="https://cite.case.law/us/507/292/#p301"><span class="citation" data-id="9432751"><a href="/opinion/112833/reno-v-flores/" aria-description="Citation for case: Reno v. Flores">123 L.Ed.2d 1</a></span></extracted-citation> (1993)).</p>
<p id="p-74">Even if one believed that the right to process can confer the right to substance in particular cases, Kingsley's interest is not one of the "fundamental liberty interests" that substantive due process protects. We have said that that doctrine protects only those liberty interests that, carefully described, are "objectively, deeply rooted in this Nation's history and tradition, and implicit in the concept of ordered liberty, such that neither liberty nor justice would exist if they were sacrificed." <em>Washington v. Glucksberg,</em><extracted-citation case-ids="916123" index="116" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">521 U.S. 702</a></span></extracted-citation>, 720-721, <extracted-citation case-ids="916123" index="117" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">117 S.Ct. 2258</a></span></extracted-citation>, <extracted-citation case-ids="916123" index="118" url="https://cite.case.law/us/521/702/#p720"><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">138 L.Ed.2d 772</a></span></extracted-citation> (1997)(citations and internal quotation marks omitted). Carefully described, the liberty interest Kingsley asserts is the right of pretrial detainees to be free from the application of force that is more than is objectively required to further some legitimate, nonpunitive, governmental interest. He does not argue (nor could he) that this asserted interest could pass the test announced in <em><span class="citation" data-id="9433522"><a href="/opinion/118144/washington-v-glucksberg/" aria-description="Citation for case: Washington v. Glucksberg">Glucksberg</a></span></em>.</p>
<p id="p-75">I conclude by emphasizing that our Constitution is not the only source of American law. There is an immense body of state statutory and common law under which individuals abused by state officials can seek relief. Kingsley himself, in addition to suing respondents for excessive force under <extracted-citation index="119" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, brought a state-law claim for assault and battery. <extracted-citation case-ids="4120237" index="120" url="https://cite.case.law/f3d/744/443/#p451"><span class="citation" data-id="9802445"><a href="/opinion/2708847/michael-kingsley-v-stan-hendrickson/" aria-description="Citation for case: Michael Kingsley v. Stan Hendrickson">744 F.3d 443</a></span></extracted-citation>, 446, n. 6 (C.A.7 2014). The Due Process Clause is not "a font of tort law to be superimposed upon" that state system. <em>Daniels v. Williams,</em><extracted-citation case-ids="6204748" index="121" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">474 U.S. 327</a></span></extracted-citation>, 332, <extracted-citation case-ids="6204748" index="122" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">106 S.Ct. 662</a></span></extracted-citation>, <extracted-citation case-ids="6204748" index="123" url="https://cite.case.law/us/474/327/#p331"><span class="citation" data-id="9430259"><a href="/opinion/111555/daniels-v-williams/" aria-description="Citation for case: Daniels v. Williams">88 L.Ed.2d 662</a></span></extracted-citation> (1986)(quoting <em>Paul v. Davis,</em><extracted-citation case-ids="12027375" index="124" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U.S. 693</a></span></extracted-citation>, 701, <extracted-citation case-ids="12027375" index="125" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">96 S.Ct. 1155</a></span></extracted-citation>, <extracted-citation case-ids="12027375" index="126" url="https://cite.case.law/us/424/693/#p701"><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">47 L.Ed.2d 405</a></span></extracted-citation> (1976)). Today's majority overlooks this in its tender-hearted desire to tortify the Fourteenth Amendment.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Kisela v. Hughes.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Kisela v. Hughes"
type: case
citation: "584 U.S. 100 (2018)"
parallel_cite: "138 S. Ct. 1148; 200 L. Ed. 2d 449"
neutral_cite: 2018 U.S. LEXIS 2066
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-04-02
docket: 17-467
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-04-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kisela v. Hughes
  varies_by_point: false
  scope_note: "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4482892/kisela-v-hughes/"
  cluster_id: 4482892
  opinion_id: 4260145
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Graham v. Connor]]", "[[Tennessee v. Garner]]", "[[Mullenix v. Luna]]", "[[White v. Pauly]]", "[[City and County of San Francisco v. Sheehan]]", "[[Brosseau v. Haugen]]"]
aliases: []
tags: ["case", "use-of-force", "deadly-force", "qualified-immunity", "section-1983", "clearly-established-law", "mental-illness"]
holding: "An officer who shot a woman holding a large kitchen knife who had moved within striking distance of another woman and ignored commands to drop it was entitled to qualified immunity: clearly established law in excessive-force cases must be defined at a high level of specificity, and officers get immunity unless existing precedent 'squarely governs' the specific facts at issue."
lake:
  record_id: Kisela v. Hughes
  status: verified
  projected_at: 2026-07-06
---

# Kisela v. Hughes

*584 U.S. 100 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Tucson officer Andrew Kisela and two others responded to a 911 report of a woman hacking a tree with a kitchen knife and acting erratically. Within about a minute of arriving they saw Amy Hughes emerge from a house carrying a large knife and walk to within six feet of another woman, Sharon Chadwick. A chain-link fence separated the officers from the two women. The officers drew their guns and ordered Hughes at least twice to drop the knife; she appeared calm but did not comply. Kisela dropped to the ground and fired four shots through the fence, wounding Hughes (non-life-threatening). It later emerged the women were roommates and Chadwick said she never felt endangered. Hughes sued Kisela under § 1983 for excessive force.

## Issue
Whether Officer Kisela was entitled to [[Qualified Immunity|qualified immunity]] — i.e., whether his use of deadly force against Hughes violated clearly established law.

## Rule
The Court assumed without deciding that the shooting may have violated the Fourth Amendment and resolved the case on [[Qualified Immunity|qualified immunity]]. "Qualified immunity attaches when an official's conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known." — 138 S. Ct. at 1152 (quoting *White v. Pauly*). ^pin-1152

Existing precedent "must have placed the statutory or constitutional question beyond debate," and the Court has "'repeatedly told courts — and the Ninth Circuit in particular — not to define clearly established law at a high level of generality.'" — *Id.*

Force law demands [[Particularity|particularity]]. "Use of excessive force is an area of the law 'in which the result depends very much on the facts of each case,' and thus police officers are entitled to qualified immunity unless existing precedent 'squarely governs' the specific facts at issue." — 138 S. Ct. at 1153 (quoting *Mullenix v. Luna*). ^pin-1153

The general rules of [[Tennessee v. Garner]] and [[Graham v. Connor]] "do not by themselves create clearly established law outside an 'obvious case.'" — *Id.*

## Application
On these facts the case was "far from an obvious case in which any competent officer would have known that shooting Hughes to protect Chadwick would violate the Fourth Amendment": Kisela had only seconds to assess the threat, faced a woman who had just been reported hacking a tree with a large knife, who had moved within a few feet of Chadwick, and who ignored at least two audible commands to drop the weapon. Nor did circuit precedent place the question beyond debate — the most analogous Ninth Circuit case (*Blanford v. Sacramento County*) favored Kisela, while the decisions the Court of Appeals relied on (*Deorle*, *Glenn*, *Harris v. Roderick*) were materially different, involving unarmed or compliant suspects. Because no clearly established law squarely governed the situation Kisela confronted, he was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Reversed. Kisela was entitled to [[Qualified Immunity|qualified immunity]] because clearly established law, defined at the proper level of specificity, did not put it beyond debate that his use of force was unconstitutional.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** ([[Common Legal Terms#per-curiam|per curiam]]; Sotomayor, J., joined by Ginsburg, J., dissenting).
- *Kisela* applies the specificity principle of [[Brosseau v. Haugen]] and [[Mullenix v. Luna]] and the "beyond debate" standard of [[White v. Pauly]] and [[City and County of San Francisco v. Sheehan]] to excessive-force [[Qualified Immunity|qualified immunity]]. It is frequently cited for the rule that officers get immunity "unless existing precedent 'squarely governs' the specific facts." No negative treatment.

## Appears on
- [[Use of Force]] — *Key — Progeny / Refinement*
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Kisela v. Hughes*, 584 U.S. 100 (2018) (per curiam) — https://www.courtlistener.com/opinion/4482892/kisela-v-hughes/ — pinpoints: 138 S. Ct. at 1152, 1153.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd973219048e2426", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kisela v. Hughes"}, "payload": {"all": [{"cite": "584 U.S. 100", "page": "100", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "584"}, {"cite": "138 S. Ct. 1148", "page": "1148", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "138"}, {"cite": "200 L. Ed. 2d 449", "page": "449", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "200"}, {"cite": "2018 U.S. LEXIS 2066", "page": "2066", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2018"}], "display": "584 U.S. 100", "official": {"cite": "584 U.S. 100", "page": "100", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "584"}, "official_selection_present": true, "record_id": "Kisela v. Hughes"}}
{"assertion_id": "6da11853ebb8e38f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1152", "record_id": "Kisela v. Hughes"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1152", "pinpoint_status": "slip-only", "quote": "--- # Kisela v. Hughes *584 U.S. 100 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tucson officer Andrew Kisela and two others responded to a 911 report of a woman hacking a tree with a kitchen knife and acting erratically. Within about a minute of arriving they saw Amy Hughes emerge from a house carrying a large knife and walk to within six feet of another woman, Sharon Chadwick. A chain-link fence separated the officers from the two women. The officers drew their guns and ordered Hughes at least twice to drop the knife; she appeared calm but did not comply. Kisela dropped to the ground and fired four shots through the fence, wounding Hughes (non-life-threatening). It later emerged the women were roommates and Chadwick said she never felt endangered. Hughes sued Kisela under § 1983 for excessive force. ## Issue Whether Officer Kisela was entitled to qualified immunity — i.e., whether his use of deadly force against Hughes violated clearly established law. ## Rule The Court assumed without deciding that the shooting may have violated the Fourth Amendment and resolved the case on qualified immunity.", "quote_fidelity": "mismatch", "record_id": "Kisela v. Hughes", "star_marker": null}}
{"assertion_id": "d3e03edb14038732", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1153", "record_id": "Kisela v. Hughes"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1153", "pinpoint_status": "slip-only", "quote": "— *Id.* Force law demands particularity.", "quote_fidelity": "mismatch", "record_id": "Kisela v. Hughes", "star_marker": null}}
{"assertion_id": "21fd04de194bb898", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kisela v. Hughes"}, "payload": {"as_of_content": "2018-04-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kisela v. Hughes", "scope_note": "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented.", "varies_by_point": false}}
```

### lake record — Kisela v. Hughes

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kisela v. Hughes",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kisela v. Hughes",
    "case_name_short": "Kisela",
    "case_name_full": "Andrew KISELA v. Amy HUGHES.",
    "input_case_name": "Kisela v. Hughes",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-04-02",
    "year": 2018,
    "docket": "17-467",
    "cluster_id": 4482892,
    "lead_opinion_id": 4260145,
    "sibling_ids": [
      4260145
    ],
    "absolute_url": "/opinion/4482892/kisela-v-hughes/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "584 U.S. 100",
      "volume": "584",
      "reporter": "U.S.",
      "page": "100",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1148",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 449",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 2066",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2066",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "584 U.S. 100",
        "volume": "584",
        "reporter": "U.S.",
        "page": "100",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1148",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1148",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "200 L. Ed. 2d 449",
        "volume": "200",
        "reporter": "L. Ed. 2d",
        "page": "449",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 2066",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "2066",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "584 U.S. 100",
    "official_selection": {
      "court_class": "scotus",
      "selected": "584 U.S. 100",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1152",
      "page": null,
      "quote": "--- # Kisela v. Hughes *584 U.S. 100 (2018)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Tucson officer Andrew Kisela and two others responded to a 911 report of a woman hacking a tree with a kitchen knife and acting erratically. Within about a minute of arriving they saw Amy Hughes emerge from a house carrying a large knife and walk to within six feet of another woman, Sharon Chadwick. A chain-link fence separated the officers from the two women. The officers drew their guns and ordered Hughes at least twice to drop the knife; she appeared calm but did not comply. Kisela dropped to the ground and fired four shots through the fence, wounding Hughes (non-life-threatening). It later emerged the women were roommates and Chadwick said she never felt endangered. Hughes sued Kisela under \u00a7 1983 for excessive force. ## Issue Whether Officer Kisela was entitled to qualified immunity \u2014 i.e., whether his use of deadly force against Hughes violated clearly established law. ## Rule The Court assumed without deciding that the shooting may have violated the Fourth Amendment and resolved the case on qualified immunity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1153",
      "page": null,
      "quote": "\u2014 *Id.* Force law demands particularity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-04-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kisela v. Hughes",
    "varies_by_point": false,
    "scope_note": "Good law (per curiam). Reaffirms and applies the Brosseau/Mullenix specificity rule: in excessive-force cases officers get qualified immunity unless existing precedent 'squarely governs' the specific facts. Sotomayor (joined by Ginsburg) dissented.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heriberto Rodriguez v. County of Los Angeles",
          "cluster_id": 4502306,
          "cite": [
            "891 F.3d 776"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ana Sandoval v. County of San Diego",
          "cluster_id": 4847368,
          "cite": [
            "985 F.3d 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frost v. New York City Police Department",
          "cluster_id": 4805103,
          "cite": [
            "980 F.3d 231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jeffery Mays v. Ronald Sprinkle",
          "cluster_id": 4869132,
          "cite": [
            "992 F.3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Amy Corbitt v. Michael Vickers",
          "cluster_id": 4638184,
          "cite": [
            "929 F.3d 1304"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirk Horshaw v. Mark Casper",
          "cluster_id": 4573724,
          "cite": [
            "910 F.3d 1027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Vos v. City of Newport Beach",
          "cluster_id": 4506067,
          "cite": [
            "892 F.3d 1024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
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
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Martin v. Susan Duffy",
          "cluster_id": 4795803,
          "cite": [
            "977 F.3d 294"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Feminist Majority Foundation v. Richard Hurley",
          "cluster_id": 4574853,
          "cite": [
            "911 F.3d 674"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naumovski v. Norris",
          "cluster_id": 4647449,
          "cite": [
            "934 F.3d 200"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jose Peroza-Benitez v. Darren Smith",
          "cluster_id": 4871933,
          "cite": [
            "994 F.3d 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raheem Jacobs v. Cumberland County",
          "cluster_id": 4906491,
          "cite": [
            "8 F.4th 187"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Capp v. County of San Diego",
          "cluster_id": 4667181,
          "cite": [
            "940 F.3d 1046"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James P. Crocker v. Deputy Sheriff Steven Eric Beatty",
          "cluster_id": 4875336,
          "cite": [
            "995 F.3d 1232"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torcivia v. Suffolk County, New York",
          "cluster_id": 5295971,
          "cite": [
            "17 F.4th 342"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Bell, Jr. v. City of Southfield, Mich.",
          "cluster_id": 6477591,
          "cite": [
            "37 F.4th 362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Semple",
          "cluster_id": 4764447,
          "cite": [
            "963 F.3d 259"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
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
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sachin Gupta v. Chad Melloh",
          "cluster_id": 5303583,
          "cite": [
            "19 F.4th 990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
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
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matthew King v. Hendricks County Commissioner",
          "cluster_id": 4740934,
          "cite": [
            "954 F.3d 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kisela v. Hughes:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4260145) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjE3MDYyNDAwMDAwJnM9NDg2OTEzMiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284260145%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      },
      "lane2_top_cited": {
        "query": "cites:(4260145)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDImcz02NDQ1OTcwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%284260145%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4260145)",
        "reviewed": 139,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 139,
        "triage_read": 1,
        "triage_snippet_classified": 138
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4260145)",
    "indexed_citing_opinions": 381,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4260145,
        "count": 381,
        "count_source": "search"
      }
    ],
    "citation_count": 1755,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kisela-v-hughes.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyOTQ2NDEmcz0xMDM3NDUzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284260145%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4260145,
        "cited_id": 110443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 112458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 180078,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 574389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 610866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 746949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 775749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 790155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4260145,
        "cited_id": 2620705,
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
    "date_created": "2026-07-05T10:16:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T10:19:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T10:16:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kisela v. Hughes

```
                 Cite as: 584 U. S. ____ (2018)            1

                             Per Curiam

SUPREME COURT OF THE UNITED STATES
          ANDREW KISELA v. AMY HUGHES
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

               No. 17–467.    Decided April 2, 2018


  PER CURIAM.
  Petitioner Andrew Kisela, a police officer in Tucson,
Arizona, shot respondent Amy Hughes. Kisela and two
other officers had arrived on the scene after hearing a
police radio report that a woman was engaging in erratic
behavior with a knife. They had been there but a few
minutes, perhaps just a minute. When Kisela fired,
Hughes was holding a large kitchen knife, had taken steps
toward another woman standing nearby, and had refused
to drop the knife after at least two commands to do so.
The question is whether at the time of the shooting
Kisela’s actions violated clearly established law.
  The record, viewed in the light most favorable to
Hughes, shows the following. In May 2010, somebody in
Hughes’ neighborhood called 911 to report that a woman
was hacking a tree with a kitchen knife. Kisela and an-
other police officer, Alex Garcia, heard about the report
over the radio in their patrol car and responded. A few
minutes later the person who had called 911 flagged down
the officers; gave them a description of the woman with
the knife; and told them the woman had been acting errat-
ically. About the same time, a third police officer, Lindsay
Kunz, arrived on her bicycle.
  Garcia spotted a woman, later identified as Sharon
Chadwick, standing next to a car in the driveway of a
nearby house. A chain-link fence with a locked gate sepa-
rated Chadwick from the officers. The officers then saw
another woman, Hughes, emerge from the house carrying
a large knife at her side. Hughes matched the description
2                     KISELA v. HUGHES

                          Per Curiam

of the woman who had been seen hacking a tree. Hughes
walked toward Chadwick and stopped no more than six
feet from her.
   All three officers drew their guns. At least twice they
told Hughes to drop the knife. Viewing the record in the
light most favorable to Hughes, Chadwick said “take it
easy” to both Hughes and the officers. Hughes appeared
calm, but she did not acknowledge the officers’ presence or
drop the knife. The top bar of the chain-link fence blocked
Kisela’s line of fire, so he dropped to the ground and shot
Hughes four times through the fence. Then the officers
jumped the fence, handcuffed Hughes, and called para-
medics, who transported her to a hospital. There she was
treated for non-life-threatening injuries. Less than a
minute had transpired from the moment the officers saw
Chadwick to the moment Kisela fired shots.
   All three of the officers later said that at the time of the
shooting they subjectively believed Hughes to be a threat
to Chadwick. After the shooting, the officers discovered
that Chadwick and Hughes were roommates, that Hughes
had a history of mental illness, and that Hughes had been
upset with Chadwick over a $20 debt. In an affidavit
produced during discovery, Chadwick said that a few
minutes before the shooting her boyfriend had told her
Hughes was threatening to kill Chadwick’s dog, named
Bunny. Chadwick “came home to find” Hughes “somewhat
distressed,” and Hughes was in the house holding Bunny
“in one hand and a kitchen knife in the other.” Hughes
asked Chadwick if she “wanted [her] to use the knife on
the dog.” The officers knew none of this, though. Chad-
wick went outside to get $20 from her car, which is when
the officers first saw her. In her affidavit Chadwick said
that she did not feel endangered at any time. Ibid. Based
on her experience as Hughes’ roommate, Chadwick stated
that Hughes “occasionally has episodes in which she acts
inappropriately,” but “she is only seeking attention.” 2
                  Cite as: 584 U. S. ____ (2018)             3

                           Per Curiam

Record 108.
   Hughes sued Kisela under Rev. Stat. §1979, 42 U. S. C.
§1983, alleging that Kisela had used excessive force in
violation of the Fourth Amendment. The District Court
granted summary judgment to Kisela, but the Court of
Appeals for the Ninth Circuit reversed. 862 F. 3d 775
(2016).
   The Court of Appeals first held that the record, viewed
in the light most favorable to Hughes, was sufficient to
demonstrate that Kisela violated the Fourth Amendment.
See id., at 782. The court next held that the violation was
clearly established because, in its view, the constitutional
violation was obvious and because of Circuit precedent
that the court perceived to be analogous. Id., at 785.
Kisela filed a petition for rehearing en banc. Over the
dissent of seven judges, the Court of Appeals denied it.
Kisela then filed a petition for certiorari in this Court.
That petition is now granted.
   In one of the first cases on this general subject, Tennes-
see v. Garner, 471 U. S. 1 (1985), the Court addressed the
constitutionality of the police using force that can be deadly.
There, the Court held that “[w]here the officer has proba-
ble cause to believe that the suspect poses a threat of
serious physical harm, either to the officer or to others, it
is not constitutionally unreasonable to prevent escape by
using deadly force.” Id., at 11.
   In Graham v. Connor, 490 U. S. 386, 396 (1989), the
Court held that the question whether an officer has used
excessive force “requires careful attention to the facts and
circumstances of each particular case, including the sever-
ity of the crime at issue, whether the suspect poses an
immediate threat to the safety of the officers or others,
and whether he is actively resisting arrest or attempting
to evade arrest by flight.” “The ‘reasonableness’ of a par-
ticular use of force must be judged from the perspective of
a reasonable officer on the scene, rather than with the
4                    KISELA v. HUGHES

                         Per Curiam

20/20 vision of hindsight.” Ibid. And “[t]he calculus of
reasonableness must embody allowance for the fact that
police officers are often forced to make split-second judg-
ments—in circumstances that are tense, uncertain, and
rapidly evolving—about the amount of force that is neces-
sary in a particular situation.” Id., at 396–397.
    Here, the Court need not, and does not, decide whether
Kisela violated the Fourth Amendment when he used
deadly force against Hughes. For even assuming a Fourth
Amendment violation occurred—a proposition that is not
at all evident—on these facts Kisela was at least entitled
to qualified immunity.
    “Qualified immunity attaches when an official’s conduct
does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.” White v. Pauly, 580 U. S. ___, ___ (2017) (per
curiam) (slip op., at 6) (alterations and internal quotation
marks omitted). “Because the focus is on whether the
officer had fair notice that her conduct was unlawful,
reasonableness is judged against the backdrop of the law
at the time of the conduct.” Brosseau v. Haugen, 543 U. S.
194, 198 (2004) (per curiam).
    Although “this Court’s caselaw does not require a case
directly on point for a right to be clearly established,
existing precedent must have placed the statutory or
constitutional question beyond debate.” White, 580 U. S.,
at ___ (slip op., at 6) (internal quotation marks omitted).
“In other words, immunity protects all but the plainly
incompetent or those who knowingly violate the law.”
Ibid. (internal quotation marks omitted). This Court has
“ ‘repeatedly told courts—and the Ninth Circuit in particu-
lar—not to define clearly established law at a high level of
generality.’ ”   City and County of San Francisco v.
Sheehan, 575 U. S. ___, ___ (2015) (slip op., at 13) (quoting
Ashcroft v. al-Kidd, 563 U. S. 731, 742 (2011)); see also
Brosseau, supra, at 198–199.
                  Cite as: 584 U. S. ____ (2018)             5

                           Per Curiam

   “[S]pecificity is especially important in the Fourth
Amendment context, where the Court has recognized that
it is sometimes difficult for an officer to determine how the
relevant legal doctrine, here excessive force, will apply to
the factual situation the officer confronts.” Mullenix v.
Luna, 577 U. S. ___, ___ (2015) (per curiam) (slip op., at 5)
(internal quotation marks omitted). Use of excessive force
is an area of the law “in which the result depends very
much on the facts of each case,” and thus police officers
are entitled to qualified immunity unless existing prece-
dent “squarely governs” the specific facts at issue. Id., at
___ (slip op., at 6) (internal quotation marks omitted and
emphasis deleted). Precedent involving similar facts can
help move a case beyond the otherwise “hazy border be-
tween excessive and acceptable force” and thereby provide
an officer notice that a specific use of force is unlaw-
ful. Id., at ___ (slip op., at 12) (internal quotation marks
omitted).
   “Of course, general statements of the law are not inher-
ently incapable of giving fair and clear warning to offic-
ers.” White, 580 U. S., at ___ (slip op., at 7) (internal
quotation marks omitted). But the general rules set forth
in “Garner and Graham do not by themselves create clearly
established law outside an ‘obvious case.’ ” Ibid. Where
constitutional guidelines seem inapplicable or too remote,
it does not suffice for a court simply to state that an officer
may not use unreasonable and excessive force, deny quali-
fied immunity, and then remit the case for a trial on the
question of reasonableness. An officer “cannot be said to
have violated a clearly established right unless the right’s
contours were sufficiently definite that any reasonable
official in the defendant’s shoes would have understood
that he was violating it.” Plumhoff v. Rickard, 572 U. S.
___, ___ (2014) (slip op., at 12). That is a necessary part of
the qualified-immunity standard, and it is a part of the
standard that the Court of Appeals here failed to imple-
6                    KISELA v. HUGHES

                         Per Curiam

ment in a correct way.
   Kisela says he shot Hughes because, although the offic-
ers themselves were in no apparent danger, he believed
she was a threat to Chadwick. Kisela had mere seconds to
assess the potential danger to Chadwick. He was con-
fronted with a woman who had just been seen hacking a
tree with a large kitchen knife and whose behavior was
erratic enough to cause a concerned bystander to call 911
and then flag down Kisela and Garcia. Kisela was sepa-
rated from Hughes and Chadwick by a chain-link fence;
Hughes had moved to within a few feet of Chadwick; and
she failed to acknowledge at least two commands to drop
the knife. Those commands were loud enough that Chad-
wick, who was standing next to Hughes, heard them. This
is far from an obvious case in which any competent officer
would have known that shooting Hughes to protect Chad-
wick would violate the Fourth Amendment.
   The Court of Appeals made additional errors in conclud-
ing that its own precedent clearly established that Kisela
used excessive force. To begin with, “even if a controlling
circuit precedent could constitute clearly established law
in these circumstances, it does not do so here.” Sheehan,
supra, at ___ (slip op., at 13). In fact, the most analogous
Circuit precedent favors Kisela. See Blanford v. Sacra-
mento County, 406 F. 3d 1110 (CA9 2005). In Blanford,
the police responded to a report that a man was walking
through a residential neighborhood carrying a sword and
acting in an erratic manner. Id., at 1112. There, as here,
the police shot the man after he refused their commands
to drop his weapon (there, as here, the man might not
have heard the commands). Id., at 1113. There, as here,
the police believed (perhaps mistakenly), that the man
posed an immediate threat to others. Ibid. There, the
Court of Appeals determined that the use of deadly force
did not violate the Fourth Amendment. Id., at 1119.
Based on that decision, a reasonable officer could have
                 Cite as: 584 U. S. ____ (2018)            7

                          Per Curiam

believed the same thing was true in the instant case.
  In contrast, not one of the decisions relied on by the
Court of Appeals—Deorle v. Rutherford, 272 F. 3d 1272
(CA9 2001), Glenn v. Washington County, 673 F. 3d 864
(CA9 2011), and Harris v. Roderick, 126 F. 3d 1189 (CA9
1997)—supports denying Kisela qualified immunity. As
for Deorle, this Court has already instructed the Court of
Appeals not to read its decision in that case too broadly in
deciding whether a new set of facts is governed by clearly
established law. Sheehan, 572 U. S., at ___–___ (slip op.,
at 13–14). Deorle involved a police officer who shot an
unarmed man in the face, without warning, even though
the officer had a clear line of retreat; there were no by-
standers nearby; the man had been “physically compliant
and generally followed all the officers’ instructions”; and
he had been under police observation for roughly 40
minutes. 272 F. 3d, at 1276, 1281–1282. In this case,
by contrast, Hughes was armed with a large knife; was
within striking distance of Chadwick; ignored the officers’
orders to drop the weapon; and the situation unfolded in
less than a minute. “Whatever the merits of the decision
in Deorle, the differences between that case and the case
before us leap from the page.” Sheehan, supra, at ___ (slip
op., at 14).
  Glenn, which the panel described as “[t]he most analo-
gous Ninth Circuit case,” 862 F. 3d, at 783, was decided
after the shooting at issue here. Thus, Glenn “could not
have given fair notice to [Kisela]” because a reasonable
officer is not required to foresee judicial decisions that do
not yet exist in instances where the requirements of the
Fourth Amendment are far from obvious. Brosseau, 543
U. S., at 200, n. 4. Glenn was therefore “of no use in the
clearly established inquiry.” Brosseau, supra, at 200, n. 4.
Other judges brought this mistaken or misleading citation
to the panel’s attention while Kisela’s petition for rehear-
ing en banc was pending before the Court of Appeals. 862
8                     KISELA v. HUGHES

                          Per Curiam

F.3d, at 795, n. 2 (Ikuta, J., dissenting from denial of
rehearing en banc). The panel then amended its opinion,
but nevertheless still attempted to “rely on Glenn as illus-
trative, not as indicative of the clearly established law in
2010.” Id., at 784, n. 2 (majority opinion). The panel
failed to explain the difference between “illustrative” and
“indicative” precedent, and none is apparent.
   The amended opinion also asserted, for the first time
and without explanation, that the Court of Appeals’ deci-
sion in Harris clearly established that the shooting here
was unconstitutional. Id., at 785. The new mention of
Harris replaced a reference in the panel’s first opinion to
Glenn—the case that postdated the shooting at issue here.
Compare 841 F. 3d 1081, 1090 (CA9 2016) (“As indicated
by Glenn and Deorle, . . . that right was clearly estab-
lished”), with 862 F. 3d, at 785 (“As indicated by Deorle
and Harris, . . . that right was clearly established”).
   The panel’s reliance on Harris “does not pass the
straight-face test.” 862 F. 3d, at 797 (opinion of Ikuta, J.).
In Harris, the Court of Appeals determined that an FBI
sniper, who was positioned safely on a hilltop, used exces-
sive force when he shot a man in the back while the man
was retreating to a cabin during what has been referred to
as the Ruby Ridge standoff. 126 F. 3d, at 1202–1203.
Suffice it to say, a reasonable police officer could miss the
connection between the situation confronting the sniper at
Ruby Ridge and the situation confronting Kisela in
Hughes’ front yard.
   For these reasons, the petition for certiorari is granted;
the judgment of the Court of Appeals is reversed; and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.
                 Cite as: 584 U. S. ____ (2018)           1

                  SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
          ANDREW KISELA v. AMY HUGHES
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT

              No. 17–467.   Decided April 2, 2018


   JUSTICE SOTOMAYOR, with whom JUSTICE GINSBURG
joins, dissenting.
   Officer Andrew Kisela shot Amy Hughes while she was
speaking with her roommate, Sharon Chadwick, outside of
their home. The record, properly construed at this stage,
shows that at the time of the shooting: Hughes stood
stationary about six feet away from Chadwick, appeared
“composed and content,” Appellant’s Excerpts of Record
109 (Record), and held a kitchen knife down at her side
with the blade facing away from Chadwick. Hughes was
nowhere near the officers, had committed no illegal act,
was suspected of no crime, and did not raise the knife in
the direction of Chadwick or anyone else. Faced with
these facts, the two other responding officers held their
fire, and one testified that he “wanted to continue trying
verbal command[s] and see if that would work.” Id., at
120. But not Kisela. He thought it necessary to use deadly
force, and so, without giving a warning that he would
open fire, he shot Hughes four times, leaving her seriously
injured.
   If this account of Kisela’s conduct sounds unreasonable,
that is because it was. And yet, the Court today insulates
that conduct from liability under the doctrine of qualified
immunity, holding that Kisela violated no “clearly estab­
lished” law. See ante, at 5–6. I disagree. Viewing the
facts in the light most favorable to Hughes, as the Court
must at summary judgment, a jury could find that Kisela
violated Hughes’ clearly established Fourth Amendment
rights by needlessly resorting to lethal force. In holding
2                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

otherwise, the Court misapprehends the facts and misap­
plies the law, effectively treating qualified immunity as an
absolute shield. I therefore respectfully dissent.
                               I
   This case arrives at our doorstep on summary judgment,
so we must “view the evidence . . . in the light most favor­
able to” Hughes, the nonmovant, “with respect to the
central facts of this case.” Tolan v. Cotton, 572 U. S. ___,
___ (2014) (per curiam) (slip op., at 8). The majority pur­
ports to honor this well-settled principle, but its efforts fall
short. Although the majority sets forth most of the rele­
vant events that transpired, it conspicuously omits several
critical facts and draws premature inferences that bear on
the qualified-immunity inquiry. Those errors are fatal to
its analysis, because properly construing all of the facts in
the light most favorable to Hughes, and drawing all infer­
ences in her favor, a jury could find that the following
events occurred on the day of Hughes’ encounter with the
Tucson police.
   On May 21, 2010, Kisela and Officer-in-Training Alex
Garcia received a “ ‘check welfare’ ” call about a woman
chopping away at a tree with a knife. 862 F. 3d 775, 778
(CA9 2016). They responded to the scene, where they
were informed by the person who had placed the call (not
Chadwick) that the woman with the knife had been acting
“erratically.” Ibid. A third officer, Lindsay Kunz, later
joined the scene. The officers observed Hughes, who
matched the description given to the officers of the woman
alleged to have been cutting the tree, emerge from a house
with a kitchen knife in her hand. Hughes exited the front
door and approached Chadwick, who was standing outside
in the driveway.
   Hughes then stopped about six feet from Chadwick,
holding the kitchen knife down at her side with the blade
pointed away from Chadwick. Hughes and Chadwick
                 Cite as: 584 U. S. ____ (2018)            3

                   SOTOMAYOR, J., dissenting

conversed with one another; Hughes appeared “composed
and content,” Record 109, and did not look angry. See 862
F. 3d, at 778. At no point during this exchange did
Hughes raise the kitchen knife or verbally threaten to
harm Chadwick or the officers. Chadwick later averred
that, during the incident, she was never in fear of Hughes
and “was not the least bit threatened by the fact that
[Hughes] had a knife in her hand” and that Hughes “never
acted in a threatening manner.” Record 110–111. The
officers did not observe Hughes commit any crime, nor was
Hughes suspected of committing one. See 862 F. 3d, at
780.
   Nevertheless, the officers hastily drew their guns and
ordered Hughes to drop the knife. The officers gave that
order twice, but the commands came “in quick succession.”
Id., at 778. The evidence in the record suggests that
Hughes may not have heard or understood the officers’
commands and may not have been aware of the officers’
presence at all. Record 109–110, 195, 323–324 (Officer
Kunz’s testimony that “it seemed as though [Hughes]
didn’t even know we were there,” and “[i]t was like she
didn’t hear us almost”); id., at 304 (Officer Garcia’s testi­
mony that Hughes acted “almost as if we weren’t there”).
Although the officers were in uniform, they never verbally
identified themselves as law enforcement officers.
   Kisela did not wait for Hughes to register, much less
respond to, the officers’ rushed commands. Instead, Kisela
immediately and unilaterally escalated the situation.
Without giving any advance warning that he would shoot,
and without attempting less dangerous methods to deesca­
late the situation, he dropped to the ground and shot four
times at Hughes (who was stationary) through a chain-
link fence. After being shot, Hughes fell to the ground,
screaming and bleeding from her wounds. She looked at
the officers and asked, “ ‘Why’d you shoot me?’ ” Id., at
308. Hughes was immediately transported to the hospital,
4                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

where she required treatment for her injuries. Kisela
alone resorted to deadly force in this case. Confronted
with the same circumstances as Kisela, neither of his
fellow officers took that drastic measure.
                              II
   Police officers are not entitled to qualified immunity if
“(1) they violated a federal statutory or constitutional
right, and (2) the unlawfulness of their conduct was ‘clearly
established at the time.’ ” District of Columbia v. Wesby,
583 U. S. ___, ___ (2018) (slip op., at 13) (quoting Reichle v.
Howards, 566 U. S. 658, 664 (2012)). Faithfully applying
that well-settled standard, the Ninth Circuit held that a
jury could find that Kisela violated Hughes’ clearly estab­
lished Fourth Amendment rights. That conclusion was
correct.
                               A
   I begin with the first step of the qualified-immunity
inquiry: whether there was a violation of a constitutional
right. Hughes alleges that Kisela violated her Fourth
Amendment rights by deploying excessive force against
her. In assessing such a claim, courts must ask “whether
the officers’ actions are ‘objectively reasonable’ in light of
the facts and circumstances confronting them.” Graham
v. Connor, 490 U. S. 386, 397 (1989). That inquiry “re­
quires careful attention to the facts and circumstances of
each particular case, including the severity of the crime at
issue, whether the suspect poses an immediate threat to
the safety of the officers or others, and whether he is
actively resisting arrest or attempting to evade arrest by
flight.” Id., at 396; see also Tennessee v. Garner, 471 U. S.
1, 11 (1985). All of those factors (and others) support the
Ninth Circuit’s conclusion that a jury could find that
Kisela’s use of deadly force was objectively unreasonable.
862 F. 3d, at 779–782. Indeed, the panel’s resolution of
                 Cite as: 584 U. S. ____ (2018)           5

                   SOTOMAYOR, J., dissenting

this question was so convincing that not a single judge on
the Ninth Circuit, including the seven who dissented from
denial of rehearing en banc, expressly disputed that con­
clusion. See id., at 791–799 (opinion of Ikuta, J.). Neither
does the majority here, which simply assumes without
deciding that “a Fourth Amendment violation occurred.”
Ante, at 4.
   First, Hughes committed no crime and was not suspected
of committing a crime. The officers were responding to a
“check welfare” call, which reported no criminal activity,
and the officers did not observe any illegal activity while
at the scene. The mere fact that Hughes held a kitchen
knife down at her side with the blade pointed away from
Chadwick hardly elevates the situation to one that justi­
fies deadly force.
   Second, a jury could reasonably conclude that Hughes
presented no immediate or objective threat to Chadwick or
the other officers. It is true that Kisela had received a
report that a woman matching Hughes’ description had
been acting erratically. But the police officers themselves
never witnessed any erratic conduct. Instead, when
viewed in the light most favorable to Hughes, the record
evidence of what the police encountered paints a calmer
picture. It shows that Hughes was several feet from
Chadwick and even farther from the officers, she never
made any aggressive or threatening movements, and she
appeared “composed and content” during the brief
encounter.
   Third, Hughes did not resist or evade arrest. Based on
this record, there is significant doubt as to whether she
was aware of the officers’ presence at all, and evidence
suggests that Hughes did not hear the officers’ swift com­
mands to drop the knife.
   Finally, the record suggests that Kisela could have, but
failed to, use less intrusive means before deploying deadly
force. 862 F. 3d, at 781. For instance, Hughes submitted
6                    KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

expert testimony concluding that Kisela should have used
his Taser and that shooting his gun through the fence was
dangerous because a bullet could have fragmented against
the fence and hit Chadwick or his fellow officers. Ibid.; see
also Bryan v. MacPherson, 630 F. 3d 805, 831 (CA9 2010)
(noting that “police are required to consider what other
tactics if any were available to effect the arrest” and
whether there are “clear, reasonable, and less intrusive
alternatives” (internal quotation marks and alteration
omitted)). Consistent with that assessment, the other two
officers on the scene declined to fire at Hughes, and one of
them explained that he was inclined to use “some of the
lesser means” than shooting, including verbal commands,
because he believed there was time “[t]o try to talk
[Hughes] down.” Record 120–121. That two officers on
the scene, presented with the same circumstances as
Kisela, did not use deadly force reveals just how unneces­
sary and unreasonable it was for Kisela to fire four shots
at Hughes. See Plumhoff v. Rickard, 572 U. S. ___, ___
(2014) (slip op., at 8) (“We analyze [the objective reason-
ableness] question from the perspective of a reasonable
officer on the scene” (internal quotation marks omitted)).
  Taken together, the foregoing facts would permit a jury
to conclude that Kisela acted outside the bounds of the
Fourth Amendment by shooting Hughes four times.
                               B
  Rather than defend the reasonableness of Kisela’s con­
duct, the majority sidesteps the inquiry altogether and
focuses instead on the “clearly established” prong of the
qualified-immunity analysis. Ante, at 4. To be “ ‘clearly
established’ . . . [t]he contours of the right must be suffi­
ciently clear that a reasonable official would understand
that what he is doing violates that right.” Anderson v.
Creighton, 483 U. S. 635, 640 (1987). That standard is not
nearly as onerous as the majority makes it out to be. As
                  Cite as: 584 U. S. ____ (2018)             7

                    SOTOMAYOR, J., dissenting

even the majority must acknowledge, ante, at 4, this Court
has long rejected the notion that “an official action is
protected by qualified immunity unless the very action in
question has previously been held unlawful,” Anderson,
483 U. S., at 640. “[O]fficials can still be on notice that
their conduct violates established law even in novel factual
circumstances.” Hope v. Pelzer, 536 U. S. 730, 741 (2002).
At its core, then, the “clearly established” inquiry boils
down to whether Kisela had “fair notice” that he acted
unconstitutionally. See ibid.; Brosseau v. Haugen, 543
U. S. 194, 198 (2004) (per curiam) (“[T]he focus” of quali­
fied immunity “is on whether the officer had fair notice
that her conduct was unlawful”).
   The answer to that question is yes. This Court’s prece­
dents make clear that a police officer may only deploy
deadly force against an individual if the officer “has prob­
able cause to believe that the [person] poses a threat of
serious physical harm, either to the officer or to others.”
Garner, 471 U. S., at 11; see also Graham, 490 U. S., at
397. It is equally well established that any use of lethal
force must be justified by some legitimate governmental
interest. See Scott v. Harris, 550 U. S. 372, 383 (2007);
Mullenix v. Luna, 577 U. S. ___, ___–___ (2015)
(SOTOMAYOR, J., dissenting) (slip op., at 2–3). Consistent
with those clearly established principles, and contrary to
the majority’s conclusion, Ninth Circuit precedent predat­
ing these events further confirms that Kisela’s conduct
was clearly unreasonable. See Brosseau, 543 U. S., at 199
(“[A] body of relevant case law” may “ ‘clearly establish’ ”
the violation of a constitutional right); Ashcroft v. al-Kidd,
563 U. S. 731, 746 (2011) (KENNEDY, J., concurring)
(“[Q]ualified immunity is lost when plaintiffs point either
to ‘cases of controlling authority in their jurisdiction at the
time of the incident’ or to ‘a consensus of cases of persua­
sive authority such that a reasonable officer could not
have believed that his actions were lawful’ ” (quoting
8                     KISELA v. HUGHES

                    SOTOMAYOR, J., dissenting

Wilson v. Layne, 526 U. S. 603, 617 (1999))). Because
Kisela plainly lacked any legitimate interest justifying the
use of deadly force against a woman who posed no objec­
tive threat of harm to officers or others, had committed no
crime, and appeared calm and collected during the police
encounter, he was not entitled to qualified immunity.
   The Ninth Circuit’s opinion in Deorle v. Rutherford, 272
F. 3d 1272 (2001) proves the point. In that case, the police
encountered a man who had reportedly been acting “errat­
ically.” Id., at 1276. The man was “verbally abusive,”
shouted “ ‘kill me’ ” at the officers, screamed that he would
“ ‘kick [the] ass’ ” of one of the officers, and “brandish[ed] a
hatchet at a police officer,” ultimately throwing it “into a
clump of trees when told to put it down.” Id., at 1276–
1277. The officers also observed the man carrying an
unloaded crossbow in one hand and what appeared to be
“a can or a bottle of lighter fluid in the other.” Id., at
1277. The man discarded the crossbow when instructed to
do so by the police and then steadily walked toward one of
the officers. Ibid. In response, that officer, without giving
a warning, shot the man in the face with beanbag rounds.
Id., at 1278. The man suffered serious injuries, including
multiple fractures to his cranium and the loss of his left
eye. Ibid.
   The Ninth Circuit denied qualified immunity to the
officer, concluding that his use of force was objectively
unreasonable under clearly established law. Id., at 1285–
1286. The court held, “Every police officer should know
that it is objectively unreasonable to shoot . . . an unarmed
man who: has committed no serious offense, is mentally or
emotionally disturbed, has been given no warning of the
imminent use of such a significant degree of force, poses
no risk of flight, and presents no objectively reasonable
threat to the safety of the officer or other individuals.” Id.,
at 1285.
   The same holds true here. Like the man in Deorle,
                 Cite as: 584 U. S. ____ (2018)           9

                   SOTOMAYOR, J., dissenting

Hughes committed no serious crime, had been given no
warning of the imminent use of force, posed no risk of
flight, and presented no objectively reasonable threat to
the safety of officers or others. In fact, Hughes presented
even less of a danger than the man in Deorle, for, unlike
him, she did not threaten to “kick [their] ass,” did not
appear agitated, and did not raise her kitchen knife or
make any aggressive gestures toward the police or Chad­
wick. If the police officers acted unreasonably in shooting
the agitated, screaming man in Deorle with beanbag bul­
lets, a fortiori Kisela acted unreasonably in shooting the
calm-looking, stationary Hughes with real bullets. In my
view, Deorle and the precedent it cites place the unlawful­
ness of Kisela’s conduct “ ‘beyond debate.’ ” Wesby, 583
U. S., at ___ (slip op., at 15).
   The majority strains mightily to distinguish Deorle, to
no avail. It asserts, for instance, that, unlike the man in
Deorle, Hughes was “armed with a large knife.” Ante, at 7.
But that is not a fair characterization of the record, par­
ticularly at this procedural juncture. Hughes was not
“armed” with a knife. She was holding “a kitchen knife—
an everyday household item which can be used as a
weapon but ordinarily is a tool for safe, benign purposes”—
down at her side with the blade pointed away from Chad­
wick. 862 F. 3d, at 788 (Berzon, J., concurring in denial of
rehearing en banc). Hughes also spoke calmly with
Chadwick during the events at issue, did not raise the
knife, and made no other aggressive movements, under­
mining any suggestion that she was a threat to Chadwick
or anyone else. Similarly, the majority asserts that
Hughes was “within striking distance” of Chadwick, ante,
at 7, but that stretches the facts and contravenes this
Court’s repeated admonition that inferences must be
drawn in the exact opposite direction, i.e., in favor of
Hughes. See Tolan, 572 U. S., at ___ (slip op., at 8). The
facts, properly viewed, show that, when she was shot,
10                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

Hughes had stopped and stood still about six feet away
from Chadwick. Whether Hughes could “strik[e]” Chad­
wick from that particular distance, even though the kitchen
knife was held down at her side, is an inference that
should be drawn by the jury, not this Court.
   The majority next posits that Hughes, unlike the man in
Deorle, “ignored the officers’ orders to drop the” kitchen
knife. Ante, at 7. Yet again, the majority here draws
inferences in favor of Kisela, instead of Hughes. The
available evidence would allow a reasonable jury to find
that Hughes did not hear or register the officers’ swift
commands and that Kisela, like his fellow officers on the
scene, should have realized that as well. See supra, at 3–
4. Accordingly, at least at the summary-judgment stage,
the Court is mistaken in distinguishing Deorle based on
Hughes’ ostensible disobedience to the officers’ directives.
   The majority also implies that Deorle is distinguishable
because the police in that case observed the man over a
40-minute period, whereas the situation here unfolded in
less than a minute. Ante, at 7. But that fact favors
Hughes, not Kisela. The only reason this case unfolded in
such an abrupt timeframe is because Kisela, unlike his
fellow officer, showed no interest in trying to talk further
to Hughes or use a “lesser means” of force. See Record
120–121, 304.
   Finally, the majority passingly notes that “this Court
has already instructed the Court of Appeals not to read
[Deorle] too broadly.” Ante, at 7 (citing City and County of
San Francisco v. Sheehan, 575 U. S. ___, ___–___ (2015)
(slip op., at 13–14)). But the Court in Sheehan concluded
that Deorle was plainly distinguishable because, unlike in
Deorle, the officers there confronted a woman who “was
dangerous, recalcitrant, law-breaking, and out of sight.”
575 U. S., at ___ (slip op., at 14). As explained above,
however, Hughes was none of those things: She did not
threaten or endanger the officers or Chadwick, she did not
                      Cite as: 584 U. S. ____ (2018)                    11

                       SOTOMAYOR, J., dissenting

break any laws, and she was visible to the officers on the
scene. See supra, at 2–4. Thus, there simply is no basis
for the Court’s assertion that “ ‘the differences between
[Deorle] and the case before us leap from the page.’ ” Ante,
at 7 (quoting Sheehan, 575 U. S., at ___ (slip op., at 14)).
   Deorle, moreover, is not the only case that provided fair
notice to Kisela that shooting Hughes under these circum­
stances was unreasonable. For instance, the Ninth Circuit
has held that the use of deadly force against an individual
holding a semiautomatic rifle was unconstitutional where
the individual “did not point the gun at the officers and
apparently was not facing them when they shot him the
first time.” Curnow v. Ridgecrest Police, 952 F. 2d 321,
325 (1991). Similarly, in Harris v. Roderick, 126 F. 3d
1189 (1997), the Ninth Circuit held that the officer unrea­
sonably used deadly force against a man who, although
armed, made “no threatening movement” or “aggressive
move of any kind.” Id., at 1203.* Both Curnow and Har-
ris establish that, where, as here, an individual with a
weapon poses no objective and immediate threat to officers
or third parties, law enforcement cannot resort to exces­
sive force. See Harris, 126 F. 3d, at 1201 (“Law enforce­
ment officers may not shoot to kill unless, at a minimum,
the suspect presents an immediate threat to the officers,
or is fleeing and his escape will result in a serious threat
of injury to persons”).
   If all that were not enough, decisions from several other
Circuits illustrate that the Fourth Amendment clearly
——————
  * The majority insists that reliance on Harris fails the “ ‘straight-face
test’ ” because Harris involved an FBI sniper on a hilltop who shot a
man while he was retreating to a cabin during a standoff. Ante, at 8
(quoting 862 F. 3d, at 797 (opinion of Ikuta, J.)). If anything, though,
the context of Harris could be viewed as more dangerous than the
context here because, unlike Hughes, the suspect in Harris had en­
gaged in a firefight with other officers the previous day, during which
an officer was shot. See 126 F. 3d, at 1193–1194.
12                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

forbids the use of deadly force against a person who is
merely holding a knife but not threatening anyone with it.
See, e.g., McKinney v. DeKalb County, 997 F. 2d 1440,
1442 (CA11 1993) (affirming denial of summary judgment
based on qualified immunity to officer who shot a person
holding a butcher knife in one hand and a foot-long stick
in the other, where the person threw the stick and began
to rise from his seated position); Reyes v. Bridgwater, 362
Fed. Appx. 403, 404–405 (CA5 2010) (reversing grant of
summary judgment based on qualified immunity to officer
who shot a person holding a kitchen knife in his apart­
ment entryway, even though he refused to follow the
officer’s multiple commands to drop the knife); Duong v.
Telford Borough, 186 Fed. Appx. 214, 215, 217 (CA3 2006)
(affirming denial of summary judgment based on qualified
immunity to officer who shot a person holding a knife
because a reasonable jury could conclude that the plaintiff
was sitting down and pointing the knife away from the
officer at the time he was shot and had not received any
warnings to drop the knife).
  Against this wall of case law, the majority points to a
single Ninth Circuit decision, Blanford v. Sacramento
County, 406 F. 3d 1110 (2005), as proof that Kisela rea­
sonably could have believed that Hughes posed an imme­
diate danger. But Blanford involved far different circum­
stances. In that case, officers observed a man walking
through a neighborhood brandishing a 2½-foot cavalry
sword; officers commanded the man to drop the sword,
identified themselves as police, and warned “ ‘We’ll shoot.’ ”
Id., at 1112–1113. The man responded with “a loud growl­
ing or roaring sound,” which increased the officers’ concern
that he posed a risk of harm. Id., at 1113. In an effort to
“evade [police] authority,” the man, while still wielding the
sword, tried to enter a home, thus prompting officers to
open fire to protect anyone who might be inside. Id., at
1113, 1118. The Ninth Circuit concluded that use of deadly
                 Cite as: 584 U. S. ____ (2018)           13

                   SOTOMAYOR, J., dissenting

force was reasonable in those circumstances. See id., at
1119.
  This case differs significantly from Blanford in several
key respects. Unlike the man in Blanford, Hughes held a
kitchen knife down by her side, as compared to a 2½-foot
sword; she appeared calm and collected, and did not make
threatening noises or gestures toward the officers on the
scene; she stood still in front of her own home, and was not
wandering about the neighborhood, evading law enforce­
ment, or attempting to enter another house. Moreover,
unlike the officers in Blanford, Kisela never verbally
identified himself as an officer and never warned Hughes
that he was going to shoot before he did so. Given these
significant differences, no reasonable officer would believe
that Blanford justified Kisela’s conduct. The majority’s
conclusion to the contrary is fanciful.
                         *     *     *
   In sum, precedent existing at the time of the shooting
clearly established the unconstitutionality of Kisela’s
conduct. The majority’s decision, no matter how much it
says otherwise, ultimately rests on a faulty premise: that
those cases are not identical to this one. But that is not
the law, for our cases have never required a factually
identical case to satisfy the “clearly established” standard.
Hope, 536 U. S., at 739. It is enough that governing law
places “the constitutionality of the officer’s conduct beyond
debate.” Wesby, 583 U. S., at ___ (slip op., at 13) (internal
quotation marks omitted). Because, taking the facts in the
light most favorable to Hughes, it is “beyond debate” that
Kisela’s use of deadly force was objectively unreasonable,
he was not entitled to summary judgment on the basis of
qualified immunity.
                          III
  For the foregoing reasons, it is clear to me that the
14                   KISELA v. HUGHES

                   SOTOMAYOR, J., dissenting

Court of Appeals got it right. But even if that result were
not so clear, I cannot agree with the majority’s apparent
view that the decision below was so manifestly incorrect as
to warrant “the extraordinary remedy of a summary re­
versal.” Major League Baseball Players Assn. v. Garvey,
532 U. S. 504, 512–513 (2001) (Stevens, J., dissenting). “A
summary reversal is a rare disposition, usually reserved
by this Court for situations in which the law is settled and
stable, the facts are not in dispute, and the decision below
is clearly in error.” Schweiker v. Hansen, 450 U. S. 785,
791 (1981) (Marshall, J., dissenting); Office of Personnel
Management v. Richmond, 496 U. S. 414, 422 (1990)
(“Summary reversals of courts of appeals are unusual
under any circumstances”). This is not such a case. The
relevant facts are hotly disputed, and the qualified-
immunity question here is, at the very best, a close call.
Rather than letting this case go to a jury, the Court de­
cides to intervene prematurely, purporting to correct an
error that is not at all clear.
   This unwarranted summary reversal is symptomatic of
“a disturbing trend regarding the use of this Court’s re­
sources” in qualified-immunity cases. Salazar-Limon v.
Houston, 581 U. S. ___, ___ (2017) (SOTOMAYOR, J., dis­
senting from denial of certiorari) (slip op., at 8). As I have
previously noted, this Court routinely displays an un­
flinching willingness “to summarily reverse courts for
wrongly denying officers the protection of qualified im­
munity” but “rarely intervene[s] where courts wrongly
afford officers the benefit of qualified immunity in these
same cases.” Id., at ___–___ (slip op., at 8–9); see also
Baude, Is Qualified Immunity Unlawful? 106 Cal. L. Rev.
45, 82 (2018) (“[N]early all of the Supreme Court’s quali­
fied immunity cases come out the same way—by finding
immunity for the officials”); Reinhardt, The Demise of
Habeas Corpus and the Rise of Qualified Immunity: The
Court’s Ever Increasing Limitations on the Development
                 Cite as: 584 U. S. ____ (2018)          15

                   SOTOMAYOR, J., dissenting

and Enforcement of Constitutional Rights and Some Par­
ticularly Unfortunate Consequences, 113 Mich. L. Rev.
1219, 1244–1250 (2015). Such a one-sided approach to
qualified immunity transforms the doctrine into an abso­
lute shield for law enforcement officers, gutting the deter­
rent effect of the Fourth Amendment.
   The majority today exacerbates that troubling asym­
metry. Its decision is not just wrong on the law; it also
sends an alarming signal to law enforcement officers and
the public. It tells officers that they can shoot first and
think later, and it tells the public that palpably unreason­
able conduct will go unpunished. Because there is noth-
ing right or just under the law about this, I respectfully
dissent.

```

---

## GROUP: _overhaul2/lake/cases/Mathis v. United States (1968).json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Mathis v. United States (1968)"
type: case
citation: "391 U.S. 1 (1968)"
parallel_cite: "88 S. Ct. 1503; 20 L. Ed. 2d 381; 2 C.B. 903; 21 A.F.T.R.2d (RIA) 1251"
neutral_cite: 1968 U.S. LEXIS 3108
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-05-06
docket: 726
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1968-05-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Mathis v. United States (1968)"
  varies_by_point: true
  scope_note: "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis."
  point_overrides:
    - point: legacy-limited-mathis-v-united-states-1968
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Howes v. Fields
          cluster_id: 623144
          cite: 565 U.S. 499
          field_ii: limited
      scope_note: "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107676/mathis-v-united-states/"
  cluster_id: 107676
  opinion_id: 9423682
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Howes v. Fields]]", "[[Orozco v. Texas]]", "[[Beckwith v. United States]]"]
aliases: ["Mathis v. United States"]
tags: ["case", "fifth-amendment", "miranda", "custody", "prison-inmate", "irs"]
holding: "Miranda warnings are required when a person already in custody (here, serving a prison sentence) is interrogated by officers, even though the questioning concerns an entirely separate matter and even though it is a routine tax investigation; the reason the person is in custody does not curtail the warnings."
lake:
  record_id: "Mathis v. United States (1968)"
  status: under_review
  projected_at: 2026-07-06
---

# Mathis v. United States (1968)

*391 U.S. 1 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — by [[Howes v. Fields]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While Mathis was serving a state sentence in prison, a federal revenue agent interviewed him about his individual income-tax returns, obtaining documents and oral statements without giving any [[Miranda and Custodial Interrogation|Miranda warnings]]. Those statements were later used to convict him in federal court of knowingly filing false claims for tax refunds. At trial he sought, unsuccessfully, to suppress the statements under [[Miranda v. Arizona]]; the District Court and Fifth Circuit rejected the claim.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] were required before a revenue agent questioned a person who was already in custody — serving a sentence for a separate offense — in the course of a tax investigation.

## Rule
Yes. The Court rejected the Government's two distinctions. "The Government here seeks to escape application of the *Miranda* warnings on two arguments: (1) that these questions were asked as a part of a routine tax investigation . . . and (2) that the petitioner had not been put in jail by the officers questioning him, but was there for an entirely separate offense. These differences are too minor and shadowy to justify a departure from the well-considered conclusions of *Miranda* with reference to warnings to be given to a person held in custody." — 391 U.S. at 4. ^pin-4

The reason for custody is irrelevant: "There is no substance to such a distinction . . . . We find nothing in the *Miranda* opinion which calls for a curtailment of the warnings to be given persons under interrogation by officers based on the reason why the person is in custody." — *Id.* at 4–5. ^pin-5

## Application
Mathis was indisputably "in custody" — he was serving a prison sentence — and the revenue agent's questioning produced strongly incriminating statements used against him. That the questioning arose from a "routine tax investigation" did not exempt it (tax investigations frequently become criminal prosecutions, as this one did), and that he was imprisoned for a different offense did not remove Miranda's protection. Because no warnings were given, the statements were inadmissible and the conviction had to be reversed.

## Conclusion
Miranda applied to the custodial interrogation; the failure to warn required reversal. The judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**; **limited by** [[Howes v. Fields]].
- *Mathis*'s core holding remains good law: a person already in custody does not lose Miranda's protection because the questioning concerns a *separate* matter. But the broad reading that **incarceration itself always constitutes Miranda "custody"** was **rejected/limited** in [[Howes v. Fields]], 565 U.S. 499 (2012), which holds that questioning an inmate requires a totality-of-circumstances custody analysis (imprisonment alone is not enough). The custody-not-focus principle was also developed in [[Beckwith v. United States]], and the in-home custody analog appears in [[Orozco v. Texas]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Mathis v. United States*, 391 U.S. 1 (1968) — https://www.courtlistener.com/opinion/107676/mathis-v-united-states/ — pinpoints: 4, 5.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "18401ecac52bf97d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mathis v. United States (1968)"}, "payload": {"all": [{"cite": "391 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "391"}, {"cite": "88 S. Ct. 1503", "page": "1503", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 381", "page": "381", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 3108", "page": "3108", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}, {"cite": "2 C.B. 903", "page": "903", "reporter": "C.B.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "2"}, {"cite": "21 A.F.T.R.2d (RIA) 1251", "page": "1251", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "21"}], "display": "391 U.S. 1", "official": {"cite": "391 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "391"}, "official_selection_present": true, "record_id": "Mathis v. United States (1968)"}}
{"assertion_id": "8a23edce7294bd3c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-4", "record_id": "Mathis v. United States (1968)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-4", "pinpoint_status": "slip-only", "quote": "--- # Mathis v. United States (1968) *391 U.S. 1 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — by [[Howes v. Fields]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While Mathis was serving a state sentence in prison, a federal revenue agent interviewed him about his individual income-tax returns, obtaining documents and oral statements without giving any Miranda warnings. Those statements were later used to convict him in federal court of knowingly filing false claims for tax refunds. At trial he sought, unsuccessfully, to suppress the statements under [[Miranda v. Arizona]]; the District Court and Fifth Circuit rejected the claim. ## Issue Whether Miranda warnings were required before a revenue agent questioned a person who was already in custody — serving a sentence for a separate offense — in the course of a tax investigation. ## Rule Yes. The Court rejected the Government's two distinctions.", "quote_fidelity": "mismatch", "record_id": "Mathis v. United States (1968)", "star_marker": null}}
{"assertion_id": "8a324f1c08d7b225", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-5", "record_id": "Mathis v. United States (1968)"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-5", "pinpoint_status": "slip-only", "quote": "There is no substance to such a distinction . . . . We find nothing in the *Miranda* opinion which calls for a curtailment of the warnings to be given persons under interrogation by officers based on the reason why the person is in custody.", "quote_fidelity": "mismatch", "record_id": "Mathis v. United States (1968)", "star_marker": null}}
{"assertion_id": "a3344e5096a3d4f8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mathis v. United States (1968)"}, "payload": {"as_of_content": "1968-05-06", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Mathis v. United States (1968)", "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) — prison questioning now takes a totality-of-circumstances custody analysis.", "varies_by_point": true}}
```

### lake record — Mathis v. United States (1968)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mathis v. United States (1968)",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Mathis v. United States",
    "case_name_short": "Mathis",
    "case_name_full": "Mathis v. United States",
    "input_case_name": "Mathis v. United States (1968)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-05-06",
    "year": 1968,
    "docket": "726",
    "cluster_id": 107676,
    "lead_opinion_id": 9423682,
    "sibling_ids": [
      107676,
      9423682,
      9423683
    ],
    "absolute_url": "/opinion/107676/mathis-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "391 U.S. 1",
      "volume": "391",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1503",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 381",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 C.B. 903",
        "volume": "2",
        "reporter": "C.B.",
        "page": "903",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 A.F.T.R.2d (RIA) 1251",
        "volume": "21",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1251",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 3108",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3108",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "391 U.S. 1",
        "volume": "391",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1503",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1503",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 381",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 3108",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3108",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 C.B. 903",
        "volume": "2",
        "reporter": "C.B.",
        "page": "903",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "21 A.F.T.R.2d (RIA) 1251",
        "volume": "21",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1251",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "391 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "391 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-4",
      "page": null,
      "quote": "--- # Mathis v. United States (1968) *391 U.S. 1 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* \u2014 by [[Howes v. Fields]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While Mathis was serving a state sentence in prison, a federal revenue agent interviewed him about his individual income-tax returns, obtaining documents and oral statements without giving any Miranda warnings. Those statements were later used to convict him in federal court of knowingly filing false claims for tax refunds. At trial he sought, unsuccessfully, to suppress the statements under [[Miranda v. Arizona]]; the District Court and Fifth Circuit rejected the claim. ## Issue Whether Miranda warnings were required before a revenue agent questioned a person who was already in custody \u2014 serving a sentence for a separate offense \u2014 in the course of a tax investigation. ## Rule Yes. The Court rejected the Government's two distinctions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-5",
      "page": null,
      "quote": "There is no substance to such a distinction . . . . We find nothing in the *Miranda* opinion which calls for a curtailment of the warnings to be given persons under interrogation by officers based on the reason why the person is in custody.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1968-05-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mathis v. United States (1968)",
    "varies_by_point": true,
    "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) \u2014 prison questioning now takes a totality-of-circumstances custody analysis.",
    "point_overrides": [
      {
        "point": "legacy-limited-mathis-v-united-states-1968",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Howes v. Fields",
            "cluster_id": 623144,
            "cite": "565 U.S. 499",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Holding stands: Miranda is not lost because in-custody questioning concerns a separate/unrelated matter (here, an IRS interview of a state prisoner). But the broad reading that incarceration itself is always Miranda 'custody' was rejected/limited by Howes v. Fields, 565 U.S. 499 (2012) \u2014 prison questioning now takes a totality-of-circumstances custody analysis."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": "565 U.S. 499",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph Michael Moultrie",
          "cluster_id": 4405157,
          "cite": [
            "224 So. 3d 349",
            "2017 La. LEXIS 1382",
            "2017 WL 2836066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ledbetter",
          "cluster_id": 6294956,
          "cite": [
            "47 Misc. 3d 336",
            "998 N.Y.S.2d 286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Passino",
          "cluster_id": 5899747,
          "cite": [
            "53 A.D.3d 204",
            "861 N.Y.S.2d 168"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
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
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harper",
          "cluster_id": 2382899,
          "cite": [
            "613 A.2d 945",
            "1992 Me. LEXIS 202"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America David E. Mitchell, Revenue Office of the Internal Revenue Service v. Roger L. Sharp",
          "cluster_id": 552785,
          "cite": [
            "920 F.2d 1167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ingersoll v. Palmer",
          "cluster_id": 2604190,
          "cite": [
            "743 P.2d 1299",
            "43 Cal. 3d 1321",
            "241 Cal. Rptr. 42",
            "1987 Cal. LEXIS 451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Larson",
          "cluster_id": 2080732,
          "cite": [
            "346 N.W.2d 199",
            "1984 Minn. App. LEXIS 3051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Falby",
          "cluster_id": 2380627,
          "cite": [
            "187 Conn. 6",
            "444 A.2d 213",
            "1982 Conn. LEXIS 499"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane1_negative"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beckwith v. United States",
          "cluster_id": 109430,
          "cite": [
            "48 L. Ed. 2d 1",
            "96 S. Ct. 1612",
            "425 U.S. 341",
            "1976 U.S. LEXIS 147",
            "37 A.F.T.R.2d (RIA) 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donaldson v. United States",
          "cluster_id": 108236,
          "cite": [
            "27 L. Ed. 2d 580",
            "91 S. Ct. 534",
            "400 U.S. 517",
            "1971 U.S. LEXIS 147",
            "14 Fed. R. Serv. 2d 1096",
            "27 A.F.T.R.2d (RIA) 482"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Petzoldt v. Commissioner",
          "cluster_id": 4706920,
          "cite": [
            "92 T.C. 661",
            "1989 U.S. Tax Ct. LEXIS 42",
            "92 T.C. No. 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Orozco v. Texas",
          "cluster_id": 107883,
          "cite": [
            "22 L. Ed. 2d 311",
            "394 U.S. 324",
            "89 S. Ct. 1095",
            "1969 U.S. LEXIS 2154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Roldan",
          "cluster_id": 2546413,
          "cite": [
            "110 P.3d 289",
            "27 Cal. Rptr. 3d 360",
            "35 Cal. 4th 646",
            "2005 Cal. Daily Op. Serv. 3440",
            "2005 Daily Journal DAR 4656",
            "2005 Cal. LEXIS 4270"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Illinois",
          "cluster_id": 108480,
          "cite": [
            "31 L. Ed. 2d 202",
            "92 S. Ct. 916",
            "405 U.S. 278",
            "1972 U.S. LEXIS 81"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blain v. Commonwealth",
          "cluster_id": 1349204,
          "cite": [
            "371 S.E.2d 838",
            "7 Va. App. 10",
            "5 Va. Law Rep. 356",
            "1988 Va. App. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
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
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 1203058,
          "cite": [
            "824 P.2d 533",
            "64 Wash. App. 410",
            "1992 Wash. App. LEXIS 249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cannon v. State",
          "cluster_id": 1564923,
          "cite": [
            "691 S.W.2d 664",
            "1985 Tex. Crim. App. LEXIS 1371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Haas",
          "cluster_id": 2057986,
          "cite": [
            "369 N.E.2d 692",
            "373 Mass. 545",
            "1977 Mass. LEXIS 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth George Montos",
          "cluster_id": 288244,
          "cite": [
            "421 F.2d 215"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Heggins",
          "cluster_id": 1547181,
          "cite": [
            "809 A.2d 908"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mathis v. United States (1968):lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107676 OR 9423682 OR 9423683) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODkzMTg0MDAwMDAmcz0yMzgwNjI3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107676+OR+9423682+OR+9423683%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107676 OR 9423682 OR 9423683)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDAmcz0xMzEyMjYyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107676+OR+9423682+OR+9423683%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107676 OR 9423682 OR 9423683)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107676 OR 9423682 OR 9423683)",
    "indexed_citing_opinions": 477,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107676,
        "count": 444,
        "count_source": "search"
      },
      {
        "opinion_id": 9423682,
        "count": 44,
        "count_source": "search"
      },
      {
        "opinion_id": 9423683,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 762,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mathis-v-united-states-1968.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0MzMwNzMmcz00NjU2NTgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107676+OR+9423682+OR+9423683%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107676,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107676,
        "cited_id": 275662,
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
    "date_created": "2026-07-05T12:53:28Z",
    "date_modified": "2026-07-06T08:17:45Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:53:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mathis v. United States (1968)

```
<opinion type="majority">
<author id="b48-6">Me. Justice Black</author>
<p id="AN">delivered the opinion of the Court.</p>
<p id="b48-7">Petitioner was convicted by a jury in a United States District Court on two counts charging that he knowingly filed false claims against the Government in violation of <span class="citation no-link">18 U. S. C. § 287</span><footnotemark>1</footnotemark> and sentenced to 30 months’ imprisonment on each count, the sentences to run concurrently. The frauds charged were claims for tax refunds growing out of petitioner’s individual income taxes for 1960 and 1961. Both income tax returns for these two years asserted receipts of income from two different companies which the government agents were unable to locate and which evidence offered tended to show were nonexistent. The amount of income claimed in each tax return was calculated in such a way as to show that these two nonexistent employers had withheld taxes sufficient to justify substantial refunds to petitioner. The Government paid the 1960 tax refund to petitioner of $885.60 as claimed, but the record fails to show whether the 19.61 claimed refund was paid. A part of the evidence on which the conviction rested consisted of documents and oral statements obtained from petitioner by a government agent while petitioner was in prison serving a state sentence. Before eliciting this information, the government agent did not not warn petitioner that any evi<page-number citation-index="1" label="3">*3</page-number>dence he gave the Government could be used against him, and that he had a right to remain silent if he desired as well as a right to the presence of counsel and that if he was unable to afford counsel one would be appointed for him. At trial petitioner sought several times without success to have the judge hold hearings out of the presence of the jury to prove that his statements to the revenue agent were given without these warnings and should therefore not be used as evidence against him. For this contention he relied exclusively on our case of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). The District Court rejected this contention as did the Court of Appeals in affirming. <span class="citation" data-id="9452694"><a href="/opinion/275684/perma-life-mufflers-inc-v-international-parts-corporation/" aria-description="Citation for case: Perma Life Mufflers, Inc. v. International Parts Corporation">376 F. 2d 695</a></span>. We granted certiorari to decide whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case calls for reversal. We hold that it does.</p>
<p id="b49-5">There can be no doubt that the documents and oral statements given by petitioner to the government agent and used against him were strongly incriminating.<footnotemark>2</footnotemark> In the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>case this Court’s opinion stated at some length the constitutional reasons why one in custody who is interrogated by officers about matters that might tend to incriminate him is entitled to be warned “that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him <page-number citation-index="1" label="4">*4</page-number>prior to any questioning if he so desires.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>. The Government here seeks to escape application of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings on two arguments: (1) that these questions were asked as a part of a routine tax investigation where no criminal proceedings might even be brought, and (2) that the petitioner had not been put in jail by the officers questioning him, but was there for an entirely separate offense. These differences are too minor and shadowy to justify a departure from the well-considered conclusions of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>with reference to warnings to be given to a person held in custody.</p>
<p id="b50-6">It is true that a “routine tax investigation” may be initiated for the purpose of a civil action rather than criminal prosecution. To this extent tax investigations differ from investigations of murder, robbery, and other crimes. But tax investigations frequently lead to criminal prosecutions, just as the one here did. In fact, the last visit of the revenue agent to the jail to question petitioner took place only eight days before the full-fledged criminal investigation concededly began. And, as the investigating revenue agent was compelled to admit, there was always the possibility during his investigation that his work would end up in a criminal prosecution. We reject the contention that tax investigations are immune from the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements <em>for </em>warnings to be given a person in custody.</p>
<p id="b50-7">The Government also seeks to narrow the scope of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>holding by making it applicable only to questioning one who is “in custody” in connection with the very case under investigation. There is no substance to such a distinction, and in effect it goes against the whole purpose of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision which was designed to give meaningful protection to Fifth Amendment rights. We find nothing in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion which calls for a curtailment of the warnings to be given persons <page-number citation-index="1" label="5">*5</page-number>under interrogation by officers based on the reason why the person is in custody. In speaking of “custody” the language of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion is clear and unequivocal:</p>
<blockquote id="b51-5">“To summarize, we hold that when an individual is taken into custody or otherwise deprived of his freedom by the authorities in any significant way and is subjected to questioning, the privilege against self-incrimination is jeopardized.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 478</a></span>.</blockquote>
<p id="b51-6">And the opinion goes on to say that the person so held must be given the warnings about his right to be silent and his right to have a lawyer.</p>
<p id="b51-7">Thus, the courts below were wrong in permitting the introduction of petitioner’s self-incriminating evidence given without warning of his right to be silent and right to counsel. The cause is reversed and remanded for further proceedings consistent with this opinion.</p>
<p id="b51-8">
<em>It is so ordered.</em>
</p>
<judges id="b51-9">Mr. Justice Marshall took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b48-8"> <span class="citation no-link">18 U. S. C. § 287</span> provides: “Whoever makes or presents to any person or officer in the civil, military, or naval service of the United States, or to any department or agency thereof, any claim upon or against the United States, or any department or agency thereof, knowing such claim to be false, fictitious, or fraudulent, shall be fined not more than $10,000 or imprisoned not more than five years, or both.”</p>
</footnote>
<footnote label="2">
<p id="b49-6"> Internal Revenue Agent Lawless testified that on October 30, 1964, he interviewed petitioner in the Florida State Penitentiary to determine if the 1960 return had been prepared by petitioner and to obtain petitioner’s consent in writing to extend the statute of limitations on the 1960 return. At this interview petitioner identified the 1960 tax return and the signature thereon as his; he also signed the extension form. Again on March 2, 1965, Agent Lawless interviewed petitioner at the penitentiary, and this time petitioner identified the 1961 tax return and signature thereon as his and signed an extension form for this return.</p>
</footnote>
</opinion>
```

---
