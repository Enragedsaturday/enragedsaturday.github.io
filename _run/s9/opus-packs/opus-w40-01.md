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

## GROUP: content/cases/South Dakota v. Neville.md  (`case`, 5 assertions)

### content_page

```
---
title: South Dakota v. Neville
type: case
citation: "459 U.S. 553 (1983)"
parallel_cite: "103 S. Ct. 916; 74 L. Ed. 2d 748; 51 U.S.L.W. 4148"
neutral_cite: 1983 U.S. LEXIS 129
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-02-22
docket: No. 81-1453
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
  opinion_url: "https://www.courtlistener.com/opinion/110832/south-dakota-v-neville/"
  cluster_id: 110832
  opinion_id: null
  identity_checked: true
lake:
  record_id: South Dakota v. Neville
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Confessions, Interrogation & the Fifth Amendment]]"
    role: Anchor
related:
  - "[[Schmerber v. California]]"
tags:
  - case
  - fifth-amendment
  - self-incrimination
  - blood-alcohol-test
  - implied-consent
  - due-process
  - dwi
holding: "Admitting into evidence a drunk-driving suspect's refusal to submit to a blood-alcohol test does not violate the Fifth Amendment privilege against self-incrimination, because a refusal — offered as a choice by police after a lawful request — is not an act coerced by the officer; nor does admitting the refusal offend due process even though the officer did not warn the suspect that his refusal could be used against him at trial."
aliases:
  - South Dakota v. Neville
  - "South Dakota v. Neville (1983)"
---

# South Dakota v. Neville

*459 U.S. 553 (1983)* (No. 81-1453) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110832 → combined opinion 110832 (O'Connor, J.; 459 U.S. 553, argued Dec. 8, 1982, decided Feb. 22, 1983). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*564`). S9 promotes. -->

## Background
Two Madison, South Dakota, officers stopped Neville for running a stop sign. He staggered getting out of the car, smelled of alcohol, had no license (revoked after a prior DWI), and failed field sobriety tests. After his arrest and *[[Miranda v. Arizona|Miranda]]* warnings, the officers asked him to submit to a blood-alcohol test and warned that he could lose his license if he refused. Neville refused, saying he was too drunk to pass the test, and refused again at the station. South Dakota law made a refusal admissible at trial, but Neville moved to suppress evidence of his refusal, and the South Dakota courts suppressed it as a violation of the privilege against self-incrimination.

## Issue
Whether admitting a suspect's refusal to take a blood-alcohol test violates the Fifth Amendment privilege against self-incrimination, and whether admitting the refusal denies due process when the officer did not warn that the refusal could be used against him.

## Rule
Building on *[[Schmerber v. California|Schmerber]]* (which allowed a State to compel a blood test itself), the Court reasoned that the privilege bars only *compelled* self-incrimination, and that offering a suspect the choice to take the test or have his refusal used against him is not the kind of coercion the Fifth Amendment forbids. It held: "We hold, therefore, that a refusal to take a blood-alcohol test, after a police officer has lawfully requested it, is not an act coerced by the officer, and thus is not protected by the privilege against self-incrimination." — 459 U.S. at 564. ^pin-564

## Application
Because the State could constitutionally have compelled the test outright, offering the milder alternative of refusal (with attendant penalties) was no less legitimate; the choice, though unpleasant, was not the "cruel trilemma" the privilege guards against. On the separate due-process question, the Court distinguished *[[Doyle v. Ohio]]*: the officer's warning that refusal could cost Neville his license carried no implicit assurance that the refusal would not be used against him at trial, so it was not fundamentally unfair to admit the refusal even absent an express warning.

## Conclusion
The judgment of the Supreme Court of South Dakota was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. O'Connor, J., delivered the opinion of the Court. Stevens, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Neville* is an anchor for the boundary of the Fifth Amendment privilege in the DWI context: a test refusal is not compelled testimony, so its admission is neither self-incrimination nor a due-process violation. Teach it with *[[Schmerber v. California]]* (compelled blood tests and the physical-evidence/testimony line) as the pair marking what the privilege does and does not reach when the State seeks blood-alcohol evidence.

## Appears on
- [[Confessions, Interrogation & the Fifth Amendment]] — *Anchor*

