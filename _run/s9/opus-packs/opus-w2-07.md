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

## GROUP: _overhaul2/lake/cases/California v. Trombetta.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: California v. Trombetta
type: case
citation: "467 U.S. 479 (1984)"
parallel_cite: "104 S. Ct. 2528; 81 L. Ed. 2d 413; 52 U.S.L.W. 4744"
neutral_cite: 1984 U.S. LEXIS 103
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-06-11
docket: No. 83-305
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
  opinion_url: "https://www.courtlistener.com/opinion/111206/california-v-trombetta/"
  cluster_id: 111206
  opinion_id: null
  identity_checked: true
lake:
  record_id: California v. Trombetta
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Anchor
related:
  - "[[Brady and Giglio]]"
  - "[[Arizona v. Youngblood]]"
tags:
  - case
  - fourteenth-amendment
  - due-process
  - preservation-of-evidence
  - brady
  - dui
holding: "The Due Process Clause does not require law enforcement to preserve breath samples taken from suspected drunk drivers, because the constitutional duty to preserve evidence reaches only evidence whose exculpatory value was apparent before it was destroyed and that the defendant cannot replace by other reasonably available means."
aliases:
  - California v. Trombetta
  - "California v. Trombetta (1984)"
---

# California v. Trombetta

*467 U.S. 479 (1984)* (No. 83-305) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 111206 → combined opinion 111206 (Marshall, J.; 467 U.S. 479, decided June 11, 1984). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*489`). S9 promotes. -->

## Background
The respondents were arrested for driving while intoxicated after failing breath-analysis tests on an Intoxilyzer machine. Under California's testing practices, the breath samples themselves were not preserved after the machine produced its blood-alcohol reading. The respondents moved to suppress the test results, arguing that the State's failure to save the samples — which they might have tested independently — deprived them of potentially [[Brady and Giglio|exculpatory]] evidence in violation of due process. The California Court of Appeal agreed and held the results inadmissible.

## Issue
Whether the Due Process Clause requires the police to preserve breath samples of suspected drunk drivers so that defendants may subject them to independent testing.

## Rule
The Court held that whatever duty the Constitution imposes to preserve evidence is a limited one, defined by two requirements the lost evidence must meet: "evidence must both possess an exculpatory value that was apparent before the evidence was destroyed, and be of such a nature that the defendant would be unable to obtain comparable evidence by other reasonably available means." — 467 U.S. at 489. ^pin-489

## Application
Breath samples satisfied neither requirement. Given the Intoxilyzer's demonstrated and certified accuracy, the chance that a preserved sample would have been [[Brady and Giglio|exculpatory]] was "extremely low" — so any [[Brady and Giglio|exculpatory]] value was speculative, not apparent. And defendants had other, comparable ways to challenge a reading: inspecting the machine's calibration and operation, and cross-examining the officer who administered the test. Because the samples were neither apparently [[Brady and Giglio|exculpatory]] nor irreplaceable, the State's failure to preserve them did not offend due process.

## Conclusion
The judgment was **reversed**. Marshall, J., delivered the opinion of a unanimous Court; O'Connor, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Trombetta* fixes the duty-to-preserve standard for evidence of **apparent [[Brady and Giglio|exculpatory]] value**. Its companion rule — for evidence that is only **potentially useful**, where the defendant must instead prove **bad faith** — arrived four years later in *[[Arizona v. Youngblood]]* (1988). Teach the two as a pair: *Trombetta* sets the materiality gate; *[[Arizona v. Youngblood|Youngblood]]* supplies the bad-faith gate for everything short of apparent [[Brady and Giglio|exculpatory]] value.

## Appears on
- [[Brady and Giglio]] — *Anchor*

## Sources
- [*California v. Trombetta*, 467 U.S. 479 (1984)](https://www.courtlistener.com/opinion/111206/california-v-trombetta/) — pinpoint: 489 (Marshall, J., for the Court; the CL opinion text carries the reporter star `*489` immediately before the two-part standard). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "24fdfb72a0de344c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "California v. Trombetta"}, "payload": {"all": [{"cite": "467 U.S. 479", "page": "479", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "467"}, {"cite": "104 S. Ct. 2528", "page": "2528", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "81 L. Ed. 2d 413", "page": "413", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "1984 U.S. LEXIS 103", "page": "103", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4744", "page": "4744", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "467 U.S. 479", "official": {"cite": "467 U.S. 479", "page": "479", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "467"}, "official_selection_present": true, "record_id": "California v. Trombetta"}}
{"assertion_id": "1086b2049660413b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "California v. Trombetta"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "California v. Trombetta", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — California v. Trombetta

```json
{
  "schema_version": "s2.v1",
  "record_id": "California v. Trombetta",
  "status": "under_review",
  "identity": {
    "case_name": "California v. Trombetta",
    "case_name_short": "Trombetta",
    "case_name_full": "CALIFORNIA v. TROMBETTA Et Al.",
    "input_case_name": "California v. Trombetta",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-06-11",
    "year": 1984,
    "docket": "No. 83-305",
    "cluster_id": 111206,
    "lead_opinion_id": 9429651,
    "sibling_ids": [],
    "absolute_url": "/opinion/111206/california-v-trombetta/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 479",
      "volume": "467",
      "reporter": "U.S.",
      "page": "479",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2528",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 413",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4744",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4744",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 103",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 479",
        "volume": "467",
        "reporter": "U.S.",
        "page": "479",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2528",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 413",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 103",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "103",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4744",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4744",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 479",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 479",
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
    "date_created": "2026-07-06T13:45:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "california-v-trombetta--111206",
      "to_record_id": "California v. Trombetta",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — California v. Trombetta

```
<opinion type="majority">
<author id="b538-10">Justice Marshall</author>
<p id="AHv">delivered the opinion of the Court.</p>
<p id="b538-11">The Due Process Clause of the Fourteenth Amendment requires the State to disclose to criminal defendants favorable evidence that is material either to guilt or to punishment. <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976); <em>Brady </em>v. <page-number citation-index="1" label="481">*481</page-number><em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963). This case raises the question whether the Fourteenth Amendment also demands that the State preserve potentially exculpatory evidence on behalf of defendants. In particular, the question presented is whether the Due Process Clause requires law enforcement agencies to preserve breath samples of suspected drunken drivers in order for the results of breath-analysis tests to be admissible in criminal prosecutions.</p>
<p id="b539-8">f — I</p>
<p id="b539-3">The Omicron Intoxilyzer (Intoxilyzer) is a device used in California to measure the concentration of alcohol in the blood of motorists suspected of driving while under the influence of intoxicating liquor.<footnotemark>1</footnotemark> The Intoxilyzer analyzes the suspect’s breath. To operate the device, law enforcement officers follow these procedures:</p>
<blockquote id="b539-4">“Prior to any test, the device is purged by pumping clean air through it until readings of 0.00 are obtained. The breath test requires a sample of‘alveolar’ (deep lung) air; to assure that such a sample is obtained, the subject is required to blow air into the intoxilyzer at a constant pressure for a period of several seconds. A breath sample is captured in the intoxilyzer’s chamber and infrared light is used to sense the alcohol level. Two samples are taken, and the result of each is indicated on a printout card. The two tests must register within 0.02 of each other in order to be admissible in court. After each test, the chamber is purged with clean air and then <page-number citation-index="1" label="482">*482</page-number>checked for a reading of zero alcohol. The machine is calibrated weekly, and the calibration results, as well as a portion of the calibration samples, are available to the defendant.” <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#141" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d 138, 141-142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#321" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr. 319, 321</a></span> (1983) (citations omitted).</blockquote>
<p id="b540-5">In unrelated incidents in 1980 and 1981, each of the respondents in this case was stopped on suspicion of drunken driving on California highways. Each respondent submitted to an Intoxilyzer test.<footnotemark>2</footnotemark> Each respondent registered a blood-alcohol concentration substantially higher than 0.10 percent. Under California law at that time, drivers with higher than 0.10 percent blood-alcohol concentrations were presumed to be intoxicated. Cal. Veh. Code Ann. § 23126(a)(3) (West 1971) (amended 1981). Respondents were all charged with driving while intoxicated in violation of Cal. Veh. Code Ann. §23102 (West 1971) (amended 1981).</p>
<p id="b540-6">Prior to trial in Municipal Court, each respondent filed a motion to suppress the Intoxilyzer test results on the ground that the arresting officers had failed to preserve samples of respondents' breath. Although preservation of breath samples is technically feasible,<footnotemark>3</footnotemark> California law enforcement offi<page-number citation-index="1" label="483">*483</page-number>cers do not ordinarily preserve breath samples, and made no effort to do so in these cases. Respondents each claimed that, had a breath sample been preserved, he would have been able to impeach the incriminating Intoxilyzer results. All of respondents’ motions to suppress were denied. Respondents Ward and Berry then submitted their cases on the police records and were convicted. Ward and Berry subsequently petitioned the California Court of Appeal for writs of habeas corpus. Respondents Trombetta and Cox did not submit to trial. They sought direct appeal from the Municipal Court orders, and their appeals were eventually transferred to the Court of Appeal to be consolidated with the Ward and Berry petitions.<footnotemark>4</footnotemark></p>
<p id="b541-5">The California Court of Appeal ruled in favor of respondents. After implicitly accepting that breath samples would be useful to respondents’ defenses, the court reviewed the available technologies and determined that the arresting officers had the capacity to preserve breath samples for respondents. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#141" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 141-142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#320" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 320-321</a></span>. Relying heavily on the California Supreme Court’s decision in <em>People </em>v. <em>Hitch, </em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">12 Cal. 3d 641</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">527 P. 2d 361</a></span> (1974), the Court of Appeal concluded: “Due process demands simply that where evidence is collected by the state, as it is with the intoxilyzer, or any other breath testing device, law enforcement agencies must establish and follow rigorous and <page-number citation-index="1" label="484">*484</page-number>systematic procedures to preserve the captured evidence or its equivalent for the use of the defendant.” <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#144" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#323" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 323</a></span>.<footnotemark>5</footnotemark> The court granted respondents Ward and Berry new trials, and ordered that the Intoxilyzer results not be admitted as evidence against the other two respondents. The State unsuccessfully petitioned for certiorari in the California Supreme Court, and then petitioned for review in this Court. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./464/1037/">464 U. S. 1037</a></span> (1984), and now reverse.</p>
<p id="b543-4"><page-number citation-index="1" label="485">*485</page-number>II</p>
<p id="b543-5">Under the Due Process Clause of the Fourteenth Amendment, criminal prosecutions must comport with prevailing notions of fundamental fairness. We have long interpreted this standard of fairness to require that criminal defendants be afforded a meaningful opportunity to present a complete defense. To safeguard that right, the Court has developed “what might loosely be called the area of constitutionally guaranteed access to evidence.” <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#867" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 867</a></span> (1982). Taken together, this group of constitutional privileges delivers exculpatory evidence into the hands of the accused, thereby protecting the innocent from erroneous conviction and ensuring the integrity of our criminal justice system.</p>
<p id="b543-6">The most rudimentary of the access-to-evidence cases impose upon the prosecution a constitutional obligation to report to the defendant and to the trial court whenever government witnesses lie under oath. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269-272</a></span> (1959); see also <em>Mooney </em>v. <em>Holohan, </em><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span> (1935). But criminal defendants are entitled to much more than protection against perjury. A defendant has a constitutionally protected privilege to request and obtain from the prosecution evidence that is either material to the guilt of the defendant or relevant to the punishment to be imposed. <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>. Even in the absence of a specific request, the prosecution has a constitutional duty to turn over exculpatory evidence that would raise a reasonable doubt about the defendant’s guilt. <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U. S., at 112</a></span>. The prosecution must also reveal the contents of plea agreements with key government witnesses, see <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">405 U. S. 150</a></span> (1972), and under some circumstances may be required to disclose the identity of undercover informants who possess evidence critical to the defense, <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957).</p>
<p id="b544-4"><page-number citation-index="1" label="486">*486</page-number>Less clear from our access-to-evidence cases is the extent to which the Due Process Clause imposes on the government the additional responsibility of guaranteeing criminal defendants access to exculpatory evidence beyond the government’s possession. On a few occasions, we have suggested that the Federal Government might transgress constitutional limitations if it exercised its sovereign powers so as to hamper a criminal defendant’s preparation for trial. For instance, in <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#324" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 324</a></span> (1971), and in <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#795" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 795, n. 17</a></span> (1977), we intimated that a due process violation might occur if the Government delayed an indictment for so long that the defendant’s ability to mount an effective defense was impaired. Similarly, in <em>United States </em>v. <em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/" aria-description="Citation for case: United States v. Valenzuela-Bernal">Valenzuela-Bernal, supra,</a></span> </em>we acknowledged that the Government could offend the Due Process Clause of the Fifth Amendment if, by deporting potential witnesses, it diminished a defendant’s opportunity to put on an effective defense.<footnotemark>6</footnotemark> <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#873" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S., at 873</a></span>.</p>
<p id="b544-5">We have, however, never squarely addressed the government’s duty to take affirmative steps to preserve evidence on behalf of criminal defendants. The absence of doctrinal development in this area reflects, in part, the difficulty of developing rules to deal with evidence destroyed through prosecutorial neglect or oversight. Whenever potentially exculpatory evidence is permanently lost, courts face the treacherous task of divining the import of materials whose contents are unknown and, very often, disputed. Cf. <em>United States </em>v. <span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#870" aria-description="Citation for case: United States v. Valenzuela-Bernal"><em>Valenzuela-Bernal, supra, </em>at 870</a></span>. Moreover, fashioning remedies for the illegal destruction of evidence can pose troubling choices. In nondisclosure cases, a court can <page-number citation-index="1" label="487">*487</page-number>grant the defendant a new trial at which the previously suppressed evidence may be introduced. But when evidence has been destroyed in violation of the Constitution, the court must choose between barring further prosecution or suppressing — as the California Court of Appeal did in this case— the State’s most probative evidence. '</p>
<p id="b545-5">One case in which we have discussed due process constraints on the Government’s failure to preserve potentially exculpatory evidence is <em>Killian </em>v. <em>United States, </em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">368 U. S. 231</a></span> (1961). In <em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">Killian</a></span>, </em>the petitioner had been convicted of giving false testimony in violation of <span class="citation no-link">18 U. S. C. § 1001</span>. A key element of the Government’s case was an investigatory report prepared by the Federal Bureau of Investigation. The Solicitor General conceded that, prior to petitioner’s trial, the F. B. I. agents who prepared the investigatory report destroyed the preliminary, notes they had made while interviewing witnesses. The petitioner argued that these notes would have been helpful to his defense and that the agents had violated the Due Process Clause by destroying this exculpatory evidence. While not denying that the notes might have contributed to the petitioner’s defense, the Court ruled that their destruction did not rise to the level of constitutional violation:</p>
<blockquote id="b545-6">“If the agents’ notes . . . were made only for the purpose of transferring the data thereon . . . , and if, having served that purpose, they were destroyed by the agents in good faith and in accord with their normal practices, it would be clear that their destruction did not constitute an impermissible destruction of evidence nor deprive petitioner of any right.” <span class="citation no-link"><em>Id., </em>at 242</span>.</blockquote>
<p id="b545-7">In many respects the instant case is reminiscent of <em>Killian </em>v. <em>United States. </em>To the extent that respondents’ breath samples came into the possession of California authorities, it was for the limited purpose of providing raw data to the <page-number citation-index="1" label="488">*488</page-number>Intoxilyzer.<footnotemark>7</footnotemark> The evidence to be presented at trial was not the breath itself but rather the Intoxilyzer results obtained from the breath samples. As the petitioner in <em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/" aria-description="Citation for case: Killian v. United States">Killian</a></span> </em>wanted the agents’ notes hi order to impeach their final reports, respondents here seek the breath samples in order to challenge incriminating tests results produced with the Intoxilyzer.</p>
<p id="b546-4">Given our precedents in this area, we cannot agree with the California Court of Appeal that the State’s failure to retain breath samples for respondents constitutes a violation of the Federal Constitution. To begin with, California authorities in this case did not destroy respondents’ breath samples in a calculated effort to circumvent the disclosure requirements established by <em>Brady </em>v. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Maryland</a></span> </em>and its progeny. In failing to preserve breath samples for respondents, the officers here were acting “in good faith and in accord with their normal practice.” <em>Killian </em>v. <em>United States, supra, </em>at 242. The record contains no allegation of official animus towards respondents or of a conscious effort to suppress exculpatory evidence.</p>
<p id="b546-5">More importantly, California’s policy of not preserving breath samples is without constitutional defect. Whatever duty the Constitution imposes on the States to preserve evidence, that duty must be limited to evidence that might be expected to play a significant role in the suspect’s defense.<footnotemark>8</footnotemark> <page-number citation-index="1" label="489">*489</page-number>To meet this standard of constitutional materiality, see <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#109" aria-description="Citation for case: United States v. Agurs">427 U. S., at 109-110</a></span>, evidence must both possess an exculpatory value that was apparent before the evidence was destroyed, and be of such a nature that the defendant would be unable to obtain comparable evidence by other reasonably available means. Neither of these conditions is met on the facts of this case.</p>
<p id="b547-5">Although the preservation of breath samples might conceivably have contributed to respondents’ defenses, a dispassionate review of the Intoxilyzer and the California testing procedures can only lead one to conclude that the chances are extremely low that preserved samples would have been exculpatory. The accuracy of the Intoxilyzer has been reviewed and certified by the California Department of Health.<footnotemark>9</footnotemark> To protect suspects against machine malfunctions, the Department has developed test procedures that include two independent measurements (which must be closely correlated for the results to be admissible) bracketed by blank runs designed to ensure that the machine is purged of alcohol traces from previous tests. See <em>supra, </em>at 481-482. In all but a tiny fraction of cases, preserved breath samples would simply confirm the Intoxilyzer’s determination that the defendant had a high level of blood-alcohol concentration at the time of the test. Once the Intoxilyzer indicated that respondents were legally drunk, breath samples were much more likely to provide inculpatory than exculpatory evidence.<footnotemark>10</footnotemark></p>
<p id="b548-4"><page-number citation-index="1" label="490">*490</page-number>Even if one were to assume that the Intoxilyzer results in this case were inaccurate and that breath samples might therefore have been exculpatory, it does not follow that respondents were without alternative means of demonstrating their innocence. Respondents and <em>amici </em>have identified only a limited number of ways in which an Intoxilyzer might malfunction: faulty calibration, extraneous interference with machine measurements, and operator error. See Brief for Respondents 32-34; Brief for California Public Defender’s Association et al. as <em>Amici Curiae </em>25-40. Respondents were perfectly capable of raising these issues without resort to preserved breath samples. To protect against faulty calibration, California gives drunken driving defendants the opportunity to inspect the machine used to test their breath as well as that machine’s weekly calibration results and the breath samples used in the calibrations. See <em>supra, </em>at 481-482. Respondents could have utilized these data to impeach the machine’s reliability. As to improper measurements, the parties have identified only two sources capable of interfering with test results: radio waves and chemicals that appear in the blood of those who are dieting. For defendants whose test results might have been affected by either of these factors, it remains possible to introduce at trial evidence demonstrating that the defendant was dieting at the time of the test or that the test was conducted near a source of radio waves. Finally, as to operator error, the defendant retains the right to cross-examine the law enforcement officer who administered the Intoxilyzer test, and to attempt to raise doubts in the mind of the factfinder whether the test was properly administered.<footnotemark>11</footnotemark></p>
<p id="ABc"><page-number citation-index="1" label="491">*491</page-number>H-1 I — H</p>
<p id="Avg">We conclude, therefore, that the Due Process Clause of the Fourteenth Amendment does not require that law enforcement agencies preserve breath samples in order to introduce the results of breath-analysis tests at trial.<footnotemark>12</footnotemark> Accordingly, the judgment of the California Court of Appeal is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="Abc">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b539-5"> Law enforcement agencies in California are obliged to use breath-analysis equipment that has been approved by the State’s Department of Health. See 17 <span class="citation no-link">Cal. Admin. Code § 1221</span> (1976). The Department has approved a number of blood-alcohol testing devices employing a variety of technologies, see List of Instruments and Related Accessories Approved for Breath Alcohol Analysis (Dec. 20, 1979), reprinted in App. 238-247, of which the Omicron Intoxilyzer is the most popular model, see Brief for Petitioner 6, n. 6.</p>
</footnote>
<footnote label="2">
<p id="b540-7"> Under California law, drunken driving suspects are given the choice of having their blood-alcohol concentraton determined by either a blood test, a urine test, or a breath test. Cal. Veh. Code Ann. § 13353 (West 1971 and Supp. 1984). Suspects who refuse to submit to any test are liable to have their driving licenses suspended. <em>Ibid.</em></p>
</footnote>
<footnote label="3">
<p id="b540-8"> The California Department of Health has approved a device, known as an Intoximeter Field Crimper-Indium Tube Encapsulation Kit (Kit), which officers can use to preserve breath samples. App. 247. To use the Kit, a suspect must breathe directly into an indium tube, which preserves samples in three separate chambers. See <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#142" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d 138, 142</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#321" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr. 319, 321</a></span> (1983). The breath trapped in each chamber can later be used to determine the suspect’s blood-alcohol concentration through the use of a laboratory instrument known as a Gas Chromatograph Intoxi-meter, which has also been approved by the California Department of Health. App. 242-243. Because the suspect must breathe directly into the indium tube, the Kit cannot be used to preserve the same breath sample used in an Intoxilyzer test. See, <em>supra, </em>at 481-482. Other devices, <page-number citation-index="1" label="483">*483</page-number>similar in function to the Kit, can be attached to an Intoxilyzer and used to collect the air that the Intoxilyzer purges, see Brief for Respondents 18-19, but none of these devices has yet received approval from the California Department of Health, see Reply Brief for Petitioner 3-4.</p>
</footnote>
<footnote label="4">
<p id="b541-9"> The California Court of Appeal expressed some doubt whether respondents Trombetta and Cox were entitled to appeal their suppression orders and ultimately ordered that their appeals be dismissed. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#140" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 140, 143</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#320" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 320, 323</a></span>. The court, however, ruled on the merits of their claims and thereby exercised jurisdiction over their appeals. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#144" aria-description="Citation for case: People v. Trombetta"><em>Id., </em>at 144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#323" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 323</a></span>. As to Trombetta and Cox, the Court of Appeal decision was comparable to a judgment affirming a suppression order, which is reviewable in this Court under <span class="citation no-link">28 U. S. C. § 1257</span>(3). Cf., <em>e. g., Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287</a></span> (1984).</p>
</footnote>
<footnote label="5">
<p id="b542-5"> <em>People </em>v. <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>involved another device used to measure blood-alcohol concentrations. With that device, a suspect’s breath bubbles through a glass ampoule containing special chemicals that change colors depending on the amount of alcohol in the suspect’s blood. <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#644" aria-description="Citation for case: People v. Hitch">12 Cal. 3d, at 644</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#363" aria-description="Citation for case: People v. Hitch">527 P. 2d, at 363-364</a></span>. In keeping with California procedures, law enforcement officials in <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>discarded the ampoule after they had completed their testing, even though the ampoule might have been saved for retesting by the defendant. Relying on this Court’s decisions in <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), and <em>Giglio </em>v. <em>United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#153" aria-description="Citation for case: Giglio v. United States">405 U. S. 150, 153-154</a></span> (1972), the California Supreme Court concluded that the Due Process Clause is implicated when a State intentionally destroys evidence that might have proved favorable to a criminal defendant. <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#645" aria-description="Citation for case: People v. Hitch">12 Cal. 3d, at 645-650</a></span>, <span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/#364" aria-description="Citation for case: People v. Hitch">527 P. 2d, at 364-370</a></span>. The <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>decision was noteworthy in that it extrapolated from <em>Brady’s </em>disclosure requirement an additional constitutional duty on the part of prosecutors to preserve potentially exculpatory evidence. See Note, The Right to Independent Testing: A New Hitch in the Preservation of Evidence Doctrine, <span class="citation no-link">75 Colum. L. Rev. 1355</span>, 1364-1368 (1975); cf. <em>United States </em>v. <em>Bryant, </em>142 U. S. App. D. C. 132, 141, <span class="citation" data-id="9456634"><a href="/opinion/295318/united-states-v-carlton-e-bryant-united-states-of-america-v-william-e/#651" aria-description="Citation for case: United States v. Carlton E. Bryant, United States of...">439 F. 2d 642, 651</a></span> (1971) (Wright, J.) (Government must make “ ‘earnest efforts’ to pre serve crucial materials and to find them once a discovery request is made”).</p>
<p id="b542-6">For a number of years, there was uncertainty whether the California courts would extend the <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>decision to the Intoxilyzer. In <em>People </em>v. <em>Miller, </em><span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">52 Cal. App. 3d 666</a></span>, <span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">125 Cal. Rptr. 341</a></span> (1975), a Court of Appeal panel refused to extend <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span> </em>because the Intoxilyzer does not reduce breath samples to a preservable form comparable to the ampoules created with the device involved in <em><span class="citation" data-id="9548888"><a href="/opinion/1176854/people-v-hitch/" aria-description="Citation for case: People v. Hitch">Hitch</a></span>. </em>The Court of Appeal in <em>Trombetta </em>declined to follow <em><span class="citation" data-id="2140951"><a href="/opinion/2140951/people-v-miller/" aria-description="Citation for case: People v. Miller">Miller</a></span>, </em>and reasoned that as long as there were other methods of preserving specimens (such as the Indium Tube Kit, see n. 3, <em>supra), </em>the State was obliged to preserve a breath sample equivalent to the one used in the Intoxilyzer. <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#143" aria-description="Citation for case: People v. Trombetta">142 Cal. App. 3d, at 143-144</a></span>, <span class="citation" data-id="9729885"><a href="/opinion/2169170/people-v-trombetta/#322" aria-description="Citation for case: People v. Trombetta">190 Cal. Rptr., at 322-323</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b544-6"> In related cases arising under the Sixth and Fourteenth Amendments, we have recognized that criminal defendants are entitled to call witnesses on their own behalf and to cross-examine witnesses who have testified on the government’s behalf. See <em>Davis </em>v. <em>Alaska, </em><span class="citation" data-id="9425616"><a href="/opinion/108974/davis-v-alaska/" aria-description="Citation for case: Davis v. Alaska">415 U. S. 308</a></span> (1974); <em>Washington </em>v. <em>Texas, </em><span class="citation" data-id="9423455"><a href="/opinion/107481/washington-v-texas/" aria-description="Citation for case: Washington v. Texas">388 U. S. 14</a></span> (1967).</p>
</footnote>
<footnote label="7">
<p id="b546-6"> We accept the California Court of Appeal’s conclusion that the Intox-ilyzer procedure brought respondents’ breath samples into the possession of California officials. The capacity to preserve breath samples is equivalent to the actual possession of samples. See n. 5, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b546-7"> In our prosecutorial disclosure cases, we have imposed a similar requirement of materiality, <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), and have rejected the notion that a “prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>; see also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972) (“We know of no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case”).</p>
</footnote>
<footnote label="9">
<p id="b547-6"> The Intoxilyzer has also passed accuracy requirements established by the National Highway Traffic Safety Administration of the Department of Transportation. See <span class="citation no-link">38 Fed. Reg. 30459</span> (1973); A. Flores, Results of the First Semi-Annual Qualification Testing of Devices to Measure Breath Alcohol 10 (Dept, of Transportation 1975).</p>
</footnote>
<footnote label="10">
<p id="b547-7"> The materiality of breath samples is directly related to the reliability of the Intoxilyzer itself. The degree to which preserved samples are material depends on how reliable the Intoxilyzer is. This correlation suggests that a more direct constitutional attack might be made on the sufficiency of the evidence underlying the State’s case. After all, if the Intoxilyzer were <page-number citation-index="1" label="490">*490</page-number>truly prone to erroneous readings, then Intoxilyzer results without more might be insufficient to establish guilt beyond a reasonable doubt. <em>Jackson </em>v. <em>Virginia, </em><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U. S. 307</a></span> (1979).</p>
</footnote>
<footnote label="11">
<p id="b548-6"> Respondents could also have protected themselves from erroneous on-the-scene testing by electing to submit to urine or blood tests, see n. 2, <em>supra, </em>because the State automatically would have preserved urine and <page-number citation-index="1" label="491">*491</page-number>blood samples for retesting by respondents. Respondents, however, were not informed of the difference between the various testing procedures when they were asked to select among the three available methods of testing blood-alcohol concentrations. But see Cal. Veh. Code Ann. § 13353.5 (West 1971) (enacted in 1983) (requiring suspects to be informed that samples will be retained only in urine and blood tests). To the extent that this and other access-to-evidence cases turn on the underlying fairness of governmental procedures, it would be anomalous to permit the State to justify its actions by relying on procedural alternatives that were available, but unknown to the defendant. Similarly, it is irrelevant to our inquiry that California permits an accused drunken driver to have a second blood-alcohol test conducted by independent experts, since there is no evidence on this record that respondents were aware of this alternative.</p>
</footnote>
<footnote label="12">
<p id="AdNB"> State courts and legislatures, of course, remain free to adopt more rigorous safeguards governing the admissibility of scientific evidence than those imposed by the Federal Constitution. See, <em>e. g., Lauderdale </em>v. <em>State, </em><span class="citation" data-id="1351919"><a href="/opinion/1351919/lauderdale-v-state/" aria-description="Citation for case: Lauderdale v. State">548 P. 2d 376</a></span> (Alaska 1976); <em>City of Lodi </em>v. <em>Hine, </em><span class="citation" data-id="1800375"><a href="/opinion/1800375/city-of-lodi-v-hine/" aria-description="Citation for case: City of Lodi v. Hine">107 Wis. 2d 118</a></span>, <span class="citation" data-id="1800375"><a href="/opinion/1800375/city-of-lodi-v-hine/" aria-description="Citation for case: City of Lodi v. Hine">318 N. W. 2d 383</a></span> (1982).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Camara v. Municipal Court.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Camara v. Municipal Court"
type: case
citation: "387 U.S. 523 (1967)"
parallel_cite: "87 S. Ct. 1727; 18 L. Ed. 2d 930"
neutral_cite: 1967 U.S. LEXIS 1254
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-05
docket: 92
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Camara v. Municipal Court
  varies_by_point: false
  scope_note: "Overruled Frank v. Maryland; remains the foundational administrative-warrant case."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/"
  cluster_id: 107473
  opinion_id: 107473
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[See v. City of Seattle]]", "[[City of Los Angeles v. Patel]]", "[[New York v. Burger]]"]
aliases: ["Camara v. Municipal Court of City and County of San Francisco"]
tags: ["case", "fourth-amendment", "administrative-search", "inspection", "warrant"]
holding: "Administrative inspections of private property generally require a warrant, but it may be an \"area warrant\" issued on reasonable…"
lake:
  record_id: Camara v. Municipal Court
  status: under_review
  projected_at: 2026-07-06
---

# Camara v. Municipal Court

*387 U.S. 523 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A San Francisco housing inspector sought to enter Camara's residence for a routine code inspection without a warrant. Camara refused entry on three occasions and was criminally charged under the ordinance for refusing to permit the warrantless inspection. He challenged the constitutionality of compelling a warrantless administrative inspection.

## Issue
Whether administrative inspections of private property require a warrant, and on what showing of "probable cause" such a warrant may issue.

## Rule
Administrative inspections require a warrant procedure: "we hold that administrative searches of the kind at issue here are significant intrusions upon the interests protected by the Fourth Amendment, that such searches when authorized and conducted without a warrant procedure lack the traditional safeguards which the Fourth Amendment guarantees to the individual". — 387 U.S. at 534. ^pin-534

But probable cause for such a warrant can rest on reasonable area standards rather than individualized suspicion: "'probable cause' to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling." — *Id.* at 538. ^pin-538

## Application
Camara had a constitutional right to insist on a warrant before the housing inspection, so he could not be criminally punished for refusing a warrantless one. Because the inspection program's goals could be met through area warrants issued on reasonable administrative standards, requiring a warrant did not frustrate the program; the warrantless-inspection scheme could not be enforced against him.

## Conclusion
A warrant was required for the administrative inspection; Camara's conviction for refusing the warrantless inspection could not stand (overruling *Frank v. Maryland*).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Camara* **overruled** *[[Frank v. Maryland]]*, was extended to commercial premises in [[See v. City of Seattle]], and its pre-compliance-review principle was applied in [[City of Los Angeles v. Patel]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *Camara v. Municipal Court*, 387 U.S. 523 (1967) — https://www.courtlistener.com/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/ — pinpoints: 534, 538.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2f38a10b7ceb9d84", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Camara v. Municipal Court"}, "payload": {"all": [{"cite": "387 U.S. 523", "page": "523", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "387"}, {"cite": "87 S. Ct. 1727", "page": "1727", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 930", "page": "930", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1254", "page": "1254", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "387 U.S. 523", "official": {"cite": "387 U.S. 523", "page": "523", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "387"}, "official_selection_present": true, "record_id": "Camara v. Municipal Court"}}
{"assertion_id": "f63f308b2738abb4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-534", "record_id": "Camara v. Municipal Court"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-534", "pinpoint_status": "slip-only", "quote": "such a warrant may issue. ## Rule Administrative inspections require a warrant procedure:", "quote_fidelity": "mismatch", "record_id": "Camara v. Municipal Court", "star_marker": null}}
{"assertion_id": "fd111b2f54df4f87", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-538", "record_id": "Camara v. Municipal Court"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-538", "pinpoint_status": "slip-only", "quote": "'probable cause' to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling.", "quote_fidelity": "mismatch", "record_id": "Camara v. Municipal Court", "star_marker": null}}
{"assertion_id": "b71eb672fd223069", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Camara v. Municipal Court"}, "payload": {"as_of_content": "1967-06-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Camara v. Municipal Court", "scope_note": "Overruled Frank v. Maryland; remains the foundational administrative-warrant case.", "varies_by_point": false}}
```

### lake record — Camara v. Municipal Court

```json
{
  "schema_version": "s2.v1",
  "record_id": "Camara v. Municipal Court",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Camara v. Municipal Court of City and County of San Francisco",
    "case_name_short": "Camara",
    "case_name_full": "Camara v. Municipal Court of the City and County of San Francisco",
    "input_case_name": "Camara v. Municipal Court",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-05",
    "year": 1967,
    "docket": "92",
    "cluster_id": 107473,
    "lead_opinion_id": 107473,
    "sibling_ids": [
      107473
    ],
    "absolute_url": "/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "387 U.S. 523",
      "volume": "387",
      "reporter": "U.S.",
      "page": "523",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1727",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 930",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "930",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1254",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1254",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "387 U.S. 523",
        "volume": "387",
        "reporter": "U.S.",
        "page": "523",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1727",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 930",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "930",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1254",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1254",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "387 U.S. 523",
    "official_selection": {
      "court_class": "scotus",
      "selected": "387 U.S. 523",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-534",
      "page": null,
      "quote": "such a warrant may issue. ## Rule Administrative inspections require a warrant procedure:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-538",
      "page": null,
      "quote": "'probable cause' to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Camara v. Municipal Court",
    "varies_by_point": false,
    "scope_note": "Overruled Frank v. Maryland; remains the foundational administrative-warrant case.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. O'Donnell",
          "cluster_id": 4427767,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
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
        "journal_ref": "Camara v. Municipal Court:lane1_negative"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
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
        "journal_ref": "Camara v. Municipal Court:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107473) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDUyMTI0ODAwMDAwJnM9MzE2Nzk5OSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107473%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(107473)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjM5JnM9MTEyNDcyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107473%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107473)",
        "reviewed": 56,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 56,
        "triage_read": 0,
        "triage_snippet_classified": 56
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107473)",
    "indexed_citing_opinions": 2314,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107473,
        "count": 2314,
        "count_source": "search"
      }
    ],
    "citation_count": 3595,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/camara-v-municipal-court.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNjI4NTUmcz0xMDI2NTcxNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107473%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107473,
        "cited_id": 95698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 96230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 96902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 1306345,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 1334923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2008391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2049948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2062881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2155771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2305304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2430498,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 2435050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 3620827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 3783238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 5521228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107473,
        "cited_id": 9442232,
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
    "date_created": "2026-07-04T23:26:45Z",
    "date_modified": "2026-07-06T07:29:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:28:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:26:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Camara v. Municipal Court

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b569-2">
<span citation-index="1" class="star-pagination" label="525"> 
   *525
   </span>
  Mr. Justice White
 </author>
<p id="AnHt">
  delivered the opinion of the Court.
 </p>
<p id="b569-3">
  In
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span>, this Court upheld, by a five-to-four vote, a state court conviction of a homeowner who refused to permit a municipal health inspector to enter and inspect his premises without a search warrant. In
  <em>
   Eaton
  </em>
  v.
  <em>
   Price,
  </em>
  <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263</a></span>, a similar conviction was affirmed by an equally divided Court. Since those closely divided decisions, more intensive efforts at all levels of government to contain and eliminate urban blight have led to increasing use of such inspection techniques, while numerous decisions of this Court have more fully defined the Fourth Amendment's effect on state and municipal action.
  <em>
   E. g., Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>;
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>. In view of the growing nationwide importance of the problem, we noted probable jurisdiction in this case and in
  <em>
   See
  </em>
  v.
  <em>
   City of Seattle, post,
  </em>
  p. 541, to re-examine whether administrative inspection programs, as presently authorized and conducted, violate Fourth Amendment rights as those rights are enforced against the States through the Fourteenth Amendment. <span class="citation multiple-matches"><a href="/c/U.%20S./385/808/">385 U. S. 808</a></span>.
 </p>
<p id="b569-4">
  Appellant brought this action in a California Superior Court alleging that he was awaiting trial on a criminal charge of violating the San Francisco Housing Code by refusing to permit a warrantless inspection of his residence, and that a writ of prohibition should issue to the criminal court because the ordinance authorizing such inspections is unconstitutional on its face. The Superior Court denied the writ, the District Court of Appeal affirmed, and the Supreme Court of California denied a petition for hearing. Appellant properly raised and had considered by the California courts the federal constitutional questions he now presents to this Court.
 </p>
<p id="b569-5">
  Though there were no judicial findings of fact in this prohibition proceeding, we shall set forth the parties’ factual allegations. On November 6, 1963, an inspector
  <span citation-index="1" class="star-pagination" label="526"> 
   *526
   </span>
  of the Division of Housing Inspection of the San Francisco Department of Public Health entered an apartment building to make a routine annual inspection for possible violations of the city's Housing Code.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The building’s manager informed the inspector that appellant, lessee of the ground floor, was using the rear of his leasehold as a personal residence. Claiming that the building’s occupancy permit did not allow residential use of the ground floor, the inspector confronted appellant and demanded that he permit an inspection of the premises. Appellant refused to allow the inspection because the inspector lacked a search warrant.
 </p>
<p id="b570-6">
  The inspector returned on November 8, again without a warrant, and appellant again refused to allow an inspection. ' A citation was then mailed ordering appellant to appear at the district attorney’s office. When appellant failed to appear, two inspectors returned to his apartment on November 22. They informed appellant that he was required by law to permit an inspection under § 503 of the Housing Code:
 </p>
<blockquote id="b570-7">
  “Sec. 503 Right to Enter Building. Authorized employees of the City departments or City agencies, so far as may be necessary for the performance of their duties, shall, upon presentation of proper credentials, have the right to enter, at reasonable times, any building, structure, or premises in the City to perform any duty imposed upon them by the Municipal Code.”
 </blockquote>
<p id="b571-4">
<span citation-index="1" class="star-pagination" label="527"> 
   *527
   </span>
  Appellant nevertheless refused the inspectors access to his apartment without a search warrant. Thereafter, a complaint was filed charging him with refusing to permit a lawful inspection in violation of § 507 of the Code.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Appellant was arrested on December 2 and released on bail. When his demurrer to the criminal complaint was denied, appellant filed this petition for a writ of prohibition.
 </p>
<p id="b571-5">
  Appellant has argued throughout this litigation that § 503 is contrary to the Fourth and Fourteenth Amendments in that it authorizes municipal officials to enter a private dwelling without a search warrant and without probable cause to believe that a violation of the Housing Code exists therein. Consequently, appellant contends, he may not be prosecuted under § 507 for refusing to permit an inspection unconstitutionally authorized by § 503. Relying on
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland, Eaton
  </em>
  v.
  <em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price</a></span>,
  </em>
  and decisions in other States,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  the District
  <span citation-index="1" class="star-pagination" label="528"> 
   *528
   </span>
  Court of Appeal held that § 503 does not violate Fourth Amendment rights because it “is part of a regulatory scheme which is essentially civil rather than criminal in nature, inasmuch as that section creates a right of inspection which is limited in scope and may not be exercised under unreasonable conditions.” Having concluded that
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>,
  </em>
  to the extent that it sanctioned such warrantless inspections, must be overruled, we reverse.
 </p>
<p id="b572-5">
  I.
 </p>
<p id="b572-6">
  The Fourth Amendment provides that, “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” The basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials. The Fourth Amendment thus gives concrete expression to a right of the people which “is basic to a free society.”
  <em>
   Wolf
  </em>
  v.
  <em>
   Colorado,
  </em>
  <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>. As such, the Fourth Amendment is enforceable against the States through the Fourteenth Amendment.
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30</a></span>.
 </p>
<p id="b572-7">
  Though there has been general agreement as to the fundamental purpose of the Fourth Amendment, translation of the abstract prohibition against “unreasonable searches and seizures” into workable guidelines for the decision of particular cases is a difficult task which has for many years divided the members of this Court. Nevertheless, one governing principle, justified by history and by current experience, has consistently been followed: except in certain carefully defined classes of cases, a search of private property without proper con
  <span citation-index="1" class="star-pagination" label="529"> 
   *529
   </span>
  sent is “unreasonable” unless it has been authorized by a valid search warrant. See,
  <em>
   e. g., Stoner
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Jeffers,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>;
  <em>
   McDonald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>. As the Court explained in
  <em>
   Johnson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 14:
 </p>
<blockquote id="b573-5">
  “The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.”
 </blockquote>
<p id="b573-6">
  In
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>,
  </em>
  this Court upheld the conviction of one who refused to permit a warrantless inspection of private premises for the purposes of locating and abating a suspected public nuisance. Although
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  can arguably be distinguished from this case on its facts,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  opinion has generally been interpreted as carving out an additional exception to the rule that warrantless searches are unreasonable under the Fourth Amendment. See
  <em>
   Eaton
  </em>
  v.
  <em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price, supra.</a></span>
  </em>
  The District Court of Appeal so interpreted
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  in this case, and that ruling is the core of appellant’s challenge here. We proceed to a re-examination of the factors which
  <span citation-index="1" class="star-pagination" label="530"> 
   *530
   </span>
  persuaded the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority to adopt this construction of the Fourth Amendment’s prohibition against unreasonable searches.
 </p>
<p id="b574-5">
  To the
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority, municipal fire, health, and housing inspection programs “touch at most upon the periphery of the important interests safeguarded by the Fourteenth Amendment’s protection against official intrusion,” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367</a></span>, because the inspections are merely to determine whether physical conditions exist which do not comply with minimum standards prescribed in local regulatory ordinances. Since the inspector does not ask that the property owner open his doors to a search for “evidence of criminal action” which may be used to secure the owner’s criminal conviction, historic interests of “self-protection” jointly protected by the Fourth and Fifth Amendments
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  are said not to be involved, but only the less intense “right to be secure from intrusion into personal privacy.”
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#365" aria-description="Citation for case: Frank v. Maryland"><em>
   Id.,
  </em>
  at 365</a></span>.
 </p>
<p id="b574-6">
  We may agree that a routine inspection of the physical condition of private property is a less hostile intrusion than the typical policeman’s search for the fruits and instrumentalities of crime. For this reason alone,
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  differed from the great bulk of Fourth Amendment cases which have been considered by this Court. But we cannot agree that the Fourth Amendment interests at stake in these inspection cases are merely “peripheral.”. It is surely anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  For instance, even the most law-abiding citi
  <span citation-index="1" class="star-pagination" label="531"> 
   *531
   </span>
  zen. has a very tangible interest in limiting the circumstances under which the sanctity of his home may be broken by official authority, for the possibility of criminal entry under the guise of official sanction is a serious threat to personal and family security. And even accepting
  <em>
   Frank’s
  </em>
  rather remarkable premise, inspections of the kind we are here considering do in fact jeopardize “self-protection” interests of the property owner. Like most regulatory laws, fire, health, and housing codes are enforced by criminal processes. In some cities, discovery of a violation by the inspector leads to a criminal complaint.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  Even in cities where discovery of a violation produces only an administrative compliance order,
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  refusal to comply is a criminal offense, and the fact of compliance is verified by a second inspection, again without a warrant.
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  Finally, as this case demonstrates, refusal to permit an inspection is itself a crime, punishable by fine or even by jail sentence.
 </p>
<p id="b575-4">
  The
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority suggested, and appellee reasserts, two other justifications for permitting administrative health and safety inspections without a warrant. First, it is argued that these inspections are “designed to make the least possible demand on the individual occupant.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367</a></span>. The ordinances authorizing inspections are hedged with safeguards, and at any rate the inspector’s particular decision to enter must comply with the constitutional standard of reasonableness even if -he may enter without a warrant.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  In addition, the argument
  <span citation-index="1" class="star-pagination" label="532"> 
   *532
   </span>
  proceeds, the warrant process could not function effectively in this field. The decision to inspect an entire municipal area is based upon legislative or administrative assessment of broad factors such as the area’s age and condition. Unless the magistrate is to review such policy matters, he must issue a “rubber stamp” warrant which provides no protection at all to the property owner.
 </p>
<p id="b576-6">
  In our opinion, these arguments unduly discount the purposes behind the warrant machinery contemplated by the Fourth Amendment. Under the present system, when the inspector demands entry, the occupant has no way of knowing whether enforcement of the municipal code involved requires inspection of his premises, no way of knowing the lawful limits of the inspector’s power to search, and no way of knowing whether the inspector himself is acting under proper authorization. These are questions which may be reviewed by a neutral magistrate without any reassessment of the basic agency decision to canvass an area. Yet, only by refusing entry and risking a criminal conviction can the occupant at present challenge the inspector’s decision to search. And even if the occupant possesses sufficient fortitude to take this risk, as appellant did here, he may never learn any more about the reason for the inspection than that the law generally allows housing inspectors to gain entry. The practical effect of this system is to leave the occupant subject to the discretion of the official in the field. This is precisely the discretion to invade private property which we have consistently circumscribed by a requirement that a disinterested party warrant the need to
  <span citation-index="1" class="star-pagination" label="533"> 
   *533
   </span>
  search. See cases cited, p. 529,
  <em>
   supra.
  </em>
  We simply cannot say that the protections provided by the warrant procedure are not needed in this context; broad statutory safeguards are no substitute for individualized review, particularly when those safeguards may only be invoked at the risk of a criminal penalty.
 </p>
<p id="b577-5">
  The final justification suggested for warrantless administrative searches is that the public interest demands such a rule: it is vigorously argued that the health and safety of entire urban populations is dependent upon enforcement of minimum fire, housing, and sanitation standards, and that the only effective means of enforcing such codes is by routine systematized inspection of all physical structures. Of course, in applying any reasonableness standard, including one of constitutional dimension, an argument that the public interest demands a particular rule must receive careful consideration. But we think this argument misses the mark. The question is not, at this stage at least, whether these inspections may be made, but whether they may be made without a warrant. For example, to say that gambling raids may not be made at the discretion of the police without a warrant is not necessarily to say that gambling raids may never be made. In assessing whether the public interest demands creation of a general exception to the Fourth Amendment’s warrant requirement, the question is not whether the public interest justifies the type of search in question, but whether the authority to search should be evidenced by a warrant, which in turn depends in part upon whether the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search. See
  <em>
   Schmerber
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span>. It has nowhere been urged that fire, health, and housing code inspection programs could not achieve their goals within the confines of a reasonable search warrant requirement. Thus, we do not find the public need argument dispositive.
 </p>
<p id="b578-3">
<span citation-index="1" class="star-pagination" label="534"> 
   *534
   </span>
  In summary, we hold that administrative searches of the kind at issue here are significant intrusions upon the interests protected by the Fourth Amendment, that such searches when authorized and conducted without a warrant procedure lack the traditional safeguards which the Fourth Amendment guarantees to the individual, and that the reasons put forth in
  <em>
   Frank
  </em>
  v.
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span>
  </em>
  and in other cases for upholding these warrantless searches are insufficient to justify so substantial a weakening of the Fourth Amendment’s protections. Because of the nature of the municipal programs under consideration, however, these conclusions must be the beginning, not the end, of our inquiry. The
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  majority gave recognition to the unique character of these inspection programs by refusing to require search warrants; to reject that disposition does not justify ignoring the question whether some other accommodation between public need and individual rights is essential.
 </p>
<p id="b578-4">
  II.
 </p>
<p id="b578-5">
  The Fourth Amendment provides that, “no Warrants shall issue, but upon probable cause.” Borrowing from more typical Fourth Amendment cases, appellant argues not only that code enforcement inspection programs must be circumscribed by a warrant procedure, but also that warrants should issue only when the inspector possesses probable cause to believe that a particular dwelling contains violations of the minimum standards prescribed by the code being enforced. We disagree.
 </p>
<p id="b578-6">
  In cases in which the Fourth Amendment requires that a warrant to search be obtained, “probable cause” is the standard by which a particular decision to search is tested against the constitutional mandate of reasonableness. To apply this standard, it is obviously necessary first to focus upon the governmental interest which allegedly justifies official intrusion upon the constitutionally pro
  <span citation-index="1" class="star-pagination" label="535"> 
   *535
   </span>
  tected interests of the private citizen. Por example, in a criminal investigation, the police may undertake to recover specific stolen or contraband goods. But that public interest would hardly justify a sweeping search of an entire city conducted in the hope that these goods might be found. Consequently, a search for these goods, even with a warrant, is “reasonable” only when there is “probable cause” to believe that they will be uncovered in a particular dwelling.
 </p>
<p id="b579-5">
  Unlike the search pursuant to a criminal investigation, the inspection programs at issue here are aimed at securing city-wide compliance with minimum physical standards for private property. The primary governmental interest at stake is to prevent even the unintentional development of conditions which are hazardous to public health and safety. Because fires and epidemics may ravage large urban areas, because unsightly conditions adversely affect the economic values of neighboring structures, numerous courts have upheld the police power of municipalities to impose and enforce such minimum standards even upon existing structures.
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
  In determining whether a particular inspection is reasonable — and thus in determining whether there is probable cause to issue a warrant for that inspection — the need for the inspection must be weighed in terms of these reasonable goals of code enforcement.
 </p>
<p id="b579-6">
  There is unanimous agreement among those most familiar with this field that the only effective way to seek universal compliance with the minimum standards required by municipal codes is through routine periodic
  <span citation-index="1" class="star-pagination" label="536"> 
   *536
   </span>
  inspections of all structures.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  It is here that the probable cause debate is focused, for the agency’s decision to conduct an area inspection is unavoidably based on its appraisal of conditions in the area as a whole, not on its knowledge of conditions in each particular building. Appellee contends that, if the probable cause standard urged by appellant is adopted, the area inspection will be eliminated as a means of seeking compliance with code standards and the reasonable goals of code enforcement will be dealt a crushing blow.
 </p>
<p id="b580-6">
  In meeting this contention, appellant argues first, that his probable cause standard would not jeopardize area inspection programs because only a minute portion of the population will refuse to consent to such inspections, and second, that individual privacy in any event should be given preference to the public interest in conducting such inspections. The first argument, even if true, is irrelevant to the question whether the area inspection is reasonable within the meaning of the Fourth Amendment. The second argument is in effect an assertion that the area inspection is an unreasonable search. Unfortunately, there can be no ready test for determining reasonableness
  <span citation-index="1" class="star-pagination" label="537"> 
   *537
   </span>
  other than by balancing the need to search against the invasion which the search entails. But we think that a number of persuasive factors combine to support the reasonableness of area code-enforcement inspections. First, such programs have a long history of judicial and public acceptance. See
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#367" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 367-371</a></span>. Second, the public interest demands that all dangerous conditions be prevented or abated, yet it is doubtful that any other canvassing technique would achieve acceptable results. Many such conditions— faulty wiring is an obvious example — are not observable from outside the building and indeed may not be apparent to the inexpert occupant himself. Finally, because the inspections are neither personal in nature nor aimed at the discovery of evidence of crime, they involve a relatively limited invasion of the urban citizen’s privacy. Both the majority and the dissent in
  <em>
   <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
  </em>
  emphatically supported this conclusion:
 </p>
<blockquote id="b581-5">
  “Time and experience have forcefully taught that the power to inspect dwelling places, either as a matter of systematic area-by-area search or, as here, to treat a specific problem, is of indispensable importance to the maintenance of community health; a power that would be greatly hobbled by the blanket requirement of the safeguards necessary for a search of evidence of criminal acts. The need for preventive action is great, and city after city has seen this need and granted the power of inspection to its health officials; and these inspections are apparently welcomed by all but an insignificant few. Certainly, the nature of our society has not vitiated the need for inspections first thought necessary 158 years ago, nor has experience revealed any abuse or inroad on freedom in meeting this need by means that history and dominant public opinion have sanctioned.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#372" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 372</a></span>.
 </blockquote>
<blockquote id="b582-5">
<span citation-index="1" class="star-pagination" label="538"> 
   *538
   </span>
  . . This is not to suggest that a health official need show the same kind of proof to a magistrate to obtain a warrant as one must who would search for the fruits or instrumentalities of crime. Where considerations of health and safety are involved, the facts that would justify an inference of 'probable cause’ to make an inspection are clearly different from those that would justify such an inference where a criminal investigation has been undertaken. Experience may show the need for periodic inspections of certain facilities without a further showing of cause to believe that substandard conditions dangerous to the public are being maintained. The passage of a certain period without inspection might of itself be sufficient in a given situation to justify the issuance of a warrant. The test of 'probable cause’ required by the Fourth Amendment can take into account the nature of the search that is being sought.” <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#383" aria-description="Citation for case: Frank v. Maryland">359 U. S., at 383</a></span> (Mr. Justice Douglas, dissenting).
 </blockquote>
<p id="b582-6">
  Having concluded that the area inspection is a “reasonable” search of private property within the meaning of the Fourth Amendment, it is obvious that “probable cause” to issue a warrant to inspect must exist if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling. Such standards, which will vary with the municipal program being enforced, may be based upon the passage of time, the nature of the building
  <em>
   (e. g.,
  </em>
  a multi-family apartment house), or the condition of the entire area, but they will not necessarily depend upon specific knowledge of the condition of the particular dwelling. It has been suggested that so to vary the probable cause test from the standard applied in criminal cases would be to authorize a “synthetic search warrant” and thereby to lessen the overall protections of the Fourth Amendment.
  <em>
   Frank
  </em>
  v.
  <em>
   Maryland,
  </em>
  359
  <span citation-index="1" class="star-pagination" label="539"> 
   *539
   </span>
  U. S., at 373. But we do not agree. The warrant procedure is designed to guarantee that a decision to search private property is justified by a reasonable governmental interest. But reasonableness is still the ultimate standard. If a valid public interest justifies the intrusion contemplated, then there is probable cause to issue a suitably restricted search warrant. Cf.
  <em>
   Oklahoma Press Pub. Co.
  </em>
  v.
  <em>
   Walling,
  </em>
  <span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186</a></span>. Such an approach neither endangers time-honored doctrines applicable to criminal investigations nor makes a nullity of the probable cause requirement in this area. It merely gives full recognition to the competing public and private interests here at stake and, in so doing, best fulfills the historic purpose behind the constitutional right to be free from unreasonable government invasions of privacy. See
  <em>
   Eaton
  </em>
  v.
  <em>
   Price,
  </em>
  <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#273" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S., at 273-274</a></span> (opinion of Mr. Justice Brennan).
 </p>
<p id="b583-5">
  III.
 </p>
<p id="b583-6">
  Since our holding emphasizes the controlling standard of reasonableness, nothing we say today is intended to foreclose prompt inspections, even without a warrant, that the law has traditionally upheld in emergency situations. See
  <em>
   North American Cold Storage Co.
  </em>
  v.
  <em>
   City of Chicago,
  </em>
  <span class="citation" data-id="96902"><a href="/opinion/96902/north-american-cold-storage-co-v-city-of-chicago/" aria-description="Citation for case: North American Cold Storage Co. v. City of Chicago">211 U. S. 306</a></span> (seizure of unwholesome food);
  <em>
   Jacobson
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="96230"><a href="/opinion/96230/jacobson-v-massachusetts/" aria-description="Citation for case: Jacobson v. Massachusetts">197 U. S. 11</a></span> (compulsory smallpox vaccination);
  <em>
   Compagnie Francaise
  </em>
  v.
  <em>
   Board of Health,
  </em>
  <span class="citation" data-id="9417887"><a href="/opinion/95698/compagnie-francaise-de-navigation-a-vapeur-v-louisiana-state-board-of/" aria-description="Citation for case: Compagnie Francaise De Navigation a Vapeur v. Louisiana...">186 U. S. 380</a></span> (health quarantine);
  <em>
   Kroplin
  </em>
  v.
  <em>
   Truax,
  </em>
  <span class="citation" data-id="3783238"><a href="/opinion/4026648/kroplin-v-truax/" aria-description="Citation for case: Kroplin v. Truax">119 Ohio St. 610</a></span>, <span class="citation" data-id="3783238"><a href="/opinion/4026648/kroplin-v-truax/" aria-description="Citation for case: Kroplin v. Truax">165 N. E. 498</a></span> (summary destruction of tubercular cattle). On the other hand, in the .case of most routine area inspections, there is no compelling urgency to inspect at a particular time or on a particular day. Moreover, most citizens allow inspections of their property without a warrant. Thus, as a practical matter and in light of the Fourth Amendment’s requirement that a warrant specify the property to be searched, it seems likely that warrants should normally be sought only after entry is refused unless
  <span citation-index="1" class="star-pagination" label="540"> 
   *540
   </span>
  there has been a citizen complaint or there is other satisfactory reason for securing immediate entry. Similarly, the requirement of a warrant procedure does not suggest any change in what seems to be the prevailing local policy, in most situations, of authorizing entry, but not entry by force, to inspect.
 </p>
<p id="b584-5">
  IV.
 </p>
<p id="b584-6">
  In this case, appellant has been charged with a crime for his refusal to permit housing inspectors to enter his leasehold without a warrant. There was no emergency demanding immediate access; in fact, the inspectors made three trips to the building in an attempt to obtain appellant’s consent to search. Yet no warrant was obtained and thus appellant was unable to verify either the need for or the appropriate limits of the inspection. No doubt, the inspectors entered the public portion of the building with the consent of the landlord, through the building’s manager, but appellee does not contend that such consent was sufficient to authorize inspection of appellant’s premises. Cf.
  <em>
   Stoner
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>;
  <em>
   Chapman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>;
  <em>
   McDonald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>. Assuming the facts to be as the parties have alleged, we therefore conclude that appellant had a constitutional right to insist that the inspectors obtain a warrant to search and that appellant may not constitutionally be convicted for refusing to consent to the inspection. It appears from the opinion of the District Court of Appeal that under these circumstances a writ of prohibition will issue to the criminal court under California law.
 </p>
<p id="b584-7">
  The judgment is vacated and the case is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b584-8">
<em>
   It is so ordered.
  </em>
</p>
<judges id="b584-9">
  [For dissenting opinion of Mr. Justice Clark, see
  <em>
   post,
  </em>
  p. 546.]
 </judges>












<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b570-8">
   The inspection was conducted pursuant to § 86 (3) of the San Francisco Municipal Code, which provides that apartment house operators shall pay an annual license fee in part to defray the cost of periodic inspections of their buildings. The inspections are to be made by the Bureau of Housing Inspection “at least once a year and as often thereafter as may be deemed necessary.” The permit of occupancy, which prescribes the apartment units which a building may contain, is not issued until the license is obtained.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b571-6">
   “Sec. 507 PENALTY FOR Violation. Any person, the owner or his authorized agent who violates, disobeys, omits, neglects, or refuses to comply with, or who resists or opposes the execution of any of the provisions of this Code, or any order of the Superintendent, the Director of Public Works, or the Director of Public Health made pursuant to this Code, shall be guilty of a misdemeanor and upon conviction thereof shall be punished by a fine not exceeding five hundred dollars ($500.00), or by imprisonment, not exceeding six (6) months or by both such fine and imprisonment, unless otherwise provided in this Code, and shall be deemed guilty of a separate offense for every day such violation, disobedience, omission, neglect or refusal shall continue.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b571-7">
<em>
    Givner
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/" aria-description="Citation for case: Givner v. State">210 Md. 484</a></span>, <span class="citation" data-id="2305304"><a href="/opinion/2305304/givner-v-state/" aria-description="Citation for case: Givner v. State">124 A. 2d 764</a></span> (1956);
   <em>
    City of St. Louis
   </em>
   v.
   <em>
    Evans,
   </em>
   <span class="citation" data-id="2435050"><a href="/opinion/2435050/city-of-st-louis-v-evans/" aria-description="Citation for case: City of St. Louis v. Evans">337 S. W. 2d 948</a></span> (Mo. 1960);
   <em>
    State ex rel. Eaton
   </em>
   v.
   <em>
    Pnce,
   </em>
   <span class="citation no-link">168 Ohio St. 123</span>, <span class="citation no-link">151 N. E. 2d 523</span> (1958), aff’d by an equally divided Court, <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263</a></span> (1960). See also
   <em>
    State
   </em>
   v.
   <em>
    Rees,
   </em>
   <span class="citation" data-id="9570716"><a href="/opinion/1306345/state-v-rees/" aria-description="Citation for case: State v. Rees">258 Iowa 813</a></span>, <span class="citation" data-id="9570716"><a href="/opinion/1306345/state-v-rees/" aria-description="Citation for case: State v. Rees">139 N. W. 2d 406</a></span> (1966);
   <em>
    Commonwealth
   </em>
   v.
   <em>
    Hadley,
   </em>
   <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">351 Mass. 439</a></span>, <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">222 N. E. 2d 681</a></span> (1966), appeal docketed Jan. 5, 1967, No. 1179, Misc., O. T. 1966;
   <em>
    People
   </em>
   v.
   <em>
    Laverne,
   </em>
   14 N. Y. 2d 304, <span class="citation" data-id="5521228"><a href="/opinion/5673733/people-v-laverne/" aria-description="Citation for case: People v. Laverne">200 N. E. 2d 441</a></span> (1964).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b573-7">
   In
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>,
   </em>
   the Baltimore ordinance required that the health inspector “have cause to suspect that a nuisance exists in any house, cellar or enclosure” before he could demand entry without a warrant, a requirement obviously met in
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
   </em>
   because the inspector observed extreme structural decay and a pile of rodent feces on the appellant’s premises. Section 503 of the San Francisco Housing Code has no such “cause” requirement, but neither did the Ohio ordinance at issue in
   <em>
    Eaton
   </em>
   v.
   <em>
    <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">Price</a></span>,
   </em>
   a case which four Justices thought was controlled by
   <em>
    Frank.
   </em>
   <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#264" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S., at 264, 265, n. 2</a></span> (opinion of Mr. Justice BrennaN).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b574-7">
   See
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   116 17. S. 616. Compare
   <em>
    Schmerber
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 766-772</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b574-8">
   See
   <em>
    Abel v. United States,
   </em>
   <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#254" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 254-256</a></span> (MR. Justice Brennan, dissenting);
   <em>
    District of Columbia
   </em>
   v.
   <em>
    Little,
   </em>
   85 U. S. App. D. C. 242, <span class="citation" data-id="9442232"><a href="/opinion/223783/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">178 F. 2d 13</a></span>, aff’d, <span class="citation" data-id="104766"><a href="/opinion/104766/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">339 U. S. 1</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b575-5">
   See New York, N. Y., Administrative Code § D26-8.0 (1964).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b575-6">
   See Washington, D. C., Housing Regulations §2104.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b575-7">
   This is the more prevalent enforcement procedure. See Note, Enforcement of Municipal Housing Codes, <span class="citation no-link">78 Harv. L. Rev. 801</span>, 813-816.
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b575-8">
   The San Francisco Code requires that the inspector display-proper credentials, that he inspect “at reasonable times,” and that
   <span citation-index="1" class="star-pagination" label="532"> 
    *532
    </span>
   he not obtain entry by force, at least when there is no emergency. The Baltimore ordinance in
   <em>
    <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span>
   </em>
   required that the inspector “have cause to suspect that a nuisance exists.” Some cities notify residents in advance, by mail or posted notice, of impending area inspections. State courts upholding these inspections without warrants have imposed a general reasonableness requirement. See cases cited, n. 3,
   <em>
    supra.
   </em>
</p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b579-7">
   See
   <em>
    Abbate Bros.
   </em>
   v.
   <em>
    City of Chicago,
   </em>
   <span class="citation" data-id="2049948"><a href="/opinion/2049948/abbate-bros-inc-v-city-of-chicago/" aria-description="Citation for case: Abbate Bros., Inc. v. City of Chicago">11 Ill. 2d 337</a></span>, <span class="citation" data-id="2049948"><a href="/opinion/2049948/abbate-bros-inc-v-city-of-chicago/" aria-description="Citation for case: Abbate Bros., Inc. v. City of Chicago">142 N. E. 2d 691</a></span>;
   <em>
    City of Louisville
   </em>
   v.
   <em>
    Thompson,
   </em>
   <span class="citation" data-id="2430498"><a href="/opinion/2430498/city-of-louisville-v-thompson/" aria-description="Citation for case: City of Louisville v. Thompson">339 S. W. 2d 869</a></span> (Ky.) ;
   <em>
    Adamec
   </em>
   v.
   <em>
    Post,
   </em>
   <span class="citation" data-id="3620827"><a href="/opinion/3637215/adamec-v-post/" aria-description="Citation for case: Adamec v. Post">273 N. Y. 250</a></span>, <span class="citation" data-id="3620827"><a href="/opinion/3637215/adamec-v-post/" aria-description="Citation for case: Adamec v. Post">7 N. E. 2d 120</a></span>;
   <em>
    Paquette
   </em>
   v.
   <em>
    City of Fall River,
   </em>
   <span class="citation" data-id="2062881"><a href="/opinion/2062881/paquette-v-city-of-fall-river/" aria-description="Citation for case: Paquette v. City of Fall River">338 Mass. 368</a></span>, <span class="citation" data-id="2062881"><a href="/opinion/2062881/paquette-v-city-of-fall-river/" aria-description="Citation for case: Paquette v. City of Fall River">155 N. E. 2d 775</a></span>;
   <em>
    Richards
   </em>
   v.
   <em>
    City of Columbia,
   </em>
   227 S. C. 538, <span class="citation" data-id="9585880"><a href="/opinion/1334923/richards-v-city-of-columbia/" aria-description="Citation for case: Richards v. City of Columbia">88 S. E. 2d 683</a></span>;
   <em>
    Boden
   </em>
   v.
   <em>
    City of Milwaukee,
   </em>
   <span class="citation" data-id="2155771"><a href="/opinion/2155771/boden-v-city-of-milwaukee/" aria-description="Citation for case: Boden v. City of Milwaukee">8 Wis. 2d 318</a></span>, <span class="citation" data-id="2155771"><a href="/opinion/2155771/boden-v-city-of-milwaukee/" aria-description="Citation for case: Boden v. City of Milwaukee">99 N. W. 2d 156</a></span>.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b580-7">
   See Osgood &amp; Zwerner, Rehabilitation and Conservation, 25 Law &amp; Contemp. Prob. 705, 718 and n. 43; Schwartz, Crucial Areas in Administrative Law, <span class="citation no-link">34 Geo. Wash. L. Rev. 401</span>, 423 and n. 93; Comment, Rent Withholding and the Improvement of Substandard Housing, <span class="citation no-link">53 Calif. L. Rev. 304</span>, 316-317; Note, Enforcement of Municipal Housing Codes, <span class="citation no-link">78 Harv. L. Rev. 801</span>, 807, 851; Note, Municipal Housing Codes, <span class="citation no-link">69 Harv. L. Rev. 1115</span>, 1124-1125. Section 311 (a) of the Housing and Urban Development Act of 1965, <span class="citation no-link">79 Stat. 478</span>, <span class="citation no-link">42 U. S. C. § 1468</span> (1964 ed., Supp. I), authorizes grants of federal funds “to cities, other municipalities, and counties for the purpose of assisting such localities in carrying out programs of concentrated code enforcement in deteriorated or deteriorating areas in which such enforcement, together with those public improvements to be provided by the locality, may be expected to arrest the decline of the area.”
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Caniglia v. Strom.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Caniglia v. Strom"
type: case
citation: "593 U.S. 194 (2021)"
parallel_cite: "209 L. Ed. 2d 604; 141 S. Ct. 1596"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-05-17
docket: 20-157
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-05-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Caniglia v. Strom
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4883694/caniglia-v-strom/"
  cluster_id: 4883694
  opinion_id: 4687473
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Progeny / Refinement"
related: ["[[Cady v. Dombrowski]]", "[[Brigham City v. Stuart]]", "[[Kentucky v. King]]"]
aliases: []
tags: ["case", "fourth-amendment", "community-caretaking", "home", "warrantless-entry"]
holding: "There is NO freestanding 'community caretaking' exception authorizing warrantless entry into the HOME. Cady's caretaking rationale was…"
lake:
  record_id: Caniglia v. Strom
  status: verified
  projected_at: 2026-07-06
---

# Caniglia v. Strom

*593 U.S. 194 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a marital argument in which Caniglia melodramatically suggested his wife shoot him, she spent the night elsewhere and, unable to reach him the next day, asked police for a welfare check. Officers, concerned he was suicidal, persuaded him to go for a psychiatric evaluation and then — without a warrant or his consent — entered his home and seized his firearms. The First Circuit upheld the entry under a freestanding "community caretaking" exception drawn from *[[Cady v. Dombrowski]]*.

## Issue
Whether the community-caretaking rationale of *[[Cady v. Dombrowski]]* creates a standalone exception authorizing warrantless entry into and seizures within the home.

## Rule
There is no such freestanding exception: "The First Circuit's 'community caretaking' rule, however, goes beyond anything this Court has recognized." — *Caniglia v. Strom*, 593 U.S. 194 (2021) (slip op., at 3). ^pin-op3

*[[Cady v. Dombrowski|Cady]]* does not support extending caretaking to the home: "Neither the holding nor logic of *Cady* justified that approach. True, *Cady* also involved a warrantless search for a firearm. But the location of that search was an impounded vehicle — not a home — 'a constitutional difference' that the opinion repeatedly stressed." — *Id.* (slip op., at 4). ^pin-op4

## Application
The officers entered Caniglia's home and seized his firearms with no warrant, no consent, and — as the case came up — no recognized [[Exigent Circumstances and Hot Pursuit|exigency]], relying solely on a freestanding caretaking theory. Because *[[Cady v. Dombrowski|Cady]]* concerned an impounded vehicle rather than a home, its caretaking rationale did not authorize this warrantless entry into Caniglia's house.

## Conclusion
There is no standalone community-caretaking exception for the home; the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Caniglia* **cabins** [[Cady v. Dombrowski]] to the vehicle context and leaves intact the home-entry exceptions of [[Emergency Aid|emergency aid]] and [[Exigent Circumstances and Hot Pursuit|exigency]] ([[Brigham City v. Stuart]]; [[Kentucky v. King]]).

## Appears on
- [[Emergency Aid]] — *Key — Progeny / Refinement*

## Sources
- *Caniglia v. Strom*, 593 U.S. 194 (2021) — https://www.courtlistener.com/opinion/4883694/caniglia-v-strom/ — pinpoints: slip op., at 3, 4 (CL carries the slip opinion; cluster 4883694 → opinion 4687473).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5ad08ba2a1dddf5b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Caniglia v. Strom"}, "payload": {"all": [{"cite": "593 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "593"}, {"cite": "209 L. Ed. 2d 604", "page": "604", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "209"}, {"cite": "141 S. Ct. 1596", "page": "1596", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}], "display": "593 U.S. 194", "official": {"cite": "593 U.S. 194", "page": "194", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "593"}, "official_selection_present": true, "record_id": "Caniglia v. Strom"}}
{"assertion_id": "3a0b456f2405eba8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op3", "record_id": "Caniglia v. Strom"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op3", "pinpoint_status": "slip-only", "quote": "exception drawn from *Cady v. Dombrowski*. ## Issue Whether the community-caretaking rationale of *Cady v. Dombrowski* creates a standalone exception authorizing warrantless entry into and seizures within the home. ## Rule There is no such freestanding exception:", "quote_fidelity": "mismatch", "record_id": "Caniglia v. Strom", "star_marker": null}}
{"assertion_id": "5efdcbbb748ab7e2", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op4", "record_id": "Caniglia v. Strom"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op4", "pinpoint_status": "slip-only", "quote": "Neither the holding nor logic of *Cady* justified that approach. True, *Cady* also involved a warrantless search for a firearm. But the location of that search was an impounded vehicle — not a home — 'a constitutional difference' that the opinion repeatedly stressed.", "quote_fidelity": "mismatch", "record_id": "Caniglia v. Strom", "star_marker": null}}
{"assertion_id": "c25d009a536217eb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Caniglia v. Strom"}, "payload": {"as_of_content": "2021-05-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Caniglia v. Strom", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Caniglia v. Strom

```json
{
  "schema_version": "s2.v1",
  "record_id": "Caniglia v. Strom",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Caniglia v. Strom",
    "case_name_short": "Caniglia",
    "case_name_full": "",
    "input_case_name": "Caniglia v. Strom",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-05-17",
    "year": 2021,
    "docket": "20-157",
    "cluster_id": 4883694,
    "lead_opinion_id": 4687473,
    "sibling_ids": [
      4687473
    ],
    "absolute_url": "/opinion/4883694/caniglia-v-strom/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "593 U.S. 194",
      "volume": "593",
      "reporter": "U.S.",
      "page": "194",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "209 L. Ed. 2d 604",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 1596",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "593 U.S. 194",
        "volume": "593",
        "reporter": "U.S.",
        "page": "194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 604",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "604",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 1596",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "593 U.S. 194",
    "official_selection": {
      "court_class": "scotus",
      "selected": "593 U.S. 194",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op3",
      "page": null,
      "quote": "exception drawn from *Cady v. Dombrowski*. ## Issue Whether the community-caretaking rationale of *Cady v. Dombrowski* creates a standalone exception authorizing warrantless entry into and seizures within the home. ## Rule There is no such freestanding exception:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op4",
      "page": null,
      "quote": "Neither the holding nor logic of *Cady* justified that approach. True, *Cady* also involved a warrantless search for a firearm. But the location of that search was an impounded vehicle \u2014 not a home \u2014 'a constitutional difference' that the opinion repeatedly stressed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-05-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Caniglia v. Strom",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
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
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teresa Graham v. Shannon Barnette",
          "cluster_id": 4900401,
          "cite": [
            "5 F.4th 872"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aljohani",
          "cluster_id": 6478244,
          "cite": [
            "463 Ill. Dec. 764",
            "211 N.E.3d 325",
            "2022 IL 127037"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany J. Buckley v. Hennepin County",
          "cluster_id": 4957820,
          "cite": [
            "9 F.4th 757"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
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
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell Taylor",
          "cluster_id": 9386597,
          "cite": [
            "63 F.4th 637"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Sanders",
          "cluster_id": 4900399,
          "cite": [
            "4 F.4th 672"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hagestedt",
          "cluster_id": 10328364,
          "cite": [
            "2025 IL 130286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guerrero",
          "cluster_id": 5303613,
          "cite": [
            "19 F.4th 547"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaron Howard Morgan",
          "cluster_id": 9409483,
          "cite": [
            "71 F.4th 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Clemons v. John Couch",
          "cluster_id": 4898166,
          "cite": [
            "3 F.4th 897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bakutis v. Dean",
          "cluster_id": 10339329,
          "cite": [
            "129 F.4th 299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. W. Case",
          "cluster_id": 10032858,
          "cite": [
            "553 P.3d 985",
            "417 Mont. 354",
            "2024 MT 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Edgin, M.",
          "cluster_id": 10316123,
          "cite": [
            "273 A.3d 573",
            "2022 Pa. Super. 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Giambro",
          "cluster_id": 10314463,
          "cite": [
            "126 F.4th 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Grassrope",
          "cluster_id": 9508066,
          "cite": [
            "970 N.W.2d 558",
            "2022 S.D. 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tidwell v. State",
          "cluster_id": 10367697,
          "cite": [
            "863 S.E.2d 127",
            "312 Ga. 459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tran",
          "cluster_id": 9479664,
          "cite": [
            "545 P.3d 248",
            "2024 UT 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Antoine Maxwell",
          "cluster_id": 9455466,
          "cite": [
            "89 F.4th 671"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alexander Treisman",
          "cluster_id": 9409277,
          "cite": [
            "71 F.4th 225"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Delaware v. McKenzie S. Beasley",
          "cluster_id": 10876355,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Caniglia v. Strom:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4687473) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 0,
        "triage_snippet_classified": 52
      },
      "lane2_top_cited": {
        "query": "cites:(4687473)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTAwODg2MzYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284687473%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4687473)",
        "reviewed": 27,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 27,
        "triage_read": 0,
        "triage_snippet_classified": 27
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4687473)",
    "indexed_citing_opinions": 62,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4687473,
        "count": 62,
        "count_source": "search"
      }
    ],
    "citation_count": 154,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/caniglia-v-strom.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNjU3NSZzPTk0MTUwODUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%284687473%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4687473,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 110067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 856347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 858288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 2801435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 4516423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9413217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9422640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9423434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9424643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9425411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9426490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9429413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9431979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9432531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9434949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9441559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4687473,
        "cited_id": 9842006,
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
    "date_created": "2026-07-04T23:28:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:32:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:29:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Caniglia v. Strom

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

                      CANIGLIA v. STROM ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIRST CIRCUIT

      No. 20–157.      Argued March 24, 2021—Decided May 17, 2021
During an argument with his wife, petitioner Edward Caniglia placed a
 handgun on the dining room table and asked his wife to “shoot [him]
 and get it over with.” His wife instead left the home and spent the
 night at a hotel. The next morning, she was unable to reach her hus-
 band by phone, so she called the police to request a welfare check. The
 responding officers accompanied Caniglia’s wife to the home, where
 they encountered Caniglia on the porch. The officers called an ambu-
 lance based on the belief that Caniglia posed a risk to himself or others.
 Caniglia agreed to go to the hospital for a psychiatric evaluation on the
 condition that the officers not confiscate his firearms. But once
 Caniglia left, the officers located and seized his weapons. Caniglia
 sued, claiming that the officers had entered his home and seized him
 and his firearms without a warrant in violation of the Fourth Amend-
 ment. The District Court granted summary judgment to the officers.
 The First Circuit affirmed, extrapolating from the Court’s decision in
 Cady v. Dombrowski, 413 U. S. 433, a theory that the officers’ removal
 of Caniglia and his firearms from his home was justified by a “commu-
 nity caretaking exception” to the warrant requirement.
Held: Neither the holding nor logic of Cady justifies such warrantless
 searches and seizures in the home. Cady held that a warrantless
 search of an impounded vehicle for an unsecured firearm did not vio-
 late the Fourth Amendment. In reaching this conclusion, the Court
 noted that the officers who patrol the “public highways” are often
 called to discharge noncriminal “community caretaking functions,”
 such as responding to disabled vehicles or investigating accidents. 413
 U. S., at 441. But searches of vehicles and homes are constitutionally
 different, as the Cady opinion repeatedly stressed. Id., at 439, 440–
 442. The very core of the Fourth Amendment’s guarantee is the right
2                          CANIGLIA v. STROM

                                  Syllabus

    of a person to retreat into his or her home and “there be free from un-
    reasonable governmental intrusion.” Florida v. Jardines, 569 U. S. 1,
    6. A recognition of the existence of “community caretaking” tasks, like
    rendering aid to motorists in disabled vehicles, is not an open-ended
    license to perform them anywhere. Pp. 3–4.
953 F. 3d 112, vacated and remanded.

  THOMAS, J., delivered the opinion for a unanimous Court. ROBERTS,
C. J., filed a concurring opinion, in which BREYER, J., joined. ALITO, J.,
and KAVANAUGH, J., filed concurring opinions.
                        Cite as: 593 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–157
                                    _________________


          EDWARD A. CANIGLIA, PETITIONER v.
              ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                                  [May 17, 2021]

  JUSTICE THOMAS delivered the opinion of the Court.
  Decades ago, this Court held that a warrantless search of
an impounded vehicle for an unsecured firearm did not vio-
late the Fourth Amendment. Cady v. Dombrowski, 413
U. S. 433 (1973). In reaching this conclusion, the Court ob-
served that police officers who patrol the “public highways”
are often called to discharge noncriminal “community care-
taking functions,” such as responding to disabled vehicles
or investigating accidents. Id., at 441. The question today
is whether Cady’s acknowledgment of these “caretaking”
duties creates a standalone doctrine that justifies warrant-
less searches and seizures in the home. It does not.
                               I
  During an argument with his wife at their Rhode Island
home, Edward Caniglia (petitioner) retrieved a handgun
from the bedroom, put it on the dining room table, and
asked his wife to “shoot [him] now and get it over with.” She
declined, and instead left to spend the night at a hotel. The
next morning, when petitioner’s wife discovered that she
could not reach him by telephone, she called the police (re-
spondents) to request a welfare check.
2                    CANIGLIA v. STROM

                      Opinion of the Court

   Respondents accompanied petitioner’s wife to the home,
where they encountered petitioner on the porch. Petitioner
spoke with respondents and confirmed his wife’s account of
the argument, but denied that he was suicidal. Respond-
ents, however, thought that petitioner posed a risk to him-
self or others. They called an ambulance, and petitioner
agreed to go to the hospital for a psychiatric evaluation—
but only after respondents allegedly promised not to confis-
cate his firearms. Once the ambulance had taken petitioner
away, however, respondents seized the weapons. Guided
by petitioner’s wife—whom they allegedly misinformed
about his wishes—respondents entered the home and took
two handguns.
   Petitioner sued, claiming that respondents violated the
Fourth Amendment when they entered his home and seized
him and his firearms without a warrant. The District Court
granted summary judgment to respondents, and the First
Circuit affirmed solely on the ground that the decision to
remove petitioner and his firearms from the premises fell
within a “community caretaking exception” to the warrant
requirement. 953 F. 3d 112, 121–123, 131 and nn. 5, 9
(2020). Citing this Court’s statement in Cady that police
officers often have noncriminal reasons to interact with mo-
torists on “public highways,” 413 U. S., at 441, the First Cir-
cuit extrapolated a freestanding community-caretaking ex-
ception that applies to both cars and homes. 953 F. 3d, at
124 (“Threats to individual and community safety are not
confined to the highways”). Accordingly, the First Circuit
saw no need to consider whether anyone had consented to
respondents’ actions; whether these actions were justified
by “exigent circumstances”; or whether any state law per-
mitted this kind of mental-health intervention. Id., at 122–
123. All that mattered was that respondents’ efforts to pro-
tect petitioner and those around him were “distinct from
‘the normal work of criminal investigation,’ ” fell “within the
realm of reason,” and generally tracked what the court
                   Cite as: 593 U. S. ____ (2021)               3

                       Opinion of the Court

viewed to be “sound police procedure.” Id., at 123–128, 132–
133. We granted certiorari. 592 U. S. ___ (2020).
                                 II
    The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” The “ ‘very
core’ ” of this guarantee is “ ‘the right of a man to retreat into
his own home and there be free from unreasonable govern-
mental intrusion.’ ” Florida v. Jardines, 569 U. S. 1, 6
(2013).
    To be sure, the Fourth Amendment does not prohibit all
unwelcome intrusions “on private property,” ibid.—only
“unreasonable” ones. We have thus recognized a few per-
missible invasions of the home and its curtilage. Perhaps
most familiar, for example, are searches and seizures pur-
suant to a valid warrant. See Collins v. Virginia, 584 U. S.
___, ___–___ (2018) (slip op., at 5–6). We have also held that
law enforcement officers may enter private property with-
out a warrant when certain exigent circumstances exist, in-
cluding the need to “ ‘render emergency assistance to an in-
jured occupant or to protect an occupant from imminent
injury.’ ” Kentucky v. King, 563 U. S. 452, 460, 470 (2011);
see also Brigham City v. Stuart, 547 U. S. 398, 403–404
(2006) (listing other examples of exigent circumstances).
And, of course, officers may generally take actions that
“ ‘any private citizen might do’ ” without fear of liability.
E.g., Jardines, 569 U. S., at 8 (approaching a home and
knocking on the front door).
    The First Circuit’s “community caretaking” rule, how-
ever, goes beyond anything this Court has recognized. The
decision below assumed that respondents lacked a warrant
or consent, and it expressly disclaimed the possibility that
they were reacting to a crime. The court also declined to
consider whether any recognized exigent circumstances
were present because respondents had forfeited the point.
4                    CANIGLIA v. STROM

                      Opinion of the Court

Nor did it find that respondents’ actions were akin to what
a private citizen might have had authority to do if peti-
tioner’s wife had approached a neighbor for assistance in-
stead of the police.
   Neither the holding nor logic of Cady justified that ap-
proach. True, Cady also involved a warrantless search for
a firearm. But the location of that search was an im-
pounded vehicle—not a home—“ ‘a constitutional differ-
ence’ ” that the opinion repeatedly stressed. 413 U. S., at
439; see also id., at 440–442. In fact, Cady expressly con-
trasted its treatment of a vehicle already under police con-
trol with a search of a car “parked adjacent to the dwelling
place of the owner.” Id., at 446–448 (citing Coolidge v. New
Hampshire, 403 U. S. 443 (1971)).
   Cady’s unmistakable distinction between vehicles and
homes also places into proper context its reference to “com-
munity caretaking.” This quote comes from a portion of the
opinion explaining that the “frequency with which . . . vehi-
cle[s] can become disabled or involved in . . . accident[s] on
public highways” often requires police to perform noncrim-
inal “community caretaking functions,” such as providing
aid to motorists. 413 U. S., at 441. But, this recognition
that police officers perform many civic tasks in modern so-
ciety was just that—a recognition that these tasks exist,
and not an open-ended license to perform them anywhere.
                         *    *     *
    What is reasonable for vehicles is different from what is
reasonable for homes. Cady acknowledged as much, and
this Court has repeatedly “declined to expand the scope of
. . . exceptions to the warrant requirement to permit war-
rantless entry into the home.” Collins, 584 U. S., at ___ (slip
op., at 8). We thus vacate the judgment below and remand
for further proceedings consistent with this opinion.

                                              It is so ordered.
                 Cite as: 593 U. S. ____ (2021)            1

                   ROBERTS, C. J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–157
                         _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                        [May 17, 2021]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE BREYER
joins, concurring.
   Fifteen years ago, this Court unanimously recognized
that “[t]he role of a peace officer includes preventing vio-
lence and restoring order, not simply rendering first aid to
casualties.” Brigham City v. Stuart, 547 U. S. 398, 406
(2006). A warrant to enter a home is not required, we ex-
plained, when there is a “need to assist persons who are se-
riously injured or threatened with such injury.” Id., at 403;
see also Michigan v. Fisher, 558 U. S. 45, 49 (2009) (per cu-
riam) (warrantless entry justified where “there was an ob-
jectively reasonable basis for believing that medical assis-
tance was needed, or persons were in danger” (internal
quotation marks omitted)). Nothing in today’s opinion is to
the contrary, and I join it on that basis.
                  Cite as: 593 U. S. ____ (2021)            1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 20–157
                          _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                         [May 17, 2021]

   JUSTICE ALITO, concurring.
   I join the opinion of the Court but write separately to ex-
plain my understanding of the Court’s holding and to high-
light some important questions that the Court does not de-
cide.
   1. The Court holds—and I entirely agree—that there is
no special Fourth Amendment rule for a broad category of
cases involving “community caretaking.” As I understand
the term, it describes the many police tasks that go beyond
criminal law enforcement. These tasks vary widely, and
there is no clear limit on how far they might extend in the
future. The category potentially includes any non-law-en-
forcement work that a community chooses to assign, and
because of the breadth of activities that may be described
as community caretaking, we should not assume that the
Fourth Amendment’s command of reasonableness applies
in the same way to everything that might be viewed as fall-
ing into this broad category.
   The Court’s decision in Cady v. Dombrowski, 413 U. S.
433 (1973), did not recognize any such “freestanding”
Fourth Amendment category. See ante, at 2, 4. The opinion
merely used the phrase “community caretaking” in passing.
413 U. S., at 441.
   2. While there is no overarching “community caretaking”
doctrine, it does not follow that all searches and seizures
2                        CANIGLIA v. STROM

                          ALITO, J., concurring

conducted for non-law-enforcement purposes must be ana-
lyzed under precisely the same Fourth Amendment rules
developed in criminal cases. Those rules may or may not be
appropriate for use in various non-criminal-law-enforce-
ment contexts. We do not decide that issue today.
   3. This case falls within one important category of cases
that could be viewed as involving community caretaking:
conducting a search or seizure for the purpose of preventing
a person from committing suicide. Assuming that peti-
tioner did not voluntarily consent to go with the officers for
a psychological assessment,1 he was seized and thus sub-
jected to a serious deprivation of liberty. But was this war-
rantless seizure “reasonable”? We have addressed the
standards required by due process for involuntary commit-
ment to a mental treatment facility, see Addington v. Texas,
441 U. S. 418, 427 (1979); see also O’Connor v. Donaldson,
422 U. S. 563, 574–576 (1975); Foucha v. Louisiana, 504
U. S. 71, 75–77, 83 (1992), but we have not addressed
Fourth Amendment restrictions on seizures like the one
that we must assume occurred here, i.e., a short-term sei-
zure conducted for the purpose of ascertaining whether a
person presents an imminent risk of suicide. Every State
has laws allowing emergency seizures for psychiatric treat-
ment, observation, or stabilization, but these laws vary in
many respects, including the categories of persons who may
request the emergency action, the reasons that can justify
the action, the necessity of a judicial proceeding, and the
nature of the proceeding.2 Mentioning these laws only in
passing, petitioner asked us to render a decision that could
——————
   1 The Court of Appeals assumed petitioner’s consent was not voluntary

because the police allegedly promised that they would not seize his guns
if he went for a psychological evaluation. 953 F. 3d 112, 121 (CA1 2020).
The Court does not decide whether this assumption was justified.
   2 See Brief for Petitioner 38–39, n. 4 (gathering state authorities); L.

Hedman et al., State Laws on Emergency Holds for Mental Health Sta-
bilization, 67 Psychiatric Servs. 579 (2016).
                  Cite as: 593 U. S. ____ (2021)            3

                      ALITO, J., concurring

call features of these laws into question. The Court appro-
priately refrains from doing so.
   4. This case also implicates another body of law that pe-
titioner glossed over: the so-called “red flag” laws that some
States are now enacting. These laws enable the police to
seize guns pursuant to a court order to prevent their use for
suicide or the infliction of harm on innocent persons. See,
e.g., Cal. Penal Code Ann. §§18125–18148 (West Cum.
Supp. 2021); Fla. Stat. §790.401(4) (Cum. Supp. 2021);
Mass. Gen. Laws Ann., ch. 140, §131T (2021). They typi-
cally specify the standard that must be met and the proce-
dures that must be followed before firearms may be seized.
Provisions of red flag laws may be challenged under the
Fourth Amendment, and those cases may come before us.
Our decision today does not address those issues.
   5. One additional category of cases should be noted: those
involving warrantless, nonconsensual searches of a home
for the purpose of ascertaining whether a resident is in ur-
gent need of medical attention and cannot summon help.
At oral argument, THE CHIEF JUSTICE posed a question
that highlighted this problem. He imagined a situation in
which neighbors of an elderly woman call the police and ex-
press concern because the woman had agreed to come over
for dinner at 6 p.m., but by 8 p.m., had not appeared or
called even though she was never late for anything. The
woman had not been seen leaving her home, and she was
not answering the phone. Nor could the neighbors reach
her relatives by phone. If the police entered the home with-
out a warrant to see if she needed help, would that violate
the Fourth Amendment? Tr. of Oral Arg. 6–8.
   Petitioner’s answer was that it would. Indeed, he argued,
even if 24 hours went by, the police still could not lawfully
enter without a warrant. If the situation remained un-
changed for several days, he suggested, the police might be
able to enter after obtaining “a warrant for a missing per-
son.” Id., at 9.
4                        CANIGLIA v. STROM

                          ALITO, J., concurring

  THE CHIEF JUSTICE’s question concerns an important
real-world problem. Today, more than ever, many people,
including many elderly persons, live alone.3 Many elderly
men and women fall in their homes,4 or become incapaci-
tated for other reasons, and unfortunately, there are many
cases in which such persons cannot call for assistance. In
those cases, the chances for a good recovery may fade with
each passing hour.5 So in THE CHIEF JUSTICE’s imaginary
case, if the elderly woman was seriously hurt or sick and
the police heeded petitioner’s suggestion about what the
Fourth Amendment demands, there is a fair chance she
would not be found alive. This imaginary woman may have
regarded her house as her castle, but it is doubtful that she
would have wanted it to be the place where she died alone
and in agony.
  Our current precedents do not address situations like
this. We have held that the police may enter a home with-
out a warrant when there are “exigent circumstances.”
Payton v. New York, 445 U. S. 573, 590 (1980). But circum-
stances are exigent only when there is not enough time to
get a warrant, see Missouri v. McNeely, 569 U. S. 141, 149
(2013); Michigan v. Tyler, 436 U. S. 499, 509 (1978), and
warrants are not typically granted for the purpose of check-
ing on a person’s medical condition. Perhaps States should
institute procedures for the issuance of such warrants, but
——————
   3 Dept. of Commerce, Bureau of Census, The Rise of Living Alone,

Fig. HH–4 (2020), https://www.census.gov/content/dam/Census/
library /visualizations/time-series/demo/families-and-households/hh-4.pdf;
Ortiz-Ospina, The Rise of Living Alone (Dec. 10, 2019), https://our-
worldindata.org/living-alone; Smith, Cities With the Most Adults Living
Alone (May 4, 2020), https://www.self.inc/blog/adults-living-alone.
   4 See B. Moreland, R. Kakara, & A. Henry, Trends in Nonfatal Falls

and Fall-Related Injuries Among Adults Aged ≥65 Years—United States,
2012–2018, 69 Morbidity and Mortality Weekly Rep. 875 (2020).
   5 See, e.g., J. Gurley, N. Lum, M. Sande, B. Lo, & M. Katz, Persons

Found in Their Homes Helpless or Dead, 334 New Eng. J. Med. 1710
(1996).
                Cite as: 593 U. S. ____ (2021)          5

                    ALITO, J., concurring

in the meantime, courts may be required to grapple with
the basic Fourth Amendment question of reasonableness.
   6. The three categories of cases discussed above are
simply illustrative. Searches and seizures conducted for
other non-law-enforcement purposes may arise and may
present their own Fourth Amendment issues. Today’s de-
cision does not settle those questions.
                         *    *       *
  In sum, the Court properly rejects the broad “community
caretaking” theory on which the decision below was based.
The Court’s decision goes no further, and on that under-
standing, I join the opinion in full.
                  Cite as: 593 U. S. ____ (2021)             1

                   KAVANAUGH, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 20–157
                          _________________


        EDWARD A. CANIGLIA, PETITIONER v.
            ROBERT F. STROM, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
             APPEALS FOR THE FIRST CIRCUIT
                         [May 17, 2021]

   JUSTICE KAVANAUGH, concurring.
   I join the Court’s opinion in full. I write separately to
underscore and elaborate on THE CHIEF JUSTICE’s point
that the Court’s decision does not prevent police officers
from taking reasonable steps to assist those who are inside
a home and in need of aid. See ante, at 1 (ROBERTS, C. J.,
concurring). For example, as I will explain, police officers
may enter a home without a warrant in circumstances
where they are reasonably trying to prevent a potential su-
icide or to help an elderly person who has been out of con-
tact and may have fallen and suffered a serious injury.
   Ratified in 1791 and made applicable to the States in
1868, the Fourth Amendment protects the “right of the peo-
ple to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” As the con-
stitutional text establishes, the “ultimate touchstone of the
Fourth Amendment is reasonableness.” Riley v. California,
573 U. S. 373, 381 (2014) (internal quotation marks omit-
ted). The Court has said that a warrant supported by prob-
able cause is ordinarily required for law enforcement offic-
ers to enter a home. See U. S. Const., Amdt. 4. But drawing
on common-law analogies and a commonsense appraisal of
what is “reasonable,” the Court has recognized various sit-
uations where a warrant is not required. For example, the
exigent circumstances doctrine allows officers to enter a
2                    CANIGLIA v. STROM

                   KAVANAUGH, J., concurring

home without a warrant in certain situations, including: to
fight a fire and investigate its cause; to prevent the immi-
nent destruction of evidence; to engage in hot pursuit of a
fleeing felon or prevent a suspect’s escape; to address a
threat to the safety of law enforcement officers or the gen-
eral public; to render emergency assistance to an injured
occupant; or to protect an occupant who is threatened with
serious injury. See Mitchell v. Wisconsin, 588 U. S. ___, ___
(2019) (plurality opinion) (slip op., at 6); City and County of
San Francisco v. Sheehan, 575 U. S. 600, 612 (2015); Ken-
tucky v. King, 563 U. S. 452, 460, 462 (2011); Michigan v.
Fisher, 558 U. S. 45, 47 (2009) (per curiam); Brigham City
v. Stuart, 547 U. S. 398, 403 (2006); Minnesota v. Olson, 495
U. S. 91, 100 (1990); Michigan v. Clifford, 464 U. S. 287,
293, and n. 4 (1984) (plurality opinion); Mincey v. Arizona,
437 U. S. 385, 392–394 (1978); Michigan v. Tyler, 436 U. S.
499, 509–510 (1978); United States v. Santana, 427 U. S.
38, 42–43 (1976); Warden, Md. Penitentiary v. Hayden, 387
U. S. 294, 298–299 (1967); Ker v. California, 374 U. S. 23,
40–41 (1963) (plurality opinion).
   Over the years, many courts, like the First Circuit in this
case, have relied on what they have labeled a “community
caretaking” doctrine to allow warrantless entries into the
home for a non-investigatory purpose, such as to prevent a
suicide or to conduct a welfare check on an older individual
who has been out of contact. But as the Court today ex-
plains, any such standalone community caretaking doctrine
was primarily devised for searches of cars, not homes. Ante,
at 3–4; see Cady v. Dombrowski, 413 U. S. 433, 447–448
(1973).
   That said, this Fourth Amendment issue is more labeling
than substance. The Court’s Fourth Amendment case law
already recognizes the exigent circumstances doctrine,
which allows an officer to enter a home without a warrant
if the “exigencies of the situation make the needs of law en-
                  Cite as: 593 U. S. ____ (2021)             3

                   KAVANAUGH, J., concurring

forcement so compelling that the warrantless search is ob-
jectively reasonable under the Fourth Amendment.”
Brigham City, 547 U. S., at 403 (internal quotation marks
omitted); see also ante, at 3. As relevant here, one such rec-
ognized “exigency” is the “need to assist persons who are
seriously injured or threatened with such injury.” Brigham
City, 547 U. S., at 403; see also ante, at 1 (ROBERTS, C. J.,
concurring). The Fourth Amendment allows officers to en-
ter a home if they have “an objectively reasonable basis for
believing” that such help is needed, and if the officers’ ac-
tions inside the home are reasonable under the circum-
stances. Brigham City, 547 U. S., at 406; see also Michigan
v. Fisher, 558 U. S., at 47–48.
   This case does not require us to explore all the contours
of the exigent circumstances doctrine as applied to emer-
gency-aid situations because the officers here disclaimed re-
liance on that doctrine. But to avoid any confusion going
forward, I think it important to briefly describe how the doc-
trine applies to some heartland emergency-aid situations.
   As Chief Judge Livingston has cogently explained, alt-
hough this doctrinal area does not draw much attention
from courts or scholars, “municipal police spend a good deal
of time responding to calls about missing persons, sick
neighbors, and premises left open at night.” Livingston, Po-
lice, Community Caretaking, and the Fourth Amendment,
1998 U. Chi. Leg. Forum 261, 263 (1998). And as she aptly
noted, “the responsibility of police officers to search for
missing persons, to mediate disputes, and to aid the ill or
injured has never been the subject of serious debate; nor
has” the “responsibility of police to provide services in an
emergency.” Id., at 302.
   Consistent with that reality, the Court’s exigency prece-
dents, as I read them, permit warrantless entries when po-
lice officers have an objectively reasonable basis to believe
that there is a current, ongoing crisis for which it is reason-
4                       CANIGLIA v. STROM

                      KAVANAUGH, J., concurring

able to act now. See, e.g., Sheehan, 575 U. S., at 612; Mich-
igan v. Fisher, 558 U. S., at 48–49; Brigham City, 547 U. S.,
at 406–407. The officers do not need to show that the harm
has already occurred or is mere moments away, because
knowing that will often be difficult if not impossible in cases
involving, for example, a person who is currently suicidal or
an elderly person who has been out of contact and may have
fallen. If someone is at risk of serious harm and it is rea-
sonable for officers to intervene now, that is enough for the
officers to enter.
   A few (non-exhaustive) examples illustrate the point.
   Suppose that a woman calls a healthcare hotline or 911
and says that she is contemplating suicide, that she has
firearms in her home, and that she might as well die. The
operator alerts the police, and two officers respond by driv-
ing to the woman’s home. They knock on the door but do
not receive a response. May the officers enter the home? Of
course.
   The exigent circumstances doctrine applies because the
officers have an “objectively reasonable basis” for believing
that an occupant is “seriously injured or threatened with
such injury.” Id., at 400, 403; cf. Sheehan, 575 U. S., at 612
(officers could enter the room of a mentally ill person who
had locked herself inside with a knife). After all, a suicidal
individual in such a scenario could kill herself at any mo-
ment. The Fourth Amendment does not require officers to
stand idly outside as the suicide takes place.1
   Consider another example. Suppose that an elderly man
is uncharacteristically absent from Sunday church services
——————
   1 In 2019 in the United States, 47,511 people committed suicide. That

number is more than double the number of annual homicides. See Dept.
of Health and Human Servs., Centers for Disease Control and Preven-
tion, D. Stone, C. Jones, & K. Mack, Changes in Suicide Rates––United
States, 2018–2019, 70 Morbidity and Mortality Weekly Rep. 261, 263
(2021) (MMWR); Dept. of Justice, Federal Bureau of Investigation, Uni-
form Crime Report, Crime in the United States, 2019, p. 2 (2020).
                      Cite as: 593 U. S. ____ (2021)                     5

                       KAVANAUGH, J., concurring

and repeatedly fails to answer his phone throughout the
day and night. A concerned relative calls the police and
asks the officers to perform a wellness check. Two officers
drive to the man’s home. They knock but receive no re-
sponse. May the officers enter the home? Of course.
   Again, the officers have an “objectively reasonable basis”
for believing that an occupant is “seriously injured or
threatened with such injury.” Brigham City, 547 U. S., at
400, 403. Among other possibilities, the elderly man may
have fallen and hurt himself, a common cause of death or
serious injury for older individuals. The Fourth Amend-
ment does not prevent the officers from entering the home
and checking on the man’s well-being.2
   To be sure, courts, police departments, and police officers
alike must take care that officers’ actions in those kinds of
cases are reasonable under the circumstances. But both of
those examples and others as well, such as cases involving
unattended young children inside a home, illustrate the
kinds of warrantless entries that are perfectly constitu-
tional under the exigent circumstances doctrine, in my
view.
   With those observations, I join the Court’s opinion in full.




——————
  2 In 2018 in the United States, approximately 32,000 older adults died

from falls. Falls are also the leading cause of injury for older adults. B.
Moreland, R. Kakara, & A. Henry, Trends in Nonfatal Falls and Fall-
Related Injuries Among Adults Aged ≥ 65 Years––United States, 2012–
2018, 69 MMWR 875 (2020).

```

---

## GROUP: _overhaul2/lake/cases/Cardwell v. Lewis.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Cardwell v. Lewis"
type: case
citation: "417 U.S. 583 (1974)"
parallel_cite: "94 S. Ct. 2464; 41 L. Ed. 2d 325; 69 Ohio Op. 2d 69"
neutral_cite: 1974 U.S. LEXIS 75
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-06-17
docket: 72-1603
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Cardwell v. Lewis
  varies_by_point: false
  scope_note: "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/"
  cluster_id: 109069
  opinion_id: 109069
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
  - page: "[[Reasonable Expectation of Privacy]]"
    role: "Related (cross-doctrine)"
related: ["[[Chambers v. Maroney]]", "[[Cooper v. California]]", "[[Coolidge v. New Hampshire]]", "[[New York v. Class]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "reduced-expectation-of-privacy", "vehicle-exterior", "no-search"]
holding: "Examining a car's exterior (paint scrapings, tire tread) on probable cause in a public lot invades no privacy interest the warrant requirement protects; one has a reduced expectation of privacy in a vehicle, especially its exterior."
lake:
  record_id: Cardwell v. Lewis
  status: verified
  projected_at: 2026-07-09
---

# Cardwell v. Lewis

*417 U.S. 583 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police investigating a murder had probable cause to believe the respondent's car had been used in the crime. After the respondent came to the station and was arrested, police impounded his car from a public commercial lot, towed it to an impound area, and there took paint scrapings from the exterior and made a cast of a tire tread. That exterior evidence was introduced at his murder trial.

## Issue
Whether the warrantless examination of an automobile's exterior — paint scrapings and tire tread — on probable cause, after the car was impounded from a public lot, is a search that violates the Fourth Amendment.

## Rule
No. A vehicle, and especially its exterior, carries a reduced expectation of privacy: "One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view." — 417 U.S. at 590 (plurality opinion). ^pin-590

Because only the exterior was examined, no protected privacy was invaded: "With the 'search' limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed." — *Id.* at 591. ^pin-591

The bottom line: "where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments." — [*Id.* at 592](https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/#:~:text=where%20probable%20cause%20exists%2C%20a). ^pin-592

## Application
Nothing from the interior of the car and no personal effects were searched or seized; the evidence was limited to paint scrapings from the exterior and an observation of the tire tread on an operative wheel, taken from a car left in a public lot. With probable cause established, that exterior examination invaded no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and the prior impoundment did not change the result, since police could have made the same examination on the spot.

## Conclusion
The exterior examination was reasonable; the seizure and examination did not violate the Fourth Amendment, and the grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Powell, J., concurred in the result on a different ground).
- No negative treatment of the exterior-examination / reduced-vehicle-privacy rationale, which the Court has continued to invoke (e.g., quoted in [[United States v. Chadwick]] and reflected in the no-REP-in-a-public-VIN holding of [[New York v. Class]]).

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*
- [[Reasonable Expectation of Privacy]] — *Related (cross-doctrine)*

## Sources
- *Cardwell v. Lewis*, 417 U.S. 583 (1974) — https://www.courtlistener.com/opinion/109069/cardwell-v-lewis/ — pinpoints: 590, 591, 592.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "99e7541f4bb0180f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Cardwell v. Lewis"}, "payload": {"all": [{"cite": "417 U.S. 583", "page": "583", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "417"}, {"cite": "94 S. Ct. 2464", "page": "2464", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "41 L. Ed. 2d 325", "page": "325", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "41"}, {"cite": "1974 U.S. LEXIS 75", "page": "75", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}, {"cite": "69 Ohio Op. 2d 69", "page": "69", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "69"}], "display": "417 U.S. 583", "official": {"cite": "417 U.S. 583", "page": "583", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "417"}, "official_selection_present": true, "record_id": "Cardwell v. Lewis"}}
{"assertion_id": "8500bba7f2621150", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-592", "record_id": "Cardwell v. Lewis"}, "payload": {"fragment": "#:~:text=where%20probable%20cause%20exists%2C%20a", "page": null, "pin_id": "pin-592", "pinpoint_status": "star-verified", "quote": "where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments.", "quote_fidelity": "matched", "record_id": "Cardwell v. Lewis", "star_marker": "592"}}
{"assertion_id": "8c59b463831b9dc8", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-591", "record_id": "Cardwell v. Lewis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-591", "pinpoint_status": "slip-only", "quote": "With the 'search' limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed.", "quote_fidelity": "mismatch", "record_id": "Cardwell v. Lewis", "star_marker": null}}
{"assertion_id": "c860a721e8ead1d6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-590", "record_id": "Cardwell v. Lewis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-590", "pinpoint_status": "slip-only", "quote": "--- # Cardwell v. Lewis *417 U.S. 583 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police investigating a murder had probable cause to believe the respondent's car had been used in the crime. After the respondent came to the station and was arrested, police impounded his car from a public commercial lot, towed it to an impound area, and there took paint scrapings from the exterior and made a cast of a tire tread. That exterior evidence was introduced at his murder trial. ## Issue Whether the warrantless examination of an automobile's exterior — paint scrapings and tire tread — on probable cause, after the car was impounded from a public lot, is a search that violates the Fourth Amendment. ## Rule No. A vehicle, and especially its exterior, carries a reduced expectation of privacy:", "quote_fidelity": "mismatch", "record_id": "Cardwell v. Lewis", "star_marker": null}}
{"assertion_id": "10c632673a25231e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Cardwell v. Lewis"}, "payload": {"as_of_content": "1974-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Cardwell v. Lewis", "scope_note": "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick).", "varies_by_point": false}}
```

### lake record — Cardwell v. Lewis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Cardwell v. Lewis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Cardwell v. Lewis",
    "case_name_short": "Cardwell",
    "case_name_full": "Cardwell, Warden v. Lewis",
    "input_case_name": "Cardwell v. Lewis",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-06-17",
    "year": 1974,
    "docket": "72-1603",
    "cluster_id": 109069,
    "lead_opinion_id": 109069,
    "sibling_ids": [
      109069,
      9425767,
      9425768,
      9425769
    ],
    "absolute_url": "/opinion/109069/cardwell-v-lewis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8997104,
        "score": 20,
        "case_name": "Cardwell v. Lewis"
      },
      {
        "cluster_id": 8996372,
        "score": 20,
        "case_name": "Cardwell v. Lewis"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "417 U.S. 583",
      "volume": "417",
      "reporter": "U.S.",
      "page": "583",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 2464",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 325",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 Ohio Op. 2d 69",
        "volume": "69",
        "reporter": "Ohio Op. 2d",
        "page": "69",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 75",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "417 U.S. 583",
        "volume": "417",
        "reporter": "U.S.",
        "page": "583",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 2464",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "2464",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 L. Ed. 2d 325",
        "volume": "41",
        "reporter": "L. Ed. 2d",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 75",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "75",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 Ohio Op. 2d 69",
        "volume": "69",
        "reporter": "Ohio Op. 2d",
        "page": "69",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "417 U.S. 583",
    "official_selection": {
      "court_class": "scotus",
      "selected": "417 U.S. 583",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-590",
      "page": null,
      "quote": "--- # Cardwell v. Lewis *417 U.S. 583 (1974)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police investigating a murder had probable cause to believe the respondent's car had been used in the crime. After the respondent came to the station and was arrested, police impounded his car from a public commercial lot, towed it to an impound area, and there took paint scrapings from the exterior and made a cast of a tire tread. That exterior evidence was introduced at his murder trial. ## Issue Whether the warrantless examination of an automobile's exterior \u2014 paint scrapings and tire tread \u2014 on probable cause, after the car was impounded from a public lot, is a search that violates the Fourth Amendment. ## Rule No. A vehicle, and especially its exterior, carries a reduced expectation of privacy:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-591",
      "page": null,
      "quote": "With the 'search' limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-592",
      "page": null,
      "quote": "where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments.",
      "star_marker": "592",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 16006,
      "fragment": "#:~:text=where%20probable%20cause%20exists%2C%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Cardwell v. Lewis",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Blackmun, J., joined by Burger, White, Rehnquist; Powell, J., concurring in the result). The reduced-expectation-of-privacy-in-a-vehicle's-exterior rationale is settled and routinely cited (e.g., quoted in United States v. Chadwick).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
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
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
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
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Savva",
          "cluster_id": 2277827,
          "cite": [
            "616 A.2d 774",
            "159 Vt. 75",
            "1992 Vt. LEXIS 116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cyrus Jonathan George",
          "cluster_id": 588130,
          "cite": [
            "971 F.2d 1113"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanchez",
          "cluster_id": 2383586,
          "cite": [
            "800 S.W.2d 292",
            "1990 WL 178626"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Francisco Paulino",
          "cluster_id": 508162,
          "cite": [
            "850 F.2d 93",
            "1988 U.S. App. LEXIS 8724",
            "1988 WL 64524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane1_negative"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johns",
          "cluster_id": 111305,
          "cite": [
            "83 L. Ed. 2d 890",
            "105 S. Ct. 881",
            "469 U.S. 478",
            "1985 U.S. LEXIS 45",
            "53 U.S.L.W. 4126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carmine Tramunti",
          "cluster_id": 326798,
          "cite": [
            "513 F.2d 1087"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
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
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 1142777,
          "cite": [
            "666 P.2d 802",
            "295 Or. 227",
            "1983 Ore. LEXIS 1342"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Alston",
          "cluster_id": 2283490,
          "cite": [
            "440 A.2d 1311",
            "88 N.J. 211",
            "1981 N.J. LEXIS 1677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carlo Scott Bagley",
          "cluster_id": 457913,
          "cite": [
            "772 F.2d 482",
            "19 Fed. R. Serv. 222",
            "1985 U.S. App. LEXIS 23309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Cardwell v. Lewis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTgzMTY4MDAwMDAmcz0xNjM4MjczJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzcmcz0yMDY2MDk3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
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
    "complete_query": "cites:(109069 OR 9425767 OR 9425768 OR 9425769)",
    "indexed_citing_opinions": 662,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109069,
        "count": 589,
        "count_source": "search"
      },
      {
        "opinion_id": 9425767,
        "count": 102,
        "count_source": "search"
      },
      {
        "opinion_id": 9425768,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425769,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1012,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/cardwell-v-lewis.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3MDU0NTEmcz00NzM5MTkzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109069+OR+9425767+OR+9425768+OR+9425769%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109069,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 310138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109069,
        "cited_id": 1380337,
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
    "date_created": "2026-07-04T23:32:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:36:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:32:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Cardwell v. Lewis

```
<div>
<center><b><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U.S. 583</a></span> (1974)</b></center>
<center><h1>CARDWELL, WARDEN<br>
v.<br>
LEWIS.</h1></center>
<center>No. 72-1603.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18, 1974.</center>
<center>Decided June 17, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SIXTH CIRCUIT.
<p><span class="star-pagination">*584</span> <i>Leo J. Conway,</i> Assistant Attorney General of Ohio, argued the cause for petitioner. With him on the brief were <i>William J. Brown,</i> Attorney General, and <i>Nicholas R. Curci,</i> Assistant Attorney General.</p>
<p><i>Bruce A. Campbell,</i> by appointment of the Court, 414 <span class="star-pagination">*585</span> U. S. 1140, argued the cause and filed a brief for respondent.</p>
<p><i>Andrew L. Frey</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. On the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen,</i> and <i>Edward R. Korman.</i></p>
<p>MR. JUSTICE BLACKMUN announced the judgment of the Court and an opinion in which the CHIEF JUSTICE, MR. JUSTICE WHITE, and MR. JUSTICE REHNQUIST join.</p>
<p>This case presents the issue of the legality, under the Fourth and Fourteenth Amendments, of a warrantless seizure of an automobile and the examination of its exterior at a police impoundment area after the car had been removed from a public parking lot.</p>
<p>Evidence obtained upon this examination was introduced at the respondent's state court trial for first-degree murder. He was convicted. The Federal District Court, on a habeas corpus application, ruled that the examination was a search violative of the Fourth and Fourteenth Amendments. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp. 26</a></span> (SD Ohio 1972). The United States Court of Appeals for the Sixth Circuit affirmed. <span class="citation" data-id="310138"><a href="/opinion/310138/arthur-ben-lewis-jr-v-harold-j-cardwell-warden/" aria-description="Citation for case: Arthur Ben Lewis, Jr. v. Harold J. Cardwell, Warden">476 F. 2d 467</a></span> (1973). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1062/">414 U. S. 1062</a></span> (1973), and now conclude that, under the circumstances of this case, there was no violation of the protection afforded by the Amendments.</p>
<p></p>
<h2>I</h2>
<p>In 1968 respondent Arthur Ben Lewis, Jr., was tried and convicted by a jury in an Ohio state court for the first-degree murder of Paul Radcliffe. On appeal, the Supreme Court of Ohio affirmed the judgment of conviction. <i>State</i> v. <i>Lewis,</i> <span class="citation" data-id="6754444"><a href="/opinion/6864632/state-v-lewis/" aria-description="Citation for case: State v. Lewis">22 Ohio St. 2d 125</a></span>, <span class="citation" data-id="6754444"><a href="/opinion/6864632/state-v-lewis/" aria-description="Citation for case: State v. Lewis">258 N. E. 2d 445</a></span> (1970). This Court denied review. <i>Lewis</i> v. <i>Ohio,</i> <span class="citation" data-id="8973497"><a href="/opinion/8981620/lewis-v-ohio/" aria-description="Citation for case: Lewis v. Ohio">400 U. S. 959</a></span> (1970).</p>
<p><span class="star-pagination">*586</span> On respondent's federal habeas application, the District Court, from the record and after an evidentiary hearing, adduced the following facts:</p>
<p>On the afternoon of July 19, 1967, Radcliffe's body was found near his car on the banks of the Olentangy River in Delaware County, Ohio. The car had gone over the embankment and had come to rest in brush. Radcliffe had died from shotgun wounds. Casts were made of tire tracks at the scene, and foreign paint scrapings were removed from the right rear fender of Radcliffe's automobile.</p>
<p>Within five days of Radcliffe's death, the investigation began to focus upon respondent Lewis. It was learned that Lewis knew Radcliffe. Lewis had been negotiating the sale of a business and had executed a contract of sale. The purchaser, Jack Smith, employed Radcliffe, an accountant, to examine Lewis' books. Police went to Lewis' place of business to question him and there observed the model and color of his car in the thought that it might have been used to push the Radcliffe vehicle over the embankment. Not until several months later, however, in late September, was Lewis again questioned. On October 9, he was asked to appear the next morning at the Office of the Division of Criminal Activities in Columbus for further interrogation.</p>
<p>On October 10, at 8 a. m., a warrant for respondent's arrest was obtained.<sup>[1]</sup> The District Court found that at <span class="star-pagination">*587</span> this time, in addition to probable cause for the arrest, the police also had probable cause to believe that Lewis' car was used in the commission of the crime. An automobile similar to his had been observed leaving the scene; the color of his vehicle was similar to the color of the paint scrapings from the victim's car; in a telephone call to Mrs. Smith, made by a person who said he was Radcliffe, but proved not to be,<sup>[2]</sup> the caller made statements that, if true, would benefit only Lewis; he had had body repair work done on the grille, hood, right front fender, and other parts of his car on the day following the crime; and the victim's desk calendar for the day of his death showed the notation, "Call Ben Lewis."<sup>[3]</sup></p>
<p>Respondent Lewis complied with the request to appear. He drove his car to the Activities Office, placed it in a public commercial parking lot a half block away, and arrived shortly after 10 a. m. Although the police were in possession of the arrest warrant for the entire period that Lewis was present, he was not served with that warrant or arrested until late that afternoon, at approximately 5 p. m. Two hours earlier, Lewis had been permitted to call his lawyer, and two attorneys were present on his behalf in the office at the time of the formal arrest. Upon the arrest, Lewis' car keys and the parking lot claim check were released to the police. A tow truck <span class="star-pagination">*588</span> was dispatched to remove the car from the parking lot to the police impoundment lot.</p>
<p>The impounded car was examined the next day by a technician from the Ohio Bureau of Criminal Investigation. The tread of its right rear tire was found to match the cast of a tire impression made at the scene of the crime.<sup>[4]</sup> The technician testified that, in his opinion, the foreign paint on the fender of Radcliffe's car was not different from the paint samples taken from respondent's vehicle, that is, there was no difference in color, texture, or order of layering of the paint.</p>
<p>The District Court concluded that the seizure and examination of Lewis' car were violative of the Fourth and Fourteenth Amendments, and that the evidence obtained therefrom should have been excluded at the state court trial. The court, accordingly, issued a writ of habeas corpus requiring the State to "initiate action for a new trial of" respondent within 90 days or, in the alternative, to release him. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#44" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 44</a></span>. The Court of Appeals, in affirming, held that the scraping of paint from the exterior of Lewis' car was in fact a search, within the meaning of the Fourth Amendment; that there was no consent to that search; that it was not incident to Lewis' arrest; and that the seizure of the car could not be justified on the ground that the vehicle was an instrumentality of the crime in plain view.</p>
<p></p>
<h2>II</h2>
<p>This case is factually different from prior car search cases decided by this Court. The evidence with which we are concerned is not the product of a "search" that implicates <span class="star-pagination">*589</span> traditional considerations of the owner's privacy interest. It consisted of paint scrapings from the <i>exterior</i> and an observation of the tread of a tire on an operative wheel. The issue, therefore, is whether the examination of an automobile's exterior upon probable cause invades a right to privacy which the interposition of a warrant requirement is meant to protect. This is an issue this Court has not previously addressed.</p>
<p>The common-law notion that a warrant to search and seize is dependent upon the assertion of a superior government interest in property, see, <i>e. g., </i><i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 1066 (1765), and the proposition that a warrant is valid "only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it," <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span> (1921), were explicitly rejected as controlling Fourth Amendment considerations in <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-306</a></span> (1967). Rather than property rights, the primary object of the Fourth Amendment was determined to be the protection of privacy. <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#305" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden"><i>Id.,</i> at 305-306</a></span>. And it had been said earlier: "The decisions of this Court have time and again underscored the essential purpose of the Fourth Amendment to shield the citizen from unwarranted intrusions into his privacy." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#498" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 498</a></span> (1958). See also <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#769" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 769-770</a></span> (1966); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 350</a></span> (1967); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 14-15</a></span> (1973).</p>
<p>At least since <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), the Court has recognized a distinction between the warrantless search and seizure of automobiles or other movable vehicles, on the one hand, and the search of a home or office, on the other. Generally, less stringent <span class="star-pagination">*590</span> warrant requirements have been applied to vehicles. In <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#49" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 49</a></span> (1970), the Court chronicled the development of car searches and seizures.<sup>[5]</sup> An underlying factor in the <i>Carroll-Chambers</i> line of decisions has been the exigent circumstances that exist in connection with movable vehicles. "[T]he circumstances that furnish probable cause to search a particular auto for particular articles are most often unforeseeable; moreover, the opportunity to search is fleeting since a car is readily movable." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 50-51</a></span>. This is strikingly true where the automobile's owner is alerted to police intentions and, as a consequence, the motivation to remove evidence from official grasp is heightened.</p>
<p>There is still another distinguishing factor. "The search of an automobile is far less intrusive on the rights protected by the Fourth Amendment than the search of one's person or of a building." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (POWELL, J., concurring). One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. A car has little capacity for escaping public scrutiny. It travels public thoroughfares where both its occupants and its contents are in plain view. See <i>People</i> v. <i>Case,</i> <span class="citation" data-id="7951958"><a href="/opinion/7998117/people-v-case/#388" aria-description="Citation for case: People v. Case">220 Mich. 379, 388-389</a></span>, <span class="star-pagination">*591</span> <span class="citation" data-id="7951958"><a href="/opinion/7998117/people-v-case/#292" aria-description="Citation for case: People v. Case">190 N. W. 289, 292</a></span> (1922). "What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S., at 351</a></span>; <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S., at 14</a></span>. This is not to say that no part of the interior of an automobile has Fourth Amendment protection; the exercise of a desire to be mobile does not, of course, waive one's right to be free of unreasonable government intrusion. But insofar as Fourth Amendment protection extends to a motor vehicle, it is the right to privacy that is the touchstone of our inquiry.</p>
<p>In the present case, nothing from the interior of the car and no personal effects, which the Fourth Amendment traditionally has been deemed to protect, were searched or seized and introduced in evidence.<sup>[6]</sup> With the "search" limited to the examination of the tire on the wheel and the taking of paint scrapings from the exterior of the vehicle left in the public parking lot, we fail to comprehend what expectation of privacy was infringed.<sup>[7]</sup> Stated <span class="star-pagination">*592</span> simply, the invasion of privacy, "if it can be said to exist, is abstract and theoretical." <i>Air Pollution Variance Board</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974). Under circumstances such as these, where probable cause exists, a warrantless examination of the exterior of a car is not unreasonable under the Fourth and Fourteenth Amendments.<sup>[8]</sup></p>
<p>Here, it has been established and is conceded that the police had probable cause to search Lewis' car. An automobile similar in color and model to his car had been seen leaving the scene of the crime. This similarity was corroborated by comparison of the paint scrapings taken from the victim's car with the color and paint of Lewis' automobile. Lewis had had repair work done on his car immediately following the death of the victim. And he had a nexus with Radcliffe on the day of death. All this provided reason to believe that the car was used in the commission of the crime for which Lewis was arrested. <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p></p>
<h2>III</h2>
<p>Concluding, as we have, that the examination of the exterior of the vehicle upon probable cause was reasonable, <span class="star-pagination">*593</span> we have yet to determine whether the prior impoundment of the automobile rendered that examination a violation of the Fourth and Fourteenth Amendments. We do not think that, because the police impounded the car prior to the examination, which they could have made on the spot, there is a constitutional barrier to the use of the evidence obtained thereby. Under the circumstances of this case, the seizure itself was not unreasonable.</p>
<p>Respondent asserts that this case is indistinguishable from <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971). We do not agree. The present case differs from <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> both in the scope of the search<sup>[9]</sup> and in the circumstances of the seizure. Since the Coolidge car was parked on the defendant's driveway, the seizure of that automobile required an entry upon private property. Here, as in <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), the automobile was seized from a public place where access was not meaningfully restricted. This is, in fact, the ground upon which the <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> plurality opinion distinguished <i>Chambers,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 463</a></span> n. 20. See also <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#446" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 446-447</a></span> (1973).</p>
<p>In considering whether the lack of a warrant to seize a vehicle invalidates the otherwise legal examination of the car, <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> is highly pertinent. In <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> four men in an automobile were arrested shortly after an armed robbery. The Court concluded that there was probable cause to arrest and probable cause to search the vehicle. The car was taken from the highway to <span class="star-pagination">*594</span> the police station where, some time later, a search producing incriminating evidence, was conducted. We stated:</p>
<blockquote>"For constitutional purposes, we see no difference between on the one hand seizing and holding a car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. Given probable cause to search, either course is reasonable under the Fourth Amendment.</blockquote>
<blockquote>". . . The probable-cause factor still obtained at the station house and so did the mobility of the car unless the Fourth Amendment permits a warrantless seizure of the car and the denial of its use to anyone until a warrant is secured. In that event there is little to choose in terms of practical consequences between an immediate search without a warrant and the car's immobilization until a warrant is obtained." <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span>.</blockquote>
<p>The fact that the car in <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> was seized after being stopped on a highway, whereas Lewis' car was seized from a public parking lot, has little, if any, legal significance.<sup>[10]</sup> The same arguments and considerations of exigency, immobilization on the spot, and posting a <span class="star-pagination">*595</span> guard obtain. In fact, because the interrogation session ended with awareness that Lewis had been arrested and that his car constituted incriminating evidence, the incentive and potential for the car's removal substantially increased. There was testimony at the federal hearing that Lewis asked one of his attorneys to see that his wife and family got the car, and that the attorney relinquished the keys to the police in order to avoid a physical confrontation. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#33" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 33</a></span>. In <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> all occupants of the car were in custody and there were no means of relating this fact or the location of the car (if it had not been impounded) to a friend or confederate. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> also stated that a search of the car on the spot was impractical because it was dark and the search could not be carefully executed. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 52</a></span> n. 10. Here too, the seizure facilitated the type of close examination necessary.<sup>[11]</sup></p>
<p>Respondent contends that here, unlike <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> probable cause to search the car existed for some time prior to arrest and that, therefore, there were no exigent circumstances. Assuming that probable cause previously existed, we know of no case or principle that suggests that the right to search on probable cause and the reasonableness of seizing a car under exigent circumstances are foreclosed if a warrant was not obtained at the first practicable moment. Exigent circumstances with regard to vehicles are not limited to situations where probable cause is unforeseeable and arises only at the time of arrest. Cf. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, id.,</i> at 50-51</a></span>. The exigency may arise at any time, and the fact that the police might have obtained <span class="star-pagination">*596</span> a warrant earlier does not negate the possibility of a current situation's necessitating prompt police action.<sup>[12]</sup></p>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE POWELL, concurring in the result.</p>
<p>I would reverse the judgment of the Court of Appeals for the reasons set forth in my concurring opinion in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973). As stated therein, I would hold that "federal collateral review of a state prisoner's Fourth Amendment claims claims which rarely bear on innocenceshould be confined solely to the question of whether the petitioner [for habeas corpus] was provided a fair opportunity to raise and have adjudicated the question in state courts." <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Ibid.</a></span></i> In this case there is no contention that respondent was denied a full and fair opportunity to litigate his claim in the state courts.</p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE DOUGLAS, MR. JUSTICE BRENNAN, and MR. JUSTICE MARSHALL join, dissenting.</p>
<p>The most fundamental rule in this area of constitutional law is that "searches conducted outside the judicial process, without prior approval by judge or magistrate, are <i>per se</i> unreasonable under the Fourth Amendment subject only to a few specifically established and well-delineated exceptions." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>. See also <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span>. Since there was no warrant authorizing <span class="star-pagination">*597</span> the search and seizure in this case, and since none of the "specifically established and well-delineated exceptions" to the warrant requirement here existed, I am convinced the judgment of the Court of Appeals must be affirmed.<sup>[1]</sup></p>
<p>In casting about for some way to avoid the impact of our previous decisions, the plurality opinion first suggests, <i>ante,</i> at 588-589, that no "search" really took place in this case, since all that the police did was to scrape paint from the respondent's car and make observations of its tires. Whatever merit this argument might possess in the abstract, it is irrelevant in the circumstances disclosed by this record. The argument is irrelevant for the simple reason that the police, before taking the paint scrapings and looking at the tires, first took possession of the car itself. The Fourth and Fourteenth Amendments protect against "unreasonable searches and <i>seizures,</i>" and there most assuredly was a seizure here.</p>
<p>The plurality opinion next seems to suggest that the basic constitutional rule can be overlooked in this case because the subject of the seizure was an automobile. It is true, of course, that a line of decisions, beginning with <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>, have recognized a so-called "automobile exception" to the constitutional requirement of a warrant. But "[t]he word `automobile' is not a talisman in whose presence the Fourth Amendment fades away and disappears." <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#461" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Coolidge, supra,</i> at 461-462</a></span>. Rather, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine simply recognizes the obviousthat a <i>moving</i> automobile on the open road presents a situation "where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the <span class="star-pagination">*598</span> warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 153</a></span>. See also <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span>. Where there is no reasonable likelihood that the automobile would or could be moved, the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine is simply inapplicable. See, <i>e. g., <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge, supra;</a></span> </i><i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>.</p>
<p>The facts of this case make clear beyond peradventure that the "automobile exception" is not available to uphold the warrantless seizure of the respondent's car. Well before the time that the automobile was seized, the respondentand the keys to his carwere securely within police custody. There was thus absolutely no likelihood that the respondent could have either moved the car or meddled with it during the time necessary to obtain a search warrant. And there was no realistic possibility that anyone else was in a position to do so either. I am at a loss, therefore, to understand the plurality opinion's conclusion, <i>ante,</i> at 595, that there was a "potential for the car's removal" during the period immediately preceding the car's seizure. The facts of record can only support a diametrically opposite conclusion.</p>
<p>Finally, the plurality opinion suggests that other "exigent circumstances" might have excused the failure of the police to procure a warrant. The opinion nowhere states what these mystical exigencies might have been, and counsel for the petitioner has not been so inventive as to suggest any.<sup>[2]</sup> Since the authorities had taken care to procure an arrest warrant even before the respondent <span class="star-pagination">*599</span> arrived for questioning, it can scarcely be said that probable cause was not discovered until so late a point in time as to prevent the obtaining of a warrant for seizure of the automobile. And, with the automobile effectively immobilized during the period of the respondent's interrogation, the fear that evidence might be destroyed was hardly an exigency, particularly when it is remembered that no such fear prompted a seizure during all the preceding months while the respondent, though under investigation, had been in full control of the car.<sup>[3]</sup> This is, quite simply, a case where no exigent circumstances existed.<sup>[4]</sup></p>
<p>Until today it has been clear that "[n]either <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> . . . nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 50</a></span>. I would follow the settled constitutional law established in our decisions and affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[1]  The arrest warrant was obtained in Delaware County, where the crime was committed. The Activities Office is in adjacent Franklin County. In Ohio, an arrest warrant may be served in any county of the State. <span class="citation no-link">Ohio Rev. Code Ann. § 2941.36</span> (1953). In contrast, a search warrant in Ohio may be issued by a judge or magistrate only "within his jurisdiction." <span class="citation no-link">Ohio Rev. Code Ann. § 2933.21</span> (Supp. 1972). Thus, a search warrant obtained in Delaware County is not valid in Franklin County.</p>
<p>[2]  The call was made at about 9:30 a. m. on July 19 by a man who identified himself to Mrs. Smith as Radcliffe and who stated that the books were in "A-1 condition." Mrs. Smith, who knew the victim, did not identify the caller as Radcliffe. Gunshots were heard between 8 a. m. and 8:30 a. m. that day by two women who lived near the site of the crime. It thus became clear that someone had impersonated Radcliffe in making the telephone call.</p>
<p>[3]  The calendar's page for July 19 was missing. Investigation disclosed a writing indentation, on the next and underlying page for July 20, which indicated what had been written on the page for July 19.</p>
<p>[4]  Apparently, the car's trunk was also opened and a tire in the trunk was observed. <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#33" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp. 26, 33</a></span>; <span class="citation" data-id="310138"><a href="/opinion/310138/arthur-ben-lewis-jr-v-harold-j-cardwell-warden/#468" aria-description="Citation for case: Arthur Ben Lewis, Jr. v. Harold J. Cardwell, Warden">476 F. 2d 467, 468</a></span>. No evidence obtained from any part of the interior of the vehicle, however, was introduced.</p>
<p>[5]  The Court there discussed the following post-<i>Carroll</i> cases: <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); <i>Scher</i> v. <i>United States,</i> <span class="citation" data-id="103100"><a href="/opinion/103100/scher-v-united-states/" aria-description="Citation for case: Scher v. United States">305 U. S. 251</a></span> (1938); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949); <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968). Cases decided since <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span></i> and that now might be added to the list include <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973). See also <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968); Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span> (1974).</p>
<p>[6]  Petitioner contends that Lewis' car keys and the parking lot claim check were seized in plain view as an incident to his arrest, and that this seizure served to transfer constructive possession of the vehicle which could then be searched and seized as an instrumentality of the crime. We feel that the District Court and the Court of Appeals were correct in rejecting this argument. Irrespective of the plain-view or instrumentality analyses, the concept of constructive possession has not been found to justify the search or seizure of an item not in actual possession.</p>
<p>[7]  As has been noted, the arrest was made at the Office of the Division of Criminal Activities; but the examination of the vehicle took place some time later at the police impoundment lot. This difference in time and place eliminates any search-incident-to-an-arrest contention.
</p>
<p>"The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crimethings which might easily happen where the weapon or evidence is on the accused's person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964).</p>
<p>See also <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47</a></span> (1970).</p>
<p>[8]  Again, we are not confronted with any issue as to the propriety of a search of a car's interior. "Neither <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span></i> nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords." <i>Id.,</i> at 50.</p>
<p>[9]  <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> concerned a thorough and extensive search of the entire automobile including the interior from which, by vacuum sweepings, incriminating evidence was obtained. A search of that kind raises different and additional considerations not present in the examination of a tire on an operative wheel and in the taking of exterior paint samples from the vehicle in the present case for which there was no reasonable expectation of privacy.</p>
<p>[10]  Before the District Court, the State argued that Lewis had consented to the seizure of his car by requesting that the police impound it for safekeeping. The District Court stated:
</p>
<p>"Viewing the evidence in the light most favorable to the State, petitioner [Lewis] did not clearly and unequivocally consent to the seizure and search of the automobile. The testimony . . . established, at most, that petitioner consented to their taking custody of the car for safekeeping. There is no evidence that petitioner consented, expressly or impliedly, to a seizure of the automobile for purposes of a search. . . ." <span class="citation" data-id="1380337"><a href="/opinion/1380337/lewis-v-cardwell/#37" aria-description="Citation for case: Lewis v. Cardwell">354 F. Supp., at 37-38</a></span>.</p>
<p>Inasmuch as we hold the seizure to be justified under <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>,</i> we do not reach the issue of Lewis' consent.</p>
<p>[11]  To make a comparison with a paint scraping required that a section of the painted exterior that had not been recently repaired be sampled. This conceivably could necessitate several scrapings if the first sample was not conclusive after laboratory analysis. Similarly, to make a cast of the tire tread on the operative wheel would require laboratory equipment.</p>
<p>[12]  We do not address the question found to be determinative in MR. JUSTICE POWELL's opinion concurring in the result. This question was not raised or briefed by the parties.</p>
<p>[1]  This dissent is directed toward the search-and-seizure analysis in MR. JUSTICE BLACKMUN's plurality opinion. Like the plurality, I do not consider the issue raised by MR. JUSTICE POWELL's concurrence, it having been neither briefed nor argued by the parties.</p>
<p>[2]  Even the Solicitor General, who appeared as <i>amicus curiae</i> urging a reversal of the Court of Appeals' judgment in this case, has candidly admitted in his brief that "no satisfactory reason appears for the failure of the law enforcement officers to have obtained a warrant there appears on the facts of this case to have been no real likelihood that respondent would have destroyed or concealed the evidence sought during the time required to seek and procure a warrant." Brief for United States as <i>Amicus Curiae</i> 4-5.</p>
<p>[3]  It can hardly be argued that the questioning of the respondent by the police for the first time alerted him to their intentions, thus suddenly providing him a motivation to remove the car from "official grasp." <i>Ante,</i> at 590, 595. Even putting to one side the question of how the respondent could have acted to destroy any evidence while he was in police custody, the fact is that he was fully aware of official suspicion during several months preceding the interrogation. He had been questioned on several occasions prior to his arrest, and he had been alerted on the day before the interrogation that the police wished to see him. Nonetheless, he voluntarily drove his car to Columbus to keep his appointment with the investigators.</p>
<p>[4]  The plurality opinion correctly rejects, <i>ante,</i> at 591-592, n. 7, the petitioner's contention that the seizure here was incident to the arrest of the respondent. "Once an accused is under arrest and in custody, then a search made at another place, without a warrant; is simply not incident to the arrest." <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>.</p>

</div>
```

---