## Sources
- [*South Dakota v. Neville*, 459 U.S. 553 (1983)](https://www.courtlistener.com/opinion/110832/south-dakota-v-neville/) — pinpoint: 564 (O'Connor, J., for the Court; the CL opinion text places the quoted holding just after the reporter star `*564`, i.e., on page 564). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ba7e8560f26d5c0a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "459 U.S. 553 (1983)", "court": "U.S. Supreme Court", "neutral_cite": "1983 U.S. LEXIS 129", "official_citation_present": true, "parallel_cite": "103 S. Ct. 916; 74 L. Ed. 2d 748; 51 U.S.L.W. 4148", "title": "South Dakota v. Neville", "year": "1983"}}
{"assertion_id": "4777d5690ae986c2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Admitting into evidence a drunk-driving suspect's refusal to submit to a blood-alcohol test does not violate the Fifth Amendment privilege against self-incrimination, because a refusal — offered as a choice by police after a lawful request — is not an act coerced by the officer; nor does admitting the refusal offend due process even though the officer did not warn the suspect that his refusal could be used against him at trial.", "title": "South Dakota v. Neville"}}
{"assertion_id": "b1e5d693389b6e54", "dimension": "support", "kind": "home_role", "locator": {"home": "Confessions, Interrogation & the Fifth Amendment"}, "payload": {"home": "Confessions, Interrogation & the Fifth Amendment", "role": "Anchor", "title": "South Dakota v. Neville"}}
{"assertion_id": "671d8d6f8e7549cd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "South Dakota v. Neville"}}
{"assertion_id": "c82ea3e2210e2b16", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "South Dakota v. Neville", "varies_by_point": "false"}}
```

### lake record — South Dakota v. Neville

```json
{
  "schema_version": "s2.v1",
  "record_id": "South Dakota v. Neville",
  "status": "under_review",
  "identity": {
    "case_name": "South Dakota v. Neville",
    "case_name_short": "Neville",
    "case_name_full": "South Dakota v. Neville",
    "input_case_name": "South Dakota v. Neville",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-02-22",
    "year": 1983,
    "docket": "No. 81-1453",
    "cluster_id": 110832,
    "lead_opinion_id": 9429007,
    "sibling_ids": [],
    "absolute_url": "/opinion/110832/south-dakota-v-neville/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "459 U.S. 553",
      "volume": "459",
      "reporter": "U.S.",
      "page": "553",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 916",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "916",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 L. Ed. 2d 748",
        "volume": "74",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4148",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4148",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 129",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "459 U.S. 553",
        "volume": "459",
        "reporter": "U.S.",
        "page": "553",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 916",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "916",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 L. Ed. 2d 748",
        "volume": "74",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 129",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4148",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4148",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "459 U.S. 553",
    "official_selection": {
      "court_class": "scotus",
      "selected": "459 U.S. 553",
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
    "date_created": "2026-07-06T13:44:52Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "south-dakota-v-neville--110832",
      "to_record_id": "South Dakota v. Neville",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — South Dakota v. Neville

```
<opinion type="majority">
<author id="b714-6">Justice O’Connor</author>
<p id="A6k">delivered the opinion of the Court.</p>
<p id="b714-7"><em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), held that a State could force a defendant to submit to a blood-alcohol test without violating the defendant’s Fifth Amendment right against self-incrimination. We now address a question left open in <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 765, n. 9</a></span>, and hold that the admission into evidence of a defendant’s refusal to submit to such a test likewise does not offend the right against self-incrimination.</p>
<p id="b714-8">I</p>
<p id="b714-9">Two Madison, South Dakota, police officers stopped respondent’s car after they saw him fail to stop at a stop sign. The officers asked respondent for his driver’s license and asked him to get out of the car. As he left the car, respondent staggered and fell against the car to support himself. <page-number citation-index="1" label="555">*555</page-number>The officers smelled alcohol on his breath. Respondent did not have a driver’s license, and informed the officers that it was revoked after a previous driving-while-intoxicated conviction. The officers asked respondent to touch his finger to his nose and to walk a straight line. When respondent failed these field sobriety tests, he was placed under arrest and read his <em>Miranda </em>rights.<footnotemark>1</footnotemark> Respondent acknowledged that he understood his rights and agreed to talk without a lawyer present. App. 11. Reading from a printed card, the officers then asked respondent to submit to a blood-alcohol test and warned him that he could lose his license if he refused.<footnotemark>2</footnotemark> Respondent refused to take the test, stating “I’m too drunk, I won’t pass the test.” The officers again read the request to <page-number citation-index="1" label="556">*556</page-number>submit to a test, and then took respondent to the police station, where they read the request to submit a third time. Respondent continued to refuse to take the test, again saying he was too drunk to pass it.<footnotemark>3</footnotemark></p>
<p id="b716-5">South Dakota law specifically declares that refusal to submit to a blood-alcohol test “may be admissible into evidence at the trial.” S. D. Comp. Laws Ann. §32-23-10.1 (Supp. 1982).<footnotemark>4</footnotemark> Nevertheless, respondent sought to suppress all evidence of his refusal to take the blood-alcohol test. The Circuit Court granted the suppression motion for three reasons: the South Dakota statute allowing evidence of refusal violated respondent’s federal constitutional rights; the officers failed to advise respondent that the refusal could be used against him at trial; and the refusal was irrelevant to the issues before the court. The State appealed from the entire order. The South Dakota Supreme Court affirmed the suppression of the act of refusal on the grounds that § 32-23-10.1, which allows the introduction of this evidence, violated the federal and state privilege against self-incrimination.<footnotemark>5</footnotemark> <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/" aria-description="Citation for case: State v. Neville">312 N. W. 2d 723</a></span> (1981). The court reasoned that <page-number citation-index="1" label="557">*557</page-number>the refusal was a communicative act involving respondent’s testimonial capacities and that the State compelled this communication by forcing respondent “‘to choose between submitting to a perhaps unpleasant examination and producing <page-number citation-index="1" label="558">*558</page-number>testimonial evidence against himself,’” <em><span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/" aria-description="Citation for case: State v. Neville">id.,</a></span> </em>at 726 (quoting <em>State </em>v. <em>Andrews, </em><span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/#262" aria-description="Citation for case: State v. Andrews">297 Minn. 260, 262</a></span>, <span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/#864" aria-description="Citation for case: State v. Andrews">212 N. W. 2d 863, 864</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/881/">419 U. S. 881</a></span> (1974)).<footnotemark>6</footnotemark></p>
<p id="b718-8">Since other jurisdictions have found no Fifth Amendment violation from the admission of evidence of refusal to submit to blood-alcohol tests,<footnotemark>7</footnotemark> we granted certiorari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./456/971/">456 U. S. 971</a></span> (1982).</p>
<p id="b718-9">HH hH</p>
<p id="b718-3">The situation underlying this case — that of the drunk driver — occurs with tragic frequency on our Nation’s highways. The carnage caused by drunk drivers is well documented and needs no detailed recitation here. This Court, although not having the daily contact with the problem that the state courts have, has repeatedly lamented the tragedy. See <em>Breithaupt </em>v. <em>Abram, </em><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#439" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 439</a></span> (1957) (“The increasing slaughter on our highways, most of which should be avoidable, now reaches the astounding figures only heard of on the battlefield”); <em>Tate </em>v. <em>Short, </em><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/#401" aria-description="Citation for case: Tate v. Short">401 U. S. 395, 401</a></span> (1971) (Blackmun, J., concurring) (deploring “traffic irresponsibility and the frightful carnage it spews upon our highways”); <em>Perez </em>v. <em>Campbell, </em><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/#657" aria-description="Citation for case: Perez. v. Campbell">402 U. S. 637, 657, 672</a></span> (1971) (Blackmun, J., concurring) (footnote omitted) (“The slaughter on the highways of this Nation exceeds the death toll of all our <page-number citation-index="1" label="559">*559</page-number>wars”); <em>Mackey </em>v. <em>Montrym, </em><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/#17" aria-description="Citation for case: MacKey v. Montrym">443 U. S. 1, 17-19</a></span> (1979) (recognizing the “compelling interest in highway safety”).</p>
<p id="b719-5">As part of its program to deter drinkers from driving, South Dakota has enacted an “implied consent” law. S. D. Comp. Laws Ann. § 32-23-10 (Supp. 1982). This statute declares that any person operating a vehicle in South Dakota is deemed to have consented to a chemical test of the alcoholic content of his blood if arrested for driving while intoxicated. In <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), this Court upheld a state-compelled blood test against a claim that it infringed the Fifth Amendment right against self-incrimination, made applicable to the States through the Fourteenth Amendment.<footnotemark>8</footnotemark> We recognized- that a coerced blood test infringed to some degree the “inviolability of the human personality” and the “requirement that the State procure the evidence against an accused ‘by its own independent labors,’ ” but noted the privilege has never been given the full scope suggested by the values it helps to protect. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#762" aria-description="Citation for case: Schmerber v. California">Id., at 762</a></span>. We therefore held that the privilege bars the State only from compelling “communications” or “testimony.” Since a blood test was “physical or real” evidence rather than testimonial evidence, we found it unprotected by the Fifth Amendment privilege.</p>
<p id="b719-6"><em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>then, clearly allows a State to force a person suspected of driving while intoxicated to submit to a blood-alcohol test.<footnotemark>9</footnotemark> South Dakota, however, has declined to authorize its police officers to administer a blood-alcohol test against the suspect’s will. Rather, to avoid violent confrontations, the South Dakota statute permits a suspect to <page-number citation-index="1" label="560">*560</page-number>refuse the test, and indeed requires police officers to inform the suspect of his right to refuse. S. D. Comp. Laws Ann. § 32-23-10 (Supp. 1982). This permission is not without a price, however. South Dakota law authorizes the Department of Public Safety, after providing the person who has refused the test an opportunity for a hearing, to revoke for one year both the person’s license to drive and any nonresident operating privileges he may possess. § 32-23-11. Such a penalty for refusing to take a blood-alcohol test is unquestionably legitimate, assuming appropriate procedural protections. See <em>Mackey </em>v. <em><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">Montrym, supra.</a></span></em></p>
<p id="b720-5">South Dakota further discourages the choice of refusal by allowing the refusal to be used against the defendant at trial. S. D. Comp. Laws. Ann. §§32-23-10.1 and 19-13-28.1 (Supp. 1982). <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>expressly reserved the question of whether evidence of refusal violated the privilege against self-incrimination. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S., at 765, n. 9</a></span>. The Court did indicate that general Fifth Amendment principles, rather than the particular holding of <em>Griffin </em>v. <em>California, </em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965), should control the inquiry. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S., at 766, n. 9</a></span>.<footnotemark>10</footnotemark></p>
<p id="b720-6">Most courts applying general Fifth Amendment principles to the refusal to take a blood test have found no violation of the privilege against self-incrimination. Many courts, following the lead of Justice Traynor’s opinion for the California Supreme Court in <em>People </em>v. <em>Sudduth, </em><span class="citation" data-id="1390455"><a href="/opinion/1390455/people-v-sudduth/" aria-description="Citation for case: People v. Sudduth">65 Cal. 2d 543</a></span>, <span class="citation" data-id="1390455"><a href="/opinion/1390455/people-v-sudduth/" aria-description="Citation for case: People v. Sudduth">421 P. 2d 401</a></span> (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/850/">389 U. S. 850</a></span> (1967), have reasoned that refusal to submit is a physical act rather than a communication and for this reason is not protected by the <page-number citation-index="1" label="561">*561</page-number>privilege.<footnotemark>11</footnotemark> As Justice Traynor explained more fully in the companion case of <em>People </em>v. <em>Ellis, </em><span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/" aria-description="Citation for case: People v. Ellis">65 Cal. 2d 529</a></span>, <span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/" aria-description="Citation for case: People v. Ellis">421 P. 2d 393</a></span> (1966) (refusal to display voice not testimonial), evidence of refusal to take a potentially incriminating test is similar to other circumstantial evidence of consciousness of guilt, such as escape from custody and suppression of evidence. The court below, relying on <em>Dudley </em>v. <em>State, </em><span class="citation" data-id="9641061"><a href="/opinion/1497914/dudley-v-state/" aria-description="Citation for case: Dudley v. State">548 S. W. 2d 706</a></span> (Tex. Crim. App. 1977), and <em>State </em>v. <em>Andrews, </em><span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/" aria-description="Citation for case: State v. Andrews">297 Minn. 260</a></span>, <span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/" aria-description="Citation for case: State v. Andrews">212 N. W. 2d 863</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/881/">419 U. S. 881</a></span> (1974), rejected this view. This minority view emphasizes that the refusal is “a tacit or overt expression and communication of defendant’s thoughts,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">312 N. W. 2d, at 726</a></span>, and that the Constitution “simply forbids any compulsory revealing or communication of an accused person’s thoughts or mental processes, whether it is by acts, failure to act, words spoken or failure to speak.” <span class="citation" data-id="9641061"><a href="/opinion/1497914/dudley-v-state/#708" aria-description="Citation for case: Dudley v. State"><em>Dudley, supra, </em>at 708</a></span>.</p>
<p id="b721-5">While we find considerable force in the analogies to flight and suppression of evidence suggested by Justice Traynor, we decline to rest our decision on this ground. As we recognized in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>the distinction between real or physical evidence, on the one hand, and communications or testimony, on the other, is not readily drawn in many cases. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S., at 764</a></span>.<footnotemark>12</footnotemark> The situations arising from a refusal present a diffi<page-number citation-index="1" label="562">*562</page-number>cult gradation from a person who indicates refusal by complete inaction, to one who nods his head negatively, to one who states “I refuse to take the test,” to the respondent here, who stated “I’m too drunk, I won’t pass the test.” Since no impermissible coercion is involved when the suspect refuses to submit to take the test, regardless of the form of refusal, we prefer to rest our decision on this ground, and draw possible distinctions when necessary for decision in other circumstances.<footnotemark>13</footnotemark></p>
<p id="b722-5">As we stated in <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#397" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 397</a></span> (1976), “[t]he Court has held repeatedly that the Fifth Amendment is limited to prohibiting the use of ‘physical or moral compulsion’ exerted on the person asserting the privilege.” This coercion requirement comes directly from the constitutional language directing that no person “shall be <em>compelled </em>in any criminal case to be a witness against himself.” U. S. Const., Arndt. 5 (emphasis added). And as Professor Levy concluded in his history of the privilege, “[t]he element of compulsion or involuntariness was always an ingredient of the right and, before the right existed, of protests against incriminating interrogatories.” L. Levy, Origins of the Fifth Amendment 328 (1968).</p>
<p id="b722-6">Here, the State did not directly compel respondent to refuse the test, for it gave him the choice of submitting to the test or refusing. Of course, the fact the government gives a defendant or suspect a “choice” does not always resolve the <page-number citation-index="1" label="563">*563</page-number>compulsion inquiry. The classic Fifth Amendment violation — telling a defendant at trial to testify — does not, under an extreme view, compel the defendant to incriminate himself. He could submit to self-accusation, or testify falsely (risking perjury) or decline to testify (risking contempt). But the Court has long recognized that the Fifth Amendment prevents the State from forcing the choice of this “cruel trilemma” on the defendant. See <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964). See also <em>New Jersey </em>v. <em>Portash, </em><span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979) (telling a witness under a grant of legislative immunity to testify or face contempt sanctions is “the essence of coerced testimony”). Similarly, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>cautioned that the Fifth Amendment may bar the use of testimony obtained when the proffered alternative was to submit to a test so painful, dangerous, or severe, or so violative of religious beliefs, that almost inevitably a person would prefer “confession.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S., at 765, n. 9</a></span>.<footnotemark>14</footnotemark> Cf. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 458</a></span> (1966) (unless compulsion inherent in custodial surroundings is dispelled, no statement is truly a product of free choice).</p>
<p id="b723-4">In contrast to these prohibited choices, the values behind the Fifth Amendment are not hindered when the State offers a suspect the choice of submitting to the blood-alcohol test or having his refusal used against him. The simple blood-alcohol test is so safe, painless, and commonplace, see <em>Schmerber, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California">384 U. S., at 771</a></span>, that respondent concedes, as he must, that the State could legitimately compel the suspect, against his will, to accede to the test. Given, then, that the offer of taking a blood-alcohol test is clearly legitimate, the action becomes no <em>less </em>legitimate when the State offers a second option of refusing the test, with the attendant penalties for making that choice. Nor is this a case where the State has subtly coerced respondent into choosing the option it had no right to compel, rather than offering a true <page-number citation-index="1" label="564">*564</page-number>choice. To the contrary, the State wants respondent to choose to take the test, for the inference of intoxication arising from a positive blood-alcohol test is far stronger than that arising from a refusal to take the test.</p>
<p id="b724-4">We recognize, of course, that the choice to submit or refuse to take a blood-alcohol test will not be an easy or pleasant one for a suspect to make. But the criminal process often requires suspects and defendants to make difficult choices. See, <em>e. g., Crampton </em>v. <em>Ohio, </em>decided with <em>McGautha </em>v. <em>California, </em><span class="citation" data-id="9424551"><a href="/opinion/108329/mcgautha-v-california/#213" aria-description="Citation for case: McGautha v. California">402 U. S. 183, 213-217</a></span> (1971). We hold, therefore, that a refusal to take a blood-alcohol test, after a police officer has lawfully requested it, is not an act coerced by the officer, and thus is not protected by the privilege against self-incrimination.<footnotemark>15</footnotemark></p>
<p id="b724-5">III</p>
<p id="b724-6">Relying on <em>Doyle </em>v. <em>Ohio, </em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">426 U. S. 610</a></span> (1976), respondent also suggests that admission at trial of his refusal violates the Due Process Clause because respondent was not fully warned of the consequences of refusal. <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span> </em>held that the Due Process Clause prohibits a prosecutor from using a defendant’s silence after <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to impeach his testimony at trial. Just a Term before, in <em>United States </em>v. <em>Hale, </em><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span> (1975), we had determined under our supervisory power that the federal courts could not use such silence for impeachment because of its dubious probative value. Al<page-number citation-index="1" label="565">*565</page-number>though <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span> </em>mentioned this rationale in applying the rule to the States, <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/#617" aria-description="Citation for case: Doyle v. Ohio">426 U. S., at 617</a></span>, the Court relied on the fundamental unfairness of implicitly assuring a suspect that his silence will not be used against him and then using his silence to impeach an explanation subsequently offered at trial. <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/#618" aria-description="Citation for case: Doyle v. Ohio"><em>Id., </em>at 618</a></span>.</p>
<p id="b725-5">Unlike the situation in <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span>, </em>we do not think it fundamentally unfair for South Dakota to use the refusal to take the test as evidence of guilt, even though respondent was not specifically warned that his refusal could be used against him at trial. First, the right to silence underlying the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is one of constitutional dimension, and thus cannot be unduly burdened. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 468, n. 37</a></span>. Cf. <em>Fletcher </em>v. <em>Weir, </em><span class="citation" data-id="110668"><a href="/opinion/110668/fletcher-v-weir/" aria-description="Citation for case: Fletcher v. Weir">455 U. S. 603</a></span> (1982) (postarrest silence without <em>Miranda </em>warnings may be used to impeach trial testimony). Respondent’s right to refuse the blood-alcohol test, by contrast, is simply a matter of grace bestowed by the South Dakota Legislature.</p>
<p id="b725-6">Moreover, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings emphasize the dangers of choosing to speak (“whatever you say can and will be used as evidence against you in court”), but give no warning of adverse consequences from choosing to remain silent. This imbalance in the delivery of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, we recognized in <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span>, </em>implicitly assures the suspect that his silence will not be used against him. The warnings challenged here, by contrast, contained no such misleading implicit assurances as to the relative consequences of his choice. The officers explained that, if respondent chose to submit to the test, he had the right to know the results- and could choose to take an additional test by a person chosen by him. The officers did not specifically warn respondent that the test results could be used against him at trial.<footnotemark>16</footnotemark> Explaining the consequences of <page-number citation-index="1" label="566">*566</page-number>the other option, the officers specifically warned respondent that failure to take the test could lead to loss of driving privileges for one year. It is true the officers did not inform respondent of the further consequence that evidence of refusal could be used against him in court,<footnotemark>17</footnotemark> but we think it unrealistic to say that the warnings given here implicitly assure a suspect that no consequences other than those mentioned will occur. Importantly, the warning that he could lose his driver’s license made it clear that refusing the test was not a “safe harbor,” free of adverse consequences.</p>
<p id="b726-5">While the State did not actually warn respondent that the test results could be used against him, we hold that such a failure to warn was not the sort of implicit promise to forgo use of evidence that would unfairly “trick” respondent if the evidence were later offered against him at trial. We therefore conclude that the use of evidence of refusal after these warnings comported with the fundamental fairness required by due process.</p>
<p id="b726-6">IV</p>
<p id="b726-7">The judgment of the South Dakota Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b726-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b715-5"> The officer read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning from a printed card. He read: “You have the right to remain silent. You don’t have to talk to me unless you want to do so. If you want to talk to me I must advise you whatever you say can and will be used as evidence against you in court. You have the right to confer with a lawyer, and to have a lawyer present with you while you’re being questioned. If you want a lawyer but are unable to pay for one, a lawyer will be appointed to represent you free of any cost to you. Knowing these rights, do you want to talk to me without having a lawyer present? You may stop talking to me at any time. You may also demand a lawyer at any time.” App. 8. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-473</a></span> (1966).</p>
</footnote>
<footnote label="2">
<p id="b715-6"> The card read: “I have arrested you for driving or being in actual physical control of a vehicle while under the influence of alcohol or drugs, a violation of S. D. C. L. 32-23-1. I request that you submit to a chemical test of your blood to determine your blood alcohol concentration. You have the right to refuse to submit to such a test and if you do refuse no test will be given. You have the right to a chemical test by a person of your own choosing at your own expense in addition to the test I have requested. You have the right to know the results of any chemical test. If you refuse the test I have requested, your driver’s license and any non-residence driving privilege may be revoked for one year after an opportunity to appear before a hearing officer to determine if your driver’s license or non-residence driving privilege shall be revoked. If your driver’s license or non-residence driving privileges are revoked by the hearing officer, you have the right to appeal to Circuit Court. Do you understand what I told you? Do you wish to submit to the chemical test I have requested?” App. 8-10.</p>
</footnote>
<footnote label="3">
<p id="b716-6"> Responding to other questions, respondent informed the officers that he had been drinking “close to one ease” by himself at home, and that his last drink was “about ten minutes ago.” Tr. of Preliminary Hearing 8.</p>
</footnote>
<footnote label="4">
<p id="b716-7"> South Dakota Comp. Laws Ann. §19-13-28.1 (Supp. 1982) likewise declares that, notwithstanding the general rule in South Dakota that the claim of a privilege is not a proper subject of comment by judge or counsel, evidence of refusal to submit to a chemical analysis of blood, urine, breath, or other bodily substance “is admissible into evidence” at a trial for driving under the influence of alcohol. A person “may not claim privilege against self-incrimination with regard to admission of refusal to submit to chemical analysis.” <em>Ibid.</em></p>
</footnote>
<footnote label="5">
<p id="b716-8"> As Justice Stevens emphasizes, <em>post, </em>at 567, the South Dakota Supreme Court clearly held that the statute violated the State as well as Federal Constitution. Although this would be an <em>adequate </em>state ground for decision, we do not read the opinion as resting on an <em>independent </em>state ground. Rather, we think the court determined that admission of this evidence violated the Fifth Amendment privilege against self-incrimination, and then concluded without further analysis that the state privilege was <page-number citation-index="1" label="557">*557</page-number>violated as well. In reaching its holding, the court first analyzed our decisions in <em>Schmerber </em>v. California, <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), and <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra.</a></span> </em>The court then described the issue for its review as being “[t]o determine whether the <em>Fifth Amendment </em>privilege against self-incrimination applies to refusal evidence,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#725" aria-description="Citation for case: State v. Neville">312 N. W. 2d 723, 725</a></span> (1981) (emphasis added), and later asked “whether this testimonial evidence was compelled for purposes of applying the <em>Fifth Amendment </em>standard,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">id., at 726</a></span> (emphasis added). The cases relied on by the court to resolve these issues analyze the <em>federal </em>privilege against self-incrimination.</p>
<p id="b717-6">The analysis of the court below was remarkably similar to that of the state-court opinion reviewed in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#651" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 651-653</a></span> (1979). That state-court opinion analyzed various decisions interpreting the Federal Constitution, concluded that the Fourth Amendment violated the police procedure at issue there, and then summarily held that the State Constitution was therefore also infringed. As we characterized their analysis, every police practice found to violate the Fourth Amendment would, without further analysis, be held to be contrary to the State Constitution as well. In such a situation, we concluded, this Court has jurisdiction to review the federal constitutional issue decided below.</p>
<p id="b717-7">Justice Stevens, while expressing general dissatisfaction with <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>, </em>attempts to distinguish it by noting that the state court there had said the State and Federal Constitutions are “ ‘substantially similar’ and that ‘a violation of the latter is necessarily a violation of the former.’ ” <em>Post, </em>at 571, n. 7. But the South Dakota Supreme Court made virtually identical statements. In a footnote, the court recognized the textual difference between the federal and state constitutional privileges against self-incrimination, but noted that this Court in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>had interpreted the Fifth Amendment prohibition “in light of the more liberal definition of ‘evidence’ as used in our state constitution.” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">312 N. W. 2d, at 726</a></span>, n. Therefore, the court concluded, “[s]ince the Fifth Amendment of the U. S. Constitution is broad enough to exclude this evidence, there is no need to draw a distinction at this time between S. D. Const. Art. VI, § 9 and the Fifth Amendment of the U. S. Constitution.” <em>Ibid. </em>The court could not have stated more clearly that it simply assumed that any violation of the Fifth Amendment privilege also violated, without further analysis, the state privilege. This was precisely the reasoning we found sufficient in <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span> </em>to give us jurisdiction to hear the case and decide the federal constitutional issue.</p>
</footnote>
<footnote label="6">
<p id="b718-4"> The South Dakota Supreme Court also remanded for a determination whether respondent’s statement that he was too drunk to pass the test was made after a voluntary waiver of his right to remain silent. As yet, of course, there has been no final judgment in this ease. This Court nevertheless has jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span>(3) to review the federal constitutional issue which has been finally determined, because if the State ultimately prevails at trial, the federal issue will be mooted; and if the State loses at trial, governing state law, S. D. Comp. Laws Ann. §§ 23A-32-4 and 23A-32-5 (1979), prevents it from again presenting the federal claim for review. See <em>California </em>v. <em>Stewart </em>(decided with <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#498" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 498, n. 71</a></span> (1966)); <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#481" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 481</a></span> (1975).</p>
</footnote>
<footnote label="7">
<p id="b718-5"> See, <em>e. g., </em>cases cited in nn. 11 and 13, <em>infra.</em></p>
</footnote>
<footnote label="8">
<p id="b719-7"><em> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>also rejected arguments that the coerced blood test violated the right to due process, the right to counsel, and the prohibition against unreasonable searches and seizures.</p>
</footnote>
<footnote label="9">
<p id="b719-8"> <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>did caution that due process concerns could be involved if the police initiated physical violence while administering the test, refused to respect a reasonable request to undergo a different form of testing, or responded to resistance with inappropriate force. 384 U. S., at 760, n. 4.</p>
</footnote>
<footnote label="10">
<p id="b720-7"> <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span> </em>held that a prosecutor’s or trial court’s comments on a defendant’s refusal to take the witness stand impermissibly burdened the defendant’s Fifth Amendment right to refuse. Unlike the defendant’s situation in <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span>, </em>a person suspected of drunk driving has no constitutional right to refuse to take a blood-alcohol test. The specific rule of <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span> </em>is thus inapplicable.</p>
</footnote>
<footnote label="11">
<p id="b721-6"> See, <em>e. g., Newhouse </em>v. <em>Misterly, </em><span class="citation" data-id="286322"><a href="/opinion/286322/bettie-jane-newhouse-v-john-misterly-sheriff/" aria-description="Citation for case: Bettie Jane Newhouse v. John Misterly, Sheriff">415 F. 2d 514</a></span> (CA9 1969); <em>Hill </em>v. <em>State, </em><span class="citation" data-id="9935939"><a href="/opinion/1607970/hill-v-state/#324" aria-description="Citation for case: Hill v. State">366 So. 2d 318, 324-325</a></span> (Ala. 1979); <em>Campbell </em>v. <em>Superior Court, </em><span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/" aria-description="Citation for case: Campbell v. Superior Court">106 Ariz. 542</a></span>, <span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/" aria-description="Citation for case: Campbell v. Superior Court">479 P. 2d 685</a></span> (1971); <em>State </em>v. <em>Haze, </em><span class="citation" data-id="1161273"><a href="/opinion/1161273/state-v-haze/" aria-description="Citation for case: State v. Haze">218 Kan. 60</a></span>, <span class="citation" data-id="1161273"><a href="/opinion/1161273/state-v-haze/" aria-description="Citation for case: State v. Haze">542 P. 2d 720</a></span> (1975) (refusal to give handwriting exemplar); <em>City of Westerville </em>v. <em>Cunningham, </em><span class="citation" data-id="6754052"><a href="/opinion/6864305/city-of-westerville-v-cunningham/" aria-description="Citation for case: City of Westerville v. Cunningham">15 Ohio St. 2d 121</a></span>, <span class="citation" data-id="6754052"><a href="/opinion/6864305/city-of-westerville-v-cunningham/" aria-description="Citation for case: City of Westerville v. Cunningham">239 N. E. 2d 40</a></span> (1968).</p>
</footnote>
<footnote label="12">
<p id="b721-7"> The Court in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>pointed to the lie detector test as an example of evidence that is difficult to characterize as testimonial or real. Even though the test may seek to obtain physical evidence, we reasoned that to compel a person to submit to such testing “is to evoke the spirit and history of the Fifth Amendment.” 384 U. S., at 764. See also <em>People </em>v. <em>Ellis, </em><span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/#537" aria-description="Citation for case: People v. Ellis">65 Cal. 2d 529, 537</a></span>, and n. 9, <span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/#397" aria-description="Citation for case: People v. Ellis">421 P. 2d 393, 397</a></span>, and n. 9 (1966) (analyzing lie detector tests as within the Fifth Amendment privilege). A second example of seemingly physical evidence that nevertheless invokes Fifth Amendment protection was presented in <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454</a></span> (1981). There, we held that the Fifth Amendment privilege protected compelled <page-number citation-index="1" label="562">*562</page-number>disclosures during a court-ordered psychiatric examination. We specifically rejected the claim that the psychiatrist was observing the patient’s communications simply to infer facts of his mind, rather than to examine the truth of the patient’s statements.</p>
</footnote>
<footnote label="13">
<p id="b722-8"> Many courts have found no self-incrimination problem on the ground of no coercion, or on the analytically related ground that the State, if it can compel submission to the test, can qualify the right to refuse the test. See, <em>e. g., Welch </em>v. <em>District Court, </em><span class="citation" data-id="364649"><a href="/opinion/364649/gene-l-welch-v-district-court-of-vermont-unit-no-5-washington-county/" aria-description="Citation for case: Gene L. Welch v. District Court of Vermont Unit No. 5,...">594 F. 2d 903</a></span> (CA2 1979); <em>State </em>v. <em>Meints, </em><span class="citation" data-id="9516145"><a href="/opinion/2000371/state-v-meints/" aria-description="Citation for case: State v. Meints">189 Neb. 264</a></span>, <span class="citation" data-id="9516145"><a href="/opinion/2000371/state-v-meints/" aria-description="Citation for case: State v. Meints">202 N. W. 2d 202</a></span> (1972); <em>State </em>v. <em>Gardner, </em><span class="citation" data-id="1271135"><a href="/opinion/1271135/state-v-gardner/" aria-description="Citation for case: State v. Gardner">52 Ore. App. 663</a></span>, <span class="citation" data-id="1271135"><a href="/opinion/1271135/state-v-gardner/" aria-description="Citation for case: State v. Gardner">629 P. 2d 412</a></span> (1981); <em>State </em>v. <em>Brean, </em><span class="citation" data-id="1519760"><a href="/opinion/1519760/state-v-brean/" aria-description="Citation for case: State v. Brean">136 Vt. 147</a></span>, <span class="citation" data-id="1519760"><a href="/opinion/1519760/state-v-brean/" aria-description="Citation for case: State v. Brean">385 A. 2d 1085</a></span> (1978).</p>
</footnote>
<footnote label="14">
<p id="b723-5"> Nothing in the record suggests that respondent made or could sustain such a claim in this ease.</p>
</footnote>
<footnote label="15">
<p id="b724-7"> In the context of an arrest for driving while intoxicated, a police inquiry of whether the suspect will take a blood-alcohol test is not an interrogation within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>As we stated in <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 301</a></span> (1980), police words or actions “normally attendant to arrest and custody” do not constitute interrogation. The police inquiry here is highly regulated by state law, and is presented in virtually the same words to all suspects. It is similar to a police request to submit to fingerprinting or photography. Respondent’s choice of refusal thus enjoys no prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protection outside the basic Fifth Amendment protection. See generally Arenella, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>and the Privilege Against Self-Incrimination: A Reappraisal, <span class="citation no-link">20 Am. Crim. L. Rev. 31</span>, 56-58 (1982).</p>
</footnote>
<footnote label="16">
<p id="b725-7"> Even though the officers did not specifically advise respondent that the test results could be used against him in court, no one would seriously contend that this failure to warn would make the test results inadmissible, had respondent chosen to submit to the test. Cf. <em>Schneckloth </em>v. <em>Busta</em><page-number citation-index="1" label="566">*566</page-number><em>monte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973) (knowledge of right to refuse not an essential part of proving effective consent to a search).</p>
</footnote>
<footnote label="17">
<p id="b726-12"> Since the State wants the suspect to submit to the test, it is in its interest fully to warn suspects of the consequences of refusal. We are informed that police officers in South Dakota now warn suspects that evidence of their refusal can be used against them in court. Tr. of Oral Arg. 16.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/South Dakota v. Opperman.md  (`case`, 5 assertions)

### content_page

```
---
title: "South Dakota v. Opperman"
type: case
citation: "428 U.S. 364 (1976)"
parallel_cite: "96 S. Ct. 3092; 49 L. Ed. 2d 1000"
neutral_cite: 1976 U.S. LEXIS 15
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-07-06
docket: 75-76
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: South Dakota v. Opperman
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109537/south-dakota-v-opperman/"
  cluster_id: 109537
  opinion_id: 109537
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Anchor"
related: ["[[Colorado v. Bertine]]", "[[Florida v. Wells]]", "[[Cady v. Dombrowski]]", "[[Illinois v. Lafayette]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory", "impoundment", "administrative-search"]
holding: "An inventory search of a lawfully impounded vehicle conducted pursuant to standard police procedures, and not as a pretext concealing an…"
lake:
  record_id: South Dakota v. Opperman
  status: verified
  projected_at: 2026-07-06
---

# South Dakota v. Opperman

*428 U.S. 364 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Opperman's car was impounded for repeated overnight parking violations. Following standard department procedure, an officer inventoried the car using a standard form, opened the unlocked glove compartment, and found marijuana. Opperman was convicted and moved to suppress the marijuana as the product of a warrantless search.

## Issue
Whether a routine inventory search of a lawfully impounded vehicle, conducted under standard police procedures, is reasonable under the Fourth Amendment.

## Rule
Routine inventories under standardized procedures are reasonable. The Court emphasized that "there is no suggestion whatever that this standard procedure, essentially like that followed throughout the country, was a pretext concealing an investigatory police motive." — 428 U.S. at 376. ^pin-376

"On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not 'unreasonable' under the Fourth Amendment." — *Id.* ^pin-376a

## Application
The car was lawfully impounded; the inventory followed standard procedure and was prompted by valuables in plain view, with no indication it was a pretext for an investigatory search. On those facts, opening the glove compartment and inventorying the contents was reasonable, and the marijuana was admissible.

## Conclusion
The routine inventory under standard procedures was reasonable; the South Dakota Supreme Court's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The inventory doctrine was refined by [[Colorado v. Bertine]] (closed containers, opened under standardized criteria) and [[Florida v. Wells]] (no inventory used as a ruse for general rummaging); it draws on the vehicle-caretaking roots of [[Cady v. Dombrowski]] and parallels the booking inventory of an arrestee's effects in [[Illinois v. Lafayette]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *South Dakota v. Opperman*, 428 U.S. 364 (1976) — https://www.courtlistener.com/opinion/109537/south-dakota-v-opperman/ — pinpoint: 376.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bf98feb5ce505c8d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "428 U.S. 364 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 15", "official_citation_present": true, "parallel_cite": "96 S. Ct. 3092; 49 L. Ed. 2d 1000", "title": "South Dakota v. Opperman", "year": "1976"}}
{"assertion_id": "8494e15d87c8aa7f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An inventory search of a lawfully impounded vehicle conducted pursuant to standard police procedures, and not as a pretext concealing an…", "title": "South Dakota v. Opperman"}}
{"assertion_id": "ab4779efed1d2860", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Key — Anchor", "title": "South Dakota v. Opperman"}}
{"assertion_id": "0ba60fe09428c9a1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "South Dakota v. Opperman", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "South Dakota v. Opperman", "varies_by_point": "false"}}
{"assertion_id": "650b63c64df01fc1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "South Dakota v. Opperman"}}
```

### lake record — South Dakota v. Opperman

```json
{
  "schema_version": "s2.v1",
  "record_id": "South Dakota v. Opperman",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "South Dakota v. Opperman",
    "case_name_short": "Opperman",
    "case_name_full": "South Dakota v. Opperman",
    "input_case_name": "South Dakota v. Opperman",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-07-06",
    "year": 1976,
    "docket": "75-76",
    "cluster_id": 109537,
    "lead_opinion_id": 109537,
    "sibling_ids": [
      109537,
      9426579,
      9426580,
      9426581
    ],
    "absolute_url": "/opinion/109537/south-dakota-v-opperman/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 364",
      "volume": "428",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3092",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1000",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 15",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "15",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 364",
        "volume": "428",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3092",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1000",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 15",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "15",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-376",
      "page": null,
      "quote": "--- # South Dakota v. Opperman *428 U.S. 364 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Opperman's car was impounded for repeated overnight parking violations. Following standard department procedure, an officer inventoried the car using a standard form, opened the unlocked glove compartment, and found marijuana. Opperman was convicted and moved to suppress the marijuana as the product of a warrantless search. ## Issue Whether a routine inventory search of a lawfully impounded vehicle, conducted under standard police procedures, is reasonable under the Fourth Amendment. ## Rule Routine inventories under standardized procedures are reasonable. The Court emphasized that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-376a",
      "page": null,
      "quote": "On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not 'unreasonable' under the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "South Dakota v. Opperman",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Charles E. Blake v. State of Mississippi",
          "cluster_id": 4541114,
          "cite": [
            "256 So. 3d 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
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
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ehiabhi",
          "cluster_id": 4434347,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Finley",
          "cluster_id": 111880,
          "cite": [
            "95 L. Ed. 2d 539",
            "107 S. Ct. 1990",
            "481 U.S. 551",
            "1987 U.S. LEXIS 2058",
            "55 U.S.L.W. 4612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Long",
          "cluster_id": 111020,
          "cite": [
            "77 L. Ed. 2d 1201",
            "103 S. Ct. 3469",
            "463 U.S. 1032",
            "1983 U.S. LEXIS 7",
            "51 U.S.L.W. 5231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Kennedy",
          "cluster_id": 110714,
          "cite": [
            "72 L. Ed. 2d 416",
            "102 S. Ct. 2083",
            "456 U.S. 667",
            "1982 U.S. LEXIS 111",
            "50 U.S.L.W. 4544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Neville",
          "cluster_id": 110832,
          "cite": [
            "74 L. Ed. 2d 748",
            "103 S. Ct. 916",
            "459 U.S. 553",
            "1983 U.S. LEXIS 129",
            "51 U.S.L.W. 4148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk4NzgwODAwMDAwJnM9NDQwNTI4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MTkmcz0xMTQyODQxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
        "reviewed": 70,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 70,
        "triage_read": 0,
        "triage_snippet_classified": 70
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
    "indexed_citing_opinions": 2070,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109537,
        "count": 1793,
        "count_source": "search"
      },
      {
        "opinion_id": 9426579,
        "count": 336,
        "count_source": "search"
      },
      {
        "opinion_id": 9426580,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9426581,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3446,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/south-dakota-v-opperman.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTEyMzkmcz0xMDMyODM2MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109537,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 274387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 292850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 296084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 302928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 307000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 310049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 313477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 314840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 332335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1141627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1153594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1185375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1207398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1239412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1256845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1271156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1273048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1311789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1312019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1367368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1494540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1600787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1659036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1762007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1770477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1868897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2060145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2350702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2353003,
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
    "date_created": "2026-07-05T20:10:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:10:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:10:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:13:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:10:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — South Dakota v. Opperman

```
<div>
<center><b><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364</a></span> (1976)</b></center>
<center><h1>SOUTH DAKOTA<br>
v.<br>
OPPERMAN.</h1></center>
<center>No. 75-76.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29, 1976.</center>
<center>Decided July 6, 1976.</center>
CERTIORARI TO THE SUPREME COURT OF SOUTH DAKOTA.
<p><i>William J. Janklow,</i> Attorney General of South Dakota, argued the cause for petitioner. With him on the brief was <i>Earl R. Mettler,</i> Assistant Attorney General.</p>
<p><i>Robert C. Ulrich,</i> by appointment of the Court, 423 <span class="star-pagination">*365</span> U. S. 1012, argued the cause for respondent <i>pro hac vice.</i> With him on the brief were <i>Lee M. McCahren</i> and <i>John F. Hagemann.</i><sup>[*]</sup></p>
<p>MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We review the judgment of the Supreme Court of South Dakota, holding that local police violated the Fourth Amendment to the Federal Constitution, as applicable to the States under the Fourteenth Amendment, when they conducted a routine inventory search of an automobile lawfully impounded by police for violations of municipal parking ordinances.</p>
<p></p>
<h2>(1)</h2>
<p>Local ordinances prohibit parking in certain areas of downtown Vermillion, S. D., between the hours of 2 a. m. and 6 a. m. During the early morning hours of December 10, 1973, a Vermillion police officer observed respondent's unoccupied vehicle illegally parked in the restricted zone. At approximately 3 a. m., the officer issued an overtime parking ticket and placed it on the car's windshield. The citation warned:</p>
<blockquote>"Vehicles in violation of any parking ordinance may be towed from the area."</blockquote>
<p>At approximately 10 o'clock on the same morning, another <span class="star-pagination">*366</span> officer issued a second ticket for an overtime parking violation. These circumstances were routinely reported to police headquarters, and after the vehicle was inspected, the car was towed to the city impound lot.</p>
<p>From outside the car at the impound lot, a police officer observed a watch on the dashboard and other items of personal property located on the back seat and back floorboard. At the officer's direction, the car door was then unlocked and, using a standard inventory form pursuant to standard police procedures, the officer inventoried the contents of the car, including the contents of the glove compartment, which was unlocked. There he found marihuana contained in a plastic bag. All items, including the contraband, were removed to the police department for safekeeping.<sup>[1]</sup> During the late afternoon of December 10, respondent appeared at the police department to claim his property. The marihuana was retained by police.</p>
<p>Respondent was subsequently arrested on charges of possession of marihuana. His motion to suppress the evidence yielded by the inventory search was denied; he was convicted after a jury trial and sentenced to a fine of $100 and 14 days' incarceration in the county jail. On appeal, the Supreme Court of South Dakota reversed <span class="star-pagination">*367</span> the conviction. 89 S. D. , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152</a></span>. The court concluded that the evidence had been obtained in violation of the Fourth Amendment prohibition against unreasonable searches and seizures. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./423/923/">423 U. S. 923</a></span> (1975), and we reverse.</p>
<p></p>
<h2>(2)</h2>
<p>This Court has traditionally drawn a distinction between automobiles and homes or offices in relation to the Fourth Amendment. Although automobiles are "effects" and thus within the reach of the Fourth Amendment, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973), warrantless examinations of automobiles have been upheld in circumstances in which a search of a home or office would not. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#589" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 589</a></span> (1974); <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 439-440</a></span>; <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#48" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 48</a></span> (1970).</p>
<p>The reason for this well-settled distinction is twofold. First, the inherent mobility of automobiles creates circumstances of such exigency that, as a practical necessity, rigorous enforcement of the warrant requirement is impossible. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span> (1925); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#459" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 459-460</a></span> (1971). But the Court has also upheld warrantless searches where no immediate danger was presented that the car would be removed from the jurisdiction. <i>Chambers</i> v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Maroney, supra,</i> at 51-52</a></span>; <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967). Besides the element of mobility, less rigorous warrant requirements govern because the expectation of privacy with respect to one's automobile is significantly less than that relating to one's home or office.<sup>[2]</sup> In discharging their varied responsibilities <span class="star-pagination">*368</span> for ensuring the public safety, law enforcement officials are necessarily brought into frequent contact with automobiles. Most of this contact is distinctly noncriminal in nature. <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#442" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 442</a></span>. Automobiles, unlike homes, are subjected to pervasive and continuing governmental regulation and controls, including periodic inspection and licensing requirements. As an everyday occurrence, police stop and examine vehicles when license plates or inspection stickers have expired, or if other violations, such as exhaust fumes or excessive noise, are noted, or if headlights or other safety equipment are not in proper working order.</p>
<p>The expectation of privacy as to automobiles in further diminished by the obviously public nature of automobile travel. Only two Terms ago, the Court noted:</p>
<blockquote>"One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. . . . It travels public thoroughfares where both its occupants and its contents are in plain view." <i>Cardwell</i> v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis"><i>Lewis, supra,</i> at 590</a></span>.</blockquote>
<p>In the interests of public safety and as part of what the Court has called "community caretaking functions," <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 441</a></span>, automobiles are frequently taken into police custody. Vehicle accidents present one such occasion. To permit the uninterrupted flow of traffic and in some circumstances to preserve evidence, disabled or damaged vehicles will often be removed from the highways or streets at the behest of police engaged solely in caretaking and traffic-control activities. <span class="star-pagination">*369</span> Police will also frequently remove and impound automobiles which violate parking ordinances and which thereby jeopardize both the public safety and the efficient movement of vehicular traffic.<sup>[3]</sup> The authority of police to seize and remove from the streets vehicles impeding traffic or threatening public safety and convenience is beyond challenge.</p>
<p>When vehicles are impounded, local police departments generally follow a routine practice of securing and inventorying the automobiles' contents. These procedures developed in response to three distinct needs: the protection of the owner's property while it remains in police custody, <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/#961" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960, 961</a></span> (CA9 1972); the protection of the police against claims or disputes over lost or stolen property, <i>United States</i> v. <i>Kelehar,</i> <span class="citation" data-id="307000"><a href="/opinion/307000/united-states-v-levy-alan-kelehar-aka-james-stone/#178" aria-description="Citation for case: United States v. Levy Alan Kelehar, A/K/A James Stone">470 F. 2d 176, 178</a></span> (CA5 1972); and the protection of the police from potential danger, <i>Cooper</i> v. <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California"><i>California, supra,</i> at 61-62</a></span>. The practice has been viewed as essential to respond to incidents of theft or vandalism. See <i>Cabbler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/#522" aria-description="Citation for case: Cabbler v. Commonwealth">212 Va. 520, 522</a></span>, <span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/#782" aria-description="Citation for case: Cabbler v. Commonwealth">184 S. E. 2d 781, 782</a></span> (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/1073/">405 U. S. 1073</a></span> (1972); <i>Warrix</i> v. <i>State,</i> <span class="citation" data-id="1762007"><a href="/opinion/1762007/warrix-v-state/#376" aria-description="Citation for case: Warrix v. State">50 Wis. 2d 368, 376</a></span>, <span class="citation" data-id="1762007"><a href="/opinion/1762007/warrix-v-state/#194" aria-description="Citation for case: Warrix v. State">184 N. W. 2d 189, 194</a></span> (1971). In addition, police frequently attempt to determine whether a vehicle has been stolen and thereafter abandoned.</p>
<p>These caretaking procedures have almost uniformly been upheld by the state courts, which by virtue of the localized nature of traffic regulation have had considerable occasion to deal with the issue.<sup>[4]</sup> Applying the <span class="star-pagination">*370</span> Fourth Amendment standard of "reasonableness,"<sup>[5]</sup> the state courts have overwhelmingly concluded that, even if an inventory is characterized as a "search,"<sup>[6]</sup> the <span class="star-pagination">*371</span> intrusion is constitutionally permissible. See, <i>e. g., </i><i>City of St. Paul</i> v. <i>Myles,</i> <span class="citation" data-id="1239412"><a href="/opinion/1239412/city-of-st-paul-v-myles/#300" aria-description="Citation for case: City of St. Paul v. Myles">298 Minn. 298, 300-301</a></span>, <span class="citation" data-id="1239412"><a href="/opinion/1239412/city-of-st-paul-v-myles/#699" aria-description="Citation for case: City of St. Paul v. Myles">218 N. W. 2d 697, 699</a></span> (1974); <i>State</i> v. <i>Tully,</i> <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/#136" aria-description="Citation for case: State v. Tully">166 Conn. 126, 136</a></span>, <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/#609" aria-description="Citation for case: State v. Tully">348 A. 2d 603, 609</a></span> (1974); <i>People</i> v. <i>Trusty,</i> <span class="citation" data-id="9848553"><a href="/opinion/1273048/people-v-trusty/#296" aria-description="Citation for case: People v. Trusty">183 Colo. 291, 296-297</a></span>, <span class="citation" data-id="9848553"><a href="/opinion/1273048/people-v-trusty/#425" aria-description="Citation for case: People v. Trusty">516 P. 2d 423, 425-426</a></span> (1973); <i>People</i> v. <i>Sullivan,</i> 29 N. Y. 2d 69, 73, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#466" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d 464, 466</a></span> (1971); <i>Cabbler</i> v. <i><span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/" aria-description="Citation for case: Cabbler v. Commonwealth">Commonwealth, supra</a></span></i><i>; </i><i>Warrix</i> v. <i>State, supra</i><i>; </i><i>State</i> v. <i>Wallen,</i> <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/" aria-description="Citation for case: State v. Wallen">185 Neb. 44</a></span>, <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/" aria-description="Citation for case: State v. Wallen">173 N. W. 2d 372</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/912/">399 U. S. 912</a></span> (1970); <i>State</i> v. <i>Criscola,</i> <span class="citation" data-id="1141627"><a href="/opinion/1141627/state-v-criscola/" aria-description="Citation for case: State v. Criscola">21 Utah 2d 272</a></span>, <span class="citation" data-id="1141627"><a href="/opinion/1141627/state-v-criscola/" aria-description="Citation for case: State v. Criscola">444 P. 2d 517</a></span> (1968); <i>State</i> v. <i>Montague,</i> <span class="citation" data-id="1207398"><a href="/opinion/1207398/state-v-montague/" aria-description="Citation for case: State v. Montague">73 Wash. 2d 381</a></span>, <span class="citation" data-id="1207398"><a href="/opinion/1207398/state-v-montague/" aria-description="Citation for case: State v. Montague">438 P. 2d 571</a></span> (1968); <i>People</i> v. <i>Clark,</i> <span class="citation" data-id="9719416"><a href="/opinion/2111286/people-v-clark/" aria-description="Citation for case: People v. Clark">32 Ill. App. 3d 898</a></span>, <span class="citation no-link">336 N. E. 2d 892</span> (1975); <i>State</i> v. <i>Achter,</i> <span class="citation" data-id="1770477"><a href="/opinion/1770477/state-v-achter/" aria-description="Citation for case: State v. Achter">512 S. W. 2d 894</a></span> (Mo. Ct. App. 1974); <i>Bennett</i> v. <i>State,</i> <span class="citation" data-id="9538969"><a href="/opinion/1153594/bennett-v-state/" aria-description="Citation for case: Bennett v. State">507 P. 2d 1252</a></span> (Okla. Crim. App. 1973); <i>People</i> v. <i>Willis,</i> <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">46 Mich. App. 436</a></span>, <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">208 N. W. 2d 204</a></span> (1973); <i>State</i> v. <i>All,</i> 17 N. C. App. 284, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/" aria-description="Citation for case: State v. All">193 S. E. 2d 770</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973); <i>Godbee</i> v. <i>State,</i> <span class="citation" data-id="1659036"><a href="/opinion/1659036/godbee-v-state/" aria-description="Citation for case: Godbee v. State">224 So. 2d 441</a></span> (Fla. Dist. Ct. App. 1969). Even the seminal state decision relied on by the South Dakota Supreme Court in reaching the contrary result. <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation no-link">4 Cal. 2d 699</span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84</a></span> (1971), expressly approved police caretaking activities resulting in the securing of property within the officer's plain view.</p>
<p>The majority of the Federal Courts of Appeals have likewise sustained inventory procedures as reasonable police intrusions. As Judge Wisdom has observed:</p>
<blockquote>"[W]hen the police take custody of any sort of container [such as] an automobile . . . it is reasonable to search the container to itemize the property to be held by the police. [This reflects] the underlying principle that the fourth amendment proscribes only <i>unreasonable</i> searches." <i>United States</i> v. <i>Gravitt,</i> <span class="citation" data-id="313366"><a href="/opinion/313366/united-states-v-jerry-eugene-gravitt/#378" aria-description="Citation for case: United States v. Jerry Eugene Gravitt">484 F. 2d 375, 378</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1135/">414 U. S. 1135</a></span> (1974) (emphasis in original).</blockquote>
<p><span class="star-pagination">*372</span> See also <i>Cabbler</i> v. <i>Superintendent,</i> <span class="citation" data-id="332335"><a href="/opinion/332335/herbert-w-cabbler-v-superintendent-virginia-state-penitentiary/" aria-description="Citation for case: Herbert W. Cabbler v. Superintendent, Virginia State...">528 F. 2d 1142</a></span> (CA4 1975), cert. pending, No. 75-1463; <i>Barker</i> v. <i>Johnson,</i> <span class="citation" data-id="313477"><a href="/opinion/313477/daniel-barker-v-dale-johnson/" aria-description="Citation for case: Daniel Barker v. Dale Johnson">484 F. 2d 941</a></span> (CA6 1973); <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960</a></span> (CA9 1972); <i>United States</i> v. <i>Lipscomb,</i> <span class="citation" data-id="293775"><a href="/opinion/293775/united-states-v-robert-edward-lipscomb/" aria-description="Citation for case: United States v. Robert Edward Lipscomb">435 F. 2d 795</a></span> (CA5 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/980/">401 U. S. 980</a></span> (1971); <i>United States</i> v. <i>Pennington,</i> <span class="citation" data-id="9456780"><a href="/opinion/296084/united-states-v-james-larry-pennington/" aria-description="Citation for case: United States v. James Larry Pennington">441 F. 2d 249</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/854/">404 U. S. 854</a></span> (1971); <i>United States</i> v. <i>Boyd,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/436/1203/">436 F. 2d 1203</a></span> (CA5 1971); <i>Cotton</i> v. <i>United States,</i> <span class="citation" data-id="274387"><a href="/opinion/274387/gary-leland-cotton-v-united-states/" aria-description="Citation for case: Gary Leland Cotton v. United States">371 F. 2d 385</a></span> (CA9 1967). Accord, <i>Lowe</i> v. <i>Hopper,</i> <span class="citation" data-id="1367368"><a href="/opinion/1367368/lowe-v-hopper/#976" aria-description="Citation for case: Lowe v. Hopper">400 F. Supp. 970, 976-977</a></span> (SD Ga. 1975); <i>United States</i> v. <i>Spitalieri,</i> <span class="citation" data-id="1494540"><a href="/opinion/1494540/united-states-v-spitalieri/#169" aria-description="Citation for case: United States v. Spitalieri">391 F. Supp. 167, 169-170</a></span> (ND Ohio 1975); <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="1445531"><a href="/opinion/1445531/united-states-v-smith/" aria-description="Citation for case: United States v. Smith">340 F. Supp. 1023</a></span> (Conn. 1972); <i>United States</i> v. <i>Fuller,</i> <span class="citation" data-id="1868897"><a href="/opinion/1868897/united-states-v-fuller/" aria-description="Citation for case: United States v. Fuller">277 F. Supp. 97</a></span> (DC 1967), conviction aff'd, 139 U. S. App. D. C. 375, <span class="citation" data-id="292850"><a href="/opinion/292850/morris-fuller-v-united-states/" aria-description="Citation for case: Morris Fuller v. United States">433 F. 2d 533</a></span> (1970). These cases have recognized that standard inventories often include an examination of the glove compartment, since it is a customary place for documents of ownership and registration, <i>United States</i> v. <span class="citation" data-id="9456780"><a href="/opinion/296084/united-states-v-james-larry-pennington/#251" aria-description="Citation for case: United States v. James Larry Pennington"><i>Pennington, supra,</i> at 251</a></span>, as well as a place for the temporary storage of valuables.</p>
<p></p>
<h2>(3)</h2>
<p>The decisions of this Court point unmistakably to the conclusion reached by both federal and state courts that inventories pursuant to standard police procedures are reasonable. In the first such case, Mr. Justice Black made plain the nature of the inquiry before us:</p>
<blockquote>"But the question here is not whether the search was <i>authorized</i> by state law. The question is rather whether the search was <i>reasonable</i> under the Fourth Amendment." <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61</a></span> (emphasis added).</blockquote>
<p>And, in his last writing on the Fourth Amendment, Mr. Justice Black said:</p>
<blockquote>"[T]he Fourth Amendment does not require that every search be made pursuant to a warrant. It <span class="star-pagination">*373</span> prohibits only `<i>unreasonable</i> searches and seizures.' The relevant test <i>is not the reasonableness of the opportunity to procure a warrant,</i> but the reasonableness of the seizure under all the circumstances. The test of reasonableness cannot be fixed by <i>per se</i> rules; each case must be decided on its own facts." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#509" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 509-510</a></span> (concurring and dissenting) (emphasis added).</blockquote>
<p>In applying the reasonableness standard adopted by the Framers, this Court has consistently sustained police intrusions into automobiles impounded or otherwise in lawful police custody where the process is aimed at securing or protecting the car and its contents. In <i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>,</i> the Court upheld the inventory of a car impounded under the authority of a state forfeiture statute. Even though the inventory was conducted in a distinctly criminal setting<sup>[7]</sup> and carried out a week after the car had been impounded, the Court nonetheless found that the car search, including examination of the glove compartment where contraband was found, was reasonable under the circumstances. This conclusion was reached despite the fact that no warrant had issued and probable cause to search for the contraband in the vehicle had not been established. The Court said in language explicitly applicable here:</p>
<blockquote>"It would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own protection, to search it." <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>.<sup>[8]</sup></blockquote>
<p><span class="star-pagination">*374</span> In the following Term, the Court in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968), upheld the introduction of evidence, seized by an officer who, after conducting an inventory search of a car and while taking means to safeguard it, observed a car registration card lying on the metal stripping of the car door. Rejecting the argument that a warrant was necessary, the Court held that the intrusion was justifiable since it was "taken to protect the car while it was in police custody." <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States"><i>Id.,</i> at 236</a></span>.<sup>[9]</sup></p>
<p>Finally, in <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski, supra</a></span></i><i>,</i> the Court upheld a warrantless search of an automobile towed to a private garage even though no probable cause existed to believe that the vehicle contained fruits of a crime. The sole justification for the warrantless incursion was that it was incident to the caretaking function of the local police to protect the community's safety. Indeed, the protective search was instituted solely because local police "were under the impression" that the incapacitated driver, a Chicago police officer, was required to carry his service revolver at all times; the police had reasonable grounds to believe a weapon might be in the car, and thus available to vandals. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#436" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 436</a></span>. The Court carefully noted that the protective search was <span class="star-pagination">*375</span> carried out in accordance with <i>standard procedures</i> in the local police department, <i>ibid.,</i> a factor tending to ensure that the intrusion would be limited in scope to the extent necessary to carry out the caretaking function. See <i>United States</i> v. <i>Spitalieri,</i> <span class="citation" data-id="1494540"><a href="/opinion/1494540/united-states-v-spitalieri/#169" aria-description="Citation for case: United States v. Spitalieri">391 F. Supp., at 169</a></span>. In reaching this result, the Court in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> distinguished <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964), on the grounds that the holding, invalidating a car search conducted after a vagrancy arrest, "stands only for the proposition that the search challenged there could not be justified as one incident to an arrest." <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#444" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 444</a></span>. <i><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span></i> therefore did not raise the issue of the constitutionality of a protective inventory of a car lawfully within police custody.</p>
<p>The holdings in <i>Cooper, Harris,</i> and <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> point the way to the correct resolution of this case. None of the three cases, of course, involves the precise situation presented here; but, as in all Fourth Amendment cases, we are obliged to look to all the facts and circumstances of this case in light of the principles set forth in these prior decisions.</p>
<blockquote>"[W]hether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case . . . ." <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S., at 59</a></span>.</blockquote>
<p>The Vermillion police were indisputably engaged in a caretaking search of a lawfully impounded automobile. Cf. <i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/#471" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468, 471</a></span> (CA8 1973). The inventory was conducted only after the car had been impounded for multiple parking violations. The owner, having left his car illegally parked for an extended period, and thus subject to impoundment, was not present to make other arrangements for the safekeeping of his belongings. The inventory itself was prompted by the presence in plain view of a number of <span class="star-pagination">*376</span> valuables inside the car. As in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span>,</i> there is no suggestion whatever that this standard procedure, essentially like that followed throughout the country, was a pretext concealing an investigatory police motive.<sup>[10]</sup></p>
<p>On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not "unreasonable" under the Fourth Amendment.</p>
<p>The judgment of the South Dakota Supreme Court is therefore reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>While I join the opinion of the Court, I add this opinion to express additional views as to why the search conducted in this case is valid under the Fourth and Fourteenth Amendments. This inquiry involves two distinct questions: (i) whether routine inventory searches are impermissible, and (ii) if not, whether they must be conducted pursuant to a warrant.</p>
<p></p>
<h2>
<span class="star-pagination">*377</span> I</h2>
<p>The central purpose of the Fourth Amendment is to safeguard the privacy and security of individuals against arbitrary invasions by government officials. See, <i>e. g., </i><i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). None of our prior decisions is dispositive of the issue whether the Amendment permits routine inventory "searches"<sup>[1]</sup> of automobiles.<sup>[2]</sup> Resolution of this <span class="star-pagination">*378</span> question requires a weighing of the governmental and societal interests advanced to justify such intrusions against the constitutionally protected interest of the individual citizen in the privacy of his effects. <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 555; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878-879</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#892" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 892</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447-448</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968). Cf. <i>Camara</i> v. <i>Municipal Court, supra,</i> at 534-535. As noted in the Court's opinion, see <i>ante,</i> at 369, three interests generally have been advanced in support of inventory searches: (i) protection of the police from danger; (ii) protection of the police against claims and disputes over lost or stolen property; and (iii) protection of the owner's property while it remains in police custody.</p>
<p>Except in rare cases, there is little danger associated with impounding unsearched automobiles. But the occasional danger that may exist cannot be discounted entirely. See <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967). The harmful consequences in those rare cases may be great, and there does not appear to be any effective way of identifying in advance those circumstances or classes of automobile impoundments which represent a greater risk. Society also has an important interest in minimizing the number of false claims filed against police since they may diminish the community's respect for law enforcement generally and lower department morale, thereby impairing the effectiveness of the police.<sup>[3]</sup> It <span class="star-pagination">*379</span> is not clear, however, that inventories are a completely effective means of discouraging false claims, since there remains the possibility of accompanying such claims with an assertion that an item was stolen prior to the inventory or was intentionally omitted from the police records.</p>
<p>The protection of the owner's property is a significant interest for both the policeman and the citizen. It is argued that an inventory is not necessary since locked doors and rolled-up windows afford the same protection that the contents of a parked automobile normally enjoy.<sup>[4]</sup> But many owners might leave valuables in their automobile temporarily that they would not leave there unattended for the several days that police custody may last. There is thus a substantial gain in security if automobiles are inventoried and valuable items removed for storage. And, while the same security could be attained by posting a guard at the storage lot, that alternative may be prohibitively expensive, especially for smaller jurisdictions.<sup>[5]</sup></p>
<p>Against these interests must be weighed the citizen's interest in the privacy of the contents of his automobile. Although the expectation of privacy in an automobile is significantly less than the traditional expectation of privacy associated with the home, <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 561-562; <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra,</a></span></i> at 896 n. 2; see <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality opinion), the unrestrained search <span class="star-pagination">*380</span> of an automobile and its contents would constitute a serious intrusion upon the privacy of the individual in many circumstances. But such a search is not at issue in this case. As the Court's opinion emphasizes, the search here was limited to an inventory of the unoccupied automobile and was conducted strictly in accord with the regulations of the Vermillion Police Department.<sup>[6]</sup> Upholding searches of this type provides no general license for the police to examine all the contents of such automobiles.<sup>[7]</sup></p>
<p>I agree with the Court that the Constitution permits routine inventory searches, and turn next to the question whether they must be conducted pursuant to a warrant.</p>
<p></p>
<h2>
<span class="star-pagination">*381</span> II</h2>
<p>While the Fourth Amendment speaks broadly in terms of "unreasonable searches and seizures,"<sup>[8]</sup> the decisions of this Court have recognized that the definition of "reasonableness" turns, at least in part, on the more specific dictates of the Warrant Clause. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315</a></span> (1972); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356</a></span> (1967); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. As the Court explained in <i>Katz</i> v. <i>United States, supra,</i> at 357, "[s]earches conducted without warrants have been held unlawful `notwithstanding facts unquestionably showing probable cause,' <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>, for the Constitution requires `that the deliberate, impartial judgment of a judicial officer . . . be interposed between the citizen and the police . . . .' <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-482</a></span>." Thus, although "[s]ome have argued that `[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable,' <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950)," "[t]his view has not been accepted." <i>United States</i> v. <i>United States District Court, supra,</i> at 315, and n. 16. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). Except in a few carefully defined classes of cases, a search of private property without valid consent is "unreasonable" unless it has been authorized by a valid search warrant. See, <i>e. g., </i><i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span> (1973); <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span> (1964); <span class="star-pagination">*382</span> <i>Camara</i> v. <i>Municipal Court, supra,</i> at 528; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951); <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1925).</p>
<p>Although the Court has validated warrantless searches of automobiles in circumstances that would not justify a search of a home or office, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), these decisions establish no general "automobile exception" to the warrant requirement. See <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964). Rather, they demonstrate that " `for the purposes of the Fourth Amendment there is a constitutional difference between houses and cars,' " <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 439</a></span>, quoting <i>Chambers</i> v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney"><i>Maroney, supra,</i> at 52</a></span>, a difference that may in some cases justify a warrantless search.<sup>[9]</sup></p>
<p>The routine inventory search under consideration in this case does not fall within any of the established exceptions to the warrant requirement.<sup>[10]</sup> But examination of the interests which are protected when searches are <span class="star-pagination">*383</span> conditioned on warrants issued by a judicial officer reveals that none of these is implicated here. A warrant may issue only upon "probable cause." In the criminal context the requirement of a warrant protects the individual's legitimate expectation of privacy against the overzealous police officer. "Its protection consists in requiring that those inferences [concerning probable cause] be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). See, <i>e. g., </i><i>United States</i> v. <i>United States District Court, supra,</i> at 316-318. Inventory searches, however, are not conducted in order to discover evidence of crime. The officer does not make a discretionary determination to search based on a judgment that certain conditions are present. Inventory searches are conducted in accordance with established police department rules or policy and occur whenever an automobile is seized. There are thus no special facts for a neutral magistrate to evaluate.</p>
<p>A related purpose of the warrant requirement is to prevent hindsight from affecting the evaluation of the reasonableness of a search. See <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 565; cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, 455 n. 22 (1976) (MARSHALL, J., dissenting). In the case of an inventory search conducted in accordance with standard police department procedures, there is no significant danger of hindsight justification. The absence of a warrant will not impair the effectiveness of post-search review of the reasonableness of a particular inventory search.</p>
<p>Warrants also have been required outside the context of a criminal investigation. In <i>Camara</i> v. <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Municipal Court</a></span></i><i>,</i> the Court held that, absent consent, a warrant was necessary to conduct an areawide building code inspection, <span class="star-pagination">*384</span> even though the search could be made absent cause to believe that there were violations in the particular buildings being searched. In requiring a warrant the Court emphasized that "[t]he practical effect of [the existing warrantless search procedures had been] to leave the occupant subject to the discretion of the official in the field," since</p>
<blockquote>"when [an] inspector demands entry, the occupant ha[d] no way of knowing whether enforcement of the municipal code involved require[d] inspection of his premises, no way of knowing the lawful limits of the inspector's power to search, and no way of knowing whether the inspector himself [was] acting under proper authorization." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>.</blockquote>
<p>In the inventory search context these concerns are absent. The owner or prior occupant of the automobile is not present, nor, in many cases, is there any real likelihood that he could be located within a reasonable period of time. More importantly, no significant discretion is placed in the hands of the individual officer: he usually has no choice as to the subject of the search or its scope.<sup>[11]</sup></p>
<p>In sum, I agree with the Court that the routine inventory search in this case is constitutional.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN and MR. JUSTICE STEWART join, dissenting.</p>
<p>The Court today holds that the Fourth Amendment permits a routine police inventory search of the closed <span class="star-pagination">*385</span> glove compartment of a locked automobile impounded for ordinary traffic violations. Under the Court's holding, such a search may be made without attempting to secure the consent of the owner and without any particular reason to believe the impounded automobile contains contraband, evidence, or valuables, or presents any danger to its custodians or the public.<sup>[1]</sup> Because I believe this holding to be contrary to sound elaboration of established Fourth Amendment principles, I dissent.</p>
<p>As MR. JUSTICE POWELL recognizes, the requirement of a warrant aside, resolution of the question whether an inventory search of closed compartments inside a locked automobile can ever be justified as a constitutionally "reasonable" search<sup>[2]</sup> depends upon a reconciliation of the owner's constitutionally protected privacy interests against governmental intrusion, and legitimate governmental interests furthered by securing the car and its contents. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). The Court fails clearly to articulate the reasons for its reconciliation of these interests in this case, but it is at least clear to me that the considerations <span class="star-pagination">*386</span> alluded to by the Court, and further discussed by MR. JUSTICE POWELL, are insufficient to justify the Court's result in this case.</p>
<p>To begin with, the Court appears to suggest by reference to a "diminished" expectation of privacy, <i>ante,</i> at 368, that a person's constitutional interest in protecting the integrity of closed compartments of his locked automobile may routinely be sacrificed to governmental interests requiring interference with that privacy that are less compelling than would be necessary to justify a search of similar scope of the person's home or office. This has never been the law. The Court correctly observes that some prior cases have drawn distinctions between automobiles and homes or offices in Fourth Amendment cases; but even as the Court's discussion makes clear, the reasons for distinction in those cases are not present here. Thus, <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), permitted certain probable-cause searches to be carried out without warrants in view of the exigencies created by the mobility of automobiles, but both decisions reaffirmed that the standard of probable cause necessary to authorize such a search was no less than the standard applicable to search of a home or office. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51</a></span>; <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#155" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 155-156</a></span>.<sup>[3]</sup> In other contexts the Court has recognized that automobile travel sacrifices some privacy interests to the publicity of plain view, <i>e. g., </i><i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion); cf. <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968). But this recognition, too, is inapposite here, for there is no question of plain view in <span class="star-pagination">*387</span> this case.<sup>[4]</sup> Nor does this case concern intrusions of the scope that the Court apparently assumes would ordinarily be permissible in order to insure the running safety of a car. While it may be that privacy expectations associated with automobile travel are in some regards less than those associated with a home or office, see <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 561-562, it is equally clear that "[t]he word `automobile' is not a talisman in whose presence the Fourth Amendment fades away . . . ," <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>, <span class="star-pagination">*388</span> 461 (1971).<sup>[5]</sup> Thus, we have recognized that "[a] <i>search,</i> even of an automobile, is a substantial invasion of privacy," <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#896" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 896</a></span> (1975) (emphasis added), and accordingly or cases have consistently recognized that the nature and substantiality of interest required to justify <i>a search</i> of private areas of an automobile is no less than that necessary to justify an intrusion of similar scope into a home or office. See, <i>e. g., </i><i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>; </i><i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269-270</a></span> (1973); <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge, supra;</a></span> </i><i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216, 221-222</a></span> (1968); <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964).<sup>[6]</sup></p>
<p><span class="star-pagination">*389</span> The Court's opinion appears to suggest that its result may in any event be justified because the inventory search procedure is a "reasonable" response to</p>
<blockquote>"three distinct needs: the protection of the owner's property while it remains in police custody . . . ; the protection of the police against claims or disputes over lost or stolen property . . . ; and the protection of the police from potential danger." <i>Ante,</i> at 369.<sup>[7]</sup></blockquote>
<p>This suggestion is flagrantly misleading, however, because the record of this case explicitly belies any relevance of the last two concerns. In any event it is my view that none of these "needs," separately or together, can suffice to justify the inventory search procedure approved by the Court.</p>
<p>First, this search cannot be justified in any way as a safety measure, forthough the Court ignores itthe sole purpose given by the State for the Vermillion police's inventory procedure was to secure <i>valuables,</i> Record 75, 98. Nor is there any indication that the officer's search in this case was tailored in any way to safety concerns, or that ordinarily it is so circumscribed. Even aside from the actual basis for the police practice in this case, however, I do not believe that any blanket safety argument could justify a program of routine <span class="star-pagination">*390</span> searches of the scope permitted here. As MR. JUSTICE POWELL recognizes, ordinarily "there is little danger associated with impounding unsearched automobiles," <i>ante,</i> at 378.<sup>[8]</sup> Thus, while the safety rationale may not be entirely discounted when it is actually relied upon, it surely cannot justify the search of every car upon the basis of undifferentiated possibility of harm; on the contrary, such an intrusion could ordinarily be justified only in those individual cases where the officer's inspection was prompted by specific circumstances indicating the possibility <span class="star-pagination">*391</span> of a particular danger. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21, 27</a></span>; cf. <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#448" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 448</a></span> (1973).</p>
<p>Second, the Court suggests that the search for valuables in the closed glove compartment might be justified as a measure to protect the police against lost property claims. Again, this suggestion is belied by the record, sincealthough the Court declines to discuss itthe South Dakota Supreme Court's interpretation of state law explicitly absolves the police, as "gratuitous depositors," from any obligation beyond inventorying objects in plain view and locking the car. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#159" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 159</a></span> (1975).<sup>[9]</sup> Moreover, as MR. JUSTICE POWELL notes, <i>ante,</i> at 378-379, it may well be doubted that an inventory procedure would in any event work significantly to minimize the frustrations of false claims.<sup>[10]</sup></p>
<p>Finally, the Court suggests that the public interest in protecting valuables that may be found inside a closed compartment of an impounded car may justify the inventory procedure. I recognize the genuineness of this governmental interest in protecting property from pilferage. But even if I assume that the posting of a guard would be fiscally impossible as an alternative means to <span class="star-pagination">*392</span> the same protective end,<sup>[11]</sup> I cannot agree with the Court's conclusion. The Court's result authorizesindeed it appears to requirethe routine search of nearly every<sup>[12]</sup> car impounded.<sup>[13]</sup> In my view, the Constitution does not permit such searches as a matter of routine; absent specific consent, such a search is permissible only in exceptional circumstances of particular necessity.</p>
<p>It is at least clear that any owner might prohibit the police from executing a protective search of his impounded car, since by hypothesis the inventory is conducted for the owner's benefit. Moreover, it is obvious that not everyone whose car is impounded would want it to be searched. Respondent himself proves this; but <span class="star-pagination">*393</span> one need not carry contraband to prefer that the police not examine one's private possessions. Indeed, that preference is the premise of the Fourth Amendment. Nevertheless, according to the Court's result the law may presume that each owner in respondent's position consents to the search. I cannot agree. In my view, the Court's approach is squarely contrary to the law of consent;<sup>[14]</sup> it ignores the duty, in the absence of consent, to analyze in each individual case whether there is a need to search a particular car for the protection of its owner which is sufficient to outweigh the particular invasion. It is clear to me under established principles that in order to override the absence of explicit consent, such a search must at least be conditioned upon the fulfillment of two requirements.<sup>[15]</sup> First, there must be specific cause to believe that a search of the scope to be undertaken is necessary in order to preserve the integrity of particular valuable property threatened by the impoundment:</p>
<blockquote>"[I]n justifying the particular intrusion the police officer must be able to point to specific and articulable facts which . . . reasonably warrant that intrusion." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span>.</blockquote>
<p>Such a requirement of "specificity in the information upon which police action is predicated is the central teaching of this Court's Fourth Amendment jurisprudence," <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">id.,</a></span></i> at 21 n. 18, for "[t]he basic purpose of this <span class="star-pagination">*394</span> Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 883-884</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#448" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 448</a></span>; <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 27</a></span>. Second, even where a search might be appropriate, such an intrusion may only follow the exhaustion and failure of reasonable efforts under the circumstances to identify and reach the owner of the property in order to facilitate alternative means of security or to obtain his consent to the search, for in this context the right to refuse the search remains with the owner. Cf. <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span> (1968).<sup>[16]</sup></p>
<p>Because the record in this case shows that the procedures followed by the Vermillion police in searching respondent's car fall far short of these standards, in my view the search was impermissible and its fruits must be suppressed. First, so far as the record shows, the police in this case had no reason to believe that the glove compartment of the impounded car contained particular property of any substantial value. Moreover, the owner had apparently thought it adequate to protect whatever he left in the car overnight on the street in a business area simply to lock the car, and there is nothing in the record to show that the impoundment <span class="star-pagination">*395</span> lot would prove a less secure location against pilferage,<sup>[17]</sup> cf. <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#707" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699, 707</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#89" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84, 89</a></span> (1971), particularly when it would seem likely that the owner would claim his car and its contents promptly, at least if it contained valuables worth protecting.<sup>[18]</sup> Even if the police had cause to believe that the impounded car's glove compartment contained particular valuables, however, they made no effort to secure the owner's consent to the search. Although the Court relies, as it must, upon the fact that respondent was not present to make other arrangements for the care of his belongings, <i>ante,</i> at 375, in my view that is not the end of the inquiry. Here the police readily ascertained the ownership of the vehicle, Record 98-99, yet they searched it immediately without taking any steps to locate respondent and procure his consent to the inventory or advise him to make alternative arrangements to safeguard his property, <i>id.,</i> at 32, 72, 73, 79. Such a failure is inconsistent with the rationale that the inventory procedure is carried out for the benefit of the owner.</p>
<p>The Court's result in this case elevates the conservation of property interestsindeed mere possibilities of property interestsabove the privacy and security interests <span class="star-pagination">*396</span> protected by the Fourth Amendment. For this reason I dissent. On the remand it should be clear in any event that this Court's holding does not preclude a contrary resolution of this case or others involving the same issues under any applicable state law. See <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#726" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 726</a></span> (1975) (MARSHALL, J., dissenting).</p>
<p>Statement of MR. JUSTICE WHITE.</p>
<p>Although I do not subscribe to all of my Brother MARSHALL'S dissenting opinion, particularly some aspects of his discussion concerning the necessity for obtaining the consent of the car owner, I agree with most of his analysis and conclusions and consequently dissent from the judgment of the Court.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed by <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>S. Clark Moore,</i> Assistant Attorney General, and <i>Kent L. Richland</i> and <i>Robert R. Anderson,</i> Deputy Attorneys General, for the State of California; by <i>Theodore L. Sendak,</i> Attorney General, and <i>Donald P. Bogard,</i> Executive Assistant Attorney General, for the State of Indiana; by <i>Toney Anaya,</i> Attorney General, and <i>Warren O. F. Harris,</i> Deputy Attorney General, for the State of New Mexico; and by <i>Wayne W. Schmidt</i> for Americans for Effective Law Enforcement, Inc.</p>
<p>[1]  At respondent's trial, the officer who conducted the inventory testified as follows:
</p>
<p>"Q. And why did you inventory this car?</p>
<p>"A. Mainly for safekeeping, because we have had a lot of trouble in the past of people getting into the impound lot and breaking into cars and stealing stuff out of them.</p>
<p>"Q. Do you know whether the vehicles that were broken into . . . were locked or unlocked?</p>
<p>"A. Both of them were locked, they would be locked." Record 74. In describing the impound lot, the officer stated:</p>
<p>"A. It's the old county highway yard. It has a wooden fence partially around part of it, and kind of a dilapidated wire fence, a makeshift fence." <i>Id.,</i> at 73.</p>
<p>[2]  In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), the Court held that a warrant was required to effect an unconsented administrative entry into and inspection of private dwellings or commercial premises to ascertain health or safety conditions. In contrast, this procedure has never been held applicable to automobile inspections for safety purposes.</p>
<p>[3]  The New York Court of Appeals has noted that in New York City alone, 108,332 cars were towed away for traffic violations during 1969. <i>People</i> v. <i>Sullivan,</i> 29 N. Y. 2d 69, 71, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#465" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d 464, 465</a></span> (1971).</p>
<p>[4]  In contrast to state officials engaged in everyday caretaking functions:
</p>
<p>"The contact with vehicles by federal law enforcement officers usually, if not always, involves the detection or investigation of crimes unrelated to the operation of a vehicle." <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#440" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 440</a></span> (1973).</p>
<p>[5]  In analyzing the issue of reasonableness <i>vel non,</i> the courts have not sought to determine whether a protective inventory was justified by "probable cause." The standard of probable cause is peculiarly related to criminal investigations, not routine, noncriminal procedures. See generally Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 850-851 (1974). The probable-cause approach is unhelpful when analysis centers upon the reasonableness of routine administrative caretaking functions, particularly when no claim is made that the protective procedures are a subterfuge for criminal investigations.
</p>
<p>In view of the noncriminal context of inventory searches, and the inapplicability in such a setting of the requirement of probable cause, courts have heldand quite correctlythat search warrants are not required, linked as the warrant requirement textually is to the probable-cause concept. We have frequently observed that the warrant requirement assures that legal inferences and conclusions as to probable cause will be drawn by a neutral magistrate unrelated to the criminal investigative-enforcement process. With respect to noninvestigative police inventories of automobiles lawfully within governmental custody, however, the policies underlying the warrant requirement, to which MR. JUSTICE POWELL refers, are inapplicable.</p>
<p>[6]  Given the benign noncriminal context of the intrusion, see <i>Wyman</i> v. <i>James,</i> <span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#317" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 317</a></span> (1971), some courts have concluded that an inventory does not constitute a search for Fourth Amendment purposes. See, <i>e. g., </i><i>People</i> v. <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#77" aria-description="Citation for case: People v. Sullivan"><i>Sullivan, supra,</i> at 77</a></span>, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#469" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d, at 469</a></span>; <i>People</i> v. <i>Willis,</i> <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">46 Mich. App. 436</a></span>, <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">208 N. W. 2d 204</a></span> (1973); <i>State</i> v. <i>Wallen,</i> <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/#49" aria-description="Citation for case: State v. Wallen">185 Neb. 44, 49-50</a></span>, <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/#376" aria-description="Citation for case: State v. Wallen">173 N. W. 2d 372, 376</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/912/">399 U. S. 912</a></span> (1970). Other courts have expressed doubts as to whether the intrusion is classifiable as a search. <i>State</i> v. <i>All,</i> 17 N. C. App. 284, 286, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/#772" aria-description="Citation for case: State v. All">193 S. E. 2d 770, 772</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973). Petitioner, however, has expressly abandoned the contention that the inventory in this case is exempt from the Fourth Amendment standard of reasonableness. Tr. of Oral Arg. 5.</p>
<p>[7]  In <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>,</i> the owner had been arrested on narcotics charges, and the car was taken into custody pursuant to the state forfeiture statute. The search was conducted several months before the forfeiture proceedings were actually instituted.</p>
<p>[8]  There was, of course, no certainty at the time of the search that forfeiture proceedings would ever be held. Accordingly, there was no reason for the police to assume automatically that the automobile would eventually be forfeited to the State. Indeed, as the California Court of Appeal stated, "[T]he instant record nowhere discloses that forfeiture proceedings were instituted in respect to defendant's car . . . ." <i>People</i> v. <i>Cooper,</i> <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#596" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d 587, 596</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#489" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr. 483, 489</a></span> (1965). No reason would therefore appear to limit <i>Cooper</i> to an impoundment pursuant to a forfeiture statute.</p>
<p>[9]  The Court expressly noted that the legality of the inventory was not presented, since the evidence was discovered at the point when the officer was taking protective measures to secure the automobile from the elements. But the Court clearly held that the officer acted properly in opening the car for protective reasons.</p>
<p>[10]  The inventory was not unreasonable in scope. Respondent's motion to suppress in state court challenged the inventory only as to items inside the car not in plain view. But once the policeman was lawfully inside the car to secure the personal property in plain view, it was not unreasonable to open the unlocked glove compartment, to which vandals would have had ready and unobstructed access once inside the car.
</p>
<p>The "consent" theory advanced by the dissent rests on the assumption that the inventory is exclusively for the protection of the car owner. It is not. The protection of the municipality and public officers from claims of lost or stolen property and the protection of the public from vandals who might find a firearm, <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>,</i> or as here, contraband drugs, are also crucial.</p>
<p>[1]  Routine inventories of automobiles intrude upon an area in which the private citizen has a "reasonable expectation of privacy." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967) (Harlan, J., concurring). Thus, despite their benign purpose, when conducted by government officials they constitute "searches" for purposes of the Fourth Amendment. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, 18 n. 15 (1968); <i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468</a></span> (CA8 1973); <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#709" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699, 709-710</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#90" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84, 90-91</a></span> (1971) (en banc). Cf. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 591</a></span> (1974) (plurality opinion).</p>
<p>[2]  The principal decisions relied on by the State to justify the inventory search in this case, <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); and <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973), each relied in part on significant factors not found here. <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> only involved an application of the "plain view" doctrine. In <i>Cooper</i> the Court validated an automobile search that took place one week after the vehicle was impounded on the theory that the police had a possessory interest in the car based on a state forfeiture statute requiring them to retain it some four months until the forfeiture sale. See <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>. Finally, in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> the Court held that the search of an automobile trunk "which the officer reasonably believed to contain a gun" was not unreasonable within the meaning of the Fourth and Fourteenth Amendments. 413 U. S., at 448. See also <i>id.,</i> at 436-437. The police in a typical inventory search case, however, will have no reasonable belief as to the particular automobile's contents. And, although the police in this case knew with certainty that there were items of personal property within the exposed interior of the car <i>i. e.,</i> the watch on the dashboardsee <i>ante,</i> at 366, this information alone did not, in the circumstances of this case, provide additional justification for the search of the closed console glove compartment in which the contraband was discovered.</p>
<p>[3]  The interest in protecting the police from liability for lost or stolen property is not relevant in this case. Respondent's motion to suppress was limited to items inside the automobile not in plain view. And, the Supreme Court of South Dakota here held that the removal of objects in plain view, and the closing of windows and locking of doors, satisfied any duty the police department owed the automobile's owner to protect property in police possession. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#159" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 159</a></span> (1975).</p>
<p>[4]  See <i>Mozzetti</i> v. <i>Superior Court, supra,</i> at 709-710, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#90" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d, at 90-91</a></span>.</p>
<p>[5]  See Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 853 (1974).</p>
<p>[6]  A complete "inventory report" is required of all vehicles impounded by the Vermillion Police Department. The standard inventory consists of a survey of the vehicle's exteriorwindows, fenders, trunk, and hoodapparently for damage, and its interior, to locate "valuables" for storage. As part of each inventory a standard report form is completed. The report in this case listed the items discovered in both the automobile's interior and the unlocked glove compartment. The only notation regarding the trunk was that it was locked. A police officer testified that all impounded vehicles are searched, that the search always includes the glove compartment, and that the trunk had not been searched in this case because it was locked. See Record 33-34, 73-79.</p>
<p>[7]  As part of their inventory search the police may discover materials such as letters or checkbooks that "touch upon intimate areas of an individual's personal affairs," and "reveal much about a person's activities, associations, and beliefs." <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 78-79</a></span> (1974) (POWELL, J., concurring). See also <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span>, 401 n. 7 (1976). In this case the police found, <i>inter alia,</i> "miscellaneous papers," a checkbook, an installment loan book, and a social security status card. Record 77. There is, however, no evidence in the record that in carrying out their established inventory duties the Vermillion police do other than search for and remove for storage such property without examining its contents.</p>
<p>[8]  The Amendment provides that
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[9]  This difference turns primarily on the mobility of the automobile and the impracticability of obtaining a warrant in many circumstances, <i>e. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span> (1925). The lesser expectation of privacy in an automobile also is important. See <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span>, 896 n. 2 (1975); <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 590</a></span>; <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (POWELL, J., concurring). See <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 441-442</a></span>.</p>
<p>[10]  See, <i>e. g., </i><i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span> (1967); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-177</a></span> (1949); <i>Carroll</i> v. <i>United States, supra,</i> at 153, 156. See also <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454-456</a></span> (1948); <i>United States</i> v. <i>Mapp,</i> <span class="citation" data-id="310049"><a href="/opinion/310049/united-states-v-edward-mapp-aka-sonny-woods/#76" aria-description="Citation for case: United States v. Edward Mapp, A/K/A Sonny Woods">476 F. 2d 67, 76</a></span> (CA2 1973) (listing then-recognized exceptions to warrant requirement: (i) hot pursuit; (ii) plain-view doctrine; (iii) emergency situation; (iv) automobile search; (v) consent; and (vi) incident to arrest).</p>
<p>[11]  In this case, for example, the officer who conducted the search testified that the offending automobile was towed to the city impound lot after a second ticket had been issued for a parking violation. The officer further testified that all vehicles taken to the lot are searched in accordance with a "standard inventory sheet" and "all items [discovered in the vehicles] are removed for safekeeping." Record 74. See n. 6, <i>supra.</i></p>
<p>[1]  The Court does not consider, however, whether the police might open and search the glove compartment if it is locked, or whether the police might search a locked trunk or other compartment.</p>
<p>[2]  I agree with MR. JUSTICE POWELL's conclusion, <i>ante,</i> at 377 n. 1, that, as petitioner conceded, Tr. of Oral Arg. 5, the examination of the closed glove compartment in this case is a "search." See <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 530</a></span> (1967): "It is surely anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior." See also <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967), quoted in n. 5, <i>infra.</i> Indeed, the Court recognized in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968), that the procedure invoked here would constitute a search for Fourth Amendment purposes.</p>
<p>[3]  This is, of course, "probable cause in the sense of specific knowledge about a particular automobile." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#281" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 281</a></span> (1973) (POWELL, J., concurring).</p>
<p>[4]  In its opinion below, the Supreme Court of South Dakota stated that in its view the police were constitutionally justified in entering the car to remove, list, and secure objects in plain view from the outside of the car. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#158" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 158-159</a></span> (1975). This issue is not presented on certiorari here.
</p>
<p>Contrary to the Court's assertion, however, <i>ante,</i> at 375-376, the search of respondent's car was not in any way "prompted by the presence in plain view of a number of valuables inside the car." In fact, the record plainly states that every vehicle taken to the city impound lot was inventoried, Record 33, 74, 75, and that as a matter of "standard procedure," "every inventory search" would involve entry into the car's closed glove compartment. <i>Id.,</i> at 43, 44. See also Tr. of Oral Arg. 7. In any case, as MR. JUSTICE POWELL recognizes, <i>ante,</i> at 377-378, n. 2, entry to remove plain-view articles from the car could not justify a further search into the car's closed areas. Cf. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763, 764-768</a></span> (1969). Despite the Court's confusion on this pointfurther reflected by its discussion of <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84</a></span> (1971), <i>ante,</i> at 371, and its reliance on state and lower federal-court cases approving nothing more than inventorying of plain-view items, <i>e. g., </i><i>Barker</i> v. <i>Johnson,</i> <span class="citation" data-id="313477"><a href="/opinion/313477/daniel-barker-v-dale-johnson/" aria-description="Citation for case: Daniel Barker v. Dale Johnson">484 F. 2d 941</a></span> (CA6 1973); <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960</a></span> (CA9 1972); <i>United States</i> v. <i>Fuller,</i> <span class="citation" data-id="1868897"><a href="/opinion/1868897/united-states-v-fuller/" aria-description="Citation for case: United States v. Fuller">277 F. Supp. 97</a></span> (DC 1967), conviction aff'd, 139 U. S. App. D. C. 375, <span class="citation" data-id="292850"><a href="/opinion/292850/morris-fuller-v-united-states/" aria-description="Citation for case: Morris Fuller v. United States">433 F. 2d 533</a></span> (1970); <i>State</i> v. <i>Tully,</i> <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/" aria-description="Citation for case: State v. Tully">166 Conn. 126</a></span>, <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/" aria-description="Citation for case: State v. Tully">348 A. 2d 603</a></span> (1974); <i>State</i> v. <i>Achter,</i> <span class="citation" data-id="1770477"><a href="/opinion/1770477/state-v-achter/" aria-description="Citation for case: State v. Achter">512 S. W. 2d 894</a></span> (Mo. Ct. App. 1974); <i>State</i> v. <i>All,</i> 17 N. C. App. 284, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/" aria-description="Citation for case: State v. All">193 S. E. 2d 770</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973)I must conclude that the Court's holding also permits the intrusion into a car and its console even in the absence of articles in plain view.</p>
<p>[5]  Moreover, as the Court observed in <i>Cooper</i> v. <i>California, supra,</i> at 61: " `[L]awful custody of an automobile does not of itself dispense with constitutional requirements of searches thereafter made of it.' "</p>
<p>[6]  It would be wholly unrealistic to say that there is no reasonable and actual expectation in maintaining the privacy of closed compartments of a locked automobile, when it is customary for people in this day to carry their most personal and private papers and effects in their automobiles from time to time. Cf. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352</a></span> (1967) (opinion of the Court); <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span> (Harlan, J., concurring). Indeed, this fact is implicit in the very basis of the Court's holdingthat such compartments may contain valuables in need of safeguarding.
</p>
<p>MR. JUSTICE POWELL observes, <i>ante,</i> at 380, and n. 7, that the police would not be justified in sifting through papers secured under the procedure employed here. I agree with this, and I note that the Court's opinion does not authorize the inspection of suitcases, boxes, or other containers which might themselves be sealed, removed, and secured without further intrusion. See, <i>e. g., </i><i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468</a></span> (CA8 1973); <i>State</i> v. <i>McDougal,</i> <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/" aria-description="Citation for case: State v. McDougal">68 Wis. 2d 399</a></span>, <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/" aria-description="Citation for case: State v. McDougal">228 N. W. 2d 671</a></span> (1975); <i>Mozzetti</i> v. <i>Superior Court, supra</i><i>.</i> But this limitation does not remedy the Fourth Amendment intrusion when the simple inventorying of closed areas discloses tokens, literature, medicines, or other things which on their face may "reveal much about a person's activities, associations, and beliefs," <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 78-79</a></span> (1974) (POWELL, J., concurring).</p>
<p>[7]  The Court also observes that "[i]n addition, police frequently attempt to determine whether a vehicle has been stolen and thereafter abandoned." <i>Ante,</i> at 369. The Court places no reliance on this concern in this case, however, nor could it. There is no suggestion that the police suspected that respondent's car was stolen, or that their search was directed at, or stopped with, a determination of the car's ownership. Indeed, although the police readily identified the car as respondent's, Record 98-99, the record does not show that they ever sought to contact him.</p>
<p>[8]  The very premise of the State's chief argument, that the cars must be searched in order to protect valuables because no guard is posted around the vehicles, itself belies the argument that they must be searched at the city lot in order to protect the police there. These circumstances alone suffice to distinguish the dicta from <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>, recited by the Court, <i>ante,</i> at 373.
</p>
<p>The Court suggests a further "crucial" justification for the search in this case: "protection of the <i>public</i> from vandals who might find a firearm, <i>Cady</i> v. <i>Dombrowski,</i> [<span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973)], or as here, contraband drugs" (emphasis added). <i>Ante,</i> at 376 n. 10. This rationale, too, is absolutely without support in this record. There is simply no indication the police were looking for dangerous items. Indeed, even though the police found shotgun shells in the interior of the car, they never opened the trunk to determine whether it might contain a shotgun. Cf. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady, supra</a></span></i><i>.</i> Aside from this, the suggestion is simply untenable as a matter of law. If this asserted rationale justifies search of all impounded automobiles, it must logically also justify the search of <i>all</i> automobiles, whether impounded or not, located in a similar area, for the argument is not based upon the custodial role of the police. See also <i>Cooper</i> v. <i>California, supra,</i> at 61, quoted in n. 5, <i>supra.</i> But this Court has never permitted the search of any car or home on the mere undifferentiated assumption that it might be vandalized and the vandals might find dangerous weapons or substances. Certainly <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>,</i> permitting a limited search of a wrecked automobile where, <i>inter alia,</i> the police had a reasonable belief that the car contained a specific firearm, 413 U. S., at 448, does not so hold.</p>
<p>[9]  Even were the State to impose a higher standard of custodial responsibility upon the police, however, it is equally clear that such a requirement must be read in light of the Fourth Amendment's pre-eminence to require protective measures other than interior examination of closed areas.</p>
<p>[10]  Indeed, if such claims can be deterred at all, they might more effectively be deterred by sealing the doors and trunk of the car so that an unbroken seal would certify that the car had not been opened during custody. See <i>Cabbler</i> v. <i>Superintendent,</i> <span class="citation" data-id="2353003"><a href="/opinion/2353003/cabbler-v-superintendent-virginia-state-penitentiary/#700" aria-description="Citation for case: Cabbler v. Superintendent, Virginia State Penitentiary">374 F. Supp. 690, 700</a></span> (ED Va. 1974), rev'd, <span class="citation" data-id="332335"><a href="/opinion/332335/herbert-w-cabbler-v-superintendent-virginia-state-penitentiary/" aria-description="Citation for case: Herbert W. Cabbler v. Superintendent, Virginia State...">528 F. 2d 1142</a></span> (CA4 1975), cert. pending, No. 75-1463.</p>
<p>[11]  I do not believe, however, that the Court is entitled to make this assumption, there being no such indication in the record. Cf. <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 447</a></span>.</p>
<p>[12]  The Court makes clear, <i>ante,</i> at 375, that the police may not proceed to search an impounded car if the owner is able to make other arrangements for the safekeeping of his belongings. Additionally, while the Court does not require consent before a search, it does not hold that the police may proceed with such a search in the face of the owner's denial of permission. In my view, if the owner of the vehicle is in police custody or otherwise in communication with the police, his consent to the inventory is prerequisite to an inventory search. See <i>Cabbler</i> v. <i>Superintendent, supra,</i> at 700; cf. <i>State</i> v. <i>McDougal,</i> <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/#413" aria-description="Citation for case: State v. McDougal">68 Wis. 2d, at 413</a></span>, <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/#678" aria-description="Citation for case: State v. McDougal">228 N. W. 2d, at 678</a></span>; <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#708" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d, at 708</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#89" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d, at 89</a></span>.</p>
<p>[13]  In so requiring, the Court appears to recognize that a search of some, but not all, cars which there is no specific cause to believe contain valuables would itself belie any asserted property-securing purpose.
</p>
<p>The Court makes much of the fact that the search here was a routine procedure, and attempts to analogize <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>.</i> But it is quite clear that the routine in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> was only to search where there was a reasonable belief that the car contained a dangerous weapon, 413 U. S., at 443; see <i>Dombrowski</i> v. <i>Cady,</i> <span class="citation" data-id="8783591"><a href="/opinion/8799464/dombrowski-v-cady/#532" aria-description="Citation for case: Dombrowski v. Cady">319 F. Supp. 530, 532</a></span> (ED Wis. 1970), not, as here, to search every car in custody without particular cause.</p>
<p>[14]  Even if it may be true that many persons would ordinarily consent to a protective inventory of their car upon its impoundment, this fact is not dispositive since even a majority lacks authority to consent to the search of <i>all</i> cars in order to assure the search of theirs. Cf. <i>United States</i> v. <i>Matlock,</i> <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 171</a></span> (1974); <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964).</p>
<p>[15]  I need not consider here whether a warrant would be required in such a case.</p>
<p>[16]  Additionally, although not relevant on this record, since the inventory procedure is premised upon benefit to the owner, it cannot be executed in any case in which there is reason to believe the owner would prefer to forgo it. This principle, which is fully consistent with the Court's result today, requires, for example, that when the police harbor suspicions (amounting to less than probable cause) that evidence or contraband may be found inside the automobile, they may not inventory it, for they must presume that the owner would refuse to permit the search.</p>
<p>[17]  While evidence at the suppression hearing suggested that the inventory procedures were prompted by past thefts at the impound lot, the testimony refers to only two such thefts, see <i>ante,</i> at 366 n. 1, over an undisclosed period of time. There is no reason on this record to believe that the likelihood of pilferage at the lot was higher or lower than that on the street where respondent left his car with valuables in plain view inside. Moreover, the failure of the police to secure such frequently stolen items as the car's battery, suggests that the risk of loss from the impoundment was not in fact thought severe.</p>
<p>[18]  In fact respondent claimed his possessions about five hours after his car was removed from the street. Record 39, 93.</p>

</div>
```

---

## GROUP: content/cases/Stone v. Powell.md  (`case`, 5 assertions)

### content_page

```
---
title: Stone v. Powell
type: case
citation: "428 U.S. 465 (1976)"
parallel_cite: "96 S. Ct. 3037; 49 L. Ed. 2d 1067"
neutral_cite: 1976 U.S. LEXIS 86
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-10-04
docket: No. 74-1055
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
  opinion_url: "https://www.courtlistener.com/opinion/109540/stone-v-powell/"
  cluster_id: 109540
  opinion_id: null
  identity_checked: true
lake:
  record_id: Stone v. Powell
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Mapp v. Ohio]]"
  - "[[United States v. Calandra]]"
  - "[[United States v. Janis]]"
  - "[[United States v. Leon]]"
tags:
  - case
  - fourth-amendment
  - exclusionary-rule
  - habeas-corpus
  - deterrence
  - collateral-review
holding: "Where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial; the exclusionary rule's deterrent purpose is not meaningfully served by relitigating settled Fourth Amendment claims on collateral review."
aliases:
  - Stone v. Powell
  - "Stone v. Powell (1976)"
---

# Stone v. Powell

*428 U.S. 465 (1976)* (No. 74-1055) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109540 → combined opinion 109540 (Powell, J.; 428 U.S. 465, argued Feb. 24, 1976, decided July 6, 1976; consolidated with No. 74-1222, Wolff v. Rice). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*494`). S9 promotes. -->

## Background
Lloyd Powell was convicted of murder in a California state court after a killing during a liquor-store altercation. Ten hours later, a Nevada officer arrested him under a local vagrancy ordinance, and a search incident to that arrest turned up a .38 revolver later identified as the murder weapon. Powell argued the vagrancy ordinance was unconstitutional, so the arrest and search were unlawful and the revolver evidence should have been excluded; he litigated that Fourth Amendment claim in the California courts and lost. He then sought federal [[Common Legal Terms#habeas-corpus|habeas corpus]], and the Ninth Circuit granted relief. In a companion case (*Wolff v. Rice*), a Nebraska prisoner similarly obtained federal [[Common Legal Terms#habeas-corpus|habeas]] relief on a Fourth Amendment claim. The State wardens sought review.

## Issue
Whether a federal court, on a state prisoner's petition for [[Common Legal Terms#habeas-corpus|habeas corpus]], should entertain a claim that evidence obtained in an unconstitutional search or seizure was admitted at trial, when the prisoner already had an opportunity for full and fair litigation of that claim in the state courts.

## Rule
Reasoning that the exclusionary rule is a judicially created deterrent remedy rather than a personal constitutional right, the Court weighed its marginal deterrent value on collateral review against the costs of excluding reliable evidence and disrupting final state judgments, and found the balance decisively against relitigation. It held: "In sum, we conclude that where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial." — 428 U.S. at 494. ^pin-494

## Application
Whatever added deterrence federal [[Common Legal Terms#habeas-corpus|habeas]] review might supply in isolated cases, it would come long after the police conduct, would fall on officers who had no way to anticipate a later collateral ruling, and would be swamped by the costs to truth-seeking and finality — the diversion of the trial from guilt or innocence, the release of the plainly guilty, and the erosion of respect for the criminal-justice system. Because Powell and Rice had each been afforded a full and fair opportunity to press their Fourth Amendment claims in state court, no further federal [[Common Legal Terms#habeas-corpus|habeas]] remedy was constitutionally required.

## Conclusion
The judgments of the Courts of Appeals were **reversed**. Powell, J., delivered the opinion of the Court. Burger, C.J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, J., joined; White, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Stone* is an exclusionary-rule anchor for the deterrence-and-cost framework and its limits on where the rule reaches: on federal [[Common Legal Terms#habeas-corpus|habeas]], a fully and fairly litigated Fourth Amendment claim is not a ground for relief. It belongs with the cost-benefit line — *[[United States v. Calandra]]* (grand jury), *[[United States v. Janis]]* (civil tax), and later *[[United States v. Leon]]* (good faith) — that treats suppression as a deterrent remedy applied only where its benefits outweigh its costs, all downstream of *[[Mapp v. Ohio]]*.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*Stone v. Powell*, 428 U.S. 465 (1976)](https://www.courtlistener.com/opinion/109540/stone-v-powell/) — pinpoint: 494 (Powell, J., for the Court; the CL opinion text places the quoted "In sum" holding between the reporter stars `*494` and `*495`, i.e., on page 494; the dissent cites the same holding as "Ante, at 494"). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f734ebc7d31a300", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "428 U.S. 465 (1976)", "court": "U.S. Supreme Court", "neutral_cite": "1976 U.S. LEXIS 86", "official_citation_present": true, "parallel_cite": "96 S. Ct. 3037; 49 L. Ed. 2d 1067", "title": "Stone v. Powell", "year": "1976"}}
{"assertion_id": "54ff8c7a859294c1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial; the exclusionary rule's deterrent purpose is not meaningfully served by relitigating settled Fourth Amendment claims on collateral review.", "title": "Stone v. Powell"}}
{"assertion_id": "c973cee1eb073b1e", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Anchor", "title": "Stone v. Powell"}}
{"assertion_id": "98d8b386eff308fa", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Stone v. Powell", "varies_by_point": "false"}}
{"assertion_id": "d6bb5c63bc2063c8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Stone v. Powell"}}
```

### lake record — Stone v. Powell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stone v. Powell",
  "status": "under_review",
  "identity": {
    "case_name": "Stone v. Powell",
    "case_name_short": "Powell",
    "case_name_full": "Stone, Warden v. Powell",
    "input_case_name": "Stone v. Powell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-10-04",
    "year": 1976,
    "docket": "No. 74-1055",
    "cluster_id": 109540,
    "lead_opinion_id": 9426587,
    "sibling_ids": [],
    "absolute_url": "/opinion/109540/stone-v-powell/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 465",
      "volume": "428",
      "reporter": "U.S.",
      "page": "465",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3037",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3037",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1067",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 86",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 465",
        "volume": "428",
        "reporter": "U.S.",
        "page": "465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3037",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3037",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1067",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1067",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 86",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "86",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 465",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 465",
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
    "date_created": "2026-07-06T13:42:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:42:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "stone-v-powell--109540",
      "to_record_id": "Stone v. Powell",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Stone v. Powell

```
<opinion type="majority">
<author id="b492-4"><page-number citation-index="1" label="468">*468</page-number>Mr. Justice Powell</author>
<p id="A4I">delivered the opinion of the Court.</p>
<p id="b492-5">Respondents in these cases were convicted of criminal offenses in state courts, and their convictions were affirmed on appeal. The prosecution in each case relied upon evidence obtained by searches and seizures alleged by respondents to have been unlawful. Each respondent subsequently sought relief in a Federal District Court by filing a petition for a writ of federal habeas corpus under <page-number citation-index="1" label="469">*469</page-number><span class="citation no-link">28 U. S. C. § 2254</span>. The question presented is whether a federal court should consider, in ruling on a petition for habeas corpus relief filed by a state prisoner, a claim that evidence obtained by an unconstitutional search or seizure was introduced at his trial, when he has previously been afforded an opportunity for full and fair litigation of his claim in the state courts. The issue is of considerable importance to the administration of criminal justice.</p>
<p id="b493-4">I</p>
<p id="b493-5">We summarize first the relevant facts and procedural history of these cases.</p>
<p id="b493-6">A</p>
<p id="b493-7">Respondent Lloyd Powell was convicted of murder in June 1968 after trial in a California state court. At about midnight on February 17, 1968, he and three companions entered the Bonanza Liquor Store in San Ber-nardino, Cal., where Powell became involved in an altercation with Gerald Parsons, the store manager, over the theft of a bottle of wine. In the scuffling that followed Powell shot and killed Parsons’ wife. Ten hours later an officer of the Henderson, Nev., Police Department arrested Powell for violation of the Henderson vagrancy ordinance,<footnotemark>1</footnotemark> and in the search incident to the arrest discovered a .38-caliber revolver with six expended cartridges in the cylinder.</p>
<p id="b493-8">Powell was extradited to California and convicted of <page-number citation-index="1" label="470">*470</page-number>second-degree murder in the Superior Court of San Ber-nardino County. Parsons and Powell’s accomplices at the liquor store testified against him. A criminologist testified that the revolver found on Powell was the gun that killed Parsons’ wife. The trial court rejected Powell’s contention that testimony by the Henderson police officer as to the search and the discovery of the revolver should have been excluded because the vagrancy ordinance was unconstitutional. In October 1969, the conviction was affirmed by a California District Court of Appeal. Although the issue was duly presented, that court found it unnecessary to pass upon the legality of the arrest and search because it concluded that the error, if any, in admitting the testimony of the Henderson officer was harmless beyond a reasonable doubt under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). The Supreme Court of California denied Powell’s petition for habeas corpus relief.</p>
<p id="b494-5">In August 1971 Powell filed an amended petition for a writ of federal habeas corpus under <span class="citation no-link">28 U. S. C. § 2254</span> in the United States District Court for the Northern District of California, contending that the testimony concerning the .38-caliber revolver should have been excluded as the fruit of an illegal search. He argued that his arrest had been unlawful because the Henderson vagrancy ordinance was unconstitutionally vague, and that the arresting officer lacked probable cause to believe that he was violating it. The District Court concluded that the arresting officer had probable cause and held that even if the vagrancy ordinance was unconstitutional, the deterrent purpose of the exclusionary rule does not require that it be applied to bar admission of the fruits of a search incident to an otherwise valid arrest. In the alternative, that court agreed with the California District Court of Appeal that the admission of the evidence con<page-number citation-index="1" label="471">*471</page-number>cerning Powell’s arrest, if error, was harmless beyond a reasonable doubt.</p>
<p id="b495-5">In December 1974, the Court of Appeals for the Ninth Circuit reversed. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden">507 F. 2d 93</a></span>. The court concluded that the vagrancy ordinance was unconstitutionally vague,<footnotemark>2</footnotemark> that Powell’s arrest was therefore illegal, and that although exclusion of the evidence would serve no deterrent purpose with regard to police officers who were enforcing statutes in good faith, exclusion would serve the public interest by deterring legislators from enacting unconstitutional statutes. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#98" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden"><em>Id., </em>at 98</a></span>. After an independent review of the evidence the court concluded that the admission of the evidence was not harmless error since it supported the testimony of Parsons and Powell’s accomplices. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#99" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden"><em>Id., </em>at 99</a></span>.</p>
<p id="b495-6">B</p>
<p id="b495-7">Respondent David Rice was convicted of murder in April 1971 after trial in a Nebraska state court. At 2:05 a. m. on August 17, 1970, Omaha police received a telephone call that a woman had been heard screaming at 2867 Ohio Street. As one of the officers sent to that address examined a suitcase lying in the doorway, it exploded, killing him instantly. By August 22 the investigation of the murder centered on Duane Peak, a 15-year-old member of the National Committee to Com<page-number citation-index="1" label="472">*472</page-number>bat Fascism (NCCF), and that afternoon a warrant was issued for Peak’s arrest. The investigation also focused on other known members of the NCCF, including Rice, some of whom were believed to be planning to kill Peak before he could incriminate them. In their search for Peak, the police went to Rice’s home at 10:30 that night and found lights and a television on, but there was no response to their repeated knocking. While some officers remained to watch the premises, a warrant was obtained to search for explosives and illegal weapons believed to be in Rice’s possession. Peak was not in the house, but upon entering the police discovered, in plain view, dynamite, blasting caps, and other materials useful in the construction of explosive devices. Peak subsequently was arrested, and on August 27, Rice voluntarily surrendered. The clothes Rice was wearing at that time were subjected to chemical analysis, disclosing dynamite particles.</p>
<p id="b496-5">Rice was tried for first-degree murder in the District Court of Douglas County. At trial Peak admitted planting the suitcase and making the telephone call, and implicated Rice in the bombing plot. As corroborative evidence the State introduced items seized during the search, as well as the results of the chemical analysis of Rice’s clothing. The court denied Rice’s motion to suppress this evidence. On appeal the Supreme Court of Nebraska affirmed the conviction, holding that the search of Rice’s home had been pursuant to a valid search warrant. <em>State </em>v. <em>Rice, </em><span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">188 Neb. 728</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">199 N. W. 2d 480</a></span> (1972).</p>
<p id="b496-6">In September 1972 Rice filed a petition for a writ of habeas corpus in the United States District Court for Nebraska. Rice’s sole contention was that his incarceration was unlawful because the evidence underlying his conviction had been discovered as the result of an illegal <page-number citation-index="1" label="473">*473</page-number>search of his home. The District Court concluded that the search warrant was invalid, as the supporting affidavit was defective under <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), and <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964). <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#190" aria-description="Citation for case: Rice v. Wolff">388 F. Supp. 185, 190-194</a></span> (1974).<footnotemark>3</footnotemark> The court also rejected the State’s contention that even if the warrant was invalid the search was justified because of the valid arrest warrant for Peak and because of the exigent circumstances of the situation — danger to Peak and search for bombs and explosives believed in possession of the NCCF. The court reasoned that the arrest warrant did not justify the entry as the police lacked probable cause to believe Peak was in the house, and further concluded that the circumstances were not sufficiently exigent to justify an immediate warrantless <page-number citation-index="1" label="474">*474</page-number>search. <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#194" aria-description="Citation for case: Rice v. Wolff"><em>Id., </em>at 194-202</a></span>.<footnotemark>4</footnotemark> The Court of Appeals for the Eighth Circuit affirmed, substantially for the reasons stated by the District Court. <span class="citation" data-id="326825"><a href="/opinion/326825/david-l-rice-v-charles-l-wolff-jr-warden-nebraska-penal-and/" aria-description="Citation for case: David L. Rice v. Charles L. Wolff, Jr., Warden, Nebraska...">513 F. 2d 1280</a></span> (1975).</p>
<p id="b498-5">Petitioners Stone and Wolff, the wardens of the respective state prisons where Powell and Rice are incarcerated, petitioned for review of these decisions, raising questions concerning the scope of federal habeas corpus and the role of the exclusionary rule upon collateral review of cases involving Fourth Amendment claims. We granted their petitions for certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./422/1055/">422 U. S. 1055</a></span> (1975).<footnotemark>5</footnotemark> We now reverse.</p>
<p id="b498-6">II</p>
<p id="b498-7">The authority of federal courts to issue the writ of habeas corpus <em>ad subjiciendum </em><footnotemark>6</footnotemark> was included in the first <page-number citation-index="1" label="475">*475</page-number>grant of federal-court jurisdiction, made by the Judiciary Act of 1789, c. 20, § 14, <span class="citation no-link">1 Stat. 81</span>, with the limitation that the writ extend only to prisoners held in custody by the United States. The original statutory authorization did not define the substantive reach of the writ. It merely stated that the courts of the United States “shall have power to issue writs of . . . <em>habeas corpus . . . <span class="citation no-link">Ibid.</span> </em>The courts defined the scope of the writ in accordance with the common law and limited it to an inquiry as to the jurisdiction of the sentencing tribunal. See, <em>e. g., Ex parte Watkins, </em><span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet. 193</a></span> (1830) (Marshall, C. J.).</p>
<p id="b499-5">In 1867 the writ was extended to state prisoners. Act of Feb. 5, 1867, c. 28, § 1, <span class="citation no-link">14 Stat. 385</span>. Under the 1867 Act federal courts were authorized to give relief in “all cases where any person may be restrained of his or her liberty in violation of the constitution, or of any treaty or law of the United States . . . .” But the limitation of federal habeas corpus jurisdiction to consideration of the jurisdiction of the sentencing court persisted. See'; <em>e. g., In re Wood, </em><span class="citation" data-id="93092"><a href="/opinion/93092/in-re-wood/" aria-description="Citation for case: In Re Wood">140 U. S. 278</a></span> <em>(1891); In re Rahrer, </em><span class="citation" data-id="93112"><a href="/opinion/93112/in-re-rahrer/" aria-description="Citation for case: In Re Rahrer">140 U. S. 545</a></span> (1891); <em>Andrews </em>v. <em>Swartz, </em><span class="citation" data-id="94093"><a href="/opinion/94093/andrews-v-swartz/" aria-description="Citation for case: Andrews v. Swartz">156 U. S. 272</a></span> (1895); <em>Bergemann </em>v. <em>Backer, </em><span class="citation" data-id="94176"><a href="/opinion/94176/bergemann-v-backer/" aria-description="Citation for case: Bergemann v. Backer">157 U. S. 655</a></span> (1895); <em>Pettibone </em>v. <em>Nichols, </em><span class="citation" data-id="9418069"><a href="/opinion/96517/pettibone-v-nichols/" aria-description="Citation for case: Pettibone v. Nichols">203 U. S. 192</a></span> (1906). And, although the concept of “jurisdiction” was subjected to considerable strain as the substantive scope of the writ was expanded,<footnotemark>7</footnotemark> this <page-number citation-index="1" label="476">*476</page-number>expansion was limited to only a few classes of cases<footnotemark>8</footnotemark> until <em>Frank </em>v. <em>Mangum, </em><span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309</a></span>, in 1915. In <em><span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">Frank</a></span>, </em>the prisoner had claimed in the state courts that the proceedings which resulted in his conviction for murder had been dominated by a mob. After the State Supreme Court rejected his contentions, Frank unsuccessfully sought habeas corpus relief in the Federal District Court. This Court affirmed the denial of relief because Frank’s federal claims had been considered by a competent and unbiased state tribunal. The Court recognized, however, that if a habeas corpus court found that the State had failed to provide adequate “corrective process” for the full and fair litigation of federal claims, whether or not “jurisdictional,” the court could inquire into the merits to determine whether a detention was lawful. <em>Id,., </em>at 333-336.</p>
<p id="b500-5">In the landmark decision in <em>Brown </em>v. <em>Allen, </em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#482" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 482-487</a></span> (1953), the scope of the writ was expanded still further.<footnotemark>9</footnotemark> In that case and its companion case, <em>Daniels </em>v. <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span>, </em>state prisoners applied for federal habeas corpus relief claiming that the trial courts had erred <page-number citation-index="1" label="477">*477</page-number>in failing to quash their indictments due to alleged discrimination in the selection of grand jurors and in ruling certain confessions admissible. In <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Brown</a></span>, </em>the highest court of the State had rejected these claims oil direct appeal, <em>State </em>v. <em>Brown, </em><span class="citation" data-id="1242993"><a href="/opinion/1242993/state-v-brown/" aria-description="Citation for case: State v. Brown">233 N. C. 202</a></span>, <span class="citation" data-id="1242993"><a href="/opinion/1242993/state-v-brown/" aria-description="Citation for case: State v. Brown">63 S. E. 2d 99</a></span>, and this Court had denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./341/943/">341 U. S. 943</a></span> (1951). Despite the apparent adequacy of the state corrective process, the Court reviewed the denial of the writ of habeas corpus and held that Brown was entitled to a full reconsideration of these constitutional claims, including, if appropriate, a hearing in the Federal District Court. In <em>Daniels, </em>however, the State Supreme Court on direct review had refused to consider the appeal because the papers were filed out of time. This Court held that since the state-court judgment rested on a reasonable application of the State’s legitimate procedural rules, a ground that would have barred direct review of his federal claims by this Court, the District Court lacked authority to grant habeas corpus relief. See <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#458" aria-description="Citation for case: Brown v. Allen">344 U. S., at 458, 486</a></span>.</p>
<p id="b501-5">This final barrier to broad collateral re-examination of state criminal convictions in federal habeas corpus proceedings was removed in <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span> (1963) .<footnotemark>10</footnotemark> Noia and two codefendants had been convicted <page-number citation-index="1" label="478">*478</page-number>of felony murder. The sole evidence against each defendant was a signed confession. Noia’s codefendants, but not Noia himself, appealed their convictions. Although their appeals were unsuccessful, in subsequent state proceedings they were able to establish that their confessions had been coerced and their convictions therefore procured in violation of the Constitution. In a subsequent federal habeas corpus proceeding, it was stipulated that Noia’s confession also had been coerced, but the District Court followed <em>Daniels </em>in holding that Noia’s failure to appeal barred habeas corpus review. See <em>United States </em>v. <em>Fay, </em><span class="citation" data-id="1973566"><a href="/opinion/1973566/united-states-ex-rel-noia-v-fay/#225" aria-description="Citation for case: United States Ex Rel. Noia v. Fay">183 F. Supp. 222, 225</a></span> (SDNY 1960). The Court of Appeals reversed, ordering that Noia’s conviction be set aside and that he be released from custody or that a new trial be granted. This Court affirmed the grant of the writ, narrowly restricting the circumstances in which a federal court may refuse to consider the merits of federal constitutional claims<footnotemark>11</footnotemark></p>
<p id="AeAh">During the period in which the substantive scope of the writ was expanded, the Court did not consider whether exceptions to full review might exist with respect <page-number citation-index="1" label="479">*479</page-number>to particular categories of constitutional claims. Prior to the Court’s decision in <em>Kaufman </em>v. <em>United States, </em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), however, a substantial majority of the Federal Courts of Appeals had concluded that collateral review of search-and-seizure claims was inappropriate on motions filed by federal prisoners under <span class="citation no-link">28 U. S. C. § 2255</span>, the modem postconviction procedure available to federal prisoners in lieu of habeas corpus.<footnotemark>12</footnotemark> The primary rationale advanced in support of those decisions was that Fourth Amendment violations are different in kind from denials of Fifth or Sixth Amendment rights in that claims of illegal search and seizure do not “impugn the integrity of the fact-finding process or challenge evidence as inherently unreliable; rather, the exclusion of illegally seized evidence is simply a prophylactic device intended generally to deter Fourth Amendment violations by law enforcement officers.” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#224" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 224</a></span>. See <em>Thornton </em>v. <em>United States, </em>125 U. S. App. D. C. 114, <span class="citation" data-id="9452299"><a href="/opinion/273740/charles-j-thornton-v-united-states/" aria-description="Citation for case: Charles J. Thornton v. United States">368 F. 2d 822</a></span> (1966).</p>
<p id="b503-5"><em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>rejected this rationale and held that search- and-seizure claims are cognizable in § 2255 proceedings. The Court noted that “the federal habeas remedy extends to state prisoners alleging that unconstitutionally obtained evidence was admitted against them at trial,” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#225" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 225</a></span>, citing, <em>e. g., Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 <page-number citation-index="1" label="480">*480</page-number>U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968), and concluded, as a matter of statutory construction, that there was no basis for restricting “access by federal prisoners with illegal search-and-seizure claims to federal collateral remedies, while placing no similar restriction on access by state prisoners,” <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#226" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 226</a></span>. Although in recent years the view has been expressed that the Court should re-examine the substantive scope of federal habeas jurisdiction and limit collateral review of search-and-seizure claims “solely to the question of whether the petitioner was provided a fair opportunity to raise and have adjudicated the question in state courts,” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973) (Powell, J., concurring),<footnotemark>13</footnotemark> the Court, without discussion or consideration of the issue, has continued to accept jurisdiction in cases raising such claims. See <em>Lefkowitz </em>v. <em>Newsome, </em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">420 U. S. 283</a></span> (1975); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974) (plurality opinion).<footnotemark>14</footnotemark></p>
<p id="b504-5">The discussion in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>of the scope of federal habeas corpus rests on the view that the effectuation of the Fourth Amendment, as applied to the States through the Fourteenth Amendment, requires the granting of habeas corpus relief when a prisoner has been con<page-number citation-index="1" label="481">*481</page-number>victed in state court on the basis of evidence obtained in an illegal search or seizure since those Amendments were held in <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), to require exclusion of such evidence at trial and reversal of conviction upon direct review.<footnotemark>15</footnotemark> Until these cases we have not had occasion fully to consider the validity of this view. See, <em>e. g., Schneckloth </em>v. <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Bustamonte, supra,</a></span> </em>at 249 n. 38; <em>Cardwell </em>v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#596" aria-description="Citation for case: Cardwell v. Lewis"><em>Lewis, supra, </em>at 596</a></span>, and n. 12. Upon examination, we conclude, in light of the nature and purpose of the Fourth Amendment exclusionary rule, that this view is unjustified.<footnotemark>16</footnotemark> We hold, therefore, that <page-number citation-index="1" label="482">*482</page-number>where .the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim, the Constitution does not require that a.state prisoner be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial.<footnotemark>17</footnotemark></p>
<p id="b506-5">Ill</p>
<p id="b506-6">The Fourth Amendment assures the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” The Amendment was primarily a reaction to the evils associated with the use of the general warrant in England and the writs of assistance in the Colonies, <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span> (1965); <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#363" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 363-365</a></span> (1959), and was intended to protect the “sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886), from searches under unchecked general authority.<footnotemark>18</footnotemark></p>
<p id="b506-7">The exclusionary rule was a judicially created means of effectuating the rights secured by the Fourth Amendment. Prior to the Court’s decisions in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span> (1921), there existed no barrier to the introduction in criminal trials of evidence obtained in violation of the Amendment. See <em>Adams </em>v. <em>New York, </em><page-number citation-index="1" label="483">*483</page-number><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904).<footnotemark>19</footnotemark> In <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>the Court held that the defendant could petition before trial for the return of property secured through an illegal search or seizure conducted by federal authorities. In <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>the Court held broadly that such evidence could not be introduced in a federal prosecution. See <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304-305</a></span> (1967). See also <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920) (fruits of illegally seized evidence). Thirty-five years after <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>the Court held in <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949), that the right to be free from arbitrary intrusion by the police that is protected by the Fourth Amendment is “implicit in 'the concept of ordered liberty’ and as such enforceable against the States through the [Fourteenth Amendment] Due Process Clause.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado"><em>Id., </em>at 27-28</a></span>. The Court concluded, however, that the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>exclusionary rule would not be imposed upon the States as “an essential ingredient of [that] right.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#29" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 29</a></span>. The -full force of <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>was eroded in subsequent decisions, see <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960); <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span> (1956), and a little more than a decade later the exclusionary rule was held applicable to the States in <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p id="b508-4"><page-number citation-index="1" label="484">*484</page-number>Decisions prior to <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>advanced two principal reasons for application of the rule in federal trials. The Court in <em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">Elkins</a></span>, </em>for example, in the context of its special supervisory role over the lower federal courts, referred to the “imperative of judicial integrity,” suggesting that exclusion of illegally seized evidence prevents contamination of the judicial process. <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#222" aria-description="Citation for case: Elkins v. United States">364 U. S., at 222</a></span>.<footnotemark>20</footnotemark> But even in that context a more pragmatic ground was emphasized:</p>
<blockquote id="b508-5">“The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it.” <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States"><em>Id., </em>at 217</a></span>.</blockquote>
<p id="b508-6">The <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>majority justified the application of the rule to the States on several grounds,<footnotemark>21</footnotemark> but relied principally upon the belief that exclusion would deter future unlawful police conduct. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 658</a></span>.</p>
<p id="b509-4"><page-number citation-index="1" label="485">*485</page-number>Although our decisions often have alluded to the “imperative of judicial integrity,” <em>e. g., United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975), they demonstrate the limited role of this justification in the determination whether to apply the rule in a particular context.<footnotemark>22</footnotemark> Logically extended this justification would require that courts exclude unconstitutionally seized evidence despite lack of objection by the defendant, or even over his assent. Cf. <em>Henry </em>v. <em>Mississippi, </em><span class="citation" data-id="9422929"><a href="/opinion/106962/henry-v-mississippi/" aria-description="Citation for case: Henry v. Mississippi">379 U. S. 443</a></span> (1965). It also would require abandonment of the standing limitations on who may object to the introduction of unconstitutionally seized evidence, <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969), and retreat from the proposition that judicial proceedings need not abate when the defendant’s person is unconstitutionally seized, <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952). Similarly, the interest in promoting judicial integrity does not prevent the use of illegally seized evidence in grand jury proceedings. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span> (1974). Nor does it require that the trial court exclude such evidence from use for impeachment of a defendant, even though its introduction is certain to result in conviction in some cases. <em>Walder </em>v. <em>United States, </em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954). The teaching of these cases is clear. While courts, of course, must ever be concerned with preserving the integrity of the judicial process, this concern has limited force as a justification for the exclusion of highly probative evidence.<footnotemark>23</footnotemark> <page-number citation-index="1" label="486">*486</page-number>The force of this justification becomes minimal where federal habeas corpus relief is sought by a prisoner who previously has been afforded the opportunity for full and fair consideration of his search-and-seizure claim at trial and on direct review.</p>
<p id="b510-4">The primary justification for the exclusionary rule then is the deterrence of police conduct that violates Fourth Amendment rights. <em>Post-Mapp </em>decisions have established that the rule is not a personal constitutional right. It is not calculated to redress the injury to the privacy of the victim of the search or seizure, for any “ [r] eparation comes too late.” <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#637" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 637</a></span> (1965). Instead,</p>
<blockquote id="b510-5">“the rule is a judicially created remedy designed to safeguard Fourth Amendment rights generally through its deterrent effect . . . .” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.</blockquote>
<p id="b510-6">Accord, <em>United States </em>v. <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier"><em>Peltier, supra, </em>at 538-539</a></span>; <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#28" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 28-29</a></span> (1968); <em>Linkletter </em>v. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker"><em>Walker, supra, </em>at 636-637</a></span>; <em>Tehan </em>v. <em>United States ex rel. Shott, </em><span class="citation" data-id="6751647"><a href="/opinion/6862154/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States ex rel. Shott">382 U. S. 406, 416</a></span> (1966).</p>
<p id="b510-7"><em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>involved the enforcement of the exclusionary rule at state trials and on direct review. The decision in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>, </em>as noted above, is premised on the view that implementation of the Fourth Amendment also requires the consideration of search-and-seizure claims upon collateral review of state convictions. But despite the broad deterrent purpose of the exclusionary rule, it has never been interpreted to proscribe the introduction of illegally seized evidence in all proceedings or against all persons. As in the case of any remedial device, “the application of the rule has been restricted to those areas where its reme<page-number citation-index="1" label="487">*487</page-number>dial objectives are thought most efficaciously served.” <em>United States </em>v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>.<footnotemark>24</footnotemark> Thus, our refusal to extend the exclusionary rule to grand jury proceedings was based on a balancing of the potential injury to the historic role and function of the grand jury by such extension against the potential contribution to the effectuation of the Fourth Amendment through deterrence of police misconduct:</p>
<blockquote id="b511-5">“Any incremental deterrent effect which might be achieved by extending the rule to grand jury proceedings is uncertain at best. Whatever deterrence of police misconduct may result from the exclusion of illegally seized evidence from criminal trials, it is unrealistic to assume that application of the rule to grand jury proceedings would significantly further that goal. Such an extension would deter only police investigation consciously directed toward the discovery of evidence solely for use in a grand jury investigation. . . . We therefore decline to embrace a view that would achieve a speculative and undoubtedly minimal advance in the deterrence of police misconduct at the expense of substantially <page-number citation-index="1" label="488">*488</page-number>impeding the role of the grand jury.” <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#351" aria-description="Citation for case: United States v. Calandra">414 U. S., at 351-352</a></span> (footnote omitted).</blockquote>
<p id="b512-5">The same pragmatic analysis of the exclusionary rule’s usefulness in a particular context was evident earlier in <em>Walder </em>v. <em>United </em>States, <em>supra, </em>where the Court permitted the Government to use unlawfully seized evidence to impeach the credibility of a defendant who had testified broadly in his own defense. The Court held, in effect, that the interests safeguarded by the exclusionary rule in that context were outweighed by the need to prevent perjury and to assure the integrity of the trial process. The judgment in <em><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span> </em>revealed most clearly that the policies behind the exclusionary rule are not absolute. Rather, they must be evaluated in light of competing policies. In that case, the public interest in determination of truth at trial<footnotemark>25</footnotemark> was deemed to outweigh the incremental contribution that might have been made to the protection of Fourth Amendment values by application of the rule.</p>
<p id="b512-6">The balancing process at work in these cases also finds expression in the standing requirement. Standing to invoke the exclusionary rule has been found to exist only when the Government attempts to use illegally obtained evidence to incriminate the victim of the illegal search. <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span> (1973); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 491-492</a></span> (1963). See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960). The standing requirement is premised on the view that the “additional benefits of extending the . . . rule” to defendants other than the victim of the search or seizure are outweighed by the “further encroachment upon the <page-number citation-index="1" label="489">*489</page-number>public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth." <em>Alderman </em>v. <em>United States, supra, </em>at 174-175.<footnotemark>26</footnotemark></p>
<p id="b513-5">IV</p>
<p id="b513-6">We turn now to the specific question presented by these cases. Respondents allege violations of Fourth Amendment rights guaranteed them through the Fourteenth Amendment. The question is whether state prisoners— who have been afforded the opportunity for full and fair consideration of their reliance upon the exclusionary rule with respect to seized evidence by the state courts at trial and on direct review — may invoke their claim again on federal habeas corpus review. The answer is to be found by weighing the utility of the exclusionary rule against the costs of extending it to collateral review of Fourth Amendment claims.</p>
<p id="b513-7">The costs of applying the exclusionary rule even at trial and on direct review are well known: <footnotemark>27</footnotemark> the focus <page-number citation-index="1" label="490">*490</page-number>of the trial, and the attention of the participants therein, are diverted from the ultimate question of guilt or innocence that should be the central concern in a criminal proceeding.<footnotemark>28</footnotemark> Moreover, the physical evidence sought to be excluded is typically reliable and often the most probative information bearing on the guilt or innocence of the defendant. As Mr. Justice Black emphasized in his dissent in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>:</em></p>
<blockquote id="b514-5"><em>“A </em>claim of illegal search and seizure under the Fourth Amendment is crucially different from many other constitutional rights; ordinarily the evidence seized can in no way have been rendered untrustworthy by the means of its seizure and indeed often this evidence alone establishes beyond virtually any shadow of a doubt that the defendant is guilty.” 394 U. S., at 237.</blockquote>
<p id="b514-6">Application of the rule thus deflects the truthfinding process and often frees the guilty. The disparity in particular cases between the error committed by the police officer and the windfall afforded a guilty defendant by application of the rule is contrary to the idea of proportionality that is essential to the concept of justice.<footnotemark>29</footnotemark> Thus, <page-number citation-index="1" label="491">*491</page-number>although the rule is thought to deter unlawful police activity in part through the nurturing of respect for Fourth Amendment values, if applied indiscriminately it may well have the opposite effect of generating disrespect for the law and administration of justice.<footnotemark>30</footnotemark> These long-recognized costs of the rule persist when a criminal conviction is sought to be overturned on collateral review on the ground that a search-and-seizure claim was erroneously rejected by two or more tiers of state courts.<footnotemark>31</footnotemark></p>
<p id="b516-4"><page-number citation-index="1" label="492">*492</page-number>Evidence obtained by police officers in violation of the Fourth Amendment is excluded at trial in the hope that the frequency of future violations will decrease. Despite the absence of supportive empirical evidence,<footnotemark>32</footnotemark> we have assumed that the immediate effect of exclusion will be to discourage law enforcement officials from violating the Fourth Amendment by removing the incentive to disregard it. More importantly, over the long term, this demonstration that our society attaches serious consequences to violation of constitutional rights is thought to encourage those who formulate law enforcement policies, and the officers who implement them, to incorporate Fourth Amendment ideals into their value system.<footnotemark>33</footnotemark></p>
<p id="b517-4"><page-number citation-index="1" label="493">*493</page-number>We adhere to the view that these considerations support the implementation of the exclusionary rule at trial and its enforcement on direct appeal of state-court convictions. But the additional contribution, if any, of the consideration of search-and-seizure claims of state prisoners on collateral review is small in relation to the costs. To be sure, each case in which such claim is considered may add marginally to an awareness of the values protected by the Fourth Amendment. There is no reason to believe, however, that the overall educative effect of the exclusionary rule would be appreciably diminished if search-and-seizure claims could not be raised in federal habeas corpus review of state convictions.<footnotemark>34</footnotemark> Nor is there reason to assume that any specific disincentive already created by the risk of exclusion of evidence at trial or the reversal of convictions on direct review would be enhanced if there were the further risk that a conviction obtained in state court and affirmed on direct review might be overturned in collateral proceedings often occurring years after the incarceration of the defendant. The view that the deterrence of Fourth Amendment violations would be furthered rests on the dubious assumption that law enforcement authorities would fear that federal habeas review might reveal flaws in a search or seizure that went undetected at trial and on appeal.<footnotemark>35</footnotemark> Even if one rationally could assume that <page-number citation-index="1" label="494">*494</page-number>some additional incremental deterrent effect would be present in isolated cases, the resulting advance of the legitimate goal of furthering Fourth Amendment rights would be outweighed by the acknowledged costs to other values vital to a rational system of criminal justice.</p>
<p id="b518-5">In sum, we conclude that where the State has provided an opportunity for full and fair litigation of a Fourth Amendment claim,<footnotemark>36</footnotemark> a state prisoner may not be granted federal habeas corpus relief on the ground that evidence obtained in an unconstitutional search or seizure was introduced at his trial.<footnotemark>37</footnotemark> In this context the <page-number citation-index="1" label="495">*495</page-number>contribution of the exclusionary rule, if any, to the effec-tuation of the Fourth Amendment is minimal and the substantial societal costs of application of the rule persist with special force.<footnotemark>38</footnotemark></p>
<p id="b520-3"><page-number citation-index="1" label="496">*496</page-number>Accordingly, the judgments of the Courts of Appeals are</p>
<p id="b520-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b493-9"> The ordinance provides:</p>
<blockquote id="b493-10">“Every person is a vagrant wbo:</blockquote>
<blockquote id="b493-11">“[1] Loiters or wanders upon the streets or from place to place without apparent reason or business and [2] who refuses to identify himself and to account for his presence when asked by a police officer to do so [3] if surrounding circumstances are such as to indicate to a reasonable man that the public safety demands such identification.”</blockquote>
</footnote>
<footnote label="2">
<p id="b495-8"> In support of the vagueness holding the court relied principally on <em>Papachristou </em>v. <em>Jacksonville, </em><span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/" aria-description="Citation for case: Papachristou v. City of Jacksonville">405 U. S. 156</a></span> (1972), where we invalidated a city ordinance in part defining vagrants as "persons wandering or strolling around from place to place without any lawful purpose or object . . . <span class="citation" data-id="108472"><a href="/opinion/108472/papachristou-v-city-of-jacksonville/#156" aria-description="Citation for case: Papachristou v. City of Jacksonville"><em>Id., </em>at 156-157, n. 1</a></span>. Noting the similarity between the first element of the Henderson ordinance, see n. 1, <em>supra, </em>and the Jacksonville ordinance, it concluded that the second and third elements of the Henderson ordinance were not sufficiently specific to cure its overall vagueness. <span class="citation" data-id="323709"><a href="/opinion/323709/lloyd-charles-powell-v-w-t-stone-warden/#95" aria-description="Citation for case: Lloyd Charles Powell v. W. T. Stone, Warden">507 F. 2d, at 95-97</a></span>. Petitioner Stone challenges these conclusions, but in view of our disposition of the case we need not consider this issue.</p>
</footnote>
<footnote label="3">
<p id="b497-5"> The sole evidence presented to the magistrate was the affidavit in support of the warrant application. It indicated that the police believed explosives and illegal weapons were present in Rice’s home because (1) Rice was an official of the NCCF, (2) a violent killing of an officer had occurred and it appeared that the NCCF was involved, and (3) police had received information in the past that Rice possessed weapons and explosives, which he had said should be used against the police. See <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/" aria-description="Citation for case: Rice v. Wolff">388 F. Supp., at 189</a></span> n. 1. In concluding that there existed probable cause for issuance of the warrant, although the Nebraska Supreme Court found the affidavit alone sufficient, it also referred to information contained in testimony adduced at the suppression hearing but not included in the affidavit. <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#738" aria-description="Citation for case: State v. Rice">188 Neb. 728, 738-739</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#487" aria-description="Citation for case: State v. Rice">199 N. W. 2d 480, 487-488</a></span>. See also <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#754" aria-description="Citation for case: State v. Rice"><em>id., </em>at 754</a></span>, <span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/#495" aria-description="Citation for case: State v. Rice">199 N. W. 2d, at 495</a></span> (concurring opinion). The District Court limited its probable-cause inquiry to the face of the affidavit, see <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S., at 413</a></span> n. 3; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 109</a></span> n. 1, and concluded probable cause was lacking. Petitioner Wolff contends that police should be permitted to supplement the information contained in an affidavit for a search warrant at the hearing on a motion to suppress, a contention that we have several times rejected, see, <em>e. g., Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span>, 565 n. 8 (1971); <em>Aguilar </em>v. <em>Texas, supra, </em>at 109 n. 1, and need not reach again here.</p>
</footnote>
<footnote label="4">
<p id="b498-8"> The District Court further held that the evidence of dynamite particles found on Rice’s clothing should have been suppressed as the tainted fruit of an arrest warrant that would not have been issued but for the unlawful search of his home. <span class="citation" data-id="2313059"><a href="/opinion/2313059/rice-v-wolff/#202" aria-description="Citation for case: Rice v. Wolff">388 F. Supp., at 202-207</a></span>. See <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).</p>
</footnote>
<footnote label="5">
<p id="b498-9"> In the orders granting certiorari in these cases we requested that counsel in <em>Stone </em>v. <em>Powell </em>and <em>Wolff </em>v. <em><span class="citation" data-id="9591942"><a href="/opinion/1346717/state-v-rice/" aria-description="Citation for case: State v. Rice">Rice</a></span> </em>respectively address the questions:</p>
<blockquote id="b498-10">“Whether, in light of the fact that the District Court found that the Henderson, Nev., police officer had probable cause to arrest respondent for violation of an ordinance which at the time of the arrest had not been authoritatively determined to be unconstitutional, respondent’s claim that the gun discovered as a result of a search incident to that arrest violated his rights under the Fourth and Fourteenth Amendments to the United States Constitution is one cognizable under <span class="citation no-link">28 U. S. C. §2254</span>.</blockquote>
<blockquote id="b498-11">“Whether the constitutional validity of the entry and search of respondent’s premises by Omaha police officers under the circumstances of this case is a question properly cognizable under <span class="citation no-link">28 U. S. C. § 2254</span>.”</blockquote>
</footnote>
<footnote label="6">
<p id="b498-12"> It is now well established that the phrase “habeas corpus” used alone refers to the common-law writ of habeas corpus <em>ad subjicien-</em><page-number citation-index="1" label="475">*475</page-number><em>dum, </em>known as the “Great Writ.” <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#95" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 95</a></span> (1807) (Marshall, C. J.).</p>
</footnote>
<footnote label="7">
<p id="b499-8"> Prior to 1889 there was, in practical effect, no appellate review in federal criminal cases. The possibility of Supreme Court review on certificate of division of opinion in the circuit court was remote because of the practice of single district judges’ holding circuit court. See P. Bator, P. Mishkin, E&gt;. Shapiro, &amp; H. Wechsler, Hart &amp; Wech-sler’s The Federal Courts and the Federal System 1539-1540 (2d ed. 1973); F. Frankfurter &amp; J. Landis, The Business of the Supreme Court 31-32, 79-80, and n. 107 (1927). Pressure naturally developed for expansion of the scope of habeas corpus to reach otherwise <page-number citation-index="1" label="476">*476</page-number>unreviewable decisions involving fundamental rights. See <em>Ex parte Siebold, </em><span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/#376" aria-description="Citation for case: Ex Parte Siebold">100 U. S. 371, 376-377</a></span> (1880); Bator, Finality in Criminal Law and Federal Habeas Corpus For State Prisoners, <span class="citation no-link">76 Harv. L. Rev. 441</span>, 473, and n. 75 (1963).</p>
</footnote>
<footnote label="8">
<p id="b500-10"> The expansion occurred primarily with regard to (i) convictions based on assertedly unconstitutional statutes, <em>e. g., Ex parte <span class="citation" data-id="90042"><a href="/opinion/90042/ex-parte-siebold/" aria-description="Citation for case: Ex Parte Siebold">Siebold, supra,</a></span> </em>or (ii) detentions based upon an allegedly illegal sentence, <em>e. g., Ex parte Lange, </em><span class="citation" data-id="9416939"><a href="/opinion/88804/ex-parte-lange/" aria-description="Citation for case: Ex Parte Lange">18 Wall. 163</a></span> (1874). See Bator, <em>supra, </em>n. 7, at 465-474.</p>
</footnote>
<footnote label="9">
<p id="b500-11"> There has been disagreement among scholars as to whether the result in <em>Brown </em>v. <em><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span> </em>was foreshadowed by the Court’s decision in <em>Moore </em>v. <em>Dempsey, </em><span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span> (1923). Compare Hart, Foreword: The Time Chart of the Justices, <span class="citation no-link">73 Harv. L. Rev. 84</span>, 105 (1959); Reitz, Federal Habeas Corpus; Impact of an Abortive State Proceeding, <span class="citation no-link">74 Harv. L. Rev. 1315</span>, 1328-1329 (1961), with Bator, <em>supra, </em>n. 7, at 488-491. See also <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#421" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 421</a></span>, and n. 30 (1963); <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#457" aria-description="Citation for case: Fay v. Noia"><em>id., </em>at 457-460</a></span> (Harlan, J., dissenting).</p>
</footnote>
<footnote label="10">
<p id="b501-6"> Despite the expansion of the scope of the writ, there has been no change in the established rule with respect to nonconstitutional claims. The writ of habeas corpus and its federal counterpart, <span class="citation no-link">28 U. S. C. § 2255</span>, “will not be allowed to do service for an appeal.” <em>Sunal </em>v. <em>Large, </em><span class="citation" data-id="8163802"><a href="/opinion/8201865/sunal-v-large/#178" aria-description="Citation for case: Sunal v. Large">332 U. S. 174, 178</a></span> (1947). For this reason, non-constitutional claims that could have been raised on appeal, but were not, may not be asserted in collateral proceedings. <span class="citation" data-id="8163802"><a href="/opinion/8201865/sunal-v-large/#178" aria-description="Citation for case: Sunal v. Large"><em>Id., </em>at 178-179</a></span>; <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9425745"><a href="/opinion/109059/davis-v-united-states/#345" aria-description="Citation for case: Davis v. United States">417 U. S. 333, 345-346</a></span>, and n. 15 (1974). Even those nonconstitutional claims that could not have been asserted on direct appeal can be raised on collateral review only if the alleged error constituted “ 'a fundamental defect which inherently results in a complete miscarriage of justice,’ ” <span class="citation" data-id="9425745"><a href="/opinion/109059/davis-v-united-states/#346" aria-description="Citation for case: Davis v. United States"><em>id., </em>at 346</a></span>, quoting <em>Hill </em>v. <em>United States, </em><span class="citation" data-id="9422329"><a href="/opinion/106329/hill-v-united-states/#428" aria-description="Citation for case: Hill v. United States">368 U. S. 424, 428</a></span> (1962).</p>
</footnote>
<footnote label="11">
<p id="b502-5"> In construing broadly the power of a federal district court to consider constitutional claims presented in a petition for writ of habeas corpus, the Court in <em>Fay </em>also reaffirmed the equitable nature of the writ, noting that “[discretion is implicit in the statutory command that the judge . . . 'dispose of the matter as law and justice require.’ <span class="citation no-link">28 U. S. C. §2243</span>.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#438" aria-description="Citation for case: Fay v. Noia">372 U. S., at 438</a></span>. More recently, in <em>Francis </em>v. <em>Henderson, </em><span class="citation" data-id="9426387"><a href="/opinion/109439/francis-v-henderson/" aria-description="Citation for case: Francis v. Henderson">425 U. S. 536</a></span> (1976), holding that a state prisoner who failed to malee a timely challenge to the composition of the grand jury that indicted him cannot bring such a challenge in a post-conviction federal habeas corpus proceeding absent a claim of actual prejudice, we emphasized:</p>
<blockquote id="b502-6">“This Court has long recognized that in some circumstances considerations of comity and concerns for the orderly administration of criminal justice require a federal court to forgo the exercise of its habeas corpus power. See <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#425" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 425-426</a></span>.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#539" aria-description="Citation for case: Fay v. Noia"><em>Id., </em>at 539</a></span>.</blockquote>
</footnote>
<footnote label="12">
<p id="b503-6"> Compare, <em>e. g., United States </em>v. <em>Re, </em><span class="citation" data-id="9452511"><a href="/opinion/274722/united-states-v-gerardo-a-re-also-known-as-jerry-a-re-and-gerard-f-re/" aria-description="Citation for case: United States v. Gerardo A. Re, Also Known as Jerry A. Re...">372 F. 2d 641</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./388/912/">388 U. S. 912</a></span> (1967); <em>United States </em>v. <em>Jenkins, </em><span class="citation" data-id="251645"><a href="/opinion/251645/united-states-v-ernest-jenkins/" aria-description="Citation for case: United States v. Ernest Jenkins">281 F. 2d 193</a></span> (CA3 1960); <em>Eisner </em>v. <em>United States, </em><span class="citation" data-id="269188"><a href="/opinion/269188/samson-eisner-v-united-states/" aria-description="Citation for case: Samson Eisner v. United States">351 F. 2d 55</a></span> (CA6 1965); <em>De Welles </em>v. <em>United States, </em><span class="citation" data-id="274584"><a href="/opinion/274584/roy-w-de-welles-v-united-states/" aria-description="Citation for case: Roy W. De Welles v. United States">372 F. 2d 67</a></span> (CA7), cert denied, <span class="citation multiple-matches"><a href="/c/U.%20S./388/919/">388 U. S. 919</a></span> (1967); <em>Williams </em>v. <em>United States, </em><span class="citation" data-id="258120"><a href="/opinion/258120/joseph-kenneth-williams-v-united-states/" aria-description="Citation for case: Joseph Kenneth Williams v. United States">307 F. 2d 366</a></span> (CA9 1962); <em>Armstead </em>v. <em>United States, </em><span class="citation" data-id="260927"><a href="/opinion/260927/george-armstead-v-united-states/" aria-description="Citation for case: George Armstead v. United States">318 F. 2d 725</a></span> (CA5 1963), with, <em>e. g., United States </em>v. <em>Sutton, </em><span class="citation" data-id="261495"><a href="/opinion/261495/united-states-v-paul-sutton/" aria-description="Citation for case: United States v. Paul Sutton">321 F. 2d 221</a></span> (CA4 1963); <em>Gaitan </em>v. <em>United States, 317 </em>F. 2d 494 (CA10 1963). See also <em>Thornton </em>v. <em>United States, </em>125 U. S. App. D. C. 114, <span class="citation" data-id="9452299"><a href="/opinion/273740/charles-j-thornton-v-united-states/" aria-description="Citation for case: Charles J. Thornton v. United States">368 F. 2d 822</a></span> (1966) (search-and-seizure claims not cognizable under § 2255 absent special circumstances).</p>
</footnote>
<footnote label="13">
<p id="b504-6"> See, <em>e. g., </em>Friendly, Is Innocence Irrelevant? Collateral Attack on Criminal Judgments, 38 U. CM. L. Rev. 142 (1970).</p>
</footnote>
<footnote label="14">
<p id="b504-7"> In <em><span class="citation" data-id="9426003"><a href="/opinion/109196/lefkowitz-v-newsome/" aria-description="Citation for case: Lefkowitz v. Newsome">Newsome</a></span> </em>the Court focused on the issue whether a state defendant’s plea of guilty waives federal habeas corpus review where state law does not foreclose review of the plea on direct appeal, and did not consider the substantive scope of the writ. See 420 U. S., at 287 n. 4. Similarly, in <em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span> </em>and <em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span> </em>the question considered here was not presented in the petition for certiorari, and in neither case was relief granted on the basis of a search-and-seizure claim. In <em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span> </em>the plurality expressly noted that it was not addressing the issue of the substantive scope of the writ. See 417 U. S., at 596, and a. 12.</p>
</footnote>
<footnote label="15">
<p id="b505-5"> As Mr. Justice Black commented in dissent, 394 U. S., at 231, 239, the <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>majority made no effort to justify its result in light of the long-recognized deterrent purpose of the exclusionary rule. Instead, the Court relied on a series of prior cases as implicitly establishing the proposition that search-and-seizure claims are cognizable in federal habeas corpus proceedings. See <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Carafas </em>v. <em>LaValee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967). But only in <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span> </em>did this Court order habeas relief on the basis of a search-and-seizure claim, and in that case, as well as in <em>Warden, </em>the issue of the substantive scope of the writ was not presented to the Court in the petition for writ of certiorari. Moreover, of the other “numerous occasions” cited by Mr. Justice BreNNAN’s dissent, <em>post, </em>at 518-519, in which the Court has accepted jurisdiction over collateral attacks by state prisoners raising Fourth Amendment claims, in only one <em>case</em>—Whiteley v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971)—was relief granted on that basis. And in <em>Whiteley, </em>as in <em>Man-cusi, </em>the issue of the substantive scope of the writ was not presented in the petition for certiorari. As emphasized by Mr. Justice Black, only in the most exceptional cases will we consider issues not raised in the petition. 394 U. S., at 239, and n. 7.</p>
</footnote>
<footnote label="16">
<p id="b505-6"> The issue in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>was the scope of § 2255. Our decision today rejects the dictum in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>concerning the applicability of the exclusionary rule in federal habeas corpus review of state-court decisions pursuant to § 2254. To the extent the application of the exclusionary rule in <em><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span> </em>did not rely upon the supervisory role of this Court over the lower federal courts, cf. <em>Elkins </em>v. <page-number citation-index="1" label="482">*482</page-number><em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960), see <em>infra, </em>at 484, the rationale for its application in that context is also rejected.</p>
</footnote>
<footnote label="17">
<p id="b506-9"> We find it unnecessary to consider the other issues concerning the exclusionary rule, or the statutory scope of the habeas corpus statute, raised by the parties. These include, principally, whether in view of the purpose of the rule, it should be applied on a <em>per se </em>basis without regard to the nature of the constitutional claim or the circumstances of the police action.</p>
</footnote>
<footnote label="18">
<p id="b506-10"> See generally J. Landynski, Search and Seizure and the Supreme Court (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937).</p>
</footnote>
<footnote label="19">
<p id="b507-4"> The roots of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>decision lay in an early decision, <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), where the Court held that the compulsory production of a person’s private books and papers for introduction against him at trial violated the Fourth and Fifth Amendments. <em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>, </em>however, had been severely limited in <em>Adams </em>v. <em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">New York</a></span>, </em>where the Court, emphasizing that the “law held unconstitutional [in Boyd] virtually compelled the defendant to furnish testimony against himself,” <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/#598" aria-description="Citation for case: Adams v. New York">192 U. S., at 598</a></span>, adhered to the common-law rule that a trial court must not inquire, on Fourth Amendment grounds, into the method by which otherwise competent evidence was acquired. See, <em>e. g., Commonwealth </em>v. <em>Dana, </em><span class="citation" data-id="6407794"><a href="/opinion/6534076/commonwealth-v-dana/" aria-description="Citation for case: Commonwealth v. Dana">43 Mass. 329</a></span> (1841).</p>
</footnote>
<footnote label="20">
<p id="b508-7"> See <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12-13</a></span> (1968); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-392, 394</a></span> (1914); <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 470</a></span> (1928) (Holmes, J., dissenting); <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#484" aria-description="Citation for case: Olmstead v. United States"><em>id., </em>at 484</a></span> (Brandéis, J., dissenting).</p>
</footnote>
<footnote label="21">
<p id="b508-8"> See <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656</a></span> (prevention of introduction of evidence where introduction is “tantamount” to a coerced confession); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#658" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 658</a></span> (deterrence of Fourth Amendment violations); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#659" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 659</a></span> (preservation of judicial integrity).</p>
<p id="b508-9">Only four Justices adopted the view that the Fourth Amendment itself requires the exclusion of unconstitutionally seized evidence in state criminal trials. See <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 656</a></span>; <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#666" aria-description="Citation for case: Mapp v. Ohio"><em>id., </em>at 666</a></span> (Douglas, J., concurring). Mr. Justice Black adhered to his view that the Fourth Amendment, standing alone, was not sufficient, see <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#39" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 39</a></span> (1949) (concurring opinion), but concluded that, when the Fourth Amendment is considered in conjunction with the Fifth Amendment ban against compelled self-incrimination, a constitutional basis emerges for requiring exclusion. <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 661</a></span> (concurring opinion). See n. 19, <em>supra.</em></p>
</footnote>
<footnote label="22">
<p id="b509-5"> See Monaghan, Foreword: Constitutional Common Law, <span class="citation no-link">89 Harv. L. Rev. 1</span>,- 5 — 6, and n. 33 (1975).</p>
</footnote>
<footnote label="23">
<p id="b509-6"> As we recognized last Term, judicial integrity is “not offended if law enforcement officials reasonably believed in good faith that their conduct was in accordance with the law even if decisions subsequent to the search and seizure have held that conduct of the type engaged in by the law enforcement officials is not permitted by the <page-number citation-index="1" label="486">*486</page-number>Constitution.” <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 538</a></span> (1975) (emphasis omitted).</p>
</footnote>
<footnote label="24">
<p id="b511-6"> As Professor Amsterdam has observed:</p>
<blockquote id="b511-7">“The rule is unsupportable as reparation or compensatory dispensation to the injured criminal; its sole rational justification is the experience of its indispensability in fexert[ing] general legal pressures to secure obedience to the Fourth Amendment on the part of . . . law-enforcing officers.’ As it serves this function, the rule is a needed, but grud[g]ingly taken, medicament; no more should be swallowed than is needed to combat the disease. Granted that so many criminals must go free as will deter the constables from blundering, pursuance of this policy of liberation beyond the confines of necessity inflicts gratuitous harm on the public interest . . . .” Search, Seizure, and Section 2255: A Comment, <span class="citation no-link">112 U. Pa. L. Rev. 378</span>, 388-389 (1964) (footnotes omitted).</blockquote>
</footnote>
<footnote label="25">
<p id="b512-7"> See generally M. Frankel, The Search For Truth — An Umpireal View, 31st Annual Benjamin N. Cardozo Lecture, Association of the Bar of the City of New York, Dec. 16, 1974.</p>
</footnote>
<footnote label="26">
<p id="b513-8"> Cases addressing the question, whether search-and-seizure holdings should be applied retroactively also have focused on the deterrent purpose served by the exclusionary rule, consistently with the balancing analysis applied generally in the exclusionary rule context. See <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#249" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 249-251, 253-254</a></span>, and n. 21 (1969); <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 636-637</a></span> (1965). Cf. <em>Fuller </em>v. <em>Alaska, </em><span class="citation" data-id="9423835"><a href="/opinion/107788/fuller-v-alaska/#81" aria-description="Citation for case: Fuller v. Alaska">393 U. S. 80, 81</a></span> (1968). The “attenuation-of-t-he-taint” doctrine also is consistent with the balancing approach. See <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491-492</a></span>; Amsterdam, <em>supra, </em>n. 24, at 389-390.</p>
</footnote>
<footnote label="27">
<p id="b513-9"> See, <em>e. g., Irvine </em>v. <em>California, </em><span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#136" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 136</a></span> (1954); <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (Burger, C. J., dissenting); <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (1926) (Cardozo, J.); 8 J. Wigmore, Evidence § 2184a, pp. 51-52 (McNaughton ed. 1961); Amsterdam, <em>supra, </em>n. 24, at 388-391; Friendly, <em>supra, </em>n. 13, at 161; Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span>, 736-754 (1970), and <page-number citation-index="1" label="490">*490</page-number>sources cited therein; Paulsen, The Exclusionary Rule and Misconduct by the Police, 52 J. Crim. L. C. &amp; P. S. 255, 256 (1961); Wright, Must the Criminal Go Free If the Constable Blunders?, <span class="citation no-link">50 Tex. L. Rev. 736</span> (1972).</p>
</footnote>
<footnote label="28">
<p id="b514-8"> See address by Justice Schaefer of the Supreme Court of Illinois, Is the Adversary System Working in Optimal Fashion?, delivered at the National Conference on the Causes of Popular Dissatisfaction With the Administration of Justice, pp. 8-9, Apr. 8, 1976; cf. Frankel, <em>supra, </em>n. 25.</p>
</footnote>
<footnote label="29">
<p id="b514-9"> Many of the proposals for modification of the scope of the exclusionary rule recognize at least implicitly the role of proportionality in the criminal justice system and the potential value of establishing a direct relationship between the nature of the violation and the decision whether to invoke the rule. See ALI, A <page-number citation-index="1" label="491">*491</page-number>Model Code of Pre-arraignment Procedure, § 290.2, pp. 181-183 (1975) (“substantial violations”); H. Friendly, Benchmarks 260-262 (1967) (even at trial, exclusion should be limited to “the fruit of activity intentionally or flagrantly illegal”); 8 Wigmore, <em>supra, </em>n. 27, at 52-53. See n. 17, <em>supra.</em></p>
</footnote>
<footnote label="30">
<p id="b515-6"> In a different context, Dallin H. Oaks has observed:</p>
<blockquote id="b515-7">“I am criticizing, not our concern with procedures, but our preoccupation, in which we may lose sight of the fact that our procedures are not the ultimate goals of our legal system. Our goals are truth and justice, and procedures are but means to these ends. . . .</blockquote>
<blockquote id="b515-8">“Truth and justice are ultimate values, so understood by our people, and the law and the legal profession will not be worthy of public respect and loyalty if we allow our attention to be diverted from these goals.” Ethics, Morality and Professional Responsibility, 1975 B. Y. U. L. Rev. 591, 596.</blockquote>
</footnote>
<footnote label="31">
<p id="b515-9"> Resort to habeas corpus, especially for purposes other than to assure that no innocent person suffers an unconstitutional loss of liberty, results in serious intrusions on values important to our system of government. They include “(i) the most effective utilization of limited judicial resources, (ii) the necessity of finality in criminal trials, (iii) the minimization of friction between our federal and state systems of justice, and (iv) the maintenance of the constitutional balance upon which the doctrine of federalism is founded.” <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#259" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 259</a></span> (Powell, J., concurring). See also <em>Kaufman </em>v. <em>United States, </em>394 U. S., at 231 (Black, J., dissenting); Friendly, <em>supra, </em>n. 13.</p>
<p id="b515-10">We nevertheless afford broad habeas corpus relief, recognizing the need in a free society for an additional safeguard against <page-number citation-index="1" label="492">*492</page-number>compelling an innocent man to suffer an unconstitutional loss of liberty. The Court in <em>Fay </em>v. <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span> </em>described habeas corpus as a remedy for “whatever society deems to be intolerable restraints,” and recognized that those to whom the writ should be granted “are persons whom society has grievously wronged.” <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#401" aria-description="Citation for case: Fay v. Noia">372 U. S., at 401, 441</a></span>. But in the case of a typical Fourth Amendment claim, asserted on collateral attack, a convicted defendant is usually asking society to redetermine an issue that has no bearing on the basic justice of his incarceration.</p>
</footnote>
<footnote label="32">
<p id="b516-6"> The efficacy of the exclusionary rule has long been the subject of sharp debate. Until recently, scholarly empirical research was unavailable. <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S., at 218</a></span>, And, the evidence derived from recent empirical research is still inconclusive. Compare, <em>e. g., </em>Oaks, <em>supra, </em>n. 27; Spiotto, Search and Seizure: An Empirical Study of the Exclusionary Rule and Its Alternatives, 2 J. Legal Studies 243 (1973), with, <em>e. g., </em>Canon, Is the Exclusionary Rule in Failing Health?, Some New Data an,d a Plea Against a Precipitous Conclusion, 62 Ky. L. J. 681 (1974). See <em>United States </em>v. <em>Janis, ante, </em>at 450-452, n. 22; Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 475 n. 593 (1974); Comment, On the Limitations of Empirical Evaluations of the Exclusionary Rule: A Critique of the Spiotto Research and United States v. Calandra, <span class="citation no-link">69 Nw. U. L. Rev. 740</span> (1974).</p>
</footnote>
<footnote label="33">
<p id="b516-7"> See Oaks, <em>supra, </em>n. 27, at 756.</p>
</footnote>
<footnote label="34">
<p id="b517-5"> “As the exclusionary rule is applied time after time, it seems that its deterrent efficacy at some stage reaches a point of diminishing returns, and beyond that point its continued application is a public nuisance.” Amsterdam, <em>supra, </em>n. 24, at 389.</p>
</footnote>
<footnote label="35">
<p id="b517-6"> The policy arguments that respondents marshal in support of the view that federal habeas corpus review is necessary to effectuate the Fourth Amendment stem from a basic mistrust of the state courts as fair and competent forums for the adjudication of federal constitutional rights. The argument is that state courts cannot be trusted to effectuate Fourth Amendment values through <page-number citation-index="1" label="494">*494</page-number>fair application of the rule, and the oversight jurisdiction of this Court on certiorari is an inadequate safeguard. The principal rationale for this view emphasizes the broad differences in the respective institutional settings within which federal judges and state judges operate. Despite differences in institutional environment and the unsympathetic attitude to federal constitutional claims of some state judges in years past, we are unwilling to assume that there now exists a general lack of appropriate sensitivity to constitutional rights in the trial and appellate courts of the several States. State courts, like federal courts, have a constitutional obligation to safeguard personal liberties and to uphold federal law. <em>Martin </em>v. <em>Hunter’s Lessee, </em><span class="citation" data-id="85160"><a href="/opinion/85160/martin-v-hunters-lessee/#341" aria-description="Citation for case: Martin v. Hunter&#x27;s Lessee">1 Wheat. 304, 341-344</a></span> (1816). Moreover, the argument that federal judges are more expert in applying federal constitutional law is especially unpersuasive in the context of search-and-seizure claims, since they are dealt with on a daily basis by trial level judges in both systems. In sum, there is “no intrinsic reason why the fact that a man is a federal judge should make him more competent, or conscientious, or learned with respect to the [consideration of Fourth Amendment claims] than his neighbor in the state courthouse.” Bator, <em>supra, </em>n. 7, at 509.</p>
</footnote>
<footnote label="36">
<p id="b518-7"> Cf. <em>Townsend </em>v. <em>Sain, </em><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963).</p>
</footnote>
<footnote label="37">
<p id="b518-8"> Mr. Justice Brennan’s dissent characterizes the Court’s opinion as laying the groundwork for a “drastic withdrawal of federal habeas jurisdiction, if not for all grounds . . . , then at least [for many] <em>Post, </em>at 517. It refers variously to our opinion as a “novel reinterpretation of the habeas statutes,” <em>post, </em>at 515; as a “harbinger of future eviscerations of the habeas statutes,” <em>post, </em>at 516; as “rewriting] Congress’ jurisdictional statutes . . . and [bar<page-number citation-index="1" label="495">*495</page-number>ring] access to federal courts by state prisoners with constitutional claims distasteful to a majority” of the Court, <em>post, </em>at 522; and as a “denigration of constitutional guarantees [that] must appall citizens taught to expect judicial respect” of constitutional rights, <em>post, </em>at 523.</p>
<p id="b519-6">With all respect, the hyperbole of the dissenting opinion is misdirected. Our decision today is <em>not </em>concerned with the scope of the habeas corpus statute as authority for litigating constitutional claims generally. We do reaffirm that the exclusionary rule is a judicially created remedy rather than a personal constitutional right, see <em>supra, </em>at 486, and we emphasize the minimal utility of the rule when sought to be applied to Fourth Amendment claims in a habeas corpus proceeding. As Mr. Justice Black recognized in this context, “ordinarily the evidence seized can in no way have been rendered untrustworthy . . . and indeed often . . . alone establishes beyond virtually any shadow of a doubt that the defendant is guilty.” <em>Kaufman </em>v. <em>United States, </em>394 U. S., at 237 (dissenting opinion). In sum, we hold only that a federal court need not apply the exclusionary rule on habeas review of a Fourth Amendment claim absent a showing that the state prisoner was denied an opportunity for a full and fair litigation of that claim at trial and on direct review. Our decision does not mean that the federal court lacks jurisdiction over such a claim, but only that the application of the rule is limited to cases in which there has been both such a showing and a Fourth Amendment violation.</p>
</footnote>
<footnote label="38">
<p id="b519-7"> See n. 31, <em>supra. </em>Respondents contend that since they filed petitions for federal habeas corpus rather than seeking direct review by this Court through an application for a writ of certiorari, and since the time to apply for certiorari has now passed, any diminution in their ability to obtain habeas corpus relief on the ground evidence obtained in an unconstitutional search or seizure was introduced at their trials should be prospective. Cf. <em>England </em>v. <em>Louisiana State Board of Medical Examiners, </em><span class="citation" data-id="9422712"><a href="/opinion/106729/england-v-louisiana-state-board-of-medical-examiners/#422" aria-description="Citation for case: England v. Louisiana State Board of Medical Examiners">375 U. S. 411, 422-423</a></span> (1964). We reject these contentions. Although not required to do so under the Court’s prior decisions, see <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span> (1963), respondents were, of course, free to file a timely petition for certiorari prior to seeking federal habeas corpus relief.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Stovall v. Denno.md  (`case`, 5 assertions)

### content_page

```
---
title: "Stovall v. Denno"
type: case
citation: "388 U.S. 293 (1967)"
parallel_cite: "87 S. Ct. 1967; 18 L. Ed. 2d 1199"
neutral_cite: 1967 U.S. LEXIS 1087
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-12
docket: 254
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Stovall v. Denno
  varies_by_point: false
  scope_note: "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107488/stovall-v-denno/"
  cluster_id: 107488
  opinion_id: 107488
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Gilbert v. California]]", "[[United States v. Wade]]", "[[Neil v. Biggers]]", "[[Manson v. Brathwaite]]"]
aliases: []
tags: ["case", "eyewitness-identification", "due-process", "suggestive-identification"]
holding: "A confrontation that is unnecessarily suggestive and conducive to irreparable mistaken identification can violate due process;…"
lake:
  record_id: Stovall v. Denno
  status: verified
  projected_at: 2026-07-06
---

# Stovall v. Denno

*388 U.S. 293 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Stovall was brought, handcuffed, to the hospital room of a stabbing victim (Mrs. Behrendt)—who was the only person who could identify her attacker and might not survive—where she identified him in a one-on-one showup. He challenged the identification as unnecessarily suggestive and as a denial of due process, independent of any right-to-counsel claim.

## Issue
Whether an unnecessarily suggestive identification procedure can violate due process, and how that claim is judged.

## Rule
Suggestive identification procedures are tested for due-process fairness under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The claim asks whether "the confrontation conducted in this case was so unnecessarily suggestive and conducive to irreparable mistaken identification that he was denied due process of law. This is a recognized ground of attack upon a conviction independent of any right to counsel claim." — 388 U.S. at 302. ^pin-302

And "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it." — *Id.* ^pin-302a

## Application
Although showing a suspect singly has been widely condemned, the totality here justified it: Mrs. Behrendt was the only person who could identify or exonerate Stovall, no one knew how long she would live, and she could not come to a station-house lineup. On those facts the immediate hospital showup was imperative and did not deny Stovall due process.

## Conclusion
On these facts the suggestive hospital showup did not violate due process; the judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The origin of the due-process attack on suggestive identifications; the reliability-focused "linchpin" test was later developed in [[Neil v. Biggers]] and [[Manson v. Brathwaite]]. *Stovall*'s separate holding that the [[United States v. Wade]] / [[Gilbert v. California]] counsel rules were non-retroactive has been superseded by later retroactivity doctrine, but its due-process identification holding remains good law.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Stovall v. Denno*, 388 U.S. 293 (1967) — https://www.courtlistener.com/opinion/107488/stovall-v-denno/ — pinpoint: 302.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1db0769e5c7156d5", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "388 U.S. 293 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 1087", "official_citation_present": true, "parallel_cite": "87 S. Ct. 1967; 18 L. Ed. 2d 1199", "title": "Stovall v. Denno", "year": "1967"}}
{"assertion_id": "770f9560ce7fc61e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confrontation that is unnecessarily suggestive and conducive to irreparable mistaken identification can violate due process;…", "title": "Stovall v. Denno"}}
{"assertion_id": "cb4ed9b69d90accc", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Anchor", "title": "Stovall v. Denno"}}
{"assertion_id": "151348f8d6d23433", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Stovall v. Denno"}}
{"assertion_id": "d07a04d02f875645", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-06-12", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Stovall v. Denno", "field_i_validity": "good_law", "scope_note": "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite.", "title": "Stovall v. Denno", "varies_by_point": "false"}}
```

### lake record — Stovall v. Denno

```json
{
  "schema_version": "s2.v1",
  "record_id": "Stovall v. Denno",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Stovall v. Denno",
    "case_name_short": "Stovall",
    "case_name_full": "Stovall v. Denno, Warden",
    "input_case_name": "Stovall v. Denno",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-12",
    "year": 1967,
    "docket": "254",
    "cluster_id": 107488,
    "lead_opinion_id": 107488,
    "sibling_ids": [
      107488,
      9423482,
      9423483
    ],
    "absolute_url": "/opinion/107488/stovall-v-denno/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "388 U.S. 293",
      "volume": "388",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1967",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1199",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1087",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1087",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "388 U.S. 293",
        "volume": "388",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1967",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1967",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 1199",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1087",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1087",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "388 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "388 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-302",
      "page": null,
      "quote": "--- # Stovall v. Denno *388 U.S. 293 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Stovall was brought, handcuffed, to the hospital room of a stabbing victim (Mrs. Behrendt)\u2014who was the only person who could identify her attacker and might not survive\u2014where she identified him in a one-on-one showup. He challenged the identification as unnecessarily suggestive and as a denial of due process, independent of any right-to-counsel claim. ## Issue Whether an unnecessarily suggestive identification procedure can violate due process, and how that claim is judged. ## Rule Suggestive identification procedures are tested for due-process fairness under the totality of the circumstances. The claim asks whether",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-302a",
      "page": null,
      "quote": "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it.",
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
    "composite_basis_ref": "Stovall v. Denno",
    "varies_by_point": false,
    "scope_note": "Due-process suggestiveness holding remains good law; reliability framework later developed in Neil v. Biggers / Manson v. Brathwaite.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Hopkins",
          "cluster_id": 4607692,
          "cite": [
            "920 F.3d 690"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Neil C. Albee v. State of Indiana",
          "cluster_id": 4371568,
          "cite": [
            "71 N.E.3d 856",
            "2017 WL 765903",
            "2017 Ind. App. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. David Ruiz-Hiracheta",
          "cluster_id": 2766491,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. David Ruiz-Hiracheta",
          "cluster_id": 2766490,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Andres Deleon-Gloria",
          "cluster_id": 2766489,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Andres Deleon-Gloria",
          "cluster_id": 2766488,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Escalante-Reyes",
          "cluster_id": 805234,
          "cite": [
            "689 F.3d 415",
            "2012 WL 3024195",
            "2012 U.S. App. LEXIS 15385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane1_negative"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Batson v. Kentucky",
          "cluster_id": 111662,
          "cite": [
            "90 L. Ed. 2d 69",
            "106 S. Ct. 1712",
            "476 U.S. 79",
            "1986 U.S. LEXIS 150",
            "54 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albright v. Oliver",
          "cluster_id": 112924,
          "cite": [
            "127 L. Ed. 2d 114",
            "114 S. Ct. 807",
            "510 U.S. 266",
            "1994 U.S. LEXIS 1319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Witherspoon v. Illinois",
          "cluster_id": 107715,
          "cite": [
            "20 L. Ed. 2d 776",
            "88 S. Ct. 1770",
            "391 U.S. 510",
            "1968 U.S. LEXIS 1469",
            "46 Ohio Op. 2d 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockhart v. Fretwell",
          "cluster_id": 112807,
          "cite": [
            "122 L. Ed. 2d 180",
            "113 S. Ct. 838",
            "506 U.S. 364",
            "1993 U.S. LEXIS 1016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. Kentucky",
          "cluster_id": 111785,
          "cite": [
            "93 L. Ed. 2d 649",
            "107 S. Ct. 708",
            "479 U.S. 314",
            "1987 U.S. LEXIS 283",
            "55 U.S.L.W. 4089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montgomery v. Louisiana",
          "cluster_id": 3171724,
          "cite": [
            "577 U.S. 190",
            "136 S. Ct. 718",
            "193 L. Ed. 2d 599",
            "25 Fla. L. Weekly Fed. S 611",
            "84 U.S.L.W. 4063",
            "2016 U.S. LEXIS 862"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Geesa v. State",
          "cluster_id": 1522092,
          "cite": [
            "820 S.W.2d 154",
            "1991 Tex. Crim. App. LEXIS 240",
            "1991 WL 226418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harper v. Virginia Department of Taxation",
          "cluster_id": 112890,
          "cite": [
            "125 L. Ed. 2d 74",
            "113 S. Ct. 2510",
            "509 U.S. 86",
            "1993 U.S. LEXIS 4212",
            "7 Fla. L. Weekly Fed. S 456",
            "16 Employee Benefits Cas. (BNA) 2313",
            "93 Daily Journal DAR 7730",
            "93 Cal. Daily Op. Serv. 4491",
            "61 U.S.L.W. 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
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
        "journal_ref": "Stovall v. Denno:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107488 OR 9423482 OR 9423483) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzExMTIwMDAwMDAwJnM9MzEwNjk3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107488+OR+9423482+OR+9423483%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107488 OR 9423482 OR 9423483)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02OTQmcz0xMjMxMjk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107488+OR+9423482+OR+9423483%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107488 OR 9423482 OR 9423483)",
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
    "complete_query": "cites:(107488 OR 9423482 OR 9423483)",
    "indexed_citing_opinions": 4105,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107488,
        "count": 3847,
        "count_source": "search"
      },
      {
        "opinion_id": 9423482,
        "count": 359,
        "count_source": "search"
      },
      {
        "opinion_id": 9423483,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6067,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/stovall-v-denno.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNzg3NDUmcz05NDE2OTMzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107488+OR+9423482+OR+9423483%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107488,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 270486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 271227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107488,
        "cited_id": 271407,
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
    "date_created": "2026-07-05T21:06:15Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:09:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Stovall v. Denno

```
<div>
<center><b><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U.S. 293</a></span> (1967)</b></center>
<center><h1>STOVALL<br>
v.<br>
DENNO, WARDEN.</h1></center>
<center>No. 254.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 16, 1967.</center>
<center>Decided June 12, 1967.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*294</span> <i>Leon B. Polsky</i> argued the cause and filed briefs for petitioner.</p>
<p><i>William Cahn</i> argued the cause and filed a brief for respondent.</p>
<p><i>H. Richard Uviller</i> argued the cause and filed a brief for the New York State District Attorneys' Association, as <i>amicus curiae,</i> urging affirmance.</p>
<p><i>Louis J. Lefkowitz,</i> Attorney General, <i>pro se, Samuel A. Hirshowitz,</i> First Assistant Attorney General, and <i>Barry Mahoney,</i> Assistant Attorney General, filed a brief for the Attorney General of New York, as <i>amicus curiae,</i> urging affirmance.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>This federal habeas corpus proceeding attacks collaterally a state criminal conviction for the same alleged constitutional errors in the admission of allegedly tainted identification evidence that were before us on direct review of the convictions involved in <i>United States</i> v. <i>Wade, ante,</i> p. 218, and <i>Gilbert</i> v. <i>California, ante,</i> p. 263. This case therefore provides a vehicle for deciding the extent to which the rules announced in <i>Wade</i> and <i>Gilbert</i> requiring the exclusion of identification evidence which is tainted by exhibiting the accused to identifying witnesses before trial in the absence of his counselare to be applied retroactively. See <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>; <i>Tehan</i> v. <i>Shott,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./382/406/">382 U. S. 406</a></span>; <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span>.<sup>[1]</sup> A further question is whether in any event, on the facts of the particular confrontation <span class="star-pagination">*295</span> involved in this case, petitioner was denied due process of law in violation of the Fourteenth Amendment. Cf. <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>.</p>
<p>Dr. Paul Behrendt was stabbed to death in the kitchen of his home in Garden City, Long Island, about midnight August 23, 1961. Dr. Behrendt's wife, also a physician, had followed her husband to the kitchen and jumped at the assailant. He knocked her to the floor and stabbed her 11 times. The police found a shirt on the kitchen floor and keys in a pocket which they traced to petitioner. They arrested him on the afternoon of August 24. An arraignment was promptly held but was postponed until petitioner could retain counsel.</p>
<p>Mrs. Behrendt was hospitalized for major surgery to save her life. The police, without affording petitioner time to retain counsel, arranged with her surgeon to permit them to bring petitioner to her hospital room about noon of August 25, the day after the surgery. Petitioner was handcuffed to one of five police officers who, with two members of the staff of the District Attorney, brought him to the hospital room. Petitioner was the only Negro in the room. Mrs. Behrendt identified him from her hospital bed after being asked by an officer whether he "was the man" and after petitioner repeated at the direction of an officer a "few words for voice identification." None of the witnesses could recall the words that were used. Mrs. Behrendt and the officers testified at the trial to her identification of the petitioner in the hospital room, and she also made an in-court identification of petitioner in the courtroom.</p>
<p>Petitioner was convicted and sentenced to death. The New York Court of Appeals affirmed without opinion. 13 N. Y. 2d 1094, <span class="citation" data-id="5521096"><a href="/opinion/5673625/people-v-stovall/" aria-description="Citation for case: People v. Stovall">196 N. E. 2d 65</a></span>. Petitioner <i>pro se</i> sought federal habeas corpus in the District Court for the Southern District of New York. He claimed that among other constitutional rights allegedly denied him <span class="star-pagination">*296</span> at his trial, the admission of Mrs. Behrendt's identification testimony violated his rights under the Fifth, Sixth, and Fourteenth Amendments because he had been compelled to submit to the hospital room confrontation without the help of counsel and under circumstances which unfairly focused the witness' attention on him as the man believed by the police to be the guilty person. The District Court dismissed the petition after hearing argument on an unrelated claim of an alleged invalid search and seizure. On appeal to the Court of Appeals for the Second Circuit a panel of that court initially reversed the dismissal after reaching the issue of the admissibility of Mrs. Behrendt's identification evidence and holding it inadmissible on the ground that the hospital room identification violated petitioner's constitutional right to the assistance of counsel. The Court of Appeals thereafter heard the case <i>en banc,</i> vacated the panel decision, and affirmed the District Court. <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1000/">384 U. S. 1000</a></span>, and set the case for argument with <i>Wade</i> and <i>Gilbert.</i> We hold that <i>Wade</i> and <i>Gilbert</i> affect only those cases and all future cases which involve confrontations for identification purposes conducted in the absence of counsel after this date. The rulings of <i>Wade</i> and <i>Gilbert</i> are therefore inapplicable in the present case. We think also that on the facts of this case petitioner was not deprived of due process of law in violation of the Fourteenth Amendment. The judgment of the Court of Appeals is, therefore, affirmed.</p>
<p></p>
<h2>I.</h2>
<p>Our recent discussions of the retroactivity of other constitutional rules of criminal procedure make unnecessary any detailed treatment of that question here. <i>Linkletter</i> v. <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Walker, supra</a></span></i><i>; </i><i>Tehan</i> v. <i>Shott, supra</i><i>; </i><i>Johnson</i> v. <i>New <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Jersey, supra</a></span></i><i>.</i> "These cases establish the principle that in criminal litigation concerning constitutional <span class="star-pagination">*297</span> claims, `the Court may in the interest of justice make the rule prospective . . . where the exigencies of the situation require such an application' . . . ." <i><span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">Johnson, supra,</a></span></i> 384 U. S., at 726-727. The criteria guiding resolution of the question implicate (a) the purpose to be served by the new standards, (b) the extent of the reliance by law enforcement authorities on the old standards, and (c) the effect on the administration of justice of a retroactive application of the new standards. "[T]he retroactivity or nonretroactivity of a rule is not automatically determined by the provision of the Constitution on which the dictate is based. Each constitutional rule of criminal procedure has its own distinct functions, its own background of precedent, and its own impact on the administration of justice, and the way in which these factors combine must inevitably vary with the dictate involved." <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#728" aria-description="Citation for case: Johnson v. New Jersey"><i>Johnson, supra,</i> at 728</a></span>.</p>
<p><i>Wade</i> and <i>Gilbert</i> fashion exclusionary rules to deter law enforcement authorities from exhibiting an accused to witnesses before trial for identification purposes without notice to and in the absence of counsel. A conviction which rests on a mistaken identification is a gross miscarriage of justice. The <i>Wade</i> and <i>Gilbert</i> rules are aimed at minimizing that possibility by preventing the unfairness at the pretrial confrontation that experience has proved can occur and assuring meaningful examination of the identification witness' testimony at trial. Does it follow that the rules should be applied retroactively? We do not think so.</p>
<p>It is true that the right to the assistance of counsel has been applied retroactively at stages of the prosecution where denial of the right must almost invariably deny a fair trial, for example, at the trial itself. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, or at some forms of arraignment. <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>, or on appeal, <i>Douglas</i> v. <i>California,</i> <span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span>. "The basic purpose <span class="star-pagination">*298</span> of a trial is the determination of truth, and it is self-evident that to deny a lawyer's help through the technical intricacies of a criminal trial or to deny a full opportunity to appeal a conviction because the accused is poor is to impede that purpose and to infect a criminal proceeding with the clear danger of convicting the innocent." <i>Tehan</i> v. <i>Shott, supra,</i> at 416. We have also retroactively applied rules of criminal procedure fashioned to correct serious flaws in the fact-finding process at trial. See for example <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368</a></span>. Although the <i>Wade</i> and <i>Gilbert</i> rules also are aimed at avoiding unfairness at the trial by enhancing the reliability of the fact-finding process in the area of identification evidence, "the question whether a constitutional rule of criminal procedure does or does not enhance the reliability of the fact-finding process at trial is necessarily a matter of degree." <i>Johnson</i> v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#728" aria-description="Citation for case: Johnson v. New Jersey"><i>New Jersey, supra,</i> at 728-729</a></span>. The extent to which a condemned practice infects the integrity of the truth-determining process at trial is a "question of probabilities." 384 U. S., at 729. Such probabilities must in turn be weighed against the prior justified reliance upon the old standard and the impact of retroactivity upon the administration of justice.</p>
<p>We have outlined in <i>Wade</i> the dangers and unfairness inherent in confrontations for identification. The possibility of unfairness at that point is great, both because of the manner in which confrontations are frequently conducted, and because of the likelihood that the accused will often be precluded from reconstructing what occurred and thereby from obtaining a full hearing on the identification issue at trial. The presence of counsel will significantly promote fairness at the confrontation and a full hearing at trial on the issue of identification. We have, therefore, concluded that the confrontation is a "critical stage," and that counsel is required at all confrontations. It must be recognized, however, that, unlike <span class="star-pagination">*299</span> cases in which counsel is absent at trial or on appeal, it may confidently be assumed that confrontations for identification can be and often have been conducted in the absence of counsel with scrupulous fairness and without prejudice to the accused at trial. Therefore, while we feel that the exclusionary rules set forth in <i>Wade</i> and <i>Gilbert</i> are justified by the need to assure the integrity and reliability of our system of justice, they undoubtedly will affect cases in which no unfairness will be present. Of course, we should also assume there have been injustices in the past which could have been averted by having counsel present at the confrontation for identification, just as there are injustices when counsel is absent at trial. But the certainty and frequency with which we can say in the confrontation cases that no injustice occurred differs greatly enough from the cases involving absence of counsel at trial or on appeal to justify treating the situations as different in kind for the purpose of retroactive application, especially in light of the strong countervailing interests outlined below, and because it remains open to all persons to allege and prove, as Stovall attempts to do in this case, that the confrontation resulted in such unfairness that it infringed his right to due process of law. See <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span> (C. A. 4th Cir. 1966).</p>
<p>The unusual force of the countervailing considerations strengthens our conclusion in favor of prospective application. The law enforcement officials of the Federal Government and of all 50 States have heretofore proceeded on the premise that the Constitution did not require the presence of counsel at pretrial confrontations for identification. Today's rulings were not foreshadowed in our cases; no court announced such a requirement until <i>Wade</i> was decided by the Court of Appeals for the Fifth Circuit, <span class="citation" data-id="9451495"><a href="/opinion/271227/billy-joe-wade-v-united-states/" aria-description="Citation for case: Billy Joe Wade v. United States">358 F. 2d 557</a></span>. The overwhelming majority of American courts have always treated the evidence question <span class="star-pagination">*300</span> not as one of admissibility but as one of credibility for the jury. Wall, Eye-Witness Identification in Criminal Cases 38. Law enforcement authorities fairly relied on this virtually unanimous weight of authority, now no longer valid, in conducting pretrial confrontations in the absence of counsel. It is, therefore, very clear that retroactive application of <i>Wade</i> and <i>Gilbert</i> "would seriously disrupt the administration of our criminal laws." <i>Johnson</i> v. <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#731" aria-description="Citation for case: Johnson v. New Jersey"><i>New Jersey, supra,</i> at 731</a></span>. In <i>Tehan</i> v. <i>Shott, supra</i><i>,</i> we thought it persuasive against retroactive application of the no-comment rule of <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>, that such application would have a serious impact on the six States that allowed comment on an accused's failure to take the stand. We said, "To require all of those States now to void the conviction of every person who did not testify at his trial would have an impact upon the administration of their criminal law so devastating as to need no elaboration." 382 U. S., at 419. That impact is insignificant compared to the impact to be expected from retroactivity of the <i>Wade</i> and <i>Gilbert</i> rules. At the very least, the processing of current criminal calendars would be disrupted while hearings were conducted to determine taint, if any, in identification evidence, and whether in any event the admission of the evidence was harmless error. Doubtless, too, inquiry would be handicapped by the unavailability of witnesses and dim memories. We conclude, therefore, that the <i>Wade</i> and <i>Gilbert</i> rules should not be made retroactive.</p>
<p>We also conclude that, for these purposes, no distinction is justified between convictions now final, as in the instant case, and convictions at various stages of trial and direct review. We regard the factors of reliance and burden on the administration of justice as entitled to such overriding significance as to make that distinction <span class="star-pagination">*301</span> unsupportable.<sup>[2]</sup> We recognize that Wade and Gilbert are, therefore, the only victims of pretrial confrontations in the absence of their counsel to have the benefit of the rules established in their cases. That they must be given that benefit is, however, an unavoidable consequence of the necessity that constitutional adjudications not stand as mere dictum. Sound policies of decision-making, rooted in the command of Article III of the Constitution that we resolve issues solely in concrete cases or controversies,<sup>[3]</sup> and in the possible effect upon the incentive of counsel to advance contentions requiring a change in the law,<sup>[4]</sup> militate against denying Wade and Gilbert the benefit of today's decisions. Inequity arguably results from according the benefit of a new rule to the parties in the case in which it is announced but not to other litigants similarly situated in the trial or appellate process who have raised the same issue.<sup>[5]</sup> But we regard the fact that the parties involved are chance beneficiaries as an insignificant cost for adherence to sound principles of decision-making.</p>
<p></p>
<h2>II.</h2>
<p>We turn now to the question whether petitioner, although not entitled to the application of <i>Wade</i> and <i>Gilbert</i> to his case, is entitled to relief on his claim that in any event the confrontation conducted in this <span class="star-pagination">*302</span> case was so unnecessarily suggestive and conductive to irreparable mistaken identification that he was denied due process of law. This is a recognized ground of attack upon a conviction independent of any right to counsel claim. <i>Palmer</i> v. <i>Peyton,</i> <span class="citation" data-id="271407"><a href="/opinion/271407/raymond-palmer-v-c-c-peyton-superintendent-of-the-virginia-state/" aria-description="Citation for case: Raymond Palmer v. C. C. Peyton, Superintendent of the...">359 F. 2d 199</a></span> (C. A. 4th Cir. 1966). The practice of showing suspects singly to persons for the purpose of identification, and not as part of a lineup, has been widely condemned.<sup>[6]</sup> However, a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it, and the record in the present case reveals that the showing of Stovall to Mrs. Behrendt in an immediate hospital confrontation was imperative. The Court of Appeals, <i>en banc,</i> stated <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#735" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d, at 735</a></span>,</p>
<blockquote>"Here was the only person in the world who could possibly exonerate Stovall. Her words, and only her words, `He is not the man' could have resulted in freedom for Stovall. The hospital was not far distant from the courthouse and jail. No one knew how long Mrs. Behrendt might live. Faced with the responsibility of identifying the attacker, with the need for immediate action and with the knowledge that Mrs. Behrendt could not visit the jail, the police followed the only feasible procedure and took Stovall to the hospital room. Under these circumstances, the usual police station line-up, which Stovall now argues he should have had, was out of the question."</blockquote>
<p>The judgment of the Court of Appeals is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE DOUGLAS is of the view that the deprivation of the right to counsel in the setting of this case <span class="star-pagination">*303</span> should be given retroactive effect as it was in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, and in <i>Douglas</i> v. <i>California,</i> <span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span>. And see <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#640" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 640</a></span> (dissenting opinion); <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#736" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 736</a></span> (dissenting opinion).</p>
<p>MR. JUSTICE FORTAS would reverse and remand for a new trial on the ground that the State's reference at trial to the improper hospital identification violated petitioner's Fourteenth Amendment rights and was prejudicial. He would not reach the question of retroactivity of <i>Wade</i> and <i>Gilbert.</i></p>
<p>MR. JUSTICE WHITE, whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART join.</p>
<p>For the reasons stated in my separate opinion in <i>United States</i> v. <i>Wade, ante,</i> p. 250, I perceive no constitutional error in the identification procedure to which the petitioner was subjected. I concur in the result and in that portion of the Court's opinion which limits application of the new Sixth Amendment rule.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>In <i>United States</i> v. <i>Wade, ante,</i> p. 218, and <i>Gilbert</i> v. <i>California, ante,</i> p. 263, the Court holds that lineup identification testimony should be excluded if it was obtained by exhibiting an accused to identifying witnesses before trial in the absence of his counsel. I concurred in part in those holdings as to out-of-court lineup identification on the ground that the right to counsel is guaranteed in federal courts by the Sixth Amendment and in state courts by the Sixth and Fourteenth Amendments. The first question in this case is whether other defendants, already in prison on <span class="star-pagination">*304</span> such unconstitutional evidence, shall be accorded the benefit of the rule. In this case the Court holds that the petitioner here, convicted on such unconstitutional evidence, must remain in prison, and that besides Wade and Gilbert, who are "chance beneficiaries," no one can invoke the rule except defendants exhibited in lineups in the future. I dissent from that holding. It keeps people serving sentences who were convicted through the use of unconstitutional evidence. This is sought to be justified on the ground that retroactive application of the holding in <i>Gilbert</i> and <i>Wade</i> would somehow work a "burden on the administration of justice" and would not serve the Court's purpose "to deter law enforcement authorities." It seems to me that to deny this petitioner and others like him the benefit of the new rule deprives them of a constitutional trial and perpetrates a rank discrimination against them. Once the Court determines what the Constitution says, I do not believe it has the power, by weighing "countervailing interests," to legislate a timetable by which the Constitution's provisions shall become effective. For reasons stated in my dissent in <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#640" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 640</a></span>, I would hold that the petitioner here and every other person in jail under convictions based on unconstitutional evidence should be given the advantage of today's newly announced constitutional rules.</p>
<p>The Court goes on, however, to hold that even though its new constitutional rule about the Sixth Amendment's right to counsel cannot help this petitioner, he is nevertheless entitled to a consideration of his claim, "independent of any right to counsel claim," that his identification by one of the victims of the robbery was made under circumstances so "unfair" that he was denied "due process of law" guaranteed by the Fourteenth Amendment. Although the Court finds petitioner's claim without merit, I dissent from its holding that a general <span class="star-pagination">*305</span> claim of "unfairness" at the lineup is "open to all persons to allege and prove." The term "due process of law" is a direct descendant of Magna Charta's promise of a trial according to the "law of the land" as it has been established by the lawmaking agency, constitutional or legislative. No one has ever been able to point to a word in our constitutional history that shows the Framers ever intended that the Due Process Clause of the Fifth or Fourteenth Amendment was designed to mean any more than that defendants charged with crimes should be entitled to a trial governed by the laws, constitutional and statutory, that are in existence at the time of the commission of the crime and the time of the trial. The concept of due process under which the Court purports to decide this question, however, is that this Court looks at "the totality of the circumstances" of a particular case to determine in its own judgment whether they comport with the Court's notions of decency, fairness, and fundamental justice, and, if so, declares they comport with the Constitution, and, if not, declares they are forbidden by the Constitution. See, <i>e. g., </i><i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>. Such a constitutional formula substitutes this Court's judgment of what is right for what the Constitution declares shall be the supreme law of the land. This due process notion proceeds as though our written Constitution, designed to grant limited powers to government, had neutralized its limitations by using the Due Process Clause to authorize this Court to override its written limiting language by substituting the Court's view of what powers the Framers should have granted government. Once again I dissent from any such view of the Constitution. Where accepted, its result is to make this Court not a Constitution-interpreter, but a day-to-day Constitution-maker.</p>
<p>But even if the Due Process Clause could possibly be construed as giving such latitudinarian powers to the <span class="star-pagination">*306</span> Court, I would still think the Court goes too far in holding that the courts can look at the particular circumstances of each identification lineup to determine at large whether they are too "suggestive and conducive to irreparable mistaken identification" to be constitutional. That result is to freeze as constitutional or as unconstitutional the circumstances of each case, giving the States and the Federal Government no permanent constitutional standards. It also transfers to this Court power to determine what the Constitution should say, instead of performance of its undoubted constitutional power to determine what the Constitution does say. And the result in this particular case is to put into a constitutional mould a rule of evidence which I think is plainly within the constitutional powers of the States in creating and enforcing their own criminal laws. I must say with all deference that for this Court to hold that the Due Process Clause gives it power to bar state introduction of lineup testimony on its notion of fairness, not because it violates some specific constitutional prohibition, is an arbitrary, wholly capricious action.</p>
<p>I would not affirm this case but would reverse and remand for consideration of whether the out-of-court lineup identification of petitioner was, under <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span>, harmless error. If it was not, petitioner is entitled to a new trial because of a denial of the right to counsel guaranteed by the Sixth Amendment which the Fourteenth Amendment makes obligatory on the States.</p>
<h2>NOTES</h2>
<p>[1]  Although respondent did not raise the bar of retroactivity, the Attorney General of the State of New York, as <i>amicus curiae,</i> extensively briefed the issue of retroactivity and petitioner, in his reply brief, addressed himself to this question. Compare <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#646" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 646, n. 3</a></span>.</p>
<p>[2]  Schaefer, The Control of "Sunbursts": Techniques of Prospective Overruling, 22 Record of N. Y. C. B. A. 394, 408-411 (1967).</p>
<p>[3]  Note, Prospective Overruling and Retroactive Application in the Federal Courts, 71 Yale L. J. 907, 930-933 (1962).</p>
<p>[4]  See Mishkin, Foreword, The Supreme Court 1964 Term, <span class="citation no-link">79 Harv. L. Rev. 56</span>, 60-61 (1965).</p>
<p>[5]  See Mishkin, n. 4, <i>supra,</i> at 61, n. 23; Bender, The Retroactive Effect of an Overruling Constitutional Decision: <i>Mapp</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span>,</i> <span class="citation no-link">110 U. Pa. L. Rev. 650</span>, 675-678 (1962); Schwartz, Retroactivity, Reliability, and Due Process: A Reply to Professor Mishkin, <span class="citation no-link">33 U. Chi. L. Rev. 719</span>, 764 (1966).</p>
<p>[6]  See Wall, Eye-Witness Identification in Criminal Cases 26-40; Paul, Identification of Accused Persons, 12 Austl. L. J. 42, 44 (1938); Williams &amp; Hammelmann, Identification Parades, Part I, [1963] Crim. L. Rev. 479, 480-481; Frankfurter, The Case of Sacco and Vanzetti 31-32.</p>

</div>
```

---
